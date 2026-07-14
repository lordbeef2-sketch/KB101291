# NI DOCUMENT BUNDLE: license-manager

<!--NI_BUNDLE_CHUNK bundle=license-manager start=1 end=15 -->
<!--NI_TOPIC bundle=license-manager path=20-7-new-changes-and-features.html language=enus -->
## TOPIC 00001: License Manager 20.7 to 21.8 Compatibility and Support Changes

- bundle_id: `license-manager`
- source_path: `20-7-new-changes-and-features.html`
- source_url: https://docs-be.ni.com/bundle/license-manager/raw/resource/enus/20-7-new-changes-and-features.html
- document_id: `license-manager`
- page_type: `leaf`
- content_type: `reference`
- source_description: License Manager 20.7 to 21.8 makes changes to compatibility and support. License Manager 20.7 to 21.8 is only compatible with Volume License Manager 3.2.2 and later. If you are using FlexNet Publisher instead of Volume License Manager, License Manager 20.7 to 21.8 is only compatible with FlexNet Pub

### License Manager 20.7 to 21.8 Compatibility
 and Support Changes

License Manager 20.7 to 21.8 makes changes to compatibility and support.

- License Manager 20.7 to 21.8 is only compatible with Volume License Manager 3.2.2 and
 later.
- If you are using FlexNet Publisher instead of Volume License Manager, License Manager 20.7
 to 21.8 is only compatible with FlexNet Publisher 11.16.4 and later.
- License Manager is dropping support for Windows 7, Windows 8.1, Windows Server 2008 R2,
 Windows Server 2012 R2, and all 32-bit Windows operating systems in 2021.
 Versions of this product that ship after May 1, 2021, may not install or
 execute correctly on these operating systems. This includes both the server
 executable lmgrd.exe and the vendor daemon
 nilm.exe . For detailed information about NI
 operating system support, visit ni.com/r/win32bitsupport .

Parent topic:

License Manager New Features and Changes

Related information:

- NI Support for Windows 7, Windows 8.1, Windows Server 2008 R2, Windows Server
 2012 R2, and All 32-Bit Windows

<!--NI_TOPIC bundle=license-manager path=2022q4-new-features-and-changes.html language=enus -->
## TOPIC 00002: License Manager 21.8.1 New Features

- bundle_id: `license-manager`
- source_path: `2022q4-new-features-and-changes.html`
- source_url: https://docs-be.ni.com/bundle/license-manager/raw/resource/enus/2022q4-new-features-and-changes.html
- document_id: `license-manager`
- page_type: `leaf`
- content_type: `reference`
- source_description: License Manager 21.8.1 adds new features. This release includes the following major improvements: Entitlement-based and serial number-based license subscriptions are automatically renewed upon launching NI License Manager.Your licenses fail to automatically renew if you are not connected to the netw

### License Manager 21.8.1 New Features

License Manager 21.8.1 adds new features.

This release includes the following major improvements:

- Entitlement-based and serial number-based license subscriptions are automatically renewed
 upon launching NI License Manager. Note Your licenses fail to
 automatically renew if you are not connected to the network, if you are
 logged out of your NI user account, if your entitlement or serial number is
 not linked to your NI user account, if you have an offline activation that
 requires manual renewal, or if there is a server error.
- Some software products have built-in grace periods that allow you to use
 software past the end of the subscription term.

Parent topic:

License Manager New Features and Changes

<!--NI_TOPIC bundle=license-manager path=4-4-new-features-and-changes.html language=enus -->
## TOPIC 00003: License Manager 4.4 to 4.7 Compatibility Changes

- bundle_id: `license-manager`
- source_path: `4-4-new-features-and-changes.html`
- source_url: https://docs-be.ni.com/bundle/license-manager/raw/resource/enus/4-4-new-features-and-changes.html
- document_id: `license-manager`
- page_type: `leaf`
- content_type: `reference`
- source_description: License Manager 4.4 to 4.7 makes changes to compatibility. License Manager 4.4 to 4.7 is only compatible with Volume License Manager 3.1.1 and later. If you are using FlexNet Publisher instead of Volume License Manager, License Manager 4.4 to 4.7 is only compatible with FlexNet Publisher 11.15.0 and

### License Manager 4.4 to 4.7 Compatibility
 Changes

License Manager 4.4 to 4.7 makes changes to compatibility.

- License Manager 4.4 to 4.7 is only compatible with Volume License Manager 3.1.1 and
 later.
- If you are using FlexNet Publisher instead of Volume License Manager, License Manager 4.4
 to 4.7 is only compatible with FlexNet Publisher 11.15.0 and later.

Parent topic:

License Manager New Features and Changes

<!--NI_TOPIC bundle=license-manager path=activating.html language=enus -->
## TOPIC 00004: Activating Software

- bundle_id: `license-manager`
- source_path: `activating.html`
- source_url: https://docs-be.ni.com/bundle/license-manager/raw/resource/enus/activating.html
- document_id: `license-manager`
- page_type: `leaf`
- content_type: `task`
- source_description: Activate software products using NI License Manager. Before you begin, purchase a license for NI software and create a user account on ni.com. If you are transferring software to another endpoint, review the NI Software License Agreement for information regarding transfer and seat limitations. If yo

### Activating Software

Activate software products using NI License Manager.

Before you begin, purchase a license for
 NI software and create a user account on ni.com.

Note

1. Click Activate Software.
2. Activate NI software. 
 Option
Activation Type
DescriptionCheck my account for licenses
Online
Log in to your NI user account to check for licenses associated with your
 account to activate software.
If your account lacks the appropriate license for software, activate the
 product using an activation code or a serial number.
Enter a serial number
Online
Log in to your NI user account and enter a serial number to activate software. Find serial
 numbers in the following locations:On the Certificate of Ownership
 included in your software kit.
 On the product's packing slip
 or shipping label.
 On a previously installed
 version of your application software, by selecting Help»About.Note Visit How to Find
 the Serial Number or System Tag of My NI Hardware for the latest information
 regarding locating a serial number
Enter activation codes
Online/Offline
Enter an activation code to activate software. To receive an activation code,
 log in to your NI user account and click Generate an activation
 code or visit ni.com/activate.Note 
Your code is sent to your email inbox after you submit the Activation
 Code Generation form.
Connect to a volume license server
Online/Offline
Provide the volume license server address where NI software should check for
 licenses. Note For home use
 through a volume license agreement, request a license file from your volume
 license administrator. 
 Note If you were using a trial version of
 NI software before you began the activation process, you may need to restart the
 software.

License Manager attempts to automatically
 renew licenses when their subscription term ends.

Use the software immediately after activation.

Related tasks:

- Setting up Volume License Server Access
- Installing a License File
- Extending an Evaluation Period Manually

Related information:

- MyNI Dashboard
- Understanding NI Software Policies
- How to find the Serial Number or System Tag of My NI Product

<!--NI_TOPIC bundle=license-manager path=automate-activation.html language=enus -->
## TOPIC 00005: Automating Software Activation

- bundle_id: `license-manager`
- source_path: `automate-activation.html`
- source_url: https://docs-be.ni.com/bundle/license-manager/raw/resource/enus/automate-activation.html
- document_id: `license-manager`
- page_type: `leaf`
- content_type: `reference`
- source_description: License administrators or NI software delivery managers can automate software activation and add volume license servers. To do so, run License Manager from the command line or from a batch file using NILicensingCmd.exe. The path for NILicensingCmd.exe is as follows: For 64-bit computers: Program Fil

### Automating Software Activation

License administrators or NI software delivery managers can automate software
 activation and add volume license servers.

To do so, run License Manager from the command line or from a batch
 file using NILicensingCmd.exe.

NILicensingCmd.exe

- For 64-bit computers: Program Files
 (x86)\National Instruments\Shared\License Manager\NILicensingCmd.exe

Note

#### Software Activation Command-Line
 Flags

Below is a table containing common command-line flags associated with software activation.
 You can see descriptions of the License Manager command-line flags by entering the command
 NILicensingCmd.exe /help.

| Flag | Description | Syntax | Example(s) |
| --- | --- | --- | --- |
| /activateall | Launches the Activate Software window. This command is equivalent to clicking the Activate Software button in License Manager. | NILicensingCmd.exe /silent /activateall /serialnumber <serial number> | NILicensingCmd.exe /silent /activateall /serialnumber A11B11C11 |
| /activate /type package | Launches the Activate Software window with a preselected package or family. These commands are equivalent to right-clicking on software or family in License Manager and selecting Activate Software. | NILicensingCmd.exe /activate /type package /name <packagename> /version <version> /serialnumber <serial number> | NILicensingCmd.exe /activate /type package /name LabVIEW_PDS_PKG /version 17.0000 /serialnumber A111A1A11 |
| /activate /type family | NILicensingCmd.exe /activate /type family /name <familyname> /serialnumber <serial number> | NILicensingCmd.exe /activate /type family /name LabVIEW_ADE_170000 /serialnumber A12B12345 |  |
| /applyactivationcodes | Activates one or more licenses using the activation codes provided. This command is equivalent to clicking activate software and selecting Enter activation codes in License Manager. | NILicensingCmd.exe /applyactivationcodes [<activation code1>,<activation code2>, [, ...]] | NILicensingCmd.exe /applyactivationcodes 5CFL-Q7JG-X7GV-XL83-NDSM,FHFZ-V3MP-S3RY-FHRJ-69HY |
| /silent | Activates a software silently. Note This command requires an Internet connection that allows access to the NI website over an encrypted web connection (https). Serial numbers are optional for silent activation. If you log into your NI User Account before running command-line arguments, License Manager checks your account for any necessary software licenses. Silent activation fails if you: You enter incorrect or incomplete information, such as an invalid serial number You are not logged in to your account You have conflicting licenses associated with your account You do not have the necessary licenses associated with your account and did not pass any serial numbers as parameters Note If silent activation fails, error messages do not interrupt the remaining automation scripts. You must manually activate the failed activations before you can use your software. | NILicensingCmd.exe /silent /activate /type package /name <packagename> /version <version> /serialnumber <serial number> | NILicensingCmd.exe /silent /activate /type package /name LabVIEW_PDS_PKG /version 9.0000 /serialnumber A111A1A11 |
| /addservers | Silently points a computer to a volume license server to check out licenses. This command is equivalent to selecting » Manage Volume License Servers to add a volume license server. | NILicensingCmd.exe /addservers servername[:portnumber][,servername[:portnumber],...] | NILicensingCmd.exe /addservers server1 NILicensingCmd.exe /addservers server1:28000 NILicensingCmd.exe /addservers server1:28000,server2 |

Related tasks:

- Activating Software
- Setting up Volume License Server Access

Related information:

- NI Volume License Program for Software

<!--NI_TOPIC bundle=license-manager path=deactivate-transfer.html language=enus -->
## TOPIC 00006: Deactivating Software

- bundle_id: `license-manager`
- source_path: `deactivate-transfer.html`
- source_url: https://docs-be.ni.com/bundle/license-manager/raw/resource/enus/deactivate-transfer.html
- document_id: `license-manager`
- page_type: `leaf`
- content_type: `task`
- source_description: Use License Manager to deactivate a software license on a computer or virtual machine. If you intend to transfer software to another endpoint, review the NI Software License Agreement for information regarding transfer and seat limitations. If you use NI Volume License Manager to manage NI software

### Deactivating Software

Use License Manager to deactivate a software license on a computer or virtual
 machine.

Note

1. Click Local Licenses.
2. Select a licensed software.
3. In the 
 Actions section, click 
 Deactivate.
4. In the 
 Deactivate dialog box, click 
 Yes. 
 Note Once software is deactivated, reuse
 the activation code to activate the software on another endpoint.

Related tasks:

- Activating Software

Related information:

- NI Downloads
- Understanding NI Software Policies
- General Purpose Software License Agreement

<!--NI_TOPIC bundle=license-manager path=eval.html language=enus -->
## TOPIC 00007: Evaluation Periods

- bundle_id: `license-manager`
- source_path: `eval.html`
- source_url: https://docs-be.ni.com/bundle/license-manager/raw/resource/enus/eval.html
- document_id: `license-manager`
- page_type: `leaf`
- content_type: `concept`
- source_description: During an evaluation period, you are allowed to use the product with certain limitations, such as reduced functionality and limited execution time, for a predetermined amount of time. Once the evaluation period ends, you must purchase the product to continue using it. You can evaluate most NI produc

### Evaluation Periods

During an evaluation period, you are allowed to use the product with certain
 limitations, such as reduced functionality and limited execution time, for a predetermined
 amount of time.

Once the evaluation period ends, you must purchase the product to continue using it. You can
 evaluate most NI products, in accordance with the NI license agreement.

You can automatically or manually extend the evaluation period for most products by using
 License Manager.

Note

Parent topic:

NI License Manager Manual

Related information:

- Understanding NI Software Policies

<!--NI_TOPIC bundle=license-manager path=extend-eval-manual.html language=enus -->
## TOPIC 00008: Extending an Evaluation Period Manually

- bundle_id: `license-manager`
- source_path: `extend-eval-manual.html`
- source_url: https://docs-be.ni.com/bundle/license-manager/raw/resource/enus/extend-eval-manual.html
- document_id: `license-manager`
- page_type: `leaf`
- content_type: `task`
- source_description: Use License Manager to manually extend the evaluation period for software when you cannot automatically extend the evaluation period. Click Local Licenses. Right-click the unlicensed software and select Activate. If prompted to log in, click LOG IN TO ACTIVATE. Enter your NI User Account credentials

### Extending an Evaluation Period
 Manually

Use License Manager to manually extend the evaluation period for software when you
 cannot automatically extend the evaluation period.

1. Click Local Licenses.
2. Right-click the unlicensed software and select Activate. 
 Note If prompted to log in, click
 LOG IN TO ACTIVATE. Enter your NI User Account credentials and
 click Log in.
3. Extend the trial. 
 OptionDescriptionExtending the trial online
 Click EXTEND TRIAL.Extending the trial offline
 Visit ni.com/extendevaluation to acquire an evaluation
 code.
 Enter your Computer ID when prompted on the website.Note You can find the Computer ID in
 NI License Manager in the General section, by clicking
 Computer Information or on the Activate
 Software window.
 Enter the evaluation code in the Activate Software
 window. Click ACTIVATE.
4. Click 
 FINISH.

Parent topic:

Evaluation Periods

Related reference:

- Automating Product Activation

Related information:

- Understanding NI Software Policies
- MyNI Dashboard
- Extending Your Evaluation

<!--NI_TOPIC bundle=license-manager path=license-file-install.html language=enus -->
## TOPIC 00009: Installing a License File

- bundle_id: `license-manager`
- source_path: `license-file-install.html`
- source_url: https://docs-be.ni.com/bundle/license-manager/raw/resource/enus/license-file-install.html
- document_id: `license-manager`
- page_type: `leaf`
- content_type: `task`
- source_description: Use License Manager to install a license file that you receive from NI or from the administrator of a volume license server. Select Install License File . Choose a license file to install. License Manager updates to reflect the addition of the new license files. You may need to activate new licenses

### Installing a License File

Use License Manager to install a license file that you receive from NI or from the
 administrator of a volume license server.

1. Select [IMAGE alt='image' src='GUID-4BADACB4-3362-48F1-8A3F-855B57ACF50F-a5.gif']»Install License File.
2. Choose a license file to install.

License Manager updates to reflect the
 addition of the new license files.

You may need to activate new licenses.

Related tasks:

- Activating Software

<!--NI_TOPIC bundle=license-manager path=license-manager-2025-q4.html language=enus -->
## TOPIC 00010: License Manager 2025 Q4 New Features

- bundle_id: `license-manager`
- source_path: `license-manager-2025-q4.html`
- source_url: https://docs-be.ni.com/bundle/license-manager/raw/resource/enus/license-manager-2025-q4.html
- document_id: `license-manager`
- page_type: `leaf`
- content_type: `concept`
- source_description: License Manager 2025 Q4 adds a new flag. This release includes the following improvements: New flag /applyactivationcodes has been added to Automating Software Activation.

### License Manager 2025 Q4 New Features

License Manager 2025 Q4 adds a new flag.

This release includes the following improvements:

- New flag /applyactivationcodes has been added to
 Automating Software Activation .

Parent topic:

License Manager New Features and Changes

<!--NI_TOPIC bundle=license-manager path=license-manager-overview.html language=enus -->
## TOPIC 00011: License Manager Overview

- bundle_id: `license-manager`
- source_path: `license-manager-overview.html`
- source_url: https://docs-be.ni.com/bundle/license-manager/raw/resource/enus/license-manager-overview.html
- document_id: `license-manager`
- page_type: `leaf`
- content_type: `concept`
- source_description: License Manager helps you manage licensed NI software assets.

### License Manager
 Overview

License Manager helps you manage licensed NI software
 assets.

<!--NI_TOPIC bundle=license-manager path=manual-overview.html language=enus -->
## TOPIC 00012: What is License Manager and Who Is It For?

- bundle_id: `license-manager`
- source_path: `manual-overview.html`
- source_url: https://docs-be.ni.com/bundle/license-manager/raw/resource/enus/manual-overview.html
- document_id: `license-manager`
- page_type: `leaf`
- content_type: `reference`
- source_description: License Manager is software that license administrators use to control access to software using license activation. Use License Manager to automate product activation and add volume license servers. Key Features The features that set NI License Manager apart. The Key Features topic is a list of the

### What is License Manager and Who Is It
 For?

License Manager is software that license administrators use to control access to
 software using license activation. Use License Manager to automate product activation and add
 volume license servers.

#### Key Features

The features that set NI License Manager apart.

- Activating a
 Product
- Deactivating and
 Transferring a Product
- Installing a
 License File
- Activation
 Automation

#### Capabilities of License Manager

| Objective | Required Software |
| --- | --- |
| Manage and activate individual licenses. | License Manager |
| Manage and activate licenses in conjunction with a license server. | License Manager, Volume License Server or FlexNet Publisher |

<!--NI_TOPIC bundle=license-manager path=new-features-and-changes.html language=enus -->
## TOPIC 00013: License Manager New Features and Changes

- bundle_id: `license-manager`
- source_path: `new-features-and-changes.html`
- source_url: https://docs-be.ni.com/bundle/license-manager/raw/resource/enus/new-features-and-changes.html
- document_id: `license-manager`
- page_type: `leaf`
- content_type: `concept`
- source_description: Learn about updates, including new features and behavior changes, introduced in each version of License Manager. Discover what is new in the latest releases of License Manager.If you cannot find new features and changes for your version, it might not include user-facing updates. However, your versio

### License Manager
 New Features and Changes

Learn about updates, including new features and behavior changes, introduced in each
 version of License Manager.

License Manager

Note

Release Notes

<!--NI_TOPIC bundle=license-manager path=user-manual-welcome.html language=enus -->
## TOPIC 00014: License Manager User Manual

- bundle_id: `license-manager`
- source_path: `user-manual-welcome.html`
- source_url: https://docs-be.ni.com/bundle/license-manager/raw/resource/enus/user-manual-welcome.html
- document_id: `license-manager`
- page_type: `leaf`
- content_type: `concept`
- source_description: The License Manager User Manual provides detailed descriptions of the product functionality and the step by step processes for use. Looking for Something Else?For information not found in the User Manual for your product, such as specifications and API reference, browse Related Information.

### License Manager
 User Manual

The License Manager User Manual provides detailed
 descriptions of the product functionality and the step by step processes for use.

#### Looking for Something Else?

For information not found in the User Manual
 for your product, such as specifications and API reference, browse *Related
 Information*.

Related information:

- License Manager Compatibility
- License Manager Release Notes
- Verify Domain of License Manager and Volume License
 Manager
- License Manager Download
- License Manager Third-Party SDK Download

<!--NI_TOPIC bundle=license-manager path=using-volume-license-server.html language=enus -->
## TOPIC 00015: Using a Volume License Server

- bundle_id: `license-manager`
- source_path: `using-volume-license-server.html`
- source_url: https://docs-be.ni.com/bundle/license-manager/raw/resource/enus/using-volume-license-server.html
- document_id: `license-manager`
- page_type: `leaf`
- content_type: `concept`
- source_description: Use NI License Manager to check out licenses from a volume license server. Setting up Volume License Server Access Use License Manager to enable the use of a volume license server. You must have a Volume License Agreement with NI to access a volume license server to check out NI products. A volume l

### Using a Volume License Server

Use NI License Manager to check out licenses from a volume license server.

#### Setting up Volume License Server
 Access

Use License Manager to enable the use of a volume license server.

Note

A *volume license server* is a computer that is used to manage volume licenses
 for NI products on a given network. For details on your company's volume license server,
 contact your volume license administrator. For more information about the NI Volume License
 Program, visit the NI Volume License Program for Software web page.

Note

localhost

127.0.0.1

1. Select [IMAGE alt='image' src='GUID-4BADACB4-3362-48F1-8A3F-855B57ACF50F-a5.gif']»Manage Volume License Servers.
2. Enter the names of the volume license servers on which your NI products should check
 for licenses. Separate
 these
 names with commas. 
 Note You can configure your products to
 check a specific port on a volume license server. Enter the following,
 separated
 by a colon:volume license server name
 port number 27000 is implied when there is no port specified. Ports range from 1-64000,
 inclusive. For example, if you enter server1, server2:28001,
 server3 and launch a product that requires a license. Your product first
 checks port 27000 of server1 for a valid license, then moves to port
 28001 of server2, port 27000 of server3, and finally
 your local system. If your product does not find a license on any of the volume license
 servers or your local system, your product will not start.
 Table 2.Examples of valid server entries.Server Entry
 Syntax
 ExampleServer name
 server
 server1
 Server's network name
 server.domain.com
 server1.ni.com
 Server's IP address
 IP Address
 127.0.0.2
 Server name with specified port
 server[:port]
 server2:27000
 Server's network name with specified port
 server.domain.com[:port]
 server3.ni.com:28432
 "Triple redundant" server
 server, server, server
 server1, server2, server3
3. Click 
 OK.

Related tasks:

- Requesting Group Membership from a Volume License Server
- Updating Information on the Volume License Server
- Switching between Licenses on a Volume License Server

Related information:

- NI Volume License Program for Software

#### Removing Volume License Server
 Access

Use License Manager to remove a volume license server.

1. Select [IMAGE alt='image' src='GUID-4BADACB4-3362-48F1-8A3F-855B57ACF50F-a5.gif']»Manage Volume License Servers.
2. Delete the server entry that you no longer wish to access.
3. Click 
 OK.

#### Requesting Group Membership from a Volume
 License Server

Use NI License Manager to request group membership from volume license servers
 running NI Volume License Manager 3.0 or later.

Group membership allows you to access all software products available to that group.

Note

Requesting Group Membership During License Activation

1. Click Network Licenses.
2. Select the server for which you want to request group membership. 
 If there is more than one server, select the tab with the server to change.
3. Click the Manage Client link.
4. Complete the form that appears. 
 Note Fields marked with an
 asterisk are required.
 The amount of the form you have to complete depends on the situation. 
 SituationActionDifferent software user and computer owner
 Complete both sides of the formSame software user and computer owner
 Complete one side of the form and click Copy all to
 computer or Copy all to user to
 copy the information to the other half of the form
5. Select the groups you want to join.
6. Click Send Request. 
 Note You may want to record the
 Administrator Information in case you need to contact the volume license
 administrator in the future.

After the volume license server accepts
 your request, you can check out licenses for any NI software included in that group.

Parent topic:

NI License Manager Manual

Related tasks:

- Setting up Volume License Server Access
- Updating Information on the Volume License Server
- Setting up and Removing Volume License Server Access
- Switching between Licenses on a Volume License Server

#### Requesting Group Membership During License
 Activation

Request group membership from volume license servers during the license activation
 process.

Group membership allows you to access all software products available to that group.

Note

Requesting Group Membership from a Volume License
 Server.

1. Choose Connect to a volume license server from the
 drop-down
 menu while activating a license.
2. Enter the server address or host name of the server for which you want to
 request group membership.
3. Click Connect.
4. Select one or more user groups to join and click
 Next.
5. Fill out the Admin requestform as
 requested by your volume license administrator.
6. Optional: 
 If you want to enter different information for user and computer groups, uncheck Use the same
 information for computer and user groups.
7. Click Submit.

Check Status

Parent topic:

Requesting Group Membership from a Volume License Server

Related information:

- Requesting Group Membership from a Volume License Server

#### Updating Information on the Volume License Server

Use NI License Manager to update your user or computer information on volume license servers running NI Volume License Manager 3.0 and later.

1. Click Network Licenses.
2. Select the server to which you want to send updated information. 
 If there is more than one server, select the tab with the server to change.
3. Click the 
 Manage Client link.
4. Complete the form that appears.
5. Click 
 Send Request.

Parent topic:

NI License Manager Manual

Related tasks:

- Removing Volume License Server Access
- Requesting Group Membership from a Volume License Server
- Setting up and Removing Volume License Server Access
- Switching between Licenses on a Volume License Server

#### Switching between Licenses on a Volume License Server

Use License Manager to switch between software licenses.

This feature is available only for concurrent licenses hosted by a volume license server.

Note

- Concurrent license switching works on products
 shipped after August 2008, such as LabVIEW 8.6.
- Non-concurrent license switching works on
 products shipped after May 2017, such as LabVIEW NXG.

If you are using managed concurrent
 licenses, you must have permission assigned on the volume license server. Contact the
 administrator of your volume license agreement for assistance with assigning permissions.

License Manager looks for all licenses available on the volume license server.

If your volume license includes concurrent licenses for multiple types of the same product,
 you can switch between concurrent licenses to use a specific product type. For example, you
 have concurrent licenses for LabVIEW Professional and LabVIEW Full. You need only LabVIEW
 Full, disable license checkout for LabVIEW Professional to save the license for another
 user.

Use License Manager to switch licenses by disabling and enabling volume licenses.

1. Disable the use of a specific volume license 
 
 The license status changes to red to indicate the volume license is disabled.
  1. Click Network Licenses.
  2. Select the product listed under a volume license server in the tree.
  3. In the 
 Actions section, click 
 Disable, if the node selected in the tree allows it.
2. Enable the use of the specific volume license. 
 
 The license status changes from red (concurrent) or gray (non-concurrent) to
 green to indicate the volume license is enabled.
  1. Click Network Licenses.
  2. Select the product listed under a volume license server in the tree.
  3. In the Actions section, click Enable,
 if the node selected in the tree allows it.

Parent topic:

License Manager Manual

Related tasks:

- Setting up Volume License Server Access
- Requesting Group Membership from a Volume License Server
- Updating Information on the Volume License Server
- Setting up and Removing Volume License Server Access
- Requesting Group Membership from a Volume License Server
- Updating Information on the Volume License Server

#### Checking License Expiration

Check your license type and expiration date.

Note

1. Launch Volume License Manager.
2. Navigate to the Status tab.
3. Check the License File Expiration field. 
 If you have a perpetual license, the value will be Permanent rather than a
 date.
