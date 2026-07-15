# NI DOCUMENT BUNDLE: labview-nxg-creating-first-application

<!--NI_BUNDLE_CHUNK bundle=labview-nxg-creating-first-application start=1 end=14 -->
<!--NI_TOPIC bundle=labview-nxg-creating-first-application path=abort-execution.html language=enus -->
## TOPIC 00001: Warning about the Abort Button

- bundle_id: `labview-nxg-creating-first-application`
- source_path: `abort-execution.html`
- source_url: https://docs-be.ni.com/bundle/labview-nxg-creating-first-application/raw/resource/enus/abort-execution.html
- document_id: `labview-nxg-creating-first-application`
- page_type: `leaf`
- content_type: `concept`
- source_description: The Abort button stops a program before it completes execution. Aborting a program that uses external resources, such as external hardware or file I/O operations, might leave the resources in an unknown state and cause the program to return errors the next time you access the resources. An alternati

Warning about the Abort Button

The 
 Abort button stops a program before it completes execution.

Aborting a program that uses external resources, such as external hardware or file I/O operations, might leave the resources in an unknown state and cause the program to return errors the next time you access the resources. An alternative to using the 
 Abort button is to enclose code that uses external resources in a While Loop with a 
 Stop button. Using the 
 Stop button instead of the 
 Abort button cleans up external resources before stopping execution.

Note

Parent topic:

Creating Your First Application

<!--NI_TOPIC bundle=labview-nxg-creating-first-application path=analyzing-data.html language=enus -->
## TOPIC 00002: Analyzing Data in an Interactive Graph

- bundle_id: `labview-nxg-creating-first-application`
- source_path: `analyzing-data.html`
- source_url: https://docs-be.ni.com/bundle/labview-nxg-creating-first-application/raw/resource/enus/analyzing-data.html
- document_id: `labview-nxg-creating-first-application`
- page_type: `leaf`
- content_type: `task`
- source_description: You can better understand your data by visualizing it in an interactive graph. Viewing data in different formats can provide insight into trends or outliers in the data. For certain data types, you can also use an analysis panel to configure and apply an analysis function, capture the data that the

Analyzing Data in an Interactive Graph

You can better understand your data by visualizing it in an interactive graph.

Viewing data in different formats can provide insight into trends or outliers in the data. For certain data types, you can also use an analysis panel to configure and apply an analysis function, capture the data that the function produces, and create a node that replicates the analysis function you configure to use in your code.

1. Capture data that your application generated using one of the following options:
  - Right-click a panel object and select 
 Capture data .
  - Select 
 Data»Capture panel data .
2. Double-click the data item in the 
 Captured Data tab to visualize the data in the workspace.
3. Use the workspace to explore and configure the data in the graph.
4. If you want to apply an analysis function to the data in the graph, select an analysis panel on the 
 Plots tab. 
 org.dita.html5/xsl/topic.xsl 455Note To use analysis panels, your data item must be an analog waveform of double-precision floating-point numbers or a 1D-array of double-precision floating-point numbers. If your data item does not meet the data type requirement, use a conversion node and capture the converted data to complete this step. 
 Analysis FunctionDescriptionAmplitude Measurements
 Performs peak amplitude measurement.Curve Fit
 Finds the line that best represents an input signal or input data set using a specific fitting method.FFT Spectrum
 Computes the averaged FFT spectrum of a signal.Filter
 Applies a lowpass, highpass, bandpass, or bandstop filter to a signal.Histogram
 Finds the discrete histogram of a signal.Limit Testing
 Performs limit testing by comparing the signal to upper and lower limits that you define.Pulse and Transition Measurements
 Returns various measurements of a specific pulse in a periodic waveform or an array of periodic waveforms, such as the period, pulse duration, and duty cycle.Resample
 Resamples a signal according to a specific delay and sampling interval.Scaling and Mapping
 Scales a signal based on a straight line.Signal Correlation
 Computes the auto correlation of a signal or cross correlation of two signals.Statistics
 Performs statistical calculations on a signal.Tone Measurements
 Finds tones with specific amplitude and frequency parameters. 
 Adjust the variables of the analysis function until it meets the requirements of your application. The graph updates in real time to show the resulting data on the same graph as the original data. You can click 
 Capture & view data in the top right corner to view only the data that the function produces with the current configuration. 
 org.dita.html5/xsl/topic.xsl 455Note To create a node that replicates the analysis function you configured, open the 
 Configured Code pane at the bottom of the analysis panel, click 
 Copy to Clipboard, and then paste the node onto the diagram in a VI.

Parent topic:

Creating Your First Application

<!--NI_TOPIC bundle=labview-nxg-creating-first-application path=capturing-data.html language=enus -->
## TOPIC 00003: Capturing and Analyzing Data

- bundle_id: `labview-nxg-creating-first-application`
- source_path: `capturing-data.html`
- source_url: https://docs-be.ni.com/bundle/labview-nxg-creating-first-application/raw/resource/enus/capturing-data.html
- document_id: `labview-nxg-creating-first-application`
- page_type: `leaf`
- content_type: `task`
- source_description: You can save and analyze the data that a device or code generates in a variety of ways. Viewing data in different formats can provide insight into trends or outliers in the data. What to Use An application that generates data What to Do Use the editor to capture, store, and analyze data. Use indicat

Capturing and Analyzing Data

You can save and analyze the data that a device or code generates in a variety of ways. Viewing data in different formats can provide insight into trends or outliers in the data.

#### What to Use

- An application that generates data

#### What to Do

Use the editor to capture, store, and analyze data.

[IMAGE alt='1378' src='GUID-A7C60F53-ED97-410B-A558-3E6655010537-a5.png']

|  | Use indicators on the panel to display data that your application generates. Right-click a control, indicator, or terminal and select Capture data to capture and save the data to use later. |
| --- | --- |
|  | Use the Capture panel data button to save selected data as a data item. |
|  | View and interact with all the data you captured in a project in the Captured Data tab. Each data item represents a piece of data that originated from a single data source at a single time. |
|  | You can double-click a data item to view it in the workspace, which shows the data in an interactive graph. If the data is an analog waveform of double-precision floating-point numbers or a 1D array of double-precision floating-point numbers, you can apply and customize an analysis filter by choosing an option in the Plots tab. Right-click a data item in the Captured Data tab and select Export to export data to the following file formats: Comma-separated values file (.csv) Technical Data Management Streaming file (.tdms) MATLAB® formatted binary file (.mat) |

Parent topic:

Creating Your First Application

<!--NI_TOPIC bundle=labview-nxg-creating-first-application path=choose-right-vi-reentrancy.html language=enus -->
## TOPIC 00004: Choosing the Right VI Reentrancy Option for a SubVI

- bundle_id: `labview-nxg-creating-first-application`
- source_path: `choose-right-vi-reentrancy.html`
- source_url: https://docs-be.ni.com/bundle/labview-nxg-creating-first-application/raw/resource/enus/choose-right-vi-reentrancy.html
- document_id: `labview-nxg-creating-first-application`
- page_type: `leaf`
- content_type: `task`
- source_description: On the Document tab, in the Behavior section, click Properties to access VI Reentrancy options for your subVI. In the resulting dialog box, select the Execution tab. Choose one of the following options: Option Description None Allocates a single data space for use by all instances of the subVI. Ther

Choosing the Right VI Reentrancy Option for a SubVI

1. On the 
 Document tab, in the 
 Behavior section, click 
 Properties to access VI Reentrancy options for your subVI.
2. In the resulting dialog box, select the 
 Execution tab.
3. Choose one of the following options: 
 OptionDescriptionNone
 Allocates a single data space for use by all instances of the subVI. Therefore, the software executes multiple, simultaneous calls to a subVI one at a time in an indeterminate order. Because every instance of the subVI shares the same data space, all calls to the subVI also share a single state, which preserves the values of controls and uninitialized shift registers among calls.Stateless
 Allocates one copy, or clone, of the subVI for each processor on your machine. Each call to the subVI can then access one of these shared clones instead of waiting on the main subVI. If there are not enough shared clones for each call to the subVI, additional clones are allocated on demand. Each instance of the subVI may access a different clone each time it is called.Stateful
 Allocates a separate clone for each instance of the subVI. Each instance of the subVI stores data in its own pre-allocated clone.

Parent topic:

Creating a WebVI

Parent topic:

SubVIs

<!--NI_TOPIC bundle=labview-nxg-creating-first-application path=configure-vi-as-subvi.html language=enus -->
## TOPIC 00005: Configuring an Existing VI For Use As a SubVI

- bundle_id: `labview-nxg-creating-first-application`
- source_path: `configure-vi-as-subvi.html`
- source_url: https://docs-be.ni.com/bundle/labview-nxg-creating-first-application/raw/resource/enus/configure-vi-as-subvi.html
- document_id: `labview-nxg-creating-first-application`
- page_type: `leaf`
- content_type: `task`
- source_description: To turn an existing VI into a subVI, use the icon editor to assign input and output terminals and to customize the appearance of the subVI node. What to Do Select EditIcon and connector pane to display the icon editor. Select an icon template. You can set a background color and choose whether to inc

Configuring an Existing VI For Use As a SubVI

To turn an existing VI into a subVI, use the icon editor to assign input and output terminals and to customize the appearance of the subVI node.

#### What to Do

[IMAGE alt='1378' src='GUID-F1EB11F5-F55F-4D2D-8FB1-8FD0204B0746-a5.png']

|  | Select Edit » Icon and connector pane to display the icon editor. |
| --- | --- |
|  | Select an icon template. You can set a background color and choose whether to include the filename on the icon. You can also save the current design as a custom template. |
|  | Select a template for the terminal layout based on the number of terminals you need. Tip You can drag the bottom right corner of the icon to change the number of terminal selectors displayed. |
|  | Click a terminal selector to assign a control or indicator on the subVI panel or diagram to a specific input or output of the subVI. |
|  | Drag text and graphics from the palette to the icon to depict what the subVI does. |
|  | To use a VI as a subVI on another diagram, drag the VI from the Project Files tab to the other diagram and wire the input and output terminals. |

Parent topic:

Creating a WebVI

<!--NI_TOPIC bundle=labview-nxg-creating-first-application path=create-vi.html language=enus -->
## TOPIC 00006: Creating a WebVI

- bundle_id: `labview-nxg-creating-first-application`
- source_path: `create-vi.html`
- source_url: https://docs-be.ni.com/bundle/labview-nxg-creating-first-application/raw/resource/enus/create-vi.html
- document_id: `labview-nxg-creating-first-application`
- page_type: `leaf`
- content_type: `task`
- source_description: Create a webVI (.gviweb) in which you can write a program. In the Navigation pane, click NewWebVI. Top-level VIs must be WebVIs. Complete any of the following tasks to accomplish your programming goals: On the diagram, write code that performs your desired task when the program executes. On the pane

Creating a WebVI

Create a webVI (.gviweb) in which you can write a program.

1. In the Navigation pane, click New»WebVI. 
 org.dita.html5/xsl/topic.xsl 455Note Top-level VIs must be WebVIs.
2. Complete any of the following tasks to accomplish your programming goals:
  - On the diagram, write code that performs your desired task when the program
 executes.
  - On the panel, build a user interface .
  - On the icon editor, add inputs and outputs to configure a WebVI or a
 VI as a SubVI . After you save the SubVI, you can add it to the diagram of other
 VIs.

build the
 WebVI into a web page

Parent topic:

Creating Your First Application

Parent topic:

Applications

<!--NI_TOPIC bundle=labview-nxg-creating-first-application path=creating-a-subvi.html language=enus -->
## TOPIC 00007: Creating a SubVI

- bundle_id: `labview-nxg-creating-first-application`
- source_path: `creating-a-subvi.html`
- source_url: https://docs-be.ni.com/bundle/labview-nxg-creating-first-application/raw/resource/enus/creating-a-subvi.html
- document_id: `labview-nxg-creating-first-application`
- page_type: `leaf`
- content_type: `task`
- source_description: Right-click the diagram of an existing VI and select Create New SubVI to add an empty subVI node to the diagram. This creates a new .gvi file and adds it to the project. This file corresponds to the subVI node that appears on the diagram. Double-click the subVI node to begin adding code to the subVI

Creating a SubVI

1. Right-click the diagram of an existing VI and select 
 Create New SubVI to add an empty subVI node to the diagram. 
 This creates a new 
 .gvi file and adds it to the project. This file corresponds to the subVI node that appears on the diagram.
2. Double-click the subVI node to begin adding code to the subVI.
3. Click 
 Edit Icon and add inputs and outputs to pass data in and out of the subVI. 
 The inputs and outputs you add to the subVI icon must correspond to inputs and outputs on the diagram.

To add the new subVI as a node on other diagrams, locate the subVI in the 
 Project Files tab and drag it to the diagram where you want to use it.

Note

Parent topic:

Creating a WebVI

<!--NI_TOPIC bundle=labview-nxg-creating-first-application path=creating-your-first.html language=enus -->
## TOPIC 00008: Creating Your First Application

- bundle_id: `labview-nxg-creating-first-application`
- source_path: `creating-your-first.html`
- source_url: https://docs-be.ni.com/bundle/labview-nxg-creating-first-application/raw/resource/enus/creating-your-first.html
- document_id: `labview-nxg-creating-first-application`
- page_type: `leaf`
- content_type: `task`
- source_description: Learn about the different tasks you complete in LabVIEW NXG to create an application. Visualize, design, and document your hardware in SystemDesigner—Manage the hardware configuration of your application. Create a VI—Write a program to perform a task. Capture and analyze data—Save or analyze data th

Creating Your First Application

Learn about the different tasks you complete in LabVIEW NXG
 to create an application.

- [Visualize, design, and document your hardware in
 SystemDesigner](/csh?topicname=visualizing-designing-documenting-your-hardware-labview-nxg.html)—Manage the hardware configuration of your application.
- [Create a VI](/csh?topicname=create-vi.html)—Write a program to perform a task.
- [Capture and analyze data](/csh?topicname=capturing-data.html)—Save or analyze data that a
 device or code generates.
- [Build and distribute your application](/csh?topicname=build-and-dist.html)—Generate files
 for running your application outside the editor and distributing it to other
 machines.

<!--NI_TOPIC bundle=labview-nxg-creating-first-application path=minimize-subvi-overhead.html language=enus -->
## TOPIC 00009: Minimizing SubVI Overhead

- bundle_id: `labview-nxg-creating-first-application`
- source_path: `minimize-subvi-overhead.html`
- source_url: https://docs-be.ni.com/bundle/labview-nxg-creating-first-application/raw/resource/enus/minimize-subvi-overhead.html
- document_id: `labview-nxg-creating-first-application`
- page_type: `leaf`
- content_type: `task`
- source_description: Inlining a subVI into its calling VIs helps minimize the overhead associated with calling the subVI. When you inline a subVI, G Web Development Software inserts the compiled code of the subVI into the compiled code of the calling VI. If you then make changes to the subVI, G Web Development Software

Minimizing SubVI Overhead

Inlining a subVI into its calling VIs helps minimize the overhead associated with calling
 the subVI.

When you inline a subVI, G Web Development Software
 inserts the compiled code of the subVI into the compiled code of the
 calling VI. If you then make changes to the subVI, G Web Development Software
 recompiles all calling VIs of that subVI to include those changes.
 Essentially, inlining a subVI removes the need to call the subVI at
 run time. Instead, the subVI code executes inside the compiled code
 of the calling VI.

A subVI that you want to inline cannot have any of the following
 characteristics:

- Contains recursion
- Contains certain diagram nodes, such as control references.
 These nodes generate edit-time error messages if you enable
 subVI inlining.

Complete the following steps to inline a
 subVI.

1. On the Document tab, in the
 Behavior section, click
 Properties to access the
 property settings for the subVI.
2. Place a checkmark in the Inline subVI into calling
 VIs checkbox.
3. Set VI Reentrancy to
 Stateless or
 Stateful to configure
 reentrant execution.
4. Click OK.

Parent topic:

Creating a WebVI

Parent topic:

SubVIs

<!--NI_TOPIC bundle=labview-nxg-creating-first-application path=resizing-data-sets-to-open-in-analysis-panels.html language=enus -->
## TOPIC 00010: Resizing Data Sets to Open in Analysis Panels

- bundle_id: `labview-nxg-creating-first-application`
- source_path: `resizing-data-sets-to-open-in-analysis-panels.html`
- source_url: https://docs-be.ni.com/bundle/labview-nxg-creating-first-application/raw/resource/enus/resizing-data-sets-to-open-in-analysis-panels.html
- document_id: `labview-nxg-creating-first-application`
- page_type: `leaf`
- content_type: `task`
- source_description: If you need to open a large data set in an analysis panel, you must first trim the data to a smaller size. Analysis panels have the following upper limits to the amount of data they can process: 1 million samples per channel when you launch analysis panels from the Interactive Analysis section 9 MB

Resizing Data Sets to Open in Analysis Panels

If you need to open a large data set in an analysis panel, you must first trim the data to a smaller size.

- 1 million samples per channel when you launch analysis panels from the 
 Interactive Analysis section
- 9 MB total file size when you select a data set from the 
 Input Signal pull-down menu of an analysis panel

Complete the following steps to resize a data set:

1. Double-click the data item to open it in the workspace and use the thumbnail view to select a subset of the data.
2. Click 
 Crop to Frame to create a new capture of the subset. 
 If the subset meets the upper limits criteria, you can open the subset in an analysis panel.

Parent topic:

Creating Your First Application

<!--NI_TOPIC bundle=labview-nxg-creating-first-application path=subvi-from-selection.html language=enus -->
## TOPIC 00011: Creating a SubVI from a Section of Existing Code

- bundle_id: `labview-nxg-creating-first-application`
- source_path: `subvi-from-selection.html`
- source_url: https://docs-be.ni.com/bundle/labview-nxg-creating-first-application/raw/resource/enus/subvi-from-selection.html
- document_id: `labview-nxg-creating-first-application`
- page_type: `leaf`
- content_type: `task`
- source_description: Select the section of code you want to reuse. Click EditCreate subVI from selection to generate a new .gvi file in the project. To open this file, double-click the corresponding subVI node that contains the section of code you selected. The subVI diagram and connector pane include inputs and outputs

Creating a SubVI from a Section of Existing Code

1. Select the section of code you want to reuse.
2. Click 
 Edit»Create subVI from selection to generate a new 
 .gvi file in the project. 
 To open this file, double-click the corresponding subVI node that contains the section of code you selected. The subVI diagram and connector pane include inputs and outputs for every wire that enters and exits the section of code. The panel automatically includes the corresponding controls and indicators. 
 org.dita.html5/xsl/topic.xsl 455Tip To disable automatically placing items on the panel, click 
 File»Preferences, select the 
 VI tab, and disable 
 Place items on the panel when creating subVI from selection.
3. Rename and save the new 
 .gvi file. 
 Choose a name that describes what function the VI performs so that other users can clearly understand any diagram that uses the VI as a subVI.

To add the new subVI as a node on other diagrams, locate the subVI in the 
 Project Files tab and drag it to the diagram where you want to use it.

Note

Parent topic:

Creating a WebVI

<!--NI_TOPIC bundle=labview-nxg-creating-first-application path=using-analysis-panels-to-process-data.html language=enus -->
## TOPIC 00012: Customizing Analysis Functions Using Interactive Graphs

- bundle_id: `labview-nxg-creating-first-application`
- source_path: `using-analysis-panels-to-process-data.html`
- source_url: https://docs-be.ni.com/bundle/labview-nxg-creating-first-application/raw/resource/enus/using-analysis-panels-to-process-data.html
- document_id: `labview-nxg-creating-first-application`
- page_type: `leaf`
- content_type: `task`
- source_description: Use visualized data to configure filters, frequency domain transfers, and statistical analysis functions and create a customized node that you can use in your code. Locate or place one of the following analysis nodes on the diagram of a VI. Analysis Function Description Amplitude Measurements Perfor

Customizing Analysis Functions Using Interactive Graphs

Use visualized data to configure filters, frequency domain transfers, and statistical analysis functions and create a customized node that you can use in your code.

1. Locate or place one of the following analysis nodes on the diagram of a VI. 
 Analysis FunctionDescriptionAmplitude Measurements
 Performs peak amplitude measurement.Curve Fit
 Finds the line that best represents an input signal or input data set using a specific fitting method.FFT Spectrum
 Computes the averaged FFT spectrum of a signal.Filter
 Applies a lowpass, highpass, bandpass, or bandstop filter to a signal.Histogram
 Finds the discrete histogram of a signal.Limit Testing
 Performs limit testing by comparing the signal to upper and lower limits that you define.Pulse and Transition Measurements
 Returns various measurements of a specific pulse in a periodic waveform or an array of periodic waveforms, such as the period, pulse duration, and duty cycle.Resample
 Resamples a signal according to a specific delay and sampling interval.Scaling and Mapping
 Scales a signal based on a straight line.Signal Correlation
 Computes the auto correlation of a signal or cross correlation of two signals.Statistics
 Performs statistical calculations on a signal.Tone Measurements
 Finds tones with specific amplitude and frequency parameters.
2. Select the node and click 
 Analysis panel on the 
 Item tab.
3. Adjust the variables of the analysis node until it meets the requirements of your application. 
 
 The graph updates in real time to show sample data and the data resulting from the analysis function. Click 
 Capture & view data in the top right corner to view only the data that the function produces with the current configuration.
  1. Above the graph, choose between a sample input and any valid data item that you previously captured and saved in the project.
  2. To the right of the graph, adjust the inputs of the node.
4. Open the 
 Configured Code pane at the bottom of the analysis panel to view the customized node that corresponds to the function. To update the configuration of the node on the diagram, click 
 Update node. If you want to create a new node with the current configuration, click 
 Copy to Clipboard and then paste the new node onto the diagram.

Parent topic:

Creating Your First Application

<!--NI_TOPIC bundle=labview-nxg-creating-first-application path=vi-reentrancy.html language=enus -->
## TOPIC 00013: VI Reentrancy

- bundle_id: `labview-nxg-creating-first-application`
- source_path: `vi-reentrancy.html`
- source_url: https://docs-be.ni.com/bundle/labview-nxg-creating-first-application/raw/resource/enus/vi-reentrancy.html
- document_id: `labview-nxg-creating-first-application`
- page_type: `leaf`
- content_type: `concept`
- source_description: You can choose from three VI reentrancy options that determine how your subVI executes when it is called at more than one point in the dataflow at the same time. Reentrancy is the simultaneous execution of multiple calls for a subVI. By default, each call to the subVI is executed one after another.

VI Reentrancy

You can choose from three VI reentrancy options that determine how your subVI executes when it is called at more than one point in the dataflow at the same time. Reentrancy is the simultaneous execution of multiple calls for a subVI.

By default, each call to the subVI is executed one after another. This may cause your application to execute slowly or have unexpected behavior. To allow multiple calls to a subVI to execute simultaneously, set a reentrant execution state for the subVI.

Refer to the following table to determine which VI reentrancy option is best for your subVI.

| What your subVI needs | Option(s) to use |
| --- | --- |
| Ability to maintain state | Stateful maintains state for each instance of the subVI. None maintains a single state across all instances of the subVI. |
| Minimize wait time when multiple VIs call your subVI at the same time | Stateful eliminates wait time completely. Stateless results in wait time if there are more calls to the subVI than there are clones. However, the wait time is always within a certain range. |
| Determinism, or the same wait time for each call to the subVI | Stateful guarantees the same exact wait time for each call to the subVI. This minimizes jitter in applications involving time-sensitive data. |
| Minimize memory usage | None uses the least memory. Stateless uses less memory than Stateful if your subVI needs the other features of reentrancy. |
| Minimize call overhead | Stateful is the most efficient for calling a subVI many times, such as within a loop. |

Parent topic:

Creating a WebVI

Parent topic:

SubVIs

<!--NI_TOPIC bundle=labview-nxg-creating-first-application path=what-is-a-subvi.html language=enus -->
## TOPIC 00014: SubVIs

- bundle_id: `labview-nxg-creating-first-application`
- source_path: `what-is-a-subvi.html`
- source_url: https://docs-be.ni.com/bundle/labview-nxg-creating-first-application/raw/resource/enus/what-is-a-subvi.html
- document_id: `labview-nxg-creating-first-application`
- page_type: `leaf`
- content_type: `concept`
- source_description: After you build a VI, you can call it from the diagram of another VI within the same project. A VI called from the diagram of another VI is a subVI. SubVIs contain reusable code and simplify the diagrams of calling VIs. SubVIs are analogous to functions or subroutines in other programming languages.

SubVIs

After you build a VI, you can call it from the diagram of another VI within the same project. 
 A VI called from the diagram of another VI is a 
 *subVI*. SubVIs contain reusable code and simplify the diagrams of calling VIs. SubVIs are analogous to functions or subroutines in other programming languages.

When you add an instance of a subVI to the diagram of another VI, the subVI appears as a single node, similar to a node from the palette. When data in the calling VI reaches the subVI node, the software executes the diagram of the subVI.

The following diagram shows two common situations that benefit from subVIs.

[IMAGE alt='1378' src='GUID-4901C208-BA72-45FF-81C7-D511777122AF-a5.png']

1. Users may have difficulty understanding the purpose of this section of code because it performs several operations. The more complex a diagram, the more time it takes to interpret sections of code.
2. The same code appears in two different places. Repeated code increases the likelihood of errors. For example, if you change one section of repeated code, you must remember to make the same change everywhere the code section occurs.

The following diagram shows two solutions that subVIs provide.

[IMAGE alt='1378' src='GUID-D10F49F5-A9AF-4187-B639-D13733311C30-a5.png']

1. The Coin Flip subVI represents the highlighted code inside the For Loop of the previous diagram. The subVI simplifies the diagram and communicates the purpose of the code through its label and node icon.
2. The Percentage subVI represents one of the duplicate sections of highlighted code from the previous diagram. The Percentage subVI performs the same function in two places without repeating code. If you change code in the VI called by the Percentage subVI, both instances of the subVI change.

Parent topic:

Creating a WebVI

Parent topic:

Programming in G
