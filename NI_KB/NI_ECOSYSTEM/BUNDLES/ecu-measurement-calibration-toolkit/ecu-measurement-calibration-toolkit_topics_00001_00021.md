# NI DOCUMENT BUNDLE: ecu-measurement-calibration-toolkit

<!--NI_BUNDLE_CHUNK bundle=ecu-measurement-calibration-toolkit start=1 end=21 -->
<!--NI_TOPIC bundle=ecu-measurement-calibration-toolkit path=application-development-on-compactrio-or-r-se.html language=enus -->
## TOPIC 00001: Application Development on CompactRIO or R Series Using an NI 985x or NI 986x C Series Module

- bundle_id: `ecu-measurement-calibration-toolkit`
- source_path: `application-development-on-compactrio-or-r-se.html`
- source_url: https://docs-be.ni.com/bundle/ecu-measurement-calibration-toolkit/raw/resource/enus/application-development-on-compactrio-or-r-se.html
- document_id: `ecu-measurement-calibration-toolkit`
- page_type: `leaf`
- content_type: `concept`
- source_description: To run a project on an FPGA target with an NI 985x C Series module, you need an FPGA bitfile (.lvbitx). The FPGA bitfile is downloaded to the FPGA target on the execution host. A bitfile is a compiled version of an FPGA VI. FPGA VIs, and thus bitfiles, define the CAN, analog, digital, and pulse widt

### Application Development on CompactRIO or R Series Using an NI 985x or NI 986x C Series
 Module

To run a project on an FPGA target with an
 NI 985x C Series module, you need an FPGA bitfile
 (.lvbitx). The FPGA bitfile is downloaded to the FPGA target on the
 execution host. A bitfile is a compiled version of an FPGA VI. FPGA VIs, and thus
 bitfiles, define the CAN, analog, digital, and pulse width modulation (PWM) inputs and
 outputs of an FPGA target. The ECU M&C Toolkit includes FPGA bitfiles for several
 FPGA targets. If your target is not included in the examples, you can use the examples
 as a template and adjust them based on your installed FPGA target.

The default bitfiles are sufficient for a basic ECU M&C application. However, in some
 situations you may need to modify the existing FPGA code or create a custom bitfile. For
 example, to use additional I/O on the FPGA target, you must add these I/O to the FPGA
 VI. You must install the LabVIEW FPGA Module to create these files.

Modify the FPGA VI according to the following guidelines:

- Do not modify, remove, or rename any block diagram controls and indicators named
 __CAN0 Rx Data, __CAN0 Rx Ready, __CAN0 Tx Data Frame, __CAN0 Tx Ready, __CAN0 Bit
 Timing, __CAN0 FPGA Is Running, __CAN0 Start, __CAN0 FIFO Full, or __CAN0 FIFO
 Empty. If you intend to use multiple CAN 985 x modules on your
 FPGA, you need to duplicate and rename all controls and indicators accordingly.
- Do not modify the CAN read and write code except to filter CAN IDs on the receiving
 side to minimize the amount of CAN data transfers to the host.
- As you create controls or indicators, ensure that each control name is unique within
 the VI.

Refer to the LabVIEW FPGA Module documentation for more information about creating FPGA
 VIs and bitfiles for an FPGA target.

When using the ECU M&C Toolkit on CompactRIO with an NI 985x C
 Series module, the interface name is based on the bitfile you use and the interface name
 you set. For example, MyInterface@MyBitfile.lvbitx,
 CAN@lvbitfile.lvbitx, or
 CAN0@mybitfile.lvbitx.

The interface name you use must be part of all parameters in the FPGA code for the CAN
 communication. Also, the ECU M&C Toolkit needs the interface name for correct
 functionality.

If you define the interface name to be *CAN0*, you must name the parameters as
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

In addition, you need to set the name of the internally used FIFO to *__CAN0
 FIFO* (the FIFO is set to U32, 1029 elements, target scoped, and block
 memory).

After recompiling your FPGA VI, copy the bitfile to the root directory of your CompactRIO
 controller and specify the bitfile in the interface name. Or copy the file to any
 location on the CompactRIO controller and specify an absolute path or path relative to
 the root for the bitfile.

If you are using an NI-XNET 986*x* C Series module on your CompactRIO target,
 you need to start an FPGA VI on the target before accessing the port with the ECU
 M&C Toolkit. Refer to the *Getting Started with CompactRIO* section in
 the *NI-XNET Hardware and Software Help* for more information about compiling
 the FPGA VI. When the VI is running, you can access the NI 986*x* module as
 you would program on a Windows or PXI LabVIEW Real-Time target.

<!--NI_TOPIC bundle=ecu-measurement-calibration-toolkit path=can-calibration-protocol-ccp-overview.html language=enus -->
## TOPIC 00002: CAN Calibration Protocol (CCP) Overview

- bundle_id: `ecu-measurement-calibration-toolkit`
- source_path: `can-calibration-protocol-ccp-overview.html`
- source_url: https://docs-be.ni.com/bundle/ecu-measurement-calibration-toolkit/raw/resource/enus/can-calibration-protocol-ccp-overview.html
- document_id: `ecu-measurement-calibration-toolkit`
- page_type: `leaf`
- content_type: `concept`
- source_description: The CAN Calibration Protocol is a CAN-based master-slave protocol for calibration and data acquisition. A single master device (host) can be connected to one or more slave devices. Before a slave device may accept commands from the host, the host has to establish a logical point-to-point connection

### CAN Calibration Protocol (CCP) Overview

The CAN Calibration Protocol is a CAN-based master-slave protocol for calibration and
 data acquisition. A single master device (host) can be connected to one or more slave
 devices. Before a slave device may accept commands from the host, the host has to
 establish a logical point-to-point connection to the slave device. After this connection
 has been established, the slave device has to acknowledge each command received from the
 host within a specified time.

CCP defines two function sets—one for control/memory transfer, and one for data
 acquisitions that are independent of each other and may run asynchronously. The control
 commands are used to carry out functions in the slave device, and may use the slave to
 perform tasks on other devices. The data acquisition commands are used for continuous
 data acquisition from a slave device. The devices continuously transmit internal data
 according to a list that has been configured by the host. Data acquisition is initiated
 by the host, then executed by the slave device, and may be based on a fixed sampling
 rate or be event-driven.

The communication of controllers with a master device through CCP is based on the CAN
 2.0B standard (11-bit and 29-bit identifier), which includes 2.0A (11-bit identifier)
 for data acquisition from the controllers, memory transfers to the controllers, and
 control functions in the controllers for calibration.

The ECU M&C Toolkit abstracts the CCP communication layer so that it is transparent
 to the user. For most cases it is sufficient that the underlying CCP communication is
 handled by the toolkit kernel itself. Nevertheless, the ECU M&C Toolkit offers
 direct access to the low level CCP commands if a non-standard timing behavior or
 independent user defined command sequence is needed.

#### CCP Protocol Version

The ECU M&C Toolkit supports the CAN
 Calibration Protocol specification, version 2.1.

<!--NI_TOPIC bundle=ecu-measurement-calibration-toolkit path=choose-the-programming-language.html language=enus -->
## TOPIC 00003: Choose the Programming Language

- bundle_id: `ecu-measurement-calibration-toolkit`
- source_path: `choose-the-programming-language.html`
- source_url: https://docs-be.ni.com/bundle/ecu-measurement-calibration-toolkit/raw/resource/enus/choose-the-programming-language.html
- document_id: `ecu-measurement-calibration-toolkit`
- page_type: `leaf`
- content_type: `concept`
- source_description: The programming language you use for application development determines how to access the ECU M&C APIs. LabVIEWECU M&C Toolkit functions and controls are available in the LabVIEW palettes. In LabVIEW, the ECU M&C Toolkit palette is located: Within the All Functions palette for LabVIEW 7.1 Within the

### Choose the Programming Language

The programming language you use for application development determines how to access the
 ECU M&C APIs.

#### LabVIEW

ECU M&C Toolkit functions and controls are available
 in the LabVIEW palettes. In LabVIEW, the ECU M&C Toolkit
 palette is located:

- Within the All Functions palette for LabVIEW 7.1
- Within the Addons palette for LabVIEW 8.0 and 8.1

The reference for each ECU M&C Toolkit API function is in a separate topic
 identified by the VI name. To access the reference for a function from within
 LabVIEW, press Ctrl-H to open the Help window, click the
 appropriate ECU M&C function, and then follow the link. The ECU M&C Toolkit
 software includes a full set of examples for LabVIEW. These examples teach
 programming basics as well as advanced topics. The example help describes each
 example and includes a link you can use to open the VI.

#### LabWindows/CVI

Within LabWindows/CVI™,
 the ECU M&C Toolkit function panel is in Libraries»ECU Measurement
 and Calibration Toolkit. Like other LabWindows/CVI function panels,
 the ECU M&C Toolkit function panel provides help for each function and the
 ability to generate code. The reference for each API function is located in a
 separate topic identified by the function name. You can access the reference for
 each function directly from within the function panel. The header file for the ECU
 M&C APIs is niemc.h. The library for the ECU M&C APIs is
 niemcc.lib. The toolkit software includes a full set of
 examples for LabWindows/CVI. The examples are installed in the LabWindows/CVI
 directory under samples\ecumc. Each example provides a complete
 LabWindows/CVI project (.prj file).

A description of each
 example is provided in comments at the top of the .c
 file.

#### Visual C++ 6

The ECU M&C Toolkit
 software supports Microsoft Visual C/C++ 6. The header file for Visual C/C++ 6 is in
 the Program Files\National
 Instruments\Shared\ExternalCompilerSupport\C\include folder.

To
 use the ECU M&C API, include the niemc.h header file in the
 code, then link with the niemcc.lib library file.

The
 niemcc.lib library file is in the Program
 Files\National Instruments\Shared\ExternalCompilerSupport\C\lib32\msvc
 folder.

For C applications (files with a .c extension),
 include the header file by adding a #include to the beginning of
 the code, like this:

#include "niemc.h"

For C++ applications (files with a .cpp extension), define
 __cplusplus before including the header, like this:

#define __cplusplus

#include "niemc.h"

The __cplusplus define enables the transition from C++ to the C
 language functions.

The reference for each API function is in the C function
 topic identified by the function name.

On Windows Vista (with Standard User
 Account), the typical path to the C examples folder is
 \Users\Public\Documents\National Instruments\ECU Measurement and
 Calibration Toolkit\Examples\MS Visual C.

On Windows XP/2000, the
 typical path to the C examples folder is \Documents and Settings\All
 Users\Documents\National Instruments\ECU Measurement and Calibration
 Toolkit\Examples\MS Visual C.

Each example is in a separate
 folder. A description of each example is in comments at the top of the
 .c file. At the command prompt, after setting MSVC environment
 variables (such as with MS vcvars32.bat), you can build each
 example using a command such as:

cl /I<HDir> measure.c
 <LibDir>\niemcc.lib

<HDir> is the folder where niemc.h can be
 found.

<LibDir> is the folder where niemcc.lib can be
 found.

#### Other Programming Languages

The ECU
 M&C Toolkit software does not provide formal support for programming languages
 other than those described in the preceding sections. If the programming language
 provides a mechanism to call a Dynamic Link Library (DLL), you can create code to
 call ECU M&C API functions. All functions for the ECU M&C API are located in
 niemcc.dll. If the programming language supports the Microsoft
 Win32 APIs, you can load pointers to ECU M&C Toolkit functions in the
 application. The following text demonstrates use of the Win32 functions for C/C++
 environments other than Visual C/C++ 6. For more detailed information, refer to
 Microsoft documentation.

The following C language code fragment illustrates
 how to call Win32 LoadLibrary to load the DLL for the ECU M&C
 API:

#include <windows.h>

#include "niemc.h"

HINSTANCE NiMcLib = NULL;

NiMcLib = LoadLibrary("niemcc.dll");

Next, the application must call the Win32 GetProcAddress
 function to obtain a pointer to each ECU M&C Toolkit function that the
 application will use. For each function, you must declare a pointer variable using
 the prototype of the function. For the prototypes of each ECU M&C Toolkit
 function, refer to the C function topic identified by the function
 name.

Before exiting the application, you must unload the ECU M&C Toolkit
 DLL as follows:

FreeLibrary (NiMcLib);

<!--NI_TOPIC bundle=ecu-measurement-calibration-toolkit path=ecu-mc-api-basic-programming-model.html language=enus -->
## TOPIC 00004: ECU M&C API Basic Programming Model

- bundle_id: `ecu-measurement-calibration-toolkit`
- source_path: `ecu-mc-api-basic-programming-model.html`
- source_url: https://docs-be.ni.com/bundle/ecu-measurement-calibration-toolkit/raw/resource/enus/ecu-mc-api-basic-programming-model.html
- document_id: `ecu-measurement-calibration-toolkit`
- page_type: `leaf`
- content_type: `concept`
- source_description: The following figure illustrates the process to initiate communication to an ECU with the ECU M&C Channel functions. A description of each step in the decision process follows the flowchart. ECU OpenThe ECU Open function combines the opening of a selected ASAM MCD 2MC database file with the .A2L fil

### ECU M&C API Basic Programming Model

The following figure illustrates the process to initiate communication to an ECU with the
 ECU M&C Channel functions. A description of each step in the decision process
 follows the flowchart.

[IMAGE alt='image' src='GUID-25176726-016D-43E6-A889-F568173CF683-a5.svg']

#### ECU Open

The ECU Open function combines the
 opening of a selected ASAM MCD 2MC database file with the .A2L file
 extension and the selection of a stored ECU name. The required parameters are the
 ASAM MCD 2MC database path and filename, and the dedicated CAN interface if you are
 using XCP or CCP with CAN. The CAN interface is used for communication with the ECU.
 If you are using XCP with UDP or TCP, a port number and IP address or hostname must
 be defined in the A2L database.

The function to open and select an ECU is MC
 ECU Open.vi in LabVIEW or mcDatabaseOpen followed by
 mcECUSelect in C.

Note

#### ASAM
 MCD 2MC Communication Properties for XCP or CCP with CAN

If your ASAM MCD
 2MC database file already contains communication properties, you can directly open
 the communication to your selected ECU.

If the communication properties are
 not stored in the ASAM MCD 2MC file, the communication properties must be manually
 set. To establish communication through XCP or CCP with CAN, the target ECU slave
 should be addressed by setting the following properties.

- CRO ID : The Command Receive Object (CRO) ID is used to
 send commands and data from the host to the slave device.
- DTO ID : The Data Transmission Object (DTO) ID is used by
 the ECU to respond to CCP commands and to send data and status information to
 the CCP master.
- Station Address : CCP is based on the idea that several
 ECUs can share the same CAN Arbitration IDs for CCP communication. To avoid
 communication conflicts, CCP defines a Station Address 
 that has to be unique for all ECUs sharing the same CAN Arbitration IDs. Unless
 an ECU has been addressed by its Station Address , the ECU
 must not react to CCP commands sent by the CCP master.
- Baudrate : The baudrate property
 may be missing in an A2L database file and can be set explicitly within the
 application. This property provides the baud rate at which communication will
 occur, and applies to all tasks initialized with the interface. You can specify
 one of the predefined baud rates, or specify advanced baud rates which refer to
 the settings of the Bit Timing Register 0 (BTR0) and 1 (BTR1). For more
 information, refer to the Interface Properties dialog in
 MAX, or the NI-CAN Hardware and Software Manual . The baud rate
 is originally set within MAX.

#### ASAM
 MCD 2MC Communication Properties for XCP with UDP or TCP

If the XCP
 communication properties are not stored in the ASAM MCD 2MC file, the communication
 properties must be manually set. To establish communication through XCP with UDP or
 TCP the target ECU slave should be addressed by setting the following
 properties.

- IP Address or hostname : The IP address 
 refers to the identifier for a computer or device on a TCP/IP network. Networks
 using the TCP/IP protocol route messages based on the IP address of the
 destination. A hostname describes the unique name by which a device
 is known on a network. Hostnames are used by various naming systems: NIS, DNS,
 SMB, etc. Hostnames are high-level aliases which ultimately correlate to unique
 network hardware MAC addresses.
- Port number : In TCP/IP and UDP networks, a port is an
 end-point to a logical connection through which a client program specifies a
 server program on a computer in a network. Port numbers range from 0 to 65536,
 but only port numbers 0 to 1024 are reserved for privileged services and
 designated as well-known ports.

#### ECU Connect

The ECU
 Connect function establishes communication to the selected ECU
 through CCP using the CCP CONNECT command or through XCP using the CONNECT command.
 It establishes a logical connection to an ECU. Unless a slave device (ECU) is
 unconnected, it must not execute or respond to any command sent by the application.
 The only exception to this rule is the Test command, in which case the slave with
 the specified address may acknowledge the command. After a successful ECU
 Connect you can create a Measurement Task or read/write a
 Characteristic.

The function to open and select an ECU is MC ECU Connect.vi in
 LabVIEW and mcECUConnect in C.

#### ECU Disconnect

The ECU
 Disconnect function permanently disconnects the specified CCP slave
 and ends the measurement and calibration session. When the measurement and
 calibration session is terminated, all CCP DAQ lists for the device is stopped and
 cleared, and the protection masks of the device are set to their default
 values.

The function to disconnect an ECU is MC ECU Disconnect.vi in LabVIEW
 or mcECUDisconnect in C.

#### ECU Close

The MC ECU
 Close function deselects the ECU and closes the remaining database
 reference handle. MC ECU Close must always be the final ECU
 M&C function call. If you do not use MC ECU Close, the
 remaining task configurations can cause problems in the execution of subsequent ECU
 M&C applications.

The function to close an ECU is MC ECU Close.vi in
 LabVIEW. To deselect the ECU and close the database reference handle in C, call the
 function mcECUDeselect followed by
 mcDatabaseClose.

#### Characteristic Read and Write

##### Access Characteristics

To access the
 Characteristics of an ECU you must select and connect to the specified ECU through
 the procedure given above. The function to open and select an ECU is MC ECU Open.vi
 in LabVIEW, or mcDatabaseOpen followed by
 mcECUSelectEx in C. Once the ECU has been connected an ECU
 Reference handle (ECU ref out in LabVIEW,
 ECURefNum in C) must be acquired before any additional actions
 can be performed.

##### Characteristic Read

The application must
 call the Read Characteristic function to obtain scaled
 floating point samples. The application typically calls Read
 Characteristic on demand. Calling Read
 Characteristic in a loop can cause significant CAN network traffic,
 as Characteristics may contain large amounts of data.

The function to read 0-
 to 2-dimensional Characteristics is MC Characteristic Read.vi in LabVIEW or
 mcCharacteristicRead in C. The function to read single double values as
 Characteristics is MC Characteristic Read Single Value.vi in LabVIEW or
 mcCharacteristicReadSingleValue in C.

Before reading a
 Characteristic, it may be helpful to verify the dimension of the Characteristic
 based on the definition in the ASAM MCD 2MC database file. Depending on the
 dimension of the Characteristic, use the appropriate Read
 function for reading a double, a 1D array of doubles, or a 2D array of
 doubles.

The function to verify a dimension of a named Characteristic is MC
 Get Property.vi with the parameter Characteristic/Dimension
 in LabVIEW or mcGetProperty with the parameter
 mcPropChar_Dimension in C.

##### Characteristic Write

The application must
 call the Write Characteristic function to output scaled
 floating-point samples. The application typically calls Write
 Characteristic on demand. Calling Write
 Characteristic in a loop can cause significant network traffic, as
 Characteristics may contain large amounts of data.

The function to write a
 Characteristic is MC Characteristic Write.vi in LabVIEW or
 mcCharacteristicWrite in C.

Before writing a
 Characteristic, it may be helpful to verify the dimension of the Characteristic
 based on the definition in the ASAM MCD 2MC database file. Depending on the
 dimension of the Characteristic, use the appropriate Write
 function for writing a double, a 1D array of doubles, or a 2D array of
 doubles.

The function to verify a dimension of a named Characteristic is MC
 Get Property.vi with the parameter Characteristic/Dimension
 in LabVIEW or mcGetProperty with the parameter
 mcPropChar_Dimension in C.

#### Measurement Task

To create a Measurement task you need to select available Measurement signals from an
 ASAM MCD 2MC database file. Create a valid ECU Reference handle as described in the
 *Access Characteristics* section.

The following figure shows the process to perform an ECU Measurement task. A description
 of each step in the decision process follows the flowchart.

[IMAGE alt='image' src='GUID-84E7A15B-408E-4F9F-BE51-9CA3B467BD02-a5.svg']

##### DAQ Initialize

The DAQ
 Initialize function initializes a list of Measurement channels as a
 single Measurement task. The communication for that Measurement task is started by
 the first DAQ Read function. The DAQ
 Initialize function is MC DAQ Initialize.vi in LabVIEW or
 mcDAQInitialize in other languages.

The DAQ
 Initialize function uses the following input parameters:

Measurement list

ECU Reference handle

ECU Open

ECU Connect

Mode

SampleRate

DTO ID

##### DAQ Start Stop

The optional function
 DAQ Start Stop starts or stops the transmission of the
 DAQ lists for an ECU M&C Measurement task. If you do not specify MC DAQ Start
 Stop.vi before your first DAQ Read or DAQ
 Write function, MC DAQ Start Stop is implicitly performed by the
 first DAQ Read or DAQ Write call.
 After you start the transmission of the DAQ lists or STIM lists, you can no longer
 change the configuration of the Measurement task with Set
 Property. DAQ Start Stop is implicitly
 performed by DAQ Clear to stop the transmission of the DAQ
 lists.

The function to start a DAQ List is MC DAQ Start Stop.vi in LabVIEW or
 mcDAQStartStop in C.

##### DAQ Read

The application must call the
 DAQ Read function to obtain floating-point samples. The
 application typically calls DAQ Read in a loop until done.
 The Read function is MC DAQ Read.vi in LabVIEW (all types
 that don't end in Time & Dbl) or
 mcDAQRead in other languages.

The behavior of
 Read depends on the initialized sample rate and the
 selected mode.

sample rate = 0

DAQ Read returns a single sample from the most recent
 message(s) received from the network. One sample is returned for every channel in
 the DAQ Initialize list.

The following figure shows an
 example of DAQ Read with a sample rate = 0. *A*,
 *B*, and *C* represent messages for the initialized
 channels. *def* represents the default value 0. If no message is received
 after the start of the application, the default value 0 is returned along with a
 warning.

Figure 1.

[IMAGE alt='image' src='GUID-C64232A6-F145-4C4F-B7C0-E1A57D9E6EFC-a5.svg']

sample rate > 0

DAQ Read returns an array of samples for every channel in
 the DAQ Initialize list. Each time the clock ticks at the
 specified rate, a sample from the most recent message(s) is inserted into the
 arrays. In other words, the samples are repeated in the array at the specified rate
 until a new message is received. By using the same sample rate with NI-DAQ Analog
 Input channels or NI-DAQmx Analog Input channels, you can compare ECU DAQ and
 NI-DAQ/NI-DAQmx samples over time.

The following figure shows an example of
 DAQ Read with a sample rate > 0. *A*,
 *B*, and *C* represent messages for the initialized
 channels. *delta-t*represents the time between samples as specified by
 the sample rate. *def* represents the default value 0.

Figure 2.

[IMAGE alt='image' src='GUID-AA6A350F-BFC7-4EFF-800F-1E4833CE057B-a5.svg']

##### DAQ Write

If you are using XCP and the
 DAQ initialize mode is set to STIM list the application must
 call the DAQ Write function to output floating-point samples.
 The application typically calls DAQ Write in a loop until
 done. The DAQ Write function is MC DAQ
 Write.vi in LabVIEW or mcDAQWrite in other
 languages.

##### DAQ Clear

DAQ
 Clear must always be the final function called for a specific
 Measurement task. If you do not use DAQ Clear, the remaining
 Measurement task configuration can cause problems in the execution of subsequent ECU
 M&C applications. Because this function clears the Measurement task, the
 Measurement task reference is transferred into an ECU reference task handle. To
 change the properties of a running Measurement task, use DAQ Start
 Stop to stop the task, Set Property to change
 the desired DAQ property, then DAQ Start Stop to restart the
 Measurement task again.

The function to clear a DAQ list is MC DAQ Clear.vi in
 LabVIEW or mcDAQClear in C.

Related information:

- ECU M&C API for LabVIEW
- ECU M&C API for C

<!--NI_TOPIC bundle=ecu-measurement-calibration-toolkit path=ecu-mc-overview.html language=enus -->
## TOPIC 00005: ECU M&C Overview

- bundle_id: `ecu-measurement-calibration-toolkit`
- source_path: `ecu-mc-overview.html`
- source_url: https://docs-be.ni.com/bundle/ecu-measurement-calibration-toolkit/raw/resource/enus/ecu-mc-overview.html
- document_id: `ecu-measurement-calibration-toolkit`
- page_type: `leaf`
- content_type: `concept`
- source_description: The ECU Measurement and Calibration (ECU M&C) Toolkit contains a development system for electronic control units (ECU) based on existing ASAM standards. The function set of the ECU M&C Toolkit enables engineers to optimize and verify the functionality of electronic controller devices. Most ECUs inte

### ECU M&C Overview

The ECU Measurement and Calibration (ECU M&C) Toolkit contains a development system
 for electronic control units (ECU) based on existing ASAM standards. The function set of
 the ECU M&C Toolkit enables engineers to optimize and verify the functionality of
 electronic controller devices. Most ECUs interact with other ECUs, external sensors, and
 actuators in a Controller Area Network (CAN). During the development and verification
 phase of an ECU, engineers access the ECU for acquired data (Measurement), or to adjust
 parameters inside the ECU itself (calibration). Since the bandwidth and number of
 identifiers for a CAN network is limited, the Association for Standardization of
 Automation and Measuring Systems (ASAM e.V.) has specified the CAN Calibration Protocol
 (CCP), a protocol layer based on CAN to access the Measurement and calibration data in
 an ECU.

To build on the functionality of the CAN Calibration Protocol (CCP), ASAM defined the new
 protocol specification XCP (Universal Measurement and Calibration Protocol) which can be
 considered an improved and generalized version of CCP. The X
 represents the various transportation layers used by the members of the XCP protocol
 family—for instance, XCP on CAN, XCP on TCP/IP, XCP on UDP/IP, XCP on USB, etc.

The ECU M&C Toolkit is particularly suited to the automotive industry and their
 component suppliers. It provides a function set that can be used in the development or
 verification phase of an ECU. Access to the data inside an ECU takes place based on
 information stored in an ASAM MCD 2MC (*.A2L) database file provided by
 the ECU supplier. Selecting each signal by its name provides convenient access to the
 data inside an ECU. The ECU M&C Toolkit uses XCP and CCP as the fundamental
 communication protocols and to support ECU database (*.A2L) files. You
 can easily switch between the XCP and CCP protocol layers through software.

#### Measurement and Calibration Databases

The ASAP description file
 (ASAP2 or ASAM MCD 2MC) is used to describe the ECU internal memory configuration.
 An ASAM MCD 2MC description file with the file extension .A2L
 contains information and access location for the relevant data objects in the ECU,
 such as:

- Project relevant information
- ECU data structure
- Conversion procedures for representation in physical units
- Descriptions of the available Measurement channels inside the ECU
- Descriptions of the available Characteristics inside the ECU
- Descriptions of how to access the ECU over CAN

Use of the ECU M&C Toolkit requires an existing ASAM MCD 2MC database file.
 These files can be generated by various third-party utilities. A database editor for
 ASAM MCD 2MC databases is not part of the ECU M&C Toolkit.

#### ECU
 Measurements

The ECU M&C Toolkit gives the user access to ECU internal
 physical values defined by their names in the ASAM MCD 2MC database file. Based on
 this information, the ECU M&C Toolkit communicates through XCP or CCP to the
 ECU. A DAQ (data acquisition) list can be set up, which sends ECU internal data
 synchronously or asynchronously to the XCP or CCP master. The ECU M&C Toolkit
 provides a way to configure several Measurement channels into a single Measurement
 task. The term *task* refers to a list of measurements (channels) read or
 written together. A common use of the task concept is to read DAQ channels available
 on the ECU.

#### ECU
 Characteristics

ECU *Characteristics* are maps of ECU internal
 variables, which may be used as calibration information or set-point information.
 The ECU memory content of Characteristics can be read or even changed with the help
 of the ECU M&C Toolkit.

<!--NI_TOPIC bundle=ecu-measurement-calibration-toolkit path=extended-support-changes.html language=enus -->
## TOPIC 00006: Updates and Changes for ECU Measurement and Calibration Toolkit Extended Support Versions

- bundle_id: `ecu-measurement-calibration-toolkit`
- source_path: `extended-support-changes.html`
- source_url: https://docs-be.ni.com/bundle/ecu-measurement-calibration-toolkit/raw/resource/enus/extended-support-changes.html
- document_id: `ecu-measurement-calibration-toolkit`
- page_type: `leaf`
- content_type: `concept`
- source_description: Browse updates and changes made in ECU Measurement and Calibration Toolkit versions on extended support. If you cannot find changes for your version, it might be a more recent version, documented as a new feature. Or, your version might not have included user-facing updates. You can find more inform

### Updates and Changes for ECU Measurement and
 Calibration Toolkit Extended Support Versions

Browse updates and changes made in ECU Measurement and
 Calibration Toolkit versions
 on extended support.

Note

Release Notes

#### ECU Measurement and Calibration Toolkit 2022
 Q4 New Features and Changes

- Added support for LabVIEW 2022 Q3.

#### ECU Measurement and Calibration Toolkit 21.5
 New Features and Changes

- Added support for LabVIEW 2021.

#### ECU Measurement and Calibration Toolkit 20.7
 New Features and Changes

- Added support for XCP protocol on the NI-XNET IP Stack within VeriStand CCP/XCP Custom
 Device.
- Added support for VeriStand 2020 R4.

<!--NI_TOPIC bundle=ecu-measurement-calibration-toolkit path=generic-ccp-functions.html language=enus -->
## TOPIC 00007: Generic CCP Functions

- bundle_id: `ecu-measurement-calibration-toolkit`
- source_path: `generic-ccp-functions.html`
- source_url: https://docs-be.ni.com/bundle/ecu-measurement-calibration-toolkit/raw/resource/enus/generic-ccp-functions.html
- document_id: `ecu-measurement-calibration-toolkit`
- page_type: `leaf`
- content_type: `concept`
- source_description: The generic ECU M&C CCP functions provide direct access to the CCP commands on a very low programming level. For further information for the use and parameters of the CCP commands, refer to the CAN Calibration Protocol Specification, Version 2.1. The following table provides an overview of the CCP c

### Generic CCP Functions

The generic ECU M&C CCP functions provide direct access to the CCP commands on a very
 low programming level. For further information for the use and parameters of the CCP
 commands, refer to the *CAN Calibration Protocol Specification, Version 2.1*.
 The following table provides an overview of the CCP commands and their corresponding
 LabVIEW VIs or C functions.

| CCP Command | LabVIEW VI Name | C Function Name |
| --- | --- | --- |
| ACTION_SERVICE | MC CCP Action Service.vi | mcCCPActionService |
| BUILD_CHKSUM | MC Build Checksum.vi | mcBuildChecksum |
| CLEAR_MEMORY | MC Clear Memory.vi | mcClearMemory |
| DIAG_SERVICE | MC CCP Diag Service.vi | mcCCPDiagService |
| DNLOAD | MC Download.vi | mcDownload |
| GET_ACTIVE_CAL_PAGE | MC CCP Get Active Cal Page.vi | mcCCPGetActiveCalPage |
| GET_S_STATUS | MC CCP Get Session Status.vi | mcCCPGetSessionStatus |
| GET_CCP_VERSION | MC CCP Get Version.vi | mcCCPGetVersion |
| MOVE | MC CCP Move Memory.vi | mcCCPMoveMemory |
| PROGRAM | MC Program.vi | mcProgram |
| SELECT_CAL_PAGE | MC CCP Select Cal Page.vi | mcCCPSelectCalPage |
| SET_S_STATUS | MC CCP Set Session Status.vi | mcCCPSetSessionStatus |
| UPLOAD | MC Upload.vi | mcUpload |

Related information:

- ECU M&C API for LabVIEW
- ECU M&C API for C

<!--NI_TOPIC bundle=ecu-measurement-calibration-toolkit path=generic-xcp-functions.html language=enus -->
## TOPIC 00008: Generic XCP Functions

- bundle_id: `ecu-measurement-calibration-toolkit`
- source_path: `generic-xcp-functions.html`
- source_url: https://docs-be.ni.com/bundle/ecu-measurement-calibration-toolkit/raw/resource/enus/generic-xcp-functions.html
- document_id: `ecu-measurement-calibration-toolkit`
- page_type: `leaf`
- content_type: `concept`
- source_description: The generic ECU M&C XCP functions provide direct access to the XCP commands on a very low programming level. For more information about the use and parameters of the XCP commands, refer to the ASAM XCP Part 2 Protocol Layer Specification. The following table provides an overview of the XCP commands

### Generic XCP Functions

The generic ECU M&C XCP functions provide direct access to the XCP commands on a very
 low programming level. For more information about the use and parameters of the XCP
 commands, refer to the ASAM *XCP Part 2 Protocol Layer Specification*. The
 following table provides an overview of the XCP commands with their corresponding
 LabVIEW VIs or C functions.

| CCP Command | LabVIEW VI Name | C Function Name |
| --- | --- | --- |
| BUILD_CHKSUM | MC Build Checksum.vi | mcBuildChecksum |
| CLEAR_MEMORY | MC Clear Memory.vi | mcClearMemory |
| COPY_CAL_PAGE | MC XCP Copy Cal Page.vi | mcXCPCopyCalPage |
| DOWNLOAD | MC Download.vi | mcDownload |
| GET_CAL_PAGE | MC XCP Get Cal Page.vi | mcXCPGetCalPage |
| GET_ID | MC XCP Get ID.vi | mcXCPGetId |
| GET_STATUS | MC XCP Get Status.vi | mcXCPGetStatus |
| PROGRAM | MC Program.vi | mcProgram |
| PROGRAM_PREPARE | MC XCP Program Prepare.vi | mcXCPProgramPrepare |
| PROGRAM_RESET | MC Program Reset .vi | mcProgramReset |
| PROGRAM_START | MC Program Start.vi | mcProgramStart |
| PROGRAM_VERIFY | MC Program Verify.vi | mcProgramVerify |
| SET_CAL_PAGE | MC XCP Select Cal Page.vi | mcXCPSetCalPage |
| SET_REQUEST | MC XCP Set Request.vi | mcXCPSetRequest |
| SET_SEGMENT_MODE | MC XCP Set Segment Mode.vi | mcXCPSetSegmentMode |
| UPLOAD | MC Upload.vi | mcUpload |

Related information:

- ECU M&C API for LabVIEW
- ECU M&C API for C

<!--NI_TOPIC bundle=ecu-measurement-calibration-toolkit path=get-names.html language=enus -->
## TOPIC 00009: Get Names

- bundle_id: `ecu-measurement-calibration-toolkit`
- source_path: `get-names.html`
- source_url: https://docs-be.ni.com/bundle/ecu-measurement-calibration-toolkit/raw/resource/enus/get-names.html
- document_id: `ecu-measurement-calibration-toolkit`
- page_type: `leaf`
- content_type: `concept`
- source_description: If you are developing an application that another person will use, you may not want to specify a fixed channel list for a Measurement task or a fixed channel for a Characteristic in the application. Ideally, you want the end-user to select the channels of interest from user interface controls such a

### Get Names

If you are developing an application that another person will use, you may not want to
 specify a fixed channel list for a Measurement task or a fixed channel for a
 Characteristic in the application. Ideally, you want the end-user to select the channels
 of interest from user interface controls such as list boxes.

The Get Names function queries an ASAM MCD 2MC database and
 returns a list of all channels in that database regarding the selected query mode. You
 can use this list to populate user interface controls. The user can then select channels
 from these controls, avoiding the need to type in each name. Once the user makes the
 selections, the application can pass the resulting list to the appropriate function,
 such as DAQ Initialize, for an ECU Measurement channel list.

The Get Names function is MC Get Names.vi in LabVIEW or
 mcGetNames in C.

Related information:

- MC Get Names.vi
- mcGetNames

<!--NI_TOPIC bundle=ecu-measurement-calibration-toolkit path=labview-real-time-rt-configuration.html language=enus -->
## TOPIC 00010: LabVIEW Real-Time (RT) Configuration

- bundle_id: `ecu-measurement-calibration-toolkit`
- source_path: `labview-real-time-rt-configuration.html`
- source_url: https://docs-be.ni.com/bundle/ecu-measurement-calibration-toolkit/raw/resource/enus/labview-real-time-rt-configuration.html
- document_id: `ecu-measurement-calibration-toolkit`
- page_type: `leaf`
- content_type: `concept`
- source_description: LabVIEW Real-Time (RT) combines easy-to-use LabVIEW programming with the power of real-time systems. PXI SystemWhen you use an NI PXI controller as a LabVIEW RT system, you can install a PXI CAN or PXI XNET card and use the ECU M&C Toolkit to develop real-time applications for XCP or CCP using NI-CA

### LabVIEW Real-Time (RT) Configuration

LabVIEW Real-Time (RT) combines easy-to-use LabVIEW programming with the power of
 real-time systems.

#### PXI System

When you use an NI PXI controller as a LabVIEW RT
 system, you can install a PXI CAN or PXI XNET card and use the ECU M&C Toolkit
 to develop real-time applications for XCP or CCP using NI-CAN. You can also use the
 integrated ethernet ports for TCP and UDP communication.

As with any other NI
 product for LabVIEW RT, you can install the ECU M&C Toolkit software to the RT
 system using the Remote Systems node in MAX. For more
 information, refer to the LabVIEW RT documentation.

After inserting the PXI
 CAN cards and installing the NI-CAN or NI-XNET and ECU M&C Toolkit software to
 the LabVIEW RT system, you need to verify the setup.

#### NI-CAN on PXI RT System

Within the MAX
 Tools menu, select NI-CAN»RT Hardware
 Configuration. The RT Hardware Configuration tool provides features
 similar to Devices and Interfaces on the local system. Use
 the RT Hardware Configuration tool to self-test the CAN cards and assign an
 interface name to each physical CAN port.

#### NI-XNET on PXI RT System

On the RT target, you can configure your
 NI-XNET hardware the same way as on the local system. Find your PXI target device in
 MAX under Remote Systems and expand the tree. Open the
 Devices and Interfaces node and perform a self-test for
 all NI-XNET devices.

#### CompactRIO System

To install the ECU M&C toolkit to the CompactRIO
 target using MAX, expand the Remote Systems node, right-click
 your target's Software node, and select Add/Remove
 Software to launch the Real-Time Software Wizard.

For using
 XNET CAN modules with CompactRIO, install the NI-XNET software on the target using
 MAX. Refer to *NI-XNET Hardware and Software Help* for information about
 generating and loading an FPGA bit file to enable access to the modules from the
 LabVIEW Real-Time operating system.

CompactRIO FPGA-based CAN modules are
 supported by the NI-RIO software. CompactRIO FPGA-based CAN modules require an
 additional FPGA Bridge VI, which is available as part of the LabVIEW ECUMC examples.
 For more information about using CompactRIO FPGA-based CAN modules with NI-RIO
 software, refer to the NI-RIO documentation.

You can also use the integrated
 ethernet ports for TCP and UDP communication.

#### A2L Databases and SeedKey/Checksum Libraries on RT
 Targets

You need to download your A2L (ASAM MCD 2MC/ASAP2) database files
 and associated SeedKey and checksum libraries to the LabVIEW Real-Time target. The
 libraries must be compiled for the target platform and should be placed in the
 following location:

- NI Phar Lap ETS (.dll): Same directory as A2L file
- NI Linux Real-Time (.so): /usr/local/lib If your libraries
 use file names with version numbers, you need to create corresponding
 symbolic links without the version extension. Finally, execute the
 ldconfig command on the target (e.g. via SSH). In the
 A2L databases, specify your library names without "lib" prefix and file
 extension.

If libraries compatible with your platform are not available, consider using the
 Remote SeedKey Server (which is part of the LabVIEW ECUMC examples) to utilize a
 SeedKey DLL running on a Windows system over the network.

Refer to LabVIEW
 Real-Time documentation for instructions on how to transfer files to the target
 system, e.g. using FTP or SFTP, WebDAV, SD Cards, or USB drives.

<!--NI_TOPIC bundle=ecu-measurement-calibration-toolkit path=memory-programming.html language=enus -->
## TOPIC 00011: Memory Programming

- bundle_id: `ecu-measurement-calibration-toolkit`
- source_path: `memory-programming.html`
- source_url: https://docs-be.ni.com/bundle/ecu-measurement-calibration-toolkit/raw/resource/enus/memory-programming.html
- document_id: `ecu-measurement-calibration-toolkit`
- page_type: `leaf`
- content_type: `concept`
- source_description: The ECU Measurement and Calibration Toolkit allows you to issue a memory programming sequence for your ECU after you create an ECU Reference handle as described in ECU M&C API Basic Programming Model. The following flowchart illustrates the general process of a memory programming sequence of an ECU

### Memory Programming

The ECU Measurement and Calibration Toolkit allows you to issue a memory programming sequence for
 your ECU after you create an ECU Reference handle as described in *ECU M&C API
 Basic Programming Model*.

The following flowchart illustrates the general process of a memory programming sequence
 of an ECU with the ECU M&C functions. A description of each step in the decision
 process follows the flowchart.

[IMAGE alt='image' src='GUID-A7C3C7C8-9A67-4499-9FF5-A10EEA23E01E-a5.svg']

Related concepts:

- ECU M&C API Basic Programming Model

#### Program Start

The Program Start function sets the ECU into the memory
 programming mode. Note that in this mode specific features might be restricted, for
 instance, the ECU might refuse to change into the programming mode while a DAQ list is
 running. The Program Start function is MC Program
 Start.vi in LabVIEW and mcProgramStart in other
 languages.

Related information:

- MC Program Start.vi
- mcProgramStart

#### Clear Memory

It might be necessary to clear the memory before it is reprogrammed. The details are
 ECU-dependent. The Clear Memory function performs the memory
 clearing operation. It is MC Clear Memory.vi in LabVIEW or
 mcClearMemory in other languages.

Related information:

- MC Clear Memory.vi
- mcClearMemory

#### Program

The Program function actually downloads the new code to the ECU.
 It is MC Program.vi in LabVIEW or mcProgram in
 other languages.

Related information:

- MC Program.vi
- mcProgram

#### Program Reset

The Program Reset function terminates a programming sequence. Note
 that for the XCP protocol, Program Reset performs a hardware
 reset of the ECU and causes a disconnect. You have to reconnect to the ECU using the
 ECU Connect function to perform further operations. The
 Program Reset function is MC Program
 Reset.vi in LabVIEW and mcProgramReset in other
 languages.

Related information:

- MC Program Reset.vi
- mcProgramReset

#### Optional Steps for the XCP Protocol

##### XCP Program Prepare

An ECU using the XCP
 protocol might require an XCP PROGRAM_PREPARE command before a programming sequence
 is started. This command can be issued with the XCP Program
 Prepare function. It is MC XCP Program
 Prepare.vi in LabVIEW and mcXCPProgramPrepare in
 other languages.

##### Set XCP Programming Properties

XCP allows
 the programming process to be controlled by several variables. These are the
 Compression Method, Encryption
 Method, Programming Method, and
 Access Method properties. They default to 0, but can be
 set to any value before the programming process starts. The allowed values for these
 properties are ECU-specific. If any of these properties is set to a nonzero value,
 an appropriate PROGRAM_FORMAT XCP command is issued before the programming takes
 place. Note that the Access Method property also affects the
 Clear Memory function.

##### XCP Program Verify

After the memory
 programming XCP allows to verify whether the operation was successful by the
 PROGRAM_VERIFY XCP command. The details of this command are highly ECU-specific.
 This command can be issued using the XCP Program Verify
 function. It is MC XCP Program Verify.vi in LabVIEW and
 mcXCPProgramVerify in other languages.

Related information:

- MC XCP Program Prepare.vi
- mcXCPProgramPrepare
- MC XCP Program Verify.vi
- mcXCPProgramVerify

<!--NI_TOPIC bundle=ecu-measurement-calibration-toolkit path=new-features-and-changes.html language=enus -->
## TOPIC 00012: ECU Measurement and Calibration Toolkit New Features and Changes

- bundle_id: `ecu-measurement-calibration-toolkit`
- source_path: `new-features-and-changes.html`
- source_url: https://docs-be.ni.com/bundle/ecu-measurement-calibration-toolkit/raw/resource/enus/new-features-and-changes.html
- document_id: `ecu-measurement-calibration-toolkit`
- page_type: `leaf`
- content_type: `concept`
- source_description: Learn about updates, including new features and behavior changes, introduced in each version of ECU Measurement and Calibration Toolkit. Discover what is new in the latest releases of ECU Measurement and Calibration Toolkit.If you cannot find new features and changes for your version, it might not i

### ECU Measurement and
 Calibration Toolkit
 New Features and Changes

Learn about updates, including new features and behavior changes, introduced in each
 version of ECU Measurement and
 Calibration Toolkit.

ECU Measurement and
 Calibration Toolkit

Note

Release Notes

Related information:

- Software and Driver Downloads

<!--NI_TOPIC bundle=ecu-measurement-calibration-toolkit path=ni-io-trace.html language=enus -->
## TOPIC 00013: NI I/O Trace

- bundle_id: `ecu-measurement-calibration-toolkit`
- source_path: `ni-io-trace.html`
- source_url: https://docs-be.ni.com/bundle/ecu-measurement-calibration-toolkit/raw/resource/enus/ni-io-trace.html
- document_id: `ecu-measurement-calibration-toolkit`
- page_type: `leaf`
- content_type: `concept`
- source_description: The NI I/O Trace (formerly NI-Spy) tool monitors function calls to the ECU M&C API to aid in the debugging of an application. To launch this tool, open the Software branch of the MAX configuration tree, right-click NI I/O Trace, and select Launch NI I/O Trace. If you have more than one NI driver ins

### NI I/O Trace

The NI I/O Trace (formerly NI-Spy) tool monitors function calls to the ECU M&C API to
 aid in the debugging of an application. To launch this tool, open the
 Software branch of the MAX configuration tree, right-click
 NI I/O Trace, and select Launch NI I/O
 Trace.

If you have more than one NI driver installed on your computer, you can specify which
 APIs you want to monitor at any time. By default, all installed APIs are enabled. To
 select the APIs to monitor, select Tools»Options, select the
 View Selection tab, and select the desired APIs under
 Installed API Choices.

<!--NI_TOPIC bundle=ecu-measurement-calibration-toolkit path=seed-and-key-algorithm.html language=enus -->
## TOPIC 00014: Seed and Key Algorithm

- bundle_id: `ecu-measurement-calibration-toolkit`
- source_path: `seed-and-key-algorithm.html`
- source_url: https://docs-be.ni.com/bundle/ecu-measurement-calibration-toolkit/raw/resource/enus/seed-and-key-algorithm.html
- document_id: `ecu-measurement-calibration-toolkit`
- page_type: `leaf`
- content_type: `concept`
- source_description: To restrict access to an ECU, you can add a defined login mechanism to ECU software. The Association for Standardization of Automation and Measuring Systems (ASAM) defines this seed, which may be stored in the A2L file. A typical login mechanism may happen as follows: Connect to the ECU. Exchange st

### Seed and Key Algorithm

To restrict access to an ECU, you can add a defined login mechanism to ECU software. The
 Association for Standardization of Automation and Measuring Systems (ASAM) defines this
 seed, which may be stored in the A2L file. A typical login mechanism may happen as
 follows:

1. Connect to the ECU.
2. Exchange station identifications.
3. Get the seed for the key.
4. Calculate the key using a seed and key DLL as ASAM defines.
5. Unlock the ECU protection by sending the calculated key.

ASAM AE Common defines the seed and key algorithm in the *Seed and Key and Checksum
 Calculation API Version 1.0*. The specification defines the Win32 APIs for
 seed and key calculation and checksum calculation.

#### Definition for Seed and Key
 Algorithm

Function name:
 ASAP1A_CCP_ComputeKeyFromSeed

| Parameter | Description |
| --- | --- |
| 1 | Pointer to the seed data, retrieved from the ECU GET_SEED command. |
| 2 | Seed data size in number of bytes. |
| 3 | Pointer to key data, returning the calculated key. |
| 4 | Key data size in number of bytes. |
| 5 | Key data size in number of bytes. |

The calling convention is as defined in the *WIN32 API Specification for
 ASAP1b*, section 2.4.

#### Seed
 and Key Example

The following example shows a possible header file for a
 library for key calculation.

```text
/*
// Header file for ASAP1a CCP V2.1 Seed and Key Algorithm
*/
#ifndef _SEEDKEY_H_
#define _SEEDKEY_H_
#ifndef DllImport
#define DllImport __declspec( dllimport )
#endif
#ifndef DllExport
#define DllExport __declspec( dllexport )
#endif
#ifdef SEEDKEYAPI_IMPL // only defined by implementor of SeedKeyApi
#define SEEDKEYAPI DllExport __cdecl
#else
#define SEEDKEYAPI DllImport __cdecl
#endif
#ifdef __cplusplus
extern "C" {
#endif 

BOOL SEEDKEYAPI ASAP1A_CCP_ComputeKeyFromSeed (BYTE *Seed,
unsigned short SizeSeed, BYTE *Key, unsigned short MaxSizeKey,
unsigned short *SizeKey);
// Seed: Pointer to seed data
// SizeSeed:Size of seed data (length of "Seed")
// Key: Pointer, where DLL should insert the calculated key data.
// MaxSizeKey: Maximum size of "Key".
// SizeKey: Should be set from DLL corresponding to the number of data
// inserted to "Key" (at most "MaxSizeKey")
// Result: The value FALSE (= 0) indicates that the key could not be
// calculated from seed data (for example, "MaxSizeKey" is too small).
// TRUE (!= 0) indicates success of key calculation.
#ifdef __cplusplus
}
#endif
#endif //_SEEDKEY_H_
```

#### Checksum Algorithm

ASAM proposed a WIN32 API function to have a common interface to implement the checksum
 algorithms for verifying ECU calibration and program data. For details, refer to the
 *ASAM Seed and Key and Checksum Calculation API Version 1.0*.

##### Definition for a Checksum
 Algorithm

Function name: BOOL CalcChecksum(struct TRange *ptr, int
 nRanges, BYTE *pnChecksum, int *pnSignificant, WORD nFlags)

| Parameter | Description |
| --- | --- |
| 1 | Pointer to an array of ranges, stored in structures of type TRange. |
| 2 | Number of ranges stored in the array that parameter 1 points to. |
| 3 | Pointer to a byte array where the checksum must be stored. The DLL writes a maximum of 8 bytes, so the caller should reserve space for 8 bytes of data. |
| 4 | Length of actually calculated checksum (1...8). |
| 5 | Flag field for commanding how the algorithm works. Currently, only bit 0 is defined: Bit 0 = 0: pnChecksum receives the algorithm checksum calculation result. Bit 0 = 1: pnChecksum points to a checksum that is compared within the DLL with the checksum that the algorithm calculates. Returns TRUE if the checksums are identical, FALSE otherwise. All other bits are reserved and should be set to 0. |

TRange is defined as follows:

```text
struct TRange
{
char *pMem;
unsigned long lLen;
} 
```

The
 calling convention is as defined in the *WIN32 API Specification for
 ASAP1b*, section 2.4.

##### Checksum Algorithm Example

The following example shows a possible header
 file for a library for checksum calculation.

```text
/*
// checksum.h
// Header file for Checksum Algorithm
*/
#ifndef _CHECKSUM_H
#define _CHECKSUM_H
#ifdef __cplusplus
extern "C" {
#endif
#ifndef DllImport
#define DllImport __declspec( dllimport )
#endif
#ifndef DllExport
#define DllExport __declspec( dllexport )
#endif
#ifdef CHECKSUMAPI_IMPL // only defined by implementor of ChecksumApi
#define CHECKSUMAPI DllExport __cdecl
#else
#define CHECKSUMAPI DllImport __cdecl
#endif
struct TRange
{
char *pMem;
unsigned long lLen;
};
#ifdef __cplusplus
extern "C" {
#endif
BOOL CHECKSUMAPI CalcChecksum (struct TRange *ptr,
int nRanges,
BYTE *pnChecksum,
int *pnSignificant,
WORD nFlags);
#ifdef __cplusplus
}
#endif
#endif //_CHECKSUM_H 
        
```

<!--NI_TOPIC bundle=ecu-measurement-calibration-toolkit path=setget-properties.html language=enus -->
## TOPIC 00015: Set/Get Properties

- bundle_id: `ecu-measurement-calibration-toolkit`
- source_path: `setget-properties.html`
- source_url: https://docs-be.ni.com/bundle/ecu-measurement-calibration-toolkit/raw/resource/enus/setget-properties.html
- document_id: `ecu-measurement-calibration-toolkit`
- page_type: `leaf`
- content_type: `concept`
- source_description: If you need to change particular parameters within an application, such as the DTO ID, use the following sequence: Initialize the Measurement task as stopped. The Initialize function is MC DAQ Initialize.vi in LabVIEW or mcDAQInitialize in C. Use Set Property to specify the new value for the DTO ID

### Set/Get Properties

If you need to change particular parameters within an application, such as the
 DTO ID, use the following sequence:

1. Initialize the Measurement task as stopped. The Initialize 
 function is MC DAQ Initialize.vi in LabVIEW or mcDAQInitialize in
 C.
2. Use Set Property to specify the new value for the
 DTO ID property. The Set Property 
 function is MC Set Property.vi in LabVIEW or mcSetProperty in
 C.
3. Start the Measurement task with the Start function. The
 Start function is MC DAQ Start Stop.vi in LabVIEW or
 mcDAQStartStop in C. You can also start the Measurement task
 implicitly by issuing DAQ Read .

After the task is started you may need to change properties again. To change properties
 within the application, use the DAQ Start Stop function to stop
 the Measurement task, Set Property to change properties, then
 start the task again.

You also can use the Get Property function to get the value of any
 property. The Get Property function returns values whether the
 task is running or not. The Get Property function is MC Get
 Property.vi in LabVIEW or mcGetProperty in C.

Related information:

- MC DAQ Initialize.vi
- mcDAQInitialize
- MC Set Property.vi
- mcSetProperty
- MC DAQ Start Stop.vi
- mcDAQStartStop
- MC Get Property.vi
- mcGetProperty

<!--NI_TOPIC bundle=ecu-measurement-calibration-toolkit path=structure-of-the-ecu-mc-api.html language=enus -->
## TOPIC 00016: Structure of the ECU M&C API

- bundle_id: `ecu-measurement-calibration-toolkit`
- source_path: `structure-of-the-ecu-mc-api.html`
- source_url: https://docs-be.ni.com/bundle/ecu-measurement-calibration-toolkit/raw/resource/enus/structure-of-the-ecu-mc-api.html
- document_id: `ecu-measurement-calibration-toolkit`
- page_type: `leaf`
- content_type: `concept`
- source_description: The ECU M&C API is divided into three main function categories, the high-level Channel-based functions, and the generic low-level XCP and CCP functions. The ECU M&C Channel functions provide an easy way to access ECU internal data through named channels. The ECU M&C XCP functions provide direct acce

### Structure of the ECU M&C API

The ECU M&C API is divided into three main function categories, the high-level
 Channel-based functions, and the generic low-level XCP and CCP functions. The ECU
 M&C Channel functions provide an easy way to access ECU internal data through named
 channels. The ECU M&C XCP functions provide direct access to the XCP commands on a
 very low programming level. The ECU M&C CCP functions provide direct access to the
 CCP commands on a very low programming level. The following figure outlines the three
 function categories.

[IMAGE alt='image' src='GUID-CE619200-C13A-40AA-97ED-5C9C81EF23BC-a5.svg']

#### ECU M&C Channel Functions

With the ECU M&C Channel functions there are a number of ways to access memory
 content in an ECU. The starting point is always the creation of a database task,
 which is the link to a valid ASAM MCD 2MC database file (*.A2L
 file), and the selection of the protocol (XCP or CCP). With the database task
 reference it is possible to create an ECU task reference, which links to the
 selected ECU. Depending on the application scenario, the ECU task reference can be
 used for the following:

- Creation of a Measurement task to measure ECU internal data continuously or on
 demand
- Direct read/write of 0- to 2-dimensional Characteristics
- Read/write of single Measurement values on demand

##### What
 is an ECU Measurement?

An ECU Measurement, called *ECU Data
 Acquisition (DAQ)* in the XCP and CCP specifications, is a definition of
 specific procedures and CAN messages sent from the slave device (ECU) to the master
 device for fast data acquisition (DAQ).

The XCP protocol supports
 synchronous data transfer in both directions, from Master to Slave (DAQ list) and
 from Slave to Master (STIM list). XCP allows several DAQ lists, which may be
 simultaneously active. The sampling and transfer of each DAQ list is triggered by
 individual events in the slave. To allow reduction of the transfer rate, a transfer
 rate prescaler may be applied to the DAQ lists.

##### What
 is an ECU Characteristic?

An ECU Characteristic represents an ECU internal
 memory range with defined access methods through the CCP protocol. The memory range
 of a single Characteristic can be structured in three ways:

- 0-dimensional—a single value
- 1-dimensional—a curve of values
- 2-dimensional—a field of values

A Characteristic may be defined as read-only or read and write
 accessible.

#### ECU M&C XCP and CCP Functions

The ECU M&C Channel functions do not expose the method used for ECU memory access.
 However, some applications may need specific XCP or CCP command sequences, or custom
 designed commands, which are not supported by the XCP or CCP protocols. For these
 applications, the ECU M&C XCP functions and the ECU M&C CCP functions provide
 access to the ECU information at a very low level.

<!--NI_TOPIC bundle=ecu-measurement-calibration-toolkit path=summary-of-ccp-standard.html language=enus -->
## TOPIC 00017: Summary of CCP Standard

- bundle_id: `ecu-measurement-calibration-toolkit`
- source_path: `summary-of-ccp-standard.html`
- source_url: https://docs-be.ni.com/bundle/ecu-measurement-calibration-toolkit/raw/resource/enus/summary-of-ccp-standard.html
- document_id: `ecu-measurement-calibration-toolkit`
- page_type: `leaf`
- content_type: `concept`
- source_description: Controller Area Network (CAN)Bosch developed the Controller Area Network (CAN) in the mid-1980s. Using CAN, devices (controllers, sensors, and actuators) are connected on a common serial bus. This network of devices can be thought of as a scaled-down, real-time, low-cost version of the networks used

### Summary of CCP Standard

#### Controller Area Network (CAN)

Bosch developed the Controller Area
 Network (CAN) in the mid-1980s. Using CAN, devices (controllers, sensors, and
 actuators) are connected on a common serial bus. This network of devices can be
 thought of as a scaled-down, real-time, low-cost version of the networks used to
 connect personal computers. Any device on a CAN network can communicate with any
 other device using a common pair of wires.

As CAN implementations increased in
 the automotive industry, CAN was standardized internationally as ISO 11898. CAN
 chips were created by major semiconductor manufacturers such as Intel, Motorola, and
 Philips. With these developments, manufacturers of industrial automation equipment
 began to consider CAN for use in industrial applications. Comparison of the
 requirements for automotive and industrial device networks showed numerous
 similarities, including the transition away from dedicated signal lines, low cost,
 resistance to harsh environments, and high real-time capabilities.

#### CAN Calibration Protocol (CCP)

The amount of electronics introduced into the automobile has increased significantly.
 This trend is expected to continue as automobile manufacturers initiate further advances
 in safety, reliability and comfort. The introduction of advanced control
 systems—combining multiple sensors, actuators and electronic control units—has begun to
 place extensive demands on the existing Controller Area Network (CAN) communication bus.
 To enable the new generation of automotive electronics, new and highly sophisticated
 software, calibration, measurement, and diagnostic equipment must be used. At this time
 almost no standards exist in the area of software interfaces for such devices. Each
 company has its proprietary systems and interfaces to support the development of these
 high-end configurations.

The CAN Calibration Protocol was originally developed and introduced by Ingenieurbüro
 Helmut Kleinknecht, a manufacturer of calibration systems, and is used in various
 application areas in the automotive industry. Afterwards CCP was taken over by the ASAP
 working group and enhanced with optional functions and is now maintained by the ASAM
 organization.

##### Scope of CCP

The CAN Calibration Protocol is a CAN-based master-slave protocol for calibration and
 data acquisition using the CAN 2.0B standard (11-bit and 29-bit identifiers), which
 includes 2.0A (11-bit identifier). A single master device (host) can be connected to one
 or more slave devices. Before a slave device may accept commands from the host, the host
 must establish a logical point-to-point connection to the slave device. After this
 connection has been established, the slave device has to acknowledge each command
 received from the host within a specific time.

CCP offers continuous or event driven data acquisition from the controllers, as well as
 memory transfers to and control functions in the controllers for calibration
 purposes.

With these functions, CCP may be used in:

- The development of electronic control units (ECU)
- Systems for functional and environmental tests of an ECU
- Test systems and test stands for controlled devices (combustion engines, gearboxes,
 suspension systems, climate-control systems, body systems, anti-locking
 systems)
- On-board test and Measurement systems of pre-series vehicles
- Any non-automotive application of CAN-based distributed electronic control
 systems

CCP defines two function sets—one for control/memory transfer, and one for data
 acquisitions that are independent of each other and may run asynchronously. The control
 commands are used to carry out functions in the slave device, and may use the slave to
 perform tasks on other devices. The data acquisition commands are used for continuous
 data acquisition from a slave device. The devices continuously transmit internal data
 according to a list that has been configured by the host. Data acquisition is initiated
 by the host, then executed by the slave device, and may be based on a fixed sampling
 rate or be event-driven.

##### CCP Protocol Definition

Two communication objects are defined by CCP to handle the communication between host and
 slave devices—The Command Receive Object (CRO), which is used to send commands and data
 from the host to the slave device; and the Data Transmission Object (DTO), which is used
 to transmit handshake messages, data, and status information from the slave device to
 the host. Each of these message objects is assigned a unique CAN ID. Messages that are
 returned from the slave as a message to a command are called Command Return Messages
 (CRMs).

A Command Receive Object is a CAN message consisting of eight bytes. The first byte of a
 CRO is the command code, followed by the command
 counter byte. The command counter is generated for reference by the host
 to make sure that the CRM returned by a slave device corresponds to the correct host
 command. The rest of the message builds the parameter and data fields. The structure is
 as follows:

[IMAGE alt='image' src='GUID-8B9339EE-A0D6-4721-9408-95DB0590A1F4-a5.png']

A Data Transmission Object has a Packet ID (PID) as the first byte. This PID determines
 how the rest of the message is interpreted. CCP differentiates between three types of
 DTOs:

| PID | Type |
| --- | --- |
| 0x00–0xFD | Data Acquisition Message |
| 0xFE | Event Message |
| 0xFF | Command Return Message |

Event Messages and Command Return Messages have the following structure:

[IMAGE alt='image' src='GUID-96FDE890-4935-4250-9CC4-30D54C4ABF7D-a5.png']

In the case of an Event Message, the Counter field does not
 contain valid data and has to be ignored by the host. For Command Return Messages
 (CRMs), the Counter field must have the same value as the counter field of the
 corresponding CRO. The error field contains information about the error state. The
 parameter and data fields contain the
 data returned from the slave device to the host. Event Messages and CRMs consist of
 eight bytes.

Data Acquisition Messages (DAQ Messages or DAMs) have a PID in the
 first byte, and the rest of the message contains data. DAMs may be shorter than eight
 bytes:

[IMAGE alt='image' src='GUID-5A8F1403-DBB7-4E44-A59E-1AC40AC0ECA7-a5.png']

Since the PIDs 0x00–0xFD are reserved for Data Acquisition Messages, a CCP slave device
 can send up to 253 different DAMs. Each DAQ message can transfer up to seven bytes of
 data. The number of DAQ Messages supported by a slave device depends on the device
 itself.

Data acquisition is performed through a CCP slave device by reading data from a device's
 memory and copying it into the data field of a DAQ message. So the CCP slave device
 keeps a list of entries for each DAM. These lists are called Object Definition Tables
 (ODTs). Each ODT entry holds information about the memory address where data is stored
 inside the device and the size of the data to be sent. The data of the first ODT entry
 is placed in the first byte of the data field of the DAQ message. The data of the next
 entry is placed at the first free byte of the DAQ message, and so on.

<!--NI_TOPIC bundle=ecu-measurement-calibration-toolkit path=universal-measurement-and-calibration-protoco.html language=enus -->
## TOPIC 00018: Universal Measurement and Calibration Protocol (XCP) Overview

- bundle_id: `ecu-measurement-calibration-toolkit`
- source_path: `universal-measurement-and-calibration-protoco.html`
- source_url: https://docs-be.ni.com/bundle/ecu-measurement-calibration-toolkit/raw/resource/enus/universal-measurement-and-calibration-protoco.html
- document_id: `ecu-measurement-calibration-toolkit`
- page_type: `leaf`
- content_type: `concept`
- source_description: The Universal Measurement and Calibration Protocol (XCP) is a single-master/single-slave protocol for calibration and data acquisition based on various transport layers. Communication is always initiated by the XCP master. An XCP slave must respond to requests from the master within a specified time

### Universal Measurement and Calibration Protocol (XCP) Overview

The Universal Measurement and Calibration Protocol (XCP) is a single-master/single-slave
 protocol for calibration and data acquisition based on various transport layers.
 Communication is always initiated by the XCP master. An XCP slave must respond to
 requests from the master within a specified time. The XCP protocol uses a soft
 master/slave principle: once the master establishes a communication channel with the
 slave, the slave can send certain messages (Events, Service Requests and Data
 Acquisition messages) autonomously. In addition, the master sends Data Stimulation
 messages without expecting a direct response from the slave.

The XCP builds a continuous, logical, unambiguous point-to-point connection with 1
 specific slave when establishing a communication channel. The XCP slave cannot handle
 multiple connections. The master is not allowed to broadcast XCP messages to multiple
 slaves at the same time. The identification parameters of the Transport Layer (for
 instance, CAN identifiers on CAN) must be chosen in such a way that they build
 independent and unambiguously distinguishable communication channels.

The ECU M&C Toolkit abstracts the XCP communication layer so that it is transparent
 to the user. For most cases it is sufficient that the underlying XCP communication is
 handled by the toolkit kernel. Nevertheless, the ECU M&C Toolkit offers direct
 access to the low level XCP commands if a non-standard timing behavior or independent
 user defined command sequence is required.

#### XCP Protocol Version

The ECU M&C Toolkit supports the XCP
 Calibration Protocol Specification, version 1.0.

For further information
 related to the XCP protocol, refer to the XCP Calibration Protocol Specification,
 version 1.0, The Universal Measurement and Calibration Protocol Family, Part 1, by
 ASAM e.V.

<!--NI_TOPIC bundle=ecu-measurement-calibration-toolkit path=user-manual-welcome.html language=enus -->
## TOPIC 00019: ECU Measurement and Calibration Toolkit User Manual

- bundle_id: `ecu-measurement-calibration-toolkit`
- source_path: `user-manual-welcome.html`
- source_url: https://docs-be.ni.com/bundle/ecu-measurement-calibration-toolkit/raw/resource/enus/user-manual-welcome.html
- document_id: `ecu-measurement-calibration-toolkit`
- page_type: `leaf`
- content_type: `concept`
- source_description: The ECU Measurement and Calibration Toolkit User Manual provides detailed descriptions of the product functionality and the step by step processes for use. Looking for Something Else?For information not found in the User Manual for your product, such as specifications and API reference, browse Relat

### ECU Measurement and
 Calibration Toolkit
 User Manual

The ECU Measurement and
 Calibration Toolkit User Manual provides detailed
 descriptions of the product functionality and the step by step processes for use.

#### Looking for Something Else?

For information not found in the User Manual
 for your product, such as specifications and API reference, browse *Related
 Information*.

Related information:

- Download ECU Measurement and Calibration Toolkit
- ECU Measurement and Calibration Toolkit Release Notes
- Interactive Activation Guide
- ECU M&C API for LabVIEW
- ECU M&C API for C
- Discussion Forums
- NI Learning Center

<!--NI_TOPIC bundle=ecu-measurement-calibration-toolkit path=xcp-and-ccp-trace.html language=enus -->
## TOPIC 00020: XCP and CCP Trace

- bundle_id: `ecu-measurement-calibration-toolkit`
- source_path: `xcp-and-ccp-trace.html`
- source_url: https://docs-be.ni.com/bundle/ecu-measurement-calibration-toolkit/raw/resource/enus/xcp-and-ccp-trace.html
- document_id: `ecu-measurement-calibration-toolkit`
- page_type: `leaf`
- content_type: `concept`
- source_description: The XCP and CCP Trace tool monitors XCP and CCP protocol communication to aid in the debugging of an application. Launch this tool from the Start menu in Start»Programs»National Instruments»ECUMC XCP and CCP Trace. The XCP and CCP Trace application monitors, records, and displays XCP and CCP communi

### XCP and CCP Trace

The XCP and CCP Trace tool monitors XCP and CCP protocol communication to aid in the
 debugging of an application. Launch this tool from the Start menu
 in Start»Programs»National Instruments»ECUMC XCP and CCP
 Trace.

[IMAGE alt='image' src='GUID-852D0F68-4884-4DF0-B3C3-88E123E766FC-a5.gif']

The XCP and CCP Trace application monitors, records, and displays XCP and CCP
 communication commands and parameters called by your ECU M&C application using the
 XCP or CCP protocol. Use XCP and CCP Trace to analyze your application's communication
 and to verify that the communication with your ECU slave is correct.

You can use this application only when the ECU M&C application you want to debug is
 running on the same Windows machine.

XCP and CCP Trace may slow down the performance of your application, communication to
 your ECU slave, and the entire system. You should use XCP and CCP Trace only while you
 are debugging or when performance is not critical.

For further information about the displayed XCP or CCP commands and parameters, refer to
 the ASAM *XCP Part 2 Protocol Layer Specification* or *CAN Calibration
 Protocol Version 2.1* specification documents.

#### Saving Captured Communication Data

To save the information
 displayed in the XCP and CCP Trace capture window, select File»Save
 As. In the Save As dialog box, specify a name for the capture file.
 An .xlg extension is typically used for saving XCP and CCP Trace
 capture information. The XCP and CCP Trace log is stored in ASCII format; you can
 use any text editor to view the .xlg file.

#### Capturing Data

Capture is activated
 automatically after XCP and CCP Trace is started. To turn capture on, click the
 Start button [IMAGE alt='image' src='GUID-AA76EDB0-8149-4388-AF6F-FF803D6BE45C-a5.gif'] in the toolbar. To turn capture off, click the Stop
 button [IMAGE alt='image' src='GUID-ADA4ED13-C08D-4910-A7C1-F485A3BD6EBA-a5.gif'] in the toolbar.

#### XCP and CCP Trace Options

To view or modify the XCP and CCP Trace capture options, select
 Trace»Options.

##### Capture

You can specify the types of messages to capture with XCP and CCP
 Trace. By default, only XCP/CCP commands are enabled. To select the XCP/CCP messages
 to capture, select Trace»Options, and then select the message
 types you want to capture:

Commands

DAQ Messages

STIM Messages

##### Call History Depth

Call
 History Depth determines the maximum number of events that XCP and
 CCP Trace displays; the default value is 1000. When the number of captured events
 exceeds the Call History Depth setting, only the most recent
 calls are kept.

<!--NI_TOPIC bundle=ecu-measurement-calibration-toolkit path=xnet-ip-stack.html language=enus -->
## TOPIC 00021: XNET IP Stack

- bundle_id: `ecu-measurement-calibration-toolkit`
- source_path: `xnet-ip-stack.html`
- source_url: https://docs-be.ni.com/bundle/ecu-measurement-calibration-toolkit/raw/resource/enus/xnet-ip-stack.html
- document_id: `ecu-measurement-calibration-toolkit`
- page_type: `leaf`
- content_type: `concept`
- source_description: ECU Measurement and Calibration XCP functions support both XNET IP stack and native operating system IP stacks. Both can be used together or exclusively with the limitation that a single session can only use one of them at a time. By default, XCP functions use the operating system IP stack. To use a

### XNET IP Stack

ECU Measurement and Calibration XCP functions support both XNET IP stack and native
 operating system IP stacks. Both can be used together or exclusively with the limitation
 that a single session can only use one of them at a time.

By default, XCP functions use the operating system IP stack. To use an XNET IP stack, set
 the IP XNET Stack Name parameter of MC Set Property VI (or the
 mcPropIPXnetStackName parameter of mcSetProperty) to a valid
 name of an XNET IP stack.

The XNET IP stack must be created beforehand using the NI-XNET API. Refer to
 *NI-XNET Hardware and Software Help* and NI-XNET examples for information
 about configuring, creating, and clearing an XNET IP stack. To switch back to using the
 OS IP stack, provide an empty string to the same property.

The XNET IP stack supports multiple virtual interfaces for a single physical interface.
 Use the IP XNET Local Interface parameter
 (mcPropIPXnetLocalInterface) to specify which virtual
 interface should be used. This parameter is optional. Refer to *NI-XNET Hardware
 and Software Help* for more information about using virtual interfaces in an
 IP stack associated with a single XNET interface.

Related information:

- MC Set Property.vi
- mcSetProperty
