# NI DOCUMENT BUNDLE: fpga-interface-c

<!--NI_BUNDLE_CHUNK bundle=fpga-interface-c start=1 end=15 -->
<!--NI_TOPIC bundle=fpga-interface-c path=building-a-c-c-application.html language=enus -->
## TOPIC 00001: Building a C/C++ Application

- bundle_id: `fpga-interface-c`
- source_path: `building-a-c-c-application.html`
- source_url: https://docs-be.ni.com/bundle/fpga-interface-c/raw/resource/enus/building-a-c-c-application.html
- document_id: `fpga-interface-c`
- page_type: `leaf`
- content_type: `concept`
- source_description: Creating a ProjectUse your development tools to create a project or a makefile that includes the two header files and the source file. Add a new source file to the project or makefile. In the new source file, use #include to include the generated .h header file. The generated .h header file uses #in

### Building a C/C++ Application

#### Creating a Project

Use your development tools to create a project or a
 makefile that includes the two header files and the source file. Add a new source
 file to the project or makefile. In the new source file, use
 #include to include the generated .h
 header file. The generated .h header file uses
 #include to include NiFpga.h.

The
 Examples directory contains examples of project files and
 makefiles for different operating systems.

| Operating System | Compile Tools Package |
| --- | --- |
| NI Linux Real-Time (Intel x64-based) | GNU C and C++ Compile Tools x64 |
| NI Linux Real-Time (ARM-based) | GNU C and C++ Compile Tools for ARMv7 |

ni.com/info

NILRTCrossCompile

If you are developing
 an application for an R Series device, refer to the NI tutorial *Building an R
 Series FPGA Interface Host Application in C*.

#### Writing C/C++ Code Using FPGA Interface C API Functions

All C/C++
 applications must call the required functions. In order to interact with
 FPGA VIs, your application must call a
 session function to open an FPGA session. From there, call
 other functions in NiFpga.h to read and write to controls and
 indicators, use interrupts, or use other C/C++ functions.

Refer to the
 installed examples to see how to use C API functions.

#### Developing and Maintaining the C/C++ Application

The constants in the
 generated header file are tied to the specific bitfile used to generate them. If you
 modify the FPGA VI, you must recompile the VI, regenerate the C API, and rebuild any
 C/C++ application that used the original C API. This is because the register offsets
 for controls and indicators may have changed unexpectedly. If you do not regenerate
 and rebuild, and instead try to use a new bitfile with an older application, you get
 the NiFpga_Status_SignatureMismatch error message. The signature of
 the bitfile does not match the signature passed to the NiFpga_Open
 function.

FPGA

FPGA

Tip

.dll

.out

.so

.exe

.dll

.out

.lvbitx

Related concepts:

- Generated Files
- Examples
- Naming Conventions for Generated Files and Constants

Related information:

- Getting Started with C/C++ Development for
 NI Linux Real-Time
- GNU C and C++ Compile Tools x64
- GNU C and C++ Compile Tools for
 ARMv7

<!--NI_TOPIC bundle=fpga-interface-c path=deploying-and-running-applications.html language=enus -->
## TOPIC 00002: Deploying and Running Applications

- bundle_id: `fpga-interface-c`
- source_path: `deploying-and-running-applications.html`
- source_url: https://docs-be.ni.com/bundle/fpga-interface-c/raw/resource/enus/deploying-and-running-applications.html
- document_id: `fpga-interface-c`
- page_type: `leaf`
- content_type: `concept`
- source_description: Windows and LinuxIn Windows and Linux, you can run a C/C++ application from within your development environment. If the original bitfile was built for a remote RIO target, your C/C++ application can interact with FPGA VIs that run on a remote RIO target. To run a C/C++ application on a remote target

### Deploying and Running Applications

#### Windows and Linux

In Windows and Linux, you can run a C/C++ application
 from within your development environment. If the original bitfile was built for a
 remote RIO target, your C/C++ application can interact with FPGA
 VIs that run on a remote RIO target. To run a C/C++ application on a remote target,
 change the resource passed into NiFpga_Open from a local resource,
 such as RIO0, to a remote resource, such as
 rio://<hostnameOrIpAddress>/RIO0.
 You can substitute a valid RIO alias for the resource name.

#### VxWorks

If you are developing for a VxWorks system, you can use the
 serial console for debugging. FTP the built binary
 (MyApplication.out) and the .lvbitx
 file to the root directory of the target. Using the serial console, type the
 ld command as shown in the following example to load the
 library:

ld < MyApplication.out

After loading the
 library, you can call any function in the library from the serial
 console.

When your application is complete and debugged, you can set up the
 system to run it on startup. Modify ni-rt.ini by appending to
 StartupDLLs under the [LVRT]
 section.

For example, when you change
 "StartupDLLs=<DLLs>;" to
 "StartupDLLs=<DLLs>;/c/MyApplication.out;",
 your application runs every time the system starts up.

#### Phar
 Lap ETS

If you are using LabWindows/CVI to develop an application for a Phar Lap ETS
 real-time target, the mnaufacturer recommends that you use the LabWindows/CVI
 Real-Time Module. Select Run»Select Execution Target for Debugging»New Execution
 Target to specify your target system. Then select Run»Manage Files on Real-Time Execution Target to add the .lvbitx file. You can then run
 the application by selecting Run»Debug Project. Refer to the *LabWindows/CVI User Manual* at
 *ni.com/docs* for more information about running and deploying
 applications.

If you are using Microsoft Visual C++ to develop an application for a Phar Lap
 ETS real-time target, you must set up the system to run your application on
 startup. FTP the built binary (MyApplication.dll) and the
 .lvbitx file to the root directory of the target. Then
 modify ni-rt.ini by appending to
 StartupDLLs under the [LVRT] section.

For example, when you change
 "StartupDLLs=<DLLs>;" to
 "StartupDLLs=<DLLs>;C:\MyApplication.dll;",
 your application runs every time the system starts up.

#### NI
 Linux Real-Time

For information about developing C/C++ applications for NI
 Linux Real-Time targets, go to *ni.com/info* and enter the info code
 *EclipseIDE*.

#### Specifying the Location of the .lvbitx File

Because different operating
 systems have different default current working directories for applications, you
 must pass an absolute path for the bitfile parameter of the
 NiFpga_Open function. If you pass only the filename instead of
 an absolute path, the operating system cannot locate the bitfile.

<!--NI_TOPIC bundle=fpga-interface-c path=examples.html language=enus -->
## TOPIC 00003: Examples

- bundle_id: `fpga-interface-c`
- source_path: `examples.html`
- source_url: https://docs-be.ni.com/bundle/fpga-interface-c/raw/resource/enus/examples.html
- document_id: `fpga-interface-c`
- page_type: `leaf`
- content_type: `concept`
- source_description: The Examples directory is installed in C:\Users\Public\Documents\National Instruments\FPGA Interface C API\Examples\ and contains the following subdirectories: Platforms Arrays FIFOs IRQs Additionally, if LabWindows/CVI support is selected during installation, the FPGA Interface C API installer inst

### Examples

The Examples directory is installed in
 C:\Users\Public\Documents\National Instruments\FPGA Interface C
 API\Examples\ and contains the following subdirectories:

- Platforms
- Arrays
- FIFOs
- IRQs

Additionally, if LabWindows/CVI support is selected during installation, the FPGA
 Interface C API installer installs examples in
 C:\Users\Public\Documents\National Instruments\CVI\samples\FPGA Interface
 C API\.

The manufacturer recommends that you make a copy of any example files before modifying them. If
 you inadvertently modify installed files and want to revert changes, delete the modified
 files. Then use Add or Remove Programs to repair the FPGA
 Interface C API software installation.

#### The
 Platforms Subdirectory

The Platforms subdirectory
 contains LabVIEW source code and versions of a C/C++ application created for certain
 supported operating systems and compilers. Each subdirectory under
 Platforms contains example source code and project files
 specific to the minimum compatible version of the given compiler. For example, the
 files in \Examples\Platforms\Windows\CVI\9.0\ work with
 LabWindows/CVI 9.0 or later.

The C/C++ application is written in
 Example.cpp or Example.c, depending on
 the compiler. The application tests the temperature of the FPGA device, then waits
 while toggling either the FPGA LED (on a CompactRIO device) or Connector0/DO0 (on an
 R Series device).

Complete the following steps to prepare an example for
 use:

1. Launch Example.lvproj .
2. In the LabVIEW Project Explorer window, add your FPGA
 target to the project.
3. If the Select Programming Mode dialog box appears, select
 LabVIEW FPGA Interface and click
 Continue .
4. The example project is populated with RIO devices containing FPGA targets.
 Expand one of the FPGA targets to find the example FPGA VI that works with your
 target. Note If you
 are using an R Series device, expand the PCI or PXI FPGA target. If you are
 using CompactRIO or Single-Board RIO, expand the CompactRIO FPGA target. The
 FPGA VI may require some modification to work with
 your target.
5. Drag the example FPGA VI to your FPGA target.
6. Open the FPGA VI to check for errors. You can resolve most
 errors by adding new FPGA I/O items to your project. In the LabVIEW
 Project Explorer window, right-click the FPGA target item and
 select New»FPGA I/O . On the New FPGA I/O dialog box that
 appears, select all available I/O resources, then click
 OK . Note The example application does
 not work without modification on NI 781x devices. The application reads the
 board temperature, and NI 781x devices do not support temperature reading.
 To use the example on these devices, you must remove the temperature-reading
 code.
7. Right-click the FPGA VI and select Create Build
 Specification from the shortcut menu. Under Build
 Specifications , right-click the new build specification for the
 example FPGA VI, select Build , and
 wait for the build to complete. Note For versions of LabVIEW
 earlier than 2010, right-click the example FPGA VI,
 select Compile, and wait for the compilation to
 complete.
8. Right-click the example FPGA VI and select Launch
 C API Generator .
9. In the FPGA Interface C API Generator dialog box that
 appears, change the Output Directory to the appropriate
 subdirectory. You can find the subdirectory that is appropriate for your
 operating system and compiler under Platforms .
10. Click Generate to generate the C API.
11. In the output directory that you selected in Step 9 above, find the associated
 project file and open it.
  - For LabWindows/CVI, the project file is a .cws 
 file.
  - For Microsoft Visual C++, the project file is a
 .sln file.
  - For Linux Real-Time and Wind River Workbench, you must import the entire
 directory using File»Import»Existing Project into Workspace .
  - For Linux, you must transfer the entire directory to your Linux
 development computer.

Note

Fixing Build Problems in NI Linux Real-Time
 Applications

#### The Arrays, FIFOs, and IRQs
 Subdirectories

The Arrays,
 FIFOs, and IRQs subdirectories contain
 example source code and generated header files. They provide examples of how to
 write code using the Array, FIFO, and
 IRQ functions, but they are not ready to run.

Related concepts:

- Using the FPGA Interface C API with LabWindows/CVI
- Generating a C API for a LabVIEW FPGA Application

Related information:

- Fixing Build Problems in NI Linux Real-Time Applications

<!--NI_TOPIC bundle=fpga-interface-c path=generated-files.html language=enus -->
## TOPIC 00004: Generated Files

- bundle_id: `fpga-interface-c`
- source_path: `generated-files.html`
- source_url: https://docs-be.ni.com/bundle/fpga-interface-c/raw/resource/enus/generated-files.html
- document_id: `fpga-interface-c`
- page_type: `leaf`
- content_type: `concept`
- source_description: The generated FPGA Interface C API consists of the following files: a .h file a .lvbitx file NiFpga.h NiFpga.c Generated .h FileThe .h file is a C header file that contains all the constants required by function calls in your application. For example, NiFpga_Open requires the name of the .lvbitx fil

### Generated Files

The generated FPGA Interface C API consists of the following files:

- a .h file
- a .lvbitx file
- NiFpga.h
- NiFpga.c

#### Generated .h File

The .h file is a C header file
 that contains all the constants required by function calls in your application. For
 example, NiFpga_Open requires the name of the
 .lvbitx file, provided by the generated
 *_Bitfile constant. A digital signature of the FPGA
 bitstream in the bitfile, provided by the generated *_Signature
 constant.

The other constants represent register offsets of:

- Each control
- Indicator
- FIFO in your VI
- Other necessary information

#### Generated .lvbitx Bitfile

This is a
 version of the original .lvbitx bitfile, renamed to match the
 prefix of the constants in the .h header file.
 NiFpga_Open must find this file in order to ensure the
 bitstream is downloaded to the FPGA.

#### NiFpga.h File

This is a C header file. It
 is identical for all generated C APIs. It declares all the errors, types, constants,
 and functions needed to write an application. Most of these functions are defined in
 NiFpga.c.

#### NiFpga.c File

NiFpga.c

NiFpga

Note

NiFpga.h

NiFpga.c

Related concepts:

- Naming Conventions for Generated Files and Constants
- Using the FPGA Interface C API with LabWindows/CVI
- Generating a C API for a LabVIEW FPGA Application

<!--NI_TOPIC bundle=fpga-interface-c path=generating-a-c-api-for-a-labview-fpga-applica.html language=enus -->
## TOPIC 00005: Generating a C API for a LabVIEW FPGA Application

- bundle_id: `fpga-interface-c`
- source_path: `generating-a-c-api-for-a-labview-fpga-applica.html`
- source_url: https://docs-be.ni.com/bundle/fpga-interface-c/raw/resource/enus/generating-a-c-api-for-a-labview-fpga-applica.html
- document_id: `fpga-interface-c`
- page_type: `leaf`
- content_type: `concept`
- source_description: You can generate a C API for a LabVIEW FPGA application from: The LabVIEW Project Explorer window The Windows Start menu Windows command line The generated C API consists of the files needed to build and run a C/C++ application.The FPGA Interface C API Generator works only on .lvbitx files created w

### Generating a C API for a LabVIEW FPGA Application

- The LabVIEW Project Explorer window
- The Windows Start menu
- Windows command line

The generated C API consists of the files needed to build and run a C/C++
 application.

The FPGA Interface C API Generator works only on .lvbitx
 files created with LabVIEW 2009 or later. It does not work on
 .lvbit files created with older versions of LabVIEW, or on
 .lvbitx files created with the pioneer NI Labs version of the
 FPGA Interface C API.

- [Generating a C API from the LabVIEW Project Explorer Window](generating-a-c-api-from-the-labview-project-explorer-window.html)
- [Generating a C API from LabWindows/CVI 2010 or Later](generating-a-c-api-from-labwindows-cvi-%202010-or-later.html)
- [Generating a C API from the Windows Start Menu](generating-a-c-api-from-the-windows-start-menu.html)
- [Generating a C API from a Windows Command Line](generating-a-c-api-from-a-windows-command-line.html)

Related concepts:

- Generated Files
- Naming Conventions for Generated Files and Constants
- Using the FPGA Interface C API with LabWindows/CVI

<!--NI_TOPIC bundle=fpga-interface-c path=generating-a-c-api-from-a-windows-command-line.html language=enus -->
## TOPIC 00006: Generating a C API from a Windows Command Line

- bundle_id: `fpga-interface-c`
- source_path: `generating-a-c-api-from-a-windows-command-line.html`
- source_url: https://docs-be.ni.com/bundle/fpga-interface-c/raw/resource/enus/generating-a-c-api-from-a-windows-command-line.html
- document_id: `fpga-interface-c`
- page_type: `leaf`
- content_type: `concept`
- source_description: Use the following syntax to generate a C API for a compiled bitfile from a Windows command line: capigen.exe "<absolute path to .lvbitx file>" ["<absolute path to output directory>" [<prefix override>]]. Note that the second and third arguments, the path to output directory and prefix override, are

### Generating a C API from a Windows Command
 Line

Use the following syntax to generate a C API for a compiled bitfile from a Windows
 command line:

capigen.exe "<absolute path to .lvbitx
 file>" ["<absolute path to output directory>"
 [<prefix override>]].

Note

If you are using LabWindows/CVI to develop your C application, use the following syntax
 to exclude NiFpga.h and NiFpga.c. The FPGA
 Interface C API installs header and library files with LabWindows/CVI support:

capigen.exe -e "<absolute path to .lvbitx
 file>" ["<absolute path to output directory>"
 [<prefix override>]].

Parent topic:

Generating a C API for a LabVIEW FPGA Application

<!--NI_TOPIC bundle=fpga-interface-c path=generating-a-c-api-from-labwindows-cvi- 2010-or-later.html language=enus -->
## TOPIC 00007: Generating a C API from LabWindows/CVI 2010 or Later

- bundle_id: `fpga-interface-c`
- source_path: `generating-a-c-api-from-labwindows-cvi- 2010-or-later.html`
- source_url: https://docs-be.ni.com/bundle/fpga-interface-c/raw/resource/enus/generating-a-c-api-from-labwindows-cvi-%202010-or-later.html
- document_id: `fpga-interface-c`
- page_type: `leaf`
- content_type: `concept`
- source_description: Complete the following steps to generate a C API for a compiled bitfile from LabWindows/CVI 2010 or later: Select Tools»Launch FPGA Interface C API Generator. On the FPGA Interface C API Generator dialog box that appears, browse to the compiled FPGA bitfile or type an absolute path to it. Select an

### Generating a C API from LabWindows/CVI 2010 or
 Later

Complete the following steps to generate a C API for a compiled bitfile from
 LabWindows/CVI 2010 or later:

1. Select Tools»Launch FPGA Interface C API Generator .
2. On the FPGA Interface C API Generator dialog box that
 appears, browse to the compiled FPGA bitfile or type an absolute path to it.
3. Select an output directory for the C API. If you do not select an output directory,
 the C API files will be created in the directory that contains the bitfile. You can
 browse to a directory or type an absolute path to it.
4. Optionally, you can change the prefix for the generated files. Also, you can change
 the prefix for the constants in the generated .h file. Note that
 Exclude NiFpga.h/NiFpga.c is checked because the FPGA
 Interface C API installs header and library files with LabWindows/CVI support.

Parent topic:

Generating a C API for a LabVIEW FPGA Application

<!--NI_TOPIC bundle=fpga-interface-c path=generating-a-c-api-from-the-labview-project-explorer-window.html language=enus -->
## TOPIC 00008: Generating a C API from the LabVIEW Project Explorer Window

- bundle_id: `fpga-interface-c`
- source_path: `generating-a-c-api-from-the-labview-project-explorer-window.html`
- source_url: https://docs-be.ni.com/bundle/fpga-interface-c/raw/resource/enus/generating-a-c-api-from-the-labview-project-explorer-window.html
- document_id: `fpga-interface-c`
- page_type: `leaf`
- content_type: `concept`
- source_description: Complete the following steps to generate a C API for a compiled bitfile from the LabVIEW Project Explorer window: Right-click the FPGA VI and select Create Build Specification from the shortcut menu. Under Build Specifications, right-click the new build specification for the example FPGA VI, select

### Generating a C API from the LabVIEW
 Project Explorer Window

Complete the following steps to generate a C API for a compiled bitfile from the
 LabVIEW Project Explorer window:

1. Right-click the FPGA VI and select Create Build
 Specification from the shortcut menu.
2. Under Build Specifications , right-click the new build
 specification for the example FPGA VI, select
 Build , and wait for the build to complete. Note For versions of
 LabVIEW earlier than 2010, right-click the example FPGA VI.
 Then select Compile, and wait for the compilation to
 complete.
3. Right-click the compiled FPGA VI item and select
 Launch C API Generator from the shortcut menu.
4. On the FPGA Interface C API Generator dialog box that
 appears, ensure that the right compiled FPGA bitfile is selected. You can navigate
 to the right bitfile or type an absolute path to it.
5. Select an output directory for the C API. If you do not select an output directory,
 the C API files will be created in the directory that contains the bitfile. You can
 browse to a directory or type an absolute path to it.
6. Optionally, you can change the prefix for the generated files and for the constants
 in the generated .h file.
7. If you are using LabWindows/CVI to develop your C application, place a check beside
 Exclude NiFpga.h/NiFpga.c . The FPGA Interface C API
 installs header and library files with LabWindows/CVI support.

Parent topic:

Generating a C API for a LabVIEW FPGA Application

<!--NI_TOPIC bundle=fpga-interface-c path=generating-a-c-api-from-the-windows-start-menu.html language=enus -->
## TOPIC 00009: Generating a C API from the Windows Start Menu

- bundle_id: `fpga-interface-c`
- source_path: `generating-a-c-api-from-the-windows-start-menu.html`
- source_url: https://docs-be.ni.com/bundle/fpga-interface-c/raw/resource/enus/generating-a-c-api-from-the-windows-start-menu.html
- document_id: `fpga-interface-c`
- page_type: `leaf`
- content_type: `concept`
- source_description: Complete the following steps to generate a C API for a compiled bitfile from the Windows Start menu: Select Start»All Programs»National Instruments»FPGA Interface C API»FPGA Interface C API Generator . On the FPGA Interface C API Generator dialog box that appears, browse to the compiled FPGA bitfile

### Generating a C API from the Windows Start
 Menu

Complete the following steps to generate a C API for a compiled bitfile from the
 Windows Start menu:

1. Select Start»All Programs»National Instruments»FPGA Interface C API»FPGA
 Interface C API Generator .
2. On the FPGA Interface C API Generator dialog box that
 appears, browse to the compiled FPGA bitfile or type an absolute path to it.
3. Select an output directory for the C API. If you do not select an output directory,
 the C API files will be created in the directory that contains the bitfile. You can
 browse to a directory or type an absolute path to it.
4. Optionally, you can change the prefix for the generated files and for the constants
 in the generated .h file.
5. If you are using LabWindows/CVI to develop your C application, place a check beside
 Exclude NiFpga.h/NiFpga.c because the FPGA Interface C
 API installs header and library files with LabWindows/CVI support.

Parent topic:

Generating a C API for a LabVIEW FPGA Application

<!--NI_TOPIC bundle=fpga-interface-c path=naming-conventions-for-generated-files-and-co.html language=enus -->
## TOPIC 00010: Naming Conventions for Generated Files and Constants

- bundle_id: `fpga-interface-c`
- source_path: `naming-conventions-for-generated-files-and-co.html`
- source_url: https://docs-be.ni.com/bundle/fpga-interface-c/raw/resource/enus/naming-conventions-for-generated-files-and-co.html
- document_id: `fpga-interface-c`
- page_type: `leaf`
- content_type: `concept`
- source_description: Unless you specify a custom prefix, the FPGA Interface C API Generator names the generated .h file, the .lvbitx file, and the constants in the .h file based on the name of the FPGA VI from which the application bitfile was compiled. Characters Permitted in File and Constant NamesThe FPGA Interface C

### Naming Conventions for Generated Files and Constants

Unless you specify a custom prefix, the FPGA Interface C API Generator names the generated
 .h file, the .lvbitx file, and the
 constants in the .h file based on the name of the FPGA VI from which
 the application bitfile was compiled.

#### Characters Permitted in File and Constant Names

FPGA
 Interface C API Generator

FPGA

FPGA Interface C API Generator

- Single-byte alphanumeric characters and underscores in the names of
 FPGA VIs
- Labels of controls and indicators
- Names of FIFOs

FPGA Interface C API
 Generator

FPGA

Note

#### Naming of Files and Constants

For example, if the original bitfile was
 compiled from an FPGA VI called My
 Temperature-Monitoring Application.vi, the generated
 .lvbitx the default name of the generated .lvbitx file is
 NiFpga_MyTemperatureMonitoringApplication.lvbitx.

The
 FPGA Interface C API Generator uses the following parameters
 to create the names of each constant in the .h file:

- VI name or custom prefix
- The data type
- Label or name of each control, indicator
- FIFO in the FPGA VI

Before using the label or name in the name of the constant, the FPGA
 Interface C API Generator removes all characters except alphanumeric
 characters and the underscores from:

- The label of the control or indicator
- Name of the FIFO

The following example is the name of a constant corresponding to a Boolean
 indicator called Max Temp Exceeded in the FPGA
 VI described
 above:

NiFpga_MyTemperatureMonitoringApplication_IndicatorBool_MaxTempExceeded

<!--NI_TOPIC bundle=fpga-interface-c path=overview.html language=enus -->
## TOPIC 00011: FPGA Interface C API Overview

- bundle_id: `fpga-interface-c`
- source_path: `overview.html`
- source_url: https://docs-be.ni.com/bundle/fpga-interface-c/raw/resource/enus/overview.html
- document_id: `fpga-interface-c`
- page_type: `leaf`
- content_type: `concept`
- source_description: The FPGA Interface C API is add-on software for the NI-CompactRIO and R Series drivers. It enables communication between the processor and the user-programmable FPGA within NI reconfigurable I/O (RIO) hardware such as: CompactRIO modules CompactRIO Single-Board Controllers FlexRIO devices Multifunct

### FPGA Interface C API
 Overview

The FPGA Interface C API is add-on software for the NI-CompactRIO and R Series drivers.
 It enables communication between the processor and the user-programmable FPGA within NI
 reconfigurable I/O (RIO) hardware such as:

- CompactRIO modules
- CompactRIO Single-Board Controllers
- FlexRIO devices
- Multifunction reconfigurable I/O devices
- MXI-Express RIO accessories for embedded control and acquisition applications

The FPGA Interface C API helps you use LabVIEW to program the NI hardware FPGA and choose
 LabVIEW or C/C++ tools to program the system processor.

<!--NI_TOPIC bundle=fpga-interface-c path=user-manual-welcome.html language=enus -->
## TOPIC 00012: FPGA Interface C API User Manual

- bundle_id: `fpga-interface-c`
- source_path: `user-manual-welcome.html`
- source_url: https://docs-be.ni.com/bundle/fpga-interface-c/raw/resource/enus/user-manual-welcome.html
- document_id: `fpga-interface-c`
- page_type: `leaf`
- content_type: `concept`
- source_description: The FPGA Interface C API User Manual provides detailed descriptions of the product functionality and the step by step processes for use. Looking for Something Else?For information not found in the User Manual for your product, such as specifications and API reference, browse Related Information.

### FPGA Interface C API
 User Manual

The FPGA Interface C API User Manual provides detailed
 descriptions of the product functionality and the step by step processes for use.

#### Looking for Something Else?

For information not found in the User Manual
 for your product, such as specifications and API reference, browse *Related
 Information*.

Related information:

- NI CompactRIO User Manual
- Hardware and Software Operating System
 Compatibility
- License Setup and Activation

<!--NI_TOPIC bundle=fpga-interface-c path=using-the-fpga-interface-c-api-with-labwindow.html language=enus -->
## TOPIC 00013: Using the FPGA Interface C API with LabWindows/CVI

- bundle_id: `fpga-interface-c`
- source_path: `using-the-fpga-interface-c-api-with-labwindow.html`
- source_url: https://docs-be.ni.com/bundle/fpga-interface-c/raw/resource/enus/using-the-fpga-interface-c-api-with-labwindow.html
- document_id: `fpga-interface-c`
- page_type: `leaf`
- content_type: `concept`
- source_description: You can generate a C API for a LabVIEW FPGA application and develop your C application using LabWindows/CVI 9.0 or later.The FPGA Interface C API installer installs the following items if you select LabWindows/CVI support during installation: FPGA Interface C API Library and header file for LabWindo

### Using the FPGA Interface C API with LabWindows/CVI

You can generate a C API for a LabVIEW FPGA application and develop your C application using
 LabWindows/CVI 9.0 or later.

The FPGA Interface C API installer installs the following items if you select LabWindows/CVI
 support during installation:

- FPGA Interface C API Library and header file for LabWindows/CVI. This library supports LabWindows/CVI development and debugging features like user protection and resource tracking.
- LabWindows/CVI function panels for the FPGA Interface C API Library. These function panels are customized to help you select appropriate parameter values in calls to the library functions. This customization is also available in the Show Prototypes feature of the LabWindows/CVI source editor.
- LabWindows/CVI examples.

With LabWindows/CVI 2010 or later, you can launch the FPGA Interface C API
 Generator from LabWindows/CVI. With LabWindows/CVI 9.0 or later, you can
 launch the FPGA Interface C API Generator from the LabVIEW
 Project Explorer window, from the Windows Start
 menu, or from a Windows command line.

If you are using only LabWindows/CVI to develop your C application, you can exclude
 NiFpga.h and NiFpga.c from the files that
 you generate using the FPGA Interface C API Generator. The header and
 library files installed with LabWindows/CVI support make NiFpga.h
 and NiFpga.c unnecessary.

Related concepts:

- Examples
- Generating a C API for a LabVIEW FPGA Application

<!--NI_TOPIC bundle=fpga-interface-c path=what-you-can-do-with-the-fpga-interface-c-api.html language=enus -->
## TOPIC 00014: What You Can Do with the FPGA Interface C API

- bundle_id: `fpga-interface-c`
- source_path: `what-you-can-do-with-the-fpga-interface-c-api.html`
- source_url: https://docs-be.ni.com/bundle/fpga-interface-c/raw/resource/enus/what-you-can-do-with-the-fpga-interface-c-api.html
- document_id: `fpga-interface-c`
- page_type: `leaf`
- content_type: `concept`
- source_description: The FPGA Interface C API enables C/C++ applications to interact directly with compiled LabVIEW FPGA VIs on RIO devices without using LabVIEW. C/C++ applications can download: A VI to a RIO target Perform DMA data transfers Wait on and acknowledge interrupts Read from and write to named controls and

### What You Can Do with the FPGA Interface C API

The FPGA Interface C API enables C/C++ applications to interact directly with compiled LabVIEW
 FPGA VIs on RIO devices without using LabVIEW. C/C++ applications can download:

- A VI to a RIO target
- Perform DMA data transfers
- Wait on and acknowledge interrupts
- Read from and write to named controls and indicators using C function calls

A C/C++ application created with the C API can run on the real-time processor of a CompactRIO or
 single-board RIO device. It can also interact with VIs running on the FPGA of the RIO
 system. Alternatively, a C/C++ application can run on the real-time processor of a PXI
 system or the processor of a Windows or Linux PC. It can also interact with VIs running
 on the FPGA of a PXI or PCI RIO device.

#### What You Cannot Do with the C API

The
 current version of the C API does not support the following features:

- Scan Interface mode and I/O variables
- Reading from and writing to controls, indicators, and FIFOs containing the
 following:
  - Fixed-point types
  - Floating-point types
  - Clusters
  - Arrays containing anything other than supported scalar types
- The following methods callable from an Invoke Method node:
  - Read TEDS
  - NI 9802 methods:
    - Mount SD Card
    - Unmount SD Card
  - FlexRIO Adapter Module methods:
    - Control IO Module Power
    - IO Module Status
    - Redetect IO Module

<!--NI_TOPIC bundle=fpga-interface-c path=what-you-need-to-get-started.html language=enus -->
## TOPIC 00015: What You Need to Get Started

- bundle_id: `fpga-interface-c`
- source_path: `what-you-need-to-get-started.html`
- source_url: https://docs-be.ni.com/bundle/fpga-interface-c/raw/resource/enus/what-you-need-to-get-started.html
- document_id: `fpga-interface-c`
- page_type: `leaf`
- content_type: `concept`
- source_description: In addition to a RIO device such as a CompactRIO reconfigurable chassis, a single-board RIO device, or a PXI or PCI RIO device, you need the following software to use the FPGA Interface C API: LabVIEW 2012 SP1 or later (32-bit only) LabVIEW FPGA Module 2012 SP1 or later (32-bit only) 2015 or later v

### What You Need to Get Started

In addition to a RIO device such as a CompactRIO reconfigurable chassis, a single-board RIO
 device, or a PXI or PCI RIO device, you need the following software to use the FPGA Interface
 C API:

- LabVIEW 2012 SP1 or later (32-bit only)
- LabVIEW FPGA Module 2012 SP1 or later (32-bit only)
- 2015 or later version of the driver software for your device
- Supported development operating system:
 Operating System
64-bit
32-bitWindows 10
✓
✓Windows 8.1
✓
✓Windows 7 Professional SP1
✓
✓Windows Server 2012 R2
✓
—Windows Server 2008 R2 SP1
✓
—

#### Supported Target Operating
 Systems

When you have generated the C API from LabVIEW FPGA in a supported Windows
 operating system, you can create a C application that calls into the C API. Although you can
 use a variety of development environments (such as LabWindows/CVI), both your C application
 and the CompactRIO Device Drivers software must run on the target operating system and CPU
 architecture.

The C application and the CompactRIO device drivers software runs on the
 following operating systems and CPU architectures:

| CPU Architecture | Operating System | Versions or Distributions | Hardware Targets |
| --- | --- | --- | --- |
| x86, x86_64 | Windows | Any version supported for development | PC, PXI |
| x86, x86_64 | Linux | Red Hat Enterprise Linux 6.x, Scientific Linux 6.x, openSUSE 13.1 or 12.x | PC, PXI |
| x86_64, ARM | LabVIEW Real-Time | NI Linux Real-Time | NI CompactRIO |
| x86 | LabVIEW Real-Time | Phar Lap ETS | PC, PXI |
| PowerPC | LabVIEW Real-Time | VxWorks | CompactRIO, single-board RIO |

#### Supported C/C++ Compilers

The C/C++ compiler you can use to compile your
 application depends on the operating system the application runs on. The manufacturer has
 tested the following combinations of target platforms and C/C++ compilers:

| Target Platform | Tested and Supported C/C++ Compiler(s) |
| --- | --- |
| Windows | LabWindows/CVI 9.0 or later; Microsoft Visual C++ 2003 or later. |
| NI Linux Real-Time (Intel x64-based) | GNU C and C++ Compile Tools x64 |
| NI Linux Real-Time (ARM-based) | GNU C and C++ Compile Tools for ARMv7 |
| Phar Lap ETS | LabWindows/CVI 9.0 or later; Microsoft Visual C ++ 2003, 2008, or 2010 only. .Note NI ETS 2014 supports Microsoft Visual C ++ 2003, 2008, or 2010 NI ETS 2017 supports Microsoft Visual C ++ 2008 or 2010 only. |
| VxWorks | Wind River Workbench 2.3 or later; GNU Tool Chain for VxWorks, available for download. |
| Linux | GCC 3 or later. |

You can use a different ANSI C or ISO C compiler that supports your target
 platform. If you use a compiler that is not listed above, you might need to modify the
 provided examples and other components of the FPGA Interface C API.

Related information:

- Getting Started with C/C++ Development for
 NI Linux Real-Time
- GNU C and C++ Compile Tools x64
- GNU C and C++ Compile Tools for
 ARMv7
