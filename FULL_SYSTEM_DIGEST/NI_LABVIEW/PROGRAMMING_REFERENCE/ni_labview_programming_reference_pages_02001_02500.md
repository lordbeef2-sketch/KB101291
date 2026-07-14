# NI_LABVIEW_PROGRAMMING_REFERENCE

<!--SYSTEM_CORPUS id=NI_LABVIEW_PROGRAMMING_REFERENCE format=markdown generated=2026-07-14T12:02:18+00:00 -->
- title: LabVIEW Programming Reference Manual
- source: https://docs-be.ni.com/bundle/labview-api-ref/preprocessedpdf/enus
- source_sha256: 7a54c389b4f3d78e2215f55c9f156124d3668ce61d0d5018094e356004d895ac
- versions: 2024 Q1|2024 Q3|2025 Q1|2025 Q3|2026 Q1
- fidelity: full-text-records

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2001 ordinal=2001 -->
## Functions

Functions


      width specifies the horizontal coordinate that increases to the right.

      •      height —

      height specifies the vertical coordinate that increases to the bottom.


•      polar attributes —

  polar attributes describes the format for the grid and scale of the polar plot and indicates how
  the graph should handle negative magnitude data, whether to clip the data or to draw it.

      •     maximum —

     maximum specifies the maximum value for the scale.

      •     minimum —

     minimum specifies the minimum value for the scale.

      •       clip to min —

       clip to min specifies whether to clip (TRUE) or draw (FALSE) negative magnitude data.

      •       log?(F) —

       log? specifies if the scale is logarithmic.

      •       grid color —

       grid color specifies the color of the grid.

     The default in RGB is 102, 102, 102.

      You can wire a color box constant to this input.

      •       plot color —

       plot color specifies the color of the plot.

     The default in RGB is 0, 255, 0.


                                                   © National Instruments 2001

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2001 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2002 ordinal=2002 -->
## Functions

Functions


               You can wire a color box constant to this input.

                     •      fmt and prec —

               fmt and prec specifies the numeric format and precision for the scale numbers.

                           •      format —

                   format specifies the numeric format for the scale numbers.

                   0      Decimal
                   1        Scientific
                   2       Engineering
                   3       Binary
                   4       Octal
                   5      Hex

                           •       precision —

                     precision specifies the precision for the scale numbers. The default is 1.


                     •       visible section —

                   visible section specifies which quadrant(s) of the polar plot you want to view.

               0  Upper right quadrant
               1  Lower right quadrant
               2  Lower left quadrant
               3  Upper left quadrant
               4  Upper right and left quadrants
               5  Lower right and left quadrants
               6  Right upper and lower quadrants
               7  Left upper and lower quadrants
               8   All quadrants (default)


               •      Lines/Points —


2002   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2002 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2003 ordinal=2003 -->
## Functions

Functions


    Lines/Points sets whether the VI represents the polar data as points or lines between points.

    0              Lines
    1              Points

   •       Size —

    Size specifies the size, in pixels, of the lines or points this VI plots.

   •     new picture —

   new picture is the picture that contains the plot. You can wire this output to any other picture
    input to add more drawing instructions to the picture.

    You also can wire this output to the Picture to Pixmap VI to obtain an image data cluster. You
    then can save the image data to a file using the Graphics Formats VIs.


Examples

Refer to the following example files included with LabVIEW.

  • labview\examples\Graphics and Sound\Picture Plots\Simple
   Polar Plot.vi

SmithSmith PlotPlot

Takes a picture and the data for a Smith plot and appends a picture that represents the
Smith plot of the data.


                                                    © National Instruments 2003

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2003 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2004 ordinal=2004 -->
## Functions

Functions

      Inputs/Outputs

               •       [user-specified font] —

             [user-specified font] specifies the specific font characteristics for the text to draw.

          The VI ignores this input unless desired font is User-specified Font.

                     •      Font Name: —

               Font Name specifies the font to use for the text.

                           If you misspell the font name or specify a font that is not installed on the computer, the
                operating system selects a font.

                     •       Size —

                 Size specifies the size of the font in points.

                     •       Strikeout? —

                 Strikeout? specifies if the text appears in strikeout. If Strikeout? is TRUE, the text appears in
                   strikeout.

                     •        Italic? —

                    Italic? specifies if the text appears in italics. If Italic? is TRUE, the text appears in italics.

                     •      Underline? —

                Underline? specifies if the text is underlined. If Underline? is TRUE, the text appears
                 underlined.

                     •      Outline? —

                Outline? specifies if the text is outlined. If Outline? is TRUE, the text appears outlined.

                     •     Shadow? —

             Shadow? specifies if the text has a shadow. If Shadow? is TRUE, the text appears in shadow.

                     •      Bold? —


2004   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2004 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2005 ordinal=2005 -->
## Functions

Functions


      Bold? specifies if the text is bold. If Bold? is TRUE, the text appears bold.


•      desired font(Application) —

  desired font specifies the text font.

  0     User-specified Font
        Application Font  1         (default)
  2    System Font
  3     Dialog Font

•       picture —

  picture is the picture to which you want to add the plot. The default is an empty picture.

•      smith plot —

  smith plot is an array of points, where each point is a cluster containing the rand xvalues that
  make up the complex impedance, z, of r+ jx.

      •        r —

        r is the resistance component of the complex impedance.

      •      x —

      x is the reactance component of the complex impedance.


•      dimensions (w,h) —

  dimensions specifies the top left point of the drawn bitmap.

      •      width —

      width specifies the horizontal coordinate that increases to the right.

      •      height —


                                                   © National Instruments 2005

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2005 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2006 ordinal=2006 -->
## Functions

Functions


                height specifies the vertical coordinate that increases to the bottom.


               •      dimensions incl scales? (T) —

           dimensions incl scales? indicates whether the dimensions input includes the scales, in addition
             to the plot area.

                    If FALSE, the dimensions input describes the plot area, and the VI draws the scales outside of the
             rectangle. If TRUE (default), the VI draws the scales inside of dimensions and insets the plot area
             to make room for the text.

               •      top left point(0, 0) —

           top left point specifies in coordinates where to place the top-left corner of the image in the new
             picture.

                     •      x —

               x is the horizontal coordinate that increases to the right.

                     •      y —

               y is the vertical coordinate that increases to the bottom.


               •      smith plot section —

           smith plot section describes the portion of the graph you want to display.

                  It contains four values that represent a rectangle superimposed over the Smith plot.

                     •      x minimum —

               x minimum is the smallest allowable value in the range of horizontal coordinates.

                     •      x maximum —

               x maximum is the largest allowable value in the range of horizontal coordinates.

                     •      y minimum —


2006   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2006 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2007 ordinal=2007 -->
## Functions

Functions


      y minimum is the smallest allowable value in the range of vertical coordinates.

      •      y maximum —

      y maximum is the largest allowable value in the range of vertical coordinates.


•      smith plot cosmetics —

  smith plot cosmetics specifies the style to use in drawing the plot.

      •       Plot Style —

       Plot Style is the style of plot to display.

     The default is a plot of lines and points.

      •      Line Color —

      Line Color is the color of the line.

     The default in RGB is 0, 153, 255.

      You can wire a color box constant to this input.

      •      Point Color —

      Point Color is the color of the points.

     The default in RGB is 0, 153, 255.

      You can wire a color box constant to this input.


•      smith grid cosmetics —

  smith grid cosmetics describes the style to use for the grids.

      •     R color —

     R color specifies the color of the resistance, r, circles for the grids.


                                                   © National Instruments 2007

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2007 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2008 ordinal=2008 -->
## Functions

Functions


                     •     R grids —

            R grids specifies to draw the resistance, r, circles for the grids.

                     •     X color —

              X color specifies the color of the reactance, x, circles for the grids.

                     •     X grids —

              X grids specifies to draw the reactance, x, circles for the grids.

                     •      Labels —

                Labels specifies to draw labels in the plot corners when you zoom in on a section of the
                   plot.


               •     new picture —

         new picture is the picture that contains the plot. You can wire this output to any other picture
            input to add more drawing instructions to the picture.

           You also can wire this output to the Picture to Pixmap VI to obtain an image data cluster. You
           then can save the image data to a file using the Graphics Formats VIs.


     Examples

       Refer to the following example files included with LabVIEW.

            • labview\examples\Graphics and Sound\Picture Plots\Simple
        Smith Plot.vi

      SmithSmith MultiMulti PlotPlot

      Takes a picture and an array of Smith plots and appends a picture that represents the
      superimposed Smith plots of the data.


2008   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2008 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2009 ordinal=2009 -->
## Functions

Functions


Inputs/Outputs

   •       [user-specified font] —

    [user-specified font] specifies the specific font characteristics for the text to draw.

    The VI ignores this input unless desired font is User-specified Font.

         •      Font Name: —

        Font Name specifies the font to use for the text.

              If you misspell the font name or specify a font that is not installed on the computer, the
        operating system selects a font.

         •       Size —

         Size specifies the size of the font in points.

         •       Strikeout? —

         Strikeout? specifies if the text appears in strikeout. If Strikeout? is TRUE, the text appears in
          strikeout.

         •        Italic? —

          Italic? specifies if the text appears in italics. If Italic? is TRUE, the text appears in italics.

         •      Underline? —

        Underline? specifies if the text is underlined. If Underline? is TRUE, the text appears
         underlined.

         •      Outline? —


                                                    © National Instruments 2009

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2009 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2010 ordinal=2010 -->
## Functions

Functions


                Outline? specifies if the text is outlined. If Outline? is TRUE, the text appears outlined.

                     •     Shadow? —

             Shadow? specifies if the text has a shadow. If Shadow? is TRUE, the text appears in shadow.

                     •      Bold? —

               Bold? specifies if the text is bold. If Bold? is TRUE, the text appears bold.


               •      desired font(Application) —

            desired font specifies the text font.

           0     User-specified Font
                   Application Font           1
                    (default)
           2    System Font
           3     Dialog Font

               •       picture —

             picture is the picture to which you want to add the plot. The default is an empty picture.

               •       rect —

             rect contains the upper-left and lower-right coordinates that describe a rectangle bounding the
               text.

          The VI clips text to the coordinates of this rectangle. Horizontal coordinates increase to the right,
          and vertical coordinates increase to the bottom.

                     •        left —

                     left is the horizontal coordinate of the left edge of the rectangle.

                     •      top —

               top is the vertical coordinate of the top edge of the rectangle.


2010   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2010 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2011 ordinal=2011 -->
## Functions

Functions


      •       right —

       right is the horizontal coordinate of the right edge of the rectangle.

      •     bottom —

     bottom is the vertical coordinate of the bottom edge of the rectangle.


•      smith plot section —

  smith plot section describes the portion of the graph you want to display.

   It contains four values that represent a rectangle superimposed over the Smith plot.

      •      x minimum —

      x minimum is the smallest allowable value in the range of horizontal coordinates.

      •      x maximum —

      x maximum is the largest allowable value in the range of horizontal coordinates.

      •      y minimum —

      y minimum is the smallest allowable value in the range of vertical coordinates.

      •      y maximum —

      y maximum is the largest allowable value in the range of vertical coordinates.


•      smith grid cosmetics —

  smith grid cosmetics describes the style to use for the grids.

      •     R color —

     R color specifies the color of the resistance, r, circles for the grids.

      •     R grids —


                                                   © National Instruments 2011

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2011 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2012 ordinal=2012 -->
## Functions

Functions


            R grids specifies to draw the resistance, r, circles for the grids.

                     •     X color —

              X color specifies the color of the reactance, x, circles for the grids.

                     •     X grids —

              X grids specifies to draw the reactance, x, circles for the grids.

                     •      Labels —

                Labels specifies to draw labels in the plot corners when you zoom in on a section of the
                   plot.


               •      smith multi plot —

           smith multi plot is an array of clusters, where each cluster contains an array of points.

          A point is represented by a cluster containing the rand xvalues that make up the complex
           impedance r+ jx.

                     •      smith plot —

               smith plot is an array of points, where each point is a cluster containing the rand xvalues
                 that make up the complex impedance, z, of r+ jx.

                           •        r —

                         r is the resistance component of the complex impedance.

                           •      x —

                   x is the reactance component of the complex impedance.


               •      smith plot cosmetics —

           smith plot cosmetics specifies the style to use in drawing the plot.


2012   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2012 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2013 ordinal=2013 -->
## Functions

Functions


      •       Plot Style —

       Plot Style is the style of plot to display.

     The default is a plot of lines and points.

      •      Line Color —

      Line Color is the color of the line.

     The default in RGB is 0, 153, 255.

      You can wire a color box constant to this input.

      •      Point Color —

      Point Color is the color of the points.

     The default in RGB is 0, 153, 255.

      You can wire a color box constant to this input.


•      dimensions incl scales? (T) —

  dimensions incl scales? indicates whether the rect input includes the scales, in addition to the
  plot area.

   If FALSE, the rect input describes the plot area, and the VI draws the scales outside of the
  rectangle. If TRUE, the VI draws the scales inside of rect and insets the plot area to make room
  for the text.

•     new picture —

  new picture is the picture that contains the plot. You can wire this output to any other picture
  input to add more drawing instructions to the picture.

  You also can wire this output to the Picture to Pixmap VI to obtain an image data cluster. You
  then can save the image data to a file using the Graphics Formats VIs.


                                                   © National Instruments 2013

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2013 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2014 ordinal=2014 -->
## Functions

Functions

     Examples

       Refer to the following example files included with LabVIEW.

            • labview\examples\Graphics and Sound\Picture Plots\Smith
        Multi Plot with Styles.vi

      NormalizeNormalize SmithSmith PlotPlot

      Takes data for a Smith plot and normalizes it, meaning that the data is scaled relative
       to a known value.


      Inputs/Outputs

               •     Zo (50.0) —

          Zo is the characteristic impedance of the system.

               •      points {r,x} —

            points {r,x} is an array of points, where each point is a cluster containing the rand xvalues that
          make up the complex impedance r+ jx.

                     •        r —

                    r is the resistance component of the complex impedance.

                     •      x —

               x is the reactance component of the complex impedance.


               •      points complex —

            points complex is an array of complex numbers.

               •      normalized smith points {r,x} —


2014   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2014 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2015 ordinal=2015 -->
## Functions

Functions


    normalized smith points {r,x} is an array of clusters of points containing the normalized data.
    Each cluster contains an rand an xvalue.

         •        r —

          r is the resistance component of the complex impedance.

         •      x —

        x is the reactance component of the complex impedance.


You can wire an array of points to this VI, where each point is a cluster of an rand an x
value, or you can wire an array of complex data to this VI. The VI detects which data
input you wire and uses that input. If you wire both inputs, the VI normalizes the array
of points.

This VI normalizes the data with respect to a specified characteristic impedance, Zo, of
the system. Then it returns the resulting data as an array of clusters of points, where
each cluster contains an rand an xvalue. You can wire the normalized smith points
output directly to the Smith Plot VI.

Examples

Refer to the following example files included with LabVIEW.

  • labview\examples\Graphics and Sound\Picture Plots\Smith
   Multi Plot with Styles.vi

PlotPlot XYXY

Takes a picture and an array of points and appends a picture that represents an XY
graph of the data.

To create controls for the cluster inputs in this VI, right-click the cluster terminal and
select Create»Control from the shortcut menu.


                                                    © National Instruments 2015

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2015 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2016 ordinal=2016 -->
## Functions

Functions


      Inputs/Outputs

               •       [user-specified font] —

             [user-specified font] specifies the specific font characteristics for the text to draw.

          The VI ignores this input unless desired font is User-specified Font.

                     •      Font Name: —

               Font Name specifies the font to use for the text.

                           If you misspell the font name or specify a font that is not installed on the computer, the
                operating system selects a font.

                     •       Size —

                 Size specifies the size of the font in points.

                     •       Strikeout? —

                 Strikeout? specifies if the text appears in strikeout. If Strikeout? is TRUE, the text appears in
                   strikeout.

                     •        Italic? —

                    Italic? specifies if the text appears in italics. If Italic? is TRUE, the text appears in italics.

                     •      Underline? —

                Underline? specifies if the text is underlined. If Underline? is TRUE, the text appears
                 underlined.


2016   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2016 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2017 ordinal=2017 -->
## Functions

Functions


      •      Outline? —

      Outline? specifies if the text is outlined. If Outline? is TRUE, the text appears outlined.

      •     Shadow? —

     Shadow? specifies if the text has a shadow. If Shadow? is TRUE, the text appears in shadow.

      •      Bold? —

      Bold? specifies if the text is bold. If Bold? is TRUE, the text appears bold.


•      desired font(Application) —

  desired font specifies the text font.

  0     User-specified Font
        Application Font  1         (default)
  2    System Font
  3     Dialog Font

•       picture —

  picture is the picture to which you want to add the graph. The default is an empty picture.

•      data —

  data is an array of points, where each point is a cluster of x and y pixel coordinates.

      •      x —

      x is the horizontal coordinate that increases to the right.

      •      y —

      y is the vertical coordinate that increases to the bottom.


•      dimensions (w,h) —


                                                   © National Instruments 2017

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2017 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2018 ordinal=2018 -->
## Functions

Functions


           dimensions specifies the top left point of the drawn bitmap.

                     •      width —

               width specifies the horizontal coordinate that increases to the right.

                     •      height —

                height specifies the vertical coordinate that increases to the bottom.


               •      top left point(0, 0) —

           top left point specifies in coordinates where to place the top-left corner of the image in the new
             picture.

                     •      x —

               x is the horizontal coordinate that increases to the right.

                     •      y —

               y is the vertical coordinate that increases to the bottom.


               •       cartesian axis attributes —

            cartesian axis attributes specifies the range and format for the x- and y- axes.

                    If the minimum and maximum values are the same, or if you do not wire the cartesian axis
             attributes input, the VI calculates the minimum and maximum values from the data.

                     •      x minimum —

               x minimum is the smallest allowable value in the range of horizontal coordinates.

                     •      x maximum —

               x maximum is the largest allowable value in the range of horizontal coordinates.

                     •      x log? —


2018   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2018 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2019 ordinal=2019 -->
## Functions

Functions


  x log? indicates whether the scale should be logarithmic.

•      x precision —

  x precision specifies the precision for the scale numbers on the x-axis.

•      x format —

  x format specifies the numeric format for the scale numbers on the x-axis. The default is
  Decimal.

  0       Decimal
  1        Scientific
  2       Engineering
  3       Binary
  4       Octal
  5      Hex

•      y minimum —

  y minimum is the smallest allowable value in the range of vertical coordinates.

•      y maximum —

  y maximum is the largest allowable value in the range of vertical coordinates.

•      y log? —

  y log? indicates whether the scale should be logarithmic.

•      y precision —

  y precision specifies the precision for the scale numbers on the y-axis.

•      y format —

  y format specifies the numeric format for the scale numbers on the y-axis. The default is
  Decimal.

  0       Decimal


                                                © National Instruments 2019

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2019 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2020 ordinal=2020 -->
## Functions

Functions


               1        Scientific
               2       Engineering
               3       Binary
               4       Octal
               5      Hex


               •       cartesian grid cosmetics —

            cartesian grid cosmetics specifies the style for the grid of the graph.

                     •       line color —

                  line color specifies the color of the line.

               You can wire a color box constant to this input.

                     •       text color —

                  text color specifies the color of the text.

               You can wire a color box constant to this input.

                     •       tick length(3) —

                  tick length specifies the length of the tick marks on the edge of the scale.

                     •      crossing axes —

                 crossing axes specifies if the VI draws the axes at the originating coordinate. If crossing axes
                      is TRUE, the VI draws the axes at the originating coordinate. If crossing axes is FALSE, the VI
               draws the axes at the bottom left edge of the plot.

                     •       visible grid? —

                   visible grid? specifies if the VI displays the grid in the graph. If visible grid? is TRUE, the VI
                 displays the grid in the graph.


               •      XY plot cosmetics —

           XY plot cosmetics specifies the plot color, the style for the plot, and the baseline. This VI uses the


2020   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2020 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2021 ordinal=2021 -->
## Functions

Functions


  baseline only if the XY plot type is comb plot.

      •       plot color —

       plot color specifies the color of the plot.

     The default in RGB is 255, 255, 0.

      You can wire a color box constant to this input.

      •      XY plot type —

      XY plot type specifies the style of plot to display.

      0   points
      1   squares
      2   circles
      3   connected points (default)
      4   connected squares
      5   connected circles
      6  comb plot
      7   sized scatter plot
      8   sized-colored scatter plot
      9  min-max lines

      •      baseline —

      baseline specifies the baseline of a plot. The default is 0.


•       [sized scatter plot cosmetics] —

  sized scatter plot cosmetics specifies the range of sizes for frequency distribution points,
  assuming the xy plot type is sized scatter plot or sized-colored scatter plot.

      •     min size —

     min size specifies the smallest size to be used for points in a scatter plot.

      •     max size —


                                                   © National Instruments 2021

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2021 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2022 ordinal=2022 -->
## Functions

Functions


            max size specifies the largest size to be used for points in a scatter plot.

                     •     maps to max size —

             maps to max size defines the maximum size to which the uppermost point in the scatter
                  plot can be mapped.

                     •       color array —

                 color array maps specific colors for points of each size.


               •     new picture —

         new picture is the picture that contains the plot. You can wire this output to any other picture
            input to add more drawing instructions to the picture.

           You also can wire this output to the Picture to Pixmap VI to obtain an image data cluster. You
           then can save the image data to a file using the Graphics Formats VIs.


       This VI ignores the values of the x minimum, x maximum, y minimum, and y
     maximum subparameters of the cartesian axis attributes input. The VI ignores the
      subparameters because it automatically scales the axes. Use the Plot Multi-XY VI if you
      do not want to use automatic scaling.

     Examples

       Refer to the following example files included with LabVIEW.

            • labview\examples\Graphics and Sound\Picture Plots\
        Waveform and XY Plots.vi
            • labview\examples\Graphics and Sound\Picture Plots\
        Artificial Strip Chart.vi

       PlotPlot Multi-XYMulti-XY

      Takes a picture and an array of plots and appends a picture of an XY graph of the data
       with the plots overlaid on the same graph.


2022   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2022 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2023 ordinal=2023 -->
## Functions

Functions

Each plot is an array of points.


Inputs/Outputs

   •       [user-specified font] —

    [user-specified font] specifies the specific font characteristics for the text to draw.

    The VI ignores this input unless desired font is User-specified Font.

         •      Font Name: —

        Font Name specifies the font to use for the text.

              If you misspell the font name or specify a font that is not installed on the computer, the
        operating system selects a font.

         •       Size —

         Size specifies the size of the font in points.

         •       Strikeout? —

         Strikeout? specifies if the text appears in strikeout. If Strikeout? is TRUE, the text appears in
          strikeout.

         •        Italic? —

          Italic? specifies if the text appears in italics. If Italic? is TRUE, the text appears in italics.

         •      Underline? —


                                                    © National Instruments 2023

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2023 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2024 ordinal=2024 -->
## Functions

Functions


                Underline? specifies if the text is underlined. If Underline? is TRUE, the text appears
                 underlined.

                     •      Outline? —

                Outline? specifies if the text is outlined. If Outline? is TRUE, the text appears outlined.

                     •     Shadow? —

             Shadow? specifies if the text has a shadow. If Shadow? is TRUE, the text appears in shadow.

                     •      Bold? —

               Bold? specifies if the text is bold. If Bold? is TRUE, the text appears bold.


               •      desired font(Application) —

            desired font specifies the text font.

           0     User-specified Font
                   Application Font
           1                    (default)
           2    System Font
           3     Dialog Font

               •       picture —

             picture is the picture to which you want to add the plot. The default is an empty picture.

               •      data —

           data is an array of clusters of plots, where each plot is an array of points.

                     •      data —

               data is an array of clusters of plots, where each plot is an array of points.

                           •      x —


2024   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2024 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2025 ordinal=2025 -->
## Functions

Functions


          x is the horizontal coordinate that increases to the right.

             •      y —

          y is the vertical coordinate that increases to the bottom.


•      dimensions (w,h) —

  dimensions specifies the top left point of the drawn bitmap.

      •      width —

      width specifies the horizontal coordinate that increases to the right.

      •      height —

      height specifies the vertical coordinate that increases to the bottom.


•      top left point(0, 0) —

  top left point specifies in coordinates where to place the top-left corner of the image in the new
  picture.

      •      x —

      x is the horizontal coordinate that increases to the right.

      •      y —

      y is the vertical coordinate that increases to the bottom.


•       cartesian axis attributes —

  cartesian axis attributes specifies the range and format for the x- and y- axes.

   If the minimum and maximum values are the same, or if you do not wire the cartesian axis
  attributes input, the VI calculates the minimum and maximum values from the data.


                                                   © National Instruments 2025

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2025 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2026 ordinal=2026 -->
## Functions

Functions


                     •      x minimum —

               x minimum is the smallest allowable value in the range of horizontal coordinates.

                     •      x maximum —

               x maximum is the largest allowable value in the range of horizontal coordinates.

                     •      x log? —

               x log? indicates whether the scale should be logarithmic.

                     •      x precision —

               x precision specifies the precision for the scale numbers on the x-axis.

                     •      x format —

               x format specifies the numeric format for the scale numbers on the x-axis. The default is
             Decimal.

               0       Decimal
               1        Scientific
               2       Engineering
               3       Binary
               4       Octal
               5      Hex

                     •      y minimum —

               y minimum is the smallest allowable value in the range of vertical coordinates.

                     •      y maximum —

               y maximum is the largest allowable value in the range of vertical coordinates.

                     •      y log? —

               y log? indicates whether the scale should be logarithmic.

                     •      y precision —


2026   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2026 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2027 ordinal=2027 -->
## Functions

Functions


      y precision specifies the precision for the scale numbers on the y-axis.

      •      y format —

      y format specifies the numeric format for the scale numbers on the y-axis. The default is
     Decimal.

      0       Decimal
      1        Scientific
      2       Engineering
      3       Binary
      4       Octal
      5      Hex


•       cartesian grid cosmetics —

  cartesian grid cosmetics specifies the style for the grid of the graph.

      •       line color —

       line color specifies the color of the line.

      You can wire a color box constant to this input.

      •       text color —

       text color specifies the color of the text.

      You can wire a color box constant to this input.

      •       tick length(3) —

       tick length specifies the length of the tick marks on the edge of the scale.

      •      crossing axes —

      crossing axes specifies if the VI draws the axes at the originating coordinate. If crossing axes
         is TRUE, the VI draws the axes at the originating coordinate. If crossing axes is FALSE, the VI
      draws the axes at the bottom left edge of the plot.


                                                   © National Instruments 2027

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2027 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2028 ordinal=2028 -->
## Functions

Functions


                     •       visible grid? —

                   visible grid? specifies if the VI displays the grid in the graph. If visible grid? is TRUE, the VI
                 displays the grid in the graph.


               •      XY plot cosmetics —

           XY plot cosmetics specifies the plot color, the style for the plot, and the baseline. This VI uses the
            baseline only if the XY plot type is comb plot.

                     •       plot color —

                 plot color specifies the color of the plot.

              The default in RGB is 255, 255, 0.

               You can wire a color box constant to this input.

                     •      XY plot type —

              XY plot type specifies the style of plot to display.

               0   points
               1   squares
               2   circles
               3   connected points (default)
               4   connected squares
               5   connected circles
               6  comb plot
               7   sized scatter plot
               8   sized-colored scatter plot
               9  min-max lines

                     •      baseline —

                baseline specifies the baseline of a plot. The default is 0.


               •       [sized scatter plot cosmetics] —


2028   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2028 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2029 ordinal=2029 -->
## Functions

Functions


    sized scatter plot cosmetics specifies the range of sizes for frequency distribution points,
    assuming the xy plot type is sized scatter plot or sized-colored scatter plot.

         •     min size —

       min size specifies the smallest size to be used for points in a scatter plot.

         •     max size —

      max size specifies the largest size to be used for points in a scatter plot.

         •     maps to max size —

      maps to max size defines the maximum size to which the uppermost point in the scatter
         plot can be mapped.

         •       color array —

         color array maps specific colors for points of each size.


   •     new picture —

   new picture is the picture that contains the plot. You can wire this output to any other picture
    input to add more drawing instructions to the picture.

    You also can wire this output to the Picture to Pixmap VI to obtain an image data cluster. You
    then can save the image data to a file using the Graphics Formats VIs.


Examples

Refer to the following example files included with LabVIEW.

  • labview\examples\Graphics and Sound\Picture Plots\XY
   Multi Plot.vi

PlotPlot WaveformWaveform

Takes uniformly distributed data and a picture and creates a new picture that
represents a waveform graph of the data.


                                                    © National Instruments 2029

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2029 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2030 ordinal=2030 -->
## Functions

Functions


      Inputs/Outputs

               •       [user-specified font] —

             [user-specified font] specifies the specific font characteristics for the text to draw.

          The VI ignores this input unless desired font is User-specified Font.

                     •      Font Name: —

               Font Name specifies the font to use for the text.

                           If you misspell the font name or specify a font that is not installed on the computer, the
                operating system selects a font.

                     •       Size —

                 Size specifies the size of the font in points.

                     •       Strikeout? —

                 Strikeout? specifies if the text appears in strikeout. If Strikeout? is TRUE, the text appears in
                   strikeout.

                     •        Italic? —

                    Italic? specifies if the text appears in italics. If Italic? is TRUE, the text appears in italics.

                     •      Underline? —

                Underline? specifies if the text is underlined. If Underline? is TRUE, the text appears
                 underlined.

                     •      Outline? —


2030   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2030 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2031 ordinal=2031 -->
## Functions

Functions


      Outline? specifies if the text is outlined. If Outline? is TRUE, the text appears outlined.

      •     Shadow? —

     Shadow? specifies if the text has a shadow. If Shadow? is TRUE, the text appears in shadow.

      •      Bold? —

      Bold? specifies if the text is bold. If Bold? is TRUE, the text appears bold.


•      desired font(Application) —

  desired font specifies the text font.

  0     User-specified Font
        Application Font  1
         (default)
  2    System Font
  3     Dialog Font

•       picture —

  picture is the picture to which you want to add the graph. The default is an empty picture.

•      bounding rect —

  bounding rect contains the upper-left and lower-right coordinates that describe a rectangle
  bounding the plot, including the x- and y-axes.

  Horizontal coordinates increase to the right, and vertical coordinates increase to the bottom.

      •        left —

        left is the horizontal coordinate of the left edge of the rectangle.

      •      top —

      top is the vertical coordinate of the top edge of the rectangle.

      •       right —


                                                   © National Instruments 2031

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2031 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2032 ordinal=2032 -->
## Functions

Functions


                  right is the horizontal coordinate of the right edge of the rectangle.

                     •     bottom —

              bottom is the vertical coordinate of the bottom edge of the rectangle.


               •       cartesian axis attributes —

            cartesian axis attributes specifies the range and format for the x- and y- axes.

                    If the minimum and maximum values are the same, or if you do not wire the cartesian axis
             attributes input, the VI calculates the minimum and maximum values from the data.

                     •      x minimum —

               x minimum is the smallest allowable value in the range of horizontal coordinates.

                     •      x maximum —

               x maximum is the largest allowable value in the range of horizontal coordinates.

                     •      x log? —

               x log? indicates whether the scale should be logarithmic.

                     •      x precision —

               x precision specifies the precision for the scale numbers on the x-axis.

                     •      x format —

               x format specifies the numeric format for the scale numbers on the x-axis. The default is
             Decimal.

               0       Decimal
               1        Scientific
               2       Engineering
               3       Binary
               4       Octal


2032   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2032 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2033 ordinal=2033 -->
## Functions

Functions


      5      Hex

      •      y minimum —

      y minimum is the smallest allowable value in the range of vertical coordinates.

      •      y maximum —

      y maximum is the largest allowable value in the range of vertical coordinates.

      •      y log? —

      y log? indicates whether the scale should be logarithmic.

      •      y precision —

      y precision specifies the precision for the scale numbers on the y-axis.

      •      y format —

      y format specifies the numeric format for the scale numbers on the y-axis. The default is
     Decimal.

      0       Decimal
      1        Scientific
      2       Engineering
      3       Binary
      4       Octal
      5      Hex


•     waveform data —

  waveform data contains the initial X value, the spacing between points along the x-axis, and the
  y data that you want to plot.

      •      Xo(0) —

     Xo is the initial value of x.


                                                   © National Instruments 2033

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2033 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2034 ordinal=2034 -->
## Functions

Functions


              The default is 0.

                     •       delta X(1) —

                 delta X determines the spacing between points along the x-axis.

              The default is 1.

                     •      Y data —

               Y data specifies the data that you want to plot along the y-axis.


               •       cartesian grid cosmetics —

            cartesian grid cosmetics specifies the style for the grid of the graph.

                     •       line color —

                  line color specifies the color of the line.

               You can wire a color box constant to this input.

                     •       text color —

                  text color specifies the color of the text.

               You can wire a color box constant to this input.

                     •       tick length(3) —

                  tick length specifies the length of the tick marks on the edge of the scale.

                     •      crossing axes —

                 crossing axes specifies if the VI draws the axes at the originating coordinate. If crossing axes
                      is TRUE, the VI draws the axes at the originating coordinate. If crossing axes is FALSE, the VI
               draws the axes at the bottom left edge of the plot.

                     •       visible grid? —


2034   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2034 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2035 ordinal=2035 -->
## Functions

Functions


       visible grid? specifies if the VI displays the grid in the graph. If visible grid? is TRUE, the VI
       displays the grid in the graph.


•     waveform plot cosmetics —

  waveform plot cosmetics specifies the plot color, the style for the plot, and the baseline. The VI
  uses the baseline only if the waveform plot type is comb plot or bar plot.

      •       plot color —

       plot color specifies the color of the plot.

     The default in RGB is 255, 255, 0.

      You can wire a color box constant to this input.

      •     waveform plot type —

     waveform plot type is the style of plot to display.

     The default is a plot of connected points.

      0    points
      1    squares
      2     circles
           connected points
      3              (default)
      4    connected squares
      5    connected circles
      6        fill to baselines
      7   comb plot
      8    bar plot

      •      baseline —

      baseline specifies the baseline of a plot. The default is 0.


•       [bar style] —


                                                   © National Instruments 2035

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2035 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2036 ordinal=2036 -->
## Functions

Functions


           bar style specifies the style for bar plots, assuming the waveform plot type is bar plot.

                     •      bar width(50%) —

               bar width specifies the width of each bar relative to the rest of the graph.

                     •      frame?(T) —

               frame? indicates whether to include a frame around the bars in the graph.

                     •      frame color(black) —

               frame color is the color of the bars in the graph.

              The default is black.

               You can wire a color box constant to this input.


               •     new picture —

         new picture is the picture that contains the plot. You can wire this output to any other picture
            input to add more drawing instructions to the picture.

           You also can wire this output to the Picture to Pixmap VI to obtain an image data cluster. You
           then can save the image data to a file using the Graphics Formats VIs.


     Examples

       Refer to the following example files included with LabVIEW.

            • labview\examples\Graphics and Sound\Picture Plots\
        Waveform and XY Plots.vi
            • labview\examples\Graphics and Sound\Picture Plots\
        Histogram Plot.vi

      RadarRadar PlotPlot

      Takes a picture and an array of plots and appends a picture that represents the radar
       plot of the data.

2036   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2036 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2037 ordinal=2037 -->
## Functions

Functions

You can use a radar plot to compare the performance of one set of data with another
set of data. This VI uses the Draw Legend VI as a subVI.


Inputs/Outputs

   •       [user-specified font] —

    [user-specified font] specifies the specific font characteristics for the text to draw.

    The VI ignores this input unless desired font is User-specified Font.

         •      Font Name: —

        Font Name specifies the font to use for the text.

              If you misspell the font name or specify a font that is not installed on the computer, the
        operating system selects a font.

         •       Size —

         Size specifies the size of the font in points.

         •       Strikeout? —

         Strikeout? specifies if the text appears in strikeout. If Strikeout? is TRUE, the text appears in
          strikeout.

         •        Italic? —

          Italic? specifies if the text appears in italics. If Italic? is TRUE, the text appears in italics.

         •      Underline? —


                                                    © National Instruments 2037

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2037 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2038 ordinal=2038 -->
## Functions

Functions


                Underline? specifies if the text is underlined. If Underline? is TRUE, the text appears
                 underlined.

                     •      Outline? —

                Outline? specifies if the text is outlined. If Outline? is TRUE, the text appears outlined.

                     •     Shadow? —

             Shadow? specifies if the text has a shadow. If Shadow? is TRUE, the text appears in shadow.

                     •      Bold? —

               Bold? specifies if the text is bold. If Bold? is TRUE, the text appears bold.


               •      desired font(Application) —

            desired font specifies the text font.

           0     User-specified Font
                   Application Font
           1                    (default)
           2    System Font
           3     Dialog Font

               •       picture —

             picture is the picture to which you want to add the plot. The default is an empty picture.

               •      data —

           data is a 2D array, where each row represents a plot.

          The VI draws each index in a plot on a corresponding y-scale. A straight line connects all the
            points in a plot.

               •       plot info —

             plot info specifies the name, color, and fill option for each plot.

          The index of this array matches the row index in data.


2038   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2038 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2039 ordinal=2039 -->
## Functions

Functions


  The VI uses plot name and plot color for the legend.

      •       plot name —

       plot name is the name of the plot.

      •       plot color (white) —

       plot color is the color of the plot.

     The default in RGB is white.

      You can wire a color box constant to this input.

      •        fill?(F) —

         fill? specifies whether to fill the interior.

          If FALSE (default), the VI draws only the outlines.


•       axis info —

  axis info specifies the label (name) of each y-axis and the minimum and maximum value of each
   y-axis.

  The index of this array matches the column index in data.

      •       label —

       label is the label of the y-axis.

      •     max value —

     max value is the maximum value of the y-axis.

      •     min value —

     min value is the minimum value of the y-axis.


•      axes info —


                                                   © National Instruments 2039

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2039 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2040 ordinal=2040 -->
## Functions

Functions


           axes info specifies the color, format and precision of the y-axes, and whether to autoscale the y-
             axes.

                     •       color (white) —

                 color is the color for all the y-axes.

              The default in RGB is 255, 255, 255.

               You can wire a color box constant to this input.

                     •      format and precision —

               format and precision specifies the format of the values on the y-axes.

                           •      format —

                   format specifies the numeric format for the scale numbers.

                   0      Decimal
                   1        Scientific
                   2       Engineering
                   3       Binary
                   4       Octal
                   5      Hex

                           •       precision —

                     precision specifies the precision for the scale numbers. The default is 1.


                     •      autoscale? (false) —

                autoscale? specifies whether to autoscale each y-axis independently.

                           If FALSE (default), the VI does not autoscale each y-axis.


               •      legend info —

           legend info specifies the location of the plot legend relative to the radar plot.


2040   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2040 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2041 ordinal=2041 -->
## Functions

Functions


      •      position (none) —

       position specifies where to draw the legend.

      0 None (default)—The VI does not draw the legend.
      1 Top
      2 Right
      3 Bottom
      4 Left

      •       text color(white) —

       text color is the color of the labels of the y-axes, as shown in the legend.

     The default in RGB is 255, 255, 255.

      You can wire a color box constant to this input.


•      dimension (w,h) —

  dimension (w,h) specifies the rectangle in coordinates into which the VI draws the radar plot
  and legend.

      •      Width —

      Width is the horizontal coordinate that increases to the right.

      •      Height —

      Height is the vertical coordinate that increases to the bottom.


•      top left point(0, 0) —

  top left point specifies in coordinates where to place the top-left corner of the image in the new
  picture.

      •      x —

      x is the horizontal coordinate that increases to the right.


                                                   © National Instruments 2041

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2041 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2042 ordinal=2042 -->
## Functions

Functions


                     •      y —

               y is the vertical coordinate that increases to the bottom.


               •     new picture —

         new picture is the picture that contains the plot. You can wire this output to any other picture
            input to add more drawing instructions to the picture.

           You also can wire this output to the Picture to Pixmap VI to obtain an image data cluster. You
           then can save the image data to a file using the Graphics Formats VIs.


     Examples

       Refer to the following example files included with LabVIEW.

            • labview\examples\Graphics and Sound\Picture Plots\Simple
        Radar Plot.vi

     DrawDraw LegendLegend

      Takes a picture and adds a legend to the picture.

      The Radar Plot VI uses this VI as a subVI.


      Inputs/Outputs

               •       [user-specified font] —

             [user-specified font] specifies the specific font characteristics for the text to draw.


2042   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2042 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2043 ordinal=2043 -->
## Functions

Functions


  The VI ignores this input unless desired font is User-specified Font.

      •      Font Name: —

      Font Name specifies the font to use for the text.

          If you misspell the font name or specify a font that is not installed on the computer, the
      operating system selects a font.

      •       Size —

       Size specifies the size of the font in points.

      •       Strikeout? —

       Strikeout? specifies if the text appears in strikeout. If Strikeout? is TRUE, the text appears in
       strikeout.

      •        Italic? —

        Italic? specifies if the text appears in italics. If Italic? is TRUE, the text appears in italics.

      •      Underline? —

      Underline? specifies if the text is underlined. If Underline? is TRUE, the text appears
       underlined.

      •      Outline? —

      Outline? specifies if the text is outlined. If Outline? is TRUE, the text appears outlined.

      •     Shadow? —

     Shadow? specifies if the text has a shadow. If Shadow? is TRUE, the text appears in shadow.

      •      Bold? —

      Bold? specifies if the text is bold. If Bold? is TRUE, the text appears bold.


•      desired font(Application) —

  desired font specifies the text font.


                                                   © National Instruments 2043

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2043 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2044 ordinal=2044 -->
## Functions

Functions


           0     User-specified Font
                   Application Font           1                    (default)
           2    System Font
           3     Dialog Font

               •       picture —

             picture is the picture to which you want to add the legend. The default is an empty picture.

               •       plot info —

             plot info specifies the name and color for each plot in the legend.

                     •       plot name —

                 plot name is the name of the plot.

                     •       plot color —

                 plot color is the color of the plot.

              The default is black.

               You can wire a color box constant to this input.

                     •        fill?(F) —

                        fill? does not affect the legend and the VI ignores this value.


               •       text color(black) —

             text color is the color of the text. The default is black.

           You can wire a color box constant to this input.

               •       rect —

             rect contains the coordinates that describe a rectangle bounding the legend.

             Horizontal coordinates increase to the right, and vertical coordinates increase to the bottom.


2044   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2044 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2045 ordinal=2045 -->
## Functions

Functions


         •        left —

           left is the horizontal coordinate of the left edge of the rectangle.

         •      top —

        top is the vertical coordinate of the top edge of the rectangle.

         •       right —

         right is the horizontal coordinate of the right edge of the rectangle.

         •     bottom —

       bottom is the vertical coordinate of the bottom edge of the rectangle.


   •     new picture —

   new picture is the picture that contains the legend. You can wire this output to any other picture
    input to add more drawing instructions to the picture.

    You also can wire this output to the Picture to Pixmap VI to obtain an image data cluster. You
    then can save the image data to a file using the Graphics Formats VIs.


CalcCalc ScaleScale SpecsSpecs

Takes a specification for a Cartesian style scale and calculates the coordinates and
labels to use for the scale.


Inputs/Outputs

   •       [user-specified font] —

    [user-specified font] specifies the specific font characteristics for the text to draw.


                                                    © National Instruments 2045

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2045 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2046 ordinal=2046 -->
## Functions

Functions


          The VI ignores this input unless desired font is User-specified Font.

                     •      Font Name: —

               Font Name specifies the font to use for the text.

                           If you misspell the font name or specify a font that is not installed on the computer, the
                operating system selects a font.

                     •       Size —

                 Size specifies the size of the font in points.

                     •       Strikeout? —

                 Strikeout? specifies if the text appears in strikeout. If Strikeout? is TRUE, the text appears in
                   strikeout.

                     •        Italic? —

                    Italic? specifies if the text appears in italics. If Italic? is TRUE, the text appears in italics.

                     •      Underline? —

                Underline? specifies if the text is underlined. If Underline? is TRUE, the text appears
                 underlined.

                     •      Outline? —

                Outline? specifies if the text is outlined. If Outline? is TRUE, the text appears outlined.

                     •     Shadow? —

             Shadow? specifies if the text has a shadow. If Shadow? is TRUE, the text appears in shadow.

                     •      Bold? —

               Bold? specifies if the text is bold. If Bold? is TRUE, the text appears bold.


               •      desired font(Application) —

            desired font specifies the text font.


2046   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2046 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2047 ordinal=2047 -->
## Functions

Functions


  0     User-specified Font
        Application Font  1         (default)
  2    System Font
  3     Dialog Font

•       scale definition —

  scale definition specifies the pixel coordinates and values for both ends of the scale, and the
  numeric format and precision for the scale numbers.

      •      coordinate 1 —

      coordinate 1 contains the pixel coordinates for the left of a vertical scale or the top of a
       horizontal scale.

      •      value 1 —

      value 1 contains the minimum value for the scale numbers.

      •      coordinate 2 —

      coordinate 2 contains the pixel coordinates for the right of a vertical scale or the bottom of
      a horizontal scale.

      •      value 2 —

      value 2 contains the maximum value for the scale numbers.

      •       log?(F) —

       log? specifies if the scale is logarithmic.

      •      fmt and prec —

      fmt and prec specifies the numeric format and precision for the scale numbers.

             •      format —

          format specifies the numeric format for the scale numbers.


                                                   © National Instruments 2047

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2047 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2048 ordinal=2048 -->
## Functions

Functions


                   0      Decimal
                   1        Scientific
                   2       Engineering
                   3       Binary
                   4       Octal
                   5      Hex

                           •       precision —

                     precision specifies the precision for the scale numbers. The default is 1.


               •       scale attributes —

             scale attributes describes the format for the scale.

                     •      horizontal —

                 horizontal indicates whether to draw a horizontal or vertical scale.

                     •       left/top —

                  left/top indicates whether to draw the text to the left for a vertical scale and the top for a
                 horizontal scale (TRUE), or to the right for a vertical scale and the bottom for a horizontal
                 scale (FALSE).

                     •     draw bar —

              draw bar indicates whether to draw a bar as part of the scale.

                     •       line color —

                  line color specifies the color of the line.

               You can wire a color box constant to this input.

                     •       text color(black) —


2048   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2048 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2049 ordinal=2049 -->
## Functions

Functions


         text color is the color of the text. The default is black.

        You can wire a color box constant to this input.


   •       scale specs —

    scale specs is an array of clusters containing the coordinates and labels you can use in the scale.

         •      coordinate —

        coordinate specifies the coordinates to use in the scale.

         •       label —

         label specifies the labels to use in the scale.


Wire the scale specs output of this VI to the scale specs input of the Draw Scale VI to
draw a scale.

Examples

Refer to the following example files included with LabVIEW.

  • labview\examples\Graphics and Sound\Picture Plots\Simple
   Scale.vi

DrawDraw ScaleScale

Draws a scale onto a picture.


                                                    © National Instruments 2049

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2049 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2050 ordinal=2050 -->
## Functions

Functions

      Inputs/Outputs

               •       [user-specified font] —

             [user-specified font] specifies the specific font characteristics for the text to draw.

          The VI ignores this input unless desired font is User-specified Font.

                     •      Font Name: —

               Font Name specifies the font to use for the text.

                           If you misspell the font name or specify a font that is not installed on the computer, the
                operating system selects a font.

                     •       Size —

                 Size specifies the size of the font in points.

                     •       Strikeout? —

                 Strikeout? specifies if the text appears in strikeout. If Strikeout? is TRUE, the text appears in
                   strikeout.

                     •        Italic? —

                    Italic? specifies if the text appears in italics. If Italic? is TRUE, the text appears in italics.

                     •      Underline? —

                Underline? specifies if the text is underlined. If Underline? is TRUE, the text appears
                 underlined.

                     •      Outline? —

                Outline? specifies if the text is outlined. If Outline? is TRUE, the text appears outlined.

                     •     Shadow? —

             Shadow? specifies if the text has a shadow. If Shadow? is TRUE, the text appears in shadow.

                     •      Bold? —


2050   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2050 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2051 ordinal=2051 -->
## Functions

Functions


      Bold? specifies if the text is bold. If Bold? is TRUE, the text appears bold.


•      desired font(Application) —

  desired font specifies the text font.

  0     User-specified Font
        Application Font  1         (default)
  2    System Font
  3     Dialog Font

•       picture —

  picture is the picture to which you want to add the scale. The default is an empty picture.

•       scale specs —

  scale specs is an array of clusters containing the coordinates and labels you can use in the scale.

  Use the Calc Scale Specs VI to obtain the values for this input.

      •      coordinate —

      coordinate specifies the coordinates to use in the scale.

      •       label —

       label specifies the labels to use in the scale.


•      constant coordinate —

  constant coordinate is the location of the x coordinate in a vertical scale, or the y coordinate in a
  horizontal scale.

•       tick length(3) —

  tick length specifies the length of the tick marks on the edge of the scale.

•       scale attributes —

                                                   © National Instruments 2051

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2051 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2052 ordinal=2052 -->
## Functions

Functions


             scale attributes describes the format for the scale.

                     •      horizontal —

                 horizontal indicates whether to draw a horizontal or vertical scale.

                     •       left/top —

                  left/top indicates whether to draw the text to the left for a vertical scale and the top for a
                 horizontal scale (TRUE), or to the right for a vertical scale and the bottom for a horizontal
                 scale (FALSE).

                     •     draw bar —

              draw bar indicates whether to draw a bar as part of the scale.

                     •       line color —

                  line color specifies the color of the line.

               You can wire a color box constant to this input.

                     •       text color(black) —

                  text color is the color of the text. The default is black.

               You can wire a color box constant to this input.


               •     new picture —

         new picture is the picture that contains the scale. You can wire this output to any other picture
            input to add more drawing instructions to the picture.

           You also can wire this output to the Picture to Pixmap VI to obtain an image data cluster. You
           then can save the image data to a file using the Graphics Formats VIs.


     Examples

       Refer to the following example files included with LabVIEW.

            • labview\examples\Graphics and Sound\Picture Plots\Simple

2052   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2052 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2053 ordinal=2053 -->
## Functions

Functions

   Scale.vi

MapMap SetupSetup

Uses pixel and data ranges to determine scale factors such that (a * data value) + b is
the pixel value that corresponds to that data value.


Inputs/Outputs

   •       log?(F) —

    log? specifies if the scale is logarithmic.

   •      coordinate 1 —

    coordinate 1 is the pixel location for the first point.

   •      value 1 —

    value 1 is the actual data value for the first point.

   •      coordinate 2 —

    coordinate 2 is the pixel location for the second point.

   •      value 2 —

    value 2 is the actual data value for the second point.

   •       scale factors —

    scale factors is the scale factor created from the two points.

    Use this output as the input for other VIs such as the Map Pixel to Value VI and the Map Value to
     Pixel VI.


                                                    © National Instruments 2053

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2053 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2054 ordinal=2054 -->
## Functions

Functions


                     •      a —

              a is the value used for the scale factor equation.

                     •     b —

             b is the value used for the scale factor equation.

                     •       log?(F) —

                 log? indicates if the scale is logarithmic.


     MapMap ValueValue toto PixelPixel

      Uses the domain value and the cluster returned by the Map Setup VI to determine a
        pixel value corresponding to that domain value.


      Inputs/Outputs

               •       scale factors —

             scale factors is a cluster returned by the Map Setup VI.

                     •      a —

              a is the value used in the scale factor equation in the Map Setup VI.

                     •     b —

             b is the value used in the scale factor equation in the Map Setup VI.

                     •       log?(F) —

                 log? specifies if the scale is logarithmic.


2054   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2054 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2055 ordinal=2055 -->
## Functions

Functions

   •      x —

    x is the domain value.

   •       pixel —

     pixel is the pixel value corresponding to the domain value.


MapMap PixelPixel toto ValueValue

Uses the pixel value and the cluster returned by the Map Setup VI to determine the
domain value corresponding to that pixel value.


Inputs/Outputs

   •       scale factors —

    scale factors is a cluster returned by the Map Setup VI.

         •      a —

       a is the value used in the scale factor equation in the Map Setup VI.

         •     b —

       b is the value used in the scale factor equation in the Map Setup VI.

         •       log?(F) —

         log? specifies if the scale is logarithmic.


   •       pixel —

     pixel is the pixel value.

   •      x —


                                                    © National Instruments 2055

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2055 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2056 ordinal=2056 -->
## Functions

Functions


           x is the domain value corresponding to the pixel value set in pixel.

      PicturePicture FunctionsFunctions

      Use the Picture Functions VIs to create visual representations of data. Many of these
       picture VIs use clusters to define points and rectangles. The VIs related to drawing text
      use clusters and enumerations to describe the font choice and the positioning of the
        text.


         Palette                     Description        Object

       Draw Point  Sets a pixel in a picture to a specified color.


                   Changes the current pen location of a picture to the specified position or by the       Move Pen
                       specified amount if the position is relative.


       Draw Line   Draws a line from the current pen position to the specified location in a picture.

       Draw
         Multiple    Draws multiple connected lines into a picture.
         Lines

       Draw
                   Draws a rectangle, optionally filling the interior.
         Rectangle

       Draw
                   Draws a patterned rectangle in the specified picture to create the effect of graying-out
        Grayed Out
                   a section of the picture.
         Rect


2056   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2056 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2057 ordinal=2057 -->
## Functions

Functions


Palette             Description
Object

Draw           Draws a rounded rectangle into a picture.Round Rect


Draw Oval   Draws an oval in the rectangle you specify, optionally filling the interior.


Draw Arc    Draws an arc in a picture.


Draw Text           Draws a string into a picture.at Point


Get Text     Returns a cluster that contains the left, top, right, and bottom dimensions, in pixels, of
Rect        a string.


Draw Text           Draws a string into a picture.in Rect

Draw Circle           Draws a circle based on a specified radius and center point.by Radius


            Returns two new colors well matched to the input color for highlight and shadow
Hilite Color              coloration, based on the input color and a percentage you specify.


            Converts a pixmap into a picture so you can use other Picture Functions VIs to append
Draw
            drawing instructions to the image. The data type you wire to the data input
Unflattened
            determines the polymorphic instance to use. If you want to convert a 4-bit or 8-bit
Pixmap
            pixmap, you must manually select the polymorphic instance you want to use.

Draw
Flattened   Draws a 1-, 4-, or 8-bit pixmap or a 24-bit RGB pixmap into a picture.
Pixmap


                                                    © National Instruments 2057

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2057 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2058 ordinal=2058 -->
## Functions

Functions


         Palette                     Description
        Object

                      Applies a mask to an image and returns the mask information in the mask element of         Create                  image data. This VI is useful if you want to make a certain color in an image       Mask                      transparent before writing the image to a 2D picture control.


         Picture to   Converts a picture to a cluster of image data you can use to perform certain tasks with
       Pixmap     the image, such as save it to a file using the Graphics Formats VIs.


        Get Image   Returns a subset of a source image instead of the entire image. Use the Picture to
        Subset     Pixmap VI to convert a picture to a cluster you can wire to image data.


                     Returns an empty picture. The picture input for all Picture VIs is an empty picture by
                        default.
       Empty
         Picture VI   You also can create a picture constant for an empty or existing picture and wire the
                     constant to any picture input. You can resize the constant or right-click it and select
                        Visible Items»Scrollbar from the shortcut menu to view the entire picture.

         Color Box                  Use the color box constant to supply a constant color value to the block diagram.
        Constant

         Color to     Resolves any color input, including system colors, into its respective red, green, and
       RGB        blue components.


       RGB to
                     Converts a red, green, and blue value from 0 to 255 to the corresponding RGB color.
         Color

     DrawDraw PointPoint

       Sets a pixel in a picture to a specified color.


2058   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2058 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2059 ordinal=2059 -->
## Functions

Functions


Inputs/Outputs

   •       picture —

    picture is the picture to which you want to add a pixel. The default is an empty picture.

   •       point(x,y) —

     point(x,y) is the coordinate of the pixel to set in the resulting picture relative to the current
    location of the origin.

         •      x —

        x is the horizontal coordinate that increases to the right.

         •      y —

        y is the vertical coordinate that increases to the bottom.


   •       color(black) —

    color is the color of the pixel. The default is black.

    You can wire a color box constant to this input.

   •     pen —

    pen sets the width and style of the pen the VI uses to draw the picture.

         •      Width —

       Width sets the width in pixels of the pen the VI uses to draw the picture.

         •       Style —

         Style sets the style of the line the VI uses to draw the picture.


                                                    © National Instruments 2059

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2059 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2060 ordinal=2060 -->
## Functions

Functions


                          Solid               0
                            (default)
               1      Dash
               2      Dot
               3      DashDot
               4      DashDotDot


               •     new picture —

         new picture is the picture that contains the new image. You can wire this output to any other
             picture input to add more drawing instructions to the picture.

           You also can wire this output to the Picture to Pixmap VI to obtain an image data cluster. You
           then can use the Graphics Formats VIs to save the image data to a file. You can wire this output
             to the Concatenate Strings function to concatenate the output from multiple Picture Functions
              VIs so that they draw on a single picture control.


     MoveMove PenPen

      Changes the current pen location of a picture to the specified position or by the
       specified amount if the position is relative.


      Inputs/Outputs

               •       picture —

             picture is the picture whose current pen location you want to move. The default is an empty
              picture.

               •     new position —

         new position is the point to which the pen moves in the new picture.


2060   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2060 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2061 ordinal=2061 -->
## Functions

Functions


       If absolute coordinates? is TRUE, the pen moves to the absolute coordinate specified by new
     position. If absolute coordinates? is FALSE, the pen moves relative to the current pen location in
     picture.

         •      x —

        x is the horizontal coordinate that increases to the right.

         •      y —

        y is the vertical coordinate that increases to the bottom.


   •      absolute coordinates?(T) —

    absolute coordinates? specifies whether the point new position is in absolute or relative
    coordinates.

    The default is absolute (TRUE).

   •     new picture —

   new picture is the picture that contains the new image. You can wire this output to any other
    picture input to add more drawing instructions to the picture.

    You also can wire this output to the Picture to Pixmap VI to obtain an image data cluster. You
    then can use the Graphics Formats VIs to save the image data to a file. You can wire this output
    to the Concatenate Strings function to concatenate the output from multiple Picture Functions
     VIs so that they draw on a single picture control.


Examples

Refer to the following example files included with LabVIEW.

  • labview\examples\Graphics and Sound\2D Picture Control\
   Pen Attributes And Image subsetting.vi

DrawDraw LineLine

Draws a line from the current pen position to the specified location in a picture.


                                                    © National Instruments 2061

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2061 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2062 ordinal=2062 -->
## Functions

Functions

      The end point is either absolute or relative to the current position, depending on the
       value of the absolute coordinates? input.


      Inputs/Outputs

               •       picture —

             picture is the picture to which you want to add the line. The default is an empty picture.

               •     end point —

          end point is the end point of the new line.

                    If absolute coordinates? is TRUE, the line draws to the absolute coordinate that end point
              specifies. If absolute coordinates? is FALSE, the line draws relative to the current pen location in
             picture.

                     •      x —

               x is the horizontal coordinate that increases to the right.

                     •      y —

               y is the vertical coordinate that increases to the bottom.


               •      absolute coordinates?(T) —

            absolute coordinates? specifies whether the point new position is in absolute or relative
             coordinates.

          The default is absolute (TRUE).

               •       color(black) —

             color is the color of the pixel. The default is black.


2062   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2062 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2063 ordinal=2063 -->
## Functions

Functions


    You can wire a color box constant to this input.

   •     pen —

    pen sets the width and style of the pen the VI uses to draw the picture.

         •      Width —

       Width sets the width in pixels of the pen the VI uses to draw the picture.

         •       Style —

         Style sets the style of the line the VI uses to draw the picture.

                  Solid
        0                   (default)
        1      Dash
        2      Dot
        3      DashDot
        4      DashDotDot


   •     new picture —

   new picture is the picture that contains the new image. You can wire this output to any other
    picture input to add more drawing instructions to the picture.

    You also can wire this output to the Picture to Pixmap VI to obtain an image data cluster. You
    then can use the Graphics Formats VIs to save the image data to a file. You can wire this output
    to the Concatenate Strings function to concatenate the output from multiple Picture Functions
     VIs so that they draw on a single picture control.


Examples

Refer to the following example files included with LabVIEW.

  • labview\examples\Graphics and Sound\2D Picture Control\
   Pen Attributes And Image subsetting.vi


                                                    © National Instruments 2063

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2063 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2064 ordinal=2064 -->
## Functions

Functions

     DrawDraw MultipleMultiple LinesLines

      Draws multiple connected lines into a picture.

      You also can use the VI to draw color-filled polygons by passing TRUE to the fill? input.
         All points are absolute coordinates.


      Inputs/Outputs

               •       picture —

             picture is the picture to which you want to add lines. The default is an empty picture.

               •       line endpoints —

              line endpoints is an array of points describing the lines to draw.

          The lines are drawn in the specified color, connecting the points in order. All coordinates are
             absolute.

                     •      x —

               x is the horizontal coordinate that increases to the right.

                     •      y —

               y is the vertical coordinate that increases to the bottom.


               •        fill?(F) —

                  fill? specifies whether to fill the interior.

                    If FALSE (default), the VI draws only the outlines.

               •       color(black) —


2064   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2064 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2065 ordinal=2065 -->
## Functions

Functions


    color is the color of the lines.

       If the interior is filled, the VI uses this color for the interior. The default is black.

    You can wire a color box constant to this input.

   •     pen —

    pen sets the width and style of the pen the VI uses to draw the picture.

         •      Width —

       Width sets the width in pixels of the pen the VI uses to draw the picture.

         •       Style —

         Style sets the style of the line the VI uses to draw the picture.

                  Solid
        0                   (default)
        1      Dash
        2      Dot
        3      DashDot
        4      DashDotDot


   •     new picture —

   new picture is the picture that contains the new image. You can wire this output to any other
    picture input to add more drawing instructions to the picture.

    You also can wire this output to the Picture to Pixmap VI to obtain an image data cluster. You
    then can use the Graphics Formats VIs to save the image data to a file. You can wire this output
    to the Concatenate Strings function to concatenate the output from multiple Picture Functions
     VIs so that they draw on a single picture control.


DrawDraw RectangleRectangle

Draws a rectangle, optionally filling the interior.


                                                    © National Instruments 2065

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2065 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2066 ordinal=2066 -->
## Functions

Functions


      Inputs/Outputs

               •       picture —

             picture is the picture to which you want to add the rectangle. The default is an empty picture.

               •       rect —

             rect is a cluster that contains four numeric controls that describe the left, top, right, and bottom
            coordinates of the outer edges of the rectangle.

             Horizontal coordinates increase to the right, and vertical coordinates increase to the bottom.

                     •        left —

                     left is the horizontal coordinate of the left edge of the rectangle.

                     •      top —

               top is the vertical coordinate of the top edge of the rectangle.

                     •       right —

                  right is the horizontal coordinate of the right edge of the rectangle.

                     •     bottom —

              bottom is the vertical coordinate of the bottom edge of the rectangle.


               •        fill?(F) —

                  fill? specifies whether to fill the interior.

                    If FALSE (default), the VI draws only the outlines.

               •       color(black) —

             color is the color of the lines.


2066   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2066 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2067 ordinal=2067 -->
## Functions

Functions


       If the interior is filled, the VI uses this color for the interior. The default is black.

    You can wire a color box constant to this input.

   •     pen —

    pen sets the width and style of the pen the VI uses to draw the picture.

         •      Width —

       Width sets the width in pixels of the pen the VI uses to draw the picture.

         •       Style —

         Style sets the style of the line the VI uses to draw the picture.

                  Solid        0                   (default)
        1      Dash
        2      Dot
        3      DashDot
        4      DashDotDot


   •     new picture —

   new picture is the picture that contains the new image. You can wire this output to any other
    picture input to add more drawing instructions to the picture.

    You also can wire this output to the Picture to Pixmap VI to obtain an image data cluster. You
    then can use the Graphics Formats VIs to save the image data to a file. You can wire this output
    to the Concatenate Strings function to concatenate the output from multiple Picture Functions
     VIs so that they draw on a single picture control.


DrawDraw GrayedGrayed OutOut RectRect

Draws a patterned rectangle in the specified picture to create the effect of graying-out
a section of the picture.

An underlying picture shows through the holes in the pattern. The VI does not frame


                                                    © National Instruments 2067

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2067 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2068 ordinal=2068 -->
## Functions

Functions

       the rectangle.


      Inputs/Outputs

               •       picture —

             picture is the picture to which you want to add the rectangle. The default is an empty picture.

               •       rect —

             rect is a cluster that contains four numeric controls that describe the left, top, right, and bottom
            coordinates of the outer edges of the rectangle.

             Horizontal coordinates increase to the right, and vertical coordinates increase to the bottom.

                     •        left —

                     left is the horizontal coordinate of the left edge of the rectangle.

                     •      top —

               top is the vertical coordinate of the top edge of the rectangle.

                     •       right —

                  right is the horizontal coordinate of the right edge of the rectangle.

                     •     bottom —

              bottom is the vertical coordinate of the bottom edge of the rectangle.


               •       color(black) —

             color is the color of the pattern. In black and white, the VI uses white.

           You can wire a color box constant to this input.

               •     new picture —


2068   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2068 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2069 ordinal=2069 -->
## Functions

Functions


   new picture is the picture that contains the new image. You can wire this output to any other
    picture input to add more drawing instructions to the picture.

    You also can wire this output to the Picture to Pixmap VI to obtain an image data cluster. You
    then can use the Graphics Formats VIs to save the image data to a file. You can wire this output
    to the Concatenate Strings function to concatenate the output from multiple Picture Functions
     VIs so that they draw on a single picture control.


DrawDraw RoundRound RectRect

Draws a rounded rectangle into a picture.


Inputs/Outputs

   •      oval height —

    oval height is the height of an oval that defines the amount of curvature for the corners.

   •      oval width —

    oval width is the width of an oval that defines the amount of curvature for the corners.

   •       picture —

    picture is the picture to which you want to add the rectangle. The default is an empty picture.

   •       rect —

     rect is a cluster that contains four numeric controls that describe the left, top, right, and bottom
    coordinates of the outer edges of a rectangle that circumscribes the rounded rectangle.

    Horizontal coordinates increase to the right, and vertical coordinates increase to the bottom.


                                                    © National Instruments 2069

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2069 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2070 ordinal=2070 -->
## Functions

Functions


                     •        left —

                     left is the horizontal coordinate of the left edge of the rectangle.

                     •      top —

               top is the vertical coordinate of the top edge of the rectangle.

                     •       right —

                  right is the horizontal coordinate of the right edge of the rectangle.

                     •     bottom —

              bottom is the vertical coordinate of the bottom edge of the rectangle.


               •        fill?(F) —

                  fill? specifies whether to fill the interior.

                    If FALSE (default), the VI draws only the outlines.

               •       color(black) —

             color is the color of the lines.

                    If the interior is filled, the VI uses this color for the interior. The default is black.

           You can wire a color box constant to this input.

               •     pen —

          pen sets the width and style of the pen the VI uses to draw the picture.

                     •      Width —

               Width sets the width in pixels of the pen the VI uses to draw the picture.

                     •       Style —

                 Style sets the style of the line the VI uses to draw the picture.


2070   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2070 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2071 ordinal=2071 -->
## Functions

Functions


                  Solid        0
                   (default)
        1      Dash
        2      Dot
        3      DashDot
        4      DashDotDot


   •     new picture —

   new picture is the picture that contains the new image. You can wire this output to any other
    picture input to add more drawing instructions to the picture.

    You also can wire this output to the Picture to Pixmap VI to obtain an image data cluster. You
    then can use the Graphics Formats VIs to save the image data to a file. You can wire this output
    to the Concatenate Strings function to concatenate the output from multiple Picture Functions
     VIs so that they draw on a single picture control.


If oval height and oval width are zero, you get a normal rectangle. If they are greater
than zero, they describe how the corners of the rectangle should be rounded, as
shown in the following illustration.


DrawDraw OvalOval

Draws an oval in the rectangle you specify, optionally filling the interior.


                                                    © National Instruments 2071

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2071 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2072 ordinal=2072 -->
## Functions

Functions


      Inputs/Outputs

               •       picture —

             picture is the picture to which you want to add the oval. The default is an empty picture.

               •       rect —

             rect is a cluster that contains four numeric controls that describe the left, top, right, and bottom
            coordinates of the outer edges of the rectangle.

             Horizontal coordinates increase to the right, and vertical coordinates increase to the bottom.

                     •        left —

                     left is the horizontal coordinate of the left edge of the rectangle.

                     •      top —

               top is the vertical coordinate of the top edge of the rectangle.

                     •       right —

                  right is the horizontal coordinate of the right edge of the rectangle.

                     •     bottom —

              bottom is the vertical coordinate of the bottom edge of the rectangle.


               •        fill?(F) —

                  fill? specifies whether to fill the interior.

                    If FALSE (default), the VI draws only the outlines.

               •       color(black) —

             color is the color of the lines.


2072   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2072 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2073 ordinal=2073 -->
## Functions

Functions


       If the interior is filled, the VI uses this color for the interior. The default is black.

    You can wire a color box constant to this input.

   •     pen —

    pen sets the width and style of the pen the VI uses to draw the picture.

         •      Width —

       Width sets the width in pixels of the pen the VI uses to draw the picture.

         •       Style —

         Style sets the style of the line the VI uses to draw the picture.

                  Solid        0                   (default)
        1      Dash
        2      Dot
        3      DashDot
        4      DashDotDot


   •     new picture —

   new picture is the picture that contains the new image. You can wire this output to any other
    picture input to add more drawing instructions to the picture.

    You also can wire this output to the Picture to Pixmap VI to obtain an image data cluster. You
    then can use the Graphics Formats VIs to save the image data to a file. You can wire this output
    to the Concatenate Strings function to concatenate the output from multiple Picture Functions
     VIs so that they draw on a single picture control.


DrawDraw ArcArc

Draws an arc in a picture.


                                                    © National Instruments 2073

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2073 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2074 ordinal=2074 -->
## Functions

Functions


      Inputs/Outputs

               •      arc size[degrees] —

            arc size determines the degree value of the circle you want to draw.

             This value can range from -360 to 360. For example, a value of 360 creates a complete circle, and
           a value of 180 creates a semicircle.

               •       start angle[degrees] —

              start angle determines where the arc begins.

               •       picture —

             picture is the picture to which you want to add the arc. The default is an empty picture.

               •       rect —

             rect is a cluster that contains four numeric controls that describe the left, top, right, and bottom
            coordinates of the outer edges of the rectangle.

             Horizontal coordinates increase to the right, and vertical coordinates increase to the bottom.

                     •        left —

                     left is the horizontal coordinate of the left edge of the rectangle.

                     •      top —

               top is the vertical coordinate of the top edge of the rectangle.

                     •       right —

                  right is the horizontal coordinate of the right edge of the rectangle.

                     •     bottom —


2074   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2074 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2075 ordinal=2075 -->
## Functions

Functions


     bottom is the vertical coordinate of the bottom edge of the rectangle.


•        fill?(F) —

   fill? specifies whether to fill the rectangle. If FALSE (default), the VI draws only the arc
  component and does not draw interior bounds of the wedge.

•       color(black) —

  color is the color of the lines.

   If the interior is filled, the VI uses this color for the interior. The default is black.

  You can wire a color box constant to this input.

•     pen —

  pen sets the width and style of the pen the VI uses to draw the picture.

      •      Width —

      Width sets the width in pixels of the pen the VI uses to draw the picture.

      •       Style —

       Style sets the style of the line the VI uses to draw the picture.

               Solid      0
                 (default)
      1      Dash
      2      Dot
      3      DashDot
      4      DashDotDot


•     new picture —

  new picture is the picture that contains the new image. You can wire this output to any other
  picture input to add more drawing instructions to the picture.


                                                   © National Instruments 2075

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2075 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2076 ordinal=2076 -->
## Functions

Functions


           You also can wire this output to the Picture to Pixmap VI to obtain an image data cluster. You
           then can use the Graphics Formats VIs to save the image data to a file. You can wire this output
             to the Concatenate Strings function to concatenate the output from multiple Picture Functions
              VIs so that they draw on a single picture control.


      A rectangle specifies the size of an oval that contains the arc. Thus, the arc may not fill
       the whole rectangle. LabVIEW specifies the angles that describe the arc in degrees. It
      can range from –360° to 360°, with positive angles appearing clockwise, and negative
       angles appearing counterclockwise. Zero degrees is straight up.

      LabVIEW measures all angles as though the enclosing rectangle were square. Thus, a
        line from the center to the upper-right corner describes an angle of 45°. The following
        illustration shows the conventions used in specifying the angle of a point of an arc.


     DrawDraw TextText atat PointPoint

      Draws a string into a picture.

       This VI automatically calculates the bounding rectangle of the text and positions the
        text with respect to the point you specify.


2076   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2076 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2077 ordinal=2077 -->
## Functions

Functions

Inputs/Outputs

   •       [user-specified font] —

    [user-specified font] specifies the specific font characteristics for the text to draw.

    The VI ignores this input unless desired font is User-specified Font.

         •      Font Name: —

        Font Name specifies the font to use for the text.

              If you misspell the font name or specify a font that is not installed on the computer, the
        operating system selects a font.

         •       Size —

         Size specifies the size of the font in points.

         •       Strikeout? —

         Strikeout? specifies if the text appears in strikeout. If Strikeout? is TRUE, the text appears in
          strikeout.

         •        Italic? —

          Italic? specifies if the text appears in italics. If Italic? is TRUE, the text appears in italics.

         •      Underline? —

        Underline? specifies if the text is underlined. If Underline? is TRUE, the text appears
         underlined.

         •      Outline? —

        Outline? specifies if the text is outlined. If Outline? is TRUE, the text appears outlined.

         •     Shadow? —

       Shadow? specifies if the text has a shadow. If Shadow? is TRUE, the text appears in shadow.

         •      Bold? —


                                                    © National Instruments 2077

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2077 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2078 ordinal=2078 -->
## Functions

Functions


               Bold? specifies if the text is bold. If Bold? is TRUE, the text appears bold.


               •      desired font(Application) —

            desired font specifies the text font.

           0     User-specified Font
                   Application Font           1                    (default)
           2    System Font
           3     Dialog Font

               •       picture —

             picture is the picture to which you want to add the text string. The default is an empty picture.

               •       origin —

             origin is the coordinate of the starting point of the text.

                     •      x —

               x is the horizontal coordinate that increases to the right.

                     •      y —

               y is the vertical coordinate that increases to the bottom.


               •       alignment(left, top) —

           alignment specifies the location of the text relative to the origin you specify.

                     •      horizontal —

                 horizontal sets the horizontal position of the text with respect to the origin.

               0 left—The horizontal component of origin specifies the left edge of the text.


2078   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2078 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2079 ordinal=2079 -->
## Functions

Functions


      1 center—The horizontal component of the origin specifies the center of the text.
      2 right—The horizontal component of origin specifies the right of the text.

      •       vertical —

       vertical sets the vertical position of the text with respect to the origin.

      0 top—The vertical component of origin specifies the top edge of the text.
      1 center—The vertical component of the origin specifies the center of the text.
      2 bottom—The vertical component of origin specifies the bottom of the text.


•       text —

  text is the string to draw in the picture.

•       text color(black) —

  text color is the color of the text. The default is black.

  You can wire a color box constant to this input.

•     BG color(transparent) —

  BG color is the color of the background of the text.

  The default is transparent.

  You can wire a color box constant to this input.

•       text orientation —

  text orientation sets the orientation of the text to draw.

  0 None (default)—Text appears normal.
  1 Stacked—Text appears stacked.
   Clockwise—Text appears rotated 90° clockwise, which results in vertical text that reads
  2
   downward.
   Counterclockwise—Text appears rotated 90° counterclockwise, which results in vertical text
  3
    that reads upward.


                                                   © National Instruments 2079

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2079 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2080 ordinal=2080 -->
## Functions

Functions

               •     new picture —

         new picture is the picture that contains the new image. You can wire this output to any other
             picture input to add more drawing instructions to the picture.

           You also can wire this output to the Picture to Pixmap VI to obtain an image data cluster. You
           then can use the Graphics Formats VIs to save the image data to a file. You can wire this output
             to the Concatenate Strings function to concatenate the output from multiple Picture Functions
              VIs so that they draw on a single picture control.

               •       text rect —

             text rect is a cluster that contains coordinates that describe the left, top, right, and bottom
            coordinates of the outer edges of the rectangle.

                     •        left —

                     left is the horizontal coordinate of the left edge of the rectangle.

                     •      top —

               top is the vertical coordinate of the top edge of the rectangle.

                     •       right —

                  right is the horizontal coordinate of the right edge of the rectangle.

                     •     bottom —

              bottom is the vertical coordinate of the bottom edge of the rectangle.


      GetGet TextText RectRect

       Returns a cluster that contains the left, top, right, and bottom dimensions, in pixels, of
      a string.


2080   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2080 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2081 ordinal=2081 -->
## Functions

Functions


Inputs/Outputs

   •       [user-specified font] —

    [user-specified font] specifies the specific font characteristics for the text to draw.

    The VI ignores this input unless desired font is User-specified Font.

         •      Font Name: —

        Font Name specifies the font to use for the text.

              If you misspell the font name or specify a font that is not installed on the computer, the
        operating system selects a font.

         •       Size —

         Size specifies the size of the font in points.

         •       Strikeout? —

         Strikeout? specifies if the text appears in strikeout. If Strikeout? is TRUE, the text appears in
          strikeout.

         •        Italic? —

          Italic? specifies if the text appears in italics. If Italic? is TRUE, the text appears in italics.

         •      Underline? —

        Underline? specifies if the text is underlined. If Underline? is TRUE, the text appears
         underlined.

         •      Outline? —

        Outline? specifies if the text is outlined. If Outline? is TRUE, the text appears outlined.

         •     Shadow? —


                                                    © National Instruments 2081

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2081 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2082 ordinal=2082 -->
## Functions

Functions


             Shadow? specifies if the text has a shadow. If Shadow? is TRUE, the text appears in shadow.

                     •      Bold? —

               Bold? specifies if the text is bold. If Bold? is TRUE, the text appears bold.


               •      desired font(Application) —

            desired font specifies the text font.

           0     User-specified Font
                   Application Font           1
                    (default)
           2    System Font
           3     Dialog Font

               •       alignment(left, top) —

           alignment specifies the location of the text relative to the origin you specify.

                     •      horizontal —

                 horizontal sets the horizontal position of the text with respect to the origin.

               0 left—The horizontal component of origin specifies the left edge of the text.
               1 center—The horizontal component of the origin specifies the center of the text.
               2 right—The horizontal component of origin specifies the right of the text.

                     •       vertical —

                  vertical sets the vertical position of the text with respect to the origin.

               0 top—The vertical component of origin specifies the top edge of the text.
               1 center—The vertical component of the origin specifies the center of the text.
               2 bottom—The vertical component of origin specifies the bottom of the text.


               •       origin(0,0) —


2082   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2082 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2083 ordinal=2083 -->
## Functions

Functions


  origin is the coordinate of the starting point of the text.

      •      horizontal —

       horizontal is the x-axis coordinate that increases to the right.

      •       vertical —

       vertical is the y-axis coordinate that increases to the bottom.


•       text —

  text is the string to draw in the picture.

•       text orientation —

  text orientation sets the orientation of the text for which you want the bounding rectangle.

  0 None (default)—Text appears normal.
  1 Stacked—Text appears stacked.
   Clockwise—Text appears rotated 90° clockwise. This results in vertical text that reads
  2   downward.
   Counterclockwise—Text appears rotated 90° counterclockwise. This results in vertical text that
  3   reads upward.

•       rect —

  rect is a cluster that contains coordinates that describe the left, top, right, and bottom
  coordinates of the outer edges of the rectangle.

  Horizontal coordinates increase to the right, and vertical coordinates increase to the bottom.

      •        left —

        left is the horizontal coordinate of the left edge of the rectangle.

      •      top —

      top is the vertical coordinate of the top edge of the rectangle.

      •       right —


                                                   © National Instruments 2083

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2083 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2084 ordinal=2084 -->
## Functions

Functions


                  right is the horizontal coordinate of the right edge of the rectangle.

                     •     bottom —

              bottom is the vertical coordinate of the bottom edge of the rectangle.


     DrawDraw TextText inin RectRect

      Draws a string into a picture.

           If the string is larger than the rectangle you specify, the VI clips, or crops, the string to
       the area of the rectangle.


      Inputs/Outputs

               •       [user-specified font] —

             [user-specified font] specifies the specific font characteristics for the text to draw.

          The VI ignores this input unless desired font is User-specified Font.

                     •      Font Name: —

               Font Name specifies the font to use for the text.

                           If you misspell the font name or specify a font that is not installed on the computer, the
                operating system selects a font.

                     •       Size —


2084   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2084 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2085 ordinal=2085 -->
## Functions

Functions


       Size specifies the size of the font in points.

      •       Strikeout? —

       Strikeout? specifies if the text appears in strikeout. If Strikeout? is TRUE, the text appears in
       strikeout.

      •        Italic? —

        Italic? specifies if the text appears in italics. If Italic? is TRUE, the text appears in italics.

      •      Underline? —

      Underline? specifies if the text is underlined. If Underline? is TRUE, the text appears
       underlined.

      •      Outline? —

      Outline? specifies if the text is outlined. If Outline? is TRUE, the text appears outlined.

      •     Shadow? —

     Shadow? specifies if the text has a shadow. If Shadow? is TRUE, the text appears in shadow.

      •      Bold? —

      Bold? specifies if the text is bold. If Bold? is TRUE, the text appears bold.


•      desired font(Application) —

  desired font specifies the text font.

  0     User-specified Font
        Application Font
  1
         (default)
  2    System Font
  3     Dialog Font

•       picture —

  picture is the picture to which you want to add the text string. The default is an empty picture.


                                                   © National Instruments 2085

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2085 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2086 ordinal=2086 -->
## Functions

Functions

               •       text orientation —

             text orientation sets the orientation of the text to draw.

           0 None (default)—Text appears normal.
           1 Stacked—Text appears stacked.
             Clockwise—Text appears rotated 90° clockwise, which results in vertical text that reads           2            downward.
             Counterclockwise—Text appears rotated 90° counterclockwise, which results in vertical text           3              that reads upward.

               •       rect —

             rect contains the upper-left and lower-right coordinates that describe a rectangle bounding the
               text.

          The VI clips text to the coordinates of this rectangle. Horizontal coordinates increase to the right,
          and vertical coordinates increase to the bottom.

                     •        left —

                     left is the horizontal coordinate of the left edge of the rectangle.

                     •      top —

               top is the vertical coordinate of the top edge of the rectangle.

                     •       right —

                  right is the horizontal coordinate of the right edge of the rectangle.

                     •     bottom —

              bottom is the vertical coordinate of the bottom edge of the rectangle.


               •       text —

             text is the string to draw in the picture.

               •       text color(black) —

             text color is the color of the text. The default is black.


2086   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2086 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2087 ordinal=2087 -->
## Functions

Functions


    You can wire a color box constant to this input.

   •     BG color(transparent) —

   BG color is the color of the background of the text.

    The default is transparent.

    You can wire a color box constant to this input.

   •     new picture —

   new picture is the picture that contains the new image. You can wire this output to any other
    picture input to add more drawing instructions to the picture.

    You also can wire this output to the Picture to Pixmap VI to obtain an image data cluster. You
    then can use the Graphics Formats VIs to save the image data to a file. You can wire this output
    to the Concatenate Strings function to concatenate the output from multiple Picture Functions
     VIs so that they draw on a single picture control.


DrawDraw CircleCircle byby RadiusRadius

Draws a circle based on a specified radius and center point.


Inputs/Outputs

   •      arc size(360) —

    arc size determines the degree value of the circle you want to draw.

    This value can range from -360 to 360. For example, a value of 360 creates a complete circle, and
    a value of 180 creates a semicircle.


                                                    © National Instruments 2087

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2087 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2088 ordinal=2088 -->
## Functions

Functions

               •       start angle(0) —

              start angle determines where the arc begins.

               •       picture —

             picture is the picture to which you want to add the circle. The default is an empty picture.

               •      radius —

            radius determines the size of the circle, in pixels.

                      If, for example, this value is 40, the radius of the resulting circle is 40 pixels.

               •       pixel center —

             pixel center contains the coordinates around which the VI draws the circle.

                     •      horizontal —

                 horizontal is the pixel center of the circle relative to the x-coordinate of the current origin.

                     •       vertical —

                  vertical is the pixel center of the circle relative to the y-coordinate of the current origin.


               •        fill?(F) —

                  fill? specifies whether to fill the interior.

                    If FALSE (default), the VI draws only the outlines.

               •       color(black) —

             color sets the pen color to use when drawing the oval.

                    If unwired, the VI uses the last color specified as the pen color.

           You can wire a color box constant to this input.

               •     pen —

          pen sets the width and style of the pen the VI uses to draw the picture.


2088   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2088 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2089 ordinal=2089 -->
## Functions

Functions


         •      Width —

       Width sets the width in pixels of the pen the VI uses to draw the picture.

         •       Style —

         Style sets the style of the line the VI uses to draw the picture.

                  Solid        0                   (default)
        1      Dash
        2      Dot
        3      DashDot
        4      DashDotDot


   •     new picture —

   new picture is the picture that contains the new image. You can wire this output to any other
    picture input to add more drawing instructions to the picture.

    You also can wire this output to the Picture to Pixmap VI to obtain an image data cluster. You
    then can use the Graphics Formats VIs to save the image data to a file. You can wire this output
    to the Concatenate Strings function to concatenate the output from multiple Picture Functions
     VIs so that they draw on a single picture control.


The Draw Circle by Radius VI uses the information you specify and calls the Draw Oval
VI.

A rectangle specifies the size of an oval that contains the arc. Thus, the arc may not fill
the whole rectangle. LabVIEW specifies the angles that describe the arc in degrees. It
can range from –360° to 360°, with positive angles appearing clockwise, and negative
angles appearing counterclockwise. Zero degrees is straight up.

LabVIEW measures all angles as though the enclosing rectangle were square. Thus, a
line from the center to the upper-right corner describes an angle of 45°. The following
illustration shows the conventions used in specifying the angle of a point of an arc.


                                                    © National Instruments 2089

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2089 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2090 ordinal=2090 -->
## Functions

Functions


        HiliteHilite ColorColor

       Returns two new colors well matched to the input color for highlight and shadow
       coloration, based on the input color and a percentage you specify.

      You can use the highlight colors to create three-dimensionally shaded objects.


      Inputs/Outputs

               •      Color In —

            Color In is the input color on which to base the returned highlight and shadow colors.

           You can wire a color box constant to this input.

               •      Percentage(30) —

           Percentage determines the degree of highlighting and shadow in the new colors.

          The default is 30 percent.

               •       Hilite —

              Hilite is the new color matched as a highlight to the input color.

               •     Shadow —

         Shadow is the new color matched as a shadow to the input color.


2090   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2090 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2091 ordinal=2091 -->
## Functions

Functions

DrawDraw UnflattenedUnflattened PixmapPixmap

Converts a pixmap into a picture so you can use other Picture Functions VIs to append
drawing instructions to the image. The data type you wire to the data input determines
the polymorphic instance to use. If you want to convert a 4-bit or 8-bit pixmap, you
must manually select the polymorphic instance you want to use.


  • Draw True-Color Pixmap VI
  • Draw 1-Bit Pixmap VI
  • Draw 4-Bit Pixmap VI
  • Draw 8-Bit Pixmap VI
DrawDraw True-ColorTrue-Color PixmapPixmap VIVI

Converts a pixmap into a picture so you can use other Picture Functions VIs to append
drawing instructions to the image. The data type you wire to the data input determines
the polymorphic instance to use. If you want to convert a 4-bit or 8-bit pixmap, you
must manually select the polymorphic instance you want to use.


Inputs/Outputs

   •       picture —

    picture is the picture to which you want to add the pixmap. The default is an empty picture.

   •      top left point(0, 0) —

    top left point specifies in coordinates where to place the top-left corner of the image in the new
     picture.


                                                    © National Instruments 2091

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2091 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2092 ordinal=2092 -->
## Functions

Functions


                     •      x —

               x is the horizontal coordinate that increases to the right.

                     •      y —

               y is the vertical coordinate that increases to the bottom.


               •      data (RGB format) —

           data is a 2D array of 32-bit unsigned integers that describes the color of each pixel in the image
              in raster order.

           Each pixel has three bytes to describe its color. The first byte for each pixel describes the red
             value, the second byte describes the green value, and the third byte describes the blue value.

               •     mask —

         mask is an array of bytes in which each bit describes mask information for a pixel. The first byte
            describes the first eight pixels, the second byte describes the next eight pixels, and so on.

                    If a bit is zero, LabVIEW draws the corresponding pixel as transparent. If the array is empty,
           LabVIEW draws all pixels without transparency. If the array does not contain a bit for each pixel
              in the image, LabVIEW draws any pixels missing from the array without transparency.

               •     new picture —

         new picture is the picture that contains the new image. You can wire this output to any other
             picture input to add more drawing instructions to the picture.

   DrawDraw 1-Bit1-Bit PixmapPixmap VIVI

       Converts a pixmap into a picture so you can use other Picture Functions VIs to append
      drawing instructions to the image. The data type you wire to the data input determines
       the polymorphic instance to use. If you want to convert a 4-bit or 8-bit pixmap, you
      must manually select the polymorphic instance you want to use.


2092   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2092 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2093 ordinal=2093 -->
## Functions

Functions


Inputs/Outputs

   •       picture —

    picture is the picture to which you want to add the pixmap. The default is an empty picture.

   •      top left point(0, 0) —

    top left point specifies in coordinates where to place the top-left corner of the image in the new
     picture.

         •      x —

        x is the horizontal coordinate that increases to the right.

         •      y —

        y is the vertical coordinate that increases to the bottom.


   •      data —

    data is a 2D array of Boolean inputs in which each input represents a single pixel.

    A value of FALSE in data corresponds to element 0 in color table. A value of TRUE in data
    corresponds to element 1 in color table.

   •       color table —

    color table is an array of two colors to which the array of data maps.

       If data is FALSE, the default is black. If data is TRUE, the default is white.

   •     mask —

   mask is an array of bytes in which each bit describes mask information for a pixel. The first byte
    describes the first eight pixels, the second byte describes the next eight pixels, and so on.

       If a bit is zero, LabVIEW draws the corresponding pixel as transparent. If the array is empty,


                                                    © National Instruments 2093

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2093 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2094 ordinal=2094 -->
## Functions

Functions


           LabVIEW draws all pixels without transparency. If the array does not contain a bit for each pixel
              in the image, LabVIEW draws any pixels missing from the array without transparency.

               •     new picture —

         new picture is the picture that contains the new image. You can wire this output to any other
             picture input to add more drawing instructions to the picture.

   DrawDraw 4-Bit4-Bit PixmapPixmap VIVI

       Converts a pixmap into a picture so you can use other Picture Functions VIs to append
      drawing instructions to the image. The data type you wire to the data input determines
       the polymorphic instance to use. If you want to convert a 4-bit or 8-bit pixmap, you
      must manually select the polymorphic instance you want to use.


      Inputs/Outputs

               •       picture —

             picture is the picture to which you want to add the pixmap. The default is an empty picture.

               •      top left point(0, 0) —

           top left point specifies in coordinates where to place the top-left corner of the image in the new
             picture.

                     •      x —

               x is the horizontal coordinate that increases to the right.

                     •      y —


2094   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2094 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2095 ordinal=2095 -->
## Functions

Functions


        y is the vertical coordinate that increases to the bottom.


   •      data —

    data is a 2D array of 8-bit unsigned integers that describes the color of each pixel in the image in
     raster order.

    Each element in data specifies the index of the corresponding color in color table. Thus, valid
    values in data are the indices of the color table array, or 0 through 15.

   •       color table —

    color table is an array of up to 16 colors to which the array of data maps.

    color table stores 32-bit RGB values where the most-significant byte is zero, followed in order by
     red, green, and blue values. If unwired, the VI uses the default LabVIEW 16-color palette.

   •     mask —

   mask is an array of bytes in which each bit describes mask information for a pixel. The first byte
    describes the first eight pixels, the second byte describes the next eight pixels, and so on.

       If a bit is zero, LabVIEW draws the corresponding pixel as transparent. If the array is empty,
    LabVIEW draws all pixels without transparency. If the array does not contain a bit for each pixel
     in the image, LabVIEW draws any pixels missing from the array without transparency.

   •     new picture —

   new picture is the picture that contains the new image. You can wire this output to any other
    picture input to add more drawing instructions to the picture.

DrawDraw 8-Bit8-Bit PixmapPixmap VIVI

Converts a pixmap into a picture so you can use other Picture Functions VIs to append
drawing instructions to the image. The data type you wire to the data input determines
the polymorphic instance to use. If you want to convert a 4-bit or 8-bit pixmap, you
must manually select the polymorphic instance you want to use.


                                                    © National Instruments 2095

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2095 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2096 ordinal=2096 -->
## Functions

Functions


      Inputs/Outputs

               •       picture —

             picture is the picture to which you want to add the pixmap. The default is an empty picture.

               •      top left point(0, 0) —

           top left point specifies in coordinates where to place the top-left corner of the image in the new
             picture.

                     •      x —

               x is the horizontal coordinate that increases to the right.

                     •      y —

               y is the vertical coordinate that increases to the bottom.


               •      data —

           data is a 2D array of 8-bit unsigned integers that describes the color of each pixel in the image in
              raster order.

           Each element in data specifies the index of the corresponding color in color table. Thus, valid
            values in data are the indices of the color table array, or 0 through 255.

               •       color table —

             color table is an array of up to 256 colors to which the array of data maps.

             color table stores 32-bit RGB values where the most-significant byte is zero, followed in order by
             red, green, and blue values. If unwired, the VI uses the default LabVIEW 256-color palette.

               •     mask —

         mask is an array of bytes in which each bit describes mask information for a pixel. The first byte


2096   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2096 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2097 ordinal=2097 -->
## Functions

Functions


    describes the first eight pixels, the second byte describes the next eight pixels, and so on.

       If a bit is zero, LabVIEW draws the corresponding pixel as transparent. If the array is empty,
    LabVIEW draws all pixels without transparency. If the array does not contain a bit for each pixel
     in the image, LabVIEW draws any pixels missing from the array without transparency.

   •     new picture —

   new picture is the picture that contains the new image. You can wire this output to any other
    picture input to add more drawing instructions to the picture.


DrawDraw FlattenedFlattened PixmapPixmap

Draws a 1-, 4-, or 8-bit pixmap or a 24-bit RGB pixmap into a picture.

This VI takes a 1D array of bytes as input and assumes the user completes all packing
and padding.


Inputs/Outputs

   •       picture —

    picture is the picture to which you want to add the array of data. The default is an empty picture.

   •     image data —

    image data describes the image you want to draw or manipulate.

         •     image type —

       image type is reserved for future use.

         •     image depth —

       image depth specifies the color depth of the image, which is the number of bits to use to


                                                    © National Instruments 2097

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2097 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2098 ordinal=2098 -->
## Functions

Functions


                 describe the color of each pixel in the image. Valid values include 1, 4, 8, and 24 bits per
                    pixel.

              image depth affects how LabVIEW interprets the values of image and colors.

                     •     image —

              image is an array of bytes that describes the color of each pixel in the image in raster order.
              The value of image depth determines how LabVIEW interprets the value of this input.

                           If image depth is 24, each pixel has three bytes to describe its color. The first byte for each
                   pixel describes the red value, the second byte describes the green value, and the third byte
                 describes the blue value.

                           If image depth is 8, each pixel has one byte to describe its color. The value of each byte
                corresponds to an element in colors, which stores 32-bit RGB values where the most-
                   significant byte is zero, followed in order by red, green, and blue values. Valid values include
               0 through 255.

                           If image depth is 4, the behavior is similar to when image depth is 8 except valid values in
              image include 0 through 15.

                           If image depth is 1, any value of zero in image corresponds to element 0 in colors. All other
                 values correspond to element 1 in colors.

                     •     mask —

             mask is an array of bytes in which each bit describes mask information for a pixel. The first
                byte describes the first eight pixels, the second byte describes the next eight pixels, and so
                 on.

                           If a bit is zero, LabVIEW draws the corresponding pixel as transparent. If the array is empty,
              LabVIEW draws all pixels without transparency. If the array does not contain a bit for each
                   pixel in the image, LabVIEW draws any pixels missing from the array without transparency.

                     •       colors —

                 colors is an array of RGB color values that correspond to the values in image. The value of
              image depth determines how LabVIEW interprets the value of this input. colors stores 32-bit
            RGB values where the most-significant byte is zero, followed in order by red, green, and blue
                  values. Valid values include 0 through 255.


2098   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2098 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2099 ordinal=2099 -->
## Functions

Functions


          If image depth is 24, LabVIEW ignores this input.

          If image depth is 8, the array can have 256 elements.

          If image depth is 4, the array can have 16 elements.

          If image depth is 1, the array can have 2 elements.

      •      Rectangle —

      Rectangle is a cluster that contains coordinates that describe the bounding rectangle in
      which you want to draw the image.

     The VI clips the image to the width and height of the rectangle. The bottom and right edges
       of the rectangle bounds do not contain image pixels. Horizontal coordinates increase to the
        right, and vertical coordinates increase to the bottom.

             •        left —

              left is the horizontal coordinate of the left edge of the rectangle.

             •      top —

          top is the vertical coordinate of the top edge of the rectangle.

             •       right —

            right is the horizontal coordinate of the right edge of the rectangle.

             •     bottom —

         bottom is the vertical coordinate of the bottom edge of the rectangle.


•     new picture —

  new picture is the picture that contains the new image. You can wire this output to any other
  picture input to add more drawing instructions to the picture.


                                                   © National Instruments 2099

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2099 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2100 ordinal=2100 -->
## Functions

Functions

           Note This VI interprets 32-bit images as 24-bit images.

      You can use this VI with one of the Graphics Formats VIs that reads graphics files in a
       flattened format. You also can use the Flatten Pixmap VI to produce flattened pixmap
       data. Use the Unflatten Pixmap VI to unflatten data for use with one of the other VIs
      used to draw a pixmap.

      The Draw Flattened Pixmap VI expects all images to be padded with a 2-byte
      boundary. The Draw Flattened Pixmap VI does not pad images. The various Graphics
      Formats VIs which load images also pad images appropriately for use in the Draw
       Flattened Pixmap VI. If you choose to upload your image in a different way, you need to
      pad the data with a 2-byte boundary yourself before using the Draw Flattened Pixmap
         VI.

      CreateCreate MaskMask

       Applies a mask to an image and returns the mask information in the mask element of
      image data. This VI is useful if you want to make a certain color in an image
       transparent before writing the image to a 2D picture control.


      Inputs/Outputs

               •     image data —

          image data returns information about the image so you can use the Draw Flattened Pixmap VI to
          draw it as a picture.

                     •     image type —

              image type is reserved for future use.

                     •     image depth —


2100   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2100 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2101 ordinal=2101 -->
## Functions

Functions


  image depth specifies the color depth of the image, which is the number of bits to use to
  describe the color of each pixel in the image. Valid values include 1, 4, 8, and 24 bits per
   pixel.

  image depth affects how LabVIEW interprets the values of image and colors.

•     image —

  image is an array of bytes that describes the color of each pixel in the image in raster order.
  The value of image depth determines how LabVIEW interprets the value of this output.

   If image depth is 24, each pixel has three bytes to describe its color. The first byte for each
  pixel describes the red value, the second byte describes the green value, and the third byte
  describes the blue value.

   If image depth is 8, each pixel has one byte to describe its color. The value of each byte
  corresponds to an element in colors, which stores 32-bit RGB values where the most-
  significant byte is zero, followed in order by red, green, and blue values. Valid values include
  0 through 255.

   If image depth is 4, the behavior is similar to when image depth is 8 except valid values in
  image include 0 through 15.

   If image depth is 1, any value of zero in image corresponds to element 0 in colors. All other
  values correspond to element 1 in colors.

•     mask —

  mask is an array of bytes in which each bit describes mask information for a pixel. The first
  byte describes the first eight pixels, the second byte describes the next eight pixels, and so
  on.

   If a bit is zero, LabVIEW draws the corresponding pixel as transparent. If the array is empty,
  LabVIEW draws all pixels without transparency. If the array does not contain a bit for each
  pixel in the image, LabVIEW draws any pixels missing from the array without transparency.

•       colors —

  colors is an array of RGB color values that correspond to the values in image. The value of
  image depth determines how LabVIEW interprets the value of this output.


                                                © National Instruments 2101

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2101 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2102 ordinal=2102 -->
## Functions

Functions


                           If image depth is 24, LabVIEW ignores this input.

                           If image depth is 8, the array can have 256 elements.

                           If image depth is 4, the array can have 16 elements.

                           If image depth is 1, the array can have 2 elements.

                     •      Rectangle —

                Rectangle is a cluster that contains coordinates that describe the bounding rectangle of the
                image.

              The VI clips the image to the width and height of the rectangle. The bottom and right edges
                  of the rectangle bounds do not contain image pixels. Horizontal coordinates increase to the
                    right, and vertical coordinates increase to the bottom.

                           •        left —

                          left is the horizontal coordinate of the left edge of the rectangle.

                           •      top —

                   top is the vertical coordinate of the top edge of the rectangle.

                           •       right —

                      right is the horizontal coordinate of the right edge of the rectangle.

                           •     bottom —

                  bottom is the vertical coordinate of the bottom edge of the rectangle.


               •     Mask Color (Black) —

          Mask Color is the color in the image you want to appear transparent for 24-bit, 8-bit, and 4-bit
            images.

           You can wire a color box constant to this input.

               •       1-Bit Mask Value (T) —

2102   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2102 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2103 ordinal=2103 -->
## Functions

Functions


   If 1-Bit Mask Value is TRUE (default), the VI draws all elements in the image array with an index
  of 1 as transparent. If FALSE, the VI draws all elements with an index of 0 as transparent.

  The VI ignores this input if image data does not describe a 1-bit image.

•     Combine Masks? (F) —

   If Combine Masks? is TRUE, the VI combines any existing mask information for the image and
  the mask information you wire to this VI and applies all the mask information to the image. If
  FALSE (default), the VI applies only the mask information you wire to this VI.

•     image data —

  image data describes the image you want to draw or manipulate.

      •     image type —

     image type is reserved for future use.

      •     image depth —

     image depth specifies the color depth of the image, which is the number of bits to use to
      describe the color of each pixel in the image. Valid values include 1, 4, 8, and 24 bits per
        pixel.

     image depth affects how LabVIEW interprets the values of image and colors.

      •     image —

     image is an array of bytes that describes the color of each pixel in the image in raster order.
     The value of image depth determines how LabVIEW interprets the value of this input.

          If image depth is 24, each pixel has three bytes to describe its color. The first byte for each
       pixel describes the red value, the second byte describes the green value, and the third byte
      describes the blue value.

          If image depth is 8, each pixel has one byte to describe its color. The value of each bit
      corresponds to an element in colors, which stores 32-bit RGB values where the most
       significant byte is zero, followed in order by red, green, and blue values. Valid values include
      0 through 255.

          If image depth is 4, the behavior is similar to when image depth is 8 except valid values in


                                                   © National Instruments 2103

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2103 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2104 ordinal=2104 -->
## Functions

Functions


              image include 0 through 15.

                           If image depth is 1, any value of zero in image corresponds to element 0 in colors. All other
                 values correspond to element 1 in colors.

              The size of the array might be larger than expected due to padding.

                     •     mask —

             mask is an array of bytes in which each bit describes mask information for a pixel. The first
                byte describes the first eight pixels, the second byte describes the next eight pixels, and so
                 on.

                           If a bit is zero, LabVIEW draws the corresponding pixel as transparent. If the array is empty,
              LabVIEW draws all pixels without transparency. If the array does not contain a bit for each
                   pixel in the image, LabVIEW draws any pixels missing from the array without transparency.

                     •       colors —

                 colors is an array of RGB color values that correspond to the values in image. The value of
              image depth determines how LabVIEW interprets the value of this input. colors stores 32-bit
            RGB values where the most-significant byte is zero, followed in order by red, green, and blue
                  values. Valid values include 0 through 255.

                           If image depth is 24, LabVIEW ignores this output.

                           If image depth is 8, the array can have 256 elements.

                           If image depth is 4, the array can have 16 elements.

                           If image depth is 1, the array can have 2 elements.

                           If the array is empty for any depth other than 24 bits per pixel, the image is using the default
              LabVIEW color palette.

                     •      Rectangle —

                Rectangle is a cluster that contains coordinates that describe the bounding rectangle in
               which you want to draw the image.

                 Horizontal coordinates increase to the right, and vertical coordinates increase to the


2104   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2104 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2105 ordinal=2105 -->
## Functions

Functions


        bottom.

                •        left —

                left is the horizontal coordinate of the left edge of the rectangle.

                •      top —

            top is the vertical coordinate of the top edge of the rectangle.

                •       right —

              right is the horizontal coordinate of the right edge of the rectangle.

                •     bottom —

           bottom is the vertical coordinate of the bottom edge of the rectangle.


Use the Flatten Pixmap VI to convert a pixmap to a cluster you can wire to image data.
If the image is 4-bit, 8-bit, or 24-bit, wire a color to the Mask Color input. If the image is
1-bit, wire a value to the 1-Bit Mask Value input.

Examples

Refer to the following example files included with LabVIEW.

  • labview\examples\Graphics and Sound\2D Picture Control\
   Using Mask with Picture.vi

PicturePicture toto PixmapPixmap

Converts a picture to a cluster of image data you can use to perform certain tasks with
the image, such as save it to a file using the Graphics Formats VIs.


                                                    © National Instruments 2105

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2105 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2106 ordinal=2106 -->
## Functions

Functions


      Inputs/Outputs

               •       picture —

             picture is the picture you want to convert to a pixmap.

               •       rect —

             rect is a cluster that contains coordinates that describe the bounding rectangle of the image you
          want to convert.

          The default is to return the entire image. Horizontal coordinates increase to the right, and
              vertical coordinates increase to the bottom.

                     •        left —

                     left is the horizontal coordinate of the left edge of the rectangle.

                     •      top —

               top is the vertical coordinate of the top edge of the rectangle.

                     •       right —

                  right is the horizontal coordinate of the right edge of the rectangle.

                     •     bottom —

              bottom is the vertical coordinate of the bottom edge of the rectangle.


               •      depth —

           depth specifies the color depth of the image, which is the number of bits to use to describe the
             color of each pixel in the image. Valid values include 1, 4, 8, and 24 bits per pixel.

          The default is 24.

               •      Background Color —


2106   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2106 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2107 ordinal=2107 -->
## Functions

Functions


  Background Color sets the background color of the image.

•     new picture —

  new picture returns picture unchanged.

•     image data —

  image data returns information about the pixmap so you can use the Graphics Formats VIs to
  save the pixmap to a file.

      •     image type —

     image type is reserved for future use.

      •     image depth —

     image depth specifies the color depth of the image, which is the number of bits to use to
      describe the color of each pixel in the image. Valid values include 1, 4, 8, and 24 bits per
        pixel.

     image depth affects how LabVIEW interprets the values of image and colors.

      •     image —

     image is an array of bytes that describes the color of each pixel in the image in raster order.
     The value of image depth determines how LabVIEW interprets the value of this output.

          If image depth is 24, each pixel has three bytes to describe its color. The first byte for each
       pixel describes the red value, the second byte describes the green value, and the third byte
      describes the blue value.

          If image depth is 8, each pixel has one byte to describe its color. The value of each bit
      corresponds to an element in colors, which stores 32-bit RGB values where the most
       significant byte is zero, followed in order by red, green, and blue values. Valid values include
      0 through 255.

          If image depth is 4, the behavior is similar to when image depth is 8 except valid values in
     image include 0 through 15.

          If image depth is 1, any value of zero in image corresponds to element 0 in colors. All other
      values correspond to element 1 in colors.


                                                   © National Instruments 2107

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2107 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2108 ordinal=2108 -->
## Functions

Functions


              The size of the array might be larger than expected due to padding.

                     •     mask —

             mask is an array of bytes in which each bit describes mask information for a pixel. The first
                byte describes the first eight pixels, the second byte describes the next eight pixels, and so
                 on.

                           If a bit is zero, LabVIEW draws the corresponding pixel as transparent. If the array is empty,
              LabVIEW draws all pixels without transparency. If the array does not contain a bit for each
                   pixel in the image, LabVIEW draws any pixels missing from the array without transparency.

                     •       colors —

                 colors is an array of RGB color values that correspond to the values in image. The value of
              image depth determines how LabVIEW interprets the value of this output.

                           If image depth is 24, LabVIEW ignores this output.

                           If image depth is 8, the array can have 256 elements.

                           If image depth is 4, the array can have 16 elements.

                           If image depth is 1, the array can have 2 elements.

                           If the array is empty for any depth other than 24 bits per pixel, the image is using the default
              LabVIEW color palette.

                     •      Rectangle —

                Rectangle is a cluster that contains coordinates that describe the bounding rectangle of the
                image.

                 Horizontal coordinates increase to the right, and vertical coordinates increase to the
               bottom.

                           •        left —

                          left is the horizontal coordinate of the left edge of the rectangle.

                           •      top —


2108   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2108 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2109 ordinal=2109 -->
## Functions

Functions


            top is the vertical coordinate of the top edge of the rectangle.

                •       right —

              right is the horizontal coordinate of the right edge of the rectangle.

                •     bottom —

           bottom is the vertical coordinate of the bottom edge of the rectangle.


GetGet ImageImage SubsetSubset

Returns a subset of a source image instead of the entire image. Use the Picture to
Pixmap VI to convert a picture to a cluster you can wire to image data.

If you wire 32-bit image data to this VI, the VI strips the alpha channel and returns
24-bit image data.


Inputs/Outputs

   •     image data —

    image data describes the image you want to draw or manipulate.

         •     image type —

       image type is reserved for future use.

         •     image depth —

       image depth specifies the color depth of the image, which is the number of bits to use to


                                                    © National Instruments 2109

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2109 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2110 ordinal=2110 -->
## Functions

Functions


                 describe the color of each pixel in the image. Valid values include 1, 4, 8, and 24 bits per
                    pixel.

              image depth affects how LabVIEW interprets the values of image and colors.

                     •     image —

              image is an array of bytes that describes the color of each pixel in the image in raster order.
              The value of image depth determines how LabVIEW interprets the value of this input.

                           If image depth is 24, each pixel has three bytes to describe its color. The first byte for each
                   pixel describes the red value, the second byte describes the green value, and the third byte
                 describes the blue value.

                           If image depth is 8, each pixel has one byte to describe its color. The value of each byte
                corresponds to an element in colors, which stores 32-bit RGB values where the most-
                   significant byte is zero, followed in order by red, green, and blue values. Valid values include
               0 through 255.

                           If image depth is 4, the behavior is similar to when image depth is 8 except valid values in
              image include 0 through 15.

                           If image depth is 1, any value of zero in image corresponds to element 0 in colors. All other
                 values correspond to element 1 in colors.

                     •     mask —

             mask is an array of bytes in which each bit describes mask information for a pixel. The first
                byte describes the first eight pixels, the second byte describes the next eight pixels, and so
                 on.

                           If a bit is zero, LabVIEW draws the corresponding pixel as transparent. If the array is empty,
              LabVIEW draws all pixels without transparency. If the array does not contain a bit for each
                   pixel in the image, LabVIEW draws any pixels missing from the array without transparency.

                     •       colors —

                 colors is an array of RGB color values that correspond to the values in image. The value of
              image depth determines how LabVIEW interprets the value of this input. colors stores 32-bit
            RGB values where the most-significant byte is zero, followed in order by red, green, and blue
                  values. Valid values include 0 through 255.


2110   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2110 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2111 ordinal=2111 -->
## Functions

Functions


          If image depth is 24, LabVIEW ignores this input.

          If image depth is 8, the array can have 256 elements.

          If image depth is 4, the array can have 16 elements.

          If image depth is 1, the array can have 2 elements.

      •      Rectangle —

      Rectangle is a cluster that contains coordinates that describe the bounding rectangle in
      which you want to draw the image.

     The VI clips the image to the width and height of the rectangle. The bottom and right edges
       of the rectangle bounds do not contain image pixels. Horizontal coordinates increase to the
        right, and vertical coordinates increase to the bottom.

             •        left —

              left is the horizontal coordinate of the left edge of the rectangle.

             •      top —

          top is the vertical coordinate of the top edge of the rectangle.

             •       right —

            right is the horizontal coordinate of the right edge of the rectangle.

             •     bottom —

         bottom is the vertical coordinate of the bottom edge of the rectangle.


•      subset rect —

  subset rect is a cluster that contains coordinates that describe the bounding rectangle of the
  image subset.

   If the coordinates do not describe a valid rectangle, the VI coerces the coordinates to a valid
  rectangle and returns the coerced coordinates in true subset rect.


                                                   © National Instruments 2111

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2111 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2112 ordinal=2112 -->
## Functions

Functions


                     •        left —

                     left is the horizontal coordinate of the left edge of the rectangle.

                     •      top —

               top is the vertical coordinate of the top edge of the rectangle.

                     •       right —

                  right is the horizontal coordinate of the right edge of the rectangle.

                     •     bottom —

              bottom is the vertical coordinate of the bottom edge of the rectangle.


               •     image subset —

          image subset returns information about the image subset so you can use the Draw Flattened
          Pixmap VI to draw the image as a picture or use the Graphics Formats VIs to save the image to a
                  file.

                     •     image type —

              image type is reserved for future use.

                     •     image depth —

              image depth specifies the color depth of the image, which is the number of bits to use to
                 describe the color of each pixel in the image. Valid values include 1, 4, 8, and 24 bits per
                    pixel.

              image depth affects how LabVIEW interprets the values of image and colors.

                     •     image —

              image is an array of bytes that describes the color of each pixel in the image in raster order.
              The value of image depth determines how LabVIEW interprets the value of this output.

                           If image depth is 24, each pixel has three bytes to describe its color. The first byte for each
                   pixel describes the red value, the second byte describes the green value, and the third byte


2112   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2112 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2113 ordinal=2113 -->
## Functions

Functions


  describes the blue value.

   If image depth is 8, each pixel has one byte to describe its color. The value of each bit
  corresponds to an element in colors, which stores 32-bit RGB values where the most
  significant byte is zero, followed in order by red, green, and blue values. Valid values include
  0 through 255.

   If image depth is 4, the behavior is similar to when image depth is 8 except valid values in
  image include 0 through 15.

   If image depth is 1, any value of zero in image corresponds to element 0 in colors. All other
  values correspond to element 1 in colors.

  The size of the array might be larger than expected due to padding.

•     mask —

  mask is an array of bytes in which each bit describes mask information for a pixel. The first
  byte describes the first eight pixels, the second byte describes the next eight pixels, and so
  on.

   If a bit is zero, LabVIEW draws the corresponding pixel as transparent. If the array is empty,
  LabVIEW draws all pixels without transparency. If the array does not contain a bit for each
  pixel in the image, LabVIEW draws any pixels missing from the array without transparency.

•       colors —

  colors is an array of RGB color values that correspond to the values in image. The value of
  image depth determines how LabVIEW interprets the value of this output.

   If image depth is 24, LabVIEW ignores this output.

   If image depth is 8, the array can have 256 elements.

   If image depth is 4, the array can have 16 elements.

   If image depth is 1, the array can have 2 elements.

   If the array is empty for any depth other than 24 bits per pixel, the image is using the default
  LabVIEW color palette.

•      Rectangle —


                                                © National Instruments 2113

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2113 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2114 ordinal=2114 -->
## Functions

Functions


                Rectangle is a cluster that contains coordinates that describe the bounding rectangle of the
                image.

                 Horizontal coordinates increase to the right, and vertical coordinates increase to the
               bottom.

                           •        left —

                          left is the horizontal coordinate of the left edge of the rectangle.

                           •      top —

                   top is the vertical coordinate of the top edge of the rectangle.

                           •       right —

                      right is the horizontal coordinate of the right edge of the rectangle.

                           •     bottom —

                  bottom is the vertical coordinate of the bottom edge of the rectangle.


               •      true subset rect —

            true subset rect is a cluster that contains coordinates that describe the bounding rectangle of
            the image subset returned by the VI.

                     •        left —

                     left is the horizontal coordinate of the left edge of the rectangle.

                     •      top —

               top is the vertical coordinate of the top edge of the rectangle.

                     •       right —

                  right is the horizontal coordinate of the right edge of the rectangle.

                     •     bottom —


2114   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2114 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2115 ordinal=2115 -->
## Functions

Functions


       bottom is the vertical coordinate of the bottom edge of the rectangle.


Examples

Refer to the following example files included with LabVIEW.

  • labview\examples\Graphics and Sound\2D Picture Control\
   Pen Attributes And Image subsetting.vi

EmptyEmpty PicturePicture VIVI

Returns an empty picture. The picture input for all Picture VIs is an empty picture by
default.

You also can create a picture constant for an empty or existing picture and wire the
constant to any picture input. You can resize the constant or right-click it and select
Visible Items»Scrollbar from the shortcut menu to view the entire picture.


Inputs/Outputs

   •     empty picture —

   empty picture is the output.


ColorColor BoxBox ConstantConstant

Use the color box constant to supply a constant color value to the block diagram.

Use the color picker to set the color in the color box constant.

You cannot change the value of the color box constant while the VI runs. You can assign

                                                    © National Instruments 2115

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2115 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2116 ordinal=2116 -->
## Functions

Functions

      a label to this constant.


      ColorColor toto RGBRGB

       Resolves any color input, including system colors, into its respective red, green, and
       blue components.

      To perform a task such as color arithmetic with symbolic colors, you must convert the
       colors to their red, green, and blue components.


      Inputs/Outputs

               •      Color —

            Color is the color that you want to convert to its respective red, green, and blue components.

               •      Resolved Color —

            resolved color is the resolved color in RGB format.

               •     R —

         R is the red component of the RGB value, 0 to 255.

               •     G —

         G is the green component of the RGB value, 0 to 255.

               •     B —

         B is the blue component of the RGB value, 0 to 255.


2116   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2116 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2117 ordinal=2117 -->
## Functions

Functions

RGBRGB toto ColorColor

Converts a red, green, and blue value from 0 to 255 to the corresponding RGB color.


Inputs/Outputs

   •     R —

   R is the red value for the color, 0 to 255.

   •     G —

   G is the green value for the color, 0 to 255.

   •     B —

   B is the blue value for the color, 0 to 255.

   •      Color —

    Color is the RGB color value that corresponds to R, G, and B.

GraphicsGraphics FormatsFormats

Use the Graphics Formats VIs to retrieve or store image data in BMP, JPEG, or PNG
image files.


 Palette Object  Description

 Write JPEG
                Writes a JPEG file.
 File


                                                    © National Instruments 2117

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2117 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2118 ordinal=2118 -->
## Functions

Functions


         Palette Object  Description

         Write PNG File  Writes a PNG file.


         Write BMP File  Writes a Windows bitmap file.


       Read JPEG     Reads a JPEG file and creates the data necessary to display the file in a picture
           File             control.


                     Reads a PNG file and creates the data necessary to display the file in a picture       Read PNG File
                          control.


                     Reads a Windows bitmap file and creates the data necessary to display the file in a
       Read BMP File                         picture control.


         Flatten                       Converts pixmap data from a 2D array to a 1D array.
       Pixmap

         Unflatten
                       Converts a cluster of image data into a 2D array.       Pixmap

       WriteWrite JPEGJPEG FileFile

       Writes a JPEG file.

           If you want to write a pixmap to a file, use the Flatten Pixmap VI to convert the data to
      an image data cluster before using this VI. If you want to write a picture to a file, use
       the Picture to Pixmap VI to convert the data to an image data cluster before using this
         VI.


2118   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2118 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2119 ordinal=2119 -->
## Functions

Functions


Inputs/Outputs

   •       quality (80) —

    quality specifies the level of quality you want for the JPEG using the IJG JPEG library scale,
    which ranges from 0 to 100. The default is 80.

    The scale balances image quality and file size. A value in the 75–95 range produces a compressed
      file with a high-quality image, and a value below 50 produces a smaller file size with a low-
     quality image.

   •      path to JPEG file —

    path to JPEG file specifies the path to and name of the JPEG file to write.

       If you do not specify a path, LabVIEW displays a file dialog box so the user can navigate to the
      file.

   •     image data —

    image data describes the image you want to draw or manipulate.

       If you wire 32-bit image data to this VI, the VI returns a 24-bit pixmap.

         •     image type —

       image type is reserved for future use.

         •     image depth —

       image depth specifies the color depth of the image, which is the number of bits to use to
         describe the color of each pixel in the image. Valid values include 1, 4, 8, and 24 bits per
          pixel.

       image depth affects how LabVIEW interprets the values of image and colors.

         •     image —

       image is an array of bytes that describes the color of each pixel in the image in raster order.


                                                    © National Instruments 2119

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2119 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2120 ordinal=2120 -->
## Functions

Functions


              The value of image depth determines how LabVIEW interprets the value of this input.

                           If image depth is 24, each pixel has three bytes to describe its color. The first byte for each
                   pixel describes the red value, the second byte describes the green value, and the third byte
                 describes the blue value.

                           If image depth is 8, each pixel has one byte to describe its color. The value of each byte
                corresponds to an element in colors, which stores 32-bit RGB values where the most-
                   significant byte is zero, followed in order by red, green, and blue values. Valid values include
               0 through 255.

                           If image depth is 4, the behavior is similar to when image depth is 8 except valid values in
              image include 0 through 15.

                           If image depth is 1, any value of zero in image corresponds to element 0 in colors. All other
                 values correspond to element 1 in colors.

                     •     mask —

             mask is an array of bytes in which each bit describes mask information for a pixel. The first
                byte describes the first eight pixels, the second byte describes the next eight pixels, and so
                 on.

                           If a bit is zero, LabVIEW draws the corresponding pixel as transparent. If the array is empty,
              LabVIEW draws all pixels without transparency. If the array does not contain a bit for each
                   pixel in the image, LabVIEW draws any pixels missing from the array without transparency.

                     •       colors —

                 colors is an array of RGB color values that correspond to the values in image. The value of
              image depth determines how LabVIEW interprets the value of this input. colors stores 32-bit
            RGB values where the most-significant byte is zero, followed in order by red, green, and blue
                  values. Valid values include 0 through 255. In the Write File VIs (BMP, JPEG, and PNG),
              LabVIEW does not have an automatic color table. Use the colors input even for image depth
                  of lower bit value to ensure the best performance of the Write File VIs.

                           If image depth is 24, LabVIEW ignores this input.

                           If image depth is 8, the array can have 256 elements.

                           If image depth is 4, the array can have 16 elements.


2120   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2120 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2121 ordinal=2121 -->
## Functions

Functions


          If image depth is 1, the array can have 2 elements.

      •      Rectangle —

      Rectangle is a cluster that contains coordinates that describe the bounding rectangle of the
      image.

     The bottom and right edges of the rectangle bounds do not contain image pixels. Horizontal
      coordinates increase to the right, and vertical coordinates increase to the bottom.

             •        left —

              left is the horizontal coordinate of the left edge of the rectangle.

             •      top —

          top is the vertical coordinate of the top edge of the rectangle.

             •       right —

            right is the horizontal coordinate of the right edge of the rectangle.

             •     bottom —

         bottom is the vertical coordinate of the bottom edge of the rectangle.


•       error in (no error) —

  error in describes error conditions that occur before this node runs. This input provides
  standard error in functionality.

•      path —

  path specifies the path to the JPEG file.

•       error out —

  error out contains error information. This output provides standard error out functionality.


                                                   © National Instruments 2121

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2121 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2122 ordinal=2122 -->
## Functions

Functions

       WriteWrite PNGPNG FileFile

       Writes a PNG file.

           If you want to write a pixmap to a file, use the Flatten Pixmap VI to convert the data to
      an image data cluster before using this VI. If you want to write a picture to a file, use
       the Picture to Pixmap VI to convert the data to an image data cluster before using this
         VI.


      Inputs/Outputs

               •      compression (default) —

           compression specifies the level of file compression you want for the PNG file.

          The quality of the graphic is not affected by the compression, but the graphic file size and speed
             of compression are affected by this value. Valid values range from –1 to 9 and balance file
           compression with speed. The following table lists example values for compression.

              -1  Good compression and speed (default)
           0   No compression
           1   Best speed with compression
           9   Best compression

               •      path to PNG file —

           path to PNG file specifies the path to and name of the PNG file to write.

                    If you do not specify a path, LabVIEW displays a file dialog box so the user can navigate to the
                  file.

               •     image data —

          image data describes the image you want to draw or manipulate.

                    If you wire 32-bit image data to this VI, the VI returns a 24-bit pixmap.


2122   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2122 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2123 ordinal=2123 -->
## Functions

Functions


•     image type —

  image type is reserved for future use.

•     image depth —

  image depth specifies the color depth of the image, which is the number of bits to use to
  describe the color of each pixel in the image. Valid values include 1, 4, 8, and 24 bits per
   pixel.

  image depth affects how LabVIEW interprets the values of image and colors.

•     image —

  image is an array of bytes that describes the color of each pixel in the image in raster order.
  The value of image depth determines how LabVIEW interprets the value of this input.

   If image depth is 24, each pixel has three bytes to describe its color. The first byte for each
  pixel describes the red value, the second byte describes the green value, and the third byte
  describes the blue value.

   If image depth is 8, each pixel has one byte to describe its color. The value of each byte
  corresponds to an element in colors, which stores 32-bit RGB values where the most-
  significant byte is zero, followed in order by red, green, and blue values. Valid values include
  0 through 255.

   If image depth is 4, the behavior is similar to when image depth is 8 except valid values in
  image include 0 through 15.

   If image depth is 1, any value of zero in image corresponds to element 0 in colors. All other
  values correspond to element 1 in colors.

•     mask —

  mask is an array of bytes in which each bit describes mask information for a pixel. The first
  byte describes the first eight pixels, the second byte describes the next eight pixels, and so
  on.

   If a bit is zero, LabVIEW draws the corresponding pixel as transparent. If the array is empty,
  LabVIEW draws all pixels without transparency. If the array does not contain a bit for each
  pixel in the image, LabVIEW draws any pixels missing from the array without transparency.

•       colors —


                                                © National Instruments 2123

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2123 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2124 ordinal=2124 -->
## Functions

Functions


                 colors is an array of RGB color values that correspond to the values in image. The value of
              image depth determines how LabVIEW interprets the value of this input. colors stores 32-bit
            RGB values where the most-significant byte is zero, followed in order by red, green, and blue
                  values. Valid values include 0 through 255. In the Write File VIs (BMP, JPEG, and PNG),
              LabVIEW does not have an automatic color table. Use the colors input even for image depth
                  of lower bit value to ensure the best performance of the Write File VIs.

                           If image depth is 24, LabVIEW ignores this input.

                           If image depth is 8, the array can have 256 elements.

                           If image depth is 4, the array can have 16 elements.

                           If image depth is 1, the array can have 2 elements.

                     •      Rectangle —

                Rectangle is a cluster that contains coordinates that describe the bounding rectangle of the
                image.

              The bottom and right edges of the rectangle bounds do not contain image pixels. Horizontal
                coordinates increase to the right, and vertical coordinates increase to the bottom.

                           •        left —

                          left is the horizontal coordinate of the left edge of the rectangle.

                           •      top —

                   top is the vertical coordinate of the top edge of the rectangle.

                           •       right —

                      right is the horizontal coordinate of the right edge of the rectangle.

                           •     bottom —

                  bottom is the vertical coordinate of the bottom edge of the rectangle.


               •       error in (no error) —


2124   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2124 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2125 ordinal=2125 -->
## Functions

Functions


    error in describes error conditions that occur before this node runs. This input provides
    standard error in functionality.

   •      path —

    path specifies the path to the PNG file.

   •       error out —

    error out contains error information. This output provides standard error out functionality.


WriteWrite BMPBMP FileFile

Writes a Windows bitmap file.

If you want to write a pixmap to a file, use the Flatten Pixmap VI to convert the data to
an image data cluster before using this VI. If you want to write a picture to a file, use
the Picture to Pixmap VI to convert the data to an image data cluster before using this
VI.


Inputs/Outputs

   •      path to BMP file —

    path to BMP file specifies the path to and name of the bitmap file to write.

       If you do not specify a path, LabVIEW displays a file dialog box so the user can navigate to the
      file.

   •     image data —

    image data describes the image you want to draw or manipulate.

       If you wire 32-bit image data to this VI, the VI returns a 24-bit pixmap.


                                                    © National Instruments 2125

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2125 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2126 ordinal=2126 -->
## Functions

Functions


                     •     image type —

              image type is reserved for future use.

                     •     image depth —

              image depth specifies the color depth of the image, which is the number of bits to use to
                 describe the color of each pixel in the image. Valid values include 1, 4, 8, and 24 bits per
                    pixel.

              image depth affects how LabVIEW interprets the values of image and colors.

                     •     image —

              image is an array of bytes that describes the color of each pixel in the image in raster order.
              The value of image depth determines how LabVIEW interprets the value of this input.

                           If image depth is 24, each pixel has three bytes to describe its color. The first byte for each
                   pixel describes the red value, the second byte describes the green value, and the third byte
                 describes the blue value.

                           If image depth is 8, each pixel has one byte to describe its color. The value of each byte
                corresponds to an element in colors, which stores 32-bit RGB values where the most-
                   significant byte is zero, followed in order by red, green, and blue values. Valid values include
               0 through 255.

                           If image depth is 4, the behavior is similar to when image depth is 8 except valid values in
              image include 0 through 15.

                           If image depth is 1, any value of zero in image corresponds to element 0 in colors. All other
                 values correspond to element 1 in colors.

                     •     mask —

             mask is an array of bytes in which each bit describes mask information for a pixel. The first
                byte describes the first eight pixels, the second byte describes the next eight pixels, and so
                 on.

                           If a bit is zero, LabVIEW draws the corresponding pixel as transparent. If the array is empty,
              LabVIEW draws all pixels without transparency. If the array does not contain a bit for each
                   pixel in the image, LabVIEW draws any pixels missing from the array without transparency.

                     •       colors —


2126   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2126 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2127 ordinal=2127 -->
## Functions

Functions


       colors is an array of RGB color values that correspond to the values in image. The value of
     image depth determines how LabVIEW interprets the value of this input. colors stores 32-bit
     RGB values where the most-significant byte is zero, followed in order by red, green, and blue
       values. Valid values include 0 through 255. In the Write File VIs (BMP, JPEG, and PNG),
      LabVIEW does not have an automatic color table. Use the colors input even for image depth
       of lower bit value to ensure the best performance of the Write File VIs.

          If image depth is 24, LabVIEW ignores this input.

          If image depth is 8, the array can have 256 elements.

          If image depth is 4, the array can have 16 elements.

          If image depth is 1, the array can have 2 elements.

      •      Rectangle —

      Rectangle is a cluster that contains coordinates that describe the bounding rectangle of the
      image.

     The bottom and right edges of the rectangle bounds do not contain image pixels. Horizontal
      coordinates increase to the right, and vertical coordinates increase to the bottom.

             •        left —

              left is the horizontal coordinate of the left edge of the rectangle.

             •      top —

          top is the vertical coordinate of the top edge of the rectangle.

             •       right —

            right is the horizontal coordinate of the right edge of the rectangle.

             •     bottom —

         bottom is the vertical coordinate of the bottom edge of the rectangle.


•       error in (no error) —


                                                   © National Instruments 2127

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2127 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2128 ordinal=2128 -->
## Functions

Functions


             error in describes error conditions that occur before this node runs. This input provides
            standard error in functionality.

               •      path —

           path specifies the path of the pixmap.

               •       error out —

             error out contains error information. This output provides standard error out functionality.


     ReadRead JPEGJPEG FileFile

      Reads a JPEG file and creates the data necessary to display the file in a picture control.

      Use the Draw Flattened Pixmap VI to display the bitmap you acquire with this VI. Use
       the Unflatten Pixmap VI to work with the data as a 2D array.

           Note This VI automatically reads JPEG files as 24-bit images.


      Inputs/Outputs

               •      path to JPEG file —

           path to JPEG file specifies the path to and name of the JPEG file to read.

                    If you do not specify a path, LabVIEW displays a file dialog box so the user can navigate to the
                  file.

               •       error in (no error) —

             error in describes error conditions that occur before this node runs. This input provides
            standard error in functionality.

               •      use 8 bit color table —

2128   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2128 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2129 ordinal=2129 -->
## Functions

Functions


  use 8 bit color table reads the JPEG file at an 8 bit per pixel image depth instead of 24 bit per
  pixel image depth. The default value is FALSE.

•      path —

  path specifies the path of the pixmap.

•     image data —

  image data returns information about the image so you can use the Draw Flattened Pixmap VI to
  draw it as a picture.

      •     image type —

     image type is reserved for future use.

      •     image depth —

     image depth specifies the color depth of the image, which is the number of bits to use to
      describe the color of each pixel in the image. Valid values include 1, 4, 8, and 24 bits per
        pixel.

     image depth affects how LabVIEW interprets the values of image and colors.

      •     image —

     image is an array of bytes that describes the color of each pixel in the image in raster order.
     The value of image depth determines how LabVIEW interprets the value of this output.

          If image depth is 24, each pixel has three bytes to describe its color. The first byte for each
       pixel describes the red value, the second byte describes the green value, and the third byte
      describes the blue value.

          If image depth is 8, each pixel has one byte to describe its color. The value of each bit
      corresponds to an element in colors, which stores 32-bit RGB values where the most
       significant byte is zero, followed in order by red, green, and blue values. Valid values include
      0 through 255.

     The size of the array might be larger than expected due to padding.

      •     mask —


                                                   © National Instruments 2129

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2129 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2130 ordinal=2130 -->
## Functions

Functions


             mask is an array of bytes in which each bit describes mask information for a pixel. The first
                byte describes the first eight pixels, the second byte describes the next eight pixels, and so
                 on. In this VI, the mask array is always empty.

                Since the array is empty, LabVIEW draws all pixels without transparency.

                     •       colors —

                 colors is an array of RGB color values that correspond to the values in image. The value of
              image depth determines how LabVIEW interprets the value of this output.

                           If image depth is 24, LabVIEW ignores this output.

                           If image depth is 8, the array can have 256 elements.

                           If the array is empty for any depth other than 24 bits per pixel, the image is using the default
              LabVIEW color palette.

                     •      Rectangle —

                Rectangle is a cluster that contains coordinates that describe the bounding rectangle of the
                image.

                 Horizontal coordinates increase to the right, and vertical coordinates increase to the
               bottom.

                           •        left —

                          left is the horizontal coordinate of the left edge of the rectangle.

                           •      top —

                   top is the vertical coordinate of the top edge of the rectangle.

                           •       right —

                      right is the horizontal coordinate of the right edge of the rectangle.

                           •     bottom —


2130   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2130 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2131 ordinal=2131 -->
## Functions

Functions


           bottom is the vertical coordinate of the bottom edge of the rectangle.


   •       error out —

    error out contains error information. This output provides standard error out functionality.


ReadRead PNGPNG FileFile

Reads a PNG file and creates the data necessary to display the file in a picture control.

Use the Draw Flattened Pixmap VI to display the bitmap you acquire with this VI. Use
the Unflatten Pixmap VI to work with the data as a 2D array.

      Note This VI can read 32-bit PNG files.


Inputs/Outputs

   •      path to PNG file —

    path to PNG file specifies the path to and name of the PNG file to read.

       If you do not specify a path, LabVIEW displays a file dialog box so the user can navigate to the
      file.

   •       error in (no error) —

    error in describes error conditions that occur before this node runs. This input provides
    standard error in functionality.

   •      Transparency Thresh —


                                                    © National Instruments 2131

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2131 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2132 ordinal=2132 -->
## Functions

Functions


           Transparency Thresh incorporates alpha information for a 32-bit PNG image into the mask of
            the resulting image data. LabVIEW treats as opaque any alpha values equal to or greater than
           Transparency Thresh. LabVIEW treats all other alpha values as fully transparent. The value of
           Transparency Thresh must be between 0 and 255.

               •      path —

           path specifies the path of the pixmap.

               •     image data —

          image data returns information about the image so you can use the Draw Flattened Pixmap VI to
          draw it as a picture.

                     •     image type —

              image type is reserved for future use.

                     •     image depth —

              image depth specifies the color depth of the image, which is the number of bits to use to
                 describe the color of each pixel in the image. Valid values include 1, 4, 8, 24, and 32 bits
                per pixel.

              image depth affects how LabVIEW interprets the values of image and colors.

                     •     image —

              image is an array of bytes that describes the color of each pixel in the image in raster order.
              The value of image depth determines how LabVIEW interprets the value of this output.

                           If image depth is 32, each pixel has three bytes to describe its color, and a fourth byte to
                 describe transparency. The fourth byte is known as the 8-bit alpha channel. The first byte
                   for each pixel describes the red value, the second byte describes the green value, and the
                  third byte describes the blue value.

                           If image depth is 24, each pixel has three bytes to describe its color. When the image depth
                      is 24, the behavior is similar to when image depth is 32. However, 24-bit images do not
               have an extra fourth byte to describe transparency.

                           If image depth is 8, each pixel has one byte to describe its color. The value of each bit
                corresponds to an element in colors, which stores 32-bit RGB values where the most


2132   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2132 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2133 ordinal=2133 -->
## Functions

Functions


  significant byte is zero, followed in order by red, green, and blue values. Valid values include
  0 through 255.

   If image depth is 4, the behavior is similar to when image depth is 8 except valid values in
  image include 0 through 15.

   If image depth is 1, any value of zero in image corresponds to element 0 in colors. All other
  values correspond to element 1 in colors.

  The size of the array might be larger than expected due to padding.

•     mask —

  mask is an array of bytes in which each bit describes mask information for a pixel. The first
  byte describes the first eight pixels, the second byte describes the next eight pixels, and so
  on.

  In 32-bit cases, the mask is always filled. For all other cases in this VI, the mask array is
  empty. If the array is empty, LabVIEW draws all pixels without transparency. If the array does
  not contain a bit for each pixel in the image, LabVIEW draws any pixels missing from the
  array without transparency.

•       colors —

  colors is an array of RGB color values that correspond to the values in image. The value of
  image depth determines how LabVIEW interprets the value of this output.

   If image depth is 32 or 24, LabVIEW ignores this output.

   If image depth is 8, the array can have 256 elements.

   If image depth is 4, the array can have 16 elements.

   If image depth is 1, the array can have 2 elements.

   If the array is empty for any depth other than 24 bits per pixel, the image is using the default
  LabVIEW color palette.

•      Rectangle —

  Rectangle is a cluster that contains coordinates that describe the bounding rectangle of the


                                                © National Instruments 2133

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2133 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2134 ordinal=2134 -->
## Functions

Functions


                image.

                 Horizontal coordinates increase to the right, and vertical coordinates increase to the
               bottom.

                           •        left —

                          left is the horizontal coordinate of the left edge of the rectangle.

                           •      top —

                   top is the vertical coordinate of the top edge of the rectangle.

                           •       right —

                      right is the horizontal coordinate of the right edge of the rectangle.

                           •     bottom —

                  bottom is the vertical coordinate of the bottom edge of the rectangle.


               •       error out —

             error out contains error information. This output provides standard error out functionality.


      You might receive an error if you attempt to read a PNG file whose image type is not
      supported in LabVIEW. LabVIEW supports JPG, BMP, and PNG images. To load a PNG
      image with an unsupported image type in LabVIEW, use a third-party graphics format
       converter to save the image as a standard file format that LabVIEW can load (JPG, BMP,
       or PNG).

     ReadRead BMPBMP FileFile

      Reads a Windows bitmap file and creates the data necessary to display the file in a
       picture control.

      Use the Draw Flattened Pixmap VI to display the bitmap you acquire with this VI. Use


2134   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2134 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2135 ordinal=2135 -->
## Functions

Functions

the Unflatten Pixmap VI to work with the data as a 2D array.


Inputs/Outputs

   •      path to BMP file —

    path to BMP file specifies the path to and name of the bitmap file to read.

       If you do not specify a path, LabVIEW displays a file dialog box so the user can navigate to the
      file.

   •       error in (no error) —

    error in describes error conditions that occur before this node runs. This input provides
    standard error in functionality.

   •      path —

    path specifies the path of the pixmap.

   •     image data —

    image data returns information about the image so you can use the Draw Flattened Pixmap VI to
    draw it as a picture.

         •     image type —

       image type is reserved for future use.

         •     image depth —

       image depth specifies the color depth of the image, which is the number of bits to use to
         describe the color of each pixel in the image. Valid values include 1, 4, 8, and 24 bits per
          pixel.

       image depth affects how LabVIEW interprets the values of image and colors.

         •     image —


                                                    © National Instruments 2135

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2135 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2136 ordinal=2136 -->
## Functions

Functions


              image is an array of bytes that describes the color of each pixel in the image in raster order.
              The value of image depth determines how LabVIEW interprets the value of this output.

                           If image depth is 24, each pixel has three bytes to describe its color. The first byte for each
                   pixel describes the red value, the second byte describes the green value, and the third byte
                 describes the blue value.

                           If image depth is 8, each pixel has one byte to describe its color. The value of each bit
                corresponds to an element in colors, which stores 32-bit RGB values where the most
                   significant byte is zero, followed in order by red, green, and blue values. Valid values include
               0 through 255.

                           If image depth is 4, the behavior is similar to when image depth is 8 except valid values in
              image include 0 through 15.

                           If image depth is 1, any value of zero in image corresponds to element 0 in colors. All other
                 values correspond to element 1 in colors.

              The size of the array might be larger than expected due to padding.

                     •     mask —

             mask is an array of bytes in which each bit describes mask information for a pixel. The first
                byte describes the first eight pixels, the second byte describes the next eight pixels, and so
                 on. In this VI, the mask array is always empty.

                Since the array is empty, LabVIEW draws all pixels without transparency.

                     •       colors —

                 colors is an array of RGB color values that correspond to the values in image. The value of
              image depth determines how LabVIEW interprets the value of this output.

                           If image depth is 24, LabVIEW ignores this output.

                           If image depth is 8, the array can have 256 elements.

                           If image depth is 4, the array can have 16 elements.

                           If image depth is 1, the array can have 2 elements.


2136   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2136 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2137 ordinal=2137 -->
## Functions

Functions


              If the array is empty for any depth other than 24 bits per pixel, the image is using the default
       LabVIEW color palette. In this VI, the array is always filled up for 8, 4, and 1 bit cases.

         •      Rectangle —

        Rectangle is a cluster that contains coordinates that describe the bounding rectangle of the
        image.

         Horizontal coordinates increase to the right, and vertical coordinates increase to the
        bottom.

                •        left —

                left is the horizontal coordinate of the left edge of the rectangle.

                •      top —

            top is the vertical coordinate of the top edge of the rectangle.

                •       right —

              right is the horizontal coordinate of the right edge of the rectangle.

                •     bottom —

           bottom is the vertical coordinate of the bottom edge of the rectangle.


   •       error out —

    error out contains error information. This output provides standard error out functionality.


FlattenFlatten PixmapPixmap

Converts pixmap data from a 2D array to a 1D array.

You can write the resulting 1D array to a file or use the low-level Draw Flattened
Pixmap VI to view it.


                                                    © National Instruments 2137

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2137 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2138 ordinal=2138 -->
## Functions

Functions


      Inputs/Outputs

               •      top left —

           top left specifies in coordinates where to place the top-left corner of the image.

                     •      x —

               x is the horizontal coordinate that increases to the right.

                     •      y —

               y is the vertical coordinate that increases to the bottom.


               •       24-bit pixmap —

             24-bit pixmap is the 2D array of data to convert to image data.

          The dimensions of the image data match the dimensions of this array.

               •       8-bit pixmap —

              8-bit pixmap is the 2D array of data to convert to image data.

          The dimensions of the image data match the dimensions of this array. The VI uses the data as
            indexes into the color array.

               •       4-bit pixmap —

              4-bit pixmap is the 2D array of data to convert to image data.

          The dimensions of the image data match the dimensions of this array. The VI uses the data as
            indexes into the color array.

               •       1-bit pixmap —


2138   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2138 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2139 ordinal=2139 -->
## Functions

Functions


  1-bit pixmap is the 2D array of data to convert to image data.

  The dimensions of the image data match the dimensions of this array. Elements that are FALSE
  map to element 0 in the color table. Elements that are TRUE map to element 1 in the color table.

•       colors —

  colors is an array of RGB color values that correspond to the values in the pixmap input you
  wire. Which pixmap input you wire determines how LabVIEW interprets the value of this input.

   If you wire data to 24-bit pixmap, LabVIEW ignores this input. If you wire data to 8-bit pixmap,
  the array can have 256 elements. If you wire data to 4-bit pixmap, the array can have 16
  elements. If you wire data to 1-bit pixmap, the array can have 2 elements. If the colors array is
  empty for any depth other than 24 bits per pixel, the image uses the default LabVIEW color
  palette.

•     mask —

  mask is a 1D array that describes mask information for each pixel.

   If the mask array is empty, LabVIEW draws all resulting pixels without transparency.

•     image data —

  image data returns information about the pixmap so you can use the Draw Flattened Pixmap VI
  to draw the pixmap as a picture or use the Graphics Formats VIs to save the pixmap to a file.

      •     image type —

     image type is reserved for future use.

      •     image depth —

     image depth specifies the color depth of the image, which is the number of bits to use to
      describe the color of each pixel in the image. Valid values include 1, 4, 8, and 24 bits per
        pixel.

     image depth affects how LabVIEW interprets the values of image and colors.

      •     image —

     image is an array of bytes that describes the color of each pixel in the image in raster order.


                                                   © National Instruments 2139

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2139 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2140 ordinal=2140 -->
## Functions

Functions


              The value of image depth determines how LabVIEW interprets the value of this output.

                           If image depth is 24, each pixel has three bytes to describe its color. The first byte for each
                   pixel describes the red value, the second byte describes the green value, and the third byte
                 describes the blue value.

                           If image depth is 8, each pixel has one byte to describe its color. The value of each bit
                corresponds to an element in colors, which stores 32-bit RGB values where the most
                   significant byte is zero, followed in order by red, green, and blue values. Valid values include
               0 through 255.

                           If image depth is 4, the behavior is similar to when image depth is 8 except valid values in
              image include 0 through 15.

                           If image depth is 1, any value of zero in image corresponds to element 0 in colors. All other
                 values correspond to element 1 in colors.

              The size of the array might be larger than expected due to padding.

                     •     mask —

             mask is an array of bytes in which each bit describes mask information for a pixel. The first
                byte describes the first eight pixels, the second byte describes the next eight pixels, and so
                 on.

                           If a bit is zero, LabVIEW draws the corresponding pixel as transparent. If the array is empty,
              LabVIEW draws all pixels without transparency. If the array does not contain a bit for each
                   pixel in the image, LabVIEW draws any pixels missing from the array without transparency.

                     •       colors —

                 colors is an array of RGB color values that correspond to the values in image. The value of
              image depth determines how LabVIEW interprets the value of this output.

                           If image depth is 24, LabVIEW ignores this output.

                           If image depth is 8, the array can have 256 elements.

                           If image depth is 4, the array can have 16 elements.

                           If image depth is 1, the array can have 2 elements.


2140   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2140 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2141 ordinal=2141 -->
## Functions

Functions


              If the array is empty for any depth other than 24 bits per pixel, the image is using the default
       LabVIEW color palette.

         •      Rectangle —

        Rectangle is a cluster that contains coordinates that describe the bounding rectangle of the
        image.

         Horizontal coordinates increase to the right, and vertical coordinates increase to the
        bottom.

                •        left —

                left is the horizontal coordinate of the left edge of the rectangle.

                •      top —

            top is the vertical coordinate of the top edge of the rectangle.

                •       right —

              right is the horizontal coordinate of the right edge of the rectangle.

                •     bottom —

           bottom is the vertical coordinate of the bottom edge of the rectangle.


UnflattenUnflatten PixmapPixmap

Converts a cluster of image data into a 2D array.


                                                    © National Instruments 2141

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2141 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2142 ordinal=2142 -->
## Functions

Functions

      Inputs/Outputs

               •     image data —

          image data describes the image you want to draw or manipulate.

                    If you wire 32-bit image data to this VI, the VI returns a 24-bit pixmap.

                     •     image type —

              image type is reserved for future use.

                     •     image depth —

              image depth specifies the color depth of the image, which is the number of bits to use to
                 describe the color of each pixel in the image. Valid values include 1, 4, 8, and 24 bits per
                    pixel.

              image depth affects how LabVIEW interprets the values of image and colors.

                     •     image —

              image is an array of bytes that describes the color of each pixel in the image in raster order.
              The value of image depth determines how LabVIEW interprets the value of this input.

                           If image depth is 24, each pixel has three bytes to describe its color. The first byte for each
                   pixel describes the red value, the second byte describes the green value, and the third byte
                 describes the blue value.

                           If image depth is 8, each pixel has one byte to describe its color. The value of each byte
                corresponds to an element in colors, which stores 32-bit RGB values where the most-
                   significant byte is zero, followed in order by red, green, and blue values. Valid values include
               0 through 255.

                           If image depth is 4, the behavior is similar to when image depth is 8 except valid values in
              image include 0 through 15.

                           If image depth is 1, any value of zero in image corresponds to element 0 in colors. All other
                 values correspond to element 1 in colors.

                     •     mask —

             mask is an array of bytes in which each bit describes mask information for a pixel. The first


2142   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2142 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2143 ordinal=2143 -->
## Functions

Functions


  byte describes the first eight pixels, the second byte describes the next eight pixels, and so
  on.

   If a bit is zero, LabVIEW draws the corresponding pixel as transparent. If the array is empty,
  LabVIEW draws all pixels without transparency. If the array does not contain a bit for each
  pixel in the image, LabVIEW draws any pixels missing from the array without transparency.

•       colors —

  colors is an array of RGB color values that correspond to the values in image. The value of
  image depth determines how LabVIEW interprets the value of this input. colors stores 32-bit
  RGB values where the most-significant byte is zero, followed in order by red, green, and blue
  values. Valid values include 0 through 255.

   If image depth is 24, LabVIEW ignores this input.

   If image depth is 8, the array can have 256 elements.

   If image depth is 4, the array can have 16 elements.

   If image depth is 1, the array can have 2 elements.

•      Rectangle —

  Rectangle is a cluster that contains coordinates that describe the bounding rectangle of the
  image.

  The bottom and right edges of the rectangle bounds do not contain image pixels. Horizontal
  coordinates increase to the right, and vertical coordinates increase to the bottom.

      •        left —

        left is the horizontal coordinate of the left edge of the rectangle.

      •      top —

      top is the vertical coordinate of the top edge of the rectangle.

      •       right —


                                                © National Instruments 2143

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2143 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2144 ordinal=2144 -->
## Functions

Functions


                      right is the horizontal coordinate of the right edge of the rectangle.

                           •     bottom —

                  bottom is the vertical coordinate of the bottom edge of the rectangle.


               •      top left —

           top left is a cluster that contains a horizontal (x) and a vertical (y) component.

                     •      x —

               x is the horizontal coordinate that increases to the right.

                     •      y —

               y is the vertical coordinate that increases to the bottom.


               •       24-bit pixmap —

             24-bit pixmap returns the 2D array of data to draw as a pixmap.

          The dimensions of the pixmap match the dimensions of this array.

               •       8-bit pixmap —

              8-bit pixmap returns the 2D array of data to draw as a pixmap.

          The dimensions of the pixmap match the dimensions of this array. The VI uses the data as
            indexes in the colors output.

               •       4-bit pixmap —

              4-bit pixmap returns the 2D array of data to draw as a pixmap.

          The dimensions of the pixmap match the dimensions of this array. The VI uses the data as
            indexes in the colors output.

               •       1-bit pixmap —

2144   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2144 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2145 ordinal=2145 -->
## Functions

Functions


     1-bit pixmap returns the 2D array of data to draw as a bitmap.

    The dimensions of the bitmap match the dimensions of this array. Elements that are FALSE map
    to element 0 in the colors output and elements that are TRUE map to element 1.

   •       colors —

    colors is an array of RGB color values that correspond to the values in the pixmap output.

    For the 24-bit pixmap, LabVIEW ignores this output. For the 8-bit pixmap, the array can have
    256 elements. For the 4-bit pixmap, the array can have 16 elements. For the 1-bit pixmap, the
    array can have 2 elements.

   •     mask —

   mask is an array of bytes in which each bit describes mask information for a pixel. The first byte
    describes the first eight pixels, the second byte describes the next eight pixels, and so on.

       If a bit is zero, LabVIEW draws the corresponding pixel as transparent. If the array is empty,
    LabVIEW draws all pixels without transparency. If the array does not contain a bit for each pixel
     in the image, LabVIEW draws any pixels missing from the array without transparency.


When you use a Graphics Formats VI to read a graphics file, the VI returns the image
data in a cluster. Use the Draw Unflattened Pixmap VI to display the data directly or use
the Unflatten Pixmap VI to convert the data to a more useful 2D representation.

In this VI, only one of the various pixmap outputs (24-bit, 8-bit, 4-bit, or 1-bit) is valid at
a time. In other words, this VI will not produce an output of two different pixmap
values.

BeepBeep (Windows)(Windows)

Causes the system to issue an audible tone. (Windows Vista 64-bit) This VI might not
work correctly if use system alert? is FALSE.


                                                    © National Instruments 2145

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2145 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2146 ordinal=2146 -->
## Functions

Functions

      Inputs/Outputs

               •      frequency (Hz) —

           frequency (Hz) is the frequency of the tone in Hertz. LabVIEW ignores this parameter when use
           system alert? is TRUE.

               •      duration (msec) —

            duration (msec) is the duration of the tone in milliseconds. LabVIEW ignores this parameter
          when use system alert? is TRUE.

               •      use system alert? (T) —

           use system alert? specifies whether LabVIEW uses the default system alert and ignores
           frequency (Hz) and duration (msec). If FALSE, this VI makes a synchronous beep using the
             specified frequency and duration.

          The default is TRUE.

     SoundSound

      Use the Sound VIs to play sounds.

      (Windows) You must have DirectX 8.0 or later to use the Sound VIs.

       (Linux) You must have the Open Sound System (OSS) driver to use the Sound VIs.
      LabVIEW searches for input and output devices by looking for files named /dev/dsp
       or /dev/dspX, where X is an integer between 0 and 16. LabVIEW attempts to open
      each input and output device. If LabVIEW cannot detect the sound card, check that a
       device file named /dev/dsp or /dev/dspX exists on the local system and that you
      have permission to read from and write to the device. If you moved this device to a
       location other than the default, LabVIEW can work with a symbolic link.


2146   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2146 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2147 ordinal=2147 -->
## Functions

Functions


 Palette Object   Description

 Output         Use the Sound Output VIs to configure and control a sound output device.


 Input          Use the Sound Input VIs to configure and control a sound input device.


 Files           Use the Sound Files VIs to create and retrieve PC wave files (.wav).


OutputOutput

Use the Sound Output VIs to configure and control a sound output device.

(Windows) You must have DirectX 8.0 or later to use the Sound Output VIs.

(Linux) You must have the Open Sound System (OSS) driver to use this VI. LabVIEW
searches for input and output devices by looking for files named /dev/dsp or /dev/
dspX, where X is an integer between 0 and 16. LabVIEW attempts to open each input
and output device. If LabVIEW cannot detect the sound card, check that a device file
named /dev/dsp or /dev/dspX exists on the local system and that you have
permission to read from and write to the device. If you moved this device to a location
other than the default, LabVIEW can work with a symbolic link.


 Palette
            Description
 Object

 Play       Plays data from the sound output device using finite sampling. This Express VI
 Waveform  automatically configures an output task and clears the task after the output completes.

 Sound
 Output    Configures a sound output device to generate data. Use the Sound Output Write VI to
 Configure


                                                    © National Instruments 2147

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2147 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2148 ordinal=2148 -->
## Functions

Functions


         Palette                    Description
        Object

                     write the data to the device.


       Sound                      Starts playback from the device. This VI is necessary only if the Sound Output Stop VI        Output                  has previously been called.          Start


       Sound     Writes data to a sound output device. You must use the Sound Output Configure VI to
        Output     configure the device if you are writing continuously. You must manually select the
         Write      polymorphic instance you want to use.


       Sound                   Stops the device from playing sound from the buffer. Use the Sound Output Clear VI to        Output
                      clear the data in the buffer. Use the Sound Output Start VI to restart output.        Stop

       Sound                   Stops the device from playing sound, clears the buffer, returns the task to the default        Output                       state, and clears the resources associated with the task. The task becomes invalid.
         Clear

       Sound
        Output    Waits until all of the sound is played by the output device.
        Wait

       Sound
        Output    Returns information about the current state of a sound output task.
          Info

       Sound
        Output
                    Sets the volume at which the sound output device plays.
         Set
       Volume

         Play
       Sound    Opens a file and starts playing it immediately.
           File


2148   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2148 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2149 ordinal=2149 -->
## Functions

Functions

PlayPlay WaveformWaveform

Plays data from the sound output device using finite sampling. This Express VI
automatically configures an output task and clears the task after the output
completes.

(Windows) You must have DirectX 8.0 or later to use this VI. (Linux) You must have the
Open Sound System (OSS) driver to use this VI.


Dialog Box Options

 Option           Description

 Device              Lists the sound devices you have connected.

                  Contains the following options:

                               • Min sample rate (Hz)—

                      Returns the minimum output sample rate the selected device supports.

                               • Max sample rate (Hz)—

 Device               Returns the maximum output sample rate the selected device supports.
 capabilities
                               • Resolution (bits)—

                         Specifies the quality of each sample in bits. The default is 16 bits.

                               • #Channels—

                         Specifies the number of channels. 1 is Mono, and 2 is Stereo.


 Test Device        Tests the selected sound device by playing a 500 Hz tone for approximately 1/4


                                                    © National Instruments 2149

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2149 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2150 ordinal=2150 -->
## Functions

Functions


        Option           Description

                          second.


      Inputs/Outputs

               •      Device —

               Lists the sound devices you have connected.

               •       error in —

          The error in cluster can accept error information wired from VIs previously called. Use this
            information to decide if any functionality should be bypassed in the event of errors from other
               VIs. The pop-up option Explain Error (or Explain Warning) gives more information about the
             error displayed.

               •      Data —

             Specifies the data this Express VI plays.

           You can wire a waveform, an array of waveforms (one waveform per channel), or the Data output
             of the Acquire Sound Express VI to this input. The Play Waveform Express VI uses the timing
            information the waveform data type specifies to play back sound.

               •       error out —

          The error out cluster passes error or warning information out of a VI to be used by other VIs. The
           pop-up option Explain Error (or Explain Warning) gives more information about the error
             displayed.


     Components

       Specifies the number of channels. 1 is Mono, and 2 is Stereo.

       Specifies the quality of each sample in bits. The default is 16 bits.

       Returns the maximum output sample rate the selected device supports.

       Returns the minimum output sample rate the selected device supports.

2150   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2150 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2151 ordinal=2151 -->
## Functions

Functions

Lists the sound devices you have connected.

The error out cluster passes error or warning information out of a VI to be used by
other VIs. The pop-up option Explain Error (or Explain Warning) gives more
information about the error displayed.

The source string describes the origin of the error or warning. The pop-up option
Explain Error (or Explain Warning) gives more information about the error displayed.

The code input identifies the error or warning. The pop-up option Explain Error (or
Explain Warning) gives more information about the error displayed.

The status boolean is either TRUE (X) for an error, or FALSE (checkmark) for no error or
a warning. The pop-up option Explain Error (or Explain Warning) gives more
information about the error displayed.

Tests the selected sound device by playing a 500 Hz tone for approximately 1/4 second.
SoundSound OutputOutput ConfigureConfigure

Configures a sound output device to generate data. Use the Sound Output Write VI to
write the data to the device.

(Windows) You must have DirectX 8.0 or later to use this VI. (Linux) You must have the
Open Sound System (OSS) driver to use this VI.


Inputs/Outputs

   •     number of samples/ch —

   number of samples/ch specifies the number of samples per channel in the buffer.


                                                    © National Instruments 2151

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2151 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2152 ordinal=2152 -->
## Functions

Functions


           Use a large number of samples for continuous operations. Use a smaller number of samples if
           you want to use less memory.

               •     sample mode —

           sample mode specifies whether you intend to write just once (Finite Samples) or continuously
           (Continuous Samples).

              In Finite Samples mode, call Sound Output Write only until you have written the number of
           samples specified in number of samples/ch. In Continuous Samples mode, you can call Sound
           Output Write repeatedly as needed.

               •      device ID —

            device ID is the input or output device you access for a sound operation. In general, most users
            should select the default value of 0.

          The value ranges from 0 to n–1, where nis the number of input or output devices on the
            computer.

               •     sound format —

          sound format sets the playing rate, the number of channels, and the bits per sample of the
           sound operation. The values for each of these controls is dependent on your sound card.

               Note Setting sample rate (S/s) and bits per sample high uses more of the computer
                memory when the VI runs. Also, not all operating systems and sound cards support
                            all sound format options.

                     •     sample rate (S/s) —

              sample rate (S/s) sets the sampling rate for the sound operation. Common rates are 44,100
                   S/s, 22,050 S/s, and 11,025 S/s. The default is 22,050 S/s.

                     •     number of channels —

             number of channels specifies the number of channels. This input can accept as many
                channels as the sound card supports. For most sound cards 1 is Mono and 2 is Stereo.

                     •       bits per sample —


2152   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2152 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2153 ordinal=2153 -->
## Functions

Functions


         bits per sample specifies the quality of each sample in bits. Common resolutions are 16 bits
       and 8 bits. The default is 16 bits.


   •       error in (no error) —

    error in describes error conditions that occur before this node runs. This input provides
    standard error in functionality.

   •      task ID —

    task ID returns an identification number associated with the configuration on the specified
     device. You can pass task ID to other sound operation VIs.

   •       error out —

    error out contains error information. This output provides standard error out functionality.


Examples

Refer to the following example files included with LabVIEW.

  • labview\examples\Graphics and Sound\Sound\Generate
   Sound.vi
  • labview\examples\Graphics and Sound\Sound\Sound File to
   Sound Output.vi
  • labview\examples\Graphics and Sound\Sound\Simultaneous
   Sound Input Output.vi
SoundSound OutputOutput StartStart

Starts playback from the device. This VI is necessary only if the Sound Output Stop VI
has previously been called.

(Windows) You must have DirectX 8.0 or later to use this VI. (Linux) You must have the
Open Sound System (OSS) driver to use this VI.


                                                    © National Instruments 2153

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2153 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2154 ordinal=2154 -->
## Functions

Functions


      Inputs/Outputs

               •      task ID —

            task ID is the sound operation from the configured device you want to manipulate or input.

           You generate task ID with the Sound Output Configure VI.

               •       error in (no error) —

             error in describes error conditions that occur before this node runs. This input provides
            standard error in functionality.

               •      task ID out —

            task ID out is the manipulated sound operation originally passed to the task ID parameter.

               •       error out —

             error out contains error information. This output provides standard error out functionality.

   SoundSound OutputOutput WriteWrite

       Writes data to a sound output device. You must use the Sound Output Configure VI to
       configure the device if you are writing continuously. You must manually select the
      polymorphic instance you want to use.

      (Windows) You must have DirectX 8.0 or later to use this VI. (Linux) You must have the
     Open Sound System (OSS) driver to use this VI.

           Note If the buffer you set using the number of samples/ch input of the
            Sound File Read VI is full when the application executes, LabVIEW
               automatically implements a wait on the Sound Output Write VI even if you
                set timeout to 0. This may cause the data flow to hang and return
             unexpected results.

2154   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2154 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2155 ordinal=2155 -->
## Functions

Functions


  • Sound Output Write (DBL) VI
  • Sound Output Write (DBL Single) VI
  • Sound Output Write (SGL) VI
  • Sound Output Write (U8) VI
  • Sound Output Write (I16) VI
  • Sound Output Write (I32) VI

Examples

Refer to the following example files included with LabVIEW.

  • labview\examples\Graphics and Sound\Sound\Sound File to
   Sound Output.vi
  • labview\examples\Graphics and Sound\Sound\Generate
   Sound.vi
  • labview\examples\Graphics and Sound\Sound\Simultaneous
   Sound Input Output.vi
SoundSound OutputOutput WriteWrite (DBL)(DBL) VIVI

Writes data to a sound output device. You must use the Sound Output Configure VI to
configure the device if you are writing continuously. You must manually select the
polymorphic instance you want to use.

(Windows) You must have DirectX 8.0 or later to use this VI. (Linux) You must have the
Open Sound System (OSS) driver to use this VI.

      Note If the buffer you set using the number of samples/ch input of the
      Sound File Read VI is full when the application executes, LabVIEW
        automatically implements a wait on the Sound Output Write VI even if you
        set timeout to 0. This may cause the data flow to hang and return
       unexpected results.


                                                    © National Instruments 2155

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2155 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2156 ordinal=2156 -->
## Functions

Functions


      Inputs/Outputs

               •      task ID —

            task ID is the sound operation from the configured device you want to manipulate or input.

           You generate task ID with the Sound Output Configure VI.

               •      data —

           data writes any sound data to the internal buffers. For multi-channel sound data, data is an
             array of waveforms where each element of the array is a single channel.

          The specified data type determines the range of values for the sound data.

               •       error in (no error) —

             error in describes error conditions that occur before this node runs. This input provides
            standard error in functionality.

               •      timeout (sec) —

           timeout (sec) specifies the time, in seconds, that the function waits for the sound operation to
            complete.

             This VI returns an error if the time elapses. The default is 10. If you set timeout (sec) to -1, the VI
            waits indefinitely. If you set timeout (sec) to 0, the VI returns immediately while the sound
            continues to play. You can use the Sound Output Wait VI to wait for playback to complete.

               •      task ID out —

            task ID out is the manipulated sound operation originally passed to the task ID parameter.

               •       error out —

             error out contains error information. This output provides standard error out functionality.


2156   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2156 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2157 ordinal=2157 -->
## Functions

Functions

Examples

Refer to the following example files included with LabVIEW.

  • labview\examples\Graphics and Sound\Sound\Sound File to
   Sound Output.vi
  • labview\examples\Graphics and Sound\Sound\Generate
   Sound.vi
  • labview\examples\Graphics and Sound\Sound\Simultaneous
   Sound Input Output.vi
SoundSound OutputOutput WriteWrite (DBL(DBL Single)Single) VIVI

Writes data to a sound output device. You must use the Sound Output Configure VI to
configure the device if you are writing continuously. You must manually select the
polymorphic instance you want to use.

      Note The WFM instance of this VI writes data from a single waveform that
       uses double-precision floating point numbers for the sound data.


Inputs/Outputs

   •      task ID —

    task ID is the sound operation from the configured device you want to manipulate or input.

    You generate task ID with the Sound Output Configure VI.

   •      data —

    data writes any sound data to the internal buffers.


                                                    © National Instruments 2157

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2157 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2158 ordinal=2158 -->
## Functions

Functions


          The specified data type determines the range of values for the sound data.

               •       error in (no error) —

             error in describes error conditions that occur before this node runs. This input provides
            standard error in functionality.

               •      timeout (sec) —

           timeout (sec) specifies the time, in seconds, that the function waits for the sound operation to
            complete.

             This VI returns an error if the time elapses. The default is 10. If you set timeout (sec) to -1, the VI
            waits indefinitely. If you set timeout (sec) to 0, the VI returns immediately while the sound
            continues to play. You can use the Sound Output Wait VI to wait for playback to complete.

               •      task ID out —

            task ID out is the manipulated sound operation originally passed to the task ID parameter.

               •       error out —

             error out contains error information. This output provides standard error out functionality.


     Examples

       Refer to the following example files included with LabVIEW.

            • labview\examples\Graphics and Sound\Sound\Sound File to
        Sound Output.vi
            • labview\examples\Graphics and Sound\Sound\Generate
        Sound.vi
            • labview\examples\Graphics and Sound\Sound\Simultaneous
        Sound Input Output.vi
   SoundSound OutputOutput WriteWrite (SGL)(SGL) VIVI

       Writes data to a sound output device. You must use the Sound Output Configure VI to
       configure the device if you are writing continuously. You must manually select the

2158   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2158 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2159 ordinal=2159 -->
## Functions

Functions

polymorphic instance you want to use.

      Note Use the SGL instance to write data from a waveform that uses single-
        precision floating point numbers for the sound data.


Inputs/Outputs

   •      task ID —

    task ID is the sound operation from the configured device you want to manipulate or input.

    You generate task ID with the Sound Output Configure VI.

   •      data —

    data writes any sound data to the internal buffers. For multi-channel sound data, data is an
    array of waveforms where each element of the array is a single channel.

    The specified data type determines the range of values for the sound data.

   •       error in (no error) —

    error in describes error conditions that occur before this node runs. This input provides
    standard error in functionality.

   •      timeout (sec) —

    timeout (sec) specifies the time, in seconds, that the function waits for the sound operation to
    complete.

    This VI returns an error if the time elapses. The default is 10. If you set timeout (sec) to -1, the VI
    waits indefinitely. If you set timeout (sec) to 0, the VI returns immediately while the sound
    continues to play. You can use the Sound Output Wait VI to wait for playback to complete.

   •      task ID out —

    task ID out is the manipulated sound operation originally passed to the task ID parameter.


                                                    © National Instruments 2159

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2159 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2160 ordinal=2160 -->
## Functions

Functions

               •       error out —

             error out contains error information. This output provides standard error out functionality.


     Examples

       Refer to the following example files included with LabVIEW.

            • labview\examples\Graphics and Sound\Sound\Sound File to
        Sound Output.vi
            • labview\examples\Graphics and Sound\Sound\Generate
        Sound.vi
            • labview\examples\Graphics and Sound\Sound\Simultaneous
        Sound Input Output.vi
   SoundSound OutputOutput WriteWrite (U8)(U8) VIVI

       Writes data to a sound output device. You must use the Sound Output Configure VI to
       configure the device if you are writing continuously. You must manually select the
      polymorphic instance you want to use.

      (Windows) You must have DirectX 8.0 or later to use this VI. (Linux) You must have the
     Open Sound System (OSS) driver to use this VI.

           Note If the buffer you set using the number of samples/ch input of the
            Sound File Read VI is full when the application executes, LabVIEW
               automatically implements a wait on the Sound Output Write VI even if you
                set timeout to 0. This may cause the data flow to hang and return
             unexpected results.


2160   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2160 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2161 ordinal=2161 -->
## Functions

Functions

Inputs/Outputs

   •      task ID —

    task ID is the sound operation from the configured device you want to manipulate or input.

    You generate task ID with the Sound Output Configure VI.

   •      data —

    data writes any sound data to the internal buffers. For multi-channel sound data, data is an
    array of waveforms where each element of the array is a single channel.

    The specified data type determines the range of values for the sound data.

   •       error in (no error) —

    error in describes error conditions that occur before this node runs. This input provides
    standard error in functionality.

   •      timeout (sec) —

    timeout (sec) specifies the time, in seconds, that the function waits for the sound operation to
    complete.

    This VI returns an error if the time elapses. The default is 10. If you set timeout (sec) to -1, the VI
    waits indefinitely. If you set timeout (sec) to 0, the VI returns immediately while the sound
    continues to play. You can use the Sound Output Wait VI to wait for playback to complete.

   •      task ID out —

    task ID out is the manipulated sound operation originally passed to the task ID parameter.

   •       error out —

    error out contains error information. This output provides standard error out functionality.


Examples

Refer to the following example files included with LabVIEW.

  • labview\examples\Graphics and Sound\Sound\Sound File to
   Sound Output.vi

                                                    © National Instruments 2161

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2161 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2162 ordinal=2162 -->
## Functions

Functions

            • labview\examples\Graphics and Sound\Sound\Generate
        Sound.vi
            • labview\examples\Graphics and Sound\Sound\Simultaneous
        Sound Input Output.vi
   SoundSound OutputOutput WriteWrite (I16)(I16) VIVI

       Writes data to a sound output device. You must use the Sound Output Configure VI to
       configure the device if you are writing continuously. You must manually select the
      polymorphic instance you want to use.

      (Windows) You must have DirectX 8.0 or later to use this VI. (Linux) You must have the
     Open Sound System (OSS) driver to use this VI.

           Note If the buffer you set using the number of samples/ch input of the
            Sound File Read VI is full when the application executes, LabVIEW
               automatically implements a wait on the Sound Output Write VI even if you
                set timeout to 0. This may cause the data flow to hang and return
             unexpected results.


      Inputs/Outputs

               •      task ID —

            task ID is the sound operation from the configured device you want to manipulate or input.

           You generate task ID with the Sound Output Configure VI.

               •      data —

           data writes any sound data to the internal buffers. For multi-channel sound data, data is an
             array of waveforms where each element of the array is a single channel.


2162   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2162 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2163 ordinal=2163 -->
## Functions

Functions


    The specified data type determines the range of values for the sound data.

   •       error in (no error) —

    error in describes error conditions that occur before this node runs. This input provides
    standard error in functionality.

   •      timeout (sec) —

    timeout (sec) specifies the time, in seconds, that the function waits for the sound operation to
    complete.

    This VI returns an error if the time elapses. The default is 10. If you set timeout (sec) to -1, the VI
    waits indefinitely. If you set timeout (sec) to 0, the VI returns immediately while the sound
    continues to play. You can use the Sound Output Wait VI to wait for playback to complete.

   •      task ID out —

    task ID out is the manipulated sound operation originally passed to the task ID parameter.

   •       error out —

    error out contains error information. This output provides standard error out functionality.


Examples

Refer to the following example files included with LabVIEW.

  • labview\examples\Graphics and Sound\Sound\Sound File to
   Sound Output.vi
  • labview\examples\Graphics and Sound\Sound\Generate
   Sound.vi
  • labview\examples\Graphics and Sound\Sound\Simultaneous
   Sound Input Output.vi
SoundSound OutputOutput WriteWrite (I32)(I32) VIVI

Writes data to a sound output device. You must use the Sound Output Configure VI to
configure the device if you are writing continuously. You must manually select the

                                                    © National Instruments 2163

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2163 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2164 ordinal=2164 -->
## Functions

Functions

      polymorphic instance you want to use.

      (Windows) You must have DirectX 8.0 or later to use this VI. (Linux) You must have the
     Open Sound System (OSS) driver to use this VI.

           Note If the buffer you set using the number of samples/ch input of the
            Sound File Read VI is full when the application executes, LabVIEW
               automatically implements a wait on the Sound Output Write VI even if you
                set timeout to 0. This may cause the data flow to hang and return
             unexpected results.


      Inputs/Outputs

               •      task ID —

            task ID is the sound operation from the configured device you want to manipulate or input.

           You generate task ID with the Sound Output Configure VI.

               •      data —

           data writes any sound data to the internal buffers. For multi-channel sound data, data is an
             array of waveforms where each element of the array is a single channel.

          The specified data type determines the range of values for the sound data.

               •       error in (no error) —

             error in describes error conditions that occur before this node runs. This input provides
            standard error in functionality.

               •      timeout (sec) —

           timeout (sec) specifies the time, in seconds, that the function waits for the sound operation to
            complete.


2164   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2164 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2165 ordinal=2165 -->
## Functions

Functions


    This VI returns an error if the time elapses. The default is 10. If you set timeout (sec) to -1, the VI
    waits indefinitely. If you set timeout (sec) to 0, the VI returns immediately while the sound
    continues to play. You can use the Sound Output Wait VI to wait for playback to complete.

   •      task ID out —

    task ID out is the manipulated sound operation originally passed to the task ID parameter.

   •       error out —

    error out contains error information. This output provides standard error out functionality.


Examples

Refer to the following example files included with LabVIEW.

  • labview\examples\Graphics and Sound\Sound\Sound File to
   Sound Output.vi
  • labview\examples\Graphics and Sound\Sound\Generate
   Sound.vi
  • labview\examples\Graphics and Sound\Sound\Simultaneous
   Sound Input Output.vi
SoundSound OutputOutput StopStop

Stops the device from playing sound from the buffer. Use the Sound Output Clear VI to
clear the data in the buffer. Use the Sound Output Start VI to restart output.

(Windows) You must have DirectX 8.0 or later to use this VI. (Linux) You must have the
Open Sound System (OSS) driver to use this VI.


Inputs/Outputs

   •      task ID —

                                                    © National Instruments 2165

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2165 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2166 ordinal=2166 -->
## Functions

Functions


            task ID is the sound operation from the configured device you want to manipulate or input.

           You generate task ID with the Sound Output Configure VI.

               •       error in (no error) —

             error in describes error conditions that occur before this node runs. This input provides
            standard error in functionality.

               •      task ID out —

            task ID out is the manipulated sound operation originally passed to the task ID parameter.

               •       error out —

             error out contains error information. This output provides standard error out functionality.

   SoundSound OutputOutput ClearClear

       Stops the device from playing sound, clears the buffer, returns the task to the default
        state, and clears the resources associated with the task. The task becomes invalid.

      (Windows) You must have DirectX 8.0 or later to use this VI. (Linux) You must have the
     Open Sound System (OSS) driver to use this VI.


      Inputs/Outputs

               •      task ID —

            task ID is the sound operation from the configured device you want to manipulate or input.

           You generate task ID with the Sound Output Configure VI.

               •       error in (no error) —


2166   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2166 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2167 ordinal=2167 -->
## Functions

Functions


    error in describes error conditions that occur before this node runs. This input provides
    standard error in functionality.

   •       error out —

    error out contains error information. This output provides standard error out functionality.


Examples

Refer to the following example files included with LabVIEW.

  • labview\examples\Graphics and Sound\Sound\Sound Player.vi
  • labview\examples\Graphics and Sound\Sound\Generate
   Sound.vi
  • labview\examples\Graphics and Sound\Sound\Simultaneous
   Sound Input Output.vi
SoundSound OutputOutput WaitWait

Waits until all of the sound is played by the output device.

(Windows) You must have DirectX 8.0 or later to use this VI. (Linux) You must have the
Open Sound System (OSS) driver to use this VI.


Inputs/Outputs

   •      task ID —

    task ID is the sound operation from the configured device you want to manipulate or input.

    You generate task ID with the Sound Output Configure VI.

   •       error in (no error) —

                                                    © National Instruments 2167

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2167 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2168 ordinal=2168 -->
## Functions

Functions


             error in describes error conditions that occur before this node runs. This input provides
            standard error in functionality.

               •      timeout (sec) —

           timeout (sec) specifies the time, in seconds, that the VI waits for the sound operation to
            complete.

             This VI returns an error if the time elapses. The default is 10. If you set timeout (sec) to -1, the VI
            waits indefinitely.

               •      task ID out —

            task ID out is the manipulated sound operation originally passed to the task ID parameter.

               •       error out —

             error out contains error information. This output provides standard error out functionality.


     Examples

       Refer to the following example files included with LabVIEW.

            • labview\examples\Graphics and Sound\Sound\Sound File to
        Sound Output.vi
   SoundSound OutputOutput InfoInfo

       Returns information about the current state of a sound output task.

      (Windows) You must have DirectX 8.0 or later to use this VI. (Linux) You must have the
     Open Sound System (OSS) driver to use this VI.


2168   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2168 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2169 ordinal=2169 -->
## Functions

Functions

Inputs/Outputs

   •      task ID —

    task ID is the sound operation from the configured device you want to manipulate or input.

    You generate task ID with the Sound Output Configure VI.

   •       error in (no error) —

    error in describes error conditions that occur before this node runs. This input provides
    standard error in functionality.

   •      task ID out —

    task ID out is the manipulated sound operation originally passed to the task ID parameter.

   •        is playing? —

      is playing? indicates if the sound output task is playing.

   •     volume —

    volume returns the volume of the sound operation, one value per channel. 0 is silent and 100 is
    the loudest volume.

   •       error out —

    error out contains error information. This output provides standard error out functionality.


Examples

Refer to the following example files included with LabVIEW.

  • labview\examples\Graphics and Sound\Sound\Sound Player.vi
SoundSound OutputOutput SetSet VolumeVolume

Sets the volume at which the sound output device plays.

(Windows) You must have DirectX 8.0 or later to use this VI. (Linux) You must have the

                                                    © National Instruments 2169

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2169 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2170 ordinal=2170 -->
## Functions

Functions

     Open Sound System (OSS) driver to use this VI.

           Note Some Linux distributions use a version of the OSS sound driver that
             does not support setting volume through the DSP device file. LabVIEW
             cannot set the output volume on these distributions and returns a warning.


            • Sound Output Set Volume (Single) VI
            • Sound Output Set Volume (Array) VI

     Examples

       Refer to the following example files included with LabVIEW.

            • labview\examples\Graphics and Sound\Sound\Sound File to
        Sound Output.vi
            • labview\examples\Graphics and Sound\Sound\Generate
        Sound.vi
   SoundSound OutputOutput SetSet VolumeVolume (Single)(Single) VIVI

       Sets the volume at which the sound output device plays.

      (Windows) You must have DirectX 8.0 or later to use this VI. (Linux) You must have the
     Open Sound System (OSS) driver to use this VI.

           Note Some Linux distributions use a version of the OSS sound driver that
             does not support setting volume through the DSP device file. LabVIEW
             cannot set the output volume on these distributions and returns a warning.


2170   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2170 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2171 ordinal=2171 -->
## Functions

Functions


Inputs/Outputs

   •      task ID —

    task ID is the sound operation from the configured device you want to manipulate or input.

    You generate task ID with the Sound Output Configure VI.

   •     volume —

    volume specifies the volume of the sound operation. 0 is silent and 100 is the loudest volume.
    The default is 100.

   •       error in (no error) —

    error in describes error conditions that occur before this node runs. This input provides
    standard error in functionality.

   •      task ID out —

    task ID out is the manipulated sound operation originally passed to the task ID parameter.

   •       error out —

    error out contains error information. This output provides standard error out functionality.


Examples

Refer to the following example files included with LabVIEW.

  • labview\examples\Graphics and Sound\Sound\Sound File to
   Sound Output.vi
  • labview\examples\Graphics and Sound\Sound\Generate
   Sound.vi


                                                    © National Instruments 2171

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2171 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2172 ordinal=2172 -->
## Functions

Functions

   SoundSound OutputOutput SetSet VolumeVolume (Array)(Array) VIVI

       Sets the volume at which the sound output device plays.

      (Windows) You must have DirectX 8.0 or later to use this VI. (Linux) You must have the
     Open Sound System (OSS) driver to use this VI.

           Note Some Linux distributions use a version of the OSS sound driver that
             does not support setting volume through the DSP device file. LabVIEW
             cannot set the output volume on these distributions and returns a warning.


      Inputs/Outputs

               •      task ID —

            task ID is the sound operation from the configured device you want to manipulate or input.

           You generate task ID with the Sound Output Configure VI.

               •     volume —

          volume specifies the volume of the sound operation, one element per channel. 0 is silent and
           100 is the loudest volume. The default is 100.

               •       error in (no error) —

             error in describes error conditions that occur before this node runs. This input provides
            standard error in functionality.

               •      task ID out —

            task ID out is the manipulated sound operation originally passed to the task ID parameter.

               •       error out —


2172   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2172 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2173 ordinal=2173 -->
## Functions

Functions


    error out contains error information. This output provides standard error out functionality.


Examples

Refer to the following example files included with LabVIEW.

  • labview\examples\Graphics and Sound\Sound\Sound File to
   Sound Output.vi
  • labview\examples\Graphics and Sound\Sound\Generate
   Sound.vi
PlayPlay SoundSound FileFile

Opens a file and starts playing it immediately.

(Windows) You must have DirectX 8.0 or later to use this VI. (Linux) You must have the
Open Sound System (OSS) driver to use this VI.


Inputs/Outputs

   •      device ID —

    device ID is the input or output device you access for a sound operation. In general, most users
    should select the default value of 0.

    The value ranges from 0 to n–1, where nis the number of input or output devices on the
    computer.

   •      path —

    path specifies the absolute path to the file from which you want to play sound data.


                                                    © National Instruments 2173

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2173 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2174 ordinal=2174 -->
## Functions

Functions


                    If the path is empty or invalid, the VI returns an error. The default is <Not A Path>.

               •       error in (no error) —

             error in describes error conditions that occur before this node runs. This input provides
            standard error in functionality.

               •      timeout (sec) —

           timeout (sec)specifies the time, in seconds, that the VI waits for the sound operation to
            complete.

          The default is 0. This VI returns an error if the time elapses, unless timeout (sec) is 0. If you set
           timeout (sec) to 0, this VI returns immediately while the sound continues to play. You can use
            the Sound Output Wait VI to wait for playback to complete. If you set timeout (sec) to -1, this VI
            waits until the sound finishes playing.

               •      task ID —

            task ID returns an identification number associated with the configuration on the specified
             device. You can pass task ID to other sound operation VIs.

               •       error out —

             error out contains error information. This output provides standard error out functionality.


     Examples

       Refer to the following example files included with LabVIEW.

            • labview\examples\Graphics and Sound\Sound\Sound Player.vi

      InputInput

      Use the Sound Input VIs to configure and control a sound input device.

      (Windows) You must have DirectX 8.0 or later to use the Sound Input VIs.

       (Linux) You must have the Open Sound System (OSS) driver to use this VI. LabVIEW
       searches for input and output devices by looking for files named /dev/dsp or /dev/


2174   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2174 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2175 ordinal=2175 -->
## Functions

Functions

dspX, where X is an integer between 0 and 16. LabVIEW attempts to open each input
and output device. If LabVIEW cannot detect the sound card, check that a device file
named /dev/dsp or /dev/dspX exists on the local system and that you have
permission to read from and write to the device. If you moved this device to a location
other than the default, LabVIEW can work with a symbolic link.


 Palette           Description Object

 Acquire    Acquires data from a sound device. This Express VI automatically configures an input
 Sound     task, acquires the data, and clears the task after the acquisition completes.


 Sound           Configures a sound input device to acquire data and send the data to the buffer. Use the
 Input         Sound Input Read VI to read the data. Configure

 Sound             Starts data acquisition from the device. This VI is necessary only if Sound Input Stop has
 Input            previously been called. Start


 Sound    Reads data from a sound input device. You must use the Sound Input Configure VI to
 Input      configure the device. You must manually select the polymorphic instance you want to
 Read      use.


 Sound    Stops data acquisition from the device. Use the Sound Input Clear VI to clear the data in
 Input      the buffer. Use the Sound Input Start VI to restart the acquisition after calling the Sound
 Stop      Input Stop VI.


 Sound
           Stops acquisition of data, clears the buffer, returns the task to the default state, and
 Input
             clears the resources associated with the task. The task becomes invalid.
 Clear


                                                    © National Instruments 2175

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2175 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2176 ordinal=2176 -->
## Functions

Functions

    AcquireAcquire SoundSound

       Acquires data from a sound device. This Express VI automatically configures an input
        task, acquires the data, and clears the task after the acquisition completes.

      (Windows) You must have DirectX 8.0 or later to use this VI. (Linux) You must have the
     Open Sound System (OSS) driver to use this VI.


      Dialog Box Options

        Option              Description

        Device                 Lists the sound devices you have connected.


        #Channels           Specifies the number of channels. 1 is Mono, and 2 is Stereo.


        Resolution (bits)     Specifies the quality of each sample in bits. The default is 16 bits.


        Duration (s)         Sets the number of seconds for which you want to acquire sound.


       Sample rate (Hz)     Specifies the sample rate in hertz.


        Preview             Displays a preview of the sound operation in the graph.


2176   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2176 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2177 ordinal=2177 -->
## Functions

Functions


 Option              Description

 Graph Preview       Displays a preview of the sound operation.


Inputs/Outputs

   •      Device —

     Lists the sound devices you have connected.

   •     Sample rate (Hz) —

     Specifies the sample rate in hertz.

   •      Resolution (bits) —

     Specifies the quality of each sample in bits. The default is 16 bits.

   •       error in (no error) —

    Describes error conditions that occur before this node runs.

   •      Duration (s) —

    Sets the number of seconds for which you want to acquire sound.

   •      #Channels —

     Specifies the number of channels. 1 is Mono, and 2 is Stereo.

   •      Data —

    Returns the data this Express VI acquires from the selected device using the settings you specify
     in the configuration dialog box.

    You can convert this output to a waveform or one-dimensional array of waveforms (one per
    channel) by using the Convert from Dynamic Data function.

   •       error out —

    Contains error information. This output provides standard error out functionality.


                                                    © National Instruments 2177

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2177 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2178 ordinal=2178 -->
## Functions

Functions

     Components

       Specifies the quality of each sample in bits. The default is 16 bits.

        Lists the sound devices you have connected.

       Sets the number of seconds for which you want to acquire sound.

       Specifies the number of channels. 1 is Mono, and 2 is Stereo.

       Displays a preview of the sound operation in the graph.

       Specifies the sample rate in hertz.

       Displays a preview of the sound operation.
   SoundSound InputInput ConfigureConfigure

       Configures a sound input device to acquire data and send the data to the buffer. Use
       the Sound Input Read VI to read the data.

      (Windows) You must have DirectX 8.0 or later to use this VI. (Linux) You must have the
     Open Sound System (OSS) driver to use this VI.


      Inputs/Outputs

               •     number of samples/ch —

          number of samples/ch specifies the number of samples per channel in the buffer.

           Use a large number of samples for continuous operations. Use a smaller number of samples if
           you want to use less memory.

               •     sample mode —

2178   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2178 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2179 ordinal=2179 -->
## Functions

Functions


  sample mode specifies whether the VI acquires samples just once (Finite Samples) or
  continuously (Continuous Samples).

  In Finite Samples mode, call Sound Input Read only until you have written the number of
  samples specified in number of samples/ch. In Continuous Samples mode, you can call Sound
  Input Read repeatedly as needed.

•      device ID —

  device ID is the input or output device you access for a sound operation. In general, most users
  should select the default value of 0.

  The value ranges from 0 to n–1, where nis the number of input or output devices on the
  computer.

•     sound format —

  sound format sets the acquisition rate, the number of channels, and the bits per sample of the
  sound operation. The values for each of these controls is dependent on your sound card.

        Note Setting sample rate (S/s) and bits per sample high uses more of the computer
        memory when the VI runs. Also, not all operating systems and sound cards support
               all sound format options.

      •     sample rate (S/s) —

      sample rate (S/s) sets the sampling rate for the sound operation. Common rates are 44,100
       S/s, 22,050 S/s, and 11,025 S/s. The default is 22,050 S/s.

      •     number of channels —

     number of channels specifies the number of channels. This input can accept as many
      channels as the sound card supports. For most sound cards 1 is Mono and 2 is Stereo.

      •       bits per sample —

       bits per sample specifies the quality of each sample in bits. Common resolutions are 16 bits
     and 8 bits. The default is 16 bits.


•       error in (no error) —


                                                   © National Instruments 2179

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2179 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2180 ordinal=2180 -->
## Functions

Functions


             error in describes error conditions that occur before this node runs. This input provides
            standard error in functionality.

               •      task ID —

            task ID returns an identification number associated with the configuration on the specified
             device. You can pass task ID to other sound operation VIs.

               •       error out —

             error out contains error information. This output provides standard error out functionality.


     Examples

       Refer to the following example files included with LabVIEW.

            • labview\examples\Graphics and Sound\Sound\Continuous
        Sound Input.vi
            • labview\examples\Graphics and Sound\Sound\Finite Sound
        Input.vi
            • labview\examples\Graphics and Sound\Sound\Simultaneous
        Sound Input Output.vi
   SoundSound InputInput StartStart

        Starts data acquisition from the device. This VI is necessary only if Sound Input Stop
      has previously been called.

      (Windows) You must have DirectX 8.0 or later to use this VI. (Linux) You must have the
     Open Sound System (OSS) driver to use this VI.


      Inputs/Outputs

               •      task ID —

2180   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2180 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2181 ordinal=2181 -->
## Functions

Functions


    task ID is the sound operation from the configured device you want to manipulate or input.

    You generate task ID with the Sound Input Configure VI.

   •       error in (no error) —

    error in describes error conditions that occur before this node runs. This input provides
    standard error in functionality.

   •      task ID out —

    task ID out is the manipulated sound operation originally passed to the task ID parameter.

   •       error out —

    error out contains error information. This output provides standard error out functionality.

SoundSound InputInput ReadRead

Reads data from a sound input device. You must use the Sound Input Configure VI to
configure the device. You must manually select the polymorphic instance you want to
use.

(Windows) You must have DirectX 8.0 or later to use this VI. (Linux) You must have the
Open Sound System (OSS) driver to use this VI.


  • Sound Input Read (DBL) VI
  • Sound Input Read (SGL) VI
  • Sound Input Read (U8) VI
  • Sound Input Read (I16) VI
  • Sound Input Read (I32) VI

Examples

Refer to the following example files included with LabVIEW.

                                                    © National Instruments 2181

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2181 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2182 ordinal=2182 -->
## Functions

Functions

            • labview\examples\Graphics and Sound\Sound\Continuous
        Sound Input.vi
            • labview\examples\Graphics and Sound\Sound\Finite Sound
        Input.vi
            • labview\examples\Graphics and Sound\Sound\Simultaneous
        Sound Input Output.vi
   SoundSound InputInput ReadRead (DBL)(DBL) VIVI

      Reads data from a sound input device. You must use the Sound Input Configure VI to
       configure the device. You must manually select the polymorphic instance you want to
       use.

      (Windows) You must have DirectX 8.0 or later to use this VI. (Linux) You must have the
     Open Sound System (OSS) driver to use this VI.


      Inputs/Outputs

               •     number of samples/ch —

          number of samples/ch specifies the number of samples per channel to read from the buffer.

               •      task ID —

            task ID is the sound operation from the configured device you want to manipulate or input.

           You generate task ID with the Sound Input Configure VI.

               •       error in (no error) —

             error in describes error conditions that occur before this node runs. This input provides
            standard error in functionality.

               •      timeout (sec) —


2182   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2182 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2183 ordinal=2183 -->
## Functions

Functions


    timeout (sec) specifies the time, in seconds, that the VI waits for the sound operation to
    complete.

    This VI returns an error if the time elapses. The default is 10. If you set timeout (sec) to -1, the VI
    waits indefinitely.

   •      task ID out —

    task ID out is the manipulated sound operation originally passed to the task ID parameter.

   •      data —

    data reads any sound data from the internal buffers. For multi-channel sound data, data is an
    array of waveforms where each element of the array is a single channel.

    The specified data type determines the range of values for the sound data.

   •       error out —

    error out contains error information. This output provides standard error out functionality.


Examples

Refer to the following example files included with LabVIEW.

  • labview\examples\Graphics and Sound\Sound\Continuous
   Sound Input.vi
  • labview\examples\Graphics and Sound\Sound\Finite Sound
   Input.vi
  • labview\examples\Graphics and Sound\Sound\Simultaneous
   Sound Input Output.vi
SoundSound InputInput ReadRead (SGL)(SGL) VIVI

Reads data from a sound input device. You must use the Sound Input Configure VI to
configure the device. You must manually select the polymorphic instance you want to
use.


                                                    © National Instruments 2183

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2183 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2184 ordinal=2184 -->
## Functions

Functions

      (Windows) You must have DirectX 8.0 or later to use this VI. (Linux) You must have the
     Open Sound System (OSS) driver to use this VI.


      Inputs/Outputs

               •     number of samples/ch —

          number of samples/ch specifies the number of samples per channel to read from the buffer.

               •      task ID —

            task ID is the sound operation from the configured device you want to manipulate or input.

           You generate task ID with the Sound Input Configure VI.

               •       error in (no error) —

             error in describes error conditions that occur before this node runs. This input provides
            standard error in functionality.

               •      timeout (sec) —

           timeout (sec) specifies the time, in seconds, that the VI waits for the sound operation to
            complete.

             This VI returns an error if the time elapses. The default is 10. If you set timeout (sec) to -1, the VI
            waits indefinitely.

               •      task ID out —

            task ID out is the manipulated sound operation originally passed to the task ID parameter.

               •      data —

           data reads any sound data from the internal buffers. For multi-channel sound data, data is an
             array of waveforms where each element of the array is a single channel.

          The specified data type determines the range of values for the sound data.


2184   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2184 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2185 ordinal=2185 -->
## Functions

Functions

   •       error out —

    error out contains error information. This output provides standard error out functionality.


Examples

Refer to the following example files included with LabVIEW.

  • labview\examples\Graphics and Sound\Sound\Continuous
   Sound Input.vi
  • labview\examples\Graphics and Sound\Sound\Finite Sound
   Input.vi
  • labview\examples\Graphics and Sound\Sound\Simultaneous
   Sound Input Output.vi
SoundSound InputInput ReadRead (U8)(U8) VIVI

Reads data from a sound input device. You must use the Sound Input Configure VI to
configure the device. You must manually select the polymorphic instance you want to
use.

(Windows) You must have DirectX 8.0 or later to use this VI. (Linux) You must have the
Open Sound System (OSS) driver to use this VI.


Inputs/Outputs

   •     number of samples/ch —

   number of samples/ch specifies the number of samples per channel to read from the buffer.

   •      task ID —


                                                    © National Instruments 2185

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2185 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2186 ordinal=2186 -->
## Functions

Functions


            task ID is the sound operation from the configured device you want to manipulate or input.

           You generate task ID with the Sound Input Configure VI.

               •       error in (no error) —

             error in describes error conditions that occur before this node runs. This input provides
            standard error in functionality.

               •      timeout (sec) —

           timeout (sec) specifies the time, in seconds, that the VI waits for the sound operation to
            complete.

             This VI returns an error if the time elapses. The default is 10. If you set timeout (sec) to -1, the VI
            waits indefinitely.

               •      task ID out —

            task ID out is the manipulated sound operation originally passed to the task ID parameter.

               •      data —

           data reads any sound data from the internal buffers. For multi-channel sound data, data is an
             array of waveforms where each element of the array is a single channel.

          The specified data type determines the range of values for the sound data.

               •       error out —

             error out contains error information. This output provides standard error out functionality.


     Examples

       Refer to the following example files included with LabVIEW.

            • labview\examples\Graphics and Sound\Sound\Continuous
        Sound Input.vi
            • labview\examples\Graphics and Sound\Sound\Finite Sound
        Input.vi
            • labview\examples\Graphics and Sound\Sound\Simultaneous


2186   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2186 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2187 ordinal=2187 -->
## Functions

Functions

   Sound Input Output.vi
SoundSound InputInput ReadRead (I16)(I16) VIVI

Reads data from a sound input device. You must use the Sound Input Configure VI to
configure the device. You must manually select the polymorphic instance you want to
use.

(Windows) You must have DirectX 8.0 or later to use this VI. (Linux) You must have the
Open Sound System (OSS) driver to use this VI.


Inputs/Outputs

   •     number of samples/ch —

   number of samples/ch specifies the number of samples per channel to read from the buffer.

   •      task ID —

    task ID is the sound operation from the configured device you want to manipulate or input.

    You generate task ID with the Sound Input Configure VI.

   •       error in (no error) —

    error in describes error conditions that occur before this node runs. This input provides
    standard error in functionality.

   •      timeout (sec) —

    timeout (sec) specifies the time, in seconds, that the VI waits for the sound operation to
    complete.

    This VI returns an error if the time elapses. The default is 10. If you set timeout (sec) to -1, the VI
    waits indefinitely.


                                                    © National Instruments 2187

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2187 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2188 ordinal=2188 -->
## Functions

Functions

               •      task ID out —

            task ID out is the manipulated sound operation originally passed to the task ID parameter.

               •      data —

           data reads any sound data from the internal buffers. For multi-channel sound data, data is an
             array of waveforms where each element of the array is a single channel.

          The specified data type determines the range of values for the sound data.

               •       error out —

             error out contains error information. This output provides standard error out functionality.


     Examples

       Refer to the following example files included with LabVIEW.

            • labview\examples\Graphics and Sound\Sound\Continuous
        Sound Input.vi
            • labview\examples\Graphics and Sound\Sound\Finite Sound
        Input.vi
            • labview\examples\Graphics and Sound\Sound\Simultaneous
        Sound Input Output.vi
   SoundSound InputInput ReadRead (I32)(I32) VIVI

      Reads data from a sound input device. You must use the Sound Input Configure VI to
       configure the device. You must manually select the polymorphic instance you want to
       use.

      (Windows) You must have DirectX 8.0 or later to use this VI. (Linux) You must have the
     Open Sound System (OSS) driver to use this VI.


2188   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2188 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2189 ordinal=2189 -->
## Functions

Functions


Inputs/Outputs

   •     number of samples/ch —

   number of samples/ch specifies the number of samples per channel to read from the buffer.

   •      task ID —

    task ID is the sound operation from the configured device you want to manipulate or input.

    You generate task ID with the Sound Input Configure VI.

   •       error in (no error) —

    error in describes error conditions that occur before this node runs. This input provides
    standard error in functionality.

   •      timeout (sec) —

    timeout (sec) specifies the time, in seconds, that the VI waits for the sound operation to
    complete.

    This VI returns an error if the time elapses. The default is 10. If you set timeout (sec) to -1, the VI
    waits indefinitely.

   •      task ID out —

    task ID out is the manipulated sound operation originally passed to the task ID parameter.

   •      data —

    data reads any sound data from the internal buffers. For multi-channel sound data, data is an
    array of waveforms where each element of the array is a single channel.

    The specified data type determines the range of values for the sound data.

   •       error out —

    error out contains error information. This output provides standard error out functionality.


                                                    © National Instruments 2189

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2189 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2190 ordinal=2190 -->
## Functions

Functions

     Examples

       Refer to the following example files included with LabVIEW.

            • labview\examples\Graphics and Sound\Sound\Continuous
        Sound Input.vi
            • labview\examples\Graphics and Sound\Sound\Finite Sound
        Input.vi
            • labview\examples\Graphics and Sound\Sound\Simultaneous
        Sound Input Output.vi
   SoundSound InputInput StopStop

       Stops data acquisition from the device. Use the Sound Input Clear VI to clear the data
        in the buffer. Use the Sound Input Start VI to restart the acquisition after calling the
      Sound Input Stop VI.

      (Windows) You must have DirectX 8.0 or later to use this VI. (Linux) You must have the
     Open Sound System (OSS) driver to use this VI.


      Inputs/Outputs

               •      task ID —

            task ID is the sound operation from the configured device you want to manipulate or input.

           You generate task ID with the Sound Input Configure VI.

               •       error in (no error) —

             error in describes error conditions that occur before this node runs. This input provides
            standard error in functionality.

               •      task ID out —


2190   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2190 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2191 ordinal=2191 -->
## Functions

Functions


    task ID out is the manipulated sound operation originally passed to the task ID parameter.

   •       error out —

    error out contains error information. This output provides standard error out functionality.

SoundSound InputInput ClearClear

Stops acquisition of data, clears the buffer, returns the task to the default state, and
clears the resources associated with the task. The task becomes invalid.

(Windows) You must have DirectX 8.0 or later to use this VI. (Linux) You must have the
Open Sound System (OSS) driver to use this VI.


Inputs/Outputs

   •      task ID —

    task ID is the sound operation from the configured device you want to manipulate or input.

    You generate task ID with the Sound Input Configure VI.

   •       error in (no error) —

    error in describes error conditions that occur before this node runs. This input provides
    standard error in functionality.

   •       error out —

    error out contains error information. This output provides standard error out functionality.


Examples

Refer to the following example files included with LabVIEW.

                                                    © National Instruments 2191

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2191 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2192 ordinal=2192 -->
## Functions

Functions

            • labview\examples\Graphics and Sound\Sound\Finite Sound
        Input.vi
            • labview\examples\Graphics and Sound\Sound\Continuous
        Sound Input.vi
            • labview\examples\Graphics and Sound\Sound\Simultaneous
        Sound Input Output.vi

       FilesFiles

      Use the Sound Files VIs to create and retrieve PC wave files (.wav).

      (Windows) You must have DirectX 8.0 or later to use the Sound File VIs.

       (Linux) You must have the Open Sound System (OSS) driver to use this VI. LabVIEW
       searches for input and output devices by looking for files named /dev/dsp or /dev/
      dspX, where X is an integer between 0 and 16. LabVIEW attempts to open each input
      and output device. If LabVIEW cannot detect the sound card, check that a device file
     named /dev/dsp or /dev/dspX exists on the local system and that you have
       permission to read from and write to the device. If you moved this device to a location
       other than the default, LabVIEW can work with a symbolic link.


         Palette
                       Description        Object

       Sound File    Reads data from a .wav file into an array of waveforms. This VI automatically
       Read Simple   opens, reads, and closes the .wav file.


       Sound File     Writes data from an array of waveforms to a .wav file. This VI automatically opens,
         Write Simple   writes to, and closes the .wav file.


       Sound File    Opens a .wav file for reading or creates a new .wav file for writing. You must
       Open         manually select the polymorphic instance you want to use.


2192   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2192 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2193 ordinal=2193 -->
## Functions

Functions


 Palette               Description
 Object

 Sound File                Retrieves data about a .wav file. This VI accepts either a path or a refnum. Info


 Sound File    Reads data from a .wav file into an array of waveforms. You must manually select
 Read          the polymorphic instance you want to use.


 Sound File                Writes data from a waveform or an array of waveforms to a .wav file. Write

 Sound File               Closes a .wav file. Close

SoundSound FileFile ReadRead SimpleSimple

Reads data from a .wav file into an array of waveforms. This VI automatically opens,
reads, and closes the .wav file.

(Windows) You must have DirectX 8.0 or later to use this VI.

      Note This VI retrieves only uncompressed wave files.


Inputs/Outputs

   •     number of samples/ch (-1: all) —

   number of samples/ch specifies the number of samples per channel to read from the file. -1
     specifies all samples.


                                                    © National Instruments 2193

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2193 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2194 ordinal=2194 -->
## Functions

Functions

               •      path —

           path specifies the absolute path to the wave file.

                    If the path is empty or invalid, the VI returns an error. The default is <Not A Path>.

               •      position mode —

            position mode, together with position offset, specifies where the read operation begins.

         Absolute starts the operation at the beginning of the file plus position offset, so the offset is
              relative to the beginning of the file. Relative starts the operation at the current location of the
                 file mark plus position offset. The default is Relative.

               •      position offset —

            position offset specifies how far from the location specified by position mode to start reading.

           You express position offset in units of samples. The default is 0.

               •       error in (no error) —

             error in describes error conditions that occur before this node runs. This input provides
            standard error in functionality.

               •      path out —

           path out identifies the wave file passed in path.

               •      data —

           data reads any sound data from the file. For multi-channel sound data, data is an array of
           waveforms where each element of the array is a single channel.

          The specified data type determines the range of values for the sound data.

               •       offset —

             offset indicates the new location of the file mark relative to the beginning of the file, in units of
            samples.

          The default is 0.

               •       error out —


2194   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2194 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2195 ordinal=2195 -->
## Functions

Functions


    error out contains error information. This output provides standard error out functionality.


Examples

Refer to the following example files included with LabVIEW.

  • labview\examples\Graphics and Sound\Sound\Read Sound File
   to Graph.vi
SoundSound FileFile WriteWrite SimpleSimple

Writes data from an array of waveforms to a .wav file. This VI automatically opens,
writes to, and closes the .wav file.

(Windows) You must have DirectX 8.0 or later to use this VI. (Linux) You must have the
Open Sound System (OSS) driver to use this VI.


Inputs/Outputs

   •      path —

    path specifies the absolute path to the wave file.

       If the path is empty or invalid, the VI returns an error. The default is <Not A Path>.

   •      data —

    data writes any sound data to the internal buffers. For multi-channel sound data, data is an
    array of waveforms where each element of the array is a single channel.

    The specified data type determines the range of values for the sound data.

   •       bits per sample —


                                                    © National Instruments 2195

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2195 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2196 ordinal=2196 -->
## Functions

Functions


              bits per sample specifies the quality of each sample in bits. Common resolutions are 16 bits and
           8 bits. The default is 16 bits.

               •       error in (no error) —

             error in describes error conditions that occur before this node runs. This input provides
            standard error in functionality.

               •      path out —

           path out identifies the wave file passed in path.

               •       error out —

             error out contains error information. This output provides standard error out functionality.

   SoundSound FileFile OpenOpen

      Opens a .wav file for reading or creates a new .wav file for writing. You must
      manually select the polymorphic instance you want to use.

      (Windows) You must have DirectX 8.0 or later to use this VI. (Linux) You must have the
     Open Sound System (OSS) driver to use this VI.


            • Sound File Read Open VI
            • Sound File Write Open VI

     Examples

       Refer to the following example files included with LabVIEW.

            • labview\examples\Graphics and Sound\Sound\Sound File to
        Sound Output.vi
            • labview\examples\Graphics and Sound\Sound\Sound Input to


2196   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2196 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2197 ordinal=2197 -->
## Functions

Functions

   File.vi
SoundSound FileFile ReadRead OpenOpen VIVI

Opens a .wav file for reading or creates a new .wav file for writing. You must
manually select the polymorphic instance you want to use.

(Windows) You must have DirectX 8.0 or later to use this VI. (Linux) You must have the
Open Sound System (OSS) driver to use this VI.


Inputs/Outputs

   •      path —

    path specifies the absolute path to the wave file.

       If the path is empty or invalid, the VI returns an error. The default is <Not A Path>.

   •       error in (no error) —

    error in describes error conditions that occur before this node runs. This input provides
    standard error in functionality.

   •     sound file refnum —

    sound file refnum returns a reference to the sound file. You can pass sound file refnum to other
    Sound Files VIs.

   •       error out —

    error out contains error information. This output provides standard error out functionality.


Examples

Refer to the following example files included with LabVIEW.


                                                    © National Instruments 2197

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2197 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2198 ordinal=2198 -->
## Functions

Functions

            • labview\examples\Graphics and Sound\Sound\Sound File to
        Sound Output.vi
            • labview\examples\Graphics and Sound\Sound\Sound Input to
        File.vi
   SoundSound FileFile WriteWrite OpenOpen VIVI

      Opens a .wav file for reading or creates a new .wav file for writing. You must
      manually select the polymorphic instance you want to use.

      (Windows) You must have DirectX 8.0 or later to use this VI. (Linux) You must have the
     Open Sound System (OSS) driver to use this VI.


      Inputs/Outputs

               •      path —

           path specifies the absolute path to the wave file.

                    If the path is empty or invalid, the VI returns an error. The default is <Not A Path>.

               •     sound format —

          sound format sets the sample rate, the number of channels, and the bits per sample for the
          wave file. The values for each of these controls is dependent on your sound card.

                     •     sample rate (S/s) —

              sample rate (S/s) sets the sampling rate for the wave file. Common rates are 44,100 S/s,
                22,050 S/s, and 11,025 S/s. The default is 22050 S/s.

                     •     number of channels —

             number of channels specifies the number of channels. This input can accept as many


2198   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2198 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2199 ordinal=2199 -->
## Functions

Functions


        channels as the sound card supports. For most sound cards 1 is Mono and 2 is Stereo.

         •       bits per sample —

         bits per sample specifies the quality of each sample in bits. Common resolutions are 16 bits
       and 8 bits. The default is 16 bits.


   •       error in (no error) —

    error in describes error conditions that occur before this node runs. This input provides
    standard error in functionality.

   •     sound file refnum —

    sound file refnum returns a reference to the sound file. You can pass sound file refnum to other
    Sound Files VIs.

   •       error out —

    error out contains error information. This output provides standard error out functionality.


Examples

Refer to the following example files included with LabVIEW.

  • labview\examples\Graphics and Sound\Sound\Sound File to
   Sound Output.vi
  • labview\examples\Graphics and Sound\Sound\Sound Input to
   File.vi
SoundSound FileFile InfoInfo

Retrieves data about a .wav file. This VI accepts either a path or a refnum.

(Windows) You must have DirectX 8.0 or later to use this VI. (Linux) You must have the
Open Sound System (OSS) driver to use this VI.


                                                    © National Instruments 2199

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2199 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2200 ordinal=2200 -->
## Functions

Functions


            • Sound File Info (path) VI
            • Sound File Info (refnum) VI

     Examples

       Refer to the following example files included with LabVIEW.

            • labview\examples\Graphics and Sound\Sound\Sound File to
        Sound Output.vi
   SoundSound FileFile InfoInfo (path)(path) VIVI

       Retrieves data about a .wav file. This VI accepts either a path or a refnum.

      (Windows) You must have DirectX 8.0 or later to use this VI. (Linux) You must have the
     Open Sound System (OSS) driver to use this VI.


      Inputs/Outputs

               •      path —

           path specifies the absolute path to the wave file.

                    If the path is empty or invalid, the VI returns an error. The default is <Not A Path>.

               •       error in (no error) —

             error in describes error conditions that occur before this node runs. This input provides
            standard error in functionality.

               •      path out —


2200   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2200 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2201 ordinal=2201 -->
## Functions

Functions


    path out identifies the wave file passed in path.

   •       total number of samples/ch —

     total number of samples/ch returns the total number of samples per channel in the wave file.

   •     sound format —

    sound format returns the sample rate, the number of channels, and the number of bits per
    sample in the wave file.

         •     sample rate (S/s) —

       sample rate (S/s) is the sampling rate for the wave file. Common rates are 44,100 S/s, 22,050
          S/s, and 11,025 S/s.

         •     number of channels —

       number of channels specifies the number of channels in the wave file. This input can
        accept as many channels as the sound card supports. For most sound cards 1 is Mono and 2
           is Stereo.

         •       bits per sample —

         bits per sample is the quality of each sample in bits. Common resolutions are 16 bits and 8
           bits.


   •       error out —

    error out contains error information. This output provides standard error out functionality.


Examples

Refer to the following example files included with LabVIEW.

  • labview\examples\Graphics and Sound\Sound\Sound File to
   Sound Output.vi


                                                    © National Instruments 2201

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2201 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2202 ordinal=2202 -->
## Functions

Functions

   SoundSound FileFile InfoInfo (refnum)(refnum) VIVI

       Retrieves data about a .wav file. This VI accepts either a path or a refnum.

      (Windows) You must have DirectX 8.0 or later to use this VI. (Linux) You must have the
     Open Sound System (OSS) driver to use this VI.


      Inputs/Outputs

               •     sound file refnum —

          sound file refnum is the reference to the sound file.

           You generate sound file refnum with the Sound File Open VI.

               •       error in (no error) —

             error in describes error conditions that occur before this node runs. This input provides
            standard error in functionality.

               •     sound file refnum out —

          sound file refnum out is the reference to the sound file originally passed in the sound file
          refnum parameter.

               •       total number of samples/ch —

              total number of samples/ch returns the total number of samples per channel in the wave file.

               •     sound format —

          sound format returns the sample rate, the number of channels, and the number of bits per
           sample in the wave file.

                     •     sample rate (S/s) —


2202   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2202 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2203 ordinal=2203 -->
## Functions

Functions


       sample rate (S/s) is the sampling rate for the wave file. Common rates are 44,100 S/s, 22,050
          S/s, and 11,025 S/s.

         •     number of channels —

       number of channels specifies the number of channels in the wave file. This input can
        accept as many channels as the sound card supports. For most sound cards 1 is Mono and 2
           is Stereo.

         •       bits per sample —

         bits per sample is the quality of each sample in bits. Common resolutions are 16 bits and 8
           bits.


   •       error out —

    error out contains error information. This output provides standard error out functionality.


Examples

Refer to the following example files included with LabVIEW.

  • labview\examples\Graphics and Sound\Sound\Sound File to
   Sound Output.vi
SoundSound FileFile ReadRead

Reads data from a .wav file into an array of waveforms. You must manually select the
polymorphic instance you want to use.

(Windows) You must have DirectX 8.0 or later to use this VI.

      Note This VI retrieves only uncompressed wave files. LabVIEW uses large
      amounts of memory when reading an entire wave file at once. Instead, read
      wave files in chunks.


                                                    © National Instruments 2203

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2203 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2204 ordinal=2204 -->
## Functions

Functions


            • Sound File Read (DBL) VI
            • Sound File Read (SGL) VI
            • Sound File Read (U8) VI
            • Sound File Read (I16) VI
            • Sound File Read (I32) VI

     Examples

       Refer to the following example files included with LabVIEW.

            • labview\examples\Graphics and Sound\Sound\Sound File to
        Sound Output.vi
   SoundSound FileFile ReadRead (DBL)(DBL) VIVI

      Reads data from a .wav file into an array of waveforms. You must manually select the
      polymorphic instance you want to use.

      (Windows) You must have DirectX 8.0 or later to use this VI.

           Note This VI retrieves only uncompressed wave files. LabVIEW uses large
            amounts of memory when reading an entire wave file at once. Instead, read
            wave files in chunks.


      Inputs/Outputs

               •     number of samples/ch (-1: all) —

2204   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2204 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2205 ordinal=2205 -->
## Functions

Functions


  number of samples/ch specifies the number of samples per channel to read from the file. -1
  specifies all samples.

•     sound file refnum —

  sound file refnum is the reference to the sound file.

  You generate sound file refnum with the Sound File Open VI.

•      position mode —

  position mode, together with position offset, specifies where the read operation begins.

  Absolute starts the operation at the beginning of the file plus position offset, so the offset is
  relative to the beginning of the file. Relative starts the operation at the current location of the
   file mark plus position offset. The default is Relative.

•      position offset —

  position offset specifies how far from the location specified by position mode to start reading.

  You express position offset in units of samples. The default is 0.

•       error in (no error) —

  error in describes error conditions that occur before this node runs. This input provides
  standard error in functionality.

•     sound file refnum out —

  sound file refnum out is the reference to the sound file originally passed in the sound file
  refnum parameter.

•      data —

  data reads any sound data from the file. For multi-channel sound data, data is an array of
  waveforms where each element of the array is a single channel.

  The specified data type determines the range of values for the sound data.

•       offset —

  offset indicates the new location of the file mark relative to the beginning of the file, in units of
  samples.


                                                   © National Instruments 2205

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2205 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2206 ordinal=2206 -->
## Functions

Functions


          The default is 0.

               •       error out —

             error out contains error information. This output provides standard error out functionality.

               •     end of file? —

          end of file? returns TRUE when the VI reaches the end of the file.


     Examples

       Refer to the following example files included with LabVIEW.

            • labview\examples\Graphics and Sound\Sound\Sound File to
        Sound Output.vi
   SoundSound FileFile ReadRead (SGL)(SGL) VIVI

      Reads data from a .wav file into an array of waveforms. You must manually select the
      polymorphic instance you want to use.

      (Windows) You must have DirectX 8.0 or later to use this VI.

           Note This VI retrieves only uncompressed wave files. LabVIEW uses large
            amounts of memory when reading an entire wave file at once. Instead, read
            wave files in chunks.


2206   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2206 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2207 ordinal=2207 -->
## Functions

Functions

Inputs/Outputs

   •     number of samples/ch (-1: all) —

   number of samples/ch specifies the number of samples per channel to read from the file. -1
     specifies all samples.

   •     sound file refnum —

    sound file refnum is the reference to the sound file.

    You generate sound file refnum with the Sound File Open VI.

   •      position mode —

    position mode, together with position offset, specifies where the read operation begins.

   Absolute starts the operation at the beginning of the file plus position offset, so the offset is
     relative to the beginning of the file. Relative starts the operation at the current location of the
      file mark plus position offset. The default is Relative.

   •      position offset —

    position offset specifies how far from the location specified by position mode to start reading.

    You express position offset in units of samples. The default is 0.

   •       error in (no error) —

    error in describes error conditions that occur before this node runs. This input provides
    standard error in functionality.

   •     sound file refnum out —

    sound file refnum out is the reference to the sound file originally passed in the sound file
    refnum parameter.

   •      data —

    data reads any sound data from the file. For multi-channel sound data, data is an array of
    waveforms where each element of the array is a single channel.

   •       offset —

     offset indicates the new location of the file mark relative to the beginning of the file, in units of


                                                    © National Instruments 2207

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2207 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2208 ordinal=2208 -->
## Functions

Functions


            samples.

          The default is 0.

               •       error out —

             error out contains error information. This output provides standard error out functionality.

               •     end of file? —

          end of file? returns TRUE when the VI reaches the end of the file.


     Examples

       Refer to the following example files included with LabVIEW.

            • labview\examples\Graphics and Sound\Sound\Sound File to
        Sound Output.vi
   SoundSound FileFile ReadRead (U8)(U8) VIVI

      Reads data from a .wav file into an array of waveforms. You must manually select the
      polymorphic instance you want to use.

      (Windows) You must have DirectX 8.0 or later to use this VI.

           Note This VI retrieves only uncompressed wave files. LabVIEW uses large
            amounts of memory when reading an entire wave file at once. Instead, read
            wave files in chunks.


2208   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2208 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2209 ordinal=2209 -->
## Functions

Functions

Inputs/Outputs

   •     number of samples/ch (-1: all) —

   number of samples/ch specifies the number of samples per channel to read from the file. -1
     specifies all samples.

   •     sound file refnum —

    sound file refnum is the reference to the sound file.

    You generate sound file refnum with the Sound File Open VI.

   •      position mode —

    position mode, together with position offset, specifies where the read operation begins.

   Absolute starts the operation at the beginning of the file plus position offset, so the offset is
     relative to the beginning of the file. Relative starts the operation at the current location of the
      file mark plus position offset. The default is Relative.

   •      position offset —

    position offset specifies how far from the location specified by position mode to start reading.

    You express position offset in units of samples. The default is 0.

   •       error in (no error) —

    error in describes error conditions that occur before this node runs. This input provides
    standard error in functionality.

   •     sound file refnum out —

    sound file refnum out is the reference to the sound file originally passed in the sound file
    refnum parameter.

   •      data —

    data reads any sound data from the file. For multi-channel sound data, data is an array of
    waveforms where each element of the array is a single channel.

    The specified data type determines the range of values for the sound data.

   •       offset —


                                                    © National Instruments 2209

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2209 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2210 ordinal=2210 -->
## Functions

Functions


             offset indicates the new location of the file mark relative to the beginning of the file, in units of
            samples.

          The default is 0.

               •       error out —

             error out contains error information. This output provides standard error out functionality.

               •     end of file? —

          end of file? returns TRUE when the VI reaches the end of the file.


     Examples

       Refer to the following example files included with LabVIEW.

            • labview\examples\Graphics and Sound\Sound\Sound File to
        Sound Output.vi
   SoundSound FileFile ReadRead (I16)(I16) VIVI

      Reads data from a .wav file into an array of waveforms. You must manually select the
      polymorphic instance you want to use.

      (Windows) You must have DirectX 8.0 or later to use this VI.

           Note This VI retrieves only uncompressed wave files. LabVIEW uses large
            amounts of memory when reading an entire wave file at once. Instead, read
            wave files in chunks.


2210   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2210 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2211 ordinal=2211 -->
## Functions

Functions

Inputs/Outputs

   •     number of samples/ch (-1: all) —

   number of samples/ch specifies the number of samples per channel to read from the file. -1
     specifies all samples.

   •     sound file refnum —

    sound file refnum is the reference to the sound file.

    You generate sound file refnum with the Sound File Open VI.

   •      position mode —

    position mode, together with position offset, specifies where the read operation begins.

   Absolute starts the operation at the beginning of the file plus position offset, so the offset is
     relative to the beginning of the file. Relative starts the operation at the current location of the
      file mark plus position offset. The default is Relative.

   •      position offset —

    position offset specifies how far from the location specified by position mode to start reading.

    You express position offset in units of samples. The default is 0.

   •       error in (no error) —

    error in describes error conditions that occur before this node runs. This input provides
    standard error in functionality.

   •     sound file refnum out —

    sound file refnum out is the reference to the sound file originally passed in the sound file
    refnum parameter.

   •      data —

    data reads any sound data from the file. For multi-channel sound data, data is an array of
    waveforms where each element of the array is a single channel.

    The specified data type determines the range of values for the sound data.

   •       offset —


                                                    © National Instruments 2211

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2211 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2212 ordinal=2212 -->
## Functions

Functions


             offset indicates the new location of the file mark relative to the beginning of the file, in units of
            samples.

          The default is 0.

               •       error out —

             error out contains error information. This output provides standard error out functionality.

               •     end of file? —

          end of file? returns TRUE when the VI reaches the end of the file.


     Examples

       Refer to the following example files included with LabVIEW.

            • labview\examples\Graphics and Sound\Sound\Sound File to
        Sound Output.vi
   SoundSound FileFile ReadRead (I32)(I32) VIVI

      Reads data from a .wav file into an array of waveforms. You must manually select the
      polymorphic instance you want to use.

      (Windows) You must have DirectX 8.0 or later to use this VI.

           Note This VI retrieves only uncompressed wave files. LabVIEW uses large
            amounts of memory when reading an entire wave file at once. Instead, read
            wave files in chunks.


2212   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2212 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2213 ordinal=2213 -->
## Functions

Functions

Inputs/Outputs

   •     number of samples/ch (-1: all) —

   number of samples/ch specifies the number of samples per channel to read from the file. -1
     specifies all samples.

   •     sound file refnum —

    sound file refnum is the reference to the sound file.

    You generate sound file refnum with the Sound File Open VI.

   •      position mode —

    position mode, together with position offset, specifies where the read operation begins.

   Absolute starts the operation at the beginning of the file plus position offset, so the offset is
     relative to the beginning of the file. Relative starts the operation at the current location of the
      file mark plus position offset. The default is Relative.

   •      position offset —

    position offset specifies how far from the location specified by position mode to start reading.

    You express position offset in units of samples. The default is 0.

   •       error in (no error) —

    error in describes error conditions that occur before this node runs. This input provides
    standard error in functionality.

   •     sound file refnum out —

    sound file refnum out is the reference to the sound file originally passed in the sound file
    refnum parameter.

   •      data —

    data reads any sound data from the file. For multi-channel sound data, data is an array of
    waveforms where each element of the array is a single channel.

    The specified data type determines the range of values for the sound data.

   •       offset —


                                                    © National Instruments 2213

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2213 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2214 ordinal=2214 -->
## Functions

Functions


             offset indicates the new location of the file mark relative to the beginning of the file, in units of
            samples.

          The default is 0.

               •       error out —

             error out contains error information. This output provides standard error out functionality.

               •     end of file? —

          end of file? returns TRUE when the VI reaches the end of the file.


     Examples

       Refer to the following example files included with LabVIEW.

            • labview\examples\Graphics and Sound\Sound\Sound File to
        Sound Output.vi
   SoundSound FileFile WriteWrite

       Writes data from a waveform or an array of waveforms to a .wav file.

      (Windows) You must have DirectX 8.0 or later to use this VI. (Linux) You must have the
     Open Sound System (OSS) driver to use this VI.


            • Sound File Write (DBL) VI
            • Sound File Write (DBL Single) VI
            • Sound File Write (SGL) VI
            • Sound File Write (U8) VI
            • Sound File Write (I16) VI
            • Sound File Write (I32) VI


2214   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2214 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2215 ordinal=2215 -->
## Functions

Functions

Examples

Refer to the following example files included with LabVIEW.

  • labview\examples\Graphics and Sound\Sound\Sound Input to
   File.vi
SoundSound FileFile WriteWrite (DBL)(DBL) VIVI

Writes data from a waveform or an array of waveforms to a .wav file.

(Windows) You must have DirectX 8.0 or later to use this VI. (Linux) You must have the
Open Sound System (OSS) driver to use this VI.


Inputs/Outputs

   •     sound file refnum —

    sound file refnum is the reference to the sound file.

    You generate sound file refnum with the Sound File Open VI.

   •      data —

    data writes any sound data to the internal buffers. For multi-channel sound data, data is an
    array of waveforms where each element of the array is a single channel.

    The specified data type determines the range of values for the sound data.

   •       error in (no error) —

    error in describes error conditions that occur before this node runs. This input provides
    standard error in functionality.

   •     sound file refnum out —


                                                    © National Instruments 2215

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2215 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2216 ordinal=2216 -->
## Functions

Functions


          sound file refnum out is the reference to the sound file originally passed in the sound file
          refnum parameter.

               •       error out —

             error out contains error information. This output provides standard error out functionality.


     Examples

       Refer to the following example files included with LabVIEW.

            • labview\examples\Graphics and Sound\Sound\Sound Input to
        File.vi
   SoundSound FileFile WriteWrite (DBL(DBL Single)Single) VIVI

       Writes data from a waveform or an array of waveforms to a .wav file.

           Note The WFM instance of this VI writes data from a single waveform that
              uses double-precision floating point numbers for the sound data.


      Inputs/Outputs

               •     sound file refnum —

          sound file refnum is the reference to the sound file.

           You generate sound file refnum with the Sound File Open VI.

               •      data —

           data writes any sound data to the internal buffers.


2216   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2216 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2217 ordinal=2217 -->
## Functions

Functions


    The specified data type determines the range of values for the sound data.

   •       error in (no error) —

    error in describes error conditions that occur before this node runs. This input provides
    standard error in functionality.

   •     sound file refnum out —

    sound file refnum out is the reference to the sound file originally passed in the sound file
    refnum parameter.

   •       error out —

    error out contains error information. This output provides standard error out functionality.


Examples

Refer to the following example files included with LabVIEW.

  • labview\examples\Graphics and Sound\Sound\Sound Input to
   File.vi
SoundSound FileFile WriteWrite (SGL)(SGL) VIVI

Writes data from a waveform or an array of waveforms to a .wav file.

      Note Use the SGL instance to write data from a waveform that uses single-
        precision floating point numbers for the sound data.


Inputs/Outputs

   •     sound file refnum —

                                                    © National Instruments 2217

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2217 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2218 ordinal=2218 -->
## Functions

Functions


          sound file refnum is the reference to the sound file.

           You generate sound file refnum with the Sound File Open VI.

               •      data —

           data writes any sound data to the internal buffers. For multi-channel sound data, data is an
             array of waveforms where each element of the array is a single channel.

          The specified data type determines the range of values for the sound data.

               •       error in (no error) —

             error in describes error conditions that occur before this node runs. This input provides
            standard error in functionality.

               •     sound file refnum out —

          sound file refnum out is the reference to the sound file originally passed in the sound file
          refnum parameter.

               •       error out —

             error out contains error information. This output provides standard error out functionality.


     Examples

       Refer to the following example files included with LabVIEW.

            • labview\examples\Graphics and Sound\Sound\Sound Input to
        File.vi
   SoundSound FileFile WriteWrite (U8)(U8) VIVI

       Writes data from a waveform or an array of waveforms to a .wav file.

      (Windows) You must have DirectX 8.0 or later to use this VI. (Linux) You must have the
     Open Sound System (OSS) driver to use this VI.


2218   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2218 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2219 ordinal=2219 -->
## Functions

Functions


Inputs/Outputs

   •     sound file refnum —

    sound file refnum is the reference to the sound file.

    You generate sound file refnum with the Sound File Open VI.

   •      data —

    data writes any sound data to the internal buffers. For multi-channel sound data, data is an
    array of waveforms where each element of the array is a single channel.

    The specified data type determines the range of values for the sound data.

   •       error in (no error) —

    error in describes error conditions that occur before this node runs. This input provides
    standard error in functionality.

   •     sound file refnum out —

    sound file refnum out is the reference to the sound file originally passed in the sound file
    refnum parameter.

   •       error out —

    error out contains error information. This output provides standard error out functionality.


Examples

Refer to the following example files included with LabVIEW.

  • labview\examples\Graphics and Sound\Sound\Sound Input to
   File.vi


                                                    © National Instruments 2219

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2219 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2220 ordinal=2220 -->
## Functions

Functions

   SoundSound FileFile WriteWrite (I16)(I16) VIVI

       Writes data from a waveform or an array of waveforms to a .wav file.

      (Windows) You must have DirectX 8.0 or later to use this VI. (Linux) You must have the
     Open Sound System (OSS) driver to use this VI.


      Inputs/Outputs

               •     sound file refnum —

          sound file refnum is the reference to the sound file.

           You generate sound file refnum with the Sound File Open VI.

               •      data —

           data writes any sound data to the internal buffers. For multi-channel sound data, data is an
             array of waveforms where each element of the array is a single channel.

          The specified data type determines the range of values for the sound data.

               •       error in (no error) —

             error in describes error conditions that occur before this node runs. This input provides
            standard error in functionality.

               •     sound file refnum out —

          sound file refnum out is the reference to the sound file originally passed in the sound file
          refnum parameter.

               •       error out —

             error out contains error information. This output provides standard error out functionality.


2220   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2220 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2221 ordinal=2221 -->
## Functions

Functions

Examples

Refer to the following example files included with LabVIEW.

  • labview\examples\Graphics and Sound\Sound\Sound Input to
   File.vi
SoundSound FileFile WriteWrite (I32)(I32) VIVI

Writes data from a waveform or an array of waveforms to a .wav file.

(Windows) You must have DirectX 8.0 or later to use this VI. (Linux) You must have the
Open Sound System (OSS) driver to use this VI.


Inputs/Outputs

   •     sound file refnum —

    sound file refnum is the reference to the sound file.

    You generate sound file refnum with the Sound File Open VI.

   •      data —

    data writes any sound data to the internal buffers. For multi-channel sound data, data is an
    array of waveforms where each element of the array is a single channel.

    The specified data type determines the range of values for the sound data.

   •       error in (no error) —

    error in describes error conditions that occur before this node runs. This input provides
    standard error in functionality.

   •     sound file refnum out —


                                                    © National Instruments 2221

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2221 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2222 ordinal=2222 -->
## Functions

Functions


          sound file refnum out is the reference to the sound file originally passed in the sound file
          refnum parameter.

               •       error out —

             error out contains error information. This output provides standard error out functionality.


     Examples

       Refer to the following example files included with LabVIEW.

            • labview\examples\Graphics and Sound\Sound\Sound Input to
        File.vi
   SoundSound FileFile CloseClose

       Closes a .wav file.

      (Windows) You must have DirectX 8.0 or later to use this VI. (Linux) You must have the
     Open Sound System (OSS) driver to use this VI.


      Inputs/Outputs

               •     sound file refnum —

          sound file refnum is the reference to the sound file.

           You generate sound file refnum with the Sound File Open VI.

               •       error in (no error) —

             error in describes error conditions that occur before this node runs. This input provides
            standard error in functionality.

               •       error out —

2222   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2222 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2223 ordinal=2223 -->
## Functions

Functions


    error out contains error information. This output provides standard error out functionality.


Examples

Refer to the following example files included with LabVIEW.

  • labview\examples\Graphics and Sound\Sound\Sound Input to
   File.vi
  • labview\examples\Graphics and Sound\Sound\Sound File to
   Sound Output.vi

MathMath PlotPlot HelpersHelpers

This section contains reference information for 2D and 3D Math Plots.

The following VIs appear on the block diagram when you add the associated plot to
the front panel. You can find plots on the 2D Graph and 3D Graph palette.

2D2D CompassCompass PlotPlot HelperHelper

Graphs vectors that emanate from the center origin in a compass plot. Multiple
references to this VI generate multiple plots on the same graph.

      Note This VI appears on the block diagram when you add a Compass Plot to
       the front panel. You can find the Compass Plot on the Graph palette.


  • Plot Helper (Vector) VI
  • Plot Helper (Complex) VI

Examples

Refer to the following example files included with LabVIEW.

                                                    © National Instruments 2223

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2223 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2224 ordinal=2224 -->
## Functions

Functions

            • labview\examples\Controls and Indicators\Graphs and
        Charts\Math Plots - 2D\Compass Plot.vi
    PlotPlot HelperHelper (Vector)(Vector) VIVI

      Graphs vectors that emanate from the center origin in a compass plot. Multiple
       references to this VI generate multiple plots on the same graph.

           Note This VI appears on the block diagram when you add a Compass Plot to
              the front panel. You can find the Compass Plot on the Graph palette.


      Inputs/Outputs

               •     2D Plot Class Obj Array in —

          2D Plot Class Obj Array in is a reference to the class that stores the data of the 2D plot.

               •      theta vector —

            theta vector specifies the angles on the compass plot you want to graph.

               •      radius vector —

            radius vector specifies the vector length as it extends from the center.

               •       error in (no error) —

             error in describes error conditions that occur before this node runs. This input provides
            standard error in functionality.

               •     2D Plot Class Obj Array out —

          2D Plot Class Obj Array out is the graph of the 2D plot.

               •       error out —


2224   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2224 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2225 ordinal=2225 -->
## Functions

Functions


    error out contains error information. This output provides standard error out functionality.


Examples

Refer to the following example files included with LabVIEW.

  • labview\examples\Controls and Indicators\Graphs and
   Charts\Math Plots - 2D\Compass Plot.vi
PlotPlot HelperHelper (Complex)(Complex) VIVI

Graphs vectors that emanate from the center origin in a compass plot. Multiple
references to this VI generate multiple plots on the same graph.

      Note This VI appears on the block diagram when you add a Compass Plot to
       the front panel. You can find the Compass Plot on the Graph palette.


Inputs/Outputs

   •     2D Plot Class Obj Array in —

   2D Plot Class Obj Array in is a reference to the class that stores the data of the 2D plot.

   •      z vector —

    z vector specifies a vector of complex numbers.

   •       error in (no error) —

    error in describes error conditions that occur before this node runs. This input provides
    standard error in functionality.

   •     2D Plot Class Obj Array out —

                                                    © National Instruments 2225

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2225 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2226 ordinal=2226 -->
## Functions

Functions


          2D Plot Class Obj Array out is the graph of the 2D plot.

               •       error out —

             error out contains error information. This output provides standard error out functionality.


     Examples

       Refer to the following example files included with LabVIEW.

            • labview\examples\Controls and Indicators\Graphs and
        Charts\Math Plots - 2D\Compass Plot.vi

     2D2D ErrorError BarBar PlotPlot HelperHelper

      Graphs a plot that displays the percentage or vector of error at each point above and
      below the line graph. Multiple references to this VI generate multiple plots on the same
       graph.

           Note This VI appears on the block diagram when you add a Error Bar Plot to
              the front panel. You can find the Error Bar Plot on the Graph palette.


            • Plot Helper (Percentage) VI
            • Plot Helper (Fixed) VI

     Examples

       Refer to the following example files included with LabVIEW.

            • labview\examples\Controls and Indicators\Graphs and
        Charts\Math Plots - 2D\Error Bar Plot.vi


2226   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2226 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2227 ordinal=2227 -->
## Functions

Functions

PlotPlot HelperHelper (Percentage)(Percentage) VIVI

Graphs a plot that displays the percentage or vector of error at each point above and
below the line graph. Multiple references to this VI generate multiple plots on the same
graph.

      Note This VI appears on the block diagram when you add a Error Bar Plot to
       the front panel. You can find the Error Bar Plot on the Graph palette.


Inputs/Outputs

   •       error b percentage —

    error b percentage specifies the percentage of error that appears at each point below the
    graphed line relative to values you specify in y vector.

   •       error a percentage —

    error a percentage specifies the percentage of error that appears at each point above the
    graphed line relative to values you specify in y vector.

   •     2D Plot Class Obj Array in —

   2D Plot Class Obj Array in is a reference to the class that stores the data of the 2D plot.

   •      x vector —

    x vector specifies the x-coordinates you want to plot.

   •      y vector —

    y vector specifies the y-coordinates you want to plot.

   •       error in (no error) —

                                                    © National Instruments 2227

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2227 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2228 ordinal=2228 -->
## Functions

Functions


             error in describes error conditions that occur before this node runs. This input provides
            standard error in functionality.

               •     2D Plot Class Obj Array out —

          2D Plot Class Obj Array out is the graph of the error bar plot.

               •       error out —

             error out contains error information. This output provides standard error out functionality.


     Examples

       Refer to the following example files included with LabVIEW.

            • labview\examples\Controls and Indicators\Graphs and
        Charts\Math Plots - 2D\Error Bar Plot.vi
    PlotPlot HelperHelper (Fixed)(Fixed) VIVI

      Graphs a plot that displays the percentage or vector of error at each point above and
      below the line graph. Multiple references to this VI generate multiple plots on the same
       graph.

           Note This VI appears on the block diagram when you add a Error Bar Plot to
              the front panel. You can find the Error Bar Plot on the Graph palette.


      Inputs/Outputs

               •       error b vector —

2228   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2228 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2229 ordinal=2229 -->
## Functions

Functions


    error b vector specifies the vector of error that appears at each point below the graphed line
     relative to values you specify in y vector.

   •       error a vector —

    error a vector specifies the vector of error that appears at each point above the graphed line
     relative to values you specify in y vector.

   •     2D Plot Class Obj Array in —

   2D Plot Class Obj Array in is a reference to the class that stores the data of the 2D plot.

   •      x vector —

    x vector specifies the x-coordinates you want to plot.

   •      y vector —

    y vector specifies the y-coordinates you want to plot.

   •       error in (no error) —

    error in describes error conditions that occur before this node runs. This input provides
    standard error in functionality.

   •     2D Plot Class Obj Array out —

   2D Plot Class Obj Array out is the graph of the error bar plot.

   •       error out —

    error out contains error information. This output provides standard error out functionality.


Examples

Refer to the following example files included with LabVIEW.

  • labview\examples\Controls and Indicators\Graphs and
   Charts\Math Plots - 2D\Error Bar Plot.vi


                                                    © National Instruments 2229

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2229 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2230 ordinal=2230 -->
## Functions

Functions

     2D2D FeatherFeather PlotPlot HelperHelper

      Graphs vectors that emanate from equally spaced points along a horizontal axis at
        zero. Multiple references to this VI generate multiple plots on the same graph.

           Note This VI appears on the block diagram when you add a Feather Plot to
              the front panel. You can find the Feather Plot on the Graph palette.


            • Plot Helper (Vector) VI
            • Plot Helper (Complex) VI

     Examples

       Refer to the following example files included with LabVIEW.

            • labview\examples\Controls and Indicators\Graphs and
        Charts\Math Plots - 2D\Feather Plot.vi
    PlotPlot HelperHelper (Vector)(Vector) VIVI

      Graphs vectors that emanate from equally spaced points along a horizontal axis at
        zero. Multiple references to this VI generate multiple plots on the same graph.

           Note This VI appears on the block diagram when you add a Feather Plot to
              the front panel. You can find the Feather Plot on the Graph palette.


2230   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2230 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2231 ordinal=2231 -->
## Functions

Functions

Inputs/Outputs

   •     2D Plot Class Obj Array in —

   2D Plot Class Obj Array in is a reference to the class that stores the data of the 2D plot.

   •      x vector —

    x vector specifies the x-coordinates for the end points of the vectors that emanate from the
    horizontal axis.

   •      y vector —

    y vector specifies the y-coordinates for the length of the vectors that emanate from the
    horizontal axis.

   •       error in (no error) —

    The error in cluster can accept error information wired from VIs previously called. Use this
    information to decide if any functionality should be bypassed in the event of errors from other
     VIs. The pop-up option Explain Error (or Explain Warning) gives more information about the
     error displayed.

   •     2D Plot Class Obj Array out —

   2D Plot Class Obj Array out is the graph of the feather plot.

   •       error out —

    error out passes error or warning information out of a VI to be used by other VIs. Right-click the
    error out indicator on the front panel and select Explain Error or Explain Warning from the
    shortcut menu for more information about the error.


Examples

Refer to the following example files included with LabVIEW.

  • labview\examples\Controls and Indicators\Graphs and
   Charts\Math Plots - 2D\Feather Plot.vi


                                                    © National Instruments 2231

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2231 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2232 ordinal=2232 -->
## Functions

Functions

    PlotPlot HelperHelper (Complex)(Complex) VIVI

      Graphs vectors that emanate from equally spaced points along a horizontal axis at
        zero. Multiple references to this VI generate multiple plots on the same graph.

           Note This VI appears on the block diagram when you add a Feather Plot to
              the front panel. You can find the Feather Plot on the Graph palette.


      Inputs/Outputs

               •     2D Plot Class Obj Array in —

          2D Plot Class Obj Array in is a reference to the class that stores the data of the 2D plot.

               •      z vector —

            z vector specifies a vector of complex numbers.

               •       error in (no error) —

             error in describes error conditions that occur before this node runs. This input provides
            standard error in functionality.

               •     2D Plot Class Obj Array out —

          2D Plot Class Obj Array out is the graph of the feather plot.

               •       error out —

             error out contains error information. This output provides standard error out functionality.


     Examples

       Refer to the following example files included with LabVIEW.


2232   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2232 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2233 ordinal=2233 -->
## Functions

Functions

  • labview\examples\Controls and Indicators\Graphs and
   Charts\Math Plots - 2D\Feather Plot.vi

3D3D BarBar PlotPlot HelperHelper

Generates a plot of vertical bars.

      Note This VI appears on the block diagram when you add a Bar plot to the
        front panel. You can find the Bar plot on the 3D Graph palette.


  • Plot Helper (Matrix) VI
  • Plot Helper (Vector) VI

Examples

Refer to the following example files included with LabVIEW.

  • labview\examples\Controls and Indicators\Graphs and
   Charts\Math Plots - 3D\3D Bar Graph.vi
PlotPlot HelperHelper (Matrix)(Matrix) VIVI

Generates a plot of vertical bars.

      Note This VI appears on the block diagram when you add a Bar plot to the
        front panel. You can find the Bar plot on the 3D Graph palette.


                                                    © National Instruments 2233

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2233 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2234 ordinal=2234 -->
## Functions

Functions

      Inputs/Outputs

               •      y vector —

           y vector is a 1D array that specifies the y-coordinates of the bars you want to plot. If you wire y
            vector the length of y vector must equal the length of z matrix.

               •      z matrix —

            z matrix is a 2D array that specifies the heights of the bars you graph.

               •       error in (no error) —

             error in describes error conditions that occur before this node runs. This input provides
            standard error in functionality.

               •     3D Plot lvclass Array out —

          3D Plot lvclass Array out is the graph of the 3D plot.

               •       error out —

             error out contains error information. This output provides standard error out functionality.


     Examples

       Refer to the following example files included with LabVIEW.

            • labview\examples\Controls and Indicators\Graphs and
        Charts\Math Plots - 3D\3D Bar Graph.vi
    PlotPlot HelperHelper (Vector)(Vector) VIVI

       Generates a plot of vertical bars.

           Note This VI appears on the block diagram when you add a Bar plot to the
                front panel. You can find the Bar plot on the 3D Graph palette.


2234   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2234 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2235 ordinal=2235 -->
## Functions

Functions


Inputs/Outputs

   •      y vector —

    y vector is a 1D array that specifies the y-coordinates of the bars you want to plot. If you wire y
     vector, the length of y vector must equal the length of z vector.

   •      z vector —

    z vector is a 1D array that specifies the heights of the bars you want to plot.

   •       error in (no error) —

    error in describes error conditions that occur before this node runs. This input provides
    standard error in functionality.

   •     3D Plot lvclass Array out —

   3D Plot lvclass Array out is the graph of the 3D plot.

   •       error out —

    error out contains error information. This output provides standard error out functionality.


Examples

Refer to the following example files included with LabVIEW.

  • labview\examples\Controls and Indicators\Graphs and
   Charts\Math Plots - 3D\3D Bar Graph.vi

3D3D CometComet PlotPlot HelperHelper

Creates an animated graph with a circle that follows the data points. Multiple
references to this VI generate multiple plots for the same graph.


                                                    © National Instruments 2235

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2235 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2236 ordinal=2236 -->
## Functions

Functions

           Note This VI appears on the block diagram when you add a Comet plot to
              the front panel. You can find the Comet plot on the 3D Graph palette.


            • Plot Helper (Vector) VI
            • Plot Helper (Matrix) VI
            • Plot Helper (Matrices) VI

     Examples

       Refer to the following example files included with LabVIEW.

            • labview\examples\Controls and Indicators\Graphs and
        Charts\Math Plots - 3D\3D Comet Graph.vi
    PlotPlot HelperHelper (Vector)(Vector) VIVI

       Creates an animated graph with a circle that follows the data points. Multiple
       references to this VI generate multiple plots for the same graph.

           Note This VI appears on the block diagram when you add a Comet plot to
              the front panel. You can find the Comet plot on the 3D Graph palette.


      Inputs/Outputs

               •     3D Plot lvclass Array in —


2236   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2236 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2237 ordinal=2237 -->
## Functions

Functions


   3D Plot lvclass Array in is a reference to the class that stores the data of the 3D plot.

   •      x vector —

    x vector is a 1D array that specifies the x-coordinates that graph the plot.

   •      y vector —

    y vector is a 1D array that specifies the y-coordinates that graph the plot.

   •       error in (no error) —

    error in describes error conditions that occur before this node runs. This input provides
    standard error in functionality.

   •      z vector —

    z vector is a 1D array that specifies the z-coordinates that graph the plot.

   •       Plot ID —

    Plot ID specifies the index of the plot you want to graph. When you graph more than one plot,
     select the drop-down listbox under the color spectrum to the right of the graph to change the
     plot.

   •     3D Plot lvclass Array out —

   3D Plot lvclass Array out is the graph of the 3D plot.

   •       error out —

    error out contains error information. This output provides standard error out functionality.


Examples

Refer to the following example files included with LabVIEW.

  • labview\examples\Controls and Indicators\Graphs and
   Charts\Math Plots - 3D\3D Comet Graph.vi


                                                    © National Instruments 2237

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2237 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2238 ordinal=2238 -->
## Functions

Functions

    PlotPlot HelperHelper (Matrix)(Matrix) VIVI

       Creates an animated graph with a circle that follows the data points. Multiple
       references to this VI generate multiple plots for the same graph.

           Note This VI appears on the block diagram when you add a Comet plot to
              the front panel. You can find the Comet plot on the 3D Graph palette.


      Inputs/Outputs

               •     3D Plot lvclass Array in —

          3D Plot lvclass Array in is a reference to the class that stores the data of the 3D plot.

               •      x vector —

           x vector is a 1D array that specifies the x-coordinates that graph the plot.

               •      y vector —

           y vector is a 1D array that specifies the y-coordinates that graph the plot.

               •       error in (no error) —

             error in describes error conditions that occur before this node runs. This input provides
            standard error in functionality.

               •      z matrix —

            z matrix is a 2D array that specifies the z-coordinates that graph the plot.

               •       Plot ID —


2238   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2238 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2239 ordinal=2239 -->
## Functions

Functions


    Plot ID specifies the index of the plot you want to graph. When you graph more than one plot,
     select the drop-down listbox under the color spectrum to the right of the graph to change the
     plot.

   •     3D Plot lvclass Array out —

   3D Plot lvclass Array out is the graph of the 3D plot.

   •       error out —

    error out contains error information. This output provides standard error out functionality.


Examples

Refer to the following example files included with LabVIEW.

  • labview\examples\Controls and Indicators\Graphs and
   Charts\Math Plots - 3D\3D Comet Graph.vi
PlotPlot HelperHelper (Matrices)(Matrices) VIVI

Creates an animated graph with a circle that follows the data points. Multiple
references to this VI generate multiple plots for the same graph.

      Note This VI appears on the block diagram when you add a Comet plot to
       the front panel. You can find the Comet plot on the 3D Graph palette.


Inputs/Outputs

   •     3D Plot lvclass Array in —


                                                    © National Instruments 2239

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2239 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2240 ordinal=2240 -->
## Functions

Functions


          3D Plot lvclass Array in is a reference to the class that stores the data of the 3D plot.

               •      x matrix —

           x matrix is a 2D array that specifies the x-coordinates that graph the plot.

               •      y matrix —

           y matrix is a 2D array that specifies the y-coordinates that graph the plot.

               •       error in (no error) —

             error in describes error conditions that occur before this node runs. This input provides
            standard error in functionality.

               •      z matrix —

            z matrix is a 2D array that specifies the z-coordinates that graph the plot.

               •       Plot ID —

             Plot ID specifies the index of the plot you want to graph. When you graph more than one plot,
             select the drop-down listbox under the color spectrum to the right of the graph to change the
              plot.

               •     3D Plot lvclass Array out —

          3D Plot lvclass Array out is the graph of the 3D plot.

               •       error out —

             error out contains error information. This output provides standard error out functionality.


     Examples

       Refer to the following example files included with LabVIEW.

            • labview\examples\Controls and Indicators\Graphs and
        Charts\Math Plots - 3D\3D Comet Graph.vi


2240   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2240 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2241 ordinal=2241 -->
## Functions

Functions

3D3D ContourContour PlotPlot HelperHelper

Graphs a plot with contour lines. Multiple references to this VI generate multiple plots
for the same graph.

      Note This VI appears on the block diagram when you add a Contour plot to
       the front panel. You can find the Contour plot on the 3D Graph palette.


  • Plot Helper (Vector) VI
  • Plot Helper (Matrix) VI

When x matrix, y matrix, and z matrix are the same size, the Contour plot graphs
values that correspond to each element at the same location in all the matrices.

Examples

Refer to the following example files included with LabVIEW.

  • labview\examples\Controls and Indicators\Graphs and
   Charts\Math Plots - 3D\3D Contour Graph.vi
PlotPlot HelperHelper (Vector)(Vector) VIVI

Graphs a plot with contour lines. Multiple references to this VI generate multiple plots
for the same graph.

      Note This VI appears on the block diagram when you add a Contour plot to
       the front panel. You can find the Contour plot on the 3D Graph palette.


                                                    © National Instruments 2241

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2241 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2242 ordinal=2242 -->
## Functions

Functions


      Inputs/Outputs

               •     3D Plot lvclass Array in —

          3D Plot lvclass Array in is a reference to the class that stores the data of the 3D plot.

               •      x vector —

           x vector is a 1D array that specifies the x-coordinates that graph the plot.

               •      y vector —

           y vector is a 1D array that specifies the y-coordinates that graph the plot.

               •       error in (no error) —

             error in describes error conditions that occur before this node runs. This input provides
            standard error in functionality.

               •      z matrix —

            z matrix is a 2D array that specifies the z-coordinates that graph the plot.

               •       Plot ID —

             Plot ID specifies the index of the plot you want to graph. When you graph more than one plot,
             select the drop-down listbox under the color spectrum to the right of the graph to change the
              plot.

               •     3D Plot lvclass Array out —

          3D Plot lvclass Array out is the graph of the 3D plot.

               •       error out —

             error out contains error information. This output provides standard error out functionality.


     When x matrix, y matrix, and z matrix are the same size, the Contour plot graphs

2242   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2242 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2243 ordinal=2243 -->
## Functions

Functions

values that correspond to each element at the same location in all the matrices.

Examples

Refer to the following example files included with LabVIEW.

  • labview\examples\Controls and Indicators\Graphs and
   Charts\Math Plots - 3D\3D Contour Graph.vi
PlotPlot HelperHelper (Matrix)(Matrix) VIVI

Graphs a plot with contour lines. Multiple references to this VI generate multiple plots
for the same graph.

      Note This VI appears on the block diagram when you add a Contour plot to
       the front panel. You can find the Contour plot on the 3D Graph palette.


Inputs/Outputs

   •     3D Plot lvclass Array in —

   3D Plot lvclass Array in is a reference to the class that stores the data of the 3D plot.

   •      x matrix —

    x matrix is a 2D array that specifies the x-coordinates that graph the plot.

   •      y matrix —

    y matrix is a 2D array that specifies the y-coordinates that graph the plot.

   •       error in (no error) —


                                                    © National Instruments 2243

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2243 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2244 ordinal=2244 -->
## Functions

Functions


             error in describes error conditions that occur before this node runs. This input provides
            standard error in functionality.

               •      z matrix —

            z matrix is a 2D array that specifies the z-coordinates that graph the plot.

               •       Plot ID —

             Plot ID specifies the index of the plot you want to graph. When you graph more than one plot,
             select the drop-down listbox under the color spectrum to the right of the graph to change the
              plot.

               •     3D Plot lvclass Array out —

          3D Plot lvclass Array out is the graph of the 3D plot.

               •       error out —

             error out contains error information. This output provides standard error out functionality.


     When x matrix, y matrix, and z matrix are the same size, the Contour plot graphs
       values that correspond to each element at the same location in all the matrices.

     Examples

       Refer to the following example files included with LabVIEW.

            • labview\examples\Controls and Indicators\Graphs and
        Charts\Math Plots - 3D\3D Contour Graph.vi

     3D3D MeshMesh PlotPlot HelperHelper

      Graphs a mesh surface with open spaces. Multiple references to this VI generate
       multiple plots for the same graph.

           Note This VI appears on the block diagram when you add a Mesh plot to the
                front panel. You can find the Mesh plot on the 3D Graph palette.


2244   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2244 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2245 ordinal=2245 -->
## Functions

Functions


  • Plot Helper (Vector) VI
  • Plot Helper (Matrix) VI

When x matrix, y matrix, and z matrix are the same size, the Mesh plot graphs values
that correspond to each elements at the same location in all the matrices.

Examples

Refer to the following example files included with LabVIEW.

  • labview\examples\Controls and Indicators\Graphs and
   Charts\Math Plots - 3D\3D Mesh Graph.vi
PlotPlot HelperHelper (Vector)(Vector) VIVI

Graphs a mesh surface with open spaces. Multiple references to this VI generate
multiple plots for the same graph.

      Note This VI appears on the block diagram when you add a Mesh plot to the
        front panel. You can find the Mesh plot on the 3D Graph palette.


Inputs/Outputs

   •     3D Plot lvclass Array in —

   3D Plot lvclass Array in is a reference to the class that stores the data of the 3D plot.

   •      x vector —

                                                    © National Instruments 2245

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2245 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2246 ordinal=2246 -->
## Functions

Functions


           x vector is a 1D array that specifies the x-coordinates that graph the plot.

               •      y vector —

           y vector is a 1D array that specifies the y-coordinates that graph the plot.

               •       error in (no error) —

             error in describes error conditions that occur before this node runs. This input provides
            standard error in functionality.

               •      z matrix —

            z matrix is a 2D array that specifies the z-coordinates that graph the plot.

               •       Plot ID —

             Plot ID specifies the index of the plot you want to graph. When you graph more than one plot,
             select the drop-down listbox under the color spectrum to the right of the graph to change the
              plot.

               •     3D Plot lvclass Array out —

          3D Plot lvclass Array out is the graph of the 3D plot.

               •       error out —

             error out contains error information. This output provides standard error out functionality.


     When x matrix, y matrix, and z matrix are the same size, the Mesh plot graphs values
       that correspond to each elements at the same location in all the matrices.

     Examples

       Refer to the following example files included with LabVIEW.

            • labview\examples\Controls and Indicators\Graphs and
        Charts\Math Plots - 3D\3D Mesh Graph.vi


2246   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2246 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2247 ordinal=2247 -->
## Functions

Functions

PlotPlot HelperHelper (Matrix)(Matrix) VIVI

Graphs a mesh surface with open spaces. Multiple references to this VI generate
multiple plots for the same graph.

      Note This VI appears on the block diagram when you add a Mesh plot to the
        front panel. You can find the Mesh plot on the 3D Graph palette.


Inputs/Outputs

   •     3D Plot lvclass Array in —

   3D Plot lvclass Array in is a reference to the class that stores the data of the 3D plot.

   •      x matrix —

    x matrix is a 2D array that specifies the x-coordinates that graph the plot.

   •      y matrix —

    y matrix is a 2D array that specifies the y-coordinates that graph the plot.

   •       error in (no error) —

    error in describes error conditions that occur before this node runs. This input provides
    standard error in functionality.

   •      z matrix —

    z matrix is a 2D array that specifies the z-coordinates that graph the plot.

   •       Plot ID —


                                                    © National Instruments 2247

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2247 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2248 ordinal=2248 -->
## Functions

Functions


             Plot ID specifies the index of the plot you want to graph. When you graph more than one plot,
             select the drop-down listbox under the color spectrum to the right of the graph to change the
              plot.

               •     3D Plot lvclass Array out —

          3D Plot lvclass Array out is the graph of the 3D plot.

               •       error out —

             error out contains error information. This output provides standard error out functionality.


     When x matrix, y matrix, and z matrix are the same size, the Mesh plot graphs values
       that correspond to each elements at the same location in all the matrices.

     Examples

       Refer to the following example files included with LabVIEW.

            • labview\examples\Controls and Indicators\Graphs and
        Charts\Math Plots - 3D\3D Mesh Graph.vi

     3D3D PiePie PlotPlot HelperHelper

       Generates a pie chart.

           Note This VI appears on the block diagram when you add a Pie plot to the
                front panel. You can find the Pie plot on the 3D Graph palette.


            • Plot Helper (Vector) VI
            • Plot Helper (Matrix) VI


2248   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2248 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2249 ordinal=2249 -->
## Functions

Functions

Examples

Refer to the following example files included with LabVIEW.

  • labview\examples\Controls and Indicators\Graphs and
   Charts\Math Plots - 3D\3D Pie Graph.vi
PlotPlot HelperHelper (Vector)(Vector) VIVI

Generates a pie chart.

      Note This VI appears on the block diagram when you add a Pie plot to the
        front panel. You can find the Pie plot on the 3D Graph palette.


Inputs/Outputs

   •      x vector —

    x vector is a 1D array that specifies the size of the slices, or percentages of pie, that appear in the
    graph. LabVIEW ignores the non-positive elements in x vector.

   •       offset vector —

     offset vector specifies how far slices of pie offset from the center point if they offset. The length
     of offset vector must equal the length of x vector.

   •       error in (no error) —

    error in describes error conditions that occur before this node runs. This input provides
    standard error in functionality.

   •     3D Plot lvclass Array out —

   3D Plot lvclass Array out is the graph of the 3D plot.


                                                    © National Instruments 2249

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2249 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2250 ordinal=2250 -->
## Functions

Functions

               •       error out —

             error out contains error information. This output provides standard error out functionality.


     Examples

       Refer to the following example files included with LabVIEW.

            • labview\examples\Controls and Indicators\Graphs and
        Charts\Math Plots - 3D\3D Pie Graph.vi
    PlotPlot HelperHelper (Matrix)(Matrix) VIVI

       Generates a pie chart.

           Note This VI appears on the block diagram when you add a Pie plot to the
                front panel. You can find the Pie plot on the 3D Graph palette.


      Inputs/Outputs

               •      x matrix —

           x matrix is a 2D array that specifies the size of the slices, or percentages of pie, that appear in the
            graph. LabVIEW ignores the non-positive elements in x matrix.

               •       offset matrix —

             offset matrix specifies how far slices of pie offset from the center point if they offset. The length
             of offset matrix must equal the length of x matrix.

               •       error in (no error) —

             error in describes error conditions that occur before this node runs. This input provides


2250   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2250 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2251 ordinal=2251 -->
## Functions

Functions


    standard error in functionality.

   •     3D Plot lvclass Array out —

   3D Plot lvclass Array out is the graph of the 3D plot.

   •       error out —

    error out contains error information. This output provides standard error out functionality.


Examples

Refer to the following example files included with LabVIEW.

  • labview\examples\Controls and Indicators\Graphs and
   Charts\Math Plots - 3D\3D Pie Graph.vi

3D3D QuiverQuiver PlotPlot HelperHelper

Graphs a plot of normal vectors. Multiple references to this VI generate multiple plots
for the same graph.

      Note This VI appears on the block diagram when you add a Quiver plot to
       the front panel. You can find the Quiver plot on the 3D Graph palette.


  • Plot Helper (Vector) VI
  • Plot Helper (Matrix) VI

Examples

Refer to the following example files included with LabVIEW.

  • labview\examples\Controls and Indicators\Graphs and


                                                    © National Instruments 2251

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2251 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2252 ordinal=2252 -->
## Functions

Functions

        Charts\Math Plots - 3D\3D Quiver Graph.vi
    PlotPlot HelperHelper (Vector)(Vector) VIVI

      Graphs a plot of normal vectors. Multiple references to this VI generate multiple plots
        for the same graph.

           Note This VI appears on the block diagram when you add a Quiver plot to
              the front panel. You can find the Quiver plot on the 3D Graph palette.


      Inputs/Outputs

               •     Nz matrix —

          Nz matrix is a 2D array that specifies the length of the z vector in relation to the z-plane.

               •     Ny matrix —

          Ny matrix is a 2D array that specifies the length of the y vector in relation to the z-plane.

               •     Nx matrix —

          Nx matrix is a 2D array that specifies the length of the x vector in relation to the z-plane.

               •     3D Plot lvclass Array in —

          3D Plot lvclass Array in is a reference to the class that stores the data of the 3D plot.

               •      x vector —

           x vector is a 1D array that specifies the x-coordinates that graph the plot.


2252   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2252 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2253 ordinal=2253 -->
## Functions

Functions

   •      y vector —

    y vector is a 1D array that specifies the y-coordinates that graph the plot.

   •      z matrix —

    z matrix is a 2D array that specifies the z-coordinates that graph the plot.

   •       error in (no error) —

    error in describes error conditions that occur before this node runs. This input provides
    standard error in functionality.

   •       Plot ID —

    Plot ID specifies the index of the plot you want to graph. When you graph more than one plot,
     select the drop-down listbox under the color spectrum to the right of the graph to change the
     plot.

   •     3D Plot lvclass Array out —

   3D Plot lvclass Array out is the graph of the 3D plot.

   •       error out —

    error out contains error information. This output provides standard error out functionality.


Examples

Refer to the following example files included with LabVIEW.

  • labview\examples\Controls and Indicators\Graphs and
   Charts\Math Plots - 3D\3D Quiver Graph.vi
PlotPlot HelperHelper (Matrix)(Matrix) VIVI

Graphs a plot of normal vectors. Multiple references to this VI generate multiple plots
for the same graph.


                                                    © National Instruments 2253

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2253 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2254 ordinal=2254 -->
## Functions

Functions

           Note This VI appears on the block diagram when you add a Quiver plot to
              the front panel. You can find the Quiver plot on the 3D Graph palette.


      Inputs/Outputs

               •     Nz matrix —

          Nz matrix is a 2D array that specifies the length of the z vector in relation to the z-plane.

               •     Ny matrix —

          Ny matrix is a 2D array that specifies the length of the y vector in relation to the z-plane.

               •     Nx matrix —

          Nx matrix is a 2D array that specifies the length of the x vector in relation to the z-plane.

               •     3D Plot lvclass Array in —

          3D Plot lvclass Array in is a reference to the class that stores the data of the 3D plot.

               •      x matrix —

           x matrix is a 2D array that specifies the x-coordinates that graph the plot.

               •      y matrix —

           y matrix is a 2D array that specifies the y-coordinates that graph the plot.

               •      z matrix —

            z matrix is a 2D array that specifies the z-coordinates that graph the plot.

               •       error in (no error) —

2254   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2254 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2255 ordinal=2255 -->
## Functions

Functions


    error in describes error conditions that occur before this node runs. This input provides
    standard error in functionality.

   •       Plot ID —

    Plot ID specifies the index of the plot you want to graph. When you graph more than one plot,
     select the drop-down listbox under the color spectrum to the right of the graph to change the
     plot.

   •     3D Plot lvclass Array out —

   3D Plot lvclass Array out is the graph of the 3D plot.

   •       error out —

    error out contains error information. This output provides standard error out functionality.


Examples

Refer to the following example files included with LabVIEW.

  • labview\examples\Controls and Indicators\Graphs and
   Charts\Math Plots - 3D\3D Quiver Graph.vi

3D3D RibbonRibbon PlotPlot HelperHelper

Generates a plot of parallel lines. Multiple references to this VI generate multiple plots
for the same graph.

      Note This VI appears on the block diagram when you add a Ribbon plot to
       the front panel. You can find the Ribbon plot on the 3D Graph palette.


  • Plot Helper (Standard) VI
  • Plot Helper (Vector) VI


                                                    © National Instruments 2255

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2255 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2256 ordinal=2256 -->
## Functions

Functions

            • Plot Helper (Matrix) VI

     Examples

       Refer to the following example files included with LabVIEW.

            • labview\examples\Controls and Indicators\Graphs and
        Charts\Math Plots - 3D\3D Ribbon Graph.vi
    PlotPlot HelperHelper (Standard)(Standard) VIVI

       Generates a plot of parallel lines. Multiple references to this VI generate multiple plots
        for the same graph.

           Note This VI appears on the block diagram when you add a Ribbon plot to
              the front panel. You can find the Ribbon plot on the 3D Graph palette.


      Inputs/Outputs

               •     3D Plot lvclass Array in —

          3D Plot lvclass Array in is a reference to the class that stores the data of the 3D plot.

               •      y vector —

           y vector is a 1D array that specifies the y-coordinates that graph the plot.

               •       error in (no error) —

             error in describes error conditions that occur before this node runs. This input provides
            standard error in functionality.

               •      z matrix —


2256   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2256 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2257 ordinal=2257 -->
## Functions

Functions


    z matrix is a 2D array that specifies the z-coordinates that graph the plot. A ribbon generates for
    each row in z matrix.

   •       Plot ID —

    Plot ID specifies the index of the plot you want to graph. When you graph more than one plot,
     select the drop-down listbox under the color spectrum to the right of the graph to change the
     plot.

   •     3D Plot lvclass Array out —

   3D Plot lvclass Array out is the graph of the 3D plot.

   •       error out —

    error out contains error information. This output provides standard error out functionality.


Examples

Refer to the following example files included with LabVIEW.

  • labview\examples\Controls and Indicators\Graphs and
   Charts\Math Plots - 3D\3D Ribbon Graph.vi
PlotPlot HelperHelper (Vector)(Vector) VIVI

Generates a plot of parallel lines. Multiple references to this VI generate multiple plots
for the same graph.

      Note This VI appears on the block diagram when you add a Ribbon plot to
       the front panel. You can find the Ribbon plot on the 3D Graph palette.


                                                    © National Instruments 2257

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2257 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2258 ordinal=2258 -->
## Functions

Functions


      Inputs/Outputs

               •     3D Plot lvclass Array in —

          3D Plot lvclass Array in is a reference to the class that stores the data of the 3D plot.

               •      x vector —

           x vector is a 1D array that specifies the x-coordinates that graph the plot.

               •      y vector —

           y vector is a 1D array that specifies the y-coordinates that graph the plot.

               •       error in (no error) —

             error in describes error conditions that occur before this node runs. This input provides
            standard error in functionality.

               •      z matrix —

            z matrix is a 2D array that specifies the z-coordinates that graph the plot. A ribbon generates for
           each row in z matrix.

               •       Plot ID —

             Plot ID specifies the index of the plot you want to graph. When you graph more than one plot,
             select the drop-down listbox under the color spectrum to the right of the graph to change the
              plot.

               •     3D Plot lvclass Array out —

          3D Plot lvclass Array out is the graph of the 3D plot.

               •       error out —

             error out contains error information. This output provides standard error out functionality.


2258   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2258 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2259 ordinal=2259 -->
## Functions

Functions

Examples

Refer to the following example files included with LabVIEW.

  • labview\examples\Controls and Indicators\Graphs and
   Charts\Math Plots - 3D\3D Ribbon Graph.vi
PlotPlot HelperHelper (Matrix)(Matrix) VIVI

Generates a plot of parallel lines. Multiple references to this VI generate multiple plots
for the same graph.

      Note This VI appears on the block diagram when you add a Ribbon plot to
       the front panel. You can find the Ribbon plot on the 3D Graph palette.


Inputs/Outputs

   •     3D Plot lvclass Array in —

   3D Plot lvclass Array in is a reference to the class that stores the data of the 3D plot.

   •      x matrix —

    x matrix is a 2D array that specifies the x-coordinates that graph the plot.

   •      y matrix —

    y matrix is a 2D array that specifies the y-coordinates that graph the plot.

   •       error in (no error) —

    error in describes error conditions that occur before this node runs. This input provides


                                                    © National Instruments 2259

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2259 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2260 ordinal=2260 -->
## Functions

Functions


            standard error in functionality.

               •      z matrix —

            z matrix is a 2D array that specifies the z-coordinates that graph the plot. A ribbon generates for
           each row in z matrix.

               •       Plot ID —

             Plot ID specifies the index of the plot you want to graph. When you graph more than one plot,
             select the drop-down listbox under the color spectrum to the right of the graph to change the
              plot.

               •     3D Plot lvclass Array out —

          3D Plot lvclass Array out is the graph of the 3D plot.

               •       error out —

             error out contains error information. This output provides standard error out functionality.


     Examples

       Refer to the following example files included with LabVIEW.

            • labview\examples\Controls and Indicators\Graphs and
        Charts\Math Plots - 3D\3D Ribbon Graph.vi

     3D3D ScatterScatter PlotPlot HelperHelper

      Graphs data to show trends in statistics and the relationship between two sets of data.
       Multiple references to this VI generate multiple plots for the same graph.

           Note This VI appears on the block diagram when you add a Scatter plot to
              the front panel. You can find the Scatter plot on the 3D Graph palette.


2260   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2260 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2261 ordinal=2261 -->
## Functions

Functions

  • Plot Helper (Vector) VI
  • Plot Helper (Matrix) VI
  • Plot Helper (Matrices) VI

Examples

Refer to the following example files included with LabVIEW.

  • labview\examples\Controls and Indicators\Graphs and
   Charts\Math Plots - 3D\3D Scatter Graph.vi
PlotPlot HelperHelper (Vector)(Vector) VIVI

Graphs data to show trends in statistics and the relationship between two sets of data.
Multiple references to this VI generate multiple plots for the same graph.

      Note This VI appears on the block diagram when you add a Scatter plot to
       the front panel. You can find the Scatter plot on the 3D Graph palette.


Inputs/Outputs

   •     3D Plot lvclass Array in —

   3D Plot lvclass Array in is a reference to the class that stores the data of the 3D plot.

   •      x vector —

    x vector is a 1D array that specifies the x-coordinates that graph the plot.

   •      y vector —


                                                    © National Instruments 2261

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2261 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2262 ordinal=2262 -->
## Functions

Functions


           y vector is a 1D array that specifies the y-coordinates that graph the plot.

               •       error in (no error) —

             error in describes error conditions that occur before this node runs. This input provides
            standard error in functionality.

               •      z vector —

            z vector is a 1D array that specifies the z-coordinates that graph the plot.

               •       Plot ID —

             Plot ID specifies the index of the plot you want to graph. When you graph more than one plot,
             select the drop-down listbox under the color spectrum to the right of the graph to change the
              plot.

               •     3D Plot lvclass Array out —

          3D Plot lvclass Array out is the graph of the 3D plot.

               •       error out —

             error out contains error information. This output provides standard error out functionality.


     Examples

       Refer to the following example files included with LabVIEW.

            • labview\examples\Controls and Indicators\Graphs and
        Charts\Math Plots - 3D\3D Scatter Graph.vi
    PlotPlot HelperHelper (Matrix)(Matrix) VIVI

      Graphs data to show trends in statistics and the relationship between two sets of data.
       Multiple references to this VI generate multiple plots for the same graph.

           Note This VI appears on the block diagram when you add a Scatter plot to


2262   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2262 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2263 ordinal=2263 -->
## Functions

Functions


       the front panel. You can find the Scatter plot on the 3D Graph palette.


Inputs/Outputs

   •     3D Plot lvclass Array in —

   3D Plot lvclass Array in is a reference to the class that stores the data of the 3D plot.

   •      x vector —

    x vector is a 1D array that specifies the x-coordinates that graph the plot.

   •      y vector —

    y vector is a 1D array that specifies the y-coordinates that graph the plot.

   •       error in (no error) —

    error in describes error conditions that occur before this node runs. This input provides
    standard error in functionality.

   •      z matrix —

    z matrix is a 2D array that specifies the z-coordinates that graph the plot.

   •       Plot ID —

    Plot ID specifies the index of the plot you want to graph. When you graph more than one plot,
     select the drop-down listbox under the color spectrum to the right of the graph to change the
     plot.

   •     3D Plot lvclass Array out —

   3D Plot lvclass Array out is the graph of the 3D plot.

   •       error out —


                                                    © National Instruments 2263

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2263 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2264 ordinal=2264 -->
## Functions

Functions


             error out contains error information. This output provides standard error out functionality.


     Examples

       Refer to the following example files included with LabVIEW.

            • labview\examples\Controls and Indicators\Graphs and
        Charts\Math Plots - 3D\3D Scatter Graph.vi
    PlotPlot HelperHelper (Matrices)(Matrices) VIVI

      Graphs data to show trends in statistics and the relationship between two sets of data.
       Multiple references to this VI generate multiple plots for the same graph.

           Note This VI appears on the block diagram when you add a Scatter plot to
              the front panel. You can find the Scatter plot on the 3D Graph palette.


      Inputs/Outputs

               •     3D Plot lvclass Array in —

          3D Plot lvclass Array in is a reference to the class that stores the data of the 3D plot.

               •      x matrix —

           x matrix is a 2D array that specifies the x-coordinates that graph the plot.

               •      y matrix —

           y matrix is a 2D array that specifies the y-coordinates that graph the plot.


2264   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2264 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2265 ordinal=2265 -->
## Functions

Functions

   •       error in (no error) —

    error in describes error conditions that occur before this node runs. This input provides
    standard error in functionality.

   •      z matrix —

    z matrix is a 2D array that specifies the z-coordinates that graph the plot.

   •       Plot ID —

    Plot ID specifies the index of the plot you want to graph. When you graph more than one plot,
     select the drop-down listbox under the color spectrum to the right of the graph to change the
     plot.

   •     3D Plot lvclass Array out —

   3D Plot lvclass Array out is the graph of the 3D plot.

   •       error out —

    error out contains error information. This output provides standard error out functionality.


Examples

Refer to the following example files included with LabVIEW.

  • labview\examples\Controls and Indicators\Graphs and
   Charts\Math Plots - 3D\3D Scatter Graph.vi

3D3D StemStem PlotPlot HelperHelper

Displays an impulse response and organizes data by its distribution at 0 on the z-plane.
Multiple references to this VI generate multiple plots for the same graph.

      Note This VI appears on the block diagram when you add a Stem plot to the
        front panel. You can find the Stem plot on the 3D Graph palette.


                                                    © National Instruments 2265

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2265 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2266 ordinal=2266 -->
## Functions

Functions


            • Plot Helper (Vector) VI
            • Plot Helper (Matrix) VI
            • Plot Helper (Matrices) VI

     Examples

       Refer to the following example files included with LabVIEW.

            • labview\examples\Controls and Indicators\Graphs and
        Charts\Math Plots - 3D\3D Stem Graph.vi
    PlotPlot HelperHelper (Vector)(Vector) VIVI

       Displays an impulse response and organizes data by its distribution at 0 on the z-plane.
       Multiple references to this VI generate multiple plots for the same graph.

           Note This VI appears on the block diagram when you add a Stem plot to the
                front panel. You can find the Stem plot on the 3D Graph palette.


      Inputs/Outputs

               •     3D Plot lvclass Array in —

          3D Plot lvclass Array in is a reference to the class that stores the data of the 3D plot.

               •      x vector —

           x vector is a 1D array that specifies the x-coordinates that graph the plot.


2266   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2266 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2267 ordinal=2267 -->
## Functions

Functions

   •      y vector —

    y vector is a 1D array that specifies the y-coordinates that graph the plot.

   •       error in (no error) —

    error in describes error conditions that occur before this node runs. This input provides
    standard error in functionality.

   •      z vector —

    z vector is a 1D array that specifies the z-coordinates that graph the plot.

   •       Plot ID —

    Plot ID specifies the index of the plot you want to graph. When you graph more than one plot,
     select the drop-down listbox under the color spectrum to the right of the graph to change the
     plot.

   •     3D Plot lvclass Array out —

   3D Plot lvclass Array out is the graph of the 3D plot.

   •       error out —

    error out contains error information. This output provides standard error out functionality.


Examples

Refer to the following example files included with LabVIEW.

  • labview\examples\Controls and Indicators\Graphs and
   Charts\Math Plots - 3D\3D Stem Graph.vi
PlotPlot HelperHelper (Matrix)(Matrix) VIVI

Displays an impulse response and organizes data by its distribution at 0 on the z-plane.
Multiple references to this VI generate multiple plots for the same graph.


                                                    © National Instruments 2267

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2267 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2268 ordinal=2268 -->
## Functions

Functions

           Note This VI appears on the block diagram when you add a Stem plot to the
                front panel. You can find the Stem plot on the 3D Graph palette.


      Inputs/Outputs

               •     3D Plot lvclass Array in —

          3D Plot lvclass Array in is a reference to the class that stores the data of the 3D plot.

               •      x vector —

           x vector is a 1D array that specifies the x-coordinates that graph the plot.

               •      y vector —

           y vector is a 1D array that specifies the y-coordinates that graph the plot.

               •       error in (no error) —

             error in describes error conditions that occur before this node runs. This input provides
            standard error in functionality.

               •      z matrix —

            z matrix is a 2D array that specifies the z-coordinates that graph the plot.

               •       Plot ID —

             Plot ID specifies the index of the plot you want to graph. When you graph more than one plot,
             select the drop-down listbox under the color spectrum to the right of the graph to change the
              plot.

               •     3D Plot lvclass Array out —

          3D Plot lvclass Array out is the graph of the 3D plot.


2268   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2268 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2269 ordinal=2269 -->
## Functions

Functions

   •       error out —

    error out contains error information. This output provides standard error out functionality.


Examples

Refer to the following example files included with LabVIEW.

  • labview\examples\Controls and Indicators\Graphs and
   Charts\Math Plots - 3D\3D Stem Graph.vi
PlotPlot HelperHelper (Matrices)(Matrices) VIVI

Displays an impulse response and organizes data by its distribution at 0 on the z-plane.
Multiple references to this VI generate multiple plots for the same graph.

      Note This VI appears on the block diagram when you add a Stem plot to the
        front panel. You can find the Stem plot on the 3D Graph palette.


Inputs/Outputs

   •     3D Plot lvclass Array in —

   3D Plot lvclass Array in is a reference to the class that stores the data of the 3D plot.

   •      x matrix —

    x matrix is a 2D array that specifies the x-coordinates that graph the plot.

   •      y matrix —


                                                    © National Instruments 2269

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2269 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2270 ordinal=2270 -->
## Functions

Functions


           y matrix is a 2D array that specifies the y-coordinates that graph the plot.

               •       error in (no error) —

             error in describes error conditions that occur before this node runs. This input provides
            standard error in functionality.

               •      z matrix —

            z matrix is a 2D array that specifies the z-coordinates that graph the plot.

               •       Plot ID —

             Plot ID specifies the index of the plot you want to graph. When you graph more than one plot,
             select the drop-down listbox under the color spectrum to the right of the graph to change the
              plot.

               •     3D Plot lvclass Array out —

          3D Plot lvclass Array out is the graph of the 3D plot.

               •       error out —

             error out contains error information. This output provides standard error out functionality.


     Examples

       Refer to the following example files included with LabVIEW.

            • labview\examples\Controls and Indicators\Graphs and
        Charts\Math Plots - 3D\3D Stem Graph.vi

     3D3D SurfaceSurface PlotPlot HelperHelper

      Graphs data with a connecting surface. Multiple references to this VI generate multiple
       plots for the same graph.

           Note This VI appears on the block diagram when you add a Surface plot to
              the front panel. You can find the Surface plot on the 3D Graph palette.


2270   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2270 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2271 ordinal=2271 -->
## Functions

Functions


  • Plot Helper (Vector) VI
  • Plot Helper (Matrix) VI

When x matrix, y matrix, and z matrix are the same size, the Surface plot graphs
values that correspond to each elements at the same location in all the matrices.

Examples

Refer to the following example files included with LabVIEW.

  • labview\examples\Controls and Indicators\Graphs and
   Charts\Math Plots - 3D\3D Surface Graph.vi
PlotPlot HelperHelper (Vector)(Vector) VIVI

Graphs data with a connecting surface. Multiple references to this VI generate multiple
plots for the same graph.

      Note This VI appears on the block diagram when you add a Surface plot to
       the front panel. You can find the Surface plot on the 3D Graph palette.


Inputs/Outputs

   •     3D Plot lvclass Array in —

   3D Plot lvclass Array in is a reference to the class that stores the data of the 3D plot.

   •      x vector —

                                                    © National Instruments 2271

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2271 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2272 ordinal=2272 -->
## Functions

Functions


           x vector is a 1D array that specifies the x-coordinates that graph the plot.

               •      y vector —

           y vector is a 1D array that specifies the y-coordinates that graph the plot.

               •       error in (no error) —

             error in describes error conditions that occur before this node runs. This input provides
            standard error in functionality.

               •      z matrix —

            z matrix is a 2D array that specifies the z-coordinates that graph the plot.

               •       Plot ID —

             Plot ID specifies the index of the plot you want to graph. When you graph more than one plot,
             select the drop-down listbox under the color spectrum to the right of the graph to change the
              plot.

               •     3D Plot lvclass Array out —

          3D Plot lvclass Array out is the graph of the 3D plot.

               •       error out —

             error out contains error information. This output provides standard error out functionality.


     When x matrix, y matrix, and z matrix are the same size, the Surface plot graphs
       values that correspond to each elements at the same location in all the matrices.

     Examples

       Refer to the following example files included with LabVIEW.

            • labview\examples\Controls and Indicators\Graphs and
        Charts\Math Plots - 3D\3D Surface Graph.vi


2272   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2272 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2273 ordinal=2273 -->
## Functions

Functions

PlotPlot HelperHelper (Matrix)(Matrix) VIVI

Graphs data with a connecting surface. Multiple references to this VI generate multiple
plots for the same graph.

      Note This VI appears on the block diagram when you add a Surface plot to
       the front panel. You can find the Surface plot on the 3D Graph palette.


Inputs/Outputs

   •     3D Plot lvclass Array in —

   3D Plot lvclass Array in is a reference to the class that stores the data of the 3D plot.

   •      x matrix —

    x matrix is a 2D array that specifies the x-coordinates that graph the plot.

   •      y matrix —

    y matrix is a 2D array that specifies the y-coordinates that graph the plot.

   •       error in (no error) —

    error in describes error conditions that occur before this node runs. This input provides
    standard error in functionality.

   •      z matrix —

    z matrix is a 2D array that specifies the z-coordinates that graph the plot.

   •       Plot ID —


                                                    © National Instruments 2273

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2273 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2274 ordinal=2274 -->
## Functions

Functions


             Plot ID specifies the index of the plot you want to graph. When you graph more than one plot,
             select the drop-down listbox under the color spectrum to the right of the graph to change the
              plot.

               •     3D Plot lvclass Array out —

          3D Plot lvclass Array out is the graph of the 3D plot.

               •       error out —

             error out contains error information. This output provides standard error out functionality.


     When x matrix, y matrix, and z matrix are the same size, the Surface plot graphs
       values that correspond to each elements at the same location in all the matrices.

     Examples

       Refer to the following example files included with LabVIEW.

            • labview\examples\Controls and Indicators\Graphs and
        Charts\Math Plots - 3D\3D Surface Graph.vi

     3D3D WaterfallWaterfall PlotPlot HelperHelper

      Graphs the surface of the data and the area on the y-axis below the data points.
       Multiple references to this VI generate multiple plots for the same graph.

           Note This VI appears on the block diagram when you add a Waterfall plot to
              the front panel. You can find the Waterfall plot on the 3D Graph palette.


            • Plot Helper (Vector) VI
            • Plot Helper (Matrix) VI

      The Waterfall graph plots only the rows of x matrix, y matrix, and z matrix.

2274   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2274 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2275 ordinal=2275 -->
## Functions

Functions

Examples

Refer to the following example files included with LabVIEW.

  • labview\examples\Controls and Indicators\Graphs and
   Charts\Math Plots - 3D\3D Waterfall Graph.vi
PlotPlot HelperHelper (Vector)(Vector) VIVI

Graphs the surface of the data and the area on the y-axis below the data points.
Multiple references to this VI generate multiple plots for the same graph.

      Note This VI appears on the block diagram when you add a Waterfall plot to
       the front panel. You can find the Waterfall plot on the 3D Graph palette.


Inputs/Outputs

   •     3D Plot lvclass Array in —

   3D Plot lvclass Array in is a reference to the class that stores the data of the 3D plot.

   •      x vector —

    x vector is a 1D array that specifies the x-coordinates that graph the plot.

   •      y vector —

    y vector is a 1D array that specifies the y-coordinates that graph the plot.

   •       error in (no error) —

    error in describes error conditions that occur before this node runs. This input provides


                                                    © National Instruments 2275

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2275 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2276 ordinal=2276 -->
## Functions

Functions


            standard error in functionality.

               •      z matrix —

            z matrix is a 2D array that specifies the z-coordinates that graph the plot.

               •       Plot ID —

             Plot ID specifies the index of the plot you want to graph. When you graph more than one plot,
             select the drop-down listbox under the color spectrum to the right of the graph to change the
              plot.

               •     3D Plot lvclass Array out —

          3D Plot lvclass Array out is the graph of the 3D plot.

               •       error out —

             error out contains error information. This output provides standard error out functionality.


      The Waterfall graph plots only the rows of x matrix, y matrix, and z matrix.

     Examples

       Refer to the following example files included with LabVIEW.

            • labview\examples\Controls and Indicators\Graphs and
        Charts\Math Plots - 3D\3D Waterfall Graph.vi
    PlotPlot HelperHelper (Matrix)(Matrix) VIVI

      Graphs the surface of the data and the area on the y-axis below the data points.
       Multiple references to this VI generate multiple plots for the same graph.

           Note This VI appears on the block diagram when you add a Waterfall plot to
              the front panel. You can find the Waterfall plot on the 3D Graph palette.


2276   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2276 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2277 ordinal=2277 -->
## Functions

Functions


Inputs/Outputs

   •     3D Plot lvclass Array in —

   3D Plot lvclass Array in is a reference to the class that stores the data of the 3D plot.

   •      x matrix —

    x matrix is a 2D array that specifies the x-coordinates that graph the plot.

   •      y matrix —

    y matrix is a 2D array that specifies the y-coordinates that graph the plot.

   •       error in (no error) —

    error in describes error conditions that occur before this node runs. This input provides
    standard error in functionality.

   •      z matrix —

    z matrix is a 2D array that specifies the z-coordinates that graph the plot.

   •       Plot ID —

    Plot ID specifies the index of the plot you want to graph. When you graph more than one plot,
     select the drop-down listbox under the color spectrum to the right of the graph to change the
     plot.

   •     3D Plot lvclass Array out —

   3D Plot lvclass Array out is the graph of the 3D plot.

   •       error out —

    error out contains error information. This output provides standard error out functionality.


The Waterfall graph plots only the rows of x matrix, y matrix, and z matrix.

                                                    © National Instruments 2277

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2277 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2278 ordinal=2278 -->
## Functions

Functions

     Examples

       Refer to the following example files included with LabVIEW.

            • labview\examples\Controls and Indicators\Graphs and
        Charts\Math Plots - 3D\3D Waterfall Graph.vi

     3D3D LineLine PlotPlot SetupSetup

       Plots a line or curve in terms of x, y, and z points. This VI has three 1D array inputs that
       specify each point on the line or curve.

           Note This VI appears on the block diagram when you add a 3D Line Graph to
              the front panel. You can find the 3D Line Graph on the 3D Graph palette.


      Inputs/Outputs

               •       color vector —

             color vector maps each point in the z vector to a color index on the color ramp. By default, the
            values of the z vector are used as the index.

               •       plots in —

             plots in is a reference to the class that stores the data of the 3D plot. This input allows you to
            wire multiple plots.

               •      x vector —

           x vector is a 1D array that specifies the x-coordinates of the points on the plot.

               •      y vector —


2278   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2278 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2279 ordinal=2279 -->
## Functions

Functions


    y vector is a 1D array that specifies the y-coordinates of the points on the plot.

   •      z vector —

    z vector is a 1D array that specifies the z-coordinates of the points on the plot. The x and y
    vectors shift the set of data in the z vector.

   •       plot ID —

    plot ID specifies the index of the plot you want to graph.

   •       plots out —

    plots out is the graph of the 3D plot.


3D3D SurfaceSurface PlotPlot SetupSetup

Plots a surface in terms of x, y, and z points. This VI has two 1D arrays and one 2D array
that specify each point on the plot.

      Note This VI appears on the block diagram when you add a 3D Surface
       Graph to the front panel. You can find the 3D Surface Graph on the 3D Graph
         palette.


Inputs/Outputs

   •       color matrix —

    color matrix maps each point in the z matrix to a color index on the color ramp. By default, the
    values of the z matrix are used as the index.

   •       plots in —


                                                    © National Instruments 2279

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2279 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2280 ordinal=2280 -->
## Functions

Functions


             plots in is a reference to the class that stores the data of the 3D plot. This input allows you to
            wire multiple plots.

               •      x vector —

           x vector is a 1D array that specifies the x-coordinates of the points on the plot.

               •      y vector —

           y vector is a 1D array that specifies the y-coordinates of the points on the plot.

               •      z matrix —

            z matrix is a 2D array that specifies the z-coordinates of the points on the plot. The x and y
             vectors shift the set of data in the z matrix.

               •       plot ID —

             plot ID specifies the index of the plot you want to graph.

               •       plots out —

             plots out is the graph of the 3D plot.


     3D3D ParametricParametric PlotPlot SetupSetup

       Plots a surface in terms of x, y, and z points. This VI has three 2D array inputs that
       specify each point on the plot.

           Note This VI appears on the block diagram when you add a 3D Parametric
             Graph to the front panel. You can find the 3D Parametric Graph on the 3D
            Graph palette


2280   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2280 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2281 ordinal=2281 -->
## Functions

Functions

Inputs/Outputs

   •       color matrix —

    color matrix maps each point in the z matrix to a color index on the color ramp. By default, the
    values of the z matrix are used as the index.

   •       plots in —

    plots in is a reference to the class that stores the data of the 3D plot. This input allows you to
    wire multiple plots.

   •      x matrix —

    x matrix is a 2D array that specifies the x-coordinates of the points on the plot.

   •      y matrix —

    y matrix is a 2D array that specifies the y-coordinates of the points on the plot.

   •      z matrix —

    z matrix is a 2D array that specifies the z-coordinates of the points on the plot.

   •       plot ID —

    plot ID specifies the index of the plot you want to graph.

   •       plots out —

    plots out is the graph of the 3D plot.


XYXY PlotPlot MatrixMatrix HelperHelper

Graphs rows and columns of scatter graphs.

      Note This VI appears on the block diagram when you add a XY Plot Matrix to
       the front panel. You can find the XY Plot Matrix on the Graph palette.


                                                    © National Instruments 2281

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2281 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2282 ordinal=2282 -->
## Functions

Functions


      Inputs/Outputs

               •     2D Plotmatrix Class Obj Array in —

          2D Plot Class Obj Array in is a reference to the class that stores the data of the XY plot.

               •      x matrix —

           x matrix specifies the x-coordinates you want to plot. The number of columns in x matrix
              specifies the number of columns of individual graphs that generate when you run the VI.

               •      y matrix —

           y matrix specifies the y-coordinates you want to plot. The number of columns in y matrix
              specifies the number of rows of individual graphs that generate when you run the VI.

               •       error in (no error) —

             error in describes error conditions that occur before this node runs. This input provides
            standard error in functionality.

               •     2D Plotmatrix Class Obj Array out —

          2D Plotmatrix Class Obj Array out is the graph of the XY plot matrix.

               •       error out —

             error out contains error information. This output provides standard error out functionality.


     Examples

       Refer to the following example files included with LabVIEW.

            • labview\examples\Controls and Indicators\Graphs and
        Charts\Math Plots - 2D\XY Plot Matrix.vi


2282   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2282 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2283 ordinal=2283 -->
## Functions

Functions

3D3D PicturePicture ControlControl

Use the 3D Picture Control VIs to display graphical representations of objects in 3D
scenes.


 Palette Object   Description

 Geometries     Use the Geometries VIs to assign or configure the shapes of objects in a 3D scene.


 Object         Use the Object VIs to create or find objects to use in a 3D scene.


               Use the Transformations VIs to apply common transformations, such as rotation, Transformations                    translation, and scaling, to objects in a 3D scene graph.


               Use the File Loading VIs to load geometries of various model types in a 3D scene File Loading                  graph.


 Helpers        Use the Helpers VIs to perform some common tasks in setting up a 3D scene.


GeometriesGeometries

Use the Geometries VIs to assign or configure the shapes of objects in a 3D scene.


                                                    © National Instruments 2283

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2283 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2284 ordinal=2284 -->
## Functions

Functions


         Palette Object    Description

                          Sets a 3D object you create with the Create Object VI to a box by applying a box
         Create Box                       geometry to the object.


                          Applies a sphere geometry to a three-dimensional object that appears in a 3D         Create Sphere                          scene.


                          Sets a 3D object you create with the Create Object VI to a cone by applying a cone         Create Cone
                       geometry to the object.


                          Sets a 3D object you create with the Create Object VI to a cylinder by applying a         Create Cylinder                            cylinder geometry to the object.


         Create Height    Converts a 2D array of values to a 3D height field and applies the height field to a
          Field          3D object that appears in a 3D scene.


         Create Mesh      Creates a 3D mesh to apply to a 3D object that appears in a 3D scene.

         Create Mesh                          Creates a mesh with customizable color and draw options.        with Attributes

         Create 3D Axis    Creates an x, y, and z axis object to define 3D space in a scene.

                          Sets a 3D object you create with the Create Object VI to a text object and applies
         Create Text
                         the text, font, and color you specify to the object.

         Create Text with
                          Creates a text object with customizable format and position options.
        Alignment

    CreateCreate BoxBox

       Sets a 3D object you create with the Create Object VI to a box by applying a box
      geometry to the object.


2284   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2284 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2285 ordinal=2285 -->
## Functions

Functions


Inputs/Outputs

   •      Color —

    Color specifies the color of the object in RGBA format. Color accepts a cluster of numeric values
    0 through 1, where 0 represents the absence of the red, green, or blue color and 1 represents a
      full saturation of the color. The alpha value indicates the transparency of the red, green, and
    blue colors.

         •     Red —

       Red specifies the red value. The default is 1.

         •      Green —

       Green specifies the green value. The default is 0.

         •      Blue —

        Blue specifies the blue value. The default is 0.

         •      Alpha —

        Alpha specifies the level of opacity of the RGB color when you apply the color to a 3D object.
        Alpha must be a value between 0 and 1. The default is 1.


   •      Length X —

    Length X is the length of the x-axis.

   •      Length Y —

    Length Y is the length of the y-axis.

   •      Length Z —

    Length Z is the length of the z-axis.


                                                    © National Instruments 2285

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2285 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2286 ordinal=2286 -->
## Functions

Functions

               •       error in (no error) —

             error in describes error conditions that occur before this node runs. This input provides
            standard error in functionality.

               •     New Box Refnum —

         New Box Refnum is the reference to the created geometry.

               •       error out —

             error out contains error information. This output provides standard error out functionality.


     Examples

       Refer to the following example files included with LabVIEW.

            • labview\examples\Controls and Indicators\Graphs and
        Charts\Math Plots - 3D (ActiveX)\3D Curve Graph
        (ActiveX).vi
    CreateCreate SphereSphere

       Applies a sphere geometry to a three-dimensional object that appears in a 3D scene.


      Inputs/Outputs

               •      Color —

            Color specifies the color of the object in RGBA format. Color accepts a cluster of numeric values
           0 through 1, where 0 represents the absence of the red, green, or blue color and 1 represents a
                full saturation of the color. The alpha value indicates the transparency of the red, green, and
            blue colors.


2286   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2286 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2287 ordinal=2287 -->
## Functions

Functions


         •     Red —

       Red specifies the red value. The default is 1.

         •      Green —

       Green specifies the green value. The default is 0.

         •      Blue —

        Blue specifies the blue value. The default is 0.

         •      Alpha —

        Alpha specifies the level of opacity of the RGB color when you apply the color to a 3D object.
        Alpha must be a value between 0 and 1. The default is 1.


   •      Radius —

    Radius specifies the radius of the object.

   •       error in (no error) —

    error in describes error conditions that occur before this node runs. This input provides
    standard error in functionality.

   •       Detail —

     Detail specifies the number of vertices to use in drawing the object. A higher detail value
    produces a better approximation of the geometry. The default is 1.

   •     New Sphere Refnum —

   New Sphere Refnum is the reference to the created geometry.

   •       error out —

    error out contains error information. This output provides standard error out functionality.


Examples

Refer to the following example files included with LabVIEW.

                                                    © National Instruments 2287

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2287 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2288 ordinal=2288 -->
## Functions

Functions

            • labview\examples\Graphics and Sound\3D Picture Control\3D
        Model of Solar System.vi
    CreateCreate ConeCone

       Sets a 3D object you create with the Create Object VI to a cone by applying a cone
      geometry to the object.


      Inputs/Outputs

               •      Color —

            Color specifies the color of the object in RGBA format. Color accepts a cluster of numeric values
           0 through 1, where 0 represents the absence of the red, green, or blue color and 1 represents a
                full saturation of the color. The alpha value indicates the transparency of the red, green, and
            blue colors.

                     •     Red —

             Red specifies the red value. The default is 1.

                     •      Green —

              Green specifies the green value. The default is 0.

                     •      Blue —

               Blue specifies the blue value. The default is 0.

                     •      Alpha —

               Alpha specifies the level of opacity of the RGB color when you apply the color to a 3D object.
               Alpha must be a value between 0 and 1. The default is 1.


               •      Height —

2288   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2288 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2289 ordinal=2289 -->
## Functions

Functions


    Height specifies the length of the vertical axis of the object.

   •      Radius —

    Radius specifies the radius of the object.

   •       error in (no error) —

    error in describes error conditions that occur before this node runs. This input provides
    standard error in functionality.

   •       Detail —

     Detail specifies the number of vertices to use in drawing the object. A higher detail value
    produces a better approximation of the geometry. The default is 1.

   •     New Cone Refnum —

   New Cone Refnum is the reference to the created geometry.

   •       error out —

    error out contains error information. This output provides standard error out functionality.

CreateCreate CylinderCylinder

Sets a 3D object you create with the Create Object VI to a cylinder by applying a
cylinder geometry to the object.


Inputs/Outputs

   •      Color —

    Color specifies the color of the object in RGBA format. Color accepts a cluster of numeric values


                                                    © National Instruments 2289

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2289 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2290 ordinal=2290 -->
## Functions

Functions


           0 through 1, where 0 represents the absence of the red, green, or blue color and 1 represents a
                full saturation of the color. The alpha value indicates the transparency of the red, green, and
            blue colors.

                     •     Red —

             Red specifies the red value. The default is 1.

                     •      Green —

              Green specifies the green value. The default is 0.

                     •      Blue —

               Blue specifies the blue value. The default is 0.

                     •      Alpha —

               Alpha specifies the level of opacity of the RGB color when you apply the color to a 3D object.
               Alpha must be a value between 0 and 1. The default is 1.


               •      Height —

           Height specifies the length of the vertical axis of the object.

               •      Radius —

           Radius specifies the radius of the object.

               •       error in (no error) —

             error in describes error conditions that occur before this node runs. This input provides
            standard error in functionality.

               •       Detail —

             Detail specifies the number of vertices to use in drawing the object. A higher detail value
           produces a better approximation of the geometry. The default is 1.

               •     New Cylinder Refnum —

         New Cylinder Refnum is the reference to the created geometry.


2290   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2290 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2291 ordinal=2291 -->
## Functions

Functions

   •       error out —

    error out contains error information. This output provides standard error out functionality.

CreateCreate HeightHeight FieldField

Converts a 2D array of values to a 3D height field and applies the height field to a 3D
object that appears in a 3D scene.


Inputs/Outputs

   •      Color —

    Color specifies the color of the object in RGBA format. Color accepts a cluster of numeric values
    0 through 1, where 0 represents the absence of the red, green, or blue color and 1 represents a
      full saturation of the color. The alpha value indicates the transparency of the red, green, and
    blue colors.

         •     Red —

       Red specifies the red value. The default is 1.

         •      Green —

       Green specifies the green value. The default is 0.

         •      Blue —

        Blue specifies the blue value. The default is 0.

         •      Alpha —


                                                    © National Instruments 2291

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2291 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2292 ordinal=2292 -->
## Functions

Functions


               Alpha specifies the level of opacity of the RGB color when you apply the color to a 3D object.
               Alpha must be a value between 0 and 1. The default is 1.


               •      Data —

           Data is a 2D array of values that represent the height of the surface of the object at evenly spaced
              intervals.

               •     Row Interval —

         Row Interval specifies the distance between the intervals on the x-axis of the object at which the
            height field Data is taken.

               •     Column Interval —

          Column Interval specifies the distance between the intervals on the y-axis of the object at which
            the height field Data is taken.

               •       error in (no error) —

             error in describes error conditions that occur before this node runs. This input provides
            standard error in functionality.

               •      Base Height —

           Base Height specifies the actual height value of the surface of the object when the value in the
            height field is the minimum z value.

               •     New Height Field Refnum —

         New Height Field Refnum is the reference to the created geometry.

               •       error out —

             error out contains error information. This output provides standard error out functionality.

    CreateCreate MeshMesh

       Creates a 3D mesh to apply to a 3D object that appears in a 3D scene.

2292   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2292 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2293 ordinal=2293 -->
## Functions

Functions


Inputs/Outputs

   •       error in (no error) —

    error in describes error conditions that occur before this node runs. This input provides
    standard error in functionality.

   •     New Mesh Refnum —

   New Mesh Refnum returns the reference to the mesh.

   •       error out —

    error out contains error information. This output provides standard error out functionality.


Examples

Refer to the following example files included with LabVIEW.

  • labview\examples\Controls and Indicators\Graphs and
   Charts\Math Plots - 3D (ActiveX)\3D Curve Graph
   (ActiveX).vi
CreateCreate MeshMesh withwith AttributesAttributes

Creates a mesh with customizable color and draw options.


                                                    © National Instruments 2293

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2293 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2294 ordinal=2294 -->
## Functions

Functions

      Inputs/Outputs

               •      Color Array —

            Color Array specifies the RGBA color values for the colors that Color Binding Mode applies to the
          3D object. Color Binding Mode references only the first index in the array if you set the mode to
         Overall whereas it references the respective number of indices if you set the mode to Per
         Primitive or Per Vertex.

                     •     Red —

             Red specifies the red value. The default is 1.

                     •      Green —

              Green specifies the green value. The default is 0.

                     •      Blue —

               Blue specifies the blue value. The default is 0.

                     •      Alpha —

               Alpha specifies the level of opacity of the RGB color when the color is applied to the 3D
                  object. Alpha must be a value between 0 and 1. The default is 1.


               •      Color Binding Mode —

            Color Binding Mode specifies the mode to use to bind color to the mesh. The mode determines
         how LabVIEW assigns the color you specify in Color Array.

               Note The Per Primitive and Overall modes differ in behavior only when
                 Draw Mode is Points, Lines, Triangles, or Quads.


           0 Overall (default)—One color binds uniformly to the entire mesh.
           1 Per Primitive—Different colors bind to each primitive in the mesh.
           2 Per Vertex—Different colors bind to each vertex of the mesh.
           3 Binding Off—No colors bind to the mesh.

               •     Draw Mode —


2294   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2294 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2295 ordinal=2295 -->
## Functions

Functions


  Draw Mode specifies the mode LabVIEW uses to draw the mesh. The mode determines how
  LabVIEW interprets the data you wire to Vertex Array.

  0      Points (default)
  1      Lines
  2      Line Strip
  3      Line Loop
  4      Triangles
  5      Triangle Strip
  6      Triangle Fan
  7     Quads
  8     Quad Strip
  9     Polygon

•      Vertex Array —

  Vertex Array sets the x, y, and z coordinate values in 3D space that LabVIEW uses to draw the
  mesh. The settings you specify in Color Array, Draw Mode, and Indices determine how LabVIEW
  interprets the vertices.

      •     X —

      •      Y —

      •     Z —


•       Indices —

  Indices determines the order in which LabVIEW processes the data in the Color Array and Vertex
  Array of the mesh. For example, if Indices is [3, 2, 4, 1], then V0 appears at index 3 in the Vertex
  Array, the color of V0 appears at index 3 in the Color Array, and so on.

        Note If you set Color Binding Mode to Per Primitive, the color refers to the
            entire face formed by V0, V1…VN (where Draw Mode determines N) rather than only
           the index you specify.

•     Normal Array —

  Normal Array sets the x, y, and z values that define the array of normals that Normal Binding


                                                   © National Instruments 2295

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2295 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2296 ordinal=2296 -->
## Functions

Functions


         Mode applies to the 3D object.

                     •     X —

                     •      Y —

                     •     Z —


               •       error in (no error) —

             error in describes error conditions that occur before this node runs. This input provides
            standard error in functionality.

               •     Normal Binding Mode —

          Normal Binding Mode sets the binding mode for the normal vectors of the mesh. The mode
            determines how LabVIEW assigns the normals you specify in Normal Array to the 3D object.
           Normals determine how lights in a 3D scene affect the rendering of a 3D object.

           0        Overall
           1       Per Primitive
           2       Per Vertex
           3       Binding Off

               •      Texture Coordinate Array —

            Texture Coordinate Array sets the s and t coordinates that define how to apply a texture to the
           mesh. You must assign a texture to the mesh with the Apply Texture VI for this array to have
           meaning. Each element of the array is a coordinate in a 2-D plane of domain {0..1, 0..1}, where
               [0,0] is the bottom-left pixel of the image, and [1, 1] is the top-right pixel.

                     •     S —

                     •     T —


               •     New Mesh Refnum —

         New Mesh Refnum returns the reference to the mesh.

               •       error out —


2296   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2296 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2297 ordinal=2297 -->
## Functions

Functions


    error out contains error information. This output provides standard error out functionality.

CreateCreate 3D3D AxisAxis

Creates an x, y, and z axis object to define 3D space in a scene.


Inputs/Outputs

   •      Half plane? —

    Half plane? specifies whether to use both sides of the axis boundary. The default is TRUE, which
     specifies to use a half plane.

   •      Color —

    Color specifies the color of the object in RGBA format. Color accepts a cluster of numeric values
    0 through 1, where 0 represents the absence of the red, green, or blue color and 1 represents a
      full saturation of the color. The alpha value indicates the transparency of the red, green, and
    blue colors.

         •     Red —

       Red specifies the red value. The default is 1.

         •      Green —

       Green specifies the green value. The default is 0.

         •      Blue —


                                                    © National Instruments 2297

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2297 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2298 ordinal=2298 -->
## Functions

Functions


               Blue specifies the blue value. The default is 0.

                     •      Alpha —

               Alpha specifies the level of opacity of the RGB color when you apply the color to a 3D object.
               Alpha must be a value between 0 and 1. The default is 1.


               •     Name —

         Name specifies the name of the axis object.

               •      Length —

           Length specifies the length of the axis in coordinate units. The default is 2.

               •      Radius —

           Radius specifies the radius of the axis in coordinate units. The default is 0.01.

               •       error in (no error) —

             error in describes error conditions that occur before this node runs. This input provides
            standard error in functionality.

               •       Axis label? —

             Axis label? specifies whether to display axis labels. The default is FALSE.

               •      Character Size —

            Character Size specifies the height of the axis label text characters in coordinate units. For
            example, set character size to 1 to create an axis label equal in height to a geometric object with
           a height of 1. The default is 0.5.

               •     New Object Refnum —

         New Object Refnum returns the reference to the object.

               •       error out —

             error out contains error information. This output provides standard error out functionality.


2298   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2298 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2299 ordinal=2299 -->
## Functions

Functions

CreateCreate TextText

Sets a 3D object you create with the Create Object VI to a text object and applies the
text, font, and color you specify to the object.


Inputs/Outputs

   •      Text —

    Text is the text that appears when you generate the 3D scene.

   •      Path to font file —

    Path to font file specifies the path to the font you want to use to display the Text. LabVIEW
    accepts only TrueType fonts. The path you wire to this VI must have a .ttf file extension. If you
   do not wire Path to font file, LabVIEW displays the text using a Courier font.

   •      Color —

    Color specifies the color of the object in RGBA format. Color accepts a cluster of numeric values
    0 through 1, where 0 represents the absence of the red, green, or blue color and 1 represents a
      full saturation of the color. The alpha value indicates the transparency of the red, green, and
    blue colors.

         •     Red —

       Red specifies the red value. The default is 1.

         •      Green —

       Green specifies the green value. The default is 0.

         •      Blue —

        Blue specifies the blue value. The default is 0.


                                                    © National Instruments 2299

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2299 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2300 ordinal=2300 -->
## Functions

Functions


                     •      Alpha —

               Alpha specifies the level of opacity of the RGB color when you apply the color to a 3D object.
               Alpha must be a value between 0 and 1. The default is 1.


               •       error in (no error) —

             error in describes error conditions that occur before this node runs. This input provides
            standard error in functionality.

               •     New Text Refnum —

         New Text Refnum returns a reference to the text, including the font and color you specify.

               •       error out —

             error out contains error information. This output provides standard error out functionality.

    CreateCreate TextText withwith AlignmentAlignment

       Creates a text object with customizable format and position options.


      Inputs/Outputs

               •      Font Options —

           Font Options specifies alignment, position, and wrap options for the text.

                     •      Alignment —


2300   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2300 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2301 ordinal=2301 -->
## Functions

Functions


      •      Horizontal Alignment —

      Horizontal Alignment specifies the horizontal alignment of the text.

      0           Center
      1             Left
      2           Right

      •       Vertical Alignment —

       Vertical Alignment specifies the vertical alignment of the text.

      0    Base Line
      1    Bottom
      2    Bottom Base Line
      3    Center
      4    Top


•       Axis Alignment —

  Axis Alignment specifies the alignment of the text in relation to the x, y, and z axes.

  0      Reversed X-Y
  1      Reversed X-Z
  2      Reversed Y-Z
  3      Screen
  4       X-Y
  5      X-Z
  6       Y-Z

•       Vertical? —

  Vertical? specifies whether the text runs vertically. The default is FALSE.

•     Wrap Distance —

  Wrap Distance specifies the distance to wrap the text in coordinate units.


                                                © National Instruments 2301

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2301 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2302 ordinal=2302 -->
## Functions

Functions

               •      Color —

            Color specifies the color of the object in RGBA format. Color accepts a cluster of numeric values
           0 through 1, where 0 represents the absence of the red, green, or blue color and 1 represents a
                full saturation of the color. The alpha value indicates the transparency of the red, green, and
            blue colors.

                     •     Red —

             Red specifies the red value. The default is 1.

                     •      Green —

              Green specifies the green value. The default is 0.

                     •      Blue —

               Blue specifies the blue value. The default is 0.

                     •      Alpha —

               Alpha specifies the level of opacity of the RGB color when you apply the color to a 3D object.
               Alpha must be a value between 0 and 1. The default is 1.


               •      Text —

            Text specifies the text of the object.

               •      Font Name —

           Font Name specifies the font to use for the text.

                    If you misspell the font name or specify a font that is not installed on the computer, the
            operating system selects a font.

               •      Character Size —

            Character Size specifies the height of the text characters in coordinate units. For example, set
             character size to 1 to create text characters equal in height to a geometric object with a height of
               1. The default is 0.5.

               •       error in (no error) —


2302   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2302 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2303 ordinal=2303 -->
## Functions

Functions


    error in describes error conditions that occur before this node runs. This input provides
    standard error in functionality.

   •     New Text Refnum —

   New Text Refnum returns a reference to the text, including the font and color you specify.

   •       error out —

    error out contains error information. This output provides standard error out functionality.


ObjectObject

Use the Object VIs to create or find objects to use in a 3D scene.


 Palette             Description
 Object

 Create             Creates a new 3D object to display in the 3D scene. Object


 Add Object  Adds a 3D object to a scene.


             Takes a 3D scene reference and an object name and returns the first object in the
 Find Object
            scene with a matching name.

 Set          Specifies surface properties used by lighting equations during rendering. Inputs
 Material     specified by this VI appear only in lit scenes.

 Set
 Drawing     Specifies the rendering mode for 3D objects.
 Style

 Set
            Blends fragment color outputs with destination colors for texturing 3D objects.
 Blending


                                                    © National Instruments 2303

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2303 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2304 ordinal=2304 -->
## Functions

Functions

    CreateCreate ObjectObject

       Creates a new 3D object to display in the 3D scene.

      To display a new object in the 3D picture control, you must use the SceneObject
       Properties and SceneObject Methods to set the geometric form and other attributes of
       the object.


            • Create Object (name) VI
            • Create Object (drawable) VI
            • Create Object (drawable with reference) VI

     Examples

       Refer to the following example files included with LabVIEW.

            • labview\examples\Graphics and Sound\3D Picture Control\3D
        Model of Solar System.vi
            • labview\examples\Graphics and Sound\3D Picture Control\
        Order of Transformations.vi
            • labview\examples\Graphics and Sound\3D Picture Control\
        Using Meshes.vi
   AddAdd ObjectObject

      Adds a 3D object to a scene.


            • Add Object (no reference) VI
            • Add Object (reference) VI


2304   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2304 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2305 ordinal=2305 -->
## Functions

Functions

AddAdd ObjectObject (no(no reference)reference) VIVI

Adds a 3D object to a scene.


Inputs/Outputs

   •      Scene Object In —

    Scene Object In specifies a reference to the scene you want to manipulate.

   •     New Object In —

   New Object In specifies a reference to the object you want to add to the scene.

   •       error in (no error) —

    error in describes error conditions that occur before this node runs. This input provides
    standard error in functionality.

   •      Scene Object Out —

    Scene Object Out returns a reference to the scene object.

   •       error out —

    error out contains error information. This output provides standard error out functionality.

AddAdd ObjectObject (reference)(reference) VIVI

Adds a 3D object to a scene.


                                                    © National Instruments 2305

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2305 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2306 ordinal=2306 -->
## Functions

Functions

      Inputs/Outputs

               •      Scene Object In —

           Scene Object In specifies a reference to the scene you want to manipulate.

               •     New Object In —

         New Object In specifies a reference to the object you want to add to the scene.

               •       error in (no error) —

             error in describes error conditions that occur before this node runs. This input provides
            standard error in functionality.

               •      Scene Object Out —

           Scene Object Out returns a reference to the scene object.

               •     New Object Out —

         New Object Out returns a reference to the object you add to the scene.

               •       error out —

             error out contains error information. This output provides standard error out functionality.

   FindFind ObjectObject

      Takes a 3D scene reference and an object name and returns the first object in the scene
       with a matching name.


      Inputs/Outputs

               •      Scene Refnum —


2306   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2306 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2307 ordinal=2307 -->
## Functions

Functions


    Scene Refnum is the reference to the scene that contains the object.

   •      Object Name —

    Object Name is the name of the object you want to find.

   •       error in (no error) —

    error in describes error conditions that occur before this node runs. This input provides
    standard error in functionality.

   •      Object Refnum —

    Object Refnum is the reference to the found object.

   •       error out —

    error out contains error information. This output provides standard error out functionality.

SetSet MaterialMaterial

Specifies surface properties used by lighting equations during rendering. Inputs
specified by this VI appear only in lit scenes.


Inputs/Outputs

   •      Specular —

    Specular specifies the RGBA color value that represents the reflection of direct, specular light off
     of the object.


                                                    © National Instruments 2307

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2307 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2308 ordinal=2308 -->
## Functions

Functions


                     •     Red —

             Red specifies the red value. The default is 0.

                     •      Green —

              Green specifies the green value. The default is 0.

                     •      Blue —

               Blue specifies the blue value. The default is 0.

                     •      Alpha —

               Alpha specifies the level of opacity. The default value is 0.


               •     Ambient —

           Ambient specifies the RGBA color value that indirect, ambient light affects.

                     •     Red —

             Red specifies the red value. The default is 0.

                     •      Green —

              Green specifies the green value. The default is 0.

                     •      Blue —

               Blue specifies the blue value. The default is 0.

                     •      Alpha —

               Alpha specifies the level of opacity. The default value is 0.


               •      Scene Object In —

           Scene Object In specifies a reference to the scene you want to manipulate.

               •      Color Mode —


2308   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2308 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2309 ordinal=2309 -->
## Functions

Functions


  Color Mode specifies how the 3D object reacts to light.

  0 Inherit Material (default)—The object inherits the color mode of a parent object.
   Use entire Material—The emissive color of the material and its ambient, diffuse, and specular  1    reflectance values all affect the reaction of the material to a light source.
   Ignore Ambient—LabVIEW ignores the ambient color and uses the base color of the object in  2     its place.
   Ignore Diffuse—LabVIEW ignores the diffuse color and uses the base color of the object in its  3    place.
   Ignore Specular—LabVIEW ignores the specular color and uses the base color of the object in  4     its place.
   Ignore Emission—LabVIEW ignores the emissive color and uses the base color of the object in  5     its place.
   Ignore Ambient and Diffuse—LabVIEW ignores the ambient and diffuse colors and uses the  6   base color of the object in their place.

•      Shininess —

  Shininess specifies the size of the highlight that appears on the object when light reflects
  specularly off the object. Shininess can be a value from 0-128. The default is 0.

•       error in (no error) —

  error in describes error conditions that occur before this node runs. This input provides
  standard error in functionality.

•      Emission —

  Emission specifies the RGBA color value of the emissive light of the object. Emissive light
  emanates from the object itself instead of an external light source.

      •     Red —

     Red specifies the red value. The default is 0.

      •      Green —

      Green specifies the green value. The default is 0.

      •      Blue —


                                                   © National Instruments 2309

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2309 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2310 ordinal=2310 -->
## Functions

Functions


               Blue specifies the blue value. The default is 0.

                     •      Alpha —

               Alpha specifies the level of opacity. The default value is 0.


               •       Diffuse —

             Diffuse specifies the RGBA color value of the lit object. LabVIEW determines the RBGA value
           based on the angle between the orientation of the object and the direction of the light source.

                     •     Red —

             Red specifies the red value. The default is 0.

                     •      Green —

              Green specifies the green value. The default is 0.

                     •      Blue —

               Blue specifies the blue value. The default is 0.

                     •      Alpha —

               Alpha specifies the level of opacity. The default value is 0.


               •      Scene Object Out —

           Scene Object Out returns a reference to the scene object.

               •       error out —

             error out contains error information. This output provides standard error out functionality.

    SetSet DrawingDrawing StyleStyle

       Specifies the rendering mode for 3D objects.

2310   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2310 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2311 ordinal=2311 -->
## Functions

Functions


Inputs/Outputs

   •      Face Culling Mode —

    Face Culling Mode specifies whether an object's front-facing and back-facing polygons are
     visible.

    0 Inherit Value—Inherits the mode of the parent object.
    1 No Culling—Both the front and the back side are visible.
    2 Cull Back Face—Only the front side is visible.
    3 Cull Front Face—Only the back side is visible.
    4 Cull Both Faces—Neither the front nor the back side are visible.

   •      Frontface Mode —

    Frontface Mode specifies the winding order of an object. Face Culling Mode interprets this input
    to determine the visibility of the object's polygons.

    0 Inherit Value—Inherits the mode of the parent object.
    1 Counterclockwise—The object faces the front.
    2 Clockwise—The object faces the back.

   •      Scene Object In —

    Scene Object In specifies a reference to the scene you want to manipulate.

   •     Mode —

   Mode specifies the method you use to draw the 3D object.

    0 Inherit Value (default)—Inherits the draw style of a parent object.
    1 Points—Draws the object by placing points at the vertices of the object.
     Wireframe—Draws the object with line segments that connect at the vertices to form a
    2
     bounded geometry.


                                                    © National Instruments 2311

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2311 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2312 ordinal=2312 -->
## Functions

Functions


           3 Polygon—Draws the object with a fully bounded and filled geometry.

               •       Size —

             Size specifies the size of the points you use to draw the geometry. Set the value to -1 to inherit
            the point size of a parent object. The default is -1.

               •       error in (no error) —

             error in describes error conditions that occur before this node runs. This input provides
            standard error in functionality.

               •      Scene Object Out —

           Scene Object Out returns a reference to the scene object.

               •       error out —

             error out contains error information. This output provides standard error out functionality.

    SetSet BlendingBlending

      Blends fragment color outputs with destination colors for texturing 3D objects.


      Inputs/Outputs

               •      Scene Object In —

           Scene Object In specifies a reference to the scene you want to manipulate.

               •     Mode —

         Mode specifies how the color values you apply to a 3D object blend.


2312   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2312 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2313 ordinal=2313 -->
## Functions

Functions


  0 Inherit Value (default)—The object inherits the blending mode of a parent object.
  1 On—Enables blending.
  2 Off—Disables blending.

•      Bin —

  Bin specifies the draw bin in which you drop and store objects. The bin of an object affects the
  order in which the object appears when you render the scene.

  0 Normal Bin (default)—Stores objects without a specific sorting pattern.
   Opaque Bin—Sorts objects in the scene from front to back relative to the viewer to ensure that  1    objects closer to the camera render first.
   Transparent Bin—Sorts objects in the scene from back to front relative to the viewer to ensure
  2
    that transparent or translucent objects correctly blend with objects that appear behind them.

•       error in (no error) —

  error in describes error conditions that occur before this node runs. This input provides
  standard error in functionality.

•      Destination —

  Destination specifies the blend factor you apply to the color values of the currently stored pixels.

  The following source and destination color components are described as (Rs, Gs, Bs, As) for
  source components and (Rd, Gd, Bd, Ad) for destination components. The components have
  integer values between 0 and (kR, kG, kB, kA), where kR=2mR 1, kG=2mG 1, kB=2mB 1, and
  kA=2mA 1. (mR, mG, mB, mA) is the number of bitplanes for each red, green, blue, and alpha
  value.

  0 Zero (default)—(0, 0, 0, 0)
  1 One—(1, 1, 1, 1)
  2 Source Color—(RS/kR, Gs/kG, Bs/kB, As/kA)
  3 One Minus Source Color—(1, 1, 1, 1)-(RS/kR, Gs/kG, Bs/kB, As/kA)
  4 Source Alpha—(As/kA, As/kA, As/kA, As/kA)
  5 One Minus Source Alpha—(1, 1, 1, 1)-(As/kA, As/kA, As/kA, As/kA)
  6 Destination Alpha—(Ad/kA, Ad/kA, Ad/kA, Ad/kA)
  7 One Minus Destination Alpha—(1, 1, 1, 1)-(Ad/kA,Ad/kA, Ad/kA, Ad/kA)

•      Source —


                                                   © National Instruments 2313

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2313 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2314 ordinal=2314 -->
## Functions

Functions


           Source specifies the blend factor you apply to the color values of the incoming fragment.

          The following source and destination color components are described as (Rs, Gs, Bs, As) for
            source components and (Rd, Gd, Bd, Ad) for destination components. The components have
             integer values between 0 and (kR, kG, kB, kA), where kR=2mR 1, kG=2mG 1, kB=2mB 1, and
          kA=2mA 1. (mR, mG, mB, mA) is the number of bitplanes for each red, green, blue, and alpha
             value.

           0 Zero (default)—(0, 0, 0, 0)
           1 One—(1, 1, 1, 1)
           2 Destination Color—(Rd/kR, Gd/kG, Bd/kB, Ad/kA)
           3 One Minus Destination Color—(1, 1, 1, 1)-(Rd/kR, Gd/kG, Bd/kB, Ad/kA)
           4 Source Alpha—(As/kA, As/kA, As/kA, As/kA)
           5 One Minus Source Alpha—(1, 1, 1, 1)-(As/kA, As/kA, As/kA, As/kA)
           6 Destination Alpha—(Ad/kA, Ad/kA, Ad/kA, Ad/kA)
           7 One Minus Destination Alpha—(1, 1, 1, 1)-(Ad/kA, Ad/kA, Ad/kA, Ad/kA)
           8 Source Alpha Saturate—(i, i, i, 1) where i=min (As, kA, Ad)/kA

               •      Scene Object Out —

           Scene Object Out returns a reference to the scene object.

               •       error out —

             error out contains error information. This output provides standard error out functionality.


      TransformationsTransformations

      Use the Transformations VIs to apply common transformations, such as rotation,
        translation, and scaling, to objects in a 3D scene graph.

           Note LabVIEW transforms objects about their center of mass. A cone's center
               of mass is one-fourth of the way from the center of the base to the vertex, not
               equidistant between the highest and lowest point.


2314   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2314 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2315 ordinal=2315 -->
## Functions

Functions


Palette Object  Description

Rotate X-axis    Rotates an object about the X-axis.

Rotate Y-axis    Rotates an object about the Y-axis.

Rotate Z-axis    Rotates an object about the Z-axis.

Get Rotation    Returns the rotation applied to an object in a 3D scene in axis-angle form.


                 Clears any rotations previously applied to an object in a 3D scene and rotates the
Set Rotation     object by the values Axis and Angle. This VI performs an absolute rotation from
                the object's initial position.


                Rotates an object in a 3D scene by the values Axis and Angle. This VI performs aRotate Object
                  relative rotation from the object's current position.


Get Translation  Returns the translation applied to an object in a 3D scene.


                 Clears any translations previously applied to an object in a 3D scene and
Set Translation  translates the object by the vector you specify. This VI performs an absolute
                 translation from the object's initial position.


Translate        Translates an object in a 3D scene by the vector you specify. This VI performs a
Object           relative translation from the object's current position.


Get Scale       Returns the scale factors applied to an object in a 3D scene.


                 Clears any previous scale operation applied to an object in a 3D scene and applies
Set Scale       the scaling factors you specify. This VI performs an absolute scale from the
                 object's initial position.


                                                    © National Instruments 2315

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2315 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2316 ordinal=2316 -->
## Functions

Functions


         Palette Object  Description

                        Uniformly scales an object in a 3D scene by the factors you specify. This VI
         Scale Object                       performs a relative scale from the object's current position.


         Clear            Clears any transformations previously applied to an object in a 3D scene by
         Transformation modifying the identity matrices that describe the transformations.

    RotateRotate X-axisX-axis

       Rotates an object about the X-axis.


      Inputs/Outputs

               •       Relative? —

             Relative? specifies whether the rotation is relative to the axis. The default is FALSE.

               •      Scene Object In —

           Scene Object In specifies a reference to the scene you want to manipulate.

               •      angle —

            angle specifies the angle of rotation. The default is 0.

               •       error in (no error) —

             error in describes error conditions that occur before this node runs. This input provides
            standard error in functionality.

               •      angle unit —


2316   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2316 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2317 ordinal=2317 -->
## Functions

Functions


    angle unit specifies the units of rotation in degrees or radians. The default is degrees.

   •      Scene Object Out —

    Scene Object Out returns a reference to the scene object.

   •       error out —

    error out contains error information. This output provides standard error out functionality.

RotateRotate Y-axisY-axis

Rotates an object about the Y-axis.


Inputs/Outputs

   •       Relative? —

    Relative? specifies whether the rotation is relative to the axis. The default is FALSE.

   •      Scene Object In —

    Scene Object In specifies a reference to the scene you want to manipulate.

   •      angle —

    angle specifies the angle of rotation. The default is 0.

   •       error in (no error) —

    error in describes error conditions that occur before this node runs. This input provides
    standard error in functionality.

   •      angle unit —


                                                    © National Instruments 2317

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2317 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2318 ordinal=2318 -->
## Functions

Functions


            angle unit specifies the units of rotation in degrees or radians. The default is degrees.

               •      Scene Object Out —

           Scene Object Out returns a reference to the scene object.

               •       error out —

             error out contains error information. This output provides standard error out functionality.

    RotateRotate Z-axisZ-axis

       Rotates an object about the Z-axis.


      Inputs/Outputs

               •       Relative? —

             Relative? specifies whether the rotation is relative to the axis. The default is FALSE.

               •      Scene Object In —

           Scene Object In specifies a reference to the scene you want to manipulate.

               •      angle —

            angle specifies the angle of rotation. The default is 0.

               •       error in (no error) —

             error in describes error conditions that occur before this node runs. This input provides
            standard error in functionality.

               •      angle unit —


2318   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2318 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2319 ordinal=2319 -->
## Functions

Functions


    angle unit specifies the units of rotation in degrees or radians. The default is degrees.

   •      Scene Object Out —

    Scene Object Out returns a reference to the scene object.

   •       error out —

    error out contains error information. This output provides standard error out functionality.

GetGet RotationRotation

Returns the rotation applied to an object in a 3D scene in axis-angle form.


Inputs/Outputs

   •      Scene Object —

    Scene Object returns the Scene Object input.

   •       error in (no error) —

    error in describes error conditions that occur before this node runs. This input provides
    standard error in functionality.

   •      Scene Object —

    Scene Object is the reference to the object whose rotation you want to get.

   •       Axis —

    Axis returns the x, y, and z coordinates that define the axis around which the rotation occurs.

         •     X —


                                                    © National Instruments 2319

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2319 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2320 ordinal=2320 -->
## Functions

Functions


              X indicates the x coordinate.

                     •      Y —

               Y indicates the y coordinate.

                     •     Z —

              Z indicates the z coordinate.


               •      Angle —

           Angle returns the angle of the rotation around the axis.

               •       error out —

             error out contains error information. This output provides standard error out functionality.

    SetSet RotationRotation

       Clears any rotations previously applied to an object in a 3D scene and rotates the
       object by the values Axis and Angle. This VI performs an absolute rotation from the
       object's initial position.


      Inputs/Outputs

               •      Scene Object —

           Scene Object is the reference to the object you want to rotate.

               •       Axis —


2320   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2320 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2321 ordinal=2321 -->
## Functions

Functions


    Axis specifies the x, y, and z coordinates that define the axis around which the rotation occurs.

         •     X —

       X specifies the x coordinate.

         •      Y —

        Y specifies the y coordinate.

         •     Z —

       Z specifies the z coordinate.


   •      Angle —

    Angle specifies the angle in radians around the Axis by which the rotation occurs.

   •       error in (no error) —

    error in describes error conditions that occur before this node runs. This input provides
    standard error in functionality.

   •      Rotated Scene Object —

    Rotated Scene Object is the reference to the rotated 3D object.

   •       error out —

    error out contains error information. This output provides standard error out functionality.

RotateRotate ObjectObject

Rotates an object in a 3D scene by the values Axis and Angle. This VI performs a
relative rotation from the object's current position.


                                                    © National Instruments 2321

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2321 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2322 ordinal=2322 -->
## Functions

Functions


      Inputs/Outputs

               •      Scene.Object In —

            Scene.Object In is the reference to the 3D object you want to rotate.

               •       Axis —

             Axis specifies the x, y, and z coordinates that define the axis around which the rotation occurs.

                     •     X —

              X specifies the x coordinate.

                     •      Y —

               Y specifies the y coordinate.

                     •     Z —

              Z specifies the z coordinate.


               •      Angle —

           Angle specifies the angle in radians around the Axis by which the rotation occurs.

               •       error in (no error) —

             error in describes error conditions that occur before this node runs. This input provides
            standard error in functionality.

               •      Scene.Object Out —

            Scene.Object Out returns the reference to the rotated 3D object.

               •       error out —

             error out contains error information. This output provides standard error out functionality.


2322   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2322 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2323 ordinal=2323 -->
## Functions

Functions

Examples

Refer to the following example files included with LabVIEW.

  • labview\examples\Graphics and Sound\3D Picture Control\3D
   Model of Solar System.vi
  • labview\examples\Graphics and Sound\3D Picture Control\
   Order of Transformations.vi
GetGet TranslationTranslation

Returns the translation applied to an object in a 3D scene.


Inputs/Outputs

   •      Scene Object —

    Scene Object is the reference to the object whose translation you want to get.

   •       error in (no error) —

    error in describes error conditions that occur before this node runs. This input provides
    standard error in functionality.

   •      Scene Object —

    Scene Object returns the Scene Object input.

   •      Transformation:Get Translation —

    Transformation:Get Translation returns the x, y, and z factors that define the translation applied
    to the Scene Object.

         •     X —


                                                    © National Instruments 2323

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2323 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2324 ordinal=2324 -->
## Functions

Functions


              X indicates the x factor.

                     •      Y —

               Y indicates the y factor.

                     •     Z —

              Z indicates the z factor.


               •       error out —

             error out contains error information. This output provides standard error out functionality.

    SetSet TranslationTranslation

       Clears any translations previously applied to an object in a 3D scene and translates the
       object by the vector you specify. This VI performs an absolute translation from the
       object's initial position.

      Use the Translate Object VI to translate an object from the object's current position.


      Inputs/Outputs

               •      Scene Object —

           Scene Object is the reference to the object you want to translate.

               •      Translation —

            Translation contains the x, y, and z coordinates that define the vector you want to use in the
              translation.


2324   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2324 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2325 ordinal=2325 -->
## Functions

Functions


         •     X —

       X specifies the x coordinate.

         •      Y —

        Y specifies the y coordinate.

         •     Z —

       Z specifies the z coordinate.


   •       error in (no error) —

    error in describes error conditions that occur before this node runs. This input provides
    standard error in functionality.

   •      Translated Object —

    Translated Object is the reference to the translated 3D object.

   •       error out —

    error out contains error information. This output provides standard error out functionality.

TranslateTranslate ObjectObject

Translates an object in a 3D scene by the vector you specify. This VI performs a relative
translation from the object's current position.

Use the Set Translation VI to translate an object from the object's initial position.


Inputs/Outputs

   •      Scene.Object In —

                                                    © National Instruments 2325

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2325 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2326 ordinal=2326 -->
## Functions

Functions


            Scene.Object In is the reference to the 3D object you want to translate.

               •      Translation —

            Translation contains the x, y, and z coordinates that define the vector you want to use in the
              translation.

                     •     X —

              X specifies the x coordinate.

                     •      Y —

               Y specifies the y coordinate.

                     •     Z —

              Z specifies the z coordinate.


               •       error in (no error) —

             error in describes error conditions that occur before this node runs. This input provides
            standard error in functionality.

               •      Scene.Object Out —

            Scene.Object Out returns the reference to the translated 3D object.

               •       error out —

             error out contains error information. This output provides standard error out functionality.


     Examples

       Refer to the following example files included with LabVIEW.

            • labview\examples\Graphics and Sound\3D Picture Control\3D
        Model of Solar System.vi
            • labview\examples\Graphics and Sound\3D Picture Control\
        Order of Transformations.vi

2326   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2326 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2327 ordinal=2327 -->
## Functions

Functions

GetGet ScaleScale

Returns the scale factors applied to an object in a 3D scene.


Inputs/Outputs

   •      Scene Object —

    Scene Object returns the Scene Object input.

   •       error in (no error) —

    error in describes error conditions that occur before this node runs. This input provides
    standard error in functionality.

   •      Scene Object —

    Scene Object is the reference to the object whose scale you want to get.

   •      Transformation:Get Scale —

    Transformation:Get Scale returns the x, y, and z factors that define the scale of the Scene
    Object.

         •     X —

       X indicates the x factor.

         •      Y —

        Y indicates the y factor.

         •     Z —

       Z indicates the z factor.


   •       error out —


                                                    © National Instruments 2327

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2327 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2328 ordinal=2328 -->
## Functions

Functions


             error out contains error information. This output provides standard error out functionality.

    SetSet ScaleScale

       Clears any previous scale operation applied to an object in a 3D scene and applies the
       scaling factors you specify. This VI performs an absolute scale from the object's initial
       position.


      Inputs/Outputs

               •      Scene Object —

           Scene Object is the reference to the object to which you want to apply a scale.

               •      Scale —

            Scale specifies the x, y, and z factors that define the scale of the 3D object.

                     •     X —

              X indicates the x factor.

                     •      Y —

               Y indicates the y factor.

                     •     Z —

              Z indicates the z factor.


               •       error in (no error) —

             error in describes error conditions that occur before this node runs. This input provides
            standard error in functionality.


2328   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2328 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2329 ordinal=2329 -->
## Functions

Functions

   •      Scaled Object —

    Scaled Object is the reference to the scaled 3D object.

   •       error out —

    error out contains error information. This output provides standard error out functionality.

ScaleScale ObjectObject

Uniformly scales an object in a 3D scene by the factors you specify. This VI performs a
relative scale from the object's current position.


Inputs/Outputs

   •      Scene.Object In —

    Scene.Object In is the reference to the 3D object you want to uniformly scale.

   •      Scale —

    Scale specifies the x, y, and z factors that define the scale of the 3D object.

         •     X —

       X indicates the x factor.

         •      Y —

        Y indicates the y factor.

         •     Z —

       Z indicates the z factor.


   •       error in (no error) —

                                                    © National Instruments 2329

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2329 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2330 ordinal=2330 -->
## Functions

Functions


             error in describes error conditions that occur before this node runs. This input provides
            standard error in functionality.

               •      Scene.Object Out —

            Scene.Object Out returns the reference to the scaled 3D object.

               •       error out —

             error out contains error information. This output provides standard error out functionality.

    ClearClear TransformationTransformation

       Clears any transformations previously applied to an object in a 3D scene by modifying
       the identity matrices that describe the transformations.


      Inputs/Outputs

               •      Object Refnum In —

            Object Refnum In is the reference to the object with transformations applied.

               •       error in (no error) —

             error in describes error conditions that occur before this node runs. This input provides
            standard error in functionality.

               •      Object Refnum Out —

            Object Refnum Out is the reference to the object with transformations cleared.

               •       error out —

             error out contains error information. This output provides standard error out functionality.


2330   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2330 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2331 ordinal=2331 -->
## Functions

Functions

Examples

Refer to the following example files included with LabVIEW.

  • labview\examples\Graphics and Sound\3D Picture Control\3D
   Model of Solar System.vi
  • labview\examples\Graphics and Sound\3D Picture Control\
   Order of Transformations.vi

FileFile LoadingLoading

Use the File Loading VIs to load geometries of various model types in a 3D scene graph.


 Palette            Description
 Object

          Loads a three-dimensional object model saved in Virtual Reality Modeling Language
 Load           (VRML) format to display in a 3D scene. VRML files commonly appear with a .wrl file VRML File
            extension.


 Load ASE  Loads a three-dimensional object model saved in 3D Studio ASCII Exchange (ASE)
 Geometry format to display in a 3D scene.


 Load STL  Loads a three-dimensional object model saved in ASCII stereolithography (STL) format
 Geometry  to display in a 3D scene.

LoadLoad VRMLVRML FileFile

Loads a three-dimensional object model saved in Virtual Reality Modeling Language
(VRML) format to display in a 3D scene. VRML files commonly appear with a .wrl file
extension.

                                                    © National Instruments 2331

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2331 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2332 ordinal=2332 -->
## Functions

Functions


      Inputs/Outputs

               •      Path —

           Path is the path to the WRL or VRML file.

               •       error in —

             error out contains error information. This output provides standard error out functionality.

               •      Scene:Read Scene File —

           Scene:Read Scene File returns the reference to the loaded file.

               •       error out —

             error out contains error information. This output provides standard error out functionality.

   LoadLoad ASEASE GeometryGeometry

      Loads a three-dimensional object model saved in 3D Studio ASCII Exchange (ASE)
       format to display in a 3D scene.


      Inputs/Outputs

               •     Model File —

          Model File is the path to the model file.

               •       error in (no error) —

             error in describes error conditions that occur before this node runs. This input provides


2332   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2332 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2333 ordinal=2333 -->
## Functions

Functions


    standard error in functionality.

   •     New Mesh Refnum —

   New Mesh Refnum returns the reference to the loaded geometry.

   •       error out —

    error out contains error information. This output provides standard error out functionality.

LoadLoad STLSTL GeometryGeometry

Loads a three-dimensional object model saved in ASCII stereolithography (STL) format
to display in a 3D scene.


Inputs/Outputs

   •     Model File —

    Model File is the path to the model file.

   •       error in (no error) —

    error in describes error conditions that occur before this node runs. This input provides
    standard error in functionality.

   •     New Mesh Refnum —

   New Mesh Refnum returns the reference to the loaded geometry.

   •       error out —

    error out contains error information. This output provides standard error out functionality.


                                                    © National Instruments 2333

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2333 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2334 ordinal=2334 -->
## Functions

Functions

      HelpersHelpers

      Use the Helpers VIs to perform some common tasks in setting up a 3D scene.


         Palette                    Description        Object

         Color      Converts an RGB color and an alpha into an RGBA cluster that you can apply to a 3D
       Change     object.


        Setup                    Creates a new window with hardware acceleration for rendering the 3D scene.
       Window


                Maps real-world data onto a 3D model.
        Sensor
        Mapping   Use the Sensor Mapping Express VI to wire an array of data values to represent sensors
                 you configure using the dialog box options below.


         Create                    Defines a plane in the 3D scene beyond which objects cannot be drawn.          Clip Plane


      New Light  Creates a new light source for the 3D scene.


                    Creates a new texture from an image and applies the texture to the surface of an object
         Texture
                       in the 3D scene.

         Set Clip
                    Defines the plane beyond which LabVIEW clips, or does not render, surfaces in a scene.
        Plane

         Set Light   Creates and positions a light source in 3D space relative to a 3D object.

        Apply
                Maps a texture to the surface of a 3D object. You must manually select the polymorphic
         Texture


2334   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2334 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2335 ordinal=2335 -->
## Functions

Functions


 Palette            Description
 Object

            instance to use.

ColorColor ChangeChange

Converts an RGB color and an alpha into an RGBA cluster that you can apply to a 3D
object.


Inputs/Outputs

   •      Color —

    Color is the color that you want to convert to its respective red, green, and blue components.

   •      Alpha —

    Alpha specifies the level of opacity of the RGB color when the color is applied to the 3D object.
    Alpha must be a value between 0 and 1, where 0 is transparent and 1 is opaque. The default is
     1.

          Note If you want the returned color to be transparent when you apply it to a
             SceneObject, you must enable blending on the SceneObject and set the Blending:Bin
             property to Transparent Bin.

   •     RGBA —

   RGBA is the input color converted to the RGBA format.

         •     R —

      R indicates the red value.


                                                    © National Instruments 2335

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2335 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2336 ordinal=2336 -->
## Functions

Functions


                     •     G —

            G indicates the green value.

                     •     B —

            B indicates the blue value.

                     •     A —

             A indicates the Alpha value.

   SetupSetup WindowWindow

       Creates a new window with hardware acceleration for rendering the 3D scene.


      Inputs/Outputs

               •     Window State —

         Window State specifies the state of the new window.

           0 Open (default)—The new window is open but is not maximized, minimized, or hidden.
           1 Minimized—The new window is minimized.
           2 Maximized—The new window is maximized.
           Hidden—The new window is floating but is not visible because LabVIEW is not the active
           3
               application.

               •     Camera Controller —

          Camera Controller sets the interaction of the camera with the 3D scene.


2336   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2336 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2337 ordinal=2337 -->
## Functions

Functions


    0 None (default)—The camera does not interact with the scene.
    1 Spherical—The camera rotates and moves as if pinned to a sphere.
    2 Flying—The camera flies through the scene freely.

   •       error in (no error) —

    error in describes error conditions that occur before this node runs. This input provides
    standard error in functionality.

   •     New Window Refnum —

   New Window Refnum is the reference to the window.

   •       error out —

    error out contains error information. This output provides standard error out functionality.


Examples

Refer to the following example files included with LabVIEW.

  • labview\examples\Graphics and Sound\3D Picture Control\3D
   Model of Solar System.vi
SensorSensor MappingMapping

Maps real-world data onto a 3D model.

Use the Sensor Mapping Express VI to wire an array of data values to represent sensors
you configure using the dialog box options below.


                                                    © National Instruments 2337

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2337 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2338 ordinal=2338 -->
## Functions

Functions

      Dialog Box Options

        Option    Description

                    Displays a file dialog box you can use to navigate to a file of a 3D model you create using
                 a CAD program. LabVIEW supports the following file formats for three-dimensional
                    object models:

       Load           •  Virtual Reality Modeling Language (VRML)
       Model          •  Stereolithography (STL)

                     Note VRML files commonly appear with a .wrl file extension.


       Model                     Specifies the path to the 3D model you want to load.
        Path


                    Displays the 3D model. Right-click the 3D model on the sensor canvas to place free        Sensor                    sensors. You can configure sensors to represent NI-DAQmx channels or create free
        Canvas                   sensors to represent data you wire to the Express VI.

                  Determines how LabVIEW draws the 3D model. Use this option to ensure accurate
                 placement of the sensors. Select from the following options:

                               • Points—Draws the model by placing points at the vertices of the object.
                               • Wireframe+Polygons—Draws the model with line segments that connect at the       Draw                          vertices to form a bounded geometry on top of the fully bounded and filled         Style
                      geometric 3D model.
                               • Wireframe—Draws the model with line segments that connect at the vertices to
                     form a bounded geometry.
                               • Polygons—Draws the model with a fully bounded and filled geometry.


        Sensor    Determines the size of the sensors you place on the 3D model. Use this option to ensure
         Size       accurate placement of the sensors.


      DAQmx
                       Lists all NI-DAQmx tasks you create and save. Selecting a NI-DAQmx task from the pull-
        Task
               down menu populates the Channels List with the channels for the task.
      Name


2338   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2338 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2339 ordinal=2339 -->
## Functions

Functions


 Option    Description

               Note The DAQmx Task Name option does not appear unless you install NI-
                DAQmx. Refer to the DAQGettingStartedGuidefor more information
                  about installing NI-DAQmx. Refer to the NI-DAQmxHelpfor more
                    information about using NI-DAQmx channels.


             Lists DAQ channels and free sensors. Select a DAQmx task from the pull-down menu.
 Channels LabVIEW populates the Channels List with the channels for the DAQmx task. Drag and
 List      drop DAQmx task channels from the list to place sensors on the 3D model. You also can
             right-click the 3D model to place free sensors on the model.


         Removes a sensor from the 3D model. Select a sensor in the Channels List and click the Delete           Delete Sensor button to remove the sensor from the list. Deleting a sensor from the 3D
 Sensor         model does not delete the channel from the DAQmx task.


           Configures the minimum and maximum value ranges for the incoming data. For
           example, if you change the color ramp minimum to 100 and the maximum to 200, the
           data values should range from 100–200. After you set the value range, click the top and
 Color     bottom out-of-range colors to configure the colors to indicate if a value is outside of the
 Ramp     value range you set.

             Right-click the Color Ramp control and use the shortcut menu items to customize the
           appearance, size, colors, and number of colors.


Inputs/Outputs

   •      Sensor Values —

    Contains the sensor values. Wire a 1D array of double-precision, floating-point numbers whose
    positions correspond to the order you configure the sensors in the Configure Sensors dialog
    box.

   •       error in (no error) —

    Describes error conditions that occur before this node runs.


                                                    © National Instruments 2339

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2339 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2340 ordinal=2340 -->
## Functions

Functions

               •       error out —

            Contains error information. This output provides standard error out functionality.

               •      Scene Ref Out —

            Returns a reference to a 3D scene object. Wire this output to the 3D picture control to add a 3D
             picture control to the front panel window and view the 3D model.


       Configuring the Draw Style or Sensor Size options in the Configure Sensors dialog box
      does not affect the appearance of the 3D model in the front panel window when the VI
       runs. The sensors do not appear on the 3D model when the VI runs.

     Components

       error out passes error or warning information out of a VI to be used by other VIs. Right-
        click the error out indicator on the front panel and select Explain Error or Explain
      Warning from the shortcut menu for more information about the error.

      source string describes the origin of the error or warning. Right-click the error out
       indicator on the front panel and select Explain Error or Explain Warning from the
       shortcut menu for more information about the error.

      code is the error or warning code. Right-click the error out indicator on the front panel
      and select Explain Error or Explain Warning from the shortcut menu for more
       information about the error.

       status is TRUE (X) if an error occurred or FALSE (checkmark) to indicate a warning or
       that no error occurred. Right-click the error out indicator on the front panel and select
       Explain Error or Explain Warning from the shortcut menu for more information about
       the error.

       Configures the minimum and maximum value ranges for the incoming data. For
      example, if you change the color ramp minimum to 100 and the maximum to 200, the
       data values should range from 100–200. After you set the value range, click the top and
      bottom out-of-range colors to configure the colors to indicate if a value is outside of
       the value range you set.


2340   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2340 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2341 ordinal=2341 -->
## Functions

Functions

Right-click the Color Ramp control and use the shortcut menu items to customize the
appearance, size, colors, and number of colors.

Specifies the path to the 3D model you want to load.

Determines how LabVIEW draws the 3D model. Use this option to ensure accurate
placement of the sensors. Select from the following options:

  • Points—Draws the model by placing points at the vertices of the object.
  • Wireframe+Polygons—Draws the model with line segments that connect at the
    vertices to form a bounded geometry on top of the fully bounded and filled
   geometric 3D model.
  • Wireframe—Draws the model with line segments that connect at the vertices to
   form a bounded geometry.
  • Polygons—Draws the model with a fully bounded and filled geometry.

Removes a sensor from the 3D model. Select a sensor in the Channels List and click
the Delete Sensor button to remove the sensor from the list. Deleting a sensor from
the 3D model does not delete the channel from the DAQmx task.

Determines the size of the sensors you place on the 3D model. Use this option to
ensure accurate placement of the sensors.

Lists all NI-DAQmx tasks you create and save. Selecting a NI-DAQmx task from the pull-
down menu populates the Channels List with the channels for the task.

Lists DAQ channels and free sensors. Select a DAQmx task from the pull-down menu.
LabVIEW populates the Channels List with the channels for the DAQmx task. Drag and
drop DAQmx task channels from the list to place sensors on the 3D model. You also can
right-click the 3D model to place free sensors on the model.

Determines how LabVIEW draws the 3D model. Use this option to ensure accurate
placement of the sensors. Select from the following options: Points--Draws the model
by placing points at the vertices of the object. Wireframe+Polygons--Draws the model
with line segments that connect at the vertices to form a bounded geometry on top of
the fully bounded and filled geometric 3D model. Wireframe--Draws the model with
line segments that connect at the vertices to form a bounded geometry. Polygons--
Draws the model with a fully bounded and filled geometry.


                                                    © National Instruments 2341

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2341 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2342 ordinal=2342 -->
## Functions

Functions

      Determines the size of the sensors you place on the 3D model. Use this option to
      ensure accurate placement of the sensors.

        Lists all NI-DAQmx tasks you create and save. Selecting a NI-DAQmx task from the pull-
     down menu populates the Channels List with the channels for the task.

       Displays a file dialog box you can use to navigate to a file of a 3D model you create
       using a CAD program. LabVIEW supports the following file formats for three-
      dimensional object models:

            • Virtual Reality Modeling Language (VRML)
            • Stereolithography (STL)

       Displays the 3D model. Right-click the 3D model on the sensor canvas to place free
       sensors. You can configure sensors to represent NI-DAQmx channels or create free
       sensors to represent data you wire to the Express VI.
    CreateCreate ClipClip PlanePlane

       Defines a plane in the 3D scene beyond which objects cannot be drawn.


      Inputs/Outputs

               •      Plane —

           Plane is a cluster consisting of the four coefficients of the plane equation.

                     •     A —

             A specifies the Acoefficient of the plane equation.

                     •     B —


2342   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2342 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2343 ordinal=2343 -->
## Functions

Functions


      B specifies the Bcoefficient of the plane equation.

         •     C —

       C specifies the Ccoefficient of the plane equation.

         •     D —

      D specifies the Dcoefficient of the plane equation.


   •     Number —

   Number is the integer used to identify the plane. Number must be a value between 0 and 5,
     inclusive.

   •       error in (no error) —

    error in describes error conditions that occur before this node runs. This input provides
    standard error in functionality.

   •     New Clip Plane Refnum —

   New Clip Plane Refnum is the reference to the clip plane.

   •       error out —

    error out contains error information. This output provides standard error out functionality.


The coordinates of points in a clip plane are determined by the following equation:

Ax+By+Cz+D = 0

LabVIEW determines the side of the plane on which objects appear based on the
orientation of the plane. A plane defined by the constants 1, 1, 1, and 0 is opposite in
orientation to a plane defined by the constants –1, –1, –1, and 0.


                                                    © National Instruments 2343

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2343 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2344 ordinal=2344 -->
## Functions

Functions

   NewNew LightLight

       Creates a new light source for the 3D scene.


      Inputs/Outputs

               •      At Infinity —

            At Infinity specifies whether the light source is at an infinite distance from the scene. When At
              Infinity is TRUE, all light strikes the scene in parallel. The default is FALSE.

               •       Light Number —

            Light Number is the index, or integer used to identify the light. Light Number must be a value
           between 0 and 7, inclusive. You cannot index more than 8 lights in a 3D scene.

               •       error in (no error) —

             error in describes error conditions that occur before this node runs. This input provides
            standard error in functionality.

               •     New Light Refnum —

         New Light Refnum is the reference to the light.

               •       error out —

             error out contains error information. This output provides standard error out functionality.


     Examples

       Refer to the following example files included with LabVIEW.

            • labview\examples\Controls and Indicators\Graphs and
        Charts\Math Plots - 3D (ActiveX)\3D Curve Graph
        (ActiveX).vi

2344   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2344 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2345 ordinal=2345 -->
## Functions

Functions

TextureTexture

Creates a new texture from an image and applies the texture to the surface of an object
in the 3D scene.


Inputs/Outputs

   •     Image —

    Image describes the image you want to draw or manipulate.

         •     image type —

       image type is reserved for future use.

         •     image depth —

       image depth specifies the color depth of the image, which is the number of bits to use to
         describe the color of each pixel in the image. Valid values include 1, 4, 8, and 24 bits per
          pixel.

       image depth affects how LabVIEW interprets the values of image and colors.

         •     image —

       image is an array of bytes that describes the color of each pixel in the image in raster order.
       The value of image depth determines how LabVIEW interprets the value of this input.

              If image depth is 24, each pixel has three bytes to describe its color. The first byte for each
          pixel describes the red value, the second byte describes the green value, and the third byte
         describes the blue value.

              If image depth is 8, each pixel has one byte to describe its color. The value of each byte
        corresponds to an element in colors, which stores 32-bit RGB values where the most-
          significant byte is zero, followed in order by red, green, and blue values. Valid values include
        0 through 255.


                                                    © National Instruments 2345

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2345 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2346 ordinal=2346 -->
## Functions

Functions


                           If image depth is 4, the behavior is similar to when image depth is 8 except valid values in
              image include 0 through 15.

                           If image depth is 1, any value of zero in image corresponds to element 0 in colors. All other
                 values correspond to element 1 in colors.

                     •     mask —

             mask is an array of bytes in which each bit describes mask information for a pixel. The first
                byte describes the first eight pixels, the second byte describes the next eight pixels, and so
                 on.

                           If a bit is zero, LabVIEW draws the corresponding pixel as transparent. If the array is empty,
              LabVIEW draws all pixels without transparency. If the array does not contain a bit for each
                   pixel in the image, LabVIEW draws any pixels missing from the array without transparency.

                     •       colors —

                 colors is an array of RGB color values that correspond to the values in image. The value of
              image depth determines how LabVIEW interprets the value of this input. colors stores 32-bit
            RGB values where the most-significant byte is zero, followed in order by red, green, and blue
                  values. Valid values include 0 through 255.

                           If image depth is 24, LabVIEW ignores this input.

                           If image depth is 8, the array can have 256 elements.

                           If image depth is 4, the array can have 16 elements.

                           If image depth is 1, the array can have 2 elements.

                     •      Rectangle —

                Rectangle is a cluster that contains coordinates that describe the bounding rectangle in
               which you want to draw the image.

              The VI clips the image to the width and height of the rectangle. The bottom and right edges
                  of the rectangle bounds do not contain image pixels. Horizontal coordinates increase to the
                    right, and vertical coordinates increase to the bottom.

                           •        left —


2346   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2346 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2347 ordinal=2347 -->
## Functions

Functions


                left is the horizontal coordinate of the left edge of the rectangle.

                •      top —

            top is the vertical coordinate of the top edge of the rectangle.

                •       right —

              right is the horizontal coordinate of the right edge of the rectangle.

                •     bottom —

           bottom is the vertical coordinate of the bottom edge of the rectangle.


   •       error in (no error) —

    error in describes error conditions that occur before this node runs. This input provides
    standard error in functionality.

   •     New Texture Refnum —

   New Texture Refnum is the reference to the texture.

   •       error out —

    error out contains error information. This output provides standard error out functionality.


Examples

Refer to the following example files included with LabVIEW.

  • labview\examples\Graphics and Sound\3D Picture Control\3D
   Model of Solar System.vi
  • labview\examples\Graphics and Sound\3D Picture Control\
   Using Meshes.vi


                                                    © National Instruments 2347

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2347 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2348 ordinal=2348 -->
## Functions

Functions

    SetSet ClipClip PlanePlane

       Defines the plane beyond which LabVIEW clips, or does not render, surfaces in a scene.


            • Set Clip Plane (no reference) VI
            • Set Clip Plane (reference) VI
    SetSet ClipClip PlanePlane (no(no reference)reference) VIVI

       Defines the plane beyond which LabVIEW clips, or does not render, surfaces in a scene.


      Inputs/Outputs

               •      Scene Object In —

           Scene Object In specifies a reference to the scene you want to manipulate.

               •       Clip Plane Refnum In —

             Clip Plane Refnum In specifies a reference to the clip plane.

               •       Clip Plane State —

             Clip Plane State specifies whether to enable the clip plane state.

           0 Inherit Value (default)—The clip plane inherits the clip plane state of a parent object.
           1 Off—Disables the clip plane so it does not apply to the object.
           2 On—Enables the clip plane.

               •       error in (no error) —


2348   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2348 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2349 ordinal=2349 -->
## Functions

Functions


    error in describes error conditions that occur before this node runs. This input provides
    standard error in functionality.

   •      Scene Object Out —

    Scene Object Out returns a reference to the scene object.

   •       error out —

    error out contains error information. This output provides standard error out functionality.

SetSet ClipClip PlanePlane (reference)(reference) VIVI


Inputs/Outputs

   •      Scene Object In —

    Scene Object In specifies a reference to the scene you want to manipulate.

   •       Clip Plane Refnum In —

     Clip Plane Refnum In specifies a reference to the clip plane.

   •       Clip Plane State —

     Clip Plane State specifies whether to enable the clip plane state.

    0 Inherit Value (default)—The clip plane inherits the clip plane state of a parent object.
    1 Off—Disables the clip plane so it does not apply to the object.
    2 On—Enables the clip plane.

   •       error in (no error) —

    error in describes error conditions that occur before this node runs. This input provides


                                                    © National Instruments 2349

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2349 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2350 ordinal=2350 -->
## Functions

Functions


            standard error in functionality.

               •      Scene Object Out —

           Scene Object Out returns a reference to the scene object.

               •       Clip Plane Refnum Out —

             Clip Plane Refnum Out returns a reference to the clip plane object.

               •       error out —

             error out contains error information. This output provides standard error out functionality.

    SetSet LightLight

       Creates and positions a light source in 3D space relative to a 3D object.


            • Set Light (no reference) VI
            • Set Light (reference) VI
    SetSet LightLight (no(no reference)reference) VIVI

       Creates and positions a light source in 3D space relative to a 3D object.


      Inputs/Outputs

               •       Light State —


2350   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2350 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2351 ordinal=2351 -->
## Functions

Functions


  Light State specifies whether to enable the light state.

  0 Inherit Value (default)—The light inherits the state of the parent object.
  1 Off—Disables the light.
  2 On—Enables the light.

•      Scene Object In —

  Scene Object In specifies a reference to the scene you want to manipulate.

•       Light Refnum In —

  Light Refnum In specifies a reference to the light.

•      Position —

  Position specifies the x, y, and z coordinates that define the position of the light relative to its
  owning object.

      •     X —

     X specifies the X coordinate of the light source. The default value is 0.

      •      Y —

      Y specifies the Y coordinate of the light source. The default value is 0.

      •     Z —

     Z specifies the Z coordinate of the light source. The default value is 0.


•       error in (no error) —

  error in describes error conditions that occur before this node runs. This input provides
  standard error in functionality.

•      Scene Object Out —

  Scene Object Out returns a reference to the scene object.

•       error out —


                                                   © National Instruments 2351

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2351 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2352 ordinal=2352 -->
## Functions

Functions


             error out contains error information. This output provides standard error out functionality.

    SetSet LightLight (reference)(reference) VIVI


      Inputs/Outputs

               •       Light State —

            Light State specifies whether to enable the light state.

           0 Inherit Value (default)—The light inherits the state of the parent object.
           1 Off—Disables the light.
           2 On—Enables the light.

               •      Scene Object In —

           Scene Object In specifies a reference to the scene you want to manipulate.

               •       Light Refnum In —

            Light Refnum In specifies a reference to the light.

               •      Position —

            Position specifies the x, y, and z coordinates that define the position of the light relative to its
           owning object.

                     •     X —

              X specifies the X coordinate of the light source. The default value is 0.

                     •      Y —


2352   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2352 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2353 ordinal=2353 -->
## Functions

Functions


        Y specifies the Y coordinate of the light source. The default value is 0.

         •     Z —

       Z specifies the Z coordinate of the light source. The default value is 0.


   •       error in (no error) —

    error in describes error conditions that occur before this node runs. This input provides
    standard error in functionality.

   •      Scene Object Out —

    Scene Object Out returns a reference to the scene object.

   •       Light Refnum Out —

    Light Refnum In returns a reference to the light.

   •       error out —

    error out contains error information. This output provides standard error out functionality.

ApplyApply TextureTexture

Maps a texture to the surface of a 3D object. You must manually select the polymorphic
instance to use.


  • Apply Texture (no reference) VI
  • Apply Texture (reference) VI


                                                    © National Instruments 2353

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2353 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2354 ordinal=2354 -->
## Functions

Functions

   ApplyApply TextureTexture (no(no reference)reference) VIVI

      Maps a texture to the surface of a 3D object. You must manually select the polymorphic
       instance to use.


      Inputs/Outputs

               •       Vertical Wrap Mode —

             Vertical Wrap Mode specifies how to vertically wrap the texture around a 3D object.

           Clamp (default)—The texture does not repeat across the surface of the object when you pass
           0 texture coordinates outside the range [0…1]. LabVIEW interprets any texture coordinates in
           Image outside this range with clamped values.
           Repeat—The texture repeats across the surface of the object when you pass texture
           1 coordinates outside the range [0…1]. LabVIEW only considers the fractional part of the texture
              coordinate. For example, LabVIEW interprets 0.4 and 3.4 as the same texture coordinate.

               •      Horizontal Wrap Mode —

            Horizontal Wrap Mode specifies how to horizontally wrap the texture around a 3D object.

           Clamp (default)—The texture does not repeat across the surface of the object when you pass
           0 texture coordinates outside the range [0…1]. LabVIEW interprets any texture coordinates in
           Image outside this range with clamped values.
           Repeat—The texture repeats across the surface of the object when you pass texture
           1 coordinates outside the range [0…1]. LabVIEW only considers the fractional part of the texture
              coordinate. For example, LabVIEW interprets 0.4 and 3.4 as the same texture coordinate.

               •      Scene Object In —


2354   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2354 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2355 ordinal=2355 -->
## Functions

Functions


  Scene Object In specifies a reference to the scene you want to manipulate.

•     Image Data —

  Image Data specifies the image you want to apply as a texture.

      •     image type —

      •     image depth —

      •     image —

      •     mask —

      •       colors —

      •      Rectangle —

             •        left —

             •      top —

             •       right —

             •     bottom —


•      Apply Mode —

  Apply Mode specifies how LabVIEW applies the texture to the 3D object.


   As a Decal (default)—Applies the texture as a decal, blending the colors of the texture and the
   geometry of the object according to the following formula:
  0
    Result Color=(1–Alpha in texel)*Color of geometry+Alpha in texel*Color in texel

   The alpha of the vertex does not change and is the same as the alpha in the geometry.


                                                   © National Instruments 2355

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2355 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2356 ordinal=2356 -->
## Functions

Functions


            With Modulation—Applies the texture to the surface of the object and modulates the texture by
             the color of the surface according to the following formulas:
           1              Result Color=Color(texel)*Color(geometry)

              Result Alpha=Alpha(texel)*Alpha(geometry)


            With Blending—Blends the texture with the Blend Color of the texture according to the
              following formula:
           2
              Result Color=(–Color in texel)*Color in geometry+Color in texel*Blend Color

            The resulting alpha value is Alpha(texel)*Alpha(geometry)

            As a Replacement—Replaces the color of the geometry with the color of the texture. LabVIEW           3
              also replaces the alpha value of the geometry with the alpha value of the texture.

               •       error in (no error) —

             error in describes error conditions that occur before this node runs. This input provides
            standard error in functionality.

               •        Filter Mode —

               Filter Mode specifies the method to use to filter the texel colors applied to the geometry.
              Different values affect the quality and speed of the texture mapping.

           0 No Filtration (default)—LabVIEW uses the closest texel for the texture color.
             Linear Filtration—Filters the texture by taking the weighted linear average of the 2x2 array of
           1
               texels that lies nearest to the center of the pixels of the texture map.
            Simple Mipmap Filtration—Stores mipmaps, or multiple copies of the texture, at increasingly
           2 smaller resolutions. LabVIEW chooses the mipmap with texels closest in size to the pixel it is
               texturing and then chooses the nearest texel as the texture color.
               Bilinear Filtration—Performs a linear filtration but uses the mipmap with texels closest in size
           3
              to the pixel LabVIEW is texturing.
               Trilinear Filtration—LabVIEW chooses the two mipmaps that are closest in size to the pixel it is
           4 texturing and then performs a linear filtration on both textures. The resulting texture color is
             the weighted average of the two values.

               •      Blend Color —


2356   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2356 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2357 ordinal=2357 -->
## Functions

Functions


    Blend Color specifies the RGBA color to use to blend the texture you apply to the object. This
    input blends a color with a texture when Apply Mode is set to With Blending.

         •     Red —

       Red specifies the red value. The default is 0.

         •      Green —

       Green specifies the green value. The default is 0.

         •      Blue —

        Blue specifies the blue value. The default is 0.

         •      Alpha —

        Alpha specifies the level of opacity. The default value is 0.


   •      Scene Object Out —

    Scene Object Out returns a reference to the scene object.

   •       error out —

    error out contains error information. This output provides standard error out functionality.

ApplyApply TextureTexture (reference)(reference) VIVI

      Note Returns a reference to a texture in a scene.


                                                    © National Instruments 2357

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2357 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2358 ordinal=2358 -->
## Functions

Functions


      Inputs/Outputs

               •       Vertical Wrap Mode —

             Vertical Wrap Mode specifies how to vertically wrap the texture around a 3D object.

           Clamp (default)—The texture does not repeat across the surface of the object when you pass
           0 texture coordinates outside the range [0…1]. LabVIEW interprets any texture coordinates in
           Image outside this range with clamped values.
           Repeat—The texture repeats across the surface of the object when you pass texture
           1 coordinates outside the range [0…1]. LabVIEW only considers the fractional part of the texture
              coordinate. For example, LabVIEW interprets 0.4 and 3.4 as the same texture coordinate.

               •      Horizontal Wrap Mode —

            Horizontal Wrap Mode specifies how to horizontally wrap the texture around a 3D object.

           Clamp (default)—The texture does not repeat across the surface of the object when you pass
           0 texture coordinates outside the range [0…1]. LabVIEW interprets any texture coordinates in
           Image outside this range with clamped values.
           Repeat—The texture repeats across the surface of the object when you pass texture
           1 coordinates outside the range [0…1]. LabVIEW only considers the fractional part of the texture
              coordinate. For example, LabVIEW interprets 0.4 and 3.4 as the same texture coordinate.

               •      Scene Object In —

           Scene Object In specifies a reference to the scene you want to manipulate.

               •     Image Data —

          Image Data specifies the image you want to apply as a texture.

                     •     image type —


2358   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2358 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2359 ordinal=2359 -->
## Functions

Functions


      •     image depth —

      •     image —

      •     mask —

      •       colors —

      •      Rectangle —

             •        left —

             •      top —

             •       right —

             •     bottom —


•      Apply Mode —

  Apply Mode specifies how LabVIEW applies the texture to the 3D object.


   As a Decal (default)—Applies the texture as a decal, blending the colors of the texture and the
   geometry of the object according to the following formula:
  0    Result Color=(1–Alpha in texel)*Color of geometry+Alpha in texel*Color in texel

   The alpha of the vertex does not change and is the same as the alpha in the geometry.


   With Modulation—Applies the texture to the surface of the object and modulates the texture by
   the color of the surface according to the following formulas:
  1
    Result Color=Color(texel)*Color(geometry)

    Result Alpha=Alpha(texel)*Alpha(geometry)


  2 With Blending—Blends the texture with the Blend Color of the texture according to the


                                                   © National Instruments 2359

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2359 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2360 ordinal=2360 -->
## Functions

Functions


              following formula:

              Result Color=(–Color in texel)*Color in geometry+Color in texel*Blend Color

            The resulting alpha value is Alpha(texel)*Alpha(geometry)

            As a Replacement—Replaces the color of the geometry with the color of the texture. LabVIEW           3              also replaces the alpha value of the geometry with the alpha value of the texture.

               •       error in (no error) —

             error in describes error conditions that occur before this node runs. This input provides
            standard error in functionality.

               •        Filter Mode —

               Filter Mode specifies the method to use to filter the texel colors applied to the geometry.
              Different values affect the quality and speed of the texture mapping.

           0 No Filtration (default)—LabVIEW uses the closest texel for the texture color.
             Linear Filtration—Filters the texture by taking the weighted linear average of the 2x2 array of           1
               texels that lies nearest to the center of the pixels of the texture map.
            Simple Mipmap Filtration—Stores mipmaps, or multiple copies of the texture, at increasingly
           2 smaller resolutions. LabVIEW chooses the mipmap with texels closest in size to the pixel it is
               texturing and then chooses the nearest texel as the texture color.
               Bilinear Filtration—Performs a linear filtration but uses the mipmap with texels closest in size           3              to the pixel LabVIEW is texturing.
               Trilinear Filtration—LabVIEW chooses the two mipmaps that are closest in size to the pixel it is
           4 texturing and then performs a linear filtration on both textures. The resulting texture color is
             the weighted average of the two values.

               •      Blend Color —

           Blend Color specifies the RGBA color to use to blend the texture you apply to the object. This
            input blends a color with a texture when Apply Mode is set to With Blending.

                     •     Red —

             Red specifies the red value. The default is 0.


2360   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2360 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2361 ordinal=2361 -->
## Functions

Functions


         •      Green —

       Green specifies the green value. The default is 0.

         •      Blue —

        Blue specifies the blue value. The default is 0.

         •      Alpha —

        Alpha specifies the level of opacity. The default value is 0.


   •      Scene Object Out —

    Scene Object Out returns a reference to the scene object.

   •      Texture Refnum —

    Texture Refnum returns the reference to the texture.

   •       error out —

    error out contains error information. This output provides standard error out functionality.

ApplicationApplication ControlControl

Use the Application Control VIs and functions to programmatically control VIs and
LabVIEW applications on the local computer or across a network. You can use these VIs
and functions to configure multiple VIs at the same time.


 Palette
                Description
 Object

 Open
 Application    Returns a reference to a VI Server application running on the specified computer.
 Reference


                                                    © National Instruments 2361

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2361 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2362 ordinal=2362 -->
## Functions

Functions


         Palette                       Description
        Object

         Function

       Open VI                       Returns a reference to a VI, custom control, or global variable specified by a path to         Reference                       the file on disk, name string, or existing reference.
         Function

                       Maintains a static reference to a VI. You can configure the Static VI Reference
          Static VI        function to output a generic or strictly typed VI reference. After you place the Static
         Reference      VI Reference function on a block diagram, double-click the function to display a file
                        dialog box where you can select a VI.

         Close                       Closes a refnum associated with an open VI, VI object, an open application instance,         Reference                        or a .NET, ActiveX or Python object.
         Function

                       Returns the arguments passed from the command line when LabVIEW or a
        Get            LabVIEW-built application launched. User-defined arguments start after two
      Command    hyphens (--) surrounded by spaces in the command line.
         Line
        Arguments       If an argument contains double quotation marks ("), this VI returns the argument
                       without the quotation marks.

                       Gets (reads) and/or sets (writes) properties of a reference. Use the property node to
         Property       get or set properties and methods on local or remote application instances, VIs, and
       Node           objects. You also can use the Property Node to access the private data of a LabVIEW
                           class.

                       Invokes a method or action on a reference. Most methods have associated        Invoke Node                       parameters.

          Call By         Calls the VI specified by reference. The reference VI must be a strictly typed VI
         Reference      reference.

                          Starts an asynchronous call to the VI indicated by the reference input. Depending
          Start
                   on how you prepare reference for asynchronous execution with the Open VI
        Asynchronous
                       Reference function, you can either ignore the VI after calling it or collect its outputs
          Call VI
                         at a later time with the Wait On Asynchronous Call node.

        Wait On
        Asynchronous  Waits for an asynchronous call to a target VI to finish executing and then returns the
          Call VI


2362   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2362 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2363 ordinal=2363 -->
## Functions

Functions


Palette               Description
Object

              outputs of the target VI. To use the Wait On Asynchronous Call node on a reference,
             you must include the 0x100 option flag as part of the options input of the Open VI
              Reference function when you open the reference. You also must call the target VI
              with the Start Asynchronous Call node.

To More              Typecasts a reference, such as a control or a type definition, to a more specific classSpecific Class               or interface in the inheritance hierarchy.Function

To More
              Typecasts a reference, such as a control or a type definition, to a more generic classGeneric Class               or interface in the inheritance hierarchy.Function

Class                Selects the class of the output. You also can create a class specifier constant from aSpecifier               control refnum control or terminal.
Constant

              Returns a static VI reference to the current VI by default. You can reconfigure this
               reference to return a reference to the current application, to a control or indicator in
              the VI, or to a pane by clicking on the block diagram icon and choosing from theVI Server
               shortcut menu. You can use this reference to access the properties and methods forReference              the associated VI, application, control, indicator, or pane. The VI Server Reference
              always returns a fully authenticated reference. Use caution when passing
               references to other VIs if you are concerned about password security.

              Returns the chain of callers from the current VI to the top-level VI. Element 0 of the
Call Chain       call chain array contains the name of the lowest VI in the call chain. Subsequent
Function      elements are callers of the lower VIs in the call chain. The last element of the call
              chain array is the name of the top-level VI.

              Returns drag data from the current drag and drop operation. Only use this function
Get Drag Drop when it is necessary to access the drag data, not just to examine the data type. If a
Data Function  drag and drop operation is not in progress, LabVIEW returns an error. If the data
              requested is unavailable, LabVIEW returns an error.

              Stops the VI in which it executes, just as if you clicked the Abort Execution button
            on the toolbar. Before you call this function with a TRUE input, be sure to complete
Stop Function
                    all final tasks for the VI first, such as closing files, setting safe values for devices
              being controlled, and so on.

Quit LabVIEW
              Stops all executing VIs and ends the current instance of LabVIEW.
Function


                                                    © National Instruments 2363

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2363 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2364 ordinal=2364 -->
## Functions

Functions


         Palette                       Description
        Object

                        Sets values to the controls for the VI you reference. This function offers better         Set Control                      performance than VI Server objects that write to the terminal of a front panel         Values by                          control, such as using the Value property in the Control class. However, this         Index
                        function requires more advanced application design than other methods for setting         Function                         control values.

                       Gets values from the controls for the VI you reference. This function offers better        Get Control                      performance than VI Server objects that read from the terminal of a front panel         Values by
                          control, such as using the Value property in the Control class. However, this         Index                        function requires more advanced application design than other methods for getting         Function                         control values.

         Palette       You can use the Palette Editing VIs to edit the Controls or Functions palette set
         Editing        programmatically.


       CPU         Use the CPU Information functions to obtain information on the characteristics of a
         Information   computer or target.


       Memory      Use the Memory Control VIs and functions to improve LabVIEW memory
         Control       performance.


                     You can use the VI Scripting VI and functions to create, edit, and run VIs          VI Scripting
                       programmatically.


         Application
                    Use the Application Builder VIs to build, deploy, or clean build specifications.
         Builder

    OpenOpen ApplicationApplication ReferenceReference FunctionFunction

       Returns a reference to a VI Server application running on the specified computer.

           If you specify an empty string for machine name, it returns a reference to the local
      LabVIEW application in which this function is running. If you do specify a machine
      name, it attempts to establish a TCP connection with a remote VI Server on that

2364   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2364 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2365 ordinal=2365 -->
## Functions

Functions

machine on the specified port.


Inputs/Outputs

   •     machine name ("": open local reference) —

    machine name is the address of the computer that runs an application instance to which you
    want to establish a connection.

    This address can be in dotted decimal notation (such as 130.164.15.250) or domain name
    notation (such as foo.ni.com). An empty string causes this function to return a reference to
    the local application instance.
   •      port number or service name (3363) —

    port number or service name can accept a numeric or a string input. The default is a numeric.
    port number or service name is the port on which the remote LabVIEW application is listening.

       If you specify a service name, LabVIEW queries the NI Service Locator for the port number that
    the server registered. The default is to use the default VI Server listener port number (3363).

    To establish communication between a VI and another LabVIEW application, you must know
    both the machine name and the port number or service name on which the VI Server in the
    other LabVIEW application is listening. If you have more than one LabVIEW application on the
   same machine, one or more of those applications may be listening on a port other than the
     default VI Server listener port. In this case, make sure to supply the port number or service
    name. Use the VI Server page to set the port number and service name for a VI Server or use the
    Server:Port and Server:Service Name properties to set the port number or service name
    programmatically.

          Note The VI Server settings in the Options dialog box apply to the default application
              instance, or VIs not in a project. To set VI Server settings for a project application
              instance, right-click the target in the Project Explorer window.

   •      timeout ms (60000) —

    timeout ms specifies the time, in milliseconds, that the function waits to complete and return an
     error. The default value is 60,000 ms or 1 minute. A value of –1 indicates to wait indefinitely.


                                                    © National Instruments 2365

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2365 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2366 ordinal=2366 -->
## Functions

Functions

               •       error in (no error) —

             error in describes error conditions that occur before this node runs. This input provides
            standard error in functionality.

               •      application reference —

            application reference is the reference to the specified application.

               •       error out —

             error out contains error information. This output provides standard error out functionality.


      You can use the application reference output as an input to the Property and Invoke
      Nodes to get or set properties and invoke methods on the application. Using it as the
       input to the Open VI Reference function lets you get references to VIs in that
       application. Close the reference with the Close Reference function. If you do not close
        this reference, it closes automatically after the top-level VI associated with this
       function completes execution. However, it is good practice to conserve the resources
       involved in maintaining the connection by closing the reference when you finish using
           it.

           If you use the Open Application Reference function on a remote VI Server connection,
      you may receive an error that the network connection was closed by a peer. Verify that
       the machine is allowed access by selecting Tools»Options»VI Server on the server
        side. You also can verify the user access settings in the User access section of the VI
       Server page on the server side, also located in the Options dialog box.

    OpenOpen VIVI ReferenceReference FunctionFunction

       Returns a reference to a VI, custom control, or global variable specified by a path to the
          file on disk, name string, or existing reference.


2366   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2366 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2367 ordinal=2367 -->
## Functions

Functions

Inputs/Outputs

   •      type specifier VI Refnum (for type only) —

    type specifier VI Refnum (for type only) determines the connector pane information and data
    type of vi reference. LabVIEW ignores the actual value of this input.

    By default, the function returns a Generic VI reference.

       If you want to use the vi reference output of this function with the Call By Reference node or the
     Start Asynchronous Call node, you must wire a strictly typed VI reference to this input.

       If you wire a strictly typed VI reference to this input, the connector pane of the VI specified by vi
    path must match the connector pane of this input.

   •      application reference (local) —

    application reference is a reference to a LabVIEW application instance.

    By default, LabVIEW uses the application instance of the calling VI. You can obtain references to
    other application instances with the Open Application Reference function. If you wire a reference
    to another application instance to the application reference input, vi path refers to a location in
    the file system of the computer that is running that application instance.
   •        vi path —

     vi path accepts a path to the VI that you want to reference, a string containing the name of the VI
    that you want to reference, or a VI reference to the VI that you want to reference.

       If you wire a path, LabVIEW searches for a VI in memory that you previously loaded from that
    path on the same target. If you wire a name string, the string must match the full delimited name
     of a VI in memory on that target. If a matching VI is not found in memory, LabVIEW then tries to
    load the VI from that file on disk. An error occurs if LabVIEW cannot find the file.

       If the path is relative, the VI interprets the path as relative to the caller VI or to the application
     directory, if the caller VI is not saved.

          Note

                     If you specify a remote application instance with application reference, the path is
              interpreted on the remote machine in the context of the remote file system. The path
                  is expressed using the local computer's path separators, but is translated to the
            remote computer's path separators when the request arrives there.


                                                    © National Instruments 2367

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2367 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2368 ordinal=2368 -->
## Functions

Functions


                     For example, to reference a VI on Linux at My HD/LabVIEW Vis/foo.vi from a
                  Windows–based application, use the path My HD:\LabVIEW Vis\foo.vi.
                      Conversely, to reference a VI on a computer running Windows at C:\labview\
                foo.vi from an Linux application, wire the path C/labview/foo.vi.


                    If you wire a path or you wire both VI and application references, LabVIEW waits until the user
             interface is idle to load the VI from disk. If you wire a name string or a VI reference without an
             application reference, LabVIEW does not need to wait until the user interface is idle, as it does
            not load a VI from disk. LabVIEW will only search in memory for a VI with a specified name.

               Note LabVIEW does not support the ability to open a reference to a clone VI using a
                name with the Open VI Reference function. Using this function to open a reference to
                   a clone VI may cause LabVIEW to crash.

               •      options —

            options determines characteristics of the VI referenced by vi reference, including whether you
           can call the VI asynchronously. The default is 0x0.

            Create options by combining a subset of the following option flags.

           Option                   Description
              flag
                 Record modifications—Use this option flag when you want an asterisk (*) to appear by
           0x01  the VI title when changes have been made using VI Server. The VI must be in edit mode
                      for LabVIEW to record the modifications.
               Open templates for editing—Use this option flag to open the original .vit file. If you do
                  not select this option flag, LabVIEW opens a new instance of the template VI. Edits made
           0x02
                    to an instance do not affect the original .vit file. This option flag has no effect on non-
                  template files.
                Prompt user to save—Use this option flag to prompt the user to save changes when this
                      VI reference closes if all the following conditions are true:
                               • The referenced VI or its subVIs contain unsaved changes.
           0x04       • There are no other open references to the referenced VI.
                               • The referenced VI is able to leave memory. A VI is able to leave memory, for example,
                                       if no other VIs call the VI, the front panel of the VI is closed, and the VI is not a
                  member of an open project library, and so on.


2368   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2368 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2369 ordinal=2369 -->
## Functions

Functions


Option       Description
flag

      Prepare for reentrant run—Use this option flag when you want a reference to a reentrant
       clone of the target VI, instead of the target VI itself. Reentrant clones of a VI allow you to
      open multiple front panels of the same VI or to run multiple copies of the same VI in
        parallel. For each reference to the target VI, LabVIEW creates a separate clone of the
       target VI. This clone is not part of the pool of shared clones used by regular subVI calls.

      LabVIEW ignores this flag if you wire the type specifier VI Refnum (for type only) input
      because when you provide a type specifier, you can always get a reentrant clone if the
0x08   target VI is reentrant. LabVIEW returns error 1096 if the target VI is not reentrant.

             Tip Use this flag in combination with the Run VI method to execute multiple
                reentrant clones in parallel. Use the Start Asynchronous Call node instead of
               the Run VI method to run target VIs asynchronously. In addition to providing a
               simpler interface and better performance, the Start Asynchronous Call node
                allows you to collect the outputs of the target VI with a corresponding Wait On
              Asynchronous Call node.

      Prompt to find missing subVIs—Use this option flag to prompt the user to allow LabVIEW0x10
       to search for missing subVIs of the referenced VI.
      Hide loading dialog box—Prevents LabVIEW from displaying the loading dialog box
     when searching for missing subVIs of the referenced VI.

0x20
           Note This option flag does not affect whether LabVIEW prompts you to find
               the missing VIs or not.

      Enable simultaneous calls on reentrant VIs—Use this option flag when you want to use
       multiple Call By Reference or Start Asynchronous Call nodes to execute clones of a
       reentrant target VI in parallel, as when you use these nodes within a For Loop with
        parallel loop iterations. This option flag enables parallel execution because it gives each
        Call By Reference node access to the data spaces of the clone VIs. If you do not use this
       option flag, calls to the same target VI execute one at a time because they must wait for
0x40  access to the same data space.

      The 0x40 option flag is valid only in the following situations:

             • The target VI is reentrant and shares clones.
             • The target VI is reentrant, and you also include either the 0x80 or the 0x100 option
              flag.


                                                 © National Instruments 2369

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2369 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2370 ordinal=2370 -->
## Functions

Functions


           Option                   Description
              flag

                    Note LabVIEW returns error 1591 if the 0x40 option flag is not valid for the
                              target VI or the other included option flags.

                  Prepare to call and forget—Use this option flag when you want to call a target VI
                  asynchronously with the Start Asynchronous Call node but you do not need to know
               when or what the VI returns. Do not use this option flag with 0x08 or 0x100.
           0x80
                    Note LabVIEW returns error 1578 if you use this option flag with a reference
                             to a remote VI.

                  Prepare to call and collect—Use this option flag when you want to collect the results of
                an asynchronous call to a target VI with the Wait On Asynchronous Call node. If you use
                      this option flag, you must include one Wait On Asynchronous Call node for every call that
                 you begin with a Start Asynchronous Call node to ensure that LabVIEW does not retain
           0x100 any started calls in memory indefinitely. Do not use this option flag with 0x08 or 0x80.

                    Note LabVIEW returns error 1578 if you use this option with a reference to a
                         remote VI.


               •       error in (no error) —

             error in describes error conditions that occur before this node runs. This input provides
            standard error in functionality.

               •      password ("") —

           password is the password for the VI whose reference you want to open.

            Wire a password to this input if you want to edit a password-protected target VI. If you wire the
             correct password, the function returns an authenticated reference to the VI. If you wire an
             incorrect password to this input, the function returns an error and an invalid VI reference.
           LabVIEW ignores this input if the target VI is not password-protected. If you do not wire a
           password to this input and the target VI is password-protected, the Open VI Reference function
             returns a valid reference, but you cannot use the reference to edit the VI.

               Note You can also use a VI Server Reference to get an authenticated reference to a VI.

               •        vi reference —

2370   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2370 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2371 ordinal=2371 -->
## Functions

Functions


     vi reference is the refnum associated with the requested VI.

       If the function fails, vi reference contains Not A Refnum.
   •       error out —

    error out contains error information. This output provides standard error out functionality.


The Open VI Reference function prepares a VI reference for dynamic calls by the Call By
Reference node, the Start Asynchronous Call node, and the Wait On Asynchronous Call
node. Use the type specifier VI Refnum (for type only) and the options inputs to
prepare a reference for dynamic execution.

Opening References for Dynamic VI Calls

If you want to call the specified VI dynamically with the Call By Reference Node or the
Start Asynchronous Call Node, you must use appropriate data for the following
parameters:

  • type specifier VI Refnum (for type only)—Wire a strictly typed VI reference to this
    input.
  • options—Determine whether the 0x08, 0x40, 0x80, and 0x100 option flags apply to
   the way you want to call the referenced VI.

Criteria for Opening Strictly Typed References

If you wire a strictly typed VI reference to the type specifier VI Refnum (for type only),
the VI specified by vi path must meet the following criteria:

  • The VI cannot be broken.
  • The VI cannot be active as a top-level VI unless the VI is reentrant.
  • The connector pane of the VI must match the connector pane of type specifier VI
   Refnum (for type only).

Opening References to Reentrant VIs
If you open a reference to a reentrant VI, consider the following details:

  • Dynamic calls to reentrant target VIs execute serially unless you specify 0x40 as

                                                    © National Instruments 2371

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2371 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2372 ordinal=2372 -->
## Functions

Functions

         one of the options.
            •  If you use the 0x40 option flag to execute instances of a reentrant target VI in
            parallel, vi reference refers to the target VI rather than to a clone of the target VI.
          However, both the Call By Reference node and the Start Asynchronous Call node
             call a clone of the target VI. Therefore, if you call a VI Server property or method on
            vi reference, the property or method does not affect the clone VIs that those nodes
           actually call.
            • The Equal? function always returns TRUE when you compare two references to the
        same reentrant VI. To determine whether the references refer to the same instance
           of the reentrant VI, use the Type Cast function to convert the references to 32-bit
          signed integers. Then use the Equal? Function to compare those integers.

      Aborting Open References

      You can abort all open VI references either manually from the front panel of the VI or
      by using the Abort VI method. However, VI references prepared for asynchronous
       execution have important caveats depending on the options used to open the
       reference:

            • 0x80—A call-and-forget VI aborts only if you manually abort it from its front panel
           or call the Abort VI method on it. Otherwise, the VI runs to completion, even if you
           close the reference or abort the calling VI.
            • 0x100—Call-and-collect VIs abort for the following reasons:
     ◦ You abort the VI that opened the call-and-collect VI reference. In this case,
            LabVIEW aborts all running instances of the VI.
     ◦ You manually abort a specific instance of the VI. In this case, exactly one Wait
          On Asynchronous Call node returns an error indicating that the called VI
              aborted. All other Wait On Asynchronous Call nodes that are waiting on calls to
              the same VI reference continue waiting.
     ◦ You call the Abort VI method on the call-and-collect VI reference. In this case,
            LabVIEW aborts all currently running instances of the VI. A corresponding
           number of Wait On Asynchronous Call nodes return errors.

      Closing Open References

        After you finish using a reference that you obtain with this function, close the reference
       with the Close Reference function. Explicitly closing a reference enables LabVIEW to
        free the resources involved in maintaining that reference, thereby contributing to

2372   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2372 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2373 ordinal=2373 -->
## Functions

Functions

optimal memory allocation and performance. Otherwise, LabVIEW cannot close the
reference until the VI that opened the reference finishes executing.

      Note Closing a reference that was opened with the 0x80 option flag does not
       abort the referenced VI.

Opening a VI Reference in a Stand-Alone Application

If you want to dynamically open a VI on both the development computer and within a
stand-alone application, use a relative path for vi path.

Miscellaneous Details

  •  If you set the Execution:Run When Opened, Execution:Show Front Panel On Load,
    or Execution:Show Front Panel On Call properties or the corresponding options in
   the VI Properties dialog box of the target VI, LabVIEW ignores the settings.
  • To open a new Facade VI reference, wire a FacadeVI class to type specifier VI
   Refnum (for type only).

Examples

Refer to the following example files included with LabVIEW.

  • labview\examples\Application Control\VI Server\
   Asynchronous Call By Reference\Asynchronous Call and
   Collect (Using Option 0x40).vi
  • labview\examples\Application Control\VI Server\
   Asynchronous Call By Reference\Asynchronous Call and
   Forget.vi
  • labview\examples\Application Control\VI Server\
   Asynchronous Call By Reference\Asynchronous Call and
   Collect.vi

StaticStatic VIVI ReferenceReference

Maintains a static reference to a VI. You can configure the Static VI Reference function
to output a generic or strictly typed VI reference. After you place the Static VI Reference

                                                    © National Instruments 2373

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2373 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2374 ordinal=2374 -->
## Functions

Functions

       function on a block diagram, double-click the function to display a file dialog box
      where you can select a VI.


      Inputs/Outputs

               •    —

              vi reference is the refnum associated with the configured VI.

                    If the VI is not valid, vi reference contains Not A Refnum.

      The Static VI Reference function acts as a subVI and appears in the VI hierarchy of the
       top-level VI. By default, the output is a generic VI reference.

      You can change the output of this function to a strictly typed VI reference. Right-click
       the function and select Strictly Typed VI Reference from the shortcut menu to change
       the output. A red star in the upper left corner of the function icon indicates the
       reference is strictly typed. The strictly typed VI reference identifies the connector pane
       of the VI you are calling. You can create a strictly typed VI reference only from a VI or VI
       template, not from a polymorphic VI or other non-VI file such as a global variable or
        control.

      Use a strictly typed VI reference if you want to call the referenced VI with the Call By
       Reference node or the Start Asynchronous Call node. When you create a strictly typed
        VI reference, you cannot wire vi reference to the Run VI method. You cannot use the
      Run VI method to run a VI that is already reserved for execution by another VI. A strictly
      typed static VI reference also reserves any subVIs when a top-level VI is reserved, thus
      making it ineligible for the Run VI method. Refer to the Run VI method for more
       information.

      LabVIEW loads the referenced VI into memory when you load the top-level VI. When
       the Static VI Reference function outputs a strictly typed VI reference, LabVIEW reserves
       the referenced VI as long as the top-level VI is running. LabVIEW closes this reference
     when the top-level VI is no longer in memory. You do not have to explicitly close the
       reference this function returns.

2374   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2374 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2375 ordinal=2375 -->
## Functions

Functions

      Note LabVIEW does not check whether the referenced VI can compile. If the
        referenced VI is broken, LabVIEW does not recognize that it is broken until
       you run the top-level VI. If you execute an Open VI Reference function that
        references the broken VI, you receive an error.

            If you want LabVIEW to check for a broken referenced VI before you run the
        top-level VI, use the referenced VI directly in the top-level VI instead of using a
         Static VI Reference function by clicking the Select a VI icon or text on the
       Functions palette and navigating to the VI you want to add to the block
       diagram.

CloseClose ReferenceReference FunctionFunction

Closes a refnum associated with an open VI, VI object, an open application instance, or
a .NET, ActiveX or Python object.


Inputs/Outputs

   •      reference —

    reference is the refnum associated with an open VI, VI object, an open application instance, or a
    .NET or ActiveX object. reference also accepts 1D arrays of references.

   •       error in (no error) —

    error in describes error conditions that occur before this node runs. With the following
    exception, this input provides standard error in functionality.

    This node runs normally evenifan error occurred before this node runs.

   •       error out —

    error out contains error information. This output provides standard error out functionality.


                                                    © National Instruments 2375

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2375 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2376 ordinal=2376 -->
## Functions

Functions

     When you create a refnum to a VI, LabVIEW loads the VI into memory. The VI stays in
     memory until you close the refnum and until the VI meets the following conditions:

            • There are no other open references to the referenced VI.
            • The front panel of the VI is not open.
            • The VI is not a subVI of another VI in memory.
            • The VI is not a member of an open project library.

     GetGet CommandCommand LineLine ArgumentsArguments

       Returns the arguments passed from the command line when LabVIEW or a LabVIEW-
        built application launched. User-defined arguments start after two hyphens (--)
      surrounded by spaces in the command line.

           If an argument contains double quotation marks ("), this VI returns the argument
       without the quotation marks.


      Inputs/Outputs

               •       error in (no error) —

             error in describes error conditions that occur before this node runs. This input provides
            standard error in functionality.

               •      application name —

            application name returns the name of the application that launched this VI. The application can
          be LabVIEW or a LabVIEW-built application.

               •      arguments —

           arguments returns the user-defined arguments passed from the command line. User-defined
           arguments start after two hyphens (--) surrounded by spaces in the command line.

               •       error out —


2376   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2376 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2377 ordinal=2377 -->
## Functions

Functions


    error out contains error information. This output provides standard error out functionality.


For example, if you enter C:\temp\MyLabVIEWApp.exe -- abc 123 TRUE in
the command line when launching a LabVIEW-built application, application name
returns MyLabVIEWApp.exe and arguments returns an array of the following strings:
"abc", "123", "TRUE".

PropertyProperty NodeNode

Gets (reads) and/or sets (writes) properties of a reference. Use the property node to get
or set properties and methods on local or remote application instances, VIs, and
objects. You also can use the Property Node to access the private data of a LabVIEW
class.

The Property Node automatically adapts to the class of the object that you reference.
LabVIEW includes Property Nodes preconfigured to access XML Properties, VISA
properties, .NET properties, and ActiveX properties.


Inputs/Outputs

   •      reference —

    reference is the refnum associated with the object for which you want to set or get properties.

       If the Property Node class is Application or VI, you do not have to wire a refnum to this input. For
    the Application class, the default is the current application instance. For the VI class, the default
      is the VI containing the Property Node.

    You also can wire a LabVIEW class to the reference input to access the private data of the
    LabVIEW class.

   •       error in (no error) —


                                                    © National Instruments 2377

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2377 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2378 ordinal=2378 -->
## Functions

Functions


             error in describes error conditions that occur before this node runs. This input provides
            standard error in functionality.

               •      Property —

            property 2..n are examples of properties you want to set (write).

               •      reference out —

            reference out returns reference unchanged.

               •       error out —

             error out contains error information. This output provides standard error out functionality.

               •      Property —

            property 1..n are examples of properties you want to get (read).


      To select the class on which to execute the property, wire the refnum to the reference
       input. For example, to select the VI, Generic, or Application class, wire the VI, VI object,
       or application reference to the reference input. The node adapts to the class
       automatically. You also can right-click the node and select a class from the shortcut
      menu.

      You can wire a LabVIEW class to the reference input of a Property Node. If the LabVIEW
       class has accessor VIs that you can access through a Property Node, you can read from
       or write to the accessor VIs using a Property Node.

      You can quickly view the implementation of a LabVIEW class property if the block
      diagram of the accessor VI is available. To view the implementation of a LabVIEW class
       property, right-click the property and select Open Accessor VI from the shortcut menu.
           If the property is dynamic with more than one implementation, selecting this option
       displays the Choose Implementation dialog box. Use this dialog box to view all
      implementations of the property, or dynamic dispatch member VI, and open one or
      more implementations.

           Note If you do not wire the Property Node, the class property still executes


2378   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2378 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2379 ordinal=2379 -->
## Functions

Functions


        at run-time.

If the Property Node opens and returns a reference to an object, use the Close
Reference function to close the reference.

Move the cursor over terminals in the Property Node to display more information
about the property in the Context Help window. You also can right-click a property
terminal and select Help For Propertyfrom the shortcut menu, where Propertyis
the name of the property.

You can read or write multiple properties using a single node. However, some
properties are not readable and some are not writable. Use the Positioning tool to
resize the Property Node to add new terminals. A small direction arrow to the right of
the property indicates a property you read. A small direction arrow to the left of the
property indicates a property you write. Right-click the property and select Change to
Read or Change to Write from the shortcut menu to change the operation of the
property.

The node executes from top to bottom. The Property Node does not execute if an error
occurs before it executes, so always check for the possibility of errors. If an error
occurs in a property, LabVIEW ignores the remaining properties and returns an error. If
you right-click the Property Node and select Ignore Errors Inside Node, LabVIEW
executes the remaining properties on the Property Node. Only the first error is
returned by the Property Node. The error out cluster contains information about
which property caused the error.

Properties have a short or long name that you can change by right-clicking and
selecting Name Format from the shortcut menu. The No Names format displays only
the data type for each property.

      Note You can right-click the Property Node and select Downcast to Class
       from the shortcut menu to typecast a reference to a more specific class in the
        inheritance hierarchy. For example, select Downcast to Class from an
       Interchangeable Virtual Instruments (IVI) class driver to view the IVI specific
        driver properties. This item is not supported for all class types. If Downcast
        to Class is disabled, you can use the To More Specific Class and To More


                                                    © National Instruments 2379

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2379 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2380 ordinal=2380 -->
## Functions

Functions


              Generic Class functions.

     InvokeInvoke NodeNode

       Invokes a method or action on a reference. Most methods have associated parameters.

           If the node is configured for VI Server Application class or Virtual Instrument class and
       reference is unwired, reference defaults to the current Application or VI. LabVIEW
       includes Invoke Nodes preconfigured to access XML methods, .NET methods, and
       ActiveX methods.


      Inputs/Outputs

               •      reference —

            reference is the refnum associated with the object on which you want to invoke a method or
           perform an action. If the Invoke Node class is Application or VI, you do not have to wire a refnum
             to this input. For the Application class, the default is the current application instance. For the VI
              class, the default is the VI containing the Invoke Node.

               •       error in (no error) —

             error in describes error conditions that occur before this node runs. This input provides
            standard error in functionality.

               •      input 1 —

            input 1..n are example input parameters of a method.

               •      reference out —

            reference out returns reference unchanged.

               •       error out —


2380   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2380 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2381 ordinal=2381 -->
## Functions

Functions


     error out contains error information. This output provides standard error out functionality.

   •      return value —

    return value is an example return value of a method.

   •      output 1 —

    output 1..n are example output parameters of a method.


To select the class on which to execute the method, wire the refnum to the reference
input. For example, to select the VI, Control, or Application class, wire the VI, VI object,
or application reference to reference. The node adapts to the class automatically. You
also can right-click the node and select a class from the shortcut menu.

Right-click the node and select Help For Methodfrom the shortcut menu, where
Method is the name of the method, for more information about the method and its
parameters.

You can get (read) and set (write) the values of the method parameters. Parameters
with a white background are required inputs and the parameters with a gray
background are recommended inputs.

If the small direction arrow on the parameter is on the right, you are getting the
parameter value. If the small direction arrow on a parameter is on the left, you are
setting the parameter value. Methods have a short or long name that you can change
by right-clicking and selecting Name Format from the shortcut menu. The No Names
format displays only the data type for each method.

      Note You can right-click the Invoke Node and select Downcast to Class from
       the shortcut menu to typecast a reference to a more specific class in the
        inheritance hierarchy. For example, select Downcast to Class from an
        Interchangeable Virtual Instruments (IVI) class driver to view the IVI specific
        driver properties. This item is not supported for all class types. If Downcast
        to Class is disabled, you can use the To More Specific Class and To More
       Generic Class functions.


                                                    © National Instruments 2381

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2381 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2382 ordinal=2382 -->
## Functions

Functions

     .NET Invoke Node (Windows)

           If you right-click the Invoke Node and select Select Class».NET»Browse from the
       shortcut menu, LabVIEW displays the Select Object From Assembly dialog box.

     On the front panel or block diagram, right-click a .NET object, select Create»Invoke
      Node, and select a method from the shortcut menu to invoke a method for the object.
      You also can invoke .NET-specific methods for a .NET object. On the block diagram,
        right-click a .NET object, select Create»Invoke Node, and select a .NET-specific
      method from the shortcut menu.

      ActiveX Invoke Node (Windows)

       ActiveX does not support 64-bit integer data types. If you wire 64-bit integer data to a
       variant parameter of an ActiveX Invoke Node, LabVIEW converts the data to a double-
       precision, floating-point number. If you right-click the Invoke Node and select Select
      Class»ActiveX»Browse from the shortcut menu, LabVIEW displays the Select Object
      From Type Library dialog box.

     On the front panel or block diagram, right-click an ActiveX object, select
       Create»Invoke Node, and select a method from the shortcut menu to invoke a method
        for the object. You also can invoke ActiveX-specific methods for an ActiveX object. On
       the block diagram, right-click an ActiveX object, select Create»Invoke Node, and select
      an ActiveX-specific method from the shortcut menu.

      CallCall ByBy ReferenceReference

        Calls the VI specified by reference. The reference VI must be a strictly typed VI
       reference.


      Inputs/Outputs

               •      reference —

2382   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2382 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2383 ordinal=2383 -->
## Functions

Functions


    reference is the refnum associated with a VI that is already open.

    The reference must be a strictly typed VI reference.

   •       error in (no error) —

    error in describes error conditions that occur before this node runs. This input provides
    standard error in functionality.

   •      reference out —

    reference out returns reference unchanged.

   •       error out —

    error out contains error information. This output provides standard error out functionality.


Both the Call By Reference node and the subVI node call a VI. The Call By Reference
node enables you to call any VI dynamically whose connector pane matches that of the
strictly typed reference input. Use the Open VI Reference function to obtain a strictly
typed reference. A subVI node only allows you to call a specific VI that is statically
determined when you place the subVI node on the block diagram.

Interface Details

The interface of this node includes the following features:

  • Accessing inputs and outputs of the target VI—When you wire a strictly typed VI
    reference to the reference input of the Call By Reference node, the node displays
   the connector pane of the referenced VI. Wire data to the input terminals of the
   connector pane to pass the data to the called VI. Use the output terminals of the
   connector pane to access the data that the called VI returns.
  • Changing the connector pane of a wired Call By Reference node—To force the Call
   By Reference node to display a different connector pane after you change the
    reference input, right-click the node and select Adapt To Reference Input from the
    shortcut menu.


                                                    © National Instruments 2383

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2383 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2384 ordinal=2384 -->
## Functions

Functions

      Execution Details

       This node exhibits the following execution behaviors:

            • Synchronous execution—Like most block diagram objects, the Call By Reference
         node executes synchronously, preventing data flow from continuing along its
          output wires until the target VI finishes executing. If you want to run the target VI
          asynchronously while the block diagram beyond the VI call continues executing,
          use the Start Asynchronous Call node instead.
            • Performance overhead for calling a VI dynamically—The overhead for calling a VI
         by reference in the local application instance is negligible compared to the
          overhead of using a subVI node. LabVIEW requires significantly more overhead to
             call a VI by reference in a remote application instance.

      Alternative Ways to Call a VI

      The Call By Reference node is not the best choice for dynamically calling a VI in the
       following circumstances:

            • Asynchronous execution—If you want to call a target VI asynchronously, use the
            Start Asynchronous Call node instead of the Call By Reference node.
            • Opening the front panel of a target VI without running the VI—If you want to
         open the front panel of a target VI without causing the VI to run, use the Front
          Panel:Open method instead of the Call By Reference node.

      StartStart AsynchronousAsynchronous CallCall VIVI

        Starts an asynchronous call to the VI indicated by the reference input. Depending on
     how you prepare reference for asynchronous execution with the Open VI Reference
       function, you can either ignore the VI after calling it or collect its outputs at a later time
       with the Wait On Asynchronous Call node.


2384   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2384 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2385 ordinal=2385 -->
## Functions

Functions

Inputs/Outputs

   •      reference —
    reference is a reference to a target VI that you want to call asynchronously.
    The reference must meet the following criteria:
         • Be strictly typed
         • Be prepared for asynchronous execution by the Open VI Reference function using either the
        0x80 or 0x100 option flag. You can combine other option flags with these asynchronous
         options.
   •       error in (no error) —
    error in describes error conditions that occur before this node runs. This input provides
    standard error in functionality.
   •      reference out —
    reference out returns reference unchanged.
   •       error out —
    error out contains error information. This output provides standard error out functionality.

Interface Details

The interface of this node includes the following features:

  • Access to inputs of the target VI—When you wire a strictly typed VI reference to the
    reference input of the Start Asynchronous Call node, the node displays the input
    portion of the connector pane of the referenced VI. Wire data to the input terminals
    of the connector pane to pass the data to the target VI.
  • No access to outputs of the target VI—Because the purpose of the Start
   Asynchronous Call node is to start a VI call without waiting for it to complete, the
   outputs of the VI call are not available from the Start Asynchronous Call node. To
    collect the outputs of the target VI, use the Wait On Asynchronous Call node.

Execution Details

This node exhibits the following execution behaviors:

  • Serial or parallel execution—When you pass the same VI reference to multiple
    Start Asynchronous Call nodes, LabVIEW serializes the calls by default. To allow
    parallel execution, make the target VI reentrant and set the 0x40 option flag when
   you open its reference with the Open VI Reference function. Regardless of whether
   the calls execute serially or simultaneously, this node returns immediately,
    allowing dataflow to continue in the calling VI.

                                                    © National Instruments 2385

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2385 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2386 ordinal=2386 -->
## Functions

Functions

            •  If you include 0x40 as part of the options input, VI Server properties and
         methods do not modify called VI clones—If you set the 0x40 option flag when you
         open a reference to a target VI, the Start Asynchronous Call node starts a call to a
          clone of the referenced VI, not to the referenced VI itself. Therefore, if you call a VI
          Server property or method on the original reference that the Open VI Reference
           function returns, the effects of that property or method are not reflected in the VI
          clone that the Start Asynchronous Call node actually calls. To perform VI Server
           tasks such as opening or positioning the front panel on the VI that is actually
            called, you must call the property or method within the reentrant VI itself.
            • Does not require the user interface thread to be idle

     Examples

       Refer to the following example files included with LabVIEW.

            • labview\examples\Application Control\VI Server\
        Asynchronous Call By Reference\Asynchronous Call and
        Forget.vi
            • labview\examples\Application Control\VI Server\
        Asynchronous Call By Reference\Asynchronous Call and
        Collect.vi

     WaitWait OnOn AsynchronousAsynchronous CallCall VIVI

       Waits for an asynchronous call to a target VI to finish executing and then returns the
       outputs of the target VI. To use the Wait On Asynchronous Call node on a reference,
      you must include the 0x100 option flag as part of the options input of the Open VI
       Reference function when you open the reference. You also must call the target VI with
       the Start Asynchronous Call node.


      Inputs/Outputs

               •      reference —

2386   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2386 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2387 ordinal=2387 -->
## Functions

Functions

    reference is a reference to a target VI that you want to call asynchronously.
    The reference must meet the following criteria:
         •  Strictly typed
         • Prepared for asynchronous execution by the Open VI Reference function with the 0x100
        option flag. You can combine other option flags with this option.
         •  Called by a Start Asynchronous Call node elsewhere in the calling VI
   •       error in (no error) —
    error in describes error conditions that occur before this node runs. This input provides
    standard error in functionality.
   •      reference out —
    reference out returns reference unchanged.
   •       error out —
    error out contains error information. This output provides standard error out functionality.

Interface Details
The interface of this node includes the following features:

  • No access to inputs of the target VI—The Wait On Asynchronous Call node does
   not provide access to the inputs of the target VI. You can pass inputs to the target VI
   when you call it with a Start Asynchronous Call node.
  • Access to outputs of the target VI—When you wire a strictly typed VI reference to
   the reference input of the Wait On Asynchronous Call node, the node displays the
   output portion of the connector pane of the referenced VI. Use the output
    terminals of the connector pane to access the data returned by the target VI.

Execution Details
This node exhibits the following execution behaviors:

  • Ability to wait for only a specified amount of time—To specify how long this node
    waits for the associated asynchronous call to complete, right-click the node and
    select Timeout from the shortcut menu to display the Timeout for Wait On
   Asynchronous Call dialog box. Use this dialog box to specify how long the node
    waits on the corresponding VI call before returning a timeout error.
  • Ability to wait on multiple calls to the same VI reference—If you pass the same VI
    reference to multiple Start Asynchronous Call nodes, you cannot predict which
   Wait On Asynchronous Call node will detect the completion of each call. You can
    take precautions to match a Wait On Asynchronous Call Node to a specific VI call if
    necessary.

                                                    © National Instruments 2387

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2387 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2388 ordinal=2388 -->
## Functions

Functions

            • Does not require the user interface thread to execute

      Caveats and Recommendations

            • Can be called before the corresponding Start Asynchronous Call node
            • Every Start Asynchronous Call node that uses a 0x100 reference must have a
          corresponding Wait On Asynchronous node—If you start an asynchronous call to a
            call-and-collect reference, LabVIEW cannot free the reference until a Wait On
         Asynchronous Call node collects the outputs of the VI call to that reference.

     Examples

       Refer to the following example files included with LabVIEW.

            • labview\examples\Application Control\VI Server\
        Asynchronous Call By Reference\Asynchronous Call and
        Collect.vi
            • labview\examples\Application Control\VI Server\
        Asynchronous Call By Reference\Asynchronous Call and
        Collect (Using Option 0x40).vi

     ToTo MoreMore SpecificSpecific ClassClass FunctionFunction

       Typecasts a reference, such as a control or a type definition, to a more specific class or
        interface in the inheritance hierarchy.

       For example, if Class A inherits from Class B, a variable of type B can hold a value of
       type A. You can use the function to downcast from type B to type A. If the typecast is
        invalid, this function returns an error at run time.

      You can use the To More Specific Class function for casting any class hierarchy in
      LabVIEW, including VI Server refnums, .NET/ActiveX refnums, and LabVIEW classes or
        interfaces.


2388   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2388 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2389 ordinal=2389 -->
## Functions

Functions

Inputs/Outputs

   •       target class —

    target class is the class or interface to which you want to downcast reference.

    You can wire a class specifier constant or any wire of the target type to this input.
   •      reference —

    reference is the refnum or LabVIEW class or interface to downcast.

   •       error in —

    error in describes error conditions that occur before this node runs. This input provides
    standard error in functionality.

   •       specific class reference —

     specific class reference is the downcast reference.

       If the target class is incompatible with the reference, the function returns an error and specific
     class reference is Not A Refnum.
   •       error out —

    error out contains error information. This output provides standard error out functionality.


You can use the To More Specific Class function to manipulate the properties or
methods from a more specific class or interface than that of the reference. For
example, if you build an array of references to boolean, numeric, and string controls,
LabVIEW casts these references to the more generic Control class because an array can
contain only one data type, and each of these controls is a member of the Control
class. If you then want to manipulate the properties for only the boolean controls in
the array, you can create a reference to the array and use the To More Specific Class
function to downcast the array reference to the Boolean class.

Wire a VI refnum to reference and a Facade VI refnum to target class to downcast from
VI to Facade VI.

You also can use data value references to downcast classes. The To More Specific Class
function waits to execute until the reference is available for downcast. To downcast a
class or interface, wire the data value reference of the target class or interface to target

                                                    © National Instruments 2389

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2389 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2390 ordinal=2390 -->
## Functions

Functions

        class.

      Related Information

       Casting LabVIEW Classes

     Examples

       Refer to the following example files included with LabVIEW.

            • labview\examples\Application Control\VI Server\To More
        Specific Class\To More Specific Class.vi

     ToTo MoreMore GenericGeneric ClassClass FunctionFunction

       Typecasts a reference, such as a control or a type definition, to a more generic class or
        interface in the inheritance hierarchy.

       For example, if Class A inherits from Class B, the function upcasts a variable of type A
       to a variable of type B.

      You can use the To More Generic Class function for casting any class hierarchy in
      LabVIEW, including VI Server refnums, .NET/ActiveX refnums, and LabVIEW classes or
        interfaces.


      Inputs/Outputs

               •       target class —

             target class is the class or interface to which you want to upcast reference.

           You can wire a class specifier constant or any wire of the target type to this input.
               •      reference —

            reference is the refnum or LabVIEW class or interface to upcast.


2390   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2390 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2391 ordinal=2391 -->
## Functions

Functions

   •      generic class reference —

    generic class reference is the upcasted reference.

       If an error occurs, generic class reference is Not A Refnum.


This function does not have error in and error out parameters because LabVIEW can
determine at edit time whether you have wired the reference to a compatible target
class. If you wire the reference to an incompatible target class, the wire breaks and
you receive a Class conflict error.

You can use the To More Generic Class function to manipulate the properties or
methods from a more generic class or interface than that of the reference. For
example, you can wire an enum control reference to the To More Generic Class
function to upcast the reference to the Numeric class. You then can manipulate the
Numeric class properties of the control, but you no longer can access the specific
properties of the Enum class.

Wire a Facade VI refnum to reference and a VI refnum to target class to upcast from
Facade VI to VI.

Related Information

Casting LabVIEW Classes

ClassClass SpecifierSpecifier ConstantConstant

Selects the class of the output. You also can create a class specifier constant from a
control refnum control or terminal.

You can use the Class Browser window to create a class specifier constant for some VI
Server classes.

Use this constant with the To More Specific Class or To More Generic Class functions.
Since the value of the constant is always Not A Refnum, you cannot wire this
constant to the input of a Property Node.


                                                    © National Instruments 2391

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2391 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2392 ordinal=2392 -->
## Functions

Functions


       VIVI ServerServer ReferenceReference

       Returns a static VI reference to the current VI by default. You can reconfigure this
       reference to return a reference to the current application, to a control or indicator in
       the VI, or to a pane by clicking on the block diagram icon and choosing from the
       shortcut menu. You can use this reference to access the properties and methods for
       the associated VI, application, control, indicator, or pane. The VI Server Reference
      always returns a fully authenticated reference. Use caution when passing references to
       other VIs if you are concerned about password security.

      You also can right-click a front panel object or terminal and select Create»Reference
      from the shortcut menu to create a VI Server reference.

      To link the reference constant to the current application, VI, or a pane of the current VI,
        click the VI Server reference on the block diagram and select This Application, This VI,
       or Pane. You also can right-click the VI Server reference and select Link to»This
       Application, Link to»This VI, or Link to»Pane from the shortcut menu. To link the
       reference to a control or indicator within the VI, click or right-click the reference in the
     same way and then select the control or indicator to which you want to link from the
       shortcut menu.

      Use a Property Node or Invoke Node to access the properties and methods for the
       control or indicator using a VI Server reference.

           If the VI Server reference is associated with a control or indicator, you can right-click
       the VI Server reference and select Find Control or Find Indicator from the shortcut
     menu to find the associated control or indicator. You also can right-click and select
       Find»References to find the associated references. Although you can use VI Server
       references with Property Nodes to pass data, you can achieve better performance
      through other ways. Try wiring the data directly or using local or global variables
       instead before using VI Server references to pass data.

       Refer to Comparing References to compare VI Server references.

           Note If you place a VI Server reference on a Facade VI and select This VI, the


2392   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2392 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2393 ordinal=2393 -->
## Functions

Functions


         VI Server reference returns a reference of type Facade VI.


Inputs/Outputs

   •      This VI —


Examples

Refer to the following example files included with LabVIEW.

  • labview\examples\Application Control\VI Server\Control
   References\Control References.vi

CallCall ChainChain FunctionFunction

Returns the chain of callers from the current VI to the top-level VI. Element 0 of the call
chain array contains the name of the lowest VI in the call chain. Subsequent elements
are callers of the lower VIs in the call chain. The last element of the call chain array is
the name of the top-level VI.


Inputs/Outputs

   •        call chain —

     call chain is the chain of callers from the current VI to the top-level VI.

GetGet DragDrag DropDrop DataData FunctionFunction

Returns drag data from the current drag and drop operation. Only use this function

                                                    © National Instruments 2393

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2393 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2394 ordinal=2394 -->
## Functions

Functions

     when it is necessary to access the drag data, not just to examine the data type. If a drag
      and drop operation is not in progress, LabVIEW returns an error. If the data requested
         is unavailable, LabVIEW returns an error.


      Inputs/Outputs

               •      data name —

           data name is the user-defined name of the drag data that you want to retrieve. You also can use
            the built-in LabVIEW data types.

          LabVIEW Data Type   Definition
         LV_TEXT             String
         LV_TREE_TAG       String
                                   Array of a cluster that contains an array of strings in the item you are
                                 dragging (in order from left to right), an integer that represents the glyph
         LV_TREE_ITEMS    index associated with the item from which you are dragging data, and an
                                    integer that represents the indent level of the item from which you are
                                   dragging.
                                   Array of a cluster that contains an array of strings in the item you are
         LV_LISTBOX_ITEMS dragging (in order from left to right) and an integer that represents the
                                 glyph index associated with the item from which you are dragging data.
         LV_PATH            Path

               •      type —

           type is the data type of the drag data you want to retrieve.

               •       error in —

             error in describes error conditions that occur before this node runs. This input provides
            standard error in functionality.

               •      data —

           data is the drag data returned from LabVIEW. data can adapt to any data type.

               •       error out —

2394   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2394 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2395 ordinal=2395 -->
## Functions

Functions


    error out contains error information. This output provides standard error out functionality.


Examples

Refer to the following example files included with LabVIEW.

  • labview\examples\Structures\Event Structure\Drag and Drop
   - Passing Custom Drag Data.vi

StopStop FunctionFunction

Stops the VI in which it executes, just as if you clicked the Abort Execution button on
the toolbar. Before you call this function with a TRUE input, be sure to complete all
final tasks for the VI first, such as closing files, setting safe values for devices being
controlled, and so on.

If you wired the input, stop occurs only if the input value is TRUE. The default is to stop
as soon as the node that is currently executing finishes.


Inputs/Outputs

   •      stop? (T) —

    stop? is the Boolean value that determines if the VI stops.

       If you wire an error cluster to stop? and an error occurs, the error cluster passes a TRUE value to
    the function.

If you need to abort execution of all VIs in a hierarchy from the block diagram, you can
use this function, but you must use it with caution. If you put this function in a subVI,
you should make its behavior clear to other users of the VI because this function
causes their VI hierarchies to abort execution.

In general, avoid using this function when you have a built-in termination protocol in a

                                                    © National Instruments 2395

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2395 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2396 ordinal=2396 -->
## Functions

Functions

         VI. For example, I/O operations should be performed in While Loops so that the VI can
       terminate the loop on an I/O error. Also, consider using a front panel stop button
      Boolean control to terminate the loop at the request of the user rather than using this
       function.

      QuitQuit LabVIEWLabVIEW FunctionFunction

       Stops all executing VIs and ends the current instance of LabVIEW.

       This function shuts down only LabVIEW. The function does not affect other
       applications. The function stops all running VIs the same way the Stop function does. If
       there is any unsaved work in memory, you will be prompted to save. Selecting Cancel
        will abort the quit.


      Inputs/Outputs

               •       quit? (T) —

                    If quit? is TRUE (default), LabVIEW quits.

                    If you wire an error cluster to quit? and an error occurs, the error cluster passes a TRUE value to
            the function.

      SetSet ControlControl ValuesValues byby IndexIndex FunctionFunction

       Sets values to the controls for the VI you reference. This function offers better
      performance than VI Server objects that write to the terminal of a front panel control,
      such as using the Value property in the Control class. However, this function requires
      more advanced application design than other methods for setting control values.


2396   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2396 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2397 ordinal=2397 -->
## Functions

Functions

Inputs/Outputs

   •       VI Refnum —

     VI Refnum specifies a reference to the VI for which you want to set multiple control values. You
    can wire a strict or non-strict reference to this input. The default is a reference to the current VI.

   •      control indexes —

    control indexes specifies the indexes of the front panel controls for which you want to set
     values.

    Use the Control Index property in the Control class to retrieve control indexes.
   •      data values —

    data values specifies the values to write to the controls. The default is a variant, but you also can
     specify the data type for the values you want to write to the control. To specify a single control,
    wire a scalar index to control indexes and wire a single value to data values.

   •       error in (no error) —

    error in describes error conditions that occur before this node runs. This input provides
    standard error in functionality.

   •       error out —

    error out contains error information. This output provides standard error out functionality.


The Set Control Values by Index function requires that the VI for which you want to set
control values is running or in run mode. Furthermore, the controls for which you want
to set values must have terminals on the block diagram.

      Note Because controls nested within clusters or arrays do not have
        terminals on the block diagram, you cannot set values for those controls.

This function iterates over the length of the shorter of the two arrays you wire to
control indexes and data values. The function attempts to set all values and does not
stop on the first error. If an error occurs for multiple indices or values, LabVIEW reports
only the first error.


                                                    © National Instruments 2397

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2397 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2398 ordinal=2398 -->
## Functions

Functions

      Application Design Considerations

      Use the following recommendations to obtain the best performance when you set
       control values with this function:

            • Retrieve the index of a control only once during an initialization section of an
           application.
            • To set control values for the current VI, leave VI Refnum unwired.
            • Set multiple values in a single call to minimize overhead.
            • To set values for a group of controls that have the same data type, wire an array of
           that data type to data values. For example, wire an array of 64-bit double-precision
            floating point numbers to data values to update a large group of numeric controls
         whose representation is 64-bit double-precision, floating point.

     GetGet ControlControl ValuesValues byby IndexIndex FunctionFunction

       Gets values from the controls for the VI you reference. This function offers better
      performance than VI Server objects that read from the terminal of a front panel
        control, such as using the Value property in the Control class. However, this function
       requires more advanced application design than other methods for getting control
       values.


      Inputs/Outputs

               •       VI Refnum —

             VI Refnum specifies a reference to the VI from which you want to get control values. You can wire
           a strict or non-strict reference to this input. The default is a reference to the current VI.

               •      control indexes —

            control indexes specifies an array of indices of front panel controls for which you want to get
             values.

           Use the Control Index property in the Control class to retrieve control indexes.
               •       error in (no error) —

2398   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2398 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2399 ordinal=2399 -->
## Functions

Functions


    error in describes error conditions that occur before this node runs. This input provides
    standard error in functionality.

   •      data values —

    data values returns the control values.

   •       error out —

    error out contains error information. This output provides standard error out functionality.


The Get Control Values by Index function requires that the VI from which you want to
get control values is running or in run mode. Furthermore, the controls for which you
want to get values must have terminals on the block diagram.

      Note Because controls nested within clusters or arrays do not have
        terminals on the block diagram, you cannot get values for those controls.

Application Design Considerations

Use the following recommendations to obtain the best performance when you get
control values with this function:

  • Retrieve the index of a control only once during an initialization section of an
    application.
  • To get control values from the current VI, leave VI Refnum unwired.

PalettePalette EditingEditing

You can use the Palette Editing VIs to edit the Controls or Functions palette set
programmatically.

      Note The LabVIEW Run-Time Engine does not support the Palette Editing
         VIs. Error -4406 occurs if you call the Palette Editing VIs in the LabVIEW
       Run-Time Engine.


                                                    © National Instruments 2399

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2399 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2400 ordinal=2400 -->
## Functions

Functions


         Palette                      Description        Object

         Write                      Writes palette data to a palette file (.mnu).         Palette

       Read                        Extracts data from a palette file (.mnu).         Palette


                    Updates the Controls and Functions palette set programmatically.
         Refresh
         Palettes      This method is similar to the Save Changes button on the Edit Controls and
                     Functions Palette Set dialog box.


       WriteWrite PalettePalette

       Writes palette data to a palette file (.mnu).

           Caution If you use this VI to edit palettes in the labview\menus
                directory, LabVIEW does not save the edits in a copy of the original palettes.
                After you edit the palettes, you cannot revert to the original palettes.


      Inputs/Outputs

               •      application reference —

            application reference is a reference to a target. The default is the local computer. If the target is
            not the local computer, you must wire the application reference input to edit the Controls and


2400   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2400 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2401 ordinal=2401 -->
## Functions

Functions


  Functions palette set.

  Create a project with the target you want to reference. Use the Project:Projects[] property to
  obtain the target reference from the project. When you have the target reference, use the
  Application property to obtain the application reference.

•       palette path —

  palette path is the path, including the filename, of the palette file (.mnu). The filename must
  have a.mnu extension.

•       palette type —

  palette type determines whether the palette file (.mnu) contains data for the Controls palette or
  Functions palette.

  -2              Controls
  -1             Functions

•       palette data —

  palette data contains the data this VI writes to the palette file (.mnu).

      •      display name —

      display name is the name of the palette.

          If the selected palette format is Category (Standard) or Category (Icons and Text) and you
     move the cursor over the palette icon, display name appears in a tip strip above the palette
       icon. If the selected palette format is Icons or Icons and Text and you move the cursor over
      the palette icon, display name appears at the top of the palette. If the selected palette
      format is Text or Tree, display name appears as text to identify the palette.

      •      view format —

      view format specifies the appearance of the palette items within the selected palette view.
      You can select Icons, Text, or Icons and Text.

      0      Icons
      1      Text


                                                   © National Instruments 2401

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2401 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2402 ordinal=2402 -->
## Functions

Functions


               2      Icons and Text

                     •       palette width —

                 palette width specifies how many palette items can fit in one palette row. palette width
              must be greater than or equal to 0. If palette width is less than 0, the VI returns an error.

                     •      items —

               items describes the palette items or subpalettes on the palette.

                           •      item path —

                   item path is the path to the palette item or subpalette. item path accepts all type of
                      paths. To create an empty slot on the palette, leave item path empty. If item path is
                   empty, LabVIEW ignores any additional data in the items cluster.

                 An item is not added to the palette if the item does not exist on your disk. If you still
                  want to add the item, first ensure that the path provided is valid, and then append
               <<file not found>> to the end of the item path.

                           •       library path —

                       library path (.lvlib) is the path of the library that contains the palette item.

                                 If the library does not exist on your disk, the item is added as a non-library item. If you
                               still want to add the library item, first ensure that the path provided is valid, and then
                 append <<file not found>> to the end of the library path.

                           •      use default lvlib palette —

                   use default lvlib palette configures the VI to use the default project library menu.
                  LabVIEW ignores this option unless library path (.lvlib) contains a valid path.

                           •      short name —

                    short name is the abbreviated name of the palette item or subpalette. If the selected
                   view is Category (Icons and Text) or Icons and Text, short name appears below the
                      palette item or subpalette.


2402   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2402 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2403 ordinal=2403 -->
## Functions

Functions


      •      place VI contents —

      place VI contents places the VI contents on the block diagram if TRUE. If place VI
      contents is FALSE, this VI places only the VI icon on the block diagram.

      •      hide synchronized item —

      hide synchronized item hides the synchronized item if TRUE. hide synchronized item
         is valid only if you synchronize this palette with a directory using the synchronize with
       directory input.

      •      reserve spot for synch item —

      reserve spot for synch item reserves a spot on the palette for the synchronized item.
       This input is valid only if you synchronize this palette with a directory using the
      synchronize with directory input.

      •      configure when placing VI contents —


•      256 color icon —

  256 color icon is the 8-bit color icon that signifies the palette item or subpalette.

•    B&W color icon —

 B&W color icon is the black-and-white icon that signifies the palette item or subpalette.

•      help information —

  help information determines the help file to which the Context Help window links.

      •      help tag —

      help tag contains the HTML filename or index keyword of the file you want to link to
      from the Context Help window.

      •      help file path —

      help file path contains the path or symbolic path to the file you want to link to from the


                                                © National Instruments 2403

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2403 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2404 ordinal=2404 -->
## Functions

Functions


                    Context Help window. help file path is either an HTML file or a compiled help file.


                     •       palette description —

                 palette description contains the text that appears in the Context Help window if you move
                the cursor over the subpalette icon in the Controls or Functions palette or if you move the
                 cursor over an open area of the subpalette.

                     •      synchronize information —

                synchronize information contains the synchronization information for the palette file
                (.mnu).

                           •    —

                    synchronize with directory indicates whether the palette file (.mnu) synchronizes with
                  a directory.

                           •      synchronize directory path —

                    synchronize directory path indicates the directory path to which LabVIEW
                     synchronizes the palette file (.mnu). If a palette synchronizes with a directory, the
                    items you add or delete from the directory automatically appear or disappear on the
                       palette.

                    synchronize directory path accepts any type of path when writing the palette file. This
                        VI ignores synchronize directory path if synchronize with directory is FALSE.


               •       error in (no error) —

             error in describes error conditions that occur before this node runs. This input provides
            standard error in functionality.

               •       error out —

             error out contains error information. This output provides standard error out functionality.


2404   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2404 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2405 ordinal=2405 -->
## Functions

Functions

If you have not customized the data in the palette file, use the Read Palette VI to extract
data to the palette file. After you edit the palette data, use the Refresh Palettes method
to update the palettes programmatically.

      Note LabVIEW loads a separate palette set for each target. If you write to a
        palette set for a specific target without wiring the correct reference to the
        target using application reference, the path this VI stores in the palette file
       might be incorrect.

ReadRead PalettePalette

Extracts data from a palette file (.mnu).

Use the Write Palette VI to write data to the palette file. After you edit the palette data,
use the Refresh Palettes method to update the palettes programmatically.


Inputs/Outputs

   •      application reference —

    application reference is a reference to a target. The default is the local computer. If the target is
    not the local computer, you must wire the application reference input to edit the Controls and
    Functions palette set.

    Create a project with the target you want to reference. Use the Project:Projects[] property to
    obtain the target reference from the project. When you have the target reference, use the
    Application property to obtain the application reference.

   •       palette path —

    palette path is the path, including the filename, of the palette file (.mnu). The filename must
    have a.mnu extension.

   •       palette type —


                                                    © National Instruments 2405

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2405 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2406 ordinal=2406 -->
## Functions

Functions


             palette type determines whether the palette file (.mnu) contains data for the Controls palette or
            Functions palette.

              -2              Controls
              -1             Functions

               •       error in (no error) —

             error in describes error conditions that occur before this node runs. This input provides
            standard error in functionality.

               •      duplicate palette path —

            duplicate palette path is the path of the palette file (.mnu) from which the VI reads data.

               •       palette data —

             palette data contains the data the VI reads from the palette file (.mnu).

                     •      display name —

                 display name is the name of the palette.

                           If the palette view format is Category (Standard) or Category (Icons and Text) and you
             move the cursor over the palette icon, display name appears in a tip strip above the palette
                  icon. If the selected palette view format is Icons or Icons and Text and you move the cursor
                over the palette icon, display name appears at the top of the palette. If the selected palette
               view format is Text or Tree, display name appears as text to identify the palette.

                     •      view format —

               view format specifies the appearance of the palette items within the selected palette view.

               0      Icons
               1      Text
               2      Icons and Text

                     •       palette width —

                 palette width specifies how many palette items can fit in one palette row. palette width


2406   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2406 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2407 ordinal=2407 -->
## Functions

Functions


  does not have a maximum value. If palette width is less than 0, the VI returns an error.

•      items —

  items describes the items or subpalettes on the palette.

      •      item path —

      item path is the path to the palette item or subpalette. item path returns an absolute
      path when the VI reads the palette file.

          If the item does not exist on your disk, the path returns appended with <<file not
     found>>. When the full path is not available, the path returns the file name appended
      with <<file not found>>. If the palette links to a directory, item path becomes
     FolderName/dir.mnu. If dir.mnu does not exist on your disk, the path returns
     appended with <<file not found>>. If the palette item is an empty slot, item
      path is empty.

          If the palette contains functions or built-in LabVIEW controls and indicators, item path
       returns a generic message in the form BUILT_IN_FUNC_**_**_**_***. To
      prevent undefined behavior, do not manipulate the generic message the VI returns.

      •       library path —

       library path (.lvlib) is the path of the library that contains the palette item. If the library
      item does not exist on your disk, the path returns appended with <<file not
     found>>.

      •      use default lvlib palette —

      use default lvlib palette configures the VI to use the default project library menu.
      LabVIEW ignores this option unless library path (.lvlib) contains a valid path.

      •      short name —

      short name is the abbreviated name of the palette item or subpalette. If the selected
      view is Category (Icons and Text) or Icons and Text, short name appears below the
       palette item or subpalette. If the item does not have an abbreviated name, the VI
       returns an empty string.


                                                © National Instruments 2407

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2407 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2408 ordinal=2408 -->
## Functions

Functions


                           •      place VI contents —

                    place VI contents places the contents of the VI on the block diagram if TRUE. If place VI
                    contents is FALSE, this VI places only the VI icon on the block diagram.

                           •      hide synchronized item —

                    hide synchronized item hides the synchronized item if TRUE. If you use the Edit
                     Controls and Functions Palette Set or the Palette Editing VIs to create a palette file,
                   then hide synchronized item returns FALSE unless synchronize with directory is TRUE.

                           •      reserve spot for synch item —

                    reserve spot for synch item reserves a spot on the palette for the synchronized item.

                                 If you use the Edit Controls and Functions Palette Set or the Palette Editing VIs to create
                  a palette file, then reserve spot for synch item returns FALSE unless synchronize with
                     directory is TRUE.

                           •      configure when placing VI contents —


                     •      256 color icon —

              256 color icon is the 8-bit color icon that represents the palette item or subpalette.

                     •    B&W color icon —

           B&W color icon is the black-and-white icon that represents the palette item or subpalette.

                     •      help information —

                help information determines the help file to which the Context Help window links.

                           •      help tag —

                    help tag contains the HTML filename or index keyword of the file you want to link to
                   from the Context Help window.

                           •      help file path —


2408   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2408 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2409 ordinal=2409 -->
## Functions

Functions


            help file path contains the path or symbolic path to the file you want to link to from the
            Context Help window. help file path is either an HTML file or a compiled help file.


         •       palette description —

         palette description contains the text that appears in the Context Help window if you move
        the cursor over the subpalette icon in the Controls or Functions palette or if you move the
         cursor over an open area of the subpalette.

         •      synchronize information —

        synchronize information contains the synchronization information for the palette file
        (.mnu).

                •    —

            synchronize with directory indicates whether the palette file (.mnu) synchronizes with
           a directory.

                •      synchronize directory path —

            synchronize directory path indicates the directory path to which LabVIEW
             synchronizes the palette file (.mnu). If a palette synchronizes with a directory, the
            items you add or delete from the directory automatically appear or disappear on the
              palette.

            synchronize directory path returns an absolute path when this VI reads the palette file.
             This VI ignores synchronize directory path if synchronize with directory is FALSE.


   •       error out —

    error out contains error information. This output provides standard error out functionality.


If you read from a palette set for a specific target without wiring the correct reference
to the target using the application reference input, the paths the VI returns might be
incorrect.


                                                    © National Instruments 2409

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2409 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2410 ordinal=2410 -->
## Functions

Functions

     Examples

       Refer to the following example files included with LabVIEW.

            • labview\examples\Application Control\Palette Editing API\
        Palette Editing API.lvproj

      RefreshRefresh PalettesPalettes

      Updates the Controls and Functions palette set programmatically.

       This method is similar to the Save Changes button on the Edit Controls and Functions
       Palette Set dialog box.

       Refresh Palettes is an Invoke Node with a LabVIEW class of App.


      Inputs/Outputs

               •      reference —

               •       error in (no error) —

               •       Palettes:Refresh —

               •      reference out —

               •       error out —

               •       Palettes:Refresh —

    CPUCPU InformationInformation

      Use the CPU Information functions to obtain information on the characteristics of a
      computer or target.

2410   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2410 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2411 ordinal=2411 -->
## Functions

Functions


 Palette Object                     Description

 CPU Information Function          Returns the processor characteristics of the computer.

 Number of Cache Levels Function   Returns the number of cache levels the computer contains.

 Data Cache Size Function           Returns the characteristics of the cache level you specify.

CPUCPU InformationInformation FunctionFunction

Returns the processor characteristics of the computer.


Inputs/Outputs

   •      # of logical processors —

    # of logical processors is the number of processing units.

          Note This function returns the total number of logical processors, which might be
               different from the number currently available to LabVIEW. For example, this function
             includes disabled processors in # of logical processors.

   •      # of packages —

    # of packages is the number of packages, or chips. For example, a single hyperthreaded
    processor can have two or more logical processors, and a machine with two quad-core
    processors has eight logical processors.

   •      # of cores per package —

    # of cores per package is the number of cores each package contains.

   •      # of logical processors per core —


                                                    © National Instruments 2411

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2411 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2412 ordinal=2412 -->
## Functions

Functions


           # of logical processors per core is the number of processing units each core contains.


      You can use the following properties to programmatically obtain processor
        characteristics from a LabVIEW application running on a remote computer or target
      about the system on which the application runs.

            • Application:Target:Number of Cores per Package
            • Application:Target:Number of Logical Processors
            • Application:Target:Number of Logical Processors per Core
            • Application:Target:Number of Packages

       National Instruments recommends that you use the CPU Information function rather
      than these properties to return information from the local computer.

     NumberNumber ofof CacheCache LevelsLevels FunctionFunction

       Returns the number of cache levels the computer contains.


      Inputs/Outputs

               •      # of cache levels —

           # of cache levels is the number of cache levels.


      DataData CacheCache SizeSize FunctionFunction

       Returns the characteristics of the cache level you specify.


2412   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2412 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2413 ordinal=2413 -->
## Functions

Functions

Inputs/Outputs

   •      cache level (2) —

    cache level is the cache level for which to return information. The default is 2.

   •       total cache size (in bytes) —

     total cache size (in bytes) is the size of the cache for the cache level you specify.

   •      cache entry size (in bytes) —

    cache entry size (in bytes) is the size of entries for the cache level you specify.


You can use the Application:Target:Data Cache Entry Sizes and Application:Target:Data
Cache Sizes properties to programmatically obtain information from a LabVIEW
application running on a remote computer or target about the system on which the
application runs.

National Instruments recommends that you use the Data Cache Size function rather
than these properties to return information from the local computer.

MemoryMemory ControlControl

Use the Memory Control VIs and functions to improve LabVIEW memory performance.


 Palette
              Description
 Object

 New Data
 Value        Creates a reference to data that you can use to transfer and access the data in a
 Reference     serialized way.
 Function

 Delete Data
            Removes LabVIEW access to the data that the data value reference or the external
 Value
             data value reference points to. This function deletes the reference but leaves the data
 Reference
                 intact. Memory leakage might occur if you do not delete the reference.
 Function

                                                    © National Instruments 2413

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2413 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2414 ordinal=2414 -->
## Functions

Functions


         Palette                      Description
        Object

        Get Memory  Returns the amount of physical memory that the LabVIEW process uses. This VI also
         Status        returns the status of system-wide memory usage.

       Swap Values  Places the value of the y input into the x' output and the value of the x input into the
         Function      y' output without allocating memory to perform the operation.

                      Places the value of Input into a new memory location and returns the value in        Always Copy                     Output. Use this function to control the outcome of the LabVIEW compiler buffer         Function                        allocation process.

        Request
         Deallocation  Deallocates unused memory after the VI that contains this function runs.
         Function

     NewNew DataData ValueValue ReferenceReference FunctionFunction

       Creates a reference to data that you can use to transfer and access the data in a
        serialized way.


      Inputs/Outputs

               •      data value —

           data value is the data you want the reference to point to. Use the In Place Element structure to
              alter the data and the Delete Data Value Reference function to recover the data.

               •       error in (no error) —

             error in describes error conditions that occur before this node runs. This input provides
            standard error in functionality.

               •      data value reference —

           data value reference is the reference that points to the data.


2414   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2414 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2415 ordinal=2415 -->
## Functions

Functions

   •       error out —

    error out contains error information. This output provides standard error out functionality.


Data value references contain the same data type of the data they point to. Do not type
cast data value references. However, you can upcast or downcast data value references
that contain LabVIEW classes.

DeleteDelete DataData ValueValue ReferenceReference FunctionFunction

Removes LabVIEW access to the data that the data value reference or the external data
value reference points to. This function deletes the reference but leaves the data
intact. Memory leakage might occur if you do not delete the reference.

      Note You must use this function to delete an external data value reference
      and release the associated memory to the device driver that supports and
       provides the reference; otherwise, the hardware does not have access to that
        buffer space.


Inputs/Outputs

   •      data value reference —

    data value reference points to the data you want to recover. LabVIEW deletes this reference after
    you recover the data. Use the New Data Value Reference function to create a data value
     reference.

   •       error in (no error) —

    error in describes error conditions that occur before this node runs. With the following
    exception, this input provides standard error in functionality.

    This node runs normally evenifan error occurred before this node runs.

   •      data value —

                                                    © National Instruments 2415

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2415 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2416 ordinal=2416 -->
## Functions

Functions


           data value is the data the reference points to.

               •       error out —

             error out contains error information. This output provides standard error out functionality.


      To avoid data copies, leave the data value output of this function unwired when
      working with external data value references.

      GetGet MemoryMemory StatusStatus

       Returns the amount of physical memory that the LabVIEW process uses. This VI also
       returns the status of system-wide memory usage.


      Inputs/Outputs

               •       error in (no error) —

             error in describes error conditions that occur before this node runs. This input provides
            standard error in functionality.

               •       total physical memory —

              total physical memory returns the total amount of physical memory, in kilobytes, on the
            system.

               •     memory allocated for LabVIEW —

         memory allocated for LabVIEW returns the memory size, in kilobytes, allocated for the LabVIEW
             process.

               •       free physical memory —

             free physical memory returns the amount of physical memory, in kilobytes, on the system that
                is not used.


2416   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2416 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2417 ordinal=2417 -->
## Functions

Functions

   •       error out —

    error out contains error information. This output provides standard error out functionality.


SwapSwap ValuesValues FunctionFunction

Places the value of the y input into the x' output and the value of the x input into the y'
output without allocating memory to perform the operation.


Inputs/Outputs

   •      y —

    y is any data to place in the memory location of the x input.

   •       ?(T) —

     ?(T) specifies whether you want to swap the values of the x and y inputs.

   •      x —

    x is any data to place in the memory location of the y input.

   •       y' —

     y' returns the data from the x input.

   •        x' —

     x' returns the data from the y input.


Because this function swaps values without copying data from one place to another,
the function does not consume memory to complete the swap operation. National
Instruments recommends that you use this function to increase value swapping speed
and improve memory utilization efficiency, especially when the data size is large. Visit
ni.com/info and enter the Info Code extnfw for more information about using this

                                                    © National Instruments 2417

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2417 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2418 ordinal=2418 -->
## Functions

Functions

       function.

      AlwaysAlways CopyCopy FunctionFunction

       Places the value of Input into a new memory location and returns the value in Output.
      Use this function to control the outcome of the LabVIEW compiler buffer allocation
       process.

      Use this function when you want to control the LabVIEW compiler in order to produce
      a different result regarding its buffer allocations.


      Inputs/Outputs

               •      Input —

            Input is any data to copy to a new location in memory.

               •      Output —

           Output returns the data from Input that LabVIEW copied to a new location in memory.


      RequestRequest DeallocationDeallocation FunctionFunction

       Deallocates unused memory after the VI that contains this function runs.

      Use this function only for advanced performance optimizations. Deallocating unused
     memory can improve performance in some cases. However, aggressively deallocating
     memory can cause LabVIEW to reallocate space repeatedly rather than reusing an
        allocation. Use this function if your VI allocates a large amount of data but never
       reuses that allocation.


2418   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2418 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2419 ordinal=2419 -->
## Functions

Functions

Inputs/Outputs

   •       flag —

       If flag is TRUE, this function deallocates memory after the VI that contains this function runs.


When a top-level VI calls a subVI, LabVIEW allocates a data space of memory in which
that subVI runs. When the subVI finishes running, LabVIEW usually does not deallocate
the data space until the top-level VI finishes running or until the entire application
stops, which can result in out-of-memory conditions and degradation of performance.
Use this function to deallocate the data space immediately after the VI completes
execution.

Place the Request Deallocation function in the subVI you want to deallocate memory
for. When you set the flag Boolean input to TRUE, LabVIEW reduces memory usage by
deallocating the data space for the subVI.

VIVI ScriptingScripting

You can use the VI Scripting VI and functions to create, edit, and run VIs
programmatically.

You must enable VI Scripting to use the VI Scripting VI and functions.


 Palette
             Description
 Object

 New VI
             Creates and returns a reference to a new VI.
 Function

 Open VI
 Object
           Opens a reference to the object whose label you specify with the name/order input.
 Reference
 Function

 New VI     Adds a new VI object to the front panel or block diagram of the VI specified by owner
 Object     refnum and returns a reference to the new object. VI objects include any controls,

                                                    © National Instruments 2419

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2419 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2420 ordinal=2420 -->
## Functions

Functions


         Palette                     Description
        Object

                    nodes, calls to subVIs, and user-defined controls that you can create in the LabVIEW         Function                      editing environment.

      New VI                     This cluster provides a way to define the location input of the New VI Object function
         Object                    as an offset from another object. Refer to the New VI Object Location Argument
         Offset                  example VI in the labview\examples\Application Control\VI
       From
                Scripting\Creating Objects directory for a visual comparison of the three        Referenced
                     acceptable types of arguments for the location input.         Object


                    Searches a target for objects of a particular type and returns an array of references to         Traverse                    those objects. The target can be a front panel, a block diagram, or any object that can
          for                     contain other objects, such as a For Loop, a cluster, or a user-defined control. This VI        GObjects                      also recursively finds objects nested within other container objects.


        Get                    Returns a string containing the label text of the object you specify and a reference to        GObject                      that label. This VI returns the same value as the Label.Text property.
         Label


                    Returns an array of class names, in descending order of inheritance, from the top-level
        Get Class                       class name to the class name you specify. For example, if you specify WhileLoop in
         Hierarchy                     Class Name this VI returns the array [Generic, Gobject, Node,        from Class
                Structure, Loop, WhileLoop]. This VI works for any valid class name,      Name
                      regardless of whether you have scripting or private functionality turned on or off.


     NewNew VIVI FunctionFunction

       Creates and returns a reference to a new VI.


2420   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2420 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2421 ordinal=2421 -->
## Functions

Functions

Inputs/Outputs

   •      type specifier VI Refnum (for type only) —

    type specifier VI Refnum (for type only) determines the data type of the new VI that this
    function returns in vi refnum. If you wire a reference to a pre-existing VI to this parameter,
    LabVIEW assigns the data type of that VI to the new VI. Note that LabVIEW does not copy the
    contents of the pre-existing VI into the new VI.

       If you do not wire data to this input, LabVIEW returns a Generic VI reference for vi refnum.

   •      options —

    options is a bit set that specifies two optional characteristics of the new VI reference that this
    function creates. The default is 0x0.

    options can be a combination of the following values.

        Records VI Server modifications to the new VI created by this function. When you modify
         the new VI using VI Server properties or methods, an asterisk (*) appears by the title of the
    0x01          VI in its title bar, the list of open VIs displayed in the Window menu, and the All Windows
         dialog box. The VI must be in edit mode for LabVIEW to record the modifications.
        Prompts user at close. When you attempt to close vi refnum after making changes, LabVIEW    0x04        prompts you to save before closing the VI.

   •      application refnum —

    application refnum is a reference to the LabVIEW application instance in which you want this
    function to create the new VI. By default, the function creates the new VI in the same application
    instance that called the New VI function. If you wire a reference to a remote application instance
    to application refnum, LabVIEW creates the new VI in the remote application instance.

   •      template —

    template is a path to a template VI whose contents you want LabVIEW to copy into the new VI
    that this function creates.

   When you create a new VI from a template by wiring a path to the template input, you avoid the
    need to create each template object individually in the new VI. You can modify small parts of the
    code that was copied from the template into the new VI to create a customized version of the
    template. To make modifications, you must obtain references to objects in the copied code.
    Then you can set properties or invoke methods to change the objects.

   •        vi type (standard vi) —

                                                    © National Instruments 2421

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2421 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2422 ordinal=2422 -->
## Functions

Functions


              vi type specifies the exact type of VI that this function returns as vi refnum. vi type must be at
              least as specific as type specifier VI Refnum (for type only).

           0    invalid VI type
           1    Standard VI (default)
           2    Control VI
           3    Global VI
           4    Polymorphic VI
           5    Configuration VI
           6   SubSystem
           7    Facade VI
           8   Method VI
           9    Statechart Diagram VI

               •       error in (no error) —

             error in describes error conditions that occur before this node runs. This input provides
            standard error in functionality.

               •      password —

           password is the password for the VI specified by the template parameter. If template is not
           password protected, LabVIEW ignores password. If template is password protected but you do
            not wire password, LabVIEW copies only the parts of the template VI that are not password
            protected into the new VI.

               •        vi refnum —

              vi refnum is a reference to the newly created VI. If LabVIEW fails to create a new VI, vi refnum
             returns Not A Refnum.

               •       error out —

             error out contains error information. This output provides standard error out functionality.


      By default, this function does not show the front panel or block diagram of the VI that
          it creates. Although you can inspect or modify the new VI without showing the front
       panel or block diagram, you can use the following VI properties and method to display
      and position the new VI:


2422   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2422 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2423 ordinal=2423 -->
## Functions

Functions

  • Front Panel:Open
  • Front Panel Window:Window Bounds
  • Block Diagram Window:Open
  • Block Diagram Window:Window Bounds
  • Block Diagram Window:Origin

OpenOpen VIVI ObjectObject ReferenceReference FunctionFunction

Opens a reference to the object whose label you specify with the name/order input.


Inputs/Outputs

   •        vi object class —

     vi object class indicates the class of object whose reference you wish to obtain. To specify a class
     type, wire a class specifier constant to this input. A class specifier constant displays a
     hierarchical menu that contains the classes of all of the objects in LabVIEW. You can navigate this
    hierarchy to find the class of the object you need to reference.

    This function also uses vi object class to determine the type of reference returned by object
    refnum. For example, if you wire a Boolean-typed Class Specifier Constant to vi object class, the
    returned object refnum changes to a Boolean reference.

   •     owner refnum —

   owner refnum is a reference to the owner of the object whose reference you want to obtain. The
    owner must be a front panel, a cluster, a block diagram, or a structure diagram. For example, to
    obtain a reference for a control on the front panel, wire a reference to the front panel to owner
    refnum. Likewise, to obtain a reference for an object inside a For Loop, wire a reference to the
    diagram of the For Loop to owner refnum.

   •      name/order —

    name/order indicates the object whose reference you want to obtain. name/order must match
    the label of the desired object. If you are obtaining the reference for an object within a cluster,
    you can use an array of strings that contain the names of the container hierarchy.


                                                    © National Instruments 2423

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2423 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2424 ordinal=2424 -->
## Functions

Functions

               •       error in (no error) —

             error in describes error conditions that occur before this node runs. This input provides
            standard error in functionality.

               •      object refnum —

            object refnum returns a reference to the object that matches both the class specified by vi
            object class and the label specified by name/order. This reference is of the class specified by vi
            object class.

               •       error out —

             error out contains error information. This output provides standard error out functionality.


      Use the Open VI Object Reference function to obtain a reference to any labeled object
        in a target VI. To obtain a reference to an object whose label is not known, you must
       navigate to the object from a known reference or use the Traverse for GObjects VI
       instead.

           Note You cannot use the Open VI Object Reference function to open a
               reference to a pane on the front panel. Instead, use the Traverse for GObjects
                 VI or the Pane[] property to return an array of references to all the panes on
              the front panel, and then find the appropriate reference by the name of the
              pane.

       Block diagram objects do not display a label by default. Because the Open VI Object
       Reference function uses the label to locate the desired object, you must display the
       label of an object at least once before the function can find the object. You can display
       the label of any block diagram object by selecting Visible Items»Label from the
       shortcut menu of the object.

           If two objects in the target code have the same label, Open VI Object Reference
       returns a reference to only one of the two objects. To predictably obtain the desired
       object reference, use unique labels for objects of interest in target code.

      The Open VI Object Reference function does not search nested objects within the
      owner. For example, if you specify a block diagram to be the owner of the object you


2424   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2424 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2425 ordinal=2425 -->
## Functions

Functions

want to find, the Open VI Object Reference function does not search inside of For
Loops on that block diagram. To use the Open VI Object Reference function to obtain a
reference to an object within a For Loop, you must specify the relevant For Loop to be
the owner of the object.

NewNew VIVI ObjectObject FunctionFunction

Adds a new VI object to the front panel or block diagram of the VI specified by owner
refnum and returns a reference to the new object. VI objects include any controls,
nodes, calls to subVIs, and user-defined controls that you can create in the LabVIEW
editing environment.


Inputs/Outputs

   •      auto wire? (F) —

    auto wire? specifies whether LabVIEW attempts to automatically wire the terminals of the new
    object with compatible terminals of the source object wired to location. National Instruments
   recommends that you do not use this input. Instead, use VI Scripting to wire the new object to
    other objects precisely.

   •        vi object class —

     vi object class indicates the class of the object you want to create. To specify a class, wire a class
     specifier constant to this input. A class specifier constant displays a hierarchical menu that
    contains the classes of all of the objects in LabVIEW. To identify which class to use for a specific
     object, explore the anatomy of common VI objects.

   •     owner refnum —

   owner refnum is a reference to the container into which you want to place the new object. The
    most common containers are VIs, clusters, and the diagrams of loops and other structures. For
    example, to add a new control to the front panel of a VI, wire a reference to either the relevant VI


                                                    © National Instruments 2425

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2425 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2426 ordinal=2426 -->
## Functions

Functions


            or the front panel of the relevant VI to owner refnum. To place a new object inside of a For Loop,
            wire a reference to the diagram of the relevant For Loop to owner refnum.

               •       style —

             style indicates the exact kind of object to create. When you create a constant from the style
             terminal, you obtain a list of all the objects that are native to LabVIEW. Select a value for style
             that is compatible with the class specified by vi object class. For example, you can select the
          Round Push Button style if viobject class is Boolean, and you can select the Add style if viobject
             class is Function. However, LabVIEW returns a run time error if you select the Add style when
             viobject class is Boolean because this pairing is not compatible.

               •       location —

             location specifies where the function places the new object within the container referenced by
          owner refnum. The location terminal accepts the following three kinds of arguments:

                     •  Pair of x, y coordinates—LabVIEW places the new object at the given coordinates in relation
                 to the origin of the owner. To quickly create this type of cluster, create a constant from the
                 location terminal.
                     • Reference to a pre-existing object—LabVIEW places the new object next to the referenced
                  object.
                     • New VI Object Offset From Referenced Object cluster—LabVIEW places the new object a
                  specified distance from the object referenced by this cluster.

             Refer to the New VI Object Location Argument VI in the Examples section of this topic for a visual
           comparison of these argument types.

                     •      Horizontal —

                Horizontal is the horizontal position.

                     •       Vertical —

                  Vertical is the vertical position.


               •       error in (no error) —

             error in describes error conditions that occur before this node runs. This input provides
            standard error in functionality.

               •      path —


2426   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2426 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2427 ordinal=2427 -->
## Functions

Functions


    path is a path to a subVI or pre-existing custom control. Wire data to path only when you want to
    add one of these objects to the owner.

   •     bounds —

    bounds specifies the width and height of the new object if the new object is resizable. LabVIEW
    ignores bounds for fixed-sized objects.

         •      Width —

       Width specifies the width of the object.

         •      Height —

        Height specifies the height of the object.


   •      object refnum —

    object refnum returns a reference to the new object created by this function. The reference is of
    the class specified by vi object class.

   •       error out —

    error out contains error information. This output provides standard error out functionality.


NewNew VIVI ObjectObject OffsetOffset FromFrom ReferencedReferenced ObjectObject

This cluster provides a way to define the location input of the New VI Object function
as an offset from another object. Refer to the New VI Object Location Argument
example VI in the labview\examples\Application Control\VI
Scripting\Creating Objects directory for a visual comparison of the three
acceptable types of arguments for the location input.

You must initialize the Refnum element to a reference to a pre-existing object by using
the Bundle or Bundle By Name function.


                                                    © National Instruments 2427

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2427 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2428 ordinal=2428 -->
## Functions

Functions


            Refnum is a reference to the object next to which you want the New VI Object function to
               place a new object.

               Relative Direction is the direction relative to the object referenced by Refnum where you
             want the new object to be placed.

              0            Right

              1             Left

              2          Top

              3          Bottom

              4          Top Right

              5          Top Left

              6          Bottom Right

              7          Bottom Left


              Point32 indicates the offset of the new object in the given direction from the referenced
                object.

                     Horizontal is the horizontal offset from the location specified by Relative Direction.

                        Vertical is the vertical offset from the location specified by Relative Direction.


      The New VI Object Offset From Referenced Object cluster contains a reference to
      another object, an enumerated list of relative directions from that object, and a sub-

2428   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2428 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2429 ordinal=2429 -->
## Functions

Functions

cluster of offset coordinates. Together, the relative direction and offset specify where
the New VI Object function places the new object in relation to the referenced object.

Examples

Refer to the following example files included with LabVIEW.

  • labview\examples\Application Control\VI Scripting\
   Creating Objects\New VI Object Location Argument.vi

TraverseTraverse forfor GObjectsGObjects

Searches a target for objects of a particular type and returns an array of references to
those objects. The target can be a front panel, a block diagram, or any object that can
contain other objects, such as a For Loop, a cluster, or a user-defined control. This VI
also recursively finds objects nested within other container objects.


Inputs/Outputs

   •      Other Refnum —

    Other Refnum is a reference to the container object you want to search if you specify the
    Traverse Target as Other. The reference must be a VI Server class that inherits from GObject,
    FlatSequenceFrame, or Page. LabVIEW ignores this input if Traverse Target is either FP or BD.

   •      Traverse Target —

    Traverse Target indicates the type of container object that you want to traverse. The following
    table contains the possible values for this input:

    0 FP—Front panel
    1 BD—Block diagram
    2 Other—Container objects other than the front panel or block diagram. These include structure


                                                    © National Instruments 2429

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2429 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2430 ordinal=2430 -->
## Functions

Functions


             diagrams and clusters.

               •       VI Refnum —

             VI Refnum is the reference to the VI you want to traverse. LabVIEW uses this input when Traverse
            Target is either FP or BD. LabVIEW ignores this input if you wire a reference to a specific
            container object to Other Refnum.

               •      Class Name —

            Class Name is the VI Server class name of the object for which you are searching.

               •       error in (no error) —

             error in describes error conditions that occur before this node runs. This input provides
            standard error in functionality.

               •      Traverse Generated Code (F) —

            Traverse Generated Code specifies whether to traverse code that LabVIEW generates in the
            process of implementing certain functions. The default is FALSE.

               •     dup VI Refnum —

          dup VI Refnum returns VI Refnum unchanged.

               •      References —

            References is an array of GObject references to the objects this VI finds. Use the To More Specific
             Class function to downcast each reference if necessary.

               •      # of Refs —

           # of Refs is the number of references in the References array.

               •       error out —

             error out contains error information. This output provides standard error out functionality.


      To use this VI, specify a Traverse Target of BD for block diagram or FP for front panel
      and the Class Name of the object you want to find. To traverse a specific container
       object instead of a front panel or block diagram, specify the target as Other and wire


2430   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2430 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2431 ordinal=2431 -->
## Functions

Functions

a reference to the specific object to the Other Refnum input.

Examples

Refer to the following example files included with LabVIEW.

  • labview\examples\Application Control\VI Scripting\Finding
   and Modifying Objects\Using Traverse.vi

GetGet GObjectGObject LabelLabel

Returns a string containing the label text of the object you specify and a reference to
that label. This VI returns the same value as the Label.Text property.


Inputs/Outputs

   •      GObject —

    GObject specifies the reference to the object whose label you want to get.

   •       error in (no error) —

    error in describes error conditions that occur before this node runs. This input provides
    standard error in functionality.

   •     dup GObject —

   dup GObject returns the same GObject reference you wire to GObject.

   •      Object Label —

    Object Label returns a string that contains the label text of the object you specify in GObject.
    This parameter returns the same value as the Label.Text property.

   •      Object Has Label? —


                                                    © National Instruments 2431

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2431 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2432 ordinal=2432 -->
## Functions

Functions


            Object Has Label? indicates whether the object has a label.

               •       error out —

             error out contains error information. This output provides standard error out functionality.

               •      Label Reference —

            Label Reference returns a reference to the label of the object you specify in GObject.


       This VI gets the label text of an object without requiring you to manually cast the
      GObject reference to the proper subclass. Instead, this VI attempts to cast the GObject
       reference to different LabVIEW subclasses until it casts to the correct one. Once the VI
       casts the GObject reference to the proper subclass, the VI returns the Label text and
       label reference values for that object.

      GetGet ClassClass HierarchyHierarchy fromfrom ClassClass NameName

       Returns an array of class names, in descending order of inheritance, from the top-level
       class name to the class name you specify. For example, if you specify WhileLoop in
       Class Name this VI returns the array [Generic, Gobject, Node,
     Structure, Loop, WhileLoop]. This VI works for any valid class name,
       regardless of whether you have scripting or private functionality turned on or off.

       This VI works on any class name that you can select in a Class Specifier Constant,
      which includes anything under the VI Server class hierarchy except for Application and
         VI.


      Inputs/Outputs

               •      Class Name —

            Class Name is the VI Server class name of the object for which you want to get a class hierarchy.

               •       error in (no error) —

2432   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2432 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2433 ordinal=2433 -->
## Functions

Functions


    error in describes error conditions that occur before this node runs. This input provides
    standard error in functionality.

   •      Class Hierarchy —

    Class Hierarchy returns an array of class names, in descending order of inheritance, from the
     top-level class name to the class name you specify. For example, if you specify WhileLoop in
    Class Name this VI returns the array [Generic, Gobject, Node, Structure, Loop,
   WhileLoop].

   •       error out —

    error out contains error information. This output provides standard error out functionality.

ApplicationApplication BuilderBuilder

Use the Application Builder VIs to build, deploy, or clean build specifications.


 Palette
              Description Object

               Builds a build specification using the properties in memory that you configure when
             you right-click a build specification and select Properties. To use this VI, you Build
               previously configure the build specification using the Properties shortcut menu
               option.


              Deploys the output of a build specification to a target. To use this VI, build the build
 Deploy
                specification using the Build VI.


               Deletes the build specification files that LabVIEW creates during the most recent
 Clean
                build.


                                                    © National Instruments 2433

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2433 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2434 ordinal=2434 -->
## Functions

Functions


         Palette                      Description
        Object

        Get Build     Gets the version information of a build specification. This VI returns the Major, Minor,
         Specification  Fix, and Build version numbers, which correspond to the version numbers on the
         Version       Version Information page of the properties dialog box for the build specification.


                       Sets the version information of a build specification. This VI sets the Major, Minor,
                           Fix, and Build version numbers, which correspond to the version numbers on the         Set Build                      Version Information page of the properties dialog box for the build specification.         Specification                   LabVIEW saves version information automatically only if you wire a path to this VI.         Version                       Therefore, if you wire a project reference to this VI, you must manually save the
                        project after you set the version information.


      BuildBuild

       Builds a build specification using the properties in memory that you configure when
      you right-click a build specification and select Properties. To use this VI, you
       previously configure the build specification using the Properties shortcut menu
       option.

      You cannot use the Build VI with the LabVIEW Run-Time Engine. If you plan to run a
       build specification on the LabVIEW Run-Time Engine, do not include the Build VI in any
       of the VIs for the build specification.


            • Build (path) VI
            • Build (project reference) VI
    BuildBuild (path)(path) VIVI

       Builds a build specification using the properties in memory that you configure when
      you right-click a build specification and select Properties. To use this VI, you


2434   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2434 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2435 ordinal=2435 -->
## Functions

Functions

previously configure the build specification using the Properties shortcut menu
option.

You cannot use the Build VI with the LabVIEW Run-Time Engine. If you plan to run a
build specification on the LabVIEW Run-Time Engine, do not include the Build VI in any
of the VIs for the build specification.


Inputs/Outputs

   •      Path to project —

    Path to project specifies the full path to the LabVIEW project (.lvproj) file that contains the
    build specification.

   •     Name of build specification (if empty: build all) —

   Name of build specification specifies the name of the build specification. Enter the name that
    appears under Build Specifications in the Project Explorer window to specify which build
     specification builds. You can change the name of the build specification in the Build
     specification name text box on the Information page of the build specification properties dialog
    box.

       If you do not specify a build specification, the VI builds all build specifications under the
     specified target.

   •     Name of target (My Computer) —

   Name of target specifies the target that contains the build specification. The target is My
   Computer by default.

   •       error in (no error) —

    error in describes error conditions that occur before this node runs. This input provides
    standard error in functionality.

   •      Generated files —


                                                    © National Instruments 2435

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2435 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2436 ordinal=2436 -->
## Functions

Functions


           Generated files specifies the paths to the generated build files.

               •       error out —

             error out contains error information. This output provides standard error out functionality.

    BuildBuild (project(project reference)reference) VIVI

       Builds a build specification using the properties in memory that you configure when
      you right-click a build specification and select Properties. To use this VI, you
       previously configure the build specification using the Properties shortcut menu
       option.

      You cannot use the Build VI with the LabVIEW Run-Time Engine. If you plan to run a
       build specification on the LabVIEW Run-Time Engine, do not include the Build VI in any
       of the VIs for the build specification.


      Inputs/Outputs

               •       Project reference —

            Project reference specifies a reference to the LabVIEW project (.lvproj) that contains the
             build specification.

               •     Name of build specification (if empty: build all) —

         Name of build specification specifies the name of the build specification. Enter the name that
           appears under Build Specifications in the Project Explorer window to specify which build
             specification builds. You can change the name of the build specification in the Build
             specification name text box on the Information page of the build specification properties dialog
            box.

                    If you do not specify a build specification, the VI builds all build specifications under the


2436   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2436 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2437 ordinal=2437 -->
## Functions

Functions


     specified target.

   •     Name of target (My Computer) —

   Name of target specifies the target that contains the build specification. The target is My
   Computer by default.

   •       error in (no error) —

    error in describes error conditions that occur before this node runs. This input provides
    standard error in functionality.

   •       project ref —

    project ref returns a reference to the LabVIEW project that contains the build specification.

   •      Generated files —

    Generated files specifies the paths to the generated build files.

   •       error out —

    error out contains error information. This output provides standard error out functionality.


DeployDeploy

Deploys the output of a build specification to a target. To use this VI, build the build
specification using the Build VI.


Inputs/Outputs

   •      Path to project —

    Path to project specifies the full path to the LabVIEW project (.lvproj) file that contains the
    build specification.


                                                    © National Instruments 2437

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2437 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2438 ordinal=2438 -->
## Functions

Functions

               •     Name of build specification (if empty: deploy all) —

         Name of build specification specifies the name of the build specification for the build output
           you want to deploy. The name appears under Build Specifications in the Project Explorer
           window. You can change the name of the build specification in the Build specification name text
           box on the Information page of the build specification properties dialog box.

                    If you do not specify a build specification, the VI deploys all build specifications to the specified
              target.

               •     Name of target —

         Name of target specifies the target to which you want to deploy the build specification output.

           You cannot deploy the build specification output to My Computer.

               •       error in (no error) —

             error in describes error conditions that occur before this node runs. This input provides
            standard error in functionality.

               •       error out —

             error out contains error information. This output provides standard error out functionality.


      CleanClean

       Deletes the build specification files that LabVIEW creates during the most recent build.


      Inputs/Outputs

               •      Path to project —

           Path to project specifies the full path to the LabVIEW project (.lvproj) file that contains the
             build specification.

               •     Name of build specification (if empty: clean all) —


2438   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2438 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2439 ordinal=2439 -->
## Functions

Functions


   Name of build specification specifies the name of the build specification. The name appears
    under Build Specifications in the Project Explorer window. You can change the name of the
    build specification in the Build specification name text box on the Information page of the build
     specification properties dialog box.

       If you do not specify a build specification, the VI cleans all build specifications under the
     specified target.

   •     Name of target (My Computer) —

   Name of target specifies the target that contains the build specification. The target is My
   Computer by default.

   •       error in (no error) —

    error in describes error conditions that occur before this node runs. This input provides
    standard error in functionality.

   •       error out —

    error out contains error information. This output provides standard error out functionality.


GetGet BuildBuild SpecificationSpecification VersionVersion

Gets the version information of a build specification. This VI returns the Major, Minor,
Fix, and Build version numbers, which correspond to the version numbers on the
Version Information page of the properties dialog box for the build specification.

You can use this VI to get the version information for a stand-alone applications,
installers, .NET interop assemblies, packed libraries, shared libraries, and source
distributions.

      Note Installer build specifications contain only Major, Minor, and Fix version
       numbers.

This VI returns an error if you attempt to get version information for a zip file.


                                                    © National Instruments 2439

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2439 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2440 ordinal=2440 -->
## Functions

Functions


            • Get Build Specification Version (path) VI
            • Get Build Specification Version (project reference) VI

      The following block diagram displays a common use case of how this VI works with the
       Set Build Specification Version VI and Build VI to manage an automatic nightly build
       process.


           Get Build Specification Version.vi—Gets the Major, Minor, Fix, and Build version numbers after
            reading a project path or project reference.

             In Place Element Structure—Reads the Major, Minor, Fix, and Build version numbers returned
           by the Get Build Specification Version VI and increments only the Build version number.

            Set Build Specification Version.vi—Sets the new version information with an incremented
            Build number.

             Build.vi—Creates the new build output with the new version information.

   GetGet BuildBuild SpecificationSpecification VersionVersion (path)(path) VIVI

       Gets the version information of a build specification. This VI returns the Major, Minor,
        Fix, and Build version numbers, which correspond to the version numbers on the
       Version Information page of the properties dialog box for the build specification.

      You can use this VI to get the version information for a stand-alone applications,
        installers, .NET interop assemblies, packed libraries, shared libraries, and source
        distributions.

           Note Installer build specifications contain only Major, Minor, and Fix version
             numbers.


2440   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2440 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2441 ordinal=2441 -->
## Functions

Functions

This VI returns an error if you attempt to get version information for a zip file.


Inputs/Outputs

   •      Path to project —

    Path to project specifies the full path to the LabVIEW project (.lvproj) file that contains the
    build specification.

   •     Name of build specification —

   Name of build specification specifies the name of the build specification for which you want to
    get version information. Enter the name that appears under Build Specifications in the Project
    Explorer window to retrieve the version information of a build specification.

   •     Name of target (My Computer) —

   Name of target specifies the target that contains the build specification. The target is My
   Computer by default.

   •       error in (no error) —

    error in describes error conditions that occur before this node runs. This input provides
    standard error in functionality.

   •       error out —

    error out contains error information. This output provides standard error out functionality.

   •      Build Specification Version —

    Build Specification Version returns the version information of the build specification.

         •      Major —

        Major specifies the major version. This number may increment to reflect significant feature
        changes.


                                                    © National Instruments 2441

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2441 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2442 ordinal=2442 -->
## Functions

Functions


                     •      Minor —

               Minor specifies the minor version. Similar to the Major version number, this number may
               increment to reflect minor feature changes.

                     •       Fix —

                  Fix specifies the fix version number. This number may increment for smaller changes, such
                as bug fixes.

                     •      Build —

                Build specifies the build number. This number may increment to reflect nightly builds.


      The following block diagram displays a common use case of how this VI works with the
       Set Build Specification Version VI and Build VI to manage an automatic nightly build
       process.


           Get Build Specification Version.vi—Gets the Major, Minor, Fix, and Build version numbers after
            reading a project path or project reference.

             In Place Element Structure—Reads the Major, Minor, Fix, and Build version numbers returned
           by the Get Build Specification Version VI and increments only the Build version number.

            Set Build Specification Version.vi—Sets the new version information with an incremented
            Build number.

             Build.vi—Creates the new build output with the new version information.


2442   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2442 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2443 ordinal=2443 -->
## Functions

Functions

GetGet BuildBuild SpecificationSpecification VersionVersion (project(project
reference)reference) VIVI

Gets the version information of a build specification. This VI returns the Major, Minor,
Fix, and Build version numbers, which correspond to the version numbers on the
Version Information page of the properties dialog box for the build specification.

You can use this VI to get the version information for a stand-alone applications,
installers, .NET interop assemblies, packed libraries, shared libraries, and source
distributions.

      Note Installer build specifications contain only Major, Minor, and Fix version
       numbers.

This VI returns an error if you attempt to get version information for a zip file.


Inputs/Outputs

   •       Project reference —

    Project reference specifies a reference to the LabVIEW project (.lvproj) that contains the
    build specification.

   •     Name of build specification —

   Name of build specification specifies the name of the build specification for which you want to
    get version information. Enter the name that appears under Build Specifications in the Project
    Explorer window to retrieve the version information of a build specification.

   •     Name of target (My Computer) —

   Name of target specifies the target that contains the build specification. The target is My


                                                    © National Instruments 2443

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2443 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2444 ordinal=2444 -->
## Functions

Functions


         Computer by default.

               •       error in (no error) —

             error in describes error conditions that occur before this node runs. This input provides
            standard error in functionality.

               •     dup Project reference —

          dup Project reference returns an unchanged reference to the LabVIEW project that contains the
             build specification.

               •       error out —

             error out contains error information. This output provides standard error out functionality.

               •      Build Specification Version —

            Build Specification Version returns the version information of the build specification.

                     •      Major —

               Major specifies the major version. This number may increment to reflect significant feature
                changes.

                     •      Minor —

               Minor specifies the minor version. Similar to the Major version number, this number may
               increment to reflect minor feature changes.

                     •       Fix —

                  Fix specifies the fix version number. This number may increment for smaller changes, such
                as bug fixes.

                     •      Build —

                Build specifies the build number. This number may increment to reflect nightly builds.


      The following block diagram displays a common use case of how this VI works with the
       Set Build Specification Version VI and Build VI to manage an automatic nightly build


2444   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2444 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2445 ordinal=2445 -->
## Functions

Functions

process.


    Get Build Specification Version.vi—Gets the Major, Minor, Fix, and Build version numbers after
    reading a project path or project reference.

     In Place Element Structure—Reads the Major, Minor, Fix, and Build version numbers returned
    by the Get Build Specification Version VI and increments only the Build version number.

    Set Build Specification Version.vi—Sets the new version information with an incremented
     Build number.

     Build.vi—Creates the new build output with the new version information.

SetSet BuildBuild SpecificationSpecification VersionVersion

Sets the version information of a build specification. This VI sets the Major, Minor, Fix,
and Build version numbers, which correspond to the version numbers on the Version
Information page of the properties dialog box for the build specification. LabVIEW
saves version information automatically only if you wire a path to this VI. Therefore, if
you wire a project reference to this VI, you must manually save the project after you set
the version information.

You can use this VI to set the version information for a stand-alone application,
installer, .NET interop assembly, packed library, shared library, or source distribution.

      Note Installer build specifications contain only Major, Minor, and Fix version
       numbers.

This VI returns an error if you attempt to set version information for a zip file.


                                                    © National Instruments 2445

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2445 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2446 ordinal=2446 -->
## Functions

Functions

            • Set Build Specification Version (path) VI
            • Set Build Specification Version (project reference) VI
    SetSet BuildBuild SpecificationSpecification VersionVersion (path)(path) VIVI

       Sets the version information of a build specification. This VI sets the Major, Minor, Fix,
      and Build version numbers, which correspond to the version numbers on the Version
       Information page of the properties dialog box for the build specification. LabVIEW
       saves version information automatically only if you wire a path to this VI. Therefore, if
      you wire a project reference to this VI, you must manually save the project after you set
       the version information.

      You can use this VI to set the version information for a stand-alone application,
         installer, .NET interop assembly, packed library, shared library, or source distribution.

           Note Installer build specifications contain only Major, Minor, and Fix version
             numbers.

       This VI returns an error if you attempt to set version information for a zip file.


      Inputs/Outputs

               •      Path to project —

           Path to project specifies the full path to the LabVIEW project (.lvproj) file that contains the
             build specification.

               •     Name of build specification —

         Name of build specification specifies the name of the build specification for which you want to
             set version information. Enter the name that appears under Build Specifications in the Project
            Explorer window to set the version information of a build specification.


2446   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2446 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2447 ordinal=2447 -->
## Functions

Functions

•     Name of target (My Computer) —

  Name of target specifies the target that contains the build specification. The target is My
  Computer by default.

•       error in (no error) —

  error in describes error conditions that occur before this node runs. This input provides
  standard error in functionality.

•      Build Specification Version —

  Build Specification Version returns the version information of the build specification.

      •      Major —

      Major returns the major version. Increment this number to reflect significant feature
      changes.

      •      Minor —

      Minor returns the minor version. Similar to the Major version number, increment this
     number to reflect minor feature changes.

      •       Fix —

       Fix returns the fix version number. Increment this number for smaller changes, such as bug
        fixes.

      •      Build —

      Build returns the build number. Increment this number for nightly builds.


•       error out —

  error out contains error information. This output provides standard error out functionality.


                                                   © National Instruments 2447

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2447 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2448 ordinal=2448 -->
## Functions

Functions

    SetSet BuildBuild SpecificationSpecification VersionVersion (project(project
    reference)reference) VIVI

       Sets the version information of a build specification. This VI sets the Major, Minor, Fix,
      and Build version numbers, which correspond to the version numbers on the Version
       Information page of the properties dialog box for the build specification. LabVIEW
       saves version information automatically only if you wire a path to this VI. Therefore, if
      you wire a project reference to this VI, you must manually save the project after you set
       the version information.

      You can use this VI to set the version information for a stand-alone application,
         installer, .NET interop assembly, packed library, shared library, or source distribution.

           Note Installer build specifications contain only Major, Minor, and Fix version
             numbers.

       This VI returns an error if you attempt to set version information for a zip file.


      Inputs/Outputs

               •       Project reference —

            Project reference specifies a reference to the LabVIEW project (.lvproj) that contains the
             build specification.

               •     Name of build specification —

         Name of build specification specifies the name of the build specification for which you want to
             set version information. Enter the name that appears under Build Specifications in the Project
            Explorer window to set the version information of a build specification.

               •     Name of target (My Computer) —

2448   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2448 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2449 ordinal=2449 -->
## Functions

Functions


  Name of target specifies the target that contains the build specification. The target is My
  Computer by default.

•       error in —

  error in describes error conditions that occur before this node runs. This input provides
  standard error in functionality.

•      Build Specification Version —

  Build Specification Version returns the version information of the build specification.

      •      Major —

      Major returns the major version. Increment this number to reflect significant feature
      changes.

      •      Minor —

      Minor returns the minor version. Similar to the Major version number, increment this
     number to reflect minor feature changes.

      •       Fix —

       Fix returns the fix version number. Increment this number for smaller changes, such as bug
        fixes.

      •      Build —

      Build returns the build number. Increment this number for nightly builds.


•     dup Project reference —

  dup Project reference returns an unchanged reference to the LabVIEW project that contains the
  build specification.

•       error out —

  error out contains error information. This output provides standard error out functionality.


                                                   © National Instruments 2449

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2449 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2450 ordinal=2450 -->
## Functions

Functions

     ReportReport GenerationGeneration

      Use the Report Generation VIs to create and manipulate reports of LabVIEW
       applications. You also can use the VIs on this palette to insert text, tables, and graphs
       into bookmark locations.

      The VIs on this palette can return report generation error codes.

      You can use the Report Generation VIs to generate reports that contain VI
      documentation or data the VI returns.

           Note Some of the VIs on this palette include inputs and outputs the VI
               ignores unless you install the Report Generation Toolkit.

           Note In some cases, VIs on this palette store graphic files (jpg, png, ...) on the
            windows temp folder. Links to these files are used in reports, html files, and
              other results. It is not possible to delete the files automatically because it is
               uncertain how long the reports are going to be used. It might be necessary to
               delete them manually from time to time.


         Palette Object   Description

                        Allows you to pass in a block of text along with optional formatting information
         Create Easy
                     and print the report to a designated printer or publish the report to a specified file
         Text Report
                          path.


          Print VI Panel
                           Prints a front panel or VI documentation or saves the front panel or VI
         or
                      documentation to a report.
        Documentation

          VI
                     Use the VI Documentation VIs to customize the VI documentation you print or save
        Documentation


2450   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2450 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2451 ordinal=2451 -->
## Functions

Functions


Palette Object   Description

                 to a report. VI documentation can include the icon and connector pane, front
                 panel, block diagram, VI hierarchy, revision history, controls and indicators, and
               so on.


Create Report   Creates a new report.


Print Report     Prints a report to a designated printer or to the default printer on the computer.


Save Report to
               Saves an HTML report to the file specified in report file path.File


Dispose Report  Closes the report and releases its interface, which saves memory.


HTML Reports   Use the HTML Reports Only VIs to manipulate HTML reports you create in
Only           LabVIEW.


Set Report Font  Sets the font properties of the report, including those in the headers and footers.


Append Report  Appends text to the selected report. Wire data to the text input to determine the
Text           polymorphic instance to use or manually select the instance.


              Appends a 2D array to a report as a table with the given column width. Wire data
Append Table
                 to the text data input to determine the polymorphic instance to use or manually
to Report
                  select the instance.


Append List to
              Adds a list of elements to the report.
Report


                                                    © National Instruments 2451

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2451 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2452 ordinal=2452 -->
## Functions

Functions


         Palette Object   Description

                     Use the Report Layout VIs to manipulate the layout of reports you create in
        Report Layout                       LabVIEW.


       Append Front   Creates an image of the front panel of the VI you specify in VI and appends it to a
        Panel Image to  report. Wire data to the VI input to determine the polymorphic instance to use or
        Report         manually select the instance.


       Append
                         Creates an image of the front panel object specified in ctrl reference and appends         Control Image                                      it to a report.         to Report


                        For an HTML report, the VI embeds a link to an image into the report.
       Append Image                      You can wire either a path to the image or a string that contains the image URL to
         to Report                             this polymorphic VI. Wire data to the path or URL of image input to determine the
                       polymorphic instance to use or manually select the instance.


        Advanced                     Use the Advanced Report Generation VIs to manipulate reports you create in        Report                       LabVIEW.
        Generation


                        Generates a preformatted report that contains VI documentation, data the VI
        Report           returns, and report properties, such as the author, company, and number of
                         pages.


      Examples

       Refer to the following example files included with LabVIEW.

            • labview\examples\Report Generation\HTML Reports\HTML
        Report.vi


2452   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2452 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2453 ordinal=2453 -->
## Functions

Functions

CreateCreate EasyEasy TextText ReportReport

Allows you to pass in a block of text along with optional formatting information and
print the report to a designated printer or publish the report to a specified file path.


Inputs/Outputs

   •      font settings —

    font settings indicates the font settings a report uses.

         •      charset (-1) —

        charset is the character set to use for report text. The default is -1.

         •      weight (-1) —

        weight is the thickness of the font. The default is -1.

         •     name —

      name is the font name.

         •       size —

         size is the font size.


   •       print or save? —

    print or save? specifies whether the VI prints or saves the report. The default is print. Set this
    input to save if you specify a file path in printer name or file path.


                                                    © National Instruments 2453

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2453 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2454 ordinal=2454 -->
## Functions

Functions


                 print           0
                 (default)—Prints the report.
               save           1              —Saves the report.

               •      margins —

           margins sets the page margins to use when printing the report.

                     •      margins (1.00) —

               margins sets the size of the page margins. The default is 1.00 for each margin.

                           If the margins are smaller than the minimum margins for the printer, the VI returns an error.

                           •      top —

                   top sets the distance in inches or centimeters between the top of the page and the top
                      of the content on the page.

                           •        left —

                          left sets the distance in inches or centimeters between the left edge of the page and the
                            left edge of the content on the page.

                           •       right —

                      right sets the distance in inches or centimeters between the right edge of the page and
                    the right edge of the content on the page.

                           •     bottom —

                  bottom sets the distance in inches or centimeters between the bottom of the page and
                    the bottom of the content on the page.


                     •     measurement system (default) —

              measurement system sets the units of measurement for the margins.


2454   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2454 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2455 ordinal=2455 -->
## Functions

Functions


      0 Default—Sets the margins in the measurement system configured on the computer.
      1 US—Sets the margins in inches.
      2 Metric—Sets the margins in centimeters.


•       text to be printed —

  text to be printed is the information you want to include in the report. Any information you want
  to include must be in a string.

        Note If this string contains printing codes, the VI might not behave as expected. For
          example, the string \00 prints a blank page on some computers. If the VI does not
          behave as expected, make sure this string does not contain printer codes.

•       printer name (default) or file path (dialog) —

  printer name or file path is the name of the printer to which you want to print a report or the file
  path to which you want to send a report, depending on report type. If you specify a printer
  name, the printer must be configured for use with the computer from which you print the report.
   If you specify a file path, you must set the print or save? input to save. If you do not wire this
  input, the VI uses the default printer in LabVIEW.

   If you wire a file path, you must enter the path as a string or use the Path to String function. If you
  do not specify a path, LabVIEW displays error -41003.

•      report type (HTML) —

  report type is the type of report you want to create.

   HTML
  0
    —Creates an HTML report.
   Word
  1
    (Report Generation Toolkit) —Creates a Word report.
     Excel
  2
    (Report Generation Toolkit)—Creates an Excel report.

•       orientation (portrait) —

  orientation (Windows) specifies how the report appears when it prints.


                                                   © National Instruments 2455

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2455 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2456 ordinal=2456 -->
## Functions

Functions


           0 Portrait (default)—Prints the report so the short edge of the paper is the top of the page.
           1 Landscape—Prints the report so the long edge of the paper is the top of the page.

               •       error in (no error) —

             error in describes error conditions that occur before this node runs. This input provides
            standard error in functionality.

               •      headers —

           headers specifies what information appears in the header of each page of the report.

                     •        left —

                     left is the information you want to appear in the left side of the header.

                     •      center —

                center is the information you want to appear in the center portion of the header.

                     •       right —

                  right is the information you want to appear in the right side of the header.


               •       footers —

             footers specifies what information appears in the footer of each page of the report.

                     •        left —

                     left is the information you want to appear in the left side of the footer.

                     •      center —

                center is the information you want to appear in the center portion of the footer.

                     •       right —

                  right is the information you want to appear in the right side of the footer.


               •       error out —


2456   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2456 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2457 ordinal=2457 -->
## Functions

Functions


    error out contains error information. This output provides standard error out functionality.


Use tokens with this VI to generate information in the report, such as in the headers
and footers. For example, you can insert a time stamp in the footers of the report.

You cannot use tokens with Microsoft Word and Excel reports.

You cannot use this VI with any other Report Generation VIs. Also, this VI does not give
you fine-grain control over the formatting of a report. You can use this VI to specify the
text font, set the header and footer, set margins, specify a printer, and set the page
orientation. This VI disposes of the report automatically, which frees memory space.
However, you cannot control where information is placed, append information from
another file, or clear the report of font styles, headers and footers, or text. Use the
other Report Generation VIs to generate complicated reports, such as those with many
different kinds of information.

PrintPrint VIVI PanelPanel oror DocumentationDocumentation

Prints a front panel or VI documentation or saves the front panel or VI documentation
to a report.


  • Print VI Panel or Documentation (path) VI
  • Print VI Panel or Documentation (refnum) VI
  • Print VI Panel or Documentation (string) VI

If a front panel is not visible, LabVIEW does not update the values in the objects on the
front panel. If you call a VI whose front panel is not visible and you use the Print VI
Panel or Documentation VI to create an image of the front panel, the image does not
reflect any value changes that occurred when you ran the VI.

If you want the image to reflect value changes, make sure the front panel is open
before any values change. If you do not want to display the front panel but want the
image to reflect value changes, create a Property Node from any front panel terminal

                                                    © National Instruments 2457

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2457 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2458 ordinal=2458 -->
## Functions

Functions

      on the block diagram of the VI for which you want to create a front panel image.

      You also can use the Front Panel:Get Image and Get Panel Image Scaled methods to
       return a front panel image programmatically. Use the VI Documentation VIs to print
        specific components of VI documentation or to save the components to a report.

       PrintPrint VIVI PanelPanel oror DocumentationDocumentation (path)(path) VIVI

       Prints a front panel or VI documentation or saves the front panel or VI documentation
       to a report.


      Inputs/Outputs

               •      layout options —

            layout options sets the page layout and printing options for the report, if report type is Quick
          Print. Otherwise, LabVIEW ignores this input.

                     •       orientation (unchanged) —

                 orientation specifies the page orientation of the report.

               You also can use the Printing:Page Orientation property to set the page orientation
                programmatically.

               0 Unchanged (default)—Uses the default setting for the VI.
               1 Portrait—Prints the report so the short edge of the paper is the top of the page.
               2 Landscape—Prints the report so the long edge of the paper is the top of the page.

                     •      panel scaling for page (unchanged) —

               panel scaling for page sets whether to scale the front panel so it fits on the printed page.


2458   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2458 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2459 ordinal=2459 -->
## Functions

Functions


  You also can use the Printing:Front Panel Scaling? property to set the scaling option
  programmatically.

  0 Unchanged (default)—Uses the default setting for the VI.
  1 No Scaling—Does not scale the front panel to fit on the printed page.
  2 Scale front panel to fit—Scales the front panel to fit on the printed page.

•      margins —

  margins sets the page margins of the printed report and the units of measurement for the
  margins.

  You also can use the Printing:Margins property to set the page margins programmatically.

      •      override VI margins (false) —

          If override VI margins is TRUE, the VI uses the margins you set in margins. If FALSE
        (default), the VI uses the default margins for the VI.

      •      margins (1.00) —

      margins sets the size of the page margins. The default is 1.00 for each margin.

          If the margins are smaller than the minimum margins for the printer, the VI returns an
        error.

             •      top —

          top sets the distance in inches or centimeters between the top of the page and the
          top of the content on the page.

             •        left —

              left sets the distance in inches or centimeters between the left edge of the page
         and the left edge of the content on the page.

             •       right —


                                                © National Instruments 2459

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2459 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2460 ordinal=2460 -->
## Functions

Functions


                           right sets the distance in inches or centimeters between the right edge of the page
                     and the right edge of the content on the page.

                                  •     bottom —

                     bottom sets the distance in inches or centimeters between the bottom of the page
                     and the bottom of the content on the page.


                           •     measurement system (default) —

                 measurement system sets the units of measurement for the margins.

                   0 Default—Sets the margins in inches.
                   1 US—Sets the margins in inches.
                   2 Metric—Sets the margins in centimeters.


                     •       printer options —

                 printer options sets the printer to use and the printer options.

              The VI uses this input only if report type is 0.

                           •      destination printer name (current) —

                     destination printer name is the name of the printer to which you want to print the
                       report.

                                 If you wire a printer name, that printer must be configured for use with the computer
                   from which you want to print the report.

                                 If you do not wire a printer name, the VI uses the default printer in LabVIEW. The
                  computer from which you want to print must have a default printer.

                  You can use the Query Available Printers VI to obtain a list of the printers available on
                    the computer, including the default printer in LabVIEW.


2460   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2460 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2461 ordinal=2461 -->
## Functions

Functions


      •       printing method (unchanged) —

       printing method sets how LabVIEW prints the report.

       This input is similar to the Standard printing, PostScript printing, and Bitmap printing
      buttons on the Printing page of the Options dialog box.

      You also can use the Printing:Method property to set how LabVIEW prints
      programmatically.

      0 Unchanged (default)—Uses the default setting for LabVIEW.
      1 Standard—Uses standard printing.
      2 PostScript—Uses PostScript printing.
      3 Bitmap—Uses bitmap printing.

      •       color or monochrome (unchanged) —

       color or monochrome sets whether to send color/grayscale or monochrome output to
      the printer.

       This input is similar to the Color/Grayscale printing checkbox on the Printing page of
      the Options dialog box.

      You also can use the Printing:Color/Grayscale? property to configure the colors of the
      output programmatically.

      0 Unchanged (default)—Uses the default setting for LabVIEW.
        Color/grayscale—If the printer is a color printer, LabVIEW sends color output to the      1
         printer. Otherwise, LabVIEW sends grayscale output to the printer.
      2 Monochrome—Sends monochrome output to the printer.


•      page header options —

  page header options sets whether to print page headers and configures the contents of the
  headers.

      •      page headers (unchanged) —


                                                © National Instruments 2461

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2461 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2462 ordinal=2462 -->
## Functions

Functions


                  page headers sets whether to print page headers for the report.

                  You also can use the Printing:Page Headers? property to print page headers
                     programmatically.

                  Unchanged (default)—Uses the default setting for the VI. If you wire this value, the VI                   0                      ignores the page header content options input.
                      Include page headers—Prints headers for the report using the values you wire to the
                   1                   page header content options input.
                   2 Do not include page headers—Prints no headers for the report.

                           •      page header content options —

                  page header content options sets which data to include in the page headers.

                                 If page headers is 0, the VI ignores this input.

                  You also can use the Printing:Header Content properties to customize the contents of
                    the headers programmatically.

                                  •      Include VI Name —

                                        If Include VI Name is TRUE (default), the report headers include the VI name.

                                  •      Include VI Path —

                                        If Include VI Path is TRUE (default), the report headers include the VI path.

                                  •      Include Last Modification Date —

                                        If Include Last Modification Date is TRUE (default), the report headers include the
                              last modification date.

                                  •      Include Date Printed —

                                        If Include Date Printed is TRUE (default), the report headers include the date
                           printed.


2462   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2462 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2463 ordinal=2463 -->
## Functions

Functions


                   •      Include Page Number —

                        If Include Page Number is TRUE (default), the report headers include the page
             number.

                   •      Include VI Icon —

                        If Include VI Icon is TRUE (default), the report headers include the VI icon.


•       VI path —

  VI path is the path to the VI you want to print or save to a report.

  The default is the path to the VI that contains this VI as a subVI.

•      contents (complete front panel) —

  contents sets which data to print or include in the report.

  0 Complete front panel (default)—Prints the entire front panel.
  1 Visible portion of front panel—Prints only the currently visible portion of the front panel.
    Icon, description, panel and diagram—Prints the VI description, icon and connector pane,  2    front panel, and block diagram.
   Documentation: Using the panel—Prints the VI description, front panel, and controls and
  3 indicators, including data types, names, and descriptions. LabVIEW prints the controls and
    indicators in tabbing order.
   Documentation: Using as a subVI—Prints the VI description, icon and connector pane, and
   connected controls and indicators, including data types, names, and descriptions. LabVIEW
  4    prints the controls and indicators in tabbing order. This format is similar to the format of the VI
   and function reference topics in the LabVIEWHelp.
   Documentation: Complete—Prints the VI description, icon and connector pane, front panel,
  5 controls and indicators, including data types, names, and descriptions, block diagram, a list of
    subVIs, including icons, names, and paths, revision history information, and the VI hierarchy.
   Documentation: Custom—Uses the values you wire to custom contents options to determine
  6
   which data to print.

•      report type (Quick Print) —

                                                   © National Instruments 2463

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2463 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2464 ordinal=2464 -->
## Functions

Functions


            report type sets the type of report you want to create.

           0 Quick Print (default)—Prints the report immediately.
           HTML—Creates an HTML report and returns a reference to it in report out so you can use other           1             Report Generation VIs to customize, save, or print the report.
           Word (Report Generation Toolkit)—Creates a report in Word and returns a reference to it in           2             report out so you can use other Report Generation VIs to customize, save, or print the report.
              Excel (Report Generation Toolkit)—Creates a report in Excel and returns a reference to it in           3             report out so you can use other Report Generation VIs to customize, save, or print the report.

               •       error in (no error) —

             error in describes error conditions that occur before this node runs. This input provides
            standard error in functionality.

               •     custom contents options —

          custom contents options sets which data to print or include in the report if you set contents to
           Documentation: Custom.

           You also can use the Printing:Custom properties to set which data to print programmatically.

                     •      include VI connector and icon —

                           If include VI connector and icon is TRUE, the report includes the VI icon and connector
                pane. The default is FALSE.

                     •      include VI description —

                           If include VI description is TRUE, the report includes the VI description. The default is
                FALSE.

                     •      include front panel —

                           If include front panel is TRUE, the report includes the front panel. The default is FALSE.

                     •      surround front panel with border —

                           If surround front panel with border is TRUE, the VI prints a border around the front panel.
              The default is FALSE.

                     •         list of controls options —


2464   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2464 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2465 ordinal=2465 -->
## Functions

Functions


   list of controls options sets whether to include a list of controls and indicators in the report
  and sets the data to include in the list.

      •      include list of controls —

          If include list of controls is TRUE, the report includes a list of controls and indicators.
     The default is FALSE.

      •         list which controls? —

         list which controls? sets which controls and indicators to include in the list.

      0 all controls (default)—Prints all controls and indicators.
      1 connected controls—Prints only connected controls and indicators.

      •      include control descriptions? —

          If include control descriptions? is TRUE, the report includes control and indicator
       descriptions. The default is FALSE.

      •      include control data types? —

          If include control data types? is TRUE, the report includes control and indicator data
       types. The default is FALSE.


•      block diagram options —

  block diagram options sets whether to include the block diagram in the report and how to
  print structures on the block diagram.

      •      include block diagram —

          If include block diagram is TRUE, the report includes the block diagram. The default is
      FALSE.

      •      hidden frames —

          If hidden frames is TRUE, the block diagram image includes all visible subdiagrams of


                                                © National Instruments 2465

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2465 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2466 ordinal=2466 -->
## Functions

Functions


                   each Case, Event, and Stacked Sequence structure, followed by all hidden subdiagrams
                        for each structure. If FALSE (default), the image includes only visible subdiagrams.

                           •      ordered (repeat from higher level if nested) —

                                 If ordered is TRUE, the block diagram image includes all visible subdiagrams of each
                     Case, Event, and Stacked Sequence structure, followed by all subdiagrams for each
                      structure in order, including visible and hidden subdiagrams. If FALSE (default), the
                  image does not repeat visible subdiagrams in the ordered list of subdiagrams.

                                 If Hidden frames is FALSE, the VI ignores this input.


                     •      include VI hierarchy —

                           If include VI hierarchy is TRUE, the report includes the VI hierarchy. The default is FALSE.

                     •      include list of subVIs —

                           If include list of subVIs is TRUE, the report includes a list of subVIs, including icons, names,
              and paths. The default is FALSE.

                     •      include VI history —

                           If include VI history is TRUE, the report includes revision history information. The default is
                FALSE.

                     •      include Express VI configuration information —

                           If include Express VI configuration information is TRUE, the report includes configuration
                information for any Express VIs on the block diagram. The default is FALSE.


               •      report out —

            report out is a reference to the report whose appearance, data, and printing you want to control.

           You can wire this output to other Report Generation VIs.

               •       error out —


2466   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2466 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2467 ordinal=2467 -->
## Functions

Functions


    error out contains error information. This output provides standard error out functionality.


If a front panel is not visible, LabVIEW does not update the values in the objects on the
front panel. If you call a VI whose front panel is not visible and you use the Print VI
Panel or Documentation VI to create an image of the front panel, the image does not
reflect any value changes that occurred when you ran the VI.

If you want the image to reflect value changes, make sure the front panel is open
before any values change. If you do not want to display the front panel but want the
image to reflect value changes, create a Property Node from any front panel terminal
on the block diagram of the VI for which you want to create a front panel image.

You also can use the Front Panel:Get Image and Get Panel Image Scaled methods to
return a front panel image programmatically. Use the VI Documentation VIs to print
specific components of VI documentation or to save the components to a report.

PrintPrint VIVI PanelPanel oror DocumentationDocumentation (refnum)(refnum) VIVI

Prints a front panel or VI documentation or saves the front panel or VI documentation
to a report.


Inputs/Outputs

   •      layout options —

    layout options sets the page layout and printing options for the report, if report type is Quick
    Print. Otherwise, LabVIEW ignores this input.

         •       orientation (unchanged) —


                                                    © National Instruments 2467

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2467 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2468 ordinal=2468 -->
## Functions

Functions


                 orientation specifies the page orientation of the report.

               You also can use the Printing:Page Orientation property to set the page orientation
                programmatically.

               0 Unchanged (default)—Uses the default setting for the VI.
               1 Portrait—Prints the report so the short edge of the paper is the top of the page.
               2 Landscape—Prints the report so the long edge of the paper is the top of the page.

                     •      panel scaling for page (unchanged) —

               panel scaling for page sets whether to scale the front panel so it fits on the printed page.

               You also can use the Printing:Front Panel Scaling? property to set the scaling option
                programmatically.

               0 Unchanged (default)—Uses the default setting for the VI.
               1 No Scaling—Does not scale the front panel to fit on the printed page.
               2 Scale front panel to fit—Scales the front panel to fit on the printed page.

                     •      margins —

               margins sets the page margins of the printed report and the units of measurement for the
                margins.

               You also can use the Printing:Margins property to set the page margins programmatically.

                           •      override VI margins (false) —

                                 If override VI margins is TRUE, the VI uses the margins you set in margins. If FALSE
                        (default), the VI uses the default margins for the VI.

                           •      margins (1.00) —

                   margins sets the size of the page margins. The default is 1.00 for each margin.

                                 If the margins are smaller than the minimum margins for the printer, the VI returns an
                         error.


2468   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2468 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2469 ordinal=2469 -->
## Functions

Functions


             •      top —

          top sets the distance in inches or centimeters between the top of the page and the
          top of the content on the page.

             •        left —

              left sets the distance in inches or centimeters between the left edge of the page
         and the left edge of the content on the page.

             •       right —

            right sets the distance in inches or centimeters between the right edge of the page
         and the right edge of the content on the page.

             •     bottom —

         bottom sets the distance in inches or centimeters between the bottom of the page
         and the bottom of the content on the page.


      •     measurement system (default) —

     measurement system sets the units of measurement for the margins.

      0 Default—Sets the margins in inches.
      1 US—Sets the margins in inches.
      2 Metric—Sets the margins in centimeters.


•       printer options —

  printer options sets the printer to use and the printer options.

  The VI uses this input only if report type is 0.

      •      destination printer name (current) —


                                                © National Instruments 2469

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2469 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2470 ordinal=2470 -->
## Functions

Functions


                     destination printer name is the name of the printer to which you want to print the
                       report.

                                 If you wire a printer name, that printer must be configured for use with the computer
                   from which you want to print the report.

                                 If you do not wire a printer name, the VI uses the default printer in LabVIEW. The
                  computer from which you want to print must have a default printer.

                  You can use the Query Available Printers VI to obtain a list of the printers available on
                    the computer, including the default printer in LabVIEW.

                           •       printing method (unchanged) —

                     printing method sets how LabVIEW prints the report.

                     This input is similar to the Standard printing, PostScript printing, and Bitmap printing
                    buttons on the Printing page of the Options dialog box.

                  You also can use the Printing:Method property to set how LabVIEW prints
                     programmatically.

                   0 Unchanged (default)—Uses the default setting for LabVIEW.
                   1 Standard—Uses standard printing.
                   2 PostScript—Uses PostScript printing.
                   3 Bitmap—Uses bitmap printing.

                           •       color or monochrome (unchanged) —

                     color or monochrome sets whether to send color/grayscale or monochrome output to
                    the printer.

                     This input is similar to the Color/Grayscale printing checkbox on the Printing page of
                    the Options dialog box.

                  You also can use the Printing:Color/Grayscale? property to configure the colors of the
                   output programmatically.


2470   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2470 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2471 ordinal=2471 -->
## Functions

Functions


      0 Unchanged (default)—Uses the default setting for LabVIEW.
        Color/grayscale—If the printer is a color printer, LabVIEW sends color output to the      1         printer. Otherwise, LabVIEW sends grayscale output to the printer.
      2 Monochrome—Sends monochrome output to the printer.


•      page header options —

  page header options sets whether to print page headers and configures the contents of the
  headers.

      •      page headers (unchanged) —

      page headers sets whether to print page headers for the report.

      You also can use the Printing:Page Headers? property to print page headers
      programmatically.

      Unchanged (default)—Uses the default setting for the VI. If you wire this value, the VI      0        ignores the page header content options input.
        Include page headers—Prints headers for the report using the values you wire to the      1       page header content options input.
      2 Do not include page headers—Prints no headers for the report.

      •      page header content options —

      page header content options sets which data to include in the page headers.

          If page headers is 0, the VI ignores this input.

      You also can use the Printing:Header Content properties to customize the contents of
      the headers programmatically.

             •      Include VI Name —

                 If Include VI Name is TRUE (default), the report headers include the VI name.


                                                © National Instruments 2471

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2471 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2472 ordinal=2472 -->
## Functions

Functions


                                  •      Include VI Path —

                                        If Include VI Path is TRUE (default), the report headers include the VI path.

                                  •      Include Last Modification Date —

                                        If Include Last Modification Date is TRUE (default), the report headers include the
                              last modification date.

                                  •      Include Date Printed —

                                        If Include Date Printed is TRUE (default), the report headers include the date
                           printed.

                                  •      Include Page Number —

                                        If Include Page Number is TRUE (default), the report headers include the page
                      number.

                                  •      Include VI Icon —

                                        If Include VI Icon is TRUE (default), the report headers include the VI icon.


               •       VI reference —

             VI reference is a reference to the VI you want to print or save to a report.

           You can use the Open VI Reference function to obtain a reference to another VI.

               •      contents (complete front panel) —

            contents sets which data to print or include in the report.

           0 Complete front panel (default)—Prints the entire front panel.
           1 Visible portion of front panel—Prints only the currently visible portion of the front panel.
              Icon, description, panel and diagram—Prints the VI description, icon and connector pane,
           2
               front panel, and block diagram.


2472   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2472 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2473 ordinal=2473 -->
## Functions

Functions


   Documentation: Using the panel—Prints the VI description, front panel, and controls and
  3 indicators, including data types, names, and descriptions. LabVIEW prints the controls and
    indicators in tabbing order.
   Documentation: Using as a subVI—Prints the VI description, icon and connector pane, and
   connected controls and indicators, including data types, names, and descriptions. LabVIEW
  4    prints the controls and indicators in tabbing order. This format is similar to the format of the VI
   and function reference topics in the LabVIEWHelp.
   Documentation: Complete—Prints the VI description, icon and connector pane, front panel,
  5 controls and indicators, including data types, names, and descriptions, block diagram, a list of
    subVIs, including icons, names, and paths, revision history information, and the VI hierarchy.
   Documentation: Custom—Uses the values you wire to custom contents options to determine  6   which data to print.

•      report type (Quick Print) —

  report type sets the type of report you want to create.

  0 Quick Print (default)—Prints the report immediately.
   Standard Report—Creates a report and returns a reference to it in report out so you can use
  1   other Report Generation VIs to customize or print the report.
   HTML—Creates an HTML report and returns a reference to it in report out so you can use other
  2   Report Generation VIs to customize, save, or print the report.

•       error in (no error) —

  error in describes error conditions that occur before this node runs. This input provides
  standard error in functionality.

•     custom contents options —

  custom contents options sets which data to print or include in the report if you set contents to
  Documentation: Custom.

  You also can use the Printing:Custom properties to set which data to print programmatically.

      •      include VI connector and icon —

          If include VI connector and icon is TRUE, the report includes the VI icon and connector
      pane. The default is FALSE.

      •      include VI description —


                                                   © National Instruments 2473

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2473 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2474 ordinal=2474 -->
## Functions

Functions


                           If include VI description is TRUE, the report includes the VI description. The default is
                FALSE.

                     •      include front panel —

                           If include front panel is TRUE, the report includes the front panel. The default is FALSE.

                     •      surround front panel with border —

                           If surround front panel with border is TRUE, the VI prints a border around the front panel.
              The default is FALSE.

                     •         list of controls options —

                       list of controls options sets whether to include a list of controls and indicators in the report
              and sets the data to include in the list.

                           •      include list of controls —

                                 If include list of controls is TRUE, the report includes a list of controls and indicators.
                  The default is FALSE.

                           •         list which controls? —

                            list which controls? sets which controls and indicators to include in the list.

                   0 all controls (default)—Prints all controls and indicators.
                   1 connected controls—Prints only connected controls and indicators.

                           •      include control descriptions? —

                                 If include control descriptions? is TRUE, the report includes control and indicator
                      descriptions. The default is FALSE.

                           •      include control data types? —

                                 If include control data types? is TRUE, the report includes control and indicator data
                      types. The default is FALSE.


                     •      block diagram options —


2474   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2474 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2475 ordinal=2475 -->
## Functions

Functions


  block diagram options sets whether to include the block diagram in the report and how to
  print structures on the block diagram.

      •      include block diagram —

          If include block diagram is TRUE, the report includes the block diagram. The default is
      FALSE.

      •      hidden frames —

          If hidden frames is TRUE, the block diagram image includes all visible subdiagrams of
      each Case, Event, and Stacked Sequence structure, followed by all hidden subdiagrams
       for each structure. If FALSE (default), the image includes only visible subdiagrams.

      •      ordered (repeat from higher level if nested) —

          If ordered is TRUE, the block diagram image includes all visible subdiagrams of each
      Case, Event, and Stacked Sequence structure, followed by all subdiagrams for each
       structure in order, including visible and hidden subdiagrams. If FALSE (default), the
      image does not repeat visible subdiagrams in the ordered list of subdiagrams.

          If Hidden frames is FALSE, the VI ignores this input.


•      include VI hierarchy —

   If include VI hierarchy is TRUE, the report includes the VI hierarchy. The default is FALSE.

•      include list of subVIs —

   If include list of subVIs is TRUE, the report includes a list of subVIs, including icons, names,
  and paths. The default is FALSE.

•      include VI history —

   If include VI history is TRUE, the report includes revision history information. The default is
  FALSE.

•      include Express VI configuration information —

   If include Express VI configuration information is TRUE, the report includes configuration


                                                © National Instruments 2475

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2475 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2476 ordinal=2476 -->
## Functions

Functions


                information for any Express VIs on the block diagram. The default is FALSE.


               •      report out —

            report out is a reference to the report whose appearance, data, and printing you want to control.

           You can wire this output to other Report Generation VIs.

               •       error out —

             error out contains error information. This output provides standard error out functionality.


           If a front panel is not visible, LabVIEW does not update the values in the objects on the
       front panel. If you call a VI whose front panel is not visible and you use the Print VI
       Panel or Documentation VI to create an image of the front panel, the image does not
        reflect any value changes that occurred when you ran the VI.

           If you want the image to reflect value changes, make sure the front panel is open
       before any values change. If you do not want to display the front panel but want the
      image to reflect value changes, create a Property Node from any front panel terminal
      on the block diagram of the VI for which you want to create a front panel image.

      You also can use the Front Panel:Get Image and Get Panel Image Scaled methods to
       return a front panel image programmatically. Use the VI Documentation VIs to print
        specific components of VI documentation or to save the components to a report.

       PrintPrint VIVI PanelPanel oror DocumentationDocumentation (string)(string) VIVI

       Prints a front panel or VI documentation or saves the front panel or VI documentation
       to a report.


2476   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2476 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2477 ordinal=2477 -->
## Functions

Functions

Inputs/Outputs

   •      layout options —

    layout options sets the page layout and printing options for the report, if report type is Quick
    Print. Otherwise, LabVIEW ignores this input.

         •       orientation (unchanged) —

         orientation specifies the page orientation of the report.

        You also can use the Printing:Page Orientation property to set the page orientation
        programmatically.

        0 Unchanged (default)—Uses the default setting for the VI.
        1 Portrait—Prints the report so the short edge of the paper is the top of the page.
        2 Landscape—Prints the report so the long edge of the paper is the top of the page.

         •      panel scaling for page (unchanged) —

        panel scaling for page sets whether to scale the front panel so it fits on the printed page.

        You also can use the Printing:Front Panel Scaling? property to set the scaling option
        programmatically.

        0 Unchanged (default)—Uses the default setting for the VI.
        1 No Scaling—Does not scale the front panel to fit on the printed page.
        2 Scale front panel to fit—Scales the front panel to fit on the printed page.

         •      margins —

        margins sets the page margins of the printed report and the units of measurement for the
        margins.

        You also can use the Printing:Margins property to set the page margins programmatically.

                •      override VI margins (false) —

                     If override VI margins is TRUE, the VI uses the margins you set in margins. If FALSE
               (default), the VI uses the default margins for the VI.


                                                    © National Instruments 2477

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2477 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2478 ordinal=2478 -->
## Functions

Functions


                           •      margins (1.00) —

                   margins sets the size of the page margins. The default is 1.00 for each margin.

                                 If the margins are smaller than the minimum margins for the printer, the VI returns an
                         error.

                                  •      top —

                       top sets the distance in inches or centimeters between the top of the page and the
                        top of the content on the page.

                                  •        left —

                                left sets the distance in inches or centimeters between the left edge of the page
                     and the left edge of the content on the page.

                                  •       right —

                           right sets the distance in inches or centimeters between the right edge of the page
                     and the right edge of the content on the page.

                                  •     bottom —

                     bottom sets the distance in inches or centimeters between the bottom of the page
                     and the bottom of the content on the page.


                           •     measurement system (default) —

                 measurement system sets the units of measurement for the margins.

                   0 Default—Sets the margins in inches.
                   1 US—Sets the margins in inches.
                   2 Metric—Sets the margins in centimeters.


                     •       printer options —

                 printer options sets the printer to use and the printer options.


2478   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2478 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2479 ordinal=2479 -->
## Functions

Functions


The VI uses this input only if report type is 0.

   •      destination printer name (current) —

    destination printer name is the name of the printer to which you want to print the
     report.

       If you wire a printer name, that printer must be configured for use with the computer
    from which you want to print the report.

       If you do not wire a printer name, the VI uses the default printer in LabVIEW. The
    computer from which you want to print must have a default printer.

    You can use the Query Available Printers VI to obtain a list of the printers available on
    the computer, including the default printer in LabVIEW.

   •       printing method (unchanged) —

    printing method sets how LabVIEW prints the report.

    This input is similar to the Standard printing, PostScript printing, and Bitmap printing
    buttons on the Printing page of the Options dialog box.

    You also can use the Printing:Method property to set how LabVIEW prints
    programmatically.

    0 Unchanged (default)—Uses the default setting for LabVIEW.
    1 Standard—Uses standard printing.
    2 PostScript—Uses PostScript printing.
    3 Bitmap—Uses bitmap printing.

   •       color or monochrome (unchanged) —

    color or monochrome sets whether to send color/grayscale or monochrome output to
    the printer.

    This input is similar to the Color/Grayscale printing checkbox on the Printing page of
    the Options dialog box.


                                              © National Instruments 2479

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2479 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2480 ordinal=2480 -->
## Functions

Functions


                  You also can use the Printing:Color/Grayscale? property to configure the colors of the
                   output programmatically.

                   0 Unchanged (default)—Uses the default setting for LabVIEW.
                      Color/grayscale—If the printer is a color printer, LabVIEW sends color output to the                   1                          printer. Otherwise, LabVIEW sends grayscale output to the printer.
                   2 Monochrome—Sends monochrome output to the printer.


                     •      page header options —

              page header options sets whether to print page headers and configures the contents of the
                headers.

                           •      page headers (unchanged) —

                  page headers sets whether to print page headers for the report.

                  You also can use the Printing:Page Headers? property to print page headers
                     programmatically.

                  Unchanged (default)—Uses the default setting for the VI. If you wire this value, the VI                   0                      ignores the page header content options input.
                      Include page headers—Prints headers for the report using the values you wire to the                   1                   page header content options input.
                   2 Do not include page headers—Prints no headers for the report.

                           •      page header content options —

                  page header content options sets which data to include in the page headers.

                                 If page headers is 0, the VI ignores this input.

                  You also can use the Printing:Header Content properties to customize the contents of
                    the headers programmatically.


2480   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2480 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2481 ordinal=2481 -->
## Functions

Functions


                   •      Include VI Name —

                        If Include VI Name is TRUE (default), the report headers include the VI name.

                   •      Include VI Path —

                        If Include VI Path is TRUE (default), the report headers include the VI path.

                   •      Include Last Modification Date —

                        If Include Last Modification Date is TRUE (default), the report headers include the
                  last modification date.

                   •      Include Date Printed —

                        If Include Date Printed is TRUE (default), the report headers include the date
                printed.

                   •      Include Page Number —

                        If Include Page Number is TRUE (default), the report headers include the page
             number.

                   •      Include VI Icon —

                        If Include VI Icon is TRUE (default), the report headers include the VI icon.


•       VI name —

  VI name is the name of the VI you want to print or save to a report. The VI must be in memory.

•      contents (complete front panel) —

  contents sets which data to print or include in the report.

  0 Complete front panel (default)—Prints the entire front panel.
  1 Visible portion of front panel—Prints only the currently visible portion of the front panel.


                                                   © National Instruments 2481

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2481 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2482 ordinal=2482 -->
## Functions

Functions


              Icon, description, panel and diagram—Prints the VI description, icon and connector pane,           2
               front panel, and block diagram.
            Documentation: Using the panel—Prints the VI description, front panel, and controls and
           3 indicators, including data types, names, and descriptions. LabVIEW prints the controls and
               indicators in tabbing order.
            Documentation: Using as a subVI—Prints the VI description, icon and connector pane, and
            connected controls and indicators, including data types, names, and descriptions. LabVIEW
           4               prints the controls and indicators in tabbing order. This format is similar to the format of the VI
           and function reference topics in the LabVIEWHelp.
            Documentation: Complete—Prints the VI description, icon and connector pane, front panel,
           5 controls and indicators, including data types, names, and descriptions, block diagram, a list of
              subVIs, including icons, names, and paths, revision history information, and the VI hierarchy.
            Documentation: Custom—Uses the values you wire to custom contents options to determine
           6            which data to print.

               •      report type (Quick Print) —

            report type sets the type of report you want to create.

           0 Quick Print (default)—Prints the report immediately.
              Excel (Report Generation Toolkit)—Creates a report in Excel and returns a reference to it in
           1             report out so you can use other Report Generation VIs to customize, save, or print the report.
           Word (Report Generation Toolkit)—Creates a report in Word and returns a reference to it in
           2             report out so you can use other Report Generation VIs to customize, save, or print the report.
           HTML—Creates an HTML report and returns a reference to it in report out so you can use other
           3 Report Generation VIs to customize, save, or print the report. When an HTML report is saved, a
           JPEG file is created and saved along with the HTML file.
            Standard Report (Windows)—Creates a report and returns a reference to it in report out so you           4            can use other Report Generation VIs to customize or print the report.

               •       error in (no error) —

             error in describes error conditions that occur before this node runs. This input provides
            standard error in functionality.

               •     custom contents options —

          custom contents options sets which data to print or include in the report if you set contents to
           Documentation: Custom.

           You also can use the Printing:Custom properties to set which data to print programmatically.


2482   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2482 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2483 ordinal=2483 -->
## Functions

Functions


•      include VI connector and icon —

   If include VI connector and icon is TRUE, the report includes the VI icon and connector
  pane. The default is FALSE.

•      include VI description —

   If include VI description is TRUE, the report includes the VI description. The default is
  FALSE.

•      include front panel —

   If include front panel is TRUE, the report includes the front panel. The default is FALSE.

•      surround front panel with border —

   If surround front panel with border is TRUE, the VI prints a border around the front panel.
  The default is FALSE.

•         list of controls options —

   list of controls options sets whether to include a list of controls and indicators in the report
  and sets the data to include in the list.

      •      include list of controls —

          If include list of controls is TRUE, the report includes a list of controls and indicators.
     The default is FALSE.

      •         list which controls? —

         list which controls? sets which controls and indicators to include in the list.

      0 all controls (default)—Prints all controls and indicators.
      1 connected controls—Prints only connected controls and indicators.

      •      include control descriptions? —

          If include control descriptions? is TRUE, the report includes control and indicator
       descriptions. The default is FALSE.


                                                © National Instruments 2483

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2483 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2484 ordinal=2484 -->
## Functions

Functions


                           •      include control data types? —

                                 If include control data types? is TRUE, the report includes control and indicator data
                      types. The default is FALSE.


                     •      block diagram options —

                block diagram options sets whether to include the block diagram in the report and how to
                  print structures on the block diagram.

                           •      include block diagram —

                                 If include block diagram is TRUE, the report includes the block diagram. The default is
                    FALSE.

                           •      hidden frames —

                                 If hidden frames is TRUE, the block diagram image includes all visible subdiagrams of
                   each Case, Event, and Stacked Sequence structure, followed by all hidden subdiagrams
                        for each structure. If FALSE (default), the image includes only visible subdiagrams.

                           •      ordered (repeat from higher level if nested) —

                                 If ordered is TRUE, the block diagram image includes all visible subdiagrams of each
                     Case, Event, and Stacked Sequence structure, followed by all subdiagrams for each
                      structure in order, including visible and hidden subdiagrams. If FALSE (default), the
                  image does not repeat visible subdiagrams in the ordered list of subdiagrams.

                                 If Hidden frames is FALSE, the VI ignores this input.


                     •      include VI hierarchy —

                           If include VI hierarchy is TRUE, the report includes the VI hierarchy. The default is FALSE.

                     •      include list of subVIs —

                           If include list of subVIs is TRUE, the report includes a list of subVIs, including icons, names,
              and paths. The default is FALSE.

                     •      include VI history —


2484   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2484 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2485 ordinal=2485 -->
## Functions

Functions


              If include VI history is TRUE, the report includes revision history information. The default is
        FALSE.

         •      include Express VI configuration information —

              If include Express VI configuration information is TRUE, the report includes configuration
        information for any Express VIs on the block diagram. The default is FALSE.


   •      report out —

    report out is a reference to the report whose appearance, data, and printing you want to control.

    You can wire this output to other Report Generation VIs.

   •       error out —

    error out contains error information. This output provides standard error out functionality.


If a front panel is not visible, LabVIEW does not update the values in the objects on the
front panel. If you call a VI whose front panel is not visible and you use the Print VI
Panel or Documentation VI to create an image of the front panel, the image does not
reflect any value changes that occurred when you ran the VI.

If you want the image to reflect value changes, make sure the front panel is open
before any values change. If you do not want to display the front panel but want the
image to reflect value changes, create a Property Node from any front panel terminal
on the block diagram of the VI for which you want to create a front panel image.

You also can use the Front Panel:Get Image and Get Panel Image Scaled methods to
return a front panel image programmatically. Use the VI Documentation VIs to print
specific components of VI documentation or to save the components to a report.

VIVI DocumentationDocumentation

Use the VI Documentation VIs to customize the VI documentation you print or save to a
report. VI documentation can include the icon and connector pane, front panel, block
diagram, VI hierarchy, revision history, controls and indicators, and so on.

                                                    © National Instruments 2485

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2485 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2486 ordinal=2486 -->
## Functions

Functions


         Palette                       Description        Object

       Append                       Creates an image of the front panel of the VI you specify in VI and appends it to a
         Front Panel                         report. Wire data to the VI input to determine the polymorphic instance to use or        Image to                     manually select the instance.        Report

       Append VI                       Creates an image of the block diagram of the VI you specify in VI and appends the        Block                    image to a report. Wire data to the VI input to determine the polymorphic instance
        Diagram to                        to use or manually select the instance.        Report

       Append VI
                    Appends the description of the VI you specify in VI to a report. Wire data to the VI         Description                       input to determine the polymorphic instance to use or manually select the instance.         to Report

       Append VI                    Appends the icon of the VI you specify in VI to a report. Wire data to the VI input to
         Icon to                     determine the polymorphic instance to use or manually select the instance.        Report

       Append VI                    Appends the hierarchy of the VI you specify in VI to a report. Wire data to the VI input         Hierarchy to
                        to determine the polymorphic instance to use or manually select the instance.        Report


       Append VI    Appends the revision history of the VI you specify in VI to a report. Wire data to the
         History to      VI input to determine the polymorphic instance to use or manually select the
        Report         instance.


       Append VI
                    Appends a list of controls and indicators of the VI you specify in VI to a report. Wire
           List of
                      data to the VI input to determine the polymorphic instance to use or manually select
         Controls to
                      the instance.
        Report

       Append VI
                    Appends a list of subVIs of the VI you specify in VI to a report. The list includes subVI
           List of SubVIs


2486   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2486 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2487 ordinal=2487 -->
## Functions

Functions


 Palette               Description
 Object

                 icons, names, and paths. Wire data to the VI input to determine the polymorphic to Report               instance to use or manually select the instance.


AppendAppend FrontFront PanelPanel ImageImage toto ReportReport

Creates an image of the front panel of the VI you specify in VI and appends it to a
report. Wire data to the VI input to determine the polymorphic instance to use or
manually select the instance.

The VI also includes an instance whose connector pane is compatible with versions of
the VI in LabVIEW 6.1 and earlier.


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

                                                    © National Instruments 2487

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2487 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2488 ordinal=2488 -->
## Functions

Functions


               include it in a stand-alone application.

      You also can use the following methods to return a front panel image
       programmatically:

            • Front Panel: Get Image
            • Front Panel: Get Image Scaled
   AppendAppend FrontFront PanelPanel ImageImage toto ReportReport (path)(path)
    VIVI

       Creates an image of the front panel of the VI you specify in VI and appends it to a
       report. Wire data to the VI input to determine the polymorphic instance to use or
      manually select the instance.

      The VI also includes an instance whose connector pane is compatible with versions of
       the VI in LabVIEW 6.1 and earlier.


      Inputs/Outputs

               •     image format (jpeg) —

          image format sets the format in which to save the image.

           0        PNG
                    JPEG
           1
                           (default)
           2          GIF


2488   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2488 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2489 ordinal=2489 -->
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

•      report in —

  report in is a reference to the report whose appearance, data, and printing you want to control.
  Use the Create Report VI to generate this LabVIEW class object.

•       VI —

  VI is the path to the VI whose image you want to append to the report. The default is the path to
  the VI that contains this VI as a subVI.

•      description —

  description is the description of the graphic to display if you open the HTML report in a Web
  browser set to display text only.

•       error in (no error) —

  error in describes error conditions that occur before this node runs. This input provides
  standard error in functionality.

•       visible area only? —

   If visible area only? is TRUE, the VI creates an image of only the currently visible portion of the
  front panel. The default is FALSE.

•    MS Office parameters —


                                                   © National Instruments 2489

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2489 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2490 ordinal=2490 -->
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

               •       VI path out —


2490   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2490 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2491 ordinal=2491 -->
## Functions

Functions


     VI path out returns VI unchanged.

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


                                                    © National Instruments 2491

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2491 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2492 ordinal=2492 -->
## Functions

Functions

   AppendAppend FrontFront PanelPanel ImageImage toto ReportReport
    (refnum)(refnum) VIVI

       Creates an image of the front panel of the VI you specify in VI and appends it to a
       report. Wire data to the VI input to determine the polymorphic instance to use or
      manually select the instance.

      The VI also includes an instance whose connector pane is compatible with versions of
       the VI in LabVIEW 6.1 and earlier.


      Inputs/Outputs

               •     image format (jpeg) —

          image format sets the format in which to save the image.

           0        PNG
                    JPEG
           1
                           (default)
           2          GIF

               •      alignment (default) —

           alignment sets the alignment of the image in a report. (Report Generation Toolkit) For Microsoft
          Word reports, you can use only the LEFT, RIGHT, and MIDDLE options.

           0 (default)—The VI does not add an ALIGN attribute to the <IMG> tag.
           1 LEFT
           2 RIGHT


2492   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2492 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2493 ordinal=2493 -->
## Functions

Functions


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

•       VI —

  VI is a reference to the VI whose data you want to append to the report. The default is a reference
  to the VI that contains this VI as a subVI.

•      description —

  description is the description of the graphic to display if you open the HTML report in a Web
  browser set to display text only.

•       error in (no error) —

  error in describes error conditions that occur before this node runs. This input provides
  standard error in functionality.

•       visible area only? —

   If visible area only? is TRUE, the VI creates an image of only the currently visible portion of the
  front panel. The default is FALSE.

•    MS Office parameters —

  MS Office parameters (Report Generation Toolkit) specifies the point in a Microsoft Word or
  Excel report where you want an insertion to occur. The VI ignores this input for HTML reports.

  You can specify a bookmark in Word or a named range or cell coordinates in Excel. If you set the
  report type to Word but do not specify a bookmark, the insertion occurs at the end of the
  document.


                                                   © National Instruments 2493

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2493 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2494 ordinal=2494 -->
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

2494   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2494 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2495 ordinal=2495 -->
## Functions

Functions


    end out (Report Generation Toolkit) represents the index of the character at the end of the text
    inserted in the Microsoft Word document. The VI ignores this input for HTML reports.

   •       error out —

    error out contains error information. This output provides standard error out functionality.


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
AppendAppend FrontFront PanelPanel ImageImage toto ReportReport (string)(string)
VIVI

Creates an image of the front panel of the VI you specify in VI and appends it to a
report. Wire data to the VI input to determine the polymorphic instance to use or


                                                    © National Instruments 2495

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2495 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2496 ordinal=2496 -->
## Functions

Functions

      manually select the instance.

      The VI also includes an instance whose connector pane is compatible with versions of
       the VI in LabVIEW 6.1 and earlier.


      Inputs/Outputs

               •     image format (jpeg) —

          image format sets the format in which to save the image.

           0        PNG
                    JPEG
           1                           (default)
           2          GIF

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

2496   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2496 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2497 ordinal=2497 -->
## Functions

Functions


  report in is a reference to the report whose appearance, data, and printing you want to control.
  Use the Create Report VI to generate this LabVIEW class object.

•       VI —

  VI is the name of the VI whose data you want to append to the report. The default is the name of
  the VI that contains this VI as a subVI. The VI must be in memory.

•      description —

  description is the description of the graphic to display if you open the HTML report in a Web
  browser set to display text only.

•       error in (no error) —

  error in describes error conditions that occur before this node runs. This input provides
  standard error in functionality.

•       visible area only? —

   If visible area only? is TRUE, the VI creates an image of only the currently visible portion of the
  front panel. The default is FALSE.

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


                                                   © National Instruments 2497

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2497 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2498 ordinal=2498 -->
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


2498   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2498 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2499 ordinal=2499 -->
## Functions

Functions

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

AppendAppend VIVI BlockBlock DiagramDiagram toto ReportReport

Creates an image of the block diagram of the VI you specify in VI and appends the
image to a report. Wire data to the VI input to determine the polymorphic instance to
use or manually select the instance.

      Note You cannot include the Append VI Block Diagram to Report VI in a
       stand-alone application.

You also can use the Get Diagram Image Scaled method to return a block diagram
image programmatically.


                                                    © National Instruments 2499

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2499 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2500 ordinal=2500 -->
## Functions

Functions

            • Append VI Block Diagram to Report (path) VI
            • Append VI Block Diagram to Report (refnum) VI
            • Append VI Block Diagram to Report (string) VI
   AppendAppend VIVI BlockBlock DiagramDiagram toto ReportReport (path)(path) VIVI

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


2500   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:2500 -->

