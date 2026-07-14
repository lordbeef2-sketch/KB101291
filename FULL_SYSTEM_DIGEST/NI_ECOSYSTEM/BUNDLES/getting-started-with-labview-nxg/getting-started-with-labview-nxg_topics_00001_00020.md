# NI DOCUMENT BUNDLE: getting-started-with-labview-nxg

<!--NI_BUNDLE_CHUNK bundle=getting-started-with-labview-nxg start=1 end=20 -->
<!--NI_TOPIC bundle=getting-started-with-labview-nxg path=adding-software-to-a-target-device.html language=enus -->
## TOPIC 00001: Adding Software to a Target in the Design View

- bundle_id: `getting-started-with-labview-nxg`
- source_path: `adding-software-to-a-target-device.html`
- source_url: https://docs-be.ni.com/bundle/getting-started-with-labview-nxg/raw/resource/enus/adding-software-to-a-target-device.html
- document_id: `getting-started-with-labview-nxg`
- page_type: `leaf`
- content_type: `task`
- source_description: Add an application to a device, or target, in the Design view to specify where the software executes at run time. On the Design diagram, locate the device to which you want to add software. If an application already exists in your project, drag it from the Project Files tab to the Software section o

Adding Software to a Target in the Design View

Add an application to a device, or target, in the Design view to specify where the software executes at run time.

1. On the Design diagram, locate the device to which you want to add software.
2. Optional: 
 If an application already exists in your project, drag it from the 
 Project Files tab to the 
 Software section of the target.
3. Optional: 
 If you don't have an existing application, create a new application and add a VI to it.
  1. On the target, click 
 Add Software»Application and then click 
 OK. 
 On the Application document toolbar, notice how the target selector is automatically set to the target. 
[IMAGE alt='1378' src='GUID-8B8BE4C3-B74F-41DB-83A6-B81F1106BA88-a5.png']
  2. In the Application document, add a VI to the Application folder in one of the following ways: 
 Drag an existing VI from the 
 Project Files tabs to the Application document.
 Click 
 New (+) to create a new VI.
 When you add files to the Application and open them, those software files open in the context for the target device you selected. Therefore, you can interactively edit and run the program on the target device from the VI. 
 org.dita.html5/xsl/topic.xsl 455Note When you open a VI from the 
 Project Files tab, the target of that VI can vary depending on whether it is targeted to run on multiple devices in SystemDesigner. You can use the target selector, shown in the following image, to verify the target or switch between instances of the VI on different targets. 
 
[IMAGE alt='1378' src='GUID-A02FA1CF-3E12-45EC-9BC9-DE6670CBBF3C-a5.png']
  3. If you create a new VI, create whatever code you want to run on the target. 
 org.dita.html5/xsl/topic.xsl 455Note You can use example code installed with your drivers to quickly start programming. To use example code, navigate to the Lobby in LabVIEW NXG and select 
 Learning»Examples to launch an example and copy the code to your VI.
  4. Click 
 File»Save all to save your project.
  5. Navigate back to the Design view of SystemDesigner.

You can now see software on your target.

Parent topic:

Adding Software to a Target System in the Design View

<!--NI_TOPIC bundle=getting-started-with-labview-nxg path=adding-software-to-target-device-in-design-view.html language=enus -->
## TOPIC 00002: Adding Software to a Target System in the Design View

- bundle_id: `getting-started-with-labview-nxg`
- source_path: `adding-software-to-target-device-in-design-view.html`
- source_url: https://docs-be.ni.com/bundle/getting-started-with-labview-nxg/raw/resource/enus/adding-software-to-target-device-in-design-view.html
- document_id: `getting-started-with-labview-nxg`
- page_type: `leaf`
- content_type: `task`
- source_description: Add an application or library to a target system in the Design view. When the software is deployed to the target, it applies the hardware configuration of your system design. Complete the following tasks to add software to your system. Learn about the types of software you can add to your system. Ad

Adding Software to a Target System in the
 Design View

Add an application or library to a target system in the Design view. When the
 software is deployed to the target, it applies the hardware configuration of your system
 design.

Complete the following tasks to add software
 to your system.

1. Learn about the types of [software](/csh?topicname=software-systemdesigner-devices.html) you can add to your system.
2. [Add software to your target system](/csh?topicname=adding-software-to-a-target-device.html)
 in the Design view.

Parent topic:

Visualizing, Designing, and Documenting Your Hardware in SystemDesigner

<!--NI_TOPIC bundle=getting-started-with-labview-nxg path=annotating-the-design-view.html language=enus -->
## TOPIC 00003: Annotating the Design View

- bundle_id: `getting-started-with-labview-nxg`
- source_path: `annotating-the-design-view.html`
- source_url: https://docs-be.ni.com/bundle/getting-started-with-labview-nxg/raw/resource/enus/annotating-the-design-view.html
- document_id: `getting-started-with-labview-nxg`
- page_type: `leaf`
- content_type: `concept`
- source_description: Use comments and lines from the Annotations palette to explain design decisions and document your system. When you select a comment on the Design diagram, you can customize it on the Item tab in the following ways. Item Tab Action Additional Information Add a comment label, sub-label and inline note

Annotating the Design View

Use comments and lines from the Annotations palette to explain design decisions and document your system.

When you select a comment on the Design diagram, you can customize it on the 
 Item tab in the following ways.

| Item Tab Action | Additional Information |
| --- | --- |
| Add a comment label, sub-label and inline notes. | You can type the text a comment displays on the Item tab. |
| Adjust the visual style of the comment. | You can visually group a set of annotations by styling them the same way. Edit the comment fill color, as well as border color, style and thickness, on the Item tab. |
| Set an image to display inside the comment. | Images appear at the bottom of a comment on the Design diagram. The image scales proportionately with the size of the comment. If you enable Fixed image padding, you may need to resize the comment in order to avoid image cropping. |
| Provide additional information about the comment in the Context help description field. | Text you enter appears in the context help for the comment. |
| Enter a URL or path in the More help link field to provide additional information. | The more help link appears in the context help for the comment. |

Parent topic:

Visualizing, Designing, and Documenting Your Hardware in SystemDesigner

<!--NI_TOPIC bundle=getting-started-with-labview-nxg path=control-zoom-mouse-wheel.html language=enus -->
## TOPIC 00004: Customizing Mouse Wheel Behavior

- bundle_id: `getting-started-with-labview-nxg`
- source_path: `control-zoom-mouse-wheel.html`
- source_url: https://docs-be.ni.com/bundle/getting-started-with-labview-nxg/raw/resource/enus/control-zoom-mouse-wheel.html
- document_id: `getting-started-with-labview-nxg`
- page_type: `leaf`
- content_type: `task`
- source_description: You can change the action the mouse wheel performs within the workspace. Click FilePreferences to display the Preferences dialog box. On the Editor tab, select the desired setting for Zoom Control. Setting Description Zoom with Mouse Wheel Scroll with the mouse wheel to zoom in and out within the wo

Customizing Mouse Wheel Behavior

You can change the action the mouse wheel performs within the workspace.

1. Click 
 File»Preferences to display the 
 Preferences dialog box.
2. On the 
 Editor tab, select the desired setting for Zoom Control. 
 SettingDescriptionZoom with Mouse Wheel
 Scroll with the mouse wheel to zoom in and out within the workspace.
 To scroll vertically within the workspace, hold down the <Ctrl> key while scrolling with the mouse wheel.Zoom with Ctrl + Mouse Wheel (Default)
 Hold down the <Ctrl> key while scrolling with the mouse wheel to zoom in and out within the workspace.
 To scroll vertically within the workspace, scroll with the mouse wheel.
3. Click 
 OK.

Parent topic:

Customizing G Web Development Software

<!--NI_TOPIC bundle=getting-started-with-labview-nxg path=customizing-labview-nxg.html language=enus -->
## TOPIC 00005: Customizing G Web Development Software

- bundle_id: `getting-started-with-labview-nxg`
- source_path: `customizing-labview-nxg.html`
- source_url: https://docs-be.ni.com/bundle/getting-started-with-labview-nxg/raw/resource/enus/customizing-labview-nxg.html
- document_id: `getting-started-with-labview-nxg`
- page_type: `leaf`
- content_type: `task`
- source_description: Customize the G Web Development Software environment by changing the mouse wheel behavior, displaying tabs in the editor, and adding guide lines to the panel and diagram. Customizing Mouse Wheel Behavior—Change the action the mouse wheel performs within the workspace. Displaying Tabs in the Editor—A

Customizing G Web Development Software

Customize the G Web Development Software environment by changing the mouse wheel
 behavior, displaying tabs in the editor, and adding guide lines to the panel and
 diagram.

- [Customizing Mouse Wheel Behavior](control-zoom-mouse-wheel.html)—Change
 the action the mouse wheel performs within the workspace.
- [Displaying Tabs in the Editor](display-tabs.html)—Access
 information about your project and complete project-related tasks.
- [Aligning Objects on the Panel](smart-guides.html)—Display
 guide lines to help you align and organize objects on the panel.
- [Displaying the Diagram Grid](diagram-grid.html)—Display
 guide lines to help you align and organize objects on the diagram.

reset the workspace

Parent topic:

Getting Started with G Web Development Software

<!--NI_TOPIC bundle=getting-started-with-labview-nxg path=design-view-canvas-designing-documenting-hardware-system.html language=enus -->
## TOPIC 00006: Design View: A Canvas for Designing and Documenting a Hardware System

- bundle_id: `getting-started-with-labview-nxg`
- source_path: `design-view-canvas-designing-documenting-hardware-system.html`
- source_url: https://docs-be.ni.com/bundle/getting-started-with-labview-nxg/raw/resource/enus/design-view-canvas-designing-documenting-hardware-system.html
- document_id: `getting-started-with-labview-nxg`
- page_type: `leaf`
- content_type: `concept`
- source_description: The Design view enables you to create and annotate the hardware system your project requires. SystemDesigner does not automatically populate your live hardware system in the Design view. Instead, the Design view is a blank diagram, or canvas. The Design diagram is where you add devices and connect t

Design View: A Canvas for Designing and Documenting a Hardware System

The Design view enables you to create and annotate the hardware system your project requires.

SystemDesigner does not automatically populate your live hardware system in the Design view. Instead, the Design view is a blank diagram, or canvas. The Design diagram is where you add devices and connect them to configure your hardware system.

Note

A device on the Design diagram contains several configurable features.

[IMAGE alt='1378' src='GUID-F16ECBD5-991D-4DFC-8302-95DC320E7DA3-a5.png']

1. Label—Name of the device product family.
2. Sub-label—Additional information about the device, such as the device name, hostname, model, or product family.
3. Ports—Connections between devices in your system.
4. Software—Applications that execute on the device and libraries that contain reusable source files.
5. Device slots—Controllers, modules, and empty slots.
6. Match status—Type of device match between the live device and the device
 added to the Design view.

Parent topic:

SystemDesigner

<!--NI_TOPIC bundle=getting-started-with-labview-nxg path=diagram-grid.html language=enus -->
## TOPIC 00007: Displaying the Diagram Grid

- bundle_id: `getting-started-with-labview-nxg`
- source_path: `diagram-grid.html`
- source_url: https://docs-be.ni.com/bundle/getting-started-with-labview-nxg/raw/resource/enus/diagram-grid.html
- document_id: `getting-started-with-labview-nxg`
- page_type: `leaf`
- content_type: `task`
- source_description: As you place objects on the diagram, they automatically align to a grid. Making this grid visible can help you keep the diagram organized as you add and arrange objects. Click FilePreferences to display the Preferences dialog box. On the VI tab, in the Diagram Editing Defaults section, place a check

Displaying the Diagram Grid

As you place objects on the diagram, they automatically align to a grid. Making this grid visible can help you keep the diagram organized as you add and arrange objects.

1. Click 
 File»Preferences to display the 
 Preferences dialog box.
2. On the 
 VI tab, in the 
 Diagram Editing Defaults section, place a checkmark in the 
 Always Show Grid checkbox. 
 [IMAGE alt='1378' src='GUID-836825A2-3C61-453D-A514-0D65D385612D-a5.png']

Parent topic:

Customizing G Web Development Software

<!--NI_TOPIC bundle=getting-started-with-labview-nxg path=display-tabs.html language=enus -->
## TOPIC 00008: Displaying Tabs in the Editor

- bundle_id: `getting-started-with-labview-nxg`
- source_path: `display-tabs.html`
- source_url: https://docs-be.ni.com/bundle/getting-started-with-labview-nxg/raw/resource/enus/display-tabs.html
- document_id: `getting-started-with-labview-nxg`
- page_type: `leaf`
- content_type: `task`
- source_description: Display tabs in the editor to access different types of information about your project as well as to complete project-related tasks, such as troubleshooting or resource management. Click View and select the tab(s) you want to display from the pull-down menu.

Displaying Tabs in the Editor

Display tabs in the editor to access different types of information about your project as well as to complete project-related tasks, such as troubleshooting or resource management.

View

Parent topic:

Customizing G Web Development Software

<!--NI_TOPIC bundle=getting-started-with-labview-nxg path=enable-sd.html language=enus -->
## TOPIC 00009: Enabling SystemDesigner Visibility

- bundle_id: `getting-started-with-labview-nxg`
- source_path: `enable-sd.html`
- source_url: https://docs-be.ni.com/bundle/getting-started-with-labview-nxg/raw/resource/enus/enable-sd.html
- document_id: `getting-started-with-labview-nxg`
- page_type: `leaf`
- content_type: `task`
- source_description: Update your preferences to see a visual representation of web targets in SystemDesigner. Click FilePreferences. Select Web Server and enable Show SystemDesigner. Reopen the project to apply the update.

Enabling SystemDesigner Visibility

Update your preferences to see a visual representation of web targets in
 SystemDesigner.

1. Click File»Preferences.
2. Select Web Server and enable Show
 SystemDesigner.
3. Reopen the project to apply the update.

Parent topic:

Getting Started with G Web Development Software

Parent topic:

Creating a Web Application

<!--NI_TOPIC bundle=getting-started-with-labview-nxg path=gslv.html language=enus -->
## TOPIC 00010: Getting Started with G Web Development Software

- bundle_id: `getting-started-with-labview-nxg`
- source_path: `gslv.html`
- source_url: https://docs-be.ni.com/bundle/getting-started-with-labview-nxg/raw/resource/enus/gslv.html
- document_id: `getting-started-with-labview-nxg`
- page_type: `leaf`
- content_type: `concept`
- source_description: G Web Development Software is a science and engineering-focused programming environment for designing and testing systems within a visual code diagram. The Projects tab appears when you launch G Web Development Software. Select either the Projects or Learning tab to get started. From the Projects ta

Getting Started with G Web Development
 Software

G Web Development Software is a science and engineering-focused programming environment
 for designing and testing systems within a visual code diagram. The
 Projects tab appears when you launch G Web Development Software. Select
 either the Projects or Learning tab to get
 started.

Projects

- Create a new blank web virtual instrument (webVI) project.
- Create a new project webVI based on a template.
- Open a recent project.
- Access help documentation from the right panel to learn more
 about G Web Development Software.

The Projects tab will close once you make your selection. You can
 access it again by clicking Home in the upper-left corner of the
 document.

<!--NI_TOPIC bundle=getting-started-with-labview-nxg path=keyboard-shortcuts.html language=enus -->
## TOPIC 00011: Keyboard Shortcuts

- bundle_id: `getting-started-with-labview-nxg`
- source_path: `keyboard-shortcuts.html`
- source_url: https://docs-be.ni.com/bundle/getting-started-with-labview-nxg/raw/resource/enus/keyboard-shortcuts.html
- document_id: `getting-started-with-labview-nxg`
- page_type: `leaf`
- content_type: `reference`
- source_description: The following tables list keyboard shortcuts in the environment. File Operations Shortcut Action Ctrl-N Open a new document and add it to the existing project. Ctrl-Shift-N Open a new project. Ctrl-O Open an existing project. Ctrl-W Close the current document. Ctrl-S Save the current file. Ctrl-Shif

Keyboard Shortcuts

The following tables list keyboard shortcuts in the environment.

Parent topic:

Getting Started with G Web Development Software

#### File Operations

| Shortcut | Action |
| --- | --- |
| Ctrl-N | Open a new document and add it to the existing project. |
| Ctrl-Shift-N | Open a new project. |
| Ctrl-O | Open an existing project. |
| Ctrl-W | Close the current document. |
| Ctrl-S | Save the current file. |
| Ctrl-Shift-S | Save all open files. |
| Ctrl-P | Print the current document. |
| Alt-F4 | Quit. |

#### Basic Editing

| Shortcut | Action |
| --- | --- |
| Ctrl-X Shift-Delete | Cut. |
| Ctrl-C Ctrl-Insert | Copy. |
| Ctrl-V Shift-Insert | Paste. |
| Ctrl-Z Alt-Backspace | Undo. |
| Ctrl-Y Alt-Shift-Backspace | Redo. |
| Shift-F10 Application Key | Open shortcut menu for selected item. |
| Delete | Delete. |
| Ctrl-Delete | Delete and rewire. |

#### Selecting and Moving Objects

| Shortcut | Action |
| --- | --- |
| Shift-Click | Select multiple objects. Add object to the current selection. |
| Ctrl-A | Select all objects. |
| Arrow keys | Move selected objects in grid-sized increments. |
| Shift-Arrow keys | Move selected objects four grid units. |
| Ctrl-Drag | Copy and drag selected object. |
| Ctrl-Shift-Drag | Copy selected object and move it along one axis. |
| Shift-Resize | Resize selected object while maintaining aspect ratio. |
| Ctrl-Resize | Resize selected object while maintaining center point. |
| Shift-Ctrl-Resize | Resize selected object while maintaining both aspect ratio and center point. |
| Ctrl-Drag open area | Create additional blank space along the axis you drag the mouse. |
| Double-click open area | Add free label or comment to panel or diagram. |
| Spacebar-Drag | Pan across panel or diagram. |

#### Navigating the Environment

| Shortcut | Action |
| --- | --- |
| Ctrl-F | Find and replace text or objects within a document. |
| Ctrl-Shift-F | Find and replace text or objects within a project. |
| Enter F3 Ctrl-G | Search document for next instance of text or an object. This command is only available when in Find mode. |
| Shift-Enter Shift-F3 Shift-Ctrl-G | Search document for previous instance of text or an object. This command is only available when in Find mode. |
| Ctrl-Tab | Cycle through document tabs in the order in which they appear onscreen. |
| Ctrl-Shift-Tab | Cycle through document tabs in the opposite order in which they appear onscreen. |
| Ctrl-Shift-Spacebar | Shift focus to the application-wide search bar. |
| Ctrl-\\ | Hide and show all tabs. Hide and show all panes. |

#### Navigating the Panel and Diagram

| Editor Command | Shortcut | Action |
| --- | --- | --- |
| Panel and diagram selectors | Ctrl-E | Toggle between the panel and diagram view. If the icon view is active, switch to the panel view. |
| Search | Ctrl-Spacebar (Chinese keyboards) Ctrl-Alt-Spacebar | Shift focus to the palette search bar. |
| — | Ctrl-' | Toggle the diagram grid on/off. |
| — | Shift-Ctrl-; | Toggle Smart Guides on/off. Smart Guides help you align objects on the panel. |
| Vertical scroll bar | Mouse wheel | Scroll the document vertically. |
| Horizontal scroll bar | Shift-Mouse wheel | Scroll the document horizontally. |
| — | Tab | Shift focus from one control to another in tabbing order while the code is running. |
| — | Shift-Tab | Shift focus from one control to another in reverse tabbing order while the code is running. |
| — | Ctrl-Alt-I | Open and close the icon editor. |

#### Debugging Commands

| Editor Command | Shortcut | Action |
| --- | --- | --- |
| Step In | Ctrl-Down arrow F10 | Open a node and pause. |
| Step Over | Ctrl-Right arrow F11 | Execute a node without stepping into the node and pause at the next node. |
| Step Out | Ctrl-Up arrow Shift-F11 | Complete execution of the current node and pause. |
| Add/Remove Breakpoint | Ctrl-[ | Add or remove a breakpoint on the selected node or wire to pause execution at that breakpoint. |
| Add/Remove Probe | Ctrl-] | Add or remove a probe on the selected wire, which allows you to view intermediate values on the selected wire as the code runs. |

#### Help Commands

| Shortcut | Action |
| --- | --- |
| Ctrl-H | Display the Context Help. |
| F1 | Access additional information on ni.com. |

#### Running Code

| Editor Command | Shortcut | Action |
| --- | --- | --- |
| Run | Ctrl-R | Execute this code. |
| Abort | Ctrl-. | Stop the code immediately, before it finishes executing. |
|  | Ctrl-Run button | Recompile the code in the current document. |
|  | Ctrl-Shift-Run button | Recompile the code in all documents in memory. |

#### Wiring

| Editor Command | Shortcut | Action |
| --- | --- | --- |
| Remove Broken Wires | Ctrl-B | Delete all broken wires from the diagram. |
| — | Esc Right-click Ctrl-Z | Delete a wire you are in the process of creating. |
| — | Single-click wire | Select one wire segment. |
| — | Double-click wire | Select a wire branch. |
| — | Triple-click wire | Select the entire wire. |
| — | Ctrl-click wire | Create a new wire branch from an existing wire. |
| — | Single-click while wiring | Tack down the wire segment and start a new wire segment. |
| — | Double-click while wiring | End the wire without connecting it to a node. |
| — | Tap spacebar while wiring | Switch the direction of a wire between horizontal and vertical. |
| Clean Up Diagram Clean Up Selection | Ctrl-U | Organize the diagram or the selected code to make it easier to understand. |
| Clean Up Wire | Select Clean Up Wire from the shortcut menu | Route a selected wire to decrease the number of bends in the wire and avoid crossing objects on the diagram. |

#### Editing Text

| Shortcut | Action |
| --- | --- |
| Double-click text | Select a single word in a string. |
| Triple-click text | Select the entire string. |
| Ctrl-Right arrow Ctrl-Left arrow | Move the cursor within a string by one word in the direction of the arrow. |
| Home | Move the cursor to the beginning of the current line. |
| End | Move the cursor to the end of the current line. |
| Ctrl-Home | Move the cursor to the beginning of the string. |
| Ctrl-End | Move the cursor to the end of the string. |
| Esc | Cancel text entry. |
| Ctrl-Enter | Submit text entry. |

#### Capturing Data

| Editor Command | Shortcut | Action |
| --- | --- | --- |
| Capture panel data button | Ctrl-D | Save current data values on the panel to the Captured Data tab. |

#### Navigating the Project Files and Captured Data Tabs

| Shortcut | Action |
| --- | --- |
| * (Numeric keypad) | Expand everything under the selected folder. |
| + (Numeric keypad) | Expand the selected folder. |
| - (Numeric keypad) | Collapse the selected folder. |
| Right arrow | Expand the selected folder if it is closed. Otherwise, this keyboard shortcut selects the first child. |
| Left arrow | Collapse the selected folder if it is open. Otherwise, this keyboard shortcut selects the parent. |
| Ctrl-up arrow Ctrl-down arrow | Scroll through the pane without changing the current selection. |
| Any printable key(s) | Select the item beginning with the entered letter(s). |
| Enter | Open the selected document. |
| F2 | Rename the selected item. |
| Page Up Home | Move the selection to the first item in the tree. |
| Page Down End | Moves the selection to the last item in the tree. |

#### Zooming

| Shortcut | Action |
| --- | --- |
| Ctrl-Mouse wheel | Zoom. |
| Ctrl-+ | Zoom in. |
| Ctrl-- | Zoom out. |
| Ctrl-0 | Zoom to fit. |
| Ctrl-9 | Zoom to fit the selection. |

<!--NI_TOPIC bundle=getting-started-with-labview-nxg path=live-view-representation-of-devices-in-system.html language=enus -->
## TOPIC 00012: Live View: A Visual Representation of Hardware in Your System

- bundle_id: `getting-started-with-labview-nxg`
- source_path: `live-view-representation-of-devices-in-system.html`
- source_url: https://docs-be.ni.com/bundle/getting-started-with-labview-nxg/raw/resource/enus/live-view-representation-of-devices-in-system.html
- document_id: `getting-started-with-labview-nxg`
- page_type: `leaf`
- content_type: `concept`
- source_description: The Live view displays all of the hardware that SystemDesigner can discover in your system. Each device on the Live diagram represents the configuration of a real or simulated device in your system. Refer to the following image for an example of a device on the Live diagram. Label and sub-label—Info

Live View: A Visual Representation of Hardware in Your System

The Live view displays all of the hardware that SystemDesigner can discover in your system. Each device on the Live diagram represents the configuration of a real or simulated device in your system.

Refer to the following image for an example of a device on the Live diagram.

[IMAGE alt='1378' src='GUID-F39C4271-847F-4DD2-B3DC-B90F8A916827-a5.png']

1. Label and sub-label—Information about the device, such as the device name, hostname, model, product family, and serial number.
2. Ports—Connections between devices in your system.
3. Device slots—Controllers, modules, and empty slots. 
 org.dita.html5/xsl/topic.xsl 455 Note Only some devices support controllers, such as PCs and PXI chassis. If a device does support controllers, the only slot compatible with a controller is the first slot.
4. Hardware detection type—Glyph that indicates how SystemDesigner discovers the device.

| Hardware Detection Type | Icon | Behavior |
| --- | --- | --- |
| Auto-discovered |  | The device automatically appears on the Live diagram. Changes to the live device instantly appear on the Live diagram representation of the device. When the device is unplugged, powered down, or is no-longer reachable, it automatically disappears from the Live diagram. |
| Manually identified |  | The device may automatically appear on the Live diagram, or you may need to add it. On the document toolbar, click Add Hardware. Changes to the live device may automatically appear on the Live diagram. If a change does not appear, you may need to use one of the following methods to view the change in SystemDesigner: Select the device and click Refresh under the Advanced section on the Item tab. Click Identify Instruments to re-scan for GPIB instruments. When the device is removed from the system, you must manually remove it from the Live diagram. |
| User declared |  | The device does not appear on the Live diagram until you add it manually. Changes to the live device do not apply to the Live diagram device representation. You must manually specify changes in SystemDesigner. To remove the device from the system, you must manually remove it from the Live diagram. |

Parent topic:

SystemDesigner

<!--NI_TOPIC bundle=getting-started-with-labview-nxg path=navigating-systemdesigner.html language=enus -->
## TOPIC 00013: Navigating SystemDesigner

- bundle_id: `getting-started-with-labview-nxg`
- source_path: `navigating-systemdesigner.html`
- source_url: https://docs-be.ni.com/bundle/getting-started-with-labview-nxg/raw/resource/enus/navigating-systemdesigner.html
- document_id: `getting-started-with-labview-nxg`
- page_type: `leaf`
- content_type: `task`
- source_description: Visualize and design a hardware system with the SystemDesigner editor. The following image highlights parts of the SystemDesigner editor you use to configure a system and view the relationship between hardware and software in a system. Editor selector— View all live hardware currently connected to y

Navigating SystemDesigner

Visualize and design a hardware system with the SystemDesigner editor.

[IMAGE alt='1378' src='GUID-1000E293-3BDF-4D7B-B2DD-86CE236B8AC7-a5.png']

1. Editor selector— View all live hardware currently connected to your system on the Live view, or create a system of devices on the Design view.
2. Palette— Use the palettes to find unplaced live hardware, browse the hardware catalog for devices you want to explore, or create documentation for the system you design.
3. View selector—Explore your hardware visually as a system-level diagram that displays the relationship between devices in your project, or as a table of devices, software, and device resources.
4. Configuration pane—Configure devices and resources in your project using context-sensitive options. You can expand the pane when you want to make configurations.
5. Host device—Configure the host, such as a PC or embedded controller, to control the child devices to send commands and obtain data.
6. Software—Applications that execute on the target device and libraries that contain reusable source files.
7. Downstream port—Send commands down the system towards the intended device.
8. Upstream port—Send data up the system towards the parent device.
9. Child device—Use the child device to perform measurement tasks and obtain data to process.

Parent topic:

SystemDesigner

<!--NI_TOPIC bundle=getting-started-with-labview-nxg path=pf-tr.html language=enus -->
## TOPIC 00014: Preview Features

- bundle_id: `getting-started-with-labview-nxg`
- source_path: `pf-tr.html`
- source_url: https://docs-be.ni.com/bundle/getting-started-with-labview-nxg/raw/resource/enus/pf-tr.html
- document_id: `getting-started-with-labview-nxg`
- page_type: `leaf`
- content_type: `task`
- source_description: Preview features are new features in G Web Development Software that support specific workflows. They are release-quality features, but they have functionality gaps and are only supported for specific uses. Preview features in G Web Development Software: do not change compilation or execution of exi

Preview Features

Preview features are new features in G Web Development Software that support
 specific workflows. They are release-quality features, but they have functionality gaps and
 are only supported for specific uses. Preview features in G Web Development
 Software:

- do not change compilation or execution of existing code.
- do not change the persistence of existing files.
- have supporting documentation. You can also request support at ni.com/support .

File

»

Preferences

»

Preview features

Restart software for the changes to take effect.

Parent topic:

Getting Started with G Web Development Software

Related information:

- Creating a Multi-Mode Element
- Creating an Overload Group
- Multi-Mode Element and Overload Group Behavior
- Adding Code Snippets to a Custom Palette

<!--NI_TOPIC bundle=getting-started-with-labview-nxg path=resetting-workspace.html language=enus -->
## TOPIC 00015: Resetting the Workspace

- bundle_id: `getting-started-with-labview-nxg`
- source_path: `resetting-workspace.html`
- source_url: https://docs-be.ni.com/bundle/getting-started-with-labview-nxg/raw/resource/enus/resetting-workspace.html
- document_id: `getting-started-with-labview-nxg`
- page_type: `leaf`
- content_type: `task`
- source_description: You can quickly restore the workspace to the default settings after you make adjustments. Click ViewReset Workspace. The Navigation Pane and Configuration Pane are expanded. The Errors and Warnings tab is collapsed on the bottom edge of the workspace.

Resetting the Workspace

You can quickly restore the workspace to the default settings after you make adjustments.

View

»

Reset Workspace

- The Navigation Pane and Configuration Pane are expanded.
- The 
 Errors and Warnings tab is collapsed on the bottom edge of the workspace.

Parent topic:

Customizing G Web Development Software

<!--NI_TOPIC bundle=getting-started-with-labview-nxg path=smart-guides.html language=enus -->
## TOPIC 00016: Aligning Objects on the Panel

- bundle_id: `getting-started-with-labview-nxg`
- source_path: `smart-guides.html`
- source_url: https://docs-be.ni.com/bundle/getting-started-with-labview-nxg/raw/resource/enus/smart-guides.html
- document_id: `getting-started-with-labview-nxg`
- page_type: `leaf`
- content_type: `task`
- source_description: When Smart Guides are enabled, the editor displays guide lines to help you align and organize objects as you add them to the panel. Click FilePreferences to display the Preferences dialog box. On the VI tab, in the Panel Editing Defaults section, place a checkmark in the Smart Guides checkbox. As yo

Aligning Objects on the Panel

When Smart Guides are enabled, the editor displays guide lines to help you align and organize objects as you add them to the panel.

1. Click 
 File»Preferences to display the 
 Preferences dialog box.
2. On the 
 VI tab, in the 
 Panel Editing Defaults section, place a checkmark in the 
 Smart Guides checkbox. 
 As you add objects to the panel, the editor displays guide lines to assist with alignment, as shown in the following image.
 [IMAGE alt='1378' src='GUID-3FBA69E2-8EC7-422D-8D1A-B2A2A35C5D97-a5.png']

Parent topic:

Customizing G Web Development Software

<!--NI_TOPIC bundle=getting-started-with-labview-nxg path=software-systemdesigner-devices.html language=enus -->
## TOPIC 00017: Software on SystemDesigner Devices

- bundle_id: `getting-started-with-labview-nxg`
- source_path: `software-systemdesigner-devices.html`
- source_url: https://docs-be.ni.com/bundle/getting-started-with-labview-nxg/raw/resource/enus/software-systemdesigner-devices.html
- document_id: `getting-started-with-labview-nxg`
- page_type: `leaf`
- content_type: `concept`
- source_description: Adding software to a target device on the Design view specifies where the software executes at run time. Targeting software to a specific device also provides information about the hardware configuration of the target where the software executes. You can add two types of software components directly

Software on SystemDesigner Devices

Adding software to a target device on the Design view specifies where the software executes at run time. Targeting software to a specific device also provides information about the hardware configuration of the target where the software executes.

You can add two types of software components directly to a device in SystemDesigner:

Application

Library

You can add an application or library to a specific target by clicking 
 Add software on the device on the Design view, or by dragging a component from the 
 Project Files pane onto a device.

If a file or component is not on a specific target device, it executes on the development system, which SystemDesigner labels This Computer in the Live view. This is the same as a VI running normally in a project on your computer using the live hardware in your system.

Note

Software

Table

Parent topic:

Adding Software to a Target System in the Design View

<!--NI_TOPIC bundle=getting-started-with-labview-nxg path=systemdesigner.html language=enus -->
## TOPIC 00018: SystemDesigner

- bundle_id: `getting-started-with-labview-nxg`
- source_path: `systemdesigner.html`
- source_url: https://docs-be.ni.com/bundle/getting-started-with-labview-nxg/raw/resource/enus/systemdesigner.html
- document_id: `getting-started-with-labview-nxg`
- page_type: `leaf`
- content_type: `concept`
- source_description: SystemDesigner provides a visual representation of the hardware in a system and the software targeted to specific devices in the system. Use SystemDesigner to view your connected hardware, design a system using real and simulated hardware, and target software components to specific devices in the sy

SystemDesigner

SystemDesigner provides a visual representation of the hardware in a system and the software targeted to specific devices in the system. Use SystemDesigner to view your connected hardware, design a system using real and simulated hardware, and target software components to specific devices in the system.

Whether you must develop a standalone software application on a development machine or create a complex application with multiple systems, you should use SystemDesigner to manage your project's hardware configuration.

- Live view—Displays your connected hardware and enables you to validate and debug your devices with measurement panels.
- Design view—Provides a canvas for you to design and document your hardware system, regardless of whether you have access to the physical hardware.

| SystemDesigner view | Uses |
| --- | --- |
| Live view | View connected hardware devices in software Add a device to your system that SystemDesigner does not discover Validate and debug your hardware with measurement panels |
| Design view | Design a system with or without access to physical hardware Add software to a target device, such as a PC or FPGA Test or debug a project using a subset of the required hardware Annotate a system Include a hardware configuration in a distribution Generate a report of your system configuration to retain, share, or deploy |

Parent topic:

Visualizing, Designing, and Documenting Your Hardware in SystemDesigner

<!--NI_TOPIC bundle=getting-started-with-labview-nxg path=tips-for-editing-diagram-code.html language=enus -->
## TOPIC 00019: Tips and Tricks for Editing Diagram Code

- bundle_id: `getting-started-with-labview-nxg`
- source_path: `tips-for-editing-diagram-code.html`
- source_url: https://docs-be.ni.com/bundle/getting-started-with-labview-nxg/raw/resource/enus/tips-for-editing-diagram-code.html
- document_id: `getting-started-with-labview-nxg`
- page_type: `leaf`
- content_type: `reference`
- source_description: The following time-saving tools can help you edit diagram code more efficiently. Creating Diagram Code Task Tips and Tricks Create constants, controls, and indicators using the shortcut menu. You can save time when adding constants, controls, and indicators by using the shortcut menu to add the obje

Tips and Tricks for Editing Diagram Code

The following time-saving tools can help you edit diagram code more efficiently.

#### Creating Diagram Code

| Task | Tips and Tricks |
| --- | --- |
| Create constants, controls, and indicators using the shortcut menu. | You can save time when adding constants, controls, and indicators by using the shortcut menu to add the object instead of navigating the palette. Right-click any input or output of a node and select one of the Create options from the shortcut menu. For example, to create a constant, select the Create Constant icon. |
| Create a subVI from existing code. | You can use the Create SubVI from Selection option on the document toolbar to automatically generate a new subVI from a section of existing code. Refer to Creating a SubVI from a Section of Existing Code for more information. |

#### Editing Diagram Code

| Task | Tips and Tricks |
| --- | --- |
| Replace a diagram object with a similar object without using the palette. | You can replace an object on the diagram, such as a node, terminal, or constant, with a different type of the same object without navigating the palette. For example, you can replace an Add node with a Subtract node, a Numeric Terminal with a Boolean Terminal, or a True Constant with a False Constant. Right-click the object, select Replace from the shortcut menu, and select the desired replacement object. |
| Remove a structure without deleting objects in the structure. | You can remove a loop, Case Structure, or Flat Sequence from the diagram without deleting the code it contains. Right-click the border of the structure and select Remove Name of Structure from the shortcut menu. |

#### Organizing Diagram Code

| Task | Tips and Tricks |
| --- | --- |
| Align or distribute diagram objects to improve the organization of the diagram. | On the document toolbar, click Order, Align, or Distribute to organize a set of selected objects. |
| Delete all broken wires at one time. | On the document toolbar, click Remove Broken Wires to delete all broken wires on the diagram. |
| Clean up wires. | You can automatically route a selected wire to decrease the number of bends in the wire and avoid crossing objects on the diagram. Right-click a wire and select Clean Up Wire from the shortcut menu. |
| Move a terminal label to improve diagram readability. | To change the position of a terminal label, select the terminal and update the Label Placement option in the Item tab. |
| Show a node label to improve diagram readability. | To show a node label, select the node and enable the Show Label option in the Item tab. |

Parent topic:

Getting Started with G Web Development Software

<!--NI_TOPIC bundle=getting-started-with-labview-nxg path=visualizing-designing-documenting-your-hardware-labview-nxg.html language=enus -->
## TOPIC 00020: Visualizing, Designing, and Documenting Your Hardware in SystemDesigner

- bundle_id: `getting-started-with-labview-nxg`
- source_path: `visualizing-designing-documenting-your-hardware-labview-nxg.html`
- source_url: https://docs-be.ni.com/bundle/getting-started-with-labview-nxg/raw/resource/enus/visualizing-designing-documenting-your-hardware-labview-nxg.html
- document_id: `getting-started-with-labview-nxg`
- page_type: `leaf`
- content_type: `task`
- source_description: Configure your hardware system in SystemDesigner, visualize the system, manage design specifications, and document system requirements. Complete the following tasks to design a hardware system in SystemDesigner. Learn about SystemDesigner. Verify and validate your hardware in the Live view. Design y

Visualizing, Designing, and Documenting Your
 Hardware in SystemDesigner

Configure your hardware system in SystemDesigner, visualize the system,
 manage design specifications, and document system requirements.

Complete the following tasks to design a hardware
 system in SystemDesigner.

1. Learn about [SystemDesigner](/csh?topicname=systemdesigner.html).
2. [Verify and validate
 your hardware](/csh?topicname=verifying-and-validating-your-hardware-systemdesigner.html) in the Live view.
3. [Design your
 hardware system](/csh?topicname=designing-hardware-system-design-view.html) in the Design view.
4. [Add software to a
 target system](/csh?topicname=adding-software-to-target-device-in-design-view.html) in the Design view.
5. [Document and
 capture a system](/csh?topicname=documenting-and-capturing-system-systemdesigner.html) in the Design view.
6. [Apply the hardware configuration to your system](/csh?topicname=applying-hardware-configuration.html) using the NI
 Hardware Configuration Importer.

Parent topic:

Getting Started with G Web Development Software
