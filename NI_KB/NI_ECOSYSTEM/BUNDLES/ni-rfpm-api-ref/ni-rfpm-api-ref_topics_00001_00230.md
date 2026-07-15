# NI DOCUMENT BUNDLE: ni-rfpm-api-ref

<!--NI_BUNDLE_CHUNK bundle=ni-rfpm-api-ref start=1 end=230 -->
<!--NI_TOPIC bundle=ni-rfpm-api-ref path=ninetrfpmfx40/netrfpmswitchmap.html language=enus -->
## TOPIC 00001: NI-RFPM Switch C API to NI-RFPM Switch .NET API Map

- bundle_id: `ni-rfpm-api-ref`
- source_path: `ninetrfpmfx40/netrfpmswitchmap.html`
- source_url: https://docs-be.ni.com/bundle/ni-rfpm-api-ref/raw/resource/enus/ninetrfpmfx40/netrfpmswitchmap.html
- document_id: `ni-rfpm-api-ref`
- page_type: `leaf`
- content_type: ``

NI-RFPM Switch C API to NI-RFPM Switch .NET API Map

| .NET Properties | Path | C Attributes |
| --- | --- | --- |
| RfpmSwitchDriverOperation.RangeCheck | rfpmSwitchSession.DriverOperation.RangeCheck | NIRFPMSWITCH_ATTR_RANGE_CHECK |
| RfpmSwitchDriverOperation.QueryInstrumentStatus | rfpmSwitchSession.DriverOperation.QueryInstrumentStatus | NIRFPMSWITCH_ATTR_QUERY_INSTRUMENT_STATUS |
| RfpmSwitchDriverOperation.Cache | rfpmSwitchSession.DriverOperation.Cache | NIRFPMSWITCH_ATTR_CACHE |
| RfpmSwitchDriverOperation.Simulate | rfpmSwitchSession.DriverOperation.Simulate | NIRFPMSWITCH_ATTR_SIMULATE |
| N/A | N/A | NIRFPMSWITCH_ATTR_RECORD_COERCIONS |
| N/A | N/A | NIRFPMSWITCH_ATTR_INTERCHANGE_CHECK |
| N/A | N/A | NIRFPMSWITCH_ATTR_SPECIFIC_DRIVER_PREFIX |
| RfpmSwitchDriverIdentity.GetSupportedInstrumentModels | rfpmSwitchSession.Identity.GetSupportedInstrumentModels() | NIRFPMSWITCH_ATTR_SUPPORTED_INSTRUMENT_MODELS |
| RfpmSwitchDriverIdentity.GetGroupCapabilities | rfpmSwitchSession.Identity.GetGroupCapabilities() | NIRFPMSWITCH_ATTR_GROUP_CAPABILITIES |
| RfpmSwitchDriverIdentity.InstrumentManufacturer | rfpmSwitchSession.Identity.InstrumentManufacturer | NIRFPMSWITCH_ATTR_INSTRUMENT_MANUFACTURER |
| RfpmSwitchDriverIdentity.InstrumentModel | rfpmSwitchSession.Identity.InstrumentModel | NIRFPMSWITCH_ATTR_INSTRUMENT_MODEL |
| RfpmSwitchDriverIdentity.InstrumentFirmwareRevision | rfpmSwitchSession.Identity.InstrumentFirmwareRevision | NIRFPMSWITCH_ATTR_INSTRUMENT_FIRMWARE_REVISION |
| RfpmSwitchDriverIdentity.Revision | rfpmSwitchSession.Identity.Revision | NIRFPMSWITCH_ATTR_SPECIFIC_DRIVER_REVISION |
| RfpmSwitchDriverIdentity.Vendor | rfpmSwitchSession.Identity.Vendor | NIRFPMSWITCH_ATTR_SPECIFIC_DRIVER_VENDOR |
| RfpmSwitchDriverIdentity.Description | rfpmSwitchSession.Identity.Description | NIRFPMSWITCH_ATTR_SPECIFIC_DRIVER_DESCRIPTION |
| N/A | N/A | NIRFPMSWITCH_ATTR_SPECIFIC_DRIVER_CLASS_SPEC_MAJOR_VERSION |
| N/A | N/A | NIRFPMSWITCH_ATTR_SPECIFIC_DRIVER_CLASS_SPEC_MINOR_VERSION |
| RfpmSwitchDriverOperation.LogicalName | rfpmSwitchSession.DriverOperation.LogicalName | NIRFPMSWITCH_ATTR_LOGICAL_NAME |
| RfpmSwitchDriverOperation.IOResourceDescriptor | rfpmSwitchSession.DriverOperation.IOResourceDescriptor | NIRFPMSWITCH_ATTR_IO_RESOURCE_DESCRIPTOR |
| RfpmSwitchDriverOperation.DriverSetup | rfpmSwitchSession.DriverOperation.DriverSetup | NIRFPMSWITCH_ATTR_DRIVER_SETUP |
| RfpmSwitchChannel.IsSourceChannel | rfpmSwitchSession.Channels[0].IsSourceChannel | NIRFPMSWITCH_ATTR_IS_SOURCE_CHANNEL |
| RfpmSwitchChannel.IsConfigurationChannel | rfpmSwitchSession.Channels[0].IsConfigurationChannel | NIRFPMSWITCH_ATTR_IS_CONFIGURATION_CHANNEL |
| RfpmSwitchPath.IsDebounced | rfpmSwitchSession.Path.IsDebounced | NIRFPMSWITCH_ATTR_IS_DEBOUNCED |
| RfpmSwitchCharacteristics.SettlingTime | rfpmSwitchSession.Channels[0].Characteristics.SettlingTime | NIRFPMSWITCH_ATTR_SETTLING_TIME |
| RfpmSwitchCharacteristics.Bandwidth | rfpmSwitchSession.Channels[0].Characteristics.Bandwidth | NIRFPMSWITCH_ATTR_BANDWIDTH |
| RfpmSwitchChannelCollection.Count | rfpmSwitchSession.Channels.Count | NIRFPMSWITCH_ATTR_CHANNEL_COUNT |
| RfpmSwitchCharacteristics.DCVoltageMax | rfpmSwitchSession.Channels[0].Characteristics.DCVoltageMax | NIRFPMSWITCH_ATTR_MAX_DC_VOLTAGE |
| RfpmSwitchCharacteristics.ACVoltageMax | rfpmSwitchSession.Channels[0].Characteristics.ACVoltageMax | NIRFPMSWITCH_ATTR_MAX_AC_VOLTAGE |
| RfpmSwitchCharacteristics.ACCurrentSwitchingMax | rfpmSwitchSession.Channels[0].Characteristics.ACCurrentSwitchingMax | NIRFPMSWITCH_ATTR_MAX_SWITCHING_AC_CURRENT |
| RfpmSwitchCharacteristics.DCCurrentSwitchingMax | rfpmSwitchSession.Channels[0].Characteristics.DCCurrentSwitchingMax | NIRFPMSWITCH_ATTR_MAX_SWITCHING_DC_CURRENT |
| RfpmSwitchCharacteristics.ACCurrentCarryMax | rfpmSwitchSession.Channels[0].Characteristics.ACCurrentCarryMax | NIRFPMSWITCH_ATTR_MAX_CARRY_AC_CURRENT |
| RfpmSwitchCharacteristics.DCCurrentCarryMax | rfpmSwitchSession.Channels[0].Characteristics.DCCurrentCarryMax | NIRFPMSWITCH_ATTR_MAX_CARRY_DC_CURRENT |
| RfpmSwitchCharacteristics.ACPowerSwitchingMax | rfpmSwitchSession.Channels[0].Characteristics.ACPowerSwitchingMax | NIRFPMSWITCH_ATTR_MAX_SWITCHING_AC_POWER |
| RfpmSwitchCharacteristics.DCPowerSwitchingMax | rfpmSwitchSession.Channels[0].Characteristics.DCPowerSwitchingMax | NIRFPMSWITCH_ATTR_MAX_SWITCHING_DC_POWER |
| RfpmSwitchCharacteristics.ACPowerCarryMax | rfpmSwitchSession.Channels[0].Characteristics.ACPowerCarryMax | NIRFPMSWITCH_ATTR_MAX_CARRY_AC_POWER |
| RfpmSwitchCharacteristics.DCPowerCarryMax | rfpmSwitchSession.Channels[0].Characteristics.DCPowerCarryMax | NIRFPMSWITCH_ATTR_MAX_CARRY_DC_POWER |
| RfpmSwitchCharacteristics.Impedance | rfpmSwitchSession.Channels[0].Characteristics.Impedance | NIRFPMSWITCH_ATTR_CHARACTERISTIC_IMPEDANCE |
| N/A | N/A | NIRFPMSWITCH_ATTR_NUM_OF_ROWS |
| N/A | N/A | NIRFPMSWITCH_ATTR_NUM_OF_COLUMNS |
| RfpmSwitchCharacteristics.WireMode | rfpmSwitchSession.Channels[0].Characteristics.WireMode | NIRFPMSWITCH_ATTR_WIRE_MODE |
| RfpmSwitchDriverUtility.DeviceTemperature | rfpmSwitchSession.Utility.DeviceTemperature | NIRFPMSWITCH_ATTR_DEVICE_TEMPERATURE |
| RfpmSwitchDriverUtility.ExternalPortCount | rfpmSwitchSession.Utility.ExternalPortCount | NIRFPMSWITCH_ATTR_NUMBER_OF_EXTERNAL_PORTS |
| RfpmSwitchChannel.PortType | rfpmSwitchSession.Channels[0].PortType | NIRFPMSWITCH_ATTR_PORT_TYPE |

| .NET Methods | Path | C Functions |
| --- | --- | --- |
| NIRfpmSwitch | rfpmSwitchSession = new NIRfpmSwitch(resourceName, idQuery, resetDevice) rfpmSwitchSession = new NIRfpmSwitch(resourceName, idQuery, resetDevice, lockType, accessKey) | niRFPMSwitch_init |
| NIRfpmSwitch | rfpmSwitchSession = NIRfpmSwitch(resourceName, idQuery, resetDevice, optionString) rfpmSwitchSession = NIRfpmSwitch(resourceName, idQuery, resetDevice, lockType, accessKey, optionString) | niRFPMSwitch_InitWithOptions |
| NIRfpmSwitch.Close | rfpmSwitchSession.Close() | niRFPMSwitch_close |
| N/A | N/A | niRFPMSwitch_LockSession |
| N/A | N/A | niRFPMSwitch_UnlockSession |
| RfpmSwitchChannel.Name | N/A | niRFPMSwitch_GetChannelName |
| RfpmSwitchPath.Connect | rfpmSwitchSession.Path.Connect(channel1, channel2) | niRFPMSwitch_Connect |
| RfpmSwitchPath.Disconnect | rfpmSwitchSession.Path.Disconnect(channel1, channel2) | niRFPMSwitch_Disconnect |
| RfpmSwitch.DisconnectAll | rfpmSwitchSession.Path.DisconnectAll() | niRFPMSwitch_DisconnectAll |
| RfpmSwitchPath.GetPath | rfpmSwitchSession.Path.GetPath(channel1, channel2) | niRFPMSwitch_GetPath |
| RfpmSwitchPath.SetPath | rfpmSwitchSession.Path.SetPath(pathDescription) | niRFPMSwitch_SetPath |
| RfpmSwitchPath.GetConnectedPaths | rfpmSwitchSession.Path.GetConnectedPaths() | niRFPMSwitch_ReadConnectedPaths |
| RfpmSwitchPath.GetConnectedPaths | rfpmSwitchSession.Path.GetConnectedPaths().Length | niRFPMSwitch_GetSizeOfConnectedPathsString |
| RfpmSwitchPath.CanConnect | rfpmSwitchSession.Path.CanConnect(channel1, channel2) | niRFPMSwitch_CanConnect |
| N/A |  | niRFPMSwitch_IsDebounced |
| RfpmSwitchPath.WaitForDebounce | rfpmSwitchSession.Path.WaitForDebounce(maxTime) | niRFPMSwitch_WaitForDebounce |
| RfpmSwitchPath.GetSettlingTime | rfpmSwitchSession.Path.GetSettlingTime(pathDescription, amplitudeSettlingAccuracy, frequency, power) | niRFPMSwitch_GetPathSettlingTime |
| RfpmSwitchDriverUtility.ErrorQuery | rfpmSwitchSession.Utility.ErrorQuery() | niRFPMSwitch_GetError |
| N/A | N/A | niRFPMSwitch_ClearError |
| N/A | N/A | niRFPMSwitch_error_message |
| N/A | N/A | niRFPMSwitch_error_query |
| RfpmSwitchDriverOperation.InvalidateAllAttributes | rfpmSwitchSession.DriverOperation.InvalidateAllAttributes() | niRFPMSwitch_InvalidateAllAttributes |
| RfpmSwitchDriverUtility.Reset | rfpmSwitchSession.Utility.Reset() | niRFPMSwitch_reset |
| RfpmSwitchDriverUtility.ResetDevice | rfpmSwitchSession.Utility.ResetDevice() | niRFPMSwitch_resetDevice |
| RfpmSwitchDriverUtility.ResetWithDefaults | rfpmSwitchSession.Utility.ResetWithDefaults() | niRFPMSwitch_ResetWithDefaults |
| RfpmSwitchDriverUtility.SelfTest | rfpmSwitchSession.Utility.SelfTest() | niRFPMSwitch_self_test |
| N/A | N/A | niRFPMSwitch_revision_query |
| RfpmSwitchDriverUtility.Disable | rfpmSwitchSession.Utility.Disable() | niRFPMSwitch_Disable |
| N/A | N/A | niRFPMSwitch_GetAttributeViInt32 |
| N/A | N/A | niRFPMSwitch_GetAttributeViReal64 |
| N/A | N/A | niRFPMSwitch_GetAttributeViString |
| N/A | N/A | niRFPMSwitch_GetAttributeViSession |
| N/A | N/A | niRFPMSwitch_GetAttributeViBoolean |
| N/A | N/A | niRFPMSwitch_SetAttributeViInt32 |
| N/A | N/A | niRFPMSwitch_SetAttributeViReal64 |
| N/A | N/A | niRFPMSwitch_SetAttributeViString |
| N/A | N/A | niRFPMSwitch_SetAttributeViSession |
| N/A | N/A | niRFPMSwitch_SetAttributeViBoolean |

Parent topic:

NI-RFPM .NET Class Library

<!--NI_TOPIC bundle=ni-rfpm-api-ref path=ninetrfpmfx40ref/html/00829925-a809-aa5c-83b0-3f8a9ef1ce3f.htm language=enus -->
## TOPIC 00002: ninetrfpmfx40ref/html/00829925-a809-aa5c-83b0-3f8a9ef1ce3f.htm

- bundle_id: `ni-rfpm-api-ref`
- source_path: `ninetrfpmfx40ref/html/00829925-a809-aa5c-83b0-3f8a9ef1ce3f.htm`
- source_url: https://docs-be.ni.com/bundle/ni-rfpm-api-ref/raw/resource/enus/ninetrfpmfx40ref/html/00829925-a809-aa5c-83b0-3f8a9ef1ce3f.htm
- document_id: `ni-rfpm-api-ref`
- page_type: `leaf`
- content_type: ``

RfpmMeasurementsDeembedding Methods

RfpmMeasurementsDeembedding Methods

The [RfpmMeasurementsDeembedding](ed036fc7-324d-406e-55b6-c8486627918a.htm) type exposes the following members.

##### Methods

|  | Name | Description |
| --- | --- | --- |
|  | Configure | Configures de-embedding for a specified port by providing a S2P file of the network to de-embed. |
|  | Equals | Determines whether the specified Object is equal to the current Object. (Inherited from Object.) |
|  | GetHashCode | Serves as a hash function for a particular type. (Inherited from Object.) |
|  | GetS2PFilePath | Gets the path to the S2P file that characterizes the de-embedding network for the given port. |
|  | GetS2POrientation | Gets the de-embedding network orientation. |
|  | GetType | Gets the Type of the current instance. (Inherited from Object.) |
|  | SetS2PFilePath | Sets the path to the S2P file that characterizes the de-embedding network for the given port. |
|  | SetS2POrientation | Gets the de-embedding network orientation. |
|  | ToString | Returns a string that represents the current object. (Inherited from Object.) |

Top

##### See Also

###### Reference

RfpmMeasurementsDeembedding Class

NationalInstruments.ModularInstruments.NIRfpm Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=ni-rfpm-api-ref path=ninetrfpmfx40ref/html/03b45d43-958f-77d0-785e-9c292d9f4055.htm language=enus -->
## TOPIC 00003: ninetrfpmfx40ref/html/03b45d43-958f-77d0-785e-9c292d9f4055.htm

- bundle_id: `ni-rfpm-api-ref`
- source_path: `ninetrfpmfx40ref/html/03b45d43-958f-77d0-785e-9c292d9f4055.htm`
- source_url: https://docs-be.ni.com/bundle/ni-rfpm-api-ref/raw/resource/enus/ninetrfpmfx40ref/html/03b45d43-958f-77d0-785e-9c292d9f4055.htm
- document_id: `ni-rfpm-api-ref`
- page_type: `leaf`
- content_type: ``

SourcePath Enumeration

SourcePath Enumeration

Namespace:

NationalInstruments.ModularInstruments.NIRfpm

Assembly:

##### Syntax

C#

VB

```text
public enum SourcePath
```

```text
Public Enumeration SourcePath
```

##### Members

|  | Member name | Value | Description |
| --- | --- | --- | --- |
|  | Direct | 0 | Uses the direct path through the NI-RFPM switch. This property does not support the mmWave subsystem. |
|  | Gain | 1 | Uses the amplified path through the NI-RFPM switch. This property does not support the mmWave subsystem. |
|  | Loop | 2 | Uses the path through the bypass loop of the NI-RFPM switch. This property does not support the mmWave subsystem. |
|  | Unspecified | 3 | Searches across all paths for offset data that matches the requested parameters. This property does not support the mmWave subsystem. |
|  | TwoTone | 4 | Uses the path through the two tone system. This property does not support the mmWave subsystem. |

##### See Also

###### Reference

NationalInstruments.ModularInstruments.NIRfpm Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=ni-rfpm-api-ref path=ninetrfpmfx40ref/html/0446f90c-e704-2939-6c78-400da7143224.htm language=enus -->
## TOPIC 00004: ninetrfpmfx40ref/html/0446f90c-e704-2939-6c78-400da7143224.htm

- bundle_id: `ni-rfpm-api-ref`
- source_path: `ninetrfpmfx40ref/html/0446f90c-e704-2939-6c78-400da7143224.htm`
- source_url: https://docs-be.ni.com/bundle/ni-rfpm-api-ref/raw/resource/enus/ninetrfpmfx40ref/html/0446f90c-e704-2939-6c78-400da7143224.htm
- document_id: `ni-rfpm-api-ref`
- page_type: `leaf`
- content_type: ``

RfpmSweepSettingsManager.LoadFromFile Method

RfpmSweepSettingsManagerLoadFromFile Method

Loads a sweep settings file into memory so that measurements are performed according to
 the sweeps defined in the file.

Namespace:

NationalInstruments.ModularInstruments.NIRfpm

Assembly:

##### Syntax

C#

VB

```text
public void LoadFromFile(
	string sweepSettingsFilePath
)
```

```text
Public Sub LoadFromFile ( 
	sweepSettingsFilePath As String
)
```

###### Parameters

- **sweepSettingsFilePath**
  - Type: SystemString The file path to the sweep settings file to be loaded into the driver.

##### Exceptions

| Exception | Condition |
| --- | --- |
| FileNotFoundException | The specified sweep settings file was not found. - or - The value for sweepSettingsFilePath is . |
| ObjectDisposedException | LoadFromFile(String) was called after the associated NIRfpm or RfpmDriverUtility object was disposed. |
| IviCDriverException | The file revision is not supported. - or - The file is not the correct format. - or - The underlying NI-RFPM driver returned an error. |

##### Remarks

Once sweep settings are loaded, you may call
 [GetSweepSettings](b4c6d59d-0c1e-650d-cffe-9d5c45ffb82c.htm)
 or
 [GetSweepSetting(String)](40116a7e-4a65-95bb-2512-dca35bf8fda9.htm)
 to get information about the loaded sweep settings.

You can load multiple sweep settings files by calling this method multiple times. If the
 sweep name is already present, the last loaded value is retained.

The NI-RFPM .NET API is sweep-centric, meaning the API focuses on the sweep settings file
 (formerly known as the Cal Config file) as the single point of defining measurement
 parameters. You create the sweep settings file for a given set of named sweeps which are
 then called out by name when performing calibrations and measurements.

Refer to the
 [Using the Sweep Settings Configuration File](../rfpmhelp/sweep_setting_configuration_file.html)
 and
 [Specifying Setting Parameters](../rfpmhelp/specifying_setting_parameters.html) topics for more information on the sweep settings file.

##### See Also

###### Reference

RfpmSweepSettingsManager Class

NationalInstruments.ModularInstruments.NIRfpm Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=ni-rfpm-api-ref path=ninetrfpmfx40ref/html/16d2e514-2976-37de-003e-f3b02a91e2ce.htm language=enus -->
## TOPIC 00005: ninetrfpmfx40ref/html/16d2e514-2976-37de-003e-f3b02a91e2ce.htm

- bundle_id: `ni-rfpm-api-ref`
- source_path: `ninetrfpmfx40ref/html/16d2e514-2976-37de-003e-f3b02a91e2ce.htm`
- source_url: https://docs-be.ni.com/bundle/ni-rfpm-api-ref/raw/resource/enus/ninetrfpmfx40ref/html/16d2e514-2976-37de-003e-f3b02a91e2ce.htm
- document_id: `ni-rfpm-api-ref`
- page_type: `leaf`
- content_type: ``

RfpmVectorUserCalibration.IsAbsoluteCalibrationEnabled Property

RfpmVectorUserCalibrationIsAbsoluteCalibrationEnabled Property

Namespace:

NationalInstruments.ModularInstruments.NIRfpm

Assembly:

##### Syntax

C#

VB

```text
public bool IsAbsoluteCalibrationEnabled { get; set; }
```

```text
Public Property IsAbsoluteCalibrationEnabled As Boolean
	Get
	Set
```

###### Property Value

Boolean

##### Exceptions

| Exception | Condition |
| --- | --- |
| ObjectDisposedException | IsAbsoluteCalibrationEnabled was accessed after the associated NIRfpm or RfpmDriverUtility object was disposed. |
| IviCDriverException | The underlying NI-RFPM driver returned an error. |

##### See Also

###### Reference

RfpmVectorUserCalibration Class

NationalInstruments.ModularInstruments.NIRfpm Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=ni-rfpm-api-ref path=ninetrfpmfx40ref/html/19a71931-211f-70be-e383-3d891cd5897e.htm language=enus -->
## TOPIC 00006: ninetrfpmfx40ref/html/19a71931-211f-70be-e383-3d891cd5897e.htm

- bundle_id: `ni-rfpm-api-ref`
- source_path: `ninetrfpmfx40ref/html/19a71931-211f-70be-e383-3d891cd5897e.htm`
- source_url: https://docs-be.ni.com/bundle/ni-rfpm-api-ref/raw/resource/enus/ninetrfpmfx40ref/html/19a71931-211f-70be-e383-3d891cd5897e.htm
- document_id: `ni-rfpm-api-ref`
- page_type: `leaf`
- content_type: ``

RfpmUserCalibrationInformation Structure

RfpmUserCalibrationInformation Structure

Namespace:

NationalInstruments.ModularInstruments.NIRfpm

Assembly:

##### Syntax

C#

VB

```text
public struct RfpmUserCalibrationInformation
```

```text
Public Structure RfpmUserCalibrationInformation
```

The RfpmUserCalibrationInformation type exposes the following members.

##### Properties

|  | Name | Description |
| --- | --- | --- |
|  | PortNames | Gets the names of ports that were included in the calibration. This property does not support the mmWave subsystem. |
|  | SweepSettingName | Gets the name of a sweep setting that was calibrated. This property does not support the mmWave subsystem. |
|  | Temperature | Gets the temperature of the RFPM instrument at the time the calibration was performed. This property does not support the mmWave subsystem. |
|  | TimeStamp | Gets a PrecisionDateTime object representing the timestamp when calibration was performed. This property does not support the mmWave subsystem. |

Top

##### Methods

|  | Name | Description |
| --- | --- | --- |
|  | Equals | Indicates whether this instance and a specified object are equal. (Inherited from ValueType.) |
|  | GetHashCode | Returns the hash code for this instance. (Inherited from ValueType.) |
|  | GetType | Gets the Type of the current instance. (Inherited from Object.) |
|  | ToString | Returns the fully qualified type name of this instance. (Inherited from ValueType.) |

Top

##### Remarks

The user calibration information consists of sweep name, list of ports, timestamp, and temperature.

##### Thread Safety

static

Shared

##### See Also

###### Reference

NationalInstruments.ModularInstruments.NIRfpm Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=ni-rfpm-api-ref path=ninetrfpmfx40ref/html/1ce7c9dd-0fe0-d4cf-dff3-cffcc904e905.htm language=enus -->
## TOPIC 00007: ninetrfpmfx40ref/html/1ce7c9dd-0fe0-d4cf-dff3-cffcc904e905.htm

- bundle_id: `ni-rfpm-api-ref`
- source_path: `ninetrfpmfx40ref/html/1ce7c9dd-0fe0-d4cf-dff3-cffcc904e905.htm`
- source_url: https://docs-be.ni.com/bundle/ni-rfpm-api-ref/raw/resource/enus/ninetrfpmfx40ref/html/1ce7c9dd-0fe0-d4cf-dff3-cffcc904e905.htm
- document_id: `ni-rfpm-api-ref`
- page_type: `leaf`
- content_type: ``

RfpmReceiverUserCalibration Properties

RfpmReceiverUserCalibration Properties

The [RfpmReceiverUserCalibration](1b28ea28-8eb0-b888-e662-490a8949870a.htm) type exposes the following members.

##### Properties

|  | Name | Description |
| --- | --- | --- |
|  | IsScalarCalibrationEnabled | Gets or sets a value indicating whether to collect receiver scalar error coefficients when performing auto calibration. This property does not support the mmWave subsystem. |

Top

##### See Also

###### Reference

RfpmReceiverUserCalibration Class

NationalInstruments.ModularInstruments.NIRfpm Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=ni-rfpm-api-ref path=ninetrfpmfx40ref/html/2232c5a4-2c81-a99a-4102-28445b5f58a7.htm language=enus -->
## TOPIC 00008: ninetrfpmfx40ref/html/2232c5a4-2c81-a99a-4102-28445b5f58a7.htm

- bundle_id: `ni-rfpm-api-ref`
- source_path: `ninetrfpmfx40ref/html/2232c5a4-2c81-a99a-4102-28445b5f58a7.htm`
- source_url: https://docs-be.ni.com/bundle/ni-rfpm-api-ref/raw/resource/enus/ninetrfpmfx40ref/html/2232c5a4-2c81-a99a-4102-28445b5f58a7.htm
- document_id: `ni-rfpm-api-ref`
- page_type: `leaf`
- content_type: ``

RfpmUtilityForSwitch.DisconnectAll Method

RfpmUtilityForSwitchDisconnectAll Method

Namespace:

NationalInstruments.ModularInstruments.NIRfpm

Assembly:

##### Syntax

C#

VB

```text
public void DisconnectAll(
	TimeSpan maxTime
)
```

```text
Public Sub DisconnectAll ( 
	maxTime As TimeSpan
)
```

###### Parameters

- **maxTime**
  - Type: SystemTimeSpan The time to wait for the method to complete operation before throwing an exception.

##### Exceptions

| Exception | Condition |
| --- | --- |
| ObjectDisposedException | DisconnectAll(TimeSpan) was called after the associated NIRfpm or RfpmDriverUtility object was disposed. |
| ArgumentException | Negative time was passed for maxTime. |
| IviCDriverException | The underlying NI-RFPM driver returned an error. |

##### See Also

###### Reference

RfpmUtilityForSwitch Class

NationalInstruments.ModularInstruments.NIRfpm Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=ni-rfpm-api-ref path=ninetrfpmfx40ref/html/2297f763-18ce-72b6-3354-49527adba90e.htm language=enus -->
## TOPIC 00009: ninetrfpmfx40ref/html/2297f763-18ce-72b6-3354-49527adba90e.htm

- bundle_id: `ni-rfpm-api-ref`
- source_path: `ninetrfpmfx40ref/html/2297f763-18ce-72b6-3354-49527adba90e.htm`
- source_url: https://docs-be.ni.com/bundle/ni-rfpm-api-ref/raw/resource/enus/ninetrfpmfx40ref/html/2297f763-18ce-72b6-3354-49527adba90e.htm
- document_id: `ni-rfpm-api-ref`
- page_type: `leaf`
- content_type: ``

NIRfpm.IsDisposed Property

NIRfpmIsDisposed Property

Gets a value indicating whether the session has been disposed.

Namespace:

NationalInstruments.ModularInstruments.NIRfpm

Assembly:

##### Syntax

C#

VB

```text
public bool IsDisposed { get; }
```

```text
Public ReadOnly Property IsDisposed As Boolean
	Get
```

###### Property Value

Boolean

NIRfpm

##### See Also

###### Reference

NIRfpm Class

NationalInstruments.ModularInstruments.NIRfpm Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=ni-rfpm-api-ref path=ninetrfpmfx40ref/html/262da693-5d06-495a-7196-3abf0ff2cf2b.htm language=enus -->
## TOPIC 00010: ninetrfpmfx40ref/html/262da693-5d06-495a-7196-3abf0ff2cf2b.htm

- bundle_id: `ni-rfpm-api-ref`
- source_path: `ninetrfpmfx40ref/html/262da693-5d06-495a-7196-3abf0ff2cf2b.htm`
- source_url: https://docs-be.ni.com/bundle/ni-rfpm-api-ref/raw/resource/enus/ninetrfpmfx40ref/html/262da693-5d06-495a-7196-3abf0ff2cf2b.htm
- document_id: `ni-rfpm-api-ref`
- page_type: `leaf`
- content_type: ``

RfpmDriverOperation.InvalidateAllAttributes Method

RfpmDriverOperationInvalidateAllAttributes Method

Sets all cached property values to invalid.

Namespace:

NationalInstruments.ModularInstruments.NIRfpm

Assembly:

##### Syntax

C#

VB

```text
public void InvalidateAllAttributes()
```

```text
Public Sub InvalidateAllAttributes
```

###### Implements

##### Exceptions

| Exception | Condition |
| --- | --- |
| ObjectDisposedException | InvalidateAllAttributes was called after the associated NIRfpm or RfpmDriverUtility object was disposed. |
| IviCDriverException | The underlying NI-RFPM driver returned an error. |

##### Remarks

The first time you query a driver property after calling this method, NI-RFPM queries the property value from the device.

##### See Also

###### Reference

RfpmDriverOperation Class

NationalInstruments.ModularInstruments.NIRfpm Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=ni-rfpm-api-ref path=ninetrfpmfx40ref/html/3664a29e-5f67-9bcf-56a9-1514a8c25467.htm language=enus -->
## TOPIC 00011: ninetrfpmfx40ref/html/3664a29e-5f67-9bcf-56a9-1514a8c25467.htm

- bundle_id: `ni-rfpm-api-ref`
- source_path: `ninetrfpmfx40ref/html/3664a29e-5f67-9bcf-56a9-1514a8c25467.htm`
- source_url: https://docs-be.ni.com/bundle/ni-rfpm-api-ref/raw/resource/enus/ninetrfpmfx40ref/html/3664a29e-5f67-9bcf-56a9-1514a8c25467.htm
- document_id: `ni-rfpm-api-ref`
- page_type: `leaf`
- content_type: ``

RfpmSubObject Class

RfpmSubObject Class

Represents members that are common to all sub-object NI-RFPM classes.

##### Inheritance Hierarchy

More...

Namespace:

NationalInstruments.ModularInstruments.NIRfpm

Assembly:

##### Syntax

C#

VB

```text
public abstract class RfpmSubObject
```

```text
Public MustInherit Class RfpmSubObject
```

The RfpmSubObject type exposes the following members.

##### Methods

|  | Name | Description |
| --- | --- | --- |
|  | Equals | Determines whether the specified Object is equal to the current Object. (Inherited from Object.) |
|  | Finalize | Allows an object to try to free resources and perform other cleanup operations before it is reclaimed by garbage collection. (Inherited from Object.) |
|  | GetHashCode | Serves as a hash function for a particular type. (Inherited from Object.) |
|  | GetType | Gets the Type of the current instance. (Inherited from Object.) |
|  | MemberwiseClone | Creates a shallow copy of the current Object. (Inherited from Object.) |
|  | ToString | Returns a string that represents the current object. (Inherited from Object.) |

Top

##### Remarks

Contains members that are common to all sub-object NI-RFPM classes.

##### Thread Safety

static

Shared

##### See Also

###### Reference

NationalInstruments.ModularInstruments.NIRfpm Namespace

##### Inheritance Hierarchy

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=ni-rfpm-api-ref path=ninetrfpmfx40ref/html/36c5759c-24a8-e2f1-ecfb-85f04a479745.htm language=enus -->
## TOPIC 00012: ninetrfpmfx40ref/html/36c5759c-24a8-e2f1-ecfb-85f04a479745.htm

- bundle_id: `ni-rfpm-api-ref`
- source_path: `ninetrfpmfx40ref/html/36c5759c-24a8-e2f1-ecfb-85f04a479745.htm`
- source_url: https://docs-be.ni.com/bundle/ni-rfpm-api-ref/raw/resource/enus/ninetrfpmfx40ref/html/36c5759c-24a8-e2f1-ecfb-85f04a479745.htm
- document_id: `ni-rfpm-api-ref`
- page_type: `leaf`
- content_type: ``

OptimizationMethod Enumeration

OptimizationMethod Enumeration

NIRfpm

Namespace:

NationalInstruments.ModularInstruments.NIRfpm

Assembly:

##### Syntax

C#

VB

```text
public enum OptimizationMethod
```

```text
Public Enumeration OptimizationMethod
```

##### Members

|  | Member name | Value | Description |
| --- | --- | --- | --- |
|  | Normal | 0 | Look up the NIRfpm path to use based on the peak power in order to use state freeze to achieve the best absolute amplitude accuracy. This property does not support the mmWave subsystem. |
|  | OptimizeForDynamicRange | 1 | Look up the NIRfpm path to use based on average power to optimize dynamic range, which benefits EVM and other measurements at the cost of maintaining the state freeze and absolute amplitude accuracy. This property does not support the mmWave subsystem. |

##### See Also

###### Reference

NationalInstruments.ModularInstruments.NIRfpm Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=ni-rfpm-api-ref path=ninetrfpmfx40ref/html/3712048c-05e5-f1db-5909-8003b1eb64a7.htm language=enus -->
## TOPIC 00013: ninetrfpmfx40ref/html/3712048c-05e5-f1db-5909-8003b1eb64a7.htm

- bundle_id: `ni-rfpm-api-ref`
- source_path: `ninetrfpmfx40ref/html/3712048c-05e5-f1db-5909-8003b1eb64a7.htm`
- source_url: https://docs-be.ni.com/bundle/ni-rfpm-api-ref/raw/resource/enus/ninetrfpmfx40ref/html/3712048c-05e5-f1db-5909-8003b1eb64a7.htm
- document_id: `ni-rfpm-api-ref`
- page_type: `leaf`
- content_type: ``

RfpmSweepSetting.PortCount Property

RfpmSweepSettingPortCount Property

Gets the number of ports for the sweep as defined in a currently loaded sweep settings file.

Namespace:

NationalInstruments.ModularInstruments.NIRfpm

Assembly:

##### Syntax

C#

VB

```text
public int PortCount { get; }
```

```text
Public ReadOnly Property PortCount As Integer
	Get
```

###### Property Value

Int32

##### See Also

###### Reference

RfpmSweepSetting Class

NationalInstruments.ModularInstruments.NIRfpm Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=ni-rfpm-api-ref path=ninetrfpmfx40ref/html/3712842e-bdb4-0080-a1de-ee4e13f6064a.htm language=enus -->
## TOPIC 00014: ninetrfpmfx40ref/html/3712842e-bdb4-0080-a1de-ee4e13f6064a.htm

- bundle_id: `ni-rfpm-api-ref`
- source_path: `ninetrfpmfx40ref/html/3712842e-bdb4-0080-a1de-ee4e13f6064a.htm`
- source_url: https://docs-be.ni.com/bundle/ni-rfpm-api-ref/raw/resource/enus/ninetrfpmfx40ref/html/3712842e-bdb4-0080-a1de-ee4e13f6064a.htm
- document_id: `ni-rfpm-api-ref`
- page_type: `leaf`
- content_type: ``

RfpmSweepSetting Class

RfpmSweepSetting Class

Provides properties describing a sweep setting.

##### Inheritance Hierarchy

Namespace:

NationalInstruments.ModularInstruments.NIRfpm

Assembly:

##### Syntax

C#

VB

```text
public sealed class RfpmSweepSetting
```

```text
Public NotInheritable Class RfpmSweepSetting
```

The RfpmSweepSetting type exposes the following members.

##### Properties

|  | Name | Description |
| --- | --- | --- |
|  | Name | Gets the name of the sweep setting. |
|  | PointCount | Gets the number of measurement points for the sweep as defined in a currently loaded sweep settings file. |
|  | PortCount | Gets the number of ports for the sweep as defined in a currently loaded sweep settings file. |

Top

##### Methods

|  | Name | Description |
| --- | --- | --- |
|  | Equals | Determines whether the specified Object is equal to the current Object. (Inherited from Object.) |
|  | GetHashCode | Serves as a hash function for a particular type. (Inherited from Object.) |
|  | GetType | Gets the Type of the current instance. (Inherited from Object.) |
|  | ToString | Returns a string that represents the current object. (Inherited from Object.) |

Top

##### Remarks

Obtain RfpmSweepSetting objects by calling
 [GetSweepSettings](b4c6d59d-0c1e-650d-cffe-9d5c45ffb82c.htm)
 or
 [GetSweepSetting(String)](40116a7e-4a65-95bb-2512-dca35bf8fda9.htm)
 after loading a sweep settings file into memory using
 [LoadFromFile(String)](0446f90c-e704-2939-6c78-400da7143224.htm).

Refer to the [Using the Sweep Settings Configuration File](../rfpmhelp/sweep_setting_configuration_file.html) and
 [Specifying Setting Parameters](../rfpmhelp/specifying_setting_parameters.html) topics for more information on the sweep settings file.

##### Thread Safety

static

Shared

##### See Also

###### Reference

NationalInstruments.ModularInstruments.NIRfpm Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=ni-rfpm-api-ref path=ninetrfpmfx40ref/html/40116a7e-4a65-95bb-2512-dca35bf8fda9.htm language=enus -->
## TOPIC 00015: ninetrfpmfx40ref/html/40116a7e-4a65-95bb-2512-dca35bf8fda9.htm

- bundle_id: `ni-rfpm-api-ref`
- source_path: `ninetrfpmfx40ref/html/40116a7e-4a65-95bb-2512-dca35bf8fda9.htm`
- source_url: https://docs-be.ni.com/bundle/ni-rfpm-api-ref/raw/resource/enus/ninetrfpmfx40ref/html/40116a7e-4a65-95bb-2512-dca35bf8fda9.htm
- document_id: `ni-rfpm-api-ref`
- page_type: `leaf`
- content_type: ``

RfpmSweepSettingsManager.GetSweepSetting Method

RfpmSweepSettingsManagerGetSweepSetting Method

Gets a sweep setting by name.

Namespace:

NationalInstruments.ModularInstruments.NIRfpm

Assembly:

##### Syntax

C#

VB

```text
public RfpmSweepSetting GetSweepSetting(
	string name
)
```

```text
Public Function GetSweepSetting ( 
	name As String
) As RfpmSweepSetting
```

###### Parameters

- **name**
  - Type: SystemString The name of the sweep setting defined in a loaded sweep settings file.

###### Return Value

RfpmSweepSetting

RfpmSweepSetting

##### Exceptions

| Exception | Condition |
| --- | --- |
| ArgumentException | The specified name is invalid. |
| ArgumentNullException | The value for name is . |
| ObjectDisposedException | GetSweepSetting(String) was called after the associated NIRfpm or RfpmDriverUtility object was disposed. |
| IviCDriverException | GetSweepSetting(String) was called before loading sweep settings using LoadFromFile(String). - or - The underlying NI-RFPM driver returned an error. |

##### Remarks

LoadFromFile(String)

##### See Also

###### Reference

RfpmSweepSettingsManager Class

NationalInstruments.ModularInstruments.NIRfpm Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=ni-rfpm-api-ref path=ninetrfpmfx40ref/html/403211f8-89ca-425f-f9c8-46155f810fc9.htm language=enus -->
## TOPIC 00016: ninetrfpmfx40ref/html/403211f8-89ca-425f-f9c8-46155f810fc9.htm

- bundle_id: `ni-rfpm-api-ref`
- source_path: `ninetrfpmfx40ref/html/403211f8-89ca-425f-f9c8-46155f810fc9.htm`
- source_url: https://docs-be.ni.com/bundle/ni-rfpm-api-ref/raw/resource/enus/ninetrfpmfx40ref/html/403211f8-89ca-425f-f9c8-46155f810fc9.htm
- document_id: `ni-rfpm-api-ref`
- page_type: `leaf`
- content_type: ``

RfpmMeasurements.Initiate Method (String, String)

RfpmMeasurementsInitiate Method (String, String)

Initiates a measurement on the specified ports, using the specified sweep setting defined in the sweep settings file.

Namespace:

NationalInstruments.ModularInstruments.NIRfpm

Assembly:

##### Syntax

C#

VB

```text
public void Initiate(
	string ports,
	string sweepSettingName
)
```

```text
Public Sub Initiate ( 
	ports As String,
	sweepSettingName As String
)
```

###### Parameters

- **ports**
  - Type: SystemString A comma-separated list of the ports to be measured.
- **sweepSettingName**
  - Type: SystemString The name of the sweep in the sweep settings file.

##### Exceptions

| Exception | Condition |
| --- | --- |
| ObjectDisposedException | Initiate(String, String) was called after the associated NIRfpm or RfpmDriverUtility object was disposed. |
| ArgumentNullException | The value for ports is . - or - The value for sweepSettingName is . |
| ArgumentException | The value for sweepSettingName is invalid. - or - The value for sweepSettingName is unknown. - or - The value for sweepSettingName is Empty. |
| InvalidOperationException | Initiate was called before performing calibration. |
| SelectorNameException | The value for ports is invalid. - or - The value for ports is unknown. |
| IviCDriverException | The value for ports is Empty. - or - The underlying NI-RFPM driver returned an error. |

##### Remarks

Initiate(String, String)

Perform the initiate with one of the sweep setting names from
 [GetSweepSettings](b4c6d59d-0c1e-650d-cffe-9d5c45ffb82c.htm) .

##### See Also

###### Reference

RfpmMeasurements Class

Initiate Overload

NationalInstruments.ModularInstruments.NIRfpm Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=ni-rfpm-api-ref path=ninetrfpmfx40ref/html/411d6d7b-b997-f734-8777-6b069695dc7c.htm language=enus -->
## TOPIC 00017: ninetrfpmfx40ref/html/411d6d7b-b997-f734-8777-6b069695dc7c.htm

- bundle_id: `ni-rfpm-api-ref`
- source_path: `ninetrfpmfx40ref/html/411d6d7b-b997-f734-8777-6b069695dc7c.htm`
- source_url: https://docs-be.ni.com/bundle/ni-rfpm-api-ref/raw/resource/enus/ninetrfpmfx40ref/html/411d6d7b-b997-f734-8777-6b069695dc7c.htm
- document_id: `ni-rfpm-api-ref`
- page_type: `leaf`
- content_type: ``

RfpmReceiverUserCalibration.IsScalarCalibrationEnabled Property

RfpmReceiverUserCalibrationIsScalarCalibrationEnabled Property

Namespace:

NationalInstruments.ModularInstruments.NIRfpm

Assembly:

##### Syntax

C#

VB

```text
public bool IsScalarCalibrationEnabled { get; set; }
```

```text
Public Property IsScalarCalibrationEnabled As Boolean
	Get
	Set
```

###### Property Value

Boolean

##### Exceptions

| Exception | Condition |
| --- | --- |
| ObjectDisposedException | IsScalarCalibrationEnabled was accessed after the associated NIRfpm or RfpmDriverUtility object was disposed. |
| IviCDriverException | The underlying NI-RFPM driver returned an error. |

##### See Also

###### Reference

RfpmReceiverUserCalibration Class

NationalInstruments.ModularInstruments.NIRfpm Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=ni-rfpm-api-ref path=ninetrfpmfx40ref/html/415583c1-4bd6-cc3b-7e29-abd578341f5e.htm language=enus -->
## TOPIC 00018: ninetrfpmfx40ref/html/415583c1-4bd6-cc3b-7e29-abd578341f5e.htm

- bundle_id: `ni-rfpm-api-ref`
- source_path: `ninetrfpmfx40ref/html/415583c1-4bd6-cc3b-7e29-abd578341f5e.htm`
- source_url: https://docs-be.ni.com/bundle/ni-rfpm-api-ref/raw/resource/enus/ninetrfpmfx40ref/html/415583c1-4bd6-cc3b-7e29-abd578341f5e.htm
- document_id: `ni-rfpm-api-ref`
- page_type: `leaf`
- content_type: ``

RfpmReceiverUserCalibration Methods

RfpmReceiverUserCalibration Methods

The [RfpmReceiverUserCalibration](1b28ea28-8eb0-b888-e662-490a8949870a.htm) type exposes the following members.

##### Methods

|  | Name | Description |
| --- | --- | --- |
|  | Equals | Determines whether the specified Object is equal to the current Object. (Inherited from Object.) |
|  | GetHashCode | Serves as a hash function for a particular type. (Inherited from Object.) |
|  | GetType | Gets the Type of the current instance. (Inherited from Object.) |
|  | ReadInformation | Returns information about receiver calibrations performed, indicating which sweep setting was used and which ports were calibrated using the sweep setting. This property does not support the mmWave subsystem. |
|  | ToString | Returns a string that represents the current object. (Inherited from Object.) |

Top

##### See Also

###### Reference

RfpmReceiverUserCalibration Class

NationalInstruments.ModularInstruments.NIRfpm Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=ni-rfpm-api-ref path=ninetrfpmfx40ref/html/423918c4-9c62-a105-6293-1cabb44cf565.htm language=enus -->
## TOPIC 00019: ninetrfpmfx40ref/html/423918c4-9c62-a105-6293-1cabb44cf565.htm

- bundle_id: `ni-rfpm-api-ref`
- source_path: `ninetrfpmfx40ref/html/423918c4-9c62-a105-6293-1cabb44cf565.htm`
- source_url: https://docs-be.ni.com/bundle/ni-rfpm-api-ref/raw/resource/enus/ninetrfpmfx40ref/html/423918c4-9c62-a105-6293-1cabb44cf565.htm
- document_id: `ni-rfpm-api-ref`
- page_type: `leaf`
- content_type: ``

RfpmReceiverCalibration.IsPowerCorrectionEnabled Property

RfpmReceiverCalibrationIsPowerCorrectionEnabled Property

Namespace:

NationalInstruments.ModularInstruments.NIRfpm

Assembly:

##### Syntax

C#

VB

```text
public bool IsPowerCorrectionEnabled { get; set; }
```

```text
Public Property IsPowerCorrectionEnabled As Boolean
	Get
	Set
```

###### Property Value

Boolean

##### Exceptions

| Exception | Condition |
| --- | --- |
| ObjectDisposedException | IsPowerCorrectionEnabled was accessed after the associated NIRfpm or RfpmDriverUtility object was disposed. |
| IviCDriverException | The underlying NI-RFPM driver returned an error. |

##### See Also

###### Reference

RfpmReceiverCalibration Class

NationalInstruments.ModularInstruments.NIRfpm Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=ni-rfpm-api-ref path=ninetrfpmfx40ref/html/449e6d2e-33e2-b042-6449-857a5ec3ecc3.htm language=enus -->
## TOPIC 00020: ninetrfpmfx40ref/html/449e6d2e-33e2-b042-6449-857a5ec3ecc3.htm

- bundle_id: `ni-rfpm-api-ref`
- source_path: `ninetrfpmfx40ref/html/449e6d2e-33e2-b042-6449-857a5ec3ecc3.htm`
- source_url: https://docs-be.ni.com/bundle/ni-rfpm-api-ref/raw/resource/enus/ninetrfpmfx40ref/html/449e6d2e-33e2-b042-6449-857a5ec3ecc3.htm
- document_id: `ni-rfpm-api-ref`
- page_type: `leaf`
- content_type: ``

RfpmDriverUtility.Lock Method

RfpmDriverUtilityLock Method

Acquires a synchronization lock on this instance of the driver.

Namespace:

NationalInstruments.ModularInstruments.NIRfpm

Assembly:

##### Syntax

C#

VB

```text
public IIviDriverLock Lock()
```

```text
Public Function Lock As IIviDriverLock
```

###### Return Value

IIviDriverLock

###### Implements

##### Exceptions

| Exception | Condition |
| --- | --- |
| ObjectDisposedException | Lock was called after the associated RfpmDriverUtility object was disposed. |

##### See Also

###### Reference

RfpmDriverUtility Class

Lock Overload

NationalInstruments.ModularInstruments.NIRfpm Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=ni-rfpm-api-ref path=ninetrfpmfx40ref/html/499cb326-5070-d1e7-91b9-6dcd627dd494.htm language=enus -->
## TOPIC 00021: ninetrfpmfx40ref/html/499cb326-5070-d1e7-91b9-6dcd627dd494.htm

- bundle_id: `ni-rfpm-api-ref`
- source_path: `ninetrfpmfx40ref/html/499cb326-5070-d1e7-91b9-6dcd627dd494.htm`
- source_url: https://docs-be.ni.com/bundle/ni-rfpm-api-ref/raw/resource/enus/ninetrfpmfx40ref/html/499cb326-5070-d1e7-91b9-6dcd627dd494.htm
- document_id: `ni-rfpm-api-ref`
- page_type: `leaf`
- content_type: ``

RfpmMeasurements.VectorReceiverAmplitudeSettlingAccuracy Property

RfpmMeasurementsVectorReceiverAmplitudeSettlingAccuracy Property

Namespace:

NationalInstruments.ModularInstruments.NIRfpm

Assembly:

##### Syntax

C#

VB

```text
public double VectorReceiverAmplitudeSettlingAccuracy { get; set; }
```

```text
Public Property VectorReceiverAmplitudeSettlingAccuracy As Double
	Get
	Set
```

###### Property Value

Double

##### Exceptions

| Exception | Condition |
| --- | --- |
| ObjectDisposedException | VectorReceiverAmplitudeSettlingAccuracy was accessed after the associated NIRfpm or RfpmDriverUtility object was disposed. |
| ArgumentException | The value set was invalid. |
| IviCDriverException | The underlying NI-RFPM driver returned an error. |

##### Remarks

This value is used by NI-RFPM to account for receiver settling during measurements.
 Valid values are 0.5 dB, 0.2 dB, 0.1 dB, and 0.05 dB.

##### See Also

###### Reference

RfpmMeasurements Class

NationalInstruments.ModularInstruments.NIRfpm Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=ni-rfpm-api-ref path=ninetrfpmfx40ref/html/6504a0a4-2d8f-e5cd-8fb8-974b7edc3557.htm language=enus -->
## TOPIC 00022: ninetrfpmfx40ref/html/6504a0a4-2d8f-e5cd-8fb8-974b7edc3557.htm

- bundle_id: `ni-rfpm-api-ref`
- source_path: `ninetrfpmfx40ref/html/6504a0a4-2d8f-e5cd-8fb8-974b7edc3557.htm`
- source_url: https://docs-be.ni.com/bundle/ni-rfpm-api-ref/raw/resource/enus/ninetrfpmfx40ref/html/6504a0a4-2d8f-e5cd-8fb8-974b7edc3557.htm
- document_id: `ni-rfpm-api-ref`
- page_type: `leaf`
- content_type: ``

RfpmMeasurements.FetchAllSParameters Method

RfpmMeasurementsFetchAllSParameters Method

##### Overload List

|  | Name | Description |
| --- | --- | --- |
|  | FetchAllSParameters(TimeSpan, RfpmMultipleMeasurementResultComplexDouble) | Fetches the RfpmMultipleMeasurementResultT which contains formatted S-parameter measurement results in a jagged array of complex double values, along with frequencies and port powers to enable plotting against either parameter as the X-axis. |
|  | FetchAllSParameters(DoubleMeasurementFormat, TimeSpan, RfpmMultipleMeasurementResultDouble) | Fetches the RfpmMultipleMeasurementResultT which contains formatted S-parameter measurement results in a jagged array of double values, along with frequencies and port powers to enable plotting against either parameter as the X-axis. |

Top

##### See Also

###### Reference

RfpmMeasurements Class

NationalInstruments.ModularInstruments.NIRfpm Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=ni-rfpm-api-ref path=ninetrfpmfx40ref/html/659169d7-abc1-44ea-3d41-cd6336f6d4e8.htm language=enus -->
## TOPIC 00023: ninetrfpmfx40ref/html/659169d7-abc1-44ea-3d41-cd6336f6d4e8.htm

- bundle_id: `ni-rfpm-api-ref`
- source_path: `ninetrfpmfx40ref/html/659169d7-abc1-44ea-3d41-cd6336f6d4e8.htm`
- source_url: https://docs-be.ni.com/bundle/ni-rfpm-api-ref/raw/resource/enus/ninetrfpmfx40ref/html/659169d7-abc1-44ea-3d41-cd6336f6d4e8.htm
- document_id: `ni-rfpm-api-ref`
- page_type: `leaf`
- content_type: ``

RfpmMeasurements.Deembedding Property

RfpmMeasurementsDeembedding Property

RfpmMeasurementsDeembedding

Namespace:

NationalInstruments.ModularInstruments.NIRfpm

Assembly:

##### Syntax

C#

VB

```text
public RfpmMeasurementsDeembedding Deembedding { get; }
```

```text
Public ReadOnly Property Deembedding As RfpmMeasurementsDeembedding
	Get
```

###### Property Value

RfpmMeasurementsDeembedding

##### Exceptions

| Exception | Condition |
| --- | --- |
| ObjectDisposedException | Deembedding was accessed after the associated NIRfpm object was disposed. |
| IviCDriverException | The underlying NI-RFPM driver returned an error. |

##### See Also

###### Reference

RfpmMeasurements Class

NationalInstruments.ModularInstruments.NIRfpm Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=ni-rfpm-api-ref path=ninetrfpmfx40ref/html/6fcc6368-c8c8-f9fe-e2d8-46dc4d51f56e.htm language=enus -->
## TOPIC 00024: ninetrfpmfx40ref/html/6fcc6368-c8c8-f9fe-e2d8-46dc4d51f56e.htm

- bundle_id: `ni-rfpm-api-ref`
- source_path: `ninetrfpmfx40ref/html/6fcc6368-c8c8-f9fe-e2d8-46dc4d51f56e.htm`
- source_url: https://docs-be.ni.com/bundle/ni-rfpm-api-ref/raw/resource/enus/ninetrfpmfx40ref/html/6fcc6368-c8c8-f9fe-e2d8-46dc4d51f56e.htm
- document_id: `ni-rfpm-api-ref`
- page_type: `leaf`
- content_type: ``

RfpmMeasurements Properties

RfpmMeasurements Properties

The [RfpmMeasurements](8b4fbc9c-2d99-2edc-ea64-de387b8c325d.htm) type exposes the following members.

##### Properties

|  | Name | Description |
| --- | --- | --- |
|  | Deembedding | Gets an RfpmMeasurementsDeembedding object that defines methods and properties enabling and configuring de-embedding. |
|  | ExternalSettlingTime | Gets or sets the amount of time to wait for external settling after tuning the source at each measurement point for each driving port. |
|  | IsInterpolationEnabled | Gets or sets a value indicating whether interpolation is used when fetching source and receiver offsets by parameters. This property does not support the mmWave subsystem. |
|  | IsReferenceLevelCoercionEnabled | Gets or sets a value indicating whether the reference level is coerced to the next highest reference level with a matching frequency when fetching a receiver offset by parameters. This property does not support the mmWave subsystem. |
|  | IsVectorCorrectionEnabled | Gets or sets a value indicating whether to apply the vector error coefficients to measurements. |
|  | MaximumFrequencySpanForInterpolation | Gets or sets the maximum span between two adjacent calibration frequencies for which interpolation will be performed, expressed in Hz. This property does not support the mmWave subsystem. |
|  | MaximumPowerLevelCoercion | Gets or sets the maximum power level coercion when fetching the source offset. This property does not support the mmWave subsystem. |
|  | MaximumReferenceLevelCoercion | Gets or sets the maximum difference allowed between the requested reference level and the matching reference level when IsReferenceLevelCoercionEnabled is set to , expressed in dBm. This property does not support the mmWave subsystem. |
|  | PowerLevelCoercion | Gets or sets the power level coercion when fetching the source offset. This property does not support the mmWave subsystem. |
|  | ReceiverAmplitudeSettlingAccuracy | Gets or sets the receiver amplitude settling accuracy for scalar measurements in decibels. This property does not support the mmWave subsystem. |
|  | ReferenceClockSource | Gets or sets the clock source to use for the reference clock. |
|  | ReferenceLevelPortExtension | Gets an RfpmMeasurementsReferenceLevelPortExtension object that defines methods and properties enabling and configuring reference level port extension. Supported devices: mmWave subsystem. |
|  | SourceAmplitudeSettlingAccuracy | Gets or sets the source amplitude settling accuracy for vector and scalar measurements in decibels. This property does not support the mmWave subsystem. |
|  | VectorReceiverAmplitudeSettlingAccuracy | Gets or sets the receiver amplitude settling accuracy for vector measurements in decibels. This property does not support the mmWave subsystem. |

Top

##### See Also

###### Reference

RfpmMeasurements Class

NationalInstruments.ModularInstruments.NIRfpm Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=ni-rfpm-api-ref path=ninetrfpmfx40ref/html/7207e343-b103-e408-2eb6-74255217d6ee.htm language=enus -->
## TOPIC 00025: ninetrfpmfx40ref/html/7207e343-b103-e408-2eb6-74255217d6ee.htm

- bundle_id: `ni-rfpm-api-ref`
- source_path: `ninetrfpmfx40ref/html/7207e343-b103-e408-2eb6-74255217d6ee.htm`
- source_url: https://docs-be.ni.com/bundle/ni-rfpm-api-ref/raw/resource/enus/ninetrfpmfx40ref/html/7207e343-b103-e408-2eb6-74255217d6ee.htm
- document_id: `ni-rfpm-api-ref`
- page_type: `leaf`
- content_type: ``

RfpmSweepSetting Methods

RfpmSweepSetting Methods

The [RfpmSweepSetting](3712842e-bdb4-0080-a1de-ee4e13f6064a.htm) type exposes the following members.

##### Methods

|  | Name | Description |
| --- | --- | --- |
|  | Equals | Determines whether the specified Object is equal to the current Object. (Inherited from Object.) |
|  | GetHashCode | Serves as a hash function for a particular type. (Inherited from Object.) |
|  | GetType | Gets the Type of the current instance. (Inherited from Object.) |
|  | ToString | Returns a string that represents the current object. (Inherited from Object.) |

Top

##### See Also

###### Reference

RfpmSweepSetting Class

NationalInstruments.ModularInstruments.NIRfpm Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=ni-rfpm-api-ref path=ninetrfpmfx40ref/html/72f934ae-4da3-b674-00f4-f40695c576e8.htm language=enus -->
## TOPIC 00026: ninetrfpmfx40ref/html/72f934ae-4da3-b674-00f4-f40695c576e8.htm

- bundle_id: `ni-rfpm-api-ref`
- source_path: `ninetrfpmfx40ref/html/72f934ae-4da3-b674-00f4-f40695c576e8.htm`
- source_url: https://docs-be.ni.com/bundle/ni-rfpm-api-ref/raw/resource/enus/ninetrfpmfx40ref/html/72f934ae-4da3-b674-00f4-f40695c576e8.htm
- document_id: `ni-rfpm-api-ref`
- page_type: `leaf`
- content_type: ``

CloseUserCalibrationAction Enumeration

CloseUserCalibrationAction Enumeration

Namespace:

NationalInstruments.ModularInstruments.NIRfpm

Assembly:

##### Syntax

C#

VB

```text
public enum CloseUserCalibrationAction
```

```text
Public Enumeration CloseUserCalibrationAction
```

##### Members

|  | Member name | Value | Description |
| --- | --- | --- | --- |
|  | Abort | 1 | Abort the calibration and discard the results. |
|  | Commit | 2 | Commit the calibration results. |

##### See Also

###### Reference

NationalInstruments.ModularInstruments.NIRfpm Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=ni-rfpm-api-ref path=ninetrfpmfx40ref/html/734d68a6-bc87-85d3-0786-4d412b904cca.htm language=enus -->
## TOPIC 00027: ninetrfpmfx40ref/html/734d68a6-bc87-85d3-0786-4d412b904cca.htm

- bundle_id: `ni-rfpm-api-ref`
- source_path: `ninetrfpmfx40ref/html/734d68a6-bc87-85d3-0786-4d412b904cca.htm`
- source_url: https://docs-be.ni.com/bundle/ni-rfpm-api-ref/raw/resource/enus/ninetrfpmfx40ref/html/734d68a6-bc87-85d3-0786-4d412b904cca.htm
- document_id: `ni-rfpm-api-ref`
- page_type: `leaf`
- content_type: ``

RfpmDriverIdentity Properties

RfpmDriverIdentity Properties

The [RfpmDriverIdentity](de632da7-defb-1fb7-3883-22379807234d.htm) type exposes the following members.

##### Properties

|  | Name | Description |
| --- | --- | --- |
|  | Identifier | Gets a string that contains an identifier for the NI-RFPM .NET API. |

Top

##### See Also

###### Reference

RfpmDriverIdentity Class

NationalInstruments.ModularInstruments.NIRfpm Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=ni-rfpm-api-ref path=ninetrfpmfx40ref/html/758e89b8-b1da-37d1-6448-776e57b08b7c.htm language=enus -->
## TOPIC 00028: ninetrfpmfx40ref/html/758e89b8-b1da-37d1-6448-776e57b08b7c.htm

- bundle_id: `ni-rfpm-api-ref`
- source_path: `ninetrfpmfx40ref/html/758e89b8-b1da-37d1-6448-776e57b08b7c.htm`
- source_url: https://docs-be.ni.com/bundle/ni-rfpm-api-ref/raw/resource/enus/ninetrfpmfx40ref/html/758e89b8-b1da-37d1-6448-776e57b08b7c.htm
- document_id: `ni-rfpm-api-ref`
- page_type: `leaf`
- content_type: ``

RfpmWarning.Equals Method (RfpmWarning)

RfpmWarningEquals Method (RfpmWarning)

RfpmWarning

RfpmWarning

Namespace:

NationalInstruments.ModularInstruments.NIRfpm

Assembly:

##### Syntax

C#

VB

```text
public bool Equals(
	RfpmWarning warning
)
```

```text
Public Function Equals ( 
	warning As RfpmWarning
) As Boolean
```

###### Parameters

- **warning**
  - Type: NationalInstruments.ModularInstruments.NIRfpmRfpmWarning The RfpmWarning object to be compared to the current instance of RfpmWarning.

###### Return Value

Boolean

##### See Also

###### Reference

RfpmWarning Class

Equals Overload

NationalInstruments.ModularInstruments.NIRfpm Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=ni-rfpm-api-ref path=ninetrfpmfx40ref/html/7736bfb1-b7a1-d18b-ff4f-c590ba92bce6.htm language=enus -->
## TOPIC 00029: ninetrfpmfx40ref/html/7736bfb1-b7a1-d18b-ff4f-c590ba92bce6.htm

- bundle_id: `ni-rfpm-api-ref`
- source_path: `ninetrfpmfx40ref/html/7736bfb1-b7a1-d18b-ff4f-c590ba92bce6.htm`
- source_url: https://docs-be.ni.com/bundle/ni-rfpm-api-ref/raw/resource/enus/ninetrfpmfx40ref/html/7736bfb1-b7a1-d18b-ff4f-c590ba92bce6.htm
- document_id: `ni-rfpm-api-ref`
- page_type: `leaf`
- content_type: ``

RfpmUserCalibrationSourceOffset Methods

RfpmUserCalibrationSourceOffset Methods

The [RfpmUserCalibrationSourceOffset](4f678621-3297-56a7-fe5a-c029a284edb0.htm) type exposes the following members.

##### Methods

|  | Name | Description |
| --- | --- | --- |
|  | Equals | Determines whether the specified Object is equal to the current Object. (Inherited from Object.) |
|  | Finalize | Allows an object to try to free resources and perform other cleanup operations before it is reclaimed by garbage collection. (Inherited from Object.) |
|  | GetHashCode | Serves as a hash function for a particular type. (Inherited from Object.) |
|  | GetType | Gets the Type of the current instance. (Inherited from Object.) |
|  | MemberwiseClone | Creates a shallow copy of the current Object. (Inherited from Object.) |
|  | ToString | Returns a string that represents the current object. (Inherited from Object.) |

Top

##### See Also

###### Reference

RfpmUserCalibrationSourceOffset Class

NationalInstruments.ModularInstruments.NIRfpm Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=ni-rfpm-api-ref path=ninetrfpmfx40ref/html/7dc1bba3-bb85-3c43-92d5-743ac004c9ac.htm language=enus -->
## TOPIC 00030: ninetrfpmfx40ref/html/7dc1bba3-bb85-3c43-92d5-743ac004c9ac.htm

- bundle_id: `ni-rfpm-api-ref`
- source_path: `ninetrfpmfx40ref/html/7dc1bba3-bb85-3c43-92d5-743ac004c9ac.htm`
- source_url: https://docs-be.ni.com/bundle/ni-rfpm-api-ref/raw/resource/enus/ninetrfpmfx40ref/html/7dc1bba3-bb85-3c43-92d5-743ac004c9ac.htm
- document_id: `ni-rfpm-api-ref`
- page_type: `leaf`
- content_type: ``

RfpmVectorUserCalibration.ReadInformation Method

RfpmVectorUserCalibrationReadInformation Method

RfpmUserCalibrationInformation

Namespace:

NationalInstruments.ModularInstruments.NIRfpm

Assembly:

##### Syntax

C#

VB

```text
public RfpmUserCalibrationInformation[] ReadInformation()
```

```text
Public Function ReadInformation As RfpmUserCalibrationInformation()
```

###### Return Value

RfpmUserCalibrationInformation

RfpmUserCalibrationInformation

##### Exceptions

| Exception | Condition |
| --- | --- |
| ObjectDisposedException | ReadInformation was called after the associated NIRfpm or RfpmDriverUtility object was disposed. |
| IviCDriverException | The underlying NI-RFPM driver returned an error. |

##### See Also

###### Reference

RfpmVectorUserCalibration Class

NationalInstruments.ModularInstruments.NIRfpm Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=ni-rfpm-api-ref path=ninetrfpmfx40ref/html/7f750b8b-4f3e-ae90-5346-7b2df9bdaa00.htm language=enus -->
## TOPIC 00031: ninetrfpmfx40ref/html/7f750b8b-4f3e-ae90-5346-7b2df9bdaa00.htm

- bundle_id: `ni-rfpm-api-ref`
- source_path: `ninetrfpmfx40ref/html/7f750b8b-4f3e-ae90-5346-7b2df9bdaa00.htm`
- source_url: https://docs-be.ni.com/bundle/ni-rfpm-api-ref/raw/resource/enus/ninetrfpmfx40ref/html/7f750b8b-4f3e-ae90-5346-7b2df9bdaa00.htm
- document_id: `ni-rfpm-api-ref`
- page_type: `leaf`
- content_type: ``

ReceiverType Enumeration

ReceiverType Enumeration

Specifies the receiver to fetch from.

Namespace:

NationalInstruments.ModularInstruments.NIRfpm

Assembly:

##### Syntax

C#

VB

```text
public enum ReceiverType
```

```text
Public Enumeration ReceiverType
```

##### Members

|  | Member name | Value | Description |
| --- | --- | --- | --- |
|  | Test | 1 | Test receiver. |
|  | Reference | 2 | Reference receiver. |

##### See Also

###### Reference

NationalInstruments.ModularInstruments.NIRfpm Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=ni-rfpm-api-ref path=ninetrfpmfx40ref/html/7fa163d3-3607-f1fa-ed18-7e3f2c6b285a.htm language=enus -->
## TOPIC 00032: ninetrfpmfx40ref/html/7fa163d3-3607-f1fa-ed18-7e3f2c6b285a.htm

- bundle_id: `ni-rfpm-api-ref`
- source_path: `ninetrfpmfx40ref/html/7fa163d3-3607-f1fa-ed18-7e3f2c6b285a.htm`
- source_url: https://docs-be.ni.com/bundle/ni-rfpm-api-ref/raw/resource/enus/ninetrfpmfx40ref/html/7fa163d3-3607-f1fa-ed18-7e3f2c6b285a.htm
- document_id: `ni-rfpm-api-ref`
- page_type: `leaf`
- content_type: ``

RfpmMeasurementsReferenceLevelPortExtension Methods

RfpmMeasurementsReferenceLevelPortExtension Methods

The [RfpmMeasurementsReferenceLevelPortExtension](6340ce53-f182-179b-ed0e-673a599867cf.htm) type exposes the following members.

##### Methods

|  | Name | Description |
| --- | --- | --- |
|  | CreateReferenceLevelPortExtensionTableFromS2PFile | Configures reference level port extension for a specified port by providing a S2P file of the network. Supported Devices: mmWave subsystem. |
|  | DeleteAllReferenceLevelPortExtensionTables | Deletes all reference level port extension tables for all ports. Supported Devices: mmWave subsystem. |
|  | DeleteReferenceLevelPortExtensionTable | Deletes reference level port extension table for a specified port. Supported Devices: mmWave subsystem. |
|  | Equals | Determines whether the specified Object is equal to the current Object. (Inherited from Object.) |
|  | GetHashCode | Serves as a hash function for a particular type. (Inherited from Object.) |
|  | GetPortExtensionSelectedTable | Gets the selected reference level port extension table for the given port. Supported Devices: mmWave subsystem. |
|  | GetType | Gets the Type of the current instance. (Inherited from Object.) |
|  | SetPortExtensionSelectedTable | Sets the reference level port extension table for the given port. Supported Devices: mmWave subsystem. |
|  | ToString | Returns a string that represents the current object. (Inherited from Object.) |

Top

##### See Also

###### Reference

RfpmMeasurementsReferenceLevelPortExtension Class

NationalInstruments.ModularInstruments.NIRfpm Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=ni-rfpm-api-ref path=ninetrfpmfx40ref/html/7ff0ab50-0a18-6bc6-6973-5f806ddfb01c.htm language=enus -->
## TOPIC 00033: ninetrfpmfx40ref/html/7ff0ab50-0a18-6bc6-6973-5f806ddfb01c.htm

- bundle_id: `ni-rfpm-api-ref`
- source_path: `ninetrfpmfx40ref/html/7ff0ab50-0a18-6bc6-6973-5f806ddfb01c.htm`
- source_url: https://docs-be.ni.com/bundle/ni-rfpm-api-ref/raw/resource/enus/ninetrfpmfx40ref/html/7ff0ab50-0a18-6bc6-6973-5f806ddfb01c.htm
- document_id: `ni-rfpm-api-ref`
- page_type: `leaf`
- content_type: ``

RfpmSourceCalibration.GetMaxPowerLevel Method

RfpmSourceCalibrationGetMaxPowerLevel Method

Namespace:

NationalInstruments.ModularInstruments.NIRfpm

Assembly:

##### Syntax

C#

VB

```text
public double GetMaxPowerLevel(
	string port,
	SourcePath sourcePath,
	double frequency,
	PowerLevelType powerLevelType,
	double papr,
	double runtimeScaling,
	OptimizationMethod optimizationMethod
)
```

```text
Public Function GetMaxPowerLevel ( 
	port As String,
	sourcePath As SourcePath,
	frequency As Double,
	powerLevelType As PowerLevelType,
	papr As Double,
	runtimeScaling As Double,
	optimizationMethod As OptimizationMethod
) As Double
```

###### Parameters

- **port**
  - Type: SystemStringThe port to get the maximum source power for.
- **sourcePath**
  - Type: NationalInstruments.ModularInstruments.NIRfpmSourcePathThe source path setting to et the maximum source power for.
- **frequency**
  - Type: SystemDoubleThe frequency to et the maximum source power for.
- **powerLevelType**
  - Type: NationalInstruments.ModularInstruments.NIRfpmPowerLevelTypeThe object that determines if returned value represents average envelope power or peak envelope power.
- **papr**
  - Type: SystemDoubleThe peak to average envelope power ratio of the waveform to be generated in dB.
- **runtimeScaling**
  - Type: SystemDoubleThe runtime scaling (sometimes called pre-filter gain) that will be used with the waveform that will be generated. This is in dB.
- **optimizationMethod**
  - Type: NationalInstruments.ModularInstruments.NIRfpmOptimizationMethodThe approach to use to optimize the path through NIRfpm. This parameter only applies if sourcePath is set to Unspecified.

###### Return Value

Double

##### Exceptions

| Exception | Condition |
| --- | --- |
| ObjectDisposedException | GetMaxPowerLevel(String, SourcePath, Double, PowerLevelType, Double, Double, OptimizationMethod) was called after the associated NIRfpm or RfpmDriverUtility object was disposed. |
| ArgumentNullException | The value for port is . |
| ArgumentException | The value for sourcePath is invalid. - or - The value for frequency is invalid. - or - The value for powerLevelType is invalid. - or - The value for optimizationMethod is invalid. |
| SelectorNameException | The value for port is Empty. - or - The value for port is unknown or invalid. |
| IviCDriverException | Calibration correction was not available. No source offset was found for the specified port and frequency. - or - The value for papr is invalid. - or - The value for runtimeScaling is invalid. - or - The underlying NI-RFPM driver returned an error. |

##### See Also

###### Reference

RfpmSourceCalibration Class

NationalInstruments.ModularInstruments.NIRfpm Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=ni-rfpm-api-ref path=ninetrfpmfx40ref/html/931a4a9e-7389-d071-08aa-2450c253bca5.htm language=enus -->
## TOPIC 00034: ninetrfpmfx40ref/html/931a4a9e-7389-d071-08aa-2450c253bca5.htm

- bundle_id: `ni-rfpm-api-ref`
- source_path: `ninetrfpmfx40ref/html/931a4a9e-7389-d071-08aa-2450c253bca5.htm`
- source_url: https://docs-be.ni.com/bundle/ni-rfpm-api-ref/raw/resource/enus/ninetrfpmfx40ref/html/931a4a9e-7389-d071-08aa-2450c253bca5.htm
- document_id: `ni-rfpm-api-ref`
- page_type: `leaf`
- content_type: ``

RfpmUserCalibration.Vector Property

RfpmUserCalibrationVector Property

RfpmVectorUserCalibration

Namespace:

NationalInstruments.ModularInstruments.NIRfpm

Assembly:

##### Syntax

C#

VB

```text
public RfpmVectorUserCalibration Vector { get; }
```

```text
Public ReadOnly Property Vector As RfpmVectorUserCalibration
	Get
```

###### Property Value

RfpmVectorUserCalibration

RfpmVectorUserCalibration

##### Exceptions

| Exception | Condition |
| --- | --- |
| ObjectDisposedException | Vector was accessed after the associated NIRfpm object was disposed. |

##### See Also

###### Reference

RfpmUserCalibration Class

NationalInstruments.ModularInstruments.NIRfpm Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=ni-rfpm-api-ref path=ninetrfpmfx40ref/html/9322b35b-b93d-86e4-a0d1-6f75c746901b.htm language=enus -->
## TOPIC 00035: ninetrfpmfx40ref/html/9322b35b-b93d-86e4-a0d1-6f75c746901b.htm

- bundle_id: `ni-rfpm-api-ref`
- source_path: `ninetrfpmfx40ref/html/9322b35b-b93d-86e4-a0d1-6f75c746901b.htm`
- source_url: https://docs-be.ni.com/bundle/ni-rfpm-api-ref/raw/resource/enus/ninetrfpmfx40ref/html/9322b35b-b93d-86e4-a0d1-6f75c746901b.htm
- document_id: `ni-rfpm-api-ref`
- page_type: `leaf`
- content_type: ``

RfpmWarning Operators

RfpmWarning Operators

The [RfpmWarning](4778c847-b9a6-6fe1-6939-c896ecf54d3e.htm) type exposes the following members.

##### Operators

|  | Name | Description |
| --- | --- | --- |
|  | Equality | Checks whether the two instances of RfpmWarning are equal. |
|  | Inequality | Checks whether the two instances of RfpmWarning are unequal. |

Top

##### See Also

###### Reference

RfpmWarning Class

NationalInstruments.ModularInstruments.NIRfpm Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=ni-rfpm-api-ref path=ninetrfpmfx40ref/html/932de486-7be0-1da2-afb6-6807fb0f8f21.htm language=enus -->
## TOPIC 00036: ninetrfpmfx40ref/html/932de486-7be0-1da2-afb6-6807fb0f8f21.htm

- bundle_id: `ni-rfpm-api-ref`
- source_path: `ninetrfpmfx40ref/html/932de486-7be0-1da2-afb6-6807fb0f8f21.htm`
- source_url: https://docs-be.ni.com/bundle/ni-rfpm-api-ref/raw/resource/enus/ninetrfpmfx40ref/html/932de486-7be0-1da2-afb6-6807fb0f8f21.htm
- document_id: `ni-rfpm-api-ref`
- page_type: `leaf`
- content_type: ``

RfpmMeasurements.Initiate Method (String[], String)

RfpmMeasurementsInitiate Method (String, String)

Initiates a measurement on the specified ports, using the specified sweep setting defined in the sweep settings file.

Namespace:

NationalInstruments.ModularInstruments.NIRfpm

Assembly:

##### Syntax

C#

VB

```text
public void Initiate(
	string[] ports,
	string sweepSettingName
)
```

```text
Public Sub Initiate ( 
	ports As String(),
	sweepSettingName As String
)
```

###### Parameters

- **ports**
  - Type: SystemString An array of ports to be measured.
- **sweepSettingName**
  - Type: SystemString The name of the sweep in the sweep settings file.

##### Exceptions

| Exception | Condition |
| --- | --- |
| ObjectDisposedException | Initiate(String, String) was called after the associated NIRfpm or RfpmDriverUtility object was disposed. |
| ArgumentNullException | The value for ports is . - or - The value for sweepSettingName is . |
| ArgumentException | The value for sweepSettingName is invalid. - or - The value for sweepSettingName is unknown. - or - The value for sweepSettingName is Empty. |
| InvalidOperationException | Initiate was called before performing calibration. |
| SelectorNameException | The value for a port from ports is invalid. - or - The value for a port from ports is unknown. |
| IviCDriverException | The value for a port from ports is . - or - The value for a port from ports is Empty. - or - The value for ports is an empty array. - or - The underlying NI-RFPM driver returned an error. |

##### Remarks

Initiate(String, String)

Perform the initiate with one of the sweep setting names from
 [GetSweepSettings](b4c6d59d-0c1e-650d-cffe-9d5c45ffb82c.htm).

##### See Also

###### Reference

RfpmMeasurements Class

Initiate Overload

NationalInstruments.ModularInstruments.NIRfpm Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=ni-rfpm-api-ref path=ninetrfpmfx40ref/html/951b85f5-99f8-a967-a1ae-417c2c777510.htm language=enus -->
## TOPIC 00037: ninetrfpmfx40ref/html/951b85f5-99f8-a967-a1ae-417c2c777510.htm

- bundle_id: `ni-rfpm-api-ref`
- source_path: `ninetrfpmfx40ref/html/951b85f5-99f8-a967-a1ae-417c2c777510.htm`
- source_url: https://docs-be.ni.com/bundle/ni-rfpm-api-ref/raw/resource/enus/ninetrfpmfx40ref/html/951b85f5-99f8-a967-a1ae-417c2c777510.htm
- document_id: `ni-rfpm-api-ref`
- page_type: `leaf`
- content_type: ``

RfpmSourceCalibration Methods

RfpmSourceCalibration Methods

The [RfpmSourceCalibration](f583f002-3ffd-9b52-d636-7598a7dabb07.htm) type exposes the following members.

##### Methods

|  | Name | Description |
| --- | --- | --- |
|  | Equals | Determines whether the specified Object is equal to the current Object. (Inherited from Object.) |
|  | FetchOffset | Fetches the stored source offset, calibrated power, digital gain, and settling time for a single switch path, frequency, and power setting given a specified port. This property does not support the mmWave subsystem. |
|  | GetHashCode | Serves as a hash function for a particular type. (Inherited from Object.) |
|  | GetMaxPowerLevel | Get the maximum source power for a single switch path, and frequency, given a specified port. This property does not support the mmWave subsystem. |
|  | GetType | Gets the Type of the current instance. (Inherited from Object.) |
|  | ToString | Returns a string that represents the current object. (Inherited from Object.) |

Top

##### See Also

###### Reference

RfpmSourceCalibration Class

NationalInstruments.ModularInstruments.NIRfpm Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=ni-rfpm-api-ref path=ninetrfpmfx40ref/html/95783a13-3765-5ae4-04ca-ef5bf68e252c.htm language=enus -->
## TOPIC 00038: ninetrfpmfx40ref/html/95783a13-3765-5ae4-04ca-ef5bf68e252c.htm

- bundle_id: `ni-rfpm-api-ref`
- source_path: `ninetrfpmfx40ref/html/95783a13-3765-5ae4-04ca-ef5bf68e252c.htm`
- source_url: https://docs-be.ni.com/bundle/ni-rfpm-api-ref/raw/resource/enus/ninetrfpmfx40ref/html/95783a13-3765-5ae4-04ca-ef5bf68e252c.htm
- document_id: `ni-rfpm-api-ref`
- page_type: `leaf`
- content_type: ``

RfpmMultipleMeasurementResult(T) Properties

RfpmMultipleMeasurementResultT Properties

The [RfpmMultipleMeasurementResultT](2e1b6707-1431-532f-23c4-d52f5ae28cc0.htm) generic type exposes the following members.

##### Properties

|  | Name | Description |
| --- | --- | --- |
|  | FrequencyData | Gets the measurement frequencies of all S-parameter fetch operations. |
|  | MeasurementData | Gets the measurement data of all S-parameter fetch operations. |
|  | PortPowerData | Gets the stimulus port powers of all S-parameters fetch operations. |

Top

##### See Also

###### Reference

NationalInstruments.ModularInstruments.NIRfpm Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=ni-rfpm-api-ref path=ninetrfpmfx40ref/html/9c06cbfa-0b0d-634e-9eb9-fc40d2624e67.htm language=enus -->
## TOPIC 00039: ninetrfpmfx40ref/html/9c06cbfa-0b0d-634e-9eb9-fc40d2624e67.htm

- bundle_id: `ni-rfpm-api-ref`
- source_path: `ninetrfpmfx40ref/html/9c06cbfa-0b0d-634e-9eb9-fc40d2624e67.htm`
- source_url: https://docs-be.ni.com/bundle/ni-rfpm-api-ref/raw/resource/enus/ninetrfpmfx40ref/html/9c06cbfa-0b0d-634e-9eb9-fc40d2624e67.htm
- document_id: `ni-rfpm-api-ref`
- page_type: `leaf`
- content_type: ``

RfpmWarningEventArgs Methods

RfpmWarningEventArgs Methods

The [RfpmWarningEventArgs](f7300045-ba65-d7cc-4417-5271063dc32b.htm) type exposes the following members.

##### Methods

|  | Name | Description |
| --- | --- | --- |
|  | Equals | Determines whether the specified Object is equal to the current Object. (Inherited from Object.) |
|  | GetHashCode | Serves as a hash function for a particular type. (Inherited from Object.) |
|  | GetType | Gets the Type of the current instance. (Inherited from Object.) |
|  | ToString | Returns a string that represents the current object. (Inherited from Object.) |

Top

##### See Also

###### Reference

RfpmWarningEventArgs Class

NationalInstruments.ModularInstruments.NIRfpm Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=ni-rfpm-api-ref path=ninetrfpmfx40ref/html/9cfe7e25-91c9-2c94-6664-455f4b24cf37.htm language=enus -->
## TOPIC 00040: ninetrfpmfx40ref/html/9cfe7e25-91c9-2c94-6664-455f4b24cf37.htm

- bundle_id: `ni-rfpm-api-ref`
- source_path: `ninetrfpmfx40ref/html/9cfe7e25-91c9-2c94-6664-455f4b24cf37.htm`
- source_url: https://docs-be.ni.com/bundle/ni-rfpm-api-ref/raw/resource/enus/ninetrfpmfx40ref/html/9cfe7e25-91c9-2c94-6664-455f4b24cf37.htm
- document_id: `ni-rfpm-api-ref`
- page_type: `leaf`
- content_type: ``

RfpmMeasurements.ReferenceClockSource Property

RfpmMeasurementsReferenceClockSource Property

Gets or sets the clock source to use for the reference clock.

Namespace:

NationalInstruments.ModularInstruments.NIRfpm

Assembly:

##### Syntax

C#

VB

```text
public ReferenceClockSource ReferenceClockSource { get; set; }
```

```text
Public Property ReferenceClockSource As ReferenceClockSource
	Get
	Set
```

###### Property Value

ReferenceClockSource

Onboard

##### Exceptions

| Exception | Condition |
| --- | --- |
| ObjectDisposedException | ReferenceClockSource was accessed after the associated NIRfpm or RfpmDriverUtility object was disposed. |
| ArgumentException | The value set was invalid. |
| IviCDriverException | The underlying NI-RFPM driver returned an error. |

##### See Also

###### Reference

RfpmMeasurements Class

NationalInstruments.ModularInstruments.NIRfpm Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=ni-rfpm-api-ref path=ninetrfpmfx40ref/html/9d5d227d-1eea-a021-3797-85da3e255575.htm language=enus -->
## TOPIC 00041: ninetrfpmfx40ref/html/9d5d227d-1eea-a021-3797-85da3e255575.htm

- bundle_id: `ni-rfpm-api-ref`
- source_path: `ninetrfpmfx40ref/html/9d5d227d-1eea-a021-3797-85da3e255575.htm`
- source_url: https://docs-be.ni.com/bundle/ni-rfpm-api-ref/raw/resource/enus/ninetrfpmfx40ref/html/9d5d227d-1eea-a021-3797-85da3e255575.htm
- document_id: `ni-rfpm-api-ref`
- page_type: `leaf`
- content_type: ``

RfpmVectorUserCalibration Properties

RfpmVectorUserCalibration Properties

The [RfpmVectorUserCalibration](833a7acd-0c71-ae06-9053-d7bf942354f6.htm) type exposes the following members.

##### Properties

|  | Name | Description |
| --- | --- | --- |
|  | IsAbsoluteCalibrationEnabled | Gets or sets a value indicating whether to collect absolute vector error coefficients or relative vector offsets when performing autocalibration. This property does not support the mmWave subsystem. |

Top

##### See Also

###### Reference

RfpmVectorUserCalibration Class

NationalInstruments.ModularInstruments.NIRfpm Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=ni-rfpm-api-ref path=ninetrfpmfx40ref/html/9ebadd31-f606-937e-c6fd-8bf1cc786220.htm language=enus -->
## TOPIC 00042: ninetrfpmfx40ref/html/9ebadd31-f606-937e-c6fd-8bf1cc786220.htm

- bundle_id: `ni-rfpm-api-ref`
- source_path: `ninetrfpmfx40ref/html/9ebadd31-f606-937e-c6fd-8bf1cc786220.htm`
- source_url: https://docs-be.ni.com/bundle/ni-rfpm-api-ref/raw/resource/enus/ninetrfpmfx40ref/html/9ebadd31-f606-937e-c6fd-8bf1cc786220.htm
- document_id: `ni-rfpm-api-ref`
- page_type: `leaf`
- content_type: ``

RfpmUtilityForSwitch Methods

RfpmUtilityForSwitch Methods

The [RfpmUtilityForSwitch](5e7eb211-e29f-d8d3-38f2-4dc1d5e02029.htm) type exposes the following members.

##### Methods

|  | Name | Description |
| --- | --- | --- |
|  | DisconnectAll | Disconnects all existing paths. This method does not support the mmWave subsystem. |
|  | Equals | Determines whether the specified Object is equal to the current Object. (Inherited from Object.) |
|  | GetHashCode | Serves as a hash function for a particular type. (Inherited from Object.) |
|  | GetType | Gets the Type of the current instance. (Inherited from Object.) |
|  | ToString | Returns a string that represents the current object. (Inherited from Object.) |

Top

##### See Also

###### Reference

RfpmUtilityForSwitch Class

NationalInstruments.ModularInstruments.NIRfpm Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=ni-rfpm-api-ref path=ninetrfpmfx40ref/html/9ef5c013-0384-ca3e-b595-4e7f375f1b3d.htm language=enus -->
## TOPIC 00043: ninetrfpmfx40ref/html/9ef5c013-0384-ca3e-b595-4e7f375f1b3d.htm

- bundle_id: `ni-rfpm-api-ref`
- source_path: `ninetrfpmfx40ref/html/9ef5c013-0384-ca3e-b595-4e7f375f1b3d.htm`
- source_url: https://docs-be.ni.com/bundle/ni-rfpm-api-ref/raw/resource/enus/ninetrfpmfx40ref/html/9ef5c013-0384-ca3e-b595-4e7f375f1b3d.htm
- document_id: `ni-rfpm-api-ref`
- page_type: `leaf`
- content_type: ``

RfpmUserCalibrationSourceOffset Properties

RfpmUserCalibrationSourceOffset Properties

The [RfpmUserCalibrationSourceOffset](4f678621-3297-56a7-fe5a-c029a284edb0.htm) type exposes the following members.

##### Properties

|  | Name | Description |
| --- | --- | --- |
|  | CalibratedPower | Gets the calibrated power. This property does not support the mmWave subsystem. |
|  | DigitalGain | Gets the digital gain. This property does not support the mmWave subsystem. |
|  | Offset | Gets the source offset. This property does not support the mmWave subsystem. |
|  | SettlingTime | Gets the settling time. This property does not support the mmWave subsystem. |
|  | SwitchPath | Gets the path to the switch that the offset applies to. This property does not support the mmWave subsystem. |

Top

##### See Also

###### Reference

RfpmUserCalibrationSourceOffset Class

NationalInstruments.ModularInstruments.NIRfpm Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=ni-rfpm-api-ref path=ninetrfpmfx40ref/html/b88ad7ef-fcbf-f8b8-ffd0-26775c9c5db0.htm language=enus -->
## TOPIC 00044: ninetrfpmfx40ref/html/b88ad7ef-fcbf-f8b8-ffd0-26775c9c5db0.htm

- bundle_id: `ni-rfpm-api-ref`
- source_path: `ninetrfpmfx40ref/html/b88ad7ef-fcbf-f8b8-ffd0-26775c9c5db0.htm`
- source_url: https://docs-be.ni.com/bundle/ni-rfpm-api-ref/raw/resource/enus/ninetrfpmfx40ref/html/b88ad7ef-fcbf-f8b8-ffd0-26775c9c5db0.htm
- document_id: `ni-rfpm-api-ref`
- page_type: `leaf`
- content_type: ``

RfpmSweepSettingsManager Class

RfpmSweepSettingsManager Class

Defines methods for loading and obtaining sweep settings.

##### Inheritance Hierarchy

Namespace:

NationalInstruments.ModularInstruments.NIRfpm

Assembly:

##### Syntax

C#

VB

```text
public sealed class RfpmSweepSettingsManager : RfpmSubObject
```

```text
Public NotInheritable Class RfpmSweepSettingsManager
	Inherits RfpmSubObject
```

The RfpmSweepSettingsManager type exposes the following members.

##### Methods

|  | Name | Description |
| --- | --- | --- |
|  | Equals | Determines whether the specified Object is equal to the current Object. (Inherited from Object.) |
|  | GetHashCode | Serves as a hash function for a particular type. (Inherited from Object.) |
|  | GetSweepSetting | Gets a sweep setting by name. |
|  | GetSweepSettings | Gets all sweep settings currently loaded. |
|  | GetType | Gets the Type of the current instance. (Inherited from Object.) |
|  | LoadFromFile | Loads a sweep settings file into memory so that measurements are performed according to the sweeps defined in the file. |
|  | ToString | Returns a string that represents the current object. (Inherited from Object.) |

Top

##### Remarks

This class cannot be instantiated directly. It is instantiated when an [NIRfpm](07611137-d50f-4198-6321-da5299f2e31a.htm) session is created.
 Access this class using [SweepSettingsManager](13c515b9-f203-8956-bcc0-75721301f3ca.htm).

##### Thread Safety

static

Shared

##### See Also

###### Reference

NationalInstruments.ModularInstruments.NIRfpm Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=ni-rfpm-api-ref path=ninetrfpmfx40ref/html/b8cebb77-0432-f067-9560-43e1b6f1aca7.htm language=enus -->
## TOPIC 00045: ninetrfpmfx40ref/html/b8cebb77-0432-f067-9560-43e1b6f1aca7.htm

- bundle_id: `ni-rfpm-api-ref`
- source_path: `ninetrfpmfx40ref/html/b8cebb77-0432-f067-9560-43e1b6f1aca7.htm`
- source_url: https://docs-be.ni.com/bundle/ni-rfpm-api-ref/raw/resource/enus/ninetrfpmfx40ref/html/b8cebb77-0432-f067-9560-43e1b6f1aca7.htm
- document_id: `ni-rfpm-api-ref`
- page_type: `leaf`
- content_type: ``

RfpmDriverOperation Class

RfpmDriverOperation Class

Provides properties and methods that control the operation of the NI-RFPM driver.

##### Inheritance Hierarchy

Namespace:

NationalInstruments.ModularInstruments.NIRfpm

Assembly:

##### Syntax

C#

VB

```text
public sealed class RfpmDriverOperation : RfpmSubObject, 
	IIviDriverOperation
```

```text
Public NotInheritable Class RfpmDriverOperation
	Inherits RfpmSubObject
	Implements IIviDriverOperation
```

The RfpmDriverOperation type exposes the following members.

##### Methods

|  | Name | Description |
| --- | --- | --- |
|  | Equals | Determines whether the specified Object is equal to the current Object. (Inherited from Object.) |
|  | GetHashCode | Serves as a hash function for a particular type. (Inherited from Object.) |
|  | GetType | Gets the Type of the current instance. (Inherited from Object.) |
|  | InvalidateAllAttributes | Sets all cached property values to invalid. |
|  | ToString | Returns a string that represents the current object. (Inherited from Object.) |

Top

##### Events

|  | Name | Description |
| --- | --- | --- |
|  | Warning | Occurs when the driver creates a driver warning. |

Top

##### Remarks

This class cannot be instantiated directly. It is instantiated when an [NIRfpm](07611137-d50f-4198-6321-da5299f2e31a.htm) session is created.
 Access this class using [DriverOperation](ececa8fd-0c67-a8c6-14b1-d8d1b9be8888.htm).

##### Thread Safety

static

Shared

##### See Also

###### Reference

NationalInstruments.ModularInstruments.NIRfpm Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=ni-rfpm-api-ref path=ninetrfpmfx40ref/html/c4c2bdfd-4c2e-5ae8-a7e2-c9186e77075f.htm language=enus -->
## TOPIC 00046: ninetrfpmfx40ref/html/c4c2bdfd-4c2e-5ae8-a7e2-c9186e77075f.htm

- bundle_id: `ni-rfpm-api-ref`
- source_path: `ninetrfpmfx40ref/html/c4c2bdfd-4c2e-5ae8-a7e2-c9186e77075f.htm`
- source_url: https://docs-be.ni.com/bundle/ni-rfpm-api-ref/raw/resource/enus/ninetrfpmfx40ref/html/c4c2bdfd-4c2e-5ae8-a7e2-c9186e77075f.htm
- document_id: `ni-rfpm-api-ref`
- page_type: `leaf`
- content_type: ``

RfpmWarning.Equals Method (RfpmWarning, Boolean)

RfpmWarningEquals Method (RfpmWarning, Boolean)

RfpmWarning

Namespace:

NationalInstruments.ModularInstruments.NIRfpm

Assembly:

##### Syntax

C#

VB

```text
public bool Equals(
	RfpmWarning warning,
	bool ignoreWarningMessage
)
```

```text
Public Function Equals ( 
	warning As RfpmWarning,
	ignoreWarningMessage As Boolean
) As Boolean
```

###### Parameters

- **warning**
  - Type: NationalInstruments.ModularInstruments.NIRfpmRfpmWarning The RfpmWarning object to which this object is compared.
- **ignoreWarningMessage**
  - Type: SystemBoolean A value indicating whether the warning message is ignored. If the warning message is to be ignored, then the value of ignoreWarningMessage is . If the warning message is to be compared, then the value of ignoreWarningMessage is .

###### Return Value

Boolean

##### See Also

###### Reference

RfpmWarning Class

Equals Overload

NationalInstruments.ModularInstruments.NIRfpm Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=ni-rfpm-api-ref path=ninetrfpmfx40ref/html/d51fde9d-8f85-aed2-5986-6377090f88c7.htm language=enus -->
## TOPIC 00047: ninetrfpmfx40ref/html/d51fde9d-8f85-aed2-5986-6377090f88c7.htm

- bundle_id: `ni-rfpm-api-ref`
- source_path: `ninetrfpmfx40ref/html/d51fde9d-8f85-aed2-5986-6377090f88c7.htm`
- source_url: https://docs-be.ni.com/bundle/ni-rfpm-api-ref/raw/resource/enus/ninetrfpmfx40ref/html/d51fde9d-8f85-aed2-5986-6377090f88c7.htm
- document_id: `ni-rfpm-api-ref`
- page_type: `leaf`
- content_type: ``

RfpmMeasurementsDeembedding.GetS2POrientation Method

RfpmMeasurementsDeembeddingGetS2POrientation Method

Gets the de-embedding network orientation.

Namespace:

NationalInstruments.ModularInstruments.NIRfpm

Assembly:

##### Syntax

C#

VB

```text
public DeembeddingS2POrientation GetS2POrientation(
	string portName
)
```

```text
Public Function GetS2POrientation ( 
	portName As String
) As DeembeddingS2POrientation
```

###### Parameters

- **portName**
  - Type: SystemString The name of the port.

###### Return Value

DeembeddingS2POrientation

##### Exceptions

| Exception | Condition |
| --- | --- |
| ObjectDisposedException | GetS2PFilePath(String) was called after the associated NIRfpm or RfpmDriverUtility object was disposed. |
| SelectorNameException | The value for portName is . -or- The value for portName is an empty string. -or- The value for portName is invalid. -or- The value for portName is unknown. |
| IviCDriverException | The underlying NI-RFPM driver returned an error. |

##### Remarks

The orientation specifies whether the de-embedding network in the S2P file is connected with port 1 towards the DUT or port 2 towards the DUT.

##### See Also

###### Reference

RfpmMeasurementsDeembedding Class

NationalInstruments.ModularInstruments.NIRfpm Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=ni-rfpm-api-ref path=ninetrfpmfx40ref/html/d6d70a2f-8547-20db-6f53-759d01f3e9df.htm language=enus -->
## TOPIC 00048: ninetrfpmfx40ref/html/d6d70a2f-8547-20db-6f53-759d01f3e9df.htm

- bundle_id: `ni-rfpm-api-ref`
- source_path: `ninetrfpmfx40ref/html/d6d70a2f-8547-20db-6f53-759d01f3e9df.htm`
- source_url: https://docs-be.ni.com/bundle/ni-rfpm-api-ref/raw/resource/enus/ninetrfpmfx40ref/html/d6d70a2f-8547-20db-6f53-759d01f3e9df.htm
- document_id: `ni-rfpm-api-ref`
- page_type: `leaf`
- content_type: ``

RfpmWarning.ToString Method

RfpmWarningToString Method

RfpmWarning

Namespace:

NationalInstruments.ModularInstruments.NIRfpm

Assembly:

##### Syntax

C#

VB

```text
public override string ToString()
```

```text
Public Overrides Function ToString As String
```

###### Return Value

String

RfpmWarning

##### See Also

###### Reference

RfpmWarning Class

NationalInstruments.ModularInstruments.NIRfpm Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=ni-rfpm-api-ref path=ninetrfpmfx40ref/html/d8bd4d59-dd70-2178-3073-0375311faf2a.htm language=enus -->
## TOPIC 00049: ninetrfpmfx40ref/html/d8bd4d59-dd70-2178-3073-0375311faf2a.htm

- bundle_id: `ni-rfpm-api-ref`
- source_path: `ninetrfpmfx40ref/html/d8bd4d59-dd70-2178-3073-0375311faf2a.htm`
- source_url: https://docs-be.ni.com/bundle/ni-rfpm-api-ref/raw/resource/enus/ninetrfpmfx40ref/html/d8bd4d59-dd70-2178-3073-0375311faf2a.htm
- document_id: `ni-rfpm-api-ref`
- page_type: `leaf`
- content_type: ``

RfpmRfmxCallbacks.GetInfo Method

RfpmRfmxCallbacksGetInfo Method

Namespace:

NationalInstruments.ModularInstruments.NIRfpm

Assembly:

##### Syntax

C#

VB

```text
public void GetInfo(
	out IntPtr rfpmSubsystemContext,
	out IntPtr[] rfpmCallbacks,
	out int rfpmCallbacksVersion
)
```

```text
Public Sub GetInfo ( 
	<OutAttribute> ByRef rfpmSubsystemContext As IntPtr,
	<OutAttribute> ByRef rfpmCallbacks As IntPtr(),
	<OutAttribute> ByRef rfpmCallbacksVersion As Integer
)
```

###### Parameters

- **rfpmSubsystemContext**
  - Type: SystemIntPtrReturns the NI-RFPM subsystem context.
- **rfpmCallbacks**
  - Type: SystemIntPtrReturns an array of pointers to NI-RFPM callbacks for NI-RFmx.
- **rfpmCallbacksVersion**
  - Type: SystemInt32Returns the version of the callbacks.

##### Exceptions

| Exception | Condition |
| --- | --- |
| ObjectDisposedException | GetInfo(IntPtr, IntPtr, Int32) was called after the associated NIRfpm or RfpmDriverUtility object was disposed. |

##### Remarks

Once the context and the callbacks are obtained from NI-RFPM, call
 public int RegisterExternalRFSubsystemCallbacks(IntPtr externalRFSubsystemContext, IntPtr[] callbacks, int callbackVersion);
 to register NI-RFPM callbacks within NI-RFmx session.

##### See Also

###### Reference

RfpmRfmxCallbacks Class

NationalInstruments.ModularInstruments.NIRfpm Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=ni-rfpm-api-ref path=ninetrfpmfx40ref/html/d9028d56-2813-1ddc-9aac-03766cede924.htm language=enus -->
## TOPIC 00050: ninetrfpmfx40ref/html/d9028d56-2813-1ddc-9aac-03766cede924.htm

- bundle_id: `ni-rfpm-api-ref`
- source_path: `ninetrfpmfx40ref/html/d9028d56-2813-1ddc-9aac-03766cede924.htm`
- source_url: https://docs-be.ni.com/bundle/ni-rfpm-api-ref/raw/resource/enus/ninetrfpmfx40ref/html/d9028d56-2813-1ddc-9aac-03766cede924.htm
- document_id: `ni-rfpm-api-ref`
- page_type: `leaf`
- content_type: ``

RfpmMultipleMeasurementResult(T).PortPowerData Property

RfpmMultipleMeasurementResultTPortPowerData Property

Gets the stimulus port powers of all S-parameters fetch operations.

Namespace:

NationalInstruments.ModularInstruments.NIRfpm

Assembly:

##### Syntax

C#

VB

```text
public double[][] PortPowerData { get; }
```

```text
Public ReadOnly Property PortPowerData As Double()()
	Get
```

###### Property Value

Double

##### Remarks

The stimulus port powers are measured in dBm for each port per measurement point.
 This is a flattened 2D array of number of ports (n) by the number of elements in the FrequencyData array for a n port measurement.
 The returned port powers correspond to the powers specified in the sweep setting.

##### See Also

###### Reference

NationalInstruments.ModularInstruments.NIRfpm Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=ni-rfpm-api-ref path=ninetrfpmfx40ref/html/de4f42f7-e5ad-add5-73d2-7f0fa39eef54.htm language=enus -->
## TOPIC 00051: ninetrfpmfx40ref/html/de4f42f7-e5ad-add5-73d2-7f0fa39eef54.htm

- bundle_id: `ni-rfpm-api-ref`
- source_path: `ninetrfpmfx40ref/html/de4f42f7-e5ad-add5-73d2-7f0fa39eef54.htm`
- source_url: https://docs-be.ni.com/bundle/ni-rfpm-api-ref/raw/resource/enus/ninetrfpmfx40ref/html/de4f42f7-e5ad-add5-73d2-7f0fa39eef54.htm
- document_id: `ni-rfpm-api-ref`
- page_type: `leaf`
- content_type: ``

RfpmUtilityForSwitchReceiver.SetPath Method

RfpmUtilityForSwitchReceiverSetPath Method

##### Overload List

|  | Name | Description |
| --- | --- | --- |
|  | SetPath(RfpmSwitchPathDescription, TimeSpan) | Creates a path between the channels specified with pathDescription. This method does not support the mmWave subsystem. |
|  | SetPath(String, ReceiverPath, ReceiverCouplingPath, TimeSpan) | Creates a path between specified port and the receiver (RX) using the specified receiverPath and receiverCouplingPath. This method does not support the mmWave subsystem. |

Top

##### See Also

###### Reference

RfpmUtilityForSwitchReceiver Class

NationalInstruments.ModularInstruments.NIRfpm Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=ni-rfpm-api-ref path=ninetrfpmfx40ref/html/e30830b7-7545-85da-1459-758e44f298af.htm language=enus -->
## TOPIC 00052: ninetrfpmfx40ref/html/e30830b7-7545-85da-1459-758e44f298af.htm

- bundle_id: `ni-rfpm-api-ref`
- source_path: `ninetrfpmfx40ref/html/e30830b7-7545-85da-1459-758e44f298af.htm`
- source_url: https://docs-be.ni.com/bundle/ni-rfpm-api-ref/raw/resource/enus/ninetrfpmfx40ref/html/e30830b7-7545-85da-1459-758e44f298af.htm
- document_id: `ni-rfpm-api-ref`
- page_type: `leaf`
- content_type: ``

NIRfpm.RfsgSession Property

NIRfpmRfsgSession Property

Gets an NIRfsg session object representing the underlying NI-RFSG session used by NI-RFPM.

Namespace:

NationalInstruments.ModularInstruments.NIRfpm

Assembly:

##### Syntax

C#

VB

```text
public NIRfsg RfsgSession { get; }
```

```text
Public ReadOnly Property RfsgSession As NIRfsg
	Get
```

###### Property Value

NIRfsg

##### Exceptions

| Exception | Condition |
| --- | --- |
| ObjectDisposedException | RfsgSession was accessed after the associated NIRfpm object was disposed. |

##### Remarks

NIRfpm

##### See Also

###### Reference

NIRfpm Class

NationalInstruments.ModularInstruments.NIRfpm Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=ni-rfpm-api-ref path=ninetrfpmfx40ref/html/e7194a7e-93c6-3251-7912-4a0fbb828cd9.htm language=enus -->
## TOPIC 00053: ninetrfpmfx40ref/html/e7194a7e-93c6-3251-7912-4a0fbb828cd9.htm

- bundle_id: `ni-rfpm-api-ref`
- source_path: `ninetrfpmfx40ref/html/e7194a7e-93c6-3251-7912-4a0fbb828cd9.htm`
- source_url: https://docs-be.ni.com/bundle/ni-rfpm-api-ref/raw/resource/enus/ninetrfpmfx40ref/html/e7194a7e-93c6-3251-7912-4a0fbb828cd9.htm
- document_id: `ni-rfpm-api-ref`
- page_type: `leaf`
- content_type: ``

RfpmSourceCalibration.IsPowerCorrectionEnabled Property

RfpmSourceCalibrationIsPowerCorrectionEnabled Property

Namespace:

NationalInstruments.ModularInstruments.NIRfpm

Assembly:

##### Syntax

C#

VB

```text
public bool IsPowerCorrectionEnabled { get; set; }
```

```text
Public Property IsPowerCorrectionEnabled As Boolean
	Get
	Set
```

###### Property Value

Boolean

##### Exceptions

| Exception | Condition |
| --- | --- |
| ObjectDisposedException | IsPowerCorrectionEnabled was accessed after the associated NIRfpm or RfpmDriverUtility object was disposed. |
| IviCDriverException | The underlying NI-RFPM driver returned an error. |

##### See Also

###### Reference

RfpmSourceCalibration Class

NationalInstruments.ModularInstruments.NIRfpm Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=ni-rfpm-api-ref path=ninetrfpmfx40ref/html/eca8d763-039f-e08e-fcf8-57dfbec78ed0.htm language=enus -->
## TOPIC 00054: ninetrfpmfx40ref/html/eca8d763-039f-e08e-fcf8-57dfbec78ed0.htm

- bundle_id: `ni-rfpm-api-ref`
- source_path: `ninetrfpmfx40ref/html/eca8d763-039f-e08e-fcf8-57dfbec78ed0.htm`
- source_url: https://docs-be.ni.com/bundle/ni-rfpm-api-ref/raw/resource/enus/ninetrfpmfx40ref/html/eca8d763-039f-e08e-fcf8-57dfbec78ed0.htm
- document_id: `ni-rfpm-api-ref`
- page_type: `leaf`
- content_type: ``

RfpmUserCalibrationReceiverOffset.DigitalGain Property

RfpmUserCalibrationReceiverOffsetDigitalGain Property

Namespace:

NationalInstruments.ModularInstruments.NIRfpm

Assembly:

##### Syntax

C#

VB

```text
public double DigitalGain { get; }
```

```text
Public ReadOnly Property DigitalGain As Double
	Get
```

###### Property Value

Double

##### See Also

###### Reference

RfpmUserCalibrationReceiverOffset Class

NationalInstruments.ModularInstruments.NIRfpm Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=ni-rfpm-api-ref path=ninetrfpmfx40ref/html/ececa8fd-0c67-a8c6-14b1-d8d1b9be8888.htm language=enus -->
## TOPIC 00055: ninetrfpmfx40ref/html/ececa8fd-0c67-a8c6-14b1-d8d1b9be8888.htm

- bundle_id: `ni-rfpm-api-ref`
- source_path: `ninetrfpmfx40ref/html/ececa8fd-0c67-a8c6-14b1-d8d1b9be8888.htm`
- source_url: https://docs-be.ni.com/bundle/ni-rfpm-api-ref/raw/resource/enus/ninetrfpmfx40ref/html/ececa8fd-0c67-a8c6-14b1-d8d1b9be8888.htm
- document_id: `ni-rfpm-api-ref`
- page_type: `leaf`
- content_type: ``

NIRfpm.DriverOperation Property

NIRfpmDriverOperation Property

RfpmDriverOperation

Namespace:

NationalInstruments.ModularInstruments.NIRfpm

Assembly:

##### Syntax

C#

VB

```text
public RfpmDriverOperation DriverOperation { get; }
```

```text
Public ReadOnly Property DriverOperation As RfpmDriverOperation
	Get
```

###### Property Value

RfpmDriverOperation

RfpmDriverOperation

##### Exceptions

| Exception | Condition |
| --- | --- |
| ObjectDisposedException | DriverOperation was accessed after the associated NIRfpm object was disposed. |

##### See Also

###### Reference

NIRfpm Class

NationalInstruments.ModularInstruments.NIRfpm Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=ni-rfpm-api-ref path=ninetrfpmfx40ref/html/f583f002-3ffd-9b52-d636-7598a7dabb07.htm language=enus -->
## TOPIC 00056: ninetrfpmfx40ref/html/f583f002-3ffd-9b52-d636-7598a7dabb07.htm

- bundle_id: `ni-rfpm-api-ref`
- source_path: `ninetrfpmfx40ref/html/f583f002-3ffd-9b52-d636-7598a7dabb07.htm`
- source_url: https://docs-be.ni.com/bundle/ni-rfpm-api-ref/raw/resource/enus/ninetrfpmfx40ref/html/f583f002-3ffd-9b52-d636-7598a7dabb07.htm
- document_id: `ni-rfpm-api-ref`
- page_type: `leaf`
- content_type: ``

RfpmSourceCalibration Class

RfpmSourceCalibration Class

##### Inheritance Hierarchy

Namespace:

NationalInstruments.ModularInstruments.NIRfpm

Assembly:

##### Syntax

C#

VB

```text
public sealed class RfpmSourceCalibration : RfpmSubObject
```

```text
Public NotInheritable Class RfpmSourceCalibration
	Inherits RfpmSubObject
```

The RfpmSourceCalibration type exposes the following members.

##### Properties

|  | Name | Description |
| --- | --- | --- |
|  | IsPowerCorrectionEnabled | Gets or sets a value indicating whether the output power is corrected using calibrated source offsets during S-parameter measurements. If set to false nominal calibration source offsets will be returned when FetchOffset() method is called. This property does not support the mmWave subsystem. |

Top

##### Methods

|  | Name | Description |
| --- | --- | --- |
|  | Equals | Determines whether the specified Object is equal to the current Object. (Inherited from Object.) |
|  | FetchOffset | Fetches the stored source offset, calibrated power, digital gain, and settling time for a single switch path, frequency, and power setting given a specified port. This property does not support the mmWave subsystem. |
|  | GetHashCode | Serves as a hash function for a particular type. (Inherited from Object.) |
|  | GetMaxPowerLevel | Get the maximum source power for a single switch path, and frequency, given a specified port. This property does not support the mmWave subsystem. |
|  | GetType | Gets the Type of the current instance. (Inherited from Object.) |
|  | ToString | Returns a string that represents the current object. (Inherited from Object.) |

Top

##### Remarks

This class cannot be instantiated directly. It is instantiated when the
 [NIRfpm](07611137-d50f-4198-6321-da5299f2e31a.htm)
 session object is created. Access this class using
 [Source](4f62a724-be7a-1f90-f9f0-3bdef5714d8d.htm).

##### Thread Safety

static

Shared

##### See Also

###### Reference

NationalInstruments.ModularInstruments.NIRfpm Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=ni-rfpm-api-ref path=ninetrfpmfx40ref/html/f7300045-ba65-d7cc-4417-5271063dc32b.htm language=enus -->
## TOPIC 00057: ninetrfpmfx40ref/html/f7300045-ba65-d7cc-4417-5271063dc32b.htm

- bundle_id: `ni-rfpm-api-ref`
- source_path: `ninetrfpmfx40ref/html/f7300045-ba65-d7cc-4417-5271063dc32b.htm`
- source_url: https://docs-be.ni.com/bundle/ni-rfpm-api-ref/raw/resource/enus/ninetrfpmfx40ref/html/f7300045-ba65-d7cc-4417-5271063dc32b.htm
- document_id: `ni-rfpm-api-ref`
- page_type: `leaf`
- content_type: ``

RfpmWarningEventArgs Class

RfpmWarningEventArgs Class

Warning

##### Inheritance Hierarchy

Namespace:

NationalInstruments.ModularInstruments.NIRfpm

Assembly:

##### Syntax

C#

VB

```text
public sealed class RfpmWarningEventArgs : WarningEventArgs
```

```text
Public NotInheritable Class RfpmWarningEventArgs
	Inherits WarningEventArgs
```

The RfpmWarningEventArgs type exposes the following members.

##### Properties

|  | Name | Description |
| --- | --- | --- |
|  | Code | Warning code. (Inherited from WarningEventArgs.) |
|  | Text | Text description of the warning. (Inherited from WarningEventArgs.) |
|  | Warning | Gets the warning set in the warning event arguments. |

Top

##### Methods

|  | Name | Description |
| --- | --- | --- |
|  | Equals | Determines whether the specified Object is equal to the current Object. (Inherited from Object.) |
|  | GetHashCode | Serves as a hash function for a particular type. (Inherited from Object.) |
|  | GetType | Gets the Type of the current instance. (Inherited from Object.) |
|  | ToString | Returns a string that represents the current object. (Inherited from Object.) |

Top

##### Remarks

Programming Reference

##### Thread Safety

static

Shared

##### See Also

###### Reference

NationalInstruments.ModularInstruments.NIRfpm Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=ni-rfpm-api-ref path=ninetrfpmfx40ref/html/fcab9bc3-968b-5eb8-0ea8-52ad284cd87b.htm language=enus -->
## TOPIC 00058: ninetrfpmfx40ref/html/fcab9bc3-968b-5eb8-0ea8-52ad284cd87b.htm

- bundle_id: `ni-rfpm-api-ref`
- source_path: `ninetrfpmfx40ref/html/fcab9bc3-968b-5eb8-0ea8-52ad284cd87b.htm`
- source_url: https://docs-be.ni.com/bundle/ni-rfpm-api-ref/raw/resource/enus/ninetrfpmfx40ref/html/fcab9bc3-968b-5eb8-0ea8-52ad284cd87b.htm
- document_id: `ni-rfpm-api-ref`
- page_type: `leaf`
- content_type: ``

NationalInstruments.ModularInstruments.NIRfpm Namespace

NationalInstruments.ModularInstruments.NIRfpm Namespace

Contains objects that perform S-parameter measurements and receiver measurements on multiple ports using the NI vector signal transceiver (VST).

##### Classes

|  | Class | Description |
| --- | --- | --- |
|  | NIRfpm | Represents an NI-RFPM instrument driver session. |
|  | RfpmCalibration | Provides calibration resources and operations. This property does not support the mmWave subsystem except the following attribute: SkipSelfCalibrationTimestampCheck |
|  | RfpmDriverIdentity | Provides information about the instrument and the NI-RFPM driver. |
|  | RfpmDriverOperation | Provides properties and methods that control the operation of the NI-RFPM driver. |
|  | RfpmDriverUtility | Provides a basic set of driver utility operations. |
|  | RfpmLoadBoardCalibration | Provides properties for calibrating the load board. This property does not support the mmWave subsystem. |
|  | RfpmMeasurements | Contains methods and properties to perform measurements on NI-RFPM instruments. |
|  | RfpmMeasurementsDeembedding | Provides methods and properties to configure de-embedding settings. |
|  | RfpmMeasurementsReferenceLevelPortExtension | Provides methods and properties to configure reference level port extension settings. |
|  | RfpmMultipleMeasurementResultT | Represents the measurement results of all S-parameter fetch operations. |
|  | RfpmReceiverCalibration | Contains system calibration resources and operations for receiver calibrations. This property does not support the mmWave subsystem. |
|  | RfpmReceiverUserCalibration | Contains user calibration resources and operations for receiver calibrations. This property does not support the mmWave subsystem. |
|  | RfpmRfmxCallbacks | Contains methods to query, obtain, and set parameters for callbacks needed for RFmx. This property does not support the mmWave subsystem. |
|  | RfpmSingleMeasurementResultT | Represents the measurement results of single S-parameter fetch operation. |
|  | RfpmSourceCalibration | Provides system calibration resources and operations for source calibrations. This property does not support the mmWave subsystem. |
|  | RfpmSourceUserCalibration | Provides user calibration resources and operations for source calibrations. This property does not support the mmWave subsystem. |
|  | RfpmSubObject | Represents members that are common to all sub-object NI-RFPM classes. |
|  | RfpmSweepSetting | Provides properties describing a sweep setting. |
|  | RfpmSweepSettingsManager | Defines methods for loading and obtaining sweep settings. |
|  | RfpmSystemCalibration | Provides system calibration resources and operations. This property does not support the mmWave subsystem. |
|  | RfpmUserCalibration | Provides user calibration resources and operations. This property does not support the mmWave subsystem. |
|  | RfpmUserCalibrationReceiverOffset | Represents a receiver offset for a particular path to the switch. This property does not support the mmWave subsystem. |
|  | RfpmUserCalibrationSourceOffset | Represents a source offset for a particular path to the switch. This property does not support the mmWave subsystem. |
|  | RfpmUtilityForSwitch | Contains properties and methods for connecting or disconnecting source (TX) and receiver (RX) paths using the NI-RFPM Switch session used to create the NIRfpm session. This property does not support the mmWave subsystem. |
|  | RfpmUtilityForSwitchReceiver | Contains methods for connecting to receiver (RX) using the NIRfpmSwitch session used to create the NIRfpm session. This property does not support the mmWave subsystem. |
|  | RfpmUtilityForSwitchSource | Contains methods for connecting from source (TX) using the NI-RFPM Switch session used to create the NIRfpm session. This property does not support the mmWave subsystem. |
|  | RfpmVectorUserCalibration | Contains user calibration resources and operations for vector calibrations. This method does not support the mmWave subsystem. |
|  | RfpmWarning | Provides properties and methods for handling the warnings raised by the underlying driver. |
|  | RfpmWarningEventArgs | Provides data for the Warning event. |

##### Structures

|  | Structure | Description |
| --- | --- | --- |
|  | RfpmSystemCalibrationInformation | Represents available system calibration information. This property does not support the mmWave subsystem. |
|  | RfpmUserCalibrationInformation | Represents available user calibration information. This property does not support the mmWave subsystem. |

##### Enumerations

|  | Enumeration | Description |
| --- | --- | --- |
|  | CloseUserCalibrationAction | Specifies the action to take when closing the calibration. This property does not support the mmWave subsystem. |
|  | DeembeddingS2POrientation | Specifies the orientation of the data in the S2P file relative to the NI-RFPM port. |
|  | DoubleMeasurementFormat | Specifies the format to apply to the (double) measurement data. |
|  | FileOpenMode | Specifies the mode for opening files. |
|  | OptimizationMethod | The approach to use to optimize the path through NIRfpm. This property does not support the mmWave subsystem. |
|  | PowerLevelCoercion | Specifies if and how the power level will be coerced when fetching the source offset. This property does not support the mmWave subsystem. |
|  | PowerLevelType | Determines if power(s) represent average envelop power or peak envelop power. |
|  | ReceiverCouplingPath | Specifies the path of the NI-RFPM instrument to fetch the offset for. This property does not support the mmWave subsystem. |
|  | ReceiverPath | Specifies the receiver path to fetch the receiver offset data for. This property does not support the mmWave subsystem. |
|  | ReceiverType | Specifies the receiver to fetch from. |
|  | ReferenceClockSource | Specifies the clock source to use for the reference clock. |
|  | S2POrientation | Specifies the orientation of the data in the S2P file relative to the DUT port. |
|  | SourcePath | Specifies the source path to fetch the source offset data for. This property does not support the mmWave subsystem. |

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=ni-rfpm-api-ref path=ninetrfpmfx40ref/html/fd4bacaf-578d-185a-247b-178e423567e6.htm language=enus -->
## TOPIC 00059: ninetrfpmfx40ref/html/fd4bacaf-578d-185a-247b-178e423567e6.htm

- bundle_id: `ni-rfpm-api-ref`
- source_path: `ninetrfpmfx40ref/html/fd4bacaf-578d-185a-247b-178e423567e6.htm`
- source_url: https://docs-be.ni.com/bundle/ni-rfpm-api-ref/raw/resource/enus/ninetrfpmfx40ref/html/fd4bacaf-578d-185a-247b-178e423567e6.htm
- document_id: `ni-rfpm-api-ref`
- page_type: `leaf`
- content_type: ``

RfpmSystemCalibration.Initialize Method

RfpmSystemCalibrationInitialize Method

Namespace:

NationalInstruments.ModularInstruments.NIRfpm

Assembly:

##### Syntax

C#

VB

```text
public void Initialize()
```

```text
Public Sub Initialize
```

##### Exceptions

| Exception | Condition |
| --- | --- |
| ObjectDisposedException | Initialize was called after the associated NIRfpm or RfpmDriverUtility object was disposed. |
| IviCDriverException | The underlying NI-RFPM driver returned an error. |

##### See Also

###### Reference

RfpmSystemCalibration Class

NationalInstruments.ModularInstruments.NIRfpm Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=ni-rfpm-api-ref path=ninetrfpmfx40ref/html/fd9000d5-57ec-e5a6-2fcd-47e55b8cf716.htm language=enus -->
## TOPIC 00060: ninetrfpmfx40ref/html/fd9000d5-57ec-e5a6-2fcd-47e55b8cf716.htm

- bundle_id: `ni-rfpm-api-ref`
- source_path: `ninetrfpmfx40ref/html/fd9000d5-57ec-e5a6-2fcd-47e55b8cf716.htm`
- source_url: https://docs-be.ni.com/bundle/ni-rfpm-api-ref/raw/resource/enus/ninetrfpmfx40ref/html/fd9000d5-57ec-e5a6-2fcd-47e55b8cf716.htm
- document_id: `ni-rfpm-api-ref`
- page_type: `leaf`
- content_type: ``

RfpmLoadBoardCalibration.Revision Property

RfpmLoadBoardCalibrationRevision Property

Namespace:

NationalInstruments.ModularInstruments.NIRfpm

Assembly:

##### Syntax

C#

VB

```text
public string Revision { get; }
```

```text
Public ReadOnly Property Revision As String
	Get
```

###### Property Value

String

##### Exceptions

| Exception | Condition |
| --- | --- |
| ObjectDisposedException | Revision was accessed after the associated NIRfpm or RfpmDriverUtility object was disposed. |
| IviCDriverException | The underlying NI-RFPM driver returned an error. |

##### Remarks

DeviceResourceName

DeviceResourceName

DeviceResourceName

##### See Also

###### Reference

RfpmLoadBoardCalibration Class

NationalInstruments.ModularInstruments.NIRfpm Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=ni-rfpm-api-ref path=ninetrfpmfx40ref/html/fffd10d5-4b27-46ff-a622-d04822d6b111.htm language=enus -->
## TOPIC 00061: ninetrfpmfx40ref/html/fffd10d5-4b27-46ff-a622-d04822d6b111.htm

- bundle_id: `ni-rfpm-api-ref`
- source_path: `ninetrfpmfx40ref/html/fffd10d5-4b27-46ff-a622-d04822d6b111.htm`
- source_url: https://docs-be.ni.com/bundle/ni-rfpm-api-ref/raw/resource/enus/ninetrfpmfx40ref/html/fffd10d5-4b27-46ff-a622-d04822d6b111.htm
- document_id: `ni-rfpm-api-ref`
- page_type: `leaf`
- content_type: ``

RfpmUserCalibration.SaveToFile Method

RfpmUserCalibrationSaveToFile Method

Namespace:

NationalInstruments.ModularInstruments.NIRfpm

Assembly:

##### Syntax

C#

VB

```text
public void SaveToFile(
	string calibrationStorageFilePath,
	FileOpenMode fileOpenMode
)
```

```text
Public Sub SaveToFile ( 
	calibrationStorageFilePath As String,
	fileOpenMode As FileOpenMode
)
```

###### Parameters

- **calibrationStorageFilePath**
  - Type: SystemString The path to the calibration storage file.
- **fileOpenMode**
  - Type: NationalInstruments.ModularInstruments.NIRfpmFileOpenMode The mode defining how files with the same path are treated when saving calibration and configuration data

##### Exceptions

| Exception | Condition |
| --- | --- |
| ObjectDisposedException | SaveToFile(String, FileOpenMode) was called after the associated NIRfpm or RfpmDriverUtility object was disposed. |
| ArgumentException | The value for fileOpenMode is invalid. |
| ArgumentNullException | The value for calibrationStorageFilePath is . |
| IOException | Attempted to save to a file that already exists using Create mode. |
| IviCDriverException | Saving a calibration file was attempted before performing a calibration. - or - Merge was used with a file specified by calibrationStorageFilePath that does not already exist. - or - The file specified by calibrationStorageFilePath does not have a valid .tdms extension. - or - The value for calibrationStorageFilePath is empty. - or - The underlying NI-RFPM driver returned an error. |

##### Remarks

Close user calibration before saving calibration configuration.

##### See Also

###### Reference

RfpmUserCalibration Class

NationalInstruments.ModularInstruments.NIRfpm Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=ni-rfpm-api-ref path=ninetrfpmswitchfx40ref/html/017b8ee1-9508-47a8-a589-80129d169320.htm language=enus -->
## TOPIC 00062: ninetrfpmswitchfx40ref/html/017b8ee1-9508-47a8-a589-80129d169320.htm

- bundle_id: `ni-rfpm-api-ref`
- source_path: `ninetrfpmswitchfx40ref/html/017b8ee1-9508-47a8-a589-80129d169320.htm`
- source_url: https://docs-be.ni.com/bundle/ni-rfpm-api-ref/raw/resource/enus/ninetrfpmswitchfx40ref/html/017b8ee1-9508-47a8-a589-80129d169320.htm
- document_id: `ni-rfpm-api-ref`
- page_type: `leaf`
- content_type: ``

NIRfpmSwitch Constructor (String, Boolean, Boolean, String)

NIRfpmSwitch Constructor (String, Boolean, Boolean, String)

NIRfpmSwitch

Namespace:

NationalInstruments.ModularInstruments.NIRfpmSwitch

Assembly:

##### Syntax

C#

VB

```text
public NIRfpmSwitch(
	string resourceName,
	bool idQuery,
	bool resetDevice,
	string optionString
)
```

```text
Public Sub New ( 
	resourceName As String,
	idQuery As Boolean,
	resetDevice As Boolean,
	optionString As String
)
```

###### Parameters

- **resourceName**
  - Type: SystemString The name of the device on which the session is opened.
- **idQuery**
  - Type: SystemBoolean to verify that the instrument you initialize is supported by the NI-RFPM Switch driver software. The default value is .
- **resetDevice**
  - Type: SystemBoolean to reset the switch to a known state when the session is initialized. The default value is .
- **optionString**
  - Type: SystemString The initial state of the following session properties: RangeCheck, QueryInstrumentStatus, Cache, Simulate, and DriverSetup.

##### Exceptions

| Exception | Condition |
| --- | --- |
| ArgumentException | The value for resourceName is . - or - The value for resourceName is invalid. |
| InvalidOptionValueException | The value assigned to an option in optionString is invalid. |
| IviCDriverException | The underlying NI-RFPM Switch driver returned an error. |

##### See Also

###### Reference

NIRfpmSwitch Class

NIRfpmSwitch Overload

NationalInstruments.ModularInstruments.NIRfpmSwitch Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=ni-rfpm-api-ref path=ninetrfpmswitchfx40ref/html/01cc0b70-9990-3621-c84d-6f2db7b73eb7.htm language=enus -->
## TOPIC 00063: ninetrfpmswitchfx40ref/html/01cc0b70-9990-3621-c84d-6f2db7b73eb7.htm

- bundle_id: `ni-rfpm-api-ref`
- source_path: `ninetrfpmswitchfx40ref/html/01cc0b70-9990-3621-c84d-6f2db7b73eb7.htm`
- source_url: https://docs-be.ni.com/bundle/ni-rfpm-api-ref/raw/resource/enus/ninetrfpmswitchfx40ref/html/01cc0b70-9990-3621-c84d-6f2db7b73eb7.htm
- document_id: `ni-rfpm-api-ref`
- page_type: `leaf`
- content_type: ``

RfpmSwitchPath.DisconnectAll Method

RfpmSwitchPathDisconnectAll Method

Disconnects all existing paths.

Namespace:

NationalInstruments.ModularInstruments.NIRfpmSwitch

Assembly:

##### Syntax

C#

VB

```text
public void DisconnectAll()
```

```text
Public Sub DisconnectAll
```

##### Exceptions

| Exception | Condition |
| --- | --- |
| ObjectDisposedException | DisconnectAll was called after the associated NIRfpmSwitch or RfpmSwitchDriverUtility object was disposed. |
| IviCDriverException | The underlying NI-RFPM Switch driver returned an error. |

##### Remarks

PathRemainsWarningCode

##### See Also

###### Reference

RfpmSwitchPath Class

NationalInstruments.ModularInstruments.NIRfpmSwitch Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=ni-rfpm-api-ref path=ninetrfpmswitchfx40ref/html/01d56ce7-9a14-0692-a704-616f5f65d982.htm language=enus -->
## TOPIC 00064: ninetrfpmswitchfx40ref/html/01d56ce7-9a14-0692-a704-616f5f65d982.htm

- bundle_id: `ni-rfpm-api-ref`
- source_path: `ninetrfpmswitchfx40ref/html/01d56ce7-9a14-0692-a704-616f5f65d982.htm`
- source_url: https://docs-be.ni.com/bundle/ni-rfpm-api-ref/raw/resource/enus/ninetrfpmswitchfx40ref/html/01d56ce7-9a14-0692-a704-616f5f65d982.htm
- document_id: `ni-rfpm-api-ref`
- page_type: `leaf`
- content_type: ``

RfpmSwitchDriverIdentity.SpecificationMajorVersion Property

RfpmSwitchDriverIdentitySpecificationMajorVersion Property

Gets the major version number of the class specification with which the NI-RFPM Switch driver is compliant.

Namespace:

NationalInstruments.ModularInstruments.NIRfpmSwitch

Assembly:

##### Syntax

C#

VB

```text
public int SpecificationMajorVersion { get; }
```

```text
Public ReadOnly Property SpecificationMajorVersion As Integer
	Get
```

###### Property Value

Int32

###### Implements

##### Exceptions

| Exception | Condition |
| --- | --- |
| ObjectDisposedException | SpecificationMajorVersion was accessed after the associated NIRfpmSwitch object was disposed. |

##### See Also

###### Reference

RfpmSwitchDriverIdentity Class

NationalInstruments.ModularInstruments.NIRfpmSwitch Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=ni-rfpm-api-ref path=ninetrfpmswitchfx40ref/html/02b5a881-8c3d-9049-aaad-d1d717869e3c.htm language=enus -->
## TOPIC 00065: ninetrfpmswitchfx40ref/html/02b5a881-8c3d-9049-aaad-d1d717869e3c.htm

- bundle_id: `ni-rfpm-api-ref`
- source_path: `ninetrfpmswitchfx40ref/html/02b5a881-8c3d-9049-aaad-d1d717869e3c.htm`
- source_url: https://docs-be.ni.com/bundle/ni-rfpm-api-ref/raw/resource/enus/ninetrfpmswitchfx40ref/html/02b5a881-8c3d-9049-aaad-d1d717869e3c.htm
- document_id: `ni-rfpm-api-ref`
- page_type: `leaf`
- content_type: ``

NIRfpmSwitch.Identity Property

NIRfpmSwitchIdentity Property

RfpmSwitchDriverIdentity

Namespace:

NationalInstruments.ModularInstruments.NIRfpmSwitch

Assembly:

##### Syntax

C#

VB

```text
public RfpmSwitchDriverIdentity Identity { get; }
```

```text
Public ReadOnly Property Identity As RfpmSwitchDriverIdentity
	Get
```

###### Property Value

RfpmSwitchDriverIdentity

RfpmSwitchDriverIdentity

##### Exceptions

| Exception | Condition |
| --- | --- |
| ObjectDisposedException | Identity was accessed after the associated NIRfpmSwitch object was disposed. |

##### See Also

###### Reference

NIRfpmSwitch Class

NationalInstruments.ModularInstruments.NIRfpmSwitch Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=ni-rfpm-api-ref path=ninetrfpmswitchfx40ref/html/0f98a19d-9bb1-9fe5-8997-00a42cd4c012.htm language=enus -->
## TOPIC 00066: ninetrfpmswitchfx40ref/html/0f98a19d-9bb1-9fe5-8997-00a42cd4c012.htm

- bundle_id: `ni-rfpm-api-ref`
- source_path: `ninetrfpmswitchfx40ref/html/0f98a19d-9bb1-9fe5-8997-00a42cd4c012.htm`
- source_url: https://docs-be.ni.com/bundle/ni-rfpm-api-ref/raw/resource/enus/ninetrfpmswitchfx40ref/html/0f98a19d-9bb1-9fe5-8997-00a42cd4c012.htm
- document_id: `ni-rfpm-api-ref`
- page_type: `leaf`
- content_type: ``

RfpmSwitchWarning.ToString Method

RfpmSwitchWarningToString Method

RfpmSwitchWarning

Namespace:

NationalInstruments.ModularInstruments.NIRfpmSwitch

Assembly:

##### Syntax

C#

VB

```text
public override string ToString()
```

```text
Public Overrides Function ToString As String
```

###### Return Value

String

RfpmSwitchWarning

##### See Also

###### Reference

RfpmSwitchWarning Class

NationalInstruments.ModularInstruments.NIRfpmSwitch Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=ni-rfpm-api-ref path=ninetrfpmswitchfx40ref/html/141f41db-286f-3ae6-4614-58990dc912d4.htm language=enus -->
## TOPIC 00067: ninetrfpmswitchfx40ref/html/141f41db-286f-3ae6-4614-58990dc912d4.htm

- bundle_id: `ni-rfpm-api-ref`
- source_path: `ninetrfpmswitchfx40ref/html/141f41db-286f-3ae6-4614-58990dc912d4.htm`
- source_url: https://docs-be.ni.com/bundle/ni-rfpm-api-ref/raw/resource/enus/ninetrfpmswitchfx40ref/html/141f41db-286f-3ae6-4614-58990dc912d4.htm
- document_id: `ni-rfpm-api-ref`
- page_type: `leaf`
- content_type: ``

RfpmSwitchChannelCollection Methods

RfpmSwitchChannelCollection Methods

The [RfpmSwitchChannelCollection](e98aad1c-7f80-8ae5-1f61-1ea97513b102.htm) type exposes the following members.

##### Methods

|  | Name | Description |
| --- | --- | --- |
|  | Equals | Determines whether the specified object is equal to the current object. (Inherited from Object.) |
|  | GetHashCode | Serves as the default hash function. (Inherited from Object.) |
|  | GetType | Gets the Type of the current instance. (Inherited from Object.) |
|  | ToString | Returns a string that represents the current object. (Inherited from Object.) |

Top

##### See Also

###### Reference

RfpmSwitchChannelCollection Class

NationalInstruments.ModularInstruments.NIRfpmSwitch Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=ni-rfpm-api-ref path=ninetrfpmswitchfx40ref/html/19dc9ad8-0c00-ed34-0a95-d59579189fe3.htm language=enus -->
## TOPIC 00068: ninetrfpmswitchfx40ref/html/19dc9ad8-0c00-ed34-0a95-d59579189fe3.htm

- bundle_id: `ni-rfpm-api-ref`
- source_path: `ninetrfpmswitchfx40ref/html/19dc9ad8-0c00-ed34-0a95-d59579189fe3.htm`
- source_url: https://docs-be.ni.com/bundle/ni-rfpm-api-ref/raw/resource/enus/ninetrfpmswitchfx40ref/html/19dc9ad8-0c00-ed34-0a95-d59579189fe3.htm
- document_id: `ni-rfpm-api-ref`
- page_type: `leaf`
- content_type: ``

RfpmSwitchChannel.IsConfigurationChannel Property

RfpmSwitchChannelIsConfigurationChannel Property

Gets or sets a value indicating whether to reserve the channel for creating an internal path.

Namespace:

NationalInstruments.ModularInstruments.NIRfpmSwitch

Assembly:

##### Syntax

C#

VB

```text
public bool IsConfigurationChannel { get; set; }
```

```text
Public Property IsConfigurationChannel As Boolean
	Get
	Set
```

###### Property Value

Boolean

##### Exceptions

| Exception | Condition |
| --- | --- |
| ObjectDisposedException | IsConfigurationChannel was accessed after the associated NIRfpmSwitch or RfpmSwitchDriverUtility object was disposed. |
| IviCDriverException | The underlying NI-RFPM Switch driver returned an error. |

##### Remarks

Connect(String, String)

After you identify a channel as a configuration channel, you cannot use that channel for external connections. [Connect(String, String)](46e6f96b-47c5-e9be-e30e-5d5d50b82868.htm) throws [InvalidOperationException](https://docs.microsoft.com/dotnet/api/system.invalidoperationexception)
 when you attempt to establish a connection between a configuration channel and any other channel.

##### See Also

###### Reference

RfpmSwitchChannel Class

NationalInstruments.ModularInstruments.NIRfpmSwitch Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=ni-rfpm-api-ref path=ninetrfpmswitchfx40ref/html/219f5972-e0ed-8bcf-56f1-e82458e012e1.htm language=enus -->
## TOPIC 00069: ninetrfpmswitchfx40ref/html/219f5972-e0ed-8bcf-56f1-e82458e012e1.htm

- bundle_id: `ni-rfpm-api-ref`
- source_path: `ninetrfpmswitchfx40ref/html/219f5972-e0ed-8bcf-56f1-e82458e012e1.htm`
- source_url: https://docs-be.ni.com/bundle/ni-rfpm-api-ref/raw/resource/enus/ninetrfpmswitchfx40ref/html/219f5972-e0ed-8bcf-56f1-e82458e012e1.htm
- document_id: `ni-rfpm-api-ref`
- page_type: `leaf`
- content_type: ``

RfpmSwitchWarning.ImplicitConnectionExistsWarningCode Property

RfpmSwitchWarningImplicitConnectionExistsWarningCode Property

Gets the warning code if the path between the channels is not available or the channels are not explicitly connected, but the implicit connection exists between them.

Namespace:

NationalInstruments.ModularInstruments.NIRfpmSwitch

Assembly:

##### Syntax

C#

VB

```text
public static Guid ImplicitConnectionExistsWarningCode { get; }
```

```text
Public Shared ReadOnly Property ImplicitConnectionExistsWarningCode As Guid
	Get
```

###### Property Value

Guid

Guid

##### See Also

###### Reference

RfpmSwitchWarning Class

NationalInstruments.ModularInstruments.NIRfpmSwitch Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=ni-rfpm-api-ref path=ninetrfpmswitchfx40ref/html/2b7b42f9-a0aa-6e52-dbb7-501a682ac7b3.htm language=enus -->
## TOPIC 00070: ninetrfpmswitchfx40ref/html/2b7b42f9-a0aa-6e52-dbb7-501a682ac7b3.htm

- bundle_id: `ni-rfpm-api-ref`
- source_path: `ninetrfpmswitchfx40ref/html/2b7b42f9-a0aa-6e52-dbb7-501a682ac7b3.htm`
- source_url: https://docs-be.ni.com/bundle/ni-rfpm-api-ref/raw/resource/enus/ninetrfpmswitchfx40ref/html/2b7b42f9-a0aa-6e52-dbb7-501a682ac7b3.htm
- document_id: `ni-rfpm-api-ref`
- page_type: `leaf`
- content_type: ``

RfpmSwitchChannelCollection Properties

RfpmSwitchChannelCollection Properties

The [RfpmSwitchChannelCollection](e98aad1c-7f80-8ae5-1f61-1ea97513b102.htm) type exposes the following members.

##### Properties

|  | Name | Description |
| --- | --- | --- |
|  | Count | Gets the number of channels supported by the specified device. |
|  | ItemInt32 | Gets the RfpmSwitchChannel object for the specified index. |
|  | ItemString | Gets the RfpmSwitchChannel object for the specified channel name. |

Top

##### See Also

###### Reference

RfpmSwitchChannelCollection Class

NationalInstruments.ModularInstruments.NIRfpmSwitch Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=ni-rfpm-api-ref path=ninetrfpmswitchfx40ref/html/2bfd1992-33d5-744b-87ef-7c750ff631f8.htm language=enus -->
## TOPIC 00071: ninetrfpmswitchfx40ref/html/2bfd1992-33d5-744b-87ef-7c750ff631f8.htm

- bundle_id: `ni-rfpm-api-ref`
- source_path: `ninetrfpmswitchfx40ref/html/2bfd1992-33d5-744b-87ef-7c750ff631f8.htm`
- source_url: https://docs-be.ni.com/bundle/ni-rfpm-api-ref/raw/resource/enus/ninetrfpmswitchfx40ref/html/2bfd1992-33d5-744b-87ef-7c750ff631f8.htm
- document_id: `ni-rfpm-api-ref`
- page_type: `leaf`
- content_type: ``

NIRfpmSwitch Constructor (String, Boolean, Boolean)

NIRfpmSwitch Constructor (String, Boolean, Boolean)

NIRfpmSwitch

Namespace:

NationalInstruments.ModularInstruments.NIRfpmSwitch

Assembly:

##### Syntax

C#

VB

```text
public NIRfpmSwitch(
	string resourceName,
	bool idQuery,
	bool resetDevice
)
```

```text
Public Sub New ( 
	resourceName As String,
	idQuery As Boolean,
	resetDevice As Boolean
)
```

###### Parameters

- **resourceName**
  - Type: SystemString The name of the device on which the session is opened.
- **idQuery**
  - Type: SystemBoolean to verify that the instrument you initialize is supported by the NI-RFPM Switch driver software. The default value is .
- **resetDevice**
  - Type: SystemBoolean to reset the switch to a known state when the session is initialized. The default value is .

##### Exceptions

| Exception | Condition |
| --- | --- |
| ArgumentException | The value for resourceName is . - or - The value for resourceName is invalid. |
| IviCDriverException | The underlying NI-RFPM Switch driver returned an error. |

##### See Also

###### Reference

NIRfpmSwitch Class

NIRfpmSwitch Overload

NationalInstruments.ModularInstruments.NIRfpmSwitch Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=ni-rfpm-api-ref path=ninetrfpmswitchfx40ref/html/2c55650c-fcfb-1090-eb7a-a4950c861527.htm language=enus -->
## TOPIC 00072: ninetrfpmswitchfx40ref/html/2c55650c-fcfb-1090-eb7a-a4950c861527.htm

- bundle_id: `ni-rfpm-api-ref`
- source_path: `ninetrfpmswitchfx40ref/html/2c55650c-fcfb-1090-eb7a-a4950c861527.htm`
- source_url: https://docs-be.ni.com/bundle/ni-rfpm-api-ref/raw/resource/enus/ninetrfpmswitchfx40ref/html/2c55650c-fcfb-1090-eb7a-a4950c861527.htm
- document_id: `ni-rfpm-api-ref`
- page_type: `leaf`
- content_type: ``

RfpmSwitchCharacteristics.DCVoltageMax Property

RfpmSwitchCharacteristicsDCVoltageMax Property

Gets the maximum DC voltage the channel can switch.

Namespace:

NationalInstruments.ModularInstruments.NIRfpmSwitch

Assembly:

##### Syntax

C#

VB

```text
public double DCVoltageMax { get; }
```

```text
Public ReadOnly Property DCVoltageMax As Double
	Get
```

###### Property Value

Double

##### Exceptions

| Exception | Condition |
| --- | --- |
| ObjectDisposedException | DCVoltageMax was accessed after the associated NIRfpmSwitch or RfpmSwitchDriverUtility object was disposed. |
| IviCDriverException | The underlying NI-RFPM Switch driver returned an error. |

##### See Also

###### Reference

RfpmSwitchCharacteristics Class

NationalInstruments.ModularInstruments.NIRfpmSwitch Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=ni-rfpm-api-ref path=ninetrfpmswitchfx40ref/html/408fb6af-b2b2-54ec-89c8-78595c33dd6e.htm language=enus -->
## TOPIC 00073: ninetrfpmswitchfx40ref/html/408fb6af-b2b2-54ec-89c8-78595c33dd6e.htm

- bundle_id: `ni-rfpm-api-ref`
- source_path: `ninetrfpmswitchfx40ref/html/408fb6af-b2b2-54ec-89c8-78595c33dd6e.htm`
- source_url: https://docs-be.ni.com/bundle/ni-rfpm-api-ref/raw/resource/enus/ninetrfpmswitchfx40ref/html/408fb6af-b2b2-54ec-89c8-78595c33dd6e.htm
- document_id: `ni-rfpm-api-ref`
- page_type: `leaf`
- content_type: ``

RfpmSwitchCharacteristics.DCPowerSwitchingMax Property

RfpmSwitchCharacteristicsDCPowerSwitchingMax Property

Gets the maximum DC power that the channel can switch.

Namespace:

NationalInstruments.ModularInstruments.NIRfpmSwitch

Assembly:

##### Syntax

C#

VB

```text
public double DCPowerSwitchingMax { get; }
```

```text
Public ReadOnly Property DCPowerSwitchingMax As Double
	Get
```

###### Property Value

Double

##### Exceptions

| Exception | Condition |
| --- | --- |
| ObjectDisposedException | DCPowerSwitchingMax was accessed after the associated NIRfpmSwitch or RfpmSwitchDriverUtility object was disposed. |
| IviCDriverException | The underlying NI-RFPM Switch driver returned an error. |

##### See Also

###### Reference

RfpmSwitchCharacteristics Class

NationalInstruments.ModularInstruments.NIRfpmSwitch Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=ni-rfpm-api-ref path=ninetrfpmswitchfx40ref/html/46e6f96b-47c5-e9be-e30e-5d5d50b82868.htm language=enus -->
## TOPIC 00074: ninetrfpmswitchfx40ref/html/46e6f96b-47c5-e9be-e30e-5d5d50b82868.htm

- bundle_id: `ni-rfpm-api-ref`
- source_path: `ninetrfpmswitchfx40ref/html/46e6f96b-47c5-e9be-e30e-5d5d50b82868.htm`
- source_url: https://docs-be.ni.com/bundle/ni-rfpm-api-ref/raw/resource/enus/ninetrfpmswitchfx40ref/html/46e6f96b-47c5-e9be-e30e-5d5d50b82868.htm
- document_id: `ni-rfpm-api-ref`
- page_type: `leaf`
- content_type: ``

RfpmSwitchPath.Connect Method

RfpmSwitchPathConnect Method

channel1

channel2

Namespace:

NationalInstruments.ModularInstruments.NIRfpmSwitch

Assembly:

##### Syntax

C#

VB

```text
public void Connect(
	string channel1,
	string channel2
)
```

```text
Public Sub Connect ( 
	channel1 As String,
	channel2 As String
)
```

###### Parameters

- **channel1**
  - Type: SystemString The name of the first channel in the path.
- **channel2**
  - Type: SystemString The name of the last channel in the path.

##### Exceptions

| Exception | Condition |
| --- | --- |
| SelectorNameException | channel1 or channel2 was unknown or . |
| ObjectDisposedException | Connect(String, String) was called after the associated NIRfpmSwitch or RfpmSwitchDriverUtility object was disposed. |
| InvalidOperationException | The two channels were already explicitly connected by calling Connect(String, String) or SetPath(RfpmSwitchPathDescription). - or - Both channels are connected to a different source. - or -channel1 and channel2 are the same channel. - or - The driver cannot find a path between the two channels. |
| IviCDriverException | The underlying NI-RFPM Switch driver returned an error. |

##### Remarks

| Note |
| --- |
| Paths are bidirectional. For example, if a path exists from channel1 to channel2, a path from channel2 to channel1 also exists. |

##### See Also

###### Reference

RfpmSwitchPath Class

NationalInstruments.ModularInstruments.NIRfpmSwitch Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=ni-rfpm-api-ref path=ninetrfpmswitchfx40ref/html/50b02ad0-860c-f5c1-f0a6-a9d2358f2af7.htm language=enus -->
## TOPIC 00075: ninetrfpmswitchfx40ref/html/50b02ad0-860c-f5c1-f0a6-a9d2358f2af7.htm

- bundle_id: `ni-rfpm-api-ref`
- source_path: `ninetrfpmswitchfx40ref/html/50b02ad0-860c-f5c1-f0a6-a9d2358f2af7.htm`
- source_url: https://docs-be.ni.com/bundle/ni-rfpm-api-ref/raw/resource/enus/ninetrfpmswitchfx40ref/html/50b02ad0-860c-f5c1-f0a6-a9d2358f2af7.htm
- document_id: `ni-rfpm-api-ref`
- page_type: `leaf`
- content_type: ``

RfpmSwitchDriverUtility.Lock Method (PrecisionTimeSpan)

RfpmSwitchDriverUtilityLock Method (PrecisionTimeSpan)

Acquires a synchronization lock on this instance of the NI-RFPM Switch driver.

Namespace:

NationalInstruments.ModularInstruments.NIRfpmSwitch

Assembly:

##### Syntax

C#

VB

```text
public IIviDriverLock Lock(
	PrecisionTimeSpan maxTime
)
```

```text
Public Function Lock ( 
	maxTime As PrecisionTimeSpan
) As IIviDriverLock
```

###### Parameters

- **maxTime**
  - Type: Ivi.DriverPrecisionTimeSpanThe maximum time in seconds for the synchronization lock to complete.

###### Return Value

IIviDriverLock

###### Implements

##### Exceptions

| Exception | Condition |
| --- | --- |
| ObjectDisposedException | Lock(PrecisionTimeSpan) was called after the associated RfpmSwitchDriverUtility object was disposed. |

##### See Also

###### Reference

RfpmSwitchDriverUtility Class

Lock Overload

NationalInstruments.ModularInstruments.NIRfpmSwitch Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=ni-rfpm-api-ref path=ninetrfpmswitchfx40ref/html/50fe1a67-2b58-1456-d85b-43280f2faedf.htm language=enus -->
## TOPIC 00076: ninetrfpmswitchfx40ref/html/50fe1a67-2b58-1456-d85b-43280f2faedf.htm

- bundle_id: `ni-rfpm-api-ref`
- source_path: `ninetrfpmswitchfx40ref/html/50fe1a67-2b58-1456-d85b-43280f2faedf.htm`
- source_url: https://docs-be.ni.com/bundle/ni-rfpm-api-ref/raw/resource/enus/ninetrfpmswitchfx40ref/html/50fe1a67-2b58-1456-d85b-43280f2faedf.htm
- document_id: `ni-rfpm-api-ref`
- page_type: `leaf`
- content_type: ``

RfpmSwitchDriverIdentity.Vendor Property

RfpmSwitchDriverIdentityVendor Property

Gets the the name of the vendor that supplies the NI-RFPM Switch driver.

Namespace:

NationalInstruments.ModularInstruments.NIRfpmSwitch

Assembly:

##### Syntax

C#

VB

```text
public string Vendor { get; }
```

```text
Public ReadOnly Property Vendor As String
	Get
```

###### Property Value

String

###### Implements

##### Exceptions

| Exception | Condition |
| --- | --- |
| ObjectDisposedException | Vendor was accessed after the associated NIRfpmSwitch or RfpmSwitchDriverUtility object was disposed. |
| IviCDriverException | The underlying NI-RFPM Switch driver returned an error. |

##### See Also

###### Reference

RfpmSwitchDriverIdentity Class

NationalInstruments.ModularInstruments.NIRfpmSwitch Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=ni-rfpm-api-ref path=ninetrfpmswitchfx40ref/html/5236ed4c-e9da-ac31-ba01-eec881895f5e.htm language=enus -->
## TOPIC 00077: ninetrfpmswitchfx40ref/html/5236ed4c-e9da-ac31-ba01-eec881895f5e.htm

- bundle_id: `ni-rfpm-api-ref`
- source_path: `ninetrfpmswitchfx40ref/html/5236ed4c-e9da-ac31-ba01-eec881895f5e.htm`
- source_url: https://docs-be.ni.com/bundle/ni-rfpm-api-ref/raw/resource/enus/ninetrfpmswitchfx40ref/html/5236ed4c-e9da-ac31-ba01-eec881895f5e.htm
- document_id: `ni-rfpm-api-ref`
- page_type: `leaf`
- content_type: ``

NIRfpmSwitch.Utility Property

NIRfpmSwitchUtility Property

RfpmSwitchDriverUtility

Namespace:

NationalInstruments.ModularInstruments.NIRfpmSwitch

Assembly:

##### Syntax

C#

VB

```text
public RfpmSwitchDriverUtility Utility { get; }
```

```text
Public ReadOnly Property Utility As RfpmSwitchDriverUtility
	Get
```

###### Property Value

RfpmSwitchDriverUtility

RfpmSwitchDriverUtility

##### Exceptions

| Exception | Condition |
| --- | --- |
| ObjectDisposedException | Utility was accessed after the associated NIRfpmSwitch object was disposed. |

##### See Also

###### Reference

NIRfpmSwitch Class

NationalInstruments.ModularInstruments.NIRfpmSwitch Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=ni-rfpm-api-ref path=ninetrfpmswitchfx40ref/html/62ffcdf0-827f-5bfe-69b9-94f382307d96.htm language=enus -->
## TOPIC 00078: ninetrfpmswitchfx40ref/html/62ffcdf0-827f-5bfe-69b9-94f382307d96.htm

- bundle_id: `ni-rfpm-api-ref`
- source_path: `ninetrfpmswitchfx40ref/html/62ffcdf0-827f-5bfe-69b9-94f382307d96.htm`
- source_url: https://docs-be.ni.com/bundle/ni-rfpm-api-ref/raw/resource/enus/ninetrfpmswitchfx40ref/html/62ffcdf0-827f-5bfe-69b9-94f382307d96.htm
- document_id: `ni-rfpm-api-ref`
- page_type: `leaf`
- content_type: ``

RfpmSwitchDriverUtility.Reset Method

RfpmSwitchDriverUtilityReset Method

Disconnects all created paths and returns the switch device to the initialization state.

Namespace:

NationalInstruments.ModularInstruments.NIRfpmSwitch

Assembly:

##### Syntax

C#

VB

```text
public void Reset()
```

```text
Public Sub Reset
```

###### Implements

##### Exceptions

| Exception | Condition |
| --- | --- |
| ObjectDisposedException | Reset was called after the associated NIRfpmSwitch or RfpmSwitchDriverUtility object was disposed. |
| IviCDriverException | The underlying NI-RFPM Switch driver returned an error. |

##### Remarks

Configuration channel and source channel settings remain unchanged.

##### See Also

###### Reference

RfpmSwitchDriverUtility Class

NationalInstruments.ModularInstruments.NIRfpmSwitch Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=ni-rfpm-api-ref path=ninetrfpmswitchfx40ref/html/63509172-7c9e-e67f-3534-a23937e4cdce.htm language=enus -->
## TOPIC 00079: ninetrfpmswitchfx40ref/html/63509172-7c9e-e67f-3534-a23937e4cdce.htm

- bundle_id: `ni-rfpm-api-ref`
- source_path: `ninetrfpmswitchfx40ref/html/63509172-7c9e-e67f-3534-a23937e4cdce.htm`
- source_url: https://docs-be.ni.com/bundle/ni-rfpm-api-ref/raw/resource/enus/ninetrfpmswitchfx40ref/html/63509172-7c9e-e67f-3534-a23937e4cdce.htm
- document_id: `ni-rfpm-api-ref`
- page_type: `leaf`
- content_type: ``

WireMode Enumeration

WireMode Enumeration

WireMode

Namespace:

NationalInstruments.ModularInstruments.NIRfpmSwitch

Assembly:

##### Syntax

C#

VB

```text
public enum WireMode
```

```text
Public Enumeration WireMode
```

##### Members

|  | Member name | Value | Description |
| --- | --- | --- | --- |
|  | OneWireMode | 1 | The switch device is in one-wire mode. |
|  | TwoWireMode | 2 | The switch device is in two-wire mode. |
|  | FourWireMode | 4 | The switch device is in four-wire mode. |

##### See Also

###### Reference

NationalInstruments.ModularInstruments.NIRfpmSwitch Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=ni-rfpm-api-ref path=ninetrfpmswitchfx40ref/html/663b455d-11b4-a547-c835-7f68191d7c8f.htm language=enus -->
## TOPIC 00080: ninetrfpmswitchfx40ref/html/663b455d-11b4-a547-c835-7f68191d7c8f.htm

- bundle_id: `ni-rfpm-api-ref`
- source_path: `ninetrfpmswitchfx40ref/html/663b455d-11b4-a547-c835-7f68191d7c8f.htm`
- source_url: https://docs-be.ni.com/bundle/ni-rfpm-api-ref/raw/resource/enus/ninetrfpmswitchfx40ref/html/663b455d-11b4-a547-c835-7f68191d7c8f.htm
- document_id: `ni-rfpm-api-ref`
- page_type: `leaf`
- content_type: ``

RfpmSwitchDriverIdentity.SpecificationMinorVersion Property

RfpmSwitchDriverIdentitySpecificationMinorVersion Property

Gets the minor version number of the class specification with which the NI-RFPM Switch driver is compliant.

Namespace:

NationalInstruments.ModularInstruments.NIRfpmSwitch

Assembly:

##### Syntax

C#

VB

```text
public int SpecificationMinorVersion { get; }
```

```text
Public ReadOnly Property SpecificationMinorVersion As Integer
	Get
```

###### Property Value

Int32

###### Implements

##### Exceptions

| Exception | Condition |
| --- | --- |
| ObjectDisposedException | SpecificationMinorVersion was accessed after the associated NIRfpmSwitch object was disposed. |

##### See Also

###### Reference

RfpmSwitchDriverIdentity Class

NationalInstruments.ModularInstruments.NIRfpmSwitch Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=ni-rfpm-api-ref path=ninetrfpmswitchfx40ref/html/66f2be4d-97d4-273e-df27-148f2a7a571f.htm language=enus -->
## TOPIC 00081: ninetrfpmswitchfx40ref/html/66f2be4d-97d4-273e-df27-148f2a7a571f.htm

- bundle_id: `ni-rfpm-api-ref`
- source_path: `ninetrfpmswitchfx40ref/html/66f2be4d-97d4-273e-df27-148f2a7a571f.htm`
- source_url: https://docs-be.ni.com/bundle/ni-rfpm-api-ref/raw/resource/enus/ninetrfpmswitchfx40ref/html/66f2be4d-97d4-273e-df27-148f2a7a571f.htm
- document_id: `ni-rfpm-api-ref`
- page_type: `leaf`
- content_type: ``

PathCapability Enumeration

PathCapability Enumeration

The status of a path between two channels.

Namespace:

NationalInstruments.ModularInstruments.NIRfpmSwitch

Assembly:

##### Syntax

C#

VB

```text
public enum PathCapability
```

```text
Public Enumeration PathCapability
```

##### Members

|  | Member name | Value | Description |
| --- | --- | --- | --- |
|  | Available | 1 | NI-RFPM Switch can create the path at this time. |
|  | Exists | 2 | The path already exists. |
|  | Unsupported | 3 | The switch device is not capable of creating a path between the channels you specify. |
|  | ResourceInUse | 4 | Although the path is valid, NI-RFPM Switch cannot create the path at this moment because the switch is currently using one or more of the required channels to create another path. You must destroy the other path before creating this one. |
|  | SourceConflict | 5 | NI-RFPM Switch cannot create a path because both channels are connected to different source channels. |
|  | ChannelNotAvailable | 6 | NI-RFPM Switch cannot create a path between the two channels because one of the channels is a configuration channel and unavailable for external connections. |

##### See Also

###### Reference

NationalInstruments.ModularInstruments.NIRfpmSwitch Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=ni-rfpm-api-ref path=ninetrfpmswitchfx40ref/html/6d020ddb-fbcb-f9ee-b293-5b2b5b5f14a9.htm language=enus -->
## TOPIC 00082: ninetrfpmswitchfx40ref/html/6d020ddb-fbcb-f9ee-b293-5b2b5b5f14a9.htm

- bundle_id: `ni-rfpm-api-ref`
- source_path: `ninetrfpmswitchfx40ref/html/6d020ddb-fbcb-f9ee-b293-5b2b5b5f14a9.htm`
- source_url: https://docs-be.ni.com/bundle/ni-rfpm-api-ref/raw/resource/enus/ninetrfpmswitchfx40ref/html/6d020ddb-fbcb-f9ee-b293-5b2b5b5f14a9.htm
- document_id: `ni-rfpm-api-ref`
- page_type: `leaf`
- content_type: ``

RfpmSwitchChannelCollection.Item Property

RfpmSwitchChannelCollectionItem Property

##### Overload List

|  | Name | Description |
| --- | --- | --- |
|  | ItemInt32 | Gets the RfpmSwitchChannel object for the specified index. |
|  | ItemString | Gets the RfpmSwitchChannel object for the specified channel name. |

Top

##### See Also

###### Reference

RfpmSwitchChannelCollection Class

NationalInstruments.ModularInstruments.NIRfpmSwitch Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=ni-rfpm-api-ref path=ninetrfpmswitchfx40ref/html/6e981103-0f9f-b8ba-fb3c-054e239e70f7.htm language=enus -->
## TOPIC 00083: ninetrfpmswitchfx40ref/html/6e981103-0f9f-b8ba-fb3c-054e239e70f7.htm

- bundle_id: `ni-rfpm-api-ref`
- source_path: `ninetrfpmswitchfx40ref/html/6e981103-0f9f-b8ba-fb3c-054e239e70f7.htm`
- source_url: https://docs-be.ni.com/bundle/ni-rfpm-api-ref/raw/resource/enus/ninetrfpmswitchfx40ref/html/6e981103-0f9f-b8ba-fb3c-054e239e70f7.htm
- document_id: `ni-rfpm-api-ref`
- page_type: `leaf`
- content_type: ``

RfpmSwitchChannel.Characteristics Property

RfpmSwitchChannelCharacteristics Property

RfpmSwitchCharacteristics

Namespace:

NationalInstruments.ModularInstruments.NIRfpmSwitch

Assembly:

##### Syntax

C#

VB

```text
public RfpmSwitchCharacteristics Characteristics { get; }
```

```text
Public ReadOnly Property Characteristics As RfpmSwitchCharacteristics
	Get
```

###### Property Value

RfpmSwitchCharacteristics

RfpmSwitchCharacteristics

##### Exceptions

| Exception | Condition |
| --- | --- |
| ObjectDisposedException | Characteristics was accessed after the associated NIRfpmSwitch object was disposed. |

##### See Also

###### Reference

RfpmSwitchChannel Class

NationalInstruments.ModularInstruments.NIRfpmSwitch Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=ni-rfpm-api-ref path=ninetrfpmswitchfx40ref/html/6f37f05d-00bc-b91f-43ef-db02057ebdd6.htm language=enus -->
## TOPIC 00084: ninetrfpmswitchfx40ref/html/6f37f05d-00bc-b91f-43ef-db02057ebdd6.htm

- bundle_id: `ni-rfpm-api-ref`
- source_path: `ninetrfpmswitchfx40ref/html/6f37f05d-00bc-b91f-43ef-db02057ebdd6.htm`
- source_url: https://docs-be.ni.com/bundle/ni-rfpm-api-ref/raw/resource/enus/ninetrfpmswitchfx40ref/html/6f37f05d-00bc-b91f-43ef-db02057ebdd6.htm
- document_id: `ni-rfpm-api-ref`
- page_type: `leaf`
- content_type: ``

RfpmSwitchDriverIdentity Methods

RfpmSwitchDriverIdentity Methods

The [RfpmSwitchDriverIdentity](5ce5d61e-d429-3837-f930-903791832618.htm) type exposes the following members.

##### Methods

|  | Name | Description |
| --- | --- | --- |
|  | Equals | Determines whether the specified object is equal to the current object. (Inherited from Object.) |
|  | GetGroupCapabilities | Returns a list of names of the class capability groups implemented by the IVI-specific driver. |
|  | GetHashCode | Serves as the default hash function. (Inherited from Object.) |
|  | GetSupportedInstrumentModels | Returns a list of names of instrument models with which the IVI-specific driver is compatible. |
|  | GetType | Gets the Type of the current instance. (Inherited from Object.) |
|  | ToString | Returns a string that represents the current object. (Inherited from Object.) |

Top

##### See Also

###### Reference

RfpmSwitchDriverIdentity Class

NationalInstruments.ModularInstruments.NIRfpmSwitch Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=ni-rfpm-api-ref path=ninetrfpmswitchfx40ref/html/a67904ea-5be3-9068-fc3c-401722cb15db.htm language=enus -->
## TOPIC 00085: ninetrfpmswitchfx40ref/html/a67904ea-5be3-9068-fc3c-401722cb15db.htm

- bundle_id: `ni-rfpm-api-ref`
- source_path: `ninetrfpmswitchfx40ref/html/a67904ea-5be3-9068-fc3c-401722cb15db.htm`
- source_url: https://docs-be.ni.com/bundle/ni-rfpm-api-ref/raw/resource/enus/ninetrfpmswitchfx40ref/html/a67904ea-5be3-9068-fc3c-401722cb15db.htm
- document_id: `ni-rfpm-api-ref`
- page_type: `leaf`
- content_type: ``

RfpmSwitchWarningEventArgs Class

RfpmSwitchWarningEventArgs Class

RfpmSwitchWarning

##### Inheritance Hierarchy

Namespace:

NationalInstruments.ModularInstruments.NIRfpmSwitch

Assembly:

##### Syntax

C#

VB

```text
public sealed class RfpmSwitchWarningEventArgs : WarningEventArgs
```

```text
Public NotInheritable Class RfpmSwitchWarningEventArgs
	Inherits WarningEventArgs
```

The RfpmSwitchWarningEventArgs type exposes the following members.

##### Properties

|  | Name | Description |
| --- | --- | --- |
|  | Code | Warning code. (Inherited from WarningEventArgs.) |
|  | Text | Text description of the warning. (Inherited from WarningEventArgs.) |
|  | Warning | Gets the warning set in the Warning Event Args. |

Top

##### Methods

|  | Name | Description |
| --- | --- | --- |
|  | Equals | Determines whether the specified object is equal to the current object. (Inherited from Object.) |
|  | GetHashCode | Serves as the default hash function. (Inherited from Object.) |
|  | GetType | Gets the Type of the current instance. (Inherited from Object.) |
|  | ToString | Returns a string that represents the current object. (Inherited from Object.) |

Top

##### Remarks

NI-SWITCH Function Reference

##### Thread Safety

static

Shared

##### See Also

###### Reference

NationalInstruments.ModularInstruments.NIRfpmSwitch Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=ni-rfpm-api-ref path=ninetrfpmswitchfx40ref/html/ad02aa8a-26d8-14e8-b64a-0ee806d394df.htm language=enus -->
## TOPIC 00086: ninetrfpmswitchfx40ref/html/ad02aa8a-26d8-14e8-b64a-0ee806d394df.htm

- bundle_id: `ni-rfpm-api-ref`
- source_path: `ninetrfpmswitchfx40ref/html/ad02aa8a-26d8-14e8-b64a-0ee806d394df.htm`
- source_url: https://docs-be.ni.com/bundle/ni-rfpm-api-ref/raw/resource/enus/ninetrfpmswitchfx40ref/html/ad02aa8a-26d8-14e8-b64a-0ee806d394df.htm
- document_id: `ni-rfpm-api-ref`
- page_type: `leaf`
- content_type: ``

RfpmSwitchCharacteristics.Impedance Property

RfpmSwitchCharacteristicsImpedance Property

Gets the characteristic impedance for the channel.

Namespace:

NationalInstruments.ModularInstruments.NIRfpmSwitch

Assembly:

##### Syntax

C#

VB

```text
public double Impedance { get; }
```

```text
Public ReadOnly Property Impedance As Double
	Get
```

###### Property Value

Double

##### Exceptions

| Exception | Condition |
| --- | --- |
| ObjectDisposedException | The Impedance was accessed after the associated NIRfpmSwitch or RfpmSwitchDriverUtility object was disposed. |
| IviCDriverException | The underlying NI-RFPM Switch driver returned an error. |

##### See Also

###### Reference

RfpmSwitchCharacteristics Class

NationalInstruments.ModularInstruments.NIRfpmSwitch Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=ni-rfpm-api-ref path=ninetrfpmswitchfx40ref/html/b69fdbc6-55a8-874b-fd28-a221963a8216.htm language=enus -->
## TOPIC 00087: ninetrfpmswitchfx40ref/html/b69fdbc6-55a8-874b-fd28-a221963a8216.htm

- bundle_id: `ni-rfpm-api-ref`
- source_path: `ninetrfpmswitchfx40ref/html/b69fdbc6-55a8-874b-fd28-a221963a8216.htm`
- source_url: https://docs-be.ni.com/bundle/ni-rfpm-api-ref/raw/resource/enus/ninetrfpmswitchfx40ref/html/b69fdbc6-55a8-874b-fd28-a221963a8216.htm
- document_id: `ni-rfpm-api-ref`
- page_type: `leaf`
- content_type: ``

RfpmSwitchChannel.Name Property

RfpmSwitchChannelName Property

Gets the name of the channel as defined by the switch device.

Namespace:

NationalInstruments.ModularInstruments.NIRfpmSwitch

Assembly:

##### Syntax

C#

VB

```text
public string Name { get; }
```

```text
Public ReadOnly Property Name As String
	Get
```

###### Property Value

String

##### Exceptions

| Exception | Condition |
| --- | --- |
| ObjectDisposedException | Name was accessed after the associated NIRfpmSwitch object was disposed. |

##### See Also

###### Reference

RfpmSwitchChannel Class

NationalInstruments.ModularInstruments.NIRfpmSwitch Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=ni-rfpm-api-ref path=ninetrfpmswitchfx40ref/html/b7c61930-db02-c81e-5d6d-365dbcc6d6c9.htm language=enus -->
## TOPIC 00088: ninetrfpmswitchfx40ref/html/b7c61930-db02-c81e-5d6d-365dbcc6d6c9.htm

- bundle_id: `ni-rfpm-api-ref`
- source_path: `ninetrfpmswitchfx40ref/html/b7c61930-db02-c81e-5d6d-365dbcc6d6c9.htm`
- source_url: https://docs-be.ni.com/bundle/ni-rfpm-api-ref/raw/resource/enus/ninetrfpmswitchfx40ref/html/b7c61930-db02-c81e-5d6d-365dbcc6d6c9.htm
- document_id: `ni-rfpm-api-ref`
- page_type: `leaf`
- content_type: ``

RfpmSwitchChannel.PortType Property

RfpmSwitchChannelPortType Property

Gets port type of the channel.

Namespace:

NationalInstruments.ModularInstruments.NIRfpmSwitch

Assembly:

##### Syntax

C#

VB

```text
public string PortType { get; }
```

```text
Public ReadOnly Property PortType As String
	Get
```

###### Property Value

String

Empty

##### Exceptions

| Exception | Condition |
| --- | --- |
| ObjectDisposedException | PortType was accessed after the associated NIRfpmSwitch object was disposed. |

##### See Also

###### Reference

RfpmSwitchChannel Class

NationalInstruments.ModularInstruments.NIRfpmSwitch Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=ni-rfpm-api-ref path=ninetrfpmswitchfx40ref/html/c1902c8f-dc01-365c-27eb-edb2fdc9ac14.htm language=enus -->
## TOPIC 00089: ninetrfpmswitchfx40ref/html/c1902c8f-dc01-365c-27eb-edb2fdc9ac14.htm

- bundle_id: `ni-rfpm-api-ref`
- source_path: `ninetrfpmswitchfx40ref/html/c1902c8f-dc01-365c-27eb-edb2fdc9ac14.htm`
- source_url: https://docs-be.ni.com/bundle/ni-rfpm-api-ref/raw/resource/enus/ninetrfpmswitchfx40ref/html/c1902c8f-dc01-365c-27eb-edb2fdc9ac14.htm
- document_id: `ni-rfpm-api-ref`
- page_type: `leaf`
- content_type: ``

RfpmSwitchDriverOperation Events

RfpmSwitchDriverOperation Events

The [RfpmSwitchDriverOperation](8388d6a1-b7ce-e451-51ea-3d6c82dc36e9.htm) type exposes the following members.

##### Events

|  | Name | Description |
| --- | --- | --- |
|  | Warning | Occurs when the NI-RFPM Switch driver creates a driver warning. |

Top

##### See Also

###### Reference

RfpmSwitchDriverOperation Class

NationalInstruments.ModularInstruments.NIRfpmSwitch Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=ni-rfpm-api-ref path=ninetrfpmswitchfx40ref/html/cccbba2c-e6b6-247d-6cda-a3ccef568894.htm language=enus -->
## TOPIC 00090: ninetrfpmswitchfx40ref/html/cccbba2c-e6b6-247d-6cda-a3ccef568894.htm

- bundle_id: `ni-rfpm-api-ref`
- source_path: `ninetrfpmswitchfx40ref/html/cccbba2c-e6b6-247d-6cda-a3ccef568894.htm`
- source_url: https://docs-be.ni.com/bundle/ni-rfpm-api-ref/raw/resource/enus/ninetrfpmswitchfx40ref/html/cccbba2c-e6b6-247d-6cda-a3ccef568894.htm
- document_id: `ni-rfpm-api-ref`
- page_type: `leaf`
- content_type: ``

RfpmSwitchDriverOperation.RangeCheck Property

RfpmSwitchDriverOperationRangeCheck Property

Gets or sets a value indicating whether to validate proper values and method parameters.

Namespace:

NationalInstruments.ModularInstruments.NIRfpmSwitch

Assembly:

##### Syntax

C#

VB

```text
public bool RangeCheck { get; set; }
```

```text
Public Property RangeCheck As Boolean
	Get
	Set
```

###### Property Value

Boolean

###### Implements

##### Exceptions

| Exception | Condition |
| --- | --- |
| ObjectDisposedException | RangeCheck was accessed after the associated NIRfpmSwitch or RfpmSwitchDriverUtility object was disposed. |
| IviCDriverException | The underlying NI-RFPM Switch driver returned an error. |

##### Remarks

Range checking parameters is very useful for debugging. After you validate your program, you can set this property to 
 to disable range checking and maximize performance.

##### See Also

###### Reference

RfpmSwitchDriverOperation Class

NationalInstruments.ModularInstruments.NIRfpmSwitch Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=ni-rfpm-api-ref path=ninetrfpmswitchfx40ref/html/ce172853-d70d-49f3-2112-73a29401d11a.htm language=enus -->
## TOPIC 00091: ninetrfpmswitchfx40ref/html/ce172853-d70d-49f3-2112-73a29401d11a.htm

- bundle_id: `ni-rfpm-api-ref`
- source_path: `ninetrfpmswitchfx40ref/html/ce172853-d70d-49f3-2112-73a29401d11a.htm`
- source_url: https://docs-be.ni.com/bundle/ni-rfpm-api-ref/raw/resource/enus/ninetrfpmswitchfx40ref/html/ce172853-d70d-49f3-2112-73a29401d11a.htm
- document_id: `ni-rfpm-api-ref`
- page_type: `leaf`
- content_type: ``

RfpmSwitchPath Methods

RfpmSwitchPath Methods

The [RfpmSwitchPath](cea083a9-27c6-e932-a3b5-2a93a9e66dde.htm) type exposes the following members.

##### Methods

|  | Name | Description |
| --- | --- | --- |
|  | CanConnect | Verifies whether the switch module can create a path between channel1 and channel2. |
|  | Connect | Creates a path between channel1 and channel2. |
|  | Disconnect | Disconnects the path between two channels created using Connect(String, String) or SetPath(RfpmSwitchPathDescription). |
|  | DisconnectAll | Disconnects all existing paths. |
|  | Equals | Determines whether the specified object is equal to the current object. (Inherited from Object.) |
|  | GetConnectedPaths | Returns an array of RfpmSwitchPathDescription objects for paths that have been connected. |
|  | GetHashCode | Serves as the default hash function. (Inherited from Object.) |
|  | GetPath | Returns a RfpmSwitchPathDescription object that identifies the explicit path created with Connect(String, String) or SetPath(RfpmSwitchPathDescription). |
|  | GetSettlingTime | Queries the time to wait for the signal at the switch output to settle within the specified amplitudeSettlingAccuracy for the specified pathDescription. |
|  | GetType | Gets the Type of the current instance. (Inherited from Object.) |
|  | SetPath | Creates a path given a pathDescription. |
|  | ToString | Returns a string that represents the current object. (Inherited from Object.) |
|  | WaitForDebounce | Pauses until all created paths have settled. |

Top

##### See Also

###### Reference

RfpmSwitchPath Class

NationalInstruments.ModularInstruments.NIRfpmSwitch Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=ni-rfpm-api-ref path=ninetrfpmswitchfx40ref/html/d8929b91-2af7-e905-5608-7d76cf8e038b.htm language=enus -->
## TOPIC 00092: ninetrfpmswitchfx40ref/html/d8929b91-2af7-e905-5608-7d76cf8e038b.htm

- bundle_id: `ni-rfpm-api-ref`
- source_path: `ninetrfpmswitchfx40ref/html/d8929b91-2af7-e905-5608-7d76cf8e038b.htm`
- source_url: https://docs-be.ni.com/bundle/ni-rfpm-api-ref/raw/resource/enus/ninetrfpmswitchfx40ref/html/d8929b91-2af7-e905-5608-7d76cf8e038b.htm
- document_id: `ni-rfpm-api-ref`
- page_type: `leaf`
- content_type: ``

RfpmSwitchChannelCollection.Item Property (Int32)

RfpmSwitchChannelCollectionItem Property (Int32)

RfpmSwitchChannel

Namespace:

NationalInstruments.ModularInstruments.NIRfpmSwitch

Assembly:

##### Syntax

C#

VB

```text
public RfpmSwitchChannel this[
	int index
] { get; }
```

```text
Public ReadOnly Default Property Item ( 
	index As Integer
) As RfpmSwitchChannel
	Get
```

###### Parameters

- **index**
  - Type: SystemInt32 The index of the channel in the switch device.

###### Property Value

RfpmSwitchChannel

RfpmSwitchChannel

###### Return Value

RfpmSwitchChannel

RfpmSwitchChannel

##### Exceptions

| Exception | Condition |
| --- | --- |
| ArgumentOutOfRangeException | The index is outside the bounds. |
| ObjectDisposedException | ItemInt32 was accessed after the associated NIRfpmSwitch object was disposed. |

##### See Also

###### Reference

RfpmSwitchChannelCollection Class

Item Overload

NationalInstruments.ModularInstruments.NIRfpmSwitch Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=ni-rfpm-api-ref path=ninetrfpmswitchfx40ref/html/eb59de56-3589-7e84-ef6c-787b69df00b1.htm language=enus -->
## TOPIC 00093: ninetrfpmswitchfx40ref/html/eb59de56-3589-7e84-ef6c-787b69df00b1.htm

- bundle_id: `ni-rfpm-api-ref`
- source_path: `ninetrfpmswitchfx40ref/html/eb59de56-3589-7e84-ef6c-787b69df00b1.htm`
- source_url: https://docs-be.ni.com/bundle/ni-rfpm-api-ref/raw/resource/enus/ninetrfpmswitchfx40ref/html/eb59de56-3589-7e84-ef6c-787b69df00b1.htm
- document_id: `ni-rfpm-api-ref`
- page_type: `leaf`
- content_type: ``

RfpmSwitchDriverUtility.Disable Method

RfpmSwitchDriverUtilityDisable Method

Places the instrument in an inactive state as quickly as possible.

Namespace:

NationalInstruments.ModularInstruments.NIRfpmSwitch

Assembly:

##### Syntax

C#

VB

```text
public void Disable()
```

```text
Public Sub Disable
```

###### Implements

##### Exceptions

| Exception | Condition |
| --- | --- |
| ObjectDisposedException | Disable was called after the associated NIRfpmSwitch or RfpmSwitchDriverUtility object was disposed. |
| IviCDriverException | The underlying NI-RFPM Switch driver returned an error. |

##### Remarks

In an inactive state, an instrument has minimal or no effect on the external system to which it is connected.

##### See Also

###### Reference

RfpmSwitchDriverUtility Class

NationalInstruments.ModularInstruments.NIRfpmSwitch Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=ni-rfpm-api-ref path=rfpmcref/nirfpm_attr_autocal_receiver_scalar_calibration_enabled.html language=enus -->
## TOPIC 00094: NIRFPM_ATTR_AUTOCAL_RECEIVER_SCALAR_CALIBRATION_ENABLED

- bundle_id: `ni-rfpm-api-ref`
- source_path: `rfpmcref/nirfpm_attr_autocal_receiver_scalar_calibration_enabled.html`
- source_url: https://docs-be.ni.com/bundle/ni-rfpm-api-ref/raw/resource/enus/rfpmcref/nirfpm_attr_autocal_receiver_scalar_calibration_enabled.html
- document_id: `ni-rfpm-api-ref`
- page_type: `leaf`
- content_type: ``

NIRFPM_ATTR_AUTOCAL_RECEIVER_SCALAR_CALIBRATION_ENABLED

#### Specific Attribute

| Datatype | Access | Applies to | Coercion | High Level Functions |
| --- | --- | --- | --- | --- |
| ViBoolean | R/W | Device | None | NIRFPM_ConfigureCalibration |

#### Description

Specifies whether the autocalibration routine collects receiver scalar offsets.

This attribute does not support the mmWave subsystem.

**Default Value**: VI_TRUE

<!--NI_TOPIC bundle=ni-rfpm-api-ref path=rfpmcref/nirfpm_attr_calibration_file_vst_serial_must_match.html language=enus -->
## TOPIC 00095: NIRFPM_ATTR_CALIBRATION_FILE_VST_SERIAL_MUST_MATCH

- bundle_id: `ni-rfpm-api-ref`
- source_path: `rfpmcref/nirfpm_attr_calibration_file_vst_serial_must_match.html`
- source_url: https://docs-be.ni.com/bundle/ni-rfpm-api-ref/raw/resource/enus/rfpmcref/nirfpm_attr_calibration_file_vst_serial_must_match.html
- document_id: `ni-rfpm-api-ref`
- page_type: `leaf`
- content_type: ``

NIRFPM_ATTR_CALIBRATION_FILE_VST_SERIAL_MUST_MATCH

#### Specific Attribute

| Datatype | Access | Applies to | Coercion | High Level Functions |
| --- | --- | --- | --- | --- |
| ViBoolean | R/W | Device | None | NIRFPM_ConfigureCalibration |

#### Description

Specifies whether a calibration file will be rejected if the calibration was performed with a different VST.

This attribute does not support the mmWave subsystem.

**Default Value**: FALSE

<!--NI_TOPIC bundle=ni-rfpm-api-ref path=rfpmcref/nirfpm_attr_calibration_load_board_calibration_day.html language=enus -->
## TOPIC 00096: NIRFPM_ATTR_CALIBRATION_LOAD_BOARD_CALIBRATION_DAY

- bundle_id: `ni-rfpm-api-ref`
- source_path: `rfpmcref/nirfpm_attr_calibration_load_board_calibration_day.html`
- source_url: https://docs-be.ni.com/bundle/ni-rfpm-api-ref/raw/resource/enus/rfpmcref/nirfpm_attr_calibration_load_board_calibration_day.html
- document_id: `ni-rfpm-api-ref`
- page_type: `leaf`
- content_type: ``

NIRFPM_ATTR_CALIBRATION_LOAD_BOARD_CALIBRATION_DAY

#### Specific Attribute

| Datatype | Access | Applies to | Coercion | High Level Functions |
| --- | --- | --- | --- | --- |
| ViInt32 | RO | Device | None | None |

#### Description

Specifies the day of the last calibration for the attached calibration load board. This attribute depends on the value of the AutoCal Resource Name attribute. If the AutoCal Resource Name is an empty string and there is only one calibration load board connected, this attribute returns the calibration time of the only calibration load board. If the string is not empty or there is more than one load board, the driver will return the calibration time of the calibration load board specified by AutoCal Resource Name.

This attribute does not support the mmWave subsystem.

<!--NI_TOPIC bundle=ni-rfpm-api-ref path=rfpmcref/nirfpm_attr_deembedding_enabled.html language=enus -->
## TOPIC 00097: NIRFPM_ATTR_DEEMBEDDING_ENABLED

- bundle_id: `ni-rfpm-api-ref`
- source_path: `rfpmcref/nirfpm_attr_deembedding_enabled.html`
- source_url: https://docs-be.ni.com/bundle/ni-rfpm-api-ref/raw/resource/enus/rfpmcref/nirfpm_attr_deembedding_enabled.html
- document_id: `ni-rfpm-api-ref`
- page_type: `leaf`
- content_type: ``

NIRFPM_ATTR_DEEMBEDDING_ENABLED

#### Specific Attribute

| Datatype | Access | Applies to | Coercion | High Level Functions |
| --- | --- | --- | --- | --- |
| ViBoolean | R/W | Device | None | NIRFPM_ConfigureDeembedding |

#### Description

Specifies whether de-embedding is applied to the calibration data and the measurement data.

**Default Value**: VI_FALSE

<!--NI_TOPIC bundle=ni-rfpm-api-ref path=rfpmcref/nirfpm_attr_driver_state.html language=enus -->
## TOPIC 00098: NIRFPM_ATTR_DRIVER_STATE

- bundle_id: `ni-rfpm-api-ref`
- source_path: `rfpmcref/nirfpm_attr_driver_state.html`
- source_url: https://docs-be.ni.com/bundle/ni-rfpm-api-ref/raw/resource/enus/rfpmcref/nirfpm_attr_driver_state.html
- document_id: `ni-rfpm-api-ref`
- page_type: `leaf`
- content_type: ``

NIRFPM_ATTR_DRIVER_STATE

#### Specific Attribute

| Datatype | Access | Applies to | Coercion | High Level Functions |
| --- | --- | --- | --- | --- |
| ViString | RO | Device | None | None |

#### Description

Indicates current driver state.

This attribute does not support the mmWave subsystem.

**Defined Values**:

| Configuration | Driver is ready for initial measurement. |
| --- | --- |
| Measuring | Driver is currently taking a measurement. |
| Measurement Done | Driver has completed the measurement. |
| Calibration Configuration | Driver is ready to perform a calibration. |
| Calibrating | Driver is currently calibrating. |

<!--NI_TOPIC bundle=ni-rfpm-api-ref path=rfpmcref/nirfpm_attr_external_settling_time.html language=enus -->
## TOPIC 00099: NIRFPM_ATTR_EXTERNAL_SETTLING_TIME

- bundle_id: `ni-rfpm-api-ref`
- source_path: `rfpmcref/nirfpm_attr_external_settling_time.html`
- source_url: https://docs-be.ni.com/bundle/ni-rfpm-api-ref/raw/resource/enus/rfpmcref/nirfpm_attr_external_settling_time.html
- document_id: `ni-rfpm-api-ref`
- page_type: `leaf`
- content_type: ``

NIRFPM_ATTR_EXTERNAL_SETTLING_TIME

#### Specific Attribute

| Datatype | Access | Applies to | Coercion | High Level Functions |
| --- | --- | --- | --- | --- |
| ViReal64 | R/W | Device | None | None |

#### Description

Specifies the amount of time, in seconds, to wait for external settling after tuning the source at each measurement point for each driving port.

**Default Value**: 0

<!--NI_TOPIC bundle=ni-rfpm-api-ref path=rfpmcref/nirfpm_attr_interpolation_enabled.html language=enus -->
## TOPIC 00100: NIRFPM_ATTR_INTERPOLATION_ENABLED

- bundle_id: `ni-rfpm-api-ref`
- source_path: `rfpmcref/nirfpm_attr_interpolation_enabled.html`
- source_url: https://docs-be.ni.com/bundle/ni-rfpm-api-ref/raw/resource/enus/rfpmcref/nirfpm_attr_interpolation_enabled.html
- document_id: `ni-rfpm-api-ref`
- page_type: `leaf`
- content_type: ``

NIRFPM_ATTR_INTERPOLATION_ENABLED

#### Specific Attribute

| Datatype | Access | Applies to | Coercion | High Level Functions |
| --- | --- | --- | --- | --- |
| ViBoolean | R/W | Device | None | None |

#### Description

Specifies if interpolation is used when fetching source and receiver offsets by parameters.

This attribute does not support the mmWave subsystem.

**Default Value**: VI_FALSE

<!--NI_TOPIC bundle=ni-rfpm-api-ref path=rfpmcref/nirfpm_attr_source_power_correction_enabled.html language=enus -->
## TOPIC 00101: NIRFPM_ATTR_SOURCE_POWER_CORRECTION_ENABLED

- bundle_id: `ni-rfpm-api-ref`
- source_path: `rfpmcref/nirfpm_attr_source_power_correction_enabled.html`
- source_url: https://docs-be.ni.com/bundle/ni-rfpm-api-ref/raw/resource/enus/rfpmcref/nirfpm_attr_source_power_correction_enabled.html
- document_id: `ni-rfpm-api-ref`
- page_type: `leaf`
- content_type: ``

NIRFPM_ATTR_SOURCE_POWER_CORRECTION_ENABLED

#### Specific Attribute

| Datatype | Access | Applies to | Coercion | High Level Functions |
| --- | --- | --- | --- | --- |
| ViBoolean | R/W | Device | None | None |

#### Description

Specifies whether the source output power is corrected using calibrated source offsets during S-parameter measurements. This attribute also specifies whether the source scalar offsets are calibrated values or factory values.

This attribute does not support the mmWave subsystem.

**Default Value**: VI_TRUE

<!--NI_TOPIC bundle=ni-rfpm-api-ref path=rfpmcref/nirfpm_attr_vector_correction_enabled.html language=enus -->
## TOPIC 00102: NIRFPM_ATTR_VECTOR_CORRECTION_ENABLED

- bundle_id: `ni-rfpm-api-ref`
- source_path: `rfpmcref/nirfpm_attr_vector_correction_enabled.html`
- source_url: https://docs-be.ni.com/bundle/ni-rfpm-api-ref/raw/resource/enus/rfpmcref/nirfpm_attr_vector_correction_enabled.html
- document_id: `ni-rfpm-api-ref`
- page_type: `leaf`
- content_type: ``

NIRFPM_ATTR_VECTOR_CORRECTION_ENABLED

#### Specific Attribute

| Datatype | Access | Applies to | Coercion | High Level Functions |
| --- | --- | --- | --- | --- |
| ViBoolean | R/W | Device | None | None |

#### Description

Specifies whether the vector error offsets are applied to the measurement data.

**Default Value**: VI_TRUE

<!--NI_TOPIC bundle=ni-rfpm-api-ref path=rfpmhelp/labview.html language=enus -->
## TOPIC 00103: NI-RFPM LabVIEW Reference

- bundle_id: `ni-rfpm-api-ref`
- source_path: `rfpmhelp/labview.html`
- source_url: https://docs-be.ni.com/bundle/ni-rfpm-api-ref/raw/resource/enus/rfpmhelp/labview.html
- document_id: `ni-rfpm-api-ref`
- page_type: `leaf`
- content_type: ``

NI-RFPM LabVIEW Reference

This book contains information about NI-RFPM LabVIEW [VIs](../rfpmviref/ni-rfpm_pal.html) and [properties](../rfpmpropref/cnirfpm.html).

<!--NI_TOPIC bundle=ni-rfpm-api-ref path=rfpmhelp/ni-rfpm_switch_pal.html language=enus -->
## TOPIC 00104: NI-RFPM Switch VIs

- bundle_id: `ni-rfpm-api-ref`
- source_path: `rfpmhelp/ni-rfpm_switch_pal.html`
- source_url: https://docs-be.ni.com/bundle/ni-rfpm-api-ref/raw/resource/enus/rfpmhelp/ni-rfpm_switch_pal.html
- document_id: `ni-rfpm-api-ref`
- page_type: `leaf`
- content_type: ``

NI-RFPM Switch

Owning Palette:

NI-RFPM Switch VIs

Installed With:

Use the NI-RFPM Switch VIs to control measurement operations with your STS device.

| Palette Object | Description |
| --- | --- |
| niRFPMSwitch Read Connected Paths | Queries which switch paths are currently connected, and returns a string listing switch paths. An example output is "TX_1->port1 & RX_GAIN_1->port2". |
| niRFPMSwitch Reset Device | Resets all attributes and devices, including NI-RFSA and NI-RFSG sessions, to their default states, and clears a latched interlock signal. |

<!--NI_TOPIC bundle=ni-rfpm-api-ref path=rfpmhelp/nirfpmswitch_attr_device_temperature.html language=enus -->
## TOPIC 00105: NIRFPMSWITCH_ATTR_DEVICE_TEMPERATURE

- bundle_id: `ni-rfpm-api-ref`
- source_path: `rfpmhelp/nirfpmswitch_attr_device_temperature.html`
- source_url: https://docs-be.ni.com/bundle/ni-rfpm-api-ref/raw/resource/enus/rfpmhelp/nirfpmswitch_attr_device_temperature.html
- document_id: `ni-rfpm-api-ref`
- page_type: `leaf`
- content_type: ``

NIRFPMSWITCH_ATTR_DEVICE_TEMPERATURE

#### Specific Attribute

| Datatype | Access | Applies to | Coercion |
| --- | --- | --- | --- |
| ViReal64 | RO | Device | None |

#### Description

Specifies the temperature of the device in Celsius.

This attribute does not support the mmWave subsystem.

<!--NI_TOPIC bundle=ni-rfpm-api-ref path=rfpmhelp/nirfpmswitch_resetdevice.html language=enus -->
## TOPIC 00106: niRFPMSwitch_ResetDevice

- bundle_id: `ni-rfpm-api-ref`
- source_path: `rfpmhelp/nirfpmswitch_resetdevice.html`
- source_url: https://docs-be.ni.com/bundle/ni-rfpm-api-ref/raw/resource/enus/rfpmhelp/nirfpmswitch_resetdevice.html
- document_id: `ni-rfpm-api-ref`
- page_type: `leaf`
- content_type: ``

niRFPMSwitch_ResetDevice

niRFPMSwitch_ResetDevice (ViSession vi);

#### Purpose

Resets all attributes to their default states, and clears a latched interlock signal.

This function does not support the mmWave subsystem.

#### Parameters

| Input |  |  |
| --- | --- | --- |
| Name | Type | Description |
| vi | ViSession | Identifies your RFPM Switch session. |

#### Return Value

| Name | Type | Description |
| --- | --- | --- |
| returnValue | ViStatus | Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an NI-RFPM Switch function to determine if an error has occurred. To obtain a text description of the status code and additional information about the error condition, call the niRFPMSwitch_GetError function. To clear the error information from NI-RFPM Switch, call the niRFPMSwitch_ClearError function. The general meaning of the status code is as follows: Value Meaning 0 Success Positive Values Warnings Negative Values Errors |
| Value | Meaning |  |
| 0 | Success |  |
| Positive Values | Warnings |  |
| Negative Values | Errors |  |
|  |  |  |

<!--NI_TOPIC bundle=ni-rfpm-api-ref path=rfpmhelp/rfpm_switch_labview.html language=enus -->
## TOPIC 00107: NI-RFPM Switch LabVIEW Reference

- bundle_id: `ni-rfpm-api-ref`
- source_path: `rfpmhelp/rfpm_switch_labview.html`
- source_url: https://docs-be.ni.com/bundle/ni-rfpm-api-ref/raw/resource/enus/rfpmhelp/rfpm_switch_labview.html
- document_id: `ni-rfpm-api-ref`
- page_type: `leaf`
- content_type: ``

NI-RFPM Switch LabVIEW Reference

This book contains information about NI-RFPM Switch LabVIEW [VIs](ni-rfpm_switch_pal.html) and [properties](../rfpmswitchpropref/rfpmswitch.html).

<!--NI_TOPIC bundle=ni-rfpm-api-ref path=rfpmhelp/rfpmswitch_pal.html language=enus -->
## TOPIC 00108: NI-RFPM Switch Reference

- bundle_id: `ni-rfpm-api-ref`
- source_path: `rfpmhelp/rfpmswitch_pal.html`
- source_url: https://docs-be.ni.com/bundle/ni-rfpm-api-ref/raw/resource/enus/rfpmhelp/rfpmswitch_pal.html
- document_id: `ni-rfpm-api-ref`
- page_type: `leaf`
- content_type: ``

NI-RFPM Switch Reference

This book contains reference information about the NI-RFPM Switch VIs, properties, functions, and attributes.

<!--NI_TOPIC bundle=ni-rfpm-api-ref path=rfpmpropref/attr118c6e.html language=enus -->
## TOPIC 00109: Measurement:Reference Level Port Extension Selected Table Property

- bundle_id: `ni-rfpm-api-ref`
- source_path: `rfpmpropref/attr118c6e.html`
- source_url: https://docs-be.ni.com/bundle/ni-rfpm-api-ref/raw/resource/enus/rfpmpropref/attr118c6e.html
- document_id: `ni-rfpm-api-ref`
- page_type: `leaf`
- content_type: ``

Measurement:Reference Level Port Extension Selected Table Property

**Short Name:**Reference Level Port Extension Selected Table

Property of [niRFPM](cnirfpm.html)

Specifies reference level port extension table for the active channel.

This property does not support the RF subsystem.

**Default Value**: ****

#### Remarks

The following table lists the characteristics of this property.

| Datatype |  |
| --- | --- |
| Permissions | Read/Write |
| High-level VIs | N/A |
| Channel-based | No |
| Port-based | No |
| Device-based | No |
| Resettable | No |

<!--NI_TOPIC bundle=ni-rfpm-api-ref path=rfpmpropref/cnirfpm.html language=enus -->
## TOPIC 00110: niRFPM Properties

- bundle_id: `ni-rfpm-api-ref`
- source_path: `rfpmpropref/cnirfpm.html`
- source_url: https://docs-be.ni.com/bundle/ni-rfpm-api-ref/raw/resource/enus/rfpmpropref/cnirfpm.html
- document_id: `ni-rfpm-api-ref`
- page_type: `leaf`
- content_type: ``

niRFPM Properties

May 2021 375624E-01

Use the NI-RFPM properties to access advanced configuration options for NI-RFPM applications.

| Property | Description |
| --- | --- |
| Active Channel | Specifies the port name used to access all subsequent properties in this instance of the property node. If the property you want to use is port-based, you must first select this property and then pass the name of the specific port. If the property you specify is not port-based, pass an empty string, or omit setting this property. Details |
| Measurement:Vector Correction Enabled | Specifies whether the vector error correction is applied to the measurement data. Details |
| Measurement:De-embedding Enabled | Specifies whether de-embedding is applied to the measurement and calibration data. Details |
| Measurement:De-embedding S2P Path | Specifies the path to the S2P file that characterizes the de-embedding network for the given port. Details |
| Measurement:De-embedding S2P Orientation | Specifies whether the de-embedding network in the S2P file is connected with port 1 towards the DUT or port 2 towards the DUT. Details |
| Measurement:Reference Level Port Extension Selected Table | Specifies reference level port extension table for the active channel. This property does not support the RF subsystem. Details |
| Measurement:Reference Clock Source | Specifies the source to use for the Reference Clock. Details |
| Measurement:Interpolation Enabled | Specifies if interpolation across frequency is used when fetching source and receiver offsets by parameters. This property does not support the mmWave subsystem. Details |
| Measurement:Maximum Frequency Span for Interpolation | Specifies the maximum span between two adjacent calibration frequencies for which interpolation will be performed, expressed in Hz. This property does not support the mmWave subsystem. Details |
| Measurement:External Settling Time | Specifies the time to delay the S-parameter measurement after the source is modified to allow for external settling. This value is expressed in seconds. Details |
| Measurement:Reference Level Coercion Enabled | Specifies whether reference level is coerced to the next highest reference level with a matching frequency when fetching receiver offset by parameters. This property does not support the mmWave subsystem. Details |
| Measurement:Maximum Reference Level Coercion | Specifies the maximum difference allowed between the requested reference level and the matching reference level when reference level coercion is enabled, expressed in dBm. This property does not support the mmWave subsystem. Details |
| Measurement:Power Level Coercion Method | Specifies if and how power level is coerced when fetching the source offset. Coercion can either be to the nearest calibrated power level with a matching frequency, or to a lower power level only. This property does not support the mmWave subsystem. Details |
| Measurement:Maximum Power Level Coercion | Specifies the maximum difference allowed between the requested power level and the matching power level when power level coercion is enabled, expressed in dBm. This property does not support the mmWave subsystem. Details |
| Measurement:Source Amplitude Settling | Specifies the source amplitude settling accuracy for vector and scalar measurements in decibels. This property does not support the mmWave subsystem. Details |
| Measurement:Receiver Amplitude Settling | Specifies the receiver amplitude settling accuracy for scalar measurements in decibels. This property does not support the mmWave subsystem. Details |
| Measurement:Vector Receiver Amplitude Settling | Specifies the receiver amplitude settling accuracy for vector measurements in decibels. This property does not support the mmWave subsystem. Details |
| Calibration:Source Power Correction Enabled | Specifies whether the source output power offsets use user-calibrated values or factory calibration values. This property also specifies whether the source output power offsets are applied during S-parameter measurements. This property does not support the mmWave subsystem. Details |
| Calibration:Receiver Power Correction Enabled | Specifies whether the receiver input power offsets use user-calibrated values or factory calibration values. This property does not support the mmWave subsystem. Details |
| Calibration:AutoCal Resource Name | Specifies the resource name of the NI Automatic RF Calibration Module used for automatic calibration. This property does not support the mmWave subsystem. Details |
| Calibration:Power Meter Resource Name | Specifies the name of the power meter resource that an RF multiport calibration module uses. To read this attribute, the RF multiport calibration module must be connected. If there is only one RF multiport calibration module and the AutoCal Resource Name property is an empty string, the driver automatically detects the RF multiport calibration module to get the power meter resource name from. If there is more than one NI Automatic RF Calibration Module or the string is not empty, the driver finds the power meter resource name from the RF multiport calibration module specified by the AutoCal Resource Name property. This property does not report a valid resource name until after the niRFPM Init User Calibration VI runs. This property does not support the mmWave subsystem. Details |
| Calibration:AutoCal Absolute Vector Calibration Enabled | Specifies whether the automatic calibration routine collects absolute vector error coefficients or relative vector error coefficients. This property does not support the mmWave subsystem. Details |
| Calibration:AutoCal Source Scalar Calibration Enabled | Specifies whether the automatic calibration routine collects source scalar offsets. This property does not support the mmWave subsystem. Details |
| Calibration:AutoCal Receiver Scalar Calibration Enabled | Specifies whether the automatic calibration routine collects receiver scalar offsets. This property does not support the mmWave subsystem. Details |
| Calibration Load Board Calibration Information:Calibration Load Board Calibration Year | Returns the year of the last time the RF multiport calibration module was calibrated. This property does not support the mmWave subsystem. Details |
| Calibration Load Board Calibration Information:Calibration Load Board Calibration Month | Returns the month of the last time the RF multiport calibration module was calibrated. The returned value is expressed as an integer. For example, December is represented as 12. This property does not support the mmWave subsystem. Details |
| Calibration Load Board Calibration Information:Calibration Load Board Calibration Day | Returns the day of the last time the RF multiport calibration module was calibrated. This property does not support the mmWave subsystem. Details |
| Calibration Load Board Calibration Information:Calibration Load Board Calibration Hour | Returns the hour of the last time the RF multiport calibration module was calibrated. The time is expressed in 24-hour clock format according to your local time zone. For example, if the device was calibrated at 2:00 PM, this function returns 14 as the value of this property. This property does not support the mmWave subsystem. Details |
| Calibration Load Board Calibration Information:Calibration Load Board Calibration Minute | Returns the minute of the last time the RF multiport calibration module was calibrated. This property does not support the mmWave subsystem. Details |
| Calibration Load Board Calibration Information:Calibration Load Board Calibration Second | Returns the second of the last time the RF multiport calibration module was calibrated. This property does not support the mmWave subsystem. Details |
| Calibration Load Board Calibration Information:Calibration Load Board Calibration Temperature | Returns the temperature of the RF multiport calibration module for the last time the RF multiport calibration module was calibrated. This property does not support the mmWave subsystem. Details |
| Calibration Load Board Calibration Information:Calibration Load Board Calibration Revision | Returns the calibration revision used last time the RF multiport calibration module was calibrated. This property does not support the mmWave subsystem. Details |
| Calibration:Calibration Load Board Model Number | Returns the model number of the calibration load board. This property does not support the mmWave subsystem. Details |
| Calibration:Calibration Load Board Serial Number | Returns the serial number of the calibration load board. This property does not support the mmWave subsystem. Details |
| Driver State | Indicates the current state of the driver. Details |
| Calibration:Calibration File VST Serial Must Match | Specifies whether a calibration file will be rejected if the calibration was performed with a different VST. This property does not support the mmWave subsystem. Details |
| Calibration:Skip Self Calibration Timestamp Check | Specifies whether to skip validation of self calibration timestamp and vector calibration timestamp. This property does not support the RF subsystem. Details |

<!--NI_TOPIC bundle=ni-rfpm-api-ref path=rfpmpropref/pnirfpm_activechannel.html language=enus -->
## TOPIC 00111: Active Channel Property

- bundle_id: `ni-rfpm-api-ref`
- source_path: `rfpmpropref/pnirfpm_activechannel.html`
- source_url: https://docs-be.ni.com/bundle/ni-rfpm-api-ref/raw/resource/enus/rfpmpropref/pnirfpm_activechannel.html
- document_id: `ni-rfpm-api-ref`
- page_type: `leaf`
- content_type: ``

Active Channel Property

**Short Name:**Active Channel

Property of [niRFPM](cnirfpm.html)

Specifies the port name used to access all subsequent properties in this instance of the property node. If the property you want to use is port-based, you must first select this property and then pass the name of the specific port. If the property you specify is not port-based, pass an empty string, or omit setting this property.

The default value is "". For more information about port-based properties, refer to [Using Properties and Attributes with NI-RFPM](../rfpmhelp/attributes.html).

#### Remarks

The following table lists the characteristics of this property.

| Datatype |  |
| --- | --- |
| Permissions | Write Only |
| High-level VIs | N/A |
| Channel-based | No |
| Port-based | No |
| Device-based | No |
| Resettable | No |

<!--NI_TOPIC bundle=ni-rfpm-api-ref path=rfpmpropref/pnirfpm_autocalabsolutevectorcalibrationenabled.html language=enus -->
## TOPIC 00112: Calibration:AutoCal Absolute Vector Calibration Enabled Property

- bundle_id: `ni-rfpm-api-ref`
- source_path: `rfpmpropref/pnirfpm_autocalabsolutevectorcalibrationenabled.html`
- source_url: https://docs-be.ni.com/bundle/ni-rfpm-api-ref/raw/resource/enus/rfpmpropref/pnirfpm_autocalabsolutevectorcalibrationenabled.html
- document_id: `ni-rfpm-api-ref`
- page_type: `leaf`
- content_type: ``

Calibration:AutoCal Absolute Vector Calibration Enabled Property

**Short Name:**AutoCal Absolute Vector Calibration Enabled

Property of [niRFPM](cnirfpm.html)

Specifies whether the automatic calibration routine collects absolute vector error coefficients or relative vector error coefficients.

This property does not support the mmWave subsystem.

| TRUE | Absolute vector offsets are collected. |
| --- | --- |
| FALSE | Relative vector offsets are collected. |

**Default Value**: TRUE

#### Remarks

The following table lists the characteristics of this property.

| Datatype |  |
| --- | --- |
| Permissions | Read/Write |
| High-level VIs | NI-RFPM Configure Calibration |
| Channel-based | No |
| Port-based | No |
| Device-based | Yes |
| Resettable | No |

<!--NI_TOPIC bundle=ni-rfpm-api-ref path=rfpmpropref/pnirfpm_autocalreceiverscalarcalibrationenabled.html language=enus -->
## TOPIC 00113: Calibration:AutoCal Receiver Scalar Calibration Enabled Property

- bundle_id: `ni-rfpm-api-ref`
- source_path: `rfpmpropref/pnirfpm_autocalreceiverscalarcalibrationenabled.html`
- source_url: https://docs-be.ni.com/bundle/ni-rfpm-api-ref/raw/resource/enus/rfpmpropref/pnirfpm_autocalreceiverscalarcalibrationenabled.html
- document_id: `ni-rfpm-api-ref`
- page_type: `leaf`
- content_type: ``

Calibration:AutoCal Receiver Scalar Calibration Enabled Property

**Short Name:**AutoCal Receiver Scalar Calibration Enabled

Property of [niRFPM](cnirfpm.html)

Specifies whether the automatic calibration routine collects receiver scalar offsets.

This property does not support the mmWave subsystem.

**Default Value**: TRUE

#### Remarks

The following table lists the characteristics of this property.

| Datatype |  |
| --- | --- |
| Permissions | Read/Write |
| High-level VIs | NI-RFPM Configure Calibration |
| Channel-based | No |
| Port-based | No |
| Device-based | Yes |
| Resettable | No |

<!--NI_TOPIC bundle=ni-rfpm-api-ref path=rfpmpropref/pnirfpm_autocalresourcename.html language=enus -->
## TOPIC 00114: Calibration:AutoCal Resource Name Property

- bundle_id: `ni-rfpm-api-ref`
- source_path: `rfpmpropref/pnirfpm_autocalresourcename.html`
- source_url: https://docs-be.ni.com/bundle/ni-rfpm-api-ref/raw/resource/enus/rfpmpropref/pnirfpm_autocalresourcename.html
- document_id: `ni-rfpm-api-ref`
- page_type: `leaf`
- content_type: ``

Calibration:AutoCal Resource Name Property

**Short Name:**AutoCal Resource Name

Property of [niRFPM](cnirfpm.html)

Specifies the resource name of the NI Automatic RF Calibration Module used for automatic calibration.

This property does not support the mmWave subsystem.

Typically, this is the resource name of the NI RF multiport calibration module. If only one calibration device is connected to the system and this property is set to an empty string, calling the niRFPM Init User Calibration VI automatically selects the calibration device.

**Default Value**: **""** (empty string)

#### Remarks

The following table lists the characteristics of this property.

| Datatype |  |
| --- | --- |
| Permissions | Read/Write |
| High-level VIs | NI-RFPM Configure Calibration |
| Channel-based | No |
| Port-based | No |
| Device-based | Yes |
| Resettable | No |

<!--NI_TOPIC bundle=ni-rfpm-api-ref path=rfpmpropref/pnirfpm_autocalsourcescalarcalibrationenabled.html language=enus -->
## TOPIC 00115: Calibration:AutoCal Source Scalar Calibration Enabled Property

- bundle_id: `ni-rfpm-api-ref`
- source_path: `rfpmpropref/pnirfpm_autocalsourcescalarcalibrationenabled.html`
- source_url: https://docs-be.ni.com/bundle/ni-rfpm-api-ref/raw/resource/enus/rfpmpropref/pnirfpm_autocalsourcescalarcalibrationenabled.html
- document_id: `ni-rfpm-api-ref`
- page_type: `leaf`
- content_type: ``

Calibration:AutoCal Source Scalar Calibration Enabled Property

**Short Name:**AutoCal Source Scalar Calibration Enabled

Property of [niRFPM](cnirfpm.html)

Specifies whether the automatic calibration routine collects source scalar offsets.

This property does not support the mmWave subsystem.

**Default Value**: TRUE

#### Remarks

The following table lists the characteristics of this property.

| Datatype |  |
| --- | --- |
| Permissions | Read/Write |
| High-level VIs | NI-RFPM Configure Calibration |
| Channel-based | No |
| Port-based | No |
| Device-based | Yes |
| Resettable | No |

<!--NI_TOPIC bundle=ni-rfpm-api-ref path=rfpmpropref/pnirfpm_calibrationfilevstserialmustmatch.html language=enus -->
## TOPIC 00116: Calibration:Calibration File VST Serial Must Match Property

- bundle_id: `ni-rfpm-api-ref`
- source_path: `rfpmpropref/pnirfpm_calibrationfilevstserialmustmatch.html`
- source_url: https://docs-be.ni.com/bundle/ni-rfpm-api-ref/raw/resource/enus/rfpmpropref/pnirfpm_calibrationfilevstserialmustmatch.html
- document_id: `ni-rfpm-api-ref`
- page_type: `leaf`
- content_type: ``

Calibration:Calibration File VST Serial Must Match Property

**Short Name:**Calibration File VST Serial Must Match

Property of [niRFPM](cnirfpm.html)

Specifies whether a calibration file will be rejected if the calibration was performed with a different VST.

This property does not support the mmWave subsystem.

**Default Value**: FALSE

#### Remarks

The following table lists the characteristics of this property.

| Datatype |  |
| --- | --- |
| Permissions | Read/Write |
| High-level VIs | N/A |
| Channel-based | No |
| Port-based | No |
| Device-based | No |
| Resettable | No |

<!--NI_TOPIC bundle=ni-rfpm-api-ref path=rfpmpropref/pnirfpm_calibrationloadboardcalibrationday.html language=enus -->
## TOPIC 00117: Calibration Load Board Calibration Information:Calibration Load Board Calibration Day Property

- bundle_id: `ni-rfpm-api-ref`
- source_path: `rfpmpropref/pnirfpm_calibrationloadboardcalibrationday.html`
- source_url: https://docs-be.ni.com/bundle/ni-rfpm-api-ref/raw/resource/enus/rfpmpropref/pnirfpm_calibrationloadboardcalibrationday.html
- document_id: `ni-rfpm-api-ref`
- page_type: `leaf`
- content_type: ``

Calibration Load Board Calibration Information:Calibration Load Board Calibration Day Property

**Short Name:**Calibration Load Board Calibration Day

Property of [niRFPM](cnirfpm.html)

Returns the day of the last time the RF multiport calibration module was calibrated.

This property does not support the mmWave subsystem.

#### Remarks

The following table lists the characteristics of this property.

| Datatype |  |
| --- | --- |
| Permissions | Read Only |
| High-level VIs | N/A |
| Channel-based | No |
| Port-based | No |
| Device-based | Yes |
| Resettable | No |

<!--NI_TOPIC bundle=ni-rfpm-api-ref path=rfpmpropref/pnirfpm_calibrationloadboardcalibrationhour.html language=enus -->
## TOPIC 00118: Calibration Load Board Calibration Information:Calibration Load Board Calibration Hour Property

- bundle_id: `ni-rfpm-api-ref`
- source_path: `rfpmpropref/pnirfpm_calibrationloadboardcalibrationhour.html`
- source_url: https://docs-be.ni.com/bundle/ni-rfpm-api-ref/raw/resource/enus/rfpmpropref/pnirfpm_calibrationloadboardcalibrationhour.html
- document_id: `ni-rfpm-api-ref`
- page_type: `leaf`
- content_type: ``

Calibration Load Board Calibration Information:Calibration Load Board Calibration Hour Property

**Short Name:**Calibration Load Board Calibration Hour

Property of [niRFPM](cnirfpm.html)

Returns the hour of the last time the RF multiport calibration module was calibrated. The time is expressed in 24-hour clock format according to your local time zone. For example, if the device was calibrated at 2:00 PM, this function returns 14 as the value of this property.

This property does not support the mmWave subsystem.

#### Remarks

The following table lists the characteristics of this property.

| Datatype |  |
| --- | --- |
| Permissions | Read Only |
| High-level VIs | N/A |
| Channel-based | No |
| Port-based | No |
| Device-based | Yes |
| Resettable | No |

<!--NI_TOPIC bundle=ni-rfpm-api-ref path=rfpmpropref/pnirfpm_calibrationloadboardcalibrationminute.html language=enus -->
## TOPIC 00119: Calibration Load Board Calibration Information:Calibration Load Board Calibration Minute Property

- bundle_id: `ni-rfpm-api-ref`
- source_path: `rfpmpropref/pnirfpm_calibrationloadboardcalibrationminute.html`
- source_url: https://docs-be.ni.com/bundle/ni-rfpm-api-ref/raw/resource/enus/rfpmpropref/pnirfpm_calibrationloadboardcalibrationminute.html
- document_id: `ni-rfpm-api-ref`
- page_type: `leaf`
- content_type: ``

Calibration Load Board Calibration Information:Calibration Load Board Calibration Minute Property

**Short Name:**Calibration Load Board Calibration Minute

Property of [niRFPM](cnirfpm.html)

Returns the minute of the last time the RF multiport calibration module was calibrated.

This property does not support the mmWave subsystem.

#### Remarks

The following table lists the characteristics of this property.

| Datatype |  |
| --- | --- |
| Permissions | Read Only |
| High-level VIs | N/A |
| Channel-based | No |
| Port-based | No |
| Device-based | Yes |
| Resettable | No |

<!--NI_TOPIC bundle=ni-rfpm-api-ref path=rfpmpropref/pnirfpm_calibrationloadboardcalibrationmonth.html language=enus -->
## TOPIC 00120: Calibration Load Board Calibration Information:Calibration Load Board Calibration Month Property

- bundle_id: `ni-rfpm-api-ref`
- source_path: `rfpmpropref/pnirfpm_calibrationloadboardcalibrationmonth.html`
- source_url: https://docs-be.ni.com/bundle/ni-rfpm-api-ref/raw/resource/enus/rfpmpropref/pnirfpm_calibrationloadboardcalibrationmonth.html
- document_id: `ni-rfpm-api-ref`
- page_type: `leaf`
- content_type: ``

Calibration Load Board Calibration Information:Calibration Load Board Calibration Month Property

**Short Name:**Calibration Load Board Calibration Month

Property of [niRFPM](cnirfpm.html)

Returns the month of the last time the RF multiport calibration module was calibrated. The returned value is expressed as an integer. For example, December is represented as 12.

This property does not support the mmWave subsystem.

#### Remarks

The following table lists the characteristics of this property.

| Datatype |  |
| --- | --- |
| Permissions | Read Only |
| High-level VIs | N/A |
| Channel-based | No |
| Port-based | No |
| Device-based | Yes |
| Resettable | No |

<!--NI_TOPIC bundle=ni-rfpm-api-ref path=rfpmpropref/pnirfpm_calibrationloadboardcalibrationrevision.html language=enus -->
## TOPIC 00121: Calibration Load Board Calibration Information:Calibration Load Board Calibration Revision Property

- bundle_id: `ni-rfpm-api-ref`
- source_path: `rfpmpropref/pnirfpm_calibrationloadboardcalibrationrevision.html`
- source_url: https://docs-be.ni.com/bundle/ni-rfpm-api-ref/raw/resource/enus/rfpmpropref/pnirfpm_calibrationloadboardcalibrationrevision.html
- document_id: `ni-rfpm-api-ref`
- page_type: `leaf`
- content_type: ``

Calibration Load Board Calibration Information:Calibration Load Board Calibration Revision Property

**Short Name:**Calibration Load Board Calibration Revision

Property of [niRFPM](cnirfpm.html)

Returns the calibration revision used last time the RF multiport calibration module was calibrated.

This property does not support the mmWave subsystem.

#### Remarks

The following table lists the characteristics of this property.

| Datatype |  |
| --- | --- |
| Permissions | Read Only |
| High-level VIs | N/A |
| Channel-based | No |
| Port-based | No |
| Device-based | No |
| Resettable | No |

<!--NI_TOPIC bundle=ni-rfpm-api-ref path=rfpmpropref/pnirfpm_calibrationloadboardcalibrationsecond.html language=enus -->
## TOPIC 00122: Calibration Load Board Calibration Information:Calibration Load Board Calibration Second Property

- bundle_id: `ni-rfpm-api-ref`
- source_path: `rfpmpropref/pnirfpm_calibrationloadboardcalibrationsecond.html`
- source_url: https://docs-be.ni.com/bundle/ni-rfpm-api-ref/raw/resource/enus/rfpmpropref/pnirfpm_calibrationloadboardcalibrationsecond.html
- document_id: `ni-rfpm-api-ref`
- page_type: `leaf`
- content_type: ``

Calibration Load Board Calibration Information:Calibration Load Board Calibration Second Property

**Short Name:**Calibration Load Board Calibration Second

Property of [niRFPM](cnirfpm.html)

Returns the second of the last time the RF multiport calibration module was calibrated.

This property does not support the mmWave subsystem.

#### Remarks

The following table lists the characteristics of this property.

| Datatype |  |
| --- | --- |
| Permissions | Read Only |
| High-level VIs | N/A |
| Channel-based | No |
| Port-based | No |
| Device-based | Yes |
| Resettable | No |

<!--NI_TOPIC bundle=ni-rfpm-api-ref path=rfpmpropref/pnirfpm_calibrationloadboardcalibrationtemperature.html language=enus -->
## TOPIC 00123: Calibration Load Board Calibration Information:Calibration Load Board Calibration Temperature Property

- bundle_id: `ni-rfpm-api-ref`
- source_path: `rfpmpropref/pnirfpm_calibrationloadboardcalibrationtemperature.html`
- source_url: https://docs-be.ni.com/bundle/ni-rfpm-api-ref/raw/resource/enus/rfpmpropref/pnirfpm_calibrationloadboardcalibrationtemperature.html
- document_id: `ni-rfpm-api-ref`
- page_type: `leaf`
- content_type: ``

Calibration Load Board Calibration Information:Calibration Load Board Calibration Temperature Property

**Short Name:**Calibration Load Board Calibration Temperature

Property of [niRFPM](cnirfpm.html)

Returns the temperature of the RF multiport calibration module for the last time the RF multiport calibration module was calibrated.

This property does not support the mmWave subsystem.

**Units**: degrees Celsius

#### Remarks

The following table lists the characteristics of this property.

| Datatype |  |
| --- | --- |
| Permissions | Read Only |
| High-level VIs | N/A |
| Channel-based | No |
| Port-based | No |
| Device-based | Yes |
| Resettable | No |

<!--NI_TOPIC bundle=ni-rfpm-api-ref path=rfpmpropref/pnirfpm_calibrationloadboardcalibrationyear.html language=enus -->
## TOPIC 00124: Calibration Load Board Calibration Information:Calibration Load Board Calibration Year Property

- bundle_id: `ni-rfpm-api-ref`
- source_path: `rfpmpropref/pnirfpm_calibrationloadboardcalibrationyear.html`
- source_url: https://docs-be.ni.com/bundle/ni-rfpm-api-ref/raw/resource/enus/rfpmpropref/pnirfpm_calibrationloadboardcalibrationyear.html
- document_id: `ni-rfpm-api-ref`
- page_type: `leaf`
- content_type: ``

Calibration Load Board Calibration Information:Calibration Load Board Calibration Year Property

**Short Name:**Calibration Load Board Calibration Year

Property of [niRFPM](cnirfpm.html)

Returns the year of the last time the RF multiport calibration module was calibrated.

This property does not support the mmWave subsystem.

#### Remarks

The following table lists the characteristics of this property.

| Datatype |  |
| --- | --- |
| Permissions | Read Only |
| High-level VIs | N/A |
| Channel-based | No |
| Port-based | No |
| Device-based | Yes |
| Resettable | No |

<!--NI_TOPIC bundle=ni-rfpm-api-ref path=rfpmpropref/pnirfpm_calibrationloadboardmodelnumber.html language=enus -->
## TOPIC 00125: Calibration:Calibration Load Board Model Number Property

- bundle_id: `ni-rfpm-api-ref`
- source_path: `rfpmpropref/pnirfpm_calibrationloadboardmodelnumber.html`
- source_url: https://docs-be.ni.com/bundle/ni-rfpm-api-ref/raw/resource/enus/rfpmpropref/pnirfpm_calibrationloadboardmodelnumber.html
- document_id: `ni-rfpm-api-ref`
- page_type: `leaf`
- content_type: ``

Calibration:Calibration Load Board Model Number Property

**Short Name:**Calibration Load Board Model Number

Property of [niRFPM](cnirfpm.html)

Returns the model number of the calibration load board.

This property does not support the mmWave subsystem.

#### Remarks

The following table lists the characteristics of this property.

| Datatype |  |
| --- | --- |
| Permissions | Read Only |
| High-level VIs | N/A |
| Channel-based | No |
| Port-based | No |
| Device-based | No |
| Resettable | No |

<!--NI_TOPIC bundle=ni-rfpm-api-ref path=rfpmpropref/pnirfpm_calibrationloadboardserialnumber.html language=enus -->
## TOPIC 00126: Calibration:Calibration Load Board Serial Number Property

- bundle_id: `ni-rfpm-api-ref`
- source_path: `rfpmpropref/pnirfpm_calibrationloadboardserialnumber.html`
- source_url: https://docs-be.ni.com/bundle/ni-rfpm-api-ref/raw/resource/enus/rfpmpropref/pnirfpm_calibrationloadboardserialnumber.html
- document_id: `ni-rfpm-api-ref`
- page_type: `leaf`
- content_type: ``

Calibration:Calibration Load Board Serial Number Property

**Short Name:**Calibration Load Board Serial Number

Property of [niRFPM](cnirfpm.html)

Returns the serial number of the calibration load board.

This property does not support the mmWave subsystem.

#### Remarks

The following table lists the characteristics of this property.

| Datatype |  |
| --- | --- |
| Permissions | Read Only |
| High-level VIs | N/A |
| Channel-based | No |
| Port-based | No |
| Device-based | No |
| Resettable | No |

<!--NI_TOPIC bundle=ni-rfpm-api-ref path=rfpmpropref/pnirfpm_deembeddingenabled.html language=enus -->
## TOPIC 00127: Measurement:De-embedding Enabled Property

- bundle_id: `ni-rfpm-api-ref`
- source_path: `rfpmpropref/pnirfpm_deembeddingenabled.html`
- source_url: https://docs-be.ni.com/bundle/ni-rfpm-api-ref/raw/resource/enus/rfpmpropref/pnirfpm_deembeddingenabled.html
- document_id: `ni-rfpm-api-ref`
- page_type: `leaf`
- content_type: ``

Measurement:De-embedding Enabled Property

**Short Name:**De-embedding Enabled

Property of [niRFPM](cnirfpm.html)

Specifies whether de-embedding is applied to the measurement and calibration data.

**Default Value**: FALSE

#### Remarks

The following table lists the characteristics of this property.

| Datatype |  |
| --- | --- |
| Permissions | Read/Write |
| High-level VIs | N/A |
| Channel-based | No |
| Port-based | No |
| Device-based | Yes |
| Resettable | No |

<!--NI_TOPIC bundle=ni-rfpm-api-ref path=rfpmpropref/pnirfpm_deembeddings2p_orientation.html language=enus -->
## TOPIC 00128: Measurement:De-embedding S2P Orientation Property

- bundle_id: `ni-rfpm-api-ref`
- source_path: `rfpmpropref/pnirfpm_deembeddings2p_orientation.html`
- source_url: https://docs-be.ni.com/bundle/ni-rfpm-api-ref/raw/resource/enus/rfpmpropref/pnirfpm_deembeddings2p_orientation.html
- document_id: `ni-rfpm-api-ref`
- page_type: `leaf`
- content_type: ``

Measurement:De-embedding S2P Orientation Property

**Short Name:**De-embedding S2P Orientation

Property of [niRFPM](cnirfpm.html)

Specifies whether the de-embedding network in the S2P file is connected with port 1 towards the DUT or port 2 towards the DUT.

**Default Value**: **S2P Port1 Towards DUT**

| S2P Port1 Towards DUT (1) | Port 1 of the S2P is oriented towards the DUT. |
| --- | --- |
| S2P Port2 Towards DUT (2) | Port 2 of the S2P is oriented towards the DUT. |

#### Remarks

The following table lists the characteristics of this property.

| Datatype |  |
| --- | --- |
| Permissions | Read/Write |
| High-level VIs | NI-RFPM Configure De-Embedding |
| Channel-based | No |
| Port-based | Yes |
| Device-based | No |
| Resettable | No |

<!--NI_TOPIC bundle=ni-rfpm-api-ref path=rfpmpropref/pnirfpm_deembeddings2p_path.html language=enus -->
## TOPIC 00129: Measurement:De-embedding S2P Path Property

- bundle_id: `ni-rfpm-api-ref`
- source_path: `rfpmpropref/pnirfpm_deembeddings2p_path.html`
- source_url: https://docs-be.ni.com/bundle/ni-rfpm-api-ref/raw/resource/enus/rfpmpropref/pnirfpm_deembeddings2p_path.html
- document_id: `ni-rfpm-api-ref`
- page_type: `leaf`
- content_type: ``

Measurement:De-embedding S2P Path Property

**Short Name:**De-embedding S2P Path

Property of [niRFPM](cnirfpm.html)

Specifies the path to the S2P file that characterizes the de-embedding network for the given port.

**Default Value**: **""** (empty string)

#### Remarks

The following table lists the characteristics of this property.

| Datatype |  |
| --- | --- |
| Permissions | Read/Write |
| High-level VIs | NI-RFPM Configure De-Embedding |
| Channel-based | No |
| Port-based | Yes |
| Device-based | No |
| Resettable | No |

<!--NI_TOPIC bundle=ni-rfpm-api-ref path=rfpmpropref/pnirfpm_driverstate.html language=enus -->
## TOPIC 00130: Driver State Property

- bundle_id: `ni-rfpm-api-ref`
- source_path: `rfpmpropref/pnirfpm_driverstate.html`
- source_url: https://docs-be.ni.com/bundle/ni-rfpm-api-ref/raw/resource/enus/rfpmpropref/pnirfpm_driverstate.html
- document_id: `ni-rfpm-api-ref`
- page_type: `leaf`
- content_type: ``

Driver State Property

**Short Name:**Driver State

Property of [niRFPM](cnirfpm.html)

Indicates the current state of the driver.

#### Remarks

The following table lists the characteristics of this property.

| Datatype |  |
| --- | --- |
| Permissions | Read Only |
| High-level VIs | N/A |
| Channel-based | No |
| Port-based | No |
| Device-based | Yes |
| Resettable | No |

<!--NI_TOPIC bundle=ni-rfpm-api-ref path=rfpmpropref/pnirfpm_externalsettlingtime.html language=enus -->
## TOPIC 00131: Measurement:External Settling Time Property

- bundle_id: `ni-rfpm-api-ref`
- source_path: `rfpmpropref/pnirfpm_externalsettlingtime.html`
- source_url: https://docs-be.ni.com/bundle/ni-rfpm-api-ref/raw/resource/enus/rfpmpropref/pnirfpm_externalsettlingtime.html
- document_id: `ni-rfpm-api-ref`
- page_type: `leaf`
- content_type: ``

Measurement:External Settling Time Property

**Short Name:**External Settling Time

Property of [niRFPM](cnirfpm.html)

Specifies the time to delay the S-parameter measurement after the source is modified to allow for external settling. This value is expressed in seconds.

**Default Value**: 0

#### Remarks

The following table lists the characteristics of this property.

| Datatype |  |
| --- | --- |
| Permissions | Read/Write |
| High-level VIs | N/A |
| Channel-based | No |
| Port-based | No |
| Device-based | Yes |
| Resettable | No |

<!--NI_TOPIC bundle=ni-rfpm-api-ref path=rfpmpropref/pnirfpm_interpolationenabled.html language=enus -->
## TOPIC 00132: Measurement:Interpolation Enabled Property

- bundle_id: `ni-rfpm-api-ref`
- source_path: `rfpmpropref/pnirfpm_interpolationenabled.html`
- source_url: https://docs-be.ni.com/bundle/ni-rfpm-api-ref/raw/resource/enus/rfpmpropref/pnirfpm_interpolationenabled.html
- document_id: `ni-rfpm-api-ref`
- page_type: `leaf`
- content_type: ``

Measurement:Interpolation Enabled Property

**Short Name:**Interpolation Enabled

Property of [niRFPM](cnirfpm.html)

Specifies if interpolation across frequency is used when fetching source and receiver offsets by parameters.

This property does not support the mmWave subsystem.

**Default Value**: FALSE

#### Remarks

The following table lists the characteristics of this property.

| Datatype |  |
| --- | --- |
| Permissions | Read/Write |
| High-level VIs | N/A |
| Channel-based | No |
| Port-based | No |
| Device-based | Yes |
| Resettable | No |

<!--NI_TOPIC bundle=ni-rfpm-api-ref path=rfpmpropref/pnirfpm_maxfreqspanforinterpolation.html language=enus -->
## TOPIC 00133: Measurement:Maximum Frequency Span for Interpolation Property

- bundle_id: `ni-rfpm-api-ref`
- source_path: `rfpmpropref/pnirfpm_maxfreqspanforinterpolation.html`
- source_url: https://docs-be.ni.com/bundle/ni-rfpm-api-ref/raw/resource/enus/rfpmpropref/pnirfpm_maxfreqspanforinterpolation.html
- document_id: `ni-rfpm-api-ref`
- page_type: `leaf`
- content_type: ``

Measurement:Maximum Frequency Span for Interpolation Property

**Short Name:**Max Freq Span for Interpolation

Property of [niRFPM](cnirfpm.html)

Specifies the maximum span between two adjacent calibration frequencies for which interpolation will be performed, expressed in Hz.

This property does not support the mmWave subsystem.

Spans higher than 100 MHz are not supported and result in an error, and the driver does not accept the new value. Negative and zero spans are also not supported and result in an error, and the driver does not accept the new value.

**Default Value**: 20 MHz

#### Remarks

The following table lists the characteristics of this property.

| Datatype |  |
| --- | --- |
| Permissions | Read/Write |
| High-level VIs | N/A |
| Channel-based | No |
| Port-based | No |
| Device-based | Yes |
| Resettable | No |

<!--NI_TOPIC bundle=ni-rfpm-api-ref path=rfpmpropref/pnirfpm_maxpowerlevelcoercion.html language=enus -->
## TOPIC 00134: Measurement:Maximum Power Level Coercion Property

- bundle_id: `ni-rfpm-api-ref`
- source_path: `rfpmpropref/pnirfpm_maxpowerlevelcoercion.html`
- source_url: https://docs-be.ni.com/bundle/ni-rfpm-api-ref/raw/resource/enus/rfpmpropref/pnirfpm_maxpowerlevelcoercion.html
- document_id: `ni-rfpm-api-ref`
- page_type: `leaf`
- content_type: ``

Measurement:Maximum Power Level Coercion Property

**Short Name:**Max Power Level Coercion

Property of [niRFPM](cnirfpm.html)

Specifies the maximum difference allowed between the requested power level and the matching power level when power level coercion is enabled, expressed in dBm.

This property does not support the mmWave subsystem.

Negative and zero values are not supported and result in an error, and the driver does not accept the new value.

**Default Value**: 0.05 dB

#### Remarks

The following table lists the characteristics of this property.

| Datatype |  |
| --- | --- |
| Permissions | Read/Write |
| High-level VIs | N/A |
| Channel-based | No |
| Port-based | No |
| Device-based | Yes |
| Resettable | No |

<!--NI_TOPIC bundle=ni-rfpm-api-ref path=rfpmpropref/pnirfpm_maxreferencelevelcoercion.html language=enus -->
## TOPIC 00135: Measurement:Maximum Reference Level Coercion Property

- bundle_id: `ni-rfpm-api-ref`
- source_path: `rfpmpropref/pnirfpm_maxreferencelevelcoercion.html`
- source_url: https://docs-be.ni.com/bundle/ni-rfpm-api-ref/raw/resource/enus/rfpmpropref/pnirfpm_maxreferencelevelcoercion.html
- document_id: `ni-rfpm-api-ref`
- page_type: `leaf`
- content_type: ``

Measurement:Maximum Reference Level Coercion Property

**Short Name:**Max Reference Level Coercion

Property of [niRFPM](cnirfpm.html)

Specifies the maximum difference allowed between the requested reference level and the matching reference level when reference level coercion is enabled, expressed in dBm.

This property does not support the mmWave subsystem.

Negative and zero values are not supported and result in an error, and the driver does not accept the new value.

**Default Value**: Positive infinity

#### Remarks

The following table lists the characteristics of this property.

| Datatype |  |
| --- | --- |
| Permissions | Read/Write |
| High-level VIs | N/A |
| Channel-based | No |
| Port-based | No |
| Device-based | Yes |
| Resettable | No |

<!--NI_TOPIC bundle=ni-rfpm-api-ref path=rfpmpropref/pnirfpm_powerlevelcoercionmethod.html language=enus -->
## TOPIC 00136: Measurement:Power Level Coercion Method Property

- bundle_id: `ni-rfpm-api-ref`
- source_path: `rfpmpropref/pnirfpm_powerlevelcoercionmethod.html`
- source_url: https://docs-be.ni.com/bundle/ni-rfpm-api-ref/raw/resource/enus/rfpmpropref/pnirfpm_powerlevelcoercionmethod.html
- document_id: `ni-rfpm-api-ref`
- page_type: `leaf`
- content_type: ``

Measurement:Power Level Coercion Method Property

**Short Name:**Power Level Coercion Method

Property of [niRFPM](cnirfpm.html)

Specifies if and how power level is coerced when fetching the source offset. Coercion can either be to the nearest calibrated power level with a matching frequency, or to a lower power level only.

This property does not support the mmWave subsystem.

If you only enable power level coercion and do not enable frequency interpolation by setting the **Interpolation Enabled** property to TRUE, NI-RFPM looks for an offset that matches the requested frequency exactly, and has a power level within the range specified by the **Maximum Power Level Coercion** property. Of those points, NI-RFPM coerces to the offset whose power level is closest to the requested value.

If you enable power level coercion and set **Interpolation Enabled** to TRUE, NI-RFPM first attempts to do the same as above. If no exact frequency matches are found, NI-RFPM selects the pair of points whose power levels are in the coercible range, and whose frequencies are closest to what was requested (one above and one below), and interpolates between them.

**Default Value**: Coercion Diabled

| Coercion Disabled (1) | Power level coercion is disabled. |
| --- | --- |
| Coercion to Nearest Power (2) | Power level will be coerced to the nearest calibrated power, higher or lower. |
| Coercion to Lower Power (3) | Power level will be coerced only to a lower calibrated power. |

#### Remarks

The following table lists the characteristics of this property.

| Datatype |  |
| --- | --- |
| Permissions | Read/Write |
| High-level VIs | N/A |
| Channel-based | No |
| Port-based | No |
| Device-based | Yes |
| Resettable | No |

<!--NI_TOPIC bundle=ni-rfpm-api-ref path=rfpmpropref/pnirfpm_powermeterresourcename.html language=enus -->
## TOPIC 00137: Calibration:Power Meter Resource Name Property

- bundle_id: `ni-rfpm-api-ref`
- source_path: `rfpmpropref/pnirfpm_powermeterresourcename.html`
- source_url: https://docs-be.ni.com/bundle/ni-rfpm-api-ref/raw/resource/enus/rfpmpropref/pnirfpm_powermeterresourcename.html
- document_id: `ni-rfpm-api-ref`
- page_type: `leaf`
- content_type: ``

Calibration:Power Meter Resource Name Property

**Short Name:**Power Meter Resource Name

Property of [niRFPM](cnirfpm.html)

Specifies the name of the power meter resource that an RF multiport calibration module uses. To read this attribute, the RF multiport calibration module must be connected. If there is only one RF multiport calibration module and the AutoCal Resource Name property is an empty string, the driver automatically detects the RF multiport calibration module to get the power meter resource name from. If there is more than one NI Automatic RF Calibration Module or the string is not empty, the driver finds the power meter resource name from the RF multiport calibration module specified by the AutoCal Resource Name property. This property does not report a valid resource name until after the niRFPM Init User Calibration VI runs.

This property does not support the mmWave subsystem.

**Default Value**: **""** (empty string)

#### Remarks

The following table lists the characteristics of this property.

| Datatype |  |
| --- | --- |
| Permissions | Read Only |
| High-level VIs | N/A |
| Channel-based | No |
| Port-based | No |
| Device-based | Yes |
| Resettable | No |

<!--NI_TOPIC bundle=ni-rfpm-api-ref path=rfpmpropref/pnirfpm_receiveramplitudesettling.html language=enus -->
## TOPIC 00138: Measurement:Receiver Amplitude Settling Property

- bundle_id: `ni-rfpm-api-ref`
- source_path: `rfpmpropref/pnirfpm_receiveramplitudesettling.html`
- source_url: https://docs-be.ni.com/bundle/ni-rfpm-api-ref/raw/resource/enus/rfpmpropref/pnirfpm_receiveramplitudesettling.html
- document_id: `ni-rfpm-api-ref`
- page_type: `leaf`
- content_type: ``

Measurement:Receiver Amplitude Settling Property

**Short Name:**Receiver Amplitude Settling

Property of [niRFPM](cnirfpm.html)

Specifies the receiver amplitude settling accuracy for scalar measurements in decibels.

This property does not support the mmWave subsystem.

This value is used to calculate the receiver settling time when the Read Receiver Settling Time VI is called. Valid values are 0.5 dB, 0.2 dB, 0.1 dB, and 0.05 dB.

**Default Value**: 0.05 dB

#### Remarks

The following table lists the characteristics of this property.

| Datatype |  |
| --- | --- |
| Permissions | Read/Write |
| High-level VIs | N/A |
| Channel-based | No |
| Port-based | No |
| Device-based | Yes |
| Resettable | No |

<!--NI_TOPIC bundle=ni-rfpm-api-ref path=rfpmpropref/pnirfpm_receivercorrectionenabled.html language=enus -->
## TOPIC 00139: Calibration:Receiver Power Correction Enabled Property

- bundle_id: `ni-rfpm-api-ref`
- source_path: `rfpmpropref/pnirfpm_receivercorrectionenabled.html`
- source_url: https://docs-be.ni.com/bundle/ni-rfpm-api-ref/raw/resource/enus/rfpmpropref/pnirfpm_receivercorrectionenabled.html
- document_id: `ni-rfpm-api-ref`
- page_type: `leaf`
- content_type: ``

Calibration:Receiver Power Correction Enabled Property

**Short Name:**Receiver Power Correction Enabled

Property of [niRFPM](cnirfpm.html)

Specifies whether the receiver input power offsets use user-calibrated values or factory calibration values.

This property does not support the mmWave subsystem.

**Default Value**: TRUE

#### Remarks

The following table lists the characteristics of this property.

| Datatype |  |
| --- | --- |
| Permissions | Read/Write |
| High-level VIs | N/A |
| Channel-based | No |
| Port-based | No |
| Device-based | Yes |
| Resettable | No |

<!--NI_TOPIC bundle=ni-rfpm-api-ref path=rfpmpropref/pnirfpm_referenceclocksource.html language=enus -->
## TOPIC 00140: Measurement:Reference Clock Source Property

- bundle_id: `ni-rfpm-api-ref`
- source_path: `rfpmpropref/pnirfpm_referenceclocksource.html`
- source_url: https://docs-be.ni.com/bundle/ni-rfpm-api-ref/raw/resource/enus/rfpmpropref/pnirfpm_referenceclocksource.html
- document_id: `ni-rfpm-api-ref`
- page_type: `leaf`
- content_type: ``

Measurement:Reference Clock Source Property

**Short Name:**Reference Clock Source

Property of [niRFPM](cnirfpm.html)

Specifies the source to use for the Reference Clock.

**Default Value**: **Onboard Clock**

| Onboard Clock (0) | Uses the internal clock of the device. |
| --- | --- |
| Ref In (1) | Uses a clock supplied to the REF IN port of the device. |
| PXI Clk (2) | Uses the PXI backplane clock. |

#### Remarks

The following table lists the characteristics of this property.

| Datatype |  |
| --- | --- |
| Permissions | Read/Write |
| High-level VIs | N/A |
| Channel-based | No |
| Port-based | No |
| Device-based | Yes |
| Resettable | No |

<!--NI_TOPIC bundle=ni-rfpm-api-ref path=rfpmpropref/pnirfpm_referencelevelcoercionenabled.html language=enus -->
## TOPIC 00141: Measurement:Reference Level Coercion Enabled Property

- bundle_id: `ni-rfpm-api-ref`
- source_path: `rfpmpropref/pnirfpm_referencelevelcoercionenabled.html`
- source_url: https://docs-be.ni.com/bundle/ni-rfpm-api-ref/raw/resource/enus/rfpmpropref/pnirfpm_referencelevelcoercionenabled.html
- document_id: `ni-rfpm-api-ref`
- page_type: `leaf`
- content_type: ``

Measurement:Reference Level Coercion Enabled Property

**Short Name:**Reference Level Coercion Enabled

Property of [niRFPM](cnirfpm.html)

Specifies whether reference level is coerced to the next highest reference level with a matching frequency when fetching receiver offset by parameters.

This property does not support the mmWave subsystem.

If you only enable reference level coercion and do not enable frequency interpolation by setting the **Interpolation Enabled** property to TRUE, NI-RFPM looks for an offset that matches the requested frequency exactly, and has a reference level within the range specified by the **Maximum Reference Level Coercion** property. Of those points, NI-RFPM coerces to the offset whose reference level is closest to the requested value.

If both **Reference Level Coercion Enabled** and **Interpolation Enabled** are set to TRUE, NI-RFPM first attempts to do the same as above. If no exact frequency matches are found, NI-RFPM selects the pair of points whose reference levels are in the coercible range, and whose frequencies are closest to what was requested (one above and one below), and interpolates between them.

**Default Value**: FALSE

#### Remarks

The following table lists the characteristics of this property.

| Datatype |  |
| --- | --- |
| Permissions | Read/Write |
| High-level VIs | N/A |
| Channel-based | No |
| Port-based | No |
| Device-based | Yes |
| Resettable | No |

<!--NI_TOPIC bundle=ni-rfpm-api-ref path=rfpmpropref/pnirfpm_skipselfcalibrationtimestampcheck.html language=enus -->
## TOPIC 00142: Calibration:Skip Self Calibration Timestamp Check Property

- bundle_id: `ni-rfpm-api-ref`
- source_path: `rfpmpropref/pnirfpm_skipselfcalibrationtimestampcheck.html`
- source_url: https://docs-be.ni.com/bundle/ni-rfpm-api-ref/raw/resource/enus/rfpmpropref/pnirfpm_skipselfcalibrationtimestampcheck.html
- document_id: `ni-rfpm-api-ref`
- page_type: `leaf`
- content_type: ``

Calibration:Skip Self Calibration Timestamp Check Property

**Short Name:**Skip Self Calibration Timestamp Check

Property of [niRFPM](cnirfpm.html)

Specifies whether to skip validation of self calibration timestamp and vector calibration timestamp.

This property does not support the RF subsystem.

**Default Value**: FALSE

#### Remarks

The following table lists the characteristics of this property.

| Datatype |  |
| --- | --- |
| Permissions | Read/Write |
| High-level VIs | N/A |
| Channel-based | No |
| Port-based | No |
| Device-based | No |
| Resettable | No |

<!--NI_TOPIC bundle=ni-rfpm-api-ref path=rfpmpropref/pnirfpm_sourceamplitudesettling.html language=enus -->
## TOPIC 00143: Measurement:Source Amplitude Settling Property

- bundle_id: `ni-rfpm-api-ref`
- source_path: `rfpmpropref/pnirfpm_sourceamplitudesettling.html`
- source_url: https://docs-be.ni.com/bundle/ni-rfpm-api-ref/raw/resource/enus/rfpmpropref/pnirfpm_sourceamplitudesettling.html
- document_id: `ni-rfpm-api-ref`
- page_type: `leaf`
- content_type: ``

Measurement:Source Amplitude Settling Property

**Short Name:**Source Amplitude Settling

Property of [niRFPM](cnirfpm.html)

Specifies the source amplitude settling accuracy for vector and scalar measurements in decibels.

This property does not support the mmWave subsystem.

This value is used to calculate the source settling time when the Fetch Source Offset With Settings And Settling Time VI is called and during measurements. Valid values are 0.5 dB, 0.2 dB, 0.1 dB, and 0.05 dB.

**Default Value**: 0.05 dB

#### Remarks

The following table lists the characteristics of this property.

| Datatype |  |
| --- | --- |
| Permissions | Read/Write |
| High-level VIs | N/A |
| Channel-based | No |
| Port-based | No |
| Device-based | Yes |
| Resettable | No |

<!--NI_TOPIC bundle=ni-rfpm-api-ref path=rfpmpropref/pnirfpm_sourcecorrectionenabled.html language=enus -->
## TOPIC 00144: Calibration:Source Power Correction Enabled Property

- bundle_id: `ni-rfpm-api-ref`
- source_path: `rfpmpropref/pnirfpm_sourcecorrectionenabled.html`
- source_url: https://docs-be.ni.com/bundle/ni-rfpm-api-ref/raw/resource/enus/rfpmpropref/pnirfpm_sourcecorrectionenabled.html
- document_id: `ni-rfpm-api-ref`
- page_type: `leaf`
- content_type: ``

Calibration:Source Power Correction Enabled Property

**Short Name:**Source Power Correction Enabled

Property of [niRFPM](cnirfpm.html)

Specifies whether the source output power offsets use user-calibrated values or factory calibration values. This property also specifies whether the source output power offsets are applied during S-parameter measurements.

This property does not support the mmWave subsystem.

**Default Value**: TRUE

#### Remarks

The following table lists the characteristics of this property.

| Datatype |  |
| --- | --- |
| Permissions | Read/Write |
| High-level VIs | N/A |
| Channel-based | No |
| Port-based | No |
| Device-based | Yes |
| Resettable | No |

<!--NI_TOPIC bundle=ni-rfpm-api-ref path=rfpmpropref/pnirfpm_vectorcorrectionenabled.html language=enus -->
## TOPIC 00145: Measurement:Vector Correction Enabled Property

- bundle_id: `ni-rfpm-api-ref`
- source_path: `rfpmpropref/pnirfpm_vectorcorrectionenabled.html`
- source_url: https://docs-be.ni.com/bundle/ni-rfpm-api-ref/raw/resource/enus/rfpmpropref/pnirfpm_vectorcorrectionenabled.html
- document_id: `ni-rfpm-api-ref`
- page_type: `leaf`
- content_type: ``

Measurement:Vector Correction Enabled Property

**Short Name:**Vector Correction Enabled

Property of [niRFPM](cnirfpm.html)

Specifies whether the vector error correction is applied to the measurement data.

**Default Value**: TRUE

#### Remarks

The following table lists the characteristics of this property.

| Datatype |  |
| --- | --- |
| Permissions | Read/Write |
| High-level VIs | N/A |
| Channel-based | No |
| Port-based | No |
| Device-based | Yes |
| Resettable | No |

<!--NI_TOPIC bundle=ni-rfpm-api-ref path=rfpmpropref/pnirfpm_vectorreceiveramplitudesettling.html language=enus -->
## TOPIC 00146: Measurement:Vector Receiver Amplitude Settling Property

- bundle_id: `ni-rfpm-api-ref`
- source_path: `rfpmpropref/pnirfpm_vectorreceiveramplitudesettling.html`
- source_url: https://docs-be.ni.com/bundle/ni-rfpm-api-ref/raw/resource/enus/rfpmpropref/pnirfpm_vectorreceiveramplitudesettling.html
- document_id: `ni-rfpm-api-ref`
- page_type: `leaf`
- content_type: ``

Measurement:Vector Receiver Amplitude Settling Property

**Short Name:**Vector Receiver Amplitude Settling

Property of [niRFPM](cnirfpm.html)

Specifies the receiver amplitude settling accuracy for vector measurements in decibels.

This property does not support the mmWave subsystem.

This value is used by NI-RFPM to account for receiver settling during measurements. Valid values are 0.5 dB, 0.2 dB, 0.1 dB, and 0.05 dB.

**Default Value**: 0.05 dB

#### Remarks

The following table lists the characteristics of this property.

| Datatype |  |
| --- | --- |
| Permissions | Read/Write |
| High-level VIs | N/A |
| Channel-based | No |
| Port-based | No |
| Device-based | Yes |
| Resettable | No |

<!--NI_TOPIC bundle=ni-rfpm-api-ref path=rfpmswitchpropref/cnirfpmswitch.html language=enus -->
## TOPIC 00147: niRFPMSwitch Properties

- bundle_id: `ni-rfpm-api-ref`
- source_path: `rfpmswitchpropref/cnirfpmswitch.html`
- source_url: https://docs-be.ni.com/bundle/ni-rfpm-api-ref/raw/resource/enus/rfpmswitchpropref/cnirfpmswitch.html
- document_id: `ni-rfpm-api-ref`
- page_type: `leaf`
- content_type: ``

niRFPMSwitch Properties

April 2021, 376932C-01

Use the NI-RFPMSwitch properties to access advanced configuration options for NI-RFPMSwitch applications.

| Property | Description |
| --- | --- |
| Active Channel | Specifies the channel name used to access all subsequent properties in this instance of the property node. If the property you want to use is channel- or port-based, you must first select this property and then pass the name of the specific channel or port. If the property you specify is not channel- or port-based, pass an empty string, or omit setting this property. The default value is " ". This property does not support the mmWave subsystem. Details |
| Inherent IVI Properties:User Options:Range Check | Specifies whether to validate property values and VI parameters. The default value is TRUE. Use the niRFPMSwitch Initialize With Options VI to override this value. This property does not support the mmWave subsystem. Details |
| Inherent IVI Properties:User Options:Query Instrument Status | Specifies whether NI-RFPMSwitch queries the NI-RFPMSwitch device status after each operation. The default value is TRUE. Use the niRFPMSwitch Initialize With Options VI to override this value. This property does not support the mmWave subsystem. Details |
| Inherent IVI Properties:User Options:Cache | Specifies whether to cache the value of properties. The default value is TRUE. Use the niRFPMSwitch Initialize With Options VI to override this value. This property does not support the mmWave subsystem. Details |
| Inherent IVI Properties:User Options:Simulate | Specifies whether to simulate NI-RFPMSwitch I/O operations. The default value is FALSE. Use the niRFPMSwitch Initialize With Options VI to override this value. This property does not support the mmWave subsystem. Details |
| Inherent IVI Properties:User Options:Record Value Coercions | Specifies whether the IVI engine keeps a list of the value coercions it makes for properties with ViInt32 and ViReal64 datatypes. Note This property is currently not supported. |
|  | Note This property is currently not supported. |
| Inherent IVI Properties:User Options:Interchange Check | Specifies whether to perform interchangeability checking and retrieve interchangeability warnings. Note This property is currently not supported. |
|  | Note This property is currently not supported. |
| Inherent IVI Properties:Driver Capabilities:Channel Count | Indicates the number of channels that NI-RFPMSwitch supports. For each property for which the IVI_VAL_MULTI_CHANNEL flag property is set, the instrument driver maintains a separate cache value for each channel. This property does not support the mmWave subsystem. Details |
| Inherent IVI Properties:Driver Capabilities:Supported Instrument Models | Returns a model code of the instrument. For specific drivers that support more than one device, this property returns a comma-separated list of supported instrument models. This property does not support the mmWave subsystem. Details |
| Inherent IVI Properties:Driver Capabilities:Group Capabilities | Indicates the IviSwtch capability groups that NI-RFPMSwitch supports. This property does not support the mmWave subsystem. Details |
| Inherent IVI Properties:Instrument Identification:Manufacturer | Returns a string that contains the name of the manufacturer for the NI-RFPMSwitch device you are currently using. This property does not support the mmWave subsystem. Details |
| Inherent IVI Properties:Instrument Identification:Model | Returns a string that contains the model number or name of the NI-RFPMSwitch device that you are currently using. This property does not support the mmWave subsystem. Details |
| Inherent IVI Properties:Instrument Identification:Firmware Revision | Returns a string that contains the firmware revision information for the NI-RFPMSwitch device you are currently using. This property does not support the mmWave subsystem. Details |
| Inherent IVI Properties:Driver Identification:Description | Returns a string that contains a brief description of NI-RFPMSwitch. This property does not support the mmWave subsystem. Details |
| Inherent IVI Properties:Driver Identification:Driver Prefix | Returns a string that contains the prefix for NI-RFPMSwitch. The name of each user-callable VI in NI-RFPMSwitch starts with this prefix. This property does not support the mmWave subsystem. Details |
| Inherent IVI Properties:Driver Identification:Driver Vendor | Returns a string that contains the name of the vendor that supplies NI-RFPMSwitch. This property does not support the mmWave subsystem. Details |
| Inherent IVI Properties:Driver Identification:Revision | Returns a string that contains additional version information about NI-RFPMSwitch. This property does not support the mmWave subsystem. Details |
| Inherent IVI Properties:Driver Identification:Class Specification Major Version | Returns the major version number of the class specification with which NI-RFPMSwitch is compliant. This property does not support the mmWave subsystem. Details |
| Inherent IVI Properties:Driver Identification:Class Specification Minor Version | Returns the minor version number of the class specification with which NI-RFPMSwitch is compliant. This property does not support the mmWave subsystem. Details |
| Inherent IVI Properties:Advanced Session Information:Logical Name | Contains the logical name you specified when opening the current IVI session. You may pass a logical name to the niRFPMSwitch Initialize VI or the niRFPMSwitch Initialize With Options VI. The IVI Configuration Utility must contain an entry for the logical name. The logical name entry refers to a driver session section in the IVI Configuration file. The driver session section specifies a physical device and initial user options. This property does not support the mmWave subsystem. Details |
| Inherent IVI Properties:Advanced Session Information:I/O Resource Descriptor | Indicates the resource name NI-RFPMSwitch uses to identify the physical device. If you initialize NI-RFPMSwitch with a logical name, this property contains the resource name that corresponds to the entry in the IVI Configuration Utility. If you initialize NI-RFPM Switch with the resource name, this property contains that value. This property does not support the mmWave subsystem. Details |
| Inherent IVI Properties:Channel Configuration:Is Source Channel | Specifies whether to designate the channel as a source channel. This property does not support the mmWave subsystem. Details |
| Inherent IVI Properties:Channel Configuration:Is Configuration Channel | Specifies whether to designate the channel as a configuration channel—a channel reserved for internal path creation. NI-RFPMSwitch uses configuration channels to create paths between the channels you specify in the niRFPMSwitch Connect Channels VI. This property does not support the mmWave subsystem. Details |
| Module Characteristics:Is Debounced | Indicates whether the entire switch module has settled since the last switching command. A value of TRUE indicates that all signals going through the switch module are valid. This property does not support the mmWave subsystem. Details |
| Module Characteristics:Settling Time | Returns the maximum length of time, in seconds, from after you make a connection until the signal flowing through the channel settles. This property does not support the mmWave subsystem. Details |
| Module Characteristics:Bandwidth | Returns the bandwidth for the channel, in hertz. This property does not support the mmWave subsystem. Details |
| Device Information:Temperature | Returns the current temperature of the device, in degrees Celsius. This property does not support the mmWave subsystem. Details |
| Device Information:Number of External Ports | Returns the number of ports that you are able to connect to the device under test (DUT). This property does not support the mmWave subsystem. Details |
| Device Information:Port Type | Returns the type of the port that was specified with the active channel property. This property does not support the mmWave subsystem. Details |
| Device Information:Port Daisy Chain Depth | Returns the daisy chain depth of the port that was specified with the active channel property. This property does not support the mmWave subsystem. Details |

<!--NI_TOPIC bundle=ni-rfpm-api-ref path=rfpmswitchpropref/pnirfpm_classgroupcapabilities.html language=enus -->
## TOPIC 00148: Inherent IVI Properties:Driver Capabilities:Group Capabilities Property

- bundle_id: `ni-rfpm-api-ref`
- source_path: `rfpmswitchpropref/pnirfpm_classgroupcapabilities.html`
- source_url: https://docs-be.ni.com/bundle/ni-rfpm-api-ref/raw/resource/enus/rfpmswitchpropref/pnirfpm_classgroupcapabilities.html
- document_id: `ni-rfpm-api-ref`
- page_type: `leaf`
- content_type: ``

Inherent IVI Properties:Driver Capabilities:Group Capabilities Property

**Short Name:**Group Capabilities

Property of [niRFPMSwitch](cnirfpmswitch.html)

Indicates the IviSwtch capability groups that NI-RFPMSwitch supports.

This property does not support the mmWave subsystem.

This property is a comma-delimited list of the following group names:

- IviSwtch—Supports fundamental switch capabilities.
- IviSwtchScanner—Supports IviSwtch with the capability to scan channels.
- IviSwtchSoftwareTrigger—Supports IviSwtchScanner with the capability to receive software triggers.

#### Remarks

The following table lists the characteristics of this property.

| Datatype |  |
| --- | --- |
| Permissions | Read Only |
| Resettable | No |

<!--NI_TOPIC bundle=ni-rfpm-api-ref path=rfpmswitchpropref/pnirfpmswitch_activechannel.html language=enus -->
## TOPIC 00149: Active Channel Property

- bundle_id: `ni-rfpm-api-ref`
- source_path: `rfpmswitchpropref/pnirfpmswitch_activechannel.html`
- source_url: https://docs-be.ni.com/bundle/ni-rfpm-api-ref/raw/resource/enus/rfpmswitchpropref/pnirfpmswitch_activechannel.html
- document_id: `ni-rfpm-api-ref`
- page_type: `leaf`
- content_type: ``

Active Channel Property

**Short Name:**Active Channel

Property of [niRFPMSwitch](cnirfpmswitch.html)

Specifies the channel name used to access all subsequent properties in this instance of the property node. If the property you want to use is channel- or port-based, you must first select this property and then pass the name of the specific channel or port. If the property you specify is not channel- or port-based, pass an empty string, or omit setting this property. The default value is " ".

This property does not support the mmWave subsystem.

For more information about device-, channel-, port-, standard-, and band-based properties, refer to [Using Properties and Attributes with NI-RFPM and NI-RFPMSwitch](../rfpmhelp/attributes.html).

#### Remarks

The following table lists the characteristics of this property.

| Datatype |  |
| --- | --- |
| Permissions | Write Only |
| Resettable | No |

<!--NI_TOPIC bundle=ni-rfpm-api-ref path=rfpmswitchpropref/pnirfpmswitch_bandwidth.html language=enus -->
## TOPIC 00150: Module Characteristics:Bandwidth Property

- bundle_id: `ni-rfpm-api-ref`
- source_path: `rfpmswitchpropref/pnirfpmswitch_bandwidth.html`
- source_url: https://docs-be.ni.com/bundle/ni-rfpm-api-ref/raw/resource/enus/rfpmswitchpropref/pnirfpmswitch_bandwidth.html
- document_id: `ni-rfpm-api-ref`
- page_type: `leaf`
- content_type: ``

Module Characteristics:Bandwidth Property

**Short Name:**Bandwidth

Property of [niRFPMSwitch](cnirfpmswitch.html)

Returns the bandwidth for the channel, in hertz.

This property does not support the mmWave subsystem.

#### Remarks

The following table lists the characteristics of this property.

| Datatype |  |
| --- | --- |
| Permissions | Read Only |
| Resettable | No |

<!--NI_TOPIC bundle=ni-rfpm-api-ref path=rfpmswitchpropref/pnirfpmswitch_cache.html language=enus -->
## TOPIC 00151: Inherent IVI Properties:User Options:Cache Property

- bundle_id: `ni-rfpm-api-ref`
- source_path: `rfpmswitchpropref/pnirfpmswitch_cache.html`
- source_url: https://docs-be.ni.com/bundle/ni-rfpm-api-ref/raw/resource/enus/rfpmswitchpropref/pnirfpmswitch_cache.html
- document_id: `ni-rfpm-api-ref`
- page_type: `leaf`
- content_type: ``

Inherent IVI Properties:User Options:Cache Property

**Short Name:**Cache

Property of [niRFPMSwitch](cnirfpmswitch.html)

Specifies whether to cache the value of properties. The default value is TRUE. Use the [niRFPMSwitch Initialize With Options](/csh?topicname=rfpmswitchviref/nirfpmswitch_initialize_with_options.html) VI to override this value.

This property does not support the mmWave subsystem.

Set this property to TRUE to track the current NI-RFPMSwitch device settings and avoid sending redundant commands to the device. NI-RFPMSwitch can always cache or never cache particular properties, regardless of the setting of this property.

#### Remarks

The following table lists the characteristics of this property.

| Datatype |  |
| --- | --- |
| Permissions | Read/Write |
| Resettable | No |

<!--NI_TOPIC bundle=ni-rfpm-api-ref path=rfpmswitchpropref/pnirfpmswitch_channelcount.html language=enus -->
## TOPIC 00152: Inherent IVI Properties:Driver Capabilities:Channel Count Property

- bundle_id: `ni-rfpm-api-ref`
- source_path: `rfpmswitchpropref/pnirfpmswitch_channelcount.html`
- source_url: https://docs-be.ni.com/bundle/ni-rfpm-api-ref/raw/resource/enus/rfpmswitchpropref/pnirfpmswitch_channelcount.html
- document_id: `ni-rfpm-api-ref`
- page_type: `leaf`
- content_type: ``

Inherent IVI Properties:Driver Capabilities:Channel Count Property

**Short Name:**Channel Count

Property of [niRFPMSwitch](cnirfpmswitch.html)

Indicates the number of channels that NI-RFPMSwitch supports.
 For each property for which the IVI_VAL_MULTI_CHANNEL flag property is set, the instrument driver maintains a separate cache value for each channel.

This property does not support the mmWave subsystem.

#### Remarks

The following table lists the characteristics of this property.

| Datatype |  |
| --- | --- |
| Permissions | Read Only |
| Resettable | No |

<!--NI_TOPIC bundle=ni-rfpm-api-ref path=rfpmswitchpropref/pnirfpmswitch_classdriverprefix.html language=enus -->
## TOPIC 00153: Inherent IVI Properties:Driver Identification:Driver Prefix Property

- bundle_id: `ni-rfpm-api-ref`
- source_path: `rfpmswitchpropref/pnirfpmswitch_classdriverprefix.html`
- source_url: https://docs-be.ni.com/bundle/ni-rfpm-api-ref/raw/resource/enus/rfpmswitchpropref/pnirfpmswitch_classdriverprefix.html
- document_id: `ni-rfpm-api-ref`
- page_type: `leaf`
- content_type: ``

Inherent IVI Properties:Driver Identification:Driver Prefix Property

**Short Name:**Specific Driver Prefix

Property of [niRFPMSwitch](cnirfpmswitch.html)

Returns a string that contains the prefix for NI-RFPMSwitch. The name of each user-callable VI in NI-RFPMSwitch starts with this prefix.

This property does not support the mmWave subsystem.

#### Remarks

The following table lists the characteristics of this property.

| Datatype |  |
| --- | --- |
| Permissions | Read Only |
| Resettable | No |

<!--NI_TOPIC bundle=ni-rfpm-api-ref path=rfpmswitchpropref/pnirfpmswitch_classspecificationmajorversion.html language=enus -->
## TOPIC 00154: Inherent IVI Properties:Driver Identification:Class Specification Major Version Property

- bundle_id: `ni-rfpm-api-ref`
- source_path: `rfpmswitchpropref/pnirfpmswitch_classspecificationmajorversion.html`
- source_url: https://docs-be.ni.com/bundle/ni-rfpm-api-ref/raw/resource/enus/rfpmswitchpropref/pnirfpmswitch_classspecificationmajorversion.html
- document_id: `ni-rfpm-api-ref`
- page_type: `leaf`
- content_type: ``

Inherent IVI Properties:Driver Identification:Class Specification Major Version Property

**Short Name:**Class Specification Major Version

Property of [niRFPMSwitch](cnirfpmswitch.html)

Returns the major version number of the class specification with which NI-RFPMSwitch is compliant.

This property does not support the mmWave subsystem.

#### Remarks

The following table lists the characteristics of this property.

| Datatype |  |
| --- | --- |
| Permissions | Read Only |
| Resettable | No |

<!--NI_TOPIC bundle=ni-rfpm-api-ref path=rfpmswitchpropref/pnirfpmswitch_classspecificationminorversion.html language=enus -->
## TOPIC 00155: Inherent IVI Properties:Driver Identification:Class Specification Minor Version Property

- bundle_id: `ni-rfpm-api-ref`
- source_path: `rfpmswitchpropref/pnirfpmswitch_classspecificationminorversion.html`
- source_url: https://docs-be.ni.com/bundle/ni-rfpm-api-ref/raw/resource/enus/rfpmswitchpropref/pnirfpmswitch_classspecificationminorversion.html
- document_id: `ni-rfpm-api-ref`
- page_type: `leaf`
- content_type: ``

Inherent IVI Properties:Driver Identification:Class Specification Minor Version Property

**Short Name:**Class Specification Minor Version

Property of [niRFPMSwitch](cnirfpmswitch.html)

Returns the minor version number of the class specification with which NI-RFPMSwitch is compliant.

This property does not support the mmWave subsystem.

#### Remarks

The following table lists the characteristics of this property.

| Datatype |  |
| --- | --- |
| Permissions | Read Only |
| Resettable | No |

<!--NI_TOPIC bundle=ni-rfpm-api-ref path=rfpmswitchpropref/pnirfpmswitch_description.html language=enus -->
## TOPIC 00156: Inherent IVI Properties:Driver Identification:Description Property

- bundle_id: `ni-rfpm-api-ref`
- source_path: `rfpmswitchpropref/pnirfpmswitch_description.html`
- source_url: https://docs-be.ni.com/bundle/ni-rfpm-api-ref/raw/resource/enus/rfpmswitchpropref/pnirfpmswitch_description.html
- document_id: `ni-rfpm-api-ref`
- page_type: `leaf`
- content_type: ``

Inherent IVI Properties:Driver Identification:Description Property

**Short Name:**Description

Property of [niRFPMSwitch](cnirfpmswitch.html)

Returns a string that contains a brief description of NI-RFPMSwitch.

This property does not support the mmWave subsystem.

#### Remarks

The following table lists the characteristics of this property.

| Datatype |  |
| --- | --- |
| Permissions | Read Only |
| Resettable | No |

<!--NI_TOPIC bundle=ni-rfpm-api-ref path=rfpmswitchpropref/pnirfpmswitch_devicetemperature.html language=enus -->
## TOPIC 00157: Device Information:Temperature Property

- bundle_id: `ni-rfpm-api-ref`
- source_path: `rfpmswitchpropref/pnirfpmswitch_devicetemperature.html`
- source_url: https://docs-be.ni.com/bundle/ni-rfpm-api-ref/raw/resource/enus/rfpmswitchpropref/pnirfpmswitch_devicetemperature.html
- document_id: `ni-rfpm-api-ref`
- page_type: `leaf`
- content_type: ``

Device Information:Temperature Property

**Short Name:**Device Temperature

Property of [niRFPMSwitch](cnirfpmswitch.html)

Returns the current temperature of the device, in degrees Celsius.

This property does not support the mmWave subsystem.

#### Remarks

The following table lists the characteristics of this property.

| Datatype |  |
| --- | --- |
| Permissions | Read Only |
| Resettable | No |

<!--NI_TOPIC bundle=ni-rfpm-api-ref path=rfpmswitchpropref/pnirfpmswitch_drivervendor.html language=enus -->
## TOPIC 00158: Inherent IVI Properties:Driver Identification:Driver Vendor Property

- bundle_id: `ni-rfpm-api-ref`
- source_path: `rfpmswitchpropref/pnirfpmswitch_drivervendor.html`
- source_url: https://docs-be.ni.com/bundle/ni-rfpm-api-ref/raw/resource/enus/rfpmswitchpropref/pnirfpmswitch_drivervendor.html
- document_id: `ni-rfpm-api-ref`
- page_type: `leaf`
- content_type: ``

Inherent IVI Properties:Driver Identification:Driver Vendor Property

**Short Name:**Driver Vendor

Property of [niRFPMSwitch](cnirfpmswitch.html)

Returns a string that contains the name of the vendor that supplies NI-RFPMSwitch.

This property does not support the mmWave subsystem.

#### Remarks

The following table lists the characteristics of this property.

| Datatype |  |
| --- | --- |
| Permissions | Read Only |
| Resettable | No |

<!--NI_TOPIC bundle=ni-rfpm-api-ref path=rfpmswitchpropref/pnirfpmswitch_firmwarerevision.html language=enus -->
## TOPIC 00159: Inherent IVI Properties:Instrument Identification:Firmware Revision Property

- bundle_id: `ni-rfpm-api-ref`
- source_path: `rfpmswitchpropref/pnirfpmswitch_firmwarerevision.html`
- source_url: https://docs-be.ni.com/bundle/ni-rfpm-api-ref/raw/resource/enus/rfpmswitchpropref/pnirfpmswitch_firmwarerevision.html
- document_id: `ni-rfpm-api-ref`
- page_type: `leaf`
- content_type: ``

Inherent IVI Properties:Instrument Identification:Firmware Revision Property

**Short Name:**Firmware Revision

Property of [niRFPMSwitch](cnirfpmswitch.html)

Returns a string that contains the firmware revision information for the NI-RFPMSwitch device you are currently using.

This property does not support the mmWave subsystem.

#### Remarks

The following table lists the characteristics of this property.

| Datatype |  |
| --- | --- |
| Permissions | Read Only |
| Resettable | No |

<!--NI_TOPIC bundle=ni-rfpm-api-ref path=rfpmswitchpropref/pnirfpmswitch_interchangecheck.html language=enus -->
## TOPIC 00160: Inherent IVI Properties:User Options:Interchange Check Property

- bundle_id: `ni-rfpm-api-ref`
- source_path: `rfpmswitchpropref/pnirfpmswitch_interchangecheck.html`
- source_url: https://docs-be.ni.com/bundle/ni-rfpm-api-ref/raw/resource/enus/rfpmswitchpropref/pnirfpmswitch_interchangecheck.html
- document_id: `ni-rfpm-api-ref`
- page_type: `leaf`
- content_type: ``

Inherent IVI Properties:User Options:Interchange Check Property

**Short Name:**Interchange Check

Property of [niRFPMSwitch](cnirfpmswitch.html)

Specifies whether to perform interchangeability checking and retrieve interchangeability warnings.

|  | Note This property is currently not supported. |
| --- | --- |

#### Remarks

The following table lists the characteristics of this property.

| Datatype |  |
| --- | --- |
| Permissions | Read/Write |
| Resettable | No |

<!--NI_TOPIC bundle=ni-rfpm-api-ref path=rfpmswitchpropref/pnirfpmswitch_ioresourcedescriptor.html language=enus -->
## TOPIC 00161: Inherent IVI Properties:Advanced Session Information:I/O Resource Descriptor Property

- bundle_id: `ni-rfpm-api-ref`
- source_path: `rfpmswitchpropref/pnirfpmswitch_ioresourcedescriptor.html`
- source_url: https://docs-be.ni.com/bundle/ni-rfpm-api-ref/raw/resource/enus/rfpmswitchpropref/pnirfpmswitch_ioresourcedescriptor.html
- document_id: `ni-rfpm-api-ref`
- page_type: `leaf`
- content_type: ``

Inherent IVI Properties:Advanced Session Information:I/O Resource Descriptor Property

**Short Name:**I/O Resource Descriptor

Property of [niRFPMSwitch](cnirfpmswitch.html)

Indicates the resource name NI-RFPMSwitch uses to identify the physical device. If you initialize NI-RFPMSwitch with a logical name, this property contains the resource name that corresponds to the entry in the IVI Configuration Utility.

If you initialize NI-RFPM Switch with the resource name, this property contains that value.

This property does not support the mmWave subsystem.

#### Remarks

The following table lists the characteristics of this property.

| Datatype |  |
| --- | --- |
| Permissions | Read Only |
| Resettable | No |

<!--NI_TOPIC bundle=ni-rfpm-api-ref path=rfpmswitchpropref/pnirfpmswitch_isconfigurationchannel.html language=enus -->
## TOPIC 00162: Inherent IVI Properties:Channel Configuration:Is Configuration Channel Property

- bundle_id: `ni-rfpm-api-ref`
- source_path: `rfpmswitchpropref/pnirfpmswitch_isconfigurationchannel.html`
- source_url: https://docs-be.ni.com/bundle/ni-rfpm-api-ref/raw/resource/enus/rfpmswitchpropref/pnirfpmswitch_isconfigurationchannel.html
- document_id: `ni-rfpm-api-ref`
- page_type: `leaf`
- content_type: ``

Inherent IVI Properties:Channel Configuration:Is Configuration Channel Property

**Short Name:**Is Configuration Channel

Property of [niRFPMSwitch](cnirfpmswitch.html)

Specifies whether to designate the channel as a configuration channel—a channel reserved for internal path creation. NI-RFPMSwitch uses configuration channels to create paths between the channels you specify in the [niRFPMSwitch Connect Channels](/csh?topicname=rfpmswitchviref/nirfpmswitch_connect_channels.html) VI.

This property does not support the mmWave subsystem.

#### Remarks

The following table lists the characteristics of this property.

| Datatype |  |
| --- | --- |
| Permissions | Read Only |
| Resettable | No |

<!--NI_TOPIC bundle=ni-rfpm-api-ref path=rfpmswitchpropref/pnirfpmswitch_isdebounced.html language=enus -->
## TOPIC 00163: Module Characteristics:Is Debounced Property

- bundle_id: `ni-rfpm-api-ref`
- source_path: `rfpmswitchpropref/pnirfpmswitch_isdebounced.html`
- source_url: https://docs-be.ni.com/bundle/ni-rfpm-api-ref/raw/resource/enus/rfpmswitchpropref/pnirfpmswitch_isdebounced.html
- document_id: `ni-rfpm-api-ref`
- page_type: `leaf`
- content_type: ``

Module Characteristics:Is Debounced Property

**Short Name:**Is Debounced

Property of [niRFPMSwitch](cnirfpmswitch.html)

Indicates whether the entire switch module has settled since the last switching command. A value of TRUE indicates that all signals going through the switch module are valid.

This property does not support the mmWave subsystem.

#### Remarks

The following table lists the characteristics of this property.

| Datatype |  |
| --- | --- |
| Permissions | Read Only |
| Resettable | No |

<!--NI_TOPIC bundle=ni-rfpm-api-ref path=rfpmswitchpropref/pnirfpmswitch_issourcechannel.html language=enus -->
## TOPIC 00164: Inherent IVI Properties:Channel Configuration:Is Source Channel Property

- bundle_id: `ni-rfpm-api-ref`
- source_path: `rfpmswitchpropref/pnirfpmswitch_issourcechannel.html`
- source_url: https://docs-be.ni.com/bundle/ni-rfpm-api-ref/raw/resource/enus/rfpmswitchpropref/pnirfpmswitch_issourcechannel.html
- document_id: `ni-rfpm-api-ref`
- page_type: `leaf`
- content_type: ``

Inherent IVI Properties:Channel Configuration:Is Source Channel Property

**Short Name:**Is Source Channel

Property of [niRFPMSwitch](cnirfpmswitch.html)

Specifies whether to designate the channel as a source channel.

This property does not support the mmWave subsystem.

Set this property to TRUE when you connect the channel to a power supply, a function generator, or an active measurement point on the unit under test, and you do not want to connect the channel to another source. NI-RFPMSwitch prevents source channels from connecting to each other. The [niRFPMSwitch Connect Channels](/csh?topicname=rfpmswitchviref/nirfpmswitch_connect_channels.html) VI returns the Attempt To Connect Sources error when you attempt to connect two channels that you identify as source channels.

#### Remarks

The following table lists the characteristics of this property.

| Datatype |  |
| --- | --- |
| Permissions | Read/Write |
| Resettable | No |

<!--NI_TOPIC bundle=ni-rfpm-api-ref path=rfpmswitchpropref/pnirfpmswitch_logicalname.html language=enus -->
## TOPIC 00165: Inherent IVI Properties:Advanced Session Information:Logical Name Property

- bundle_id: `ni-rfpm-api-ref`
- source_path: `rfpmswitchpropref/pnirfpmswitch_logicalname.html`
- source_url: https://docs-be.ni.com/bundle/ni-rfpm-api-ref/raw/resource/enus/rfpmswitchpropref/pnirfpmswitch_logicalname.html
- document_id: `ni-rfpm-api-ref`
- page_type: `leaf`
- content_type: ``

Inherent IVI Properties:Advanced Session Information:Logical Name Property

**Short Name:**Logical Name

Property of [niRFPMSwitch](cnirfpmswitch.html)

Contains the logical name you specified when opening the current IVI session. You may pass a logical name to the [niRFPMSwitch Initialize](/csh?topicname=rfpmswitchviref/nirfpmswitch_initialize.html) VI or the [niRFPMSwitch Initialize With Options](/csh?topicname=rfpmswitchviref/nirfpmswitch_initialize_with_options.html) VI. The IVI Configuration Utility must contain an entry for the logical name. The logical name entry refers to a driver session section in the IVI Configuration file. The driver session section specifies a physical device and initial user options.

This property does not support the mmWave subsystem.

#### Remarks

The following table lists the characteristics of this property.

| Datatype |  |
| --- | --- |
| Permissions | Read Only |
| Resettable | No |

<!--NI_TOPIC bundle=ni-rfpm-api-ref path=rfpmswitchpropref/pnirfpmswitch_manufacturer.html language=enus -->
## TOPIC 00166: Inherent IVI Properties:Instrument Identification:Manufacturer Property

- bundle_id: `ni-rfpm-api-ref`
- source_path: `rfpmswitchpropref/pnirfpmswitch_manufacturer.html`
- source_url: https://docs-be.ni.com/bundle/ni-rfpm-api-ref/raw/resource/enus/rfpmswitchpropref/pnirfpmswitch_manufacturer.html
- document_id: `ni-rfpm-api-ref`
- page_type: `leaf`
- content_type: ``

Inherent IVI Properties:Instrument Identification:Manufacturer Property

**Short Name:**Manufacturer

Property of [niRFPMSwitch](cnirfpmswitch.html)

Returns a string that contains the name of the manufacturer for the NI-RFPMSwitch device you are currently using.

This property does not support the mmWave subsystem.

#### Remarks

The following table lists the characteristics of this property.

| Datatype |  |
| --- | --- |
| Permissions | Read Only |
| Resettable | No |

<!--NI_TOPIC bundle=ni-rfpm-api-ref path=rfpmswitchpropref/pnirfpmswitch_model.html language=enus -->
## TOPIC 00167: Inherent IVI Properties:Instrument Identification:Model Property

- bundle_id: `ni-rfpm-api-ref`
- source_path: `rfpmswitchpropref/pnirfpmswitch_model.html`
- source_url: https://docs-be.ni.com/bundle/ni-rfpm-api-ref/raw/resource/enus/rfpmswitchpropref/pnirfpmswitch_model.html
- document_id: `ni-rfpm-api-ref`
- page_type: `leaf`
- content_type: ``

Inherent IVI Properties:Instrument Identification:Model Property

**Short Name:**Model

Property of [niRFPMSwitch](cnirfpmswitch.html)

Returns a string that contains the model number or name of the NI-RFPMSwitch device that you are currently using.

This property does not support the mmWave subsystem.

#### Remarks

The following table lists the characteristics of this property.

| Datatype |  |
| --- | --- |
| Permissions | Read Only |
| Resettable | No |

<!--NI_TOPIC bundle=ni-rfpm-api-ref path=rfpmswitchpropref/pnirfpmswitch_numberofexternalports.html language=enus -->
## TOPIC 00168: Device Information:Number of External Ports Property

- bundle_id: `ni-rfpm-api-ref`
- source_path: `rfpmswitchpropref/pnirfpmswitch_numberofexternalports.html`
- source_url: https://docs-be.ni.com/bundle/ni-rfpm-api-ref/raw/resource/enus/rfpmswitchpropref/pnirfpmswitch_numberofexternalports.html
- document_id: `ni-rfpm-api-ref`
- page_type: `leaf`
- content_type: ``

Device Information:Number of External Ports Property

**Short Name:**Number of External Ports

Property of [niRFPMSwitch](cnirfpmswitch.html)

Returns the number of ports that you are able to connect to the device under test (DUT).

This property does not support the mmWave subsystem.

#### Remarks

The following table lists the characteristics of this property.

| Datatype |  |
| --- | --- |
| Permissions | Read Only |
| Resettable | No |

<!--NI_TOPIC bundle=ni-rfpm-api-ref path=rfpmswitchpropref/pnirfpmswitch_portdaisychaindepth.html language=enus -->
## TOPIC 00169: Device Information:Port Daisy Chain Depth Property

- bundle_id: `ni-rfpm-api-ref`
- source_path: `rfpmswitchpropref/pnirfpmswitch_portdaisychaindepth.html`
- source_url: https://docs-be.ni.com/bundle/ni-rfpm-api-ref/raw/resource/enus/rfpmswitchpropref/pnirfpmswitch_portdaisychaindepth.html
- document_id: `ni-rfpm-api-ref`
- page_type: `leaf`
- content_type: ``

Device Information:Port Daisy Chain Depth Property

**Short Name:**Port Daisy Chain Depth

Property of [niRFPMSwitch](cnirfpmswitch.html)

Returns the daisy chain depth of the port that was specified with the active channel property.

This property does not support the mmWave subsystem.

#### Remarks

The following table lists the characteristics of this property.

| Datatype |  |
| --- | --- |
| Permissions | Read Only |
| Resettable | No |

<!--NI_TOPIC bundle=ni-rfpm-api-ref path=rfpmswitchpropref/pnirfpmswitch_porttype.html language=enus -->
## TOPIC 00170: Device Information:Port Type Property

- bundle_id: `ni-rfpm-api-ref`
- source_path: `rfpmswitchpropref/pnirfpmswitch_porttype.html`
- source_url: https://docs-be.ni.com/bundle/ni-rfpm-api-ref/raw/resource/enus/rfpmswitchpropref/pnirfpmswitch_porttype.html
- document_id: `ni-rfpm-api-ref`
- page_type: `leaf`
- content_type: ``

Device Information:Port Type Property

**Short Name:**Port Type

Property of [niRFPMSwitch](cnirfpmswitch.html)

Returns the type of the port that was specified with the active channel property.

This property does not support the mmWave subsystem.

#### Remarks

The following table lists the characteristics of this property.

| Datatype |  |
| --- | --- |
| Permissions | Read Only |
| Resettable | No |

<!--NI_TOPIC bundle=ni-rfpm-api-ref path=rfpmswitchpropref/pnirfpmswitch_queryinstrumentstatus.html language=enus -->
## TOPIC 00171: Inherent IVI Properties:User Options:Query Instrument Status Property

- bundle_id: `ni-rfpm-api-ref`
- source_path: `rfpmswitchpropref/pnirfpmswitch_queryinstrumentstatus.html`
- source_url: https://docs-be.ni.com/bundle/ni-rfpm-api-ref/raw/resource/enus/rfpmswitchpropref/pnirfpmswitch_queryinstrumentstatus.html
- document_id: `ni-rfpm-api-ref`
- page_type: `leaf`
- content_type: ``

Inherent IVI Properties:User Options:Query Instrument Status Property

**Short Name:**Query Instrument Status

Property of [niRFPMSwitch](cnirfpmswitch.html)

Specifies whether NI-RFPMSwitch queries the NI-RFPMSwitch device status after each operation. The default value is TRUE. Use the [niRFPMSwitch Initialize With Options](/csh?topicname=rfpmswitchviref/nirfpmswitch_initialize_with_options.html) VI to override this value.

This property does not support the mmWave subsystem.

Querying the device status is useful for debugging. After you validate your program, you can set this property to FALSE to disable status checking and maximize performance. NI-RFPMSwitch can choose to ignore status checking for particular properties, regardless of the setting of this property.

#### Remarks

The following table lists the characteristics of this property.

| Datatype |  |
| --- | --- |
| Permissions | Read/Write |
| Resettable | No |

<!--NI_TOPIC bundle=ni-rfpm-api-ref path=rfpmswitchpropref/pnirfpmswitch_rangecheck.html language=enus -->
## TOPIC 00172: Inherent IVI Properties:User Options:Range Check Property

- bundle_id: `ni-rfpm-api-ref`
- source_path: `rfpmswitchpropref/pnirfpmswitch_rangecheck.html`
- source_url: https://docs-be.ni.com/bundle/ni-rfpm-api-ref/raw/resource/enus/rfpmswitchpropref/pnirfpmswitch_rangecheck.html
- document_id: `ni-rfpm-api-ref`
- page_type: `leaf`
- content_type: ``

Inherent IVI Properties:User Options:Range Check Property

**Short Name:**Range Check

Property of [niRFPMSwitch](cnirfpmswitch.html)

Specifies whether to validate property values and VI parameters. The default value is TRUE. Use the [niRFPMSwitch Initialize With Options](/csh?topicname=rfpmswitchviref/nirfpmswitch_initialize_with_options.html) VI to override this value.

This property does not support the mmWave subsystem.

Set this property to TRUE to validate the parameter values that you pass to NI-RFPMSwitch VIs. Range checking parameters is useful for debugging. After you validate your program, you can set this property to FALSE to disable range checking and maximize performance.

#### Remarks

The following table lists the characteristics of this property.

| Datatype |  |
| --- | --- |
| Permissions | Read/Write |
| Resettable | No |

<!--NI_TOPIC bundle=ni-rfpm-api-ref path=rfpmswitchpropref/pnirfpmswitch_recordvaluecoercions.html language=enus -->
## TOPIC 00173: Inherent IVI Properties:User Options:Record Value Coercions Property

- bundle_id: `ni-rfpm-api-ref`
- source_path: `rfpmswitchpropref/pnirfpmswitch_recordvaluecoercions.html`
- source_url: https://docs-be.ni.com/bundle/ni-rfpm-api-ref/raw/resource/enus/rfpmswitchpropref/pnirfpmswitch_recordvaluecoercions.html
- document_id: `ni-rfpm-api-ref`
- page_type: `leaf`
- content_type: ``

Inherent IVI Properties:User Options:Record Value Coercions Property

**Short Name:**Record Value Coercions

Property of [niRFPMSwitch](cnirfpmswitch.html)

Specifies whether the IVI engine keeps a list of the value coercions it makes for properties with ViInt32 and ViReal64 datatypes.

|  | Note This property is currently not supported. |
| --- | --- |

#### Remarks

The following table lists the characteristics of this property.

| Datatype |  |
| --- | --- |
| Permissions | Read/Write |
| Resettable | No |

<!--NI_TOPIC bundle=ni-rfpm-api-ref path=rfpmswitchpropref/pnirfpmswitch_revision.html language=enus -->
## TOPIC 00174: Inherent IVI Properties:Driver Identification:Revision Property

- bundle_id: `ni-rfpm-api-ref`
- source_path: `rfpmswitchpropref/pnirfpmswitch_revision.html`
- source_url: https://docs-be.ni.com/bundle/ni-rfpm-api-ref/raw/resource/enus/rfpmswitchpropref/pnirfpmswitch_revision.html
- document_id: `ni-rfpm-api-ref`
- page_type: `leaf`
- content_type: ``

Inherent IVI Properties:Driver Identification:Revision Property

**Short Name:**Revision

Property of [niRFPMSwitch](cnirfpmswitch.html)

Returns a string that contains additional version information about NI-RFPMSwitch.

This property does not support the mmWave subsystem.

#### Remarks

The following table lists the characteristics of this property.

| Datatype |  |
| --- | --- |
| Permissions | Read Only |
| Resettable | No |

<!--NI_TOPIC bundle=ni-rfpm-api-ref path=rfpmswitchpropref/pnirfpmswitch_settlingtime.html language=enus -->
## TOPIC 00175: Module Characteristics:Settling Time Property

- bundle_id: `ni-rfpm-api-ref`
- source_path: `rfpmswitchpropref/pnirfpmswitch_settlingtime.html`
- source_url: https://docs-be.ni.com/bundle/ni-rfpm-api-ref/raw/resource/enus/rfpmswitchpropref/pnirfpmswitch_settlingtime.html
- document_id: `ni-rfpm-api-ref`
- page_type: `leaf`
- content_type: ``

Module Characteristics:Settling Time Property

**Short Name:**Settling Time

Property of [niRFPMSwitch](cnirfpmswitch.html)

Returns the maximum length of time, in seconds, from after you make a connection until the signal flowing through the channel settles.

This property does not support the mmWave subsystem.

#### Remarks

The following table lists the characteristics of this property.

| Datatype |  |
| --- | --- |
| Permissions | Read Only |
| Resettable | No |

<!--NI_TOPIC bundle=ni-rfpm-api-ref path=rfpmswitchpropref/pnirfpmswitch_simulate.html language=enus -->
## TOPIC 00176: Inherent IVI Properties:User Options:Simulate Property

- bundle_id: `ni-rfpm-api-ref`
- source_path: `rfpmswitchpropref/pnirfpmswitch_simulate.html`
- source_url: https://docs-be.ni.com/bundle/ni-rfpm-api-ref/raw/resource/enus/rfpmswitchpropref/pnirfpmswitch_simulate.html
- document_id: `ni-rfpm-api-ref`
- page_type: `leaf`
- content_type: ``

Inherent IVI Properties:User Options:Simulate Property

**Short Name:**Simulate

Property of [niRFPMSwitch](cnirfpmswitch.html)

Specifies whether to simulate NI-RFPMSwitch I/O operations. The default value is FALSE. Use the [niRFPMSwitch Initialize With Options](/csh?topicname=rfpmswitchviref/nirfpmswitch_initialize_with_options.html) VI to override this value.

This property does not support the mmWave subsystem.

This property is useful for debugging applications without using hardware. After a session is opened, you cannot change the simulation state. Use the [niRFPMSwitch Initialize With Options](/csh?topicname=rfpmswitchviref/nirfpmswitch_initialize_with_options.html) VI to enable simulation.

#### Remarks

The following table lists the characteristics of this property.

| Datatype |  |
| --- | --- |
| Permissions | Read Only |
| Resettable | No |

<!--NI_TOPIC bundle=ni-rfpm-api-ref path=rfpmswitchpropref/pnirfpmswitch_specificdrivercapabilities.html language=enus -->
## TOPIC 00177: Inherent IVI Properties:Driver Capabilities:Supported Instrument Models Property

- bundle_id: `ni-rfpm-api-ref`
- source_path: `rfpmswitchpropref/pnirfpmswitch_specificdrivercapabilities.html`
- source_url: https://docs-be.ni.com/bundle/ni-rfpm-api-ref/raw/resource/enus/rfpmswitchpropref/pnirfpmswitch_specificdrivercapabilities.html
- document_id: `ni-rfpm-api-ref`
- page_type: `leaf`
- content_type: ``

Inherent IVI Properties:Driver Capabilities:Supported Instrument Models Property

**Short Name:**Supported Instrument Models

Property of [niRFPMSwitch](cnirfpmswitch.html)

Returns a model code of the instrument. For specific drivers that support more than one device, this property returns a comma-separated list of supported instrument models.

This property does not support the mmWave subsystem.

#### Remarks

The following table lists the characteristics of this property.

| Datatype |  |
| --- | --- |
| Permissions | Read Only |
| Resettable | No |

<!--NI_TOPIC bundle=ni-rfpm-api-ref path=rfpmviref/calibration_pal.html language=enus -->
## TOPIC 00178: Calibration

- bundle_id: `ni-rfpm-api-ref`
- source_path: `rfpmviref/calibration_pal.html`
- source_url: https://docs-be.ni.com/bundle/ni-rfpm-api-ref/raw/resource/enus/rfpmviref/calibration_pal.html
- document_id: `ni-rfpm-api-ref`
- page_type: `leaf`
- content_type: ``

Calibration

Owning Palette:

NI-RFPM VIs

Installed With:

Use the NI-RFPM Calibration VIs to control calibration operations for the STS device.

| Palette Object | Description |
| --- | --- |
| NI-RFPM Close Calibration | Closes and commits or aborts the current calibration. This VI does not support the mmWave subsystem. |
| NI-RFPM Configure Calibration | Configures user calibration resources and options. This VI does not support the mmWave subsystem. |
| NI-RFPM Fetch Receiver Offset | Fetches the stored receiver offset for a single frequency, reference level, and path setting at a specified port. When NI-RFPM de-embedding is enabled, the reference level is defined at the DUT reference plane. This VI does not support the mmWave subsystem. |
| NI-RFPM Fetch Source Offset With Settings And Settling Time | Fetches the stored source offset and settling time for a single frequency, power, and path setting for a specified port. When the De-embedding Enabled property is set to TRUE and the De-embedding S2P Path property is set to the correct de-embedding files, the power level is defined at the DUT reference plane. This VI does not support the mmWave subsystem. |
| NI-RFPM Init Calibration | Initializes user or system calibration. This VI does not support the mmWave subsystem. |
| NI-RFPM Is Calibration Action Done | Checks the status of the current calibration action, and returns an estimate of completion progress as a percentage. This VI does not support the mmWave subsystem. |
| NI-RFPM Load Calibration and Configuration | Loads calibration and sweep setting data from a file. This VI does not support the mmWave subsystem. |
| NI-RFPM Perform Calibration Action | Performs one calibration action. This VI does not support the mmWave subsystem. |
| NI-RFPM Perform System Calibration | Performs a system calibration. This VI does not support the mmWave subsystem. |
| NI-RFPM Read Available User Calibration Information | Reads the available user calibration sweep name and port list, as well as date, time, and temperature for the specified sweep type. This VI does not support the mmWave subsystem. |
| NI-RFPM Read System Calibration Information | Returns information about what ports are calibrated, as well as date, time, and temperature, for the system calibration. This VI does not support the mmWave subsystem. |
| NI-RFPM Save Calibration and Configuration | Saves the current user calibration and configuration data. This VI does not support the mmWave subsystem. |
| NI-RFPM Wait Calibration Action Done | Waits for the last user calibration action to complete. If the calibration action does not complete before the specified timeout, this VI returns a timeout error. This VI does not support the mmWave subsystem. |
| NI-RFPM Is System Calibration Valid | Notifies the user if their system calibration is still valid. To be valid, a system calibration must be within the recommended calibration interval and the temperature of the VST must be near the temperature of the calibration. This VI does not support the mmWave subsystem. |
| NI-RFPM Get System Calibration Recommended Interval | Returns the number of months for which a system calibration is valid. This VI does not support the mmWave subsystem. |

<!--NI_TOPIC bundle=ni-rfpm-api-ref path=rfpmviref/configuration_pal.html language=enus -->
## TOPIC 00179: Configuration

- bundle_id: `ni-rfpm-api-ref`
- source_path: `rfpmviref/configuration_pal.html`
- source_url: https://docs-be.ni.com/bundle/ni-rfpm-api-ref/raw/resource/enus/rfpmviref/configuration_pal.html
- document_id: `ni-rfpm-api-ref`
- page_type: `leaf`
- content_type: ``

Configuration

Owning Palette:

NI-RFPM VIs

Installed With:

Use the NI-RFPM Configuration VIs to configure operations with your STS device.

| Palette Object | Description |
| --- | --- |
| NI-RFPM Configure Deembedding | Configures de-embedding for the specified port by providing an S-parameter (S2P) file of the network to de-embed. |
| NI-RFPM Load Sweep Settings | Loads a sweep settings configuration file into memory so that measurements are performed according to the sweeps defined in the file. |
| NI-RFPM Property Node | Gets (reads) or sets (writes) NI-RFPM properties. When you read a property, NI-RFPM analyzes the current configuration to return the coerced value for that property. Setting a property may transition the session to the Configuration state. |
| NI-RFPM Read Sweep Settings Information | Returns the number of ports and number of points associated with a sweep setting. |
| NI-RFPM Read Sweep Settings Names | Returns an array of the sweep names defined in the currently-loaded sweep settings files. |
| NI-RFPM Create Reference Level Port Extension S-parameter Table (S2P file) | Creates an S-parameter reference level port extension table for the port based on the specified S2P file. This VI does not support the RF subsystem. |
| NI-RFPM Select Reference Level Port Extension Table | Selects the reference level port extension table to apply to measurements made with the port. This VI does not support the RF subsystem. |
| NI-RFPM Delete Reference Level Port Extension Table | Deletes the selected reference level port extension table for a given port. This VI does not support the RF subsystem. |
| NI-RFPM Delete All Reference Level Port Extension Tables | Deletes all configured reference level port extension tables for the session. This VI does not support the RF subsystem. |

<!--NI_TOPIC bundle=ni-rfpm-api-ref path=rfpmviref/measurement_pal.html language=enus -->
## TOPIC 00180: Measurement

- bundle_id: `ni-rfpm-api-ref`
- source_path: `rfpmviref/measurement_pal.html`
- source_url: https://docs-be.ni.com/bundle/ni-rfpm-api-ref/raw/resource/enus/rfpmviref/measurement_pal.html
- document_id: `ni-rfpm-api-ref`
- page_type: `leaf`
- content_type: ``

Measurement

Owning Palette:

NI-RFPM VIs

Installed With:

Use the NI-RFPM Measurement VIs to control measurement operations with your STS device.

| Palette Object | Description |
| --- | --- |
| NI-RFPM Fetch Receiver Measurement | Fetches the formatted receiver measurement results of the last completed measurement. |
| NI-RFPM Fetch Single S-Parameter Measurement | Fetches a single S-parameter measurement result from the last completed measurement. |
| NI-RFPM Fetch S-parameter Measurements | Fetches all S-parameter measurement results from the last completed measurement. |
| NI-RFPM Initiate | Initiates a measurement as defined in the sweep settings configuration file. |
| NI-RFPM Wait For Measurement Done | Waits for the measurement to complete. If the measurement does not complete within the specified timeout, this VI returns a timeout error. |

<!--NI_TOPIC bundle=ni-rfpm-api-ref path=rfpmviref/ni-rfpm_abort.html language=enus -->
## TOPIC 00181: NI-RFPM Abort VI

- bundle_id: `ni-rfpm-api-ref`
- source_path: `rfpmviref/ni-rfpm_abort.html`
- source_url: https://docs-be.ni.com/bundle/ni-rfpm-api-ref/raw/resource/enus/rfpmviref/ni-rfpm_abort.html
- document_id: `ni-rfpm-api-ref`
- page_type: `leaf`
- content_type: ``

NI-RFPM Abort VI

Installed With:

Stops any measurement previously initiated by the [NI-RFPM Initiate](ni-rfpm_initiate.html) VI.

[IMAGE alt='NI-RFPM Abort' src='ni-rfpm_abort.gif']

|  | instrument handle identifies your instrument session. instrument handle is obtained from the NI-RFPM Init With Resources VI and identifies a particular instrument session. |
| --- | --- |
|  | The error in (no error) cluster can accept error information wired from VIs previously called. Use this information to decide if any functionality should be bypassed in the event of errors from other VIs. Right-click the error in (no error) control on the front panel and select Explain Error or Explain Warning from the shortcut menu for more information about the error. The status boolean is either TRUE (X) for an error, or FALSE (checkmark) for no error or a warning. The pop-up option Explain Error (or Explain Warning) gives more information about the error displayed. The code input identifies the error or warning. The pop-up option Explain Error (or Explain Warning) gives more information about the error displayed. The source string describes the origin of the error or warning. The pop-up option Explain Error (or Explain Warning) gives more information about the error displayed. |
|  | The status boolean is either TRUE (X) for an error, or FALSE (checkmark) for no error or a warning. The pop-up option Explain Error (or Explain Warning) gives more information about the error displayed. |
|  | The code input identifies the error or warning. The pop-up option Explain Error (or Explain Warning) gives more information about the error displayed. |
|  | The source string describes the origin of the error or warning. The pop-up option Explain Error (or Explain Warning) gives more information about the error displayed. |
|  | instrument handle out passes a reference to your instrument session to the next VI. instrument handle out is obtained from the NI-RFPM Init With Resources VI and identifies a particular instrument session. |
|  | The error out cluster passes error or warning information out of a VI to be used by other VIs. Use this information to decide if any functionality should be bypassed in the event of errors from other VIs. The status boolean is either TRUE (X) for an error, or FALSE (checkmark) for no error or a warning. The pop-up option Explain Error (or Explain Warning) gives more information about the error displayed. The code output identifies the error or warning. The pop-up option Explain Error (or Explain Warning) gives more information about the error displayed. The source string describes the origin of the error or warning. The pop-up option Explain Error (or Explain Warning) gives more information about the error displayed. |
|  | The status boolean is either TRUE (X) for an error, or FALSE (checkmark) for no error or a warning. The pop-up option Explain Error (or Explain Warning) gives more information about the error displayed. |
|  | The code output identifies the error or warning. The pop-up option Explain Error (or Explain Warning) gives more information about the error displayed. |
|  | The source string describes the origin of the error or warning. The pop-up option Explain Error (or Explain Warning) gives more information about the error displayed. |

<!--NI_TOPIC bundle=ni-rfpm-api-ref path=rfpmviref/ni-rfpm_close.html language=enus -->
## TOPIC 00182: NI-RFPM Close VI

- bundle_id: `ni-rfpm-api-ref`
- source_path: `rfpmviref/ni-rfpm_close.html`
- source_url: https://docs-be.ni.com/bundle/ni-rfpm-api-ref/raw/resource/enus/rfpmviref/ni-rfpm_close.html
- document_id: `ni-rfpm-api-ref`
- page_type: `leaf`
- content_type: ``

NI-RFPM Close VI

Installed With:

Closes the device session.

[IMAGE alt='NI-RFPM Close' src='ni-rfpm_close.gif']

|  | instrument handle identifies your instrument session. instrument handle is obtained from the NI-RFPM Init With Resources VI and identifies a particular instrument session. |
| --- | --- |
|  | The error in cluster can accept error information wired from VIs previously called. Use this information to decide if any functionality should be bypassed in the event of errors from other VIs. Right-click the error in control on the front panel and select Explain Error or Explain Warning from the shortcut menu for more information about the error. The status boolean is either TRUE (X) for an error, or FALSE (checkmark) for no error or a warning. The pop-up option Explain Error (or Explain Warning) gives more information about the error displayed. The code input identifies the error or warning. The pop-up option Explain Error (or Explain Warning) gives more information about the error displayed. The source string describes the origin of the error or warning. The pop-up option Explain Error (or Explain Warning) gives more information about the error displayed. |
|  | The status boolean is either TRUE (X) for an error, or FALSE (checkmark) for no error or a warning. The pop-up option Explain Error (or Explain Warning) gives more information about the error displayed. |
|  | The code input identifies the error or warning. The pop-up option Explain Error (or Explain Warning) gives more information about the error displayed. |
|  | The source string describes the origin of the error or warning. The pop-up option Explain Error (or Explain Warning) gives more information about the error displayed. |
|  | The error out cluster passes error or warning information out of a VI to be used by other VIs. Use this information to decide if any functionality should be bypassed in the event of errors from other VIs. The status boolean is either TRUE (X) for an error, or FALSE (checkmark) for no error or a warning. The pop-up option Explain Error (or Explain Warning) gives more information about the error displayed. The code output identifies the error or warning. The pop-up option Explain Error (or Explain Warning) gives more information about the error displayed. The source string describes the origin of the error or warning. The pop-up option Explain Error (or Explain Warning) gives more information about the error displayed. |
|  | The status boolean is either TRUE (X) for an error, or FALSE (checkmark) for no error or a warning. The pop-up option Explain Error (or Explain Warning) gives more information about the error displayed. |
|  | The code output identifies the error or warning. The pop-up option Explain Error (or Explain Warning) gives more information about the error displayed. |
|  | The source string describes the origin of the error or warning. The pop-up option Explain Error (or Explain Warning) gives more information about the error displayed. |

<!--NI_TOPIC bundle=ni-rfpm-api-ref path=rfpmviref/ni-rfpm_close_calibration.html language=enus -->
## TOPIC 00183: NI-RFPM Close Calibration VI

- bundle_id: `ni-rfpm-api-ref`
- source_path: `rfpmviref/ni-rfpm_close_calibration.html`
- source_url: https://docs-be.ni.com/bundle/ni-rfpm-api-ref/raw/resource/enus/rfpmviref/ni-rfpm_close_calibration.html
- document_id: `ni-rfpm-api-ref`
- page_type: `leaf`
- content_type: ``

NI-RFPM Close Calibration VI

Installed With:

Closes and commits or aborts the current calibration.

This VI does not support the mmWave subsystem.

[IMAGE alt='NI-RFPM Close Calibration' src='ni-rfpm_close_calibration.gif']

|  | instrument handle identifies your instrument session. instrument handle is obtained from the NI-RFPM Init With Resources VI and identifies a particular instrument session. |
| --- | --- |
|  | Action specifies the action to perform when closing the user calibration. Abort NI-RFPM discards the calibration constants calculated during the calibration or aborts an ongoing calibration action. Commit NI-RFPM commits the calibration constants to the device. |
| Abort | NI-RFPM discards the calibration constants calculated during the calibration or aborts an ongoing calibration action. |
| Commit | NI-RFPM commits the calibration constants to the device. |
|  | The error in cluster can accept error information wired from VIs previously called. Use this information to decide if any functionality should be bypassed in the event of errors from other VIs. Right-click the error in control on the front panel and select Explain Error or Explain Warning from the shortcut menu for more information about the error. The status boolean is either TRUE (X) for an error, or FALSE (checkmark) for no error or a warning. The pop-up option Explain Error (or Explain Warning) gives more information about the error displayed. The code input identifies the error or warning. The pop-up option Explain Error (or Explain Warning) gives more information about the error displayed. The source string describes the origin of the error or warning. The pop-up option Explain Error (or Explain Warning) gives more information about the error displayed. |
|  | The status boolean is either TRUE (X) for an error, or FALSE (checkmark) for no error or a warning. The pop-up option Explain Error (or Explain Warning) gives more information about the error displayed. |
|  | The code input identifies the error or warning. The pop-up option Explain Error (or Explain Warning) gives more information about the error displayed. |
|  | The source string describes the origin of the error or warning. The pop-up option Explain Error (or Explain Warning) gives more information about the error displayed. |
|  | instrument handle out passes a reference to your instrument session to the next VI. instrument handle out is obtained from the NI-RFPM Init With Resources VI and identifies a particular instrument session. |
|  | The error out cluster passes error or warning information out of a VI to be used by other VIs. Use this information to decide if any functionality should be bypassed in the event of errors from other VIs. The status boolean is either TRUE (X) for an error, or FALSE (checkmark) for no error or a warning. The pop-up option Explain Error (or Explain Warning) gives more information about the error displayed. The code output identifies the error or warning. The pop-up option Explain Error (or Explain Warning) gives more information about the error displayed. The source string describes the origin of the error or warning. The pop-up option Explain Error (or Explain Warning) gives more information about the error displayed. |
|  | The status boolean is either TRUE (X) for an error, or FALSE (checkmark) for no error or a warning. The pop-up option Explain Error (or Explain Warning) gives more information about the error displayed. |
|  | The code output identifies the error or warning. The pop-up option Explain Error (or Explain Warning) gives more information about the error displayed. |
|  | The source string describes the origin of the error or warning. The pop-up option Explain Error (or Explain Warning) gives more information about the error displayed. |

<!--NI_TOPIC bundle=ni-rfpm-api-ref path=rfpmviref/ni-rfpm_configure_calibration.html language=enus -->
## TOPIC 00184: NI-RFPM Configure Calibration VI

- bundle_id: `ni-rfpm-api-ref`
- source_path: `rfpmviref/ni-rfpm_configure_calibration.html`
- source_url: https://docs-be.ni.com/bundle/ni-rfpm-api-ref/raw/resource/enus/rfpmviref/ni-rfpm_configure_calibration.html
- document_id: `ni-rfpm-api-ref`
- page_type: `leaf`
- content_type: ``

NI-RFPM Configure Calibration VI

Installed With:

Configures user calibration resources and options.

This VI does not support the mmWave subsystem.

[IMAGE alt='NI-RFPM Configure Calibration' src='ni-rfpm_configure_calibration.gif']

|  | instrument handle identifies your instrument session. instrument handle is obtained from the NI-RFPM Init With Resources VI and identifies a particular instrument session. |
| --- | --- |
|  | Autocal Device Resource specifies the resource name for the calibration device. When not specified or when a blank string is passed, NI-RFPM will try to detect the NI Automatic RF Calibration Module automatically. In a case where several NI Automatic RF Calibration Modules are connected to the same system controller, you must specify the resource of the NI Automatic RF Calibration Module to use. |
|  | Absolute Vector Calibration Enabled specifies whether NI-RFPM collects absolute vector calibration information or relative calibration information. The default value is true, and you do not have to set this based on sweep type. This parameter is only relevant for performing a calibration on a vector sweep setting. In source and receiver sweeps NI-RFPM ignores this. True NI-RFPM collects absolute vector calibration information. False NI-RFPM collects relative vector calibration information. |
| True | NI-RFPM collects absolute vector calibration information. |
| False | NI-RFPM collects relative vector calibration information. |
|  | Source Scalar Calibration Enabled specifies whether NI-RFPM collects source scalar offsets. The default value is true, and you do not have to set this based on sweep type. If this is set to true during a vector calibration, then NI-RFPM will also perform a source calibration. When performing a source calibration, this must be set to true or the driver errors out. This setting is ignored during receiver calibrations. |
|  | The error in (no error) cluster can accept error information wired from VIs previously called. Use this information to decide if any functionality should be bypassed in the event of errors from other VIs. Right-click the error in (no error) control on the front panel and select Explain Error or Explain Warning from the shortcut menu for more information about the error. The status boolean is either TRUE (X) for an error, or FALSE (checkmark) for no error or a warning. The pop-up option Explain Error (or Explain Warning) gives more information about the error displayed. The code input identifies the error or warning. The pop-up option Explain Error (or Explain Warning) gives more information about the error displayed. The source string describes the origin of the error or warning. The pop-up option Explain Error (or Explain Warning) gives more information about the error displayed. |
|  | The status boolean is either TRUE (X) for an error, or FALSE (checkmark) for no error or a warning. The pop-up option Explain Error (or Explain Warning) gives more information about the error displayed. |
|  | The code input identifies the error or warning. The pop-up option Explain Error (or Explain Warning) gives more information about the error displayed. |
|  | The source string describes the origin of the error or warning. The pop-up option Explain Error (or Explain Warning) gives more information about the error displayed. |
|  | Receiver Scalar Calibration Enabled specifies whether NI-RFPM collects receiver scalar offsets. The default value is true and must be set to true during receiver sweeps or else the driver will error out. During vector and source sweeps this is ignored. You do not have to set this based on sweep type. |
|  | instrument handle out passes a reference to your instrument session to the next VI. instrument handle out is obtained from the NI-RFPM Init With Resources VI and identifies a particular instrument session. |
|  | The error out cluster passes error or warning information out of a VI to be used by other VIs. Use this information to decide if any functionality should be bypassed in the event of errors from other VIs. The status boolean is either TRUE (X) for an error, or FALSE (checkmark) for no error or a warning. The pop-up option Explain Error (or Explain Warning) gives more information about the error displayed. The code output identifies the error or warning. The pop-up option Explain Error (or Explain Warning) gives more information about the error displayed. The source string describes the origin of the error or warning. The pop-up option Explain Error (or Explain Warning) gives more information about the error displayed. |
|  | The status boolean is either TRUE (X) for an error, or FALSE (checkmark) for no error or a warning. The pop-up option Explain Error (or Explain Warning) gives more information about the error displayed. |
|  | The code output identifies the error or warning. The pop-up option Explain Error (or Explain Warning) gives more information about the error displayed. |
|  | The source string describes the origin of the error or warning. The pop-up option Explain Error (or Explain Warning) gives more information about the error displayed. |

<!--NI_TOPIC bundle=ni-rfpm-api-ref path=rfpmviref/ni-rfpm_configure_deembedding.html language=enus -->
## TOPIC 00185: NI-RFPM Configure Deembedding VI

- bundle_id: `ni-rfpm-api-ref`
- source_path: `rfpmviref/ni-rfpm_configure_deembedding.html`
- source_url: https://docs-be.ni.com/bundle/ni-rfpm-api-ref/raw/resource/enus/rfpmviref/ni-rfpm_configure_deembedding.html
- document_id: `ni-rfpm-api-ref`
- page_type: `leaf`
- content_type: ``

NI-RFPM Configure Deembedding VI

Installed With:

Configures de-embedding for the specified port by providing an S-parameter (S2P) file of the network to de-embed.

[IMAGE alt='NI-RFPM Configure Deembedding' src='ni-rfpm_configure_deembedding.gif']

|  | port specifies the port to configure de-embedding for. |
| --- | --- |
|  | instrument handle identifies your instrument session. instrument handle is obtained from the NI-RFPM Init With Resources VI and identifies a particular instrument session. |
|  | Deembedding S2P File Path specifies the path to the 2-port Touchstone file (S2P) that contains de-embedding information for the specified port. |
|  | Deembedding Orientation specifies the orientation of the data in the S2P file relative to the port you specify. S2P Port1 Towards DUT Port 1 of the S2P is oriented towards the DUT. S2P Port2 Towards DUT Port 2 of the S2P is oriented towards the DUT. |
| S2P Port1 Towards DUT | Port 1 of the S2P is oriented towards the DUT. |
| S2P Port2 Towards DUT | Port 2 of the S2P is oriented towards the DUT. |
|  | The error in (no error) cluster can accept error information wired from VIs previously called. Use this information to decide if any functionality should be bypassed in the event of errors from other VIs. Right-click the error in (no error) control on the front panel and select Explain Error or Explain Warning from the shortcut menu for more information about the error. The status boolean is either TRUE (X) for an error, or FALSE (checkmark) for no error or a warning. The pop-up option Explain Error (or Explain Warning) gives more information about the error displayed. The code input identifies the error or warning. The pop-up option Explain Error (or Explain Warning) gives more information about the error displayed. The source string describes the origin of the error or warning. The pop-up option Explain Error (or Explain Warning) gives more information about the error displayed. |
|  | The status boolean is either TRUE (X) for an error, or FALSE (checkmark) for no error or a warning. The pop-up option Explain Error (or Explain Warning) gives more information about the error displayed. |
|  | The code input identifies the error or warning. The pop-up option Explain Error (or Explain Warning) gives more information about the error displayed. |
|  | The source string describes the origin of the error or warning. The pop-up option Explain Error (or Explain Warning) gives more information about the error displayed. |
|  | instrument handle out passes a reference to your instrument session to the next VI. instrument handle out is obtained from the NI-RFPM Init With Resources VI and identifies a particular instrument session. |
|  | The error out cluster passes error or warning information out of a VI to be used by other VIs. Use this information to decide if any functionality should be bypassed in the event of errors from other VIs. The status boolean is either TRUE (X) for an error, or FALSE (checkmark) for no error or a warning. The pop-up option Explain Error (or Explain Warning) gives more information about the error displayed. The code output identifies the error or warning. The pop-up option Explain Error (or Explain Warning) gives more information about the error displayed. The source string describes the origin of the error or warning. The pop-up option Explain Error (or Explain Warning) gives more information about the error displayed. |
|  | The status boolean is either TRUE (X) for an error, or FALSE (checkmark) for no error or a warning. The pop-up option Explain Error (or Explain Warning) gives more information about the error displayed. |
|  | The code output identifies the error or warning. The pop-up option Explain Error (or Explain Warning) gives more information about the error displayed. |
|  | The source string describes the origin of the error or warning. The pop-up option Explain Error (or Explain Warning) gives more information about the error displayed. |

<!--NI_TOPIC bundle=ni-rfpm-api-ref path=rfpmviref/ni-rfpm_create_reference_level_port_extension_s_parameter_table_s2p_file.html language=enus -->
## TOPIC 00186: NI-RFPM Create Reference Level Port Extension S-parameter Table (S2P file) VI

- bundle_id: `ni-rfpm-api-ref`
- source_path: `rfpmviref/ni-rfpm_create_reference_level_port_extension_s_parameter_table_s2p_file.html`
- source_url: https://docs-be.ni.com/bundle/ni-rfpm-api-ref/raw/resource/enus/rfpmviref/ni-rfpm_create_reference_level_port_extension_s_parameter_table_s2p_file.html
- document_id: `ni-rfpm-api-ref`
- page_type: `leaf`
- content_type: ``

NI-RFPM Create Reference Level Port Extension S-parameter Table (S2P file) VI

Installed With:

Creates an S-parameter reference level port extension table for the port based on the specified S2P file.

This VI does not support the RF subsystem.

[IMAGE alt='NI-RFPM Create Reference Level Port Extension S-parameter Table (S2P file)' src='ni-rfpm_create_reference_level_port_extension_s-parameter_table_(s2p_file).gif']

|  | instrument handle identifies your instrument session. instrument handle is obtained from the NI-RFPM Init With Resources VI and identifies a particular instrument session. |
| --- | --- |
|  | port specifies the port to create the reference level port extension S-parameter table for. |
|  | table name specifies the name of the S-parameter table. |
|  | S2P file Path specifies the path to the 2-port Touchstone file (S2P) that contains s-parameter information for the specified port. |
|  | The error in (no error) cluster can accept error information wired from VIs previously called. Use this information to decide if any functionality should be bypassed in the event of errors from other VIs. Right-click the error in (no error) control on the front panel and select Explain Error or Explain Warning from the shortcut menu for more information about the error. The status boolean is either TRUE (X) for an error, or FALSE (checkmark) for no error or a warning. The pop-up option Explain Error (or Explain Warning) gives more information about the error displayed. The code input identifies the error or warning. The pop-up option Explain Error (or Explain Warning) gives more information about the error displayed. The source string describes the origin of the error or warning. The pop-up option Explain Error (or Explain Warning) gives more information about the error displayed. |
|  | The status boolean is either TRUE (X) for an error, or FALSE (checkmark) for no error or a warning. The pop-up option Explain Error (or Explain Warning) gives more information about the error displayed. |
|  | The code input identifies the error or warning. The pop-up option Explain Error (or Explain Warning) gives more information about the error displayed. |
|  | The source string describes the origin of the error or warning. The pop-up option Explain Error (or Explain Warning) gives more information about the error displayed. |
|  | S-parameters orientation specifies the orientation of the data in the S2P file relative to the port you specify. S2P Port1 Towards DUT Port 1 of the S2P is oriented towards the DUT. S2P Port2 Towards DUT Port 2 of the S2P is oriented towards the DUT. |
| S2P Port1 Towards DUT | Port 1 of the S2P is oriented towards the DUT. |
| S2P Port2 Towards DUT | Port 2 of the S2P is oriented towards the DUT. |
|  | instrument handle out passes a reference to your instrument session to the next VI. instrument handle out is obtained from the NI-RFPM Init With Resources VI and identifies a particular instrument session. |
|  | The error out cluster passes error or warning information out of a VI to be used by other VIs. Use this information to decide if any functionality should be bypassed in the event of errors from other VIs. The status boolean is either TRUE (X) for an error, or FALSE (checkmark) for no error or a warning. The pop-up option Explain Error (or Explain Warning) gives more information about the error displayed. The code output identifies the error or warning. The pop-up option Explain Error (or Explain Warning) gives more information about the error displayed. The source string describes the origin of the error or warning. The pop-up option Explain Error (or Explain Warning) gives more information about the error displayed. |
|  | The status boolean is either TRUE (X) for an error, or FALSE (checkmark) for no error or a warning. The pop-up option Explain Error (or Explain Warning) gives more information about the error displayed. |
|  | The code output identifies the error or warning. The pop-up option Explain Error (or Explain Warning) gives more information about the error displayed. |
|  | The source string describes the origin of the error or warning. The pop-up option Explain Error (or Explain Warning) gives more information about the error displayed. |

<!--NI_TOPIC bundle=ni-rfpm-api-ref path=rfpmviref/ni-rfpm_delete_all_reference_level_port_extension_tables.html language=enus -->
## TOPIC 00187: NI-RFPM Delete All Reference Level Port Extension Tables VI

- bundle_id: `ni-rfpm-api-ref`
- source_path: `rfpmviref/ni-rfpm_delete_all_reference_level_port_extension_tables.html`
- source_url: https://docs-be.ni.com/bundle/ni-rfpm-api-ref/raw/resource/enus/rfpmviref/ni-rfpm_delete_all_reference_level_port_extension_tables.html
- document_id: `ni-rfpm-api-ref`
- page_type: `leaf`
- content_type: ``

NI-RFPM Delete All Reference Level Port Extension Tables VI

Installed With:

Deletes all configured reference level port extension tables for the session.

This VI does not support the RF subsystem.

[IMAGE alt='NI-RFPM Delete All Reference Level Port Extension Tables' src='ni-rfpm_delete_all_reference_level_port_extension_tables.gif']

|  | instrument handle identifies your instrument session. instrument handle is obtained from the NI-RFPM Init With Resources VI and identifies a particular instrument session. |
| --- | --- |
|  | The error in (no error) cluster can accept error information wired from VIs previously called. Use this information to decide if any functionality should be bypassed in the event of errors from other VIs. Right-click the error in (no error) control on the front panel and select Explain Error or Explain Warning from the shortcut menu for more information about the error. The status boolean is either TRUE (X) for an error, or FALSE (checkmark) for no error or a warning. The pop-up option Explain Error (or Explain Warning) gives more information about the error displayed. The code input identifies the error or warning. The pop-up option Explain Error (or Explain Warning) gives more information about the error displayed. The source string describes the origin of the error or warning. The pop-up option Explain Error (or Explain Warning) gives more information about the error displayed. |
|  | The status boolean is either TRUE (X) for an error, or FALSE (checkmark) for no error or a warning. The pop-up option Explain Error (or Explain Warning) gives more information about the error displayed. |
|  | The code input identifies the error or warning. The pop-up option Explain Error (or Explain Warning) gives more information about the error displayed. |
|  | The source string describes the origin of the error or warning. The pop-up option Explain Error (or Explain Warning) gives more information about the error displayed. |
|  | instrument handle out passes a reference to your instrument session to the next VI. instrument handle out is obtained from the NI-RFPM Init With Resources VI and identifies a particular instrument session. |
|  | The error out cluster passes error or warning information out of a VI to be used by other VIs. Use this information to decide if any functionality should be bypassed in the event of errors from other VIs. The status boolean is either TRUE (X) for an error, or FALSE (checkmark) for no error or a warning. The pop-up option Explain Error (or Explain Warning) gives more information about the error displayed. The code output identifies the error or warning. The pop-up option Explain Error (or Explain Warning) gives more information about the error displayed. The source string describes the origin of the error or warning. The pop-up option Explain Error (or Explain Warning) gives more information about the error displayed. |
|  | The status boolean is either TRUE (X) for an error, or FALSE (checkmark) for no error or a warning. The pop-up option Explain Error (or Explain Warning) gives more information about the error displayed. |
|  | The code output identifies the error or warning. The pop-up option Explain Error (or Explain Warning) gives more information about the error displayed. |
|  | The source string describes the origin of the error or warning. The pop-up option Explain Error (or Explain Warning) gives more information about the error displayed. |

<!--NI_TOPIC bundle=ni-rfpm-api-ref path=rfpmviref/ni-rfpm_delete_reference_level_port_extension_table.html language=enus -->
## TOPIC 00188: NI-RFPM Delete Reference Level Port Extension Table VI

- bundle_id: `ni-rfpm-api-ref`
- source_path: `rfpmviref/ni-rfpm_delete_reference_level_port_extension_table.html`
- source_url: https://docs-be.ni.com/bundle/ni-rfpm-api-ref/raw/resource/enus/rfpmviref/ni-rfpm_delete_reference_level_port_extension_table.html
- document_id: `ni-rfpm-api-ref`
- page_type: `leaf`
- content_type: ``

NI-RFPM Delete Reference Level Port Extension Table VI

Installed With:

Deletes the selected reference level port extension table for a given port.

This VI does not support the RF subsystem.

[IMAGE alt='NI-RFPM Delete Reference Level Port Extension Table' src='ni-rfpm_delete_reference_level_port_extension_table.gif']

|  | instrument handle identifies your instrument session. instrument handle is obtained from the NI-RFPM Init With Resources VI and identifies a particular instrument session. |
| --- | --- |
|  | port specifies the port to create the reference level port extension S-parameter table for. |
|  | table name specifies the name of the S-parameter table. |
|  | The error in (no error) cluster can accept error information wired from VIs previously called. Use this information to decide if any functionality should be bypassed in the event of errors from other VIs. Right-click the error in (no error) control on the front panel and select Explain Error or Explain Warning from the shortcut menu for more information about the error. The status boolean is either TRUE (X) for an error, or FALSE (checkmark) for no error or a warning. The pop-up option Explain Error (or Explain Warning) gives more information about the error displayed. The code input identifies the error or warning. The pop-up option Explain Error (or Explain Warning) gives more information about the error displayed. The source string describes the origin of the error or warning. The pop-up option Explain Error (or Explain Warning) gives more information about the error displayed. |
|  | The status boolean is either TRUE (X) for an error, or FALSE (checkmark) for no error or a warning. The pop-up option Explain Error (or Explain Warning) gives more information about the error displayed. |
|  | The code input identifies the error or warning. The pop-up option Explain Error (or Explain Warning) gives more information about the error displayed. |
|  | The source string describes the origin of the error or warning. The pop-up option Explain Error (or Explain Warning) gives more information about the error displayed. |
|  | instrument handle out passes a reference to your instrument session to the next VI. instrument handle out is obtained from the NI-RFPM Init With Resources VI and identifies a particular instrument session. |
|  | The error out cluster passes error or warning information out of a VI to be used by other VIs. Use this information to decide if any functionality should be bypassed in the event of errors from other VIs. The status boolean is either TRUE (X) for an error, or FALSE (checkmark) for no error or a warning. The pop-up option Explain Error (or Explain Warning) gives more information about the error displayed. The code output identifies the error or warning. The pop-up option Explain Error (or Explain Warning) gives more information about the error displayed. The source string describes the origin of the error or warning. The pop-up option Explain Error (or Explain Warning) gives more information about the error displayed. |
|  | The status boolean is either TRUE (X) for an error, or FALSE (checkmark) for no error or a warning. The pop-up option Explain Error (or Explain Warning) gives more information about the error displayed. |
|  | The code output identifies the error or warning. The pop-up option Explain Error (or Explain Warning) gives more information about the error displayed. |
|  | The source string describes the origin of the error or warning. The pop-up option Explain Error (or Explain Warning) gives more information about the error displayed. |

<!--NI_TOPIC bundle=ni-rfpm-api-ref path=rfpmviref/ni-rfpm_disconnect_all_paths.html language=enus -->
## TOPIC 00189: NI-RFPM Disconnect All Paths VI

- bundle_id: `ni-rfpm-api-ref`
- source_path: `rfpmviref/ni-rfpm_disconnect_all_paths.html`
- source_url: https://docs-be.ni.com/bundle/ni-rfpm-api-ref/raw/resource/enus/rfpmviref/ni-rfpm_disconnect_all_paths.html
- document_id: `ni-rfpm-api-ref`
- page_type: `leaf`
- content_type: ``

NI-RFPM Disconnect All Paths VI

Installed With:

Disconnects all existing paths in the underlying switch session that was passed into the [NI-RFPM Init With Resources](ni-rfpm_init_with_resources.html) VI.

This VI does not support the mmWave subsystem.

[IMAGE alt='NI-RFPM Disconnect All Paths' src='ni-rfpm_disconnect_all_paths.gif']

|  | instrument handle identifies your instrument session. instrument handle is obtained from the NI-RFPM Init With Resources VI and identifies a particular instrument session. |
| --- | --- |
|  | The error in (no error) cluster can accept error information wired from VIs previously called. Use this information to decide if any functionality should be bypassed in the event of errors from other VIs. Right-click the error in (no error) control on the front panel and select Explain Error or Explain Warning from the shortcut menu for more information about the error. The status boolean is either TRUE (X) for an error, or FALSE (checkmark) for no error or a warning. The pop-up option Explain Error (or Explain Warning) gives more information about the error displayed. The code input identifies the error or warning. The pop-up option Explain Error (or Explain Warning) gives more information about the error displayed. The source string describes the origin of the error or warning. The pop-up option Explain Error (or Explain Warning) gives more information about the error displayed. |
|  | The status boolean is either TRUE (X) for an error, or FALSE (checkmark) for no error or a warning. The pop-up option Explain Error (or Explain Warning) gives more information about the error displayed. |
|  | The code input identifies the error or warning. The pop-up option Explain Error (or Explain Warning) gives more information about the error displayed. |
|  | The source string describes the origin of the error or warning. The pop-up option Explain Error (or Explain Warning) gives more information about the error displayed. |
|  | Timeout specifies the time to wait for the operation to complete before returning an error, expressed in seconds. |
|  | instrument handle out passes a reference to your instrument session to the next VI. instrument handle out is obtained from the NI-RFPM Init With Resources VI and identifies a particular instrument session. |
|  | The error out cluster passes error or warning information out of a VI to be used by other VIs. Use this information to decide if any functionality should be bypassed in the event of errors from other VIs. The status boolean is either TRUE (X) for an error, or FALSE (checkmark) for no error or a warning. The pop-up option Explain Error (or Explain Warning) gives more information about the error displayed. The code output identifies the error or warning. The pop-up option Explain Error (or Explain Warning) gives more information about the error displayed. The source string describes the origin of the error or warning. The pop-up option Explain Error (or Explain Warning) gives more information about the error displayed. |
|  | The status boolean is either TRUE (X) for an error, or FALSE (checkmark) for no error or a warning. The pop-up option Explain Error (or Explain Warning) gives more information about the error displayed. |
|  | The code output identifies the error or warning. The pop-up option Explain Error (or Explain Warning) gives more information about the error displayed. |
|  | The source string describes the origin of the error or warning. The pop-up option Explain Error (or Explain Warning) gives more information about the error displayed. |

<!--NI_TOPIC bundle=ni-rfpm-api-ref path=rfpmviref/ni-rfpm_error_query.html language=enus -->
## TOPIC 00190: NI-RFPM Error Query VI

- bundle_id: `ni-rfpm-api-ref`
- source_path: `rfpmviref/ni-rfpm_error_query.html`
- source_url: https://docs-be.ni.com/bundle/ni-rfpm-api-ref/raw/resource/enus/rfpmviref/ni-rfpm_error_query.html
- document_id: `ni-rfpm-api-ref`
- page_type: `leaf`
- content_type: ``

NI-RFPM Error Query VI

Installed With:

Converts an **error code** returned by an NI-RFPM VI into a user-readable string.

[IMAGE alt='NI-RFPM Error Query' src='ni-rfpm_error_query.gif']

|  | instrument handle identifies your instrument session. instrument handle is obtained from the NI-RFPM Init With Resources VI and identifies a particular instrument session. |
| --- | --- |
|  | error code passes the status code that is returned from any NI-RFPM VIs. The default value is 0. |
|  | The error in cluster can accept error information wired from VIs previously called. Use this information to decide if any functionality should be bypassed in the event of errors from other VIs. Right-click the error in control on the front panel and select Explain Error or Explain Warning from the shortcut menu for more information about the error. The status boolean is either TRUE (X) for an error, or FALSE (checkmark) for no error or a warning. The pop-up option Explain Error (or Explain Warning) gives more information about the error displayed. The code input identifies the error or warning. The pop-up option Explain Error (or Explain Warning) gives more information about the error displayed. The source string describes the origin of the error or warning. The pop-up option Explain Error (or Explain Warning) gives more information about the error displayed. |
|  | The status boolean is either TRUE (X) for an error, or FALSE (checkmark) for no error or a warning. The pop-up option Explain Error (or Explain Warning) gives more information about the error displayed. |
|  | The code input identifies the error or warning. The pop-up option Explain Error (or Explain Warning) gives more information about the error displayed. |
|  | The source string describes the origin of the error or warning. The pop-up option Explain Error (or Explain Warning) gives more information about the error displayed. |
|  | instrument handle out passes a reference to your instrument session to the next VI. instrument handle out is obtained from the NI-RFPM Init With Resources VI and identifies a particular instrument session. |
|  | error message returns the user-readable message string that corresponds to the status code specified in error code. |
|  | The error out cluster passes error or warning information out of a VI to be used by other VIs. Use this information to decide if any functionality should be bypassed in the event of errors from other VIs. The status boolean is either TRUE (X) for an error, or FALSE (checkmark) for no error or a warning. The pop-up option Explain Error (or Explain Warning) gives more information about the error displayed. The code output identifies the error or warning. The pop-up option Explain Error (or Explain Warning) gives more information about the error displayed. The source string describes the origin of the error or warning. The pop-up option Explain Error (or Explain Warning) gives more information about the error displayed. |
|  | The status boolean is either TRUE (X) for an error, or FALSE (checkmark) for no error or a warning. The pop-up option Explain Error (or Explain Warning) gives more information about the error displayed. |
|  | The code output identifies the error or warning. The pop-up option Explain Error (or Explain Warning) gives more information about the error displayed. |
|  | The source string describes the origin of the error or warning. The pop-up option Explain Error (or Explain Warning) gives more information about the error displayed. |

<!--NI_TOPIC bundle=ni-rfpm-api-ref path=rfpmviref/ni-rfpm_fetch_receiver_measurement.html language=enus -->
## TOPIC 00191: NI-RFPM Fetch Receiver Measurement VI

- bundle_id: `ni-rfpm-api-ref`
- source_path: `rfpmviref/ni-rfpm_fetch_receiver_measurement.html`
- source_url: https://docs-be.ni.com/bundle/ni-rfpm-api-ref/raw/resource/enus/rfpmviref/ni-rfpm_fetch_receiver_measurement.html
- document_id: `ni-rfpm-api-ref`
- page_type: `leaf`
- content_type: ``

NI-RFPM Fetch Receiver Measurement VI

Installed With:

Fetches the formatted receiver measurement results of the last completed measurement.

#### NI-RFPM Fetch Receiver Measurement Double

Fetches the double-precision floating point receiver measurement results of the last completed measurement, along with frequencies and port powers.

[IMAGE alt='NI-RFPM Fetch Receiver Measurement Double' src='ni-rfpm_fetch_receiver_measurement_double.gif']

|  | receiver port specifies the receiver port of the measurement you are fetching. |
| --- | --- |
|  | instrument handle identifies your instrument session. instrument handle is obtained from the NI-RFPM Init With Resources VI and identifies a particular instrument session. |
|  | receiver specifies the receiver from which to fetch measurements. Test Receiver NI-RFPM fetches from the test receiver. Reference Receiver NI-RFPM fetches from the reference receiver. |
| Test Receiver | NI-RFPM fetches from the test receiver. |
| Reference Receiver | NI-RFPM fetches from the reference receiver. |
|  | format specifies the format in which to fetch the data. Log Magnitude (dB) NI-RFPM fetches the data in log magnitude format. NI-RFPM log magnitude data is presented in decibels (dB). Linear Magnitude NI-RFPM fetches the data in linear magnitude format. NI-RFPM linear magnitude data is presented as peak voltage (Vp). Phase (deg) NI-RFPM fetches the data in phase format. NI-RFPM phase data is presented in degrees of phase shift of the response with respect to the stimulus. Phase data is presented in a wrapped format (+/-180 degree segments). |
| Log Magnitude (dB) | NI-RFPM fetches the data in log magnitude format. NI-RFPM log magnitude data is presented in decibels (dB). |
| Linear Magnitude | NI-RFPM fetches the data in linear magnitude format. NI-RFPM linear magnitude data is presented as peak voltage (Vp). |
| Phase (deg) | NI-RFPM fetches the data in phase format. NI-RFPM phase data is presented in degrees of phase shift of the response with respect to the stimulus. Phase data is presented in a wrapped format (+/-180 degree segments). |
|  | driving port specifies the port that NI-RFPM applies the stimulus to during the desired measurement. |
|  | The error in cluster can accept error information wired from VIs previously called. Use this information to decide if any functionality should be bypassed in the event of errors from other VIs. Right-click the error in control on the front panel and select Explain Error or Explain Warning from the shortcut menu for more information about the error. The status boolean is either TRUE (X) for an error, or FALSE (checkmark) for no error or a warning. The pop-up option Explain Error (or Explain Warning) gives more information about the error displayed. The code input identifies the error or warning. The pop-up option Explain Error (or Explain Warning) gives more information about the error displayed. The source string describes the origin of the error or warning. The pop-up option Explain Error (or Explain Warning) gives more information about the error displayed. |
|  | The status boolean is either TRUE (X) for an error, or FALSE (checkmark) for no error or a warning. The pop-up option Explain Error (or Explain Warning) gives more information about the error displayed. |
|  | The code input identifies the error or warning. The pop-up option Explain Error (or Explain Warning) gives more information about the error displayed. |
|  | The source string describes the origin of the error or warning. The pop-up option Explain Error (or Explain Warning) gives more information about the error displayed. |
|  | Timeout specifies the time to wait for the operation to complete before returning an error, expressed in seconds. |
|  | instrument handle out passes a reference to your instrument session to the next VI. instrument handle out is obtained from the NI-RFPM Init With Resources VI and identifies a particular instrument session. |
|  | data returns the measurement data as a 1-D double array of receiver measurements per measurement point in the specified format. |
|  | frequency returns a 1-D double array of frequencies for each measurement point, in Hz. |
|  | powerreturns a 1-D double array of power levels used at the stimulus port for each measurement point, in dBm. |
|  | The error out cluster passes error or warning information out of a VI to be used by other VIs. Use this information to decide if any functionality should be bypassed in the event of errors from other VIs. The status boolean is either TRUE (X) for an error, or FALSE (checkmark) for no error or a warning. The pop-up option Explain Error (or Explain Warning) gives more information about the error displayed. The code output identifies the error or warning. The pop-up option Explain Error (or Explain Warning) gives more information about the error displayed. The source string describes the origin of the error or warning. The pop-up option Explain Error (or Explain Warning) gives more information about the error displayed. |
|  | The status boolean is either TRUE (X) for an error, or FALSE (checkmark) for no error or a warning. The pop-up option Explain Error (or Explain Warning) gives more information about the error displayed. |
|  | The code output identifies the error or warning. The pop-up option Explain Error (or Explain Warning) gives more information about the error displayed. |
|  | The source string describes the origin of the error or warning. The pop-up option Explain Error (or Explain Warning) gives more information about the error displayed. |

#### NI-RFPM Fetch Receiver Measurement Complex

Fetches the complex double-precision floating point receiver measurement results of the last completed measurement, along with frequencies and port powers.

[IMAGE alt='NI-RFPM Fetch Receiver Measurement Complex' src='ni-rfpm_fetch_receiver_measurement_complex.gif']

|  | receiver port specifies the receiver port of the measurement you are fetching. |
| --- | --- |
|  | instrument handle identifies your instrument session. instrument handle is obtained from the NI-RFPM Init With Resources VI and identifies a particular instrument session. |
|  | receiver specifies the receiver from which to fetch measurements. Test Receiver NI-RFPM fetches from the test receiver. Reference Receiver NI-RFPM fetches from the reference receiver. |
| Test Receiver | NI-RFPM fetches from the test receiver. |
| Reference Receiver | NI-RFPM fetches from the reference receiver. |
|  | format specifies the format in which to fetch the data, which is coefficient. Coefficient NI-RFPM fetches the data as 1-D IQ complex data array. |
| Coefficient | NI-RFPM fetches the data as 1-D IQ complex data array. |
|  | driving port specifies the port that NI-RFPM applies the stimulus to during the desired measurement. |
|  | The error in cluster can accept error information wired from VIs previously called. Use this information to decide if any functionality should be bypassed in the event of errors from other VIs. Right-click the error in control on the front panel and select Explain Error or Explain Warning from the shortcut menu for more information about the error. The status boolean is either TRUE (X) for an error, or FALSE (checkmark) for no error or a warning. The pop-up option Explain Error (or Explain Warning) gives more information about the error displayed. The code input identifies the error or warning. The pop-up option Explain Error (or Explain Warning) gives more information about the error displayed. The source string describes the origin of the error or warning. The pop-up option Explain Error (or Explain Warning) gives more information about the error displayed. |
|  | The status boolean is either TRUE (X) for an error, or FALSE (checkmark) for no error or a warning. The pop-up option Explain Error (or Explain Warning) gives more information about the error displayed. |
|  | The code input identifies the error or warning. The pop-up option Explain Error (or Explain Warning) gives more information about the error displayed. |
|  | The source string describes the origin of the error or warning. The pop-up option Explain Error (or Explain Warning) gives more information about the error displayed. |
|  | Timeout specifies the time to wait for the operation to complete before returning an error, expressed in seconds. |
|  | instrument handle out passes a reference to your instrument session to the next VI. instrument handle out is obtained from the NI-RFPM Init With Resources VI and identifies a particular instrument session. |
|  | data returns the measurement data as a 1-D IQ complex data array. |
|  | frequency returns a 1-D double array of frequencies for each measurement point, in Hz. |
|  | powerreturns a 1-D double array of power levels used at the stimulus port for each measurement point, in dBm. |
|  | The error out cluster passes error or warning information out of a VI to be used by other VIs. Use this information to decide if any functionality should be bypassed in the event of errors from other VIs. The status boolean is either TRUE (X) for an error, or FALSE (checkmark) for no error or a warning. The pop-up option Explain Error (or Explain Warning) gives more information about the error displayed. The code output identifies the error or warning. The pop-up option Explain Error (or Explain Warning) gives more information about the error displayed. The source string describes the origin of the error or warning. The pop-up option Explain Error (or Explain Warning) gives more information about the error displayed. |
|  | The status boolean is either TRUE (X) for an error, or FALSE (checkmark) for no error or a warning. The pop-up option Explain Error (or Explain Warning) gives more information about the error displayed. |
|  | The code output identifies the error or warning. The pop-up option Explain Error (or Explain Warning) gives more information about the error displayed. |
|  | The source string describes the origin of the error or warning. The pop-up option Explain Error (or Explain Warning) gives more information about the error displayed. |

<!--NI_TOPIC bundle=ni-rfpm-api-ref path=rfpmviref/ni-rfpm_fetch_receiver_offset.html language=enus -->
## TOPIC 00192: NI-RFPM Fetch Receiver Offset VI

- bundle_id: `ni-rfpm-api-ref`
- source_path: `rfpmviref/ni-rfpm_fetch_receiver_offset.html`
- source_url: https://docs-be.ni.com/bundle/ni-rfpm-api-ref/raw/resource/enus/rfpmviref/ni-rfpm_fetch_receiver_offset.html
- document_id: `ni-rfpm-api-ref`
- page_type: `leaf`
- content_type: ``

NI-RFPM Fetch Receiver Offset VI

Installed With:

Fetches the stored receiver offset for a single frequency, reference level, and path setting at a specified port. When NI-RFPM de-embedding is enabled, the reference level is defined at the DUT reference plane.

This VI does not support the mmWave subsystem.

Related Information

[De-embedding](../rfpmhelp/deembedding.html)

#### NI-RFPM Fetch Receiver Offset By Sweep Settings

This VI is deprecated starting from NI-RFPM 14.7 onward. Use **NI-RFPM Fetch Receiver Offset By Parameters** instead.

[IMAGE alt='NI-RFPM Fetch Receiver Offset By Sweep Settings' src='ni-rfpm_fetch_receiver_offset_by_sweep_settings.gif']

#### NI-RFPM Fetch Receiver Offset By Parameters

Fetches the stored receiver offset for a specified frequency, reference level, and path setting at a specified port. When NI-RFPM de-embedding is enabled, the reference level is defined at the DUT reference plane.

Related Information

[De-embedding](../rfpmhelp/deembedding.html)

[IMAGE alt='NI-RFPM Fetch Receiver Offset By Parameters' src='ni-rfpm_fetch_receiver_offset_by_parameters.gif']

|  | instrument handle identifies your instrument session. instrument handle is obtained from the NI-RFPM Init With Resources VI and identifies a particular instrument session. |
| --- | --- |
|  | Receiver Path specifies the receiver path used to fetch the receiver offset data. Unspecified (default) NI-RFPM searches across all paths for offset data that matches the requested parameters. Direct NI-RFPM uses the receiver direct path through the STS device. Gain NI-RFPM uses the receiver amplified path through the STS device. Loop NI-RFPM uses the path through the receiver bypass loop of the STS device. |
| Unspecified (default) | NI-RFPM searches across all paths for offset data that matches the requested parameters. |
| Direct | NI-RFPM uses the receiver direct path through the STS device. |
| Gain | NI-RFPM uses the receiver amplified path through the STS device. |
| Loop | NI-RFPM uses the path through the receiver bypass loop of the STS device. |
|  | frequency specifies the frequency to fetch the receiver offset data for. Frequency is expressed in Hz. |
|  | Reference Level specifies the reference level of the NI-RFPM receiver port in decibels milliwatt (dBm). When NI-RFPM de-embedding is enabled, the reference level is defined at the DUT reference plane. |
|  | Optimization Method specifies what to optimize for when picking the path to use through RFPM. This only applies if Receiver Path and Receiver Coupling Path are both set to Unspecified. The default value is Normal. Normal Look up the RFPM path to use based on the peak power so you can use state freeze to achieve the best absolute amplitude accuracy. Optimize for Dynamic Range Look up the RFPM path based on average power since this optimizes dynamic range which benefits EVM and other measurements at the cost of maintaining the state freeze and absolute amplitude accuracy. |
| Normal | Look up the RFPM path to use based on the peak power so you can use state freeze to achieve the best absolute amplitude accuracy. |
| Optimize for Dynamic Range | Look up the RFPM path based on average power since this optimizes dynamic range which benefits EVM and other measurements at the cost of maintaining the state freeze and absolute amplitude accuracy. |
|  | port specifies the port to fetch the receiver offsets for. |
|  | Receiver Coupling Path specifies the receiver coupling path of the STS device from which to fetch the offset. Only the coupled path is supported when using an STS-5534 port. Unspecified (default) NI-RFPM searches across all paths for offset data that matches the requested parameters. Coupled NI-RFPM uses the test receiver coupled path through the STS device. Direct NI-RFPM uses the direct receiver path through the STS device. LNA NI-RFPM uses the LNA receiver path through the STS device. |
| Unspecified (default) | NI-RFPM searches across all paths for offset data that matches the requested parameters. |
| Coupled | NI-RFPM uses the test receiver coupled path through the STS device. |
| Direct | NI-RFPM uses the direct receiver path through the STS device. |
| LNA | NI-RFPM uses the LNA receiver path through the STS device. |
|  | PAPR specifies the peak to average envelope power ratio of the waveform to be measured. Only applies if the Optimization Method is set to Optimize For Dynamic Range. The default value is 0. Valid values are 0 to positive infinity. |
|  | The error in cluster can accept error information wired from VIs previously called. Use this information to decide if any functionality should be bypassed in the event of errors from other VIs. Right-click the error in control on the front panel and select Explain Error or Explain Warning from the shortcut menu for more information about the error. The status boolean is either TRUE (X) for an error, or FALSE (checkmark) for no error or a warning. The pop-up option Explain Error (or Explain Warning) gives more information about the error displayed. The code input identifies the error or warning. The pop-up option Explain Error (or Explain Warning) gives more information about the error displayed. The source string describes the origin of the error or warning. The pop-up option Explain Error (or Explain Warning) gives more information about the error displayed. |
|  | The status boolean is either TRUE (X) for an error, or FALSE (checkmark) for no error or a warning. The pop-up option Explain Error (or Explain Warning) gives more information about the error displayed. |
|  | The code input identifies the error or warning. The pop-up option Explain Error (or Explain Warning) gives more information about the error displayed. |
|  | The source string describes the origin of the error or warning. The pop-up option Explain Error (or Explain Warning) gives more information about the error displayed. |
|  | instrument handle out passes a reference to your instrument session to the next VI. instrument handle out is obtained from the NI-RFPM Init With Resources VI and identifies a particular instrument session. |
|  | Receiver Offset returns the receiver offset for the specified settings. The value is expressed as loss of in decibels. It corresponds to the loss of the path between the DUT reference plane and the VST receiver taking into account de-embedding when enabled. |
|  | Switch Path String returns the path of the STS device that the offset applies to. |
|  | RFSA Reference Level returns the actual reference level in decibels milliwatt (dBm) which must be applied to the RFSA/RFmx driver in order to guarantee that the receiver hardware is in a valid calibrated state. |
|  | DigitalGain returns temperature corrected digital gain, in decibels. Use this value to adjust the reference level of the RFSA device while keeping the analog path fixed, for example, at calibrated/coerced reference level. Refer to the NI-RFSA Digital Gain (dB) Property for more details. |
|  | The error out cluster passes error or warning information out of a VI to be used by other VIs. Use this information to decide if any functionality should be bypassed in the event of errors from other VIs. The status boolean is either TRUE (X) for an error, or FALSE (checkmark) for no error or a warning. The pop-up option Explain Error (or Explain Warning) gives more information about the error displayed. The code output identifies the error or warning. The pop-up option Explain Error (or Explain Warning) gives more information about the error displayed. The source string describes the origin of the error or warning. The pop-up option Explain Error (or Explain Warning) gives more information about the error displayed. |
|  | The status boolean is either TRUE (X) for an error, or FALSE (checkmark) for no error or a warning. The pop-up option Explain Error (or Explain Warning) gives more information about the error displayed. |
|  | The code output identifies the error or warning. The pop-up option Explain Error (or Explain Warning) gives more information about the error displayed. |
|  | The source string describes the origin of the error or warning. The pop-up option Explain Error (or Explain Warning) gives more information about the error displayed. |

<!--NI_TOPIC bundle=ni-rfpm-api-ref path=rfpmviref/ni-rfpm_fetch_s-parameter_measurements.html language=enus -->
## TOPIC 00193: NI-RFPM Fetch S-parameter Measurements VI

- bundle_id: `ni-rfpm-api-ref`
- source_path: `rfpmviref/ni-rfpm_fetch_s-parameter_measurements.html`
- source_url: https://docs-be.ni.com/bundle/ni-rfpm-api-ref/raw/resource/enus/rfpmviref/ni-rfpm_fetch_s-parameter_measurements.html
- document_id: `ni-rfpm-api-ref`
- page_type: `leaf`
- content_type: ``

NI-RFPM Fetch S-parameter Measurements VI

Installed With:

Fetches all S-parameter measurement results from the last completed measurement.

#### NI-RFPM Fetch S-Parameter Measurements Double

Fetches all double-precision floating point S-parameter measurement results from the last completed measurement, along with frequency points and port powers.

[IMAGE alt='NI-RFPM Fetch S-Parameter Measurements Double' src='ni-rfpm_fetch_s-parameter_measurements_double.gif']

|  | instrument handle identifies your instrument session. instrument handle is obtained from the NI-RFPM Init With Resources VI and identifies a particular instrument session. |
| --- | --- |
|  | format specifies the format in which to fetch the data. Log Magnitude (dB) NI-RFPM fetches the data in log magnitude format. NI-RFPM log magnitude data is presented in decibels (dB). Linear Magnitude NI-RFPM fetches the data in linear magnitude format. NI-RFPM linear magnitude data is presented as peak voltage (Vp). Phase (deg) NI-RFPM fetches the data in phase format. NI-RFPM phase data is presented in degrees of phase shift of the response with respect to the stimulus. Phase data is presented in a wrapped format (+/-180 degree segments). |
| Log Magnitude (dB) | NI-RFPM fetches the data in log magnitude format. NI-RFPM log magnitude data is presented in decibels (dB). |
| Linear Magnitude | NI-RFPM fetches the data in linear magnitude format. NI-RFPM linear magnitude data is presented as peak voltage (Vp). |
| Phase (deg) | NI-RFPM fetches the data in phase format. NI-RFPM phase data is presented in degrees of phase shift of the response with respect to the stimulus. Phase data is presented in a wrapped format (+/-180 degree segments). |
|  | The error in cluster can accept error information wired from VIs previously called. Use this information to decide if any functionality should be bypassed in the event of errors from other VIs. Right-click the error in control on the front panel and select Explain Error or Explain Warning from the shortcut menu for more information about the error. The status boolean is either TRUE (X) for an error, or FALSE (checkmark) for no error or a warning. The pop-up option Explain Error (or Explain Warning) gives more information about the error displayed. The code input identifies the error or warning. The pop-up option Explain Error (or Explain Warning) gives more information about the error displayed. The source string describes the origin of the error or warning. The pop-up option Explain Error (or Explain Warning) gives more information about the error displayed. |
|  | The status boolean is either TRUE (X) for an error, or FALSE (checkmark) for no error or a warning. The pop-up option Explain Error (or Explain Warning) gives more information about the error displayed. |
|  | The code input identifies the error or warning. The pop-up option Explain Error (or Explain Warning) gives more information about the error displayed. |
|  | The source string describes the origin of the error or warning. The pop-up option Explain Error (or Explain Warning) gives more information about the error displayed. |
|  | Timeout specifies the time to wait for the operation to complete before returning an error, expressed in seconds. |
|  | instrument handle out passes a reference to your instrument session to the next VI. instrument handle out is obtained from the NI-RFPM Init With Resources VI and identifies a particular instrument session. |
|  | data returns the measurement data as a 3-D complex data array with a 2-D array of S-parameters per measurement point. To index this 3-D complex data array: the first index is for the measurement point in the sweep, the second index is for the response port, and the third index is for the stimulus port. |
|  | frequency returns a 1-D double array of frequencies for each measurement point, in Hz. |
|  | power returns a 2-D double array of port powers for each measurement point in dBm. The first index is for the measurement point in the sweep, and the second index is for the port. |
|  | The error out cluster passes error or warning information out of a VI to be used by other VIs. Use this information to decide if any functionality should be bypassed in the event of errors from other VIs. The status boolean is either TRUE (X) for an error, or FALSE (checkmark) for no error or a warning. The pop-up option Explain Error (or Explain Warning) gives more information about the error displayed. The code output identifies the error or warning. The pop-up option Explain Error (or Explain Warning) gives more information about the error displayed. The source string describes the origin of the error or warning. The pop-up option Explain Error (or Explain Warning) gives more information about the error displayed. |
|  | The status boolean is either TRUE (X) for an error, or FALSE (checkmark) for no error or a warning. The pop-up option Explain Error (or Explain Warning) gives more information about the error displayed. |
|  | The code output identifies the error or warning. The pop-up option Explain Error (or Explain Warning) gives more information about the error displayed. |
|  | The source string describes the origin of the error or warning. The pop-up option Explain Error (or Explain Warning) gives more information about the error displayed. |

#### NI-RFPM Fetch S-Parameter Measurements Complex

Fetches all complex double-precision floating point S-parameter measurement results from the last completed measurement, along with frequency points and port powers.

[IMAGE alt='NI-RFPM Fetch S-Parameter Measurements Complex' src='ni-rfpm_fetch_s-parameter_measurements_complex.gif']

|  | instrument handle identifies your instrument session. instrument handle is obtained from the NI-RFPM Init With Resources VI and identifies a particular instrument session. |
| --- | --- |
|  | format specifies the format in which to fetch the data, which is coefficient. Coefficient NI-RFPM fetches the data as 1-D IQ complex data array. |
| Coefficient | NI-RFPM fetches the data as 1-D IQ complex data array. |
|  | The error in cluster can accept error information wired from VIs previously called. Use this information to decide if any functionality should be bypassed in the event of errors from other VIs. Right-click the error in control on the front panel and select Explain Error or Explain Warning from the shortcut menu for more information about the error. The status boolean is either TRUE (X) for an error, or FALSE (checkmark) for no error or a warning. The pop-up option Explain Error (or Explain Warning) gives more information about the error displayed. The code input identifies the error or warning. The pop-up option Explain Error (or Explain Warning) gives more information about the error displayed. The source string describes the origin of the error or warning. The pop-up option Explain Error (or Explain Warning) gives more information about the error displayed. |
|  | The status boolean is either TRUE (X) for an error, or FALSE (checkmark) for no error or a warning. The pop-up option Explain Error (or Explain Warning) gives more information about the error displayed. |
|  | The code input identifies the error or warning. The pop-up option Explain Error (or Explain Warning) gives more information about the error displayed. |
|  | The source string describes the origin of the error or warning. The pop-up option Explain Error (or Explain Warning) gives more information about the error displayed. |
|  | Timeout specifies the time to wait for the operation to complete before returning an error, expressed in seconds. |
|  | instrument handle out passes a reference to your instrument session to the next VI. instrument handle out is obtained from the NI-RFPM Init With Resources VI and identifies a particular instrument session. |
|  | data returns the measurement data as a 3-D complex data array with a 2-D array of S-parameters per measurement point. To index this 3-D complex data array: the first index is for the measurement point in the sweep, the second index is for the response port, and the third index is for the stimulus port. |
|  | frequency returns a 1-D double array of frequencies for each measurement point, in Hz. |
|  | power returns a 2-D double array of port powers for each measurement point in dBm. The first index is for the measurement point in the sweep, and the second index is for the port. |
|  | The error out cluster passes error or warning information out of a VI to be used by other VIs. Use this information to decide if any functionality should be bypassed in the event of errors from other VIs. The status boolean is either TRUE (X) for an error, or FALSE (checkmark) for no error or a warning. The pop-up option Explain Error (or Explain Warning) gives more information about the error displayed. The code output identifies the error or warning. The pop-up option Explain Error (or Explain Warning) gives more information about the error displayed. The source string describes the origin of the error or warning. The pop-up option Explain Error (or Explain Warning) gives more information about the error displayed. |
|  | The status boolean is either TRUE (X) for an error, or FALSE (checkmark) for no error or a warning. The pop-up option Explain Error (or Explain Warning) gives more information about the error displayed. |
|  | The code output identifies the error or warning. The pop-up option Explain Error (or Explain Warning) gives more information about the error displayed. |
|  | The source string describes the origin of the error or warning. The pop-up option Explain Error (or Explain Warning) gives more information about the error displayed. |

<!--NI_TOPIC bundle=ni-rfpm-api-ref path=rfpmviref/ni-rfpm_fetch_single_s-parameter_measurement.html language=enus -->
## TOPIC 00194: NI-RFPM Fetch Single S-Parameter Measurement VI

- bundle_id: `ni-rfpm-api-ref`
- source_path: `rfpmviref/ni-rfpm_fetch_single_s-parameter_measurement.html`
- source_url: https://docs-be.ni.com/bundle/ni-rfpm-api-ref/raw/resource/enus/rfpmviref/ni-rfpm_fetch_single_s-parameter_measurement.html
- document_id: `ni-rfpm-api-ref`
- page_type: `leaf`
- content_type: ``

NI-RFPM Fetch Single S-Parameter Measurement VI

Installed With:

Fetches a single S-parameter measurement result from the last completed measurement.

#### NI-RFPM Fetch Single S-Parameter Measurement Double

Fetches a single double-precision floating point S-parameter measurement result from the last completed measurement, along with frequency points and port powers.

[IMAGE alt='NI-RFPM Fetch Single S-Parameter Measurement Double' src='ni-rfpm_fetch_single_s-parameter_measurement_double.gif']

|  | instrument handle identifies your instrument session. instrument handle is obtained from the NI-RFPM Init With Resources VI and identifies a particular instrument session. |
| --- | --- |
|  | Stimulus Port specifies the stimulus port, which is the second number of the S-parameter. Stimulus Port uses absolute port numbers. |
|  | format specifies the format in which to fetch the data. Log Magnitude (dB) NI-RFPM fetches the data in log magnitude format. NI-RFPM log magnitude data is presented in decibels (dB). Linear Magnitude NI-RFPM fetches the data in linear magnitude format. NI-RFPM linear magnitude data is presented as peak voltage (Vp). Phase (deg) NI-RFPM fetches the data in phase format. NI-RFPM phase data is presented in degrees of phase shift of the response with respect to the stimulus. Phase data is presented in a wrapped format (+/-180 degree segments). |
| Log Magnitude (dB) | NI-RFPM fetches the data in log magnitude format. NI-RFPM log magnitude data is presented in decibels (dB). |
| Linear Magnitude | NI-RFPM fetches the data in linear magnitude format. NI-RFPM linear magnitude data is presented as peak voltage (Vp). |
| Phase (deg) | NI-RFPM fetches the data in phase format. NI-RFPM phase data is presented in degrees of phase shift of the response with respect to the stimulus. Phase data is presented in a wrapped format (+/-180 degree segments). |
|  | Response Port specifies the response port, which is the first number of the S-parameter. Response Port uses absolute port numbers. |
|  | The error in cluster can accept error information wired from VIs previously called. Use this information to decide if any functionality should be bypassed in the event of errors from other VIs. Right-click the error in control on the front panel and select Explain Error or Explain Warning from the shortcut menu for more information about the error. The status boolean is either TRUE (X) for an error, or FALSE (checkmark) for no error or a warning. The pop-up option Explain Error (or Explain Warning) gives more information about the error displayed. The code input identifies the error or warning. The pop-up option Explain Error (or Explain Warning) gives more information about the error displayed. The source string describes the origin of the error or warning. The pop-up option Explain Error (or Explain Warning) gives more information about the error displayed. |
|  | The status boolean is either TRUE (X) for an error, or FALSE (checkmark) for no error or a warning. The pop-up option Explain Error (or Explain Warning) gives more information about the error displayed. |
|  | The code input identifies the error or warning. The pop-up option Explain Error (or Explain Warning) gives more information about the error displayed. |
|  | The source string describes the origin of the error or warning. The pop-up option Explain Error (or Explain Warning) gives more information about the error displayed. |
|  | Timeout specifies the time to wait for the operation to complete before returning an error, expressed in seconds. |
|  | instrument handle out passes a reference to your instrument session to the next VI. instrument handle out is obtained from the NI-RFPM Init With Resources VI and identifies a particular instrument session. |
|  | data returns the measurement data as a 1-D double array of S-parameter measurements per measurement point in the specified format. |
|  | frequency returns a 1-D double array of frequencies for each measurement point, in Hz. |
|  | powerreturns a 1-D double array of power levels used at the stimulus port for each measurement point, in dBm. |
|  | The error out cluster passes error or warning information out of a VI to be used by other VIs. Use this information to decide if any functionality should be bypassed in the event of errors from other VIs. The status boolean is either TRUE (X) for an error, or FALSE (checkmark) for no error or a warning. The pop-up option Explain Error (or Explain Warning) gives more information about the error displayed. The code output identifies the error or warning. The pop-up option Explain Error (or Explain Warning) gives more information about the error displayed. The source string describes the origin of the error or warning. The pop-up option Explain Error (or Explain Warning) gives more information about the error displayed. |
|  | The status boolean is either TRUE (X) for an error, or FALSE (checkmark) for no error or a warning. The pop-up option Explain Error (or Explain Warning) gives more information about the error displayed. |
|  | The code output identifies the error or warning. The pop-up option Explain Error (or Explain Warning) gives more information about the error displayed. |
|  | The source string describes the origin of the error or warning. The pop-up option Explain Error (or Explain Warning) gives more information about the error displayed. |

#### NI-RFPM Fetch Single S-Parameter Measurement Complex

Fetches a single complex double-precision floating point S-parameter measurement result from the last completed measurement, along with frequency points and port powers.

[IMAGE alt='NI-RFPM Fetch Single S-Parameter Measurement Complex' src='ni-rfpm_fetch_single_s-parameter_measurement_complex.gif']

|  | instrument handle identifies your instrument session. instrument handle is obtained from the NI-RFPM Init With Resources VI and identifies a particular instrument session. |
| --- | --- |
|  | Stimulus Port specifies the stimulus port, which is the second number of the S-parameter. Stimulus Port uses absolute port numbers. |
|  | format specifies the format in which to fetch the data, which is coefficient. Coefficient NI-RFPM fetches the data as 1-D IQ complex data array. |
| Coefficient | NI-RFPM fetches the data as 1-D IQ complex data array. |
|  | Response Port specifies the response port, which is the first number of the S-parameter. Response Port uses absolute port numbers. |
|  | The error in cluster can accept error information wired from VIs previously called. Use this information to decide if any functionality should be bypassed in the event of errors from other VIs. Right-click the error in control on the front panel and select Explain Error or Explain Warning from the shortcut menu for more information about the error. The status boolean is either TRUE (X) for an error, or FALSE (checkmark) for no error or a warning. The pop-up option Explain Error (or Explain Warning) gives more information about the error displayed. The code input identifies the error or warning. The pop-up option Explain Error (or Explain Warning) gives more information about the error displayed. The source string describes the origin of the error or warning. The pop-up option Explain Error (or Explain Warning) gives more information about the error displayed. |
|  | The status boolean is either TRUE (X) for an error, or FALSE (checkmark) for no error or a warning. The pop-up option Explain Error (or Explain Warning) gives more information about the error displayed. |
|  | The code input identifies the error or warning. The pop-up option Explain Error (or Explain Warning) gives more information about the error displayed. |
|  | The source string describes the origin of the error or warning. The pop-up option Explain Error (or Explain Warning) gives more information about the error displayed. |
|  | Timeout specifies the time to wait for the operation to complete before returning an error, expressed in seconds. |
|  | instrument handle out passes a reference to your instrument session to the next VI. instrument handle out is obtained from the NI-RFPM Init With Resources VI and identifies a particular instrument session. |
|  | data returns the measurement data as a 1-D IQ complex data array. |
|  | frequency returns a 1-D double array of frequencies for each measurement point, in Hz. |
|  | powerreturns a 1-D double array of power levels used at the stimulus port for each measurement point, in dBm. |
|  | The error out cluster passes error or warning information out of a VI to be used by other VIs. Use this information to decide if any functionality should be bypassed in the event of errors from other VIs. The status boolean is either TRUE (X) for an error, or FALSE (checkmark) for no error or a warning. The pop-up option Explain Error (or Explain Warning) gives more information about the error displayed. The code output identifies the error or warning. The pop-up option Explain Error (or Explain Warning) gives more information about the error displayed. The source string describes the origin of the error or warning. The pop-up option Explain Error (or Explain Warning) gives more information about the error displayed. |
|  | The status boolean is either TRUE (X) for an error, or FALSE (checkmark) for no error or a warning. The pop-up option Explain Error (or Explain Warning) gives more information about the error displayed. |
|  | The code output identifies the error or warning. The pop-up option Explain Error (or Explain Warning) gives more information about the error displayed. |
|  | The source string describes the origin of the error or warning. The pop-up option Explain Error (or Explain Warning) gives more information about the error displayed. |

<!--NI_TOPIC bundle=ni-rfpm-api-ref path=rfpmviref/ni-rfpm_fetch_source_offset_with_settings_and_settling_time.html language=enus -->
## TOPIC 00195: NI-RFPM Fetch Source Offset With Settings And Settling Time VI

- bundle_id: `ni-rfpm-api-ref`
- source_path: `rfpmviref/ni-rfpm_fetch_source_offset_with_settings_and_settling_time.html`
- source_url: https://docs-be.ni.com/bundle/ni-rfpm-api-ref/raw/resource/enus/rfpmviref/ni-rfpm_fetch_source_offset_with_settings_and_settling_time.html
- document_id: `ni-rfpm-api-ref`
- page_type: `leaf`
- content_type: ``

NI-RFPM Fetch Source Offset With Settings And Settling Time VI

Installed With:

Fetches the stored source offset and settling time for a single frequency, power, and path setting for a specified port. When the [De-embedding Enabled](../rfpmpropref/pnirfpm_deembeddingenabled.html) property is set to TRUE and the [De-embedding S2P Path](../rfpmpropref/pnirfpm_deembeddings2p_path.html) property is set to the correct de-embedding files, the power level is defined at the DUT reference plane.

This VI does not support the mmWave subsystem.

[IMAGE alt='NI-RFPM Fetch Source Offset With Settings And Settling Time' src='ni-rfpm_fetch_source_offset_with_settings_and_settling_time.gif']

|  | instrument handle identifies your instrument session. instrument handle is obtained from the NI-RFPM Init With Resources VI and identifies a particular instrument session. |
| --- | --- |
|  | Source Path specifies the source path used to fetch the source offset data. Unspecified (default) NI-RFPM searches across all paths for offset data that matches the requested parameters. Direct NI-RFPM uses the direct path through the STS device. Gain NI-RFPM uses the amplified path through the STS device. Loop NI-RFPM uses the path through the bypass loop of the STS device. Two Tone NI-RFPM uses the path through the bypass loop of the NI-RFPM Switch but retrieves calibration and settling time data specific to the two-tone generation solution that can optionally be installed in the loop path. Note Internal termination is only useful when combined with Loop or Two Tone. If internal termination is used with Direct or Gain, no signal is present out of the STS RF Subsystem. |
| Unspecified (default) | NI-RFPM searches across all paths for offset data that matches the requested parameters. |
| Direct | NI-RFPM uses the direct path through the STS device. |
| Gain | NI-RFPM uses the amplified path through the STS device. |
| Loop | NI-RFPM uses the path through the bypass loop of the STS device. |
| Two Tone | NI-RFPM uses the path through the bypass loop of the NI-RFPM Switch but retrieves calibration and settling time data specific to the two-tone generation solution that can optionally be installed in the loop path. |
|  | Note Internal termination is only useful when combined with Loop or Two Tone. If internal termination is used with Direct or Gain, no signal is present out of the STS RF Subsystem. |
|  | frequency specifies the frequency to fetch the source offset data for. This value is expressed in Hz. |
|  | power specifies the power to fetch the source offset data for. When the De-embedding Enabled property is set to TRUE and the De-embedding S2P Path property is set to the correct de-embedding files, the power level is defined at the DUT reference plane. This value is expressed in decibels milliwatt (dBm). |
|  | Optimization Method specifies what to optimize for when picking the path to use through RFPM. This only applies if Source Path is set to Unspecified. The default value is Normal. Normal Look up the NI-RFPM path to use based on the peak power so you can use state freeze to achieve the best absolute amplitude accuracy. Optimize for Dynamic Range Look up the NI-RFPM path based on average power since this optimizes dynamic range which benefits EVM and other measurements at the cost of maintaining the state freeze and absolute amplitude accuracy. |
| Normal | Look up the NI-RFPM path to use based on the peak power so you can use state freeze to achieve the best absolute amplitude accuracy. |
| Optimize for Dynamic Range | Look up the NI-RFPM path based on average power since this optimizes dynamic range which benefits EVM and other measurements at the cost of maintaining the state freeze and absolute amplitude accuracy. |
|  | Port specifies the port to fetch the source offset for. |
|  | Power Level Type specifies if power and Calibrated Power represent average envelope power or peak envelope power. The default value is Peak. Calibrated Power represents average waveform power. Peak Both power and Calibrated Power represent peak waveform power. Average Both power and Calibrated Power represent average waveform power. |
| Peak | Both power and Calibrated Power represent peak waveform power. |
| Average | Both power and Calibrated Power represent average waveform power. |
|  | PAPR specifies the peak to average envelope power ratio, in decibels, of the generated waveform. The default value is 0. Valid values are 0 to positive infinity. |
|  | Runtime Scaling specifies the runtime scaling, also called pre-filter gain, in decibels, to use with the generated waveform. The default value is 0. Valid values are negative infinity to 0. |
|  | The error in cluster can accept error information wired from VIs previously called. Use this information to decide if any functionality should be bypassed in the event of errors from other VIs. Right-click the error in control on the front panel and select Explain Error or Explain Warning from the shortcut menu for more information about the error. The status boolean is either TRUE (X) for an error, or FALSE (checkmark) for no error or a warning. The pop-up option Explain Error (or Explain Warning) gives more information about the error displayed. The code input identifies the error or warning. The pop-up option Explain Error (or Explain Warning) gives more information about the error displayed. The source string describes the origin of the error or warning. The pop-up option Explain Error (or Explain Warning) gives more information about the error displayed. |
|  | The status boolean is either TRUE (X) for an error, or FALSE (checkmark) for no error or a warning. The pop-up option Explain Error (or Explain Warning) gives more information about the error displayed. |
|  | The code input identifies the error or warning. The pop-up option Explain Error (or Explain Warning) gives more information about the error displayed. |
|  | The source string describes the origin of the error or warning. The pop-up option Explain Error (or Explain Warning) gives more information about the error displayed. |
|  | instrument handle out passes a reference to your instrument session to the next VI. instrument handle out is obtained from the NI-RFPM Init With Resources VI and identifies a particular instrument session. |
|  | Source Offset returns the source offset for the specified settings. This value is expressed as loss in decibels. The source offset corresponds to the loss of the path between the VST generator and the DUT reference plane, taking into account de-embedding when enabled. |
|  | Switch Path String returns the path of the STS device that the offset applies to. |
|  | Calibrated Power specifies the calibrated power level of the NI-RFPM source port in dBm. When NI-RFPM de-embedding is enabled, the power level is defined at the DUT reference plane. |
|  | Settling Time returns the time, in seconds, required for the signal at the specified NI-RFPM Switch source path output channel to settle within the specified source amplitude settling. |
|  | Digital Gain returns temperature corrected digital gain, in decibels. Digital gain represents the difference between the calibrated power and user-requested power, with automatic adjustments for temperature. Use this value to adjust the output power of the NI-RFPM device while keeping the analog path fixed, for example, at the calibrated power level. Refer to the NI-RFSA Digital Gain (dB) property for more details. |
|  | The error out cluster passes error or warning information out of a VI to be used by other VIs. Use this information to decide if any functionality should be bypassed in the event of errors from other VIs. The status boolean is either TRUE (X) for an error, or FALSE (checkmark) for no error or a warning. The pop-up option Explain Error (or Explain Warning) gives more information about the error displayed. The code output identifies the error or warning. The pop-up option Explain Error (or Explain Warning) gives more information about the error displayed. The source string describes the origin of the error or warning. The pop-up option Explain Error (or Explain Warning) gives more information about the error displayed. |
|  | The status boolean is either TRUE (X) for an error, or FALSE (checkmark) for no error or a warning. The pop-up option Explain Error (or Explain Warning) gives more information about the error displayed. |
|  | The code output identifies the error or warning. The pop-up option Explain Error (or Explain Warning) gives more information about the error displayed. |
|  | The source string describes the origin of the error or warning. The pop-up option Explain Error (or Explain Warning) gives more information about the error displayed. |

<!--NI_TOPIC bundle=ni-rfpm-api-ref path=rfpmviref/ni-rfpm_get_callbacks_for_rfmx.html language=enus -->
## TOPIC 00196: NI-RFPM Get Callbacks For RFmx VI

- bundle_id: `ni-rfpm-api-ref`
- source_path: `rfpmviref/ni-rfpm_get_callbacks_for_rfmx.html`
- source_url: https://docs-be.ni.com/bundle/ni-rfpm-api-ref/raw/resource/enus/rfpmviref/ni-rfpm_get_callbacks_for_rfmx.html
- document_id: `ni-rfpm-api-ref`
- page_type: `leaf`
- content_type: ``

NI-RFPM Get Callbacks For RFmx VI

Installed With:

Returns pointers to callback functions to be passed into RFmx.

This VI does not support the mmWave subsystem.

[IMAGE alt='NI-RFPM Get Callbacks For RFmx' src='ni-rfpm_get_callbacks_for_rfmx.gif']

|  | instrument handle identifies your instrument session. instrument handle is obtained from the NI-RFPM Init With Resources VI and identifies a particular instrument session. |
| --- | --- |
|  | The error in cluster can accept error information wired from VIs previously called. Use this information to decide if any functionality should be bypassed in the event of errors from other VIs. Right-click the error in control on the front panel and select Explain Error or Explain Warning from the shortcut menu for more information about the error. The status boolean is either TRUE (X) for an error, or FALSE (checkmark) for no error or a warning. The pop-up option Explain Error (or Explain Warning) gives more information about the error displayed. The code input identifies the error or warning. The pop-up option Explain Error (or Explain Warning) gives more information about the error displayed. The source string describes the origin of the error or warning. The pop-up option Explain Error (or Explain Warning) gives more information about the error displayed. |
|  | The status boolean is either TRUE (X) for an error, or FALSE (checkmark) for no error or a warning. The pop-up option Explain Error (or Explain Warning) gives more information about the error displayed. |
|  | The code input identifies the error or warning. The pop-up option Explain Error (or Explain Warning) gives more information about the error displayed. |
|  | The source string describes the origin of the error or warning. The pop-up option Explain Error (or Explain Warning) gives more information about the error displayed. |
|  | instrument handle out passes a reference to your instrument session to the next VI. instrument handle out is obtained from the NI-RFPM Init With Resources VI and identifies a particular instrument session. |
|  | Context returns a value that should be used as the input to the External RF Subsystem Context control on RFmxInstr Register External RF Subsystem Callbacks. |
|  | Callbacks For RFmx returns an array of unsigned 64-bit integers that store pointers to the callback functions. This array will be used for the input to the Callbacks control on RFmxInstr Register External RF Subsystem Callbacks. |
|  | Callback Version returns what version of the NI-RFmx callbacks these callbacks conform to. Should be used for the input to the Callback Version control on RFmxInstr Register External RF Subsystem Callbacks. |
|  | The error out cluster passes error or warning information out of a VI to be used by other VIs. Use this information to decide if any functionality should be bypassed in the event of errors from other VIs. The status boolean is either TRUE (X) for an error, or FALSE (checkmark) for no error or a warning. The pop-up option Explain Error (or Explain Warning) gives more information about the error displayed. The code output identifies the error or warning. The pop-up option Explain Error (or Explain Warning) gives more information about the error displayed. The source string describes the origin of the error or warning. The pop-up option Explain Error (or Explain Warning) gives more information about the error displayed. |
|  | The status boolean is either TRUE (X) for an error, or FALSE (checkmark) for no error or a warning. The pop-up option Explain Error (or Explain Warning) gives more information about the error displayed. |
|  | The code output identifies the error or warning. The pop-up option Explain Error (or Explain Warning) gives more information about the error displayed. |
|  | The source string describes the origin of the error or warning. The pop-up option Explain Error (or Explain Warning) gives more information about the error displayed. |

<!--NI_TOPIC bundle=ni-rfpm-api-ref path=rfpmviref/ni-rfpm_get_system_calibration_recommended_interval.html language=enus -->
## TOPIC 00197: NI-RFPM Get System Calibration Recommended Interval VI

- bundle_id: `ni-rfpm-api-ref`
- source_path: `rfpmviref/ni-rfpm_get_system_calibration_recommended_interval.html`
- source_url: https://docs-be.ni.com/bundle/ni-rfpm-api-ref/raw/resource/enus/rfpmviref/ni-rfpm_get_system_calibration_recommended_interval.html
- document_id: `ni-rfpm-api-ref`
- page_type: `leaf`
- content_type: ``

NI-RFPM Get System Calibration Recommended Interval VI

Installed With:

Returns the number of months for which a system calibration is valid.

This VI does not support the mmWave subsystem.

[IMAGE alt='NI-RFPM Get System Calibration Recommended Interval' src='ni-rfpm_get_system_calibration_recommended_interval.gif']

|  | instrument handle identifies your instrument session. instrument handle is obtained from the NI-RFPM Init With Resources VI and identifies a particular instrument session. |
| --- | --- |
|  | The error in cluster can accept error information wired from VIs previously called. Use this information to decide if any functionality should be bypassed in the event of errors from other VIs. Right-click the error in control on the front panel and select Explain Error or Explain Warning from the shortcut menu for more information about the error. The status boolean is either TRUE (X) for an error, or FALSE (checkmark) for no error or a warning. The pop-up option Explain Error (or Explain Warning) gives more information about the error displayed. The code input identifies the error or warning. The pop-up option Explain Error (or Explain Warning) gives more information about the error displayed. The source string describes the origin of the error or warning. The pop-up option Explain Error (or Explain Warning) gives more information about the error displayed. |
|  | The status boolean is either TRUE (X) for an error, or FALSE (checkmark) for no error or a warning. The pop-up option Explain Error (or Explain Warning) gives more information about the error displayed. |
|  | The code input identifies the error or warning. The pop-up option Explain Error (or Explain Warning) gives more information about the error displayed. |
|  | The source string describes the origin of the error or warning. The pop-up option Explain Error (or Explain Warning) gives more information about the error displayed. |
|  | instrument handle out passes a reference to your instrument session to the next VI. instrument handle out is obtained from the NI-RFPM Init With Resources VI and identifies a particular instrument session. |
|  | Recommended Calibration Interval returns the recommended maximum number of months between system calibrations. |
|  | The error out cluster passes error or warning information out of a VI to be used by other VIs. Use this information to decide if any functionality should be bypassed in the event of errors from other VIs. The status boolean is either TRUE (X) for an error, or FALSE (checkmark) for no error or a warning. The pop-up option Explain Error (or Explain Warning) gives more information about the error displayed. The code output identifies the error or warning. The pop-up option Explain Error (or Explain Warning) gives more information about the error displayed. The source string describes the origin of the error or warning. The pop-up option Explain Error (or Explain Warning) gives more information about the error displayed. |
|  | The status boolean is either TRUE (X) for an error, or FALSE (checkmark) for no error or a warning. The pop-up option Explain Error (or Explain Warning) gives more information about the error displayed. |
|  | The code output identifies the error or warning. The pop-up option Explain Error (or Explain Warning) gives more information about the error displayed. |
|  | The source string describes the origin of the error or warning. The pop-up option Explain Error (or Explain Warning) gives more information about the error displayed. |

<!--NI_TOPIC bundle=ni-rfpm-api-ref path=rfpmviref/ni-rfpm_init_calibration.html language=enus -->
## TOPIC 00198: NI-RFPM Init Calibration VI

- bundle_id: `ni-rfpm-api-ref`
- source_path: `rfpmviref/ni-rfpm_init_calibration.html`
- source_url: https://docs-be.ni.com/bundle/ni-rfpm-api-ref/raw/resource/enus/rfpmviref/ni-rfpm_init_calibration.html
- document_id: `ni-rfpm-api-ref`
- page_type: `leaf`
- content_type: ``

NI-RFPM Init Calibration VI

Installed With:

Initializes user or system calibration.

This VI does not support the mmWave subsystem.

[IMAGE alt='NI-RFPM Init Calibration' src='ni-rfpm_init_calibration.gif']

|  | instrument handle identifies your instrument session. instrument handle is obtained from the NI-RFPM Init With Resources VI and identifies a particular instrument session. |
| --- | --- |
|  | Calibration Type specifies the type of calibration to perform. User Initiates a user calibration. System Initiates a system calibration. |
| User | Initiates a user calibration. |
| System | Initiates a system calibration. |
|  | The error in cluster can accept error information wired from VIs previously called. Use this information to decide if any functionality should be bypassed in the event of errors from other VIs. Right-click the error in control on the front panel and select Explain Error or Explain Warning from the shortcut menu for more information about the error. The status boolean is either TRUE (X) for an error, or FALSE (checkmark) for no error or a warning. The pop-up option Explain Error (or Explain Warning) gives more information about the error displayed. The code input identifies the error or warning. The pop-up option Explain Error (or Explain Warning) gives more information about the error displayed. The source string describes the origin of the error or warning. The pop-up option Explain Error (or Explain Warning) gives more information about the error displayed. |
|  | The status boolean is either TRUE (X) for an error, or FALSE (checkmark) for no error or a warning. The pop-up option Explain Error (or Explain Warning) gives more information about the error displayed. |
|  | The code input identifies the error or warning. The pop-up option Explain Error (or Explain Warning) gives more information about the error displayed. |
|  | The source string describes the origin of the error or warning. The pop-up option Explain Error (or Explain Warning) gives more information about the error displayed. |
|  | instrument handle out passes a reference to your instrument session to the next VI. instrument handle out is obtained from the NI-RFPM Init With Resources VI and identifies a particular instrument session. |
|  | The error out cluster passes error or warning information out of a VI to be used by other VIs. Use this information to decide if any functionality should be bypassed in the event of errors from other VIs. The status boolean is either TRUE (X) for an error, or FALSE (checkmark) for no error or a warning. The pop-up option Explain Error (or Explain Warning) gives more information about the error displayed. The code output identifies the error or warning. The pop-up option Explain Error (or Explain Warning) gives more information about the error displayed. The source string describes the origin of the error or warning. The pop-up option Explain Error (or Explain Warning) gives more information about the error displayed. |
|  | The status boolean is either TRUE (X) for an error, or FALSE (checkmark) for no error or a warning. The pop-up option Explain Error (or Explain Warning) gives more information about the error displayed. |
|  | The code output identifies the error or warning. The pop-up option Explain Error (or Explain Warning) gives more information about the error displayed. |
|  | The source string describes the origin of the error or warning. The pop-up option Explain Error (or Explain Warning) gives more information about the error displayed. |

<!--NI_TOPIC bundle=ni-rfpm-api-ref path=rfpmviref/ni-rfpm_init_with_resources.html language=enus -->
## TOPIC 00199: NI-RFPM Init With Resources VI

- bundle_id: `ni-rfpm-api-ref`
- source_path: `rfpmviref/ni-rfpm_init_with_resources.html`
- source_url: https://docs-be.ni.com/bundle/ni-rfpm-api-ref/raw/resource/enus/rfpmviref/ni-rfpm_init_with_resources.html
- document_id: `ni-rfpm-api-ref`
- page_type: `leaf`
- content_type: ``

NI-RFPM Init With Resources VI

Installed With:

Initializes a session of the NI-RFPM driver and configures the measurement resources. The NI-RFSA, NI-RFSG, and either NI-RFPM Switch or IVI Switch sessions must be initialized before passing into this VI. No switch session is required for the mmWave subsystem. Pass NULL or the empty string ("") for the Switch handle parameter when using the mmWave subsystem.

[IMAGE alt='NI-RFPM Init With Resources' src='ni-rfpm_init_with_resources.gif']

|  | option string sets the initial value of certain properties for the session. A valid option would be DriverSetup=bitfile:NI-RFPM.lvbitx. |
| --- | --- |
|  | instrument handle identifies your instrument session. instrument handle is obtained from the NI-RFPM Init With Resources VI and identifies a particular instrument session. |
|  | RFSA handle specifies a handle to the NI-RFSA device. |
|  | RFSG handle specifies a handle to the NI-RFSG device. |
|  | Switch handle specifies a handle to the NI-RFPM switch. Pass NULL or the empty string ("") for this parameter when using the mmWave subsystem. |
|  | The error in cluster can accept error information wired from VIs previously called. Use this information to decide if any functionality should be bypassed in the event of errors from other VIs. Right-click the error in control on the front panel and select Explain Error or Explain Warning from the shortcut menu for more information about the error. The status boolean is either TRUE (X) for an error, or FALSE (checkmark) for no error or a warning. The pop-up option Explain Error (or Explain Warning) gives more information about the error displayed. The code input identifies the error or warning. The pop-up option Explain Error (or Explain Warning) gives more information about the error displayed. The source string describes the origin of the error or warning. The pop-up option Explain Error (or Explain Warning) gives more information about the error displayed. |
|  | The status boolean is either TRUE (X) for an error, or FALSE (checkmark) for no error or a warning. The pop-up option Explain Error (or Explain Warning) gives more information about the error displayed. |
|  | The code input identifies the error or warning. The pop-up option Explain Error (or Explain Warning) gives more information about the error displayed. |
|  | The source string describes the origin of the error or warning. The pop-up option Explain Error (or Explain Warning) gives more information about the error displayed. |
|  | instrument handle out passes a reference to your instrument session to the next VI. instrument handle out is obtained from the NI-RFPM Init With Resources VI and identifies a particular instrument session. |
|  | The error out cluster passes error or warning information out of a VI to be used by other VIs. Use this information to decide if any functionality should be bypassed in the event of errors from other VIs. The status boolean is either TRUE (X) for an error, or FALSE (checkmark) for no error or a warning. The pop-up option Explain Error (or Explain Warning) gives more information about the error displayed. The code output identifies the error or warning. The pop-up option Explain Error (or Explain Warning) gives more information about the error displayed. The source string describes the origin of the error or warning. The pop-up option Explain Error (or Explain Warning) gives more information about the error displayed. |
|  | The status boolean is either TRUE (X) for an error, or FALSE (checkmark) for no error or a warning. The pop-up option Explain Error (or Explain Warning) gives more information about the error displayed. |
|  | The code output identifies the error or warning. The pop-up option Explain Error (or Explain Warning) gives more information about the error displayed. |
|  | The source string describes the origin of the error or warning. The pop-up option Explain Error (or Explain Warning) gives more information about the error displayed. |

<!--NI_TOPIC bundle=ni-rfpm-api-ref path=rfpmviref/ni-rfpm_initiate.html language=enus -->
## TOPIC 00200: NI-RFPM Initiate VI

- bundle_id: `ni-rfpm-api-ref`
- source_path: `rfpmviref/ni-rfpm_initiate.html`
- source_url: https://docs-be.ni.com/bundle/ni-rfpm-api-ref/raw/resource/enus/rfpmviref/ni-rfpm_initiate.html
- document_id: `ni-rfpm-api-ref`
- page_type: `leaf`
- content_type: ``

NI-RFPM Initiate VI

Installed With:

Initiates a measurement as defined in the sweep settings configuration file.

[IMAGE alt='NI-RFPM Initiate' src='ni-rfpm_initiate.gif']

|  | Ports specifies an array of ports to measure. |
| --- | --- |
|  | instrument handle identifies your instrument session. instrument handle is obtained from the NI-RFPM Init With Resources VI and identifies a particular instrument session. |
|  | Sweep Setting Name specifies the name of the sweep settings for performing a measurement. |
|  | The error in cluster can accept error information wired from VIs previously called. Use this information to decide if any functionality should be bypassed in the event of errors from other VIs. Right-click the error in control on the front panel and select Explain Error or Explain Warning from the shortcut menu for more information about the error. The status boolean is either TRUE (X) for an error, or FALSE (checkmark) for no error or a warning. The pop-up option Explain Error (or Explain Warning) gives more information about the error displayed. The code input identifies the error or warning. The pop-up option Explain Error (or Explain Warning) gives more information about the error displayed. The source string describes the origin of the error or warning. The pop-up option Explain Error (or Explain Warning) gives more information about the error displayed. |
|  | The status boolean is either TRUE (X) for an error, or FALSE (checkmark) for no error or a warning. The pop-up option Explain Error (or Explain Warning) gives more information about the error displayed. |
|  | The code input identifies the error or warning. The pop-up option Explain Error (or Explain Warning) gives more information about the error displayed. |
|  | The source string describes the origin of the error or warning. The pop-up option Explain Error (or Explain Warning) gives more information about the error displayed. |
|  | instrument handle out passes a reference to your instrument session to the next VI. instrument handle out is obtained from the NI-RFPM Init With Resources VI and identifies a particular instrument session. |
|  | The error out cluster passes error or warning information out of a VI to be used by other VIs. Use this information to decide if any functionality should be bypassed in the event of errors from other VIs. The status boolean is either TRUE (X) for an error, or FALSE (checkmark) for no error or a warning. The pop-up option Explain Error (or Explain Warning) gives more information about the error displayed. The code output identifies the error or warning. The pop-up option Explain Error (or Explain Warning) gives more information about the error displayed. The source string describes the origin of the error or warning. The pop-up option Explain Error (or Explain Warning) gives more information about the error displayed. |
|  | The status boolean is either TRUE (X) for an error, or FALSE (checkmark) for no error or a warning. The pop-up option Explain Error (or Explain Warning) gives more information about the error displayed. |
|  | The code output identifies the error or warning. The pop-up option Explain Error (or Explain Warning) gives more information about the error displayed. |
|  | The source string describes the origin of the error or warning. The pop-up option Explain Error (or Explain Warning) gives more information about the error displayed. |

<!--NI_TOPIC bundle=ni-rfpm-api-ref path=rfpmviref/ni-rfpm_is_calibration_action_done.html language=enus -->
## TOPIC 00201: NI-RFPM Is Calibration Action Done VI

- bundle_id: `ni-rfpm-api-ref`
- source_path: `rfpmviref/ni-rfpm_is_calibration_action_done.html`
- source_url: https://docs-be.ni.com/bundle/ni-rfpm-api-ref/raw/resource/enus/rfpmviref/ni-rfpm_is_calibration_action_done.html
- document_id: `ni-rfpm-api-ref`
- page_type: `leaf`
- content_type: ``

NI-RFPM Is Calibration Action Done VI

Installed With:

Checks the status of the current calibration action, and returns an estimate of completion progress as a percentage.

This VI does not support the mmWave subsystem.

[IMAGE alt='NI-RFPM Is Calibration Action Done' src='ni-rfpm_is_calibration_action_done.gif']

|  | instrument handle identifies your instrument session. instrument handle is obtained from the NI-RFPM Init With Resources VI and identifies a particular instrument session. |
| --- | --- |
|  | The error in cluster can accept error information wired from VIs previously called. Use this information to decide if any functionality should be bypassed in the event of errors from other VIs. Right-click the error in control on the front panel and select Explain Error or Explain Warning from the shortcut menu for more information about the error. The status boolean is either TRUE (X) for an error, or FALSE (checkmark) for no error or a warning. The pop-up option Explain Error (or Explain Warning) gives more information about the error displayed. The code input identifies the error or warning. The pop-up option Explain Error (or Explain Warning) gives more information about the error displayed. The source string describes the origin of the error or warning. The pop-up option Explain Error (or Explain Warning) gives more information about the error displayed. |
|  | The status boolean is either TRUE (X) for an error, or FALSE (checkmark) for no error or a warning. The pop-up option Explain Error (or Explain Warning) gives more information about the error displayed. |
|  | The code input identifies the error or warning. The pop-up option Explain Error (or Explain Warning) gives more information about the error displayed. |
|  | The source string describes the origin of the error or warning. The pop-up option Explain Error (or Explain Warning) gives more information about the error displayed. |
|  | instrument handle out passes a reference to your instrument session to the next VI. instrument handle out is obtained from the NI-RFPM Init With Resources VI and identifies a particular instrument session. |
|  | Is Done? returns whether the calibration action is complete. |
|  | Progress returns an estimate of the calibration action progress, expressed as a percentage. |
|  | The error out cluster passes error or warning information out of a VI to be used by other VIs. Use this information to decide if any functionality should be bypassed in the event of errors from other VIs. The status boolean is either TRUE (X) for an error, or FALSE (checkmark) for no error or a warning. The pop-up option Explain Error (or Explain Warning) gives more information about the error displayed. The code output identifies the error or warning. The pop-up option Explain Error (or Explain Warning) gives more information about the error displayed. The source string describes the origin of the error or warning. The pop-up option Explain Error (or Explain Warning) gives more information about the error displayed. |
|  | The status boolean is either TRUE (X) for an error, or FALSE (checkmark) for no error or a warning. The pop-up option Explain Error (or Explain Warning) gives more information about the error displayed. |
|  | The code output identifies the error or warning. The pop-up option Explain Error (or Explain Warning) gives more information about the error displayed. |
|  | The source string describes the origin of the error or warning. The pop-up option Explain Error (or Explain Warning) gives more information about the error displayed. |

<!--NI_TOPIC bundle=ni-rfpm-api-ref path=rfpmviref/ni-rfpm_is_system_calibration_valid.html language=enus -->
## TOPIC 00202: NI-RFPM Is System Calibration Valid VI

- bundle_id: `ni-rfpm-api-ref`
- source_path: `rfpmviref/ni-rfpm_is_system_calibration_valid.html`
- source_url: https://docs-be.ni.com/bundle/ni-rfpm-api-ref/raw/resource/enus/rfpmviref/ni-rfpm_is_system_calibration_valid.html
- document_id: `ni-rfpm-api-ref`
- page_type: `leaf`
- content_type: ``

NI-RFPM Is System Calibration Valid VI

Installed With:

Notifies the user if their system calibration is still valid. To be valid, a system calibration must be within the recommended calibration interval and the temperature of the VST must be near the temperature of the calibration.

This VI does not support the mmWave subsystem.

[IMAGE alt='NI-RFPM Is System Calibration Valid' src='ni-rfpm_is_system_calibration_valid.gif']

|  | instrument handle identifies your instrument session. instrument handle is obtained from the NI-RFPM Init With Resources VI and identifies a particular instrument session. |
| --- | --- |
|  | The error in cluster can accept error information wired from VIs previously called. Use this information to decide if any functionality should be bypassed in the event of errors from other VIs. Right-click the error in control on the front panel and select Explain Error or Explain Warning from the shortcut menu for more information about the error. The status boolean is either TRUE (X) for an error, or FALSE (checkmark) for no error or a warning. The pop-up option Explain Error (or Explain Warning) gives more information about the error displayed. The code input identifies the error or warning. The pop-up option Explain Error (or Explain Warning) gives more information about the error displayed. The source string describes the origin of the error or warning. The pop-up option Explain Error (or Explain Warning) gives more information about the error displayed. |
|  | The status boolean is either TRUE (X) for an error, or FALSE (checkmark) for no error or a warning. The pop-up option Explain Error (or Explain Warning) gives more information about the error displayed. |
|  | The code input identifies the error or warning. The pop-up option Explain Error (or Explain Warning) gives more information about the error displayed. |
|  | The source string describes the origin of the error or warning. The pop-up option Explain Error (or Explain Warning) gives more information about the error displayed. |
|  | instrument handle out passes a reference to your instrument session to the next VI. instrument handle out is obtained from the NI-RFPM Init With Resources VI and identifies a particular instrument session. |
|  | is system calibration valid returns whether the loaded system calibration is valid. If the loaded system calibration is valid, the value is TRUE. If the loaded system calibration is not valid, the value is FALSE. If no system calibration is loaded, the value is FALSE. |
|  | The error out cluster passes error or warning information out of a VI to be used by other VIs. Use this information to decide if any functionality should be bypassed in the event of errors from other VIs. The status boolean is either TRUE (X) for an error, or FALSE (checkmark) for no error or a warning. The pop-up option Explain Error (or Explain Warning) gives more information about the error displayed. The code output identifies the error or warning. The pop-up option Explain Error (or Explain Warning) gives more information about the error displayed. The source string describes the origin of the error or warning. The pop-up option Explain Error (or Explain Warning) gives more information about the error displayed. |
|  | The status boolean is either TRUE (X) for an error, or FALSE (checkmark) for no error or a warning. The pop-up option Explain Error (or Explain Warning) gives more information about the error displayed. |
|  | The code output identifies the error or warning. The pop-up option Explain Error (or Explain Warning) gives more information about the error displayed. |
|  | The source string describes the origin of the error or warning. The pop-up option Explain Error (or Explain Warning) gives more information about the error displayed. |

<!--NI_TOPIC bundle=ni-rfpm-api-ref path=rfpmviref/ni-rfpm_load_calibration_and_configuration.html language=enus -->
## TOPIC 00203: NI-RFPM Load Calibration and Configuration VI

- bundle_id: `ni-rfpm-api-ref`
- source_path: `rfpmviref/ni-rfpm_load_calibration_and_configuration.html`
- source_url: https://docs-be.ni.com/bundle/ni-rfpm-api-ref/raw/resource/enus/rfpmviref/ni-rfpm_load_calibration_and_configuration.html
- document_id: `ni-rfpm-api-ref`
- page_type: `leaf`
- content_type: ``

NI-RFPM Load Calibration and Configuration VI

Installed With:

Loads calibration and sweep setting data from a file.

This VI does not support the mmWave subsystem.

[Details](#details)

[IMAGE alt='NI-RFPM Load Calibration and Configuration' src='ni-rfpm_load_calibration_and_configuration.gif']

|  | instrument handle in passes a reference to the next VI from your instrument session. instrument handle in is obtained from the NI-RFPM Init With Resources VI and identifies a particular instrument session. |
| --- | --- |
|  | Calibration Storage File Path specifies the path to the calibration storage file that NI-RFPM uses to load the calibration data. |
|  | The error in cluster can accept error information wired from VIs previously called. Use this information to decide if any functionality should be bypassed in the event of errors from other VIs. Right-click the error in control on the front panel and select Explain Error or Explain Warning from the shortcut menu for more information about the error. The status boolean is either TRUE (X) for an error, or FALSE (checkmark) for no error or a warning. The pop-up option Explain Error (or Explain Warning) gives more information about the error displayed. The code input identifies the error or warning. The pop-up option Explain Error (or Explain Warning) gives more information about the error displayed. The source string describes the origin of the error or warning. The pop-up option Explain Error (or Explain Warning) gives more information about the error displayed. |
|  | The status boolean is either TRUE (X) for an error, or FALSE (checkmark) for no error or a warning. The pop-up option Explain Error (or Explain Warning) gives more information about the error displayed. |
|  | The code input identifies the error or warning. The pop-up option Explain Error (or Explain Warning) gives more information about the error displayed. |
|  | The source string describes the origin of the error or warning. The pop-up option Explain Error (or Explain Warning) gives more information about the error displayed. |
|  | instrument handle out passes a reference to your instrument session to the next VI. instrument handle out is obtained from the NI-RFPM Init With Resources VI and identifies a particular instrument session. |
|  | The error out cluster passes error or warning information out of a VI to be used by other VIs. Use this information to decide if any functionality should be bypassed in the event of errors from other VIs. The status boolean is either TRUE (X) for an error, or FALSE (checkmark) for no error or a warning. The pop-up option Explain Error (or Explain Warning) gives more information about the error displayed. The code output identifies the error or warning. The pop-up option Explain Error (or Explain Warning) gives more information about the error displayed. The source string describes the origin of the error or warning. The pop-up option Explain Error (or Explain Warning) gives more information about the error displayed. |
|  | The status boolean is either TRUE (X) for an error, or FALSE (checkmark) for no error or a warning. The pop-up option Explain Error (or Explain Warning) gives more information about the error displayed. |
|  | The code output identifies the error or warning. The pop-up option Explain Error (or Explain Warning) gives more information about the error displayed. |
|  | The source string describes the origin of the error or warning. The pop-up option Explain Error (or Explain Warning) gives more information about the error displayed. |

#### Details

|  | Note If you attempt to load two sweep settings of the same name, it will return an error. |
| --- | --- |

<!--NI_TOPIC bundle=ni-rfpm-api-ref path=rfpmviref/ni-rfpm_load_sweep_settings.html language=enus -->
## TOPIC 00204: NI-RFPM Load Sweep Settings VI

- bundle_id: `ni-rfpm-api-ref`
- source_path: `rfpmviref/ni-rfpm_load_sweep_settings.html`
- source_url: https://docs-be.ni.com/bundle/ni-rfpm-api-ref/raw/resource/enus/rfpmviref/ni-rfpm_load_sweep_settings.html
- document_id: `ni-rfpm-api-ref`
- page_type: `leaf`
- content_type: ``

NI-RFPM Load Sweep Settings VI

Installed With:

Loads a sweep settings configuration file into memory so that measurements are performed according to the sweeps defined in the file.

[Details](#details)

[IMAGE alt='NI-RFPM Load Sweep Settings' src='ni-rfpm_load_sweep_settings.gif']

|  | instrument handle identifies your instrument session. instrument handle is obtained from the NI-RFPM Init With Resources VI and identifies a particular instrument session. |
| --- | --- |
|  | Sweep Settings File Path specifies the path of the sweep settings file that NI-RFPM loads. |
|  | The error in cluster can accept error information wired from VIs previously called. Use this information to decide if any functionality should be bypassed in the event of errors from other VIs. Right-click the error in control on the front panel and select Explain Error or Explain Warning from the shortcut menu for more information about the error. The status boolean is either TRUE (X) for an error, or FALSE (checkmark) for no error or a warning. The pop-up option Explain Error (or Explain Warning) gives more information about the error displayed. The code input identifies the error or warning. The pop-up option Explain Error (or Explain Warning) gives more information about the error displayed. The source string describes the origin of the error or warning. The pop-up option Explain Error (or Explain Warning) gives more information about the error displayed. |
|  | The status boolean is either TRUE (X) for an error, or FALSE (checkmark) for no error or a warning. The pop-up option Explain Error (or Explain Warning) gives more information about the error displayed. |
|  | The code input identifies the error or warning. The pop-up option Explain Error (or Explain Warning) gives more information about the error displayed. |
|  | The source string describes the origin of the error or warning. The pop-up option Explain Error (or Explain Warning) gives more information about the error displayed. |
|  | instrument handle out passes a reference to your instrument session to the next VI. instrument handle out is obtained from the NI-RFPM Init With Resources VI and identifies a particular instrument session. |
|  | The error out cluster passes error or warning information out of a VI to be used by other VIs. Use this information to decide if any functionality should be bypassed in the event of errors from other VIs. The status boolean is either TRUE (X) for an error, or FALSE (checkmark) for no error or a warning. The pop-up option Explain Error (or Explain Warning) gives more information about the error displayed. The code output identifies the error or warning. The pop-up option Explain Error (or Explain Warning) gives more information about the error displayed. The source string describes the origin of the error or warning. The pop-up option Explain Error (or Explain Warning) gives more information about the error displayed. |
|  | The status boolean is either TRUE (X) for an error, or FALSE (checkmark) for no error or a warning. The pop-up option Explain Error (or Explain Warning) gives more information about the error displayed. |
|  | The code output identifies the error or warning. The pop-up option Explain Error (or Explain Warning) gives more information about the error displayed. |
|  | The source string describes the origin of the error or warning. The pop-up option Explain Error (or Explain Warning) gives more information about the error displayed. |

#### Details

|  | Note If you attempt to load two sweep settings of the same name, it will return an error |
| --- | --- |

<!--NI_TOPIC bundle=ni-rfpm-api-ref path=rfpmviref/ni-rfpm_pal.html language=enus -->
## TOPIC 00205: NI-RFPM VIs

- bundle_id: `ni-rfpm-api-ref`
- source_path: `rfpmviref/ni-rfpm_pal.html`
- source_url: https://docs-be.ni.com/bundle/ni-rfpm-api-ref/raw/resource/enus/rfpmviref/ni-rfpm_pal.html
- document_id: `ni-rfpm-api-ref`
- page_type: `leaf`
- content_type: ``

NI-RFPM VIs

Installed With:

April 2021

This help file contains technical and programming support for using the NI-RFPM LabVIEW API. This help file provides reference material for the NI-RFPM VIs.

Use the NI-RFPM VIs to develop applications for your STS device.

| Palette Object | Description |
| --- | --- |
| NI-RFPM Close | Closes the device session. |
| NI-RFPM Init With Resources | Initializes a session of the NI-RFPM driver and configures the measurement resources. The NI-RFSA, NI-RFSG, and either NI-RFPM Switch or IVI Switch sessions must be initialized before passing into this VI. No switch session is required for the mmWave subsystem. Pass NULL or the empty string ("") for the Switch handle parameter when using the mmWave subsystem. |
| NI-RFPM Reset | Resets all attributes and devices, including NI-RFSA and NI-RFSG sessions, to their default states. |
| NI-RFPM Reset Device | Resets all attributes and devices, including NI-RFSA and NI-RFSG sessions, to their default states, and clears a latched interlock signal. This VI does not support the mmWave subsystem. |
| NI-RFPM Reset With Options | Performs a selective reset of attributes and underlying driver sessions including NI-RFSA and NI-RFSG sessions. |

| Subpalette | Description |
| --- | --- |
| Calibration | Use the NI-RFPM Calibration VIs to control calibration operations for the STS device. |
| Configuration | Use the NI-RFPM Configuration VIs to configure operations with your STS device. |
| Measurement | Use the NI-RFPM Measurement VIs to control measurement operations with your STS device. |
| Switch | Use the NI-RFPM Switch VIs to control measurement operations with your STS device. |
| Utility | Use the NI-RFPM Utility VIs to access utility features of NI-RFPM. |

<!--NI_TOPIC bundle=ni-rfpm-api-ref path=rfpmviref/ni-rfpm_perform_calibration_action.html language=enus -->
## TOPIC 00206: NI-RFPM Perform Calibration Action VI

- bundle_id: `ni-rfpm-api-ref`
- source_path: `rfpmviref/ni-rfpm_perform_calibration_action.html`
- source_url: https://docs-be.ni.com/bundle/ni-rfpm-api-ref/raw/resource/enus/rfpmviref/ni-rfpm_perform_calibration_action.html
- document_id: `ni-rfpm-api-ref`
- page_type: `leaf`
- content_type: ``

NI-RFPM Perform Calibration Action VI

Installed With:

Performs one calibration action.

This VI does not support the mmWave subsystem.

[IMAGE alt='NI-RFPM Perform Calibration Action' src='ni-rfpm_perform_calibration_action.gif']

|  | Ports specifies a one-dimensional array of port names on which to perform calibration. |
| --- | --- |
|  | instrument handle identifies your instrument session. instrument handle is obtained from the NI-RFPM Init With Resources VI and identifies a particular instrument session. |
|  | Sweep Setting Name specifies the name of the sweep settings for performing a measurement. |
|  | Calibration Action specifies the type of calibration action to perform. Cal Load Board Autocal (QSOLT) NI-RFPM performs the automatic quick short-open-load-through (QSOLT) calibration using the NI RF Multiport Auto Calibration Module. |
| Cal Load Board Autocal (QSOLT) | NI-RFPM performs the automatic quick short-open-load-through (QSOLT) calibration using the NI RF Multiport Auto Calibration Module. |
|  | The error in cluster can accept error information wired from VIs previously called. Use this information to decide if any functionality should be bypassed in the event of errors from other VIs. Right-click the error in control on the front panel and select Explain Error or Explain Warning from the shortcut menu for more information about the error. The status boolean is either TRUE (X) for an error, or FALSE (checkmark) for no error or a warning. The pop-up option Explain Error (or Explain Warning) gives more information about the error displayed. The code input identifies the error or warning. The pop-up option Explain Error (or Explain Warning) gives more information about the error displayed. The source string describes the origin of the error or warning. The pop-up option Explain Error (or Explain Warning) gives more information about the error displayed. |
|  | The status boolean is either TRUE (X) for an error, or FALSE (checkmark) for no error or a warning. The pop-up option Explain Error (or Explain Warning) gives more information about the error displayed. |
|  | The code input identifies the error or warning. The pop-up option Explain Error (or Explain Warning) gives more information about the error displayed. |
|  | The source string describes the origin of the error or warning. The pop-up option Explain Error (or Explain Warning) gives more information about the error displayed. |
|  | instrument handle out passes a reference to your instrument session to the next VI. instrument handle out is obtained from the NI-RFPM Init With Resources VI and identifies a particular instrument session. |
|  | The error out cluster passes error or warning information out of a VI to be used by other VIs. Use this information to decide if any functionality should be bypassed in the event of errors from other VIs. The status boolean is either TRUE (X) for an error, or FALSE (checkmark) for no error or a warning. The pop-up option Explain Error (or Explain Warning) gives more information about the error displayed. The code output identifies the error or warning. The pop-up option Explain Error (or Explain Warning) gives more information about the error displayed. The source string describes the origin of the error or warning. The pop-up option Explain Error (or Explain Warning) gives more information about the error displayed. |
|  | The status boolean is either TRUE (X) for an error, or FALSE (checkmark) for no error or a warning. The pop-up option Explain Error (or Explain Warning) gives more information about the error displayed. |
|  | The code output identifies the error or warning. The pop-up option Explain Error (or Explain Warning) gives more information about the error displayed. |
|  | The source string describes the origin of the error or warning. The pop-up option Explain Error (or Explain Warning) gives more information about the error displayed. |

<!--NI_TOPIC bundle=ni-rfpm-api-ref path=rfpmviref/ni-rfpm_perform_system_calibration.html language=enus -->
## TOPIC 00207: NI-RFPM Perform System Calibration VI

- bundle_id: `ni-rfpm-api-ref`
- source_path: `rfpmviref/ni-rfpm_perform_system_calibration.html`
- source_url: https://docs-be.ni.com/bundle/ni-rfpm-api-ref/raw/resource/enus/rfpmviref/ni-rfpm_perform_system_calibration.html
- document_id: `ni-rfpm-api-ref`
- page_type: `leaf`
- content_type: ``

NI-RFPM Perform System Calibration VI

Installed With:

Performs a system calibration.

This VI does not support the mmWave subsystem.

[IMAGE alt='NI-RFPM Perform System Calibration' src='ni-rfpm_perform_system_calibration.gif']

|  | instrument handle identifies your instrument session. instrument handle is obtained from the NI-RFPM Init With Resources VI and identifies a particular instrument session. |
| --- | --- |
|  | The error in cluster can accept error information wired from VIs previously called. Use this information to decide if any functionality should be bypassed in the event of errors from other VIs. Right-click the error in control on the front panel and select Explain Error or Explain Warning from the shortcut menu for more information about the error. The status boolean is either TRUE (X) for an error, or FALSE (checkmark) for no error or a warning. The pop-up option Explain Error (or Explain Warning) gives more information about the error displayed. The code input identifies the error or warning. The pop-up option Explain Error (or Explain Warning) gives more information about the error displayed. The source string describes the origin of the error or warning. The pop-up option Explain Error (or Explain Warning) gives more information about the error displayed. |
|  | The status boolean is either TRUE (X) for an error, or FALSE (checkmark) for no error or a warning. The pop-up option Explain Error (or Explain Warning) gives more information about the error displayed. |
|  | The code input identifies the error or warning. The pop-up option Explain Error (or Explain Warning) gives more information about the error displayed. |
|  | The source string describes the origin of the error or warning. The pop-up option Explain Error (or Explain Warning) gives more information about the error displayed. |
|  | instrument handle out passes a reference to your instrument session to the next VI. instrument handle out is obtained from the NI-RFPM Init With Resources VI and identifies a particular instrument session. |
|  | The error out cluster passes error or warning information out of a VI to be used by other VIs. Use this information to decide if any functionality should be bypassed in the event of errors from other VIs. The status boolean is either TRUE (X) for an error, or FALSE (checkmark) for no error or a warning. The pop-up option Explain Error (or Explain Warning) gives more information about the error displayed. The code output identifies the error or warning. The pop-up option Explain Error (or Explain Warning) gives more information about the error displayed. The source string describes the origin of the error or warning. The pop-up option Explain Error (or Explain Warning) gives more information about the error displayed. |
|  | The status boolean is either TRUE (X) for an error, or FALSE (checkmark) for no error or a warning. The pop-up option Explain Error (or Explain Warning) gives more information about the error displayed. |
|  | The code output identifies the error or warning. The pop-up option Explain Error (or Explain Warning) gives more information about the error displayed. |
|  | The source string describes the origin of the error or warning. The pop-up option Explain Error (or Explain Warning) gives more information about the error displayed. |

<!--NI_TOPIC bundle=ni-rfpm-api-ref path=rfpmviref/ni-rfpm_property_node.html language=enus -->
## TOPIC 00208: NI-RFPM Property Node VI

- bundle_id: `ni-rfpm-api-ref`
- source_path: `rfpmviref/ni-rfpm_property_node.html`
- source_url: https://docs-be.ni.com/bundle/ni-rfpm-api-ref/raw/resource/enus/rfpmviref/ni-rfpm_property_node.html
- document_id: `ni-rfpm-api-ref`
- page_type: `leaf`
- content_type: ``

NI-RFPM Property Node VI

Installed With:

Gets (reads) or sets (writes) [NI-RFPM properties](../rfpmpropref/cnirfpm.html). When you read a property, NI-RFPM analyzes the current configuration to return the coerced value for that property. Setting a property may transition the session to the Configuration state.

[IMAGE alt='NI-RFPM Property Node' src='ni-rfpm_property_node.gif']

|  | instrument handle identifies your instrument session. instrument handle is obtained from the NI-RFPM Init With Resources VI and identifies a particular instrument session. |
| --- | --- |
|  | The error in cluster can accept error information wired from VIs previously called. Use this information to decide if any functionality should be bypassed in the event of errors from other VIs. Right-click the error in control on the front panel and select Explain Error or Explain Warning from the shortcut menu for more information about the error. The status boolean is either TRUE (X) for an error, or FALSE (checkmark) for no error or a warning. The pop-up option Explain Error (or Explain Warning) gives more information about the error displayed. The code input identifies the error or warning. The pop-up option Explain Error (or Explain Warning) gives more information about the error displayed. The source string describes the origin of the error or warning. The pop-up option Explain Error (or Explain Warning) gives more information about the error displayed. |
|  | The status boolean is either TRUE (X) for an error, or FALSE (checkmark) for no error or a warning. The pop-up option Explain Error (or Explain Warning) gives more information about the error displayed. |
|  | The code input identifies the error or warning. The pop-up option Explain Error (or Explain Warning) gives more information about the error displayed. |
|  | The source string describes the origin of the error or warning. The pop-up option Explain Error (or Explain Warning) gives more information about the error displayed. |
|  | instrument handle out passes a reference to your instrument session to the next VI. instrument handle out is obtained from the NI-RFPM Init With Resources VI and identifies a particular instrument session. |
|  | The error out cluster passes error or warning information out of a VI to be used by other VIs. Use this information to decide if any functionality should be bypassed in the event of errors from other VIs. The status boolean is either TRUE (X) for an error, or FALSE (checkmark) for no error or a warning. The pop-up option Explain Error (or Explain Warning) gives more information about the error displayed. The code output identifies the error or warning. The pop-up option Explain Error (or Explain Warning) gives more information about the error displayed. The source string describes the origin of the error or warning. The pop-up option Explain Error (or Explain Warning) gives more information about the error displayed. |
|  | The status boolean is either TRUE (X) for an error, or FALSE (checkmark) for no error or a warning. The pop-up option Explain Error (or Explain Warning) gives more information about the error displayed. |
|  | The code output identifies the error or warning. The pop-up option Explain Error (or Explain Warning) gives more information about the error displayed. |
|  | The source string describes the origin of the error or warning. The pop-up option Explain Error (or Explain Warning) gives more information about the error displayed. |

<!--NI_TOPIC bundle=ni-rfpm-api-ref path=rfpmviref/ni-rfpm_read_available_user_calibration_information.html language=enus -->
## TOPIC 00209: NI-RFPM Read Available User Calibration Information VI

- bundle_id: `ni-rfpm-api-ref`
- source_path: `rfpmviref/ni-rfpm_read_available_user_calibration_information.html`
- source_url: https://docs-be.ni.com/bundle/ni-rfpm-api-ref/raw/resource/enus/rfpmviref/ni-rfpm_read_available_user_calibration_information.html
- document_id: `ni-rfpm-api-ref`
- page_type: `leaf`
- content_type: ``

NI-RFPM Read Available User Calibration Information VI

Installed With:

Reads the available user calibration sweep name and port list, as well as date, time, and temperature for the specified sweep type.

This VI does not support the mmWave subsystem.

#### NI-RFPM Read Available User Vector Calibration Information

Returns information about what ports are calibrated and for which sweep settings those ports were calibrated, as well as date, time, and temperature, for vector calibrations.

[IMAGE alt='NI-RFPM Read Available User Vector Calibration Information' src='ni-rfpm_read_available_user_vector_calibration_information.gif']

|  | instrument handle identifies your instrument session. instrument handle is obtained from the NI-RFPM Init With Resources VI and identifies a particular instrument session. |
| --- | --- |
|  | The error in cluster can accept error information wired from VIs previously called. Use this information to decide if any functionality should be bypassed in the event of errors from other VIs. Right-click the error in control on the front panel and select Explain Error or Explain Warning from the shortcut menu for more information about the error. The status boolean is either TRUE (X) for an error, or FALSE (checkmark) for no error or a warning. The pop-up option Explain Error (or Explain Warning) gives more information about the error displayed. The code input identifies the error or warning. The pop-up option Explain Error (or Explain Warning) gives more information about the error displayed. The source string describes the origin of the error or warning. The pop-up option Explain Error (or Explain Warning) gives more information about the error displayed. |
|  | The status boolean is either TRUE (X) for an error, or FALSE (checkmark) for no error or a warning. The pop-up option Explain Error (or Explain Warning) gives more information about the error displayed. |
|  | The code input identifies the error or warning. The pop-up option Explain Error (or Explain Warning) gives more information about the error displayed. |
|  | The source string describes the origin of the error or warning. The pop-up option Explain Error (or Explain Warning) gives more information about the error displayed. |
|  | instrument handle out passes a reference to your instrument session to the next VI. instrument handle out is obtained from the NI-RFPM Init With Resources VI and identifies a particular instrument session. |
|  | Sweep Setting Names returns an array of the calibrated sweep setting names. |
|  | Ports returns a two-dimensional array containing an array of ports for each sweep setting name on which the calibration action was performed. |
|  | Dates\\Times returns a timestamp for when the system calibration was performed. |
|  | The error out cluster passes error or warning information out of a VI to be used by other VIs. Use this information to decide if any functionality should be bypassed in the event of errors from other VIs. The status boolean is either TRUE (X) for an error, or FALSE (checkmark) for no error or a warning. The pop-up option Explain Error (or Explain Warning) gives more information about the error displayed. The code output identifies the error or warning. The pop-up option Explain Error (or Explain Warning) gives more information about the error displayed. The source string describes the origin of the error or warning. The pop-up option Explain Error (or Explain Warning) gives more information about the error displayed. |
|  | The status boolean is either TRUE (X) for an error, or FALSE (checkmark) for no error or a warning. The pop-up option Explain Error (or Explain Warning) gives more information about the error displayed. |
|  | The code output identifies the error or warning. The pop-up option Explain Error (or Explain Warning) gives more information about the error displayed. |
|  | The source string describes the origin of the error or warning. The pop-up option Explain Error (or Explain Warning) gives more information about the error displayed. |
|  | Temperatures returns an array of temperatures that specify the temperature of the STS device at the time of calibration. |

#### NI-RFPM Read Available User Source Offset Calibration Information

Returns information about what ports are calibrated and for which sweep settings those ports were calibrated, as well as date, time, and temperature for source calibrations.

[IMAGE alt='NI-RFPM Read Available User Source Offset Calibration Information' src='ni-rfpm_read_available_user_source_offset_calibration_information.gif']

|  | instrument handle identifies your instrument session. instrument handle is obtained from the NI-RFPM Init With Resources VI and identifies a particular instrument session. |
| --- | --- |
|  | The error in cluster can accept error information wired from VIs previously called. Use this information to decide if any functionality should be bypassed in the event of errors from other VIs. Right-click the error in control on the front panel and select Explain Error or Explain Warning from the shortcut menu for more information about the error. The status boolean is either TRUE (X) for an error, or FALSE (checkmark) for no error or a warning. The pop-up option Explain Error (or Explain Warning) gives more information about the error displayed. The code input identifies the error or warning. The pop-up option Explain Error (or Explain Warning) gives more information about the error displayed. The source string describes the origin of the error or warning. The pop-up option Explain Error (or Explain Warning) gives more information about the error displayed. |
|  | The status boolean is either TRUE (X) for an error, or FALSE (checkmark) for no error or a warning. The pop-up option Explain Error (or Explain Warning) gives more information about the error displayed. |
|  | The code input identifies the error or warning. The pop-up option Explain Error (or Explain Warning) gives more information about the error displayed. |
|  | The source string describes the origin of the error or warning. The pop-up option Explain Error (or Explain Warning) gives more information about the error displayed. |
|  | instrument handle out passes a reference to your instrument session to the next VI. instrument handle out is obtained from the NI-RFPM Init With Resources VI and identifies a particular instrument session. |
|  | Sweep Setting Names returns an array of the calibrated sweep setting names. |
|  | Ports returns a two-dimensional array containing an array of ports for each sweep setting name on which the calibration action was performed. |
|  | Dates\\Times returns a timestamp for when the system calibration was performed. |
|  | The error out cluster passes error or warning information out of a VI to be used by other VIs. Use this information to decide if any functionality should be bypassed in the event of errors from other VIs. The status boolean is either TRUE (X) for an error, or FALSE (checkmark) for no error or a warning. The pop-up option Explain Error (or Explain Warning) gives more information about the error displayed. The code output identifies the error or warning. The pop-up option Explain Error (or Explain Warning) gives more information about the error displayed. The source string describes the origin of the error or warning. The pop-up option Explain Error (or Explain Warning) gives more information about the error displayed. |
|  | The status boolean is either TRUE (X) for an error, or FALSE (checkmark) for no error or a warning. The pop-up option Explain Error (or Explain Warning) gives more information about the error displayed. |
|  | The code output identifies the error or warning. The pop-up option Explain Error (or Explain Warning) gives more information about the error displayed. |
|  | The source string describes the origin of the error or warning. The pop-up option Explain Error (or Explain Warning) gives more information about the error displayed. |
|  | Temperatures returns an array of temperatures that specify the temperature of the STS device at the time of calibration. |

#### NI-RFPM Read Available User Receiver Offset Calibration Information

Returns information about what ports are calibrated and for which sweep settings those ports were calibrated, as well as date, time, and temperature for receiver calibrations.

[IMAGE alt='NI-RFPM Read Available User Receiver Offset Calibration Information' src='ni-rfpm_read_available_user_receiver_offset_calibration_information.gif']

|  | instrument handle identifies your instrument session. instrument handle is obtained from the NI-RFPM Init With Resources VI and identifies a particular instrument session. |
| --- | --- |
|  | The error in cluster can accept error information wired from VIs previously called. Use this information to decide if any functionality should be bypassed in the event of errors from other VIs. Right-click the error in control on the front panel and select Explain Error or Explain Warning from the shortcut menu for more information about the error. The status boolean is either TRUE (X) for an error, or FALSE (checkmark) for no error or a warning. The pop-up option Explain Error (or Explain Warning) gives more information about the error displayed. The code input identifies the error or warning. The pop-up option Explain Error (or Explain Warning) gives more information about the error displayed. The source string describes the origin of the error or warning. The pop-up option Explain Error (or Explain Warning) gives more information about the error displayed. |
|  | The status boolean is either TRUE (X) for an error, or FALSE (checkmark) for no error or a warning. The pop-up option Explain Error (or Explain Warning) gives more information about the error displayed. |
|  | The code input identifies the error or warning. The pop-up option Explain Error (or Explain Warning) gives more information about the error displayed. |
|  | The source string describes the origin of the error or warning. The pop-up option Explain Error (or Explain Warning) gives more information about the error displayed. |
|  | instrument handle out passes a reference to your instrument session to the next VI. instrument handle out is obtained from the NI-RFPM Init With Resources VI and identifies a particular instrument session. |
|  | Sweep Setting Names returns an array of the calibrated sweep setting names. |
|  | Ports returns a two-dimensional array containing an array of ports for each sweep setting name on which the calibration action was performed. |
|  | Dates\\Times returns a timestamp for when the system calibration was performed. |
|  | The error out cluster passes error or warning information out of a VI to be used by other VIs. Use this information to decide if any functionality should be bypassed in the event of errors from other VIs. The status boolean is either TRUE (X) for an error, or FALSE (checkmark) for no error or a warning. The pop-up option Explain Error (or Explain Warning) gives more information about the error displayed. The code output identifies the error or warning. The pop-up option Explain Error (or Explain Warning) gives more information about the error displayed. The source string describes the origin of the error or warning. The pop-up option Explain Error (or Explain Warning) gives more information about the error displayed. |
|  | The status boolean is either TRUE (X) for an error, or FALSE (checkmark) for no error or a warning. The pop-up option Explain Error (or Explain Warning) gives more information about the error displayed. |
|  | The code output identifies the error or warning. The pop-up option Explain Error (or Explain Warning) gives more information about the error displayed. |
|  | The source string describes the origin of the error or warning. The pop-up option Explain Error (or Explain Warning) gives more information about the error displayed. |
|  | Temperatures returns an array of temperatures that specify the temperature of the STS device at the time of calibration. |

<!--NI_TOPIC bundle=ni-rfpm-api-ref path=rfpmviref/ni-rfpm_read_connected_rx_paths.html language=enus -->
## TOPIC 00210: NI-RFPM Read Connected RX Paths VI

- bundle_id: `ni-rfpm-api-ref`
- source_path: `rfpmviref/ni-rfpm_read_connected_rx_paths.html`
- source_url: https://docs-be.ni.com/bundle/ni-rfpm-api-ref/raw/resource/enus/rfpmviref/ni-rfpm_read_connected_rx_paths.html
- document_id: `ni-rfpm-api-ref`
- page_type: `leaf`
- content_type: ``

NI-RFPM Read Connected RX Paths VI

Installed With:

Queries which STS receive paths are currently connected.

This VI does not support the mmWave subsystem.

#### NI-RFPM Read Connected RX Paths By Parameters

Queries which STS receieve paths are currently connected, and returns arrays of receiver path enums, receiver coupling path enums and port strings.

[IMAGE alt='NI-RFPM Read Connected RX Paths By Parameters' src='ni-rfpm_read_connected_rx_paths_by_parameters.gif']

|  | instrument handle identifies your instrument session. instrument handle is obtained from the NI-RFPM Init With Resources VI and identifies a particular instrument session. |
| --- | --- |
|  | The error in (no error) cluster can accept error information wired from VIs previously called. Use this information to decide if any functionality should be bypassed in the event of errors from other VIs. Right-click the error in (no error) control on the front panel and select Explain Error or Explain Warning from the shortcut menu for more information about the error. The status boolean is either TRUE (X) for an error, or FALSE (checkmark) for no error or a warning. The pop-up option Explain Error (or Explain Warning) gives more information about the error displayed. The code input identifies the error or warning. The pop-up option Explain Error (or Explain Warning) gives more information about the error displayed. The source string describes the origin of the error or warning. The pop-up option Explain Error (or Explain Warning) gives more information about the error displayed. |
|  | The status boolean is either TRUE (X) for an error, or FALSE (checkmark) for no error or a warning. The pop-up option Explain Error (or Explain Warning) gives more information about the error displayed. |
|  | The code input identifies the error or warning. The pop-up option Explain Error (or Explain Warning) gives more information about the error displayed. |
|  | The source string describes the origin of the error or warning. The pop-up option Explain Error (or Explain Warning) gives more information about the error displayed. |
|  | instrument handle out passes a reference to your instrument session to the next VI. instrument handle out is obtained from the NI-RFPM Init With Resources VI and identifies a particular instrument session. |
|  | The error out cluster passes error or warning information out of a VI to be used by other VIs. Use this information to decide if any functionality should be bypassed in the event of errors from other VIs. The status boolean is either TRUE (X) for an error, or FALSE (checkmark) for no error or a warning. The pop-up option Explain Error (or Explain Warning) gives more information about the error displayed. The code output identifies the error or warning. The pop-up option Explain Error (or Explain Warning) gives more information about the error displayed. The source string describes the origin of the error or warning. The pop-up option Explain Error (or Explain Warning) gives more information about the error displayed. |
|  | The status boolean is either TRUE (X) for an error, or FALSE (checkmark) for no error or a warning. The pop-up option Explain Error (or Explain Warning) gives more information about the error displayed. |
|  | The code output identifies the error or warning. The pop-up option Explain Error (or Explain Warning) gives more information about the error displayed. |
|  | The source string describes the origin of the error or warning. The pop-up option Explain Error (or Explain Warning) gives more information about the error displayed. |
|  | Receiver Coupling Paths returns a list of STS receieve coupling paths used in current connections. |
|  | Ports returns a list of STS receieve ports used in current connections. |
|  | RX Paths returns a list of STS receive paths used in current connections. |

#### NI-RFPM Read Connected RX Paths By Switch Path String

Queries which RX switch paths are currently connected and returns a string array.

[IMAGE alt='NI-RFPM Read Connected RX Paths By Switch Path String' src='ni-rfpm_read_connected_rx_paths_by_switch_path_string.gif']

|  | instrument handle identifies your instrument session. instrument handle is obtained from the NI-RFPM Init With Resources VI and identifies a particular instrument session. |
| --- | --- |
|  | The error in (no error) cluster can accept error information wired from VIs previously called. Use this information to decide if any functionality should be bypassed in the event of errors from other VIs. Right-click the error in (no error) control on the front panel and select Explain Error or Explain Warning from the shortcut menu for more information about the error. The status boolean is either TRUE (X) for an error, or FALSE (checkmark) for no error or a warning. The pop-up option Explain Error (or Explain Warning) gives more information about the error displayed. The code input identifies the error or warning. The pop-up option Explain Error (or Explain Warning) gives more information about the error displayed. The source string describes the origin of the error or warning. The pop-up option Explain Error (or Explain Warning) gives more information about the error displayed. |
|  | The status boolean is either TRUE (X) for an error, or FALSE (checkmark) for no error or a warning. The pop-up option Explain Error (or Explain Warning) gives more information about the error displayed. |
|  | The code input identifies the error or warning. The pop-up option Explain Error (or Explain Warning) gives more information about the error displayed. |
|  | The source string describes the origin of the error or warning. The pop-up option Explain Error (or Explain Warning) gives more information about the error displayed. |
|  | instrument handle out passes a reference to your instrument session to the next VI. instrument handle out is obtained from the NI-RFPM Init With Resources VI and identifies a particular instrument session. |
|  | The error out cluster passes error or warning information out of a VI to be used by other VIs. Use this information to decide if any functionality should be bypassed in the event of errors from other VIs. The status boolean is either TRUE (X) for an error, or FALSE (checkmark) for no error or a warning. The pop-up option Explain Error (or Explain Warning) gives more information about the error displayed. The code output identifies the error or warning. The pop-up option Explain Error (or Explain Warning) gives more information about the error displayed. The source string describes the origin of the error or warning. The pop-up option Explain Error (or Explain Warning) gives more information about the error displayed. |
|  | The status boolean is either TRUE (X) for an error, or FALSE (checkmark) for no error or a warning. The pop-up option Explain Error (or Explain Warning) gives more information about the error displayed. |
|  | The code output identifies the error or warning. The pop-up option Explain Error (or Explain Warning) gives more information about the error displayed. |
|  | The source string describes the origin of the error or warning. The pop-up option Explain Error (or Explain Warning) gives more information about the error displayed. |
|  | Connected RX Paths returns a list of connected RX switch path strings. |

<!--NI_TOPIC bundle=ni-rfpm-api-ref path=rfpmviref/ni-rfpm_read_connected_tx_paths.html language=enus -->
## TOPIC 00211: NI-RFPM Read Connected TX Paths VI

- bundle_id: `ni-rfpm-api-ref`
- source_path: `rfpmviref/ni-rfpm_read_connected_tx_paths.html`
- source_url: https://docs-be.ni.com/bundle/ni-rfpm-api-ref/raw/resource/enus/rfpmviref/ni-rfpm_read_connected_tx_paths.html
- document_id: `ni-rfpm-api-ref`
- page_type: `leaf`
- content_type: ``

NI-RFPM Read Connected TX Paths VI

Installed With:

Queries which TX switch paths are currently connected and returns an array of path enums and port strings.

This VI does not support the mmWave subsystem.

#### NI-RFPM Read Connected TX Paths By Parameters

Queries which STS transmit paths are currently connected and returns arrays of transmit enums and port strings.

[IMAGE alt='NI-RFPM Read Connected TX Paths By Parameters' src='ni-rfpm_read_connected_tx_paths_by_parameters.gif']

|  | instrument handle identifies your instrument session. instrument handle is obtained from the NI-RFPM Init With Resources VI and identifies a particular instrument session. |
| --- | --- |
|  | The error in (no error) cluster can accept error information wired from VIs previously called. Use this information to decide if any functionality should be bypassed in the event of errors from other VIs. Right-click the error in (no error) control on the front panel and select Explain Error or Explain Warning from the shortcut menu for more information about the error. The status boolean is either TRUE (X) for an error, or FALSE (checkmark) for no error or a warning. The pop-up option Explain Error (or Explain Warning) gives more information about the error displayed. The code input identifies the error or warning. The pop-up option Explain Error (or Explain Warning) gives more information about the error displayed. The source string describes the origin of the error or warning. The pop-up option Explain Error (or Explain Warning) gives more information about the error displayed. |
|  | The status boolean is either TRUE (X) for an error, or FALSE (checkmark) for no error or a warning. The pop-up option Explain Error (or Explain Warning) gives more information about the error displayed. |
|  | The code input identifies the error or warning. The pop-up option Explain Error (or Explain Warning) gives more information about the error displayed. |
|  | The source string describes the origin of the error or warning. The pop-up option Explain Error (or Explain Warning) gives more information about the error displayed. |
|  | instrument handle out passes a reference to your instrument session to the next VI. instrument handle out is obtained from the NI-RFPM Init With Resources VI and identifies a particular instrument session. |
|  | The error out cluster passes error or warning information out of a VI to be used by other VIs. Use this information to decide if any functionality should be bypassed in the event of errors from other VIs. The status boolean is either TRUE (X) for an error, or FALSE (checkmark) for no error or a warning. The pop-up option Explain Error (or Explain Warning) gives more information about the error displayed. The code output identifies the error or warning. The pop-up option Explain Error (or Explain Warning) gives more information about the error displayed. The source string describes the origin of the error or warning. The pop-up option Explain Error (or Explain Warning) gives more information about the error displayed. |
|  | The status boolean is either TRUE (X) for an error, or FALSE (checkmark) for no error or a warning. The pop-up option Explain Error (or Explain Warning) gives more information about the error displayed. |
|  | The code output identifies the error or warning. The pop-up option Explain Error (or Explain Warning) gives more information about the error displayed. |
|  | The source string describes the origin of the error or warning. The pop-up option Explain Error (or Explain Warning) gives more information about the error displayed. |
|  | TX Paths returns a list of STS transmit paths used in current connections. |
|  | Ports returns a list of STS transmit ports used in current connections. |

#### NI-RFPM Read Connected TX Paths By Switch Path String

Queries which TX switch paths are currently connected and returns a string array.

[IMAGE alt='NI-RFPM Read Connected TX Paths By Switch Path String' src='ni-rfpm_read_connected_tx_paths_by_switch_path_string.gif']

|  | instrument handle identifies your instrument session. instrument handle is obtained from the NI-RFPM Init With Resources VI and identifies a particular instrument session. |
| --- | --- |
|  | The error in (no error) cluster can accept error information wired from VIs previously called. Use this information to decide if any functionality should be bypassed in the event of errors from other VIs. Right-click the error in (no error) control on the front panel and select Explain Error or Explain Warning from the shortcut menu for more information about the error. The status boolean is either TRUE (X) for an error, or FALSE (checkmark) for no error or a warning. The pop-up option Explain Error (or Explain Warning) gives more information about the error displayed. The code input identifies the error or warning. The pop-up option Explain Error (or Explain Warning) gives more information about the error displayed. The source string describes the origin of the error or warning. The pop-up option Explain Error (or Explain Warning) gives more information about the error displayed. |
|  | The status boolean is either TRUE (X) for an error, or FALSE (checkmark) for no error or a warning. The pop-up option Explain Error (or Explain Warning) gives more information about the error displayed. |
|  | The code input identifies the error or warning. The pop-up option Explain Error (or Explain Warning) gives more information about the error displayed. |
|  | The source string describes the origin of the error or warning. The pop-up option Explain Error (or Explain Warning) gives more information about the error displayed. |
|  | instrument handle out passes a reference to your instrument session to the next VI. instrument handle out is obtained from the NI-RFPM Init With Resources VI and identifies a particular instrument session. |
|  | The error out cluster passes error or warning information out of a VI to be used by other VIs. Use this information to decide if any functionality should be bypassed in the event of errors from other VIs. The status boolean is either TRUE (X) for an error, or FALSE (checkmark) for no error or a warning. The pop-up option Explain Error (or Explain Warning) gives more information about the error displayed. The code output identifies the error or warning. The pop-up option Explain Error (or Explain Warning) gives more information about the error displayed. The source string describes the origin of the error or warning. The pop-up option Explain Error (or Explain Warning) gives more information about the error displayed. |
|  | The status boolean is either TRUE (X) for an error, or FALSE (checkmark) for no error or a warning. The pop-up option Explain Error (or Explain Warning) gives more information about the error displayed. |
|  | The code output identifies the error or warning. The pop-up option Explain Error (or Explain Warning) gives more information about the error displayed. |
|  | The source string describes the origin of the error or warning. The pop-up option Explain Error (or Explain Warning) gives more information about the error displayed. |
|  | Connected TX Paths returns a list of connected TX switch path strings. |

<!--NI_TOPIC bundle=ni-rfpm-api-ref path=rfpmviref/ni-rfpm_read_measurement_resources.html language=enus -->
## TOPIC 00212: NI-RFPM Read Measurement Resources VI

- bundle_id: `ni-rfpm-api-ref`
- source_path: `rfpmviref/ni-rfpm_read_measurement_resources.html`
- source_url: https://docs-be.ni.com/bundle/ni-rfpm-api-ref/raw/resource/enus/rfpmviref/ni-rfpm_read_measurement_resources.html
- document_id: `ni-rfpm-api-ref`
- page_type: `leaf`
- content_type: ``

NI-RFPM Read Measurement Resources VI

Installed With:

Returns the stored handles to the measurement resources used by NI-RFPM. These are the same handles that are passed into the [NI-RFPM Init With Resources](ni-rfpm_init_with_resources.html) VI.

[IMAGE alt='NI-RFPM Read Measurement Resources' src='ni-rfpm_read_measurement_resources.gif']

|  | instrument handle identifies your instrument session. instrument handle is obtained from the NI-RFPM Init With Resources VI and identifies a particular instrument session. |
| --- | --- |
|  | The error in cluster can accept error information wired from VIs previously called. Use this information to decide if any functionality should be bypassed in the event of errors from other VIs. Right-click the error in control on the front panel and select Explain Error or Explain Warning from the shortcut menu for more information about the error. The status boolean is either TRUE (X) for an error, or FALSE (checkmark) for no error or a warning. The pop-up option Explain Error (or Explain Warning) gives more information about the error displayed. The code input identifies the error or warning. The pop-up option Explain Error (or Explain Warning) gives more information about the error displayed. The source string describes the origin of the error or warning. The pop-up option Explain Error (or Explain Warning) gives more information about the error displayed. |
|  | The status boolean is either TRUE (X) for an error, or FALSE (checkmark) for no error or a warning. The pop-up option Explain Error (or Explain Warning) gives more information about the error displayed. |
|  | The code input identifies the error or warning. The pop-up option Explain Error (or Explain Warning) gives more information about the error displayed. |
|  | The source string describes the origin of the error or warning. The pop-up option Explain Error (or Explain Warning) gives more information about the error displayed. |
|  | instrument handle out passes a reference to your instrument session to the next VI. instrument handle out is obtained from the NI-RFPM Init With Resources VI and identifies a particular instrument session. |
|  | RFSA handle specifies a handle to the NI-RFSA device. |
|  | RFSG handle specifies a handle to the NI-RFSG device. |
|  | Switch handle returns a handle to the NI-RFPM switch. |
|  | The error out cluster passes error or warning information out of a VI to be used by other VIs. Use this information to decide if any functionality should be bypassed in the event of errors from other VIs. The status boolean is either TRUE (X) for an error, or FALSE (checkmark) for no error or a warning. The pop-up option Explain Error (or Explain Warning) gives more information about the error displayed. The code output identifies the error or warning. The pop-up option Explain Error (or Explain Warning) gives more information about the error displayed. The source string describes the origin of the error or warning. The pop-up option Explain Error (or Explain Warning) gives more information about the error displayed. |
|  | The status boolean is either TRUE (X) for an error, or FALSE (checkmark) for no error or a warning. The pop-up option Explain Error (or Explain Warning) gives more information about the error displayed. |
|  | The code output identifies the error or warning. The pop-up option Explain Error (or Explain Warning) gives more information about the error displayed. |
|  | The source string describes the origin of the error or warning. The pop-up option Explain Error (or Explain Warning) gives more information about the error displayed. |

<!--NI_TOPIC bundle=ni-rfpm-api-ref path=rfpmviref/ni-rfpm_read_receiver_settling_time.html language=enus -->
## TOPIC 00213: NI-RFPM Read Receiver Settling Time VI

- bundle_id: `ni-rfpm-api-ref`
- source_path: `rfpmviref/ni-rfpm_read_receiver_settling_time.html`
- source_url: https://docs-be.ni.com/bundle/ni-rfpm-api-ref/raw/resource/enus/rfpmviref/ni-rfpm_read_receiver_settling_time.html
- document_id: `ni-rfpm-api-ref`
- page_type: `leaf`
- content_type: ``

NI-RFPM Read Receiver Settling Time VI

Installed With:

Queries how long a user must wait for the signal at the NI-RFPM switch receiver output channel to settle within the receiver amplitude accuracy specified by the [Receiver Amplitude Settling](../rfpmpropref/pnirfpm_receiveramplitudesettling.html) property. When NI-RFPM de-embedding is enabled, the reference level is defined at the DUT reference plane.

This VI does not support the mmWave subsystem.

The settling time is dependent on the NI-RFPM switch receiver path as well as the frequency and the reference level of the signal present at the NI-RFPM switch receiver input channel.

Related Information

[De-embedding](../rfpmhelp/deembedding.html)

#### NI-RFPM Read Receiver Settling Time By Parameter

Queries how long a user must wait for the signal at the NI-RFPM switch receiver output channel to settle within the receiver amplitude accuracy specified by the [Receiver Amplitude Settling](../rfpmpropref/pnirfpm_receiveramplitudesettling.html) property after setting the specified NI-RFPM switch receiver path. When NI-RFPM de-embedding is enabled, the reference level is defined at the DUT reference plane.

[IMAGE alt='NI-RFPM Read Receiver Settling Time By Parameter' src='ni-rfpm_read_receiver_settling_time_by_parameter.gif']

|  | port specifies the receiver port to settle. |
| --- | --- |
|  | instrument handle identifies your instrument session. instrument handle is obtained from the NI-RFPM Init With Resources VI and identifies a particular instrument session. |
|  | Receiver Path specifies the receiver path used to fetch the receiver settling time data. Direct NI-RFPM uses the receiver direct path through the STS device. Gain NI-RFPM uses the receiver amplified path through the STS device. Loop NI-RFPM uses the path through the receiver bypass loop of the STS device. |
| Direct | NI-RFPM uses the receiver direct path through the STS device. |
| Gain | NI-RFPM uses the receiver amplified path through the STS device. |
| Loop | NI-RFPM uses the path through the receiver bypass loop of the STS device. |
|  | Frequency specifies the frequency of the signal present at the NI-RFPM Switch receiver input channel, in Hz. |
|  | Reference Level specifies the reference level of the NI-RFPM receiver port in decibels milliwatt (dBm). When NI-RFPM de-embedding is enabled, the reference level is defined at the DUT reference plane. |
|  | The error in cluster can accept error information wired from VIs previously called. Use this information to decide if any functionality should be bypassed in the event of errors from other VIs. Right-click the error in control on the front panel and select Explain Error or Explain Warning from the shortcut menu for more information about the error. The status boolean is either TRUE (X) for an error, or FALSE (checkmark) for no error or a warning. The pop-up option Explain Error (or Explain Warning) gives more information about the error displayed. The code input identifies the error or warning. The pop-up option Explain Error (or Explain Warning) gives more information about the error displayed. The source string describes the origin of the error or warning. The pop-up option Explain Error (or Explain Warning) gives more information about the error displayed. |
|  | The status boolean is either TRUE (X) for an error, or FALSE (checkmark) for no error or a warning. The pop-up option Explain Error (or Explain Warning) gives more information about the error displayed. |
|  | The code input identifies the error or warning. The pop-up option Explain Error (or Explain Warning) gives more information about the error displayed. |
|  | The source string describes the origin of the error or warning. The pop-up option Explain Error (or Explain Warning) gives more information about the error displayed. |
|  | Receiver Coupling Path specifies the port module coupling path to connect using the underlying switch session. Coupled NI-RFPM uses the test receiver coupled path. Direct NI-RFPM uses the direct receiver path. LNA NI-RFPM uses the LNA receiver path. |
| Coupled | NI-RFPM uses the test receiver coupled path. |
| Direct | NI-RFPM uses the direct receiver path. |
| LNA | NI-RFPM uses the LNA receiver path. |
|  | instrument handle out passes a reference to your instrument session to the next VI. instrument handle out is obtained from the NI-RFPM Init With Resources VI and identifies a particular instrument session. |
|  | Settling Time in Secondsreturns the time, in seconds, required for the signal at the specified NI-RFPM Switch receiver path output channel to settle within the specified receiver amplitude settling. |
|  | The error out cluster passes error or warning information out of a VI to be used by other VIs. Use this information to decide if any functionality should be bypassed in the event of errors from other VIs. The status boolean is either TRUE (X) for an error, or FALSE (checkmark) for no error or a warning. The pop-up option Explain Error (or Explain Warning) gives more information about the error displayed. The code output identifies the error or warning. The pop-up option Explain Error (or Explain Warning) gives more information about the error displayed. The source string describes the origin of the error or warning. The pop-up option Explain Error (or Explain Warning) gives more information about the error displayed. |
|  | The status boolean is either TRUE (X) for an error, or FALSE (checkmark) for no error or a warning. The pop-up option Explain Error (or Explain Warning) gives more information about the error displayed. |
|  | The code output identifies the error or warning. The pop-up option Explain Error (or Explain Warning) gives more information about the error displayed. |
|  | The source string describes the origin of the error or warning. The pop-up option Explain Error (or Explain Warning) gives more information about the error displayed. |

#### NI-RFPM Read Receiver Settling Time By Switch Path String

Queries how long a user must wait for the signal at the NI-RFPM switch receiver output channel to settle within the receiver amplitude accuracy specified by the [Receiver Amplitude Settling](../rfpmpropref/pnirfpm_receiveramplitudesettling.html) property after setting the specified NI-RFPM switch receiver path. When NI-RFPM de-embedding is enabled, the reference level is defined at the DUT reference plane.

[IMAGE alt='NI-RFPM Read Receiver Settling Time By Switch Path String' src='ni-rfpm_read_receiver_settling_time_by_switch_path_string.gif']

|  | instrument handle identifies your instrument session. instrument handle is obtained from the NI-RFPM Init With Resources VI and identifies a particular instrument session. |
| --- | --- |
|  | Receiver Path specifies the NI-RFPM Switch receiver path to fetch settling time for. |
|  | Frequency specifies the frequency of the signal present at the NI-RFPM Switch receiver input channel, in Hz. |
|  | Reference Level specifies the reference level of the NI-RFPM receiver port in decibels milliwatt (dBm). When NI-RFPM de-embedding is enabled, the reference level is defined at the DUT reference plane. |
|  | The error in cluster can accept error information wired from VIs previously called. Use this information to decide if any functionality should be bypassed in the event of errors from other VIs. Right-click the error in control on the front panel and select Explain Error or Explain Warning from the shortcut menu for more information about the error. The status boolean is either TRUE (X) for an error, or FALSE (checkmark) for no error or a warning. The pop-up option Explain Error (or Explain Warning) gives more information about the error displayed. The code input identifies the error or warning. The pop-up option Explain Error (or Explain Warning) gives more information about the error displayed. The source string describes the origin of the error or warning. The pop-up option Explain Error (or Explain Warning) gives more information about the error displayed. |
|  | The status boolean is either TRUE (X) for an error, or FALSE (checkmark) for no error or a warning. The pop-up option Explain Error (or Explain Warning) gives more information about the error displayed. |
|  | The code input identifies the error or warning. The pop-up option Explain Error (or Explain Warning) gives more information about the error displayed. |
|  | The source string describes the origin of the error or warning. The pop-up option Explain Error (or Explain Warning) gives more information about the error displayed. |
|  | instrument handle out passes a reference to your instrument session to the next VI. instrument handle out is obtained from the NI-RFPM Init With Resources VI and identifies a particular instrument session. |
|  | Settling Time in Secondsreturns the time, in seconds, required for the signal at the specified NI-RFPM Switch receiver path output channel to settle within the specified receiver amplitude settling. |
|  | The error out cluster passes error or warning information out of a VI to be used by other VIs. Use this information to decide if any functionality should be bypassed in the event of errors from other VIs. The status boolean is either TRUE (X) for an error, or FALSE (checkmark) for no error or a warning. The pop-up option Explain Error (or Explain Warning) gives more information about the error displayed. The code output identifies the error or warning. The pop-up option Explain Error (or Explain Warning) gives more information about the error displayed. The source string describes the origin of the error or warning. The pop-up option Explain Error (or Explain Warning) gives more information about the error displayed. |
|  | The status boolean is either TRUE (X) for an error, or FALSE (checkmark) for no error or a warning. The pop-up option Explain Error (or Explain Warning) gives more information about the error displayed. |
|  | The code output identifies the error or warning. The pop-up option Explain Error (or Explain Warning) gives more information about the error displayed. |
|  | The source string describes the origin of the error or warning. The pop-up option Explain Error (or Explain Warning) gives more information about the error displayed. |

<!--NI_TOPIC bundle=ni-rfpm-api-ref path=rfpmviref/ni-rfpm_read_sweep_settings_information.html language=enus -->
## TOPIC 00214: NI-RFPM Read Sweep Settings Information VI

- bundle_id: `ni-rfpm-api-ref`
- source_path: `rfpmviref/ni-rfpm_read_sweep_settings_information.html`
- source_url: https://docs-be.ni.com/bundle/ni-rfpm-api-ref/raw/resource/enus/rfpmviref/ni-rfpm_read_sweep_settings_information.html
- document_id: `ni-rfpm-api-ref`
- page_type: `leaf`
- content_type: ``

NI-RFPM Read Sweep Settings Information VI

Installed With:

Returns the number of ports and number of points associated with a sweep setting.

[IMAGE alt='NI-RFPM Read Sweep Settings Information' src='ni-rfpm_read_sweep_settings_information.gif']

|  | instrument handle identifies your instrument session. instrument handle is obtained from the NI-RFPM Init With Resources VI and identifies a particular instrument session. |
| --- | --- |
|  | Sweep Settings Name specifies the sweep setting to query. |
|  | The error in cluster can accept error information wired from VIs previously called. Use this information to decide if any functionality should be bypassed in the event of errors from other VIs. Right-click the error in control on the front panel and select Explain Error or Explain Warning from the shortcut menu for more information about the error. The status boolean is either TRUE (X) for an error, or FALSE (checkmark) for no error or a warning. The pop-up option Explain Error (or Explain Warning) gives more information about the error displayed. The code input identifies the error or warning. The pop-up option Explain Error (or Explain Warning) gives more information about the error displayed. The source string describes the origin of the error or warning. The pop-up option Explain Error (or Explain Warning) gives more information about the error displayed. |
|  | The status boolean is either TRUE (X) for an error, or FALSE (checkmark) for no error or a warning. The pop-up option Explain Error (or Explain Warning) gives more information about the error displayed. |
|  | The code input identifies the error or warning. The pop-up option Explain Error (or Explain Warning) gives more information about the error displayed. |
|  | The source string describes the origin of the error or warning. The pop-up option Explain Error (or Explain Warning) gives more information about the error displayed. |
|  | instrument handle out passes a reference to your instrument session to the next VI. instrument handle out is obtained from the NI-RFPM Init With Resources VI and identifies a particular instrument session. |
|  | number of ports returns the number of ports associated with the sweep. |
|  | number of points returns the number of sweep points associated with the sweep. |
|  | The error out cluster passes error or warning information out of a VI to be used by other VIs. Use this information to decide if any functionality should be bypassed in the event of errors from other VIs. The status boolean is either TRUE (X) for an error, or FALSE (checkmark) for no error or a warning. The pop-up option Explain Error (or Explain Warning) gives more information about the error displayed. The code output identifies the error or warning. The pop-up option Explain Error (or Explain Warning) gives more information about the error displayed. The source string describes the origin of the error or warning. The pop-up option Explain Error (or Explain Warning) gives more information about the error displayed. |
|  | The status boolean is either TRUE (X) for an error, or FALSE (checkmark) for no error or a warning. The pop-up option Explain Error (or Explain Warning) gives more information about the error displayed. |
|  | The code output identifies the error or warning. The pop-up option Explain Error (or Explain Warning) gives more information about the error displayed. |
|  | The source string describes the origin of the error or warning. The pop-up option Explain Error (or Explain Warning) gives more information about the error displayed. |

<!--NI_TOPIC bundle=ni-rfpm-api-ref path=rfpmviref/ni-rfpm_read_sweep_settings_names.html language=enus -->
## TOPIC 00215: NI-RFPM Read Sweep Settings Names VI

- bundle_id: `ni-rfpm-api-ref`
- source_path: `rfpmviref/ni-rfpm_read_sweep_settings_names.html`
- source_url: https://docs-be.ni.com/bundle/ni-rfpm-api-ref/raw/resource/enus/rfpmviref/ni-rfpm_read_sweep_settings_names.html
- document_id: `ni-rfpm-api-ref`
- page_type: `leaf`
- content_type: ``

NI-RFPM Read Sweep Settings Names VI

Installed With:

Returns an array of the sweep names defined in the currently-loaded sweep settings files.

Related Information

[Using the Sweep Settings Configuration File](../rfpmhelp/sweep_setting_configuration_file.html)

[IMAGE alt='NI-RFPM Read Sweep Settings Names' src='ni-rfpm_read_sweep_settings_names.gif']

|  | instrument handle identifies your instrument session. instrument handle is obtained from the NI-RFPM Init With Resources VI and identifies a particular instrument session. |
| --- | --- |
|  | The error in cluster can accept error information wired from VIs previously called. Use this information to decide if any functionality should be bypassed in the event of errors from other VIs. Right-click the error in control on the front panel and select Explain Error or Explain Warning from the shortcut menu for more information about the error. The status boolean is either TRUE (X) for an error, or FALSE (checkmark) for no error or a warning. The pop-up option Explain Error (or Explain Warning) gives more information about the error displayed. The code input identifies the error or warning. The pop-up option Explain Error (or Explain Warning) gives more information about the error displayed. The source string describes the origin of the error or warning. The pop-up option Explain Error (or Explain Warning) gives more information about the error displayed. |
|  | The status boolean is either TRUE (X) for an error, or FALSE (checkmark) for no error or a warning. The pop-up option Explain Error (or Explain Warning) gives more information about the error displayed. |
|  | The code input identifies the error or warning. The pop-up option Explain Error (or Explain Warning) gives more information about the error displayed. |
|  | The source string describes the origin of the error or warning. The pop-up option Explain Error (or Explain Warning) gives more information about the error displayed. |
|  | instrument handle out passes a reference to your instrument session to the next VI. instrument handle out is obtained from the NI-RFPM Init With Resources VI and identifies a particular instrument session. |
|  | Sweep Settings Names returns an array of sweep settings names defined in the sweep settings configuration file. |
|  | The error out cluster passes error or warning information out of a VI to be used by other VIs. Use this information to decide if any functionality should be bypassed in the event of errors from other VIs. The status boolean is either TRUE (X) for an error, or FALSE (checkmark) for no error or a warning. The pop-up option Explain Error (or Explain Warning) gives more information about the error displayed. The code output identifies the error or warning. The pop-up option Explain Error (or Explain Warning) gives more information about the error displayed. The source string describes the origin of the error or warning. The pop-up option Explain Error (or Explain Warning) gives more information about the error displayed. |
|  | The status boolean is either TRUE (X) for an error, or FALSE (checkmark) for no error or a warning. The pop-up option Explain Error (or Explain Warning) gives more information about the error displayed. |
|  | The code output identifies the error or warning. The pop-up option Explain Error (or Explain Warning) gives more information about the error displayed. |
|  | The source string describes the origin of the error or warning. The pop-up option Explain Error (or Explain Warning) gives more information about the error displayed. |

<!--NI_TOPIC bundle=ni-rfpm-api-ref path=rfpmviref/ni-rfpm_read_system_calibration_information.html language=enus -->
## TOPIC 00216: NI-RFPM Read System Calibration Information VI

- bundle_id: `ni-rfpm-api-ref`
- source_path: `rfpmviref/ni-rfpm_read_system_calibration_information.html`
- source_url: https://docs-be.ni.com/bundle/ni-rfpm-api-ref/raw/resource/enus/rfpmviref/ni-rfpm_read_system_calibration_information.html
- document_id: `ni-rfpm-api-ref`
- page_type: `leaf`
- content_type: ``

NI-RFPM Read System Calibration Information VI

Installed With:

Returns information about what ports are calibrated, as well as date, time, and temperature, for the system calibration.

This VI does not support the mmWave subsystem.

[IMAGE alt='NI-RFPM Read System Calibration Information' src='ni-rfpm_read_system_calibration_information.gif']

|  | instrument handle identifies your instrument session. instrument handle is obtained from the NI-RFPM Init With Resources VI and identifies a particular instrument session. |
| --- | --- |
|  | The error in cluster can accept error information wired from VIs previously called. Use this information to decide if any functionality should be bypassed in the event of errors from other VIs. Right-click the error in control on the front panel and select Explain Error or Explain Warning from the shortcut menu for more information about the error. The status boolean is either TRUE (X) for an error, or FALSE (checkmark) for no error or a warning. The pop-up option Explain Error (or Explain Warning) gives more information about the error displayed. The code input identifies the error or warning. The pop-up option Explain Error (or Explain Warning) gives more information about the error displayed. The source string describes the origin of the error or warning. The pop-up option Explain Error (or Explain Warning) gives more information about the error displayed. |
|  | The status boolean is either TRUE (X) for an error, or FALSE (checkmark) for no error or a warning. The pop-up option Explain Error (or Explain Warning) gives more information about the error displayed. |
|  | The code input identifies the error or warning. The pop-up option Explain Error (or Explain Warning) gives more information about the error displayed. |
|  | The source string describes the origin of the error or warning. The pop-up option Explain Error (or Explain Warning) gives more information about the error displayed. |
|  | instrument handle out passes a reference to your instrument session to the next VI. instrument handle out is obtained from the NI-RFPM Init With Resources VI and identifies a particular instrument session. |
|  | Ports returns a one-dimensional array containing an array of ports on which the system calibration was performed. |
|  | Date\\Time returns an array of timestamps for when the system calibration was performed. |
|  | The error out cluster passes error or warning information out of a VI to be used by other VIs. Use this information to decide if any functionality should be bypassed in the event of errors from other VIs. The status boolean is either TRUE (X) for an error, or FALSE (checkmark) for no error or a warning. The pop-up option Explain Error (or Explain Warning) gives more information about the error displayed. The code output identifies the error or warning. The pop-up option Explain Error (or Explain Warning) gives more information about the error displayed. The source string describes the origin of the error or warning. The pop-up option Explain Error (or Explain Warning) gives more information about the error displayed. |
|  | The status boolean is either TRUE (X) for an error, or FALSE (checkmark) for no error or a warning. The pop-up option Explain Error (or Explain Warning) gives more information about the error displayed. |
|  | The code output identifies the error or warning. The pop-up option Explain Error (or Explain Warning) gives more information about the error displayed. |
|  | The source string describes the origin of the error or warning. The pop-up option Explain Error (or Explain Warning) gives more information about the error displayed. |
|  | Temperature returns the temperature that specifies the temperature of the STS device at the time of calibration. |

<!--NI_TOPIC bundle=ni-rfpm-api-ref path=rfpmviref/ni-rfpm_reset.html language=enus -->
## TOPIC 00217: NI-RFPM Reset VI

- bundle_id: `ni-rfpm-api-ref`
- source_path: `rfpmviref/ni-rfpm_reset.html`
- source_url: https://docs-be.ni.com/bundle/ni-rfpm-api-ref/raw/resource/enus/rfpmviref/ni-rfpm_reset.html
- document_id: `ni-rfpm-api-ref`
- page_type: `leaf`
- content_type: ``

NI-RFPM Reset VI

Installed With:

Resets all attributes and devices, including NI-RFSA and NI-RFSG sessions, to their default states.

[IMAGE alt='NI-RFPM Reset' src='ni-rfpm_reset.gif']

|  | instrument handle identifies your instrument session. instrument handle is obtained from the NI-RFPM Init With Resources VI and identifies a particular instrument session. |
| --- | --- |
|  | The error in cluster can accept error information wired from VIs previously called. Use this information to decide if any functionality should be bypassed in the event of errors from other VIs. Right-click the error in control on the front panel and select Explain Error or Explain Warning from the shortcut menu for more information about the error. The status boolean is either TRUE (X) for an error, or FALSE (checkmark) for no error or a warning. The pop-up option Explain Error (or Explain Warning) gives more information about the error displayed. The code input identifies the error or warning. The pop-up option Explain Error (or Explain Warning) gives more information about the error displayed. The source string describes the origin of the error or warning. The pop-up option Explain Error (or Explain Warning) gives more information about the error displayed. |
|  | The status boolean is either TRUE (X) for an error, or FALSE (checkmark) for no error or a warning. The pop-up option Explain Error (or Explain Warning) gives more information about the error displayed. |
|  | The code input identifies the error or warning. The pop-up option Explain Error (or Explain Warning) gives more information about the error displayed. |
|  | The source string describes the origin of the error or warning. The pop-up option Explain Error (or Explain Warning) gives more information about the error displayed. |
|  | instrument handle out passes a reference to your instrument session to the next VI. instrument handle out is obtained from the NI-RFPM Init With Resources VI and identifies a particular instrument session. |
|  | The error out cluster passes error or warning information out of a VI to be used by other VIs. Use this information to decide if any functionality should be bypassed in the event of errors from other VIs. The status boolean is either TRUE (X) for an error, or FALSE (checkmark) for no error or a warning. The pop-up option Explain Error (or Explain Warning) gives more information about the error displayed. The code output identifies the error or warning. The pop-up option Explain Error (or Explain Warning) gives more information about the error displayed. The source string describes the origin of the error or warning. The pop-up option Explain Error (or Explain Warning) gives more information about the error displayed. |
|  | The status boolean is either TRUE (X) for an error, or FALSE (checkmark) for no error or a warning. The pop-up option Explain Error (or Explain Warning) gives more information about the error displayed. |
|  | The code output identifies the error or warning. The pop-up option Explain Error (or Explain Warning) gives more information about the error displayed. |
|  | The source string describes the origin of the error or warning. The pop-up option Explain Error (or Explain Warning) gives more information about the error displayed. |

<!--NI_TOPIC bundle=ni-rfpm-api-ref path=rfpmviref/ni-rfpm_reset_device.html language=enus -->
## TOPIC 00218: NI-RFPM Reset Device VI

- bundle_id: `ni-rfpm-api-ref`
- source_path: `rfpmviref/ni-rfpm_reset_device.html`
- source_url: https://docs-be.ni.com/bundle/ni-rfpm-api-ref/raw/resource/enus/rfpmviref/ni-rfpm_reset_device.html
- document_id: `ni-rfpm-api-ref`
- page_type: `leaf`
- content_type: ``

NI-RFPM Reset Device VI

Installed With:

Resets all attributes and devices, including NI-RFSA and NI-RFSG sessions, to their default states, and clears a latched interlock signal.

This VI does not support the mmWave subsystem.

[IMAGE alt='NI-RFPM Reset Device' src='ni-rfpm_reset_device.gif']

|  | instrument handle identifies your instrument session. instrument handle is obtained from the NI-RFPM Init With Resources VI and identifies a particular instrument session. |
| --- | --- |
|  | The error in (no error) cluster can accept error information wired from VIs previously called. Use this information to decide if any functionality should be bypassed in the event of errors from other VIs. Right-click the error in (no error) control on the front panel and select Explain Error or Explain Warning from the shortcut menu for more information about the error. The status boolean is either TRUE (X) for an error, or FALSE (checkmark) for no error or a warning. The pop-up option Explain Error (or Explain Warning) gives more information about the error displayed. The code input identifies the error or warning. The pop-up option Explain Error (or Explain Warning) gives more information about the error displayed. The source string describes the origin of the error or warning. The pop-up option Explain Error (or Explain Warning) gives more information about the error displayed. |
|  | The status boolean is either TRUE (X) for an error, or FALSE (checkmark) for no error or a warning. The pop-up option Explain Error (or Explain Warning) gives more information about the error displayed. |
|  | The code input identifies the error or warning. The pop-up option Explain Error (or Explain Warning) gives more information about the error displayed. |
|  | The source string describes the origin of the error or warning. The pop-up option Explain Error (or Explain Warning) gives more information about the error displayed. |
|  | instrument handle out passes a reference to your instrument session to the next VI. instrument handle out is obtained from the NI-RFPM Init With Resources VI and identifies a particular instrument session. |
|  | The error out cluster passes error or warning information out of a VI to be used by other VIs. Use this information to decide if any functionality should be bypassed in the event of errors from other VIs. The status boolean is either TRUE (X) for an error, or FALSE (checkmark) for no error or a warning. The pop-up option Explain Error (or Explain Warning) gives more information about the error displayed. The code output identifies the error or warning. The pop-up option Explain Error (or Explain Warning) gives more information about the error displayed. The source string describes the origin of the error or warning. The pop-up option Explain Error (or Explain Warning) gives more information about the error displayed. |
|  | The status boolean is either TRUE (X) for an error, or FALSE (checkmark) for no error or a warning. The pop-up option Explain Error (or Explain Warning) gives more information about the error displayed. |
|  | The code output identifies the error or warning. The pop-up option Explain Error (or Explain Warning) gives more information about the error displayed. |
|  | The source string describes the origin of the error or warning. The pop-up option Explain Error (or Explain Warning) gives more information about the error displayed. |

<!--NI_TOPIC bundle=ni-rfpm-api-ref path=rfpmviref/ni-rfpm_reset_with_options.html language=enus -->
## TOPIC 00219: NI-RFPM Reset With Options VI

- bundle_id: `ni-rfpm-api-ref`
- source_path: `rfpmviref/ni-rfpm_reset_with_options.html`
- source_url: https://docs-be.ni.com/bundle/ni-rfpm-api-ref/raw/resource/enus/rfpmviref/ni-rfpm_reset_with_options.html
- document_id: `ni-rfpm-api-ref`
- page_type: `leaf`
- content_type: ``

NI-RFPM Reset With Options VI

Installed With:

Performs a selective reset of attributes and underlying driver sessions including NI-RFSA and NI-RFSG sessions.

[IMAGE alt='NI-RFPM Reset With Options' src='ni-rfpm_reset_with_options.gif']

|  | instrument handle identifies your instrument session. instrument handle is obtained from the NI-RFPM Init With Resources VI and identifies a particular instrument session. |
| --- | --- |
|  | options specifies the attributes and settings that are preserved during the reset operation. The following properties are used in this parameter: RFSARFSGPreserveDeembeddingTables—This option preserves previously configured de-embedding tables in the NI-RFSA and NI-RFSG sessions. This option is only supported on the mmWave subsystem. RFPMPreserveReferenceLevelPortExtensionTables—This option resets NI-RFPM without clearing the reference level port extension tables you have configured. This option is only supported on the mmWave subsystem. RFSGPreserveWaveforms—This option preserves previously configured NI-RFSG waveforms and must be used with the RFSGPreserveScripts option. RFSGPreserveScripts—This option preserves previously configured NI-RFSG scripts and must be used with the RFSGPreserveWaveforms option. RFPMPreserveSweepSettings—This option resets the NI-RFPM driver without clearing sweep settings that have been loaded into memory. RFPMPreserveCalibrationData—This option resets the NI-RFPM driver without clearing user calibration data that has been loaded into memory or collected by the driver. RFPMPreserveDeembedding—This option resets the NI-RFPM driver without clearing de-embedding data that has been loaded into memory. RFSARFSGPreserveRoutes—This option preserves previously configured routes in the NI-RFSA and NI-RFSG sessions. This option is not supported on a STS RF Subsystem using PXIe-5644/5645/5646 VST. |
|  | The error in cluster can accept error information wired from VIs previously called. Use this information to decide if any functionality should be bypassed in the event of errors from other VIs. Right-click the error in control on the front panel and select Explain Error or Explain Warning from the shortcut menu for more information about the error. The status boolean is either TRUE (X) for an error, or FALSE (checkmark) for no error or a warning. The pop-up option Explain Error (or Explain Warning) gives more information about the error displayed. The code input identifies the error or warning. The pop-up option Explain Error (or Explain Warning) gives more information about the error displayed. The source string describes the origin of the error or warning. The pop-up option Explain Error (or Explain Warning) gives more information about the error displayed. |
|  | The status boolean is either TRUE (X) for an error, or FALSE (checkmark) for no error or a warning. The pop-up option Explain Error (or Explain Warning) gives more information about the error displayed. |
|  | The code input identifies the error or warning. The pop-up option Explain Error (or Explain Warning) gives more information about the error displayed. |
|  | The source string describes the origin of the error or warning. The pop-up option Explain Error (or Explain Warning) gives more information about the error displayed. |
|  | instrument handle out passes a reference to your instrument session to the next VI. instrument handle out is obtained from the NI-RFPM Init With Resources VI and identifies a particular instrument session. |
|  | The error out cluster passes error or warning information out of a VI to be used by other VIs. Use this information to decide if any functionality should be bypassed in the event of errors from other VIs. The status boolean is either TRUE (X) for an error, or FALSE (checkmark) for no error or a warning. The pop-up option Explain Error (or Explain Warning) gives more information about the error displayed. The code output identifies the error or warning. The pop-up option Explain Error (or Explain Warning) gives more information about the error displayed. The source string describes the origin of the error or warning. The pop-up option Explain Error (or Explain Warning) gives more information about the error displayed. |
|  | The status boolean is either TRUE (X) for an error, or FALSE (checkmark) for no error or a warning. The pop-up option Explain Error (or Explain Warning) gives more information about the error displayed. |
|  | The code output identifies the error or warning. The pop-up option Explain Error (or Explain Warning) gives more information about the error displayed. |
|  | The source string describes the origin of the error or warning. The pop-up option Explain Error (or Explain Warning) gives more information about the error displayed. |

<!--NI_TOPIC bundle=ni-rfpm-api-ref path=rfpmviref/ni-rfpm_revision_query.html language=enus -->
## TOPIC 00220: NI-RFPM Revision Query VI

- bundle_id: `ni-rfpm-api-ref`
- source_path: `rfpmviref/ni-rfpm_revision_query.html`
- source_url: https://docs-be.ni.com/bundle/ni-rfpm-api-ref/raw/resource/enus/rfpmviref/ni-rfpm_revision_query.html
- document_id: `ni-rfpm-api-ref`
- page_type: `leaf`
- content_type: ``

NI-RFPM Revision Query VI

Installed With:

Returns driver and firmware revision information.

[IMAGE alt='NI-RFPM Revision Query' src='ni-rfpm_revision_query.gif']

|  | instrument handle identifies your instrument session. instrument handle is obtained from the NI-RFPM Init With Resources VI and identifies a particular instrument session. |
| --- | --- |
|  | The error in cluster can accept error information wired from VIs previously called. Use this information to decide if any functionality should be bypassed in the event of errors from other VIs. Right-click the error in control on the front panel and select Explain Error or Explain Warning from the shortcut menu for more information about the error. The status boolean is either TRUE (X) for an error, or FALSE (checkmark) for no error or a warning. The pop-up option Explain Error (or Explain Warning) gives more information about the error displayed. The code input identifies the error or warning. The pop-up option Explain Error (or Explain Warning) gives more information about the error displayed. The source string describes the origin of the error or warning. The pop-up option Explain Error (or Explain Warning) gives more information about the error displayed. |
|  | The status boolean is either TRUE (X) for an error, or FALSE (checkmark) for no error or a warning. The pop-up option Explain Error (or Explain Warning) gives more information about the error displayed. |
|  | The code input identifies the error or warning. The pop-up option Explain Error (or Explain Warning) gives more information about the error displayed. |
|  | The source string describes the origin of the error or warning. The pop-up option Explain Error (or Explain Warning) gives more information about the error displayed. |
|  | instrument handle out passes a reference to your instrument session to the next VI. instrument handle out is obtained from the NI-RFPM Init With Resources VI and identifies a particular instrument session. |
|  | instrument driver revision returns the instrument driver revision information. |
|  | firmware revision returns firmware revision information. Returns an empty string if there is no firmware information. |
|  | The error out cluster passes error or warning information out of a VI to be used by other VIs. Use this information to decide if any functionality should be bypassed in the event of errors from other VIs. The status boolean is either TRUE (X) for an error, or FALSE (checkmark) for no error or a warning. The pop-up option Explain Error (or Explain Warning) gives more information about the error displayed. The code output identifies the error or warning. The pop-up option Explain Error (or Explain Warning) gives more information about the error displayed. The source string describes the origin of the error or warning. The pop-up option Explain Error (or Explain Warning) gives more information about the error displayed. |
|  | The status boolean is either TRUE (X) for an error, or FALSE (checkmark) for no error or a warning. The pop-up option Explain Error (or Explain Warning) gives more information about the error displayed. |
|  | The code output identifies the error or warning. The pop-up option Explain Error (or Explain Warning) gives more information about the error displayed. |
|  | The source string describes the origin of the error or warning. The pop-up option Explain Error (or Explain Warning) gives more information about the error displayed. |

<!--NI_TOPIC bundle=ni-rfpm-api-ref path=rfpmviref/ni-rfpm_save_calibration_and_configuration.html language=enus -->
## TOPIC 00221: NI-RFPM Save Calibration and Configuration VI

- bundle_id: `ni-rfpm-api-ref`
- source_path: `rfpmviref/ni-rfpm_save_calibration_and_configuration.html`
- source_url: https://docs-be.ni.com/bundle/ni-rfpm-api-ref/raw/resource/enus/rfpmviref/ni-rfpm_save_calibration_and_configuration.html
- document_id: `ni-rfpm-api-ref`
- page_type: `leaf`
- content_type: ``

NI-RFPM Save Calibration and Configuration VI

Installed With:

Saves the current user calibration and configuration data.

This VI does not support the mmWave subsystem.

[IMAGE alt='NI-RFPM Save Calibration and Configuration' src='ni-rfpm_save_calibration_and_configuration.gif']

|  | instrument handle in passes a reference to the next VI from your instrument session. instrument handle in is obtained from the NI-RFPM Init With Resources VI and identifies a particular instrument session. |
| --- | --- |
|  | Calibration Storage File Path specifies the path of the calibration storage file that NI-RFPM saves the calibration data to. |
|  | Open Mode specifies how the calibration and configuration data file is written and saved if files with the same name already exist. create Attempts to save the calibration data in a new file and returns an error if a file with the same name already exists. replace or create Either creates a new file for the configuration or overwrites the existing file. merge Combines the error correction and configuration data in the existing file with the new data from the driver before saving. |
| create | Attempts to save the calibration data in a new file and returns an error if a file with the same name already exists. |
| replace or create | Either creates a new file for the configuration or overwrites the existing file. |
| merge | Combines the error correction and configuration data in the existing file with the new data from the driver before saving. |
|  | The error in cluster can accept error information wired from VIs previously called. Use this information to decide if any functionality should be bypassed in the event of errors from other VIs. Right-click the error in control on the front panel and select Explain Error or Explain Warning from the shortcut menu for more information about the error. The status boolean is either TRUE (X) for an error, or FALSE (checkmark) for no error or a warning. The pop-up option Explain Error (or Explain Warning) gives more information about the error displayed. The code input identifies the error or warning. The pop-up option Explain Error (or Explain Warning) gives more information about the error displayed. The source string describes the origin of the error or warning. The pop-up option Explain Error (or Explain Warning) gives more information about the error displayed. |
|  | The status boolean is either TRUE (X) for an error, or FALSE (checkmark) for no error or a warning. The pop-up option Explain Error (or Explain Warning) gives more information about the error displayed. |
|  | The code input identifies the error or warning. The pop-up option Explain Error (or Explain Warning) gives more information about the error displayed. |
|  | The source string describes the origin of the error or warning. The pop-up option Explain Error (or Explain Warning) gives more information about the error displayed. |
|  | instrument handle out passes a reference to your instrument session to the next VI. instrument handle out is obtained from the NI-RFPM Init With Resources VI and identifies a particular instrument session. |
|  | The error out cluster passes error or warning information out of a VI to be used by other VIs. Use this information to decide if any functionality should be bypassed in the event of errors from other VIs. The status boolean is either TRUE (X) for an error, or FALSE (checkmark) for no error or a warning. The pop-up option Explain Error (or Explain Warning) gives more information about the error displayed. The code output identifies the error or warning. The pop-up option Explain Error (or Explain Warning) gives more information about the error displayed. The source string describes the origin of the error or warning. The pop-up option Explain Error (or Explain Warning) gives more information about the error displayed. |
|  | The status boolean is either TRUE (X) for an error, or FALSE (checkmark) for no error or a warning. The pop-up option Explain Error (or Explain Warning) gives more information about the error displayed. |
|  | The code output identifies the error or warning. The pop-up option Explain Error (or Explain Warning) gives more information about the error displayed. |
|  | The source string describes the origin of the error or warning. The pop-up option Explain Error (or Explain Warning) gives more information about the error displayed. |

<!--NI_TOPIC bundle=ni-rfpm-api-ref path=rfpmviref/ni-rfpm_select_reference_level_port_extension_table.html language=enus -->
## TOPIC 00222: NI-RFPM Select Reference Level Port Extension Table VI

- bundle_id: `ni-rfpm-api-ref`
- source_path: `rfpmviref/ni-rfpm_select_reference_level_port_extension_table.html`
- source_url: https://docs-be.ni.com/bundle/ni-rfpm-api-ref/raw/resource/enus/rfpmviref/ni-rfpm_select_reference_level_port_extension_table.html
- document_id: `ni-rfpm-api-ref`
- page_type: `leaf`
- content_type: ``

NI-RFPM Select Reference Level Port Extension Table VI

Installed With:

Selects the reference level port extension table to apply to measurements made with the port.

This VI does not support the RF subsystem.

[IMAGE alt='NI-RFPM Select Reference Level Port Extension Table' src='ni-rfpm_select_reference_level_port_extension_table.gif']

|  | instrument handle identifies your instrument session. instrument handle is obtained from the NI-RFPM Init With Resources VI and identifies a particular instrument session. |
| --- | --- |
|  | port specifies the port to create the reference level port extension S-parameter table for. |
|  | table name specifies the name of the S-parameter table. |
|  | The error in (no error) cluster can accept error information wired from VIs previously called. Use this information to decide if any functionality should be bypassed in the event of errors from other VIs. Right-click the error in (no error) control on the front panel and select Explain Error or Explain Warning from the shortcut menu for more information about the error. The status boolean is either TRUE (X) for an error, or FALSE (checkmark) for no error or a warning. The pop-up option Explain Error (or Explain Warning) gives more information about the error displayed. The code input identifies the error or warning. The pop-up option Explain Error (or Explain Warning) gives more information about the error displayed. The source string describes the origin of the error or warning. The pop-up option Explain Error (or Explain Warning) gives more information about the error displayed. |
|  | The status boolean is either TRUE (X) for an error, or FALSE (checkmark) for no error or a warning. The pop-up option Explain Error (or Explain Warning) gives more information about the error displayed. |
|  | The code input identifies the error or warning. The pop-up option Explain Error (or Explain Warning) gives more information about the error displayed. |
|  | The source string describes the origin of the error or warning. The pop-up option Explain Error (or Explain Warning) gives more information about the error displayed. |
|  | instrument handle out passes a reference to your instrument session to the next VI. instrument handle out is obtained from the NI-RFPM Init With Resources VI and identifies a particular instrument session. |
|  | The error out cluster passes error or warning information out of a VI to be used by other VIs. Use this information to decide if any functionality should be bypassed in the event of errors from other VIs. The status boolean is either TRUE (X) for an error, or FALSE (checkmark) for no error or a warning. The pop-up option Explain Error (or Explain Warning) gives more information about the error displayed. The code output identifies the error or warning. The pop-up option Explain Error (or Explain Warning) gives more information about the error displayed. The source string describes the origin of the error or warning. The pop-up option Explain Error (or Explain Warning) gives more information about the error displayed. |
|  | The status boolean is either TRUE (X) for an error, or FALSE (checkmark) for no error or a warning. The pop-up option Explain Error (or Explain Warning) gives more information about the error displayed. |
|  | The code output identifies the error or warning. The pop-up option Explain Error (or Explain Warning) gives more information about the error displayed. |
|  | The source string describes the origin of the error or warning. The pop-up option Explain Error (or Explain Warning) gives more information about the error displayed. |

<!--NI_TOPIC bundle=ni-rfpm-api-ref path=rfpmviref/ni-rfpm_self-test.html language=enus -->
## TOPIC 00223: NI-RFPM Self-Test VI

- bundle_id: `ni-rfpm-api-ref`
- source_path: `rfpmviref/ni-rfpm_self-test.html`
- source_url: https://docs-be.ni.com/bundle/ni-rfpm-api-ref/raw/resource/enus/rfpmviref/ni-rfpm_self-test.html
- document_id: `ni-rfpm-api-ref`
- page_type: `leaf`
- content_type: ``

NI-RFPM Self-Test VI

Installed With:

Performs a self-test on the STS device and returns the test result. This VI performs a series of simple tests verifying that the STS device is powered on and responding.

This VI does not support the mmWave subsystem.

[IMAGE alt='NI-RFPM Self-Test' src='ni-rfpm_self-test.gif']

|  | instrument handle identifies your instrument session. instrument handle is obtained from the NI-RFPM Init With Resources VI and identifies a particular instrument session. |
| --- | --- |
|  | The error in (no error) cluster can accept error information wired from VIs previously called. Use this information to decide if any functionality should be bypassed in the event of errors from other VIs. Right-click the error in (no error) control on the front panel and select Explain Error or Explain Warning from the shortcut menu for more information about the error. The status boolean is either TRUE (X) for an error, or FALSE (checkmark) for no error or a warning. The pop-up option Explain Error (or Explain Warning) gives more information about the error displayed. The code input identifies the error or warning. The pop-up option Explain Error (or Explain Warning) gives more information about the error displayed. The source string describes the origin of the error or warning. The pop-up option Explain Error (or Explain Warning) gives more information about the error displayed. |
|  | The status boolean is either TRUE (X) for an error, or FALSE (checkmark) for no error or a warning. The pop-up option Explain Error (or Explain Warning) gives more information about the error displayed. |
|  | The code input identifies the error or warning. The pop-up option Explain Error (or Explain Warning) gives more information about the error displayed. |
|  | The source string describes the origin of the error or warning. The pop-up option Explain Error (or Explain Warning) gives more information about the error displayed. |
|  | instrument handle out passes a reference to your instrument session to the next VI. instrument handle out is obtained from the NI-RFPM Init With Resources VI and identifies a particular instrument session. |
|  | self test result returns the value from the device self-test. A value of 0 indicates that the device is powered on and responding. A value of 1 indicates that the device failed the self test. |
|  | self-test message returns the self-test response string from the STS device. |
|  | The error out cluster passes error or warning information out of a VI to be used by other VIs. Use this information to decide if any functionality should be bypassed in the event of errors from other VIs. The status boolean is either TRUE (X) for an error, or FALSE (checkmark) for no error or a warning. The pop-up option Explain Error (or Explain Warning) gives more information about the error displayed. The code output identifies the error or warning. The pop-up option Explain Error (or Explain Warning) gives more information about the error displayed. The source string describes the origin of the error or warning. The pop-up option Explain Error (or Explain Warning) gives more information about the error displayed. |
|  | The status boolean is either TRUE (X) for an error, or FALSE (checkmark) for no error or a warning. The pop-up option Explain Error (or Explain Warning) gives more information about the error displayed. |
|  | The code output identifies the error or warning. The pop-up option Explain Error (or Explain Warning) gives more information about the error displayed. |
|  | The source string describes the origin of the error or warning. The pop-up option Explain Error (or Explain Warning) gives more information about the error displayed. |

<!--NI_TOPIC bundle=ni-rfpm-api-ref path=rfpmviref/ni-rfpm_set_receiver_port_and_path_for_rfmx.html language=enus -->
## TOPIC 00224: NI-RFPM Set Receiver Port and Path For RFmx Callbacks VI

- bundle_id: `ni-rfpm-api-ref`
- source_path: `rfpmviref/ni-rfpm_set_receiver_port_and_path_for_rfmx.html`
- source_url: https://docs-be.ni.com/bundle/ni-rfpm-api-ref/raw/resource/enus/rfpmviref/ni-rfpm_set_receiver_port_and_path_for_rfmx.html
- document_id: `ni-rfpm-api-ref`
- page_type: `leaf`
- content_type: ``

NI-RFPM Set Receiver Port and Path For RFmx Callbacks VI

Installed With:

Sets the port, receiver path, and receiver coupling path for RFmx callback functions to use.

This VI does not support the mmWave subsystem.

[IMAGE alt='NI-RFPM Set Receiver Port and Path For RFmx Callbacks' src='ni-rfpm_set_receiver_port_and_path_for_rfmx_callbacks.gif']

|  | Optimization Method specifies what to optimize for when picking the path to use through RFPM. This only applies if Receiver Path and Receiver Coupling Path are both set to Unspecified. Normal Look up the RFPM path to use based on the peak power so you can use state freeze in order to achieve the best absolute amplitude accuracy. Optimize for Dynamic Range Look up the RFPM path based on average power since this optimizes dynamic range which benefits EVM and other measurements at the cost of maintaining the state freeze and absolute amplitude accuracy. |
| --- | --- |
| Normal | Look up the RFPM path to use based on the peak power so you can use state freeze in order to achieve the best absolute amplitude accuracy. |
| Optimize for Dynamic Range | Look up the RFPM path based on average power since this optimizes dynamic range which benefits EVM and other measurements at the cost of maintaining the state freeze and absolute amplitude accuracy. |
|  | PAPR specifies the estimated peak to average envelope power ratio of the waveform to be measured in dB. Only applies if the Optimization Method is set to Optimize For Dynamic Range. The default value is 0. Valid values are 0 to positive infinity. |
|  | instrument handle identifies your instrument session. instrument handle is obtained from the NI-RFPM Init With Resources VI and identifies a particular instrument session. |
|  | Port Specifies the port that will be used during calls to the RFmx callback functions. |
|  | Receiver Path specifies the receiver path that will be used during calls to the RFmx call back functions Unspecified (default) NI-RFPM searches across all paths for offset data that matches the requested parameters. Direct NI-RFPM uses the receiver direct path through the STS device. Gain NI-RFPM uses the receiver amplified path through the STS device. Loop NI-RFPM uses the path through the receiver bypass loop of the STS device. |
| Unspecified (default) | NI-RFPM searches across all paths for offset data that matches the requested parameters. |
| Direct | NI-RFPM uses the receiver direct path through the STS device. |
| Gain | NI-RFPM uses the receiver amplified path through the STS device. |
| Loop | NI-RFPM uses the path through the receiver bypass loop of the STS device. |
|  | Receiver Coupling Path specifies the receiver path through the port module that will be used during calls to the RFmx call back functions. Direct NI-RFPM uses the direct receiver path. LNA NI-RFPM uses the LNA receiver path. Test Coupler NI-RFPM uses the test receiver coupled path. Unspecified (default) NI-RFPM searches across all paths for offset data that matches the requested parameters. |
| Direct | NI-RFPM uses the direct receiver path. |
| LNA | NI-RFPM uses the LNA receiver path. |
| Test Coupler | NI-RFPM uses the test receiver coupled path. |
| Unspecified (default) | NI-RFPM searches across all paths for offset data that matches the requested parameters. |
|  | The error in cluster can accept error information wired from VIs previously called. Use this information to decide if any functionality should be bypassed in the event of errors from other VIs. Right-click the error in control on the front panel and select Explain Error or Explain Warning from the shortcut menu for more information about the error. The status boolean is either TRUE (X) for an error, or FALSE (checkmark) for no error or a warning. The pop-up option Explain Error (or Explain Warning) gives more information about the error displayed. The code input identifies the error or warning. The pop-up option Explain Error (or Explain Warning) gives more information about the error displayed. The source string describes the origin of the error or warning. The pop-up option Explain Error (or Explain Warning) gives more information about the error displayed. |
|  | The status boolean is either TRUE (X) for an error, or FALSE (checkmark) for no error or a warning. The pop-up option Explain Error (or Explain Warning) gives more information about the error displayed. |
|  | The code input identifies the error or warning. The pop-up option Explain Error (or Explain Warning) gives more information about the error displayed. |
|  | The source string describes the origin of the error or warning. The pop-up option Explain Error (or Explain Warning) gives more information about the error displayed. |
|  | instrument handle out passes a reference to your instrument session to the next VI. instrument handle out is obtained from the NI-RFPM Init With Resources VI and identifies a particular instrument session. |
|  | The error out cluster passes error or warning information out of a VI to be used by other VIs. Use this information to decide if any functionality should be bypassed in the event of errors from other VIs. The status boolean is either TRUE (X) for an error, or FALSE (checkmark) for no error or a warning. The pop-up option Explain Error (or Explain Warning) gives more information about the error displayed. The code output identifies the error or warning. The pop-up option Explain Error (or Explain Warning) gives more information about the error displayed. The source string describes the origin of the error or warning. The pop-up option Explain Error (or Explain Warning) gives more information about the error displayed. |
|  | The status boolean is either TRUE (X) for an error, or FALSE (checkmark) for no error or a warning. The pop-up option Explain Error (or Explain Warning) gives more information about the error displayed. |
|  | The code output identifies the error or warning. The pop-up option Explain Error (or Explain Warning) gives more information about the error displayed. |
|  | The source string describes the origin of the error or warning. The pop-up option Explain Error (or Explain Warning) gives more information about the error displayed. |

<!--NI_TOPIC bundle=ni-rfpm-api-ref path=rfpmviref/ni-rfpm_set_rx_path.html language=enus -->
## TOPIC 00225: NI-RFPM Set RX Path VI

- bundle_id: `ni-rfpm-api-ref`
- source_path: `rfpmviref/ni-rfpm_set_rx_path.html`
- source_url: https://docs-be.ni.com/bundle/ni-rfpm-api-ref/raw/resource/enus/rfpmviref/ni-rfpm_set_rx_path.html
- document_id: `ni-rfpm-api-ref`
- page_type: `leaf`
- content_type: ``

NI-RFPM Set RX Path VI

Installed With:

Connects the receive (Rx) path you specify to the underlying switch session that was passed into the [NI-RFPM Init With Resources](ni-rfpm_init_with_resources.html) VI. The VI waits until the switch debounces or until **timeout** is reached.

This VI does not support the mmWave subsystem.

#### NI-RFPM Set RX Path By Parameters

Connects the receive (Rx) path you specify to the underlying switch session that was passed into the [NI-RFPM Init With Resources](ni-rfpm_init_with_resources.html) VI. The VI waits until the switch debounces or until **timeout** is reached.

[IMAGE alt='NI-RFPM Set RX Path By Parameters' src='ni-rfpm_set_rx_path_by_parameters.gif']

|  | instrument handle identifies your instrument session. instrument handle is obtained from the NI-RFPM Init With Resources VI and identifies a particular instrument session. |
| --- | --- |
|  | RX port specifies the port the specified receiver is associated with. |
|  | RX path specifies the path to connect using the underlying switch session. Direct NI-RFPM uses the direct path through the NI-RFPM Switch. Gain NI-RFPM uses the amplified path through the NI-RFPM Switch. Loop NI-RFPM uses the path through the bypass loop of the NI-RFPM Switch. |
| Direct | NI-RFPM uses the direct path through the NI-RFPM Switch. |
| Gain | NI-RFPM uses the amplified path through the NI-RFPM Switch. |
| Loop | NI-RFPM uses the path through the bypass loop of the NI-RFPM Switch. |
|  | Receiver Coupling Path specifies the port module coupling path to connect using the underlying switch session. Coupled NI-RFPM uses the test receiver coupled path. Direct NI-RFPM uses the direct receiver path. LNA NI-RFPM uses the LNA receiver path. |
| Coupled | NI-RFPM uses the test receiver coupled path. |
| Direct | NI-RFPM uses the direct receiver path. |
| LNA | NI-RFPM uses the LNA receiver path. |
|  | The error in (no error) cluster can accept error information wired from VIs previously called. Use this information to decide if any functionality should be bypassed in the event of errors from other VIs. Right-click the error in (no error) control on the front panel and select Explain Error or Explain Warning from the shortcut menu for more information about the error. The status boolean is either TRUE (X) for an error, or FALSE (checkmark) for no error or a warning. The pop-up option Explain Error (or Explain Warning) gives more information about the error displayed. The code input identifies the error or warning. The pop-up option Explain Error (or Explain Warning) gives more information about the error displayed. The source string describes the origin of the error or warning. The pop-up option Explain Error (or Explain Warning) gives more information about the error displayed. |
|  | The status boolean is either TRUE (X) for an error, or FALSE (checkmark) for no error or a warning. The pop-up option Explain Error (or Explain Warning) gives more information about the error displayed. |
|  | The code input identifies the error or warning. The pop-up option Explain Error (or Explain Warning) gives more information about the error displayed. |
|  | The source string describes the origin of the error or warning. The pop-up option Explain Error (or Explain Warning) gives more information about the error displayed. |
|  | Timeout specifies the time to wait for the operation to complete before returning an error, expressed in seconds. |
|  | instrument handle out passes a reference to your instrument session to the next VI. instrument handle out is obtained from the NI-RFPM Init With Resources VI and identifies a particular instrument session. |
|  | The error out cluster passes error or warning information out of a VI to be used by other VIs. Use this information to decide if any functionality should be bypassed in the event of errors from other VIs. The status boolean is either TRUE (X) for an error, or FALSE (checkmark) for no error or a warning. The pop-up option Explain Error (or Explain Warning) gives more information about the error displayed. The code output identifies the error or warning. The pop-up option Explain Error (or Explain Warning) gives more information about the error displayed. The source string describes the origin of the error or warning. The pop-up option Explain Error (or Explain Warning) gives more information about the error displayed. |
|  | The status boolean is either TRUE (X) for an error, or FALSE (checkmark) for no error or a warning. The pop-up option Explain Error (or Explain Warning) gives more information about the error displayed. |
|  | The code output identifies the error or warning. The pop-up option Explain Error (or Explain Warning) gives more information about the error displayed. |
|  | The source string describes the origin of the error or warning. The pop-up option Explain Error (or Explain Warning) gives more information about the error displayed. |

#### NI-RFPM Set RX Path By Switch Path String

Connects the receive (Rx) path you specify to the underlying switch session that was passed into the [NI-RFPM Init With Resources](ni-rfpm_init_with_resources.html) VI. The VI waits until the switch debounces or until **timeout** is reached.

[IMAGE alt='NI-RFPM Set RX Path By Switch Path String' src='ni-rfpm_set_rx_path_by_switch_path_string.gif']

|  | instrument handle identifies your instrument session. instrument handle is obtained from the NI-RFPM Init With Resources VI and identifies a particular instrument session. |
| --- | --- |
|  | RX Switch Path specifies the switch path of the receiver port. This string should be obtained from the Switch Path String parameter of the NI-RFPM Fetch Receiver Offsets VI. |
|  | The error in (no error) cluster can accept error information wired from VIs previously called. Use this information to decide if any functionality should be bypassed in the event of errors from other VIs. Right-click the error in (no error) control on the front panel and select Explain Error or Explain Warning from the shortcut menu for more information about the error. The status boolean is either TRUE (X) for an error, or FALSE (checkmark) for no error or a warning. The pop-up option Explain Error (or Explain Warning) gives more information about the error displayed. The code input identifies the error or warning. The pop-up option Explain Error (or Explain Warning) gives more information about the error displayed. The source string describes the origin of the error or warning. The pop-up option Explain Error (or Explain Warning) gives more information about the error displayed. |
|  | The status boolean is either TRUE (X) for an error, or FALSE (checkmark) for no error or a warning. The pop-up option Explain Error (or Explain Warning) gives more information about the error displayed. |
|  | The code input identifies the error or warning. The pop-up option Explain Error (or Explain Warning) gives more information about the error displayed. |
|  | The source string describes the origin of the error or warning. The pop-up option Explain Error (or Explain Warning) gives more information about the error displayed. |
|  | Timeout specifies the time to wait for the operation to complete before returning an error, expressed in seconds. |
|  | instrument handle out passes a reference to your instrument session to the next VI. instrument handle out is obtained from the NI-RFPM Init With Resources VI and identifies a particular instrument session. |
|  | The error out cluster passes error or warning information out of a VI to be used by other VIs. Use this information to decide if any functionality should be bypassed in the event of errors from other VIs. The status boolean is either TRUE (X) for an error, or FALSE (checkmark) for no error or a warning. The pop-up option Explain Error (or Explain Warning) gives more information about the error displayed. The code output identifies the error or warning. The pop-up option Explain Error (or Explain Warning) gives more information about the error displayed. The source string describes the origin of the error or warning. The pop-up option Explain Error (or Explain Warning) gives more information about the error displayed. |
|  | The status boolean is either TRUE (X) for an error, or FALSE (checkmark) for no error or a warning. The pop-up option Explain Error (or Explain Warning) gives more information about the error displayed. |
|  | The code output identifies the error or warning. The pop-up option Explain Error (or Explain Warning) gives more information about the error displayed. |
|  | The source string describes the origin of the error or warning. The pop-up option Explain Error (or Explain Warning) gives more information about the error displayed. |

<!--NI_TOPIC bundle=ni-rfpm-api-ref path=rfpmviref/ni-rfpm_set_tx_path.html language=enus -->
## TOPIC 00226: NI-RFPM Set TX Path VI

- bundle_id: `ni-rfpm-api-ref`
- source_path: `rfpmviref/ni-rfpm_set_tx_path.html`
- source_url: https://docs-be.ni.com/bundle/ni-rfpm-api-ref/raw/resource/enus/rfpmviref/ni-rfpm_set_tx_path.html
- document_id: `ni-rfpm-api-ref`
- page_type: `leaf`
- content_type: ``

NI-RFPM Set TX Path VI

Installed With:

Connects the transmit (Tx) path you specify to the underlying switch session that was passed into the [NI-RFPM Init With Resources](ni-rfpm_init_with_resources.html) VI. The VI waits until the switch debounces or until **timeout** is reached.

This VI does not support the mmWave subsystem.

#### NI-RFPM Set TX Path By Parameters

Connects the transmit (Tx) path you specify to the underlying switch session that was passed into the [NI-RFPM Init With Resources](ni-rfpm_init_with_resources.html) VI. The VI waits until the switch debounces or until **timeout** is reached.

[IMAGE alt='NI-RFPM Set TX Path By Parameters' src='ni-rfpm_set_tx_path_by_parameters.gif']

|  | instrument handle identifies your instrument session. instrument handle is obtained from the NI-RFPM Init With Resources VI and identifies a particular instrument session. |
| --- | --- |
|  | TX port specifies the port with which the specified transmitter is associated. Valid values are portX, where X is the number of the port, or internalTermination, which connects a termination inside the RF subsystem instead of a port around the blind mate. |
|  | TX path specifies the path to connect using the underlying switch session. Direct NI-RFPM uses the direct path through the NI-RFPM Switch. Gain NI-RFPM uses the amplified path through the NI-RFPM Switch. Loop NI-RFPM uses the path through the bypass loop of the NI-RFPM Switch. Two Tone NI-RFPM uses the path through the bypass loop of the NI-RFPM Switch but retrieves calibration and settling time data specific to the two tone generation solution that can optionally be installed in the loop path. Note Internal termination is only useful when combined with Loop or Two Tone. If internal termination is used with Direct or Gain, there will be no signal out of the STS RF Subsystem. |
| Direct | NI-RFPM uses the direct path through the NI-RFPM Switch. |
| Gain | NI-RFPM uses the amplified path through the NI-RFPM Switch. |
| Loop | NI-RFPM uses the path through the bypass loop of the NI-RFPM Switch. |
| Two Tone | NI-RFPM uses the path through the bypass loop of the NI-RFPM Switch but retrieves calibration and settling time data specific to the two tone generation solution that can optionally be installed in the loop path. |
|  | Note Internal termination is only useful when combined with Loop or Two Tone. If internal termination is used with Direct or Gain, there will be no signal out of the STS RF Subsystem. |
|  | timeout specifies the time to wait for the measurement to complete operation before returning an error, expressed in seconds. |
|  | The error in (no error) cluster can accept error information wired from VIs previously called. Use this information to decide if any functionality should be bypassed in the event of errors from other VIs. Right-click the error in (no error) control on the front panel and select Explain Error or Explain Warning from the shortcut menu for more information about the error. The status boolean is either TRUE (X) for an error, or FALSE (checkmark) for no error or a warning. The pop-up option Explain Error (or Explain Warning) gives more information about the error displayed. The code input identifies the error or warning. The pop-up option Explain Error (or Explain Warning) gives more information about the error displayed. The source string describes the origin of the error or warning. The pop-up option Explain Error (or Explain Warning) gives more information about the error displayed. |
|  | The status boolean is either TRUE (X) for an error, or FALSE (checkmark) for no error or a warning. The pop-up option Explain Error (or Explain Warning) gives more information about the error displayed. |
|  | The code input identifies the error or warning. The pop-up option Explain Error (or Explain Warning) gives more information about the error displayed. |
|  | The source string describes the origin of the error or warning. The pop-up option Explain Error (or Explain Warning) gives more information about the error displayed. |
|  | instrument handle out passes a reference to your instrument session to the next VI. instrument handle out is obtained from the NI-RFPM Init With Resources VI and identifies a particular instrument session. |
|  | The error out cluster passes error or warning information out of a VI to be used by other VIs. Use this information to decide if any functionality should be bypassed in the event of errors from other VIs. The status boolean is either TRUE (X) for an error, or FALSE (checkmark) for no error or a warning. The pop-up option Explain Error (or Explain Warning) gives more information about the error displayed. The code output identifies the error or warning. The pop-up option Explain Error (or Explain Warning) gives more information about the error displayed. The source string describes the origin of the error or warning. The pop-up option Explain Error (or Explain Warning) gives more information about the error displayed. |
|  | The status boolean is either TRUE (X) for an error, or FALSE (checkmark) for no error or a warning. The pop-up option Explain Error (or Explain Warning) gives more information about the error displayed. |
|  | The code output identifies the error or warning. The pop-up option Explain Error (or Explain Warning) gives more information about the error displayed. |
|  | The source string describes the origin of the error or warning. The pop-up option Explain Error (or Explain Warning) gives more information about the error displayed. |

#### NI-RFPM Set TX Path By Switch Path String

Connects the transmit (Tx) path you specify to the underlying switch session that was passed into the [NI-RFPM Init With Resources](ni-rfpm_init_with_resources.html) VI. The VI waits until the switch debounces or until **timeout** is reached.

[IMAGE alt='NI-RFPM Set TX Path By Switch Path String' src='ni-rfpm_set_tx_path_by_switch_path_string.gif']

|  | instrument handle identifies your instrument session. instrument handle is obtained from the NI-RFPM Init With Resources VI and identifies a particular instrument session. |
| --- | --- |
|  | TX Switch Path specifies the switch path of the transmit port. This string should be obtained from the Switch Path String parameter of the NI-RFPM Fetch Source Offset With Setting and Settling Time VI. Valid value is supported end point of internalTermination, which connects a termination inside the RF subsystem instead of a port around the blindmate. |
|  | timeout specifies the time to wait for the measurement to complete operation before returning an error, expressed in seconds. |
|  | The error in (no error) cluster can accept error information wired from VIs previously called. Use this information to decide if any functionality should be bypassed in the event of errors from other VIs. Right-click the error in (no error) control on the front panel and select Explain Error or Explain Warning from the shortcut menu for more information about the error. The status boolean is either TRUE (X) for an error, or FALSE (checkmark) for no error or a warning. The pop-up option Explain Error (or Explain Warning) gives more information about the error displayed. The code input identifies the error or warning. The pop-up option Explain Error (or Explain Warning) gives more information about the error displayed. The source string describes the origin of the error or warning. The pop-up option Explain Error (or Explain Warning) gives more information about the error displayed. |
|  | The status boolean is either TRUE (X) for an error, or FALSE (checkmark) for no error or a warning. The pop-up option Explain Error (or Explain Warning) gives more information about the error displayed. |
|  | The code input identifies the error or warning. The pop-up option Explain Error (or Explain Warning) gives more information about the error displayed. |
|  | The source string describes the origin of the error or warning. The pop-up option Explain Error (or Explain Warning) gives more information about the error displayed. |
|  | instrument handle out passes a reference to your instrument session to the next VI. instrument handle out is obtained from the NI-RFPM Init With Resources VI and identifies a particular instrument session. |
|  | The error out cluster passes error or warning information out of a VI to be used by other VIs. Use this information to decide if any functionality should be bypassed in the event of errors from other VIs. The status boolean is either TRUE (X) for an error, or FALSE (checkmark) for no error or a warning. The pop-up option Explain Error (or Explain Warning) gives more information about the error displayed. The code output identifies the error or warning. The pop-up option Explain Error (or Explain Warning) gives more information about the error displayed. The source string describes the origin of the error or warning. The pop-up option Explain Error (or Explain Warning) gives more information about the error displayed. |
|  | The status boolean is either TRUE (X) for an error, or FALSE (checkmark) for no error or a warning. The pop-up option Explain Error (or Explain Warning) gives more information about the error displayed. |
|  | The code output identifies the error or warning. The pop-up option Explain Error (or Explain Warning) gives more information about the error displayed. |
|  | The source string describes the origin of the error or warning. The pop-up option Explain Error (or Explain Warning) gives more information about the error displayed. |

<!--NI_TOPIC bundle=ni-rfpm-api-ref path=rfpmviref/ni-rfpm_wait_calibration_action_done.html language=enus -->
## TOPIC 00227: NI-RFPM Wait Calibration Action Done VI

- bundle_id: `ni-rfpm-api-ref`
- source_path: `rfpmviref/ni-rfpm_wait_calibration_action_done.html`
- source_url: https://docs-be.ni.com/bundle/ni-rfpm-api-ref/raw/resource/enus/rfpmviref/ni-rfpm_wait_calibration_action_done.html
- document_id: `ni-rfpm-api-ref`
- page_type: `leaf`
- content_type: ``

NI-RFPM Wait Calibration Action Done VI

Installed With:

Waits for the last user calibration action to complete. If the calibration action does not complete before the specified timeout, this VI returns a timeout error.

This VI does not support the mmWave subsystem.

[Details](#details)

[IMAGE alt='NI-RFPM Wait Calibration Action Done' src='ni-rfpm_wait_calibration_action_done.gif']

|  | instrument handle identifies your instrument session. instrument handle is obtained from the NI-RFPM Init With Resources VI and identifies a particular instrument session. |
| --- | --- |
|  | The error in cluster can accept error information wired from VIs previously called. Use this information to decide if any functionality should be bypassed in the event of errors from other VIs. Right-click the error in control on the front panel and select Explain Error or Explain Warning from the shortcut menu for more information about the error. The status boolean is either TRUE (X) for an error, or FALSE (checkmark) for no error or a warning. The pop-up option Explain Error (or Explain Warning) gives more information about the error displayed. The code input identifies the error or warning. The pop-up option Explain Error (or Explain Warning) gives more information about the error displayed. The source string describes the origin of the error or warning. The pop-up option Explain Error (or Explain Warning) gives more information about the error displayed. |
|  | The status boolean is either TRUE (X) for an error, or FALSE (checkmark) for no error or a warning. The pop-up option Explain Error (or Explain Warning) gives more information about the error displayed. |
|  | The code input identifies the error or warning. The pop-up option Explain Error (or Explain Warning) gives more information about the error displayed. |
|  | The source string describes the origin of the error or warning. The pop-up option Explain Error (or Explain Warning) gives more information about the error displayed. |
|  | Timeout specifies the time to wait for the measurement to complete operation before returning an error, expressed in seconds. |
|  | instrument handle out passes a reference to your instrument session to the next VI. instrument handle out is obtained from the NI-RFPM Init With Resources VI and identifies a particular instrument session. |
|  | The error out cluster passes error or warning information out of a VI to be used by other VIs. Use this information to decide if any functionality should be bypassed in the event of errors from other VIs. The status boolean is either TRUE (X) for an error, or FALSE (checkmark) for no error or a warning. The pop-up option Explain Error (or Explain Warning) gives more information about the error displayed. The code output identifies the error or warning. The pop-up option Explain Error (or Explain Warning) gives more information about the error displayed. The source string describes the origin of the error or warning. The pop-up option Explain Error (or Explain Warning) gives more information about the error displayed. |
|  | The status boolean is either TRUE (X) for an error, or FALSE (checkmark) for no error or a warning. The pop-up option Explain Error (or Explain Warning) gives more information about the error displayed. |
|  | The code output identifies the error or warning. The pop-up option Explain Error (or Explain Warning) gives more information about the error displayed. |
|  | The source string describes the origin of the error or warning. The pop-up option Explain Error (or Explain Warning) gives more information about the error displayed. |

#### Details

|  | Note In rare instances, a calibration returns warning 0x3FFA4000 ("The desired accuracy could not be achieved within the maximum number of iterations.”) Due to the small residual error and the minimal impact on the specifications, NI-RFPM does not generate an error. |
| --- | --- |

<!--NI_TOPIC bundle=ni-rfpm-api-ref path=rfpmviref/ni-rfpm_wait_for_measurement_done.html language=enus -->
## TOPIC 00228: NI-RFPM Wait For Measurement Done VI

- bundle_id: `ni-rfpm-api-ref`
- source_path: `rfpmviref/ni-rfpm_wait_for_measurement_done.html`
- source_url: https://docs-be.ni.com/bundle/ni-rfpm-api-ref/raw/resource/enus/rfpmviref/ni-rfpm_wait_for_measurement_done.html
- document_id: `ni-rfpm-api-ref`
- page_type: `leaf`
- content_type: ``

NI-RFPM Wait For Measurement Done VI

Installed With:

Waits for the measurement to complete. If the measurement does not complete within the specified **timeout**, this VI returns a timeout error.

[IMAGE alt='NI-RFPM Wait For Measurement Done' src='ni-rfpm_wait_for_measurement_done.gif']

|  | instrument handle identifies your instrument session. instrument handle is obtained from the NI-RFPM Init With Resources VI and identifies a particular instrument session. |
| --- | --- |
|  | The error in cluster can accept error information wired from VIs previously called. Use this information to decide if any functionality should be bypassed in the event of errors from other VIs. Right-click the error in control on the front panel and select Explain Error or Explain Warning from the shortcut menu for more information about the error. The status boolean is either TRUE (X) for an error, or FALSE (checkmark) for no error or a warning. The pop-up option Explain Error (or Explain Warning) gives more information about the error displayed. The code input identifies the error or warning. The pop-up option Explain Error (or Explain Warning) gives more information about the error displayed. The source string describes the origin of the error or warning. The pop-up option Explain Error (or Explain Warning) gives more information about the error displayed. |
|  | The status boolean is either TRUE (X) for an error, or FALSE (checkmark) for no error or a warning. The pop-up option Explain Error (or Explain Warning) gives more information about the error displayed. |
|  | The code input identifies the error or warning. The pop-up option Explain Error (or Explain Warning) gives more information about the error displayed. |
|  | The source string describes the origin of the error or warning. The pop-up option Explain Error (or Explain Warning) gives more information about the error displayed. |
|  | Timeout specifies the time to wait for the operation to complete before returning an error, expressed in seconds. |
|  | instrument handle out passes a reference to your instrument session to the next VI. instrument handle out is obtained from the NI-RFPM Init With Resources VI and identifies a particular instrument session. |
|  | The error out cluster passes error or warning information out of a VI to be used by other VIs. Use this information to decide if any functionality should be bypassed in the event of errors from other VIs. The status boolean is either TRUE (X) for an error, or FALSE (checkmark) for no error or a warning. The pop-up option Explain Error (or Explain Warning) gives more information about the error displayed. The code output identifies the error or warning. The pop-up option Explain Error (or Explain Warning) gives more information about the error displayed. The source string describes the origin of the error or warning. The pop-up option Explain Error (or Explain Warning) gives more information about the error displayed. |
|  | The status boolean is either TRUE (X) for an error, or FALSE (checkmark) for no error or a warning. The pop-up option Explain Error (or Explain Warning) gives more information about the error displayed. |
|  | The code output identifies the error or warning. The pop-up option Explain Error (or Explain Warning) gives more information about the error displayed. |
|  | The source string describes the origin of the error or warning. The pop-up option Explain Error (or Explain Warning) gives more information about the error displayed. |

<!--NI_TOPIC bundle=ni-rfpm-api-ref path=rfpmviref/switch_pal.html language=enus -->
## TOPIC 00229: Switch

- bundle_id: `ni-rfpm-api-ref`
- source_path: `rfpmviref/switch_pal.html`
- source_url: https://docs-be.ni.com/bundle/ni-rfpm-api-ref/raw/resource/enus/rfpmviref/switch_pal.html
- document_id: `ni-rfpm-api-ref`
- page_type: `leaf`
- content_type: ``

Switch

Owning Palette:

NI-RFPM VIs

Installed With:

Use the NI-RFPM Switch VIs to control measurement operations with your STS device.

| Palette Object | Description |
| --- | --- |
| NI-RFPM Disconnect All Paths | Disconnects all existing paths in the underlying switch session that was passed into the NI-RFPM Init With Resources VI. This VI does not support the mmWave subsystem. |
| NI-RFPM Read Connected RX Paths | Queries which STS receive paths are currently connected. This VI does not support the mmWave subsystem. |
| NI-RFPM Read Connected TX Paths | Queries which TX switch paths are currently connected and returns an array of path enums and port strings. This VI does not support the mmWave subsystem. |
| NI-RFPM Read Receiver Settling Time | Queries how long a user must wait for the signal at the NI-RFPM switch receiver output channel to settle within the receiver amplitude accuracy specified by the Receiver Amplitude Settling property. When NI-RFPM de-embedding is enabled, the reference level is defined at the DUT reference plane. This VI does not support the mmWave subsystem. |
| NI-RFPM Set RX Path | Connects the receive (Rx) path you specify to the underlying switch session that was passed into the NI-RFPM Init With Resources VI. The VI waits until the switch debounces or until timeout is reached. This VI does not support the mmWave subsystem. |
| NI-RFPM Set Receiver Port and Path For RFmx Callbacks | Sets the port, receiver path, and receiver coupling path for RFmx callback functions to use. This VI does not support the mmWave subsystem. |
| NI-RFPM Set TX Path | Connects the transmit (Tx) path you specify to the underlying switch session that was passed into the NI-RFPM Init With Resources VI. The VI waits until the switch debounces or until timeout is reached. This VI does not support the mmWave subsystem. |

<!--NI_TOPIC bundle=ni-rfpm-api-ref path=rfpmviref/utility_pal.html language=enus -->
## TOPIC 00230: Utility

- bundle_id: `ni-rfpm-api-ref`
- source_path: `rfpmviref/utility_pal.html`
- source_url: https://docs-be.ni.com/bundle/ni-rfpm-api-ref/raw/resource/enus/rfpmviref/utility_pal.html
- document_id: `ni-rfpm-api-ref`
- page_type: `leaf`
- content_type: ``

Utility

Owning Palette:

NI-RFPM VIs

Installed With:

Use the NI-RFPM Utility VIs to access utility features of NI-RFPM.

| Palette Object | Description |
| --- | --- |
| NI-RFPM Abort | Stops any measurement previously initiated by the NI-RFPM Initiate VI. |
| NI-RFPM Error Query | Converts an error code returned by an NI-RFPM VI into a user-readable string. |
| NI-RFPM Get Callbacks For RFmx | Returns pointers to callback functions to be passed into RFmx. This VI does not support the mmWave subsystem. |
| NI-RFPM Read Measurement Resources | Returns the stored handles to the measurement resources used by NI-RFPM. These are the same handles that are passed into the NI-RFPM Init With Resources VI. |
| NI-RFPM Reset Device | Resets all attributes and devices, including NI-RFSA and NI-RFSG sessions, to their default states, and clears a latched interlock signal. This VI does not support the mmWave subsystem. |
| NI-RFPM Revision Query | Returns driver and firmware revision information. |
| NI-RFPM Self-Test | Performs a self-test on the STS device and returns the test result. This VI performs a series of simple tests verifying that the STS device is powered on and responding. This VI does not support the mmWave subsystem. |
