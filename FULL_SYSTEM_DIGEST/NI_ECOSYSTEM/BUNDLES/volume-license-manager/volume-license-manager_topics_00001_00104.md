# NI DOCUMENT BUNDLE: volume-license-manager

<!--NI_BUNDLE_CHUNK bundle=volume-license-manager start=1 end=104 -->
<!--NI_TOPIC bundle=volume-license-manager path=adding-custom-fields.html language=enus -->
## TOPIC 00001: Adding Custom Fields

- bundle_id: `volume-license-manager`
- source_path: `adding-custom-fields.html`
- source_url: https://docs-be.ni.com/bundle/volume-license-manager/raw/resource/enus/adding-custom-fields.html
- document_id: `volume-license-manager`
- page_type: `leaf`
- content_type: `concept`
- source_description: Complete the following steps to add custom fields: Select the ToolsPreferences menu item. Select Custom Fields in the navigation tree. Click the Add button to add a custom field. Enter the field name. Custom field names must be unique. Select whether to make the field Text or List. Default field typ

### Adding Custom Fields

Complete the following steps to add custom fields:

1. Select the Tools»Preferences menu item.
2. Select Custom Fields in the navigation tree.
3. Click the Add button to add a custom field.
4. Enter the field name. Note Custom
 field names must be unique.
5. Select whether to make the field Text or List .
 Default field type is Text . Note For
 List option, click 0 Items
 to add the list items. Edit List displays the number
 of items avaiable for selection. To add a list itemEnter the item name in the List Selection
 dialog box.Click Add.Click OK when you are finished.To delete a list itemSelect one or more fields on the list and click
 Delete.Click OK when you are finished.
6. Select whether to make the field Required or
 Optional when a client sends a permission request
 from a Volume License Installer or NI License Manager. Note All fields are optional when
 you, as the administrator, add a Computer or User from within NI VLM,
 regardless of this setting.
7. Click Save when you are finished.

Parent topic:

Configuring Custom Fields

<!--NI_TOPIC bundle=volume-license-manager path=adding-the-ni-device-driver-dvd-to-a-volume-license-installer.html language=enus -->
## TOPIC 00002: Adding the NI Device Driver DVD to a Volume License Installer

- bundle_id: `volume-license-manager`
- source_path: `adding-the-ni-device-driver-dvd-to-a-volume-license-installer.html`
- source_url: https://docs-be.ni.com/bundle/volume-license-manager/raw/resource/enus/adding-the-ni-device-driver-dvd-to-a-volume-license-installer.html
- document_id: `volume-license-manager`
- page_type: `leaf`
- content_type: `concept`
- source_description: Add the NI Device Drivers DVD to your volume license installer to eliminate disk prompts in your network-based volume license installers. Bundling the Device Drivers Before you can add the NI Device Drivers DVD to your Volume License Installer, you must first confirm whether you have a software suit

### Adding the NI Device Driver DVD to a Volume License Installer

Add the NI Device Drivers DVD to your volume license installer to eliminate disk
 prompts in your network-based volume license installers.

#### Bundling the Device
 Drivers

Before you can add the NI Device Drivers DVD to your Volume License Installer, you
 must first confirm whether you have a software suite such as NI Developer Suite,
 LabVIEW Platform or Academic Site License. To do this, navigate to the folder
 containing your software. If you are working with a suite, there will be a document
 labeled nisuite.xml. If you are working with a distribution, there
 will be a document labeled nidist.id.

After determining
 your software type, complete the following steps to bundle the NI Device Drivers DVD
 with your Volume License Installer (VLI):

Note

1. If you are working with a suite, determine whether the suite already includes NI
 Device Drivers.
  1. Navigate to the <VLI Location> and open the
 nisuite.xml file.
  2. Locate the tag with one of the following names: <distribution
 id="DRIVERS"> or <distribution
 id="DRIVERSDIST"> .
  3. Read the contents of the <inputRoot> tag.
    - If the tag contains a value, the suite already includes device
 drivers. For example, <inputRoot
 suiteVolume="5">Distributions\Device
 Drivers</inputRoot> . You do not need to
 complete any additional steps.
    - If the tag is empty, proceed with the following steps.
2. Insert the NI Device Drivers DVD.
3. Navigate to the <VLI Location> .
4. Open the _Src folder.
5. Create a folder called DriverDVD .
6. Copy the contents of the NI Device Drivers DVD, specifically the contents of the
 folder labeled DVD-MonthYear-Volume into your newly created
 DriverDVD folder. You can disregard the contents of the
 meta-data folder.
7. For distributions, complete the following steps:
  1. Navigate to the <VLI Location>\_Src folder and
 open the setup.ini file.
  2. Scroll to the bottom of the file and add
 Path=.\DriverDVD to the [Drivers] 
 section.
8. For suites, complete the following steps:
  1. Navigate to the <VLI Location> and open the
 nisuite.xml file.
  2. Locate the <distribution id="DRIVERS"> tag and
 change <inputRoot suiteVolume="5"/> to
 <inputRoot
 suiteVolume="5">_Src\DriverDVD</inputRoot> . The
 resulting section should be similar to the following: <distribution id="DRIVERS">
 <distId GUID="{D6FB44F4-CD59-4d6b-856F-66A3D06BCE94}" languages="9,7,12,17,18,2052" version="2012.08.0.0"/>
 <inputRoot suiteVolume="5"/>_Src\DriverDVD</inputRoot>
 <installOrder>49999</installOrder>
 <EULAId>None</EULAId>
 <distributionType>Driver</distributionType>
 <displayFolderId>DeveloperSuiteCore</displayFolderId>
 <name language="0009">NI Device Drivers - August 2012</name>

#### Installing the Volume License
 Installer

To install the software on a client machine using the Volume License Installer,
 complete the following steps:

1. Navigate to the Volume License Installer and run the installer executable.
2. In the Installation Wizard, ensure that you have Device Drivers set to
 install.
3. As you proceed with the installation, you should see that the installation
 switches from the software installation to the device drivers installation
 without prompting you to insert the driver disc. Note The Installation Wizard will
 still prompt you to choose which features of the device drivers to
 install.

Parent topic:

Using Volume License Servers and Installers

<!--NI_TOPIC bundle=volume-license-manager path=automating-client-software-installation.html language=enus -->
## TOPIC 00003: Automating Client Software Installation

- bundle_id: `volume-license-manager`
- source_path: `automating-client-software-installation.html`
- source_url: https://docs-be.ni.com/bundle/volume-license-manager/raw/resource/enus/automating-client-software-installation.html
- document_id: `volume-license-manager`
- page_type: `leaf`
- content_type: `concept`
- source_description: Automate the installation of Volume License Installers onto client machines. Specifying Groups The /groups command line option is supported when you have configured your Volume License Installer to send either a group permission request or a client information only request to NI VLM. Use the /groups

### Automating Client Software Installation

Automate the installation of Volume License Installers onto client
 machines.

#### Specifying Groups

The /groups command line option is supported when you have
 configured your Volume License Installer to send either a group permission request
 or a client information only request to NI VLM.

Use the
 /groups command to specify which groups a client will request
 permissions to when running a Volume License Installer. Groups are specified using
 their Group Unique ID. Refer to Finding a Group Unique ID for more
 information.

Syntax: setup.exe /groups
 "groupid[,groupid,...]"

Examples:
 setup.exe /groups "{498EE0C5-D626-4952-9E5D-D35ED217765E}"setup.exe /groups
 "{498EE0C5-D626-4952-9E5D-D35ED217765E},{01588B1A-140E-41CF-A886-3E8134B11254}"

#### Finding a Group Unique ID

You can find a Group Unique ID using the following steps:

1. In NI VLM, select the Groups view.
2. Double-click on the group for which you need a Group Unique ID.
3. Right-click on the icon in the top left corner and select Copy Group
 Unique ID to copy it to your clipboard.

[IMAGE alt='image' src='GUID-487B4CD2-C324-4737-B463-CD8F2D3D7C7E-a5.png']

#### Enabling Silent
 Installation

Use the /groups command, along with the normal silent installer
 commands, to specify which groups a client will automatically request permissions to
 when running the Volume License Installer silently.

1. Obtain the Group Unique ID.
2. From a command line, run the Volume License Installer with the following command line flags,
 depending on how many groups you use. Example: setup.exe /q
 /acceptlicenses yes /groups "groupid" Note If you have
 configured your Volume License Installer to request permissions for groups,
 but you want to override that setting when running the Volume License
 Installer silently, you can provide an empty string as the Group Unique ID
 as follows: setup.exe /q /acceptlicenses yes /groups
 "" Note For Volume License Installers
 created from NI Package Installer, use the following command for silent
 installation: setup.exe --quiet --accept-eulas /groups
 ""

Parent topic:

Managing the Volume License Server

<!--NI_TOPIC bundle=volume-license-manager path=automating-client-software-installation_2.html language=enus -->
## TOPIC 00004: Automating Client Software Installation

- bundle_id: `volume-license-manager`
- source_path: `automating-client-software-installation_2.html`
- source_url: https://docs-be.ni.com/bundle/volume-license-manager/raw/resource/enus/automating-client-software-installation_2.html
- document_id: `volume-license-manager`
- page_type: `leaf`
- content_type: `concept`
- source_description: Automate the installation of Volume License Installers onto client machines. Specifying Groups The /groups command line option is supported when you have configured your Volume License Installer to send either a group permission request or a client information only request to NI VLM. Use the /groups

### Automating Client Software Installation

Automate the installation of Volume License Installers onto client
 machines.

#### Specifying Groups

The /groups command line option is supported when you have
 configured your Volume License Installer to send either a group permission request
 or a client information only request to NI VLM.

Use the
 /groups command to specify which groups a client will request
 permissions to when running a Volume License Installer. Groups are specified using
 their Group Unique ID. Refer to Finding a Group Unique ID for more
 information.

Syntax: setup.exe /groups
 "groupid[,groupid,...]"

Examples:
 setup.exe /groups "{498EE0C5-D626-4952-9E5D-D35ED217765E}"setup.exe /groups
 "{498EE0C5-D626-4952-9E5D-D35ED217765E},{01588B1A-140E-41CF-A886-3E8134B11254}"

#### Finding a Group Unique ID

You can find a Group Unique ID using the following steps:

1. In NI VLM, select the Groups view.
2. Double-click on the group for which you need a Group Unique ID.
3. Right-click on the icon in the top left corner and select Copy Group
 Unique ID to copy it to your clipboard.

[IMAGE alt='image' src='GUID-487B4CD2-C324-4737-B463-CD8F2D3D7C7E-a5.png']

#### Enabling Silent
 Installation

Use the /groups command, along with the normal silent installer
 commands, to specify which groups a client will automatically request permissions to
 when running the Volume License Installer silently.

1. Obtain the Group Unique ID.
2. From a command line, run the Volume License Installer with the following command line flags,
 depending on how many groups you use. Example: setup.exe /q
 /acceptlicenses yes /groups "groupid" Note If you have
 configured your Volume License Installer to request permissions for groups,
 but you want to override that setting when running the Volume License
 Installer silently, you can provide an empty string as the Group Unique ID
 as follows: setup.exe /q /acceptlicenses yes /groups
 "" Note For Volume License Installers
 created from NI Package Installer, use the following command for silent
 installation: setup.exe --quiet --accept-eulas /groups
 ""

Parent topic:

Automating VLM Operations

<!--NI_TOPIC bundle=volume-license-manager path=automating-operations.html language=enus -->
## TOPIC 00005: Automating VLM Operations

- bundle_id: `volume-license-manager`
- source_path: `automating-operations.html`
- source_url: https://docs-be.ni.com/bundle/volume-license-manager/raw/resource/enus/automating-operations.html
- document_id: `volume-license-manager`
- page_type: `leaf`
- content_type: `concept`
- source_description: Learn how to automate common VLM operations.

### Automating VLM Operations

Learn how to automate common VLM operations.

- [Automating Client Software Installation](automating-client-software-installation_2.html) Automate the installation of Volume License Installers onto client machines.
- [Command Line Interface Options](using-command-line-interface-options.html) Command line options enable you to automate certain tasks when managing volume licenses. Refer to the command reference available for the niVlm.exe and nivlmcmd.exe binaries to learn more about available options.
- [Using the NI VLM Import Utility](using-the-ni-vlm-import-utility.html#GUID-AD75A7EC-A8F1-4BE6-BD7B-49B3F5A60D93) Collect client data, such as computer IDs and information from custom fields, without using volume license installers.

<!--NI_TOPIC bundle=volume-license-manager path=backing-up-and-restoring-ni-vlm-data.html language=enus -->
## TOPIC 00006: Backing up and Restoring NI VLM Data

- bundle_id: `volume-license-manager`
- source_path: `backing-up-and-restoring-ni-vlm-data.html`
- source_url: https://docs-be.ni.com/bundle/volume-license-manager/raw/resource/enus/backing-up-and-restoring-ni-vlm-data.html
- document_id: `volume-license-manager`
- page_type: `leaf`
- content_type: `concept`
- source_description: You can back up or restore your NI VLM data, settings, and log files using the Backup and Restore Wizard. Items backed up include the NI VLM configuration, license, usage data, and permission requests. The Backup and Restore Wizard provides the following features: On-demand backups, callable from wi

### Backing up and Restoring NI VLM Data

You can [back up](creating-an-ni-vlm-backup.html) or [restore](restoring-ni-vlm-from-a-backup-file.html) your NI VLM data, settings, and log files using the Backup and



 Restore Wizard. Items backed up include the NI VLM configuration, license, usage



 data, and permission requests.

The Backup and Restore Wizard provides the following features:

- On-demand backups, callable from within NI VLM and also from a command line
- On-demand data restoration
- Storage of all backed-up data in one file

You should regularly back up NI VLM to a network location so that you can restore all



 of your data in case of a catastrophic failure, such as losing all



 computer/user/permissions data after a hard drive crash.

Note

NI VLM Getting Started Wizard

#### Creating and Restoring NI VLM Backups

- Creating an NI VLM Backup
- Restoring NI VLM from a Backup File
- Finishing the NI VLM Backup/Restore Wizard
- Scheduling Regular Backups

Parent topic:

Managing the Volume License Server

<!--NI_TOPIC bundle=volume-license-manager path=batch-updating-custom-fields.html language=enus -->
## TOPIC 00007: Batch Updating Custom Fields

- bundle_id: `volume-license-manager`
- source_path: `batch-updating-custom-fields.html`
- source_url: https://docs-be.ni.com/bundle/volume-license-manager/raw/resource/enus/batch-updating-custom-fields.html
- document_id: `volume-license-manager`
- page_type: `leaf`
- content_type: `concept`
- source_description: Using Batch Update, you can update a custom field value for multiple users or computers to a single, consistent value. Complete the following steps to batch update custom fields. In the Users or Computers view, select two or more clients you want to edit. You can shift-click or control-click to sele

### Batch Updating Custom Fields

Using Batch Update, you can update a custom field value for multiple users or



 computers to a single, consistent value.

Complete the following steps to batch update custom fields.

1. In the Users or Computers view,



 select two or more clients you want to edit. You can shift-click or



 control-click to select multiple clients.
2. Click Batch Update .
3. In the dialog box that appears, edit the fields you want to update. Editing



 these fields changes the values of the selected clients to the new value. Fields



 displaying (Multiple Values) in gray text indicate that



 the selected clients have differing values for a custom field. An empty cell



 indicates all clients in the selection have an empty string as the value for



 that custom field.

Note

[IMAGE alt='image' src='GUID-72744C86-CA1E-42AA-B414-6BA934B6E54F-a5.png']

[IMAGE alt='image' src='GUID-011C70B3-2C39-4BE9-B3B3-D7AA9B3A86B7-a5.png']

Parent topic:

Configuring Custom Fields

<!--NI_TOPIC bundle=volume-license-manager path=building-volume-license-installers.html language=enus -->
## TOPIC 00008: Building Volume License Installers

- bundle_id: `volume-license-manager`
- source_path: `building-volume-license-installers.html`
- source_url: https://docs-be.ni.com/bundle/volume-license-manager/raw/resource/enus/building-volume-license-installers.html
- document_id: `volume-license-manager`
- page_type: `leaf`
- content_type: `concept`
- source_description: Building a Volume License Installer can take anywhere from a few minutes to a few hours. You can continue using NI VLM while the Volume License Installer is building.

### Building Volume License Installers

Building a Volume License Installer can take anywhere from a few minutes to a few



 hours. You can continue using NI VLM while the Volume License Installer is



 building.

Parent topic:

Creating Volume License Installers

<!--NI_TOPIC bundle=volume-license-manager path=completing-ni-volume-license-manager-setup.html language=enus -->
## TOPIC 00009: Completing VLM Setup

- bundle_id: `volume-license-manager`
- source_path: `completing-ni-volume-license-manager-setup.html`
- source_url: https://docs-be.ni.com/bundle/volume-license-manager/raw/resource/enus/completing-ni-volume-license-manager-setup.html
- document_id: `volume-license-manager`
- page_type: `leaf`
- content_type: `task`
- source_description: Launch and configure NI VLM to monitor clients. Use the following flowchart to guide you through the VLM setup process. 1 VLM Setup Process You must have Administrator privileges on the server to install and use VLM. Launch NI VLM and complete the NI VLM Getting Started Wizard. Configure the NI VLM

### Completing VLM Setup

Launch and configure NI VLM to monitor clients.

Use the following flowchart to guide you through the VLM setup process.

Figure 1.

[IMAGE alt='image' src='GUID-594783CE-6021-4A7D-A53C-325A803C6BFA-a5.svg']

Note

1. Launch NI VLM and complete the NI VLM Getting Started
 Wizard.
2. Configure the NI VLM preferences.
3. Add and edit groups.
4. Determine if the client machines are connected to the network. 
 StatusStepsConnected
 Create a volume license installer.
 Handle any permission requests.Not connected
 Collect client data.
 Import client data into NI VLM.
 Create a disconnected license file.
 Install a disconnected license file on the
 client.
5. Send a VLA log to NI.

Parent topic:

Setting up VLM

Related concepts:

- Completing the VLM Getting Started Wizard
- Configuring NI VLM Preferences
- Adding Groups
- Creating Volume License Installers
- Handling Permission Requests
- Collecting Client Data
- Importing Client Data
- Managing Disconnected License Files
- Installing Disconnected License Files
- Sending a VLA Log to NI

<!--NI_TOPIC bundle=volume-license-manager path=completing-the-disconnection-wizard.html language=enus -->
## TOPIC 00010: Completing the Disconnection Wizard

- bundle_id: `volume-license-manager`
- source_path: `completing-the-disconnection-wizard.html`
- source_url: https://docs-be.ni.com/bundle/volume-license-manager/raw/resource/enus/completing-the-disconnection-wizard.html
- document_id: `volume-license-manager`
- page_type: `leaf`
- content_type: `concept`
- source_description: The Disconnection Wizard has created the disconnected license files. If you selected to save the disconnected license files, click the link to open the containing directory. Frequently Asked Questions How do my clients install a disconnected license file?

### Completing the Disconnection Wizard

The Disconnection Wizard has created the disconnected license files. If you selected



 to save the disconnected license files, click the link to open the containing



 directory.

#### Frequently Asked Questions

[How do my clients install a disconnected license
 file?](installing-disconnected-license-files.html)

Parent topic:

Managing Disconnected License Files

<!--NI_TOPIC bundle=volume-license-manager path=completing-the-home-license-wizard.html language=enus -->
## TOPIC 00011: Completing the Home License Wizard

- bundle_id: `volume-license-manager`
- source_path: `completing-the-home-license-wizard.html`
- source_url: https://docs-be.ni.com/bundle/volume-license-manager/raw/resource/enus/completing-the-home-license-wizard.html
- document_id: `volume-license-manager`
- page_type: `leaf`
- content_type: `concept`
- source_description: The Home License Wizard has created the home license file. If you selected to save the home license file, click the link to open the containing directory. Frequently Asked Questions How do my clients install a home license file?

### Completing the Home License Wizard

The Home License Wizard has created the home license file. If you selected to save



 the home license file, click the link to open the containing directory.

#### Frequently Asked Questions

[How do my clients install a home license
 file?](installing-home-license-files.html)

Parent topic:

Creating Home License Files

<!--NI_TOPIC bundle=volume-license-manager path=completing-the-ni-volume-license-manager-getting-started-wizard.html language=enus -->
## TOPIC 00012: Completing the VLM Getting Started Wizard

- bundle_id: `volume-license-manager`
- source_path: `completing-the-ni-volume-license-manager-getting-started-wizard.html`
- source_url: https://docs-be.ni.com/bundle/volume-license-manager/raw/resource/enus/completing-the-ni-volume-license-manager-getting-started-wizard.html
- document_id: `volume-license-manager`
- page_type: `leaf`
- content_type: `concept`
- source_description: The Getting Started Wizard guides you through the process of setting up a computer as a volume license server. Use the wizard to obtain a license file, import settings, configure ports, and finalize setup. Follow the outlined steps to complete the configuration efficiently.

### Completing the VLM Getting Started Wizard

The Getting Started Wizard guides you through the process of setting up a computer as
 a volume license server. Use the wizard to obtain a license file, import settings, configure
 ports, and finalize setup. Follow the outlined steps to complete the configuration
 efficiently.

1. Obtaining or Installing an Agreement License File
2. Importing Settings from Previous NI VLM Installations
3. Specifying License Ports and Administrator Information
4. Configuring Email Preferences Learn how to configure email preferences in NI VLM by setting up the SMTP server for administrator notifications, client communications, and license management.
5. Configuring Overdraft
6. Finishing the VLM Getting Started Wizard Complete the Getting Started Wizard by clicking Finish based on your agreement license file status. If a new license file is required, relaunch VLM upon receipt to continue the setup. For valid license files, finalize the wizard to proceed with VLM configuration.

Parent topic:

Setting up VLM

Related tasks:

- Completing VLM Setup

<!--NI_TOPIC bundle=volume-license-manager path=computers-view.html language=enus -->
## TOPIC 00013: Computers View

- bundle_id: `volume-license-manager`
- source_path: `computers-view.html`
- source_url: https://docs-be.ni.com/bundle/volume-license-manager/raw/resource/enus/computers-view.html
- document_id: `volume-license-manager`
- page_type: `leaf`
- content_type: `concept`
- source_description: Use the Computers view to manage any computer listed in NI VLM. The Computers view displays the following columns: Computer name Computer ID Any custom fields you created Disconnection Expiration Home License Expiration Home Computer ID To see hidden columns, right click on any column header, select

### Computers View

Use the Computers view to manage any computer listed in NI
 VLM.

The Computers view displays the following columns:

- Computer name
- Computer ID
- Any custom fields you created
- Disconnection Expiration
- Home License Expiration
- Home Computer ID

Note

Add/Remove Columns

#### Viewing Computer
 Information

[Expand](expanding-and-collapsing-rows.html)
 each computer to view more information, including the following:

- A summary of the computer's permissions
- The computer's groups
- The computer's explicit licenses

Note

Add/Remove
 Columns

#### Editing Computers

From this view, you can perform the following tasks:

- Add 
 a computer to NI VLM
- Edit 
 a listed computers
- Delete one or more of the listed computers
- Disconnect one or more of the listed computers
- Reconnect one or more of the listed computers
- Create a home license for a listed computers
- Batch
 update a custom field value for multiple computers to a single
 value.
- Email multiple computers

Parent topic:

VLM User Interface

<!--NI_TOPIC bundle=volume-license-manager path=configuring-custom-fields.html language=enus -->
## TOPIC 00014: Configuring Custom Fields

- bundle_id: `volume-license-manager`
- source_path: `configuring-custom-fields.html`
- source_url: https://docs-be.ni.com/bundle/volume-license-manager/raw/resource/enus/configuring-custom-fields.html
- document_id: `volume-license-manager`
- page_type: `leaf`
- content_type: `concept`
- source_description: Use custom fields to store detailed information about clients as needed. These fields automatically appear and can be edited wherever applicable, including in areas such as users, computers, groups, permissions, reports, and more. Custom fields affect users and computers equally. For example, if you

### Configuring Custom Fields

Use custom fields to store detailed information about clients as needed.
 These fields automatically appear and can be edited wherever
 applicable, including in areas such as users, computers, groups,
 permissions, reports, and more.

Custom fields affect users and computers equally. For example, if
 you create a new field named
 Building, that new field appears
 in the properties of both
 Users and
 Computers.

Note

Parent topic:

Configuring NI VLM Preferences

<!--NI_TOPIC bundle=volume-license-manager path=configuring-email-preferences.html language=enus -->
## TOPIC 00015: Configuring Email Preferences

- bundle_id: `volume-license-manager`
- source_path: `configuring-email-preferences.html`
- source_url: https://docs-be.ni.com/bundle/volume-license-manager/raw/resource/enus/configuring-email-preferences.html
- document_id: `volume-license-manager`
- page_type: `leaf`
- content_type: `task`
- source_description: Learn how to configure email preferences in NI VLM by setting up the SMTP server for administrator notifications, client communications, and license management. Contact your network administrator to obtain SMTP server settings. In the General section, set Enable email to Yes. In the Outgoing Mail Se

### Configuring Email Preferences

Learn how to configure email preferences in NI VLM by setting up the SMTP server for
 administrator notifications, client communications, and license management.

Note

1. In the General section, set Enable email to
 Yes.
2. In the Outgoing Mail Server Information section, enter the SMTP server address
 in the Server Address box. 
 You can optionally specify a port number, for example,
 smtp.example.com:465. The default port is 25 if you are
 not using SSL/TLS encryption. If you are using SSL/TLS encryption, the
 default port is 465.
3. Select whether to enable encryption in the Server requires encrypted
 connection setting.
4. If the SMTP server requires authentication, enter your SMTP server
 Username and Password.
5. Enter the sender's Name and
 Email. 
 You can enter the same information as the Administrator
 Information setting, or you can specify a different name and
 email address.
6. Click Send Test Email to test the email server
 settings.
  1. In the dialog box that appears, you can either use the existing
 administrator email address, if shown, or enter another email address at
 which you want to receive the test email.
  2. Click Send.

Parent topic:

Completing the VLM Getting Started Wizard

<!--NI_TOPIC bundle=volume-license-manager path=configuring-email-server-settings.html language=enus -->
## TOPIC 00016: Configuring Email Server Settings

- bundle_id: `volume-license-manager`
- source_path: `configuring-email-server-settings.html`
- source_url: https://docs-be.ni.com/bundle/volume-license-manager/raw/resource/enus/configuring-email-server-settings.html
- document_id: `volume-license-manager`
- page_type: `leaf`
- content_type: `task`
- source_description: Enable the ability to send email from within NI VLM through an SMTP server on which you have an account. NI VLM uses the email server for features such as administrator notifications, emailing disconnected or home licenses to clients, and emailing clients when permission requests are handled. NI VLM

### Configuring Email Server Settings

Enable the ability to send email from within NI VLM through an SMTP server on which
 you have an account. NI VLM uses the email server for features such as administrator
 notifications, emailing disconnected or home licenses to clients, and emailing clients when
 permission requests are handled.

NI VLM uses the SMTP email server for the following features:

- Administrator notifications
- Emailing clients from within NI VLM
- Emailing disconnected and home licenses to clients
- Emailing clients when permission requests are handled

Note

- Before configuring the email server, ensure that Full
 Name and Email exist in Custom
 Fields.
- You may need to contact your network administrator to obtain SMTP server
 settings.

1. Select Tools»Preferences.
2. Select Email Server in the navigation tree.
3. In the General section, set Enable email to
 Yes.
4. In the Outgoing Mail Server Information section, enter the SMTP server address
 in the Server Address box. You can optionally specify a
 port number, for example, smtp.example.com:465. The default
 port is 25 if you are not using SSL/TLS encryption. If you are using SSL/TLS
 encryption, the default port is 465.
5. Select whether to enable encryption in the Server requires encrypted
 connection setting.
6. If the SMTP server requires authentication, enter your SMTP server
 Username and Password.
7. Enter the sender's Name and
 Email. You can enter the same information as the General»Administrator Information setting, or you can specify a different name and email
 address.
8. In the Options section, select Yes in Copy
 the administrator on every email sent by NI VLM to send a copy
 of each email that NI VLM sends to the person specified in the General»Administrator Information setting.
9. In the Client Communications section, select Yes to
 automatically send clients an email when permission requests are either accepted
 or rejected.
10. Click Send Test Email to test the email server
 settings. 
 In the dialog box that appears, you can either use the existing
 administrator email address, if shown, or enter another email address at
 which you want to receive the test email.
 Click Send.

Parent topic:

Configuring NI VLM Preferences

<!--NI_TOPIC bundle=volume-license-manager path=configuring-general-settings.html language=enus -->
## TOPIC 00017: Configuring General Settings

- bundle_id: `volume-license-manager`
- source_path: `configuring-general-settings.html`
- source_url: https://docs-be.ni.com/bundle/volume-license-manager/raw/resource/enus/configuring-general-settings.html
- document_id: `volume-license-manager`
- page_type: `leaf`
- content_type: `concept`
- source_description: Configure the General settings to determine volume license server start-up state, NI VLM server ports, administrator contact information, backup location, group settings, permission request settings, and VLA Log settings. Server SettingsStart volume license server on system start—Select Yes to start

### Configuring General Settings

Configure the General settings to determine volume license server start-up state, NI
 VLM server ports, administrator contact information, backup location, group settings,
 permission request settings, and VLA Log settings.

#### Server Settings

- Start volume license server on system start —Select
 Yes to start the volume license server when the
 system starts.
- Main Licensing Port—You may need to change the Main Licensing Port if you are running other
 volume license servers on this computer or have a firewall enabled or any other
 application is using currently configured ports. Note You will need to set up
 client machines to point to the new port.
- Communication Port—You may need to change the Communication Port if you have a firewall enabled
 or any other application is using currently configured ports.

#### Administrator Information

- Administrator Information—Enter administrator information, including full name, email, phone,
 and URL. This information is included in any Volume License Installers you
 create and is presented to clients in NI License Manager. The email address you
 specify here also is used if you choose to copy the administrator when emailing
 clients.

#### Backup and Restore

- Default Backup Location—Set the default location to store NI VLM backup files.



 It is recommended that you change the path to a network location or a removable



 drive. This setting is used by the Backup and Restore Wizard .

#### Groups

- Visibility—Select whether group visibility should be a system-wide setting. You can select
 Public , Private , or
 Set Individually . This setting is used while managing
 groups.
- Permission Request Handling—Select whether group permission request handling



 should be a system-wide setting. You can select



 Automatic , Manual , or



 Set Individually . This setting is used in Handling Permission Requests .

#### Miscellaneous Settings

- Automatically handle legacy permission requests —Select



 Yes to allow NI VLM to handle legacy permission



 requests automatically. Legacy permission requests are those generated by Volume



 License Installers created with NI VLM 2. x or earlier.
- Automatically handle client information-only



 requests —Select Yes to allow NI VLM to handle



 permission requests that include only client information.
- Automatically send VLA Log to NI —Select



 Yes to automatically send the VLA Log to NI, as



 necessary. The VLA Log contains usage information of NI VLM-controlled software,



 such as check-in and check-out events, along with relevant client information.



 If select No , you will need to regularly send your VLA



 Log to NI in accordance with your license agreement.

Parent topic:

Configuring NI VLM Preferences

<!--NI_TOPIC bundle=volume-license-manager path=configuring-ni-vlm-ports.html language=enus -->
## TOPIC 00018: Configuring NI VLM Ports

- bundle_id: `volume-license-manager`
- source_path: `configuring-ni-vlm-ports.html`
- source_url: https://docs-be.ni.com/bundle/volume-license-manager/raw/resource/enus/configuring-ni-vlm-ports.html
- document_id: `volume-license-manager`
- page_type: `leaf`
- content_type: `concept`
- source_description: You can change two ports on the volume license server–the Main Licensing Port and the Communication Port. Ensure that any firewalls allow communication on the license server machine and on client machines, on the Main Licensing Port, and on the Communication Port. Also ensure that no other programs

### Configuring NI VLM Ports

You can change two ports on the volume license server–the [Main Licensing Port](glossary.html#GUID-BD309744-95F6-4B4A-9381-0F22348BB3E8) and the [Communication Port](glossary.html#GUID-E2565F21-77D4-41FB-B264-0053586661D9).

Note

#### Setting NI VLM Port
 Numbers

Complete the following steps to change the Main Licensing Port and Communication Port
 of the volume license server.

1. Select the Tools»Preferences menu item.
2. Select General on the navigation tree.
3. Enter the port you want to use in the Main Licensing Port 
 option. Ports range from 1-64000, inclusive. Note If the Main Licensing Port is
 not set to the default value of 27000, clients need to set both the server
 name and Main Licensing Port number in NI License Manager. The Volume
 License Installer wizard automatically configures client machines to use the
 Main Licensing Port.
4. Enter the port number you want to use in the Communication
 Port option. You do not need to change this port unless there is
 a conflict or a firewall on the license server. If blank, the volume license
 server randomly chooses a port each time the server starts.
5. Click OK .

If you change the Main Licensing Port after it has been set, each client must
 update the port in their copy of NI License Manager. For more information on
 changing server ports on client machines, refer to Using a Network License
 Server in NI License Manager Help, which you
 can access from Help»Contents menu item in NI License Manager.

Parent topic:

Configuring General Settings

Related tasks:

- Specifying License Ports and Administrator Information

<!--NI_TOPIC bundle=volume-license-manager path=configuring-ni-vlm-preferences.html language=enus -->
## TOPIC 00019: Configuring NI VLM Preferences

- bundle_id: `volume-license-manager`
- source_path: `configuring-ni-vlm-preferences.html`
- source_url: https://docs-be.ni.com/bundle/volume-license-manager/raw/resource/enus/configuring-ni-vlm-preferences.html
- document_id: `volume-license-manager`
- page_type: `leaf`
- content_type: `concept`
- source_description: To configure volume license server settings, select Tools Preferences . You can configure the following settings:

### Configuring NI VLM Preferences

To configure volume license server settings, select Tools»Preferences. You can configure the following settings:

- [Configuring General Settings](configuring-general-settings.html) Configure the General settings to determine volume license server start-up state, NI VLM server ports, administrator contact information, backup location, group settings, permission request settings, and VLA Log settings.
- [Setting Overdraft Policies](setting-overdraft-policies.html) Select whether you want to enable overdraft in order to add new seats to your volume license agreement automatically and pay for them later. You can also specify the amount of overdraft and set pay-as-you-go.
- [Configuring Email Server Settings](configuring-email-server-settings.html) Enable the ability to send email from within NI VLM through an SMTP server on which you have an account. NI VLM uses the email server for features such as administrator notifications, emailing disconnected or home licenses to clients, and emailing clients when permission requests are handled.
- [Enabling Administrator Notifications](enabling-administrator-notifications.html) Enable or disable administrator notifications, such as notifications for waiting permission requests, agreement renewal alerts, and expiring disconnected or home licenses.
- [Configuring Custom Fields](configuring-custom-fields.html) Use custom fields to store detailed information about clients as needed. These fields automatically appear and can be edited wherever applicable, including in areas such as users, computers, groups, permissions, reports, and more.
- [Selecting the Volume License Agreement Policies](options.html) Configure Volume License Agreement (VLA) policies to manage client permissions for using NI Update Service, sending error reports, and participating in the Customer Experience Improvement Program. These settings allow you to customize client access and data sharing preferences based on organizational requirements.

Parent topic:

Managing the Volume License Server

Related tasks:

- Completing VLM Setup

<!--NI_TOPIC bundle=volume-license-manager path=configuring-overdraft.html language=enus -->
## TOPIC 00020: Configuring Overdraft

- bundle_id: `volume-license-manager`
- source_path: `configuring-overdraft.html`
- source_url: https://docs-be.ni.com/bundle/volume-license-manager/raw/resource/enus/configuring-overdraft.html
- document_id: `volume-license-manager`
- page_type: `leaf`
- content_type: `task`
- source_description: Overdraft is an agreement preference that enables you to use more licenses than the agreement specifies and pay for the licenses later. If you use more licenses than your agreement allows, NI will charge you for the number of licenses exceeded. For more information, refer to the General Purpose Soft

### Configuring Overdraft

*Overdraft* is an agreement preference that enables you to use more
 licenses than the agreement specifies and pay for the licenses later.

Note

Refer to your volume license agreement (VLA) for specific purchasing requirements and
 overdraft licensing options.

You can allow an overdraft of up to two times the number of licenses purchased with
 the agreement. The VLA Log records permissions that exceed the agreed limits, as
 well as the overdraft settings. At the conclusion of the agreement period, you
 submit the log to NI.

1. Select Enable Overdraft if you want to enable overdraft
 or select Disable Overdraft if you do not want to use
 overdraft. 
 Note This setting
 applies to all products in your agreement license file, except those
 products that use concurrent licenses. You must accept the terms and
 conditions notification before you can enable overdraft in NI VLM.
2. If you enable overdraft, complete the following steps: 
 Note 
 You do not need to select pay-as-you-go in order to enable
 overdrafts. If you do not enable pay-as-you-go, you pay for the
 overdrafted licenses when renewing your VLA.
 If you enable pay-as-you-go, the license maintenance is prorated
 when you pay for the license. If you do not enable pay-as-you-go,
 the license maintenance is not prorated. For more information on
 renewing agreements, refer to *Renewing Expired
 Agreements*.
  1. Use the slider to set the overdraft percentage. This percentage is the
 amount of licenses that you can use in addition to your purchased
 agreement licenses.
  2. Check Enable pay-as-you-go if you want to enable
 pay-as-you-go. 
 This setting reminds you when you overdraft licenses to send your VLA
 Log to NI in order to cover the overdraft by purchasing the
 corresponding licenses.

Parent topic:

Completing the VLM Getting Started Wizard

Related concepts:

- Overdraft
- Renewing Expired Agreements
- Pay-as-You-Go

<!--NI_TOPIC bundle=volume-license-manager path=creating-an-ni-vlm-backup.html language=enus -->
## TOPIC 00021: Creating an NI VLM Backup

- bundle_id: `volume-license-manager`
- source_path: `creating-an-ni-vlm-backup.html`
- source_url: https://docs-be.ni.com/bundle/volume-license-manager/raw/resource/enus/creating-an-ni-vlm-backup.html
- document_id: `volume-license-manager`
- page_type: `leaf`
- content_type: `concept`
- source_description: Complete the following steps to backup NI VLM data: Set a default backup directory from the ToolsPreferences menu item. In NI VLM, select the FileBackup/Restore NI VLM menu item to launch the Backup and Restore Wizard. Select Back up NI VLM. If you want to use a directory other than the default dire

### Creating an NI VLM Backup

Complete the following steps to backup NI VLM data:

1. Set a default backup directory from the Tools»Preferences menu item.
2. In NI VLM, select the File»Backup/Restore NI VLM menu item to launch the Backup and Restore Wizard.
3. Select Back up NI VLM .
4. If you want to use a directory other than the default directory you set in Step 1, click the
 ellipsis ( ) in the Directory section to launch a folder browser
 and select the directory where you want to store your backup file. Note Selecting a
 directory other than the default will not change the default directory set
 in Tools»Preferences.
5. In the Filename section, you can either accept or modify



 the generated filename or type your own filename.
6. Click Back Up to create the backup file. Note Once the backup completes,
 you can click the filename to open the directory that contains the backup
 file.
7. Click Finish to exit the Backup and Restore Wizard.

Parent topic:

Backing up and Restoring NI VLM Data

<!--NI_TOPIC bundle=volume-license-manager path=creating-client-activity-reports.html language=enus -->
## TOPIC 00022: Creating Client Activity Reports

- bundle_id: `volume-license-manager`
- source_path: `creating-client-activity-reports.html`
- source_url: https://docs-be.ni.com/bundle/volume-license-manager/raw/resource/enus/creating-client-activity-reports.html
- document_id: `volume-license-manager`
- page_type: `leaf`
- content_type: `concept`
- source_description: Use this report to determine how a specified client uses licenses. This report shows how many hours the specified client used each license. Complete the following steps to create a client activity report: Launch NI Volume License Manager and select ReportsClient Activity. In the Date Range section,

### Creating Client Activity Reports

Use this report to determine how a specified client uses licenses. This report shows



 how many hours the specified client used each license.

Complete the following steps to create a client activity report:

1. Launch NI Volume License Manager and select Reports»Client Activity .
2. In the Date Range section, select a start and end



 date.
3. In the Report Parameters section, select the client you



 want to examine.
4. In the Actions section, click Generate



 Report .
5. Select data in the grid to display it in the chart.
6. (Optional) In the Actions section, click



 Export Report and select a format to export the



 report. Refer to Exporting Reports for more information.

The report includes the following information:

- All licenses that the specified client used during the specified time



 period
- Any licenses that the specified client had permission to during the specified



 time period but did not use

Refer to [Customizing Reports](customizing-reports.html) to learn how to customize NI VLM reports to reflect



 how you want the data to appear.

Parent topic:

Creating Reports

<!--NI_TOPIC bundle=volume-license-manager path=creating-home-license-files.html language=enus -->
## TOPIC 00023: Creating Home License Files

- bundle_id: `volume-license-manager`
- source_path: `creating-home-license-files.html`
- source_url: https://docs-be.ni.com/bundle/volume-license-manager/raw/resource/enus/creating-home-license-files.html
- document_id: `volume-license-manager`
- page_type: `leaf`
- content_type: `task`
- source_description: Enable a client to install and run NI products included in a volume license agreement on a home computer. A home license is similar to a disconnected license but does not consume a license on the volume license server and is intended for home use only, according to the terms of your volume license a

### Creating Home License Files

Enable a client to install and run NI products included in a volume license agreement
 on a home computer.

A home license is similar to a disconnected license but does not consume a license on the
 volume license server and is intended for home use only, according to the terms of your
 volume license agreement with NI. A home license cannot contain concurrent or debug
 licenses.

Before creating a home license file, you must first add a user or computer and assign any
 appropriate permissions. For more information, refer to *Adding Users or
 Computers*.

1. In the either the Users or Computers
 view, select one computer or user.
2. Click Create Home License.
3. Complete the Home License Wizard.
4. Instruct the client to install the license file on their home machine. 
 Refer to *Installing Home License Files* for more information.

Parent topic:

Using License Files

<!--NI_TOPIC bundle=volume-license-manager path=creating-license-activity-reports.html language=enus -->
## TOPIC 00024: Creating License Activity Reports

- bundle_id: `volume-license-manager`
- source_path: `creating-license-activity-reports.html`
- source_url: https://docs-be.ni.com/bundle/volume-license-manager/raw/resource/enus/creating-license-activity-reports.html
- document_id: `volume-license-manager`
- page_type: `leaf`
- content_type: `concept`
- source_description: Use this report to determine how clients use a specified license. This report shows how many hours each client used the specified license. Complete the following steps to create a license activity report: Launch NI Volume License Manager and select ReportsLicense Activity. In the Date Range section,

### Creating License Activity Reports

Use this report to determine how clients use a specified license. This report shows



 how many hours each client used the specified license.

Complete the following steps to create a license activity report:

1. Launch NI Volume License Manager and select Reports»License Activity .
2. In the Date Range section, select a start and end



 date.
3. In the Report Parameters section, select the license you



 want to examine.
4. In the Actions section, click Generate



 Report .
5. Select data in the grid to display it in the chart.
6. (Optional) In the Actions section, click



 Export Report and select a format to export the



 report. Refer to Exporting Reports for more information.

The report includes the following information:

- All clients that used the specified license during the specified time



 period
- Any clients that had permission to the specified license during the specified



 time period but did not use it

Note

Refer to [Customizing Reports](customizing-reports.html) to learn how to customize NI VLM reports to reflect



 how you want the data to appear.

Parent topic:

Creating Reports

<!--NI_TOPIC bundle=volume-license-manager path=creating-license-allocation-concurrent-reports.html language=enus -->
## TOPIC 00025: Creating License Allocation (Concurrent) Reports

- bundle_id: `volume-license-manager`
- source_path: `creating-license-allocation-concurrent-reports.html`
- source_url: https://docs-be.ni.com/bundle/volume-license-manager/raw/resource/enus/creating-license-allocation-concurrent-reports.html
- document_id: `volume-license-manager`
- page_type: `leaf`
- content_type: `concept`
- source_description: Use this report to determine how parts of your organization used managed concurrent licenses. This report shows how many hours each portion of your organization used each license, so that you can allocate costs accordingly. Complete the following steps to create a license allocation report: Launch N

### Creating License Allocation (Concurrent) Reports

Use this report to determine how parts of your organization used managed concurrent



 licenses. This report shows how many hours each portion of your organization used



 each license, so that you can allocate costs accordingly.

Complete the following steps to create a license allocation report:

1. Launch NI Volume License Manager and select Reports»License Allocation (Concurrent) .
2. In the Date Range section, select a start and end



 date.
3. In the Report Parameters section, select the custom field



 on which you want to base cost allocation.
4. In the Actions section, click Generate



 Report .
5. (Optional) In the Actions section, click



 Export Report and select a format to export the



 report. Refer to Exporting Reports for more information.

More information about the report:

- Usage by clients that do not have a custom field value specified is displayed as



 "(Blank)".
- Clients always reflect their current custom field value. For example, if a



 client's department changes during the year, its usage counts against its new



 department for the entire year.

Note

Refer to [Customizing Reports](customizing-reports.html) to learn how to customize NI VLM reports to reflect



 how you want the data to appear.

Parent topic:

Creating Reports

<!--NI_TOPIC bundle=volume-license-manager path=creating-license-allocation-reports.html language=enus -->
## TOPIC 00026: Creating License Allocation Reports

- bundle_id: `volume-license-manager`
- source_path: `creating-license-allocation-reports.html`
- source_url: https://docs-be.ni.com/bundle/volume-license-manager/raw/resource/enus/creating-license-allocation-reports.html
- document_id: `volume-license-manager`
- page_type: `leaf`
- content_type: `concept`
- source_description: Use this report to determine how parts of your organization used non-concurrent licenses. This report shows, over time, how many seats each portion of your organization used, so that you can allocate costs accordingly. Complete the following steps to create a license allocation report: Launch NI Vol

### Creating License Allocation Reports

Use this report to determine how parts of your organization used non-concurrent



 licenses. This report shows, over time, how many seats each portion of your



 organization used, so that you can allocate costs accordingly.

Complete the following steps to create a license allocation report:

1. Launch NI Volume License Manager and select Reports»License Allocation .
2. In the Date Range section, select a start and end



 date.
3. In the Report Parameters section, select the custom field



 on which you want to base cost allocation.
4. In the Actions section, click Generate



 Report .
5. (Optional) In the Actions section, click



 Export Report and select a format to export the



 report. Refer to Exporting Reports for more information.

More information about the report:

- Seats assigned to clients that do not have a custom field value specified are



 displayed as "(Blank)"
- Seats not assigned to a client are displayed as "(Unassigned)"
- Clients always reflect their current custom field value. For example, if a



 client's department changes during the year, its assignment counts against its



 new department for the entire year.

Note

Refer to [Customizing Reports](customizing-reports.html) to learn how to customize NI VLM reports to reflect



 how you want the data to appear.

Parent topic:

Creating Reports

<!--NI_TOPIC bundle=volume-license-manager path=creating-named-user-eula-compliance-reports.html language=enus -->
## TOPIC 00027: Creating Named-User EULA Compliance Reports

- bundle_id: `volume-license-manager`
- source_path: `creating-named-user-eula-compliance-reports.html`
- source_url: https://docs-be.ni.com/bundle/volume-license-manager/raw/resource/enus/creating-named-user-eula-compliance-reports.html
- document_id: `volume-license-manager`
- page_type: `leaf`
- content_type: `concept`
- source_description: Use this report to determine whether any clients used a named-user license on more than three computers. You can use this information to help stay in compliance with the NI Software License Agreement. Complete the following steps to create a named-user EULA compliance report: Launch NI Volume Licens

### Creating Named-User EULA Compliance Reports

Use this report to determine whether any clients used a named-user license on more than three
 computers. You can use this information to help stay in compliance with the NI
 Software License Agreement.

Complete the following steps to create a named-user EULA compliance report:

1. Launch NI Volume License Manager and select Reports»Named-User EULA Compliance .
2. In the Date Range section, select a start and end




 date.
3. In the Actions section, click Generate




 Report .
4. (Optional) In the Actions section, click




 Export Report and select a format to export the




 report. Refer to Exporting Reports for more information.

Refer to [Customizing Reports](customizing-reports.html) to learn how to customize NI VLM reports to reflect




 how you want the data to appear.

Parent topic:

Creating Reports

<!--NI_TOPIC bundle=volume-license-manager path=creating-reports.html language=enus -->
## TOPIC 00028: Creating Reports

- bundle_id: `volume-license-manager`
- source_path: `creating-reports.html`
- source_url: https://docs-be.ni.com/bundle/volume-license-manager/raw/resource/enus/creating-reports.html
- document_id: `volume-license-manager`
- page_type: `leaf`
- content_type: `concept`
- source_description: Use the NI VLM Reports view to create activity, utilization, allocation, and compliance reports. License Activity shows how many hours each client used the specified license. Client Activity shows how many hours a specified client used each license. Seat Utilization shows how many seats of a specifi

### Creating Reports

Use the NI VLM Reports view to create
 activity, utilization, allocation, and compliance
 reports.

- License Activity shows how many hours each client used the specified



 license.
- Client Activity shows how many hours a specified client used each



 license.
- Seat Utilization shows how many seats of a specified license each



 client used over time and provides detailed information about any



 overdrafts.
- Seat Utilization (Concurrent) shows how many seats of a specified



 license each client used over time and whether any clients were unable to check



 out the license because no seats were available.
- License Allocation shows, over time, how many seats each portion of



 your organization used, so that you can allocate costs accordingly.
- License Allocation (Concurrent) shows how many hours each portion of



 your organization used each license, so that you can allocate costs



 accordingly.
- Named-User EULA Compliance shows any instances of a client using a



 named-user license on more than three computers.

Parent topic:

Managing, Monitoring, and Communicating with Clients

<!--NI_TOPIC bundle=volume-license-manager path=creating-seat-utilization-concurrent-reports.html language=enus -->
## TOPIC 00029: Creating Seat Utilization (Concurrent) Reports

- bundle_id: `volume-license-manager`
- source_path: `creating-seat-utilization-concurrent-reports.html`
- source_url: https://docs-be.ni.com/bundle/volume-license-manager/raw/resource/enus/creating-seat-utilization-concurrent-reports.html
- document_id: `volume-license-manager`
- page_type: `leaf`
- content_type: `concept`
- source_description: Use this report to determine how many seats of a specified concurrent license each client used over time. This report shows how many seats of the specified license clients used over time and whether any clients were unable to check out the license because no seats were available. Complete the follow

### Creating Seat Utilization (Concurrent) Reports

Use this report to determine how many seats of a specified concurrent license each



 client used over time. This report shows how many seats of the specified license



 clients used over time and whether any clients were unable to check out the license



 because no seats were available.

Complete the following steps to create a seat utilization report:

1. Launch NI Volume License Manager and select Reports»Set Utilization (Concurrent) .
2. In the Date Range section, select a start and end



 date.
3. In the Report Parameters section, select the license you



 want to examine.
4. In the Actions section, click Generate



 Report .
5. (Optional) In the Actions section, click



 Export Report and select a format to export the



 report. Refer to Exporting Reports for more information.

Note

- Denied checkouts for unmanaged concurrent licenses are displayed by
 username.
- If a client has permission to multiple licenses that grant access to a
 particular NI software product, NI VLM records a denied checkout for each
 denied license when the client tries to use that software product.

Refer to [Customizing Reports](customizing-reports.html) to learn how to customize NI VLM reports to reflect



 how you want the data to appear.

Parent topic:

Creating Reports

<!--NI_TOPIC bundle=volume-license-manager path=creating-seat-utilization-reports.html language=enus -->
## TOPIC 00030: Creating Seat Utilization Reports

- bundle_id: `volume-license-manager`
- source_path: `creating-seat-utilization-reports.html`
- source_url: https://docs-be.ni.com/bundle/volume-license-manager/raw/resource/enus/creating-seat-utilization-reports.html
- document_id: `volume-license-manager`
- page_type: `leaf`
- content_type: `concept`
- source_description: Use this report to determine how many seats of a specified non-concurrent license each client used over time. This report shows how many seats of the specified license clients used over time and provides detailed information about any overdrafts. Complete the following steps to create a seat utiliza

### Creating Seat Utilization Reports

Use this report to determine how many seats of a specified non-concurrent license



 each client used over time. This report shows how many seats of the specified



 license clients used over time and provides detailed information about any



 overdrafts.

Complete the following steps to create a seat utilization report:

1. Launch NI Volume License Manager and select Reports»Set Utilization .
2. In the Date Range section, select a start and end



 date.
3. In the Report Parameters section, select the license you



 want to examine.
4. In the Actions section, click Generate



 Report .
5. (Optional) In the Actions section, click



 Export Report and select a format to export the



 report. Refer to Exporting Reports for more information.

Refer to [Customizing Reports](customizing-reports.html) to learn how to customize NI VLM reports to reflect



 how you want the data to appear.

Parent topic:

Creating Reports

<!--NI_TOPIC bundle=volume-license-manager path=creating-volume-license-installers.html language=enus -->
## TOPIC 00031: Creating Volume License Installers

- bundle_id: `volume-license-manager`
- source_path: `creating-volume-license-installers.html`
- source_url: https://docs-be.ni.com/bundle/volume-license-manager/raw/resource/enus/creating-volume-license-installers.html
- document_id: `volume-license-manager`
- page_type: `leaf`
- content_type: `concept`
- source_description: Use the Volume License Installer Wizard to create a Volume License Installer for your NI products. Benefits The Volume License Installer Wizard modifies the installer to offer the following benefits: Automatically configures client machines to connect to NI Volume License Manager (NI VLM) for licens

### Creating Volume License Installers

Use the Volume License Installer Wizard to create a Volume License Installer for your
 NI products.

#### Benefits

The Volume License Installer Wizard modifies the
 installer to offer the following benefits:

- Automatically configures client machines to
 connect to NI Volume License Manager (NI VLM) for
 licensing
- Takes media management responsibilities out of
 the hands of clients
- Collects custom field information from clients
 that you can access through reporting
- Allows clients to request permission to join
 groups
- Installs the correct software in
 multiple-product suites for each client, based on
 the client's permissions
- Provides administrator contact information to
 clients for licensing support Note The
 first page of the Volume License Installer Wizard
 displays your current administrator information.
 Refer to [Setting Administrator Information](setting-administrator-information.html) for
 information about changing this
 information.

When a client runs a Volume License
 Installer, the installer automatically contacts NI
 VLM to retrieve updated versions of the following
 information:

- Group information
- Administrator information
- Serial numbers
- Client information and permissions

#### Using the Volume License Installer Wizard

Complete the following general steps to create
 and distribute Volume License Installers:

Note

Managing Groups

1. Select the Tools»Create Volume License Installer menu item to start the wizard.
2. Specify software source and destination paths and
 give your Volume License Installer a
 name .
3. Specify the distribution method for the Volume
 License Installer .
4. Specify how client machines should be configured
 when running the Volume License
 Installer .
5. Specify the permission request behavior for the
 Volume License Installer .
6. Specify which products to include in the Volume
 License Installer .
7. Review your selections for the Volume License
 Installer .
8. Build your Volume License Installer .
9. Review the Frequently Asked Questions and then
 distribute your new Volume License
 Installer.

Distribute the modified installer within
 your organization either by using a shared network
 drive or copying this new product installer to a
 CD, DVD, or USB drive. Because the use of this
 software is always governed by NI VLM, you can
 freely distribute the installer.

#### Best Practices

Consider using these NI VLM best practices for more efficient use of your time spent




 administering volume-licensed software from NI.

#### Using Groups to Obtain Permissions

Use Groups instead of explicitly granting licenses to clients to increase




 proficiency. Using groups allows clients to easily request permission to access




 their NI software products. Additionally, groups allow you to easily and quickly




 assign multiple permissions to clients. Refer to [Managing Groups](managing-groups.html#GUID-52AA0D4F-AD68-43E2-9B2C-0722E49E07A8) for more information on groups.

#### Creating One Volume License Installer per
 Media

Because the software within a Volume License
 Installer is installed based on the client's
 current permissions plus any permissions they are
 requesting, typically you need to create only one
 Volume License Installer per source. This feature
 works with multiple-product suites released in
 August 2010 or later.

For example, the
 following screenshot shows an installation by a
 client with permissions to LabVIEW Professional
 Development System, Vision Development Module, and
 NI SoftMotion Module in NI VLM. The client can
 select other packages to install in evaluation
 mode.

[IMAGE alt='image' src='GUID-911E0B6B-12B3-40DB-B2D4-51E2197530EB-a5.png']

Parent topic:

Using Volume License Servers and Installers

Related tasks:

- Completing VLM Setup

<!--NI_TOPIC bundle=volume-license-manager path=customizing-reports.html language=enus -->
## TOPIC 00032: Customizing Reports

- bundle_id: `volume-license-manager`
- source_path: `customizing-reports.html`
- source_url: https://docs-be.ni.com/bundle/volume-license-manager/raw/resource/enus/customizing-reports.html
- document_id: `volume-license-manager`
- page_type: `leaf`
- content_type: `concept`
- source_description: You can customize NI VLM reports to reflect how you want the data to appear. To customize your reports, first generate the report and then click the Options tab to display the options you can apply. The options available depend on the type of report you selected, as described in the following table.

### Customizing Reports

You can customize NI VLM reports to reflect how you want the data to appear.

To customize your reports, first generate the report and then click the



 Options tab to display the options you can apply. The



 options available depend on the type of report you selected, as described in the



 following table.

| Section | Option | Description |
| --- | --- | --- |
| Data View | Months, Days | Select Months if you want a monthly summary of the data. Select Days if you want a more granular view of the data. |
| Chart | All Days, Weekdays Only | When Days is selected in the Data View section, you can use these options to control which days are charted. Select All Days to chart every day within the selected date range. If you typically do not have usage on weekends, select Weekdays Only to limit your view. |
| Grid | Whole Numbers, Decimal Numbers | Select Whole Numbers to display numbers without any decimal places. Select Decimal Numbers to display numbers with one decimal place. These options effect only how data is displayed in the grid and do not effect how the numbers are calculated. |
| Sort by Total | If you want to sort the data by the value in the Total column, click Sort by Total. |  |
| Show Filter Panel | Click Show Filter Panel to enable filtering by custom field values. |  |
| Show Group Panel | Click Show Group Panel to enable grouping in the grid. Refer to Grouping Data for information. |  |
| Export | Chart and Grid, Chart Only, Grid Only | Use the Export options to select how you want data exported to file. You can export the chart only, the grid only, or both. When you export a grid with group rows or master detail rows, the file includes all grouped data and master detail data. Refer to Exporting Reports for more information. |

Parent topic:

Creating Reports

<!--NI_TOPIC bundle=volume-license-manager path=deleting-custom-fields.html language=enus -->
## TOPIC 00033: Deleting Custom Fields

- bundle_id: `volume-license-manager`
- source_path: `deleting-custom-fields.html`
- source_url: https://docs-be.ni.com/bundle/volume-license-manager/raw/resource/enus/deleting-custom-fields.html
- document_id: `volume-license-manager`
- page_type: `leaf`
- content_type: `concept`
- source_description: Complete the following steps to delete a custom field: Select the ToolsPreferences menu item. Select Custom Fields in the navigation tree. Select one or more fields on the list and click Delete. Deleting a field deletes all data associated with that field.NI VLM uses Full Name and Email for emailing

### Deleting Custom Fields

Complete the following steps to delete a custom field:

1. Select the Tools»Preferences menu item.
2. Select Custom Fields in the navigation tree.
3. Select one or more fields on the list and click Delete . Note Deleting a field deletes all data associated
 with that field.NI VLM uses Full Name and Email for emailing
 clients, in reports, and to help license
 administrators. Deleting these fields may disable
 these features and is not recommended.
4. Click Yes to confirm the deletion.
5. Click Save when you are finished.

Parent topic:

Configuring Custom Fields

<!--NI_TOPIC bundle=volume-license-manager path=editing-custom-fields.html language=enus -->
## TOPIC 00034: Editing Custom Fields

- bundle_id: `volume-license-manager`
- source_path: `editing-custom-fields.html`
- source_url: https://docs-be.ni.com/bundle/volume-license-manager/raw/resource/enus/editing-custom-fields.html
- document_id: `volume-license-manager`
- page_type: `leaf`
- content_type: `concept`
- source_description: Complete the following steps to rename a custom field: Select the ToolsPreferences menu item. Select Custom Fields in the navigation tree. Click in required field and make changes. All data associated with a renamed field is retained.NI VLM uses Full Name and Email for emailing clients, in reports,

### Editing Custom Fields

Complete the following steps to rename a custom field:

1. Select the Tools»Preferences menu item.
2. Select Custom Fields in the navigation tree.
3. Click in required field and make changes. Note All data associated with a renamed field is retained.NI VLM uses Full Name and Email for emailing clients, in reports,
 and to help license administrators. Renaming these fields may
 disable these features and is not recommended.
4. Click Save when you are finished.

Parent topic:

Configuring Custom Fields

<!--NI_TOPIC bundle=volume-license-manager path=enabling-administrator-notifications.html language=enus -->
## TOPIC 00035: Enabling Administrator Notifications

- bundle_id: `volume-license-manager`
- source_path: `enabling-administrator-notifications.html`
- source_url: https://docs-be.ni.com/bundle/volume-license-manager/raw/resource/enus/enabling-administrator-notifications.html
- document_id: `volume-license-manager`
- page_type: `leaf`
- content_type: `concept`
- source_description: Enable or disable administrator notifications, such as notifications for waiting permission requests, agreement renewal alerts, and expiring disconnected or home licenses.You can set up NI VLM to receive certain notifications about important events, such as:The NI VLM user interface has been open fo

### Enabling Administrator Notifications

Enable or disable administrator notifications, such as notifications for waiting
 permission requests, agreement renewal alerts, and expiring disconnected or home
 licenses.

You can set up NI VLM to receive certain notifications about important events, such as:

- The NI VLM user interface has been open for extended period of time. Closing NI



 VLM applies any changes and allows the server to perform important operations



 such as automatic permission request handling.
- Contract Expiration is imminent. Timely contract renewal ensures uninterrupted



 operation of NI VLM.
- Backup is too old. Keeping a more current backup ensures that recent changes in



 NI VLM are not lost.
- Disconnected or home licenses are expiring soon. Clients may not be able to run



 NI software if they are using expired disconnected or home licenses.
- Permission Requests are pending. Processing permission requests promptly ensures



 clients have access to the NI software they need.

#### Enabling Notifications

Complete the following steps to enable
 administrator notifications:

1. Ensure that you have email enabled in the Preferences»Email Server setting.
2. In the Preferences»Notifications setting, select the notifications
 you want to receive.

#### Types of Messages

When a notification is triggered, NI VLM automatically emails the person specified in the General»Administrator Information setting. At most, one email is sent per day. Some notifications also
 display a pop-up alert in the lower right corner of the screen if a notification is
 triggered while NI VLM is open.

The following table describes the behavior of each notification.

| Notification | Trigger Condition | Notes |
| --- | --- | --- |
| NI VLM Left Open | NI VLM left open for 4 hours | This notification also shows a popup alert. |
| Service Expiring | Service expiring within 60 days | You will be notified when 60, 30, 14, and 7 or fewer days remain. |
| Backup Needed | NI VLM backup older than 30 days | You will be notified every 30 days. |
| Disconnected Licenses Expiring | Disconnected licenses expiring within 14 days | — |
| Home Licenses Expiring | Home licenses expiring within 14 days | — |
| Permission Requests Pending | Requests in Permission Requests | This notification also shows a popup alert. |

Parent topic:

Configuring NI VLM Preferences

<!--NI_TOPIC bundle=volume-license-manager path=entering-required-agreement-license-file-data.html language=enus -->
## TOPIC 00036: Entering Required Agreement License File Data

- bundle_id: `volume-license-manager`
- source_path: `entering-required-agreement-license-file-data.html`
- source_url: https://docs-be.ni.com/bundle/volume-license-manager/raw/resource/enus/entering-required-agreement-license-file-data.html
- document_id: `volume-license-manager`
- page_type: `leaf`
- content_type: `concept`
- source_description: NI needs the following information in order to process your request for a new agreement license file. Complete the form, adding the following information. All fields, except Comments, are required. The Comments field is required only if you select a custom license model.Administrator Name—Enter the

### Entering Required Agreement License File Data

NI needs the following information in order to process your request for a new



 agreement license file.

1. Complete the form, adding the following information. All fields, except



 Comments , are required. The



 Comments field is required only if you select a



 custom license model.
  - Administrator Name —Enter the



 full name of the volume license administrator–the person whom NI should



 contact if there are any issue with this license



 request.
  - Administrator Email —Enter



 the email address of the volume license administrator. NI will send the



 license file to this



 address.
  - Company —Enter the name of the



 company on the volume license agreement.
  - Service



 ID —Enter the Service ID of the volume license agreement.



 You can find your Service ID on your sales order acknowledgement (SOA),



 any quotes you may have received, and in your Welcome email. If you



 cannot find your Service ID, contact your NI sales



 representative.
  - License Model —Select the license model that you want to use with your
 volume license agreement. You can select All
 Named-User , All Computer-Based ,
 and Custom - Specify in Comments (Examples in
 Help) .
  - Comments —Enter a custom license model and any other comments you might
 have. For
 example: LabVIEW Professional: 10 seats named-user and 2 seats computer-based
DIAdem Full: All named-user
TestStand Development: All computer-based Note Deployment licenses are available as computer-based licenses
 only.
2. Click Send or Save , depending on



 whether you selected to automatically request a new agreement license file or



 whether you selected to save the information to a text file and send it in



 manually.

Parent topic:

Obtaining or Installing an Agreement License File

<!--NI_TOPIC bundle=volume-license-manager path=expanding-and-collapsing-rows.html language=enus -->
## TOPIC 00037: Expanding and Collapsing Rows

- bundle_id: `volume-license-manager`
- source_path: `expanding-and-collapsing-rows.html`
- source_url: https://docs-be.ni.com/bundle/volume-license-manager/raw/resource/enus/expanding-and-collapsing-rows.html
- document_id: `volume-license-manager`
- page_type: `leaf`
- content_type: `concept`
- source_description: To expand or collapse a row, complete one of the following actions, depending on the row type: All Rows Click the row's expand button. Click once on the row and press <Ctrl-plus> on your keyboard to expand the row or <Ctrl-minus> to collapse the row. Click once on the row and press the right arrow o

### Expanding and Collapsing Rows

[IMAGE alt='image' src='GUID-BC84D94A-6967-425B-8AA1-F2FD6DCFDA7E-a5.png']

To expand or collapse a row, complete one of the following actions, depending on the



 row type:

#### All Rows

- Click the row's expand button.
- Click once on the row and press <Ctrl-plus> on your keyboard to expand the



 row or <Ctrl-minus> to collapse the row.
- Click once on the row and press the right arrow on your keyboard to expand the



 row or the left arrow to collapse the row.

#### Grouped Rows

- Double-click the row.
- To expand or collapse all rows, right-click the panel at the top of the view. In



 the context menu, select Expand All or



 Collapse All respectively.

Parent topic:

Working With the VLM User Interface

<!--NI_TOPIC bundle=volume-license-manager path=exporting-current-permissions.html language=enus -->
## TOPIC 00038: Exporting Current Permissions

- bundle_id: `volume-license-manager`
- source_path: `exporting-current-permissions.html`
- source_url: https://docs-be.ni.com/bundle/volume-license-manager/raw/resource/enus/exporting-current-permissions.html
- document_id: `volume-license-manager`
- page_type: `leaf`
- content_type: `concept`
- source_description: You can run NI VLM with a command line option to export a list of current permissions to a file. You cannot run command line options while the NI VLM user interface is running. To export current permissions, run NI Volume License Manager with the following command line option: NiVlm.exe /exportClien

### Exporting Current Permissions

You can run NI VLM with a command line option to export a list of current permissions



 to a file.

Note

To export current permissions, run NI Volume License Manager with the following



 command line option:

```text
        NiVlm.exe /exportClientPermissions <filepath>
      
```

Example: "C:\Program Files\National Instruments\Volume License



 Manager\NiVlm.exe" /exportClientPermissions C:\temp\myFile.csv

The resulting comma-separated value (CSV) file contains client names, client custom



 field values, and a license permissions.

If a client has permissions to multiple licenses, then the exported CSV file will



 contain a line for every license permission, and all other client-related data is



 duplicated. If a client has no permissions, then there will be a single row for that



 client without license information. If a license has no assigned permissions, the



 license will not be listed in the file.

License values specify the type and concurrency model, in parenthesis, for the four
 possibilities: Named-User, Named-User Concurrent,
 Computer-Based, and Computer-Based Concurrent.

Example contents:

```text
Client,Client Type,Computer ID,Full Name,Cost Center,Department,Manager,License
jsmith,User,,John Smith,4205,R&D,Jack Jones,LabVIEW 2012 Full Development System (Named-User)
SMITH,Computer,PMBF-QQ99-XX89-CW8H,John Smith,4205,R&D,Jack Jones,LabVIEW 2012 Full Development System (Computer-Based Concurrent)
jwilliams,User,,Jane Williams,1123,R&D,Jack Jones,
```

Parent topic:

Managing the Volume License Server

Related reference:

- NiVlm.exe Command Reference

<!--NI_TOPIC bundle=volume-license-manager path=exporting-reports.html language=enus -->
## TOPIC 00039: Exporting Reports

- bundle_id: `volume-license-manager`
- source_path: `exporting-reports.html`
- source_url: https://docs-be.ni.com/bundle/volume-license-manager/raw/resource/enus/exporting-reports.html
- document_id: `volume-license-manager`
- page_type: `leaf`
- content_type: `concept`
- source_description: You can export NI VLM reports into the following formats: XLSX (Excel 2007 Format) CSV (Comma Separated Values) HTML—Images are included in a linked filename_files folder. MHT—HTML with embedded images. MHT is supported by Internet Explorer, Firefox (by extension), and Opera. PNG (Image Format) Repo

### Exporting Reports

You can export NI VLM reports into the following formats:

- XLSX (Excel 2007 Format)
- CSV (Comma Separated Values)
- HTML—Images are included in a linked



 filename _files 



 folder.
- MHT—HTML with embedded images. MHT is supported by Internet Explorer, Firefox



 (by extension), and Opera.
- PNG (Image Format)

Reports are exported similarly to how they are displayed in NI VLM, with the same



 formatting, sorting, and sizing. When you export a grid with group rows or master



 detail rows, the file includes all grouped data and master detail data. To change



 how the report is displayed, click the Options tab and



 customize your report.

For reports that have a chart, you can control whether the export contains the chart,



 the grid, or both. Refer to [Customizing Reports](customizing-reports.html) for more information.

Note

- The CSV format is a text-only format and cannot contain an export of the
 chart.
- Any data that is filtered out before exporting will not be present in the
 exported file.

Parent topic:

Creating Reports

<!--NI_TOPIC bundle=volume-license-manager path=extended-support-changes.html language=enus -->
## TOPIC 00040: Updates and Changes for VLM Extended Support Versions

- bundle_id: `volume-license-manager`
- source_path: `extended-support-changes.html`
- source_url: https://docs-be.ni.com/bundle/volume-license-manager/raw/resource/enus/extended-support-changes.html
- document_id: `volume-license-manager`
- page_type: `leaf`
- content_type: `concept`
- source_description: Browse updates and changes made in VLM versions on extended support. If you cannot find changes for your version, it might be a more recent version, documented as a new feature. Or, your version might not have included user-facing updates. You can find more information about non-visible changes, suc

### Updates and Changes for VLM Extended Support Versions

Browse updates and changes made in VLM versions
 on extended support.

Note

Release Notes

#### NI VLM 3.2

##### New Features

- Volume license installers — Use volume license installers to deliver packages
 through NI Package Manager.

#### NI VLM 3.1

##### New Features

- Reporting — Use the Reports view to determine how
 licenses are used.
- Administrator Notifications — Use administrator notifications to receive
 important event notifications from NI VLM.
- Email Clients Wizard — Use the Email Clients Wizard to
 email one or more clients.
- Batch Update Custom Fields — Use Batch Update to
 modify a custom field value for multiple users or computers to a single,
 consistent value.
- VLA Log Wizard — Use the VLA Log Wizard to generate and
 send a VLA Log to NI from within NI VLM. You can also set NI VLM to
 automatically send VLA Logs to NI.
- Permission Request Client Notifications — Send emails automatically to
 clients when permission requests are handled.
- Licenses View In-Use Tab — Use the Licenses view to see
 usage for unmanaged concurrent licenses and for clients assigned by IP
 address. You can also see what time an in-use license was checked out.
- VLA Policies — Manage policies across client machines. You can control
 whether clients can use NI Update Service, can send error reports to NI, and
 can enroll in the Customer Experience Improvement Program.
- Export Current Permissions — Run NI VLM with a command line option to export
 a list of current permissions to a file.

<!--NI_TOPIC bundle=volume-license-manager path=filtering-data.html language=enus -->
## TOPIC 00041: Filtering Data

- bundle_id: `volume-license-manager`
- source_path: `filtering-data.html`
- source_url: https://docs-be.ni.com/bundle/volume-license-manager/raw/resource/enus/filtering-data.html
- document_id: `volume-license-manager`
- page_type: `leaf`
- content_type: `concept`
- source_description: To filter data in the current view, complete one of the following actions: Type in the column's Search box (searches within the contents of the column). This box is context-sensitive and can include Search, Select, Select a Date, and so on. Click a column's filter button (visible when mousing over c

### Filtering Data

To filter data in the current view, complete one of the following actions:

- Type in the column's Search box (searches within the contents of the column). Note This box is context-sensitive
 and can include Search,
 Select, Select a Date, and so
 on. [IMAGE alt='image' src='GUID-EFF82510-243D-426E-98D8-73182FAAE401-a5.png']
- Click a column's filter button (visible when mousing over column
 header) (allows advanced filtering for certain
 data types, e.g. date ranges). [IMAGE alt='image' src='GUID-E811E257-4A38-4EE7-B5FB-A7CF1F26D552-a5.png']
- Right-click on a column header and select Show Filter



 Editor for advanced filtering.

When a filter is active, a panel appears at the bottom of the grid that lists the



 current filter. Use the Enable Filter checkbox to



 enable/disable the filter or click the x to clear it



 completely. Click Edit Filter from the filter panel to edit



 the filter. Click the down arrow next to the filter name to display recent filters



 in a drop-down list.

Parent topic:

Working With the VLM User Interface

<!--NI_TOPIC bundle=volume-license-manager path=finishing-the-getting-started-wizard.html language=enus -->
## TOPIC 00042: Finishing the VLM Getting Started Wizard

- bundle_id: `volume-license-manager`
- source_path: `finishing-the-getting-started-wizard.html`
- source_url: https://docs-be.ni.com/bundle/volume-license-manager/raw/resource/enus/finishing-the-getting-started-wizard.html
- document_id: `volume-license-manager`
- page_type: `leaf`
- content_type: `task`
- source_description: Complete the Getting Started Wizard by clicking Finish based on your agreement license file status. If a new license file is required, relaunch VLM upon receipt to continue the setup. For valid license files, finalize the wizard to proceed with VLM configuration. If you requested a new agreement lic

### Finishing the VLM Getting Started Wizard

Complete the Getting Started Wizard by clicking Finish based
 on your agreement license file status. If a new license file is required, relaunch VLM upon
 receipt to continue the setup. For valid license files, finalize the wizard to proceed with
 VLM configuration.

- If you requested a new agreement license file, click
 Finish to close VLM. Relaunch VLM when you receive
 the agreement license file. The wizard opens again to guide you through the
 installation and configuration process for the agreement license file.
- If you have install a valid agreement license file, click
 Finish to close the wizard and open VLM. You can
 continue configuring VLM once it opens. 
 Note If you import
 settings from a previous installation, VLM may require you to install the
 new agreement license file, located at File»Install Agreement License File.

Parent topic:

Completing the VLM Getting Started Wizard

<!--NI_TOPIC bundle=volume-license-manager path=finishing-the-ni-vlm-backuprestore-wizard.html language=enus -->
## TOPIC 00043: Finishing the NI VLM Backup/Restore Wizard

- bundle_id: `volume-license-manager`
- source_path: `finishing-the-ni-vlm-backuprestore-wizard.html`
- source_url: https://docs-be.ni.com/bundle/volume-license-manager/raw/resource/enus/finishing-the-ni-vlm-backuprestore-wizard.html
- document_id: `volume-license-manager`
- page_type: `leaf`
- content_type: `concept`
- source_description: Click the backup filename link to open the location where the file is stored. Click Finish to close the Backup and Restore Wizard. Frequently Asked Questions How do I schedule regular backups? How do I move NI VLM to a new server?

### Finishing the NI VLM Backup/Restore Wizard

Click the backup filename link to open the location where the file is stored.

Click Finish to close the Backup and Restore Wizard.

#### Frequently Asked Questions

- How do I schedule regular backups?
- How do I move NI VLM to a new server?

Parent topic:

Backing up and Restoring NI VLM Data

<!--NI_TOPIC bundle=volume-license-manager path=finishing-volume-license-installer-creation.html language=enus -->
## TOPIC 00044: Finishing Volume License Installer Creation

- bundle_id: `volume-license-manager`
- source_path: `finishing-volume-license-installer-creation.html`
- source_url: https://docs-be.ni.com/bundle/volume-license-manager/raw/resource/enus/finishing-volume-license-installer-creation.html
- document_id: `volume-license-manager`
- page_type: `leaf`
- content_type: `concept`
- source_description: When the wizard finishes building the Volume License Installer, review any warnings or notices, then click Finish to close the wizard. You can also review the Frequently Asked Questions before closing the wizard. If the Volume License Installer you created links to other installers, such as NI Devic

### Finishing Volume License Installer Creation

When the wizard finishes building the Volume License Installer, review any warnings



 or notices, then click Finish to close the wizard. You can



 also review the Frequently Asked Questions before closing the wizard.

Note

- If the Volume License Installer you created links to other installers, such
 as NI Device Drivers, you may want to run the wizard again to create another
 Volume License Installer for the additional installers.
- If the Volume License Installer was built from an installer downloaded from
 ni.com , you may need to download the installer's
 contents. The wizard will prompt you to do so, if necessary. If you choose
 to not download the content when prompted, you can run the Volume License
 Installer from a command line using the
 /DownloadAllNoInstall option to download the installer
 contents at any time. You must download the installer contents before you
 can distribute the Volume License Installer to clients.

#### Distributing a Volume License Installer

Complete the following general steps to distribute your Volume License Installer:

1. Navigate to the destination location you designated in the wizard.
2. If necessary, copy the Volume License Installer to a network location or copy it



 to media, such as a DVD or a USB drive.
3. Inform your clients where to find the Volume License Installer.

Parent topic:

Creating Volume License Installers

<!--NI_TOPIC bundle=volume-license-manager path=glossary.html language=enus -->
## TOPIC 00045: Key Terms

- bundle_id: `volume-license-manager`
- source_path: `glossary.html`
- source_url: https://docs-be.ni.com/bundle/volume-license-manager/raw/resource/enus/glossary.html
- document_id: `volume-license-manager`
- page_type: `leaf`
- content_type: `concept`
- source_description: NI Volume License Manager uses unique terms for completing tasks. Activity Compliance Log The activity compliance log was replaced by the VLA Log in NI VLM 3.1. For more information, refer to VLA Log and Sending VLA Logs to NI. Agreement ID For more information, refer to Service ID. Agreement Licens

### Key Terms

NI Volume License Manager uses unique terms for completing
 tasks.

#### Activity Compliance Log

The activity compliance log was replaced by the
 VLA Log in NI VLM 3.1. For more information, refer to *VLA Log* and *Sending
 VLA Logs to NI*.

#### Agreement ID

For more information, refer to *Service ID*.

#### Agreement License File

A file that contains licenses, or electronic permissions, for all products in your specific
 agreement. You acquire an agreement license file
 by sending an email message to services@ni.com.
 For more information, refer to *Obtaining an
 Agreement License File*.

#### Background Process Port

For more information, refer to *Communication Port*.

#### Client

1. A person that uses NI software that is managed through a volume license



 agreement.
2. A user or a computer

#### Client Machine

The computer used by a client.

#### Communication Port

The port that NI VLM uses to communicate with client machines.

NI VLM typically uses port 465 to connect to the
 SMTP server. Depending on the system, NI VLM may use another port for communication such as
 port 587.

Note

Related tasks:

- Specifying License Ports and Administrator Information

#### Computer ID

A 16-character value that uniquely identifies your computer.

NI uses the volume license server's computer ID to create the agreement license file. You can
 find the volume license server's computer ID in the NI VLM
 Status view.

Clients can find their computer ID in NI License Manager by clicking Display Computer
 Information.

#### Computer Name

1. The name of your volume license server. You can find the computer name on the



 Status view in NI VLM.
2. The name of a computer that uses computer-based licenses. You add computer names



 to NI VLM to grant computer-based software access.

#### Computer-Based License

A license that allows NI products to be installed on a single computer with multiple users. A
 computer-based license allows disconnected
 licenses for both concurrent and non-concurrent
 licenses. A computer-based license also allows a
 single home license for non-concurrent
 licenses.

#### Custom Fields

Customizable fields in NI VLM that you can use to collect various types of



 information from your clients.

Five prepopulated fields — Full Name, Phone, Email, Department, and Cost Center — are required
 by default. NI VLM uses Full Name and Email for
 emailing clients, in reports, and to help license
 administrators.

#### Debug License

A license meant for debugging only. Debug licenses can be only computer-based licenses
 (non-concurrent or concurrent). Named-user debug
 licenses are not allowed.

#### Deployment License

A license for distributing applications that use specific software products. You must



 purchase one deployment license for each target computer on which the application is



 distributed. Deployment licenses can be only nonconcurrent, computer-based



 licenses.

#### Disconnected License

Lets a client use an NI product included in a volume license agreement while not



 attached to the network.

A disconnected license consumes one license. The license can be either non-concurrent or
 concurrent. Disconnecting a concurrent license
 decrements the total available licenses in that
 pool.

#### End User

For more information, refer to *client*.

#### Groups

A collection of licenses and clients. Licenses are permissions to use NI software.



 Every client in a given group has permission for each license in that group. You can



 use groups to define a set of clients that use the same set of software. Groups



 allow you to configure licenses and clients in various ways:

- A single software license can be shared among multiple groups
- A single group can include software from multiple media sets
- A single client can be placed in multiple groups

In previous versions of NI VLM, administrators assigned permissions to clients on a one-to-one
 basis. To use groups to assign permissions, first
 create groups based on logical groupings of
 clients, such as Control Engineering Team or Test
 Engineering Team. Next, assign licenses to each
 group. Groups can contain more than one product
 license. Licenses can be shared among groups.

Figure 2.

[IMAGE alt='image' src='GUID-9B246DAC-9CD3-4764-A61A-4D7A55186414-a5.png']

Next, assign clients to your groups, depending on license model.

Figure 3.

[IMAGE alt='image' src='GUID-794F7ABF-1133-4A2E-B606-63E976A9AFB0-a5.png']

Your groups now contain both licenses and clients. You can continue to assign



 explicit licenses to clients, if necessary.

Figure 4.

[IMAGE alt='image' src='GUID-2AD86866-01B0-4E87-B8ED-A562D1801012-a5.png']

#### Home License

Lets a client install and run NI products included in a volume license agreement on a



 home computer.

A home license does not consume a license on the volume license server and is intended for home
 use only, according to the terms of your volume license agreement with NI. You can
 generate home licenses for your clients only for NI products with non-concurrent
 development licenses. A home license cannot contain concurrent or debug
 licenses.

#### License

Gives clients the legal right to use NI products under the terms of a volume license



 agreement.

Through NI VLM, you can assign permissions to use a license to clients, depending on which
 license model you are using. Licenses can be
 assigned through groups or explicitly assigned to
 individual clients.

#### License File

A file you can generate for a client that contains the permissions needed for using a



 disconnected or home license.

For more information, refer to *agreement license file*.

#### License Models

The types of licenses you can add to your volume license agreement. For more information, refer
 to [Understanding NI
 Software Policies](https://www.ni.com/r/nilmoptionseng).

#### License Server

For more information, refer to *volume license server*.

#### License Set

Sets that administrators defined while creating Volume License Installers that



 assigned permissions to a set of clients with the same license requirements.

License sets, also known as configurations, were used in NI VLM 2.1.x. These
 were replaced by groups in NI VLM
 3.x and later.

#### Main Licensing Port

The port that client machines use to connect to the volume license server. Ports



 range from 1-64000, inclusive. The default port is 27000. If the Main Licensing Port



 is set to something other than the default, clients need to specify the Main



 Licensing Port in NI License Manager. For example, if the Main Licensing Port is



 27001, then the client would specify servername:27001.

The Volume License Installer wizard automatically sets the Main Licensing Port when



 creating Volume License Installers.

Note

Related tasks:

- Specifying License Ports and Administrator Information

#### Named-User License

A license for a single person. You can install the software on up to three computers at a time,
 but you can use it on only one computer at a time.
 A named-user license allows disconnected licenses
 for both concurrent and non-concurrent licenses. A
 named-user license also allows a single home
 license for non-concurrent and non-debug licenses.

#### Network Installer

A standard NI software installer transformed into an installer suited for installation by your
 clients. (NI VLM 2.1 and earlier). Replaced by
 Volume License Installers in NI VLM 2.1.1 and
 later.

#### NI License Manager

A utility clients use to manage various tasks associated with licensed NI



 software.

Related tasks:

- Specifying License Ports and Administrator Information

#### NI Volume License Manager (NI VLM)

A utility you use to manage various tasks associated with centralized license



 management and software asset management.

#### Overdraft

An agreement preference that enables you to use more licenses than the agreement



 allows and pay for them later. Refer to your volume license agreement for specific



 purchasing requirements and overdraft license options.

Related tasks:

- Configuring Overdraft

#### Pay-as-You-Go

An agreement preference that reminds you to update your agreement every time a permission is set
 that takes advantage of overdraft. This preference
 is relevant only when you use the overdraft
 option. You should use this option when you want
 to purchase additional NI product licenses as you
 need them.

Related tasks:

- Configuring Overdraft

#### Permissions

Enables a client to check out licenses from the volume license server. You can grant permissions
 manually or automatically. Unless you have
 overdraft turned on in NI VLM or you have a
 concurrent license, you cannot assign more
 permissions than the maximum number of seats for a
 given license.

#### Private Groups

Groups that are not visible to clients unless it is explicitly shown by the administrator or they
 are members of the private group. Use the Volume
 License Installer Wizard to allow clients to
 select private groups.

#### Public Groups

Groups visible to all clients running a Volume License Installer or with NI License



 Manager 3.5 or later installed.

#### Reconnect

Connect a client to NI VLM that previously used a disconnected license.

Expired disconnected concurrent licenses automatically reconnect in NI VLM when you
 click Apply Changes or when you launch NI VLM with the
 /reconnect command. Until a disconnected concurrent license is
 reconnected, the seat is not available for use by other clients.

Note

#### Service ID

A Service ID is a unique identifier of your agreement with NI. You need
 this identifier when you contact NI about your
 agreement.

If you have a new VLA, you can find the Service ID in the Description section of the Sales Order
 Acknowledgement (SOA). If you already have a VLA,
 you can also find the Service ID on the NI VLM
 Status view, any quotes you may have received, and
 in your Welcome email.

#### SMTP

Simple Mail Transfer Protocol (SMTP), a standard protocol for sending email across



 the Internet.

#### Usage Log

The usage log has been replaced by the reporting feature in NI VLM 3.1. For more information,
 refer to *Creating Reports*.

#### Username

The Windows login name of a person licensed to use NI products. You add usernames to



 NI VLM to grant software access for named-user licenses.

Note

#### VLA Log

Stores usage information of NI VLM-controlled software, along with client information. For more
 information, refer to *Sending a VLA Log to
 NI*.

NI VLM records into the VLA Log all instances of policy and permissions changes,

 including overdrafts. You send the VLA Log to NI when your current agreement is

 expiring, when your User or Computer list has changed, when you have added overdraft

 permissions under the pay-as-you-go option, or when you plan to move NI VLM to

 another computer.

NI then uses the information in the VLA Log to determine how much, if anything, is

 owed on the extra licenses and maintenance for the coming agreement period and

 returns to you a new agreement license file based on whether you renewed the

 agreement.

The VLA Log includes the following items:

- Custom field data for users and computers such as name, email address, user name, and computer
 name
- The date permissions were added and removed from each User or Computer
- The date a client was disconnected or a home license was created
- The date a disconnected client was reconnected
- Check-in and check-out events
- The contents of each agreement license file
- The overdraft percentage, if overdraft is enabled
- Whether pay-as-you-go is enabled
- The administrator information such as name and email address

#### Volume License Installer

A modified NI software installer that points client machines to a volume license

 server for licensing and potentially requests permissions to use the software to be

 installed.

Use the Volume License Installer Wizard, located in NI VLM under Tools»Create Volume License Installer , to update a standard NI software installer and copy the modified
 installer to a local or shared network drive. You can then distribute the modified
 installer within your organization.

For more information, refer to *Creating Volume License Installers*.

Related tasks:

- Specifying License Ports and Administrator Information

#### Volume License Server

A computer used to manage volume licenses for NI products on a given network. The

 volume license server must be active in order for clients to check out NI products

 included in a volume license agreement.

<!--NI_TOPIC bundle=volume-license-manager path=grouping-data.html language=enus -->
## TOPIC 00046: Grouping Data

- bundle_id: `volume-license-manager`
- source_path: `grouping-data.html`
- source_url: https://docs-be.ni.com/bundle/volume-license-manager/raw/resource/enus/grouping-data.html
- document_id: `volume-license-manager`
- page_type: `leaf`
- content_type: `concept`
- source_description: NI Volume License Manager lets you group data (on the main view grids only) to make it easier to manage. Grouping Rows To group rows in a view, complete one of the following actions: Drag a column header from the column header panel to the group panel. Right-click a column header and select Group Co

### Grouping Data

NI Volume License Manager lets you group data (on the main view grids only) to make



 it easier to manage.

#### Grouping Rows

[IMAGE alt='image' src='GUID-98ECE2AA-140F-4358-B5B8-F51775213971-a5.png']

To group rows in a view, complete one of
 the following actions:

- Drag a column header from the column header
 panel to the group panel.
- Right-click a column header and select
 Group Column from the
 context menu.

#### Grouping Features

You can perform the following tasks using the
 grouping feature:

- Group by multiple columns at the same
 time.
- To change group order, move a grouped column
 header to another position within the group
 panel.
- When grouping a date column, you can right
 click on a column header and set a
 Grouping Interval .
- You can also expand/collapse all group rows
 using a grouped column's right-click menu or using
 the group panel right-click menu.

#### Ungrouping Rows

To ungroup data, complete one of the following
 actions:

- Drag a column header from the group panel to
 the column header panel.
- Right-click a grouping column's header and
 select the Ungroup Column 
 from the context menu.
- Right-click on a grouped column header or the
 group panel and select Clear
 Grouping to clear a grouping.

Note

sort

filter

Parent topic:

Working With the VLM User Interface

<!--NI_TOPIC bundle=volume-license-manager path=groups-view.html language=enus -->
## TOPIC 00047: Groups View

- bundle_id: `volume-license-manager`
- source_path: `groups-view.html`
- source_url: https://docs-be.ni.com/bundle/volume-license-manager/raw/resource/enus/groups-view.html
- document_id: `volume-license-manager`
- page_type: `leaf`
- content_type: `concept`
- source_description: Use the Groups view to manage any groups listed in NI VLM. The Groups view displays the following columns: Group Name Type Visibility Description Permission Request Handling To see hidden columns, right click on any column header, select Add/Remove Columns, and select any available columns you want

### Groups View

Use the Groups view to manage any groups listed in NI
 VLM.

The Groups view displays the following columns:

- Group Name
- Type
- Visibility
- Description
- Permission Request Handling

Note

Add/Remove Columns

#### Viewing Group Information

Expand each group to view more information, including the following:

- The group's licenses
- The group's members

Note

Add/Remove
 Columns

#### Editing Groups

From this view, you can perform the following tasks:

- Add 
 a group to NI VLM
- Edit 
 a listed group
- Delete one or more of the listed groups
- Email multiple clients associated with the selected groups

Parent topic:

VLM User Interface

<!--NI_TOPIC bundle=volume-license-manager path=handling-permission-requests.html language=enus -->
## TOPIC 00048: Handling Permission Requests

- bundle_id: `volume-license-manager`
- source_path: `handling-permission-requests.html`
- source_url: https://docs-be.ni.com/bundle/volume-license-manager/raw/resource/enus/handling-permission-requests.html
- document_id: `volume-license-manager`
- page_type: `leaf`
- content_type: `concept`
- source_description: By default, NI VLM allows clients to ask for permissions (a request to be added) when they run Volume License Installers. The Volume License Installer presents the client with a dialog box that allows them to enter their user and computer information and select the groups for which to request permis

### Handling Permission Requests

By default, NI VLM allows clients to ask for permissions (a request to be added) when



 they run [Volume License Installers](creating-volume-license-installers.html). The Volume License Installer presents the



 client with a dialog box that allows them to enter their user and computer



 information and select the groups for which to request permissions. A permission



 request containing that information is sent to NI VLM. Clients can also generate



 permission requests from within NI License Manager 3.5 or later.

Note

Configuring Email Server Settings

#### Setting Permission Request
 Handling

NI VLM 3.1 can handle the following types of permission requests:

- NI VLM 3. x -formatted requests, such as permission requests
 from 3. x -version Volume License Installers and those
 generated by NI License Manager 3.5 and later
- Legacy requests from Volume License Installers generated by NI VLM
 2. x or earlier

#### Setting Handling for NI VLM 3.
 -Formatted Permission Requests

Depending on your selected settings, NI VLM handles permission requests containing
 groups using one of three methods, as follows:

- Manual (System-wide Setting) —Lets you handle permission
 requests manually for all groups.
- Automatic (System-wide Setting) —Sets NI VLM to handle
 permission requests automatically for all groups.
- Set Individually —Lets you set permission request handling
 on a group-by-group basis. If you select this option, you set permission request
 handling at the time you create or edit a group.

Complete the following steps to specify how NI VLM handles permission requests
 containing groups:

1. Select the Tools»Preferences menu item.
2. Select General on the navigation tree.
3. In the Groups section, set Permission Request Handling to
 Manual (System-wide Setting) , Automatic
 (System-wide Setting) , or Set
 Individually .
4. Click Save .

Depending on your selected settings, NI VLM handles
 3.x-formatted client information-only permission requests either
 automatically or manually. Complete the following steps to specify how NI VLM
 handles client information-only requests:

1. Select the Tools»Preferences menu item.
2. Select General on the navigation tree.
3. In the Miscellaneous section, set Automatically handle client
 information-only requests to either Yes 
 or No .
4. Click Save .

Setting Handling for Legacy Permission Requests

Depending on your selected
 settings, NI VLM handles legacy permission requests either automatically or
 manually. Legacy permission requests are those generated by Volume License
 Installers created with NI VLM 2.x or earlier. These requests do
 not contain any group requests.

Complete the following steps to determine how
 NI VLM handles legacy requests:

1. Select the Tools»Preferences menu item.
2. Select General on the navigation tree.
3. In the Miscellaneous section, set Automatically handle legacy
 permission requests to either Yes or
 No .
4. Click Save .

Handling Permission Requests

You can set NI VLM to handle permission
 requests automatically or to let you handle permission requests
 manually.

Handling Requests Automatically—When a
 permission request arrives, the client information of the requesting client is added
 or updated, and the client is added automatically to the requested groups and
 licenses if enough seats are available. If there are no seats available or if there
 are any other problems with the request, it remains in Permission Requests until you
 can handle the request manually.

Note

- Automatic permission request handling is disabled while NI VLM's user
 interface is open. Requests are stored in Permision Requests. You can either
 approve or deny requests while using NI VLM.
- If NI VLM encounters a permission request that contains groups that include
 both manual and automatic permission handling, NI VLM will handle the
 automatic requests, but you will need to handle the manual requests
 separately.

Handling Requests Manually—If you select to handle
 requests manually, the requests are placed in Permission Requests, where you can
 accept, accept with changes, or reject requests on an individual basis.

Note

You can choose to Accept or
 Reject all permission requests. If the request is
 accepted, all of the client information is imported into NI VLM, and the permissions
 for the requested groups and licenses are granted. If you reject the request, no
 information is imported into NI VLM and permissions for the requested groups and
 licenses are not granted.

You can also choose to Accept with
 Changes a 3.x-formatted permission request. This
 option allows you to edit user or computer information as well as add or remove any
 permissions before accepting the permission. Accept with
 Changes is not available for legacy permission requests.

#### Setting Handling for Legacy
 Permission Requests

Depending on your selected settings, NI VLM handles legacy permission requests either
 automatically or manually. Legacy permission requests are those generated by Volume
 License Installers created with NI VLM 2.x or earlier. These
 requests do not contain any group requests.

Complete the following steps to
 determine how NI VLM handles legacy requests:

1. Select the Tools»Preferences menu item.
2. Select General on the navigation tree.
3. In the Miscellaneous section, set Automatically handle legacy
 permission requests to either Yes or
 No .
4. Click Save .

#### Handling Permission
 Requests

You can set NI VLM to handle permission requests automatically or to let you handle
 permission requests manually.

Handling Requests
 Automatically—When a permission request arrives, the client
 information of the requesting client is added or updated, and the client is added
 automatically to the requested groups and licenses if enough seats are available. If
 there are no seats available or if there are any other problems with the request, it
 remains in Permission Requests until you can handle the request manually.

Note

- Automatic permission request handling is disabled while NI VLM's user
 interface is open. Requests are stored in Permision Requests. You can either
 approve or deny requests while using NI VLM.
- If NI VLM encounters a permission request that contains groups that include
 both manual and automatic permission handling, NI VLM will handle the
 automatic requests, but you will need to handle the manual requests
 separately.

Handling Requests Manually—If you select to handle
 requests manually, the requests are placed in Permission Requests, where you can
 accept, accept with changes, or reject requests on an individual basis.

Note

You can choose to Accept or
 Reject all permission requests. If the request is
 accepted, all of the client information is imported into NI VLM, and the permissions
 for the requested groups and licenses are granted. If you reject the request, no
 information is imported into NI VLM and permissions for the requested groups and
 licenses are not granted.

You can also choose to Accept with
 Changes a 3.x-formatted permission request. This
 option allows you to edit user or computer information as well as add or remove any
 permissions before accepting the permission. Accept with
 Changes is not available for legacy permission requests.

Parent topic:

Managing the Volume License Server

Related tasks:

- Completing VLM Setup

<!--NI_TOPIC bundle=volume-license-manager path=hiding-and-displaying-columns-in-a-view.html language=enus -->
## TOPIC 00049: Hiding and Displaying Columns in a View

- bundle_id: `volume-license-manager`
- source_path: `hiding-and-displaying-columns-in-a-view.html`
- source_url: https://docs-be.ni.com/bundle/volume-license-manager/raw/resource/enus/hiding-and-displaying-columns-in-a-view.html
- document_id: `volume-license-manager`
- page_type: `leaf`
- content_type: `concept`
- source_description: To hide or display columns in a view, complete the following steps: Right-click on any column header and select Add/Remove Columns. Drag a column header from the Customization box to the column header panel to display the column. Drag a column header to the Customization box to hide the column. You

### Hiding and Displaying Columns in a View

[IMAGE alt='image' src='GUID-69527761-74DC-48A9-8C55-7DB8B6C0DC2D-a5.png']

To hide or display columns in a view, complete the following steps:

1. Right-click on any column header and select Add/Remove



 Columns .
2. Drag a column header from the Customization box to the column header panel to



 display the column. Drag a column header to the Customization box to hide the



 column. You can also right-click to remove or add a column and double-click to



 add a column.

Note

- To rearrange the column order, click and drag
 columns to where you want to put them.
- Some primary columns cannot be removed.

Parent topic:

Working With the VLM User Interface

<!--NI_TOPIC bundle=volume-license-manager path=importing-settings-from-a-previous-ni-vlm-2x-or-earlier-installation.html language=enus -->
## TOPIC 00050: Importing Settings from a Previous NI VLM 2.x or Earlier Installation

- bundle_id: `volume-license-manager`
- source_path: `importing-settings-from-a-previous-ni-vlm-2x-or-earlier-installation.html`
- source_url: https://docs-be.ni.com/bundle/volume-license-manager/raw/resource/enus/importing-settings-from-a-previous-ni-vlm-2x-or-earlier-installation.html
- document_id: `volume-license-manager`
- page_type: `leaf`
- content_type: `concept`
- source_description: Complete the following steps to import NI VLM data files: Click the ellipsis () to navigate to the location of the data file you want to import. The Getting Started Wizard displays only the type of file necessary. You can find the data files in the following typical locations:Windows 11/10/8/7/Vista

### Importing Settings from a Previous NI VLM 2.x or Earlier Installation

Complete the following steps to import NI VLM data files:

1. Click the ellipsis ( ) to
 navigate to the location of the data file you want to import. The Getting Started Wizard
 displays only the type of file necessary. You can find the data files in the following
 typical locations: Windows 11/10/8/7/VistaC:\ProgramData\National Instruments\Volume License
 Manager\Windows XPC:\Program Files\National Instruments\Volume License
 Manager\
2. Select the file and click Open .

Parent topic:

Importing Settings from Previous NI VLM Installations

<!--NI_TOPIC bundle=volume-license-manager path=importing-settings-from-a-previous-ni-vlm-3x-installation.html language=enus -->
## TOPIC 00051: Importing Settings from a Previous NI VLM 3.x Installation

- bundle_id: `volume-license-manager`
- source_path: `importing-settings-from-a-previous-ni-vlm-3x-installation.html`
- source_url: https://docs-be.ni.com/bundle/volume-license-manager/raw/resource/enus/importing-settings-from-a-previous-ni-vlm-3x-installation.html
- document_id: `volume-license-manager`
- page_type: `leaf`
- content_type: `concept`
- source_description: Complete the following steps to import an NI VLM 3.x backup file: Click the ellipsis () to navigate to the location of your backup file. You can find the backup file in the following typical locations:Windows 11/10/8/7/VistaC:\ProgramData\National Instruments\Volume License Manager\Backups\Windows X

### Importing Settings from a Previous NI VLM 3.x Installation

Complete the following steps to import an NI VLM 3.x backup



 file:

1. Click the ellipsis ( ) to
 navigate to the location of your backup file. You can find the backup file in
 the following typical locations: Windows 11/10/8/7/VistaC:\ProgramData\National Instruments\Volume
 License Manager\Backups\Windows XPC:\Documents and Settings\All Users\Application
 Data\National Instruments\Volume License
 Manager\Backups
2. Select your most recent NI VLM backup file ( *.vlmbak ) and click



 Open .

Note

NI VLM preferences

Tools

»

Preferences

Parent topic:

Importing Settings from Previous NI VLM Installations

<!--NI_TOPIC bundle=volume-license-manager path=importing-settings-from-previous-ni-vlm-installations.html language=enus -->
## TOPIC 00052: Importing Settings from Previous NI VLM Installations

- bundle_id: `volume-license-manager`
- source_path: `importing-settings-from-previous-ni-vlm-installations.html`
- source_url: https://docs-be.ni.com/bundle/volume-license-manager/raw/resource/enus/importing-settings-from-previous-ni-vlm-installations.html
- document_id: `volume-license-manager`
- page_type: `leaf`
- content_type: `concept`
- source_description: This page gives you the option to import settings from a previous NI VLM installation. Select Do not import settings if this is the first time you have run NI VLM or if you want to install a fresh version of NI VLM. Select Import settings from a previous NI VLM 3.x installation if you have previousl

### Importing Settings from Previous NI VLM Installations

This page gives you the option to import settings from a previous NI VLM



 installation.

- Select Do not import settings if this is the first time



 you have run NI VLM or if you want to install a fresh version of NI VLM.
- Select Import settings from a previous NI VLM 3.x



 installation if you have previously set up NI VLM



 3. x on this or another computer and have access to NI VLM



 3. x backup files.
- Select Import Settings from a previous NI VLM 2.x or earlier



 installation if you have previously set up NI VLM



 2. x on this or another computer and have access to the NI



 VLM 2. x data and preferences files.

Parent topic:

Completing the VLM Getting Started Wizard

<!--NI_TOPIC bundle=volume-license-manager path=installing-agreement-license-files.html language=enus -->
## TOPIC 00053: Installing Agreement License Files

- bundle_id: `volume-license-manager`
- source_path: `installing-agreement-license-files.html`
- source_url: https://docs-be.ni.com/bundle/volume-license-manager/raw/resource/enus/installing-agreement-license-files.html
- document_id: `volume-license-manager`
- page_type: `leaf`
- content_type: `concept`
- source_description: Use the Agreement License File Installation Wizard to install a new agreement license file into NI VLM and transfer permissions from your old licenses to your new licenses. The Agreement License File Installation Wizard performs the following tasks: Automatically backs up NI VLM before applying the

### Installing Agreement License Files

Use the Agreement License File Installation Wizard to install a new
 agreement license file into NI VLM and transfer permissions
 from your old licenses to your new licenses.

The Agreement License File Installation Wizard performs the following tasks:

- Automatically backs up NI VLM before applying the new agreement license



 file
- Migrates permissions from the old agreement license file to the new agreement



 license file
- Allows you to reassign permissions, use overdraft, or delete permissions to



 bring the current permission assignments into compliance with the new volume



 license agreement file.

Parent topic:

Using License Files

#### Selecting the Agreement License File

Click the ellipsis ([IMAGE alt='image' src='GUID-AFC70F11-B3D8-4056-B2A4-E10B674BFAB4-a5.png']) to
 navigate to the agreement license file you want to install.

NI VLM automatically creates a backup before installing the new agreement license file. The
 backup is stored in the default backup directory you specified in Tools»Preferences.

Note

- If the agreement license file you selected is an NI VLM 2.x version, you
 will not be able to take advantage of all NI VLM 3. x 
 features. Clients will still be able to check out and check in
 licenses.
- You cannot install an NI VLM 1.x license file to NI VLM
 3. x . Refer to Obtaining an Agreement
 License File for information on how to request a new license file
 from NI.

#### Confirming Agreement License File Downgrade

Some or all of the licenses in your new agreement license file have earlier versions



 than the licenses currently in NI VLM. If you continue, your permissions will be



 downgraded to match this version of the agreement license file.

Click Next if you want to continue installing the new



 agreement license file. Click Back to select a different



 agreement license file. Click Cancel to cancel agreement



 license file installation.

Note

- In normal operation, a downgrade should never
 happen. You may be attempting to install an incorrect agreement license file. If you
 have questions about your agreement license file, email services@ni.com.
- Clients using software versions earlier or the
 same as the version in the new license file will
 continue to have access to their software.

#### Transferring Permissions

You can transfer the permissions of an old license to a new license of
 the same model. You can also remove the old permissions.

Some or all of the licenses in your old agreement
 license file do not have an exact match in your
 new agreement license file. During agreement
 license file installation, NI VLM automatically
 matches licenses in the old agreement license file
 with licenses in the new agreement license file
 that have the exact same product and licensing
 model and then transfers permissions associated
 with the old license to the new license. In this
 section of the wizard, you will be given a chance
 to reassign or delete the permissions associated
 with any licenses that NI VLM could not
 automatically match.

Click Next to reassign or
 delete old permissions. Click
 Back to select a different
 agreement license file. Click
 Cancel to cancel agreement
 license file installation.

To transfer permissions, select either of the following options:

- Select Transfer the permissions to another [license model]
 license to update all groups, users,
 and computers that had permissions for the old
 license to have the permissions for the new
 license that you select. This option is not
 available if there are no licenses of the same
 license model in the new license file. Note 
 If you transfer more permissions to a license
 than there are available seats or if the transfer
 consumes new overdraft permissions, you will be
 given the opportunity to remove excess permissions
 before completing agreement license file
 installation.
 If you want to transfer permissions to
 multiple licenses, you may want to remove all
 permissions and reassign them in NI VLM after
 agreement license file installation completes.
 Alternatively, you can select one destination
 license and manually reassign the other
 permissions in NI VLM.
- Select Remove all permissions assigned to this license to remove all
 permissions from groups, users, and computers for
 the old license. Use this option if you are not
 replacing this license or if you are moving to
 another license model.

#### Finishing Agreement License File Installation

If there are now more permissions for a license than there are seats available in the



 new agreement license file, you must modify permission assignments to resolve any



 errors when the Agreement License File Installation Wizard finishes.

Click Back to modify agreement license file installation



 settings or select another agreement license file. Click



 Finish to close the wizard, return to NI VLM, and modify



 permissions using the Agreement License File Installation panel as a guide. Click



 Cancel to cancel agreement license file installation.

The [Agreement License File Installation](installing-agreement-license-files.html#GUID-DBA71A13-3C70-4207-83A1-DC6E5530F486) panel appears in NI VLM when the



 wizard closes to help resolve any issues. You can remove permission assignments by



 modifying groups or explicit permissions or you can increase the [overdraft](setting-overdraft-policies.html) limit to reduce or eliminate excess permissions.

If there are no warnings or errors, click Finish to install



 the agreement license file. You can now use the Licenses,



 Users, Computers, or



 Groups views to assign new permissions, if needed.

#### Using the Agreement License File Installation Panel in NI VLM

Use this panel in NI VLM to help resolve any permission assignment issues and



 authorize any new [overdrafts](setting-overdraft-policies.html). You can remove permission assignments by modifying groups or



 explicit permissions or you can increase the overdraft limit to reduce or eliminate



 excess permissions.

Use the Groups, Licenses,



 Users, and Computers views to



 adjust the number of permission assignments as needed. You must resolve all errors



 before you can exit this panel.

Click OK to accept your changes and to authorize any new



 overdrafts, if necessary.

Note

<!--NI_TOPIC bundle=volume-license-manager path=installing-an-agreement-license-file.html language=enus -->
## TOPIC 00054: Installing an Agreement License File

- bundle_id: `volume-license-manager`
- source_path: `installing-an-agreement-license-file.html`
- source_url: https://docs-be.ni.com/bundle/volume-license-manager/raw/resource/enus/installing-an-agreement-license-file.html
- document_id: `volume-license-manager`
- page_type: `leaf`
- content_type: `concept`
- source_description: You must install a new agreement license file on your system every new agreement period or pay-as-you-go renewal to keep your agreement license file current and not expiring. Once you have received an agreement license file from NI, complete the following steps to install the file. Launch NI VLM and

### Installing an Agreement License File

You must install a new agreement license file on your system every new agreement



 period or pay-as-you-go renewal to keep your agreement license file current and not



 expiring.

Once you have received an agreement license file from NI, complete the following



 steps to install the file.

1. Launch NI VLM and select the File»Install Agreement License
 File menu item.
2. Complete the steps in the Agreement License File Installation Wizard .

Parent topic:

Managing the Volume License Server

Related tasks:

- Obtaining or Installing an Agreement License File

<!--NI_TOPIC bundle=volume-license-manager path=installing-disconnected-license-files.html language=enus -->
## TOPIC 00055: Installing Disconnected License Files

- bundle_id: `volume-license-manager`
- source_path: `installing-disconnected-license-files.html`
- source_url: https://docs-be.ni.com/bundle/volume-license-manager/raw/resource/enus/installing-disconnected-license-files.html
- document_id: `volume-license-manager`
- page_type: `leaf`
- content_type: `concept`
- source_description: When installing a disconnected license file on a client machine, you have two options—installing a disconnected license file using NI License Manager or using the NI VLM Import Utility. Complete the following steps to install a disconnected license file using NI License Manager: On the client machin

### Installing Disconnected License Files

When installing a disconnected license file on a client machine, you have two



 options—installing a disconnected license file using NI License Manager or using the



 NI VLM Import Utility.

Complete the following steps to install a disconnected license file using NI License



 Manager:

1. On the client machine, launch NI License Manager.
2. Choose Options»Install License File from the menu.
3. Select the disconnected license file and click OK .

Note

For information about using the NI VLM Import Utility, refer to [Installing Disconnected Licenses using NI VLM Import Utility](installing-disconnected-licenses-using-ni-vlm-import-utility.html).

Parent topic:

Managing Disconnected License Files

Related tasks:

- Completing VLM Setup

<!--NI_TOPIC bundle=volume-license-manager path=installing-disconnected-licenses-using-ni-vlm-import-utility.html language=enus -->
## TOPIC 00056: Installing Disconnected Licenses using NI VLM Import Utility

- bundle_id: `volume-license-manager`
- source_path: `installing-disconnected-licenses-using-ni-vlm-import-utility.html`
- source_url: https://docs-be.ni.com/bundle/volume-license-manager/raw/resource/enus/installing-disconnected-licenses-using-ni-vlm-import-utility.html
- document_id: `volume-license-manager`
- page_type: `leaf`
- content_type: `concept`
- source_description: Complete the following steps on each client machine to install disconnected license files using the NI VLM Import Utility: Create disconnected license files. For more information, refer to Creating a Disconnected License File. Copy everything in the Import Utility directory to a network drive or por

### Installing Disconnected Licenses using NI VLM Import Utility

Complete the following steps on each client machine to install disconnected license



 files using the NI VLM Import Utility:

1. Create disconnected license files. For more information, refer to Creating a Disconnected License File .
2. Copy everything in the Import Utility directory to a network drive or portable
 media, such as a USB drive, or the client machine. You can find the utility in
 the following locations: Windows 11/10/8/7/Vista
 C:\ProgramData\National Instruments\Volume
 License Manager\Import Utility\
 Windows XP
 C:\Documents and Settings\All Users\Application
 Data\National Instruments\Volume License Manager\Import
 Utility\ Note NI VLM
 Import Utility uses an XML file, nivlmImportUtility.xml, to
 determine the custom fields that are available, which fields clients must
 complete, and which are optional. The
 nivlmImportUtility.xml file updates whenever you change
 [custom fields](configuring-custom-fields.html). If you modify the custom fields, you must copy
 the updated nivlmImportUtility.xml to where you use NI VLM
 Import Utility.
3. Save the disconnected license files in the same storage location as NI VLM



 Import Utility.
4. Have clients complete the following steps:
  1. Run



 nivlmImportUtility.exe on the computer to which



 they want to install the disconnected license files.
  2. Click



 Install License Files to copy and install the



 appropriate disconnected license files onto the target client



 machine.

Parent topic:

Installing Disconnected License Files

<!--NI_TOPIC bundle=volume-license-manager path=installing-home-license-files.html language=enus -->
## TOPIC 00057: Installing Home License Files

- bundle_id: `volume-license-manager`
- source_path: `installing-home-license-files.html`
- source_url: https://docs-be.ni.com/bundle/volume-license-manager/raw/resource/enus/installing-home-license-files.html
- document_id: `volume-license-manager`
- page_type: `leaf`
- content_type: `concept`
- source_description: Complete the following steps to install a home license file using NI License Manager: On the home computer, launch NI License Manager. Choose OptionsInstall License File from the menu. Select the home license file and click OK. You can also install a home license file by dragging-and-dropping the fi

### Installing Home License Files

Complete the following steps to install a home license file using NI License



 Manager:

1. On the home computer, launch NI License Manager.
2. Choose Options»Install License File from the menu.
3. Select the home license file and click OK .

Note

Parent topic:

Creating Home License Files

<!--NI_TOPIC bundle=volume-license-manager path=licenses-view.html language=enus -->
## TOPIC 00058: Licenses View

- bundle_id: `volume-license-manager`
- source_path: `licenses-view.html`
- source_url: https://docs-be.ni.com/bundle/volume-license-manager/raw/resource/enus/licenses-view.html
- document_id: `volume-license-manager`
- page_type: `leaf`
- content_type: `concept`
- source_description: Use the Licenses view to manage the licenses in your volume license agreement. The Licenses view displays the following columns: Product Name License Name License Model Total Seats Total Seats Granted Serial Number To see hidden columns, right click on any column header, select Add/Remove Columns, a

### Licenses View

Use the Licenses view to manage the licenses in your volume
 license agreement.

The Licenses view displays the following columns:

- Product Name
- License Name
- License Model
- Total Seats
- Total Seats Granted
- Serial Number

Note

Add/Remove Columns

#### Viewing License
 Information

[Expand](expanding-and-collapsing-rows.html)
 each license to view more information, including the following:

- A summary of the permissions assigned to this license
- The list of groups (public and private) to which this license is assigned
- The list of clients (users or computers) assigned to this license
- The number of seats available for overdraft and the number of overdrafted seats
 granted. This field is visible only if overdraft is turned on for this
 license.
- The list of clients currently using this license and what time each client
 checked out the license

Note

Add/Remove
 Columns

#### Editing Licenses

From this view, you can add or remove groups and explicit permissions to this
 license. Select one of the following methods to edit a license:

- Select the license and click Edit License .
- Double-click the license.
- Select the license and press <Enter>.

#### Emailing Multiple Clients

From this view, you can also [email](sending-email-to-clients.html#GUID-7D446500-D605-4602-8772-135C9C0423E8) multiple clients associated with the selected licenses.

Parent topic:

VLM User Interface

<!--NI_TOPIC bundle=volume-license-manager path=managing-clients.html language=enus -->
## TOPIC 00059: Managing, Monitoring, and Communicating with Clients

- bundle_id: `volume-license-manager`
- source_path: `managing-clients.html`
- source_url: https://docs-be.ni.com/bundle/volume-license-manager/raw/resource/enus/managing-clients.html
- document_id: `volume-license-manager`
- page_type: `leaf`
- content_type: `concept`
- source_description: Learn how to manage, monitor, and communicate with client computers.

### Managing, Monitoring, and Communicating with
 Clients

Learn how to manage, monitor, and communicate with client computers.

- [Managing Groups](managing-groups.html#GUID-52AA0D4F-AD68-43E2-9B2C-0722E49E07A8) Use groups to configure licenses and clients.
- [Managing Users or Computers](managing-users-or-computers.html#GUID-E4D8B6A9-E17C-460B-81E1-7A373A546C5B) Manage the users or computers in NI VLM.
- [Creating Reports](creating-reports.html) Use the NI VLM Reports view to create activity, utilization, allocation, and compliance reports.
- [Sending a VLA Log to NI](sending-a-vla-log-to-ni.html#GUID-3A2BB046-EFFA-4188-B1A5-5E00D31F9B0E) Use the VLA Log Wizard to generate and send a VLA Log to NI.
- [Sending Emails to Clients](sending-email-to-clients.html#GUID-7D446500-D605-4602-8772-135C9C0423E8) Use the Email Clients Wizard to email one or more clients.

<!--NI_TOPIC bundle=volume-license-manager path=managing-disconnected-license-files.html language=enus -->
## TOPIC 00060: Managing Disconnected License Files

- bundle_id: `volume-license-manager`
- source_path: `managing-disconnected-license-files.html`
- source_url: https://docs-be.ni.com/bundle/volume-license-manager/raw/resource/enus/managing-disconnected-license-files.html
- document_id: `volume-license-manager`
- page_type: `leaf`
- content_type: `concept`
- source_description: Enable a client to use an NI product included in a volume license agreement while not attached to the network. Disconnected licenses are useful for clients working on client machines unattached to the network, such as laptops, client machines behind certain firewalls, or client machines without netw

### Managing Disconnected License Files

Enable a client to use an NI product included in a volume license agreement
 while not attached to the network.

Disconnected licenses are useful for clients working on client machines unattached to



 the network, such as laptops, client machines behind certain firewalls, or client



 machines without network cards. Without a disconnected license, these clients are



 not able to use their NI software at all times. Disconnected licenses consume a



 license on the volume license server.

Note

- If the client machine will be disconnected from the network for less than 14 days, you do not
 need to create a disconnected license file. For more information, refer to
 Using Temporary Network Licenses .
- A client can still check out a license from
 the server even if that named-user or
 computer-based license is in the disconnected
 state.
- You must create separate disconnected license
 files for computer-based and named-user licenses.
 If a client has both types of permissions, you
 must disconnect both the user and the
 computer.

#### Creating Computer-Based Disconnected License
 Files

Complete the following steps to create
 computer-based disconnected license files.

1. In the Computers view,
 select one or more computers to disconnect.
2. Click Disconnect .
3. Complete the Disconnection Wizard.
4. Install the license files on the client machine. Refer to Installing Disconnected License
 Files for more information.

#### Creating Named-User Disconnected License
 Files

Complete the following steps to create
 named-user disconnected license files.

1. In the Users view,
 select one or more users to disconnect.
2. Click Disconnect .
3. Complete the Disconnection Wizard.
4. Install the license files on the client machine. Refer to Installing Disconnected License
 Files for more information.

Parent topic:

Using License Files

Related concepts:

- Using Temporary Network Licenses

Related tasks:

- Completing VLM Setup

Related reference:

- NiVlm.exe Command Reference

<!--NI_TOPIC bundle=volume-license-manager path=managing-groups.html language=enus -->
## TOPIC 00061: Managing Groups

- bundle_id: `volume-license-manager`
- source_path: `managing-groups.html`
- source_url: https://docs-be.ni.com/bundle/volume-license-manager/raw/resource/enus/managing-groups.html
- document_id: `volume-license-manager`
- page_type: `leaf`
- content_type: `concept`
- source_description: Use groups to configure licenses and clients. A group is a collection of licenses and clients. Every client in a given group has permission for each license in a group. You can use groups to define a set of clients that use the same set of software. Instead of clients requesting permission for indiv

### Managing Groups

Use groups to configure licenses and clients.

A *group* is a collection of licenses and clients. Every client in a given group has
 permission for each license in a group. You can
 use groups to define a set of clients that use the
 same set of software.

Instead of clients requesting permission for individual licenses, they will request



 permission to join groups. Upon acceptance into a group, clients will be granted



 access to all the licenses within that group.

Parent topic:

Managing, Monitoring, and Communicating with Clients

#### Adding Groups

1. In the Groups view, click Add User
 Group or Add Computer Group .
2. Fill in the group information.
  - Name —The name of the group.
  - Visibility —Select whether the group is
 Public or Private .
 Public groups are displayed when a client runs a Volume License
 Installer and in NI License Manager 3.5 or later. Private groups are not
 displayed to clients.
  - Permission Request Handling —Select how you want
 NI VLM to handle permission requests for this group, either
 Manual or Automatic .
 For more information, refer to Handling Permission
 Requests .
  - Description —Enter a description of the group
 (optional). This description is displayed to clients when they run
 Volume License Installers and in NI License Manager's Groups list.
3. Next to the Licenses box, click
 Add to add licenses to the group. Note A group can contain only
 computer-based licenses or only named-user licenses. You cannot mix these
 license types.
4. Next to the Members box, click Add 
 to add Users or Computers to the group. Note The most efficient way to get
 clients into NI VLM is with Volume License Installers. Create Volume License
 Installers to allow clients to install software, enter their user
 information, and request permissions to groups.
5. Click Save .

Related tasks:

- Completing VLM Setup

#### Editing Groups

Select one of the following methods to edit a group from the
 Groups view:

- Click Edit Group .
- Double-click a group.

#### Deleting Groups

1. In the Groups view, select one or more groups. Use the
 <Ctrl> or
 <Shift> keys to select
 multiple groups, as necessary.
2. Click Delete Group .
3. Click Yes to confirm the deletion.

<!--NI_TOPIC bundle=volume-license-manager path=managing-locally-installed-ni-software.html language=enus -->
## TOPIC 00062: Managing Locally Installed NI Software

- bundle_id: `volume-license-manager`
- source_path: `managing-locally-installed-ni-software.html`
- source_url: https://docs-be.ni.com/bundle/volume-license-manager/raw/resource/enus/managing-locally-installed-ni-software.html
- document_id: `volume-license-manager`
- page_type: `leaf`
- content_type: `concept`
- source_description: If you have NI application software installed on the same computer as NI VLM and you want the application software to validate its license using NI VLM, complete the following steps: Launch NI License Manager. Select »Manage Volume License Servers to add a volume license server. When the NILM is n

### Managing Locally Installed NI Software

If you have NI application software installed on the same computer as NI VLM and you



 want the application software to validate its license using NI VLM, complete the



 following steps:

1. Launch NI License Manager.
2. Select »Manage Volume License Servers to add a volume license server.
 Note When the NILM is not
 connected to any servers, this step is equivalent to clicking Network
 Licenses from Views section and selecting
 Manage volume license servers.
3. Enter localhost (or 127.0.0.1 ) followed by colon and the Main
 Licensing Port ( 127.0.0.1 [:port]), if NI VLM is configured to use a
 non-default Main Licensing Port.
4. Click OK to exit.
5. Close NI License Manager.
6. In NI VLM, create a new computer in the Computers view



 with the server's computer name. Assign permissions to the new computer.
7. Click Apply Changes .
8. Relaunch your NI software.

Parent topic:

Managing the Volume License Server

<!--NI_TOPIC bundle=volume-license-manager path=managing-the-volume-license-server.html language=enus -->
## TOPIC 00063: Managing the Volume License Server

- bundle_id: `volume-license-manager`
- source_path: `managing-the-volume-license-server.html`
- source_url: https://docs-be.ni.com/bundle/volume-license-manager/raw/resource/enus/managing-the-volume-license-server.html
- document_id: `volume-license-manager`
- page_type: `leaf`
- content_type: `concept`
- source_description: Use a volume license server to manage volume licenses. Use the volume license server to perform tasks such as configuring preferences, handling permissions, and renewing agreements. To start an inactive server, click Start Volume License Server in the Status view, or select Tools Start Volume Licens

### Managing the Volume License Server

Use a volume license server to manage volume licenses. Use the volume license server to
 perform tasks such as configuring preferences, handling permissions, and renewing
 agreements.

To start an inactive server, click Start Volume License Server in
 the Status view, or select Tools»Start Volume License Server.

To stop an active server, click Stop Volume License Server in the
 Status view or select Tools»Stop Volume License Server.

Note

Parent topic:

Using Volume License Servers and Installers

<!--NI_TOPIC bundle=volume-license-manager path=managing-users-or-computers.html language=enus -->
## TOPIC 00064: Managing Users or Computers

- bundle_id: `volume-license-manager`
- source_path: `managing-users-or-computers.html`
- source_url: https://docs-be.ni.com/bundle/volume-license-manager/raw/resource/enus/managing-users-or-computers.html
- document_id: `volume-license-manager`
- page_type: `leaf`
- content_type: `concept`
- source_description: Manage the users or computers in NI VLM. Adding Users or Computers Adding Users in NI VLM In the Users view, click Add User. Complete the User Information section. A Username is required and must be unique. All other fields are optional. Add Groups or Explicit Licenses as necessary. Click Save. Addi

### Managing Users or Computers

Manage the users or computers in NI VLM.

Parent topic:

Managing, Monitoring, and Communicating with Clients

Related reference:

- nivlmcmd.exe Command Reference

#### Adding Users or Computers

##### Adding Users in NI VLM

1. In the Users view, click Add
 User .
2. Complete the User Information section. A
 Username is required and must be unique. All other
 fields are optional.
3. Add Groups or Explicit Licenses as
 necessary.
4. Click Save .

##### Adding Computers in NI VLM

1. In the Computers view, click Add
 Computer .
2. Complete the Computer Information section. A
 Computer Name is required and must be unique. All
 other fields are optional.
3. Add Groups or Explicit Licenses as
 necessary.
4. Click Save .

#### Editing Users or Computers

##### Editing Users

1. Select a user in the Users view and click Edit
 User or double-click the user.
2. Edit the User Information section as necessary. A
 Username is required and must be unique. All other
 fields are optional.
3. Add or remove Groups and Explicit
 Licenses as necessary.
4. Click Save to update the user.

##### Editing Computers

1. Select a computer in the Computers view and click
 Edit Computer or double-click the computer.
2. Edit the Computer Information section as necessary. A
 Computer Name is required and must be unique. All
 other fields are optional.
3. Add or remove Groups and Explicit
 Licenses as necessary.
4. Click Save to update the computer.

#### Deleting Users or Computers

1. In the Users or Computers view, select one or more
 clients to delete. Use the
 <Ctrl> and
 <Shift> keys to select
 multiple clients as necessary.
2. Click Delete User or Delete



 Computer .
3. To confirm the deletion, click Yes .

<!--NI_TOPIC bundle=volume-license-manager path=moving-to-another-server.html language=enus -->
## TOPIC 00065: Moving to Another Server

- bundle_id: `volume-license-manager`
- source_path: `moving-to-another-server.html`
- source_url: https://docs-be.ni.com/bundle/volume-license-manager/raw/resource/enus/moving-to-another-server.html
- document_id: `volume-license-manager`
- page_type: `leaf`
- content_type: `concept`
- source_description: Do not remove NI VLM from the old server until after you have completed these steps. Moving from a NI VLM 3.x Server Perform the following steps when you need to move NI VLM 3.x to another machine: If moving from an NI VLM 3.0 server, send the Activity Compliance Log (FileSave Activity Compliance Lo

### Moving to Another Server

Note

#### Moving from a NI VLM 3.x
 Server

Perform the following steps when you need to move NI VLM 3.x to
 another machine:

1. If moving from an NI VLM 3.0 server, send the Activity Compliance Log ( File»Save Activity Compliance Log ) from the current server to NI.
2. From within NI VLM on the current server, select the File»Backup/Restore menu item and complete the Back Up and Restore
 Wizard to back up the current NI VLM data, settings, and log
 data.
3. Copy the backup files to another location, such as a network drive or a USB
 drive.
4. Install NI VLM software onto your new server.
5. Complete the Getting Started
 Wizard that appears when you first launch NI VLM, selecting to import
 settings from a previous NI VLM 3. x installation.

#### Moving from a NI VLM 2.x
 Server

Perform the following steps when you need to move a NI VLM 2.x or
 earlier installation to another machine:

1. Send the Activity Compliance Log ( Options»Save Activity Compliance Log in NI VLM 2. x ) from the current server to
 NI.
2. Copy the configuration file ( nivlm.cfg ) and agreement license
 file ( nivlm.lic ) from the NI VLM installation directory on the
 current server to another location, such as a network drive or a USB drive.
3. Install NI VLM software onto your new server.
4. Complete the Getting Started
 Wizard that appears when you first launch NI VLM, selecting to import
 settings from a previous NI VLM 2. x installation.

#### Changing Volume License Server
 Settings on Client Machines

Once you have completed NI VLM setup, notify your clients of the change in server.
 They must then change the server name in their copy of NI License Manager using the
 following procedure:

1. Launch NI License Manager.
2. Select the top left icon and select the Manage Volume License Servers... 
 menu item.
3. Change the name in the Volume License Servers setting to the new server
 name, or to the new server IP.

Parent topic:

Managing the Volume License Server

<!--NI_TOPIC bundle=volume-license-manager path=ni-vlm-menu-items.html language=enus -->
## TOPIC 00066: VLM Menu Items

- bundle_id: `volume-license-manager`
- source_path: `ni-vlm-menu-items.html`
- source_url: https://docs-be.ni.com/bundle/volume-license-manager/raw/resource/enus/ni-vlm-menu-items.html
- document_id: `volume-license-manager`
- page_type: `leaf`
- content_type: `concept`
- source_description: Learn about the VLM menu items. If you make changes to the VLM configuration, click Apply Changes in the toolbar so that the changes take effect. File Menu Install Agreement License File Installs a new agreement license file in NI VLM. You must use this method to install any new agreement license fi

### VLM Menu
 Items

Learn about the VLM menu items.

Note

Apply Changes

#### File Menu

| Install Agreement License File | Installs a new agreement license file in NI VLM. You must use this method to install any new agreement license file. For more information, refer to Installing an Agreement License File. |
| --- | --- |
| Backup/Restore NI VLM | Backs up or restores NI VLM data, settings, and log files. For more information, refer to Backing up and Restoring NI VLM Data. |
| Load NI VLM Import Utility Data | Imports NI VLM Import Utility files into Permission Requests. For more information, refer to NI VLM Import Utility. |
| Exit | Exits NI VLM. |

#### View Menu

Note

Apply
 Changes

#### Tools Menu

| Start/Stop Volume License Server | Starts or stops the volume license server. A running volume license server is required to support your volume licenses. |
| --- | --- |
| Create Volume License Installer | Transforms a standard NI software installer into an installer suited for installation by your clients. For information, refer to Creating Volume License Installers. |
| Send VLA Log | Generates a VLA Log and either saves it or sends it automatically to NI, depending on what you select. For more information, refer toSending a VLA Log to NI or Renewing Expired Agreements. |
| Preferences | Helps you configure various options and policies. For more information, refer to Configuring NI VLM Preferences. |

#### Help Menu

| NI VLM Help | Launches the main VLM Help. |
| --- | --- |
| Current View Help | Launches theVLM Help topic for the current view. |
| Patents | Displays NI patent information. |
| About NI Volume License Manager | Displays information about VLM. |

Parent topic:

VLM User Interface

<!--NI_TOPIC bundle=volume-license-manager path=ni-vlm-user-interface.html language=enus -->
## TOPIC 00067: VLM User Interface

- bundle_id: `volume-license-manager`
- source_path: `ni-vlm-user-interface.html`
- source_url: https://docs-be.ni.com/bundle/volume-license-manager/raw/resource/enus/ni-vlm-user-interface.html
- document_id: `volume-license-manager`
- page_type: `leaf`
- content_type: `concept`
- source_description: Learn how to complete license administration tasks through the VLM user interface.

### VLM User
 Interface

Learn how to complete license administration tasks through the VLM user interface.

- [Working With the VLM User Interface](working-with-ni-vlm.html) Use the VLM user interface to move, filter, and sort data.
- [VLM Menu Items](ni-vlm-menu-items.html) Learn about the VLM menu items.
- [Status View](status-view.html) Use the Status view to display the system state and any important information or notices.
- [Licenses View](licenses-view.html) Use the Licenses view to manage the licenses in your volume license agreement.
- [Users View](users-view.html) Use the Users view to manage any users listed in NI VLM.
- [Computers View](computers-view.html) Use the Computers view to manage any computer listed in NI VLM.
- [Groups View](groups-view.html) Use the Groups view to manage any groups listed in NI VLM.
- [Reports View](reports-view.html) Use the Reports view to determine how licenses are used.
- [Permission Requests View](permission-requests-view.html) Use the Permission Requests view to accept or reject permission requests.

<!--NI_TOPIC bundle=volume-license-manager path=ni-volume-license-manager-help.html language=enus -->
## TOPIC 00068: VLM Overview

- bundle_id: `volume-license-manager`
- source_path: `ni-volume-license-manager-help.html`
- source_url: https://docs-be.ni.com/bundle/volume-license-manager/raw/resource/enus/ni-volume-license-manager-help.html
- document_id: `volume-license-manager`
- page_type: `leaf`
- content_type: `concept`
- source_description: NI Volume License Manager (VLM) is software for license administrators who need to manage and monitor their licensed NI software assets. Use VLM to administer your NI volume license agreements. To access the volume license agreement (VLA) community, visit ni.com/info and enter the info code VLACommu

### VLM
 Overview

NI Volume License Manager (VLM) is software for license administrators who need to
 manage and monitor their licensed NI software assets. Use VLM to administer your NI volume
 license agreements.

To access the volume license agreement (VLA) community, visit [ni.com/info](https://ni.com/info) and enter the
 info code VLACommunity.

To access troubleshooting information, visit [ni.com/info](https://ni.com/info) and enter the info code
 VLMTroubleshooting.

For additional assistance, contact NI Support.

#### VLM Key
 Features

VLM offers robust license management capabilities,
 including assigning licenses to user groups, creating volume license installers, and
 managing disconnected license files. VLM also enables
 exporting detailed analysis reports based on client data.

<!--NI_TOPIC bundle=volume-license-manager path=nivlm-commands.html language=enus -->
## TOPIC 00069: NiVlm.exe Command Reference

- bundle_id: `volume-license-manager`
- source_path: `nivlm-commands.html`
- source_url: https://docs-be.ni.com/bundle/volume-license-manager/raw/resource/enus/nivlm-commands.html
- document_id: `volume-license-manager`
- page_type: `leaf`
- content_type: `reference`
- source_description: You cannot run command line options with the main Volume License Manager binary (NiVlm.exe) while the NI VLM user interface is running. /backupUse this option to create a backup of NI VLM. You can also use this option with the Microsoft Windows task scheduler to back up NI VLM on a regular basis. Re

### NiVlm.exe Command
 Reference

Note

NiVlm.exe

#### /backup

Use this option to create a backup of
 NI VLM. You can also use this option with the Microsoft Windows task scheduler to
 back up NI VLM on a regular basis. Refer to the following example for typical
 usage.

```text
"C:\Program Files (x86)\National Instruments\Volume License Manager\NiVlm.exe" /backup "\\Server1\NIVLMBackUps\backups\"
```

#### /exportClientPermissions

Use this option to
 export the current permissions (clients, custom field values, and permissions) to a
 file. Refer to the following example for typical usage.

```text
"C:\Program Files (x86)\National Instruments\Volume License Manager\NiVlm.exe" /exportClientPermissions C:\temp\myFile.csv
```

#### /reconnect

Use this option to reconnect any
 expired disconnect concurrent licenses. Until a disconnected concurrent license is
 reconnected, the seat is not available for use by other clients. Refer to the
 following example for typical usage.

```text
"C:\Program Files (x86)\National Instruments\Volume License Manager\NiVlm.exe" /reconnect
```

Parent topic:

Command Line Interface Options

Related concepts:

- Scheduling Regular Backups
- Exporting Current Permissions
- Managing Disconnected License Files

<!--NI_TOPIC bundle=volume-license-manager path=nivlmcmd-commands.html language=enus -->
## TOPIC 00070: nivlmcmd.exe Command Reference

- bundle_id: `volume-license-manager`
- source_path: `nivlmcmd-commands.html`
- source_url: https://docs-be.ni.com/bundle/volume-license-manager/raw/resource/enus/nivlmcmd-commands.html
- document_id: `volume-license-manager`
- page_type: `leaf`
- content_type: `reference`
- source_description: Use the commands available with the nivlmcmd.exe binary to manage users, computers, and groups in VLM. You can also use the commands to export the activity history for clients and licenses. The nivlmcmd.exe file is located in the default VLM installation location: C:\Program Files (x86)\National Ins

### nivlmcmd.exe Command
 Reference

Use the commands available with the nivlmcmd.exe binary to manage
 users, computers, and groups in VLM. You can also use the commands to export the activity
 history for clients and licenses.

The nivlmcmd.exe file is located in the default VLM installation
 location: C:\Program Files (x86)\National Instruments\Volume License
 Manager\nivlmcmd.exe.

Note

nivlmcmd.exe

#### Global Parameters

--h

--help

-?

Tip

- All names, such as group ,
 user , computer ,
 license , and field , are
 not case-sensitive.
- If a name contains spaces, enclose the name in quotation marks. For example:
 "my group name" .
- To view field names for group details, navigate to Tools»Preferences»Custom Fields .
- Commands allow you to include multiple items, such as
 groups , users ,
 computers , and licenses , in a single
 command

Parent topic:

Command Line Interface Options

Related concepts:

- Managing Users or Computers

Related reference:

- NI VLM 2025 Q4

#### Computer Commands

Use the computer commands to add and remove computers, and view a list of computers
 using VLM.

##### computer
 add

Add a new computer to Volume License Manager. A computer name is required.

Note

| -id, --computerid | Computer ID in the format XXXX-XXXX-XXXX-XXXX. |
| --- | --- |
| -d, --detail | Computer details in the format "<field1>=<value1>". |

```text
nivlmcmd.exe computer add mycomputer -id K4K5-FQ8D-64GF-X8ZN -d "full name=John Doe" -d email=john@doe.com
```

```text
Successfully added computer: mycomputer
```

##### computer
 delete

Remove a computer from Volume License Manager. A computer name is required.

Note

```text
nivlmcmd.exe computer delete mycomputer
```

```text
Successfully deleted computer: mycomputer
```

##### computer
 list

List all computers in Volume License Manager.

```text
nivlmcmd.exe computer list
```

```text
computer1
computer2
computer3
```

#### Computer Group Commands

Manage computer groups in VLM.

##### computer-group add computer

Add computers to an existing computer group.

| <group-name> | Name of the computer group to which to add the computer. |
| --- | --- |
| <computer-name> | Name of the computer to add. |

```text
nivlmcmd.exe computer-group add computer mygroup computer1 
```

```text
nivlmcmd.exe computer-group add computer mygroup computer1 computer2 computer3 
```

##### computer-group add license

Add licenses to an existing computer group.

| <group-name> | Name of the computer group to which to add the license. |
| --- | --- |
| <package-name> | Name of the license package to add. |

```text
nivlmcmd.exe computer-group add license mygroup license1__PKG 
```

```text
nivlmcmd.exe computer-group add license mygroup license1__PKG license2__PKG license3__PKG 
```

##### computer-group create

Create new computer groups in VLM. One or more group names are required.

| <group-name> | Name of the computer group to create. Required argument. You can specify multiple group names. |
| --- | --- |

| -d | Computer group details in the format -d "<field1>=<value1>". Supported fields include visibility, description, permission request. You can also use --detail. |
| --- | --- |

```text
nivlmcmd.exe computer-group create mygroup
```

```text
nivlmcmd.exe computer-group create group1 group2 group3
```

```text
nivlmcmd.exe computer-group create computergroup -d visibility=public -d "permission request"=Manual -d description="Engineering team computers"
```

##### computer-group delete

Remove existing computer groups from VLM. One or more group names are required.

| <group-name> | Name of the computer group to delete. Required argument. You can specify multiple group names. |
| --- | --- |

| --f, --force | Delete without a confirmation prompt. |
| --- | --- |

```text
nivlmcmd.exe computer-group delete mygroup
```

```text
nivlmcmd.exe computer-group delete group1 group2 -f
```

##### computer-group list

List computer groups and their components in VLM.

| <group-name> | Name of the specific groups to list. Optional argument. If you do not specify a group, all groups are listed. |
| --- | --- |

| --c, --computers | List computers that are part of the group. |
| --- | --- |
| --l, --licenses | List licenses that are part of the group. |

Note

--computers

--licenses

```text
nivlmcmd.exe computer-group list 
```

```text
nivlmcmd.exe computer-group list mygroup 
```

```text
nivlmcmd.exe computer-group list mygroup --computers 
```

```text
nivlmcmd.exe computer-group list --licenses 
```

```text
nivlmcmd.exe computer-group list mygroup --computers --licenses 
```

##### computer-group remove computer

Remove computers from an existing computer group.

| <group-name> | Name of the computer group from which to remove the computer. |
| --- | --- |
| <computer-name> | Name of the computer to remove. |

```text
nivlmcmd.exe computer-group remove computer mygroup computer1 
```

```text
nivlmcmd.exe computer-group remove computer mygroup computer1 computer2 computer3 
```

##### computer-group remove license

Remove licenses from an existing computer group.

| <group-name> | Name of the computer group from which to remove the license. |
| --- | --- |
| <package-name> | Name of the license package to remove. |

```text
nivlmcmd.exe computer-group remove license mygroup license1__PKG 
```

```text
nivlmcmd.exe computer-group remove license mygroup license1__PKG license2__PKG license3__PKG
```

#### Export Commands

Use export commands to generate CSV files containing licenses and VLM activity
 history. This functionality supports reporting and data analysis tasks.

##### disconnected-usage

Exports disconnected license records in CSV format. You can specify a start date, an
 end date, or both to retrieve the history of disconnected usage. If you do not
 specify any dates, the system exports only the currently disconnected licenses.

| <directory> | Directory to export the disconnected usage report. |
| --- | --- |

| -s, --start-date | Start date in DD/MM/YYYY format. |
| --- | --- |
| -e, --end-date | End date in DD/MM/YYYY format. |

```text
nivlmcmd.exe disconnected-usage C:\Exports 
```

```text
nivlmcmd.exe disconnected-usage C:\Exports -s 01/01/2025 -e 31/12/2025 
```

##### export client-activity

Export client activity data to CSV format.

| <directory> | Directory to export the CSV file. |
| --- | --- |

| -c, --client- name | Name of the client to which you want to export the client activity. If you do not specify this option, all client activity is exported. |
| --- | --- |
| -s, --start-date | Start date in DD/MM/YYYY format. |
| -e, --end-date | End date in DD/MM/YYYY format. |

```text
nivlmcmd.exe export client-activity C:\Exports 
```

```text
nivlmcmd.exe export client-activity C:\Exports -c mycomputer 
```

```text
nivlmcmd.exe export client-activity C:\Exports -c mycomputer -s 01/01/2025 -e 31/12/2025
```

##### export license

Export list of all licenses to CSV format.

| <directory> | Directory to export the CSV file. |
| --- | --- |

```text
nivlmcmd.exe export licenses C:\Exports
```

##### export license-activity

Export license activity data to CSV format.

| <directory> | Directory to export the CSV file. |
| --- | --- |

| -l, --license- name | Package name of the license in which to export the activity. If you do not specify this option, all activity for all licenses is exported. Tip Use the export licenses command to find the package name of a license. |
| --- | --- |
| -s, --start-date | Start date in DD/MM/YYYY format. |
| -e, --end-date | End date in DD/MM/YYYY format. |

```text
nivlmcmd.exe export license-activity C:\Exports 
```

```text
nivlmcmd.exe export license-activity C:\Exports -l mylicense 
```

```text
nivlmcmd.exe export license-activity C:\Exports -l mylicense -s 01/01/2025 -e 31/12/2025 
```

#### User Commands

Commands for managing users in VLM.

##### user
 add

Add a user to Volume License Manager. A user name is required.

Note

| -d, --detail | User details in the format "<field1>=<value1>". |
| --- | --- |

```text
nivlmcmd.exe user add myuser -d "Full Name=John Doe" -d email=john@doe.com
```

```text
Successfully added user:myuser
```

##### user
 delete

Remove a user from VLM. A user name is required.

Note

```text
nivlmcmd.exe user delete myuser
```

```text
Successfully deleted user: myuser
```

##### user
 list

List all users in VLM.

```text
nivlmcmd.exe user list
```

```text
user1
user2
user3
```

#### User Groups Commands

Manage user groups in VLM.

##### user-group add user

Add users to an existing user group.

| <group-name> | Name of the user group to which to add the user. |
| --- | --- |
| <user-name> | Name of the user to add. |

```text
nivlmcmd.exe user-group add user mygroup user1 
```

```text
nivlmcmd.exe user-group add user mygroup user1 user2 user3 
```

##### user-group add license

Add licenses to an existing user group.

| <group-name> | Name of the user group to which to add the license. |
| --- | --- |
| <package-name> | Name of the license package to add. |

```text
nivlmcmd.exe user-group add license mygroup license1__PKG 
```

```text
nivlmcmd.exe user-group add license mygroup license1__PKG license2__PKG license3__PKG 
```

##### user-group create

Create new user groups.

| <group-name> | Name of the user group. |
| --- | --- |

| -d, --detail | User group details in the format -d "<field1>=<value1>". Supported fields include visibility, description, permission request. |
| --- | --- |

```text
nivlmcmd.exe user-group create mygroup 
```

```text
nivlmcmd.exe user-group create group1 group2 group3 
```

```text
nivlmcmd.exe user-group create usergroup -d visibility=public -d "permission request"=Manual -d description="Engineering team"
```

##### user-group delete

Delete existing user groups.

| <group-name> | Name of the user group. |
| --- | --- |

| -f, --force | Delete without a confirmation prompt. |
| --- | --- |

```text
nivlmcmd.exe user-group delete mygroup
```

```text
nivlmcmd.exe user-group delete group1 group2
```

##### user-group list

List user groups and their components in VLM.

| <group-name> | Name of the group components to list. Optional argument. If you do not specify a group, all user groups are listed. |
| --- | --- |

| -u, --users | List users who are part of the group. |
| --- | --- |
| -l, --licenses | List licenses that are part of the group. |

Note

--computers

--licenses

```text
nivlmcmd.exe user-group list 
```

```text
nivlmcmd.exe user-group list mygroup 
```

```text
nivlmcmd.exe user-group list mygroup --users 
```

```text
nivlmcmd.exe user-group list --licenses 
```

```text
nivlmcmd.exe user-group list mygroup --users --licenses 
```

##### user-group remove license

Remove licenses from an existing user group.

| <group-name> | Name of the user group from which to remove the license. |
| --- | --- |
| <user-name> | Name of the license package to remove. |

```text
nivlmcmd.exe user-group remove license mygroup license1__PKG 
```

```text
nivlmcmd.exe user-group remove license mygroup license1__PKG license2__PKG license3__PKG 
```

##### user-group remove user

Remove users from an existing user group.

| <group-name> | Name of the user group from which to remove the user. |
| --- | --- |
| <user-name> | Name of the user to remove. |

```text
nivlmcmd.exe user-group remove user mygroup user1
```

```text
nivlmcmd.exe user-group remove user mygroup user1 user2 user3
```

<!--NI_TOPIC bundle=volume-license-manager path=obtaining-a-computer-id.html language=enus -->
## TOPIC 00071: Obtaining a Computer ID

- bundle_id: `volume-license-manager`
- source_path: `obtaining-a-computer-id.html`
- source_url: https://docs-be.ni.com/bundle/volume-license-manager/raw/resource/enus/obtaining-a-computer-id.html
- document_id: `volume-license-manager`
- page_type: `leaf`
- content_type: `concept`
- source_description: To create a computer-based disconnected license or home license file, you first must obtain the computer ID of the computer for which the disconnected or home license file is being created. If you do not already have this information, have the client perform the following steps to obtain the compute

### Obtaining a Computer ID

To create a computer-based disconnected license or home license file, you first must



 obtain the computer ID of the computer for which the disconnected or home license



 file is being created. If you do not already have this information, have the client



 perform the following steps to obtain the computer ID:

1. Install the NI software they want to use onto their computer.
2. Launch NI License Manager and click Display Computer Information .

The client can contact you with the computer ID, which you will use to create a



 computer-based disconnected license or home license file. The client then installs



 the [disconnected](installing-disconnected-license-files.html) or [home license](installing-home-license-files.html) by dragging and dropping the license file onto NI License



 Manager. You can also use [NI Volume License Manager Import Utility](installing-disconnected-licenses-using-ni-vlm-import-utility.html) to install disconnected



 licenses.

Parent topic:

Specifying a Computer ID for a Home License File

<!--NI_TOPIC bundle=volume-license-manager path=obtaining-a-computer-id_2.html language=enus -->
## TOPIC 00072: Obtaining a Computer ID

- bundle_id: `volume-license-manager`
- source_path: `obtaining-a-computer-id_2.html`
- source_url: https://docs-be.ni.com/bundle/volume-license-manager/raw/resource/enus/obtaining-a-computer-id_2.html
- document_id: `volume-license-manager`
- page_type: `leaf`
- content_type: `concept`
- source_description: To create a computer-based disconnected license or home license file, you first must obtain the computer ID of the computer for which the disconnected or home license file is being created. If you do not already have this information, have the client perform the following steps to obtain the compute

### Obtaining a Computer ID

To create a computer-based disconnected license or home license file, you first must



 obtain the computer ID of the computer for which the disconnected or home license



 file is being created. If you do not already have this information, have the client



 perform the following steps to obtain the computer ID:

1. Install the NI software they want to use onto their computer.
2. Launch NI License Manager and click Display Computer Information .

The client can contact you with the computer ID, which you will use to create a



 computer-based disconnected license or home license file. The client then installs



 the [disconnected](installing-disconnected-license-files.html) or [home license](installing-home-license-files.html) by dragging and dropping the license file onto NI License



 Manager. You can also use [NI Volume License Manager Import Utility](installing-disconnected-licenses-using-ni-vlm-import-utility.html) to install disconnected



 licenses.

Parent topic:

Specifying Computer IDs for Disconnected License Files

<!--NI_TOPIC bundle=volume-license-manager path=obtaining-an-agreement-license-file.html language=enus -->
## TOPIC 00073: Obtaining an Agreement License File

- bundle_id: `volume-license-manager`
- source_path: `obtaining-an-agreement-license-file.html`
- source_url: https://docs-be.ni.com/bundle/volume-license-manager/raw/resource/enus/obtaining-an-agreement-license-file.html
- document_id: `volume-license-manager`
- page_type: `leaf`
- content_type: `task`
- source_description: You must acquire a new agreement license file whenever your volume license agreement is renewed or changes. Locate your computer ID and server name on the Status view. To obtain your agreement license file, send the following information to your local NI agreements representative at services@ni.com:

### Obtaining an Agreement License
 File

You must acquire a new agreement license file whenever your volume license agreement
 is renewed or changes.

1. Locate your computer ID and server name on the Status
 view.
2. To obtain your agreement license file, send the following information to your
 local NI agreements representative at services@ni.com: 
 Full name
 Email address
 Company name
 Service ID
 Computer ID
 Server Name
 Requested License Model
 Any additional information required by your agreement
 Note You must manage
 the agreement license file only from the computer from which the computer ID
 was generated. Using your computer ID as a key ensures that your agreement
 license file cannot be copied and used by anyone else.

NI does not use this information for any other purpose than generating the agreement
 license file.

You can find the NI Software Activation Privacy Statement at [ni.com/license/privacy](https://www.ni.com/en/about-ni/legal/privacy-statement.html).

Parent topic:

Managing the Volume License Server

<!--NI_TOPIC bundle=volume-license-manager path=obtaining-or-installing-an-agreement-license-file.html language=enus -->
## TOPIC 00074: Obtaining or Installing an Agreement License File

- bundle_id: `volume-license-manager`
- source_path: `obtaining-or-installing-an-agreement-license-file.html`
- source_url: https://docs-be.ni.com/bundle/volume-license-manager/raw/resource/enus/obtaining-or-installing-an-agreement-license-file.html
- document_id: `volume-license-manager`
- page_type: `leaf`
- content_type: `task`
- source_description: Select whether you have an NI VLM agreement license file for this computer.After the wizard completes, you can install new agreement license files from File Install Agreement License File . For more information, refer to Installing an Agreement License File Select I have an agreement license file fo

### Obtaining or Installing an Agreement License File

Note

File

»

Install Agreement License File

Installing an Agreement License
 File

- Select I have an agreement license file for this
 computer if you have already received an agreement license file
 for the computer you want to use as the volume license server.
  1. Select the agreement license file by clicking the ellipsis ([IMAGE alt='image' src='GUID-AFC70F11-B3D8-4056-B2A4-E10B674BFAB4-a5.png'])
 and browsing to its location.
- Select I do not have an agreement license file for this
 computer if you do not have an agreement license file for the
 computer that you want to use as the volume license server. 
 Note The Getting Started Wizard helps you prepare a request to obtain an
 agreement license file from NI.

Parent topic:

Completing the VLM Getting Started Wizard

Related concepts:

- Installing an Agreement License File

<!--NI_TOPIC bundle=volume-license-manager path=options.html language=enus -->
## TOPIC 00075: Selecting the Volume License Agreement Policies

- bundle_id: `volume-license-manager`
- source_path: `options.html`
- source_url: https://docs-be.ni.com/bundle/volume-license-manager/raw/resource/enus/options.html
- document_id: `volume-license-manager`
- page_type: `leaf`
- content_type: `task`
- source_description: Configure Volume License Agreement (VLA) policies to manage client permissions for using NI Update Service, sending error reports, and participating in the Customer Experience Improvement Program. These settings allow you to customize client access and data sharing preferences based on organizationa

### Selecting the Volume License Agreement
 Policies

Configure Volume License Agreement (VLA) policies to manage client permissions for
 using NI Update Service, sending error reports, and participating in the Customer Experience
 Improvement Program. These settings allow you to customize client access and data sharing
 preferences based on organizational requirements.

1. Select Tools»PreferencesVLA Policies.
2. Set the client policies associated with your volume license agreement. 
 PolicyDescriptionAllow clients to use NI Update
 Service
 This policy determines whether clients can view and download updates
 using NI Update Service.
 Choose one of the following options:
 Allow
 Allow only downloading of critical updates and
 patches
 Allow only viewing of updates
 Deny (default)
 You can view critical updates, notifications, and noncritical
 downloads by visiting [ni.com/info](https://www.ni.com/en/support/info-code.html) and entering
 each of the following Info Codes: updates and
 downloads.Allow clients to send error reports to
 NI
 This policy determines whether clients may send error report
 information to NI.
 Choose one of the following options:
 Allow (default)
 Deny
 Refer to [ni.com/privacy](http://digital.ni.com/express.nsf/bycode/rdpriv) for more
 information.Enroll clients in the Customer Experience Improvement
 Program
 This policy determines whether clients participate in the Customer
 Experience Improvement Program. This program helps NI improve the
 performance and capabilities of NI products by collecting data
 related to the use of these products.
 Choose one of the following options:
 Enroll
 Do not enroll
 Allow client to decide (default)
 Refer to [ni.com/privacy](http://digital.ni.com/express.nsf/bycode/rdpriv) for more
 information.

Parent topic:

Configuring NI VLM Preferences

<!--NI_TOPIC bundle=volume-license-manager path=permission-requests-view.html language=enus -->
## TOPIC 00076: Permission Requests View

- bundle_id: `volume-license-manager`
- source_path: `permission-requests-view.html`
- source_url: https://docs-be.ni.com/bundle/volume-license-manager/raw/resource/enus/permission-requests-view.html
- document_id: `volume-license-manager`
- page_type: `leaf`
- content_type: `concept`
- source_description: Use the Permission Requests view to accept or reject permission requests. Permissions requests are generated through the following methods: Clients running Volume License Installers can generate permission requests. Importing client data generates permission requests. Clients running NI License Mana

### Permission Requests View

Use the Permission Requests view to accept or reject
 permission requests.

Permissions requests are generated through the following methods:

- Clients running Volume License Installers can generate permission requests.
- Importing client data generates permission requests.
- Clients running NI License Manager 3.5 or later can generate permissions



 requests.

The Permission Request view displays the following



 information:

- Requester—Either a Username and/or a Computer Name
- Request Type
  - User Permission Request
  - Computer Permission Request
  - Legacy Permission Request
- Request Time

Note

Add/Remove Columns

#### Viewing Permission Request
 Information

[Expand](expanding-and-collapsing-rows.html)
 each permission request to view more information, including the following:

- Requested groups or licenses
- Client information, including custom fields

Note

Add/Remove Columns

#### Processing Permission Requests

For information on processing permission requests, refer to [Handling Permission Requests](handling-permission-requests.html).

#### Emailing Multiple Clients

From this view, you can also [email](sending-email-to-clients.html#GUID-7D446500-D605-4602-8772-135C9C0423E8) multiple clients associated with the selected permission



 requests.

Parent topic:

VLM User Interface

<!--NI_TOPIC bundle=volume-license-manager path=reconnecting-disconnected-users-or-computers.html language=enus -->
## TOPIC 00077: Reconnecting Disconnected Users or Computers

- bundle_id: `volume-license-manager`
- source_path: `reconnecting-disconnected-users-or-computers.html`
- source_url: https://docs-be.ni.com/bundle/volume-license-manager/raw/resource/enus/reconnecting-disconnected-users-or-computers.html
- document_id: `volume-license-manager`
- page_type: `leaf`
- content_type: `concept`
- source_description: Complete the following steps to reconnect one or more disconnected users or computers: Navigate to the Computers or Users view and select one or more clients you want to reconnect. Click Reconnect. Disconnected concurrent licenses that have expired are automatically reconnected when you click Apply

### Reconnecting Disconnected Users or Computers

Complete the following steps to reconnect one or more disconnected users or



 computers:

1. Navigate to the Computers or Users 



 view and select one or more clients you want to reconnect.
2. Click Reconnect .

Note

- Disconnected concurrent licenses that have expired are automatically
 reconnected when you click Apply Changes in NI VLM or
 when you launch NI VLM with the /reconnect command line option. Until a
 disconnected concurrent license is reconnected, the seat is not available
 for use by other clients.
- You cannot run command line options while the NI VLM user interface is
 running.

Parent topic:

Managing Disconnected License Files

<!--NI_TOPIC bundle=volume-license-manager path=renewing-expired-agreements.html language=enus -->
## TOPIC 00078: Renewing Expired Agreements

- bundle_id: `volume-license-manager`
- source_path: `renewing-expired-agreements.html`
- source_url: https://docs-be.ni.com/bundle/volume-license-manager/raw/resource/enus/renewing-expired-agreements.html
- document_id: `volume-license-manager`
- page_type: `leaf`
- content_type: `concept`
- source_description: Send a VLA Log to NI to renew an expired volume license agreement. The VLA Log records all instances of policy and permissions changes, including overdrafts. This information is encrypted to ensure that no one accidentally edits the VLA Log and invalidates the usage information. NI uses the VLA Log

### Renewing Expired Agreements

Send a VLA Log to NI to renew an expired volume license agreement.

The VLA Log records all instances of policy and permissions changes, including overdrafts. This
 information is encrypted to ensure that no one accidentally edits the VLA Log and
 invalidates the usage information.

NI uses the VLA Log to help determine appropriate agreement fees for renewal and,



 upon receipt of the VLA Log, NI returns to you a new agreement license file that



 reflects any changes in the quantity of licenses you own. When you receive the new



 agreement license file, install it following the directions in [Installing an Agreement License File](installing-an-agreement-license-file.html).

After 60 days past volume license agreement expiration, your software will stop working. NI
 generates a new agreement license file as soon as you send the VLA Log to NI.

At any time during the 60 days before the agreement expires or after the agreement



 expires, you can send your VLA Log to your local NI agreements representative to



 renew your software agreement.

For information on generating the VLA Log, refer to [Sending a VLA Log to NI](sending-a-vla-log-to-ni.html#GUID-3A2BB046-EFFA-4188-B1A5-5E00D31F9B0E).

Parent topic:

Managing the Volume License Server

Related tasks:

- Configuring Overdraft

<!--NI_TOPIC bundle=volume-license-manager path=reports-view.html language=enus -->
## TOPIC 00079: Reports View

- bundle_id: `volume-license-manager`
- source_path: `reports-view.html`
- source_url: https://docs-be.ni.com/bundle/volume-license-manager/raw/resource/enus/reports-view.html
- document_id: `volume-license-manager`
- page_type: `leaf`
- content_type: `concept`
- source_description: Use the Reports view to determine how licenses are used. From this view, you can view the following reports: License Activity shows how many hours each client used the specified license. Client Activity shows how many hours a specified client used each license. Seat Utilization shows how many seats

### Reports View

Use the Reports view to determine how licenses
 are used.

From this view, you can view the following reports:

- License Activity shows how many hours each client used the specified



 license.
- Client Activity shows how many hours a specified client used each



 license.
- Seat Utilization shows how many seats of a specified license each



 client used over time and provides detailed information about any



 overdrafts.
- Seat Utilization (Concurrent) shows how many seats of a specified



 license each client used over time and whether any clients were unable to check



 out the license because no seats were available.
- License Allocation shows, over time, how many seats each portion of



 your organization used, so that you can allocate costs accordingly.
- License Allocation (Concurrent) shows how many hours each portion of



 your organization used each license, so that you can allocate costs



 accordingly.
- Named-User EULA Compliance shows any instances of a client using a



 named-user license on more than three computers.

Parent topic:

VLM User Interface

<!--NI_TOPIC bundle=volume-license-manager path=requesting-an-agreement-license-file.html language=enus -->
## TOPIC 00080: Requesting an Agreement License File

- bundle_id: `volume-license-manager`
- source_path: `requesting-an-agreement-license-file.html`
- source_url: https://docs-be.ni.com/bundle/volume-license-manager/raw/resource/enus/requesting-an-agreement-license-file.html
- document_id: `volume-license-manager`
- page_type: `leaf`
- content_type: `concept`
- source_description: The wizard can help you request a new agreement license file through your default email program or save the request to a text file so that you can manually send it later. Select Send an email to NI using my default email client to have the wizard launch your default email client with a new email tha

### Requesting an Agreement License File

The wizard can help you request a new agreement license file through your default



 email program or save the request to a text file so that you can manually send it



 later.

- Select Send an email to NI using my default email client 



 to have the wizard launch your default email client with a new email that you



 can send to NI to request a new agreement license file. The email will be



 prepopulated with answers to the questionnaire in this wizard.
- Select Save the request to a text file so that I can manually send it
 later to save the necessary information to a text file. You can
 either attach the text file to an email message or open it and copy the text
 into your email message. Send the email request to services@ni.com.

Parent topic:

Obtaining or Installing an Agreement License File

<!--NI_TOPIC bundle=volume-license-manager path=resizing-and-rearranging-columns.html language=enus -->
## TOPIC 00081: Resizing and Rearranging Columns

- bundle_id: `volume-license-manager`
- source_path: `resizing-and-rearranging-columns.html`
- source_url: https://docs-be.ni.com/bundle/volume-license-manager/raw/resource/enus/resizing-and-rearranging-columns.html
- document_id: `volume-license-manager`
- page_type: `leaf`
- content_type: `concept`
- source_description: Resizing Columns To resize grid columns in a view, complete one of the following actions: Click at the end of a column and drag to the size you want. Double-click on the end of a column to fit to the contents. Right-click on a column header and select Best Fit All Columns. Rearranging Columns To rea

### Resizing and Rearranging Columns

#### Resizing Columns

[IMAGE alt='image' src='GUID-E95A6BE1-7601-424A-9A0A-BD8A4F8F1E19-a5.png']

To resize grid columns in a view, complete one of the following actions:

- Click at the end of a column and drag to the size you want.
- Double-click on the end of a column to fit to the contents.
- Right-click on a column header and select Best Fit All
 Columns .

#### Rearranging Columns

To rearrange the column order, click and drag columns to where you want to put



 them.

Parent topic:

Working With the VLM User Interface

<!--NI_TOPIC bundle=volume-license-manager path=restoring-ni-vlm-from-a-backup-file.html language=enus -->
## TOPIC 00082: Restoring NI VLM from a Backup File

- bundle_id: `volume-license-manager`
- source_path: `restoring-ni-vlm-from-a-backup-file.html`
- source_url: https://docs-be.ni.com/bundle/volume-license-manager/raw/resource/enus/restoring-ni-vlm-from-a-backup-file.html
- document_id: `volume-license-manager`
- page_type: `leaf`
- content_type: `concept`
- source_description: Complete the following steps to restore NI VLM data: In NI VLM, select the FileBackup/Restore NI VLM menu item to launch the Backup and Restore Wizard. Select Restore NI VLM. In the Restore from section, click the ellipsis () to launch a file browser and navigate to the backup file you want to use.

### Restoring NI VLM from a Backup File

Complete the following steps to restore NI VLM data:

1. In NI VLM, select the File»Backup/Restore NI VLM menu item to launch the Backup and Restore Wizard.
2. Select Restore NI VLM .
3. In the Restore from section, click the ellipsis ( ) to launch a file
 browser and navigate to the backup file you want to use. You can find your backup files in
 the backup directory you set in NI VLM preferences General settings . The backup
 file name has the following format: [default backup
 location]\yyyymmdd-hhmm.vlmbak .
4. Click Restore . Note NI
 VLM automatically backs up NI VLM's current
 configuration before restoring from the selected
 backup file. The automatic backup file name has the
 following format: [default backup
 location]\autobackup-yyyymmdd-hhmm.vlmbak.
5. Click Finish to exit the Backup and Restore Wizard.

Parent topic:

Backing up and Restoring NI VLM Data

<!--NI_TOPIC bundle=volume-license-manager path=reviewing-the-volume-license-installer-settings.html language=enus -->
## TOPIC 00083: Reviewing the Volume License Installer Settings

- bundle_id: `volume-license-manager`
- source_path: `reviewing-the-volume-license-installer-settings.html`
- source_url: https://docs-be.ni.com/bundle/volume-license-manager/raw/resource/enus/reviewing-the-volume-license-installer-settings.html
- document_id: `volume-license-manager`
- page_type: `leaf`
- content_type: `concept`
- source_description: Use this page to review the information for this Volume License Installer. Review the specifications you selected in previous pages. Click Back to return to previous pages and edit any settings. Review the list of source disks needed to create this Volume License Installer, if applicable. Ensure you

### Reviewing the Volume License Installer Settings

Use this page to review the information for this Volume License Installer.

1. Review the specifications you selected in previous pages. Click



 Back to return to previous pages and edit any



 settings.
2. Review the list of source disks needed to create this Volume License Installer,



 if applicable. Ensure you have all the source disks you need.
3. If the specifications are correct and you have all necessary source disks, click



 Build to create your Volume License Installer.

Parent topic:

Creating Volume License Installers

<!--NI_TOPIC bundle=volume-license-manager path=scheduling-regular-backups.html language=enus -->
## TOPIC 00084: Scheduling Regular Backups

- bundle_id: `volume-license-manager`
- source_path: `scheduling-regular-backups.html`
- source_url: https://docs-be.ni.com/bundle/volume-license-manager/raw/resource/enus/scheduling-regular-backups.html
- document_id: `volume-license-manager`
- page_type: `leaf`
- content_type: `concept`
- source_description: You can use the Microsoft Windows task scheduler to back up NI VLM on a regular basis. To schedule regular backups, create a scheduled task in Microsoft Windows for NI VLM and add the \backup [location] option. You can use the default backup location you set in the NI VLM preferences (ToolsPreferenc

### Scheduling Regular Backups

You can use the Microsoft Windows task scheduler to back up NI VLM on a regular



 basis.

To schedule regular backups, create a scheduled task in Microsoft Windows for NI VLM and add the
 \backup [location] option. You can use the default backup
 location you set in the NI VLM preferences (Tools»Preferences), or you can designate a new location using the optional
 [location] setting. For example:

```text
"C:\Program Files\National Instruments\Volume License Manager\NiVlm.exe" /backup "\\Server1\NIVLMBackUps\backups\"
```

Note

- You cannot run command line options while the NI VLM user interface is
 running.
- Specifying a backup location on the command line does not change the default
 backup location you specified in the NI VLM preferences.
- Scheduled backups do not run when NI VLM is open.

Parent topic:

Backing up and Restoring NI VLM Data

Related reference:

- NiVlm.exe Command Reference

<!--NI_TOPIC bundle=volume-license-manager path=selecting-disconnected-license-output-methods.html language=enus -->
## TOPIC 00085: Selecting Disconnected License Output Methods

- bundle_id: `volume-license-manager`
- source_path: `selecting-disconnected-license-output-methods.html`
- source_url: https://docs-be.ni.com/bundle/volume-license-manager/raw/resource/enus/selecting-disconnected-license-output-methods.html
- document_id: `volume-license-manager`
- page_type: `leaf`
- content_type: `concept`
- source_description: Specify the actions to take with the disconnected license files. You can select one or both of the following options: Select Save the disconnected license files to save the license files to a local drive, a network drive, a USB drive, or another location to which your clients have access. Select Ema

### Selecting Disconnected License Output Methods

Specify the actions to take with the disconnected license files. You can select one



 or both of the following options:

- Select Save the disconnected license files to save the



 license files to a local drive, a network drive, a USB drive, or another



 location to which your clients have access.
- Select Email the disconnected license files to your



 clients to email the licenses to clients. If the email server is



 not set up, click Configure Email Settings to launch the



 Email Server preferences dialog box. Refer to Configuring Email Server Settings for more information about email



 server configuration.

Parent topic:

Managing Disconnected License Files

<!--NI_TOPIC bundle=volume-license-manager path=selecting-home-license-output-methods.html language=enus -->
## TOPIC 00086: Selecting Home License Output Methods

- bundle_id: `volume-license-manager`
- source_path: `selecting-home-license-output-methods.html`
- source_url: https://docs-be.ni.com/bundle/volume-license-manager/raw/resource/enus/selecting-home-license-output-methods.html
- document_id: `volume-license-manager`
- page_type: `leaf`
- content_type: `concept`
- source_description: Specify the actions to take with the home license file. You can select one or both of the following options: Select Save home license file to save your license file to a local drive, a network drive, a USB drive, or another location to which your client has access. Select Email home license file to

### Selecting Home License Output Methods

Specify the actions to take with the home license file. You can select one or both of



 the following options:

- Select Save home license file to save your license file



 to a local drive, a network drive, a USB drive, or another location to which



 your client has access.
- Select Email home license file to client to to send the



 license file in an email. Enter the client's email address. If the email server



 is not set up, click Configure Email Settings to launch



 the Email Server preferences dialog box. Refer to Configuring Email Server Settings for more information about email



 server configuration.

Parent topic:

Creating Home License Files

<!--NI_TOPIC bundle=volume-license-manager path=selecting-the-distribution-method.html language=enus -->
## TOPIC 00087: Selecting the Distribution Method

- bundle_id: `volume-license-manager`
- source_path: `selecting-the-distribution-method.html`
- source_url: https://docs-be.ni.com/bundle/volume-license-manager/raw/resource/enus/selecting-the-distribution-method.html
- document_id: `volume-license-manager`
- page_type: `leaf`
- content_type: `concept`
- source_description: Specify the distribution method for this Volume License Installer, as follows: Select Configure the Volume License Installer to run from a network drive to eliminate disk prompts for clients and prepare the installer to run from a network location. Select Configure the Volume License Installer to ru

### Selecting the Distribution Method

Specify the distribution method for this Volume License Installer, as follows:

- Select Configure the Volume License Installer to run from a network



 drive to eliminate disk prompts for clients and prepare the



 installer to run from a network location.
- Select Configure the Volume License Installer to run from a CD or



 DVD to ensure that the size of the installer remains under the



 size limit of the media. Use this option if you intend to burn this Volume



 License Installer onto media.

Parent topic:

Creating Volume License Installers

<!--NI_TOPIC bundle=volume-license-manager path=selecting-the-installer-source-destination-and-volume-license-installer-name.html language=enus -->
## TOPIC 00088: Selecting the Installer Source, Destination, and Volume License Installer Name

- bundle_id: `volume-license-manager`
- source_path: `selecting-the-installer-source-destination-and-volume-license-installer-name.html`
- source_url: https://docs-be.ni.com/bundle/volume-license-manager/raw/resource/enus/selecting-the-installer-source-destination-and-volume-license-installer-name.html
- document_id: `volume-license-manager`
- page_type: `leaf`
- content_type: `concept`
- source_description: Specify the source, destination, and name for this Volume License Installer, as follows: In the Installer Source field, click the ellipsis () to select the offline installer source file you downloaded. The installer source file's name is generally setup.exe or install.exe In the Installer Destinatio

### Selecting the Installer Source, Destination, and Volume License Installer Name

Specify the source, destination, and name for this Volume License Installer, as



 follows:

1. In the Installer Source field, click the ellipsis ( ) to select
 the offline installer source file you downloaded. The installer source file's
 name is generally setup.exe or install.exe
2. In the Installer Destination field, click the ellipsis ( ) to browse
 to the location where you want to save your Volume License Installer. You can
 select a shared location that your clients can access or you can select a local
 drive if you want to redistribute the software on other media.
3. In the Installer Name field, enter a name to describe



 this Volume License Installer. You will typically enter the product name and



 version, such as LabVIEW 2012. This field prepopulates if you are creating a



 Volume License Installer from a multiple-product suite, such as NI Developer



 Suite.
4. In the Installer Executable Name field, select a file



 name from the drop-down list.

Note

Installer
 Destination

Installer Name

Volume License Installer Location

Parent topic:

Creating Volume License Installers

<!--NI_TOPIC bundle=volume-license-manager path=selecting-the-volume-license-server.html language=enus -->
## TOPIC 00089: Selecting the Volume License Server

- bundle_id: `volume-license-manager`
- source_path: `selecting-the-volume-license-server.html`
- source_url: https://docs-be.ni.com/bundle/volume-license-manager/raw/resource/enus/selecting-the-volume-license-server.html
- document_id: `volume-license-manager`
- page_type: `leaf`
- content_type: `concept`
- source_description: Specify how client machines should be configured when running the Volume License Installer, as follows: Select Configure client machines to connect to a volume license server to checkout licenses to point client machines to the specified volume license server to check out licenses. The Volume Licens

### Selecting the Volume License Server

Specify how client machines should be configured when running the Volume License



 Installer, as follows:

- Select Configure client machines to connect to a volume license



 server to checkout licenses to point client machines to the



 specified volume license server to check out licenses. The Volume License



 Installer wizard prepopulates this field. You can change it if you have special



 requirements. You can enter either a simple server name, fully qualified



 domain name, or the server's IP address. You can also configure a client



 machine to look at a specific port on a volume license server, the [Main Licensing Port](glossary.html#GUID-BD309744-95F6-4B4A-9381-0F22348BB3E8). Enter the volume license server name



 followed by colon and the Main Licensing Port: server[:port]. For example,



 the following are all legal server



 names:serverserver:27000server.domain.com:28432127.0.0.2When



 no Main Licensing Port is specified, 27000 is implied. Main Licensing Ports



 range from 1-64000, inclusive.
- Select Do not configure client machines to connect to a volume



 license server to checkout licenses if you do not want to



 configure client machines to point to a volume license server. Select this



 option if your organization uses only disconnected licenses.

Parent topic:

Creating Volume License Installers

<!--NI_TOPIC bundle=volume-license-manager path=sending-a-vla-log-to-ni.html language=enus -->
## TOPIC 00090: Sending a VLA Log to NI

- bundle_id: `volume-license-manager`
- source_path: `sending-a-vla-log-to-ni.html`
- source_url: https://docs-be.ni.com/bundle/volume-license-manager/raw/resource/enus/sending-a-vla-log-to-ni.html
- document_id: `volume-license-manager`
- page_type: `leaf`
- content_type: `concept`
- source_description: Use the VLA Log Wizard to generate and send a VLA Log to NI. Launch the VLA Log Wizard from the ToolsSend VLA Log menu item, and the wizard will walk you through the following steps to generate and send a VLA Log to NI. Generating a VLA Log Specify the reason and date range, as follows: Select the R

### Sending a VLA Log to NI

Use the VLA Log Wizard to generate and send a VLA Log to NI.

Launch the VLA Log Wizard from the Tools»Send VLA Log menu item, and the wizard will walk you through the following steps
 to generate and send a VLA Log to NI.

Parent topic:

Managing, Monitoring, and Communicating with Clients

Related tasks:

- Completing VLM Setup

#### Generating a VLA Log

Specify the reason and date range, as follows:

1. Select the Reason for sending VLA Log . Choose from one of the following
 options: Option
 ReasonAgreement renewal
 Your volume license agreement is expiring and you want to
 renew it.
 Send client information
 You want to update client information to grant access to
 NI technical support.
 Overdrafted with
 pay-as-you-go
 You want to enable the pay-as-you-go option and assign a
 license that increases the overdraft usage.
 Other
 You want to send a log for another reason. Note You can automatically send VLA logs by navigating to Preferences»General»Automatically send VLA Log to NI.
2. If you selected Other , enter a reason in Other



 reason and then enter a Date range .
3. Click Next .

#### Specifying the Output Method

You can select one of two ways to send your VLA Log to NI:

- Send the VLA Log now
  1. Select Send VLA Log now to send the VLA Log to NI
 immediately over a secure Internet connection.
  2. Click Send .
- Save the VLA Log to send it later
  1. Select Save VLA Log to send



 it later manually to send the VLA Log later.
  2. Click Save .
  3. Select a location to



 store the file and click Save .
  4. Contact NI at services@ni.com to send your VLA Log to NI later.

#### Sending the Specified VLA Log to NI

The VLA Log wizard generates the VLA Log and either saves it to a file or sends it,



 depending on what you selected in the previous screen.

- Click Cancel to stop VLA Log generation and delete the



 partially generated VLA Log.
- Click Back to edit your choices.

#### Finishing the VLA Log Wizard

If you selected Send VLA Log now, Volume License Manager immediately
 sends the log to NI. If you selected Save VLA Log to send it later
 manually, you can click the link to open the log's location.

Click
 Finish to exit the wizard.

VLA Log Frequently Asked
 Questions

#### VLA Log Frequently Asked Questions

The VLA Log records policy and permissions changes in NI VLM and is used to ensure
 compliance with NI contractual terms. It includes detailed information about user and computer
 permissions, license files, and overdraft settings. The log can be securely sent to NI, and
 users have the option to manage its submission preferences.

##### What is a VLA Log and How Does NI Use It?

NI VLM records into the VLA Log all instances of policy and permissions changes, including
 overdrafts. You send the VLA Log to NI in following scenarios:

- When your current agreement is expiring
- When your User or Computer list has changed
- When you have added overdraft permissions under the pay-as-you-go option
- When you plan to move NI VLM to another computer

NI uses the information in the VLA Log to ensure compliance with NI contractual terms. The
 information allows NI to determine how much, if anything, is owed on the extra licenses and
 maintenance for the coming agreement period. NI sends you a new agreement license file based
 on whether you renewed the agreement.

##### What Information Is Included in my VLA
 Log?

- The date permissions were added and removed from each User or Computer
- The date a client was disconnected or a home license was created
- The date a disconnected client was reconnected
- Check-in and check-out events
- The contents of each agreement license file
- The overdraft percentage, if overdraft is enabled
- Whether pay-as-you-go is enabled

##### How
 do I Manually Send the VLA Log to NI?

Contact NI at services@ni.com to send your VLA
 Log to NI.

##### Why Can't I Read the VLA Log?

[Reporting](creating-reports.html) gives you access to almost all information included in the VLA


 Log. You can review the reports before sending your VLA Log to NI or before asking


 questions about billing.

##### How Can I Ensure that my VLA Log is Sent to NI Securely?

The VLA Log Wizard encrypts the VLA Log file with a private key before transfer. The wizard sends
 it to NI using an HTTPS connection, the Internet standard for secure data transfer.

##### How Does NI Protect my Privacy When I Send my VLA
 Log?

To view how NI collects, uses and protects your data, refer to the *NI
 Privacy Statement*.

##### Can I Opt Out of Sending my VLA Log?

Yes, you
 can opt out of automatically sending the VLA log in the VLM Preferences dialog. Go to Tools»Preferences»General»Automatically send VLA log to NI.

Related information:

- NI Privacy Statement

<!--NI_TOPIC bundle=volume-license-manager path=sending-email-to-clients.html language=enus -->
## TOPIC 00091: Sending Emails to Clients

- bundle_id: `volume-license-manager`
- source_path: `sending-email-to-clients.html`
- source_url: https://docs-be.ni.com/bundle/volume-license-manager/raw/resource/enus/sending-email-to-clients.html
- document_id: `volume-license-manager`
- page_type: `leaf`
- content_type: `concept`
- source_description: Use the Email Clients Wizard to email one or more clients. Before using the Email Clients Wizard, you must configure the NI VLM email settings. Click Configure Email Settings to launch the Email Server preferences dialog box. For more information about email server configuration, refer to Configurin

### Sending Emails to Clients

Use the Email Clients Wizard to email one or more clients.

Before using the Email Clients Wizard, you must configure the NI
 VLM email settings. Click Configure Email Settings to launch
 the Email Server preferences dialog box.

For more information about email server configuration, refer to [Configuring Email Server
 Settings](configuring-email-server-settings.html).

Parent topic:

Managing, Monitoring, and Communicating with Clients

#### Editing Email Addresses

Use this page to add or edit the selected client email addresses.

1. Click in the Email column to edit an email address.
2. Check Overwrite the email addresses stored in NI VLM with these email



 addresses if you want to correct or update the current client



 information stored in NI VLM. This option is not available if you are sending an



 email to clients using the Permission Requests view.

#### Adding Email Content

Use this page to enter the message you want to send to the selected clients.

1. Enter a subject.
2. Enter the message text. Administrator information is appended if available, but



 you can edit it here if necessary.
3. Click Send to send the message to the selected



 clients.

#### Finishing the Wizard

This page displays the list of clients to whom the wizard successfully sent



 email.

If NI VLM encountered any issues while sending email, click



 Back to verify client email addresses and email server



 settings.

<!--NI_TOPIC bundle=volume-license-manager path=setting-an-expiration-date-for-a-home-license-file.html language=enus -->
## TOPIC 00092: Setting an Expiration Date for a Home License File

- bundle_id: `volume-license-manager`
- source_path: `setting-an-expiration-date-for-a-home-license-file.html`
- source_url: https://docs-be.ni.com/bundle/volume-license-manager/raw/resource/enus/setting-an-expiration-date-for-a-home-license-file.html
- document_id: `volume-license-manager`
- page_type: `leaf`
- content_type: `concept`
- source_description: Specify when the home license should expire. You can select from the following options: Select Expire upon license file expiration to use the expiration date of your license file. Select Expire on a specific date to select the date on which the home license file will expire. The selected date cannot

### Setting an Expiration Date for a Home License File

Specify when the home license should expire. You can select from the following



 options:

- Select Expire upon license file expiration to use the expiration date of
 your license file.
- Select Expire on a specific date to select the date on which the home
 license file will expire. The selected date cannot be after the license file
 expiration.
- Select Never expire to create a perpetual home license file. Note This option is available for
 users and computers that only use perpetual licenses. You cannot select this
 option for users and computers that use a mix of perpetual and non-perpetual
 licenses.

Once you have selected an expiration date, click Create to



 create the home license file.

Parent topic:

Creating Home License Files

<!--NI_TOPIC bundle=volume-license-manager path=setting-an-expiration-date-for-disconnected-license-files.html language=enus -->
## TOPIC 00093: Setting an Expiration Date for Disconnected License Files

- bundle_id: `volume-license-manager`
- source_path: `setting-an-expiration-date-for-disconnected-license-files.html`
- source_url: https://docs-be.ni.com/bundle/volume-license-manager/raw/resource/enus/setting-an-expiration-date-for-disconnected-license-files.html
- document_id: `volume-license-manager`
- page_type: `leaf`
- content_type: `concept`
- source_description: Specify when the disconnected licenses should expire. You can select from the following options: Select Expire upon license file expiration to use the expiration date of your license file. Select Expire on a specific date to choose the disconnected license file expiration date. The selected date can

### Setting an Expiration Date for Disconnected License Files

Specify when the disconnected licenses should expire. You can select from the



 following options:

- Select Expire upon license file expiration to use the expiration date of
 your license file.
- Select Expire on a specific date to choose the disconnected license file
 expiration date. The selected date cannot be after the license file
 expiration.
- Select Never expire to create a perpetual disconnected license file.
 Note This option is
 available for users and computers that only use perpetual licenses. You
 cannot select this option for users and computers that use a mix of
 perpetual and non-perpetual licenses.

Once you have selected an expiration date, click Disconnect to



 create the disconnected license files.

Parent topic:

Managing Disconnected License Files

<!--NI_TOPIC bundle=volume-license-manager path=setting-overdraft-policies.html language=enus -->
## TOPIC 00094: Setting Overdraft Policies

- bundle_id: `volume-license-manager`
- source_path: `setting-overdraft-policies.html`
- source_url: https://docs-be.ni.com/bundle/volume-license-manager/raw/resource/enus/setting-overdraft-policies.html
- document_id: `volume-license-manager`
- page_type: `leaf`
- content_type: `task`
- source_description: Select whether you want to enable overdraft in order to add new seats to your volume license agreement automatically and pay for them later. You can also specify the amount of overdraft and set pay-as-you-go. Allow an overdraft policy to use more licenses than the agreement specifies and pay for the

### Setting Overdraft
 Policies

Select whether you want to enable overdraft in order to add new seats
 to your volume license agreement automatically and pay for them
 later. You can also specify the amount of overdraft and set
 pay-as-you-go.

Allow an overdraft policy to use more licenses
 than the agreement specifies and pay for them
 later.

Note

Note

1. Select the Tools»Preferences menu item.
2. Select Overdraft in
 the navigation tree.
3. Check Allow overdraft
 if you want to allow overdraft. 
 Note This setting applies to all products in your
 agreement license file, except those products that
 use concurrent licenses. You must accept the terms
 and conditions notification before overdraft can
 be enabled in NI VLM.
4. Use the slider to set the overdraft
 percentage. This percentage is the amount of
 licenses that you can use in addition to your
 purchased agreement licenses.
5. Check Enable
 pay-as-you-go if you want to enable
 pay-as-you-go. This setting reminds you when you
 overdraft licenses to send your VLA Log to NI in
 order to cover the overdraft by purchasing the
 corresponding licenses. 
 Note 
 You do not need to select pay-as-you-go in
 order to enable overdrafts. If you do not check
 pay-as-you-go, you will pay for the overdrafted
 licenses at your volume license agreement
 renewal.
 If you enable pay-as-you-go, the license
 maintenance will be prorated when you pay for the
 license. If you do not enable pay-as-you-go, the
 license maintenance will not be prorated. For more
 information on renewing agreements, refer to
 *Renewing Expired Agreements*.

The overdraft policy is
 configured, and you can now use additional
 licenses as per the settings.

Parent topic:

Configuring NI VLM Preferences

<!--NI_TOPIC bundle=volume-license-manager path=setting-up-ni-vlm.html language=enus -->
## TOPIC 00095: Setting up VLM

- bundle_id: `volume-license-manager`
- source_path: `setting-up-ni-vlm.html`
- source_url: https://docs-be.ni.com/bundle/volume-license-manager/raw/resource/enus/setting-up-ni-vlm.html
- document_id: `volume-license-manager`
- page_type: `leaf`
- content_type: `concept`
- source_description: Learn how to setup VLM to administer your volume licenses. Before you begin, review the NI Volume License Agreement Startup Kit. For more information, refer to Getting Started With NI Volume License Manager (VLM). You must have Administrator privileges on the host machine operating system to install

### Setting up VLM

Learn how to setup VLM to administer your volume
 licenses.

Before you begin, review the NI Volume License Agreement Startup Kit. For more information, refer
 to *Getting Started With NI Volume License Manager (VLM)*.

Note

Related information:

- Getting Started With NI Volume License Manager (VLM)

<!--NI_TOPIC bundle=volume-license-manager path=specifying-a-computer-id-for-a-home-license-file.html language=enus -->
## TOPIC 00096: Specifying a Computer ID for a Home License File

- bundle_id: `volume-license-manager`
- source_path: `specifying-a-computer-id-for-a-home-license-file.html`
- source_url: https://docs-be.ni.com/bundle/volume-license-manager/raw/resource/enus/specifying-a-computer-id-for-a-home-license-file.html
- document_id: `volume-license-manager`
- page_type: `leaf`
- content_type: `concept`
- source_description: You must enter a Computer ID for the home computer on which you want to install the home license file. For information on how to obtain a Computer ID, refer to Obtaining a Computer ID.

### Specifying a Computer ID for a Home License File

You must enter a Computer ID for the home computer on which you want to install the



 home license file.

For information on how to obtain a Computer ID, refer to [Obtaining a Computer ID](obtaining-a-computer-id.html).

Parent topic:

Creating Home License Files

<!--NI_TOPIC bundle=volume-license-manager path=specifying-computer-ids-for-disconnected-license-files.html language=enus -->
## TOPIC 00097: Specifying Computer IDs for Disconnected License Files

- bundle_id: `volume-license-manager`
- source_path: `specifying-computer-ids-for-disconnected-license-files.html`
- source_url: https://docs-be.ni.com/bundle/volume-license-manager/raw/resource/enus/specifying-computer-ids-for-disconnected-license-files.html
- document_id: `volume-license-manager`
- page_type: `leaf`
- content_type: `concept`
- source_description: If a computer does not have a Computer ID on record in NI VLM, enter it in the Computer ID field. You must have at least one computer with a Computer ID in order to proceed. For more information about Computer IDs, refer to Obtaining a Computer ID.

### Specifying Computer IDs for Disconnected License Files

If a computer does not have a Computer ID on record in NI VLM, enter it in the



 Computer ID field. You must have at least one computer



 with a Computer ID in order to proceed.

For more information about Computer IDs, refer to [Obtaining a Computer ID](obtaining-a-computer-id.html).

Parent topic:

Managing Disconnected License Files

<!--NI_TOPIC bundle=volume-license-manager path=user-manual-welcome.html language=enus -->
## TOPIC 00098: VLM User Manual

- bundle_id: `volume-license-manager`
- source_path: `user-manual-welcome.html`
- source_url: https://docs-be.ni.com/bundle/volume-license-manager/raw/resource/enus/user-manual-welcome.html
- document_id: `volume-license-manager`
- page_type: `leaf`
- content_type: `concept`
- source_description: The VLM User Manual provides detailed descriptions of the product functionality and the step by step processes for use. Looking for Something Else?For information not found in the User Manual for your product, such as specifications and API reference, browse Related Information.

### VLM
 User Manual

The VLM User Manual provides detailed
 descriptions of the product functionality and the step by step processes for use.

#### Looking for Something Else?

For information not found in the User Manual
 for your product, such as specifications and API reference, browse *Related
 Information*.

Related information:

- Getting Started With Volume License Manager
- Volume License Manager Compatibility
- Volume License Manager Release Notes
- Volume License Manager Download
- Verify Domain of Volume License Manager

<!--NI_TOPIC bundle=volume-license-manager path=using-command-line-interface-options.html language=enus -->
## TOPIC 00099: Command Line Interface Options

- bundle_id: `volume-license-manager`
- source_path: `using-command-line-interface-options.html`
- source_url: https://docs-be.ni.com/bundle/volume-license-manager/raw/resource/enus/using-command-line-interface-options.html
- document_id: `volume-license-manager`
- page_type: `leaf`
- content_type: `reference`
- source_description: Command line options enable you to automate certain tasks when managing volume licenses. Refer to the command reference available for the niVlm.exe and nivlmcmd.exe binaries to learn more about available options.

### Command Line Interface Options

Command line options enable you to automate certain tasks when managing volume licenses.
 Refer to the command reference available for the niVlm.exe and
 nivlmcmd.exe binaries to learn more about available
 options.

Parent topic:

Automating VLM Operations

<!--NI_TOPIC bundle=volume-license-manager path=using-license-files.html language=enus -->
## TOPIC 00100: Using License Files

- bundle_id: `volume-license-manager`
- source_path: `using-license-files.html`
- source_url: https://docs-be.ni.com/bundle/volume-license-manager/raw/resource/enus/using-license-files.html
- document_id: `volume-license-manager`
- page_type: `leaf`
- content_type: `concept`
- source_description: Learn how to grant electronic permissions for client computers to use NI products.

### Using License Files

Learn how to grant electronic permissions for client computers to use NI
 products.

- [Installing Agreement License Files](installing-agreement-license-files.html#GUID-CED9C408-389C-44AC-AB85-FBD5DCD9DE8E) Use the Agreement License File Installation Wizard to install a new agreement license file into NI VLM and transfer permissions from your old licenses to your new licenses.
- [Creating Home License Files](creating-home-license-files.html) Enable a client to install and run NI products included in a volume license agreement on a home computer.
- [Managing Disconnected License Files](managing-disconnected-license-files.html) Enable a client to use an NI product included in a volume license agreement while not attached to the network.

<!--NI_TOPIC bundle=volume-license-manager path=using-temporary-network-licenses.html language=enus -->
## TOPIC 00101: Using Temporary Network Licenses

- bundle_id: `volume-license-manager`
- source_path: `using-temporary-network-licenses.html`
- source_url: https://docs-be.ni.com/bundle/volume-license-manager/raw/resource/enus/using-temporary-network-licenses.html
- document_id: `volume-license-manager`
- page_type: `leaf`
- content_type: `concept`
- source_description: Temporary network licenses are created on client machines when a licensed software program launches. Temporary network licenses ensure software access in the event that the volume license server is unreachable from the client machine, because the network was down, the volume license server was stopp

### Using Temporary Network Licenses

Temporary network licenses are created on client machines when a licensed software



 program launches. Temporary network licenses ensure software access in the event



 that the volume license server is unreachable from the client machine, because the



 network was down, the volume license server was stopped, or because the client



 machine was disconnected from the network. The NI software must have previously been



 checked out successfully for the temporary license to be generated.

The temporary network license is valid for 14 days from the first time the license is



 used. During this time, the client's software runs but displays a warning message



 each time the client launches the product.

Note

Parent topic:

Managing the Volume License Server

Related concepts:

- Managing Disconnected License Files

<!--NI_TOPIC bundle=volume-license-manager path=using-the-ni-vlm-import-utility.html language=enus -->
## TOPIC 00102: Using the NI VLM Import Utility

- bundle_id: `volume-license-manager`
- source_path: `using-the-ni-vlm-import-utility.html`
- source_url: https://docs-be.ni.com/bundle/volume-license-manager/raw/resource/enus/using-the-ni-vlm-import-utility.html
- document_id: `volume-license-manager`
- page_type: `leaf`
- content_type: `concept`
- source_description: Collect client data, such as computer IDs and information from custom fields, without using volume license installers. You can also use NI VLM Import Utility to install disconnected licenses generated by NI VLM on disconnected computers. Collecting Client Data Complete the following steps to use NI

### Using the NI VLM Import Utility

Collect client data, such as computer IDs and information from custom
 fields, without using volume license installers.

Note

Parent topic:

Automating VLM Operations

#### Collecting Client Data

Complete the following steps to use NI VLM Import Utility to collect client



 information:

1. Copy everything in the Import Utility directory to a network drive or portable
 media, such as a USB drive, or the client machine. You can find the utility in
 the following locations: Windows 11/10/8/7/Vista
 C:\ProgramData\National Instruments\Volume
 License Manager\Import Utility\
 Windows XP
 C:\Documents and Settings\All Users\Application
 Data\National Instruments\Volume License Manager\Import
 Utility\ Note NI VLM
 Import Utility uses an XML file, nivlmImportUtility.xml, to
 determine the custom fields that are available, which fields clients must
 complete, and which are optional. The
 nivlmImportUtility.xml file updates whenever you change
 [custom fields](configuring-custom-fields.html). If you modify the custom fields, you must copy
 the updated nivlmImportUtility.xml to where you use NI VLM
 Import Utility.
2. Have clients complete the following steps:
  1. Run



 nivlmImportUtility.exe on the computer that they



 want to add to NI VLM.
  2. Click Submit



 Information and complete the form. Required fields are



 marked with an asterisk (*).
  3. Clients should save the resulting



 XML file in a common place, such as a network location, or email the



 file to you.
3. Refer to Importing Client Data to import client



 information.

Related tasks:

- Completing VLM Setup

#### Importing Client Data

Once you have collected the resultant XML files from all necessary clients by using



 the NI VLM Import Utility, you can add the information to NI VLM.

Complete the following steps to import client data into NI VLM:

1. From within NI VLM, select File»Load NI VLM Import Utility Data .
2. Browse to the location of the import utility files and select all the files that



 you want to import. You can select multiple files by holding the <Shift>



 or <Ctrl> keys as you make your selections.
3. Click Open .

Loading import utility data will add entries to the Permission



 Requests queue. You will then need to accept the permission



 requests. Refer to [Handling Permission Requests](handling-permission-requests.html) for more information.

Related tasks:

- Completing VLM Setup

#### Installing Disconnected Licenses using NI VLM Import Utility

Complete the following steps on each client machine to install disconnected license



 files using the NI VLM Import Utility:

1. Create disconnected license files. For more information, refer to Creating a Disconnected License File .
2. Copy everything in the Import Utility directory to a network drive or portable
 media, such as a USB drive, or the client machine. You can find the utility in
 the following locations: Windows 11/10/8/7/Vista
 C:\ProgramData\National Instruments\Volume
 License Manager\Import Utility\
 Windows XP
 C:\Documents and Settings\All Users\Application
 Data\National Instruments\Volume License Manager\Import
 Utility\ Note NI VLM
 Import Utility uses an XML file, nivlmImportUtility.xml, to
 determine the custom fields that are available, which fields clients must
 complete, and which are optional. The
 nivlmImportUtility.xml file updates whenever you change
 [custom fields](configuring-custom-fields.html). If you modify the custom fields, you must copy
 the updated nivlmImportUtility.xml to where you use NI VLM
 Import Utility.
3. Save the disconnected license files in the same storage location as NI VLM



 Import Utility.
4. Have clients complete the following steps:
  1. Run



 nivlmImportUtility.exe on the computer to which



 they want to install the disconnected license files.
  2. Click



 Install License Files to copy and install the



 appropriate disconnected license files onto the target client



 machine.

<!--NI_TOPIC bundle=volume-license-manager path=using-volume-license-servers-and-installers.html language=enus -->
## TOPIC 00103: Using Volume License Servers and Installers

- bundle_id: `volume-license-manager`
- source_path: `using-volume-license-servers-and-installers.html`
- source_url: https://docs-be.ni.com/bundle/volume-license-manager/raw/resource/enus/using-volume-license-servers-and-installers.html
- document_id: `volume-license-manager`
- page_type: `leaf`
- content_type: `concept`
- source_description: Learn how to use volume license servers and volume license installers.

### Using Volume License Servers and
 Installers

Learn how to use volume license servers and volume license installers.

- [Managing the Volume License Server](managing-the-volume-license-server.html) Use a volume license server to manage volume licenses. Use the volume license server to perform tasks such as configuring preferences, handling permissions, and renewing agreements.
- [Configuring Client Machines](configuring-client-machines.html#GUID-E660616A-9112-4451-8205-F766E634DBBD) Configure each client machine to point to a volume license server.
- [Creating Volume License Installers](creating-volume-license-installers.html) Use the Volume License Installer Wizard to create a Volume License Installer for your NI products.
- [Adding the NI Device Driver DVD to a Volume License Installer](adding-the-ni-device-driver-dvd-to-a-volume-license-installer.html) Add the NI Device Drivers DVD to your volume license installer to eliminate disk prompts in your network-based volume license installers.

<!--NI_TOPIC bundle=volume-license-manager path=whats-new-in-ni-vlm.html language=enus -->
## TOPIC 00104: VLM New Features and Changes

- bundle_id: `volume-license-manager`
- source_path: `whats-new-in-ni-vlm.html`
- source_url: https://docs-be.ni.com/bundle/volume-license-manager/raw/resource/enus/whats-new-in-ni-vlm.html
- document_id: `volume-license-manager`
- page_type: `leaf`
- content_type: `concept`
- source_description: Learn about updates, including new features and behavior changes, introduced in each version of VLM. Discover what is new in the latest releases of VLM. If you cannot find new features and changes for your version, it might not include user-facing updates. However, your version might include non-vis

### VLM New
 Features and Changes

Learn about updates, including new features and behavior changes, introduced in each
 version of VLM.

Discover what is new in the latest releases of VLM.

Note

Release Notes

#### NI VLM 2025 Q4

##### New Features

- Added new command line interface options for the nivlmcmd.exe binary, including:
  - Group management commands to facilitate the management of user groups
 and computer groups.
  - Export command to export users, computer and license activity, and current licenses in
 use.
  - Disconnected usage export command to view current or historical
 disconnected license usage.
- Added UI functionality that allows administrators to export all user email
 addresses from VLM into a CSV file. This functionality simplifies the process of
 bulk-adding users to agreements on ni.com.

##### Changes

- Updated VLA logs to collect only business-required data. The log excludes administrative
 information and custom fields, except for location-related fields such as City,
 State/Province, Country, and Location.

Related reference:

- nivlmcmd.exe Command Reference

#### NI VLM 2024 Q4

##### New Features

- Additional command line interface support — Added new command line interface
 ( nivlmcmd.exe ) for managing users and computers.
- Notifications — Added new e-mail notification to admins for failed VLA log
 submission.
- Custom fields — Added new required custom fields for participants in the
 Enterprise Agreement Program:
  - City
  - State/Province
  - Country
- Users and computers — Added a new tab to display currently disconnected licenses.

##### Changes

- FlexNet Publisher — Upgraded FlexNet Publisher to version 11.19.6 to address security
 vulnerabilities.
- VLA log — Changed default setting to automatically send VLA logs.
- Disconnected licenses — Never Expire option now only available for
 perpetual licenses.
- Help manuals — Improved offline help experience.
- Troubleshooting — Improved logging of license file installation and restore
 operations.

#### NI VLM 2023 Q1

##### New Features

- OS support — Added OS support for Windows 11, Windows Server 2019, and Windows
 Server 2022.
- TLS support — Added TLS 1.2 encryption support for SMTP email server
 connections.

##### Changes

- CEIP data — In the VLA policies tab, the default
 value for Customer Experience Improvement Program (CEIP) data collection is
 set to Allow client to decide . Each client can select
 whether to participate in the program or not. CEIP records NI product data
 to improve the performance and capabilities of those products.
- SQLite databases — NI VLM automatically migrates existing SQL CE databases
 into SQLite. To access and restore a SQL CE backup, use the NI VLM Database
 Migration Tool. This support tool is included as a recommended package when
 downloading the NI VLM installer from NI Package Manager.

#### NI VLM 3.3

##### New Features

- Custom fields — Restrict custom field values to a discrete list of options.
- Log files — Create a .zip file for all required debug log
 files. Select Tools»Save Debug Log Files menu item to save all debug files as a .zip 
 file.
- Server logs — Enable a user option to either append or overwrite the server
 log.
