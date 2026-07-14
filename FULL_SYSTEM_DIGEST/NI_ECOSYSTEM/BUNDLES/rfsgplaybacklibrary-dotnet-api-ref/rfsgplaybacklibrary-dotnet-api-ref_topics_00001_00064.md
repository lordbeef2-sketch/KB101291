# NI DOCUMENT BUNDLE: rfsgplaybacklibrary-dotnet-api-ref

<!--NI_BUNDLE_CHUNK bundle=rfsgplaybacklibrary-dotnet-api-ref start=1 end=64 -->
<!--NI_TOPIC bundle=rfsgplaybacklibrary-dotnet-api-ref path=nationalinstruments-modularinstruments-nirfsgplayback-nirfsgplayback-clearallwaveforms__intptr.html language=enus -->
## TOPIC 00001: ClearAllWaveforms(IntPtr)

- bundle_id: `rfsgplaybacklibrary-dotnet-api-ref`
- source_path: `nationalinstruments-modularinstruments-nirfsgplayback-nirfsgplayback-clearallwaveforms__intptr.html`
- source_url: https://docs-be.ni.com/bundle/rfsgplaybacklibrary-dotnet-api-ref/raw/resource/enus/nationalinstruments-modularinstruments-nirfsgplayback-nirfsgplayback-clearallwaveforms__intptr.html
- document_id: `rfsgplaybacklibrary-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Deletes the waveforms from the NI-RFSG device memory and removes all the waveform properties from the NI-RFSG waveform properties database for the specified device. SyntaxNamespace: NationalInstruments.ModularInstruments.NIRfsgPlaybackpublic static int ClearAllWaveforms(IntPtr rfsgSession)Parameters

### ClearAllWaveforms(IntPtr)

Deletes the waveforms from the NI-RFSG device memory and removes all the waveform properties from the NI-RFSG waveform properties database for the specified device.

#### Syntax

**Namespace:**[NationalInstruments.ModularInstruments.NIRfsgPlayback](nationalinstruments-modularinstruments-nirfsgplayback.html)

public static int ClearAllWaveforms(IntPtr rfsgSession)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| rfsgSession | IntPtr | Identifies the instrument session. The rfsgSession handle is obtained from the NIRfsg.DangerousGetInstrumentHandle method. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

NIRfsgPlayback Class

<!--NI_TOPIC bundle=rfsgplaybacklibrary-dotnet-api-ref path=nationalinstruments-modularinstruments-nirfsgplayback-nirfsgplayback-clearwaveform__intptr-string.html language=enus -->
## TOPIC 00002: ClearWaveform(IntPtr, string)

- bundle_id: `rfsgplaybacklibrary-dotnet-api-ref`
- source_path: `nationalinstruments-modularinstruments-nirfsgplayback-nirfsgplayback-clearwaveform__intptr-string.html`
- source_url: https://docs-be.ni.com/bundle/rfsgplaybacklibrary-dotnet-api-ref/raw/resource/enus/nationalinstruments-modularinstruments-nirfsgplayback-nirfsgplayback-clearwaveform__intptr-string.html
- document_id: `rfsgplaybacklibrary-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Deletes the waveform from the NI-RFSG device memory and removes the waveform properties from the NI-RFSG waveform properties database for the specified device. SyntaxNamespace: NationalInstruments.ModularInstruments.NIRfsgPlaybackpublic static int ClearWaveform(IntPtr rfsgSession, string waveformNam

### ClearWaveform(IntPtr, string)

Deletes the waveform from the NI-RFSG device memory and removes the waveform properties from the NI-RFSG waveform properties database for the specified device.

#### Syntax

**Namespace:**[NationalInstruments.ModularInstruments.NIRfsgPlayback](nationalinstruments-modularinstruments-nirfsgplayback.html)

public static int ClearWaveform(IntPtr rfsgSession, string waveformName)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| rfsgSession | IntPtr | Identifies the instrument session. The rfsgSession handle is obtained from the NIRfsg.DangerousGetInstrumentHandle method. |
| waveformName | string | Specifies the name of the waveform that has to be deleted from the database. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

NIRfsgPlayback Class

<!--NI_TOPIC bundle=rfsgplaybacklibrary-dotnet-api-ref path=nationalinstruments-modularinstruments-nirfsgplayback-nirfsgplayback-downloaduserwaveform__intptr-string-complexwaveform_complexdouble_-bool.html language=enus -->
## TOPIC 00003: DownloadUserWaveform(IntPtr, string, ComplexWaveform< ComplexDouble >, bool)

- bundle_id: `rfsgplaybacklibrary-dotnet-api-ref`
- source_path: `nationalinstruments-modularinstruments-nirfsgplayback-nirfsgplayback-downloaduserwaveform__intptr-string-complexwaveform_complexdouble_-bool.html`
- source_url: https://docs-be.ni.com/bundle/rfsgplaybacklibrary-dotnet-api-ref/raw/resource/enus/nationalinstruments-modularinstruments-nirfsgplayback-nirfsgplayback-downloaduserwaveform__intptr-string-complexwaveform_complexdouble_-bool.html
- document_id: `rfsgplaybacklibrary-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Normalizes the input waveform and writes it into the NI RF vector signal generator. This VI computes the peak to average power ratio (PAPR) using the bursts in the waveform, stores the PAPR, sample rate, waveform size, and runtime scaling value of -1.5 dB in the NI-RFSG waveform database. SyntaxName

### DownloadUserWaveform(IntPtr, string, ComplexWaveform< ComplexDouble >, bool)

Normalizes the input waveform and writes it into the NI RF vector signal generator. This VI computes the peak to average power ratio (PAPR) using the bursts in the waveform, stores the PAPR, sample rate, waveform size, and runtime scaling value of -1.5 dB in the NI-RFSG waveform database.

#### Syntax

**Namespace:**[NationalInstruments.ModularInstruments.NIRfsgPlayback](nationalinstruments-modularinstruments-nirfsgplayback.html)

public static int DownloadUserWaveform(IntPtr rfsgSession, string waveformName, ComplexWaveform< ComplexDouble > waveform, bool burstPresent)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| rfsgSession | IntPtr | Identifies the instrument session. The rfsgSession handle is obtained from the NIRfsg.DangerousGetInstrumentHandle method. |
| waveformName | string | Specifies the waveform name used to write the waveform to the NI-RFSG device memory. |
| waveform | ComplexWaveform< ComplexDouble > | Specifies an array of the complex double waveform clusters which has to be downloaded to the device. |
| burstPresent | bool | specifies whether the burst is present in the given waveform. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

NIRfsgPlayback Class

<!--NI_TOPIC bundle=rfsgplaybacklibrary-dotnet-api-ref path=nationalinstruments-modularinstruments-nirfsgplayback-nirfsgplayback-downloaduserwaveform__intptr-string-complexwaveform_complexsingle_-bool.html language=enus -->
## TOPIC 00004: DownloadUserWaveform(IntPtr, string, ComplexWaveform< ComplexSingle >, bool)

- bundle_id: `rfsgplaybacklibrary-dotnet-api-ref`
- source_path: `nationalinstruments-modularinstruments-nirfsgplayback-nirfsgplayback-downloaduserwaveform__intptr-string-complexwaveform_complexsingle_-bool.html`
- source_url: https://docs-be.ni.com/bundle/rfsgplaybacklibrary-dotnet-api-ref/raw/resource/enus/nationalinstruments-modularinstruments-nirfsgplayback-nirfsgplayback-downloaduserwaveform__intptr-string-complexwaveform_complexsingle_-bool.html
- document_id: `rfsgplaybacklibrary-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Normalizes the input waveform and writes it into the NI RF vector signal generator. This VI computes the peak to average power ratio (PAPR) using the bursts in the waveform, stores the PAPR, sample rate, waveform size, and runtime scaling value of -1.5 dB in the NI-RFSG waveform database. SyntaxName

### DownloadUserWaveform(IntPtr, string, ComplexWaveform< ComplexSingle >, bool)

Normalizes the input waveform and writes it into the NI RF vector signal generator. This VI computes the peak to average power ratio (PAPR) using the bursts in the waveform, stores the PAPR, sample rate, waveform size, and runtime scaling value of -1.5 dB in the NI-RFSG waveform database.

#### Syntax

**Namespace:**[NationalInstruments.ModularInstruments.NIRfsgPlayback](nationalinstruments-modularinstruments-nirfsgplayback.html)

public static int DownloadUserWaveform(IntPtr rfsgSession, string waveformName, ComplexWaveform< ComplexSingle > waveform, bool burstPresent)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| rfsgSession | IntPtr | Identifies the instrument session. The rfsgSession handle is obtained from the NIRfsg.DangerousGetInstrumentHandle method. |
| waveformName | string | Specifies the waveform name used to store the waveform in the NI-RFSG device memory and waveform properties in the NI-RFSG database. |
| waveform | ComplexWaveform< ComplexSingle > | Specifies an array of the complex single waveform clusters which has to be downloaded to the device. |
| burstPresent | bool | Specifies whether the burst is present in the given waveform. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

NIRfsgPlayback Class

<!--NI_TOPIC bundle=rfsgplaybacklibrary-dotnet-api-ref path=nationalinstruments-modularinstruments-nirfsgplayback-nirfsgplayback-geterror__out-out.html language=enus -->
## TOPIC 00005: GetError(out int, out string)

- bundle_id: `rfsgplaybacklibrary-dotnet-api-ref`
- source_path: `nationalinstruments-modularinstruments-nirfsgplayback-nirfsgplayback-geterror__out-out.html`
- source_url: https://docs-be.ni.com/bundle/rfsgplaybacklibrary-dotnet-api-ref/raw/resource/enus/nationalinstruments-modularinstruments-nirfsgplayback-nirfsgplayback-geterror__out-out.html
- document_id: `rfsgplaybacklibrary-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the latest error code and description. SyntaxNamespace: NationalInstruments.ModularInstruments.NIRfsgPlaybackpublic static int GetError(out int errorCode, out string errorDescription)ParametersNameTypeDescriptionerrorCodeout intUpon return, contains the latest error code.errorDescriptionout str

### GetError(out int, out string)

Gets the latest error code and description.

#### Syntax

**Namespace:**[NationalInstruments.ModularInstruments.NIRfsgPlayback](nationalinstruments-modularinstruments-nirfsgplayback.html)

public static int GetError(out int errorCode, out string errorDescription)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| errorCode | out int | Upon return, contains the latest error code. |
| errorDescription | out string | Upon return, contains the latest error description. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes an error or warning condition.

Parent topic:

NIRfsgPlayback Class

<!--NI_TOPIC bundle=rfsgplaybacklibrary-dotnet-api-ref path=nationalinstruments-modularinstruments-nirfsgplayback-nirfsgplayback-readanddownloadwaveformfromfile__intptr-string-string.html language=enus -->
## TOPIC 00006: ReadAndDownloadWaveformFromFile(IntPtr, string, string)

- bundle_id: `rfsgplaybacklibrary-dotnet-api-ref`
- source_path: `nationalinstruments-modularinstruments-nirfsgplayback-nirfsgplayback-readanddownloadwaveformfromfile__intptr-string-string.html`
- source_url: https://docs-be.ni.com/bundle/rfsgplaybacklibrary-dotnet-api-ref/raw/resource/enus/nationalinstruments-modularinstruments-nirfsgplayback-nirfsgplayback-readanddownloadwaveformfromfile__intptr-string-string.html
- document_id: `rfsgplaybacklibrary-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Reads a waveform from a TDMS file, and downloads it to the NI RF vector signal generator. SyntaxNamespace: NationalInstruments.ModularInstruments.NIRfsgPlaybackpublic static int ReadAndDownloadWaveformFromFile(IntPtr rfsgSession, string filePath, string rfsgWaveformName)RemarksThis method reads the

### ReadAndDownloadWaveformFromFile(IntPtr, string, string)

Reads a waveform from a TDMS file, and downloads it to the NI RF vector signal generator.

#### Syntax

**Namespace:**[NationalInstruments.ModularInstruments.NIRfsgPlayback](nationalinstruments-modularinstruments-nirfsgplayback.html)

public static int ReadAndDownloadWaveformFromFile(IntPtr rfsgSession, string filePath, string rfsgWaveformName)

#### Remarks

- Sample Rate
- PAPR and Runtime Scaling, or Peak Power Adjustment
- RF Blanking Marker Locations
- RF Blanking Enabled
- Burst Start Locations
- Burst Stop Locations
- RF Blanking Marker Source
- Signal Bandwidth
- Waveform Size

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| rfsgSession | IntPtr | Identifies the instrument session. The rfsgSession handle is obtained from the NIRfsg.DangerousGetInstrumentHandle method. |
| filePath | string | Specifies the absolute path to the TDMS file from which the playback library reads the waveforms. |
| rfsgWaveformName | string | Specifies the waveform name used to store the waveform in the NI-RFSG device memory and waveform properties in the NI-RFSG waveform database. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

NIRfsgPlayback Class

<!--NI_TOPIC bundle=rfsgplaybacklibrary-dotnet-api-ref path=nationalinstruments-modularinstruments-nirfsgplayback-nirfsgplayback-readanddownloadwaveformsfromfile__intptr_arr1-string-string.html language=enus -->
## TOPIC 00007: ReadAndDownloadWaveformsFromFile(IntPtr[], string, string)

- bundle_id: `rfsgplaybacklibrary-dotnet-api-ref`
- source_path: `nationalinstruments-modularinstruments-nirfsgplayback-nirfsgplayback-readanddownloadwaveformsfromfile__intptr_arr1-string-string.html`
- source_url: https://docs-be.ni.com/bundle/rfsgplaybacklibrary-dotnet-api-ref/raw/resource/enus/nationalinstruments-modularinstruments-nirfsgplayback-nirfsgplayback-readanddownloadwaveformsfromfile__intptr_arr1-string-string.html
- document_id: `rfsgplaybacklibrary-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Reads the waveforms from a TDMS file, and downloads one waveform into each of the NI RF vector signal generators. The first waveform in the TDMS file is downloaded to the first NI RF vector signal generator and so on, until all the waveforms are downloaded. SyntaxNamespace: NationalInstruments.Modul

### ReadAndDownloadWaveformsFromFile(IntPtr[], string, string)

Reads the waveforms from a TDMS file, and downloads one waveform into each of the NI RF vector signal generators. The first waveform in the TDMS file is downloaded to the first NI RF vector signal generator and so on, until all the waveforms are downloaded.

#### Syntax

**Namespace:**[NationalInstruments.ModularInstruments.NIRfsgPlayback](nationalinstruments-modularinstruments-nirfsgplayback.html)

public static int ReadAndDownloadWaveformsFromFile(IntPtr[] rfsgSessions, string filePath, string rfsgWaveformName)

#### Remarks

- Sample Rate
- PAPR and Runtime Scaling, or Peak Power Adjustment
- RF Blanking Marker Locations
- RF Blanking Enabled
- Burst Start Locations
- Burst Stop Locations
- RF Blanking Marker Source
- Signal Bandwidth
- Waveform Size

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| rfsgSessions | IntPtr[] | Identifies instruments for multiple RFSG sessions. The rfsgSession handle is obtained from the NIRfsg.DangerousGetInstrumentHandle method. |
| filePath | string | Specifies the absolute path to the TDMS file from which the playback library reads the waveforms. |
| rfsgWaveformName | string | Specifies the waveform name used to store the waveform in the NI-RFSG device memory and waveform properties in the NI-RFSG waveform database. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

NIRfsgPlayback Class

<!--NI_TOPIC bundle=rfsgplaybacklibrary-dotnet-api-ref path=nationalinstruments-modularinstruments-nirfsgplayback-nirfsgplayback-readburststartlocationsfromfile__string-int-ref.html language=enus -->
## TOPIC 00008: ReadBurstStartLocationsFromFile(string, int, ref int[])

- bundle_id: `rfsgplaybacklibrary-dotnet-api-ref`
- source_path: `nationalinstruments-modularinstruments-nirfsgplayback-nirfsgplayback-readburststartlocationsfromfile__string-int-ref.html`
- source_url: https://docs-be.ni.com/bundle/rfsgplaybacklibrary-dotnet-api-ref/raw/resource/enus/nationalinstruments-modularinstruments-nirfsgplayback-nirfsgplayback-readburststartlocationsfromfile__string-int-ref.html
- document_id: `rfsgplaybacklibrary-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the RF burst start locations stored in the file. This method uses the waveformIndex as the key to read the waveform property. SyntaxNamespace: NationalInstruments.ModularInstruments.NIRfsgPlaybackpublic static int ReadBurstStartLocationsFromFile(string filePath, int waveformIndex, ref int[]

### ReadBurstStartLocationsFromFile(string, int, ref int[])

Returns the RF burst start locations stored in the file. This method uses the *waveformIndex* as the key to read the waveform property.

#### Syntax

**Namespace:**[NationalInstruments.ModularInstruments.NIRfsgPlayback](nationalinstruments-modularinstruments-nirfsgplayback.html)

public static int ReadBurstStartLocationsFromFile(string filePath, int waveformIndex, ref int[] burstStartLocations)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| filePath | string | Specifies the absolute path to the TDMS file from which the playback library reads the waveforms. |
| waveformIndex | int | Specifies the waveform number in the file for which you want to read the burst start locations. |
| burstStartLocations | ref int[] | Returns an array of the burst start locations, stored in the file for the waveform number which you specified in the waveformIndex parameter. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

NIRfsgPlayback Class

<!--NI_TOPIC bundle=rfsgplaybacklibrary-dotnet-api-ref path=nationalinstruments-modularinstruments-nirfsgplayback-nirfsgplayback-readburststoplocationsfromfile__string-int-ref.html language=enus -->
## TOPIC 00009: ReadBurstStopLocationsFromFile(string, int, ref int[])

- bundle_id: `rfsgplaybacklibrary-dotnet-api-ref`
- source_path: `nationalinstruments-modularinstruments-nirfsgplayback-nirfsgplayback-readburststoplocationsfromfile__string-int-ref.html`
- source_url: https://docs-be.ni.com/bundle/rfsgplaybacklibrary-dotnet-api-ref/raw/resource/enus/nationalinstruments-modularinstruments-nirfsgplayback-nirfsgplayback-readburststoplocationsfromfile__string-int-ref.html
- document_id: `rfsgplaybacklibrary-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the RF burst stop locations stored in the file. This method uses the waveformIndex as the key to read the waveform property. SyntaxNamespace: NationalInstruments.ModularInstruments.NIRfsgPlaybackpublic static int ReadBurstStopLocationsFromFile(string filePath, int waveformIndex, ref int[] bu

### ReadBurstStopLocationsFromFile(string, int, ref int[])

Returns the RF burst stop locations stored in the file. This method uses the *waveformIndex* as the key to read the waveform property.

#### Syntax

**Namespace:**[NationalInstruments.ModularInstruments.NIRfsgPlayback](nationalinstruments-modularinstruments-nirfsgplayback.html)

public static int ReadBurstStopLocationsFromFile(string filePath, int waveformIndex, ref int[] burstStopLocations)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| filePath | string | Specifies the absolute path to the TDMS file from which the playback library reads the waveform. |
| waveformIndex | int | Specifies the waveform number in the file for which you want to read the burst stop locations. |
| burstStopLocations | ref int[] | Returns an array of the burst stop locations, stored in the file for the waveform number which you specified in the waveformIndex parameter. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

NIRfsgPlayback Class

<!--NI_TOPIC bundle=rfsgplaybacklibrary-dotnet-api-ref path=nationalinstruments-modularinstruments-nirfsgplayback-nirfsgplayback-readpaprfromfile__string-int-out.html language=enus -->
## TOPIC 00010: ReadPaprFromFile(string, int, out double)

- bundle_id: `rfsgplaybacklibrary-dotnet-api-ref`
- source_path: `nationalinstruments-modularinstruments-nirfsgplayback-nirfsgplayback-readpaprfromfile__string-int-out.html`
- source_url: https://docs-be.ni.com/bundle/rfsgplaybacklibrary-dotnet-api-ref/raw/resource/enus/nationalinstruments-modularinstruments-nirfsgplayback-nirfsgplayback-readpaprfromfile__string-int-out.html
- document_id: `rfsgplaybacklibrary-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the peak to average power ratio (PAPR) stored in the file. This method uses the waveformIndex as the key to read the waveform property. SyntaxNamespace: NationalInstruments.ModularInstruments.NIRfsgPlaybackpublic static int ReadPaprFromFile(string filePath, int waveformIndex, out double papr

### ReadPaprFromFile(string, int, out double)

Returns the peak to average power ratio (PAPR) stored in the file. This method uses the *waveformIndex* as the key to read the waveform property.

#### Syntax

**Namespace:**[NationalInstruments.ModularInstruments.NIRfsgPlayback](nationalinstruments-modularinstruments-nirfsgplayback.html)

public static int ReadPaprFromFile(string filePath, int waveformIndex, out double papr)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| filePath | string | Specifies the absolute path to the TDMS file from which the playback library reads the waveform. |
| waveformIndex | int | Specifies the waveform number in the file for which you want to read the PAPR. |
| papr | out double | Returns the PAPR stored in the file for the waveform number you specified in the waveformIndex parameter. This value is expressed in dB. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

NIRfsgPlayback Class

<!--NI_TOPIC bundle=rfsgplaybacklibrary-dotnet-api-ref path=nationalinstruments-modularinstruments-nirfsgplayback-nirfsgplayback-readpeakpoweradjustmentfromfile__string-int-out.html language=enus -->
## TOPIC 00011: ReadPeakPowerAdjustmentFromFile(string, int, out double)

- bundle_id: `rfsgplaybacklibrary-dotnet-api-ref`
- source_path: `nationalinstruments-modularinstruments-nirfsgplayback-nirfsgplayback-readpeakpoweradjustmentfromfile__string-int-out.html`
- source_url: https://docs-be.ni.com/bundle/rfsgplaybacklibrary-dotnet-api-ref/raw/resource/enus/nationalinstruments-modularinstruments-nirfsgplayback-nirfsgplayback-readpeakpoweradjustmentfromfile__string-int-out.html
- document_id: `rfsgplaybacklibrary-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the value of the peak power adjustment stored in the file. This method uses the waveformIndex as the key to read the waveform properties. SyntaxNamespace: NationalInstruments.ModularInstruments.NIRfsgPlaybackpublic static int ReadPeakPowerAdjustmentFromFile(string filePath, int waveformIndex

### ReadPeakPowerAdjustmentFromFile(string, int, out double)

Returns the value of the peak power adjustment stored in the file. This method uses the *waveformIndex* as the key to read the waveform properties.

#### Syntax

**Namespace:**[NationalInstruments.ModularInstruments.NIRfsgPlayback](nationalinstruments-modularinstruments-nirfsgplayback.html)

public static int ReadPeakPowerAdjustmentFromFile(string filePath, int waveformIndex, out double peakPowerAdjustment)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| filePath | string | Specifies the absolute path to the TDMS file from which the playback library reads the waveform. |
| waveformIndex | int | Specifies the waveform number in the file for which you want to read the peak power adjustment location. |
| peakPowerAdjustment | out double | Returns the peak power adjustment value, stored in the file for the waveform index you specified in the waveformIndex parameter. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

NIRfsgPlayback Class

<!--NI_TOPIC bundle=rfsgplaybacklibrary-dotnet-api-ref path=nationalinstruments-modularinstruments-nirfsgplayback-nirfsgplayback-readrfblankingenabledfromfile__string-int-out.html language=enus -->
## TOPIC 00012: ReadRFBlankingEnabledFromFile(string, int, out bool)

- bundle_id: `rfsgplaybacklibrary-dotnet-api-ref`
- source_path: `nationalinstruments-modularinstruments-nirfsgplayback-nirfsgplayback-readrfblankingenabledfromfile__string-int-out.html`
- source_url: https://docs-be.ni.com/bundle/rfsgplaybacklibrary-dotnet-api-ref/raw/resource/enus/nationalinstruments-modularinstruments-nirfsgplayback-nirfsgplayback-readrfblankingenabledfromfile__string-int-out.html
- document_id: `rfsgplaybacklibrary-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the RF blanking enabled value stored in the file. This method uses the waveformIndex as the key to read the waveform properties. SyntaxNamespace: NationalInstruments.ModularInstruments.NIRfsgPlaybackpublic static int ReadRFBlankingEnabledFromFile(string filePath, int waveformIndex, out bool

### ReadRFBlankingEnabledFromFile(string, int, out bool)

Returns the RF blanking enabled value stored in the file. This method uses the *waveformIndex* as the key to read the waveform properties.

#### Syntax

**Namespace:**[NationalInstruments.ModularInstruments.NIRfsgPlayback](nationalinstruments-modularinstruments-nirfsgplayback.html)

public static int ReadRFBlankingEnabledFromFile(string filePath, int waveformIndex, out bool rfBlankingEnabled)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| filePath | string | Specifies the absolute path to the TDMS file from which the playback library reads the waveforms. |
| waveformIndex | int | Specifies the waveform number in the file for which you want to read the RF blanking enabled. |
| rfBlankingEnabled | out bool | Returns the RF blanking enabled value, stored in the file for the waveform number which you specified in the waveformIndex parameter. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

NIRfsgPlayback Class

<!--NI_TOPIC bundle=rfsgplaybacklibrary-dotnet-api-ref path=nationalinstruments-modularinstruments-nirfsgplayback-nirfsgplayback-readrfblankingmarkerlocationsfromfile__string-int-ref.html language=enus -->
## TOPIC 00013: ReadRFBlankingMarkerLocationsFromFile(string, int, ref int[])

- bundle_id: `rfsgplaybacklibrary-dotnet-api-ref`
- source_path: `nationalinstruments-modularinstruments-nirfsgplayback-nirfsgplayback-readrfblankingmarkerlocationsfromfile__string-int-ref.html`
- source_url: https://docs-be.ni.com/bundle/rfsgplaybacklibrary-dotnet-api-ref/raw/resource/enus/nationalinstruments-modularinstruments-nirfsgplayback-nirfsgplayback-readrfblankingmarkerlocationsfromfile__string-int-ref.html
- document_id: `rfsgplaybacklibrary-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the RF blanking marker locations stored in the file. This method uses the waveformIndex as the key to read the waveform property. SyntaxNamespace: NationalInstruments.ModularInstruments.NIRfsgPlaybackpublic static int ReadRFBlankingMarkerLocationsFromFile(string filePath, int waveformIndex,

### ReadRFBlankingMarkerLocationsFromFile(string, int, ref int[])

Returns the RF blanking marker locations stored in the file. This method uses the *waveformIndex* as the key to read the waveform property.

#### Syntax

**Namespace:**[NationalInstruments.ModularInstruments.NIRfsgPlayback](nationalinstruments-modularinstruments-nirfsgplayback.html)

public static int ReadRFBlankingMarkerLocationsFromFile(string filePath, int waveformIndex, ref int[] markerLocations)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| filePath | string | Specifies the absolute path to the TDMS file from which the playback library reads the waveforms. |
| waveformIndex | int | specifies the waveform number in the file for which you want to read the RF blanking marker locations. |
| markerLocations | ref int[] | returns an array of the RF blanking marker location values, stored in the file for the waveform number which you specified in the waveformIndex parameter. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

NIRfsgPlayback Class

<!--NI_TOPIC bundle=rfsgplaybacklibrary-dotnet-api-ref path=nationalinstruments-modularinstruments-nirfsgplayback-nirfsgplayback-readrfblankingmarkersourcefromfile__string-int-out.html language=enus -->
## TOPIC 00014: ReadRFBlankingMarkerSourceFromFile(string, int, out string)

- bundle_id: `rfsgplaybacklibrary-dotnet-api-ref`
- source_path: `nationalinstruments-modularinstruments-nirfsgplayback-nirfsgplayback-readrfblankingmarkersourcefromfile__string-int-out.html`
- source_url: https://docs-be.ni.com/bundle/rfsgplaybacklibrary-dotnet-api-ref/raw/resource/enus/nationalinstruments-modularinstruments-nirfsgplayback-nirfsgplayback-readrfblankingmarkersourcefromfile__string-int-out.html
- document_id: `rfsgplaybacklibrary-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the RF blanking marker source stored in the file. This method uses the waveformIndex as the key to read the waveform property. SyntaxNamespace: NationalInstruments.ModularInstruments.NIRfsgPlaybackpublic static int ReadRFBlankingMarkerSourceFromFile(string filePath, int waveformIndex, out st

### ReadRFBlankingMarkerSourceFromFile(string, int, out string)

Returns the RF blanking marker source stored in the file. This method uses the *waveformIndex* as the key to read the waveform property.

#### Syntax

**Namespace:**[NationalInstruments.ModularInstruments.NIRfsgPlayback](nationalinstruments-modularinstruments-nirfsgplayback.html)

public static int ReadRFBlankingMarkerSourceFromFile(string filePath, int waveformIndex, out string markerSource)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| filePath | string | Specifies the absolute path to the TDMS file from which the playback library reads the waveform. |
| waveformIndex | int | Specifies the waveform number in the file for which you want to read the RF blanking marker source value. |
| markerSource | out string | Returns the RF blanking marker source value, stored in the file for the waveform number which you specified in the waveformIndex parameter. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

NIRfsgPlayback Class

<!--NI_TOPIC bundle=rfsgplaybacklibrary-dotnet-api-ref path=nationalinstruments-modularinstruments-nirfsgplayback-nirfsgplayback-readruntimescalingfromfile__string-int-out.html language=enus -->
## TOPIC 00015: ReadRuntimeScalingFromFile(string, int, out double)

- bundle_id: `rfsgplaybacklibrary-dotnet-api-ref`
- source_path: `nationalinstruments-modularinstruments-nirfsgplayback-nirfsgplayback-readruntimescalingfromfile__string-int-out.html`
- source_url: https://docs-be.ni.com/bundle/rfsgplaybacklibrary-dotnet-api-ref/raw/resource/enus/nationalinstruments-modularinstruments-nirfsgplayback-nirfsgplayback-readruntimescalingfromfile__string-int-out.html
- document_id: `rfsgplaybacklibrary-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the runtime scaling value stored in the file. This method uses the waveformIndex as the key to read the waveform property. SyntaxNamespace: NationalInstruments.ModularInstruments.NIRfsgPlaybackpublic static int ReadRuntimeScalingFromFile(string filePath, int waveformIndex, out double runtime

### ReadRuntimeScalingFromFile(string, int, out double)

Returns the runtime scaling value stored in the file. This method uses the *waveformIndex* as the key to read the waveform property.

#### Syntax

**Namespace:**[NationalInstruments.ModularInstruments.NIRfsgPlayback](nationalinstruments-modularinstruments-nirfsgplayback.html)

public static int ReadRuntimeScalingFromFile(string filePath, int waveformIndex, out double runtimeScaling)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| filePath | string | Specifies the absolute path to the TDMS file from which the playback library reads the waveform. |
| waveformIndex | int | Specifies the waveform number in the file for which you want to read the runtime scaling value. |
| runtimeScaling | out double | Returns the runtime scaling value stored in the file for the waveform number you specified in the waveformIndex parameter. This value is expressed in dB. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

NIRfsgPlayback Class

<!--NI_TOPIC bundle=rfsgplaybacklibrary-dotnet-api-ref path=nationalinstruments-modularinstruments-nirfsgplayback-nirfsgplayback-readsampleratefromfile__string-int-out.html language=enus -->
## TOPIC 00016: ReadSampleRateFromFile(string, int, out double)

- bundle_id: `rfsgplaybacklibrary-dotnet-api-ref`
- source_path: `nationalinstruments-modularinstruments-nirfsgplayback-nirfsgplayback-readsampleratefromfile__string-int-out.html`
- source_url: https://docs-be.ni.com/bundle/rfsgplaybacklibrary-dotnet-api-ref/raw/resource/enus/nationalinstruments-modularinstruments-nirfsgplayback-nirfsgplayback-readsampleratefromfile__string-int-out.html
- document_id: `rfsgplaybacklibrary-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the sample rate stored in the file. This method uses the waveformIndex as the key to read the waveform property. SyntaxNamespace: NationalInstruments.ModularInstruments.NIRfsgPlaybackpublic static int ReadSampleRateFromFile(string filePath, int waveformIndex, out double sampleRate)Parameters

### ReadSampleRateFromFile(string, int, out double)

Returns the sample rate stored in the file. This method uses the *waveformIndex* as the key to read the waveform property.

#### Syntax

**Namespace:**[NationalInstruments.ModularInstruments.NIRfsgPlayback](nationalinstruments-modularinstruments-nirfsgplayback.html)

public static int ReadSampleRateFromFile(string filePath, int waveformIndex, out double sampleRate)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| filePath | string | Specifies the absolute path to the TDMS file from which the playback library reads the waveform. |
| waveformIndex | int | Specifies the waveform number in the file for which you want to read the sample rate. |
| sampleRate | out double | Returns the sample rate value, stored in the file for the waveform number you specified in the waveformIndex parameter. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

NIRfsgPlayback Class

<!--NI_TOPIC bundle=rfsgplaybacklibrary-dotnet-api-ref path=nationalinstruments-modularinstruments-nirfsgplayback-nirfsgplayback-readsignalbandwidthfromfile__string-int-out.html language=enus -->
## TOPIC 00017: ReadSignalBandwidthFromFile(string, int, out double)

- bundle_id: `rfsgplaybacklibrary-dotnet-api-ref`
- source_path: `nationalinstruments-modularinstruments-nirfsgplayback-nirfsgplayback-readsignalbandwidthfromfile__string-int-out.html`
- source_url: https://docs-be.ni.com/bundle/rfsgplaybacklibrary-dotnet-api-ref/raw/resource/enus/nationalinstruments-modularinstruments-nirfsgplayback-nirfsgplayback-readsignalbandwidthfromfile__string-int-out.html
- document_id: `rfsgplaybacklibrary-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the signal bandwidth stored in the file. This method uses the waveformIndex parameter as the key to retrieve the waveform property. SyntaxNamespace: NationalInstruments.ModularInstruments.NIRfsgPlaybackpublic static int ReadSignalBandwidthFromFile(string filePath, int waveformIndex, out doub

### ReadSignalBandwidthFromFile(string, int, out double)

Returns the signal bandwidth stored in the file. This method uses the *waveformIndex* parameter as the key to retrieve the waveform property.

#### Syntax

**Namespace:**[NationalInstruments.ModularInstruments.NIRfsgPlayback](nationalinstruments-modularinstruments-nirfsgplayback.html)

public static int ReadSignalBandwidthFromFile(string filePath, int waveformIndex, out double signalBandwidth)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| filePath | string | Specifies the absolute path to the TDMS file from which the playback library reads the waveform. |
| waveformIndex | int | Specifies the waveform number in the file for which you want to read the signal bandwidth. |
| signalBandwidth | out double | Returns the signal bandwidth stored in the file for the waveform number that you specified in the waveformIndex parameter. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

NIRfsgPlayback Class

<!--NI_TOPIC bundle=rfsgplaybacklibrary-dotnet-api-ref path=nationalinstruments-modularinstruments-nirfsgplayback-nirfsgplayback-readwaveformfileversionfromfile__string-out.html language=enus -->
## TOPIC 00018: ReadWaveformFileVersionFromFile(string, out string)

- bundle_id: `rfsgplaybacklibrary-dotnet-api-ref`
- source_path: `nationalinstruments-modularinstruments-nirfsgplayback-nirfsgplayback-readwaveformfileversionfromfile__string-out.html`
- source_url: https://docs-be.ni.com/bundle/rfsgplaybacklibrary-dotnet-api-ref/raw/resource/enus/nationalinstruments-modularinstruments-nirfsgplayback-nirfsgplayback-readwaveformfileversionfromfile__string-out.html
- document_id: `rfsgplaybacklibrary-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the waveform file version of the waveform stored in the file. SyntaxNamespace: NationalInstruments.ModularInstruments.NIRfsgPlaybackpublic static int ReadWaveformFileVersionFromFile(string filePath, out string waveformFileVersion)ParametersNameTypeDescriptionfilePathstringSpecifies the absol

### ReadWaveformFileVersionFromFile(string, out string)

Returns the waveform file version of the waveform stored in the file.

#### Syntax

**Namespace:**[NationalInstruments.ModularInstruments.NIRfsgPlayback](nationalinstruments-modularinstruments-nirfsgplayback.html)

public static int ReadWaveformFileVersionFromFile(string filePath, out string waveformFileVersion)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| filePath | string | Specifies the absolute path to the TDMS file from which the playback library reads the waveform. |
| waveformFileVersion | out string | Returns the waveform file version of the waveform stored in the file. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

NIRfsgPlayback Class

<!--NI_TOPIC bundle=rfsgplaybacklibrary-dotnet-api-ref path=nationalinstruments-modularinstruments-nirfsgplayback-nirfsgplayback-readwaveformfromfilebyindexcomplex__string-int-ref.1.html language=enus -->
## TOPIC 00019: ReadWaveformFromFileByIndexComplex(string, int, ref ComplexWaveform< ComplexDouble >)

- bundle_id: `rfsgplaybacklibrary-dotnet-api-ref`
- source_path: `nationalinstruments-modularinstruments-nirfsgplayback-nirfsgplayback-readwaveformfromfilebyindexcomplex__string-int-ref.1.html`
- source_url: https://docs-be.ni.com/bundle/rfsgplaybacklibrary-dotnet-api-ref/raw/resource/enus/nationalinstruments-modularinstruments-nirfsgplayback-nirfsgplayback-readwaveformfromfilebyindexcomplex__string-int-ref.1.html
- document_id: `rfsgplaybacklibrary-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Reads the waveform from file and returns the waveform in an output parameter. SyntaxNamespace: NationalInstruments.ModularInstruments.NIRfsgPlaybackpublic static int ReadWaveformFromFileByIndexComplex(string filePath, int waveformIndex, ref ComplexWaveform< ComplexDouble > outputWaveform)ParametersN

### ReadWaveformFromFileByIndexComplex(string, int, ref ComplexWaveform< ComplexDouble >)

Reads the waveform from file and returns the waveform in an output parameter.

#### Syntax

**Namespace:**[NationalInstruments.ModularInstruments.NIRfsgPlayback](nationalinstruments-modularinstruments-nirfsgplayback.html)

public static int ReadWaveformFromFileByIndexComplex(string filePath, int waveformIndex, ref ComplexWaveform< ComplexDouble > outputWaveform)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| filePath | string | Specifies the absolute path to the TDMS file from which the playback library reads the waveforms. |
| waveformIndex | int | Specifies the index of the waveform that you want to read from the TDMS file. |
| outputWaveform | ref ComplexWaveform< ComplexDouble > | Returns the data for a complex waveform of ComplexDouble datatype, including the start, delta, and actual values. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

NIRfsgPlayback Class

<!--NI_TOPIC bundle=rfsgplaybacklibrary-dotnet-api-ref path=nationalinstruments-modularinstruments-nirfsgplayback-nirfsgplayback-readwaveformfromfilebyindexcomplex__string-int-ref.html language=enus -->
## TOPIC 00020: ReadWaveformFromFileByIndexComplex(string, int, ref ComplexWaveform< ComplexSingle >)

- bundle_id: `rfsgplaybacklibrary-dotnet-api-ref`
- source_path: `nationalinstruments-modularinstruments-nirfsgplayback-nirfsgplayback-readwaveformfromfilebyindexcomplex__string-int-ref.html`
- source_url: https://docs-be.ni.com/bundle/rfsgplaybacklibrary-dotnet-api-ref/raw/resource/enus/nationalinstruments-modularinstruments-nirfsgplayback-nirfsgplayback-readwaveformfromfilebyindexcomplex__string-int-ref.html
- document_id: `rfsgplaybacklibrary-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Reads the waveform from file and returns the waveform in an output parameter. SyntaxNamespace: NationalInstruments.ModularInstruments.NIRfsgPlaybackpublic static int ReadWaveformFromFileByIndexComplex(string filePath, int waveformIndex, ref ComplexWaveform< ComplexSingle > outputWaveform)ParametersN

### ReadWaveformFromFileByIndexComplex(string, int, ref ComplexWaveform< ComplexSingle >)

Reads the waveform from file and returns the waveform in an output parameter.

#### Syntax

**Namespace:**[NationalInstruments.ModularInstruments.NIRfsgPlayback](nationalinstruments-modularinstruments-nirfsgplayback.html)

public static int ReadWaveformFromFileByIndexComplex(string filePath, int waveformIndex, ref ComplexWaveform< ComplexSingle > outputWaveform)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| filePath | string | Specifies the absolute path to the TDMS file from which the playback library reads the waveforms. |
| waveformIndex | int | Specifies the index of the waveform that you want to read from the TDMS file. |
| outputWaveform | ref ComplexWaveform< ComplexSingle > | Returns the data for a complex waveform of ComplexSingle type, including the start, delta, and actual values. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

NIRfsgPlayback Class

<!--NI_TOPIC bundle=rfsgplaybacklibrary-dotnet-api-ref path=nationalinstruments-modularinstruments-nirfsgplayback-nirfsgplayback-readwaveformfromfilecomplex__string-ref.1.html language=enus -->
## TOPIC 00021: ReadWaveformFromFileComplex(string, ref ComplexWaveform< ComplexDouble >)

- bundle_id: `rfsgplaybacklibrary-dotnet-api-ref`
- source_path: `nationalinstruments-modularinstruments-nirfsgplayback-nirfsgplayback-readwaveformfromfilecomplex__string-ref.1.html`
- source_url: https://docs-be.ni.com/bundle/rfsgplaybacklibrary-dotnet-api-ref/raw/resource/enus/nationalinstruments-modularinstruments-nirfsgplayback-nirfsgplayback-readwaveformfromfilecomplex__string-ref.1.html
- document_id: `rfsgplaybacklibrary-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Reads the waveform from file and returns the waveform in an output parameter. SyntaxNamespace: NationalInstruments.ModularInstruments.NIRfsgPlaybackpublic static int ReadWaveformFromFileComplex(string filePath, ref ComplexWaveform< ComplexDouble > outputWaveform)ParametersNameTypeDescriptionfilePath

### ReadWaveformFromFileComplex(string, ref ComplexWaveform< ComplexDouble >)

Reads the waveform from file and returns the waveform in an output parameter.

#### Syntax

**Namespace:**[NationalInstruments.ModularInstruments.NIRfsgPlayback](nationalinstruments-modularinstruments-nirfsgplayback.html)

public static int ReadWaveformFromFileComplex(string filePath, ref ComplexWaveform< ComplexDouble > outputWaveform)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| filePath | string | Specifies the absolute path to the TDMS file from which the playback library reads the waveforms. |
| outputWaveform | ref ComplexWaveform< ComplexDouble > | Returns the data for a complex waveform of ComplexDouble datatype, including the start, delta, and actual values. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

NIRfsgPlayback Class

<!--NI_TOPIC bundle=rfsgplaybacklibrary-dotnet-api-ref path=nationalinstruments-modularinstruments-nirfsgplayback-nirfsgplayback-readwaveformfromfilecomplex__string-ref.html language=enus -->
## TOPIC 00022: ReadWaveformFromFileComplex(string, ref ComplexWaveform< ComplexSingle >)

- bundle_id: `rfsgplaybacklibrary-dotnet-api-ref`
- source_path: `nationalinstruments-modularinstruments-nirfsgplayback-nirfsgplayback-readwaveformfromfilecomplex__string-ref.html`
- source_url: https://docs-be.ni.com/bundle/rfsgplaybacklibrary-dotnet-api-ref/raw/resource/enus/nationalinstruments-modularinstruments-nirfsgplayback-nirfsgplayback-readwaveformfromfilecomplex__string-ref.html
- document_id: `rfsgplaybacklibrary-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Reads the waveform from file and returns the waveform in an output parameter. SyntaxNamespace: NationalInstruments.ModularInstruments.NIRfsgPlaybackpublic static int ReadWaveformFromFileComplex(string filePath, ref ComplexWaveform< ComplexSingle > outputWaveform)ParametersNameTypeDescriptionfilePath

### ReadWaveformFromFileComplex(string, ref ComplexWaveform< ComplexSingle >)

Reads the waveform from file and returns the waveform in an output parameter.

#### Syntax

**Namespace:**[NationalInstruments.ModularInstruments.NIRfsgPlayback](nationalinstruments-modularinstruments-nirfsgplayback.html)

public static int ReadWaveformFromFileComplex(string filePath, ref ComplexWaveform< ComplexSingle > outputWaveform)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| filePath | string | Specifies the absolute path to the TDMS file from which the playback library reads the waveforms. |
| outputWaveform | ref ComplexWaveform< ComplexSingle > | Returns the data for a complex waveform of ComplexSingle type, including the start, delta, and actual values. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

NIRfsgPlayback Class

<!--NI_TOPIC bundle=rfsgplaybacklibrary-dotnet-api-ref path=nationalinstruments-modularinstruments-nirfsgplayback-nirfsgplayback-readwaveformsfromfilecomplex__string-int-ref.1.html language=enus -->
## TOPIC 00023: ReadWaveformsFromFileComplex(string, int, ref ComplexWaveform< ComplexSingle >[])

- bundle_id: `rfsgplaybacklibrary-dotnet-api-ref`
- source_path: `nationalinstruments-modularinstruments-nirfsgplayback-nirfsgplayback-readwaveformsfromfilecomplex__string-int-ref.1.html`
- source_url: https://docs-be.ni.com/bundle/rfsgplaybacklibrary-dotnet-api-ref/raw/resource/enus/nationalinstruments-modularinstruments-nirfsgplayback-nirfsgplayback-readwaveformsfromfilecomplex__string-int-ref.1.html
- document_id: `rfsgplaybacklibrary-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Reads the waveforms from file, and returns the waveforms in an output parameter. SyntaxNamespace: NationalInstruments.ModularInstruments.NIRfsgPlaybackpublic static int ReadWaveformsFromFileComplex(string filePath, int numberOfWaveforms, ref ComplexWaveform< ComplexSingle >[] outputWaveforms)Paramet

### ReadWaveformsFromFileComplex(string, int, ref ComplexWaveform< ComplexSingle >[])

Reads the waveforms from file, and returns the waveforms in an output parameter.

#### Syntax

**Namespace:**[NationalInstruments.ModularInstruments.NIRfsgPlayback](nationalinstruments-modularinstruments-nirfsgplayback.html)

public static int ReadWaveformsFromFileComplex(string filePath, int numberOfWaveforms, ref ComplexWaveform< ComplexSingle >[] outputWaveforms)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| filePath | string | Specifies the absolute path to the TDMS file from which the playback library reads the waveforms. |
| numberOfWaveforms | int | Specifies the number of waveforms. |
| outputWaveforms | ref ComplexWaveform< ComplexSingle >[] | Returns the array of complex waveforms of ComplexSingle read from the file. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

NIRfsgPlayback Class

<!--NI_TOPIC bundle=rfsgplaybacklibrary-dotnet-api-ref path=nationalinstruments-modularinstruments-nirfsgplayback-nirfsgplayback-readwaveformsfromfilecomplex__string-int-ref.html language=enus -->
## TOPIC 00024: ReadWaveformsFromFileComplex(string, int, ref ComplexWaveform< ComplexDouble >[])

- bundle_id: `rfsgplaybacklibrary-dotnet-api-ref`
- source_path: `nationalinstruments-modularinstruments-nirfsgplayback-nirfsgplayback-readwaveformsfromfilecomplex__string-int-ref.html`
- source_url: https://docs-be.ni.com/bundle/rfsgplaybacklibrary-dotnet-api-ref/raw/resource/enus/nationalinstruments-modularinstruments-nirfsgplayback-nirfsgplayback-readwaveformsfromfilecomplex__string-int-ref.html
- document_id: `rfsgplaybacklibrary-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Reads the waveforms from file, and returns the waveforms in an output parameter. SyntaxNamespace: NationalInstruments.ModularInstruments.NIRfsgPlaybackpublic static int ReadWaveformsFromFileComplex(string filePath, int numberOfWaveforms, ref ComplexWaveform< ComplexDouble >[] outputWaveforms)Paramet

### ReadWaveformsFromFileComplex(string, int, ref ComplexWaveform< ComplexDouble >[])

Reads the waveforms from file, and returns the waveforms in an output parameter.

#### Syntax

**Namespace:**[NationalInstruments.ModularInstruments.NIRfsgPlayback](nationalinstruments-modularinstruments-nirfsgplayback.html)

public static int ReadWaveformsFromFileComplex(string filePath, int numberOfWaveforms, ref ComplexWaveform< ComplexDouble >[] outputWaveforms)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| filePath | string | Specifies the absolute path to the TDMS file from which the playback library reads the waveforms. |
| numberOfWaveforms | int | Specifies the number of waveforms. |
| outputWaveforms | ref ComplexWaveform< ComplexDouble >[] | Returns the array of complex waveforms of ComplexDouble read from the file. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

NIRfsgPlayback Class

<!--NI_TOPIC bundle=rfsgplaybacklibrary-dotnet-api-ref path=nationalinstruments-modularinstruments-nirfsgplayback-nirfsgplayback-readwaveformsizefromfile__string-int-out.html language=enus -->
## TOPIC 00025: ReadWaveformSizeFromFile(string, int, out int)

- bundle_id: `rfsgplaybacklibrary-dotnet-api-ref`
- source_path: `nationalinstruments-modularinstruments-nirfsgplayback-nirfsgplayback-readwaveformsizefromfile__string-int-out.html`
- source_url: https://docs-be.ni.com/bundle/rfsgplaybacklibrary-dotnet-api-ref/raw/resource/enus/nationalinstruments-modularinstruments-nirfsgplayback-nirfsgplayback-readwaveformsizefromfile__string-int-out.html
- document_id: `rfsgplaybacklibrary-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the size of the waveform stored in the file. This method uses the waveformIndex parameter as the key to read the waveform property. SyntaxNamespace: NationalInstruments.ModularInstruments.NIRfsgPlaybackpublic static int ReadWaveformSizeFromFile(string filePath, int waveformIndex, out int wav

### ReadWaveformSizeFromFile(string, int, out int)

Returns the size of the waveform stored in the file. This method uses the *waveformIndex* parameter as the key to read the waveform property.

#### Syntax

**Namespace:**[NationalInstruments.ModularInstruments.NIRfsgPlayback](nationalinstruments-modularinstruments-nirfsgplayback.html)

public static int ReadWaveformSizeFromFile(string filePath, int waveformIndex, out int waveformSize)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| filePath | string | Specifies the absolute path to the TDMS file from which the playback library reads the waveform. |
| waveformIndex | int | Specifies the waveform number in the file for which you want to read the waveform size. |
| waveformSize | out int | Returns the size of the waveform stored in the file for the waveform number that you specified in the waveformIndex parameter. This value is expressed in samples. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

NIRfsgPlayback Class

<!--NI_TOPIC bundle=rfsgplaybacklibrary-dotnet-api-ref path=nationalinstruments-modularinstruments-nirfsgplayback-nirfsgplayback-retrieveautomaticsgsasharedlo__intptr-string-out.html language=enus -->
## TOPIC 00026: RetrieveAutomaticSGSASharedLO(IntPtr, string, out RfsgPlaybackAutomaticSGSASharedLO)

- bundle_id: `rfsgplaybacklibrary-dotnet-api-ref`
- source_path: `nationalinstruments-modularinstruments-nirfsgplayback-nirfsgplayback-retrieveautomaticsgsasharedlo__intptr-string-out.html`
- source_url: https://docs-be.ni.com/bundle/rfsgplaybacklibrary-dotnet-api-ref/raw/resource/enus/nationalinstruments-modularinstruments-nirfsgplayback-nirfsgplayback-retrieveautomaticsgsasharedlo__intptr-string-out.html
- document_id: `rfsgplaybacklibrary-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the value of automatic SG SA shared LO parameter. SyntaxNamespace: NationalInstruments.ModularInstruments.NIRfsgPlaybackpublic static int RetrieveAutomaticSGSASharedLO(IntPtr rfsgSession, string channelName, out RfsgPlaybackAutomaticSGSASharedLO automaticSGSASharedLO)ParametersNameTypeDescri

### RetrieveAutomaticSGSASharedLO(IntPtr, string, out RfsgPlaybackAutomaticSGSASharedLO)

Returns the value of **automatic SG SA shared LO** parameter.

#### Syntax

**Namespace:**[NationalInstruments.ModularInstruments.NIRfsgPlayback](nationalinstruments-modularinstruments-nirfsgplayback.html)

public static int RetrieveAutomaticSGSASharedLO(IntPtr rfsgSession, string channelName, out RfsgPlaybackAutomaticSGSASharedLO automaticSGSASharedLO)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| rfsgSession | IntPtr | Identifies the instrument session. The rfsgSession handle is obtained from the NIRfsg.DangerousGetInstrumentHandle method. |
| channelName | string | This parameter is reserved for future use. |
| automaticSGSASharedLO | out RfsgPlaybackAutomaticSGSASharedLO | Returns the access control of SG LO. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

NIRfsgPlayback Class

<!--NI_TOPIC bundle=rfsgplaybacklibrary-dotnet-api-ref path=nationalinstruments-modularinstruments-nirfsgplayback-nirfsgplayback-retrievedownloadedwaveformnames__intptr-out.html language=enus -->
## TOPIC 00027: RetrieveDownloadedWaveformNames(IntPtr, out string[])

- bundle_id: `rfsgplaybacklibrary-dotnet-api-ref`
- source_path: `nationalinstruments-modularinstruments-nirfsgplayback-nirfsgplayback-retrievedownloadedwaveformnames__intptr-out.html`
- source_url: https://docs-be.ni.com/bundle/rfsgplaybacklibrary-dotnet-api-ref/raw/resource/enus/nationalinstruments-modularinstruments-nirfsgplayback-nirfsgplayback-retrievedownloadedwaveformnames__intptr-out.html
- document_id: `rfsgplaybacklibrary-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the names of the waveforms that are stored in the NI-RFSG waveform database. SyntaxNamespace: NationalInstruments.ModularInstruments.NIRfsgPlaybackpublic static int RetrieveDownloadedWaveformNames(IntPtr rfsgSession, out string[] waveformNames)ParametersNameTypeDescriptionrfsgSessionIntPtrId

### RetrieveDownloadedWaveformNames(IntPtr, out string[])

Returns the names of the waveforms that are stored in the NI-RFSG waveform database.

#### Syntax

**Namespace:**[NationalInstruments.ModularInstruments.NIRfsgPlayback](nationalinstruments-modularinstruments-nirfsgplayback.html)

public static int RetrieveDownloadedWaveformNames(IntPtr rfsgSession, out string[] waveformNames)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| rfsgSession | IntPtr | Identifies the instrument session. The rfsgSession handle is obtained from the NIRfsg.DangerousGetInstrumentHandle method. |
| waveformNames | out string[] | Returns an array of the waveform names that are stored in the NI-RFSG waveform database. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

NIRfsgPlayback Class

<!--NI_TOPIC bundle=rfsgplaybacklibrary-dotnet-api-ref path=nationalinstruments-modularinstruments-nirfsgplayback-nirfsgplayback-retrievewaveformburststartlocations__intptr-string-ref.html language=enus -->
## TOPIC 00028: RetrieveWaveformBurstStartLocations(IntPtr, string, ref int[])

- bundle_id: `rfsgplaybacklibrary-dotnet-api-ref`
- source_path: `nationalinstruments-modularinstruments-nirfsgplayback-nirfsgplayback-retrievewaveformburststartlocations__intptr-string-ref.html`
- source_url: https://docs-be.ni.com/bundle/rfsgplaybacklibrary-dotnet-api-ref/raw/resource/enus/nationalinstruments-modularinstruments-nirfsgplayback-nirfsgplayback-retrievewaveformburststartlocations__intptr-string-ref.html
- document_id: `rfsgplaybacklibrary-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the RF burst start positions property stored in the NI-RFSG waveform database. This method uses the waveformName parameter as the key to retrieve the waveform property. SyntaxNamespace: NationalInstruments.ModularInstruments.NIRfsgPlaybackpublic static int RetrieveWaveformBurstStartLocations

### RetrieveWaveformBurstStartLocations(IntPtr, string, ref int[])

Returns the RF burst start positions property stored in the NI-RFSG waveform database. This method uses the *waveformName* parameter as the key to retrieve the waveform property.

#### Syntax

**Namespace:**[NationalInstruments.ModularInstruments.NIRfsgPlayback](nationalinstruments-modularinstruments-nirfsgplayback.html)

public static int RetrieveWaveformBurstStartLocations(IntPtr rfsgSession, string waveformName, ref int[] burstStartLocations)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| rfsgSession | IntPtr | Identifies the instrument session. The rfsgSession handle is obtained from the NI-RFSG DangerousGetInstrumentHandle method. |
| waveformName | string | Specifies the waveform name for which you want to retrieve the RF burst start locations. |
| burstStartLocations | ref int[] | Returns the array of RF burst start positions stored in the NI-RFSG waveform database for the waveform you specified in the waveformName parameter. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

NIRfsgPlayback Class

<!--NI_TOPIC bundle=rfsgplaybacklibrary-dotnet-api-ref path=nationalinstruments-modularinstruments-nirfsgplayback-nirfsgplayback-retrievewaveformburststoplocations__intptr-string-ref.html language=enus -->
## TOPIC 00029: RetrieveWaveformBurstStopLocations(IntPtr, string, ref int[])

- bundle_id: `rfsgplaybacklibrary-dotnet-api-ref`
- source_path: `nationalinstruments-modularinstruments-nirfsgplayback-nirfsgplayback-retrievewaveformburststoplocations__intptr-string-ref.html`
- source_url: https://docs-be.ni.com/bundle/rfsgplaybacklibrary-dotnet-api-ref/raw/resource/enus/nationalinstruments-modularinstruments-nirfsgplayback-nirfsgplayback-retrievewaveformburststoplocations__intptr-string-ref.html
- document_id: `rfsgplaybacklibrary-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the RF burst stop positions property stored in the NI-RFSG waveform database. This method uses the waveformName parameter as the key to retrieve the waveform property. SyntaxNamespace: NationalInstruments.ModularInstruments.NIRfsgPlaybackpublic static int RetrieveWaveformBurstStopLocations(I

### RetrieveWaveformBurstStopLocations(IntPtr, string, ref int[])

Returns the RF burst stop positions property stored in the NI-RFSG waveform database. This method uses the *waveformName* parameter as the key to retrieve the waveform property.

#### Syntax

**Namespace:**[NationalInstruments.ModularInstruments.NIRfsgPlayback](nationalinstruments-modularinstruments-nirfsgplayback.html)

public static int RetrieveWaveformBurstStopLocations(IntPtr rfsgSession, string waveformName, ref int[] burstStopLocations)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| rfsgSession | IntPtr | Identifies the instrument session. The rfsgSession handle is obtained from the NIRfsg.DangerousGetInstrumentHandle method. |
| waveformName | string | Specifies the name of the waveform for which you want to retrieve the RF burst stop locations. |
| burstStopLocations | ref int[] | Returns the array of RF burst stop positions stored in the NI-RFSG waveform database for the waveform you specified in the waveformName parameter. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

NIRfsgPlayback Class

<!--NI_TOPIC bundle=rfsgplaybacklibrary-dotnet-api-ref path=nationalinstruments-modularinstruments-nirfsgplayback-nirfsgplayback-retrievewaveformfileversion__intptr-string-out.html language=enus -->
## TOPIC 00030: RetrieveWaveformFileVersion(IntPtr, string, out string)

- bundle_id: `rfsgplaybacklibrary-dotnet-api-ref`
- source_path: `nationalinstruments-modularinstruments-nirfsgplayback-nirfsgplayback-retrievewaveformfileversion__intptr-string-out.html`
- source_url: https://docs-be.ni.com/bundle/rfsgplaybacklibrary-dotnet-api-ref/raw/resource/enus/nationalinstruments-modularinstruments-nirfsgplayback-nirfsgplayback-retrievewaveformfileversion__intptr-string-out.html
- document_id: `rfsgplaybacklibrary-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the waveform file version stored in the NI-RFSG waveform database. This method uses the waveformName parameter as the key to retrieve the waveform property. SyntaxNamespace: NationalInstruments.ModularInstruments.NIRfsgPlaybackpublic static int RetrieveWaveformFileVersion(IntPtr rfsgSession,

### RetrieveWaveformFileVersion(IntPtr, string, out string)

Returns the waveform file version stored in the NI-RFSG waveform database. This method uses the *waveformName* parameter as the key to retrieve the waveform property.

#### Syntax

**Namespace:**[NationalInstruments.ModularInstruments.NIRfsgPlayback](nationalinstruments-modularinstruments-nirfsgplayback.html)

public static int RetrieveWaveformFileVersion(IntPtr rfsgSession, string waveformName, out string waveformFileVersion)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| rfsgSession | IntPtr | Identifies the instrument session. The rfsgSession handle is obtained from the NIRfsg.DangerousGetInstrumentHandle method. |
| waveformName | string | Specifies the name of the waveform for which you want to retrieve the waveform file version. |
| waveformFileVersion | out string | Returns the waveform file version of the waveform stored in the NI-RFSG waveform database for the waveform you specified in the waveformName parameter. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

NIRfsgPlayback Class

<!--NI_TOPIC bundle=rfsgplaybacklibrary-dotnet-api-ref path=nationalinstruments-modularinstruments-nirfsgplayback-nirfsgplayback-retrievewaveformlooffsetmode__intptr-string-out.html language=enus -->
## TOPIC 00031: RetrieveWaveformLOOffsetMode(IntPtr, string, out NIRfsgPlaybackLOOffsetMode)

- bundle_id: `rfsgplaybacklibrary-dotnet-api-ref`
- source_path: `nationalinstruments-modularinstruments-nirfsgplayback-nirfsgplayback-retrievewaveformlooffsetmode__intptr-string-out.html`
- source_url: https://docs-be.ni.com/bundle/rfsgplaybacklibrary-dotnet-api-ref/raw/resource/enus/nationalinstruments-modularinstruments-nirfsgplayback-nirfsgplayback-retrievewaveformlooffsetmode__intptr-string-out.html
- document_id: `rfsgplaybacklibrary-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the LO offset mode value stored in the NI-RFSG waveform database. This method uses the waveformName parameter as the key to retrieve the waveform property. SyntaxNamespace: NationalInstruments.ModularInstruments.NIRfsgPlaybackpublic static int RetrieveWaveformLOOffsetMode(IntPtr rfsgSession,

### RetrieveWaveformLOOffsetMode(IntPtr, string, out NIRfsgPlaybackLOOffsetMode)

Returns the LO offset mode value stored in the NI-RFSG waveform database. This method uses the *waveformName* parameter as the key to retrieve the waveform property.

#### Syntax

**Namespace:**[NationalInstruments.ModularInstruments.NIRfsgPlayback](nationalinstruments-modularinstruments-nirfsgplayback.html)

public static int RetrieveWaveformLOOffsetMode(IntPtr rfsgSession, string waveformName, out NIRfsgPlaybackLOOffsetMode value)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| rfsgSession | IntPtr | Identifies the instrument session. The rfsgSession handle is obtained from the NIRfsg.DangerousGetInstrumentHandle method. |
| waveformName | string | Specifies the name of the waveform for which you want to retrieve the waveform LO offset mode value. |
| value | out NIRfsgPlaybackLOOffsetMode | Returns the LO offset mode value stored in the NI-RFSG waveform database for the waveform number which you specified in the waveformName parameter. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

NIRfsgPlayback Class

<!--NI_TOPIC bundle=rfsgplaybacklibrary-dotnet-api-ref path=nationalinstruments-modularinstruments-nirfsgplayback-nirfsgplayback-retrievewaveformpapr__intptr-string-out.html language=enus -->
## TOPIC 00032: RetrieveWaveformPapr(IntPtr, string, out double)

- bundle_id: `rfsgplaybacklibrary-dotnet-api-ref`
- source_path: `nationalinstruments-modularinstruments-nirfsgplayback-nirfsgplayback-retrievewaveformpapr__intptr-string-out.html`
- source_url: https://docs-be.ni.com/bundle/rfsgplaybacklibrary-dotnet-api-ref/raw/resource/enus/nationalinstruments-modularinstruments-nirfsgplayback-nirfsgplayback-retrievewaveformpapr__intptr-string-out.html
- document_id: `rfsgplaybacklibrary-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the peak to average power ratio (PAPR) stored in the NI-RFSG waveform database. This method uses the waveformName parameter as the key to retrieve the waveform property. SyntaxNamespace: NationalInstruments.ModularInstruments.NIRfsgPlaybackpublic static int RetrieveWaveformPapr(IntPtr rfsgSe

### RetrieveWaveformPapr(IntPtr, string, out double)

Returns the peak to average power ratio (PAPR) stored in the NI-RFSG waveform database. This method uses the *waveformName* parameter as the key to retrieve the waveform property.

#### Syntax

**Namespace:**[NationalInstruments.ModularInstruments.NIRfsgPlayback](nationalinstruments-modularinstruments-nirfsgplayback.html)

public static int RetrieveWaveformPapr(IntPtr rfsgSession, string waveformName, out double papr)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| rfsgSession | IntPtr | Identifies the instrument session. The rfsgSession handle is obtained from the NIRfsg.DangerousGetInstrumentHandle method. |
| waveformName | string | Specifies the name of the waveform for which you want to retrieve the PAPR. |
| papr | out double | Returns the PAPR stored in the NI-RFSG database for the waveform you specified in the waveformName parameter. This value is expressed in dB. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

NIRfsgPlayback Class

<!--NI_TOPIC bundle=rfsgplaybacklibrary-dotnet-api-ref path=nationalinstruments-modularinstruments-nirfsgplayback-nirfsgplayback-retrievewaveformpeakpoweradjustment__intptr-string-out.html language=enus -->
## TOPIC 00033: RetrieveWaveformPeakPowerAdjustment(IntPtr, string, out double)

- bundle_id: `rfsgplaybacklibrary-dotnet-api-ref`
- source_path: `nationalinstruments-modularinstruments-nirfsgplayback-nirfsgplayback-retrievewaveformpeakpoweradjustment__intptr-string-out.html`
- source_url: https://docs-be.ni.com/bundle/rfsgplaybacklibrary-dotnet-api-ref/raw/resource/enus/nationalinstruments-modularinstruments-nirfsgplayback-nirfsgplayback-retrievewaveformpeakpoweradjustment__intptr-string-out.html
- document_id: `rfsgplaybacklibrary-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the value of the Peak Power Adjustment property stored in the NI-RFSG waveform database. This method uses the waveformName parameter as the key to retrieve the waveform property. SyntaxNamespace: NationalInstruments.ModularInstruments.NIRfsgPlaybackpublic static int RetrieveWaveformPeakPower

### RetrieveWaveformPeakPowerAdjustment(IntPtr, string, out double)

Returns the value of the Peak Power Adjustment property stored in the NI-RFSG waveform database. This method uses the *waveformName* parameter as the key to retrieve the waveform property.

#### Syntax

**Namespace:**[NationalInstruments.ModularInstruments.NIRfsgPlayback](nationalinstruments-modularinstruments-nirfsgplayback.html)

public static int RetrieveWaveformPeakPowerAdjustment(IntPtr rfsgSession, string waveformName, out double peakPowerAdjustment)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| rfsgSession | IntPtr | Identifies the instrument session. The rfsgSession handle is obtained from the NIRfsg.DangerousGetInstrumentHandle method. |
| waveformName | string | Specifies the name of the waveform for which you want to retrieve the peak power adjustment value. |
| peakPowerAdjustment | out double | Returns the Peak Power Adjustment property value stored in the NI-RFSG waveform database for the waveform you specified in the waveformName parameter. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

NIRfsgPlayback Class

<!--NI_TOPIC bundle=rfsgplaybacklibrary-dotnet-api-ref path=nationalinstruments-modularinstruments-nirfsgplayback-nirfsgplayback-retrievewaveformrfblankingenabled__intptr-string-out.html language=enus -->
## TOPIC 00034: RetrieveWaveformRFBlankingEnabled(IntPtr, string, out bool)

- bundle_id: `rfsgplaybacklibrary-dotnet-api-ref`
- source_path: `nationalinstruments-modularinstruments-nirfsgplayback-nirfsgplayback-retrievewaveformrfblankingenabled__intptr-string-out.html`
- source_url: https://docs-be.ni.com/bundle/rfsgplaybacklibrary-dotnet-api-ref/raw/resource/enus/nationalinstruments-modularinstruments-nirfsgplayback-nirfsgplayback-retrievewaveformrfblankingenabled__intptr-string-out.html
- document_id: `rfsgplaybacklibrary-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the RF blanking enabled value stored in the NI-RFSG waveform database. This method uses the waveformName parameter as the key to retrieve the waveform properties. SyntaxNamespace: NationalInstruments.ModularInstruments.NIRfsgPlaybackpublic static int RetrieveWaveformRFBlankingEnabled(IntPtr

### RetrieveWaveformRFBlankingEnabled(IntPtr, string, out bool)

Returns the RF blanking enabled value stored in the NI-RFSG waveform database. This method uses the *waveformName* parameter as the key to retrieve the waveform properties.

#### Syntax

**Namespace:**[NationalInstruments.ModularInstruments.NIRfsgPlayback](nationalinstruments-modularinstruments-nirfsgplayback.html)

public static int RetrieveWaveformRFBlankingEnabled(IntPtr rfsgSession, string waveformName, out bool rfBlankingEnabled)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| rfsgSession | IntPtr | Identifies the instrument session. The rfsgSession handle is obtained from the NIRfsg.DangerousGetInstrumentHandle method. |
| waveformName | string | Specifies the name of the waveform for which you want to retrieve the RF blanking enabled value. |
| rfBlankingEnabled | out bool | Returns the RF blanking enabled stored in the NI-RFSG waveform database for the waveform which you specified in the waveformName parameter. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

NIRfsgPlayback Class

<!--NI_TOPIC bundle=rfsgplaybacklibrary-dotnet-api-ref path=nationalinstruments-modularinstruments-nirfsgplayback-nirfsgplayback-retrievewaveformrfblankingmarkerlocations__intptr-string-ref.html language=enus -->
## TOPIC 00035: RetrieveWaveformRFBlankingMarkerLocations(IntPtr, string, ref int[])

- bundle_id: `rfsgplaybacklibrary-dotnet-api-ref`
- source_path: `nationalinstruments-modularinstruments-nirfsgplayback-nirfsgplayback-retrievewaveformrfblankingmarkerlocations__intptr-string-ref.html`
- source_url: https://docs-be.ni.com/bundle/rfsgplaybacklibrary-dotnet-api-ref/raw/resource/enus/nationalinstruments-modularinstruments-nirfsgplayback-nirfsgplayback-retrievewaveformrfblankingmarkerlocations__intptr-string-ref.html
- document_id: `rfsgplaybacklibrary-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the RF blanking marker positions property stored in the NI-RFSG waveform database. This method uses the waveformName as the key to retrieve the waveform property. SyntaxNamespace: NationalInstruments.ModularInstruments.NIRfsgPlaybackpublic static int RetrieveWaveformRFBlankingMarkerLocations

### RetrieveWaveformRFBlankingMarkerLocations(IntPtr, string, ref int[])

Returns the RF blanking marker positions property stored in the NI-RFSG waveform database. This method uses the *waveformName* as the key to retrieve the waveform property.

#### Syntax

**Namespace:**[NationalInstruments.ModularInstruments.NIRfsgPlayback](nationalinstruments-modularinstruments-nirfsgplayback.html)

public static int RetrieveWaveformRFBlankingMarkerLocations(IntPtr rfsgSession, string waveformName, ref int[] markerLocations)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| rfsgSession | IntPtr | Identifies the instrument session. The rfsgSession handle is obtained from the NIRfsg.DangerousGetInstrumentHandle method. |
| waveformName | string | Specifies the name of the waveform for which you want to retrieve the retrieve RF blanking marker locations. |
| markerLocations | ref int[] | Returns the array of RF blanking marker positions stored in the NI-RFSG waveform database for the waveform you specified in the waveformName parameter. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

NIRfsgPlayback Class

<!--NI_TOPIC bundle=rfsgplaybacklibrary-dotnet-api-ref path=nationalinstruments-modularinstruments-nirfsgplayback-nirfsgplayback-retrievewaveformrfblankingmarkersource__intptr-string-out.html language=enus -->
## TOPIC 00036: RetrieveWaveformRFBlankingMarkerSource(IntPtr, string, out string)

- bundle_id: `rfsgplaybacklibrary-dotnet-api-ref`
- source_path: `nationalinstruments-modularinstruments-nirfsgplayback-nirfsgplayback-retrievewaveformrfblankingmarkersource__intptr-string-out.html`
- source_url: https://docs-be.ni.com/bundle/rfsgplaybacklibrary-dotnet-api-ref/raw/resource/enus/nationalinstruments-modularinstruments-nirfsgplayback-nirfsgplayback-retrievewaveformrfblankingmarkersource__intptr-string-out.html
- document_id: `rfsgplaybacklibrary-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the RF blanking marker source stored in the NI-RFSG waveform database. This method uses the waveformName parameter as the key to retrieve the waveform property. SyntaxNamespace: NationalInstruments.ModularInstruments.NIRfsgPlaybackpublic static int RetrieveWaveformRFBlankingMarkerSource(IntP

### RetrieveWaveformRFBlankingMarkerSource(IntPtr, string, out string)

Returns the RF blanking marker source stored in the NI-RFSG waveform database. This method uses the *waveformName* parameter as the key to retrieve the waveform property.

#### Syntax

**Namespace:**[NationalInstruments.ModularInstruments.NIRfsgPlayback](nationalinstruments-modularinstruments-nirfsgplayback.html)

public static int RetrieveWaveformRFBlankingMarkerSource(IntPtr rfsgSession, string waveformName, out string markerSource)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| rfsgSession | IntPtr | Identifies the instrument session. The rfsgSession handle is obtained from the NIRfsg.DangerousGetInstrumentHandle method. |
| waveformName | string | Specifies the name of the waveform for which you want to retrieve the RF blanking marker source value. |
| markerSource | out string | Returns the RF blanking marker source stored in the NI-RFSG waveform database for the waveform you specified in the waveformName parameter. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

NIRfsgPlayback Class

<!--NI_TOPIC bundle=rfsgplaybacklibrary-dotnet-api-ref path=nationalinstruments-modularinstruments-nirfsgplayback-nirfsgplayback-retrievewaveformruntimescaling__intptr-string-out.html language=enus -->
## TOPIC 00037: RetrieveWaveformRuntimeScaling(IntPtr, string, out double)

- bundle_id: `rfsgplaybacklibrary-dotnet-api-ref`
- source_path: `nationalinstruments-modularinstruments-nirfsgplayback-nirfsgplayback-retrievewaveformruntimescaling__intptr-string-out.html`
- source_url: https://docs-be.ni.com/bundle/rfsgplaybacklibrary-dotnet-api-ref/raw/resource/enus/nationalinstruments-modularinstruments-nirfsgplayback-nirfsgplayback-retrievewaveformruntimescaling__intptr-string-out.html
- document_id: `rfsgplaybacklibrary-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the runtime scaling value stored in the NI-RFSG waveform database. This method uses the waveformName parameter as the key to retrieve the waveform property. SyntaxNamespace: NationalInstruments.ModularInstruments.NIRfsgPlaybackpublic static int RetrieveWaveformRuntimeScaling(IntPtr rfsgSessi

### RetrieveWaveformRuntimeScaling(IntPtr, string, out double)

Returns the runtime scaling value stored in the NI-RFSG waveform database. This method uses the *waveformName* parameter as the key to retrieve the waveform property.

#### Syntax

**Namespace:**[NationalInstruments.ModularInstruments.NIRfsgPlayback](nationalinstruments-modularinstruments-nirfsgplayback.html)

public static int RetrieveWaveformRuntimeScaling(IntPtr rfsgSession, string waveformName, out double runtimeScaling)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| rfsgSession | IntPtr | Identifies the instrument session. The rfsgSession handle is obtained from the NIRfsg.DangerousGetInstrumentHandle method. |
| waveformName | string | Specifies the name of the waveform for which you want to retrieve the runtime scaling value. |
| runtimeScaling | out double | Returns the runtime scaling value stored in the NI-RFSG waveform database for the waveform you specified in the waveformName parameter. This value is expressed in dB. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

NIRfsgPlayback Class

<!--NI_TOPIC bundle=rfsgplaybacklibrary-dotnet-api-ref path=nationalinstruments-modularinstruments-nirfsgplayback-nirfsgplayback-retrievewaveformsamplerate__intptr-string-out.html language=enus -->
## TOPIC 00038: RetrieveWaveformSampleRate(IntPtr, string, out double)

- bundle_id: `rfsgplaybacklibrary-dotnet-api-ref`
- source_path: `nationalinstruments-modularinstruments-nirfsgplayback-nirfsgplayback-retrievewaveformsamplerate__intptr-string-out.html`
- source_url: https://docs-be.ni.com/bundle/rfsgplaybacklibrary-dotnet-api-ref/raw/resource/enus/nationalinstruments-modularinstruments-nirfsgplayback-nirfsgplayback-retrievewaveformsamplerate__intptr-string-out.html
- document_id: `rfsgplaybacklibrary-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the sample rate stored in the NI-RFSG waveform database. This method uses the waveformName parameter as the key to retrieve the waveform properties. SyntaxNamespace: NationalInstruments.ModularInstruments.NIRfsgPlaybackpublic static int RetrieveWaveformSampleRate(IntPtr rfsgSession, string w

### RetrieveWaveformSampleRate(IntPtr, string, out double)

Returns the sample rate stored in the NI-RFSG waveform database. This method uses the *waveformName* parameter as the key to retrieve the waveform properties.

#### Syntax

**Namespace:**[NationalInstruments.ModularInstruments.NIRfsgPlayback](nationalinstruments-modularinstruments-nirfsgplayback.html)

public static int RetrieveWaveformSampleRate(IntPtr rfsgSession, string waveformName, out double sampleRate)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| rfsgSession | IntPtr | Identifies the instrument session. The rfsgSession handle is obtained from the NIRfsg.DangerousGetInstrumentHandle method. |
| waveformName | string | Specifies the name of the waveform for which you want to retrieve the sample rate value. |
| sampleRate | out double | Returns the sampling rate stored in the NI-RFSG waveform database for the waveform you specified in the waveformName parameter. This value is expressed in samples per second (S/s). |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

NIRfsgPlayback Class

<!--NI_TOPIC bundle=rfsgplaybacklibrary-dotnet-api-ref path=nationalinstruments-modularinstruments-nirfsgplayback-nirfsgplayback-retrievewaveformsignalbandwidth__intptr-string-out.html language=enus -->
## TOPIC 00039: RetrieveWaveformSignalBandwidth(IntPtr, string, out double)

- bundle_id: `rfsgplaybacklibrary-dotnet-api-ref`
- source_path: `nationalinstruments-modularinstruments-nirfsgplayback-nirfsgplayback-retrievewaveformsignalbandwidth__intptr-string-out.html`
- source_url: https://docs-be.ni.com/bundle/rfsgplaybacklibrary-dotnet-api-ref/raw/resource/enus/nationalinstruments-modularinstruments-nirfsgplayback-nirfsgplayback-retrievewaveformsignalbandwidth__intptr-string-out.html
- document_id: `rfsgplaybacklibrary-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the signal bandwidth stored in the NI-RFSG waveform database. This method uses the waveformName parameter as the key to retrieve the waveform property. SyntaxNamespace: NationalInstruments.ModularInstruments.NIRfsgPlaybackpublic static int RetrieveWaveformSignalBandwidth(IntPtr rfsgSession,

### RetrieveWaveformSignalBandwidth(IntPtr, string, out double)

Returns the signal bandwidth stored in the NI-RFSG waveform database. This method uses the *waveformName* parameter as the key to retrieve the waveform property.

#### Syntax

**Namespace:**[NationalInstruments.ModularInstruments.NIRfsgPlayback](nationalinstruments-modularinstruments-nirfsgplayback.html)

public static int RetrieveWaveformSignalBandwidth(IntPtr rfsgSession, string waveformName, out double signalBandwidth)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| rfsgSession | IntPtr | Identifies the instrument session. The rfsgSession handle is obtained from the NIRfsg.DangerousGetInstrumentHandle method. |
| waveformName | string | Specifies the name of the waveform for which you want to retrieve the waveform signal bandwidth. |
| signalBandwidth | out double | Returns the signal bandwidth stored in the NI-RFSG waveform database for the waveform you specified in the waveformName parameter. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

NIRfsgPlayback Class

<!--NI_TOPIC bundle=rfsgplaybacklibrary-dotnet-api-ref path=nationalinstruments-modularinstruments-nirfsgplayback-nirfsgplayback-retrievewaveformsize__intptr-string-out.html language=enus -->
## TOPIC 00040: RetrieveWaveformSize(IntPtr, string, out int)

- bundle_id: `rfsgplaybacklibrary-dotnet-api-ref`
- source_path: `nationalinstruments-modularinstruments-nirfsgplayback-nirfsgplayback-retrievewaveformsize__intptr-string-out.html`
- source_url: https://docs-be.ni.com/bundle/rfsgplaybacklibrary-dotnet-api-ref/raw/resource/enus/nationalinstruments-modularinstruments-nirfsgplayback-nirfsgplayback-retrievewaveformsize__intptr-string-out.html
- document_id: `rfsgplaybacklibrary-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the size of the waveform stored in the NI-RFSG waveform database. This method uses the waveformName parameter as the key to retrieve the waveform property. SyntaxNamespace: NationalInstruments.ModularInstruments.NIRfsgPlaybackpublic static int RetrieveWaveformSize(IntPtr rfsgSession, string

### RetrieveWaveformSize(IntPtr, string, out int)

Returns the size of the waveform stored in the NI-RFSG waveform database. This method uses the *waveformName* parameter as the key to retrieve the waveform property.

#### Syntax

**Namespace:**[NationalInstruments.ModularInstruments.NIRfsgPlayback](nationalinstruments-modularinstruments-nirfsgplayback.html)

public static int RetrieveWaveformSize(IntPtr rfsgSession, string waveformName, out int waveformSize)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| rfsgSession | IntPtr | Identifies the instrument session. The rfsgSession handle is obtained from the NIRfsg.DangerousGetInstrumentHandle method. |
| waveformName | string | Specifies the name of the waveform for which you want to retrieve the waveform size. |
| waveformSize | out int | Specifies the size of the waveform stored in the NI-RFSG waveform database for the waveform you specified in the waveformName parameter. This value is expressed in samples. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

NIRfsgPlayback Class

<!--NI_TOPIC bundle=rfsgplaybacklibrary-dotnet-api-ref path=nationalinstruments-modularinstruments-nirfsgplayback-nirfsgplayback-setscripttogeneratemultiplerfsg__intptr_arr1-string.html language=enus -->
## TOPIC 00041: SetScriptToGenerateMultipleRfsg(IntPtr[], string)

- bundle_id: `rfsgplaybacklibrary-dotnet-api-ref`
- source_path: `nationalinstruments-modularinstruments-nirfsgplayback-nirfsgplayback-setscripttogeneratemultiplerfsg__intptr_arr1-string.html`
- source_url: https://docs-be.ni.com/bundle/rfsgplaybacklibrary-dotnet-api-ref/raw/resource/enus/nationalinstruments-modularinstruments-nirfsgplayback-nirfsgplayback-setscripttogeneratemultiplerfsg__intptr_arr1-string.html
- document_id: `rfsgplaybacklibrary-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Sets the NI-RFSG driver to generate the waveforms specified in the script at the average power you configure on the NI-RFSG Power Level method. If you have enabled RF Blanking for the waveform, NI-RFSG is configured to correctly blank the output during the idle times of the waveform. SyntaxNamespace

### SetScriptToGenerateMultipleRfsg(IntPtr[], string)

Sets the NI-RFSG driver to generate the waveforms specified in the script at the average power you configure on the NI-RFSG Power Level method. If you have enabled RF Blanking for the waveform, NI-RFSG is configured to correctly blank the output during the idle times of the waveform.

#### Syntax

**Namespace:**[NationalInstruments.ModularInstruments.NIRfsgPlayback](nationalinstruments-modularinstruments-nirfsgplayback.html)

public static int SetScriptToGenerateMultipleRfsg(IntPtr[] rfsgSessions, string scriptText)

#### Remarks

- Sets the NI-RFSG Peak Power Adjustment method to the minimum value of the peak to average power ratio (PAPR) of the waveforms in the script.
- Sets the NI-RFSG Pre-filter Gain method to the minimum value of the runtime scaling of the waveforms in the script.

If the version of the waveform file is lesser than 2.0, the method,

- Sets the NI-RFSG Peak Power Adjustment method to the minimum value of the Headroom of the waveforms in the script.
- Resets the NI-RFSG Pre-filter Gain method.

For the waveforms that have the RF blanking Enabled method set to True, this VI also does the following:

- If the values of RF blanking marker source of all the waveforms are empty, then the first unused marker in the script is set as the RF Blanking Source.
- Modifies the script to add the waveform burst start and stop locations as the RF Blanking marker locations

For PXIe-5840/5841/5842 and PXIe-5830/5831/5832 devices,

- Sets the NI-RFSG Signal Bandwidth method to the maximum signal bandwidth of the waveform(s) in the script, if you set the LO Offset Mode to **Auto**. If no signal bandwidth is found in any waveform of the script, the NI-RFSG Signal Bandwidth method is set to 0.8 times the Sample Rate.
- Resets the NI-RFSG Signal Bandwidth, if you set the LO Offset Mode to **No Offset**.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| rfsgSessions | IntPtr[] | Identifies instruments for multiple RFSG sessions. The rfsgSession handle is obtained from the NIRfsg.DangerousGetInstrumentHandle method. |
| scriptText | string | Specifies the script that controls the waveform generation. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

NIRfsgPlayback Class

<!--NI_TOPIC bundle=rfsgplaybacklibrary-dotnet-api-ref path=nationalinstruments-modularinstruments-nirfsgplayback-nirfsgplayback-setscripttogeneratesinglerfsg__intptr-string.html language=enus -->
## TOPIC 00042: SetScriptToGenerateSingleRfsg(IntPtr, string)

- bundle_id: `rfsgplaybacklibrary-dotnet-api-ref`
- source_path: `nationalinstruments-modularinstruments-nirfsgplayback-nirfsgplayback-setscripttogeneratesinglerfsg__intptr-string.html`
- source_url: https://docs-be.ni.com/bundle/rfsgplaybacklibrary-dotnet-api-ref/raw/resource/enus/nationalinstruments-modularinstruments-nirfsgplayback-nirfsgplayback-setscripttogeneratesinglerfsg__intptr-string.html
- document_id: `rfsgplaybacklibrary-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Sets the NI-RFSG driver to generate the waveforms specified in the script at the average power you configure on the NI-RFSG Power Level method. If you have enabled RF Blanking for the waveform, NI-RFSG is configured to correctly blank the output during the idle times of the waveform. SyntaxNamespace

### SetScriptToGenerateSingleRfsg(IntPtr, string)

Sets the NI-RFSG driver to generate the waveforms specified in the script at the average power you configure on the NI-RFSG Power Level method. If you have enabled RF Blanking for the waveform, NI-RFSG is configured to correctly blank the output during the idle times of the waveform.

#### Syntax

**Namespace:**[NationalInstruments.ModularInstruments.NIRfsgPlayback](nationalinstruments-modularinstruments-nirfsgplayback.html)

public static int SetScriptToGenerateSingleRfsg(IntPtr rfsgSession, string scriptText)

#### Remarks

- Sets the NI-RFSG Peak Power Adjustment method to the minimum value of the peak to average power ratio (PAPR) of the waveform in the script.
- Sets the NI-RFSG Pre-filter Gain method to the minimum value of the runtime scaling of the waveform in the script.

If the version of the waveform file is lesser than 2.0, the method,

- Sets the NI-RFSG Peak Power Adjustment method to the minimum value of the Headroom of the waveform in the script.
- Resets the NI-RFSG Pre-filter Gain method.

For the waveforms that have the RF blanking Enabled method set to True, this method also does the following:

- If the values of RF blanking marker source of all the waveforms are empty, then the first unused marker in the script is set as the RF Blanking Source.
- Modifies the script to add the waveform burst start and stop locations as the RF Blanking marker locations

For PXIe-5840/5841/5842 and PXIe-5830/5831/5832 devices,

- Sets the NI-RFSG Signal Bandwidth method to the maximum signal bandwidth of the waveform in the script, if you set the LO Offset Mode to **Auto**. If no signal bandwidth is found in any waveform of the script, the NI-RFSG Signal Bandwidth method is set to 0.8 times the Sample Rate.
- Resets the NI-RFSG Signal Bandwidth, if you set the LO Offset Mode to **No Offset**.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| rfsgSession | IntPtr | Identifies the instrument session. The rfsgSession handle is obtained from the NIRfsg.DangerousGetInstrumentHandle method. |
| scriptText | string | Specifies the script that controls the waveform generation. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

NIRfsgPlayback Class

<!--NI_TOPIC bundle=rfsgplaybacklibrary-dotnet-api-ref path=nationalinstruments-modularinstruments-nirfsgplayback-nirfsgplayback-storeautomaticsgsasharedlo__intptr-string-rfsgplaybackautomaticsgsasharedlo.html language=enus -->
## TOPIC 00043: StoreAutomaticSGSASharedLO(IntPtr, string, RfsgPlaybackAutomaticSGSASharedLO)

- bundle_id: `rfsgplaybacklibrary-dotnet-api-ref`
- source_path: `nationalinstruments-modularinstruments-nirfsgplayback-nirfsgplayback-storeautomaticsgsasharedlo__intptr-string-rfsgplaybackautomaticsgsasharedlo.html`
- source_url: https://docs-be.ni.com/bundle/rfsgplaybacklibrary-dotnet-api-ref/raw/resource/enus/nationalinstruments-modularinstruments-nirfsgplayback-nirfsgplayback-storeautomaticsgsasharedlo__intptr-string-rfsgplaybackautomaticsgsasharedlo.html
- document_id: `rfsgplaybacklibrary-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Stores whether the signal generator's LO signal can be shared on request by the RFmx driver. It is recommended to use Automatic sharing of local oscillator (LO) in test setups that use a vector signal transceiver (VST) with the NI-RFSG to generate a signal at the DUT's input and the RFmx driver to m

### StoreAutomaticSGSASharedLO(IntPtr, string, RfsgPlaybackAutomaticSGSASharedLO)

Stores whether the signal generator's LO signal can be shared on request by the RFmx driver. It is recommended to use Automatic sharing of local oscillator (LO) in test setups that use a vector signal transceiver (VST) with the NI-RFSG to generate a signal at the DUT's input and the RFmx driver to measure the signal at the DUT's output.

#### Syntax

**Namespace:**[NationalInstruments.ModularInstruments.NIRfsgPlayback](nationalinstruments-modularinstruments-nirfsgplayback.html)

public static int StoreAutomaticSGSASharedLO(IntPtr rfsgSession, string channelName, RfsgPlaybackAutomaticSGSASharedLO automaticSGSASharedLO)

#### Remarks

| PXIe-5840/5841/5842 | SG LO is shared with SA via an external path. Hence you must connect RF Out LO Out to RF In LO In using a cable. |
| --- | --- |
| PXIe-5830/5831/5832 | SG LO is shared with SA via an internal path. Hence the external cable connection is not required. |

1. Enable Automatic SG SA Shared LO on NI-RFSG Playback Library
2. Set the LOSource method to Automatic_SG_SA_Shared in RFmx
3. Configure other required settings on NI-RFSG and RFmx, including selecting waveforms
4. Initiate NI-RFSG
5. Initiate RFmx

Note

Measurement results might get affected while performing measurements in the RFmx driver if the signal analyzer measurement frequency span is wide enough to capture signal generator LO. In these cases, it is recommended to configure the **NIRfsgPlaybackLOOffsetMode** parameter to **NoOffset**.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| rfsgSession | IntPtr | Identifies the instrument session. The rfsgSession handle is obtained from the NIRfsg.DangerousGetInstrumentHandle method. |
| channelName | string | This parameter is reserved for future use. |
| automaticSGSASharedLO | RfsgPlaybackAutomaticSGSASharedLO | Specifies the access control of SG LO. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

NIRfsgPlayback Class

<!--NI_TOPIC bundle=rfsgplaybacklibrary-dotnet-api-ref path=nationalinstruments-modularinstruments-nirfsgplayback-nirfsgplayback-storewaveformburststartlocations__intptr-string-int_arr1.html language=enus -->
## TOPIC 00044: StoreWaveformBurstStartLocations(IntPtr, string, int[])

- bundle_id: `rfsgplaybacklibrary-dotnet-api-ref`
- source_path: `nationalinstruments-modularinstruments-nirfsgplayback-nirfsgplayback-storewaveformburststartlocations__intptr-string-int_arr1.html`
- source_url: https://docs-be.ni.com/bundle/rfsgplaybacklibrary-dotnet-api-ref/raw/resource/enus/nationalinstruments-modularinstruments-nirfsgplayback-nirfsgplayback-storewaveformburststartlocations__intptr-string-int_arr1.html
- document_id: `rfsgplaybacklibrary-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Stores the RF burst start locations, which you specify in the burstStartLocations parameter, in the NI-RFSG waveform database. SyntaxNamespace: NationalInstruments.ModularInstruments.NIRfsgPlaybackpublic static int StoreWaveformBurstStartLocations(IntPtr rfsgSession, string waveformName, int[] burst

### StoreWaveformBurstStartLocations(IntPtr, string, int[])

Stores the RF burst start locations, which you specify in the *burstStartLocations* parameter, in the NI-RFSG waveform database.

#### Syntax

**Namespace:**[NationalInstruments.ModularInstruments.NIRfsgPlayback](nationalinstruments-modularinstruments-nirfsgplayback.html)

public static int StoreWaveformBurstStartLocations(IntPtr rfsgSession, string waveformName, int[] burstStartLocations)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| rfsgSession | IntPtr | Identifies the instrument session. The rfsgSession handle is obtained from the NIRfsg.DangerousGetInstrumentHandle method. |
| waveformName | string | Specifies the name of the waveform for which you want to store the RF burst start locations. |
| burstStartLocations | int[] | Specifies the burst start locations to store in the NI-RFSG waveform database. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

NIRfsgPlayback Class

<!--NI_TOPIC bundle=rfsgplaybacklibrary-dotnet-api-ref path=nationalinstruments-modularinstruments-nirfsgplayback-nirfsgplayback-storewaveformburststoplocations__intptr-string-int_arr1.html language=enus -->
## TOPIC 00045: StoreWaveformBurstStopLocations(IntPtr, string, int[])

- bundle_id: `rfsgplaybacklibrary-dotnet-api-ref`
- source_path: `nationalinstruments-modularinstruments-nirfsgplayback-nirfsgplayback-storewaveformburststoplocations__intptr-string-int_arr1.html`
- source_url: https://docs-be.ni.com/bundle/rfsgplaybacklibrary-dotnet-api-ref/raw/resource/enus/nationalinstruments-modularinstruments-nirfsgplayback-nirfsgplayback-storewaveformburststoplocations__intptr-string-int_arr1.html
- document_id: `rfsgplaybacklibrary-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Stores the RF burst stop positions, which you specify in the burstStopLocations parameter, in the NI-RFSG waveform database. SyntaxNamespace: NationalInstruments.ModularInstruments.NIRfsgPlaybackpublic static int StoreWaveformBurstStopLocations(IntPtr rfsgSession, string waveformName, int[] burstSto

### StoreWaveformBurstStopLocations(IntPtr, string, int[])

Stores the RF burst stop positions, which you specify in the *burstStopLocations parameter*, in the NI-RFSG waveform database.

#### Syntax

**Namespace:**[NationalInstruments.ModularInstruments.NIRfsgPlayback](nationalinstruments-modularinstruments-nirfsgplayback.html)

public static int StoreWaveformBurstStopLocations(IntPtr rfsgSession, string waveformName, int[] burstStopLocations)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| rfsgSession | IntPtr | Identifies the instrument session. The rfsgSession handle is obtained from the NIRfsg.DangerousGetInstrumentHandle method. |
| waveformName | string | Specifies the name of the waveform for which you want to store the RF burst stop locations. |
| burstStopLocations | int[] | Specifies the burst stop locations to store in the NI-RFSG waveform database. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

NIRfsgPlayback Class

<!--NI_TOPIC bundle=rfsgplaybacklibrary-dotnet-api-ref path=nationalinstruments-modularinstruments-nirfsgplayback-nirfsgplayback-storewaveformlooffsetmode__intptr-string-nirfsgplaybacklooffsetmode.html language=enus -->
## TOPIC 00046: StoreWaveformLOOffsetMode(IntPtr, string, NIRfsgPlaybackLOOffsetMode)

- bundle_id: `rfsgplaybacklibrary-dotnet-api-ref`
- source_path: `nationalinstruments-modularinstruments-nirfsgplayback-nirfsgplayback-storewaveformlooffsetmode__intptr-string-nirfsgplaybacklooffsetmode.html`
- source_url: https://docs-be.ni.com/bundle/rfsgplaybacklibrary-dotnet-api-ref/raw/resource/enus/nationalinstruments-modularinstruments-nirfsgplayback-nirfsgplayback-storewaveformlooffsetmode__intptr-string-nirfsgplaybacklooffsetmode.html
- document_id: `rfsgplaybacklibrary-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Stores the LO offset mode value, which you specify in the value parameter, in the NI-RFSG waveform database. SyntaxNamespace: NationalInstruments.ModularInstruments.NIRfsgPlaybackpublic static int StoreWaveformLOOffsetMode(IntPtr rfsgSession, string waveformName, NIRfsgPlaybackLOOffsetMode value)Par

### StoreWaveformLOOffsetMode(IntPtr, string, NIRfsgPlaybackLOOffsetMode)

Stores the LO offset mode value, which you specify in the *value* parameter, in the NI-RFSG waveform database.

#### Syntax

**Namespace:**[NationalInstruments.ModularInstruments.NIRfsgPlayback](nationalinstruments-modularinstruments-nirfsgplayback.html)

public static int StoreWaveformLOOffsetMode(IntPtr rfsgSession, string waveformName, NIRfsgPlaybackLOOffsetMode value)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| rfsgSession | IntPtr | Identifies the instrument session. The rfsgSession handle is obtained from the NIRfsg.DangerousGetInstrumentHandle method. |
| waveformName | string | Specifies the waveform name for which you want to store the LO offset mode value. |
| value | NIRfsgPlaybackLOOffsetMode | Specifies the LO offset mode to store in the NI-RFSG database. The default value is Auto. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

NIRfsgPlayback Class

<!--NI_TOPIC bundle=rfsgplaybacklibrary-dotnet-api-ref path=nationalinstruments-modularinstruments-nirfsgplayback-nirfsgplayback-storewaveformpapr__intptr-string-double.html language=enus -->
## TOPIC 00047: StoreWaveformPapr(IntPtr, string, double)

- bundle_id: `rfsgplaybacklibrary-dotnet-api-ref`
- source_path: `nationalinstruments-modularinstruments-nirfsgplayback-nirfsgplayback-storewaveformpapr__intptr-string-double.html`
- source_url: https://docs-be.ni.com/bundle/rfsgplaybacklibrary-dotnet-api-ref/raw/resource/enus/nationalinstruments-modularinstruments-nirfsgplayback-nirfsgplayback-storewaveformpapr__intptr-string-double.html
- document_id: `rfsgplaybacklibrary-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Stores the peak to average power ratio (PAPR), which you specify in the PAPR parameter, in the NI-RFSG waveform database. SyntaxNamespace: NationalInstruments.ModularInstruments.NIRfsgPlaybackpublic static int StoreWaveformPapr(IntPtr rfsgSession, string waveformName, double papr)ParametersNameTypeD

### StoreWaveformPapr(IntPtr, string, double)

Stores the peak to average power ratio (PAPR), which you specify in the *PAPR* parameter, in the NI-RFSG waveform database.

#### Syntax

**Namespace:**[NationalInstruments.ModularInstruments.NIRfsgPlayback](nationalinstruments-modularinstruments-nirfsgplayback.html)

public static int StoreWaveformPapr(IntPtr rfsgSession, string waveformName, double papr)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| rfsgSession | IntPtr | Identifies the instrument session. The rfsgSession handle is obtained from the NIRfsg.DangerousGetInstrumentHandle method. |
| waveformName | string | Specifies the waveform name for which you want to store the PAPR. |
| papr | double | Specifies the PAPR to store in the NI-RFSG database. This value is expressed in dB. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

NIRfsgPlayback Class

<!--NI_TOPIC bundle=rfsgplaybacklibrary-dotnet-api-ref path=nationalinstruments-modularinstruments-nirfsgplayback-nirfsgplayback-storewaveformpeakpoweradjustment__intptr-string-double.html language=enus -->
## TOPIC 00048: StoreWaveformPeakPowerAdjustment(IntPtr, string, double)

- bundle_id: `rfsgplaybacklibrary-dotnet-api-ref`
- source_path: `nationalinstruments-modularinstruments-nirfsgplayback-nirfsgplayback-storewaveformpeakpoweradjustment__intptr-string-double.html`
- source_url: https://docs-be.ni.com/bundle/rfsgplaybacklibrary-dotnet-api-ref/raw/resource/enus/nationalinstruments-modularinstruments-nirfsgplayback-nirfsgplayback-storewaveformpeakpoweradjustment__intptr-string-double.html
- document_id: `rfsgplaybacklibrary-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Stores the peak power adjustment, which you specify in the peakPowerAdjustment parameter, in the RFSG waveform database. SyntaxNamespace: NationalInstruments.ModularInstruments.NIRfsgPlaybackpublic static int StoreWaveformPeakPowerAdjustment(IntPtr rfsgSession, string waveformName, double peakPowerA

### StoreWaveformPeakPowerAdjustment(IntPtr, string, double)

Stores the peak power adjustment, which you specify in the *peakPowerAdjustment* parameter, in the RFSG waveform database.

#### Syntax

**Namespace:**[NationalInstruments.ModularInstruments.NIRfsgPlayback](nationalinstruments-modularinstruments-nirfsgplayback.html)

public static int StoreWaveformPeakPowerAdjustment(IntPtr rfsgSession, string waveformName, double peakPowerAdjustment)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| rfsgSession | IntPtr | Identifies the instrument session. The rfsgSession handle is obtained from the NIRfsg.DangerousGetInstrumentHandle method. |
| waveformName | string | Specifies the name of the waveform for which you want to store the peak power adjustment. |
| peakPowerAdjustment | double | Specifies the peak power adjustment to store in the RFSG waveform database. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

NIRfsgPlayback Class

<!--NI_TOPIC bundle=rfsgplaybacklibrary-dotnet-api-ref path=nationalinstruments-modularinstruments-nirfsgplayback-nirfsgplayback-storewaveformrfblankingenabled__intptr-string-bool.html language=enus -->
## TOPIC 00049: StoreWaveformRFBlankingEnabled(IntPtr, string, bool)

- bundle_id: `rfsgplaybacklibrary-dotnet-api-ref`
- source_path: `nationalinstruments-modularinstruments-nirfsgplayback-nirfsgplayback-storewaveformrfblankingenabled__intptr-string-bool.html`
- source_url: https://docs-be.ni.com/bundle/rfsgplaybacklibrary-dotnet-api-ref/raw/resource/enus/nationalinstruments-modularinstruments-nirfsgplayback-nirfsgplayback-storewaveformrfblankingenabled__intptr-string-bool.html
- document_id: `rfsgplaybacklibrary-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Stores the RF blanking enabled value, which you specify in the rfBlankingEnabled parameter, in the NI-RFSG waveform database. SyntaxNamespace: NationalInstruments.ModularInstruments.NIRfsgPlaybackpublic static int StoreWaveformRFBlankingEnabled(IntPtr rfsgSession, string waveformName, bool rfBlankin

### StoreWaveformRFBlankingEnabled(IntPtr, string, bool)

Stores the RF blanking enabled value, which you specify in the *rfBlankingEnabled* parameter, in the NI-RFSG waveform database.

#### Syntax

**Namespace:**[NationalInstruments.ModularInstruments.NIRfsgPlayback](nationalinstruments-modularinstruments-nirfsgplayback.html)

public static int StoreWaveformRFBlankingEnabled(IntPtr rfsgSession, string waveformName, bool rfBlankingEnabled)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| rfsgSession | IntPtr | Identifies the instrument session. The rfsgSession handle is obtained from the NI-RFSG DangerousGetInstrumentHandle method. |
| waveformName | string | Specifies the name of the waveform for which you want to store the RF blanking enabled value. |
| rfBlankingEnabled | bool | Specifies the RF blanking enabled to store in the NI-RFSG waveform database. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

NIRfsgPlayback Class

<!--NI_TOPIC bundle=rfsgplaybacklibrary-dotnet-api-ref path=nationalinstruments-modularinstruments-nirfsgplayback-nirfsgplayback-storewaveformrfblankingmarkerlocations__intptr-string-int_arr1.html language=enus -->
## TOPIC 00050: StoreWaveformRFBlankingMarkerLocations(IntPtr, string, int[])

- bundle_id: `rfsgplaybacklibrary-dotnet-api-ref`
- source_path: `nationalinstruments-modularinstruments-nirfsgplayback-nirfsgplayback-storewaveformrfblankingmarkerlocations__intptr-string-int_arr1.html`
- source_url: https://docs-be.ni.com/bundle/rfsgplaybacklibrary-dotnet-api-ref/raw/resource/enus/nationalinstruments-modularinstruments-nirfsgplayback-nirfsgplayback-storewaveformrfblankingmarkerlocations__intptr-string-int_arr1.html
- document_id: `rfsgplaybacklibrary-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Stores the RF blanking marker positions, which you specify in the markerLocations parameter, in the NI-RFSG waveform database. SyntaxNamespace: NationalInstruments.ModularInstruments.NIRfsgPlaybackpublic static int StoreWaveformRFBlankingMarkerLocations(IntPtr rfsgSession, string waveformName, int[]

### StoreWaveformRFBlankingMarkerLocations(IntPtr, string, int[])

Stores the RF blanking marker positions, which you specify in the *markerLocations* parameter, in the NI-RFSG waveform database.

#### Syntax

**Namespace:**[NationalInstruments.ModularInstruments.NIRfsgPlayback](nationalinstruments-modularinstruments-nirfsgplayback.html)

public static int StoreWaveformRFBlankingMarkerLocations(IntPtr rfsgSession, string waveformName, int[] markerLocations)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| rfsgSession | IntPtr | Identifies the instrument session. The rfsgSession handle is obtained from the NIRfsg.DangerousGetInstrumentHandle method. |
| waveformName | string | Specifies the name of the waveform for which you want to store the RF blanking marker locations. |
| markerLocations | int[] | Specifies the RF blanking marker positions to store. It is an array of sample positions, within the waveform, of the marker events that you can use to toggle the RF blanking state. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

NIRfsgPlayback Class

<!--NI_TOPIC bundle=rfsgplaybacklibrary-dotnet-api-ref path=nationalinstruments-modularinstruments-nirfsgplayback-nirfsgplayback-storewaveformrfblankingmarkersource__intptr-string-string.html language=enus -->
## TOPIC 00051: StoreWaveformRFBlankingMarkerSource(IntPtr, string, string)

- bundle_id: `rfsgplaybacklibrary-dotnet-api-ref`
- source_path: `nationalinstruments-modularinstruments-nirfsgplayback-nirfsgplayback-storewaveformrfblankingmarkersource__intptr-string-string.html`
- source_url: https://docs-be.ni.com/bundle/rfsgplaybacklibrary-dotnet-api-ref/raw/resource/enus/nationalinstruments-modularinstruments-nirfsgplayback-nirfsgplayback-storewaveformrfblankingmarkersource__intptr-string-string.html
- document_id: `rfsgplaybacklibrary-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Stores the RF blanking marker source, which you specify in the markerSource parameter, in the NI-RFSG waveform database. SyntaxNamespace: NationalInstruments.ModularInstruments.NIRfsgPlaybackpublic static int StoreWaveformRFBlankingMarkerSource(IntPtr rfsgSession, string waveformName, string markerS

### StoreWaveformRFBlankingMarkerSource(IntPtr, string, string)

Stores the RF blanking marker source, which you specify in the *markerSource* parameter, in the NI-RFSG waveform database.

#### Syntax

**Namespace:**[NationalInstruments.ModularInstruments.NIRfsgPlayback](nationalinstruments-modularinstruments-nirfsgplayback.html)

public static int StoreWaveformRFBlankingMarkerSource(IntPtr rfsgSession, string waveformName, string markerSource)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| rfsgSession | IntPtr | Identifies the instrument session. The rfsgSession handle is obtained from the NIRfsg.DangerousGetInstrumentHandle method. |
| waveformName | string | Specifies the name of the waveform for which you want to store the RF blanking marker source. |
| markerSource | string | Specifies the RF blanking marker source to store in the NI-RFSG waveform database. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

NIRfsgPlayback Class

<!--NI_TOPIC bundle=rfsgplaybacklibrary-dotnet-api-ref path=nationalinstruments-modularinstruments-nirfsgplayback-nirfsgplayback-storewaveformruntimescaling__intptr-string-double.html language=enus -->
## TOPIC 00052: StoreWaveformRuntimeScaling(IntPtr, string, double)

- bundle_id: `rfsgplaybacklibrary-dotnet-api-ref`
- source_path: `nationalinstruments-modularinstruments-nirfsgplayback-nirfsgplayback-storewaveformruntimescaling__intptr-string-double.html`
- source_url: https://docs-be.ni.com/bundle/rfsgplaybacklibrary-dotnet-api-ref/raw/resource/enus/nationalinstruments-modularinstruments-nirfsgplayback-nirfsgplayback-storewaveformruntimescaling__intptr-string-double.html
- document_id: `rfsgplaybacklibrary-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Stores the runtime scaling value, which you specify in the runtimeScaling parameter, in the NI-RFSG waveform database. SyntaxNamespace: NationalInstruments.ModularInstruments.NIRfsgPlaybackpublic static int StoreWaveformRuntimeScaling(IntPtr rfsgSession, string waveformName, double runtimeScaling)Pa

### StoreWaveformRuntimeScaling(IntPtr, string, double)

Stores the runtime scaling value, which you specify in the *runtimeScaling* parameter, in the NI-RFSG waveform database.

#### Syntax

**Namespace:**[NationalInstruments.ModularInstruments.NIRfsgPlayback](nationalinstruments-modularinstruments-nirfsgplayback.html)

public static int StoreWaveformRuntimeScaling(IntPtr rfsgSession, string waveformName, double runtimeScaling)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| rfsgSession | IntPtr | Identifies the instrument session. The rfsgSession handle is obtained from the NIRfsg.DangerousGetInstrumentHandle method. |
| waveformName | string | Specifies the waveform name for which you want to store the runtime scaling value. |
| runtimeScaling | double | Specifies the runtime scaling value to store in the NI-RFSG database. This value is expressed in dB. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

NIRfsgPlayback Class

<!--NI_TOPIC bundle=rfsgplaybacklibrary-dotnet-api-ref path=nationalinstruments-modularinstruments-nirfsgplayback-nirfsgplayback-storewaveformsamplerate__intptr-string-double.html language=enus -->
## TOPIC 00053: StoreWaveformSampleRate(IntPtr, string, double)

- bundle_id: `rfsgplaybacklibrary-dotnet-api-ref`
- source_path: `nationalinstruments-modularinstruments-nirfsgplayback-nirfsgplayback-storewaveformsamplerate__intptr-string-double.html`
- source_url: https://docs-be.ni.com/bundle/rfsgplaybacklibrary-dotnet-api-ref/raw/resource/enus/nationalinstruments-modularinstruments-nirfsgplayback-nirfsgplayback-storewaveformsamplerate__intptr-string-double.html
- document_id: `rfsgplaybacklibrary-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Stores the sample rate, which you specify in the sampleRate parameter, in the NI-RFSG waveform database. SyntaxNamespace: NationalInstruments.ModularInstruments.NIRfsgPlaybackpublic static int StoreWaveformSampleRate(IntPtr rfsgSession, string waveformName, double sampleRate)ParametersNameTypeDescri

### StoreWaveformSampleRate(IntPtr, string, double)

Stores the sample rate, which you specify in the *sampleRate* parameter, in the NI-RFSG waveform database.

#### Syntax

**Namespace:**[NationalInstruments.ModularInstruments.NIRfsgPlayback](nationalinstruments-modularinstruments-nirfsgplayback.html)

public static int StoreWaveformSampleRate(IntPtr rfsgSession, string waveformName, double sampleRate)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| rfsgSession | IntPtr | Identifies the instrument session. The rfsgSession handle is obtained from the NIRfsg.DangerousGetInstrumentHandle method. |
| waveformName | string | Specifies the name of the waveform for which you want to store the sample rate. |
| sampleRate | double | Specifies the sampling rate to store in the NI-RFSG waveform database. This value is expressed in samples per second (S/s). |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

NIRfsgPlayback Class

<!--NI_TOPIC bundle=rfsgplaybacklibrary-dotnet-api-ref path=nationalinstruments-modularinstruments-nirfsgplayback-nirfsgplayback-storewaveformsignalbandwidth__intptr-string-double.html language=enus -->
## TOPIC 00054: StoreWaveformSignalBandwidth(IntPtr, string, double)

- bundle_id: `rfsgplaybacklibrary-dotnet-api-ref`
- source_path: `nationalinstruments-modularinstruments-nirfsgplayback-nirfsgplayback-storewaveformsignalbandwidth__intptr-string-double.html`
- source_url: https://docs-be.ni.com/bundle/rfsgplaybacklibrary-dotnet-api-ref/raw/resource/enus/nationalinstruments-modularinstruments-nirfsgplayback-nirfsgplayback-storewaveformsignalbandwidth__intptr-string-double.html
- document_id: `rfsgplaybacklibrary-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Stores the signal bandwidth, which you specify in the signalBandwidth parameter, in the NI-RFSG waveform database. SyntaxNamespace: NationalInstruments.ModularInstruments.NIRfsgPlaybackpublic static int StoreWaveformSignalBandwidth(IntPtr rfsgSession, string waveformName, double signalBandwidth)Para

### StoreWaveformSignalBandwidth(IntPtr, string, double)

Stores the signal bandwidth, which you specify in the *signalBandwidth* parameter, in the NI-RFSG waveform database.

#### Syntax

**Namespace:**[NationalInstruments.ModularInstruments.NIRfsgPlayback](nationalinstruments-modularinstruments-nirfsgplayback.html)

public static int StoreWaveformSignalBandwidth(IntPtr rfsgSession, string waveformName, double signalBandwidth)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| rfsgSession | IntPtr | Identifies the instrument session. The rfsgSession handle is obtained from the NIRfsg.DangerousGetInstrumentHandle method. |
| waveformName | string | Specifies the waveform name for which you want to store the signal bandwidth. |
| signalBandwidth | double | Specifies the signal bandwidth to store in the NI-RFSG waveform database. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

NIRfsgPlayback Class

<!--NI_TOPIC bundle=rfsgplaybacklibrary-dotnet-api-ref path=nationalinstruments-modularinstruments-nirfsgplayback-nirfsgplayback-storewaveformsize__intptr-string-int.html language=enus -->
## TOPIC 00055: StoreWaveformSize(IntPtr, string, int)

- bundle_id: `rfsgplaybacklibrary-dotnet-api-ref`
- source_path: `nationalinstruments-modularinstruments-nirfsgplayback-nirfsgplayback-storewaveformsize__intptr-string-int.html`
- source_url: https://docs-be.ni.com/bundle/rfsgplaybacklibrary-dotnet-api-ref/raw/resource/enus/nationalinstruments-modularinstruments-nirfsgplayback-nirfsgplayback-storewaveformsize__intptr-string-int.html
- document_id: `rfsgplaybacklibrary-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Stores the size of the waveform, which you specify in the waveformSize parameter, in the NI-RFSG waveform database. SyntaxNamespace: NationalInstruments.ModularInstruments.NIRfsgPlaybackpublic static int StoreWaveformSize(IntPtr rfsgSession, string waveformName, int waveformSize)ParametersNameTypeDe

### StoreWaveformSize(IntPtr, string, int)

Stores the size of the waveform, which you specify in the *waveformSize* parameter, in the NI-RFSG waveform database.

#### Syntax

**Namespace:**[NationalInstruments.ModularInstruments.NIRfsgPlayback](nationalinstruments-modularinstruments-nirfsgplayback.html)

public static int StoreWaveformSize(IntPtr rfsgSession, string waveformName, int waveformSize)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| rfsgSession | IntPtr | Identifies the instrument session. The rfsgSession handle is obtained from the NIRfsg.DangerousGetInstrumentHandle method. |
| waveformName | string | Specifies the name of the waveform for which you want to store the waveform size. |
| waveformSize | int | Specifies the size of the waveform to store in the NI-RFSG waveform database. This value is expressed in samples. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

NIRfsgPlayback Class

<!--NI_TOPIC bundle=rfsgplaybacklibrary-dotnet-api-ref path=nationalinstruments-modularinstruments-nirfsgplayback-nirfsgplayback.html language=enus -->
## TOPIC 00056: NIRfsgPlayback Class

- bundle_id: `rfsgplaybacklibrary-dotnet-api-ref`
- source_path: `nationalinstruments-modularinstruments-nirfsgplayback-nirfsgplayback.html`
- source_url: https://docs-be.ni.com/bundle/rfsgplaybacklibrary-dotnet-api-ref/raw/resource/enus/nationalinstruments-modularinstruments-nirfsgplayback-nirfsgplayback.html
- document_id: `rfsgplaybacklibrary-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Provides methods to generate the waveforms saved in a TDMS file using the NI-RFSG driver. Derives fromNoneSyntaxNamespace: NationalInstruments.ModularInstruments.NIRfsgPlaybackpublic class NIRfsgPlaybackMethodsNameDescriptionClearAllWaveforms(IntPtr)Deletes the waveforms from the NI-RFSG device memo

### NIRfsgPlayback Class

Provides methods to generate the waveforms saved in a TDMS file using the NI-RFSG driver.

#### Derives from

None

#### Syntax

**Namespace:**[NationalInstruments.ModularInstruments.NIRfsgPlayback](nationalinstruments-modularinstruments-nirfsgplayback.html)

public class NIRfsgPlayback

#### Methods

| Name | Description |
| --- | --- |
| ClearAllWaveforms(IntPtr) | Deletes the waveforms from the NI-RFSG device memory and removes all the waveform properties from the NI-RFSG waveform properties database for the specified device. |
| ClearWaveform(IntPtr, string) | Deletes the waveform from the NI-RFSG device memory and removes the waveform properties from the NI-RFSG waveform properties database for the specified device. |
| DownloadUserWaveform(IntPtr, string, ComplexWaveform< ComplexDouble >, bool) | Normalizes the input waveform and writes it into the NI RF vector signal generator. This VI computes the peak to average power ratio (PAPR) using the bursts in the waveform, stores the PAPR, sample rate, waveform size, and runtime scaling value of -1.5 dB in the NI-RFSG waveform database. |
| DownloadUserWaveform(IntPtr, string, ComplexWaveform< ComplexSingle >, bool) | Normalizes the input waveform and writes it into the NI RF vector signal generator. This VI computes the peak to average power ratio (PAPR) using the bursts in the waveform, stores the PAPR, sample rate, waveform size, and runtime scaling value of -1.5 dB in the NI-RFSG waveform database. |
| GetError(out int, out string) | Gets the latest error code and description. |
| ReadAndDownloadWaveformFromFile(IntPtr, string, string) | Reads a waveform from a TDMS file, and downloads it to the NI RF vector signal generator. |
| ReadAndDownloadWaveformsFromFile(IntPtr[], string, string) | Reads the waveforms from a TDMS file, and downloads one waveform into each of the NI RF vector signal generators. The first waveform in the TDMS file is downloaded to the first NI RF vector signal generator and so on, until all the waveforms are downloaded. |
| ReadBurstStartLocationsFromFile(string, int, ref int[]) | Returns the RF burst start locations stored in the file. This method uses the waveformIndex as the key to read the waveform property. |
| ReadBurstStopLocationsFromFile(string, int, ref int[]) | Returns the RF burst stop locations stored in the file. This method uses the waveformIndex as the key to read the waveform property. |
| ReadPaprFromFile(string, int, out double) | Returns the peak to average power ratio (PAPR) stored in the file. This method uses the waveformIndex as the key to read the waveform property. |
| ReadPeakPowerAdjustmentFromFile(string, int, out double) | Returns the value of the peak power adjustment stored in the file. This method uses the waveformIndex as the key to read the waveform properties. |
| ReadRFBlankingEnabledFromFile(string, int, out bool) | Returns the RF blanking enabled value stored in the file. This method uses the waveformIndex as the key to read the waveform properties. |
| ReadRFBlankingMarkerLocationsFromFile(string, int, ref int[]) | Returns the RF blanking marker locations stored in the file. This method uses the waveformIndex as the key to read the waveform property. |
| ReadRFBlankingMarkerSourceFromFile(string, int, out string) | Returns the RF blanking marker source stored in the file. This method uses the waveformIndex as the key to read the waveform property. |
| ReadRuntimeScalingFromFile(string, int, out double) | Returns the runtime scaling value stored in the file. This method uses the waveformIndex as the key to read the waveform property. |
| ReadSampleRateFromFile(string, int, out double) | Returns the sample rate stored in the file. This method uses the waveformIndex as the key to read the waveform property. |
| ReadSignalBandwidthFromFile(string, int, out double) | Returns the signal bandwidth stored in the file. This method uses the waveformIndex parameter as the key to retrieve the waveform property. |
| ReadWaveformFileVersionFromFile(string, out string) | Returns the waveform file version of the waveform stored in the file. |
| ReadWaveformFromFileByIndexComplex(string, int, ref ComplexWaveform< ComplexSingle >) | Reads the waveform from file and returns the waveform in an output parameter. |
| ReadWaveformFromFileByIndexComplex(string, int, ref ComplexWaveform< ComplexDouble >) | Reads the waveform from file and returns the waveform in an output parameter. |
| ReadWaveformFromFileComplex(string, ref ComplexWaveform< ComplexSingle >) | Reads the waveform from file and returns the waveform in an output parameter. |
| ReadWaveformFromFileComplex(string, ref ComplexWaveform< ComplexDouble >) | Reads the waveform from file and returns the waveform in an output parameter. |
| ReadWaveformsFromFileComplex(string, int, ref ComplexWaveform< ComplexSingle >[]) | Reads the waveforms from file, and returns the waveforms in an output parameter. |
| ReadWaveformsFromFileComplex(string, int, ref ComplexWaveform< ComplexDouble >[]) | Reads the waveforms from file, and returns the waveforms in an output parameter. |
| ReadWaveformSizeFromFile(string, int, out int) | Returns the size of the waveform stored in the file. This method uses the waveformIndex parameter as the key to read the waveform property. |
| RetrieveAutomaticSGSASharedLO(IntPtr, string, out RfsgPlaybackAutomaticSGSASharedLO) | Returns the value of automatic SG SA shared LO parameter. |
| RetrieveDownloadedWaveformNames(IntPtr, out string[]) | Returns the names of the waveforms that are stored in the NI-RFSG waveform database. |
| RetrieveWaveformBurstStartLocations(IntPtr, string, ref int[]) | Returns the RF burst start positions property stored in the NI-RFSG waveform database. This method uses the waveformName parameter as the key to retrieve the waveform property. |
| RetrieveWaveformBurstStopLocations(IntPtr, string, ref int[]) | Returns the RF burst stop positions property stored in the NI-RFSG waveform database. This method uses the waveformName parameter as the key to retrieve the waveform property. |
| RetrieveWaveformFileVersion(IntPtr, string, out string) | Returns the waveform file version stored in the NI-RFSG waveform database. This method uses the waveformName parameter as the key to retrieve the waveform property. |
| RetrieveWaveformLOOffsetMode(IntPtr, string, out NIRfsgPlaybackLOOffsetMode) | Returns the LO offset mode value stored in the NI-RFSG waveform database. This method uses the waveformName parameter as the key to retrieve the waveform property. |
| RetrieveWaveformPapr(IntPtr, string, out double) | Returns the peak to average power ratio (PAPR) stored in the NI-RFSG waveform database. This method uses the waveformName parameter as the key to retrieve the waveform property. |
| RetrieveWaveformPeakPowerAdjustment(IntPtr, string, out double) | Returns the value of the Peak Power Adjustment property stored in the NI-RFSG waveform database. This method uses the waveformName parameter as the key to retrieve the waveform property. |
| RetrieveWaveformRFBlankingEnabled(IntPtr, string, out bool) | Returns the RF blanking enabled value stored in the NI-RFSG waveform database. This method uses the waveformName parameter as the key to retrieve the waveform properties. |
| RetrieveWaveformRFBlankingMarkerLocations(IntPtr, string, ref int[]) | Returns the RF blanking marker positions property stored in the NI-RFSG waveform database. This method uses the waveformName as the key to retrieve the waveform property. |
| RetrieveWaveformRFBlankingMarkerSource(IntPtr, string, out string) | Returns the RF blanking marker source stored in the NI-RFSG waveform database. This method uses the waveformName parameter as the key to retrieve the waveform property. |
| RetrieveWaveformRuntimeScaling(IntPtr, string, out double) | Returns the runtime scaling value stored in the NI-RFSG waveform database. This method uses the waveformName parameter as the key to retrieve the waveform property. |
| RetrieveWaveformSampleRate(IntPtr, string, out double) | Returns the sample rate stored in the NI-RFSG waveform database. This method uses the waveformName parameter as the key to retrieve the waveform properties. |
| RetrieveWaveformSignalBandwidth(IntPtr, string, out double) | Returns the signal bandwidth stored in the NI-RFSG waveform database. This method uses the waveformName parameter as the key to retrieve the waveform property. |
| RetrieveWaveformSize(IntPtr, string, out int) | Returns the size of the waveform stored in the NI-RFSG waveform database. This method uses the waveformName parameter as the key to retrieve the waveform property. |
| SetScriptToGenerateMultipleRfsg(IntPtr[], string) | Sets the NI-RFSG driver to generate the waveforms specified in the script at the average power you configure on the NI-RFSG Power Level method. If you have enabled RF Blanking for the waveform, NI-RFSG is configured to correctly blank the output during the idle times of the waveform. |
| SetScriptToGenerateSingleRfsg(IntPtr, string) | Sets the NI-RFSG driver to generate the waveforms specified in the script at the average power you configure on the NI-RFSG Power Level method. If you have enabled RF Blanking for the waveform, NI-RFSG is configured to correctly blank the output during the idle times of the waveform. |
| StoreAutomaticSGSASharedLO(IntPtr, string, RfsgPlaybackAutomaticSGSASharedLO) | Stores whether the signal generator's LO signal can be shared on request by the RFmx driver. It is recommended to use Automatic sharing of local oscillator (LO) in test setups that use a vector signal transceiver (VST) with the NI-RFSG to generate a signal at the DUT's input and the RFmx driver to measure the signal at the DUT's output. |
| StoreWaveformBurstStartLocations(IntPtr, string, int[]) | Stores the RF burst start locations, which you specify in the burstStartLocations parameter, in the NI-RFSG waveform database. |
| StoreWaveformBurstStopLocations(IntPtr, string, int[]) | Stores the RF burst stop positions, which you specify in the burstStopLocations parameter, in the NI-RFSG waveform database. |
| StoreWaveformLOOffsetMode(IntPtr, string, NIRfsgPlaybackLOOffsetMode) | Stores the LO offset mode value, which you specify in the value parameter, in the NI-RFSG waveform database. |
| StoreWaveformPapr(IntPtr, string, double) | Stores the peak to average power ratio (PAPR), which you specify in the PAPR parameter, in the NI-RFSG waveform database. |
| StoreWaveformPeakPowerAdjustment(IntPtr, string, double) | Stores the peak power adjustment, which you specify in the peakPowerAdjustment parameter, in the RFSG waveform database. |
| StoreWaveformRFBlankingEnabled(IntPtr, string, bool) | Stores the RF blanking enabled value, which you specify in the rfBlankingEnabled parameter, in the NI-RFSG waveform database. |
| StoreWaveformRFBlankingMarkerLocations(IntPtr, string, int[]) | Stores the RF blanking marker positions, which you specify in the markerLocations parameter, in the NI-RFSG waveform database. |
| StoreWaveformRFBlankingMarkerSource(IntPtr, string, string) | Stores the RF blanking marker source, which you specify in the markerSource parameter, in the NI-RFSG waveform database. |
| StoreWaveformRuntimeScaling(IntPtr, string, double) | Stores the runtime scaling value, which you specify in the runtimeScaling parameter, in the NI-RFSG waveform database. |
| StoreWaveformSampleRate(IntPtr, string, double) | Stores the sample rate, which you specify in the sampleRate parameter, in the NI-RFSG waveform database. |
| StoreWaveformSignalBandwidth(IntPtr, string, double) | Stores the signal bandwidth, which you specify in the signalBandwidth parameter, in the NI-RFSG waveform database. |
| StoreWaveformSize(IntPtr, string, int) | Stores the size of the waveform, which you specify in the waveformSize parameter, in the NI-RFSG waveform database. |

Parent topic:

NationalInstruments.ModularInstruments.NIRfsgPlayback

<!--NI_TOPIC bundle=rfsgplaybacklibrary-dotnet-api-ref path=nationalinstruments-modularinstruments-nirfsgplayback-nirfsgplaybacklooffsetmode.html language=enus -->
## TOPIC 00057: NIRfsgPlaybackLOOffsetMode Enumeration

- bundle_id: `rfsgplaybacklibrary-dotnet-api-ref`
- source_path: `nationalinstruments-modularinstruments-nirfsgplayback-nirfsgplaybacklooffsetmode.html`
- source_url: https://docs-be.ni.com/bundle/rfsgplaybacklibrary-dotnet-api-ref/raw/resource/enus/nationalinstruments-modularinstruments-nirfsgplayback-nirfsgplaybacklooffsetmode.html
- document_id: `rfsgplaybacklibrary-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the LO offset mode to store in the NI-RFSG waveform database. The following enums define the behavior of the SetScriptToGenerateMultipleRfsgMethod and SetScriptToGenerateSingleRfsgMethod methods on PXIe-5840/5841/5842 and PXIe-5830/5831/5832. SyntaxNamespace: NationalInstruments.ModularIns

### NIRfsgPlaybackLOOffsetMode Enumeration

Specifies the LO offset mode to store in the NI-RFSG waveform database. The following enums define the behavior of the SetScriptToGenerateMultipleRfsgMethod and SetScriptToGenerateSingleRfsgMethod methods on PXIe-5840/5841/5842 and PXIe-5830/5831/5832.

#### Syntax

**Namespace:**[NationalInstruments.ModularInstruments.NIRfsgPlayback](nationalinstruments-modularinstruments-nirfsgplayback.html)

public enum NIRfsgPlaybackLOOffsetMode

#### Remarks

Note

Measurement results might get affected while performing measurements in the RFmx driver if the signal analyzer measurement frequency span is wide enough to capture signal generator LO. In these cases, it is recommended to configure the **NIRfsgPlaybackLOOffsetMode** parameter to **NoOffset**.

#### Members

| Name | Value | Description |
| --- | --- | --- |
| Auto | 0 | Sets the signal bandwidth value to the NI-RFSG SignalBandwidth property, and resets the NI-RFSG UpconverterFrequencyOffset property. |
| NoOffset | 1 | Resets the values of the NI-RFSG SignalBandwidth and NI-RFSG UpconverterFrequencyOffset properties. |
| Disabled | 2 | Does not set the NI-RFSG SignalBandwidth property or reset the NI-RFSG UpconverterFrequencyOffset property. |

Parent topic:

NationalInstruments.ModularInstruments.NIRfsgPlayback

<!--NI_TOPIC bundle=rfsgplaybacklibrary-dotnet-api-ref path=nationalinstruments-modularinstruments-nirfsgplayback-rfsgplaybackautomaticsgsasharedlo.html language=enus -->
## TOPIC 00058: RfsgPlaybackAutomaticSGSASharedLO Enumeration

- bundle_id: `rfsgplaybacklibrary-dotnet-api-ref`
- source_path: `nationalinstruments-modularinstruments-nirfsgplayback-rfsgplaybackautomaticsgsasharedlo.html`
- source_url: https://docs-be.ni.com/bundle/rfsgplaybacklibrary-dotnet-api-ref/raw/resource/enus/nationalinstruments-modularinstruments-nirfsgplayback-rfsgplaybackautomaticsgsasharedlo.html
- document_id: `rfsgplaybacklibrary-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: specifies the access control of NI-RFSG LO Out Export. The default value is Disabled. The following enums define the behavior of the niRFSGPlayback Set Script to Generate VI. SyntaxNamespace: NationalInstruments.ModularInstruments.NIRfsgPlaybackpublic enum RfsgPlaybackAutomaticSGSASharedLOMembersNam

### RfsgPlaybackAutomaticSGSASharedLO Enumeration

specifies the access control of NI-RFSG LO Out Export. The default value is **Disabled**. The following enums define the behavior of the niRFSGPlayback Set Script to Generate VI.

#### Syntax

**Namespace:**[NationalInstruments.ModularInstruments.NIRfsgPlayback](nationalinstruments-modularinstruments-nirfsgplayback.html)

public enum RfsgPlaybackAutomaticSGSASharedLO

#### Members

| Name | Value | Description |
| --- | --- | --- |
| Disabled | 0 | Disables automatic sharing the SG LO with SA. |
| Enabled | 1 | Enables automatic sharing the SG LO with SA. |

Parent topic:

NationalInstruments.ModularInstruments.NIRfsgPlayback

<!--NI_TOPIC bundle=rfsgplaybacklibrary-dotnet-api-ref path=nationalinstruments-modularinstruments-nirfsgplayback-rfsgplaybackconstants-marker0.html language=enus -->
## TOPIC 00059: Marker0

- bundle_id: `rfsgplaybacklibrary-dotnet-api-ref`
- source_path: `nationalinstruments-modularinstruments-nirfsgplayback-rfsgplaybackconstants-marker0.html`
- source_url: https://docs-be.ni.com/bundle/rfsgplaybacklibrary-dotnet-api-ref/raw/resource/enus/nationalinstruments-modularinstruments-nirfsgplayback-rfsgplaybackconstants-marker0.html
- document_id: `rfsgplaybacklibrary-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the source when RF blanking is tied to marker0. SyntaxNamespace: NationalInstruments.ModularInstruments.NIRfsgPlaybackpublic const string Marker0

### Marker0

Specifies the source when RF blanking is tied to marker0.

#### Syntax

**Namespace:**[NationalInstruments.ModularInstruments.NIRfsgPlayback](nationalinstruments-modularinstruments-nirfsgplayback.html)

public const string Marker0

Parent topic:

RfsgPlaybackConstants Class

<!--NI_TOPIC bundle=rfsgplaybacklibrary-dotnet-api-ref path=nationalinstruments-modularinstruments-nirfsgplayback-rfsgplaybackconstants-marker1.html language=enus -->
## TOPIC 00060: Marker1

- bundle_id: `rfsgplaybacklibrary-dotnet-api-ref`
- source_path: `nationalinstruments-modularinstruments-nirfsgplayback-rfsgplaybackconstants-marker1.html`
- source_url: https://docs-be.ni.com/bundle/rfsgplaybacklibrary-dotnet-api-ref/raw/resource/enus/nationalinstruments-modularinstruments-nirfsgplayback-rfsgplaybackconstants-marker1.html
- document_id: `rfsgplaybacklibrary-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the source when RF blanking is tied to marker1. SyntaxNamespace: NationalInstruments.ModularInstruments.NIRfsgPlaybackpublic const string Marker1

### Marker1

Specifies the source when RF blanking is tied to marker1.

#### Syntax

**Namespace:**[NationalInstruments.ModularInstruments.NIRfsgPlayback](nationalinstruments-modularinstruments-nirfsgplayback.html)

public const string Marker1

Parent topic:

RfsgPlaybackConstants Class

<!--NI_TOPIC bundle=rfsgplaybacklibrary-dotnet-api-ref path=nationalinstruments-modularinstruments-nirfsgplayback-rfsgplaybackconstants-marker2.html language=enus -->
## TOPIC 00061: Marker2

- bundle_id: `rfsgplaybacklibrary-dotnet-api-ref`
- source_path: `nationalinstruments-modularinstruments-nirfsgplayback-rfsgplaybackconstants-marker2.html`
- source_url: https://docs-be.ni.com/bundle/rfsgplaybacklibrary-dotnet-api-ref/raw/resource/enus/nationalinstruments-modularinstruments-nirfsgplayback-rfsgplaybackconstants-marker2.html
- document_id: `rfsgplaybacklibrary-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the source when RF blanking is tied to marker2. SyntaxNamespace: NationalInstruments.ModularInstruments.NIRfsgPlaybackpublic const string Marker2

### Marker2

Specifies the source when RF blanking is tied to marker2.

#### Syntax

**Namespace:**[NationalInstruments.ModularInstruments.NIRfsgPlayback](nationalinstruments-modularinstruments-nirfsgplayback.html)

public const string Marker2

Parent topic:

RfsgPlaybackConstants Class

<!--NI_TOPIC bundle=rfsgplaybacklibrary-dotnet-api-ref path=nationalinstruments-modularinstruments-nirfsgplayback-rfsgplaybackconstants-marker3.html language=enus -->
## TOPIC 00062: Marker3

- bundle_id: `rfsgplaybacklibrary-dotnet-api-ref`
- source_path: `nationalinstruments-modularinstruments-nirfsgplayback-rfsgplaybackconstants-marker3.html`
- source_url: https://docs-be.ni.com/bundle/rfsgplaybacklibrary-dotnet-api-ref/raw/resource/enus/nationalinstruments-modularinstruments-nirfsgplayback-rfsgplaybackconstants-marker3.html
- document_id: `rfsgplaybacklibrary-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the source when RF blanking is tied to marker3. SyntaxNamespace: NationalInstruments.ModularInstruments.NIRfsgPlaybackpublic const string Marker3

### Marker3

Specifies the source when RF blanking is tied to marker3.

#### Syntax

**Namespace:**[NationalInstruments.ModularInstruments.NIRfsgPlayback](nationalinstruments-modularinstruments-nirfsgplayback.html)

public const string Marker3

Parent topic:

RfsgPlaybackConstants Class

<!--NI_TOPIC bundle=rfsgplaybacklibrary-dotnet-api-ref path=nationalinstruments-modularinstruments-nirfsgplayback-rfsgplaybackconstants.html language=enus -->
## TOPIC 00063: RfsgPlaybackConstants Class

- bundle_id: `rfsgplaybacklibrary-dotnet-api-ref`
- source_path: `nationalinstruments-modularinstruments-nirfsgplayback-rfsgplaybackconstants.html`
- source_url: https://docs-be.ni.com/bundle/rfsgplaybacklibrary-dotnet-api-ref/raw/resource/enus/nationalinstruments-modularinstruments-nirfsgplayback-rfsgplaybackconstants.html
- document_id: `rfsgplaybacklibrary-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Provides string constants. Derives fromNoneSyntaxNamespace: NationalInstruments.ModularInstruments.NIRfsgPlaybackpublic class RfsgPlaybackConstantsFieldsNameDescriptionMarker0Specifies the source when RF blanking is tied to marker0. Marker1Specifies the source when RF blanking is tied to marker1. Ma

### RfsgPlaybackConstants Class

Provides string constants.

#### Derives from

None

#### Syntax

**Namespace:**[NationalInstruments.ModularInstruments.NIRfsgPlayback](nationalinstruments-modularinstruments-nirfsgplayback.html)

public class RfsgPlaybackConstants

#### Fields

| Name | Description |
| --- | --- |
| Marker0 | Specifies the source when RF blanking is tied to marker0. |
| Marker1 | Specifies the source when RF blanking is tied to marker1. |
| Marker2 | Specifies the source when RF blanking is tied to marker2. |
| Marker3 | Specifies the source when RF blanking is tied to marker3. |

Parent topic:

NationalInstruments.ModularInstruments.NIRfsgPlayback

<!--NI_TOPIC bundle=rfsgplaybacklibrary-dotnet-api-ref path=nationalinstruments-modularinstruments-nirfsgplayback.html language=enus -->
## TOPIC 00064: NationalInstruments.ModularInstruments.NIRfsgPlayback

- bundle_id: `rfsgplaybacklibrary-dotnet-api-ref`
- source_path: `nationalinstruments-modularinstruments-nirfsgplayback.html`
- source_url: https://docs-be.ni.com/bundle/rfsgplaybacklibrary-dotnet-api-ref/raw/resource/enus/nationalinstruments-modularinstruments-nirfsgplayback.html
- document_id: `rfsgplaybacklibrary-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: ClassesNameDescriptionNIRfsgPlaybackProvides methods to generate the waveforms saved in a TDMS file using the NI-RFSG driver. RfsgPlaybackConstantsProvides string constants. InterfacesNoneStructuresNoneEnumerationsNameDescriptionNIRfsgPlaybackLOOffsetModeSpecifies the LO offset mode to store in the

### NationalInstruments.ModularInstruments.NIRfsgPlayback

#### Classes

| Name | Description |
| --- | --- |
| NIRfsgPlayback | Provides methods to generate the waveforms saved in a TDMS file using the NI-RFSG driver. |
| RfsgPlaybackConstants | Provides string constants. |

#### Interfaces

None

#### Structures

None

#### Enumerations

| Name | Description |
| --- | --- |
| NIRfsgPlaybackLOOffsetMode | Specifies the LO offset mode to store in the NI-RFSG waveform database. The following enums define the behavior of the SetScriptToGenerateMultipleRfsgMethod and SetScriptToGenerateSingleRfsgMethod methods on PXIe-5840/5841/5842 and PXIe-5830/5831/5832. |
| RfsgPlaybackAutomaticSGSASharedLO | specifies the access control of NI-RFSG LO Out Export. The default value is Disabled. The following enums define the behavior of the niRFSGPlayback Set Script to Generate VI. |

#### Delegates

None
