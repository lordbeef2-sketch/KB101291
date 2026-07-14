# NI DOCUMENT BUNDLE: ni-vision-eclipse

<!--NI_BUNDLE_CHUNK bundle=ni-vision-eclipse start=1 end=9 -->
<!--NI_TOPIC bundle=ni-vision-eclipse path=configuring.html language=enus -->
## TOPIC 00001: Configuring a Remote System

- bundle_id: `ni-vision-eclipse`
- source_path: `configuring.html`
- source_url: https://docs-be.ni.com/bundle/ni-vision-eclipse/raw/resource/enus/configuring.html
- document_id: `ni-vision-eclipse`
- page_type: `leaf`
- content_type: ``

### Configuring a Remote System

Before you can run the executable you created in the previous section on your NI Linux Real-Time target, you need to add your target to the project. Complete the following steps to configure your target as a remote system in C/C++ Development Tools for NI Linux Real-Time, Eclipse Edition:

|  | Note Before proceeding with the steps in this section, ensure your target has SSH enabled. You can enable SSH on your target using Measurement & Automation Explorer (MAX) or using a DIP switch on your target (if available). |
| --- | --- |

1. Select Window»Open Perspective»Other to open the Open Perspective dialog box.
2. Select Remote System Explorer .
3. Click OK to add the Remote System Explorer perspective to the workbench.
4. Click the Define a connection to remote system button to open the New Connection wizard.
5. Select SSH Only under the General folder. 

 [IMAGE alt='image' src='note.gif']
**Note** You also can select **Linux** as the remote system type, but since connecting to NI Linux Real-Time targets requires SSH, selecting **SSH Only** shortens the number of configuration steps by pre-selecting SSH options.
6. Click Next to open the Remote SSH Only System Connection page.
7. Select a profile to contain the remote system connection from the Parent profile pull-down menu. For information about profiles, refer to the Remote System Explorer Profiles topic of the C/C++ Development Tools for NI Linux Real-Time, Eclipse Edition Help , available by selecting Help»Help Contents from the workbench view.
8. Enter the hostname or IP address of your NI Linux Real-Time target in the Host name text box. 

 [IMAGE alt='image' src='tip.gif']
**Tip** You can use MAX to identify your target's hostname and IP address.
9. (Optional) Enter a description or change the connection name in the Description and Connection name text boxes to help you identify your target when it appears in the Remote System Explorer perspective.
10. Click Finish .
11. Your target displays in the Remote Systems tab in the Remote System Explorer perspective.
12. Expand the Sftp Files folder under your target to explore the files on your target.
13. When you expand the Root folder under Sftp Files , the Enter Password dialog box appears. Enter the user name and password assigned to your target and click OK . The default user name is admin and the default password is a blank password. 

 [IMAGE alt='image' src='note.gif']
**Note** National Instruments recommends you set a password for improved security. For information on setting a password, refer to the *Logging in to your System* topic of the *Measurement & Automation Explorer Help*, available by selecting **Help»MAX Help** from MAX.
14. [IMAGE alt='image' src='note.gif']
**Note** If the connection pop-up does not include a **User ID** field, please right-click on your target under the **Remote Systems** tab and click **Properties.**You can update the **User ID** input by changing the **Default User ID** option in the **Host**category.

After configuring a remote target, you can begin [running a C/C++ executable on an NI Linux Real-Time target](running.html).

<!--NI_TOPIC bundle=ni-vision-eclipse path=creating.html language=enus -->
## TOPIC 00002: Creating a C/C++ Project

- bundle_id: `ni-vision-eclipse`
- source_path: `creating.html`
- source_url: https://docs-be.ni.com/bundle/ni-vision-eclipse/raw/resource/enus/creating.html
- document_id: `ni-vision-eclipse`
- page_type: `leaf`
- content_type: ``

### Creating a C/C++ Project

1. Switch to the C/C++ perspective.
2. Select File»New»Project to open the New Project Wizard.
3. Expand the C/C++ folder and select C Project or C++ Project depending on the programming language you wish to use.
4. Click Next to open the C Project page.
5. Enter a project name in the Project name text box.
6. Select a project type under the Executable folder in the Project type listbox.
7. Select Cross GCC in the Toolchains listbox to enable cross-compilation, which configures the compiler to create executable code for embedded systems, such as an NI Linux Real-Time target.
8. Click Next to open the Select Configurations page.
9. Enable the Debug and Release checkboxes.
10. Click Next to open the Cross GCC Command page.
11. In the Cross compiler prefix text box, enter one of the values from the following list, including the hyphen (-) at the end, to specify the correct compiler for the NI Linux Real-Time target:
  - Linux ARM-based targets 
 **(2013 software stack)** arm-none-linux-gnueabi- 
 **(2014 software stack)** arm-nilrt-linux-gnueabi-
  - Linux x64-based targets 
 **(2014 software stack)** x86_64-nilrt-linux-
12. In the Cross compiler path text box, browse to the location of the correct compiler for your target as specified in the following list: 
 Linux-Arm
  - Linux ARM-based targets 

 **(2013 software stack)** <National Instruments>\Eclipse\toolchain\gcc-4.4-arm\i386\bin 

 **(2014 software stack)** <National Instruments>\Eclipse\14.0\arm\sysroots\i686-nilrtsdk-mingw32\usr\bin\armv7a-vfp-neon-nilrt-linux-gnueabi
  - Linux x64-based targets **(2014 software stack)**<National Instruments>\Eclipse\14.0\x64\sysroots\i686-nilrtsdk-mingw32\usr\bin\x86_64-nilrt-linux
13. Click Finish to create your project and return to the workbench view.

After creating a project, you can begin [updating a C/C++ project build](updating.html).

<!--NI_TOPIC bundle=ni-vision-eclipse path=debugging.html language=enus -->
## TOPIC 00003: Debugging a C/C++ Project

- bundle_id: `ni-vision-eclipse`
- source_path: `debugging.html`
- source_url: https://docs-be.ni.com/bundle/ni-vision-eclipse/raw/resource/enus/debugging.html
- document_id: `ni-vision-eclipse`
- page_type: `leaf`
- content_type: ``

### Debugging a C/C++ Executable on an NI Linux Real-Time Target

C/C++ Development Tools for NI Linux Real-Time, Eclipse Edition offers functionality for debugging your project. Complete the following steps to debug a C/C++ project in C/C++ Development Tools for NI Linux Real-Time, Eclipse Edition:

1. Select Run»Debug Configurations to open the Debug Configurations dialog box.
2. Select the Debugger tab.
3. Click the Browse button beside the GDB debugger text box.
4. Select the correct debugger as specified in the following list:
  - Linux ARM-based targets 
 **(2013 software stack)** arm-none-linux-gnueabi-gdb.exe in the <National Instruments>\Eclipse\toolchain\gcc-4.4-arm\i386\bin directory. 
 **(2014 software stack)** arm-nilrt-linux-gnueabi-gdb.exe in the <National Instruments>\Eclipse\14.0\arm\sysroots\i686-nilrtsdk-mingw32\usr\bin\armv7a-vfp-neon-nilrt-linux-gnueabi directory.
  - Linux x64-based targets 
 **(2014 software stack)** x86_64-nilrt-linux-gdb.exe in the <National Instruments>\Eclipse\14.0\x64\sysroots\i686-nilrtsdk-mingw32\usr\bin\x86_64-nilrt-linux directory.
5. Click Open .
6. Click Apply and then Debug to start debugging the project.
7. Click Yes when C/C++ Development Tools for NI Linux Real-Time, Eclipse Edition, prompts you to switch perspectives.

<!--NI_TOPIC bundle=ni-vision-eclipse path=faqs.html language=enus -->
## TOPIC 00004: C/C++ Eclipse Edition FAQs

- bundle_id: `ni-vision-eclipse`
- source_path: `faqs.html`
- source_url: https://docs-be.ni.com/bundle/ni-vision-eclipse/raw/resource/enus/faqs.html
- document_id: `ni-vision-eclipse`
- page_type: `leaf`
- content_type: ``

### C/C++ Eclipse Edition FAQs

**Q: How do I view an image on an external display?**

The remote target must have a video out port. Refer to the display API example that ships with Vision Development Module.

**Q: How do I know what kind of processor is inside the remote target?**

Open NI-MAX. Expand **Remote Systems** and find the remote target. View the **System Settings**.

**Q: How do I handle errors?**

Use the imaqgetlasterror function to return error codes. Details about error codes are available in nivision.h.

**How do I use Eclipse to prototype an application on Windows?**

Create a project under the C/C++ Eclipse workspace with the following Microsoft Visual C++ settings.

1. Select Project»Properties»C/C++ Build»Settings»Tool Settings»Tool Settings»C Compiler(cl)»preprocessor .
2. Enter <National Instruments>\Shared\ExternalCompilerSupport\C\include to Include paths (/l) .
3. Select Project»Properties»C/C++ Build»Settings»Tool Settings»Linker(link)»Libraries .
4. Add nivision.lib to Libraries .
5. Enter a file path in Additional Libpath(/libpath) :
  - Linux ARM-based targets 
 <National Instruments>\Shared\ExternalCompilerSupport\C\lib32\msvc
  - Linux x64-based targets 
 <National Instruments>\Shared\ExternalCompilerSupport\C\lib64\msvc

<!--NI_TOPIC bundle=ni-vision-eclipse path=help_file_title.html language=enus -->
## TOPIC 00005: Getting Started with C/C++ Development Tools for NI Linux Real-Time, Eclipse Edition with the NI Vision Development Module and IMAQdx

- bundle_id: `ni-vision-eclipse`
- source_path: `help_file_title.html`
- source_url: https://docs-be.ni.com/bundle/ni-vision-eclipse/raw/resource/enus/help_file_title.html
- document_id: `ni-vision-eclipse`
- page_type: `leaf`
- content_type: ``

[IMAGE alt='image' src='ni_mainbitlogo_48.gif']

### Getting Started with C/C++ Development Tools for NI Linux Real-Time, Eclipse Edition with the NI Vision Development Module and NI-IMAQdx

July 2021, 375781E-01

This tutorial describes how to use the C/C++ Development Tools for NI Linux Real-Time, Eclipse Edition to develop an example C application using the NI Vision Development Module API and/or NI-IMAQdx, and deploy it on a Linux remote target. This tutorial outlines the basic steps required to build and deploy an example application. The settings and configurations detailed here may change for different applications.

For more information about this help file, refer to the following topics:

[Related Documentation](bp_related_documentation.html)

[Glossary](bp_glossary.html)

[NI Services](bp_technical_support_resources.html)

©2015–2021 National Instruments Corporation. All rights reserved.

Refer to the <National Instruments>\_Legal Information directory for information about NI copyright, patents, trademarks, warranties, product warnings, and export compliance.

<!--NI_TOPIC bundle=ni-vision-eclipse path=installing.html language=enus -->
## TOPIC 00006: Installing and Configuring C/C++ Development Tools for NI Linux Real-Time, Eclipse Edition

- bundle_id: `ni-vision-eclipse`
- source_path: `installing.html`
- source_url: https://docs-be.ni.com/bundle/ni-vision-eclipse/raw/resource/enus/installing.html
- document_id: `ni-vision-eclipse`
- page_type: `leaf`
- content_type: ``

### Installing and Configuring C/C++ Development Tools for NI Linux Real-Time, Eclipse Edition

The following sections guide you through installing and configuring the software for first use.

#### Installing Software

Install the following software:

1. Java (Java SE 6 or later is recommended), available for download at http://www.java.com/getjava
2. C/C++ Development Tools for NI Linux Real-Time, Eclipse Edition, available for download at ni.com. Download the Eclipse Development Tools version that corresponds to your version of LabVIEW.

#### Configuring a Workspace

Complete the following steps to configure C/C++ Development Tools for NI Linux Real-Time, Eclipse Edition, for first use:

1. Launch C/C++ Development Tools for NI Linux Real-Time, Eclipse Edition
2. When prompted, select a folder in which to store Eclipse projects and click OK .
 [IMAGE alt='Tip' src='tip.gif']
 **Tip** Enable **Use this as the default and do not ask again** to save a project folder as your default workspace.
3. In the Eclipse welcome screen, select the Workbench icon on the far right to open the workbench view.
4. C/C++ Development Tools for NI Linux Real-Time, Eclipse Edition, highlights the active perspective on the perspectives bar, as shown in the following image. The first time you use C/C++ Development Tools for NI Linux Real-Time, Eclipse Edition, the workbench view opens in the C/C++ perspective.

After configuring the workspace, you can [create a new project](creating.html) in the C/C++ perspective.

<!--NI_TOPIC bundle=ni-vision-eclipse path=running.html language=enus -->
## TOPIC 00007: Running a C/C++ Executable on an NI Linux Real-Time Target

- bundle_id: `ni-vision-eclipse`
- source_path: `running.html`
- source_url: https://docs-be.ni.com/bundle/ni-vision-eclipse/raw/resource/enus/running.html
- document_id: `ni-vision-eclipse`
- page_type: `leaf`
- content_type: ``

### Running a C/C++ Executable on an NI Linux Real-Time Target

After adding the remote target to a project, take the following steps to create a **Run Configuration** to run the executable on the remote target:

1. Select Run»Run Configurations to open the Run Configurations dialog box.
2. Select C/C++ Remote Application in the left pane.
3. Click the New launch configuration button to specify the settings of the executable on the remote target.
4. Select the target from the Connection pull-down menu.
5. Click the Browse button beside the Remote Absolute File Path for C/C++ Application text box to open the Select Remote C/C++ Application File dialog box.
6. Right-click on My Home directory in the listbox, select New»Folder to create a folder for the executable on the target.
7. Enter a name for the folder in the New folder name text box.
8. Click OK to return to the Run Configurations dialog box.
9. Append the executable name to the file path populated in the Remote Absolute File Path for C/C++ Applications text box.

 [IMAGE alt='Note' src='note.gif']
**Note** The **Remote Absolute File Path for C/C++ Applications** text box specifies the file path, including the executable name, on the target where the compiler copies the executable.
10. The program execution is displayed in the Console tab .

After running an executable on an NI Linux Real-Time target, you can begin [debugging a C/C++ project](debugging.html).

<!--NI_TOPIC bundle=ni-vision-eclipse path=updating.html language=enus -->
## TOPIC 00008: Updating a C/C++ Project Build

- bundle_id: `ni-vision-eclipse`
- source_path: `updating.html`
- source_url: https://docs-be.ni.com/bundle/ni-vision-eclipse/raw/resource/enus/updating.html
- document_id: `ni-vision-eclipse`
- page_type: `leaf`
- content_type: ``

### Updating a C/C++ Project Build

1. Highlight a project in the Project Explorer tab, then select Project»Properties from the main menu bar. You can also right click on a project and select Properties from the context popup menu.
2. Select C/C++ Build in the Properties dialog box tree, and select Internal builder from the Builder type pull-down menu.
 
 Selecting the internal builder uses C/C++ Development Tools for NI Linux Real-Time, Eclipse Edition, instead of an external build file, to build the executable.
3. Expand C/C++ Build in the Properties tree and select Settings .
  - To set the configurations, select All Configurations from the Configuration drop-down menu.
  - Select the Tool Settings tab to set the compiler, linker, and assembler options.
4. Expand Cross GCC C Compiler in the Tool Settings tree. Select Includes and click to add the following:
  - Set Include Paths (-l) 

 <National Instruments>\Shared\ExternalCompilerSupport\C\include
  - Set Include Files (-include)
    - nivision.h
    - NIIMAQdx.h
5. (Optional) Complete the following steps to improve the performance of floating-point operations:
  1. Expand Cross GCC Compiler in the Tool Settings tree and select Miscellaneous .
  2. If your system is ARM, select the Other flags text box, add a space after the existing text, then enter -mfpu=vfpv3 -mfloat-abi=softfp [IMAGE alt='Note' src='note.gif']
**Note** x64 targets do not recognize this flag.
6. Expand Cross GCC Linker or Cross G++ Linker in the Tool Settings tree and select Libraries .
 [IMAGE alt='Note' src='note.gif']
**Note** **Cross GCC Linker** appears if you are working in a C project, whereas **Cross GCC++ Linker** appears if you are working in a C++ project.
7. In the Libraries (-l) pane, click the Add... icon and add the following libraries:
 
 nivision , nivissvc , niimaqdx
8. In the Library Search Path (-L) pane, click the Add... icon and add a library path appropriate for the operating system:
  - Linux Arm7 32-bit
 <National Instruments>\Shared\ExternalCompilerSupport\C\arm\gcc
9. Expand Cross GCC Linker or Cross GCC++ Linker in the Tool Settings tree and select Miscellaneous . In the Linker flags textbox, enter -Wl, --unresolved-symbols=ignore-in-shared-libs
10. Click Apply and then OK to close the Properties dialog box.
11. Select Project»Build Project in the workbench to create an executable of your project.
12. The Console tab displays Build Finished if the build completes successfully.

After updating the C/C++ build configuration, you can begin [writing a client program](writing.html).

<!--NI_TOPIC bundle=ni-vision-eclipse path=writing.html language=enus -->
## TOPIC 00009: Writing a Client Program

- bundle_id: `ni-vision-eclipse`
- source_path: `writing.html`
- source_url: https://docs-be.ni.com/bundle/ni-vision-eclipse/raw/resource/enus/writing.html
- document_id: `ni-vision-eclipse`
- page_type: `leaf`
- content_type: ``

### Writing a Client Program

When you install Vision Development module, the nivision.h, NIIMAQdx.h, and nivisionutility.h headers become available. Any client program that invokes APIs from Vision Development Module requires the nivision.h header. Any client program that invokes APIs from Vision Acquisition Software requires the NIIMAQdx.h header.

The nivision.h header includes the following:

- CVI function declaration (Import functions)
- Forward structure declaration
- Structure definition
- Enumeration definition
- Intrinsic data type declaration
- Error codes

Build the project and transfer any executable and dependent images to the RT target.

#### Importing Existing Projects

You can use the Import Wizard to import an existing project into the workspace.

1. From the main menu bar, select File»Import... to open the Import Wizard.
2. Select General»Existing Projects into Workspace and click Next .
3. Choose either Select root directory or Select archive file and click Browse .
4. Under Projects , select the project or projects to import.
5. Click Finish to start the import.

#### Example Client Programs

Example client programs can be found at the following locations:

- Vision Development Module— <National Instruments>\Vision\Examples\Eclipse\Battery Clamp Inspection
- Vision Acquisition Software— C:\Users\Public\Documents\National Instruments\NI-IMAQdx\Examples\Eclipse\Image Acquisition

After writing a client program, you can begin [configuring a remote system](configuring.html).
