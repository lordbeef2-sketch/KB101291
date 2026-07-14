# NI DOCUMENT BUNDLE: fpga-interface-c-api-ref

<!--NI_BUNDLE_CHUNK bundle=fpga-interface-c-api-ref start=1 end=33 -->
<!--NI_TOPIC bundle=fpga-interface-c-api-ref path=capi/api_reference.html language=enus -->
## TOPIC 00001: API Reference

- bundle_id: `fpga-interface-c-api-ref`
- source_path: `capi/api_reference.html`
- source_url: https://docs-be.ni.com/bundle/fpga-interface-c-api-ref/raw/resource/enus/capi/api_reference.html
- document_id: `fpga-interface-c-api-ref`
- page_type: `leaf`
- content_type: ``

API Reference

This book describes the errors, types, constants, and functions used in the FPGA Interface C API.

|  | To view related topics, click the Locate button, shown at left, on the toolbar at the top of this window. The FPGA Interface C API Help highlights this topic in the Contents tab so you can navigate the related topics. |
| --- | --- |

<!--NI_TOPIC bundle=fpga-interface-c-api-ref path=capi/building_application.html language=enus -->
## TOPIC 00002: Building a C/C++ Application

- bundle_id: `fpga-interface-c-api-ref`
- source_path: `capi/building_application.html`
- source_url: https://docs-be.ni.com/bundle/fpga-interface-c-api-ref/raw/resource/enus/capi/building_application.html
- document_id: `fpga-interface-c-api-ref`
- page_type: `leaf`
- content_type: ``

Building a C/C++ Application

#### Creating a Project

Use your development tools to create a project or makefile that includes the [two header files and the source file](generated_files.html). Add a new source file to the project or makefile. In the new source file, use #include to include the generated .h header file. The generated .h header file uses #include to include NiFpga.h.

|  | Note The Examples directory contains examples of project files and makefiles for different operating systems. |
| --- | --- |

|  | Note If you are developing an application for an NI Linux Real-Time target, use the C/C++ Development Tools for NI Linux Real-Time, Eclipse Edition 2013 or later. For information about the development tools, go to ni.com and enter the Info Code EclipseIDE. |
| --- | --- |

|  | Note If you are developing an application for a VxWorks target, refer to the NI tutorials The Definitive Guide: Programming NI VxWorks Real-Time Controllers in C/C++ and Developing Shared Libraries for the cRIO-901x and Other VxWorks Targets. |
| --- | --- |

|  | Note If you are developing an application for an R Series device, refer to the NI tutorial Building a R Series FPGA Interface Host Application in C. |
| --- | --- |

#### Writing C/C++ Code Using FPGA Interface C API Functions

Write your code using the functions described in the [API Reference](api_reference.html) book of this help file. All C/C++ applications must call the [required functions](functions_required.html). In order to interact with FPGA VIs, your application must call a [session function](functions_session.html) to open an FPGA session. From there, call other functions in NiFpga.h to [read](functions_read.html) and [write](functions_write.html) to controls and indicators, use [interrupts](functions_interrupt.html), or use other C/C++ functions.

Refer to the installed [examples](examples.html) to see how to use C API functions.

#### Developing and Maintaining the C/C++ Application

The constants in the generated header file are tied to the specific bitfile used to generate them. If you modify the FPGA VI, you must recompile the VI, regenerate the C API, and rebuild any C/C++ application that used the original C API. This is because the register offsets for controls and indicators may have changed unexpectedly. If you do not regenerate and rebuild, and instead try to use a new bitfile with an older application, you will get the [NiFpga_Status_SignatureMismatch](errors.html) error, because the signature of the bitfile does not match the signature passed to the [NiFpga_Open](functions_session.html) function.

The names of generated constants can change if you [rename your FPGA VI or any of the controls, indicators, or FIFOs in it](naming_conventions.html). If you change only the name of the FPGA VI, you can match the previous name by [using a custom prefix](naming_conventions.html) when you regenerate the C API. If you do not rename anything, you should be able to rebuild your C/C++ application without further modification.

|  | Tip To avoid having to recompile your entire C/C++ application every time you regenerate the C API, consider creating a shared library (.dll, .out, or .so, depending on your operating system) containing all your C API function calls. A shared library can abstract lower-level FPGA calls to higher-level ones, so that you do not have to rebuild your main application (.exe, .dll, or .out) every time you rebuild the shared library. Additionally, you can make field updates to your C/C++ application, wherein you deploy a new .lvbitx and shared library without having to update the entire application. |
| --- | --- |

<!--NI_TOPIC bundle=fpga-interface-c-api-ref path=capi/capi_related_documentation.html language=enus -->
## TOPIC 00003: FPGA Interface C API Related Documentation

- bundle_id: `fpga-interface-c-api-ref`
- source_path: `capi/capi_related_documentation.html`
- source_url: https://docs-be.ni.com/bundle/fpga-interface-c-api-ref/raw/resource/enus/capi/capi_related_documentation.html
- document_id: `fpga-interface-c-api-ref`
- page_type: `leaf`
- content_type: ``

FPGA Interface C API Related Documentation

Refer to the [API Reference](api_reference.html) book of this help file for explanations and descriptions of errors, types, constants, and functions in the FPGA Interface C API.

The C API is essentially a C version of the LabVIEW FPGA Interface. The LabVIEW FPGA Interface is installed with the LabVIEW FPGA Module and with the NI CompactRIO Device Drivers software. Functions in the C API correspond to VIs and functions on the FPGA Interface palette in LabVIEW. Referring to the *FPGA Interface* book of the *LabVIEW Help* may help you understand how the C API functions work.

<!--NI_TOPIC bundle=fpga-interface-c-api-ref path=capi/constants.html language=enus -->
## TOPIC 00004: Constants

- bundle_id: `fpga-interface-c-api-ref`
- source_path: `capi/constants.html`
- source_url: https://docs-be.ni.com/bundle/fpga-interface-c-api-ref/raw/resource/enus/capi/constants.html
- document_id: `fpga-interface-c-api-ref`
- page_type: `leaf`
- content_type: ``

Constants

Functions of the FPGA Interface C API can use the following constants.

| Name | Type | Description |
| --- | --- | --- |
| NiFpga_False | NiFpga_Bool | Represents a false condition. |
| NiFpga_True | NiFpga_Bool | Represents a true condition. |
| NiFpga_OpenAttribute_NoRun | bitmask | Optional attribute to NiFpga_Open that prevents the FPGA from running when a session is opened. |
| NiFpga_CloseAttribute_NoResetIfLastSession | bitmask | Optional attribute to NiFpga_Close that prevents the FPGA from being reset when a session is closed with no other sessions open. |
| NiFpga_RunAttribute_WaitUntilDone | bitmask | Optional attribute to NiFpga_Run that blocks the thread until the FPGA finishes running. |
| NiFpga_InfiniteTimeout | uint32_t | Represents an infinite timeout. |
| NiFpga_Irq_<IRQ Number> | bitmask | Enumeration of all 32 possible IRQs. Multiple IRQs can be bitwise ORed together like this: NiFpga_Irq_3 \| NiFpga_Irq_23 |

<!--NI_TOPIC bundle=fpga-interface-c-api-ref path=capi/deploying_running.html language=enus -->
## TOPIC 00005: Deploying and Running Applications

- bundle_id: `fpga-interface-c-api-ref`
- source_path: `capi/deploying_running.html`
- source_url: https://docs-be.ni.com/bundle/fpga-interface-c-api-ref/raw/resource/enus/capi/deploying_running.html
- document_id: `fpga-interface-c-api-ref`
- page_type: `leaf`
- content_type: ``

Deploying and Running Applications

#### Windows and Linux

In Windows and Linux, you can run a C/C++ application from within your development environment. If the original bitfile was built for a remote RIO target, your C/C++ application can interact with FPGA VIs running on a remote RIO target. To run a C/C++ application on a remote target, change the resource passed into NiFpga_Open from a local resource, such as RIO0, to a remote resource, such as rio://<*hostnameOrIpAddress*>/RIO0. You can substitute a valid RIO alias for the resource name.

#### VxWorks

If you are developing for a VxWorks system, you can use the serial console for debugging. FTP the built binary (MyApplication.out) and the .lvbitx file to the root directory of the target. Using the serial console, type the ld command as shown in the following example to load the library.

ld < MyApplication.out

After loading the library, you can call any function in the library from the serial console.

When your application is complete and debugged, you can set up the system to run it on startup. Modify ni-rt.ini by appending to StartupDLLs under the [LVRT] section.

For example, you would change "StartupDLLs=<*DLLs*>;" to "StartupDLLs=<*DLLs*>;/c/MyApplication.out;". Now your application will run every time the system starts up.

#### Phar Lap ETS

##### LabWindows/CVI

If you are using LabWindows/CVI to develop an application for a Phar Lap ETS real-time target, National Instruments recommends that you use the LabWindows/CVI Real-Time Module. Select **Run»Select Execution Target for Debugging»New Execution Target** to specify your target system. Then select **Run»Manage Files on Real-Time Execution Target** to add the .lvbitx file. You can then run the application by selecting **Run»Debug Project**. Refer to the LabWindows/CVI documentation for more information about running and deploying applications.

If you do not have the LabWindows/CVI Real-Time Module, you can still create DLLs and deploy them as described in the Microsoft Visual C++ section below.

##### Microsoft Visual C++

If you are using Microsoft Visual C++ to develop an application for a Phar Lap ETS real-time target, you must set up the system to run your application on startup. FTP the built binary (MyApplication.dll) and the .lvbitx file to the root directory of the target. Then modify ni-rt.ini by appending to StartupDLLs under the [LVRT] section.

For example, you would change "StartupDLLs=<*DLLs*>;" to "StartupDLLs=<*DLLs*>;C:\MyApplication.dll;". Now your application will run every time the system starts up.

#### NI Linux Real-Time

For information about developing C/C++ applications for NI Linux Real-Time targets, go to ni.com/info and enter the Info Code EclipseIDE.

#### Specifying the Location of the .lvbitx File

Because different operating systems have different default current working directories for applications, you must pass an absolute path for the **bitfile** parameter of the NiFpga_Open function. If you pass only the filename instead of an absolute path, the operating system may not be able to locate the bitfile. For more information, refer to the [Session Functions](functions_session.html) topic of this help file.

<!--NI_TOPIC bundle=fpga-interface-c-api-ref path=capi/errors.html language=enus -->
## TOPIC 00006: Errors

- bundle_id: `fpga-interface-c-api-ref`
- source_path: `capi/errors.html`
- source_url: https://docs-be.ni.com/bundle/fpga-interface-c-api-ref/raw/resource/enus/capi/errors.html
- document_id: `fpga-interface-c-api-ref`
- page_type: `leaf`
- content_type: ``

Errors

Functions of the FPGA Interface C API can return the following errors. All error codes have negative values. For any given error code, the equal and opposite positive value represents a warning, which alerts you to a similar problem or condition that does not cause a failure.

|  | Note For any NiFpga_Status code returned that is not listed in this topic, you can look up the corresponding error string by following the directions found here. |
| --- | --- |

| Error Code | Name | Description |
| --- | --- | --- |
| 0 | NiFpga_Status_Success | No errors or warnings. |
| −50400 | NiFpga_Status_FifoTimeout | The timeout expired before the FIFO operation could complete. |
| −50405 | NiFpga_Status_TransferAborted | No transfer is in progress because the transfer was aborted by the client. The operation could not be completed as specified. |
| −52000 | NiFpga_Status_MemoryFull | A memory allocation failed. Try again after rebooting. |
| −52003 | NiFpga_Status_SoftwareFault | An unexpected software error occurred. |
| −52005 | NiFpga_Status_InvalidParameter | A parameter to a function was not valid. This could be a NULL pointer, a bad value, etc. |
| −52006 | NiFpga_Status_ResourceNotFound | A required resource was not found. The NiFpga.* library, the RIO resource, or some other resource may be missing. |
| −52010 | NiFpga_Status_ResourceNotInitialized | A required resource was not properly initialized. This could occur if NiFpga_Initialize was not called or a required NiFpga_IrqContext was not reserved. |
| −61003 | NiFpga_Status_FpgaAlreadyRunning | The FPGA is already running. |
| −61018 | NiFpga_Status_DownloadError | An error occurred downloading the VI to the FPGA device. Verify that the target is connected and powered and that the resource of the target is properly configured. |
| −61024 | NiFpga_Status_DeviceTypeMismatch | The bitfile was not compiled for the specified resource's device type. |
| −61046 | NiFpga_Status_CommunicationTimeout | An error was detected in the communication between the host computer and the FPGA target. |
| −61060 | NiFpga_Status_IrqTimeout | The timeout expired before any of the IRQs were asserted. |
| −61070 | NiFpga_Status_CorruptBitfile | The specified bitfile is invalid or corrupt. |
| −61072 | NiFpga_Status_BadDepth | The requested FIFO depth is invalid. It is either 0 or an amount not supported by the hardware. |
| −61073 | NiFpga_Status_BadReadWriteCount | The number of FIFO elements is invalid. Either the number is greater than the depth of the host memory DMA FIFO, or more elements were requested for release than had been acquired. |
| −61083 | NiFpga_Status_ClockLostLock | A hardware clocking error occurred. A derived clock lost lock with its base clock during the execution of the LabVIEW FPGA VI. If any base clocks with derived clocks are referencing an external source, make sure that the external source is connected and within the supported frequency, jitter, accuracy, duty cycle, and voltage specifications. Also verify that the characteristics of the base clock match the configuration specified in the FPGA Base Clock Properties. If all base clocks with derived clocks are generated from free-running, on-board sources, please contact National Instruments technical support at ni.com/support. |
| −61141 | NiFpga_Status_FpgaBusy | The operation could not be performed because the FPGA is busy. Stop all activities on the FPGA before requesting this operation. If the target is in Scan Interface programming mode, put it in FPGA Interface programming mode. If RIO Device Setup or MAX is currently open for downloading a bitfile to flash memory on the device, wait until the download ends. |
| −61200 | NiFpga_Status_FpgaBusyFpgaInterfaceCApi | The operation could not be performed because the FPGA is busy operating in FPGA Interface C API mode. Stop all activities on the FPGA before requesting this operation. |
| −61201 | NiFpga_Status_FpgaBusyScanInterface | The chassis is in Scan Interface programming mode. In order to run FPGA VIs, you must go to the chassis properties page, select FPGA programming mode, and deploy settings. |
| −61202 | NiFpga_Status_FpgaBusyFpgaInterface | The operation could not be performed because the FPGA is busy operating in FPGA Interface mode. Stop all activities on the FPGA before requesting this operation. |
| −61203 | NiFpga_Status_FpgaBusyInteractive | The operation could not be performed because the FPGA is busy operating in Interactive mode. Stop all activities on the FPGA before requesting this operation. |
| −61204 | NiFpga_Status_FpgaBusyEmulation | The operation could not be performed because the FPGA is busy operating in Emulation mode. Stop all activities on the FPGA before requesting this operation. |
| −61211 | NiFpga_Status_ResetCalledWithImplicitEnableRemoval | LabVIEW FPGA does not support the Reset method for bitfiles that allow removal of implicit enable signals in single-cycle Timed Loops. |
| −61212 | NiFpga_Status_AbortCalledWithImplicitEnableRemoval | LabVIEW FPGA does not support the Abort method for bitfiles that allow removal of implicit enable signals in single-cycle Timed Loops. |
| −61213 | NiFpga_Status_CloseAndResetCalledWithImplicitEnableRemoval | LabVIEW FPGA does not support Close and Reset if Last Reference for bitfiles that allow removal of implicit enable signals in single-cycle Timed Loops. Pass NiFpga_CloseAttribute_NoResetIflastSession to NiFpga_Close instead. |
| −61214 | NiFpga_Status_ImplicitEnableRemovalButNotYetRun | For bitfiles that allow removal of implicit enable signals in single-cycle Timed Loops, LabVIEW FPGA does not support this method prior to running the bitfile. |
| −61215 | NiFpga_Status_RunAfterStoppedCalledWithImplicitEnableRemoval | Bitfiles that allow removal of implicit enable signals in single-cycle Timed Loops can run only once. Download the bitfile again before re-running the VI. |
| −61216 | NiFpga_Status_GatedClockHandshakingViolation | A gated clock has violated the handshaking protocol. If you are using external gated clocks, ensure that they follow the required clock gating protocol. If you are generating your clocks internally, please contact National Instruments Technical Support. |
| −61219 | NiFpga_Status_ElementsNotPermissibleToBeAcquired | The number of elements requested must be less than or equal to the number of unacquired elements left in the host memory DMA FIFO. There are currently fewer unacquired elements left in the FIFO than are being requested. Release some acquired elements before acquiring more elements. |
| −61252 | NiFpga_Status_FpgaBusyConfiguration | The operation could not be performed because the FPGA is in configuration or discovery mode. Wait for configuration or discovery to complete and retry your operation. |
| −61253 | NiFpga_Status_CloseAndResetCalledWithResetNotSupported | LabVIEW FPGA does not support Close and Reset if Last Reference for bitfiles that do not support Reset. Pass the NiFpga_CloseAttribute_NoResetIfLastSession attribute to NiFpga_Close instead of 0. |
| −61499 | NiFpga_Status_InternalError | An unexpected internal error occurred. |
| −63003 | NiFpga_Status_TotalDmaFifoDepthExceeded | The NI-RIO driver was unable to allocate memory for a FIFO. This can happen when the combined depth of all DMA FIFOs exceeds the maximum depth for the controller, or when the controller runs out of system memory. You may be able to reconfigure the controller with a greater maximum FIFO depth. For more information, refer to NI KnowledgeBase article 65OF2ERQ. |
| −63033 | NiFpga_Status_AccessDenied | Access to the remote system was denied. Use MAX to check the Remote Device Access settings under Software»NI-RIO»NI-RIO Settings on the remote system. |
| −63038 | NiFpga_Status_HostVersionMismatch | The NI-RIO software on the host is not compatible with the software on the target. Upgrade the NI-RIO software on the host in order to connect to this target. |
| −63040 | NiFpga_Status_RpcConnectionError | A connection could not be established to the specified remote device. Ensure that the device is on and accessible over the network, that NI-RIO software is installed, and that the RIO server is running and properly configured. |
| −63043 | NiFpga_Status_RpcSessionError | The RPC session is invalid. The target may have reset or been rebooted. Check the network connection and retry the operation. |
| −63082 | NiFpga_Status NiFpga_Status_FifoReserved | The operation could not complete because another session is accessing the FIFO. Close the other session and retry. |
| −63083 | NiFpga_Status_FifoElementsCurrentlyAcquired | A Read FIFO or Write FIFO function was called while the host had acquired elements of the FIFO. Release all acquired elements before reading or writing. |
| −63084 | NiFpga_Status_MisalignedAccess | A function was called using a misaligned address. The address must be a multiple of the size of the data type. |
| −63085 | NiFpga_Status_ControlOrIndicatorTooLarge | The FPGA Read/Write Control Function is accessing a control or indicator with data that exceeds the maximum size supported on the current target. Refer to the hardware documentation for the limitations on data types for this target. |
| −63101 | NiFpga_Status_BitfileReadError | A valid .lvbitx bitfile is required. If you are using a valid .lvbitx bitfile, the bitfile may not be compatible with the software you are using. Determine which version of LabVIEW was used to make the bitfile, update your software to that version or later, and try again. |
| −63106 | NiFpga_Status_SignatureMismatch | The specified signature does not match the signature of the bitfile. If the bitfile has been recompiled, regenerate the C API and rebuild the application. |
| −63107 | NiFpga_Status_IncompatibleBitfile | The bitfile you are trying to use is incompatible with the version of NI-RIO installed on the target and/or host. Update the version of NI-RIO on the target and/or host to the same version (or later) used to compile the bitfile. Alternatively, recompile the bitfile with the same version of NI-RIO that is currently installed on the target and/or host. |
| −63150 | NiFpga_Status_HardwareFault | An unspecified hardware failure has occurred. The operation could not be completed. |
| −63192 | NiFpga_Status_InvalidResourceName | Either the supplied resource name is invalid as a RIO resource name, or the device was not found. Use MAX to find the proper resource name for the intended device. |
| −63193 | NiFpga_Status_FeatureNotSupported | The requested feature is not supported. |
| −63194 | NiFpga_Status_VersionMismatch | The NI-RIO software on the target system is not compatible with this software. Upgrade the NI-RIO software on the target system. |
| −63195 | NiFpga_Status_InvalidSession | The session is invalid or has been closed. |
| −63198 | NiFpga_Status_OutOfHandles | The maximum number of open FPGA sessions has been reached. Close some open sessions. |

<!--NI_TOPIC bundle=fpga-interface-c-api-ref path=capi/example_path_errors.html language=enus -->
## TOPIC 00007: Fixing Build Problems in NI Linux Real-Time Applications

- bundle_id: `fpga-interface-c-api-ref`
- source_path: `capi/example_path_errors.html`
- source_url: https://docs-be.ni.com/bundle/fpga-interface-c-api-ref/raw/resource/enus/capi/example_path_errors.html
- document_id: `fpga-interface-c-api-ref`
- page_type: `leaf`
- content_type: ``

Fixing Build Problems in NI Linux Real-Time Applications

When you use C/C++ Development Tools for NI Linux Real-Time to build your application, you may receive an error message similar to the following:

Program "arm-none-linux-gnueabi-g++" not found in PATH 
 
Program "arm-none-linux-gnueabi-gcc" not found in PATH

This error occurs because an installed [example](examples.html) contains a path to the C++ cross-compiler toolchain that does not match what is installed on your development system.

In order to build your application, you must first correct the compiler path in the project properties. Complete the following steps to view and change the path setting in C/C++ Development Tools for NI Linux Real-Time.

1. Select Project»Properties .
2. Select C++ Build»Settings .
3. Click Cross Settings on the Tool Settings tab.
4. Change the compiler path to one of the paths listed in the following table, depending on the version of C/C++ Development Tools for NI Linux Real-Time you are using, the bitness of Windows on your development operating system, and the processor architecture of your RIO device. 

 C/C++ Development Tools for NI Linux Real-Time Version
Windows Bitness
Processor Architecture*†
Path
2014
32-bit
arm
C:\Program Files\National Instruments\Eclipse\14.0\arm\sysroots\i686-nilrtsdk-mingw32\usr\bin\armv7a-vfp-neon-nilrt-linux-gnueabi
2014
32-bit
x64
C:\Program Files\National Instruments\Eclipse\14.0\x64\sysroots\i686-nilrtsdk-mingw32\usr\bin\x86_64-nilrt-linux
2014
64-bit
arm
C:\Program Files (x86)\National Instruments\Eclipse\14.0\arm\sysroots\i686-nilrtsdk-mingw32\usr\bin\armv7a-vfp-neon-nilrt-linux-gnueabi
2014
64-bit
x64
C:\Program Files (x86)\National Instruments\Eclipse\14.0\x64\sysroots\i686-nilrtsdk-mingw32\usr\bin\x86_64-nilrt-linux
2013
32-bit
arm
C:\Program Files\National Instruments\Eclipse\toolchain\gcc-4.4-arm\i386\bin
2013
64-bit
arm
C:\Program Files (x86)\National Instruments\Eclipse\toolchain\gcc-4.4-arm\i386\bin
**Notes:**
 

* Use arm for CompactRIO controllers that have ARM-based processors, such as the cRIO-906*x*. Use x64 for CompactRIO controllers that have x86_64-based processors, such as the cRIO-903*x*.
 

† You can determine the processor architecture of an NI Linux Real-Time controller by running uname -a from an interactive shell.

<!--NI_TOPIC bundle=fpga-interface-c-api-ref path=capi/examples.html language=enus -->
## TOPIC 00008: Examples

- bundle_id: `fpga-interface-c-api-ref`
- source_path: `capi/examples.html`
- source_url: https://docs-be.ni.com/bundle/fpga-interface-c-api-ref/raw/resource/enus/capi/examples.html
- document_id: `fpga-interface-c-api-ref`
- page_type: `leaf`
- content_type: ``

Examples

The Examples directory is installed at 
C:\Users\Public\Documents\National Instruments\FPGA Interface C API\Examples\ and contains the following subdirectories:

- Platforms
- Arrays
- FIFOs
- IRQs

Additionally, if [LabWindows/CVI support](using_lw_cvi.html) is selected at install time, the FPGA Interface C API installer installs examples at C:\Users\Public\Documents\National Instruments\CVI\samples\FPGA Interface C API\.

NI recommends that you make a copy of any example files before modifying them. If you inadvertently modify installed files and want to revert changes, delete the modified files and use **Add or Remove Programs** to repair the FPGA Interface C API software installation.

#### The Platforms Subdirectory

The Platforms subdirectory contains LabVIEW source code and versions of a C/C++ application created for certain supported operating systems and compilers. Each subdirectory under Platforms contains example source code and project files specific to the minimum compatible version of the given compiler. For example, the files at \Examples\Platforms\Windows\CVI\9.0\ work with LabWindows/CVI 9.0 or later.

The C/C++ application is written in Example.cpp or Example.c, depending on the compiler. The application tests the temperature of the FPGA device, then waits while toggling either the FPGA LED (on a CompactRIO device) or Connector0/DO0 (on an R Series device). Complete the following steps to prepare an example for use.

1. Launch Example.lvproj .
2. In the LabVIEW Project Explorer window, add your FPGA target to the project.
3. If the Select Programming Mode dialog box appears, select LabVIEW FPGA Interface and click Continue .
4. The example project is populated with RIO devices containing FPGA targets. Expand one of the FPGA targets to find the example FPGA VI that works with your target.
 [IMAGE alt='Note' src='note.gif']
**Note** If you are using an R Series device, expand the PCI or PXI FPGA target. If you are using CompactRIO or Single-Board RIO, expand the CompactRIO FPGA target. The FPGA VI may require some modification to work with your target.
5. Drag the example FPGA VI to your FPGA target.
6. Open the FPGA VI to check for errors. You can resolve most errors by adding new FPGA I/O items to your project. In the LabVIEW Project Explorer window, right-click the FPGA target item and select New»FPGA I/O . On the New FPGA I/O dialog box that appears, select all available I/O resources, then click OK .
 [IMAGE alt='Note' src='note.gif']
**Note** The example application does not work without modification on NI 781x devices. The application reads the board temperature, and NI 781x devices do not support temperature reading. To use the example on these devices, you must remove the temperature-reading code.
7. Right-click the FPGA VI and select Create Build Specification from the shortcut menu. Under Build Specifications , right-click the new build specification for the example FPGA VI, select Build , and wait for the build to complete.
 [IMAGE alt='Note' src='note.gif']
**Note** For versions of LabVIEW earlier than 2010, right-click the example FPGA VI, select **Compile**, and wait for the compilation to complete.
8. Right-click the example FPGA VI and select Launch C API Generator .
9. In the FPGA Interface C API Generator dialog box that appears, change the Output Directory to the appropriate subdirectory, under Platforms , for your target operating system and compiler.
10. Click Generate to generate the C API.
11. In the output directory you selected in step 9 above, find the associated project file and open it.
  - For LabWindows/CVI, the project file is a .cws file.
  - For Microsoft Visual C++, the project file is a .sln file.
  - For NI Linux Real-Time and Wind River Workbench, you must import the entire directory using File»Import»Existing Project into Workspace .
  - For Linux, you must transfer the entire directory to your Linux development computer.

|  | Note For NI Linux Real-Time targets, refer to the Fixing Build Problems in NI Linux Real-Time Applications topic. |
| --- | --- |

#### The Arrays, FIFOs, and IRQs Subdirectories

The Arrays, FIFOs, and IRQs subdirectories contain example source code and generated header files. They provide examples of how to write code using the [Array](functions_readarray.html), [FIFO](functions_fifo_method.html), and [IRQ](functions_interrupt.html) functions, but they are not ready to run.

<!--NI_TOPIC bundle=fpga-interface-c-api-ref path=capi/fpgac.html language=enus -->
## TOPIC 00009: FPGA Interface C API Help

- bundle_id: `fpga-interface-c-api-ref`
- source_path: `capi/fpgac.html`
- source_url: https://docs-be.ni.com/bundle/fpga-interface-c-api-ref/raw/resource/enus/capi/fpgac.html
- document_id: `fpga-interface-c-api-ref`
- page_type: `leaf`
- content_type: ``

[IMAGE alt='image' src='ni_mainbitlogo_48.gif']

FPGA Interface C API Help

This help file describes the FPGA Interface C API, which you can use to create C/C++ applications that interact with LabVIEW FPGA VIs.

To navigate this help file, use the **Contents**,
**Index**, and **Search** tabs to the left of this
window.

For more information about this help file, refer to the
following topics:

[Related
Documentation](capi_related_documentation.html)

© 2009–2023 National Instruments Corporation. All rights reserved.

<!--NI_TOPIC bundle=fpga-interface-c-api-ref path=capi/functions.html language=enus -->
## TOPIC 00010: Functions

- bundle_id: `fpga-interface-c-api-ref`
- source_path: `capi/functions.html`
- source_url: https://docs-be.ni.com/bundle/fpga-interface-c-api-ref/raw/resource/enus/capi/functions.html
- document_id: `fpga-interface-c-api-ref`
- page_type: `leaf`
- content_type: ``

Functions

This book describes the functions in the FPGA Interface C API.

|  | To view related topics, click the Locate button, shown at left, on the toolbar at the top of this window. The FPGA Interface C API Help highlights this topic in the Contents tab so you can navigate the related topics. |
| --- | --- |

<!--NI_TOPIC bundle=fpga-interface-c-api-ref path=capi/functions_fifo_method.html language=enus -->
## TOPIC 00011: FIFO Method Functions

- bundle_id: `fpga-interface-c-api-ref`
- source_path: `capi/functions_fifo_method.html`
- source_url: https://docs-be.ni.com/bundle/fpga-interface-c-api-ref/raw/resource/enus/capi/functions_fifo_method.html
- document_id: `fpga-interface-c-api-ref`
- page_type: `leaf`
- content_type: ``

FIFO Method Functions

The FPGA Interface C API includes the following FIFO method functions.

#### NiFpga_ConfigureFifo

NiFpga_Status NiFpga_ConfigureFifo(NiFpga_Session session, uint32_t fifo, size_t depth)

Specifies the depth of the host memory part of the DMA FIFO. This method is optional. In order to see the actual depth configured, use NiFpga_ConfigureFifo2.

##### Parameters

| Name | Type | Description |
| --- | --- | --- |
| session | NiFpga_Session | handle to a currently open session |
| fifo | uint32_t | FIFO to configure |
| depth | size_t | requested number of elements in the host memory part of the DMA FIFO |

##### Return Value

result of the call

#### NiFpga_ConfigureFifo2

NiFpga_Status NiFpga_ConfigureFifo2(NiFpga_Session session, uint32_t fifo, size_t requestedDepth, size_t* actualDepth)

Specifies the depth of the host memory part of the DMA FIFO. This method is optional.

##### Parameters

| Name | Type | Description |
| --- | --- | --- |
| session | NiFpga_Session | handle to a currently open session |
| fifo | uint32_t | FIFO to configure |
| requestedDepth | size_t | requested number of elements in the host memory part of the DMA FIFO |
| actualDepth | size_t* | if non-NULL, outputs the actual number of elements in the host memory part of the DMA FIFO, which may be more than the requested number |

##### Return Value

result of the call

#### NiFpga_StartFifo

NiFpga_Status NiFpga_StartFifo(NiFpga_Session session, uint32_t fifo)

Starts a FIFO. This method is optional.

##### Parameters

| Name | Type | Description |
| --- | --- | --- |
| session | NiFpga_Session | handle to a currently open session |
| fifo | uint32_t | FIFO to start |

##### Return Value

result of the call

#### NiFpga_StopFifo

NiFpga_Status NiFpga_StopFifo(NiFpga_Session session, uint32_t fifo)

Stops a FIFO. This method is optional.

##### Parameters

| Name | Type | Description |
| --- | --- | --- |
| session | NiFpga_Session | handle to a currently open session |
| fifo | uint32_t | FIFO to stop |

##### Return Value

result of the call

#### NiFpga_ReleaseFifoElements

NiFpga_Status NiFpga_ReleaseFifoElements(NiFpga_Session session, uint32_t fifo, size_t elements)

Releases previously acquired FIFO elements. The FPGA target cannot read elements acquired by the host. Therefore, the host must release elements after acquiring them. Always release all acquired elements before closing the session. Do not attempt to access FIFO elements after the elements are released or the session is closed.

##### Parameters

| Name | Type | Description |
| --- | --- | --- |
| session | NiFpga_Session | handle to a currently open session |
| fifo | uint32_t | FIFO from which to release elements |
| elements | size_t | number of elements to release |

##### Return Value

result of the call

#### NiFpga_GetPeerToPeerFifoEndpoint

NiFpga_Status NiFpga_GetPeerToPeerFifoEndpoint(NiFpga_Session session, uint32_t fifo, uint32_t* endpoint)

Gets an endpoint reference to a peer-to-peer FIFO.

##### Parameters

| Name | Type | Description |
| --- | --- | --- |
| session | NiFpga_Session | handle to a currently open session |
| fifo | uint32_t | the peer-to-peer FIFO |
| endpoint | uint32_t* | outputs the endpoint reference |

##### Return Value

result of the call

<!--NI_TOPIC bundle=fpga-interface-c-api-ref path=capi/functions_fifo_read.html language=enus -->
## TOPIC 00012: Read FIFO Functions

- bundle_id: `fpga-interface-c-api-ref`
- source_path: `capi/functions_fifo_read.html`
- source_url: https://docs-be.ni.com/bundle/fpga-interface-c-api-ref/raw/resource/enus/capi/functions_fifo_read.html
- document_id: `fpga-interface-c-api-ref`
- page_type: `leaf`
- content_type: ``

Read FIFO Functions

The FPGA Interface C API includes the following Read FIFO functions, which share similar parameters.

#### NiFpga_ReadFifoBool

NiFpga_Status NiFpga_ReadFifoBool(NiFpga_Session session, uint32_t fifo, NiFpga_Bool* data, size_t numberOfElements, uint32_t timeout, size_t* elementsRemaining)

Reads from a target-to-host FIFO of Booleans.

#### NiFpga_ReadFifoI8

NiFpga_Status NiFpga_ReadFifoI8(NiFpga_Session session, uint32_t fifo, int8_t* data, size_t numberOfElements, uint32_t timeout, size_t* elementsRemaining)

Reads from a target-to-host FIFO of signed 8-bit integers.

#### NiFpga_ReadFifoU8

NiFpga_Status NiFpga_ReadFifoU8(NiFpga_Session session, uint32_t fifo, uint8_t* data, size_t numberOfElements, uint32_t timeout, size_t* elementsRemaining)

Reads from a target-to-host FIFO of unsigned 8-bit integers.

#### NiFpga_ReadFifoI16

NiFpga_Status NiFpga_ReadFifoI16(NiFpga_Session session, uint32_t fifo, int16_t* data, size_t numberOfElements, uint32_t timeout, size_t* elementsRemaining)

Reads from a target-to-host FIFO of signed 16-bit integers.

#### NiFpga_ReadFifoU16

NiFpga_Status NiFpga_ReadFifoU16(NiFpga_Session session, uint32_t fifo, uint16_t* data, size_t numberOfElements, uint32_t timeout, size_t* elementsRemaining)

Reads from a target-to-host FIFO of unsigned 16-bit integers.

#### NiFpga_ReadFifoI32

NiFpga_Status NiFpga_ReadFifoI32(NiFpga_Session session, uint32_t fifo, int32_t* data, size_t numberOfElements, uint32_t timeout, size_t* elementsRemaining)

Reads from a target-to-host FIFO of signed 32-bit integers.

#### NiFpga_ReadFifoU32

NiFpga_Status NiFpga_ReadFifoU32(NiFpga_Session session, uint32_t fifo, uint32_t* data, size_t numberOfElements, uint32_t timeout, size_t* elementsRemaining)

Reads from a target-to-host FIFO of unsigned 32-bit integers.

#### NiFpga_ReadFifoI64

NiFpga_Status NiFpga_ReadFifoI64(NiFpga_Session session, uint32_t fifo, int64_t* data, size_t numberOfElements, uint32_t timeout, size_t* elementsRemaining)

Reads from a target-to-host FIFO of signed 64-bit integers.

#### NiFpga_ReadFifoU64

NiFpga_Status NiFpga_ReadFifoU64(NiFpga_Session session, uint32_t fifo, uint64_t* data, size_t numberOfElements, uint32_t timeout, size_t* elementsRemaining)

Reads from a target-to-host FIFO of unsigned 64-bit integers.

#### Parameters for All Read FIFO Functions

| Name | Type | Description |
| --- | --- | --- |
| session | NiFpga_Session | handle to a currently open session |
| fifo | uint32_t | target-to-host FIFO from which to read |
| data | Varies by ReadFifo function | outputs the data that was read |
| numberOfElements | size_t | number of elements to read |
| timeout | uint32_t | timeout in milliseconds, or NiFpga_InfiniteTimeout |
| elementsRemaining | size_t* | if non-NULL, outputs the number of elements remaining in the host memory part of the DMA FIFO |

#### Return Value for All Read FIFO Functions

result of the call

<!--NI_TOPIC bundle=fpga-interface-c-api-ref path=capi/functions_fifo_read_acquire.html language=enus -->
## TOPIC 00013: Acquire FIFO Read Elements Functions

- bundle_id: `fpga-interface-c-api-ref`
- source_path: `capi/functions_fifo_read_acquire.html`
- source_url: https://docs-be.ni.com/bundle/fpga-interface-c-api-ref/raw/resource/enus/capi/functions_fifo_read_acquire.html
- document_id: `fpga-interface-c-api-ref`
- page_type: `leaf`
- content_type: ``

Acquire FIFO Read Elements Functions

Acquiring, reading, and releasing FIFO elements prevents the need to copy the contents of elements from the host memory buffer to a separate user-allocated buffer before reading. The FPGA target cannot write to elements acquired by the host. Therefore, the host must release elements after reading them. The number of elements acquired may differ from the number of elements requested if, for example, the number of elements requested reaches the end of the host memory buffer. Always release all acquired elements before closing the session. Do not attempt to access FIFO elements after the elements are released or the session is closed.

The FPGA Interface C API includes the following Acquire FIFO Read Elements functions, which share similar parameters.

#### NiFpga_AcquireFifoReadElementsBool

NiFpga_Status NiFpga_AcquireFifoReadElementsBool(NiFpga_Session session, uint32_t fifo, NiFpga_Bool** elements, size_t elementsRequested, uint32_t timeout, size_t* elementsAcquired, size_t* elementsRemaining)

Acquires elements for reading from a target-to-host FIFO of Booleans.

#### NiFpga_AcquireFifoReadElementsI8

NiFpga_Status NiFpga_AcquireFifoReadElementsI8(NiFpga_Session session, uint32_t fifo, int8_t** elements, size_t elementsRequested, uint32_t timeout, size_t* elementsAcquired, size_t* elementsRemaining)

Acquires elements for reading from a target-to-host FIFO of signed 8-bit integers.

#### NiFpga_AcquireFifoReadElementsU8

NiFpga_Status NiFpga_AcquireFifoReadElementsU8(NiFpga_Session session, uint32_t fifo, uint8_t** elements, size_t elementsRequested, uint32_t timeout, size_t* elementsAcquired, size_t* elementsRemaining)

Acquires elements for reading from a target-to-host FIFO of unsigned 8-bit integers.

#### NiFpga_AcquireFifoReadElementsI16

NiFpga_Status NiFpga_AcquireFifoReadElementsI16(NiFpga_Session session, uint32_t fifo, int16_t** elements, size_t elementsRequested, uint32_t timeout, size_t* elementsAcquired, size_t* elementsRemaining)

Acquires elements for reading from a target-to-host FIFO of signed 16-bit integers.

#### NiFpga_AcquireFifoReadElementsU16

NiFpga_Status NiFpga_AcquireFifoReadElementsU16(NiFpga_Session session, uint32_t fifo, uint16_t** elements, size_t elementsRequested, uint32_t timeout, size_t* elementsAcquired, size_t* elementsRemaining)

Acquires elements for reading from a target-to-host FIFO of unsigned 16-bit integers.

#### NiFpga_AcquireFifoReadElementsI32

NiFpga_Status NiFpga_AcquireFifoReadElementsI32(NiFpga_Session session, uint32_t fifo, int32_t** elements, size_t elementsRequested, uint32_t timeout, size_t* elementsAcquired, size_t* elementsRemaining)

Acquires elements for reading from a target-to-host FIFO of signed 32-bit integers.

#### NiFpga_AcquireFifoReadElementsU32

NiFpga_Status NiFpga_AcquireFifoReadElementsU32(NiFpga_Session session, uint32_t fifo, uint32_t** elements, size_t elementsRequested, uint32_t timeout, size_t* elementsAcquired, size_t* elementsRemaining)

Acquires elements for reading from a target-to-host FIFO of unsigned 32-bit integers.

#### NiFpga_AcquireFifoReadElementsI64

NiFpga_Status NiFpga_AcquireFifoReadElementsI64(NiFpga_Session session, uint32_t fifo, int64_t** elements, size_t elementsRequested, uint32_t timeout, size_t* elementsAcquired, size_t* elementsRemaining)

Acquires elements for reading from a target-to-host FIFO of signed 64-bit integers.

#### NiFpga_AcquireFifoReadElementsU64

NiFpga_Status NiFpga_AcquireFifoReadElementsU64(NiFpga_Session session, uint32_t fifo, uint64_t** elements, size_t elementsRequested, uint32_t timeout, size_t* elementsAcquired, size_t* elementsRemaining)

Acquires elements for reading from a target-to-host FIFO of unsigned 64-bit integers.

#### Parameters for All Acquire FIFO Read Elements Functions

| Name | Type | Description |
| --- | --- | --- |
| session | NiFpga_Session | handle to a currently open session |
| fifo | uint32_t | target-to-host FIFO from which to read |
| elements | Varies by AcquireFifoReadElements function | outputs a pointer to the elements acquired |
| elementsRequested | size_t | requested number of elements |
| timeout | uint32_t | timeout in milliseconds, or NiFpga_InfiniteTimeout |
| elementsAcquired | size_t* | actual number of elements acquired, which may be less than the requested number |
| elementsRemaining | size_t* | if non-NULL, outputs the number of elements remaining in the host memory part of the DMA FIFO |

#### Return Value for All Acquire FIFO Read Elements Functions

result of the call

<!--NI_TOPIC bundle=fpga-interface-c-api-ref path=capi/functions_fifo_write.html language=enus -->
## TOPIC 00014: Write FIFO Functions

- bundle_id: `fpga-interface-c-api-ref`
- source_path: `capi/functions_fifo_write.html`
- source_url: https://docs-be.ni.com/bundle/fpga-interface-c-api-ref/raw/resource/enus/capi/functions_fifo_write.html
- document_id: `fpga-interface-c-api-ref`
- page_type: `leaf`
- content_type: ``

Write FIFO Functions

The FPGA Interface C API includes the following Write FIFO functions, which share similar parameters.

#### NiFpga_WriteFifoBool

NiFpga_Status NiFpga_WriteFifoBool(NiFpga_Session session, uint32_t fifo, const NiFpga_Bool* data, size_t numberOfElements, uint32_t timeout, size_t* emptyElementsRemaining)

Writes to a host-to-target FIFO of Booleans.

#### NiFpga_WriteFifoI8

NiFpga_Status NiFpga_WriteFifoI8(NiFpga_Session session, uint32_t fifo, const int8_t* data, size_t numberOfElements, uint32_t timeout, size_t* emptyElementsRemaining)

Writes to a host-to-target FIFO of signed 8-bit integers.

#### NiFpga_WriteFifoU8

NiFpga_Status NiFpga_WriteFifoU8(NiFpga_Session session, uint32_t fifo, const uint8_t* data, size_t numberOfElements, uint32_t timeout, size_t* emptyElementsRemaining)

Writes to a host-to-target FIFO of unsigned 8-bit integers.

#### NiFpga_WriteFifoI16

NiFpga_Status NiFpga_WriteFifoI16(NiFpga_Session session, uint32_t fifo, const int16_t* data, size_t numberOfElements, uint32_t timeout, size_t* emptyElementsRemaining)

Writes to a host-to-target FIFO of signed 16-bit integers.

#### NiFpga_WriteFifoU16

NiFpga_Status NiFpga_WriteFifoU16(NiFpga_Session session, uint32_t fifo, const uint16_t* data, size_t numberOfElements, uint32_t timeout, size_t* emptyElementsRemaining)

Writes to a host-to-target FIFO of unsigned 16-bit integers.

#### NiFpga_WriteFifoI32

NiFpga_Status NiFpga_WriteFifoI32(NiFpga_Session session, uint32_t fifo, const int32_t* data, size_t numberOfElements, uint32_t timeout, size_t* emptyElementsRemaining)

Writes to a host-to-target FIFO of signed 32-bit integers.

#### NiFpga_WriteFifoU32

NiFpga_Status NiFpga_WriteFifoU32(NiFpga_Session session, uint32_t fifo, const uint32_t* data, size_t numberOfElements, uint32_t timeout, size_t* emptyElementsRemaining)

Writes to a host-to-target FIFO of unsigned 32-bit integers.

#### NiFpga_WriteFifoI64

NiFpga_Status NiFpga_WriteFifoI64(NiFpga_Session session, uint32_t fifo, const int64_t* data, size_t numberOfElements, uint32_t timeout, size_t* emptyElementsRemaining)

Writes to a host-to-target FIFO of signed 64-bit integers.

#### NiFpga_WriteFifoU64

NiFpga_Status NiFpga_WriteFifoU64(NiFpga_Session session, uint32_t fifo, const uint64_t* data, size_t numberOfElements, uint32_t timeout, size_t* emptyElementsRemaining)

Writes to a host-to-target FIFO of unsigned 64-bit integers.

#### Parameters for All Write FIFO Functions

| Name | Type | Description |
| --- | --- | --- |
| session | NiFpga_Session | handle to a currently open session |
| fifo | uint32_t | host-to-target FIFO to which to write |
| data | Varies by WriteFifo function | data to write |
| numberOfElements | size_t | number of elements to write |
| timeout | uint32_t | timeout in milliseconds, or NiFpga_InfiniteTimeout |
| emptyElementsRemaining | size_t* | if non-NULL, outputs the number of empty elements remaining in the host memory part of the DMA FIFO |

#### Return Value for All Write FIFO Functions

result of the call

<!--NI_TOPIC bundle=fpga-interface-c-api-ref path=capi/functions_fifo_write_acquire.html language=enus -->
## TOPIC 00015: Acquire FIFO Write Elements Functions

- bundle_id: `fpga-interface-c-api-ref`
- source_path: `capi/functions_fifo_write_acquire.html`
- source_url: https://docs-be.ni.com/bundle/fpga-interface-c-api-ref/raw/resource/enus/capi/functions_fifo_write_acquire.html
- document_id: `fpga-interface-c-api-ref`
- page_type: `leaf`
- content_type: ``

Acquire FIFO Write Elements Functions

Acquiring, writing, and releasing FIFO elements prevents the need to write first into a separate user-allocated buffer and then copy the contents of elements to the host memory buffer. The FPGA target cannot read elements acquired by the host. Therefore, the host must release elements after writing to them. The number of elements acquired may differ from the number of elements requested if, for example, the number of elements requested reaches the end of the host memory buffer. Always release all acquired elements before closing the session. Do not attempt to access FIFO elements after the elements are released or the session is closed.

The FPGA Interface C API includes the following Acquire FIFO Write Elements functions, which share similar parameters.

#### NiFpga_AcquireFifoWriteElementsBool

NiFpga_Status NiFpga_AcquireFifoWriteElementsBool(NiFpga_Session session, uint32_t fifo, NiFpga_Bool** elements, size_t elementsRequested, uint32_t timeout, size_t* elementsAcquired, size_t* elementsRemaining)

Acquires elements for writing to a host-to-target FIFO of Booleans.

#### NiFpga_AcquireFifoWriteElementsI8

NiFpga_Status NiFpga_AcquireFifoWriteElementsI8(NiFpga_Session session, uint32_t fifo, int8_t** elements, size_t elementsRequested, uint32_t timeout, size_t* elementsAcquired, size_t* elementsRemaining)

Acquires elements for writing to a host-to-target FIFO of signed 8-bit integers.

#### NiFpga_AcquireFifoWriteElementsU8

NiFpga_Status NiFpga_AcquireFifoWriteElementsU8(NiFpga_Session session, uint32_t fifo, uint8_t** elements, size_t elementsRequested, uint32_t timeout, size_t* elementsAcquired, size_t* elementsRemaining)

Acquires elements for writing to a host-to-target FIFO of unsigned 8-bit integers.

#### NiFpga_AcquireFifoWriteElementsI16

NiFpga_Status NiFpga_AcquireFifoWriteElementsI16(NiFpga_Session session, uint32_t fifo, int16_t** elements, size_t elementsRequested, uint32_t timeout, size_t* elementsAcquired, size_t* elementsRemaining)

Acquires elements for writing to a host-to-target FIFO of signed 16-bit integers.

#### NiFpga_AcquireFifoWriteElementsU16

NiFpga_Status NiFpga_AcquireFifoWriteElementsU16(NiFpga_Session session, uint32_t fifo, uint16_t** elements, size_t elementsRequested, uint32_t timeout, size_t* elementsAcquired, size_t* elementsRemaining)

Acquires elements for writing to a host-to-target FIFO of unsigned 16-bit integers.

#### NiFpga_AcquireFifoWriteElementsI32

NiFpga_Status NiFpga_AcquireFifoWriteElementsI32(NiFpga_Session session, uint32_t fifo, int32_t** elements, size_t elementsRequested, uint32_t timeout, size_t* elementsAcquired, size_t* elementsRemaining)

Acquires elements for writing to a host-to-target FIFO of signed 32-bit integers.

#### NiFpga_AcquireFifoWriteElementsU32

NiFpga_Status NiFpga_AcquireFifoWriteElementsU32(NiFpga_Session session, uint32_t fifo, uint32_t** elements, size_t elementsRequested, uint32_t timeout, size_t* elementsAcquired, size_t* elementsRemaining)

Acquires elements for writing to a host-to-target FIFO of unsigned 32-bit integers.

#### NiFpga_AcquireFifoWriteElementsI64

NiFpga_Status NiFpga_AcquireFifoWriteElementsI64(NiFpga_Session session, uint32_t fifo, int64_t** elements, size_t elementsRequested, uint32_t timeout, size_t* elementsAcquired, size_t* elementsRemaining)

Acquires elements for writing to a host-to-target FIFO of signed 64-bit integers.

#### NiFpga_AcquireFifoWriteElementsU64

NiFpga_Status NiFpga_AcquireFifoWriteElementsU64(NiFpga_Session session, uint32_t fifo, uint64_t** elements, size_t elementsRequested, uint32_t timeout, size_t* elementsAcquired, size_t* elementsRemaining)

Acquires elements for writing to a host-to-target FIFO of unsigned 64-bit integers.

#### Parameters for All Acquire FIFO Write Elements Functions

| Name | Type | Description |
| --- | --- | --- |
| session | NiFpga_Session | handle to a currently open session |
| fifo | uint32_t | host-to-target FIFO to which to write |
| elements | Varies by AcquireFifoWriteElements function | outputs a pointer to the elements acquired |
| elementsRequested | size_t | requested number of elements |
| timeout | uint32_t | timeout in milliseconds, or NiFpga_InfiniteTimeout |
| elementsAcquired | size_t* | actual number of elements acquired, which may be less than the requested number |
| elementsRemaining | size_t* | if non-NULL, outputs the number of elements remaining in the host memory part of the DMA FIFO |

#### Return Value for All Acquire FIFO Write Elements Functions

result of the call

<!--NI_TOPIC bundle=fpga-interface-c-api-ref path=capi/functions_interrupt.html language=enus -->
## TOPIC 00016: Interrupt Functions

- bundle_id: `fpga-interface-c-api-ref`
- source_path: `capi/functions_interrupt.html`
- source_url: https://docs-be.ni.com/bundle/fpga-interface-c-api-ref/raw/resource/enus/capi/functions_interrupt.html
- document_id: `fpga-interface-c-api-ref`
- page_type: `leaf`
- content_type: ``

Interrupt Functions

The FPGA Interface C API includes the following interrupt functions.

#### NiFpga_ReserveIrqContext

NiFpga_Status NiFpga_ReserveIrqContext(NiFpga_Session session, NiFpga_IrqContext* context)

Reserves an IRQ context. IRQ contexts are single-threaded; only one thread can wait with a particular context at any given time. To minimize jitter when first waiting on IRQs, reserve as many contexts as the application requires.

If a context is successfully reserved (the returned status is not an error), it must be unreserved later. Otherwise a memory leak will occur.

##### Parameters

| Name | Type | Description |
| --- | --- | --- |
| session | NiFpga_Session | handle to a currently open session |
| context | NiFpga_IrqContext* | outputs the IRQ context |

##### Return Value

result of the call

#### NiFpga_UnreserveIrqContext

NiFpga_Status NiFpga_UnreserveIrqContext(NiFpga_Session session, NiFpga_IrqContext context)

Unreserves an IRQ context obtained from NiFpga_ReserveIrqContext.

##### Parameters

| Name | Type | Description |
| --- | --- | --- |
| session | NiFpga_Session | handle to a currently open session |
| context | NiFpga_IrqContext | IRQ context to unreserve |

##### Return Value

result of the call

#### NiFpga_WaitOnIrqs

NiFpga_Status NiFpga_WaitOnIrqs(NiFpga_Session session, NiFpga_IrqContext context, uint32_t irqs, uint32_t timeout, uint32_t* irqsAsserted, NiFpga_Bool* timedOut)

This is a blocking function that stops the calling thread until the FPGA asserts any IRQ in the **irqs** parameter, or until the function call times out. Before calling this function, use NiFpga_ReserveIrqContext to reserve an IRQ context. No other threads can use the same context when this function is called. You can use the **irqsAsserted** parameter to determine which IRQs were asserted for each function call.

##### Parameters

| Name | Type | Description |
| --- | --- | --- |
| session | NiFpga_Session | handle to a currently open session |
| context | NiFpga_IrqContext | IRQ context with which to wait |
| irqs | uint32_t | bitwise OR of NiFpga_Irq values |
| timeout | uint32_t | timeout in milliseconds, or NiFpga_InfiniteTimeout |
| irqsAsserted | uint32_t* | if non-NULL, outputs bitwise OR of IRQs that were asserted |
| timedOut | NiFpga_Bool* | if non-NULL, outputs whether the timeout expired |

##### Return Value

result of the call

#### NiFpga_AcknowledgeIrqs

NiFpga_Status NiFpga_AcknowledgeIrqs(NiFpga_Session session, uint32_t irqs)

Acknowledges an IRQ or set of IRQs.

##### Parameters

| Name | Type | Description |
| --- | --- | --- |
| session | NiFpga_Session | handle to a currently open session |
| irqs | uint32_t | bitwise OR of NiFpga_Irqs |

##### Return Value

result of the call

<!--NI_TOPIC bundle=fpga-interface-c-api-ref path=capi/functions_method.html language=enus -->
## TOPIC 00017: Method Functions

- bundle_id: `fpga-interface-c-api-ref`
- source_path: `capi/functions_method.html`
- source_url: https://docs-be.ni.com/bundle/fpga-interface-c-api-ref/raw/resource/enus/capi/functions_method.html
- document_id: `fpga-interface-c-api-ref`
- page_type: `leaf`
- content_type: ``

Method Functions

The FPGA Interface C API includes the following method functions.

#### NiFpga_Run

NiFpga_Status NiFpga_Run(NiFpga_Session session, uint32_t attribute)

Runs the FPGA VI on the target. If you use NiFpga_RunAttribute_WaitUntilDone, NiFpga_Run blocks the thread until the FPGA finishes running.

##### Parameters

| Name | Type | Description |
| --- | --- | --- |
| session | NiFpga_Session | handle to a currently open session |
| attribute | uint32_t | bitwise OR of any NiFpga_RunAttributes, or 0 |

##### Return Value

result of the call

#### NiFpga_Abort

NiFpga_Status NiFpga_Abort(NiFpga_Session session)

Aborts the FPGA VI.

##### Parameters

| Name | Type | Description |
| --- | --- | --- |
| session | NiFpga_Session | handle to a currently open session |

##### Return Value

result of the call

#### NiFpga_Reset

NiFpga_Status NiFpga_Reset(NiFpga_Session session)

Resets the FPGA VI.

##### Parameters

| Name | Type | Description |
| --- | --- | --- |
| session | NiFpga_Session | handle to a currently open session |

##### Return Value

result of the call

#### NiFpga_Download

NiFpga_Status NiFpga_Download(NiFpga_Session session)

Re-downloads the FPGA bitstream to the target.

##### Parameters

| Name | Type | Description |
| --- | --- | --- |
| session | NiFpga_Session | handle to a currently open session |

##### Return Value

result of the call

<!--NI_TOPIC bundle=fpga-interface-c-api-ref path=capi/functions_read.html language=enus -->
## TOPIC 00018: Read Functions

- bundle_id: `fpga-interface-c-api-ref`
- source_path: `capi/functions_read.html`
- source_url: https://docs-be.ni.com/bundle/fpga-interface-c-api-ref/raw/resource/enus/capi/functions_read.html
- document_id: `fpga-interface-c-api-ref`
- page_type: `leaf`
- content_type: ``

Read Functions

The FPGA Interface C API includes the following Read functions, which share similar parameters.

#### NiFpga_ReadBool

NiFpga_Status NiFpga_ReadBool(NiFpga_Session session, uint32_t indicator, NiFpga_Bool* value)

Reads a boolean value from a given indicator or control.

#### NiFpga_ReadI8

NiFpga_Status NiFpga_ReadI8(NiFpga_Session session, uint32_t indicator, int8_t* value)

Reads a signed 8-bit integer value from a given indicator or control.

#### NiFpga_ReadU8

NiFpga_Status NiFpga_ReadU8(NiFpga_Session session, uint32_t indicator, uint8_t* value)

Reads an unsigned 8-bit integer value from a given indicator or control.

#### NiFpga_ReadI16

NiFpga_Status NiFpga_ReadI16(NiFpga_Session session, uint32_t indicator, int16_t* value)

Reads a signed 16-bit integer value from a given indicator or control.

#### NiFpga_ReadU16

NiFpga_Status NiFpga_ReadU16(NiFpga_Session session, uint32_t indicator, uint16_t* value)

Reads an unsigned 16-bit integer value from a given indicator or control.

#### NiFpga_ReadI32

NiFpga_Status NiFpga_ReadI32(NiFpga_Session session, uint32_t indicator, int32_t* value)

Reads a signed 32-bit integer value from a given indicator or control.

#### NiFpga_ReadU32

NiFpga_Status NiFpga_ReadU32(NiFpga_Session session, uint32_t indicator, uint32_t* value)

Reads an unsigned 32-bit integer value from a given indicator or control.

#### NiFpga_ReadI64

NiFpga_Status NiFpga_ReadI64(NiFpga_Session session, uint32_t indicator, int64_t* value)

Reads a signed 64-bit integer value from a given indicator or control.

#### NiFpga_ReadU64

NiFpga_Status NiFpga_ReadU64(NiFpga_Session session, uint32_t indicator, uint64_t* value)

Reads an unsigned 64-bit integer value from a given indicator or control.

#### Parameters for All Read Functions

| Name | Type | Description |
| --- | --- | --- |
| session | NiFpga_Session | handle to a currently open session |
| indicator | uint32_t | indicator or control from which to read |
| value | Varies by Read function | outputs the value that was read |

#### Return Value for All Read Functions

result of the call

<!--NI_TOPIC bundle=fpga-interface-c-api-ref path=capi/functions_readarray.html language=enus -->
## TOPIC 00019: ReadArray Functions

- bundle_id: `fpga-interface-c-api-ref`
- source_path: `capi/functions_readarray.html`
- source_url: https://docs-be.ni.com/bundle/fpga-interface-c-api-ref/raw/resource/enus/capi/functions_readarray.html
- document_id: `fpga-interface-c-api-ref`
- page_type: `leaf`
- content_type: ``

ReadArray Functions

The FPGA Interface C API includes the following ReadArray functions, which share similar parameters.

#### NiFpga_ReadArrayBool

NiFpga_Status NiFpga_ReadArrayBool(NiFpga_Session session, uint32_t indicator, NiFpga_Bool* array, size_t size)

Reads an entire array of boolean values from a given array indicator or control.

#### NiFpga_ReadArrayI8

NiFpga_Status NiFpga_ReadArrayI8(NiFpga_Session session, uint32_t indicator, int8_t* array, size_t size)

Reads an entire array of signed 8-bit integer values from a given array indicator or control.

#### NiFpga_ReadArrayU8

NiFpga_Status NiFpga_ReadArrayU8(NiFpga_Session session, uint32_t indicator, uint8_t* array, size_t size)

Reads an entire array of unsigned 8-bit integer values from a given array indicator or control.

#### NiFpga_ReadArrayI16

NiFpga_Status NiFpga_ReadArrayI16(NiFpga_Session session, uint32_t indicator, int16_t* array, size_t size)

Reads an entire array of signed 16-bit integer values from a given array indicator or control.

#### NiFpga_ReadArrayU16

NiFpga_Status NiFpga_ReadArrayU16(NiFpga_Session session, uint32_t indicator, uint16_t* array, size_t size)

Reads an entire array of unsigned 16-bit integer values from a given array indicator or control.

#### NiFpga_ReadArrayI32

NiFpga_Status NiFpga_ReadArrayI32(NiFpga_Session session, uint32_t indicator, int32_t* array, size_t size)

Reads an entire array of signed 32-bit integer values from a given array indicator or control.

#### NiFpga_ReadArrayU32

NiFpga_Status NiFpga_ReadArrayU32(NiFpga_Session session, uint32_t indicator, uint32_t* array, size_t size)

Reads an entire array of unsigned 32-bit integer values from a given array indicator or control.

#### NiFpga_ReadArrayI64

NiFpga_Status NiFpga_ReadArrayI64(NiFpga_Session session, uint32_t indicator, int64_t* array, size_t size)

Reads an entire array of signed 64-bit integer values from a given array indicator or control.

#### NiFpga_ReadArrayU64

NiFpga_Status NiFpga_ReadArrayU64(NiFpga_Session session, uint32_t indicator, uint64_t* array, size_t size)

Reads an entire array of unsigned 64-bit integer values from a given array indicator or control.

#### Parameters for All ReadArray Functions

| Name | Type | Description |
| --- | --- | --- |
| session | NiFpga_Session | handle to a currently open session |
| indicator | uint32_t | indicator or control from which to read |
| array | Varies by ReadArray function | outputs the entire array that was read |
| size | size_t | exact number of elements in the indicator or control |

#### Warning for All ReadArray Functions

The size passed must be the *exact* number of elements in the indicator or control.

#### Return Value for All ReadArray Functions

result of the call

<!--NI_TOPIC bundle=fpga-interface-c-api-ref path=capi/functions_required.html language=enus -->
## TOPIC 00020: Required Functions

- bundle_id: `fpga-interface-c-api-ref`
- source_path: `capi/functions_required.html`
- source_url: https://docs-be.ni.com/bundle/fpga-interface-c-api-ref/raw/resource/enus/capi/functions_required.html
- document_id: `fpga-interface-c-api-ref`
- page_type: `leaf`
- content_type: ``

Required Functions

The FPGA Interface C API requires the following functions for loading and unloading the NiFpga library.

#### NiFpga_Initialize

NiFpga_Status NiFpga_Initialize(void)

You must call this function before all other function calls. This function loads the NiFpga library so that all the other functions will work. If this function succeeds, you must call NiFpga_Finalize after all other function calls.

##### Warning

This function is not thread safe.

##### Return Value

result of the call

#### NiFpga_Finalize

NiFpga_Status NiFpga_Finalize(void)

You must call this function after all other function calls if NiFpga_Initialize succeeds. This function unloads the NiFpga library.

##### Warning

This function is not thread safe.

##### Return Value

result of the call

<!--NI_TOPIC bundle=fpga-interface-c-api-ref path=capi/functions_session.html language=enus -->
## TOPIC 00021: Session Functions

- bundle_id: `fpga-interface-c-api-ref`
- source_path: `capi/functions_session.html`
- source_url: https://docs-be.ni.com/bundle/fpga-interface-c-api-ref/raw/resource/enus/capi/functions_session.html
- document_id: `fpga-interface-c-api-ref`
- page_type: `leaf`
- content_type: ``

Session Functions

The FPGA Interface C API includes the following session functions.

#### NiFpga_Open

NiFpga_Status NiFpga_Open(const char* bitfile, const char* signature, const char* resource, uint32_t attribute, NiFpga_Session* session)

Opens a session to the FPGA. This call ensures that the contents of the bitfile are programmed to the FPGA. The FPGA runs unless the NiFpga_OpenAttribute_NoRun attribute is used.

Because different operating systems have different default current working directories for applications, you must pass an absolute path for the **bitfile** parameter. If you pass only the filename instead of an absolute path, the operating system may not be able to locate the bitfile. For example, the default current working directories are C:\ni-rt\system\ for Phar Lap ETS and /c/ for VxWorks. Because the generated *_Bitfile constant is a #define to a string literal, you can use C/C++ string-literal concatenation to form an absolute path. For example, if the bitfile is in the root directory of a Phar Lap ETS system, pass the following for the **bitfile** parameter.

"C:\\" NiFpga_MyApplication_Bitfile.

##### Parameters

| Name | Type | Description |
| --- | --- | --- |
| bitfile | const char* | path to the bitfile |
| signature | const char* | signature of the bitfile |
| resource | const char* | RIO resource string to open (RIO0 or rio://mysystem/RIO) |
| attribute | uint32_t | bitwise OR of any NiFpga_OpenAttributes, or 0 |
| session | NiFpga_Session* | outputs the session handle, which must be closed when no longer needed |

##### Return Value

result of the call

#### NiFpga_Close

NiFpga_Status NiFpga_Close(NiFpga_Session session, uint32_t attribute)

Closes the session to the FPGA. The FPGA resets unless either another session is still open or you use the NiFpga_CloseAttribute_NoResetIfLastSession attribute.

##### Parameters

| Name | Type | Description |
| --- | --- | --- |
| session | NiFpga_Session | handle to a currently open session |
| attribute | uint32_t | bitwise OR of any NiFpga_CloseAttributes, or 0 |

##### Return Value

result of the call

<!--NI_TOPIC bundle=fpga-interface-c-api-ref path=capi/functions_status.html language=enus -->
## TOPIC 00022: Status Functions

- bundle_id: `fpga-interface-c-api-ref`
- source_path: `capi/functions_status.html`
- source_url: https://docs-be.ni.com/bundle/fpga-interface-c-api-ref/raw/resource/enus/capi/functions_status.html
- document_id: `fpga-interface-c-api-ref`
- page_type: `leaf`
- content_type: ``

Status Functions

The FPGA Interface C API includes the following status functions.

#### NiFpga_IsError

NiFpga_Bool NiFpga_IsError(NiFpga_Status status)

Tests whether a status is an error.

##### Parameters

| Name | Type | Description |
| --- | --- | --- |
| status | NiFpga_Status | status to check for an error |

##### Return Value

whether the status was an error

#### NiFpga_IsNotError

NiFpga_Bool NiFpga_IsNotError(NiFpga_Status status)

Tests whether a status is not an error. Success and warnings are not errors.

##### Parameters

| Name | Type | Description |
| --- | --- | --- |
| status | NiFpga_Status | status to check for an error |

##### Return Value

whether the status was a success or warning

#### NiFpga_MergeStatus

NiFpga_Status NiFpga_MergeStatus(NiFpga_Status* status, NiFpga_Status newStatus)

Conditionally sets the status to a new value. The previous status is preserved unless the new status is more of an error, which means that warnings and errors overwrite successes, and errors overwrite warnings. New errors do not overwrite older errors, and new warnings do not overwrite older warnings.

##### Parameters

| Name | Type | Description |
| --- | --- | --- |
| status | NiFpga_Status* | status to conditionally set |
| newStatus | NiFpga_Status | new status value that may be set |

##### Return Value

the resulting status

#### NiFpga_IfIsNotError

#define NiFpga_IfIsNotError(status, expression)

This macro evaluates the expression only if the status is not an error. The expression must evaluate to an NiFpga_Status, such as a call to any NiFpga_* function, because the status will be set to the returned status if the expression is evaluated.

You can use this macro to mimic status chaining in LabVIEW, where the status does not have to be explicitly checked after each call. Such code may look like the following example.

NiFpga_Status status = NiFpga_Status_Success; 

NiFpga_IfIsNotError(status, NiFpga_WriteU32(...)); 

NiFpga_IfIsNotError(status, NiFpga_WriteU32(...)); 

NiFpga_IfIsNotError(status, NiFpga_WriteU32(...));

##### Parameters

| Name | Type | Description |
| --- | --- | --- |
| status | NiFpga_Status | status to check for an error |
| expression | expression returning NiFpga_Status | expression to call if the incoming status is not an error |

<!--NI_TOPIC bundle=fpga-interface-c-api-ref path=capi/functions_write.html language=enus -->
## TOPIC 00023: Write Functions

- bundle_id: `fpga-interface-c-api-ref`
- source_path: `capi/functions_write.html`
- source_url: https://docs-be.ni.com/bundle/fpga-interface-c-api-ref/raw/resource/enus/capi/functions_write.html
- document_id: `fpga-interface-c-api-ref`
- page_type: `leaf`
- content_type: ``

Write Functions

The FPGA Interface C API includes the following Write functions, which share similar parameters.

#### NiFpga_WriteBool

NiFpga_Status NiFpga_WriteBool(NiFpga_Session session, uint32_t control, NiFpga_Bool value)

Writes a boolean value to a given control or indicator.

#### NiFpga_WriteI8

NiFpga_Status NiFpga_WriteI8(NiFpga_Session session, uint32_t control, int8_t value)

Writes a signed 8-bit integer value to a given control or indicator.

#### NiFpga_WriteU8

NiFpga_Status NiFpga_WriteU8(NiFpga_Session session, uint32_t control, uint8_t value)

Writes an unsigned 8-bit integer value to a given control or indicator.

#### NiFpga_WriteI16

NiFpga_Status NiFpga_WriteI16(NiFpga_Session session, uint32_t control, int16_t value)

Writes a signed 16-bit integer value to a given control or indicator.

#### NiFpga_WriteU16

NiFpga_Status NiFpga_WriteU16(NiFpga_Session session, uint32_t control, uint16_t value)

Writes an unsigned 16-bit integer value to a given control or indicator.

#### NiFpga_WriteI32

NiFpga_Status NiFpga_WriteI32(NiFpga_Session session, uint32_t control, int32_t value)

Writes a signed 32-bit integer value to a given control or indicator.

#### NiFpga_WriteU32

NiFpga_Status NiFpga_WriteU32(NiFpga_Session session, uint32_t control, uint32_t value)

Writes an unsigned 32-bit integer value to a given control or indicator.

#### NiFpga_WriteI64

NiFpga_Status NiFpga_WriteI64(NiFpga_Session session, uint32_t control, int64_t value)

Writes a signed 64-bit integer value to a given control or indicator.

#### NiFpga_WriteU64

NiFpga_Status NiFpga_WriteU64(NiFpga_Session session, uint32_t control, uint64_t value)

Writes an unsigned 64-bit integer value to a given control or indicator.

#### Parameters for All Write Functions

| Name | Type | Description |
| --- | --- | --- |
| session | NiFpga_Session | handle to a currently open session |
| control | uint32_t | control or indicator to which to write |
| value | Varies by Write function | value to write |

#### Return Value for All Write Functions

result of the call

<!--NI_TOPIC bundle=fpga-interface-c-api-ref path=capi/functions_writearray.html language=enus -->
## TOPIC 00024: WriteArray Functions

- bundle_id: `fpga-interface-c-api-ref`
- source_path: `capi/functions_writearray.html`
- source_url: https://docs-be.ni.com/bundle/fpga-interface-c-api-ref/raw/resource/enus/capi/functions_writearray.html
- document_id: `fpga-interface-c-api-ref`
- page_type: `leaf`
- content_type: ``

WriteArray Functions

The FPGA Interface C API includes the following WriteArray functions, which share similar parameters.

#### NiFpga_WriteArrayBool

NiFpga_Status NiFpga_WriteArrayBool(NiFpga_Session session, uint32_t control, const NiFpga_Bool* array, size_t size)

Writes an entire array of boolean values to a given array control or indicator.

#### NiFpga_WriteArrayI8

NiFpga_Status NiFpga_WriteArrayI8(NiFpga_Session session, uint32_t control, const int8_t* array, size_t size)

Writes an entire array of signed 8-bit integer values to a given array control or indicator.

#### NiFpga_WriteArrayU8

NiFpga_Status NiFpga_WriteArrayU8(NiFpga_Session session, uint32_t control, const uint8_t* array, size_t size)

Writes an entire array of unsigned 8-bit integer values to a given array control or indicator.

#### NiFpga_WriteArrayI16

NiFpga_Status NiFpga_WriteArrayI16(NiFpga_Session session, uint32_t control, const int16_t* array, size_t size)

Writes an entire array of signed 16-bit integer values to a given array control or indicator.

#### NiFpga_WriteArrayU16

NiFpga_Status NiFpga_WriteArrayU16(NiFpga_Session session, uint32_t control, const uint16_t* array, size_t size)

Writes an entire array of unsigned 16-bit integer values to a given array control or indicator.

#### NiFpga_WriteArrayI32

NiFpga_Status NiFpga_WriteArrayI32(NiFpga_Session session, uint32_t control, const int32_t* array, size_t size)

Writes an entire array of signed 32-bit integer values to a given array control or indicator.

#### NiFpga_WriteArrayU32

NiFpga_Status NiFpga_WriteArrayU32(NiFpga_Session session, uint32_t control, const uint32_t* array, size_t size)

Writes an entire array of unsigned 32-bit integer values to a given array control or indicator.

#### NiFpga_WriteArrayI64

NiFpga_Status NiFpga_WriteArrayI64(NiFpga_Session session, uint32_t control, const int64_t* array, size_t size)

Writes an entire array of signed 64-bit integer values to a given array control or indicator.

#### NiFpga_WriteArrayU64

NiFpga_Status NiFpga_WriteArrayU64(NiFpga_Session session, uint32_t control, const uint64_t* array, size_t size)

Writes an entire array of unsigned 64-bit integer values to a given array control or indicator.

#### Parameters for All WriteArray Functions

| Name | Type | Description |
| --- | --- | --- |
| session | NiFpga_Session | handle to a currently open session |
| control | uint32_t | control or indicator to which to write |
| array | Varies by WriteArray function | entire array to write |
| size | size_t | exact number of elements in the control or indicator |

#### Warning for All WriteArray Functions

The size passed must be the *exact* number of elements in the control or indicator.

#### Return Value for All WriteArray Functions

result of the call

<!--NI_TOPIC bundle=fpga-interface-c-api-ref path=capi/generated_files.html language=enus -->
## TOPIC 00025: Generated Files

- bundle_id: `fpga-interface-c-api-ref`
- source_path: `capi/generated_files.html`
- source_url: https://docs-be.ni.com/bundle/fpga-interface-c-api-ref/raw/resource/enus/capi/generated_files.html
- document_id: `fpga-interface-c-api-ref`
- page_type: `leaf`
- content_type: ``

Generated Files

The generated FPGA Interface C API consists of the following files: a .h file, a .lvbitx file, NiFpga.h, and NiFpga.c. Unless you specify a custom prefix, the FPGA Interface C API Generator names the .h file, the .lvbitx file, and the constants in the .h file [based on the name of the FPGA VI](naming_conventions.html) from which the application bitfile was compiled.

#### Generated .h File

The .h file is a C header file that contains all the constants required by function calls in your application. For example, [NiFpga_Open](functions_session.html) requires the name of the .lvbitx file, provided by the generated *_Bitfile constant; and a digital signature of the FPGA bitstream in the bitfile, provided by the generated *_Signature constant. The other constants represent register offsets of each control, indicator, and FIFO in your VI, and other necessary information.

#### Generated .lvbitx Bitfile

This is a version of the original .lvbitx bitfile, renamed to match the prefix of the constants in the .h header file. NiFpga_Open must find this file in order to ensure the bitstream is downloaded to the FPGA.

#### NiFpga.h

This is a C header file. It is identical for all generated C APIs. It declares all the [errors, types, constants, and functions](api_reference.html) needed to write an application. Most of these functions are defined in NiFpga.c.

#### NiFpga.c

This is a C source file that you must include in your application. It is identical for all generated C APIs. It defines all the functions your application can call. NiFpga.c loads and unloads the NiFpga library at runtime, and forwards function calls to that library.

|  | Note If you installed LabWindows/CVI support and are using LabWindows/CVI to develop your C application, you do not need NiFpga.h or NiFpga.c. Exclude them from the files to be generated and use the header and library files installed with LabWindows/CVI support. |
| --- | --- |

<!--NI_TOPIC bundle=fpga-interface-c-api-ref path=capi/generating_c_api.html language=enus -->
## TOPIC 00026: Generating a C API for a LabVIEW FPGA Application

- bundle_id: `fpga-interface-c-api-ref`
- source_path: `capi/generating_c_api.html`
- source_url: https://docs-be.ni.com/bundle/fpga-interface-c-api-ref/raw/resource/enus/capi/generating_c_api.html
- document_id: `fpga-interface-c-api-ref`
- page_type: `leaf`
- content_type: ``

Generating a C API for a LabVIEW FPGA Application

You can generate a C API for a LabVIEW FPGA application from the LabVIEW Project Explorer window, from the Windows Start menu, or from a Windows command line. The generated C API consists of [the files needed to build and run a C/C++ application](generated_files.html).

The FPGA Interface C API Generator works only on .lvbitx files created with LabVIEW 2009 or later. It does not work on .lvbit files created with older versions of LabVIEW, or on .lvbitx files created with the pioneer NI Labs version of the FPGA Interface C API.

With any of the following generation methods, you can [specify a custom prefix](naming_conventions.html) for generated files and for the constants in the generated .h file. If you do not specify a custom prefix, the FPGA Interface C API Generator names files and constants based on the name of the FPGA VI from which the application bitfile was compiled.

#### Generating a C API from the LabVIEW Project Explorer Window

Complete the following steps to generate a C API for a compiled bitfile from the LabVIEW Project Explorer window.

1. Right-click the FPGA VI and select Create Build Specification from the shortcut menu.
2. Under Build Specifications , right-click the new build specification for the example FPGA VI, select Build , and wait for the build to complete.
 [IMAGE alt='Note' src='note.gif']
**Note** For versions of LabVIEW earlier than 2010, right-click the example FPGA VI, select **Compile**, and wait for the compilation to complete.
3. Right-click the compiled FPGA VI item and select Launch C API Generator from the shortcut menu.
4. On the FPGA Interface C API Generator dialog box that appears, ensure that the right compiled FPGA bitfile is selected. You can browse to the right bitfile or type an absolute path to it.
5. Select an output directory for the C API. If you do not select an output directory, the C API files will be created in the directory that contains the bitfile. You can browse to a directory or type an absolute path to it.
6. Optionally, you can change the prefix for the generated files and for the constants in the generated .h file.
7. If you are using LabWindows/CVI to develop your C application, place a check beside Exclude NiFpga.h/NiFpga.c because the FPGA Interface C API installs header and library files with LabWindows/CVI support.

#### Generating a C API from LabWindows/CVI 2010 or Later

Complete the following steps to generate a C API for a compiled bitfile from [LabWindows/CVI](using_lw_cvi.html) 2010 or later.

1. Select Tools»Launch FPGA Interface C API Generator .
2. On the FPGA Interface C API Generator dialog box that appears, browse to the compiled FPGA bitfile or type an absolute path to it.
3. Select an output directory for the C API. If you do not select an output directory, the C API files will be created in the directory that contains the bitfile. You can browse to a directory or type an absolute path to it.
4. Optionally, you can change the prefix for the generated files and for the constants in the generated .h file. Note that Exclude NiFpga.h/NiFpga.c is checked because the FPGA Interface C API installs header and library files with LabWindows/CVI support.

#### Generating a C API from the Windows Start Menu

Complete the following steps to generate a C API for a compiled bitfile from the Windows Start menu.

1. Select Start»All Programs»National Instruments»FPGA Interface C API»FPGA Interface C API Generator .
2. On the FPGA Interface C API Generator dialog box that appears, browse to the compiled FPGA bitfile or type an absolute path to it.
3. Select an output directory for the C API. If you do not select an output directory, the C API files will be created in the directory that contains the bitfile. You can browse to a directory or type an absolute path to it.
4. Optionally, you can change the prefix for the generated files and for the constants in the generated .h file.
5. If you are using LabWindows/CVI to develop your C application, place a check beside Exclude NiFpga.h/NiFpga.c because the FPGA Interface C API installs header and library files with LabWindows/CVI support.

#### Generating a C API from a Windows Command Line

Use the following syntax to generate a C API for a compiled bitfile from a Windows command line. Note that the second and third arguments, the path to output directory and prefix override, are optional.

capigen.exe "<*absolute path to .lvbitx file>*" ["<*absolute path to output directory>*" [<*prefix override>*]]

If you are using [LabWindows/CVI](using_lw_cvi.html) to develop your C application, use the following syntax to exclude NiFpga.h and NiFpga.h because the FPGA Interface C API installs header and library files with LabWindows/CVI support:

capigen.exe -e "<*absolute path to .lvbitx file>*" ["<*absolute path to output directory>*" [<*prefix override>*]]

#### Using Absolute Paths to Specify File and Directory Locations

You must use an absolute path to specify the .lvbitx file. If you specify an output directory, you must also use an absolute path. However, if you do not specify an output directory, the FPGA Interface C API Generator creates the C API files in the directory containing the.lvbitx file. If a path contains spaces and you are specifying it from a Windows command line, you must enclose the path in double quotation marks. The following is an example with absolute paths.

capigen.exe "C:\Documents and Settings\<*user-name>*\My Documents\LabVIEW Data\FPGA Bitfiles\MyBitfile.lvbitx" "C:\Documents and Settings\<*user-name>*\Desktop" MyPrefix

<!--NI_TOPIC bundle=fpga-interface-c-api-ref path=capi/naming_conventions.html language=enus -->
## TOPIC 00027: Naming Conventions for Generated Files and Constants

- bundle_id: `fpga-interface-c-api-ref`
- source_path: `capi/naming_conventions.html`
- source_url: https://docs-be.ni.com/bundle/fpga-interface-c-api-ref/raw/resource/enus/capi/naming_conventions.html
- document_id: `fpga-interface-c-api-ref`
- page_type: `leaf`
- content_type: ``

Naming Conventions for Generated Files and Constants

Unless you specify a custom prefix, the FPGA Interface C API Generator names the generated .h file, the .lvbitx file, and the constants in the .h file based on the name of the FPGA VI from which the application bitfile was compiled.

#### Characters Permitted in File and Constant Names

The FPGA Interface C API Generator removes all characters except alphanumeric characters and underscores from the name of the FPGA VI before using the name of the VI as the prefix for the generated C API. The FPGA Interface C API Generator cannot properly process multi-byte characters such as those used in East Asian-locale Windows systems. National Instruments recommends that you use only single-byte alphanumeric characters and underscores in the names of FPGA VIs, labels of controls and indicators, and names of FIFOs so that the FPGA Interface C API Generator can use them to create valid C/C++ identifiers. If your FPGA VI name contains multi-byte characters, specify a custom prefix before generating the C API.

|  | Note You can use multi-byte characters in the captions of controls and indicators without affecting the generated C API. |
| --- | --- |

#### Naming of Files and Constants

For example, if the original bitfile was compiled from an FPGA VI called My Temperature-Monitoring Application.vi, the generated .lvbitx file would by default be named NiFpga_MyTemperatureMonitoringApplication.lvbitx.

The FPGA Interface C API Generator uses the VI name or custom prefix, the data type, and the label or name of each control, indicator, and FIFO in the FPGA VI, to create the names of each constant in the .h file.

The FPGA Interface C API Generator removes all characters except alphanumeric characters and underscores from the label of the control or indicator, or from the name of the FIFO, before using the label or name in the name of the constant. The following example is the name of a constant corresponding to a Boolean indicator called Max Temp Exceeded in the FPGA VI described above.

NiFpga_MyTemperatureMonitoringApplication_IndicatorBool_MaxTempExceeded

<!--NI_TOPIC bundle=fpga-interface-c-api-ref path=capi/overview.html language=enus -->
## TOPIC 00028: What You Can Do with the FPGA Interface C API

- bundle_id: `fpga-interface-c-api-ref`
- source_path: `capi/overview.html`
- source_url: https://docs-be.ni.com/bundle/fpga-interface-c-api-ref/raw/resource/enus/capi/overview.html
- document_id: `fpga-interface-c-api-ref`
- page_type: `leaf`
- content_type: ``

What You Can Do with the FPGA Interface C API

The FPGA Interface C API enables C/C++ applications to interact directly with compiled LabVIEW FPGA VIs on RIO devices without using LabVIEW. C/C++ applications can download a VI to a RIO target, perform DMA data transfers, wait on and acknowledge interrupts, and read from and write to named controls and indicators using C function calls.

A C/C++ application created with the C API can run on the real-time processor of a CompactRIO or NI Single-Board RIO device, and interact with VIs running on the FPGA of the RIO system. Alternatively, a C/C++ application can run on the real-time processor of a PXI system or the processor of a Windows or Linux PC, and interact with VIs running on the FPGA of a PXI or PCI RIO device.

#### What You Cannot Do with the C API

The current version of the C API does not support the following features.

- Scan Interface mode and I/O variables
- Reading from and writing to controls, indicators, and FIFOs containing the following:
  - Fixed-point types
  - Floating-point types
  - Clusters
  - Arrays containing anything other than supported scalar types
- The following methods callable from an Invoke Method node:
  - Read TEDS
  - NI 9802 methods
    - Mount SD Card
    - Unmount SD Card
  - NI FlexRIO Adapter Module methods
    - Control IO Module Power
    - IO Module Status
    - Redetect IO Module

<!--NI_TOPIC bundle=fpga-interface-c-api-ref path=capi/required_items.html language=enus -->
## TOPIC 00029: What You Need to Get Started

- bundle_id: `fpga-interface-c-api-ref`
- source_path: `capi/required_items.html`
- source_url: https://docs-be.ni.com/bundle/fpga-interface-c-api-ref/raw/resource/enus/capi/required_items.html
- document_id: `fpga-interface-c-api-ref`
- page_type: `leaf`
- content_type: ``

What You Need to Get Started

In addition to a RIO device such as a CompactRIO reconfigurable chassis, a Single-Board RIO device, or a PXI or PCI RIO device, you need the following software to use the FPGA Interface C API.

- LabVIEW 2012 SP1 or later (32-bit only)
- LabVIEW FPGA Module 2012 SP1 or later (32-bit only)
- 2015 or later version of the driver software for your device
- Supported development operating system: 
 Operating System
64-bit
32-bit
Windows 10
**✓**
**✓**
Windows 8.1
**✓**
**✓**
Windows 7 Professional SP1
**✓**
**✓**
Windows Server 2012 R2
**✓**
—
Windows Server 2008 R2 SP1
**✓**
—
- Supported target operating system
- Supported C/C++ Compiler

<!--NI_TOPIC bundle=fpga-interface-c-api-ref path=capi/supported_compilers.html language=enus -->
## TOPIC 00030: Supported C/C++ Compilers

- bundle_id: `fpga-interface-c-api-ref`
- source_path: `capi/supported_compilers.html`
- source_url: https://docs-be.ni.com/bundle/fpga-interface-c-api-ref/raw/resource/enus/capi/supported_compilers.html
- document_id: `fpga-interface-c-api-ref`
- page_type: `leaf`
- content_type: ``

Supported C/C++ Compilers

The C/C++ compiler you can use to compile your application depends on the operating system the application will run on. National Instruments has tested the following combinations of target platforms and C/C++ compilers.

| Target Platform | Tested and Supported C/C++ Compiler(s) |
| --- | --- |
| Windows | NI LabWindowsTM/CVITM 9.0 or later; Microsoft Visual C++ 2003 or later |
| NI Linux Real-Time | C/C++ Development Tools for NI Linux Real-Time, Eclipse Edition 2013 or later |
| Phar Lap ETS | NI LabWindows/CVI 9.0 or later; Microsoft Visual C ++ 2003, 2008, or 2010 only Note NI ETS 2014 supports Microsoft Visual C ++ 2003, 2008, or 2010 NI ETS 2017 supports Microsoft Visual C ++ 2008 or 2010 only |
|  | Note NI ETS 2014 supports Microsoft Visual C ++ 2003, 2008, or 2010 NI ETS 2017 supports Microsoft Visual C ++ 2008 or 2010 only |
| VxWorks | Wind River Workbench 2.3 or later; GNU Tool Chain for VxWorks, available for download from NI |
| Linux | GCC 3 or later |

You can use a different ANSI C or ISO C compiler that supports your target platform. If you use a compiler that is not listed above, you may have to modify the provided examples and other components of the FPGA Interface C API.

<!--NI_TOPIC bundle=fpga-interface-c-api-ref path=capi/target_os.html language=enus -->
## TOPIC 00031: Supported Target Operating Systems

- bundle_id: `fpga-interface-c-api-ref`
- source_path: `capi/target_os.html`
- source_url: https://docs-be.ni.com/bundle/fpga-interface-c-api-ref/raw/resource/enus/capi/target_os.html
- document_id: `fpga-interface-c-api-ref`
- page_type: `leaf`
- content_type: ``

Supported Target Operating Systems

When you have [generated the C API](generating_c_api.html) from LabVIEW FPGA in a [supported Windows operating system](required_items.html), you can create a C application that calls into the C API. Although you can use a variety of development environments (such as NI LabWindows/CVI), both your C application and the NI CompactRIO Device Drivers software must run on the target operating system and CPU architecture.

The C application and the NI CompactRIO Device Drivers software can run on the following operating systems and CPU architectures:

| CPU Architecture | Operating System | Versions or Distributions | Hardware Targets |
| --- | --- | --- | --- |
| x86, x86_64 | Windows | Any version supported for development | PC, PXI |
| x86, x86_64 | Linux | Red Hat Enterprise Linux 6.x, Scientific Linux 6.x, openSUSE 13.1 or 12.x | PC, PXI |
| x86_64, ARM | LabVIEW Real-Time | NI Linux Real-Time | NI CompactRIO |
| x86 | LabVIEW Real-Time | Phar Lap ETS | PC, PXI |
| PowerPC | LabVIEW Real-Time | VxWorks | NI CompactRIO, NI Single-Board RIO |

<!--NI_TOPIC bundle=fpga-interface-c-api-ref path=capi/types.html language=enus -->
## TOPIC 00032: Types

- bundle_id: `fpga-interface-c-api-ref`
- source_path: `capi/types.html`
- source_url: https://docs-be.ni.com/bundle/fpga-interface-c-api-ref/raw/resource/enus/capi/types.html
- document_id: `fpga-interface-c-api-ref`
- page_type: `leaf`
- content_type: ``

Types

Functions of the FPGA Interface C API can use the following types.

| Name | Description |
| --- | --- |
| NiFpga_Bool | A boolean value; either NiFpga_False or NiFpga_True. |
| NiFpga_Status | Represents the resulting status of a function call through its return value. 0 is success, negative values are errors, and positive values are warnings. |
| NiFpga_Session | A handle to an FPGA session. |
| NiFpga_OpenAttribute | Enumeration of attributes that can be bitwise ORed together and passed as the attribute argument to NiFpga_Open. |
| NiFpga_CloseAttribute | Enumeration of attributes that can be bitwise ORed together and passed as the attribute argument to NiFpga_Close. |
| NiFpga_RunAttribute | Enumeration of attributes that can be bitwise ORed together and passed as the attribute argument to NiFpga_Run. |
| NiFpga_Irq | Enumeration of all 32 possible IRQs. Multiple IRQs can be bitwise ORed together like this: NiFpga_Irq_3 \| NiFpga_Irq_23 |
| NiFpga_IrqContext | See NiFpga_ReserveIrqContext for more information. |

<!--NI_TOPIC bundle=fpga-interface-c-api-ref path=capi/using_lw_cvi.html language=enus -->
## TOPIC 00033: Using the FPGA Interface C API with LabWindows/CVI

- bundle_id: `fpga-interface-c-api-ref`
- source_path: `capi/using_lw_cvi.html`
- source_url: https://docs-be.ni.com/bundle/fpga-interface-c-api-ref/raw/resource/enus/capi/using_lw_cvi.html
- document_id: `fpga-interface-c-api-ref`
- page_type: `leaf`
- content_type: ``

Using the FPGA Interface C API with LabWindows/CVI

You can generate a C API for a LabVIEW FPGA application and develop your C application using LabWindows/CVI 9.0 or later.

The FPGA Interface C API installer installs the following items if you select LabWindows/CVI support during installation:

- FPGA Interface C API Library and header file for LabWindows/CVI. This library supports LabWindows/CVI development and debugging features like user protection and resource tracking.
- LabWindows/CVI function panels for the FPGA Interface C API Library. These function panels are customized to help you select appropriate parameter values in calls to the library functions. This customization is also available in the Show Prototypes feature of the LabWindows/CVI source editor.
- LabWindows/CVI examples

With LabWindows/CVI 2010 or later, you can [launch the FPGA Interface C API Generator from LabWindows/CVI](generating_c_api.html). With LabWindows/CVI 9.0 or later, you can [launch the FPGA Interface C API Generator](generating_c_api.html) from the LabVIEW Project Explorer window, from the Windows Start menu, or from a Windows command line.

If you are using only LabWindows/CVI to develop your C application, you can exclude NiFpga.h and NiFpga.c from the files that you generate using [the FPGA Interface C API Generator](generating_c_api.html). The header and library files installed with LabWindows/CVI support make NiFpga.h and NiFpga.c unnecessary.
