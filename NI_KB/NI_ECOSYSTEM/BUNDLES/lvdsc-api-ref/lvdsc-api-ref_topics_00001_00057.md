# NI DOCUMENT BUNDLE: lvdsc-api-ref

<!--NI_BUNDLE_CHUNK bundle=lvdsc-api-ref start=1 end=57 -->
<!--NI_TOPIC bundle=lvdsc-api-ref path=dialog-boxes/citadel-4-database-backup-path-dialog-box.html language=enus -->
## TOPIC 00001: Citadel 4 Database Backup Path Dialog Box

- bundle_id: `lvdsc-api-ref`
- source_path: `dialog-boxes/citadel-4-database-backup-path-dialog-box.html`
- source_url: https://docs-be.ni.com/bundle/lvdsc-api-ref/raw/resource/enus/dialog-boxes/citadel-4-database-backup-path-dialog-box.html
- document_id: `lvdsc-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: You do not have enough space on the selected drive to complete converting the Citadel 4 database to a Citadel 5 database. Select a directory on another drive to move the existing Citadel 4 database to and click the Convert button to continue the conversion. Click the Cancel button to cancel the conv

### Citadel 4 Database Backup Path Dialog Box

You do not have enough space on the selected drive to complete converting the Citadel 4 database to a Citadel 5 database. Select a directory on another drive to move the existing Citadel 4 database to and click the **Convert** button to continue the conversion.

Click the **Cancel** button to cancel the conversion.

<!--NI_TOPIC bundle=lvdsc-api-ref path=dialog-boxes/configure-alarm-printer-i-o-server-dialog-box.html language=enus -->
## TOPIC 00002: Configure Alarm Printer I/O Server Dialog Box

- bundle_id: `lvdsc-api-ref`
- source_path: `dialog-boxes/configure-alarm-printer-i-o-server-dialog-box.html`
- source_url: https://docs-be.ni.com/bundle/lvdsc-api-ref/raw/resource/enus/dialog-boxes/configure-alarm-printer-i-o-server-dialog-box.html
- document_id: `lvdsc-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: In the Create New I/O Server dialog box, select Alarm Printer from the I/O Server Type list and click the Continue button to display this dialog box. You also can right-click an existing Alarm Printer I/O server and select Properties from the shortcut menu to display this dialog box. Use this dialog

### Configure Alarm Printer I/O Server Dialog Box

In the [Create New I/O Server](/csh?context=lvmnt_dsc_lvmve_dsc_createioserver) dialog box, select **Alarm Printer** from the **I/O Server Type** list and click the **Continue** button to display this dialog box. You also can right-click an existing [Alarm Printer I/O server](/csh?context=lvmnt_dsc_lvdscconcepts_print_alarms_info) and select **Properties** from the shortcut menu to display this dialog box.

Use this dialog box to configure an instance of the Alarm Printer I/O server you want to use. The Alarm Printer I/O server allows you to send alarm and event data to a line printer.

This dialog box contains the following components:

- Port Settings —Displays options for configuring the printer with which you want to print alarm and event data. This page includes the following components:
  - Printer Port —Specifies the serial or parallel port of the printer to which the Alarm Printer I/O server connects.
  - Baud Rate —Specifies the baud rate of this instance of the Alarm Printer I/O server. You can select a value from 2400 to 115200 .
  - Data Bits —Specifies how many data bits this instance of the Alarm Printer I/O server uses. You can select 7 or 8 .
  - Parity —Specifies the parity of this instance of the Alarm Printer I/O server. You can select none , even , odd , mark , or space .
  - Stop Bits —Specifies the number of stop bits this instance of the Alarm Printer I/O server uses. You can select 1 , 1.5 , or 2 .
- Format —Displays the alarm and event information that you can print. This page includes the following components:
  - Alarm or Event —Specifies whether to print the words Alarm or Event to indicate the type of occurrence.
  - Object Name —Specifies whether to print the name of the alarm or event. The printer prints the full network path to the object.
  - Set Time —Specifies whether to print the time that the alarm or event occurred.
  - Set User —Specifies whether to print the user who triggered the alarm or event.
  - Ack Time —Specifies whether to print the time that the alarm or event was acknowledged.
  - Ack User —Specifies whether to print the user who acknowledged the alarm or event.
  - Clear Time —Specifies whether to print the time that the alarm or event was cleared.
  - Clear User —Specifies whether to print the user who cleared the alarm or event.
  - Priority —Specifies whether to print the priority of the alarm.
  - Area —Specifies whether to print the area to which the alarm belongs.
  - Value —Specifies whether to print the value of the data item when the alarm occurred.
  - Setpoint —Specifies whether to print the value of the data item you set to trigger the alarm.
  - Description —Specifies whether to print the description of the alarm or event.
  - Ack Comment —Specifies whether to print the comment entered when the alarm or event was acknowledged.
  - Date Format —Specifies the format in which to print the date when you print the Set Time , Ack Time , or Clear Time . You can select MM/DD/YYYY or DD/MM/YYYY .
  - Time Format —Specifies the format in which to print the time when you print the Set Time , Ack Time , or Clear Time . You can select AM/PM or 24 HOUR .

The printer prints the alarm and event information in the same order as listed above. A comma separates each field of information.

<!--NI_TOPIC bundle=lvdsc-api-ref path=menus/categories/dsc-module/spc/processstatistics-graphing-vis-mnu.html language=enus -->
## TOPIC 00003: Process Statistics Graphing VIs

- bundle_id: `lvdsc-api-ref`
- source_path: `menus/categories/dsc-module/spc/processstatistics-graphing-vis-mnu.html`
- source_url: https://docs-be.ni.com/bundle/lvdsc-api-ref/raw/resource/enus/menus/categories/dsc-module/spc/processstatistics-graphing-vis-mnu.html
- document_id: `lvdsc-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Use the Process Statistics Graphing VIs to plot graphs for process statistics. icon

### Process Statistics Graphing VIs

Use the Process Statistics Graphing VIs to plot graphs for process statistics.

[IMAGE alt='icon' src='processstatistics-graphing-vis-mnu.png']

- [Plot Vertical Bar Graph VI](../../../../vi-lib/addons/spc/0spcctls-llb/plot-vertical-bar-graph-vi.html) Creates a centered vertical bar graph. Bars are centered at the x[] values, with height y[]. Can be used to plot a histogram.
- [Plot Vertical Bar Graph with Limits VI](../../../../vi-lib/addons/spc/0spcctls-llb/plot-vertical-bar-graph-with-limits-vi.html) Creates a vertical bar graph centered at each of the bin centers x[] and plots the specification limits and natural process limits as vertical lines against the bar graph. This is useful for viewing the results of a histogram against relevant limits. You can turn on and off drawing of the specification limits or the natural process limits, and specify the sigma multiplier to use for the natural process limits (default 3), by wiring in the display mode. If the display mode is not wired, the specification limits and natural process limits (at 3 sigma) will be drawn by default.
- [Plot Normal PDF Graph VI](../../../../vi-lib/addons/spc/0spcctls-llb/plot-normal-pdf-graph-vi.html) Given the process mean and sigma, creates an X-Y graph of a normal Probability Distribution Function (PDF) for the process. Also returns a normal distribution array.
- [Plot Normal PDF Graph with Limits VI](../../../../vi-lib/addons/spc/0spcctls-llb/plot-normal-pdf-graph-with-limits-vi.html) Given the specification limits and the process mean and sigma, creates a graph of a normal Probability Distribution Function (PDF) of the process against the specification limits and process mean and sigma. This is a good way to represent process capability. You can turn on and off drawing of the specification limits or the natural process limits, and specify the sigma multiplier to use for the natural process limits (default 3), by wiring in the display mode. If the display mode is not wired, the specification limits and natural process limits are drawn automatically.
- [Plot Histogram and Normal PDF VI](../../../../vi-lib/addons/spc/0spcctls-llb/plot-histogram-and-normal-pdf-vi.html) Given the specification limits and the process mean and sigma, creates a graph of a normal Probability Distribution Function (PDF) of the process and a vertical bar graph centered at each of the bin centers x[] against the specification limits and process mean and sigma. You can turn on and off drawing of the specification limits or the natural process limits, and specify the sigma multiplier to use for the natural process limits (default 3), by wiring in the display mode. If the display mode is not wired, the specification limits and natural process limits (at 3 sigma) will be drawn by default.
- [Rotate Graph VI](../../../../vi-lib/addons/spc/0spcctls-llb/rotate-graph-vi.html) Given a multi-plot X-Y graph, transposes the X and Y values such that the graph is rotated clockwise 90 degrees. The X-Y Graph data type must be an array of clusters of plots, where a plot is an array of points. A point is defined as a cluster containing an x and y value.

Parent topic:

Process Statistics

<!--NI_TOPIC bundle=lvdsc-api-ref path=menus/categories/dsc-module/spc/spc-mnu.html language=enus -->
## TOPIC 00004: Statistical Process Control

- bundle_id: `lvdsc-api-ref`
- source_path: `menus/categories/dsc-module/spc/spc-mnu.html`
- source_url: https://docs-be.ni.com/bundle/lvdsc-api-ref/raw/resource/enus/menus/categories/dsc-module/spc/spc-mnu.html
- document_id: `lvdsc-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: The Statistical Process Control VIs contain controls and functions you can use for process monitoring applications. To use statistical process control effectively, you must be trained in statistical process control (SPC) methods. SPC training is necessary because success in an SPC program depends on

### Statistical Process Control

The Statistical Process Control VIs contain controls and functions you can use for process monitoring applications. To use statistical process control effectively, you must be trained in statistical process control (SPC) methods. SPC training is necessary because success in an SPC program depends on educated judgment and experience.

[IMAGE alt='icon' src='spc-mnu.png']

- [Control Charts](../../../../menus/categories/dsc-module/spc/controlcharts-mnu.html) The Control Charts VIs include variables charts, attributes charts, and rule-checking VIs. The Control Chart VIs compute control limits for control charts, create control chart graphs, and apply rules to control chart data that detect out-of-control conditions.
- [Process Statistics](../../../../menus/categories/dsc-module/spc/processstatistics-mnu.html) Use the Process Statistics VIs to estimate process distributions and capabilities, calculate and plot histograms, and plot and fit normal probability distribution functions to histograms.
- [Pareto Analysis](../../../../menus/categories/dsc-module/spc/paretoanalysis-mnu.html) Includes VIs for counting and sorting assigned causes and for creating Pareto charts. In statistical process control applications, you might need to quantify and prioritize assignable causes that prevent a process from being in control or otherwise prevent a product from conforming to specifications. You can assign causes to a sample when you detect samples are out of control from a control chart. Other items can prevent a product from conforming to specifications that need to be analyzed, such as tabulated results from product inspection. You can total, order, and present causes using the Pareto Analysis VIs.

Parent topic:

DSC Module

<!--NI_TOPIC bundle=lvdsc-api-ref path=vi-lib/addons/spc/0chart-llb/np-chart-vi.html language=enus -->
## TOPIC 00005: np Chart VI

- bundle_id: `lvdsc-api-ref`
- source_path: `vi-lib/addons/spc/0chart-llb/np-chart-vi.html`
- source_url: https://docs-be.ni.com/bundle/lvdsc-api-ref/raw/resource/enus/vi-lib/addons/spc/0chart-llb/np-chart-vi.html
- document_id: `lvdsc-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Computes points and limits for an np Chart - a control chart for number non-conforming. A range of indices for samples to be used and specific indices to ignore in the control calculation can also be specified. The actual number of samples used to calculate the control limits is supplied. FORMULAS:

### np Chart VI

Computes points and limits for an np Chart - a control chart for number non-conforming. A range of indices for samples to be used and specific indices to ignore in the control calculation can also be specified. The actual number of samples used to calculate the control limits is supplied.

FORMULAS:

pbar = · r / (n x r array length)
UCLnp = n x pbar + stderr mult x sqrt(n x pbar x (1-pbar))
CLnp = n x pbar
LCLnp = n x pbar - stderr mult x sqrt(n x pbar x (1-pbar))
standard error = sqrt(n x pbar x (1-pbar))

[IMAGE alt='icon' src='np-chart-vi.png']

#### Inputs/Outputs

| chart limit src — chart limit src specifies whether or not to use standard values for the chart limit calculations. If unwired this defaults to the most common case where the chart limits are calculated from the data in the input array. You do not have to wire this cluster unless you want the chart limits to be calculated from standard values. When using standard values, the center line for the control chart, np-bar, is set to n*p0. source — chart limit src specifies whether or not to use standard values for the chart limit calculations. If unwired this defaults to the most common case where the chart limits are calculated from the data in the input array. You do not have to wire this cluster unless you want the chart limits to be calculated from standard values. When using standard values, the center line for the control chart, np-bar, is set to n*p0. std p0 — chart limit src specifies whether or not to use standard values for the chart limit calculations. If unwired this defaults to the most common case where the chart limits are calculated from the data in the input array. You do not have to wire this cluster unless you want the chart limits to be calculated from standard values. When using standard values, the center line for the control chart, np-bar, is set to n*p0. r:# units non-conforming/sample — n: sample size — (U32) - Size of the unit sample. std error multiplier (3) — (DBL, default = 3.0). Ordinarily you would leave this unwired and the control chart limits are computed as +/- 3.0 standard errors. index spec — (Optional) cluster of: start index (I32) - index of the first sample to include in the control limit calculation. Default is 0 or index of the first sample in samples X array. end index (I32) - index of the last sample to include in the control limit calculation. Default is 0 which selects the last sample in samples X array. If this cluster is unwired, all samples in samples X input array are included in the control limit calculation. start index — (I32) - index of the first sample to include in the control limit calculation. Default is 0 or index of the first sample in samples X array. end index — (I32) - index of the last sample to include in the control limit calculation. Default is 0 which selects the last sample in samples X array. indices to ignore — indices to ignore is the indices of samples to exclude from the control limit calculation. Excluding samples is useful for eliminating out of control points from the control limit calculation. By default, this is an empty array. # samples in calc — (I32) - the number of samples used in the control limits calculation. r:# units non-conforming/sample unit — r:# units non-conforming/sample unit is the number of units non-conforming per sample inspected. np chart limits — cluster of: UCLnp (DBL) - the upper control limit. If std error multiplier is 3, this will be np-bar + 3 standard errors. CLnp (DBL) - the center line for the np control chart, np-bar. np-bar is the estimated number non-conforming for the process. LCLnp (DBL) - the lower control limit. If std error multiplier is 3, this will be np-bar - 3 standard errors. standard error (DBL) - the standard error associated with np-bar. UCLr — (DBL) - the upper control limit. If std error multiplier is 3, this will be np-bar + 3 standard errors. np-bar — (DBL) - the center line for the np control chart, np-bar. np-bar is the estimated number non-conforming for the process. LCLr — (DBL) - the lower control limit. If std error multiplier is 3, this will be np-bar - 3 standard errors. standard error — (DBL) - the standard error associated with np-bar. |
| --- |
| source — chart limit src specifies whether or not to use standard values for the chart limit calculations. If unwired this defaults to the most common case where the chart limits are calculated from the data in the input array. You do not have to wire this cluster unless you want the chart limits to be calculated from standard values. When using standard values, the center line for the control chart, np-bar, is set to n*p0. std p0 — chart limit src specifies whether or not to use standard values for the chart limit calculations. If unwired this defaults to the most common case where the chart limits are calculated from the data in the input array. You do not have to wire this cluster unless you want the chart limits to be calculated from standard values. When using standard values, the center line for the control chart, np-bar, is set to n*p0. |
| start index — (I32) - index of the first sample to include in the control limit calculation. Default is 0 or index of the first sample in samples X array. end index — (I32) - index of the last sample to include in the control limit calculation. Default is 0 which selects the last sample in samples X array. |
| UCLr — (DBL) - the upper control limit. If std error multiplier is 3, this will be np-bar + 3 standard errors. np-bar — (DBL) - the center line for the np control chart, np-bar. np-bar is the estimated number non-conforming for the process. LCLr — (DBL) - the lower control limit. If std error multiplier is 3, this will be np-bar - 3 standard errors. standard error — (DBL) - the standard error associated with np-bar. |

#### np Chart Details

The control limit calculations are as follows:If standard values are used for the control limit calculations, then np-bar is set to std n*p0, otherwise, np-bar is calculated from the input samples as specified by the index spec and indices to ignore inputs.[IMAGE alt='image' src='13-28-01.gif'], if calculated from input data, otherwise [IMAGE alt='image' src='13-28-02.gif'][IMAGE alt='image' src='13-28-03.gif'][IMAGE alt='image' src='13-28-04.gif'][IMAGE alt='image' src='13-28-05.gif'][IMAGE alt='image' src='13-28-06.gif']

Parent topic:

Control Charts

<!--NI_TOPIC bundle=lvdsc-api-ref path=vi-lib/addons/spc/0chart-llb/x-bar-r-chart-vi.html language=enus -->
## TOPIC 00006: X-bar & R Chart VI

- bundle_id: `lvdsc-api-ref`
- source_path: `vi-lib/addons/spc/0chart-llb/x-bar-r-chart-vi.html`
- source_url: https://docs-be.ni.com/bundle/lvdsc-api-ref/raw/resource/enus/vi-lib/addons/spc/0chart-llb/x-bar-r-chart-vi.html
- document_id: `lvdsc-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Computes points and limits for X-bar and Range control Charts - control charts for process mean and range. NOTE: Sample size (number of columns in the samples X array) may not exceed 25. A range of indices for samples to be used and specific indices to ignore in the control calculation can also be s

### X-bar & R Chart VI

Computes points and limits for X-bar and Range control Charts - control charts for process mean and range. NOTE: Sample size (number of columns in the samples X array) may not exceed 25. A range of indices for samples to be used and specific indices to ignore in the control calculation can also be specified. The actual number of samples used to calculate the control limits is supplied. 

FORMULAS:

UCLx = x-bar-bar + stderr mult x R-bar/(d2 x sqrt(n))
CLx = x-bar-bar
LCLx = x-bar-bar - stderr mult x R-bar/(d2 x sqrt(n))
standard error = R-bar/(d2 x sqrt(n))

UCLr = R-bar + stderr mult x d3 x R-bar/d2
CLr = R-bar
LCLr = R-bar - stderr mult x d3 x R-bar/d2
standard error = d3 x R-bar/d2

If std error multipler = 3.0, the formulas for calculating the control limits from the data are:

UCLx = x-bar-bar + A2*R-bar
LCLx = x-bar-bar - A2*R-bar

UCLr = D4*R-bar
LCLr = D3*R-bar

If std error multipler = 3.0, the formulas for calculating the control limits from given standard values: std sigma = std R0/d2

UCLx = std mean + A*std sigma
LCLx = std mean - A*std sigma

UCLr = D2*std sigma
LCLr = D1*std sigma

The constants d2, d3, A, A2, D1, D2, D3, and D4 are published in the table of factors and formulas for control charts for variables in ANSI/ASQC Standard A1-1987

[IMAGE alt='icon' src='x-bar-r-chart-vi.png']

#### Inputs/Outputs

| chart limit src — chart limit src specifies whether or not to use standard values for the chart limit calculations. If unwired, this cluster defaults to the common case where the chart limits are calculated from the data in the input sample array. You do not have to wire this cluster unless you want the chart limits to be calculated from standard values. When using standard values, the center line for the X-bar control chart, X-bar-bar, is set to std mean, and the center line for the s control chart, s-bar, is set to std s0, or std sigma*c4. source — chart limit src specifies whether or not to use standard values for the chart limit calculations. If unwired, this cluster defaults to the common case where the chart limits are calculated from the data in the input sample array. You do not have to wire this cluster unless you want the chart limits to be calculated from standard values. When using standard values, the center line for the X-bar control chart, X-bar-bar, is set to std mean, and the center line for the s control chart, s-bar, is set to std s0, or std sigma*c4. std mean — chart limit src specifies whether or not to use standard values for the chart limit calculations. If unwired, this cluster defaults to the common case where the chart limits are calculated from the data in the input sample array. You do not have to wire this cluster unless you want the chart limits to be calculated from standard values. When using standard values, the center line for the X-bar control chart, X-bar-bar, is set to std mean, and the center line for the s control chart, s-bar, is set to std s0, or std sigma*c4. std R0/sigma — chart limit src specifies whether or not to use standard values for the chart limit calculations. If unwired, this cluster defaults to the common case where the chart limits are calculated from the data in the input sample array. You do not have to wire this cluster unless you want the chart limits to be calculated from standard values. When using standard values, the center line for the X-bar control chart, X-bar-bar, is set to std mean, and the center line for the s control chart, s-bar, is set to std s0, or std sigma*c4. samples X — index spec — index spec is used to choose a range of samples in c to use for the control limit calculation. If you do not wire this cluster, all elements in c input array are included in the control limit calculation. start index — index spec is used to choose a range of samples in c to use for the control limit calculation. If you do not wire this cluster, all elements in c input array are included in the control limit calculation. end index — index spec is used to choose a range of samples in c to use for the control limit calculation. If you do not wire this cluster, all elements in c input array are included in the control limit calculation. indices to ignore — indices to ignore is the indices of samples to exclude from the control limit calculation. Excluding samples is useful for eliminating out of control points from the control limit calculation. By default, this is an empty array. std error multiplier (3) — (DBL, default = 3.0). Ordinarily you would leave this unwired and the control chart limits are computed as +/- 3.0 standard errors. X-bar-bar — (DBL) - this is an estimate of the process mean based on the grand average of the samples included in the control limit calculation. X-bar — X-bar chart limits — UCLx — CLx — LCLx — standard error — standard error is the standard error associated with the center line. Range R — R chart limits — UCLr — CLr — LCLr — standard error — standard error is the standard error associated with the center line. R-bar/d2 — (DBL) - This is an estimate of the process sigma (standard deviation) based on the average range of the samples included in the control limit calculation. # samples in calc — (I32) The number of samples used in the control limits calculation. |
| --- |
| source — chart limit src specifies whether or not to use standard values for the chart limit calculations. If unwired, this cluster defaults to the common case where the chart limits are calculated from the data in the input sample array. You do not have to wire this cluster unless you want the chart limits to be calculated from standard values. When using standard values, the center line for the X-bar control chart, X-bar-bar, is set to std mean, and the center line for the s control chart, s-bar, is set to std s0, or std sigma*c4. std mean — chart limit src specifies whether or not to use standard values for the chart limit calculations. If unwired, this cluster defaults to the common case where the chart limits are calculated from the data in the input sample array. You do not have to wire this cluster unless you want the chart limits to be calculated from standard values. When using standard values, the center line for the X-bar control chart, X-bar-bar, is set to std mean, and the center line for the s control chart, s-bar, is set to std s0, or std sigma*c4. std R0/sigma — chart limit src specifies whether or not to use standard values for the chart limit calculations. If unwired, this cluster defaults to the common case where the chart limits are calculated from the data in the input sample array. You do not have to wire this cluster unless you want the chart limits to be calculated from standard values. When using standard values, the center line for the X-bar control chart, X-bar-bar, is set to std mean, and the center line for the s control chart, s-bar, is set to std s0, or std sigma*c4. |
| start index — index spec is used to choose a range of samples in c to use for the control limit calculation. If you do not wire this cluster, all elements in c input array are included in the control limit calculation. end index — index spec is used to choose a range of samples in c to use for the control limit calculation. If you do not wire this cluster, all elements in c input array are included in the control limit calculation. |
| UCLx — CLx — LCLx — standard error — standard error is the standard error associated with the center line. |
| UCLr — CLr — LCLr — standard error — standard error is the standard error associated with the center line. |

Parent topic:

Control Charts

<!--NI_TOPIC bundle=lvdsc-api-ref path=vi-lib/addons/spc/0chart-llb/x-bar-s-chart-vi.html language=enus -->
## TOPIC 00007: X-bar & S Chart VI

- bundle_id: `lvdsc-api-ref`
- source_path: `vi-lib/addons/spc/0chart-llb/x-bar-s-chart-vi.html`
- source_url: https://docs-be.ni.com/bundle/lvdsc-api-ref/raw/resource/enus/vi-lib/addons/spc/0chart-llb/x-bar-s-chart-vi.html
- document_id: `lvdsc-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Computes points and limits for X-bar and S control Charts - control charts for mean and sample standard deviation. A range of indices for samples to be used and indices to ignore in the control calculation can also be specified. The actual number of samples used to calculate the control limits is su

### X-bar & S Chart VI

Computes points and limits for X-bar and S control Charts - control charts for mean and sample standard deviation. A range of indices for samples to be used and indices to ignore in the control calculation can also be specified. The actual number of samples used to calculate the control limits is supplied.

FORMULAS:

UCLx = x-bar-bar + stderr mult x S-bar/(c4 x sqrt(n)) 
CLx = x-bar-bar 
LCLx = x-bar-bar - stderr mult x S-bar/(c4 x sqrt(n))
standard error = S-bar/(c4 x sqrt(n)) 
UCLs = S-bar+stderr mult x S-bar x sqrt(1- c42)/c4
CLs = S-bar
LCLs = S-bar-stderr mult x S-bar x sqrt(1- c42)/c4 
standard error = S-bar x sqrt(1- c42)/c4

[IMAGE alt='icon' src='x-bar-s-chart-vi.png']

#### Inputs/Outputs

| chart limit src — chart limit src specifies whether or not to use standard values for the chart limit calculations. If unwired, this cluster defaults to the common case where the chart limits are calculated from the data in the input sample array. You do not have to wire this cluster unless you want the chart limits to be calculated from standard values. When using standard values, the center line for the X-bar control chart, X-bar-bar, is set to std mean, and the center line for the s control chart, s-bar, is set to std s0, or std sigma*c4. source — chart limit src specifies whether or not to use standard values for the chart limit calculations. If unwired, this cluster defaults to the common case where the chart limits are calculated from the data in the input sample array. You do not have to wire this cluster unless you want the chart limits to be calculated from standard values. When using standard values, the center line for the X-bar control chart, X-bar-bar, is set to std mean, and the center line for the s control chart, s-bar, is set to std s0, or std sigma*c4. std mean — chart limit src specifies whether or not to use standard values for the chart limit calculations. If unwired, this cluster defaults to the common case where the chart limits are calculated from the data in the input sample array. You do not have to wire this cluster unless you want the chart limits to be calculated from standard values. When using standard values, the center line for the X-bar control chart, X-bar-bar, is set to std mean, and the center line for the s control chart, s-bar, is set to std s0, or std sigma*c4. std s0/sigma — chart limit src specifies whether or not to use standard values for the chart limit calculations. If unwired, this cluster defaults to the common case where the chart limits are calculated from the data in the input sample array. You do not have to wire this cluster unless you want the chart limits to be calculated from standard values. When using standard values, the center line for the X-bar control chart, X-bar-bar, is set to std mean, and the center line for the s control chart, s-bar, is set to std s0, or std sigma*c4. samples X — s is the standard deviation of each input sample. This array is plotted on the s control chart. index spec — index spec is used to choose a range of samples in c to use for the control limit calculation. If you do not wire this cluster, all elements in c input array are included in the control limit calculation. start index — index spec is used to choose a range of samples in c to use for the control limit calculation. If you do not wire this cluster, all elements in c input array are included in the control limit calculation. end index — index spec is used to choose a range of samples in c to use for the control limit calculation. If you do not wire this cluster, all elements in c input array are included in the control limit calculation. indices to ignore — indices to ignore contains indices of samples to exclude from the control limit calculation, which is useful for eliminating out of control points from the control limit calculation. By default, this is an empty array. std error multiplier (3) — (DBL, default = 3.0). Ordinarily you would leave this unwired and the control chart limits are computed as +/- 3.0 standard errors. X-bar-bar — (DBL) - this is an estimate of the process mean based on the grand average of the samples included in the control limit calculation. X-bar — s is the standard deviation of each input sample. This array is plotted on the s control chart. X-bar chart limits — s is the standard deviation of each input sample. This array is plotted on the s control chart. UCLx — s is the standard deviation of each input sample. This array is plotted on the s control chart. CLx — s is the standard deviation of each input sample. This array is plotted on the s control chart. LCLx — s is the standard deviation of each input sample. This array is plotted on the s control chart. standard error — standard error is the standard error associated with the center line. s — s is the standard deviation of each input sample. This array is plotted on the s control chart. s chart limits — s is the standard deviation of each input sample. This array is plotted on the s control chart. UCLs — s is the standard deviation of each input sample. This array is plotted on the s control chart. CLs — s is the standard deviation of each input sample. This array is plotted on the s control chart. LCLs — s is the standard deviation of each input sample. This array is plotted on the s control chart. standard error — standard error is the standard error associated with the center line. s-bar/c4 — This is an estimate of the process sigma (standard deviation) based on the average standard deviation of the samples included in the control limit calculation. # samples in calc — (I32) The number of samples used in the control limits calculation. |
| --- |
| source — chart limit src specifies whether or not to use standard values for the chart limit calculations. If unwired, this cluster defaults to the common case where the chart limits are calculated from the data in the input sample array. You do not have to wire this cluster unless you want the chart limits to be calculated from standard values. When using standard values, the center line for the X-bar control chart, X-bar-bar, is set to std mean, and the center line for the s control chart, s-bar, is set to std s0, or std sigma*c4. std mean — chart limit src specifies whether or not to use standard values for the chart limit calculations. If unwired, this cluster defaults to the common case where the chart limits are calculated from the data in the input sample array. You do not have to wire this cluster unless you want the chart limits to be calculated from standard values. When using standard values, the center line for the X-bar control chart, X-bar-bar, is set to std mean, and the center line for the s control chart, s-bar, is set to std s0, or std sigma*c4. std s0/sigma — chart limit src specifies whether or not to use standard values for the chart limit calculations. If unwired, this cluster defaults to the common case where the chart limits are calculated from the data in the input sample array. You do not have to wire this cluster unless you want the chart limits to be calculated from standard values. When using standard values, the center line for the X-bar control chart, X-bar-bar, is set to std mean, and the center line for the s control chart, s-bar, is set to std s0, or std sigma*c4. |
| start index — index spec is used to choose a range of samples in c to use for the control limit calculation. If you do not wire this cluster, all elements in c input array are included in the control limit calculation. end index — index spec is used to choose a range of samples in c to use for the control limit calculation. If you do not wire this cluster, all elements in c input array are included in the control limit calculation. |
| UCLx — s is the standard deviation of each input sample. This array is plotted on the s control chart. CLx — s is the standard deviation of each input sample. This array is plotted on the s control chart. LCLx — s is the standard deviation of each input sample. This array is plotted on the s control chart. standard error — standard error is the standard error associated with the center line. |
| UCLs — s is the standard deviation of each input sample. This array is plotted on the s control chart. CLs — s is the standard deviation of each input sample. This array is plotted on the s control chart. LCLs — s is the standard deviation of each input sample. This array is plotted on the s control chart. standard error — standard error is the standard error associated with the center line. |

Parent topic:

Control Charts

<!--NI_TOPIC bundle=lvdsc-api-ref path=vi-lib/addons/spc/0chart-llb/x-mr-chart-vi.html language=enus -->
## TOPIC 00008: x & mR Chart VI

- bundle_id: `lvdsc-api-ref`
- source_path: `vi-lib/addons/spc/0chart-llb/x-mr-chart-vi.html`
- source_url: https://docs-be.ni.com/bundle/lvdsc-api-ref/raw/resource/enus/vi-lib/addons/spc/0chart-llb/x-mr-chart-vi.html
- document_id: `lvdsc-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Computes points and limits for individuals x and Moving Range Charts - control charts for mean and moving range.This VI computes the moving range over n consecutive observations where n may range from 2 to 25. A range of indices for individuals to be used and individuals to ignore in the control cal

### x & mR Chart VI

Computes points and limits for individuals x and Moving Range Charts - control charts for mean and moving range.This VI computes the moving range over n consecutive observations where n may range from 2 to 25. A range of indices for individuals to be used and individuals to ignore in the control calculation can also be specified. The actual number of individuals used to calculate the control limits is supplied.

FORMULAS:

UCLx = x-bar + stderr mult x mR-bar/d2
CLx = x-bar
LCLx = x-bar - stderr mult x mR-bar/ d2
standard error = mR-bar/d2

UCLmr = mR-bar + stderr mult x d3 x mR-bar/d2
CLmr = mR-bar
LCLmr = mR-bar - stderr mult x d3 x mR-bar/d2
standard error = d3 x mR-bar/d2

If std error multipler = 3.0, the formulas for calculating the control limits from the data are:

UCLx = x-bar + E2*mR-bar
LCLx = x-bar - E2*mR-bar

UCLr = D4*mR-bar
LCLr = D3*mR-bar

If std error multipler = 3.0, the formulas for calculating the control limits from given standard values: std sigma = std R0/d2

UCLx = std mean + 3*std sigma
LCLx = std mean - 3*std sigma

UCLr = D2*std sigma
LCLr = D1*std sigma

The constants d2, d3, E2, D1, D2, D3, and D4 are published in the table of factors and formulas for control charts for variables in ANSI/ASQC Standard A1-1987

[IMAGE alt='icon' src='x-mr-chart-vi.png']

#### Inputs/Outputs

| chart limit src — chart limit src specifies whether or not to use standard values for the chart limit calculations. If unwired, this cluster defaults to the common case where the chart limits are calculated from the data in the input sample array. You do not have to wire this cluster unless you want the chart limits to be calculated from standard values. When using standard values, the center line for the X-bar control chart, X-bar-bar, is set to std mean, and the center line for the s control chart, s-bar, is set to std s0, or std sigma*c4. source — chart limit src specifies whether or not to use standard values for the chart limit calculations. If unwired, this cluster defaults to the common case where the chart limits are calculated from the data in the input sample array. You do not have to wire this cluster unless you want the chart limits to be calculated from standard values. When using standard values, the center line for the X-bar control chart, X-bar-bar, is set to std mean, and the center line for the s control chart, s-bar, is set to std s0, or std sigma*c4. std mean — chart limit src specifies whether or not to use standard values for the chart limit calculations. If unwired, this cluster defaults to the common case where the chart limits are calculated from the data in the input sample array. You do not have to wire this cluster unless you want the chart limits to be calculated from standard values. When using standard values, the center line for the X-bar control chart, X-bar-bar, is set to std mean, and the center line for the s control chart, s-bar, is set to std s0, or std sigma*c4. std R0/sigma — chart limit src specifies whether or not to use standard values for the chart limit calculations. If unwired, this cluster defaults to the common case where the chart limits are calculated from the data in the input sample array. You do not have to wire this cluster unless you want the chart limits to be calculated from standard values. When using standard values, the center line for the X-bar control chart, X-bar-bar, is set to std mean, and the center line for the s control chart, s-bar, is set to std s0, or std sigma*c4. individuals x — individuals x are the individual observations (or samples of subgroup size 1) on which to compute control limits. index spec — (Optional) cluster of: start index (I32) - index of the first sample to include in the control limit calculation. Default is 0 or index of the first sample in samples X array. end index (I32) - index of the last sample to include in the control limit calculation. Default is 0 which selects the last sample in samples X array. If this cluster is unwired, all samples in samples X input array are included in the control limit calculation. start index — (I32) - index of the first sample to include in the control limit calculation. Default is 0 or index of the first sample in samples X array. end index — (I32) - index of the last sample to include in the control limit calculation. Default is 0 which selects the last sample in samples X array. indices to ignore — indices to ignore is the indices of samples to exclude from the control limit calculation. Excluding samples is useful for eliminating out of control points from the control limit calculation. By default, this is an empty array. std error multiplier (3) — (DBL, default = 3.0). Ordinarily you would leave this unwired and the control chart limits are computed as +/- 3.0 standard errors. n: sample size (2) — (I32) The number of individuals to use for the moving Range calculation. Min value is 2, max value is 25. Default value is 2. x-bar & mR-bar/d2 — x-bar is an estimate of the process mean based on the average of the individuals included in the control limit calculation. x-bar — x-bar is an estimate of the process mean based on the average of the individuals included in the control limit calculation. mR-bar/d2 — x-bar is an estimate of the process mean based on the average of the individuals included in the control limit calculation. x — x is the individual observations. This is the array plotted on the x control chart. x chart limits — cluster of: UCLx (DBL) - the upper control limit for the x chart. CLx (DBL) - the center line for the x control chart. Clx = x-bar and is also the estimated process mean. LCLx (DBL) - the lower control limit for the x chart. standard error (DBL) - the standard error associated with x-bar. UCLx — (DBL) - the upper control limit for the x chart. CLx — (DBL) - the center line for the x control chart. Clx = x-bar and is also the estimated process mean. LCLx — (DBL) - the lower control limit for the x chart. standard error — (DBL) - the standard error associated with x-bar. moving range mR — mR chart limits — cluster of: UCLx (DBL) - the upper control limit for the x chart. CLx (DBL) - the center line for the x control chart. Clx = x-bar and is also the estimated process mean. LCLx (DBL) - the lower control limit for the x chart. standard error (DBL) - the standard error associated with x-bar. UCLmr — (DBL) - the upper control limit for the x chart. CLmr — (DBL) - the center line for the x control chart. Clx = x-bar and is also the estimated process mean. LCLmr — (DBL) - the lower control limit for the x chart. standard error — (DBL) - the standard error associated with x-bar. # individuals in calc — (I32) The number of individuals used in the control limits calculation. |
| --- |
| source — chart limit src specifies whether or not to use standard values for the chart limit calculations. If unwired, this cluster defaults to the common case where the chart limits are calculated from the data in the input sample array. You do not have to wire this cluster unless you want the chart limits to be calculated from standard values. When using standard values, the center line for the X-bar control chart, X-bar-bar, is set to std mean, and the center line for the s control chart, s-bar, is set to std s0, or std sigma*c4. std mean — chart limit src specifies whether or not to use standard values for the chart limit calculations. If unwired, this cluster defaults to the common case where the chart limits are calculated from the data in the input sample array. You do not have to wire this cluster unless you want the chart limits to be calculated from standard values. When using standard values, the center line for the X-bar control chart, X-bar-bar, is set to std mean, and the center line for the s control chart, s-bar, is set to std s0, or std sigma*c4. std R0/sigma — chart limit src specifies whether or not to use standard values for the chart limit calculations. If unwired, this cluster defaults to the common case where the chart limits are calculated from the data in the input sample array. You do not have to wire this cluster unless you want the chart limits to be calculated from standard values. When using standard values, the center line for the X-bar control chart, X-bar-bar, is set to std mean, and the center line for the s control chart, s-bar, is set to std s0, or std sigma*c4. |
| start index — (I32) - index of the first sample to include in the control limit calculation. Default is 0 or index of the first sample in samples X array. end index — (I32) - index of the last sample to include in the control limit calculation. Default is 0 which selects the last sample in samples X array. |
| x-bar — x-bar is an estimate of the process mean based on the average of the individuals included in the control limit calculation. mR-bar/d2 — x-bar is an estimate of the process mean based on the average of the individuals included in the control limit calculation. |
| UCLx — (DBL) - the upper control limit for the x chart. CLx — (DBL) - the center line for the x control chart. Clx = x-bar and is also the estimated process mean. LCLx — (DBL) - the lower control limit for the x chart. standard error — (DBL) - the standard error associated with x-bar. |
| UCLmr — (DBL) - the upper control limit for the x chart. CLmr — (DBL) - the center line for the x control chart. Clx = x-bar and is also the estimated process mean. LCLmr — (DBL) - the lower control limit for the x chart. standard error — (DBL) - the standard error associated with x-bar. |

#### x & mR Chart Details

The control limit calculations are as follows.If standard values are used for the control limit calculations, then[IMAGE alt='image' src='13-17-01.gif'] (x-bar) is set to std mean[IMAGE alt='image' src='13-17-02.gif'] (mR-bar) is set to std R0 or std sigma * d2, otherwise, X and mR are calculated from the input samples as specified by the index spec and indices to ignore inputs.[IMAGE alt='image' src='13-17-03.gif'][IMAGE alt='image' src='13-17-04.gif'][IMAGE alt='image' src='13-17-05.gif'][IMAGE alt='image' src='13-17-06.gif'][IMAGE alt='image' src='13-17-07.gif'][IMAGE alt='image' src='13-17-08.gif'][IMAGE alt='image' src='13-17-09.gif'][IMAGE alt='image' src='13-17-10.gif']

Parent topic:

Control Charts

<!--NI_TOPIC bundle=lvdsc-api-ref path=vi-lib/addons/spc/0spcctls-llb/plot-normal-pdf-graph-with-limits-vi.html language=enus -->
## TOPIC 00009: Plot Normal PDF Graph with Limits VI

- bundle_id: `lvdsc-api-ref`
- source_path: `vi-lib/addons/spc/0spcctls-llb/plot-normal-pdf-graph-with-limits-vi.html`
- source_url: https://docs-be.ni.com/bundle/lvdsc-api-ref/raw/resource/enus/vi-lib/addons/spc/0spcctls-llb/plot-normal-pdf-graph-with-limits-vi.html
- document_id: `lvdsc-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Given the specification limits and the process mean and sigma, creates a graph of a normal Probability Distribution Function (PDF) of the process against the specification limits and process mean and sigma. This is a good way to represent process capability. You can turn on and off drawing of the sp

### Plot Normal PDF Graph with Limits VI

Given the specification limits and the process mean and sigma, creates a graph of a normal Probability Distribution Function (PDF) of the process against the specification limits and process mean and sigma. This is a good way to represent process capability. 

You can turn on and off drawing of the specification limits or the natural process limits, and specify the sigma multiplier to use for the natural process limits (default 3), by wiring in the display mode. If the display mode is not wired, the specification limits and natural process limits are drawn automatically.

[IMAGE alt='icon' src='plot-normal-pdf-graph-with-limits-vi.png']

#### Inputs/Outputs

| # PDF points to plot (50) — (I32, default 50) - The number of points to make up the Normal PDF plot. You can normally leave this unwired. PDF width (+/- sigma) — (DBL, default = 3.0) - The width to draw the PDF in terms of +/- sigma. If unconnected, the PDF is drawn from - 3 sigma to + 3 sigma by default. PDF height — (DBL, default = 0) - The height to draw the PDF. If 0, the PDF will be drawn with a height proportional to 1/(std dev) - corresponding to an area of 1 under the PDF curve. When fitting a normal PDF to a histogram, use the PDF Height output from the Fit Normal PDF to Histogram VI. upper spec limit — (DBL) - The upper specification limit of the process. lower spec limit — (DBL) - The lower specification limit of the process. process mean — (DBL) - the estimated process mean. See the Process Mean & Sigma VI or Sample Statistics VI. process sigma — (DBL) - the estimated process sigma. See the Process Mean & Sigma VI or Sample Statistics V. display mode (T,T,3) — Optional display mode specifier. Cluster of: show spec. limits (T) (Boolean) - if true, the specification limits will be drawn. show natural process limits (T) (Boolean) - if true, the natural process limits will be drawn on the plot. NPLimit sigma (3) (U32) - The sigma multiplier for the natural process limits. By default this is 3. The natural process limits drawn will then be process mean +/- NPLimit sigma*process sigma. Note that if you wire up the display mode cluster to change one of the default settings, you must specify all three elements. If unwired, the specification limits and the natural process limits will be drawn by default. show spec limits — (Boolean) - if true, the specification limits will be drawn. show natural process limits — (Boolean) - if true, the natural process limits will be drawn on the plot. NP limit sigma — (U32) - The sigma multiplier for the natural process limits. By default this is 3. The natural process limits drawn will then be process mean +/- NPLimit sigma*process sigma. normal PDF graph with limits — (X, Y Graph) - Normal probability distribution drawn with specification limits and natural process limits. |
| --- |
| show spec limits — (Boolean) - if true, the specification limits will be drawn. show natural process limits — (Boolean) - if true, the natural process limits will be drawn on the plot. NP limit sigma — (U32) - The sigma multiplier for the natural process limits. By default this is 3. The natural process limits drawn will then be process mean +/- NPLimit sigma*process sigma. |

Parent topic:

Process Statistics Graphing VIs

<!--NI_TOPIC bundle=lvdsc-api-ref path=vi-lib/addons/spc/0spcctls-llb/plot-vertical-bar-graph-vi.html language=enus -->
## TOPIC 00010: Plot Vertical Bar Graph VI

- bundle_id: `lvdsc-api-ref`
- source_path: `vi-lib/addons/spc/0spcctls-llb/plot-vertical-bar-graph-vi.html`
- source_url: https://docs-be.ni.com/bundle/lvdsc-api-ref/raw/resource/enus/vi-lib/addons/spc/0spcctls-llb/plot-vertical-bar-graph-vi.html
- document_id: `lvdsc-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Creates a centered vertical bar graph. Bars are centered at the x[] values, with height y[]. Can be used to plot a histogram. icon Inputs/Outputs c1du32.png histogram y[] histogram y[] arranges each element of this array so that the number of observations in each bin of the histogram is from left to

### Plot Vertical Bar Graph VI

Creates a centered vertical bar graph. Bars are centered at the x[] values, with height y[]. Can be used to plot a histogram.

[IMAGE alt='icon' src='plot-vertical-bar-graph-vi.png']

#### Inputs/Outputs

| histogram y[] — histogram y[] arranges each element of this array so that the number of observations in each bin of the histogram is from left to right. This is an output from the Histogram VI. bin centers x[] — bin centers x[] specifies the x-axis values for the center of each histogram bin. Connect the x values output of the histogram VI to this input. vertical bar graph — (X, Y Graph) - centered vertical bar graph, which each bar of the height given in the histogram y[] input and centered at the values given in the bin centers x[] input. |
| --- |

Parent topic:

Process Statistics Graphing VIs

<!--NI_TOPIC bundle=lvdsc-api-ref path=vi-lib/addons/spc/0spcctls-llb/plot-vertical-bar-graph-with-limits-vi.html language=enus -->
## TOPIC 00011: Plot Vertical Bar Graph with Limits VI

- bundle_id: `lvdsc-api-ref`
- source_path: `vi-lib/addons/spc/0spcctls-llb/plot-vertical-bar-graph-with-limits-vi.html`
- source_url: https://docs-be.ni.com/bundle/lvdsc-api-ref/raw/resource/enus/vi-lib/addons/spc/0spcctls-llb/plot-vertical-bar-graph-with-limits-vi.html
- document_id: `lvdsc-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Creates a vertical bar graph centered at each of the bin centers x[] and plots the specification limits and natural process limits as vertical lines against the bar graph. This is useful for viewing the results of a histogram against relevant limits. You can turn on and off drawing of the specificat

### Plot Vertical Bar Graph with Limits VI

Creates a vertical bar graph centered at each of the bin centers x[] and plots the specification limits and natural process limits as vertical lines against the bar graph. This is useful for viewing the results of a histogram against relevant limits. 

You can turn on and off drawing of the specification limits or the natural process limits, and specify the sigma multiplier to use for the natural process limits (default 3), by wiring in the display mode. If the display mode is not wired, the specification limits and natural process limits (at 3 sigma) will be drawn by default.

[IMAGE alt='icon' src='plot-vertical-bar-graph-with-limits-vi.png']

#### Inputs/Outputs

| bin centers/axis x[] — bin centers/axis x[] contains the x-axis values for the center of each histogram bin. Connect the x values output of the General Histogram VI to this input. histogram y[] — histogram y[] is organized so that each element of this array is arranged so that the number of observations in each bin of the histogram is from left to right. This is an output from the General Histogram VI. upper spec limit — (DBL) - The upper specification limit of the process. lower spec limit — (DBL) - The lower specification limit of the process. process mean — (DBL) - the estimated process mean. See the Process Mean & Sigma VI or Sample Statistics VI. process sigma — (DBL) - the estimated process sigma. See the Process Mean & Sigma VI or Sample Statistics VI. display mode (T,T,3) — Optional display mode specifier. Cluster of: show spec. limits (T) (Boolean) - if true, the specification limits will be drawn. show natural process limits (T) (Boolean) - if true, the natural process limits will be drawn on the plot. NPLimit sigma (3) (U32) - The sigma multiplier for the natural process limits. By default this is 3. The natural process limits drawn will then be process mean +/- NPLimit sigma*process sigma. Note that if you wire up the display mode cluster to change one of the default settings, you must specify all three elements. If unwired, the specification limits and the natural process limits will be drawn by default. show spec limits — (Boolean) - if true, the specification limits will be drawn. show natural process limits — (Boolean) - if true, the natural process limits will be drawn on the plot. NP limit sigma — (U32) - The sigma multiplier for the natural process limits. By default this is 3. The natural process limits drawn will then be process mean +/- NPLimit sigma*process sigma. vertical bar graph with limits — (X, Y Graph) - centered vertical bar graph with Limits optionally drawn at the natural process limits and specification limits. Each bar is drawn at the height given in the Histogram input and centered at the values given in the Bin Centers input. |
| --- |
| show spec limits — (Boolean) - if true, the specification limits will be drawn. show natural process limits — (Boolean) - if true, the natural process limits will be drawn on the plot. NP limit sigma — (U32) - The sigma multiplier for the natural process limits. By default this is 3. The natural process limits drawn will then be process mean +/- NPLimit sigma*process sigma. |

Parent topic:

Process Statistics Graphing VIs

<!--NI_TOPIC bundle=lvdsc-api-ref path=vi-lib/addons/spc/1prcstat-llb/process-mean-sigma-vi.html language=enus -->
## TOPIC 00012: Process Mean & Sigma VI

- bundle_id: `lvdsc-api-ref`
- source_path: `vi-lib/addons/spc/1prcstat-llb/process-mean-sigma-vi.html`
- source_url: https://docs-be.ni.com/bundle/lvdsc-api-ref/raw/resource/enus/vi-lib/addons/spc/1prcstat-llb/process-mean-sigma-vi.html
- document_id: `lvdsc-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Computes process mean and sigma and upper and lower natural process limits from process samples. The process sigma may be estimated in several ways. If the sample size is >1, either sample standard deviation s or range R can be used to estimate the process sigma. s or R are selected by the type inpu

### Process Mean & Sigma VI

Computes process mean and sigma and upper and lower natural process limits from process samples. The process sigma may be estimated in several ways. If the sample size is >1, either sample standard deviation s or range R can be used to estimate the process sigma. s or R are selected by the type input. If the sample size is 1, the moving range is used to estimate the process sigma. To calculate process mean and sigma on a 1D array, use the array builder primitive to create a 2D array and then wire to the samples X input. This VI interprets either a single column or a single row in a 2D array as sample size = 1.

[IMAGE alt='icon' src='process-mean-sigma-vi.png']

#### Inputs/Outputs

| samples X — type: s/R (s) — (U16) - Type of process sigma computation to perform. s: base process sigma on mean sample standard deviation (default) R: base process sigma on mean sample Range Note: if sample size is 1, process sigma is based on mean moving Range. n for moving Range (2) — (I32) - This input is ignored unless the sample size i.e. all the points in the input array samples X is contained in a single row, or there is only one column in the input array, in which case the moving range is used as a basis for estimating process mean and sigma. Min value for n is 2, max is 25. By default n is 2. sigma multiplier (3) — (DBL) - sigma multiplier for calculating upper and lower natural process limits. By default, sigma is multiplied by 3.0. process mean — (DBL) - mean of the process, estimated from X-bar-bar (or x-bar if sample size is 1). process sigma — (DBL) - sigma of the process, estimated from S-bar/c4 if type is S, R-bar/d2 if type is R, or mR-bar/d2 if sample size is 1. upper NPL — (DBL) - upper natural process limit of the process computed as process mean + sigma Multiplier * process sigma. By default this is process mean + 3.0*process sigma. lower NPL — (DBL) - lower natural process limit of the process computed as process mean - sigma multiplier * process sigma. By default this is process mean - 3.0*process sigma. |
| --- |

Parent topic:

Process Statistics

<!--NI_TOPIC bundle=lvdsc-api-ref path=vi-lib/addons/spc/1prcstat-llb/sample-statistics-vi.html language=enus -->
## TOPIC 00013: Sample Statistics VI

- bundle_id: `lvdsc-api-ref`
- source_path: `vi-lib/addons/spc/1prcstat-llb/sample-statistics-vi.html`
- source_url: https://docs-be.ni.com/bundle/lvdsc-api-ref/raw/resource/enus/vi-lib/addons/spc/1prcstat-llb/sample-statistics-vi.html
- document_id: `lvdsc-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Sample Statistics computes the standard deviation, mean (average), median, skewness and kurtosis of the input sample X containing n observations. median = middle value the values in Sample X. mean (X) = sum( X(i) )/n. Standard Deviation (X) = sqrt ( sum( (X[i] - mean (X)^2 )/(n-1) ). Skewness = sum(

### Sample Statistics VI

Sample Statistics computes the standard deviation, mean (average), median, skewness and kurtosis of the input sample X containing n observations.

median = middle value the values in Sample X.
mean (X) = sum( X(i) )/n.
Standard Deviation (X) = sqrt ( sum( (X[i] - mean (X)^2 )/(n-1) ).
Skewness = sum( sum( (X[i] - mean (X)^3 )/(n*std dev^3).
Kurtosis = sum( sum( (X[i] - mean (X)^4 )/(n*std dev^4).

[IMAGE alt='icon' src='sample-statistics-vi.png']

#### Inputs/Outputs

| sample X — median — (DBL) - center value of points in sample X. If the number of points in sample X is even, the median is the average of the center pair of points. mean — (DBL) - sample mean. sample std dev — (DBL) - sample standard deviation computed as sqrt ((X[i] - X-bar)^2)/(n-1)) where n is the number of points in X. skewness — (DBL) - degree of assymmetry of the sample X distribution around it's mean. A normal distribution has a skewness of 0. Skewness is computed as sum((X[i] - X-bar)^3)/(n*sample std. dev^3) where n is the number of points in X. kurtosis — (DBL) - relative peakedness or flatness of the sample X distribution. A normal distribution has a kurtosis of 3. Kurtosis is computed as sum((X[i] - X-bar)^4)/(n*sample std. dev^4) where n is the number of points in X. |
| --- |

Parent topic:

Process Statistics

<!--NI_TOPIC bundle=lvdsc-api-ref path=vi-lib/lvdsc/security/ni-security-get-group-info-id-principal-vi.html language=enus -->
## TOPIC 00014: NI Security Get Group Info (ID)(Principal) VI

- bundle_id: `lvdsc-api-ref`
- source_path: `vi-lib/lvdsc/security/ni-security-get-group-info-id-principal-vi.html`
- source_url: https://docs-be.ni.com/bundle/lvdsc-api-ref/raw/resource/enus/vi-lib/lvdsc/security/ni-security-get-group-info-id-principal-vi.html
- document_id: `lvdsc-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns basic information about a security group: group name, full group name, group description, and group ID. You define the group in the Domain Account Manager. You must manually select the polymorphic instance to use. Use the pull-down menu to select an instance of this VI. icon Inputs/Outputs c

### NI Security Get Group Info (ID)(Principal) VI

Returns basic information about a security group: group name, full group name, group description, and group ID. You define the group in the Domain Account Manager.

You must [manually select](/csh?context=lvcore_lvhowto_selectingdefaultinstpolyvi) the polymorphic instance to use.

Use the pull-down menu to select an instance of this VI.

[IMAGE alt='icon' src='ni-security-get-group-info-id-principal-vi.png']

#### Inputs/Outputs

| domain — domain is the domain principal to which to connect. machine — machine is the name of the computer where the domain is located. name — name is the name of the domain. ID — ID is the unique identifier of the domain. b0 — b1 — b2 — b3 — b4 — b5 — b6 — b7 — b8 — b9 — b10 — b11 — b12 — b13 — b14 — b15 — group — group is the unique identifier of the group. This VI returns basic information of this group. b0 — b1 — b2 — b3 — b4 — b5 — b6 — b7 — b8 — b9 — b10 — b11 — b12 — b13 — b14 — b15 — timeout (30 s) — timeout limits the time that this VI waits for the information to return from the domain. The default is 30 seconds. error in (no error) — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. group principal — group principal is the basic information about the group account. principal type — principal type returns whether the specified domain account is a group or user account. principal name — principal name returns the name of the user or group account. description — description returns the description of the user or group account. fullname — fullname returns the full name for the user or group account. ID — ID returns the unique identifier of the user or group account. b0 — b1 — b2 — b3 — b4 — b5 — b6 — b7 — b8 — b9 — b10 — b11 — b12 — b13 — b14 — b15 — error out — error out contains error information. This output provides standard error out functionality. |
| --- |
| machine — machine is the name of the computer where the domain is located. name — name is the name of the domain. ID — ID is the unique identifier of the domain. b0 — b1 — b2 — b3 — b4 — b5 — b6 — b7 — b8 — b9 — b10 — b11 — b12 — b13 — b14 — b15 — |
| b0 — b1 — b2 — b3 — b4 — b5 — b6 — b7 — b8 — b9 — b10 — b11 — b12 — b13 — b14 — b15 — |
| b0 — b1 — b2 — b3 — b4 — b5 — b6 — b7 — b8 — b9 — b10 — b11 — b12 — b13 — b14 — b15 — |
| principal type — principal type returns whether the specified domain account is a group or user account. principal name — principal name returns the name of the user or group account. description — description returns the description of the user or group account. fullname — fullname returns the full name for the user or group account. ID — ID returns the unique identifier of the user or group account. b0 — b1 — b2 — b3 — b4 — b5 — b6 — b7 — b8 — b9 — b10 — b11 — b12 — b13 — b14 — b15 — |
| b0 — b1 — b2 — b3 — b4 — b5 — b6 — b7 — b8 — b9 — b10 — b11 — b12 — b13 — b14 — b15 — |

Parent topic:

NI Security Get Group Info VI

<!--NI_TOPIC bundle=lvdsc-api-ref path=vi-lib/lvdsc/security/ni-security-get-group-info-name-id-vi.html language=enus -->
## TOPIC 00015: NI Security Get Group Info (Name)(ID) VI

- bundle_id: `lvdsc-api-ref`
- source_path: `vi-lib/lvdsc/security/ni-security-get-group-info-name-id-vi.html`
- source_url: https://docs-be.ni.com/bundle/lvdsc-api-ref/raw/resource/enus/vi-lib/lvdsc/security/ni-security-get-group-info-name-id-vi.html
- document_id: `lvdsc-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns basic information about a security group: group name, full group name, group description, and group ID. You define the group in the Domain Account Manager. You must manually select the polymorphic instance to use. Use the pull-down menu to select an instance of this VI. icon Inputs/Outputs c

### NI Security Get Group Info (Name)(ID) VI

Returns basic information about a security group: group name, full group name, group description, and group ID. You define the group in the Domain Account Manager.

You must [manually select](/csh?context=lvcore_lvhowto_selectingdefaultinstpolyvi) the polymorphic instance to use.

Use the pull-down menu to select an instance of this VI.

[IMAGE alt='icon' src='ni-security-get-group-info-name-id-vi.png']

#### Inputs/Outputs

| domain — domain is the unique identifier of the domain to connect to. b0 — b1 — b2 — b3 — b4 — b5 — b6 — b7 — b8 — b9 — b10 — b11 — b12 — b13 — b14 — b15 — group — group is the name of the security group. This VI returns basic information about this group. timeout (30 s) — timeout limits the time that this VI waits for the information to return from the domain. The default is 30 seconds. error in (no error) — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. group principal — group principal is the basic information about the group account. principal type — principal type returns whether the specified domain account is a group or user account. principal name — principal name returns the name of the user or group account. description — description returns the description of the user or group account. fullname — fullname returns the full name for the user or group account. ID — ID returns the unique identifier of the user or group account. b0 — b1 — b2 — b3 — b4 — b5 — b6 — b7 — b8 — b9 — b10 — b11 — b12 — b13 — b14 — b15 — error out — error out contains error information. This output provides standard error out functionality. |
| --- |
| b0 — b1 — b2 — b3 — b4 — b5 — b6 — b7 — b8 — b9 — b10 — b11 — b12 — b13 — b14 — b15 — |
| principal type — principal type returns whether the specified domain account is a group or user account. principal name — principal name returns the name of the user or group account. description — description returns the description of the user or group account. fullname — fullname returns the full name for the user or group account. ID — ID returns the unique identifier of the user or group account. b0 — b1 — b2 — b3 — b4 — b5 — b6 — b7 — b8 — b9 — b10 — b11 — b12 — b13 — b14 — b15 — |
| b0 — b1 — b2 — b3 — b4 — b5 — b6 — b7 — b8 — b9 — b10 — b11 — b12 — b13 — b14 — b15 — |

Parent topic:

NI Security Get Group Info VI

<!--NI_TOPIC bundle=lvdsc-api-ref path=vi-lib/lvdsc/security/ni-security-get-group-info-name-name-vi.html language=enus -->
## TOPIC 00016: NI Security Get Group Info (Name)(Name) VI

- bundle_id: `lvdsc-api-ref`
- source_path: `vi-lib/lvdsc/security/ni-security-get-group-info-name-name-vi.html`
- source_url: https://docs-be.ni.com/bundle/lvdsc-api-ref/raw/resource/enus/vi-lib/lvdsc/security/ni-security-get-group-info-name-name-vi.html
- document_id: `lvdsc-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns basic information about a security group: group name, full group name, group description, and group ID. You define the group in the Domain Account Manager. You must manually select the polymorphic instance to use. Use the pull-down menu to select an instance of this VI. icon Inputs/Outputs c

### NI Security Get Group Info (Name)(Name) VI

Returns basic information about a security group: group name, full group name, group description, and group ID. You define the group in the Domain Account Manager.

You must [manually select](/csh?context=lvcore_lvhowto_selectingdefaultinstpolyvi) the polymorphic instance to use.

Use the pull-down menu to select an instance of this VI.

[IMAGE alt='icon' src='ni-security-get-group-info-name-name-vi.png']

#### Inputs/Outputs

| domain machine — domain machine is the name of the computer where the domain is located. The default is localhost. domain name — domain name is the name of the domain that contains the groups and users that you want to modify. group — group is the name of the security group. This VI returns basic information about this group. timeout (30 s) — timeout limits the time that this VI waits for the information to return from the domain. The default is 30 seconds. error in (no error) — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. group principal — group principal is the basic information about the group account. principal type — principal type returns whether the specified domain account is a group or user account. principal name — principal name returns the name of the user or group account. description — description returns the description of the user or group account. fullname — fullname returns the full name for the user or group account. ID — ID returns the unique identifier of the user or group account. b0 — b1 — b2 — b3 — b4 — b5 — b6 — b7 — b8 — b9 — b10 — b11 — b12 — b13 — b14 — b15 — error out — error out contains error information. This output provides standard error out functionality. |
| --- |
| principal type — principal type returns whether the specified domain account is a group or user account. principal name — principal name returns the name of the user or group account. description — description returns the description of the user or group account. fullname — fullname returns the full name for the user or group account. ID — ID returns the unique identifier of the user or group account. b0 — b1 — b2 — b3 — b4 — b5 — b6 — b7 — b8 — b9 — b10 — b11 — b12 — b13 — b14 — b15 — |
| b0 — b1 — b2 — b3 — b4 — b5 — b6 — b7 — b8 — b9 — b10 — b11 — b12 — b13 — b14 — b15 — |

Parent topic:

NI Security Get Group Info VI

<!--NI_TOPIC bundle=lvdsc-api-ref path=vi-lib/lvdsc/security/ni-security-get-group-info-name-principal-vi.html language=enus -->
## TOPIC 00017: NI Security Get Group Info (Name)(Principal) VI

- bundle_id: `lvdsc-api-ref`
- source_path: `vi-lib/lvdsc/security/ni-security-get-group-info-name-principal-vi.html`
- source_url: https://docs-be.ni.com/bundle/lvdsc-api-ref/raw/resource/enus/vi-lib/lvdsc/security/ni-security-get-group-info-name-principal-vi.html
- document_id: `lvdsc-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns basic information about a security group: group name, full group name, group description, and group ID. You define the group in the Domain Account Manager. You must manually select the polymorphic instance to use. Use the pull-down menu to select an instance of this VI. icon Inputs/Outputs c

### NI Security Get Group Info (Name)(Principal) VI

Returns basic information about a security group: group name, full group name, group description, and group ID. You define the group in the Domain Account Manager.

You must [manually select](/csh?context=lvcore_lvhowto_selectingdefaultinstpolyvi) the polymorphic instance to use.

Use the pull-down menu to select an instance of this VI.

[IMAGE alt='icon' src='ni-security-get-group-info-name-principal-vi.png']

#### Inputs/Outputs

| domain — domain is the domain principal to which to connect. machine — machine is the name of the computer where the domain is located. name — name is the name of the domain. ID — ID is the unique identifier of the domain. b0 — b1 — b2 — b3 — b4 — b5 — b6 — b7 — b8 — b9 — b10 — b11 — b12 — b13 — b14 — b15 — group — group is the name of the security group. This VI returns basic information about this group. timeout (30 s) — timeout limits the time that this VI waits for the information to return from the domain. The default is 30 seconds. error in (no error) — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. group principal — group principal is the basic information about the group account. principal type — principal type returns whether the specified domain account is a group or user account. principal name — principal name returns the name of the user or group account. description — description returns the description of the user or group account. fullname — fullname returns the full name for the user or group account. ID — ID returns the unique identifier of the user or group account. b0 — b1 — b2 — b3 — b4 — b5 — b6 — b7 — b8 — b9 — b10 — b11 — b12 — b13 — b14 — b15 — error out — error out contains error information. This output provides standard error out functionality. |
| --- |
| machine — machine is the name of the computer where the domain is located. name — name is the name of the domain. ID — ID is the unique identifier of the domain. b0 — b1 — b2 — b3 — b4 — b5 — b6 — b7 — b8 — b9 — b10 — b11 — b12 — b13 — b14 — b15 — |
| b0 — b1 — b2 — b3 — b4 — b5 — b6 — b7 — b8 — b9 — b10 — b11 — b12 — b13 — b14 — b15 — |
| principal type — principal type returns whether the specified domain account is a group or user account. principal name — principal name returns the name of the user or group account. description — description returns the description of the user or group account. fullname — fullname returns the full name for the user or group account. ID — ID returns the unique identifier of the user or group account. b0 — b1 — b2 — b3 — b4 — b5 — b6 — b7 — b8 — b9 — b10 — b11 — b12 — b13 — b14 — b15 — |
| b0 — b1 — b2 — b3 — b4 — b5 — b6 — b7 — b8 — b9 — b10 — b11 — b12 — b13 — b14 — b15 — |

Parent topic:

NI Security Get Group Info VI

<!--NI_TOPIC bundle=lvdsc-api-ref path=vi-lib/lvdsc/security/ni-security-get-group-info-vi.html language=enus -->
## TOPIC 00018: NI Security Get Group Info VI

- bundle_id: `lvdsc-api-ref`
- source_path: `vi-lib/lvdsc/security/ni-security-get-group-info-vi.html`
- source_url: https://docs-be.ni.com/bundle/lvdsc-api-ref/raw/resource/enus/vi-lib/lvdsc/security/ni-security-get-group-info-vi.html
- document_id: `lvdsc-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns basic information about a security group: group name, full group name, group description, and group ID. You define the group in the Domain Account Manager. You must manually select the polymorphic instance to use. Use the pull-down menu to select an instance of this VI. icon

### NI Security Get Group Info VI

Returns basic information about a security group: group name, full group name, group description, and group ID. You define the group in the Domain Account Manager.

You must [manually select](/csh?context=lvcore_lvhowto_selectingdefaultinstpolyvi) the polymorphic instance to use.

Use the pull-down menu to select an instance of this VI.

[IMAGE alt='icon' src='ni-security-get-group-info-vi.png']

- [NI Security Get Group Info (Name)(Name) VI](../../../vi-lib/lvdsc/security/ni-security-get-group-info-name-name-vi.html) Returns basic information about a security group: group name, full group name, group description, and group ID. You define the group in the Domain Account Manager.
- [NI Security Get Group Info (Name)(Principal) VI](../../../vi-lib/lvdsc/security/ni-security-get-group-info-name-principal-vi.html) Returns basic information about a security group: group name, full group name, group description, and group ID. You define the group in the Domain Account Manager.
- [NI Security Get Group Info (Name)(ID) VI](../../../vi-lib/lvdsc/security/ni-security-get-group-info-name-id-vi.html) Returns basic information about a security group: group name, full group name, group description, and group ID. You define the group in the Domain Account Manager.
- [NI Security Get Group Info (ID)(Name) VI](../../../vi-lib/lvdsc/security/ni-security-get-group-info-id-name-vi.html) Returns basic information about a security group: group name, full group name, group description, and group ID. You define the group in the Domain Account Manager.
- [NI Security Get Group Info (ID)(Principal) VI](../../../vi-lib/lvdsc/security/ni-security-get-group-info-id-principal-vi.html) Returns basic information about a security group: group name, full group name, group description, and group ID. You define the group in the Domain Account Manager.
- [NI Security Get Group Info (ID)(ID) VI](../../../vi-lib/lvdsc/security/ni-security-get-group-info-id-id-vi.html) Returns basic information about a security group: group name, full group name, group description, and group ID. You define the group in the Domain Account Manager.

Parent topic:

Security

<!--NI_TOPIC bundle=lvdsc-api-ref path=vi-lib/lvdsc/security/ni-security-get-group-list-of-user-vi.html language=enus -->
## TOPIC 00019: NI Security Get Group List of User VI

- bundle_id: `lvdsc-api-ref`
- source_path: `vi-lib/lvdsc/security/ni-security-get-group-list-of-user-vi.html`
- source_url: https://docs-be.ni.com/bundle/lvdsc-api-ref/raw/resource/enus/vi-lib/lvdsc/security/ni-security-get-group-list-of-user-vi.html
- document_id: `lvdsc-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns a list of groups to which a specific user belongs. icon Inputs/Outputs ccclst.png domain domain is the domain principal to which to connect. cstr.png machine machine is the name of the computer where the domain is located. cstr.png name name is the name of the domain. cnclst.png ID ID is the

### NI Security Get Group List of User VI

Returns a list of groups to which a specific user belongs.

[IMAGE alt='icon' src='ni-security-get-group-list-of-user-vi.png']

#### Inputs/Outputs

| domain — domain is the domain principal to which to connect. machine — machine is the name of the computer where the domain is located. name — name is the name of the domain. ID — ID is the unique identifier of the domain. b0 — domain is the domain principal to which to connect. b1 — domain is the domain principal to which to connect. b2 — domain is the domain principal to which to connect. b3 — domain is the domain principal to which to connect. b4 — domain is the domain principal to which to connect. b5 — domain is the domain principal to which to connect. b6 — domain is the domain principal to which to connect. b7 — domain is the domain principal to which to connect. b8 — domain is the domain principal to which to connect. b9 — domain is the domain principal to which to connect. b10 — domain is the domain principal to which to connect. b11 — domain is the domain principal to which to connect. b12 — domain is the domain principal to which to connect. b13 — domain is the domain principal to which to connect. b14 — domain is the domain principal to which to connect. b15 — domain is the domain principal to which to connect. user — user is the unique identifier of the user. This VI returns a list of groups that the user belongs to. b0 — user is the unique identifier of the user. This VI returns a list of groups that the user belongs to. b1 — user is the unique identifier of the user. This VI returns a list of groups that the user belongs to. b2 — user is the unique identifier of the user. This VI returns a list of groups that the user belongs to. b3 — user is the unique identifier of the user. This VI returns a list of groups that the user belongs to. b4 — user is the unique identifier of the user. This VI returns a list of groups that the user belongs to. b5 — user is the unique identifier of the user. This VI returns a list of groups that the user belongs to. b6 — user is the unique identifier of the user. This VI returns a list of groups that the user belongs to. b7 — user is the unique identifier of the user. This VI returns a list of groups that the user belongs to. b8 — user is the unique identifier of the user. This VI returns a list of groups that the user belongs to. b9 — user is the unique identifier of the user. This VI returns a list of groups that the user belongs to. b10 — user is the unique identifier of the user. This VI returns a list of groups that the user belongs to. b11 — user is the unique identifier of the user. This VI returns a list of groups that the user belongs to. b12 — user is the unique identifier of the user. This VI returns a list of groups that the user belongs to. b13 — user is the unique identifier of the user. This VI returns a list of groups that the user belongs to. b14 — user is the unique identifier of the user. This VI returns a list of groups that the user belongs to. b15 — user is the unique identifier of the user. This VI returns a list of groups that the user belongs to. timeout (30 s) — timeout limits the time that this VI waits for the information to return from the domain. The default is 30 seconds. error in (no error) — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. group principals — group principals lists information about group accounts available from the domain. principal type — principal type returns whether the specified domain account is a group or user account. principal name — principal name returns the name of the user or group account. description — description returns the description of the user or group account. fullname — fullname returns the full name for the user or group account. ID — ID returns the unique identifier of the user or group account. b0 — group principals lists information about group accounts available from the domain. b1 — group principals lists information about group accounts available from the domain. b2 — group principals lists information about group accounts available from the domain. b3 — group principals lists information about group accounts available from the domain. b4 — group principals lists information about group accounts available from the domain. b5 — group principals lists information about group accounts available from the domain. b6 — group principals lists information about group accounts available from the domain. b7 — group principals lists information about group accounts available from the domain. b8 — group principals lists information about group accounts available from the domain. b9 — group principals lists information about group accounts available from the domain. b10 — group principals lists information about group accounts available from the domain. b11 — group principals lists information about group accounts available from the domain. b12 — group principals lists information about group accounts available from the domain. b13 — group principals lists information about group accounts available from the domain. b14 — group principals lists information about group accounts available from the domain. b15 — group principals lists information about group accounts available from the domain. error out — error out contains error information. This output provides standard error out functionality. |
| --- |
| machine — machine is the name of the computer where the domain is located. name — name is the name of the domain. ID — ID is the unique identifier of the domain. b0 — domain is the domain principal to which to connect. b1 — domain is the domain principal to which to connect. b2 — domain is the domain principal to which to connect. b3 — domain is the domain principal to which to connect. b4 — domain is the domain principal to which to connect. b5 — domain is the domain principal to which to connect. b6 — domain is the domain principal to which to connect. b7 — domain is the domain principal to which to connect. b8 — domain is the domain principal to which to connect. b9 — domain is the domain principal to which to connect. b10 — domain is the domain principal to which to connect. b11 — domain is the domain principal to which to connect. b12 — domain is the domain principal to which to connect. b13 — domain is the domain principal to which to connect. b14 — domain is the domain principal to which to connect. b15 — domain is the domain principal to which to connect. |
| b0 — domain is the domain principal to which to connect. b1 — domain is the domain principal to which to connect. b2 — domain is the domain principal to which to connect. b3 — domain is the domain principal to which to connect. b4 — domain is the domain principal to which to connect. b5 — domain is the domain principal to which to connect. b6 — domain is the domain principal to which to connect. b7 — domain is the domain principal to which to connect. b8 — domain is the domain principal to which to connect. b9 — domain is the domain principal to which to connect. b10 — domain is the domain principal to which to connect. b11 — domain is the domain principal to which to connect. b12 — domain is the domain principal to which to connect. b13 — domain is the domain principal to which to connect. b14 — domain is the domain principal to which to connect. b15 — domain is the domain principal to which to connect. |
| b0 — user is the unique identifier of the user. This VI returns a list of groups that the user belongs to. b1 — user is the unique identifier of the user. This VI returns a list of groups that the user belongs to. b2 — user is the unique identifier of the user. This VI returns a list of groups that the user belongs to. b3 — user is the unique identifier of the user. This VI returns a list of groups that the user belongs to. b4 — user is the unique identifier of the user. This VI returns a list of groups that the user belongs to. b5 — user is the unique identifier of the user. This VI returns a list of groups that the user belongs to. b6 — user is the unique identifier of the user. This VI returns a list of groups that the user belongs to. b7 — user is the unique identifier of the user. This VI returns a list of groups that the user belongs to. b8 — user is the unique identifier of the user. This VI returns a list of groups that the user belongs to. b9 — user is the unique identifier of the user. This VI returns a list of groups that the user belongs to. b10 — user is the unique identifier of the user. This VI returns a list of groups that the user belongs to. b11 — user is the unique identifier of the user. This VI returns a list of groups that the user belongs to. b12 — user is the unique identifier of the user. This VI returns a list of groups that the user belongs to. b13 — user is the unique identifier of the user. This VI returns a list of groups that the user belongs to. b14 — user is the unique identifier of the user. This VI returns a list of groups that the user belongs to. b15 — user is the unique identifier of the user. This VI returns a list of groups that the user belongs to. |
| principal type — principal type returns whether the specified domain account is a group or user account. principal name — principal name returns the name of the user or group account. description — description returns the description of the user or group account. fullname — fullname returns the full name for the user or group account. ID — ID returns the unique identifier of the user or group account. b0 — group principals lists information about group accounts available from the domain. b1 — group principals lists information about group accounts available from the domain. b2 — group principals lists information about group accounts available from the domain. b3 — group principals lists information about group accounts available from the domain. b4 — group principals lists information about group accounts available from the domain. b5 — group principals lists information about group accounts available from the domain. b6 — group principals lists information about group accounts available from the domain. b7 — group principals lists information about group accounts available from the domain. b8 — group principals lists information about group accounts available from the domain. b9 — group principals lists information about group accounts available from the domain. b10 — group principals lists information about group accounts available from the domain. b11 — group principals lists information about group accounts available from the domain. b12 — group principals lists information about group accounts available from the domain. b13 — group principals lists information about group accounts available from the domain. b14 — group principals lists information about group accounts available from the domain. b15 — group principals lists information about group accounts available from the domain. |
| b0 — group principals lists information about group accounts available from the domain. b1 — group principals lists information about group accounts available from the domain. b2 — group principals lists information about group accounts available from the domain. b3 — group principals lists information about group accounts available from the domain. b4 — group principals lists information about group accounts available from the domain. b5 — group principals lists information about group accounts available from the domain. b6 — group principals lists information about group accounts available from the domain. b7 — group principals lists information about group accounts available from the domain. b8 — group principals lists information about group accounts available from the domain. b9 — group principals lists information about group accounts available from the domain. b10 — group principals lists information about group accounts available from the domain. b11 — group principals lists information about group accounts available from the domain. b12 — group principals lists information about group accounts available from the domain. b13 — group principals lists information about group accounts available from the domain. b14 — group principals lists information about group accounts available from the domain. b15 — group principals lists information about group accounts available from the domain. |

Parent topic:

Security

<!--NI_TOPIC bundle=lvdsc-api-ref path=vi-lib/lvdsc/security/ni-security-get-group-list-principal-vi.html language=enus -->
## TOPIC 00020: NI Security Get Group List (Principal) VI

- bundle_id: `lvdsc-api-ref`
- source_path: `vi-lib/lvdsc/security/ni-security-get-group-list-principal-vi.html`
- source_url: https://docs-be.ni.com/bundle/lvdsc-api-ref/raw/resource/enus/vi-lib/lvdsc/security/ni-security-get-group-list-principal-vi.html
- document_id: `lvdsc-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns a list of groups available on a specific domain. Groups can contain users or other groups. You must manually select the polymorphic instance to use. Use the pull-down menu to select an instance of this VI. icon Inputs/Outputs ccclst.png domain domain is the domain principal to which to conne

### NI Security Get Group List (Principal) VI

Returns a list of groups available on a specific domain. Groups can contain users or other groups. You must manually select the polymorphic instance to use.

Use the pull-down menu to select an instance of this VI.

[IMAGE alt='icon' src='ni-security-get-group-list-principal-vi.png']

#### Inputs/Outputs

| domain — domain is the domain principal to which to connect. machine — machine is the name of the computer where the domain is located. name — name is the name of the domain. ID — ID is the unique identifier of the domain. b0 — b1 — b2 — b3 — b4 — b5 — b6 — b7 — b8 — b9 — b10 — b11 — b12 — b13 — b14 — b15 — timeout (30 s) — timeout limits the time that this VI waits for the information to return from the domain. The default is 30 seconds. error in (no error) — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. group principals — group principals lists information about group accounts available from the domain. principal type — principal type returns whether the specified domain account is a group or user account. principal name — principal name returns the name of the user or group account. description — description returns the description of the user or group account. fullname — fullname returns the full name for the user or group account. ID — ID returns the unique identifier of the user or group account. b0 — b1 — b2 — b3 — b4 — b5 — b6 — b7 — b8 — b9 — b10 — b11 — b12 — b13 — b14 — b15 — error out — error out contains error information. This output provides standard error out functionality. |
| --- |
| machine — machine is the name of the computer where the domain is located. name — name is the name of the domain. ID — ID is the unique identifier of the domain. b0 — b1 — b2 — b3 — b4 — b5 — b6 — b7 — b8 — b9 — b10 — b11 — b12 — b13 — b14 — b15 — |
| b0 — b1 — b2 — b3 — b4 — b5 — b6 — b7 — b8 — b9 — b10 — b11 — b12 — b13 — b14 — b15 — |
| principal type — principal type returns whether the specified domain account is a group or user account. principal name — principal name returns the name of the user or group account. description — description returns the description of the user or group account. fullname — fullname returns the full name for the user or group account. ID — ID returns the unique identifier of the user or group account. b0 — b1 — b2 — b3 — b4 — b5 — b6 — b7 — b8 — b9 — b10 — b11 — b12 — b13 — b14 — b15 — |
| b0 — b1 — b2 — b3 — b4 — b5 — b6 — b7 — b8 — b9 — b10 — b11 — b12 — b13 — b14 — b15 — |

Parent topic:

NI Security Get Group List VI

<!--NI_TOPIC bundle=lvdsc-api-ref path=vi-lib/lvdsc/security/ni-security-get-group-list-vi.html language=enus -->
## TOPIC 00021: NI Security Get Group List VI

- bundle_id: `lvdsc-api-ref`
- source_path: `vi-lib/lvdsc/security/ni-security-get-group-list-vi.html`
- source_url: https://docs-be.ni.com/bundle/lvdsc-api-ref/raw/resource/enus/vi-lib/lvdsc/security/ni-security-get-group-list-vi.html
- document_id: `lvdsc-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns a list of groups available on a specific domain. Groups can contain users or other groups. You must manually select the polymorphic instance to use. Use the pull-down menu to select an instance of this VI. icon

### NI Security Get Group List VI

Returns a list of groups available on a specific domain. Groups can contain users or other groups. You must manually select the polymorphic instance to use.

Use the pull-down menu to select an instance of this VI.

[IMAGE alt='icon' src='ni-security-get-group-list-vi.png']

- [NI Security Get Group List (Name) VI](../../../vi-lib/lvdsc/security/ni-security-get-group-list-name-vi.html) Returns a list of groups available on a specific domain. Groups can contain users or other groups. You must manually select the polymorphic instance to use.
- [NI Security Get Group List (Principal) VI](../../../vi-lib/lvdsc/security/ni-security-get-group-list-principal-vi.html) Returns a list of groups available on a specific domain. Groups can contain users or other groups. You must manually select the polymorphic instance to use.
- [NI Security Get Group List (ID) VI](../../../vi-lib/lvdsc/security/ni-security-get-group-list-id-vi.html) Returns a list of groups available on a specific domain. Groups can contain users or other groups. You must manually select the polymorphic instance to use.

Parent topic:

Security

<!--NI_TOPIC bundle=lvdsc-api-ref path=vi-lib/lvdsc/security/ni-security-get-user-info-id-id-vi.html language=enus -->
## TOPIC 00022: NI Security Get User Info (ID)(ID) VI

- bundle_id: `lvdsc-api-ref`
- source_path: `vi-lib/lvdsc/security/ni-security-get-user-info-id-id-vi.html`
- source_url: https://docs-be.ni.com/bundle/lvdsc-api-ref/raw/resource/enus/vi-lib/lvdsc/security/ni-security-get-user-info-id-id-vi.html
- document_id: `lvdsc-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns basic information about a user account, user name, user full name, user description, and user ID. You must manually select the polymorphic instance to use. Use the pull-down menu to select an instance of this VI. icon Inputs/Outputs cnclst.png domain domain is the unique identifier of the do

### NI Security Get User Info (ID)(ID) VI

Returns basic information about a user account, user name, user full name, user description, and user ID. You must manually select the polymorphic instance to use.

Use the pull-down menu to select an instance of this VI.

[IMAGE alt='icon' src='ni-security-get-user-info-id-id-vi.png']

#### Inputs/Outputs

| domain — domain is the unique identifier of the domain to connect to. b0 — b1 — b2 — b3 — b4 — b5 — b6 — b7 — b8 — b9 — b10 — b11 — b12 — b13 — b14 — b15 — user — user is the unique identifier of the user. This VI returns basic information of this user. b0 — b1 — b2 — b3 — b4 — b5 — b6 — b7 — b8 — b9 — b10 — b11 — b12 — b13 — b14 — b15 — timeout (30 s) — timeout limits the time that this VI waits for the information to return from the domain. The default is 30 seconds. error in (no error) — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. user principal — user principal is the basic information about the currently logged in user. principal type — principal type returns whether the specified domain account is a group or user account. principal name — principal name returns the name of the user or group account. description — description returns the description of the user or group account. fullname — fullname returns the full name for the user or group account. ID — ID returns the unique identifier of the user or group account. b0 — b1 — b2 — b3 — b4 — b5 — b6 — b7 — b8 — b9 — b10 — b11 — b12 — b13 — b14 — b15 — error out — error out contains error information. This output provides standard error out functionality. |
| --- |
| b0 — b1 — b2 — b3 — b4 — b5 — b6 — b7 — b8 — b9 — b10 — b11 — b12 — b13 — b14 — b15 — |
| b0 — b1 — b2 — b3 — b4 — b5 — b6 — b7 — b8 — b9 — b10 — b11 — b12 — b13 — b14 — b15 — |
| principal type — principal type returns whether the specified domain account is a group or user account. principal name — principal name returns the name of the user or group account. description — description returns the description of the user or group account. fullname — fullname returns the full name for the user or group account. ID — ID returns the unique identifier of the user or group account. b0 — b1 — b2 — b3 — b4 — b5 — b6 — b7 — b8 — b9 — b10 — b11 — b12 — b13 — b14 — b15 — |
| b0 — b1 — b2 — b3 — b4 — b5 — b6 — b7 — b8 — b9 — b10 — b11 — b12 — b13 — b14 — b15 — |

Parent topic:

NI Security Get User Info VI

<!--NI_TOPIC bundle=lvdsc-api-ref path=vi-lib/lvdsc/security/ni-security-get-user-info-id-name-vi.html language=enus -->
## TOPIC 00023: NI Security Get User Info (ID)(Name) VI

- bundle_id: `lvdsc-api-ref`
- source_path: `vi-lib/lvdsc/security/ni-security-get-user-info-id-name-vi.html`
- source_url: https://docs-be.ni.com/bundle/lvdsc-api-ref/raw/resource/enus/vi-lib/lvdsc/security/ni-security-get-user-info-id-name-vi.html
- document_id: `lvdsc-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns basic information about a user account, user name, user full name, user description, and user ID. You must manually select the polymorphic instance to use. Use the pull-down menu to select an instance of this VI. icon Inputs/Outputs cstr.png domain machine domain machine is the name of the c

### NI Security Get User Info (ID)(Name) VI

Returns basic information about a user account, user name, user full name, user description, and user ID. You must manually select the polymorphic instance to use.

Use the pull-down menu to select an instance of this VI.

[IMAGE alt='icon' src='ni-security-get-user-info-id-name-vi.png']

#### Inputs/Outputs

| domain machine — domain machine is the name of the computer where the domain is located. The default is localhost. domain name — domain name is the name of the domain that contains the groups and users that you want to modify. user — user is the unique identifier of the user. This VI returns basic information of this user. b0 — b1 — b2 — b3 — b4 — b5 — b6 — b7 — b8 — b9 — b10 — b11 — b12 — b13 — b14 — b15 — timeout (30 s) — timeout limits the time that this VI waits for the information to return from the domain. The default is 30 seconds. error in (no error) — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. user principal — user principal is the basic information about the currently logged in user. principal type — principal type returns whether the specified domain account is a group or user account. principal name — principal name returns the name of the user or group account. description — description returns the description of the user or group account. fullname — fullname returns the full name for the user or group account. ID — ID returns the unique identifier of the user or group account. b0 — b1 — b2 — b3 — b4 — b5 — b6 — b7 — b8 — b9 — b10 — b11 — b12 — b13 — b14 — b15 — error out — error out contains error information. This output provides standard error out functionality. |
| --- |
| b0 — b1 — b2 — b3 — b4 — b5 — b6 — b7 — b8 — b9 — b10 — b11 — b12 — b13 — b14 — b15 — |
| principal type — principal type returns whether the specified domain account is a group or user account. principal name — principal name returns the name of the user or group account. description — description returns the description of the user or group account. fullname — fullname returns the full name for the user or group account. ID — ID returns the unique identifier of the user or group account. b0 — b1 — b2 — b3 — b4 — b5 — b6 — b7 — b8 — b9 — b10 — b11 — b12 — b13 — b14 — b15 — |
| b0 — b1 — b2 — b3 — b4 — b5 — b6 — b7 — b8 — b9 — b10 — b11 — b12 — b13 — b14 — b15 — |

Parent topic:

NI Security Get User Info VI

<!--NI_TOPIC bundle=lvdsc-api-ref path=vi-lib/lvdsc/security/ni-security-get-user-info-id-principal-vi.html language=enus -->
## TOPIC 00024: NI Security Get User Info (ID)(Principal) VI

- bundle_id: `lvdsc-api-ref`
- source_path: `vi-lib/lvdsc/security/ni-security-get-user-info-id-principal-vi.html`
- source_url: https://docs-be.ni.com/bundle/lvdsc-api-ref/raw/resource/enus/vi-lib/lvdsc/security/ni-security-get-user-info-id-principal-vi.html
- document_id: `lvdsc-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns basic information about a user account, user name, user full name, user description, and user ID. You must manually select the polymorphic instance to use. Use the pull-down menu to select an instance of this VI. icon Inputs/Outputs ccclst.png domain domain is the domain principal to which t

### NI Security Get User Info (ID)(Principal) VI

Returns basic information about a user account, user name, user full name, user description, and user ID. You must manually select the polymorphic instance to use.

Use the pull-down menu to select an instance of this VI.

[IMAGE alt='icon' src='ni-security-get-user-info-id-principal-vi.png']

#### Inputs/Outputs

| domain — domain is the domain principal to which to connect. machine — machine is the name of the computer where the domain is located. name — name is the name of the domain. ID — ID is the unique identifier of the domain. b0 — b1 — b2 — b3 — b4 — b5 — b6 — b7 — b8 — b9 — b10 — b11 — b12 — b13 — b14 — b15 — user — user is the unique identifier of the user. This VI returns basic information of this user. b0 — b1 — b2 — b3 — b4 — b5 — b6 — b7 — b8 — b9 — b10 — b11 — b12 — b13 — b14 — b15 — timeout (30 s) — timeout limits the time that this VI waits for the information to return from the domain. The default is 30 seconds. error in (no error) — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. user principal — user principal is the basic information about the currently logged in user. principal type — principal type returns whether the specified domain account is a group or user account. principal name — principal name returns the name of the user or group account. description — description returns the description of the user or group account. fullname — fullname returns the full name for the user or group account. ID — ID returns the unique identifier of the user or group account. b0 — b1 — b2 — b3 — b4 — b5 — b6 — b7 — b8 — b9 — b10 — b11 — b12 — b13 — b14 — b15 — error out — error out contains error information. This output provides standard error out functionality. |
| --- |
| machine — machine is the name of the computer where the domain is located. name — name is the name of the domain. ID — ID is the unique identifier of the domain. b0 — b1 — b2 — b3 — b4 — b5 — b6 — b7 — b8 — b9 — b10 — b11 — b12 — b13 — b14 — b15 — |
| b0 — b1 — b2 — b3 — b4 — b5 — b6 — b7 — b8 — b9 — b10 — b11 — b12 — b13 — b14 — b15 — |
| b0 — b1 — b2 — b3 — b4 — b5 — b6 — b7 — b8 — b9 — b10 — b11 — b12 — b13 — b14 — b15 — |
| principal type — principal type returns whether the specified domain account is a group or user account. principal name — principal name returns the name of the user or group account. description — description returns the description of the user or group account. fullname — fullname returns the full name for the user or group account. ID — ID returns the unique identifier of the user or group account. b0 — b1 — b2 — b3 — b4 — b5 — b6 — b7 — b8 — b9 — b10 — b11 — b12 — b13 — b14 — b15 — |
| b0 — b1 — b2 — b3 — b4 — b5 — b6 — b7 — b8 — b9 — b10 — b11 — b12 — b13 — b14 — b15 — |

Parent topic:

NI Security Get User Info VI

<!--NI_TOPIC bundle=lvdsc-api-ref path=vi-lib/lvdsc/security/ni-security-get-user-info-name-id-vi.html language=enus -->
## TOPIC 00025: NI Security Get User Info (Name)(ID) VI

- bundle_id: `lvdsc-api-ref`
- source_path: `vi-lib/lvdsc/security/ni-security-get-user-info-name-id-vi.html`
- source_url: https://docs-be.ni.com/bundle/lvdsc-api-ref/raw/resource/enus/vi-lib/lvdsc/security/ni-security-get-user-info-name-id-vi.html
- document_id: `lvdsc-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns basic information about a user account, user name, user full name, user description, and user ID. You must manually select the polymorphic instance to use. Use the pull-down menu to select an instance of this VI. icon Inputs/Outputs cnclst.png domain domain is the unique identifier of the do

### NI Security Get User Info (Name)(ID) VI

Returns basic information about a user account, user name, user full name, user description, and user ID. You must manually select the polymorphic instance to use.

Use the pull-down menu to select an instance of this VI.

[IMAGE alt='icon' src='ni-security-get-user-info-name-id-vi.png']

#### Inputs/Outputs

| domain — domain is the unique identifier of the domain to connect to. b0 — b1 — b2 — b3 — b4 — b5 — b6 — b7 — b8 — b9 — b10 — b11 — b12 — b13 — b14 — b15 — user — user is the name of the user. timeout (30 s) — timeout limits the time that this VI waits for the information to return from the domain. The default is 30 seconds. error in (no error) — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. user principal — user principal is the basic information about the currently logged in user. principal type — principal type returns whether the specified domain account is a group or user account. principal name — principal name returns the name of the user or group account. description — description returns the description of the user or group account. fullname — fullname returns the full name for the user or group account. ID — ID returns the unique identifier of the user or group account. b0 — b1 — b2 — b3 — b4 — b5 — b6 — b7 — b8 — b9 — b10 — b11 — b12 — b13 — b14 — b15 — error out — error out contains error information. This output provides standard error out functionality. |
| --- |
| b0 — b1 — b2 — b3 — b4 — b5 — b6 — b7 — b8 — b9 — b10 — b11 — b12 — b13 — b14 — b15 — |
| principal type — principal type returns whether the specified domain account is a group or user account. principal name — principal name returns the name of the user or group account. description — description returns the description of the user or group account. fullname — fullname returns the full name for the user or group account. ID — ID returns the unique identifier of the user or group account. b0 — b1 — b2 — b3 — b4 — b5 — b6 — b7 — b8 — b9 — b10 — b11 — b12 — b13 — b14 — b15 — |
| b0 — b1 — b2 — b3 — b4 — b5 — b6 — b7 — b8 — b9 — b10 — b11 — b12 — b13 — b14 — b15 — |

Parent topic:

NI Security Get User Info VI

<!--NI_TOPIC bundle=lvdsc-api-ref path=vi-lib/lvdsc/security/ni-security-get-user-info-name-name-vi.html language=enus -->
## TOPIC 00026: NI Security Get User Info (Name)(Name) VI

- bundle_id: `lvdsc-api-ref`
- source_path: `vi-lib/lvdsc/security/ni-security-get-user-info-name-name-vi.html`
- source_url: https://docs-be.ni.com/bundle/lvdsc-api-ref/raw/resource/enus/vi-lib/lvdsc/security/ni-security-get-user-info-name-name-vi.html
- document_id: `lvdsc-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns basic information about a user account, user name, user full name, user description, and user ID. You must manually select the polymorphic instance to use. Use the pull-down menu to select an instance of this VI. icon Inputs/Outputs cstr.png domain machine domain machine is the name of the c

### NI Security Get User Info (Name)(Name) VI

Returns basic information about a user account, user name, user full name, user description, and user ID. You must manually select the polymorphic instance to use.

Use the pull-down menu to select an instance of this VI.

[IMAGE alt='icon' src='ni-security-get-user-info-name-name-vi.png']

#### Inputs/Outputs

| domain machine — domain machine is the name of the computer where the domain is located. The default is localhost. domain name — domain name is the name of the domain that contains the groups and users that you want to modify. user — user is the name of the user. timeout (30 s) — timeout limits the time that this VI waits for the information to return from the domain. The default is 30 seconds. error in (no error) — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. user principal — user principal is the basic information about the currently logged in user. principal type — principal type returns whether the specified domain account is a group or user account. principal name — principal name returns the name of the user or group account. description — description returns the description of the user or group account. fullname — fullname returns the full name for the user or group account. ID — ID returns the unique identifier of the user or group account. b0 — b1 — b2 — b3 — b4 — b5 — b6 — b7 — b8 — b9 — b10 — b11 — b12 — b13 — b14 — b15 — error out — error out contains error information. This output provides standard error out functionality. |
| --- |
| principal type — principal type returns whether the specified domain account is a group or user account. principal name — principal name returns the name of the user or group account. description — description returns the description of the user or group account. fullname — fullname returns the full name for the user or group account. ID — ID returns the unique identifier of the user or group account. b0 — b1 — b2 — b3 — b4 — b5 — b6 — b7 — b8 — b9 — b10 — b11 — b12 — b13 — b14 — b15 — |
| b0 — b1 — b2 — b3 — b4 — b5 — b6 — b7 — b8 — b9 — b10 — b11 — b12 — b13 — b14 — b15 — |

Parent topic:

NI Security Get User Info VI

<!--NI_TOPIC bundle=lvdsc-api-ref path=vi-lib/lvdsc/security/ni-security-get-user-list-id-vi.html language=enus -->
## TOPIC 00027: NI Security Get User List (ID) VI

- bundle_id: `lvdsc-api-ref`
- source_path: `vi-lib/lvdsc/security/ni-security-get-user-list-id-vi.html`
- source_url: https://docs-be.ni.com/bundle/lvdsc-api-ref/raw/resource/enus/vi-lib/lvdsc/security/ni-security-get-user-list-id-vi.html
- document_id: `lvdsc-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns a list of users available on a specific domain. You must manually select the polymorphic instance to use. Use the pull-down menu to select an instance of this VI. icon Inputs/Outputs cnclst.png domain domain is the unique identifier of the domain to connect to. cu8.png b0 cu8.png b1 cu8.png

### NI Security Get User List (ID) VI

Returns a list of users available on a specific domain. You must manually select the polymorphic instance to use.

Use the pull-down menu to select an instance of this VI.

[IMAGE alt='icon' src='ni-security-get-user-list-id-vi.png']

#### Inputs/Outputs

| domain — domain is the unique identifier of the domain to connect to. b0 — b1 — b2 — b3 — b4 — b5 — b6 — b7 — b8 — b9 — b10 — b11 — b12 — b13 — b14 — b15 — timeout (30 s) — timeout limits the time that this VI waits for the information to return from the domain. The default is 30 seconds. error in (no error) — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. user principals — user principals is a list of the user accounts available from the specified domain. principal type — principal type returns whether the specified domain account is a group or user account. principal name — principal name returns the name of the user or group account. description — description returns the description of the user or group account. fullname — fullname returns the full name for the user or group account. ID — ID returns the unique identifier of the user or group account. b0 — b1 — b2 — b3 — b4 — b5 — b6 — b7 — b8 — b9 — b10 — b11 — b12 — b13 — b14 — b15 — error out — error out contains error information. This output provides standard error out functionality. |
| --- |
| b0 — b1 — b2 — b3 — b4 — b5 — b6 — b7 — b8 — b9 — b10 — b11 — b12 — b13 — b14 — b15 — |
| principal type — principal type returns whether the specified domain account is a group or user account. principal name — principal name returns the name of the user or group account. description — description returns the description of the user or group account. fullname — fullname returns the full name for the user or group account. ID — ID returns the unique identifier of the user or group account. b0 — b1 — b2 — b3 — b4 — b5 — b6 — b7 — b8 — b9 — b10 — b11 — b12 — b13 — b14 — b15 — |
| b0 — b1 — b2 — b3 — b4 — b5 — b6 — b7 — b8 — b9 — b10 — b11 — b12 — b13 — b14 — b15 — |

Parent topic:

NI Security Get User List VI

<!--NI_TOPIC bundle=lvdsc-api-ref path=vi-lib/lvdsc/security/ni-security-get-user-list-name-vi.html language=enus -->
## TOPIC 00028: NI Security Get User List (Name) VI

- bundle_id: `lvdsc-api-ref`
- source_path: `vi-lib/lvdsc/security/ni-security-get-user-list-name-vi.html`
- source_url: https://docs-be.ni.com/bundle/lvdsc-api-ref/raw/resource/enus/vi-lib/lvdsc/security/ni-security-get-user-list-name-vi.html
- document_id: `lvdsc-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns a list of users available on a specific domain. You must manually select the polymorphic instance to use. Use the pull-down menu to select an instance of this VI. icon Inputs/Outputs cstr.png domain machine domain machine is the name of the computer where the domain is located. The default i

### NI Security Get User List (Name) VI

Returns a list of users available on a specific domain. You must manually select the polymorphic instance to use.

Use the pull-down menu to select an instance of this VI.

[IMAGE alt='icon' src='ni-security-get-user-list-name-vi.png']

#### Inputs/Outputs

| domain machine — domain machine is the name of the computer where the domain is located. The default is localhost. domain name — domain name is the name of the domain that contains the groups and users that you want to modify. timeout (30 s) — timeout limits the time that this VI waits for the information to return from the domain. The default is 30 seconds. error in (no error) — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. user principals — user principals is a list of the user accounts available from the specified domain. principal type — principal type returns whether the specified domain account is a group or user account. principal name — principal name returns the name of the user or group account. description — description returns the description of the user or group account. fullname — fullname returns the full name for the user or group account. ID — ID returns the unique identifier of the user or group account. b0 — b1 — b2 — b3 — b4 — b5 — b6 — b7 — b8 — b9 — b10 — b11 — b12 — b13 — b14 — b15 — error out — error out contains error information. This output provides standard error out functionality. |
| --- |
| principal type — principal type returns whether the specified domain account is a group or user account. principal name — principal name returns the name of the user or group account. description — description returns the description of the user or group account. fullname — fullname returns the full name for the user or group account. ID — ID returns the unique identifier of the user or group account. b0 — b1 — b2 — b3 — b4 — b5 — b6 — b7 — b8 — b9 — b10 — b11 — b12 — b13 — b14 — b15 — |
| b0 — b1 — b2 — b3 — b4 — b5 — b6 — b7 — b8 — b9 — b10 — b11 — b12 — b13 — b14 — b15 — |

Parent topic:

NI Security Get User List VI

<!--NI_TOPIC bundle=lvdsc-api-ref path=vi-lib/lvdsc/tagapi/classes/tag-reader/public-api/close-tag-reader-vi.html language=enus -->
## TOPIC 00029: Close Tag Reader.vi

- bundle_id: `lvdsc-api-ref`
- source_path: `vi-lib/lvdsc/tagapi/classes/tag-reader/public-api/close-tag-reader-vi.html`
- source_url: https://docs-be.ni.com/bundle/lvdsc-api-ref/raw/resource/enus/vi-lib/lvdsc/tagapi/classes/tag-reader/public-api/close-tag-reader-vi.html
- document_id: `lvdsc-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Closes a Tag Reader instance and releases all resources that LabVIEW allocates to the instance. This VI closes the specified Tag Reader instance regardless of whether an error occurred in a preceding operation. icon Inputs/Outputs cTag_Readerlvclass.png Tag Reader in specifies the data of a group of

### Close Tag Reader.vi

Closes a Tag Reader instance and releases all resources that LabVIEW allocates to the instance. This VI closes the specified Tag Reader instance regardless of whether an error occurred in a preceding operation.

[IMAGE alt='icon' src='close-tag-reader-vi.png']

#### Inputs/Outputs

| — Tag Reader in specifies the data of a group of tags that the Open Tag Reader VI opens. error in (no error) — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. error out — error out contains error information. This output provides standard error out functionality. |
| --- |

Parent topic:

Tags

<!--NI_TOPIC bundle=lvdsc-api-ref path=vi-lib/lvdsc/tagapi/classes/tag-reader/public-api/get-published-tag-names-vi.html language=enus -->
## TOPIC 00030: Get Published Tag Names.vi

- bundle_id: `lvdsc-api-ref`
- source_path: `vi-lib/lvdsc/tagapi/classes/tag-reader/public-api/get-published-tag-names-vi.html`
- source_url: https://docs-be.ni.com/bundle/lvdsc-api-ref/raw/resource/enus/vi-lib/lvdsc/tagapi/classes/tag-reader/public-api/get-published-tag-names-vi.html
- document_id: `lvdsc-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns a list of tags and processes that exist under the root URL of a Tag Reader instance. This VI returns tags and processes with a path separator that matches the path separator of the Tag Reader instance only. Use the Get Path Separator VI to get the path separator. Use the Open Tag Reader and

### Get Published Tag Names.vi

Returns a list of tags and processes that exist under the root URL of a Tag Reader instance.

This VI returns tags and processes with a path separator that matches the path separator of the Tag Reader instance only. Use the [Get Path Separator](utility/get-path-separator-vi.html) VI to get the path separator. Use the [Open Tag Reader](open-tag-reader-vi.html) and [Redirect Tag Reader](redirect-root-url-vi.html) VIs to change the **tag names** and **process names**.

[IMAGE alt='icon' src='get-published-tag-names-vi.png']

#### Inputs/Outputs

| — Tag Reader in specifies the data of a group of tags that the Open Tag Reader VI opens. error in (no error) — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. — Tag Reader out returns the value of the Tag Reader instance. tag names — tag names returns a list of tag names that the Tag Reader instance contains. process names — process names returns a list of processes that the Tag Reader instance contains. error out — error out contains error information. This output provides standard error out functionality. |
| --- |

Parent topic:

Utility

<!--NI_TOPIC bundle=lvdsc-api-ref path=vi-lib/lvdsc/tagapi/classes/tag-reader/public-api/open-tag-reader-vi.html language=enus -->
## TOPIC 00031: Open Tag Reader.vi

- bundle_id: `lvdsc-api-ref`
- source_path: `vi-lib/lvdsc/tagapi/classes/tag-reader/public-api/open-tag-reader-vi.html`
- source_url: https://docs-be.ni.com/bundle/lvdsc-api-ref/raw/resource/enus/vi-lib/lvdsc/tagapi/classes/tag-reader/public-api/open-tag-reader-vi.html
- document_id: `lvdsc-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Creates new tags for the shared variables and I/O server data items under a root URL. This VI returns a Tag Reader instance that contains all these tags. Use the Tag Reader instance to perform other tag-related operations, such as reading and writing values, accessing historical data, and reading me

### Open Tag Reader.vi

Creates new tags for the shared variables and I/O server data items under a **root URL**. This VI returns a Tag Reader instance that contains all these tags. Use the Tag Reader instance to perform other tag-related operations, such as reading and writing values, accessing historical data, and reading meta information.

You can redirect the Tag Reader instance to a new root URL by using the [Redirect Root URL](redirect-root-url-vi.html) VI.

[IMAGE alt='icon' src='open-tag-reader-vi.png']

#### Inputs/Outputs

| root URL — root URL specifies the root URL of the group of shared variables that you want to open. This VI opens all the shared variables under the root URL. The format of root URL is \\\\computer\\process\\shared_variable. This format contains three levels. You can specify the root URL to any level. The Tags VIs combine the root URL, path separator, and tag name to resolve the full tag URL. Note Ensure that the shared_variable does not contain backslashes (\\). error in (no error) — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. path separator — path separator specifies the path separator for the root URL. The default is \\. Note Ensure that the path separator does not contain single quotes ('). — Tag Reader out returns data of the tags that this VI opens. error out — error out contains error information. This output provides standard error out functionality. |
| --- |

Parent topic:

Tags

<!--NI_TOPIC bundle=lvdsc-api-ref path=vi-lib/lvdsc/tagapi/classes/tag-reader/public-api/read-current-tag-trace-as-trend-vi.html language=enus -->
## TOPIC 00032: Read Current Tag Trace as Trend.vi

- bundle_id: `lvdsc-api-ref`
- source_path: `vi-lib/lvdsc/tagapi/classes/tag-reader/public-api/read-current-tag-trace-as-trend-vi.html`
- source_url: https://docs-be.ni.com/bundle/lvdsc-api-ref/raw/resource/enus/vi-lib/lvdsc/tagapi/classes/tag-reader/public-api/read-current-tag-trace-as-trend-vi.html
- document_id: `lvdsc-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Reads the current trend of a tag in waveform format. You must manually select the polymorphic instance to use. This VI interacts with data in the Citadel database only. Use the pull-down menu to select an instance of this VI. icon

### Read Current Tag Trace as Trend.vi

Reads the current trend of a tag in waveform format. You must manually select the polymorphic instance to use.

Note

Use the pull-down menu to select an instance of this VI.

[IMAGE alt='icon' src='read-current-tag-trace-as-trend-vi.png']

- [Read Current Tag Trace as Trend (Single, Double) VI](../../../../../../vi-lib/lvdsc/tagapi/classes/tag-reader/read-current-tag-trace-as-trend/read-current-tag-trace-as-trend-single-double-vi.html) Reads the current trend of a tag in waveform format. You must manually select the polymorphic instance to use.
- [Read Current Tag Trace as Trend (Single, Boolean) VI](../../../../../../vi-lib/lvdsc/tagapi/classes/tag-reader/read-current-tag-trace-as-trend/read-current-tag-trace-as-trend-single-boolean-vi.html) Reads the current trend of a tag in waveform format. You must manually select the polymorphic instance to use.
- [Read Current Tag Trace as Trend (Single, UInt32) VI](../../../../../../vi-lib/lvdsc/tagapi/classes/tag-reader/read-current-tag-trace-as-trend/read-current-tag-trace-as-trend-single-uint32-vi.html) Reads the current trend of a tag in waveform format. You must manually select the polymorphic instance to use.
- [Read Current Tag Trace as Trend (Multiple, Double) VI](../../../../../../vi-lib/lvdsc/tagapi/classes/tag-reader/read-current-tag-trace-as-trend-multiple/read-current-tag-trace-as-trend-multiple-double-vi.html) Reads the current trend of a tag in waveform format. You must manually select the polymorphic instance to use.
- [Read Current Tag Trace as Trend (Multiple, Boolean) VI](../../../../../../vi-lib/lvdsc/tagapi/classes/tag-reader/read-current-tag-trace-as-trend-multiple/read-current-tag-trace-as-trend-multiple-boolean-vi.html) Reads the current trend of a tag in waveform format. You must manually select the polymorphic instance to use.
- [Read Current Tag Trace as Trend (Multiple, UInt32) VI](../../../../../../vi-lib/lvdsc/tagapi/classes/tag-reader/read-current-tag-trace-as-trend-multiple/read-current-tag-trace-as-trend-multiple-uint32-vi.html) Reads the current trend of a tag in waveform format. You must manually select the polymorphic instance to use.

Parent topic:

Tags

<!--NI_TOPIC bundle=lvdsc-api-ref path=vi-lib/lvdsc/tagapi/classes/tag-reader/public-api/read-tag-alarms-vi.html language=enus -->
## TOPIC 00033: Read Tag Alarms.vi

- bundle_id: `lvdsc-api-ref`
- source_path: `vi-lib/lvdsc/tagapi/classes/tag-reader/public-api/read-tag-alarms-vi.html`
- source_url: https://docs-be.ni.com/bundle/lvdsc-api-ref/raw/resource/enus/vi-lib/lvdsc/tagapi/classes/tag-reader/public-api/read-tag-alarms-vi.html
- document_id: `lvdsc-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Reads alarms for the specified tags, processes, or alarm areas. You must manually select the polymorphic instance to use. This VI interacts with data in the Citadel database only. Use the pull-down menu to select an instance of this VI. icon

### Read Tag Alarms.vi

Reads alarms for the specified tags, processes, or alarm areas. You must manually select the polymorphic instance to use.

Note

Use the pull-down menu to select an instance of this VI.

[IMAGE alt='icon' src='read-tag-alarms-vi.png']

- [Read Tag Alarms (Live, Single) VI](../../../../../../vi-lib/lvdsc/tagapi/classes/tag-reader/read-tag-alarms/read-tag-alarms-live-single-vi.html) Reads alarms for the specified tags, processes, or alarm areas. You must manually select the polymorphic instance to use.
- [Read Tag Alarms (Live, Multiple) VI](../../../../../../vi-lib/lvdsc/tagapi/classes/tag-reader/read-tag-alarms/read-tag-alarms-live-multiple-vi.html) Reads alarms for the specified tags, processes, or alarm areas. You must manually select the polymorphic instance to use.
- [Read Tag Alarms (Live, All in Process) VI](../../../../../../vi-lib/lvdsc/tagapi/classes/tag-reader/read-tag-alarms/read-tag-alarms-live-all-in-process-vi.html) Reads alarms for the specified tags, processes, or alarm areas. You must manually select the polymorphic instance to use.
- [Read Tag Alarms (Historical, Tag Name) VI](../../../../../../vi-lib/lvdsc/tagapi/classes/tag-reader/read-tag-alarms/read-tag-alarms-historical-tag-name-vi.html) Reads alarms for the specified tags, processes, or alarm areas. You must manually select the polymorphic instance to use.
- [Read Tag Alarms (Historical, Area) VI](../../../../../../vi-lib/lvdsc/tagapi/classes/tag-reader/read-tag-alarms/read-tag-alarms-historical-area-vi.html) Reads alarms for the specified tags, processes, or alarm areas. You must manually select the polymorphic instance to use.

Parent topic:

Tags

<!--NI_TOPIC bundle=lvdsc-api-ref path=vi-lib/lvdsc/tagapi/classes/tag-reader/public-api/read-tag-trace-vi.html language=enus -->
## TOPIC 00034: Read Tag Trace.vi

- bundle_id: `lvdsc-api-ref`
- source_path: `vi-lib/lvdsc/tagapi/classes/tag-reader/public-api/read-tag-trace-vi.html`
- source_url: https://docs-be.ni.com/bundle/lvdsc-api-ref/raw/resource/enus/vi-lib/lvdsc/tagapi/classes/tag-reader/public-api/read-tag-trace-vi.html
- document_id: `lvdsc-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Reads the historical trace of a tag. You must manually select the polymorphic instance to use. This VI interacts with data in the Citadel database only. Use the pull-down menu to select an instance of this VI. icon

### Read Tag Trace.vi

Reads the historical trace of a tag. You must manually select the polymorphic instance to use.

Note

Use the pull-down menu to select an instance of this VI.

[IMAGE alt='icon' src='read-tag-trace-vi.png']

- [Read Tag Trace (Double) VI](../../../../../../vi-lib/lvdsc/tagapi/classes/tag-reader/read-tag-trace/read-tag-trace-double-vi.html) Reads the historical trace of a tag. You must manually select the polymorphic instance to use.
- [Read Tag Trace (Boolean) VI](../../../../../../vi-lib/lvdsc/tagapi/classes/tag-reader/read-tag-trace/read-tag-trace-boolean-vi.html) Reads the historical trace of a tag. You must manually select the polymorphic instance to use.
- [Read Tag Trace (String) VI](../../../../../../vi-lib/lvdsc/tagapi/classes/tag-reader/read-tag-trace/read-tag-trace-string-vi.html) Reads the historical trace of a tag. You must manually select the polymorphic instance to use.
- [Read Tag Trace (UInt32) VI](../../../../../../vi-lib/lvdsc/tagapi/classes/tag-reader/read-tag-trace/read-tag-trace-uint32-vi.html) Reads the historical trace of a tag. You must manually select the polymorphic instance to use.
- [Read Tag Trace (Variant) VI](../../../../../../vi-lib/lvdsc/tagapi/classes/tag-reader/read-tag-trace/read-tag-trace-variant-vi.html) Reads the historical trace of a tag. You must manually select the polymorphic instance to use.

Parent topic:

Tags

<!--NI_TOPIC bundle=lvdsc-api-ref path=vi-lib/lvdsc/tagapi/classes/tag-reader/public-api/read-tag-vi.html language=enus -->
## TOPIC 00035: Read Tag.vi

- bundle_id: `lvdsc-api-ref`
- source_path: `vi-lib/lvdsc/tagapi/classes/tag-reader/public-api/read-tag-vi.html`
- source_url: https://docs-be.ni.com/bundle/lvdsc-api-ref/raw/resource/enus/vi-lib/lvdsc/tagapi/classes/tag-reader/public-api/read-tag-vi.html
- document_id: `lvdsc-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Reads the value of specified tags. You must manually select the polymorphic instance to use. Use the pull-down menu to select an instance of this VI. icon

### Read Tag.vi

Reads the value of specified tags. You must manually select the polymorphic instance to use.

Use the pull-down menu to select an instance of this VI.

[IMAGE alt='icon' src='read-tag-vi.png']

- [Read Tag (Single, Double) VI](../../../../../../vi-lib/lvdsc/tagapi/classes/tag-reader/read-tag/read-tag-single-double-vi.html) Reads the value of specified tags. You must manually select the polymorphic instance to use.
- [Read Tag (Single, Boolean) VI](../../../../../../vi-lib/lvdsc/tagapi/classes/tag-reader/read-tag/read-tag-single-boolean-vi.html) Reads the value of specified tags. You must manually select the polymorphic instance to use.
- [Read Tag (Single, UInt32) VI](../../../../../../vi-lib/lvdsc/tagapi/classes/tag-reader/read-tag/read-tag-single-uint32-vi.html) Reads the value of specified tags. You must manually select the polymorphic instance to use.
- [Read Tag (Single, String) VI](../../../../../../vi-lib/lvdsc/tagapi/classes/tag-reader/read-tag/read-tag-single-string-vi.html) Reads the value of specified tags. You must manually select the polymorphic instance to use.
- [Read Tag (Single, Variant) VI](../../../../../../vi-lib/lvdsc/tagapi/classes/tag-reader/read-tag/read-tag-single-variant-vi.html) Reads the value of specified tags. You must manually select the polymorphic instance to use.
- [Read Tag (Multiple, Double) VI](../../../../../../vi-lib/lvdsc/tagapi/classes/tag-reader/read-tag-multiple/read-tag-multiple-double-vi.html) Reads the value of specified tags. You must manually select the polymorphic instance to use.
- [Read Tag (Multiple, Boolean) VI](../../../../../../vi-lib/lvdsc/tagapi/classes/tag-reader/read-tag-multiple/read-tag-multiple-boolean-vi.html) Reads the value of specified tags. You must manually select the polymorphic instance to use.
- [Read Tag (Multiple, String) VI](../../../../../../vi-lib/lvdsc/tagapi/classes/tag-reader/read-tag-multiple/read-tag-multiple-string-vi.html) Reads the value of specified tags. You must manually select the polymorphic instance to use.
- [Read Tag (Multiple, UInt32) VI](../../../../../../vi-lib/lvdsc/tagapi/classes/tag-reader/read-tag-multiple/read-tag-multiple-uint32-vi.html) Reads the value of specified tags. You must manually select the polymorphic instance to use.
- [Read Tag (Multiple, Variant) VI](../../../../../../vi-lib/lvdsc/tagapi/classes/tag-reader/read-tag-multiple/read-tag-multiple-variant-vi.html) Reads the value of specified tags. You must manually select the polymorphic instance to use.

Parent topic:

Tags

<!--NI_TOPIC bundle=lvdsc-api-ref path=vi-lib/lvdsc/tagapi/classes/tag-reader/public-api/utility/configure-front-panel-binding-vi.html language=enus -->
## TOPIC 00036: Configure Front Panel Binding.vi

- bundle_id: `lvdsc-api-ref`
- source_path: `vi-lib/lvdsc/tagapi/classes/tag-reader/public-api/utility/configure-front-panel-binding-vi.html`
- source_url: https://docs-be.ni.com/bundle/lvdsc-api-ref/raw/resource/enus/vi-lib/lvdsc/tagapi/classes/tag-reader/public-api/utility/configure-front-panel-binding-vi.html
- document_id: `lvdsc-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Configures an existing binding between a front panel object and a shared variable through the corresponding tag of the shared variable. You can specify a front panel control or indicator by using the control reference. This VI resolves the corresponding shared variable for a tag and configures the f

### Configure Front Panel Binding.vi

Configures an existing binding between a front panel object and a shared variable through the corresponding tag of the shared variable. You can specify a front panel control or indicator by using the **control reference**. This VI resolves the corresponding shared variable for a tag and configures the front panel binding for that shared variable.

To use this VI, you must bind this front panel object to a shared variable.

[IMAGE alt='icon' src='configure-front-panel-binding-vi.png']

#### Inputs/Outputs

| control reference — control reference specifies the reference number associated with the object for which you want to configure the front panel binding. Create a control reference before you use this VI. — Tag Reader in specifies the data of a group of tags that the Open Tag Reader VI opens. tag name (default: auto) — tag name specifies the name of the tag for which you want to bind to the front panel object. The default is the label text of the front panel object. error in (no error) — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. show LED? (T) — show LED? specifies whether to show or hide the data binding indicator. The default is TRUE. — Tag Reader out returns the value of the Tag Reader instance. error out — error out contains error information. This output provides standard error out functionality. |
| --- |

Parent topic:

Utility

<!--NI_TOPIC bundle=lvdsc-api-ref path=vi-lib/lvdsc/tagapi/classes/tag-reader/public-api/utility/get-root-url-vi.html language=enus -->
## TOPIC 00037: Get Root URL.vi

- bundle_id: `lvdsc-api-ref`
- source_path: `vi-lib/lvdsc/tagapi/classes/tag-reader/public-api/utility/get-root-url-vi.html`
- source_url: https://docs-be.ni.com/bundle/lvdsc-api-ref/raw/resource/enus/vi-lib/lvdsc/tagapi/classes/tag-reader/public-api/utility/get-root-url-vi.html
- document_id: `lvdsc-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the root URL for a Tag Reader instance. You can change the root URL by using the Redirect Root URL VI. icon Inputs/Outputs cTag_Readerlvclass.png Tag Reader in specifies the data of a group of tags that the Open Tag Reader VI opens. cerrcodeclst.png error in (no error) error in describes err

### Get Root URL.vi

Returns the root URL for a Tag Reader instance. You can change the root URL by using the Redirect Root URL VI.

[IMAGE alt='icon' src='get-root-url-vi.png']

#### Inputs/Outputs

| — Tag Reader in specifies the data of a group of tags that the Open Tag Reader VI opens. error in (no error) — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. — Tag Reader out returns the value of the Tag Reader instance. root URL — root URL returns the root URL of the specified Tag Reader instance. error out — error out contains error information. This output provides standard error out functionality. |
| --- |

Parent topic:

Utility

<!--NI_TOPIC bundle=lvdsc-api-ref path=vi-lib/lvdsc/tagapi/classes/tag-reader/public-api/utility/get-variable-url-vi.html language=enus -->
## TOPIC 00038: Get Variable URL.vi

- bundle_id: `lvdsc-api-ref`
- source_path: `vi-lib/lvdsc/tagapi/classes/tag-reader/public-api/utility/get-variable-url-vi.html`
- source_url: https://docs-be.ni.com/bundle/lvdsc-api-ref/raw/resource/enus/vi-lib/lvdsc/tagapi/classes/tag-reader/public-api/utility/get-variable-url-vi.html
- document_id: `lvdsc-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the NI Publish-Subscribe Protocol (NI-PSP) URL of a tag. icon Inputs/Outputs cTag_Readerlvclass.png Tag Reader in specifies the data of a group of tags that the Open Tag Reader VI opens. cstr.png tag name tag name specifies the name of the tag for which you want to get the NI-PSP URL. cerrco

### Get Variable URL.vi

Returns the NI Publish-Subscribe Protocol (NI-PSP) URL of a tag.

[IMAGE alt='icon' src='get-variable-url-vi.png']

#### Inputs/Outputs

| — Tag Reader in specifies the data of a group of tags that the Open Tag Reader VI opens. tag name — tag name specifies the name of the tag for which you want to get the NI-PSP URL. error in (no error) — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. — Tag Reader out returns the value of the Tag Reader instance. shared variable URL — shared variable URL returns the NI-PSP URL for the specified tag. error out — error out contains error information. This output provides standard error out functionality. |
| --- |

Parent topic:

Utility

<!--NI_TOPIC bundle=lvdsc-api-ref path=vi-lib/lvdsc/tagapi/classes/tag-reader/public-api/utility/not-a-valid-tag-reader-vi.html language=enus -->
## TOPIC 00039: Not a Valid Tag Reader.vi

- bundle_id: `lvdsc-api-ref`
- source_path: `vi-lib/lvdsc/tagapi/classes/tag-reader/public-api/utility/not-a-valid-tag-reader-vi.html`
- source_url: https://docs-be.ni.com/bundle/lvdsc-api-ref/raw/resource/enus/vi-lib/lvdsc/tagapi/classes/tag-reader/public-api/utility/not-a-valid-tag-reader-vi.html
- document_id: `lvdsc-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Determines whether a Tag Reader instance is valid. A Tag Reader instance is valid until you close it by using the Close Tag Reader VI. This VI returns TRUE if the specified Tag Reader instance is not valid. icon Inputs/Outputs cTag_Readerlvclass.png Tag Reader in specifies the data of a group of tag

### Not a Valid Tag Reader.vi

Determines whether a Tag Reader instance is valid. A Tag Reader instance is valid until you close it by using the Close Tag Reader VI. This VI returns TRUE if the specified Tag Reader instance is not valid.

[IMAGE alt='icon' src='not-a-valid-tag-reader-vi.png']

#### Inputs/Outputs

| — Tag Reader in specifies the data of a group of tags that the Open Tag Reader VI opens. not a valid Tag Reader? — not a valid Tag Reader? returns TRUE if the specified Tag Reader instance is not valid. |
| --- |

Parent topic:

Utility

<!--NI_TOPIC bundle=lvdsc-api-ref path=vi-lib/lvdsc/tagapi/classes/tag-reader/public-api/write-tag-vi.html language=enus -->
## TOPIC 00040: Write Tag.vi

- bundle_id: `lvdsc-api-ref`
- source_path: `vi-lib/lvdsc/tagapi/classes/tag-reader/public-api/write-tag-vi.html`
- source_url: https://docs-be.ni.com/bundle/lvdsc-api-ref/raw/resource/enus/vi-lib/lvdsc/tagapi/classes/tag-reader/public-api/write-tag-vi.html
- document_id: `lvdsc-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Writes data to the value of a tag. Use the Read Tag VI to read the value of a tag. Wire data to the data input to determine the polymorphic instance to use or manually select the instance. Use the pull-down menu to select an instance of this VI. icon

### Write Tag.vi

Writes data to the value of a tag. Use the Read Tag VI to read the value of a tag. Wire data to the **data** input to determine the polymorphic instance to use or manually select the instance.

Use the pull-down menu to select an instance of this VI.

[IMAGE alt='icon' src='write-tag-vi.png']

- [Write Tag (Double) VI](../../../../../../vi-lib/lvdsc/tagapi/classes/tag-reader/write-tag/write-tag-double-vi.html) Writes data to the value of a tag. Use the Read Tag VI to read the value of a tag. Wire data to the data input to determine the polymorphic instance to use or manually select the instance.
- [Write Tag (Boolean) VI](../../../../../../vi-lib/lvdsc/tagapi/classes/tag-reader/write-tag/write-tag-boolean-vi.html) Writes data to the value of a tag. Use the Read Tag VI to read the value of a tag. Wire data to the data input to determine the polymorphic instance to use or manually select the instance.
- [Write Tag (String) VI](../../../../../../vi-lib/lvdsc/tagapi/classes/tag-reader/write-tag/write-tag-string-vi.html) Writes data to the value of a tag. Use the Read Tag VI to read the value of a tag. Wire data to the data input to determine the polymorphic instance to use or manually select the instance.
- [Write Tag (UInt32) VI](../../../../../../vi-lib/lvdsc/tagapi/classes/tag-reader/write-tag/write-tag-uint32-vi.html) Writes data to the value of a tag. Use the Read Tag VI to read the value of a tag. Wire data to the data input to determine the polymorphic instance to use or manually select the instance.
- [Write Tag (Variant) VI](../../../../../../vi-lib/lvdsc/tagapi/classes/tag-reader/write-tag/write-tag-variant-vi.html) Writes data to the value of a tag. Use the Read Tag VI to read the value of a tag. Wire data to the data input to determine the polymorphic instance to use or manually select the instance.

Parent topic:

Tags

<!--NI_TOPIC bundle=lvdsc-api-ref path=vi-lib/lvdsc/tagapi/classes/tag-reader/read-current-tag-trace-as-trend-multiple/read-current-tag-trace-as-trend-multiple-boolean-vi.html language=enus -->
## TOPIC 00041: Read Current Tag Trace as Trend (Multiple, Boolean) VI

- bundle_id: `lvdsc-api-ref`
- source_path: `vi-lib/lvdsc/tagapi/classes/tag-reader/read-current-tag-trace-as-trend-multiple/read-current-tag-trace-as-trend-multiple-boolean-vi.html`
- source_url: https://docs-be.ni.com/bundle/lvdsc-api-ref/raw/resource/enus/vi-lib/lvdsc/tagapi/classes/tag-reader/read-current-tag-trace-as-trend-multiple/read-current-tag-trace-as-trend-multiple-boolean-vi.html
- document_id: `lvdsc-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Reads the current trend of a tag in waveform format. You must manually select the polymorphic instance to use. This VI interacts with data in the Citadel database only. Use the pull-down menu to select an instance of this VI. icon Inputs/Outputs ci32.png timeout (30 s) timeout specifies the maximum

### Read Current Tag Trace as Trend (Multiple, Boolean) VI

Reads the current trend of a tag in waveform format. You must manually select the polymorphic instance to use.

Note

Use the pull-down menu to select an instance of this VI.

[IMAGE alt='icon' src='read-current-tag-trace-as-trend-multiple-boolean-vi.png']

#### Inputs/Outputs

| timeout (30 s) — timeout specifies the maximum time, in seconds, that this VI waits for reading data from the Citadel database. The default is 30. A timeout value of less than or equal to 0 specifies no timeout, which means this VI waits indefinitely until this VI receives data from the Citadel database. max points per trace (all) — max points per trace specifies the maximum number of points to read from the database. This VI returns all available points of this trace in seconds before now in the following cases: max points per trace is less than zero.The number of the data points in seconds before now is less than the max points per trace. If max points per trace is zero, this VI returns no point for the trace. The default is -1. — Tag Reader in specifies the data of a group of tags that the Open Tag Reader VI opens. tag names — tag names specifies a list of the tags for which you want to read the historical data. seconds before now (60 s) — seconds before now specifies a time interval between the start time and the current time. This VI retrieves the data in this time interval from the database. The default is 60 seconds. error in (no error) — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. database URL — database URL specifies the computer name and the database name where the Citadel database resides. Enter the database URL in the format \\\\computer\\database. interpolation interval (1 s) — interpolation interval specifies the interval, in seconds, at which this VI interpolates the data. The default is 1. — Tag Reader out returns the value of the Tag Reader instance. waveform graph — waveform graph returns a list of waveforms of the historical data of the specified tags. quality — quality returns a list of the data quality of the traces that this VI reads from multiple tags. A value of zero indicates good quality. Refer to the quality output of the DataSocket Read function for detailed descriptions of the quality values. Use the Shared Variable Error from Quality VI to convert this code to an error I/O cluster. error out — error out contains error information. This output provides standard error out functionality. |
| --- |

Parent topic:

Read Current Tag Trace as Trend.vi

<!--NI_TOPIC bundle=lvdsc-api-ref path=vi-lib/lvdsc/tagapi/classes/tag-reader/read-current-tag-trace-as-trend-multiple/read-current-tag-trace-as-trend-multiple-double-vi.html language=enus -->
## TOPIC 00042: Read Current Tag Trace as Trend (Multiple, Double) VI

- bundle_id: `lvdsc-api-ref`
- source_path: `vi-lib/lvdsc/tagapi/classes/tag-reader/read-current-tag-trace-as-trend-multiple/read-current-tag-trace-as-trend-multiple-double-vi.html`
- source_url: https://docs-be.ni.com/bundle/lvdsc-api-ref/raw/resource/enus/vi-lib/lvdsc/tagapi/classes/tag-reader/read-current-tag-trace-as-trend-multiple/read-current-tag-trace-as-trend-multiple-double-vi.html
- document_id: `lvdsc-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Reads the current trend of a tag in waveform format. You must manually select the polymorphic instance to use. This VI interacts with data in the Citadel database only. Use the pull-down menu to select an instance of this VI. icon Inputs/Outputs ci32.png timeout (30 s) timeout specifies the maximum

### Read Current Tag Trace as Trend (Multiple, Double) VI

Reads the current trend of a tag in waveform format. You must manually select the polymorphic instance to use.

Note

Use the pull-down menu to select an instance of this VI.

[IMAGE alt='icon' src='read-current-tag-trace-as-trend-multiple-double-vi.png']

#### Inputs/Outputs

| timeout (30 s) — timeout specifies the maximum time, in seconds, that this VI waits for reading data from the Citadel database. The default is 30. A timeout value of less than or equal to 0 specifies no timeout, which means this VI waits indefinitely until this VI receives data from the Citadel database. max points per trace (all) — max points per trace specifies the maximum number of points to read from the database. This VI returns all available points of this trace in seconds before now in the following cases: max points per trace is less than zero.The number of the data points in seconds before now is less than the max points per trace. If max points per trace is zero, this VI returns no point for the trace. The default is -1. — Tag Reader in specifies the data of a group of tags that the Open Tag Reader VI opens. tag names — tag names specifies a list of the tags for which you want to read the historical data. seconds before now (60 s) — seconds before now specifies a time interval between the start time and the current time. This VI retrieves the data in this time interval from the database. The default is 60 seconds. error in (no error) — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. database URL — database URL specifies the computer name and the database name where the Citadel database resides. Enter the database URL in the format \\\\computer\\database. interpolation interval (1 s) — interpolation interval specifies the interval, in seconds, at which this VI interpolates the data. The default is 1. — Tag Reader out returns the value of the Tag Reader instance. waveform graph — waveform graph returns a list of waveforms of the historical data of the specified tags. quality — quality returns a list of the data quality of the traces that this VI reads from multiple tags. A value of zero indicates good quality. Refer to the quality output of the DataSocket Read function for detailed descriptions of the quality values. Use the Shared Variable Error from Quality VI to convert this code to an error I/O cluster. error out — error out contains error information. This output provides standard error out functionality. |
| --- |

Parent topic:

Read Current Tag Trace as Trend.vi

<!--NI_TOPIC bundle=lvdsc-api-ref path=vi-lib/lvdsc/tagapi/classes/tag-reader/read-current-tag-trace-as-trend-multiple/read-current-tag-trace-as-trend-multiple-uint32-vi.html language=enus -->
## TOPIC 00043: Read Current Tag Trace as Trend (Multiple, UInt32) VI

- bundle_id: `lvdsc-api-ref`
- source_path: `vi-lib/lvdsc/tagapi/classes/tag-reader/read-current-tag-trace-as-trend-multiple/read-current-tag-trace-as-trend-multiple-uint32-vi.html`
- source_url: https://docs-be.ni.com/bundle/lvdsc-api-ref/raw/resource/enus/vi-lib/lvdsc/tagapi/classes/tag-reader/read-current-tag-trace-as-trend-multiple/read-current-tag-trace-as-trend-multiple-uint32-vi.html
- document_id: `lvdsc-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Reads the current trend of a tag in waveform format. You must manually select the polymorphic instance to use. This VI interacts with data in the Citadel database only. Use the pull-down menu to select an instance of this VI. icon Inputs/Outputs ci32.png timeout (30 s) timeout specifies the maximum

### Read Current Tag Trace as Trend (Multiple, UInt32) VI

Reads the current trend of a tag in waveform format. You must manually select the polymorphic instance to use.

Note

Use the pull-down menu to select an instance of this VI.

[IMAGE alt='icon' src='read-current-tag-trace-as-trend-multiple-uint32-vi.png']

#### Inputs/Outputs

| timeout (30 s) — timeout specifies the maximum time, in seconds, that this VI waits for reading data from the Citadel database. The default is 30. A timeout value of less than or equal to 0 specifies no timeout, which means this VI waits indefinitely until this VI receives data from the Citadel database. max points per trace (all) — max points per trace specifies the maximum number of points to read from the database. This VI returns all available points of this trace in seconds before now in the following cases: max points per trace is less than zero.The number of the data points in seconds before now is less than the max points per trace. If max points per trace is zero, this VI returns no point for the trace. The default is -1. — Tag Reader in specifies the data of a group of tags that the Open Tag Reader VI opens. tag names — tag names specifies a list of the tags for which you want to read the historical data. seconds before now (60 s) — seconds before now specifies a time interval between the start time and the current time. This VI retrieves the data in this time interval from the database. The default is 60 seconds. error in (no error) — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. database URL — database URL specifies the computer name and the database name where the Citadel database resides. Enter the database URL in the format \\\\computer\\database. interpolation interval (1 s) — interpolation interval specifies the interval, in seconds, at which this VI interpolates the data. The default is 1. — Tag Reader out returns the value of the Tag Reader instance. waveform graph — waveform graph returns a list of waveforms of the historical data of the specified tags. quality — quality returns a list of the data quality of the traces that this VI reads from multiple tags. A value of zero indicates good quality. Refer to the quality output of the DataSocket Read function for detailed descriptions of the quality values. Use the Shared Variable Error from Quality VI to convert this code to an error I/O cluster. error out — error out contains error information. This output provides standard error out functionality. |
| --- |

Parent topic:

Read Current Tag Trace as Trend.vi

<!--NI_TOPIC bundle=lvdsc-api-ref path=vi-lib/lvdsc/tagapi/classes/tag-reader/read-current-tag-trace-as-trend/read-current-tag-trace-as-trend-single-boolean-vi.html language=enus -->
## TOPIC 00044: Read Current Tag Trace as Trend (Single, Boolean) VI

- bundle_id: `lvdsc-api-ref`
- source_path: `vi-lib/lvdsc/tagapi/classes/tag-reader/read-current-tag-trace-as-trend/read-current-tag-trace-as-trend-single-boolean-vi.html`
- source_url: https://docs-be.ni.com/bundle/lvdsc-api-ref/raw/resource/enus/vi-lib/lvdsc/tagapi/classes/tag-reader/read-current-tag-trace-as-trend/read-current-tag-trace-as-trend-single-boolean-vi.html
- document_id: `lvdsc-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Reads the current trend of a tag in waveform format. You must manually select the polymorphic instance to use. This VI interacts with data in the Citadel database only. Use the pull-down menu to select an instance of this VI. icon Inputs/Outputs ci32.png timeout (30 s) timeout specifies the maximum

### Read Current Tag Trace as Trend (Single, Boolean) VI

Reads the current trend of a tag in waveform format. You must manually select the polymorphic instance to use.

Note

Use the pull-down menu to select an instance of this VI.

[IMAGE alt='icon' src='read-current-tag-trace-as-trend-single-boolean-vi.png']

#### Inputs/Outputs

| timeout (30 s) — timeout specifies the maximum time, in seconds, that this VI waits for reading data from the Citadel database. The default is 30. A timeout value of less than or equal to 0 specifies no timeout, which means this VI waits indefinitely until this VI receives data from the Citadel database. max points per trace (all) — max points per trace specifies the maximum number of points to read from the database. This VI returns all available points of this trace in seconds before now in the following cases: max points per trace is less than zero.The number of the data points in seconds before now is less than the max points per trace. If max points per trace is zero, this VI returns no point for the trace. The default is -1. — Tag Reader in specifies the data of a group of tags that the Open Tag Reader VI opens. tag name — tag name specifies the name of the tag for which you want to read the historical data. seconds before now (60 s) — seconds before now specifies a time interval between the start time and the current time. This VI retrieves the data in this time interval from the database. The default is 60 seconds. error in (no error) — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. database URL — database URL specifies the computer name and the database name where the Citadel database resides. Enter the database URL in the format \\\\computer\\database. interpolation interval (1 s) — interpolation interval specifies the interval, in seconds, at which this VI interpolates the data. The default is 1. — Tag Reader out returns the value of the Tag Reader instance. waveform graph — waveform graph returns the historical data of the specified tag in waveform format. quality — quality returns the data quality of the trace this VI reads from a tag. A value of zero indicates good quality. Refer to the quality output of the DataSocket Read function for detailed descriptions of the quality values. Use the Shared Variable Error from Quality VI to convert this code to an error I/O cluster. error out — error out contains error information. This output provides standard error out functionality. |
| --- |

Parent topic:

Read Current Tag Trace as Trend.vi

<!--NI_TOPIC bundle=lvdsc-api-ref path=vi-lib/lvdsc/tagapi/classes/tag-reader/read-current-tag-trace-as-trend/read-current-tag-trace-as-trend-single-double-vi.html language=enus -->
## TOPIC 00045: Read Current Tag Trace as Trend (Single, Double) VI

- bundle_id: `lvdsc-api-ref`
- source_path: `vi-lib/lvdsc/tagapi/classes/tag-reader/read-current-tag-trace-as-trend/read-current-tag-trace-as-trend-single-double-vi.html`
- source_url: https://docs-be.ni.com/bundle/lvdsc-api-ref/raw/resource/enus/vi-lib/lvdsc/tagapi/classes/tag-reader/read-current-tag-trace-as-trend/read-current-tag-trace-as-trend-single-double-vi.html
- document_id: `lvdsc-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Reads the current trend of a tag in waveform format. You must manually select the polymorphic instance to use. This VI interacts with data in the Citadel database only. Use the pull-down menu to select an instance of this VI. icon Inputs/Outputs ci32.png timeout (30 s) timeout specifies the maximum

### Read Current Tag Trace as Trend (Single, Double) VI

Reads the current trend of a tag in waveform format. You must manually select the polymorphic instance to use.

Note

Use the pull-down menu to select an instance of this VI.

[IMAGE alt='icon' src='read-current-tag-trace-as-trend-single-double-vi.png']

#### Inputs/Outputs

| timeout (30 s) — timeout specifies the maximum time, in seconds, that this VI waits for reading data from the Citadel database. The default is 30. A timeout value of less than or equal to 0 specifies no timeout, which means this VI waits indefinitely until this VI receives data from the Citadel database. max points per trace (all) — max points per trace specifies the maximum number of points to read from the database. This VI returns all available points of this trace in seconds before now in the following cases: max points per trace is less than zero.The number of the data points in seconds before now is less than the max points per trace. If max points per trace is zero, this VI returns no point for the trace. The default is -1. — Tag Reader in specifies the data of a group of tags that the Open Tag Reader VI opens. tag name — tag name specifies the name of the tag for which you want to read the historical data. seconds before now (60 s) — seconds before now specifies a time interval between the start time and the current time. This VI retrieves the data in this time interval from the database. The default is 60 seconds. error in (no error) — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. database URL — database URL specifies the computer name and the database name where the Citadel database resides. Enter the database URL in the format \\\\computer\\database. interpolation interval (1 s) — interpolation interval specifies the interval, in seconds, at which this VI interpolates the data. The default is 1. — Tag Reader out returns the value of the Tag Reader instance. waveform graph — waveform graph returns the historical data of the specified tag in waveform format. quality — quality returns the data quality of the trace this VI reads from a tag. A value of zero indicates good quality. Refer to the quality output of the DataSocket Read function for detailed descriptions of the quality values. Use the Shared Variable Error from Quality VI to convert this code to an error I/O cluster. error out — error out contains error information. This output provides standard error out functionality. |
| --- |

Parent topic:

Read Current Tag Trace as Trend.vi

<!--NI_TOPIC bundle=lvdsc-api-ref path=vi-lib/lvdsc/tagapi/classes/tag-reader/read-current-tag-trace-as-trend/read-current-tag-trace-as-trend-single-uint32-vi.html language=enus -->
## TOPIC 00046: Read Current Tag Trace as Trend (Single, UInt32) VI

- bundle_id: `lvdsc-api-ref`
- source_path: `vi-lib/lvdsc/tagapi/classes/tag-reader/read-current-tag-trace-as-trend/read-current-tag-trace-as-trend-single-uint32-vi.html`
- source_url: https://docs-be.ni.com/bundle/lvdsc-api-ref/raw/resource/enus/vi-lib/lvdsc/tagapi/classes/tag-reader/read-current-tag-trace-as-trend/read-current-tag-trace-as-trend-single-uint32-vi.html
- document_id: `lvdsc-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Reads the current trend of a tag in waveform format. You must manually select the polymorphic instance to use. This VI interacts with data in the Citadel database only. Use the pull-down menu to select an instance of this VI. icon Inputs/Outputs ci32.png timeout (30 s) timeout specifies the maximum

### Read Current Tag Trace as Trend (Single, UInt32) VI

Reads the current trend of a tag in waveform format. You must manually select the polymorphic instance to use.

Note

Use the pull-down menu to select an instance of this VI.

[IMAGE alt='icon' src='read-current-tag-trace-as-trend-single-uint32-vi.png']

#### Inputs/Outputs

| timeout (30 s) — timeout specifies the maximum time, in seconds, that this VI waits for reading data from the Citadel database. The default is 30. A timeout value of less than or equal to 0 specifies no timeout, which means this VI waits indefinitely until this VI receives data from the Citadel database. max points per trace (all) — max points per trace specifies the maximum number of points to read from the database. This VI returns all available points of this trace in seconds before now in the following cases: max points per trace is less than zero.The number of the data points in seconds before now is less than the max points per trace. If max points per trace is zero, this VI returns no point for the trace. The default is -1. — Tag Reader in specifies the data of a group of tags that the Open Tag Reader VI opens. tag name — tag name specifies the name of the tag for which you want to read the historical data. seconds before now (60 s) — seconds before now specifies a time interval between the start time and the current time. This VI retrieves the data in this time interval from the database. The default is 60 seconds. error in (no error) — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. database URL — database URL specifies the computer name and the database name where the Citadel database resides. Enter the database URL in the format \\\\computer\\database. interpolation interval (1 s) — interpolation interval specifies the interval, in seconds, at which this VI interpolates the data. The default is 1. — Tag Reader out returns the value of the Tag Reader instance. waveform graph — waveform graph returns the historical data of the specified tag in waveform format. quality — quality returns the data quality of the trace this VI reads from a tag. A value of zero indicates good quality. Refer to the quality output of the DataSocket Read function for detailed descriptions of the quality values. Use the Shared Variable Error from Quality VI to convert this code to an error I/O cluster. error out — error out contains error information. This output provides standard error out functionality. |
| --- |

Parent topic:

Read Current Tag Trace as Trend.vi

<!--NI_TOPIC bundle=lvdsc-api-ref path=vi-lib/lvdsc/tagapi/classes/tag-reader/read-tag-multiple/read-tag-multiple-variant-vi.html language=enus -->
## TOPIC 00047: Read Tag (Multiple, Variant) VI

- bundle_id: `lvdsc-api-ref`
- source_path: `vi-lib/lvdsc/tagapi/classes/tag-reader/read-tag-multiple/read-tag-multiple-variant-vi.html`
- source_url: https://docs-be.ni.com/bundle/lvdsc-api-ref/raw/resource/enus/vi-lib/lvdsc/tagapi/classes/tag-reader/read-tag-multiple/read-tag-multiple-variant-vi.html
- document_id: `lvdsc-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Reads the value of specified tags. You must manually select the polymorphic instance to use. Use the pull-down menu to select an instance of this VI. icon Inputs/Outputs cTag_Readerlvclass.png Tag Reader in specifies the data of a group of tags that the Open Tag Reader VI opens. c1dstr.png tag names

### Read Tag (Multiple, Variant) VI

Reads the value of specified tags. You must manually select the polymorphic instance to use.

Use the pull-down menu to select an instance of this VI.

[IMAGE alt='icon' src='read-tag-multiple-variant-vi.png']

#### Inputs/Outputs

| — Tag Reader in specifies the data of a group of tags that the Open Tag Reader VI opens. tag names — tag names specifies the names of the tags you want to read. timeout (10000 ms) — timeout specifies the maximum time, in milliseconds, that this VI waits to read the tag. The default is 10000. error in (no error) — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. status — status is TRUE (X) if an error occurred or FALSE (checkmark) to indicate a warning or that no error occurred. quality — quality returns the data quality of the data this VI reads from tags. A value of zero indicates good quality. Refer to the quality output of the DataSocket Read function for detailed descriptions of the quality values. Use the Shared Variable Error from Quality VI to convert this code to an error I/O cluster. — Tag Reader out returns the value of the Tag Reader instance. data — datareturns a list of values of the specified tags. If this VI times out when read a tag, data returns the value that this VI last read. If this VI times out before reading any data from a tag or if the type of data is incompatible, data returns a value of 0, empty, or an equivalent value for this tag. timestamps — timestamps returns a list of the timestamp data for the specified tags. error out — error out contains error information. This output provides standard error out functionality. |
| --- |

Parent topic:

Read Tag.vi

<!--NI_TOPIC bundle=lvdsc-api-ref path=vi-lib/lvdsc/tagapi/classes/tag-reader/read-tag/read-tag-single-boolean-vi.html language=enus -->
## TOPIC 00048: Read Tag (Single, Boolean) VI

- bundle_id: `lvdsc-api-ref`
- source_path: `vi-lib/lvdsc/tagapi/classes/tag-reader/read-tag/read-tag-single-boolean-vi.html`
- source_url: https://docs-be.ni.com/bundle/lvdsc-api-ref/raw/resource/enus/vi-lib/lvdsc/tagapi/classes/tag-reader/read-tag/read-tag-single-boolean-vi.html
- document_id: `lvdsc-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Reads the value of specified tags. You must manually select the polymorphic instance to use. Use the pull-down menu to select an instance of this VI. icon Inputs/Outputs cTag_Readerlvclass.png Tag Reader in specifies the data of a group of tags that the Open Tag Reader VI opens. cstr.png tag name ta

### Read Tag (Single, Boolean) VI

Reads the value of specified tags. You must manually select the polymorphic instance to use.

Use the pull-down menu to select an instance of this VI.

[IMAGE alt='icon' src='read-tag-single-boolean-vi.png']

#### Inputs/Outputs

| — Tag Reader in specifies the data of a group of tags that the Open Tag Reader VI opens. tag name — tag name specifies the name of the tag that you want to read. timeout (10000 ms) — timeout specifies the maximum time, in milliseconds, that this VI waits to read the tag. The default is 10000. error in (no error) — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. wait for updated value? (F) — wait for updated value? specifies whether this VI waits for an updated value. The default is FALSE. status — status is TRUE (X) if an error occurred or FALSE (checkmark) to indicate a warning or that no error occurred. quality — quality returns the data quality of the data this VI reads from a tag. A value of zero indicates good quality. Refer to the quality output of the DataSocket Read function for detailed descriptions of the quality values. Use the Shared Variable Error from Quality VI to convert this code to an error I/O cluster. — Tag Reader out returns the value of the Tag Reader instance. data — data returns the value of the specified tag. If this VI times out, data returns the value that this VI last read. If this VI times out before reading any data or if the type of data is incompatible, data returns FALSE. timestamp — timestamp returns the timestamp data for the specified tag. error out — error out contains error information. This output provides standard error out functionality. timed out? — timed out? returns TRUE if this VI times out waiting for an update or an initial value. |
| --- |

Parent topic:

Read Tag.vi

<!--NI_TOPIC bundle=lvdsc-api-ref path=vi-lib/lvdsc/variables/configure-alarming-vi.html language=enus -->
## TOPIC 00049: Configure Alarming VI

- bundle_id: `lvdsc-api-ref`
- source_path: `vi-lib/lvdsc/variables/configure-alarming-vi.html`
- source_url: https://docs-be.ni.com/bundle/lvdsc-api-ref/raw/resource/enus/vi-lib/lvdsc/variables/configure-alarming-vi.html
- document_id: `lvdsc-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Configures the alarm settings of a shared variable. You first must enable alarming for a shared variable before you can configure alarm settings. You enable alarming by setting the enable? input in the Configure Alarming (Shared Variable, Enable Alarming) VI to TRUE. You must manually select the pol

### Configure Alarming VI

Configures the alarm settings of a shared variable.

enable?

manually select

Note

network-published

Use the pull-down menu to select an instance of this VI.

[IMAGE alt='icon' src='configure-alarming-vi.png']

- [Configure Alarming (Shared Variable, Enable Alarming) VI](../../../vi-lib/lvdsc/variables/internal/configure-alarming-shared-variable-enable-alarming-vi.html) Configures the alarm settings of a shared variable.
- [Configure Alarming (Shared Variable, Numeric) VI](../../../vi-lib/lvdsc/variables/internal/configure-alarming-shared-variable-numeric-vi.html) Configures the alarm settings of a shared variable.
- [Configure Alarming (Shared Variable, Boolean) VI](../../../vi-lib/lvdsc/variables/internal/configure-alarming-shared-variable-boolean-vi.html) Configures the alarm settings of a shared variable.
- [Configure Alarming (Shared Variable, Bit Array) VI](../../../vi-lib/lvdsc/variables/internal/configure-alarming-shared-variable-bit-array-vi.html) Configures the alarm settings of a shared variable.
- [Configure Alarming (Shared Variable, Bad Status) VI](../../../vi-lib/lvdsc/variables/internal/configure-alarming-shared-variable-bad-status-vi.html) Configures the alarm settings of a shared variable.
- [Configure Alarming (Shared Variable, Rate of Change) VI](../../../vi-lib/lvdsc/variables/internal/configure-alarming-shared-variable-rate-of-change-vi.html) Configures the alarm settings of a shared variable.

Parent topic:

Variables & I/O Servers

<!--NI_TOPIC bundle=lvdsc-api-ref path=vi-lib/lvdsc/variables/configure-description-vi.html language=enus -->
## TOPIC 00050: Configure Description VI

- bundle_id: `lvdsc-api-ref`
- source_path: `vi-lib/lvdsc/variables/configure-description-vi.html`
- source_url: https://docs-be.ni.com/bundle/lvdsc-api-ref/raw/resource/enus/vi-lib/lvdsc/variables/configure-description-vi.html
- document_id: `lvdsc-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Configures the description of a shared variable. icon Inputs/Outputs cgenclassrntag.png variable reference in variable reference in specifies a reference number for a shared variable. Use the Create Shared Variable VI to create a refnum for a shared variable. cstr.png description description specifi

### Configure Description VI

Configures the description of a shared variable.

[IMAGE alt='icon' src='configure-description-vi.png']

#### Inputs/Outputs

| variable reference in — variable reference in specifies a reference number for a shared variable. Use the Create Shared Variable VI to create a refnum for a shared variable. description — description specifies the description you want to set for the shared variable. error in (no error) — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. variable reference out — variable reference out returns the shared variable refnum that you wire to the variable reference in input. error out — error out contains error information. This output provides standard error out functionality. |
| --- |

Parent topic:

Variables & I/O Servers

<!--NI_TOPIC bundle=lvdsc-api-ref path=vi-lib/modbus/master/create-master-instance-tcp-vi.html language=enus -->
## TOPIC 00051: Create Master Instance (TCP) VI

- bundle_id: `lvdsc-api-ref`
- source_path: `vi-lib/modbus/master/create-master-instance-tcp-vi.html`
- source_url: https://docs-be.ni.com/bundle/lvdsc-api-ref/raw/resource/enus/vi-lib/modbus/master/create-master-instance-tcp-vi.html
- document_id: `lvdsc-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Creates a serial or TCP Modbus master instance. You must manually select the polymorphic instance to use. You can use the Modbus master instance to perform read and write operations on Modbus slaves. The default read and write operation timeout is 5,000 ms. You can use the Property Node or the Set T

### Create Master Instance (TCP) VI

Creates a serial or TCP Modbus master instance. You must manually select the polymorphic instance to use.

You can use the Modbus master instance to perform read and write operations on Modbus slaves. The default read and write operation timeout is 5,000 ms. You can use the [Property Node](master-property-node-vi.html) or the [Set Timeouts](set-timeouts-vi.html) VI to change the timeout.

Use the pull-down menu to select an instance of this VI.

[IMAGE alt='icon' src='create-master-instance-tcp-vi.png']

#### Inputs/Outputs

| address — address specifies the TCP/IP address of the Modbus slave with which you want to communicate. port (502) — port specifies the TCP port of the Modbus slave with which you want to communicate. The Modbus slave can be a Modbus slave you create or a third-party Modbus slave. If you want to communicate with a third-party Modbus slave, check the documentation for the Modbus slave to find its port. The default is 502. error in (no error) — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. TCP master instance — TCP master instance returns a TCP Modbus master instance. error out — error out contains error information. This output provides standard error out functionality. |
| --- |

#### Examples

Refer to the following VIs for examples of using the Create Master Instance VI:

- labview\examples\Data Communication\Modbus\ModbusLibrary\Modbus Library.lvproj
- labview\examples\Data Communication\Modbus\Redundant Modbus Masters\Redundant Modbus Masters.lvproj

Parent topic:

Create Master Instance VI

<!--NI_TOPIC bundle=lvdsc-api-ref path=vi-lib/modbus/master/create-master-instance-vi.html language=enus -->
## TOPIC 00052: Create Master Instance VI

- bundle_id: `lvdsc-api-ref`
- source_path: `vi-lib/modbus/master/create-master-instance-vi.html`
- source_url: https://docs-be.ni.com/bundle/lvdsc-api-ref/raw/resource/enus/vi-lib/modbus/master/create-master-instance-vi.html
- document_id: `lvdsc-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Creates a serial or TCP Modbus master instance. You must manually select the polymorphic instance to use. You can use the Modbus master instance to perform read and write operations on Modbus slaves. The default read and write operation timeout is 5,000 ms. You can use the Property Node or the Set T

### Create Master Instance VI

Creates a serial or TCP Modbus master instance. You must manually select the polymorphic instance to use.

You can use the Modbus master instance to perform read and write operations on Modbus slaves. The default read and write operation timeout is 5,000 ms. You can use the [Property Node](master-property-node-vi.html) or the [Set Timeouts](set-timeouts-vi.html) VI to change the timeout.

Use the pull-down menu to select an instance of this VI.

[IMAGE alt='icon' src='create-master-instance-vi.png']

#### Examples

Refer to the following VIs for examples of using the Create Master Instance VI:

- labview\examples\Data Communication\Modbus\ModbusLibrary\Modbus Library.lvproj
- labview\examples\Data Communication\Modbus\Redundant Modbus Masters\Redundant Modbus Masters.lvproj

- [Create Master Instance (TCP) VI](../../../vi-lib/modbus/master/create-master-instance-tcp-vi.html) Creates a serial or TCP Modbus master instance. You must manually select the polymorphic instance to use.
- [Create Master Instance (Serial) VI](../../../vi-lib/modbus/master/create-master-instance-serial-vi.html) Creates a serial or TCP Modbus master instance. You must manually select the polymorphic instance to use.

Parent topic:

Modbus Master

<!--NI_TOPIC bundle=lvdsc-api-ref path=vi-lib/modbus/master/functions/mask-write-holding-register-vi.html language=enus -->
## TOPIC 00053: Mask Write Holding Register VI

- bundle_id: `lvdsc-api-ref`
- source_path: `vi-lib/modbus/master/functions/mask-write-holding-register-vi.html`
- source_url: https://docs-be.ni.com/bundle/lvdsc-api-ref/raw/resource/enus/vi-lib/modbus/master/functions/mask-write-holding-register-vi.html
- document_id: `lvdsc-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Writes values to one or more bits of a holding register. icon Inputs/Outputs cModbus_Masterlvclass.png Modbus master in Modbus master in specifies the reference to the Modbus master instance. Use the Create Master Instance VI to create a Modbus master instance. cu16.png address address specifies the

### Mask Write Holding Register VI

Writes values to one or more bits of a holding register.

[IMAGE alt='icon' src='mask-write-holding-register-vi.png']

#### Inputs/Outputs

| Modbus master in — Modbus master in specifies the reference to the Modbus master instance. Use the Create Master Instance VI to create a Modbus master instance. address — address specifies the holding register address to which you want to write the values. Valid values are between 0 and 65,535, where 65,535 is the maximum number. The address that this VI writes is 0-based, meaning that the address numbering convention for the Modbus slave starts at 0. error in (no error) — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. AND mask — AND mask specifies the AND mask you use to write bits of a holding register. Refer to the Details section of this topic for examples of specifying the AND mask. OR mask — OR mask specifies the OR mask you use to write bits of a holding register. Refer to the Details section of this topic for examples of specifying the OR mask. Modbus master out — Modbus master out returns a duplicate of Modbus master in. error out — error out contains error information. This output provides standard error out functionality. |
| --- |

#### Mask Write Holding Register Details

The Mask Write Holding Register VI uses the following algorithm to calculate the value to write to individual bits of a holding register:

|  | updated value = (current value AND AND mask) OR (OR mask AND (NOT AND mask)) |
| --- | --- |

Based on the previous algorithm, you can specify values for **AND mask** and **OR mask** according to the following rules:

- To write a bit, specify 1 for AND mask for this bit. If you want to mask a bit, specify 0 for AND mask for this bit. When you specify 0 for AND mask , the value of the bit does not change regardless of what value you specify for OR mask .
- After you specify 0 for AND mask for a bit, you can specify 0 for OR mask to change the value of this bit to 0, regardless of the current value of the bit.
- After you specify 0 for AND mask for a bit, you can specify 1 for OR mask to change the value of this bit to 1, regardless of the current value of the bit.

Parent topic:

Modbus Master

<!--NI_TOPIC bundle=lvdsc-api-ref path=vi-lib/modbus/master/functions/read-coils-vi.html language=enus -->
## TOPIC 00054: Read Coils VI

- bundle_id: `lvdsc-api-ref`
- source_path: `vi-lib/modbus/master/functions/read-coils-vi.html`
- source_url: https://docs-be.ni.com/bundle/lvdsc-api-ref/raw/resource/enus/vi-lib/modbus/master/functions/read-coils-vi.html
- document_id: `lvdsc-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Reads values from contiguous coils. The maximum number of coils this VI can read is 2,000. icon Inputs/Outputs cModbus_Masterlvclass.png Modbus master in Modbus master in specifies the reference to the Modbus master instance. Use the Create Master Instance VI to create a Modbus master instance. cu16

### Read Coils VI

Reads values from contiguous coils. The maximum number of coils this VI can read is 2,000.

[IMAGE alt='icon' src='read-coils-vi.png']

#### Inputs/Outputs

| Modbus master in — Modbus master in specifies the reference to the Modbus master instance. Use the Create Master Instance VI to create a Modbus master instance. starting address — starting address specifies the initial address for the read operation. Valid values are between 0 and 65,535, where 65,535 is the maximum number. The address that this VI reads is 0-based, meaning that the address numbering convention for the Modbus slave starts at 0. number of coils — number of coils specifies the number of coils you want to read. Valid values are between 1 and 2,000, where 2,000 is the maximum number. After you specify a value for number of coils, check the value you specify for starting address. Ensure that you do not use this VI to read the value of a coil whose address is larger than 65,535. Otherwise, LabVIEW returns error code -389113. error in (no error) — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. Modbus master out — Modbus master out returns a duplicate of Modbus master in. coil values — coil values returns the coil values. error out — error out contains error information. This output provides standard error out functionality. |
| --- |

#### Examples

Refer to the Modbus Library.lvproj in the labview\examples\Data Communication\Modbus\ModbusLibrary directory for an example of using the Read Coils VI.

Parent topic:

Modbus Master

<!--NI_TOPIC bundle=lvdsc-api-ref path=vi-lib/modbus/master/set-unit-id-vi.html language=enus -->
## TOPIC 00055: Set Unit ID VI

- bundle_id: `lvdsc-api-ref`
- source_path: `vi-lib/modbus/master/set-unit-id-vi.html`
- source_url: https://docs-be.ni.com/bundle/lvdsc-api-ref/raw/resource/enus/vi-lib/modbus/master/set-unit-id-vi.html
- document_id: `lvdsc-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Sets the identification of a serial Modbus slave. When you wire a Modbus master instance to the Modbus master in input and specify a value for the unit ID input, this Modbus master instance can communicate with the Modbus slave with the specified unit ID. This VI ignores requests from TCP Modbus mas

### Set Unit ID VI

Sets the identification of a serial Modbus slave. When you wire a Modbus master instance to the **Modbus master in** input and specify a value for the **unit ID** input, this Modbus master instance can communicate with the Modbus slave with the specified unit ID. This VI ignores requests from TCP Modbus master instances.

You can also use the [Property Node](master-property-node-vi.html) to set the identification of a Modbus slave.

[IMAGE alt='icon' src='set-unit-id-vi.png']

#### Inputs/Outputs

| Modbus master in — Modbus master in specifies the reference to the Modbus master instance. Use the Create Master Instance VI to create a Modbus master instance. unit ID — unit ID specifies the identification of the Modbus slave. error in (no error) — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. Modbus master out — Modbus master out returns a duplicate of Modbus master in. error out — error out contains error information. This output provides standard error out functionality. |
| --- |

#### Set Unit ID Details

You can use the Set Unit ID VI to simultaneously access different Modbus slaves through a single serial Modbus master instance, as shown in the following block diagram:

[IMAGE alt='image' src='loc_bd_set_unit_id_demo.gif']

The following list describes important details about the previous diagram:

|  | The serial master instance 1 output can access the Modbus slave with a unit ID of 1. |
| --- | --- |
|  | The serial master instance 2 output can access the Modbus slave with a unit ID of 2. |

Parent topic:

Utilities

<!--NI_TOPIC bundle=lvdsc-api-ref path=vi-lib/modbus/slave/functions/write-single-holding-register-vi.html language=enus -->
## TOPIC 00056: Write Single Holding Register VI

- bundle_id: `lvdsc-api-ref`
- source_path: `vi-lib/modbus/slave/functions/write-single-holding-register-vi.html`
- source_url: https://docs-be.ni.com/bundle/lvdsc-api-ref/raw/resource/enus/vi-lib/modbus/slave/functions/write-single-holding-register-vi.html
- document_id: `lvdsc-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Writes a value to a single holding register. icon Inputs/Outputs cModbus_Slavelvclass.png Modbus slave in Modbus slave in specifies the reference to the Modbus slave instance. Use the Create Slave Instance VI to create a Modbus slave instance. cu16.png address address specifies the holding register

### Write Single Holding Register VI

Writes a value to a single holding register.

[IMAGE alt='icon' src='write-single-holding-register-vi.png']

#### Inputs/Outputs

| Modbus slave in — Modbus slave in specifies the reference to the Modbus slave instance. Use the Create Slave Instance VI to create a Modbus slave instance. address — address specifies the holding register address to which you want to write the value. Valid values are between 0 and 65,535, where 65,535 is the maximum number. The address numbering convention for the Modbus slave starts at 0. holding register value — holding register value specifies the holding register value you want to write. error in (no error) — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. Modbus slave out — Modbus slave out returns a duplicate of Modbus slave in. error out — error out contains error information. This output provides standard error out functionality. |
| --- |

Parent topic:

Modbus Slave

<!--NI_TOPIC bundle=lvdsc-api-ref path=vi-lib/modbus/slave/slave-property-node-vi.html language=enus -->
## TOPIC 00057: Property Node

- bundle_id: `lvdsc-api-ref`
- source_path: `vi-lib/modbus/slave/slave-property-node-vi.html`
- source_url: https://docs-be.ni.com/bundle/lvdsc-api-ref/raw/resource/enus/vi-lib/modbus/slave/slave-property-node-vi.html
- document_id: `lvdsc-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets or reads properties of a Modbus slave. Use this node to read the daemon error and daemon status of a Modbus slave and to get the number of TCP connections and TCP connection information of a TCP Modbus slave. Daemon is a background process of Modbus slaves and responds to requests from Modbus m

### Property Node

Gets or reads properties of a Modbus slave. Use this node to read the daemon error and daemon status of a Modbus slave and to get the number of TCP connections and TCP connection information of a TCP Modbus slave. Daemon is a background process of Modbus slaves and responds to requests from Modbus master instances.

[IMAGE alt='icon' src='slave-property-node-vi.png']

#### Inputs/Outputs

| reference — reference is the refnum associated with the object for which you want to get properties. You must wire a Modbus slave instance to the reference input. Use the Create Slave Instance VI to create a Modbus slave instance. error in (no error) — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. reference out — reference is the refnum associated with the object for which you want to get properties. You must wire a Modbus slave instance to the reference input. Use the Create Slave Instance VI to create a Modbus slave instance. error out — error out contains error information. This output provides standard error out functionality. Property — |
| --- |

#### Examples

Refer to the Modbus Library.lvproj in the labview\examples\Data Communication\Modbus\ModbusLibrary directory for an example of using the Property Node function.

Parent topic:

Modbus Slave
