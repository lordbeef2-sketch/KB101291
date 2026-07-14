# NI DOCUMENT BUNDLE: labview-nxg-user-interface

<!--NI_BUNDLE_CHUNK bundle=labview-nxg-user-interface start=1 end=7 -->
<!--NI_TOPIC bundle=labview-nxg-user-interface path=centering-cursor.html language=enus -->
## TOPIC 00001: Centering a Cursor on a Graph or Chart

- bundle_id: `labview-nxg-user-interface`
- source_path: `centering-cursor.html`
- source_url: https://docs-be.ni.com/bundle/labview-nxg-user-interface/raw/resource/enus/centering-cursor.html
- document_id: `labview-nxg-user-interface`
- page_type: `leaf`
- content_type: `task`
- source_description: If you cannot locate a cursor that you added to your graph or chart, you can reset the cursor position to the center of your graph or chart. Use the cursor legend to center a cursor. Cursors are not available for intensity graphs. If you do not see the cursor legend, select Cursor Legend in the Part

Centering a Cursor on a Graph or Chart

If you cannot locate a cursor that you added to your graph or chart, you can reset the cursor position to the center of your graph or chart. 
 Use the cursor legend to center a cursor.

Note

1. If you do not see the cursor legend, select 
 Cursor Legend in the 
 Parts section on the 
 Item tab for the graph or chart.
2. On the 
 Cursor Legend, navigate to the cursor you want to center.
3. Ensure the 
 Visible? button 
 [IMAGE alt='1378' src='GUID-84751343-7EE6-486F-A777-F1C856AEF72C-a5.png'] is selected.
4. Click the 
 Center Cursor button 
 [IMAGE alt='1378' src='GUID-411CDB0C-8C52-4E4D-A260-7A6E5EB3C478-a5.png'] to center the cursor.

Parent topic:

Creating User Interfaces

<!--NI_TOPIC bundle=labview-nxg-user-interface path=clear-data.html language=enus -->
## TOPIC 00002: Clearing Indicator Display Data in a Chart, Graph, or Array

- bundle_id: `labview-nxg-user-interface`
- source_path: `clear-data.html`
- source_url: https://docs-be.ni.com/bundle/labview-nxg-user-interface/raw/resource/enus/clear-data.html
- document_id: `labview-nxg-user-interface`
- page_type: `leaf`
- content_type: `task`
- source_description: Right-click the chart, graph, or array and select Clear Data to remove all data from the indicator displays.

Clearing Indicator Display Data in a Chart, Graph, or Array

Clear Data

Parent topic:

Creating User Interfaces

<!--NI_TOPIC bundle=labview-nxg-user-interface path=controlling-panel-objects.html language=enus -->
## TOPIC 00003: Controlling Panel Objects Programmatically

- bundle_id: `labview-nxg-user-interface`
- source_path: `controlling-panel-objects.html`
- source_url: https://docs-be.ni.com/bundle/labview-nxg-user-interface/raw/resource/enus/controlling-panel-objects.html
- document_id: `labview-nxg-user-interface`
- page_type: `leaf`
- content_type: `concept`
- source_description: Control a panel object, such as a control, indicator, or the panel itself, by creating a control reference to the object. Control references are either strictly typed or general. Use control references with the Panel Manipulation nodes to control panel objects programmatically. The Chart class does

Controlling Panel Objects
 Programmatically

Control a panel object, such as a control, indicator, or the panel itself, by creating a
 control reference to the object. Control references are either strictly typed or
 general. Use control references with the Panel Manipulation
 nodes to control panel objects programmatically.

Note

Chart

Value

Parent topic:

Creating User Interfaces

#### Strictly Typed Control References

*Strictly typed control references* include data type information and accept
 only references of the same data type. For example, if a subVI accepts a strictly
 typed control reference that contains a 32-bit integer data type, you can wire only
 a reference that also contains a 32-bit integer data type to the subVI.

Complete the following steps to create a strictly
 typed control reference:

1. Place a control or indicator on the panel.
2. Right-click a panel object and select Create
 reference.
3. On the diagram, place the Static Control
 Reference of the panel object from the
 Unplaced Items tray and
 right-click the reference to create a control, indicator, or
 constant.

#### General Control References

*General control references* are flexible in the type of data they accept. For
 example, if a subVI accepts a general slide reference, you can wire a reference to a
 32-bit integer slide, single-precision slide, or a cluster of 32-bit integer slides
 to the slide reference terminal of the subVI.

Behavior

Item

```text
Reference does not include value data type
```

Note

Value

1. Place a Control Reference on the panel.
2. On the diagram, place the Control
 Reference from the Unplaced
 Items tray and click the
 Select reference type button
 next to the Reference type option on
 the Item tab to select a type.

<!--NI_TOPIC bundle=labview-nxg-user-interface path=creating-controls-dynamically-on-a-panel.html language=enus -->
## TOPIC 00004: Creating Controls Dynamically on a Panel

- bundle_id: `labview-nxg-user-interface`
- source_path: `creating-controls-dynamically-on-a-panel.html`
- source_url: https://docs-be.ni.com/bundle/labview-nxg-user-interface/raw/resource/enus/creating-controls-dynamically-on-a-panel.html
- document_id: `labview-nxg-user-interface`
- page_type: `leaf`
- content_type: `task`
- source_description: G Types allow you to reuse controls throughout your project. You can use G Types to create and delete controls dynamically at run time. What to Use Create Dynamic Control Delete Dynamic Control Wait (Milliseconds) Sequence Structure For Loop What to Do Create the following diagram to create and dele

Creating Controls Dynamically on a Panel

G Types allow you to reuse controls throughout your project. You can use G Types to create and delete controls dynamically at run time.

#### What to Use

- Create Dynamic Control
- Delete Dynamic Control
- Wait (Milliseconds)
- Sequence Structure
- For Loop

#### What to Do

Create the following diagram to create and delete controls at run time.

[IMAGE alt='1378' src='GUID-F2C5CDFF-8759-42B0-8817-E38064A35C9A-a5.png']

|  | Create a control on the panel according to the specified x and y positions. Select the Create Dynamic Control node and use the Data type option on the Item tab to specify the G Type that contains the control. The Create Dynamic Control node also returns a reference to the control. |
| --- | --- |
|  | Wait for 500 milliseconds before executing the next subdiagram. You can add a Property Node to change the properties of the control. |
|  | Delete the control from the panel. |
|  | Repeat the subdiagram for ten times. The shift registers pass the x position value from one iteration to the next. |

Parent topic:

Creating User Interfaces

<!--NI_TOPIC bundle=labview-nxg-user-interface path=setting-tabbing-order.html language=enus -->
## TOPIC 00005: Setting the Tabbing Order for Controls on the Panel

- bundle_id: `labview-nxg-user-interface`
- source_path: `setting-tabbing-order.html`
- source_url: https://docs-be.ni.com/bundle/labview-nxg-user-interface/raw/resource/enus/setting-tabbing-order.html
- document_id: `labview-nxg-user-interface`
- page_type: `leaf`
- content_type: `concept`
- source_description: Controls on the panel have an order, called tabbing order, that is unrelated to their position on the panel. Tabbing order is based on the order in which you place controls on the panel. The first control you create on the panel is element 0, the second is 1, and so on. If you delete a control, the

Setting the Tabbing Order for Controls on the Panel

Controls on the panel have an order, called tabbing order, that is unrelated to their position on the panel.

Tabbing order is based on the order in which you place controls on the panel. The first control you create on the panel is element 0, the second is 1, and so on. If you delete a control, the tabbing order adjusts automatically. The tabbing order determines the order in which the software selects controls when the user presses the <Tab> key while a VI runs.

Use the 
 Tab Order on the 
 Document tab to configure tabbing order for controls on the panel.

Parent topic:

Creating User Interfaces

<!--NI_TOPIC bundle=labview-nxg-user-interface path=userinterface.html language=enus -->
## TOPIC 00006: Creating User Interfaces

- bundle_id: `labview-nxg-user-interface`
- source_path: `userinterface.html`
- source_url: https://docs-be.ni.com/bundle/labview-nxg-user-interface/raw/resource/enus/userinterface.html
- document_id: `labview-nxg-user-interface`
- page_type: `leaf`
- content_type: `task`
- source_description: Create a user interface (UI) to allow a user to interact with a program. Use the Panel to design a UI for your program. Build UIs with controls and indicators. A control is an object that allows a user to input information into a program. An indicator is an object that gives the user information abo

Creating User Interfaces

Create a user interface (UI) to allow a user to interact with a program.

Panel

Build UIs with controls and indicators. A
 *control* is an object that allows a user to input information into a
 program. An *indicator* is an object that gives the user information
 about the program.

1. Create a program in the Diagram.
2. Switch to the Panel.
3. From the Palette, add controls and indicators to the
 Panel. 
 org.dita.html5/xsl/topic.xsl 455Note Controls and indicators
 have different data types, including numeric, Boolean, and string.
 Right-click the control or indicator to replace it with another control or
 indicator of the same data type.
4. Switch to the Diagram.
5. In the Palette, click Unplaced
 Items to add terminals that correspond to your controls and
 indicators onto the diagram.
6. Wire the new terminals into your program.
7. Click Run.

Configuration
 pane

Parent topic:

Creating a Web Application

<!--NI_TOPIC bundle=labview-nxg-user-interface path=writing-multiple-plots.html language=enus -->
## TOPIC 00007: Writing Multiple Plots to a Graph or Chart

- bundle_id: `labview-nxg-user-interface`
- source_path: `writing-multiple-plots.html`
- source_url: https://docs-be.ni.com/bundle/labview-nxg-user-interface/raw/resource/enus/writing-multiple-plots.html
- document_id: `labview-nxg-user-interface`
- page_type: `leaf`
- content_type: `task`
- source_description: Before you write multiple plots to a graph or chart, you must generate all the data sets you want to plot. Make sure each set of data has the same data type. Wire each set of data you want to plot to a Build Array node. Wire the appended array output from Build Array to a graph or chart indicator. I

Writing Multiple Plots to a Graph or Chart

Before you write multiple plots to a graph or chart, you must generate all the data sets you want to plot. Make sure each set of data has the same data type.

1. Wire each set of data you want to plot to a Build Array node.
2. Wire the appended array output from Build Array to a graph or chart indicator. 
 If your data consists of numeric, complex, or cluster values, appended array is a 2D array. Each row of the array is a separate plot. If your data consists of waveforms, appended array is a 1D array. Each waveform is a separate plot.

Parent topic:

Creating User Interfaces
