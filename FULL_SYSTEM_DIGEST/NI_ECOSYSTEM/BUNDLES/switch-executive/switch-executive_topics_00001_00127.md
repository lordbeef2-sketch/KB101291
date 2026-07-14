# NI DOCUMENT BUNDLE: switch-executive

<!--NI_BUNDLE_CHUNK bundle=switch-executive start=1 end=127 -->
<!--NI_TOPIC bundle=switch-executive path=activating-your-software.html language=enus -->
## TOPIC 00001: Activating Your Software

- bundle_id: `switch-executive`
- source_path: `activating-your-software.html`
- source_url: https://docs-be.ni.com/bundle/switch-executive/raw/resource/enus/activating-your-software.html
- document_id: `switch-executive`
- page_type: `leaf`
- content_type: `concept`
- source_description: How do I activate my software? Use the Activation Wizard to obtain an activation code for your software. You can launch the Activation Wizard two ways: Launch the product and choose to activate your software from the list of options presented. Launch License Manager by selecting Start»All Programs»N

### Activating Your Software

#### How do I activate my
 software?

Use the Activation Wizard to obtain an activation code for your software. You can
 launch the Activation Wizard two ways:

- Launch the product and choose to activate your software from the list of options
 presented.
- Launch License Manager by selecting Start»All Programs»National
 Instruments»License Manager or from Launcher in Windows 8. Click
 the Activate button in the toolbar.

Note

- If your software is a part of a Volume License Agreement (VLA), contact your
 VLA administrator for installation and activation instructions.
- The software for OS X and Linux operating systems does not require
 activation.

#### What is activation?

Activation is the process of obtaining an activation code to enable your software to
 run on your computer. An activation code is an alphanumeric string that verifies the
 software, version, and computer ID to enable features on your computer. Activation
 codes are unique and are valid on only one computer.

#### What is the Activation
 Wizard?

The Activation Wizard is a part of License Manager that steps you through the process
 of enabling software to run on your machine.

#### What information do I need to
 activate?

You need your product serial number, user name, and organization. The Activation
 Wizard determines the rest of the information. Certain activation methods may
 require additional information for delivery. This information is used only to
 activate your product. Complete disclosure of the software licensing information
 privacy policy is available at ni.com/activate/privacy. If you optionally choose to
 register your software, your information is protected under the privacy policy,
 available at ni.com/privacy.

#### How do I find my product serial
 number?

Your serial number uniquely identifies your purchase of software. You can find your
 serial number on the Certificate of Ownership included in your software kit. If your
 software kit does not include a Certificate of Ownership, you can find your serial
 number on the product packing slip or on the shipping label.

If you have installed a previous version using your serial number, you can find the
 serial number by selecting the Help»About menu item within
 the application or by selecting your product within License Manager
 (Start»All Programs»National Instruments»License Manager
 or from Launcher in Windows 8).

#### What is a Computer ID?

The computer ID contains unique information about your computer. This information is
 required to enable your software. You can find your computer ID through the
 Activation Wizard or by using License Manager, as follows:

1. Launch License Manager by selecting Start»All Programs»National
 Instruments»License Manager or from Launcher in Windows 8.
2. Click the Display Computer Information button in the
 toolbar.

#### How can I evaluate NI
 software?

You can install and run most application software in evaluation mode. This mode lets
 you use a product with certain limitations, such as reduced functionality or limited
 execution time. Refer to your product documentation for specific information on the
 product's evaluation mode.

#### Moving Software After
 Activation

To transfer your software to another computer, install and activate it on the second
 computer. You are not prohibited from transferring your software from one computer
 to another. Because activation codes are unique to each computer, you will need a
 new activation code. Refer to the How do I activate my software? section of this
 topic to learn how to acquire a new activation code and reactivate your
 software.

#### Deactivating a Product

To deactivate a product and return the product to the state it was in before you
 activated it, right-click the product in the License Manager tree and select
 Deactivate. If the product was in evaluation mode before
 you activated it, the properties of the evaluation mode may not be restored.

#### Using Windows Guest Accounts

License Manager does not support Microsoft Windows Guest accounts. You must log in to
 a non-Guest account to run licensed application software.

Parent topic:

Getting Started

<!--NI_TOPIC bundle=switch-executive path=adding-a-hardwire.html language=enus -->
## TOPIC 00002: Adding a Hardwire

- bundle_id: `switch-executive`
- source_path: `adding-a-hardwire.html`
- source_url: https://docs-be.ni.com/bundle/switch-executive/raw/resource/enus/adding-a-hardwire.html
- document_id: `switch-executive`
- page_type: `leaf`
- content_type: `concept`
- source_description: Complete the following steps to add a hardwire: Launch MAX with Switch Executive. Expand Devices and Interfaces»Switch Executive Virtual Devices. Select the Switch Executive virtual device to modify and navigate to the Schematic Configuration tab. Verify that the required switch device is selected i

### Adding a Hardwire

Complete the following steps to add a hardwire:

1. Launch MAX with Switch Executive.
2. Expand Devices and Interfaces»Switch Executive Virtual Devices .
3. Select the Switch Executive virtual device to modify and navigate to the Schematic
 Configuration tab.
4. Verify that the required switch device is selected in the Devices listbox and its schematic appears in the Schematic window.
5. Click a channel in the Schematic window to access the Edit Alias & Hardwire dialog box.
6. Type an alias name for the channel in the Alias Name textbox.
7. Select the Hardwires tab.
8. Click in the
 Available Hardwires listbox. Switch Executive adds a new
 hardwire, with a predefined name, to the Available Hardwires listbox. To edit a
 hardwire name, click the hardwire name and press <F2>.
9. (Optional) Click Associate channelName with hardwireName , where
 channelName and hardwireName are variables, depending
 on the channel and hardwire you want to associate. Switch Executive adds the channel
 to the Associated Channels listbox.
10. Click OK . The hardwire number appends as a superscript to the channel
 name in the Schematic window.
11. Click on the
 Switch Executive taskbar to save the changes.

Parent topic:

Schematic Configuration

<!--NI_TOPIC bundle=switch-executive path=adding-a-route-group.html language=enus -->
## TOPIC 00003: Adding a Route Group

- bundle_id: `switch-executive`
- source_path: `adding-a-route-group.html`
- source_url: https://docs-be.ni.com/bundle/switch-executive/raw/resource/enus/adding-a-route-group.html
- document_id: `switch-executive`
- page_type: `leaf`
- content_type: `concept`
- source_description: Complete the following steps to add a route group: Launch MAX with Switch Executive.Expand Devices and Interfaces»Switch Executive Virtual Devices. Select the Switch Executive virtual device to modify and navigate to the Schematic Configuration tab. Click at the top of the Routes and Route Groups li

### Adding a Route Group

Complete the following steps to add a route group:

1. Launch MAX with Switch Executive.
2. Expand Devices and Interfaces»Switch Executive Virtual Devices .
3. Select the Switch Executive virtual device to modify and navigate to the Schematic
 Configuration tab.
4. Click at the
 top of the Routes and Route Groups listbox. Switch Executive
 creates an empty route group with a default name,
 RouteGroupX . Note If the virtual device does not
 have any route groups defined, Switch Executive creates a default route group,
 RouteGroup0, in the Routes and Route
 Groups listbox.
5. (Optional) Right-click the route group and select Rename , or click the route group and press <F2> to edit a route group name.
6. Click on the
 Switch Executive taskbar to save the changes.

Parent topic:

Schematic Configuration

<!--NI_TOPIC bundle=switch-executive path=adding-a-route.html language=enus -->
## TOPIC 00004: Adding a Route

- bundle_id: `switch-executive`
- source_path: `adding-a-route.html`
- source_url: https://docs-be.ni.com/bundle/switch-executive/raw/resource/enus/adding-a-route.html
- document_id: `switch-executive`
- page_type: `leaf`
- content_type: `concept`
- source_description: Complete the following steps to add a route: Launch MAX with Switch Executive.Expand Devices and Interfaces»Switch Executive Virtual Devices. Select the Switch Executive virtual device to modify and navigate to the Schematic Configuration tab. Click the switch device to which you want to add a route

### Adding a Route

Complete the following steps to add a route:

1. Launch MAX with Switch Executive.
2. Expand Devices and Interfaces»Switch Executive Virtual Devices .
3. Select the Switch Executive virtual device to modify and navigate to the Schematic
 Configuration tab.
4. Click the switch device to which you want to add a route in the Devices 
 listbox. Switch Executive displays the device schematic in the
 Schematic window.
5. Enable the Show Routes checkbox below the Routes and Route Groups listbox.
6. Complete one of the following steps to add a route:
  - Add a route not associated with a route
 group —Click above the Routes and Route Groups 
 listbox. Tip You can also
 right-click in the Routes and Route Groups listbox and select
 Add Route»Empty Route.
  - Add a route associated with a route
 group —Click the route group to which you want to add a route in the
 Routes and Route Groups listbox. You can add a route to an
 existing route group or create a new route group to which to add a
 route. Note If the virtual
 device does not have any existing route groups defined, Switch Executive creates a
 default route group, RouteGroup0, in the Routes and Route
 Groups listbox to which you can add a route.
7. Complete one of the following steps depending on the topology of the switch device selected to
 create a route between channels: The route displays in the Schematic window and is added to the
 Routes and Route Groups listbox. A checkmark displays to the right
 of the device name in the Devices listbox to indicate a route exists
 on the device. Note Clicking on
 the same crosspoint or channel connection point in a different route group creates a new
 route on the virtual device.
  - General purpose topology —Click a crosspoint between two
 channels on the specific relay you want to use in the Schematic 
 window.
  - Matrix topology —Click a crosspoint between two channels in
 the Schematic window.
  - Multiplexer topology —Click a channel connection point in
 the Schematic window.
  - Third-party IVI-switch and independent topologies —Select one
 channel from the Channel 1 listbox and one channel from
 the Channel 2 listbox and
 click Create .
8. (Optional) Edit the route name.
9. Click on
 the Switch Executive taskbar to save the changes.

Parent topic:

Schematic Configuration

Related concepts:

- Adding a Route Group
- Independent Topologies
- Editing a Route

<!--NI_TOPIC bundle=switch-executive path=adding-buses.html language=enus -->
## TOPIC 00005: Adding Buses

- bundle_id: `switch-executive`
- source_path: `adding-buses.html`
- source_url: https://docs-be.ni.com/bundle/switch-executive/raw/resource/enus/adding-buses.html
- document_id: `switch-executive`
- page_type: `leaf`
- content_type: `concept`
- source_description: Complete the following steps to add a bus: Launch MAX with Switch Executive. Expand Devices and Interfaces»Switch Executive Virtual Devices. Select the Switch Executive virtual device to modify. Click the Hardwires/Buses tab. Click at the top of the Buses listbox to add a bus. Type a name for the bu

### Adding Buses

Complete the following steps to add a bus:

1. Launch MAX with Switch Executive.
2. Expand Devices and Interfaces»Switch Executive Virtual Devices .
3. Select the Switch Executive virtual device to modify.
4. Click the Hardwires/Buses tab.
5. Click at the
 top of the Buses listbox to add a bus.
6. Type a name for the bus in the Name textbox or accept the predefined alias of the bus.
7. Select a switch to associate with the bus from the IVI Switches listbox.
8. Enable the Connect to Bus checkbox.
9. Select a channel from the Base Channel pull-down menu. The base channel is the first channel of the series of hardwires that are created.
10. Select the last channel in the series of created hardwires from the End
 Channel pull-down menu. Note Some switch devices do not
 support creating multi-channel buses. If the switch device you selected from the
 IVI Switches listbox does not support multi-channel
 bus creation, you will only be able to select the same channel from the
 End Channel pull-down menu as the channel selected in
 the Base Channel pull-down menu.
11. Accept the predefined Hardwire Start Index value or type a new number in
 the Hardwire Start Index textbox. This value is the first
 number appended to the end of the generated hardwires. For example, if the start
 index is 2, BusName2 , BusName3 ,
 BusName4 , and so on are the default names created, where
 BusName is the name of the newly created bus.
12. Select another switch from the IVI Switches listbox to associate with the bus.
13. Enable the Connect to Bus checkbox.
14. Select a channel from the Base Channel pull-down menu.
15. Select the last channel in the series of created hardwires from the End Channel pull-down menu.
16. Accept the predefined Hardwire Start Index value or type a new number in the Hardwire Start Index textbox.
17. Type any comments you have in the Comment textbox.
18. Repeat steps 12 through 16 for any additional switches associated with the bus.
19. Click on the
 Switch Executive taskbar to save the changes.

Note

hardwires

#### Converting Buses to Hardwires

For additional granularity, a bus can be converted to individual
 hardwires.

Complete the following steps to convert a bus to individual
 hardwires.

Caution

1. Launch MAX with Switch Executive.
2. Expand Devices and Interfaces»Switch Executive Virtual
 Devices .
3. Select the Switch Executive virtual device to modify.
4. Click the Hardwires/Buses tab.
5. Right-click the bus you want to convert to individual hardwires from the
 Buses listbox and select Convert Bus to
 Hardwires .
6. Click Yes to complete converting the bus to individual
 hardwires.

Parent topic:

Hardwires/Buses Tab

Related concepts:

- Hardwire

<!--NI_TOPIC bundle=switch-executive path=adding-custom-data.html language=enus -->
## TOPIC 00006: Adding Custom Data

- bundle_id: `switch-executive`
- source_path: `adding-custom-data.html`
- source_url: https://docs-be.ni.com/bundle/switch-executive/raw/resource/enus/adding-custom-data.html
- document_id: `switch-executive`
- page_type: `leaf`
- content_type: `concept`
- source_description: You can add your own custom data and charts. This data is ignored at import but is saved in the workbook.

### Adding Custom Data

You can add your own custom data and charts. This data is ignored at import but is saved in the
 workbook.

Parent topic:

Managing a Virtual Device in Excel

<!--NI_TOPIC bundle=switch-executive path=adding-hardwires-to-define-multidevice-topolo.html language=enus -->
## TOPIC 00007: Adding Hardwires to Define Multidevice Topologies

- bundle_id: `switch-executive`
- source_path: `adding-hardwires-to-define-multidevice-topolo.html`
- source_url: https://docs-be.ni.com/bundle/switch-executive/raw/resource/enus/adding-hardwires-to-define-multidevice-topolo.html
- document_id: `switch-executive`
- page_type: `leaf`
- content_type: `concept`
- source_description: Complete the following steps to define a hardwire: Launch MAX with Switch Executive. Expand Devices and Interfaces»Switch Executive Virtual Devices. Select the Switch Executive virtual device to modify. Click the Hardwires/Buses tab. Click at the top of the Hardwires listbox to add a hardwire. Type

### Adding Hardwires to Define Multidevice Topologies

Complete the following steps to define a hardwire:

1. Launch MAX with Switch Executive.
2. Expand Devices and Interfaces»Switch Executive Virtual Devices .
3. Select the Switch Executive virtual device to modify.
4. Click the Hardwires/Buses tab.
5. Click at the
 top of the Hardwires listbox to add a hardwire.
6. Type a name for the hardwire in the Name textbox or the accept the predefined alias of the hardwire.
7. Select the channels that are associated with the hardwire in the Available
 Channels listbox and move them to the Associated
 Channels listbox by clicking .
8. Type any comments you have in the Comment textbox.
9. Click on the
 Switch Executive taskbar to save the changes.

To continue configuring your Switch Executive virtual device, refer to *Adding Route
 Groups*.

Parent topic:

Hardwires/Buses Tab

Related concepts:

- Adding Route Groups

<!--NI_TOPIC bundle=switch-executive path=adding-ivi-switches.html language=enus -->
## TOPIC 00008: Adding IVI Switches

- bundle_id: `switch-executive`
- source_path: `adding-ivi-switches.html`
- source_url: https://docs-be.ni.com/bundle/switch-executive/raw/resource/enus/adding-ivi-switches.html
- document_id: `switch-executive`
- page_type: `leaf`
- content_type: `concept`
- source_description: Complete the following steps to add an IVI switch to an existing Switch Executive virtual device: Launch MAX with Switch Executive.Expand Devices and Interfaces»Switch Executive Virtual Devices. Right-click the virtual device that you want to modify and select Add IVI Switch. The Add Device dialog b

### Adding IVI Switches

Complete the following steps to add an IVI switch to an existing Switch Executive virtual
 device:

1. Launch MAX with Switch Executive.
2. Expand Devices and Interfaces»Switch Executive Virtual Devices .
3. Right-click the virtual device that you want to modify and select Add IVI Switch . The Add Device dialog box appears.
4. Select the switches you want to add from the Available Switches listbox
 and click to move them to the Switches to
 Add listbox. Note If you are using National
 Instrument switches, click Configure to configure the
 settings of those switches before you add them to the Switches to
 Add listbox.If you are using *third-party switches*,
 select the IVI logical name you created.
5. Click Next . The new device is added to your configuration.
6. Click Finish .
7. Click on the
 Switch Executive taskbar to save the changes.

Refer to *Configuring Channels* to continue configuring your NI Switch Executive
 virtual device.

Parent topic:

Configuring IVI Switches

Related concepts:

- Using Third-Party Switches
- Configuring Channels

<!--NI_TOPIC bundle=switch-executive path=adding-mutual-exclusions.html language=enus -->
## TOPIC 00009: Adding Mutual Exclusions

- bundle_id: `switch-executive`
- source_path: `adding-mutual-exclusions.html`
- source_url: https://docs-be.ni.com/bundle/switch-executive/raw/resource/enus/adding-mutual-exclusions.html
- document_id: `switch-executive`
- page_type: `leaf`
- content_type: `concept`
- source_description: Complete the following steps to add a mutual exclusion: Launch MAX with Switch Executive. Expand Devices and Interfaces»Switch Executive Virtual Devices. Select the Switch Executive virtual device to modify. Click the Channels/Exclusions tab. Click at the top of the Exclusions listbox to add a mutua

### Adding Mutual Exclusions

Complete the following steps to add a mutual exclusion:

1. Launch MAX with Switch Executive.
2. Expand Devices and Interfaces»Switch Executive Virtual Devices .
3. Select the Switch Executive virtual device to modify.
4. Click the Channels/Exclusions tab.
5. Click at the
 top of the Exclusions listbox to add a mutual exclusion.
6. Type a name for the exclusion in the Name textbox or accept the predefined name.
7. Select the channels to exclude from the Available Channels listbox and
 click to add each channel to the Mutually Excluded Channels 
 listbox.
8. Type any comments you have in the Comment textbox. Note If needed, select the
 Disabled checkbox to disable the exclusion.
9. Click on the
 Switch Executive taskbar to save the changes.

Parent topic:

Channels/Exclusions Tab

<!--NI_TOPIC bundle=switch-executive path=adding-route-groups.html language=enus -->
## TOPIC 00010: Adding Route Groups

- bundle_id: `switch-executive`
- source_path: `adding-route-groups.html`
- source_url: https://docs-be.ni.com/bundle/switch-executive/raw/resource/enus/adding-route-groups.html
- document_id: `switch-executive`
- page_type: `leaf`
- content_type: `concept`
- source_description: Complete the following steps to add a route group: Launch MAX with Switch Executive. Expand Devices and Interfaces»Switch Executive Virtual Devices. Select the Switch Executive virtual device that you want to modify. Click the Routes/Groups tab. Click to create a route group. Type a name for the rou

### Adding Route Groups

Complete the following steps to add a route group:

1. Launch MAX with Switch Executive.
2. Expand Devices and Interfaces»Switch Executive Virtual Devices .
3. Select the Switch Executive virtual device that you want to modify.
4. Click the Routes/Groups tab.
5. Click to create
 a route group.
6. Type a name for the route group in the Name textbox or accept the predefined alias of the route group.
7. Drag and drop the routes and/or route groups in the Routes and Route
 Groups listbox onto the route group to populate the route group.
 Another way to add routes and/or route groups is through the Available
 Routes and Route Groups listbox. Select the routes and/or route
 groups you want to associate with the route group you created and move them to the
 Child Routes and Route Groups listbox by clicking .
8. Type any comments you have in the Comment textbox.
9. Click on the
 Switch Executive taskbar to save the changes.

To continue configuring your Switch Executive virtual device, refer to *Adding
 Routes*.

Parent topic:

Routes/Groups Tab

Related concepts:

- Adding Routes

<!--NI_TOPIC bundle=switch-executive path=adding-routes-with-the-path-editor.html language=enus -->
## TOPIC 00011: Adding Routes with the Path Editor

- bundle_id: `switch-executive`
- source_path: `adding-routes-with-the-path-editor.html`
- source_url: https://docs-be.ni.com/bundle/switch-executive/raw/resource/enus/adding-routes-with-the-path-editor.html
- document_id: `switch-executive`
- page_type: `leaf`
- content_type: `concept`
- source_description: Another method of creating or modifying a route is to use the path editor below the Visual Route Editor window. The path editor is automatically populated with the route specification string based on the selections you have made in the Visual Route Editor window. To use the path editor, type the rou

### Adding Routes with the Path Editor

Another method of creating or modifying a route is to use the path editor below the
 Visual Route Editor window.

[IMAGE alt='image' src='GUID-8D8CC204-80A2-491D-A5A3-370D029ACBCA-a5.gif']

The path editor is automatically populated with the route specification string based on
 the selections you have made in the Visual Route Editor window.

To use the path editor, type the route path in the path editor textbox in the appropriate
 format, and press <Enter> to apply your changes. Click Save
 to save your changes, or click Clear to cancel your changes.
 Refer to *Route Specification Strings* for more information.

Parent topic:

Routes/Groups Tab

Related concepts:

- Route Specification Strings

<!--NI_TOPIC bundle=switch-executive path=adding-routes.html language=enus -->
## TOPIC 00012: Adding Routes

- bundle_id: `switch-executive`
- source_path: `adding-routes.html`
- source_url: https://docs-be.ni.com/bundle/switch-executive/raw/resource/enus/adding-routes.html
- document_id: `switch-executive`
- page_type: `leaf`
- content_type: `concept`
- source_description: Complete the following steps to add a route: Launch MAX with Switch Executive. Expand Devices and Interfaces»Switch Executive Virtual Devices. Select the Switch Executive virtual device that you want to modify. Click the Routes/Groups tab. Click to add a new route. A new route appears selected in th

### Adding Routes

Complete the following steps to add a route:

1. Launch MAX with Switch Executive.
2. Expand Devices and Interfaces»Switch Executive Virtual Devices .
3. Select the Switch Executive virtual device that you want to modify.
4. Click the Routes/Groups tab.
5. Click to add a
 new route. A new route appears selected in the list of routes.
6. Type a name for the route in the Name textbox or accept the predefined alias of the route.
7. Type any comments you may have in the Comment field.
8. Select the default multiconnect behavior intended for the route in the Multiconnect Mode drop-down listbox:
  - Multiconnect Routes —Allows Switch Executive to use this route between
 multiple calls.
  - No Multiconnect —Prevents sharing between multiple calls.
9. Click the Route Groups tab.
10. Select the route group(s) that you want to associate with the route from the
 Available Route Groups listbox and click to move the
 route groups to the Parent Route Groups list. Tip You can also associate a route with a route
 group by dragging the route and dropping it on top of the route group in the
 Routes and Route Groups listbox. Route groups help
 Switch Executive identify unintentional cross-connects. For example, if you are creating a
 test system, it is likely that you are using multiple routes at the same time. To ensure
 that these routes do not cross paths unintentionally, they must be dependent on one another.
 Use groups to prevent future errors when using your Switch Executive virtual device.
11. (Optional) Click the Route Specifications tab and set route constraints.
 The values in this tab filter endpoints in the Visual Route Editor window based on the
 specifications of the route and/or the wiring mode of the switch module. Tip You can use scientific units in this tab.
 For example, instead of entering 1000000, you can enter
 1M, or you can enter 1m for 0.001.
12. Complete the following steps to define endpoints—or the beginning and end of the route
 path—using the two tables in the Visual Route Editor window as shown
 in the following figure: [IMAGE alt='image' src='GUID-A294E7BF-AE8B-4C2A-A8B2-D08DCE087299-a5.png']
  1. Select the first endpoint of the route in the Endpoint 1 
 table.
  2. Select the second endpoint of the route in the Endpoint 2 
 table. The path editor automatically populates with the route specification
 string that designates your route path. Tip Experiment with route selections to see
 how your changes affect the route specification string of a route path. Status
 icons, 
 and ,
 below the path editor indicate if there are any errors or warnings or if the path is
 valid.
  3. (Optional) Click Channels Only to enable visibility of the
 switch box between the Endpoint 1 and Endpoint 2 tables, as show in the following figure: [IMAGE alt='image' src='GUID-3480458D-1C9B-4F75-9056-8381908A14E0-a5.png'] Note By default, the
 switch box does not display between the Endpoint 1 and Endpoint 2 tables. If you do
 not see the switch box, click Channels Only. If the
 two endpoints can be connected, a solid black line displays between the two selected
 endpoints, indicating that the path is complete. [IMAGE alt='image' src='GUID-78A5ADD8-132C-441B-BF3A-E048F45F486A-a5.gif'] If the route path is invalid, the lines between the channels display as dashed
 red lines. [IMAGE alt='image' src='GUID-7D7ECFA8-908A-43A8-9622-84850D0957CA-a5.gif'] If you want to modify the path selected, you can use the path editor 
 to make your changes.
13. (Optional) Define hardwires to complete the route. Note Hardwires are defined
 by a user. For information about defining new hardwires, refer to *Adding Hardwires
 to Define Multidevice Topologies*.
  - If the two endpoints are in separate switch modules physically connected by a
 hardwire, use the drop-down listbox that opens between the two endpoint tables to select
 another hardwire to complete the route. You can use the drop-down listbox
 to manually select different routing channels and hardwires. [IMAGE alt='image' src='GUID-E04B936B-B608-4D4C-A951-AE60CA3E28B0-a5.gif'] Note The drop-down
 listbox will only display if the switch box has been enabled by clicking
 Channels Only.
  - If the two endpoints of a route are in separate switch modules connected by one or
 more intermediate switches, you must define the hardwires that connect them.
14. (Optional) Click Retry to attempt rerouting if you made changes to your virtual device configuration that might cause a route to 
 become invalid, for example, adding/removing hardwires or exclusions.
15. Click on the
 Switch Executive taskbar to save the changes.

Parent topic:

Routes/Groups Tab

Related concepts:

- Adding Routes with the Path Editor
- Hardwire
- Adding Hardwires to Define Multidevice Topologies

<!--NI_TOPIC bundle=switch-executive path=adding-set-exclusions.html language=enus -->
## TOPIC 00013: Adding Set Exclusions

- bundle_id: `switch-executive`
- source_path: `adding-set-exclusions.html`
- source_url: https://docs-be.ni.com/bundle/switch-executive/raw/resource/enus/adding-set-exclusions.html
- document_id: `switch-executive`
- page_type: `leaf`
- content_type: `concept`
- source_description: Complete the following steps to add a set exclusion: Launch MAX with Switch Executive. Expand Devices and Interfaces»Switch Executive Virtual Devices. Select the Switch Executive virtual device to modify. Click the Channels/Exclusions tab. Click at the top of the Exclusions listbox to add a set excl

### Adding Set Exclusions

Complete the following steps to add a set exclusion:

1. Launch MAX with Switch Executive.
2. Expand Devices and Interfaces»Switch Executive Virtual Devices .
3. Select the Switch Executive virtual device to modify.
4. Click the Channels/Exclusions tab.
5. Click at the
 top of the Exclusions listbox to add a set exclusion.
6. Type a name for the exclusion in the Name textbox or accept the predefined name.
7. Select the channels to exclude from the Available Channels listbox and
 move them to the Set 1 Channels listbox or Set 2
 Channels listbox by clicking and
 . Note If you cannot
 see enough information in each listbox column to make your choices, try hiding
 the MAX configuration tree to create more space in the user interface.
8. Type any comments you have in the Comment textbox.
9. Click on the
 Switch Executive taskbar to save the changes.

Parent topic:

Channels/Exclusions Tab

<!--NI_TOPIC bundle=switch-executive path=batch-renaming.html language=enus -->
## TOPIC 00014: Batch Renaming

- bundle_id: `switch-executive`
- source_path: `batch-renaming.html`
- source_url: https://docs-be.ni.com/bundle/switch-executive/raw/resource/enus/batch-renaming.html
- document_id: `switch-executive`
- page_type: `leaf`
- content_type: `concept`
- source_description: Working with systems of large channel counts may require you to rename large selections of channels, routes, route groups, and so on. Switch Executive offers a method for renaming large Switch Executive virtual device objects with a sequential naming scheme. For example, you can select a large numbe

### Batch Renaming

Working with systems of large channel counts may require you to rename large selections of
 channels, routes, route groups, and so on. Switch Executive offers a method for renaming
 large Switch Executive virtual device objects with a sequential naming scheme. For
 example, you can select a large number of objects and rename them
 Object_X.

Complete the following steps to rename a set of objects:

1. Launch MAX with Switch Executive.
2. Expand Devices and Interfaces»Switch Executive Virtual Devices .
3. Select the Switch Executive virtual device to modify.
4. Click the extended configuration tab that contains the objects you want to rename.
5. Select the objects you want to rename. You can hold down <Shift> or <Ctrl> and click to select multiple objects.
6. Click on the
 Switch Executive taskbar. If this button is not visible, click to
 expand the taskbar. The Batch Rename dialog box opens.
7. Use and to
 order the objects in the Items to Rename listbox.
 Switch Executive renames objects sequentially based on their order in this
 list. Note The
 initial order of the objects in the Items to Rename
 listbox reflects the order in which the objects were selected.
8. Type a base name for the objects in the Base Name textbox.
 Switch Executive uses this name as the prefix for all the selected objects.
9. Type a number in the Start Index textbox. Switch Executive appends this
 number to the name of the first object in the Items to Rename 
 listbox. For each object thereafter, Switch Executive increments the number by one
 and appends it to the name.
10. Click Okay . Switch Executive batch renames the objects based on the
 values you entered in the Base Name and Start
 Index textboxes. For example, with a base name of
 Object and a start index of 1 ,
 Switch Executive renames the objects Object1 ,
 Object2 , Object3 , and so on.
11. Click on the
 Switch Executive taskbar to save the changes.

Parent topic:

Extended Configuration

Related concepts:

- Extended Configuration

<!--NI_TOPIC bundle=switch-executive path=bus.html language=enus -->
## TOPIC 00015: Bus

- bundle_id: `switch-executive`
- source_path: `bus.html`
- source_url: https://docs-be.ni.com/bundle/switch-executive/raw/resource/enus/bus.html
- document_id: `switch-executive`
- page_type: `leaf`
- content_type: `concept`
- source_description: A bus is a group of hardwires associated with a single alias name. Buses are particularly helpful when hardwires are used for column or row expansion in a matrix where a series of channels are connected to another series of channels.Hardwires cannot belong to more than one bus. Hardwires are not req

### Bus

bus

Note

Parent topic:

Fundamentals

Related concepts:

- Schematic Configuration
- Extended Configuration
- Using the Configuration API

<!--NI_TOPIC bundle=switch-executive path=channel.html language=enus -->
## TOPIC 00016: Channel

- bundle_id: `switch-executive`
- source_path: `channel.html`
- source_url: https://docs-be.ni.com/bundle/switch-executive/raw/resource/enus/channel.html
- document_id: `switch-executive`
- page_type: `leaf`
- content_type: `concept`
- source_description: A channel represents a connection point on a switch module. A channel can have multiple wires and can be associated with a hardwire. A relay name is not necessarily a channel.

### Channel

A *channel* represents a connection point on a switch module. A channel can have
 multiple wires and can be associated with a hardwire. A relay name is not necessarily a
 channel.

Parent topic:

Fundamentals

Related concepts:

- Schematic Configuration
- Extended Configuration
- Using the Configuration API

<!--NI_TOPIC bundle=switch-executive path=channels-exclusions-tab.html language=enus -->
## TOPIC 00017: Channels/Exclusions Tab

- bundle_id: `switch-executive`
- source_path: `channels-exclusions-tab.html`
- source_url: https://docs-be.ni.com/bundle/switch-executive/raw/resource/enus/channels-exclusions-tab.html
- document_id: `switch-executive`
- page_type: `leaf`
- content_type: `concept`
- source_description: Connecting one signal input to another signal input can create a potentially hazardous and destructive situation. Refer to Exclusion for more information. Use the Channels/Exclusions tab to configure channels and define exclusions in Switch Executive.

### Channels/Exclusions Tab

Caution

Exclusion

Use the Channels/Exclusions tab to configure channels and define
 exclusions in Switch Executive.

[IMAGE alt='image' src='GUID-814D3E57-820D-4EFF-B0C2-6CAAFD620A54-a5.png']

Parent topic:

Extended Configuration

Related concepts:

- Exclusion

<!--NI_TOPIC bundle=switch-executive path=closing-a-session.html language=enus -->
## TOPIC 00018: Closing a Session

- bundle_id: `switch-executive`
- source_path: `closing-a-session.html`
- source_url: https://docs-be.ni.com/bundle/switch-executive/raw/resource/enus/closing-a-session.html
- document_id: `switch-executive`
- page_type: `leaf`
- content_type: `concept`
- source_description: Close a session to end communication between the Switch Executive virtual device and the software.To close a session, use the niSE Close Session VI or the niSE_CloseSession function.

### Closing a Session

Close a session to end communication between the Switch Executive virtual device and the
 software.

To close a session, use the *niSE Close Session* VI or the
 *niSE_CloseSession* function.

Parent topic:

Programming Flow

<!--NI_TOPIC bundle=switch-executive path=concepts.html language=enus -->
## TOPIC 00019: Concepts

- bundle_id: `switch-executive`
- source_path: `concepts.html`
- source_url: https://docs-be.ni.com/bundle/switch-executive/raw/resource/enus/concepts.html
- document_id: `switch-executive`
- page_type: `leaf`
- content_type: `concept`
- source_description: This section conatins information about conceptual information related to using an Switch Executive virtual device.

### Concepts

This section conatins information about conceptual information related to using an Switch
 Executive virtual device.

Parent topic:

Switch Executive Help

<!--NI_TOPIC bundle=switch-executive path=configuration-1.html language=enus -->
## TOPIC 00020: Configuration

- bundle_id: `switch-executive`
- source_path: `configuration-1.html`
- source_url: https://docs-be.ni.com/bundle/switch-executive/raw/resource/enus/configuration-1.html
- document_id: `switch-executive`
- page_type: `leaf`
- content_type: `concept`
- source_description: Configure a virtual device to create new definitions and modify existing configuration data of the switches, channels, hardwires, buses, exclusions, routes, and route groups that compose a virtual device.Some examples of configuration tasks include: Adding or removing an IVI switch from a virtual de

### Configuration

Configure a virtual device to create new definitions and modify existing configuration data of
 the switches, channels, hardwires, buses, exclusions, routes, and route groups that
 compose a virtual device.

Some examples of configuration tasks include:

- Adding or removing an IVI switch from a virtual device
- Configuring channels
- Defining an exclusion to create a connection rule
- Adding hardwires and/or a bus to define multidevice topologies
- Adding routes
- Adding route groups

Parent topic:

Concepts

Related concepts:

- Configuring a Virtual Device
- Using the Configuration API

<!--NI_TOPIC bundle=switch-executive path=configuring-a-channel.html language=enus -->
## TOPIC 00021: Configuring a Channel

- bundle_id: `switch-executive`
- source_path: `configuring-a-channel.html`
- source_url: https://docs-be.ni.com/bundle/switch-executive/raw/resource/enus/configuring-a-channel.html
- document_id: `switch-executive`
- page_type: `leaf`
- content_type: `concept`
- source_description: Complete the following steps to configure a channel: Launch MAX with Switch Executive. Expand Devices and Interfaces»Switch Executive Virtual Devices. Select the Switch Executive virtual device to modify and navigate to the Schematic Configuration tab. Click the device that contains the channel that

### Configuring a Channel

Complete the following steps to configure a channel:

1. Launch MAX with Switch Executive.
2. Expand Devices and Interfaces»Switch Executive Virtual Devices .
3. Select the Switch Executive virtual device to modify and navigate to the Schematic
 Configuration tab.
4. Click the device that contains the channel that you want to configure in the
 Devices listbox. Switch Executive displays the device
 schematic in the Schematic window.
5. Click a channel in the Schematic window to access the Edit Alias & Hardwire dialog box.
6. Type a new alias name or edit the existing alias of the channel in the Alias Name textbox.
7. Select the Hardwires tab to designate whether the channel is associated with a hardwire.
  1. Select the hardwire that you want to associate with the channel, or create a new hardwire to associate, in the Available Hardwires listbox.
  2. Click Associate channelName with
 hardwireName , where
 channelName and hardwireName are
 variables, depending on the channel and hardwire you want to associate.
 Switch Executive adds the channel to the Associated Channels listbox.
8. Click OK to accept the configuration. The hardwire number appends as a
 superscript to the channel name in the Schematic window.
9. Click on the
 Switch Executive taskbar to save the changes.

Parent topic:

Schematic Configuration

Related concepts:

- Adding a Hardwire

<!--NI_TOPIC bundle=switch-executive path=configuring-a-virtual-device.html language=enus -->
## TOPIC 00022: Configuring a Virtual Device

- bundle_id: `switch-executive`
- source_path: `configuring-a-virtual-device.html`
- source_url: https://docs-be.ni.com/bundle/switch-executive/raw/resource/enus/configuring-a-virtual-device.html
- document_id: `switch-executive`
- page_type: `leaf`
- content_type: `concept`
- source_description: Use schematic and/or extended configuration in MAX to configure an Switch Executive virtual device.The following table lists the configuration tasks you can perform using schematic configuration and extended configuration: Schematic Configuration Extended Configuration Add Channel Aliases √ √ Add/Re

### Configuring a Virtual Device

Use *schematic* and/or *extended* configuration in MAX to configure an
 Switch Executive virtual device.

The following table lists the configuration tasks you can perform using schematic configuration
 and extended configuration:

|  | Schematic Configuration | Extended Configuration |
| --- | --- | --- |
| Add Channel Aliases | √ | √ |
| Add/Remove Route Groups | √ | √ |
| Nest Route Groups | √ | √ |
| Add/Remove Routes | √ | √ |
| Add/Remove Hardwires | √ | √ |
| Add/Remove Exclusions | N/A | √ |
| Add/Remove Buses | N/A | √ |

Parent topic:

Using Switch Executive in MAX

Related concepts:

- Schematic Configuration
- Extended Configuration

<!--NI_TOPIC bundle=switch-executive path=configuring-channels.html language=enus -->
## TOPIC 00023: Configuring Channels

- bundle_id: `switch-executive`
- source_path: `configuring-channels.html`
- source_url: https://docs-be.ni.com/bundle/switch-executive/raw/resource/enus/configuring-channels.html
- document_id: `switch-executive`
- page_type: `leaf`
- content_type: `concept`
- source_description: When adding a new device to the virtual device, Switch Executive automatically queries the switch and adds its channels, and their specifications, to the channel list. Each channel has a list of predefined attributes, as shown in the following figure: If the attribute table is not visible, click. Co

### Configuring Channels

When adding a new device to the virtual device, Switch Executive automatically queries the switch
 and adds its channels, and their specifications, to the channel list. Each channel has a list
 of predefined attributes, as shown in the following figure:

[IMAGE alt='image' src='GUID-C02BFFC0-4B2F-4C0A-8F15-6265F739EC5A-a5.png']

Tip

[IMAGE alt='image' src='GUID-C79972D9-E42C-4328-8A3C-C9F7CFDF1C64-a5.gif']

Complete the following steps to configure channels:

1. Launch MAX with Switch Executive.
2. Expand Devices and Interfaces»Switch Executive Virtual Devices .
3. Select the Switch Executive virtual device to modify.
4. Click the Channels/Exclusions tab.
5. Select a channel to configure.
6. Accept the default alias of the channel, or modify it in the Alias 
 textbox. Note Some characters
 are *reserved* and cannot be used in channel names.
7. Type any comments you may have in the Comment textbox. Tip Use the Comment
 textbox for organizational purposes. Place keywords or letters at the beginning of a
 comment for convenient sorting and filtering. Document information such as wire gauge and
 color.
8. Designate whether the channel is connected to a hardwire by selecting from the
 Hardwire drop-down listbox, as shown in the following figure:
 
 If the Hardwire drop-down listbox is not visible, click [IMAGE alt='image' src='GUID-C79972D9-E42C-4328-8A3C-C9F7CFDF1C64-a5.gif']. 
 Hardwires can also be *defined* in the *hardwire panel* of the
 Hardwires/Buses tab. Associations made in the hardwires interface are reflected here.
9. Enable the Reserved for Routing checkbox if the channel should be marked as reserved for routing.
10. Click the Disabled checkbox to disable the channel.
 Disabled channels are not used in connections/routes. Disabling a channel can be useful for making unused channels or channels with a damaged relay inactive.
11. Click on the
 Switch Executive taskbar to save the changes.

Tip

Parent topic:

Channels/Exclusions Tab

Related concepts:

- Adding Hardwires to Define Multidevice Topologies
- Hardwires/Buses Tab

Related information:

- Naming Conventions

<!--NI_TOPIC bundle=switch-executive path=configuring-ivi-switches.html language=enus -->
## TOPIC 00024: Configuring IVI Switches

- bundle_id: `switch-executive`
- source_path: `configuring-ivi-switches.html`
- source_url: https://docs-be.ni.com/bundle/switch-executive/raw/resource/enus/configuring-ivi-switches.html
- document_id: `switch-executive`
- page_type: `leaf`
- content_type: `concept`
- source_description: IVI switches display in the configuration tree beneath the Switch Executive virtual device.

### Configuring IVI Switches

IVI switches display in the configuration tree beneath the *Switch Executive virtual
 device*.

[IMAGE alt='image' src='GUID-BEDAF97F-0860-4AE7-8833-C1A0395E8F92-a5.gif']

Parent topic:

Configuring a Virtual Device

Related concepts:

- Virtual Device

<!--NI_TOPIC bundle=switch-executive path=controlling-the-virtual-device.html language=enus -->
## TOPIC 00025: Controlling the Virtual Device

- bundle_id: `switch-executive`
- source_path: `controlling-the-virtual-device.html`
- source_url: https://docs-be.ni.com/bundle/switch-executive/raw/resource/enus/controlling-the-virtual-device.html
- document_id: `switch-executive`
- page_type: `leaf`
- content_type: `concept`
- source_description: Use the following VIs and functions to control an Switch Executive virtual device: niSE Connect VI and niSE_Connect function niSE_ConnectAndDisconnect VI and niSE_ConnectAndDisconnect function niSE Disconnect VI and niSE_Disconnect function niSE Disconnect All VI and niSE_DisconnectAll function niSE

### Controlling the Virtual Device

Use the following VIs and functions to control an Switch Executive virtual device:

- niSE Connect VI and niSE_Connect function
- niSE_ConnectAndDisconnect VI and niSE_ConnectAndDisconnect function
- niSE Disconnect VI and niSE_Disconnect function
- niSE Disconnect All VI and niSE_DisconnectAll function
- niSE Find Route VI and niSE_FindRoute function

route specification strings

Note

open a session

Parent topic:

Programming Flow

Related concepts:

- Route Specification Strings
- Opening a Session

<!--NI_TOPIC bundle=switch-executive path=copying-a-route-group.html language=enus -->
## TOPIC 00026: Copying a Route Group

- bundle_id: `switch-executive`
- source_path: `copying-a-route-group.html`
- source_url: https://docs-be.ni.com/bundle/switch-executive/raw/resource/enus/copying-a-route-group.html
- document_id: `switch-executive`
- page_type: `leaf`
- content_type: `concept`
- source_description: Complete the following steps to copy a route group: Launch MAX with Switch Executive.Expand Devices and Interfaces»Switch Executive Virtual Devices. Select the Switch Executive virtual device to modify and navigate to the Schematic Configuration tab. Click the route group you want to copy in the Rou

### Copying a Route Group

Complete the following steps to copy a route group:

1. Launch MAX with Switch Executive.
2. Expand Devices and Interfaces»Switch Executive Virtual Devices .
3. Select the Switch Executive virtual device to modify and navigate to the Schematic
 Configuration tab.
4. Click the route group you want to copy in the Routes and Route Groups listbox.
5. Click . Switch
 Executive creates a copy of the route group, with a predefined name, in the
 Routes and Route Groups listbox and displays the copied
 route group in the Schematic window. Note Switch Executive
 *shares* associated routes between a route group and its
 copy.
6. (Optional) Add routes to fill or disassociate routes to empty the route group.
7. Click on the
 Switch Executive taskbar to save the changes.

Parent topic:

Schematic Configuration

Related concepts:

- Sharing a Route Between Route Groups
- Adding a Route
- Disassociating a Route from a Route Group

<!--NI_TOPIC bundle=switch-executive path=creating-a-virtual-device-using-the-switch-sf.html language=enus -->
## TOPIC 00027: Creating a Virtual Device Using the Switch SFP

- bundle_id: `switch-executive`
- source_path: `creating-a-virtual-device-using-the-switch-sf.html`
- source_url: https://docs-be.ni.com/bundle/switch-executive/raw/resource/enus/creating-a-virtual-device-using-the-switch-sf.html
- document_id: `switch-executive`
- page_type: `leaf`
- content_type: `concept`
- source_description: Complete the following steps to create an Switch Executive virtual device using the Switch Soft Front Panel (SFP): Launch MAX with Switch Executive. Expand Devices and Interfaces. Right-click the DAQmx switch from which you want to create a virtual device and select Test Panels. The Switch SFP opens

### Creating a Virtual Device Using the Switch SFP

Complete the following steps to create an Switch Executive virtual device using the Switch Soft
 Front Panel (SFP):

1. Launch MAX with Switch Executive.
2. Expand Devices and Interfaces .
3. Right-click the DAQmx switch from which you want to create a virtual device and select Test Panels . The Switch SFP opens.
4. Select a device from the Device drop-down listbox.
5. Select a topology for the device from the Topology drop-down listbox.
6. Click ,
 Create Switch Executive Virtual Device . MAX automatically
 browses to the NI Switch Executive virtual device with a predefined name of
 VirtualDeviceX under Devices and
 Interfaces»Switch Executive Virtual Devices .

Note

Parent topic:

Creating a Virtual Device

<!--NI_TOPIC bundle=switch-executive path=creating-a-virtual-device-with-ni-switchblock.html language=enus -->
## TOPIC 00028: Creating a Virtual Device with SwitchBlock

- bundle_id: `switch-executive`
- source_path: `creating-a-virtual-device-with-ni-switchblock.html`
- source_url: https://docs-be.ni.com/bundle/switch-executive/raw/resource/enus/creating-a-virtual-device-with-ni-switchblock.html
- document_id: `switch-executive`
- page_type: `leaf`
- content_type: `concept`
- source_description: Complete the following steps to create an Switch Executive virtual device using SwitchBlock cards and carriers: 1. Combine the Cards in Each Carrier When creating multicarrier virtual devices, combine the cards in each carrier as follows: Launch MAX with Switch Executive. Expand Devices and Interfac

### Creating a Virtual Device with
 SwitchBlock

Complete the following steps to create an Switch Executive virtual device using SwitchBlock cards
 and carriers:

#### 1. Combine the Cards in Each Carrier

When creating multicarrier virtual devices, combine the cards in each carrier as follows:

1. Launch MAX with Switch Executive.
2. Expand Devices and Interfaces .
3. Right-click the SwitchBlock carrier and select Configure . The SwitchBlock
 Configuration dialog box displays the cards in your carrier.
4. Click Combine All or drag and drop the cards to compose devices.
5. Click OK .
 [IMAGE alt='image' src='GUID-23FAC800-57DB-48D5-B2D9-283E06C88C5D-a5.png']

#### 2. Create a New Virtual Device

1. Launch MAX with Switch Executive.
2. Expand Devices and Interfaces .
3. Right-click Switch Executive Virtual Devices and select
 Create New . The Create New dialog box opens.
4. Type a name in the Virtual Device Name textbox or accept the
 predefined Virtual Device Name. The name you select is the name used to refer to the
 virtual device in the API. [IMAGE alt='image' src='GUID-7F3FA8CD-80A8-4C83-A2AB-B810210E29E2-a5.png'] Note Some characters are
 *reserved* and cannot be used in virtual device names.
5. Select a switch device or multiple switch devices from the Available
 Switches listbox and click to add each
 switch to the Switches to Add listbox.
6. (Optional) Click Auto Create IVI Devices to create default IVI
 configurations for all Switches detected in your system. IVI configurations are required
 only if you want to import a configuration from Switch Executive 3.0 or earlier. In Switch
 Executive 3.5 and later, switch devices do not require the use of IVI.
7. Click Next . A dialog box displays the status of the virtual
 device creation.
8. Click Next . The SwitchBlock Configuration dialog box launches to
 take you through configuration of your new SwitchBlock virtual device.
9. Select one of the following programming preferences and click
 Next : [IMAGE alt='image' src='GUID-8EE892A3-9DF7-422A-A5EB-53925D15DB33-a5.png']
  - End-to-End —Configuration automatically creates routes between
 endpoints. All internal connections are made automatically. Switch Executive reserves
 the intermediate channels for routing but prevents route configuration in the
 Schematic window.
  - Graphical —Configuration allows you to manually configure your
 routes and route groups in the Schematic window of the Schematic Configuration tab.
 Switch Executive does not reserve any channels for routing.
10. (End-to-End configuration only) Reserve channels for routing. If you chose End-to-End
 configuration, a channel reservation window displays the following three tabs: [IMAGE alt='image' src='GUID-10A46F73-A2F1-45E3-B2E3-A87F03A920DD-a5.png']
  - Recommendation —Displays the recommended configuration
  - Device Diagram —Displays a device diagram showing the channels
 to help you make connections
  - Details —Provides options for channel reservation with the
 following items:
    - Channels to Reserve —Select specific buses and rows for
 channel reservation.
    - Uncheck All —Deselects all buses and rows.
    - Use Defaults —Reserves default rows and buses. This item
 is only visible when Uncheck All has been clicked. By
 default, On I/O Connectors are not reserved. If you reserve an On I/O Connector,
 you cannot use that channel as a route endpoint.
  1. Select buses and rows for channel reservation.
  2. Click Next .
11. Create buses. [IMAGE alt='image' src='GUID-DB1FD482-31D4-4400-9D17-F14B6B9E2321-a5.png']
  1. Click View Buses to see the buses that NI Switch Executive
 will create to describe the physical connections between your cards, carriers, and
 expansion bridges (if present).
  2. Click Finish to create the buses. MAX automatically browses
 to the NI Switch Executive virtual device so you can continue with system
 configuration.

Parent topic:

Creating a Virtual Device

Related information:

- Naming Conventions

<!--NI_TOPIC bundle=switch-executive path=creating-a-virtual-device.html language=enus -->
## TOPIC 00029: Creating a Virtual Device

- bundle_id: `switch-executive`
- source_path: `creating-a-virtual-device.html`
- source_url: https://docs-be.ni.com/bundle/switch-executive/raw/resource/enus/creating-a-virtual-device.html
- document_id: `switch-executive`
- page_type: `leaf`
- content_type: `concept`
- source_description: Complete the following steps to create an Switch Executive virtual device: Launch MAX with Switch Executive. Expand Devices and Interfaces. Right-click Switch Executive Virtual Devices and select Create New. The Create New dialog box opens. Type a name in the Virtual Device Name textbox or accept th

### Creating a Virtual Device

Complete the following steps to create an Switch Executive virtual device:

1. Launch MAX with Switch Executive.
2. Expand Devices and Interfaces .
3. Right-click Switch Executive Virtual Devices and select Create
 New . The Create New dialog box opens.
4. Type a name in the Virtual Device Name textbox or accept the predefined
 Virtual Device Name. The name you select is the name used to refer to the virtual device in
 the API. Note Some characters are
 *reserved* and cannot be used in virtual device names.
5. Select a switch device or multiple switch devices from the Available
 Switches listbox and click to add each
 switch to the Switches to Add listbox. Note The list of names displayed in the
 Available Switches listbox comes from NI-DAQmx configurations for
 NI-SWITCH devices and IVI configurations for third-party switches. NI-SWITCH devices
 automatically display in the Available Switches listbox. Refer to
 *Using Third-Party Switches* to create a driver session and logical name for
 third-party switches to display in the Available Switches
 listbox.If you cannot locate a device, check your NI-DAQmx and IVI configurations in
 MAX. If you are using NI switches, you must configure the hardware in MAX as described
 in the Switches Getting Started Guide.
6. (Optional) Click Configure if you are using switches to configure the
 settings of those switches.
7. (Optional) Click Auto Create IVI Devices to create default IVI
 configurations for all switches detected in your system.
8. Click Next . A dialog box displays the status of the virtual device creation.
9. Click Finish when the virtual device creation is complete. MAX
 automatically browses to the Switch Executive virtual device that you created. Note If any errors occur during this
 process (such as an IVI device not being accessible), the virtual device is still created,
 but the IVI switches that caused the errors are not added. You can *manually
 add* them later.

Refer to *Adding IVI Switches* to continue configuring your Switch Executive virtual
 device.

Parent topic:

Using Switch Executive in MAX

Related concepts:

- Using Third-Party Switches
- Adding IVI Switches

Related information:

- Naming Conventions

<!--NI_TOPIC bundle=switch-executive path=debugging-with-ni-io-trace.html language=enus -->
## TOPIC 00030: Debugging with IO Trace

- bundle_id: `switch-executive`
- source_path: `debugging-with-ni-io-trace.html`
- source_url: https://docs-be.ni.com/bundle/switch-executive/raw/resource/enus/debugging-with-ni-io-trace.html
- document_id: `switch-executive`
- page_type: `leaf`
- content_type: `concept`
- source_description: I/O Trace is an application that monitors, records, and displays National Instruments API calls made by applications. Use I/O Trace to quickly locate and analyze any erroneous National Instruments API calls that Switch Executive makes and to verify that the communication with your instrument is corr

### Debugging with IO Trace

I/O Trace is an application that monitors, records, and displays National Instruments API calls
 made by applications. Use I/O Trace to quickly locate and analyze any erroneous National
 Instruments API calls that Switch Executive makes and to verify that the communication
 with your instrument is correct.

To launch I/O Trace, navigate to Start»All Programs»National Instruments»IO
 Trace.

Tip

Properties

#### I/O Trace Monitoring
 NI Switch Executive Function Calls

[IMAGE alt='image' src='GUID-D614D741-7CCF-40B3-AB2C-650A8E02A95A-a5.png']

Tip

For more information about
 using I/O Trace, refer to the I/O Trace Help, available in NI I/O Trace at
 Help»Help Topics.

Parent topic:

Programming with Switch Executive

<!--NI_TOPIC bundle=switch-executive path=deleting-a-hardwire.html language=enus -->
## TOPIC 00031: Deleting a Hardwire

- bundle_id: `switch-executive`
- source_path: `deleting-a-hardwire.html`
- source_url: https://docs-be.ni.com/bundle/switch-executive/raw/resource/enus/deleting-a-hardwire.html
- document_id: `switch-executive`
- page_type: `leaf`
- content_type: `concept`
- source_description: Deleting hardwires can break routes requiring the hardwire. Always validate a virtual device after you delete a hardwire. Complete the following steps to delete a hardwire: Launch MAX with Switch Executive. Expand Devices and Interfaces»Switch Executive Virtual Devices. Select the Switch Executive v

### Deleting a Hardwire

Note

validate

Complete the following steps to delete a hardwire:

1. Launch MAX with Switch Executive.
2. Expand Devices and Interfaces»Switch Executive Virtual Devices .
3. Select the Switch Executive virtual device to modify and navigate to the Schematic
 Configuration tab.
4. Verify that the required switch device is selected in the Devices listbox and its schematic appears in the Schematic window.
5. Click a channel in the Schematic window to access the Edit Alias & Hardwire dialog box.
6. Select the Hardwires tab.
7. Select the hardwire you want to delete in the Available Hardwires listbox
 and click . A dialog box opens to confirm the deletion.
8. Click Yes to delete the hardwire. Switch Executive deletes the hardwire
 from the Available Hardwires listbox and disassociates any channels associated with
 the hardwire.
9. Click OK .
10. Click on the
 Switch Executive taskbar to save the changes.

Parent topic:

Schematic Configuration

Related concepts:

- Validating a Virtual Device

<!--NI_TOPIC bundle=switch-executive path=deleting-a-route-group.html language=enus -->
## TOPIC 00032: Deleting a Route Group

- bundle_id: `switch-executive`
- source_path: `deleting-a-route-group.html`
- source_url: https://docs-be.ni.com/bundle/switch-executive/raw/resource/enus/deleting-a-route-group.html
- document_id: `switch-executive`
- page_type: `leaf`
- content_type: `concept`
- source_description: Deleting a route group removes it from the virtual device: that is, Switch Executive deletes the route group and removes it from the Routes and Route Groups listbox. Complete the following steps to delete a route group: Launch MAX with Switch Executive.Expand Devices and Interfaces»Switch Executive

### Deleting a Route Group

Note

and

Routes and Route
 Groups

Complete the following steps to delete a route group:

1. Launch MAX with Switch Executive.
2. Expand Devices and Interfaces»Switch Executive Virtual Devices .
3. Select the Switch Executive virtual device to modify and navigate to the Schematic
 Configuration tab.
4. Select the route group you want to delete in the Routes and Route Groups 
 listbox and click , or right-click the route group you want to delete and
 select Delete . A dialog box opens to confirm the
 deletion. Note When
 you delete a parent route group, Switch Executive *disassociates* all
 nested route groups. Although Switch Executive deletes the parent route group
 from the virtual device and the Routes and Route Groups
 listbox, the nested, child route groups remain available in the
 Routes and Route Groups listbox.
5. Click OK to delete the route group. Switch Executive deletes the route
 group from the virtual device and the Routes and Route Groups 
 listbox.
6. Click on the
 Switch Executive taskbar to save the changes.

Parent topic:

Schematic Configuration

Related concepts:

- Disassociating a Route from a Route Group

<!--NI_TOPIC bundle=switch-executive path=deleting-a-route.html language=enus -->
## TOPIC 00033: Deleting a Route

- bundle_id: `switch-executive`
- source_path: `deleting-a-route.html`
- source_url: https://docs-be.ni.com/bundle/switch-executive/raw/resource/enus/deleting-a-route.html
- document_id: `switch-executive`
- page_type: `leaf`
- content_type: `concept`
- source_description: Deleting a route from a virtual device removes the route from its associated route groups and the Routes and Route Groups listbox. If you want to remove a route from a route group but keep it available in the Routes and Route Groups listbox, disassociate the route instead.To delete a route from its

### Deleting a Route

Note

Routes and Route Groups

Routes and Route
 Groups

disassociate

Note

Complete the following steps to delete a route:

1. Launch MAX with Switch Executive.
2. Expand Devices and Interfaces»Switch Executive Virtual Devices .
3. Select the Switch Executive virtual device to modify and navigate to the Schematic
 Configuration tab.
4. Click the device that contains the route that you want to delete in the Devices listbox. NI Switch Executive displays the device schematic in the Schematic window.
5. Enable the Show Routes checkbox below the Routes and Route Groups listbox.
6. Click the route to delete in the Routes and Route Groups listbox. Note If the route you want
 to delete is shared among multiple route groups, selecting the route within the
 route group will prompt you to disassociate the route, rather than delete it. To
 delete the route, select it as shown in the listbox not nested under any route
 groups.
7. Click or
 right-click the route and select Delete to delete the
 route. Tip 
 With the parent route group selected in the Routes and Route
 Groups listbox, you can delete a route associated with a
 single route group by clicking the point of intersection—crosspoint or
 channel connection point—between two channels in the
 Schematic window.
 For third-party IVI-switch and *independent* topologies, with the
 parent route group selected in the Routes and Route
 Groups listbox, you can delete a route associated with a
 single route group by selecting the route from the
 Connections listbox and clicking
 Delete.
8. Click OK to delete the route.
9. Click on the
 Switch Executive taskbar to save the changes.

Parent topic:

Schematic Configuration

Related concepts:

- Disassociating a Route from a Route Group
- Independent Topologies

<!--NI_TOPIC bundle=switch-executive path=deleting-a-virtual-device.html language=enus -->
## TOPIC 00034: Deleting a Virtual Device

- bundle_id: `switch-executive`
- source_path: `deleting-a-virtual-device.html`
- source_url: https://docs-be.ni.com/bundle/switch-executive/raw/resource/enus/deleting-a-virtual-device.html
- document_id: `switch-executive`
- page_type: `leaf`
- content_type: `concept`
- source_description: Complete the following steps to delete an Switch Executive virtual device: Launch MAX with Switch Executive. Expand Devices and Interfaces»Switch Executive Virtual Devices. Right-click the Switch Executive virtual device you want to delete and select Delete. A dialog box opens to confirm the deletio

### Deleting a Virtual Device

Complete the following steps to delete an Switch Executive virtual device:

1. Launch MAX with Switch Executive.
2. Expand Devices and Interfaces»Switch Executive Virtual Devices .
3. Right-click the Switch Executive virtual device you want to delete and select
 Delete . A dialog box opens to confirm the deletion. Tip To delete multiple
 virtual devices at one time, hold <Shift> or <Ctrl> while selecting
 multiple virtual devices and press <Delete>.
4. Click Yes to delete the virtual device or No to abort.

Note

Devices and Interfaces

IVI Drivers

Parent topic:

Using Switch Executive in MAX

<!--NI_TOPIC bundle=switch-executive path=deleting-buses.html language=enus -->
## TOPIC 00035: Deleting Buses

- bundle_id: `switch-executive`
- source_path: `deleting-buses.html`
- source_url: https://docs-be.ni.com/bundle/switch-executive/raw/resource/enus/deleting-buses.html
- document_id: `switch-executive`
- page_type: `leaf`
- content_type: `concept`
- source_description: Complete the following steps to delete a bus: Launch MAX with Switch Executive. Expand Devices and Interfaces»Switch Executive Virtual Devices. Select the Switch Executive virtual device to modify. Click the Hardwires/Buses tab. Select the bus you want to delete from the Buses listbox. Click . A dia

### Deleting Buses

Complete the following steps to delete a bus:

1. Launch MAX with Switch Executive.
2. Expand Devices and Interfaces»Switch Executive Virtual Devices .
3. Select the Switch Executive virtual device to modify.
4. Click the Hardwires/Buses tab.
5. Select the bus you want to delete from the Buses listbox.
6. Click . A dialog
 box opens to confirm the deletion.
7. Click Yes to delete the bus.
8. Click on the
 Switch Executive taskbar to save the changes.

Parent topic:

Hardwires/Buses Tab

<!--NI_TOPIC bundle=switch-executive path=deleting-exclusions.html language=enus -->
## TOPIC 00036: Deleting Exclusions

- bundle_id: `switch-executive`
- source_path: `deleting-exclusions.html`
- source_url: https://docs-be.ni.com/bundle/switch-executive/raw/resource/enus/deleting-exclusions.html
- document_id: `switch-executive`
- page_type: `leaf`
- content_type: `concept`
- source_description: Complete the following steps to delete an exclusion: Launch MAX with Switch Executive. Expand Devices and Interfaces»Switch Executive Virtual Devices. Select the Switch Executive virtual device to modify. Click the Channels/Exclusions tab. Select the exclusion you want to delete from the Exclusions

### Deleting Exclusions

Complete the following steps to delete an exclusion:

1. Launch MAX with Switch Executive.
2. Expand Devices and Interfaces»Switch Executive Virtual Devices .
3. Select the Switch Executive virtual device to modify.
4. Click the Channels/Exclusions tab.
5. Select the exclusion you want to delete from the Exclusions listbox.
6. Click . A dialog
 box opens to confirm the deletion.
7. Click Yes to delete the exclusion.
8. Click on the
 Switch Executive taskbar to save the changes.

Parent topic:

Channels/Exclusions Tab

<!--NI_TOPIC bundle=switch-executive path=deleting-hardwires.html language=enus -->
## TOPIC 00037: Deleting Hardwires

- bundle_id: `switch-executive`
- source_path: `deleting-hardwires.html`
- source_url: https://docs-be.ni.com/bundle/switch-executive/raw/resource/enus/deleting-hardwires.html
- document_id: `switch-executive`
- page_type: `leaf`
- content_type: `concept`
- source_description: Deleting hardwires can break routes that require the hardwire. Always validate your Switch Executive system after you delete hardwires. Complete the following steps to delete a hardwire: Launch MAX with Switch Executive. Expand Devices and Interfaces»Switch Executive Virtual Devices. Select the Swit

### Deleting Hardwires

Note

validate

Complete the following steps to delete a hardwire:

1. Launch MAX with Switch Executive.
2. Expand Devices and Interfaces»Switch Executive Virtual Devices .
3. Select the Switch Executive virtual device to modify.
4. Click the Hardwires/Buses tab.
5. Select the hardwire you want to delete in the Hardwires listbox.
6. Click . A dialog
 box opens to confirm the deletion.
7. Click Yes to delete the hardwire.
8. Click on the
 Switch Executive taskbar to save the changes.

Parent topic:

Hardwires/Buses Tab

Related concepts:

- Validating a Virtual Device

<!--NI_TOPIC bundle=switch-executive path=deleting-route-groups.html language=enus -->
## TOPIC 00038: Deleting Route Groups

- bundle_id: `switch-executive`
- source_path: `deleting-route-groups.html`
- source_url: https://docs-be.ni.com/bundle/switch-executive/raw/resource/enus/deleting-route-groups.html
- document_id: `switch-executive`
- page_type: `leaf`
- content_type: `concept`
- source_description: Complete the following steps to delete a route group: Launch MAX with Switch Executive. Expand Devices and Interfaces»Switch Executive Virtual Devices. Select the Switch Executive virtual device that you want to modify. Click the Routes/Groups tab. Select the route group you want to delete from the

### Deleting Route Groups

Complete the following steps to delete a route group:

1. Launch MAX with Switch Executive.
2. Expand Devices and Interfaces»Switch Executive Virtual Devices .
3. Select the Switch Executive virtual device that you want to modify.
4. Click the Routes/Groups tab.
5. Select the route group you want to delete from the Routes and Route Groups listbox.
6. Click . A dialog
 box opens to confirm the deletion.
7. Click OK to delete the route group.
8. Click on the
 Switch Executive taskbar to save the changes.

Parent topic:

Routes/Groups Tab

<!--NI_TOPIC bundle=switch-executive path=deleting-routes.html language=enus -->
## TOPIC 00039: Deleting Routes

- bundle_id: `switch-executive`
- source_path: `deleting-routes.html`
- source_url: https://docs-be.ni.com/bundle/switch-executive/raw/resource/enus/deleting-routes.html
- document_id: `switch-executive`
- page_type: `leaf`
- content_type: `concept`
- source_description: Complete the following steps to delete a route: Launch MAX with Switch Executive.Expand Devices and Interfaces»Switch Executive Virtual Devices. Select the Switch Executive virtual device that you want to modify. Click the Routes/Groups tab. Select the route you want to delete from Routes and Route

### Deleting Routes

Complete the following steps to delete a route:

1. Launch MAX with Switch Executive.
2. Expand Devices and Interfaces»Switch Executive Virtual Devices .
3. Select the Switch Executive virtual device that you want to modify.
4. Click the Routes/Groups tab.
5. Select the route you want to delete from Routes and Route Groups listbox.
6. Click . A dialog
 box opens to confirm the deletion.
7. Click OK to delete the route.
8. Click on the
 Switch Executive taskbar to save the changes.

Parent topic:

Routes/Groups Tab

<!--NI_TOPIC bundle=switch-executive path=deploying-a-virtual-device.html language=enus -->
## TOPIC 00040: Deploying a Virtual Device

- bundle_id: `switch-executive`
- source_path: `deploying-a-virtual-device.html`
- source_url: https://docs-be.ni.com/bundle/switch-executive/raw/resource/enus/deploying-a-virtual-device.html
- document_id: `switch-executive`
- page_type: `leaf`
- content_type: `concept`
- source_description: Complete the following steps to deploy an Switch Executive virtual device from a development system to a target system.A development system must be running a licensed development version of Switch Executive. Target, or deployment, systems can run either a licensed deployment or a licensed developmen

### Deploying a Virtual Device

Note

licensed

1. Export the configuration files from the development system with the same Switch
 Executive version as the target system.
2. Import the configuration files to the target system.
3. Validate the deployment of the Switch Executive virtual device.

Parent topic:

Using Switch Executive in MAX

Related concepts:

- Activating Your Software
- Exporting Configurations
- Importing Configurations
- Validating Deployment

<!--NI_TOPIC bundle=switch-executive path=deployment.html language=enus -->
## TOPIC 00041: Deployment

- bundle_id: `switch-executive`
- source_path: `deployment.html`
- source_url: https://docs-be.ni.com/bundle/switch-executive/raw/resource/enus/deployment.html
- document_id: `switch-executive`
- page_type: `leaf`
- content_type: `concept`
- source_description: Deploy a virtual device you developed on one computer for use on one or more other computers.A development system must be running a licensed development version of Switch Executive. Target, or deployment, systems can run either a licensed deployment or a licensed development copy of Switch Executive

### Deployment

Note

licensed

Parent topic:

Concepts

Related concepts:

- Activating Your Software
- Deploying a Virtual Device
- Using the Configuration API

<!--NI_TOPIC bundle=switch-executive path=disassociating-a-nested-route-group.html language=enus -->
## TOPIC 00042: Disassociating a Nested Route Group

- bundle_id: `switch-executive`
- source_path: `disassociating-a-nested-route-group.html`
- source_url: https://docs-be.ni.com/bundle/switch-executive/raw/resource/enus/disassociating-a-nested-route-group.html
- document_id: `switch-executive`
- page_type: `leaf`
- content_type: `concept`
- source_description: Disassociating a nested route group from a parent route group only removes the route group from the parent route group and does not delete the route group from the Routes and Route Groups listbox. If you want to delete a nested route group from its parent route group and remove it from the Routes an

### Disassociating a Nested Route Group

Note

not

Routes and Route Groups

and

Routes and Route Groups

delete

Complete the following steps to disassociate a nested route group:

1. Launch MAX with Switch Executive.
2. Expand Devices and Interfaces»Switch Executive Virtual Devices .
3. Select the Switch Executive virtual device to modify and navigate to the Schematic
 Configuration tab.
4. Expand the route group that contains the nested route group you want to disassociate in the Routes and Route Groups listbox.
5. Right-click the route group you want to disassociate and select Disassociate . A dialog box opens to confirm the disassociation.
6. Click OK . NI Switch Executive disassociates the nested, child route group from its parent route group. Notice that the previously nested route group is still available in the Routes and Route Groups listbox.
7. Click on the
 Switch Executive taskbar to save the changes.

Parent topic:

Schematic Configuration

Related concepts:

- Deleting a Route

<!--NI_TOPIC bundle=switch-executive path=disassociating-a-route-from-a-route-group.html language=enus -->
## TOPIC 00043: Disassociating a Route from a Route Group

- bundle_id: `switch-executive`
- source_path: `disassociating-a-route-from-a-route-group.html`
- source_url: https://docs-be.ni.com/bundle/switch-executive/raw/resource/enus/disassociating-a-route-from-a-route-group.html
- document_id: `switch-executive`
- page_type: `leaf`
- content_type: `concept`
- source_description: Disassociating a route from a route group only removes the route from its associated route group. The route remains on the virtual device and in the Routes and Route Groups listbox. If you want to delete a route from all its associated route groups and the Routes and Route Groups listbox, delete the

### Disassociating a Route from a Route Group

Note

Routes and Route Groups

and

Routes and Route Groups

delete

Complete the following steps to disassociate a route from a route group:

1. Launch MAX with Switch Executive.
2. Expand Devices and Interfaces»Switch Executive Virtual Devices .
3. Select the Switch Executive virtual device to modify and navigate to the Schematic
 Configuration tab.
4. Enable the Show Routes checkbox under the Routes and Route Groups listbox to view all routes.
5. Expand the route group that contains the route you want to disassociate in the Routes and Route Groups listbox.
6. Right-click the route you want to disassociate and select Disassociate . A dialog box opens to confirm the disassociation.
7. Click OK . Switch Executive disassociates the route from its associated
 route group. Notice that the route is still available in the Routes and Route
 Groups listbox.
8. Click on the
 Switch Executive taskbar to save the changes.

Parent topic:

Schematic Configuration

Related concepts:

- Deleting a Route

<!--NI_TOPIC bundle=switch-executive path=editing-a-route.html language=enus -->
## TOPIC 00044: Editing a Route

- bundle_id: `switch-executive`
- source_path: `editing-a-route.html`
- source_url: https://docs-be.ni.com/bundle/switch-executive/raw/resource/enus/editing-a-route.html
- document_id: `switch-executive`
- page_type: `leaf`
- content_type: `concept`
- source_description: Complete the following steps to edit a route:Launch MAX with Switch Executive. Expand Devices and Interfaces»Switch Executive Virtual Devices. Select the Switch Executive virtual device to modify and navigate to the Schematic Configuration tab. Enable the Show Routes checkbox under the Routes and Ro

### Editing a Route

Complete the following steps to edit a route:

1. Launch MAX with Switch Executive.
2. Expand Devices and Interfaces»Switch Executive Virtual Devices .
3. Select the Switch Executive virtual device to modify and navigate to the Schematic
 Configuration tab.
4. Enable the Show Routes checkbox under the Routes and Route Groups listbox to view all routes.
5. Click the route you want to edit in the Routes and Route Groups 
 listbox. Note When
 you edit a *shared route*, the edits apply to every instance of the
 route.
6. Complete one or more of the following editing tasks: Copy
 Click [IMAGE alt='image' src='GUID-0363BCD7-9645-43AD-A6D0-A7A0687EB4CD-a5.gif'] to create a copy of the route. NI
 Switch Executive creates a copy of the route, with a predefined
 name, in the Routes and Route Groups
 listbox.
 Rename
 Press <F2> or right-click the route and choose
 Rename to rename the route.
 Edit the Path
 General purpose, matrix, and multiplexer
 topologies—Click
 another point of intersection
 between two channels in the
 Schematic window.
 Third-party IVI-switch and independent
 topologies—Select one channel from the
 Channel 1 listbox and one
 channel from the Channel 2
 listbox and click Change.Switch Executive deletes the original route path and
 creates a new route path. If you want to create the route on a
 different device, click the device in the
 Devices listbox before you edit the
 path.
7. Click on the
 Switch Executive taskbar to save the changes.

Parent topic:

Schematic Configuration

Related concepts:

- Sharing a Route Between Route Groups

<!--NI_TOPIC bundle=switch-executive path=error-handling.html language=enus -->
## TOPIC 00045: Error Handling

- bundle_id: `switch-executive`
- source_path: `error-handling.html`
- source_url: https://docs-be.ni.com/bundle/switch-executive/raw/resource/enus/error-handling.html
- document_id: `switch-executive`
- page_type: `leaf`
- content_type: `concept`
- source_description: Use error handling to assist in troubleshooting problems with switches and debug programming. Switch Executive VIs contain error in and error out nodes to handle errors. TestStand run-time errors display when an error has occurred. C and Visual Basic use combinations of the niSE_GetError and niSE_Cl

### Error Handling

Use error handling to assist in troubleshooting problems with switches and debug programming.
 Switch Executive VIs contain error in and error out
 nodes to handle errors. TestStand run-time errors display when an error has occurred.
 C and Visual Basic use combinations of the niSE_GetError and
 niSE_ClearError functions to report errors. The C and Visual Basic
 examples contain the function NI Switch ExecutiveCheckErr that you can
 use in your own programs.

Refer to *Error Codes* for error descriptions.

Parent topic:

Programming Flow

<!--NI_TOPIC bundle=switch-executive path=examples.html language=enus -->
## TOPIC 00046: Examples

- bundle_id: `switch-executive`
- source_path: `examples.html`
- source_url: https://docs-be.ni.com/bundle/switch-executive/raw/resource/enus/examples.html
- document_id: `switch-executive`
- page_type: `leaf`
- content_type: `concept`
- source_description: Switch Executive programming examples are instructional tools that demonstrate how to integrate Switch Executive virtual devices into your systems. Switch Executive programming examples are available for the following ADEs: LabVIEW LabWindows™/CVI™ C/C++ Visual Basic TestStand For example locations

### Examples

Switch Executive programming examples are instructional tools that demonstrate how to integrate
 Switch Executive virtual devices into your systems. Switch Executive programming
 examples are available for the following ADEs:

- LabVIEW
- LabWindows™/CVI™
- C/C++
- Visual Basic
- TestStand

For example locations and supported ADE versions, refer to the *Switch Executive
 Readme* file.

Parent topic:

Programming with Switch Executive

Related information:

- Related Documentation

<!--NI_TOPIC bundle=switch-executive path=excel-workbooks.html language=enus -->
## TOPIC 00047: Excel Workbooks

- bundle_id: `switch-executive`
- source_path: `excel-workbooks.html`
- source_url: https://docs-be.ni.com/bundle/switch-executive/raw/resource/enus/excel-workbooks.html
- document_id: `switch-executive`
- page_type: `leaf`
- content_type: `concept`
- source_description: When you export to Excel workbooks (.xls and .xlsx), Switch Executive saves the configuration data of a virtual device, organized by object type, in a multi-sheet workbook. Each worksheet in the workbook contains the configuration data stored in columns and rows.The column headings specify the attri

### Excel Workbooks

When you export to Excel workbooks (.xls and .xlsx),
 Switch Executive saves the configuration data of a virtual device, organized by object
 type, in a multi-sheet workbook. Each worksheet in the workbook contains the
 configuration data stored in columns and rows.

Note

Formatting Configuration
 Data

#### Example

The following figure shows an IVI Devices worksheet. The column headings, IVI Logical
 Name and Comment, specify the attributes associated with an IVI Device object. The
 following rows define actual IVI devices, such as PXI1Slot2 and SampleMatrix1, and
 specify the attribute values associated with those devices.

[IMAGE alt='image' src='GUID-CA2FED51-5B13-42D0-9001-405E29E8DEEA-a5.png']

Parent topic:

Exporting to Excel

Related concepts:

- Formatting Configuration Data

<!--NI_TOPIC bundle=switch-executive path=exclusion.html language=enus -->
## TOPIC 00048: Exclusion

- bundle_id: `switch-executive`
- source_path: `exclusion.html`
- source_url: https://docs-be.ni.com/bundle/switch-executive/raw/resource/enus/exclusion.html
- document_id: `switch-executive`
- page_type: `leaf`
- content_type: `concept`
- source_description: An exclusion is a connection rule used to prevent specific channels from connecting to one another. Exclusions are predominately used for safety purposes.For switch devices with single-pole double-throw (SPDT)—also known as Form C—relays, a physical connection always exists between the common (COM)

### Exclusion

exclusion

Caution

Exclusions and SPDT Relays

Caution

Switch Executive currently offers two types of exclusions—mutual exclusions and set
 exclusions.

- For mutual exclusions , you create a list of channels that should never connect to one another. A source channel is a type of mutual exclusion.
- For set exclusions , you create two lists of channels. Channels from the first list should never connect to channels of the second list. For example, set exclusions can be used to separate high-power DC and RF signals.

Earlier versions of Switch Executive contained a single type of exclusion called the *source
 channel*. Source channels are a type of mutual exclusion. Switch Executive
 automatically creates a mutual exclusion called *Source Channels* and
 migrates any source channels from previous versions into this exclusion.

Parent topic:

Fundamentals

Related concepts:

- Exclusions and SPDT Relays
- Adding Mutual Exclusions
- Adding Set Exclusions
- Extended Configuration
- Using the Configuration API

<!--NI_TOPIC bundle=switch-executive path=exclusions-and-spdt-relays.html language=enus -->
## TOPIC 00049: Exclusions and SPDT Relays

- bundle_id: `switch-executive`
- source_path: `exclusions-and-spdt-relays.html`
- source_url: https://docs-be.ni.com/bundle/switch-executive/raw/resource/enus/exclusions-and-spdt-relays.html
- document_id: `switch-executive`
- page_type: `leaf`
- content_type: `concept`
- source_description: For switch devices with SPDT—also known as Form C—relays, a physical connection always exists between common (COM) and either the normally open (NO) or the normally closed (NC) pole.When using switches, calling niSE Disconnect with an SPDT relay results in a disconnect in software, but the relay pos

### Exclusions and SPDT Relays

For switch devices with SPDT—also known as Form C—relays, a physical connection always exists
 between common (COM) and either the normally open (NO) or the normally closed (NC)
 pole.

When using switches, calling *niSE Disconnect* with an SPDT relay results in a
 disconnect in software, but the relay position does not change in hardware until
 *niSE Connect* is called.

Therefore, to guarantee the state of an SPDT relay, you must connect either the NO or the NC pole
 to COM using *niSE Connect*. Switch Executive verifies that there are no
 exclusion conflicts before connecting a relay, but does not verify
 exclusions when disconnecting relays using *niSE Disconnect* or *niSE
 DisconnectAll*.

*niSE DisconnectAll* physically resets all relays to their default positions. Because
 Switch Executive does not verify exclusions on disconnect, excluded connections in
 default relay positions could pose problems for SPDT relays.

Parent topic:

Exclusion

<!--NI_TOPIC bundle=switch-executive path=export.html language=enus -->
## TOPIC 00050: Export

- bundle_id: `switch-executive`
- source_path: `export.html`
- source_url: https://docs-be.ni.com/bundle/switch-executive/raw/resource/enus/export.html
- document_id: `switch-executive`
- page_type: `leaf`
- content_type: `concept`
- source_description: Export the configuration of a virtual device to perform configuration management tasks in other file formats or with other programs such as Microsoft Excel.

### Export

Export the configuration of a virtual device to perform configuration management tasks in other
 file formats or with other programs such as Microsoft Excel.

Parent topic:

Concepts

Related concepts:

- Exporting a Virtual Device
- Using the Configuration API
- Managing a Virtual Device in Excel

<!--NI_TOPIC bundle=switch-executive path=exporting-a-virtual-device.html language=enus -->
## TOPIC 00051: Exporting a Virtual Device

- bundle_id: `switch-executive`
- source_path: `exporting-a-virtual-device.html`
- source_url: https://docs-be.ni.com/bundle/switch-executive/raw/resource/enus/exporting-a-virtual-device.html
- document_id: `switch-executive`
- page_type: `leaf`
- content_type: `concept`
- source_description: Complete the following steps to export the configuration file of an Switch Executive virtual device: Launch MAX with Switch Executive. Expand Devices and Interfaces»Switch Executive Virtual Devices. Right-click a virtual device and select . The Export dialog box opens. Select an Export Format for th

### Exporting a Virtual Device

Complete the following steps to export the configuration file of an Switch Executive virtual
 device:

1. Launch MAX with Switch Executive.
2. Expand Devices and Interfaces»Switch Executive Virtual Devices .
3. Right-click a virtual device and select . The Export dialog box opens.
4. Select an Export Format for the virtual device configuration. NI Switch Executive supports the
 following export and import formats:
5. Configuration Export File (.nce) —Recommended for export and import of complete configurations that do not need
 editing outside of Switch Executive. Allows saving of system configuration information
 for all devices and interfaces, including NI Switch Executive virtual devices.
6. Switch Executive Export File (.xml) —Recommended for export and import of individual virtual device configurations that
 do not need editing outside of Switch Executive. Caution When exporting a
 virtual device configuration that contains non-ASCII characters (0X000-0X07F) (e.g.
 ä, é, ó, ñ) to XML, NI Switch Executive extracts those special characters, and
 replaces them with blank spaces.
7. Microsoft Excel Workbooks (.xls and .xlsx) —Recommended for export and import of individual virtual device configurations in a
 format suitable for editing. Components of the switching system (virtual devices,
 channels, routes, and so on) are contained in separate workbook sheets.
8. Tab-delimited File (.txt) —Recommended for export and import of individual virtual device configurations in a
 format suitable for editing. When opened in a spreadsheet editing program,
 tab-delimited files contain the components of the switching system (virtual devices,
 channels, routes, and so on) in a single workbook sheet.
9. Select the Switch Executive version to export to from the Version 
 drop-down listbox. Click the Details button to show what data will be
 left out for older versions of Switch Executive. The default value for the version is the
 current (latest) version. Change this value if you want to export to an older version.
10. Specify a Destination File for the virtual device configuration. Caution Exporting overwrites files with the same
 filename. To avoid the loss of custom data in modified files, enter a unique Destination
 File for each export.
11. Click Finish to export the virtual device configuration. By default, the file is opened after export.

Parent topic:

Using Switch Executive in MAX

<!--NI_TOPIC bundle=switch-executive path=exporting-configurations.html language=enus -->
## TOPIC 00052: Exporting Configurations

- bundle_id: `switch-executive`
- source_path: `exporting-configurations.html`
- source_url: https://docs-be.ni.com/bundle/switch-executive/raw/resource/enus/exporting-configurations.html
- document_id: `switch-executive`
- page_type: `leaf`
- content_type: `concept`
- source_description: Complete the following steps on the development system to export the configuration files necessary to deploy an Switch Executive virtual device: Export the Switch Executive virtual device configuration file. If you are exporting a virtual device to a .nce file, skip steps 2 and 3. Export the DAQmx c

### Exporting Configurations

Complete the following steps on the development system to export the configuration files
 necessary to deploy an Switch Executive virtual device:

1. Export the Switch Executive virtual device configuration file. If you are
 exporting a virtual device to a .nce file, skip steps 2 and 3.
2. Export the DAQmx configuration file if the Switch Executive virtual device you are deploying
 uses DAQmx switches.
  1. Launch Measurement & Automation Explorer (MAX).
  2. Export the DAQmx configuration file using the Export Configuration Wizard in MAX.
 Refer to the Importing and Exporting Configurations topic of the Measurement &
 Automation Explorer Help for NI-DAQmx for more information by navigating in MAX to
 Help»Help Topics»NI-DAQmx»MAX Help for NI-DAQmx .
3. (Optional) Copy the IVI configuration file from the development system to the target system if
 you are using IVI devices. Note The IVI configuration
 file contains IVI Driver Sessions and IVI Logical Names. Because IVI Driver Sessions and
 IVI Logical Names must match between the development and target deployment systems, copy
 this file to the exact directory location on the target system as where it was installed
 in the development system.
  - (IVI Compliance Package 3.2 or higher) IVIConfigurationStore.xml , the
 IVI configuration file, is installed at Documents and Settings\All
 Users\Application Data\IVI Foundation\IVI .
  - (IVI Compliance Package 2.0 to 3.1) IVIConfigurationStore.xml , the
 IVI configuration file, is installed at Program Files\IVI\Data .
  - (IVI Compliance Package 1. x ) IVI.ini , the IVI
 configuration file, is installed at VXIPNP\WINNT[WIN95]\niivi .

Parent topic:

Deploying a Virtual Device

Related concepts:

- Exporting a Virtual Device

<!--NI_TOPIC bundle=switch-executive path=exporting-to-excel.html language=enus -->
## TOPIC 00053: Exporting to Excel

- bundle_id: `switch-executive`
- source_path: `exporting-to-excel.html`
- source_url: https://docs-be.ni.com/bundle/switch-executive/raw/resource/enus/exporting-to-excel.html
- document_id: `switch-executive`
- page_type: `leaf`
- content_type: `concept`
- source_description: To manage configuration data in Excel, first export the virtual device to an Excel-compatible file format.The following table lists the objects (worksheets) and attributes (columns) that Switch Executive generates when exporting to Excel.Switch Executive requires some attributes (columns) to success

### Exporting to Excel

To manage configuration data in Excel, first *export* the virtual device to an
 Excel-compatible file format.

Note

| Object (Worksheet) | Attribute (Column) |
| --- | --- |
| Overview | N/A |
| Virtual Device | Virtual Device Name, Comment, Export Schema Version, Channel Name Style, Route Editor Channel Display, Route Editor Route Updates, Route Editor Route Search Depth, Schematic Route Display, Schematic Route Deletion |
| IVI Devices | IVI Device Name, Comment |
| Channels | Channel IVI Device, Channel IVI Name, Alias, Hardwire, Reserved For Routing, Disabled, Comment, Wire Mode, Settling Time (s), Impedance (Ohm), Bandwidth (Hz), DC Voltage (V), AC Voltage (V), DC Switching Current (A), AC Switching Current (A), DC Carry Current (A), AC Carry Current (A), DC Switching Power (W), AC Switching Power (W), DC Carry Power (W), AC Carry Power (W) |
| Routes | Route Name, Endpoint1, Endpoint2, Specification, Type, Multiconnect Mode, Comment, Wire Mode, Settling Time (s), Impedance (Ohm), Bandwidth (Hz), DC Voltage (V), AC Voltage (V), DC Switching Current (A), AC Switching Current (A), DC Carry Current (A), AC Carry Current (A), DC Switching Power (W), AC Switching Power (W), DC Carry Power (W), AC Carry Power (W) |
| Route Groups | Route Group Name, Comment |
| Route Group Children | Route Group Name, Child |
| Hardwires | Hardwire Name, Comment |
| Exclusions | Exclusion Name, Type, Disabled, Comment |
| Mutual Exclusion Channels | Exclusion Name, Channel |
| Set Exclusion Set1 Channels | Exclusion Name, Set1 Channel |
| Set Exclusion Set2 Channels | Exclusion Name, Set2 Channel |
| Buses | Bus Name, Hardwire Name Start Index, Comment |
| Bus Channels | Bus Name, IVI Device, Base Channel, End Channel |

Parent topic:

Managing a Virtual Device in Excel

Related concepts:

- Exporting a Virtual Device

<!--NI_TOPIC bundle=switch-executive path=extended-configuration-tasks.html language=enus -->
## TOPIC 00054: Extended Configuration Tasks

- bundle_id: `switch-executive`
- source_path: `extended-configuration-tasks.html`
- source_url: https://docs-be.ni.com/bundle/switch-executive/raw/resource/enus/extended-configuration-tasks.html
- document_id: `switch-executive`
- page_type: `leaf`
- content_type: `concept`
- source_description: Some Switch Executive configuration tasks are only accessible in the extended configuration tabs in MAX. These tasks include: Reserving a channel for routingWhen you create a route with reserved for routing channels in the extended configuration tabs, Switch Executive dims the route in the Schematic

### Extended Configuration Tasks

Some Switch Executive configuration tasks are only accessible in the *extended
 configuration* tabs in MAX. These tasks include:

- Reserving a channel for routing Note When you create a route with reserved for routing channels in the extended
 configuration tabs, Switch Executive dims the route in the Schematic window. A
 dimmed route denotes that the route is not configurable in the Schematic
 Configuration tab.
- Disabling a channel
- Configuring exclusions
- Configuring buses

Although these tasks are not accessible in the Schematic Configuration tab, they are preserved in
 the virtual device configuration.

Parent topic:

Schematic Configuration

Related concepts:

- Extended Configuration

<!--NI_TOPIC bundle=switch-executive path=extended-configuration.html language=enus -->
## TOPIC 00055: Extended Configuration

- bundle_id: `switch-executive`
- source_path: `extended-configuration.html`
- source_url: https://docs-be.ni.com/bundle/switch-executive/raw/resource/enus/extended-configuration.html
- document_id: `switch-executive`
- page_type: `leaf`
- content_type: `concept`
- source_description: Use the Extended Configuration tabs—Channels/Exclusions, Hardwires/Buses, and Routes/Groups—to navigate through the configuration of an Switch Executive virtual device and configure channels, exclusions, hardwires, buses, route groups, and routes.

### Extended Configuration

Use the Extended Configuration tabs—Channels/Exclusions,
 Hardwires/Buses, and Routes/Groups—to
 navigate through the configuration of an Switch Executive virtual device and configure
 channels, exclusions, hardwires, buses, route groups, and routes.

[IMAGE alt='image' src='GUID-B5438B75-72B5-4667-8597-99CD73B3D9A2-a5.png']

Parent topic:

Configuring a Virtual Device

<!--NI_TOPIC bundle=switch-executive path=formatting-configuration-data-bus-channels.html language=enus -->
## TOPIC 00056: Formatting Configuration Data: Bus Channels

- bundle_id: `switch-executive`
- source_path: `formatting-configuration-data-bus-channels.html`
- source_url: https://docs-be.ni.com/bundle/switch-executive/raw/resource/enus/formatting-configuration-data-bus-channels.html
- document_id: `switch-executive`
- page_type: `leaf`
- content_type: `concept`
- source_description: Use the following guidelines when formatting Bus Channels in Excel.Switch Executive replaces the attribute value with "Imported Value if Unspecified" only at import. If "Imported Value if Unspecified" is N/A, Switch Executive ignores the attribute at import. Attribute (Column)Valid ValuesRequiredImp

### Formatting Configuration Data: Bus Channels

Note

import

| Attribute (Column) | Valid Values | Required | Imported Value if Unspecified |
| --- | --- | --- | --- |
| Bus Name | String | Yes | None |
| IVI Device | String | Yes | None |
| Base Channel | String | Yes | None |
| End Channel | String | Yes | None |

Parent topic:

Formatting Configuration Data

Related concepts:

- Importing Excel Data

<!--NI_TOPIC bundle=switch-executive path=formatting-configuration-data-buses.html language=enus -->
## TOPIC 00057: Formatting Configuration Data: Buses

- bundle_id: `switch-executive`
- source_path: `formatting-configuration-data-buses.html`
- source_url: https://docs-be.ni.com/bundle/switch-executive/raw/resource/enus/formatting-configuration-data-buses.html
- document_id: `switch-executive`
- page_type: `leaf`
- content_type: `concept`
- source_description: Use the following guidelines when formatting Buses in Excel.Switch Executive replaces the attribute value with "Imported Value if Unspecified" only at import. If "Imported Value if Unspecified" is N/A, Switch Executive ignores the attribute at import. Attribute (Column)Valid ValuesRequiredImported V

### Formatting Configuration Data: Buses

Note

import

| Attribute (Column) | Valid Values | Required | Imported Value if Unspecified |
| --- | --- | --- | --- |
| Bus Name | String | Yes | None |
| Hardwire Name Start Index | Integer | No | 0 |
| Comment | String Notice: Use ^t, ^r, and ^n for the tab, carriage return, and new line characters, respectively. | No | Empty String |

Parent topic:

Formatting Configuration Data

Related concepts:

- Importing Excel Data

<!--NI_TOPIC bundle=switch-executive path=formatting-configuration-data-channels.html language=enus -->
## TOPIC 00058: Formatting Configuration Data: Channels

- bundle_id: `switch-executive`
- source_path: `formatting-configuration-data-channels.html`
- source_url: https://docs-be.ni.com/bundle/switch-executive/raw/resource/enus/formatting-configuration-data-channels.html
- document_id: `switch-executive`
- page_type: `leaf`
- content_type: `concept`
- source_description: Use the following guidelines when formatting Channels in Excel.Switch Executive replaces the attribute value with "Imported Value if Unspecified" only at import. If "Imported Value if Unspecified" is N/A, Switch Executive ignores the attribute at import. Attribute (Column)Valid ValuesRequiredImporte

### Formatting Configuration Data: Channels

Note

import

| Attribute (Column) | Valid Values | Required | Imported Value if Unspecified |
| --- | --- | --- | --- |
| Channel IVI Device | String | Yes | None |
| Channel IVI Name | String | Yes | None |
| Alias | String | No | Empty String |
| Hardwire | String | No | Empty String |
| Reserved For Routing | Empty String or x Notice: Empty String means not reserved for routing | No | Empty String |
| Disabled | Empty String or x Notice: Empty String means not disabled | No | Empty String |
| Comment | String Notice: Use ^t, ^r, and ^n for the tab, carriage return, and new line characters, respectively. | No | Empty String |
| Wire Mode | 1, 2, or 4 | No | N/A |
| Settling Time (s) | Float | No | N/A |
| Impedance (Ohm) | Float | No | N/A |
| Bandwidth (Hz) | Float | No | N/A |
| DC Voltage (V) | Float | No | N/A |
| AC Voltage (V) | Float | No | N/A |
| DC Switching Current (A) | Float | No | N/A |
| AC Switching Current (A) | Float | No | N/A |
| DC Carry Current (A) | Float | No | N/A |
| AC Carry Current (A) | Float | No | N/A |
| DC Switching Power (W) | Float | No | N/A |
| AC Switching Power (W) | Float | No | N/A |
| DC Carry Power (W) | Float | No | N/A |
| AC Carry Power (W) | Float | No | N/A |

Parent topic:

Formatting Configuration Data

Related concepts:

- Importing Excel Data

<!--NI_TOPIC bundle=switch-executive path=formatting-configuration-data-exclusions.html language=enus -->
## TOPIC 00059: Formatting Configuration Data: Exclusions

- bundle_id: `switch-executive`
- source_path: `formatting-configuration-data-exclusions.html`
- source_url: https://docs-be.ni.com/bundle/switch-executive/raw/resource/enus/formatting-configuration-data-exclusions.html
- document_id: `switch-executive`
- page_type: `leaf`
- content_type: `concept`
- source_description: Use the following guidelines when formatting Exclusions in Excel.Switch Executive replaces the attribute value with "Imported Value if Unspecified" only at import. If "Imported Value if Unspecified" is N/A, Switch Executive ignores the attribute at import. Attribute (Column)Valid ValuesRequiredImpor

### Formatting Configuration Data: Exclusions

Note

import

| Attribute (Column) | Valid Values | Required | Imported Value if Unspecified |
| --- | --- | --- | --- |
| Exclusion Name | String | Yes | None |
| Type | Mutual, Set | No | Mutual |
| Disabled | Empty String or x Notice: Empty String means not disabled. | No | Empty String |
| Comment | String Notice: Use ^t, ^r, and ^n for the tab, carriage return, and new line characters, respectively. | No | Empty String |

Parent topic:

Formatting Configuration Data

Related concepts:

- Importing Excel Data

<!--NI_TOPIC bundle=switch-executive path=formatting-configuration-data-hardwires.html language=enus -->
## TOPIC 00060: Formatting Configuration Data: Hardwires

- bundle_id: `switch-executive`
- source_path: `formatting-configuration-data-hardwires.html`
- source_url: https://docs-be.ni.com/bundle/switch-executive/raw/resource/enus/formatting-configuration-data-hardwires.html
- document_id: `switch-executive`
- page_type: `leaf`
- content_type: `concept`
- source_description: Use the following guidelines when formatting Hardwires in Excel.Switch Executive replaces the attribute value with "Imported Value if Unspecified" only at import. If "Imported Value if Unspecified" is N/A, Switch Executive ignores the attribute at import. Attribute (Column)Valid ValuesRequiredImport

### Formatting Configuration Data: Hardwires

Note

import

| Attribute (Column) | Valid Values | Required | Imported Value if Unspecified |
| --- | --- | --- | --- |
| Hardwire Name | String | Yes | None |
| Comment | String Notice: Use ^t, ^r, and ^n for the tab, carriage return, and new line characters, respectively. | No | Empty String |

Parent topic:

Formatting Configuration Data

Related concepts:

- Importing Excel Data

<!--NI_TOPIC bundle=switch-executive path=formatting-configuration-data-ivi-devices.html language=enus -->
## TOPIC 00061: Formatting Configuration Data: IVI Devices

- bundle_id: `switch-executive`
- source_path: `formatting-configuration-data-ivi-devices.html`
- source_url: https://docs-be.ni.com/bundle/switch-executive/raw/resource/enus/formatting-configuration-data-ivi-devices.html
- document_id: `switch-executive`
- page_type: `leaf`
- content_type: `concept`
- source_description: Use the following guidelines when formatting IVI Devices in Excel.Switch Executive replaces the attribute value with "Imported Value if Unspecified" only at import. If "Imported Value if Unspecified" is N/A, Switch Executive ignores the attribute at import. Attribute (Column)Valid ValuesRequiredImpo

### Formatting Configuration Data: IVI Devices

Note

import

| Attribute (Column) | Valid Values | Required | Imported Value if Unspecified |
| --- | --- | --- | --- |
| IVI Device Name | String | Yes | None |
| Comment | String Notice: Use ^t, ^r, and ^n for the tab, carriage return, and new line characters, respectively. | No | Empty String |

Parent topic:

Formatting Configuration Data

Related concepts:

- Importing Excel Data

<!--NI_TOPIC bundle=switch-executive path=formatting-configuration-data-mutual-exclusio.html language=enus -->
## TOPIC 00062: Formatting Configuration Data: Mutual Exclusion Channels

- bundle_id: `switch-executive`
- source_path: `formatting-configuration-data-mutual-exclusio.html`
- source_url: https://docs-be.ni.com/bundle/switch-executive/raw/resource/enus/formatting-configuration-data-mutual-exclusio.html
- document_id: `switch-executive`
- page_type: `leaf`
- content_type: `concept`
- source_description: Use the following guidelines when formatting Mutual Exclusion Channels in Excel.Switch Executive replaces the attribute value with "Imported Value if Unspecified" only at import. If "Imported Value if Unspecified" is N/A, Switch Executive ignores the attribute at import. Attribute (Column)Valid Valu

### Formatting Configuration Data: Mutual Exclusion Channels

Note

import

| Attribute (Column) | Valid Values | Required | Imported Value if Unspecified |
| --- | --- | --- | --- |
| Exclusion Name | String | Yes | None |
| Channel | String | Yes | None |

Parent topic:

Formatting Configuration Data

Related concepts:

- Importing Excel Data

<!--NI_TOPIC bundle=switch-executive path=formatting-configuration-data-route-group-chi.html language=enus -->
## TOPIC 00063: Formatting Configuration Data: Route Group Children

- bundle_id: `switch-executive`
- source_path: `formatting-configuration-data-route-group-chi.html`
- source_url: https://docs-be.ni.com/bundle/switch-executive/raw/resource/enus/formatting-configuration-data-route-group-chi.html
- document_id: `switch-executive`
- page_type: `leaf`
- content_type: `concept`
- source_description: Use the following guidelines when formatting Route Group Children in Excel.Switch Executive replaces the attribute value with "Imported Value if Unspecified" only at import. If "Imported Value if Unspecified" is N/A, Switch Executive ignores the attribute at import. Attribute (Column)Valid ValuesReq

### Formatting Configuration Data: Route Group Children

Note

import

| Attribute (Column) | Valid Values | Required | Imported Value if Unspecified |
| --- | --- | --- | --- |
| Route Group Name | String | Yes | None |
| Child | String | Yes | None |

Parent topic:

Formatting Configuration Data

Related concepts:

- Importing Excel Data

<!--NI_TOPIC bundle=switch-executive path=formatting-configuration-data-route-groups.html language=enus -->
## TOPIC 00064: Formatting Configuration Data: Route Groups

- bundle_id: `switch-executive`
- source_path: `formatting-configuration-data-route-groups.html`
- source_url: https://docs-be.ni.com/bundle/switch-executive/raw/resource/enus/formatting-configuration-data-route-groups.html
- document_id: `switch-executive`
- page_type: `leaf`
- content_type: `concept`
- source_description: Use the following guidelines when formatting Route Groups in Excel.Switch Executive replaces the attribute value with "Imported Value if Unspecified" only at import. If "Imported Value if Unspecified" is N/A, Switch Executive ignores the attribute at import. Attribute (Column)Valid ValuesRequiredImp

### Formatting Configuration Data: Route Groups

Note

import

| Attribute (Column) | Valid Values | Required | Imported Value if Unspecified |
| --- | --- | --- | --- |
| Route Group Name | String | Yes | None |
| Comment | String Notice: Use ^t, ^r, and ^n for the tab, carriage return, and new line characters, respectively. | No | Empty String |

Parent topic:

Formatting Configuration Data

Related concepts:

- Importing Excel Data

<!--NI_TOPIC bundle=switch-executive path=formatting-configuration-data-routes.html language=enus -->
## TOPIC 00065: Formatting Configuration Data: Routes

- bundle_id: `switch-executive`
- source_path: `formatting-configuration-data-routes.html`
- source_url: https://docs-be.ni.com/bundle/switch-executive/raw/resource/enus/formatting-configuration-data-routes.html
- document_id: `switch-executive`
- page_type: `leaf`
- content_type: `concept`
- source_description: Use the following guidelines when formatting Routes in Excel.Switch Executive replaces the attribute value with "Imported Value if Unspecified" only at import. If "Imported Value if Unspecified" is N/A, Switch Executive ignores the attribute at import. Attribute (Column)Valid ValuesRequiredImported

### Formatting Configuration Data: Routes

Note

import

| Attribute (Column) | Valid Values | Required | Imported Value if Unspecified |
| --- | --- | --- | --- |
| Route Name | String | Yes | None |
| Endpoint1 | String | Yes* | Uses route spec |
| Endpoint2 | String | Yes* | Uses route spec |
| Specification | String | Yes* | Uses endpoints |
| Type | Specified By Full Path, Find By Endpoints, Find If Full Path Fails | Yes | None |
| Multiconnect Mode | Multiconnect, No Multiconnect | Yes | None |
| Comment | String Notice: Use ^t, ^r, and ^n for the tab, carriage return, and new line characters, respectively. | No | Empty String |
| Wire Mode | 1, 2, or 4 | No | Uses Endpoint1 or route specification |
| Settling Time (s) | Float | No | None |
| Impedance (Ohm) | Float | No | None |
| Bandwidth (Hz) | Float | No | None |
| DC Voltage (V) | Float | No | None |
| AC Voltage (V) | Float | No | None |
| DC Switching Current (A) | Float | No | None |
| AC Switching Current (A) | Float | No | None |
| DC Carry Current (A) | Float | No | None |
| AC Carry Current (A) | Float | No | None |
| DC Switching Power (W) | Float | No | None |
| AC Switching Power (W) | Float | No | None |
| DC Carry Power (W) | Float | No | None |
| AC Carry Power (W) | Float | No | None |

* One of these is required: either both endpoints or the specification. When all three are
 specified, the specification is used before the endpoints.

Parent topic:

Formatting Configuration Data

Related concepts:

- Importing Excel Data

<!--NI_TOPIC bundle=switch-executive path=formatting-configuration-data-set-exclusion-s-2.html language=enus -->
## TOPIC 00066: Formatting Configuration Data: Set Exclusion Set1 Channels

- bundle_id: `switch-executive`
- source_path: `formatting-configuration-data-set-exclusion-s-2.html`
- source_url: https://docs-be.ni.com/bundle/switch-executive/raw/resource/enus/formatting-configuration-data-set-exclusion-s-2.html
- document_id: `switch-executive`
- page_type: `leaf`
- content_type: `concept`
- source_description: Use the following guidelines when formatting Set Exclusion Set1 Channels in Excel.Switch Executive replaces the attribute value with "Imported Value if Unspecified" only at import. If "Imported Value if Unspecified" is N/A, Switch Executive ignores the attribute at import. Attribute (Column)Valid Va

### Formatting Configuration Data: Set Exclusion Set1 Channels

Note

import

| Attribute (Column) | Valid Values | Required | Imported Value if Unspecified |
| --- | --- | --- | --- |
| Exclusion Name | String | Yes | None |
| Set1 Channel | String | Yes | None |

Parent topic:

Formatting Configuration Data

Related concepts:

- Importing Excel Data

<!--NI_TOPIC bundle=switch-executive path=formatting-configuration-data-set-exclusion-s.html language=enus -->
## TOPIC 00067: Formatting Configuration Data: Set Exclusion Set2 Channels

- bundle_id: `switch-executive`
- source_path: `formatting-configuration-data-set-exclusion-s.html`
- source_url: https://docs-be.ni.com/bundle/switch-executive/raw/resource/enus/formatting-configuration-data-set-exclusion-s.html
- document_id: `switch-executive`
- page_type: `leaf`
- content_type: `concept`
- source_description: Use the following guidelines when formatting Set Exclusion Set2 Channels in Excel.Switch Executive replaces the attribute value with "Imported Value if Unspecified" only at import. If "Imported Value if Unspecified" is N/A, Switch Executive ignores the attribute at import. Attribute (Column)Valid Va

### Formatting Configuration Data: Set Exclusion Set2 Channels

Note

import

| Attribute (Column) | Valid Values | Required | Imported Value if Unspecified |
| --- | --- | --- | --- |
| Exclusion Name | String | Yes | None |
| Set2 Channel | String | Yes | None |

Parent topic:

Formatting Configuration Data

Related concepts:

- Importing Excel Data

<!--NI_TOPIC bundle=switch-executive path=formatting-configuration-data-virtual-device.html language=enus -->
## TOPIC 00068: Formatting Configuration Data: Virtual Device

- bundle_id: `switch-executive`
- source_path: `formatting-configuration-data-virtual-device.html`
- source_url: https://docs-be.ni.com/bundle/switch-executive/raw/resource/enus/formatting-configuration-data-virtual-device.html
- document_id: `switch-executive`
- page_type: `leaf`
- content_type: `concept`
- source_description: Use the following guidelines when formatting a Virtual Device in Excel.Switch Executive replaces the attribute value with "Imported Value if Unspecified" only at import. If "Imported Value if Unspecified" is N/A, Switch Executive ignores the attribute at import. Attribute (Column)Valid ValuesRequire

### Formatting Configuration Data: Virtual Device

Note

import

| Attribute (Column) | Valid Values | Required | Imported Value if Unspecified |
| --- | --- | --- | --- |
| Virtual Device Name | String | No | Value specified in Import dialog or API |
| Comment | String Notice: Use ^t, ^r, and ^n for the tab, carriage return, and new line characters, respectively. | No | Empty String |
| Export Schema Version | 1 | No | 1 |
| Channel Name Style | Full Name OnlyAlias Or Full NameAlias And Full Name | No | Alias Or Full Name |
| Route Editor Channel Display | Show Channels Without Aliases Hide Channels Without Aliases | No | Show Channels Without Aliases |
| Route Editor Route Updates | Auto Update Routes Manual Update Routes | No | Auto Update Routes |
| Route Editor Route Search Depth | Low Medium High | No | Low |
| Schematic Route Display | Hide RoutesShow Routes | No | Hide Routes |
| Schematic Route Deletion | Show Notification DialogDo Not Show Notification Dialog | No | Show Notification Dialog |

Parent topic:

Formatting Configuration Data

Related concepts:

- Importing Excel Data

<!--NI_TOPIC bundle=switch-executive path=formatting-configuration-data.html language=enus -->
## TOPIC 00069: Formatting Configuration Data

- bundle_id: `switch-executive`
- source_path: `formatting-configuration-data.html`
- source_url: https://docs-be.ni.com/bundle/switch-executive/raw/resource/enus/formatting-configuration-data.html
- document_id: `switch-executive`
- page_type: `leaf`
- content_type: `concept`
- source_description: Switch Executive organizes the configuration data associated with a virtual device in the columns and rows of a worksheet. To modify and add data without affecting the ability to import the file, adhere to the following guidelines.If you fail to format data in Excel in accordance with the following

### Formatting Configuration Data

Note

Note

#### Rows

- Inserting a row —You can insert a row anywhere in a workbook.
  - Switch Executive requires an empty row between configuration data and
 any custom non-configuration data you add to a worksheet.
  - Switch Executive does not require an empty row between a column heading
 row and its data rows.

#### Columns

- Inserting a column —You can insert a column anywhere in a workbook.
  - Switch Executive accepts empty columns.
- Deleting a column —You can only delete a column in a workbook if it is not a required column. All other columns are optional.
- Renaming a column —Not supported, unless the column was added by a user.
- Reordering columns —You can reorder any column in a workbook.

#### Worksheets

- Inserting a worksheet —You can insert a worksheet or a custom sheet, such as a chart sheet, macro, or a dialog sheet, anywhere in a workbook.
- Inserting a chart or object —You can insert a chart or other object anywhere in a worksheet.
- Deleting a worksheet —You can only delete a worksheet if it is not the IVI Device worksheet. The IVI Device worksheet is required when you import; all other worksheets are optional.
- Renaming a worksheet —You can rename any worksheet.
- Reordering worksheets —You can reorder any worksheet.

#### Workbooks

- Renaming a workbook —You can rename a workbook.

Parent topic:

Managing a Virtual Device in Excel

<!--NI_TOPIC bundle=switch-executive path=fundamentals.html language=enus -->
## TOPIC 00070: Fundamentals

- bundle_id: `switch-executive`
- source_path: `fundamentals.html`
- source_url: https://docs-be.ni.com/bundle/switch-executive/raw/resource/enus/fundamentals.html
- document_id: `switch-executive`
- page_type: `leaf`
- content_type: `concept`
- source_description: This section conatins information about the terminology related to NI Switch Executive.

### Fundamentals

This section conatins information about the terminology related to NI Switch Executive.

Parent topic:

Switch Executive Help

<!--NI_TOPIC bundle=switch-executive path=generating-a-report.html language=enus -->
## TOPIC 00071: Generating a Report

- bundle_id: `switch-executive`
- source_path: `generating-a-report.html`
- source_url: https://docs-be.ni.com/bundle/switch-executive/raw/resource/enus/generating-a-report.html
- document_id: `switch-executive`
- page_type: `leaf`
- content_type: `concept`
- source_description: Complete the following steps to generate a report of your Switch Executive virtual device configuration: Launch MAX with Switch Executive. Expand Devices and Interfaces»NI Switch Executive Virtual Devices. Select the virtual device you want to report. Click . A file window opens. Select a location t

### Generating a Report

Complete the following steps to generate a report of your Switch Executive virtual device
 configuration:

1. Launch MAX with Switch Executive.
2. Expand Devices and Interfaces»NI Switch Executive Virtual Devices .
3. Select the virtual device you want to report.
4. Click . A file
 window opens.
5. Select a location to save your report and click OK .
6. Click on the
 Switch Executive taskbar to save the changes.

Tip

Parent topic:

Using Switch Executive in MAX

<!--NI_TOPIC bundle=switch-executive path=getting-started-1.html language=enus -->
## TOPIC 00072: Getting Started

- bundle_id: `switch-executive`
- source_path: `getting-started-1.html`
- source_url: https://docs-be.ni.com/bundle/switch-executive/raw/resource/enus/getting-started-1.html
- document_id: `switch-executive`
- page_type: `leaf`
- content_type: `concept`
- source_description: You can find information about how to begin using Switch Executive with your ADE, any files to include in your application, and considerations for each ADE in this topic.To successfully build your application, you must have Switch Executive and one of the following ADEs installed:LabVIEW LabWindows/

### Getting Started

You can find information about how to begin using Switch Executive with your ADE, any files to
 include in your application, and considerations for each ADE in this topic.

To successfully build your application, you must have Switch Executive and one of the following
 ADEs installed:

- LabVIEW
- LabWindows/CVI
- Visual C++
- Visual Basic
- TestStand

Parent topic:

Programming with Switch Executive

Related concepts:

- Using Switch Executive in LabVIEW
- Using Switch Executive in LabWindows/CVI
- Using Switch Executive in Visual C++
- Using Switch Executive in Visual Basic
- Using Switch Executive in NI TestStand

<!--NI_TOPIC bundle=switch-executive path=getting-started-with-schematic-configuration.html language=enus -->
## TOPIC 00073: Getting Started with Schematic Configuration

- bundle_id: `switch-executive`
- source_path: `getting-started-with-schematic-configuration.html`
- source_url: https://docs-be.ni.com/bundle/switch-executive/raw/resource/enus/getting-started-with-schematic-configuration.html
- document_id: `switch-executive`
- page_type: `leaf`
- content_type: `concept`
- source_description: The following steps represent the general workflow for schematic configuration: Launch MAX with Switch Executive. Expand Devices and Interfaces»Switch Executive Virtual Devices. Select the NI Switch Executive virtual device to modify and navigate to the Schematic Configuration tab. Click at the top

### Getting Started with Schematic Configuration

The following steps represent the general workflow for schematic configuration:

1. Launch MAX with Switch Executive.
2. Expand Devices and Interfaces»Switch Executive Virtual Devices .
3. Select the NI Switch Executive virtual device to modify and navigate to the Schematic Configuration tab.
4. Click at the
 top of the Routes and Route Groups listbox to create a route
 group .
5. Select the device that contains the channel to configure in the Devices listbox. The device schematic displays in the Schematic window.
6. Click a channel name in the Schematic window to access the Edit Alias & Hardwire dialog box and configure channel aliases and hardwires .
7. Repeat step 6 until you have configured all the channel aliases and hardwires on the virtual device.
8. Complete one of the following steps depending on the topology of the switch device selected to
 create a route between channels: The route displays in the Schematic window and is added to the
 route group. Note You can click
 the point of intersection between two channels, crosspoint or channel connection point, in
 the Schematic window to *delete the route* between
 channels.
  - General purpose topology —Click a crosspoint between two
 channels on the specific relay you want to use in the Schematic 
 window.
  - Matrix topology —Click a crosspoint between two channels in the
 Schematic window.
  - Multiplexer topology —Click a channel connection point in the
 Schematic window.
  - Third-party IVI-switch and independent topologies —Select one
 channel from the Channel 1 listbox and one channel from the
 Channel 2 listbox and click Create .
9. Repeat step 8 until you have created all the routes that you want to add to the route group. You
 can select a different device in the Devices listbox to create routes
 across multiple devices. Note By
 default, NI Switch Executive does not display the routes associated with a route group in
 the Routes and Route Groups listbox. Enable the Show
 Routes checkbox below the Routes and Route Groups
 listbox to display the routes associated with a route group and manage those routes
 individually.
10. Click on the
 Switch Executive taskbar to save the changes.
11. Validate the changes.

Parent topic:

Schematic Configuration

Related concepts:

- Adding a Route Group
- Configuring a Channel
- Adding a Route
- Independent Topologies
- Deleting a Route
- Validating a Virtual Device

<!--NI_TOPIC bundle=switch-executive path=getting-started.html language=enus -->
## TOPIC 00074: Getting Started

- bundle_id: `switch-executive`
- source_path: `getting-started.html`
- source_url: https://docs-be.ni.com/bundle/switch-executive/raw/resource/enus/getting-started.html
- document_id: `switch-executive`
- page_type: `leaf`
- content_type: `concept`
- source_description: Switch Executive is a configuration application you can use to simplify your switching systems. With Switch Executive, you can perform any of the following tasks: Develop multiple device switch systems represented as a single virtual device Create end-to-end signal routing Make route selections base

### Getting Started

Switch Executive is a configuration application you can use to simplify your switching systems.
 With Switch Executive, you can perform any of the following tasks:

- Develop multiple device switch systems represented as a single virtual device
- Create end-to-end signal routing
- Make route selections based on signal characteristics and switch capabilities
- Create route groups used to make intelligent resource selections when creating routes
- Create switch routing for end-to-end calibration and maximum execution speed
- Create aliases for channels
- Preconfigure routes and route groups that can be called by name at run time
- Control IVI-compliant third-party switches
- Generate a report of your switching system
- Create routes graphically with an interactive schematic view of your switch devices
- Configure large and complex switching systems quickly with Excel integration
- View the state of switches with the debug panel

Note

accessing the switch IVI session

Parent topic:

Switch Executive Help

<!--NI_TOPIC bundle=switch-executive path=hardwire.html language=enus -->
## TOPIC 00075: Hardwire

- bundle_id: `switch-executive`
- source_path: `hardwire.html`
- source_url: https://docs-be.ni.com/bundle/switch-executive/raw/resource/enus/hardwire.html
- document_id: `switch-executive`
- page_type: `leaf`
- content_type: `concept`
- source_description: A hardwire is any physical connection between switch channels, such as wiring, analog buses, matrix expansion plugs, and so on. A hardwire can have any number of channels attached to it.Some characters are reserved and cannot be used in hardwire names.

### Hardwire

hardwire

Note

reserved

Parent topic:

Fundamentals

Related concepts:

- Schematic Configuration
- Extended Configuration
- Using the Configuration API

Related information:

- Naming Conventions

<!--NI_TOPIC bundle=switch-executive path=hardwires-and-reserved-for-routing-channels.html language=enus -->
## TOPIC 00076: Hardwires and Reserved for Routing Channels

- bundle_id: `switch-executive`
- source_path: `hardwires-and-reserved-for-routing-channels.html`
- source_url: https://docs-be.ni.com/bundle/switch-executive/raw/resource/enus/hardwires-and-reserved-for-routing-channels.html
- document_id: `switch-executive`
- page_type: `leaf`
- content_type: `concept`
- source_description: Reserved for routing is an extension of the IVI configuration channel as defined by the IVI specification and requires intermediate channels on a route to be marked as configuration channels.Switch Executive takes full advantage of the IVI configuration channel definition. By marking channels as res

### Hardwires and Reserved for Routing Channels

*Reserved for routing* is an extension of the IVI configuration channel as defined by
 the IVI specification and requires intermediate channels on a route to be marked as
 configuration channels.

Switch Executive takes full advantage of the IVI configuration channel definition. By marking
 channels as reserved for routing, creating a route across multiple devices becomes very
 easy.

In the following figure, to connect dev_1/com0 to dev_2/ch0,
 the signal travels across hardwire hw_0, dev_1/ch0,
 and dev_2/com0. To complete the path, dev_1/ch0 and
 dev_2/com0 should be marked as reserved for routing. Because the
 IVI configuration channel definition is applied to dev_1 and
 dev_2 as a single device, the two appropriate channels can be
 marked as reserved for routing.

[IMAGE alt='image' src='GUID-69907C7D-5399-41B0-9C69-92F5887D8049-a5.gif']

To simplify marking channels as reserved for routing, Switch Executive allows a channel not
 marked as reserved for routing to be used as an intermediate channel if—and only if—the
 channel is connected to a hardwire connected to an endpoint of the route. For example,
 in the following figure, dev_1/r0 can be connected to
 dev_2/c0 even though dev_2/r0 is not marked as
 reserved for routing.

[IMAGE alt='image' src='GUID-A7BA8BD6-229D-41EA-9A55-7C5A991357C9-a5.gif']

Tip

bus

Parent topic:

Hardwire

Related concepts:

- Reserved for Routing
- Bus

<!--NI_TOPIC bundle=switch-executive path=hardwires-buses-tab.html language=enus -->
## TOPIC 00077: Hardwires/Buses Tab

- bundle_id: `switch-executive`
- source_path: `hardwires-buses-tab.html`
- source_url: https://docs-be.ni.com/bundle/switch-executive/raw/resource/enus/hardwires-buses-tab.html
- document_id: `switch-executive`
- page_type: `leaf`
- content_type: `concept`
- source_description: Use the Hardwires/Buses tab to configure hardwires and buses in Switch Executive.Hardwires that belong to a bus only display in the Buses listbox and are nested underneath their respective bus. Hardwires that do not belong to a bus display in the Hardwires listbox.

### Hardwires/Buses Tab

Use the Hardwires/Buses tab to configure hardwires and buses in Switch
 Executive.

Hardwires that belong to a bus only display in the Buses listbox and are
 nested underneath their respective bus. Hardwires that do not belong to a bus display in
 the Hardwires listbox.

[IMAGE alt='image' src='GUID-280411D7-3B00-4BEC-8BE4-0B5FEB636133-a5.png']

Parent topic:

Extended Configuration

<!--NI_TOPIC bundle=switch-executive path=import.html language=enus -->
## TOPIC 00078: Import

- bundle_id: `switch-executive`
- source_path: `import.html`
- source_url: https://docs-be.ni.com/bundle/switch-executive/raw/resource/enus/import.html
- document_id: `switch-executive`
- page_type: `leaf`
- content_type: `concept`
- source_description: After you have managed the configuration of a virtual device in other file formats or with other programs such as Microsoft Excel, import the configuration back to Switch Executive to continue working with the virtual device.

### Import

After you have managed the configuration of a virtual device in other file formats or with other
 programs such as Microsoft Excel, import the configuration back to Switch Executive to
 continue working with the virtual device.

Parent topic:

Concepts

Related concepts:

- Importing a Virtual Device
- Using the Configuration API

<!--NI_TOPIC bundle=switch-executive path=importing-a-virtual-device.html language=enus -->
## TOPIC 00079: Importing a Virtual Device

- bundle_id: `switch-executive`
- source_path: `importing-a-virtual-device.html`
- source_url: https://docs-be.ni.com/bundle/switch-executive/raw/resource/enus/importing-a-virtual-device.html
- document_id: `switch-executive`
- page_type: `leaf`
- content_type: `concept`
- source_description: Complete the following steps to import the configuration file of an Switch Executive virtual device: Launch MAX with Switch Executive. Expand Devices and Interfaces. Right-click Switch Executive Virtual Devices and select . The Import dialog box opens. Select an Import Format for the virtual device

### Importing a Virtual Device

Complete the following steps to import the configuration file of an Switch Executive virtual
 device:

1. Launch MAX with Switch Executive.
2. Expand Devices and Interfaces .
3. Right-click Switch Executive Virtual Devices and select . The
 Import dialog box opens.
4. Select an Import Format for the virtual device configuration. Switch
 Executive supports the following import formats. Note If using the Configuration Export
 (.nce) file format, skip to step 7.
5. Configuration Export File (.nce) —Recommended for import and export of complete configurations that do not
 need editing outside of NI Switch Executive. Allows saving of system
 configuration information for all devices and interfaces, including NI
 Switch Executive virtual devices.
6. Switch Executive Export File (.xml) —Recommended for import and export of individual virtual device
 configurations that do not need editing outside of Switch
 Executive.
7. Microsoft Excel Workbooks (.xls and .xlsx) —Recommended for import and export of individual virtual device
 configurations in a format suitable for editing. Components of the
 switching system (virtual devices, channels, routes, and so on) are
 contained in separate workbook sheets.
8. Tab-delimited File (.txt) —Recommended for import and export of individual virtual device
 configurations in a format suitable for editing. When opened in a
 spreadsheet editing program, tab-delimited files contain the components
 of the switching system (virtual devices, channels, routes, and so on)
 in a single workbook sheet.
9. Select the Source File to import. The source file is the file that contains the virtual device configuration you exported from the development system.
10. Select a name for the virtual device from the Virtual Device Name 
 drop-down listbox. Note To ensure that Virtual Device Name matches the virtual device name in the file,
 recommends that you always select (Extract name from source
 file). Note Make sure the Switch Executive
 virtual device name matches that used in your test code.
11. Click Finish to import the virtual device configuration. The
 Switch Executive virtual device configuration is loaded into MAX. Note (XML file format only) If any
 errors occur during this process (such as an IVI device not being accessible),
 the virtual device is created, but the IVI switches that caused errors are not
 added. When the IVI switches are not added, the channels of those switches are
 also not added, which can break routes or route groups. You can *manually
 add* the IVI switches later.

Parent topic:

Using Switch Executive in MAX

Related concepts:

- Adding IVI Switches

<!--NI_TOPIC bundle=switch-executive path=importing-configurations.html language=enus -->
## TOPIC 00080: Importing Configurations

- bundle_id: `switch-executive`
- source_path: `importing-configurations.html`
- source_url: https://docs-be.ni.com/bundle/switch-executive/raw/resource/enus/importing-configurations.html
- document_id: `switch-executive`
- page_type: `leaf`
- content_type: `concept`
- source_description: After you export configuration files from the development system, complete the following steps on the target system to import the configuration files necessary to deploy an Switch Executive virtual device: Verify that the target has the following items installed: A licensed deployment or development

### Importing Configurations

After you *export* configuration files from the development system, complete the
 following steps on the target system to import the configuration files necessary to deploy an
 Switch Executive virtual device:

1. Verify that the target has the following items installed:
  1. A licensed deployment or development copy of Switch Executive
  2. Windows 8.1/8.0/7/Vista/XP SP3
  3. IVI instrument drivers for your switch modules Note Currently C class drivers are supported
 only. You can create your own C class IVI drivers with Measurement Studio
 templates—specifically in LabWindows/CVI. For more information about Measurement
 Studio, visit ni.com.
  4. Skip steps e and f if you are importing a virtual device from a .nce 
 file.
  5. If the virtual device you are deploying uses DAQmx switches, a DAQmx configuration
 file imported from the development system from which you are deploying. Complete the
 following steps to import the DAQmx configuration file:
    1. Launch Measurement & Automation Explorer (MAX).
    2. Import the DAQmx configuration file using the Import Configuration Wizard in MAX.
 Refer to the Importing and Exporting Configurations topic of the
 Measurement & Automation Explorer Help for NI-DAQmx for
 more information by navigating in MAX to Help»Help Topics»NI-DAQmx»MAX
 Help for NI-DAQmx .
  6. (Optional) If you are using IVI devices, an IVI configuration file copied
 from and installed in the same directory as the development system from which you are
 deploying. Copying the IVI configuration file from the development system to the target
 system ensures that both systems are using the same IVI Logical Names.
2. Import the NI Switch Executive virtual device configuration file.

Parent topic:

Deploying a Virtual Device

Related concepts:

- Exporting Configurations
- Activating Your Software
- Importing a Virtual Device

<!--NI_TOPIC bundle=switch-executive path=importing-excel-data.html language=enus -->
## TOPIC 00081: Importing Excel Data

- bundle_id: `switch-executive`
- source_path: `importing-excel-data.html`
- source_url: https://docs-be.ni.com/bundle/switch-executive/raw/resource/enus/importing-excel-data.html
- document_id: `switch-executive`
- page_type: `leaf`
- content_type: `concept`
- source_description: After you have customized the virtual device configuration in Excel, import the configuration to continue working with the virtual device in other environments/interfaces.Switch Executive preserves the state of your file at import to preserve custom, non-configuration data. Troubleshooting If you ex

### Importing Excel Data

import

Note

#### Troubleshooting

If you experience an error at import, verify that you have customized data in Excel in accordance with the *formatting* rules and guidelines.

Parent topic:

Managing a Virtual Device in Excel

Related concepts:

- Importing a Virtual Device
- Formatting Configuration Data

<!--NI_TOPIC bundle=switch-executive path=independent-topologies.html language=enus -->
## TOPIC 00082: Independent Topologies

- bundle_id: `switch-executive`
- source_path: `independent-topologies.html`
- source_url: https://docs-be.ni.com/bundle/switch-executive/raw/resource/enus/independent-topologies.html
- document_id: `switch-executive`
- page_type: `leaf`
- content_type: `concept`
- source_description: Some switch modules can be configured with an independent topology. Like third-party switch modules, switch modules using an independent topology do not contain the information required to draw a schematic. Instead, Switch Executive displays the schematic as three listboxes, Channel 1, Channel 2, an

### Independent Topologies

Some switch modules can be configured with an independent topology. Like *third-party*
 switch modules, switch modules using an independent topology do not contain the information
 required to draw a schematic. Instead, Switch Executive displays the schematic as three
 listboxes, Channel 1, Channel 2, and
 Connections, as shown in the following figure:

[IMAGE alt='image' src='GUID-71CF7EF8-0A1C-443D-9ADB-814412897FC1-a5.png']

The Routes and Route Groups and Devices listboxes
 function the same in an independent topology as they do in other topologies. In an independent
 topology, the Channel 1 and Channel 2 listboxes
 display all the channels available for the device, including the aliases and hardwires
 associated with the channels. The Connections listbox displays the
 routes associated with a route group.

Schematic Configuration

Note

Schematic
 Configuration

#### Route Groups

Schematic configuration of a route group in an independent topology is similar to schematic
 configuration of a route group in other topologies. Refer to the following related topics
 for information about configuring a route group in an independent topology:

#### Routes

Schematic configuration of a route in an independent topology has similarities and differences with schematic configuration of a route in other topologies. Refer to the following related topics for information about configuring a route in an independent topology:

- Adding a Route Complete the following steps to add a route to an independent topology:
  1. Launch MAX with Switch Executive.
  2. Expand Devices and Interfaces»Switch Executive Virtual
 Devices .
  3. Select the Switch Executive virtual device to modify and navigate to the
 Schematic Configuration tab.
  4. Select the device with the independent topology to which you want to add a route in
 the Devices listbox.
  5. Enable the Show Routes checkbox below the Routes and Route
 Groups listbox.
  6. Complete one of the following steps to add a route:
    - Add a route not associated with a route
 group —Click above the Routes and Route
 Groups listbox. Tip You can also right-click in the
 Routes and Route Groups listbox and select
 Add Route»Empty Route.
    - Add a route associated with a route
 group —Click the route group to which you want to add a route in the
 Routes and Route Groups listbox. You can add a route to
 an existing route group or create a new route group to which to add a
 route. Note If the
 virtual device does not have any existing route groups defined, Switch Executive
 creates a default route group, RouteGroup0, in the
 Routes and Route Groups listbox to which you can add a
 route.
  7. Select a channel in the Channel 1 listbox as an endpoint for the route.
  8. Select a channel in the Channel 2 listbox as another endpoint for the route.
  9. Confirm the route creation: Switch Executive adds a route with a predefined name to the Routes
 and Route Groups listbox, adds a checkmark to the left of the device
 name in the Devices listbox to indicate a route exists on the
 device, and displays the path of the route in the Connections
 listbox.
    - If the route selected is not associated with a route group, click
 Change .
    - If the route selected is associated with a route group, click
 Create .
  10. Click on the Switch Executive taskbar to save the changes.

Parent topic:

Schematic Configuration

Related concepts:

- Third-Party Switches
- Adding a Route Group
- Copying a Route Group
- Nesting a Route Group
- Disassociating a Nested Route Group
- Deleting a Route Group
- Editing a Route
- Sharing a Route Between Route Groups
- Disassociating a Route from a Route Group
- Deleting a Route

<!--NI_TOPIC bundle=switch-executive path=ivi-switch.html language=enus -->
## TOPIC 00083: IVI Switch

- bundle_id: `switch-executive`
- source_path: `ivi-switch.html`
- source_url: https://docs-be.ni.com/bundle/switch-executive/raw/resource/enus/ivi-switch.html
- document_id: `switch-executive`
- page_type: `leaf`
- content_type: `concept`
- source_description: An IVI switch is a switch module that uses an IVI-compliant instrument driver. The IVI Foundation defines IVI-compliance in the IviSwtch Class Specification, available at www.ivifoundation.org. IVI-compliant switches include all National Instrument switches and some third-party switches.

### IVI Switch

An *IVI switch* is a switch module that uses an IVI-compliant instrument driver. The
 IVI Foundation defines IVI-compliance in the IviSwtch Class Specification, available at
 www.ivifoundation.org. IVI-compliant switches include all National Instrument switches
 and some third-party switches.

Parent topic:

Fundamentals

Related concepts:

- Configuring IVI Switches
- Using the Configuration API

<!--NI_TOPIC bundle=switch-executive path=managing-a-virtual-device-in-excel.html language=enus -->
## TOPIC 00084: Managing a Virtual Device in Excel

- bundle_id: `switch-executive`
- source_path: `managing-a-virtual-device-in-excel.html`
- source_url: https://docs-be.ni.com/bundle/switch-executive/raw/resource/enus/managing-a-virtual-device-in-excel.html
- document_id: `switch-executive`
- page_type: `leaf`
- content_type: `concept`
- source_description: Switch Executive includes options in MAX and functions in the Configuration API to export and manage a virtual device in Microsoft Excel. You can use Excel to scale, customize, and streamline Switch Executive configuration management and perform any of the following tasks: Mass rename devices or cha

### Managing a Virtual Device in Excel

Switch Executive includes options in MAX and functions in the *Configuration API* to
 *export* and manage a virtual device in Microsoft Excel. You can use
 Excel to scale, customize, and streamline Switch Executive configuration
 *management* and perform any of the following tasks:

- Mass rename devices or channels
- Mass define routes
- Store non-configuration information (pinout and other system data) with Switch Executive
 configuration information in one file

When you have completed your management tasks in Excel, you can *import* the modified
 configuration to continue working with the virtual device in other
 environments/interfaces.

Parent topic:

Switch Executive Help

Related concepts:

- Using the Configuration API
- Exporting to Excel
- Performing Common Management Tasks
- Importing Excel Data

<!--NI_TOPIC bundle=switch-executive path=multiconnect-mode.html language=enus -->
## TOPIC 00085: Multiconnect Mode

- bundle_id: `switch-executive`
- source_path: `multiconnect-mode.html`
- source_url: https://docs-be.ni.com/bundle/switch-executive/raw/resource/enus/multiconnect-mode.html
- document_id: `switch-executive`
- page_type: `leaf`
- content_type: `concept`
- source_description: The typical state of a switch is either connected or disconnected. Physically, there is no way for a switch to be connected more than once—it is either connected or it is not. In certain situations, however, it is useful to think of a connection as something that can happen more than once.For exampl

### Multiconnect Mode

The typical state of a switch is either connected or disconnected. Physically, there is no way
 for a switch to be connected more than once—it is either connected or it is not. In
 certain situations, however, it is useful to think of a connection as something that can
 happen more than once.

For example, consider having two tests that can operate simultaneously. Although these tests
 primarily use different instruments and test points, they share a connection from a
 power supply to the UUT power input. Instead of having to manually handle this shared
 connection by some extra component, it is preferable to create the two tests
 independently such that they could be operated individually or simultaneously.
 Switch Executive facilitates this sort of sharing with multiconnection.

You can make a connection with no multiconnection or multiconnect
 routes.

If a route is connected with no multiconnection, the route must be disconnected before it can be
 reconnected. If you try to connect a route that was connected without multiconnection,
 an error condition occurs.

If a route is connected with multiconnect routes, the route can be connected multiple times. The
 first connection call performs a physical hardware connection. Successive calls merely
 increase a reference count on the connection. Similarly, disconnect calls decrease the
 reference count. When the reference count is at 0, the hardware is physically
 disconnected.

When you *add a route*, you can set the default multiconnect mode for the
 route—Multiconnect  Routes or
 No Multiconnect. If you do not set the default multiconnect
 mode, the mode defaults to Multiconnect Routes.

#### Sharing Route Legs

It is possible to share route legs as long as the routes share a common start or
 endpoint as shown in the following figure:

[IMAGE alt='image' src='GUID-1F426239-5BD3-44FB-9AF2-921C09155A07-a5.gif']

Switch Executive manages the legs internally, keeping the leg connected until it
 is no longer needed.

Parent topic:

Programming with Switch Executive

Related concepts:

- Adding Routes

<!--NI_TOPIC bundle=switch-executive path=nesting-a-route-group.html language=enus -->
## TOPIC 00086: Nesting a Route Group

- bundle_id: `switch-executive`
- source_path: `nesting-a-route-group.html`
- source_url: https://docs-be.ni.com/bundle/switch-executive/raw/resource/enus/nesting-a-route-group.html
- document_id: `switch-executive`
- page_type: `leaf`
- content_type: `concept`
- source_description: Complete the following steps to nest RouteGroup0 in RouteGroup1, where RouteGroup0 and RouteGroup1 are variables: Launch MAX with Switch Executive.Expand Devices and Interfaces»Switch Executive Virtual Devices. Select the Switch Executive virtual device to modify and navigate to the Schematic Config

### Nesting a Route Group

Complete the following steps to nest RouteGroup0 in
 RouteGroup1, where RouteGroup0 and
 RouteGroup1 are variables:

1. Launch MAX with Switch Executive.
2. Expand Devices and Interfaces»Switch Executive Virtual Devices .
3. Select the Switch Executive virtual device to modify and navigate to the Schematic
 Configuration tab.
4. Select RouteGroup0 in the Routes and Route Groups 
 listbox.
5. Drag and drop RouteGroup0 on RouteGroup1 . NI Switch Executive nests RouteGroup0 —the child route group—within RouteGroup1 —the parent route group—and displays the routes of both in the schematic of RouteGroup1 . Any edits that you make in the child route group are reflected in the parent route group.
6. Click on the
 Switch Executive taskbar to save the changes.

Parent topic:

Schematic Configuration

<!--NI_TOPIC bundle=switch-executive path=ni-switch-executive-and-ivi.html language=enus -->
## TOPIC 00087: Switch Executive and IVI

- bundle_id: `switch-executive`
- source_path: `ni-switch-executive-and-ivi.html`
- source_url: https://docs-be.ni.com/bundle/switch-executive/raw/resource/enus/ni-switch-executive-and-ivi.html
- document_id: `switch-executive`
- page_type: `leaf`
- content_type: `concept`
- source_description: Switch Executive is built on top of the IVI switch class driver and works with any IVI-compliant switch driver.The following figure represents the relationship between configuration utilities; application development environments (ADEs) such as LabVIEW, TestStand, LabWindows/CVI, or Visual Basic; Sw

### Switch Executive and IVI

Switch Executive is built on top of the IVI switch class driver and works with any IVI-compliant
 switch driver.

The following figure represents the relationship between configuration utilities; application
 development environments (ADEs) such as LabVIEW, TestStand, LabWindows/CVI, or Visual
 Basic; Switch Executive; the IVI switch-class driver; and IVI switch-compliant specific
 drivers such as NI-SWITCH:

[IMAGE alt='image' src='GUID-D34D58C9-FC76-4A2C-84CA-38D72478A6A6-a5.gif']

Parent topic:

Getting Started

<!--NI_TOPIC bundle=switch-executive path=ni-switch-executive-help.html language=enus -->
## TOPIC 00088: Switch Executive Help

- bundle_id: `switch-executive`
- source_path: `ni-switch-executive-help.html`
- source_url: https://docs-be.ni.com/bundle/switch-executive/raw/resource/enus/ni-switch-executive-help.html
- document_id: `switch-executive`
- page_type: `leaf`
- content_type: `concept`
- source_description: August 2015, 370404J-01 This help file contains development and programming support for Switch Executive. In addition to instructions for creating and configuring an Switch Executive virtual device, this help file contains getting started steps for programming your virtual device using LabVIEW, LabW

### Switch Executive Help

August 2015, 370404J-01

This help file contains development and programming support for Switch Executive. In addition to
 instructions for creating and configuring an Switch Executive virtual device, this help
 file contains *getting started steps* for programming your virtual device
 using LabVIEW, LabWindows™/CVI™, TestStand™, and Microsoft Visual Basic and includes
 *LabVIEW*, *C*, *TestStand*, and *Visual
 Basic* programming references.

Related concepts:

- Programming Flow
- Using Switch Executive in NI TestStand

<!--NI_TOPIC bundle=switch-executive path=opening-a-session.html language=enus -->
## TOPIC 00089: Opening a Session

- bundle_id: `switch-executive`
- source_path: `opening-a-session.html`
- source_url: https://docs-be.ni.com/bundle/switch-executive/raw/resource/enus/opening-a-session.html
- document_id: `switch-executive`
- page_type: `leaf`
- content_type: `concept`
- source_description: Open a session to communicate with an Switch Executive virtual device. This is similar to opening a file before reading/writing to it. To open a session, use the niSE Open Session VI or the niSE_OpenSession function.

### Opening a Session

Open a session to communicate with an Switch Executive virtual device. This is similar to opening
 a file before reading/writing to it.

To open a session, use the *niSE Open Session* VI or the
 *niSE_OpenSession* function.

Parent topic:

Programming Flow

<!--NI_TOPIC bundle=switch-executive path=overview.html language=enus -->
## TOPIC 00090: Switch Executive Overview

- bundle_id: `switch-executive`
- source_path: `overview.html`
- source_url: https://docs-be.ni.com/bundle/switch-executive/raw/resource/enus/overview.html
- document_id: `switch-executive`
- page_type: `leaf`
- content_type: `concept`
- source_description: Switch Executive is switch management and routing application software that accelerates development and simplifies the maintenance of switch systems. Switch Executive provides interactive configuration and automatic routing capabilities that make it easier to design a switch system. You can simplify

### Switch Executive
 Overview

Switch Executive is switch management and routing application software that
 accelerates development and simplifies the maintenance of switch systems.

Switch Executive provides interactive configuration and automatic routing capabilities
 that make it easier to design a switch system. You can simplify your system’s
 documentation for future modifications by assigning aliases to switch modules, external
 connections, and signal routes. Test code developed with Switch Executive can be reused
 in LabVIEW, LabWindows™/CVI, Measurement Studio, and TestStand. You can choose from a
 development license, a deployment license for distributing developing code, or a
 debug/deploy license, which you can use to resolve issues on applications that were
 created with a development license.

<!--NI_TOPIC bundle=switch-executive path=performing-common-management-tasks.html language=enus -->
## TOPIC 00091: Performing Common Management Tasks

- bundle_id: `switch-executive`
- source_path: `performing-common-management-tasks.html`
- source_url: https://docs-be.ni.com/bundle/switch-executive/raw/resource/enus/performing-common-management-tasks.html
- document_id: `switch-executive`
- page_type: `leaf`
- content_type: `concept`
- source_description: You can modify Switch Executive data in Excel to create custom configurations. To modify data in Excel without affecting the ability to import the file, always populate required columns and format the data appropriately.Refer to the following management task cases for instructions about how to custo

### Performing Common Management Tasks

You can modify Switch Executive data in Excel to create custom configurations. To modify data in
 Excel without affecting the ability to import the file, always populate required columns
 and *format* the data appropriately.

Note

- Mass Renaming Channel Aliases
- Mass Creating Routes
- Editing an IVI Device Name
- Changing an IVI Device Topology
- Merging Two Virtual Devices

#### Mass Renaming Channel Aliases

Complete the following steps to mass rename channel aliases:

1. Click the Channels sheet tab at the bottom of the screen
 to display the Channels worksheet.
2. Populate the Alias column with aliases for each Channel
 IVI Device/Channel IVI Name you want to alias.
3. Save the edits.

#### Mass Creating Routes

Complete the following steps to mass create routes:

1. Click the Routes sheet tab at the bottom of the screen to
 display the Routes worksheet.
2. Insert a row for each route you want to create, and populate the required
 attributes (columns): Refer to *Formatting Configuration Data: Routes* for detailed
 information about formatting Route attributes (columns).
  - Route Name
  - Either both Endpoint1 and Endpoint2, or Specification, or all three
  - Type
  - Multiconnect Mode
3. (Optional) Populate other attributes (columns).
4. Save the edits.

#### Editing an IVI Device Name

#### Globally Editing Device References

Complete the following steps to globally edit device references:

1. Open a search and replace for the entire workbook.
2. Specify the existing IVI device name as the search string and the replacing IVI
 device name as the replace string. Excel edits every device reference in the
 workbook.
3. Save the edits.

#### Individually Editing Device
 References

Complete the following steps to individually edit device references:

1. Open a search.
2. Specify the existing IVI device name as the search string. Excel finds an
 instance of the IVI Device Name in the workbook.
3. Edit the device reference.
4. Repeat steps 2 and 3 until you have edited every device reference in the
 workbook.
5. Save the edits.

Note

#### Changing an IVI Device
 Topology

Complete the following steps to change an IVI device topology:

1. Add new channels.
  1. Click the Channels sheet tab at the bottom of the
 screen to display the Channels worksheet.
  2. Insert a row for each channel you want to create and populate the
 required attributes (columns): Refer to Formatting Configuration Data: Channels for
 detailed information about formatting Channel attributes (columns).
    - Channel IVI Device
    - Channel IVI Name
  3. (Optional) Populate other attributes (columns).
2. Replace existing channel references with new channel references using one of the
 following methods: Note Channel
 references display in the Channel IVI Name, Channel, Set1 Channel, Set2
 Channel, Base Channel, End Channel, Endpoint1, Endpoint2, and Specification
 columns of the Channels, Mutual Exclusion Channels, Set Exclusion Set1
 Channels, Set Exclusion Set2 Channels, Bus Channels, and Routes
 worksheets.
  - Globally editing channel references —Complete the
 following steps to globally edit channel references:
    1. Open a search and replace for the entire workbook.
    2. Specify the existing IVI Channel name as the search string and
 the replacing IVI Channel name as the replace string. Excel
 edits every channel reference in the workbook.
    3. Save the edits.
  - Individually editing channel references —Complete
 the following steps to individually edit channel references:
    1. Open a search.
    2. Specify the existing IVI Channel name as the search string.
 Excel finds an instance of the IVI Channel Name in the
 workbook.
    3. Edit the channel reference.
    4. Repeat steps b and c until you have edited every device
 reference in the workbook.
    5. Save the edits.
3. Delete unused channels and channel references.
  1. Click the Channels sheet tab at the bottom of the
 screen to display the Channels worksheet.
  2. Delete the row for any IVI channel that does not exist on the new
 topology.
  3. Delete any rows in other worksheets that contain unused channel
 references.
4. Save the edits. Note Ensure that the topology in the IVI Configuration in MAX is updated to
 match the new topology.

#### Merging Two Virtual Devices

Complete the following steps to create one virtual device from two:

1. Merge the virtual devices.
  1. Open the workbooks for both Virtual Device1 and Virtual Device2.
  2. Click a worksheet tab at the bottom of the screen in Virtual
 Device2.
  3. Copy the rows of entire worksheet (excluding column headers).
  4. Insert the copied rows into the same worksheet in the Virtual Device1
 workbook. Virtual Device1 now contains the rows of both Virtual Device1
 and Virtual Device2.
  5. Repeat steps b through d for each worksheet (excluding the Virtual
 Device worksheet) in Virtual Device2.
  6. Close the Virtual Device2 workbook. Virtual Device1 contains the merged
 virtual device data.
2. Delete any redundant rows (IVI devices) on the IVI Devices worksheet.
3. Resolve any reference conflicts. Note References display in the
 Alias, Hardwire, Exclusion Name, Channel, Set1Channel, Set2 Channel,
 Hardwire Name, Bus Name, Base Channel, End Channel, Route Name, Endpoint1,
 Endpoint2, Specification, Route Group Name, Child columns of the workbook.
  1. Excluding the Virtual Device and IVI Devices worksheets, verify that all
 references are unique in the following columns of the workbook:
    - Alias
    - Exclusion Name
    - Hardwire Name
    - Bus Name
    - Route Name
    - Route Group Name
  2. If necessary, replace non-unique references in the workbook.
4. Save the edits.

Parent topic:

Managing a Virtual Device in Excel

Related concepts:

- Formatting Configuration Data
- Formatting Configuration Data: Routes
- Formatting Configuration Data: Channels

<!--NI_TOPIC bundle=switch-executive path=programming-flow.html language=enus -->
## TOPIC 00092: Programming Flow

- bundle_id: `switch-executive`
- source_path: `programming-flow.html`
- source_url: https://docs-be.ni.com/bundle/switch-executive/raw/resource/enus/programming-flow.html
- document_id: `switch-executive`
- page_type: `leaf`
- content_type: `concept`
- source_description: Complete the following steps to program an Switch Executive virtual device: Open a session. Control the virtual device. (Optional) Handle Errors. Close the session. The following figure represents the programming flow of Switch Executive:

### Programming Flow

Complete the following steps to program an Switch Executive virtual device:

1. Open a session.
2. Control the virtual device.
3. (Optional) Handle Errors .
4. Close the session.

The following figure represents the programming flow of Switch Executive:

[IMAGE alt='image' src='GUID-F23BEF46-E494-4CF9-AD64-03699CF5D9D9-a5.gif']

Parent topic:

Programming with Switch Executive

Related concepts:

- Opening a Session
- Controlling the Virtual Device
- Error Handling
- Closing a Session

<!--NI_TOPIC bundle=switch-executive path=programming-with-ni-switch-executive.html language=enus -->
## TOPIC 00093: Programming with Switch Executive

- bundle_id: `switch-executive`
- source_path: `programming-with-ni-switch-executive.html`
- source_url: https://docs-be.ni.com/bundle/switch-executive/raw/resource/enus/programming-with-ni-switch-executive.html
- document_id: `switch-executive`
- page_type: `leaf`
- content_type: `concept`
- source_description: Switch Executive provides full programmatic control of your virtual device using an application development environment (ADE). Refer to Getting Started to begin using your virtual device in LabVIEW, TestStand, LabWindows/CVI, or Visual Basic.

### Programming with Switch Executive

Switch Executive provides full programmatic control of your virtual device using an application
 development environment (ADE). Refer to *Getting Started* to begin using your
 virtual device in LabVIEW, TestStand, LabWindows/CVI, or Visual Basic.

Parent topic:

Switch Executive Help

Related concepts:

- Getting Started

<!--NI_TOPIC bundle=switch-executive path=programming.html language=enus -->
## TOPIC 00094: Programming

- bundle_id: `switch-executive`
- source_path: `programming.html`
- source_url: https://docs-be.ni.com/bundle/switch-executive/raw/resource/enus/programming.html
- document_id: `switch-executive`
- page_type: `leaf`
- content_type: `concept`
- source_description: Program a virtual device using an application development environment (ADE) such as LabVIEW, TestStand, LabWindows/CVI, or Visual Basic. Because an ADE recognizes a virtual device as a single instrument, programming time is significantly reduced.

### Programming

Program a virtual device using an application development environment (ADE) such as LabVIEW,
 TestStand, LabWindows/CVI, or Visual Basic. Because an ADE
 recognizes a virtual device as a single instrument, programming
 time is significantly reduced.

Parent topic:

Concepts

Related concepts:

- Programming with Switch Executive

<!--NI_TOPIC bundle=switch-executive path=removing-ivi-switches.html language=enus -->
## TOPIC 00095: Removing IVI Switches

- bundle_id: `switch-executive`
- source_path: `removing-ivi-switches.html`
- source_url: https://docs-be.ni.com/bundle/switch-executive/raw/resource/enus/removing-ivi-switches.html
- document_id: `switch-executive`
- page_type: `leaf`
- content_type: `concept`
- source_description: Complete the following steps to remove an IVI switch from an existing Switch Executive virtual device: Launch MAX with Switch Executive.Expand Devices and Interfaces»Switch Executive Virtual Devices. Expand the Switch Executive virtual device containing the IVI switch you want to remove. Right-click

### Removing IVI Switches

Complete the following steps to remove an IVI switch from an existing Switch Executive virtual
 device:

1. Launch MAX with Switch Executive.
2. Expand Devices and Interfaces»Switch Executive Virtual Devices .
3. Expand the Switch Executive virtual device containing the IVI switch you want to remove.
4. Right-click the IVI switch to remove and select Remove IVI Switch . A
 dialog box opens to confirm the removal of the IVI switch. Note When you remove an IVI switch,
 its channels are also removed from your configuration. This removal may break
 some of your routes.
5. Click Yes to remove the IVI switch or No to
 abort.

Parent topic:

Configuring IVI Switches

<!--NI_TOPIC bundle=switch-executive path=report-generation.html language=enus -->
## TOPIC 00096: Report Generation

- bundle_id: `switch-executive`
- source_path: `report-generation.html`
- source_url: https://docs-be.ni.com/bundle/switch-executive/raw/resource/enus/report-generation.html
- document_id: `switch-executive`
- page_type: `leaf`
- content_type: `concept`
- source_description: Generate a detailed report that includes the definitions and configurations of the IVI switch modules, channels, hardwires, buses, exclusions, routes, and route groups that compose a virtual device.

### Report Generation

Generate a detailed report that includes the definitions and configurations of the IVI switch
 modules, channels, hardwires, buses, exclusions, routes, and route groups that compose a
 virtual device.

Parent topic:

Concepts

Related concepts:

- Generating a Report
- Using the Configuration API

<!--NI_TOPIC bundle=switch-executive path=reserved-for-routing.html language=enus -->
## TOPIC 00097: Reserved for Routing

- bundle_id: `switch-executive`
- source_path: `reserved-for-routing.html`
- source_url: https://docs-be.ni.com/bundle/switch-executive/raw/resource/enus/reserved-for-routing.html
- document_id: `switch-executive`
- page_type: `leaf`
- content_type: `concept`
- source_description: Switch Executive uses channels that are reserved for routing to complete routes within a switch.For example, in the following matrix, you want to connect C0 to C2. Depending on the route configurations, you can mark R0, R1, or R2 as reserved for routing to complete the route path. Channels that are

### Reserved for Routing

Switch Executive uses channels that are *reserved for routing* to complete routes
 within a switch.

For example, in the following matrix, you want to connect C0 to C2. Depending on the route
 configurations, you can mark R0, R1, or R2 as reserved for routing to complete the route
 path. Channels that are reserved for routing cannot be used as endpoints for new
 routes.

[IMAGE alt='image' src='GUID-D105B21F-F636-4FB2-A32B-9E09317445BA-a5.gif']

Note

configuration channels

[IMAGE alt='image' src='GUID-C2989B06-A528-4BB9-A3E0-6FB3BBA64155-a5.gif']

Note

route specification string

Note

- In a route, endpoint channels cannot be marked as reserved for routing.
- IVI has a similar concept for configuration channels. Whereas
 Switch Executive honors any configuration channels that are set up as part
 of the IVI configuration, these configuration channels do not have the same
 flexibility as an Switch Executive channel marked as reserved for routing.
 Specific restrictions placed on route specification strings
 exist for IVI configuration channels.

When configuring routes, if Switch Executive cannot find a potential path between channels, you
 may be recommended to mark certain channels as reserved for routing to complete the
 route. Choose different channels to use when completing a route by doing one of the
 following:

- Editing the channel name in the device box or the route string to choose a channel explicitly
- Changing the hardwire selector on a route to choose a channel implicitly

Note

Parent topic:

Channel

Related concepts:

- Route Specification Strings
- Hardwires and Reserved for Routing Channels

<!--NI_TOPIC bundle=switch-executive path=route-group.html language=enus -->
## TOPIC 00098: Route Group

- bundle_id: `switch-executive`
- source_path: `route-group.html`
- source_url: https://docs-be.ni.com/bundle/switch-executive/raw/resource/enus/route-group.html
- document_id: `switch-executive`
- page_type: `leaf`
- content_type: `concept`
- source_description: A route group is a group of individual routes and/or other route groups associated with a single alias name. Use route groups to set up simultaneous switching configurations quickly. Route groups also enable Switch Executive to make better decisions about which resources to use when creating a route

### Route Group

A *route group* is a group of individual routes and/or other route groups associated
 with a single alias name. Use route groups to set up simultaneous switching configurations
 quickly. Route groups also enable Switch Executive to make better decisions about which
 resources to use when creating a route. When two or more routes are added to a
 route group, Switch Executive ensures these routes do not use conflicting
 resources.

For example, the route group named RouteGroup1, shown in the following figure,
 consists of routes Route1, Route2, and Route3.
 The route group named RouteGroup2 consists of routes Route4,
 Route5, and the route group RouteGroup1. When
 Connect calls RouteGroup1, all routes within that route group
 are activated.

[IMAGE alt='image' src='GUID-156CD42C-5D60-49A6-99C4-730426EEFD67-a5.gif']

In a single test step, multiple switch routes may need to be connected. By grouping those routes,
 a single call to the *niSE Connect* VI or the
 *niSE_Connect* function can connect everything needed for the test
 step without having to connect each route separately.

specification string

Note

reserved

Parent topic:

Fundamentals

Related concepts:

- Route Specification Strings
- Schematic Configuration
- Extended Configuration
- Using the Configuration API

Related information:

- Naming Conventions

<!--NI_TOPIC bundle=switch-executive path=route-specification-strings.html language=enus -->
## TOPIC 00099: Route Specification Strings

- bundle_id: `switch-executive`
- source_path: `route-specification-strings.html`
- source_url: https://docs-be.ni.com/bundle/switch-executive/raw/resource/enus/route-specification-strings.html
- document_id: `switch-executive`
- page_type: `leaf`
- content_type: `concept`
- source_description: Route specification strings are the paths connecting two channels and are composed of one or more routes delimited by ampersands (&). For example, in the following line of syntax, there are three defined routes or route groups:routeOrGroup & routeOrGroup & routeOrGroup . . . where routeOrGroup can b

### Route Specification Strings

Route specification strings are the paths connecting two channels and are composed of one or more
 routes delimited by ampersands (&). For example, in the following line of
 syntax, there are three defined routes or route groups:

routeOrGroup & routeOrGroup & routeOrGroup . . .

where routeOrGroup can be the following:

- Route name
- Route group name
- Two endpoint channels to be connected that are delimited by -> . NI Switch Executive dynamically determines the path between the endpoints. In this mode, a hardwire alias name can
be substituted for the endpoints. 
 channel -> channel
- Fully specified path enclosed in square brackets consisting of one or more endpoint channels
 delimited by -> : [channel -> channel ->
 channel...] where channel can be the following:
  - A channel alias name
  - A unique name created by combining the IVI device logical name and IVI channel name
 separated by a forward slash ( / ) delimiter, such as
 device/iviChan .

Tip

->

Note

- Any channel , other than an endpoint, within a route specification
 string must be reserved for routing or directly hardwired to one of the endpoint
 channels.
- channels used as endpoints must not be reserved for routing
 channels.
- When connecting a route, the list of channels must obey the exclusion rules both
 explicitly in the route specification string as well as implicitly by any previous
 connections. Exclusion violations result in an error.

The following are samples of route specification strings for a matrix:

| Route Specification String Examples | Description |
| --- | --- |
| A->B | Connect channel A to channel B. NI Switch Executive automatically determines the path between the two channels. |
| [SampleMatrix1/c0->SampleMatrix1/r1->SampleMatrix1/c4] | A fully specified path between column 0 and column 4 of SampleMatrix1. Row 1 must be marked as reserved for routing. |
| [Scope->R3->SampleMatrix1/c6] | A fully specified path between the channel named Scope and column 6 of SampleMatrix1. Row 3 must be marked as reserved for routing. |
| Scope->SampleMatrix1/c6 | Connect the channel named Scope to column 6 of SampleMatrix1. NI Switch Executive automatically determines the path between the two channels. |
| ArbToInput & ScopeToOutput | Complete the connections for route group ArbToInput and ScopeToOutput. |
| PowerDevice & [Scope->R3->UUT_Out] | Complete the connections for route group PowerDevice and complete the fully specified path between the channel named Scope and the channel named UUT_Out. R3 must be marked as a reserved for routing. |

Each supported ADE has an associated Route Specification String Example. Refer
 to the *Examples* for the appropriate ADE to see how route specification strings
 are used when programming.

Parent topic:

Programming with Switch Executive

Related concepts:

- Examples

<!--NI_TOPIC bundle=switch-executive path=route.html language=enus -->
## TOPIC 00100: Route

- bundle_id: `switch-executive`
- source_path: `route.html`
- source_url: https://docs-be.ni.com/bundle/switch-executive/raw/resource/enus/route.html
- document_id: `switch-executive`
- page_type: `leaf`
- content_type: `concept`
- source_description: A route is a connection from one channel (row, column, COM, NO, and so on) to another. Routes are the primary building blocks of any Switch Executive virtual device. Some characters are reserved and cannot be used in route names.

### Route

route

Note

reserved

Parent topic:

Fundamentals

Related concepts:

- Schematic Configuration
- Extended Configuration
- Using the Configuration API

Related information:

- Naming Conventions

<!--NI_TOPIC bundle=switch-executive path=routes-groups-tab.html language=enus -->
## TOPIC 00101: Routes/Groups Tab

- bundle_id: `switch-executive`
- source_path: `routes-groups-tab.html`
- source_url: https://docs-be.ni.com/bundle/switch-executive/raw/resource/enus/routes-groups-tab.html
- document_id: `switch-executive`
- page_type: `leaf`
- content_type: `concept`
- source_description: Use the Routes/Groups tab to configure routes and route groups in Switch Executive.

### Routes/Groups Tab

Use the Routes/Groups tab to configure routes and route groups in Switch
 Executive.

[IMAGE alt='image' src='GUID-2FE95F27-9A30-4249-BE27-FD01546FE71C-a5.png']

Parent topic:

Extended Configuration

<!--NI_TOPIC bundle=switch-executive path=schematic-configuration.html language=enus -->
## TOPIC 00102: Schematic Configuration

- bundle_id: `switch-executive`
- source_path: `schematic-configuration.html`
- source_url: https://docs-be.ni.com/bundle/switch-executive/raw/resource/enus/schematic-configuration.html
- document_id: `switch-executive`
- page_type: `leaf`
- content_type: `concept`
- source_description: In the Schematic Configuration tab, Switch Executive renders a schematic, or a graphical representation, of each switch in a virtual device. Click the device schematic to quickly configure a virtual device, including channel aliases and hardwires. Switch Executive represents third-party, IVI-complia

### Schematic Configuration

Schematic Configuration

Note

third-party

independent topologies

Schematic
 Configuration

The Routes and Route Groups and Devices listboxes
 and the Schematic window compose the Schematic
 Configuration tab. In the following figure, a matrix topology schematic
 displays in the Schematic window:

[IMAGE alt='image' src='GUID-E2DDB4EE-569F-4900-9E24-019ACECD0367-a5.png']

#### Routes and Route Groups

The Routes and Route Groups listbox contains all the route
 groups associated with a virtual device.

Note

RouteGroup0

Routes and Route
 Groups

Use the
 buttons at the top of the Routes and Route Groups listbox to
 manage route groups and routes.

| Button | Function |
| --- | --- |
|  | Adds a route group to the virtual device and the Routes and Route Groups listbox. When routes are added to the route group, the new route group displays in the Schematic window. |
|  | Adds a route to the virtual device and the Routes and Route Groups listbox. This button is disabled when the Show Routes checkbox is disabled. |
|  | Creates a copy of the route group and adds it to the virtual device and the Routes and Route Groups listbox. The copy of the route group displays in the Schematic window. When the Show Routes checkbox is enabled, this button can copy routes in addition to route groups. |
|  | Deletes the route group from the virtual device and the Routes and Route Groups listbox. The route group no longer displays in the Schematic window. When deleting a nested route group, this button disassociates the child route group from the parent route group. When the Show Routes checkbox is enabled, this button can delete routes in addition to route groups. |

Tip

Routes and Route Groups

#### Show Routes

Enable the Show Routes checkbox, located below the
 Routes and Route Groups listbox, to manage the individual
 routes of a route group. When you enable the Show Routes
 checkbox, the create route button is enabled, and you can use the copy button to
 copy a route.

#### Filter

Use the filter textbox, located directly below the Routes and Route
 Groups listbox, for searching. Type the first characters of a route
 or route group name, and all names that match the search string display in the
 Routes and Route Groups listbox. The search string is not
 case sensitive.

#### Devices

The Devices listbox contains all the IVI switches associated
 with a virtual device. Click a switch device to display the channels, routes, route
 groups, and hardwires associated with the switch in the
 Schematic window.

A checkmark displays to the left
 of the device name in the Devices listbox to indicate that a
 route exists on the device.

#### Schematic

The Schematic window is a graphical representation of all the
 channels, routes, and hardwires of a route group on a particular switch device
 associated with a virtual device.

When you associate a channel with a
 hardwire, the hardwire number appends as a superscript to the channel name in the
 schematic.

A route displays in color on the schematic to represent its
 electrical connectivity. If an electrical path is shared between two or more routes,
 the routes display in the same color on the schematic.

Note

Schematic
 Configuration

Parent topic:

Configuring a Virtual Device

Related concepts:

- Third-Party Switches
- Independent Topologies

<!--NI_TOPIC bundle=switch-executive path=session-reference-counting.html language=enus -->
## TOPIC 00103: Session Reference Counting

- bundle_id: `switch-executive`
- source_path: `session-reference-counting.html`
- source_url: https://docs-be.ni.com/bundle/switch-executive/raw/resource/enus/session-reference-counting.html
- document_id: `switch-executive`
- page_type: `leaf`
- content_type: `concept`
- source_description: Switch Executive uses a reference counting scheme to manage open session handles to an Switch Executive virtual device. Each call to the niSE Open Session VI or the niSE_OpenSession function must be matched with a subsequent call to the niSE Close Session VI or the niSE_CloseSession function.Multipl

### Session Reference Counting

Switch Executive uses a reference counting scheme to manage open session handles to an Switch
 Executive virtual device. Each call to the *niSE Open Session* VI or the
 *niSE_OpenSession* function must be matched with a
 subsequent call to the *niSE Close Session* VI or the
 *niSE_CloseSession* function.

niSE_OpenSession

Note

niSE_CloseSession

niSE_CloseSession

Tip

niSE_CloseSession

niSE
 Disconnect All

niSE_DisconnectAll

niSE_OpenSession

Parent topic:

Programming with Switch Executive

<!--NI_TOPIC bundle=switch-executive path=setting-configuration-options.html language=enus -->
## TOPIC 00104: Setting Configuration Options

- bundle_id: `switch-executive`
- source_path: `setting-configuration-options.html`
- source_url: https://docs-be.ni.com/bundle/switch-executive/raw/resource/enus/setting-configuration-options.html
- document_id: `switch-executive`
- page_type: `leaf`
- content_type: `concept`
- source_description: When selecting channel paths, the list of available channels can become cumbersome in large systems. To reduce clutter, a number of configuration options are available.Complete the following steps to configure options in Switch Executive: Launch MAX with Switch Executive.Expand Devices and Interface

### Setting Configuration Options

When selecting channel paths, the list of available channels can become cumbersome in large
 systems. To reduce clutter, a number of configuration options are available.

Complete the following steps to configure options in Switch Executive:

1. Launch MAX with Switch Executive.
2. Expand Devices and Interfaces»Switch Executive Virtual Devices .
3. Right-click the virtual device you want to configure and select Options ,
 or click on
 the Switch Executive taskbar and select . The
 Configuration Options dialog box opens.
4. Click the General tab.
  1. Configure the channel name display. The following table lists the available options: Option
 DescriptionDisplay full name only
 Switch Executive lists the full name of the channel. For example,
 SampleMatrix1/ab0.
 Display alias or full name (default)
 If the channel has an alias, the alias is listed. If no alias is
 designated for the channel, the full name is listed.
 Display alias and full name
 Switch Executive lists the alias and the full name of the
 channel.
  2. Configure the visual route editor selections. The following table lists the available options: Option
 DescriptionHide channels without aliases
 Switch Executive only lists channels with aliases. NI Switch Executive
 disables this option by default.
 Defer updates on configuration changes
 Switch Executive defers verification and rerouting when configuration
 changes are made (changes to names, reserved for routing channels, and so on).
 In systems with a large number of routes, this verification and rerouting
 process can be time consuming. To speed up this operation, you can defer this
 process and *validate* your configuration at a later time. To
 reroute any broken routes, select the broken routes and click
 Retry. Switch Executive disables this option by
 default.
 Routing search depth
 Switch Executive chooses the depth by which the routing algorithm
 searches for paths to recommend changes to reserved for routing channels. You
 can select Low (default),
 Medium, or High.
5. Click the Schematic tab and select Disable delete notification dialog to turn off delete notifications in the Schematic Configuration tab.
6. Click OK .
7. Click on the
 Switch Executive taskbar to save the changes.

Parent topic:

Configuring a Virtual Device

Related concepts:

- Validating a Virtual Device

<!--NI_TOPIC bundle=switch-executive path=setting-properties-and-attributes-before-read.html language=enus -->
## TOPIC 00105: Setting Properties and Attributes Before Reading Them

- bundle_id: `switch-executive`
- source_path: `setting-properties-and-attributes-before-read.html`
- source_url: https://docs-be.ni.com/bundle/switch-executive/raw/resource/enus/setting-properties-and-attributes-before-read.html
- document_id: `switch-executive`
- page_type: `leaf`
- content_type: `concept`
- source_description: Properties and attributes are modified when you set them or when you call a configuration VI or function that sets them, respectively. It is important to set the properties or attributes or call any configuration VIs or functions before reading back any property or attribute values for the following

### Setting Properties and Attributes Before Reading Them

Properties and attributes are modified when you set them or when you call a configuration VI or
 function that sets them, respectively. It is important to set the properties or
 attributes or call any configuration VIs or functions before reading back any property
 or attribute values for the following reasons:

- Values read are coerced depending on the current configuration of the session. If you read a property or attribute value and then set other properties or attributes, the value read may no longer be valid.
- The driver verifies that the configuration of the device is valid at the time the property or attribute is read. It is possible to get an error when reading a property or attribute if the configuration is not valid at that point, even when a setting later could make it valid.
- Reading properties or attributes causes the driver to verify the current configuration. If you change some of the settings later, those settings need to be validated again.

Note

Parent topic:

Programming with Switch Executive

<!--NI_TOPIC bundle=switch-executive path=sharing-a-route-between-route-groups.html language=enus -->
## TOPIC 00106: Sharing a Route Between Route Groups

- bundle_id: `switch-executive`
- source_path: `sharing-a-route-between-route-groups.html`
- source_url: https://docs-be.ni.com/bundle/switch-executive/raw/resource/enus/sharing-a-route-between-route-groups.html
- document_id: `switch-executive`
- page_type: `leaf`
- content_type: `concept`
- source_description: Complete the following steps to share a route, routeA, between two route groups, RouteGroup0 and RouteGroup1—where routeA, RouteGroup0, and RouteGroup1 are variables: Launch MAX with Switch Executive. Expand Devices and Interfaces»Switch Executive Virtual Devices. Select the Switch Executive virtual

### Sharing a Route Between Route Groups

Complete the following steps to share a route, routeA, between two route groups,
 RouteGroup0 and RouteGroup1—where
 routeA, RouteGroup0, and
 RouteGroup1 are variables:

1. Launch MAX with Switch Executive.
2. Expand Devices and Interfaces»Switch Executive Virtual Devices .
3. Select the Switch Executive virtual device to modify and navigate to the Schematic
 Configuration tab.
4. Enable the Show Routes checkbox under the Routes and Route
 Groups listbox. Switch Executive displays all the routes of the
 virtual device, associated in route groups or not, in the Routes and
 Route Groups listbox.
5. Click routeA in the Routes and Route Groups listbox.
6. Drag routeA and drop it on RouteGroup0 .
7. Click routeA in the Routes and Route Groups listbox.
8. Drag routeA and drop it on RouteGroup1 . routeA is now shared between RouteGroup0 and RouteGroup1 .
9. Click on the
 Switch Executive taskbar to save the changes.

Parent topic:

Schematic Configuration

<!--NI_TOPIC bundle=switch-executive path=sorting-filtering-commenting.html language=enus -->
## TOPIC 00107: Sorting, Filtering, & Commenting

- bundle_id: `switch-executive`
- source_path: `sorting-filtering-commenting.html`
- source_url: https://docs-be.ni.com/bundle/switch-executive/raw/resource/enus/sorting-filtering-commenting.html
- document_id: `switch-executive`
- page_type: `leaf`
- content_type: `concept`
- source_description: You can sort, filter, and add comments to a particular element of an Switch Executive virtual device in the extended configuration tabs.Sorting Click the heading of a column in the listbox of any object to sort the list alphanumerically. Filtering Use the textboxes below every column under an object

### Sorting, Filtering, & Commenting

You can sort, filter, and add comments to a particular element of an Switch Executive virtual
 device in the *extended configuration* tabs.

#### Sorting

Click the heading of a column in the listbox of any object to sort the list alphanumerically.

#### Filtering

Use the textboxes below every column under an object's listbox to filter the contents of that
 column. For example, if you type C in the filtering textbox, Switch Executive
 filters out every item in the list that does not begin with a C. Entering C1
 filters out every item that does not begin with C1, and so on. You can use multiple filters in a
 textbox by typing commas. For example, entering R,C filters all items that
 begin with R or C. Filtering is not case sensitive.

#### Comments

Use the Comment textboxes to document the virtual device. Choose the item to comment, and type your comments.

Parent topic:

Extended Configuration

Related concepts:

- Extended Configuration

<!--NI_TOPIC bundle=switch-executive path=specification-type.html language=enus -->
## TOPIC 00108: Specification Type

- bundle_id: `switch-executive`
- source_path: `specification-type.html`
- source_url: https://docs-be.ni.com/bundle/switch-executive/raw/resource/enus/specification-type.html
- document_id: `switch-executive`
- page_type: `leaf`
- content_type: `concept`
- source_description: Specification type is the connection method the routing engine uses to determine a route.On the Routes/Groups tab, select from the following connection methods: Specified By Full Path—The routing engine uses the fully specified path to determine the route. Find By Endpoints—The routing engine uses e

### Specification Type

Specification type is the connection method the routing engine uses to determine a route.

On the Routes/Groups tab, select from the following connection
 methods:

- Specified By Full Path —The routing engine uses the fully specified path
 to determine the route.
- Find By Endpoints —The routing engine uses endpoints to determine the
 route.
- Find If Full Path Fails —If the full path fails to connect, the routing
 engine uses endpoints to determine the route.

Parent topic:

Programming with Switch Executive

<!--NI_TOPIC bundle=switch-executive path=tab-delimited-text-files.html language=enus -->
## TOPIC 00109: Tab-Delimited Text Files

- bundle_id: `switch-executive`
- source_path: `tab-delimited-text-files.html`
- source_url: https://docs-be.ni.com/bundle/switch-executive/raw/resource/enus/tab-delimited-text-files.html
- document_id: `switch-executive`
- page_type: `leaf`
- content_type: `concept`
- source_description: When you export to a tab-delimited (.txt) file, Switch Executive saves the configuration data of a virtual device in a single Excel-compatible file. When you open a tab-delimited file in Excel, Switch Executive objects, organized by object type, are separated by an empty row. The first row immediate

### Tab-Delimited Text Files

.txt

Note

Formatting Configuration
 Data

Parent topic:

Exporting to Excel

Related concepts:

- Formatting Configuration Data

<!--NI_TOPIC bundle=switch-executive path=third-party-switches.html language=enus -->
## TOPIC 00110: Third-Party Switches

- bundle_id: `switch-executive`
- source_path: `third-party-switches.html`
- source_url: https://docs-be.ni.com/bundle/switch-executive/raw/resource/enus/third-party-switches.html
- document_id: `switch-executive`
- page_type: `leaf`
- content_type: `concept`
- source_description: In addition to switch modules, Switch Executive virtual devices support IVI-compliant, third-party switches. Because third-party switches do not contain the information required to draw a schematic, Switch Executive displays the schematic as three listboxes: Channel 1, Channel 2, and Connections.Swi

### Third-Party Switches

In addition to switch modules, Switch Executive virtual devices support IVI-compliant,
 *third-party* switches. Because third-party switches do not contain the
 information required to draw a schematic, Switch Executive displays the schematic as
 three listboxes: Channel 1, Channel 2, and Connections.

Switch Executive also displays schematic listboxes for switches that use an independent topology.
 Refer to *Independent Topologies* for instructions about how to configure a
 third-party switch using the Schematic Configuration tab.

Parent topic:

Schematic Configuration

Related concepts:

- Using Third-Party Switches
- Independent Topologies

<!--NI_TOPIC bundle=switch-executive path=user-manual-welcome.html language=enus -->
## TOPIC 00111: Switch Executive User Manual

- bundle_id: `switch-executive`
- source_path: `user-manual-welcome.html`
- source_url: https://docs-be.ni.com/bundle/switch-executive/raw/resource/enus/user-manual-welcome.html
- document_id: `switch-executive`
- page_type: `leaf`
- content_type: `concept`
- source_description: The Switch Executive User Manual provides detailed descriptions of the product functionality and the step by step processes for use. Looking for Something Else?For information not found in the User Manual for your product, such as specifications and API reference, browse Related Information.

### Switch Executive
 User Manual

The Switch Executive User Manual provides detailed
 descriptions of the product functionality and the step by step processes for use.

#### Looking for Something Else?

For information not found in the User Manual
 for your product, such as specifications and API reference, browse *Related
 Information*.

Related information:

- Hardware and Software Operating System
 Compatibility
- License Setup and Activation

<!--NI_TOPIC bundle=switch-executive path=using-ni-switch-executive-in-labview.html language=enus -->
## TOPIC 00112: Using Switch Executive in LabVIEW

- bundle_id: `switch-executive`
- source_path: `using-ni-switch-executive-in-labview.html`
- source_url: https://docs-be.ni.com/bundle/switch-executive/raw/resource/enus/using-ni-switch-executive-in-labview.html
- document_id: `switch-executive`
- page_type: `leaf`
- content_type: `concept`
- source_description: This topic assumes that you are using LabVIEW to manage your code development and that you are familiar with the ADE. Follow these steps to develop an Switch Executive application in LabVIEW:Open an existing or new LabVIEW VI. Locate the Switch Executive VIs. From the Functions palette, select Measu

### Using Switch Executive in LabVIEW

This topic assumes that you are using LabVIEW to manage your code development and that you are
 familiar with the ADE.

Follow these steps to develop an Switch Executive application in LabVIEW:

1. Open an existing or new LabVIEW VI.
2. Locate the Switch Executive VIs. From the Functions palette, select
 Measurement I/O»Switch Executive .
3. Select the VIs that you want to use and drop them on the block diagram to build your application.

#### Example Programs

Use the LabVIEW Example Finder to search or browse examples. Switch Executive
 examples are classified by keyword, so you can search for a particular device or
 measurement function.

To browse the Switch Executive examples available in
 LabVIEW, launch LabVIEW, click Help»Find
 Examples, and navigate to Toolkits and Modules»Switch
 Executive.

For additional information regarding Switch
 Executive examples, refer to *Examples*.

Parent topic:

Getting Started

Related concepts:

- Examples

<!--NI_TOPIC bundle=switch-executive path=using-ni-switch-executive-in-labwindows-cvi.html language=enus -->
## TOPIC 00113: Using Switch Executive in LabWindows/CVI

- bundle_id: `switch-executive`
- source_path: `using-ni-switch-executive-in-labwindows-cvi.html`
- source_url: https://docs-be.ni.com/bundle/switch-executive/raw/resource/enus/using-ni-switch-executive-in-labwindows-cvi.html
- document_id: `switch-executive`
- page_type: `leaf`
- content_type: `concept`
- source_description: This topic assumes that you are using the LabWindows/CVI ADE to manage your code development and that you are familiar with the ADE. Follow these steps to develop an Switch Executive application in LabWindows/CVI:Open an existing or new project file. Load the Switch Executive function panel(s). (Run

### Using Switch Executive in
 LabWindows/CVI

This topic assumes that you are using the LabWindows/CVI ADE to manage your code development and
 that you are familiar with the ADE.

Follow these steps to develop an Switch Executive application in LabWindows/CVI:

1. Open an existing or new project file.
2. Load the Switch Executive function panel(s).
  - (Run-time) nise.lfp at <CVI>\bin or
 \Shared\<CVI>\bin .
  - (Configuration) niseCfg.fp at
 <CVI>\bin or
 \Shared\<CVI>\bin .
3. Use the function panel to navigate the function hierarchy and generate function calls with the proper syntax and variable values.

#### Example Programs

For additional information regarding Switch Executive examples, refer to
 *Examples*.

Parent topic:

Getting Started

Related concepts:

- Examples

<!--NI_TOPIC bundle=switch-executive path=using-ni-switch-executive-in-max.html language=enus -->
## TOPIC 00114: Using Switch Executive in MAX

- bundle_id: `switch-executive`
- source_path: `using-ni-switch-executive-in-max.html`
- source_url: https://docs-be.ni.com/bundle/switch-executive/raw/resource/enus/using-ni-switch-executive-in-max.html
- document_id: `switch-executive`
- page_type: `leaf`
- content_type: `concept`
- source_description: Expand this topic to view instructions about how to use Switch Executive in Measurement & Automation Explorer (MAX).

### Using Switch Executive in MAX

Expand this topic to view instructions about how to use Switch Executive in Measurement &
 Automation Explorer (MAX).

[IMAGE alt='image' src='GUID-57350D73-591E-485F-A299-D43FEB5F3550-a5.png']

Parent topic:

Getting Started

<!--NI_TOPIC bundle=switch-executive path=using-ni-switch-executive-in-ni-teststand.html language=enus -->
## TOPIC 00115: Using Switch Executive in NI TestStand

- bundle_id: `switch-executive`
- source_path: `using-ni-switch-executive-in-ni-teststand.html`
- source_url: https://docs-be.ni.com/bundle/switch-executive/raw/resource/enus/using-ni-switch-executive-in-ni-teststand.html
- document_id: `switch-executive`
- page_type: `leaf`
- content_type: `concept`
- source_description: Using Switch Executive in TestStand, you can configure switching actions for TestStand steps. Implement individual switch operations for your TestStand steps with the Switching panel on the Step Properties dialog box. The IVI Switch step type supports not only the IVI class layer but also Switch Exe

### Using Switch Executive in NI TestStand

Using Switch Executive in TestStand, you can configure switching actions for TestStand steps.
 Implement individual switch operations for your TestStand steps with the Switching panel on
 the Step Properties dialog box. The IVI Switch step type supports not only the IVI class layer
 but also Switch Executive operations.

#### TestStand Switching Panel

TestStand includes a Switching panel on the Properties tab of the Step Settings pane. Use
 this feature with Switch Executive.

Use the Switching panel to specify the switching
 action you want TestStand to perform for a step. The following figure shows the Switching
 panel:

[IMAGE alt='image' src='GUID-AC27953E-61BA-4116-B80E-C54F7D949014-a5.png']

The Switching panel contains the following controls:

- Enable Switching —Specifies whether to perform the specified
 switching action for the step.
- Switch Executive Virtual Device —Specifies an expression that
 TestStand evaluates at run time to determine the virtual device on which TestStand
 performs the switching action.
- Operation —Specifies whether to connect or disconnect the
 specified routes or to disconnect all previously connected routes. This operation returns
 as soon as the instrument is ready for another operation, which may occur before or after
 the switches involved settle. Select the Wait For Debounce Before Executing
 Step checkbox if you want to wait until all switches have debounced. You can
 select from the following options:
  - Connect —Connects the paths for the specified routes in the
 Route(s) to Connect control.
  - Disconnect —Disconnects the paths defined by the specified
 routes in the Route(s) to Disconnect control.
  - Disconnect All —Disconnects all paths previously created.
  - Connect/Disconnect —Connects the paths for the routes
 specified in the Route(s) to Connect control and disconnects
 the paths for the routes specified in the Route(s) to
 Disconnect control. Use the Operation Order ring
 control to specify whether the disconnect operation occurs before or after the connect
 operation.
- Route(s) to Connect —Specifies the routes you are connecting. The
 expression must be a valid route specification string as defined by the Switch Executive
 configuration for the virtual device name you are using. The string can be a combination
 of route group alias names, route names, and physical route paths.
- Route(s) to Disconnect —Specifies the routes you are
 disconnecting. The expression must be a valid route specification string as defined by the
 Switch Executive configuration for the virtual device name you are using. The string can
 be a combination of route group alias names, route names, and physical route paths.
- Multiconnect Mode —Specifies the behavior when more than one
 connection operation occurs on a specific route. You can select from the following
 options:
  - Multiconnect Routes —A route can be connected multiple times.
 The route must contain the same endpoints and path. Switch Executive automatically
 reference counts the routes. If you issue multiple connect operations for a specific
 route, the route is not physically disconnected until an equal number of disconnect
 operations occur. You can either issue the Disconnect operation manually or use a
 lifetime setting for the route. The Disconnect All operation disconnects a route even
 if the route reference count is greater than 1.
  - No Multiconnect —A route can only be connected once. Any
 attempt to reconnect a route that is already connected results in an error.
  - Use Default Setting for Route —Use the setting defined for the
 route in the Switch Executive virtual device configuration. Note Use Default Setting for
 Route was first available in Switch Executive 2.0.
- Operation Order —Specifies whether the Disconnect operation occurs
 before or after the Connect operation. You can select from the following options:
  - Disconnect Before Connect —Disconnect the specified routes
 before connecting any routes. Disconnect Before Connect is the typical mode of
 operation.
  - Connect Before Disconnect —Connect the specified routes before
 disconnecting any routes. Use this mode of operation when you are switching electric
 current and want to ensure that a load is always connected to your source.
- Connection Lifetime —Specifies the lifetime that TestStand applies
 to the routes specified for the connect or connect/disconnect actions. You can specify
 whether you want the route to exist until manually disconnected later, or until the step,
 sequence, thread or execution completes. If you use the Multiconnect Mode, a route can
 exist longer if another step specifies its own lifetime for the same route. Selecting a
 lifetime other than manual guarantees that the route stays connected as long as the step,
 sequence, thread, or execution in which you connect is still executing. If you manually
 disconnect a route that was previously connected using a non-manual lifetime setting,
 TestStand releases the reference to the route for the last step that performed a connect
 action for that route.
- Wait for Debounce Before Executing Step —Specifies whether the
 operation waits for all switches to debounce before returning to TestStand. The wait for
 debounce occurs after both Connect and Disconnect operations are complete.

Parent topic:

Getting Started

<!--NI_TOPIC bundle=switch-executive path=using-ni-switch-executive-in-visual-basic.html language=enus -->
## TOPIC 00116: Using Switch Executive in Visual Basic

- bundle_id: `switch-executive`
- source_path: `using-ni-switch-executive-in-visual-basic.html`
- source_url: https://docs-be.ni.com/bundle/switch-executive/raw/resource/enus/using-ni-switch-executive-in-visual-basic.html
- document_id: `switch-executive`
- page_type: `leaf`
- content_type: `concept`
- source_description: This topic assumes that you are using the Microsoft Visual Basic ADE to manage your code development and that you are familiar with the ADE. Follow these steps to develop an Switch Executive application in Visual Basic:Open an existing or new Visual Basic project. Create files necessary for your app

### Using Switch Executive in Visual Basic

This topic assumes that you are using the Microsoft Visual Basic ADE to manage your code
 development and that you are familiar with the ADE.

Follow these steps to develop an Switch Executive application in Visual Basic:

1. Open an existing or new Visual Basic project.
2. Create files necessary for your application: form definition and event handling code ( .frm ), Visual Basic generic code module ( .bas ), or Visual Basic class module ( .cls ). Add these files to the project.
3. Add a reference to the Switch Executive Library, which is part of the Switch Executive DLL. In
 Visual Basic 6.0, select the Project»References menu option and
 Switch Executive Version 1.0 or Switch Executive
 Configuration API Version 1.0 . If you do not see NI Switch Executive listed there,
 use the Browse button and browse to system32\nise.dll . Note If Switch Executive does not display in the
 references dialog box in Visual Basic or if you are trying to use the type library in a
 language other than Visual Basic, you can add a reference to the nise.dll file
 in your system directory.
4. Use the Object Browser <F2> to find function prototypes and constants.
5. Add NI Switch Executive function calls to your application.
6. Click Run .

#### Example Programs

For additional information regarding Switch Executive examples, refer to
 *Examples*. To load an example project with Visual Basic 6.0, select
 File»Open Project, then select the .vbp file of your
 choice.

#### String Passing

In Visual Basic, variables of data type String do not need special modifications to be passed
 to Switch Executive functions. Visual Basic automatically appends a null character to the end of
 a string before passing it (by reference, because strings cannot be passed by value in Visual
 Basic) to a procedure or function.

#### Parameter Passing

By default, Visual Basic passes parameters by reference. Prepend the ByVal keyword if you need to pass by value.

Parent topic:

Getting Started

Related concepts:

- Examples

<!--NI_TOPIC bundle=switch-executive path=using-ni-switch-executive-in-visual-c.html language=enus -->
## TOPIC 00117: Using Switch Executive in Visual C++

- bundle_id: `switch-executive`
- source_path: `using-ni-switch-executive-in-visual-c.html`
- source_url: https://docs-be.ni.com/bundle/switch-executive/raw/resource/enus/using-ni-switch-executive-in-visual-c.html
- document_id: `switch-executive`
- page_type: `leaf`
- content_type: `concept`
- source_description: This topic assumes that you are using the Microsoft Visual C++ ADE to manage your code development and that you are familiar with the ADE.Follow these steps to develop an Switch Executive application in Visual C++:Open an existing or new Visual C++ project. Create source files of type C source code

### Using Switch Executive in Visual C++

This topic assumes that you are using the Microsoft Visual C++ ADE to manage your code
 development and that you are familiar with the ADE.

Follow these steps to develop an Switch Executive application in Visual C++:

1. Open an existing or new Visual C++ project.
2. Create source files of type C source code ( .c ) or C++ source code
 ( .cpp ) and add them to the project. Make sure that you include
 the Switch Executive header file, nise.h , in your source code files
 as follows: #include "nise.h" .
3. Specify the directory that contains the Switch Executive header file under the
 Preprocessor»Additional include directories settings in
 your compiler—for Visual C++ 6.0 these files are under
 Project»Settings»C/C++ . The Switch Executive header files
 are located at <SwitchExecutive>\API\C .
4. Add the Switch Executive import library nise.lib to the project under
 Link»General»Object/Library Modules . The Switch Executive
 import library files are located in the
 <SwitchExecutive>\API\C directory within your Switch
 Executive directory. Tip The nise.h file includes visatypes.h from
 NI-VISA. If the compiler is having trouble locating that file, you can add your
 VXIPnP include directory (e.g. "c:\vxipnp\winnt\include") to
 the project's list of directories to include from.
5. Add Switch Executive function calls to your application.
6. Build your application.

#### String Passing

To pass strings, pass a pointer to the first element of the character array. Be sure that the string is null-terminated.

#### Parameter Passing

By default, C passes parameters by value. Remember to pass pointers to variables when you need to pass by address.

Parent topic:

Getting Started

<!--NI_TOPIC bundle=switch-executive path=using-properties-and-attributes.html language=enus -->
## TOPIC 00118: Using Properties and Attributes

- bundle_id: `switch-executive`
- source_path: `using-properties-and-attributes.html`
- source_url: https://docs-be.ni.com/bundle/switch-executive/raw/resource/enus/using-properties-and-attributes.html
- document_id: `switch-executive`
- page_type: `leaf`
- content_type: `concept`
- source_description: Switch Executive contains high-level VIs and functions that set most of the device properties and attributes. Using the configuration API, you can use additional properties and attributes to modify Switch Executive virtual device configurations.Refer to Switch Executive LabVIEW Reference or Switch E

### Using Properties and Attributes

Switch Executive contains high-level VIs and functions that set most of the device properties and
 attributes. Using the configuration API, you can use additional properties and
 attributes to modify Switch Executive virtual device configurations.

Refer to *Switch Executive LabVIEW Reference* or *Switch Executive C Function
 Reference* for a complete listing of the available properties and attributes
 in Switch Executive.

#### Accessing Properties

In LabVIEW, properties are accessed through the Switch Executive property
 node.

Complete the following steps to access properties in LabVIEW:

1. Open a VI.
2. Right-click in the block diagram view to open the
 Functions palette.
3. Select Measurement I/O»Switch Executive»Configuration»Property
 Nodes to open the Switch Executive Configuration API Property
 Nodes palette.
4. Drag and drop the icon of the specific property node you want to use to the
 block diagram.
5. Left-click the property node and select the property that you want to use.
6. Resize the property node to add additional properties by dragging the resizing
 handle at the top or bottom of the node and release the mouse button.

Parent topic:

Programming with Switch Executive

<!--NI_TOPIC bundle=switch-executive path=using-the-configuration-api-in-excel.html language=enus -->
## TOPIC 00119: Using the Configuration API in Excel

- bundle_id: `switch-executive`
- source_path: `using-the-configuration-api-in-excel.html`
- source_url: https://docs-be.ni.com/bundle/switch-executive/raw/resource/enus/using-the-configuration-api-in-excel.html
- document_id: `switch-executive`
- page_type: `leaf`
- content_type: `concept`
- source_description: The use of the configuration API in Microsoft Excel was first available in Switch Executive 2.1. For more information about using the configuration API in Excel, visit ni.com/info and enter the Info Code NISEConfig.

### Using the Configuration API in Excel

The use of the configuration API in Microsoft Excel was first available in Switch Executive 2.1.
 For more information about using the configuration API in Excel, visit
 ni.com/info and enter the Info Code NISEConfig.

Parent topic:

Using the Configuration API

<!--NI_TOPIC bundle=switch-executive path=using-the-configuration-api-in-visual-c.html language=enus -->
## TOPIC 00120: Using the Configuration API in Visual C++

- bundle_id: `switch-executive`
- source_path: `using-the-configuration-api-in-visual-c.html`
- source_url: https://docs-be.ni.com/bundle/switch-executive/raw/resource/enus/using-the-configuration-api-in-visual-c.html
- document_id: `switch-executive`
- page_type: `leaf`
- content_type: `concept`
- source_description: Include the following lines in your code to use the Switch Executive Configuration API from Visual C++: #include "comdef.h" #import "C:\windows\system32\nise.dll" tlbid(2) no_namespace The tlbid(2) attribute is important because the COM type library is the second resource in a DLL. The first typelib

### Using the Configuration API in Visual C++

Include the following lines in your code to use the Switch Executive Configuration API from
 Visual C++:

#include "comdef.h"

#import "C:\windows\system32\nise.dll" tlbid(2) no_namespace

Note

tlbid(2)

typelib

no_namespace

#### Example

#include "stdafx.h"

#include
 "comdef.h"

#import "C:\windows\system32\nise.dll"
 tlbid(2) no_namespace

int _tmain(int argc, _TCHAR*
 argv[])

{

HRESULT hr = CoInitialize(NULL);

if
 (SUCCEEDED(hr))

{

VirtualDevicesPtr nise(__uuidof(NiseVirtualDevices)); // creates a smart
 pointer, no need to destroy this one

VirtualDevice* vd;
 // this will hold a pointer to VirtualDevice
 interface.

long numDevices;

BSTR
 vdName;

numDevices = nise->GetCount(); // get the
 number of virtual devices. You should have one (the example one) after default
 installation

vd = nise->GetItem(1); // get the first
 element in the collection of virtual devices. You can loop from 1 to numDevices
 if you want to examine the whole system

vdName =
 vd->GetName(); //get the name of the first configuration in a
 collection

SysTreeString(vdName);

vd->Release();
 // vd is not a smart pointer, you should release it. Smart pointers end in
 "Ptr"

CoUninitialize();

}

return 0;

}

Parent topic:

Using the Configuration API

<!--NI_TOPIC bundle=switch-executive path=using-the-configuration-api.html language=enus -->
## TOPIC 00121: Using the Configuration API

- bundle_id: `switch-executive`
- source_path: `using-the-configuration-api.html`
- source_url: https://docs-be.ni.com/bundle/switch-executive/raw/resource/enus/using-the-configuration-api.html
- document_id: `switch-executive`
- page_type: `leaf`
- content_type: `concept`
- source_description: The configuration API provides a programmatic interface to configure your Switch Executive virtual devices. Use the configuration API for the following tasks: Virtual device creation/editing—Create new virtual devices programmatically and edit existing configurations. The configuration API provides

### Using the Configuration API

The configuration API provides a programmatic interface to configure your Switch Executive
 virtual devices. Use the configuration API for the following tasks:

- Virtual device creation/editing —Create new virtual devices
 programmatically and edit existing configurations. The configuration API provides
 programmatic access to IVI devices, channels, exclusions, hardwires, buses, routes,
 and route groups.
- Configuration management —Programmatically import, export,
 delete, and rename Switch Executive configurations.
- Report generation —Create both simple and advanced reports by
 reading the configuration associated with a specified virtual device.

#### Object Hierarchy

[IMAGE alt='image' src='GUID-613260BF-7328-4DA3-89B2-49817C9F708B-a5.gif']

#### Additional Considerations

Differences exist between creating and editing your configuration in MAX and doing so
 programmatically:

- In MAX, you can change the hardwire on a channel from the channel details.
 Programmatically, you can only read the hardwire on the channel. To change the
 hardwire on a channel programmatically, you must first disassociate that channel
 from its current hardwire (if it was on a hardwire), and then associate it with
 another hardwire.
- The MAX UI configuration performs extensive checks when creating routes. When
 programmatically creating routes and route groups, Switch Executive performs
 only a portion of these checks:
  - You can programmatically set the constraints for a route, but these
 constraints are not checked when you set the route specification.
  - You can programmatically create a route that uses channels with
 different wire modes.
  - You can programmatically set the route specification to any well-formed
 string of channels. Although Switch Executive checks the route
 specification string for both valid channel names and syntax, it does
 not verify that the intermediate channels are reserved for routing, nor
 does it check for violations of exclusion conflicts.
  - You can programmatically add routes to the route group. However, Switch
 Executive does not check whether the routes can coexist in the route
 group. Switch Executive does not check for the exclusion conflicts or
 repetitive use of reserved for routing channels.

For best results, open your configuration in MAX, load all routes and route
 groups in the Routes/Groups tab, and run the
 *validator* and/or the *test panel* to verify your
 configuration.

Parent topic:

Switch Executive Help

Related concepts:

- Validating a Virtual Device

<!--NI_TOPIC bundle=switch-executive path=using-third-party-switches.html language=enus -->
## TOPIC 00122: Using Third-Party Switches

- bundle_id: `switch-executive`
- source_path: `using-third-party-switches.html`
- source_url: https://docs-be.ni.com/bundle/switch-executive/raw/resource/enus/using-third-party-switches.html
- document_id: `switch-executive`
- page_type: `leaf`
- content_type: `concept`
- source_description: Switch Executive uses IVI driver sessions and/or IVI logical names as a way to communicate with all IVI-compliant switches. For Switch Executive to recognize a third-party switch, you must create an IVI configuration.Complete the following steps to create an IVI configuration for a third-party, IVI-

### Using Third-Party Switches

Switch Executive uses IVI driver sessions and/or IVI logical names as a way to communicate with
 all IVI-compliant switches. For Switch Executive to recognize a third-party switch, you
 must create an IVI configuration.

Complete the following steps to create an IVI configuration for a third-party, IVI-compliant
 switch:

#### Create a Driver Session

1. Launch MAX with Switch Executive.
2. Expand IVI Drivers .
3. Right-click Driver Sessions .
4. Select Create New (case-sensitive) . A driver session with a default name of NewDriverSessionX is created.
5. Select the General tab at the bottom of the window that displays on the right.
6. Edit the driver setup string as needed. You may need to modify the driver setup string to specify appropriate topology information. Refer to your third-party software vendor for more information.
7. Select the Hardware tab.
8. Select the hardware in the Hardware Assets window.
9. (Optional) Click the Add and Remove buttons to add and remove hardware assets.
10. Edit the resource descriptor as needed. Refer to the instrument driver vendor for information about specifying the resource descriptor.
11. Select the Software tab.
12. Select the IVI driver for the switch from the Software Module drop-down
 listbox. Note If the
 software module does not display in the drop-down listbox, contact the
 instrument driver vendor for an updated installer.
13. Cycle through the tabs and make any additional changes where appropriate.
14. Click in
 the Switch Executive taskbar to save the changes.

#### Create a Logical Name

1. Launch MAX with Switch Executive.
2. Expand IVI Drivers .
3. Right-click Logical Names .
4. Select Create New (case-sensitive) . A logical name with a default name of NewLogicalName is created.
5. Select the driver session you created for your switch from the Driver Session drop-down listbox in the window on the right.
6. Click in the
 Switch Executive taskbar to save the changes.

Parent topic:

Configuring IVI Switches

<!--NI_TOPIC bundle=switch-executive path=validating-a-virtual-device.html language=enus -->
## TOPIC 00123: Validating a Virtual Device

- bundle_id: `switch-executive`
- source_path: `validating-a-virtual-device.html`
- source_url: https://docs-be.ni.com/bundle/switch-executive/raw/resource/enus/validating-a-virtual-device.html
- document_id: `switch-executive`
- page_type: `leaf`
- content_type: `concept`
- source_description: Complete the following steps to validate an Switch Executive virtual device:Launch MAX with Switch Executive. Expand Devices and Interfaces»Switch Executive Virtual Devices. Select the virtual device you want to validate. Click on the Switch Executive taskbar in MAX. A dialog box opens. (Optional) S

### Validating a Virtual Device

Complete the following steps to validate an Switch Executive virtual device:

1. Launch MAX with Switch Executive.
2. Expand Devices and Interfaces»Switch Executive Virtual Devices .
3. Select the virtual device you want to validate.
4. Click on the
 Switch Executive taskbar in MAX. A dialog box opens.
5. (Optional) Select the Use Simulation Mode checkbox to simulate
 connections during validation. Note Simulation mode simulates the
 configuration of your virtual device, performs a valid system check, and reduces
 the wear and tear on switch relays. Simulation mode does not physically
 communicate with your switches. Caution If you do not use Simulation
 mode, ensure that you have disconnected any fixturing or wiring that might be
 damaged by connecting all of your routes and route groups.
6. Click the checkbox items you want to validate: IVI Configuration , Routes , and/or Route Groups .
7. Click Next . A window displays the validation status of the items in your configuration and if the validation passes or fails.
8. Proceed to step 9 if the validation test passes. If the validation status includes any errors, correct the configuration and repeat steps 4 through 7.
9. Click Finish . Now you can program and/or deploy the virtual device.
10. Click on the
 Switch Executive taskbar to save the configuration.

Parent topic:

Using Switch Executive in MAX

<!--NI_TOPIC bundle=switch-executive path=validating-deployment.html language=enus -->
## TOPIC 00124: Validating Deployment

- bundle_id: `switch-executive`
- source_path: `validating-deployment.html`
- source_url: https://docs-be.ni.com/bundle/switch-executive/raw/resource/enus/validating-deployment.html
- document_id: `switch-executive`
- page_type: `leaf`
- content_type: `concept`
- source_description: Validate the deployment of an Switch Executive virtual device to ensure the following: The correct IVI switches are present and named properly Routes are valid Route groups are valid

### Validating Deployment

*Validate* the deployment of an Switch Executive virtual device to ensure the
 following:

- The correct IVI switches are present and named properly
- Routes are valid
- Route groups are valid

Parent topic:

Deploying a Virtual Device

Related concepts:

- Validating a Virtual Device

<!--NI_TOPIC bundle=switch-executive path=validation.html language=enus -->
## TOPIC 00125: Validation

- bundle_id: `switch-executive`
- source_path: `validation.html`
- source_url: https://docs-be.ni.com/bundle/switch-executive/raw/resource/enus/validation.html
- document_id: `switch-executive`
- page_type: `leaf`
- content_type: `concept`
- source_description: Validate a virtual device to ensure that IVI configurations, routes, and route groups are valid and route group members do not use conflicting resources.You should always validate after making any modifications to the virtual device configuration and after deploying a virtual device.

### Validation

Validate a virtual device to ensure that IVI configurations, routes, and route groups are valid
 and route group members do not use conflicting resources.

You should always validate after making any modifications to the virtual device configuration and
 after deploying a virtual device.

Parent topic:

Concepts

Related concepts:

- Validating a Virtual Device
- Using the Configuration API

<!--NI_TOPIC bundle=switch-executive path=verifying-system-requirements.html language=enus -->
## TOPIC 00126: Verifying System Requirements

- bundle_id: `switch-executive`
- source_path: `verifying-system-requirements.html`
- source_url: https://docs-be.ni.com/bundle/switch-executive/raw/resource/enus/verifying-system-requirements.html
- document_id: `switch-executive`
- page_type: `leaf`
- content_type: `concept`
- source_description: Verify your system includes the following before you configure an Switch Executive virtual device: An Switch Executive development license The Development System Requirements of the Switch Executive Readme file An application development environment (ADE), such as LabVIEW, TestStand, LabWindows/CVI,

### Verifying System Requirements

Verify your system includes the following before you configure an Switch Executive virtual
 device:

- An Switch Executive development license
- The Development System Requirements of the Switch Executive Readme 
 file
- An application development environment (ADE), such as LabVIEW, TestStand, LabWindows/CVI, or
 Visual Basic
- IVI switches with installed IVI-compliant specific instrument drivers Note Switch Executive only
 supports C-based specific drivers. You can create your own C-based specific IVI
 driver with LabWindows/CVI templates.

Parent topic:

Getting Started

Related concepts:

- Activating Your Software
- Configuring IVI Switches

Related information:

- Related Documentation

<!--NI_TOPIC bundle=switch-executive path=virtual-device.html language=enus -->
## TOPIC 00127: Virtual Device

- bundle_id: `switch-executive`
- source_path: `virtual-device.html`
- source_url: https://docs-be.ni.com/bundle/switch-executive/raw/resource/enus/virtual-device.html
- document_id: `switch-executive`
- page_type: `leaf`
- content_type: `concept`
- source_description: A Switch Executive virtual device represents a switching system. As such, a virtual device is composed of the switch modules, channels, hardwires, buses, exclusions, routes, and route group definitions and configurations that are a part of the switching system.

### Virtual Device

A Switch Executive *virtual device* represents a switching system. As such, a
 *virtual device* is composed of the switch modules, channels, hardwires,
 buses, exclusions, routes, and route group definitions and configurations that are a
 part of the switching system.

Parent topic:

Fundamentals

Related concepts:

- Creating a Virtual Device
- Creating a Virtual Device Using the Switch SFP
- Using the Configuration API
