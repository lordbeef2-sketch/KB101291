# NI DOCUMENT BUNDLE: rfsgplaybacklibrary-c-api-ref

<!--NI_BUNDLE_CHUNK bundle=rfsgplaybacklibrary-c-api-ref start=1 end=70 -->
<!--NI_TOPIC bundle=rfsgplaybacklibrary-c-api-ref path=group____root__ni_r_f_s_g_playback__attributes.html language=enus -->
## TOPIC 00001: Attributes

- bundle_id: `rfsgplaybacklibrary-c-api-ref`
- source_path: `group____root__ni_r_f_s_g_playback__attributes.html`
- source_url: https://docs-be.ni.com/bundle/rfsgplaybacklibrary-c-api-ref/raw/resource/enus/group____root__ni_r_f_s_g_playback__attributes.html
- document_id: `rfsgplaybacklibrary-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: GroupsNoneGroup membersNoneAttachmentsNone

### Attributes

#### Groups

None

#### Group members

None

#### Attachments

None

Parent topic:

niRFSGPlayback.h

<!--NI_TOPIC bundle=rfsgplaybacklibrary-c-api-ref path=group____root__ni_r_f_s_g_playback__functions.html language=enus -->
## TOPIC 00002: Functions

- bundle_id: `rfsgplaybacklibrary-c-api-ref`
- source_path: `group____root__ni_r_f_s_g_playback__functions.html`
- source_url: https://docs-be.ni.com/bundle/rfsgplaybacklibrary-c-api-ref/raw/resource/enus/group____root__ni_r_f_s_g_playback__functions.html
- document_id: `rfsgplaybacklibrary-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: GroupsAdvancedUtilityGroup membersNameDescriptionniRFSGPlayback_ClearAllWaveformsDeletes all the waveforms from NI-RFSG device memory and removes all the waveform property from the NI-RFSG waveform database for the specified device. niRFSGPlayback_ClearWaveformDeletes the waveform from NI-RFSG devic

### Functions

#### Groups

- Advanced
- Utility

#### Group members

| Name | Description |
| --- | --- |
| niRFSGPlayback_ClearAllWaveforms | Deletes all the waveforms from NI-RFSG device memory and removes all the waveform property from the NI-RFSG waveform database for the specified device. |
| niRFSGPlayback_ClearWaveform | Deletes the waveform from NI-RFSG device memory and removes the waveform property from the NI-RFSG waveform database for the specified device. |
| niRFSGPlayback_DownloadUserWaveformComplexF32 | Normalizes the input waveform and writes it into the NI RF vector signal generator. This VI computes the peak to average power ratio (PAPR) using the bursts in the waveform, stores the PAPR, sample rate, waveform size, and runtime scaling value of -1.5 dB in the NI-RFSG waveform database. |
| niRFSGPlayback_DownloadUserWaveformComplexF32Split | Normalizes the in-phase and quadrature-phase part of the input waveform and writes it into the NI RF vector signal generator. This function computes the peak to average power ratio (PAPR) using the bursts in the waveform, stores the PAPR, sample rate, waveform size, and runtime scaling value of -1.5 dB in the NI-RFSG waveform database. |
| niRFSGPlayback_DownloadUserWaveformComplexF64 | Normalizes the input waveform and writes it into the NI RF vector signal generator. This VI computes the peak to average power ratio (PAPR) using the bursts in the waveform, stores the PAPR, sample rate, waveform size, and runtime scaling value of -1.5 dB in the NI-RFSG waveform database. |
| niRFSGPlayback_DownloadUserWaveformComplexF64Split | Normalizes the in-phase and quadrature-phase part of the input waveform and writes it into the NI RF vector signal generator. This VI computes the peak to average power ratio (PAPR) using the bursts in the waveform, stores the PAPR, sample rate, waveform size, and runtime scaling value of -1.5 dB in the NI-RFSG waveform database. |
| niRFSGPlayback_GetError | Gets the latest error code and description. |
| niRFSGPlayback_ReadAndDownloadWaveformFromFile | Reads a waveform from a TDMS file, and downloads it to the NI RF vector signal generator. This function reads the following information from the TDMS file and writes it into the NI-RFSG waveform database: |
| niRFSGPlayback_ReadAndDownloadWaveformsFromFile | Reads the waveforms from a TDMS file, and downloads one waveform into each of the NI RF vector signal generators. The first waveform in the TDMS file is downloaded to the first NI RF vector signal generator and so on, until all the waveforms are downloaded. This function reads the following information from the TDMS file and writes it into the NI-RFSG waveform database: |
| niRFSGPlayback_ReadWaveformFromFileByIndexComplexF32 | Reads the waveform from file and returns the waveform in an output parameter. |
| niRFSGPlayback_ReadWaveformFromFileByIndexComplexF32Split | Reads the waveform from file and returns the in-phase and quadrature-phase part of the waveform in the output parameters. |
| niRFSGPlayback_ReadWaveformFromFileByIndexComplexF64 | Reads the waveform from file and returns the waveform in an output parameter. |
| niRFSGPlayback_ReadWaveformFromFileByIndexComplexF64Split | Reads the waveform from file and returns the in-phase and quadrature-phase part of the waveform in the output parameters. |
| niRFSGPlayback_ReadWaveformFromFileComplexF32 | Reads the waveform from file and returns the waveform in an output parameter. |
| niRFSGPlayback_ReadWaveformFromFileComplexF32Split | Reads the waveform from file and returns the in-phase and quadrature-phase part of the waveform in the output parameters. |
| niRFSGPlayback_ReadWaveformFromFileComplexF64 | Reads the waveform from the file and returns the waveform in an output parameter. |
| niRFSGPlayback_ReadWaveformFromFileComplexF64Split | Reads the waveform from file and returns the in-phase and quadrature-phase part of the waveform in the output parameters. |
| niRFSGPlayback_ReadWaveformsFromFileComplexF32 | Reads the waveforms from file and returns the waveforms in an output parameter. |
| niRFSGPlayback_ReadWaveformsFromFileComplexF32Split | Reads the waveforms from file and returns the in-phase and quadrature-phase part of the waveforms in the output parameters. |
| niRFSGPlayback_ReadWaveformsFromFileComplexF64 | Reads the waveforms from file and returns the waveforms in an output parameter. |
| niRFSGPlayback_ReadWaveformsFromFileComplexF64Split | Reads the waveforms from file and returns the in-phase and quadrature-phase part of the waveforms in the output parameters. |
| niRFSGPlayback_SetScriptToGenerateMultipleRFSG | Configures the NI-RFSG driver to generate the waveforms specified in the script at the average power you configure on the NIRFSG_ATTR_POWER_LEVEL_TYPE attribute. If you have enabled RF Blanking for the waveform, NI-RFSG is configured to correctly blank the output during the idle times of the waveform. |
| niRFSGPlayback_SetScriptToGenerateSingleRFSG | Configures the NI-RFSG driver to generate the waveforms specified in the script at the average power you configure on the NIRFSG_ATTR_POWER_LEVEL_TYPE attribute. If you have enabled RF Blanking for the waveform, NI-RFSG is configured to correctly blank the output during the idle times of the waveform. |

#### Attachments

None

Parent topic:

niRFSGPlayback.h

<!--NI_TOPIC bundle=rfsgplaybacklibrary-c-api-ref path=group____root__ni_r_f_s_g_playback__functions_1ga04b41bd51b6c523a5e3dfc9eb1f7b688.html language=enus -->
## TOPIC 00003: niRFSGPlayback_ReadWaveformFromFileByIndexComplexF64Split

- bundle_id: `rfsgplaybacklibrary-c-api-ref`
- source_path: `group____root__ni_r_f_s_g_playback__functions_1ga04b41bd51b6c523a5e3dfc9eb1f7b688.html`
- source_url: https://docs-be.ni.com/bundle/rfsgplaybacklibrary-c-api-ref/raw/resource/enus/group____root__ni_r_f_s_g_playback__functions_1ga04b41bd51b6c523a5e3dfc9eb1f7b688.html
- document_id: `rfsgplaybacklibrary-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Reads the waveform from file and returns the in-phase and quadrature-phase part of the waveform in the output parameters. Syntaxint32 __stdcall niRFSGPlayback_ReadWaveformFromFileByIndexComplexF64Split(ViConstString filePath, ViInt32 waveformIndex, ViInt32 outputWaveformBufferSize, ViReal64 t0, ViRe

### niRFSGPlayback_ReadWaveformFromFileByIndexComplexF64Split

Reads the waveform from file and returns the in-phase and quadrature-phase part of the waveform in the output parameters.

#### Syntax

int32 __stdcall niRFSGPlayback_ReadWaveformFromFileByIndexComplexF64Split(ViConstString filePath, ViInt32 waveformIndex, ViInt32 outputWaveformBufferSize, ViReal64 t0, ViReal64 dt, ViReal64[] i, ViReal64[] q, ViInt32 actualWaveformSize)

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| filePath | [in] | ViConstString | Specifies the absolute path to the TDMS file from which the playback library reads the waveforms. |
| waveformIndex | [in] | ViInt32 | Specifies the index of the waveform that you want to read from the TDMS file. |
| outputWaveformBufferSize | [in] | ViInt32 | Specifies the size of the outputWaveform array. Set the outputWaveformBufferSize parameter to 0 to get the size of the outputWaveform array in the actualWaveformSize parameter. |
| t0 | [out] | ViReal64 | This element should be ignored. |
| dt | [out] | ViReal64 | Returns the inverse of the sample rate of the waveform. |
| i | [out] | ViReal64[] | Returns the in-phase part of the waveform. |
| q | [out] | ViReal64[] | Returns the quadrature-phase part of the waveform. |
| actualWaveformSize | [out] | ViInt32 | Returns the actual size of the array, if you pass NULL to all output array parameters, and set the outputWaveformBufferSize parameter to 0. |

#### Returns

Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred. To obtain a text description of the status code and additional information about the error condition, call the [niRFSGPlayback_GetError](group____root__ni_r_f_s_g_playback__functions_1ga5985403bcf5416e344ce264b3a73fc4a.html) function. The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

Functions

<!--NI_TOPIC bundle=rfsgplaybacklibrary-c-api-ref path=group____root__ni_r_f_s_g_playback__functions_1ga1fdb7b1437a0d909998476d0d5ad27de.html language=enus -->
## TOPIC 00004: niRFSGPlayback_ReadWaveformFromFileComplexF32Split

- bundle_id: `rfsgplaybacklibrary-c-api-ref`
- source_path: `group____root__ni_r_f_s_g_playback__functions_1ga1fdb7b1437a0d909998476d0d5ad27de.html`
- source_url: https://docs-be.ni.com/bundle/rfsgplaybacklibrary-c-api-ref/raw/resource/enus/group____root__ni_r_f_s_g_playback__functions_1ga1fdb7b1437a0d909998476d0d5ad27de.html
- document_id: `rfsgplaybacklibrary-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Reads the waveform from file and returns the in-phase and quadrature-phase part of the waveform in the output parameters. Syntaxint32 __stdcall niRFSGPlayback_ReadWaveformFromFileComplexF32Split(ViConstString filePath, ViInt32 outputWaveformBufferSize, ViReal64 t0, ViReal64 dt, ViReal32[] i, ViReal3

### niRFSGPlayback_ReadWaveformFromFileComplexF32Split

Reads the waveform from file and returns the in-phase and quadrature-phase part of the waveform in the output parameters.

#### Syntax

int32 __stdcall niRFSGPlayback_ReadWaveformFromFileComplexF32Split(ViConstString filePath, ViInt32 outputWaveformBufferSize, ViReal64 t0, ViReal64 dt, ViReal32[] i, ViReal32[] q, ViInt32 actualWaveformSize)

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| filePath | [in] | ViConstString | Specifies the absolute path to the TDMS file from which the playback library reads the waveforms. |
| outputWaveformBufferSize | [in] | ViInt32 | Specifies the size of the outputWaveform array. Set the outputWaveformBufferSize parameter to 0 to get the size of the outputWaveform array in the actualWaveformSize parameter. |
| t0 | [out] | ViReal64 | This element should be ignored. |
| dt | [out] | ViReal64 | Returns the inverse of the sample rate of the waveform. |
| i | [out] | ViReal32[] | Returns the in-phase part of the waveform. |
| q | [out] | ViReal32[] | Returns the quadrature-phase part of the waveform. |
| actualWaveformSize | [out] | ViInt32 | Returns the actual size of the array, if you pass NULL to all output array parameters, and set the outputWaveformBufferSize parameter to 0. |

#### Returns

Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred. To obtain a text description of the status code and additional information about the error condition, call the [niRFSGPlayback_GetError](group____root__ni_r_f_s_g_playback__functions_1ga5985403bcf5416e344ce264b3a73fc4a.html) function. The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

Functions

<!--NI_TOPIC bundle=rfsgplaybacklibrary-c-api-ref path=group____root__ni_r_f_s_g_playback__functions_1ga2af05f2cdbc5b2a6f7dd8cfbb6da1a45.html language=enus -->
## TOPIC 00005: niRFSGPlayback_ReadWaveformsFromFileComplexF64Split

- bundle_id: `rfsgplaybacklibrary-c-api-ref`
- source_path: `group____root__ni_r_f_s_g_playback__functions_1ga2af05f2cdbc5b2a6f7dd8cfbb6da1a45.html`
- source_url: https://docs-be.ni.com/bundle/rfsgplaybacklibrary-c-api-ref/raw/resource/enus/group____root__ni_r_f_s_g_playback__functions_1ga2af05f2cdbc5b2a6f7dd8cfbb6da1a45.html
- document_id: `rfsgplaybacklibrary-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Reads the waveforms from file and returns the in-phase and quadrature-phase part of the waveforms in the output parameters. Syntaxint32 __stdcall niRFSGPlayback_ReadWaveformsFromFileComplexF64Split(ViConstString filePath, ViInt32 numberOfWaveforms, ViInt32 outputWaveformBufferSize, ViReal64[] t0, Vi

### niRFSGPlayback_ReadWaveformsFromFileComplexF64Split

Reads the waveforms from file and returns the in-phase and quadrature-phase part of the waveforms in the output parameters.

#### Syntax

int32 __stdcall niRFSGPlayback_ReadWaveformsFromFileComplexF64Split(ViConstString filePath, ViInt32 numberOfWaveforms, ViInt32 outputWaveformBufferSize, ViReal64[] t0, ViReal64[] dt, ViReal64[] i, ViReal64[] q, ViInt32 actualSizePerWaveform)

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| filePath | [in] | ViConstString | Specifies the absolute path to the TDMS file from which the playback library reads the waveforms. |
| numberOfWaveforms | [in] | ViInt32 | Specifies the number of waveforms to read. |
| outputWaveformBufferSize | [in] | ViInt32 | Specifies the size of the outputWaveform array. Set the outputWaveformBufferSize parameter to 0 to get the size of the outputWaveform array in the actualWaveformSize parameter. |
| t0 | [out] | ViReal64[] | This element should be ignored. |
| dt | [out] | ViReal64[] | Returns the inverse of the sample rate of the waveform. |
| i | [out] | ViReal64[] | Returns the in-phase part of the waveforms. |
| q | [out] | ViReal64[] | Returns the quadrature-phase part of the waveforms. |
| actualSizePerWaveform | [out] | ViInt32 | Returns the actual size of the array, if you pass NULL to all output array parameters, and set the outputBufferSizePerWaveform parameter to 0. |

#### Returns

Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred. To obtain a text description of the status code and additional information about the error condition, call the [niRFSGPlayback_GetError](group____root__ni_r_f_s_g_playback__functions_1ga5985403bcf5416e344ce264b3a73fc4a.html) function. The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

Functions

<!--NI_TOPIC bundle=rfsgplaybacklibrary-c-api-ref path=group____root__ni_r_f_s_g_playback__functions_1ga327a529fd25c446308fe61820a3ca90d.html language=enus -->
## TOPIC 00006: niRFSGPlayback_SetScriptToGenerateMultipleRFSG

- bundle_id: `rfsgplaybacklibrary-c-api-ref`
- source_path: `group____root__ni_r_f_s_g_playback__functions_1ga327a529fd25c446308fe61820a3ca90d.html`
- source_url: https://docs-be.ni.com/bundle/rfsgplaybacklibrary-c-api-ref/raw/resource/enus/group____root__ni_r_f_s_g_playback__functions_1ga327a529fd25c446308fe61820a3ca90d.html
- document_id: `rfsgplaybacklibrary-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Configures the NI-RFSG driver to generate the waveforms specified in the script at the average power you configure on the NIRFSG_ATTR_POWER_LEVEL_TYPE attribute. If you have enabled RF Blanking for the waveform, NI-RFSG is configured to correctly blank the output during the idle times of the wavefor

### niRFSGPlayback_SetScriptToGenerateMultipleRFSG

Configures the NI-RFSG driver to generate the waveforms specified in the script at the average power you configure on the NIRFSG_ATTR_POWER_LEVEL_TYPE attribute. If you have enabled RF Blanking for the waveform, NI-RFSG is configured to correctly blank the output during the idle times of the waveform.

#### Syntax

int32 __stdcall niRFSGPlayback_SetScriptToGenerateMultipleRFSG(ViSession[] rfsgSession, ViInt32 numberOfSessions, ViConstString scriptText)

#### Remarks

The NIRFSG_ATTR_IQ_RATE attribute is set to the sample rate of the waveforms in the script.

If the version of the waveform file is 2.0 or later, the function,

- Sets the NIRFSG_ATTR_PEAK_POWER_ADJUSTMENT attribute to the minimum value of the peak to average power ratio (PAPR) of the waveforms in the script.
- Sets the NIRFSG_ATTR_PEAK_POWER_ADJUSTMENT attribute to the minimum value of the runtime scaling of the waveforms in the script.

If the version of the waveform file is lesser than 2.0, the function,

- Sets the NIRFSG_ATTR_PEAK_POWER_ADJUSTMENT attribute to the minimum value of the Headroom of the waveforms in the script.
- Resets the NIRFSG_ATTR_PEAK_POWER_ADJUSTMENT attribute.

For the waveforms that have the RF blanking Enabled attribute set to True, this function also does the following:

- If the values of RF blanking marker source of all the waveforms are empty, then the first unused marker in the script is set as the RF Blanking Source.
- Modifies the script to add the waveform burst start and stop locations as the RF Blanking marker locations

For PXIe-5840/5841/5842 and PXIe-5830/5831/5832 devices,

- Sets the NIRFSG_ATTR_SIGNAL_BANDWIDTH attribute to the maximum signal bandwidth of the waveforms in the script, if you set the LO Offset Mode to NIRFSGPLAYBACK_VAL_LO_OFFSET_MODE_AUTO. If no signal bandwidth is found in any waveform of the script, the NIRFSG_ATTR_SIGNAL_BANDWIDTH attribute is set to 0.8 times the Sample Rate.
- Resets the NIRFSG_ATTR_SIGNAL_BANDWIDTH attribute, if you set the LO Offset Mode to NIRFSGPLAYBACK_VAL_LO_OFFSET_MODE_NO_OFFSET.

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| rfsgSession | [out] | ViSession[] | Identifies the instrument session. rfsgSession is obtained from either the niRFSG_init function or the niRFSG_InitWithOptions function. |
| numberOfSessions | [in] | ViInt32 | Specifies the number of instrument sessions. |
| scriptText | [in] | ViConstString | Specifies the script that controls the waveform generation. |

#### Returns

Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred. To obtain a text description of the status code and additional information about the error condition, call the [niRFSGPlayback_GetError](group____root__ni_r_f_s_g_playback__functions_1ga5985403bcf5416e344ce264b3a73fc4a.html) function. The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

Functions

<!--NI_TOPIC bundle=rfsgplaybacklibrary-c-api-ref path=group____root__ni_r_f_s_g_playback__functions_1ga33f893ef9b49019ca4c268cc37da3bf5.html language=enus -->
## TOPIC 00007: niRFSGPlayback_ReadWaveformsFromFileComplexF64

- bundle_id: `rfsgplaybacklibrary-c-api-ref`
- source_path: `group____root__ni_r_f_s_g_playback__functions_1ga33f893ef9b49019ca4c268cc37da3bf5.html`
- source_url: https://docs-be.ni.com/bundle/rfsgplaybacklibrary-c-api-ref/raw/resource/enus/group____root__ni_r_f_s_g_playback__functions_1ga33f893ef9b49019ca4c268cc37da3bf5.html
- document_id: `rfsgplaybacklibrary-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Reads the waveforms from file and returns the waveforms in an output parameter. Syntaxint32 __stdcall niRFSGPlayback_ReadWaveformsFromFileComplexF64(ViConstString filePath, ViInt32 numberOfWaveforms, ViInt32 outputBufferSizePerWaveform, ViReal64[] t0, ViReal64[] dt, NIComplexNumber[] outputWaveforms

### niRFSGPlayback_ReadWaveformsFromFileComplexF64

Reads the waveforms from file and returns the waveforms in an output parameter.

#### Syntax

int32 __stdcall niRFSGPlayback_ReadWaveformsFromFileComplexF64(ViConstString filePath, ViInt32 numberOfWaveforms, ViInt32 outputBufferSizePerWaveform, ViReal64[] t0, ViReal64[] dt, NIComplexNumber[] outputWaveforms, ViInt32 actualSizePerWaveform)

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| filePath | [in] | ViConstString | Specifies the absolute path to the TDMS file from which the playback library reads the waveforms. |
| numberOfWaveforms | [in] | ViInt32 | Specifies the number of waveforms to read. |
| outputBufferSizePerWaveform | [in] | ViInt32 | Specifies the size of the outputWaveform array. Set the outputWaveformBufferSize parameter to 0 to get the size of the outputWaveform array in the actualWaveformSize parameter. |
| t0 | [out] | ViReal64[] | This element should be ignored. |
| dt | [out] | ViReal64[] | Returns the inverse of the sample rate of the waveform. |
| outputWaveforms | [out] | NIComplexNumber[] | Returns the complex waveform samples stored in an array. |
| actualSizePerWaveform | [out] | ViInt32 | Returns the actual size of the array, if you pass NULL to all output array parameters, and set the outputBufferSizePerWaveform parameter to 0. |

#### Returns

Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred. To obtain a text description of the status code and additional information about the error condition, call the [niRFSGPlayback_GetError](group____root__ni_r_f_s_g_playback__functions_1ga5985403bcf5416e344ce264b3a73fc4a.html) function. The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

Functions

<!--NI_TOPIC bundle=rfsgplaybacklibrary-c-api-ref path=group____root__ni_r_f_s_g_playback__functions_1ga3ac3ec40f5706457d05f3c1962eeb7b1.html language=enus -->
## TOPIC 00008: niRFSGPlayback_ReadWaveformFromFileByIndexComplexF32Split

- bundle_id: `rfsgplaybacklibrary-c-api-ref`
- source_path: `group____root__ni_r_f_s_g_playback__functions_1ga3ac3ec40f5706457d05f3c1962eeb7b1.html`
- source_url: https://docs-be.ni.com/bundle/rfsgplaybacklibrary-c-api-ref/raw/resource/enus/group____root__ni_r_f_s_g_playback__functions_1ga3ac3ec40f5706457d05f3c1962eeb7b1.html
- document_id: `rfsgplaybacklibrary-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Reads the waveform from file and returns the in-phase and quadrature-phase part of the waveform in the output parameters. Syntaxint32 __stdcall niRFSGPlayback_ReadWaveformFromFileByIndexComplexF32Split(ViConstString filePath, ViInt32 waveformIndex, ViInt32 outputWaveformBufferSize, ViReal64 t0, ViRe

### niRFSGPlayback_ReadWaveformFromFileByIndexComplexF32Split

Reads the waveform from file and returns the in-phase and quadrature-phase part of the waveform in the output parameters.

#### Syntax

int32 __stdcall niRFSGPlayback_ReadWaveformFromFileByIndexComplexF32Split(ViConstString filePath, ViInt32 waveformIndex, ViInt32 outputWaveformBufferSize, ViReal64 t0, ViReal64 dt, ViReal32[] i, ViReal32[] q, ViInt32 actualWaveformSize)

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| filePath | [in] | ViConstString | Specifies the absolute path to the TDMS file from which the playback library reads the waveforms. |
| waveformIndex | [in] | ViInt32 | Specifies the index of the waveform that you want to read from the TDMS file. |
| outputWaveformBufferSize | [in] | ViInt32 | Specifies the size of the outputWaveform array. Set the outputWaveformBufferSize parameter to 0 to get the size of the outputWaveform array in the actualWaveformSize parameter. |
| t0 | [out] | ViReal64 | This element should be ignored. |
| dt | [out] | ViReal64 | Returns the inverse of the sample rate of the waveform. |
| i | [out] | ViReal32[] | Returns the in-phase part of the waveform. |
| q | [out] | ViReal32[] | Returns the quadrature-phase part of the waveform. |
| actualWaveformSize | [out] | ViInt32 | Returns the actual size of the array, if you pass NULL to all output array parameters, and set the outputWaveformBufferSize parameter to 0. |

#### Returns

Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred. To obtain a text description of the status code and additional information about the error condition, call the [niRFSGPlayback_GetError](group____root__ni_r_f_s_g_playback__functions_1ga5985403bcf5416e344ce264b3a73fc4a.html) function. The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

Functions

<!--NI_TOPIC bundle=rfsgplaybacklibrary-c-api-ref path=group____root__ni_r_f_s_g_playback__functions_1ga5985403bcf5416e344ce264b3a73fc4a.html language=enus -->
## TOPIC 00009: niRFSGPlayback_GetError

- bundle_id: `rfsgplaybacklibrary-c-api-ref`
- source_path: `group____root__ni_r_f_s_g_playback__functions_1ga5985403bcf5416e344ce264b3a73fc4a.html`
- source_url: https://docs-be.ni.com/bundle/rfsgplaybacklibrary-c-api-ref/raw/resource/enus/group____root__ni_r_f_s_g_playback__functions_1ga5985403bcf5416e344ce264b3a73fc4a.html
- document_id: `rfsgplaybacklibrary-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the latest error code and description. Syntaxint32 __stdcall niRFSGPlayback_GetError(int errorCode, int32 errorDescriptionBufferSize, ViChar[] errorDescription)ParametersNameDirectionTypeDescriptionerrorCode[out]intReturns the latest error code. errorDescriptionBufferSize[in]int32Specifies the

### niRFSGPlayback_GetError

Gets the latest error code and description.

#### Syntax

int32 __stdcall niRFSGPlayback_GetError(int errorCode, int32 errorDescriptionBufferSize, ViChar[] errorDescription)

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| errorCode | [out] | int | Returns the latest error code. |
| errorDescriptionBufferSize | [in] | int32 | Specifies the size of errorDescription array. |
| errorDescription | [out] | ViChar[] | Returns the latest error description. |

#### Returns

Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred. To obtain a text description of the status code and additional information about the error condition, call the [niRFSGPlayback_GetError](group____root__ni_r_f_s_g_playback__functions_1ga5985403bcf5416e344ce264b3a73fc4a.html) function. The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

Functions

<!--NI_TOPIC bundle=rfsgplaybacklibrary-c-api-ref path=group____root__ni_r_f_s_g_playback__functions_1ga5f7818f03776894077afb4a1349b58dc.html language=enus -->
## TOPIC 00010: niRFSGPlayback_DownloadUserWaveformComplexF32Split

- bundle_id: `rfsgplaybacklibrary-c-api-ref`
- source_path: `group____root__ni_r_f_s_g_playback__functions_1ga5f7818f03776894077afb4a1349b58dc.html`
- source_url: https://docs-be.ni.com/bundle/rfsgplaybacklibrary-c-api-ref/raw/resource/enus/group____root__ni_r_f_s_g_playback__functions_1ga5f7818f03776894077afb4a1349b58dc.html
- document_id: `rfsgplaybacklibrary-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Normalizes the in-phase and quadrature-phase part of the input waveform and writes it into the NI RF vector signal generator. This function computes the peak to average power ratio (PAPR) using the bursts in the waveform, stores the PAPR, sample rate, waveform size, and runtime scaling value of -1.5

### niRFSGPlayback_DownloadUserWaveformComplexF32Split

Normalizes the in-phase and quadrature-phase part of the input waveform and writes it into the NI RF vector signal generator. This function computes the peak to average power ratio (PAPR) using the bursts in the waveform, stores the PAPR, sample rate, waveform size, and runtime scaling value of -1.5 dB in the NI-RFSG waveform database.

#### Syntax

int32 __stdcall niRFSGPlayback_DownloadUserWaveformComplexF32Split(ViSession rfsgSession, ViConstString rfsgWaveformName, ViReal64 t0, ViReal64 dt, ViReal32[] i, ViReal32[] q, ViInt32 waveformSize, ViInt32 burstPresent)

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| rfsgSession | [in] | ViSession | Identifies the instrument session. rfsgSession is obtained from either the niRFSG_init function or the niRFSG_InitWithOptions function. |
| rfsgWaveformName | [in] | ViConstString | Specifies the name used to write the waveform to the NI-RFSG device memory. |
| t0 | [in] | ViReal64 | Specifies the start time of the given input waveform. |
| dt | [in] | ViReal64 | Specifies the time interval between the samples in the given input waveform. |
| i | [out] | ViReal32[] | Returns the in-phase part of the input waveform. |
| q | [out] | ViReal32[] | Returns the quadrature-phase part of the input waveform. |
| waveformSize | [in] | ViInt32 | Specifies the size of the waveform array. |
| burstPresent | [in] | ViInt32 | Specifies whether the burst is present in the given waveform. |

#### Returns

Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred. To obtain a text description of the status code and additional information about the error condition, call the [niRFSGPlayback_GetError](group____root__ni_r_f_s_g_playback__functions_1ga5985403bcf5416e344ce264b3a73fc4a.html) function. The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

Functions

<!--NI_TOPIC bundle=rfsgplaybacklibrary-c-api-ref path=group____root__ni_r_f_s_g_playback__functions_1ga6740272a1c2ce779e34641496658bd4f.html language=enus -->
## TOPIC 00011: niRFSGPlayback_ReadWaveformFromFileComplexF64

- bundle_id: `rfsgplaybacklibrary-c-api-ref`
- source_path: `group____root__ni_r_f_s_g_playback__functions_1ga6740272a1c2ce779e34641496658bd4f.html`
- source_url: https://docs-be.ni.com/bundle/rfsgplaybacklibrary-c-api-ref/raw/resource/enus/group____root__ni_r_f_s_g_playback__functions_1ga6740272a1c2ce779e34641496658bd4f.html
- document_id: `rfsgplaybacklibrary-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Reads the waveform from the file and returns the waveform in an output parameter. Syntaxint32 __stdcall niRFSGPlayback_ReadWaveformFromFileComplexF64(ViConstString filePath, ViInt32 outputWaveformBufferSize, ViReal64 t0, ViReal64 dt, NIComplexNumber[] outputWaveform, ViInt32 actualWaveformSize)Param

### niRFSGPlayback_ReadWaveformFromFileComplexF64

Reads the waveform from the file and returns the waveform in an output parameter.

#### Syntax

int32 __stdcall niRFSGPlayback_ReadWaveformFromFileComplexF64(ViConstString filePath, ViInt32 outputWaveformBufferSize, ViReal64 t0, ViReal64 dt, NIComplexNumber[] outputWaveform, ViInt32 actualWaveformSize)

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| filePath | [in] | ViConstString | Specifies the absolute path to the TDMS file from which the playback library reads the waveforms. |
| outputWaveformBufferSize | [in] | ViInt32 | Specifies the size of the outputWaveform array. Set the outputWaveformBufferSize parameter to 0 to get the size of the outputWaveform array in the actualWaveformSize parameter. |
| t0 | [out] | ViReal64 | This element should be ignored. |
| dt | [out] | ViReal64 | Returns the inverse of the sample rate of the waveform. |
| outputWaveform | [out] | NIComplexNumber[] | Returns the complex waveform samples stored in an array. |
| actualWaveformSize | [out] | ViInt32 | Returns the actual size of the array, if you pass NULL to all output array parameters, and set the outputWaveformBufferSize parameter to 0. |

#### Returns

Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred. To obtain a text description of the status code and additional information about the error condition, call the [niRFSGPlayback_GetError](group____root__ni_r_f_s_g_playback__functions_1ga5985403bcf5416e344ce264b3a73fc4a.html) function. The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

Functions

<!--NI_TOPIC bundle=rfsgplaybacklibrary-c-api-ref path=group____root__ni_r_f_s_g_playback__functions_1ga67c00516ba5f940d837a42e84792071d.html language=enus -->
## TOPIC 00012: niRFSGPlayback_ReadWaveformsFromFileComplexF32Split

- bundle_id: `rfsgplaybacklibrary-c-api-ref`
- source_path: `group____root__ni_r_f_s_g_playback__functions_1ga67c00516ba5f940d837a42e84792071d.html`
- source_url: https://docs-be.ni.com/bundle/rfsgplaybacklibrary-c-api-ref/raw/resource/enus/group____root__ni_r_f_s_g_playback__functions_1ga67c00516ba5f940d837a42e84792071d.html
- document_id: `rfsgplaybacklibrary-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Reads the waveforms from file and returns the in-phase and quadrature-phase part of the waveforms in the output parameters. Syntaxint32 __stdcall niRFSGPlayback_ReadWaveformsFromFileComplexF32Split(ViConstString filePath, ViInt32 numberOfWaveforms, ViInt32 outputBufferSizePerWaveform, ViReal64[] t0,

### niRFSGPlayback_ReadWaveformsFromFileComplexF32Split

Reads the waveforms from file and returns the in-phase and quadrature-phase part of the waveforms in the output parameters.

#### Syntax

int32 __stdcall niRFSGPlayback_ReadWaveformsFromFileComplexF32Split(ViConstString filePath, ViInt32 numberOfWaveforms, ViInt32 outputBufferSizePerWaveform, ViReal64[] t0, ViReal64[] dt, ViReal32[] i, ViReal32[] q, ViInt32 actualWaveformSize)

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| filePath | [in] | ViConstString | Specifies the absolute path to the TDMS file from which the playback library reads the waveforms. |
| numberOfWaveforms | [in] | ViInt32 | Specifies the number of waveforms to read. |
| outputBufferSizePerWaveform | [in] | ViInt32 | Specifies the size of the outputWaveform array. Set the outputBufferSizePerWaveform parameter to 0 to get the size of the outputWaveform array in the actualWaveformSize parameter. |
| t0 | [out] | ViReal64[] | This element should be ignored. |
| dt | [out] | ViReal64[] | Returns the inverse of the sample rate of the waveform. |
| i | [out] | ViReal32[] | Returns the in-phase part of the waveforms. |
| q | [out] | ViReal32[] | Returns the quadrature-phase part of the waveforms. |
| actualWaveformSize | [out] | ViInt32 | Returns the actual size of the array, if you pass NULL to all output array parameters, and set the outputWaveformBufferSize parameter to 0. |

#### Returns

Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred. To obtain a text description of the status code and additional information about the error condition, call the [niRFSGPlayback_GetError](group____root__ni_r_f_s_g_playback__functions_1ga5985403bcf5416e344ce264b3a73fc4a.html) function. The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

Functions

<!--NI_TOPIC bundle=rfsgplaybacklibrary-c-api-ref path=group____root__ni_r_f_s_g_playback__functions_1ga6d2c2d0d790d1d2ea2e9b778bb92f186.html language=enus -->
## TOPIC 00013: niRFSGPlayback_ReadWaveformsFromFileComplexF32

- bundle_id: `rfsgplaybacklibrary-c-api-ref`
- source_path: `group____root__ni_r_f_s_g_playback__functions_1ga6d2c2d0d790d1d2ea2e9b778bb92f186.html`
- source_url: https://docs-be.ni.com/bundle/rfsgplaybacklibrary-c-api-ref/raw/resource/enus/group____root__ni_r_f_s_g_playback__functions_1ga6d2c2d0d790d1d2ea2e9b778bb92f186.html
- document_id: `rfsgplaybacklibrary-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Reads the waveforms from file and returns the waveforms in an output parameter. Syntaxint32 __stdcall niRFSGPlayback_ReadWaveformsFromFileComplexF32(ViConstString filePath, ViInt32 numberOfWaveforms, ViInt32 outputBufferSizePerWaveform, ViReal64[] t0, ViReal64[] dt, NIComplexNumberF32[] outputWavefo

### niRFSGPlayback_ReadWaveformsFromFileComplexF32

Reads the waveforms from file and returns the waveforms in an output parameter.

#### Syntax

int32 __stdcall niRFSGPlayback_ReadWaveformsFromFileComplexF32(ViConstString filePath, ViInt32 numberOfWaveforms, ViInt32 outputBufferSizePerWaveform, ViReal64[] t0, ViReal64[] dt, NIComplexNumberF32[] outputWaveforms, ViInt32 actualWaveformSize)

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| filePath | [in] | ViConstString | Specifies the absolute path to the TDMS file from which the playback library reads the waveforms. |
| numberOfWaveforms | [in] | ViInt32 | Specifies the number of waveforms to read. |
| outputBufferSizePerWaveform | [in] | ViInt32 | Specifies the size of the outputWaveform array. Set the outputBufferSizePerWaveform parameter to 0 to get the size of the outputWaveform array in the actualWaveformSize parameter. |
| t0 | [out] | ViReal64[] | This element should be ignored. |
| dt | [out] | ViReal64[] | Returns the inverse of the sample rate of the waveform. |
| outputWaveforms | [out] | NIComplexNumberF32[] | Returns the complex waveform samples stored in an array. |
| actualWaveformSize | [out] | ViInt32 | Returns the actual size of the array, if you pass NULL to all output array parameters, and set the outputWaveformBufferSize parameter to 0. |

#### Returns

Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred. To obtain a text description of the status code and additional information about the error condition, call the [niRFSGPlayback_GetError](group____root__ni_r_f_s_g_playback__functions_1ga5985403bcf5416e344ce264b3a73fc4a.html) function. The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

Functions

<!--NI_TOPIC bundle=rfsgplaybacklibrary-c-api-ref path=group____root__ni_r_f_s_g_playback__functions_1ga7270e740457f30b0a9362c33fb3e1f89.html language=enus -->
## TOPIC 00014: niRFSGPlayback_DownloadUserWaveformComplexF64

- bundle_id: `rfsgplaybacklibrary-c-api-ref`
- source_path: `group____root__ni_r_f_s_g_playback__functions_1ga7270e740457f30b0a9362c33fb3e1f89.html`
- source_url: https://docs-be.ni.com/bundle/rfsgplaybacklibrary-c-api-ref/raw/resource/enus/group____root__ni_r_f_s_g_playback__functions_1ga7270e740457f30b0a9362c33fb3e1f89.html
- document_id: `rfsgplaybacklibrary-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Normalizes the input waveform and writes it into the NI RF vector signal generator. This VI computes the peak to average power ratio (PAPR) using the bursts in the waveform, stores the PAPR, sample rate, waveform size, and runtime scaling value of -1.5 dB in the NI-RFSG waveform database. Syntaxint3

### niRFSGPlayback_DownloadUserWaveformComplexF64

Normalizes the input waveform and writes it into the NI RF vector signal generator. This VI computes the peak to average power ratio (PAPR) using the bursts in the waveform, stores the PAPR, sample rate, waveform size, and runtime scaling value of -1.5 dB in the NI-RFSG waveform database.

#### Syntax

int32 __stdcall niRFSGPlayback_DownloadUserWaveformComplexF64(ViSession rfsgSession, ViConstString rfsgWaveformName, ViReal64 t0, ViReal64 dt, NIComplexNumber[] waveform, ViInt32 waveformSize, ViInt32 burstPresent)

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| rfsgSession | [in] | ViSession | Identifies the instrument session. rfsgSession is obtained from either the niRFSG_init function or the niRFSG_InitWithOptions function. |
| rfsgWaveformName | [in] | ViConstString | Specifies the name used to write the waveform to the NI-RFSG device memory. |
| t0 | [in] | ViReal64 | Specifies the start time of the given input waveform. |
| dt | [in] | ViReal64 | Specifies the time interval between the samples in the given input waveform. |
| waveform | [out] | NIComplexNumber[] | Specifies an array of the complex double waveform clusters which has to be downloaded to the device. |
| waveformSize | [in] | ViInt32 | Specifies the size of the waveform array. |
| burstPresent | [in] | ViInt32 | Specifies whether the burst is present in the given waveform. |

#### Returns

Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred. To obtain a text description of the status code and additional information about the error condition, call the [niRFSGPlayback_GetError](group____root__ni_r_f_s_g_playback__functions_1ga5985403bcf5416e344ce264b3a73fc4a.html) function. The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

Functions

<!--NI_TOPIC bundle=rfsgplaybacklibrary-c-api-ref path=group____root__ni_r_f_s_g_playback__functions_1ga7d3c83233d1afcb47b993bfee142298d.html language=enus -->
## TOPIC 00015: niRFSGPlayback_SetScriptToGenerateSingleRFSG

- bundle_id: `rfsgplaybacklibrary-c-api-ref`
- source_path: `group____root__ni_r_f_s_g_playback__functions_1ga7d3c83233d1afcb47b993bfee142298d.html`
- source_url: https://docs-be.ni.com/bundle/rfsgplaybacklibrary-c-api-ref/raw/resource/enus/group____root__ni_r_f_s_g_playback__functions_1ga7d3c83233d1afcb47b993bfee142298d.html
- document_id: `rfsgplaybacklibrary-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Configures the NI-RFSG driver to generate the waveforms specified in the script at the average power you configure on the NIRFSG_ATTR_POWER_LEVEL_TYPE attribute. If you have enabled RF Blanking for the waveform, NI-RFSG is configured to correctly blank the output during the idle times of the wavefor

### niRFSGPlayback_SetScriptToGenerateSingleRFSG

Configures the NI-RFSG driver to generate the waveforms specified in the script at the average power you configure on the NIRFSG_ATTR_POWER_LEVEL_TYPE attribute. If you have enabled RF Blanking for the waveform, NI-RFSG is configured to correctly blank the output during the idle times of the waveform.

#### Syntax

int32 __stdcall niRFSGPlayback_SetScriptToGenerateSingleRFSG(ViSession rfsgSession, ViConstString scriptText)

#### Remarks

The NIRFSG_ATTR_IQ_RATE attribute is set to the sample rate of the waveforms in the script.

If the version of the waveform file is 2.0 or later, the function,

- Sets the NIRFSG_ATTR_PEAK_POWER_ADJUSTMENT attribute to the minimum value of the peak to average power ratio (PAPR) of the waveform in the script.
- Sets the NIRFSG_ATTR_PEAK_POWER_ADJUSTMENT attribute to the minimum value of the runtime scaling of the waveform in the script.

If the version of the waveform file is lesser than 2.0, the function,

- Sets the NIRFSG_ATTR_PEAK_POWER_ADJUSTMENT attribute to the minimum value of the Headroom of the waveform in the script.
- Resets the NIRFSG_ATTR_PEAK_POWER_ADJUSTMENT attribute.

For the waveforms that have the RF blanking Enabled attribute set to True, this function also does the following:

- If the values of RF blanking marker source of all the waveforms are empty, then the first unused marker in the script is set as the RF Blanking Source.
- Modifies the script to add the waveform burst start and stop locations as the RF Blanking marker locations

For PXIe-5840/5841/5842 and PXIe-5830/5831/5832 devices,

- Sets the NIRFSG_ATTR_SIGNAL_BANDWIDTH attribute to the maximum signal bandwidth of the waveform in the script, if you set the LO Offset Mode to NIRFSGPLAYBACK_VAL_LO_OFFSET_MODE_AUTO. If no signal bandwidth is found in any waveform of the script, the NIRFSG_ATTR_SIGNAL_BANDWIDTH attribute is set to 0.8 times the Sample Rate.
- Resets the NIRFSG_ATTR_SIGNAL_BANDWIDTH attribute, if you set the LO Offset Mode to NIRFSGPLAYBACK_VAL_LO_OFFSET_MODE_NO_OFFSET.

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| rfsgSession | [in] | ViSession | Identifies the instrument session. rfsgSession is obtained from either the niRFSG_init function or the niRFSG_InitWithOptions function. |
| scriptText | [in] | ViConstString | Specifies the script that controls the waveform generation. |

#### Returns

Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred. To obtain a text description of the status code and additional information about the error condition, call the [niRFSGPlayback_GetError](group____root__ni_r_f_s_g_playback__functions_1ga5985403bcf5416e344ce264b3a73fc4a.html) function. The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

Functions

<!--NI_TOPIC bundle=rfsgplaybacklibrary-c-api-ref path=group____root__ni_r_f_s_g_playback__functions_1ga88b9b5511681ec097547be1d9863eb3d.html language=enus -->
## TOPIC 00016: niRFSGPlayback_ReadWaveformFromFileComplexF64Split

- bundle_id: `rfsgplaybacklibrary-c-api-ref`
- source_path: `group____root__ni_r_f_s_g_playback__functions_1ga88b9b5511681ec097547be1d9863eb3d.html`
- source_url: https://docs-be.ni.com/bundle/rfsgplaybacklibrary-c-api-ref/raw/resource/enus/group____root__ni_r_f_s_g_playback__functions_1ga88b9b5511681ec097547be1d9863eb3d.html
- document_id: `rfsgplaybacklibrary-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Reads the waveform from file and returns the in-phase and quadrature-phase part of the waveform in the output parameters. Syntaxint32 __stdcall niRFSGPlayback_ReadWaveformFromFileComplexF64Split(ViConstString filePath, ViInt32 outputWaveformBufferSize, ViReal64 t0, ViReal64 dt, ViReal64[] i, ViReal6

### niRFSGPlayback_ReadWaveformFromFileComplexF64Split

Reads the waveform from file and returns the in-phase and quadrature-phase part of the waveform in the output parameters.

#### Syntax

int32 __stdcall niRFSGPlayback_ReadWaveformFromFileComplexF64Split(ViConstString filePath, ViInt32 outputWaveformBufferSize, ViReal64 t0, ViReal64 dt, ViReal64[] i, ViReal64[] q, ViInt32 actualWaveformSize)

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| filePath | [in] | ViConstString | Specifies the absolute path to the TDMS file from which the playback library reads the waveforms. |
| outputWaveformBufferSize | [in] | ViInt32 | Specifies the size of the outputWaveform array. Set the outputWaveformBufferSize parameter to 0 to get the size of the outputWaveform array in the actualWaveformSize parameter. |
| t0 | [out] | ViReal64 | This element should be ignored. |
| dt | [out] | ViReal64 | Returns the inverse of the sample rate of the waveform. |
| i | [out] | ViReal64[] | Returns the in-phase part of the waveform. |
| q | [out] | ViReal64[] | Returns the quadrature-phase part of the waveform. |
| actualWaveformSize | [out] | ViInt32 | Returns the actual size of the array, if you pass NULL to all output array parameters, and set the outputWaveformBufferSize parameter to 0. |

#### Returns

Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred. To obtain a text description of the status code and additional information about the error condition, call the [niRFSGPlayback_GetError](group____root__ni_r_f_s_g_playback__functions_1ga5985403bcf5416e344ce264b3a73fc4a.html) function. The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

Functions

<!--NI_TOPIC bundle=rfsgplaybacklibrary-c-api-ref path=group____root__ni_r_f_s_g_playback__functions_1ga8bbc751369cc8356a59b1b250e9fb39e.html language=enus -->
## TOPIC 00017: niRFSGPlayback_ClearAllWaveforms

- bundle_id: `rfsgplaybacklibrary-c-api-ref`
- source_path: `group____root__ni_r_f_s_g_playback__functions_1ga8bbc751369cc8356a59b1b250e9fb39e.html`
- source_url: https://docs-be.ni.com/bundle/rfsgplaybacklibrary-c-api-ref/raw/resource/enus/group____root__ni_r_f_s_g_playback__functions_1ga8bbc751369cc8356a59b1b250e9fb39e.html
- document_id: `rfsgplaybacklibrary-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Deletes all the waveforms from NI-RFSG device memory and removes all the waveform property from the NI-RFSG waveform database for the specified device. Syntaxint32 __stdcall niRFSGPlayback_ClearAllWaveforms(ViSession rfsgSession)ParametersNameDirectionTypeDescriptionrfsgSession[in]ViSessionIdentifie

### niRFSGPlayback_ClearAllWaveforms

Deletes all the waveforms from NI-RFSG device memory and removes all the waveform property from the NI-RFSG waveform database for the specified device.

#### Syntax

int32 __stdcall niRFSGPlayback_ClearAllWaveforms(ViSession rfsgSession)

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| rfsgSession | [in] | ViSession | Identifies the instrument session. rfsgSession is obtained from either the niRFSG_init function or the niRFSG_InitWithOptions function. |

#### Returns

Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred. To obtain a text description of the status code and additional information about the error condition, call the [niRFSGPlayback_GetError](group____root__ni_r_f_s_g_playback__functions_1ga5985403bcf5416e344ce264b3a73fc4a.html) function. The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

Functions

<!--NI_TOPIC bundle=rfsgplaybacklibrary-c-api-ref path=group____root__ni_r_f_s_g_playback__functions_1ga95172806e164598498fec12c4380fdc8.html language=enus -->
## TOPIC 00018: niRFSGPlayback_ReadWaveformFromFileByIndexComplexF32

- bundle_id: `rfsgplaybacklibrary-c-api-ref`
- source_path: `group____root__ni_r_f_s_g_playback__functions_1ga95172806e164598498fec12c4380fdc8.html`
- source_url: https://docs-be.ni.com/bundle/rfsgplaybacklibrary-c-api-ref/raw/resource/enus/group____root__ni_r_f_s_g_playback__functions_1ga95172806e164598498fec12c4380fdc8.html
- document_id: `rfsgplaybacklibrary-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Reads the waveform from file and returns the waveform in an output parameter. Syntaxint32 __stdcall niRFSGPlayback_ReadWaveformFromFileByIndexComplexF32(ViConstString filePath, ViInt32 waveformIndex, ViInt32 outputWaveformBufferSize, ViReal64 t0, ViReal64 dt, NIComplexNumberF32[] outputWaveform, ViI

### niRFSGPlayback_ReadWaveformFromFileByIndexComplexF32

Reads the waveform from file and returns the waveform in an output parameter.

#### Syntax

int32 __stdcall niRFSGPlayback_ReadWaveformFromFileByIndexComplexF32(ViConstString filePath, ViInt32 waveformIndex, ViInt32 outputWaveformBufferSize, ViReal64 t0, ViReal64 dt, NIComplexNumberF32[] outputWaveform, ViInt32 actualWaveformSize)

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| filePath | [in] | ViConstString | Specifies the absolute path to the TDMS file from which the playback library reads the waveforms. |
| waveformIndex | [in] | ViInt32 | Specifies the index of the waveform that you want to read from the TDMS file. |
| outputWaveformBufferSize | [in] | ViInt32 | Specifies the size of the outputWaveform array. Set the outputWaveformBufferSize parameter to 0 to get the size of the outputWaveform array in the actualWaveformSize parameter. |
| t0 | [out] | ViReal64 | This element should be ignored. |
| dt | [out] | ViReal64 | Returns the inverse of the sample rate of the waveform. |
| outputWaveform | [out] | NIComplexNumberF32[] | Returns the complex waveform samples stored in an array. |
| actualWaveformSize | [out] | ViInt32 | Returns the actual size of the array, if you pass NULL to all output array parameters, and set the outputWaveformBufferSize parameter to 0. |

#### Returns

Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred. To obtain a text description of the status code and additional information about the error condition, call the [niRFSGPlayback_GetError](group____root__ni_r_f_s_g_playback__functions_1ga5985403bcf5416e344ce264b3a73fc4a.html) function. The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

Functions

<!--NI_TOPIC bundle=rfsgplaybacklibrary-c-api-ref path=group____root__ni_r_f_s_g_playback__functions_1ga9652e855a037183740539ca6db3c4723.html language=enus -->
## TOPIC 00019: niRFSGPlayback_ClearWaveform

- bundle_id: `rfsgplaybacklibrary-c-api-ref`
- source_path: `group____root__ni_r_f_s_g_playback__functions_1ga9652e855a037183740539ca6db3c4723.html`
- source_url: https://docs-be.ni.com/bundle/rfsgplaybacklibrary-c-api-ref/raw/resource/enus/group____root__ni_r_f_s_g_playback__functions_1ga9652e855a037183740539ca6db3c4723.html
- document_id: `rfsgplaybacklibrary-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Deletes the waveform from NI-RFSG device memory and removes the waveform property from the NI-RFSG waveform database for the specified device. Syntaxint32 __stdcall niRFSGPlayback_ClearWaveform(ViSession rfsgSession, ViConstString waveformName)ParametersNameDirectionTypeDescriptionrfsgSession[in]ViS

### niRFSGPlayback_ClearWaveform

Deletes the waveform from NI-RFSG device memory and removes the waveform property from the NI-RFSG waveform database for the specified device.

#### Syntax

int32 __stdcall niRFSGPlayback_ClearWaveform(ViSession rfsgSession, ViConstString waveformName)

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| rfsgSession | [in] | ViSession | Identifies the instrument session. rfsgSession is obtained from either the niRFSG_init function or the niRFSG_InitWithOptions function. |
| waveformName | [in] | ViConstString | Specifies the waveform name to be deleted from the database. |

#### Returns

Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred. To obtain a text description of the status code and additional information about the error condition, call the [niRFSGPlayback_GetError](group____root__ni_r_f_s_g_playback__functions_1ga5985403bcf5416e344ce264b3a73fc4a.html) function. The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

Functions

<!--NI_TOPIC bundle=rfsgplaybacklibrary-c-api-ref path=group____root__ni_r_f_s_g_playback__functions_1gaa1d70c90c4f0fdc71e79a0c9c53548d6.html language=enus -->
## TOPIC 00020: niRFSGPlayback_ReadAndDownloadWaveformFromFile

- bundle_id: `rfsgplaybacklibrary-c-api-ref`
- source_path: `group____root__ni_r_f_s_g_playback__functions_1gaa1d70c90c4f0fdc71e79a0c9c53548d6.html`
- source_url: https://docs-be.ni.com/bundle/rfsgplaybacklibrary-c-api-ref/raw/resource/enus/group____root__ni_r_f_s_g_playback__functions_1gaa1d70c90c4f0fdc71e79a0c9c53548d6.html
- document_id: `rfsgplaybacklibrary-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Reads a waveform from a TDMS file, and downloads it to the NI RF vector signal generator. This function reads the following information from the TDMS file and writes it into the NI-RFSG waveform database: Syntaxint32 __stdcall niRFSGPlayback_ReadAndDownloadWaveformFromFile(ViSession rfsgSession, ViC

### niRFSGPlayback_ReadAndDownloadWaveformFromFile

Reads a waveform from a TDMS file, and downloads it to the NI RF vector signal generator. 
 This function reads the following information from the TDMS file and writes it into the NI-RFSG waveform database:

#### Syntax

int32 __stdcall niRFSGPlayback_ReadAndDownloadWaveformFromFile(ViSession rfsgSession, ViConstString filePath, ViConstString rfsgWaveformName)

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

If RF blanking marker locations are present in the file, but burst locations are not present, burst locations are calculated from RF blanking marker locations and stored in the NI-RFSG waveform database. 
 This function internally sets the NIRFSG_ATTR_POWER_LEVEL_TYPE attribute value to NIRFSG_VAL_PEAK_POWER before writing waveforms to NI-RFSG device memory. This function completes this tasks for each NI-RFSG session. 
 This function returns an error, if the TDMS file has more than one waveform.

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| rfsgSession | [in] | ViSession | Identifies the instrument session. rfsgSession is obtained from either the niRFSG_init function or the niRFSG_InitWithOptions function. |
| filePath | [in] | ViConstString | Specifies the absolute path to the TDMS file from which the playback library reads the waveforms. |
| rfsgWaveformName | [in] | ViConstString | Specifies the waveform name used to store the waveform in NI-RFSG device memory and waveform property in the NI-RFSG waveform database. |

#### Returns

Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred. To obtain a text description of the status code and additional information about the error condition, call the [niRFSGPlayback_GetError](group____root__ni_r_f_s_g_playback__functions_1ga5985403bcf5416e344ce264b3a73fc4a.html) function. The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

Functions

<!--NI_TOPIC bundle=rfsgplaybacklibrary-c-api-ref path=group____root__ni_r_f_s_g_playback__functions_1gaa5d45b80176760f3d66883f90643ca0e.html language=enus -->
## TOPIC 00021: niRFSGPlayback_DownloadUserWaveformComplexF32

- bundle_id: `rfsgplaybacklibrary-c-api-ref`
- source_path: `group____root__ni_r_f_s_g_playback__functions_1gaa5d45b80176760f3d66883f90643ca0e.html`
- source_url: https://docs-be.ni.com/bundle/rfsgplaybacklibrary-c-api-ref/raw/resource/enus/group____root__ni_r_f_s_g_playback__functions_1gaa5d45b80176760f3d66883f90643ca0e.html
- document_id: `rfsgplaybacklibrary-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Normalizes the input waveform and writes it into the NI RF vector signal generator. This VI computes the peak to average power ratio (PAPR) using the bursts in the waveform, stores the PAPR, sample rate, waveform size, and runtime scaling value of -1.5 dB in the NI-RFSG waveform database. Syntaxint3

### niRFSGPlayback_DownloadUserWaveformComplexF32

Normalizes the input waveform and writes it into the NI RF vector signal generator. This VI computes the peak to average power ratio (PAPR) using the bursts in the waveform, stores the PAPR, sample rate, waveform size, and runtime scaling value of -1.5 dB in the NI-RFSG waveform database.

#### Syntax

int32 __stdcall niRFSGPlayback_DownloadUserWaveformComplexF32(ViSession rfsgSession, ViConstString rfsgWaveformName, ViReal64 t0, ViReal64 dt, NIComplexNumberF32[] waveform, ViInt32 waveformSize, ViInt32 burstPresent)

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| rfsgSession | [in] | ViSession | Identifies the instrument session. rfsgSession is obtained from either the niRFSG_init function or the niRFSG_InitWithOptions function. |
| rfsgWaveformName | [in] | ViConstString | Specifies the name used to write the waveform to the NI-RFSG device memory. |
| t0 | [in] | ViReal64 | Specifies the start time of the given input waveform. |
| dt | [in] | ViReal64 | Specifies the time interval between the samples in the given input waveform. |
| waveform | [out] | NIComplexNumberF32[] | Specifies an array of the complex single waveform clusters to be downloaded to the device. |
| waveformSize | [in] | ViInt32 | Specifies the size of the waveform array. |
| burstPresent | [in] | ViInt32 | Specifies whether the burst is present in the given waveform. |

#### Returns

Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred. To obtain a text description of the status code and additional information about the error condition, call the [niRFSGPlayback_GetError](group____root__ni_r_f_s_g_playback__functions_1ga5985403bcf5416e344ce264b3a73fc4a.html) function. The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

Functions

<!--NI_TOPIC bundle=rfsgplaybacklibrary-c-api-ref path=group____root__ni_r_f_s_g_playback__functions_1gab8b3a7e38b276a236ae435dc25c45271.html language=enus -->
## TOPIC 00022: niRFSGPlayback_ReadAndDownloadWaveformsFromFile

- bundle_id: `rfsgplaybacklibrary-c-api-ref`
- source_path: `group____root__ni_r_f_s_g_playback__functions_1gab8b3a7e38b276a236ae435dc25c45271.html`
- source_url: https://docs-be.ni.com/bundle/rfsgplaybacklibrary-c-api-ref/raw/resource/enus/group____root__ni_r_f_s_g_playback__functions_1gab8b3a7e38b276a236ae435dc25c45271.html
- document_id: `rfsgplaybacklibrary-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Reads the waveforms from a TDMS file, and downloads one waveform into each of the NI RF vector signal generators. The first waveform in the TDMS file is downloaded to the first NI RF vector signal generator and so on, until all the waveforms are downloaded. This function reads the following informat

### niRFSGPlayback_ReadAndDownloadWaveformsFromFile

Reads the waveforms from a TDMS file, and downloads one waveform into each of the NI RF vector signal generators. The first waveform in the TDMS file is downloaded to the first NI RF vector signal generator and so on, until all the waveforms are downloaded. This function reads the following information from the TDMS file and writes it into the NI-RFSG waveform database:

#### Syntax

int32 __stdcall niRFSGPlayback_ReadAndDownloadWaveformsFromFile(ViSession[] rfsgSession, ViInt32 numberOfSessions, ViConstString filePath, ViConstString rfsgWaveformName)

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

If RF blanking marker locations are present in the file, but burst locations are not present, burst locations are calculated from RF blanking marker locations and stored in the NI-RFSG waveform database. 
 This function internally sets the NIRFSG_ATTR_POWER_LEVEL_TYPE attribute value to NIRFSG_VAL_PEAK_POWER before writing waveforms to NI-RFSG device memory. This function completes this tasks for each NI-RFSG session. 
 This function returns an error, if the number of waveforms in the TDMS file does not match the number of RFSG sessions.

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| rfsgSession | [out] | ViSession[] | Identifies the instrument session. rfsgSession is obtained from either the niRFSG_init function or the niRFSG_InitWithOptions function. |
| numberOfSessions | [in] | ViInt32 | Specifies the number of instrument sessions. |
| filePath | [in] | ViConstString | Specifies the absolute path to the TDMS file from which the playback library reads the waveforms. |
| rfsgWaveformName | [in] | ViConstString | Specifies the waveform name used to store the waveform in NI-RFSG device memory and waveform property in the NI-RFSG waveform database. |

#### Returns

Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred. To obtain a text description of the status code and additional information about the error condition, call the [niRFSGPlayback_GetError](group____root__ni_r_f_s_g_playback__functions_1ga5985403bcf5416e344ce264b3a73fc4a.html) function. The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

Functions

<!--NI_TOPIC bundle=rfsgplaybacklibrary-c-api-ref path=group____root__ni_r_f_s_g_playback__functions_1gaba56b0b57a2518be08015ea2473b0049.html language=enus -->
## TOPIC 00023: niRFSGPlayback_DownloadUserWaveformComplexF64Split

- bundle_id: `rfsgplaybacklibrary-c-api-ref`
- source_path: `group____root__ni_r_f_s_g_playback__functions_1gaba56b0b57a2518be08015ea2473b0049.html`
- source_url: https://docs-be.ni.com/bundle/rfsgplaybacklibrary-c-api-ref/raw/resource/enus/group____root__ni_r_f_s_g_playback__functions_1gaba56b0b57a2518be08015ea2473b0049.html
- document_id: `rfsgplaybacklibrary-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Normalizes the in-phase and quadrature-phase part of the input waveform and writes it into the NI RF vector signal generator. This VI computes the peak to average power ratio (PAPR) using the bursts in the waveform, stores the PAPR, sample rate, waveform size, and runtime scaling value of -1.5 dB in

### niRFSGPlayback_DownloadUserWaveformComplexF64Split

Normalizes the in-phase and quadrature-phase part of the input waveform and writes it into the NI RF vector signal generator. This VI computes the peak to average power ratio (PAPR) using the bursts in the waveform, stores the PAPR, sample rate, waveform size, and runtime scaling value of -1.5 dB in the NI-RFSG waveform database.

#### Syntax

int32 __stdcall niRFSGPlayback_DownloadUserWaveformComplexF64Split(ViSession rfsgSession, ViConstString rfsgWaveformName, ViReal64 t0, ViReal64 dt, ViReal64[] i, ViReal64[] q, ViInt32 waveformSize, ViInt32 burstPresent)

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| rfsgSession | [in] | ViSession | Identifies the instrument session. rfsgSession is obtained from either the niRFSG_init function or the niRFSG_InitWithOptions function. |
| rfsgWaveformName | [in] | ViConstString | Specifies the name used to write the waveform to the NI-RFSG device memory. |
| t0 | [in] | ViReal64 | Specifies the start time of the given input waveform. |
| dt | [in] | ViReal64 | Specifies the time interval between the samples in the given input waveform. |
| i | [out] | ViReal64[] | Returns the in-phase part of the input waveform. |
| q | [out] | ViReal64[] | Returns the quadrature-phase part of the input waveform. |
| waveformSize | [in] | ViInt32 | Specifies the size of the waveform array. |
| burstPresent | [in] | ViInt32 | Specifies whether the burst is present in the given waveform. |

#### Returns

Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred. To obtain a text description of the status code and additional information about the error condition, call the [niRFSGPlayback_GetError](group____root__ni_r_f_s_g_playback__functions_1ga5985403bcf5416e344ce264b3a73fc4a.html) function. The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

Functions

<!--NI_TOPIC bundle=rfsgplaybacklibrary-c-api-ref path=group____root__ni_r_f_s_g_playback__functions_1gac66e26960f90bd3bc9562236f95daddd.html language=enus -->
## TOPIC 00024: niRFSGPlayback_ReadWaveformFromFileByIndexComplexF64

- bundle_id: `rfsgplaybacklibrary-c-api-ref`
- source_path: `group____root__ni_r_f_s_g_playback__functions_1gac66e26960f90bd3bc9562236f95daddd.html`
- source_url: https://docs-be.ni.com/bundle/rfsgplaybacklibrary-c-api-ref/raw/resource/enus/group____root__ni_r_f_s_g_playback__functions_1gac66e26960f90bd3bc9562236f95daddd.html
- document_id: `rfsgplaybacklibrary-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Reads the waveform from file and returns the waveform in an output parameter. Syntaxint32 __stdcall niRFSGPlayback_ReadWaveformFromFileByIndexComplexF64(ViConstString filePath, ViInt32 waveformIndex, ViInt32 outputWaveformBufferSize, ViReal64 t0, ViReal64 dt, NIComplexNumber[] outputWaveform, ViInt3

### niRFSGPlayback_ReadWaveformFromFileByIndexComplexF64

Reads the waveform from file and returns the waveform in an output parameter.

#### Syntax

int32 __stdcall niRFSGPlayback_ReadWaveformFromFileByIndexComplexF64(ViConstString filePath, ViInt32 waveformIndex, ViInt32 outputWaveformBufferSize, ViReal64 t0, ViReal64 dt, NIComplexNumber[] outputWaveform, ViInt32 actualWaveformSize)

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| filePath | [in] | ViConstString | Specifies the absolute path to the TDMS file from which the playback library reads the waveforms. |
| waveformIndex | [in] | ViInt32 | Specifies the index of the waveform that you want to read from the TDMS file. |
| outputWaveformBufferSize | [in] | ViInt32 | Specifies the size of the outputWaveform array. Set the outputWaveformBufferSize parameter to 0 to get the size of the outputWaveform array in the actualWaveformSize parameter. |
| t0 | [out] | ViReal64 | This element should be ignored. |
| dt | [out] | ViReal64 | Returns the inverse of the sample rate of the waveform. |
| outputWaveform | [out] | NIComplexNumber[] | Returns the complex waveform samples stored in an array. |
| actualWaveformSize | [out] | ViInt32 | Returns the actual size of the array, if you pass NULL to all output array parameters, and set the outputWaveformBufferSize parameter to 0. |

#### Returns

Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred. To obtain a text description of the status code and additional information about the error condition, call the [niRFSGPlayback_GetError](group____root__ni_r_f_s_g_playback__functions_1ga5985403bcf5416e344ce264b3a73fc4a.html) function. The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

Functions

<!--NI_TOPIC bundle=rfsgplaybacklibrary-c-api-ref path=group____root__ni_r_f_s_g_playback__functions_1gaf53459e2e85ad1b4539e9b1828f2378a.html language=enus -->
## TOPIC 00025: niRFSGPlayback_ReadWaveformFromFileComplexF32

- bundle_id: `rfsgplaybacklibrary-c-api-ref`
- source_path: `group____root__ni_r_f_s_g_playback__functions_1gaf53459e2e85ad1b4539e9b1828f2378a.html`
- source_url: https://docs-be.ni.com/bundle/rfsgplaybacklibrary-c-api-ref/raw/resource/enus/group____root__ni_r_f_s_g_playback__functions_1gaf53459e2e85ad1b4539e9b1828f2378a.html
- document_id: `rfsgplaybacklibrary-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Reads the waveform from file and returns the waveform in an output parameter. Syntaxint32 __stdcall niRFSGPlayback_ReadWaveformFromFileComplexF32(ViConstString filePath, ViInt32 outputWaveformBufferSize, ViReal64 t0, ViReal64 dt, NIComplexNumberF32[] outputWaveform, ViInt32 actualWaveformSize)Parame

### niRFSGPlayback_ReadWaveformFromFileComplexF32

Reads the waveform from file and returns the waveform in an output parameter.

#### Syntax

int32 __stdcall niRFSGPlayback_ReadWaveformFromFileComplexF32(ViConstString filePath, ViInt32 outputWaveformBufferSize, ViReal64 t0, ViReal64 dt, NIComplexNumberF32[] outputWaveform, ViInt32 actualWaveformSize)

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| filePath | [in] | ViConstString | Specifies the absolute path to the TDMS file from which the playback library reads the waveforms. |
| outputWaveformBufferSize | [in] | ViInt32 | Specifies the size of the outputWaveform array. Set the outputWaveformBufferSize parameter to 0 to get the size of the outputWaveform array in the actualWaveformSize parameter. |
| t0 | [out] | ViReal64 | This element should be ignored. |
| dt | [out] | ViReal64 | Returns the inverse of the sample rate of the waveform. |
| outputWaveform | [out] | NIComplexNumberF32[] | Returns the complex waveform samples stored in an array. |
| actualWaveformSize | [out] | ViInt32 | Returns the actual size of the array, if you pass NULL to all output array parameters, and set the outputWaveformBufferSize parameter to 0. |

#### Returns

Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred. To obtain a text description of the status code and additional information about the error condition, call the [niRFSGPlayback_GetError](group____root__ni_r_f_s_g_playback__functions_1ga5985403bcf5416e344ce264b3a73fc4a.html) function. The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

Functions

<!--NI_TOPIC bundle=rfsgplaybacklibrary-c-api-ref path=group____root__ni_r_f_s_g_playback__functions__advanced.html language=enus -->
## TOPIC 00026: Advanced

- bundle_id: `rfsgplaybacklibrary-c-api-ref`
- source_path: `group____root__ni_r_f_s_g_playback__functions__advanced.html`
- source_url: https://docs-be.ni.com/bundle/rfsgplaybacklibrary-c-api-ref/raw/resource/enus/group____root__ni_r_f_s_g_playback__functions__advanced.html
- document_id: `rfsgplaybacklibrary-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: GroupsObsoleteGroup membersNameDescriptionniRFSGPlayback_RetrieveAutomaticSGSASharedLOReturns the value of automaticSGSASharedLO parameter. niRFSGPlayback_RetrieveDownloadedWaveformNamesReturns the names of the waveforms that are stored in the NI-RFSG waveform database. niRFSGPlayback_RetrieveWavefo

### Advanced

#### Groups

- Obsolete

#### Group members

| Name | Description |
| --- | --- |
| niRFSGPlayback_RetrieveAutomaticSGSASharedLO | Returns the value of automaticSGSASharedLO parameter. |
| niRFSGPlayback_RetrieveDownloadedWaveformNames | Returns the names of the waveforms that are stored in the NI-RFSG waveform database. |
| niRFSGPlayback_RetrieveWaveformBurstStartLocations | Returns the burst start locations stored in the NI-RFSG waveform database. This function uses the waveformName as the key to retrieve the waveform property. |
| niRFSGPlayback_RetrieveWaveformBurstStopLocations | Returns burst stop locations stored in the NI-RFSG waveform database. This function uses the waveformName as the key to retrieve the waveform property. |
| niRFSGPlayback_RetrieveWaveformFileVersion | Returns the waveform file version of the waveform stored in the NI-RFSG waveform database. This function uses the waveformName as the key to retrieve the waveform property. |
| niRFSGPlayback_RetrieveWaveformLOOffsetMode | Returns the LO offset mode value stored in the NI-RFSG waveform database. This function uses the waveformName as the key to retrieve the waveform property. |
| niRFSGPlayback_RetrieveWaveformPAPR | Returns the peak to average power ratio (PAPR) stored in the NI-RFSG waveform database. This function uses the waveformName as the key to retrieve the waveform property. |
| niRFSGPlayback_RetrieveWaveformRFBlankingEnabled | Returns the RF blanking enabled value stored in the NI-RFSG waveform database. This function uses the waveformName as the key to retrieve the waveform property. |
| niRFSGPlayback_RetrieveWaveformRuntimeScaling | Returns the runtime scaling value stored in the NI-RFSG waveform database. This function uses the waveformName as the key to retrieve the waveform property. |
| niRFSGPlayback_RetrieveWaveformSampleRate | Returns the sample rate stored in NI-RFSG waveform database. This function uses the waveformName parameter as the key to retrieve the waveform property. |
| niRFSGPlayback_RetrieveWaveformSignalBandwidth | Returns the signal bandwidth stored in the NI-RFSG waveform database. This function uses the waveformName as the key to retrieve the waveform property. |
| niRFSGPlayback_RetrieveWaveformSize | Returns the size of the waveform stored in the NI-RFSG waveform database. This function uses the waveformName as the key to retrieve the waveform property. |
| niRFSGPlayback_StoreAutomaticSGSASharedLO | Stores whether the signal generator's LO signal can be shared on request by the RFmx driver. It is recommended to use Automatic sharing of local oscillator (LO) in test setups that use a vector signal transceiver (VST) with the NI-RFSG to generate a signal at the DUT's input and the RFmx driver to measure the signal at the DUT's output. |
| niRFSGPlayback_StoreWaveformBurstStartLocations | Stores the burst start location, which you specify in the burstStartLocations parameter, in the NI-RFSG waveform database. |
| niRFSGPlayback_StoreWaveformBurstStopLocations | Stores the burst stop location, which you specify in the burstStopLocations parameter, in the NI-RFSG waveform database. |
| niRFSGPlayback_StoreWaveformLOOffsetMode | Stores the LO offset mode value, which you specify in the LOOffsetMode parameter, in the NI-RFSG waveform database. |
| niRFSGPlayback_StoreWaveformPAPR | Stores the peak to average power ratio (PAPR), which you specify in the PAPR parameter, in the NI-RFSG waveform database. |
| niRFSGPlayback_StoreWaveformRFBlankingEnabled | Stores the RF blanking enabled value, which you specify in the rfBlankingEnabled parameter, in the NI-RFSG waveform database. |
| niRFSGPlayback_StoreWaveformRFBlankingMarkerSource | Stores the RF blanking marker source, which you specify in the markerSource parameter, in the NI-RFSG waveform database. |
| niRFSGPlayback_StoreWaveformRuntimeScaling | Stores the runtime scaling value, which you specify in the runtimeScaling parameter, in the NI-RFSG waveform database. |
| niRFSGPlayback_StoreWaveformSampleRate | Stores the sample rate, which you specify in the sampleRate parameter, in the NI-RFSG waveform database. |
| niRFSGPlayback_StoreWaveformSignalBandwidth | Stores the signal bandwidth, which you specify in the signalBandwidth parameter, in the NI-RFSG waveform database. |
| niRFSGPlayback_StoreWaveformSize | Stores the size of the waveform, which you specify in the waveformSize parameter, in the NI-RFSG waveform database. |

#### Attachments

None

Parent topic:

Functions

<!--NI_TOPIC bundle=rfsgplaybacklibrary-c-api-ref path=group____root__ni_r_f_s_g_playback__functions__advanced_1ga0a5dda804c75e62ac092e8b1466663c7.html language=enus -->
## TOPIC 00027: niRFSGPlayback_StoreWaveformRFBlankingMarkerSource

- bundle_id: `rfsgplaybacklibrary-c-api-ref`
- source_path: `group____root__ni_r_f_s_g_playback__functions__advanced_1ga0a5dda804c75e62ac092e8b1466663c7.html`
- source_url: https://docs-be.ni.com/bundle/rfsgplaybacklibrary-c-api-ref/raw/resource/enus/group____root__ni_r_f_s_g_playback__functions__advanced_1ga0a5dda804c75e62ac092e8b1466663c7.html
- document_id: `rfsgplaybacklibrary-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Stores the RF blanking marker source, which you specify in the markerSource parameter, in the NI-RFSG waveform database. Syntaxint32 __stdcall niRFSGPlayback_StoreWaveformRFBlankingMarkerSource(ViSession rfsgSession, ViConstString waveformName, const ViChar[] markerSource)ParametersNameDirectionType

### niRFSGPlayback_StoreWaveformRFBlankingMarkerSource

Stores the RF blanking marker source, which you specify in the **markerSource** parameter, in the NI-RFSG waveform database.

#### Syntax

int32 __stdcall niRFSGPlayback_StoreWaveformRFBlankingMarkerSource(ViSession rfsgSession, ViConstString waveformName, const ViChar[] markerSource)

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| rfsgSession | [in] | ViSession | Identifies the instrument session. rfsgSession is obtained from either the niRFSG_init function or the niRFSG_InitWithOptions function. |
| waveformName | [in] | ViConstString | Specifies the waveform name for which you want to store RF blanking marker source. |
| markerSource | [in] | const ViChar[] | Specifies the RF blanking marker source to store in the NI-RFSG waveform database.NameValueNIRFSG_VAL_MARKER0RF blanking is tied to marker0 event.NIRFSG_VAL_MARKER1RF blanking is tied to marker1 event.NIRFSG_VAL_MARKER2RF blanking is tied to marker2 event.NIRFSG_VAL_MARKER3RF blanking is tied to marker3 event. |
| Name | Value |  |  |
| NIRFSG_VAL_MARKER0 | RF blanking is tied to marker0 event. |  |  |
| NIRFSG_VAL_MARKER1 | RF blanking is tied to marker1 event. |  |  |
| NIRFSG_VAL_MARKER2 | RF blanking is tied to marker2 event. |  |  |
| NIRFSG_VAL_MARKER3 | RF blanking is tied to marker3 event. |  |  |

#### Returns

Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred. To obtain a text description of the status code and additional information about the error condition, call the [niRFSGPlayback_GetError](group____root__ni_r_f_s_g_playback__functions_1ga5985403bcf5416e344ce264b3a73fc4a.html) function. The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

Advanced

<!--NI_TOPIC bundle=rfsgplaybacklibrary-c-api-ref path=group____root__ni_r_f_s_g_playback__functions__advanced_1ga1a626b3b77b2c91da56d67c21ab04e00.html language=enus -->
## TOPIC 00028: niRFSGPlayback_StoreWaveformBurstStartLocations

- bundle_id: `rfsgplaybacklibrary-c-api-ref`
- source_path: `group____root__ni_r_f_s_g_playback__functions__advanced_1ga1a626b3b77b2c91da56d67c21ab04e00.html`
- source_url: https://docs-be.ni.com/bundle/rfsgplaybacklibrary-c-api-ref/raw/resource/enus/group____root__ni_r_f_s_g_playback__functions__advanced_1ga1a626b3b77b2c91da56d67c21ab04e00.html
- document_id: `rfsgplaybacklibrary-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Stores the burst start location, which you specify in the burstStartLocations parameter, in the NI-RFSG waveform database. Syntaxint32 __stdcall niRFSGPlayback_StoreWaveformBurstStartLocations(ViSession rfsgSession, ViConstString waveformName, ViInt32[] burstStartLocations, ViInt32 numberOfLocations

### niRFSGPlayback_StoreWaveformBurstStartLocations

Stores the burst start location, which you specify in the **burstStartLocations** parameter, in the NI-RFSG waveform database.

#### Syntax

int32 __stdcall niRFSGPlayback_StoreWaveformBurstStartLocations(ViSession rfsgSession, ViConstString waveformName, ViInt32[] burstStartLocations, ViInt32 numberOfLocations)

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| rfsgSession | [in] | ViSession | Identifies the instrument session. rfsgSession is obtained from either the niRFSG_init function or the niRFSG_InitWithOptions function. |
| waveformName | [in] | ViConstString | Specifies the waveform name for which you want to store the burst start locations. |
| burstStartLocations | [out] | ViInt32[] | Specifies an array of the burst start locations to store in the NI-RFSG waveform database. |
| numberOfLocations | [in] | ViInt32 | Specifies the number of burst start locations. |

#### Returns

Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred. To obtain a text description of the status code and additional information about the error condition, call the [niRFSGPlayback_GetError](group____root__ni_r_f_s_g_playback__functions_1ga5985403bcf5416e344ce264b3a73fc4a.html) function. The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

Advanced

<!--NI_TOPIC bundle=rfsgplaybacklibrary-c-api-ref path=group____root__ni_r_f_s_g_playback__functions__advanced_1ga1f072f34464ce3ab043d7325dc8bcaa4.html language=enus -->
## TOPIC 00029: niRFSGPlayback_StoreWaveformBurstStopLocations

- bundle_id: `rfsgplaybacklibrary-c-api-ref`
- source_path: `group____root__ni_r_f_s_g_playback__functions__advanced_1ga1f072f34464ce3ab043d7325dc8bcaa4.html`
- source_url: https://docs-be.ni.com/bundle/rfsgplaybacklibrary-c-api-ref/raw/resource/enus/group____root__ni_r_f_s_g_playback__functions__advanced_1ga1f072f34464ce3ab043d7325dc8bcaa4.html
- document_id: `rfsgplaybacklibrary-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Stores the burst stop location, which you specify in the burstStopLocations parameter, in the NI-RFSG waveform database. Syntaxint32 __stdcall niRFSGPlayback_StoreWaveformBurstStopLocations(ViSession rfsgSession, ViConstString waveformName, ViInt32[] burstStopLocations, ViInt32 numberOfLocations)Par

### niRFSGPlayback_StoreWaveformBurstStopLocations

Stores the burst stop location, which you specify in the **burstStopLocations** parameter, in the NI-RFSG waveform database.

#### Syntax

int32 __stdcall niRFSGPlayback_StoreWaveformBurstStopLocations(ViSession rfsgSession, ViConstString waveformName, ViInt32[] burstStopLocations, ViInt32 numberOfLocations)

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| rfsgSession | [in] | ViSession | Identifies the instrument session. rfsgSession is obtained from either the niRFSG_init function or the niRFSG_InitWithOptions function. |
| waveformName | [in] | ViConstString | Specifies the waveform name for which you want to store the burst stop locations. |
| burstStopLocations | [out] | ViInt32[] | Specifies an array of the burst stop locations to store in the NI-RFSG waveform database. |
| numberOfLocations | [in] | ViInt32 | Specifies the number of burst stop locations. |

#### Returns

Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred. To obtain a text description of the status code and additional information about the error condition, call the [niRFSGPlayback_GetError](group____root__ni_r_f_s_g_playback__functions_1ga5985403bcf5416e344ce264b3a73fc4a.html) function. The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

Advanced

<!--NI_TOPIC bundle=rfsgplaybacklibrary-c-api-ref path=group____root__ni_r_f_s_g_playback__functions__advanced_1ga268531d736c3708038c062eee24cc174.html language=enus -->
## TOPIC 00030: niRFSGPlayback_RetrieveWaveformRuntimeScaling

- bundle_id: `rfsgplaybacklibrary-c-api-ref`
- source_path: `group____root__ni_r_f_s_g_playback__functions__advanced_1ga268531d736c3708038c062eee24cc174.html`
- source_url: https://docs-be.ni.com/bundle/rfsgplaybacklibrary-c-api-ref/raw/resource/enus/group____root__ni_r_f_s_g_playback__functions__advanced_1ga268531d736c3708038c062eee24cc174.html
- document_id: `rfsgplaybacklibrary-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the runtime scaling value stored in the NI-RFSG waveform database. This function uses the waveformName as the key to retrieve the waveform property. Syntaxint32 __stdcall niRFSGPlayback_RetrieveWaveformRuntimeScaling(ViSession rfsgSession, ViConstString waveformName, ViReal64 runtimeScaling)

### niRFSGPlayback_RetrieveWaveformRuntimeScaling

Returns the runtime scaling value stored in the NI-RFSG waveform database. This function uses the **waveformName** as the key to retrieve the waveform property.

#### Syntax

int32 __stdcall niRFSGPlayback_RetrieveWaveformRuntimeScaling(ViSession rfsgSession, ViConstString waveformName, ViReal64 runtimeScaling)

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| rfsgSession | [in] | ViSession | Identifies the instrument session. rfsgSession is obtained from either the niRFSG_init function or the niRFSG_InitWithOptions function. |
| waveformName | [in] | ViConstString | Specifies the name of the waveform for which you want to retrieve the runtime scaling value. |
| runtimeScaling | [out] | ViReal64 | Returns the runtime scaling value stored in the NI-RFSG waveform database for the waveform you specified in the waveformName parameter. This value is expressed in dB. |

#### Returns

Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred. To obtain a text description of the status code and additional information about the error condition, call the [niRFSGPlayback_GetError](group____root__ni_r_f_s_g_playback__functions_1ga5985403bcf5416e344ce264b3a73fc4a.html) function. The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

Advanced

<!--NI_TOPIC bundle=rfsgplaybacklibrary-c-api-ref path=group____root__ni_r_f_s_g_playback__functions__advanced_1ga2b92a6b6b3eb010ba68b2fc8c55ab51f.html language=enus -->
## TOPIC 00031: niRFSGPlayback_RetrieveDownloadedWaveformNames

- bundle_id: `rfsgplaybacklibrary-c-api-ref`
- source_path: `group____root__ni_r_f_s_g_playback__functions__advanced_1ga2b92a6b6b3eb010ba68b2fc8c55ab51f.html`
- source_url: https://docs-be.ni.com/bundle/rfsgplaybacklibrary-c-api-ref/raw/resource/enus/group____root__ni_r_f_s_g_playback__functions__advanced_1ga2b92a6b6b3eb010ba68b2fc8c55ab51f.html
- document_id: `rfsgplaybacklibrary-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the names of the waveforms that are stored in the NI-RFSG waveform database. Syntaxint32 __stdcall niRFSGPlayback_RetrieveDownloadedWaveformNames(ViSession rfsgSession, ViInt32 outputWaveformNamesBufferSize, ViChar waveformNames)ParametersNameDirectionTypeDescriptionrfsgSession[in]ViSessionI

### niRFSGPlayback_RetrieveDownloadedWaveformNames

Returns the names of the waveforms that are stored in the NI-RFSG waveform database.

#### Syntax

int32 __stdcall niRFSGPlayback_RetrieveDownloadedWaveformNames(ViSession rfsgSession, ViInt32 outputWaveformNamesBufferSize, ViChar waveformNames)

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| rfsgSession | [in] | ViSession | Identifies the instrument session. rfsgSession is obtained from either the niRFSG_init function or the niRFSG_InitWithOptions function. |
| outputWaveformNamesBufferSize | [in] | ViInt32 | Specifies the number of elements in the waveformNames parameter. |
| waveformNames | [out] | ViChar | Returns an array of the waveform names that are stored in the NI-RFSG waveform database. |

#### Returns

Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred. To obtain a text description of the status code and additional information about the error condition, call the [niRFSGPlayback_GetError](group____root__ni_r_f_s_g_playback__functions_1ga5985403bcf5416e344ce264b3a73fc4a.html) function. The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

Advanced

<!--NI_TOPIC bundle=rfsgplaybacklibrary-c-api-ref path=group____root__ni_r_f_s_g_playback__functions__advanced_1ga449c2734384a50b244da57c364033c5b.html language=enus -->
## TOPIC 00032: niRFSGPlayback_StoreWaveformRuntimeScaling

- bundle_id: `rfsgplaybacklibrary-c-api-ref`
- source_path: `group____root__ni_r_f_s_g_playback__functions__advanced_1ga449c2734384a50b244da57c364033c5b.html`
- source_url: https://docs-be.ni.com/bundle/rfsgplaybacklibrary-c-api-ref/raw/resource/enus/group____root__ni_r_f_s_g_playback__functions__advanced_1ga449c2734384a50b244da57c364033c5b.html
- document_id: `rfsgplaybacklibrary-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Stores the runtime scaling value, which you specify in the runtimeScaling parameter, in the NI-RFSG waveform database. Syntaxint32 __stdcall niRFSGPlayback_StoreWaveformRuntimeScaling(ViSession rfsgSession, ViConstString waveformName, ViReal64 runtimeScaling)ParametersNameDirectionTypeDescriptionrfs

### niRFSGPlayback_StoreWaveformRuntimeScaling

Stores the runtime scaling value, which you specify in the **runtimeScaling** parameter, in the NI-RFSG waveform database.

#### Syntax

int32 __stdcall niRFSGPlayback_StoreWaveformRuntimeScaling(ViSession rfsgSession, ViConstString waveformName, ViReal64 runtimeScaling)

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| rfsgSession | [in] | ViSession | Identifies the instrument session. rfsgSession is obtained from either the niRFSG_init function or the niRFSG_InitWithOptions function. |
| waveformName | [in] | ViConstString | Specifies the waveform name for which you want to store runtime scaling value. |
| runtimeScaling | [in] | ViReal64 | Specifies the runtime scaling value to store in the NI-RFSG database. This value is expressed in dB. |

#### Returns

Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred. To obtain a text description of the status code and additional information about the error condition, call the [niRFSGPlayback_GetError](group____root__ni_r_f_s_g_playback__functions_1ga5985403bcf5416e344ce264b3a73fc4a.html) function. The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

Advanced

<!--NI_TOPIC bundle=rfsgplaybacklibrary-c-api-ref path=group____root__ni_r_f_s_g_playback__functions__advanced_1ga4d3471d0d2b631e0a6e0b54963bf26f2.html language=enus -->
## TOPIC 00033: niRFSGPlayback_RetrieveWaveformSampleRate

- bundle_id: `rfsgplaybacklibrary-c-api-ref`
- source_path: `group____root__ni_r_f_s_g_playback__functions__advanced_1ga4d3471d0d2b631e0a6e0b54963bf26f2.html`
- source_url: https://docs-be.ni.com/bundle/rfsgplaybacklibrary-c-api-ref/raw/resource/enus/group____root__ni_r_f_s_g_playback__functions__advanced_1ga4d3471d0d2b631e0a6e0b54963bf26f2.html
- document_id: `rfsgplaybacklibrary-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the sample rate stored in NI-RFSG waveform database. This function uses the waveformName parameter as the key to retrieve the waveform property. Syntaxint32 __stdcall niRFSGPlayback_RetrieveWaveformSampleRate(ViSession rfsgSession, ViConstString waveformName, ViReal64 sampleRate)ParametersNa

### niRFSGPlayback_RetrieveWaveformSampleRate

Returns the sample rate stored in NI-RFSG waveform database. This function uses the **waveformName** parameter as the key to retrieve the waveform property.

#### Syntax

int32 __stdcall niRFSGPlayback_RetrieveWaveformSampleRate(ViSession rfsgSession, ViConstString waveformName, ViReal64 sampleRate)

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| rfsgSession | [in] | ViSession | Identifies the instrument session. rfsgSession is obtained from either the niRFSG_init function or the niRFSG_InitWithOptions function. |
| waveformName | [in] | ViConstString | Specifies the waveform name for which you want to retrieve the sample rate value. |
| sampleRate | [out] | ViReal64 | Returns the sampling rate stored in the NI-RFSG waveform database for the waveform you specified in the waveformName parameter. This value is expressed in samples per second (S/s). |

#### Returns

Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred. To obtain a text description of the status code and additional information about the error condition, call the [niRFSGPlayback_GetError](group____root__ni_r_f_s_g_playback__functions_1ga5985403bcf5416e344ce264b3a73fc4a.html) function. The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

Advanced

<!--NI_TOPIC bundle=rfsgplaybacklibrary-c-api-ref path=group____root__ni_r_f_s_g_playback__functions__advanced_1ga4d948ad9f90b57727579c0d6491fae13.html language=enus -->
## TOPIC 00034: niRFSGPlayback_RetrieveAutomaticSGSASharedLO

- bundle_id: `rfsgplaybacklibrary-c-api-ref`
- source_path: `group____root__ni_r_f_s_g_playback__functions__advanced_1ga4d948ad9f90b57727579c0d6491fae13.html`
- source_url: https://docs-be.ni.com/bundle/rfsgplaybacklibrary-c-api-ref/raw/resource/enus/group____root__ni_r_f_s_g_playback__functions__advanced_1ga4d948ad9f90b57727579c0d6491fae13.html
- document_id: `rfsgplaybacklibrary-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the value of automaticSGSASharedLO parameter. Syntaxint32 __stdcall niRFSGPlayback_RetrieveAutomaticSGSASharedLO(ViSession rfsgSession, ViConstString channelName, ViInt32 automaticSGSASharedLO)ParametersNameDirectionTypeDescriptionrfsgSession[in]ViSessionIdentifies the instrument session. rf

### niRFSGPlayback_RetrieveAutomaticSGSASharedLO

Returns the value of **automaticSGSASharedLO** parameter.

#### Syntax

int32 __stdcall niRFSGPlayback_RetrieveAutomaticSGSASharedLO(ViSession rfsgSession, ViConstString channelName, ViInt32 automaticSGSASharedLO)

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| rfsgSession | [in] | ViSession | Identifies the instrument session. rfsgSession is obtained from either the niRFSG_init function or the niRFSG_InitWithOptions function. |
| channelName | [in] | ViConstString | This parameter is reserved for future use. |
| automaticSGSASharedLO | [out] | ViInt32 | Returns the access control of NI-RFSG LO Out Export. |

#### Returns

Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred. To obtain a text description of the status code and additional information about the error condition, call the [niRFSGPlayback_GetError](group____root__ni_r_f_s_g_playback__functions_1ga5985403bcf5416e344ce264b3a73fc4a.html) function. The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

Advanced

<!--NI_TOPIC bundle=rfsgplaybacklibrary-c-api-ref path=group____root__ni_r_f_s_g_playback__functions__advanced_1ga505ce997180b63113eb86f7d821c99e7.html language=enus -->
## TOPIC 00035: niRFSGPlayback_RetrieveWaveformBurstStartLocations

- bundle_id: `rfsgplaybacklibrary-c-api-ref`
- source_path: `group____root__ni_r_f_s_g_playback__functions__advanced_1ga505ce997180b63113eb86f7d821c99e7.html`
- source_url: https://docs-be.ni.com/bundle/rfsgplaybacklibrary-c-api-ref/raw/resource/enus/group____root__ni_r_f_s_g_playback__functions__advanced_1ga505ce997180b63113eb86f7d821c99e7.html
- document_id: `rfsgplaybacklibrary-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the burst start locations stored in the NI-RFSG waveform database. This function uses the waveformName as the key to retrieve the waveform property. Syntaxint32 __stdcall niRFSGPlayback_RetrieveWaveformBurstStartLocations(ViSession rfsgSession, ViConstString waveformName, ViInt32 burstStartL

### niRFSGPlayback_RetrieveWaveformBurstStartLocations

Returns the burst start locations stored in the NI-RFSG waveform database. This function uses the **waveformName** as the key to retrieve the waveform property.

#### Syntax

int32 __stdcall niRFSGPlayback_RetrieveWaveformBurstStartLocations(ViSession rfsgSession, ViConstString waveformName, ViInt32 burstStartLocationsSize, ViInt32[] burstStartLocations, ViInt32 actualNumberOfLocations)

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| rfsgSession | [in] | ViSession | Identifies the instrument session. rfsgSession is obtained from either the niRFSG_init function or the niRFSG_InitWithOptions function. |
| waveformName | [in] | ViConstString | Specifies the waveform name for which you want to retrieve the the burst start locations. |
| burstStartLocationsSize | [in] | ViInt32 | Specifies the size of the burstStartLocations array. Set the burstStartLocationsSize parameter to 0 to get the size of the burstStartLocations array in the actualNumberOfLocations parameter. |
| burstStartLocations | [out] | ViInt32[] | Returns the array of burst start locations, stored in the NI-RFSG waveform database, for the waveform you specified in the waveformName parameter. |
| actualNumberOfLocations | [out] | ViInt32 | Returns the actual size of the array, if you pass NULL to all output array parameters, and set the burstStartLocationsSize parameter to 0. |

#### Returns

Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred. To obtain a text description of the status code and additional information about the error condition, call the [niRFSGPlayback_GetError](group____root__ni_r_f_s_g_playback__functions_1ga5985403bcf5416e344ce264b3a73fc4a.html) function. The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

Advanced

<!--NI_TOPIC bundle=rfsgplaybacklibrary-c-api-ref path=group____root__ni_r_f_s_g_playback__functions__advanced_1ga64186af8aa30c8ab65a50d3f6f3e31f2.html language=enus -->
## TOPIC 00036: niRFSGPlayback_RetrieveWaveformPAPR

- bundle_id: `rfsgplaybacklibrary-c-api-ref`
- source_path: `group____root__ni_r_f_s_g_playback__functions__advanced_1ga64186af8aa30c8ab65a50d3f6f3e31f2.html`
- source_url: https://docs-be.ni.com/bundle/rfsgplaybacklibrary-c-api-ref/raw/resource/enus/group____root__ni_r_f_s_g_playback__functions__advanced_1ga64186af8aa30c8ab65a50d3f6f3e31f2.html
- document_id: `rfsgplaybacklibrary-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the peak to average power ratio (PAPR) stored in the NI-RFSG waveform database. This function uses the waveformName as the key to retrieve the waveform property. Syntaxint32 __stdcall niRFSGPlayback_RetrieveWaveformPAPR(ViSession rfsgSession, ViConstString waveformName, ViReal64 loOffsetMode

### niRFSGPlayback_RetrieveWaveformPAPR

Returns the peak to average power ratio (PAPR) stored in the NI-RFSG waveform database. This function uses the **waveformName** as the key to retrieve the waveform property.

#### Syntax

int32 __stdcall niRFSGPlayback_RetrieveWaveformPAPR(ViSession rfsgSession, ViConstString waveformName, ViReal64 loOffsetMode)

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| rfsgSession | [in] | ViSession | Identifies the instrument session. rfsgSession is obtained from either the niRFSG_init function or the niRFSG_InitWithOptions function. |
| waveformName | [in] | ViConstString | Specifies the name of the waveform for which you want to retrieve the PAPR. |
| loOffsetMode | [out] | ViReal64 | Returns the PAPR stored in the NI-RFSG waveform database for the waveform you specified in the waveformName parameter. This value is expressed in dB. |

#### Returns

Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred. To obtain a text description of the status code and additional information about the error condition, call the [niRFSGPlayback_GetError](group____root__ni_r_f_s_g_playback__functions_1ga5985403bcf5416e344ce264b3a73fc4a.html) function. The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

Advanced

<!--NI_TOPIC bundle=rfsgplaybacklibrary-c-api-ref path=group____root__ni_r_f_s_g_playback__functions__advanced_1ga6dcb38a60464fa29dd8ab5e8b9007cb0.html language=enus -->
## TOPIC 00037: niRFSGPlayback_StoreWaveformSignalBandwidth

- bundle_id: `rfsgplaybacklibrary-c-api-ref`
- source_path: `group____root__ni_r_f_s_g_playback__functions__advanced_1ga6dcb38a60464fa29dd8ab5e8b9007cb0.html`
- source_url: https://docs-be.ni.com/bundle/rfsgplaybacklibrary-c-api-ref/raw/resource/enus/group____root__ni_r_f_s_g_playback__functions__advanced_1ga6dcb38a60464fa29dd8ab5e8b9007cb0.html
- document_id: `rfsgplaybacklibrary-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Stores the signal bandwidth, which you specify in the signalBandwidth parameter, in the NI-RFSG waveform database. Syntaxint32 __stdcall niRFSGPlayback_StoreWaveformSignalBandwidth(ViSession rfsgSession, ViConstString waveformName, ViReal64 signalBandwidth)ParametersNameDirectionTypeDescriptionrfsgS

### niRFSGPlayback_StoreWaveformSignalBandwidth

Stores the signal bandwidth, which you specify in the **signalBandwidth** parameter, in the NI-RFSG waveform database.

#### Syntax

int32 __stdcall niRFSGPlayback_StoreWaveformSignalBandwidth(ViSession rfsgSession, ViConstString waveformName, ViReal64 signalBandwidth)

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| rfsgSession | [in] | ViSession | Identifies the instrument session. rfsgSession is obtained from either the niRFSG_init function or the niRFSG_InitWithOptions function. |
| waveformName | [in] | ViConstString | Specifies the waveform name for which you want to store the signal bandwidth. |
| signalBandwidth | [in] | ViReal64 | Specifies the signal bandwidth to store in the NI-RFSG waveform database. |

#### Returns

Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred. To obtain a text description of the status code and additional information about the error condition, call the [niRFSGPlayback_GetError](group____root__ni_r_f_s_g_playback__functions_1ga5985403bcf5416e344ce264b3a73fc4a.html) function. The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

Advanced

<!--NI_TOPIC bundle=rfsgplaybacklibrary-c-api-ref path=group____root__ni_r_f_s_g_playback__functions__advanced_1ga7eb5e0ebed4a41f93881ff42972fdf1f.html language=enus -->
## TOPIC 00038: niRFSGPlayback_RetrieveWaveformFileVersion

- bundle_id: `rfsgplaybacklibrary-c-api-ref`
- source_path: `group____root__ni_r_f_s_g_playback__functions__advanced_1ga7eb5e0ebed4a41f93881ff42972fdf1f.html`
- source_url: https://docs-be.ni.com/bundle/rfsgplaybacklibrary-c-api-ref/raw/resource/enus/group____root__ni_r_f_s_g_playback__functions__advanced_1ga7eb5e0ebed4a41f93881ff42972fdf1f.html
- document_id: `rfsgplaybacklibrary-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the waveform file version of the waveform stored in the NI-RFSG waveform database. This function uses the waveformName as the key to retrieve the waveform property. Syntaxint32 __stdcall niRFSGPlayback_RetrieveWaveformFileVersion(ViSession rfsgSession, ViConstString waveformName, ViInt32 wav

### niRFSGPlayback_RetrieveWaveformFileVersion

Returns the waveform file version of the waveform stored in the NI-RFSG waveform database. This function uses the **waveformName** as the key to retrieve the waveform property.

#### Syntax

int32 __stdcall niRFSGPlayback_RetrieveWaveformFileVersion(ViSession rfsgSession, ViConstString waveformName, ViInt32 waveformFileVersionBufferSize, ViChar waveformFileVersion)

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| rfsgSession | [in] | ViSession | Identifies the instrument session. rfsgSession is obtained from either the niRFSG_init function or the niRFSG_InitWithOptions function. |
| waveformName | [in] | ViConstString | Specifies the name of the waveform for which you want to retrieve the waveform file version. |
| waveformFileVersionBufferSize | [in] | ViInt32 | Specifies the buffer size of the waveformFileVersion parameter. |
| waveformFileVersion | [out] | ViChar | Returns the waveform file version of the waveform stored stored in the NI-RFSG waveform database for the waveform you specified in the waveformName parameter. This value is expressed in samples. |

#### Returns

Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred. To obtain a text description of the status code and additional information about the error condition, call the [niRFSGPlayback_GetError](group____root__ni_r_f_s_g_playback__functions_1ga5985403bcf5416e344ce264b3a73fc4a.html) function. The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

Advanced

<!--NI_TOPIC bundle=rfsgplaybacklibrary-c-api-ref path=group____root__ni_r_f_s_g_playback__functions__advanced_1gaa148cf67b78b220029171f40cea46b4d.html language=enus -->
## TOPIC 00039: niRFSGPlayback_RetrieveWaveformSignalBandwidth

- bundle_id: `rfsgplaybacklibrary-c-api-ref`
- source_path: `group____root__ni_r_f_s_g_playback__functions__advanced_1gaa148cf67b78b220029171f40cea46b4d.html`
- source_url: https://docs-be.ni.com/bundle/rfsgplaybacklibrary-c-api-ref/raw/resource/enus/group____root__ni_r_f_s_g_playback__functions__advanced_1gaa148cf67b78b220029171f40cea46b4d.html
- document_id: `rfsgplaybacklibrary-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the signal bandwidth stored in the NI-RFSG waveform database. This function uses the waveformName as the key to retrieve the waveform property. Syntaxint32 __stdcall niRFSGPlayback_RetrieveWaveformSignalBandwidth(ViSession rfsgSession, ViConstString waveformName, ViReal64 signalBandwidth)Par

### niRFSGPlayback_RetrieveWaveformSignalBandwidth

Returns the signal bandwidth stored in the NI-RFSG waveform database. This function uses the **waveformName** as the key to retrieve the waveform property.

#### Syntax

int32 __stdcall niRFSGPlayback_RetrieveWaveformSignalBandwidth(ViSession rfsgSession, ViConstString waveformName, ViReal64 signalBandwidth)

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| rfsgSession | [in] | ViSession | Identifies the instrument session. rfsgSession is obtained from either the niRFSG_init function or the niRFSG_InitWithOptions function. |
| waveformName | [in] | ViConstString | Specifies the name of the waveform for which you want to retrieve the waveform signal bandwidth. |
| signalBandwidth | [out] | ViReal64 | Returns the signal bandwidth, stored in the NI-RFSG waveform database, for the waveform you specified in the waveformName parameter. |

#### Returns

Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred. To obtain a text description of the status code and additional information about the error condition, call the [niRFSGPlayback_GetError](group____root__ni_r_f_s_g_playback__functions_1ga5985403bcf5416e344ce264b3a73fc4a.html) function. The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

Advanced

<!--NI_TOPIC bundle=rfsgplaybacklibrary-c-api-ref path=group____root__ni_r_f_s_g_playback__functions__advanced_1gab8fd0f86cc2a4dff37d1e3fff55c4445.html language=enus -->
## TOPIC 00040: niRFSGPlayback_StoreWaveformSampleRate

- bundle_id: `rfsgplaybacklibrary-c-api-ref`
- source_path: `group____root__ni_r_f_s_g_playback__functions__advanced_1gab8fd0f86cc2a4dff37d1e3fff55c4445.html`
- source_url: https://docs-be.ni.com/bundle/rfsgplaybacklibrary-c-api-ref/raw/resource/enus/group____root__ni_r_f_s_g_playback__functions__advanced_1gab8fd0f86cc2a4dff37d1e3fff55c4445.html
- document_id: `rfsgplaybacklibrary-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Stores the sample rate, which you specify in the sampleRate parameter, in the NI-RFSG waveform database. Syntaxint32 __stdcall niRFSGPlayback_StoreWaveformSampleRate(ViSession rfsgSession, ViConstString waveformName, ViReal64 sampleRate)ParametersNameDirectionTypeDescriptionrfsgSession[in]ViSessionI

### niRFSGPlayback_StoreWaveformSampleRate

Stores the sample rate, which you specify in the **sampleRate** parameter, in the NI-RFSG waveform database.

#### Syntax

int32 __stdcall niRFSGPlayback_StoreWaveformSampleRate(ViSession rfsgSession, ViConstString waveformName, ViReal64 sampleRate)

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| rfsgSession | [in] | ViSession | Identifies the instrument session. rfsgSession is obtained from either the niRFSG_init function or the niRFSG_InitWithOptions function. |
| waveformName | [in] | ViConstString | Specifies the waveform name for which you want to store the sample rate. |
| sampleRate | [in] | ViReal64 | Specifies the sampling rate to store in the NI-RFSG waveform database. This value is expressed in samples per second (S/s). |

#### Returns

Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred. To obtain a text description of the status code and additional information about the error condition, call the [niRFSGPlayback_GetError](group____root__ni_r_f_s_g_playback__functions_1ga5985403bcf5416e344ce264b3a73fc4a.html) function. The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

Advanced

<!--NI_TOPIC bundle=rfsgplaybacklibrary-c-api-ref path=group____root__ni_r_f_s_g_playback__functions__advanced_1gab94b64afaff02c3d775c723bd99402c8.html language=enus -->
## TOPIC 00041: niRFSGPlayback_RetrieveWaveformRFBlankingEnabled

- bundle_id: `rfsgplaybacklibrary-c-api-ref`
- source_path: `group____root__ni_r_f_s_g_playback__functions__advanced_1gab94b64afaff02c3d775c723bd99402c8.html`
- source_url: https://docs-be.ni.com/bundle/rfsgplaybacklibrary-c-api-ref/raw/resource/enus/group____root__ni_r_f_s_g_playback__functions__advanced_1gab94b64afaff02c3d775c723bd99402c8.html
- document_id: `rfsgplaybacklibrary-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the RF blanking enabled value stored in the NI-RFSG waveform database. This function uses the waveformName as the key to retrieve the waveform property. Syntaxint32 __stdcall niRFSGPlayback_RetrieveWaveformRFBlankingEnabled(ViSession rfsgSession, ViConstString waveformName, ViInt32 rfBlankin

### niRFSGPlayback_RetrieveWaveformRFBlankingEnabled

Returns the RF blanking enabled value stored in the NI-RFSG waveform database. This function uses the **waveformName** as the key to retrieve the waveform property.

#### Syntax

int32 __stdcall niRFSGPlayback_RetrieveWaveformRFBlankingEnabled(ViSession rfsgSession, ViConstString waveformName, ViInt32 rfBlankingEnabled)

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| rfsgSession | [in] | ViSession | Identifies the instrument session. rfsgSession is obtained from either the niRFSG_init function or the niRFSG_InitWithOptions function. |
| waveformName | [in] | ViConstString | Specifies the waveform name for which you want to retrieve the RF blanking enabled value. |
| rfBlankingEnabled | [out] | ViInt32 | Returns the RF blanking enabled value, stored in the NI-RFSG waveform database for the waveform number you specified in the waveformName parameter. |

#### Returns

Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred. To obtain a text description of the status code and additional information about the error condition, call the [niRFSGPlayback_GetError](group____root__ni_r_f_s_g_playback__functions_1ga5985403bcf5416e344ce264b3a73fc4a.html) function. The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

Advanced

<!--NI_TOPIC bundle=rfsgplaybacklibrary-c-api-ref path=group____root__ni_r_f_s_g_playback__functions__advanced_1gabea457afd8a153832d3f00893c159d46.html language=enus -->
## TOPIC 00042: niRFSGPlayback_StoreWaveformLOOffsetMode

- bundle_id: `rfsgplaybacklibrary-c-api-ref`
- source_path: `group____root__ni_r_f_s_g_playback__functions__advanced_1gabea457afd8a153832d3f00893c159d46.html`
- source_url: https://docs-be.ni.com/bundle/rfsgplaybacklibrary-c-api-ref/raw/resource/enus/group____root__ni_r_f_s_g_playback__functions__advanced_1gabea457afd8a153832d3f00893c159d46.html
- document_id: `rfsgplaybacklibrary-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Stores the LO offset mode value, which you specify in the LOOffsetMode parameter, in the NI-RFSG waveform database. Syntaxint32 __stdcall niRFSGPlayback_StoreWaveformLOOffsetMode(ViSession rfsgSession, ViConstString waveformName, ViInt32 loOffsetMode)ParametersNameDirectionTypeDescriptionrfsgSession

### niRFSGPlayback_StoreWaveformLOOffsetMode

Stores the LO offset mode value, which you specify in the **LOOffsetMode** parameter, in the NI-RFSG waveform database.

#### Syntax

int32 __stdcall niRFSGPlayback_StoreWaveformLOOffsetMode(ViSession rfsgSession, ViConstString waveformName, ViInt32 loOffsetMode)

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| rfsgSession | [in] | ViSession | Identifies the instrument session. rfsgSession is obtained from either the niRFSG_init function or the niRFSG_InitWithOptions function. |
| waveformName | [in] | ViConstString | Specifies the waveform name for which you want to store the LO offset mode value. |
| loOffsetMode | [in] | ViInt32 | Specifies the LO offset mode to store in the NI-RFSG waveform database. The following enums define the behavior of the niRFSGPlayback_SetScriptToGenerateSingleRFSG and niRFSGPlayback_SetScriptToGenerateMultipleRFSG functions on PXIe-5840/5841/5842 and PXIe-5830/5831/5832.NameValueNIRFSGPLAYBACK_VAL_LO_OFFSET_MODE_AUTO(0)Sets the signal bandwidth value to the NIRFSG_ATTR_SIGNAL_BANDWIDTH attribute, and resets the NIRFSG_ATTR_UPCONVERTER_FREQUENCY_OFFSET attribute.NIRFSGPLAYBACK_VAL_LO_OFFSET_MODE_NO_OFFSET(1)Resets the values of the NIRFSG_ATTR_SIGNAL_BANDWIDTH and NIRFSG_ATTR_UPCONVERTER_FREQUENCY_OFFSET attributes.NIRFSGPLAYBACK_VAL_LO_OFFSET_MODE_DISABLED(2)Does not set the NIRFSG_ATTR_SIGNAL_BANDWIDTH attribute or reset the NIRFSG_ATTR_UPCONVERTER_FREQUENCY_OFFSET attribute.Measurement results might get affected while performing measurements in the RFmx driver if the signal analyzer measurement frequency span is wide enough to capture signal generator LO. In these cases, it is recommended to configure the LOOffsetMode parameter to NIRFSGPLAYBACK_VAL_LO_OFFSET_MODE_NO_OFFSET. |
| Name | Value |  |  |
| NIRFSGPLAYBACK_VAL_LO_OFFSET_MODE_AUTO(0) | Sets the signal bandwidth value to the NIRFSG_ATTR_SIGNAL_BANDWIDTH attribute, and resets the NIRFSG_ATTR_UPCONVERTER_FREQUENCY_OFFSET attribute. |  |  |
| NIRFSGPLAYBACK_VAL_LO_OFFSET_MODE_NO_OFFSET(1) | Resets the values of the NIRFSG_ATTR_SIGNAL_BANDWIDTH and NIRFSG_ATTR_UPCONVERTER_FREQUENCY_OFFSET attributes. |  |  |
| NIRFSGPLAYBACK_VAL_LO_OFFSET_MODE_DISABLED(2) | Does not set the NIRFSG_ATTR_SIGNAL_BANDWIDTH attribute or reset the NIRFSG_ATTR_UPCONVERTER_FREQUENCY_OFFSET attribute. |  |  |

#### Returns

Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred. To obtain a text description of the status code and additional information about the error condition, call the [niRFSGPlayback_GetError](group____root__ni_r_f_s_g_playback__functions_1ga5985403bcf5416e344ce264b3a73fc4a.html) function. The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

Advanced

<!--NI_TOPIC bundle=rfsgplaybacklibrary-c-api-ref path=group____root__ni_r_f_s_g_playback__functions__advanced_1gacb08eb0aa0160df86f21d4fff70ecd6b.html language=enus -->
## TOPIC 00043: niRFSGPlayback_RetrieveWaveformBurstStopLocations

- bundle_id: `rfsgplaybacklibrary-c-api-ref`
- source_path: `group____root__ni_r_f_s_g_playback__functions__advanced_1gacb08eb0aa0160df86f21d4fff70ecd6b.html`
- source_url: https://docs-be.ni.com/bundle/rfsgplaybacklibrary-c-api-ref/raw/resource/enus/group____root__ni_r_f_s_g_playback__functions__advanced_1gacb08eb0aa0160df86f21d4fff70ecd6b.html
- document_id: `rfsgplaybacklibrary-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns burst stop locations stored in the NI-RFSG waveform database. This function uses the waveformName as the key to retrieve the waveform property. Syntaxint32 __stdcall niRFSGPlayback_RetrieveWaveformBurstStopLocations(ViSession rfsgSession, ViConstString waveformName, ViInt32 burstStopLocation

### niRFSGPlayback_RetrieveWaveformBurstStopLocations

Returns burst stop locations stored in the NI-RFSG waveform database. This function uses the **waveformName** as the key to retrieve the waveform property.

#### Syntax

int32 __stdcall niRFSGPlayback_RetrieveWaveformBurstStopLocations(ViSession rfsgSession, ViConstString waveformName, ViInt32 burstStopLocationsSize, ViInt32[] burstStopLocations, ViInt32 actualNumberOfLocations)

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| rfsgSession | [in] | ViSession | Identifies the instrument session. rfsgSession is obtained from either the niRFSG_init function or the niRFSG_InitWithOptions function. |
| waveformName | [in] | ViConstString | Specifies the waveform name for which you want to retrieve the burst stop locations. |
| burstStopLocationsSize | [in] | ViInt32 | Specifies the size of the burstStopLocations array. Set the burstStopLocationsSize parameter to 0 to get the size of the burstStopLocations array in the actualNumberOfLocations parameter. |
| burstStopLocations | [out] | ViInt32[] | Returns the array of the burst stop locations, stored in the NI-RFSG waveform database for the waveform you specified in the waveformName parameter. |
| actualNumberOfLocations | [out] | ViInt32 | Returns the actual size of the array, if you pass NULL to all output array parameters, and set the burstStopLocationsSize parameter to 0. |

#### Returns

Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred. To obtain a text description of the status code and additional information about the error condition, call the [niRFSGPlayback_GetError](group____root__ni_r_f_s_g_playback__functions_1ga5985403bcf5416e344ce264b3a73fc4a.html) function. The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

Advanced

<!--NI_TOPIC bundle=rfsgplaybacklibrary-c-api-ref path=group____root__ni_r_f_s_g_playback__functions__advanced_1gad17125971b099e2794f172fb80b46a48.html language=enus -->
## TOPIC 00044: niRFSGPlayback_RetrieveWaveformLOOffsetMode

- bundle_id: `rfsgplaybacklibrary-c-api-ref`
- source_path: `group____root__ni_r_f_s_g_playback__functions__advanced_1gad17125971b099e2794f172fb80b46a48.html`
- source_url: https://docs-be.ni.com/bundle/rfsgplaybacklibrary-c-api-ref/raw/resource/enus/group____root__ni_r_f_s_g_playback__functions__advanced_1gad17125971b099e2794f172fb80b46a48.html
- document_id: `rfsgplaybacklibrary-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the LO offset mode value stored in the NI-RFSG waveform database. This function uses the waveformName as the key to retrieve the waveform property. Syntaxint32 __stdcall niRFSGPlayback_RetrieveWaveformLOOffsetMode(ViSession rfsgSession, ViConstString waveformName, ViInt32 loOffsetMode)Parame

### niRFSGPlayback_RetrieveWaveformLOOffsetMode

Returns the LO offset mode value stored in the NI-RFSG waveform database. This function uses the **waveformName** as the key to retrieve the waveform property.

#### Syntax

int32 __stdcall niRFSGPlayback_RetrieveWaveformLOOffsetMode(ViSession rfsgSession, ViConstString waveformName, ViInt32 loOffsetMode)

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| rfsgSession | [in] | ViSession | Identifies the instrument session. rfsgSession is obtained from either the niRFSG_init function or the niRFSG_InitWithOptions function. |
| waveformName | [in] | ViConstString | Specifies the name of the waveform for which you want to retrieve the waveform LO offset mode value. |
| loOffsetMode | [out] | ViInt32 | Returns the LO offset mode value, stored in the NI-RFSG waveform database, for the waveform you specified in the waveformName parameter. |

#### Returns

Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred. To obtain a text description of the status code and additional information about the error condition, call the [niRFSGPlayback_GetError](group____root__ni_r_f_s_g_playback__functions_1ga5985403bcf5416e344ce264b3a73fc4a.html) function. The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

Advanced

<!--NI_TOPIC bundle=rfsgplaybacklibrary-c-api-ref path=group____root__ni_r_f_s_g_playback__functions__advanced_1gad56a44865ab2414c7188b427e6e38a47.html language=enus -->
## TOPIC 00045: niRFSGPlayback_StoreWaveformPAPR

- bundle_id: `rfsgplaybacklibrary-c-api-ref`
- source_path: `group____root__ni_r_f_s_g_playback__functions__advanced_1gad56a44865ab2414c7188b427e6e38a47.html`
- source_url: https://docs-be.ni.com/bundle/rfsgplaybacklibrary-c-api-ref/raw/resource/enus/group____root__ni_r_f_s_g_playback__functions__advanced_1gad56a44865ab2414c7188b427e6e38a47.html
- document_id: `rfsgplaybacklibrary-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Stores the peak to average power ratio (PAPR), which you specify in the PAPR parameter, in the NI-RFSG waveform database. Syntaxint32 __stdcall niRFSGPlayback_StoreWaveformPAPR(ViSession rfsgSession, ViConstString waveformName, ViReal64 papr)ParametersNameDirectionTypeDescriptionrfsgSession[in]ViSes

### niRFSGPlayback_StoreWaveformPAPR

Stores the peak to average power ratio (PAPR), which you specify in the **PAPR** parameter, in the NI-RFSG waveform database.

#### Syntax

int32 __stdcall niRFSGPlayback_StoreWaveformPAPR(ViSession rfsgSession, ViConstString waveformName, ViReal64 papr)

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| rfsgSession | [in] | ViSession | Identifies the instrument session. rfsgSession is obtained from either the niRFSG_init function or the niRFSG_InitWithOptions function. |
| waveformName | [in] | ViConstString | Specifies the waveform name for which you want to store the LO offset mode value. |
| papr | [in] | ViReal64 | Specifies the PAPR to store in the NI-RFSG database. This value is expressed in dB. |

#### Returns

Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred. To obtain a text description of the status code and additional information about the error condition, call the [niRFSGPlayback_GetError](group____root__ni_r_f_s_g_playback__functions_1ga5985403bcf5416e344ce264b3a73fc4a.html) function. The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

Advanced

<!--NI_TOPIC bundle=rfsgplaybacklibrary-c-api-ref path=group____root__ni_r_f_s_g_playback__functions__advanced_1gad674ff28164a20c8676c1098ab1cc1d0.html language=enus -->
## TOPIC 00046: niRFSGPlayback_StoreWaveformRFBlankingEnabled

- bundle_id: `rfsgplaybacklibrary-c-api-ref`
- source_path: `group____root__ni_r_f_s_g_playback__functions__advanced_1gad674ff28164a20c8676c1098ab1cc1d0.html`
- source_url: https://docs-be.ni.com/bundle/rfsgplaybacklibrary-c-api-ref/raw/resource/enus/group____root__ni_r_f_s_g_playback__functions__advanced_1gad674ff28164a20c8676c1098ab1cc1d0.html
- document_id: `rfsgplaybacklibrary-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Stores the RF blanking enabled value, which you specify in the rfBlankingEnabled parameter, in the NI-RFSG waveform database. Syntaxint32 __stdcall niRFSGPlayback_StoreWaveformRFBlankingEnabled(ViSession rfsgSession, ViConstString waveformName, ViInt32 rfBlankingEnabled)ParametersNameDirectionTypeDe

### niRFSGPlayback_StoreWaveformRFBlankingEnabled

Stores the RF blanking enabled value, which you specify in the **rfBlankingEnabled** parameter, in the NI-RFSG waveform database.

#### Syntax

int32 __stdcall niRFSGPlayback_StoreWaveformRFBlankingEnabled(ViSession rfsgSession, ViConstString waveformName, ViInt32 rfBlankingEnabled)

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| rfsgSession | [in] | ViSession | Identifies the instrument session. rfsgSession is obtained from either the niRFSG_init function or the niRFSG_InitWithOptions function. |
| waveformName | [in] | ViConstString | Specifies the waveform name for which you want to store the RF blanking enabled value. |
| rfBlankingEnabled | [in] | ViInt32 | Specifies the RF blanking enabled value to store in the NI-RFSG waveform database. |

#### Returns

Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred. To obtain a text description of the status code and additional information about the error condition, call the [niRFSGPlayback_GetError](group____root__ni_r_f_s_g_playback__functions_1ga5985403bcf5416e344ce264b3a73fc4a.html) function. The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

Advanced

<!--NI_TOPIC bundle=rfsgplaybacklibrary-c-api-ref path=group____root__ni_r_f_s_g_playback__functions__advanced_1gae51b9b2b8a6e27a02bb3738721262848.html language=enus -->
## TOPIC 00047: niRFSGPlayback_RetrieveWaveformSize

- bundle_id: `rfsgplaybacklibrary-c-api-ref`
- source_path: `group____root__ni_r_f_s_g_playback__functions__advanced_1gae51b9b2b8a6e27a02bb3738721262848.html`
- source_url: https://docs-be.ni.com/bundle/rfsgplaybacklibrary-c-api-ref/raw/resource/enus/group____root__ni_r_f_s_g_playback__functions__advanced_1gae51b9b2b8a6e27a02bb3738721262848.html
- document_id: `rfsgplaybacklibrary-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the size of the waveform stored in the NI-RFSG waveform database. This function uses the waveformName as the key to retrieve the waveform property. Syntaxint32 __stdcall niRFSGPlayback_RetrieveWaveformSize(ViSession rfsgSession, ViConstString waveformName, ViInt32 waveformSize)ParametersName

### niRFSGPlayback_RetrieveWaveformSize

Returns the size of the waveform stored in the NI-RFSG waveform database. This function uses the **waveformName** as the key to retrieve the waveform property.

#### Syntax

int32 __stdcall niRFSGPlayback_RetrieveWaveformSize(ViSession rfsgSession, ViConstString waveformName, ViInt32 waveformSize)

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| rfsgSession | [in] | ViSession | Identifies the instrument session. rfsgSession is obtained from either the niRFSG_init function or the niRFSG_InitWithOptions function. |
| waveformName | [in] | ViConstString | Specifies the name of the waveform for which you want to retrieve the waveform size. |
| waveformSize | [out] | ViInt32 | Returns the size of the waveform stored stored in the NI-RFSG waveform database for the waveform you specified in the waveformName parameter. This value is expressed in samples. |

#### Returns

Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred. To obtain a text description of the status code and additional information about the error condition, call the [niRFSGPlayback_GetError](group____root__ni_r_f_s_g_playback__functions_1ga5985403bcf5416e344ce264b3a73fc4a.html) function. The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

Advanced

<!--NI_TOPIC bundle=rfsgplaybacklibrary-c-api-ref path=group____root__ni_r_f_s_g_playback__functions__advanced_1gaf545713bc6762d66f6269e03e5c04cd9.html language=enus -->
## TOPIC 00048: niRFSGPlayback_StoreAutomaticSGSASharedLO

- bundle_id: `rfsgplaybacklibrary-c-api-ref`
- source_path: `group____root__ni_r_f_s_g_playback__functions__advanced_1gaf545713bc6762d66f6269e03e5c04cd9.html`
- source_url: https://docs-be.ni.com/bundle/rfsgplaybacklibrary-c-api-ref/raw/resource/enus/group____root__ni_r_f_s_g_playback__functions__advanced_1gaf545713bc6762d66f6269e03e5c04cd9.html
- document_id: `rfsgplaybacklibrary-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Stores whether the signal generator's LO signal can be shared on request by the RFmx driver. It is recommended to use Automatic sharing of local oscillator (LO) in test setups that use a vector signal transceiver (VST) with the NI-RFSG to generate a signal at the DUT's input and the RFmx driver to m

### niRFSGPlayback_StoreAutomaticSGSASharedLO

Stores whether the signal generator's LO signal can be shared on request by the RFmx driver. It is recommended to use Automatic sharing of local oscillator (LO) in test setups that use a vector signal transceiver (VST) with the NI-RFSG to generate a signal at the DUT's input and the RFmx driver to measure the signal at the DUT's output.

#### Syntax

int32 __stdcall niRFSGPlayback_StoreAutomaticSGSASharedLO(ViSession rfsgSession, ViConstString channelName, ViInt32 automaticSGSASharedLO)

#### Remarks

When using instruments that do not have LO with excellent phase noise, to minimize the contribution of the instrument's phase noise affecting your measurement, it is recommended to share the LO between the signal generator (SG) and signal analyzer (SA).

To enable sharing signal generator's LO with signal analyzer automatically, setup the device specific physical connections as mentioned in the following table and follow the steps in the mentioned order.

| Name | Value |
| --- | --- |
| PXIe-5840/5841/5842 | SG LO is shared with SA via an external path. Hence you must connect RF Out LO Out to RF In LO In using a cable. |
| PXIe-5830/5831/5832 | SG LO is shared with SA via an internal path. Hence the external cable connection is not required. |

1. Enable Automatic SGSA Shared LO on NI-RFSG Playback Library
2. Set the RFMXINSTR_ATTR_LO_SOURCE attribute to **RFMXINSTR_VAL_LO_SOURCE_AUTOMATIC_SG_SA_SHARED** in RFmx
3. Configure other required settings on NI-RFSG and RFmx, including selecting waveforms
4. Initiate NI-RFSG
5. Initiate RFmx

Measurement results might get affected while performing measurements in the RFmx driver if the signal analyzer measurement frequency span is wide enough to capture signal generator LO. In these cases, it is recommended to configure the **LOOffsetMode** parameter to **NIRFSGPLAYBACK_VAL_LO_OFFSET_MODE_NO_OFFSET**.

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| rfsgSession | [in] | ViSession | Identifies the instrument session. rfsgSession is obtained from either the niRFSG_init function or the niRFSG_InitWithOptions function. |
| channelName | [in] | ViConstString | This parameter is reserved for future use. |
| automaticSGSASharedLO | [in] | ViInt32 | specifies the access control of SG LO.NameValueNIRFSGPLAYBACK_VAL_AUTOMATIC_SG_SA_SHARED_LO_DISABLED (0)Disables automatic sharing the SG LO with SA.NIRFSGPLAYBACK_VAL_AUTOMATIC_SG_SA_SHARED_LO_ENABLED (1)Enables automatic sharing the SG LO with SA. |
| Name | Value |  |  |
| NIRFSGPLAYBACK_VAL_AUTOMATIC_SG_SA_SHARED_LO_DISABLED (0) | Disables automatic sharing the SG LO with SA. |  |  |
| NIRFSGPLAYBACK_VAL_AUTOMATIC_SG_SA_SHARED_LO_ENABLED (1) | Enables automatic sharing the SG LO with SA. |  |  |

#### Returns

Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred. To obtain a text description of the status code and additional information about the error condition, call the [niRFSGPlayback_GetError](group____root__ni_r_f_s_g_playback__functions_1ga5985403bcf5416e344ce264b3a73fc4a.html) function. The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

Advanced

<!--NI_TOPIC bundle=rfsgplaybacklibrary-c-api-ref path=group____root__ni_r_f_s_g_playback__functions__advanced_1gaf90d57ad612f9b10bfa1a27251433598.html language=enus -->
## TOPIC 00049: niRFSGPlayback_StoreWaveformSize

- bundle_id: `rfsgplaybacklibrary-c-api-ref`
- source_path: `group____root__ni_r_f_s_g_playback__functions__advanced_1gaf90d57ad612f9b10bfa1a27251433598.html`
- source_url: https://docs-be.ni.com/bundle/rfsgplaybacklibrary-c-api-ref/raw/resource/enus/group____root__ni_r_f_s_g_playback__functions__advanced_1gaf90d57ad612f9b10bfa1a27251433598.html
- document_id: `rfsgplaybacklibrary-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Stores the size of the waveform, which you specify in the waveformSize parameter, in the NI-RFSG waveform database. Syntaxint32 __stdcall niRFSGPlayback_StoreWaveformSize(ViSession rfsgSession, ViConstString waveformName, ViInt32 waveformSize)ParametersNameDirectionTypeDescriptionrfsgSession[in]ViSe

### niRFSGPlayback_StoreWaveformSize

Stores the size of the waveform, which you specify in the **waveformSize** parameter, in the NI-RFSG waveform database.

#### Syntax

int32 __stdcall niRFSGPlayback_StoreWaveformSize(ViSession rfsgSession, ViConstString waveformName, ViInt32 waveformSize)

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| rfsgSession | [in] | ViSession | Identifies the instrument session. rfsgSession is obtained from either the niRFSG_init function or the niRFSG_InitWithOptions function. |
| waveformName | [in] | ViConstString | Specifies the name of the waveform for which you want to store the waveform size. |
| waveformSize | [in] | ViInt32 | Specifies the size of the waveform to store in the NI-RFSG waveform database. This value is expressed in samples. |

#### Returns

Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred. To obtain a text description of the status code and additional information about the error condition, call the [niRFSGPlayback_GetError](group____root__ni_r_f_s_g_playback__functions_1ga5985403bcf5416e344ce264b3a73fc4a.html) function. The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

Advanced

<!--NI_TOPIC bundle=rfsgplaybacklibrary-c-api-ref path=group____root__ni_r_f_s_g_playback__functions__advanced__obsolete.html language=enus -->
## TOPIC 00050: Obsolete

- bundle_id: `rfsgplaybacklibrary-c-api-ref`
- source_path: `group____root__ni_r_f_s_g_playback__functions__advanced__obsolete.html`
- source_url: https://docs-be.ni.com/bundle/rfsgplaybacklibrary-c-api-ref/raw/resource/enus/group____root__ni_r_f_s_g_playback__functions__advanced__obsolete.html
- document_id: `rfsgplaybacklibrary-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: GroupsNoneGroup membersNameDescriptionniRFSGPlayback_RetrieveWaveformPeakPowerAdjustmentReturns the peak power adjustment value stored in the NI-RFSG waveform database. This function uses the waveformName as the key to retrieve the waveform property. niRFSGPlayback_RetrieveWaveformRFBlankingMarkerLo

### Obsolete

#### Groups

None

#### Group members

| Name | Description |
| --- | --- |
| niRFSGPlayback_RetrieveWaveformPeakPowerAdjustment | Returns the peak power adjustment value stored in the NI-RFSG waveform database. This function uses the waveformName as the key to retrieve the waveform property. |
| niRFSGPlayback_RetrieveWaveformRFBlankingMarkerLocations | Returns the RF blanking marker positions stored in the NI-RFSG waveform database. This function uses the waveformName as the key to retrieve the waveform property. |
| niRFSGPlayback_RetrieveWaveformRFBlankingMarkerSource | Returns the RF blanking marker source stored in the NI-RFSG waveform database. This function uses the waveformName as the key to retrieve the waveform property. |
| niRFSGPlayback_StoreWaveformPeakPowerAdjustment | Stores the peak power adjustment, which you specify in the peakPowerAdjustment parameter, in the NI-RFSG waveform database. |
| niRFSGPlayback_StoreWaveformRFBlankingMarkerLocations | Stores the RF blanking marker positions, which you specify in the markerLocations parameter, in the NI-RFSG waveform database. |

#### Attachments

None

Parent topic:

Advanced

<!--NI_TOPIC bundle=rfsgplaybacklibrary-c-api-ref path=group____root__ni_r_f_s_g_playback__functions__advanced__obsolete_1ga6be185b8df0dcb98e70c71e560edd7f9.html language=enus -->
## TOPIC 00051: niRFSGPlayback_RetrieveWaveformPeakPowerAdjustment

- bundle_id: `rfsgplaybacklibrary-c-api-ref`
- source_path: `group____root__ni_r_f_s_g_playback__functions__advanced__obsolete_1ga6be185b8df0dcb98e70c71e560edd7f9.html`
- source_url: https://docs-be.ni.com/bundle/rfsgplaybacklibrary-c-api-ref/raw/resource/enus/group____root__ni_r_f_s_g_playback__functions__advanced__obsolete_1ga6be185b8df0dcb98e70c71e560edd7f9.html
- document_id: `rfsgplaybacklibrary-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the peak power adjustment value stored in the NI-RFSG waveform database. This function uses the waveformName as the key to retrieve the waveform property. Syntaxint32 __stdcall niRFSGPlayback_RetrieveWaveformPeakPowerAdjustment(ViSession rfsgSession, ViConstString waveformName, ViReal64 peak

### niRFSGPlayback_RetrieveWaveformPeakPowerAdjustment

Returns the peak power adjustment value stored in the NI-RFSG waveform database. This function uses the **waveformName** as the key to retrieve the waveform property.

#### Syntax

int32 __stdcall niRFSGPlayback_RetrieveWaveformPeakPowerAdjustment(ViSession rfsgSession, ViConstString waveformName, ViReal64 peakPowerAdjustment)

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| rfsgSession | [in] | ViSession | Identifies the instrument session. rfsgSession is obtained from either the niRFSG_init function or the niRFSG_InitWithOptions function. |
| waveformName | [in] | ViConstString | Specifies the waveform name for which you want to retrieve the peak power adjustment value. |
| peakPowerAdjustment | [out] | ViReal64 | Returns the NIRFSG_ATTR_PEAK_POWER_ADJUSTMENT value, stored in the NI-RFSG waveform database, for the waveform you specified in the waveformName parameter. |

#### Returns

Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred. To obtain a text description of the status code and additional information about the error condition, call the [niRFSGPlayback_GetError](group____root__ni_r_f_s_g_playback__functions_1ga5985403bcf5416e344ce264b3a73fc4a.html) function. The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

Obsolete

<!--NI_TOPIC bundle=rfsgplaybacklibrary-c-api-ref path=group____root__ni_r_f_s_g_playback__functions__advanced__obsolete_1ga78b420731683ed0843a507eba59e5ba5.html language=enus -->
## TOPIC 00052: niRFSGPlayback_RetrieveWaveformRFBlankingMarkerLocations

- bundle_id: `rfsgplaybacklibrary-c-api-ref`
- source_path: `group____root__ni_r_f_s_g_playback__functions__advanced__obsolete_1ga78b420731683ed0843a507eba59e5ba5.html`
- source_url: https://docs-be.ni.com/bundle/rfsgplaybacklibrary-c-api-ref/raw/resource/enus/group____root__ni_r_f_s_g_playback__functions__advanced__obsolete_1ga78b420731683ed0843a507eba59e5ba5.html
- document_id: `rfsgplaybacklibrary-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the RF blanking marker positions stored in the NI-RFSG waveform database. This function uses the waveformName as the key to retrieve the waveform property. Syntaxint32 __stdcall niRFSGPlayback_RetrieveWaveformRFBlankingMarkerLocations(ViSession rfsgSession, ViConstString waveformName, ViInt3

### niRFSGPlayback_RetrieveWaveformRFBlankingMarkerLocations

Returns the RF blanking marker positions stored in the NI-RFSG waveform database. This function uses the **waveformName** as the key to retrieve the waveform property.

#### Syntax

int32 __stdcall niRFSGPlayback_RetrieveWaveformRFBlankingMarkerLocations(ViSession rfsgSession, ViConstString waveformName, ViInt32 markerLocationsSize, ViInt32[] markerLocations, ViInt32 actualNumberOfLocations)

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| rfsgSession | [in] | ViSession | Identifies the instrument session. rfsgSession is obtained from either the niRFSG_init function or the niRFSG_InitWithOptions function. |
| waveformName | [in] | ViConstString | Specifies the waveform name for which you want to retrieve the RF blanking marker locations. |
| markerLocationsSize | [in] | ViInt32 | Specifies the size of the markerLocations array. Set the markerLocationsSize parameter to 0 to get the size of the markerLocations array in the actualNumberOfLocations parameter. |
| markerLocations | [out] | ViInt32[] | Returns the array of RF blanking marker positions, stored in the NI-RFSG waveform database for the waveform you specified in the waveformName parameter. |
| actualNumberOfLocations | [out] | ViInt32 | Returns the actual size of the array, if you pass NULL to all output array parameters, and set the markerLocationsSize parameter to 0. |

#### Returns

Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred. To obtain a text description of the status code and additional information about the error condition, call the [niRFSGPlayback_GetError](group____root__ni_r_f_s_g_playback__functions_1ga5985403bcf5416e344ce264b3a73fc4a.html) function. The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

Obsolete

<!--NI_TOPIC bundle=rfsgplaybacklibrary-c-api-ref path=group____root__ni_r_f_s_g_playback__functions__advanced__obsolete_1gab27624f2ce941257d19e2acfe867f79f.html language=enus -->
## TOPIC 00053: niRFSGPlayback_StoreWaveformRFBlankingMarkerLocations

- bundle_id: `rfsgplaybacklibrary-c-api-ref`
- source_path: `group____root__ni_r_f_s_g_playback__functions__advanced__obsolete_1gab27624f2ce941257d19e2acfe867f79f.html`
- source_url: https://docs-be.ni.com/bundle/rfsgplaybacklibrary-c-api-ref/raw/resource/enus/group____root__ni_r_f_s_g_playback__functions__advanced__obsolete_1gab27624f2ce941257d19e2acfe867f79f.html
- document_id: `rfsgplaybacklibrary-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Stores the RF blanking marker positions, which you specify in the markerLocations parameter, in the NI-RFSG waveform database. Syntaxint32 __stdcall niRFSGPlayback_StoreWaveformRFBlankingMarkerLocations(ViSession rfsgSession, ViConstString waveformName, ViInt32[] markerLocations, ViInt32 numberOfLoc

### niRFSGPlayback_StoreWaveformRFBlankingMarkerLocations

Stores the RF blanking marker positions, which you specify in the **markerLocations** parameter, in the NI-RFSG waveform database.

#### Syntax

int32 __stdcall niRFSGPlayback_StoreWaveformRFBlankingMarkerLocations(ViSession rfsgSession, ViConstString waveformName, ViInt32[] markerLocations, ViInt32 numberOfLocations)

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| rfsgSession | [in] | ViSession | Identifies the instrument session. rfsgSession is obtained from either the niRFSG_init function or the niRFSG_InitWithOptions function. |
| waveformName | [in] | ViConstString | Specifies the waveform name for which you want to store the RF blanking marker locations. |
| markerLocations | [out] | ViInt32[] | Specifies the RF blanking marker positions to store. It is an array of sample positions, within the waveform, of the marker events that you can use to toggle the RF blanking state. |
| numberOfLocations | [in] | ViInt32 | Specifies the number of marker locations. |

#### Returns

Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred. To obtain a text description of the status code and additional information about the error condition, call the [niRFSGPlayback_GetError](group____root__ni_r_f_s_g_playback__functions_1ga5985403bcf5416e344ce264b3a73fc4a.html) function. The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

Obsolete

<!--NI_TOPIC bundle=rfsgplaybacklibrary-c-api-ref path=group____root__ni_r_f_s_g_playback__functions__advanced__obsolete_1gaf8ffd58e8563c7cabdf52c179b08aae8.html language=enus -->
## TOPIC 00054: niRFSGPlayback_StoreWaveformPeakPowerAdjustment

- bundle_id: `rfsgplaybacklibrary-c-api-ref`
- source_path: `group____root__ni_r_f_s_g_playback__functions__advanced__obsolete_1gaf8ffd58e8563c7cabdf52c179b08aae8.html`
- source_url: https://docs-be.ni.com/bundle/rfsgplaybacklibrary-c-api-ref/raw/resource/enus/group____root__ni_r_f_s_g_playback__functions__advanced__obsolete_1gaf8ffd58e8563c7cabdf52c179b08aae8.html
- document_id: `rfsgplaybacklibrary-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Stores the peak power adjustment, which you specify in the peakPowerAdjustment parameter, in the NI-RFSG waveform database. Syntaxint32 __stdcall niRFSGPlayback_StoreWaveformPeakPowerAdjustment(ViSession rfsgSession, ViConstString waveformName, ViReal64 peakPowerAdjustment)ParametersNameDirectionTyp

### niRFSGPlayback_StoreWaveformPeakPowerAdjustment

Stores the peak power adjustment, which you specify in the **peakPowerAdjustment** parameter, in the NI-RFSG waveform database.

#### Syntax

int32 __stdcall niRFSGPlayback_StoreWaveformPeakPowerAdjustment(ViSession rfsgSession, ViConstString waveformName, ViReal64 peakPowerAdjustment)

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| rfsgSession | [in] | ViSession | Identifies the instrument session. rfsgSession is obtained from either the niRFSG_init function or the niRFSG_InitWithOptions function. |
| waveformName | [in] | ViConstString | Specifies the waveform name for which you want to store the peak power adjustment. |
| peakPowerAdjustment | [in] | ViReal64 | Specifies the peak power adjustment to store in the NI-RFSG waveform database. |

#### Returns

Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred. To obtain a text description of the status code and additional information about the error condition, call the [niRFSGPlayback_GetError](group____root__ni_r_f_s_g_playback__functions_1ga5985403bcf5416e344ce264b3a73fc4a.html) function. The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

Obsolete

<!--NI_TOPIC bundle=rfsgplaybacklibrary-c-api-ref path=group____root__ni_r_f_s_g_playback__functions__advanced__obsolete_1gaff3294d3bc270147f5852b744672e55f.html language=enus -->
## TOPIC 00055: niRFSGPlayback_RetrieveWaveformRFBlankingMarkerSource

- bundle_id: `rfsgplaybacklibrary-c-api-ref`
- source_path: `group____root__ni_r_f_s_g_playback__functions__advanced__obsolete_1gaff3294d3bc270147f5852b744672e55f.html`
- source_url: https://docs-be.ni.com/bundle/rfsgplaybacklibrary-c-api-ref/raw/resource/enus/group____root__ni_r_f_s_g_playback__functions__advanced__obsolete_1gaff3294d3bc270147f5852b744672e55f.html
- document_id: `rfsgplaybacklibrary-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the RF blanking marker source stored in the NI-RFSG waveform database. This function uses the waveformName as the key to retrieve the waveform property. Syntaxint32 __stdcall niRFSGPlayback_RetrieveWaveformRFBlankingMarkerSource(ViSession rfsgSession, ViConstString waveformName, ViInt32 mark

### niRFSGPlayback_RetrieveWaveformRFBlankingMarkerSource

Returns the RF blanking marker source stored in the NI-RFSG waveform database. This function uses the **waveformName** as the key to retrieve the waveform property.

#### Syntax

int32 __stdcall niRFSGPlayback_RetrieveWaveformRFBlankingMarkerSource(ViSession rfsgSession, ViConstString waveformName, ViInt32 markerSourceSize, ViChar[] markerSource)

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| rfsgSession | [in] | ViSession | Identifies the instrument session. rfsgSession is obtained from either the niRFSG_init function or the niRFSG_InitWithOptions function. |
| waveformName | [in] | ViConstString | Specifies the waveform name for which you want to retrieve the RF blanking marker locations. |
| markerSourceSize | [in] | ViInt32 | Specifies the size of the markerSource array. |
| markerSource | [out] | ViChar[] | Returns the size of the RF blanking marker source, stored in the NI-RFSG waveform database, for the waveform you specified in the waveformName parameter. |

#### Returns

Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred. To obtain a text description of the status code and additional information about the error condition, call the [niRFSGPlayback_GetError](group____root__ni_r_f_s_g_playback__functions_1ga5985403bcf5416e344ce264b3a73fc4a.html) function. The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

Obsolete

<!--NI_TOPIC bundle=rfsgplaybacklibrary-c-api-ref path=group____root__ni_r_f_s_g_playback__functions__utility.html language=enus -->
## TOPIC 00056: Utility

- bundle_id: `rfsgplaybacklibrary-c-api-ref`
- source_path: `group____root__ni_r_f_s_g_playback__functions__utility.html`
- source_url: https://docs-be.ni.com/bundle/rfsgplaybacklibrary-c-api-ref/raw/resource/enus/group____root__ni_r_f_s_g_playback__functions__utility.html
- document_id: `rfsgplaybacklibrary-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: GroupsObsoleteGroup membersNameDescriptionniRFSGPlayback_ReadBurstStartLocationsFromFileReturns the burst start locations stored in the file. This function uses the waveformIndex parameter as the key to retrieve the waveform property. niRFSGPlayback_ReadBurstStopLocationsFromFileReturns the RF blank

### Utility

#### Groups

- Obsolete

#### Group members

| Name | Description |
| --- | --- |
| niRFSGPlayback_ReadBurstStartLocationsFromFile | Returns the burst start locations stored in the file. This function uses the waveformIndex parameter as the key to retrieve the waveform property. |
| niRFSGPlayback_ReadBurstStopLocationsFromFile | Returns the RF blanking marker positions stored in the NI-RFSG database. This function uses the waveformName as the key to retrieve the waveform property. |
| niRFSGPlayback_ReadPAPRFromFile | Returns the peak to average power ratio (PAPR) stored in the file. This function uses the waveformIndex parameter as the key to retrieve the waveform property. |
| niRFSGPlayback_ReadRFBlankingEnabledFromFile | Returns the RF blanking enabled value stored in the file. This function uses the waveformIndex as the key to retrieve the waveform property. |
| niRFSGPlayback_ReadRFBlankingMarkerSourceFromFile | Returns the RF blanking marker source stored in the file. This function uses the waveformIndex as the key to retrieve the waveform property. |
| niRFSGPlayback_ReadRuntimeScalingFromFile | Returns the runtime scaling value stored in the file. This function uses the waveformIndex parameter as the key to retrieve the waveform property. |
| niRFSGPlayback_ReadSampleRateFromFile | Returns the sample rate stored in the file. This function uses the waveformIndex as the key to retrieve the waveform property. |
| niRFSGPlayback_ReadSignalBandwidthFromFile | Returns the signal bandwidth stored in the file. This function uses the waveformIndex parameter as the key to retrieve the waveform property. |
| niRFSGPlayback_ReadWaveformFileVersionFromFile | Returns the waveform file version of the waveform stored in the file. |
| niRFSGPlayback_ReadWaveformSizeFromFile | Returns the size of the waveform stored in the file. This function uses the waveformIndex parameter as the key to retrieve the waveform property. |

#### Attachments

None

Parent topic:

Functions

<!--NI_TOPIC bundle=rfsgplaybacklibrary-c-api-ref path=group____root__ni_r_f_s_g_playback__functions__utility_1ga007afca8612cfe6c2c9555c7f1838063.html language=enus -->
## TOPIC 00057: niRFSGPlayback_ReadRFBlankingEnabledFromFile

- bundle_id: `rfsgplaybacklibrary-c-api-ref`
- source_path: `group____root__ni_r_f_s_g_playback__functions__utility_1ga007afca8612cfe6c2c9555c7f1838063.html`
- source_url: https://docs-be.ni.com/bundle/rfsgplaybacklibrary-c-api-ref/raw/resource/enus/group____root__ni_r_f_s_g_playback__functions__utility_1ga007afca8612cfe6c2c9555c7f1838063.html
- document_id: `rfsgplaybacklibrary-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the RF blanking enabled value stored in the file. This function uses the waveformIndex as the key to retrieve the waveform property. Syntaxint32 __stdcall niRFSGPlayback_ReadRFBlankingEnabledFromFile(ViConstString filePath, ViInt32 waveformIndex, ViInt32 rfBlankingEnabled)ParametersNameDirec

### niRFSGPlayback_ReadRFBlankingEnabledFromFile

Returns the RF blanking enabled value stored in the file. This function uses the **waveformIndex** as the key to retrieve the waveform property.

#### Syntax

int32 __stdcall niRFSGPlayback_ReadRFBlankingEnabledFromFile(ViConstString filePath, ViInt32 waveformIndex, ViInt32 rfBlankingEnabled)

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| filePath | [in] | ViConstString | Specifies the absolute path to the TDMS file from which the playback library reads the waveforms. |
| waveformIndex | [in] | ViInt32 | Specifies the waveform number in the file for which you want to read the RF blanking enabled. |
| rfBlankingEnabled | [out] | ViInt32 | Returns the RF blanking marker enabled value, stored in the file for the waveform number which you specified in the waveformIndex parameter. |

#### Returns

Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred. To obtain a text description of the status code and additional information about the error condition, call the [niRFSGPlayback_GetError](group____root__ni_r_f_s_g_playback__functions_1ga5985403bcf5416e344ce264b3a73fc4a.html) function. The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

Utility

<!--NI_TOPIC bundle=rfsgplaybacklibrary-c-api-ref path=group____root__ni_r_f_s_g_playback__functions__utility_1ga0407d43830e2c4d63c59157d1ac6839c.html language=enus -->
## TOPIC 00058: niRFSGPlayback_ReadRuntimeScalingFromFile

- bundle_id: `rfsgplaybacklibrary-c-api-ref`
- source_path: `group____root__ni_r_f_s_g_playback__functions__utility_1ga0407d43830e2c4d63c59157d1ac6839c.html`
- source_url: https://docs-be.ni.com/bundle/rfsgplaybacklibrary-c-api-ref/raw/resource/enus/group____root__ni_r_f_s_g_playback__functions__utility_1ga0407d43830e2c4d63c59157d1ac6839c.html
- document_id: `rfsgplaybacklibrary-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the runtime scaling value stored in the file. This function uses the waveformIndex parameter as the key to retrieve the waveform property. Syntaxint32 __stdcall niRFSGPlayback_ReadRuntimeScalingFromFile(ViConstString filePath, ViInt32 waveformIndex, ViReal64 runtimeScaling)ParametersNameDire

### niRFSGPlayback_ReadRuntimeScalingFromFile

Returns the runtime scaling value stored in the file. This function uses the **waveformIndex** parameter as the key to retrieve the waveform property.

#### Syntax

int32 __stdcall niRFSGPlayback_ReadRuntimeScalingFromFile(ViConstString filePath, ViInt32 waveformIndex, ViReal64 runtimeScaling)

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| filePath | [in] | ViConstString | Specifies the absolute path to the TDMS file from which the playback library reads the waveforms. |
| waveformIndex | [in] | ViInt32 | Specifies the waveform number in the file for which you want to read the runtime scaling value. |
| runtimeScaling | [out] | ViReal64 | Returns the runtime scaling value stored in the file for the waveform number that you specified in the waveformIndex parameter. This value is expressed in dB. |

#### Returns

Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred. To obtain a text description of the status code and additional information about the error condition, call the [niRFSGPlayback_GetError](group____root__ni_r_f_s_g_playback__functions_1ga5985403bcf5416e344ce264b3a73fc4a.html) function. The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

Utility

<!--NI_TOPIC bundle=rfsgplaybacklibrary-c-api-ref path=group____root__ni_r_f_s_g_playback__functions__utility_1ga297c954ed58dba341fd58205f1e0dac9.html language=enus -->
## TOPIC 00059: niRFSGPlayback_ReadWaveformFileVersionFromFile

- bundle_id: `rfsgplaybacklibrary-c-api-ref`
- source_path: `group____root__ni_r_f_s_g_playback__functions__utility_1ga297c954ed58dba341fd58205f1e0dac9.html`
- source_url: https://docs-be.ni.com/bundle/rfsgplaybacklibrary-c-api-ref/raw/resource/enus/group____root__ni_r_f_s_g_playback__functions__utility_1ga297c954ed58dba341fd58205f1e0dac9.html
- document_id: `rfsgplaybacklibrary-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the waveform file version of the waveform stored in the file. Syntaxint32 __stdcall niRFSGPlayback_ReadWaveformFileVersionFromFile(ViConstString filePath, ViInt32 waveformFileVersionBufferSize, ViChar waveformFileVersion)ParametersNameDirectionTypeDescriptionfilePath[in]ViConstStringSpecifie

### niRFSGPlayback_ReadWaveformFileVersionFromFile

Returns the waveform file version of the waveform stored in the file.

#### Syntax

int32 __stdcall niRFSGPlayback_ReadWaveformFileVersionFromFile(ViConstString filePath, ViInt32 waveformFileVersionBufferSize, ViChar waveformFileVersion)

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| filePath | [in] | ViConstString | Specifies the absolute path to the TDMS file from which the playback library reads the waveforms. |
| waveformFileVersionBufferSize | [in] | ViInt32 | Specifies the buffer size of the waveformFileVersion parameter. |
| waveformFileVersion | [out] | ViChar | Returns the waveform file version of the waveform stored in the file. |

#### Returns

Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred. To obtain a text description of the status code and additional information about the error condition, call the [niRFSGPlayback_GetError](group____root__ni_r_f_s_g_playback__functions_1ga5985403bcf5416e344ce264b3a73fc4a.html) function. The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

Utility

<!--NI_TOPIC bundle=rfsgplaybacklibrary-c-api-ref path=group____root__ni_r_f_s_g_playback__functions__utility_1ga8719cdf29b49aa9ed70f975087fadae6.html language=enus -->
## TOPIC 00060: niRFSGPlayback_ReadSampleRateFromFile

- bundle_id: `rfsgplaybacklibrary-c-api-ref`
- source_path: `group____root__ni_r_f_s_g_playback__functions__utility_1ga8719cdf29b49aa9ed70f975087fadae6.html`
- source_url: https://docs-be.ni.com/bundle/rfsgplaybacklibrary-c-api-ref/raw/resource/enus/group____root__ni_r_f_s_g_playback__functions__utility_1ga8719cdf29b49aa9ed70f975087fadae6.html
- document_id: `rfsgplaybacklibrary-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the sample rate stored in the file. This function uses the waveformIndex as the key to retrieve the waveform property. Syntaxint32 __stdcall niRFSGPlayback_ReadSampleRateFromFile(ViConstString filePath, ViInt32 waveformIndex, ViReal64 sampleRate)ParametersNameDirectionTypeDescriptionfilePath

### niRFSGPlayback_ReadSampleRateFromFile

Returns the sample rate stored in the file. This function uses the **waveformIndex** as the key to retrieve the waveform property.

#### Syntax

int32 __stdcall niRFSGPlayback_ReadSampleRateFromFile(ViConstString filePath, ViInt32 waveformIndex, ViReal64 sampleRate)

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| filePath | [in] | ViConstString | Specifies the absolute path to the TDMS file from which the playback library reads the waveforms. |
| waveformIndex | [in] | ViInt32 | Specifies the waveform number in the file for which you want to read the sample rate. |
| sampleRate | [out] | ViReal64 | Returns the sample rate value, stored in the file for the waveform number which you specified in the waveformIndex parameter. |

#### Returns

Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred. To obtain a text description of the status code and additional information about the error condition, call the [niRFSGPlayback_GetError](group____root__ni_r_f_s_g_playback__functions_1ga5985403bcf5416e344ce264b3a73fc4a.html) function. The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

Utility

<!--NI_TOPIC bundle=rfsgplaybacklibrary-c-api-ref path=group____root__ni_r_f_s_g_playback__functions__utility_1gaa018c738ba1fea6a7c380537f9562be6.html language=enus -->
## TOPIC 00061: niRFSGPlayback_ReadBurstStopLocationsFromFile

- bundle_id: `rfsgplaybacklibrary-c-api-ref`
- source_path: `group____root__ni_r_f_s_g_playback__functions__utility_1gaa018c738ba1fea6a7c380537f9562be6.html`
- source_url: https://docs-be.ni.com/bundle/rfsgplaybacklibrary-c-api-ref/raw/resource/enus/group____root__ni_r_f_s_g_playback__functions__utility_1gaa018c738ba1fea6a7c380537f9562be6.html
- document_id: `rfsgplaybacklibrary-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the RF blanking marker positions stored in the NI-RFSG database. This function uses the waveformName as the key to retrieve the waveform property. Syntaxint32 __stdcall niRFSGPlayback_ReadBurstStopLocationsFromFile(ViConstString filePath, ViInt32 waveformIndex, ViInt32 burstStopLocationsSize

### niRFSGPlayback_ReadBurstStopLocationsFromFile

Returns the RF blanking marker positions stored in the NI-RFSG database. This function uses the **waveformName** as the key to retrieve the waveform property.

#### Syntax

int32 __stdcall niRFSGPlayback_ReadBurstStopLocationsFromFile(ViConstString filePath, ViInt32 waveformIndex, ViInt32 burstStopLocationsSize, ViInt32[] burstStopLocations, ViInt32 actualNumberOfLocations)

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| filePath | [in] | ViConstString | Specifies the absolute path to the TDMS file from which the playback library reads the waveforms. |
| waveformIndex | [in] | ViInt32 | Specifies the waveform name for which you want to retrieve the burst stop locations. |
| burstStopLocationsSize | [in] | ViInt32 | Specifies the size of the burstStopLocations array. Set the burstStopLocationsSize parameter to 0 to get the size of the burstStartLocations array in the actualNumberOfLocations parameter. |
| burstStopLocations | [out] | ViInt32[] | Returns an array of the burst stop locations, stored in the file for the waveform number which you specified in the waveformIndex parameter. |
| actualNumberOfLocations | [out] | ViInt32 | Returns the actual size of the array, if you pass NULL to all output array parameters, and set the burstStopLocationsSize parameter to 0. |

#### Returns

Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred. To obtain a text description of the status code and additional information about the error condition, call the [niRFSGPlayback_GetError](group____root__ni_r_f_s_g_playback__functions_1ga5985403bcf5416e344ce264b3a73fc4a.html) function. The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

Utility

<!--NI_TOPIC bundle=rfsgplaybacklibrary-c-api-ref path=group____root__ni_r_f_s_g_playback__functions__utility_1gaba734c518ed0fd4e80d46feec959e683.html language=enus -->
## TOPIC 00062: niRFSGPlayback_ReadPAPRFromFile

- bundle_id: `rfsgplaybacklibrary-c-api-ref`
- source_path: `group____root__ni_r_f_s_g_playback__functions__utility_1gaba734c518ed0fd4e80d46feec959e683.html`
- source_url: https://docs-be.ni.com/bundle/rfsgplaybacklibrary-c-api-ref/raw/resource/enus/group____root__ni_r_f_s_g_playback__functions__utility_1gaba734c518ed0fd4e80d46feec959e683.html
- document_id: `rfsgplaybacklibrary-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the peak to average power ratio (PAPR) stored in the file. This function uses the waveformIndex parameter as the key to retrieve the waveform property. Syntaxint32 __stdcall niRFSGPlayback_ReadPAPRFromFile(ViConstString filePath, ViInt32 waveformIndex, ViReal64 papr)ParametersNameDirectionTy

### niRFSGPlayback_ReadPAPRFromFile

Returns the peak to average power ratio (PAPR) stored in the file. This function uses the **waveformIndex** parameter as the key to retrieve the waveform property.

#### Syntax

int32 __stdcall niRFSGPlayback_ReadPAPRFromFile(ViConstString filePath, ViInt32 waveformIndex, ViReal64 papr)

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| filePath | [in] | ViConstString | Specifies the absolute path to the TDMS file from which the playback library reads the waveforms. |
| waveformIndex | [in] | ViInt32 | Specifies the waveform number in the file for which you want to read the PAPR. |
| papr | [out] | ViReal64 | Returns the PAPR stored in the file for the waveform number that you specified in the waveformIndex parameter. This value is expressed in dB. |

#### Returns

Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred. To obtain a text description of the status code and additional information about the error condition, call the [niRFSGPlayback_GetError](group____root__ni_r_f_s_g_playback__functions_1ga5985403bcf5416e344ce264b3a73fc4a.html) function. The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

Utility

<!--NI_TOPIC bundle=rfsgplaybacklibrary-c-api-ref path=group____root__ni_r_f_s_g_playback__functions__utility_1gaefb6f5f1d96a896c073a6f8031037498.html language=enus -->
## TOPIC 00063: niRFSGPlayback_ReadRFBlankingMarkerSourceFromFile

- bundle_id: `rfsgplaybacklibrary-c-api-ref`
- source_path: `group____root__ni_r_f_s_g_playback__functions__utility_1gaefb6f5f1d96a896c073a6f8031037498.html`
- source_url: https://docs-be.ni.com/bundle/rfsgplaybacklibrary-c-api-ref/raw/resource/enus/group____root__ni_r_f_s_g_playback__functions__utility_1gaefb6f5f1d96a896c073a6f8031037498.html
- document_id: `rfsgplaybacklibrary-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the RF blanking marker source stored in the file. This function uses the waveformIndex as the key to retrieve the waveform property. Syntaxint32 __stdcall niRFSGPlayback_ReadRFBlankingMarkerSourceFromFile(ViConstString filePath, ViInt32 waveformIndex, ViInt32 markerSourceSize, ViChar[] marke

### niRFSGPlayback_ReadRFBlankingMarkerSourceFromFile

Returns the RF blanking marker source stored in the file. This function uses the **waveformIndex** as the key to retrieve the waveform property.

#### Syntax

int32 __stdcall niRFSGPlayback_ReadRFBlankingMarkerSourceFromFile(ViConstString filePath, ViInt32 waveformIndex, ViInt32 markerSourceSize, ViChar[] markerSource)

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| filePath | [in] | ViConstString | Specifies the absolute path to the TDMS file from which the playback library reads the waveforms. |
| waveformIndex | [in] | ViInt32 | Specifies the waveform number in the file for which you want to read the RF blanking marker source. |
| markerSourceSize | [in] | ViInt32 | Specifies the size of the array in the markerSource parameter. |
| markerSource | [out] | ViChar[] | Returns the RF blanking marker source value, stored in the file for the waveform number which you specified in the waveformIndex parameter. |

#### Returns

Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred. To obtain a text description of the status code and additional information about the error condition, call the [niRFSGPlayback_GetError](group____root__ni_r_f_s_g_playback__functions_1ga5985403bcf5416e344ce264b3a73fc4a.html) function. The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

Utility

<!--NI_TOPIC bundle=rfsgplaybacklibrary-c-api-ref path=group____root__ni_r_f_s_g_playback__functions__utility_1gaf3e0027be9d21f2dbe553769ed162ec6.html language=enus -->
## TOPIC 00064: niRFSGPlayback_ReadSignalBandwidthFromFile

- bundle_id: `rfsgplaybacklibrary-c-api-ref`
- source_path: `group____root__ni_r_f_s_g_playback__functions__utility_1gaf3e0027be9d21f2dbe553769ed162ec6.html`
- source_url: https://docs-be.ni.com/bundle/rfsgplaybacklibrary-c-api-ref/raw/resource/enus/group____root__ni_r_f_s_g_playback__functions__utility_1gaf3e0027be9d21f2dbe553769ed162ec6.html
- document_id: `rfsgplaybacklibrary-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the signal bandwidth stored in the file. This function uses the waveformIndex parameter as the key to retrieve the waveform property. Syntaxint32 __stdcall niRFSGPlayback_ReadSignalBandwidthFromFile(ViConstString filePath, ViInt32 waveformIndex, ViReal64 signalBandwidth)ParametersNameDirecti

### niRFSGPlayback_ReadSignalBandwidthFromFile

Returns the signal bandwidth stored in the file. This function uses the **waveformIndex** parameter as the key to retrieve the waveform property.

#### Syntax

int32 __stdcall niRFSGPlayback_ReadSignalBandwidthFromFile(ViConstString filePath, ViInt32 waveformIndex, ViReal64 signalBandwidth)

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| filePath | [in] | ViConstString | Specifies the absolute path to the TDMS file from which the playback library reads the waveforms. |
| waveformIndex | [in] | ViInt32 | Specifies the waveform number in the file for which you want to read the signal bandwidth. |
| signalBandwidth | [out] | ViReal64 | Returns the signal bandwidth stored in the file for the waveform number that you specified in the waveformIndex parameter. |

#### Returns

Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred. To obtain a text description of the status code and additional information about the error condition, call the [niRFSGPlayback_GetError](group____root__ni_r_f_s_g_playback__functions_1ga5985403bcf5416e344ce264b3a73fc4a.html) function. The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

Utility

<!--NI_TOPIC bundle=rfsgplaybacklibrary-c-api-ref path=group____root__ni_r_f_s_g_playback__functions__utility_1gafab62ab60cfcabebf3835cfb24631b18.html language=enus -->
## TOPIC 00065: niRFSGPlayback_ReadBurstStartLocationsFromFile

- bundle_id: `rfsgplaybacklibrary-c-api-ref`
- source_path: `group____root__ni_r_f_s_g_playback__functions__utility_1gafab62ab60cfcabebf3835cfb24631b18.html`
- source_url: https://docs-be.ni.com/bundle/rfsgplaybacklibrary-c-api-ref/raw/resource/enus/group____root__ni_r_f_s_g_playback__functions__utility_1gafab62ab60cfcabebf3835cfb24631b18.html
- document_id: `rfsgplaybacklibrary-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the burst start locations stored in the file. This function uses the waveformIndex parameter as the key to retrieve the waveform property. Syntaxint32 __stdcall niRFSGPlayback_ReadBurstStartLocationsFromFile(ViConstString filePath, ViInt32 waveformIndex, ViInt32 burstStartLocationsSize, ViIn

### niRFSGPlayback_ReadBurstStartLocationsFromFile

Returns the burst start locations stored in the file. This function uses the **waveformIndex** parameter as the key to retrieve the waveform property.

#### Syntax

int32 __stdcall niRFSGPlayback_ReadBurstStartLocationsFromFile(ViConstString filePath, ViInt32 waveformIndex, ViInt32 burstStartLocationsSize, ViInt32[] burstStartLocations, ViInt32 actualNumberOfLocations)

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| filePath | [in] | ViConstString | Specifies the absolute path to the TDMS file from which the playback library reads the waveforms. |
| waveformIndex | [in] | ViInt32 | Specifies the waveform number in the file for which you want to read the burst start locations. |
| burstStartLocationsSize | [in] | ViInt32 | Specifies the size of the burstStartLocations array. Set the burstStartLocationsSize parameter to 0 to get the size of the burstStartLocations array in the actualNumberOfLocations parameter. |
| burstStartLocations | [out] | ViInt32[] | Returns an array of the burst start locations, stored in the file for the waveform number that you specified in the waveformIndex parameter. |
| actualNumberOfLocations | [out] | ViInt32 | Returns the actual size of the array, if you pass NULL to all output array parameters, and set the burstStartLocationsSize parameter to 0. |

#### Returns

Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred. To obtain a text description of the status code and additional information about the error condition, call the [niRFSGPlayback_GetError](group____root__ni_r_f_s_g_playback__functions_1ga5985403bcf5416e344ce264b3a73fc4a.html) function. The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

Utility

<!--NI_TOPIC bundle=rfsgplaybacklibrary-c-api-ref path=group____root__ni_r_f_s_g_playback__functions__utility_1gaff03b17559b08f60a89b0871c2012c9f.html language=enus -->
## TOPIC 00066: niRFSGPlayback_ReadWaveformSizeFromFile

- bundle_id: `rfsgplaybacklibrary-c-api-ref`
- source_path: `group____root__ni_r_f_s_g_playback__functions__utility_1gaff03b17559b08f60a89b0871c2012c9f.html`
- source_url: https://docs-be.ni.com/bundle/rfsgplaybacklibrary-c-api-ref/raw/resource/enus/group____root__ni_r_f_s_g_playback__functions__utility_1gaff03b17559b08f60a89b0871c2012c9f.html
- document_id: `rfsgplaybacklibrary-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the size of the waveform stored in the file. This function uses the waveformIndex parameter as the key to retrieve the waveform property. Syntaxint32 __stdcall niRFSGPlayback_ReadWaveformSizeFromFile(ViConstString filePath, ViInt32 waveformIndex, ViInt32 waveformSize)ParametersNameDirectionT

### niRFSGPlayback_ReadWaveformSizeFromFile

Returns the size of the waveform stored in the file. This function uses the **waveformIndex** parameter as the key to retrieve the waveform property.

#### Syntax

int32 __stdcall niRFSGPlayback_ReadWaveformSizeFromFile(ViConstString filePath, ViInt32 waveformIndex, ViInt32 waveformSize)

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| filePath | [in] | ViConstString | Specifies the absolute path to the TDMS file from which the playback library reads the waveforms. |
| waveformIndex | [in] | ViInt32 | Specifies the waveform number in the file for which you want to read the waveform size. |
| waveformSize | [out] | ViInt32 | Returns the size of the waveform stored in the file for the waveform number that you specified in the waveformIndex parameter. This value is expressed in samples. |

#### Returns

Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred. To obtain a text description of the status code and additional information about the error condition, call the [niRFSGPlayback_GetError](group____root__ni_r_f_s_g_playback__functions_1ga5985403bcf5416e344ce264b3a73fc4a.html) function. The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

Utility

<!--NI_TOPIC bundle=rfsgplaybacklibrary-c-api-ref path=group____root__ni_r_f_s_g_playback__functions__utility__obsolete.html language=enus -->
## TOPIC 00067: Obsolete

- bundle_id: `rfsgplaybacklibrary-c-api-ref`
- source_path: `group____root__ni_r_f_s_g_playback__functions__utility__obsolete.html`
- source_url: https://docs-be.ni.com/bundle/rfsgplaybacklibrary-c-api-ref/raw/resource/enus/group____root__ni_r_f_s_g_playback__functions__utility__obsolete.html
- document_id: `rfsgplaybacklibrary-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: GroupsNoneGroup membersNameDescriptionniRFSGPlayback_ReadPeakPowerAdjustmentFromFileReturns the peak power adjustment locations stored in the file. This function uses the waveformIndex as the key to retrieve the waveform property. niRFSGPlayback_ReadRFBlankingMarkerLocationsFromFileReturns the RF bl

### Obsolete

#### Groups

None

#### Group members

| Name | Description |
| --- | --- |
| niRFSGPlayback_ReadPeakPowerAdjustmentFromFile | Returns the peak power adjustment locations stored in the file. This function uses the waveformIndex as the key to retrieve the waveform property. |
| niRFSGPlayback_ReadRFBlankingMarkerLocationsFromFile | Returns the RF blanking marker locations stored in the file. This function uses the waveformIndex as the key to retrieve the waveform property. |

#### Attachments

None

Parent topic:

Utility

<!--NI_TOPIC bundle=rfsgplaybacklibrary-c-api-ref path=group____root__ni_r_f_s_g_playback__functions__utility__obsolete_1ga35e977e338c0ecae4ec52d73c7d555f7.html language=enus -->
## TOPIC 00068: niRFSGPlayback_ReadRFBlankingMarkerLocationsFromFile

- bundle_id: `rfsgplaybacklibrary-c-api-ref`
- source_path: `group____root__ni_r_f_s_g_playback__functions__utility__obsolete_1ga35e977e338c0ecae4ec52d73c7d555f7.html`
- source_url: https://docs-be.ni.com/bundle/rfsgplaybacklibrary-c-api-ref/raw/resource/enus/group____root__ni_r_f_s_g_playback__functions__utility__obsolete_1ga35e977e338c0ecae4ec52d73c7d555f7.html
- document_id: `rfsgplaybacklibrary-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the RF blanking marker locations stored in the file. This function uses the waveformIndex as the key to retrieve the waveform property. Syntaxint32 __stdcall niRFSGPlayback_ReadRFBlankingMarkerLocationsFromFile(ViConstString filePath, ViInt32 waveformIndex, ViInt32 markerLocationsSize, ViInt

### niRFSGPlayback_ReadRFBlankingMarkerLocationsFromFile

Returns the RF blanking marker locations stored in the file. This function uses the **waveformIndex** as the key to retrieve the waveform property.

#### Syntax

int32 __stdcall niRFSGPlayback_ReadRFBlankingMarkerLocationsFromFile(ViConstString filePath, ViInt32 waveformIndex, ViInt32 markerLocationsSize, ViInt32[] markerLocations, ViInt32 actualNumberOfLocations)

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| filePath | [in] | ViConstString | Specifies the absolute path to the TDMS file from which the playback library reads the waveforms. |
| waveformIndex | [in] | ViInt32 | Specifies the waveform number in the file for which you want to read the RF blanking marker locations. |
| markerLocationsSize | [in] | ViInt32 | Specifies the size of the markerLocations array. Set the markerLocationsSize parameter to 0 to get the size of the markerLocations array in the actualNumberOfLocations parameter. |
| markerLocations | [out] | ViInt32[] | Returns the array of RF blanking marker locations values, stored in the file, for the waveform number you specified in the waveformIndex parameter. |
| actualNumberOfLocations | [out] | ViInt32 | Returns the actual size of the array, if you pass NULL to all output array parameters, and set the markerLocationsSize parameter to 0. |

#### Returns

Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred. To obtain a text description of the status code and additional information about the error condition, call the [niRFSGPlayback_GetError](group____root__ni_r_f_s_g_playback__functions_1ga5985403bcf5416e344ce264b3a73fc4a.html) function. The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

Obsolete

<!--NI_TOPIC bundle=rfsgplaybacklibrary-c-api-ref path=group____root__ni_r_f_s_g_playback__functions__utility__obsolete_1gaa4847be6a1cbcacbee3f95b24e157faa.html language=enus -->
## TOPIC 00069: niRFSGPlayback_ReadPeakPowerAdjustmentFromFile

- bundle_id: `rfsgplaybacklibrary-c-api-ref`
- source_path: `group____root__ni_r_f_s_g_playback__functions__utility__obsolete_1gaa4847be6a1cbcacbee3f95b24e157faa.html`
- source_url: https://docs-be.ni.com/bundle/rfsgplaybacklibrary-c-api-ref/raw/resource/enus/group____root__ni_r_f_s_g_playback__functions__utility__obsolete_1gaa4847be6a1cbcacbee3f95b24e157faa.html
- document_id: `rfsgplaybacklibrary-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the peak power adjustment locations stored in the file. This function uses the waveformIndex as the key to retrieve the waveform property. Syntaxint32 __stdcall niRFSGPlayback_ReadPeakPowerAdjustmentFromFile(ViConstString filePath, ViInt32 waveformIndex, ViReal64 peakPowerAdjustment)Paramete

### niRFSGPlayback_ReadPeakPowerAdjustmentFromFile

Returns the peak power adjustment locations stored in the file. This function uses the **waveformIndex** as the key to retrieve the waveform property.

#### Syntax

int32 __stdcall niRFSGPlayback_ReadPeakPowerAdjustmentFromFile(ViConstString filePath, ViInt32 waveformIndex, ViReal64 peakPowerAdjustment)

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| filePath | [in] | ViConstString | Specifies the absolute path to the TDMS file from which the playback library reads the waveforms. |
| waveformIndex | [in] | ViInt32 | Specifies the waveform number in the file for which you want to read the peak power adjustment location. |
| peakPowerAdjustment | [out] | ViReal64 | Returns the peak power adjustment value, stored in the file for the waveform number which you specified in the waveformIndex parameter. |

#### Returns

Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred. To obtain a text description of the status code and additional information about the error condition, call the [niRFSGPlayback_GetError](group____root__ni_r_f_s_g_playback__functions_1ga5985403bcf5416e344ce264b3a73fc4a.html) function. The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

Obsolete

<!--NI_TOPIC bundle=rfsgplaybacklibrary-c-api-ref path=group__root__ni_r_f_s_g_playback.html language=enus -->
## TOPIC 00070: niRFSGPlayback.h

- bundle_id: `rfsgplaybacklibrary-c-api-ref`
- source_path: `group__root__ni_r_f_s_g_playback.html`
- source_url: https://docs-be.ni.com/bundle/rfsgplaybacklibrary-c-api-ref/raw/resource/enus/group__root__ni_r_f_s_g_playback.html
- document_id: `rfsgplaybacklibrary-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: GroupsAttributesFunctionsGroup membersNoneAttachmentsNone

### niRFSGPlayback.h

#### Groups

- Attributes
- Functions

#### Group members

None

#### Attachments

None
