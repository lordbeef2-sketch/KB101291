# NI_LABVIEW_PROGRAMMING_REFERENCE

<!--SYSTEM_CORPUS id=NI_LABVIEW_PROGRAMMING_REFERENCE format=markdown generated=2026-07-14T12:02:18+00:00 -->
- title: LabVIEW Programming Reference Manual
- source: https://docs-be.ni.com/bundle/labview-api-ref/preprocessedpdf/enus
- source_sha256: 7a54c389b4f3d78e2215f55c9f156124d3668ce61d0d5018094e356004d895ac
- versions: 2024 Q1|2024 Q3|2025 Q1|2025 Q3|2026 Q1
- fidelity: full-text-records

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6001 ordinal=6001 -->
## Functions

Functions


Option      Description

                     • One header per segment—

                 Creates one header per segment in the file to which LabVIEW writes the data.
                  Select this option if the acquisition rate of the data changes over time, if you
                 acquire two or more signals at different acquisition rates, or if the list of signals
               you log changes over time.

                     • One header only—

                 Creates only one header in the file to which LabVIEW writes the data. Select this
                option if you acquire the same list of signals at the same constant acquisition
                    rate.

                     • No headers—

                 Creates an empty column for the time data each channel generates. This option
               does not include the data from the x-axis.

                   Note This option is available only when you select the Text (LVM)
                         option from the File Format section.


            Contains the following options:

                     • One column per channel—

                 Creates a separate column for time data each channel generates. This option
                 includes a column of values from the x-axis for every column of values from the y-
                    axis. Select this option if you acquire signals of different types or at different
                  acquisition rates.
X Value
                     • One column only—Columns
                 Creates only one column for the time data the channels generate. This option
                 includes only one column of values from the x-axis. Select this option if you
                 acquire signals at the same acquisition rate.

                     • Empty time column—

              Does not create a header in the file to which LabVIEW writes the data.


                                                    © National Instruments 6001

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6001 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6002 ordinal=6002 -->
## Functions

Functions


        Option      Description

                     Contains the following options:

                                  • Tab—

                       Uses tabs to delimit fields in the text file.

                                  • Comma—
         Delimiter
                       Uses commas to delimit fields in the text file.

                         Note These options are available only when you select the Text (LVM)
                                 option from the File Format section.


                     Contains the description of the measurement file. LabVIEW appends the text you
                      enter in this text box to the header of the file. This text box is unavailable when you
                       select the Microsoft Excel (.xlsx) option from the File Format section.

                                  • Advanced—          File
         Description                          Displays the Configure User Defined Properties dialog box when you select the
                        Binary (TDMS) or Binary with XML Header (TDM) option from the File Format
                            section. Displays the Configure Advanced Excel Options dialog box when you
                            select the Microsoft Excel (.xlsx) option. This button is unavailable when you
                            select the Text (LVM) option.


      Inputs/Outputs

               •       error in (no error) —

            Describes error conditions that occur before this node runs.

               •     Comment —

          Appends a comment to each data set written to the measurement file. This input is unavailable
          when you select the Microsoft Excel (.xlsx) option from the File Format section.

               •      new_file —


6002   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6002 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6003 ordinal=6003 -->
## Functions

Functions


   If TRUE, stops writing to the current file, creates the next file in the series, and writes to that file
  instead. This input is available only when you select the Save to series of files (multiple files)
  option.

•      Signals —

  Contains the input signal or signals.

   If you wire two or more signals with the same name to the Signals input, LabVIEW appends an
  integer to the end of the names written in the file, which enforces unique channel names. For
  example, if you wire two signals named Sine to the Signals input, LabVIEW writes the names as
  Sine and Sine 1.

        Note To change or customize how a signal name displays, use the Set Dynamic Data
            Attributes Express VI.

•      Flush? (T) — Specifies whether LabVIEW writes data to the Microsoft Excel file each time
   after this Express VI runs. If the value is FALSE, LabVIEW does not write the data to the Microsoft
  Excel file. Instead, LabVIEW stores the data in a temporary file. If the value is TRUE, LabVIEW
  writes the data from the temporary file to the Excel file and then purges the temporary file. The
  default is TRUE.

        Note If you use this Express VI to write data iteratively, setting the Flush? input to
         TRUE at each iteration might affect the writing performance negatively. National
           Instruments recommends that you wire a FALSE value to this input until the last
            iteration of the entire writing process. For the last iteration, you can wire a TRUE
           value to this input to write all data to the Excel file.

•      Filename —

  Specifies the name of the file to which you want to write data. If Filename is not wired, the VI
  uses the Filename specified in the configuration dialog box.

•     DAQmx Task —

  Specifies the DAQmx task to use to populate data on the DAQmx Properties page of the
  Configure User Defined Properties dialog box.

•      Reset — Specifies whether you want to reset the data file when you run this Express VI
   iteratively. LabVIEW ignores this input when you run this Express VI in the first iteration. During
  the second and subsequent iterations, if the value is FALSE, this Express VI appends data to a file
    if the file already exists. Depending on your configuration for this Express VI, if the value is TRUE,
   this Express VI renames, overwrites, or skips a file if the file already exists. The default is FALSE.

                                                   © National Instruments 6003

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6003 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6004 ordinal=6004 -->
## Functions

Functions

               •      Enable —

            Enables or disables the Express VI. The default is ON or TRUE.

               •       error out —

            Contains error information. This output provides standard error out functionality.

               •      Saving Data —

             Indicates if the Express VI is saving the data.

               •      Filename Out —

            Returns the name of the file.


           Note The behavior of this VI changes depending upon the target. If the
               current target does not or might not have a host computer connected, the
               configuration dialog box displays warnings next to options that are invalid
              without a host. If you configure this VI to prompt for input and run the VI on a
                target with no user interface, such as the Real-Time Module with no host
             computer connected, this VI returns an error.

      You can also use the Storage/DataPlugin VIs to read from and write to .tdm files, or
      you can use the TDM Streaming functions to read from and write to .tdms files.

     Examples

       Refer to the following example files included with LabVIEW.

            • labview\examples\File IO\TDMS\Express Read and Write\TDMS
        Express Write Data (Time and Frequency Domain).vi
            • labview\examples\File IO\TDMS\Express Read and Write\TDMS
        Express Write Data (Time Domain).vi
            • labview\examples\File IO\Spreadsheet\Excel\Write Excel
        File.vi


6004   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6004 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6005 ordinal=6005 -->
## Functions

Functions

ReportReport

Generates a preformatted report that contains VI documentation, data the VI returns,
and report properties, such as the author, company, and number of pages.


Dialog Box Options

 Option      Description

             Contains the following options:

                       • Report title—

                   Specifies the title of the report.

                       • Author name—

                   Specifies the author of the report.

                       • Company name—

                   Specifies the name of the company.
 Report
 Information     • Operator name—

                   Specifies the name of the operator who generated the data for the report.

                       • Report print date—

                  Includes the date of the report.

                       • Report print time—

                  Includes the time of the report.

                       • Page number—


                                                    © National Instruments 6005

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6005 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6006 ordinal=6006 -->
## Functions

Functions


        Option      Description

                          Includes the current page number of the report.

                                   •  Total pages—

                          Includes the total number of pages of the report.

                           This option prints the total number of pages in the following formats:
            ◦ (Word 2000, XP, and 2003) Page xof n
            ◦ (Word 2007) x/n
                                   •  VI documentation (appendix)—

                          Includes the VI documentation in an appendix.

                                   • Comments—

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

        Data Input       • Include graph (data input 2)—
        2
                            Specifies whether to include a graph with the data.


6006   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6006 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6007 ordinal=6007 -->
## Functions

Functions


 Option      Description

                       • Title—

                   Specifies the title for the data.

                       •  Y-axis label—

                   Specifies the label for the y-axis.

                       • Include table—

                   Specifies whether to include a table with the data.


               Specifies where to send the report. You can export the report to a Microsoft Word
 Destination  document or a Microsoft Excel worksheet, print to a printer, or save the report in
          HTML format for use on a Web page.


 Path to             Path where you want to save the report. save report

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


                                                    © National Instruments 6007

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6007 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6008 ordinal=6008 -->
## Functions

Functions


            Enables or disables the Express VI. The default is TRUE.

               •     Saved Report Path —

            Returns the path where this Express VI saves the report.

               •       error out —

            Contains error information. This output provides standard error out functionality.

     SignalSignal ManipulationManipulation

      Use the Signal Manipulation Express VIs to manipulate signals and to perform data
       type conversions.

           Note The VIs on this palette return an error if an input signal is a waveform
              with a dt less than or equal to zero.


         Palette                       Description
        Object

                    Merges two or more supported signals, such as scalar numerics, 1D or 2D arrays of
                      numerics, scalar Booleans, 1D or 2D arrays of Booleans, waveforms, or 1D arrays of
        Merge
                     waveforms, into a single output. Resize the function to add inputs. This function
         Signals
                       automatically appears on the block diagram when you wire a signal output to the
                       wire branch of another signal.

                          Splits two or more signals into component signals. Resize the function to add
          Split Signals
                       outputs.

                      Accepts multiple signals as inputs and returns only the signals you select. You can
         Select
                        specify which signals to include in the output and change the order of the input
         Signals
                          signals.


6008   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6008 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6009 ordinal=6009 -->
## Functions

Functions


Palette              Description
Object

             Performs an alignment of signals by changing the start time or performs aAlign and             resampling of signals by changing the time delta. This Express VI returns theResample              adjusted signals.


               Collects input signals and returns the most recent data, up to the specified
          maximum number of samples per channel. When you call this Express VI repeatedly
Collector     and the Express VI reaches the maximum number of samples per channel, the
              Express VI discards the oldest data and adds the newest data to the collected
             samples.


Sample       Acquires a large number of data points and compresses the data points into a
Compression  smaller number of points.


             Uses triggering to extract a segment out of a signal. The trigger conditions can be
Trigger and   based on a start or stop trigger threshold or can be static. When a trigger condition is
Gate            static, the trigger occurs immediately and this Express VI returns a predefined
           number of samples.


Relay         Configures a relay switch that turns the input signal on and off.


            Appends signals to each other. You can use this Express VI to append a signal to the
Append      end of another signal, append signals in a combined signal to each other, append
Signals       the same signal to the end of each signal in a combined signal, or append a
            combined signal to another combined signal.


Repack       Accepts signals with any number of data points and produces packets of signals that
Values       use a packet size you specify.

Extract
Portion of     Extracts portions of data from the input signals and returns the extracted data. You
Signal


                                                    © National Instruments 6009

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6009 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6010 ordinal=6010 -->
## Functions

Functions


         Palette                       Description
        Object

                    can extract a single point or a range of data, and you can extract data by time or
                        index. You also can find the time and index of the first occurrence of a value.


                       Stores data from previous iterations of a loop and passes the data after the specified        Delay Values                  number of iterations occur.

        Convert
        from         Converts the dynamic data type to numeric, Boolean, waveform, and array data
       Dynamic      types for use with other VIs and functions.
        Data

        Convert to                      Converts numeric, Boolean, waveform and array data types to the dynamic data
       Dynamic                      type for use with Express VIs.        Data


        Group Digital Groups digital data into a digital data array and groups digital waveforms into a
         Signals        digital waveform array.

         Set Dynamic
        Data          Sets the attributes of the dynamic data you wire to Signals In.
          Attributes

        Get Dynamic
        Data          Retrieves the attributes of the dynamic data you wire to Signals In.
          Attributes

     MergeMerge SignalsSignals

      Merges two or more supported signals, such as scalar numerics, 1D or 2D arrays of
       numerics, scalar Booleans, 1D or 2D arrays of Booleans, waveforms, or 1D arrays of
      waveforms, into a single output. Resize the function to add inputs. This function
       automatically appears on the block diagram when you wire a signal output to the wire
      branch of another signal.


6010   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6010 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6011 ordinal=6011 -->
## Functions

Functions


Inputs/Outputs

   •      input signal —

    input signal specifies the signal you want to combine with another signal.

   •      input signal —

   •     combined signal —

    combined signal returns the combined signals. You can wire the dynamic data type to a graph or
    numeric indicator. For example, if you wire the combined signal to a graph indicator, LabVIEW
    represents each signal as an individual plot.


This function outputs a single wire with a dynamic data type. Internally, an array of
waveforms composes this wire. When you merge signals, each input signal becomes
one or more elements in the waveform array.

SplitSplit SignalsSignals

Splits two or more signals into component signals. Resize the function to add outputs.

Each unit of the original signal contains the time information (t0 and dt) of the
waveform. When LabVIEW splits the signal, each resulting signal retains the original
information.


Inputs/Outputs

   •     combined signal —

    combined signal contains a signal you want to split into component signals.

   •      output signal —

                                                    © National Instruments 6011

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6011 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6012 ordinal=6012 -->
## Functions

Functions


           output signal returns the component signals.

      SelectSelect SignalsSignals

       Accepts multiple signals as inputs and returns only the signals you select. You can
       specify which signals to include in the output and change the order of the input
        signals.


      Dialog Box Options

        Option  Description

                 Contains the following options:

                            • Unselected signals—

                          Lists all the input signals. The index number associated with each signal reflects the
                     order of the input signals on the input wire.

                            • Selected signals—

                          Lists the signals in the order in which you selected them. The original index number
                    remains associated with the signal. If you wire the Selector Input input, the VI uses         Select
                     the signals that this input specifies instead.         Signals
                            • Select—

                  Moves a signal from the Unselected signals list to the Selected signals list.

                            • Deselect—

                  Moves a signal from the Selected signals list to the Unselected signals list.

                            • Sort—


6012   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6012 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6013 ordinal=6013 -->
## Functions

Functions


 Option  Description

              Sorts the signals in the Selected signals list in numerical order based on the index
            number.


Inputs/Outputs

   •      Signals —

    Contains the input signal or signals.

   •       error in (no error) —

    Describes error conditions that occur before this node runs.

   •      Selector Input —

    Selects which signals to include from the Signals input.

    This input can be a set of signals with the last point in each signal representing a true or false.
   When the last point in a signal represents true, the corresponding signal is included. This input
    also can be one signal, with each data point representing a true or false. Numeric values greater
    than or equal to 0.5 are true, and values less than 0.5 are false. If Selector Input is not wired, the
     VI uses the Selected signals specified in the configuration dialog box.

   •      Signal Out —

    Returns the output signal.

   •       error out —

    Contains error information. This output provides standard error out functionality.


Components

Moves a signal from the Selected signals list to the Unselected signals list.

Moves a signal from the Unselected signals list to the Selected signals list.

Sorts the signals in the Selected signals list in numerical order based on the index

                                                    © National Instruments 6013

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6013 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6014 ordinal=6014 -->
## Functions

Functions

      number.

        Lists the signals in the order in which you selected them. The original index number
      remains associated with the signal. If you wire the Selector Input input, the VI uses the
       signals that this input specifies instead.

        Lists all the input signals. The index number associated with each signal reflects the
       order of the input signals on the input wire.

      AlignAlign andand ResampleResample

      Performs an alignment of signals by changing the start time or performs a resampling
       of signals by changing the time delta. This Express VI returns the adjusted signals.


      Dialog Box Options

        Option        Description

                      Contains the following options:

                                     •  Single segment—

         Acquisition        Aligns and/or resamples each iteration separately.
        Type
                                     • Continuous—

                             Aligns and/or resamples all iterations as one continuous segment.


         Align          Aligns the signals to have the same start time.

        Alignment
                      Contains the following options:
         Interval


6014   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6014 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6015 ordinal=6015 -->
## Functions

Functions


Option        Description

                        • Global—

                    Aligns the start and end times of signals by adding zero values to the beginning
                    of the signal that starts last and to the end of the signal that ends first.

                        • Common—

                    Aligns the start and end times of signals by using the start time of the signal
                   that starts last and the end time of the signal that ends first.


Resample    Resamples the signals to have the same sampling interval.

              Contains the following options:

                        • Lowest dt—

                Resamples all the signals to have the same sampling interval as the signal with
                  the smallest sampling interval.

                        •  Specific dt—

Resampling      Resamples all the signals to have a user-defined sampling interval.
Interval
        ◦ dt—

                    Sampling interval you define. The default is 1.

                        • Reference signal—

                Resamples all the signals to have the same sampling interval as a reference
                     signal.


           When resampling, you might need to add points to the signal. Interpolation Mode
               controls how LabVIEW calculates the amplitude of the new points. InterpolationInterpolation
           Mode contains the following options:Mode
                        • Linear—


                                                    © National Instruments 6015

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6015 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6016 ordinal=6016 -->
## Functions

Functions


        Option        Description

                          Returns an output sample value equal to a linear interpolation between the two
                           input samples that are closest to the output sample value in time.

                                     • Coerce—

                          Returns an output sample value equal to the input sample value that is closest
                            to the output sample value in time.

                                     • Spline—

                         Uses the spline interpolation algorithm to compute the resampled values.

                                     • FIR filter—

                         Uses an FIR filter to compute the resampled values.

                      Contains the following options:

                                     •  Alias rejection (dB)—

                             Specifies the minimum attenuation level of signal components aliased after any
                          resampling operation. The default is 120. This option is available only when you        FIR Filter
                              select FIR filter.        Parameters
                                     • Normalized bandwidth—

                             Specifies the fraction of the new sampling rate that is not attenuated. The
                             default is 0.4536. This option is available only when you select FIR filter.


                       Defines whether an input signal is an open or closed interval. The default is TRUE,
       Open        which selects an open interval. For example, assume an input signal has t0 = 0, dt =
         interval        1, and Y = {0, 1, 2}. An open interval returns a final time value of 2. A closed interval
                        returns a final time value of 3.


                        Displays sample input signals you can use as a reference to determine how the
       Sample       configuration options you select affect the actual input signals.
        Input Data
                                     If you wire data to the Express VI and run it, Sample Input Data displays real data. If


6016   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6016 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6017 ordinal=6017 -->
## Functions

Functions


 Option        Description

             you close and reopen the Express VI, Sample Input Data displays sample data until
             you run the VI again.


               Displays a preview of the measurement. The Result Preview plot indicates the value
                of the selected measurement with a dotted line.
 Result                        If you wire data to the Express VI and run the VI, Result Preview displays real data. If
 Preview             you close and reopen the Express VI, Result Preview displays sample data until you
              run the VI again. If the cutoff frequency values are invalid, Result Preview does not
                display valid data.


Inputs/Outputs

   •       error in (no error) —

    Describes error conditions that occur before this node runs.

   •      Reset —

    Controls the initialization of the internal state of the VI. The default is FALSE.

   •      Signals 2 —

    Contains the input signal(s).

   •      Signals —

    Contains the input signal or signals.

   •      Reference Signal —

    Contains a reference signal whose sampling interval is used as the rate at which this Express VI
    resamples the input signals. If you wire a value to this input, the wired value overrides the value
    you set in the configuration dialog box.

   •      dt —

     Specifies a sampling interval you define. If you wire a value to this input, the wired value


                                                    © National Instruments 6017

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6017 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6018 ordinal=6018 -->
## Functions

Functions


             overrides the value you set in the configuration dialog box.

               •     Resampled Signals —

            Returns the resampled signals.

               •       error out —

            Contains error information. This output provides standard error out functionality.

               •     Resampled Signals 2 —

            Returns the resampled signals.

      CollectorCollector

       Collects input signals and returns the most recent data, up to the specified maximum
      number of samples per channel. When you call this Express VI repeatedly and the
       Express VI reaches the maximum number of samples per channel, the Express VI
       discards the oldest data and adds the newest data to the collected samples.


      Dialog Box Options

        Option              Description

      Maximum number    Specifies the maximum number of samples per channel you want the
         of samples           Express VI to collect. The default is 1000.


      Inputs/Outputs

               •      Signals —


6018   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6018 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6019 ordinal=6019 -->
## Functions

Functions


    Contains the input signal or signals.

   •      Reset —

    Controls the initialization of the internal state of the VI. The default is FALSE.

   •       error in (no error) —

    Describes error conditions that occur before this node runs.

   •      Enable —

    Enables or disables the Express VI. The default is ON or TRUE.

   •      Collected Signals —

    Returns the most recent samples of collected data.

   •       error out —

    Contains error information. This output provides standard error out functionality.


Examples

Refer to the following example files included with LabVIEW.

  • labview\examples\Express VIs\Express VI - Collector.vi

Components

Specifies the maximum number of samples per channel you want the Express VI to
collect. The default is 1000.

SampleSample CompressionCompression

Acquires a large number of data points and compresses the data points into a smaller
number of points.


                                                    © National Instruments 6019

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6019 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6020 ordinal=6020 -->
## Functions

Functions


      Dialog Box Options

        Option        Description

                       Contains the following option:

                                      • Reduction factor—        Reduction
         Specifications                      Number of points in the Signals input to reduce to one point in the resulting
                                signal. The default is 10.

                       Contains the following options:

                                      • Minimum—

                         Reduces the Signals input by using the lowest value in each segment.

             ◦ Minimum Plot Color—

                                Color of the Minimum plot. This option is available only when you place a
                            checkmark in the Minimum checkbox.

                                      • Maximum—

                         Reduces the Signals input by using the highest value in each segment.        Reduction
       Methods             ◦ Maximum Plot Color—

                                Color of the Maximum plot. This option is available only when you place a
                            checkmark in the Maximum checkbox.

                                      • Last—

                         Reduces the Signals input by using the last point in each segment.

             ◦ Last Plot Color—

                                Color of the Last plot. This option is available only when you place a
                            checkmark in the Last checkbox.


6020   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6020 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6021 ordinal=6021 -->
## Functions

Functions


 Option        Description

                          • Median—

                  Reduces the Signals input by using the median value of the points in each
                  segment.

         ◦ Median Plot Color—

                        Color of the Median plot. This option is available only when you place a
                     checkmark in the Median checkbox.

                          • Mean—

                  Reduces the Signals input by using the mean value of the points in each
                  segment.

         ◦ Mean Plot Color—

                        Color of the Mean plot. This option is available only when you place a
                     checkmark in the Mean checkbox.


                Displays the input signal.

 Input Signal     If you wire data to the Express VI and run it, Input Signal displays real data. If you
                close and reopen the Express VI, Input Signal displays sample data until you run
               the Express VI again.


                Displays a preview of the measurement. The Result Preview plot indicates the
                value of the selected measurement with a dotted line.
 Result                         If you wire data to the Express VI and run the VI, Result Preview displays real data.
 Preview                         If you close and reopen the Express VI, Result Preview displays sample data until
              you run the VI again. If the cutoff frequency values are invalid, Result Preview does
               not display valid data.


Inputs/Outputs

   •       error in (no error) —


                                                    © National Instruments 6021

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6021 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6022 ordinal=6022 -->
## Functions

Functions


            Describes error conditions that occur before this node runs.

               •      Reset —

            Controls the initialization of the internal state of the VI. The default is FALSE.

               •      Enable —

            Enables or disables the Express VI. The default is ON or TRUE.

               •      Signals —

            Contains the input signal or signals.

               •      Data Valid —

             Indicates whether the data is valid.

               •     Median —

            Returns the median value of the points in each bin as the resulting signal output.

               •     Minimum —

            Returns the lowest value in each bin as the resulting signal output.

               •      Last —

            Returns the last point in each bin as the resulting signal output.

               •     Mean —

            Returns the mean value of the points in each bin as the resulting signal output.

               •     Maximum —

            Returns the highest value in each bin as the resulting signal output.

               •       error out —

            Contains error information. This output provides standard error out functionality.


6022   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6022 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6023 ordinal=6023 -->
## Functions

Functions

Examples

Refer to the following example files included with LabVIEW.

  • labview\examples\Express VIs\Express VI - Sample
   Compression.vi

Components

Color of the Median plot. This option is available only when you place a checkmark in
the Median checkbox.

Color of the Mean plot. This option is available only when you place a checkmark in
the Mean checkbox.

Color of the Last plot. This option is available only when you place a checkmark in the
Last checkbox.

Color of the Maximum plot. This option is available only when you place a checkmark
in the Maximum checkbox.

Color of the Minimum plot. This option is available only when you place a checkmark
in the Minimum checkbox.

Displays the input signal.

Reduces the Signals input by using the median value of the points in each segment.

Reduces the Signals input by using the mean value of the points in each segment.

Reduces the Signals input by using the last point in each segment.

Reduces the Signals input by using the highest value in each segment.

Reduces the Signals input by using the lowest value in each segment.

Number of points in the Signals input to reduce to one point in the resulting signal.
The default is 10.


                                                    © National Instruments 6023

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6023 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6024 ordinal=6024 -->
## Functions

Functions

       Displays a preview of the measurement. The Result Preview plot indicates the value of
       the selected measurement with a dotted line.

      TriggerTrigger andand GateGate

      Uses triggering to extract a segment out of a signal. The trigger conditions can be
      based on a start or stop trigger threshold or can be static. When a trigger condition is
         static, the trigger occurs immediately and this Express VI returns a predefined number
       of samples.


      Dialog Box Options

        Option   Description

                  Contains the following options:

                              • Threshold—

                     Uses a threshold to indicate when to start triggering.

          ◦  Start sense—

                             Specifies on what edge of the signal to start taking samples. The options are
                            Rising edge, Rising or Falling edge, or Falling edge. This option is available only
         Start          when you select Threshold.
         Trigger
          ◦  Start level—

                         Amplitude that the signal must cross in the Start sense direction before the
                           Express VI starts taking samples. The default is 0. This option is available only
                     when you select Threshold.

          ◦ Pre samples—

                             Specifies the number of samples that occur before the start trigger to return.


6024   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6024 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6025 ordinal=6025 -->
## Functions

Functions


Option   Description

                The default is 0. This option is available only when you select Threshold.

                 • Immediate—

              Begins the triggering immediately. The start of the signal is the start trigger.

          Contains the following options:

                 • Number of samples—

            Ends the triggering when the Express VI collects Samples.

      ◦ Samples—

                    Specifies the number of samples to collect before stopping the trigger. The
                   default is 1000.

                 • Threshold—
Stop             Uses a threshold to indicate when to start triggering.
Trigger
      ◦ Stop sense—

                    Specifies on what edge of the signal to stop taking samples. The options are
                   Rising edge, Rising or Falling edge, or Falling edge. This option is available only
              when you select Threshold.

      ◦ Stop level—

                 Amplitude that the signal must cross in the Stop sense direction before the
                  Express VI stops taking samples. The default is 0. This option is available only
              when you select Threshold.

          Contains the following options:

                 •  Trigger channel—
General
               Specifies the channel to use if the dynamic data type input contains multiple
                signals. The default is 0.


                                                    © National Instruments 6025

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6025 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6026 ordinal=6026 -->
## Functions

Functions


        Option   Description

                              • Reset after each trigger found—

                       Resets the trigger conditions after finding each trigger. When you select this option,
                      the Trigger and Gate Express VI does not buffer data with each iteration of a loop.
                        Select this checkbox when you have a new data set for each iteration and you want
                        to find data related only to the first trigger point. Deselect this checkbox when you
                   want to pass only one set of data into a loop and then call the Trigger and Gate
                       Express VI in a loop to get all the triggers in the data.

                       Note When you do not select this option, the Trigger and Gate Express VI
                                  buffers data. In this case, if the Trigger and Gate Express VI is called in a
                                 loop, it can start a backlog of data if there is new data for each loop
                              (because one set of data can contain several trigger points). Because
                                there is no reset, it buffers all the data from each loop so that it can find
                                          all the triggers, but all the triggers might not be found.

                              • Remain triggered after trigger found—

                    Remains triggered after finding a trigger. This option is available only when you
                         select the Threshold option in the Start Trigger section.

                              • Hysteresis—

                         Specifies the amount above and below Start level or Stop level through which
                       Signals must pass before a trigger level crossing is detected. The default is 0.

                    Use trigger hysteresis to prevent noise from causing a false trigger. For a rising edge
                        Start sense or Stop sense, the signal must pass below Start level or Stop level
                    minus Hysteresis before detecting a trigger level crossing. For a falling edge Start
                     sense or Stop sense, the signal must pass above Start level or Stop level plus
                       Hysteresis before detecting a trigger level crossing.

                  Contains the following options:

                              • Automatic number of samples—
        Output
       segment      Specifies that the Express VI returns the portion of the signal that matches the
          size            trigger criteria.

                              • Number of output samples—


6026   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6026 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6027 ordinal=6027 -->
## Functions

Functions


 Option   Description

                Specifies the number of samples to include in each output segment. This option is
                available only if the Automatic number of samples checkbox does not contain a
              checkmark.


           Displays the input signal.

                 If you wire data to the Express VI and run it, Input Signal displays real data. If you close
         and reopen the Express VI, Input Signal displays sample data until you run the Express VI Input
           again. Signal
                   • Number of points in the data—

                Specifies the number of points in the data. The default is 4400.


           Displays a preview of the measurement. The Results Preview plot indicates the value of
          the selected measurement with a dotted line.
 Results                 If you wire data to the Express VI and run the VI, Results Preview displays real data. If you
 Preview           close and reopen the Express VI, Results Preview displays sample data until you run the
            VI again. If the cutoff frequency values are invalid, Results Preview does not display valid
           data.


Inputs/Outputs

   •       error in (no error) —

    Describes error conditions that occur before this node runs.

   •      Signals —

    Contains the input signal or signals.

   •      Reset —

    Controls the initialization of the internal state of the VI. The default is FALSE.

   •      Data Index —


                                                    © National Instruments 6027

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6027 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6028 ordinal=6028 -->
## Functions

Functions


            Contains the index of the detected trigger. If this Express VI is in a loop, wire Data Index to the
              iteration terminal of the loop.

               •     Manual Trigger —

              Starts the trigger immediately and overrides the Start Trigger settings you configure. The default
                is FALSE.

               •      Data Available —

             Indicates if data is available that meets the requirements of the trigger.

               •       error out —

            Contains error information. This output provides standard error out functionality.

               •      Previous Signals —

            Contains the last triggered output data. If no data meets the requirements of the trigger, this
           output contains the most recent segment that meet the requirements of the trigger.

               •      Triggered Signals —

            Returns the resulting segment between Start Trigger and Stop Trigger. If no data meets the
            requirements of the trigger, this output returns an empty signal.

     RelayRelay

       Configures a relay switch that turns the input signal on and off.


      Dialog Box Options

        Option        Description

        Output when
                       Contains the following options:
        Relay Off


6028   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6028 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6029 ordinal=6029 -->
## Functions

Functions


 Option        Description

                          • Empty data—

                     Indicates that if Enable is FALSE, the Result output is empty.

                          • 0 values—

                     Indicates that if Enable is FALSE, the Result output is a signal with all the
                      characteristics of the input signal except that the amplitude is zero.

               Contains the following option:

 Test                   • Enable—
 Configuration
                   Enables or disables the Express VI. The default is OFF.


                Displays the input signal.

 Input Signal     If you wire data to the Express VI and run it, Input Signal displays real data. If you
                close and reopen the Express VI, Input Signal displays sample data until you run
               the Express VI again.


                Displays a preview of the measurement. The Result Preview plot indicates the
               value of the selected measurement with a dotted line.
 Result                         If you wire data to the Express VI and run the VI, Result Preview displays real data. If
 Preview             you close and reopen the Express VI, Result Preview displays sample data until you
              run the VI again. If the cutoff frequency values are invalid, Result Preview does not
                display valid data.


Inputs/Outputs

   •      Signals —

    Contains the input signal or signals.

   •      Enable —


                                                    © National Instruments 6029

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6029 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6030 ordinal=6030 -->
## Functions

Functions


            Enables or disables the Express VI. The value you wire to this input overrides the value set in the
            Configure Relay dialog box. The default is OFF.

               •       error in (no error) —

            Describes error conditions that occur before this node runs.

               •       error out —

            Contains error information. This output provides standard error out functionality.

               •      Result —

            Returns the resulting data based on the configuration of the Express VI.


     Examples

       Refer to the following example files included with LabVIEW.

            • labview\examples\Express VIs\Express VI - Relay.vi

     Components

       Displays a preview of the measurement. The Result Preview plot indicates the value of
       the selected measurement with a dotted line.

       Displays the input signal.

      Enables or disables the Express VI. The default is OFF.

       Indicates that if Enable is FALSE, the Result output is empty.

       Indicates that if Enable is FALSE, the Result output is a signal with all the
        characteristics of the input signal except that the amplitude is zero.

     AppendAppend SignalsSignals

      Appends signals to each other. You can use this Express VI to append a signal to the
      end of another signal, append signals in a combined signal to each other, append the

6030   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6030 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6031 ordinal=6031 -->
## Functions

Functions

same signal to the end of each signal in a combined signal, or append a combined
signal to another combined signal.


Dialog Box Options

 Option     Description

            Displays an input signal.
 Input                    If you wire data to the Express VI and run it, Input Signal A displays real data. If you
 Signal A            close and reopen the Express VI, Input Signal A displays sample data until you run the
              VI again.


            Displays an input signal.
 Input                    If you wire data to the Express VI and run it, Input Signal B displays real data. If you
 Signal B            close and reopen the Express VI, Input Signal B displays sample data until you run the
              VI again.


 Append   Appends signals only if the t0 aligns with the end of the previous signal and the dt
 only if t0   matches. If a checkmark appears in the checkbox and the t0 does not align or the dt
 aligns     does not match, the VI returns an error. If you want to append signals even if the t0
 and dt     does not align or the dt does not match, remove the checkmark from the Append only
 matches     if t0 aligns and dt matches checkbox.


            Displays a preview of the appended signal(s).
 Appended
 Signals       If you wire data to the Express VI and run it, Appended Signals Preview displays real
 Preview    data. If you close and reopen the Express VI, Appended Signals Preview displays
           sample data until you run the VI again.


                                                    © National Instruments 6031

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6031 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6032 ordinal=6032 -->
## Functions

Functions

      Inputs/Outputs

               •      Input Signal A —

            Contains a single or combined signal.

               •      Input Signal B —

            Contains a single or combined signal.

               •       error in (no error) —

            Describes error conditions that occur before this node runs.

               •     Appended Signals —

            Returns the appended signal(s).

               •       error out —

            Contains error information. This output provides standard error out functionality.


      A combined signal is comprised of one or more signals using the Merge Signals
       function.

           If you wire only a combined signal to Input Signal A, each signal in the combined
       signal appends the following signal to create one signal as a result. If you wire a
      combined signal to Input Signal A and a single signal to Input Signal B, the Express VI
      appends Input Signal B to the end of each of the signals in Input Signal A. If you wire a
      combined signal to Input Signal A and another combined signal to Input Signal B, the
       Express VI appends the first signal within Input Signal B to the end of the first signal
       within Input Signal A, the second signal within Input Signal B to the end of the second
       signal within Input Signal A, and so on. The result has as many combined signals as
       the input with the least number of combined signals. If Input Signal A is empty or not
       wired and you wire a single signal to Input Signal B, the Express VI returns Input Signal
       B. If you wire only a combined signal to Input Signal B, each signal in the combined
       signal appends the following signal to create one signal as a result.


6032   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6032 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6033 ordinal=6033 -->
## Functions

Functions

Examples

Refer to the following example files included with LabVIEW.

  • labview\examples\Express VIs\Express VI - Append
   Signals.vi

Components

Appends signals only if the t0 aligns with the end of the previous signal and the dt
matches. If a checkmark appears in the checkbox and the t0 does not align or the dt
does not match, the VI returns an error. If you want to append signals even if the t0
does not align or the dt does not match, remove the checkmark from the Append only
if t0 aligns and dt matches checkbox.

Displays an input signal.

Displays an input signal.

Preview of the resulting signal(s)

Displays a preview of the appended signal(s).

RepackRepack ValuesValues

Accepts signals with any number of data points and produces packets of signals that
use a packet size you specify.


Dialog Box Options

 Option             Description

 Output segment
                      Specifies the number of samples to include in each output segment. The
 size


                                                    © National Instruments 6033

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6033 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6034 ordinal=6034 -->
## Functions

Functions


        Option             Description

                              default is 100.


      Inputs/Outputs

               •      Signals —

            Contains the input signal or signals.

               •       error in (no error) —

            Describes error conditions that occur before this node runs.

               •      Data Index —

            Contains the index of the repacked values. When the Express VI is in a While Loop, wire Data
            Index to the iteration terminal to take a larger array and iteratively generate packets of smaller
               size. If you do not wire Data Index to the iteration terminal, smaller data segments are collected
             into one larger packet.

               •      Data Available —

             Indicates if data is available to make a packet.

               •      Result —

            Returns the resulting data based on the configuration of the Express VI.

               •       error out —

            Contains error information. This output provides standard error out functionality.


      To take a larger array and iteratively generate packets of smaller size, place the Repack
       Values Express VI in a While Loop and wire the Data Index input to the iteration
       terminal. Select the packet size for the Repack Values Express VI. The VI reads the
       Signals input once into a buffer during the first iteration of the While Loop. LabVIEW
       ignores this input for subsequent iterations. On each loop iteration, the Result output
       returns a segment of data starting from the first data point in the buffer. The Data
       Available output remains TRUE until there are not enough data points left to make a

6034   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6034 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6035 ordinal=6035 -->
## Functions

Functions

packet.

To collect smaller data segments into one larger packet, place the Repack Values
Express VI in a While Loop and do not wire the Data Index input or wire a value of 0 to
the Data Index input. The VI accepts new input on every loop iteration. The Data
Available output remains FALSE until the VI has accepted enough data points to make
a packet of the size you specified. When this Express VI returns the result packet, the
Data Available output is TRUE. On the next iteration, it reverts back to FALSE.

Components

Specifies the number of samples to include in each output segment. The default is 100.

ExtractExtract PortionPortion ofof SignalSignal

Extracts portions of data from the input signals and returns the extracted data. You can
extract a single point or a range of data, and you can extract data by time or index. You
also can find the time and index of the first occurrence of a value.


Dialog Box Options

 Option   Description

          Contains the following options:

                   • Begin at offset (x-axis units)—

                Starts the extraction when the signal crosses the value you specify in Offset.

       ◦ Offset— Begin
                   Value that Begin at offset (x-axis units) uses. The default is 0.

                   • Begin at sample number—

                Starts the extraction at the point you enter in Sample number.


                                                    © National Instruments 6035

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6035 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6036 ordinal=6036 -->
## Functions

Functions


        Option   Description

          ◦ Sample number—

                          Value that Begin at sample number uses. The default is 0.

                  Contains the following options:

                              • Length (x-axis units)—

                    Ends the extraction after the extracted signal is the length you enter in Length.

          ◦ Length—

                             Specifies the value that Length (x-axis units) uses. The default is 1.

                              • Number of samples—        Duration
         or Span                    Ends the extraction after the extracted signal contains the number of points you
                        specify in Samples.

          ◦ Samples—

                          Value that Number of samples uses. The default is 1.

                              • Remaining samples—

                    Ends the extraction at the end of the signal.


                   Displays the input signal.
        Input                              If you wire data to the Express VI and run it, Input Signal displays real data. If you close
         Signal                and reopen the Express VI, Input Signal displays sample data until you run the Express VI
                    again.


                   Displays a preview of the measurement. The Result Preview plot indicates the value of
                  the selected measurement with a dotted line.         Result
        Preview                              If you wire data to the Express VI and run the VI, Result Preview displays real data. If you
                   close and reopen the Express VI, Result Preview displays sample data until you run the


6036   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6036 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6037 ordinal=6037 -->
## Functions

Functions


 Option   Description

            VI again. If the cutoff frequency values are invalid, Result Preview does not display valid
           data.


Inputs/Outputs

   •      Signals —

    Contains the input signal or signals.

   •      Begin Sample —

     Specifies the value that Begin at sample number uses. The value you wire to this input overrides
    the value you set in the configuration dialog box.

   •      Length —

     Specifies the value that Length (x-axis units) uses. The value you wire to this input overrides the
    value you set in the configuration dialog box.

   •       error in (no error) —

    Describes error conditions that occur before this node runs.

   •     Samples —

     Specifies the value that Number of Samples uses. The value you wire to this input overrides the
    value you set in the configuration dialog box.

   •      Begin Offset —

     Specifies the value that Begin at Offset (x-axis units) uses. The value you wire to this input
    overrides the value you set in the configuration dialog box.

   •      Section —

    Returns the extracted portion of the input signal.

   •       error out —

    Contains error information. This output provides standard error out functionality.


                                                    © National Instruments 6037

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6037 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6038 ordinal=6038 -->
## Functions

Functions

     Components

       Displays a preview of the measurement. The Result Preview plot indicates the value of
       the selected measurement with a dotted line.

       Displays the input signal.

       Value that Number of samples uses. The default is 1.

      Ends the extraction after the extracted signal contains the number of points you
       specify in Samples.

       Specifies the value that Length (x-axis units) uses. The default is 1.

      Ends the extraction after the extracted signal is the length you enter in Length.

      Ends the extraction at the end of the signal.

       Value that Begin at offset (x-axis units) uses. The default is 0.

        Starts the extraction when the signal crosses the value you specify in Offset.

       Value that Begin at sample number uses. The default is 0.

        Starts the extraction at the point you enter in Sample number.

     DelayDelay ValuesValues

       Stores data from previous iterations of a loop and passes the data after the specified
      number of iterations occur.


6038   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6038 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6039 ordinal=6039 -->
## Functions

Functions

Dialog Box Options

 Option      Description

 History     Contains the number of iterations of the loop to delay the packet of data. The default
 size            is 1.


Inputs/Outputs

   •      Signals —

    Contains the input signal or signals.

   •      Enable —

    Enables or disables the Express VI. The default is ON or TRUE.

   •       error in (no error) —

    Describes error conditions that occur before this node runs.

   •      Delayed Signals —

    Returns the delayed signal(s).

   •       error out —

    Contains error information. This output provides standard error out functionality.


The value you wire to History Size determines the number of times the loop iterates
before the Express VI returns data. For example, if you enter 1 in History size, the
Express VI does not return the data wired to the Signals input after the first iteration of
the loop. The second time the loop iterates, the Express VI returns the value from the
first iteration of the loop. The third time the loop iterates, the Express VI returns the
value from the second iteration of the loop.

Components

Contains the number of iterations of the loop to delay the packet of data. The default is

                                                    © National Instruments 6039

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6039 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6040 ordinal=6040 -->
## Functions

Functions

        1.

     ConvertConvert fromfrom DynamicDynamic DataData

       Converts the dynamic data type to numeric, Boolean, waveform, and array data types
        for use with other VIs and functions.


      Dialog Box Options

        Option      Description

                    Contains the following options:

                                  •  Floating point numbers (double)—

                       Formats numeric values as double-precision, floating-point numbers, including
                         the values in arrays.

                                  • Boolean (TRUE and FALSE)—

        Conversion     Formats numeric values as Boolean values, including the values in arrays.

                                  • Resulting data type—

                           Specifies the data type that you want to convert to from the dynamic data type.

                                  • Channel—

                           Specifies the channel from which you want to retrieve the data.


                      Displays the input signal.
        Input                                  If you wire data to the Express VI and run it, Input Signal displays real data. If you
         Signal                      close and reopen the Express VI, Input Signal displays sample data until you run the VI
                      again.

         Result       Displays a preview of the measurement. The Result Preview plot indicates the value


6040   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6040 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6041 ordinal=6041 -->
## Functions

Functions


 Option      Description

              of the selected measurement with a dotted line.

                     If you wire data to the Express VI and run the VI, Result Preview displays real data. If
 Preview    you close and reopen the Express VI, Result Preview displays sample data until you
            run the VI again. If the cutoff frequency values are invalid, Result Preview does not
              display valid data.


Inputs/Outputs

   •      Channel — Specifies the channel from which you want to retrieve the data. The value you
    wire to this input overrides the value you set in the configuration dialog box.
   •     Dynamic Data Type —

    Contains the input signal formatted as dynamic data.

   •      Array —

    Returns the output signal converted into an array of numeric values. You also can configure the
    Convert from Dynamic Data Express VI to return the following outputs:

         • Scalar—Returns the output signal converted into a numeric value.
         • Waveform—Returns the output signal converted into a waveform.
         • Array of Waveform—Returns the output signal converted into a 1D array of waveform data.

Components

Displays a preview of the measurement. The Result Preview plot indicates the value of
the selected measurement with a dotted line.

Specifies the channel from which you want to retrieve the data.

Displays the input signal.

Specifies the data type that you want to convert to from the dynamic data type.

Formats numeric values as Boolean values, including the values in arrays.

Formats numeric values as double-precision, floating-point numbers, including the
values in arrays.

                                                    © National Instruments 6041

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6041 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6042 ordinal=6042 -->
## Functions

Functions

     ConvertConvert toto DynamicDynamic DataData

       Converts numeric, Boolean, waveform and array data types to the dynamic data type
        for use with Express VIs.


      Dialog Box Options

        Option      Description

                    Contains the following option:

                                  • Input data type—        Conversion
                           Specifies the data type that you want to convert to the dynamic data type.

                    Contains the following options:

                                  •  Floating point numbers (double)—

         Scalar           Specifies that numeric values are double-precision, floating-point numbers.
        Data Type
                                  • Boolean (TRUE and FALSE)—

                           Specifies that numeric values are Boolean values.

                    Contains the following options:

                                  • Zero—

                          Sets the t0 of the input signal to zero.         Start Time
                                  • Now—

                          Sets the t0 of the input signal to the current system time.

         Inputs      Displays the input signal.


6042   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6042 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6043 ordinal=6043 -->
## Functions

Functions


 Option      Description

                     If you wire data to the Express VI and run it, Inputs displays real data. If you close and
            reopen the Express VI, Inputs displays sample data until you run the VI again.

              Displays a preview of the measurement. The Results Preview plot indicates the value
              of the selected measurement with a dotted line.

 Results         If you wire data to the Express VI and run the VI, Results Preview displays real data. If
 Preview    you close and reopen the Express VI, Results Preview displays sample data until you
            run the VI again. If the cutoff frequency values are invalid, Results Preview does not
              display valid data.


Inputs/Outputs

   •      Array —

    Contains the input waveform or array of numbers or Boolean values. You also can configure the
    Convert to Dynamic Data Express VI to accept the following outputs:

         • 2D Array—Contains the input signal formatted as a 2D array of numbers.
         • Array of Waveforms—Contains the input signal formatted as a 2D array of waveforms.
         • Boolean—Contains the input signal formatted as a single Boolean value.
         • Double—Contains the input signal formatted as a double-precision, floating-point number.
         • Waveform—Contains the input signal formatted as a waveform.
   •     Dynamic Data Type —

    Returns a dynamic data type with the values you entered in the Array input.


Components

Sets the t0 of the input signal to the current system time.

Sets the t0 of the input signal to zero.

Contains the input signal formatted as a single Boolean value.

Returns a dynamic data type with the values you entered in the Array input.


                                                    © National Instruments 6043

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6043 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6044 ordinal=6044 -->
## Functions

Functions

       Specifies the data type that you want to convert to the dynamic data type.

       Specifies that numeric values are Boolean values.

       Specifies that numeric values are double-precision, floating-point numbers.

       Contains the input signal formatted as a waveform.

       contains the input signal formatted as a 2D array of waveforms.

     GroupGroup DigitalDigital SignalsSignals

      Groups digital data into a digital data array and groups digital waveforms into a digital
      waveform array.

      LabVIEW treats ungrouped signals as individual groups.


      Dialog Box Options

        Option     Description

                     Specifies the number of signals you want to wire to the Express VI. Configure this option
                             first.       Number
         of signals                    This number must match the number of signals you wire to Digital Data In. Otherwise,
                 LabVIEW returns an error.


       Use
                    Allows you to retain the original names of the waveforms you wire to Digital Data In.
        incoming
                    This checkbox contains a checkmark by default. Remove the checkmark from this
       waveform
                  checkbox to use the line and bus names you specify using the Rename button.
       names


6044   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6044 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6045 ordinal=6045 -->
## Functions

Functions


 Option     Description

 Order of            Displays the sequential order of the digital signals.
 signals


            Contains the lines and buses you configure in the configuration dialog box.

 Plot      Use this tree control to drag and drop lines into the order you want to view them in the
 Legend    output array. To put lines into groups, right-click a line and select Insert Bus and then
           drag other lines onto that bus. You cannot drag a line onto another line, a bus onto
           another bus, or a bus onto a line.


 Graph      Displays a preview of the lines and buses based on the organization you specify in the
 Preview    configuration dialog box.


            Allows you to rename the line or bus you select in the Plot Legend tree control. You also
           can right-click a line or bus and select Rename from the shortcut menu or double-click
           a line or bus to type a new name.
 Rename
           To rename lines or buses, you must remove the checkmark from the Use incoming
          waveform names checkbox. Otherwise, the incoming line names take precedence over
            the new names you specify.


             Inserts a new bus above the line or bus you select in the Plot Legend tree control. You
 Insert Bus            also can right-click a line or bus and select Insert Bus from the shortcut menu.


            Deletes all the buses from the Plot Legend tree control.
 Delete All           To delete a single bus, right-click the bus and select Delete Bus from the shortcut
 Buses          menu. You can delete only buses, not lines. LabVIEW considers lines listed under
            deleted buses as ungrouped signals.


Inputs/Outputs

   •       error in (no error) —
    Describes error conditions that occur before this node runs.

                                                    © National Instruments 6045

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6045 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6046 ordinal=6046 -->
## Functions

Functions

               •       Digital Data In —
             Specifies the input signals you want to organize into groups.
               •       error out —
            Contains error information. This output provides standard error out functionality.
               •       Digital Data Out —
            Returns a digital data array or a digital waveform array, depending on the data type of Digital
           Data In.

      SetSet DynamicDynamic DataData AttributesAttributes

       Sets the attributes of the dynamic data you wire to Signals In.


      Dialog Box Options

        Option  Description

                 Contains the following options:

           All            •  Start timestamp—
         Signals
                       Specifies whether to set the start timestamp of the signals.


                   Specifies the index of the signal whose attributes you want to set. The default is 0.

                 Signal Index contains the following options:
         Signal
                            • Signal name—
        Index
                       Specifies whether to set the name of the signal.

          ◦ Signal name value—


6046   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6046 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6047 ordinal=6047 -->
## Functions

Functions


Option  Description

                  Specifies the name of the signal.

                 This option is available only if you place a checkmark in the Signal name
                checkbox.

               • Time mode—

              Specifies whether to apply absolute time or relative time to the signal.

      ◦ Time mode value—
                  Specifies the time mode to apply to the signal. You can choose from the following
                  options:
        ▪ Absolute (default)—Displays the timestamp in terms of time elapsed since
                     12:00 a.m., Friday, January 1, 1904, Universal Time [01-01-1904 00:00:00].
        ▪ Relative—Displays the timestamp in terms of seconds starting from zero. For
                    example, 100 in relative time equals 1 minute and 40 seconds.

                 This option is available only if you place a checkmark in the Time mode
                checkbox.

               • Timestamp—

              Specifies whether to set the timestamp of the signal.

      ◦ Timestamp value—

                  Specifies the timestamp to apply to the signal.

                 This option is available only if you place a checkmark in the Timestamp
                checkbox.

               • X dimension—

              Specifies whether to set the X dimension of the signal.

      ◦ X dimension value—
                  Specifies the X dimension of the signal. You can choose from the following
                  options:
        ▪ No Unit [-] (default)
        ▪ Time [sec]
        ▪ Frequency [Hz]


                                                    © National Instruments 6047

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6047 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6048 ordinal=6048 -->
## Functions

Functions


        Option  Description

                          This option is available only if you place a checkmark in the X dimension
                        checkbox.

                            • Unit—

                       Specifies whether to set the unit of measurement of the signal.

          ◦ Unit value—

                            Specifies the unit of measurement of the signal. For example, if the signal whose
                            attributes you want to set measures voltage, you can specify V for volts or kV for
                              kilo volts.

                          This option is available only if you place a checkmark in the Unit checkbox.


      Inputs/Outputs

               •       error in —
            Describes error conditions that occur before this node runs.
               •      Signals In —
             Specifies the dynamic data that contains the input signal or signals.
               •      Signal Index —
             Specifies the index of the signal whose attributes you want to configure.

          The value you wire to this input overrides the value you set in the configuration dialog box.

               •       error out —
            Contains error information. This output provides standard error out functionality.
               •      Signals Out —
            Returns the dynamic data that contains the signal you set with this Express VI and any
           unchanged signals from Signals In.

     GetGet DynamicDynamic DataData AttributesAttributes

       Retrieves the attributes of the dynamic data you wire to Signals In.


6048   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6048 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6049 ordinal=6049 -->
## Functions

Functions


Dialog Box Options

 Option       Description

               Specifies the index of the signal whose attributes you want to retrieve. The default is
                 0.

              Signal Index contains the following options:

                       •  Start timestamp—

                   Specifies whether to return the start timestamp of the signal.

                       • Signal name—

                   Specifies whether to return the name of the signal.

 Signal              • Time mode—
 Index
                   Specifies whether to return the time mode of the signal.

                       • Timestamp—

                   Specifies whether to return the timestamp of the signal.

                       • X dimension—

                   Specifies whether to return the X dimension of the signal.

                       • Unit—

                   Specifies whether to return the unit of measurement of the signal.


Inputs/Outputs

   •       error in —

                                                    © National Instruments 6049

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6049 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6050 ordinal=6050 -->
## Functions

Functions

            Describes error conditions that occur before this node runs.
               •      Signals In —
             Specifies the dynamic data that contains the input signal or signals.
               •      Signal Index —
             Specifies the index of the signal whose attributes you want to retrieve.

          The value you wire to this input overrides the value you set in the configuration dialog box.

               •      Signals Out —
            Returns Signals In unchanged.
               •      Signal Name — Returns the name of the signal.

             This output is available only if you place a checkmark in the Signal name checkbox in the
             configuration dialog box.

               •     Time Mode — Returns the time mode of the signal.

             This output is available only if you place a checkmark in the Time mode checkbox in the
             configuration dialog box.

               •     Timestamp — Returns the timestamp of the signal.

             This output is available only if you place a checkmark in the Timestamp checkbox in the
             configuration dialog box.

               •       Start Timestamp — Returns the start timestamp of the signal.

             This output is available only if you place a checkmark in the Start timestamp checkbox in the
             configuration dialog box.

               •     X Dimension — Returns the X dimension of the signal.

             This output is available only if you place a checkmark in the X dimension checkbox in the
             configuration dialog box.

               •      Unit — Returns the unit of measurement of the signal.

             This output is available only if you place a checkmark in the Unit checkbox in the configuration
             dialog box.

               •       error out —
            Contains error information. This output provides standard error out functionality.


6050   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6050 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6051 ordinal=6051 -->
## Functions

Functions

ExecutionExecution ControlControl

Use the Execution Control Express VIs and structures to add control and timing to VIs.


 Palette           Description
 Object

 While     Repeats the subdiagram inside it until the conditional terminal, an input terminal,
 Loop      receives a particular Boolean value. When you place this While Loop on the block
 with      diagram, a stop button also appears on the block diagram and is wired to the
 Button    conditional terminal.

            Consists of one or more subdiagrams, or frames, that execute sequentially. Use the Flat
          Sequence structure to ensure that a subdiagram executes before or after another
 Flat       subdiagram. Data flow for the Flat Sequence structure differs from data flow for other
 Sequence  structures. Frames in a Flat Sequence structure execute from left to right and when all
 Structure  data values wired to a frame are available. The data leaves each frame as the frame
             finishes executing. This means the input of one frame can depend on the output of
           another frame.

           Contains one or more subdiagrams, or cases, exactly one of which executes when the
 Case            structure executes. The value wired to the case selector determines which case to Structure            execute.

 Time             Inserts a time delay into the calling VI. Delay

 Elapsed
            Indicates the amount of time that has elapsed since the specified start time.
 Time


Examples

Refer to the following example files included with LabVIEW.

  • labview\examples\Structures


                                                    © National Instruments 6051

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6051 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6052 ordinal=6052 -->
## Functions

Functions

     WhileWhile LoopLoop withwith ButtonButton

      Repeats the subdiagram inside it until the conditional terminal, an input terminal,
       receives a particular Boolean value. When you place this While Loop on the block
       diagram, a stop button also appears on the block diagram and is wired to the
       conditional terminal.

           If you select a While Loop on the Structures palette and place it on the block diagram,
      a stop button does not appear.


      FlatFlat SequenceSequence StructureStructure

       Consists of one or more subdiagrams, or frames, that execute sequentially. Use the
        Flat Sequence structure to ensure that a subdiagram executes before or after another
      subdiagram. Data flow for the Flat Sequence structure differs from data flow for other
        structures. Frames in a Flat Sequence structure execute from left to right and when all
       data values wired to a frame are available. The data leaves each frame as the frame
        finishes executing. This means the input of one frame can depend on the output of
      another frame.

       Unlike in the Stacked Sequence structure, you do not need to use sequence locals to
       pass data from frame to frame in the Flat Sequence structure. Since the Flat Sequence
       structure displays each frame on the block diagram, you can wire from frame to frame
       without using sequence locals and without hiding code.

     When you add or delete frames in a Flat Sequence structure, the structure resizes
       automatically.

      You cannot drag tunnels across the frames of a Flat Sequence structure.

      To avoid overusing Flat Sequence structures, attempt to control the data flow of your
        VI by establishing data dependency or using flow-through parameters.


6052   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6052 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6053 ordinal=6053 -->
## Functions

Functions

(Real-Time, Windows) To convert a Flat Sequence structure to a Timed Sequence
structure, right-click the Flat Sequence structure and select Replace with Timed
Sequence from the shortcut menu.


Stacked Sequence Structure

A Stacked Sequence structure consists of one or more subdiagrams, or frames, that
execute sequentially. Right-click the structure border to add and delete frames or to
create sequence locals to pass data between frames. Use the Stacked Sequence
structure to ensure a subdiagram executes before or after another subdiagram.

To create a Stacked Sequence structure, place a Flat Sequence structure on the block
diagram, right-click the Flat Sequence structure, and select Replace with Stacked
Sequence.


To scroll through the available subdiagrams, click the decrement and increment
arrows in the selector label. You can add, duplicate, rearrange, or delete the
subdiagrams. You can use a sequence local terminal to pass data from one frame to
any subsequent frame.

Use the Stacked Sequence structure if you want to conserve space on the block
diagram. Use the Flat Sequence structure to avoid using sequence locals and to better
document the block diagram. To convert the Stacked Sequence structure to a Flat
Sequence structure, right-click the Stacked Sequence structure and select
Replace»Replace with Flat Sequence from the shortcut menu.

To convert the Stacked Sequence structure to a Case structure, right-click the Stacked
Sequence structure and select Replace»Replace with Case Structure from the

                                                    © National Instruments 6053

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6053 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6054 ordinal=6054 -->
## Functions

Functions

       shortcut menu.

      The Stacked Sequence structure does not start to execute until all data wired to the
       structure arrive. The data wired from each frame leave only when all the frames
      complete execution.

      To avoid overusing Stacked Sequence structures, attempt to control the data flow of
       the VI by establishing data dependency or using flow-through parameters.

     CaseCase StructureStructure

       Contains one or more subdiagrams, or cases, exactly one of which executes when the
       structure executes. The value wired to the case selector determines which case to
       execute.


     Components of a Case Structure


            •   Selector label—Displays the value(s) for which the associated case executes. You


6054   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6054 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6055 ordinal=6055 -->
## Functions

Functions

   can specify a single value or a range of values. You also can use the selector label to
    specify a default case.
  •   Subdiagram(case)—Contains the code that executes when the value wired to
   the case selector matches the value that appears in the selector label. To modify
   the number or order of subdiagrams, right-click the border of the Case structure
   and select the appropriate option.
  •   Case selector—Selects which case to execute based on the value of the input
    data. The input data can be a Boolean, string, integer, enumerated type or error
    cluster. The data type you wire to the case selector determines the allowed cases
   you can enter in the selector label.
Configuring a Case Structure

  • Creating a basic Case structure
  • Quickly wiring an output tunnel for all cases

Rearranging a Case Structure

  • Adding subdiagrams between other subdiagrams
  • Moving between subdiagrams
  • Shifting subdiagrams to a different position in the order of subdiagrams
  • Swapping the subdiagrams of two cases
  • Removing a Case structure without deleting contained code

Troubleshooting a Case Structure

  • Preventing indicators from resetting to default values
  • Missing string values of enumerated controls

Examples

Refer to the following example files included with LabVIEW.

  • labview\examples\Structures\Case Structure\Case Structure
   - Selector Data Types.vi


                                                    © National Instruments 6055

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6055 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6056 ordinal=6056 -->
## Functions

Functions

     TimeTime DelayDelay

        Inserts a time delay into the calling VI.


      Dialog Box Options

        Option              Description

       Time delay           Specifies how many seconds to delay running the calling VI. The default is
         (seconds)             1.000.


      Inputs/Outputs

               •      Delay Time (s) —

             Specifies how many seconds to wait. The value you wire to this input overrides the value you set
              in the configuration dialog box.

               •       error in (no error) —

            Describes error conditions that occur before this node runs.

               •       error out —

            Contains error information. This output provides standard error out functionality.

     ElapsedElapsed TimeTime

       Indicates the amount of time that has elapsed since the specified start time.


6056   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6056 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6057 ordinal=6057 -->
## Functions

Functions


Dialog Box Options

 Option                  Description

                           Specifies how much time must elapse before the Time has Elapsed
 Elapsed time (seconds)                       Boolean is set to TRUE. The default is 1.000.


 Automatically reset                         Resets the elapsed time marker. after time target

Inputs/Outputs

   •      Reset —

    Controls the initialization of the internal state of the VI. The default is FALSE.

   •     Time Target (s) —

     Specifies how much time must elapse before the Time has Elapsed Boolean is set to TRUE. The
     default is 1.

   •      Auto Reset —

    Resets the start time to the value in Present (s) when the Express VI reaches the Time Target (s).

   •       error in (no error) —

    Describes error conditions that occur before this node runs.

   •      Set Start Time (s) —

    Uses the current time or a time offset from 12:00 a.m., Friday, January 1, 1904 [01-01-1904
     00:00:00] as the start time instead of the time this VI first ran.


                                                    © National Instruments 6057

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6057 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6058 ordinal=6058 -->
## Functions

Functions


                    If the value is 0, the Express VI uses the current time as the start time. The Express VI uses any
            other value as the number of seconds offset from 12:00 a.m., Friday, January 1, 1904 [01-01-1904
              00:00:00]. For example if the value is 1, the Express VI measures the elapsed time since 12:00:01
             a.m., Friday, January 1, 1904 [01-01-1904 00:00:01]. You can wire this input to the Present (s)
           output of another Elapsed Time Express VI to get this value.

               •      Present (s) —

             Displays the present time in seconds since 12:00 a.m., Friday, January 1, 1904, Universal Time
            [01-01-1904 00:00:00].

               •       Start Time Text —

                    If Automatically reset after time target is FALSE, displays (in text format) the date and time the
              VI first ran or the time you wire to the Set Start Time (s) input. Otherwise displays the date and
           time of the last reset.

               •      Present Text —

             Displays the present date and time in text format.

               •     Time has Elapsed —

             Indicates if the Elapsed Time (s) is greater than the start time plus Time Target (s).

               •      Get Start Time (s) —

                    If Automatically reset after time target is FALSE, displays the date and time the VI first ran or the
           time you wire to the Set Start Time (s) input. Otherwise displays the date and time of the last
              reset.

               •       error out —

            Contains error information. This output provides standard error out functionality.

               •      Elapsed Time (s) —

             Displays the amount of time in seconds that has elapsed since the start time and the Present (s)
             time.

               •      Elapsed Time Text —

             Displays the amount of time in seconds that has elapsed since the start time.


6058   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6058 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6059 ordinal=6059 -->
## Functions

Functions

ArithmeticArithmetic && ComparisonComparison

Use the Arithmetic & Comparison Express VIs and functions to perform arithmetic
functions and to compare Boolean values, strings, and numeric values.


 Palette              Description Object

            Uses a calculator interface to create mathematical formulas. You can use this Express
 Formula                VI to perform most math functions that a basic scientific calculator can compute.


 Scaling and            Changes the amplitude of a signal by scaling or mapping the signal. Mapping

 Time
 Domain     Performs one of several math functions on time domain signals.
 Math

            Use the Express Numeric functions to create and perform arithmetic and complex
 Express     mathematical operations on numbers and to convert numbers from one data type to
 Numeric     another. Use the VIs and functions on the Elementary & Special Functions palette to
             perform trigonometric and logarithmic functions.


 Express     Use the Math functions to create and to perform logarithmic and trigonometric
 Math        equations and to compute hyperbolic functions and their inverses.


 Express
            Use the Express Boolean functions to perform logical operations on Boolean values.
 Boolean


 Express     Use the Express Comparison VI and functions to compare Boolean values, strings,
 Comparison numeric values, arrays, and clusters.


                                                    © National Instruments 6059

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6059 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6060 ordinal=6060 -->
## Functions

Functions

     FormulaFormula

      Uses a calculator interface to create mathematical formulas. You can use this Express
        VI to perform most math functions that a basic scientific calculator can compute.


      Dialog Box Options

        Option     Description

                     Displays the formula as you enter it. You can enter variables and operations into this
        Formula                       text box by using the Input buttons or by directly entering a formula.


         Errors      Indicates if the formula is valid.


                     Enters a variable (X1-X8) into the formula. Enter a new variable name in the Label text       X1                  box associated with the variable to rename the variable.


                     Displays the name of the variable. Enter a new variable name in this text box to rename
       X1 (STR)
                    the default variable (X1-X8).


      Home     Moves the cursor to the beginning of the text in the formula text box.


        Backspace  Deletes the last character entered in the formula text box.


         Clear      Completely clears the text in the formula text box.


6060   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6060 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6061 ordinal=6061 -->
## Functions

Functions


Option     Description

End       Moves the cursor to the end of the text in the formula text box.


e           Enters the value of e into the formula.


            Enters ** into the formula. This operator computes the value of x raised to the y**
           power.


log         Enters log( into the formula. This operator computes the logarithm to the base 10.


ln          Enters ln( into the formula. This operator computes the natural base e logarithm.


            Enters mod( into the formula. This operator computes the remainder of x/y, when themod
            quotient is rounded toward –Infinity.


            Enters min( into the formula. This operator compares two integer values and returnsmin
           the smaller value.


Pi          Enters the value of Pi into the formula.


sqrt        Enters sqrt( into the formula. This operator computes the square root.


log2        Enters log2( into the formula. This operator computes the base-2 logarithm.


exp        Enters exp( into the formula. This operator computes the value of e raised to a power.


                                                    © National Instruments 6061

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6061 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6062 ordinal=6062 -->
## Functions

Functions


        Option     Description

                     Enters rem( into the formula. This operator computes the remainder of x/y, when the       rem
                    quotient is rounded toward –Infinity.


                     Enters max( into the formula. This operator compares two integer values and returns      max
                    the larger value.


           /           Right parenthesis.


                     Enters sin( into the formula. This operator computes the sine of x, where x is in         sin
                      radians.


        abs        Enters abs( into the formula. This operation computes the absolute value of x.


         *            Left parenthesis.


                     Enters cos( into the formula. This operator computes the cosine of x, where x is in        cos
                      radians.


          int         Enters int( into the formula. This operation rounds x to the nearest integer.


            -            Addition.


                     Enters tan( into the formula. This operation computes the tangent of x, where x is in        tan
                      radians.


         sign        Enters sign( into the formula. This operation returns 1 if x is greater than 0, returns 0


6062   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6062 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6063 ordinal=6063 -->
## Functions

Functions


 Option     Description

                     if x is equal to 0, and returns –1 if x is less than 0.


             Enters the decimal separator into the formula. Regardless of the decimal pointer
              settings, this dialog box only uses the period (.) as a decimal separator. Decimal
 Point             This Express VI uses the Formula Node, and the Formula Node does not recognize
              localized decimal separators and reserves the comma for another use.


 E           Enters the value of e into the formula.


 +            Division.


 (            Multiplication.


 )           Subtraction.


 More       Contains more advanced functions, such as acos, expm1, floor, gamma, and sinc,
 Functions  that you can use in the Formula Express VI.


Inputs/Outputs

   •       error in (no error) —
    Describes error conditions that occur before this node runs.
   •     X1 —
     (X1-X8) are the input values for the formula you specified in the configuration dialog box.
   •       error out —
    Contains error information. This output provides standard error out functionality.
   •      Result —
    Returns the resulting data based on the configuration of the Express VI.


                                                    © National Instruments 6063

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6063 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6064 ordinal=6064 -->
## Functions

Functions

      ScalingScaling andand MappingMapping

      Changes the amplitude of a signal by scaling or mapping the signal.


      Dialog Box Options

        Option        Description

                       Contains the following options:

                                      • Normalize—

                          Determines the scale and offset necessary to transform the signal so that its
                     maximum is Highest peak and its minimum is Lowest peak.

             ◦ Lowest peak—

                                   Specifies the minimum value used to normalize the signal. The default is
                                  0.

             ◦ Highest peak—

                                   Specifies the maximum value used to normalize the signal. The default is         Scaling or
                                  1.       Mapping
        Type
                                      • Linear (Y=mX+b)—

                            Sets the scale mapping mode to be linear, which scales the signal based on a
                               straight line.

             ◦ Slope (m)—

                              Slope used for Linear (Y=mX+b) scaling. The default is 1.

             ◦ Y intercept (b)—

                                  Intercept used for Linear (Y=mX+b) scaling. The default is 0.

                                      • Logarithmic—


6064   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6064 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6065 ordinal=6065 -->
## Functions

Functions


 Option        Description

                    Sets the scale mapping mode to be logarithmic, which scales the signal based
                on a decibel reference.

                 LabVIEW scales the signal using the following equation: y= 20log10(x/db
                    reference)

         ◦ db reference—

                       Reference for the Logarithmic scaling. The default is 1.

                          • Interpolated—

                    Scales the signals based on a table of values that are interpolated linearly onto
                  a scaling factor.

         ◦ Define Table—

                         Displays the Define Signal dialog box, which you use to define a table of
                        values for Interpolated scaling.


Inputs/Outputs

   •      Signals —

    Contains the input signal or signals.

   •       error in (no error) —

    Describes error conditions that occur before this node runs.

   •       error out —

    Contains error information. This output provides standard error out functionality.

   •      Scaled Signals —

    Returns the scaled signals.


                                                    © National Instruments 6065

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6065 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6066 ordinal=6066 -->
## Functions

Functions

     Examples

       Refer to the following example files included with LabVIEW.

            • labview\examples\Express VIs\Express VI - Scaling and
        Mapping.vi

     TimeTime DomainDomain MathMath

      Performs one of several math functions on time domain signals.


      Dialog Box Options

        Option        Description

                       Contains the following options:

                                     •  Derivative (dX/dt)—

                           Returns the numeric derivative of the signal.

                        LabVIEW computes the output sample of dX/dtat index ias yi=(xi– xi–1)/dt.

                                     •  Difference (dX)—

        Mathematical                           Returns the numeric difference of the signal.
        Operation
                        LabVIEW computes the output sample of dXat index ias yi=xi–xi–1.

                                     •  Integral (Sum[Xdt])—

                           Returns the numeric integral of the signal.

                        LabVIEW computes the output sample of Sum[Xdt]at index ias yi=yi–1 +
                            xidt.


6066   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6066 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6067 ordinal=6067 -->
## Functions

Functions


Option        Description

                         • Summation (Sum[X])—

                  Returns the summation of the signal.

                LabVIEW computes the output sample of Sum[X]at index ias yi=yi–1 + xi.

              Contains the following options:

                         • Continuous calculation—

                 Uses data from previous segments of data in performing the calculation.Calculation
Mode                         • Per segment calculation—

                Does not use data from previous segments of data in performing the
                     calculation.

              Contains the following options:

                         • Use mathematical operation name—

                   Displays the name of the mathematical operation as the name of the Express VI
               on the block diagram.
Result Name
                         • Express VI name—

                   Displays the name of the Express VI on the block diagram. Remove the
                checkmark from the Use mathematical operation name checkbox to edit the
              name of the Express VI.


               Displays the input signal.

Input Signal     If you wire data to the Express VI and run it, Input Signal displays real data. If you
               close and reopen the Express VI, Input Signal displays sample data until you run
              the Express VI again.


Result
               Displays a preview of the measurement. The Result Preview plot indicates the
Preview


                                                    © National Instruments 6067

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6067 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6068 ordinal=6068 -->
## Functions

Functions


        Option        Description

                       value of the selected measurement with a dotted line.

                                      If you wire data to the Express VI and run it, Result Preview displays real data. If you
                        close and reopen the Express VI, Result Preview displays sample data until you run
                       the VI again. If the cutoff frequency values are invalid, Result Preview does not
                        display valid data.


      Inputs/Outputs

               •      Signals —

            Contains the input signal or signals.

               •       error in (no error) —

            Describes error conditions that occur before this node runs.

               •       error out —

            Contains error information. This output provides standard error out functionality.

               •      Result —

            Returns the resulting data based on the configuration of the Express VI.

      ExpressExpress NumericNumeric

      Use the Express Numeric functions to create and perform arithmetic and complex
      mathematical operations on numbers and to convert numbers from one data type to
       another. Use the VIs and functions on the Elementary & Special Functions palette to
      perform trigonometric and logarithmic functions.

      You also can access the following constants from this palette:

            • positive infinity
            • negative infinity
            • machine epsilon

6068   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6068 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6069 ordinal=6069 -->
## Functions

Functions


Palette            DescriptionObject

Add
          Computes the sum of the inputs.Function

Subtract          Computes the difference of the inputs.Function

Multiply
            Returns the product of the inputs.Function

Divide          Computes the quotient of the inputs.Function

Increment          Adds 1 to the input value.Function

Decrement            Subtracts 1 from the input value.Function

           Performs arithmetic on one or more numeric, array, cluster, or Boolean inputs. To
             select the operation (Add, Multiply, AND, OR, or XOR), right-click the function and
Compound             select Change Mode from the shortcut menu. When you select this function from theArithmetic
           Numeric palette, the default mode is Add. When you select this function from the
           Boolean palette, the default mode is OR.

Absolute
Value       Returns the absolute value of the input.
Function

Round To
          Rounds the input to the nearest integer. If the value of the input is midway between
Nearest
          two integers, the function returns the nearest even integer.
Function

Round
Toward
            Truncates the input to the next lowest integer.
-Infinity
Function

Round
Toward
          Rounds the input to the next highest integer.
+Infinity
Function


                                                    © National Instruments 6069

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6069 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6070 ordinal=6070 -->
## Functions

Functions


         Palette                     Description
        Object

         Scale By
       Power Of 2  Multiplies x by 2 raised to the power of n.
         Function

        Square
        Root      Computes the square root of the input value.
         Function

        Square                 Computes the square of the input value.
         Function

        Negate                   Negates the input value.         Function

         Reciprocal                     Divides 1 by the input value.         Function

         Sign                    Returns the sign of number.         Function

        Numeric   Use the numeric constant to pass a numeric value to the block diagram. Set this value
        Constant   by clicking inside the constant with the Operating tool and typing a value.

       Random
       Number    Produces a double-precision, floating-point number between 0 and 1. The number
          (0-1)       generated is greater than or equal to 0, but less than 1. The distribution is uniform.
         Function

          Positive                    Returns the value Inf (infinity).           Infinity

         Negative                    Returns the value -Inf (negative infinity).           Infinity

                    Represents the round-off error for a floating-point number with a given precision. Use
        Machine
                    the machine epsilon constant to compare whether two floating-point numbers are
         Epsilon
                      equivalent.

         Express
       Math &
                  Use the Express Math & Scientific Constants to create LabVIEW applications.
          Scientific
        Constants


6070   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6070 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6071 ordinal=6071 -->
## Functions

Functions

AddAdd FunctionFunction

Computes the sum of the inputs.


Inputs/Outputs

   •      x —

    x can be a scalar number, array or cluster of numbers, array of clusters of numbers, and so on.

   •      y —

    y can be a scalar number, a fixed-point number, an array or cluster of numbers, an array of
     clusters of numbers, a time stamp, and so on.

   •      x+y —

    x+y is the sum of x and y.

          Note You can manually configure this function to output data of a type you want. To
              specify the output data type, right-click the function and select Properties to display
             the Object Properties dialog box. On the Output Configuration page, click the
            Representation icon and select the data type you want. A blue coercion dot appears
           on the output terminal of the function to indicate that you have configured the
            output data type.


Matrix Details

When you wire matrix data as an input to this function, a VI that includes subVIs that
work with the matrix data type replaces the function. The resulting VI has the same
icon but contains a matrix-specific algorithm. The node remains a VI if you disconnect
the matrix from the inputs. Wire other data types as inputs to restore the original
function. If you wire a data type to a function and that data type causes a basic math
operation to fail, the function returns a NaN.

You also can add two or more values using the Compound Arithmetic function.

                                                    © National Instruments 6071

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6071 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6072 ordinal=6072 -->
## Functions

Functions

      Fixed-Point Details

           If you wire fixed-point values to Numeric functions such as Add, Subtract, Multiply, and
       Square, the functions usually return values that do not lose any bits of word length.
      However, if the operation creates a value that exceeds the maximum word length that
      LabVIEW accepts, overflow or rounding conditions can occur. LabVIEW accepts a
     maximum word length of 64 bits. Use the Numeric Node Properties dialog box to
       configure how LabVIEW handles overflow or rounding of fixed-point data.

     Examples

       Refer to the following example files included with LabVIEW.

            • labview\examples\Numerics\Numeric Functions.vi

      SubtractSubtract FunctionFunction

      Computes the difference of the inputs.

           If you wire two waveform values or two dynamic data type values to this function,
       error in and error out terminals appear on the function. Subtracting two time stamp
       values yields a numeric value (difference in time), and subtracting a numeric value
      from a time stamp value yields a time stamp. You cannot subtract a time stamp value
      from a numeric value. The dimensions of two matrices that you want to subtract must
      be the same. Otherwise, this function returns an empty matrix. The connector pane
       displays the default data types for this polymorphic function.


      Inputs/Outputs

               •      x —

           x specifies the input value.

             This input accepts the following data types:
                     • Number
                     • Timestamp

6072   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6072 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6073 ordinal=6073 -->
## Functions

Functions

         • Analog Waveform
    This input also accepts an array or an array of clusters of the listed data types.
   •      y —

    y can be a scalar number, a fixed-point number, an array or cluster of numbers, an array of
     clusters of numbers, a time stamp, and so on.

   •       x-y —

    x-y is the difference between x and y.

          Note You can manually configure this function to output data of a type you want. To
              specify the output data type, right-click the function and select Properties to display
             the Object Properties dialog box. On the Output Configuration page, click the
            Representation icon and select the data type you want. A blue coercion dot appears
           on the output terminal of the function to indicate that you have configured the
            output data type.


When you wire matrix data as an input to this function, a VI that includes subVIs that
work with the matrix data type replaces the function. The resulting VI has the same
icon but contains a matrix-specific algorithm. The node remains a VI if you disconnect
the matrix from the input(s). Wire other data types as inputs to restore the original
function. If you wire a data type to a function and that data type causes a basic math
operation to fail, the function returns an empty matrix or NaN.

Fixed-Point Details

If you wire fixed-point values to Numeric functions such as Add, Subtract, Multiply, and
Square, the functions usually return values that do not lose any bits of word length.
However, if the operation creates a value that exceeds the maximum word length that
LabVIEW accepts, overflow or rounding conditions can occur. LabVIEW accepts a
maximum word length of 64 bits. Use the Numeric Node Properties dialog box to
configure how LabVIEW handles overflow or rounding of fixed-point data.

Examples

Refer to the following example files included with LabVIEW.

  • labview\examples\Numerics\Numeric Functions.vi

                                                    © National Instruments 6073

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6073 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6074 ordinal=6074 -->
## Functions

Functions

       MultiplyMultiply FunctionFunction

       Returns the product of the inputs.

           If you wire two waveform values or two dynamic data type values to this function,
       error in and error out terminals appear on the function. The connector pane displays
       the default data types for this polymorphic function.


      Inputs/Outputs

               •      x —

           x can be a scalar number, array or cluster of numbers, array of clusters of numbers, and so on.

               •      y —

           y can be a scalar number, array or cluster of numbers, array of clusters of numbers, and so on.

               •      x*y —

            x*y is the product of x multiplied by y.


      You cannot use this function to multiply a matrix and a vector. Use the A x B VI instead.

     When multiplying two matrices, if the number of rows in the second matrix does not
      match the number of columns in the first matrix, this function returns an empty
       matrix. Refer to the A x B VI for more information about matrix multiplication.

     When you wire matrix data as an input to this function, a VI that includes subVIs that
      work with the matrix data type replaces the function. The resulting VI has the same
       icon but contains a matrix-specific algorithm. The node remains a VI if you disconnect
       the matrix from the input(s). Wire other data types as inputs to restore the original
       function. If you wire a data type to a function and that data type causes a basic math
       operation to fail, the function returns an empty matrix or NaN.


6074   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6074 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6075 ordinal=6075 -->
## Functions

Functions

Fixed-Point Details

If you wire fixed-point values to Numeric functions such as Add, Subtract, Multiply, and
Square, the functions usually return values that do not lose any bits of word length.
However, if the operation creates a value that exceeds the maximum word length that
LabVIEW accepts, overflow or rounding conditions can occur. LabVIEW accepts a
maximum word length of 64 bits. Use the Numeric Node Properties dialog box to
configure how LabVIEW handles overflow or rounding of fixed-point data.

Examples

Refer to the following example files included with LabVIEW.

  • labview\examples\Numerics\Numeric Functions.vi

DivideDivide FunctionFunction

Computes the quotient of the inputs.


Inputs/Outputs

   •      x —

    x can be a scalar number, array or cluster of numbers, array of clusters of numbers, and so on.

   •      y —

    y can be a scalar number, array or cluster of numbers, array of clusters of numbers, and so on.

   •       x/y —

    x/y is a double-precision, floating-point number if both x and y are integers. In general, the
    output type is the widest representation of the inputs if the inputs are not integers or if their
    representations differ.

          Note You can manually configure this function to output data of a type you want. To


                                                    © National Instruments 6075

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6075 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6076 ordinal=6076 -->
## Functions

Functions


                      specify the output data type, right-click the function and select Properties to display
                     the Object Properties dialog box. On the Output Configuration page, click the
                    Representation icon and select the data type you want. A blue coercion dot appears
                 on the output terminal of the function to indicate that you have configured the
                    output data type.


      Fixed-Point Details

           If you wire fixed-point values to this function, by default LabVIEW configures the
       integer word length of the quotient to avoid overflow for nonzero values of y. However,
      because the precision of the quotient can be infinite, rounding conditions always
       occur. Use the Numeric Node Properties dialog box to configure how LabVIEW handles
      rounding of fixed-point data. This function always uses the Saturate overflow mode to
      handle overflow.

      IncrementIncrement FunctionFunction

      Adds 1 to the input value.

      The connector pane displays the default data types for this polymorphic function.


      Inputs/Outputs

               •      x —

           x specifies the input value.

             This input accepts the following data types:

                     • Number
                     • Timestamp
                     • Analog Waveform

             This input also accepts an array or an array of clusters of the listed data types.

               •      x+1 —

6076   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6076 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6077 ordinal=6077 -->
## Functions

Functions


    x+1 is the result of x+1. If the input is a time stamp value, this function increments the time by
    one second. If the input is an enumerated type value, this function increments the last
    enumerated value to the first.

          Note You can manually configure this function to output data of a type you want. To
              specify the output data type, right-click the function and select Properties to display
             the Object Properties dialog box. On the Output Configuration page, click the
            Representation icon and select the data type you want. A blue coercion dot appears
           on the output terminal of the function to indicate that you have configured the
            output data type.


Examples

Refer to the following example files included with LabVIEW.

  • labview\examples\Numerics\Numeric Functions.vi

DecrementDecrement FunctionFunction

Subtracts 1 from the input value.

The connector pane displays the default data types for this polymorphic function.


Inputs/Outputs

   •      x —

    x specifies the input value.

    This input accepts the following data types:

         • Number
         • Timestamp
         • Analog Waveform


                                                    © National Instruments 6077

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6077 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6078 ordinal=6078 -->
## Functions

Functions


             This input also accepts an array or an array of clusters of the listed data types.

               •       x-1 —

             x-1 is the result of x-1. If the input is a time stamp value, this function decrements the time by
          one second. If the input is an enumerated type value, this function decrements the first
           enumerated value to the last.

               Note You can manually configure this function to output data of a type you want. To
                      specify the output data type, right-click the function and select Properties to display
                     the Object Properties dialog box. On the Output Configuration page, click the
                    Representation icon and select the data type you want. A blue coercion dot appears
                 on the output terminal of the function to indicate that you have configured the
                    output data type.


     Examples

       Refer to the following example files included with LabVIEW.

            • labview\examples\Numerics\Numeric Functions.vi

     CompoundCompound ArithmeticArithmetic

      Performs arithmetic on one or more numeric, array, cluster, or Boolean inputs. To
        select the operation (Add, Multiply, AND, OR, or XOR), right-click the function and
        select Change Mode from the shortcut menu. When you select this function from the
      Numeric palette, the default mode is Add. When you select this function from the
      Boolean palette, the default mode is OR.

      The connector pane displays the default data types for this polymorphic function.


6078   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6078 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6079 ordinal=6079 -->
## Functions

Functions

Inputs/Outputs

   •      value —

    value 0..n-1 can be a number or Boolean value, an array of numbers or Boolean values, a cluster,
    array of clusters, and so on.

    You can wire a waveform to only one value input. If an input is a waveform, you can have an
    unlimited number of scalar inputs of varying sizes. If value is an error cluster, only the status
    parameter of the error cluster passes to the input terminal.

   •      value —

   •       result —

     result returns the result of the selected operation applied to the value 0..n-1. For AND, OR, or
    XOR, result returns the bitwise operations on numeric inputs and logical operations on Boolean
     inputs.


Add inputs to the node by right-clicking an input and selecting Add Input from the
shortcut menu or by resizing the function.

You can invert the inputs or the output of this function by right-clicking the individual
terminals and selecting Invert from the shortcut menu. For Add, select Invert to
negate an input or the output. For Multiply, select Invert to use the reciprocal of an
input or to produce the reciprocal of the output. For AND, OR, or XOR, select Invert to
bitwise complement an integer input or output or to logically negate an input or
output.

When you use the Compound Arithmetic function to perform an XOR operation on 3 or
more values, the Compound Arithmetic function performs an XOR operation on the
first pair of inputs, then performs an XOR operation on the result of the first pair of
inputs and the next input, and so on until all inputs have been processed.

      Note You cannot use this function with fixed-point numbers. If you wire
        fixed-point numbers to this function, the VI appears with a broken Run
        button.


                                                    © National Instruments 6079

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6079 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6080 ordinal=6080 -->
## Functions

Functions

      AbsoluteAbsolute ValueValue FunctionFunction

       Returns the absolute value of the input.

      The connector pane displays the default data types for this polymorphic function.


      Inputs/Outputs

               •      x —

           x can be a scalar number, a fixed-point number, an array or cluster of numbers, an array of
              clusters of numbers, and so on.

           x cannot be an unsigned integer, because unsigned integers represent only non-negative
              integers.

               •       abs(x) —

            abs(x) is the absolute value of x.

         When x is of the form x = a + bi, that is, when x is complex, the following equation defines abs(x):


     When you wire matrix data as an input to this function, a VI that includes subVIs that
      work with the matrix data type replaces the function. The resulting VI has the same
       icon but contains a matrix-specific algorithm. The node remains a VI if you disconnect
       the matrix from the inputs. Wire other data types as inputs to restore the original
       function. If you wire a data type to a function and that data type causes a basic math
       operation to fail, the function returns a NaN.

           If the absolute value of x is outside the range of the data type of x, abs(x) overflows to
      a value within the range of the data type. For example, if x is an 8-bit integer and the
       value of x is -128, abs(x) returns -128 since 128 is outside the range of 8-bit integers,
       -128 to 127.


6080   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6080 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6081 ordinal=6081 -->
## Functions

Functions

Examples

Refer to the following example files included with LabVIEW.

  • labview\examples\Numerics\Numeric Functions.vi

RoundRound ToTo NearestNearest FunctionFunction

Rounds the input to the nearest integer. If the value of the input is midway between
two integers, the function returns the nearest even integer.

For example, if number is 1.5 or 2.5, nearest integer value is 2.

      Note Note IEEE standards determine the rounding method for this function.
        This method produces more accurate values with no positive or negative bias
       because it does not round all integers in the same direction.

The connector pane displays the default data types for this polymorphic function.


Inputs/Outputs

   •     number —

   number can be a scalar number, array or cluster of numbers, array of clusters of numbers, and
    so on.

   •      nearest integer value —

    nearest integer value is the resulting nearest integer to number. If the input is a time stamp
     value, the function rounds to the nearest second.

   When number is in the form of a + bi, that is, when number is complex, the function returns a
    complex number defined by the nearest integer to the real and imaginary parts of number. The
    following equation defines nearest integer value: nearest integer value(x) = nearest integer
     value(a) + i* nearest integer value(b)


                                                    © National Instruments 6081

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6081 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6082 ordinal=6082 -->
## Functions

Functions

     Examples

       Refer to the following example files included with LabVIEW.

            • labview\examples\Numerics\Numeric Functions.vi

     RoundRound TowardToward -Infinity-Infinity FunctionFunction

       Truncates the input to the next lowest integer.

       For example, if the input is 3.8, the result is 3. If the input is –3.8, the result is –4. The
       connector pane displays the default data types for this polymorphic function.


      Inputs/Outputs

               •      x —

           x can be a scalar number, array or cluster of numbers, array of clusters of numbers, and so on.

               •       floor(x): largest int <= x —

              floor(x): largest int ≤ x is the resulting lowest integer, closest to x. If the input is a time stamp
             value, the function rounds to the previous second.

         When x is of the form x = a + bi, that is, when x is complex, the function returns a complex
          number defined by the next lowest integers to the real and imaginary parts of x. The following
            equation defines floor(x): largest int ≤ x: floor(x) = floor(a) + ifloor(b)

     RoundRound TowardToward +Infinity+Infinity FunctionFunction

      Rounds the input to the next highest integer.

       For example, if the input is 3.1, the result is 4. If the input is –3.1, the result is –3. The
       connector pane displays the default data types for this polymorphic function.


6082   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6082 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6083 ordinal=6083 -->
## Functions

Functions


Inputs/Outputs

   •      x —

    x can be a scalar number, array or cluster of numbers, array of clusters of numbers, and so on.

   •        ceil(x): smallest int >= x —

     ceil(x): smallest int >= x is the resulting highest integer, closest to x. If the input is a time stamp
     value, the function rounds to the next second.

   When x is of the form x = a + bi, that is, when x is complex, the function returns a complex
   number defined by the next highest integers to the real and imaginary parts of x. The following
    equation defines ceil(x): smallest int >= x: ceil(x) = ceil(a) + iceil(b)

ScaleScale ByBy PowerPower OfOf 22 FunctionFunction

Multiplies x by 2 raised to the power of n.

If x is an integer or fixed-point number, this function is the equivalent of an arithmetic
shift. The connector pane displays the default data types for this polymorphic
function.


Inputs/Outputs

   •     n —

   n can be a scalar number, array or cluster of numbers, array of clusters of numbers, and so on.

       If n is a floating-point number, this function rounds n before it scales x (0.5 rounds to 0; 0.51
    rounds to 1). If n is a 64-bit integer, LabVIEW coerces n to a 32-bit integer.
   •      x —

    x can be a scalar number, array or cluster of numbers, array of clusters of numbers, and so on.

   •      x*2^n —

                                                    © National Instruments 6083

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6083 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6084 ordinal=6084 -->
## Functions

Functions


           x*2^n is the result of multiplying x by 2, raised to the power of n.


           If you wire a fixed-point value to this function, the resulting output value retains the
       fixed-point configuration settings of the input value. However, the value is likely to
       truncate or wrap.

     Examples

       Refer to the following example files included with LabVIEW.

            • labview\examples\Numerics\Numeric Functions.vi

      SquareSquare RootRoot FunctionFunction

      Computes the square root of the input value.

           If x is negative, the square root is NaN unless x is complex. If x is a matrix, this function
       takes the matrix square root of x. The connector pane displays the default data types
        for this polymorphic function.

           Note If you wire a value that has a unit with an odd exponent to the square
               root function, the wire breaks because LabVIEW does not support units with
                fractional exponents. For example, 15m² is an acceptable input value, but
            15m3 is not an acceptable input value.


      Inputs/Outputs

               •      x —

           x can be a scalar number, array or cluster of numbers, array of clusters of numbers, and so on.

               •       sqrt(x) —


6084   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6084 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6085 ordinal=6085 -->
## Functions

Functions


     sqrt(x) is a double-precision, floating-point number if x is an integer.

       If x is less than 0, sqrt(x) is not a number (NaN), unless x is complex. When x is of the form x = a +
     bi, that is, when x is complex, the function defines the magnitude and phase with the following
    equations:                            where |x| is the magnitude of x and arg(x) is the

    phase of x:              arg(x) = arctan2(b,a)

          Note You can manually configure this function to output data of a type you want. To
              specify the output data type, right-click the function and select Properties to display
             the Object Properties dialog box. On the Output Configuration page, click the
            Representation icon and select the data type you want. A blue coercion dot appears
           on the output terminal of the function to indicate that you have configured the
            output data type.


When you wire matrix data as an input to this function, a VI that includes subVIs that
work with the matrix data type replaces the function. The resulting VI has the same
icon but contains a matrix-specific algorithm. The node remains a VI if you disconnect
the matrix from the input(s). Wire other data types as inputs to restore the original
function. If you wire a data type to a function and that data type causes a basic math
operation to fail, the function returns an empty matrix or NaN.

Refer to the Matrix Square Root VI for more information.

Fixed-Point Details

If you wire a signed fixed-point value to this function, the function converts the signed
number into a floating-point number and performs the square root operation. By
default, LabVIEW configures the integer word length of the square root to avoid
overflow. However, because the precision of the square root can be infinite, rounding
conditions always occur. Use the Numeric Node Properties dialog box to configure
how LabVIEW handles overflow and rounding of fixed-point data.

Examples

Refer to the following example files included with LabVIEW.


                                                    © National Instruments 6085

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6085 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6086 ordinal=6086 -->
## Functions

Functions

            • labview\examples\Numerics\Numeric Functions.vi

      SquareSquare FunctionFunction

      Computes the square of the input value.

      The connector pane displays the default data types for this polymorphic function.


      Inputs/Outputs

               •      x —

           x can be a scalar number, array or cluster of numbers, array of clusters of numbers, and so on.

               •      x^2 —

           x^2 is of the same numeric representation as x.

               Note You can manually configure this function to output data of a type you want. To
                      specify the output data type, right-click the function and select Properties to display
                     the Object Properties dialog box. On the Output Configuration page, click the
                    Representation icon and select the data type you want. A blue coercion dot appears
                 on the output terminal of the function to indicate that you have configured the
                    output data type.


           If you wire fixed-point values to Numeric functions such as Add, Subtract, Multiply, and
       Square, the functions usually return values that do not lose any bits of word length.
      However, if the operation creates a value that exceeds the maximum word length that
      LabVIEW accepts, overflow or rounding conditions can occur. LabVIEW accepts a
     maximum word length of 64 bits. Use the Numeric Node Properties dialog box to
       configure how LabVIEW handles overflow or rounding of fixed-point data.

     Examples

       Refer to the following example files included with LabVIEW.


6086   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6086 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6087 ordinal=6087 -->
## Functions

Functions

  • labview\examples\Numerics\Numeric Functions.vi

NegateNegate FunctionFunction

Negates the input value.

The connector pane displays the default data types for this polymorphic function.


Inputs/Outputs

   •      x —

    x can be a scalar number, a fixed-point number, an array or cluster of numbers, an array of
     clusters of numbers, and so on. x cannot be an unsigned integer, because unsigned integers
    represent only non-negative integers.

   •       -x —

     -x is the negative value of x.


Examples

Refer to the following example files included with LabVIEW.

  • labview\examples\Numerics\Numeric Functions.vi

ReciprocalReciprocal FunctionFunction

Divides 1 by the input value.

The connector pane displays the default data types for this polymorphic function.


                                                    © National Instruments 6087

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6087 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6088 ordinal=6088 -->
## Functions

Functions

      Inputs/Outputs

               •      x —

           x can be a scalar number, array or cluster of numbers, array of clusters of numbers, and so on.

               •      1/x —

            1/x is infinity if x is 0. If x is an integer, 1/x is a double-precision, floating-point number.


      Fixed-Point Details

           If you wire a fixed-point value to this function, by default LabVIEW configures the
       integer word length of the reciprocal to avoid overflow. However, because the
       precision of the reciprocal can be infinite, rounding conditions always occur. Use the
      Numeric Node Properties dialog box to configure how LabVIEW handles rounding of
       fixed-point data. This function always uses the Saturate overflow mode to handle
       overflow.

     Examples

       Refer to the following example files included with LabVIEW.

            • labview\examples\Numerics\Numeric Functions.vi

      SignSign FunctionFunction

       Returns the sign of number.

           Note For nonzero complex numbers, this function returns a complex value
              with the same phase as the input and with a magnitude of 1.

       Text-based programming languages typically call this function signum or sgn. The
       connector pane displays the default data types for this polymorphic function.


6088   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6088 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6089 ordinal=6089 -->
## Functions

Functions

Inputs/Outputs

   •     number —

   number can be a scalar number, array or cluster of numbers, array of clusters of numbers, and
    so on.

   •        -1, 0, 1 —

     –1, 0, 1 returns 1 if the input value is greater than 0, returns 0 if the input value is equal to 0, and
    returns –1 if the input value is less than 0.

   When number is in the form of a + bi, that is, when number is complex, the following defines -1,
     0, 1:

Examples

Refer to the following example files included with LabVIEW.

  • labview\examples\Numerics\Numeric Functions.vi

NumericNumeric ConstantConstant

Use the numeric constant to pass a numeric value to the block diagram. Set this value
by clicking inside the constant with the Operating tool and typing a value.

If you enter a floating-point number for the numeric constant, the default
representation is a double-precision, floating-point number. If you enter an integer,
the default representation is a 32-bit integer. If you enter a complex number, the
default representation is a double-precision, complex number. For example, if you
enter 123, the representation is a 32-bit integer. If you enter 123., the representation is
a double-precision, floating-point number. You also can change the numeric
representation of a numeric constant.

You cannot change the value of the numeric constant while the VI runs. You can assign
a label to this constant.


                                                    © National Instruments 6089

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6089 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6090 ordinal=6090 -->
## Functions

Functions

     RandomRandom NumberNumber (0-1)(0-1) FunctionFunction

      Produces a double-precision, floating-point number between 0 and 1. The number
       generated is greater than or equal to 0, but less than 1. The distribution is uniform.

        Alternatively, you can use several of the Signal Generation VIs or the Signal Generation
      PtByPt VIs to regenerate the same random sequence. For example, the Uniform White
       Noise VI allows you to set a seed number that you can use to initialize the generation
       of a pseudorandom pattern.


      Inputs/Outputs

               •     number (0 to 1) —

          number (0 to 1) is a double-precision, floating-point number between 0 and 1.


       PositivePositive InfinityInfinity

       Returns the value Inf (infinity).

      LabVIEW converts Inf to the highest value for a data type. For example, converting Inf
       to a 16-bit signed integer returns the value 32,767, the highest possible value for a
        16-bit signed integer.


      NegativeNegative InfinityInfinity

       Returns the value -Inf (negative infinity).

      LabVIEW converts -Inf to the lowest value for a data type. For example, converting -Inf
       to a 16-bit signed integer returns the value -32,768, the lowest possible value for a
        16-bit signed integer.


6090   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6090 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6091 ordinal=6091 -->
## Functions

Functions


MachineMachine EpsilonEpsilon

Represents the round-off error for a floating-point number with a given precision. Use
the machine epsilon constant to compare whether two floating-point numbers are
equivalent.


ExpressExpress MathMath && ScientificScientific ConstantsConstants

Use the Express Math & Scientific Constants to create LabVIEW applications.

The following constants are Committee on Data for Science and Technology (CODATA)
2006 values. Some of the constants on this palette have units.


 Palette Object                             Description

 Pi                                        Returns the value 3.1415926535897932.

 Pi Multiplied By 2                          Returns the value 6.2831853071795865.

 Pi Divided By 2                            Returns the value 1.5707963267948966.

 Reciprocal Of Pi                           Returns the value 0.31830988618379067.

 Natural Logarithm Of Pi                    Returns the value 1.1447298858494002.

 Natural Logarithm Base                    Returns the value 2.7182818284590452.

 Reciprocal Of e                            Returns the value 0.36787944117144232.

 Base 10 Logarithm Of e                     Returns the value 0.43429448190325183.

 Natural Logarithm Of 10                    Returns the value 2.3025850929940597.

 Natural Logarithm Of 2                     Returns the value 0.69314718055994531.

 Planck's Constant (J/Hz)                    Returns the value 6.62607015e-34.

                                                    © National Instruments 6091

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6091 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6092 ordinal=6092 -->
## Functions

Functions


         Palette Object                             Description

        Elementary Charge (C)                     Returns the value 1.602176634e-19.

       Speed Of Light In Vacuum (m/sec)           Returns the value 299792458.

         Gravitational Constant (N m2/kg2)           Returns the value 6.67430e-11.

        Avogadro Constant (1/mol)                 Returns the value 6.02214076e23.

        Rydberg Constant (1/m)                    Returns the value 10973731.568160.

        Molar Gas Constant (J/(mol K))              Returns the value 8.314462618.

    PiPi

       Returns the value 3.1415926535897932.


    PiPi MultipliedMultiplied ByBy 22

       Returns the value 6.2831853071795865.


    PiPi DividedDivided ByBy 22

       Returns the value 1.5707963267948966.


    ReciprocalReciprocal OfOf PiPi

       Returns the value 0.31830988618379067.

6092   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6092 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6093 ordinal=6093 -->
## Functions

Functions


NaturalNatural LogarithmLogarithm OfOf PiPi

Returns the value 1.1447298858494002.


NaturalNatural LogarithmLogarithm BaseBase

Returns the value 2.7182818284590452.


ReciprocalReciprocal OfOf ee

Returns the value 0.36787944117144232.


BaseBase 1010 LogarithmLogarithm OfOf ee

Returns the value 0.43429448190325183.


                                                    © National Instruments 6093

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6093 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6094 ordinal=6094 -->
## Functions

Functions

    NaturalNatural LogarithmLogarithm OfOf 1010

       Returns the value 2.3025850929940597.


    NaturalNatural LogarithmLogarithm OfOf 22

       Returns the value 0.69314718055994531.


    Planck'sPlanck's ConstantConstant (J/Hz)(J/Hz)

       Returns the value 6.62607015e-34.


   ElementaryElementary ChargeCharge (C)(C)

       Returns the value 1.602176634e-19.


   SpeedSpeed OfOf LightLight InIn VacuumVacuum (m/sec)(m/sec)

       Returns the value 299792458.


6094   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6094 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6095 ordinal=6095 -->
## Functions

Functions


GravitationalGravitational ConstantConstant (N(N m2/kg2)m2/kg2)

Returns the value 6.67430e-11.


AvogadroAvogadro ConstantConstant (1/mol)(1/mol)

Returns the value 6.02214076e23.


RydbergRydberg ConstantConstant (1/m)(1/m)

Returns the value 10973731.568160.


MolarMolar GasGas ConstantConstant (J/(mol(J/(mol K))K))

Returns the value 8.314462618.


ExpressExpress MathMath

Use the Math functions to create and to perform logarithmic and trigonometric
equations and to compute hyperbolic functions and their inverses.

                                                    © National Instruments 6095

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6095 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6096 ordinal=6096 -->
## Functions

Functions


         Palette Object            Description

         Express Trigonometric    Use the Express Trigonometric functions to create and to perform
         Functions                trigonometric equations.


         Express Exponential      Use the Express Exponential functions to create and perform
         Functions                exponential equations.


         Express Hyperbolic       Use the Express Hyperbolic functions to create and to perform
         Functions                hyperbolic equations.


      ExpressExpress TrigonometricTrigonometric FunctionsFunctions

      Use the Express Trigonometric functions to create and to perform trigonometric
       equations.


         Palette Object         Description

         Sine Function        Computes the sine of x, where x is in radians.

        Cosine Function      Computes the cosine of x, where x is in radians.

        Tangent Function     Computes the tangent of x, where x is in radians.

                          Computes the secant of x, where x is in radians. Secant is the reciprocal of
        Secant Function
                                 cosine.

                          Computes the cosecant of x, where x is in radians. Cosecant is the
        Cosecant Function
                                  reciprocal of sine.

                          Computes the cotangent of x, where x is in radians. Cotangent is the
        Cotangent Function
                                  reciprocal of tangent.


6096   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6096 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6097 ordinal=6097 -->
## Functions

Functions


 Palette Object         Description

 Inverse Sine Function  Computes the arcsine of x.

 Inverse Cosine                   Computes the arccosine of x. Function

 Inverse Tangent                   Computes the arctangent of x.
 Function

 Inverse Secant                   Computes the inverse secant of x. Function

 Inverse Cosecant                   Computes the inverse cosecant of x.
 Function

 Inverse Cotangent                   Computes the inverse cotangent of x. Function

 Sine & Cosine        Computes both the sine and cosine of x, where x is in radians. Use this
 Function               function only when you need both results.

 Sinc Function        Computes the sine of x divided by x, where x is in radians.

 Inverse Tangent (2                   Computes the arctangent of y/x.
 Input) Function

SineSine FunctionFunction

Computes the sine of x, where x is in radians.

The connector pane displays the default data types for this polymorphic function.


Inputs/Outputs

   •      x —

    x can be a scalar number, array or cluster of numbers, array of clusters of numbers, and so on.

   •       sin(x) —


                                                    © National Instruments 6097

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6097 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6098 ordinal=6098 -->
## Functions

Functions


              sin(x) is of the same numeric representation as x.

         When x is of the form x = a + bi, that is, when x is complex, the following equation defines sin(x):
              sin(x) = sin(a) * cosh(b) + i(cos(a) * sinh(b))

     Examples

       Refer to the following example files included with LabVIEW.

            • labview\examples\Mathematics\Elementary & Special
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


6098   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6098 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6099 ordinal=6099 -->
## Functions

Functions

Examples

Refer to the following example files included with LabVIEW.

  • labview\examples\Mathematics\Elementary & Special
   Functions\Trigonometric Functions\Sine.vi
TangentTangent FunctionFunction

Computes the tangent of x, where x is in radians.

The connector pane displays the default data types for this polymorphic function.


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


                                                    © National Instruments 6099

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6099 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6100 ordinal=6100 -->
## Functions

Functions

   SecantSecant FunctionFunction

      Computes the secant of x, where x is in radians. Secant is the reciprocal of cosine.

      The connector pane displays the default data types for this polymorphic function.


      Inputs/Outputs

               •      x —

           x can be a scalar number, array or cluster of numbers, array of clusters of numbers, and so on.

               •       1/cos(x) —

             1/cos(x) is of the same numeric representation as x.


     Examples

       Refer to the following example files included with LabVIEW.

            • labview\examples\Mathematics\Elementary & Special
        Functions\Trigonometric Functions\Sine.vi
   CosecantCosecant FunctionFunction

      Computes the cosecant of x, where x is in radians. Cosecant is the reciprocal of sine.

      The connector pane displays the default data types for this polymorphic function.


6100   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6100 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6101 ordinal=6101 -->
## Functions

Functions

Inputs/Outputs

   •      x —

    x can be a scalar number, array or cluster of numbers, array of clusters of numbers, and so on.

   •       1/sin(x) —

     1/sin(x) is of the same numeric representation as x.


Examples

Refer to the following example files included with LabVIEW.

  • labview\examples\Mathematics\Elementary & Special
   Functions\Trigonometric Functions\Sine.vi
CotangentCotangent FunctionFunction

Computes the cotangent of x, where x is in radians. Cotangent is the reciprocal of
tangent.

The connector pane displays the default data types for this polymorphic function.


Inputs/Outputs

   •      x —

    x can be a scalar number, array or cluster of numbers, array of clusters of numbers, and so on.

   •       1/tan(x) —

    1/tan(x) is of the same numeric representation as x.


                                                    © National Instruments 6101

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6101 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6102 ordinal=6102 -->
## Functions

Functions

     Examples

       Refer to the following example files included with LabVIEW.

            • labview\examples\Mathematics\Elementary & Special
        Functions\Trigonometric Functions\Sine.vi
    InverseInverse SineSine FunctionFunction

      Computes the arcsine of x.

           If x is not complex and is less than –1 or greater than 1, the result is NaN. The
       connector pane displays the default data types for this polymorphic function.


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


6102   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6102 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6103 ordinal=6103 -->
## Functions

Functions

InverseInverse CosineCosine FunctionFunction

Computes the arccosine of x.

If x is not complex and is less than –1 or greater than 1, the result is NaN. The
connector pane displays the default data types for this polymorphic function.


Inputs/Outputs

   •      x —

    x can be a scalar number, array or cluster of numbers, array of clusters of numbers, and so on.

   •       arccos(x) —

    arccos(x) is of the same numeric representation as x. When x is of the form x = a + bi, that is,
   when x is complex, the following equation defines arccos(x):


Examples

Refer to the following example files included with LabVIEW.

  • labview\examples\Mathematics\Elementary & Special
   Functions\Trigonometric Functions\Sine.vi
InverseInverse TangentTangent FunctionFunction

Computes the arctangent of x.

The connector pane displays the default data types for this polymorphic function.


                                                    © National Instruments 6103

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6103 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6104 ordinal=6104 -->
## Functions

Functions


      Inputs/Outputs

               •      x —

           x can be a scalar number, array or cluster of numbers, array of clusters of numbers, and so on.

               •       arctan(x) —

             arctan(x) is of the same numeric representation as x. When x is of the form x = a + bi, that is,
          when x is complex, the following equation defines arctan(x):


             arctan(x) ranges from -pi/2 to pi/2.


     Examples

       Refer to the following example files included with LabVIEW.

            • labview\examples\Mathematics\Elementary & Special
        Functions\Trigonometric Functions\Sine.vi
    InverseInverse SecantSecant FunctionFunction

      Computes the inverse secant of x.

      The connector pane displays the default data types for this polymorphic function.


      Inputs/Outputs

               •      x —

6104   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6104 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6105 ordinal=6105 -->
## Functions

Functions


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


Inputs/Outputs

   •      x —

    x can be a scalar number, array or cluster of numbers, array of clusters of numbers, and so on.

   •       arccsc(x) —

     arccsc(x) is of the same numeric representation as x.


Examples

Refer to the following example files included with LabVIEW.


                                                    © National Instruments 6105

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6105 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6106 ordinal=6106 -->
## Functions

Functions

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


     Examples

       Refer to the following example files included with LabVIEW.

            • labview\examples\Mathematics\Elementary & Special
        Functions\Trigonometric Functions\Sine.vi
   SineSine && CosineCosine FunctionFunction

      Computes both the sine and cosine of x, where x is in radians. Use this function only
     when you need both results.

      The connector pane displays the default data types for this polymorphic function.


6106   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6106 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6107 ordinal=6107 -->
## Functions

Functions


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

The connector pane displays the default data types for this polymorphic function.


Inputs/Outputs

   •      x —

    x can be a scalar number, array or cluster of numbers, array of clusters of numbers, and so on.

   •       sin(x)/x —


                                                    © National Instruments 6107

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6107 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6108 ordinal=6108 -->
## Functions

Functions


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

           y can be a scalar number, array or cluster of numbers, array of clusters of numbers, and so on.

               •      x —

           x can be a scalar number, array or cluster of numbers, array of clusters of numbers, and so on.

               •       atan2(y,x) —

             atan2(y,x) is the arctangent of y and x, in radians. atan2(y,x) falls in the range [-pi, pi]. When x or
           y are complex, the following equation defines atan2(y,x):


6108   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6108 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6109 ordinal=6109 -->
## Functions

Functions


Examples

Refer to the following example files included with LabVIEW.

  • labview\examples\Mathematics\Elementary & Special
   Functions\Trigonometric Functions\Sine.vi

ExpressExpress ExponentialExponential FunctionsFunctions

Use the Express Exponential functions to create and perform exponential equations.


 Palette Object     Description

 Exponential                Computes the value of e raised to the x power, or the exponential of x. Function

 Exponential (Arg)                Computes 1 less than the value of e raised to the x power. -1 Function

 Power Of 10                Computes 10 raised to the x power. Function

 Power Of 2
                Computes 2 raised to the x power.
 Function

 Power Of X
                Computes x raised to the y power.
 Function

 Y-th Root of X      Returns the yth root of the input value x. If x is not complex, x must be greater
 Function          than or equal to zero unless y is an integer. Otherwise, the result is NaN.

 Natural Logarithm
                Computes the base e natural logarithm of x.
 Function

 Natural Logarithm
                Computes the natural logarithm of (x + 1).
 (Arg +1) Function


                                                    © National Instruments 6109

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6109 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6110 ordinal=6110 -->
## Functions

Functions


         Palette Object     Description

        Logarithm Base                       Computes the base 10 logarithm of x.        10 Function

        Logarithm Base 2                       Computes the base 2 logarithm of x.         Function

        Logarithm Base X                       Computes the base x logarithm of y.         Function

    ExponentialExponential FunctionFunction

      Computes the value of e raised to the x power, or the exponential of x.

           Note For very small values of x, the Exponential (Arg) -1 function is more
              accurate than using this function then subtracting 1 from the output.

      The connector pane displays the default data types for this polymorphic function.


      Inputs/Outputs

               •      x —

           x can be a scalar number, array or cluster of numbers, array of clusters of numbers, and so on.

               •      exp(x) —

            exp(x) is of the same numeric representation as x. The following equation defines the
            exponential exp(x):

             exp(a+bi) = exp(a)(cos(b)+i sin(b))

          when x is of the form x = a + bi, that is, when x is complex.


           If x is a matrix, this function computes the exponential of x. When you wire matrix data

6110   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6110 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6111 ordinal=6111 -->
## Functions

Functions

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


Inputs/Outputs

   •      x —

    x can be a scalar number, array or cluster of numbers, array of clusters of numbers, and so on.

   •      exp(x) -1 —

    exp(x)-1 is of the same numeric representation as x.

   When x is of the form x = a + bi, that is, when x is complex, the following equation defines
    exp(x)-1:exp(x)-1 = (exp(a) * (cos(b)+i sin(b))) – 1

                                                    © National Instruments 6111

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6111 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6112 ordinal=6112 -->
## Functions

Functions

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

           10^x is of the same numeric representation as x.

         When x is of the form x = a + bi, that is, when x is complex, the following equation defines
            10^x:10^x = 10^a * 10^(bi) = 10^a * (cos(b * ln(10)) + i sin (b * ln(10)))

     Examples

       Refer to the following example files included with LabVIEW.

            • labview\examples\Mathematics\Elementary & Special
        Functions\Exponential Functions\Exponential.vi


6112   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6112 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6113 ordinal=6113 -->
## Functions

Functions

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
   Functions\Exponential Functions\Exponential.vi
PowerPower OfOf XX FunctionFunction

Computes x raised to the y power.

If x is not complex, it must be greater than zero unless y is an integer value. Otherwise,
the result is NaN. If y is 0, x^y is 1 for all values of x, including 0. The connector pane
displays the default data types for this polymorphic function.


                                                    © National Instruments 6113

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6113 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6114 ordinal=6114 -->
## Functions

Functions


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

     Examples

       Refer to the following example files included with LabVIEW.

            • labview\examples\Mathematics\Elementary & Special
        Functions\Exponential Functions\Exponential.vi
    Y-thY-th RootRoot ofof XX FunctionFunction

       Returns the yth root of the input value x. If x is not complex, x must be greater than or

6114   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6114 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6115 ordinal=6115 -->
## Functions

Functions

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
   Functions\Exponential Functions\Exponential.vi
NaturalNatural LogarithmLogarithm FunctionFunction

Computes the base e natural logarithm of x.

If x is 0, ln(x) is –∞. If x is not complex and is less than 0, ln(x) is NaN.

      Note For very small values of x, the Natural Logarithm (Arg +1) function is


                                                    © National Instruments 6115

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6115 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6116 ordinal=6116 -->
## Functions

Functions


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

     Examples

       Refer to the following example files included with LabVIEW.

            • labview\examples\Mathematics\Elementary & Special
        Functions\Exponential Functions\Exponential.vi


6116   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6116 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6117 ordinal=6117 -->
## Functions

Functions

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
LogarithmLogarithm BaseBase 1010 FunctionFunction

Computes the base 10 logarithm of x.

If x is 0, log(x) is negative infinity. If x is not complex and is less than 0, log(x) is NaN.
The connector pane displays the default data types for this polymorphic function.


                                                    © National Instruments 6117

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6117 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6118 ordinal=6118 -->
## Functions

Functions


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


      Inputs/Outputs

               •      x —


6118   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6118 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6119 ordinal=6119 -->
## Functions

Functions


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

   •      x —

    x can be a scalar number, array or cluster of numbers, array of clusters of numbers, and so on.

   •       logx(y) —

                                                    © National Instruments 6119

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6119 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6120 ordinal=6120 -->
## Functions

Functions


             logx(y) is the logarithm of y to the base x. When x and y are complex, the following equation
             defines logx(y):

             logx(y) = ln(y)/ln(x)

             Refer to the Natural Logarithm function for more information.


     Examples

       Refer to the following example files included with LabVIEW.

            • labview\examples\Mathematics\Elementary & Special
        Functions\Exponential Functions\Exponential.vi

      ExpressExpress HyperbolicHyperbolic FunctionsFunctions

      Use the Express Hyperbolic functions to create and to perform hyperbolic equations.


         Palette Object                             Description

         Hyperbolic Sine Function                Computes the hyperbolic sine of x.

         Hyperbolic Cosine Function              Computes the hyperbolic cosine of x.

         Hyperbolic Tangent Function             Computes the hyperbolic tangent of x.

         Hyperbolic Secant Function              Computes the hyperbolic secant of x.

         Hyperbolic Cosecant Function            Computes the hyperbolic cosecant of x.

         Hyperbolic Cotangent Function           Computes the hyperbolic cotangent of x.

         Inverse Hyperbolic Sine Function          Computes the inverse hyperbolic sine of x.

         Inverse Hyperbolic Cosine Function        Computes the inverse hyperbolic cosine of x.

         Inverse Hyperbolic Tangent Function       Computes the inverse hyperbolic tangent of x.

         Inverse Hyperbolic Secant Function        Computes the inverse hyperbolic secant of x.

         Inverse Hyperbolic Cosecant Function      Computes the inverse hyperbolic cosecant of x.

6120   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6120 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6121 ordinal=6121 -->
## Functions

Functions


 Palette Object                             Description

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
HyperbolicHyperbolic CosineCosine FunctionFunction

Computes the hyperbolic cosine of x.

The connector pane displays the default data types for this polymorphic function.


                                                    © National Instruments 6121

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6121 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6122 ordinal=6122 -->
## Functions

Functions


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

           x can be a scalar number, array or cluster of numbers, array of clusters of numbers, and so on.

               •      tanh(x) —


6122   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6122 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6123 ordinal=6123 -->
## Functions

Functions


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
   Functions\Trigonometric Functions\Sine.vi


                                                    © National Instruments 6123

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6123 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6124 ordinal=6124 -->
## Functions

Functions

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


6124   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6124 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6125 ordinal=6125 -->
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


                                                    © National Instruments 6125

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6125 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6126 ordinal=6126 -->
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


6126   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6126 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6127 ordinal=6127 -->
## Functions

Functions

InverseInverse HyperbolicHyperbolic TangentTangent FunctionFunction

Computes the inverse hyperbolic tangent of x.

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


                                                    © National Instruments 6127

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6127 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6128 ordinal=6128 -->
## Functions

Functions


      Inputs/Outputs

               •      x —

           x can be a scalar number, array or cluster of numbers, array of clusters of numbers, and so on.

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


6128   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6128 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6129 ordinal=6129 -->
## Functions

Functions

Examples

Refer to the following example files included with LabVIEW.

  • labview\examples\Mathematics\Elementary & Special
   Functions\Trigonometric Functions\Sine.vi
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

ExpressExpress BooleanBoolean

Use the Express Boolean functions to perform logical operations on Boolean values.

                                                    © National Instruments 6129

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6129 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6130 ordinal=6130 -->
## Functions

Functions


         Palette                   Description        Object

                Computes the logical AND of the inputs. Both inputs must be Boolean values, numeric
       And                    values, or error clusters. If both inputs are TRUE, the function returns TRUE. Otherwise, it         Function                    returns FALSE.

                Computes the logical OR of the inputs. Both inputs must be Boolean values, numeric        Or                    values, or error clusters. If both inputs are FALSE, the function returns FALSE. Otherwise,
         Function                             it returns TRUE.

         Exclusive Computes the logical exclusive or (XOR) of the inputs. Both inputs must be Boolean
        Or        values, numeric values, or error clusters. If both inputs are TRUE or both inputs are
         Function  FALSE, the function returns FALSE. Otherwise, it returns TRUE.

        Not      Computes the logical negation of the input. If x is FALSE, the function returns TRUE. If x is
         Function  TRUE, the function returns FALSE.

                Computes the logical NAND of the inputs. Both inputs must be Boolean values, numeric
        Not And                    values, or error clusters. If both inputs are TRUE, the function returns FALSE. Otherwise,         Function                             it returns TRUE.

                Computes the logical NOR of the inputs. Both inputs must be Boolean values, numeric        Not Or
                    values, or error clusters. If both inputs are FALSE, the function returns TRUE. Otherwise,         Function                             it returns FALSE.

        Not                Computes the logical negation of the logical exclusive or (XOR) of the inputs. Both inputs         Exclusive                must be Boolean values, numeric values, or error clusters. If both inputs are TRUE or
        Or                 both inputs are FALSE, the function returns TRUE. Otherwise, it returns FALSE.
         Function

                  Negates x and then computes the logical OR of y and the negated x. Both inputs must be
         Implies
                 Boolean values, numeric values, or error clusters. If x is TRUE and y is FALSE, the function
         Function
                    returns FALSE. Otherwise, it returns TRUE.

        True
                Use this constant to provide a value of TRUE to the block diagram.
        Constant

         False
                Use this constant to provide a value of FALSE to the block diagram.
        Constant


6130   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6130 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6131 ordinal=6131 -->
## Functions

Functions

AndAnd FunctionFunction

Computes the logical AND of the inputs. Both inputs must be Boolean values, numeric
values, or error clusters. If both inputs are TRUE, the function returns TRUE. Otherwise,
it returns FALSE.

      Note This function performs bitwise operations on numeric inputs.

The connector pane displays the default data types for this polymorphic function.


Inputs/Outputs

   •      x —

    x must be a Boolean value or a number.x can be a scalar, array or cluster of numbers or Boolean
     values, array of clusters of numbers or Boolean values, and so on. If x is an error cluster, only the
    status parameter of the error cluster passes to the input terminal.

   •      y —

    y must be a Boolean value or a number. y can be a scalar, array or cluster of numbers or Boolean
     values, arrays of clusters of numbers or Boolean values, and so on. If y is an error cluster, only
    the status parameter of the error cluster passes to the input terminal.

   •      x .and. y? —

    x .and. y? is the logical AND of x and y.


And Truth Table

 x             y              x .and. y?

 T            T            T

 T             F              F

 F            T              F

                                                    © National Instruments 6131

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6131 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6132 ordinal=6132 -->
## Functions

Functions


        x             y              x .and. y?

        F             F              F

     Examples

       Refer to the following example files included with LabVIEW.

            • labview\examples\Booleans\Boolean Functions.vi

      OrOr FunctionFunction

      Computes the logical OR of the inputs. Both inputs must be Boolean values, numeric
       values, or error clusters. If both inputs are FALSE, the function returns FALSE.
       Otherwise, it returns TRUE.

           Note This function performs bitwise operations on numeric inputs.

      The connector pane displays the default data types for this polymorphic function.


      Inputs/Outputs

               •      x —

           x must be a Boolean value or a number. x can be a scalar, array or cluster of numbers or Boolean
             values, array of clusters of numbers or Boolean values, and so on. If x is an error cluster, only the
             status parameter of the error cluster passes to the input terminal.

               •      y —

           y must be a Boolean value or a number. y can be a scalar, array or cluster of numbers or Boolean
             values, arrays of clusters of numbers or Boolean values, and so on. If y is an error cluster, only
            the status parameter of the error cluster passes to the input terminal.

               •      x .or. y? —


6132   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6132 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6133 ordinal=6133 -->
## Functions

Functions


    x .or. y? is the logical Or of x and y.


Or Truth Table

 x               y                x .or. y?

 T              T              T

 T               F              T

 F              T              T

 F               F               F

Examples

Refer to the following example files included with LabVIEW.

  • labview\examples\Booleans\Boolean Functions.vi

ExclusiveExclusive OrOr FunctionFunction

Computes the logical exclusive or (XOR) of the inputs. Both inputs must be Boolean
values, numeric values, or error clusters. If both inputs are TRUE or both inputs are
FALSE, the function returns FALSE. Otherwise, it returns TRUE.

      Note This function performs bitwise operations on numeric inputs.

The connector pane displays the default data types for this polymorphic function.


Inputs/Outputs

   •      x —


                                                    © National Instruments 6133

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6133 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6134 ordinal=6134 -->
## Functions

Functions


           x must be a Boolean value or a number.x can be a scalar, array or cluster of numbers or Boolean
             values, array of clusters of numbers or Boolean values, and so on. If x is an error cluster, only the
             status parameter of the error cluster passes to the input terminal.

               •      y —

           y must be a Boolean value or a number.y can be a scalar, array or cluster of numbers or Boolean
             values, arrays of clusters of numbers or Boolean values, and so on. If y is an error cluster, only
            the status parameter of the error cluster passes to the input terminal.

               •      x .xor. y? —

           x .xor. y? is the logical exclusive or (XOR) of x and y.


      Exclusive Or Truth Table

        x              y               x .xor. y?

       T             T              F

       T              F             T

        F             T             T

        F              F              F

     Examples

       Refer to the following example files included with LabVIEW.

            • labview\examples\Booleans\Boolean Functions.vi

      NotNot FunctionFunction

      Computes the logical negation of the input. If x is FALSE, the function returns TRUE. If x
         is TRUE, the function returns FALSE.

           Note This function performs bitwise operations on numeric inputs.


6134   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6134 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6135 ordinal=6135 -->
## Functions

Functions

The connector pane displays the default data types for this polymorphic function.


Inputs/Outputs

   •      x —

    x can be a scalar Boolean value or number, array or cluster of Boolean values or numbers, array
     of clusters of Boolean values or numbers, and so on. If x is an error cluster, only the status
    parameter of the error cluster passes to the input terminal.

   •       .not. x? —

     .not. x? is the logical negation of x.


Not Truth Table

 x                        .not. x?

 F                  T

 T                   F

Examples

Refer to the following example files included with LabVIEW.

  • labview\examples\Booleans\Boolean Functions.vi

NotNot AndAnd FunctionFunction

Computes the logical NAND of the inputs. Both inputs must be Boolean values,
numeric values, or error clusters. If both inputs are TRUE, the function returns FALSE.
Otherwise, it returns TRUE.

      Note This function performs bitwise operations on numeric inputs.


                                                    © National Instruments 6135

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6135 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6136 ordinal=6136 -->
## Functions

Functions

      The connector pane displays the default data types for this polymorphic function.


      Inputs/Outputs

               •      x —

           x must be a Boolean value or a number. x can be a scalar, array or cluster of numbers or Boolean
             values, array of clusters of numbers or Boolean values, and so on. If x is an error cluster, only the
             status parameter of the error cluster passes to the input terminal.

               •      y —

           y must be a Boolean value or a number. y can be a scalar, array or cluster of numbers or Boolean
             values, arrays of clusters of numbers or Boolean values, and so on. If y is an error cluster, only
            the status parameter of the error cluster passes to the input terminal.

               •       .not. (x .and. y)? —

              .not. (x .and. y)? is the logical NAND of x and y.


     Not And Truth Table

        x         y            .not. (x .and. y)?

       T         T         F

       T         F         T

        F         T         T

        F         F         T

     Examples

       Refer to the following example files included with LabVIEW.

            • labview\examples\Booleans\Boolean Functions.vi


6136   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6136 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6137 ordinal=6137 -->
## Functions

Functions

NotNot OrOr FunctionFunction

Computes the logical NOR of the inputs. Both inputs must be Boolean values, numeric
values, or error clusters. If both inputs are FALSE, the function returns TRUE.
Otherwise, it returns FALSE.

      Note This function performs bitwise operations on numeric inputs.

The connector pane displays the default data types for this polymorphic function.


Inputs/Outputs

   •      x —

    x must be a Boolean value or a number. x can be a scalar, array or cluster of numbers or Boolean
     values, array of clusters of numbers or Boolean values, and so on. If x is an error cluster, only the
    status parameter of the error cluster passes to the input terminal.

   •      y —

    y must be a Boolean value or a number. y can be a scalar, array or cluster of numbers or Boolean
     values, arrays of clusters of numbers or Boolean values, and so on. If y is an error cluster, only
    the status parameter of the error cluster passes to the input terminal.

   •       .not. (x .or. y)? —

     .not. (x .or. y)? is the logical NOR of x and y.


Not Or Truth Table

 x          y             .not. (x .or. y)?

 T         T          F

 T          F          F

 F         T          F

                                                    © National Instruments 6137

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6137 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6138 ordinal=6138 -->
## Functions

Functions


        x          y             .not. (x .or. y)?

        F          F          T

     Examples

       Refer to the following example files included with LabVIEW.

            • labview\examples\Booleans\Boolean Functions.vi

      NotNot ExclusiveExclusive OrOr FunctionFunction

      Computes the logical negation of the logical exclusive or (XOR) of the inputs. Both
       inputs must be Boolean values, numeric values, or error clusters. If both inputs are
     TRUE or both inputs are FALSE, the function returns TRUE. Otherwise, it returns FALSE.

           Note This function performs bitwise operations on numeric inputs.

      The connector pane displays the default data types for this polymorphic function.


      Inputs/Outputs

               •      x —

           x must be a Boolean value or a number. x can be a scalar, array or cluster of numbers or Boolean
             values, array of clusters of numbers or Boolean values, and so on. If x is an error cluster, only the
             status parameter of the error cluster passes to the input terminal.

               •      y —

           y must be a Boolean value or a number. y can be a scalar, array or cluster of numbers or Boolean
             values, arrays of clusters of numbers or Boolean values, and so on. If y is an error cluster, only
            the status parameter of the error cluster passes to the input terminal.

               •       .not. (x .xor. y)? —


6138   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6138 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6139 ordinal=6139 -->
## Functions

Functions


     .not. (x .xor. y)? is the logical negation of the logical exclusive or (XOR) of x and y.


Not Exclusive Or Truth Table>

 x          y            .not. (x .xor. y)?

 T         T         T

 T          F          F

 F         T          F

 F          F         T

Examples

Refer to the following example files included with LabVIEW.

  • labview\examples\Booleans\Boolean Functions.vi

ImpliesImplies FunctionFunction

Negates x and then computes the logical OR of y and the negated x. Both inputs must
be Boolean values, numeric values, or error clusters. If x is TRUE and y is FALSE, the
function returns FALSE. Otherwise, it returns TRUE.

      Note This function performs bitwise operations on numeric inputs.

The connector pane displays the default data types for this polymorphic function.


Inputs/Outputs

   •      x —


                                                    © National Instruments 6139

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6139 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6140 ordinal=6140 -->
## Functions

Functions


           x must be a Boolean value or a number. x can be a scalar, array or cluster of numbers or Boolean
             values, array of clusters of numbers or Boolean values, and so on. If x is an error cluster, only the
             status parameter of the error cluster passes to the input terminal.

               •      y —

           y must be a Boolean value or a number. y can be a scalar, array or cluster of numbers or Boolean
             values, arrays of clusters of numbers or Boolean values, and so on. If y is an error cluster, only
            the status parameter of the error cluster passes to the input terminal.

               •      x .implies. y? —

           x .implies. y? is the logical OR of y and of the logical negation of x.


      Implies Truth Table

        x           y           x .implies. y?

       T          T          T

       T           F           F

        F          T          T

        F           F          T

     Examples

       Refer to the following example files included with LabVIEW.

            • labview\examples\Booleans\Boolean Functions.vi

      TrueTrue ConstantConstant

      Use this constant to provide a value of TRUE to the block diagram.

      You can assign a label to this constant by right-clicking the constant and selecting
        Visible Items»Label from the shortcut menu.

      You can change this value to FALSE by using the Operating tool to click the T portion of


6140   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6140 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6141 ordinal=6141 -->
## Functions

Functions

the constant or by right-clicking the constant and selecting Data Operations»Change
Value to False from the shortcut menu. You cannot change this value while the VI runs.


FalseFalse ConstantConstant

Use this constant to provide a value of FALSE to the block diagram.

You can assign a label to this constant by right-clicking the constant and selecting
Visible Items»Label from the shortcut menu.

You can change this value to TRUE by using the Operating tool to click the F portion of
the constant or by right-clicking the constant and selecting Data Operations»Change
Value to True from the shortcut menu. You cannot change this value while the VI runs.


ExpressExpress ComparisonComparison

Use the Express Comparison VI and functions to compare Boolean values, strings,
numeric values, arrays, and clusters.

The Express Comparison VI and functions treat Boolean, string, numeric, array, and
cluster values differently. You can change the comparison mode of some Express
Comparison VI and functions. You also can use the character Comparison functions to
compare characters.


 Palette
               Description
 Object

 Equal?        Returns TRUE if x is equal to y. Otherwise, this function returns FALSE. You can
 Function     change the comparison mode of this function.

                                                    © National Instruments 6141

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6141 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6142 ordinal=6142 -->
## Functions

Functions


         Palette                       Description
        Object

        Not Equal?    Returns TRUE if x is not equal to y. Otherwise, this function returns FALSE. You can
         Function     change the comparison mode of this function.

         Greater?      Returns TRUE if x is greater than y. Otherwise, this function returns FALSE. You can
         Function     change the comparison mode of this function.

         Less?         Returns TRUE if x is less than y. Otherwise, this function returns FALSE. You can
         Function     change the comparison mode of this function.

         Greater Or                      Returns TRUE if x is greater than or equal to y. Otherwise, this function returns
        Equal?                      FALSE. You can change the comparison mode of this function.         Function

         Less Or                      Returns TRUE if x is less than or equal to y. Otherwise, this function returns FALSE.
        Equal?                    You can change the comparison mode of this function.         Function

        Equal To 0?                      Returns TRUE if x is equal to 0. Otherwise, this function returns FALSE.         Function

        Not Equal To                      Returns TRUE if x is not equal to 0. Otherwise, this function returns FALSE.         0? Function

         Greater Than                      Returns TRUE if x is greater than 0. Otherwise, this function returns FALSE.         0? Function

         Less Than 0?                      Returns TRUE if x is less than 0. Otherwise, this function returns FALSE.         Function

         Greater Or                      Returns TRUE if x is greater than or equal to 0. Otherwise, this function returns        Equal To 0?
                      FALSE.         Function

         Less Or Equal
        To 0?         Returns TRUE if x is less than or equal to 0. Otherwise, this function returns FALSE.
         Function

                      Returns the value wired to the t input or f input, depending on the value of s. If s is
         Select
                    TRUE, this function returns the value wired to t. If s is FALSE, this function returns
         Function
                      the value wired to f.

                   Compares input items you specify to determine whether values are equal, greater
        Comparison
                        than, less than, and so on.


6142   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6142 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6143 ordinal=6143 -->
## Functions

Functions

Equal?Equal? FunctionFunction

Returns TRUE if x is equal to y. Otherwise, this function returns FALSE. You can change
the comparison mode of this function.

If you compare two matrices, the default comparison mode is Compare Aggregates,
and this function returns a scalar. You can compare an array or cluster of a data type to
a scalar of the same data type and produce an array or cluster of Boolean values. The
connector pane displays the default data types for this polymorphic function.


Inputs/Outputs

   •      x —

    x is a value to compare to y

   •      y —

    y must be of the same type as x.

   •      x = y? —

   When you compare arrays, x = y? is a scalar in Compare Aggregates mode and a Boolean array in
   Compare Elements mode (default).


When comparing VI Server references, this function returns TRUE when the two
references refer to the same object, regardless of whether the references have the
same capability or the same value. For example, one might be a strict reference to a
digital numeric control and the other might be a generic reference but if they refer to
the same object, they are equal. To compare the actual values of the references, use
the Type Cast function to convert the references to 32-bit signed integers. Then use the
Equal? function to compare those integers.

Similarly to the previous situation, if you have a local reference and a remote reference
to the same LabVIEW object, this function returns FALSE. However, when two
references refer to the same object but one of them is authenticated and the other is

                                                    © National Instruments 6143

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6143 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6144 ordinal=6144 -->
## Functions

Functions

       not, this function still returns TRUE.

           Note If you compare two inputs with the value not a number, NaN, or one
              input with the value NaN to an input with another value, this function always
               returns FALSE. Use the Not a Number/Path/Refnum? function to compare one
              or more inputs with a value of NaN.

     When you wire matrix data as an input to this function, a VI that includes subVIs that
      work with the matrix data type replaces the function. The resulting VI has the same
       icon but contains a matrix-specific algorithm. The node remains a VI if you disconnect
       the matrix from the input(s). Wire other data types as inputs to restore the original
       function. If you wire a data type to a function and that data type causes a basic math
       operation to fail, the function returns an empty matrix or NaN.

     Examples

       Refer to the following example files included with LabVIEW.

            • labview\examples\Comparison\Comparison Functions.vi

      NotNot Equal?Equal? FunctionFunction

       Returns TRUE if x is not equal to y. Otherwise, this function returns FALSE. You can
      change the comparison mode of this function.

           If you compare two matrices, the default comparison mode is Compare Aggregates,
      and this function returns a scalar. You can compare an array or cluster of a data type to
      a scalar of the same data type and produce an array or cluster of Booleans. The
       connector pane displays the default data types for this polymorphic function.


      Inputs/Outputs

               •      x —


6144   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6144 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6145 ordinal=6145 -->
## Functions

Functions


     xis a value to compare to y

   •      y —
    y must be of the same type as x
   •      x != y? —

    x!=y? returns the Boolean result of the operation. When you compare arrays, x!=y? is a scalar in
   Compare Aggregates mode and a Boolean array in Compare Elements mode (default).


When comparing VI Server references, this function returns FALSE when the two
references refer to the same object, regardless of whether the references have the
same capability or the same value. For example, one might be a strict reference to a
digital numeric control and the other might be a generic reference but if they refer to
the same object, they are equal. To compare the actual values of the references, use
the Type Cast function to convert the references to 32-bit signed integers. Then use the
Not Equal? function to compare those integers.

Similarly to the previous situation, if you have a local reference and a remote reference
to the same LabVIEW object, this function returns TRUE. However, when two
references refer to the same object but one of them is authenticated and the other is
not, this function still returns FALSE.

      Note If you compare two inputs with the value not a number, NaN, or one
        input with the value NaN to an input with another value, this function always
        returns TRUE. Use the Not a Number/Path/Refnum? function to compare one
        or more inputs with a value of NaN.

When you wire matrix data as an input to this function, a VI that includes subVIs that
work with the matrix data type replaces the function. The resulting VI has the same
icon but contains a matrix-specific algorithm. The node remains a VI if you disconnect
the matrix from the input(s). Wire other data types as inputs to restore the original
function. If you wire a data type to a function and that data type causes a basic math
operation to fail, the function returns an empty matrix or NaN.


                                                    © National Instruments 6145

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6145 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6146 ordinal=6146 -->
## Functions

Functions

     Examples

       Refer to the following example files included with LabVIEW.

            • labview\examples\Comparison\Comparison Functions.vi

       Greater?Greater? FunctionFunction

       Returns TRUE if x is greater than y. Otherwise, this function returns FALSE. You can
      change the comparison mode of this function.

      You can compare an array or cluster of a data type to a scalar of the same data type
      and produce an array or cluster of Boolean values. The connector pane displays the
       default data types for this polymorphic function.


      Inputs/Outputs

               •      x —

           x is a value to compare to y

               •      y —

           y must be of the same type as x

               •      x > y? —

           x > y? returns the Boolean result of the operation.

         When you compare arrays, x > y? is a scalar in Compare Aggregates mode and a Boolean array in
          Compare Elements mode (default).

      Less?Less? FunctionFunction

       Returns TRUE if x is less than y. Otherwise, this function returns FALSE. You can change
       the comparison mode of this function.


6146   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6146 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6147 ordinal=6147 -->
## Functions

Functions

You can compare an array or cluster of a data type to a scalar of the same data type
and produce an array or cluster of Boolean values. The connector pane displays the
default data types for this polymorphic function.


Inputs/Outputs

   •      x —

    x is a value to compare to y

   •      y —

    y must be of the same type as x

   •      x < y? —

    x < y? returns the Boolean result of the operation. When you compare arrays, x < y? is a scalar in
   Compare Aggregates mode and a Boolean array in Compare Elements mode (default).


GreaterGreater OrOr Equal?Equal? FunctionFunction

Returns TRUE if x is greater than or equal to y. Otherwise, this function returns FALSE.
You can change the comparison mode of this function.

You can compare an array or cluster of a data type to a scalar of the same data type
and produce an array or cluster of Boolean values. The connector pane displays the
default data types for this polymorphic function.


Inputs/Outputs

   •      x —


                                                    © National Instruments 6147

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6147 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6148 ordinal=6148 -->
## Functions

Functions


           x is a value to compare to y

               •      y —

           y must be of the same type as x

               •      x >= y? —

           x >= y? returns the Boolean result of the operation.

         When you compare arrays, x >= y? is a scalar in Compare Aggregates mode and a Boolean array
              in Compare Elements mode (default).


      LessLess OrOr Equal?Equal? FunctionFunction

       Returns TRUE if x is less than or equal to y. Otherwise, this function returns FALSE. You
      can change the comparison mode of this function.

      You can compare an array or cluster of a data type to a scalar of the same data type
      and produce an array or cluster of Boolean values. The connector pane displays the
       default data types for this polymorphic function.


      Inputs/Outputs

               •      x —

           x is a value to compare to y

               •      y —

           y must be of the same type as x

               •      x <= y? —

           x ≤ y? returns the Boolean result of the operation. When you compare arrays, x ≤ y? is a scalar in
          Compare Aggregates mode and a Boolean array in Compare Elements mode (default).


6148   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6148 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6149 ordinal=6149 -->
## Functions

Functions

EqualEqual ToTo 0?0? FunctionFunction

Returns TRUE if x is equal to 0. Otherwise, this function returns FALSE.

The connector pane displays the default data types for this polymorphic function.


Inputs/Outputs

   •      x —

    x can be a numeric scalar value, cluster, array of numbers, or a time stamp value.

   •      x = 0? —

    x = 0? is a Boolean value of the same data type structure as x.


NotNot EqualEqual ToTo 0?0? FunctionFunction

Returns TRUE if x is not equal to 0. Otherwise, this function returns FALSE.

The connector pane displays the default data types for this polymorphic function.


Inputs/Outputs

   •      x —

    x can be a numeric scalar value, cluster, array of numbers, or a time stamp value.

   •      x != 0? —

    x!= 0? is a Boolean value of the same data type structure as x.


                                                    © National Instruments 6149

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6149 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6150 ordinal=6150 -->
## Functions

Functions

      GreaterGreater ThanThan 0?0? FunctionFunction

       Returns TRUE if x is greater than 0. Otherwise, this function returns FALSE.

      The connector pane displays the default data types for this polymorphic function.


      Inputs/Outputs

               •      x —

           x can be a numeric scalar value, cluster, array of numbers, or a time stamp value.

               •      x > 0? —

           x > 0? is a Boolean value of the same data type structure as x.


      LessLess ThanThan 0?0? FunctionFunction

       Returns TRUE if x is less than 0. Otherwise, this function returns FALSE.

      The connector pane displays the default data types for this polymorphic function.


      Inputs/Outputs

               •      x —

           x can be a numeric scalar value, cluster, array of numbers, or a time stamp value.

               •      x < 0? —

           x < 0? is a Boolean value of the same data type structure as x.


6150   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6150 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6151 ordinal=6151 -->
## Functions

Functions

GreaterGreater OrOr EqualEqual ToTo 0?0? FunctionFunction

Returns TRUE if x is greater than or equal to 0. Otherwise, this function returns FALSE.

The connector pane displays the default data types for this polymorphic function.


Inputs/Outputs

   •      x —

    x can be a numeric scalar value, cluster, array of numbers, or a time stamp value.

   •      x >= 0? —

    x >= 0? is a Boolean value of the same data type structure as x.


LessLess OrOr EqualEqual ToTo 0?0? FunctionFunction

Returns TRUE if x is less than or equal to 0. Otherwise, this function returns FALSE.

The connector pane displays the default data types for this polymorphic function.


Inputs/Outputs

   •      x —

    x can be a numeric scalar value, cluster, array of numbers, or a time stamp value.

   •      x <= 0? —

    x ≤ 0? is a Boolean value of the same data type structure as x.


                                                    © National Instruments 6151

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6151 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6152 ordinal=6152 -->
## Functions

Functions

       SelectSelect FunctionFunction

       Returns the value wired to the t input or f input, depending on the value of s. If s is
      TRUE, this function returns the value wired to t. If s is FALSE, this function returns the
       value wired to f.

      The connector pane displays the default data types for this polymorphic function.


      Inputs/Outputs

               •        t —

               t is the value that this function returns if s passes a TRUE value.

               t and f must be of the same type, but they can have different numeric representations.
               •       s —

             s determines whether the function returns the value of t or f in s? t:f.

                    If you wire an error cluster to s and an error occurs, the error cluster passes a TRUE value to the
             function. Otherwise, the error cluster passes a FALSE value to the function.
               •         f —

                 f is the value that this function returns if s passes a FALSE value.

               t and f must be of the same type, but they can have different numeric representations.
               •       s? t:f —

             s? t:f is the value wired to t if s is TRUE. s? t:f is the value wired to f if s is FALSE.


      ComparisonComparison

      Compares input items you specify to determine whether values are equal, greater
       than, less than, and so on.


6152   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6152 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6153 ordinal=6153 -->
## Functions

Functions


Dialog Box Options

 Option       Description

              Contains the following options:

                        • Data points—Compares the data points of the signals in Operand 1 to the data
                  points of the signals in Operand 2, the value you specify in Value, or the
                 Constant Value to Compare Against input.
                        • Timestamps—Compares the initial time stamps (t0) of the signals in Operand 1
                   to the initial time stamps (t0) of the signals in Operand 2, the value you specify in
                   Value, or the Constant Value to Compare Against input.
                        • Time between points—Compares the time between points (dt) of the signals in
               Operand 1 to the time between points (dt) of the signals in Operand 2, the value
                you specify in Value, or the Constant Value to Compare Against input.
 Items to           • Number of data points—Compares the number of data points of the signals in
 Compare       Operand 1 to the number of data points of the signals in Operand 2, the value
                you specify in Value, or the Constant Value to Compare Against input.
                        • Signal name—Compares the signal names of the signals in Operand 1 to the
                    signal names of the signals in Operand 2, the value you specify in Value, or the
                 Constant Value to Compare Against input. When comparing signal names, you
                can use wildcards to match strings. You can use the question mark character (?)
                   to match any single character. You can use the asterisk character (*) to match any
                sequence of zero or more characters.

                             If you select Signal name, the Comparison Condition section is disabled and set
                   to = Equal.

              Contains the following options:

                        • = Equal—

                 Determines if two inputs are equal.
 Compare
                Because all comparison operations are floating-point operations, consider using
 Condition
                 Equal within tolerance for equality comparisons.

                        • <> Not equal—

                 Determines if two inputs are unequal.


                                                    © National Instruments 6153

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6153 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6154 ordinal=6154 -->
## Functions

Functions


        Option       Description

                                   • > Greater—

                        Determines if the first input is greater than the second input.

                                   • >= Greater or equal—

                        Determines if the first input is greater than or equal to the second input.

                                   • < Less—

                        Determines if the first input is less than the second input.

                                   • <= Less than or equal—

                        Determines if the first input is less than or equal to the second input.

                                   • Equal within tolerance—

                        Determines if the inputs are equal within the tolerance you specify in Tolerance.

            ◦ Tolerance—

                                 Specifies the level of tolerance to use when determining if an input is Equal
                              within tolerance. The default is 0.01.

                                   •  In range—

                        Determines if an input falls in the range Minimum and Maximum specify.

                                   • Out of range—

                        Determines if an input falls out of the range Minimum and Maximum specify.

                                   • Minimum—

                            Specifies the minimum value of the In range and Out of range comparisons. The
                          Express VI includes Minimum in the range. The default is 0.

                                   • Maximum—

                            Specifies the maximum value of the In range and Out of range comparisons. The
                          Express VI includes Maximum in the range. The default is 1.


6154   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6154 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6155 ordinal=6155 -->
## Functions

Functions


Option       Description

             Contains the following options:

                      • Second signal input—

               Compares the Operand 1 input of the Express VI to a second signal input as
               opposed to a value you specify in Value or the Constant Value to Compare
                 Against input. Select this option to include the Operand 2 input on the Express
                       VI.

                            If Operand 1 and Operand 2 are the same size, each item in Operand 1 is
               compared to the corresponding item in Operand 2. If Operand 1 and Operand 2
                 are of different sizes, all the items in Operand 1 are compared to the first item in
               Operand 2.

                      • Value—

               Compares the Operand 1 input to a constant value you specify. The default is 0. If
               you wire the Constant Value to Compare Against input, the VI uses the value
                  that this input specifies instead.

        ◦ Point value—Comparison
Inputs
                       Specifies the constant value with which to compare the Operand 1 input.
                  The default is 0.

        ◦ Timestamp value—

                       Specifies the timestamp to apply to the signal.

                      This option is available only if you place a checkmark in the Timestamp
                     checkbox.

        ◦ Delta time value—

                       Specifies the constant value with which to compare the Operand 1 input.
                  The default is 0.

        ◦ Number of points value—

                       Specifies the number of points to compare. The default is 0.

        ◦ Signal name value—


                                                    © National Instruments 6155

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6155 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6156 ordinal=6156 -->
## Functions

Functions


        Option       Description

                                 Specifies the name of the signal.

                     Contains the following options:

                                   • One result per data point—

                         Returns one result per data point. This option is available only when you select
                        Data points from the Items to Compare pull-down menu.

                                   • One result per channel—

                         Returns one result per channel. When you select Data points from the Items to
                     Compare pull-down menu, One result per channel returns 1 only if all data
                           points in the channel pass the specified comparison. If any point fails, it returns
         Result              0.

                                   • One result for all channels—

                         Returns one result for all the channels. When you select Data points from the
                        Items to Compare pull-down menu, One result for all channels returns 1 only if
                                   all data points in the channels pass the specified comparison. If any point fails, it
                           returns 0.

                                   •  Invert result—

                             Inverts the outputs.

                     Contains the following option:

                                   • Change Express VI name to name of function—
         Result
      Name          Changes the name of the Express VI on the block diagram to the name of the
                           function you select in the Comparison Condition section of the configuration
                           dialog box.


                       Displays the input signal.
        Input Signal                                   If you wire data to the Express VI and run it, Input Signal displays real data. If you
                       close and reopen the Express VI, Input Signal displays sample data until you run the


6156   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6156 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6157 ordinal=6157 -->
## Functions

Functions


 Option       Description

              Express VI again.


              Contains the following options:

 Result           If you wire data to the Express VI and run the VI, Result Preview displays real data. If
 Preview     you close and reopen the Express VI, Result Preview displays sample data until you
             run the VI again. If the cutoff frequency values are invalid, Result Preview does not
               display valid data.


Inputs/Outputs

   •       error in (no error) —

    Describes error conditions that occur before this node runs.

   •     Operand 2 —

     Specifies the second signal input for comparison. This input is available only when you select
    Second signal input in the configuration dialog box.

   •      Constant Value to Compare Against —

     Specifies the constant value with which to compare the Operand 1 input. If Constant Value to
   Compare Against is not wired, the VI uses the Value specified in the configuration dialog box.

   •     Operand 1 —

     Specifies the first input for comparison.

   •       Invert Output —

     Inverts the outputs.

   •      Result —

    Returns the resulting data based on the configuration of the Express VI.

   •       error out —


                                                    © National Instruments 6157

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6157 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6158 ordinal=6158 -->
## Functions

Functions


            Contains error information. This output provides standard error out functionality.

     BuildBuild XYXY GraphGraph

      Formats data to be displayed on an XY graph.

           Note This Express VI appears on the block diagram when you add an Express
             XY graph to the front panel. You can find the Express XY graph on the Graph
                palette.


       Dialog Box Options

        Option        Description

                        Clears the data on the graph each time the Express VI is called during execution.
         Clear data on
        each call      Regardless of the value of Clear data on each call, the Express VI clears the data on
                       the graph the first time it is called during execution.


       Inputs/Outputs

               •     X Input —

             Specifies the X input.

               •      Y Input —

             Specifies the Y input.

               •      Enable —


6158   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6158 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6159 ordinal=6159 -->
## Functions

Functions


    Enables or disables the Express VI. The default is ON or TRUE.

   •       error in (no error) —

    Describes error conditions that occur before this node runs.

   •      Reset —

    Controls the initialization of the internal state of the VI. The default is FALSE.

   •      XY Graph —

    Returns the XY graph as the output of the Express VI.

   •       error out —

    Contains error information. This output provides standard error out functionality.


Examples

Refer to the following example files included with LabVIEW.

  • labview\examples\Express VIs\Lissajous with Express
   VIs.vi

Components

Clears the data on the graph each time the Express VI is called during execution.

BuildBuild TableTable

Converts a signal or signals into a table of data that lists the amplitude of each signal
and the time data for each point in the signal.

      Note This Express VI appears on the block diagram when you add an Express
        table to the front panel. You can find the Express table on the List, Table &
       Tree palette.


                                                    © National Instruments 6159

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6159 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6160 ordinal=6160 -->
## Functions

Functions


       Dialog Box Options

        Option     Description

                    Contains the following options:

                                 • Precision—

                     Changes the digits of precision of the numbers in the table. The default is 2.

                                 • Format the numbers—

                     Changes the displayed format of the numbers in the table. Examples of each
                       format appear in parentheses after the name of the format.        Format
          for                                 • Clear data on each call—       Numeric
        Table                       Empties the table cells after each iteration.
        Data
                                 • Include time data—

                         Includes the time data for the signal in the table.

                                 • Use specified precision—

                      Formats the numbers with the precision you specify in Precision. This option is
                          available only when you select Fractional/Scientific (12.345), Fractional (12.345),
                         or Scientific (1.234E1) from the Format the numbers pull-down menu.


       Inputs/Outputs

               •       error in (no error) —

            Describes error conditions that occur before this node runs.

               •      Reset —


6160   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6160 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6161 ordinal=6161 -->
## Functions

Functions


    Controls the initialization of the internal state of the VI. The default is FALSE.

   •      Include time data —

    Includes the time data for the signal in the table. The value you wire to this input overrides the
    value you set in the configuration dialog box.

   •      Signals —

    Contains the input signal or signals.

   •      Enable —

    Enables or disables the Express VI. The default is ON or TRUE.

   •      Table —

    Displays a table formatted according to the specifications you set.

   •       error out —

    Contains error information. This output provides standard error out functionality.


Components

Changes the digits of precision of the numbers in the table. The default is 2.

Formats the numbers with the precision you specify in Precision. This option is
available only when you select Fractional/Scientific (12.345), Fractional (12.345), or
Scientific (1.234E1) from the Format the numbers pull-down menu.

Empties the table cells after each iteration.

Changes the displayed format of the numbers in the table. Examples of each format
appear in parentheses after the name of the format.

Includes the time data for the signal in the table.


                                                    © National Instruments 6161

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6161 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6162 ordinal=6162 -->
## Functions

Functions

    AddonsAddons

      Use the Addons category to access LabVIEW add-ons and to locate palettes of some
      modules or toolkits that you have installed in LabVIEW.

        After you install a module or toolkit in LabVIEW, a palette that represents that module
       or toolkit appears in a relevant category on the Functions palette. For example, the
      Database Connectivity Toolkit palette appears in the Connectivity category.

     Some module and toolkit palettes also appear in the Addons category. To view a
       palette in the Addons category, browse the Addons category on the Functions palette.

      You can determine whether a module or toolkit subpalette has multiple owning
       palettes by searching for the module or toolkit on the Functions palette. If the search
      produces multiple results, the subpalette has more than one location. The names of
       the owning palettes appear in brackets to the right of the subpalette name.

           Note (Windows) You can choose whether to activate the license of the
            module or toolkit during installation. If you choose not to activate the
            module or toolkit license, an evaluation period begins when you launch
             LabVIEW, which allows you to evaluate the software for free for a set period of
               time. If you do not activate the license before the evaluation period expires,
              the module or toolkit palette disappears from the palettes, and you can no
              longer use the module or toolkit.

        Click Find LabVIEW Add-ons in the Addons category to access LabVIEW add-ons and
       other code distributed on the LabVIEW Tools Network at ni.com/labview-tools-
       network. If the JKI VI Package Manager (VIPM) software is installed, LabVIEW launches
           it. If the VIPM software is not installed, LabVIEW launches the LabVIEW Tools Network.


         Palette
                      Description
        Object

         Find        Launch VI Package Manager to discover and install LabVIEW add-ons from the

6162   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6162 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6163 ordinal=6163 -->
## Functions

Functions


 Palette              Description
 Object

 LabVIEW            LabVIEW Tools Network. Package your own reusable code and share it with others. Add-ons...

FindFind LabVIEWLabVIEW Add-ons...Add-ons...

Launch VI Package Manager to discover and install LabVIEW add-ons from the LabVIEW
Tools Network. Package your own reusable code and share it with others.

ToolkitsToolkits

You can purchase several add-on software packages for developing specialized
applications in LabVIEW. LabVIEW add-ons include modules and toolkits that National
Instruments develops and toolkits, applications, and other code from third parties.
You can purchase the following add-on packages to extend the LabVIEW programming
environment:

  • Signal processing and analysis tools
  • Professional development tools to optimize, test, and distribute your VIs
  • Third-party connectivity tools to Microsoft Office for professional reporting,
   databases to access and store data, and embedded design tools
  • Control and simulation tools

LabVIEW Add-ons from National Instruments

If you evaluate a LabVIEW module or toolkit, at any point during the evaluation period,
you can upgrade from an evaluation version to the paid version.

LabVIEW Add-ons from Third Parties

Use the JKI VI Package Manager (VIPM) software to find, install, and manage add-ons
from third parties. Third-party LabVIEW add-ons include palettes of VIs, instrument
drivers, custom controls and indicators, and so on. Refer to the LabVIEW Tools Network
for more information about available third-party add-ons.


                                                    © National Instruments 6163

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6163 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6164 ordinal=6164 -->
## Functions

Functions

     FavoritesFavorites

      Use the Favorites category to group together items on the Functions palette that you
       access frequently. You can add items to the Favorites category using the Category
       (Standard), Category (Icons and Text), Icons, and Icons and Text formats. You then
      can organize your Favorites using the Organize Favorites dialog box.


    UserUser LibrariesLibraries

      Use the User Libraries palette to add VIs to the Functions palette. By default, the User
       Libraries palette does not contain any objects.


         Palette                     Description
        Object

         Express                   Use the Express User Libraries palette to add VIs to the Functions palette. By default,        User
                     the Express User Libraries palette does not contain any objects.          Libraries

     ExpressExpress UserUser LibrariesLibraries

      Use the Express User Libraries palette to add VIs to the Functions palette. By default,
       the Express User Libraries palette does not contain any objects.


6164   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6164 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6165 ordinal=6165 -->
## Property and Method Reference

Property and Method Reference

PropertyProperty andand MethodMethod ReferenceReference

This section describes each property and method and lists the class to which each
object belongs.

© 2005–2023 National Instruments Corporation. All rights reserved. Refer to the
<National Instruments>\_Legal Information directory for information
about NI copyright, patents, trademarks, warranties, product warnings, and export
compliance.

LabVIEWLabVIEW 3D3D GraphGraph

LabVIEWLabVIEW 3D3D GraphGraph PropertiesProperties


 Property           Description

 Graph:Projection                 Changes the projection of the 3D graph. Mode

 Graph:Background                     Specifies the background color of the plot. Color

 Graph:View                    Sets the direction to view the 3D graph. Direction

                 Speeds up the pan, zoom, and rotate operations on the 3D graph. LabVIEW
 Graph:Fast Draw   removes geometries when performing pan, zoom, or rotate to speed up the
                     rotate operations.

 Graph:3d Picture
                   Reference to the 3D graph.
 Control Reference

 Graph:X-Y Grid
                  View the 3D graph in the direction of the X-Y plane.
 Visible

 Graph:Y-Z Grid
                  View the 3D graph in the direction of the Y-Z plane.
 Visible

 Graph:X-Z Grid
                  View the 3D graph in the direction of the X-Z plane.
 Visible

 Graph:Lighting     Enables all lighting effects in the 3D scene.

                                                    © National Instruments 6165

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6165 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6166 ordinal=6166 -->
## Property and Method Reference

Property and Method Reference


        Property           Description

         Graph:Disable      Disables updates to the 3D graph. If you do not want the 3D graph to render for
        Updates          each property you write, use this property to disable updates to the 3D graph.

                           Gets or sets the active plot. After you get or set the active plot, you then can set          Plots:Active Plot                             properties or invoke methods that affect only the specified plot.

         Plots:Draw XY                             Displays the projection of the 3D graph on the X-Y plane.         Projection

         Plots:Draw YZ                             Displays the projection of the 3D graph on the Y-Z plane.         Projection

         Plots:Draw XZ                             Displays the projection of the 3D graph on the X-Z plane.         Projection

         Plots:Surface Draw Draws the 3D graph surface.

         Plots:Surface                            Sets the color of the 3D graph surface.         Color Map

         Plots:Surface       Specifies the level of opacity of the color you apply to the 3D graph surface.
         Opacity            Opacity ranges from 0 to 1 where 1 is completely opaque.

         Plots:Surface                            Applies shading to the 3D graph surface.        Shading

         Plots:Contour                            Sets the color of the 3D graph contour.         Color

         Plots:Contour Axis  Determines the axis of the contour.

         Plots:Contour
                          Enables or disables the contour on the 3D graph.       Draw

         Plots:Contour       Specifies whether the contour is anti-aliased to smooth lines and edges that
          Antialiasing       appear jagged.

         Plots:Contour
                              Specifies the width of the contour on the 3D graph object.
        Width

         Plots:Contour
                              Specifies the mode of the 3D graph contour.
       Mode

         Plots:Contour
                            Sets the number of contour lines.
         Levels

         Plots:Contour
                            Sets the amount of space between each contour line.
          Interval


6166   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6166 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6167 ordinal=6167 -->
## Property and Method Reference

Property and Method Reference


Property           Description

Plots:Contour                   Sets the value of each contour line.Level List

Plots:Contour Line                   Line style of the contour on the 3D graph.Style

Plots:Contour                  Anchors the 3D graph plot.Anchored

Plots:Contour                  Anchors the 3D graph plot to a specific point.Anchor Point

Plots:Normal                   Sets the color of the 3D graph normal.Color

Plots:Normal                     Specifies the length of the normal.
Length

Plots:Normal                     Specifies the width of the normal.
Width

Plots:Normal Draw Draws the normals of the 3D graph.

Plots:Normal       Specifies whether the normal is anti-aliased to smooth lines and edges that
Antialiasing       appear jagged.

Plots:Overlay                   Sets the color of the 3D graph overlay.Color

Plots:Overlay       Displays the overlay on the plot.

Plots:Overlay       Specifies whether the overlay is anti-aliased to smooth lines and edges that
Antialiasing       appear jagged.

Plots:Overlay
                     Specifies the size and width of the point of the overlay.
Point Size

Plots:Overlay Line
                     Specifies the width of the overlay lines on the 3D graph.
Width

Plots:Overlay
                   Sets the point style for the points on the plot overlay.
Point Style

Plots:Overlay Line
                   Sets the line style for the lines on the plot overlay.
Style

Plots:Surface
                   Applies shine to the 3D graph surface.
Shininess


                                                    © National Instruments 6167

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6167 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6168 ordinal=6168 -->
## Property and Method Reference

Property and Method Reference


        Property           Description

         Plots:Coordinate                            Configures the coordinate system of the 3D graph surface.        System

         Axes:Active Axis     Sets the axis you want to configure.

         Axes:Caption                             Displays the axis caption in the 3D graph.
          Visible

         Axes:Caption                            Sets the color of the axis caption.         Color

         Axes:Caption Font                            Sets the font size of the caption for the axis.
         Size

         Axes:Caption Text   Configures the text of the axis caption to display on the 3D graph.

         Axes:Grid Visible    Displays the axis grid in the 3D graph.

         Axes:Grid Color     Sets the color of the axis grid on the 3D graph.

         Axes:Major Tick                             Displays the major tick marks on the axis in the 3D graph.
          Visible

         Axes:Tick Color     Sets the color of the tick marks on the axis.

         Axes:Major Tick     Specifies the number of major tick marks that appear on the axis. Major Tick
        Count            Count also determines the number of grid lines and value labels.

         Axes:Minor Tick                            Sets the visibility of minor tick marks on the axis.          Visible

         Axes:Minor Tick                              Specifies the number of minor tick marks on the axis.        Count

         Axes:Label Visible   Displays the axis label in the 3D graph.

         Axes:Label Color    Sets the color of the axis label.

         Axes:Label Font
                              Specifies the font size of the label for the axes on the 3D graph.
         Size

        Axes:Range
                             Adjusts the scale automatically to reflect the data you wire to the 3D graph.
         Autoscale

        Axes:Range
                            Sets the maximum value of the scale.
       Maximum

        Axes:Range
                            Sets the minimum value of the scale.
       Minimum


6168   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6168 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6169 ordinal=6169 -->
## Property and Method Reference

Property and Method Reference


Property           Description

Axes:Label         Displays the axis label on the opposite side of the grid that the Axes:Label
Opposite Visible     Visible property displays the label.

Axes:Caption       Displays the axis caption on the opposite side of the axis that the Axes:Caption
Opposite Visible     Visible property displays the caption.

Value Pairs:X Value  Lists the index, name, and value of the value pairs you want to display on the
Pairs Data Array    3D graph.

Value Pairs:X Value                    Displays tick marks on the 3D graph for the value pairs you configure.Pairs Show Ticks

Value Pairs:X Value                    Displays grid lines for each value pair. The grid line appears on the graph at thePairs Show Grid                  corresponding value.Lines

Value Pairs:X Value                     Specifies how value pairs appear on the 3D graph.Pairs Labels

Value Pairs:Y Value  Lists the index, name, and value of the value pairs you want to display on the
Pairs Data Array    3D graph.

Value Pairs:Y Value                    Displays tick marks on the 3D graph for the value pairs you configure.Pairs Show Ticks

Value Pairs:Y Value                    Displays grid lines for each value pair. The grid line appears on the graph at thePairs Show Grid
                  corresponding value.Lines

Value Pairs:Y Value
                     Specifies how value pairs appear on the 3D graph.Pairs Labels

Value Pairs:Z Value  Lists the index, name, and value of the value pairs you want to display on the
Pairs Data Array    3D graph.

Value Pairs:Z Value
                    Displays tick marks on the 3D graph for the value pairs you configure.
Pairs Show Ticks

Value Pairs:Z Value
                    Displays grid lines for each value pair. The grid line appears on the graph at the
Pairs Show Grid
                  corresponding value.
Lines

Value Pairs:Z Value
                     Specifies how value pairs appear on the 3D graph.
Pairs Labels

Format:X Axis
                   Sets the formatting for the x-axis.
Format String


                                                    © National Instruments 6169

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6169 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6170 ordinal=6170 -->
## Property and Method Reference

Property and Method Reference


        Property           Description

        Format:Y Axis                            Sets the formatting for the y-axis.        Format String

        Format:Z Axis                            Sets the formatting for the z-axis.        Format String

         Cursors:Active                            Sets the cursor you want to configure.         Cursor

         Cursors:Cursor                             Displays the cursor in the 3D scene.          Visible

         Cursors:Cursor                          Enables you to move the cursor you configure around the 3D graph.        Enable

         Cursors:Cursor                             Displays the cursor point on the 3D graph.
         Point Visible

         Cursors:Cursor                            Sets the color of the cursor point on the 3D graph.
         Point Color

         Cursors:Cursor                              Specifies the size of the point on the cursor.
         Point Size

         Cursors:Cursor X
                             Displays the position of the cursor on the x-axis.         Position

         Cursors:Cursor Y
                             Displays the position of the cursor on the y-axis.         Position

         Cursors:Cursor Z
                             Displays the position of the cursor on the z-axis.         Position

         Cursors:Cursor                            Sets the style of the cursor lock.
        Lock Style

         Cursors:Cursor
                            Sets the plot you want to configure.
         Plot

         Cursors:Cursor
                            Sets the visibility of the cursor row.
      Row

         Cursors:Cursor
                            Sets the style of the cursor column.
       Column

         Cursors:Cursor
                             Displays the cursor line on the 3D graph.
         Line Visible

         Cursors:Cursor     Sets the color of the cursor line.

6170   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6170 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6171 ordinal=6171 -->
## Property and Method Reference

Property and Method Reference


Property           Description

Line Color

Cursors:Cursor                     Specifies the width of the cursor line on the 3D graph.Line Width

Cursors:Cursor      Specifies the level of opacity of the color you apply to the cursor plane. Opacity
Plane Opacity      ranges from 0 to 1 where 1 is completely opaque.

Cursors:Cursor                   Sets the color of the cursor plane on the 3D graph.Plane Color

Cursors:Cursor                    Displays the X-Y cursor plane on the 3D graph.
Plane XY

Cursors:Cursor                    Displays the Y-Z cursor plane on the 3D graph.Plane YZ

Cursors:Cursor                    Displays the X-Z cursor plane on the 3D graph.Plane XZ

Cursors:Cursor                     Specifies the font size of the cursor name and values on the 3D graph.Font Size

Cursors:Cursor                    Displays the cursor position on the 3D graph.Show Position

Cursors:Cursor                    Displays the cursor name on the 3D graph.Show Name

Cursors:Cursor                     Specifies the color of the cursor text on the 3D graph.Text Color

Cursors:Cursor
Text Background    Specifies the color of the cursor text background on the 3D graph.
Color

Cursors:Cursor      Specifies the level of opacity of the color you apply to the cursor text. Opacity
Text Opacity       ranges from 0 to 1 where 1 is completely opaque.

Cursors:Cursor List  Specifies the cursor list that allows the user to manually edit the cursor data.

Lights:Brightness   Sets the level of brightness of the lights in the 3D scene.

Lights:Focus        Sets the level of focus of the lights in the 3D scene.

                    Indicates the linear factor of attenuation (kl) you apply to the light. The linear
Lights:Linear
                     factor of attenuation drops in a linear manner as distance from the light
Attenuation
                     increases.


                                                    © National Instruments 6171

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6171 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6172 ordinal=6172 -->
## Property and Method Reference

Property and Method Reference


        Property           Description

                              Indicates the quadratic factor of attenuation (kq) you apply to the light. The          Lights: Quadratic                            quadratic factor of attenuation drops by the square of the distance from the         Attenuation                                   light.

          Lights:Light Array   Sets the coordinates of the lights on the 3D graph.

      Graph:ProjectionGraph:Projection ModeMode

      Changes the projection of the 3D graph.

     Remarks

      The following table lists the characteristics of this property.


        Data type

         Permissions                                                          Read/Write

         Available in Run-Time Engine                                             Yes

         Available in Real-Time Operating System                                  Yes

         Settable when the VI is running                                           Yes

        Loads the front panel into memory                                       Yes

       Need to authenticate before use                                No

        Loads the block diagram into memory                            No

     Graph:BackgroundGraph:Background ColorColor

       Specifies the background color of the plot.

     Remarks

      The following table lists the characteristics of this property.


        Data type


6172   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6172 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6173 ordinal=6173 -->
## Property and Method Reference

Property and Method Reference


 Permissions                                                          Read/Write

 Available in Run-Time Engine                                             Yes

 Available in Real-Time Operating System                                  Yes

 Settable when the VI is running                                           Yes

 Loads the front panel into memory                                       Yes

 Need to authenticate before use                                No

 Loads the block diagram into memory                            No

Graph:ViewGraph:View DirectionDirection

Sets the direction to view the 3D graph.

Remarks

The following table lists the characteristics of this property.


 Data type

 Permissions                                                          Read/Write

 Available in Run-Time Engine                                             Yes

 Available in Real-Time Operating System                                  Yes

 Settable when the VI is running                                           Yes

 Loads the front panel into memory                                       Yes

 Need to authenticate before use                                No

 Loads the block diagram into memory                            No

Graph:FastGraph:Fast DrawDraw

Speeds up the pan, zoom, and rotate operations on the 3D graph. LabVIEW removes
geometries when performing pan, zoom, or rotate to speed up the rotate operations.


                                                    © National Instruments 6173

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6173 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6174 ordinal=6174 -->
## Property and Method Reference

Property and Method Reference

     Remarks

      The following table lists the characteristics of this property.


        Data type

         Permissions                                                          Read/Write

         Available in Run-Time Engine                                             Yes

         Available in Real-Time Operating System                                  Yes

         Settable when the VI is running                                           Yes

        Loads the front panel into memory                                       Yes

       Need to authenticate before use                                No

        Loads the block diagram into memory                            No

     Graph:3dGraph:3d PicturePicture ControlControl ReferenceReference

       Reference to the 3D graph.

     Remarks

      The following table lists the characteristics of this property.


        Data type

         Permissions                                                     Read Only

         Available in Run-Time Engine                                              Yes

         Available in Real-Time Operating System                                   Yes

         Settable when the VI is running                                            Yes

        Loads the front panel into memory                                         Yes

       Need to authenticate before use                                 No

        Loads the block diagram into memory                             No


6174   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6174 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6175 ordinal=6175 -->
## Property and Method Reference

Property and Method Reference

Graph:X-YGraph:X-Y GridGrid VisibleVisible

View the 3D graph in the direction of the X-Y plane.

Remarks

The following table lists the characteristics of this property.


 Data type

 Permissions                                                          Read/Write

 Available in Run-Time Engine                                             Yes

 Available in Real-Time Operating System                                  Yes

 Settable when the VI is running                                           Yes

 Loads the front panel into memory                                       Yes

 Need to authenticate before use                                No

 Loads the block diagram into memory                            No

Graph:Y-ZGraph:Y-Z GridGrid VisibleVisible

View the 3D graph in the direction of the Y-Z plane.

Remarks

The following table lists the characteristics of this property.


 Data type

 Permissions                                                          Read/Write

 Available in Run-Time Engine                                             Yes

 Available in Real-Time Operating System                                  Yes

 Settable when the VI is running                                           Yes

 Loads the front panel into memory                                       Yes

 Need to authenticate before use                                No

                                                    © National Instruments 6175

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6175 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6176 ordinal=6176 -->
## Property and Method Reference

Property and Method Reference


        Loads the block diagram into memory                            No

     Graph:X-ZGraph:X-Z GridGrid VisibleVisible

      View the 3D graph in the direction of the X-Z plane.

     Remarks

      The following table lists the characteristics of this property.


        Data type

         Permissions                                                          Read/Write

         Available in Run-Time Engine                                             Yes

         Available in Real-Time Operating System                                  Yes

         Settable when the VI is running                                           Yes

        Loads the front panel into memory                                       Yes

       Need to authenticate before use                                No

        Loads the block diagram into memory                            No

      Graph:LightingGraph:Lighting

      Enables all lighting effects in the 3D scene.

     Remarks

      The following table lists the characteristics of this property.


        Data type

         Permissions                                                          Read/Write

         Available in Run-Time Engine                                             Yes

         Available in Real-Time Operating System                                  Yes

         Settable when the VI is running                                           Yes

6176   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6176 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6177 ordinal=6177 -->
## Property and Method Reference

Property and Method Reference


 Loads the front panel into memory                                       Yes

 Need to authenticate before use                                No

 Loads the block diagram into memory                            No

Graph:DisableGraph:Disable UpdatesUpdates

Disables updates to the 3D graph. If you do not want the 3D graph to render for each
property you write, use this property to disable updates to the 3D graph.

Remarks

The following table lists the characteristics of this property.


 Data type

 Permissions                                                          Read/Write

 Available in Run-Time Engine                                             Yes

 Available in Real-Time Operating System                                  Yes

 Settable when the VI is running                                           Yes

 Loads the front panel into memory                                       Yes

 Need to authenticate before use                                No

 Loads the block diagram into memory                            No

Plots:ActivePlots:Active PlotPlot

Gets or sets the active plot. After you get or set the active plot, you then can set
properties or invoke methods that affect only the specified plot.

Remarks

The following table lists the characteristics of this property.


 Data type


                                                    © National Instruments 6177

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6177 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6178 ordinal=6178 -->
## Property and Method Reference

Property and Method Reference


         Permissions                                                          Read/Write

         Available in Run-Time Engine                                             Yes

         Available in Real-Time Operating System                                  Yes

         Settable when the VI is running                                           Yes

        Loads the front panel into memory                                       Yes

       Need to authenticate before use                                No

        Loads the block diagram into memory                            No

      Plots:DrawPlots:Draw XYXY ProjectionProjection

       Displays the projection of the 3D graph on the X-Y plane.

     Remarks

      The following table lists the characteristics of this property.


        Data type

         Permissions                                                          Read/Write

         Available in Run-Time Engine                                             Yes

         Available in Real-Time Operating System                                  Yes

         Settable when the VI is running                                           Yes

        Loads the front panel into memory                                       Yes

       Need to authenticate before use                                No

        Loads the block diagram into memory                            No

      Plots:DrawPlots:Draw YZYZ ProjectionProjection

       Displays the projection of the 3D graph on the Y-Z plane.

     Remarks

      The following table lists the characteristics of this property.

6178   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6178 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6179 ordinal=6179 -->
## Property and Method Reference

Property and Method Reference


 Data type

 Permissions                                                          Read/Write

 Available in Run-Time Engine                                             Yes

 Available in Real-Time Operating System                                  Yes

 Settable when the VI is running                                           Yes

 Loads the front panel into memory                                       Yes

 Need to authenticate before use                                No

 Loads the block diagram into memory                            No

Plots:DrawPlots:Draw XZXZ ProjectionProjection

Displays the projection of the 3D graph on the X-Z plane.

Remarks

The following table lists the characteristics of this property.


 Data type

 Permissions                                                          Read/Write

 Available in Run-Time Engine                                             Yes

 Available in Real-Time Operating System                                  Yes

 Settable when the VI is running                                           Yes

 Loads the front panel into memory                                       Yes

 Need to authenticate before use                                No

 Loads the block diagram into memory                            No

Plots:SurfacePlots:Surface DrawDraw

Draws the 3D graph surface.


                                                    © National Instruments 6179

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6179 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6180 ordinal=6180 -->
## Property and Method Reference

Property and Method Reference

     Remarks

      The following table lists the characteristics of this property.


        Data type

         Permissions                                                          Read/Write

         Available in Run-Time Engine                                             Yes

         Available in Real-Time Operating System                                  Yes

         Settable when the VI is running                                           Yes

        Loads the front panel into memory                                       Yes

       Need to authenticate before use                                No

        Loads the block diagram into memory                            No

      Plots:SurfacePlots:Surface ColorColor MapMap

       Sets the color of the 3D graph surface.

     Remarks

      The following table lists the characteristics of this property.


        Data type

         Permissions                                                          Read/Write

         Available in Run-Time Engine                                             Yes

         Available in Real-Time Operating System                                  Yes

         Settable when the VI is running                                           Yes

        Loads the front panel into memory                                       Yes

       Need to authenticate before use                                No

        Loads the block diagram into memory                            No


6180   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6180 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6181 ordinal=6181 -->
## Property and Method Reference

Property and Method Reference

Plots:SurfacePlots:Surface OpacityOpacity

Specifies the level of opacity of the color you apply to the 3D graph surface. Opacity
ranges from 0 to 1 where 1 is completely opaque.

Remarks

The following table lists the characteristics of this property.


 Data type

 Permissions                                                          Read/Write

 Available in Run-Time Engine                                             Yes

 Available in Real-Time Operating System                                  Yes

 Settable when the VI is running                                           Yes

 Loads the front panel into memory                                       Yes

 Need to authenticate before use                                No

 Loads the block diagram into memory                            No

Plots:SurfacePlots:Surface ShadingShading

Applies shading to the 3D graph surface.

Remarks

The following table lists the characteristics of this property.


 Data type

 Permissions                                                          Read/Write

 Available in Run-Time Engine                                             Yes

 Available in Real-Time Operating System                                  Yes

 Settable when the VI is running                                           Yes

 Loads the front panel into memory                                       Yes


                                                    © National Instruments 6181

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6181 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6182 ordinal=6182 -->
## Property and Method Reference

Property and Method Reference


       Need to authenticate before use                                No

        Loads the block diagram into memory                            No

      Plots:ContourPlots:Contour ColorColor

       Sets the color of the 3D graph contour.

     Remarks

      The following table lists the characteristics of this property.


        Data type

         Permissions                                                          Read/Write

         Available in Run-Time Engine                                             Yes

         Available in Real-Time Operating System                                  Yes

         Settable when the VI is running                                           Yes

        Loads the front panel into memory                                       Yes

       Need to authenticate before use                                No

        Loads the block diagram into memory                            No

      Plots:ContourPlots:Contour AxisAxis

      Determines the axis of the contour.

     Remarks

      The following table lists the characteristics of this property.


        Data type

         Permissions                                                          Read/Write

         Available in Run-Time Engine                                             Yes

         Available in Real-Time Operating System                                  Yes

6182   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6182 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6183 ordinal=6183 -->
## Property and Method Reference

Property and Method Reference


 Settable when the VI is running                                           Yes

 Loads the front panel into memory                                       Yes

 Need to authenticate before use                                No

 Loads the block diagram into memory                            No

Plots:ContourPlots:Contour DrawDraw

Enables or disables the contour on the 3D graph.

Remarks

The following table lists the characteristics of this property.


 Data type

 Permissions                                                          Read/Write

 Available in Run-Time Engine                                             Yes

 Available in Real-Time Operating System                                  Yes

 Settable when the VI is running                                           Yes

 Loads the front panel into memory                                       Yes

 Need to authenticate before use                                No

 Loads the block diagram into memory                            No

Plots:ContourPlots:Contour AntialiasingAntialiasing

Specifies whether the contour is anti-aliased to smooth lines and edges that appear
jagged.

Remarks

The following table lists the characteristics of this property.


 Data type


                                                    © National Instruments 6183

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6183 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6184 ordinal=6184 -->
## Property and Method Reference

Property and Method Reference


         Permissions                                                          Read/Write

         Available in Run-Time Engine                                             Yes

         Available in Real-Time Operating System                                  Yes

         Settable when the VI is running                                           Yes

        Loads the front panel into memory                                       Yes

       Need to authenticate before use                                No

        Loads the block diagram into memory                            No

      Plots:ContourPlots:Contour WidthWidth

       Specifies the width of the contour on the 3D graph object.

     Remarks

      The following table lists the characteristics of this property.


        Data type

         Permissions                                                          Read/Write

         Available in Run-Time Engine                                             Yes

         Available in Real-Time Operating System                                  Yes

         Settable when the VI is running                                           Yes

        Loads the front panel into memory                                       Yes

       Need to authenticate before use                                No

        Loads the block diagram into memory                            No

      Plots:ContourPlots:Contour ModeMode

       Specifies the mode of the 3D graph contour.

     Remarks

      The following table lists the characteristics of this property.

6184   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6184 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6185 ordinal=6185 -->
## Property and Method Reference

Property and Method Reference


 Data type

 Permissions                                                          Read/Write

 Available in Run-Time Engine                                             Yes

 Available in Real-Time Operating System                                  Yes

 Settable when the VI is running                                           Yes

 Loads the front panel into memory                                       Yes

 Need to authenticate before use                                No

 Loads the block diagram into memory                            No

Plots:ContourPlots:Contour LevelsLevels

Sets the number of contour lines.

Remarks

The following table lists the characteristics of this property.


 Data type

 Permissions                                                          Read/Write

 Available in Run-Time Engine                                             Yes

 Available in Real-Time Operating System                                  Yes

 Settable when the VI is running                                           Yes

 Loads the front panel into memory                                       Yes

 Need to authenticate before use                                No

 Loads the block diagram into memory                            No

Plots:ContourPlots:Contour IntervalInterval

Sets the amount of space between each contour line.


                                                    © National Instruments 6185

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6185 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6186 ordinal=6186 -->
## Property and Method Reference

Property and Method Reference

     Remarks

      The following table lists the characteristics of this property.


        Data type

         Permissions                                                          Read/Write

         Available in Run-Time Engine                                             Yes

         Available in Real-Time Operating System                                  Yes

         Settable when the VI is running                                           Yes

        Loads the front panel into memory                                       Yes

       Need to authenticate before use                                No

        Loads the block diagram into memory                            No

      Plots:ContourPlots:Contour LevelLevel ListList

       Sets the value of each contour line.

     Remarks

      The following table lists the characteristics of this property.


        Data type

         Permissions                                                          Read/Write

         Available in Run-Time Engine                                             Yes

         Available in Real-Time Operating System                                  Yes

         Settable when the VI is running                                           Yes

        Loads the front panel into memory                                       Yes

       Need to authenticate before use                                No

        Loads the block diagram into memory                            No


6186   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6186 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6187 ordinal=6187 -->
## Property and Method Reference

Property and Method Reference

Plots:ContourPlots:Contour LineLine StyleStyle

Line style of the contour on the 3D graph.

Remarks

The following table lists the characteristics of this property.


 Data type

 Permissions                                                          Read/Write

 Available in Run-Time Engine                                             Yes

 Available in Real-Time Operating System                                  Yes

 Settable when the VI is running                                           Yes

 Loads the front panel into memory                                       Yes

 Need to authenticate before use                                No

 Loads the block diagram into memory                            No

Plots:ContourPlots:Contour AnchoredAnchored

Anchors the 3D graph plot.

Remarks

The following table lists the characteristics of this property.


 Data type

 Permissions                                                          Read/Write

 Available in Run-Time Engine                                             Yes

 Available in Real-Time Operating System                                  Yes

 Settable when the VI is running                                           Yes

 Loads the front panel into memory                                       Yes

 Need to authenticate before use                                No

                                                    © National Instruments 6187

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6187 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6188 ordinal=6188 -->
## Property and Method Reference

Property and Method Reference


        Loads the block diagram into memory                            No

      Plots:ContourPlots:Contour AnchorAnchor PointPoint

      Anchors the 3D graph plot to a specific point.

     Remarks

      The following table lists the characteristics of this property.


        Data type

         Permissions                                                          Read/Write

         Available in Run-Time Engine                                             Yes

         Available in Real-Time Operating System                                  Yes

         Settable when the VI is running                                           Yes

        Loads the front panel into memory                                       Yes

       Need to authenticate before use                                No

        Loads the block diagram into memory                            No

     Plots:NormalPlots:Normal ColorColor

       Sets the color of the 3D graph normal.

     Remarks

      The following table lists the characteristics of this property.


        Data type

         Permissions                                                          Read/Write

         Available in Run-Time Engine                                             Yes

         Available in Real-Time Operating System                                  Yes

         Settable when the VI is running                                           Yes

6188   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6188 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6189 ordinal=6189 -->
## Property and Method Reference

Property and Method Reference


 Loads the front panel into memory                                       Yes

 Need to authenticate before use                                No

 Loads the block diagram into memory                            No

Plots:NormalPlots:Normal LengthLength

Specifies the length of the normal.

Remarks

The following table lists the characteristics of this property.


 Data type

 Permissions                                                          Read/Write

 Available in Run-Time Engine                                             Yes

 Available in Real-Time Operating System                                  Yes

 Settable when the VI is running                                           Yes

 Loads the front panel into memory                                       Yes

 Need to authenticate before use                                No

 Loads the block diagram into memory                            No

Plots:NormalPlots:Normal WidthWidth

Specifies the width of the normal.

Remarks

The following table lists the characteristics of this property.


 Data type

 Permissions                                                          Read/Write

 Available in Run-Time Engine                                             Yes

                                                    © National Instruments 6189

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6189 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6190 ordinal=6190 -->
## Property and Method Reference

Property and Method Reference


         Available in Real-Time Operating System                                  Yes

         Settable when the VI is running                                           Yes

        Loads the front panel into memory                                       Yes

       Need to authenticate before use                                No

        Loads the block diagram into memory                            No

     Plots:NormalPlots:Normal DrawDraw

      Draws the normals of the 3D graph.

     Remarks

      The following table lists the characteristics of this property.


        Data type

         Permissions                                                          Read/Write

         Available in Run-Time Engine                                             Yes

         Available in Real-Time Operating System                                  Yes

         Settable when the VI is running                                           Yes

        Loads the front panel into memory                                       Yes

       Need to authenticate before use                                No

        Loads the block diagram into memory                            No

     Plots:NormalPlots:Normal AntialiasingAntialiasing

       Specifies whether the normal is anti-aliased to smooth lines and edges that appear
       jagged.

     Remarks

      The following table lists the characteristics of this property.


6190   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6190 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6191 ordinal=6191 -->
## Property and Method Reference

Property and Method Reference


 Data type

 Permissions                                                          Read/Write

 Available in Run-Time Engine                                             Yes

 Available in Real-Time Operating System                                  Yes

 Settable when the VI is running                                           Yes

 Loads the front panel into memory                                       Yes

 Need to authenticate before use                                No

 Loads the block diagram into memory                            No

Plots:OverlayPlots:Overlay ColorColor

Sets the color of the 3D graph overlay.

Remarks

The following table lists the characteristics of this property.


 Data type

 Permissions                                                          Read/Write

 Available in Run-Time Engine                                             Yes

 Available in Real-Time Operating System                                  Yes

 Settable when the VI is running                                           Yes

 Loads the front panel into memory                                       Yes

 Need to authenticate before use                                No

 Loads the block diagram into memory                            No

Plots:OverlayPlots:Overlay

Displays the overlay on the plot.


                                                    © National Instruments 6191

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6191 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6192 ordinal=6192 -->
## Property and Method Reference

Property and Method Reference

     Remarks

      The following table lists the characteristics of this property.


        Data type

         Permissions                                                          Read/Write

         Available in Run-Time Engine                                             Yes

         Available in Real-Time Operating System                                  Yes

         Settable when the VI is running                                           Yes

        Loads the front panel into memory                                       Yes

       Need to authenticate before use                                No

        Loads the block diagram into memory                            No

      Plots:OverlayPlots:Overlay AntialiasingAntialiasing

       Specifies whether the overlay is anti-aliased to smooth lines and edges that appear
       jagged.

     Remarks

      The following table lists the characteristics of this property.


        Data type

         Permissions                                                          Read/Write

         Available in Run-Time Engine                                             Yes

         Available in Real-Time Operating System                                  Yes

         Settable when the VI is running                                           Yes

        Loads the front panel into memory                                       Yes

       Need to authenticate before use                                No

        Loads the block diagram into memory                            No


6192   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6192 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6193 ordinal=6193 -->
## Property and Method Reference

Property and Method Reference

Plots:OverlayPlots:Overlay PointPoint SizeSize

Specifies the size and width of the point of the overlay.

Remarks

The following table lists the characteristics of this property.


 Data type

 Permissions                                                          Read/Write

 Available in Run-Time Engine                                             Yes

 Available in Real-Time Operating System                                  Yes

 Settable when the VI is running                                           Yes

 Loads the front panel into memory                                       Yes

 Need to authenticate before use                                No

 Loads the block diagram into memory                            No

Plots:OverlayPlots:Overlay LineLine WidthWidth

Specifies the width of the overlay lines on the 3D graph.

Remarks

The following table lists the characteristics of this property.


 Data type

 Permissions                                                          Read/Write

 Available in Run-Time Engine                                             Yes

 Available in Real-Time Operating System                                  Yes

 Settable when the VI is running                                           Yes

 Loads the front panel into memory                                       Yes

 Need to authenticate before use                                No

                                                    © National Instruments 6193

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6193 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6194 ordinal=6194 -->
## Property and Method Reference

Property and Method Reference


        Loads the block diagram into memory                            No

      Plots:OverlayPlots:Overlay PointPoint StyleStyle

       Sets the point style for the points on the plot overlay.

     Remarks

      The following table lists the characteristics of this property.


        Data type

         Permissions                                                          Read/Write

         Available in Run-Time Engine                                             Yes

         Available in Real-Time Operating System                                  Yes

         Settable when the VI is running                                           Yes

        Loads the front panel into memory                                       Yes

       Need to authenticate before use                                No

        Loads the block diagram into memory                            No

      Plots:OverlayPlots:Overlay LineLine StyleStyle

       Sets the line style for the lines on the plot overlay.

     Remarks

      The following table lists the characteristics of this property.


        Data type

         Permissions                                                          Read/Write

         Available in Run-Time Engine                                             Yes

         Available in Real-Time Operating System                                  Yes

         Settable when the VI is running                                           Yes

6194   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6194 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6195 ordinal=6195 -->
## Property and Method Reference

Property and Method Reference


 Loads the front panel into memory                                       Yes

 Need to authenticate before use                                No

 Loads the block diagram into memory                            No

Plots:SurfacePlots:Surface ShininessShininess

Applies shine to the 3D graph surface.

Remarks

The following table lists the characteristics of this property.


 Data type

 Permissions                                                          Read/Write

 Available in Run-Time Engine                                             Yes

 Available in Real-Time Operating System                                  Yes

 Settable when the VI is running                                           Yes

 Loads the front panel into memory                                       Yes

 Need to authenticate before use                                No

 Loads the block diagram into memory                            No

Plots:CoordinatePlots:Coordinate SystemSystem

Configures the coordinate system of the 3D graph surface.

Remarks

The following table lists the characteristics of this property.


 Data type

 Permissions                                                          Read/Write

 Available in Run-Time Engine                                             Yes

                                                    © National Instruments 6195

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6195 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6196 ordinal=6196 -->
## Property and Method Reference

Property and Method Reference


         Available in Real-Time Operating System                                  Yes

         Settable when the VI is running                                           Yes

        Loads the front panel into memory                                       Yes

       Need to authenticate before use                                No

        Loads the block diagram into memory                            No

      Axes:ActiveAxes:Active AxisAxis

       Sets the axis you want to configure.

     Remarks

      The following table lists the characteristics of this property.


        Data type

         Permissions                                                          Read/Write

         Available in Run-Time Engine                                             Yes

         Available in Real-Time Operating System                                  Yes

         Settable when the VI is running                                           Yes

        Loads the front panel into memory                                       Yes

       Need to authenticate before use                                No

        Loads the block diagram into memory                            No

      Axes:CaptionAxes:Caption VisibleVisible

       Displays the axis caption in the 3D graph.

     Remarks

      The following table lists the characteristics of this property.


        Data type

6196   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6196 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6197 ordinal=6197 -->
## Property and Method Reference

Property and Method Reference


 Permissions                                                          Read/Write

 Available in Run-Time Engine                                             Yes

 Available in Real-Time Operating System                                  Yes

 Settable when the VI is running                                           Yes

 Loads the front panel into memory                                       Yes

 Need to authenticate before use                                No

 Loads the block diagram into memory                            No

Axes:CaptionAxes:Caption ColorColor

Sets the color of the axis caption.

Remarks

The following table lists the characteristics of this property.


 Data type

 Permissions                                                          Read/Write

 Available in Run-Time Engine                                             Yes

 Available in Real-Time Operating System                                  Yes

 Settable when the VI is running                                           Yes

 Loads the front panel into memory                                       Yes

 Need to authenticate before use                                No

 Loads the block diagram into memory                            No

Axes:CaptionAxes:Caption FontFont SizeSize

Sets the font size of the caption for the axis.

Remarks

The following table lists the characteristics of this property.

                                                    © National Instruments 6197

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6197 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6198 ordinal=6198 -->
## Property and Method Reference

Property and Method Reference


        Data type

         Permissions                                                          Read/Write

         Available in Run-Time Engine                                             Yes

         Available in Real-Time Operating System                                  Yes

         Settable when the VI is running                                           Yes

        Loads the front panel into memory                                       Yes

       Need to authenticate before use                                No

        Loads the block diagram into memory                            No

      Axes:CaptionAxes:Caption TextText

       Configures the text of the axis caption to display on the 3D graph.

     Remarks

      The following table lists the characteristics of this property.


        Data type

         Permissions                                                          Read/Write

         Available in Run-Time Engine                                             Yes

         Available in Real-Time Operating System                                  Yes

         Settable when the VI is running                                           Yes

        Loads the front panel into memory                                       Yes

       Need to authenticate before use                                No

        Loads the block diagram into memory                            No

      Axes:GridAxes:Grid VisibleVisible

       Displays the axis grid in the 3D graph.


6198   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6198 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6199 ordinal=6199 -->
## Property and Method Reference

Property and Method Reference

Remarks

The following table lists the characteristics of this property.


 Data type

 Permissions                                                          Read/Write

 Available in Run-Time Engine                                             Yes

 Available in Real-Time Operating System                                  Yes

 Settable when the VI is running                                           Yes

 Loads the front panel into memory                                       Yes

 Need to authenticate before use                                No

 Loads the block diagram into memory                            No

Axes:GridAxes:Grid ColorColor

Sets the color of the axis grid on the 3D graph.

Remarks

The following table lists the characteristics of this property.


 Data type

 Permissions                                                          Read/Write

 Available in Run-Time Engine                                             Yes

 Available in Real-Time Operating System                                  Yes

 Settable when the VI is running                                           Yes

 Loads the front panel into memory                                       Yes

 Need to authenticate before use                                No

 Loads the block diagram into memory                            No


                                                    © National Instruments 6199

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6199 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6200 ordinal=6200 -->
## Property and Method Reference

Property and Method Reference

      Axes:MajorAxes:Major TickTick VisibleVisible

       Displays the major tick marks on the axis in the 3D graph.

     Remarks

      The following table lists the characteristics of this property.


        Data type

         Permissions                                                          Read/Write

         Available in Run-Time Engine                                             Yes

         Available in Real-Time Operating System                                  Yes

         Settable when the VI is running                                           Yes

        Loads the front panel into memory                                       Yes

       Need to authenticate before use                                No

        Loads the block diagram into memory                            No

      Axes:TickAxes:Tick ColorColor

       Sets the color of the tick marks on the axis.

     Remarks

      The following table lists the characteristics of this property.


        Data type

         Permissions                                                          Read/Write

         Available in Run-Time Engine                                             Yes

         Available in Real-Time Operating System                                  Yes

         Settable when the VI is running                                           Yes

        Loads the front panel into memory                                       Yes

       Need to authenticate before use                                No

6200   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6200 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6201 ordinal=6201 -->
## Property and Method Reference

Property and Method Reference


 Loads the block diagram into memory                            No

Axes:MajorAxes:Major TickTick CountCount

Specifies the number of major tick marks that appear on the axis. Major Tick Count
also determines the number of grid lines and value labels.

Remarks

The following table lists the characteristics of this property.


 Data type

 Permissions                                                          Read/Write

 Available in Run-Time Engine                                             Yes

 Available in Real-Time Operating System                                  Yes

 Settable when the VI is running                                           Yes

 Loads the front panel into memory                                       Yes

 Need to authenticate before use                                No

 Loads the block diagram into memory                            No

Axes:MinorAxes:Minor TickTick VisibleVisible

Sets the visibility of minor tick marks on the axis.

Remarks

The following table lists the characteristics of this property.


 Data type

 Permissions                                                          Read/Write

 Available in Run-Time Engine                                             Yes

 Available in Real-Time Operating System                                  Yes


                                                    © National Instruments 6201

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6201 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6202 ordinal=6202 -->
## Property and Method Reference

Property and Method Reference


         Settable when the VI is running                                           Yes

        Loads the front panel into memory                                       Yes

       Need to authenticate before use                                No

        Loads the block diagram into memory                            No

      Axes:MinorAxes:Minor TickTick CountCount

       Specifies the number of minor tick marks on the axis.

     Remarks

      The following table lists the characteristics of this property.


        Data type

         Permissions                                                          Read/Write

         Available in Run-Time Engine                                             Yes

         Available in Real-Time Operating System                                  Yes

         Settable when the VI is running                                           Yes

        Loads the front panel into memory                                       Yes

       Need to authenticate before use                                No

        Loads the block diagram into memory                            No

      Axes:LabelAxes:Label VisibleVisible

       Displays the axis label in the 3D graph.

     Remarks

      The following table lists the characteristics of this property.


        Data type

         Permissions                                                          Read/Write

6202   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6202 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6203 ordinal=6203 -->
## Property and Method Reference

Property and Method Reference


 Available in Run-Time Engine                                             Yes

 Available in Real-Time Operating System                                  Yes

 Settable when the VI is running                                           Yes

 Loads the front panel into memory                                       Yes

 Need to authenticate before use                                No

 Loads the block diagram into memory                            No

Axes:LabelAxes:Label ColorColor

Sets the color of the axis label.

Remarks

The following table lists the characteristics of this property.


 Data type

 Permissions                                                          Read/Write

 Available in Run-Time Engine                                             Yes

 Available in Real-Time Operating System                                  Yes

 Settable when the VI is running                                           Yes

 Loads the front panel into memory                                       Yes

 Need to authenticate before use                                No

 Loads the block diagram into memory                            No

Axes:LabelAxes:Label FontFont SizeSize

Specifies the font size of the label for the axes on the 3D graph.

Remarks

The following table lists the characteristics of this property.


                                                    © National Instruments 6203

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6203 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6204 ordinal=6204 -->
## Property and Method Reference

Property and Method Reference


        Data type

         Permissions                                                          Read/Write

         Available in Run-Time Engine                                             Yes

         Available in Real-Time Operating System                                  Yes

         Settable when the VI is running                                           Yes

        Loads the front panel into memory                                       Yes

       Need to authenticate before use                                No

        Loads the block diagram into memory                            No

     Axes:RangeAxes:Range AutoscaleAutoscale

       Adjusts the scale automatically to reflect the data you wire to the 3D graph.

     Remarks

      The following table lists the characteristics of this property.


        Data type

         Permissions                                                          Read/Write

         Available in Run-Time Engine                                             Yes

         Available in Real-Time Operating System                                  Yes

         Settable when the VI is running                                           Yes

        Loads the front panel into memory                                       Yes

       Need to authenticate before use                                No

        Loads the block diagram into memory                            No

     Axes:RangeAxes:Range MaximumMaximum

       Sets the maximum value of the scale.


6204   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6204 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6205 ordinal=6205 -->
## Property and Method Reference

Property and Method Reference

Remarks

The following table lists the characteristics of this property.


 Data type

 Permissions                                                          Read/Write

 Available in Run-Time Engine                                             Yes

 Available in Real-Time Operating System                                  Yes

 Settable when the VI is running                                           Yes

 Loads the front panel into memory                                       Yes

 Need to authenticate before use                                No

 Loads the block diagram into memory                            No

Axes:RangeAxes:Range MinimumMinimum

Sets the minimum value of the scale.

Remarks

The following table lists the characteristics of this property.


 Data type

 Permissions                                                          Read/Write

 Available in Run-Time Engine                                             Yes

 Available in Real-Time Operating System                                  Yes

 Settable when the VI is running                                           Yes

 Loads the front panel into memory                                       Yes

 Need to authenticate before use                                No

 Loads the block diagram into memory                            No


                                                    © National Instruments 6205

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6205 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6206 ordinal=6206 -->
## Property and Method Reference

Property and Method Reference

      Axes:LabelAxes:Label OppositeOpposite VisibleVisible

       Displays the axis label on the opposite side of the grid that the Axes:Label Visible
       property displays the label.

     Remarks

      The following table lists the characteristics of this property.


        Data type

         Permissions                                                          Read/Write

         Available in Run-Time Engine                                             Yes

         Available in Real-Time Operating System                                  Yes

         Settable when the VI is running                                           Yes

        Loads the front panel into memory                                       Yes

       Need to authenticate before use                                No

        Loads the block diagram into memory                            No

      Axes:CaptionAxes:Caption OppositeOpposite VisibleVisible

       Displays the axis caption on the opposite side of the axis that the Axes:Caption Visible
       property displays the caption.

     Remarks

      The following table lists the characteristics of this property.


        Data type

         Permissions                                                          Read/Write

         Available in Run-Time Engine                                             Yes

         Available in Real-Time Operating System                                  Yes

         Settable when the VI is running                                           Yes


6206   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6206 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6207 ordinal=6207 -->
## Property and Method Reference

Property and Method Reference


 Loads the front panel into memory                                       Yes

 Need to authenticate before use                                No

 Loads the block diagram into memory                            No

ValueValue Pairs:XPairs:X ValueValue PairsPairs DataData ArrayArray

Lists the index, name, and value of the value pairs you want to display on the 3D graph.

Remarks

The following table lists the characteristics of this property.


 Data type

 Permissions                                                          Read/Write

 Available in Run-Time Engine                                             Yes

 Available in Real-Time Operating System                                  Yes

 Settable when the VI is running                                           Yes

 Loads the front panel into memory                                       Yes

 Need to authenticate before use                                No

 Loads the block diagram into memory                            No

ValueValue Pairs:XPairs:X ValueValue PairsPairs ShowShow TicksTicks

Displays tick marks on the 3D graph for the value pairs you configure.

Remarks

The following table lists the characteristics of this property.


 Data type

 Permissions                                                          Read/Write

 Available in Run-Time Engine                                             Yes

                                                    © National Instruments 6207

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6207 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6208 ordinal=6208 -->
## Property and Method Reference

Property and Method Reference


         Available in Real-Time Operating System                                  Yes

         Settable when the VI is running                                           Yes

        Loads the front panel into memory                                       Yes

       Need to authenticate before use                                No

        Loads the block diagram into memory                            No

     ValueValue Pairs:XPairs:X ValueValue PairsPairs ShowShow GridGrid LinesLines

       Displays grid lines for each value pair. The grid line appears on the graph at the
       corresponding value.

     Remarks

      The following table lists the characteristics of this property.


        Data type

         Permissions                                                          Read/Write

         Available in Run-Time Engine                                             Yes

         Available in Real-Time Operating System                                  Yes

         Settable when the VI is running                                           Yes

        Loads the front panel into memory                                       Yes

       Need to authenticate before use                                No

        Loads the block diagram into memory                            No

     ValueValue Pairs:XPairs:X ValueValue PairsPairs LabelsLabels

       Specifies how value pairs appear on the 3D graph.

     Remarks

      The following table lists the characteristics of this property.


6208   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6208 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6209 ordinal=6209 -->
## Property and Method Reference

Property and Method Reference


 Data type

 Permissions                                                          Read/Write

 Available in Run-Time Engine                                             Yes

 Available in Real-Time Operating System                                  Yes

 Settable when the VI is running                                           Yes

 Loads the front panel into memory                                       Yes

 Need to authenticate before use                                No

 Loads the block diagram into memory                            No

ValueValue Pairs:YPairs:Y ValueValue PairsPairs DataData ArrayArray

Lists the index, name, and value of the value pairs you want to display on the 3D graph.

Remarks

The following table lists the characteristics of this property.


 Data type

 Permissions                                                          Read/Write

 Available in Run-Time Engine                                             Yes

 Available in Real-Time Operating System                                  Yes

 Settable when the VI is running                                           Yes

 Loads the front panel into memory                                       Yes

 Need to authenticate before use                                No

 Loads the block diagram into memory                            No

ValueValue Pairs:YPairs:Y ValueValue PairsPairs ShowShow TicksTicks

Displays tick marks on the 3D graph for the value pairs you configure.


                                                    © National Instruments 6209

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6209 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6210 ordinal=6210 -->
## Property and Method Reference

Property and Method Reference

     Remarks

      The following table lists the characteristics of this property.


        Data type

         Permissions                                                          Read/Write

         Available in Run-Time Engine                                             Yes

         Available in Real-Time Operating System                                  Yes

         Settable when the VI is running                                           Yes

        Loads the front panel into memory                                       Yes

       Need to authenticate before use                                No

        Loads the block diagram into memory                            No

     ValueValue Pairs:YPairs:Y ValueValue PairsPairs ShowShow GridGrid LinesLines

       Displays grid lines for each value pair. The grid line appears on the graph at the
       corresponding value.

     Remarks

      The following table lists the characteristics of this property.


        Data type

         Permissions                                                          Read/Write

         Available in Run-Time Engine                                             Yes

         Available in Real-Time Operating System                                  Yes

         Settable when the VI is running                                           Yes

        Loads the front panel into memory                                       Yes

       Need to authenticate before use                                No

        Loads the block diagram into memory                            No


6210   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6210 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6211 ordinal=6211 -->
## Property and Method Reference

Property and Method Reference

ValueValue Pairs:YPairs:Y ValueValue PairsPairs LabelsLabels

Specifies how value pairs appear on the 3D graph.

Remarks

The following table lists the characteristics of this property.


 Data type

 Permissions                                                          Read/Write

 Available in Run-Time Engine                                             Yes

 Available in Real-Time Operating System                                  Yes

 Settable when the VI is running                                           Yes

 Loads the front panel into memory                                       Yes

 Need to authenticate before use                                No

 Loads the block diagram into memory                            No

ValueValue Pairs:ZPairs:Z ValueValue PairsPairs DataData ArrayArray

Lists the index, name, and value of the value pairs you want to display on the 3D graph.

Remarks

The following table lists the characteristics of this property.


 Data type

 Permissions                                                          Read/Write

 Available in Run-Time Engine                                             Yes

 Available in Real-Time Operating System                                  Yes

 Settable when the VI is running                                           Yes

 Loads the front panel into memory                                       Yes

 Need to authenticate before use                                No

                                                    © National Instruments 6211

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6211 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6212 ordinal=6212 -->
## Property and Method Reference

Property and Method Reference


        Loads the block diagram into memory                            No

     ValueValue Pairs:ZPairs:Z ValueValue PairsPairs ShowShow TicksTicks

       Displays tick marks on the 3D graph for the value pairs you configure.

     Remarks

      The following table lists the characteristics of this property.


        Data type

         Permissions                                                          Read/Write

         Available in Run-Time Engine                                             Yes

         Available in Real-Time Operating System                                  Yes

         Settable when the VI is running                                           Yes

        Loads the front panel into memory                                       Yes

       Need to authenticate before use                                No

        Loads the block diagram into memory                            No

     ValueValue Pairs:ZPairs:Z ValueValue PairsPairs ShowShow GridGrid LinesLines

       Displays grid lines for each value pair. The grid line appears on the graph at the
       corresponding value.

     Remarks

      The following table lists the characteristics of this property.


        Data type

         Permissions                                                          Read/Write

         Available in Run-Time Engine                                             Yes

         Available in Real-Time Operating System                                  Yes


6212   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6212 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6213 ordinal=6213 -->
## Property and Method Reference

Property and Method Reference


 Settable when the VI is running                                           Yes

 Loads the front panel into memory                                       Yes

 Need to authenticate before use                                No

 Loads the block diagram into memory                            No

ValueValue Pairs:ZPairs:Z ValueValue PairsPairs LabelsLabels

Specifies how value pairs appear on the 3D graph.

Remarks

The following table lists the characteristics of this property.


 Data type

 Permissions                                                          Read/Write

 Available in Run-Time Engine                                             Yes

 Available in Real-Time Operating System                                  Yes

 Settable when the VI is running                                           Yes

 Loads the front panel into memory                                       Yes

 Need to authenticate before use                                No

 Loads the block diagram into memory                            No

Format:XFormat:X AxisAxis FormatFormat StringString

Sets the formatting for the x-axis.

Remarks

The following table lists the characteristics of this property.


 Data type

 Permissions                                                          Read/Write

                                                    © National Instruments 6213

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6213 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6214 ordinal=6214 -->
## Property and Method Reference

Property and Method Reference


         Available in Run-Time Engine                                             Yes

         Available in Real-Time Operating System                                  Yes

         Settable when the VI is running                                           Yes

        Loads the front panel into memory                                       Yes

       Need to authenticate before use                                No

        Loads the block diagram into memory                            No

     Format:YFormat:Y AxisAxis FormatFormat StringString

       Sets the formatting for the y-axis.

     Remarks

      The following table lists the characteristics of this property.


        Data type

         Permissions                                                          Read/Write

         Available in Run-Time Engine                                             Yes

         Available in Real-Time Operating System                                  Yes

         Settable when the VI is running                                           Yes

        Loads the front panel into memory                                       Yes

       Need to authenticate before use                                No

        Loads the block diagram into memory                            No

     Format:ZFormat:Z AxisAxis FormatFormat StringString

       Sets the formatting for the z-axis.

     Remarks

      The following table lists the characteristics of this property.


6214   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6214 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6215 ordinal=6215 -->
## Property and Method Reference

Property and Method Reference


 Data type

 Permissions                                                          Read/Write

 Available in Run-Time Engine                                             Yes

 Available in Real-Time Operating System                                  Yes

 Settable when the VI is running                                           Yes

 Loads the front panel into memory                                       Yes

 Need to authenticate before use                                No

 Loads the block diagram into memory                            No

Cursors:ActiveCursors:Active CursorCursor

Sets the cursor you want to configure.

Remarks

The following table lists the characteristics of this property.


 Data type

 Permissions                                                          Read/Write

 Available in Run-Time Engine                                             Yes

 Available in Real-Time Operating System                                  Yes

 Settable when the VI is running                                           Yes

 Loads the front panel into memory                                       Yes

 Need to authenticate before use                                No

 Loads the block diagram into memory                            No

Cursors:CursorCursors:Cursor VisibleVisible

Displays the cursor in the 3D scene.


                                                    © National Instruments 6215

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6215 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6216 ordinal=6216 -->
## Property and Method Reference

Property and Method Reference

     Remarks

      The following table lists the characteristics of this property.


        Data type

         Permissions                                                          Read/Write

         Available in Run-Time Engine                                             Yes

         Available in Real-Time Operating System                                  Yes

         Settable when the VI is running                                           Yes

        Loads the front panel into memory                                       Yes

       Need to authenticate before use                                No

        Loads the block diagram into memory                            No

      Cursors:CursorCursors:Cursor EnableEnable

      Enables you to move the cursor you configure around the 3D graph.

     Remarks

      The following table lists the characteristics of this property.


        Data type

         Permissions                                                          Read/Write

         Available in Run-Time Engine                                             Yes

         Available in Real-Time Operating System                                  Yes

         Settable when the VI is running                                           Yes

        Loads the front panel into memory                                       Yes

       Need to authenticate before use                                No

        Loads the block diagram into memory                            No


6216   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6216 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6217 ordinal=6217 -->
## Property and Method Reference

Property and Method Reference

Cursors:CursorCursors:Cursor PointPoint VisibleVisible

Displays the cursor point on the 3D graph.

Remarks

The following table lists the characteristics of this property.


 Data type

 Permissions                                                          Read/Write

 Available in Run-Time Engine                                             Yes

 Available in Real-Time Operating System                                  Yes

 Settable when the VI is running                                           Yes

 Loads the front panel into memory                                       Yes

 Need to authenticate before use                                No

 Loads the block diagram into memory                            No

Cursors:CursorCursors:Cursor PointPoint ColorColor

Sets the color of the cursor point on the 3D graph.

Remarks

The following table lists the characteristics of this property.


 Data type

 Permissions                                                          Read/Write

 Available in Run-Time Engine                                             Yes

 Available in Real-Time Operating System                                  Yes

 Settable when the VI is running                                           Yes

 Loads the front panel into memory                                       Yes

 Need to authenticate before use                                No

                                                    © National Instruments 6217

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6217 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6218 ordinal=6218 -->
## Property and Method Reference

Property and Method Reference


        Loads the block diagram into memory                            No

      Cursors:CursorCursors:Cursor PointPoint SizeSize

       Specifies the size of the point on the cursor.

     Remarks

      The following table lists the characteristics of this property.


        Data type

         Permissions                                                          Read/Write

         Available in Run-Time Engine                                             Yes

         Available in Real-Time Operating System                                  Yes

         Settable when the VI is running                                           Yes

        Loads the front panel into memory                                       Yes

       Need to authenticate before use                                No

        Loads the block diagram into memory                            No

      Cursors:CursorCursors:Cursor XX PositionPosition

       Displays the position of the cursor on the x-axis.

     Remarks

      The following table lists the characteristics of this property.


        Data type

         Permissions                                                          Read/Write

         Available in Run-Time Engine                                             Yes

         Available in Real-Time Operating System                                  Yes

         Settable when the VI is running                                           Yes

6218   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6218 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6219 ordinal=6219 -->
## Property and Method Reference

Property and Method Reference


 Loads the front panel into memory                                       Yes

 Need to authenticate before use                                No

 Loads the block diagram into memory                            No

Cursors:CursorCursors:Cursor YY PositionPosition

Displays the position of the cursor on the y-axis.

Remarks

The following table lists the characteristics of this property.


 Data type

 Permissions                                                          Read/Write

 Available in Run-Time Engine                                             Yes

 Available in Real-Time Operating System                                  Yes

 Settable when the VI is running                                           Yes

 Loads the front panel into memory                                       Yes

 Need to authenticate before use                                No

 Loads the block diagram into memory                            No

Cursors:CursorCursors:Cursor ZZ PositionPosition

Displays the position of the cursor on the z-axis.

Remarks

The following table lists the characteristics of this property.


 Data type

 Permissions                                                          Read/Write

 Available in Run-Time Engine                                             Yes

                                                    © National Instruments 6219

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6219 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6220 ordinal=6220 -->
## Property and Method Reference

Property and Method Reference


         Available in Real-Time Operating System                                  Yes

         Settable when the VI is running                                           Yes

        Loads the front panel into memory                                       Yes

       Need to authenticate before use                                No

        Loads the block diagram into memory                            No

      Cursors:CursorCursors:Cursor LockLock StyleStyle

       Sets the style of the cursor lock.

     Remarks

      The following table lists the characteristics of this property.


        Data type

         Permissions                                                          Read/Write

         Available in Run-Time Engine                                             Yes

         Available in Real-Time Operating System                                  Yes

         Settable when the VI is running                                           Yes

        Loads the front panel into memory                                       Yes

       Need to authenticate before use                                No

        Loads the block diagram into memory                            No

      Cursors:CursorCursors:Cursor PlotPlot

       Sets the plot you want to configure.

     Remarks

      The following table lists the characteristics of this property.


        Data type

6220   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6220 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6221 ordinal=6221 -->
## Property and Method Reference

Property and Method Reference


 Permissions                                                          Read/Write

 Available in Run-Time Engine                                             Yes

 Available in Real-Time Operating System                                  Yes

 Settable when the VI is running                                           Yes

 Loads the front panel into memory                                       Yes

 Need to authenticate before use                                No

 Loads the block diagram into memory                            No

Cursors:CursorCursors:Cursor RowRow

Sets the visibility of the cursor row.

Remarks

The following table lists the characteristics of this property.


 Data type

 Permissions                                                          Read/Write

 Available in Run-Time Engine                                             Yes

 Available in Real-Time Operating System                                  Yes

 Settable when the VI is running                                           Yes

 Loads the front panel into memory                                       Yes

 Need to authenticate before use                                No

 Loads the block diagram into memory                            No

Cursors:CursorCursors:Cursor ColumnColumn

Sets the style of the cursor column.

Remarks

The following table lists the characteristics of this property.

                                                    © National Instruments 6221

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6221 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6222 ordinal=6222 -->
## Property and Method Reference

Property and Method Reference


        Data type

         Permissions                                                          Read/Write

         Available in Run-Time Engine                                             Yes

         Available in Real-Time Operating System                                  Yes

         Settable when the VI is running                                           Yes

        Loads the front panel into memory                                       Yes

       Need to authenticate before use                                No

        Loads the block diagram into memory                            No

      Cursors:CursorCursors:Cursor LineLine VisibleVisible

       Displays the cursor line on the 3D graph.

     Remarks

      The following table lists the characteristics of this property.


        Data type

         Permissions                                                          Read/Write

         Available in Run-Time Engine                                             Yes

         Available in Real-Time Operating System                                  Yes

         Settable when the VI is running                                           Yes

        Loads the front panel into memory                                       Yes

       Need to authenticate before use                                No

        Loads the block diagram into memory                            No

      Cursors:CursorCursors:Cursor LineLine ColorColor

       Sets the color of the cursor line.


6222   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6222 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6223 ordinal=6223 -->
## Property and Method Reference

Property and Method Reference

Remarks

The following table lists the characteristics of this property.


 Data type

 Permissions                                                          Read/Write

 Available in Run-Time Engine                                             Yes

 Available in Real-Time Operating System                                  Yes

 Settable when the VI is running                                           Yes

 Loads the front panel into memory                                       Yes

 Need to authenticate before use                                No

 Loads the block diagram into memory                            No

Cursors:CursorCursors:Cursor LineLine WidthWidth

Specifies the width of the cursor line on the 3D graph.

Remarks

The following table lists the characteristics of this property.


 Data type

 Permissions                                                          Read/Write

 Available in Run-Time Engine                                             Yes

 Available in Real-Time Operating System                                  Yes

 Settable when the VI is running                                           Yes

 Loads the front panel into memory                                       Yes

 Need to authenticate before use                                No

 Loads the block diagram into memory                            No


                                                    © National Instruments 6223

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6223 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6224 ordinal=6224 -->
## Property and Method Reference

Property and Method Reference

      Cursors:CursorCursors:Cursor PlanePlane OpacityOpacity

       Specifies the level of opacity of the color you apply to the cursor plane. Opacity ranges
      from 0 to 1 where 1 is completely opaque.

     Remarks

      The following table lists the characteristics of this property.


        Data type

         Permissions                                                          Read/Write

         Available in Run-Time Engine                                             Yes

         Available in Real-Time Operating System                                  Yes

         Settable when the VI is running                                           Yes

        Loads the front panel into memory                                       Yes

       Need to authenticate before use                                No

        Loads the block diagram into memory                            No

      Cursors:CursorCursors:Cursor PlanePlane ColorColor

       Sets the color of the cursor plane on the 3D graph.

     Remarks

      The following table lists the characteristics of this property.


        Data type

         Permissions                                                          Read/Write

         Available in Run-Time Engine                                             Yes

         Available in Real-Time Operating System                                  Yes

         Settable when the VI is running                                           Yes

        Loads the front panel into memory                                       Yes


6224   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6224 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6225 ordinal=6225 -->
## Property and Method Reference

Property and Method Reference


 Need to authenticate before use                                No

 Loads the block diagram into memory                            No

Cursors:CursorCursors:Cursor PlanePlane XYXY

Displays the X-Y cursor plane on the 3D graph.

Remarks

The following table lists the characteristics of this property.


 Data type

 Permissions                                                          Read/Write

 Available in Run-Time Engine                                             Yes

 Available in Real-Time Operating System                                  Yes

 Settable when the VI is running                                           Yes

 Loads the front panel into memory                                       Yes

 Need to authenticate before use                                No

 Loads the block diagram into memory                            No

Cursors:CursorCursors:Cursor PlanePlane YZYZ

Displays the Y-Z cursor plane on the 3D graph.

Remarks

The following table lists the characteristics of this property.


 Data type

 Permissions                                                          Read/Write

 Available in Run-Time Engine                                             Yes

 Available in Real-Time Operating System                                  Yes

                                                    © National Instruments 6225

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6225 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6226 ordinal=6226 -->
## Property and Method Reference

Property and Method Reference


         Settable when the VI is running                                           Yes

        Loads the front panel into memory                                       Yes

       Need to authenticate before use                                No

        Loads the block diagram into memory                            No

      Cursors:CursorCursors:Cursor PlanePlane XZXZ

       Displays the X-Z cursor plane on the 3D graph.

     Remarks

      The following table lists the characteristics of this property.


        Data type

         Permissions                                                          Read/Write

         Available in Run-Time Engine                                             Yes

         Available in Real-Time Operating System                                  Yes

         Settable when the VI is running                                           Yes

        Loads the front panel into memory                                       Yes

       Need to authenticate before use                                No

        Loads the block diagram into memory                            No

      Cursors:CursorCursors:Cursor FontFont SizeSize

       Specifies the font size of the cursor name and values on the 3D graph.

     Remarks

      The following table lists the characteristics of this property.


        Data type

         Permissions                                                          Read/Write

6226   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6226 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6227 ordinal=6227 -->
## Property and Method Reference

Property and Method Reference


 Available in Run-Time Engine                                             Yes

 Available in Real-Time Operating System                                  Yes

 Settable when the VI is running                                           Yes

 Loads the front panel into memory                                       Yes

 Need to authenticate before use                                No

 Loads the block diagram into memory                            No

Cursors:CursorCursors:Cursor ShowShow PositionPosition

Displays the cursor position on the 3D graph.

Remarks

The following table lists the characteristics of this property.


 Data type

 Permissions                                                          Read/Write

 Available in Run-Time Engine                                             Yes

 Available in Real-Time Operating System                                  Yes

 Settable when the VI is running                                           Yes

 Loads the front panel into memory                                       Yes

 Need to authenticate before use                                No

 Loads the block diagram into memory                            No

Cursors:CursorCursors:Cursor ShowShow NameName

Displays the cursor name on the 3D graph.

Remarks

The following table lists the characteristics of this property.


                                                    © National Instruments 6227

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6227 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6228 ordinal=6228 -->
## Property and Method Reference

Property and Method Reference


        Data type

         Permissions                                                          Read/Write

         Available in Run-Time Engine                                             Yes

         Available in Real-Time Operating System                                  Yes

         Settable when the VI is running                                           Yes

        Loads the front panel into memory                                       Yes

       Need to authenticate before use                                No

        Loads the block diagram into memory                            No

      Cursors:CursorCursors:Cursor TextText ColorColor

       Specifies the color of the cursor text on the 3D graph.

     Remarks

      The following table lists the characteristics of this property.


        Data type

         Permissions                                                          Read/Write

         Available in Run-Time Engine                                             Yes

         Available in Real-Time Operating System                                  Yes

         Settable when the VI is running                                           Yes

        Loads the front panel into memory                                       Yes

       Need to authenticate before use                                No

        Loads the block diagram into memory                            No

      Cursors:CursorCursors:Cursor TextText BackgroundBackground ColorColor

       Specifies the color of the cursor text background on the 3D graph.


6228   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6228 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6229 ordinal=6229 -->
## Property and Method Reference

Property and Method Reference

Remarks

The following table lists the characteristics of this property.


 Data type

 Permissions                                                          Read/Write

 Available in Run-Time Engine                                             Yes

 Available in Real-Time Operating System                                  Yes

 Settable when the VI is running                                           Yes

 Loads the front panel into memory                                       Yes

 Need to authenticate before use                                No

 Loads the block diagram into memory                            No

Cursors:CursorCursors:Cursor TextText OpacityOpacity

Specifies the level of opacity of the color you apply to the cursor text. Opacity ranges
from 0 to 1 where 1 is completely opaque.

Remarks

The following table lists the characteristics of this property.


 Data type

 Permissions                                                          Read/Write

 Available in Run-Time Engine                                             Yes

 Available in Real-Time Operating System                                  Yes

 Settable when the VI is running                                           Yes

 Loads the front panel into memory                                       Yes

 Need to authenticate before use                                No

 Loads the block diagram into memory                            No


                                                    © National Instruments 6229

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6229 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6230 ordinal=6230 -->
## Property and Method Reference

Property and Method Reference

      Cursors:CursorCursors:Cursor ListList

       Specifies the cursor list that allows the user to manually edit the cursor data.

     Remarks

      The following table lists the characteristics of this property.


        Data type

         Permissions                                                          Read/Write

         Available in Run-Time Engine                                             Yes

         Available in Real-Time Operating System                                  Yes

         Settable when the VI is running                                           Yes

        Loads the front panel into memory                                       Yes

       Need to authenticate before use                                No

        Loads the block diagram into memory                            No

      Lights:BrightnessLights:Brightness

       Sets the level of brightness of the lights in the 3D scene.

     Remarks

      The following table lists the characteristics of this property.


        Data type

         Permissions                                                          Read/Write

         Available in Run-Time Engine                                             Yes

         Available in Real-Time Operating System                                  Yes

         Settable when the VI is running                                           Yes

        Loads the front panel into memory                                       Yes

       Need to authenticate before use                                No

6230   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6230 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6231 ordinal=6231 -->
## Property and Method Reference

Property and Method Reference


 Loads the block diagram into memory                            No

Lights:FocusLights:Focus

Sets the level of focus of the lights in the 3D scene.

Remarks

The following table lists the characteristics of this property.


 Data type

 Permissions                                                          Read/Write

 Available in Run-Time Engine                                             Yes

 Available in Real-Time Operating System                                  Yes

 Settable when the VI is running                                           Yes

 Loads the front panel into memory                                       Yes

 Need to authenticate before use                                No

 Loads the block diagram into memory                            No

Lights:LinearLights:Linear AttenuationAttenuation

Indicates the linear factor of attenuation (kl) you apply to the light. The linear factor of
attenuation drops in a linear manner as distance from the light increases.

Remarks

The following table lists the characteristics of this property.


 Data type

 Permissions                                                          Read/Write

 Available in Run-Time Engine                                             Yes

 Available in Real-Time Operating System                                  Yes


                                                    © National Instruments 6231

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6231 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6232 ordinal=6232 -->
## Property and Method Reference

Property and Method Reference


         Settable when the VI is running                                           Yes

        Loads the front panel into memory                                       Yes

       Need to authenticate before use                                No

        Loads the block diagram into memory                            No

      Lights:Lights: QuadraticQuadratic AttenuationAttenuation

       Indicates the quadratic factor of attenuation (kq) you apply to the light. The quadratic
        factor of attenuation drops by the square of the distance from the light.

     Remarks

      The following table lists the characteristics of this property.


        Data type

         Permissions                                                          Read/Write

         Available in Run-Time Engine                                             Yes

         Available in Real-Time Operating System                                  Yes

         Settable when the VI is running                                           Yes

        Loads the front panel into memory                                       Yes

       Need to authenticate before use                                No

        Loads the block diagram into memory                            No

      Lights:LightLights:Light ArrayArray

       Sets the coordinates of the lights on the 3D graph.

     Remarks

      The following table lists the characteristics of this property.


        Data type


6232   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6232 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6233 ordinal=6233 -->
## Property and Method Reference

Property and Method Reference


 Permissions                                                          Read/Write

 Available in Run-Time Engine                                             Yes

 Available in Real-Time Operating System                                  Yes

 Settable when the VI is running                                           Yes

 Loads the front panel into memory                                       Yes

 Need to authenticate before use                                No

 Loads the block diagram into memory                            No

ActiveXActiveX PropertiesProperties andand MethodsMethods forfor LabVIEWLabVIEW

This book describes the LabVIEW properties and methods that third-party software
can access through the ActiveX protocol.

© 2005–2023 National Instruments Corporation. All rights reserved. Refer to the
<National Instruments>\_Legal Information directory for information
about NI copyright, patents, trademarks, warranties, product warnings, and export
compliance.

ApplicationApplication PropertiesProperties andand MethodsMethods

This book contains the property and method reference information for the Application
class.

ApplicationApplication MethodsMethods (ActiveX)(ActiveX)

An Application object exports methods that affect LabVIEW.

      Note Method parameters denoted by [] are optional for that method.

Refer to the ActiveX Enumerations for more information about the enumerations used
in various methods.

In the following topics, an asterisk (*) at the end of a data type name indicates that the


                                                    © National Instruments 6233

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6233 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6234 ordinal=6234 -->
## Property and Method Reference

Property and Method Reference

      method is a pointer.

     Methods

       Method                      Description

                                     Returns an array of names and an array of paths for all methods of a
                                            class. The methods of the class are member VIs that can be called         AllMethodsOfLVClass2                                     as subVIs. In other words, global VIs, control VIs, and polymorphic
                                           VIs are excluded from the output arrays.


                            On Windows and Mac OS X, brings the application windows to the         BringToFront
                                            front.


                                  Launches the National Instruments DataSocket Browser dialog box
        BrowseDataSocket                                       to establish a connection to a DataSocket item.


         CreateLVClassInterfaceLibrary  Creates a new LabVIEW interface.


         CreateLibrary                 Creates a new LabVIEW project library.


        GetHierImgScaled            Gets the scaled image of the VI Hierarchy.


                                     Returns the version of LabVIEW that last saved the VI. This version
                                   might be different than the file format version of the VI. For
         GetVIEditorVersion           example, if you used LabVIEW 9.0.1 to save a VI, the VI has a file
                                    format version of 9.0, but this method returns 9.0.1. To obtain the
                                                     file format version of the VI, use the GetVIVersion method.


         GetVIReference               Places a VI in memory and returns the IDispatch pointer for the VI.


6234   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6234 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6235 ordinal=6235 -->
## Property and Method Reference

Property and Method Reference


Method                      Description

                            Returns the version of LabVIEW in which the VI was last saved.
                         LabVIEW does not open the VI when retrieving the versionGetVIVersion                              information. If you specify a path to a file that is not a VI, LabVIEW
                              returns error 6559.


                            Returns the path to the VI that implements the specified method
LVClassImplementingVIPath   within the specified class. If the specified class does not implement
                             the method, this method returns an ancestor VI implementation.


                            Returns the version of LabVIEW in which the LabVIEW project libraryLibraryGetFileLVVersion
                        was created.


                          Loads and compiles VIs in a directory, including VIs inMassCompile
                                subdirectories, for the specified application instance.


                             Creates a new, empty LabVIEW project. You also can use theNewProject                         LabVIEW Project Explorer window to create a new project.


OpenLibrary               Opens the LabVIEW project library.


                          Loads a LabVIEW project from disk. If the project is already in
                        memory, this method returns a reference to the existing project.
                          You can use this reference with the Project properties.OpenProject
                                In LabVIEW, you also can select File»Open Project to navigate to
                        and open a project.


                            Returns the LabVIEW file format version of the project. This version
ProjectGetFileLVVersion      might be different from the version of LabVIEW in which the project
                        was last saved.


                                                    © National Instruments 6235

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6235 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6236 ordinal=6236 -->
## Property and Method Reference

Property and Method Reference


       Method                      Description

         Quit                          Quits the application.


        _GetVIQualifiedName         Returns the qualified name of a VI without loading the VI.


      AllMethodsOfLVClass2AllMethodsOfLVClass2

       Returns an array of names and an array of paths for all methods of a class. The
      methods of the class are member VIs that can be called as subVIs. In other words,
       global VIs, control VIs, and polymorphic VIs are excluded from the output arrays.

     Syntax

     object.AllMethodsOfLVClass2(MethodNames, MethodPaths, Path,
     [Scope])
     Parameters

      Name        Type                   Description

                                              Returns an array of filenames for all methods of the class,
       MethodNames  array of strings by ref                                                 including methods of ancestor classes.

                                              Returns an array of paths to all methods of the class,
        MethodPaths   array of strings by ref                                                 including methods of ancestor classes.

                                                   Specifies the path to a .lvclass file in memory whose        Path          path
                                        methods you want to access.

                                                Controls which methods LabVIEW returns. The default is
        Scope         LibraryItemScopeEnum
                                               only the public methods.

     Return Value

       array of strings by ref


6236   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6236 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6237 ordinal=6237 -->
## Property and Method Reference

Property and Method Reference

BringToFrontBringToFront

On Windows and Mac OS X, brings the application windows to the front.

Syntax

object.BringToFront()
Return Value

none

BrowseDataSocketBrowseDataSocket

Launches the National Instruments DataSocket Browser dialog box to establish a
connection to a DataSocket item.

Syntax

object.BrowseDataSocket([prompt], [selectedURL])
Parameters

 Name      Type  Description

 prompt       String  Specifies the title of the DataSocket Browser dialog box.

                    Returns the URL of the connection specified by the user in the DataSocket selectedURL  String                  Browser dialog box.

Return Value

none

CreateLibraryCreateLibrary

Creates a new LabVIEW project library.

Syntax

object.CreateLibrary([createPalette])

                                                    © National Instruments 6237

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6237 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6238 ordinal=6238 -->
## Property and Method Reference

Property and Method Reference

     Parameters

      Name       Type     Description

                                  Specifies whether you want to set a default palette for all VIs the project         createPalette Boolean                                     library owns. The default is FALSE, which does not set a default palette.

     Return Value

       Library*

       CreateLVClassInterfaceLibraryCreateLVClassInterfaceLibrary

       Creates a new LabVIEW interface.

     Syntax

     object.CreateLVClassInterfaceLibrary()
     Return Value

      none

      GetHierImgScaledGetHierImgScaled

       Gets the scaled image of the VI Hierarchy.

     Syntax

     object.GetHierImgScaled(imgdepth, imgdata, maxwidth,
     maxheight, VIToHighlight)
     Parameters

      Name       Type       Description

                                     Indicates the color depth, or number of supported colors, of the image:
        imgdepth     long       1 (1-bit, black and white), 4 (4-bit, 16 colors), 8 (8-bit, 256 colors), or 24
                                         (24-bit, true color). The default is 8.


6238   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6238 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6239 ordinal=6239 -->
## Property and Method Reference

Property and Method Reference


Name       Type       Description

                         Information about the image so you can use the Draw Flattened Pixmap
                              VI to draw it as a picture or use the Graphics Formats VIs to save the
                      image to a file.

                                         • image type—Reserved for future use.
                                         • image depth—Specifies the color depth of the image, which is the
                        number of bits to use to describe the color of each pixel in the
                             image. Valid values include 1, 4, 8, and 24 bits per pixel. image
                          depth affects how LabVIEW interprets the values of image and
                                 colors.
                                         • image—Array of bytes that describes the color of each pixel in the
                          image in raster order. The value of image depth determines how
                          LabVIEW interprets the value of this output.

                                                If image depth is 24, each pixel has three bytes to describe its
                                   color. The first byte for each pixel describes the red value, the
                           second byte describes the green value, and the third byte describes
                             the blue value.

                                                If image depth is 8, each pixel has one byte to describe its color.imgdata      ImageData
                         The value of each bit corresponds to an element in colors, which
                                stores 32-bit RGB values where the most-significant byte is zero,
                             followed in order by red, green, and blue values.

                                                If image depth is 4, the behavior is similar to when image depth is
                      8 except valid values in image include 0 through 15.

                                                If image depth is 1, any value of zero in image corresponds to
                           element 0 in colors. All other values correspond to element 1 in
                                 colors.

                         The size of the array might be larger than expected due to padding.

                                         • mask—Array of bytes in which each bit describes mask information
                                  for a pixel. The first byte describes the first eight pixels, the second
                             byte describes the next eight pixels, and so on. If a bit is zero,
                          LabVIEW draws the corresponding pixel as transparent. If the array
                                        is empty, LabVIEW draws all pixels without transparency. If the
                               array does not contain a bit for each pixel in the image, LabVIEW
                           draws any pixels missing from the array without transparency.


                                                    © National Instruments 6239

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6239 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6240 ordinal=6240 -->
## Property and Method Reference

Property and Method Reference


      Name       Type       Description

                                                      • colors—Array of RGB color values that correspond to the values in
                                    image. The value of image depth determines how LabVIEW
                                          interprets the value of this output. If image depth is 24, LabVIEW
                                       ignores this output. If image depth is 8, the array has 256
                                      elements. If image depth is 4, the array has 16 elements. If image
                                  depth is 1, the array has 2 elements.
                                                      • Rectangle—Cluster that contains coordinates that describe the
                                  bounding rectangle of the image, where the upper-left corner is at
                                                 (0,0). The bottom right edges of the bounds does not include the
                                     image.

                                     Specifies the width of the returned image. If this input is 0, the width of
                                  the returned image is the same size as the default image when it is
                                  displayed in the VI Hierarchy window in LabVIEW. Also, LabVIEW cannot
       maxwidth     long                                       distort the returned image if the specifiedMaximum Width and
                         Maximum Height parameters do not retain the same ratio as the
                                    default image.

                                     Specifies the height of the returned image. If this input is 0, the height
                                     of the returned image is the same size as the default image when it is
                                  displayed in the VI Hierarchy window in LabVIEW. Also, LabVIEW cannot
        maxheight    long                                       distort the returned image if the specifiedMaximum Width and
                         Maximum Height parameters do not retain the same ratio as the
                                    default image.

                                     Specifies the VI to highlight within the hierarchy image. In addition to
         VIToHighlight  variant     placing a purple border around the specified VI, LabVIEW expands or
                                    collapses the hierarchy to focus on the VI.

     Return Value

      none

       GetVIEditorVersionGetVIEditorVersion

       Returns the version of LabVIEW that last saved the VI.

       This version might be different than the file format version of the VI. For example, if
      you used LabVIEW 9.0.1 to save a VI, the VI has a file format version of 9.0, but this

6240   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6240 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6241 ordinal=6241 -->
## Property and Method Reference

Property and Method Reference

method returns 9.0.1. To obtain the file format version of the VI, use the GetVIVersion
method.

LabVIEW does not open the VI when retrieving the version information. If you specify a
path to a file that is not a VI, LabVIEW returns error 6559.

Syntax

object.GetVIEditorVersion(VI Path, [Version Number])
Parameters

 Name           Type           Description

 VI Path           path           Path to the VI whose version you want to get.

 Version Number   unsigned long   Version number of LabVIEW in which the VI was last saved.

Return Value

String

_GetVIQualifiedName_GetVIQualifiedName

Returns the qualified name of a VI without loading the VI.

Syntax

object._GetVIQualifiedName(VIPath, VIQualifiedName)
Parameters

 Name                        Type         Description

 VIPath                          path        Path to the VI.

 VIQualifiedName                    string        Qualified name of the VI.

Return Value

none

                                                    © National Instruments 6241

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6241 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6242 ordinal=6242 -->
## Property and Method Reference

Property and Method Reference

      GetVIReferenceGetVIReference

       Places a VI in memory and returns the IDispatch pointer for the VI.

     Syntax

     object.GetVIReference(viPath, [password], [resvForCall],
     [options])
     Parameters

      Name     Type     Description

         viPath       String    Absolute path to the VI placed in memory.

                                                  If the VI is password-protected, you must enter the password to make any        password   String
                                    edits.

                                                  If TRUE, the VI is set to an execution state called reserved. You cannot edit a
                              reserved VI because the VI can be called as a subVI at any time while its
                              parent VI runs. Setting the VI to reserved at the time of the reference speeds
                         up calls to the VI. However, this state does not support any of the edit mode
                                properties or methods. To bring the VI out of the reserved execution state,         resvForCall Boolean
                                close this reference and open a new reference by setting resvForCall to
                              FALSE.

                                                  If you are working with a reentrant VI, it is important to set this parameter
                                to TRUE so that LabVIEW can call the VI efficiently.


                         A bit set that specifies how the VI reference is treated. options can be a
                             combination of the following values. The default is 0x10.

                                  Record modifications. An asterisk (*) appears by the VI title to
                             0x01  indicate that changes have been made using VI Server. The VI must                   unsigned
         options                  be in edit mode for LabVIEW to record the modifications.                    long
                              Open templates for editing. This option opens the original .vit
                                                       file. If you do not select this option, LabVIEW opens a new instance
                             0x02
                                        of the template VI. Edits made to an instance do not affect the
                                          original .vit file. This option has no effect on non-template files.


6242   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6242 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6243 ordinal=6243 -->
## Property and Method Reference

Property and Method Reference


 Name     Type     Description


                         Prompt user to save changes when this VI reference closes if all the
                               following conditions are true:

                                              • The referenced VI or its subVIs contain unsaved changes.
                                              • There are no other open references to the referenced VI.                      0x04
                                              • The referenced VI is able to leave memory. A VI is able to leave
                            memory, for example, if no other VIs call the VI, the front panel
                                    of the VI is closed, and the VI is not a member of an open
                                    project library, and so on.

                            Prepare for reentrant run. Reserves the target VI so it cannot be
                              edited and if the target VI is reentrant, allocates a dedicated parallel
                            data space for this VI reference. If the target VI is not reentrant, this
                        method returns an error. When you release the VI reference,
                          LabVIEW unreserves the reentrant target VI and deallocates a
                                  parallel data space. Use this option with the Run method to run                      0x08                              multiple instances of a reentrant VI simultaneously. If you target a
                              reentrant VI and do not use this option, this method returns a
                              reference to the VI without allocating a parallel data space for the VI
                                reference. When you do not use this option, multiple calls to this
                        method for a reentrant VI return references to the same VI with the
                        same data space, and this method does not clone the VI.

                      0x10 Prompt user to find missing subVIs of the referenced VI.

                       Do not display the loading dialog box when searching for missing
                             subVIs of the referenced VI.
                      0x20
                            Note This option does not affect whether LabVIEW
                                  prompts you to find the missing VIs or not.


Return Value

VirtualInstrument*


                                                    © National Instruments 6243

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6243 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6244 ordinal=6244 -->
## Property and Method Reference

Property and Method Reference

      GetVIVersionGetVIVersion

       Returns the version of LabVIEW in which the VI was last saved. LabVIEW does not open
       the VI when retrieving the version information. If you specify a path to a file that is not
      a VI, LabVIEW returns error 6559.

     Syntax

     object.GetVIVersion(VIPath, versNum)
     Parameters

      Name     Type             Description

         VIPath      String           Path to the VI whose version you want to get.

       versNum   unsigned long    Returns the version number of the VI specified in viPath.

     Return Value

       String

       LibraryGetFileLVVersionLibraryGetFileLVVersion

       Returns the version of LabVIEW in which the LabVIEW project library was created.

     Syntax

     object.LibraryGetFileLVVersion(libPath, [versNum])
     Parameters

      Name            Type         Description

         libPath            path          Specifies the path to the library.

       versNum          Long*        Returns the version number.

     Return Value

       String

6244   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6244 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6245 ordinal=6245 -->
## Property and Method Reference

Property and Method Reference

LVClassImplementingVIPathLVClassImplementingVIPath

Returns the path to the VI that implements the specified method within the specified
class. If the specified class does not implement the method, this method returns an
ancestor VI implementation.

Syntax

object.LVClassImplementingVIPath(PathToVI, ClassPath,
MethodName, Scope)
Parameters

 Name       Type                   Description

                                    Path to the VI that implements the method specified by PathToVI      path
                                      the Path To Class and Method Name inputs.

                                          Specifies the path to the class in which you are searching ClassPath     path
                                            for Method Name.

                                          Specifies the filename of the method for which you want MethodName  string
                                        to know the implementing VI.

 Scope        LibraryItemScopeEnum Returns the access scope of the returned VI.

Return Value

path

MassCompileMassCompile

Loads and compiles VIs in a directory, including VIs in subdirectories, for the specified
application instance.

This method is similar to the Mass Compile option in the Mass Compile dialog box.

Syntax

object.MassCompile(directory, [logFile], [appendLog],
[viCacheSize], [reloadLVSBs], [User Stopped])


                                                    © National Instruments 6245

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6245 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6246 ordinal=6246 -->
## Property and Method Reference

Property and Method Reference

     Parameters

      Name      Type     Description

         directory     String    Directory where the mass compile begins.

                                     File path where the results of the mass compile are placed. The default is          logFile       String                          no log file.

       appendLog  Boolean  Indicates whether results are appended to the log file. The default is FALSE.

                        Number of VIs allowed to be in memory during the mass compile. The         viCacheSize  Long                                 default is none.

                                                  If TRUE, ignores CINs in VIs and the application searches for them. Use this
        reloadLVSBs Boolean parameter when a large number of CINs have been recompiled and need to
                          be reloaded. The default is FALSE.

        User                    Boolean  Indicates whether the user stopped the mass compile operation.        Stopped

     Return Value

      none

      NewProjectNewProject

       Creates a new, empty LabVIEW project. You also can use the LabVIEW Project Explorer
      window to create a new project.

     Syntax

     object.NewProject()
     Return Value

       Project*

      OpenLibraryOpenLibrary

      Opens the LabVIEW project library.


6246   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6246 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6247 ordinal=6247 -->
## Property and Method Reference

Property and Method Reference

Syntax

object.OpenLibrary(path)
Parameters

 Name     Type      Description

 path       String      Specifies the path to the project library to open.

Return Value

Library*

OpenProjectOpenProject

Loads a LabVIEW project from disk. If the project is already in memory, this method
returns a reference to the existing project. You can use this reference with the Project
properties.

In LabVIEW, you also can select File»Open Project to navigate to and open a project.

Syntax

object.OpenProject(path)
Parameters

 Name            Type               Description

 path                 String              Path to the project.

Return Value

Project*

ProjectGetFileLVVersionProjectGetFileLVVersion

Returns the LabVIEW file format version of the project. This version might be different
from the version of LabVIEW in which the project was last saved.

                                                    © National Instruments 6247

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6247 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6248 ordinal=6248 -->
## Property and Method Reference

Property and Method Reference

     Syntax

     object.ProjectGetFileLVVersion(Project Path, [Version
     Number])
     Parameters

      Name                Type                 Description

         Project Path            path                   Specifies the path to the project.

         Version Number         unsigned long        Returns the version number.

     Return Value

        string

      QuitQuit

       Quits the application.

     Syntax

     object.Quit()
     Return Value

      none

      ApplicationApplication PropertiesProperties (ActiveX)(ActiveX)

      An Application object exports properties that affect LabVIEW.

       Refer to the ActiveX Enumerations for more information about the enumerations used
        in various properties.


6248   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6248 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6249 ordinal=6249 -->
## Property and Method Reference

Property and Method Reference

Properties

 Property                             Description

                                     Returns an array of references to each LabVIEW project in
 AllProjects                       memory. You can use these references with the Project
                                         properties.


                                     Returns a list of VIs in memory for the calling VI application
                                         instance. This property returns an error if you use it to
 AllVIsInMemory                       return a list of remote VIs. Use the ExportedVIs property to
                                       return a list of exported VIs. This property is read only. This
                                     property is available only in the local versions of LabVIEW.


                                        Indicates the LabVIEW instance the VI is running in, AppKind                                       including invalid application types.


 AppName                          Filename of the application. This property is read only.


                                        Indicates the target CPU of an application. This property is AppTargetCPU                                    read only.


                                        Indicates the operating system for which the application
 AppTargetOS                     was built. Mac OS refers to Mac OS versions 9 and 8. Carbon
                                           refers to Mac OS X. This property is read only.


                                     Absolute path to the directory where the application is
 ApplicationDirectory
                                         located. This property is read only.


                                         Specifies whether the application closes when all the
 AutomaticClose
                                       references to it are released. The default is TRUE.


                                                    © National Instruments 6249

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6249 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6250 ordinal=6250 -->
## Property and Method Reference

Property and Method Reference


        Property                             Description

                                            Returns an array of user-defined command-line arguments
       CmdArgs                                          passed when LabVIEW launched.


         DefaultDataLocation                 Path to the LabVIEW Data directory.


                                            Returns a list of exported VIs in memory. This property is         ExportedVIs                                            read only.


                                                 Indicates the language of the LabVIEW environment or
        Language                            stand-alone application as a string according to ISO 639.
                                              Values include en, de, fr, ja, ko, and zh-cn.


                                               Build number of the actual operating system. This string
                                                returns an alphanumeric value of the build number that       OSBuildNumber                                        you can use to compare the build version of operating
                                              systems. This property is read only.


                                               Detailed name of the operating system where the
                                                application is actually running. This string value returns the
                                              operating system and its version, such as Microsoft
        OSDetailedName                 Windows XP. This property is similar to a combination of
                                  OSName and OSVersion, which return the platform name
                                      and a numeric version number respectively. This property
                                                              is read only.


                                 Name of the operating system where the application is
                                                  actually running. This string value is the same as
                                            AppTargetOS, except among versions of
      OSName                             Windows—specifically, AppTargetOS has one enumeration
                                      on Windows XP while OSName returns the exact version of
                                      Windows your application is running on. This property is
                                            read only.


6250   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6250 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6251 ordinal=6251 -->
## Property and Method Reference

Property and Method Reference


Property                             Description

                                      Version number of the actual operating system. This
OSVersion                                     property is read only.


PrintDefaultPrinter                   Gets or sets the name of the default printer in LabVIEW.


PrintMethod                         Gets or sets how LabVIEW prints.


                                        Specifies whether to print the hidden contents of iconified
                                         cluster constants that might be present on the blockPrintSetupCustomClusterConstants
                                  diagram when using the custom format with one of the
                                         print documentation VI methods.


                                        Specifies whether to print the connector pane and icon of
PrintSetupCustomConnector            VIs when using the custom format with one of the print
                                  documentation VI methods.


                                        Specifies whether to print descriptions of front panel
PrintSetupCustomControlDesc         controls when using the custom format with one of the
                                         print documentation VI methods.


                                        Specifies whether to print data type information for
PrintSetupCustomControlTypes       LabVIEW front panel controls when using the custom
                                   format with one of the print documentation VI methods.


                                        Specifies whether to print LabVIEW front panel control
                                     information when using the custom format with one of the
PrintSetupCustomControls             print documentation VI methods. This property does not
                                           affect the image of the front panel, just the list of controls
                               and indicators in the generated documentation.


                                                    © National Instruments 6251

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6251 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6252 ordinal=6252 -->
## Property and Method Reference

Property and Method Reference


        Property                             Description

                                                  Specifies whether to print VI descriptions when using the
        PrintSetupCustomDescription        custom format with one of the print documentation VI
                                          methods.


                                                  Specifies whether to print LabVIEW block diagrams when
        PrintSetupCustomDiagram            using the custom format with one of the print
                                         documentation VI methods.


                                                  Specifies whether to print the hidden frames in LabVIEW
                                         Case and Stacked Sequence structures that might be        PrintSetupCustomDiagramHidden
                                             present on the block diagram when using the custom
                                            format with one of the print documentation VI methods.


                                                  Specifies whether to print visible subdiagrams of each
                                              Case, Event, and Stacked Sequence structure in sequence
                                             with the non-visible subdiagrams when using the custom        PrintSetupCustomDiagramRepeat                                            format with one of the print documentation VI methods. If
                                        you print the visible frames in sequence, those frames will
                                                   print twice.


                                                  Specifies whether to print the configuration information for
                                         any LabVIEW Express VIs on the block diagram when using         PrintSetupCustomExpressVIConfigInfo
                                             the custom format with one of the print documentation VI
                                          methods.


                                                  Specifies whether to print the hierarchy of the VI in
        PrintSetupCustomHierarchy        memory when using the custom format with one of the
                                                   print documentation VI methods.


                                                  Specifies whether to print the VI revision history
        PrintSetupCustomHistory             information when using the custom format with one of the
                                                   print documentation VI methods.


6252   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6252 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6253 ordinal=6253 -->
## Property and Method Reference

Property and Method Reference


Property                             Description

                                        Specifies whether to print the label and/or caption for each
PrintSetupCustomLabel                control when using the custom format with one of the print
                                  documentation VI methods.


                                        Specifies whether to print the LabVIEW front panel when
PrintSetupCustomPanel               using the custom format with one of the print
                                  documentation VI methods.


                                        Specifies whether to print the LabVIEW front panel with a
PrintSetupCustomPanelBorder        border when using the custom format with one of the print
                                  documentation VI methods.


                                        Specifies whether to print a list of the LabVIEW subVIs and
                                     Express VIs including the icon, name, and path when using
                                    the custom format with one of the print documentation VI
                                  methods. If a polymorphic VI is a subVI, LabVIEW prints thePrintSetupCustomSubVIs                                      instance used in the top-level VI including the icon, name,
                               and path. If the top-level VI is polymorphic, LabVIEW prints
                                 a list of all the instances of the polymorphic VI including
                                    the icon, name, and path of each instance.


                            Maximum number of characters on a single line in a file.
                                          Affects the PrintVIToHTML, PrintVIToRTF, and PrintVIToText
PrintSetupFileWrapText
                                  methods. Set this property to 0 to print all the characters
                               on one line so the text does not wrap.


                                    Percentage value from 0 to 100 specifying the level of
                                        quality you want for the JPEG graphic in VIs printed either
                                          interactively or with the PrintVIToHTML method. The scale
PrintSetupJPEGQuality               balances image quality and file size. A value in the 75-95
                                   range produces a compressed file with a high-quality
                                    image, and a value below 50 produces a smaller file size
                                    with a low-quality image. The default is 80.


                                                    © National Instruments 6253

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6253 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6254 ordinal=6254 -->
## Property and Method Reference

Property and Method Reference


        Property                             Description

                                    Number between –1 and 9 that specifies the level of
                                          compression you want for the PNG file for graphics in VIs
                                               printed either interactively or with the PrintVIToHTML
                                         method. The quality of the graphic is not affected by the
                                            compression, but the graphic file size and speed of
                                          compression are affected by this value. Valid values range        PrintSetupPNGCompressLevel                                         from –1 to 9 and balance file compression with speed. 0
                                              designates no compression. 1 designates the best speed
                                             with some compression. 9 designates the best
                                            compression, but slower speed. –1 (the default value)
                                              designates the best combination of good compression and
                                             speed.


                                            Returns an alphabetized array of printer names available         PrintersAvailable                                      on the computer.


                                                                          If TRUE, LabVIEW sends color/grayscale output to the
         PrintingColorDepth                      printer. If FALSE, LabVIEW sends monochrome output to
                                             the printer.


                                                                          If you are not targeted to a real-time (RT) platform, this
                                             property is always TRUE. If you are targeted to an RT-
                                             platform and the host is connected, this property is TRUE.
                                   When this property is FALSE, the host is not connected,        RTHostConnected
                                                requiring that the Real-Time Module application must be
                                              able to handle all operations independent of the host. Use
                                                     this property to determine when it is safe to display a
                                               dialog box that requires user interaction.


                                       The version number of the LabVIEW file format to which
                                        LabVIEW documents are saved by the application. This
        SaveVersion                           version number might be different than the version
                                     number of the application. For example, a LabVIEW with
                                               version number 9.0.1 will save LabVIEW documents with a


6254   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6254 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6255 ordinal=6255 -->
## Property and Method Reference

Property and Method Reference


Property                             Description

                                                    file format version of 9.0.


                               An array of the LabVIEW versions to which this version of
                                LabVIEW can save. The array is in reverse chronological
                                        order, with the element at position zero in the array beingSaveVersions                                    the current version of LabVIEW. Each element of the array
                                                  is a valid version to pass to VI server functions which save
                                      to previous versions.


                                       Writing the property: Setting this property to TRUE enables
                                    the display of tip strips on LabVIEW front panel controls.
ShowFPTipStrips                      Setting the property to FALSE prevents them from being
                                       displayed. Reading the property: Specifies whether tip
                                           strips display when idling over controls on the front panel.


                                   User name used to open the application. This property isUserName                                   read only.


                                    Gets or sets the LabVIEW VI server port. LabVIEW returns an
VIServerPort                            error if you attempt to access this property on a remote
                                        application.


                                      Version number of the application. In a stand-alone
                                       application or shared library, this property returns the
Version
                                      version of the LabVIEW Run-Time Engine. This property is
                                   read only.


                                      Version year of the application. In a built application or
VersionYear                         shared library, this property returns the version year of the
                                LabVIEW Run-Time Engine.


                                                    © National Instruments 6255

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6255 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6256 ordinal=6256 -->
## Property and Method Reference

Property and Method Reference

       AllProjectsAllProjects

       Returns an array of references to each LabVIEW project in memory. You can use these
       references with the Project properties.

     Syntax

     object.AllProjects
     Data Type

       Array of projects

      AllVIsInMemoryAllVIsInMemory

       Returns a list of VIs in memory for the calling VI application instance. This property
       returns an error if you use it to return a list of remote VIs. Use the ExportedVIs property
       to return a list of exported VIs. This property is read only. This property is available
       only in the local versions of LabVIEW.

           Note If you have multiple application instances open simultaneously, be
              sure to wire an application reference to the reference input. For example,
            LabVIEW opens a new application instance each time you create a LabVIEW
               project or a target for a LabVIEW project.

     Syntax

     object.AllVIsInMemory
     Data Type

       Array of strings

      AppKindAppKind

       Indicates the LabVIEW instance the VI is running in, including invalid application types.

         1. Development System, including the Base Development System, Full Development
          System, or Professional Development System

6256   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6256 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6257 ordinal=6257 -->
## Property and Method Reference

Property and Method Reference

 2. Run-Time System
 3. Student Edition
 4. Embedded LabVIEW, including LabVIEW Real-Time
 5. Evaluation
 6. Custom

Syntax

object.AppKind
Data Type

AppKindEnum

ApplicationDirectoryApplicationDirectory

Absolute path to the directory where the application is located. This property is read
only.

Syntax

object.ApplicationDirectory
Data Type

String

AppNameAppName

Filename of the application. This property is read only.

Syntax

object.AppName
Data Type

String


                                                    © National Instruments 6257

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6257 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6258 ordinal=6258 -->
## Property and Method Reference

Property and Method Reference

      AppTargetCPUAppTargetCPU

       Indicates the target CPU of an application. This property is read only.

     Syntax

     object.AppTargetCPU
     Data Type

      AppTargCPUEnum

      AppTargetOSAppTargetOS

       Indicates the operating system for which the application was built. Mac OS refers to
     Mac OS versions 9 and 8. Carbon refers to Mac OS X. This property is read only.

     Syntax

     object.AppTargetOS
     Data Type

      AppTargOSEnum

      AutomaticCloseAutomaticClose

       Specifies whether the application closes when all the references to it are released. The
       default is TRUE.

     Syntax

     object.AutomaticClose
     Data Type

      Boolean


6258   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6258 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6259 ordinal=6259 -->
## Property and Method Reference

Property and Method Reference

CmdArgsCmdArgs

Returns an array of user-defined command-line arguments passed when LabVIEW
launched.

User-defined arguments start after two hyphens (--) surrounded by spaces in the
command line. The first string in the array is the name of the executable launched. This
property does not return the name of the VI launched or the LLB that contains the VI. If
a user-defined command-line argument contains double quotation marks ("), this
property returns the argument without the quotation marks.

If you use this property in a stand-alone application, you can pass all arguments as
user-defined arguments so you do not need to enter the two hyphens before user-
defined arguments in the command line.

This property is similar to the Pass all command line arguments to application option
on the Advanced page of the LabVIEW Application Properties dialog box.

Syntax

object.CmdArgs
Data Type

Array of strings

DefaultDataLocationDefaultDataLocation

Path to the LabVIEW Data directory.

You can use this directory to store the data files LabVIEW generates, such as .lvm or
.txt files. When you install LabVIEW, the installer creates a LabVIEW Data
subdirectory in the default file directory for the operating system to help you organize
and locate the data files LabVIEW generates.

Syntax

object.DefaultDataLocation


                                                    © National Instruments 6259

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6259 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6260 ordinal=6260 -->
## Property and Method Reference

Property and Method Reference

     Data Type

       String

      ExportedVIsExportedVIs

       Returns a list of exported VIs in memory. This property is read only.

     Syntax

     object.ExportedVIs
     Data Type

       Array of strings

      LanguageLanguage

       Indicates the language of the LabVIEW environment or stand-alone application as a
        string according to ISO 639. Values include en, de, fr, ja, ko, and zh-cn.

     Syntax

     object.Language
     Data Type

       String

     OSBuildNumberOSBuildNumber

       Build number of the actual operating system. This string returns an alphanumeric
       value of the build number that you can use to compare the build version of operating
       systems. This property is read only.

           Note A newer version of an operating system often returns a larger
             alphanumeric value.


6260   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6260 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6261 ordinal=6261 -->
## Property and Method Reference

Property and Method Reference

Syntax

object.OSBuildNumber
Data Type

string

OSDetailedNameOSDetailedName

Detailed name of the operating system where the application is actually running.

This string value returns the operating system and its version, such as Microsoft
Windows XP. This property is similar to a combination of OSName and OSVersion,
which return the platform name and a numeric version number respectively. This
property is read only.

Service pack installations or other changes to the operating system might affect this
string value.
Syntax

object.OSDetailedName
Data Type

string

OSNameOSName

Name of the operating system where the application is actually running.

This string value is the same as AppTargetOS, except among versions of
Windows—specifically, AppTargetOS has one enumeration on Windows XP while
OSName returns the exact version of Windows your application is running on. This
property is read only.

Syntax

object.OSName


                                                    © National Instruments 6261

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6261 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6262 ordinal=6262 -->
## Property and Method Reference

Property and Method Reference

     Data Type

        string

      OSVersionOSVersion

       Version number of the actual operating system. This property is read only.

     Syntax

     object.OSVersion
     Data Type

        string

       PrintDefaultPrinterPrintDefaultPrinter

       Gets or sets the name of the default printer in LabVIEW.

      To set the default printer, enter the full path to the printer, such as \\myprinter\
      ab01.

     Syntax

     object.PrintDefaultPrinter
     Data Type

        string

       PrintersAvailablePrintersAvailable

       Returns an alphabetized array of printer names available on the computer.

     Syntax

     object.PrintersAvailable


6262   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6262 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6263 ordinal=6263 -->
## Property and Method Reference

Property and Method Reference

Data Type

Array of strings

PrintingColorDepthPrintingColorDepth

If TRUE, LabVIEW sends color/grayscale output to the printer. If FALSE, LabVIEW sends
monochrome output to the printer.

Syntax

object.PrintingColorDepth
Data Type

Boolean

PrintMethodPrintMethod

Gets or sets how LabVIEW prints.

Syntax

object.PrintMethod
Data Type

PrintMethodsEnum

PrintSetupCustomClusterConstantsPrintSetupCustomClusterConstants

Specifies whether to print the hidden contents of iconified cluster constants that might
be present on the block diagram when using the custom format with one of the print
documentation VI methods.

Syntax

object.PrintSetupCustomClusterConstants


                                                    © National Instruments 6263

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6263 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6264 ordinal=6264 -->
## Property and Method Reference

Property and Method Reference

     Data Type

      bool

      PrintSetupCustomConnectorPrintSetupCustomConnector

       Specifies whether to print the connector pane and icon of VIs when using the custom
       format with one of the print documentation VI methods.

     Syntax

     object.PrintSetupCustomConnector
     Data Type

      Boolean

      PrintSetupCustomControlDescPrintSetupCustomControlDesc

       Specifies whether to print descriptions of front panel controls when using the custom
       format with one of the print documentation VI methods.

     Syntax

     object.PrintSetupCustomControlDesc
     Data Type

      Boolean

      PrintSetupCustomControlsPrintSetupCustomControls

       Specifies whether to print LabVIEW front panel control information when using the
      custom format with one of the print documentation VI methods. This property does
       not affect the image of the front panel, just the list of controls and indicators in the
       generated documentation.

     Syntax

     object.PrintSetupCustomControls

6264   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6264 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6265 ordinal=6265 -->
## Property and Method Reference

Property and Method Reference

Data Type

Boolean

PrintSetupCustomControlTypesPrintSetupCustomControlTypes

Specifies whether to print data type information for LabVIEW front panel controls
when using the custom format with one of the print documentation VI methods.

Syntax

object.PrintSetupCustomControlTypes
Data Type

Boolean

PrintSetupCustomDescriptionPrintSetupCustomDescription

Specifies whether to print VI descriptions when using the custom format with one of
the print documentation VI methods.

Syntax

object.PrintSetupCustomDescription
Data Type

Boolean

PrintSetupCustomDiagramPrintSetupCustomDiagram

Specifies whether to print LabVIEW block diagrams when using the custom format
with one of the print documentation VI methods.

Syntax

object.PrintSetupCustomDiagram


                                                    © National Instruments 6265

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6265 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6266 ordinal=6266 -->
## Property and Method Reference

Property and Method Reference

     Data Type

      Boolean

      PrintSetupCustomDiagramHiddenPrintSetupCustomDiagramHidden

       Specifies whether to print the hidden frames in LabVIEW Case and Stacked Sequence
       structures that might be present on the block diagram when using the custom format
       with one of the print documentation VI methods.

     Syntax

     object.PrintSetupCustomDiagramHidden
     Data Type

      Boolean

      PrintSetupCustomDiagramRepeatPrintSetupCustomDiagramRepeat

       Specifies whether to print visible subdiagrams of each Case, Event, and Stacked
      Sequence structure in sequence with the non-visible subdiagrams when using the
      custom format with one of the print documentation VI methods. If you print the visible
      frames in sequence, those frames will print twice.

     Syntax

     object.PrintSetupCustomDiagramRepeat
     Data Type

      Boolean

      PrintSetupCustomExpressVIConfigInfoPrintSetupCustomExpressVIConfigInfo

       Specifies whether to print the configuration information for any LabVIEW Express VIs
      on the block diagram when using the custom format with one of the print
      documentation VI methods.


6266   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6266 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6267 ordinal=6267 -->
## Property and Method Reference

Property and Method Reference

Syntax

object.PrintSetupCustomExpressVIConfigInfo
Data Type

Boolean

PrintSetupCustomHierarchyPrintSetupCustomHierarchy

Specifies whether to print the hierarchy of the VI in memory when using the custom
format with one of the print documentation VI methods.

Syntax

object.PrintSetupCustomHierarchy
Data Type

Boolean

PrintSetupCustomHistoryPrintSetupCustomHistory

Specifies whether to print the VI revision history information when using the custom
format with one of the print documentation VI methods.

Syntax

object.PrintSetupCustomHistory
Data Type

Boolean

PrintSetupCustomLabelPrintSetupCustomLabel

Specifies whether to print the label and/or caption for each control when using the
custom format with one of the print documentation VI methods.


                                                    © National Instruments 6267

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6267 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6268 ordinal=6268 -->
## Property and Method Reference

Property and Method Reference

     Syntax

     object.PrintSetupCustomLabel
     Data Type

      PrintSetupCustomLabelEnum

      PrintSetupCustomPanelPrintSetupCustomPanel

       Specifies whether to print the LabVIEW front panel when using the custom format with
      one of the print documentation VI methods.

     Syntax

     object.PrintSetupCustomPanel
     Data Type

      Boolean

      PrintSetupCustomPanelBorderPrintSetupCustomPanelBorder

       Specifies whether to print the LabVIEW front panel with a border when using the
      custom format with one of the print documentation VI methods.

     Syntax

     object.PrintSetupCustomPanelBorder
     Data Type

      Boolean

      PrintSetupCustomSubVIsPrintSetupCustomSubVIs

       Specifies whether to print a list of the LabVIEW subVIs and Express VIs including the
        icon, name, and path when using the custom format with one of the print
      documentation VI methods. If a polymorphic VI is a subVI, LabVIEW prints the instance
      used in the top-level VI including the icon, name, and path. If the top-level VI is

6268   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6268 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6269 ordinal=6269 -->
## Property and Method Reference

Property and Method Reference

polymorphic, LabVIEW prints a list of all the instances of the polymorphic VI including
the icon, name, and path of each instance.

Syntax

object.PrintSetupCustomSubVIs
Data Type

Boolean

PrintSetupFileWrapTextPrintSetupFileWrapText

Maximum number of characters on a single line in a file. Affects the PrintVIToHTML,
PrintVIToRTF, and PrintVIToText methods. Set this property to 0 to print all the
characters on one line so the text does not wrap.

Syntax

object.PrintSetupFileWrapText
Data Type

long

PrintSetupJPEGQualityPrintSetupJPEGQuality

Percentage value from 0 to 100 specifying the level of quality you want for the JPEG
graphic in VIs printed either interactively or with the PrintVIToHTML method. The scale
balances image quality and file size. A value in the 75-95 range produces a compressed
file with a high-quality image, and a value below 50 produces a smaller file size with a
low-quality image. The default is 80.

Syntax

object.PrintSetupJPEGQuality
Data Type

long

                                                    © National Instruments 6269

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6269 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6270 ordinal=6270 -->
## Property and Method Reference

Property and Method Reference

      PrintSetupPNGCompressLevelPrintSetupPNGCompressLevel

     Number between –1 and 9 that specifies the level of compression you want for the
     PNG file for graphics in VIs printed either interactively or with the PrintVIToHTML
      method. The quality of the graphic is not affected by the compression, but the graphic
          file size and speed of compression are affected by this value. Valid values range from
      –1 to 9 and balance file compression with speed. 0 designates no compression. 1
       designates the best speed with some compression. 9 designates the best compression,
      but slower speed. –1 (the default value) designates the best combination of good
      compression and speed.

     Syntax

     object.PrintSetupPNGCompressLevel
     Data Type

       long

      RTHostConnectedRTHostConnected

           If you are not targeted to a real-time (RT) platform, this property is always TRUE. If you
       are targeted to an RT-platform and the host is connected, this property is TRUE. When
        this property is FALSE, the host is not connected, requiring that the Real-Time Module
       application must be able to handle all operations independent of the host. Use this
       property to determine when it is safe to display a dialog box that requires user
        interaction.

     Syntax

     object.RTHostConnected
     Data Type

      Boolean

      SaveVersionSaveVersion

      The version number of the LabVIEW file format to which LabVIEW documents are saved


6270   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6270 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6271 ordinal=6271 -->
## Property and Method Reference

Property and Method Reference

by the application. This version number might be different than the version number of
the application. For example, a LabVIEW with version number 9.0.1 will save LabVIEW
documents with a file format version of 9.0.

Syntax

object.SaveVersion
Data Type

string

SaveVersionsSaveVersions

An array of the LabVIEW versions to which this version of LabVIEW can save. The array
is in reverse chronological order, with the element at position zero in the array being
the current version of LabVIEW. Each element of the array is a valid version to pass to
VI server functions which save to previous versions.

Syntax

object.SaveVersions
Data Type

variant

ShowFPTipStripsShowFPTipStrips

Writing the property: Setting this property to TRUE enables the display of tip strips on
LabVIEW front panel controls. Setting the property to FALSE prevents them from being
displayed. Reading the property: Specifies whether tip strips display when idling over
controls on the front panel.

Syntax

object.ShowFPTipStrips


                                                    © National Instruments 6271

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6271 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6272 ordinal=6272 -->
## Property and Method Reference

Property and Method Reference

     Data Type

      Boolean

     UserNameUserName

      User name used to open the application. This property is read only.

     Syntax

     object.UserName
     Data Type

        string

      VersionVersion

       Version number of the application. In a stand-alone application or shared library, this
       property returns the version of the LabVIEW Run-Time Engine. This property is read
        only.

     Syntax

     object.Version
     Data Type

        string

      VersionYearVersionYear

       Version year of the application. In a built application or shared library, this property
       returns the version year of the LabVIEW Run-Time Engine.

     Syntax

     object.VersionYear


6272   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6272 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6273 ordinal=6273 -->
## Property and Method Reference

Property and Method Reference

Data Type

String

VIServerPortVIServerPort

Gets or sets the LabVIEW VI server port. LabVIEW returns an error if you attempt to
access this property on a remote application.

Syntax

object.VIServerPort
Data Type

unsigned long

EnumerationsEnumerations (ActiveX)(ActiveX)

The following enumerations are used in the various properties and methods.

AppKindEnumAppKindEnum

Indicates the type of application.


 Name            Value  Description

 eInvalidAppKind   0      Invalid application kind

                       LabVIEW Development System, including the Base Development
 eDevSysKind      1
                         System, Full Development System, or Professional Development System

 eRunTimeSysKind 2     Run-Time System

 eStudEdKind      3     LabVIEW Student Edition

 eEmbeddedKind   4    Embedded System, including LabVIEW Real-Time

 eEvaluation       5      Evaluation version


                                                    © National Instruments 6273

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6273 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6274 ordinal=6274 -->
## Property and Method Reference

Property and Method Reference

     AppTargCPUEnumAppTargCPUEnum

       Indicates the central processing unit (CPU) of the machine on which the application is
       running.


      Name                                Value         Description

         eInvalidTargCPU                      0               Invalid target CPU

        eMotorola68kCPU                     1             Motorola 68K

       ePowerPCCPU                        2           PowerPC

        eIntelx86CPU                        3                Intel x86

       eSPARCCPU                          4           SPARC

       ePARISCCPU                         5             PA-RISC

       eMIPSCPU                           6            MIPS

        eAlphaCPU                          7             Alpha

       eArmCPU                            8          ARM

       eX64CPU                            9             AMD/Intel x64

     AppTargOSEnumAppTargOSEnum

       Indicates the type of operating system (OS) on which the application is running. Mac
     OS refers to Mac OS versions 8 and 9. Carbon refers to Mac OS X.


      Name                              Value           Description

         eInvalidTargOS                     0                 Invalid Target OS

       eMacOS                           1            Mac OS X

       eWin31OS                         2            Windows 3.1

       eWin95NTOS                      3            Windows 95/NT

         eSolaris1OS                       4                Solaris 1

         eSolaris2OS                       5                Solaris 2

       eHPUXOS                         6             HP-UX


6274   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6274 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6275 ordinal=6275 -->
## Property and Method Reference

Property and Method Reference


 Name                              Value           Description

 ePowerMaxOS                     7            PowerMax

 eLinuxOS                         8               Linux

 eIrixOS                           9                     Irix

 eRhapsodyOS                      10            Rhapsody

 eBeOS                            11           BeOS

 eAIXOS                           12              AIX

 eOSF1OS                         13           OSF1

 eVxWorksOS                       14            VxWorks

 ePharlapOS                       15             Phar Lap

 eCarbonOS                        16            Carbon

 eRTXOS                           17            RTX

 eWin64OS                         18           Windows x64

 eLinux64OS                       19              Linux x64

ExecStateEnumExecStateEnum

Indicates the execution state of a VI.


 Name                Value     Description

 eBad                0           VI has errors; it cannot run.

 eIdle                1           VI is not running, but the VI is in memory.

 eRunTopLevel         2           VI is running as a top-level VI.

 eRunning            3           VI is running as a subVI.

FPRunTimePosEnumFPRunTimePosEnum

Indicates the run-time LabVIEW front panel position.


                                                    © National Instruments 6275

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6275 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6276 ordinal=6276 -->
## Property and Method Reference

Property and Method Reference


      Name                                    Value            Description

       eRTPUnchanged                          0              Unchanged

        eRTPCentered                            1               Centered

        eRTPMaximized                          2               Maximized

        eRTPMinimized                           3               Minimized

       eRTPCustom                             4              Custom

     FPStateEnumFPStateEnum

       Indicates how LabVIEW displays the front panel window.


      Name      Value  Description

                                            If you read this property and an error occurs, the property returns this value. If          Invalid     0                       you set the property to this value, the property returns an error.

        Standard   1     The front panel window is open but is not minimized, maximized, or hidden.

                       The front panel window is not open. If you set the property to this value, the
        Closed     2                           property returns an error.

                       The front panel window is floating but is not visible because LabVIEW is not the
                             active application. If you set the property to this value and close all references
                            to the front panel, the window remains open but hidden. Because the VI is
        Hidden    3                         open, the Getting Started window does not appear. To solve this problem, open
                          the VI from the operating system. For example, double-click the VI in Windows
                            Explorer to open the VI.

        Minimized  4     The front panel window is minimized.

        Maximized 5     The front panel window is maximized.

     HTMLImageFormatEnumHTMLImageFormatEnum

       Indicates the HTML image format to use for printing to an HTML file.


      Name                   Value                  Description

       ePNG                  0                PNG format


6276   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6276 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6277 ordinal=6277 -->
## Property and Method Reference

Property and Method Reference


 Name                   Value                  Description

 eJPEG                  1                  JPEG format

 eGIF                   2                      GIF format

LibraryItemScopeEnumLibraryItemScopeEnum

Indicates the LibraryItem scope.


 0               Invalid Scope

 1              Public

 2               Private

 3              Protected

 4           Community

PageOrientationEnumPageOrientationEnum

Indicates the page orientation when LabVIEW prints the VI.


 Name         Value  Description

 Portrait       0      Prints the report so the short edge of the paper is the top of the page.

 Landscape    1      Prints the report so the long edge of the paper is the top of the page.

 Rotated              Rotates the paper 90 degrees counterclockwise and prints the report using a
              2
 Portrait                portrait orientation.

 Rotated              Rotates the paper 90 degrees counterclockwise and prints the report using a
              3
 Landscape           landscape orientation.

PrintFormatEnumPrintFormatEnum

Indicates the image format to use for printing.


                                                    © National Instruments 6277

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6277 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6278 ordinal=6278 -->
## Property and Method Reference

Property and Method Reference


      Name       Value  Description

       eCustom    0     Use the Application properties to specify the format.

                                Prints the VI description, icon and connector pane, front panel, and block        eStandard   1                            diagram.

                                Prints the VI description, front panel, and controls and indicators, including
        eUsingPanel  2     data types, names, and descriptions. LabVIEW prints the controls and
                               indicators in tabbing order.

                                Prints the VI description, icon and connector pane, and connected controls
        eUsingSubVI 3     and indicators, including data types, names, and descriptions. LabVIEW prints
                            the controls and indicators in tabbing order.

                                Prints the VI description; icon and connector pane; front panel; controls and
                                indicators, including data types, names, and descriptions; block diagram; a        eComplete   4
                                          list of subVIs, including icons, names, and paths; revision history information;
                        and the VI hierarchy.

     PrintMarginsEnumPrintMarginsEnum

       Array of variants that include the following elements:


      Name            Value       Description

        element 1           (float)      top

        element 2           (float)         left

        element 3           (float)      bottom

        element 4           (float)       right

        element 5          (byte)      measurement system (0=Inches, 1=cm)

     PrintMethodsEnumPrintMethodsEnum

       Indicates how LabVIEW prints the data.


      Name     Value  Description

                            Translates the VI print data (front panel, block diagram, icon, and so on) and
        Standard  0
                        sends it to the printer using the standard operating system drawing commands.

6278   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6278 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6279 ordinal=6279 -->
## Property and Method Reference

Property and Method Reference


 Name     Value  Description

                You must use this option if the printer does not have PostScript support or if you
                want the printer driver to handle the PostScript translation instead of LabVIEW.

                    Translates the VI print data in PostScript (.ps) format and sends it to the printer
                  as PostScript commands. Do not use this option if the printer or printer driver PostScript 1
                 does not support PostScript printing. PostScript printouts reproduce the image
                    of the screen, including patterns, line styles, and fonts, more accurately.

                   Creates a bitmap, draws all data for that page into the bitmap, and sends the Bitmap    2                 bitmap to the printer.

PrintSetupCustomLabelEnumPrintSetupCustomLabelEnum

Indicates whether to print the label and/or caption for each control when using the
custom format with one of the print documentation VI methods.


 Name         Value  Description

 Label         0      Prints only the label of the front panel control.

 Caption       1      Prints only the caption of the front panel control.

                         Prints the caption and the label in square brackets of the front panel Caption[Label] 2                         control.

VIExecSysEnumVIExecSysEnum

Indicates the execution system in which a VI runs.


 Name                             Value       Description

 eESysInvalid                      0             Invalid execution system

 eESysUserInterface                 1           User interface

 eESysNormal                      2           Standard

 eESysInstrIO                      3           Instrument I/O

 eESysDAQ                        4           Data acquisition (DAQ)

 eESysOther1                      5           Other 1


                                                    © National Instruments 6279

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6279 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6280 ordinal=6280 -->
## Property and Method Reference

Property and Method Reference


      Name                             Value       Description

        eESysOther2                      6           Other 2

        eESysSameAsCaller                7         Same as caller

     VIFPBehaviorEnumVIFPBehaviorEnum

       Indicates how LabVIEW displays the front panel window.


      Name     Value  Description

                                          If you read this property and an error occurs, the property returns this value. If          Invalid    0                       you set the property to this value, the property returns an error.

         Default    1     The front panel window is not floating or modal.

                      The front panel window stays on top of all other non-modal LabVIEW windows.         Floating   2                      The Just-In-Time Advice window is an example of a floating window.

         Floating/                      The front panel window is floating and when you switch from LabVIEW to         Auto-     3
                         another application, the window does not appear.        Hide

                      The front panel window stays on top of all other LabVIEW windows until you
        Modal    4                           close the window or open another modal window.

     VILockStateEnumVILockStateEnum

       Indicates the lock state of a VI.


      Name                                 Value        Description

         eInvalidLockState                     0             Invalid VI lock state

        eUnlockedState                       1           Unlocked

        eLockedNoPwdState                   2            Locked, no password

        ePwdProtectedState                   3            Password-protected


6280   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6280 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6281 ordinal=6281 -->
## Property and Method Reference

Property and Method Reference

VIPriorityEnumVIPriorityEnum

Indicates the execution priority of a VI.


 Name                                   Value           Description

 ePriInvalid                             0                 Invalid priority

 ePriBackground                         1             Background

 ePriNormal                            2             Normal

 ePriAboveNormal                       3             Above normal

 ePriHigh                               4              High

 ePriCritical                             5                  Critical

 ePriSubroutine                         6              Subroutine

VITypeEnumVITypeEnum

Indicates the type of a VI.


 Name                                      Value         Description

 eInvalidVIType                            0               Invalid VI type

 eStandardVIType                          1            Standard VI

 eControlVIType                            2             Control VI

 eGlobalVIType                             3             Global VI

 ePolymorphicVIType                       4            Polymorphic VI

 eConfigurationVIType                       5             Configuration VI

 eSubSystemVIType                         6           SubSystem

 eFacadeVIType                            7            Facade VI

 eMethodVIType                            8           Method VI


                                                    © National Instruments 6281

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6281 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6282 ordinal=6282 -->
## Property and Method Reference

Property and Method Reference

     ProjectProject PropertiesProperties andand MethodsMethods

       This book contains the property and method reference information for the Project
        class.

      ProjectProject MethodsMethods (ActiveX)(ActiveX)

     Methods

       Method          Description

                          Closes a LabVIEW project and all references to all items in the project. This
                     method also closes the LabVIEW Project Explorer window if it is open and closes
         Close           any VIs that are open in any application instance owned by the project. In
                        LabVIEW, you also can select File»Close All to close the project and the Project
                           Explorer window.


                          Closes only the LabVIEW Project Explorer window. This method does not close VI        CloseWindow                       windows.


        DeployItems     Deploys an array of items in the LabVIEW project.


       OpenWindow     Displays the LabVIEW Project Explorer window.


                        Saves the LabVIEW project to the path that the project was previously saved to or
        Save
                        loaded from or to a specified path.


                        Saves a copy of the LabVIEW project that is readable by LabVIEW version 8.0 and
        SaveForPrevious
                                 later.


6282   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6282 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6283 ordinal=6283 -->
## Property and Method Reference

Property and Method Reference

CloseClose

Closes a LabVIEW project and all references to all items in the project. This method
also closes the LabVIEW Project Explorer window if it is open and closes any VIs that
are open in any application instance owned by the project. In LabVIEW, you also can
select File»Close All to close the project and the Project Explorer window.

Syntax

object.Close()
Return Value

none

CloseWindowCloseWindow

Closes only the LabVIEW Project Explorer window. This method does not close VI
windows.

In LabVIEW, you also can select File»Exit to close the Project Explorer window and any
VIs that are open.

Syntax

object.CloseWindow()
Return Value

none

DeployItemsDeployItems

Deploys an array of items in the LabVIEW project.

Syntax

object.DeployItems(items, silent, [UserName], [Password])


                                                    © National Instruments 6283

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6283 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6284 ordinal=6284 -->
## Property and Method Reference

Property and Method Reference

     Parameters

      Name     Type                  Description

        items      kLVProjectItemObjRef1  Specifies an array of references to items in the project.

                                                                     If TRUE, LabVIEW does not display any dialog boxes during the          silent      Boolean                                        deploy operation.

       UserName  String                   Specifies the user name.

                                              Specifies the password to use to unlock a password-protected        Password   string                                              project library.

     Return Value

      none

     OpenWindowOpenWindow

       Displays the LabVIEW Project Explorer window.

     Syntax

     object.OpenWindow()
     Return Value

      none

      SaveSave

      Saves the LabVIEW project to the path that the project was previously saved to or
      loaded from or to a specified path.

           If the project has not been saved and the value of the path parameter is <Not A
     Path> or path is not specified, this method returns an error.

     Syntax

     object.Save(path)


6284   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6284 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6285 ordinal=6285 -->
## Property and Method Reference

Property and Method Reference

Parameters

 Name            Type               Description

 path                 String              Path to the project.

Return Value

none

SaveForPreviousSaveForPrevious

Saves a copy of the LabVIEW project that is readable by LabVIEW version 8.0 and later.

      Note The LabVIEW Datalogging and Supervisory Control Module supports
         this method in the Run-Time Engine.

Syntax

object.SaveForPrevious([path], [Version])
Parameters

 Name  Type  Description

 path    path  Path to where you want to save a copy of the project.

                Version of LabVIEW for which you want to save. Wire the version number, such as
 Version  string 8.6 or 2009, to the Target Version input. The default is the immediately previous
                 version.

Return Value

none

ProjectProject PropertiesProperties (ActiveX)(ActiveX)

In the following topics, an asterisk (*) at the end of a data type name indicates that the
property is a pointer.

                                                    © National Instruments 6285

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6285 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6286 ordinal=6286 -->
## Property and Method Reference

Property and Method Reference

      Properties

        Property            Description

                                               If the LabVIEW Project Explorer window has focus, returns an array of
                              references to the selected project items in the Project Explorer window. If the
         ActiveItemsInTree    Project Explorer window does not have focus, returns a reference to the
                               project item associated with the VI window that has focus. You can use these
                              references with the ProjectItem properties.


                            Returns the application reference for the My Computer target in the LabVIEW         Application                                 project. You can use this reference with the Application properties.


         Description          Gets or sets the description of the LabVIEW project.


                            Returns a reference to My Computer in the Project Explorer window for the       MyComputer                         LabVIEW project. You can use this reference with the TargetItem properties.


                            Gets the name of the LabVIEW project. If the project has been saved, this
      Name               property returns the filename with the file extension. If the project has not
                         been saved, this property returns untitled project x.


                            Gets the path to the saved LabVIEW project on disk. This path includes the
        Path
                             filename of the project.


                            Returns a reference to the project root in the LabVIEW Project Explorer
                          window. The project root is the top item that represents the LabVIEW project
        Root
                                 in the Project Explorer window. You can use this reference with the
                              ProjectItem properties.


                            Returns an array of references to the project items currently selected in the
         SelectedItemsInTree
                         LabVIEW Project Explorer window. You can use these references with the


6286   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6286 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6287 ordinal=6287 -->
## Property and Method Reference

Property and Method Reference


 Property            Description

                      ProjectItem properties.


                     Returns an array of references to all targets in the current LabVIEW project. Targets                   You can use these references with the TargetItem properties.


 WindowState        Returns the state of the LabVIEW Project Explorer window.


ActiveItemsInTreeActiveItemsInTree

If the LabVIEW Project Explorer window has focus, returns an array of references to the
selected project items in the Project Explorer window. If the Project Explorer window
does not have focus, returns a reference to the project item associated with the VI
window that has focus. You can use these references with the ProjectItem properties.

Syntax

object.ActiveItemsInTree
Data Type

1D array of ProjectItems

ApplicationApplication

Returns the application reference for the My Computer target in the LabVIEW project.
You can use this reference with the Application properties.

If the project has multiple targets, each target is associated with a single application
instance.

Syntax

object.Application


                                                    © National Instruments 6287

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6287 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6288 ordinal=6288 -->
## Property and Method Reference

Property and Method Reference

     Data Type

       Application*

       DescriptionDescription

       Gets or sets the description of the LabVIEW project.

     Syntax

     object.Description
     Data Type

       String

     MyComputerMyComputer

       Returns a reference to My Computer in the Project Explorer window for the LabVIEW
        project. You can use this reference with the TargetItem properties.

     Syntax

     object.MyComputer
     Data Type

       TargetItem*

     NameName

       Gets the name of the LabVIEW project. If the project has been saved, this property
       returns the filename with the file extension. If the project has not been saved, this
       property returns untitled project x.

     Syntax

     object.Name


6288   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6288 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6289 ordinal=6289 -->
## Property and Method Reference

Property and Method Reference

Data Type

string

PathPath

Gets the path to the saved LabVIEW project on disk. This path includes the filename of
the project.

Syntax

object.Path
Data Type

string

RootRoot

Returns a reference to the project root in the LabVIEW Project Explorer window. The
project root is the top item that represents the LabVIEW project in the Project Explorer
window. You can use this reference with the ProjectItem properties.

Syntax

object.Root
Data Type

ProjectItem*

SelectedItemsInTreeSelectedItemsInTree

Returns an array of references to the project items currently selected in the LabVIEW
Project Explorer window. You can use these references with the ProjectItem properties.

Syntax

object.SelectedItemsInTree


                                                    © National Instruments 6289

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6289 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6290 ordinal=6290 -->
## Property and Method Reference

Property and Method Reference

     Data Type

      1D array of ProjectItems

       TargetsTargets

       Returns an array of references to all targets in the current LabVIEW project. You can use
       these references with the TargetItem properties.

     Syntax

     object.Targets
     Data Type

      1D array of TargetItems

      WindowStateWindowState

       Returns the state of the LabVIEW Project Explorer window.

     Syntax

     object.WindowState
     Data Type

      FPStateEnum

     ProjectItemProjectItem PropertiesProperties andand MethodsMethods

       This book contains the property and method reference information for the ProjectItem
        class.

      ProjectItemProjectItem MethodsMethods (ActiveX)(ActiveX)


6290   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6290 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6291 ordinal=6291 -->
## Property and Method Reference

Property and Method Reference

Methods

 Method               Description

                    Adds a file at the specified path to the LabVIEW project with the referenced
 AddFile                        project item as the parent.


                    Adds a new project item of the specified type to the LabVIEW project with AddItem                      the referenced item as the parent.


                    Adds an item that exists in memory to the LabVIEW project with the AddItemFromMemory
                       referenced project item as the parent.


                   Removes the referenced project item from the LabVIEW project. If the item Delete                     has children, the children also are deleted.


 DeleteTag           Removes the named tag from the LabVIEW project item.


                      Returns LabVIEW project items that are descendents of the referenced item.
 GetAllDescendents       If you specify a value for type, this method only returns project items of the
                        specified type.


 GetTag               Returns a tag value associated with the LabVIEW project item.


                      Returns an array of tag names of all tags on the referenced LabVIEW project
 GetTagNames
                        item.


 GetXMLTag            Returns the value in an XML tag.


                                                    © National Instruments 6291

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6291 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6292 ordinal=6292 -->
## Property and Method Reference

Property and Method Reference


       Method               Description

        SetTag                Sets a tag value associated with the LabVIEW project.


        SetXMLTag            Set the value of an XML tag associated with the LabVIEW project.


      AddFileAddFile

      Adds a file at the specified path to the LabVIEW project with the referenced project
      item as the parent.

     Syntax

     object.AddFile(path)
     Parameters

      Name        Type          Description

        path           String         Path to the file you want to add.

     Return Value

       ProjectItem*

      AddItemAddItem

      Adds a new project item of the specified type to the LabVIEW project with the
       referenced item as the parent.

       This method returns an error if the specified type cannot be created under the current
       item. The method also returns an error when you try to add a shared variable to a
        library that is not opened in a project.

     Syntax

     object.AddItem(name, path, type)

6292   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6292 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6293 ordinal=6293 -->
## Property and Method Reference

Property and Method Reference

Parameters

 Name Type  Description

 name  String Name of the project item you want to add.

 path   String Path to the project item you want to add.

                Specifies the project item type.The following values are the most common type
                values:

                         • VI
                         • Folder
                         • Library
                         • XControl
                         • EXE
                         • DLL
                         • Source Distribution
                         • Installer type   String
                         • Zip File
                         • Hyperlink

           Some of the values listed above are supported only on certain LabVIEW
             Development Systems. Refer to ni.com/labview for more information about
             LabVIEW Development Systems.

             To determine the value of type for a project item that is not listed above, use the
               TypeString property to programmatically return the type of the item. For cross-
              language reasons, this string is always in English.


Return Value

ProjectItem*

AddItemFromMemoryAddItemFromMemory

Adds an item that exists in memory to the LabVIEW project with the referenced project
item as the parent.

Syntax

object.AddItemFromMemory(name)

                                                    © National Instruments 6293

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6293 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6294 ordinal=6294 -->
## Property and Method Reference

Property and Method Reference

     Parameters

      Name Type  Description

       name  String Name that exists in memory, such as foo.vi, of the project item you want to add.

     Return Value

       ProjectItem*

      DeleteDelete

      Removes the referenced project item from the LabVIEW project. If the item has
       children, the children also are deleted.

     Syntax

     object.Delete()
     Return Value

      none

      DeleteTagDeleteTag

      Removes the named tag from the LabVIEW project item.

     Syntax

     object.DeleteTag(tagName)
     Parameters

      Name    Type   Description

       tagName   String  Name of the tag. Use the GetTagNames method to retrieve the tag names.

     Return Value

      Boolean

6294   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6294 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6295 ordinal=6295 -->
## Property and Method Reference

Property and Method Reference

GetAllDescendentsGetAllDescendents

Returns LabVIEW project items that are descendents of the referenced item. If you
specify a value for type, this method only returns project items of the specified type.

This method returns a flat list that includes all descendents unless you use the type,
excludeDependencies, excludeBuilds, and excludeTargets parameters to limit what
the method returns.

Syntax

object.GetAllDescendents(type, [excludeDependencies],
[excludeBuilds], [excludeTargets])
Parameters

 Name              Type     Description

                                  Specifies the project item type. The following values are the most
                       common type values:

                                                  • VI
                                                  • Folder
                                                  • Library
                                                  • XControl
                                                  • EXE
                                                  • DLL
                                                  • Source Distribution
                                                  • Installer
 type                   String        • Zip File
                                                  • Hyperlink

                        Some of the values listed above are supported only on certain
                            LabVIEW Development Systems. Refer to ni.com/labview for more
                                information about LabVIEW Development Systems.

                            To determine the value of type for a project item that is not listed
                               above, use the TypeString property to programmatically return
                               the type of the item. For cross-language reasons, this string is
                              always in English.

 excludeDependencies Boolean  If TRUE, does not return Dependencies or any items under

                                                    © National Instruments 6295

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6295 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6296 ordinal=6296 -->
## Property and Method Reference

Property and Method Reference


      Name              Type     Description

                                     Dependencies. The default is FALSE.

                                                                 If TRUE, does not return Build Specifications or any items under         excludeBuilds        Boolean                                        Build Specifications. The default is FALSE.

                                                                 If TRUE, does not return any targets or any items under targets.         excludeTargets       Boolean
                                  The default is FALSE.

     Return Value

      1D array of ProjectItems

      GetTagGetTag

       Returns a tag value associated with the LabVIEW project item.

     Syntax

     object.GetTag(tagName, value, [isPersistent])
     Parameters

      Name      Type     Description

       tagName    String   Name of the tag. Use the GetTagNames method to retrieve the tag names.

         value        variant    Specifies the tag value as a variant.

                              Returns TRUE if LabVIEW saves the tag information when you save the          isPersistent Boolean*
                           LabVIEW project. Returns FALSE otherwise.

     Return Value

      Boolean

     GetTagNamesGetTagNames

       Returns an array of tag names of all tags on the referenced LabVIEW project item.


6296   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6296 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6297 ordinal=6297 -->
## Property and Method Reference

Property and Method Reference

Syntax

object.GetTagNames()
Return Value

Array of strings

GetXMLTagGetXMLTag

Returns the value in an XML tag.

Use the SetXMLTag method to set the value in an XML tag.

Syntax

object.GetXMLTag(tagName, [value], [isPersistent])
Parameters

 Name      Type     Description

 tagName    String   Name of the tag. Use the GetTagNames method to retrieve the tag names.

 value        String*    Returns the value of the XML tag as a string.

                      Returns TRUE if LabVIEW saves the tag information when you save the isPersistent Boolean*                    LabVIEW project. Returns FALSE otherwise.

Return Value

Boolean

SetTagSetTag

Sets a tag value associated with the LabVIEW project.

Syntax

object.SetTag(tagName, value, [isPersistent])


                                                    © National Instruments 6297

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6297 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6298 ordinal=6298 -->
## Property and Method Reference

Property and Method Reference

     Parameters

      Name      Type     Description

       tagName    String   Name of the tag. Use the GetTagNames method to retrieve the tag names.

         value        variant   Specifies the tag value as a variant.

                                                 If TRUE, LabVIEW saves the tag information when you save the LabVIEW          isPersistent Boolean                                  project. The default is FALSE.

     Return Value

      none

      SetXMLTagSetXMLTag

       Set the value of an XML tag associated with the LabVIEW project.

     Syntax

     object.SetXMLTag(tagName, value, [isPersistent])
     Parameters

      Name      Type     Description

       tagName    String   Name of the tag. Use the GetTagNames method to retrieve the tag names.

         value        variant   Specifies the tag value as a variant.

                                                 If TRUE, LabVIEW saves the tag information when you save the LabVIEW
          isPersistent Boolean
                                  project. The default is FALSE.

     Return Value

      none

      ProjectItemProjectItem PropertiesProperties (ActiveX)(ActiveX)

        In the following topics, an asterisk (*) at the end of a data type name indicates that the
       property is a pointer.

6298   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6298 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6299 ordinal=6299 -->
## Property and Method Reference

Property and Method Reference

Properties

 Property                             Description

                                     Returns an array of references to all children of the
 Children                              referenced LabVIEW project item. You can use these
                                       references with the ProjectItem properties.


                                     Returns TRUE if this item or items beneath this item in the ContainsConflicts                                        project tree are in conflict.


                                         Gets, as a string, the name of the LabVIEW project item as DisplayName
                                     the name appears in the LabVIEW Project Explorer window.


                                     Returns an array of references to all project items that FindCallers
                                       reference the project item you select.


                                     Returns an array of references to all project items that are FindChildren                                        children of the project item you select.


                                     Returns an array of references to all project items that are FindConflicts                                           in conflict with the project item you select.


                                     Returns an array of references to all project items that are
 FindFriends
                                         friends of the project item you select.


                                     Returns an array of references to all project items that are
 FindItemsIncorrectlyClaimedByLibrary
                                    claimed by a library but do not reciprocate the claim.


                                     Returns an array of references to all project items under
 FindItemsThatMakeThisADependency
                                     the target that are not under dependencies but cause this


                                                    © National Instruments 6299

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6299 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6300 ordinal=6300 -->
## Property and Method Reference

Property and Method Reference


        Property                             Description

                                            item to be under dependencies.


                                             Returns an array of references to all top-level project items         FindItemsWithNoCallers                                                that call no other project items.


                                             Returns an array of references to all project items that are        FindSubVIs                                              subVIs of the item you select.


                                             Returns an array of references to all VI project items that         FindVariableCallers
                                                reference the variable project item you select.


                                             Gets the icon of the project item in the LabVIEW Project
         Icon                                   Explorer window using the Icon cluster, which limits size
                                       and color depth.


                                             Returns TRUE if the referenced LabVIEW project item
          InConflict                                 conflicts with another item with a different path under the
                                     same target.


                                             Gets the item ID of the referenced LabVIEW project item as
                                         a string. You can use this item ID to uniquely identify the
        ItemID
                                              referenced item even if the path, name, or location in the
                                        LabVIEW Project Explorer window changes.


                                             Gets the type of the LabVIEW project item as it exists in the
                                                 project library as a GUID string. Use the
         LibraryItemType
                                               LibraryItemTypeString property to return the type as a
                                          human-readable string.


6300   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6300 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6301 ordinal=6301 -->
## Property and Method Reference

Property and Method Reference


Property                             Description

                                    Returns the type of the LabVIEW project item as it exists in
LibraryItemTypeString                the project library as a string. Use the LibraryItemType
                                     property to return the type as a GUID.


                                    Gets the name of the referenced LabVIEW project item as itName                                                  is saved in the file.


                                    Returns a reference to the parent of the referenced
Parent                           LabVIEW project item. You can use this reference with the
                                      ProjectItem properties.


Path                                Gets the path of the referenced LabVIEW project item.


                                    Returns a reference to the LabVIEW project to which the
Project                               referenced project item belongs. You can use this reference
                                    with the Project properties.


                                    Returns a reference to the target that contains the
Target                                referenced LabVIEW project item. You can use this
                                       reference with the TargetItem properties.


                                    Gets the type of the LabVIEW project item as a GUID string.
TypeGUID
                                Use the TypeString property to return the type as a string.


                                    Gets the type of the LabVIEW project item as a string. Use
TypeString
                                     the TypeGUID property to return the type as a GUID.


                                                            If the LabVIEW project item refers to a VI, this property
VI
                                       returns a reference to the VI. Otherwise, this property


                                                    © National Instruments 6301

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6301 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6302 ordinal=6302 -->
## Property and Method Reference

Property and Method Reference


        Property                             Description

                                                returns NULL.


                                                                           If the project item refers to a VI in memory, this property
                                                returns a reference to the VI. If the project item refers to a
        VINoLoad                                 VI not in memory or to something that is not a VI, this
                                              property returns Not a Refnum. You can use this
                                                reference with the VI properties.


                                                                           If TRUE, indicates that the LabVIEW Project Explorer
                                     window is visible and ancestors of the LabVIEW project
          VisibleInTree                                            item are expanded in the Project Explorer window up to
                                             the root of the project item.


      ChildrenChildren

       Returns an array of references to all children of the referenced LabVIEW project item.
      You can use these references with the ProjectItem properties.

     Syntax

     object.Children
     Data Type

      1D array of ProjectItems

       ContainsConflictsContainsConflicts

       Returns TRUE if this item or items beneath this item in the project tree are in conflict.

     Syntax

     object.ContainsConflicts


6302   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6302 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6303 ordinal=6303 -->
## Property and Method Reference

Property and Method Reference

Data Type

Boolean

DisplayNameDisplayName

Gets, as a string, the name of the LabVIEW project item as the name appears in the
LabVIEW Project Explorer window.

Syntax

object.DisplayName
Data Type

string

FindCallersFindCallers

Returns an array of references to all project items that reference the project item you
select.

Syntax

object.FindCallers
Data Type

ProjectItem*

FindChildrenFindChildren

Returns an array of references to all project items that are children of the project item
you select.

Syntax

object.FindChildren


                                                    © National Instruments 6303

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6303 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6304 ordinal=6304 -->
## Property and Method Reference

Property and Method Reference

     Data Type

       ProjectItem*

       FindConflictsFindConflicts

       Returns an array of references to all project items that are in conflict with the project
      item you select.

     Syntax

     object.FindConflicts
     Data Type

      1D array of ProjectItems

      FindFriendsFindFriends

       Returns an array of references to all project items that are friends of the project item
      you select.

     Syntax

     object.FindFriends
     Data Type

       ProjectItem*

      FindItemsIncorrectlyClaimedByLibraryFindItemsIncorrectlyClaimedByLibrary

       Returns an array of references to all project items that are claimed by a library but do
       not reciprocate the claim.

     Syntax

     object.FindItemsIncorrectlyClaimedByLibrary


6304   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6304 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6305 ordinal=6305 -->
## Property and Method Reference

Property and Method Reference

Data Type

kLVProjectItemObjRef1

FindItemsThatMakeThisADependencyFindItemsThatMakeThisADependency

Returns an array of references to all project items under the target that are not under
dependencies but cause this item to be under dependencies.

Syntax

object.FindItemsThatMakeThisADependency
Data Type

ProjectItem*

FindItemsWithNoCallersFindItemsWithNoCallers

Returns an array of references to all top-level project items that call no other project
items.

Syntax

object.FindItemsWithNoCallers
Data Type

1D array of ProjectItems

FindSubVIsFindSubVIs

Returns an array of references to all project items that are subVIs of the item you
select.

Syntax

object.FindSubVIs


                                                    © National Instruments 6305

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6305 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6306 ordinal=6306 -->
## Property and Method Reference

Property and Method Reference

     Data Type

      1D array of ProjectItems

       FindVariableCallersFindVariableCallers

       Returns an array of references to all VI project items that reference the variable project
      item you select.

     Syntax

     object.FindVariableCallers
     Data Type

      1D array of ProjectItems

      IconIcon

       Gets the icon of the project item in the LabVIEW Project Explorer window using the
       Icon cluster, which limits size and color depth.

     Syntax

     object.Icon
     Data Type

      ImageData

       InConflictInConflict

       Returns TRUE if the referenced LabVIEW project item conflicts with another item with a
        different path under the same target.

     Syntax

     object.InConflict


6306   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6306 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6307 ordinal=6307 -->
## Property and Method Reference

Property and Method Reference

Data Type

Boolean

ItemIDItemID

Gets the item ID of the referenced LabVIEW project item as a string. You can use this
item ID to uniquely identify the referenced item even if the path, name, or location in
the LabVIEW Project Explorer window changes.

Syntax

object.ItemID
Data Type

string

LibraryItemTypeLibraryItemType

Gets the type of the LabVIEW project item as it exists in the project library as a GUID
string.

Use the LibraryItemTypeString property to return the type as a human-readable string.

If the item is not part of a library, this property returns an error.

Syntax

object.LibraryItemType
Data Type

string

LibraryItemTypeStringLibraryItemTypeString

Returns the type of the LabVIEW project item as it exists in the project library as a
string.


                                                    © National Instruments 6307

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6307 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6308 ordinal=6308 -->
## Property and Method Reference

Property and Method Reference

      Use the LibraryItemType property to return the type as a GUID.

       This property is valid only if the LabVIEW project item exists in a project library.

     Syntax

     object.LibraryItemTypeString
     Data Type

        string

     NameName

       Gets the name of the referenced LabVIEW project item as it is saved in the file.

      Use the DisplayName property to get the name as it appears in the LabVIEW Project
       Explorer window.

     Syntax

     object.Name
     Data Type

        string

      ParentParent

       Returns a reference to the parent of the referenced LabVIEW project item. You can use
        this reference with the ProjectItem properties.

     Syntax

     object.Parent
     Data Type

       ProjectItem*


6308   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6308 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6309 ordinal=6309 -->
## Property and Method Reference

Property and Method Reference

PathPath

Gets the path of the referenced LabVIEW project item.

Syntax

object.Path
Data Type

string

ProjectProject

Returns a reference to the LabVIEW project to which the referenced project item
belongs. You can use this reference with the Project properties.

Syntax

object.Project
Data Type

Project*

TargetTarget

Returns a reference to the target that contains the referenced LabVIEW project item.
You can use this reference with the TargetItem properties.

Syntax

object.Target
Data Type

TargetItem*


                                                    © National Instruments 6309

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6309 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6310 ordinal=6310 -->
## Property and Method Reference

Property and Method Reference

     TypeGUIDTypeGUID

       Gets the type of the LabVIEW project item as a GUID string.

      Use the TypeString property to return the type as a string.

     Syntax

     object.TypeGUID
     Data Type

        string

      TypeStringTypeString

       Gets the type of the LabVIEW project item as a string.

      Use the TypeGUID property to return the type as a GUID.

     Syntax

     object.TypeString
     Data Type

        string

       VIVI

           If the LabVIEW project item refers to a VI, this property returns a reference to the VI.
       Otherwise, this property returns NULL.

           Note This property does not record changes to the VI. If you use this
               reference for editing the VI you will not be prompted to save when the
               reference closes.


6310   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6310 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6311 ordinal=6311 -->
## Property and Method Reference

Property and Method Reference

Syntax

object.VI
Data Type

VirtualInstrument*

VINoLoadVINoLoad

If the project item refers to a VI in memory, this property returns a reference to the VI. If
the project item refers to a VI not in memory or to something that is not a VI, this
property returns Not a Refnum. You can use this reference with the VI properties.

Syntax

object.VINoLoad
Data Type

VIObjRef

VisibleInTreeVisibleInTree

If TRUE, indicates that the LabVIEW Project Explorer window is visible and ancestors of
the LabVIEW project item are expanded in the Project Explorer window up to the root
of the project item.

Syntax

object.VisibleInTree
Data Type

Boolean

LibraryLibrary PropertiesProperties andand MethodsMethods

This book contains the property and method reference information for the Library
class.

                                                    © National Instruments 6311

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6311 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6312 ordinal=6312 -->
## Property and Method Reference

Property and Method Reference

       LibraryLibrary MethodsMethods (ActiveX)(ActiveX)

      Use these methods to configure LabVIEW project libraries.

     Methods

       Method                       Description

         DeleteLibTag                  Deletes a tag from the LabVIEW project library.


                                      Disconnects a LabVIEW project library that is a sublibrary of        DisconnectFromLibrary                                     another project library from the owning project library.


         GetLibTag                      Retrieves a tag set on the LabVIEW project library.


                                     Returns the lock state of the LabVIEW project library and indicates
        GetLockState                whether the password for the project library is in the password
                                       cache.


                                        Retrieves the access scope for an item that the LabVIEW project        GetSourceScope                                             library owns, such as public or private access.


                                        Retrieves a list of names for all tags set on the LabVIEW project
       GetTagNames
                                               library.


                                        Displays this library in a Project Explorer window. If the library is
                                       already in a Project Explorer window, this method displays the
                                         Project Explorer window and sets focus to the library item in the
                                  window. If the library is already in a stand-alone project library
         HiliteInProjectWindow
                               window for which the library is the root item, this method displays
                                      the stand-alone project library window. If the library is not in any
                                  window, this method opens a stand-alone project library window
                                       containing the library.


6312   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6312 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6313 ordinal=6313 -->
## Property and Method Reference

Property and Method Reference


 Method                       Description

 Save                        Saves the LabVIEW project library file.


 SaveCopy                   Saves a copy of the LabVIEW project library file.


                            Saves a copy of the project library and all items within the project
                                   library that is readable by LabVIEW 8.0 and later. This method is SaveForPrevious                                  similar to the LabVIEW Version section on the Save for Previous
                               Version dialog box.


 SetLibTag                     Sets a tag on the LabVIEW project library.


                               Sets the level of editing permission for a LabVIEW project library, SetLockState                                including the password.


                               Sets the access scope of an item that the LabVIEW project library SetSourceScope                            owns, such as public or private access.


                               Sets the access scope of an item that the LabVIEW project library
                            owns, such as public or private access. If the item is a dynamic SetSourceScopeAndPropagate                               dispatch VI, LabVIEW also changes the scope of other
                              implementations.

DeleteLibTagDeleteLibTag

Deletes a tag from the LabVIEW project library.

Syntax

object.DeleteLibTag(tagName, [itemRef])


                                                    © National Instruments 6313

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6313 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6314 ordinal=6314 -->
## Property and Method Reference

Property and Method Reference

     Parameters

      Name    Type         Description

       tagName  String      Name of the tag. Use the GetTagNames method to retrieve the tag names.

        itemRef   ProjectItem*  Reference to the Project Library Item.

     Return Value

      Boolean
   DisconnectFromLibraryDisconnectFromLibrary

       Disconnects a LabVIEW project library that is a sublibrary of another project library
      from the owning project library.

     Syntax

     object.DisconnectFromLibrary()
     Return Value

      none
   GetLibTagGetLibTag

       Retrieves a tag set on the LabVIEW project library.

     Syntax

     object.GetLibTag(tagName, [value], [isPersistent],
     [itemRef])
     Parameters

      Name      Type         Description

       tagName    String      Name of the tag. Use the GetTagNames method to retrieve the tag

6314   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6314 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6315 ordinal=6315 -->
## Property and Method Reference

Property and Method Reference


 Name      Type         Description

                       names.

 value        variant       Returns the value of the tag.

                         Returns TRUE if LabVIEW saves the tag information when you save the isPersistent Boolean*                       LabVIEW project. Returns FALSE otherwise.

 itemRef     ProjectItem* Reference to the Project Library Item.

Return Value

Boolean
GetLockStateGetLockState

Returns the lock state of the LabVIEW project library and indicates whether the
password for the project library is in the password cache.

This method is similar to the Protection box on the General Settings page of the
Project Library Properties dialog box.

Syntax

object.GetLockState([pwdInCache])
Parameters

 Name       Type           Description

 pwdInCache  Boolean by ref  Indicates whether the password is currently in the password cache.

Return Value

VILockStateEnum


                                                    © National Instruments 6315

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6315 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6316 ordinal=6316 -->
## Property and Method Reference

Property and Method Reference

   GetSourceScopeGetSourceScope

       Retrieves the access scope for an item that the LabVIEW project library owns, such as
       public or private access.

     Syntax

     object.GetSourceScope(sourceRef, [inherited])
     Parameters

      Name    Type         Description

                                Reference to the item in the project library for which you want to retrieve         sourceRef  ProjectItem*                                 scope.

         inherited  Boolean      Indicates whether the specified item is inherited.

     Return Value

      LibraryItemScopeEnum
   GetTagNamesGetTagNames

       Retrieves a list of names for all tags set on the LabVIEW project library.

     Syntax

     object.GetTagNames([itemRef])
     Parameters

      Name       Type                 Description

        itemRef       ProjectItem*         Reference to the Project Library Item.

     Return Value

       Array of strings

6316   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6316 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6317 ordinal=6317 -->
## Property and Method Reference

Property and Method Reference

HiliteInProjectWindowHiliteInProjectWindow

Displays this library in a Project Explorer window. If the library is already in a Project
Explorer window, this method displays the Project Explorer window and sets focus to
the library item in the window. If the library is already in a stand-alone project library
window for which the library is the root item, this method displays the stand-alone
project library window. If the library is not in any window, this method opens a stand-
alone project library window containing the library.

Syntax

object.HiliteInProjectWindow()
Return Value

none
SaveSave

Saves the LabVIEW project library file.

Syntax

object.Save([path])
Parameters

 Name      Type        Description

 path         String       Path to the LabVIEW project library file.

Return Value

none


                                                    © National Instruments 6317

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6317 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6318 ordinal=6318 -->
## Property and Method Reference

Property and Method Reference

   SaveCopySaveCopy

      Saves a copy of the LabVIEW project library file.

     Syntax

     object.SaveCopy(destDir, [newName], [newLibPath])
     Parameters

      Name       Type   Description

         destDir        String   Specifies the destination directory for the copy of the project library.

      newName     String   Specifies the name of the copy of the project library.

        newLibPath   String  Returns the path to the copy of the project library.

     Return Value

      none
   SaveForPreviousSaveForPrevious

      Saves a copy of the project library and all items within the project library that is
       readable by LabVIEW 8.0 and later. This method is similar to the LabVIEW Version
       section on the Save for Previous Version dialog box.

           Note The LabVIEW Datalogging and Supervisory Control Module supports
                 this method in the Run-Time Engine.

     Syntax

     object.SaveForPrevious(Path, [Version])


6318   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6318 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6319 ordinal=6319 -->
## Property and Method Reference

Property and Method Reference

Parameters

 Name  Type  Description

 Path    path  Path to the directory where you want to save the LabVIEW project library.

                Version of LabVIEW for which you want to save. Wire the version number, such as
 Version  string 8.6 or 2009, to the Target Version input. The default is the immediately previous
                 version.

Return Value

none
SetLibTagSetLibTag

Sets a tag on the LabVIEW project library.

Syntax

object.SetLibTag(tagName, [value], [isPersistent],
[itemRef])
Parameters

 Name      Type         Description

                   Name of the tag. Use the GetTagNames method to retrieve the tag tagName    String
                       names.

 value        variant       Specifies the value of the tag.

                         Returns TRUE if LabVIEW saves the tag information when you save the
 isPersistent Boolean*
                       LabVIEW project. Returns FALSE otherwise.

 itemRef     ProjectItem* Reference to the Project Library Item.

Return Value

none


                                                    © National Instruments 6319

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6319 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6320 ordinal=6320 -->
## Property and Method Reference

Property and Method Reference

    SetLockStateSetLockState

       Sets the level of editing permission for a LabVIEW project library, including the
      password.

       This method is similar to the Protection box on the General Settings page of the
      LabVIEW Project Library Properties dialog box.

     Syntax

     object.SetLockState(lockState, [Interactive], [Password],
     [putInCache])
     Parameters

      Name      Type             Description

         lockState   VILockStateEnum Lock state.

                                          Specifies whether to display a dialog box that prompts you to          Interactive  Boolean                                  change the lock state. The default is FALSE.

                                                               If lockState is Password-protected, Password is the new password.
        Password    String                    If you are changing lockState from Password-protected, Password
                                                    is the old password. The default is an empty string.

                                                               If lockState is Password-protected, putinCache specifies whether
        putInCache Boolean                                        to place the new password in the cache. The default is FALSE.

     Return Value

      none
   SetSourceScopeSetSourceScope

       Sets the access scope of an item that the LabVIEW project library owns, such as public
       or private access.

       This method is similar to the Access Scope box on the Item Settings page of the


6320   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6320 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6321 ordinal=6321 -->
## Property and Method Reference

Property and Method Reference

LabVIEW Project Library Properties dialog box.

Syntax

object.SetSourceScope(sourceRef, [scope])
Parameters

 Name    Type                   Description

                                  Reference to the item in the project library for which you want sourceRef  ProjectItem*
                                    to set scope.

                                      Specifies the access setting for the item.

                                                       • Public—The item is visible when users view the project
                                                library. Other VIs and applications can call public VIs.
 scope     LibraryItemScopeEnum     • Private—The item does not appear visible when users
                                    view the project library or palettes if you lock the project
                                                library. Other VIs and applications that the project library
                                   does not own cannot call a private VI.


Return Value

none
SetSourceScopeAndPropagateSetSourceScopeAndPropagate

Sets the access scope of an item that the LabVIEW project library owns, such as public
or private access. If the item is a dynamic dispatch VI, LabVIEW also changes the scope
of other implementations.

Syntax

object.SetSourceScopeAndPropagate(source ref, scope)


                                                    © National Instruments 6321

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6321 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6322 ordinal=6322 -->
## Property and Method Reference

Property and Method Reference

     Parameters

      Name  Type        Description

        source Refnum      Contains a reference to the item in the project library for which you want to
          ref     control       set or retrieve access.

                                Specifies the access setting for the item.

                                              •  invalid scope—The item is an invalid value. The item is visible whenever
                                 the read function receives an error and causes an error to occur if you
                                pass this item to a write function.
                                              • public—The item is visible when users view the project library. Other VIs
                            and applications can call public VIs.              Enumerated
        scope                         • private—The item does not appear visible when users view the project                type control                                       library or palettes if you lock the project library. Other VIs and
                                   applications that the project library does not own cannot call a private
                                            VI.
                                              • protected—The item is visible to other VIs in the same class or a
                               descendant class.
                                              • community—The item is visible when users view the project library.


     Return Value

      none

       LibraryLibrary PropertiesProperties (ActiveX)(ActiveX)

      Use these properties to configure LabVIEW project libraries.

      Properties

        Property                        Description

                                            Specifies the name of the computer where the alarms and
        AlarmsEventsDBComputer
                                        events database resides.


        AlarmsEventsDBName            Specifies the name of the database where the LabVIEW Shared


6322   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6322 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6323 ordinal=6323 -->
## Property and Method Reference

Property and Method Reference


Property                        Description

                                  Variable Engine logs alarms and events.


                                   Specifies the file path to the database where the LabVIEW SharedAlarmsEventsDBPath                                  Variable Engine logs alarms and events.


AlarmsEventsEnable            Enables alarms and events logging capability if set to TRUE.


                                 Sets the alarms and events database to be the same as the
AlarmsEventsUseDataLoggingDB database that logs data. If set to TRUE, LabVIEW ignores
                                 properties set on the AlarmsEvents database.


                                 Sets or returns whether LabVIEW stores the library in theContainsCompiledCode                             compiled object cache.


DataLoggingDBComputer         Specifies the name of the computer where the database resides.


                                   Specifies the name of the database where the LabVIEW SharedDataLoggingDBName
                                  Variable Engine logs data.


                                   Specifies the file path to the database where the LabVIEW Shared
DataLoggingDBPath
                                  Variable Engine logs data.


DataLoggingEnable             Enables data logging capability if set to TRUE.


                                 Sets the lifespan (in days) of the logged data in the database. If
DataLoggingLifespan            value is 0, then data is always available, otherwise the database
                             can destroy data after the number of specified days.


                                                    © National Instruments 6323

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6323 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6324 ordinal=6324 -->
## Property and Method Reference

Property and Method Reference


        Property                        Description

                                            Specifies the description of the LabVIEW project library for the
         Description                                        Context Help window.


                                       Path or symbolic path to an HTML file (.htm or .html) or
        HelpDocumentPath             compiled help file (.chm or .hlp) to which the LabVIEW project
                                               library is linked.


                                        Index keyword or HTML filename for a topic in the compiled help
                                                         file to which the LabVIEW project library is linked. To link to a
        HelpDocumentTag                                  bookmark within an HTML file, add # followed by the name of
                                        the bookmark to the end of the filename.


        LocalName                  The localized name of the item.


        QualifiedName                 Returns the qualified name of the library.


         Version                     The version number of the LabVIEW project library.

   AlarmsEventsDBComputerAlarmsEventsDBComputer

       Specifies the name of the computer where the alarms and events database resides.

     Syntax

     object.AlarmsEventsDBComputer
     Data Type

        string


6324   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6324 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6325 ordinal=6325 -->
## Property and Method Reference

Property and Method Reference

AlarmsEventsDBNameAlarmsEventsDBName

Specifies the name of the database where the LabVIEW Shared Variable Engine logs
alarms and events.

Syntax

object.AlarmsEventsDBName
Data Type

string
AlarmsEventsDBPathAlarmsEventsDBPath

Specifies the file path to the database where the LabVIEW Shared Variable Engine logs
alarms and events.

Syntax

object.AlarmsEventsDBPath
Data Type

string
AlarmsEventsEnableAlarmsEventsEnable

Enables alarms and events logging capability if set to TRUE.

Syntax

object.AlarmsEventsEnable
Data Type

Boolean


                                                    © National Instruments 6325

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6325 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6326 ordinal=6326 -->
## Property and Method Reference

Property and Method Reference

   AlarmsEventsUseDataLoggingDBAlarmsEventsUseDataLoggingDB

       Sets the alarms and events database to be the same as the database that logs data. If
       set to TRUE, LabVIEW ignores properties set on the AlarmsEvents database.

     Syntax

     object.AlarmsEventsUseDataLoggingDB
     Data Type

      Boolean
   ContainsCompiledCodeContainsCompiledCode

       Sets or returns whether LabVIEW stores the library in the compiled object cache.

           If TRUE, LabVIEW does notstore the library in the compiled object cache. In this case,
      you must save the library every time you modify a member of the library or when you
       migrate the library to a new version of LabVIEW. If FALSE, LabVIEW stores the library in
       the compiled object cache so you must save the library only when you change the
        library itself.

       This property is similar to the Separate compiled code from source file option on the
       General Settings page of the Project Library Properties dialog box.

     Syntax

     object.ContainsCompiledCode
     Data Type

      Boolean
   DataLoggingDBComputerDataLoggingDBComputer

       Specifies the name of the computer where the database resides.

6326   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6326 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6327 ordinal=6327 -->
## Property and Method Reference

Property and Method Reference

Syntax

object.DataLoggingDBComputer
Data Type

string
DataLoggingDBNameDataLoggingDBName

Specifies the name of the database where the LabVIEW Shared Variable Engine logs
data.

Syntax

object.DataLoggingDBName
Data Type

string
DataLoggingDBPathDataLoggingDBPath

Specifies the file path to the database where the LabVIEW Shared Variable Engine logs
data.

Syntax

object.DataLoggingDBPath
Data Type

string
DataLoggingEnableDataLoggingEnable

Enables data logging capability if set to TRUE.


                                                    © National Instruments 6327

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6327 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6328 ordinal=6328 -->
## Property and Method Reference

Property and Method Reference

     Syntax

     object.DataLoggingEnable
     Data Type

      Boolean
   DataLoggingLifespanDataLoggingLifespan

       Sets the lifespan (in days) of the logged data in the database. If value is 0, then data is
      always available, otherwise the database can destroy data after the number of
       specified days.

      The database only discards data if new data is logged. This property affects all data
      from the LabVIEW project library stored in the database, not just the most recent data.
       For example, if you set this property to four days and you have three days of data, the
      database does not destroy any data. However, if you set this same property to two
      days from four days and you have three days of data, the database can destroy any
       data collected more than two days ago.

     Syntax

     object.DataLoggingLifespan
     Data Type

      Long
    DescriptionDescription

       Specifies the description of the LabVIEW project library for the Context Help window.

           If you want to display a carriage return in the LabVIEW Context Help window, you must
       separate paragraphs with two carriage returns.


6328   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6328 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6329 ordinal=6329 -->
## Property and Method Reference

Property and Method Reference

Syntax

object.Description
Data Type

string
HelpDocumentPathHelpDocumentPath

Path or symbolic path to an HTML file (.htm or .html) or compiled help file (.chm or
.hlp) to which the LabVIEW project library is linked.

If the path is to a compiled help file, use the HelpDocumentTag property to determine
the specific topic in that help file.

This property is similar to the Help path text box on the Documentation page of the
LabVIEW Project Library Properties dialog box.

Syntax

object.HelpDocumentPath
Data Type

string
HelpDocumentTagHelpDocumentTag

Index keyword or HTML filename for a topic in the compiled help file to which the
LabVIEW project library is linked. To link to a bookmark within an HTML file, add #
followed by the name of the bookmark to the end of the filename.

Use this property only when HelpDocumentPath is a path to a compiled help file
(.chm or .hlp).

For .chm files, this property can be an HTML filename or index keyword. For .hlp
files, this property can be an index keyword.

                                                    © National Instruments 6329

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6329 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6330 ordinal=6330 -->
## Property and Method Reference

Property and Method Reference

       This property is similar to the Help tag text box on the Documentation page of the
      LabVIEW Project Library Properties dialog box.

     Syntax

     object.HelpDocumentTag
     Data Type

        string
   LocalNameLocalName

      The localized name of the item.

       This property is similar to the Localized Name text box on the Documentation page of
       the LabVIEW Project Library Properties dialog box.

     Syntax

     object.LocalName
     Data Type

        string
   QualifiedNameQualifiedName

       Returns the qualified name of the library.

     Syntax

     object.QualifiedName
     Data Type

       String


6330   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6330 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6331 ordinal=6331 -->
## Property and Method Reference

Property and Method Reference

VersionVersion

The version number of the LabVIEW project library.

This property is similar to the Version Number component on the General Settings
page of the LabVIEW Project Library Properties dialog box.

Syntax

object.Version
Data Type

LVLibraryVersion

XInterfaceLibraryXInterfaceLibrary PropertiesProperties andand MethodsMethods

This book contains the property and method reference information for the
XInterfaceLibrary class.
XInterfaceLibraryXInterfaceLibrary MethodsMethods (ActiveX)(ActiveX)

Methods

 Method           Description

 AddAbility         Creates a new ability of the specified type.


 AddMethod        Creates a new method.


 NewProperty      Creates a new property folder and returns a reference to it.


                                                    © National Instruments 6331

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6331 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6332 ordinal=6332 -->
## Property and Method Reference

Property and Method Reference

    AddAbilityAddAbility

       Creates a new ability of the specified type.

     Syntax

     object.AddAbility(name, [viPath], [folder])
     Parameters

      Name Type         Description

       name  String      Name for the ability you want to create.

                                               If you specify viPath, LabVIEW uses an existing VI for the ability. If you do not         viPath path                               specify viPath, LabVIEW creates a new VI for the ability.

         folder  ProjectItem*  Creates the ability in the specified folder.

     Return Value

       ProjectItem*
   AddMethodAddMethod

       Creates a new method.

     Syntax

     object.AddMethod([viPath], [folder])
     Parameters

      Name Type         Description

                                               If you specify viPath, LabVIEW uses an existing VI for the method. If you do
         viPath path
                            not specify viPath, LabVIEW creates a new VI for the method.

         folder  ProjectItem*  Creates the method in the specified folder.


6332   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6332 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6333 ordinal=6333 -->
## Property and Method Reference

Property and Method Reference

Return Value

ProjectItem*
NewPropertyNewProperty

Creates a new property folder and returns a reference to it.

Syntax

object.NewProperty(name, folder)
Parameters

 Name    Type              Description

 name     String         Name of the new property folder to create.

 folder    ProjectItem*       Folder in which to create the new property folder.

Return Value

PropertyFolder*

PropertyFolderPropertyFolder PropertiesProperties andand MethodsMethods

This book contains the property and method reference information for the
PropertyFolder class.

PropertyFolderPropertyFolder MethodsMethods (ActiveX)(ActiveX)

Methods

 Method        Description

                Creates a new read or write property VI if you do not set viPath. If you set viPath,
 AddPropertyVI
              LabVIEW uses an existing VI as a property VI.


                                                    © National Instruments 6333

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6333 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6334 ordinal=6334 -->
## Property and Method Reference

Property and Method Reference

   AddPropertyVIAddPropertyVI

       Creates a new read or write property VI if you do not set viPath. If you set viPath,
      LabVIEW uses an existing VI as a property VI.

     Syntax

     object.AddPropertyVI([read], [viPath])
     Parameters

      Name Type     Description

                                         If TRUE, creates a read property VI. If FALSE, creates a write property VI. The        read   Boolean                           default is TRUE.

                        Path to the property VI. This parameter is optional. If you specify a path, LabVIEW         viPath path                        uses an existing VI as a property VI.

     Return Value

       ProjectItem*

      XPropertyFolderXPropertyFolder PropertiesProperties andand MethodsMethods

       This book contains the property and method reference information for the
       XPropertyFolder class.
    XPropertyFolderXPropertyFolder PropertiesProperties (ActiveX)(ActiveX)
      Properties

        Property         Description

         Description       Sets or gets the description of the property folder.


6334   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6334 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6335 ordinal=6335 -->
## Property and Method Reference

Property and Method Reference


 Property         Description

 HelpTag          Sets or gets the help tag of the property folder.


 Identifier         Sets or gets the property identifier of the property folder.


 LongName       Sets or gets the long name of the property folder.

DescriptionDescription

Sets or gets the description of the property folder.

Syntax

object.Description
Data Type

string
HelpTagHelpTag

Sets or gets the help tag of the property folder.

Syntax

object.HelpTag
Data Type
string


                                                    © National Instruments 6335

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6335 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6336 ordinal=6336 -->
## Property and Method Reference

Property and Method Reference

    IdentifierIdentifier

       Sets or gets the property identifier of the property folder.

     Syntax

     object.Identifier
     Data Type
        string
   LongNameLongName

       Sets or gets the long name of the property folder.

     Syntax

     object.LongName
     Data Type
        string
      TargetItemTargetItem PropertiesProperties andand MethodsMethods

       This book contains the property and method reference information for the TargetItem
        class.

      TargetItemTargetItem MethodsMethods (ActiveX)(ActiveX)

     Methods

       Method              Description

                              Refreshes Dependencies under this target in the LabVIEW Project Explorer
        RefreshDependencies window. You also can use the Project Explorer window to refresh
                             dependencies.


6336   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6336 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6337 ordinal=6337 -->
## Property and Method Reference

Property and Method Reference

RefreshDependenciesRefreshDependencies

Refreshes Dependencies under this target in the LabVIEW Project Explorer window.
You also can use the Project Explorer window to refresh dependencies.

Syntax

object.RefreshDependencies()
Return Value

none

TargetItemTargetItem PropertiesProperties (ActiveX)(ActiveX)

In the following topics, an asterisk (*) at the end of a data type name indicates that the
property is a pointer.

Properties

 Property           Description

                    Returns a reference to Build Specifications under the current target in the
 BuildSpecifications LabVIEW Project Explorer window. You can use this reference with the
                    ProjectItem properties.


                    Returns a reference to Dependencies under the current target in the LabVIEW
 Dependencies       Project Explorer window. You can use this reference with the ProjectItem
                      properties.

BuildSpecificationsBuildSpecifications

Returns a reference to Build Specifications under the current target in the LabVIEW
Project Explorer window. You can use this reference with the ProjectItem properties.


                                                    © National Instruments 6337

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6337 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6338 ordinal=6338 -->
## Property and Method Reference

Property and Method Reference

     Syntax

     object.BuildSpecifications
     Data Type

       ProjectItem*
   DependenciesDependencies

       Returns a reference to Dependencies under the current target in the LabVIEW Project
       Explorer window. You can use this reference with the ProjectItem properties.

     Syntax

     object.Dependencies
     Data Type

       ProjectItem*

      VIVI PropertiesProperties andand MethodsMethods

       This book contains the property and method reference information for the VI class.

       VIVI MethodsMethods (ActiveX)(ActiveX)

      A VirtualInstrument object exports methods that affect a given VI. A VirtualInstrument
       object is instantiated by invoking the GetVIReference method on the Application
       object.

           Note Methods parameters denoted by [] are optional for that method.

       Refer to the ActiveX Enumerations for more information about enumerations used in
       various properties.


6338   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6338 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6339 ordinal=6339 -->
## Property and Method Reference

Property and Method Reference

Methods

 Method                       Description

 Abort                        Aborts the VI execution.


 Call                              Calls the VI as a subVI.


                                  Calls the VI as a subVI. Optionally, you can open the front panel of
 Call2                         the VI and close it after the call is over. You also can suspend the VI
                        when called.


                                 Specifies whether to automatically center the LabVIEW front panel CenterFrontPanel
                         window on the computer screen.


 CloseFrontPanel               Closes the LabVIEW front panel window.


 DisconnectFromLibrary        Disconnects the VI from the owning LabVIEW project library.


                               Exports the following strings about VI and LabVIEW front panel
                                objects to a tagged text file: VI name and description, object
                               caption labels, object free labels, default data (string, table, path,
                          and array default data), private data (listbox item names, table row
 ExportVIStrings
                          and column headers, graph plot names, graph cursor names, graph
                              annotation names, and tab control page captions), and
                            polymorphic VI data (instance names in the polymorphic VI and
                                 selector shortcut menus).


 FPGetRuntimePos             Returns the position of the LabVIEW window at run time.


 FPRunTimePosRunCentered    Sets a VI to center its front panel every time the VI runs.


                                                    © National Instruments 6339

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6339 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6340 ordinal=6340 -->
## Property and Method Reference

Property and Method Reference


       Method                       Description

                                       Sets a custom position for the VI to move its front panel to every
       FPRunTimePosRunCustom                                    time the VI runs.


       FPRunTimePosRunMax         Sets a VI to maximize its front panel every time the VI runs.


       FPRunTimePosRunMin         Sets a VI to minimize its front panel every time the VI runs.


       FPRunTimePosRunUnchanged  Sets the VI to not move its front panel when the VI runs.


                                      Gets the value of the named LabVIEW control or indicator as
         GetControlValue                variant data. Use the LabVIEW Variant to Data function to convert
                                      the data to another LabVIEW data type.


                                     Returns the lock state of the VI and indicates whether the password
        GetLockState                                            for the VI is in the password cache.


                                        This method returns the names and paths of the VI dependencies
                                          of a VI. You can use this method to return a specific subset of the
        GetVIDependencies              total set of VI dependencies of a VI. This method does not return
                                      non-VI dependencies, such as project libraries, XControls, classes,
                                and statecharts.


                                     Imports the following strings about VI and LabVIEW front panel
                                        objects from a tagged text file: VI name and description, object
                                      caption labels, object free labels, default data (string, table, path,
                                and array default data), private data (listbox item names, table row
         ImportVIStrings
                                and column headers, graph plot names, graph cursor names, graph
                                      annotation names, and tab control page captions), and
                                    polymorphic VI data (instance names in the polymorphic VI and
                                          selector shortcut menus).


6340   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6340 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6341 ordinal=6341 -->
## Property and Method Reference

Property and Method Reference


Method                       Description

                          Changes the defaults of all controls on the LabVIEW front panel to
MakeCurValueDefault                          be the current values. This method is available only in edit mode.


                         Opens the LabVIEW front panel window. If the front panel is
                              already open, this method changes the state of the front panel
                        window to the state you wire to this method. Use the
OpenFrontPanel              CloseFrontPanel method to close the front panel window.

                           You also can use the FPState property to set the state of a front
                             panel window that is already open.


                                 Prints just the LabVIEW front panel to the current printer. You
PrintPanel                   cannot use this method to print a block diagram, list of controls, or
                            polymorphic VI front panel.


                            Saves the VI information to an HTML file and saves the graphics inPrintVIToHTML
                                external files.


                                 Prints the VI information to a printer. If you use this method in a
PrintVIToPrinter               stand-alone application or DLL, LabVIEW prints only the front
                               panel.


PrintVIToRTF                 Saves the VI information to an RTF file.


                            Saves the VI information to a text file. You cannot save the icon,
PrintVIToText                 connector pane, front panel, block diagram, subVI icons, and VI
                               hierarchy to text.


                          Changes the current values of all controls on the LabVIEW front
ReinitializeAllToDefault
                             panel to their defaults.


                                                    © National Instruments 6341

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6341 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6342 ordinal=6342 -->
## Property and Method Reference

Property and Method Reference


       Method                       Description

         Revert                        Discards changes and reloads a VI from disk.


                                           Starts the VI execution, similar to the Run button in LabVIEW. This
                                method is different than calling a VI because it uses the current
                                       values of all front panel controls for execution rather than using
                                     data passed in through parameters. This method also ignores the
       Run                                  ShowFPOnCall
                                      property of a VI and the
                                         CloseFPAfterCall
                                         property. You cannot use this method to run a VI that is already
                                      reserved for execution by another VI.


        SaveForPrevious             Saves a copy of the VI that is readable by LabVIEW 8.0 and later.


                                    Saves a VI and synchronizes the VI with the edited version in other        SaveInstrument
                                        application instances before saving.


                                    Saves the LabVIEW run-time menu to a file specified by filePath.
       SaveRunTimeMenu            This method works only when the VI is running. It saves only menu
                                      items with valid tags.


         SetControlValue               Sets the value of a named LabVIEW control or indicator.


                                       Sets the lock state of a VI. If Interactive is FALSE (default), you can
                                    use Password to unlock a password-protected VI or set the
         SetLockState                password of an unprotected VI. If Interactive is TRUE, LabVIEW
                                       ignores Password and displays a dialog box that prompts you to
                                  change the lock state.


         SetVIIcon                      Sets the image of a VI icon from a file.


6342   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6342 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6343 ordinal=6343 -->
## Property and Method Reference

Property and Method Reference

AbortAbort

Aborts the VI execution.

This method is similar to the Abort Execution button on the LabVIEW toolbar.

Syntax

object.Abort()
Return Value

Boolean

CallCall

Calls the VI as a subVI.

Syntax

object.Call([paramNames], [paramVals])
Parameters

 Name       Type    Description

               array of
                  Names of the LabVIEW front panel objects that act as input and output paramNames  strings                      parameters to the call.
             by ref

                        Input values for the input parameters and return values from the output
               array of  parameters in the order in which the names were specified in
 paramVals     variants paramNames. Designates the front panel object values for the input
             by ref    parameters. The values of parameters can be numeric, Boolean, string, or
                           array. A cluster in LabVIEW is represented as an array of variants in ActiveX.

Return Value

none


                                                    © National Instruments 6343

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6343 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6344 ordinal=6344 -->
## Property and Method Reference

Property and Method Reference

       Call2Call2

        Calls the VI as a subVI. Optionally, you can open the front panel of the VI and close it
        after the call is over. You also can suspend the VI when called.

     Syntax

     object.Call2([Param Names], [Param Values], [Open Front
     Panel], [Close Front Panel After Call], [Suspend On Call],
     [Bring App To Front])
     Parameters

      Name   Type     Description

                   array of       Param          Names of the LabVIEW front panel objects that act as input and output                     strings
       Names            parameters to the call.                by ref

                            Input values for the input parameters and return values from the output
                   array of  parameters in the order in which the names were specified in paramNames.       Param                    variants  Designates the front panel object values for the input parameters. The values
         Values                by ref    of parameters can be numeric, Boolean, string, or array. A cluster in LabVIEW is
                           represented as an array of variants in ActiveX.

       Open
         Front    Boolean Opens the front panel of the VI.
        Panel

         Close
         Front                            Closes the front panel of the VI after the call if the front panel was not already
        Panel    Boolean
                             closed.
          After
          Call

        Suspend
                 Boolean Suspends, or pauses the execution of, the VI on call.
      On Call

         Bring
       App To   Boolean  Brings the application to the front.
         Front


6344   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6344 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6345 ordinal=6345 -->
## Property and Method Reference

Property and Method Reference

Return Value

none

CenterFrontPanelCenterFrontPanel

Specifies whether to automatically center the LabVIEW front panel window on the
computer screen.

Syntax

object.CenterFrontPanel()
Return Value

none

CloseFrontPanelCloseFrontPanel

Closes the LabVIEW front panel window.

Use the OpenFrontPanel method to open a front panel window.

Syntax

object.CloseFrontPanel()
Return Value

none

DisconnectFromLibraryDisconnectFromLibrary

Disconnects the VI from the owning LabVIEW project library.

Syntax

object.DisconnectFromLibrary()


                                                    © National Instruments 6345

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6345 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6346 ordinal=6346 -->
## Property and Method Reference

Property and Method Reference

     Return Value

      none

       ExportVIStringsExportVIStrings

       Exports the following strings about VI and LabVIEW front panel objects to a tagged text
          file: VI name and description, object caption labels, object free labels, default data
        (string, table, path, and array default data), private data (listbox item names, table row
      and column headers, graph plot names, graph cursor names, graph annotation names,
      and tab control page captions), and polymorphic VI data (instance names in the
      polymorphic VI and selector shortcut menus).

     Syntax

     object.ExportVIStrings(stringFile, [interactive],
     [logFile], [captions], [diagram])
     Parameters

      Name     Type     Description

                            Path of the VI strings file including the filename. If you do not enter a          stringFile   String                              filename, set interactive to TRUE so the user can set the VI strings filename.

                                Specifies whether to display the file dialog box to select the name of the VI          interactive Boolean                                 strings file. The default value is FALSE.

                            Path of the log file created to list errors that occurred while exporting VI          logFile      String                                 strings to a tagged text file. The default is no logging.

                                Specifies whether control captions should be automatically created. The
         captions   Boolean
                               default value is FALSE.

        diagram   Boolean  Specifies whether to export block diagram strings. The default value is FALSE.

     Return Value

      none


6346   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6346 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6347 ordinal=6347 -->
## Property and Method Reference

Property and Method Reference

FPGetRuntimePosFPGetRuntimePos

Returns the position of the LabVIEW window at run time.

For single-pane front panels, minimum size refers to the content area of that pane, not
including the scroll bars. For multi-pane front panels, minimum size refers to the entire
front panel, including any visible scroll bars.

Syntax

object.FPGetRuntimePos([type], [position], [size],
[monitor], [useCurPos], [useCurSize])
Parameters

 Name     Type           Description

                           Returns whether the front panel is unchanged, centered, maximized, type       FPRuntimePos                           minimized, or has a custom setting.

                       A pair of numbers that represents the coordinates of the top left             Array of position                   corner of the front panel window. Each element in the pair occupies             variants
                        one element of an array that contains two elements.

                       A pair of numbers that represents the height and width of the front             Array of
 size                      panel window. Each element in the pair occupies one element of an             variants                             array that contains two elements.

                              Specifies the monitor on which the front panel window appears, if you
                         have multiple monitors. The value 0 is the primary monitor and is the
                             default value. If you specify a value other than 0, the VI runs on that
 monitor    short          monitor. If you specify a monitor number greater than the number of
                          monitors on the system, or if you specify a negative number, LabVIEW
                             returns an error. The monitor number corresponds to the video card
                        you plug the monitor in to.

                           Returns the value of the Use Current Position checkbox in the
 useCurPos  Boolean
                     Window Run-Time Position dialog box in LabVIEW.

                           Returns the value of the Use Current Size checkbox in the Window
 useCurSize Boolean
                        Run-Time Position dialog box in LabVIEW.


                                                    © National Instruments 6347

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6347 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6348 ordinal=6348 -->
## Property and Method Reference

Property and Method Reference

     Return Value

      FPRunTimePosEnum

      FPRunTimePosRunCenteredFPRunTimePosRunCentered

       Sets a VI to center its front panel every time the VI runs.

       For single-pane front panels, minimum size refers to the content area of that pane, not
       including the scroll bars. For multi-pane front panels, minimum size refers to the entire
       front panel, including any visible scroll bars.

     Syntax

     object.FPRunTimePosRunCentered([monitor], [size])
     Parameters

      Name   Type    Description

                             Specifies the monitor on which the front panel window appears, if you have
                           multiple monitors. The value 0 is the primary monitor and is the default value. If
                       you specify a value other than 0, the VI runs on that monitor. If you specify a
        monitor  short                         monitor number greater than the number of monitors on the system, or if you
                             specify a negative number, LabVIEW returns an error. The monitor number
                         corresponds to the video card you plug the monitor in to.

                      A pair of numbers that represents the height and width of the front panel                  Array of          size             window. Each element in the pair occupies one element of an array that
                   variants                           contains two elements.

     Return Value

      none

     FPRunTimePosRunCustomFPRunTimePosRunCustom

       Sets a custom position for the VI to move its front panel to every time the VI runs.

       For single-pane front panels, minimum size refers to the content area of that pane, not


6348   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6348 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6349 ordinal=6349 -->
## Property and Method Reference

Property and Method Reference

including the scroll bars. For multi-pane front panels, minimum size refers to the entire
front panel, including any visible scroll bars.

You can use this method with text-based programming languages. Refer to the
following example of a code snippet for using this method while working in C#:

object[] pos = new object[2];

object[] size = new object[2];

pos[0] = 100; //top

pos[1] = 100; //left

size[0] = 900; // height

size[1] = 300; // width

vi.FPRunTimePosRunCustom(pos, size);

Syntax

object.FPRunTimePosRunCustom([position], [size])
Parameters

 Name   Type    Description

                A pair of numbers that represents the coordinates of the top left corner of the
          Array of
 position           front panel window. Each element in the pair occupies one element of an array
           variants
                    that contains two elements.

                A pair of numbers that represents the height and width of the front panel
          Array of
 size             window. Each element in the pair occupies one element of an array that
           variants
                   contains two elements.

Return Value

none


                                                    © National Instruments 6349

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6349 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6350 ordinal=6350 -->
## Property and Method Reference

Property and Method Reference

     FPRunTimePosRunMaxFPRunTimePosRunMax

       Sets a VI to maximize its front panel every time the VI runs.

     Syntax

     object.FPRunTimePosRunMax([monitor])
     Parameters

      Name   Type  Description

                          Specifies the monitor on which the front panel window appears, if you have
                         multiple monitors. The value 0 is the primary monitor and is the default value. If
                     you specify a value other than 0, the VI runs on that monitor. If you specify a        monitor  short                       monitor number greater than the number of monitors on the system, or if you
                          specify a negative number, LabVIEW returns an error. The monitor number
                       corresponds to the video card you plug the monitor in to.

     Return Value

      none

     FPRunTimePosRunMinFPRunTimePosRunMin

       Sets a VI to minimize its front panel every time the VI runs.

     Syntax

     object.FPRunTimePosRunMin([monitor])
     Parameters

      Name   Type  Description

                          Specifies the monitor on which the front panel window appears, if you have
                         multiple monitors. The value 0 is the primary monitor and is the default value. If
                     you specify a value other than 0, the VI runs on that monitor. If you specify a
        monitor  short
                       monitor number greater than the number of monitors on the system, or if you
                          specify a negative number, LabVIEW returns an error. The monitor number
                       corresponds to the video card you plug the monitor in to.


6350   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6350 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6351 ordinal=6351 -->
## Property and Method Reference

Property and Method Reference

Return Value

none

FPRunTimePosRunUnchangedFPRunTimePosRunUnchanged

Sets the VI to not move its front panel when the VI runs.

Syntax

object.FPRunTimePosRunUnchanged()
Return Value

none

GetControlValueGetControlValue

Gets the value of the named LabVIEW control or indicator as variant data. Use the
LabVIEW Variant to Data function to convert the data to another LabVIEW data type.

The first time you call this method on a VI whose front panel is not open, this method
returns the default values of the control or indicator rather than the actual values.
Thereafter, it returns the actual value.

For optimization purposes, LabVIEW does not keep track of data values on controls
and indicators until LabVIEW determines you want them, that is, until you call this
method or display the front panel. When you display the front panel, LabVIEW begins
keeping track of the values.

Syntax

object.GetControlValue(controlName)
Parameters

 Name          Type    Description

 controlName      String   Name of the control or indicator whose value you want.


                                                    © National Instruments 6351

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6351 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6352 ordinal=6352 -->
## Property and Method Reference

Property and Method Reference

     Return Value

       variant

      GetLockStateGetLockState

       Returns the lock state of the VI and indicates whether the password for the VI is in the
      password cache.

     Syntax

     object.GetLockState([pwdInCache])
     Parameters

      Name       Type           Description

        pwdInCache  Boolean by ref  Indicates whether the password is currently in the password cache.

     Return Value

      VILockStateEnum

      GetVIDependenciesGetVIDependencies

       This method returns the names and paths of the VI dependencies of a VI. You can use
        this method to return a specific subset of the total set of VI dependencies of a VI. This
      method does not return non-VI dependencies, such as project libraries, XControls,
        classes, and statecharts.

      LabVIEW combines the parameter values you specify using the logical AND operator to
      determine which dependencies to return. For example, you must pass TRUE to both
        Static VI Refs? and Include Control VIs? in order for LabVIEW to return a static VI
       reference to a custom control or indicator.

      By default, this method does not load the block diagram into memory. However, if you
       specify certain input values, LabVIEW loads the block diagram.


6352   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6352 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6353 ordinal=6353 -->
## Property and Method Reference

Property and Method Reference

Syntax

object.GetVIDependencies([dependencyNames],
[dependencyPaths], [wholeHierarchy], [commentedOut],
[staticVIRefs], [dynDispatching], [missingItems],
[standardVIs], [reentrantClones], [polyVIs], [globalVIs],
[controlVIs], [genericVIs], [callSetupVIs], [expressVIs],
[loadDiagram])
Parameters

 Name            Type     Description

 dependencyNames  string    Returns the names of the VI dependencies.

                     array of
 dependencyPaths   strings   Returns the directory paths of the VI dependencies.
                  by ref

                                                If FALSE (default), LabVIEW returns only the dependencies of the
                              current VI. If TRUE, LabVIEW returns all dependencies for the entire wholeHierarchy    Boolean
                                  VI hierarchy. Use the TRUE case to perform hierarchy traversals
                            without having to implement recursion detection yourself.

                                Specifies whether LabVIEW returns dependencies to VIs in diagrams
                               that LabVIEW does not invoke, such as those in the Disable case of a
                          Diagram Disable structure. Also, if you wire a constant to the
                                selector terminal of a Case structure, LabVIEW considers
                           dependencies in non-executing cases to be commented out and
                          does not invoke them.

                               Only include commented out diagrams if diagram already
                           0
                               loaded
 commentedOut     variant
                              Never include commented out diagrams
                           1
                                     (default)

                               Always include commented out diagrams
                              —This option causes LabVIEW to load the block diagrams of VI
                           2 dependencies. If a block diagram requires a password not
                                   currently in the LabVIEW password cache, LabVIEW returns an
                                       error.


                                                    © National Instruments 6353

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6353 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6354 ordinal=6354 -->
## Property and Method Reference

Property and Method Reference


      Name            Type     Description

                                                             If TRUE, LabVIEW returns VIs referenced with Static VI Reference
          staticVIRefs        Boolean  functions, including the top-level VI if it contains a reference to itself.
                                The default is FALSE.

                                        Specifies which VIs LabVIEW returns if the VI contains a dynamic
                                      dispatch subVI.

                               No dynamic dispatch VIs                                   0                                              (default)

                                         Include nearest implementation
        dynDispatching     variant     —Returns only the VI whose icon LabVIEW display on the node.                                   1                                          This VI is the implementation nearest to the wired class data
                                            type.

                                         Include all overrides
                                   2 —Returns all VIs currently in memory to which the node could
                                         dispatch at run time.


                                                             If TRUE, LabVIEW returns names and paths for any missing
                                    dependencies. LabVIEW returns dependencies as missing if they are
                                        corrupt, saved in a later version of LabVIEW, or if they cannot be
        missingItems       Boolean                                  found on disk. Since the types of missing dependencies are
                                unknown, LabVIEW returns missing dependencies regardless of how
                                 you configure other parameters. The default is FALSE.

                                                             If TRUE (default), LabVIEW returns subVIs, including polymorphic VI
         standardVIs        Boolean                                       instances and instantiations of generic VIs.

                                        Specifies whether LabVIEW returns clone VIs of reentrant VIs that are
                                    dependencies.

                                   0  Include the clone VI
         reentrantClones    Boolean                                          Include the original reentrant VI instead of the clone VI
                                   1
                                               (default)

                                   2  Include both the original reentrant VI and the clone VI


         polyVIs            Boolean  If TRUE (default), LabVIEW returns polymorphic VIs.

         globalVIs          Boolean  If TRUE (default), LabVIEW returns global VIs.


6354   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6354 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6355 ordinal=6355 -->
## Property and Method Reference

Property and Method Reference


 Name            Type     Description

                                                If TRUE (default), LabVIEW returns type definitions and strict type controlVIs         Boolean                                  definitions.

 genericVIs         Boolean  If TRUE (default), LabVIEW returns generic VIs.

                                                If TRUE (default), LabVIEW returns subVI calls that use the
                                alternative Call Setup options, such as Reload for each call or Load
                        and retain on first call. Because these VIs are dynamically loaded,                  Boolean callSetupVIs                 they may or may not be in memory. To include any VIs missing from                     control                         memory, set the Include Missing Items to TRUE. To bring any
                             missing items into memory in a development environment, set Load
                            Block Diagram to TRUE.

                                                If TRUE, LabVIEW returns Express VIs as dependencies. If you want
                               edit-time Express VI dependencies, set Keep Express VIs? to TRUE. If                  Boolean expressVIs                 you want run-time Express VI dependencies, set Keep Express VIs?                     control
                               to FALSE. Regardless of this setting, LabVIEW returns any subVI calls
                               that the Express VI scripts into the referenced VI.

                                                If TRUE, LabVIEW loads this VI block diagram before it evaluates
                           whether any dependencies exist. If you open a block diagram from a
                  Boolean loadDiagram                  location that is different from the location in which it is originally                     control                              saved, LabVIEW may load new subVIs into memory. This may affect
                             the Include Alternate Call Setup VIs? option. The default is FALSE.

Return Value

none

ImportVIStringsImportVIStrings

Imports the following strings about VI and LabVIEW front panel objects from a tagged
text file: VI name and description, object caption labels, object free labels, default data
(string, table, path, and array default data), private data (listbox item names, table row
and column headers, graph plot names, graph cursor names, graph annotation names,
and tab control page captions), and polymorphic VI data (instance names in the
polymorphic VI and selector shortcut menus).

Syntax

object.ImportVIStrings(stringFile, [interactive],

                                                    © National Instruments 6355

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6355 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6356 ordinal=6356 -->
## Property and Method Reference

Property and Method Reference

     [logFile])
     Parameters

      Name     Type     Description

                            Path of the VI strings file including the filename. If you do not enter a
          stringFile   String                              filename, set interactive to TRUE so the user can set the VI strings filename.

                                                If TRUE, the user can see the file dialog box to select the name of the VI          interactive Boolean                                 strings file. The default is FALSE.

                            Path of the log file created to list errors that occurred while importing VI          logFile      String                                 strings from a tagged text file. The default is no logging.

     Return Value

      none

      MakeCurValueDefaultMakeCurValueDefault

      Changes the defaults of all controls on the LabVIEW front panel to be the current
       values. This method is available only in edit mode.

     Syntax

     object.MakeCurValueDefault()
     Return Value

      none

      OpenFrontPanelOpenFrontPanel

      Opens the LabVIEW front panel window. If the front panel is already open, this method
      changes the state of the front panel window to the state you wire to this method. Use
       the CloseFrontPanel method to close the front panel window.

      You also can use the FPState property to set the state of a front panel window that is
       already open.


6356   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6356 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6357 ordinal=6357 -->
## Property and Method Reference

Property and Method Reference

Syntax

object.OpenFrontPanel([activate], [state])
Parameters

 Name   Type          Description

 activate  Boolean            If TRUE (default), the front panel window opens as the active window.

 state    FPStateEnum  Sets the state in which to open the front panel window.

Return Value

none

PrintPanelPrintPanel

Prints just the LabVIEW front panel to the current printer. You cannot use this method
to print a block diagram, list of controls, or polymorphic VI front panel.

Syntax

object.PrintPanel([entirePanel])
Parameters

 Name      Type     Description

                        Indicates whether the entire front panel is printed. If FALSE (default), only
 entirePanel Boolean
                      the currently visible portion of the front panel is printed.

Return Value

none

PrintVIToHTMLPrintVIToHTML

Saves the VI information to an HTML file and saves the graphics in external files.


                                                    © National Instruments 6357

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6357 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6358 ordinal=6358 -->
## Property and Method Reference

Property and Method Reference

     Syntax

     object.PrintVIToHTML(htmlFilePath, [append], [format],
     [imageFormat], [imageDepth], [imageDirectory])
     Parameters

      Name         Type                    Description

                                               Path to the HTML file in which you want to save the VI
                                                   information. The directory in which you want to save         htmlFilePath    String                                                the file must already exist, and you must wire a full
                                              path including the HTML filename.

                                                     Specifies whether the new information will be
       append        Boolean                                          appended to an existing file. The default is FALSE.

                                                     Specifies which VI information to print and the format
        format         PrintFormatEnum         of the printout. You can select from eCustom,
                                                 eStandard, eUsingPanel, eUsingSubVI, or eComplete.

        imageFormat   HTMLImageFormatEnum Format of the graphic files. Select from ePNG or eJPEG.

                                                  Sets the color depth, or number of supported colors, of
                                                the image: 1 (1-bit, black and white), 4 (4-bit, 16 colors),
        imageDepth    Long                                             8 (8-bit, 256 colors), or 24 (24-bit, true color). The
                                                    default is 8.

                                               Path to the directory in which you want to save the
                                                  graphic files. The directory in which you want to save
         imageDirectory  String                   the files must already exist. If not specified, LabVIEW
                                                saves the image files in the same directory as the HTML
                                                  or RTF file.

     Return Value

      none

       PrintVIToPrinterPrintVIToPrinter

       Prints the VI information to a printer. If you use this method in a stand-alone
       application or DLL, LabVIEW prints only the front panel.


6358   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6358 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6359 ordinal=6359 -->
## Property and Method Reference

Property and Method Reference

Syntax

object.PrintVIToPrinter([format], [scalePanel],
[scaleDiagram], [pageHeaders], [pageBreaks],
[sectionHeaders])
Parameters

 Name         Type              Description

                                      Specifies which VI information to print and the format of the
 format         PrintFormatEnum  printout. You can select from eCustom, eStandard,
                                   eUsingPanel, eUsingSubVI, or eComplete.

                                      Specifies whether the front panel will be scaled to fit the page.
 scalePanel      Boolean                              The default is TRUE.

                                      Specifies whether the block diagram will be scaled to fit the
 scaleDiagram   Boolean                                  page. The default is TRUE.

                                      Specifies whether page headers (which include the page
 pageHeaders   Boolean         number, VI name, and last modification data) will be printed.
                              The default is TRUE.

                                      Specifies whether page breaks will be inserted between the
                                    following sections: connector icon and description, front
 pageBreaks     Boolean           panel, list of front panel control details, block diagram, block
                                diagram details, VI hierarchy, and list of subVIs. The default is
                                  FALSE.

                                      Specifies whether to print headers for each section listed
 sectionHeaders Boolean          above. If format is eCustom, eStandard, or eComplete, the
                                     default is TRUE. Otherwise, the default is FALSE.

Return Value

none

PrintVIToRTFPrintVIToRTF

Saves the VI information to an RTF file.


                                                    © National Instruments 6359

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6359 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6360 ordinal=6360 -->
## Property and Method Reference

Property and Method Reference

     Syntax

     object.PrintVIToRTF(rtfFilePath, [append], [format],
     [imageFormat], [imageDepth], [imageDirectory],
     [helpFormat])
     Parameters

      Name         Type              Description

                                         Path to the RTF file in which you want to save the VI
                                            information. The directory in which you want to save the file          rtfFilePath       String                                    must already exist, and you must specify a full path including
                                          the RTF filename.

                                              Specifies whether the new information will be appended to an       append        Boolean                                                existing file. The default is FALSE.

                                              Specifies which VI information to print and the format of the
        format         PrintFormatEnum  printout. You can select from eCustom, eStandard,
                                           eUsingPanel, eUsingSubVI, or eComplete.

                                      Format of the graphics file. The default is 0, which corresponds
        imageFormat   Long                                            to the BMP format. BMP is the only format supported.

                                            Sets the color depth, or number of supported colors, of the
        imageDepth    Long             image: 1 (1-bit, black and white), 4 (4-bit, 16 colors), 8 (8-bit,
                                       256 colors), or 24 (24-bit, true color). The default is 8.

                                         Path to the directory in which you want to save the graphic
                                                           files. The directory in which you want to save the files must         imageDirectory  String
                                           already exist. If not specified, LabVIEW saves the image files in
                                          the same directory as the HTML or RTF file.

                                              Specifies whether to save the graphics externally and place
        helpFormat    Boolean           references in the RTF file. Set this parameter to TRUE if you are
                                             creating a help file. The default is FALSE.

     Return Value

      none


6360   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6360 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6361 ordinal=6361 -->
## Property and Method Reference

Property and Method Reference

PrintVIToTextPrintVIToText

Saves the VI information to a text file. You cannot save the icon, connector pane, front
panel, block diagram, subVI icons, and VI hierarchy to text.

Syntax

object.PrintVIToText(textFilePath, [append], [format])
Parameters

 Name      Type              Description

                              Path to the text file in which you want to save the VI information.
 textFilePath  String           The directory in which you want to save the file must already
                                       exist, and you must specify a full path including the text filename.

                                  Specifies whether the new information will be appended to an
 append     Boolean                                   existing file. The default is FALSE.

                                  Specifies which VI information to print and the format of the
                                   printout. You can select from eCustom, eStandard, eUsingPanel,
                               eUsingSubVI, or eComplete.
 format      PrintFormatEnum
                              Note The eCustom, eStandard, eUsingPanel, and
                                      eUsingSubVI parameters print only connector pane
                                             controls.


Return Value

none

ReinitializeAllToDefaultReinitializeAllToDefault

Changes the current values of all controls on the LabVIEW front panel to their defaults.

Syntax

object.ReinitializeAllToDefault()


                                                    © National Instruments 6361

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6361 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6362 ordinal=6362 -->
## Property and Method Reference

Property and Method Reference

     Return Value

      none

      RevertRevert

       Discards changes and reloads a VI from disk.

     Syntax

     object.Revert()
     Return Value

      none

     RunRun

        Starts the VI execution, similar to the Run button in LabVIEW. This method is different
      than calling a VI because it uses the current values of all front panel controls for
       execution rather than using data passed in through parameters. This method also
       ignores the ShowFPOnCall property of a VI and the CloseFPAfterCall property. You
      cannot use this method to run a VI that is already reserved for execution by another VI.

     Syntax

     object.Run([async])
     Parameters

      Name Type     Description

        async  Boolean   If TRUE, you do not need to wait for the VI to finish running. The default is FALSE.

     Return Value

      none


6362   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6362 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6363 ordinal=6363 -->
## Property and Method Reference

Property and Method Reference

SaveForPreviousSaveForPrevious

Saves a copy of the VI that is readable by LabVIEW 8.0 and later.

Syntax

object.SaveForPrevious(Path to Saved File, [Warnings],
[Target Version])
Parameters

 Name              Type    Description

 Path to Saved File      String   Path where you want to save the VI.

 Warnings              String   Returns any warnings that occurred while saving the VI.

 Target Version                 Version of LabVIEW to which you want to save the VI.

Return Value

none

SaveInstrumentSaveInstrument

Saves a VI and synchronizes the VI with the edited version in other application
instances before saving.

Syntax

object.SaveInstrument([viPath], [saveACopy],
[withoutDiagram])
Parameters

 Name           Type      Description

 viPath              String     Path of the VI file. The default is the current location.

 saveACopy        Boolean   Indicates whether to save a copy of the VI to another file.

 withoutDiagram   Boolean   Indicates whether to save the VI without the block diagram.


                                                    © National Instruments 6363

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6363 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6364 ordinal=6364 -->
## Property and Method Reference

Property and Method Reference

     Return Value

      none

     SaveRunTimeMenuSaveRunTimeMenu

      Saves the LabVIEW run-time menu to a file specified by filePath. This method works
       only when the VI is running. It saves only menu items with valid tags.

     Syntax

     object.SaveRunTimeMenu(filePath)
     Parameters

      Name      Type      Description

          filePath      String    Path to where you want to save the run-time menu.

     Return Value

      none

      SetControlValueSetControlValue

       Sets the value of a named LabVIEW control or indicator.

     Syntax

     object.SetControlValue(controlName, value)
     Parameters

      Name       Type   Description

        controlName  String  Name of the front panel control.

                      New value of the front panel control. This value can be numeric, Boolean,
         value         variant  string, or array. A cluster in LabVIEW is represented as an array of variants in
                                 ActiveX.


6364   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6364 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6365 ordinal=6365 -->
## Property and Method Reference

Property and Method Reference

Return Value

none

SetLockStateSetLockState

Sets the lock state of a VI. If Interactive is FALSE (default), you can use Password to
unlock a password-protected VI or set the password of an unprotected VI. If Interactive
is TRUE, LabVIEW ignores Password and displays a dialog box that prompts you to
change the lock state.

Syntax

object.SetLockState(lockState, [Interactive], [Password],
[putInCache])
Parameters

 Name      Type             Description

 lockState   VILockStateEnum Lock state.

                                 Specifies whether to display a dialog box that prompts you to Interactive  Boolean                           change the lock state. The default is FALSE.

                                                  If lockState is Password-protected, Password is the new password.
 Password    String                    If you are changing lockState from Password-protected, Password
                                          is the old password. The default is an empty string.

                                                  If lockState is Password-protected, putinCache specifies whether putInCache Boolean                                to place the new password in the cache. The default is FALSE.

Return Value

none

SetVIIconSetVIIcon

Sets the image of a VI icon from a file.


                                                    © National Instruments 6365

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6365 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6366 ordinal=6366 -->
## Property and Method Reference

Property and Method Reference

     Syntax

     object.SetVIIcon(imageFile)
     Parameters

      Name        Type      Description

         imageFile       String     Path to the image you want to use for the VI icon.

     Return Value

      none

       VIVI PropertiesProperties (ActiveX)(ActiveX)

      A VirtualInstrument object exports properties that affect a given VI. A
       VirtualInstrument object is instantiated by invoking the GetVIReference method on the
       Application object.

        In the following topics, an asterisk (*) at the end of a data type name indicates that the
       property is a pointer. Property parameters denoted by [] are optional for that property.

       Refer to the ActiveX Enumerations for more information about enumerations used in
       various properties.

      Properties

        Property                       Description

                                                                  If TRUE, you can use debugging tools on the VI. Set this property
        AllowDebugging                 to FALSE to reduce memory requirements and to improve
                                     performance slightly for the VI.


                                           Indicates whether changes were made to the block diagram
         BDModificationBitSet            since the VI was saved or opened, depending on which was last.
                                                                  If the value is zero, no changes were made. If the value is


6366   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6366 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6367 ordinal=6367 -->
## Property and Method Reference

Property and Method Reference


Property                       Description

                               nonzero, changes were made. This property is read only.


                                  Size of the LabVIEW block diagram in bytes. This property is readBDSize                                   only.


                               Returns a list of all the loaded VIs that call the referenced VI. ThisCallers                               property is read only.


CloneName               Name of the clone VI. Returns an error if the VI is not a clone.


                                  Indicates whether to close the LabVIEW front panel after the VI
CloseFPAfterCall                                  runs.


                          Amount of memory used for VI code in bytes. This property is
CodeSize                              read only.


                          Amount of memory allocated for data in bytes. You cannot readDataSize
                                     this property if the VI is running. This property is read only.


                                 Description of the VI that appears in the LabVIEW Context Help
Description                 window when you move the cursor over the VI icon and in VI
                             documentation you generate.


                                                   If TRUE, the VI opens in edit mode. If FALSE, the VI opens in run
EditMode
                           mode, and the title bar, menu bar, and toolbar do not appear.


ExecInlining                      Specifies whether to inline the subVI into its calling VIs.


                                                    © National Instruments 6367

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6367 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6368 ordinal=6368 -->
## Property and Method Reference

Property and Method Reference


        Property                       Description

         ExecIsInlineable                Returns TRUE if you can inline this subVI into its calling VIs.


                                           Indicates the priority of the VI when it runs in parallel with other         ExecPriority                                             tasks.


         ExecState                        Indicates the execution state of the VI.


        ExpandWhenDroppedAsSubVI    Expands to show terminals when dropped as a subVI.


                                           Indicates whether to display shortcut menus for LabVIEW front
                                       panel objects while the VI runs. If you do not display default run-
        FPAllowRTPopup                                      time shortcut menus, you can continue to include customized
                                         shortcut menus.


                                         Sets the behavior of the LabVIEW front panel window. Valid
                                         values include 0 (

                                             Invalid
                                                                  ), 1 (
                                          Default
        FPBehavior                                  ), 2 (
                                           Floating
                                                                  ), 3 (
                                         Floating/Auto-Hide
                                                                  ), and 4 (
                                   Modal
                                                                  ).


                                           Indicates whether to highlight Boolean controls that have a
         FPHiliteReturnButton
                                         shortcut key of <Enter>.


6368   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6368 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6369 ordinal=6369 -->
## Property and Method Reference

Property and Method Reference


Property                       Description

                                  Indicates whether the LabVIEW front panel window adjusts its
                                    size in proportion with a change in monitor resolution. TheFPKeepWinProps                          window changes size so it covers the same percentage of the
                               screen that it covered at its original resolution.


                                  Indicates whether the user can minimize the LabVIEW front panel
FPMinimizable                          window while the VI runs.


                                  Indicates whether changes were made to the LabVIEW front
FPModificationBitSet            panel since the VI was saved. If the value is zero, no changes
                            where made. If the value is nonzero, changes were made.


                           The monitor on which the LabVIEW front panel window appears,
FPMonitor                                     if you have multiple monitors. The value 0 is the primary
                                monitor.


                                  Indicates whether the user can resize the LabVIEW front panel
FPResizable                          window while the VI runs.


FPRunTransparently             Sets the VI to run transparently.


                                  Indicates whether to display the menu bar on the LabVIEW front
FPShowMenuBar
                              panel while the VI runs.


                                  Size of the LabVIEW front panel in bytes. This property is read
FPSize
                                   only.


                                Current state of the LabVIEW front panel window. Valid values
FPState
                                include 0 (


                                                    © National Instruments 6369

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6369 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6370 ordinal=6370 -->
## Property and Method Reference

Property and Method Reference


        Property                       Description

                                             Invalid
                                                                  ), 1 (
                                      Standard
                                                                  ), 2 (
                                      Closed
                                                                  ), 3 (
                                    Hidden
                                                                  ), 4 (
                                      Minimized
                                                                  ), and 5 (
                                     Maximized
                                                                  ).

                                 A state of

                                      Standard
                                         or
                                     Maximized
                                           indicates that the front panel window is visible to the user.

                                                                  If you attempt to set this property for a front panel window that
                                                       is not open, the property returns an error.


                                           Indicates whether to display a title bar on the LabVIEW front
         FPTitleBarVisible                                       panel while the VI runs.


                                         Sets the window transparency level of the VI. The level of
                                        transparency is a percentage where 0 is opaque and 100 is
        FPTransparency                    invisible. This property returns an error if you specify a value
                                         outside the range of 0 to 100. If you set FPRunTransparently to
                                              False, changing this property has no effect.


                                   The four elements in the cluster are the top, left, bottom, and
                                              right values of the LabVIEW front panel window, which includes
       FPWinBounds                  the interior region, scroll bars, title bar, menu bar, and toolbar.
                                    They are in global screen coordinates, that is, the numbers refer
                                          to coordinates within a computer monitor's screen (rather than


6370   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6370 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6371 ordinal=6371 -->
## Property and Method Reference

Property and Method Reference


Property                       Description

                           an open window).

                            You can set this property only for VIs with open front panels. If
                            you do not want the VI for which you want to set this property to
                             appear to users, use the

                            Hidden
                                value of the FPStateEnum data type for the FPState property to
                               hide the front panel of the VI.


                                  Indicates whether the close button in the LabVIEW title bar is
FPWinClosable                  disabled and the Close item in the LabVIEW File menu is
                                  disabled.


                                  Indicates whether the VI has a custom title string. Write FALSE toFPWinCustomTitle                           remove the custom title string.


                                 Writing TRUE to this value brings the front panel to the front. This
                               property applies only in the application instance of the calling VI.
FPWinIsFrontMost                Writing FALSE to this value has no effect. If you read this
                                 property, it indicates whether the front panel window is the front
                          window (ignoring floating windows).


                           The four elements in the cluster are the top, left, bottom, and
                                    right values of the interior portion of the LabVIEW front panel,
                              not including the scroll bars, title bar, menu bar, and toolbar. The
                                   cluster elements are in global screen coordinates, that is, the
                           numbers refer to coordinates within a computer monitor's
                               screen (rather than an open window).FPWinPanelBounds
                            You can set this property only for VIs with open front panels. If
                            you do not want the VI for which you want to set this property to
                             appear to users, use the

                            Hidden
                                value of the FPStateEnum data type for the FPState property to

                                                    © National Instruments 6371

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6371 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6372 ordinal=6372 -->
## Property and Method Reference

Property and Method Reference


        Property                       Description

                                        hide the front panel of the VI.


                                            String that appears in the LabVIEW title bar. This string does not         FPWinTitle                                    have to match the VI filename.


                                      Path to an HTML file (.htm or .html) or compiled help file
                                  (.chm or .hlp) to which the VI is linked. If the path is to a        HelpDocumentPath
                                     compiled help file, use the HelpDocumentTag property to
                                      determine the specific topic in that help file.


                                        Index keyword or HTML filename for a topic in the compiled help
                                                        file to which the VI is linked. To link to a bookmark within an
                              HTML file, add # followed by the name of the bookmark to the
                                  end of the filename. Use this property only when
        HelpDocumentTag             HelpDocumentPath is a path to a compiled help file (.chm or
                                     .hlp).

                                        For .chm files, this property can be an HTML filename or index
                                      keyword. For .hlp files, this property can be an index keyword.


                                URL for the web-based help topic to link to a VI from the Detailed        HelpDocumentUrl                                      help link in the Context Help window.


                                           Indicates whether to link to a web-based help file from the
        HelpUseOnline
                                         Detailed help link in the Context Help window for a VI.


                                           Indicates whether to add a comment to the VI revision history
        HistAddCommentsAtSave
                                        every time the VI is saved.


                                           Indicates whether to prompt for a VI revision history comment
        HistPromptAtClose
                                when the VI closes.


6372   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6372 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6373 ordinal=6373 -->
## Property and Method Reference

Property and Method Reference


Property                       Description

                                  Indicates whether to prompt for a VI revision history comment
HistPromptForCommentsAtSave                         when the VI is saved.


                                  Indicates whether to add comments to the VI revision history
                         when certain events occur, such as conversion to a new versionHistRecordAppComments                                  of LabVIEW, subVI changes, and changes to the name or path of
                               the VI.


                                  Indicates whether to use the global default history or to use theHistUseDefaults                                values entered in other history properties.


                               Returns all the text that was added to the VI revision history. ThisHistoryText                               property is read only.


IsCloneVI                      Returns TRUE if the VI is a clone VI.


                               Returns TRUE if the VI is running as a probe and the probe VI isIsProbe                              open.


IsReentrant                      Indicates whether a VI can be reentrant.


                               Returns the name of the LabVIEW project library, XControl, or
Library                      LabVIEW class that owns the VI. If no library, XControl, or class
                          owns the VI, the property returns NULL.


                                  Indicates whether to write LabVIEW front panel values to a
LogAtFinish
                                datalog file after the VI runs.


                                                    © National Instruments 6373

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6373 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6374 ordinal=6374 -->
## Property and Method Reference

Property and Method Reference


        Property                       Description

                                      Path of the datalog file in which LabVIEW front panel data and a
         LogFilePath                                      time stamp are written.


                             Name of the VI file. You can write this property only if the VI has
                                       not been saved to disk. If a LabVIEW project library owns the VI,      Name                                               this property returns the qualified name of the VI, which includes
                                        the project library filename.


                                       Returns a reference to the Application that owns this VI. Close       OwningApp                                               this reference when you are finished using it.


        Path                          Path to the VI file. This property is read only.


        PreferredExecSystem             Indicates the execution system in which the VI runs.


                                                                  If TRUE, LabVIEW includes the date printed in the headers for the
         PrintHeaderDatePrint               VI. Use the PrintingHeaders property to set whether LabVIEW
                                             prints the headers for the VI.


                                                                  If TRUE, LabVIEW includes the last modified date in the headers
        PrintHeaderModifyDate           for the VI. Use the PrintingHeaders property to set whether
                                   LabVIEW prints the headers for the VI.


                                                                  If TRUE, LabVIEW includes the page number in the headers for
        PrintHeaderPageNumber        the VI. Use the PrintingHeaders property to set whether LabVIEW
                                             prints the headers for the VI.


                                                                  If TRUE, LabVIEW includes the VI icon in the headers for the VI.
         PrintHeaderVIIcon
                                   Use the PrintingHeaders property to set whether LabVIEW prints


6374   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6374 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6375 ordinal=6375 -->
## Property and Method Reference

Property and Method Reference


Property                       Description

                               the headers for the VI.


                                                   If TRUE, LabVIEW includes the VI name in the headers for the VI.
PrintHeaderVIName           Use the PrintingHeaders property to set whether LabVIEW prints
                               the headers for the VI.


                                  Indicates whether to print the LabVIEW front panel after the VIPrintLogFileAtFinish
                                  runs.


                               Gets or sets the page margins to use when printing the VI inPrintMargins                                inches or centimeters.


                                                   If TRUE, LabVIEW scales the block diagram to fit on the printed
PrintingBDScaling                               page.


PrintingFPScaling                         If TRUE, LabVIEW scales the front panel to fit on the printed page.


                                                   If TRUE, LabVIEW includes the VI path in the headers for the VI.
PrintingHeaderVIPath          Use the PrintingHeaders property to set whether LabVIEW prints
                               the headers for the VI.


                                                   If TRUE, LabVIEW prints headers for the VI. Use the PrintHeader
PrintingHeaders
                                 properties in this class to customize the contents of the headers.


PrintingOrientation             Gets or sets the page orientation to use when printing the VI.


                                  Indicates the type of reentrancy LabVIEW uses for a reentrant VI.
ReentrancyType
                                 This property is similar to options on the Execution Properties


                                                    © National Instruments 6375

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6375 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6376 ordinal=6376 -->
## Property and Method Reference

Property and Method Reference


        Property                       Description

                                    page of the VI Properties dialog box.


        RevisionNumber                Current revision number of the VI.


       RunOnOpen                      Indicates whether to run the VI when it opens.


                               When read, this property returns the run-time menu path of the
                                                     VI. When written, this property updates the run-time menu path       RunTimeMenuPath
                                            of the VI. If the VI is running when you write this property, it
                                      updates the menu with data from the new path.


                                           Indicates whether to show the LabVIEW front panel when the VI        ShowFPOnCall                                                       is called.


                                           Indicates whether to show the LabVIEW front panel when the VI       ShowFPOnLoad                                                       is loaded.


                                           Indicates whether the VI should be suspended when it is called        SuspendOnCall                                       as a subVI. Use this property carefully with reentrant VIs.


                                           Indicates whether to display the Abort Execution button on the
        TBShowAbortButton
                                   LabVIEW toolbar while the VI runs.


                                           Indicates whether to display the Run Continuously button on the
        TBShowFreeRunButton
                                   LabVIEW toolbar while the VI runs.


                                           Indicates whether to display the Run button on the LabVIEW
       TBShowRunButton
                                          toolbar while the VI runs.


6376   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6376 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6377 ordinal=6377 -->
## Property and Method Reference

Property and Method Reference


 Property                       Description

                                   Indicates whether to display the LabVIEW toolbar while the VI
 TBVisible                                   runs.


 VIType                           Indicates the type of the VI.


AllowDebuggingAllowDebugging

If TRUE, you can use debugging tools on the VI. Set this property to FALSE to reduce
memory requirements and to improve performance slightly for the VI.

You cannot debug a reentrant VI.

      Note Writing this property causes the VI to be recompiled. Writing TRUE
       causes extra code and data to be generated for the VI. This code and data
       enables LabVIEW to set breakpoints and single-step through the VI. Writing
       FALSE removes this code and data, reducing the total size of the VI.

Syntax

object.AllowDebugging
Data Type

Boolean

BDModificationBitSetBDModificationBitSet

Indicates whether changes were made to the block diagram since the VI was saved or
opened, depending on which was last. If the value is zero, no changes were made. If
the value is nonzero, changes were made. This property is read only.

Syntax

object.BDModificationBitSet


                                                    © National Instruments 6377

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6377 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6378 ordinal=6378 -->
## Property and Method Reference

Property and Method Reference

     Data Type

       long

      BDSizeBDSize

       Size of the LabVIEW block diagram in bytes. This property is read only.

     Syntax

     object.BDSize
     Data Type

       long

       CallersCallers

       Returns a list of all the loaded VIs that call the referenced VI. This property is read only.

     Syntax

     object.Callers
     Data Type

       Array of strings

     CloneNameCloneName

     Name of the clone VI. Returns an error if the VI is not a clone.

     Syntax

     object.CloneName
     Data Type

        string


6378   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6378 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6379 ordinal=6379 -->
## Property and Method Reference

Property and Method Reference

CloseFPAfterCallCloseFPAfterCall

Indicates whether to close the LabVIEW front panel after the VI runs.

Syntax

object.CloseFPAfterCall
Data Type

Boolean

CodeSizeCodeSize

Amount of memory used for VI code in bytes. This property is read only.

Syntax

object.CodeSize
Data Type

long

DataSizeDataSize

Amount of memory allocated for data in bytes. You cannot read this property if the VI is
running. This property is read only.

Syntax

object.DataSize
Data Type

long

DescriptionDescription

Description of the VI that appears in the LabVIEW Context Help window when you

                                                    © National Instruments 6379

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6379 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6380 ordinal=6380 -->
## Property and Method Reference

Property and Method Reference

     move the cursor over the VI icon and in VI documentation you generate.

      You can format the text in the description to appear bold in the Context Help window.

     Syntax

     object.Description
     Data Type

       String

      EditModeEditMode

           If TRUE, the VI opens in edit mode. If FALSE, the VI opens in run mode, and the title bar,
     menu bar, and toolbar do not appear.

      To write this property, you must call it before you open the front panel of the VI.

     Syntax

     object.EditMode
     Data Type

      Boolean

       ExecInliningExecInlining

       Specifies whether to inline the subVI into its calling VIs.

     Syntax

     object.ExecInlining
     Data Type

      bool


6380   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6380 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6381 ordinal=6381 -->
## Property and Method Reference

Property and Method Reference

ExecIsInlineableExecIsInlineable

Returns TRUE if you can inline this subVI into its calling VIs.

Syntax

object.ExecIsInlineable
Data Type

bool

ExecPriorityExecPriority

Indicates the priority of the VI when it runs in parallel with other tasks.

Syntax

object.ExecPriority
Data Type

VIPriorityEnum

ExecStateExecState

Indicates the execution state of the VI.

Syntax

object.ExecState
Data Type

ExecStateEnum

ExpandWhenDroppedAsSubVIExpandWhenDroppedAsSubVI

Expands to show terminals when dropped as a subVI.


                                                    © National Instruments 6381

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6381 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6382 ordinal=6382 -->
## Property and Method Reference

Property and Method Reference

     Syntax

     object.ExpandWhenDroppedAsSubVI
     Data Type

      Boolean

      FPAllowRTPopupFPAllowRTPopup

       Indicates whether to display shortcut menus for LabVIEW front panel objects while the
        VI runs. If you do not display default run-time shortcut menus, you can continue to
       include customized shortcut menus.

     Syntax

     object.FPAllowRTPopup
     Data Type

      Boolean

      FPBehaviorFPBehavior

       Sets the behavior of the LabVIEW front panel window. Valid values include 0
      (Invalid), 1 (Default), 2 (Floating), 3 (Floating/Auto-Hide), and 4
      (Modal).

     Syntax

     object.FPBehavior
     Data Type

      VIFPBehaviorEnum

      FPHiliteReturnButtonFPHiliteReturnButton

       Indicates whether to highlight Boolean controls that have a shortcut key of <Enter>.


6382   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6382 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6383 ordinal=6383 -->
## Property and Method Reference

Property and Method Reference

Syntax

object.FPHiliteReturnButton
Data Type

Boolean

FPKeepWinPropsFPKeepWinProps

Indicates whether the LabVIEW front panel window adjusts its size in proportion with a
change in monitor resolution. The window changes size so it covers the same
percentage of the screen that it covered at its original resolution.

Syntax

object.FPKeepWinProps
Data Type

Boolean

FPMinimizableFPMinimizable

Indicates whether the user can minimize the LabVIEW front panel window while the VI
runs.

If you load the VI in a subpanel control, this property is read only and always returns a
value of FALSE.

This property is similar to the Allow user to minimize window checkbox in the
LabVIEW Customize Window Appearance dialog box.

Syntax

object.FPMinimizable
Data Type

Boolean


                                                    © National Instruments 6383

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6383 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6384 ordinal=6384 -->
## Property and Method Reference

Property and Method Reference

      FPModificationBitSetFPModificationBitSet

       Indicates whether changes were made to the LabVIEW front panel since the VI was
       saved. If the value is zero, no changes where made. If the value is nonzero, changes
      were made.

     Syntax

     object.FPModificationBitSet
     Data Type

       long

      FPMonitorFPMonitor

      The monitor on which the LabVIEW front panel window appears, if you have multiple
       monitors. The value 0 is the primary monitor.

     Syntax

     object.FPMonitor
     Data Type

       short

      FPResizableFPResizable

       Indicates whether the user can resize the LabVIEW front panel window while the VI
       runs.

           If you load the VI in a subpanel control, this property is read only and always returns a
       value of FALSE.

       This property is similar to the Allow user to resize window checkbox in the LabVIEW
      Customize Window Appearance dialog box.


6384   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6384 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6385 ordinal=6385 -->
## Property and Method Reference

Property and Method Reference

Syntax

object.FPResizable
Data Type

Boolean

FPRunTransparentlyFPRunTransparently

Sets the VI to run transparently.

Syntax

object.FPRunTransparently
Data Type

Boolean

FPShowMenuBarFPShowMenuBar

Indicates whether to display the menu bar on the LabVIEW front panel while the VI
runs.

If you load the VI in a subpanel control, this property is read only and always returns a
value of FALSE.

Syntax

object.FPShowMenuBar
Data Type

Boolean

FPSizeFPSize

Size of the LabVIEW front panel in bytes. This property is read only.


                                                    © National Instruments 6385

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6385 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6386 ordinal=6386 -->
## Property and Method Reference

Property and Method Reference

       This property is similar to the Front Panel Objects option on the Memory Usage page
       of the LabVIEW VI Properties dialog box.

     Syntax

     object.FPSize
     Data Type

       long

      FPStateFPState

       Current state of the LabVIEW front panel window. Valid values include 0 (Invalid), 1
      (Standard), 2 (Closed), 3 (Hidden), 4 (Minimized), and 5 (Maximized).

      A state of

      Standard
       or
      Maximized
       indicates that the front panel window is visible to the user.

           If you attempt to set this property for a front panel window that is not open, the
       property returns an error.

     Syntax

     object.FPState
     Data Type

      FPStateEnum

       FPTitleBarVisibleFPTitleBarVisible

       Indicates whether to display a title bar on the LabVIEW front panel while the VI runs.

           If you load the VI in a subpanel control, this property is read only and always returns a
       value of FALSE.

6386   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6386 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6387 ordinal=6387 -->
## Property and Method Reference

Property and Method Reference

This property is similar to the Window has title bar option on the LabVIEW Customize
Window Appearance dialog box.

Syntax

object.FPTitleBarVisible
Data Type

Boolean

FPTransparencyFPTransparency

Sets the window transparency level of the VI.

The level of transparency is a percentage where 0 is opaque and 100 is invisible. This
property returns an error if you specify a value outside the range of 0 to 100. If you set
FPRunTransparently to False, changing this property has no effect.

Syntax

object.FPTransparency
Data Type

char

FPWinBoundsFPWinBounds

The four elements in the cluster are the top, left, bottom, and right values of the
LabVIEW front panel window, which includes the interior region, scroll bars, title bar,
menu bar, and toolbar. They are in global screen coordinates, that is, the numbers
refer to coordinates within a computer monitor's screen (rather than an open window).

You can set this property only for VIs with open front panels. If you do not want the VI
for which you want to set this property to appear to users, use the

Hidden
value of the FPStateEnum data type for the FPState property to hide the front panel of
the VI.

                                                    © National Instruments 6387

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6387 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6388 ordinal=6388 -->
## Property and Method Reference

Property and Method Reference

     When you read this property, LabVIEW returns the window bounds of the VI. If the front
       panel of the VI is not open, LabVIEW returns the window bounds of the VI in the
       position it was last saved.

           If you load the VI in a subpanel control, this property is read only.

     Syntax

     object.FPWinBounds
     Data Type

       Array of short variants (four elements)

      FPWinClosableFPWinClosable

       Indicates whether the close button in the LabVIEW title bar is disabled and the Close
      item in the LabVIEW File menu is disabled.

       This property prevents users from closing a VI during execution.

           If you load the VI in a subpanel control, this property is read only and always returns a
       value of FALSE.

     Syntax

     object.FPWinClosable
     Data Type

      Boolean

      FPWinCustomTitleFPWinCustomTitle

       Indicates whether the VI has a custom title string. Write FALSE to remove the custom
         title string.

     Syntax

     object.FPWinCustomTitle

6388   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6388 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6389 ordinal=6389 -->
## Property and Method Reference

Property and Method Reference

Data Type

Boolean

FPWinIsFrontMostFPWinIsFrontMost

Writing TRUE to this value brings the front panel to the front. This property applies
only in the application instance of the calling VI. Writing FALSE to this value has no
effect. If you read this property, it indicates whether the front panel window is the
front window (ignoring floating windows).

Syntax

object.FPWinIsFrontMost
Data Type

Boolean

FPWinPanelBoundsFPWinPanelBounds

The four elements in the cluster are the top, left, bottom, and right values of the
interior portion of the LabVIEW front panel, not including the scroll bars, title bar,
menu bar, and toolbar. The cluster elements are in global screen coordinates, that is,
the numbers refer to coordinates within a computer monitor's screen (rather than an
open window).

You can set this property only for VIs with open front panels. If you do not want the VI
for which you want to set this property to appear to users, use the

Hidden
value of the FPStateEnum data type for the FPState property to hide the front panel of
the VI.

When you read this property, LabVIEW returns the front panel bounds of the VI. If the
front panel of the VI is not open, LabVIEW returns the front panel bounds of the VI in
the position it was last saved.

This property returns the size of the front panel bounds. These bounds adjust if you

                                                    © National Instruments 6389

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6389 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6390 ordinal=6390 -->
## Property and Method Reference

Property and Method Reference

      change the size or placement of objects in the front panel. Dynamic changes in data
      can occur if you alter bound front panel objects.

           If you load the VI in a subpanel control, this property is read only.

     Syntax

     object.FPWinPanelBounds
     Data Type

      1D array of shorts (four elements) by ref

      FPWinTitleFPWinTitle

       String that appears in the LabVIEW title bar. This string does not have to match the VI
       filename.

       This property is similar to the Window title option on the Window Appearance page of
       the LabVIEW VI Properties dialog box.

     Syntax

     object.FPWinTitle
     Data Type

       String

      HelpDocumentPathHelpDocumentPath

      Path to an HTML file (.htm or .html) or compiled help file (.chm or .hlp) to which
       the VI is linked. If the path is to a compiled help file, use the HelpDocumentTag
       property to determine the specific topic in that help file.

       This property is similar to the Help Path text box on the Documentation page of the
      LabVIEW VI Properties dialog box.


6390   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6390 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6391 ordinal=6391 -->
## Property and Method Reference

Property and Method Reference

Syntax

object.HelpDocumentPath
Data Type

string

HelpDocumentTagHelpDocumentTag

Index keyword or HTML filename for a topic in the compiled help file to which the VI is
linked. To link to a bookmark within an HTML file, add # followed by the name of the
bookmark to the end of the filename. Use this property only when HelpDocumentPath
is a path to a compiled help file (.chm or .hlp).

For .chm files, this property can be an HTML filename or index keyword. For .hlp
files, this property can be an index keyword.

This property is similar to the Help Tag text box on the Documentation page of the
LabVIEW VI Properties dialog box.

Syntax

object.HelpDocumentTag
Data Type

string

HelpDocumentUrlHelpDocumentUrl

URL for the web-based help topic to link to a VI from the Detailed help link in the
Context Help window.

Use the HelpUseOnline property to indicate that you want to link a VI to a web-based
help file from the Context Help window.

Syntax

object.HelpDocumentUrl

                                                    © National Instruments 6391

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6391 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6392 ordinal=6392 -->
## Property and Method Reference

Property and Method Reference

     Data Type

        string

      HelpUseOnlineHelpUseOnline

       Indicates whether to link to a web-based help file from the Detailed help link in the
      Context Help window for a VI.

      Use the HelpDocumentURL property to specify the URL of the web-based help file.

     Syntax

     object.HelpUseOnline
     Data Type

      bool

      HistAddCommentsAtSaveHistAddCommentsAtSave

       Indicates whether to add a comment to the VI revision history every time the VI is
       saved.

       This property is similar to the options available in the LabVIEW History window.

     Syntax

     object.HistAddCommentsAtSave
     Data Type

        string

       HistoryTextHistoryText

       Returns all the text that was added to the VI revision history. This property is read only.


6392   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6392 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6393 ordinal=6393 -->
## Property and Method Reference

Property and Method Reference

Syntax

object.HistoryText
Data Type

string

HistPromptAtCloseHistPromptAtClose

Indicates whether to prompt for a VI revision history comment when the VI closes.

This property is similar to the options available in the LabVIEW History window.

Syntax

object.HistPromptAtClose
Data Type

Boolean

HistPromptForCommentsAtSaveHistPromptForCommentsAtSave

Indicates whether to prompt for a VI revision history comment when the VI is saved.

This property is similar to the options available in the LabVIEW History window.

Syntax

object.HistPromptForCommentsAtSave
Data Type

Boolean

HistRecordAppCommentsHistRecordAppComments

Indicates whether to add comments to the VI revision history when certain events
occur, such as conversion to a new version of LabVIEW, subVI changes, and changes to


                                                    © National Instruments 6393

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6393 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6394 ordinal=6394 -->
## Property and Method Reference

Property and Method Reference

       the name or path of the VI.

       This property is similar to the options available in the LabVIEW Revision History
       Properties page of the VI Properties dialog box or the Revision History page of the
      Options dialog box.

     Syntax

     object.HistRecordAppComments
     Data Type

      Boolean

      HistUseDefaultsHistUseDefaults

       Indicates whether to use the global default history or to use the values entered in other
       history properties.

       This property is similar to the options available in the Revision History page of the
      LabVIEW VI Properties dialog box. You can specify the global default history in the
      LabVIEW VI Properties dialog box.

     Syntax

     object.HistUseDefaults
     Data Type

      Boolean

       IsCloneVIIsCloneVI

       Returns TRUE if the VI is a clone VI.

     Syntax

     object.IsCloneVI


6394   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6394 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6395 ordinal=6395 -->
## Property and Method Reference

Property and Method Reference

Data Type

Boolean

IsProbeIsProbe

Returns TRUE if the VI is running as a probe and the probe VI is open.

Syntax

object.IsProbe
Data Type

Boolean

IsReentrantIsReentrant

Indicates whether a VI can be reentrant.

Syntax

object.IsReentrant
Data Type

Boolean

LibraryLibrary

Returns the name of the LabVIEW project library, XControl, or LabVIEW class that owns
the VI. If no library, XControl, or class owns the VI, the property returns NULL.

Syntax

object.Library
Data Type

Library*

                                                    © National Instruments 6395

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6395 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6396 ordinal=6396 -->
## Property and Method Reference

Property and Method Reference

      LogAtFinishLogAtFinish

       Indicates whether to write LabVIEW front panel values to a datalog file after the VI runs.

           Note If you set LogAtFinish without having set the LogFilePath property, the
              next time this VI finishes executing, a dialog box appears prompting you to
               specify the file path.

     Syntax

     object.LogAtFinish
     Data Type

      Boolean

      LogFilePathLogFilePath

      Path of the datalog file in which LabVIEW front panel data and a time stamp are
        written.

           Note Use this property in conjunction with the LogAtFinish property, which
                specifies whether to log the data. If you set the LogAtFinish property without
               also setting this property, a dialog box appears at run time, prompting you to
               specify a file path.

     Syntax

     object.LogFilePath
     Data Type

        string

     NameName

     Name of the VI file. You can write this property only if the VI has not been saved to disk.
           If a LabVIEW project library owns the VI, this property returns the qualified name of the

6396   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6396 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6397 ordinal=6397 -->
## Property and Method Reference

Property and Method Reference

VI, which includes the project library filename.

Syntax

object.Name
Data Type

string

OwningAppOwningApp

Returns a reference to the Application that owns this VI. Close this reference when you
are finished using it.

Syntax

object.OwningApp
Data Type

Application*

PathPath

Path to the VI file. This property is read only.

Syntax

object.Path
Data Type

string

PreferredExecSystemPreferredExecSystem

Indicates the execution system in which the VI runs.


                                                    © National Instruments 6397

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6397 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6398 ordinal=6398 -->
## Property and Method Reference

Property and Method Reference

     Syntax

     object.PreferredExecSystem
     Data Type

      VIExecSysEnum

      PrintHeaderDatePrintPrintHeaderDatePrint

           If TRUE, LabVIEW includes the date printed in the headers for the VI. Use the
       PrintingHeaders property to set whether LabVIEW prints the headers for the VI.

     Syntax

     object.PrintHeaderDatePrint
     Data Type

      Boolean

      PrintHeaderModifyDatePrintHeaderModifyDate

           If TRUE, LabVIEW includes the last modified date in the headers for the VI. Use the
       PrintingHeaders property to set whether LabVIEW prints the headers for the VI.

     Syntax

     object.PrintHeaderModifyDate
     Data Type

      Boolean

      PrintHeaderPageNumberPrintHeaderPageNumber

           If TRUE, LabVIEW includes the page number in the headers for the VI. Use the
       PrintingHeaders property to set whether LabVIEW prints the headers for the VI.


6398   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6398 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6399 ordinal=6399 -->
## Property and Method Reference

Property and Method Reference

Syntax

object.PrintHeaderPageNumber
Data Type

Boolean

PrintHeaderVIIconPrintHeaderVIIcon

If TRUE, LabVIEW includes the VI icon in the headers for the VI. Use the PrintingHeaders
property to set whether LabVIEW prints the headers for the VI.

Syntax

object.PrintHeaderVIIcon
Data Type

Boolean

PrintHeaderVINamePrintHeaderVIName

If TRUE, LabVIEW includes the VI name in the headers for the VI. Use the
PrintingHeaders property to set whether LabVIEW prints the headers for the VI.

Syntax

object.PrintHeaderVIName
Data Type

Boolean

PrintingBDScalingPrintingBDScaling

If TRUE, LabVIEW scales the block diagram to fit on the printed page.

This property is similar to the Scale printed block diagram to fit page checkbox on the
Print Options page of the LabVIEW VI Properties dialog box.


                                                    © National Instruments 6399

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6399 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6400 ordinal=6400 -->
## Property and Method Reference

Property and Method Reference

     Syntax

     object.PrintingBDScaling
     Data Type

      Boolean

       PrintingFPScalingPrintingFPScaling

           If TRUE, LabVIEW scales the front panel to fit on the printed page.

       This property is similar to the Scale printed front panel to fit page checkbox on the
       Print Options page of the LabVIEW VI Properties dialog box.

     Syntax

     object.PrintingFPScaling
     Data Type

      Boolean

      PrintingHeadersPrintingHeaders

           If TRUE, LabVIEW prints headers for the VI. Use the PrintHeader properties in this class
       to customize the contents of the headers.

       This property is similar to the Print header (name, date, page number) checkbox on
       the Print Options page of the LabVIEW VI Properties dialog box.

     Syntax

     object.PrintingHeaders
     Data Type

      Boolean


6400   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6400 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6401 ordinal=6401 -->
## Property and Method Reference

Property and Method Reference

PrintingHeaderVIPathPrintingHeaderVIPath

If TRUE, LabVIEW includes the VI path in the headers for the VI. Use the
PrintingHeaders property to set whether LabVIEW prints the headers for the VI.

Syntax

object.PrintingHeaderVIPath
Data Type

Boolean

PrintingOrientationPrintingOrientation

Gets or sets the page orientation to use when printing the VI.

Syntax

object.PrintingOrientation
Data Type

PageOrientationEnum

PrintLogFileAtFinishPrintLogFileAtFinish

Indicates whether to print the LabVIEW front panel after the VI runs.

Syntax

object.PrintLogFileAtFinish
Data Type

Boolean

PrintMarginsPrintMargins

Gets or sets the page margins to use when printing the VI in inches or centimeters.

                                                    © National Instruments 6401

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6401 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6402 ordinal=6402 -->
## Property and Method Reference

Property and Method Reference

       This property is similar to the Use custom page margins checkbox on the Print
      Options page of the LabVIEW VI Properties dialog box.

     Syntax

     object.PrintMargins
     Data Type

      PrintMarginsEnum

      ReentrancyTypeReentrancyType

       Indicates the type of reentrancy LabVIEW uses for a reentrant VI. This property is
        similar to options on the Execution Properties page of the VI Properties dialog box.

     Syntax

     object.ReentrancyType
     Data Type

      kReentrancyTypeTD

      RevisionNumberRevisionNumber

       Current revision number of the VI.

     When writing this property, you can write only a value greater than the current revision
      number. If you attempt to write a revision number whose value is less than the current
       revision number, the property returns an error.

       This property is similar to the options available in the Revision History page of the
      LabVIEW VI Properties dialog box.

     Syntax

     object.RevisionNumber


6402   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6402 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6403 ordinal=6403 -->
## Property and Method Reference

Property and Method Reference

Data Type

long

RunOnOpenRunOnOpen

Indicates whether to run the VI when it opens.

Syntax

object.RunOnOpen
Data Type

Boolean

RunTimeMenuPathRunTimeMenuPath

When read, this property returns the run-time menu path of the VI. When written, this
property updates the run-time menu path of the VI. If the VI is running when you write
this property, it updates the menu with data from the new path.

Use this property to programmatically specify the path for a run-time menu (.rtm)
file. This is useful if you are developing multilingual applications and you want to
switch menus for each language programmatically.

Syntax

object.RunTimeMenuPath
Data Type

string

ShowFPOnCallShowFPOnCall

Indicates whether to show the LabVIEW front panel when the VI is called.


                                                    © National Instruments 6403

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6403 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6404 ordinal=6404 -->
## Property and Method Reference

Property and Method Reference

     Syntax

     object.ShowFPOnCall
     Data Type

      Boolean

     ShowFPOnLoadShowFPOnLoad

       Indicates whether to show the LabVIEW front panel when the VI is loaded.

     Syntax

     object.ShowFPOnLoad
     Data Type

      Boolean

      SuspendOnCallSuspendOnCall

       Indicates whether the VI should be suspended when it is called as a subVI. Use this
       property carefully with reentrant VIs.

     Syntax

     object.SuspendOnCall
     Data Type

      Boolean

      TBShowAbortButtonTBShowAbortButton

       Indicates whether to display the Abort Execution button on the LabVIEW toolbar while
       the VI runs.

       This property is similar to the Show Abort button option on the LabVIEW Customize
     Window Appearance dialog box.


6404   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6404 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6405 ordinal=6405 -->
## Property and Method Reference

Property and Method Reference

Syntax

object.TBShowAbortButton
Data Type

Boolean

TBShowFreeRunButtonTBShowFreeRunButton

Indicates whether to display the Run Continuously button on the LabVIEW toolbar
while the VI runs.

Syntax

object.TBShowFreeRunButton
Data Type

Boolean

TBShowRunButtonTBShowRunButton

Indicates whether to display the Run button on the LabVIEW toolbar while the VI runs.

Syntax

object.TBShowRunButton
Data Type

Boolean

TBVisibleTBVisible

Indicates whether to display the LabVIEW toolbar while the VI runs.

Syntax

object.TBVisible


                                                    © National Instruments 6405

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6405 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6406 ordinal=6406 -->
## Property and Method Reference

Property and Method Reference

     Data Type

      Boolean

      VITypeVIType

       Indicates the type of the VI.

       This property returns one of the following values:

            • Invalid VI type—LabVIEW returns the Invalid VI type value for invalid VI references.
            • Standard VI—LabVIEW returns the Standard VI value for VIs you create that contain
         a front panel and block diagram.
            • Control VI—LabVIEW returns the Control VI value for subVIs you create to define a
         custom control or indicator.
            • Global VI—LabVIEW returns the Global VI value for subVIs you create when creating
           global variables.
            • Polymorphic VI—LabVIEW returns the Polymorphic VI value for subVIs you create
          as a collection of VIs with the same connector pane patterns. Each VI in the
           collection is an instance of the polymorphic VI.
            • Configuration VI—The Configuration VI type is not supported.
            • SubSystem—LabVIEW returns the SubSystem value for subVIs for the LabVIEW
          Control Design and Simulation Module that you can place only on a simulation
          diagram.
            • Facade VI—LabVIEW returns the Facade VI value for subVIs that LabVIEW creates
        when you create an XControl. A Facade VI represents a Facade ability, which
           defines the appearance of an XControl.
            • Method VI—LabVIEW returns the Method VI value for subVIs that LabVIEW creates
            for each XControl method you create and add to the XControl Library.

     Syntax

     object.VIType
     Data Type

      VITypeEnum


6406   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6406 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6407 ordinal=6407 -->
## Property and Method Reference

Property and Method Reference

DataSocketDataSocket PropertiesProperties


 Property                  Description

 Buffer Maximum Bytes     Get or set DataSocket buffer maximum bytes.

 Buffer Maximum Packets    Get or set DataSocket buffer maximum packets.

 Buffer Utilization (Bytes)    Returns DataSocket buffer utilization (current bytes / max bytes).

 Buffer Utilization (Packets)  Returns DataSocket buffer utilization (current packets / max packets).

 Connection Status         Returns DataSocket connection status.

 URL                      Returns DataSocket URL.

BufferBuffer MaximumMaximum BytesBytes

Get or set DataSocket buffer maximum bytes.

Remarks

The following table lists the characteristics of this property.


 Data type

 Permissions                                                          Read/Write

 Available in Run-Time Engine                                             Yes

 Available in Real-Time Operating System                                  Yes

BufferBuffer MaximumMaximum PacketsPackets

Get or set DataSocket buffer maximum packets.

Remarks

The following table lists the characteristics of this property.


 Data type

                                                    © National Instruments 6407

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6407 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6408 ordinal=6408 -->
## Property and Method Reference

Property and Method Reference


         Permissions                                                          Read/Write

         Available in Run-Time Engine                                             Yes

         Available in Real-Time Operating System                                  Yes

     BufferBuffer UtilizationUtilization (Bytes)(Bytes)

       Returns DataSocket buffer utilization (current bytes / max bytes).

      Remarks

      The following table lists the characteristics of this property.


        Data type

         Permissions                                                     Read Only

         Available in Run-Time Engine                                              Yes

         Available in Real-Time Operating System                                   Yes

     BufferBuffer UtilizationUtilization (Packets)(Packets)

       Returns DataSocket buffer utilization (current packets / max packets).

      Remarks

      The following table lists the characteristics of this property.


        Data type

         Permissions                                                     Read Only

         Available in Run-Time Engine                                              Yes

         Available in Real-Time Operating System                                   Yes


6408   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6408 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6409 ordinal=6409 -->
## Property and Method Reference

Property and Method Reference

ConnectionConnection StatusStatus

Returns DataSocket connection status.

Remarks

The following table lists the characteristics of this property.


 Data type

 Permissions                                                     Read Only

 Available in Run-Time Engine                                              Yes

 Available in Real-Time Operating System                                   Yes

URLURL

Returns DataSocket URL.

Remarks

The following table lists the characteristics of this property.


 Data type

 Permissions                                                     Read Only

 Available in Run-Time Engine                                              Yes

 Available in Real-Time Operating System                                   Yes

FilesystemFilesystem StatisticsStatistics

Contains statistics for an SFTP-accessible filesystem. Use the Filesystem Statistics
Node to read total and free disk space.

FilesystemFilesystem StatisticsStatistics PropertiesProperties


                                                    © National Instruments 6409

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6409 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6410 ordinal=6410 -->
## Property and Method Reference

Property and Method Reference


        Property  Description

        Get Bytes                 Reads the free space, in bytes, reported for a filesystem on an SFTP server.         Free VI

        Get Bytes                 Reads the total space, in bytes, reported for a filesystem of an SFTP server.         Total VI

                   Returns TRUE if this Filesystem Statistics object represents a read-only filesystem.
           Is Read
        Only VI    Read-only filesystems contains files whose attributes indicate they are writable.
                  However, no files can be modified, created, renamed, or deleted.


     GetGet BytesBytes FreeFree VIVI

      Reads the free space, in bytes, reported for a filesystem on an SFTP server.

     Remarks

      The following table lists the characteristics of this property.


        Data type

         Permissions                                                     Read Only

         Available in Run-Time Engine                                              Yes

         Available in Real-Time Operating System                                   Yes

         Settable when the VI is running                                            Yes

        Loads the front panel into memory                                         Yes

       Need to authenticate before use                                 No

        Loads the block diagram into memory                             No

     GetGet BytesBytes TotalTotal VIVI

      Reads the total space, in bytes, reported for a filesystem of an SFTP server.


6410   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6410 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6411 ordinal=6411 -->
## Property and Method Reference

Property and Method Reference

Remarks

The following table lists the characteristics of this property.


 Data type

 Permissions                                                     Read Only

 Available in Run-Time Engine                                              Yes

 Available in Real-Time Operating System                                   Yes

 Settable when the VI is running                                            Yes

 Loads the front panel into memory                                         Yes

 Need to authenticate before use                                 No

 Loads the block diagram into memory                             No

IsIs ReadRead OnlyOnly VIVI

Returns TRUE if this Filesystem Statistics object represents a read-only filesystem.

Read-only filesystems contains files whose attributes indicate they are writable.
However, no files can be modified, created, renamed, or deleted.

Remarks

The following table lists the characteristics of this property.


 Data type

 Permissions                                                     Read Only

 Available in Run-Time Engine                                              Yes

 Available in Real-Time Operating System                                   Yes

 Settable when the VI is running                                            Yes

 Loads the front panel into memory                                         Yes

 Need to authenticate before use                                 No

 Loads the block diagram into memory                             No

                                                    © National Instruments 6411

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6411 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6412 ordinal=6412 -->
## Property and Method Reference

Property and Method Reference

    LabVIEWLabVIEW ManagerManager FunctionsFunctions

       This book describes the LabVIEW Manager functions that you can call from external C/
      C++ code to interact with the underlying infrastructure of LabVIEW. You can use these
       functions to perform simple and complex operations, ranging from low-level byte
       manipulation to sorting data and managing memory.

      Complete the following steps to use these functions.

         1. Include the header file extcode.h and link to labviewv.lib in any C/C++ files
         from which you want to call the functions.
         2. Use the function signatures in this book to call the functions.
         3. Create a shared library of these source files.
         4. Use the Call Library Function Node to call the shared library in LabVIEW.

      FileFile ManagerManager FunctionsFunctions

      The file manager functions can create, open and close files, write data to files, and
       read data from files. In addition, file manager routines can create directories,
      determine characteristics of files and directories, and copy files.

      The file manager defines the Path data type for use in describing paths to files and
        directories. The data structure for the Path data type is private. Use file manager
       routines to create and manipulate the Path data type.

      You must include the appropriate header and library files to use these functions in a
      shared library.

      You can perform the following operations by using the functions listed.

            • Current position mark, positioning
     ◦ FMSeek
     ◦ FMTell
            • Default access rights information, getting
     ◦ FGetDefGroup
            • Directory contents, creating and determining
     ◦ FListDir

6412   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6412 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6413 ordinal=6413 -->
## Property and Method Reference

Property and Method Reference

 ◦ FNewDir
• End-of-file mark, positioning
 ◦ FGetEOF
 ◦ FSetEOF
•  File data to disk, flushing
 ◦ FFlush
•  File operations, performing basic
 ◦ FCreate
 ◦ FCreateAlways
 ◦ FMClose
 ◦ FMOpen
 ◦ FMRead
 ◦ FMWrite
•  File range, locking
 ◦ FLockOrUnlockRange
•  File refnums, manipulating
 ◦ FDisposeRefNum
 ◦ FIsARefNum
 ◦ FNewRefNum
 ◦ FRefNumToFD
 ◦ FRefNumToPath
•  File, directory, and volume information determination
 ◦ FExists
 ◦ FGetAccessRights
 ◦ FGetInfo
 ◦ FGetVolInfo
 ◦ FSetAccessRights
 ◦ FSetInfo
• Filenames and patterns, matching
 ◦ FStrFitsPat
• Files and directories, moving and deleting
 ◦ FMove
 ◦ FRemove
•  Files, copying
 ◦ FCopy
• Path type, determining
 ◦ FGetPathType


                                                   © National Instruments 6413

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6413 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6414 ordinal=6414 -->
## Property and Method Reference

Property and Method Reference

     ◦ FIsAPathOfType
     ◦ FSetPathType
            • Path, extracting information
     ◦ FDepth
     ◦ FDirName
     ◦ FName
     ◦ FNamePtr
     ◦ FVolName
            • Paths, comparing
     ◦ FIsAPath
     ◦ FIsAPathOrNotAPath
     ◦ FIsEmptyPath
     ◦ FPathCmp
            • Paths, converting to and from other representations
     ◦ FArrToPath
     ◦ FFlattenPath
     ◦ FPathToArr
     ◦ FPathToAZString
     ◦ FPathToDSString
     ◦ FStringToPath
     ◦ FTextToPath
     ◦ FUnFlattenPath
            • Paths, creating
     ◦ FAddPath
     ◦ FAppendName
     ◦ FAppPath
     ◦ FEmptyPath
     ◦ FMakePath
     ◦ FNotAPath
     ◦ FRelPath
            • Paths, disposing
     ◦ FDestroyPath
            • Paths, duplicating
     ◦ FPathCpy
     ◦ FPathToPath


6414   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6414 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6415 ordinal=6415 -->
## Property and Method Reference

Property and Method Reference

FAddPathFAddPath (LabVIEW(LabVIEW ManagerManager Function)Function)

MgErr FAddPath(basePath, relPath, newPath);

Purpose

Creates an absolute path by appending a relative path to an absolute path. You can
pass the same path variable for the new path that you use for basePath or relPath.
Therefore, you can call this function in the following three ways:

  • err = FAddPath(basePath, relPath, newPath);/* the new
   path is returned in a third path variable */
  • err = FAddPath(path, relPath, path); /* the new path
   writes over the old base path */
  • err = FAddPath(basepath, path, path); /* the new path
   writes over the old relative path */

Parameters

 Name       Type    Description

 basePath   Path   Absolute path to which you want to append a relative path.

 relPath     Path    Relative path you want to append to the existing base path.

 newPath    Path   Path returned byFAddPath.

Return Value

MgErr, which can contain the following errors. If you receive errors from LabVIEW
Manager functions, most error names correspond to LabVIEW error codes.


 Value               Corresponding Error Code or Description

 noErr           No error.

 mgArgErr          1

 mFullErr          2


                                                    © National Instruments 6415

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6415 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6416 ordinal=6416 -->
## Property and Method Reference

Property and Method Reference

    FAppendNameFAppendName (LabVIEW(LabVIEW ManagerManager Function)Function)

     MgErr FAppendName(path, name);

     Purpose

      Appends a file or directory name to an existing path.

     Parameters

      Name Type  Description

                    Base path to which you want to append a new file or directory name.
        path  Path                 FAppendName returns the resulting path in this parameter.

      name PStr  File or directory name you want to append to the existing path.

     Return Value

      MgErr, which can contain the following errors. If you receive errors from LabVIEW
      Manager functions, most error names correspond to LabVIEW error codes.


        Value               Corresponding Error Code or Description

       noErr           No error.

       mgArgErr          1

       mFullErr          2

     FAppPathFAppPath (LabVIEW(LabVIEW ManagerManager Function)Function)

     MgErr FAppPath(p);

     Purpose

       Indicates the path to the LabVIEW application currently running.


6416   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6416 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6417 ordinal=6417 -->
## Property and Method Reference

Property and Method Reference

Parameters

 Name Type  Description

              Path in which FAppPath stores the path to the current application. p must already p    Path
             be an allocated path.

Return Value

MgErr, which can contain the following errors. If you receive errors from LabVIEW
Manager functions, most error names correspond to LabVIEW error codes.


 Value                 Corresponding Error Code or Description

 noErr             No error.

 mgArgErr            1

 mFullErr            2

 fIOErr              6

 fNotFound          7

FArrToPathFArrToPath (LabVIEW(LabVIEW ManagerManager Function)Function)

MgErr FArrToPath(arr, relative, path);

Purpose

Converts a one-dimensional LabVIEW array of strings to a path of the type specified by
relative. Each string in the array is converted in order into a component name of the
resulting path.

If no error occurs, path is set to a path whose component names are the strings in arr.
If an error occurs, path is set to the canonical invalid path.


                                                    © National Instruments 6417

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6417 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6418 ordinal=6418 -->
## Property and Method Reference

Property and Method Reference

     Parameters

      Name   Type      Description

         arr    UHandle DS handle containing the array of strings you want to convert to a path.

                                              If TRUE, the resulting path is relative. Otherwise, the resulting path is          relative Bool32
                              absolute.

                           Path where FArrToPath stores the resulting path. This path must already        path   Path
                         have been allocated.

     Return Value

      MgErr, which can contain the following errors. If you receive errors from LabVIEW
      Manager functions, most error names correspond to LabVIEW error codes.


        Value               Corresponding Error Code or Description

       noErr           No error.

       mgArgErr          1

       mFullErr          2

     FCopyFCopy (LabVIEW(LabVIEW ManagerManager Function)Function)

     MgErr FCopy(oldPath, newPath);

     Purpose

      Copies a file, preserving the type, creator, and access rights. The file to be copied must
       not be open. If an error occurs, the new file is not created.

     Parameters

      Name      Type    Description

        oldPath    Path   Path of the file or directory you want to copy.

       newPath   Path   Path, including filename, where you want to store the new file.


6418   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6418 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6419 ordinal=6419 -->
## Property and Method Reference

Property and Method Reference

Return Value

MgErr, which can contain the following errors. If you receive errors from LabVIEW
Manager functions, most error names correspond to LabVIEW error codes.


 Value                 Corresponding Error Code or Description

 noErr             No error.

 mgArgErr            1

 mFullErr            2

 fIsOpen             5

 fIOErr              6

 fNotFound          7

 fNoPerm             8

 fDiskFull          9

 fDupPath            10

 fTMFOpen            11

FCreateFCreate (LabVIEW(LabVIEW ManagerManager Function)Function)

MgErr FCreate(fdp, path, permissions, openMode, denyMode,
group);

Purpose

Creates a file with the name and location specified by path and with the specified
permissions, and opens it for writing and reading, as specified by openMode. If the file
already exists, the function returns an error.

You can use denyMode to control concurrent access to the file from within LabVIEW.
You can use the group parameter to assign the file to a Linux group. LabVIEW ignores
group on Windows and Mac OS X.

If the function creates the file, the resulting file descriptor is stored in the address


                                                    © National Instruments 6419

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6419 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6420 ordinal=6420 -->
## Property and Method Reference

Property and Method Reference

       referred to by fdp. If an error occurs, the function stores 0 in the address referred to by
      fdp and returns an error.

           Note Before you call this function, ensure that you understand how to use
               pointers as parameters.

     Parameters

      Name      Type    Description

                File   Address at which FCreate stores the file descriptor for the new file. If
        fdp
                *     FCreate fails, it stores 0 in the address fdp. This parameter is a pointer.

        path       Path   Path of the file you want to create.

        permissions int32 Permissions to assign to the new file.

                             Access mode to use in opening the file. The following values are defined in
                             the file extcode.h.

       openMode  int32     • openReadOnly—Open for reading.
                                               • openWriteOnly—Open for writing.
                                               • openReadWrite—Open for both reading and writing.

                       Mode that determines what level of concurrent access to the file is allowed.
                          The following values are defined in the file extcode.h.

                                               • denyReadWrite—Prevents others from reading from and writing to
                                 the file while it is open.
       denyMode  int32
                                               • denyWriteOnly—Prevents others from writing to the file only while
                                                     it is open.
                                               • denyNeither—Allows others to read from and write to the file while
                                                     it is open.

        group      PStr   Linux group you want to assign to the new file.

     Return Value

      MgErr, which can contain the following errors. If you receive errors from LabVIEW
      Manager functions, most error names correspond to LabVIEW error codes.


6420   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6420 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6421 ordinal=6421 -->
## Property and Method Reference

Property and Method Reference


 Value         Corresponding Error Code or Description

 noErr       No error.

 mgArgErr    1

 fIsOpen       5. This error is returned only on Mac OS X. Windows returns fIOErr.

 fIOErr       6

 fNoPerm     8

 fDupPath    10

 fTMFOpen    11

FCreateAlwaysFCreateAlways (LabVIEW(LabVIEW ManagerManager Function)Function)

MgErr FCreateAlways(fdp, path, permissions, openMode,
denyMode, group);

Purpose

Creates a file with the name and location specified by path and with the specified
permissions, and opens the file for writing and reading, as specified by openMode. If
the file already exists, this function opens and truncates the file.

You can use denyMode to control concurrent access to the file from within LabVIEW.
You can use the group parameter to assign the file to a Linux group. LabVIEW ignores
group on Windows and Mac OS X.

If the function creates the file, the resulting file descriptor is stored in the address
referred to by fdp. If an error occurs, the function stores 0 in the address referred to by
fdp and returns an error.

      Note Before you call this function, ensure that you understand how to use
        pointers as parameters.


                                                    © National Instruments 6421

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6421 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6422 ordinal=6422 -->
## Property and Method Reference

Property and Method Reference

     Parameters

      Name      Type    Description

                            Address at which FCreateAlways stores the file descriptor for the new
                File
        fdp                           file. If FCreateAlways fails, it stores 0 in the address fdp. This parameter
                *
                                         is a pointer.

        path       Path   Path of the file you want to create.

        permissions int32 Permissions to assign to the new file.

                             Access mode to use in opening the file. The following values are defined in
                             the file extcode.h.

       openMode  int32     • openReadOnly—Open for reading.
                                               • openWriteOnly—Open for writing.
                                               • openReadWrite—Open for both reading and writing.

                       Mode that determines what level of concurrent access to the file is allowed.
                          The following values are defined in the file extcode.h.

                                               • denyReadWrite—Prevents others from reading from and writing to
                                 the file while it is open.
       denyMode  int32
                                               • denyWriteOnly—Prevents others from writing to the file only while
                                                     it is open.
                                               • denyNeither—Allows others to read from and write to the file while
                                                     it is open.

        group      PStr   Linux group you want to assign to the new file.

     Return Value

      MgErr, which can contain the following errors. If you receive errors from LabVIEW
      Manager functions, most error names correspond to LabVIEW error codes.


        Value         Corresponding Error Code or Description

       noErr       No error.

       mgArgErr    1

       fIsOpen       5. This error is returned only on Mac OS X. Windows returns fIOErr.

6422   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6422 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6423 ordinal=6423 -->
## Property and Method Reference

Property and Method Reference


 Value         Corresponding Error Code or Description

 fIOErr       6

 fNoPerm     8

 fDupPath    10

 fTMFOpen    11

FDepthFDepth (LabVIEW(LabVIEW ManagerManager Function)Function)

int32 FDepth(path);

Purpose

Computes the depth, or number of component names, of a path.

Parameters

 Name      Type       Description

 path      Path      Path whose depth you want to determine.

Return Value

int32, indicating the depth of the path, which can contain the following values.


 Value   Description

 –1     Badly formed path.

 0      Path is the root directory.

 1      Path is in the root directory.

 2      Path is in a subdirectory of the root directory, one level from the root directory.

 n–1    Path is n–2 levels from the root directory.

 N      Path is n–1 levels from the root directory.


                                                    © National Instruments 6423

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6423 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6424 ordinal=6424 -->
## Property and Method Reference

Property and Method Reference

     FDestroyPathFDestroyPath (LabVIEW(LabVIEW ManagerManager Function)Function)

     void FDestroyPath(&pp);

     Purpose

       Release the memory of an allocated path and NULL the path pointer.

     Parameters

      Name     Type          Description

       pp       Path *      A pointer to the path you want to deallocate.

     Return Value

      None.

           Note This function replaces the older FDisposePath function. The older
               function is still available, but its use is discouraged. By passing a pointer to
              the path instead of the path directly, the FDestroyPath function can
              properly NULL out the path, thus preventing double deallocation errors. The
           new function also can handle NULL paths, eliminating the need to check for
           NULL prior to calling FDisposePath. A typical use of the new function is
                 illustrated by the following text:


         Path p;
         p = FNotAPath(NULL);
         // insert code here that uses the path
         FDestroyPath(&p);
         // p == NULL at this point

     FDirNameFDirName (LabVIEW(LabVIEW ManagerManager Function)Function)

     MgErr FDirName(path, dir);


6424   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6424 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6425 ordinal=6425 -->
## Property and Method Reference

Property and Method Reference

Purpose

Creates a path for the parent directory of a specified path. You can pass the same path
variable for the parent path that you use for path. Therefore, you can call this function
in the following two ways:

  • err = FDirName(path, dir);/* the parent path is returned
   in a second path variable */
  • err = FDirName(path, path);/* the parent path writes over
   the existing path */

Parameters

 Name    Type     Description

 path    Path    Path whose parent path you want to determine.

 dir      Path    Parameter in which FDirName stores the parent path.

Return Value

MgErr, which can contain the following errors. If you receive errors from LabVIEW
Manager functions, most error names correspond to LabVIEW error codes.


 Value               Corresponding Error Code or Description

 noErr           No error.

 mgArgErr          1

FDisposeRefNumFDisposeRefNum (LabVIEW(LabVIEW ManagerManager Function)Function)

MgErr FDisposeRefNum(refNum);

Purpose

Disposes of the specified file refNum.


                                                    © National Instruments 6425

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6425 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6426 ordinal=6426 -->
## Property and Method Reference

Property and Method Reference

     Parameters

      Name       Type              Description

       refNum     LVRefNum          File refnum of which you want to dispose.

     Return Value

      MgErr, which can contain the following errors. If you receive errors from LabVIEW
      Manager functions, most error names correspond to LabVIEW error codes.


        Value               Corresponding Error Code or Description

       noErr           No error.

       mgArgErr          1

     FEmptyPathFEmptyPath (LabVIEW(LabVIEW ManagerManager Function)Function)

     Path FEmptyPath(p);

     Purpose

      Makes an empty absolute path, which is not the same as disposing the path.

     Parameters

      Name Type  Description

                      Path allocated by FEmptyPath. If NULL, FEmptyPath allocates a new path and
       p    Path  returns the value. If p is a path, FEmptyPath sets the existing path to an empty
                     path and returns the new p.

     Return Value

      The resulting path; if p was not NULL, the return value is the same empty absolute
      path as p. If an error occurs, this function returns NULL.


6426   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6426 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6427 ordinal=6427 -->
## Property and Method Reference

Property and Method Reference

FExistsFExists (LabVIEW(LabVIEW ManagerManager Function)Function)

int32 FExists(path);

Purpose

Returns information about the specified file or directory. It returns less information
than FGetInfo, but it is much quicker on most platforms.

Parameters

 Name   Type    Description

 path    Path   Path of the file or directory about which you want information.

Return Value

int32, which can contain the following values.


 Value                      Description

 kFIsFile                 Specified item is a file.

 kFIsFolder               Specified item is a directory or folder.

 kFNotExist               Specified item does not exist.

FFlattenPathFFlattenPath (LabVIEW(LabVIEW ManagerManager Function)Function)

int32 FFlattenPath(p, fp);

Purpose

Converts path into a flat form that you can use to write the path as information to a
file. This function stores the resulting flat path in a pre-allocated buffer and returns the
number of bytes.

To determine the size needed for the flattened path, pass NULL for fp. The function
returns the necessary size without writing anything into the location pointed to by fp.

                                                    © National Instruments 6427

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6427 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6428 ordinal=6428 -->
## Property and Method Reference

Property and Method Reference

     Parameters

      Name Type  Description

        path  Path Path you want to flatten.

                      Address in which FFlattenPath stores the resulting flattened path. If NULL,
         fp    UPtr FFlattenPath does not write anything to this address, but does return the size
                        that the flattened path would require. This parameter is a pointer.

     Return Value

      int32, indicating the number of bytes required to store the flattened path.

     FFlushFFlush (LabVIEW(LabVIEW ManagerManager Function)Function)

     MgErr FFlush(fd);

     Purpose

       Writes any buffered data for the specified file out to the disk.

     Parameters

      Name      Type        Description

         fd        File         File descriptor associated with the file.

     Return Value

      MgErr, which can contain the following errors. If you receive errors from LabVIEW
      Manager functions, most error names correspond to LabVIEW error codes.


        Value               Corresponding Error Code or Description

       noErr           No error.

       mgArgErr          1

       fIOErr            6


6428   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6428 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6429 ordinal=6429 -->
## Property and Method Reference

Property and Method Reference

FGetAccessRightsFGetAccessRights (LabVIEW(LabVIEW ManagerManager Function)Function)

MgErr FGetAccessRights(path, owner, group, permPtr);

Purpose

Returns access rights information about the specified file or directory.

Parameters

 Name   Type      Description

 path    Path     Path of the file or directory about which you want access rights information.

                    Address at which FGetAccessRights stores the owner of the file or owner   PStr
                        directory.

                    Address at which FGetAccessRights stores the group of the file or group   PStr
                        directory.

                    Address at which FGetAccessRights stores the permissions of the file or permPtr int32 *
                        directory. This parameter is a pointer.

Return Value

MgErr, which can contain the following errors. If you receive errors from LabVIEW
Manager functions, most error names correspond to LabVIEW error codes.


 Value                 Corresponding Error Code or Description

 noErr             No error.

 mgArgErr            1

 fIOErr              6

 fNotFound          7

FGetDefGroupFGetDefGroup (LabVIEW(LabVIEW ManagerManager Function)Function)

LStrHandle FGetDefGroup(groupHandle);


                                                    © National Instruments 6429

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6429 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6430 ordinal=6430 -->
## Property and Method Reference

Property and Method Reference

     Purpose

       Gets the LabVIEW default group for a file or directory.

     Parameters

      Name       Type          Description

                                  Handle that represents the LabVIEW default group for a file or
                                          directory. If groupHandle is NULL, FGetDefGroup allocates a
        groupHandle LStrHandle new handle and returns the default group in it. If groupHandle is a
                                      handle, FGetDefGroup returns it, and groupHandle resizes to
                                    hold the default group.

     Return Value

      The resulting LStrHandle. If groupHandle was not NULL, the return value is the
     same LStrHandle as groupHandle. If an error occurs, this function returns NULL.

     FGetEOFFGetEOF (LabVIEW(LabVIEW ManagerManager Function)Function)

     MgErr FGetEOF(fd, sizep);

     Purpose

       Returns the size of the specified file.

     Parameters

      Name Type      Description

         fd    File       File descriptor associated with the file.

                         Address at which FGetEOF stores the size of the file in bytes. If an error occurs,         sizep  int32 *
                           *sizep is undefined. This parameter is a pointer.

     Return Value

      MgErr, which can contain the following errors. If you receive errors from LabVIEW

6430   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6430 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6431 ordinal=6431 -->
## Property and Method Reference

Property and Method Reference

Manager functions, most error names correspond to LabVIEW error codes.


 Value               Corresponding Error Code or Description

 noErr           No error.

 mgArgErr          1

 fIOErr            6

FGetInfoFGetInfo (LabVIEW(LabVIEW ManagerManager Function)Function)

MgErr FGetInfo(path, infop);

Purpose

Returns information about the specified file or directory.

Parameters

 Name Type        Description

 path  Path       Path of the file or directory about which you want information.

                   Address where FGetInfo stores information about the file or directory. If an infop  FInfoPtr
                      error occurs, infop is undefined. This parameter is a pointer.

FInfoPtr is a data structure that defines the attributes of a file or directory. The
following code lists the file/directory information record, FInfoPtr.


 typedef struct {
         int32        type;        /* system specific file type-- 0 for directories
 */
         int32        creator;        /* system specific file creator-- 0 for
 folders (on Mac only)*/
         int32        permissions;        /* system specific file access rights */
         int32        size;        /* file size in bytes (data fork on Mac) or
 entries in directory*/
         int32        rfSize;        /* resource fork size (on Mac only) */
         uint32        cdate;        /* creation date: seconds since system
 reference time */


                                                    © National Instruments 6431

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6431 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6432 ordinal=6432 -->
## Property and Method Reference

Property and Method Reference


                 uint32        mdate;        /* last modification date: seconds since system
         ref time */
                 Bool32        folder;        /* indicates whether path refers to a folder
         */
                 Bool32        isInvisible;        /* indicates whether file is visible in
         File Dialog (on Mac only)*/
                 Point        location;        /* system specific desktop geographical
         location (on Mac only)*/
                 Str255        owner;        /* owner (in pascal string form) of file or
         folder */
                 Str255        group;        /* group (in pascal string form) of file or
         folder */
                 }        FInfoRec, *FInfoPtr;

     Return Value

      MgErr, which can contain the following errors. If you receive errors from LabVIEW
      Manager functions, most error names correspond to LabVIEW error codes.


        Value                 Corresponding Error Code or Description

       noErr             No error.

       mgArgErr            1

       fIOErr              6

       fNotFound          7

     FGetPathTypeFGetPathType (LabVIEW(LabVIEW ManagerManager Function)Function)

      MgErr FGetPathType(path, typePtr)

     Purpose

       Returns the type, relative, absolute, or <Not a Path>, of a path.

     Parameters

      Name   Type      Description

        path   Path     Path whose type you want to determine.

6432   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6432 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6433 ordinal=6433 -->
## Property and Method Reference

Property and Method Reference


 Name   Type      Description

                   Address at which FGetPathType stores the type. *typePtr can have the
                     following values:

                                 • fAbsPath—The path is absolute.
 typePtr int32 *
                                 • fRelPath—The path is relative.
                                 • fNotAPath—The path is the canonical invalid path or an error occurred.

                     This parameter is a pointer.

Return Value

MgErr, which can contain the following errors. If you receive errors from LabVIEW
Manager functions, most error names correspond to LabVIEW error codes.


 Value               Corresponding Error Code or Description

 noErr           No error.

 mgArgErr          1

FGetVolInfoFGetVolInfo (LabVIEW(LabVIEW ManagerManager Function)Function)

MgErr FGetVolInfo(path, vinfo);

Purpose

Gets a path specification and information for the volume containing the specified file
or directory.

Parameters

 Name Type          Description

                      Path of a file or directory contained on the volume from which you want to
                       get information. This path is overwritten with a path specifying the volume
 path  Path                       containing the specified file or directory. If an error occurs, path is
                       undefined.

 vinfo  VInfoRec * Address at which FgetVolInfo stores the information about the volume.

                                                    © National Instruments 6433

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6433 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6434 ordinal=6434 -->
## Property and Method Reference

Property and Method Reference


      Name Type          Description

                                                  If an error occurs, vinfo is undefined. This parameter is a pointer.

      The following code describes the volume information record, VInfoRec.


         typedef struct {
                 uint32        size;        /* size in bytes of a volume */
                 uint32        used;        /* number of bytes used on volume */
                 uint32        free;        /* number of bytes available for use on volume
         */
         }        VInfoRec;

     Return Value

      MgErr, which can contain the following errors. If you receive errors from LabVIEW
      Manager functions, most error names correspond to LabVIEW error codes.


        Value               Corresponding Error Code or Description

       noErr           No error.

       mgArgErr          1

       fIOErr            6

      FIsAPathFIsAPath (LabVIEW(LabVIEW ManagerManager Function)Function)

     Bool32 FIsAPath(path);

     Purpose

      Determines whether path is a valid path.

     Parameters

      Name           Type             Description

        path          Path           Path you want to verify.


6434   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6434 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6435 ordinal=6435 -->
## Property and Method Reference

Property and Method Reference

Return Value

Bool32, which can contain the following values.


 Value        Description

 TRUE        Path is well formed and type is absolute or relative.

 FALSE      Path is not valid.

FIsAPathOfTypeFIsAPathOfType (LabVIEW(LabVIEW ManagerManager Function)Function)

Bool32 FIsAPathOfType(path, ofType);

Purpose

Determines whether a path is a valid path of the specified type, relative or absolute.

Parameters

 Name  Type    Description

 path   Path   Path you want to compare to the specified type.

               Type you want to compare to the path's type. ofType can have the following
                   values:
 ofType int32                            • fAbsPath—Compare the path's type to absolute.
                            • fRelPath—Compare the path's type to relative.


Return Value

Bool32, which can contain the following values.


 Value        Description

 TRUE        Path is well formed and type is identical to ofType.

 FALSE       Otherwise.


                                                    © National Instruments 6435

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6435 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6436 ordinal=6436 -->
## Property and Method Reference

Property and Method Reference

     FIsAPathOrNotAPathFIsAPathOrNotAPath (LabVIEW(LabVIEW ManagerManager Function)Function)

     Bool32 FIsAPathOrNotAPath(path);

     Purpose

      Determines whether path is a valid path or the canonical invalid path.

     Parameters

      Name           Type             Description

        path          Path           Path you want to verify.

     Return Value

      Bool32, which can contain the following values.


        Value     Description

       TRUE     Path is well formed and type is absolute, relative, or <Not a Path>.

       FALSE   Path is not valid.

     FIsARefNumFIsARefNum (LabVIEW(LabVIEW ManagerManager Function)Function)

     Bool32 FIsARefNum(refNum);

     Purpose

      Determines whether refNum is a valid file refnum.

     Parameters

      Name         Type                  Description

       refNum       LVRefNum              File refnum you want to verify.


6436   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6436 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6437 ordinal=6437 -->
## Property and Method Reference

Property and Method Reference

Return Value

Bool32, which can contain the following values.


 Value        Description

 TRUE          File refnum has been created and not yet disposed.

 FALSE        File refnum is not valid.

FIsEmptyPathFIsEmptyPath (LabVIEW(LabVIEW ManagerManager Function)Function)

Bool32 FIsEmptyPath(path);

Purpose

Determines whether path is a valid empty path.

Parameters

 Name           Type             Description

 path          Path           Path you want to verify.

Return Value

Bool32, which can contain the following values.


 Value      Description

 TRUE      Path is well formed and empty and type is absolute or relative.

 FALSE    Path is not a valid empty path.

FListDirFListDir (LabVIEW(LabVIEW ManagerManager Function)Function)

MgErr FListDir(path, list, typeH);


                                                    © National Instruments 6437

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6437 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6438 ordinal=6438 -->
## Property and Method Reference

Property and Method Reference

     Purpose

      Determines the contents of a directory.

      The function fills the handle passed in list with a CPStr, where the cnt field specifies
       the number of concatenated Pascal strings that follow in the str[] field. If typeH is
       not NULL, the function fills the handle passed in typeH with the file type information
        for each filename or directory name stored in list.

     Parameters

      Name Type            Description

        path  Path          Path of the directory whose contents you want to determine.

                             Handle in which FListDir stores a series of concatenated Pascal
            list   CPStrHandle  strings, preceded by a 4-byte integer field, cnt, that indicates the number
                                   of items in the buffer.

                             Handle in which FListDir stores a series of FileType records. If
                            typeH is not NULL, FListDir stores one FileType record in typeH for
        typeH FileType                             each Pascal string in list. The nth FileType in typeH denotes the file
                                                                                                          th                               type information about the file or directory named in the n   string in list.


         typedef struct {
                 int32 flags;
                 int32 type;
                 } FileType;

      Only the least significant four bits of flags contain useful information. The remaining
        bits are reserved for use by LabVIEW. You can test these four bits using the following
       four masks:


         #define kIsFile 0x01
         #define kRecognizedType 0x02
         #define kIsLink 0x04
         #define kFIsInvisible 0x08

      The kIsFile bit is set if the item described by the file type record is a file. Otherwise,


6438   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6438 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6439 ordinal=6439 -->
## Property and Method Reference

Property and Method Reference

kIsFile  is clear. The kRecognizedType bit is set if the item described is a file for
which you can determine a 4-character file type. Otherwise, kRecognizedType  is
clear. The kIsLink bit is set if the item described is a Linux link or Mac OS X alias.
Otherwise, kIsLink  is clear. The kFIsInvisible bit is set if the item described
does not appear in a file dialog box. Otherwise, kFIsInvisible  is clear.

The value of type is defined only if the kRecognizedType bit is set in flags. In
this case, type is the 4-character file type of the file described by the file type record.
This 4-character file type is provided by the file system on Mac OS X and is computed
by examining the filename extension on other systems.

Return Value

MgErr, which can contain the following errors. If you receive errors from LabVIEW
Manager functions, most error names correspond to LabVIEW error codes.


 Value                 Corresponding Error Code or Description

 noErr             No error.

 mgArgErr            1

 mFullErr            2

 fIOErr              6

 fNotFound          7

 fNoPerm             8

FLockOrUnlockRangeFLockOrUnlockRange (LabVIEW(LabVIEW ManagerManager Function)Function)

MgErr FLockOrUnlockRange(fd, mode, offset, count, lock);

Purpose

Locks or unlocks a section of a file.


                                                    © National Instruments 6439

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6439 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6440 ordinal=6440 -->
## Property and Method Reference

Property and Method Reference

     Parameters

      Name Type     Description

         fd    File     File descriptor associated with the file.

                           Position in the file relative to which FLockOrUnlockRange determines the
                                   first byte to lock or unlock, using the following values:

                                         • fStart—The first byte to lock or unlock is located offset bytes from the
                                   start of the file. offset must be greater than or equal to 0.
      mode int32                                         • fCurrent—The first byte to lock or unlock is located offset bytes from the
                              current position mark. offset can be positive, 0, or negative.
                                         • fEnd—The first byte to lock or unlock is located offset bytes from the end of
                             the file. offset must be less that or equal to 0.

                      The position of the first byte to lock or unlock. The position is the number of
          offset int32   bytes from the beginning of the file, the current position mark, or the end of the
                                     file, as determined by mode.

                    Number of bytes to lock or unlock starting at the location specified by mode and
        count int32                              offset.

                           Indicates whether FLockOrUnlockRange locks or unlocks a range of bytes. If
         lock  Bool32
                   TRUE the function locks a range. If FALSE the function unlocks a range.

     Return Value

      MgErr, which can contain the following errors. If you receive errors from LabVIEW
      Manager functions, most error names correspond to LabVIEW error codes.


        Value            Corresponding Error Code or Description

       noErr        No error.

       fIOErr         6

     FMakePathFMakePath (LabVIEW(LabVIEW ManagerManager Function)Function)

     Path FMakePath(path, type, [volume, directory, directory,
     ..., name,] NULL);


6440   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6440 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6441 ordinal=6441 -->
## Property and Method Reference

Property and Method Reference

The brackets indicate that the volume, directory, and name parameters are optional.

Purpose

Creates a new path. If path is NULL, this function allocates and returns a new path.
Otherwise, path is set to the new path, and this function returns path. If an error
occurs or path is not specified correctly, the function returns NULL.

When you finish using a path, dispose of it using FDestroyPath.

Parameters

 Name    Type    Description

 path    Path   Parameter in which FMakePath returns the new path if path is not NULL.

                 Type of path you want to create. If fAbsPath, the new path is absolute. If
 type    int32
               fRelPath, the new path is relative.

                    (Optional) Pascal string containing a legal volume name. An empty string
 volume  PStr   indicates to go up a level in the path hierarchy. Use this parameter only for
                   absolute paths on Mac OS X or Windows.

                    (Optional) Pascal string containing a legal directory name. An empty string
 directory PStr                     indicates to go up a level in the path hierarchy.

                    (Optional) File or directory name. An empty string indicates to go up a level in
 name    PStr                   the path hierarchy.

 NULL    PStr   Marker indicating the end of the path.

Return Value

The resulting path. If you specified path, the return value is the same as path. If an
error occurs, this function returns NULL.

FMCloseFMClose (LabVIEW(LabVIEW ManagerManager Function)Function)

MgErr FMClose(fd);


                                                    © National Instruments 6441

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6441 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6442 ordinal=6442 -->
## Property and Method Reference

Property and Method Reference

     Purpose

       Closes the file associated with the file descriptor fd.

     Parameters

      Name    Type     Description

         fd      File     File descriptor associated with the file you want to close.

     Return Value

      MgErr, which can contain the following errors. If you receive errors from LabVIEW
      Manager functions, most error names correspond to LabVIEW error codes.


        Value               Corresponding Error Code or Description

       noErr           No error.

       mgArgErr          1

       fIOErr            6

    FMOpenFMOpen (LabVIEW(LabVIEW ManagerManager Function)Function)

     MgErr FMOpen(fdp, path, openMode, denyMode);

     Purpose

      Opens a file with the name and location specified by path for writing and reading, as
       specified by openMode.

      You can use denyMode to control concurrent access to the file from within LabVIEW.

           If the function opens the file, the resulting file descriptor is stored in the address
       referred to by fdp. If an error occurs, the function stores 0 in the address referred to by
      fdp and returns an error.


6442   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6442 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6443 ordinal=6443 -->
## Property and Method Reference

Property and Method Reference

      Note Before you call this function, ensure that you understand how to use
        pointers as parameters.

Parameters

 Name     Type    Description

         File   Address at which FMOpen stores the file descriptor for the new file. If FMOpen fdp
         *          fails, it stores 0 in the address fdp. This parameter is a pointer.

 path     Path   Path of the file you want to open.

                    Access mode to use in opening the file. The following values are defined in the
                             file extcode.h.

                                 • openReadOnly—Open for reading.
                                 • openWriteOnly—Open for writing;Open for writing; file is not
                         truncated (data is not removed). On Mac OS X, this mode provides true
                          write-only access to files. On Windows or Linux, LabVIEW I/O functions openMode int32
                         are built in the C standard I/O library, with which you have write-only
                         access to a file only if you are truncating the file or making the access
                        append-only. Therefore, this mode actually allows both read and write
                         access to files on Windows or Linux.
                                 • openReadWrite—Open for both reading and writing.
                                 • openWriteOnlyTruncate—Open for writing; truncates the file.

                Mode that determines what level of concurrent access to the file is allowed.
                  The following values are defined in the file extcode.h.

                                 • denyReadWrite—Prevents others from reading from and writing to the
                                   file while it is open.
 denyMode int32
                                 • denyWriteOnly—Prevents others from writing to the file only while it
                                  is open.
                                 • denyNeither—Allows others to read from and write to the file while it
                                  is open.


Return Value

MgErr, which can contain the following errors. If you receive errors from LabVIEW
Manager functions, most error names correspond to LabVIEW error codes.


                                                    © National Instruments 6443

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6443 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6444 ordinal=6444 -->
## Property and Method Reference

Property and Method Reference


        Value          Corresponding Error Code or Description

       noErr        No error.

       mgArgErr     1

       fIsOpen         5. This error is returned only on Mac OS X. Windows returns fIOErr.

       fIOErr        6

       fNotFound    7

       fTMFOpen     11

     FMoveFMove (LabVIEW(LabVIEW ManagerManager Function)Function)

     MgErr FMove(oldPath, newPath);

     Purpose

      Moves a file or renames it if the new path indicates the file is to remain in the same
        directory.

     Parameters

      Name    Type  Description

        oldPath  Path Path of the file or directory you want to move.

                           Path, including the name of the file or directory, where you want to move the file
       newPath Path                          or directory.

     Return Value

      MgErr, which can contain the following errors. If you receive errors from LabVIEW
      Manager functions, most error names correspond to LabVIEW error codes.


        Value                 Corresponding Error Code or Description

       noErr             No error.

       mgArgErr            1


6444   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6444 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6445 ordinal=6445 -->
## Property and Method Reference

Property and Method Reference


 Value                 Corresponding Error Code or Description

 mFullErr            2

 fIsOpen             5

 fIOErr              6

 fNotFound          7

 fNoPerm             8

 fDiskFull          9

 fDupPath            10

 fTMFOpen            11

FMReadFMRead (LabVIEW(LabVIEW ManagerManager Function)Function)

MgErr FMRead(fd, inCount, outCountp, buffer);

Purpose

Reads inCount bytes from the file specified by the file descriptor fd. The function starts
from the current position mark and reads the data into memory, starting at the
address specified by buffer. Use the FMSeek function to set the current position mark
and the FMTell function to return the position of the current position mark.

The function stores the actual number of bytes read in *outCountp. The number of
bytes can be less than inCount if the function encounters end-of-file before reading
inCount bytes. The number of bytes is zero if any other error occurs.

Parameters

 Name     Type      Description

 fd       File       File descriptor associated with the file from which you want to read.

 inCount   int32   Number of bytes you want to read.

                      Address at which FMRead stores the number of bytes read. FMRead does
 outCountp int32 *
                      not store any value if NULL is passed. This parameter is a pointer.

 buffer     UPtr     Address where FMRead stores the data.

                                                    © National Instruments 6445

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6445 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6446 ordinal=6446 -->
## Property and Method Reference

Property and Method Reference

     Return Value

      MgErr, which can contain the following errors. If you receive errors from LabVIEW
      Manager functions, most error names correspond to LabVIEW error codes.


        Value               Corresponding Error Code or Description

       noErr           No error.

       mgArgErr          1 or inCount < 0.

       fEOF               4

       fIOErr            6

     FMSeekFMSeek (LabVIEW(LabVIEW ManagerManager Function)Function)

     MgErr FMSeek(fd, ofst, mode);

     Purpose

       Sets the current position mark for a file to the specified point, relative to the beginning
       of the file, the current position in the file, or the end of the file. If the point you specify
         is past the end of the file, the position mark is set to the end of the file. If the point you
       specify is before the beginning of the file, the position mark is set to the beginning of
       the file. If an error occurs, the current position mark does not move.

     Parameters

      Name Type    Description

         fd    File   File descriptor associated with the file.

                 New position of the current position mark. The position is the number of bytes
          ofst   int32 from the beginning of the file, the current position mark, or the end of the file, as
                      determined by mode.

                         Position in the file relative to which FMSeek sets the current position mark for a
                                   file, using the following values:
      mode int32
                                       • fStart—Current position mark moves to ofst bytes relative to the start of


6446   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6446 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6447 ordinal=6447 -->
## Property and Method Reference

Property and Method Reference


 Name Type    Description

                    the file. ofst must be greater than or equal to 0.
                           • fCurrent—Current position mark moves ofst bytes from the current
                     position mark. ofst can be positive, 0, or negative.
                           • fEnd—Current position mark moves to ofst bytes from the end of the file. ofst
                 must be less than or equal to 0.


Return Value

MgErr, which can contain the following errors. If you receive errors from LabVIEW
Manager functions, most error names correspond to LabVIEW error codes.


 Value               Corresponding Error Code or Description

 noErr           No error.

 mgArgErr          1

 fEOF               4

 fIOErr            6

FMTellFMTell (LabVIEW(LabVIEW ManagerManager Function)Function)

MgErr FMTell(fd, ofstp);

Purpose

Returns the position of the current position mark in the file.

Parameters

 Name Type      Description

 fd    File       File descriptor associated with the file.

                  Address at which FMTell stores the position of the current position mark, in
 ofstp  int32 * terms of bytes relative to the beginning of the file. If an error occurs, ofstp is
                   undefined. This parameter is a pointer.

                                                    © National Instruments 6447

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6447 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6448 ordinal=6448 -->
## Property and Method Reference

Property and Method Reference

     Return Value

      MgErr, which can contain the following errors. If you receive errors from LabVIEW
      Manager functions, most error names correspond to LabVIEW error codes.


        Value               Corresponding Error Code or Description

       noErr           No error.

       mgArgErr          1

       fIOErr            6

     FMWriteFMWrite (LabVIEW(LabVIEW ManagerManager Function)Function)

     MgErr FMWrite(fd, inCount, outCountp, buffer);

     Purpose

       Writes inCount bytes from memory, starting at the address specified by buffer, to the
          file specified by the file descriptor fd, starting from the current position mark. Use the
      FMSeek function to set the current position mark and the FMTell function to return the
       position of the current position mark.

      The function stores the actual number of bytes written in *outCountp. The number of
       bytes stored can be less than inCount if an fDiskFull error occurs before the
       function writes inCount bytes. The number of bytes stored is zero if any other error
       occurs.

     Parameters

      Name     Type      Description

         fd       File       File descriptor associated with the file from which you want to write.

        inCount   int32   Number of bytes you want to write.

                              Address at which FMWrite stores the number of bytes written. FMWrite
        outCountp int32 *
                            does not store any value if NULL is passed. This parameter is a pointer.

         buffer     UPtr     Address of the data you want to write.


6448   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6448 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6449 ordinal=6449 -->
## Property and Method Reference

Property and Method Reference

Return Value

MgErr, which can contain the following errors. If you receive errors from LabVIEW
Manager functions, most error names correspond to LabVIEW error codes.


 Value                 Corresponding Error Code or Description

 noErr             No error.

 mgArgErr            1 or inCount < 0.

 fIOErr              6

 fNoPerm             8

 fDiskFull          9

FNameFName (LabVIEW(LabVIEW ManagerManager Function)Function)

MgErr FName(path, name);

Purpose

Copies the last component name of a specified path into a string handle and resizes
the handle as necessary.

Parameters

 Name Type             Description

 path  Path            Path whose last component name you want to determine.

                       Handle in which FName returns the last component name as a Pascal name StringHandle
                              string.

Return Value

MgErr, which can contain the following errors. If you receive errors from LabVIEW
Manager functions, most error names correspond to LabVIEW error codes.


                                                    © National Instruments 6449

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6449 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6450 ordinal=6450 -->
## Property and Method Reference

Property and Method Reference


        Value               Corresponding Error Code or Description

       noErr           No error.

       mgArgErr          1

       mFullErr          2

     FNamePtrFNamePtr (LabVIEW(LabVIEW ManagerManager Function)Function)

     MgErr FNamePtr(path, name);

     Purpose

      Copies the last component name of a path to the address specified by name. This
       routine does not allocate space for the returned data. Therefore, name must specify
       allocated memory of sufficient size to hold the component name.

     Parameters

      Name Type  Description

        path  Path Path whose last component name you want to determine.

                      Address at which FNamePtr stores the last component name as a Pascal string.
      name PStr  This address must specify allocated memory of sufficient size to hold the name. This
                     parameter is a pointer.

     Return Value

      MgErr, which can contain the following errors. If you receive errors from LabVIEW
      Manager functions, most error names correspond to LabVIEW error codes.


        Value               Corresponding Error Code or Description

       noErr           No error.

       mgArgErr          1

       mFullErr          2


6450   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6450 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6451 ordinal=6451 -->
## Property and Method Reference

Property and Method Reference

FNewDirFNewDir (LabVIEW(LabVIEW ManagerManager Function)Function)

MgErr FNewDir(path, permissions);

Purpose

Creates a new directory with the specified permissions. If an error occurs, the function
does not create the directory.

Parameters

 Name             Type        Description

 path            Path       Path of the directory you want to create.

 permissions       int32      Permissions for the new directory.

Return Value

MgErr, which can contain the following errors. If you receive errors from LabVIEW
Manager functions, most error names correspond to LabVIEW error codes.


 Value               Corresponding Error Code or Description

 noErr           No error.

 mgArgErr          1

 fIOErr            6

 fNoPerm           8

 fDupPath          10

FNewRefNumFNewRefNum (LabVIEW(LabVIEW ManagerManager Function)Function)

MgErr FNewRefNum(path, fd, refNumPtr);

Purpose

Creates a new file refnum for an open file with the name and location specified by path

                                                    © National Instruments 6451

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6451 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6452 ordinal=6452 -->
## Property and Method Reference

Property and Method Reference

      and the file descriptor fd.

           If the file refnum is created, the resulting file refnum is stored in the address referred to
      by refNumPtr. If an error occurs, NULL is stored in the address referred to by
      refNumPtr and the error is returned.

     Parameters

      Name     Type          Description

        path     Path         Path of the open file for which you want to create a file refnum.

                                           File descriptor of the open file for which you want to create a file
         fd       File                                  refnum.

                                 Address at which FNewRefNum stores the new file refnum. This        refNumPtr LVRefNum *
                                 parameter is a pointer.

     Return Value

      MgErr, which can contain the following errors. If you receive errors from LabVIEW
      Manager functions, most error names correspond to LabVIEW error codes.


        Value               Corresponding Error Code or Description

       noErr           No error.

       mgArgErr          1

       mFullErr          2

     FNotAPathFNotAPath (LabVIEW(LabVIEW ManagerManager Function)Function)

     Path FNotAPath(p);

     Purpose

       Creates a path that is the canonical invalid path.


6452   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6452 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6453 ordinal=6453 -->
## Property and Method Reference

Property and Method Reference

Parameters

 Name Type  Description

              Path allocated by FNotAPath. If NULL, FNotAPath allocates a new canonical
 p    Path  invalid path and returns the value. If p is a path, FNotAPath sets the existing path
               to the canonical invalid path and returns the new p.

Return Value

The resulting path. If p is not NULL, the return value is the same canonical invalid path
as p. If an error occurs, this function returns NULL.

FPathCmpFPathCmp (LabVIEW(LabVIEW ManagerManager Function)Function)

int32 FPathCmp(lsp1, lsp2);

Purpose

Compares two paths.

Parameters

 Name       Type         Description

 lsp1       Path          First path you want to compare.

 lsp2       Path       Second path you want to compare.

Return Value

int32, which can contain the following values.


 Value  Description

 –1     Paths are of different types. For example, one is absolute and the other is relative.

 0      Paths are identical.

 n+1   Paths have the same first n components but are not identical.


                                                    © National Instruments 6453

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6453 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6454 ordinal=6454 -->
## Property and Method Reference

Property and Method Reference

     FPathCpyFPathCpy (LabVIEW(LabVIEW ManagerManager Function)Function)

     MgErr FPathCpy(dst, src);

     Purpose

       Duplicates the path specified by src and stores the resulting path in the existing path,
        dst.

     Parameters

      Name Type  Description

                      Path where FPathCpy places the resulting duplicate path. This path must already         dst   Path
                    have been created.

         src   Path Path you want to duplicate.

     Return Value

      MgErr, which can contain the following errors. If you receive errors from LabVIEW
      Manager functions, most error names correspond to LabVIEW error codes.


        Value               Corresponding Error Code or Description

       noErr           No error.

       mgArgErr          1

     FPathToArrFPathToArr (LabVIEW(LabVIEW ManagerManager Function)Function)

     MgErr FPathToArr(path, relativePtr, arr);

     Purpose

       Converts a path to a one-dimensional LabVIEW array of strings and determines
      whether the path is relative. Each component name of the path is converted in order
       into a string in the resulting array.


6454   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6454 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6455 ordinal=6455 -->
## Property and Method Reference

Property and Method Reference

If no error occurs, arr is set to an array of strings containing the component names of
path. If an error occurs, arr is set to an empty array.

Parameters

 Name     Type        Description

 path     Path       Path you want to convert to an array of strings.

                       Address at which to store a Boolean value indicating whether the
 relativePtr Bool32 *                           specified path is relative. This parameter is a pointer.

                  DS handle where FPathToArr stores the resulting array of strings. This arr       UHandle
                       handle must already have been allocated.

Return Value

MgErr, which can contain the following errors. If you receive errors from LabVIEW
Manager functions, most error names correspond to LabVIEW error codes.


 Value               Corresponding Error Code or Description

 noErr           No error.

 mgArgErr          1 or unallocated array.

 mFullErr          2

FPathToAZStringFPathToAZString (LabVIEW(LabVIEW ManagerManager Function)Function)

MgErr FPathToAZString(p, txt);

Purpose

Converts a path to an LStr and stores the string as an application zone handle. The
LStr contains the platform-specific syntax for the path.


                                                    © National Instruments 6455

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6455 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6456 ordinal=6456 -->
## Property and Method Reference

Property and Method Reference

     Parameters

      Name Type             Description

       p    Path            Path you want to convert to a string.

                                Address at which FPathToAZString stores the resulting string. If
                                 nonzero, the function assumes it is a valid handle, resizes the handle,          txt   LstrHandle *
                                                   fills in its value, and stores the handle at the address referred to by txt.
                                  This parameter is a pointer.

     Return Value

      MgErr, which can contain the following errors. If you receive errors from LabVIEW
      Manager functions, most error names correspond to LabVIEW error codes.


        Value               Corresponding Error Code or Description

       noErr           No error.

       mgArgErr          1

       mFullErr          2

       fIOErr            6

     FPathToDSStringFPathToDSString (LabVIEW(LabVIEW ManagerManager Function)Function)

     MgErr FPathToDSString(p, txt);

     Purpose

       Converts a path to an LStr and stores the string as a data space zone handle. The
     LStr contains the platform-specific syntax for the path.

     Parameters

      Name Type             Description

       p    Path            Path you want to convert to a string.


6456   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6456 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6457 ordinal=6457 -->
## Property and Method Reference

Property and Method Reference


 Name Type             Description

                        Address at which FPathToDSString stores the resulting string. If
                         nonzero, the function assumes it is a valid handle, resizes the handle, txt   LstrHandle *
                                       fills in its value, and stores the handle at the address referred to by txt.
                          This parameter is a pointer.

Return Value

MgErr, which can contain the following errors. If you receive errors from LabVIEW
Manager functions, most error names correspond to LabVIEW error codes.


 Value               Corresponding Error Code or Description

 noErr           No error.

 mgArgErr          1

 mFullErr          2

 fIOErr            6

FPathToPathFPathToPath (LabVIEW(LabVIEW ManagerManager Function)Function)

MgErr FPathToPath(p);

Purpose

Duplicates a path and returns the new path in the same variable.

Parameters

 Name Type     Description

                 Address of the path you want to duplicate. Variable to which FPathToPath p    Path *
                  returns the resulting path. This parameter is a pointer.

Return Value

MgErr, which can contain the following errors. If you receive errors from LabVIEW

                                                    © National Instruments 6457

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6457 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6458 ordinal=6458 -->
## Property and Method Reference

Property and Method Reference

      Manager functions, most error names correspond to LabVIEW error codes.


        Value               Corresponding Error Code or Description

       noErr           No error.

       mgArgErr          1

     FRefNumToFDFRefNumToFD (LabVIEW(LabVIEW ManagerManager Function)Function)

     MgErr FRefNumToFD(refNum, fdp);

     Purpose

       Gets the file descriptor associated with the specified file refnum.

           If no error occurs, the resulting file descriptor is stored in the address referred to by
       fdp. If an error occurs, NULL is stored in the address referred to by fdp, and the error is
       returned.

     Parameters

      Name   Type        Description

       refNum LVRefNum The file refnum whose associated file descriptor you want to get.

                            Address at which FRefNumToFD stores the file descriptor associated with        fdp    File *
                             the specified file refnum. This parameter is a pointer.

     Return Value

      MgErr, which can contain the following errors. If you receive errors from LabVIEW
      Manager functions, most error names correspond to LabVIEW error codes.


        Value               Corresponding Error Code or Description

       noErr           No error.

       mgArgErr          1


6458   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6458 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6459 ordinal=6459 -->
## Property and Method Reference

Property and Method Reference

FRefNumToPathFRefNumToPath (LabVIEW(LabVIEW ManagerManager Function)Function)

MgErr FRefNumToPath(refNum, path);

Purpose

Gets the path associated with the specified file refnum and stores the resulting path in
the existing path.

If no error occurs, path is set to the path associated with the specified file refnum. If an
error occurs, path is set to the canonical invalid path.

Parameters

 Name   Type        Description

 refNum LVRefNum The file refnum whose associated path you want to get.

                     Path where FRefNumToPath stores the path associated with the specified path   Path
                              file refnum. This path must already have been created.

Return Value

MgErr, which can contain the following errors. If you receive errors from LabVIEW
Manager functions, most error names correspond to LabVIEW error codes.


 Value               Corresponding Error Code or Description

 noErr           No error.

 mgArgErr          1

 mFullErr          2

FRelPathFRelPath (LabVIEW(LabVIEW ManagerManager Function)Function)

MgErr FRelPath(startPath, endPath, relPath);


                                                    © National Instruments 6459

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6459 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6460 ordinal=6460 -->
## Property and Method Reference

Property and Method Reference

     Purpose

      Computes a relative path between two absolute paths. You can pass the same path
       variable for the new path that you use for startPath or relPath. Therefore, you can call
        this function in the following three ways:

            • FRelPath(startPath, endPath, relPath);/* the relative
        path is returned in a third path variable */
            • FRelPath(startPath, endPath, startPath); /* the new path
        writes over the old startPath */
            • FRelPath(startPath, endPath, endPath); /* the new path
        writes over the old endPath */

     Parameters

      Name     Type   Description

         startPath  Path  Absolute path from which you want the relative path to be computed.

        endPath   Path  Absolute path to which you want the relative path to be computed.

         relPath    Path  Path returned by fAddPath.

     Return Value

      MgErr, which can contain the following errors. If you receive errors from LabVIEW
      Manager functions, most error names correspond to LabVIEW error codes.


        Value               Corresponding Error Code or Description

       noErr           No error.

       mgArgErr          1

       mFullErr          2

    FRemoveFRemove (LabVIEW(LabVIEW ManagerManager Function)Function)

     MgErr FRemove(path);


6460   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6460 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6461 ordinal=6461 -->
## Property and Method Reference

Property and Method Reference

Purpose

Deletes a file or a directory. If an error occurs, this function does not remove the file or
directory.

Parameters

 Name     Type      Description

 path     Path     Path of the file or directory you want to delete.

Return Value

MgErr, which can contain the following errors. If you receive errors from LabVIEW
Manager functions, most error names correspond to LabVIEW error codes.


 Value                 Corresponding Error Code or Description

 noErr             No error.

 mgArgErr            1

 fIsOpen             5 or directory is not empty.

 fIOErr              6

 fNotFound          7

 fNoPerm             8

FSetAccessRightsFSetAccessRights (LabVIEW(LabVIEW ManagerManager Function)Function)

MgErr FSetAccessRights(path, owner, group, permPtr);

Purpose

Sets access rights information for the specified file or directory. If an error occurs, no
information changes.


                                                    © National Instruments 6461

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6461 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6462 ordinal=6462 -->
## Property and Method Reference

Property and Method Reference

     Parameters

      Name   Type      Description

                            Path of the file or directory for which you want to set access rights
        path    Path                              information.

                     New owner that FSetAccessRights sets for the file or directory if owner
       owner   PStr
                                       is not NULL.

                     New group that FSetAccessRights sets for the file or directory if group is
        group   PStr
                            not NULL.

                            Address of new permissions that FSetAccessRights sets for the file or
        permPtr int32 *
                               directory if permPtr is not NULL.

     Return Value

      MgErr, which can contain the following errors. If you receive errors from LabVIEW
      Manager functions, most error names correspond to LabVIEW error codes.


        Value                 Corresponding Error Code or Description

       noErr             No error.

       mgArgErr            1

       fIOErr              6

       fNotFound          7

     FSetEOFFSetEOF (LabVIEW(LabVIEW ManagerManager Function)Function)

     MgErr FSetEOF(fd, size);

     Purpose

       Sets the size of the specified file. If an error occurs, the file size does not change.


6462   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6462 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6463 ordinal=6463 -->
## Property and Method Reference

Property and Method Reference

Parameters

 Name      Type              Description

 fd        File                File descriptor associated with the file.

 size      int32 *       New file size in bytes.

Return Value

MgErr, which can contain the following errors. If you receive errors from LabVIEW
Manager functions, most error names correspond to LabVIEW error codes.


 Value                 Corresponding Error Code or Description

 noErr             No error.

 mgArgErr            1 or size < 0.

 fIOErr              6

 fNoPerm             8

 fDiskFull          9

FSetInfoFSetInfo (LabVIEW(LabVIEW ManagerManager Function)Function)

MgErr FSetInfo(path, infop);

Purpose

Sets information for the specified file or directory. If an error occurs, no information
changes.

Parameters

 Name  Type         Description

 path   Path        Path of the file or directory for which you want to set information.

 infop  FInfoPtr   Address of informationFSetInfo sets for the file or directory.


                                                    © National Instruments 6463

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6463 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6464 ordinal=6464 -->
## Property and Method Reference

Property and Method Reference

     FInfoPtr is a data structure that defines the attributes of a file or directory. The
       following code lists the file/directory information record, FInfoPtr.


         typedef struct {
                 int32        type;        /* system specific file type-- 0 for directories
         */
                 int32        creator;        /* system specific file creator-- 0 for
         folders (on Mac only)*/
                 int32        permissions;        /* system specific file access rights */
                 int32        size;        /* file size in bytes (data fork on Mac) or
         entries in directory*/
                 int32        rfSize;        /* resource fork size (on Mac only) */
                 uint32        cdate;        /* creation date: seconds since system
         reference time */
                 uint32        mdate;        /* last modification date: seconds since system
         ref time */
                 Bool32        folder;        /* indicates whether path refers to a folder
         */
                 Bool32        isInvisible;        /* indicates whether file is visible in
         File Dialog (on Mac only)*/
                 Point        location;        /* system specific desktop geographical
         location (on Mac only)*/
                 Str255        owner;        /* owner (in pascal string form) of file or
         folder */
                 Str255        group;        /* group (in pascal string form) of file or
         folder */
                 }        FInfoRec, *FInfoPtr;

     Return Value

      MgErr, which can contain the following errors. If you receive errors from LabVIEW
      Manager functions, most error names correspond to LabVIEW error codes.


        Value                 Corresponding Error Code or Description

       noErr             No error.

       mgArgErr            1

       fIOErr              6

       fNotFound          7


6464   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6464 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6465 ordinal=6465 -->
## Property and Method Reference

Property and Method Reference

FSetPathTypeFSetPathType (LabVIEW(LabVIEW ManagerManager Function)Function)

MgErr FSetPathType(path, type);

Purpose

Changes the type of a path, which must be a valid path, to the specified type, relative
or absolute.

Parameters

 Name  Type     Description

 path   Path    Path whose type you want to change.

             New type you want the path to have. type can have the following values:

 type   int32       • fAbsPath—The path is absolute.
                             • fRelPath—The path is relative.


Return Value

MgErr, which can contain the following errors. If you receive errors from LabVIEW
Manager functions, most error names correspond to LabVIEW error codes.


 Value               Corresponding Error Code or Description

 noErr           No error.

 mgArgErr          1 or invalid type.

FStrFitsPatFStrFitsPat (LabVIEW(LabVIEW ManagerManager Function)Function)

Bool32 FStrFitsPat(pat, str, pLen, sLen);

Purpose

Determines whether a filename, str, matches a pattern, pat.


                                                    © National Instruments 6465

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6465 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6466 ordinal=6466 -->
## Property and Method Reference

Property and Method Reference

     Parameters

      Name Type      Description

                            Pattern (string) to which filename is to be compared. The following characters
                        have special meanings in the pattern.

                    \ is literal, not treated as having a special meaning. A single backslash at the
                       end of pat is the same as two backslashes.        pat   uChar *
                    ? matches any one character.

                    * matches zero or more characters.

          str   uChar * Filename (string) to compare to pattern.

       pLen  int32   Number of characters in pat.

        sLen  int32   Number of characters in str.

     Return Value

      Bool32, which can contain the following values.


        Value            Description

       TRUE           Filename fits the pattern.

       FALSE          Filename does not match the pattern.

      FStringToPathFStringToPath (LabVIEW(LabVIEW ManagerManager Function)Function)

     MgErr FStringToPath(text, p);

     Purpose

       Creates a path from an LStr. The LStr contains the platform-specific syntax for a
       path.


6466   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6466 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6467 ordinal=6467 -->
## Property and Method Reference

Property and Method Reference

Parameters

 Name Type          Description

 text   LstrHandle  String that contains the path in platform-specific syntax.

                      Address at which FStringToPath stores the resulting path. If nonzero,
                      the function assumes it is a valid path, resizes the path, and fills in its value.
 p    Path *
                                     If NULL, the function creates a new path, fills in its value, and stores the
                     path at the address referred to by p. This parameter is a pointer.

Return Value

MgErr, which can contain the following errors. If you receive errors from LabVIEW
Manager functions, most error names correspond to LabVIEW error codes.


 Value               Corresponding Error Code or Description

 noErr           No error.

 mFullErr          2

FTextToPathFTextToPath (LabVIEW(LabVIEW ManagerManager Function)Function)

MgErr FTextToPath(text, tlen, *p);

Purpose

Creates a path from a string at the address text that represents a path in the platform-
specific syntax for a path.

Parameters

 Name Type     Description

 text   UPtr     String that contains the path in platform-specific syntax.

 tlen   int32  Number of characters in text.

                 Address at which FTextToPath stores the resulting path. If nonzero, the
 p    Path *
                  function assumes it is a valid path, resizes the path, and fills in its value. If NULL,


                                                    © National Instruments 6467

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6467 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6468 ordinal=6468 -->
## Property and Method Reference

Property and Method Reference


      Name Type     Description

                         the function creates a new path, fills in its value, and stores the path at the
                        address referred to by p. This parameter is a pointer.

     Return Value

      MgErr, which can contain the following errors. If you receive errors from LabVIEW
      Manager functions, most error names correspond to LabVIEW error codes.


        Value               Corresponding Error Code or Description

       noErr           No error.

       mFullErr          2

     FUnFlattenPathFUnFlattenPath (LabVIEW(LabVIEW ManagerManager Function)Function)

     int32 FUnFlattenPath(fp, pPtr);

     Purpose

       Converts a flattened path, created using FFlattenPath, into a path.

     Parameters

      Name Type     Description

         fp    UPtr    Pointer to the flattened path you want to convert to a path.

                        Address at which FUnFlattenPath stores the resulting path. This parameter is        pPtr  Path *
                       a pointer.

     Return Value

     Number of bytes the function interpreted as a path.


6468   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6468 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6469 ordinal=6469 -->
## Property and Method Reference

Property and Method Reference

FVolNameFVolName (LabVIEW(LabVIEW ManagerManager Function)Function)

MgErr FVolName(path, vol);

Purpose

Creates a path for the volume of an absolute path by removing all but the first
component name from path. You can pass the same path variable for the volume path
that you use for path. Therefore, you can call this function in the following two ways:

  • err = FVolName(path, vol); /* the parent path is returned
   in a second path variable */
  • err = FVolName(path, path);/* the parent path writes over
   the existing path */

Parameters

 Name    Type     Description

 path    Path    Path whose volume path you want to determine.

 vol     Path    Parameter in which FVolName stores the volume path.

Return Value

MgErr, which can contain the following errors. If you receive errors from LabVIEW
Manager functions, most error names correspond to LabVIEW error codes.


 Value               Corresponding Error Code or Description

 noErr           No error.

 mgArgErr          1

PermissionsPermissions forfor FilesFiles andand DirectoriesDirectories

The file manager uses the int32 data type to describe permissions for files and
directories. The manager uses only the least significant nine bits of the int32.


                                                    © National Instruments 6469

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6469 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6470 ordinal=6470 -->
## Property and Method Reference

Property and Method Reference

       (Linux) The nine bits of permissions correspond exactly to nine Linux permission bits
       governing read, write, and execute permissions for user, group, and others. The
       following illustration shows permission bits on Linux.


      (Windows) The file manager ignores permissions for directories. For files, the manager
       uses only bit 7 (the Linux user write permission bit). If this bit is clear, the file is read-
        only. Otherwise, you can write to the file.

      (OS X) The file manager uses all nine bits for directories (folders). The manager uses
       the bits that control read, write, and execute permissions, respectively, on Linux to
       control See Files, Make Changes, and See Folders access rights, respectively, on Mac
     OS X.

    MemoryMemory ManagerManager FunctionsFunctions

      The memory manager functions can dynamically allocate, manipulate, and release
      memory.

      You must include the appropriate header and library files to use these functions in a
      shared library.

      You can perform the following operations by using the functions listed.

            • Handles and pointers, verifying
     ◦ DSCheckHandle
     ◦ DSCheckPtr
            • Handles, allocating and releasing
     ◦ DSCopyHandle
     ◦ DSDisposeHandle
     ◦ DSGetHandleSize
     ◦ DSNewAlignedHandle

6470   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6470 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6471 ordinal=6471 -->
## Property and Method Reference

Property and Method Reference

  ◦ DSNewAlignedHClr
  ◦ DSNewHandle
  ◦ DSNewHClr
  ◦ DSRecoverHandle
  ◦ DSSetAlignedHandleSize
  ◦ DSSetAlignedHSzClr
  ◦ DSSetHandleSize
  ◦ DSSetHSzClr
  ◦ NumericArrayResize
  • Memory utilities
  ◦ ClearMem
  ◦ MoveBlock
  ◦ SwapBlock
  • Memory zone utilities
  ◦ DSHeapCheck
  ◦ DSMaxMem
  ◦ DSMemStats
  • Pointers, allocating and releasing
  ◦ DSDisposePtr
  ◦ DSNewPClr
  ◦ DSNewPtr

ClearMemClearMem (LabVIEW(LabVIEW ManagerManager Function)Function)

void ClearMem(p, size);

Purpose

Sets size bytes starting at the address referenced by p to 0.

Parameters

 Name     Type          Description

 p       UPtr          Pointer to block of memory you want to clear.

 size      size_t     Number of bytes you want to clear.


                                                    © National Instruments 6471

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6471 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6472 ordinal=6472 -->
## Property and Method Reference

Property and Method Reference

     DSCheckHandleDSCheckHandle (LabVIEW(LabVIEW ManagerManager Function)Function)

     MgErr DSCheckHandle(h);

     Purpose

        Verifies that the specified handle is a handle. If it is not a handle, this function returns
     mZoneErr.

     Parameters

      Name        Type                   Description

       h          Uhandle            Handle you want to verify.

     Return Value

      MgErr, which can contain the following errors. If you receive errors from LabVIEW
      Manager functions, most error names correspond to LabVIEW error codes.


        Value               Corresponding Error Code or Description

       noErr           No error.

       mZoneErr          Handle or pointer not in specified zone.

     DSCheckPtrDSCheckPtr (LabVIEW(LabVIEW ManagerManager Function)Function)

     MgErr DSCheckPtr(p);

     Purpose

        Verifies that the specified pointer is allocated with XX NewPtr or XX NewPClr. If it is
       not a pointer, this function returns mZoneErr.


6472   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6472 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6473 ordinal=6473 -->
## Property and Method Reference

Property and Method Reference

Parameters

 Name          Type            Description

 p            UPtr           Pointer you want to verify.

Return Value

MgErr, which can contain the following errors. If you receive errors from LabVIEW
Manager functions, most error names correspond to LabVIEW error codes.


 Value               Corresponding Error Code or Description

 noErr           No error.

 mZoneErr          Handle or pointer not in specified zone.

DSCopyHandleDSCopyHandle (LabVIEW(LabVIEW ManagerManager Function)Function)

MgErr DSCopyHandle(void *ph, const void *hsrc)

Purpose

Copies the data referenced by the handle hsrc into the handle pointed to by ph or a
new handle if ph points to NULL.

Parameters

 Name Type        Description

                     Pointer to the handle to copy the data into. This must point to a valid handle
 ph   UHandle*                    or NULL. If it points to NULL, a new handle is allocated.

 hsrc  UHandle  The handle containing the data to copy.

Return Value

MgErr, which can contain the following errors. If you receive errors from LabVIEW
Manager functions, most error names correspond to LabVIEW error codes.

                                                    © National Instruments 6473

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6473 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6474 ordinal=6474 -->
## Property and Method Reference

Property and Method Reference


        Value               Corresponding Error Code or Description

       noErr           No error.

       mZoneErr          Handle or pointer not in specified zone.

       mFullErr          2

     DSDisposeHandleDSDisposeHandle (LabVIEW(LabVIEW ManagerManager Function)Function)

     MgErr DSDisposeHandle(h);

     Purpose

       Releases the memory referenced by the specified handle.

     Parameters

      Name       Type                 Description

       h         UHandle           Handle you want to dispose of.

     Return Value

      MgErr, which can contain the following errors. If you receive errors from LabVIEW
      Manager functions, most error names correspond to LabVIEW error codes.


        Value               Corresponding Error Code or Description

       noErr           No error.

       mZoneErr          Handle or pointer not in specified zone.

     DSDisposePtrDSDisposePtr (LabVIEW(LabVIEW ManagerManager Function)Function)

     MgErr DSDisposePtr(p);


6474   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6474 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6475 ordinal=6475 -->
## Property and Method Reference

Property and Method Reference

Purpose

Releases the memory referenced by the specified pointer.

Parameters

 Name        Type          Description

 p          UPtr          Pointer you want to dispose of.

Return Value

MgErr, which can contain the following errors. If you receive errors from LabVIEW
Manager functions, most error names correspond to LabVIEW error codes.


 Value               Corresponding Error Code or Description

 noErr           No error.

 mZoneErr          Handle or pointer not in specified zone.

DSGetHandleSizeDSGetHandleSize (LabVIEW(LabVIEW ManagerManager Function)Function)

size_t DSGetHandleSize(h);

Purpose

Returns the size of the block of memory referenced by the specified handle.

Parameters

 Name     Type             Description

 h        UHandle       Handle whose size you want to determine.

Return Value

The size in bytes of the relocatable block referenced by the handle h. If an error occurs,


                                                    © National Instruments 6475

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6475 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6476 ordinal=6476 -->
## Property and Method Reference

Property and Method Reference

        this function returns a negative number.

     DSHeapCheckDSHeapCheck (LabVIEW(LabVIEW ManagerManager Function)Function)

     MgErr DSHeapCheck(Bool32 d);

     Purpose

        Verifies that the heap currently being accessed is not corrupt. This function returns 0
        for an intact heap and a nonzero value for a corrupt heap.

     Parameters

      Name        Type               Description

       d          Bool32           Reserved for use by LabVIEW.

     Return Value

      MgErr, which can contain the following errors. If you receive errors from LabVIEW
      Manager functions, most error names correspond to LabVIEW error codes.


        Value                    Corresponding Error Code or Description

       noErr                 The heap is intact.

       mCorruptErr           74

    DSMaxMemDSMaxMem (LabVIEW(LabVIEW ManagerManager Function)Function)

     size_t DSMaxMem();

     Purpose

       Returns the size of the largest block of contiguous memory available for allocation.


6476   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6476 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6477 ordinal=6477 -->
## Property and Method Reference

Property and Method Reference

Return Value

size_t, the size of the largest block of contiguous memory available for allocation.

DSMemStatsDSMemStats (LabVIEW(LabVIEW ManagerManager Function)Function)

MgErr DSMemStats(MemStatRec *msrp);

Purpose

Returns various statistics about the memory in a zone.

Parameters

 Name Type          Description

                           Statistics about the zone's free memory in a MemStatRec structure. This msrp  MemStatRec
                     parameter is a pointer.

The following code defines the MemStatRec structure:


 typedef struct {
         int32 totFreeSize, maxFreeSize, nFreeBlocks;
         int32 totAllocSize, maxAllocSize;
         int32 nPointers, nUnlockedHdls, nLockedHdls;
         int32 reserved [4];
         }

The free memory in a zone consists of a number of blocks of contiguous memory. In
the MemStatRec structure, totFreeSize is the sum of the sizes of the contiguous
memory blocks. maxFreeSize is the largest of the contiguous memory blocks, as
returned by XXMaxMem. nFreeBlocks is the number of the contiguous memory blocks.

Similarly, the allocated memory in a zone consists of a number of blocks of contiguous
memory. In the MemStatRec structure, totAllocSize is the sum of the sizes of
the contiguous memory blocks. maxAllocSize is the largest of the contiguous
memory blocks.


                                                    © National Instruments 6477

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6477 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6478 ordinal=6478 -->
## Property and Method Reference

Property and Method Reference

      Because there are three different varieties of allocated blocks, the numbers of blocks
       of each type is returned separately. nPointers (int32) is the number of pointers.
     nUnlockedHdls (int32) is the number of unlocked handles. nLockedHdls
      (int32) is the number of locked handles. Add the values of nPointers,
     nUnlockedHdls, and nLockedHdls together to find the total number of allocated
       blocks.

      The four reserved fields are reserved for use by National Instruments.

     Return Value

      MgErr, which can contain the following errors. If you receive errors from LabVIEW
      Manager functions, most error names correspond to LabVIEW error codes.


        Value               Corresponding Error Code or Description

       noErr           No error.

       mZoneErr          Handle or pointer not in specified zone.

       mFullErr          2

     DSNewAlignedHandleDSNewAlignedHandle (LabVIEW(LabVIEW ManagerManager Function)Function)

     UHandle DSNewAlignedHandle (size, alignment,
     alignmentOffset);

     Purpose

       Creates a new handle to a relocatable block of memory of the specified size,
       alignment, and alignmentOffset. If you align the block of memory specifically for the
       data representation you want, you can improve the speed at which LabVIEW accesses
       that data or the speed and efficiency of data transfers to or from hardware.

       This function is most useful when you allocate arrays of LabVIEW data that you plan to
       access with specific operations, such as SSE or AVX vector instructions that perform
       better when you align the data at 16- or 32-byte boundaries, respectively. You also can
      improve the performance of DMA data transfers between LabVIEW-allocated memory
      and hardware, such as data acquisition devices or disk. For example, set the data

6478   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6478 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6479 ordinal=6479 -->
## Property and Method Reference

Property and Method Reference

alignment at 64 bytes for cacheline size, 128 bytes for PCIe max payload size, or 512
bytes for PCIe read request size.

      Note Use DSNewHandle instead of this function if you do not need to
       access arrays of LabVIEW data with specific operations, such as vector
        instructions or DMA data transfers. If you use this function incorrectly, you
       can cause your application to perform poorly or cause LabVIEW to crash.

Parameters

 Name          Type     Description

 size          size_t  Size, in bytes, of the block of memory you want to create.

                        Boundary to which you want to align the block of memory. You must
                              set the value to a power of 2, from 8 to 32,768. If you set the value to a
 alignment     size_t                      number other than a power of 2, LabVIEW raises the value to the next
                       power of 2.

                              Offset from the beginning of the allocation to the part of the allocation
                             that you want to align. You must specify alignmentOffset to align data
                     when the memory block contains header information at the beginning
 alignmentOffset size_t  of the allocation. If you set alignmentOffset to a number other than 0,
                        you create the memory block before the alignment boundary to
                          account for the header information and to align the data with the
                          boundary.

Calculating the Alignment Offset

The correct value of alignmentOffset depends upon the platform for which you
compile the code, the number of dimensions in the array, and the data type of the
array elements.

National Instruments recommends using the Offset macro, located in the extcode.h
header file in the labview/cintools directory, to get the correct alignment offset.
For example, the following code defines an array:


 typedef struct MyArray_t {
         int32 count;
         EltType elt[1];

                                                    © National Instruments 6479

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6479 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6480 ordinal=6480 -->
## Property and Method Reference

Property and Method Reference


                 } MyArray;

      You can use the following expression to get the correct alignment offset for the array
       defined above:

     Offset(MyArray, elt)

      Use the Offset macro to get the correct value for alignmentOffset regardless of the
       data type of the array or the platform you use.

      The following code is an example of how to use the Offset macro with this function for
      a two-dimensional array:


         typedef struct {
                 int32_t rows;
                 int32_t cols;
                 float64 data[1];
                 } Float64Matrix;


         typedef Float64Matrix ** Float64MatrixHandle;
         #define NROWS 256
         #define NCOLS 256


     ...


         alignment = sizeof(float64) * N_FLOAT64S_PER_VECTOR_REGISTER;
         totalNumberOfElements = NROWS * NCOLS;


         size = Offset(Float64Matrix, data) + (totalNumberOfElements * sizeof(float64));
         alignmentOffset = Offset(Float64Matrix, data);
         Float64MatrixHandle matrixHandle = (Float64MatrixHandle)DSNewAlignedHandle(size,
         alignment, alignmentOffset);
         (*matrixHandle)->rows = NROWS;
         (*matrixHandle)->cols = NCOLS;

     Return Value

      A handle of the specified size, alignment, and alignmentOffset. If an error occurs, this
       function returns NULL.


6480   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6480 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6481 ordinal=6481 -->
## Property and Method Reference

Property and Method Reference

DSNewAlignedHClrDSNewAlignedHClr (LabVIEW(LabVIEW ManagerManager Function)Function)

UHandle DSNewAlignedHClr (size, alignment,
alignmentOffset);

Purpose

Creates a new handle to a relocatable block of memory of the specified size,
alignment, and alignmentOffset and initializes the memory to zero. If you align the
block of memory specifically for the data representation you want, you can improve
the speed at which LabVIEW accesses that data or the speed and efficiency of data
transfers to or from hardware.

This function is most useful when you allocate arrays of LabVIEW data that you plan to
access with specific operations, such as SSE or AVX vector instructions that perform
better when you align the data at 16- or 32-byte boundaries, respectively. You also can
improve the performance of DMA data transfers between LabVIEW-allocated memory
and hardware, such as data acquisition devices or disk. For example, set the data
alignment at 64 bytes for cacheline size, 128 bytes for PCIe max payload size, or 512
bytes for PCIe read request size.

      Note Use DSNewHClr instead of this function if you do not need to access
        arrays of LabVIEW data with specific operations, such as vector instructions
        or DMA data transfers. If you use this function incorrectly, you can cause your
        application to perform poorly or cause LabVIEW to crash.

Parameters

 Name          Type     Description

 size          size_t  Size, in bytes, of the block of memory you want to create.

                        Boundary to which you want to align the block of memory. You must
                              set the value to a power of 2, from 8 to 32,768. If you set the value to a
 alignment     size_t                      number other than a power of 2, LabVIEW raises the value to the next
                       power of 2.

                              Offset from the beginning of the allocation to the part of the allocation
 alignmentOffset size_t                             that you want to align. You must specify alignmentOffset to align data


                                                    © National Instruments 6481

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6481 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6482 ordinal=6482 -->
## Property and Method Reference

Property and Method Reference


      Name          Type     Description

                            when the memory block contains header information at the beginning
                                      of the allocation. If you set alignmentOffset to a number other than 0,
                               you create the memory block before the alignment boundary to
                                 account for the header information and to align the data with the
                                 boundary.

      Calculating the Alignment Offset

      The correct value of alignmentOffset depends upon the platform for which you
      compile the code, the number of dimensions in the array, and the data type of the
       array elements.

       National Instruments recommends using the Offset macro, located in the extcode.h
      header file in the labview/cintools directory, to get the correct alignment offset.
       For example, the following code defines an array:


         typedef struct MyArray_t {
                 int32 count;
                 EltType elt[1];
                 } MyArray;

      You can use the following expression to get the correct alignment offset for the array
       defined above:

     Offset(MyArray, elt)

      Use the Offset macro to get the correct value for alignmentOffset regardless of the
       data type of the array or the platform you use.

      The following code is an example of how to use the Offset macro with this function for
      a two-dimensional array:


         typedef struct {
                 int32_t rows;
                 int32_t cols;
                 float64 data[1];
                 } Float64Matrix;


6482   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6482 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6483 ordinal=6483 -->
## Property and Method Reference

Property and Method Reference


 typedef Float64Matrix ** Float64MatrixHandle;
 #define NROWS 256
 #define NCOLS 256


...


 alignment = sizeof(float64) * N_FLOAT64S_PER_VECTOR_REGISTER;
 totalNumberOfElements = NROWS * NCOLS;


 size = Offset(Float64Matrix, data) + (totalNumberOfElements * sizeof(float64));
 alignmentOffset = Offset(Float64Matrix, data);
 Float64MatrixHandle matrixHandle = (Float64MatrixHandle)DSNewAlignedHClr(size,
 alignment, alignmentOffset);
 (*matrixHandle)->rows = NROWS;
 (*matrixHandle)->cols = NCOLS;

Return Value

A handle of the specified size, alignment, and alignmentOffset, where the block of
memory is set to all zeros. If an error occurs, this function returns NULL.

DSNewHandleDSNewHandle (LabVIEW(LabVIEW ManagerManager Function)Function)

UHandle DSNewHandle(size);

Purpose

Creates a new handle to a relocatable block of memory of the specified size. The
routine aligns all handles and pointers in DS to accommodate the largest possible data
representations for the platform in use.

Parameters

 Name    Type          Description

 size     size_t       Size, in bytes, of the handle you want to create.


                                                    © National Instruments 6483

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6483 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6484 ordinal=6484 -->
## Property and Method Reference

Property and Method Reference

     Return Value

      A handle of the specified size. If an error occurs, this function returns NULL.

     DSNewHClrDSNewHClr (LabVIEW(LabVIEW ManagerManager Function)Function)

     UHandle DSNewHClr(size);

     Purpose

       Creates a new handle to a relocatable block of memory of the specified size and
         initializes the memory to zero.

     Parameters

      Name    Type          Description

          size     size_t       Size, in bytes, of the handle you want to create.

     Return Value

      A handle of the specified size, where the block of memory is set to all zeros. If an error
       occurs, this function returns NULL.

     DSNewPClrDSNewPClr (LabVIEW(LabVIEW ManagerManager Function)Function)

     UPtr DSNewPClr(size);

     Purpose

       Creates a new pointer to a non-relocatable block of memory of the specified size and
         initializes the memory to zero.

     Parameters

      Name    Type          Description

          size     size_t       Size, in bytes, of the pointer you want to create.

6484   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6484 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6485 ordinal=6485 -->
## Property and Method Reference

Property and Method Reference

Return Value

A pointer to a block of size bytes filled with zeros. If an error occurs, this function
returns NULL.

DSNewPtrDSNewPtr (LabVIEW(LabVIEW ManagerManager Function)Function)

UPtr DSNewPtr(size);

Purpose

Creates a new pointer to a non-relocatable block of memory of the specified size.

Parameters

 Name    Type          Description

 size     size_t       Size, in bytes, of the pointer you want to create.

Return Value

A pointer to a block of size bytes. If an error occurs, this function returns NULL.

DSRecoverHandleDSRecoverHandle (LabVIEW(LabVIEW ManagerManager Function)Function)

UHandle DSRecoverHandle(p);

Purpose

Given a pointer to a block of memory that was originally declared as a handle, this
function returns a handle to the block of memory.

This function is useful when you have the address of a block of memory that you know
is a handle, and you need to get a true handle to the block of memory.


                                                    © National Instruments 6485

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6485 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6486 ordinal=6486 -->
## Property and Method Reference

Property and Method Reference

     Parameters

      Name      Type       Description

       p        UPtr       Pointer to a relocatable block of memory.

     Return Value

      A handle to the block of memory to which p refers. If an error occurs, this function
       returns NULL.

     DSSetAlignedHandleSizeDSSetAlignedHandleSize (LabVIEW(LabVIEW ManagerManager Function)Function)

     MgErr DSSetAlignedHandleSize (h, size, alignment,
     alignmentOffset)

     Purpose

      Changes the size, alignment, and alignment offset of the block of memory that the
       specified handle references. If you align the block of memory specifically for the data
       representation you want, you can improve the speed at which LabVIEW accesses that
       data or the speed and efficiency of data transfers to or from hardware.

       This function is most useful when you allocate arrays of LabVIEW data that you plan to
       access with specific operations, such as SSE or AVX vector instructions that perform
       better when you align the data at 16- or 32-byte boundaries, respectively. You also can
      improve the performance of DMA data transfers between LabVIEW-allocated memory
      and hardware, such as data acquisition devices or disk. For example, set the data
      alignment at 64 bytes for cacheline size, 128 bytes for PCIe max payload size, or 512
       bytes for PCIe read request size.

      To use this function to resize and realign an array handle, you must calculate how
     many bytes the resized array requires and where to align the block of memory
       referenced by the handle. Many platforms have memory alignment requirements that
     make it difficult to determine the correct size for the resulting array. Learn about how
      LabVIEW stores data in memory to calculate the size and alignment of array elements,
       especially for arbitrary data types such as clusters.


6486   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6486 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6487 ordinal=6487 -->
## Property and Method Reference

Property and Method Reference

      Note Use DSSetHandleSize instead of this function if you do not need to
       access arrays of LabVIEW data with specific operations, such as vector
        instructions or DMA data transfers. If you use this function incorrectly, you
       can cause your application to perform poorly or cause LabVIEW to crash. To
        resize a handle for a numeric array, use the NumericArrayResize
      manager function instead of DSSetAlignedHandleSize. You cannot use
         this function on a locked handle.

Parameters

 Name          Type      Description

 h            UHandle Handle you want to resize.

 size          size_t   Size, in bytes, of the block of memory you want to create.

                         Boundary to which you want to align the block of memory. You must
                               set the value to a power of 2, from 8 to 32,768. If you set the value to a
 alignment     size_t                       number other than a power of 2, LabVIEW raises the value to the next
                        power of 2.

                               Offset from the beginning of the allocation to the part of the
                               allocation that you want to align. You must specify alignmentOffset
                              to align data when the memory block contains header information at
 alignmentOffset size_t   the beginning of the allocation. If you set alignmentOffset to a
                       number other than 0, you create the memory block before the
                           alignment boundary to account for the header information and to
                               align the data with the boundary.

Calculating the Alignment Offset

The correct value of alignmentOffset depends upon the platform for which you
compile the code, the number of dimensions in the array, and the data type of the
array elements.

National Instruments recommends using the Offset macro, located in the extcode.h
header file in the labview/cintools directory, to get the correct alignment offset.
For example, the following code defines an array:


 typedef struct MyArray_t {

                                                    © National Instruments 6487

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6487 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6488 ordinal=6488 -->
## Property and Method Reference

Property and Method Reference


                 int32 count;
                 EltType elt[1];
                 } MyArray;

      You can use the following expression to get the correct alignment offset for the array
       defined above:

     Offset(MyArray, elt)

      Use this macro to get the correct value for alignmentOffset regardless of the data type
       of the array or the platform you use.

      The following code is an example of how to use the Offset macro with this function for
      a two-dimensional array:


         typedef struct {
                 int32_t rows;
                 int32_t cols;
                 float64 data[1];
                 } Float64Matrix;


         typedef Float64Matrix ** Float64MatrixHandle;


         #define NROWS 256
         #define NCOLS 256


     ...


         alignment = sizeof(float64) * N_FLOAT64S_PER_VECTOR_REGISTER;
         totalNumberOfElements = NROWS * NCOLS;


         size = Offset(Float64Matrix, data) + (totalNumberOfElements * sizeof(float64));
         alignmentOffset = Offset(Float64Matrix, data);
         MgErr err = DSSetAlignedHandleSize(matrixHandle, size, alignment, alignmentOffset);
         (*matrixHandle)->rows = NROWS;
         (*matrixHandle)->cols = NCOLS;

     Return Value

      MgErr, which can contain the following errors. Most error names you can receive from

6488   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6488 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6489 ordinal=6489 -->
## Property and Method Reference

Property and Method Reference

LabVIEW Manager functions correspond to LabVIEW error codes.


 Value      Corresponding Error Code or Description

 noErr    No error.

          Memory is full. If you receive this error while developing a large application or storing
 mFullErr  large sets of data in LabVIEW, refer to the KnowledgeBase at ni.com for more
             information.

DSSetAlignedHSzClrDSSetAlignedHSzClr (LabVIEW(LabVIEW ManagerManager Function)Function)

MgErr DSSetAlignedHSzClr (h, size, alignment,
alignmentOffset)

Purpose

Changes the size, alignment, and alignment offset of the block of memory referenced
by the specified handle and sets any new memory to zero. If you align the block of
memory specifically for the data representation you want, you can improve the speed
at which LabVIEW accesses that data or the speed and efficiency of data transfers to or
from hardware.

This function is most useful when you allocate arrays of LabVIEW data that you plan to
access with specific operations, such as SSE or AVX vector instructions that perform
better when you align the data at 16- or 32-byte boundaries, respectively. You also can
improve the performance of DMA data transfers between LabVIEW-allocated memory
and hardware, such as data acquisition devices or disk. For example, set the data
alignment at 64 bytes for cacheline size, 128 bytes for PCIe max payload size, or 512
bytes for PCIe read request size.

      Note Use DSSetHSzClr instead of this function if you do not need to
       access arrays of LabVIEW data with specific operations, such as vector
        instructions or DMA data transfers. If you use this function incorrectly, you
       can cause your application to perform poorly or cause LabVIEW to crash. To
        resize a handle for a numeric array, use the NumericArrayResize
      manager function instead of DSSetAlignedHSzClr. You cannot use this


                                                    © National Instruments 6489

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6489 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6490 ordinal=6490 -->
## Property and Method Reference

Property and Method Reference


               function on a locked handle.

     Parameters

      Name          Type      Description

       h            UHandle Handle you want to resize.

          size          size_t   Size, in bytes, of the block of memory you want to create.

                                Boundary to which you want to align the block of memory. You must
                                        set the value to a power of 2, from 8 to 32,768. If you set the value to a
        alignment     size_t                              number other than a power of 2, LabVIEW raises the value to the next
                               power of 2.

                                        Offset from the beginning of the allocation to the part of the
                                        allocation that you want to align. You must specify alignmentOffset
                                      to align data when the memory block contains header information at
        alignmentOffset size_t   the beginning of the allocation. If you set alignmentOffset to a
                              number other than 0, you create the memory block before the
                                   alignment boundary to account for the header information and to
                                        align the data with the boundary.

      Calculating the Alignment Offset

      The correct value of alignmentOffset depends upon the platform for which you
      compile the code, the number of dimensions in the array, and the data type of the
       array elements.

       National Instruments recommends using the Offset macro, located in the extcode.h
      header file in the labview/cintools directory, to get the correct alignment offset.
       For example, the following code defines an array:


         typedef struct MyArray_t {
                 int32 count;
                 EltType elt[1];
                 } MyArray;

      You can use the following expression to get the correct alignment offset for the array
       defined above:


6490   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6490 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6491 ordinal=6491 -->
## Property and Method Reference

Property and Method Reference

Offset(MyArray, elt)

Use this macro to get the correct value for alignmentOffset regardless of the data type
of the array or the platform you use.

The following code is an example of how to use the Offset macro with this function for
a two-dimensional array:


 typedef struct {
         int32_t rows;
         int32_t cols;
         float64 data[1];
         } Float64Matrix;


 typedef Float64Matrix ** Float64MatrixHandle;


 #define NROWS 256
 #define NCOLS 256


...


 alignment = sizeof(float64) * N_FLOAT64S_PER_VECTOR_REGISTER;
 totalNumberOfElements = NROWS * NCOLS;


 size = Offset(Float64Matrix, data) + (totalNumberOfElements * sizeof(float64));
 alignmentOffset = Offset(Float64Matrix, data);
 MgErr err = DSSetAlignedHSzClr(matrixHandle, size, alignment, alignmentOffset);
 (*matrixHandle)->rows = NROWS;
 (*matrixHandle)->cols = NCOLS;

Return Value

MgErr, which can contain the following errors. Most error names you can receive from
LabVIEW Manager functions correspond to LabVIEW error codes.


 Value      Corresponding Error Code or Description

 noErr    No error.

          Memory is full. If you receive this error while developing a large application or storing
 mFullErr              large sets of data in LabVIEW, refer to the KnowledgeBase at ni.com for more


                                                    © National Instruments 6491

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6491 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6492 ordinal=6492 -->
## Property and Method Reference

Property and Method Reference


        Value      Corresponding Error Code or Description

                      information.

     DSSetHandleSizeDSSetHandleSize (LabVIEW(LabVIEW ManagerManager Function)Function)

     MgErr DSSetHandleSize(h, size);

     Purpose

      Changes the size of the block of memory referenced by the specified handle.

      To use this function to resize an array handle, you must calculate how many bytes the
       resized array requires. Many platforms have memory alignment requirements that
     make it difficult to determine the correct size for the resulting array. Learn about how
      LabVIEW stores data in memory to calculate the size and alignment of array elements,
       especially for arbitrary data types such as clusters.

      To resize a handle for a numeric array, use the NumericArrayResize manager function
       instead of DSSetHandleSize.

     Do not use this function on a locked handle.

     Parameters

      Name       Type                Description

       h         UHandle          Handle you want to resize.

          size       size_t         New size, in bytes, of the handle.

     Return Value

      MgErr, which can contain the following errors. If you receive errors from LabVIEW
      Manager functions, most error names correspond to LabVIEW error codes.


        Value               Corresponding Error Code or Description

       noErr           No error.

6492   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6492 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6493 ordinal=6493 -->
## Property and Method Reference

Property and Method Reference


 Value               Corresponding Error Code or Description

 mZoneErr          Handle or pointer not in specified zone.

 mFullErr          2

DSSetHSzClrDSSetHSzClr (LabVIEW(LabVIEW ManagerManager Function)Function)

MgErr DSSetHSzClr(h, size);

Purpose

Changes the size of the block of memory referenced by the specified handle and sets
any new memory to zero. Do not use this function on a locked handle.

Parameters

 Name       Type                Description

 h         UHandle          Handle you want to resize.

 size       size_t         New size, in bytes, of the handle.

Return Value

MgErr, which can contain the following errors. If you receive errors from LabVIEW
Manager functions, most error names correspond to LabVIEW error codes.


 Value               Corresponding Error Code or Description

 noErr           No error.

 mZoneErr          Handle or pointer not in specified zone.

 mFullErr          2

MoveBlockMoveBlock (LabVIEW(LabVIEW ManagerManager Function)Function)

void MoveBlock(ps, pd, size);


                                                    © National Instruments 6493

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6493 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6494 ordinal=6494 -->
## Property and Method Reference

Property and Method Reference

     Purpose

      Moves size bytes from one address to another. The source and destination memory
       blocks can overlap.

     Parameters

      Name      Type             Description

        ps        UPtr             Pointer to source.

       pd        UPtr             Pointer to destination.

          size       size_t       Number of bytes you want to move.

     NumericArrayResizeNumericArrayResize (LabVIEW(LabVIEW ManagerManager Function)Function)

      MgErr NumericArrayResize (int32 typeCode, int32 numDims, Uhandle *dataHP, size_t
       totalNewSize)

     Purpose

       Resizes a data handle that refers to a numeric array. This routine also accounts for
      alignment issues. It does not set the array dimension field. If *dataHP is NULL,
      LabVIEW allocates a new array handle in *dataHP.

     Parameters

      Name        Type      Description

        typeCode    int32    Data type for the array you want to resize.

       numDims    int32   Number of dimensions in the data structure to which the handle refers.

        *dataHP     UHandle  Pointer to the handle you want to resize.

        totalNewSize size_t  New number of elements to which the handle refers.

     Return Value

      MgErr, which can contain the following errors. If you receive errors from LabVIEW

6494   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6494 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6495 ordinal=6495 -->
## Property and Method Reference

Property and Method Reference

Manager functions, most error names correspond to LabVIEW error codes.


 Value               Corresponding Error Code or Description

 noErr           No error.

 mZoneErr          Handle or pointer not in specified zone.

 mFullErr          2

Possible Values for this Type Code Input

 Data Type                                      Type Code (numbers in hexadecimal)

 8-bit integer                                      01 or iB

 16-bit integer                                     02 or iW

 32-bit integer                                     03 or iL

 64-bit integer                                     04 or iQ

 8-bit unsigned integer                              05 or uB

 16-bit unsigned integer                             06 or uW

 32-bit unsigned integer                             07 or uL

 64-bit unsigned integer                             08 or uQ

 Single-precision, floating-point number               09 or fs

 Double-precision, floating-point number              0A or fD

 Extended-precision, floating-point number            0B or fX

 Complex single-precision, floating-point number       0C or cS

 Complex double-precision, floating-point number      0D or cD

 Complex extended-precision, floating-point number     0E or cX

SwapBlockSwapBlock (LabVIEW(LabVIEW ManagerManager Function)Function)

void SwapBlock(ps, pd, size);


                                                    © National Instruments 6495

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6495 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6496 ordinal=6496 -->
## Property and Method Reference

Property and Method Reference

     Purpose

      Swaps size bytes between the section of memory referred to by ps and pd. The source
      and destination memory blocks should not overlap.

     Parameters

      Name      Type             Description

        ps        UPtr             Pointer to source.

       pd        UPtr             Pointer to destination.

          size       size_t       Number of bytes you want to move.

     SupportSupport ManagerManager FunctionsFunctions

      You can use the support manager functions for bit or byte manipulation of data, string
       manipulation, mathematical operations, sorting, searching, and determining the
       current time and date.

      You must include the appropriate header and library files to use these functions in a
      shared library.

      You can perform the following operations by using the functions listed.

            • Byte manipulation operations
     ◦ Cat4Chrs
     ◦ GetALong
     ◦ Hi16
     ◦ HiByte
     ◦ HiNibble
     ◦ Lo16
     ◦ LoByte
     ◦ Long
     ◦ LoNibble
     ◦ Offset
     ◦ SetALong
     ◦ Word

6496   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6496 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6497 ordinal=6497 -->
## Property and Method Reference

Property and Method Reference

• Mathematical operations
 ◦ Abs
 ◦ Max
 ◦ Min
 ◦ Pin
 ◦ RandomGen
• String manipulation
 ◦ BlockCmp
 ◦ CPStrBuf
 ◦ CPStrCmp
 ◦ CPStrIndex
 ◦ CPStrInsert
 ◦ CPStrLen
 ◦ CPStrRemove
 ◦ CPStrReplace
 ◦ CPStrSize
 ◦ CToPStr
 ◦ FileNameCmp
 ◦ FileNameIndCmp
 ◦ FileNameNCmp
 ◦ FPrintf
 ◦ HexChar
 ◦ IsAlpha
 ◦  IsDigit
 ◦ IsLower
 ◦ IsUpper
 ◦ LStrBuf
 ◦ LStrCmp
 ◦ LStrLen
 ◦ LStrPrintf
 ◦ LToCStr
 ◦ LToPStr
 ◦ PPrintf
 ◦ PPrintfp
 ◦ PPStrCaseCmp
 ◦ PPStrCmp
 ◦ PStrBuf


                                                   © National Instruments 6497

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6497 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6498 ordinal=6498 -->
## Property and Method Reference

Property and Method Reference

     ◦ PStrCaseCmp
     ◦ PStrCat
     ◦ PStrCmp
     ◦ PStrCpy
     ◦ PStrLen
     ◦ PStrNCpy
     ◦ PToCStr
     ◦ PToLStr
     ◦ SPrintf
     ◦ SPrintfp
     ◦ StrCat
     ◦ StrCmp
     ◦ StrCpy
     ◦ StrLen
     ◦ StrNCaseCmp
     ◦ StrNCmp
     ◦ StrNCpy
     ◦ ToLower
     ◦ ToUpper
            • Synchronization functions
     ◦ Occur
     ◦ PostLVUserEvent
            •  Utility functions
     ◦ BinSearch
     ◦ NIGetOneErrorCode
     ◦ QSort
     ◦ Unused
            • Time functions
     ◦ ASCIITime
     ◦ DateCString
     ◦ DateToSecs
     ◦ MilliSecs
     ◦ SecsToDate
     ◦ TimeCString
     ◦ TimeInSecs


6498   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6498 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6499 ordinal=6499 -->
## Property and Method Reference

Property and Method Reference

AbsAbs (LabVIEW(LabVIEW ManagerManager Function)Function)

int32 Abs(n);

Purpose

Returns the absolute value of n, unless n is –231, in which case the function returns the
number unmodified.

Parameters

 Name    Type       Description

 n       int32    int32 whose absolute value you want to determine.

Return Value

The resulting int32.

ASCIITimeASCIITime (LabVIEW(LabVIEW ManagerManager Function)Function)

CStr ASCIITime(secs);

Purpose

Returns a pointer to a string representing the date and time of day corresponding to t
seconds after 12:00 a.m., Friday, January 1, 1904, Universal Time [01-01-1904
00:00:00]. This function uses the same date format as that returned by the DateCString
function using a mode of 2. The date is followed by a space. The time is in the same
format as that returned by the TimeCString function using a mode of 0. For example,
this function might return Tuesday, Dec 22, 1992 5:30. Date formats vary
with your system configuration.

Parameters

 Name Type     Description

 secs  uInt32 Seconds since 12:00 a.m., Friday, January 1, 1904, Universal Time [01-01-1904

                                                    © National Instruments 6499

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6499 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6500 ordinal=6500 -->
## Property and Method Reference

Property and Method Reference


      Name Type     Description

                            00:00:00].

     Return Value

      The date and time as a C string.

     BinSearchBinSearch (LabVIEW(LabVIEW ManagerManager Function)Function)

     int32 BinSearch(arrayp, n, elmtSize, key, compareProcP);

     Purpose

      Searches an array of an arbitrary data type using the binary search algorithm. In
       addition to passing the array you want to search to this routine, you also pass a
      comparison procedure that this sort routine then uses to compare elements in the
        array.

      The comparison routine should return a number less than zero if a is less than b, zero if
      a is equal to b, and a number greater than zero if a is greater than b.

      You should declare the comparison routine to have the following parameters and
       return type:

       int32 compareProcP(UPtr a, UPtr b);

     Parameters

      Name         Type      Description

        arrayp       UPtr      Pointer to an array of data.

       n           int32   Number of elements in the array you want to search.

        elmtSize     int32    Size in bytes of an array element.

        key         UPtr      Pointer to the data for which you want to search.

                               Comparison routine you want BinSearch to use to compare array
       compareProcP ProcPtr
                                   elements. BinSearch passes this routine the addresses of two


6500   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6500 -->

