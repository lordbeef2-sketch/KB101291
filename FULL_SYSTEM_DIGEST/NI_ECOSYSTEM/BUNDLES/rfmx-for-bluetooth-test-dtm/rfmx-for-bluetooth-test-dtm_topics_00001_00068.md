# NI DOCUMENT BUNDLE: rfmx-for-bluetooth-test-dtm

<!--NI_BUNDLE_CHUNK bundle=rfmx-for-bluetooth-test-dtm start=1 end=68 -->
<!--NI_TOPIC bundle=rfmx-for-bluetooth-test-dtm path=bluetoothdtm/bp_help_file_title.html language=enus -->
## TOPIC 00001: RFmx for Bluetooth® Test Direct Test Mode Help

- bundle_id: `rfmx-for-bluetooth-test-dtm`
- source_path: `bluetoothdtm/bp_help_file_title.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-for-bluetooth-test-dtm/raw/resource/enus/bluetoothdtm/bp_help_file_title.html
- document_id: `rfmx-for-bluetooth-test-dtm`
- page_type: `leaf`
- content_type: ``

[IMAGE alt='image' src='ni_mainbitlogo_48.gif']

### RFmx for Bluetooth® Test Direct Test Mode Help

April 2021, 377891D-01

This help file contains an introduction to the RFmx for Bluetooth® direct test mode commands in LabVIEW, C, and .NET environments to configure a Bluetooth device.

© 2019–2021 National Instruments Corporation. All rights reserved.

Refer to the <National Instruments>\_Legal Information directory for information about NI copyright, patents, trademarks, warranties, product warnings, and export compliance.

<!--NI_TOPIC bundle=rfmx-for-bluetooth-test-dtm path=bluetoothdtm/dotnet_help_file_title.html language=enus -->
## TOPIC 00002: RFmx for Bluetooth® Test Direct Test Mode .NET Help

- bundle_id: `rfmx-for-bluetooth-test-dtm`
- source_path: `bluetoothdtm/dotnet_help_file_title.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-for-bluetooth-test-dtm/raw/resource/enus/bluetoothdtm/dotnet_help_file_title.html
- document_id: `rfmx-for-bluetooth-test-dtm`
- page_type: `leaf`
- content_type: ``

### RFmx for Bluetooth® Test Direct Test Mode .NET Reference

This help file contains information about the RFmx for Bluetooth® Direct Test Mode methods and values that you can use when programming your application.

© 2019–2021 National Instruments Corporation. All rights reserved.

<!--NI_TOPIC bundle=rfmx-for-bluetooth-test-dtm path=bluetoothdtm/standard_functionality_for_error_in_parameters.html language=enus -->
## TOPIC 00003: Using the Standard Functionality for error in Parameters

- bundle_id: `rfmx-for-bluetooth-test-dtm`
- source_path: `bluetoothdtm/standard_functionality_for_error_in_parameters.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-for-bluetooth-test-dtm/raw/resource/enus/bluetoothdtm/standard_functionality_for_error_in_parameters.html
- document_id: `rfmx-for-bluetooth-test-dtm`
- page_type: `leaf`
- content_type: ``

### Using the Standard Functionality for error in Parameters

Many LabVIEW nodes such as VIs contain an **error in** parameter that you can use to manage errors. These parameters typically provide the same, standard functionality. When a node exhibits different parameter functionality, the exceptions are documented in the reference material for that node.

|  | Note Some nodes, such as error handling VIs, contain an error in parameter that does not provide standard error in functionality, but that does contain standard error in cluster elements. |
| --- | --- |

Standard **error in** functionality is as follows:

|  | error in describes error conditions that occur before this node runs. The default is no error. If an error occurred before this node runs, the node passes the error in value to error out. This node runs normally only if no error occurred before this node runs. If an error occurs while this node runs, it runs normally and sets its own error status in error out. Use error in and error out to check errors and to specify execution order by wiring error out from one node to error in of the next node. |
| --- | --- |

The **error in** cluster contains the following cluster elements:

|  | status is TRUE (X) if an error occurred before this node ran or FALSE (checkmark) to indicate a warning or that no error occurred before this node ran. The default is FALSE. |
| --- | --- |
|  | code is the error or warning code. The default is 0. If status is TRUE, code is an error code. If status is FALSE, code is 0 or a warning code. |
|  | source specifies the origin of the error or warning and is, in most cases, the name of the node that produced the error or warning. The default is an empty string. |

<!--NI_TOPIC bundle=rfmx-for-bluetooth-test-dtm path=bluetoothdtm/standard_functionality_for_error_out_parameters.html language=enus -->
## TOPIC 00004: Using the Standard Functionality for error out Parameters

- bundle_id: `rfmx-for-bluetooth-test-dtm`
- source_path: `bluetoothdtm/standard_functionality_for_error_out_parameters.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-for-bluetooth-test-dtm/raw/resource/enus/bluetoothdtm/standard_functionality_for_error_out_parameters.html
- document_id: `rfmx-for-bluetooth-test-dtm`
- page_type: `leaf`
- content_type: ``

### Using the Standard Functionality for error out Parameters

Many LabVIEW VIs contain an **error out** parameter you can use to manage errors. These parameters typically provide the same, standard functionality. When a node exhibits different parameter functionality, the exceptions are documented in the reference material for that node.

Standard **error out** functionality is as follows:

|  | error out contains error information. If error in indicates that an error occurred before this VI ran, error out contains the same error information. Otherwise, it describes the error status that this VI produces. Right-click the error out front panel indicator and select Explain Error from the shortcut menu for more information about the error. |
| --- | --- |

The **error out** contains the following cluster elements:

|  | status is TRUE (X) if an error occurred or FALSE (checkmark) to indicate a warning or that no error occurred. |
| --- | --- |
|  | code is the error or warning code. If status is TRUE, code is an error code. If status is FALSE, code is 0 or a warning code. |
|  | source specifies the origin of the error or warning and is, in most cases, the name of the node that produced the error or warning. |

<!--NI_TOPIC bundle=rfmx-for-bluetooth-test-dtm path=bluetoothdtm/working_with_application_manifest.html language=enus -->
## TOPIC 00005: Creating an Application with RFmx

- bundle_id: `rfmx-for-bluetooth-test-dtm`
- source_path: `bluetoothdtm/working_with_application_manifest.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-for-bluetooth-test-dtm/raw/resource/enus/bluetoothdtm/working_with_application_manifest.html
- document_id: `rfmx-for-bluetooth-test-dtm`
- page_type: `leaf`
- content_type: ``

### Working with Application Manifest

NI recommends that you embed an application manifest in the .exe file you create with Bluetooth Direct Test Mode to avoid undesirable visual artifacts on very high resolution displays running Windows 10.
For WPF-based applications, the dpiAware element in the manifest should be set totrue/pm. For other applications it should be set to false.
Refer to Application Manifests on the Microsoft TechNet site for more information about application manifests. 
 Refer to your ADE documentation for information about how to embed an application manifest in your .exe file.

<!--NI_TOPIC bundle=rfmx-for-bluetooth-test-dtm path=bluetoothdtmdotnet/html/0cb3fbfd-2d94-df3f-df94-8be1c8f79684.htm language=enus -->
## TOPIC 00006: BluetoothDtmModulationIndex Enumeration

- bundle_id: `rfmx-for-bluetooth-test-dtm`
- source_path: `bluetoothdtmdotnet/html/0cb3fbfd-2d94-df3f-df94-8be1c8f79684.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-for-bluetooth-test-dtm/raw/resource/enus/bluetoothdtmdotnet/html/0cb3fbfd-2d94-df3f-df94-8be1c8f79684.htm
- document_id: `rfmx-for-bluetooth-test-dtm`
- page_type: `leaf`
- content_type: ``

BluetoothDtmModulationIndex Enumeration

### BluetoothDtmModulationIndex Enumeration

Specifies the type of modulation index at the generator. The default value is Standard.

Namespace:

NationalInstruments.BluetoothDtm

Assembly:

##### Syntax

C#

VB

```text
public enum BluetoothDtmModulationIndex
```

```text
Public Enumeration BluetoothDtmModulationIndex
```

##### Members

|  | Member name | Value | Description |
| --- | --- | --- | --- |
|  | Standard | 0 | The packets are generated with standard modulation index. |
|  | Stable | 1 | The packets are generated with stable modulation index. |

##### See Also

###### Reference

NationalInstruments.BluetoothDtm Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-for-bluetooth-test-dtm path=bluetoothdtmdotnet/html/0f92a84d-f5b5-44e7-b73e-eb1f0ee5276e.htm language=enus -->
## TOPIC 00007: NIBluetoothDtm Methods

- bundle_id: `rfmx-for-bluetooth-test-dtm`
- source_path: `bluetoothdtmdotnet/html/0f92a84d-f5b5-44e7-b73e-eb1f0ee5276e.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-for-bluetooth-test-dtm/raw/resource/enus/bluetoothdtmdotnet/html/0f92a84d-f5b5-44e7-b73e-eb1f0ee5276e.htm
- document_id: `rfmx-for-bluetooth-test-dtm`
- page_type: `leaf`
- content_type: ``

NIBluetoothDtm Methods

### NIBluetoothDtm Methods

The [NIBluetoothDtm](25ad6596-b19d-4146-9643-f08eb3dd86c4.htm) type exposes the following members.

##### Methods

|  | Name | Description |
| --- | --- | --- |
|  | Close | Closes a device session or the event object that you specify in the VISA resource name parameter. |
|  | ConfigureVisaSerialSettings | Configures the VISA serial settings for the device under test (DUT) specified by the VISA resource name parameter. |
|  | CreateCustomCommand | Sends the specified custom command to the device under test (DUT). |
|  | Dispose | Closes the VISA session. Call this method a number of times equal to the number of times you obtained a reference to the VISA session for a particular resource name. |
|  | Equals | Determines whether the specified Object is equal to the current Object. (Inherited from Object.) |
|  | GetHashCode | Serves as a hash function for a particular type. (Inherited from Object.) |
|  | GetType | Gets the Type of the current instance. (Inherited from Object.) |
|  | HciLEDirectionFindingReceiverTest | Sends a command to the device under test (DUT) to start the receiver test. |
|  | HciLEDirectionFindingTransmitterTest | Sends a command to the device under test (DUT) to start the transmitter test. |
|  | HciLEEnhancedReceiverTest | Sends a command to the device under test (DUT) to start the receiver test. |
|  | HciLEEnhancedTransmitterTest | Sends the command to the device under test (DUT) to start the transmitter test. |
|  | HciLEReceiverTest | Sends a command to the device under test (DUT) to start the receiver test. |
|  | HciLETestEnd | Sends the command to the device under test (DUT) to end the transmitter or receiver test. |
|  | HciLETransmitterTest | Sends a command to the device under test (DUT) to start the transmitter test. |
|  | HciReadBluetoothDeviceAddress | Sends the command to the device under test (DUT) to get its Bluetooth device (BD) address. |
|  | HciReset | Resets the device under test (DUT) specified by the VISA resource name parameter. |
|  | SetVisaTimeout | Sets the timeout value, in milliseconds (ms), for the VISA session of the device under test (DUT), specified by the VISA resource name parameter. |
|  | ToString | Returns a string that represents the current object. (Inherited from Object.) |

Top

##### See Also

###### Reference

NIBluetoothDtm Class

NationalInstruments.BluetoothDtm Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-for-bluetooth-test-dtm path=bluetoothdtmdotnet/html/1033e53e-d97f-06aa-be65-1ab6e39ea879.htm language=enus -->
## TOPIC 00008: BluetoothDtmException Class

- bundle_id: `rfmx-for-bluetooth-test-dtm`
- source_path: `bluetoothdtmdotnet/html/1033e53e-d97f-06aa-be65-1ab6e39ea879.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-for-bluetooth-test-dtm/raw/resource/enus/bluetoothdtmdotnet/html/1033e53e-d97f-06aa-be65-1ab6e39ea879.htm
- document_id: `rfmx-for-bluetooth-test-dtm`
- page_type: `leaf`
- content_type: ``

BluetoothDtmException Class

### BluetoothDtmException Class

Initializes a new instance of the BluetoothDtmException class with a specified error message.

##### Inheritance Hierarchy

Namespace:

NationalInstruments.BluetoothDtm

Assembly:

##### Syntax

C#

VB

```text
public class BluetoothDtmException : Exception
```

```text
Public Class BluetoothDtmException
	Inherits Exception
```

The BluetoothDtmException type exposes the following members.

##### Constructors

|  | Name | Description |
| --- | --- | --- |
|  | BluetoothDtmException | Initializes a new instance of the BluetoothDtmException class |
|  | BluetoothDtmException(String) | Initializes a new instance of the class BluetoothDtmException with a specified error message. |

Top

##### Properties

|  | Name | Description |
| --- | --- | --- |
|  | Data | Gets a collection of key/value pairs that provide additional user-defined information about the exception. (Inherited from Exception.) |
|  | HelpLink | Gets or sets a link to the help file associated with this exception. (Inherited from Exception.) |
|  | HResult | Gets or sets HRESULT, a coded numerical value that is assigned to a specific exception. (Inherited from Exception.) |
|  | InnerException | Gets the Exception instance that caused the current exception. (Inherited from Exception.) |
|  | Message | Gets a message that describes the current exception. (Inherited from Exception.) |
|  | Source | Gets or sets the name of the application or the object that causes the error. (Inherited from Exception.) |
|  | StackTrace | Gets a string representation of the immediate frames on the call stack. (Inherited from Exception.) |
|  | TargetSite | Gets the method that throws the current exception. (Inherited from Exception.) |

Top

##### Methods

|  | Name | Description |
| --- | --- | --- |
|  | Equals | Determines whether the specified Object is equal to the current Object. (Inherited from Object.) |
|  | Finalize | Allows an object to try to free resources and perform other cleanup operations before it is reclaimed by garbage collection. (Inherited from Object.) |
|  | GetBaseException | When overridden in a derived class, returns the Exception that is the root cause of one or more subsequent exceptions. (Inherited from Exception.) |
|  | GetHashCode | Serves as a hash function for a particular type. (Inherited from Object.) |
|  | GetObjectData | When overridden in a derived class, sets the SerializationInfo with information about the exception. (Inherited from Exception.) |
|  | GetType | Gets the runtime type of the current instance. (Inherited from Exception.) |
|  | MemberwiseClone | Creates a shallow copy of the current Object. (Inherited from Object.) |
|  | ToString | Creates and returns a string representation of the current exception. (Inherited from Exception.) |

Top

##### Events

|  | Name | Description |
| --- | --- | --- |
|  | SerializeObjectState | Occurs when an exception is serialized to create an exception state object that contains serialized data about the exception. (Inherited from Exception.) |

Top

##### Remarks

##### Thread Safety

static

Shared

##### See Also

###### Reference

NationalInstruments.BluetoothDtm Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-for-bluetooth-test-dtm path=bluetoothdtmdotnet/html/190ab751-831a-bc52-4b17-00ddd90afe50.htm language=enus -->
## TOPIC 00009: NIBluetoothDtm Constructor

- bundle_id: `rfmx-for-bluetooth-test-dtm`
- source_path: `bluetoothdtmdotnet/html/190ab751-831a-bc52-4b17-00ddd90afe50.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-for-bluetooth-test-dtm/raw/resource/enus/bluetoothdtmdotnet/html/190ab751-831a-bc52-4b17-00ddd90afe50.htm
- document_id: `rfmx-for-bluetooth-test-dtm`
- page_type: `leaf`
- content_type: ``

NIBluetoothDtm Constructor

### NIBluetoothDtm Constructor

Creates an NI-VISA session to the device you specify through the resourceName parameter.

Namespace:

NationalInstruments.BluetoothDtm

Assembly:

##### Syntax

C#

VB

```text
public NIBluetoothDtm(
	string resourceName
)
```

```text
Public Sub New ( 
	resourceName As String
)
```

###### Parameters

- **resourceName**
  - Type: SystemStringSpecifies the resource name of the device to initialize.

##### See Also

###### Reference

NIBluetoothDtm Class

NationalInstruments.BluetoothDtm Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-for-bluetooth-test-dtm path=bluetoothdtmdotnet/html/1ec2dc19-a142-7fb8-b344-2c9d6ccd1b9c.htm language=enus -->
## TOPIC 00010: NIBluetoothDtmHciLETestEnd Method

- bundle_id: `rfmx-for-bluetooth-test-dtm`
- source_path: `bluetoothdtmdotnet/html/1ec2dc19-a142-7fb8-b344-2c9d6ccd1b9c.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-for-bluetooth-test-dtm/raw/resource/enus/bluetoothdtmdotnet/html/1ec2dc19-a142-7fb8-b344-2c9d6ccd1b9c.htm
- document_id: `rfmx-for-bluetooth-test-dtm`
- page_type: `leaf`
- content_type: ``

NIBluetoothDtm.HciLETestEnd Method

### NIBluetoothDtmHciLETestEnd Method

Sends the command to the device under test (DUT) to end the transmitter or receiver test.

Namespace:

NationalInstruments.BluetoothDtm

Assembly:

##### Syntax

C#

VB

```text
public int HciLETestEnd(
	out int packetCount,
	out int status
)
```

```text
Public Function HciLETestEnd ( 
	<OutAttribute> ByRef packetCount As Integer,
	<OutAttribute> ByRef status As Integer
) As Integer
```

###### Parameters

- **packetCount**
  - Type: SystemInt32Returns the number of packets received by the DUT.
- **status**
  - Type: SystemInt32returns the status of the test end command. The DUT receives and executes the test end command if the status parameter returns a 0x00 value. The test end command fails if the status parameter returns a non-zero (0x01-0xFF) value.

###### Return Value

Int32

##### Remarks

##### See Also

###### Reference

NIBluetoothDtm Class

NationalInstruments.BluetoothDtm Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-for-bluetooth-test-dtm path=bluetoothdtmdotnet/html/22f47a7c-b589-a8a6-727a-2e1ea6cfe918.htm language=enus -->
## TOPIC 00011: NIBluetoothDtmHciLEEnhancedTransmitterTest Method

- bundle_id: `rfmx-for-bluetooth-test-dtm`
- source_path: `bluetoothdtmdotnet/html/22f47a7c-b589-a8a6-727a-2e1ea6cfe918.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-for-bluetooth-test-dtm/raw/resource/enus/bluetoothdtmdotnet/html/22f47a7c-b589-a8a6-727a-2e1ea6cfe918.htm
- document_id: `rfmx-for-bluetooth-test-dtm`
- page_type: `leaf`
- content_type: ``

NIBluetoothDtm.HciLEEnhancedTransmitterTest Method

### NIBluetoothDtmHciLEEnhancedTransmitterTest Method

Sends the command to the device under test (DUT) to start the transmitter test.

Namespace:

NationalInstruments.BluetoothDtm

Assembly:

##### Syntax

C#

VB

```text
public int HciLEEnhancedTransmitterTest(
	int channelNumber,
	int payloadLengthBytes,
	BluetoothDtmLEPatternType lePatternType,
	BluetoothDtmTransmitterPhy phy,
	out int status
)
```

```text
Public Function HciLEEnhancedTransmitterTest ( 
	channelNumber As Integer,
	payloadLengthBytes As Integer,
	lePatternType As BluetoothDtmLEPatternType,
	phy As BluetoothDtmTransmitterPhy,
	<OutAttribute> ByRef status As Integer
) As Integer
```

###### Parameters

- **channelNumber**
  - Type: SystemInt32Specifies the Bluetooth transmit channel number of the signal generated by the DUT. The default value is 0.
- **payloadLengthBytes**
  - Type: SystemInt32Specifies the length, in bytes, of payload data in each packet that the DUT transmits. The default value is 37.
- **lePatternType**
  - Type: NationalInstruments.BluetoothDtmBluetoothDtmLEPatternTypeSpecifies the type of payload to use for the LE packet. Payload type values of Type_Prbs9, Type_11110000, and Type_10101010 must be supported by the DUT. The remaining payload type values are optional. The default value is Type_Prbs9.
- **phy**
  - Type: NationalInstruments.BluetoothDtmBluetoothDtmTransmitterPhySpecifies the type of the packet to be transmitted by the physical layer of the DUT. The default value is Phy_1Mbps.
- **status**
  - Type: SystemInt32Returns the status of the transmitter test command. The DUT receives and executes the transmitter test command if the status parameter returns a 0x00 value. The transmitter test command fails if the status parameter returns a non-zero (0x01-0xFF) value.

###### Return Value

Int32

##### Remarks

##### See Also

###### Reference

NIBluetoothDtm Class

NationalInstruments.BluetoothDtm Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-for-bluetooth-test-dtm path=bluetoothdtmdotnet/html/25ad6596-b19d-4146-9643-f08eb3dd86c4.htm language=enus -->
## TOPIC 00012: NIBluetoothDtm Class

- bundle_id: `rfmx-for-bluetooth-test-dtm`
- source_path: `bluetoothdtmdotnet/html/25ad6596-b19d-4146-9643-f08eb3dd86c4.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-for-bluetooth-test-dtm/raw/resource/enus/bluetoothdtmdotnet/html/25ad6596-b19d-4146-9643-f08eb3dd86c4.htm
- document_id: `rfmx-for-bluetooth-test-dtm`
- page_type: `leaf`
- content_type: ``

NIBluetoothDtm Class

### NIBluetoothDtm Class

Defines a root class which is used to identify and control BluetoothDtm signal configuration.

##### Inheritance Hierarchy

Namespace:

NationalInstruments.BluetoothDtm

Assembly:

##### Syntax

C#

VB

```text
public sealed class NIBluetoothDtm : IDisposable
```

```text
Public NotInheritable Class NIBluetoothDtm
	Implements IDisposable
```

The NIBluetoothDtm type exposes the following members.

##### Constructors

|  | Name | Description |
| --- | --- | --- |
|  | NIBluetoothDtm | Creates an NI-VISA session to the device you specify through the resourceName parameter. |

Top

##### Methods

|  | Name | Description |
| --- | --- | --- |
|  | Close | Closes a device session or the event object that you specify in the VISA resource name parameter. |
|  | ConfigureVisaSerialSettings | Configures the VISA serial settings for the device under test (DUT) specified by the VISA resource name parameter. |
|  | CreateCustomCommand | Sends the specified custom command to the device under test (DUT). |
|  | Dispose | Closes the VISA session. Call this method a number of times equal to the number of times you obtained a reference to the VISA session for a particular resource name. |
|  | Equals | Determines whether the specified Object is equal to the current Object. (Inherited from Object.) |
|  | GetHashCode | Serves as a hash function for a particular type. (Inherited from Object.) |
|  | GetType | Gets the Type of the current instance. (Inherited from Object.) |
|  | HciLEDirectionFindingReceiverTest | Sends a command to the device under test (DUT) to start the receiver test. |
|  | HciLEDirectionFindingTransmitterTest | Sends a command to the device under test (DUT) to start the transmitter test. |
|  | HciLEEnhancedReceiverTest | Sends a command to the device under test (DUT) to start the receiver test. |
|  | HciLEEnhancedTransmitterTest | Sends the command to the device under test (DUT) to start the transmitter test. |
|  | HciLEReceiverTest | Sends a command to the device under test (DUT) to start the receiver test. |
|  | HciLETestEnd | Sends the command to the device under test (DUT) to end the transmitter or receiver test. |
|  | HciLETransmitterTest | Sends a command to the device under test (DUT) to start the transmitter test. |
|  | HciReadBluetoothDeviceAddress | Sends the command to the device under test (DUT) to get its Bluetooth device (BD) address. |
|  | HciReset | Resets the device under test (DUT) specified by the VISA resource name parameter. |
|  | SetVisaTimeout | Sets the timeout value, in milliseconds (ms), for the VISA session of the device under test (DUT), specified by the VISA resource name parameter. |
|  | ToString | Returns a string that represents the current object. (Inherited from Object.) |

Top

##### See Also

###### Reference

NationalInstruments.BluetoothDtm Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-for-bluetooth-test-dtm path=bluetoothdtmdotnet/html/2630488f-928c-256e-0e82-84f6a79ba1c2.htm language=enus -->
## TOPIC 00013: NIBluetoothDtmHciLEEnhancedReceiverTest Method

- bundle_id: `rfmx-for-bluetooth-test-dtm`
- source_path: `bluetoothdtmdotnet/html/2630488f-928c-256e-0e82-84f6a79ba1c2.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-for-bluetooth-test-dtm/raw/resource/enus/bluetoothdtmdotnet/html/2630488f-928c-256e-0e82-84f6a79ba1c2.htm
- document_id: `rfmx-for-bluetooth-test-dtm`
- page_type: `leaf`
- content_type: ``

NIBluetoothDtm.HciLEEnhancedReceiverTest Method

### NIBluetoothDtmHciLEEnhancedReceiverTest Method

Sends a command to the device under test (DUT) to start the receiver test.

Namespace:

NationalInstruments.BluetoothDtm

Assembly:

##### Syntax

C#

VB

```text
public int HciLEEnhancedReceiverTest(
	int channelNumber,
	BluetoothDtmModulationIndex modulationIndex,
	BluetoothDtmReceiverPhy phy,
	out int status
)
```

```text
Public Function HciLEEnhancedReceiverTest ( 
	channelNumber As Integer,
	modulationIndex As BluetoothDtmModulationIndex,
	phy As BluetoothDtmReceiverPhy,
	<OutAttribute> ByRef status As Integer
) As Integer
```

###### Parameters

- **channelNumber**
  - Type: SystemInt32 Specifies the Bluetooth transmit channel number of the generated signal. The default value is 0.
- **modulationIndex**
  - Type: NationalInstruments.BluetoothDtmBluetoothDtmModulationIndexSpecifies the type of modulation index at the generator. The default value is Standard.
- **phy**
  - Type: NationalInstruments.BluetoothDtmBluetoothDtmReceiverPhySpecifies the type of the generated packet by the physical layer of the DUT. The default value is Phy_1Mbps.
- **status**
  - Type: SystemInt32Returns the status of the receiver test command. The DUT receives and executes the receiver test command if the status parameter returns a 0x00 value. The receiver test command fails if the status parameter returns a non-zero (0x01-0xFF) value.

###### Return Value

Int32

##### Remarks

##### See Also

###### Reference

NIBluetoothDtm Class

NationalInstruments.BluetoothDtm Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-for-bluetooth-test-dtm path=bluetoothdtmdotnet/html/32093b88-0b32-3de8-e417-f4af6e1b8d26.htm language=enus -->
## TOPIC 00014: BluetoothDtmException Methods

- bundle_id: `rfmx-for-bluetooth-test-dtm`
- source_path: `bluetoothdtmdotnet/html/32093b88-0b32-3de8-e417-f4af6e1b8d26.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-for-bluetooth-test-dtm/raw/resource/enus/bluetoothdtmdotnet/html/32093b88-0b32-3de8-e417-f4af6e1b8d26.htm
- document_id: `rfmx-for-bluetooth-test-dtm`
- page_type: `leaf`
- content_type: ``

BluetoothDtmException Methods

### BluetoothDtmException Methods

The [BluetoothDtmException](1033e53e-d97f-06aa-be65-1ab6e39ea879.htm) type exposes the following members.

##### Methods

|  | Name | Description |
| --- | --- | --- |
|  | Equals | Determines whether the specified Object is equal to the current Object. (Inherited from Object.) |
|  | Finalize | Allows an object to try to free resources and perform other cleanup operations before it is reclaimed by garbage collection. (Inherited from Object.) |
|  | GetBaseException | When overridden in a derived class, returns the Exception that is the root cause of one or more subsequent exceptions. (Inherited from Exception.) |
|  | GetHashCode | Serves as a hash function for a particular type. (Inherited from Object.) |
|  | GetObjectData | When overridden in a derived class, sets the SerializationInfo with information about the exception. (Inherited from Exception.) |
|  | GetType | Gets the runtime type of the current instance. (Inherited from Exception.) |
|  | MemberwiseClone | Creates a shallow copy of the current Object. (Inherited from Object.) |
|  | ToString | Creates and returns a string representation of the current exception. (Inherited from Exception.) |

Top

##### See Also

###### Reference

BluetoothDtmException Class

NationalInstruments.BluetoothDtm Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-for-bluetooth-test-dtm path=bluetoothdtmdotnet/html/3b454599-2829-2bb3-9769-bd1440e4c7c6.htm language=enus -->
## TOPIC 00015: NIBluetoothDtmCreateCustomCommand Method

- bundle_id: `rfmx-for-bluetooth-test-dtm`
- source_path: `bluetoothdtmdotnet/html/3b454599-2829-2bb3-9769-bd1440e4c7c6.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-for-bluetooth-test-dtm/raw/resource/enus/bluetoothdtmdotnet/html/3b454599-2829-2bb3-9769-bd1440e4c7c6.htm
- document_id: `rfmx-for-bluetooth-test-dtm`
- page_type: `leaf`
- content_type: ``

NIBluetoothDtm.CreateCustomCommand Method

### NIBluetoothDtmCreateCustomCommand Method

Sends the specified custom command to the device under test (DUT).

Namespace:

NationalInstruments.BluetoothDtm

Assembly:

##### Syntax

C#

VB

```text
public int CreateCustomCommand(
	int[] opCode,
	int[] commandParameters,
	ref int[] returnParameters
)
```

```text
Public Function CreateCustomCommand ( 
	opCode As Integer(),
	commandParameters As Integer(),
	ByRef returnParameters As Integer()
) As Integer
```

###### Parameters

- **opCode**
  - Type: SystemInt32Specifies an array of custom opcode commands to send to the DUT.
- **commandParameters**
  - Type: SystemInt32Specifies an array of the input parameters required for the custom command.
- **returnParameters**
  - Type: SystemInt32Returns an array of the parameters sent by the DUT in response to the custom command.

###### Return Value

Int32

##### Remarks

##### See Also

###### Reference

NIBluetoothDtm Class

NationalInstruments.BluetoothDtm Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-for-bluetooth-test-dtm path=bluetoothdtmdotnet/html/3f283c5e-c9f3-9117-7c3e-69b1f7c391cc.htm language=enus -->
## TOPIC 00016: NIBluetoothDtmConfigureVisaSerialSettings Method

- bundle_id: `rfmx-for-bluetooth-test-dtm`
- source_path: `bluetoothdtmdotnet/html/3f283c5e-c9f3-9117-7c3e-69b1f7c391cc.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-for-bluetooth-test-dtm/raw/resource/enus/bluetoothdtmdotnet/html/3f283c5e-c9f3-9117-7c3e-69b1f7c391cc.htm
- document_id: `rfmx-for-bluetooth-test-dtm`
- page_type: `leaf`
- content_type: ``

NIBluetoothDtm.ConfigureVisaSerialSettings Method

### NIBluetoothDtmConfigureVisaSerialSettings Method

Configures the VISA serial settings for the device under test (DUT) specified by the VISA resource name parameter.

Namespace:

NationalInstruments.BluetoothDtm

Assembly:

##### Syntax

C#

VB

```text
public int ConfigureVisaSerialSettings(
	ushort dataBits,
	uint baudRate,
	BluetoothDtmFlowControl flowControl,
	BluetoothDtmStopBits stopBits,
	BluetoothDtmParity parity
)
```

```text
Public Function ConfigureVisaSerialSettings ( 
	dataBits As UShort,
	baudRate As UInteger,
	flowControl As BluetoothDtmFlowControl,
	stopBits As BluetoothDtmStopBits,
	parity As BluetoothDtmParity
) As Integer
```

###### Parameters

- **dataBits**
  - Type: SystemUInt16Specifies the number of data bits contained in each frame. Valid values are 5 to 8, inclusive. The data bits for each frame are located in the low-order bits of every byte stored in the memory. The default value is 8.
- **baudRate**
  - Type: SystemUInt32Specifies the baud rate of the given communication port. The default value is 115,200.
- **flowControl**
  - Type: NationalInstruments.BluetoothDtmBluetoothDtmFlowControlSpecifies the baud rate of the given communication port. Specifies the flow control method used for transmitting and receiving data. The default value is RtsCts.
- **stopBits**
  - Type: NationalInstruments.BluetoothDtmBluetoothDtmStopBitsSpecifies the number of stop bits used to indicate the end of a frame. Valid values are StopBits1_0, StopBits1_5, and StopBits2_0. The default value is StopBits1_0.
- **parity**
  - Type: NationalInstruments.BluetoothDtmBluetoothDtmParitySpecifies the parity bit used with each transmitted or received frame. The default value is None

###### Return Value

Int32

##### Remarks

##### See Also

###### Reference

NIBluetoothDtm Class

NationalInstruments.BluetoothDtm Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-for-bluetooth-test-dtm path=bluetoothdtmdotnet/html/53dacf78-9e0e-0fa5-b0f3-6f06e1324bc9.htm language=enus -->
## TOPIC 00017: NIBluetoothDtmHciReadBluetoothDeviceAddress Method

- bundle_id: `rfmx-for-bluetooth-test-dtm`
- source_path: `bluetoothdtmdotnet/html/53dacf78-9e0e-0fa5-b0f3-6f06e1324bc9.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-for-bluetooth-test-dtm/raw/resource/enus/bluetoothdtmdotnet/html/53dacf78-9e0e-0fa5-b0f3-6f06e1324bc9.htm
- document_id: `rfmx-for-bluetooth-test-dtm`
- page_type: `leaf`
- content_type: ``

NIBluetoothDtm.HciReadBluetoothDeviceAddress Method

### NIBluetoothDtmHciReadBluetoothDeviceAddress Method

Sends the command to the device under test (DUT) to get its Bluetooth device (BD) address.

Namespace:

NationalInstruments.BluetoothDtm

Assembly:

##### Syntax

C#

VB

```text
public int HciReadBluetoothDeviceAddress(
	out long bluetoothDeviceAddress,
	out int status
)
```

```text
Public Function HciReadBluetoothDeviceAddress ( 
	<OutAttribute> ByRef bluetoothDeviceAddress As Long,
	<OutAttribute> ByRef status As Integer
) As Integer
```

###### Parameters

- **bluetoothDeviceAddress**
  - Type: SystemInt64returns the BD address of the DUT.
- **status**
  - Type: SystemInt32Returns the status of the read BD_ADDR command. The DUT receives and executes the read BD_ADDR command if the status parameter returns a 0x00 value. The read BD_ADDR command fails if the status parameter returns a non-zero (0x01-0xFF) value.

###### Return Value

Int32

##### Remarks

##### See Also

###### Reference

NIBluetoothDtm Class

NationalInstruments.BluetoothDtm Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-for-bluetooth-test-dtm path=bluetoothdtmdotnet/html/5794b952-1d88-ae36-60a2-b3511347fc5e.htm language=enus -->
## TOPIC 00018: NIBluetoothDtmHciLEDirectionFindingReceiverTest Method

- bundle_id: `rfmx-for-bluetooth-test-dtm`
- source_path: `bluetoothdtmdotnet/html/5794b952-1d88-ae36-60a2-b3511347fc5e.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-for-bluetooth-test-dtm/raw/resource/enus/bluetoothdtmdotnet/html/5794b952-1d88-ae36-60a2-b3511347fc5e.htm
- document_id: `rfmx-for-bluetooth-test-dtm`
- page_type: `leaf`
- content_type: ``

NIBluetoothDtm.HciLEDirectionFindingReceiverTest Method

### NIBluetoothDtmHciLEDirectionFindingReceiverTest Method

Sends a command to the device under test (DUT) to start the receiver test.

Namespace:

NationalInstruments.BluetoothDtm

Assembly:

##### Syntax

C#

VB

```text
public int HciLEDirectionFindingReceiverTest(
	int channelNumber,
	BluetoothDtmModulationIndex modulationIndex,
	BluetoothDtmReceiverPhy phy,
	BluetoothDtmDirectionFindingMode directionFindingMode,
	int switchingPatternLength,
	double cteLength,
	double cteSlotDuration,
	int[] antennaID,
	out int status
)
```

```text
Public Function HciLEDirectionFindingReceiverTest ( 
	channelNumber As Integer,
	modulationIndex As BluetoothDtmModulationIndex,
	phy As BluetoothDtmReceiverPhy,
	directionFindingMode As BluetoothDtmDirectionFindingMode,
	switchingPatternLength As Integer,
	cteLength As Double,
	cteSlotDuration As Double,
	antennaID As Integer(),
	<OutAttribute> ByRef status As Integer
) As Integer
```

###### Parameters

- **channelNumber**
  - Type: SystemInt32 Specifies the Bluetooth transmit channel number of the generated signal. The default value is 0.
- **modulationIndex**
  - Type: NationalInstruments.BluetoothDtmBluetoothDtmModulationIndexSpecifies the type of modulation index at the generator. The default value is Standard.
- **phy**
  - Type: NationalInstruments.BluetoothDtmBluetoothDtmReceiverPhySpecifies the type of the packet to be transmitted by the physical layer of the DUT. The default value is Phy_1Mbps
- **directionFindingMode**
  - Type: NationalInstruments.BluetoothDtmBluetoothDtmDirectionFindingMode Specifies the mode of direction finding. The default value is Disabled
- **switchingPatternLength**
  - Type: SystemInt32 Specifies the length of the antenna switching pattern. The default value is 0.
- **cteLength**
  - Type: SystemDoubleSpecifies the length of the constant tone extension field in the generated signal. This value is expressed in seconds. This parameter is applicable only when you set the Direction Finding Mode parameter to either AngleofArrival or AngleofDeparture. The default value is 160 microseconds.
- **cteSlotDuration**
  - Type: SystemDoubleSpecifies the length of the antenna switching and sampling slots in the constant tone extension field. This value is expressed in seconds. The default value is 1 us. Valid values are 1 us and 2 us.
- **antennaID**
  - Type: SystemInt32 Specifies the array of Antenna IDs in the antenna switching pattern. The length of Antenna IDs array must be equal to Length Of Switching Pattern.
- **status**
  - Type: SystemInt32Returns the status of the receiver test command. The DUT receives and executes the receiver test command if the status parameter returns a 0x00 value. The receiver test command fails if the status parameter returns a non-zero (0x01-0xFF) value.

###### Return Value

Int32

##### See Also

###### Reference

NIBluetoothDtm Class

NationalInstruments.BluetoothDtm Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-for-bluetooth-test-dtm path=bluetoothdtmdotnet/html/57fd1edf-17bc-05d9-1be6-aa0d82e7e93c.htm language=enus -->
## TOPIC 00019: BluetoothDtmException Properties

- bundle_id: `rfmx-for-bluetooth-test-dtm`
- source_path: `bluetoothdtmdotnet/html/57fd1edf-17bc-05d9-1be6-aa0d82e7e93c.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-for-bluetooth-test-dtm/raw/resource/enus/bluetoothdtmdotnet/html/57fd1edf-17bc-05d9-1be6-aa0d82e7e93c.htm
- document_id: `rfmx-for-bluetooth-test-dtm`
- page_type: `leaf`
- content_type: ``

BluetoothDtmException Properties

### BluetoothDtmException Properties

The [BluetoothDtmException](1033e53e-d97f-06aa-be65-1ab6e39ea879.htm) type exposes the following members.

##### Properties

|  | Name | Description |
| --- | --- | --- |
|  | Data | Gets a collection of key/value pairs that provide additional user-defined information about the exception. (Inherited from Exception.) |
|  | HelpLink | Gets or sets a link to the help file associated with this exception. (Inherited from Exception.) |
|  | HResult | Gets or sets HRESULT, a coded numerical value that is assigned to a specific exception. (Inherited from Exception.) |
|  | InnerException | Gets the Exception instance that caused the current exception. (Inherited from Exception.) |
|  | Message | Gets a message that describes the current exception. (Inherited from Exception.) |
|  | Source | Gets or sets the name of the application or the object that causes the error. (Inherited from Exception.) |
|  | StackTrace | Gets a string representation of the immediate frames on the call stack. (Inherited from Exception.) |
|  | TargetSite | Gets the method that throws the current exception. (Inherited from Exception.) |

Top

##### See Also

###### Reference

BluetoothDtmException Class

NationalInstruments.BluetoothDtm Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-for-bluetooth-test-dtm path=bluetoothdtmdotnet/html/58693a32-0208-9c9e-c657-87d9ae018f8d.htm language=enus -->
## TOPIC 00020: NIBluetoothDtmHciLEDirectionFindingTransmitterTest Method

- bundle_id: `rfmx-for-bluetooth-test-dtm`
- source_path: `bluetoothdtmdotnet/html/58693a32-0208-9c9e-c657-87d9ae018f8d.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-for-bluetooth-test-dtm/raw/resource/enus/bluetoothdtmdotnet/html/58693a32-0208-9c9e-c657-87d9ae018f8d.htm
- document_id: `rfmx-for-bluetooth-test-dtm`
- page_type: `leaf`
- content_type: ``

NIBluetoothDtm.HciLEDirectionFindingTransmitterTest Method

### NIBluetoothDtmHciLEDirectionFindingTransmitterTest Method

Sends a command to the device under test (DUT) to start the transmitter test.

Namespace:

NationalInstruments.BluetoothDtm

Assembly:

##### Syntax

C#

VB

```text
public int HciLEDirectionFindingTransmitterTest(
	int channelNumber,
	int payloadLength,
	BluetoothDtmLEPatternType lePatternType,
	BluetoothDtmTransmitterPhy phy,
	BluetoothDtmDirectionFindingMode directionFindingMode,
	int switchingPatternLength,
	double cteLength,
	double cteSlotDuration,
	int[] antennaID,
	out int status
)
```

```text
Public Function HciLEDirectionFindingTransmitterTest ( 
	channelNumber As Integer,
	payloadLength As Integer,
	lePatternType As BluetoothDtmLEPatternType,
	phy As BluetoothDtmTransmitterPhy,
	directionFindingMode As BluetoothDtmDirectionFindingMode,
	switchingPatternLength As Integer,
	cteLength As Double,
	cteSlotDuration As Double,
	antennaID As Integer(),
	<OutAttribute> ByRef status As Integer
) As Integer
```

###### Parameters

- **channelNumber**
  - Type: SystemInt32 Specifies the Bluetooth transmit channel number of the generated signal. The default value is 0.
- **payloadLength**
  - Type: SystemInt32Specifies the length of payload data in each packet that the DUT transmits. This value is expressed in bytes. The default value is 37.
- **lePatternType**
  - Type: NationalInstruments.BluetoothDtmBluetoothDtmLEPatternTypeSpecifies the type of payload to use for the LE packet. Payload type values of Type_Prbs9, Type_11110000, and Type_10101010 must be supported by the DUT. The remaining payload type values are optional. The default value is Type_Prbs9.
- **phy**
  - Type: NationalInstruments.BluetoothDtmBluetoothDtmTransmitterPhySpecifies the type of the packet to be transmitted by the physical layer of the DUT. The default value is Phy_1Mbps
- **directionFindingMode**
  - Type: NationalInstruments.BluetoothDtmBluetoothDtmDirectionFindingModeSpecifies the mode of direction finding. The default value is Disabled.
- **switchingPatternLength**
  - Type: SystemInt32Specifies the length of the antenna switching pattern. The default value is 0.
- **cteLength**
  - Type: SystemDoubleSpecifies the length of the constant tone extension field in the generated signal. This value is expressed in seconds. This parameter is applicable only when you set the Direction Finding Mode parameter to either AngleofArrival or AngleofDeparture. The default value is 160 microseconds.
- **cteSlotDuration**
  - Type: SystemDoubleSpecifies the length of the antenna switching and sampling slots in the constant tone extension field. This value is expressed in seconds. The default value is 1 us.
- **antennaID**
  - Type: SystemInt32 Specifies the array of Antenna IDs in the antenna switching pattern. The length of Antenna IDs array must be equal to Length Of Switching Pattern.
- **status**
  - Type: SystemInt32Returns the status of the transmitter test command. The DUT receives and executes the transmitter test command if the status parameter returns a 0x00 value. The transmitter test command fails if the status parameter returns a non-zero (0x01-0xFF) value.

###### Return Value

Int32

##### See Also

###### Reference

NIBluetoothDtm Class

NationalInstruments.BluetoothDtm Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-for-bluetooth-test-dtm path=bluetoothdtmdotnet/html/5d328c4f-da0e-6245-0815-73bde0132c7d.htm language=enus -->
## TOPIC 00021: NIBluetoothDtmHciLEReceiverTest Method

- bundle_id: `rfmx-for-bluetooth-test-dtm`
- source_path: `bluetoothdtmdotnet/html/5d328c4f-da0e-6245-0815-73bde0132c7d.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-for-bluetooth-test-dtm/raw/resource/enus/bluetoothdtmdotnet/html/5d328c4f-da0e-6245-0815-73bde0132c7d.htm
- document_id: `rfmx-for-bluetooth-test-dtm`
- page_type: `leaf`
- content_type: ``

NIBluetoothDtm.HciLEReceiverTest Method

### NIBluetoothDtmHciLEReceiverTest Method

Sends a command to the device under test (DUT) to start the receiver test.

Namespace:

NationalInstruments.BluetoothDtm

Assembly:

##### Syntax

C#

VB

```text
public int HciLEReceiverTest(
	int channelNumber,
	out int status
)
```

```text
Public Function HciLEReceiverTest ( 
	channelNumber As Integer,
	<OutAttribute> ByRef status As Integer
) As Integer
```

###### Parameters

- **channelNumber**
  - Type: SystemInt32Specifies the Bluetooth transmit channel number of the generated signal. The default value is 0.
- **status**
  - Type: SystemInt32Returns the status of the receiver test command. The DUT receives and executes the receiver test command if the status parameter returns a 0x00 value. The receiver test command fails if the status parameter returns a non-zero (0x01-0xFF) value.

###### Return Value

Int32

##### Remarks

##### See Also

###### Reference

NIBluetoothDtm Class

NationalInstruments.BluetoothDtm Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-for-bluetooth-test-dtm path=bluetoothdtmdotnet/html/63333076-b82c-7c67-32f4-3396834093b5.htm language=enus -->
## TOPIC 00022: NIBluetoothDtmSetVisaTimeout Method

- bundle_id: `rfmx-for-bluetooth-test-dtm`
- source_path: `bluetoothdtmdotnet/html/63333076-b82c-7c67-32f4-3396834093b5.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-for-bluetooth-test-dtm/raw/resource/enus/bluetoothdtmdotnet/html/63333076-b82c-7c67-32f4-3396834093b5.htm
- document_id: `rfmx-for-bluetooth-test-dtm`
- page_type: `leaf`
- content_type: ``

NIBluetoothDtm.SetVisaTimeout Method

### NIBluetoothDtmSetVisaTimeout Method

Sets the timeout value, in milliseconds (ms), for the VISA session of the device under test (DUT), specified by the VISA resource name parameter.

Namespace:

NationalInstruments.BluetoothDtm

Assembly:

##### Syntax

C#

VB

```text
public int SetVisaTimeout(
	uint timeout
)
```

```text
Public Function SetVisaTimeout ( 
	timeout As UInteger
) As Integer
```

###### Parameters

- **timeout**
  - Type: SystemUInt32Specifies the minimum timeout value, in milliseconds (ms), to use when accessing the device. The default value is 2000.

###### Return Value

Int32

##### Remarks

##### See Also

###### Reference

NIBluetoothDtm Class

NationalInstruments.BluetoothDtm Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-for-bluetooth-test-dtm path=bluetoothdtmdotnet/html/63f2639e-385a-b69c-b4e4-9e0614803d34.htm language=enus -->
## TOPIC 00023: NIBluetoothDtmDispose Method

- bundle_id: `rfmx-for-bluetooth-test-dtm`
- source_path: `bluetoothdtmdotnet/html/63f2639e-385a-b69c-b4e4-9e0614803d34.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-for-bluetooth-test-dtm/raw/resource/enus/bluetoothdtmdotnet/html/63f2639e-385a-b69c-b4e4-9e0614803d34.htm
- document_id: `rfmx-for-bluetooth-test-dtm`
- page_type: `leaf`
- content_type: ``

NIBluetoothDtm.Dispose Method

### NIBluetoothDtmDispose Method

Closes the VISA session. Call this method a number of times equal to the number of times you obtained a reference to the VISA session for a particular resource name.

Namespace:

NationalInstruments.BluetoothDtm

Assembly:

##### Syntax

C#

VB

```text
public void Dispose()
```

```text
Public Sub Dispose
```

###### Implements

##### See Also

###### Reference

NIBluetoothDtm Class

NationalInstruments.BluetoothDtm Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-for-bluetooth-test-dtm path=bluetoothdtmdotnet/html/64542740-7a66-10a0-b546-d270b29eafb4.htm language=enus -->
## TOPIC 00024: BluetoothDtmException Constructor

- bundle_id: `rfmx-for-bluetooth-test-dtm`
- source_path: `bluetoothdtmdotnet/html/64542740-7a66-10a0-b546-d270b29eafb4.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-for-bluetooth-test-dtm/raw/resource/enus/bluetoothdtmdotnet/html/64542740-7a66-10a0-b546-d270b29eafb4.htm
- document_id: `rfmx-for-bluetooth-test-dtm`
- page_type: `leaf`
- content_type: ``

BluetoothDtmException Constructor

### BluetoothDtmException Constructor

BluetoothDtmException

Namespace:

NationalInstruments.BluetoothDtm

Assembly:

##### Syntax

C#

VB

```text
public BluetoothDtmException()
```

```text
Public Sub New
```

##### See Also

###### Reference

BluetoothDtmException Class

BluetoothDtmException Overload

NationalInstruments.BluetoothDtm Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-for-bluetooth-test-dtm path=bluetoothdtmdotnet/html/697a9951-75e5-0967-6249-e10942ea9b34.htm language=enus -->
## TOPIC 00025: BluetoothDtmStopBits Enumeration

- bundle_id: `rfmx-for-bluetooth-test-dtm`
- source_path: `bluetoothdtmdotnet/html/697a9951-75e5-0967-6249-e10942ea9b34.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-for-bluetooth-test-dtm/raw/resource/enus/bluetoothdtmdotnet/html/697a9951-75e5-0967-6249-e10942ea9b34.htm
- document_id: `rfmx-for-bluetooth-test-dtm`
- page_type: `leaf`
- content_type: ``

BluetoothDtmStopBits Enumeration

### BluetoothDtmStopBits Enumeration

specifies the number of stop bits used to indicate the end of a frame. The default value is StopBits1_0.

Namespace:

NationalInstruments.BluetoothDtm

Assembly:

##### Syntax

C#

VB

```text
public enum BluetoothDtmStopBits
```

```text
Public Enumeration BluetoothDtmStopBits
```

##### Members

|  | Member name | Value | Description |
| --- | --- | --- | --- |
|  | StopBits1_0 | 10 | Specifies that the number of stop bits used is 1. |
|  | StopBits1_5 | 15 | Specifies that the number of stop bits used is 1.5. |
|  | StopBits2_0 | 20 | Specifies that the number of stop bits used is 2. |

##### See Also

###### Reference

NationalInstruments.BluetoothDtm Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-for-bluetooth-test-dtm path=bluetoothdtmdotnet/html/73e9860a-beed-9fc2-90b8-50d3f5df2ecd.htm language=enus -->
## TOPIC 00026: BluetoothDtmFlowControl Enumeration

- bundle_id: `rfmx-for-bluetooth-test-dtm`
- source_path: `bluetoothdtmdotnet/html/73e9860a-beed-9fc2-90b8-50d3f5df2ecd.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-for-bluetooth-test-dtm/raw/resource/enus/bluetoothdtmdotnet/html/73e9860a-beed-9fc2-90b8-50d3f5df2ecd.htm
- document_id: `rfmx-for-bluetooth-test-dtm`
- page_type: `leaf`
- content_type: ``

BluetoothDtmFlowControl Enumeration

### BluetoothDtmFlowControl Enumeration

Specifies the flow control method used for transmitting and receiving data. The default value is RtsCts

Namespace:

NationalInstruments.BluetoothDtm

Assembly:

##### Syntax

C#

VB

```text
public enum BluetoothDtmFlowControl
```

```text
Public Enumeration BluetoothDtmFlowControl
```

##### Members

|  | Member name | Value | Description |
| --- | --- | --- | --- |
|  | None | 0 | Does not use flow control, and the buffers on both sides of the connection are assumed to be large enough to hold all the transferred data. |
|  | XOnXOff | 1 | Uses the XON and XOFF characters to complete flow control. The transfer mechanism controls input flow by transmitting XOFF when the low-level I/O receive buffer is nearly full, and it controls the output flow by suspending transmission when XOFF is received. |
|  | RtsCts | 2 | Uses the RTS output signal and the CTS input signal to complete flow control. The transfer mechanism controls input flow by unasserting the RTS signal when the low-level I/O receive buffer is nearly full. The transfer mechanism also controls output flow by suspending the transmission when the CTS signal is unasserted. |
|  | DtrDsr | 4 | Uses the DTR output signal and the DSR input signal to complete flow control. The transfer mechanism controls input flow by unasserting the DTR signal when the low-level I/O receive buffer is nearly full. The transfer mechanism also controls output flow by suspending the transmission when the DSR signal is unasserted. |

##### See Also

###### Reference

NationalInstruments.BluetoothDtm Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-for-bluetooth-test-dtm path=bluetoothdtmdotnet/html/8a57e438-a013-7327-32ed-d756fd0018e2.htm language=enus -->
## TOPIC 00027: BluetoothDtmException Constructor

- bundle_id: `rfmx-for-bluetooth-test-dtm`
- source_path: `bluetoothdtmdotnet/html/8a57e438-a013-7327-32ed-d756fd0018e2.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-for-bluetooth-test-dtm/raw/resource/enus/bluetoothdtmdotnet/html/8a57e438-a013-7327-32ed-d756fd0018e2.htm
- document_id: `rfmx-for-bluetooth-test-dtm`
- page_type: `leaf`
- content_type: ``

BluetoothDtmException Constructor

### BluetoothDtmException Constructor

##### Overload List

|  | Name | Description |
| --- | --- | --- |
|  | BluetoothDtmException | Initializes a new instance of the BluetoothDtmException class |
|  | BluetoothDtmException(String) | Initializes a new instance of the class BluetoothDtmException with a specified error message. |

Top

##### See Also

###### Reference

BluetoothDtmException Class

NationalInstruments.BluetoothDtm Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-for-bluetooth-test-dtm path=bluetoothdtmdotnet/html/9e97dcd5-45c2-9bd1-a084-cf714e139d89.htm language=enus -->
## TOPIC 00028: BluetoothDtmLEPatternType Enumeration

- bundle_id: `rfmx-for-bluetooth-test-dtm`
- source_path: `bluetoothdtmdotnet/html/9e97dcd5-45c2-9bd1-a084-cf714e139d89.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-for-bluetooth-test-dtm/raw/resource/enus/bluetoothdtmdotnet/html/9e97dcd5-45c2-9bd1-a084-cf714e139d89.htm
- document_id: `rfmx-for-bluetooth-test-dtm`
- page_type: `leaf`
- content_type: ``

BluetoothDtmLEPatternType Enumeration

### BluetoothDtmLEPatternType Enumeration

Specifies the type of payload to use for the LE packet. Payload type values of Type_Prbs9, Type_11110000, and Type_10101010 must be supported by the DUT. The remaining payload type values are optional. The default value is Type_Prbs9.

Namespace:

NationalInstruments.BluetoothDtm

Assembly:

##### Syntax

C#

VB

```text
public enum BluetoothDtmLEPatternType
```

```text
Public Enumeration BluetoothDtmLEPatternType
```

##### Members

|  | Member name | Value | Description |
| --- | --- | --- | --- |
|  | Type_Prbs9 | 0 | Specifies that the bit sequence is PRBS9. |
|  | Type_11110000 | 1 | Specifies that the bit sequence is 11110000. |
|  | Type_10101010 | 2 | Specifies that the bit sequence is 10101010. |
|  | Type_Prbs15 | 3 | Specifies that the bit sequence is PRBS15. |
|  | Type_11111111 | 4 | Specifies that the bit sequence is 11111111. |
|  | Type_00000000 | 5 | Specifies that the bit sequence is 00000000. |
|  | Type_00001111 | 6 | Specifies that the bit sequence is 00001111. |
|  | Type_01010101 | 7 | Specifies that the bit sequence is 01010101. |

##### See Also

###### Reference

NationalInstruments.BluetoothDtm Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-for-bluetooth-test-dtm path=bluetoothdtmdotnet/html/a0ab2a76-a8b5-47fe-8bf8-5e6015177eb8.htm language=enus -->
## TOPIC 00029: NIBluetoothDtmClose Method

- bundle_id: `rfmx-for-bluetooth-test-dtm`
- source_path: `bluetoothdtmdotnet/html/a0ab2a76-a8b5-47fe-8bf8-5e6015177eb8.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-for-bluetooth-test-dtm/raw/resource/enus/bluetoothdtmdotnet/html/a0ab2a76-a8b5-47fe-8bf8-5e6015177eb8.htm
- document_id: `rfmx-for-bluetooth-test-dtm`
- page_type: `leaf`
- content_type: ``

NIBluetoothDtm.Close Method

### NIBluetoothDtmClose Method

Closes a device session or the event object that you specify in the VISA resource name parameter.

Namespace:

NationalInstruments.BluetoothDtm

Assembly:

##### Syntax

C#

VB

```text
public void Close()
```

```text
Public Sub Close
```

###### Return Value

##### Remarks

##### See Also

###### Reference

NIBluetoothDtm Class

NationalInstruments.BluetoothDtm Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-for-bluetooth-test-dtm path=bluetoothdtmdotnet/html/a3392fa4-58eb-c58f-2fb9-2e28c11c7f64.htm language=enus -->
## TOPIC 00030: BluetoothDtmException Constructor (String)

- bundle_id: `rfmx-for-bluetooth-test-dtm`
- source_path: `bluetoothdtmdotnet/html/a3392fa4-58eb-c58f-2fb9-2e28c11c7f64.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-for-bluetooth-test-dtm/raw/resource/enus/bluetoothdtmdotnet/html/a3392fa4-58eb-c58f-2fb9-2e28c11c7f64.htm
- document_id: `rfmx-for-bluetooth-test-dtm`
- page_type: `leaf`
- content_type: ``

BluetoothDtmException Constructor (String)

### BluetoothDtmException Constructor (String)

Initializes a new instance of the class BluetoothDtmException with a specified error message.

Namespace:

NationalInstruments.BluetoothDtm

Assembly:

##### Syntax

C#

VB

```text
public BluetoothDtmException(
	string message
)
```

```text
Public Sub New ( 
	message As String
)
```

###### Parameters

- **message**
  - Type: SystemStringThe message that describes the error.

##### See Also

###### Reference

BluetoothDtmException Class

BluetoothDtmException Overload

NationalInstruments.BluetoothDtm Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-for-bluetooth-test-dtm path=bluetoothdtmdotnet/html/a8f4a810-413c-fa9d-655f-9fbcbb444c4b.htm language=enus -->
## TOPIC 00031: BluetoothDtmTransmitterPhy Enumeration

- bundle_id: `rfmx-for-bluetooth-test-dtm`
- source_path: `bluetoothdtmdotnet/html/a8f4a810-413c-fa9d-655f-9fbcbb444c4b.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-for-bluetooth-test-dtm/raw/resource/enus/bluetoothdtmdotnet/html/a8f4a810-413c-fa9d-655f-9fbcbb444c4b.htm
- document_id: `rfmx-for-bluetooth-test-dtm`
- page_type: `leaf`
- content_type: ``

BluetoothDtmTransmitterPhy Enumeration

### BluetoothDtmTransmitterPhy Enumeration

Specifies the type of the packet to be transmitted by the physical layer of the DUT. The default value is Phy_1Mbps.

Namespace:

NationalInstruments.BluetoothDtm

Assembly:

##### Syntax

C#

VB

```text
public enum BluetoothDtmTransmitterPhy
```

```text
Public Enumeration BluetoothDtmTransmitterPhy
```

##### Members

|  | Member name | Value | Description |
| --- | --- | --- | --- |
|  | Phy_1Mbps | 1 | Transmitter is set to use the LE 1M PHY. |
|  | Phy_2Mbps | 2 | Transmitter is set to use the LE 2M PHY. |
|  | Phy_Coded_125Kbps | 3 | Transmitter is set to use the LE Coded PHY with S = 8 data coding. |
|  | Phy_Coded_500Kbps | 4 | Transmitter is set to use the LE Coded PHY with S = 2 data coding. |

##### See Also

###### Reference

NationalInstruments.BluetoothDtm Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-for-bluetooth-test-dtm path=bluetoothdtmdotnet/html/a914417f-8fc8-8b7c-132f-c94c5897e375.htm language=enus -->
## TOPIC 00032: BluetoothDtmParity Enumeration

- bundle_id: `rfmx-for-bluetooth-test-dtm`
- source_path: `bluetoothdtmdotnet/html/a914417f-8fc8-8b7c-132f-c94c5897e375.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-for-bluetooth-test-dtm/raw/resource/enus/bluetoothdtmdotnet/html/a914417f-8fc8-8b7c-132f-c94c5897e375.htm
- document_id: `rfmx-for-bluetooth-test-dtm`
- page_type: `leaf`
- content_type: ``

BluetoothDtmParity Enumeration

### BluetoothDtmParity Enumeration

Specifies the parity bit used with each transmitted or received frame. The default value is None.

Namespace:

NationalInstruments.BluetoothDtm

Assembly:

##### Syntax

C#

VB

```text
public enum BluetoothDtmParity
```

```text
Public Enumeration BluetoothDtmParity
```

##### Members

|  | Member name | Value | Description |
| --- | --- | --- | --- |
|  | None | 0 | Specifies that the frame does not contain a parity bit. |
|  | Odd | 1 | Specifies that the parity is odd. |
|  | Even | 2 | Specifies that the parity is even. |
|  | Mark | 3 | Specifies that the parity bit is always 1. |
|  | Space | 4 | Specifies that the parity bit is always 0. |

##### See Also

###### Reference

NationalInstruments.BluetoothDtm Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-for-bluetooth-test-dtm path=bluetoothdtmdotnet/html/acb72f0d-e6a8-b92a-db82-0854d9889c68.htm language=enus -->
## TOPIC 00033: NationalInstruments.BluetoothDtm Namespace

- bundle_id: `rfmx-for-bluetooth-test-dtm`
- source_path: `bluetoothdtmdotnet/html/acb72f0d-e6a8-b92a-db82-0854d9889c68.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-for-bluetooth-test-dtm/raw/resource/enus/bluetoothdtmdotnet/html/acb72f0d-e6a8-b92a-db82-0854d9889c68.htm
- document_id: `rfmx-for-bluetooth-test-dtm`
- page_type: `leaf`
- content_type: ``

NationalInstruments.BluetoothDtm Namespace

### NationalInstruments.BluetoothDtm Namespace

##### Classes

|  | Class | Description |
| --- | --- | --- |
|  | BluetoothDtmException | Initializes a new instance of the BluetoothDtmException class with a specified error message. |
|  | NIBluetoothDtm | Defines a root class which is used to identify and control BluetoothDtm signal configuration. |

##### Enumerations

|  | Enumeration | Description |
| --- | --- | --- |
|  | BluetoothDtmDirectionFindingMode | Specifies the mode of direction finding. The default value is Disabled. |
|  | BluetoothDtmFlowControl | Specifies the flow control method used for transmitting and receiving data. The default value is RtsCts |
|  | BluetoothDtmLEPatternType | Specifies the type of payload to use for the LE packet. Payload type values of Type_Prbs9, Type_11110000, and Type_10101010 must be supported by the DUT. The remaining payload type values are optional. The default value is Type_Prbs9. |
|  | BluetoothDtmModulationIndex | Specifies the type of modulation index at the generator. The default value is Standard. |
|  | BluetoothDtmParity | Specifies the parity bit used with each transmitted or received frame. The default value is None. |
|  | BluetoothDtmReceiverPhy | Specifies the type of the generated packet by the physical layer of the DUT. The default value is Phy_1Mbps. |
|  | BluetoothDtmStopBits | specifies the number of stop bits used to indicate the end of a frame. The default value is StopBits1_0. |
|  | BluetoothDtmTransmitterPhy | Specifies the type of the packet to be transmitted by the physical layer of the DUT. The default value is Phy_1Mbps. |

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-for-bluetooth-test-dtm path=bluetoothdtmdotnet/html/bada242e-fb3a-d3a5-22b8-21043067cc35.htm language=enus -->
## TOPIC 00034: BluetoothDtmException Events

- bundle_id: `rfmx-for-bluetooth-test-dtm`
- source_path: `bluetoothdtmdotnet/html/bada242e-fb3a-d3a5-22b8-21043067cc35.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-for-bluetooth-test-dtm/raw/resource/enus/bluetoothdtmdotnet/html/bada242e-fb3a-d3a5-22b8-21043067cc35.htm
- document_id: `rfmx-for-bluetooth-test-dtm`
- page_type: `leaf`
- content_type: ``

BluetoothDtmException Events

### BluetoothDtmException Events

The [BluetoothDtmException](1033e53e-d97f-06aa-be65-1ab6e39ea879.htm) type exposes the following members.

##### Events

|  | Name | Description |
| --- | --- | --- |
|  | SerializeObjectState | Occurs when an exception is serialized to create an exception state object that contains serialized data about the exception. (Inherited from Exception.) |

Top

##### See Also

###### Reference

BluetoothDtmException Class

NationalInstruments.BluetoothDtm Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-for-bluetooth-test-dtm path=bluetoothdtmdotnet/html/c10728d9-0265-2c36-2c90-cc32553a9a51.htm language=enus -->
## TOPIC 00035: BluetoothDtmDirectionFindingMode Enumeration

- bundle_id: `rfmx-for-bluetooth-test-dtm`
- source_path: `bluetoothdtmdotnet/html/c10728d9-0265-2c36-2c90-cc32553a9a51.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-for-bluetooth-test-dtm/raw/resource/enus/bluetoothdtmdotnet/html/c10728d9-0265-2c36-2c90-cc32553a9a51.htm
- document_id: `rfmx-for-bluetooth-test-dtm`
- page_type: `leaf`
- content_type: ``

BluetoothDtmDirectionFindingMode Enumeration

### BluetoothDtmDirectionFindingMode Enumeration

Specifies the mode of direction finding. The default value is Disabled.

Namespace:

NationalInstruments.BluetoothDtm

Assembly:

##### Syntax

C#

VB

```text
public enum BluetoothDtmDirectionFindingMode
```

```text
Public Enumeration BluetoothDtmDirectionFindingMode
```

##### Members

|  | Member name | Value | Description |
| --- | --- | --- | --- |
|  | Disabled | 0 | Specifies that the LE packet does not have fields required for direction finding. |
|  | AngleOfArrival | 1 | Specifies the LE packets uses the angle of arrival method of direction finding. |
|  | AngleOfDeparture | 2 | Specifies the LE packet uses angle of departure method of direction finding. |

##### See Also

###### Reference

NationalInstruments.BluetoothDtm Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-for-bluetooth-test-dtm path=bluetoothdtmdotnet/html/e2d52a66-bb45-5ab7-3e65-3611e6154a55.htm language=enus -->
## TOPIC 00036: NIBluetoothDtmHciLETransmitterTest Method

- bundle_id: `rfmx-for-bluetooth-test-dtm`
- source_path: `bluetoothdtmdotnet/html/e2d52a66-bb45-5ab7-3e65-3611e6154a55.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-for-bluetooth-test-dtm/raw/resource/enus/bluetoothdtmdotnet/html/e2d52a66-bb45-5ab7-3e65-3611e6154a55.htm
- document_id: `rfmx-for-bluetooth-test-dtm`
- page_type: `leaf`
- content_type: ``

NIBluetoothDtm.HciLETransmitterTest Method

### NIBluetoothDtmHciLETransmitterTest Method

Sends a command to the device under test (DUT) to start the transmitter test.

Namespace:

NationalInstruments.BluetoothDtm

Assembly:

##### Syntax

C#

VB

```text
public int HciLETransmitterTest(
	int channelNumber,
	int payloadLengthBytes,
	BluetoothDtmLEPatternType lePatternType,
	out int status
)
```

```text
Public Function HciLETransmitterTest ( 
	channelNumber As Integer,
	payloadLengthBytes As Integer,
	lePatternType As BluetoothDtmLEPatternType,
	<OutAttribute> ByRef status As Integer
) As Integer
```

###### Parameters

- **channelNumber**
  - Type: SystemInt32Specifies the Bluetooth transmit channel number of the signal generated by the DUT. The default value is 0.
- **payloadLengthBytes**
  - Type: SystemInt32Specifies the length, in bytes, of payload data in each packet that the DUT transmits. The default value is 37.
- **lePatternType**
  - Type: NationalInstruments.BluetoothDtmBluetoothDtmLEPatternTypeSpecifies the type of payload to use for the LE packet. Payload type values of Type_Prbs9, Type_11110000, and Type_10101010 must be supported by the DUT. The remaining payload type values are optional. The default value is Type_Prbs9.
- **status**
  - Type: SystemInt32Returns the status of the transmitter test command. The DUT receives and executes the transmitter test command if the status parameter returns a 0x00 value. The transmitter test command fails if the status parameter returns a non-zero (0x01-0xFF) value.

###### Return Value

Int32

##### Remarks

##### See Also

###### Reference

NIBluetoothDtm Class

NationalInstruments.BluetoothDtm Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-for-bluetooth-test-dtm path=bluetoothdtmdotnet/html/e77ccc1f-09cd-7c61-0a38-6729217f3e3b.htm language=enus -->
## TOPIC 00037: NIBluetoothDtmHciReset Method

- bundle_id: `rfmx-for-bluetooth-test-dtm`
- source_path: `bluetoothdtmdotnet/html/e77ccc1f-09cd-7c61-0a38-6729217f3e3b.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-for-bluetooth-test-dtm/raw/resource/enus/bluetoothdtmdotnet/html/e77ccc1f-09cd-7c61-0a38-6729217f3e3b.htm
- document_id: `rfmx-for-bluetooth-test-dtm`
- page_type: `leaf`
- content_type: ``

NIBluetoothDtm.HciReset Method

### NIBluetoothDtmHciReset Method

Resets the device under test (DUT) specified by the VISA resource name parameter.

Namespace:

NationalInstruments.BluetoothDtm

Assembly:

##### Syntax

C#

VB

```text
public int HciReset(
	out int status
)
```

```text
Public Function HciReset ( 
	<OutAttribute> ByRef status As Integer
) As Integer
```

###### Parameters

- **status**
  - Type: SystemInt32Returns the status of the reset command. The DUT receives and executes the reset command if the status parameter returns a 0x00 value. The reset command fails if the parameter returns a non-zero (0x01-0xFF) value.

###### Return Value

Int32

##### Remarks

##### See Also

###### Reference

NIBluetoothDtm Class

NationalInstruments.BluetoothDtm Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-for-bluetooth-test-dtm path=bluetoothdtmdotnet/html/ec5a93a7-0f5f-9b9b-07c6-e969655406d9.htm language=enus -->
## TOPIC 00038: BluetoothDtmReceiverPhy Enumeration

- bundle_id: `rfmx-for-bluetooth-test-dtm`
- source_path: `bluetoothdtmdotnet/html/ec5a93a7-0f5f-9b9b-07c6-e969655406d9.htm`
- source_url: https://docs-be.ni.com/bundle/rfmx-for-bluetooth-test-dtm/raw/resource/enus/bluetoothdtmdotnet/html/ec5a93a7-0f5f-9b9b-07c6-e969655406d9.htm
- document_id: `rfmx-for-bluetooth-test-dtm`
- page_type: `leaf`
- content_type: ``

BluetoothDtmReceiverPhy Enumeration

### BluetoothDtmReceiverPhy Enumeration

Specifies the type of the generated packet by the physical layer of the DUT. The default value is Phy_1Mbps.

Namespace:

NationalInstruments.BluetoothDtm

Assembly:

##### Syntax

C#

VB

```text
public enum BluetoothDtmReceiverPhy
```

```text
Public Enumeration BluetoothDtmReceiverPhy
```

##### Members

|  | Member name | Value | Description |
| --- | --- | --- | --- |
|  | Phy_1Mbps | 1 | Receiver is set to use the LE 1M PHY. |
|  | Phy_2Mbps | 2 | Receiver is set to use the LE 2M PHY. |
|  | Phy_Coded | 3 | Receiver is set to use the Coded PHY. |

##### See Also

###### Reference

NationalInstruments.BluetoothDtm Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=rfmx-for-bluetooth-test-dtm path=cvibluetoothdtm/cvinibluetoothdtm_createcustomcommand.html language=enus -->
## TOPIC 00039: niBluetoothDTM_CreateCustomCommand

- bundle_id: `rfmx-for-bluetooth-test-dtm`
- source_path: `cvibluetoothdtm/cvinibluetoothdtm_createcustomcommand.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-for-bluetooth-test-dtm/raw/resource/enus/cvibluetoothdtm/cvinibluetoothdtm_createcustomcommand.html
- document_id: `rfmx-for-bluetooth-test-dtm`
- page_type: `leaf`
- content_type: ``

### niBluetoothDTM_CreateCustomCommand

int32 __stdcall niBluetoothDTM_CreateCustomCommand (niBluetoothDTMSession* session,
 int32 opCode[],
 int32 opCodeLength,
 int32 commandParameters[],
 int32 commandParametersLength,
 int32 returnParameters[],
 int32 arraySize,
 int32 *actualArraySize);

#### Purpose

Sends the specified custom command to the device under test (DUT).

#### Parameters

| Input |  |  |
| --- | --- | --- |
| Name | Type | Description |
| session | niBluetoothDTMSession | Specifies the name of the communication port to which the DUT is connected. |
| opCode | int32[] | Specifies the opcode of the custom commands to send to the DUT. |
| opCodeLength | int32 | Specifies the length of the opCode array. |
| commandParameters | int32[] | Specifies an array of the input parameters required for the custom command. |
| commandParametersLength | int32 | Specifies the length of the commandParameters array. |
| arraySize | int32 | Specifies the size of the array. Set the arraySize parameter to 0 to get the size of all the arrays in the actualArraySize parameter. |
| Output |  |  |
| Name | Type | Description |
| returnParameters | int32[] | Returns an array of the parameters sent by the DUT in response to the custom command. |
| actualArraySize | int32* | Returns the actual size of the array, if you pass NULL to returnParameters array, and set the arraySize parameter to 0. |

#### Return Value

| Name | Type | Description |
| --- | --- | --- |
| returnValue | int32 | Returns the status code of this operation. The status code either indicates success or describes an error or warning. Examine the status code from each call to an niBluetoothDTM function to determine if an error has occurred. The general meaning of the status code is as follows: Value Meaning 0 Success Positive Values Warnings Negative Values Errors |
| Value | Meaning |  |
| 0 | Success |  |
| Positive Values | Warnings |  |
| Negative Values | Errors |  |
|  |  |  |

<!--NI_TOPIC bundle=rfmx-for-bluetooth-test-dtm path=cvibluetoothdtm/cvinibluetoothdtm_hciledirectionfindingreceivertest.html language=enus -->
## TOPIC 00040: niBluetoothDTM_HCILEDirectionFindingReceiverTest

- bundle_id: `rfmx-for-bluetooth-test-dtm`
- source_path: `cvibluetoothdtm/cvinibluetoothdtm_hciledirectionfindingreceivertest.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-for-bluetooth-test-dtm/raw/resource/enus/cvibluetoothdtm/cvinibluetoothdtm_hciledirectionfindingreceivertest.html
- document_id: `rfmx-for-bluetooth-test-dtm`
- page_type: `leaf`
- content_type: ``

### niBluetoothDTM_HCILEDirectionFindingReceiverTest

int32 __stdcall niBluetoothDTM_HCILEDirectionFindingReceiverTest(
 niBluetoothDTMSession session,
 int32 channelNumber,
 int32 modulationIndex,
 int32 PHY,
 int32 directionFindingMode,
 int32 switchingPatternLength,
 float64 CTELength,
 float64 CTESlotDuration,
 int32 antennaID[],
 int32 antennaIDArraySize,
 int32 *status);

#### Purpose

Sends the command to the device under test (DUT) to start the receiver test.

#### Parameters

| Input |  |  |
| --- | --- | --- |
| Name | Type | Description |
| session | niBluetoothDTMSession | Specifies the name of the communication port to which the DUT is connected. |
| channelNumber | int32 | Specifies the Bluetooth transmit channel number of the generated signal. The default value is 0. |
| modulationIndex | int32 | Specifies the type of modulation index at the generator. The default value is NIBLUETOOTHDTM_VAL_MODULATION_INDEX_STANDARD. NIBLUETOOTHDTM_VAL_MODULATION_INDEX_STANDARD (0) The packets are generated with standard modulation index. NIBLUETOOTHDTM_VAL_MODULATION_INDEX_STABLE (1) The packets are generated with stable modulation index. |
| NIBLUETOOTHDTM_VAL_MODULATION_INDEX_STANDARD (0) | The packets are generated with standard modulation index. |  |
| NIBLUETOOTHDTM_VAL_MODULATION_INDEX_STABLE (1) | The packets are generated with stable modulation index. |  |
| PHY | int32 | Specifies the type of the generated packet by the physical layer of the DUT. The default value is NIBLUETOOTHDTM_VAL_RECEIVER_PHY_1MBPS. NIBLUETOOTHDTM_VAL_RECEIVER_PHY_1MBPS (0) Receiver is set to use the LE 1M PHY. NIBLUETOOTHDTM_VAL_RECEIVER_PHY_2MBPS (1) Receiver is set to use the LE 2M PHY. NIBLUETOOTHDTM_VAL_RECEIVER_PHY_CODED (2) Receiver is set to use the Coded PHY. |
| NIBLUETOOTHDTM_VAL_RECEIVER_PHY_1MBPS (0) | Receiver is set to use the LE 1M PHY. |  |
| NIBLUETOOTHDTM_VAL_RECEIVER_PHY_2MBPS (1) | Receiver is set to use the LE 2M PHY. |  |
| NIBLUETOOTHDTM_VAL_RECEIVER_PHY_CODED (2) | Receiver is set to use the Coded PHY. |  |
| directionFindingMode | int32 | Specifies the mode of direction finding. The default value is NIBLUETOOTHDTM_VAL_DIRECTION_FINDING_MODE_DISABLED. NIBLUETOOTHDTM_VAL_DIRECTION_FINDING_MODE_DISABLED (0) Specifies that the LE packet does not have fields required for direction finding. NIBLUETOOTHDTM_VAL_DIRECTION_FINDING_MODE_ANGLE_OF_ARRIVAL (1) Specifies the LE packets uses the angle of arrival method of direction finding. NIBLUETOOTHDTM_VAL_DIRECTION_FINDING_MODE_ANGLE_OF_DEPARTURE (2) Specifies the LE packet uses angle of departure method of direction finding. |
| NIBLUETOOTHDTM_VAL_DIRECTION_FINDING_MODE_DISABLED (0) | Specifies that the LE packet does not have fields required for direction finding. |  |
| NIBLUETOOTHDTM_VAL_DIRECTION_FINDING_MODE_ANGLE_OF_ARRIVAL (1) | Specifies the LE packets uses the angle of arrival method of direction finding. |  |
| NIBLUETOOTHDTM_VAL_DIRECTION_FINDING_MODE_ANGLE_OF_DEPARTURE (2) | Specifies the LE packet uses angle of departure method of direction finding. |  |
| lengthOfSwitchingPattern | int32 | Specifies the length of the antenna switching pattern. The default value is 0. |
| CTELength | float64 | Specifies specifies the length of the constant tone extension field in the generated signal. This value is expressed in seconds. This parameter is applicable only when you set the directionFindingMode parameter to either NIBLUETOOTHDTM_VAL_DIRECTION_FINDING_MODE_ANGLE_OF_ARRIVAL or NIBLUETOOTHDTM_VAL_DIRECTION_FINDING_MODE_ANGLE_OF_DEPARTURE. The default value is 160 microseconds. |
| CTESlotDuration | float64 | Specifies the length of the antenna switching and sampling slots in the constant tone extension field. This value is expressed in seconds. The default value is 1 us. Valid values are 1 us and 2 us. |
| antennaID | int32[] | Specifies the array of Antenna IDs in the antenna switching pattern. The length of Antenna IDs array must be equal to Length Of Switching Pattern parameter. |
| antennaIDArraySize | int32 | Specifies size of antennaID parameter. |
| Output |  |  |
| Name | Type | Description |
| status | int32 | Returns the status of the receiver test command. The DUT receives and executes the receiver test command if the status parameter returns a 0x00 value. The receiver test command fails if the status parameter returns a non-zero (0x01-0xFF) value. |

#### Return Value

| Name | Type | Description |
| --- | --- | --- |
| returnValue | int32 | Returns the status code of this operation. The status code either indicates success or describes an error or warning. Examine the status code from each call to an niBluetoothDTM function to determine if an error has occurred. The general meaning of the status code is as follows: Value Meaning 0 Success Positive Values Warnings Negative Values Errors |
| Value | Meaning |  |
| 0 | Success |  |
| Positive Values | Warnings |  |
| Negative Values | Errors |  |
|  |  |  |

<!--NI_TOPIC bundle=rfmx-for-bluetooth-test-dtm path=cvibluetoothdtm/cvinibluetoothdtm_hciledirectionfindingtransmittertest.html language=enus -->
## TOPIC 00041: niBluetoothDTM_HCILEDirectionFindingTransmitterTest

- bundle_id: `rfmx-for-bluetooth-test-dtm`
- source_path: `cvibluetoothdtm/cvinibluetoothdtm_hciledirectionfindingtransmittertest.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-for-bluetooth-test-dtm/raw/resource/enus/cvibluetoothdtm/cvinibluetoothdtm_hciledirectionfindingtransmittertest.html
- document_id: `rfmx-for-bluetooth-test-dtm`
- page_type: `leaf`
- content_type: ``

### niBluetoothDTM_HCILEDirectionFindingTransmitterTest

int32 __stdcall niBluetoothDTM_HCILEDirectionFindingTransmitterTest(
 niBluetoothDTMSession session,
 int32 channelNumber,
 int32 payloadLength,
 int32 LEPatternType,
 int32 PHY,
 int32 directionFindingMode,
 int32 switchingPatternLength,
 float64 CTELength,
 float64 CTESlotDuration,
 int32 antennaID[],
 int32 antennaIDArraySize,
 int32 *status);

#### Purpose

Sends the command to the device under test (DUT) to start the transmitter test.

#### Parameters

| Input |  |  |
| --- | --- | --- |
| Name | Type | Description |
| session | niBluetoothDTMSession | Specifies the name of the communication port to which the DUT is connected. |
| channelNumber | int32 | Specifies the Bluetooth transmit channel number of the generated signal. The default value is 0. |
| payloadLength | int32 | Specifies the length of payload data in each packet that the DUT transmits. This value is expressed in bytes. The default value is 37. |
| LEPatternType | int32 | Specifies the type of payload to use for the LE packet. Payload type values of NIBLUETOOTHDTM_VAL_LE_PATTERN_TYPE_PRBS9, NIBLUETOOTHDTM_VAL_LE_PATTERN_TYPE_11110000, and NIBLUETOOTHDTM_VAL_LE_PATTERN_TYPE_10101010 must be supported by the DUT. The remaining payload type values are optional. The default value is NIBLUETOOTHDTM_VAL_LE_PATTERN_TYPE_PRBS9. NIBLUETOOTHDTM_VAL_LE_PATTERN_TYPE_PRBS9 (0) Specifies that the bit sequence is PRBS9. NIBLUETOOTHDTM_VAL_LE_PATTERN_TYPE_11110000 (1) Specifies that the bit sequence is 11110000. NIBLUETOOTHDTM_VAL_LE_PATTERN_TYPE_10101010 (2) Specifies that the bit sequence is 10101010. NIBLUETOOTHDTM_VAL_LE_PATTERN_TYPE_PRBS15 (3) Specifies that the bit sequence is PRBS15. NIBLUETOOTHDTM_VAL_LE_PATTERN_TYPE_11111111 (4) Specifies that the bit sequence is 11111111. NIBLUETOOTHDTM_VAL_LE_PATTERN_TYPE_00000000 (5) Specifies that the bit sequence is 00000000. NIBLUETOOTHDTM_VAL_LE_PATTERN_TYPE_00001111 (6) Specifies that the bit sequence is 00001111. NIBLUETOOTHDTM_VAL_LE_PATTERN_TYPE_01010101 (7) Specifies that the bit sequence is 01010101. |
| NIBLUETOOTHDTM_VAL_LE_PATTERN_TYPE_PRBS9 (0) | Specifies that the bit sequence is PRBS9. |  |
| NIBLUETOOTHDTM_VAL_LE_PATTERN_TYPE_11110000 (1) | Specifies that the bit sequence is 11110000. |  |
| NIBLUETOOTHDTM_VAL_LE_PATTERN_TYPE_10101010 (2) | Specifies that the bit sequence is 10101010. |  |
| NIBLUETOOTHDTM_VAL_LE_PATTERN_TYPE_PRBS15 (3) | Specifies that the bit sequence is PRBS15. |  |
| NIBLUETOOTHDTM_VAL_LE_PATTERN_TYPE_11111111 (4) | Specifies that the bit sequence is 11111111. |  |
| NIBLUETOOTHDTM_VAL_LE_PATTERN_TYPE_00000000 (5) | Specifies that the bit sequence is 00000000. |  |
| NIBLUETOOTHDTM_VAL_LE_PATTERN_TYPE_00001111 (6) | Specifies that the bit sequence is 00001111. |  |
| NIBLUETOOTHDTM_VAL_LE_PATTERN_TYPE_01010101 (7) | Specifies that the bit sequence is 01010101. |  |
| PHY | int32 | Specifies the type of the packet to be transmitted by the physical layer of the DUT. The default is NIBLUETOOTHDTM_VAL_TRANSMITTER_PHY_1MBPS. NIBLUETOOTHDTM_VAL_TRANSMITTER_PHY_1MBPS (0) Transmitter is set to use the LE 1M PHY. NIBLUETOOTHDTM_VAL_TRANSMITTER_PHY_2MBPS (1) Transmitter is set to use the LE 2M PHY. NIBLUETOOTHDTM_VAL_TRANSMITTER_PHY_CODED_125KBPS (2) Transmitter is set to use the LE Coded PHY with S = 8 data coding. NIBLUETOOTHDTM_VAL_TRANSMITTER_PHY_CODED_500KBPS (3) Transmitter is set to use the LE Coded PHY with S = 2 data coding. |
| NIBLUETOOTHDTM_VAL_TRANSMITTER_PHY_1MBPS (0) | Transmitter is set to use the LE 1M PHY. |  |
| NIBLUETOOTHDTM_VAL_TRANSMITTER_PHY_2MBPS (1) | Transmitter is set to use the LE 2M PHY. |  |
| NIBLUETOOTHDTM_VAL_TRANSMITTER_PHY_CODED_125KBPS (2) | Transmitter is set to use the LE Coded PHY with S = 8 data coding. |  |
| NIBLUETOOTHDTM_VAL_TRANSMITTER_PHY_CODED_500KBPS (3) | Transmitter is set to use the LE Coded PHY with S = 2 data coding. |  |
| directionFindingMode | int32 | Specifies the mode of direction finding. The default value is NIBLUETOOTHDTM_VAL_DIRECTION_FINDING_MODE_DISABLED. NIBLUETOOTHDTM_VAL_DIRECTION_FINDING_MODE_DISABLED (0) Specifies that the LE packet does not have fields required for direction finding. NIBLUETOOTHDTM_VAL_DIRECTION_FINDING_MODE_ANGLE_OF_ARRIVAL (1) Specifies the LE packets uses the angle of arrival method of direction finding. NIBLUETOOTHDTM_VAL_DIRECTION_FINDING_MODE_ANGLE_OF_DEPARTURE (2) Specifies the LE packet uses angle of departure method of direction finding. |
| NIBLUETOOTHDTM_VAL_DIRECTION_FINDING_MODE_DISABLED (0) | Specifies that the LE packet does not have fields required for direction finding. |  |
| NIBLUETOOTHDTM_VAL_DIRECTION_FINDING_MODE_ANGLE_OF_ARRIVAL (1) | Specifies the LE packets uses the angle of arrival method of direction finding. |  |
| NIBLUETOOTHDTM_VAL_DIRECTION_FINDING_MODE_ANGLE_OF_DEPARTURE (2) | Specifies the LE packet uses angle of departure method of direction finding. |  |
| switchingPatternLength | int32 | Specifies the length of the antenna switching pattern. The default value is 0. |
| CTELength | float64 | Specifies the length of the constant tone extension field in the generated signal. This value is expressed in seconds. This parameter is applicable only when you set the directionFindingMode parameter to either NIBLUETOOTHDTM_VAL_DIRECTION_FINDING_MODE_ANGLE_OF_ARRIVAL or NIBLUETOOTHDTM_VAL_DIRECTION_FINDING_MODE_ANGLE_OF_DEPARTURE. The default value is 160 microseconds. |
| CTESlotDuration | float64 | Specifies the length of the antenna switching and sampling slots in the constant tone extension field. This value is expressed in seconds. The default value is 1 us. |
| antennaID | int32[] | Specifies the array of Antenna IDs in the antenna switching pattern. The length of Antenna IDs array must be equal to length of the switching pattern. |
| antennaIDArraySize | int32 | Specifies the size of the array. |
| Output |  |  |
| Name | Type | Description |
| status | int32 | Returns the status of the transmitter test command. The DUT receives and executes the transmitter test command if the status parameter returns a 0x00 value. The transmitter test command fails if the status parameter returns a non-zero (0x01-0xFF) value. |

#### Return Value

| Name | Type | Description |
| --- | --- | --- |
| returnValue | int32 | Returns the status code of this operation. The status code either indicates success or describes an error or warning. Examine the status code from each call to an niBluetoothDTM function to determine if an error has occurred. The general meaning of the status code is as follows: Value Meaning 0 Success Positive Values Warnings Negative Values Errors |
| Value | Meaning |  |
| 0 | Success |  |
| Positive Values | Warnings |  |
| Negative Values | Errors |  |
|  |  |  |

<!--NI_TOPIC bundle=rfmx-for-bluetooth-test-dtm path=cvibluetoothdtm/cvinibluetoothdtm_hcileenhancedreceivertest.html language=enus -->
## TOPIC 00042: niBluetoothDTM_HCILEEnhancedReceiverTest

- bundle_id: `rfmx-for-bluetooth-test-dtm`
- source_path: `cvibluetoothdtm/cvinibluetoothdtm_hcileenhancedreceivertest.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-for-bluetooth-test-dtm/raw/resource/enus/cvibluetoothdtm/cvinibluetoothdtm_hcileenhancedreceivertest.html
- document_id: `rfmx-for-bluetooth-test-dtm`
- page_type: `leaf`
- content_type: ``

### niBluetoothDTM_HCILEEnhancedReceiverTest

int32 __stdcall niBluetoothDTM_HCILEEnhancedReceiverTest(
 niBluetoothDTMSession session,
 int32 channelNumber,
 int32 modulationIndex,
 int32 PHY,
 int32 *status);

#### Purpose

Sends the command to the device under test (DUT) to start the receiver test.

#### Parameters

| Input |  |  |
| --- | --- | --- |
| Name | Type | Description |
| session | niBluetoothDTMSession | Specifies the name of the communication port to which the DUT is connected. |
| channelNumber | int32 | Specifies the Bluetooth transmit channel number of the generated signal. The default value is 0. |
| modulationIndex | int32 | Specifies the type of modulation index at the generator. The default value is NIBLUETOOTHDTM_VAL_MODULATION_INDEX_STANDARD. NIBLUETOOTHDTM_VAL_MODULATION_INDEX_STANDARD (0) The packets are generated with standard modulation index. NIBLUETOOTHDTM_VAL_MODULATION_INDEX_STABLE (1) The packets are generated with stable modulation index. |
| NIBLUETOOTHDTM_VAL_MODULATION_INDEX_STANDARD (0) | The packets are generated with standard modulation index. |  |
| NIBLUETOOTHDTM_VAL_MODULATION_INDEX_STABLE (1) | The packets are generated with stable modulation index. |  |
| PHY | int32 | Specifies the type of the generated packet by the physical layer of the DUT. The default value is NIBLUETOOTHDTM_VAL_RECEIVER_PHY_1MBPS. NIBLUETOOTHDTM_VAL_RECEIVER_PHY_1MBPS (0) Receiver is set to use the LE 1M PHY. NIBLUETOOTHDTM_VAL_RECEIVER_PHY_2MBPS (1) Receiver is set to use the LE 2M PHY. NIBLUETOOTHDTM_VAL_RECEIVER_PHY_CODED (2) Receiver is set to use the Coded PHY. |
| NIBLUETOOTHDTM_VAL_RECEIVER_PHY_1MBPS (0) | Receiver is set to use the LE 1M PHY. |  |
| NIBLUETOOTHDTM_VAL_RECEIVER_PHY_2MBPS (1) | Receiver is set to use the LE 2M PHY. |  |
| NIBLUETOOTHDTM_VAL_RECEIVER_PHY_CODED (2) | Receiver is set to use the Coded PHY. |  |
| Output |  |  |
| Name | Type | Description |
| status | int32 | Returns the status of the receiver test command. The DUT receives and executes the receiver test command if the status parameter returns a 0x00 value. The receiver test command fails if the status parameter returns a non-zero (0x01-0xFF) value. |

#### Return Value

| Name | Type | Description |
| --- | --- | --- |
| returnValue | int32 | Returns the status code of this operation. The status code either indicates success or describes an error or warning. Examine the status code from each call to an niBluetoothDTM function to determine if an error has occurred. The general meaning of the status code is as follows: Value Meaning 0 Success Positive Values Warnings Negative Values Errors |
| Value | Meaning |  |
| 0 | Success |  |
| Positive Values | Warnings |  |
| Negative Values | Errors |  |
|  |  |  |

<!--NI_TOPIC bundle=rfmx-for-bluetooth-test-dtm path=cvibluetoothdtm/cvinibluetoothdtm_hcileenhancedtransmittertest.html language=enus -->
## TOPIC 00043: niBluetoothDTM_HCILEEnhancedTransmitterTest

- bundle_id: `rfmx-for-bluetooth-test-dtm`
- source_path: `cvibluetoothdtm/cvinibluetoothdtm_hcileenhancedtransmittertest.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-for-bluetooth-test-dtm/raw/resource/enus/cvibluetoothdtm/cvinibluetoothdtm_hcileenhancedtransmittertest.html
- document_id: `rfmx-for-bluetooth-test-dtm`
- page_type: `leaf`
- content_type: ``

### niBluetoothDTM_HCILEEnhancedTransmitterTest

int32 __stdcall niBluetoothDTM_HCILEEnhancedTransmitterTest(
 niBluetoothDTMSession session,
 int32 channelNumber,
 int32 payloadLengthBytes,
 int32 LEPatternType,
 int32 PHY,
 int32 *status);

#### Purpose

Sends the command to the device under test (DUT) to start the transmitter test.

#### Parameters

| Input |  |  |
| --- | --- | --- |
| Name | Type | Description |
| session | niBluetoothDTMSession | Specifies the name of the communication port to which the DUT is connected. |
| channelNumber | int32 | Specifies the Bluetooth transmit channel number of the signal generated by the DUT. The default value is 0. |
| payloadLengthBytes | int32 | Specifies the length, in bytes, of payload data in each packet that the DUT transmits. The default value is 37. |
| LEPatternType | int32 | Specifies the type of payload to use for the LE packet. Payload type values of NIBLUETOOTHDTM_VAL_LE_PATTERN_TYPE_PRBS9, NIBLUETOOTHDTM_VAL_LE_PATTERN_TYPE_11110000, and NIBLUETOOTHDTM_VAL_LE_PATTERN_TYPE_10101010 must be supported by the DUT. The remaining payload type values are optional. The default value is NIBLUETOOTHDTM_VAL_LE_PATTERN_TYPE_PRBS9. NIBLUETOOTHDTM_VAL_LE_PATTERN_TYPE_PRBS9 (0) Specifies that the bit sequence is PRBS9. NIBLUETOOTHDTM_VAL_LE_PATTERN_TYPE_11110000 (1) Specifies that the bit sequence is 11110000. NIBLUETOOTHDTM_VAL_LE_PATTERN_TYPE_10101010 (2) Specifies that the bit sequence is 10101010. NIBLUETOOTHDTM_VAL_LE_PATTERN_TYPE_PRBS15 (3) Specifies that the bit sequence is PRBS15. NIBLUETOOTHDTM_VAL_LE_PATTERN_TYPE_11111111 (4) Specifies that the bit sequence is 11111111. NIBLUETOOTHDTM_VAL_LE_PATTERN_TYPE_00000000 (5) Specifies that the bit sequence is 00000000. NIBLUETOOTHDTM_VAL_LE_PATTERN_TYPE_00001111 (6) Specifies that the bit sequence is 00001111. NIBLUETOOTHDTM_VAL_LE_PATTERN_TYPE_01010101 (7) Specifies that the bit sequence is 01010101. |
| NIBLUETOOTHDTM_VAL_LE_PATTERN_TYPE_PRBS9 (0) | Specifies that the bit sequence is PRBS9. |  |
| NIBLUETOOTHDTM_VAL_LE_PATTERN_TYPE_11110000 (1) | Specifies that the bit sequence is 11110000. |  |
| NIBLUETOOTHDTM_VAL_LE_PATTERN_TYPE_10101010 (2) | Specifies that the bit sequence is 10101010. |  |
| NIBLUETOOTHDTM_VAL_LE_PATTERN_TYPE_PRBS15 (3) | Specifies that the bit sequence is PRBS15. |  |
| NIBLUETOOTHDTM_VAL_LE_PATTERN_TYPE_11111111 (4) | Specifies that the bit sequence is 11111111. |  |
| NIBLUETOOTHDTM_VAL_LE_PATTERN_TYPE_00000000 (5) | Specifies that the bit sequence is 00000000. |  |
| NIBLUETOOTHDTM_VAL_LE_PATTERN_TYPE_00001111 (6) | Specifies that the bit sequence is 00001111. |  |
| NIBLUETOOTHDTM_VAL_LE_PATTERN_TYPE_01010101 (7) | Specifies that the bit sequence is 01010101. |  |
| PHY | int32 | Specifies the type of the packet to be transmitted by the physical layer of the DUT. The default is NIBLUETOOTHDTM_VAL_TRANSMITTER_PHY_1MBPS. NIBLUETOOTHDTM_VAL_TRANSMITTER_PHY_1MBPS (0) Transmitter is set to use the LE 1M PHY. NIBLUETOOTHDTM_VAL_TRANSMITTER_PHY_2MBPS (1) Transmitter is set to use the LE 2M PHY. NIBLUETOOTHDTM_VAL_TRANSMITTER_PHY_CODED_125KBPS (2) Transmitter is set to use the LE Coded PHY with S = 8 data coding. NIBLUETOOTHDTM_VAL_TRANSMITTER_PHY_CODED_500KBPS (3) Transmitter is set to use the LE Coded PHY with S = 2 data coding. |
| NIBLUETOOTHDTM_VAL_TRANSMITTER_PHY_1MBPS (0) | Transmitter is set to use the LE 1M PHY. |  |
| NIBLUETOOTHDTM_VAL_TRANSMITTER_PHY_2MBPS (1) | Transmitter is set to use the LE 2M PHY. |  |
| NIBLUETOOTHDTM_VAL_TRANSMITTER_PHY_CODED_125KBPS (2) | Transmitter is set to use the LE Coded PHY with S = 8 data coding. |  |
| NIBLUETOOTHDTM_VAL_TRANSMITTER_PHY_CODED_500KBPS (3) | Transmitter is set to use the LE Coded PHY with S = 2 data coding. |  |
| Output |  |  |
| Name | Type | Description |
| status | int32 | Returns the status of the transmitter test command. The DUT receives and executes the transmitter test command if the status parameter returns a 0x00 value. The transmitter test command fails if the status parameter returns a non-zero (0x01-0xFF) value. |

#### Return Value

| Name | Type | Description |
| --- | --- | --- |
| returnValue | int32 | Returns the status code of this operation. The status code either indicates success or describes an error or warning. Examine the status code from each call to an niBluetoothDTM function to determine if an error has occurred. The general meaning of the status code is as follows: Value Meaning 0 Success Positive Values Warnings Negative Values Errors |
| Value | Meaning |  |
| 0 | Success |  |
| Positive Values | Warnings |  |
| Negative Values | Errors |  |
|  |  |  |

<!--NI_TOPIC bundle=rfmx-for-bluetooth-test-dtm path=cvibluetoothdtm/cvinibluetoothdtm_hcilereceivertest.html language=enus -->
## TOPIC 00044: niBluetoothDTM_HCILEReceiverTest

- bundle_id: `rfmx-for-bluetooth-test-dtm`
- source_path: `cvibluetoothdtm/cvinibluetoothdtm_hcilereceivertest.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-for-bluetooth-test-dtm/raw/resource/enus/cvibluetoothdtm/cvinibluetoothdtm_hcilereceivertest.html
- document_id: `rfmx-for-bluetooth-test-dtm`
- page_type: `leaf`
- content_type: ``

### niBluetoothDTM_HCILEReceiverTest

int32 __stdcall niBluetoothDTM_HCILEReceiverTest (niBluetoothDTMSession* session, 
 int32 channelNumber,
 int32 *status);

#### Purpose

Sends the command to the device under test (DUT) to start the receiver test.

#### Parameters

| Input |  |  |
| --- | --- | --- |
| Name | Type | Description |
| session | niBluetoothDTMSession | Specifies the name of the communication port to which the DUT is connected. |
| channelNumber | int32 | Specifies the Bluetooth transmit channel number of the generated signal. The default value is 0. |
| Output |  |  |
| Name | Type | Description |
| status | int32* | Returns the status of the receiver test command. The DUT receives and executes the receiver test command if the status parameter returns a 0x00 value. The receiver test command fails if the status parameter returns a non-zero (0x01-0xFF) value. |

#### Return Value

| Name | Type | Description |
| --- | --- | --- |
| returnValue | int32 | Returns the status code of this operation. The status code either indicates success or describes an error or warning. Examine the status code from each call to an niBluetoothDTM function to determine if an error has occurred. The general meaning of the status code is as follows: Value Meaning 0 Success Positive Values Warnings Negative Values Errors |
| Value | Meaning |  |
| 0 | Success |  |
| Positive Values | Warnings |  |
| Negative Values | Errors |  |
|  |  |  |

<!--NI_TOPIC bundle=rfmx-for-bluetooth-test-dtm path=cvibluetoothdtm/cvinibluetoothdtm_hciletestend.html language=enus -->
## TOPIC 00045: niBluetoothDTM_HCILETestEnd

- bundle_id: `rfmx-for-bluetooth-test-dtm`
- source_path: `cvibluetoothdtm/cvinibluetoothdtm_hciletestend.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-for-bluetooth-test-dtm/raw/resource/enus/cvibluetoothdtm/cvinibluetoothdtm_hciletestend.html
- document_id: `rfmx-for-bluetooth-test-dtm`
- page_type: `leaf`
- content_type: ``

### niBluetoothDTM_HCILETestEnd

int32 __stdcall niBluetoothDTM_HCILETestEnd (niBluetoothDTMSession* session,
 int32* packetCount,
 int32* status);

#### Purpose

Sends the command to the DUT to end the transmitter or the receiver test.

#### Parameters

| Input |  |  |
| --- | --- | --- |
| Name | Type | Description |
| session | niBluetoothDTMSession | Specifies the name of the communication port to which the DUT is connected. |
| Output |  |  |
| Name | Type | Description |
| packetCount | int32* | Returns the number of packets received by the DUT. |
| status | int32* | Returns the status of the test end command. The DUT receives and executes the test end command if the status parameter returns a 0x00 value. The test end command fails if the status parameter returns a non-zero (0x01-0xFF) value. |

#### Return Value

| Name | Type | Description |
| --- | --- | --- |
| returnValue | int32 | Returns the status code of this operation. The status code either indicates success or describes an error or warning. Examine the status code from each call to an niBluetoothDTM function to determine if an error has occurred. The general meaning of the status code is as follows: Value Meaning 0 Success Positive Values Warnings Negative Values Errors |
| Value | Meaning |  |
| 0 | Success |  |
| Positive Values | Warnings |  |
| Negative Values | Errors |  |
|  |  |  |

<!--NI_TOPIC bundle=rfmx-for-bluetooth-test-dtm path=cvibluetoothdtm/cvinibluetoothdtm_hciletransmittertest.html language=enus -->
## TOPIC 00046: niBluetoothDTM_HCILEReceiverTest

- bundle_id: `rfmx-for-bluetooth-test-dtm`
- source_path: `cvibluetoothdtm/cvinibluetoothdtm_hciletransmittertest.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-for-bluetooth-test-dtm/raw/resource/enus/cvibluetoothdtm/cvinibluetoothdtm_hciletransmittertest.html
- document_id: `rfmx-for-bluetooth-test-dtm`
- page_type: `leaf`
- content_type: ``

### niBluetoothDTM_HCILETransmitterTest

int32 __stdcall niBluetoothDTM_HCILETransmitterTest (niBluetoothDTMSession* session,
 int32 channelNumber,
 int32 payloadLengthBytes,
 int32 LEPatternType,
 int32 *status);

#### Purpose

Sends the command to the device under test (DUT) to start the transmitter test.

#### Parameters

| Input |  |  |
| --- | --- | --- |
| Name | Type | Description |
| session | niBluetoothDTMSession | Specifies the name of the communication port to which the DUT is connected. |
| channelNumber | int32 | Specifies the Bluetooth transmit channel number of the signal generated by the DUT. The default value is 0. |
| payloadLengthBytes | int32 | Specifies the length, in bytes, of payload data in each packet that the DUT transmits. The default value is 37. |
| LEPatternType | int32 | Specifies the type of payload to use for the LE packet. Payload type values of NIBLUETOOTHDTM_VAL_LE_PATTERN_TYPE_PRBS9, NIBLUETOOTHDTM_VAL_LE_PATTERN_TYPE_11110000, and NIBLUETOOTHDTM_VAL_LE_PATTERN_TYPE_10101010 must be supported by the DUT. The remaining payload type values are optional. The default value is NIBLUETOOTHDTM_VAL_LE_PATTERN_TYPE_PRBS9. NIBLUETOOTHDTM_VAL_LE_PATTERN_TYPE_PRBS9 (0) Specifies that the bit sequence is PRBS9. NIBLUETOOTHDTM_VAL_LE_PATTERN_TYPE_11110000 (1) Specifies that the bit sequence is 11110000. NIBLUETOOTHDTM_VAL_LE_PATTERN_TYPE_10101010 (2) Specifies that the bit sequence is 10101010. NIBLUETOOTHDTM_VAL_LE_PATTERN_TYPE_PRBS15 (3) Specifies that the bit sequence is PRBS15. NIBLUETOOTHDTM_VAL_LE_PATTERN_TYPE_11111111 (4) Specifies that the bit sequence is 11111111. NIBLUETOOTHDTM_VAL_LE_PATTERN_TYPE_00000000 (5) Specifies that the bit sequence is 00000000. NIBLUETOOTHDTM_VAL_LE_PATTERN_TYPE_00001111 (6) Specifies that the bit sequence is 00001111. NIBLUETOOTHDTM_VAL_LE_PATTERN_TYPE_01010101 (7) Specifies that the bit sequence is 01010101. |
| NIBLUETOOTHDTM_VAL_LE_PATTERN_TYPE_PRBS9 (0) | Specifies that the bit sequence is PRBS9. |  |
| NIBLUETOOTHDTM_VAL_LE_PATTERN_TYPE_11110000 (1) | Specifies that the bit sequence is 11110000. |  |
| NIBLUETOOTHDTM_VAL_LE_PATTERN_TYPE_10101010 (2) | Specifies that the bit sequence is 10101010. |  |
| NIBLUETOOTHDTM_VAL_LE_PATTERN_TYPE_PRBS15 (3) | Specifies that the bit sequence is PRBS15. |  |
| NIBLUETOOTHDTM_VAL_LE_PATTERN_TYPE_11111111 (4) | Specifies that the bit sequence is 11111111. |  |
| NIBLUETOOTHDTM_VAL_LE_PATTERN_TYPE_00000000 (5) | Specifies that the bit sequence is 00000000. |  |
| NIBLUETOOTHDTM_VAL_LE_PATTERN_TYPE_00001111 (6) | Specifies that the bit sequence is 00001111. |  |
| NIBLUETOOTHDTM_VAL_LE_PATTERN_TYPE_01010101 (7) | Specifies that the bit sequence is 01010101. |  |
| Output |  |  |
| Name | Type | Description |
| status | int32 | Returns the status of the transmitter test command. The DUT receives and executes the transmitter test command if the status parameter returns a 0x00 value. The transmitter test command fails if the status parameter returns a non-zero (0x01-0xFF) value. |

#### Return Value

| Name | Type | Description |
| --- | --- | --- |
| returnValue | int32 | Returns the status code of this operation. The status code either indicates success or describes an error or warning. Examine the status code from each call to an niBluetoothDTM function to determine if an error has occurred. The general meaning of the status code is as follows: Value Meaning 0 Success Positive Values Warnings Negative Values Errors |
| Value | Meaning |  |
| 0 | Success |  |
| Positive Values | Warnings |  |
| Negative Values | Errors |  |
|  |  |  |

<!--NI_TOPIC bundle=rfmx-for-bluetooth-test-dtm path=cvibluetoothdtm/cvinibluetoothdtm_hcireadbd_addr.html language=enus -->
## TOPIC 00047: niBluetoothDTM_HCIReadBD_ADDR

- bundle_id: `rfmx-for-bluetooth-test-dtm`
- source_path: `cvibluetoothdtm/cvinibluetoothdtm_hcireadbd_addr.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-for-bluetooth-test-dtm/raw/resource/enus/cvibluetoothdtm/cvinibluetoothdtm_hcireadbd_addr.html
- document_id: `rfmx-for-bluetooth-test-dtm`
- page_type: `leaf`
- content_type: ``

### niBluetoothDTM_HCIReadBD_ADDR

int32 __stdcall niBluetoothDTM_HCIReadBD_ADDR (niBluetoothDTMSession* session,
 int64 *BDAddress,
 int32 *status);

#### Purpose

Sends the command to the device under test (DUT) to get its Bluetooth device (BD) address.

#### Parameters

| Input |  |  |
| --- | --- | --- |
| Name | Type | Description |
| session | niBluetoothDTMSession | Specifies the name of the communication port to which the DUT is connected. |
| Output |  |  |
| Name | Type | Description |
| BDAddress | int64* | Returns the BD address of the DUT. |
| status | int32* | Returns the status of the read BD_ADDR command. The DUT receives and executes the read BD_ADDR command if the status parameter returns a 0x00 value. The read BD_ADDR command fails if the status parameter returns a non-zero (0x01-0xFF) value. |

#### Return Value

| Name | Type | Description |
| --- | --- | --- |
| returnValue | int32 | Returns the status code of this operation. The status code either indicates success or describes an error or warning. Examine the status code from each call to an niBluetoothDTM function to determine if an error has occurred. The general meaning of the status code is as follows: Value Meaning 0 Success Positive Values Warnings Negative Values Errors |
| Value | Meaning |  |
| 0 | Success |  |
| Positive Values | Warnings |  |
| Negative Values | Errors |  |
|  |  |  |

<!--NI_TOPIC bundle=rfmx-for-bluetooth-test-dtm path=cvibluetoothdtm/cvinibluetoothdtm_hcireset.html language=enus -->
## TOPIC 00048: niBluetoothDTM_HCIReset

- bundle_id: `rfmx-for-bluetooth-test-dtm`
- source_path: `cvibluetoothdtm/cvinibluetoothdtm_hcireset.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-for-bluetooth-test-dtm/raw/resource/enus/cvibluetoothdtm/cvinibluetoothdtm_hcireset.html
- document_id: `rfmx-for-bluetooth-test-dtm`
- page_type: `leaf`
- content_type: ``

### niBluetoothDTM_HCIReset

int32 __stdcall niBluetoothDTM_HCIReset (niBluetoothDTMSession* session,
 int32 *status);

#### Purpose

Resets the device under test (DUT) specified by the **session** parameter.

#### Parameters

| Input |  |  |
| --- | --- | --- |
| Name | Type | Description |
| session | niBluetoothDTMSession | Specifies the name of the communication port to which the DUT is connected. |
| Output |  |  |
| Name | Type | Description |
| status | int32 | Returns the status of the reset command. The DUT receives and executes the reset command if the status parameter returns a 0x00 value. The reset command fails if the status parameter returns a non-zero (0x01-0xFF) value. |

#### Return Value

| Name | Type | Description |
| --- | --- | --- |
| returnValue | int32 | Returns the status code of this operation. The status code either indicates success or describes an error or warning. Examine the status code from each call to an niBluetoothDTM function to determine if an error has occurred. The general meaning of the status code is as follows: Value Meaning 0 Success Positive Values Warnings Negative Values Errors |
| Value | Meaning |  |
| 0 | Success |  |
| Positive Values | Warnings |  |
| Negative Values | Errors |  |
|  |  |  |

<!--NI_TOPIC bundle=rfmx-for-bluetooth-test-dtm path=cvibluetoothdtm/cvinibluetoothdtm_visaclosesession.html language=enus -->
## TOPIC 00049: niBluetoothDTM_VISACloseSession

- bundle_id: `rfmx-for-bluetooth-test-dtm`
- source_path: `cvibluetoothdtm/cvinibluetoothdtm_visaclosesession.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-for-bluetooth-test-dtm/raw/resource/enus/cvibluetoothdtm/cvinibluetoothdtm_visaclosesession.html
- document_id: `rfmx-for-bluetooth-test-dtm`
- page_type: `leaf`
- content_type: ``

### niBluetoothDTM_VISACloseSession

int32 __stdcall niBluetoothDTM_VISACloseSession (niBluetoothDTMSession* session);

#### Purpose

Closes a device session or the event object that you specify in the **session** parameter.

#### Parameters

| Input |  |  |
| --- | --- | --- |
| Name | Type | Description |
| session | niBluetoothDTMSession | Specifies the name of the communication port to which the DUT is connected. |

#### Return Value

| Name | Type | Description |
| --- | --- | --- |
| returnValue | int32 | Returns the status code of this operation. The status code either indicates success or describes an error or warning. Examine the status code from each call to an niBluetoothDTM function to determine if an error has occurred. The general meaning of the status code is as follows: Value Meaning 0 Success Positive Values Warnings Negative Values Errors |
| Value | Meaning |  |
| 0 | Success |  |
| Positive Values | Warnings |  |
| Negative Values | Errors |  |
|  |  |  |

<!--NI_TOPIC bundle=rfmx-for-bluetooth-test-dtm path=cvibluetoothdtm/cvinibluetoothdtm_visaconfigureserialsettings.html language=enus -->
## TOPIC 00050: niBluetoothDTM_VISAConfigureSerialSettings

- bundle_id: `rfmx-for-bluetooth-test-dtm`
- source_path: `cvibluetoothdtm/cvinibluetoothdtm_visaconfigureserialsettings.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-for-bluetooth-test-dtm/raw/resource/enus/cvibluetoothdtm/cvinibluetoothdtm_visaconfigureserialsettings.html
- document_id: `rfmx-for-bluetooth-test-dtm`
- page_type: `leaf`
- content_type: ``

### niBluetoothDTM_VISAConfigureSerialSettings

int32 __stdcall niBluetoothDTM_VISAConfigureSerialSettings (niBluetoothDTMSession *session,
 uInt16 dataBits,
 uInt32 baudRate,
 uInt16 flowControl,
 uInt16 stopBits,
 uInt16 parity);

#### Purpose

Configures the VISA serial settings for the device under test (DUT) specified by the **session** parameter.

#### Parameters

| Input |  |  |
| --- | --- | --- |
| Name | Type | Description |
| session | niBluetoothDTMSession | Specifies the name of the communication port to which the DUT is connected. |
| dataBits | uInt16 | Specifies the number of data bits contained in each frame. Valid values are 5 to 8, inclusive. The data bits for each frame are located in the low-order bits of every byte stored in the memory. The default value is 8. |
| baudRate | uInt32 | Specifies the baud rate of the given communication port. The default value is 115,200. |
| flowControl | int32 | specifies the flow control method used for transmitting and receiving data. The default value is RTS/CTS. NIBLUETOOTHDTM_VAL_FLOW_CONTROL_NONE (0) Does not use flow control, and the buffers on both sides of the connection are assumed to be large enough to hold all the transferred data. NIBLUETOOTHDTM_VAL_FLOW_CONTROL_XON_XOFF (1) Uses the XON and XOFF characters to complete flow control. The transfer mechanism controls input flow by transmitting XOFF when the low-level I/O receive buffer is nearly full, and it controls the output flow by suspending transmission when XOFF is received. NIBLUETOOTHDTM_VAL_FLOW_CONTROL_RTS_CTS (2) Uses the RTS output signal and the CTS input signal to complete flow control. The transfer mechanism controls input flow by unasserting the RTS signal when the low-level I/O receive buffer is nearly full. The transfer mechanism also controls output flow by suspending the transmission when the CTS signal is unasserted. NIBLUETOOTHDTM_VAL_FLOW_CONTROL_XON_XOFF_AND_RTS_CTS (3) Uses values of XON/XOFF and RTS/CTS. NIBLUETOOTHDTM_VAL_FLOW_CONTROL_DTR_DSR (4) Uses the DTR output signal and the DSR input signal to complete flow control. The transfer mechanism controls input flow by unasserting the DTR signal when the low-level I/O receive buffer is nearly full. The transfer mechanism also controls output flow by suspending the transmission when the DSR signal is unasserted. NIBLUETOOTHDTM_VAL_FLOW_CONTROL_XON_XOFF_AND_DTR_DSR (5) Uses values of XON/XOFF and DTR/DSR. |
| NIBLUETOOTHDTM_VAL_FLOW_CONTROL_NONE (0) | Does not use flow control, and the buffers on both sides of the connection are assumed to be large enough to hold all the transferred data. |  |
| NIBLUETOOTHDTM_VAL_FLOW_CONTROL_XON_XOFF (1) | Uses the XON and XOFF characters to complete flow control. The transfer mechanism controls input flow by transmitting XOFF when the low-level I/O receive buffer is nearly full, and it controls the output flow by suspending transmission when XOFF is received. |  |
| NIBLUETOOTHDTM_VAL_FLOW_CONTROL_RTS_CTS (2) | Uses the RTS output signal and the CTS input signal to complete flow control. The transfer mechanism controls input flow by unasserting the RTS signal when the low-level I/O receive buffer is nearly full. The transfer mechanism also controls output flow by suspending the transmission when the CTS signal is unasserted. |  |
| NIBLUETOOTHDTM_VAL_FLOW_CONTROL_XON_XOFF_AND_RTS_CTS (3) | Uses values of XON/XOFF and RTS/CTS. |  |
| NIBLUETOOTHDTM_VAL_FLOW_CONTROL_DTR_DSR (4) | Uses the DTR output signal and the DSR input signal to complete flow control. The transfer mechanism controls input flow by unasserting the DTR signal when the low-level I/O receive buffer is nearly full. The transfer mechanism also controls output flow by suspending the transmission when the DSR signal is unasserted. |  |
| NIBLUETOOTHDTM_VAL_FLOW_CONTROL_XON_XOFF_AND_DTR_DSR (5) | Uses values of XON/XOFF and DTR/DSR. |  |
| stopBits | uInt16 | Specifies the number of stop bits used to indicate the end of a frame. The default value is 1.0. |
| parity | uInt16 | Specifies the parity bit used with each transmitted or received frame. The default value is NIBLUETOOTHDTM_VAL_PARITY_NONE. NIBLUETOOTHDTM_VAL_PARITY_NONE (0) Specifies that the frame does not contain a parity bit. NIBLUETOOTHDTM_VAL_PARITY_ODD (1) Specifies that the parity is odd. NIBLUETOOTHDTM_VAL_PARITY_EVEN (2) Specifies that the parity is even. NIBLUETOOTHDTM_VAL_PARITY_MARK (3) Specifies that the parity bit is always 1. NIBLUETOOTHDTM_VAL_PARITY_SPACE (4) Specifies that the parity bit is always 0. |
| NIBLUETOOTHDTM_VAL_PARITY_NONE (0) | Specifies that the frame does not contain a parity bit. |  |
| NIBLUETOOTHDTM_VAL_PARITY_ODD (1) | Specifies that the parity is odd. |  |
| NIBLUETOOTHDTM_VAL_PARITY_EVEN (2) | Specifies that the parity is even. |  |
| NIBLUETOOTHDTM_VAL_PARITY_MARK (3) | Specifies that the parity bit is always 1. |  |
| NIBLUETOOTHDTM_VAL_PARITY_SPACE (4) | Specifies that the parity bit is always 0. |  |

#### Return Value

| Name | Type | Description |
| --- | --- | --- |
| returnValue | int32 | Returns the status code of this operation. The status code either indicates success or describes an error or warning. Examine the status code from each call to an niBluetoothDTM function to determine if an error has occurred. The general meaning of the status code is as follows: Value Meaning 0 Success Positive Values Warnings Negative Values Errors |
| Value | Meaning |  |
| 0 | Success |  |
| Positive Values | Warnings |  |
| Negative Values | Errors |  |
|  |  |  |

<!--NI_TOPIC bundle=rfmx-for-bluetooth-test-dtm path=cvibluetoothdtm/cvinibluetoothdtm_visaopensession.html language=enus -->
## TOPIC 00051: niBluetoothDTM_VISAOpenSession

- bundle_id: `rfmx-for-bluetooth-test-dtm`
- source_path: `cvibluetoothdtm/cvinibluetoothdtm_visaopensession.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-for-bluetooth-test-dtm/raw/resource/enus/cvibluetoothdtm/cvinibluetoothdtm_visaopensession.html
- document_id: `rfmx-for-bluetooth-test-dtm`
- page_type: `leaf`
- content_type: ``

### niBluetoothDTM_VISAOpenSession

int32 __stdcall niBluetoothDTM_VISAOpenSession (char session[],
 niBluetoothDTMSession* sessionOut);

#### Purpose

Opens a session of the device under test (DUT) specified by the **session** parameter, and returns a session identifier that can be used to call any other operations on that DUT.

#### Parameters

| Input |  |  |
| --- | --- | --- |
| Name | Type | Description |
| session | char[] | Specifies the name of the communication port to which the DUT is connected. |
| Output |  |  |
| Name | Type | Description |
| sessionOut | niBluetoothDTMSession* | Returns the name of the communication port to which the DUT is connected. |

#### Return Value

| Name | Type | Description |
| --- | --- | --- |
| returnValue | int32 | Returns the status code of this operation. The status code either indicates success or describes an error or warning. Examine the status code from each call to an niBluetoothDTM function to determine if an error has occurred. The general meaning of the status code is as follows: Value Meaning 0 Success Positive Values Warnings Negative Values Errors |
| Value | Meaning |  |
| 0 | Success |  |
| Positive Values | Warnings |  |
| Negative Values | Errors |  |
|  |  |  |

<!--NI_TOPIC bundle=rfmx-for-bluetooth-test-dtm path=cvibluetoothdtm/cvinibluetoothdtm_visasettimeout.html language=enus -->
## TOPIC 00052: niBluetoothDTM_VISASetTimeout

- bundle_id: `rfmx-for-bluetooth-test-dtm`
- source_path: `cvibluetoothdtm/cvinibluetoothdtm_visasettimeout.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-for-bluetooth-test-dtm/raw/resource/enus/cvibluetoothdtm/cvinibluetoothdtm_visasettimeout.html
- document_id: `rfmx-for-bluetooth-test-dtm`
- page_type: `leaf`
- content_type: ``

### niBluetoothDTM_VISASetTimeout

int32 __stdcall niBluetoothDTM_VISASetTimeout (niBluetoothDTMSession *session,
 uInt32 timeout);

#### Purpose

Sets the timeout value, in milliseconds (ms), for the VISA session of the device under test (DUT), specified by the **session** parameter.

#### Parameters

| Input |  |  |
| --- | --- | --- |
| Name | Type | Description |
| session | niBluetoothDTMSession | Specifies the name of the communication port to which the DUT is connected. |
| timeout | uInt32 | Specifies the minimum timeout value, in milliseconds (ms), to use when accessing the device. The default value is 2,000. Note The actual timeout that VISA returns may be higher than the specified timeout. |
|  | Note | The actual timeout that VISA returns may be higher than the specified timeout. |

#### Return Value

| Name | Type | Description |
| --- | --- | --- |
| returnValue | int32 | Returns the status code of this operation. The status code either indicates success or describes an error or warning. Examine the status code from each call to an niBluetoothDTM function to determine if an error has occurred. The general meaning of the status code is as follows: Value Meaning 0 Success Positive Values Warnings Negative Values Errors |
| Value | Meaning |  |
| 0 | Success |  |
| Positive Values | Warnings |  |
| Negative Values | Errors |  |
|  |  |  |

<!--NI_TOPIC bundle=rfmx-for-bluetooth-test-dtm path=cvibluetoothdtm/help_file_title.html language=enus -->
## TOPIC 00053: RFmx for Bluetooth® Test Direct Test Mode C Reference

- bundle_id: `rfmx-for-bluetooth-test-dtm`
- source_path: `cvibluetoothdtm/help_file_title.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-for-bluetooth-test-dtm/raw/resource/enus/cvibluetoothdtm/help_file_title.html
- document_id: `rfmx-for-bluetooth-test-dtm`
- page_type: `leaf`
- content_type: ``

### RFmx for Bluetooth® Test Direct Test Mode C Reference

This help file contains information about the RFmx for Bluetooth® Test Direct Test Mode generation functions that you can use when programming your application.

© 2019–2021 National Instruments Corporation. All rights reserved.

<!--NI_TOPIC bundle=rfmx-for-bluetooth-test-dtm path=lvbluetoothdtmvi/nibluetoothdtm_create_custom_command.html language=enus -->
## TOPIC 00054: niBluetoothDTM Create Custom Command (VI)

- bundle_id: `rfmx-for-bluetooth-test-dtm`
- source_path: `lvbluetoothdtmvi/nibluetoothdtm_create_custom_command.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-for-bluetooth-test-dtm/raw/resource/enus/lvbluetoothdtmvi/nibluetoothdtm_create_custom_command.html
- document_id: `rfmx-for-bluetooth-test-dtm`
- page_type: `leaf`
- content_type: ``

### niBluetoothDTM Create Custom Command (VI)

Owning Palette:

Bluetooth Direct Test Mode VIs

Sends the specified custom command to the device under test (DUT).

[IMAGE alt='niBluetoothDTM Create Custom Command' src='nibluetoothdtm_create_custom_command.gif']

|  | VISA resource name specifies the name of the resource to be opened. This parameter also specifies the VISA session and class. |
| --- | --- |
|  | opcode specifies an array of custom opcode commands to send to the DUT. |
|  | command parameters specifies an array of the input parameters required for the custom command. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | VISA resource name out returns the resource name to which a VISA session is opened and the resource class. The class name matches the VISA resource name parameter. |
|  | return parameters returns an array of the parameters sent by the DUT in response to the custom command. |
|  | error out contains error information. This output provides standard error out functionality. |

<!--NI_TOPIC bundle=rfmx-for-bluetooth-test-dtm path=lvbluetoothdtmvi/nibluetoothdtm_hci_le_direction_finding_receiver_test.html language=enus -->
## TOPIC 00055: niBluetoothDTM HCI LE Direction Finding Receiver Test (VI)

- bundle_id: `rfmx-for-bluetooth-test-dtm`
- source_path: `lvbluetoothdtmvi/nibluetoothdtm_hci_le_direction_finding_receiver_test.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-for-bluetooth-test-dtm/raw/resource/enus/lvbluetoothdtmvi/nibluetoothdtm_hci_le_direction_finding_receiver_test.html
- document_id: `rfmx-for-bluetooth-test-dtm`
- page_type: `leaf`
- content_type: ``

### niBluetoothDTM HCI LE Direction Finding Receiver Test (VI)

Owning Palette:

Bluetooth Direct Test Mode VIs

Sends a command to the device under test (DUT) to start the receiver test.

[IMAGE alt='niBluetoothDTM HCI LE Direction Finding Receiver Test' src='nibluetoothdtm_hci_le_direction_finding_receiver_test.gif']

|  | VISA resource name specifies the name of the resource to be opened. This parameter also specifies the VISA session and class. |
| --- | --- |
|  | channel number specifies the Bluetooth transmit channel number of the generated signal. The default value is 0. |
|  | PHY specifies the type of the generated packet by the physical layer of the DUT. The default value is 1Mbps. 1Mbps (0) Receiver is set to use the LE 1M PHY. 2Mbps (1) Receiver is set to use the LE 2M PHY. Coded (2) Receiver is set to use the Coded PHY. |
| 1Mbps (0) | Receiver is set to use the LE 1M PHY. |
| 2Mbps (1) | Receiver is set to use the LE 2M PHY. |
| Coded (2) | Receiver is set to use the Coded PHY. |
|  | modulation index specifies the type of modulation index at the generator. The default value is Standard. Standard (0) The packets are generated with standard modulation index. Stable (1) The packets are generated with stable modulation index. |
| Standard (0) | The packets are generated with standard modulation index. |
| Stable (1) | The packets are generated with stable modulation index. |
|  | Direction Finding Mode specifies the mode of direction finding. The default value is Disabled. Disabled (0) Specifies that the LE packet does not have fields required for direction finding. Angle of Arrival (1) Specifies the LE packets uses the angle of arrival method of direction finding. Angle of Departure (2) Specifies the LE packet uses angle of departure method of direction finding. |
| Disabled (0) | Specifies that the LE packet does not have fields required for direction finding. |
| Angle of Arrival (1) | Specifies the LE packets uses the angle of arrival method of direction finding. |
| Angle of Departure (2) | Specifies the LE packet uses angle of departure method of direction finding. |
|  | CTE Length specifies the length of the constant tone extension field in the generated signal. This value is expressed in seconds. This parameter is applicable only when you set the Direction Finding Mode parameter to either Angle of Arrival or Angle of Departure. The default value is 160 microseconds. |
|  | CTE Slot Duration specifies the length of the antenna switching and sampling slots in the constant tone extension field. This value is expressed in seconds. The default value is 1 us. 1 us (0.000001) Specifies that the length of the antenna switching and sampling slots in the constant tone extension field is 1 microseconds. 2 us (0.000002) Specifies that the length of the antenna switching and sampling slots in the constant tone extension field is 2 microseconds. |
| 1 us (0.000001) | Specifies that the length of the antenna switching and sampling slots in the constant tone extension field is 1 microseconds. |
| 2 us (0.000002) | Specifies that the length of the antenna switching and sampling slots in the constant tone extension field is 2 microseconds. |
|  | Antenna IDs specifies the array of Antenna IDs in the antenna switching pattern. The length of Antenna IDs array must be equal to Length Of Switching Pattern. |
|  | Switching Pattern Length specifies the length of the antenna switching pattern. The default value is 0. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | VISA resource name out returns the resource name to which a VISA session is opened and the resource class. The class name matches the VISA resource name parameter. |
|  | status returns the status of the receiver test command. The DUT receives and executes the receiver test command if the status parameter returns a 0x00 value. The receiver test command fails if the status parameter returns a non-zero (0x01-0xFF) value. |
|  | error out contains error information. This output provides standard error out functionality. |

<!--NI_TOPIC bundle=rfmx-for-bluetooth-test-dtm path=lvbluetoothdtmvi/nibluetoothdtm_hci_le_direction_finding_transmitter_test.html language=enus -->
## TOPIC 00056: niBluetoothDTM HCI LE Direction Finding Transmitter Test (VI)

- bundle_id: `rfmx-for-bluetooth-test-dtm`
- source_path: `lvbluetoothdtmvi/nibluetoothdtm_hci_le_direction_finding_transmitter_test.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-for-bluetooth-test-dtm/raw/resource/enus/lvbluetoothdtmvi/nibluetoothdtm_hci_le_direction_finding_transmitter_test.html
- document_id: `rfmx-for-bluetooth-test-dtm`
- page_type: `leaf`
- content_type: ``

### niBluetoothDTM HCI LE Direction Finding Transmitter Test (VI)

Owning Palette:

Bluetooth Direct Test Mode VIs

Sends a command to the device under test (DUT) to start the transmitter test.

[IMAGE alt='niBluetoothDTM HCI LE Direction Finding Transmitter Test' src='nibluetoothdtm_hci_le_direction_finding_transmitter_test.gif']

|  | VISA resource name specifies the name of the resource to be opened. This parameter also specifies the VISA session and class. |
| --- | --- |
|  | channel number specifies the Bluetooth transmit channel number of the generated signal. The default value is 0. |
|  | payload length specifies the length of payload data in each packet that the DUT transmits. This value is expressed in bytes. The default value is 37. |
|  | LE pattern type specifies the type of payload to use for the LE packet. The default value is PRBS9. Payload type values of PRBS9, 11110000, and 10101010 must be supported by the DUT. The remaining payload type values are optional. PRBS9 (0) Specifies that the bit sequence is PRBS9. 11110000 (1) Specifies that the bit sequence is 11110000. 10101010 (2) Specifies that the bit sequence is 10101010. PRBS15 (3) Specifies that the bit sequence is PRBS15. 11111111 (4) Specifies that the bit sequence is 11111111. 00000000 (5) Specifies that the bit sequence is 00000000. 00001111 (6) Specifies that the bit sequence is 00001111. 01010101 (7) Specifies that the bit sequence is 01010101. |
| PRBS9 (0) | Specifies that the bit sequence is PRBS9. |
| 11110000 (1) | Specifies that the bit sequence is 11110000. |
| 10101010 (2) | Specifies that the bit sequence is 10101010. |
| PRBS15 (3) | Specifies that the bit sequence is PRBS15. |
| 11111111 (4) | Specifies that the bit sequence is 11111111. |
| 00000000 (5) | Specifies that the bit sequence is 00000000. |
| 00001111 (6) | Specifies that the bit sequence is 00001111. |
| 01010101 (7) | Specifies that the bit sequence is 01010101. |
|  | PHY specifies the type of the packet to be transmitted by the physical layer of the DUT. The default value is 1Mbps. 1Mbps (0) Transmitter is set to use the LE 1M PHY. 2Mbps (1) Transmitter is set to use the LE 2M PHY. Coded 125kbps (2) Transmitter is set to use the LE Coded PHY with S = 8 data coding. Coded 500kbps (3) Transmitter is set to use the LE Coded PHY with S = 2 data coding. |
| 1Mbps (0) | Transmitter is set to use the LE 1M PHY. |
| 2Mbps (1) | Transmitter is set to use the LE 2M PHY. |
| Coded 125kbps (2) | Transmitter is set to use the LE Coded PHY with S = 8 data coding. |
| Coded 500kbps (3) | Transmitter is set to use the LE Coded PHY with S = 2 data coding. |
|  | Direction Finding Mode specifies the mode of direction finding. The default value is Disabled. Disabled (0) Specifies that the LE packet does not have fields required for direction finding. Angle of Arrival (1) Specifies the LE packets uses the angle of arrival method of direction finding. Angle of Departure (2) Specifies the LE packet uses angle of departure method of direction finding. |
| Disabled (0) | Specifies that the LE packet does not have fields required for direction finding. |
| Angle of Arrival (1) | Specifies the LE packets uses the angle of arrival method of direction finding. |
| Angle of Departure (2) | Specifies the LE packet uses angle of departure method of direction finding. |
|  | CTE Length specifies the length of the constant tone extension field in the generated signal. This value is expressed in seconds. This parameter is applicable only when you set the Direction Finding Mode parameter to either Angle of Arrival or Angle of Departure. The default value is 160 microseconds. |
|  | CTE Slot Duration specifies the length of the antenna switching and sampling slots in the constant tone extension field. This value is expressed in seconds. The default value is 1 us. 1 us (0.000001) Specifies that the length of the antenna switching and sampling slots in the constant tone extension field is 1 microseconds. 2 us (0.000002) Specifies that the length of the antenna switching and sampling slots in the constant tone extension field is 2 microseconds. |
| 1 us (0.000001) | Specifies that the length of the antenna switching and sampling slots in the constant tone extension field is 1 microseconds. |
| 2 us (0.000002) | Specifies that the length of the antenna switching and sampling slots in the constant tone extension field is 2 microseconds. |
|  | Antenna IDs specifies the array of Antenna IDs in the antenna switching pattern. The length of Antenna IDs array must be equal to Length Of Switching Pattern. |
|  | Switching Pattern Length specifies the length of the antenna switching pattern. The default value is 0. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | VISA resource name out returns the resource name to which a VISA session is opened and the resource class. The class name matches the VISA resource name parameter. |
|  | status returns the status of the transmitter test command. The DUT receives and executes the transmitter test command if the status parameter returns a 0x00 value. The transmitter test command fails if the status parameter returns a non-zero (0x01-0xFF) value. |
|  | error out contains error information. This output provides standard error out functionality. |

<!--NI_TOPIC bundle=rfmx-for-bluetooth-test-dtm path=lvbluetoothdtmvi/nibluetoothdtm_hci_le_enhanced_receiver_test.html language=enus -->
## TOPIC 00057: niBluetoothDTM HCI LE Enhanced Receiver Test (VI)

- bundle_id: `rfmx-for-bluetooth-test-dtm`
- source_path: `lvbluetoothdtmvi/nibluetoothdtm_hci_le_enhanced_receiver_test.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-for-bluetooth-test-dtm/raw/resource/enus/lvbluetoothdtmvi/nibluetoothdtm_hci_le_enhanced_receiver_test.html
- document_id: `rfmx-for-bluetooth-test-dtm`
- page_type: `leaf`
- content_type: ``

### niBluetoothDTM HCI LE Enhanced Receiver Test (VI)

Owning Palette:

Bluetooth Direct Test Mode VIs

Sends a command to the device under test (DUT) to start the receiver test.

[IMAGE alt='niBluetoothDTM HCI LE Enhanced Receiver Test' src='nibluetoothdtm_hci_le_enhanced_receiver_test.gif']

|  | VISA resource name specifies the resource name corresponding to the DUT. |
| --- | --- |
|  | channel number specifies the Bluetooth transmit channel number of the generated signal. The default value is 0. |
|  | PHY specifies the type of the generated packet by the physical layer of the DUT. The default value is 1Mbps. 1Mbps (0) Receiver is set to use the LE 1M PHY. 2Mbps (1) Receiver is set to use the LE 2M PHY. Coded (2) Receiver is set to use the Coded PHY. |
| 1Mbps (0) | Receiver is set to use the LE 1M PHY. |
| 2Mbps (1) | Receiver is set to use the LE 2M PHY. |
| Coded (2) | Receiver is set to use the Coded PHY. |
|  | modulation index specifies the type of modulation index at the generator. The default value is Standard. Standard (0) The packets are generated with standard modulation index. Stable (1) The packets are generated with stable modulation index. |
| Standard (0) | The packets are generated with standard modulation index. |
| Stable (1) | The packets are generated with stable modulation index. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | VISA resource name out returns the resource name to which a VISA session is opened and the resource class. The class name matches the VISA resource name parameter. |
|  | status returns the status of the receiver test command. The DUT receives and executes the receiver test command if the status parameter returns a 0x00 value. The receiver test command fails if the status parameter returns a non-zero (0x01-0xFF) value. |
|  | error out contains error information. This output provides standard error out functionality. |

<!--NI_TOPIC bundle=rfmx-for-bluetooth-test-dtm path=lvbluetoothdtmvi/nibluetoothdtm_hci_le_enhanced_transmitter_test.html language=enus -->
## TOPIC 00058: niBluetoothDTM HCI LE Enhanced Transmitter Test (VI)

- bundle_id: `rfmx-for-bluetooth-test-dtm`
- source_path: `lvbluetoothdtmvi/nibluetoothdtm_hci_le_enhanced_transmitter_test.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-for-bluetooth-test-dtm/raw/resource/enus/lvbluetoothdtmvi/nibluetoothdtm_hci_le_enhanced_transmitter_test.html
- document_id: `rfmx-for-bluetooth-test-dtm`
- page_type: `leaf`
- content_type: ``

### niBluetoothDTM HCI LE Enhanced Transmitter Test (VI)

Owning Palette:

Bluetooth Direct Test Mode VIs

Sends the command to the device under test (DUT) to start the transmitter test.

[IMAGE alt='niBluetoothDTM HCI LE Enhanced Transmitter Test' src='nibluetoothdtm_hci_le_enhanced_transmitter_test.gif']

|  | VISA resource name specifies the resource name corresponding to the DUT. |
| --- | --- |
|  | channel number specifies the Bluetooth transmit channel number of the signal generated by the DUT. The default value is 0. |
|  | payload length specifies the length of payload data in each packet that the DUT transmits. This value is expressed in bytes. The default value is 37. |
|  | LE pattern type specifies the type of payload to use for the LE packet. The default value is PRBS9. Payload type values of PRBS9, 11110000, and 10101010 must be supported by the DUT. The remaining payload type values are optional. PRBS9 (0) Specifies that the bit sequence is PRBS9. 11110000 (1) Specifies that the bit sequence is 11110000. 10101010 (2) Specifies that the bit sequence is 10101010. PRBS15 (3) Specifies that the bit sequence is PRBS15. 11111111 (4) Specifies that the bit sequence is 11111111. 00000000 (5) Specifies that the bit sequence is 00000000. 00001111 (6) Specifies that the bit sequence is 00001111. 01010101 (7) Specifies that the bit sequence is 01010101. |
| PRBS9 (0) | Specifies that the bit sequence is PRBS9. |
| 11110000 (1) | Specifies that the bit sequence is 11110000. |
| 10101010 (2) | Specifies that the bit sequence is 10101010. |
| PRBS15 (3) | Specifies that the bit sequence is PRBS15. |
| 11111111 (4) | Specifies that the bit sequence is 11111111. |
| 00000000 (5) | Specifies that the bit sequence is 00000000. |
| 00001111 (6) | Specifies that the bit sequence is 00001111. |
| 01010101 (7) | Specifies that the bit sequence is 01010101. |
|  | PHY specifies the type of the packet to be transmitted by the physical layer of the DUT. The default value is 1Mbps. 1Mbps (0) Transmitter is set to use the LE 1M PHY. 2Mbps (1) Transmitter is set to use the LE 2M PHY. Coded 125kbps (2) Transmitter is set to use the LE Coded PHY with S = 8 data coding. Coded 500kbps (3) Transmitter is set to use the LE Coded PHY with S = 2 data coding. |
| 1Mbps (0) | Transmitter is set to use the LE 1M PHY. |
| 2Mbps (1) | Transmitter is set to use the LE 2M PHY. |
| Coded 125kbps (2) | Transmitter is set to use the LE Coded PHY with S = 8 data coding. |
| Coded 500kbps (3) | Transmitter is set to use the LE Coded PHY with S = 2 data coding. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | VISA resource name out returns the resource name to which a VISA session is opened and the resource class. The class name matches the VISA resource name parameter. |
|  | status returns the status of the transmitter test command. The DUT receives and executes the transmitter test command if the status parameter returns a 0x00 value. The transmitter test command fails if the status parameter returns a non-zero (0x01-0xFF) value. |
|  | error out contains error information. This output provides standard error out functionality. |

<!--NI_TOPIC bundle=rfmx-for-bluetooth-test-dtm path=lvbluetoothdtmvi/nibluetoothdtm_hci_le_receiver_test.html language=enus -->
## TOPIC 00059: niBluetoothDTM HCI LE Receiver Test (VI)

- bundle_id: `rfmx-for-bluetooth-test-dtm`
- source_path: `lvbluetoothdtmvi/nibluetoothdtm_hci_le_receiver_test.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-for-bluetooth-test-dtm/raw/resource/enus/lvbluetoothdtmvi/nibluetoothdtm_hci_le_receiver_test.html
- document_id: `rfmx-for-bluetooth-test-dtm`
- page_type: `leaf`
- content_type: ``

### niBluetoothDTM HCI LE Receiver Test (VI)

Owning Palette:

Bluetooth Direct Test Mode VIs

Sends the command to the device under test (DUT) to start the receiver test.

[IMAGE alt='niBluetoothDTM HCI LE Receiver Test' src='nibluetoothdtm_hci_le_receiver_test.gif']

|  | VISA resource name specifies the name of the resource to be opened. This parameter also specifies the VISA session and class. |
| --- | --- |
|  | channel number specifies the Bluetooth transmit channel number of the generated signal. The default value is 0. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | VISA resource name out returns the resource name to which a VISA session is opened and the resource class. The class name matches the VISA resource name parameter. |
|  | status returns the status of the receiver test command. The DUT receives and executes the receiver test command if the status parameter returns a 0x00 value. The receiver test command fails if the status parameter returns a non-zero (0x01-0xFF) value. |
|  | error out contains error information. This output provides standard error out functionality. |

<!--NI_TOPIC bundle=rfmx-for-bluetooth-test-dtm path=lvbluetoothdtmvi/nibluetoothdtm_hci_le_test_end.html language=enus -->
## TOPIC 00060: niBluetoothDTM HCI LE Test End (VI)

- bundle_id: `rfmx-for-bluetooth-test-dtm`
- source_path: `lvbluetoothdtmvi/nibluetoothdtm_hci_le_test_end.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-for-bluetooth-test-dtm/raw/resource/enus/lvbluetoothdtmvi/nibluetoothdtm_hci_le_test_end.html
- document_id: `rfmx-for-bluetooth-test-dtm`
- page_type: `leaf`
- content_type: ``

### niBluetoothDTM HCI LE Test End (VI)

Owning Palette:

Bluetooth Direct Test Mode VIs

Sends the command to the device under test (DUT) to end the transmitter or receiver test.

[IMAGE alt='niBluetoothDTM HCI LE Test End' src='nibluetoothdtm_hci_le_test_end.gif']

|  | VISA resource name specifies the name of the resource to be opened. This parameter also specifies the VISA session and class. |
| --- | --- |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | VISA resource name out returns the resource name to which a VISA session is opened and the resource class. The class name matches the VISA resource name parameter. |
|  | status returns the status of the test end command. The DUT receives and executes the test end command if the status parameter returns a 0x00 value. The test end command fails if the status parameter returns a non-zero (0x01-0xFF) value. |
|  | packet count returns the number of packets received by the DUT. |
|  | error out contains error information. This output provides standard error out functionality. |

<!--NI_TOPIC bundle=rfmx-for-bluetooth-test-dtm path=lvbluetoothdtmvi/nibluetoothdtm_hci_le_transmitter_test.html language=enus -->
## TOPIC 00061: niBluetoothDTM HCI LE Transmitter Test (VI)

- bundle_id: `rfmx-for-bluetooth-test-dtm`
- source_path: `lvbluetoothdtmvi/nibluetoothdtm_hci_le_transmitter_test.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-for-bluetooth-test-dtm/raw/resource/enus/lvbluetoothdtmvi/nibluetoothdtm_hci_le_transmitter_test.html
- document_id: `rfmx-for-bluetooth-test-dtm`
- page_type: `leaf`
- content_type: ``

### niBluetoothDTM HCI LE Transmitter Test (VI)

Owning Palette:

Bluetooth Direct Test Mode VIs

Sends a command to the device under test (DUT) to start the transmitter test.

[IMAGE alt='niBluetoothDTM HCI LE Transmitter Test' src='nibluetoothdtm_hci_le_transmitter_test.gif']

|  | VISA resource name specifies the resource name corresponding to the DUT. |
| --- | --- |
|  | channel number specifies the Bluetooth transmit channel number of the signal generated by the DUT. The default value is 0. |
|  | payload length specifies the length of payload data in each packet that the DUT transmits. This value is expressed in bytes. The default value is 37. |
|  | LE pattern type specifies the type of payload to use for the LE packet. The default value is PRBS9. Payload type values of PRBS9, 11110000, and 10101010 must be supported by the DUT. The remaining payload type values are optional. PRBS9 (0) Specifies that the bit sequence is PRBS9. 11110000 (1) Specifies that the bit sequence is 11110000. 10101010 (2) Specifies that the bit sequence is 10101010. PRBS15 (3) Specifies that the bit sequence is PRBS15. 11111111 (4) Specifies that the bit sequence is 11111111. 00000000 (5) Specifies that the bit sequence is 00000000. 00001111 (6) Specifies that the bit sequence is 00001111. 01010101 (7) Specifies that the bit sequence is 01010101. |
| PRBS9 (0) | Specifies that the bit sequence is PRBS9. |
| 11110000 (1) | Specifies that the bit sequence is 11110000. |
| 10101010 (2) | Specifies that the bit sequence is 10101010. |
| PRBS15 (3) | Specifies that the bit sequence is PRBS15. |
| 11111111 (4) | Specifies that the bit sequence is 11111111. |
| 00000000 (5) | Specifies that the bit sequence is 00000000. |
| 00001111 (6) | Specifies that the bit sequence is 00001111. |
| 01010101 (7) | Specifies that the bit sequence is 01010101. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | VISA resource name out returns the resource name to which a VISA session is opened and the resource class. The class name matches the VISA resource name parameter. |
|  | status returns the status of the transmitter test command. The DUT receives and executes the transmitter test command if the status parameter returns a 0x00 value. The transmitter test command fails if the status parameter returns a non-zero (0x01-0xFF) value. |
|  | error out contains error information. This output provides standard error out functionality. |

<!--NI_TOPIC bundle=rfmx-for-bluetooth-test-dtm path=lvbluetoothdtmvi/nibluetoothdtm_hci_read_bd_addr.html language=enus -->
## TOPIC 00062: niBluetoothDTM HCI Read BD_ADDR (VI)

- bundle_id: `rfmx-for-bluetooth-test-dtm`
- source_path: `lvbluetoothdtmvi/nibluetoothdtm_hci_read_bd_addr.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-for-bluetooth-test-dtm/raw/resource/enus/lvbluetoothdtmvi/nibluetoothdtm_hci_read_bd_addr.html
- document_id: `rfmx-for-bluetooth-test-dtm`
- page_type: `leaf`
- content_type: ``

### niBluetoothDTM HCI Read BD_ADDR (VI)

Owning Palette:

Bluetooth Direct Test Mode VIs

Sends the command to the device under test (DUT) to get its Bluetooth device (BD) address.

[IMAGE alt='niBluetoothDTM HCI Read BD_ADDR' src='nibluetoothdtm_hci_read_bd_addr.gif']

|  | VISA resource name specifies the name of the resource to be opened. This parameter also specifies the VISA session and class. |
| --- | --- |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | VISA resource name out returns the resource name to which a VISA session is opened and the resource class. The class name matches the VISA resource name parameter. |
|  | status returns the status of the read BD_ADDR command. The DUT receives and executes the read BD_ADDR command if the status parameter returns a 0x00 value. The read BD_ADDR command fails if the status parameter returns a non-zero (0x01-0xFF) value. |
|  | BD_ADDR returns the BD address of the DUT. |
|  | error out contains error information. This output provides standard error out functionality. |

<!--NI_TOPIC bundle=rfmx-for-bluetooth-test-dtm path=lvbluetoothdtmvi/nibluetoothdtm_hci_reset.html language=enus -->
## TOPIC 00063: niBluetoothDTM HCI Reset (VI)

- bundle_id: `rfmx-for-bluetooth-test-dtm`
- source_path: `lvbluetoothdtmvi/nibluetoothdtm_hci_reset.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-for-bluetooth-test-dtm/raw/resource/enus/lvbluetoothdtmvi/nibluetoothdtm_hci_reset.html
- document_id: `rfmx-for-bluetooth-test-dtm`
- page_type: `leaf`
- content_type: ``

### niBluetoothDTM HCI Reset (VI)

Owning Palette:

Bluetooth Direct Test Mode VIs

Resets the device under test (DUT) specified by the **VISA resource name** parameter.

[IMAGE alt='niBluetoothDTM HCI Reset' src='nibluetoothdtm_hci_reset.gif']

|  | VISA resource name specifies the resource name corresponding to the DUT. |
| --- | --- |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | VISA resource name out returns the resource name to which a VISA session is opened and the resource class. The class name matches the VISA resource name parameter. |
|  | status returns the status of the reset command. The DUT receives and executes the reset command if the status parameter returns a 0x00 value. The reset command fails if the parameter returns a non-zero (0x01-0xFF) value. |
|  | error out contains error information. This output provides standard error out functionality. |

<!--NI_TOPIC bundle=rfmx-for-bluetooth-test-dtm path=lvbluetoothdtmvi/nibluetoothdtm_pal.html language=enus -->
## TOPIC 00064: RFmx for Bluetooth® Test Direct Test Mode VIs

- bundle_id: `rfmx-for-bluetooth-test-dtm`
- source_path: `lvbluetoothdtmvi/nibluetoothdtm_pal.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-for-bluetooth-test-dtm/raw/resource/enus/lvbluetoothdtmvi/nibluetoothdtm_pal.html
- document_id: `rfmx-for-bluetooth-test-dtm`
- page_type: `leaf`
- content_type: ``

### RFmx for Bluetooth® Test Direct Test Mode VIs

Use the VIs on this palette to send commands to the device under test (DUT). These VIs help to control the DUT by directing it to perform tasks such as starting the transmitter or receiver test, ending the test, getting the BD address.

© 2019–2021 National Instruments Corporation. All rights reserved.

| Palette Object | Description |
| --- | --- |
| niBluetoothDTM VISA Open Session | Opens a session of the device under test (DUT) specified by the VISA resource name parameter, and returns a session identifier that can be used to call any other operations on that DUT. |
| niBluetoothDTM VISA Configure Serial Settings | Configures the VISA serial settings for the device under test (DUT) specified by the VISA resource name parameter. |
| niBluetoothDTM VISA Set Timeout | Sets the timeout value, in milliseconds (ms), for the VISA session of the device under test (DUT), specified by the VISA resource name parameter. |
| niBluetoothDTM HCI Read BD_ADDR | Sends the command to the device under test (DUT) to get its Bluetooth device (BD) address. |
| niBluetoothDTM HCI LE Transmitter Test | Sends a command to the device under test (DUT) to start the transmitter test. |
| niBluetoothDTM HCI LE Receiver Test | Sends the command to the device under test (DUT) to start the receiver test. |
| niBluetoothDTM HCI LE Enhanced Transmitter Test | Sends the command to the device under test (DUT) to start the transmitter test. |
| niBluetoothDTM HCI LE Enhanced Receiver Test | Sends a command to the device under test (DUT) to start the receiver test. |
| niBluetoothDTM HCI LE Direction Finding Transmitter Test | Sends a command to the device under test (DUT) to start the transmitter test. |
| niBluetoothDTM HCI LE Direction Finding Receiver Test | Sends a command to the device under test (DUT) to start the receiver test. |
| niBluetoothDTM Create Custom Command | Sends the specified custom command to the device under test (DUT). |
| niBluetoothDTM HCI LE Test End | Sends the command to the device under test (DUT) to end the transmitter or receiver test. |
| niBluetoothDTM HCI Reset | Resets the device under test (DUT) specified by the VISA resource name parameter. |
| niBluetoothDTM VISA Close Session | Closes a device session or the event object that you specify in the VISA resource name parameter. |

<!--NI_TOPIC bundle=rfmx-for-bluetooth-test-dtm path=lvbluetoothdtmvi/nibluetoothdtm_visa_close_session.html language=enus -->
## TOPIC 00065: niBluetoothDTM VISA Close Session (VI)

- bundle_id: `rfmx-for-bluetooth-test-dtm`
- source_path: `lvbluetoothdtmvi/nibluetoothdtm_visa_close_session.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-for-bluetooth-test-dtm/raw/resource/enus/lvbluetoothdtmvi/nibluetoothdtm_visa_close_session.html
- document_id: `rfmx-for-bluetooth-test-dtm`
- page_type: `leaf`
- content_type: ``

### niBluetoothDTM VISA Close Session (VI)

Owning Palette:

Bluetooth Direct Test Mode VIs

Closes a device session or the event object that you specify in the **VISA resource name** parameter.

[IMAGE alt='niBluetoothDTM VISA Close Session' src='nibluetoothdtm_visa_close_session.gif']

|  | VISA resource name specifies the name of the resource you want to close. This parameter also specifies the VISA session and class. |
| --- | --- |
|  | error out contains error information. This output provides standard error out functionality. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |

<!--NI_TOPIC bundle=rfmx-for-bluetooth-test-dtm path=lvbluetoothdtmvi/nibluetoothdtm_visa_configure_serial_settings.html language=enus -->
## TOPIC 00066: niBluetoothDTM VISA Configure Serial Settings (VI)

- bundle_id: `rfmx-for-bluetooth-test-dtm`
- source_path: `lvbluetoothdtmvi/nibluetoothdtm_visa_configure_serial_settings.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-for-bluetooth-test-dtm/raw/resource/enus/lvbluetoothdtmvi/nibluetoothdtm_visa_configure_serial_settings.html
- document_id: `rfmx-for-bluetooth-test-dtm`
- page_type: `leaf`
- content_type: ``

### niBluetoothDTM VISA Configure Serial Settings (VI)

Owning Palette:

Bluetooth Direct Test Mode VIs

Configures the VISA serial settings for the device under test (DUT) specified by the **VISA resource name** parameter.

[IMAGE alt='niBluetoothDTM VISA Configure Serial Settings' src='nibluetoothdtm_visa_configure_serial_settings.gif']

|  | VISA resource name specifies the name of the resource to be configured. This parameter also specifies the VISA session and class. |
| --- | --- |
|  | baud rate specifies the baud rate of the given communication port. The default value is 115,200. |
|  | flow control specifies the flow control method used for transmitting and receiving data. The default value is RTS/CTS. None (0) Does not use flow control, and the buffers on both sides of the connection are assumed to be large enough to hold all the transferred data. XON/XOFF (1) Uses the XON and XOFF characters to complete flow control. The transfer mechanism controls input flow by transmitting XOFF when the low-level I/O receive buffer is nearly full, and it controls the output flow by suspending transmission when XOFF is received. RTS/CTS (2) Uses the RTS output signal and the CTS input signal to complete flow control. The transfer mechanism controls input flow by unasserting the RTS signal when the low-level I/O receive buffer is nearly full. The transfer mechanism also controls output flow by suspending the transmission when the CTS signal is unasserted. XON/XOFF & RTS/CTS (3) Uses values of XON/XOFF and RTS/CTS. DTR/DSR (4) Uses the DTR output signal and the DSR input signal to complete flow control. The transfer mechanism controls input flow by unasserting the DTR signal when the low-level I/O receive buffer is nearly full. The transfer mechanism also controls output flow by suspending the transmission when the DSR signal is unasserted. XON/XOFF & DTR/DSR (5) Uses values of XON/XOFF and DTR/DSR. |
| None (0) | Does not use flow control, and the buffers on both sides of the connection are assumed to be large enough to hold all the transferred data. |
| XON/XOFF (1) | Uses the XON and XOFF characters to complete flow control. The transfer mechanism controls input flow by transmitting XOFF when the low-level I/O receive buffer is nearly full, and it controls the output flow by suspending transmission when XOFF is received. |
| RTS/CTS (2) | Uses the RTS output signal and the CTS input signal to complete flow control. The transfer mechanism controls input flow by unasserting the RTS signal when the low-level I/O receive buffer is nearly full. The transfer mechanism also controls output flow by suspending the transmission when the CTS signal is unasserted. |
| XON/XOFF & RTS/CTS (3) | Uses values of XON/XOFF and RTS/CTS. |
| DTR/DSR (4) | Uses the DTR output signal and the DSR input signal to complete flow control. The transfer mechanism controls input flow by unasserting the DTR signal when the low-level I/O receive buffer is nearly full. The transfer mechanism also controls output flow by suspending the transmission when the DSR signal is unasserted. |
| XON/XOFF & DTR/DSR (5) | Uses values of XON/XOFF and DTR/DSR. |
|  | stop bits specifies the number of stop bits used to indicate the end of a frame. The default value is 1.0. 1.0 (10) Specifies that the number of stop bits used is 1. 1.5 (15) Specifies that the number of stop bits used is 1.5. 2.0 (20) Specifies that the number of stop bits used is 2. |
| 1.0 (10) | Specifies that the number of stop bits used is 1. |
| 1.5 (15) | Specifies that the number of stop bits used is 1.5. |
| 2.0 (20) | Specifies that the number of stop bits used is 2. |
|  | data bits specifies the number of data bits contained in each frame. Valid values are 5 to 8, inclusive. The data bits for each frame are located in the low-order bits of every byte stored in the memory. The default value is 8. |
|  | parity specifies the parity bit used with each transmitted or received frame. The default value is None. None (0) Specifies that the frame does not contain a parity bit. Odd (1) Specifies that the parity is odd. Even (2) Specifies that the parity is even. Mark (3) Specifies that the parity bit is always 1. Space (4) Specifies that the parity bit is always 0. |
| None (0) | Specifies that the frame does not contain a parity bit. |
| Odd (1) | Specifies that the parity is odd. |
| Even (2) | Specifies that the parity is even. |
| Mark (3) | Specifies that the parity bit is always 1. |
| Space (4) | Specifies that the parity bit is always 0. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | VISA resource name out returns the resource name to which a VISA session is opened and the resource class. The class name matches the VISA resource name parameter. |
|  | error out contains error information. This output provides standard error out functionality. |

<!--NI_TOPIC bundle=rfmx-for-bluetooth-test-dtm path=lvbluetoothdtmvi/nibluetoothdtm_visa_open_session.html language=enus -->
## TOPIC 00067: niBluetoothDTM VISA Open Session (VI)

- bundle_id: `rfmx-for-bluetooth-test-dtm`
- source_path: `lvbluetoothdtmvi/nibluetoothdtm_visa_open_session.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-for-bluetooth-test-dtm/raw/resource/enus/lvbluetoothdtmvi/nibluetoothdtm_visa_open_session.html
- document_id: `rfmx-for-bluetooth-test-dtm`
- page_type: `leaf`
- content_type: ``

### niBluetoothDTM VISA Open Session (VI)

Owning Palette:

Bluetooth Direct Test Mode VIs

Opens a session of the device under test (DUT) specified by the **VISA resource name** parameter, and returns a session identifier that can be used to call any other operations on that DUT.

[IMAGE alt='niBluetoothDTM VISA Open Session' src='nibluetoothdtm_visa_open_session.gif']

|  | VISA resource name specifies the name of the resource to be opened. This parameter also specifies the VISA session and class. |
| --- | --- |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | VISA resource name out returns the resource name to which a VISA session is opened and the resource class. The class name matches the VISA resource name parameter. |
|  | error out contains error information. This output provides standard error out functionality. |

<!--NI_TOPIC bundle=rfmx-for-bluetooth-test-dtm path=lvbluetoothdtmvi/nibluetoothdtm_visa_set_timeout.html language=enus -->
## TOPIC 00068: niBluetoothDTM VISA Set Timeout (VI)

- bundle_id: `rfmx-for-bluetooth-test-dtm`
- source_path: `lvbluetoothdtmvi/nibluetoothdtm_visa_set_timeout.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-for-bluetooth-test-dtm/raw/resource/enus/lvbluetoothdtmvi/nibluetoothdtm_visa_set_timeout.html
- document_id: `rfmx-for-bluetooth-test-dtm`
- page_type: `leaf`
- content_type: ``

### niBluetoothDTM VISA Set Timeout (VI)

Owning Palette:

Bluetooth Direct Test Mode VIs

Sets the timeout value, in milliseconds (ms), for the VISA session of the device under test (DUT), specified by the **VISA resource name** parameter.

[IMAGE alt='niBluetoothDTM VISA Set Timeout' src='nibluetoothdtm_visa_set_timeout.gif']

|  | VISA resource name specifies the name of the resource for which you set the timeout value. This parameter also specifies the VISA session and class. |
| --- | --- |
|  | timeout specifies the minimum timeout value, in milliseconds (ms), to use when accessing the device. The default value is 2000. Note The actual timeout that VISA returns may be higher than the specified timeout. |
|  | Note The actual timeout that VISA returns may be higher than the specified timeout. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | VISA resource name out returns the resource name to which a VISA session is opened and the resource class. The class name matches the VISA resource name parameter. |
|  | error out contains error information. This output provides standard error out functionality. |
