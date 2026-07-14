# NI DOCUMENT BUNDLE: labview-nxg-systemdesigner

<!--NI_BUNDLE_CHUNK bundle=labview-nxg-systemdesigner start=1 end=19 -->
<!--NI_TOPIC bundle=labview-nxg-systemdesigner path=adding-software-to-a-target-device.html language=enus -->
## TOPIC 00001: Adding Software to a Target in the Design View

- bundle_id: `labview-nxg-systemdesigner`
- source_path: `adding-software-to-a-target-device.html`
- source_url: https://docs-be.ni.com/bundle/labview-nxg-systemdesigner/raw/resource/enus/adding-software-to-a-target-device.html
- document_id: `labview-nxg-systemdesigner`
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

Related concepts:

- Software on SystemDesigner Devices

Related tasks:

- Navigating SystemDesigner

<!--NI_TOPIC bundle=labview-nxg-systemdesigner path=annotating-the-design-view.html language=enus -->
## TOPIC 00002: Annotating the Design View

- bundle_id: `labview-nxg-systemdesigner`
- source_path: `annotating-the-design-view.html`
- source_url: https://docs-be.ni.com/bundle/labview-nxg-systemdesigner/raw/resource/enus/annotating-the-design-view.html
- document_id: `labview-nxg-systemdesigner`
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

Related tasks:

- Documenting a System Design
- Exporting the Hardware Configuration of a Target

<!--NI_TOPIC bundle=labview-nxg-systemdesigner path=capturing-hardware-configuration-of-a-system.html language=enus -->
## TOPIC 00003: Capturing the Hardware Configuration of a System

- bundle_id: `labview-nxg-systemdesigner`
- source_path: `capturing-hardware-configuration-of-a-system.html`
- source_url: https://docs-be.ni.com/bundle/labview-nxg-systemdesigner/raw/resource/enus/capturing-hardware-configuration-of-a-system.html
- document_id: `labview-nxg-systemdesigner`
- page_type: `leaf`
- content_type: `task`
- source_description: Capture the hardware configuration of a system to save, share, or deploy. Record hardware in one of the following ways: Create a report of a system design—Record the hardware setup and device requirements of your system as a CSV file. Export the hardware configuration of your system to another machi

Capturing the Hardware Configuration of a System

Capture the hardware configuration of a system to save, share, or deploy.

Record hardware in one of the following ways:

- Create a report of
 a system design —Record the hardware setup and device requirements of your
 system as a CSV file.
- Export the hardware configuration of your system to another machine —Capture
 the hardware dependencies of your project as an NI Hardware Configuration file
 ( .nihwcfg ) to deploy to another machine.

Related tasks:

- Designing a Hardware System in the Design View

<!--NI_TOPIC bundle=labview-nxg-systemdesigner path=configuring-a-device-match-in-systemdesigner.html language=enus -->
## TOPIC 00004: Configuring a Device Match in SystemDesigner

- bundle_id: `labview-nxg-systemdesigner`
- source_path: `configuring-a-device-match-in-systemdesigner.html`
- source_url: https://docs-be.ni.com/bundle/labview-nxg-systemdesigner/raw/resource/enus/configuring-a-device-match-in-systemdesigner.html
- document_id: `labview-nxg-systemdesigner`
- page_type: `leaf`
- content_type: `task`
- source_description: Use device matching to apply updates to your live hardware configuration based on changes you make in the Design view. If SystemDesigner finds a matching device on the Design diagram, it automatically applies updates to the matching live device in your project. Navigate to the Design view. Ensure th

Configuring a Device Match in SystemDesigner

Use device matching to apply updates to your live hardware configuration based on changes you make in the Design view.

If SystemDesigner finds a matching device on the Design diagram, it automatically applies updates to the matching live device in your project.

1. Navigate to the Design view.
2. Ensure that 
 Sync is set to 
 Enable hardware matching. 
 The Sync setting determines if you can apply changes in your project to matching live hardware in your system. Sync is set to Enable hardware matching when you open SystemDesigner for the first time.
3. On the Design diagram, find the device you want to match with your live hardware. 
 If the device is not already on the Design diagram, find it on the palette and place it on the diagram. 
 org.dita.html5/xsl/topic.xsl 455Tip Any device on the Live diagram that does not have a match on the Design diagram appears in the Unplaced Live Hardware palette.
4. Verify the match status of the device. 
 SystemDesigner assigns a PC, chassis, or network device one of the following match status icons to inform you whether a device matches with live hardware. 
 Match StatusIconDescriptionHardware matching disabled[IMAGE alt='1378' src='GUID-86A58B7D-FBD4-41E0-8813-54F600295602-a5.png']When 
 Sync is set toDisable hardware matching, SystemDesigner prevents changes to devices in the Design view from applying to matching live hardware.Not Matched[IMAGE alt='1378' src='GUID-71B11BC8-A22D-479C-8339-576A8C36726D-a5.png']SystemDesigner does not identify a corresponding device on the Live diagram.Partially Matched[IMAGE alt='1378' src='GUID-A247F3F1-25A5-4640-819C-6E9BA618F5C0-a5.png']SystemDesigner identifies a potential match on the Live and Design diagrams. Click 
 Update modules in chassis to update the device on the Design diagram to match the configuration of the device on the Live diagram.Matched[IMAGE alt='1378' src='GUID-EF31963A-E4ED-44F6-B109-5A3827D0CA41-a5.png']SystemDesigner identifies a corresponding device on the Live diagram.
5. If the device does not have a match, configure the device on the Design diagram to match the device configuration on the Live diagram. 
 The following device characteristics must match on both the Design view and Live view for SystemDesigner to identify a match. 
 Matching CriteriaTasksDevice modelSearch for the correct model on the Design view palette and the 
 Model drop-down menu in the 
 Identity section of the 
 Item tab.Device nameUse the 
 Device name field in the 
 Identity section of the 
 Item tab to change the name of a device on the Design diagram.Order of controllers and modules inside a chassisIf a device is partially matched, click 
 Update modules in chassis on the 
 Item tab to update the order of the modules in the chassis to match the corresponding live chassis. This button only appears when 
 Sync is set to 
 Enable hardware matching.Device port connectionsEnsure port connections are identical to those of the device on the Live diagram.

After you enable hardware matching and configure the device on the Design diagram to match the configuration of the live hardware, SystemDesigner automatically matches the devices.

Parent topic:

Designing a Hardware System in the Design View

Related tasks:

- Designing a Hardware System in the Design View
- Swapping Device Models in a System
- Managing Visible Device Ports

<!--NI_TOPIC bundle=labview-nxg-systemdesigner path=design-view-canvas-designing-documenting-hardware-system.html language=enus -->
## TOPIC 00005: Design View: A Canvas for Designing and Documenting a Hardware System

- bundle_id: `labview-nxg-systemdesigner`
- source_path: `design-view-canvas-designing-documenting-hardware-system.html`
- source_url: https://docs-be.ni.com/bundle/labview-nxg-systemdesigner/raw/resource/enus/design-view-canvas-designing-documenting-hardware-system.html
- document_id: `labview-nxg-systemdesigner`
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

Related concepts:

- Live View: A Visual Representation of Hardware in Your System

Related tasks:

- Designing a Hardware System in the Design View
- Adding Software to a Target in the Design View

Related information:

- NI Driver Downloads

<!--NI_TOPIC bundle=labview-nxg-systemdesigner path=designing-hardware-system-design-view.html language=enus -->
## TOPIC 00006: Designing a Hardware System in the Design View

- bundle_id: `labview-nxg-systemdesigner`
- source_path: `designing-hardware-system-design-view.html`
- source_url: https://docs-be.ni.com/bundle/labview-nxg-systemdesigner/raw/resource/enus/designing-hardware-system-design-view.html
- document_id: `labview-nxg-systemdesigner`
- page_type: `leaf`
- content_type: `task`
- source_description: Use the Design view to design and document a virtual hardware system using hardware you do and do not own. The Design view enables you to design a new hardware system, modify an existing hardware system, and document the system to retain or share with others. There are many ways you can design or mo

Designing a Hardware System in the Design View

Use the Design view to design and document a virtual hardware system using hardware you do and do not own.

The Design view enables you to design a new hardware system, modify an existing hardware system, and document the system to retain or share with others.

There are many ways you can design or modify a hardware system in the Design view, depending on the hardware available to you, the instrument drivers installed, and your system needs:

- Design a
 system using your current system as a template —Create a new system using the
 hardware connected to your local machine by removing, modifying, or adding devices.
- Design a new
 system —Create a new system by adding virtual hardware devices and wiring them
 together.
- Swap device
 models —Switch out one device for another device to better meet your system
 needs.
- Manage visible
 device ports —Hide unused device ports on devices to remove clutter from the
 Design diagram.
- Configure a Device Match in SystemDesigner —Enable hardware matching to apply
 changes to a live hardware device from the Design view.

<!--NI_TOPIC bundle=labview-nxg-systemdesigner path=designing-new-system.html language=enus -->
## TOPIC 00007: Designing a New System

- bundle_id: `labview-nxg-systemdesigner`
- source_path: `designing-new-system.html`
- source_url: https://docs-be.ni.com/bundle/labview-nxg-systemdesigner/raw/resource/enus/designing-new-system.html
- document_id: `labview-nxg-systemdesigner`
- page_type: `leaf`
- content_type: `task`
- source_description: Design a system to your exact specifications using virtual hardware in the Design view. Navigate to the Design view. Considering your system requirements, customize the system in any of the following ways: Add your target to the Design diagram. Refer to the table below for instructions on how to add

Designing a New System

Design a system to your exact specifications using virtual hardware in the Design view.

1. Navigate to the Design view.
2. Considering your system requirements, customize the system in any of the following ways:
  - Add your target to the Design diagram. Refer to the table below for instructions on how to add a target to the Design diagram, depending on the system you need to create. 
 I want to create a PC systemI want to create a PXI systemOn the palette, select 
 PC»PC to add a generic computer to the Design diagram.On the palette, select 
 PXI»PXI chassis to select the chassis model your system needs and add it to the Design diagram.On the PXI chassis, click 
 Add device on the first port.Select the product family of the controller you need and then select the controller.
  - From the palette, add hardware devices to the Design diagram.
  - Wire the compatible device ports together based on the port configurations of the device. For example, downstream device ports connect to upstream device ports. 
 org.dita.html5/xsl/topic.xsl 455 Note If a wire appears broken, the connected devices are not compatible. In the 
 Item tab, select 
 Documentation»Manual to review device specifications.
  - Rename the device names to something more useful or identifiable for you and your team.
  - Add comments and images to the Design
 diagram to include notes about the system. Refer to [Annotating the Design View](/csh?topicname=annotating-the-design-view.html) for more information.
3. After you complete your system design, click 
 File»Save SystemDesigner.
4. On the document toolbar, click 
 Create SystemDesigner Report to capture the system for you to share or retain as a CSV file.

Parent topic:

Designing a Hardware System in the Design View

Related tasks:

- Designing a New System Using Your Live Hardware as a Template
- Managing Visible Device Ports
- Swapping Device Models in a System
- Configuring a Device Match in SystemDesigner

<!--NI_TOPIC bundle=labview-nxg-systemdesigner path=designing-system-existing-template.html language=enus -->
## TOPIC 00008: Designing a New System Using Your Live Hardware as a Template

- bundle_id: `labview-nxg-systemdesigner`
- source_path: `designing-system-existing-template.html`
- source_url: https://docs-be.ni.com/bundle/labview-nxg-systemdesigner/raw/resource/enus/designing-system-existing-template.html
- document_id: `labview-nxg-systemdesigner`
- page_type: `leaf`
- content_type: `task`
- source_description: To create a new system, you can use a connected hardware system as a template to modify or add devices to in the Design view of SystemDesigner. Navigate to the Design view. On the palette, click Unplaced Live Hardware. The devices on the Unplaced Live Hardware palette have same configuration as the

Designing a New System Using Your Live Hardware as a Template

To create a new system, you can use a connected hardware system as a template to modify or add devices to in the Design view of SystemDesigner.

1. Navigate to the Design view.
2. On the palette, click 
 Unplaced Live Hardware. 
 org.dita.html5/xsl/topic.xsl 455Note The devices on the Unplaced Live Hardware palette have same configuration as the matching device on the Live diagram. However, devices on the Design diagram do not change when modifications occur to a matching device on the Live diagram. Additionally, SystemDesigner does not remove a device from the Design diagram after you remove the matching device from the Live diagram.
3. Select 
 All to add all discovered hardware devices to the Design diagram.
4. Optional: 
 Considering your system requirements, customize the system in any of the following ways:
  - From the palette, add hardware devices to the Design diagram.
  - Wire the compatible device ports together based on the port configurations of the device. For example, downstream device ports connect to upstream device ports. 
 org.dita.html5/xsl/topic.xsl 455 Note If a wire appears broken, the connected devices are not compatible. In the 
 Item tab, select 
 Documentation»Manual to review device specifications.
  - Rename the device names to something more useful or identifiable for you and your team.
  - Add comments and images to the Design
 diagram to include notes about the system. Refer to [Annotating the Design View](/csh?topicname=annotating-the-design-view.html) for more information.
5. After you complete your system design, click 
 File»Save SystemDesigner.
6. On the document toolbar, click 
 Create SystemDesigner Report to capture the system for you to share or retain as a CSV file.

Parent topic:

Designing a Hardware System in the Design View

Related tasks:

- Designing a New System
- Managing Visible Device Ports
- Swapping Device Models in a System
- Configuring a Device Match in SystemDesigner

<!--NI_TOPIC bundle=labview-nxg-systemdesigner path=documenting-a-system-design.html language=enus -->
## TOPIC 00009: Documenting a System Design

- bundle_id: `labview-nxg-systemdesigner`
- source_path: `documenting-a-system-design.html`
- source_url: https://docs-be.ni.com/bundle/labview-nxg-systemdesigner/raw/resource/enus/documenting-a-system-design.html
- document_id: `labview-nxg-systemdesigner`
- page_type: `leaf`
- content_type: `task`
- source_description: Create a report of the hardware setup and device requirements of your system from either the Live view or Design view. The report records the location, label, product family, model, vendor, device name, and serial number of the devices in your system as a comma-separated value (CSV) file. Navigate t

Documenting a System Design

Create a report of the hardware setup and device requirements of your system from either the Live view or Design view.

The report records the location, label, product family, model, vendor, device name, and serial number of the devices in your system as a comma-separated value (CSV) file.

1. Navigate to the view which possesses the system you want to capture.
2. On the document toolbar, click 
 Export»SystemDesigner Report (.csv) to produce a report.
3. Select the location to save the report on your local machine and click 
 Save.

Parent topic:

Capturing the Hardware Configuration of a System

Related concepts:

- Annotating the Design View

Related tasks:

- Exporting the Hardware Configuration of a Target

<!--NI_TOPIC bundle=labview-nxg-systemdesigner path=exporting-hardware-configuration-of-a-target.html language=enus -->
## TOPIC 00010: Exporting the Hardware Configuration of a Target

- bundle_id: `labview-nxg-systemdesigner`
- source_path: `exporting-hardware-configuration-of-a-target.html`
- source_url: https://docs-be.ni.com/bundle/labview-nxg-systemdesigner/raw/resource/enus/exporting-hardware-configuration-of-a-target.html
- document_id: `labview-nxg-systemdesigner`
- page_type: `leaf`
- content_type: `task`
- source_description: Export the hardware configuration of your system as an NI Hardware Configuration file (.nihwcfg) to capture hardware dependencies. Navigate to either the Live view or Design view, depending on where your target's hardware configuration is in the project. On the document toolbar, select ExportNI Hard

Exporting the Hardware Configuration of a Target

Export the hardware configuration of your system as an NI Hardware Configuration file (.nihwcfg) to capture hardware dependencies.

1. Navigate to either the Live view or Design view, depending on where your target's hardware configuration is in the project.
2. On the document toolbar, select 
 Export»NI Hardware Configuration file (.nihwcfg).
3. If the SystemDesigner view you have open contains more than one target, select the target whose hardware configuration you want to export. 
 org.dita.html5/xsl/topic.xsl 455Note In the Live view, the only supported system is This Computer.
4. Select or deselect the hardware configuration you need to include for your project and click 
 OK.
5. Select the location to save the NI Hardware Configuration file on your local machine and click 
 OK.
6. Navigate to where you saved the NI Hardware Configuration file and send a copy of it to the system that will use it.

apply the hardware dependencies

Note

Parent topic:

Capturing the Hardware Configuration of a System

Related concepts:

- Annotating the Design View

Related tasks:

- Documenting a System Design

<!--NI_TOPIC bundle=labview-nxg-systemdesigner path=live-view-representation-of-devices-in-system.html language=enus -->
## TOPIC 00011: Live View: A Visual Representation of Hardware in Your System

- bundle_id: `labview-nxg-systemdesigner`
- source_path: `live-view-representation-of-devices-in-system.html`
- source_url: https://docs-be.ni.com/bundle/labview-nxg-systemdesigner/raw/resource/enus/live-view-representation-of-devices-in-system.html
- document_id: `labview-nxg-systemdesigner`
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

Related concepts:

- Design View: A Canvas for Designing and Documenting a Hardware System

Related tasks:

- Verifying Your Hardware Appears in the Live View
- Manually Adding Hardware to the Live View of SystemDesigner
- Validating Your Hardware with Measurement Panels

<!--NI_TOPIC bundle=labview-nxg-systemdesigner path=managing-available-device-ports.html language=enus -->
## TOPIC 00012: Managing Visible Device Ports

- bundle_id: `labview-nxg-systemdesigner`
- source_path: `managing-available-device-ports.html`
- source_url: https://docs-be.ni.com/bundle/labview-nxg-systemdesigner/raw/resource/enus/managing-available-device-ports.html
- document_id: `labview-nxg-systemdesigner`
- page_type: `leaf`
- content_type: `task`
- source_description: Show or hide device ports of PCs and remote controllers in the Design view to organize the system you create. In the Ports section of the device you want to organize, right-click a port and select Manage Ports to open the Manage Ports dialog and view the device ports you can display. Select each dev

Managing Visible Device Ports

Show or hide device ports of PCs and remote controllers in the Design view to organize the system you create.

1. In the 
 Ports section of the device you want to organize, right-click a port and select 
 Manage Ports to open the 
 Manage Ports dialog and view the device ports you can display.
2. Select each device port you want to display. 
 Consider the following behaviors when choosing device ports to display:
 Connecting a visible port to a hidden port on a separate device causes the hidden port to become visible. 
 org.dita.html5/xsl/topic.xsl 455Tip To connect to a hidden port on a device, wire a visible port terminal to the terminal next to the 
 Manage Ports button on the device.
 Hiding a wired port causes the existing wire to break. You cannot hide wired ports on the Live diagram.
 Displaying a port may rearrange the display order of the device ports, depending on the alphabetical order of the port names.
 Saving a project only preserves visible port designations on the Design diagram. 
 After you close the 
 Manage Ports dialog, SystemDesigner updates the device port display on the diagram.
3. To hide a device port, right-click the port and select 
 Hide Port or deselect the port in the 
 Manage Ports pop-up.

Parent topic:

Designing a Hardware System in the Design View

Related tasks:

- Swapping Device Models in a System
- Designing a Hardware System in the Design View
- Configuring a Device Match in SystemDesigner

<!--NI_TOPIC bundle=labview-nxg-systemdesigner path=manually-adding-hardware-live-view.html language=enus -->
## TOPIC 00013: Manually Adding Hardware to the Live View of SystemDesigner

- bundle_id: `labview-nxg-systemdesigner`
- source_path: `manually-adding-hardware-live-view.html`
- source_url: https://docs-be.ni.com/bundle/labview-nxg-systemdesigner/raw/resource/enus/manually-adding-hardware-live-view.html
- document_id: `labview-nxg-systemdesigner`
- page_type: `leaf`
- content_type: `task`
- source_description: Manually add hardware devices that do not automatically appear on the Live diagram. Navigate to the Live view of SystemDesigner. On the document toolbar, click Add Hardware. Follow the instructions for the appropriate device category: Device Category Instructions Network Resources Select the resourc

Manually Adding Hardware to the Live View of SystemDesigner

Manually add hardware devices that do not automatically appear on the Live diagram.

1. Navigate to the Live view of SystemDesigner.
2. On the document toolbar, click 
 Add Hardware.
3. Follow the instructions for the appropriate device category: 
 Device CategoryInstructionsNetwork Resources
 Select the resource on the 
 Add Hardware dialog box and click 
 Add.Missing SystemDesigner Support
 Click 
 Find Support to install required instrument drivers with NI Package Manager. 
 org.dita.html5/xsl/topic.xsl 455Note If you install SystemDesigner support for a device, you may need to restart LabVIEW NXG before the device appears on the Live diagram.Non-Discoverable Devices
 Click 
 Launch NI MAX to find and add the device to the Live diagram manually.Device with known IP address or hostname
 Click the 
 Add hardware by address tab and enter the IP address or hostname of the device to which you want to connect, then click 
 Connect. 
 org.dita.html5/xsl/topic.xsl 455Note A device category only appears when a device in your system meets the criteria for the category.
4. If the device requires login credentials, enter a valid password.
5. Click 
 Add and verify that the device appears on the Live diagram. 
 org.dita.html5/xsl/topic.xsl 455Note If your device still doesn't appear on the Live diagram, refer to your hardware and driver manuals for troubleshooting help.

#### Learn More

Complete the 
 *Getting Started with Instrument Control* lesson in software to learn more about setting up your devices in the Live view.

Related concepts:

- Live View: A Visual Representation of Hardware in Your System

Related tasks:

- Verifying Your Hardware Appears in the Live View
- Validating Your Hardware with Measurement Panels

<!--NI_TOPIC bundle=labview-nxg-systemdesigner path=navigating-systemdesigner.html language=enus -->
## TOPIC 00014: Navigating SystemDesigner

- bundle_id: `labview-nxg-systemdesigner`
- source_path: `navigating-systemdesigner.html`
- source_url: https://docs-be.ni.com/bundle/labview-nxg-systemdesigner/raw/resource/enus/navigating-systemdesigner.html
- document_id: `labview-nxg-systemdesigner`
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

Related concepts:

- SystemDesigner
- Live View: A Visual Representation of Hardware in Your System
- Design View: A Canvas for Designing and Documenting a Hardware System

<!--NI_TOPIC bundle=labview-nxg-systemdesigner path=software-systemdesigner-devices.html language=enus -->
## TOPIC 00015: Software on SystemDesigner Devices

- bundle_id: `labview-nxg-systemdesigner`
- source_path: `software-systemdesigner-devices.html`
- source_url: https://docs-be.ni.com/bundle/labview-nxg-systemdesigner/raw/resource/enus/software-systemdesigner-devices.html
- document_id: `labview-nxg-systemdesigner`
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

Related tasks:

- Adding Software to a Target in the Design View
- Navigating SystemDesigner

<!--NI_TOPIC bundle=labview-nxg-systemdesigner path=swapping-device-models.html language=enus -->
## TOPIC 00016: Swapping Device Models in a System

- bundle_id: `labview-nxg-systemdesigner`
- source_path: `swapping-device-models.html`
- source_url: https://docs-be.ni.com/bundle/labview-nxg-systemdesigner/raw/resource/enus/swapping-device-models.html
- document_id: `labview-nxg-systemdesigner`
- page_type: `leaf`
- content_type: `task`
- source_description: Quickly replace one device model with another in the Design view. Navigate to the Design view. Select the device you want to swap for another device. On the Item tab, select a new device from the Model drop-down menu. Not all devices support the Model drop-down menu. Complete the following tasks if

Swapping Device Models in a System

Quickly replace one device model with another in the Design view.

1. Navigate to the Design view.
2. Select the device you want to swap for another device.
3. On the 
 Item tab, select a new device from the 
 Model drop-down menu. 
 org.dita.html5/xsl/topic.xsl 455Note Not all devices support the 
 Model drop-down menu. Complete the following tasks if the device you want to change doesn't have a 
 Model drop-down menu:
 Delete the device model you no longer want to use and add the desired device model from the palette.(VISA) If the VISA device is [not matched](/csh?topicname=configuring-a-device-match-in-systemdesigner.html) to a device in the Live
 view, type the device you want into either the Vendor or Model
 field. If your VISA device is matched to a device in the Live view,
 you must disable hardware matching before you can replace the device
 on the Design view. On the document toolbar, click Sync»Disable hardware matching to stop matching devices between the SystemDesigner
 views.
4. Optional: 
 Delete broken wires and wire compatible devices together.
5. Optional: 
 Repeat steps 2-4 to replace another device model for a new one.

Parent topic:

Designing a Hardware System in the Design View

Related tasks:

- Designing a Hardware System in the Design View
- Managing Visible Device Ports
- Configuring a Device Match in SystemDesigner

<!--NI_TOPIC bundle=labview-nxg-systemdesigner path=systemdesigner.html language=enus -->
## TOPIC 00017: SystemDesigner

- bundle_id: `labview-nxg-systemdesigner`
- source_path: `systemdesigner.html`
- source_url: https://docs-be.ni.com/bundle/labview-nxg-systemdesigner/raw/resource/enus/systemdesigner.html
- document_id: `labview-nxg-systemdesigner`
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

Related concepts:

- Live View: A Visual Representation of Hardware in Your System
- Design View: A Canvas for Designing and Documenting a Hardware System

Related tasks:

- Navigating SystemDesigner

<!--NI_TOPIC bundle=labview-nxg-systemdesigner path=validating-your-hardware-with-measurement-panels.html language=enus -->
## TOPIC 00018: Validating Your Hardware with Measurement Panels

- bundle_id: `labview-nxg-systemdesigner`
- source_path: `validating-your-hardware-with-measurement-panels.html`
- source_url: https://docs-be.ni.com/bundle/labview-nxg-systemdesigner/raw/resource/enus/validating-your-hardware-with-measurement-panels.html
- document_id: `labview-nxg-systemdesigner`
- page_type: `leaf`
- content_type: `task`
- source_description: Launch a measurement panel from SystemDesigner to validate your hardware, specify measurement inputs and outputs, and configure tasks. It is helpful to think of measurement panels as the same as test panels and tasks in NI MAX or interactive soft front panels available in driver software. Before you

Validating Your Hardware with Measurement Panels

Launch a measurement panel from SystemDesigner to validate your hardware, specify measurement inputs and outputs, and configure tasks.

Tip

- Install the drivers your local machine needs to communicate with and control the hardware.
- Verify SystemDesigner detects your hardware in the
 Live view.

1. Navigate to Live view of SystemDesigner. 
 org.dita.html5/xsl/topic.xsl 455Note If a [device match](/csh?topicname=configuring-a-device-match-in-systemdesigner.html) exists on the Design view, you
 can also launch a measurement panel for the matched device from the Design
 view.
2. Locate the device you want to validate and configure to acquire measurement data.
3. Click the device on the diagram.
4. On the 
 Item tab, expand 
 Use hardware section.
5. Click 
 Create measurement panel to launch a measurement panel.

After you validate and configure your hardware with measurement panels, you can acquire and analyze your measurement data.

Related concepts:

- Live View: A Visual Representation of Hardware in Your System

Related tasks:

- Verifying Your Hardware Appears in the Live View
- Manually Adding Hardware to the Live View of SystemDesigner

<!--NI_TOPIC bundle=labview-nxg-systemdesigner path=verifying-your-hardware-appears-in-the-live-view.html language=enus -->
## TOPIC 00019: Verifying Your Hardware Appears in the Live View

- bundle_id: `labview-nxg-systemdesigner`
- source_path: `verifying-your-hardware-appears-in-the-live-view.html`
- source_url: https://docs-be.ni.com/bundle/labview-nxg-systemdesigner/raw/resource/enus/verifying-your-hardware-appears-in-the-live-view.html
- document_id: `labview-nxg-systemdesigner`
- page_type: `leaf`
- content_type: `task`
- source_description: Use the Live view of SystemDesigner to see all hardware available for use in your application. Depending on your device and connection type, most devices automatically appear on the Live view after you plug them into your local machine. If you have not done so already, plug your devices into your lo

Verifying Your Hardware Appears in the Live View

Use the Live view of SystemDesigner to see all hardware available for use in your application.

Depending on your device and connection type, most devices automatically appear on the Live view after you plug them into your local machine.

1. If you have not done so already, plug your devices into your local machine.
2. Navigate to the Live view of SystemDesigner.
3. Verify your hardware devices are visible on the Live diagram. 
 org.dita.html5/xsl/topic.xsl 455Note Even if you do not have access to physical hardware, you should see your local machine on the Live diagram. SystemDesigner automatically labels your local machine 
 This Computer to help you determine the difference between the computer running LabVIEW NXG—that is, This Computer—and any other PC target you create on the Design view.

If a device in your system does not automatically appear in the Live view, you can [manually add the device](/csh?topicname=manually-adding-hardware-live-view.html) to the Live diagram.

Related concepts:

- Live View: A Visual Representation of Hardware in Your System

Related tasks:

- Manually Adding Hardware to the Live View of SystemDesigner
- Validating Your Hardware with Measurement Panels
