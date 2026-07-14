# NI DOCUMENT BUNDLE: ni-scope-dotnet-api-ref

<!--NI_BUNDLE_CHUNK bundle=ni-scope-dotnet-api-ref start=1 end=33 -->
<!--NI_TOPIC bundle=ni-scope-dotnet-api-ref path=ninetscopefx45ref/html/m_nationalinstruments_modularinstruments_niscope_niscope_isdeviceready.htm language=enus -->
## TOPIC 00001: ninetscopefx45ref/html/m_nationalinstruments_modularinstruments_niscope_niscope_isdeviceready.htm

- bundle_id: `ni-scope-dotnet-api-ref`
- source_path: `ninetscopefx45ref/html/m_nationalinstruments_modularinstruments_niscope_niscope_isdeviceready.htm`
- source_url: https://docs-be.ni.com/bundle/ni-scope-dotnet-api-ref/raw/resource/enus/ninetscopefx45ref/html/m_nationalinstruments_modularinstruments_niscope_niscope_isdeviceready.htm
- document_id: `ni-scope-dotnet-api-ref`
- page_type: `leaf`
- content_type: ``

NIScope.IsDeviceReady Method

NIScopeIsDeviceReady Method

Determines whether the instrument is ready for use or the instrument is still undergoing initialization.

Namespace:

NationalInstruments.ModularInstruments.NIScope

Assembly:

##### Syntax

C#

VB

```text
public static bool IsDeviceReady(
	string resourceName
)
```

```text
Public Shared Function IsDeviceReady ( 
	resourceName As String
) As Boolean
```

###### Parameters

- **resourceName**
  - Type: SystemStringThe name of the instrument to be checked.

###### Return Value

Boolean

##### See Also

###### Reference

NIScope Class

NationalInstruments.ModularInstruments.NIScope Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=ni-scope-dotnet-api-ref path=ninetscopefx45ref/html/m_nationalinstruments_modularinstruments_niscope_scopeadvancetriggersource_op_implicit.1.htm language=enus -->
## TOPIC 00002: ninetscopefx45ref/html/m_nationalinstruments_modularinstruments_niscope_scopeadvancetriggersource_op_implicit.1.htm

- bundle_id: `ni-scope-dotnet-api-ref`
- source_path: `ninetscopefx45ref/html/m_nationalinstruments_modularinstruments_niscope_scopeadvancetriggersource_op_implicit.1.htm`
- source_url: https://docs-be.ni.com/bundle/ni-scope-dotnet-api-ref/raw/resource/enus/ninetscopefx45ref/html/m_nationalinstruments_modularinstruments_niscope_scopeadvancetriggersource_op_implicit.1.htm
- document_id: `ni-scope-dotnet-api-ref`
- page_type: `leaf`
- content_type: ``

ScopeAdvanceTriggerSource Implicit Conversion (String to ScopeAdvanceTriggerSource)

ScopeAdvanceTriggerSource  Conversion (String to ScopeAdvanceTriggerSource)

String

ScopeAdvanceTriggerSource

Namespace:

NationalInstruments.ModularInstruments.NIScope

Assembly:

##### Syntax

C#

VB

```text
public static implicit operator ScopeAdvanceTriggerSource (
	string source
)
```

```text
Public Shared Widening Operator CType ( 
	source As String
) As ScopeAdvanceTriggerSource
```

###### Parameters

- **source**
  - Type: SystemString Specifies the String to be converted to an equivalent ScopeAdvanceTriggerSource object.

###### Return Value

ScopeAdvanceTriggerSource

ScopeAdvanceTriggerSource

String

##### See Also

###### Reference

ScopeAdvanceTriggerSource Class

NationalInstruments.ModularInstruments.NIScope Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=ni-scope-dotnet-api-ref path=ninetscopefx45ref/html/m_nationalinstruments_modularinstruments_niscope_scopechannel_getfrequencyresponse.htm language=enus -->
## TOPIC 00003: ninetscopefx45ref/html/m_nationalinstruments_modularinstruments_niscope_scopechannel_getfrequencyresponse.htm

- bundle_id: `ni-scope-dotnet-api-ref`
- source_path: `ninetscopefx45ref/html/m_nationalinstruments_modularinstruments_niscope_scopechannel_getfrequencyresponse.htm`
- source_url: https://docs-be.ni.com/bundle/ni-scope-dotnet-api-ref/raw/resource/enus/ninetscopefx45ref/html/m_nationalinstruments_modularinstruments_niscope_scopechannel_getfrequencyresponse.htm
- document_id: `ni-scope-dotnet-api-ref`
- page_type: `leaf`
- content_type: ``

ScopeChannel.GetFrequencyResponse Method

ScopeChannelGetFrequencyResponse Method

Gets the frequency response of the digitizer for the current configurations of the channel attributes.

Namespace:

NationalInstruments.ModularInstruments.NIScope

Assembly:

##### Syntax

C#

VB

```text
public void GetFrequencyResponse(
	out double[] frequencies,
	out double[] amplitudes,
	out double[] phases
)
```

```text
Public Sub GetFrequencyResponse ( 
	<OutAttribute> ByRef frequencies As Double(),
	<OutAttribute> ByRef amplitudes As Double(),
	<OutAttribute> ByRef phases As Double()
)
```

###### Parameters

- **frequencies**
  - Type: SystemDouble The frequencies that correspond with the amplitude and phase response of the instrument.
- **amplitudes**
  - Type: SystemDouble The magnitudes that correspond with the magnitude response of the instrument.
- **phases**
  - Type: SystemDouble The phases that correspond with the phase response of the instrument.

##### Remarks

You can use this method only with high-speed digitizers that support onboard signal processing (OSP).

##### See Also

###### Reference

ScopeChannel Class

NationalInstruments.ModularInstruments.NIScope Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=ni-scope-dotnet-api-ref path=ninetscopefx45ref/html/m_nationalinstruments_modularinstruments_niscope_scopechannelmeasurement_beginfetchcomplexint16.htm language=enus -->
## TOPIC 00004: ninetscopefx45ref/html/m_nationalinstruments_modularinstruments_niscope_scopechannelmeasurement_beginfetchcomplexint16.htm

- bundle_id: `ni-scope-dotnet-api-ref`
- source_path: `ninetscopefx45ref/html/m_nationalinstruments_modularinstruments_niscope_scopechannelmeasurement_beginfetchcomplexint16.htm`
- source_url: https://docs-be.ni.com/bundle/ni-scope-dotnet-api-ref/raw/resource/enus/ninetscopefx45ref/html/m_nationalinstruments_modularinstruments_niscope_scopechannelmeasurement_beginfetchcomplexint16.htm
- document_id: `ni-scope-dotnet-api-ref`
- page_type: `leaf`
- content_type: ``

ScopeChannelMeasurement.BeginFetchComplexInt16 Method

ScopeChannelMeasurementBeginFetchComplexInt16 Method

Begins an asynchronous retrieval of data from single channels and records.

Namespace:

NationalInstruments.ModularInstruments.NIScope

Assembly:

##### Syntax

C#

VB

```text
public IAsyncResult BeginFetchComplexInt16(
	PrecisionTimeSpan timeout,
	long numberOfSamples,
	ComplexWaveformCollection<ComplexInt16> waveforms,
	AsyncCallback callback,
	Object asyncState
)
```

```text
Public Function BeginFetchComplexInt16 ( 
	timeout As PrecisionTimeSpan,
	numberOfSamples As Long,
	waveforms As ComplexWaveformCollection(Of ComplexInt16),
	callback As AsyncCallback,
	asyncState As Object
) As IAsyncResult
```

###### Parameters

- **timeout**
  - Type: NationalInstrumentsPrecisionTimeSpan The time to wait for data to be acquired. Using 0 for this parameter tells NI-SCOPE to fetch whatever is currently available. Using -1 for this parameter implies infinite timeout.
- **numberOfSamples**
  - Type: SystemInt64 The maximum number of samples to fetch for each waveform. If the acquisition finishes with fewer points than requested, some instruments return partial data if the acquisition finished, was aborted, or a timeout of 0 was used. Use –1 for this parameter if you want to fetch all available samples. The method reads the actual record length and attempts to acquire all available samples. If it fails to complete within the timeout period, the method returns an error.
- **waveforms**
  - Type: NationalInstrumentsComplexWaveformCollectionComplexInt16 An array of type ComplexWaveformCollectionTData.
- **callback**
  - Type: SystemAsyncCallback A delegate of type AsyncCallback, which will be invoked once the operation is complete.
- **asyncState**
  - Type: SystemObject The state of the asynchronous operation.

###### Return Value

IAsyncResult

IAsyncResult

##### See Also

###### Reference

ScopeChannelMeasurement Class

NationalInstruments.ModularInstruments.NIScope Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=ni-scope-dotnet-api-ref path=ninetscopefx45ref/html/m_nationalinstruments_modularinstruments_niscope_scopedriveridentity_getgroupcapabilities.htm language=enus -->
## TOPIC 00005: ninetscopefx45ref/html/m_nationalinstruments_modularinstruments_niscope_scopedriveridentity_getgroupcapabilities.htm

- bundle_id: `ni-scope-dotnet-api-ref`
- source_path: `ninetscopefx45ref/html/m_nationalinstruments_modularinstruments_niscope_scopedriveridentity_getgroupcapabilities.htm`
- source_url: https://docs-be.ni.com/bundle/ni-scope-dotnet-api-ref/raw/resource/enus/ninetscopefx45ref/html/m_nationalinstruments_modularinstruments_niscope_scopedriveridentity_getgroupcapabilities.htm
- document_id: `ni-scope-dotnet-api-ref`
- page_type: `leaf`
- content_type: ``

ScopeDriverIdentity.GetGroupCapabilities Method

ScopeDriverIdentityGetGroupCapabilities Method

Returns a list of names of class capability groups that the IVI specific driver implements.

Namespace:

NationalInstruments.ModularInstruments.NIScope

Assembly:

##### Syntax

C#

VB

```text
public string[] GetGroupCapabilities()
```

```text
Public Function GetGroupCapabilities As String()
```

###### Return Value

String

String

###### Implements

##### See Also

###### Reference

ScopeDriverIdentity Class

NationalInstruments.ModularInstruments.NIScope Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=ni-scope-dotnet-api-ref path=ninetscopefx45ref/html/m_nationalinstruments_modularinstruments_niscope_scopedriverlock_dispose.htm language=enus -->
## TOPIC 00006: ninetscopefx45ref/html/m_nationalinstruments_modularinstruments_niscope_scopedriverlock_dispose.htm

- bundle_id: `ni-scope-dotnet-api-ref`
- source_path: `ninetscopefx45ref/html/m_nationalinstruments_modularinstruments_niscope_scopedriverlock_dispose.htm`
- source_url: https://docs-be.ni.com/bundle/ni-scope-dotnet-api-ref/raw/resource/enus/ninetscopefx45ref/html/m_nationalinstruments_modularinstruments_niscope_scopedriverlock_dispose.htm
- document_id: `ni-scope-dotnet-api-ref`
- page_type: `leaf`
- content_type: ``

ScopeDriverLock.Dispose Method

ScopeDriverLockDispose Method

Releases a driver synchronization lock.

Namespace:

NationalInstruments.ModularInstruments.NIScope

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

ScopeDriverLock Class

NationalInstruments.ModularInstruments.NIScope Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=ni-scope-dotnet-api-ref path=ninetscopefx45ref/html/m_nationalinstruments_modularinstruments_niscope_scopedriverutility_disable.htm language=enus -->
## TOPIC 00007: ninetscopefx45ref/html/m_nationalinstruments_modularinstruments_niscope_scopedriverutility_disable.htm

- bundle_id: `ni-scope-dotnet-api-ref`
- source_path: `ninetscopefx45ref/html/m_nationalinstruments_modularinstruments_niscope_scopedriverutility_disable.htm`
- source_url: https://docs-be.ni.com/bundle/ni-scope-dotnet-api-ref/raw/resource/enus/ninetscopefx45ref/html/m_nationalinstruments_modularinstruments_niscope_scopedriverutility_disable.htm
- document_id: `ni-scope-dotnet-api-ref`
- page_type: `leaf`
- content_type: ``

ScopeDriverUtility.Disable Method

ScopeDriverUtilityDisable Method

Places the instrument in a quiescent state as quickly as possible.

Namespace:

NationalInstruments.ModularInstruments.NIScope

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

##### Remarks

In a quiescent state, an instrument has no or minimal effect on the external system to which it is connected.

##### See Also

###### Reference

ScopeDriverUtility Class

NationalInstruments.ModularInstruments.NIScope Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=ni-scope-dotnet-api-ref path=ninetscopefx45ref/html/m_nationalinstruments_modularinstruments_niscope_scopedriverutility_exportattributeconfigurationbuffer.htm language=enus -->
## TOPIC 00008: ninetscopefx45ref/html/m_nationalinstruments_modularinstruments_niscope_scopedriverutility_exportattributeconfigurationbuffer.htm

- bundle_id: `ni-scope-dotnet-api-ref`
- source_path: `ninetscopefx45ref/html/m_nationalinstruments_modularinstruments_niscope_scopedriverutility_exportattributeconfigurationbuffer.htm`
- source_url: https://docs-be.ni.com/bundle/ni-scope-dotnet-api-ref/raw/resource/enus/ninetscopefx45ref/html/m_nationalinstruments_modularinstruments_niscope_scopedriverutility_exportattributeconfigurationbuffer.htm
- document_id: `ni-scope-dotnet-api-ref`
- page_type: `leaf`
- content_type: ``

ScopeDriverUtility.ExportAttributeConfigurationBuffer Method

ScopeDriverUtilityExportAttributeConfigurationBuffer Method

Byte

Namespace:

NationalInstruments.ModularInstruments.NIScope

Assembly:

##### Syntax

C#

VB

```text
public byte[] ExportAttributeConfigurationBuffer()
```

```text
Public Function ExportAttributeConfigurationBuffer As Byte()
```

###### Return Value

Byte

Byte

##### Exceptions

| Exception | Condition |
| --- | --- |
| ObjectDisposedException | The ExportAttributeConfigurationBuffer method was called after the associated NIScope object was disposed. |
| IviCDriverException | The underlying NI-SCOPE driver returned an error. |

##### Remarks

NIScope

- The configuration exported from PXI1Slot1 is imported into PXI2Slot2.
- The configuration exported from PXI1Slot2 is imported into PXI2Slot3.

| Note |
| --- |
| NI-SCOPE will return an error if the total number of channels initialized for the exporting session is not equal to the total number of channels initialized for the importing session. |

##### See Also

###### Reference

ScopeDriverUtility Class

NationalInstruments.ModularInstruments.NIScope Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=ni-scope-dotnet-api-ref path=ninetscopefx45ref/html/m_nationalinstruments_modularinstruments_niscope_scopedriverutility_getchannelnamefromstring.htm language=enus -->
## TOPIC 00009: ninetscopefx45ref/html/m_nationalinstruments_modularinstruments_niscope_scopedriverutility_getchannelnamefromstring.htm

- bundle_id: `ni-scope-dotnet-api-ref`
- source_path: `ninetscopefx45ref/html/m_nationalinstruments_modularinstruments_niscope_scopedriverutility_getchannelnamefromstring.htm`
- source_url: https://docs-be.ni.com/bundle/ni-scope-dotnet-api-ref/raw/resource/enus/ninetscopefx45ref/html/m_nationalinstruments_modularinstruments_niscope_scopedriverutility_getchannelnamefromstring.htm
- document_id: `ni-scope-dotnet-api-ref`
- page_type: `leaf`
- content_type: ``

ScopeDriverUtility.GetChannelNameFromString Method

ScopeDriverUtilityGetChannelNameFromString Method

String

Namespace:

NationalInstruments.ModularInstruments.NIScope

Assembly:

##### Syntax

C#

VB

```text
public string GetChannelNameFromString(
	string index
)
```

```text
Public Function GetChannelNameFromString ( 
	index As String
) As String
```

###### Parameters

- **index**
  - Type: SystemString Index list for the channels in the session. Valid values are from 0 to the number of channels in the session minus 1. The input string can be in one of the following formats: "0,2,3,1" --> Comma-separated list "0-3" --> Range using a hyphen "0:3" --> Range using a colon - The above formats can be combined: "1, 1:2, 0-3" - Out-of-order indices are supported: "2,3,0" - Repeated indices are supported: "1, 2, 2, 3, 0" - White-space characters (space, tab, newline, vertical tab, feed, carriage return) are allowed between characters: " 1,2", "1 , 2 ", " 1 ,2 ", "1, 2", "1 , 2" are valid strings - Ranges can be incrementing (0-3) or decrementing (3-0)

###### Return Value

String

String

##### Exceptions

| Exception | Condition |
| --- | --- |
| ObjectDisposedException | The GetChannelNameFromString(String) method was called after the associated NIScope or ScopeDriverUtility object was disposed. |
| OutOfRangeException | If one of the indices in the list is greater than or equal to the number of channels in the session. |
| SelectorNameException | If the input list does not have a valid format or contains a negative index. |
| IviCDriverException | If the input list is empty. |

##### Remarks

##### See Also

###### Reference

ScopeDriverUtility Class

NationalInstruments.ModularInstruments.NIScope Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=ni-scope-dotnet-api-ref path=ninetscopefx45ref/html/m_nationalinstruments_modularinstruments_niscope_scopedriverutility_importattributeconfigurationbuffer.htm language=enus -->
## TOPIC 00010: ninetscopefx45ref/html/m_nationalinstruments_modularinstruments_niscope_scopedriverutility_importattributeconfigurationbuffer.htm

- bundle_id: `ni-scope-dotnet-api-ref`
- source_path: `ninetscopefx45ref/html/m_nationalinstruments_modularinstruments_niscope_scopedriverutility_importattributeconfigurationbuffer.htm`
- source_url: https://docs-be.ni.com/bundle/ni-scope-dotnet-api-ref/raw/resource/enus/ninetscopefx45ref/html/m_nationalinstruments_modularinstruments_niscope_scopedriverutility_importattributeconfigurationbuffer.htm
- document_id: `ni-scope-dotnet-api-ref`
- page_type: `leaf`
- content_type: ``

ScopeDriverUtility.ImportAttributeConfigurationBuffer Method

ScopeDriverUtilityImportAttributeConfigurationBuffer Method

Byte

configuration

Namespace:

NationalInstruments.ModularInstruments.NIScope

Assembly:

##### Syntax

C#

VB

```text
public void ImportAttributeConfigurationBuffer(
	byte[] configuration
)
```

```text
Public Sub ImportAttributeConfigurationBuffer ( 
	configuration As Byte()
)
```

###### Parameters

- **configuration**
  - Type: SystemByte The byte array that contains the attribute configuration to import.

##### Exceptions

| Exception | Condition |
| --- | --- |
| ObjectDisposedException | The ImportAttributeConfigurationBuffer(Byte) method was called after the associated NIScope object was disposed. |
| NullReferenceException | The buffer or its underlying data have been disposed |
| IviCDriverException | The underlying NI-SCOPE driver returned an error. |

##### Remarks

| Note |
| --- |
| You cannot call this method while the session is in a running state, such as while acquiring a signal. |

NIScope

- The configuration exported from PXI1Slot1 is imported into PXI2Slot2.
- The configuration exported from PXI1Slot2 is imported into PXI2Slot3.

| Note |
| --- |
| NI-SCOPE will return an error if the total number of channels initialized for the exporting session is not equal to the total number of channels initialized for the importing session. |

##### See Also

###### Reference

ScopeDriverUtility Class

NationalInstruments.ModularInstruments.NIScope Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=ni-scope-dotnet-api-ref path=ninetscopefx45ref/html/m_nationalinstruments_modularinstruments_niscope_scopedriverutility_importattributeconfigurationfile.htm language=enus -->
## TOPIC 00011: ninetscopefx45ref/html/m_nationalinstruments_modularinstruments_niscope_scopedriverutility_importattributeconfigurationfile.htm

- bundle_id: `ni-scope-dotnet-api-ref`
- source_path: `ninetscopefx45ref/html/m_nationalinstruments_modularinstruments_niscope_scopedriverutility_importattributeconfigurationfile.htm`
- source_url: https://docs-be.ni.com/bundle/ni-scope-dotnet-api-ref/raw/resource/enus/ninetscopefx45ref/html/m_nationalinstruments_modularinstruments_niscope_scopedriverutility_importattributeconfigurationfile.htm
- document_id: `ni-scope-dotnet-api-ref`
- page_type: `leaf`
- content_type: ``

ScopeDriverUtility.ImportAttributeConfigurationFile Method

ScopeDriverUtilityImportAttributeConfigurationFile Method

Imports an attribute configuration to the session from the specified file.

Namespace:

NationalInstruments.ModularInstruments.NIScope

Assembly:

##### Syntax

C#

VB

```text
public void ImportAttributeConfigurationFile(
	string filePath
)
```

```text
Public Sub ImportAttributeConfigurationFile ( 
	filePath As String
)
```

###### Parameters

- **filePath**
  - Type: SystemString The absolute path to the file containing the attribute configuration to import. If you specify an empty or relative path, this method returns an error. The default file extension is .niscopeconfig.

##### Exceptions

| Exception | Condition |
| --- | --- |
| ObjectDisposedException | The ImportAttributeConfigurationFile(String) method was called after the associated NIScope object was disposed. |
| IviCDriverException | The underlying NI-SCOPE driver returned an error. |

##### Remarks

| Note |
| --- |
| You cannot call this method while the session is in a running state, such as while acquiring a signal. |

NIScope

- The configuration exported from PXI1Slot1 is imported into PXI2Slot2.
- The configuration exported from PXI1Slot2 is imported into PXI2Slot3.

| Note |
| --- |
| NI-SCOPE will return an error if the total number of channels initialized for the exporting session is not equal to the total number of channels initialized for the importing session. |

##### See Also

###### Reference

ScopeDriverUtility Class

NationalInstruments.ModularInstruments.NIScope Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=ni-scope-dotnet-api-ref path=ninetscopefx45ref/html/m_nationalinstruments_modularinstruments_niscope_scopedriverutility_lock.1.htm language=enus -->
## TOPIC 00012: ninetscopefx45ref/html/m_nationalinstruments_modularinstruments_niscope_scopedriverutility_lock.1.htm

- bundle_id: `ni-scope-dotnet-api-ref`
- source_path: `ninetscopefx45ref/html/m_nationalinstruments_modularinstruments_niscope_scopedriverutility_lock.1.htm`
- source_url: https://docs-be.ni.com/bundle/ni-scope-dotnet-api-ref/raw/resource/enus/ninetscopefx45ref/html/m_nationalinstruments_modularinstruments_niscope_scopedriverutility_lock.1.htm
- document_id: `ni-scope-dotnet-api-ref`
- page_type: `leaf`
- content_type: ``

ScopeDriverUtility.Lock Method (PrecisionTimeSpan)

ScopeDriverUtilityLock Method (PrecisionTimeSpan)

Attempts to acquire a synchronization lock on this instance of the driver and specifies the maximum amount of time to wait to acquire the lock.

Namespace:

NationalInstruments.ModularInstruments.NIScope

Assembly:

##### Syntax

C#

VB

```text
public ScopeDriverLock Lock(
	PrecisionTimeSpan maxTime
)
```

```text
Public Function Lock ( 
	maxTime As PrecisionTimeSpan
) As ScopeDriverLock
```

###### Parameters

- **maxTime**
  - Type: NationalInstrumentsPrecisionTimeSpan The maximum amount of time to wait to acquire the lock.

###### Return Value

ScopeDriverLock

##### See Also

###### Reference

ScopeDriverUtility Class

Lock Overload

NationalInstruments.ModularInstruments.NIScope Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=ni-scope-dotnet-api-ref path=ninetscopefx45ref/html/m_nationalinstruments_modularinstruments_niscope_scopedriverutility_lock.htm language=enus -->
## TOPIC 00013: ninetscopefx45ref/html/m_nationalinstruments_modularinstruments_niscope_scopedriverutility_lock.htm

- bundle_id: `ni-scope-dotnet-api-ref`
- source_path: `ninetscopefx45ref/html/m_nationalinstruments_modularinstruments_niscope_scopedriverutility_lock.htm`
- source_url: https://docs-be.ni.com/bundle/ni-scope-dotnet-api-ref/raw/resource/enus/ninetscopefx45ref/html/m_nationalinstruments_modularinstruments_niscope_scopedriverutility_lock.htm
- document_id: `ni-scope-dotnet-api-ref`
- page_type: `leaf`
- content_type: ``

ScopeDriverUtility.Lock Method

ScopeDriverUtilityLock Method

Attempts to acquire a synchronization lock on this instance of the driver.

Namespace:

NationalInstruments.ModularInstruments.NIScope

Assembly:

##### Syntax

C#

VB

```text
public ScopeDriverLock Lock()
```

```text
Public Function Lock As ScopeDriverLock
```

###### Return Value

ScopeDriverLock

##### See Also

###### Reference

ScopeDriverUtility Class

Lock Overload

NationalInstruments.ModularInstruments.NIScope Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=ni-scope-dotnet-api-ref path=ninetscopefx45ref/html/m_nationalinstruments_modularinstruments_niscope_scopedriverutility_querydriverrevision.htm language=enus -->
## TOPIC 00014: ninetscopefx45ref/html/m_nationalinstruments_modularinstruments_niscope_scopedriverutility_querydriverrevision.htm

- bundle_id: `ni-scope-dotnet-api-ref`
- source_path: `ninetscopefx45ref/html/m_nationalinstruments_modularinstruments_niscope_scopedriverutility_querydriverrevision.htm`
- source_url: https://docs-be.ni.com/bundle/ni-scope-dotnet-api-ref/raw/resource/enus/ninetscopefx45ref/html/m_nationalinstruments_modularinstruments_niscope_scopedriverutility_querydriverrevision.htm
- document_id: `ni-scope-dotnet-api-ref`
- page_type: `leaf`
- content_type: ``

ScopeDriverUtility.QueryDriverRevision Method

ScopeDriverUtilityQueryDriverRevision Method

Returns the revision numbers of the NI-SCOPE instrument driver.

Namespace:

NationalInstruments.ModularInstruments.NIScope

Assembly:

##### Syntax

C#

VB

```text
public ScopeRevisionQueryResult QueryDriverRevision()
```

```text
Public Function QueryDriverRevision As ScopeRevisionQueryResult
```

###### Return Value

ScopeRevisionQueryResult

ScopeRevisionQueryResult

##### See Also

###### Reference

ScopeDriverUtility Class

NationalInstruments.ModularInstruments.NIScope Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=ni-scope-dotnet-api-ref path=ninetscopefx45ref/html/m_nationalinstruments_modularinstruments_niscope_scopedriverutility_reset.htm language=enus -->
## TOPIC 00015: ninetscopefx45ref/html/m_nationalinstruments_modularinstruments_niscope_scopedriverutility_reset.htm

- bundle_id: `ni-scope-dotnet-api-ref`
- source_path: `ninetscopefx45ref/html/m_nationalinstruments_modularinstruments_niscope_scopedriverutility_reset.htm`
- source_url: https://docs-be.ni.com/bundle/ni-scope-dotnet-api-ref/raw/resource/enus/ninetscopefx45ref/html/m_nationalinstruments_modularinstruments_niscope_scopedriverutility_reset.htm
- document_id: `ni-scope-dotnet-api-ref`
- page_type: `leaf`
- content_type: ``

ScopeDriverUtility.Reset Method

ScopeDriverUtilityReset Method

Resets all properties to their default value and stops export of all external signals and events.

Namespace:

NationalInstruments.ModularInstruments.NIScope

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

##### See Also

###### Reference

ScopeDriverUtility Class

NationalInstruments.ModularInstruments.NIScope Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=ni-scope-dotnet-api-ref path=ninetscopefx45ref/html/m_nationalinstruments_modularinstruments_niscope_scopeedgetrigger_configure.htm language=enus -->
## TOPIC 00016: ninetscopefx45ref/html/m_nationalinstruments_modularinstruments_niscope_scopeedgetrigger_configure.htm

- bundle_id: `ni-scope-dotnet-api-ref`
- source_path: `ninetscopefx45ref/html/m_nationalinstruments_modularinstruments_niscope_scopeedgetrigger_configure.htm`
- source_url: https://docs-be.ni.com/bundle/ni-scope-dotnet-api-ref/raw/resource/enus/ninetscopefx45ref/html/m_nationalinstruments_modularinstruments_niscope_scopeedgetrigger_configure.htm
- document_id: `ni-scope-dotnet-api-ref`
- page_type: `leaf`
- content_type: ``

ScopeEdgeTrigger.Configure Method

ScopeEdgeTriggerConfigure Method

Configures common properties for analog edge triggering.

Namespace:

NationalInstruments.ModularInstruments.NIScope

Assembly:

##### Syntax

C#

VB

```text
public void Configure(
	ScopeTriggerSource triggerSource,
	double triggerLevel,
	ScopeTriggerSlope triggerSlope,
	ScopeTriggerCoupling triggerCoupling,
	PrecisionTimeSpan triggerHoldoff,
	PrecisionTimeSpan triggerDelay
)
```

```text
Public Sub Configure ( 
	triggerSource As ScopeTriggerSource,
	triggerLevel As Double,
	triggerSlope As ScopeTriggerSlope,
	triggerCoupling As ScopeTriggerCoupling,
	triggerHoldoff As PrecisionTimeSpan,
	triggerDelay As PrecisionTimeSpan
)
```

###### Parameters

- **triggerSource**
  - Type: NationalInstruments.ModularInstruments.NIScopeScopeTriggerSource The trigger source. Refer to ScopeTriggerSource for defined values.
- **triggerLevel**
  - Type: SystemDouble The voltage threshold for the trigger. Refer to Level for more information.
- **triggerSlope**
  - Type: NationalInstruments.ModularInstruments.NIScopeScopeTriggerSlope A value indicating whether you want a rising edge or a falling edge to trigger the digitizer. Refer to ScopeTriggerSlopefor defined values.
- **triggerCoupling**
  - Type: NationalInstruments.ModularInstruments.NIScopeScopeTriggerCoupling Applies coupling and filtering options to the trigger signal. Refer to ScopeTriggerCoupling for defined values.
- **triggerHoldoff**
  - Type: NationalInstrumentsPrecisionTimeSpan The length of time the digitizer waits after detecting a trigger before enabling NI-SCOPE to detect another trigger. Refer to Holdoff for more information.
- **triggerDelay**
  - Type: NationalInstrumentsPrecisionTimeSpan The length of time the digitizer waits after receiving the trigger to start acquiring data. Refer to Delay for more information.

##### See Also

###### Reference

ScopeEdgeTrigger Class

NationalInstruments.ModularInstruments.NIScope Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=ni-scope-dotnet-api-ref path=ninetscopefx45ref/html/m_nationalinstruments_modularinstruments_niscope_scopeendofacquisitioneventoutputterminal_fromstring.htm language=enus -->
## TOPIC 00017: ninetscopefx45ref/html/m_nationalinstruments_modularinstruments_niscope_scopeendofacquisitioneventoutputterminal_fromstring.htm

- bundle_id: `ni-scope-dotnet-api-ref`
- source_path: `ninetscopefx45ref/html/m_nationalinstruments_modularinstruments_niscope_scopeendofacquisitioneventoutputterminal_fromstring.htm`
- source_url: https://docs-be.ni.com/bundle/ni-scope-dotnet-api-ref/raw/resource/enus/ninetscopefx45ref/html/m_nationalinstruments_modularinstruments_niscope_scopeendofacquisitioneventoutputterminal_fromstring.htm
- document_id: `ni-scope-dotnet-api-ref`
- page_type: `leaf`
- content_type: ``

ScopeEndOfAcquisitionEventOutputTerminal.FromString Method

ScopeEndOfAcquisitionEventOutputTerminalFromString Method

ScopeEndOfAcquisitionEventOutputTerminal

String

Namespace:

NationalInstruments.ModularInstruments.NIScope

Assembly:

##### Syntax

C#

VB

```text
public static ScopeEndOfAcquisitionEventOutputTerminal FromString(
	string source
)
```

```text
Public Shared Function FromString ( 
	source As String
) As ScopeEndOfAcquisitionEventOutputTerminal
```

###### Parameters

- **source**
  - Type: SystemString Specifies the String that the ScopeEndOfAcquisitionEventOutputTerminal object returned represents.

###### Return Value

ScopeEndOfAcquisitionEventOutputTerminal

ScopeEndOfAcquisitionEventOutputTerminal

String

##### See Also

###### Reference

ScopeEndOfAcquisitionEventOutputTerminal Class

NationalInstruments.ModularInstruments.NIScope Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=ni-scope-dotnet-api-ref path=ninetscopefx45ref/html/m_nationalinstruments_modularinstruments_niscope_scopeendofacquisitioneventoutputterminal_op_equality.htm language=enus -->
## TOPIC 00018: ninetscopefx45ref/html/m_nationalinstruments_modularinstruments_niscope_scopeendofacquisitioneventoutputterminal_op_equality.htm

- bundle_id: `ni-scope-dotnet-api-ref`
- source_path: `ninetscopefx45ref/html/m_nationalinstruments_modularinstruments_niscope_scopeendofacquisitioneventoutputterminal_op_equality.htm`
- source_url: https://docs-be.ni.com/bundle/ni-scope-dotnet-api-ref/raw/resource/enus/ninetscopefx45ref/html/m_nationalinstruments_modularinstruments_niscope_scopeendofacquisitioneventoutputterminal_op_equality.htm
- document_id: `ni-scope-dotnet-api-ref`
- page_type: `leaf`
- content_type: ``

ScopeEndOfAcquisitionEventOutputTerminal.Equality Operator

ScopeEndOfAcquisitionEventOutputTerminalEquality Operator

ScopeEndOfAcquisitionEventOutputTerminal

Namespace:

NationalInstruments.ModularInstruments.NIScope

Assembly:

##### Syntax

C#

VB

```text
public static bool operator ==(
	ScopeEndOfAcquisitionEventOutputTerminal source1,
	ScopeEndOfAcquisitionEventOutputTerminal source2
)
```

```text
Public Shared Operator = ( 
	source1 As ScopeEndOfAcquisitionEventOutputTerminal,
	source2 As ScopeEndOfAcquisitionEventOutputTerminal
) As Boolean
```

###### Parameters

- **source1**
  - Type: NationalInstruments.ModularInstruments.NIScopeScopeEndOfAcquisitionEventOutputTerminal Specifies the first ScopeEndOfAcquisitionEventOutputTerminal object to compare.
- **source2**
  - Type: NationalInstruments.ModularInstruments.NIScopeScopeEndOfAcquisitionEventOutputTerminal Specifies the second ScopeEndOfAcquisitionEventOutputTerminal object to compare.

###### Return Value

Boolean

##### See Also

###### Reference

ScopeEndOfAcquisitionEventOutputTerminal Class

NationalInstruments.ModularInstruments.NIScope Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=ni-scope-dotnet-api-ref path=ninetscopefx45ref/html/m_nationalinstruments_modularinstruments_niscope_scopeendofrecordeventoutputterminal_equals.1.htm language=enus -->
## TOPIC 00019: ninetscopefx45ref/html/m_nationalinstruments_modularinstruments_niscope_scopeendofrecordeventoutputterminal_equals.1.htm

- bundle_id: `ni-scope-dotnet-api-ref`
- source_path: `ninetscopefx45ref/html/m_nationalinstruments_modularinstruments_niscope_scopeendofrecordeventoutputterminal_equals.1.htm`
- source_url: https://docs-be.ni.com/bundle/ni-scope-dotnet-api-ref/raw/resource/enus/ninetscopefx45ref/html/m_nationalinstruments_modularinstruments_niscope_scopeendofrecordeventoutputterminal_equals.1.htm
- document_id: `ni-scope-dotnet-api-ref`
- page_type: `leaf`
- content_type: ``

ScopeEndOfRecordEventOutputTerminal.Equals Method (Object)

ScopeEndOfRecordEventOutputTerminalEquals Method (Object)

ScopeEndOfRecordEventOutputTerminal

Namespace:

NationalInstruments.ModularInstruments.NIScope

Assembly:

##### Syntax

C#

VB

```text
public override bool Equals(
	Object obj
)
```

```text
Public Overrides Function Equals ( 
	obj As Object
) As Boolean
```

###### Parameters

- **obj**
  - Type: SystemObject Specifies the object to compare to the current instance of ScopeEndOfRecordEventOutputTerminal.

###### Return Value

Boolean

##### See Also

###### Reference

ScopeEndOfRecordEventOutputTerminal Class

Equals Overload

NationalInstruments.ModularInstruments.NIScope Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=ni-scope-dotnet-api-ref path=ninetscopefx45ref/html/m_nationalinstruments_modularinstruments_niscope_scopeendofrecordeventoutputterminal_equals.htm language=enus -->
## TOPIC 00020: ninetscopefx45ref/html/m_nationalinstruments_modularinstruments_niscope_scopeendofrecordeventoutputterminal_equals.htm

- bundle_id: `ni-scope-dotnet-api-ref`
- source_path: `ninetscopefx45ref/html/m_nationalinstruments_modularinstruments_niscope_scopeendofrecordeventoutputterminal_equals.htm`
- source_url: https://docs-be.ni.com/bundle/ni-scope-dotnet-api-ref/raw/resource/enus/ninetscopefx45ref/html/m_nationalinstruments_modularinstruments_niscope_scopeendofrecordeventoutputterminal_equals.htm
- document_id: `ni-scope-dotnet-api-ref`
- page_type: `leaf`
- content_type: ``

ScopeEndOfRecordEventOutputTerminal.Equals Method (ScopeEndOfRecordEventOutputTerminal)

ScopeEndOfRecordEventOutputTerminalEquals Method (ScopeEndOfRecordEventOutputTerminal)

ScopeEndOfRecordEventOutputTerminal

ScopeEndOfRecordEventOutputTerminal

Namespace:

NationalInstruments.ModularInstruments.NIScope

Assembly:

##### Syntax

C#

VB

```text
public bool Equals(
	ScopeEndOfRecordEventOutputTerminal source
)
```

```text
Public Function Equals ( 
	source As ScopeEndOfRecordEventOutputTerminal
) As Boolean
```

###### Parameters

- **source**
  - Type: NationalInstruments.ModularInstruments.NIScopeScopeEndOfRecordEventOutputTerminal Specifies the ScopeEndOfRecordEventOutputTerminal object to compare to the current instance of ScopeEndOfRecordEventOutputTerminal.

###### Return Value

Boolean

##### See Also

###### Reference

ScopeEndOfRecordEventOutputTerminal Class

Equals Overload

NationalInstruments.ModularInstruments.NIScope Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=ni-scope-dotnet-api-ref path=ninetscopefx45ref/html/m_nationalinstruments_modularinstruments_niscope_scopetrigger_configuretriggerhysteresis.htm language=enus -->
## TOPIC 00021: ninetscopefx45ref/html/m_nationalinstruments_modularinstruments_niscope_scopetrigger_configuretriggerhysteresis.htm

- bundle_id: `ni-scope-dotnet-api-ref`
- source_path: `ninetscopefx45ref/html/m_nationalinstruments_modularinstruments_niscope_scopetrigger_configuretriggerhysteresis.htm`
- source_url: https://docs-be.ni.com/bundle/ni-scope-dotnet-api-ref/raw/resource/enus/ninetscopefx45ref/html/m_nationalinstruments_modularinstruments_niscope_scopetrigger_configuretriggerhysteresis.htm
- document_id: `ni-scope-dotnet-api-ref`
- page_type: `leaf`
- content_type: ``

ScopeTrigger.ConfigureTriggerHysteresis Method

ScopeTriggerConfigureTriggerHysteresis Method

Configures common properties for analog hysteresis triggering.

Namespace:

NationalInstruments.ModularInstruments.NIScope

Assembly:

##### Syntax

C#

VB

```text
public void ConfigureTriggerHysteresis(
	ScopeTriggerSource triggerSource,
	double triggerLevel,
	double triggerhysteresisSize,
	ScopeTriggerSlope triggerSlope,
	ScopeTriggerCoupling triggerCoupling,
	PrecisionTimeSpan triggerHoldoff,
	PrecisionTimeSpan triggerDelay
)
```

```text
Public Sub ConfigureTriggerHysteresis ( 
	triggerSource As ScopeTriggerSource,
	triggerLevel As Double,
	triggerhysteresisSize As Double,
	triggerSlope As ScopeTriggerSlope,
	triggerCoupling As ScopeTriggerCoupling,
	triggerHoldoff As PrecisionTimeSpan,
	triggerDelay As PrecisionTimeSpan
)
```

###### Parameters

- **triggerSource**
  - Type: NationalInstruments.ModularInstruments.NIScopeScopeTriggerSource The trigger source.
- **triggerLevel**
  - Type: SystemDouble The voltage threshold for the trigger.
- **triggerhysteresisSize**
  - Type: SystemDouble The size of the hysteresis window, in volts, on either side of the Level.
- **triggerSlope**
  - Type: NationalInstruments.ModularInstruments.NIScopeScopeTriggerSlope A value indicating whether you want a rising edge or a falling edge to trigger the digitizer.
- **triggerCoupling**
  - Type: NationalInstruments.ModularInstruments.NIScopeScopeTriggerCoupling A value indicating whether to apply coupling and filtering options to the trigger signal.
- **triggerHoldoff**
  - Type: NationalInstrumentsPrecisionTimeSpan The length of time the digitizer waits after detecting a trigger before enabling NI-SCOPE to detect another trigger.
- **triggerDelay**
  - Type: NationalInstrumentsPrecisionTimeSpan The time duration, in seconds, that the digitizer waits after receiving the trigger to start acquiring data.

##### See Also

###### Reference

ScopeTrigger Class

NationalInstruments.ModularInstruments.NIScope Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=ni-scope-dotnet-api-ref path=ninetscopefx45ref/html/m_nationalinstruments_modularinstruments_niscope_scopetrigger_configuretriggerimmediate.htm language=enus -->
## TOPIC 00022: ninetscopefx45ref/html/m_nationalinstruments_modularinstruments_niscope_scopetrigger_configuretriggerimmediate.htm

- bundle_id: `ni-scope-dotnet-api-ref`
- source_path: `ninetscopefx45ref/html/m_nationalinstruments_modularinstruments_niscope_scopetrigger_configuretriggerimmediate.htm`
- source_url: https://docs-be.ni.com/bundle/ni-scope-dotnet-api-ref/raw/resource/enus/ninetscopefx45ref/html/m_nationalinstruments_modularinstruments_niscope_scopetrigger_configuretriggerimmediate.htm
- document_id: `ni-scope-dotnet-api-ref`
- page_type: `leaf`
- content_type: ``

ScopeTrigger.ConfigureTriggerImmediate Method

ScopeTriggerConfigureTriggerImmediate Method

Configures common properties for immediate triggering. Immediate triggering means the digitizer triggers itself.

Namespace:

NationalInstruments.ModularInstruments.NIScope

Assembly:

##### Syntax

C#

VB

```text
public void ConfigureTriggerImmediate()
```

```text
Public Sub ConfigureTriggerImmediate
```

##### See Also

###### Reference

ScopeTrigger Class

NationalInstruments.ModularInstruments.NIScope Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=ni-scope-dotnet-api-ref path=ninetscopefx45ref/html/m_nationalinstruments_modularinstruments_niscope_scopetriggersource_equals.1.htm language=enus -->
## TOPIC 00023: ninetscopefx45ref/html/m_nationalinstruments_modularinstruments_niscope_scopetriggersource_equals.1.htm

- bundle_id: `ni-scope-dotnet-api-ref`
- source_path: `ninetscopefx45ref/html/m_nationalinstruments_modularinstruments_niscope_scopetriggersource_equals.1.htm`
- source_url: https://docs-be.ni.com/bundle/ni-scope-dotnet-api-ref/raw/resource/enus/ninetscopefx45ref/html/m_nationalinstruments_modularinstruments_niscope_scopetriggersource_equals.1.htm
- document_id: `ni-scope-dotnet-api-ref`
- page_type: `leaf`
- content_type: ``

ScopeTriggerSource.Equals Method (Object)

ScopeTriggerSourceEquals Method (Object)

ScopeTriggerSource

Namespace:

NationalInstruments.ModularInstruments.NIScope

Assembly:

##### Syntax

C#

VB

```text
public override bool Equals(
	Object obj
)
```

```text
Public Overrides Function Equals ( 
	obj As Object
) As Boolean
```

###### Parameters

- **obj**
  - Type: SystemObject Specifies the object to compare to the current instance of ScopeTriggerSource.

###### Return Value

Boolean

##### See Also

###### Reference

ScopeTriggerSource Class

Equals Overload

NationalInstruments.ModularInstruments.NIScope Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=ni-scope-dotnet-api-ref path=ninetscopefx45ref/html/m_nationalinstruments_modularinstruments_niscope_scopetriggersource_equals.htm language=enus -->
## TOPIC 00024: ninetscopefx45ref/html/m_nationalinstruments_modularinstruments_niscope_scopetriggersource_equals.htm

- bundle_id: `ni-scope-dotnet-api-ref`
- source_path: `ninetscopefx45ref/html/m_nationalinstruments_modularinstruments_niscope_scopetriggersource_equals.htm`
- source_url: https://docs-be.ni.com/bundle/ni-scope-dotnet-api-ref/raw/resource/enus/ninetscopefx45ref/html/m_nationalinstruments_modularinstruments_niscope_scopetriggersource_equals.htm
- document_id: `ni-scope-dotnet-api-ref`
- page_type: `leaf`
- content_type: ``

ScopeTriggerSource.Equals Method (ScopeTriggerSource)

ScopeTriggerSourceEquals Method (ScopeTriggerSource)

ScopeTriggerSource

ScopeTriggerSource

Namespace:

NationalInstruments.ModularInstruments.NIScope

Assembly:

##### Syntax

C#

VB

```text
public bool Equals(
	ScopeTriggerSource source
)
```

```text
Public Function Equals ( 
	source As ScopeTriggerSource
) As Boolean
```

###### Parameters

- **source**
  - Type: NationalInstruments.ModularInstruments.NIScopeScopeTriggerSource Specifies the ScopeTriggerSource object to compare to the current instance of ScopeTriggerSource.

###### Return Value

Boolean

##### See Also

###### Reference

ScopeTriggerSource Class

Equals Overload

NationalInstruments.ModularInstruments.NIScope Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=ni-scope-dotnet-api-ref path=ninetscopefx45ref/html/m_nationalinstruments_modularinstruments_niscope_scopewarning_op_inequality.htm language=enus -->
## TOPIC 00025: ninetscopefx45ref/html/m_nationalinstruments_modularinstruments_niscope_scopewarning_op_inequality.htm

- bundle_id: `ni-scope-dotnet-api-ref`
- source_path: `ninetscopefx45ref/html/m_nationalinstruments_modularinstruments_niscope_scopewarning_op_inequality.htm`
- source_url: https://docs-be.ni.com/bundle/ni-scope-dotnet-api-ref/raw/resource/enus/ninetscopefx45ref/html/m_nationalinstruments_modularinstruments_niscope_scopewarning_op_inequality.htm
- document_id: `ni-scope-dotnet-api-ref`
- page_type: `leaf`
- content_type: ``

ScopeWarning.Inequality Operator

ScopeWarningInequality Operator

ScopeWarning

Namespace:

NationalInstruments.ModularInstruments.NIScope

Assembly:

##### Syntax

C#

VB

```text
public static bool operator !=(
	ScopeWarning warning1,
	ScopeWarning warning2
)
```

```text
Public Shared Operator <> ( 
	warning1 As ScopeWarning,
	warning2 As ScopeWarning
) As Boolean
```

###### Parameters

- **warning1**
  - Type: NationalInstruments.ModularInstruments.NIScopeScopeWarning A ScopeWarning object.
- **warning2**
  - Type: NationalInstruments.ModularInstruments.NIScopeScopeWarning A ScopeWarning object.

###### Return Value

Boolean

##### See Also

###### Reference

ScopeWarning Class

NationalInstruments.ModularInstruments.NIScope Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=ni-scope-dotnet-api-ref path=ninetscopefx45ref/html/m_nationalinstruments_modularinstruments_niscope_scopewarning_tostring.htm language=enus -->
## TOPIC 00026: ninetscopefx45ref/html/m_nationalinstruments_modularinstruments_niscope_scopewarning_tostring.htm

- bundle_id: `ni-scope-dotnet-api-ref`
- source_path: `ninetscopefx45ref/html/m_nationalinstruments_modularinstruments_niscope_scopewarning_tostring.htm`
- source_url: https://docs-be.ni.com/bundle/ni-scope-dotnet-api-ref/raw/resource/enus/ninetscopefx45ref/html/m_nationalinstruments_modularinstruments_niscope_scopewarning_tostring.htm
- document_id: `ni-scope-dotnet-api-ref`
- page_type: `leaf`
- content_type: ``

ScopeWarning.ToString Method

ScopeWarningToString Method

ScopeWarning

Namespace:

NationalInstruments.ModularInstruments.NIScope

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

String

ScopeWarning

##### See Also

###### Reference

ScopeWarning Class

NationalInstruments.ModularInstruments.NIScope Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=ni-scope-dotnet-api-ref path=ninetscopefx45ref/html/m_nationalinstruments_modularinstruments_niscope_scopewaveforminfo_equals.htm language=enus -->
## TOPIC 00027: ninetscopefx45ref/html/m_nationalinstruments_modularinstruments_niscope_scopewaveforminfo_equals.htm

- bundle_id: `ni-scope-dotnet-api-ref`
- source_path: `ninetscopefx45ref/html/m_nationalinstruments_modularinstruments_niscope_scopewaveforminfo_equals.htm`
- source_url: https://docs-be.ni.com/bundle/ni-scope-dotnet-api-ref/raw/resource/enus/ninetscopefx45ref/html/m_nationalinstruments_modularinstruments_niscope_scopewaveforminfo_equals.htm
- document_id: `ni-scope-dotnet-api-ref`
- page_type: `leaf`
- content_type: ``

ScopeWaveformInfo.Equals Method (ScopeWaveformInfo)

ScopeWaveformInfoEquals Method (ScopeWaveformInfo)

ScopeWaveformInfo

ScopeWaveformInfo

Namespace:

NationalInstruments.ModularInstruments.NIScope

Assembly:

##### Syntax

C#

VB

```text
public bool Equals(
	ScopeWaveformInfo waveformInfo
)
```

```text
Public Function Equals ( 
	waveformInfo As ScopeWaveformInfo
) As Boolean
```

###### Parameters

- **waveformInfo**
  - Type: NationalInstruments.ModularInstruments.NIScopeScopeWaveformInfoThe ScopeWaveformInfo object to be compared to the current instance of ScopeWaveformInfo.

###### Return Value

Boolean

##### See Also

###### Reference

ScopeWaveformInfo Structure

Equals Overload

NationalInstruments.ModularInstruments.NIScope Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=ni-scope-dotnet-api-ref path=ninetscopefx45ref/html/m_nationalinstruments_modularinstruments_niscope_scopewaveforminfo_op_equality.htm language=enus -->
## TOPIC 00028: ninetscopefx45ref/html/m_nationalinstruments_modularinstruments_niscope_scopewaveforminfo_op_equality.htm

- bundle_id: `ni-scope-dotnet-api-ref`
- source_path: `ninetscopefx45ref/html/m_nationalinstruments_modularinstruments_niscope_scopewaveforminfo_op_equality.htm`
- source_url: https://docs-be.ni.com/bundle/ni-scope-dotnet-api-ref/raw/resource/enus/ninetscopefx45ref/html/m_nationalinstruments_modularinstruments_niscope_scopewaveforminfo_op_equality.htm
- document_id: `ni-scope-dotnet-api-ref`
- page_type: `leaf`
- content_type: ``

ScopeWaveformInfo.Equality Operator

ScopeWaveformInfoEquality Operator

ScopeWaveformInfo

Namespace:

NationalInstruments.ModularInstruments.NIScope

Assembly:

##### Syntax

C#

VB

```text
public static bool operator ==(
	ScopeWaveformInfo waveformInfo1,
	ScopeWaveformInfo waveformInfo2
)
```

```text
Public Shared Operator = ( 
	waveformInfo1 As ScopeWaveformInfo,
	waveformInfo2 As ScopeWaveformInfo
) As Boolean
```

###### Parameters

- **waveformInfo1**
  - Type: NationalInstruments.ModularInstruments.NIScopeScopeWaveformInfoA ScopeWaveformInfo object.
- **waveformInfo2**
  - Type: NationalInstruments.ModularInstruments.NIScopeScopeWaveformInfoA ScopeWaveformInfo object.

###### Return Value

Boolean

##### See Also

###### Reference

ScopeWaveformInfo Structure

NationalInstruments.ModularInstruments.NIScope Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=ni-scope-dotnet-api-ref path=ninetscopefx45ref/html/overload_nationalinstruments_modularinstruments_niscope_scopeadvancetriggersource_equals.htm language=enus -->
## TOPIC 00029: ninetscopefx45ref/html/overload_nationalinstruments_modularinstruments_niscope_scopeadvancetriggersource_equals.htm

- bundle_id: `ni-scope-dotnet-api-ref`
- source_path: `ninetscopefx45ref/html/overload_nationalinstruments_modularinstruments_niscope_scopeadvancetriggersource_equals.htm`
- source_url: https://docs-be.ni.com/bundle/ni-scope-dotnet-api-ref/raw/resource/enus/ninetscopefx45ref/html/overload_nationalinstruments_modularinstruments_niscope_scopeadvancetriggersource_equals.htm
- document_id: `ni-scope-dotnet-api-ref`
- page_type: `leaf`
- content_type: ``

ScopeAdvanceTriggerSource.Equals Method

ScopeAdvanceTriggerSourceEquals Method

##### Overload List

|  | Name | Description |
| --- | --- | --- |
|  | Equals(Object) | Determines whether the current instance of ScopeAdvanceTriggerSource and the specified object are equal. (Overrides ObjectEquals(Object).) |
|  | Equals(ScopeAdvanceTriggerSource) | Determines whether the current instance of ScopeAdvanceTriggerSource and the specified ScopeAdvanceTriggerSource object are equal. |

Top

##### See Also

###### Reference

ScopeAdvanceTriggerSource Class

NationalInstruments.ModularInstruments.NIScope Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=ni-scope-dotnet-api-ref path=ninetscopefx45ref/html/overload_nationalinstruments_modularinstruments_niscope_scopechannelmeasurement_fetcharraymeasurement.htm language=enus -->
## TOPIC 00030: ninetscopefx45ref/html/overload_nationalinstruments_modularinstruments_niscope_scopechannelmeasurement_fetcharraymeasurement.htm

- bundle_id: `ni-scope-dotnet-api-ref`
- source_path: `ninetscopefx45ref/html/overload_nationalinstruments_modularinstruments_niscope_scopechannelmeasurement_fetcharraymeasurement.htm`
- source_url: https://docs-be.ni.com/bundle/ni-scope-dotnet-api-ref/raw/resource/enus/ninetscopefx45ref/html/overload_nationalinstruments_modularinstruments_niscope_scopechannelmeasurement_fetcharraymeasurement.htm
- document_id: `ni-scope-dotnet-api-ref`
- page_type: `leaf`
- content_type: ``

ScopeChannelMeasurement.FetchArrayMeasurement Method

ScopeChannelMeasurementFetchArrayMeasurement Method

##### Overload List

|  | Name | Description |
| --- | --- | --- |
|  | FetchArrayMeasurement(PrecisionTimeSpan, ScopeArrayMeasurementType, AnalogWaveformCollectionDouble) | Obtains a waveform from the digitizer and returns the specified measurement array. This method may return multiple waveforms depending on the number of channels, the acquisition type, and the number of records you specify. |
|  | FetchArrayMeasurement(PrecisionTimeSpan, ScopeArrayMeasurementType, AnalogWaveformCollectionDouble, ScopeWaveformInfo) | Obtains a waveform from the digitizer and returns the specified measurement array. This method may return multiple waveforms depending on the number of channels, the acquisition type, and the number of records you specify. |

Top

##### See Also

###### Reference

ScopeChannelMeasurement Class

NationalInstruments.ModularInstruments.NIScope Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=ni-scope-dotnet-api-ref path=ninetscopefx45ref/html/overload_nationalinstruments_modularinstruments_niscope_scopecoefficientinfo_equals.htm language=enus -->
## TOPIC 00031: ninetscopefx45ref/html/overload_nationalinstruments_modularinstruments_niscope_scopecoefficientinfo_equals.htm

- bundle_id: `ni-scope-dotnet-api-ref`
- source_path: `ninetscopefx45ref/html/overload_nationalinstruments_modularinstruments_niscope_scopecoefficientinfo_equals.htm`
- source_url: https://docs-be.ni.com/bundle/ni-scope-dotnet-api-ref/raw/resource/enus/ninetscopefx45ref/html/overload_nationalinstruments_modularinstruments_niscope_scopecoefficientinfo_equals.htm
- document_id: `ni-scope-dotnet-api-ref`
- page_type: `leaf`
- content_type: ``

ScopeCoefficientInfo.Equals Method

ScopeCoefficientInfoEquals Method

##### Overload List

|  | Name | Description |
| --- | --- | --- |
|  | Equals(Object) | Determines if the current instance of ScopeCoefficientInfo and the object that you specify are equal. (Overrides ValueTypeEquals(Object).) |
|  | Equals(ScopeCoefficientInfo) | Determines whether the current instance of ScopeCoefficientInfo and the ScopeCoefficientInfo object that you specify are equal. |

Top

##### See Also

###### Reference

ScopeCoefficientInfo Structure

NationalInstruments.ModularInstruments.NIScope Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=ni-scope-dotnet-api-ref path=ninetscopefx45ref/html/overload_nationalinstruments_modularinstruments_niscope_scopeerrorqueryresult_equals.htm language=enus -->
## TOPIC 00032: ninetscopefx45ref/html/overload_nationalinstruments_modularinstruments_niscope_scopeerrorqueryresult_equals.htm

- bundle_id: `ni-scope-dotnet-api-ref`
- source_path: `ninetscopefx45ref/html/overload_nationalinstruments_modularinstruments_niscope_scopeerrorqueryresult_equals.htm`
- source_url: https://docs-be.ni.com/bundle/ni-scope-dotnet-api-ref/raw/resource/enus/ninetscopefx45ref/html/overload_nationalinstruments_modularinstruments_niscope_scopeerrorqueryresult_equals.htm
- document_id: `ni-scope-dotnet-api-ref`
- page_type: `leaf`
- content_type: ``

ScopeErrorQueryResult.Equals Method

ScopeErrorQueryResultEquals Method

##### Overload List

|  | Name | Description |
| --- | --- | --- |
|  | Equals(Object) | Determines whether the current instance of ScopeErrorQueryResult and the object that you specify are equal. (Overrides ValueTypeEquals(Object).) |
|  | Equals(ScopeErrorQueryResult) | Determines whether the current instance of ScopeErrorQueryResult and the ScopeErrorQueryResult object that you specify are equal. |

Top

##### See Also

###### Reference

ScopeErrorQueryResult Structure

NationalInstruments.ModularInstruments.NIScope Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=ni-scope-dotnet-api-ref path=ninetscopefx45ref/html/overload_nationalinstruments_modularinstruments_niscope_scopeinputclocksource_equals.htm language=enus -->
## TOPIC 00033: ninetscopefx45ref/html/overload_nationalinstruments_modularinstruments_niscope_scopeinputclocksource_equals.htm

- bundle_id: `ni-scope-dotnet-api-ref`
- source_path: `ninetscopefx45ref/html/overload_nationalinstruments_modularinstruments_niscope_scopeinputclocksource_equals.htm`
- source_url: https://docs-be.ni.com/bundle/ni-scope-dotnet-api-ref/raw/resource/enus/ninetscopefx45ref/html/overload_nationalinstruments_modularinstruments_niscope_scopeinputclocksource_equals.htm
- document_id: `ni-scope-dotnet-api-ref`
- page_type: `leaf`
- content_type: ``

ScopeInputClockSource.Equals Method

ScopeInputClockSourceEquals Method

##### Overload List

|  | Name | Description |
| --- | --- | --- |
|  | Equals(Object) | Determines whether the current instance of ScopeInputClockSource and the specified object are equal. (Overrides ObjectEquals(Object).) |
|  | Equals(ScopeInputClockSource) | Determines whether the current instance of ScopeInputClockSource and the specified ScopeInputClockSource object are equal. |

Top

##### See Also

###### Reference

ScopeInputClockSource Class

NationalInstruments.ModularInstruments.NIScope Namespace

Copyright © National Instruments Corporation. All Rights Reserved.
