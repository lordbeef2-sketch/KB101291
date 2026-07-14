# NI DOCUMENT BUNDLE: automotive-diagnostic-command-set-toolkit

<!--NI_BUNDLE_CHUNK bundle=automotive-diagnostic-command-set-toolkit start=1 end=16 -->
<!--NI_TOPIC bundle=automotive-diagnostic-command-set-toolkit path=activating-your-software.html language=enus -->
## TOPIC 00001: Activating Your Software

- bundle_id: `automotive-diagnostic-command-set-toolkit`
- source_path: `activating-your-software.html`
- source_url: https://docs-be.ni.com/bundle/automotive-diagnostic-command-set-toolkit/raw/resource/enus/activating-your-software.html
- document_id: `automotive-diagnostic-command-set-toolkit`
- page_type: `leaf`
- content_type: `concept`
- source_description: How Do I Activate My Software? Before using your product, you must activate it in accordance with its license agreement. To activate a product, you must first purchase a license. For information on purchasing licenses, contact your local NI sales representative or visit ni.com/niglobal. Complete the

### Activating Your Software

#### How Do I Activate My Software?

Before using your product, you must activate it in accordance with its license agreement. To activate a product, you must first purchase a license. For information on purchasing licenses, contact your local NI sales representative or visit ni.com/niglobal.

Complete the following steps to activate your NI products:

1. Open NI License Manager from the following location:
  - (Windows 7) Select Start»All Programs»National Instruments»License Manager»NI License
 Manager .
  - (Windows 8) Click NI Launcher and select NI License
 Manager .
  - (Windows 10) Select Start»National Instruments»NI License Manager .
2. Select one of the following methods to launch the Activate Software window: 
 Note The first time
 you open NI software, the license activation window launches automatically.
  - Click Activate Software on the ribbon.
  - When in the Local Licenses view, right-click the
 product in the License tree and select
 Activate .
3. If requested, log in to your NI User Account. If you do not have a User Account, you must create one.
4. Select one of the following methods to activate your products.
  - Check my account for licenses. Licenses associated with your account are verified
 successfully, activation completes. If your account lacks the
 appropriate licenses for a particular product, proceed to activate
 the product using either a activation code or a serial number.
  - Enter a serial number. You can find your serial numbers in the following locations:
    - On the Certificate of Ownership included in your software
 kit,
    - On the product packing slip or shipping label,
    - Visit ni.com/info and enter the Info Code
 SerialNumbers_en.
    - If you have installed a previous version of your application
 software using your serial number, you can find the serial
 number by selecting Help»About within the
 application.
    - Contact your local NI
 branch.
  - Enter activation codes. Click on Generate an activation code or visit
 ni.com/activate to obtain an activation code.
  - Connect to a volume license server. Enter the name of the volume license server on which
 your NI products should check for licenses.
5. Follow the prompts in the Activate Software window to complete activation.

If you activated through your NI software, you can use the product immediately after successful activation.

Note

- If you were using NI software before you began the activation process, you may need to restart the software for the change to take effect.
- If your NI software is licensed through a volume license agreement, you do not need to activate your product. Instead, you need to point NI License Manager to a volume license server. For more information, refer to the Using a Volume License Server topic of the NI License Manager Help .

#### What Is Activation?

Activation is the process of obtaining an activation code to enable your software to run on your computer. An activation code is an alphanumeric string that verifies the software, version, and computer ID to enable features on your computer. Activation codes are unique and are valid on only one computer.

#### What Information Do I Need to Activate My NI Software?

You need your NI User account log-in, the product version and serial number, and a computer ID that uniquely identifies your computer. Certain activation methods may require additional information for delivery. This information is used only to activate your product. Complete disclosure of the NI software licensing information privacy policy is available at ni.com/activate/privacy. If you optionally choose to register your software, your information is protected under the NI privacy policy, available at ni.com/privacy.

#### How Do I Find My Product Serial Number?

Your serial number uniquely identifies your purchase of NI software. You can find your serial number on the Certificate of Ownership included in your software kit, or you can visit ni.com/info and enter the Info Code SerialNumbers_en.

If you have installed a previous version using your serial number, you can find the serial number by selecting Help»About within the application. You can also contact your local NI branch at ni.com/contact.

#### What Is a Computer ID?

The computer ID is a 16-character value that uniquely identifies your computer. NI requires this information to enable your software. You can find your computer ID through the NI Licensing Wizard or by using NI License Manager, as follows:

1. Launch the NI License Manager.
2. Click Computer Information in the ribbon.

For more information about product activation and licensing, refer to ni.com/activate.

#### How Can I Evaluate NI Software?

You can evaluate most NI products, in accordance with the license agreement. Evaluation terms vary, depending on which product you want to evaluate. Refer to your product documentation for specific information on the product's evaluation mode.

#### Moving Software after Activation

To transfer your software to another computer, uninstall the software on the first computer, then install and activate it on the second computer. You can transfer your software from one computer to another; you do not need to contact or inform NI of the transfer. Because activation codes are unique to each computer, you will need a new activation code. Refer to the How do I Activate my Software? section of this topic to learn how to acquire a new activation code and reactivate your software.

#### Deactivating a Product

To deactivate a product and return it to its preactivation state, navigate to the Local Licenses view, select the product to be deactivated, and click Deactivate from the ribbon. Alternatively, navigate to the Local Licenses view, right-click the product in the License tree, and click Deactivate. If the product was in evaluation mode before you activated it, the properties of the evaluation mode may not be restored.

#### Using Windows Guest Accounts

NI License Manager does not support Microsoft Windows Guest accounts. You must log in to a non-Guest account to run licensed NI application software.

<!--NI_TOPIC bundle=automotive-diagnostic-command-set-toolkit path=application-development-on-compactrio-or-r-se.html language=enus -->
## TOPIC 00002: Application Development on CompactRIO or R Series Using the NI 985x or NI 986x C Series Module

- bundle_id: `automotive-diagnostic-command-set-toolkit`
- source_path: `application-development-on-compactrio-or-r-se.html`
- source_url: https://docs-be.ni.com/bundle/automotive-diagnostic-command-set-toolkit/raw/resource/enus/application-development-on-compactrio-or-r-se.html
- document_id: `automotive-diagnostic-command-set-toolkit`
- page_type: `leaf`
- content_type: `concept`
- source_description: To run a project on an FPGA target with an NI 985x C Series module, you need an FPGA bitfile (.lvbitx). The FPGA bitfile is downloaded to the FPGA target on the execution host. A bitfile is a compiled version of an FPGA VI. FPGA VIs, and thus bitfiles, define the CAN, analog, digital, and pulse widt

### Application Development on CompactRIO or R Series Using the NI 985x or NI 986x C Series Module

To run a project on an FPGA target with an NI 985x C Series module, you need an FPGA bitfile
 (.lvbitx). The FPGA bitfile is downloaded to the FPGA target on the
 execution host. A bitfile is a compiled version of an FPGA VI. FPGA VIs, and thus
 bitfiles, define the CAN, analog, digital, and pulse width modulation (PWM) inputs and
 outputs of an FPGA target. The Automotive Diagnostic Command Set does not include FPGA
 bitfiles for any FPGA target. Refer to the LabVIEW FPGA Module documentation for more
 information about creating FPGA VIs and bitfiles for an FPGA target.

The default FPGA VI is sufficient for a basic Automotive Diagnostic Command Set application.
 However, in some situations you may need to modify the existing FPGA code to create a
 custom bitfile. For example, to use additional I/O on the FPGA target, you must add
 these I/O to the FPGA VI. You must install the LabVIEW FPGA Module to create these
 files.

Modify the FPGA VI according to the following guidelines:

- Do not modify, remove, or rename any block diagram controls and indicators named __CAN0
 Rx Data , __CAN0 Rx Ready , __CAN0 Tx Data
 Frame , __CAN0 Tx Ready , __CAN0 Bit
 Timing , __CAN0 FPGA Is Running , __CAN0
 Start , __CAN0 FIFO Full, or __CAN0 FIFO
 Empty . If you intend to use multiple CAN 985x modules on your FPGA, you
 need to duplicate and rename all controls and indicators accordingly.
- Do not modify the CAN read and write code except to filter CAN IDs on the receiving side to minimize the amount of CAN data transfers to the host.
- As you create controls or indicators, ensure that each control name is unique within the VI.

Refer to the LabVIEW FPGA Module documentation for more information about creating FPGA VIs and
 bitfiles for an FPGA target.

When using ADCS on CompactRIO with an NI 985x C Series module, the interface name is based on the
 bitfile you use and the interface name you set. For example,
 MyInterface@MyBitfile.lvbitx,
 CAN@lvbitfile.lvbitx, or CAN0@mybitfile.lvbitx.

The interface name you use must be part of all parameters in the FPGA code for the CAN
 communication. Also, the ADCS needs the interface name for correct functionality.

If you define the interface name to be CAN0, you must name the parameters as
 follows:

- __CAN0 Rx Data
- __CAN0 Rx Ready
- __CAN0 Tx Data Frame
- __CAN0 Tx Ready
- __CAN0 Bit Timing
- __CAN0 FPGA Is Running
- __CAN0 Start
- __CAN0 FIFO Full
- __CAN0 FIFO Ready

In addition, you need to set the name of the internally used FIFO to __CAN0 FIFO
 (the FIFO is set to U32, 1029 elements, target scoped, and block memory).

After recompiling your FPGA VI, copy the bitfile to the root directory of your CompactRIO
 controller and specify the bitfile in the interface name. Or copy the file to any
 location on the CompactRIO controller and specify an absolute path or path relative to
 the root for the bitfile.

If you are using an NI-XNET 986x C Series module on your CompactRIO target, you need to start an
 FPGA VI on the target before accessing the port with ADCS. Refer to the Getting
 Started with CompactRIO section in the NI-XNET Hardware and
 Software Help for more information about compiling the FPGA VI. When the
 VI is running, you can access the NI 986x module as you would program on a Windows or
 PXI LabVIEW Real-Time target.

<!--NI_TOPIC bundle=automotive-diagnostic-command-set-toolkit path=automotive-diagnostic-command-set-api-structu.html language=enus -->
## TOPIC 00003: Automotive Diagnostic Command Set API Structure

- bundle_id: `automotive-diagnostic-command-set-toolkit`
- source_path: `automotive-diagnostic-command-set-api-structu.html`
- source_url: https://docs-be.ni.com/bundle/automotive-diagnostic-command-set-toolkit/raw/resource/enus/automotive-diagnostic-command-set-api-structu.html
- document_id: `automotive-diagnostic-command-set-toolkit`
- page_type: `leaf`
- content_type: `concept`
- source_description: The top two layer routines are available as API functions. Each diagnostic service for KWP2000, UDS, and OBD is available as one routine. Also available on the top level are auxiliary routines for converting scaled physical data values to and from their binary representations used in the diagnostic

### Automotive Diagnostic Command Set API Structure

The top two layer routines are available as API functions. Each diagnostic service for KWP2000,
 UDS, and OBD is available as one routine. Also available on the top level are auxiliary
 routines for converting scaled physical data values to and from their binary
 representations used in the diagnostic services.

On the second layer are more general routines for opening and closing diagnostic communication
 channels and executing a diagnostic service. Auxiliary routines create the diagnostic
 identifiers from the logical ECU address.

<!--NI_TOPIC bundle=automotive-diagnostic-command-set-toolkit path=available-diagnostic-services.html language=enus -->
## TOPIC 00004: Available Diagnostic Services

- bundle_id: `automotive-diagnostic-command-set-toolkit`
- source_path: `available-diagnostic-services.html`
- source_url: https://docs-be.ni.com/bundle/automotive-diagnostic-command-set-toolkit/raw/resource/enus/available-diagnostic-services.html
- document_id: `automotive-diagnostic-command-set-toolkit`
- page_type: `leaf`
- content_type: `concept`
- source_description: The standards on automotive diagnostic define many different services for many purposes. Unfortunately, most services leave a large amount of room for manufacturer-specific variants and extensions. NI has implemented the most used variants while trying not to overload them with optional parameters.H

### Available Diagnostic Services

The standards on automotive diagnostic define many different services for many purposes.
 Unfortunately, most services leave a large amount of room for manufacturer-specific
 variants and extensions. NI has implemented the most used variants while trying not to
 overload them with optional parameters.

However, all services are implemented in LabVIEW and open to the user. If you are missing a
 service or variant of an existing service, you can easily add or modify it on your
 own.

In the C API, you can also implement your own diagnostic services using the
 ndDiagnosticService routine. However, the templates from the
 existing services are not available.

<!--NI_TOPIC bundle=automotive-diagnostic-command-set-toolkit path=choosing-the-programming-language.html language=enus -->
## TOPIC 00005: Choosing the Programming Language

- bundle_id: `automotive-diagnostic-command-set-toolkit`
- source_path: `choosing-the-programming-language.html`
- source_url: https://docs-be.ni.com/bundle/automotive-diagnostic-command-set-toolkit/raw/resource/enus/choosing-the-programming-language.html
- document_id: `automotive-diagnostic-command-set-toolkit`
- page_type: `leaf`
- content_type: `concept`
- source_description: The programming language you use for application development determines how to access the Automotive Diagnostic Command Set APIs.

### Choosing the Programming Language

The programming language you use for application development determines how to access the
 Automotive Diagnostic Command Set APIs.

Related concepts:

- LabVIEW
- LabWindows/CVI
- Visual C++ 6
- Other Programming Languages

<!--NI_TOPIC bundle=automotive-diagnostic-command-set-toolkit path=general-programming-model.html language=enus -->
## TOPIC 00006: General Programming Model

- bundle_id: `automotive-diagnostic-command-set-toolkit`
- source_path: `general-programming-model.html`
- source_url: https://docs-be.ni.com/bundle/automotive-diagnostic-command-set-toolkit/raw/resource/enus/general-programming-model.html
- document_id: `automotive-diagnostic-command-set-toolkit`
- page_type: `leaf`
- content_type: `concept`
- source_description: First, you must open a diagnostic communication link. This involves initializing the CAN/LIN port and defining communication parameters such as the baud rate. For CAN-based diagnostics, the CAN identifiers on which the diagnostic communication takes place must be defined also. No actual communicatio

### General Programming Model

[IMAGE alt='image' src='GUID-77F98523-A645-4CB6-BD84-06EE2B07EC9B-a5.gif']

First, you must open a diagnostic communication link. This involves initializing the CAN/LIN port
 and defining communication parameters such as the baud rate. For CAN-based diagnostics,
 the CAN identifiers on which the diagnostic communication takes place must be defined
 also. No actual communication to the ECU takes place at this stage.

For the VW TP 2.0, you then must establish a communication channel to the ECU using the VWTP
 Connect routine. The communication channel properties are negotiated between the host
 and ECU.

After these steps, the diagnostic communication is established, and you can execute diagnostic
 services of your choice. Note that for the VW TP 2.0, you must execute the VWTP
 ConnectionTest routine periodically (once per second) to keep the communication channel
 open.

When you finish your diagnostic services, you must close the diagnostic communication link. This
 finally closes the CAN or LIN port. For the VW TP 2.0, you should disconnect the
 communication channel established before closing.

<!--NI_TOPIC bundle=automotive-diagnostic-command-set-toolkit path=labview-real-time-rt-configuration.html language=enus -->
## TOPIC 00007: LabVIEW Real-Time (RT) Configuration

- bundle_id: `automotive-diagnostic-command-set-toolkit`
- source_path: `labview-real-time-rt-configuration.html`
- source_url: https://docs-be.ni.com/bundle/automotive-diagnostic-command-set-toolkit/raw/resource/enus/labview-real-time-rt-configuration.html
- document_id: `automotive-diagnostic-command-set-toolkit`
- page_type: `leaf`
- content_type: `concept`
- source_description: LabVIEW Real-Time (RT) combines easy-to-use LabVIEW programming with the power of real-time systems. When you use an NI PXI controller as a LabVIEW RT system, you can install a PXI CAN card and use the NI-CAN APIs to develop real-time applications. As with any NI software library for LabVIEW RT, you

### LabVIEW Real-Time (RT) Configuration

LabVIEW Real-Time (RT) combines easy-to-use LabVIEW programming with the power of real-time
 systems. When you use an NI PXI controller as a LabVIEW RT system, you can install a PXI
 CAN card and use the NI-CAN APIs to develop real-time applications. As with any NI
 software library for LabVIEW RT, you must install the Automotive Diagnostic Command Set
 software to the LabVIEW RT target using the Remote Systems branch in MAX. For more
 information, refer to the LabVIEW RT documentation.

After you install the PXI CAN cards and download the Automotive Diagnostic Command Set software
 to the LabVIEW RT system, you must verify the installation.

Related concepts:

- Activating Your Software

<!--NI_TOPIC bundle=automotive-diagnostic-command-set-toolkit path=labview.html language=enus -->
## TOPIC 00008: LabVIEW

- bundle_id: `automotive-diagnostic-command-set-toolkit`
- source_path: `labview.html`
- source_url: https://docs-be.ni.com/bundle/automotive-diagnostic-command-set-toolkit/raw/resource/enus/labview.html
- document_id: `automotive-diagnostic-command-set-toolkit`
- page_type: `leaf`
- content_type: `concept`
- source_description: Automotive Diagnostic Command Set functions and controls are in the LabVIEW palettes. In LabVIEW, the Automotive Diagnostic Command Set palette is in the Addons palette.The Automotive Diagnostic Command Set API for LabVIEW section of this help describes each LabVIEW VI for the Automotive Diagnostic

### LabVIEW

Automotive Diagnostic Command Set functions and controls are in the LabVIEW palettes. In LabVIEW,
 the Automotive Diagnostic Command Set palette is in the Addons palette.

The *Automotive Diagnostic Command Set API for LabVIEW* section of this help describes
 each LabVIEW VI for the Automotive Diagnostic Command Set API.

To access the VI reference from within LabVIEW, press <Ctrl-H> to open
 the Help window, click the appropriate Automotive Diagnostic Command Set VI, and follow
 the link. The Automotive Diagnostic Command Set software includes a full set of LabVIEW
 examples. These examples teach programming basics as well as advanced topics. The
 example help describes each example and includes a link you can use to open the VI.

Parent topic:

Choosing the Programming Language

<!--NI_TOPIC bundle=automotive-diagnostic-command-set-toolkit path=labwindows-cvi.html language=enus -->
## TOPIC 00009: LabWindows/CVI

- bundle_id: `automotive-diagnostic-command-set-toolkit`
- source_path: `labwindows-cvi.html`
- source_url: https://docs-be.ni.com/bundle/automotive-diagnostic-command-set-toolkit/raw/resource/enus/labwindows-cvi.html
- document_id: `automotive-diagnostic-command-set-toolkit`
- page_type: `leaf`
- content_type: `concept`
- source_description: Within LabWindows/CVI, the Automotive Diagnostic Command Set function panel is in Libraries»Automotive Diagnostic Command Set. As with other LabWindows/CVI function panels, the Automotive Diagnostic Command Set function panel provides help for each function and the ability to generate code. The Auto

### LabWindows/CVI

Within LabWindows/CVI, the Automotive Diagnostic Command Set function panel is in
 Libraries»Automotive Diagnostic Command Set. As with other
 LabWindows/CVI function panels, the Automotive Diagnostic Command Set function panel
 provides help for each function and the ability to generate code. The *Automotive
 Diagnostic Command Set API for C* section of this help describes each
 Automotive Diagnostic Command Set API function. You can access the reference for each
 function directly from within the function panel. The Automotive Diagnostic Command Set
 API header file is nidiagcs.h. The Automotive Diagnostic Command Set
 API library is nidiagcs.lib. The toolkit software includes a full set
 of LabWindows/CVI examples. The examples are in the LabWindows/CVI
 \samples\Automotive Diagnostic Command Set directory. Each
 example includes a complete LabWindows/CVI project (.prj file). The
 example description is in comments at the top of the .c file.

Parent topic:

Choosing the Programming Language

<!--NI_TOPIC bundle=automotive-diagnostic-command-set-toolkit path=other-programming-languages.html language=enus -->
## TOPIC 00010: Other Programming Languages

- bundle_id: `automotive-diagnostic-command-set-toolkit`
- source_path: `other-programming-languages.html`
- source_url: https://docs-be.ni.com/bundle/automotive-diagnostic-command-set-toolkit/raw/resource/enus/other-programming-languages.html
- document_id: `automotive-diagnostic-command-set-toolkit`
- page_type: `leaf`
- content_type: `concept`
- source_description: The Automotive Diagnostic Command Set software does not provide formal support for programming languages other than those described in the preceding sections. If the programming language includes a mechanism to call a Dynamic Link Library (DLL), you can create code to call Automotive Diagnostic Comm

### Other Programming Languages

The Automotive Diagnostic Command Set software does not provide formal support for programming
 languages other than those described in the preceding sections. If the programming
 language includes a mechanism to call a Dynamic Link Library (DLL), you can create code
 to call Automotive Diagnostic Command Set functions. All functions for the Automotive
 Diagnostic Command Set API are in nidiagcs.dll. If the programming
 language supports the Microsoft Win32 APIs, you can load pointers to Automotive
 Diagnostic Command Set functions in the application. The following section describes how
 to use the Win32 functions for C/C++ environments other than Visual C/C++ 6. For more
 detailed information, refer to Microsoft documentation.

The following C language code fragment shows how to call Win32 LoadLibrary to
 load the Automotive Diagnostic Command Set API DLL:

#include <windows.h> #include "nidiagcs.h" HINSTANCE NiDiagCSLib = NULL; NiMcLib =
 LoadLibrary("nidiagcs.dll");

Next, the application must call the Win32 GetProcAddress function to obtain a
 pointer to each Automotive Diagnostic Command Set function the application uses. For
 each function, you must declare a pointer variable using the prototype of the function.
 For the Automotive Diagnostic Command Set function prototypes, refer to the
 *Automotive Diagnostic Command Set API for C* section of this help.
 Before exiting the application, you must unload the Automotive Diagnostic Command Set
 DLL as follows:

FreeLibrary (NiDiagCSLib);

Parent topic:

Choosing the Programming Language

<!--NI_TOPIC bundle=automotive-diagnostic-command-set-toolkit path=overview.html language=enus -->
## TOPIC 00011: Automotive Diagnostic Command Set Toolkit Overview

- bundle_id: `automotive-diagnostic-command-set-toolkit`
- source_path: `overview.html`
- source_url: https://docs-be.ni.com/bundle/automotive-diagnostic-command-set-toolkit/raw/resource/enus/overview.html
- document_id: `automotive-diagnostic-command-set-toolkit`
- page_type: `leaf`
- content_type: `concept`
- source_description: This help provides instructions for using the Automotive Diagnostic Command Set Toolkit and contains information about installation, configuration, and troubleshooting. It also includes the Automotive Diagnostic Command Set Toolkit LabVIEW and C API reference. Diagnostics involve remote execution of

### Automotive Diagnostic Command Set
 Toolkit
 Overview

This help provides instructions for using the Automotive Diagnostic Command Set Toolkit
 and contains information about installation, configuration, and troubleshooting. It also
 includes the Automotive Diagnostic Command Set Toolkit LabVIEW and C API reference.

Diagnostics involve remote execution of routines, or services, on ECUs. To execute a
 routine, you send a byte string as a request to an ECU, and the ECU usually answers with
 a response byte string. Several diagnostic protocols such as KWP2000 and UDS standardize
 the format of the services to be executed, but those standards leave a large amount of
 room for manufacturer-specific extensions. A newer trend is the emission-related
 legislated OnBoard Diagnostics (OBD), which is manufacturer independent and standardized
 in SAE J1979 and ISO 15031-5. This standard adds another set of services that follow the
 same scheme.

Because diagnostics were traditionally executed on serial communication links, the byte
 string length is not limited. For newer, CAN, LIN, or Ethernet-based diagnostics, this
 involves using a transport protocol that segments the arbitrarily long byte strings into
 pieces that can be transferred over the CAN or LIN bus, and reassembles them on the
 receiver side. Several transport protocols accomplish this task. The Automotive
 Diagnostic Command Set implements the ISO TP (standardized in ISO 15765-2) for CAN and
 LIN-based diagnostics, the manufacturer-specific VW TP 2.0 for CAN-based diagnostics,
 and the Diagnostics on IP (DoIP) transport protocol (standardized as ISO 13400) for
 Ethernet-based diagnostics.

Note

<!--NI_TOPIC bundle=automotive-diagnostic-command-set-toolkit path=structure-of-the-automotive-diagnostic-comman.html language=enus -->
## TOPIC 00012: Structure of the Automotive Diagnostic Command Set

- bundle_id: `automotive-diagnostic-command-set-toolkit`
- source_path: `structure-of-the-automotive-diagnostic-comman.html`
- source_url: https://docs-be.ni.com/bundle/automotive-diagnostic-command-set-toolkit/raw/resource/enus/structure-of-the-automotive-diagnostic-comman.html
- document_id: `automotive-diagnostic-command-set-toolkit`
- page_type: `leaf`
- content_type: `concept`
- source_description: The Automotive Diagnostic Command Set is structured into three layers of functionality:The top layer implements three sets of diagnostic services for the diagnostic protocols KWP2000, UDS (DiagOnCAN), and OBD (On-Board Diagnostics). The second layer implements general routines involving opening and

### Structure of the Automotive Diagnostic Command Set

[IMAGE alt='image' src='GUID-65F59451-B1CE-4B79-895D-B8AB0E84F250-a5.gif']

The Automotive Diagnostic Command Set is structured into three layers of functionality:

- The top layer implements three sets of diagnostic services for the diagnostic protocols KWP2000, UDS (DiagOnCAN), and OBD (On-Board Diagnostics).
- The second layer implements general routines involving opening and closing diagnostic communication connections, connecting and disconnecting to/from an ECU, and executing a diagnostic service on byte level. The latter routine is the one the top layer uses heavily.
- The third layer implements the transport protocols needed for diagnostic communication to an ECU. The second layer uses these routines to communicate to an ECU.

All three top layers are fully implemented in LabVIEW.

The transport protocols then execute CAN/LIN Read/Write operations through a specialized DLL for
 streamlining the CAN/LIN data flow, especially in higher busload situations.

<!--NI_TOPIC bundle=automotive-diagnostic-command-set-toolkit path=tweaking-the-transport-protocol.html language=enus -->
## TOPIC 00013: Tweaking the Transport Protocol

- bundle_id: `automotive-diagnostic-command-set-toolkit`
- source_path: `tweaking-the-transport-protocol.html`
- source_url: https://docs-be.ni.com/bundle/automotive-diagnostic-command-set-toolkit/raw/resource/enus/tweaking-the-transport-protocol.html
- document_id: `automotive-diagnostic-command-set-toolkit`
- page_type: `leaf`
- content_type: `concept`
- source_description: A set of global constants controls transport protocol behavior. These constants default to maximum performance. To check the properties of an implementation of a transport protocol in an ECU, for example, you may want to change the constants to nonstandard values using the Get/Set Property routines.

### Tweaking the Transport Protocol

A set of global constants controls transport protocol behavior. These constants default to
 maximum performance. To check the properties of an implementation of a transport
 protocol in an ECU, for example, you may want to change the constants to nonstandard
 values using the Get/Set Property routines.

<!--NI_TOPIC bundle=automotive-diagnostic-command-set-toolkit path=user-manual-welcome.html language=enus -->
## TOPIC 00014: Automotive Diagnostic Command Set Toolkit User Manual

- bundle_id: `automotive-diagnostic-command-set-toolkit`
- source_path: `user-manual-welcome.html`
- source_url: https://docs-be.ni.com/bundle/automotive-diagnostic-command-set-toolkit/raw/resource/enus/user-manual-welcome.html
- document_id: `automotive-diagnostic-command-set-toolkit`
- page_type: `leaf`
- content_type: `concept`
- source_description: The Automotive Diagnostic Command Set Toolkit User Manual provides detailed descriptions of the product functionality and the step by step processes for use. Looking for Something Else?For information not found in the User Manual for your product, such as specifications and API reference, browse Rel

### Automotive Diagnostic Command Set
 Toolkit
 User Manual

The Automotive Diagnostic Command Set
 Toolkit User Manual provides detailed
 descriptions of the product functionality and the step by step processes for use.

#### Looking for Something Else?

For information not found in the User Manual
 for your product, such as specifications and API reference, browse *Related
 Information*.

Related information:

- Automotive Diagnostic Command Set Toolkit
 LabVIEW API Reference
- Automotive Diagnostic Command Set Toolkit
 C API Reference
- Hardware and Software Operating System
 Compatibility
- License Setup and Activation

<!--NI_TOPIC bundle=automotive-diagnostic-command-set-toolkit path=using-an-xnet-ip-stack.html language=enus -->
## TOPIC 00015: Using an XNET IP Stack

- bundle_id: `automotive-diagnostic-command-set-toolkit`
- source_path: `using-an-xnet-ip-stack.html`
- source_url: https://docs-be.ni.com/bundle/automotive-diagnostic-command-set-toolkit/raw/resource/enus/using-an-xnet-ip-stack.html
- document_id: `automotive-diagnostic-command-set-toolkit`
- page_type: `leaf`
- content_type: `concept`
- source_description: Each ADCS DoIP session can use either the native operating system IP stack or an XNET IP Stack, and parallel ADCS sessions can use any combination of IP stacks and virtual interfaces.By default, DoIP sessions use the operating system IP stack. To use an XNET IP Stack, set the XNET IP stack name para

### Using an XNET IP Stack

Each ADCS DoIP session can use either the native operating system IP stack or an XNET IP Stack,
 and parallel ADCS sessions can use any combination of IP stacks and virtual
 interfaces.

By default, DoIP sessions use the operating system IP stack. To use an XNET IP Stack, set the
 XNET IP stack name parameter of *Open Diagnostic On
 IP.vi* (or the xnetStackName parameter of
 *ndOpenDiagnosticOnIPStack*) to a valid name of an XNET IP Stack.

ADCS obtains a reference to the selected XNET IP Stack. After communication is complete, the
 function *Close Diagnostic.vi* or *ndCloseDiagnostic* must be used
 to free that reference in all cases.

An XNET IP Stack allows the configuration of an NI-XNET network interface independent from other
 network interfaces in the system and provides advanced features such as virtual
 interfaces and VLANs. The XNET IP Stack must be created beforehand using the NI-XNET
 API. Refer to NI-XNET Hardware and Software Help and NI-XNET examples
 for information about configuring, creating, and clearing an XNET IP Stack.

<!--NI_TOPIC bundle=automotive-diagnostic-command-set-toolkit path=visual-c-6.html language=enus -->
## TOPIC 00016: Visual C++ 6

- bundle_id: `automotive-diagnostic-command-set-toolkit`
- source_path: `visual-c-6.html`
- source_url: https://docs-be.ni.com/bundle/automotive-diagnostic-command-set-toolkit/raw/resource/enus/visual-c-6.html
- document_id: `automotive-diagnostic-command-set-toolkit`
- page_type: `leaf`
- content_type: `concept`
- source_description: The Automotive Diagnostic Command Set software supports Microsoft Visual C/C++ 6.The header file for Visual C/C++ 6 is in the Program Files\National Instruments\Shared\ExternalCompilerSupport\C\include folder. To use the Automotive Diagnostic Command Set API, include the nidiagcs.h header file in th

### Visual C++ 6

The Automotive Diagnostic Command Set software supports Microsoft Visual C/C++ 6.

The header file for Visual C/C++ 6 is in the Program Files\National
 Instruments\Shared\ExternalCompilerSupport\C\include folder. To use the
 Automotive Diagnostic Command Set API, include the nidiagcs.h header
 file in the code, then link with the nidiagcs.lib library file. The
 library file is in the Program Files\National
 Instruments\Shared\ExternalCompilerSupport\C\lib32\msvc folder.

For C applications (files with a .c extension), include the header file by
 adding a #include to the beginning of the code, as follows:

#include "nidiagcs.h"

For C++ applications (files with a .cpp extension), define
 __cplusplus before including the header, as follows:

#define __cplusplus

#include "nidiagcs.h"

The __cplusplus define enables the transition from C++ to the C language
 functions.

The *Automotive Diagnostic Command Set API for C* section of this help describes each
 function.

On Windows Vista (with Standard User Account), the typical path to the C examples folder is
 \Users\Public\Documents\National Instruments\Automotive Diagnostic Command
 Set\Examples\MS Visual C.

On Windows XP/2000, the typical path to the C examples folder is \Documents and
 Settings\All Users\Documents\National Instruments\Automotive Diagnostic Command
 Set\Examples\MS Visual C.

Each example is in a separate folder. The example description is in comments at the top of the
 .c file. At the command prompt, after setting MSVC environment
 variables (such as with MS vcvars32.bat), you can build each example
 using a command such as:

cl /I<HDir> GetDTCs.c <LibDir>\nidiagcs.lib

<HDir> is the folder where nidiagcs.h can be
 found.

<LibDir> is the folder where nidiagcs.lib can be
 found.

Parent topic:

Choosing the Programming Language
