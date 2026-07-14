# NI DOCUMENT BUNDLE: labview-desktop-execution-trace-toolkit

<!--NI_BUNDLE_CHUNK bundle=labview-desktop-execution-trace-toolkit start=1 end=28 -->
<!--NI_TOPIC bundle=labview-desktop-execution-trace-toolkit path=comparing-trace-data.html language=enus -->
## TOPIC 00001: Comparing Trace Data

- bundle_id: `labview-desktop-execution-trace-toolkit`
- source_path: `comparing-trace-data.html`
- source_url: https://docs-be.ni.com/bundle/labview-desktop-execution-trace-toolkit/raw/resource/enus/comparing-trace-data.html
- document_id: `labview-desktop-execution-trace-toolkit`
- page_type: `leaf`
- content_type: `task`
- source_description: You can compare two trace sessions of the same trace or different traces by using the Compare Traces window. Click Compare Traces on the View tab to display the Compare Traces window. Select the trace sessions you want to compare from the Session Name pull-down menus. If the menus do not contain a s

### Comparing Trace Data

You can compare two trace sessions of the same trace or different traces
 by using the Compare Traces window.

1. Click Compare Traces on the View tab to
 display the Compare Traces window.
2. Select the trace sessions you want to compare from the Session
 Name pull-down menus. If the menus do not contain a session you want to
 compare and you know the session exists in the current trace, click the refresh button or
 press <F5> to refresh the Session Name pull-down menu. 
 Note If you want to compare
 sessions of two different traces, make sure both traces are open.
3. To compare part of a trace session, enter orders of execution of the first
 and last event you want to compare in the
 Begin Index or
 End Index field.
4. Click Compare in the middle of this window. The Desktop Execution Trace
 Toolkit loads the trace sessions you selected and starts comparison. After the
 comparison finishes, the toolkit highlights the differences in the table pane for
 each selected session.
5. Click the Next or Previous button to navigate to the next or previous difference.
6. Click a difference to view the details in the details pane for each
 selected session. You also can use the table pane shortcut menu to navigate to call
 chain VIs or hide specific columns.

To compare different parts of the same trace, you also can click Split on the View tab to split the current trace into two displays and scroll to the sessions you want to compare in the two displays.

Parent topic:

Desktop Execution Trace Concepts

Related information::

- Part 6: Comparing Trace Data

<!--NI_TOPIC bundle=labview-desktop-execution-trace-toolkit path=configuring-a-trace-session.html language=enus -->
## TOPIC 00002: Configuring a Trace Session

- bundle_id: `labview-desktop-execution-trace-toolkit`
- source_path: `configuring-a-trace-session.html`
- source_url: https://docs-be.ni.com/bundle/labview-desktop-execution-trace-toolkit/raw/resource/enus/configuring-a-trace-session.html
- document_id: `labview-desktop-execution-trace-toolkit`
- page_type: `leaf`
- content_type: `task`
- source_description: After you open a trace connection, you can specify types of execution events you want to capture to reduce the memory the Desktop Execution Trace Toolkit uses and avoid running out of memory. The configuration you specify is specific to the application instance you select on the Home tab. If you cli

### Configuring a Trace Session

After you open a trace connection, you can specify types of execution events you want to
 capture to reduce the memory the Desktop Execution Trace Toolkit uses and avoid running out
 of memory.

The configuration you specify is specific to the application instance you select on
 the Home tab. If you click New Trace on
 the Home tab to open a trace for another application instance,
 the trace session configuration reverts to the default.

You can use one of the following methods to configure trace sessions:

- If you want to quickly select event types without specifying detailed events,
 complete the following steps: 
 Click the arrow below Capture Settings to display
 the Capture Settings pull-down menu.
 Place checkmarks in the checkboxes for the events you want to trace. By
 default, the Desktop Execution Trace Toolkit traces all execution events
 except timeout events of the Event structure type and memory allocation
 events.
 You can enable the Memory
 Threshold option by placing a checkmark in the
 Memory Allocations checkbox. Use this option
 to avoid capturing small memory allocation events, such as allocations
 LabVIEW makes internally, that do not have significant impact on the
 application you are tracing. For example, you can use this option to
 ignore memory allocations of less than 1,000 bytes.
 Click the table pane to apply the configuration settings.
- If you want to specify not only event types but also detailed events, complete
 the following steps: 
 Click the Capture Settings image to display
 the Capture Settings dialog box. By default,
 the Desktop Execution Trace Toolkit traces all execution events
 except timeout events of the Event structure type and memory
 allocation events.
 Note The
 Capture Settings dialog box
 automatically updates for the configurations you specify in the
 Capture Settings pull-down menu.
 Select an item in the type list to display the corresponding page of
 this dialog box.
 Place checkmarks in the checkboxes for the events you want to
 trace.
 Click Save to save the
 capture settings in a configuration settings (.ini)
 file or click Load to load an existing
 configuration file so that you can share trace session configurations
 between traces.
 Click OK to apply the configuration settings and
 close the Capture Settings dialog box.

Enter the tasks the user should do after finishing this task (optional).

Parent topic:

Desktop Execution Trace Concepts

Related concepts:

- Opening a Trace Connection

Related tasks:

- Part 2: Configuring a Trace Session

<!--NI_TOPIC bundle=labview-desktop-execution-trace-toolkit path=configuring-the-labview-vi-server.html language=enus -->
## TOPIC 00003: Part 2: Configuring a Trace Session

- bundle_id: `labview-desktop-execution-trace-toolkit`
- source_path: `configuring-the-labview-vi-server.html`
- source_url: https://docs-be.ni.com/bundle/labview-desktop-execution-trace-toolkit/raw/resource/enus/configuring-the-labview-vi-server.html
- document_id: `labview-desktop-execution-trace-toolkit`
- page_type: `leaf`
- content_type: `task`
- source_description: In Part 1 of this tutorial, you open a trace connection between the toolkit and the example project you want to trace. In Part 2 of this tutorial, you configure a trace session for the trace connection you opened in Part 1. In the Desktop Execution Trace Toolkit, click the arrow below Capture Settin

### Part 2: Configuring a Trace Session

In Part 1 of this tutorial, you open a trace connection between the toolkit and the
 example project you want to trace. In Part 2 of this tutorial, you configure a trace session for
 the trace connection you opened in Part 1.

1. In the Desktop Execution Trace Toolkit, click the arrow below Capture
 Settings to display the Capture Settings pull-down
 menu, in which you can quickly select the event types you want to trace.
2. Place a checkmark in the Memory Allocations checkbox to capture
 memory allocation events.
3. You can enter a value in the Memory Threshold field to avoid
 capturing small memory allocation events. For example, you can use this option to ignore
 memory allocations of less than 1,000 bytes. In this example, use the default
 configuration. 
 Tip Selecting only the types you want to trace and specifying a reasonable
 memory threshold can improve the efficiency of memory usage and save time analyzing
 trace data.
4. Click the Capture Settings image to launch the Capture
 Settings dialog box, in which you can select the detailed events you want to
 trace for the types you select on the Capture Settings pull-down
 menu.
5. Hover over the
 head
 of this dialog box, the toolkit displays an illustration about the capturing process. Make
 sure you understand the illustration. The toolkit does not capture the events you deselect
 in the dialog box. Select only the events you want to trace so that you can reduce the
 amount of data that the toolkit must process and that you must analyze. 
 Tip To capture a specific event but temporarily prevent the table pane from
 displaying the event, you can filter the trace data after you execute a trace
 session.
6. Double-check that the Memory Allocations checkbox contains a
 checkmark. The Capture Settings dialog box automatically updates for
 the configurations you specify in the Capture Settings pull-down
 menu.
7. Click OK to apply the capture settings and close the
 Capture Settings dialog box.

After you configure a trace session for Desktop Execution Trace Toolkit.lvproj, you can
 execute the trace session in Part 3 of this tutorial.

Parent topic:

Get Started with an Example

Related concepts:

- Opening a Trace Connection

Related tasks:

- Configuring a Trace Session
- Part 5: Filtering Trace Data

<!--NI_TOPIC bundle=labview-desktop-execution-trace-toolkit path=configuring-the-lv-vi-server.html language=enus -->
## TOPIC 00004: Configuring the LabVIEW VI Server

- bundle_id: `labview-desktop-execution-trace-toolkit`
- source_path: `configuring-the-lv-vi-server.html`
- source_url: https://docs-be.ni.com/bundle/labview-desktop-execution-trace-toolkit/raw/resource/enus/configuring-the-lv-vi-server.html
- document_id: `labview-desktop-execution-trace-toolkit`
- page_type: `leaf`
- content_type: `task`
- source_description: The Desktop Execution Trace Toolkit uses the LabVIEW VI Server to connect to the applications on which you execute trace sessions, including VIs, LabVIEW projects, stand-alone applications, and shared library files. If you want to debug stand-alone applications or shared library files, you must conf

### Configuring the LabVIEW VI Server

The Desktop Execution Trace Toolkit uses the LabVIEW VI Server to connect to the
 applications on which you execute trace sessions, including VIs, LabVIEW projects,
 stand-alone applications, and shared library files.

Note

If you try to open a trace connection and you receive a message that LabVIEW VI
 Server access is not enabled, complete the following steps to enable VI Server
 access:

1. In LabVIEW on the computer where the application to trace runs, select Tools»Options from the menu bar to display the Options
 dialog box.
2. Select VI Server from the Category
 list to display the VI Server page.
3. Complete the following steps to enable VI Server:
  1. Place a checkmark in the TCP/IP checkbox.
  2. Optional: 
 If you are tracing a VI or LabVIEW project that is part of a
 stand-alone application or shared library file, complete the following
 steps: 
 Change the default port value (3363)
 to a unique TCP/IP port number in the
 Port field.
 Note You can
 specify any integer as a port number, but National
 Instruments recommends specifying a unique port for each
 application or shared library file you build. Because the
 Desktop Execution Trace Toolkit captures all the data on a
 given TCP/IP port, having multiple application instances on
 a single port can cause the toolkit to capture data that
 does not pertain to the application or shared library file
 you want to trace.
 Return to the Desktop Execution Trace Toolkit.
 In the Port field on the
 Home tab, enter the port number you
 specified when you configured the LabVIEW VI Server.
 Return to the VI Server page of the
 Options dialog box in LabVIEW.
4. Complete the following steps to grant machine access:
  - If you are tracing applications on a local computer, complete the
 following steps:
    1. Confirm that the Machine access list on the
 VI Server page includes the name
 localhost or the address
 127.0.0.1 . If it does not, click
 Add to enable the Machine
 name/address field and enter localhost or 127.0.0.1.
 The toolkit uses this name or address to communicate with the
 applications you trace.
    2. Click OK to close the
 Options dialog box and apply the
 configuration settings.
  - If you are tracing applications on a remote computer, complete the
 following steps:
    1. In the Machine Access section of the
 VI Server page, click
 Add to enable the Machine
 name/address field.
    2. In the Machine name/address field, enter the
 IP address or name of the computer where the Desktop Execution Trace
 Toolkit runs.
    3. Click OK to close the
 Options dialog box and apply the
 configuration settings.
    4. Return to the local computer where the Desktop Execution Trace
 Toolkit runs.
    5. In the Machine field on the
 Home tab, specify the IP address or name of
 the computer where LabVIEW runs.
5. Retry opening the trace connection.

Parent topic:

Desktop Execution Trace Concepts

<!--NI_TOPIC bundle=labview-desktop-execution-trace-toolkit path=executing-a-trace-session.html language=enus -->
## TOPIC 00005: Executing a Trace Session

- bundle_id: `labview-desktop-execution-trace-toolkit`
- source_path: `executing-a-trace-session.html`
- source_url: https://docs-be.ni.com/bundle/labview-desktop-execution-trace-toolkit/raw/resource/enus/executing-a-trace-session.html
- document_id: `labview-desktop-execution-trace-toolkit`
- page_type: `leaf`
- content_type: `task`
- source_description: After you open a trace connection, you can execute a trace session to capture the data. Complete the following steps to execute a trace session. Click Start on the Home tab or press <Ctrl-R> to start the trace session and begin tracing data. In LabVIEW, run the application you want to trace. If you

### Executing a Trace Session

After you open a trace connection, you can execute a trace session to capture the data.
 Complete the following steps to execute a trace session.

1. Click Start on the Home tab or
 press <Ctrl-R> to start the trace session and begin tracing data.
2. In LabVIEW, run the application you want to trace. If you want to trace a
 stand-alone application, run the executable. The table pane of the Desktop
 Execution Trace Toolkit displays the execution events you selected when you
 configured the trace session. You also can filter trace data that appears in the
 table pane to make the table easier to read.
3. When you finish tracing data, click Stop or press
 <Ctrl-T> to end the trace session.

.txt

Parent topic:

Desktop Execution Trace Concepts

Related concepts:

- Reviewing Trace Data
- Opening a Trace Connection
- Saving or Exporting Trace Data

Related tasks:

- Part 4: Reviewing Trace Data
- Configuring a Trace Session

<!--NI_TOPIC bundle=labview-desktop-execution-trace-toolkit path=filter-trace-data.html language=enus -->
## TOPIC 00006: Filtering Trace Data

- bundle_id: `labview-desktop-execution-trace-toolkit`
- source_path: `filter-trace-data.html`
- source_url: https://docs-be.ni.com/bundle/labview-desktop-execution-trace-toolkit/raw/resource/enus/filter-trace-data.html
- document_id: `labview-desktop-execution-trace-toolkit`
- page_type: `leaf`
- content_type: `task`
- source_description: Interact with events in the Configure Displayed Events dialog box to temporarily filter the trace data you do not need from the table pane. Complete the following steps to display and interact with the Configure Displayed Events dialog box: In the table pane, click Filter Settings on the View tab to

### Filtering Trace Data

Interact with events in the Configure Displayed Events dialog box to
 temporarily filter the trace data you do not need from the table pane.

Configure Displayed Events

1. In the table pane, click Filter Settings on the
 View tab to display the Configure Displayed
 Events dialog box. The type list displays the different sources
 of trace events. 
 Note The dialog box is not
 available when the table pane does not display any events to filter.
2. Select an item in the type list to display the corresponding page of the dialog
 box. Each page includes a list of events that you can choose to filter. You can
 select or deselect events so they appear or do not appear in the table pane. You
 also can deselect entire types in the type list to filter all the events of that
 type.
3. Optional: 
 Click Save to save the filter settings in a
 configuration settings (.ini) file or click
 Load to load an existing configuration file so that
 you can share filter settings between traces.
4. Click Ok to close the Configure Displayed
 Events dialog box and apply the filter. 
 Tip You can quickly filter the events that occur in a specified VI
 by right-clicking the VI and selecting Filter this VI from
 Display from the shortcut menu.

Filtering events prevents those events from appearing in the table pane. However, the
 Desktop Execution Trace Toolkit continues to trace filtered events. If you are sure
 that you do not need to use specific events at all, deselect them from the
 Capture Settings dialog box to reduce the amount of memory
 that the toolkit uses.

Tip

You can use the Configure Displayed Events dialog box to filter
 or display events at any time, regardless of whether the toolkit is tracing data.
 The table pane updates to match the new configuration settings each time you click
 OK in the Configure Displayed Events
 dialog box. You also can click Reset Filter to remove all
 event filters.

Parent topic:

Reviewing Trace Data

Related tasks:

- Part 5: Filtering Trace Data

<!--NI_TOPIC bundle=labview-desktop-execution-trace-toolkit path=getting-started.html language=enus -->
## TOPIC 00007: Get Started with an Example

- bundle_id: `labview-desktop-execution-trace-toolkit`
- source_path: `getting-started.html`
- source_url: https://docs-be.ni.com/bundle/labview-desktop-execution-trace-toolkit/raw/resource/enus/getting-started.html
- document_id: `labview-desktop-execution-trace-toolkit`
- page_type: `leaf`
- content_type: `concept`
- source_description: This book contains step-by-step instructions to help you get started with the Desktop Execution Trace Toolkit by using the LabVIEW example project Desktop Execution Trace Toolkit.lvproj in the labview\examples\Desktop Execution Trace directory. This tutorial assumes you have fundamental knowledge ab

### Get Started with an Example

This book contains step-by-step instructions to help you get started with the Desktop
 Execution Trace Toolkit by using the LabVIEW example project Desktop Execution Trace
 Toolkit.lvproj in thelabview\examples\Desktop Execution
 Trace directory. This tutorial assumes you have fundamental knowledge about
 using LabVIEW.

#### Benefits of Using the Desktop
 Execution Trace Toolkit

Debugging and optimizing applications may be
 tedious, time-consuming, and expensive. Even if code is syntactically correct and
 functionally complete, the code may still contain problems. Such problems as
 reference leaks can impact performance or lead to incorrect or unexpected behaviors.
 These oversights can be difficult to reproduce and even more difficult to locate,
 especially in large and complex applications.

The Desktop Execution Trace
 Toolkit can provide details about execution events that LabVIEW generates when
 executing an application and the context in which events occur.

Use this
 toolkit to:

- reduce the time to track down undesirable behaviors
- detect memory and reference leaks
- isolate the source of a specific event
- identify the last call before an error
- ensure that the execution of an application is the same on different
 targets

- [Part 1: Opening a Trace Connection](part-1-opening-a-trace-connection.html) In Part 1 of this tutorial, you open a trace connection between the Desktop Execution Trace Toolkit and the example project Desktop Execution Trace Toolkit.lvproj , before you begin a trace session.
- [Part 2: Configuring a Trace Session](configuring-the-labview-vi-server.html) In Part 1 of this tutorial, you open a trace connection between the toolkit and the example project you want to trace. In Part 2 of this tutorial, you configure a trace session for the trace connection you opened in Part 1.
- [Part 3: Executing a Trace Session](part-2-configuring-a-trace-session.html) In Part 2 of this tutorial, you configure the trace data you want to acquire from Desktop Execution Trace Toolkit.lvproj for a trace session. In Part 3 of this tutorial, you execute the trace session and capture the trace data.
- [Part 4: Reviewing Trace Data](part-3-executing-a-trace-session.html) In Part 3 of this tutorial, you execute the trace session and capture the trace data from Desktop Execution Trace Toolkit.lvproj . In Part 4 of this tutorial, you review the trace data that the Desktop Execution Trace Toolkit captures and displays in the table pane.
- [Part 5: Filtering Trace Data](part-4-reviewing-trace-data.html) In Part 4 of this tutorial, you review the trace data that the Desktop Execution Trace Toolkit captures from Desktop Execution Trace Toolkit.lvproj . You may notice that executing a trace session even on a small application can capture hundreds of execution events. In Part 5 of this tutorial, you execute a second trace session and filter the events that the table pane displays to make the table pane easier to read.
- [Part 6: Comparing Trace Data](part-5-filtering-trace-data.html) In Part 5 of this tutorial, you execute a second trace session and filter the trace data in the table pane. In Part 6 of this tutorial, you can either split the table pane or use the Compare Traces window to compare the traces you executed in previous parts of this tutorial.
- [Part 7: Saving or Exporting Trace Data](part-6-comparing-trace-data.html) In Part 6 of this tutorial, you compare the trace sessions that you executed in Part 3 and Part 5 of this tutorial. In Part 7 of this tutorial, you save or export the trace file.

<!--NI_TOPIC bundle=labview-desktop-execution-trace-toolkit path=highlighting-paired-events.html language=enus -->
## TOPIC 00008: Highlighting Paired Events

- bundle_id: `labview-desktop-execution-trace-toolkit`
- source_path: `highlighting-paired-events.html`
- source_url: https://docs-be.ni.com/bundle/labview-desktop-execution-trace-toolkit/raw/resource/enus/highlighting-paired-events.html
- document_id: `labview-desktop-execution-trace-toolkit`
- page_type: `leaf`
- content_type: `task`
- source_description: After you select an event, right-click the table pane and select Highlight Paired Events from the shortcut menu to find whether an event is paired with the event you selected. For example, VI Start Execution and VI Stop Execution are paired events. The Desktop Execution Trace Toolkit also displays t

### Highlighting Paired Events

After you select an event, right-click the table pane and select Highlight
 Paired Events from the shortcut menu to find whether an event is paired with
 the event you selected.

For example, VI Start Execution and VI Stop Execution are paired events. The Desktop
 Execution Trace Toolkit also displays the duration between the two paired events in
 the details pane.

Parent topic:

Reviewing Trace Data

<!--NI_TOPIC bundle=labview-desktop-execution-trace-toolkit path=memory-considerations.html language=enus -->
## TOPIC 00009: Memory Considerations

- bundle_id: `labview-desktop-execution-trace-toolkit`
- source_path: `memory-considerations.html`
- source_url: https://docs-be.ni.com/bundle/labview-desktop-execution-trace-toolkit/raw/resource/enus/memory-considerations.html
- document_id: `labview-desktop-execution-trace-toolkit`
- page_type: `leaf`
- content_type: `concept`
- source_description: The Desktop Execution Trace Toolkit stores trace data in memory. By default, you can keep at most 100,000 events in the toolkit. If you reach the memory buffer limit, the toolkit removes the oldest events from memory and overwrites the oldest data in the table pane. Therefore, the table pane always

### Memory Considerations

The Desktop Execution Trace Toolkit stores trace data in memory. By default, you can keep
 at most 100,000 events in the toolkit.

If you reach the memory buffer limit, the toolkit removes the oldest events from memory
 and overwrites the oldest data in the table pane. Therefore, the table pane always
 contains the latest trace data.

Tip

Data

Stop Tracing

When Exceed Limit

When you trace large applications or execute long trace sessions, you can use the
 following techniques to improve the efficiency of the memory buffer.

- Increase the memory buffer limit—Click the Data tab and
 change the default number in the Maximum Events field. Ensure
 that the maximum value is adequate for the applications you want to trace so that
 you do not lose any trace data.
- Deselect unused events—Click Capture Settings on the
 Home tab to select only relevant events or types so that
 you can avoid using excessive memory.
- Enable logging trace data—Select Enable Logging on the
 Data tab, specify a log file, and select
 Discard Oldest from the When Exceed
 Limit pull-down menu. When you execute a trace session indefinitely,
 the Desktop Execution Trace Toolkit logs all the trace data to the log file so that
 you can view all the trace data later and do not need to worry about the toolkit
 running out of memory.

Parent topic:

Desktop Execution Trace Concepts

Related tasks:

- Configuring a Trace Session
- Executing a Trace Session

<!--NI_TOPIC bundle=labview-desktop-execution-trace-toolkit path=navigating-to-trace-sessions.html language=enus -->
## TOPIC 00010: Navigating to Trace Sessions

- bundle_id: `labview-desktop-execution-trace-toolkit`
- source_path: `navigating-to-trace-sessions.html`
- source_url: https://docs-be.ni.com/bundle/labview-desktop-execution-trace-toolkit/raw/resource/enus/navigating-to-trace-sessions.html
- document_id: `labview-desktop-execution-trace-toolkit`
- page_type: `leaf`
- content_type: `concept`
- source_description: The Desktop Execution Trace Toolkit displays all the trace data for an application instance in one display. Every time you click Start to execute a trace session, the toolkit appends the trace data of the trace session to the current trace data in the table pane and displays a bookmark for the trace

### Navigating to Trace Sessions

The Desktop Execution Trace Toolkit displays all the trace data for an application
 instance in one display.

Every time you click Start to execute a trace session, the toolkit
 appends the trace data of the trace session to the current trace data in the table pane
 and displays a bookmark for the trace session on the vertical scroll bar. You can
 quickly navigate to the first event of a trace session by clicking the bookmark.

Parent topic:

Reviewing Trace Data

<!--NI_TOPIC bundle=labview-desktop-execution-trace-toolkit path=navigating-to-vis.html language=enus -->
## TOPIC 00011: Navigating to VIs

- bundle_id: `labview-desktop-execution-trace-toolkit`
- source_path: `navigating-to-vis.html`
- source_url: https://docs-be.ni.com/bundle/labview-desktop-execution-trace-toolkit/raw/resource/enus/navigating-to-vis.html
- document_id: `labview-desktop-execution-trace-toolkit`
- page_type: `leaf`
- content_type: `task`
- source_description: The Desktop Execution Trace Toolkit to easily move between trace events in the toolkit and VIs in LabVIEW. Use one of the following methods to navigate to a VI related with the event you select: Double-click an event in the table pane. The toolkit opens the VI where the event occurs in LabVIEW. If t

### Navigating to VIs

The Desktop Execution Trace Toolkit to easily move between trace events in the toolkit
 and VIs in LabVIEW.

Use one of the following methods to navigate to a VI
 related with the event you select:

- Double-click an event in the table pane. The toolkit opens the VI where the
 event occurs in LabVIEW. If the Highlight column for the
 event displays Object, the toolkit also highlights the
 object related to the event in the VI.
- Select an event in the table pane and click Navigate on
 the View tab.
- Right-click the table pane and select Navigate to Call Chain
 VIs from the shortcut menu. The toolkit displays a submenu which
 contains the chain of callers, from the current VI to the top-level. VI. Select
 the specific VI you need to navigate to from the submenu.

Parent topic:

Reviewing Trace Data

<!--NI_TOPIC bundle=labview-desktop-execution-trace-toolkit path=opening-a-trace-connectin.html language=enus -->
## TOPIC 00012: Opening a Trace Connection

- bundle_id: `labview-desktop-execution-trace-toolkit`
- source_path: `opening-a-trace-connectin.html`
- source_url: https://docs-be.ni.com/bundle/labview-desktop-execution-trace-toolkit/raw/resource/enus/opening-a-trace-connectin.html
- document_id: `labview-desktop-execution-trace-toolkit`
- page_type: `leaf`
- content_type: `concept`
- source_description: You can open a trace connection from the toolkit or from a LabVIEW VI or project. Before you can execute a trace session, you must open a trace connection between the Desktop Execution Trace Toolkit and the LabVIEW application instance in which the application you want to debug runs. If you did not

### Opening a Trace Connection

You can open a trace connection from the toolkit or from a LabVIEW VI or
 project.

Before you can execute a trace session, you must open a trace connection between
 the Desktop Execution Trace Toolkit and the LabVIEW application instance in
 which the application you want to debug runs.

Note

After you open a trace connection to a LabVIEW application instance, you can
 configure and execute trace sessions on applications running in that
 instance.

- [Opening a Trace Connection from LabVIEW](opening-a-trace-connection-lv.html) Within labVIEW, you can open a trace connection whether you are working on a VI or on a project.
- [Opening a Trace Connection from the Desktop Execution Trace Toolkit](opening-a-trace-connection-dett.html) In the Desktop Execcution Trace Toolkit, you can complete the following steps to open a trace connection to a LabVIEW application instance.

Parent topic:

Desktop Execution Trace Concepts

Related tasks:

- Configuring the LabVIEW VI Server
- Opening a Trace Connection from LabVIEW

<!--NI_TOPIC bundle=labview-desktop-execution-trace-toolkit path=opening-a-trace-connection-dett.html language=enus -->
## TOPIC 00013: Opening a Trace Connection from the Desktop Execution Trace Toolkit

- bundle_id: `labview-desktop-execution-trace-toolkit`
- source_path: `opening-a-trace-connection-dett.html`
- source_url: https://docs-be.ni.com/bundle/labview-desktop-execution-trace-toolkit/raw/resource/enus/opening-a-trace-connection-dett.html
- document_id: `labview-desktop-execution-trace-toolkit`
- page_type: `leaf`
- content_type: `task`
- source_description: In the Desktop Execcution Trace Toolkit, you can complete the following steps to open a trace connection to a LabVIEW application instance. Open the application instance in LabVIEW before you complete the following steps:If you want to open a trace connection to a stand-alone application or a shared

### Opening a Trace Connection from the Desktop
 Execution Trace Toolkit

In the Desktop Execcution Trace Toolkit, you can complete the following steps to open a
 trace connection to a LabVIEW application instance.

Note

1. Specify the computer name or IP address in the Machine
 field on the Home tab. 
 If you are tracing applications on a local computer, confirm that the
 Machine field displays the name of your local
 computer.
 If you are tracing applications on a remote computer, enter the IP
 address or name of the remote computer where the applications you are
 debugging run.
2. Ensure that the port number in the Port field is the
 same as the number you specified when you configured the LabVIEW VI
 Server.
3. Select the application instance that you want to connect from the
 Application Instance pull-down menu. 
 Note If the Application Instance pull-down menu is empty
 and you know that the VI Server is enabled and that a local application
 instance is open, you can click the refresh button next to the pull-down
 menu or press <F5> to refresh the
 Application Instance list.

Parent topic:

Opening a Trace Connection

<!--NI_TOPIC bundle=labview-desktop-execution-trace-toolkit path=opening-a-trace-connection-lv.html language=enus -->
## TOPIC 00014: Opening a Trace Connection from LabVIEW

- bundle_id: `labview-desktop-execution-trace-toolkit`
- source_path: `opening-a-trace-connection-lv.html`
- source_url: https://docs-be.ni.com/bundle/labview-desktop-execution-trace-toolkit/raw/resource/enus/opening-a-trace-connection-lv.html
- document_id: `labview-desktop-execution-trace-toolkit`
- page_type: `leaf`
- content_type: `task`
- source_description: Within labVIEW, you can open a trace connection whether you are working on a VI or on a project. In LabVIEW, you can use one of the following methods to open a trace connection between the Desktop Execution Trace Toolkit and a LabVIEW application instance: In the LabVIEW Project Explorer window, rig

### Opening a Trace Connection from
 LabVIEW

Within labVIEW, you can open a trace connection whether you are working on a VI or on
 a project.

In LabVIEW, you can use one of the following methods to
 open a trace connection between the Desktop Execution Trace Toolkit and a LabVIEW
 application instance:

- In the LabVIEW Project Explorer window, right-click
 My Computer and select Trace
 Execution from the shortcut menu.
- On the menu bar in the Project Explorer window or in a
 LabVIEW VI, select Tools»Profile»Trace Execution.

Parent topic:

Opening a Trace Connection

Related concepts:

- Opening a Trace Connection

Related tasks:

- Configuring the LabVIEW VI Server

<!--NI_TOPIC bundle=labview-desktop-execution-trace-toolkit path=overview.html language=enus -->
## TOPIC 00015: LabVIEW Desktop Execution Trace Toolkit Overview

- bundle_id: `labview-desktop-execution-trace-toolkit`
- source_path: `overview.html`
- source_url: https://docs-be.ni.com/bundle/labview-desktop-execution-trace-toolkit/raw/resource/enus/overview.html
- document_id: `labview-desktop-execution-trace-toolkit`
- page_type: `leaf`
- content_type: `concept`
- source_description: The LabVIEW Desktop Execution Trace Toolkit for Windows is a stand-alone application that captures execution events from applications running on the desktop of a local or remote computer and displays the execution events in the table pane. For each execution event that occurs, the table pane display

### LabVIEW Desktop Execution Trace
 Toolkit
 Overview

The LabVIEW Desktop Execution Trace Toolkit for Windows is a stand-alone application
 that captures execution events from applications running on the desktop of a local or
 remote computer and displays the execution events in the table pane. For each execution
 event that occurs, the table pane displays the type of event, the time the event occurs,
 the VI in which it occurs, and any additional details that are available. You can use
 the Desktop Execution Trace Toolkit to debug and optimize large LabVIEW applications,
 including those with multiple loops, client-server architectures, dynamically-loaded
 VIs, and so on.

<!--NI_TOPIC bundle=labview-desktop-execution-trace-toolkit path=part-1-opening-a-trace-connection.html language=enus -->
## TOPIC 00016: Part 1: Opening a Trace Connection

- bundle_id: `labview-desktop-execution-trace-toolkit`
- source_path: `part-1-opening-a-trace-connection.html`
- source_url: https://docs-be.ni.com/bundle/labview-desktop-execution-trace-toolkit/raw/resource/enus/part-1-opening-a-trace-connection.html
- document_id: `labview-desktop-execution-trace-toolkit`
- page_type: `leaf`
- content_type: `task`
- source_description: In Part 1 of this tutorial, you open a trace connection between the Desktop Execution Trace Toolkit and the example project Desktop Execution Trace Toolkit.lvproj, before you begin a trace session. Launch LabView. Navigate to the labview\examples\Desktop Execution Trace Toolkit.lvproj. In the Projec

### Part 1: Opening a Trace Connection

In Part 1 of this tutorial, you open a trace connection between the Desktop
 Execution Trace Toolkit and the example project Desktop Execution Trace
 Toolkit.lvproj, before you begin a trace session.

1. Launch LabView.
2. Navigate to the labview\examples\Desktop Execution Trace
 Toolkit.lvproj.
3. In the Project Explorer window, right-click My
 Computer and select Trace Execution from the shortcut
 menu to launch the Desktop Execution Trace Toolkit and open a trace connection to the
 project. 
 Note The toolkit uses the LabVIEW VI
 Server to connect to the applications on which you execute trace sessions. If LabVIEW
 prompts you to enable the VI Server, click Yes.
4. Verify that the Machine field displays the name of computer on
 which the example project runs and that the Port field displays the
 default port value 3363.
5. Verify that the Application Instance pull-down menu displays
 Desktop Execution Trace Toolkit.lvproj.

After you open a trace connection between the toolkit and Desktop Execution Trace
 Toolkit.lvproj, you can configure a trace session in Part 2 of this tutorial.

Parent topic:

Get Started with an Example

<!--NI_TOPIC bundle=labview-desktop-execution-trace-toolkit path=part-2-configuring-a-trace-session.html language=enus -->
## TOPIC 00017: Part 3: Executing a Trace Session

- bundle_id: `labview-desktop-execution-trace-toolkit`
- source_path: `part-2-configuring-a-trace-session.html`
- source_url: https://docs-be.ni.com/bundle/labview-desktop-execution-trace-toolkit/raw/resource/enus/part-2-configuring-a-trace-session.html
- document_id: `labview-desktop-execution-trace-toolkit`
- page_type: `leaf`
- content_type: `task`
- source_description: In Part 2 of this tutorial, you configure the trace data you want to acquire from Desktop Execution Trace Toolkit.lvproj for a trace session. In Part 3 of this tutorial, you execute the trace session and capture the trace data. In the Desktop Execution Trace Toolkit, click Start on the Home tab or p

### Part 3: Executing a Trace Session

In Part 2 of this tutorial, you configure the trace data you want to acquire from
 Desktop Execution Trace Toolkit.lvproj for a trace session. In Part 3
 of this tutorial, you execute the trace session and capture the trace data.

1. In the Desktop Execution Trace Toolkit, click Start on
 the Home tab or press <Ctrl-R> to begin tracing
 data.
2. In the LabVIEW Project Explorer window, double-click
 Desktop Execution - Generate Trace Events.vi to open the
 VI.
3. In LabVIEW, click Run to run the VI. The toolkit begins
 tracing the execution events that occur as the VI runs, automatically scrolling
 to the bottom of the table pane, and displaying the latest events. 
 Tip In the Desktop Execution Trace
 Toolkit, you can click Auto Scroll on the
 View tab to disable auto scroll and review trace
 data when the toolkit is executing a trace session.
4. Click OK on the front panel of the VI to see the events
 that occur when the VI starts running.
5. Click Memory Allocation on the front panel of the VI to
 generate memory allocation events.
6. Click Stop on the front panel of the VI to stop the
 VI.
7. Close the VI.
8. In the toolkit, click Stop or press <Ctrl-T> to stop
 tracing data and complete the trace session.
9. Select File»Save or press <Ctrl-S> to save the trace file as Desktop
 Execution Trace Toolkit.lvproj.det.

After you execute the trace session, you can review the trace data in Part 4 of this
 tutorial.

Parent topic:

Get Started with an Example

<!--NI_TOPIC bundle=labview-desktop-execution-trace-toolkit path=part-3-executing-a-trace-session.html language=enus -->
## TOPIC 00018: Part 4: Reviewing Trace Data

- bundle_id: `labview-desktop-execution-trace-toolkit`
- source_path: `part-3-executing-a-trace-session.html`
- source_url: https://docs-be.ni.com/bundle/labview-desktop-execution-trace-toolkit/raw/resource/enus/part-3-executing-a-trace-session.html
- document_id: `labview-desktop-execution-trace-toolkit`
- page_type: `leaf`
- content_type: `task`
- source_description: In Part 3 of this tutorial, you execute the trace session and capture the trace data from Desktop Execution Trace Toolkit.lvproj. In Part 4 of this tutorial, you review the trace data that the Desktop Execution Trace Toolkit captures and displays in the table pane. Select File»Open or press <Ctrl-O>

### Part 4: Reviewing Trace Data

In Part 3 of this tutorial, you execute the trace session and capture the trace data
 from Desktop Execution Trace Toolkit.lvproj. In Part 4 of this tutorial,
 you review the trace data that the Desktop Execution Trace Toolkit captures and displays in
 the table pane.

1. Select File»Open or press <Ctrl-O> to open Desktop Execution Trace
 Toolkit.lvproj.det you saved in Part 3 if it is not already open.
2. Select a specific event in the table pane. Notice that the toolkit displays
 additional details about the event in the details pane, including the call chain
 and VI path.
3. Right-click a VI Start Execution event in the table pane
 and select Highlight Paired Events from the shortcut
 menu. The toolkit highlights the VI Stop Execution event
 as the paired event for VI Start Execution.
4. Right-click the table pane and select Time Stamp»Relative from the shortcut menu. The Time column
 displays the relative time between the current event and the first event in the
 table pane. By default, the Time column displays the
 absolute time, which is the actual time when an event occurs. 
 Tip You can change the time format
 on the General page of the Options
 dialog box. 
 The toolkit begins tracing the execution events that occur as the VI
 runs, automatically scrolling to the bottom of the table pane, and displaying
 the latest events.
5. Click an event, press and hold down the <Ctrl> key, and click another event.
 The toolkit displays the duration between the two events in the details
 pane.
6. Double-click an event which displays Object in the
 Highlight column. The toolkit opens the VI in which
 the event occurs and highlights the related object in the VI. If the event
 displays VI in the Highlight
 column, the toolkit only opens the VI. 
 Note You also can use one of the following methods to navigate to a VI related
 with the event you select:Click Navigate on the View tab to navigate to
 the VI.Right-click an event and select Navigate to Call Chain
 VIs from the shortcut menu. You can select in the
 chain of callers from the current VI to the top-level VI.
7. Click the header of the Event column to sort the event
 names alphabetically. Notice that the column header displays an arrow to show
 that the toolkit groups the events in the table pane based on event types.
8. Identify all the memory allocation events in the table pane. 
 Note You can change the highlight color for each event in the table pane.
 Select File»Options or click Options on the
 View tab to launch the Options
 dialog box, select Table Highlight from the category
 list, and click the color box for a specific event type to change the
 highlight color.
9. Complete the following steps to review the trace data in an external
 application.
  1. Click the first memory allocation event in the table pane, press and
 hold down the <Shift> key, and click the last memory allocation event
 in the table pane to select all the memory allocation events in the
 table pane.
  2. Press <Ctrl-C> to copy the memory allocation events to the
 clipboard.
  3. Launch a text editor and open a blank file.
  4. Press <Ctrl-V> to paste the memory allocation events from the
 clipboard. 
 Note You can copy and paste the trace data in
 the toolkit to .txt files and .xls
 files.
  5. Save and close the file so that you can use the trace data for memory
 allocation events later without launching the toolkit.
10. In the toolkit, click the header of the # column to
 display the events in the order the events occur, which is the default
 setting.
11. Optional: 
 You also can right-click the table pane and select
 Columns from the shortcut menu to specify which
 columns the table pane displays.
12. Select File»Save to save the trace.
13. In LabView, close the VI.

After you review the trace data, you can filter the trace data to make the table pane
 easier to read in Part 5 of this tutorial.

Parent topic:

Get Started with an Example

Related tasks:

- Executing a Trace Session

<!--NI_TOPIC bundle=labview-desktop-execution-trace-toolkit path=part-4-reviewing-trace-data.html language=enus -->
## TOPIC 00019: Part 5: Filtering Trace Data

- bundle_id: `labview-desktop-execution-trace-toolkit`
- source_path: `part-4-reviewing-trace-data.html`
- source_url: https://docs-be.ni.com/bundle/labview-desktop-execution-trace-toolkit/raw/resource/enus/part-4-reviewing-trace-data.html
- document_id: `labview-desktop-execution-trace-toolkit`
- page_type: `leaf`
- content_type: `task`
- source_description: In Part 4 of this tutorial, you review the trace data that the Desktop Execution Trace Toolkit captures from Desktop Execution Trace Toolkit.lvproj. You may notice that executing a trace session even on a small application can capture hundreds of execution events. In Part 5 of this tutorial, you exe

### Part 5: Filtering Trace Data

In Part 4 of this tutorial, you review the trace data that the Desktop Execution Trace
 Toolkit captures from Desktop Execution Trace Toolkit.lvproj. You may
 notice that executing a trace session even on a small application can capture hundreds of
 execution events. In Part 5 of this tutorial, you execute a second trace session and filter
 the events that the table pane displays to make the table pane easier to read.

1. In the Desktop Execution Trace Toolkit, select File»Open to open Desktop Execution Trace
 Toolkit.lvproj.det you saved in Part 4.
2. Click Start on the Home tab to
 execute a new trace session.
3. In LabVIEW, open the Desktop Execution - Generate Trace Events VI if it is not
 already open.
4. In LabVIEW, click Run to run the VI. In the toolkit, the
 table pane updates to display the trace data for the new trace session.
5. In LabVIEW, click Load Dynamic VI on the front panel of
 the VI to load the Desktop Execution - Strip Chart SubVI. In the toolkit, the
 VI column in the table pane shows that events now
 occur in the Desktop Execution - Strip Chart SubVI VI.
6. In the toolkit, click the View tab and select
 Filter Settings to display the Configure
 Displayed Events dialog box.
7. Hover over the
 head
 of this dialog box, the toolkit displays an illustration about the filtering
 process. Make sure you understand the illustration. The toolkit continues to
 trace the events you deselect in the dialog box but does not display them in the
 table pane. 
 Tip If you do not want the toolkit
 to trace a specific type of events at all, you must click the arrow below
 Capture Settings on the Home
 tab and deselect the event type in the Capture
 Settings pull-down menu so that you can reduce the amount of
 data that the toolkit must process and that you must analyze.
8. Select VIs from the type list to display the
 VIs page of the dialog box.
9. On the VIs page, the toolkit displays all the VIs that the
 toolkit traces in the current application instance. Remove the checkmark from
 the Desktop Execution - Strip Chart SubVI.vi
 checkbox. 
 Tip You also can
 right-click the VI on the table pane and select Filter this VI
 from Display from the shortcut menu.
10. Click OK to filter the events that occur in the
 subVI. 
 Note The filter settings you specify in the Configure Displayed
 Events dialog box is specific to not only the current trace
 session but the entire table pane. The trace data of the previous trace
 session in the table pane also updates to match the filter settings.
11. Search the table pane to confirm that the toolkit updates not to display the
 filtered events.
  1. Click Search on the View
 tab or press <Ctrl-F> to launch the search bar at the bottom of
 the table pane.
  2. Enter Strip in the field and click Previous or
 Next to search the table pane for the events
 that occur in the Desktop Execution - Strip Chart SubVI VI. The toolkit
 prompts the message that the toolkit cannot find the text
12. Click Reset Filter to clear the filter settings and
 display the filtered events.
13. On the search bar, click Previous or
 Next again to search the table pane for the events
 that contain the Strip keyword. You can find all the events that occur in the
 Desktop Execution - Strip Chart SubVI VI.
14. In LabVIEW, click Stop on the front panel of the
 VI.
15. Close the Desktop Execution - Generate Trace Events VI and Desktop Execution -
 Strip Chart SubVI VI.
16. In the toolkit, click Stop on the
 Home tab to stop executing the trace session.
17. Select File»Save to save the trace file.
18. Click Clear on the Home tab or
 press <Ctrl-L> so that all the events disappear in the table pane.

Filtering events prevents those events from appearing in the table pane. You can use
 the Configure Displayed Events dialog box to specify events to
 filter or display at any time. The table pane updates to match the new configuration
 settings each time you click OK in the Configure
 Displayed Events dialog box.

After you review the trace data, you can filter the trace data to make the table pane easier to
 read in Part 5 of this tutorial.

Parent topic:

Get Started with an Example

Related concepts:

- Reviewing Trace Data

<!--NI_TOPIC bundle=labview-desktop-execution-trace-toolkit path=part-5-filtering-trace-data.html language=enus -->
## TOPIC 00020: Part 6: Comparing Trace Data

- bundle_id: `labview-desktop-execution-trace-toolkit`
- source_path: `part-5-filtering-trace-data.html`
- source_url: https://docs-be.ni.com/bundle/labview-desktop-execution-trace-toolkit/raw/resource/enus/part-5-filtering-trace-data.html
- document_id: `labview-desktop-execution-trace-toolkit`
- page_type: `leaf`
- content_type: `topic`
- source_description: In Part 5 of this tutorial, you execute a second trace session and filter the trace data in the table pane. In Part 6 of this tutorial, you can either split the table pane or use the Compare Traces window to compare the traces you executed in previous parts of this tutorial. Splitting the Table Pane

### Part 6: Comparing Trace Data

In Part 5 of this tutorial, you execute a second trace session and filter the trace
 data in the table pane. In Part 6 of this tutorial, you can either split the table pane or
 use the Compare Traces window to compare the traces you executed in
 previous parts of this tutorial.

#### Splitting the Table Pane

You can split the table pane into two to
 compare the trace data in two displays which contain the same trace data.

1. In the Desktop Execution Trace Toolkit, select File»Open to open Desktop Execution Trace
 Toolkit.lvproj.det you saved in Part 5.
2. Click the View tab and click the
 Split image to split the table pane horizontally. The
 toolkit displays the same trace data in two displays. Tip You also
 can click the arrow below Split and select
 Split Pane (Up/Down) from the pull-down menu to
 split the table pane vertically.
3. Identify the bookmarks for the sessions, which
 are green icons on the vertical scroll bars in the two displays. The Desktop
 Execution Trace Toolkit automatically creates bookmarks when you start a new
 trace session. In this example, the two bookmarks represent the two trace
 sessions you executed in Part 3 and Part 5 respectively.
4. Hover over the first bookmark in the left display. The toolkit displays
 Navigate to Session 1: and the time when the first session
 starts. Click the bookmark to navigate to the first event of the first
 session.
5. Click the second bookmark in the right display to navigate to the first event of
 the second session. Move the vertical scroll bar to display the first event at
 the top of the display.
6. Compare the two sessions to locate the differences between the two trace
 sessions. Tip You also can use the Split
 button to review different parts in a long trace.
7. Click Reset Pane on the View tab
 to display the trace data in one display.

#### Using the Compare
 Traces Window

You also can use the Compare
 Traces window to compare two trace sessions of the same or different
 trace files. The Compare Traces window highlights the
 differences to make it easier to compare trace sessions.

1. Click Compare Traces on the View 
 tab to launch the Compare Traces window.
2. Select Desktop Execution Trace Toolkit.lvproj.det: session
 1 from the Session Name pull-down menu in
 the Compare 1 pane. The toolkit displays the number of the
 first event of this session in the Begin Index field and
 the number of the last event of this session in the End
 Index field.
3. Select Desktop Execution Trace Toolkit.lvproj.det: session
 2 from the Session Name pull-down menu in
 the Compare 2 pane. Note If you cannot find the trace
 session that you want to compare, verify that you open the application
 instance of the trace session and click the refresh button next to the
 Session Name pull-down menu to refresh the
 information that the toolkit displays for the trace.
4. Click Compare ( ) in the middle of the two
 panes to start comparing the two sessions. The toolkit automatically aligns the
 two sessions and highlights the differences in green.
5. Click Next ( ) in the middle of the two
 panes to move to the next difference.
6. Compare the two sessions to understand the differences between the two trace
 sessions. Note You may notice
 that the second session does not display memory allocation events. By
 default, the toolkit does not capture memory allocation events. Before
 executing the first trace session in Part 3 of the tutorial, you specify the
 configurations in the Capture Settings dialog box to
 capture memory allocation events. You save the trace file by selecting File»Save. However, the toolkit saves only the trace data instead of
 capture settings. When you executed the second session in Part 5, the
 toolkit applies the default settings and does not capture memory allocation
 events.
7. Close the Compare Traces window and save the trace
 file.

You also can compare the trace sessions of two trace files by clicking
 New Trace on the Home tab, opening
 a trace file or executing a trace session in the new trace window, and comparing the
 trace sessions of the two trace files in the Compare Traces
 window.

Tip

Begin Index

End
 Index

Filter Settings

View

Parent topic:

Get Started with an Example

<!--NI_TOPIC bundle=labview-desktop-execution-trace-toolkit path=part-6-comparing-trace-data.html language=enus -->
## TOPIC 00021: Part 7: Saving or Exporting Trace Data

- bundle_id: `labview-desktop-execution-trace-toolkit`
- source_path: `part-6-comparing-trace-data.html`
- source_url: https://docs-be.ni.com/bundle/labview-desktop-execution-trace-toolkit/raw/resource/enus/part-6-comparing-trace-data.html
- document_id: `labview-desktop-execution-trace-toolkit`
- page_type: `leaf`
- content_type: `topic`
- source_description: In Part 6 of this tutorial, you compare the trace sessions that you executed in Part 3 and Part 5 of this tutorial. In Part 7 of this tutorial, you save or export the trace file. Saving a Trace File You may know that you can save traces by selecting File»Save or pressing <Ctrl-S>. The Desktop Execut

### Part 7: Saving or Exporting Trace Data

In Part 6 of this tutorial, you compare the trace sessions that you executed in Part 3
 and Part 5 of this tutorial. In Part 7 of this tutorial, you save or export the trace
 file.

#### Saving a
 Trace File

You may know that you can save traces by selecting File»Save or pressing <Ctrl-S>. The Desktop Execution Trace Toolkit saves
 traces as execution trace (.det) files that the toolkit can reload
 in the table pane.

#### Exporting a Trace File

If you need to
 review the trace data later by using Microsoft Excel spreadsheet software or any
 text editor without opening the toolkit, you can export the trace file.

1. In the Desktop Execution Trace Toolkit, select File»Open to open Desktop Execution Trace
 Toolkit.lvproj.det you saved in Part 6 if it is not already
 open.
2. Select File»Export or press <Ctrl-E> to export the trace to a .txt file.
3. Navigate to the .txt file and open the file by using Microsoft Excel
 spreadsheet software or any text editor to review the contents of the export
 file.
4. Close the export file.

You may notice that the toolkit separates the trace data in the export file by
 tab delimiter. You can change the default delimiter in export files.

1. Select File»Options or click Options on the View tab to launch
 the Options dialog box.
2. Select General from the category list.
3. On the General page, select a delimiter from the Delimiter pull-down
 menu.
4. Select Custom from the
 Delimiter pull-down menu and specify a delimiter in
 the Custom field.
5. Click OK to apply the setting.

Parent topic:

Get Started with an Example

Related concepts:

- Saving or Exporting Trace Data

Related tasks:

- Comparing Trace Data

<!--NI_TOPIC bundle=labview-desktop-execution-trace-toolkit path=reviewing-partial-trace-data.html language=enus -->
## TOPIC 00022: Reviewing Partial Trace Data in an External Application

- bundle_id: `labview-desktop-execution-trace-toolkit`
- source_path: `reviewing-partial-trace-data.html`
- source_url: https://docs-be.ni.com/bundle/labview-desktop-execution-trace-toolkit/raw/resource/enus/reviewing-partial-trace-data.html
- document_id: `labview-desktop-execution-trace-toolkit`
- page_type: `leaf`
- content_type: `task`
- source_description: Desktop Trace Execution Toolkit allows you to open and review any part of trace data in a text editor. Select one or multiple events. Press <Ctrl-C> to copy the events to the clipboard. Launch Microsoft Excel, or a text editor, and open a blank file. Press <Ctrl-V> to paste the events from the clipb

### Reviewing Partial Trace Data in an External
 Application

Desktop Trace Execution Toolkit allows you to open and review any part of trace data in a
 text editor.

1. Select one or multiple events.
2. Press <Ctrl-C> to copy the events to the clipboard.
3. Launch Microsoft Excel, or a text editor, and open a blank file.
4. Press <Ctrl-V> to paste the events from the clipboard.
5. Save and close the file containing the events you pasted from the clipboard so
 that you can view the trace data later without launching the Desktop Execution
 Trace Toolkit.

Parent topic:

Reviewing Trace Data

<!--NI_TOPIC bundle=labview-desktop-execution-trace-toolkit path=reviewing-trace-data.html language=enus -->
## TOPIC 00023: Reviewing Trace Data

- bundle_id: `labview-desktop-execution-trace-toolkit`
- source_path: `reviewing-trace-data.html`
- source_url: https://docs-be.ni.com/bundle/labview-desktop-execution-trace-toolkit/raw/resource/enus/reviewing-trace-data.html
- document_id: `labview-desktop-execution-trace-toolkit`
- page_type: `leaf`
- content_type: `concept`
- source_description: Executing a trace session even on a small application can capture hundreds of execution events. You can use the following techniques to make the table pane easier to read:

### Reviewing Trace Data

Executing a trace session even on a small application can capture hundreds of
 execution events.

You can use the following techniques to make the table pane easier to read:

- [Filtering Trace Data](filter-trace-data.html) Interact with events in the Configure Displayed Events dialog box to temporarily filter the trace data you do not need from the table pane.
- [Searching the Table Pane](searching-the-table-pane.html) Complete the following steps to search for any text in the table pane.
- [Highlighting Paired Events](highlighting-paired-events.html) After you select an event, right-click the table pane and select Highlight Paired Events from the shortcut menu to find whether an event is paired with the event you selected.
- [Navigating to VIs](navigating-to-vis.html) The Desktop Execution Trace Toolkit to easily move between trace events in the toolkit and VIs in LabVIEW.
- [Viewing the Duration Between Events](viewing-the-duration-btwn-events.html) The Desktop Execution Trace Toolkit displays the actual time when an event occurs in the Time column of the table pane and allows you to identify the duration between events as well.
- [Reviewing Partial Trace Data in an External Application](reviewing-partial-trace-data.html) Desktop Trace Execution Toolkit allows you to open and review any part of trace data in a text editor.
- [Navigating to Trace Sessions](navigating-to-trace-sessions.html) The Desktop Execution Trace Toolkit displays all the trace data for an application instance in one display.

Parent topic:

Desktop Execution Trace Concepts

Related tasks:

- Part 4: Reviewing Trace Data
- Executing a Trace Session

<!--NI_TOPIC bundle=labview-desktop-execution-trace-toolkit path=saving-or-exporting-trace-data.html language=enus -->
## TOPIC 00024: Saving or Exporting Trace Data

- bundle_id: `labview-desktop-execution-trace-toolkit`
- source_path: `saving-or-exporting-trace-data.html`
- source_url: https://docs-be.ni.com/bundle/labview-desktop-execution-trace-toolkit/raw/resource/enus/saving-or-exporting-trace-data.html
- document_id: `labview-desktop-execution-trace-toolkit`
- page_type: `leaf`
- content_type: `concept`
- source_description: After you execute trace sessions in a trace, you can save the trace to view it at a later time in the Desktop Execution Trace Toolkit. You also can export the trace to a text file that you can view in any text editor. Saving a Trace Select File»Save or press <Ctrl-S> to save the trace sessions in a

### Saving or Exporting Trace Data

After you execute trace sessions in a trace, you can save the trace to view it at a
 later time in the Desktop Execution Trace Toolkit. You also can export the trace to a text
 file that you can view in any text editor.

#### Saving a Trace

Select File»Save or press <Ctrl-S> to save the trace
 sessions in a trace.

The Desktop Execution Trace Toolkit saves traces
 as execution trace (.det) files that the toolkit can reload in the
 table pane. Select File»Open or press <Ctrl-O> to load a saved trace.

#### Exporting a Trace

You can export a trace to a text (.txt) file that you can view
 later in any text editor. Select File»Export or press <Ctrl-E> to export a trace.

You can use the
 General page of the Options dialog box to specify the type of
 delimiter to use in the text file.

Parent topic:

Desktop Execution Trace Concepts

Related tasks:

- Executing a Trace Session

Related information::

- Part 7: Saving or Exporting Trace Data

<!--NI_TOPIC bundle=labview-desktop-execution-trace-toolkit path=searching-the-table-pane.html language=enus -->
## TOPIC 00025: Searching the Table Pane

- bundle_id: `labview-desktop-execution-trace-toolkit`
- source_path: `searching-the-table-pane.html`
- source_url: https://docs-be.ni.com/bundle/labview-desktop-execution-trace-toolkit/raw/resource/enus/searching-the-table-pane.html
- document_id: `labview-desktop-execution-trace-toolkit`
- page_type: `leaf`
- content_type: `task`
- source_description: Complete the following steps to search for any text in the table pane. Click Search on the View tab or press <Ctrl+F> to display the Search bar at the bottom of the main window. In the displayed Search bar, enter any part of a VI name, an event type, or the text in the other columns in the table pan

### Searching the Table Pane

Complete the following steps to search for any text in the table pane.

1. Click Search on the View tab or
 press <Ctrl+F> to display the Search bar at the
 bottom of the main window.
2. In the displayed Search bar, enter any part of a VI
 name, an event type, or the text in the other columns in the table pane. 
 Tip 
 Use the asterisk (*) wildcard to return events that contain a
 certain string.
 Use the caret (^) regular expression to return events that start
 with a certain string.
3. Click Previous or Next to
 navigate to the event you search for.

Split

View

Parent topic:

Reviewing Trace Data

Related information::

- Part 6: Comparing Trace Data

<!--NI_TOPIC bundle=labview-desktop-execution-trace-toolkit path=user-manual-welcome.html language=enus -->
## TOPIC 00026: LabVIEW Desktop Execution Trace Toolkit User Manual

- bundle_id: `labview-desktop-execution-trace-toolkit`
- source_path: `user-manual-welcome.html`
- source_url: https://docs-be.ni.com/bundle/labview-desktop-execution-trace-toolkit/raw/resource/enus/user-manual-welcome.html
- document_id: `labview-desktop-execution-trace-toolkit`
- page_type: `leaf`
- content_type: `concept`
- source_description: The LabVIEW Desktop Execution Trace Toolkit User Manual provides detailed descriptions of the product functionality and the step by step processes for use. Looking for Something Else?For information not found in the User Manual for your product, such as specifications and API reference, browse Relat

### LabVIEW Desktop Execution Trace
 Toolkit
 User Manual

The LabVIEW Desktop Execution Trace
 Toolkit User Manual provides detailed
 descriptions of the product functionality and the step by step processes for use.

#### Looking for Something Else?

For information not found in the User Manual
 for your product, such as specifications and API reference, browse *Related
 Information*.

Related information:

- Software and Driver Downloads
- License Setup and Activation
- Release Notes
- LabVIEW User Manual
- OS Compatibility
- NI Learning Center
- Hardware and Software Operating System
 Compatibility

<!--NI_TOPIC bundle=labview-desktop-execution-trace-toolkit path=using-the-desktop-execution-trace-toolkit.html language=enus -->
## TOPIC 00027: Desktop Execution Trace Concepts

- bundle_id: `labview-desktop-execution-trace-toolkit`
- source_path: `using-the-desktop-execution-trace-toolkit.html`
- source_url: https://docs-be.ni.com/bundle/labview-desktop-execution-trace-toolkit/raw/resource/enus/using-the-desktop-execution-trace-toolkit.html
- document_id: `labview-desktop-execution-trace-toolkit`
- page_type: `leaf`
- content_type: `concept`
- source_description: You can use the Desktop Execution Trace Toolkit to debug and optimize large LabVIEW applications, including those with multiple loops, client-server architectures, dynamically-loaded VIs. This toolkit captures execution events from applications running on the desktop of a local or remote computer an

### Desktop Execution Trace Concepts

You can use the Desktop Execution Trace Toolkit to debug and optimize large LabVIEW
 applications, including those with multiple loops, client-server architectures,
 dynamically-loaded VIs.

This toolkit captures execution events from applications running on the desktop of a
 local or remote computer and displays the execution events in the table pane.

Note

LabVIEW
 User Manual

#### Trace Data

The execution events that the Desktop Execution Trace Toolkit captures from LabVIEW
 applications are called trace data. You can browse the trace data in the table pane,
 save the trace data in execution trace (.det) files, or export the
 trace data to text (.txt) files.

#### Trace Sessions

When you use the Desktop Execution Trace Toolkit to capture trace data from a LabVIEW
 application, you are executing a trace session. A trace session is the period of
 time between when you click Start and
 Stop in the Desktop Execution Trace Toolkit. During this
 time, the toolkit captures trace data from LabVIEW applications or VIs that run in
 the application instance you select from the Application
 Instance pull-down menu on the Home
 tab.

#### Trace Procedures

Tracing a LabVIEW application instance, a VI that runs in the application instance
 you select, a LabVIEW stand-alone application, or a shared library file typically
 involves the following steps:

- [Opening a Trace Connection](opening-a-trace-connectin.html) You can open a trace connection from the toolkit or from a LabVIEW VI or project.
- [Configuring the LabVIEW VI Server](configuring-the-lv-vi-server.html) The Desktop Execution Trace Toolkit uses the LabVIEW VI Server to connect to the applications on which you execute trace sessions, including VIs, LabVIEW projects, stand-alone applications, and shared library files.
- [Configuring a Trace Session](configuring-a-trace-session.html) After you open a trace connection, you can specify types of execution events you want to capture to reduce the memory the Desktop Execution Trace Toolkit uses and avoid running out of memory.
- [Executing a Trace Session](executing-a-trace-session.html) After you open a trace connection, you can execute a trace session to capture the data. Complete the following steps to execute a trace session.
- [Reviewing Trace Data](reviewing-trace-data.html) Executing a trace session even on a small application can capture hundreds of execution events.
- [Comparing Trace Data](comparing-trace-data.html) You can compare two trace sessions of the same trace or different traces by using the Compare Traces window.
- [Saving or Exporting Trace Data](saving-or-exporting-trace-data.html) After you execute trace sessions in a trace, you can save the trace to view it at a later time in the Desktop Execution Trace Toolkit. You also can export the trace to a text file that you can view in any text editor.
- [Memory Considerations](memory-considerations.html) The Desktop Execution Trace Toolkit stores trace data in memory. By default, you can keep at most 100,000 events in the toolkit.

<!--NI_TOPIC bundle=labview-desktop-execution-trace-toolkit path=viewing-the-duration-btwn-events.html language=enus -->
## TOPIC 00028: Viewing the Duration Between Events

- bundle_id: `labview-desktop-execution-trace-toolkit`
- source_path: `viewing-the-duration-btwn-events.html`
- source_url: https://docs-be.ni.com/bundle/labview-desktop-execution-trace-toolkit/raw/resource/enus/viewing-the-duration-btwn-events.html
- document_id: `labview-desktop-execution-trace-toolkit`
- page_type: `leaf`
- content_type: `task`
- source_description: The Desktop Execution Trace Toolkit displays the actual time when an event occurs in the Time column of the table pane and allows you to identify the duration between events as well. Follow one of these methods: Right-click the table pane and select Time Stamp»Relative from the shortcut menu. The ta

### Viewing the Duration Between Events

The Desktop Execution Trace Toolkit displays the actual time when an event occurs in the
 Time column of the table pane and allows you to identify the
 duration between events as well.

- Right-click the table pane and select Time Stamp»Relative from the shortcut menu. The table pane
 updates to display the duration between the event you select
 and the first event in the trace.
- Select an event in the table pane, press and hold the <Ctrl> key, and
 click another event. The details pane displays the duration
 between the two events.

Parent topic:

Reviewing Trace Data
