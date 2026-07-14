# NI DOCUMENT BUNDLE: rfsgplaybacklibrary-labview-api-ref

<!--NI_BUNDLE_CHUNK bundle=rfsgplaybacklibrary-labview-api-ref start=1 end=62 -->
<!--NI_TOPIC bundle=rfsgplaybacklibrary-labview-api-ref path=instr-lib/nirfsgplayback/nirfsgplayback-clear-all-waveforms-vi.html language=enus -->
## TOPIC 00001: niRFSGPlayback Clear All Waveforms VI

- bundle_id: `rfsgplaybacklibrary-labview-api-ref`
- source_path: `instr-lib/nirfsgplayback/nirfsgplayback-clear-all-waveforms-vi.html`
- source_url: https://docs-be.ni.com/bundle/rfsgplaybacklibrary-labview-api-ref/raw/resource/enus/instr-lib/nirfsgplayback/nirfsgplayback-clear-all-waveforms-vi.html
- document_id: `rfsgplaybacklibrary-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Deletes all the waveforms from NI-RFSG memory and removes all the waveform properties from the NI-RFSG waveform database for the specified device. icon Inputs/Outputs civrn.png instrument handle in instrument handle in identifies the instrument session. instrument handle in is obtained from either t

### niRFSGPlayback Clear All Waveforms VI

Deletes all the waveforms from NI-RFSG memory and removes all the waveform properties from the NI-RFSG waveform database for the specified device.

[IMAGE alt='icon' src='nirfsgplayback-clear-all-waveforms-vi.png']

#### Inputs/Outputs

| instrument handle in — instrument handle in identifies the instrument session. instrument handle in is obtained from either the niRFSG Initialize VI or the niRFSG Initialize With Options VI. error in — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. instrument handle out — instrument handle out passes a reference from the instrument session to the next VI. error out — error out contains error information. This output provides standard error out functionality. |
| --- |

Parent topic:

NI-RFSG Playback Library

<!--NI_TOPIC bundle=rfsgplaybacklibrary-labview-api-ref path=instr-lib/nirfsgplayback/nirfsgplayback-clear-waveform-vi.html language=enus -->
## TOPIC 00002: niRFSGPlayback Clear Waveform VI

- bundle_id: `rfsgplaybacklibrary-labview-api-ref`
- source_path: `instr-lib/nirfsgplayback/nirfsgplayback-clear-waveform-vi.html`
- source_url: https://docs-be.ni.com/bundle/rfsgplaybacklibrary-labview-api-ref/raw/resource/enus/instr-lib/nirfsgplayback/nirfsgplayback-clear-waveform-vi.html
- document_id: `rfsgplaybacklibrary-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Deletes the waveform from NI-RFSG device memory and removes the waveform properties from NI-RFSG waveform database for the specified device. icon Inputs/Outputs civrn.png instrument handle in instrument handle in identifies the instrument session. instrument handle in is obtained from either the niR

### niRFSGPlayback Clear Waveform VI

Deletes the waveform from NI-RFSG device memory and removes the waveform properties from NI-RFSG waveform database for the specified device.

[IMAGE alt='icon' src='nirfsgplayback-clear-waveform-vi.png']

#### Inputs/Outputs

| instrument handle in — instrument handle in identifies the instrument session. instrument handle in is obtained from either the niRFSG Initialize VI or the niRFSG Initialize With Options VI. waveform name — waveform name specifies the name of the waveform to delete from the NI-RFSG database. error in — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. instrument handle out — instrument handle out passes a reference from the instrument session to the next VI. error out — error out contains error information. This output provides standard error out functionality. |
| --- |

Parent topic:

NI-RFSG Playback Library

<!--NI_TOPIC bundle=rfsgplaybacklibrary-labview-api-ref path=instr-lib/nirfsgplayback/nirfsgplayback-download-user-waveform-cdb-vi.html language=enus -->
## TOPIC 00003: niRFSGPlayback Download User Waveform (CDB) VI

- bundle_id: `rfsgplaybacklibrary-labview-api-ref`
- source_path: `instr-lib/nirfsgplayback/nirfsgplayback-download-user-waveform-cdb-vi.html`
- source_url: https://docs-be.ni.com/bundle/rfsgplaybacklibrary-labview-api-ref/raw/resource/enus/instr-lib/nirfsgplayback/nirfsgplayback-download-user-waveform-cdb-vi.html
- document_id: `rfsgplaybacklibrary-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Normalizes the input waveform and writes it into the NI RF vector signal generator. This VI computes the peak to average power ratio (PAPR) using the bursts in the waveform, stores the PAPR, sample rate, waveform size, and runtime scaling value of -1.5 dB in the NI-RFSG waveform database. icon Input

### niRFSGPlayback Download User Waveform (CDB) VI

Normalizes the input waveform and writes it into the NI RF vector signal generator. This VI computes the peak to average power ratio (PAPR) using the bursts in the waveform, stores the PAPR, sample rate, waveform size, and runtime scaling value of -1.5 dB in the NI-RFSG waveform database.

[IMAGE alt='icon' src='nirfsgplayback-download-user-waveform-cdb-vi.png']

#### Inputs/Outputs

| instrument handle in — instrument handle in identifies the instrument session. instrument handle in is obtained from either the niRFSG Initialize VI or the niRFSG Initialize With Options VI. waveform name — waveform name specifies the name used to write the waveform to the NI-RFSG device memory. waveform in — waveform in specifies an array of the complex double waveform clusters which has to be downloaded to the device. t0 — t0 specifies the start time of the given input waveform. dt — dt specifies the time interval between the samples in the given input waveform. y — y specifies an array of the complex double waveform to be downloaded to the device. burst present — burst present specifies whether the burst is present in the given waveform. error in — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. instrument handle out — instrument handle out passes a reference from the instrument session to the next VI. error out — error out contains error information. This output provides standard error out functionality. |
| --- |
| t0 — t0 specifies the start time of the given input waveform. dt — dt specifies the time interval between the samples in the given input waveform. y — y specifies an array of the complex double waveform to be downloaded to the device. |

Parent topic:

niRFSGPlayback Download User Waveform VI

<!--NI_TOPIC bundle=rfsgplaybacklibrary-labview-api-ref path=instr-lib/nirfsgplayback/nirfsgplayback-download-user-waveform-csg-vi.html language=enus -->
## TOPIC 00004: niRFSGPlayback Download User Waveform (CSG) VI

- bundle_id: `rfsgplaybacklibrary-labview-api-ref`
- source_path: `instr-lib/nirfsgplayback/nirfsgplayback-download-user-waveform-csg-vi.html`
- source_url: https://docs-be.ni.com/bundle/rfsgplaybacklibrary-labview-api-ref/raw/resource/enus/instr-lib/nirfsgplayback/nirfsgplayback-download-user-waveform-csg-vi.html
- document_id: `rfsgplaybacklibrary-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Normalizes the input waveform and writes it into the NI RF vector signal generator. This VI computes the peak to average power ratio (PAPR) using the bursts in the waveform, stores the PAPR, sample rate, waveform size, and runtime scaling value of -1.5 dB in the NI-RFSG waveform database. icon Input

### niRFSGPlayback Download User Waveform (CSG) VI

Normalizes the input waveform and writes it into the NI RF vector signal generator. This VI computes the peak to average power ratio (PAPR) using the bursts in the waveform, stores the PAPR, sample rate, waveform size, and runtime scaling value of -1.5 dB in the NI-RFSG waveform database.

[IMAGE alt='icon' src='nirfsgplayback-download-user-waveform-csg-vi.png']

#### Inputs/Outputs

| instrument handle in — instrument handle in identifies the instrument session. instrument handle in is obtained from either the niRFSG Initialize VI or the niRFSG Initialize With Options VI. waveform name — waveform name specifies the name used to write the waveform to the NI-RFSG device memory. waveform in — waveform in specifies an array of the complex single waveform clusters which has to be downloaded to the device. t0 — t0 specifies the start time of the given input waveform. dt — dt specifies the time interval between the samples in the given input waveform. y — y specifies an array of the complex single waveform to be downloaded to the device. burst present — burst present specifies whether the burst is present in the given waveform. error in — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. instrument handle out — instrument handle out passes a reference from the instrument session to the next VI. error out — error out contains error information. This output provides standard error out functionality. |
| --- |
| t0 — t0 specifies the start time of the given input waveform. dt — dt specifies the time interval between the samples in the given input waveform. y — y specifies an array of the complex single waveform to be downloaded to the device. |

Parent topic:

niRFSGPlayback Download User Waveform VI

<!--NI_TOPIC bundle=rfsgplaybacklibrary-labview-api-ref path=instr-lib/nirfsgplayback/nirfsgplayback-download-user-waveform-vi.html language=enus -->
## TOPIC 00005: niRFSGPlayback Download User Waveform VI

- bundle_id: `rfsgplaybacklibrary-labview-api-ref`
- source_path: `instr-lib/nirfsgplayback/nirfsgplayback-download-user-waveform-vi.html`
- source_url: https://docs-be.ni.com/bundle/rfsgplaybacklibrary-labview-api-ref/raw/resource/enus/instr-lib/nirfsgplayback/nirfsgplayback-download-user-waveform-vi.html
- document_id: `rfsgplaybacklibrary-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Normalizes the input waveform and writes it into the NI RF vector signal generator. This VI computes the peak to average power ratio (PAPR) using the bursts in the waveform, stores the PAPR, sample rate, waveform size, and runtime scaling value of -1.5 dB in the NI-RFSG waveform database. icon

### niRFSGPlayback Download User Waveform VI

Normalizes the input waveform and writes it into the NI RF vector signal generator. This VI computes the peak to average power ratio (PAPR) using the bursts in the waveform, stores the PAPR, sample rate, waveform size, and runtime scaling value of -1.5 dB in the NI-RFSG waveform database.

[IMAGE alt='icon' src='nirfsgplayback-download-user-waveform-vi.png']

- [niRFSGPlayback Download User Waveform (CSG) VI](../../instr-lib/nirfsgplayback/nirfsgplayback-download-user-waveform-csg-vi.html) Normalizes the input waveform and writes it into the NI RF vector signal generator. This VI computes the peak to average power ratio (PAPR) using the bursts in the waveform, stores the PAPR, sample rate, waveform size, and runtime scaling value of -1.5 dB in the NI-RFSG waveform database.
- [niRFSGPlayback Download User Waveform (CDB) VI](../../instr-lib/nirfsgplayback/nirfsgplayback-download-user-waveform-cdb-vi.html) Normalizes the input waveform and writes it into the NI RF vector signal generator. This VI computes the peak to average power ratio (PAPR) using the bursts in the waveform, stores the PAPR, sample rate, waveform size, and runtime scaling value of -1.5 dB in the NI-RFSG waveform database.

Parent topic:

NI-RFSG Playback Library

<!--NI_TOPIC bundle=rfsgplaybacklibrary-labview-api-ref path=instr-lib/nirfsgplayback/nirfsgplayback-read-and-download-waveform-from-file-1-wfm-1-rfsg-tdms-vi.html language=enus -->
## TOPIC 00006: niRFSGPlayback Read and Download Waveform From File (1 Wfm, 1 RFSG, TDMS) VI

- bundle_id: `rfsgplaybacklibrary-labview-api-ref`
- source_path: `instr-lib/nirfsgplayback/nirfsgplayback-read-and-download-waveform-from-file-1-wfm-1-rfsg-tdms-vi.html`
- source_url: https://docs-be.ni.com/bundle/rfsgplaybacklibrary-labview-api-ref/raw/resource/enus/instr-lib/nirfsgplayback/nirfsgplayback-read-and-download-waveform-from-file-1-wfm-1-rfsg-tdms-vi.html
- document_id: `rfsgplaybacklibrary-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Reads a waveform from a TDMS file, and downloads it to the NI RF vector signal generator. This VI reads the following information from the TDMS file and writes it into the NI-RFSG waveform database: Sample Rate PAPR and Runtime Scaling, or Peak Power Adjustment RF Blanking Marker Locations RF Blanki

### niRFSGPlayback Read and Download Waveform From File (1 Wfm, 1 RFSG, TDMS) VI

Reads a waveform from a TDMS file, and downloads it to the NI RF vector signal generator.

This VI reads the following information from the TDMS file and writes it into the NI-RFSG waveform database:

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

This VI internally sets niRFSG Power Level Type property value to **Peak Power** before writing the waveform to NI-RFSG device memory.

This VI returns an error, if the TDMS file has more than one waveform.

[IMAGE alt='icon' src='nirfsgplayback-read-and-download-waveform-from-file-1-wfm-1-rfsg-tdms-vi.png']

#### Inputs/Outputs

| instrument handle in — instrument handle in identifies the instrument session. instrument handle in is obtained from either the niRFSG Initialize VI or the niRFSG Initialize With Options VI. waveform name — waveform name specifies the name of the waveform used to store the waveform in NI-RFSG device memory and waveform properties in the NI-RFSG waveform database. file path — file path specifies the absolute path to the TDMS file from which the playback library reads the waveforms. error in — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. instrument handle out — instrument handle out passes a reference from the instrument session to the next VI. error out — error out contains error information. This output provides standard error out functionality. |
| --- |

Parent topic:

niRFSGPlayback Read and Download Waveform From File VI

<!--NI_TOPIC bundle=rfsgplaybacklibrary-labview-api-ref path=instr-lib/nirfsgplayback/nirfsgplayback-read-and-download-waveform-from-file-1-wfm-per-rfsg-tdms-vi.html language=enus -->
## TOPIC 00007: niRFSGPlayback Read and Download Waveform From File (1 Wfm per RFSG, TDMS) VI

- bundle_id: `rfsgplaybacklibrary-labview-api-ref`
- source_path: `instr-lib/nirfsgplayback/nirfsgplayback-read-and-download-waveform-from-file-1-wfm-per-rfsg-tdms-vi.html`
- source_url: https://docs-be.ni.com/bundle/rfsgplaybacklibrary-labview-api-ref/raw/resource/enus/instr-lib/nirfsgplayback/nirfsgplayback-read-and-download-waveform-from-file-1-wfm-per-rfsg-tdms-vi.html
- document_id: `rfsgplaybacklibrary-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Reads the waveforms from a TDMS file, and downloads one waveform into each of the NI RF vector signal generators. The first waveform in the TDMS file is downloaded to the first NI RF vector signal generator and so on, until all the waveforms are downloaded. This VI reads the following information fr

### niRFSGPlayback Read and Download Waveform From File (1 Wfm per RFSG, TDMS) VI

Reads the waveforms from a TDMS file, and downloads one waveform into each of the NI RF vector signal generators. The first waveform in the TDMS file is downloaded to the first NI RF vector signal generator and so on, until all the waveforms are downloaded.

This VI reads the following information from the TDMS file and writes it into the NI-RFSG waveform database:

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

This VI internally sets niRFSG Power Level Type property to **Peak Power** before writing the waveform to NI-RFSG device memory. This VI completes this tasks for each NI-RFSG session.

This VI returns an error, if the number of waveforms in the TDMS file does not match the number of RFSG sessions.

[IMAGE alt='icon' src='nirfsgplayback-read-and-download-waveform-from-file-1-wfm-per-rfsg-tdms-vi.png']

#### Inputs/Outputs

| instrument handles in — instrument handles in identifies instruments for multiple NI-RFSG sessions. instrument handles in is obtained from the niRFSG Initialize VI or the niRFSG Initialize With Options VI. waveform name — waveform name specifies the name of the waveform used to store the waveform in NI-RFSG device memory and waveform properties in the NI-RFSG waveform database. file path — file path specifies the absolute path to the TDMS file from which the playback library reads the waveforms. error in — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. instrument handles out — instrument handles out passes an array of NI-RFSG instrument sessions to the next VI. error out — error out contains error information. This output provides standard error out functionality. |
| --- |

Parent topic:

niRFSGPlayback Read and Download Waveform From File VI

<!--NI_TOPIC bundle=rfsgplaybacklibrary-labview-api-ref path=instr-lib/nirfsgplayback/nirfsgplayback-read-and-download-waveform-from-file-vi.html language=enus -->
## TOPIC 00008: niRFSGPlayback Read and Download Waveform From File VI

- bundle_id: `rfsgplaybacklibrary-labview-api-ref`
- source_path: `instr-lib/nirfsgplayback/nirfsgplayback-read-and-download-waveform-from-file-vi.html`
- source_url: https://docs-be.ni.com/bundle/rfsgplaybacklibrary-labview-api-ref/raw/resource/enus/instr-lib/nirfsgplayback/nirfsgplayback-read-and-download-waveform-from-file-vi.html
- document_id: `rfsgplaybacklibrary-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Reads the waveform stored in a technical data management streaming (TDMS) file, downloads it to NI RF vector signal generators, and stores the waveform properties found in the TDMS file in the NI-RFSG waveform database. icon

### niRFSGPlayback Read and Download Waveform From File VI

Reads the waveform stored in a technical data management streaming (TDMS) file, downloads it to NI RF vector signal generators, and stores the waveform properties found in the TDMS file in the NI-RFSG waveform database.

[IMAGE alt='icon' src='nirfsgplayback-read-and-download-waveform-from-file-vi.png']

- [niRFSGPlayback Read and Download Waveform From File (1 Wfm, 1 RFSG, TDMS) VI](../../instr-lib/nirfsgplayback/nirfsgplayback-read-and-download-waveform-from-file-1-wfm-1-rfsg-tdms-vi.html) Reads a waveform from a TDMS file, and downloads it to the NI RF vector signal generator.
- [niRFSGPlayback Read and Download Waveform From File (1 Wfm per RFSG, TDMS) VI](../../instr-lib/nirfsgplayback/nirfsgplayback-read-and-download-waveform-from-file-1-wfm-per-rfsg-tdms-vi.html) Reads the waveforms from a TDMS file, and downloads one waveform into each of the NI RF vector signal generators. The first waveform in the TDMS file is downloaded to the first NI RF vector signal generator and so on, until all the waveforms are downloaded.

Parent topic:

NI-RFSG Playback Library

<!--NI_TOPIC bundle=rfsgplaybacklibrary-labview-api-ref path=instr-lib/nirfsgplayback/nirfsgplayback-read-burst-start-locations-from-file-vi.html language=enus -->
## TOPIC 00009: niRFSGPlayback Read Burst Start Locations From File VI

- bundle_id: `rfsgplaybacklibrary-labview-api-ref`
- source_path: `instr-lib/nirfsgplayback/nirfsgplayback-read-burst-start-locations-from-file-vi.html`
- source_url: https://docs-be.ni.com/bundle/rfsgplaybacklibrary-labview-api-ref/raw/resource/enus/instr-lib/nirfsgplayback/nirfsgplayback-read-burst-start-locations-from-file-vi.html
- document_id: `rfsgplaybacklibrary-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the burst start locations stored in the file. This VI uses the waveform index parameter as the key to retrieve the waveform property. icon Inputs/Outputs cpath.png file path file path specifies the absolute path to the TDMS file from which the playback library reads the waveform. ci32.png wa

### niRFSGPlayback Read Burst Start Locations From File VI

Returns the burst start locations stored in the file. This VI uses the **waveform index** parameter as the key to retrieve the waveform property.

[IMAGE alt='icon' src='nirfsgplayback-read-burst-start-locations-from-file-vi.png']

#### Inputs/Outputs

| file path — file path specifies the absolute path to the TDMS file from which the playback library reads the waveform. waveform index — waveform index specifies the waveform number in the file for which you want to read the burst start locations. error in — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. burst start locations — burst start locations returns an array of the burst start locations stored in the file for the waveform number that you specified in the waveform index parameter. error out — error out contains error information. This output provides standard error out functionality. |
| --- |

Parent topic:

Utility

<!--NI_TOPIC bundle=rfsgplaybacklibrary-labview-api-ref path=instr-lib/nirfsgplayback/nirfsgplayback-read-burst-stop-locations-from-file-vi.html language=enus -->
## TOPIC 00010: niRFSGPlayback Read Burst Stop Locations From File VI

- bundle_id: `rfsgplaybacklibrary-labview-api-ref`
- source_path: `instr-lib/nirfsgplayback/nirfsgplayback-read-burst-stop-locations-from-file-vi.html`
- source_url: https://docs-be.ni.com/bundle/rfsgplaybacklibrary-labview-api-ref/raw/resource/enus/instr-lib/nirfsgplayback/nirfsgplayback-read-burst-stop-locations-from-file-vi.html
- document_id: `rfsgplaybacklibrary-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the burst stop locations stored in the file. This VI uses the waveform index parameter as the key to retrieve the waveform property. icon Inputs/Outputs cpath.png file path file path specifies the absolute path to the TDMS file from which the playback library reads the waveform. ci32.png wav

### niRFSGPlayback Read Burst Stop Locations From File VI

Returns the burst stop locations stored in the file. This VI uses the **waveform index** parameter as the key to retrieve the waveform property.

[IMAGE alt='icon' src='nirfsgplayback-read-burst-stop-locations-from-file-vi.png']

#### Inputs/Outputs

| file path — file path specifies the absolute path to the TDMS file from which the playback library reads the waveform. waveform index — waveform index specifies the waveform number in the file for which you want to read the burst stop locations. error in — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. burst stop locations — burst stop locations returns an array of the burst stop locations stored in the file for the waveform number that you specified in the waveform index parameter. error out — error out contains error information. This output provides standard error out functionality. |
| --- |

Parent topic:

Utility

<!--NI_TOPIC bundle=rfsgplaybacklibrary-labview-api-ref path=instr-lib/nirfsgplayback/nirfsgplayback-read-papr-from-file-vi.html language=enus -->
## TOPIC 00011: niRFSGPlayback Read PAPR From File VI

- bundle_id: `rfsgplaybacklibrary-labview-api-ref`
- source_path: `instr-lib/nirfsgplayback/nirfsgplayback-read-papr-from-file-vi.html`
- source_url: https://docs-be.ni.com/bundle/rfsgplaybacklibrary-labview-api-ref/raw/resource/enus/instr-lib/nirfsgplayback/nirfsgplayback-read-papr-from-file-vi.html
- document_id: `rfsgplaybacklibrary-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the peak to average power ratio (PAPR) stored in the file. This VI uses the waveform index parameter as the key to read the waveform property. icon Inputs/Outputs cpath.png file path file path specifies the absolute path to the TDMS file from which the playback library reads the waveform. ci

### niRFSGPlayback Read PAPR From File VI

Returns the peak to average power ratio (PAPR) stored in the file. This VI uses the **waveform index** parameter as the key to read the waveform property.

[IMAGE alt='icon' src='nirfsgplayback-read-papr-from-file-vi.png']

#### Inputs/Outputs

| file path — file path specifies the absolute path to the TDMS file from which the playback library reads the waveform. waveform index — waveform index specifies the waveform number in the file for which you want to read the PAPR. error in — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. PAPR — PAPR returns the PAPR stored in the file for the waveform number that you specified in the waveform index parameter. This value is expressed in dB. error out — error out contains error information. This output provides standard error out functionality. |
| --- |

Parent topic:

Utility

<!--NI_TOPIC bundle=rfsgplaybacklibrary-labview-api-ref path=instr-lib/nirfsgplayback/nirfsgplayback-read-peak-power-adjustment-from-file-vi.html language=enus -->
## TOPIC 00012: niRFSGPlayback Read Peak Power Adjustment From File VI

- bundle_id: `rfsgplaybacklibrary-labview-api-ref`
- source_path: `instr-lib/nirfsgplayback/nirfsgplayback-read-peak-power-adjustment-from-file-vi.html`
- source_url: https://docs-be.ni.com/bundle/rfsgplaybacklibrary-labview-api-ref/raw/resource/enus/instr-lib/nirfsgplayback/nirfsgplayback-read-peak-power-adjustment-from-file-vi.html
- document_id: `rfsgplaybacklibrary-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the value of the peak power adjustment stored in the file. This VI uses the waveform index as the key to retrieve the waveform property. icon Inputs/Outputs cpath.png file path file path specifies the absolute path to the TDMS file from which the playback library reads the waveform. ci32.png

### niRFSGPlayback Read Peak Power Adjustment From File VI

Returns the value of the peak power adjustment stored in the file. This VI uses the **waveform index** as the key to retrieve the waveform property.

[IMAGE alt='icon' src='nirfsgplayback-read-peak-power-adjustment-from-file-vi.png']

#### Inputs/Outputs

| file path — file path specifies the absolute path to the TDMS file from which the playback library reads the waveform. waveform index — waveform index specifies the waveform number in the file for which you want to read the peak power adjustment location. error in — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. peak power adjustment — peak power adjustment returns the peak power adjustment value stored in the file for the waveform number that you specified in the waveform index parameter. error out — error out contains error information. This output provides standard error out functionality. |
| --- |

Parent topic:

Obsolete

<!--NI_TOPIC bundle=rfsgplaybacklibrary-labview-api-ref path=instr-lib/nirfsgplayback/nirfsgplayback-read-rf-blanking-enabled-from-file-vi.html language=enus -->
## TOPIC 00013: niRFSGPlayback Read RF Blanking Enabled From File VI

- bundle_id: `rfsgplaybacklibrary-labview-api-ref`
- source_path: `instr-lib/nirfsgplayback/nirfsgplayback-read-rf-blanking-enabled-from-file-vi.html`
- source_url: https://docs-be.ni.com/bundle/rfsgplaybacklibrary-labview-api-ref/raw/resource/enus/instr-lib/nirfsgplayback/nirfsgplayback-read-rf-blanking-enabled-from-file-vi.html
- document_id: `rfsgplaybacklibrary-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the RF blanking enabled value stored in the file. This VI uses the waveform index parameter as the key to retrieve the waveform property. icon Inputs/Outputs cpath.png file path file path specifies the absolute path to the TDMS file from which the playback library reads the waveform. ci32.pn

### niRFSGPlayback Read RF Blanking Enabled From File VI

Returns the RF blanking enabled value stored in the file. This VI uses the **waveform index** parameter as the key to retrieve the waveform property.

[IMAGE alt='icon' src='nirfsgplayback-read-rf-blanking-enabled-from-file-vi.png']

#### Inputs/Outputs

| file path — file path specifies the absolute path to the TDMS file from which the playback library reads the waveform. waveform index — waveform index specifies the waveform number in the file for which you want to read the RF blanking enabled value. error in — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. RF blanking enabled — RF blanking enabled returns the RF blanking enabled value stored in the file for the waveform number that you specified in the waveform index parameter. error out — error out contains error information. This output provides standard error out functionality. |
| --- |

Parent topic:

Utility

<!--NI_TOPIC bundle=rfsgplaybacklibrary-labview-api-ref path=instr-lib/nirfsgplayback/nirfsgplayback-read-rf-blanking-marker-locations-from-file-vi.html language=enus -->
## TOPIC 00014: niRFSGPlayback Read RF Blanking Marker Locations From File VI

- bundle_id: `rfsgplaybacklibrary-labview-api-ref`
- source_path: `instr-lib/nirfsgplayback/nirfsgplayback-read-rf-blanking-marker-locations-from-file-vi.html`
- source_url: https://docs-be.ni.com/bundle/rfsgplaybacklibrary-labview-api-ref/raw/resource/enus/instr-lib/nirfsgplayback/nirfsgplayback-read-rf-blanking-marker-locations-from-file-vi.html
- document_id: `rfsgplaybacklibrary-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the RF blanking marker locations stored in the file. This VI uses the waveform index as the key to retrieve the waveform property. icon Inputs/Outputs cpath.png file path file path specifies the absolute path to the TDMS file from which the playback library reads the waveform. ci32.png wavef

### niRFSGPlayback Read RF Blanking Marker Locations From File VI

Returns the RF blanking marker locations stored in the file. This VI uses the **waveform index** as the key to retrieve the waveform property.

[IMAGE alt='icon' src='nirfsgplayback-read-rf-blanking-marker-locations-from-file-vi.png']

#### Inputs/Outputs

| file path — file path specifies the absolute path to the TDMS file from which the playback library reads the waveform. waveform index — waveform index specifies the waveform number in the file for which you want to read the RF blanking marker locations. error in — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. RF blanking marker locations — RF blanking marker locations returns an array of the RF blanking marker location values stored in the file for the waveform number that you specified in the waveform index parameter. error out — error out contains error information. This output provides standard error out functionality. |
| --- |

Parent topic:

Obsolete

<!--NI_TOPIC bundle=rfsgplaybacklibrary-labview-api-ref path=instr-lib/nirfsgplayback/nirfsgplayback-read-rf-blanking-marker-source-from-file-vi.html language=enus -->
## TOPIC 00015: niRFSGPlayback Read RF Blanking Marker Source From File VI

- bundle_id: `rfsgplaybacklibrary-labview-api-ref`
- source_path: `instr-lib/nirfsgplayback/nirfsgplayback-read-rf-blanking-marker-source-from-file-vi.html`
- source_url: https://docs-be.ni.com/bundle/rfsgplaybacklibrary-labview-api-ref/raw/resource/enus/instr-lib/nirfsgplayback/nirfsgplayback-read-rf-blanking-marker-source-from-file-vi.html
- document_id: `rfsgplaybacklibrary-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the RF blanking marker source stored in the file. This VI uses the waveform index parameter as the key to retrieve the waveform property. icon Inputs/Outputs cpath.png file path file path specifies the absolute path to the TDMS file from which the playback library reads the waveform. ci32.pn

### niRFSGPlayback Read RF Blanking Marker Source From File VI

Returns the RF blanking marker source stored in the file. This VI uses the **waveform index** parameter as the key to retrieve the waveform property.

[IMAGE alt='icon' src='nirfsgplayback-read-rf-blanking-marker-source-from-file-vi.png']

#### Inputs/Outputs

| file path — file path specifies the absolute path to the TDMS file from which the playback library reads the waveform. waveform index — waveform index specifies the waveform number in the file for which you want to read the RF blanking marker source value. error in — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. RF blanking marker source — RF blanking marker source returns the RF blanking marker source value stored in the file for the waveform number that you specified in the waveform index parameter. error out — error out contains error information. This output provides standard error out functionality. |
| --- |

Parent topic:

Utility

<!--NI_TOPIC bundle=rfsgplaybacklibrary-labview-api-ref path=instr-lib/nirfsgplayback/nirfsgplayback-read-runtime-scaling-from-file-vi.html language=enus -->
## TOPIC 00016: niRFSGPlayback Read Runtime Scaling From File VI

- bundle_id: `rfsgplaybacklibrary-labview-api-ref`
- source_path: `instr-lib/nirfsgplayback/nirfsgplayback-read-runtime-scaling-from-file-vi.html`
- source_url: https://docs-be.ni.com/bundle/rfsgplaybacklibrary-labview-api-ref/raw/resource/enus/instr-lib/nirfsgplayback/nirfsgplayback-read-runtime-scaling-from-file-vi.html
- document_id: `rfsgplaybacklibrary-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the runtime scaling value stored in the file. This VI uses the waveform index parameter as the key to read the waveform property. icon Inputs/Outputs cpath.png file path file path specifies the absolute path to the TDMS file from which the playback library reads the waveform. ci32.png wavefo

### niRFSGPlayback Read Runtime Scaling From File VI

Returns the runtime scaling value stored in the file. This VI uses the **waveform index** parameter as the key to read the waveform property.

[IMAGE alt='icon' src='nirfsgplayback-read-runtime-scaling-from-file-vi.png']

#### Inputs/Outputs

| file path — file path specifies the absolute path to the TDMS file from which the playback library reads the waveform. waveform index — waveform index specifies the waveform number in the file for which you want to read the runtime scaling value. error in — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. runtime scaling — runtime scaling returns the runtime scaling value stored in the file for the waveform number that specified in the waveform index parameter. This value is expressed in dB. error out — error out contains error information. This output provides standard error out functionality. |
| --- |

Parent topic:

Utility

<!--NI_TOPIC bundle=rfsgplaybacklibrary-labview-api-ref path=instr-lib/nirfsgplayback/nirfsgplayback-read-sample-rate-from-file-vi.html language=enus -->
## TOPIC 00017: niRFSGPlayback Read Sample Rate From File VI

- bundle_id: `rfsgplaybacklibrary-labview-api-ref`
- source_path: `instr-lib/nirfsgplayback/nirfsgplayback-read-sample-rate-from-file-vi.html`
- source_url: https://docs-be.ni.com/bundle/rfsgplaybacklibrary-labview-api-ref/raw/resource/enus/instr-lib/nirfsgplayback/nirfsgplayback-read-sample-rate-from-file-vi.html
- document_id: `rfsgplaybacklibrary-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the sample rate stored in the file. This VI uses the waveform index as the key to retrieve the waveform property. icon Inputs/Outputs cpath.png file path file path specifies the absolute path to the TDMS file from which the playback library reads the waveform. ci32.png waveform index wavefor

### niRFSGPlayback Read Sample Rate From File VI

Returns the sample rate stored in the file. This VI uses the **waveform index** as the key to retrieve the waveform property.

[IMAGE alt='icon' src='nirfsgplayback-read-sample-rate-from-file-vi.png']

#### Inputs/Outputs

| file path — file path specifies the absolute path to the TDMS file from which the playback library reads the waveform. waveform index — waveform index specifies the waveform number in the file for which you want to read the sample rate. error in — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. sample rate — sample rate returns the sample rate value stored in the file for the waveform number that you specified in the waveform index parameter. error out — error out contains error information. This output provides standard error out functionality. |
| --- |

Parent topic:

Utility

<!--NI_TOPIC bundle=rfsgplaybacklibrary-labview-api-ref path=instr-lib/nirfsgplayback/nirfsgplayback-read-signal-bandwidth-from-file-vi.html language=enus -->
## TOPIC 00018: niRFSGPlayback Read Signal Bandwidth From File VI

- bundle_id: `rfsgplaybacklibrary-labview-api-ref`
- source_path: `instr-lib/nirfsgplayback/nirfsgplayback-read-signal-bandwidth-from-file-vi.html`
- source_url: https://docs-be.ni.com/bundle/rfsgplaybacklibrary-labview-api-ref/raw/resource/enus/instr-lib/nirfsgplayback/nirfsgplayback-read-signal-bandwidth-from-file-vi.html
- document_id: `rfsgplaybacklibrary-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the signal bandwidth stored in the file. This VI uses the waveform index parameter as the key to retrieve the waveform property. icon Inputs/Outputs cpath.png file path file path specifies the absolute path to the TDMS file from which the playback library reads the waveform. ci32.png wavefor

### niRFSGPlayback Read Signal Bandwidth From File VI

Returns the signal bandwidth stored in the file. This VI uses the **waveform index** parameter as the key to retrieve the waveform property.

[IMAGE alt='icon' src='nirfsgplayback-read-signal-bandwidth-from-file-vi.png']

#### Inputs/Outputs

| file path — file path specifies the absolute path to the TDMS file from which the playback library reads the waveform. waveform index — waveform index specifies the waveform number in the file for which you want to read the signal bandwidth. error in — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. signal bandwidth — signal bandwidth returns the signal bandwidth stored in the file for the waveform number that you specified in the waveform index parameter. error out — error out contains error information. This output provides standard error out functionality. |
| --- |

Parent topic:

Utility

<!--NI_TOPIC bundle=rfsgplaybacklibrary-labview-api-ref path=instr-lib/nirfsgplayback/nirfsgplayback-read-waveform-file-version-from-file-vi.html language=enus -->
## TOPIC 00019: niRFSGPlayback Read Waveform File Version From File VI

- bundle_id: `rfsgplaybacklibrary-labview-api-ref`
- source_path: `instr-lib/nirfsgplayback/nirfsgplayback-read-waveform-file-version-from-file-vi.html`
- source_url: https://docs-be.ni.com/bundle/rfsgplaybacklibrary-labview-api-ref/raw/resource/enus/instr-lib/nirfsgplayback/nirfsgplayback-read-waveform-file-version-from-file-vi.html
- document_id: `rfsgplaybacklibrary-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the waveform file version of the waveform stored in the file. icon Inputs/Outputs cpath.png file path file path specifies the absolute path to the TDMS file from which the playback library reads the waveforms. cerrcodeclst.png error in error in describes error conditions that occur before th

### niRFSGPlayback Read Waveform File Version From File VI

Returns the waveform file version of the waveform stored in the file.

[IMAGE alt='icon' src='nirfsgplayback-read-waveform-file-version-from-file-vi.png']

#### Inputs/Outputs

| file path — file path specifies the absolute path to the TDMS file from which the playback library reads the waveforms. error in — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. waveform file version — waveform file version returns the waveform file version of the waveform stored in the NI-RFSG waveform database for the waveform you specified in the waveform name parameter. error out — error out contains error information. This output provides standard error out functionality. |
| --- |

Parent topic:

Utility

<!--NI_TOPIC bundle=rfsgplaybacklibrary-labview-api-ref path=instr-lib/nirfsgplayback/nirfsgplayback-read-waveform-from-file-1-wfm-tdms-cdb-vi.html language=enus -->
## TOPIC 00020: niRFSGPlayback Read Waveform From File (1 Wfm,TDMS, CDB) VI

- bundle_id: `rfsgplaybacklibrary-labview-api-ref`
- source_path: `instr-lib/nirfsgplayback/nirfsgplayback-read-waveform-from-file-1-wfm-tdms-cdb-vi.html`
- source_url: https://docs-be.ni.com/bundle/rfsgplaybacklibrary-labview-api-ref/raw/resource/enus/instr-lib/nirfsgplayback/nirfsgplayback-read-waveform-from-file-1-wfm-tdms-cdb-vi.html
- document_id: `rfsgplaybacklibrary-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Reads the waveform from the file and returns the waveform in the waveform parameter. icon Inputs/Outputs cpath.png file path file path specifies the absolute path to the TDMS file from which the playback library reads the waveforms. ci32.png waveform index waveform index specifies the index of the w

### niRFSGPlayback Read Waveform From File (1 Wfm,TDMS, CDB) VI

Reads the waveform from the file and returns the waveform in the **waveform** parameter.

[IMAGE alt='icon' src='nirfsgplayback-read-waveform-from-file-1-wfm-tdms-cdb-vi.png']

#### Inputs/Outputs

| file path — file path specifies the absolute path to the TDMS file from which the playback library reads the waveforms. waveform index — waveform index specifies the index of the waveform that you want to read from the TDMS file. error in — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. waveform — waveform returns the data for a complex waveform, including the start, delta, and actual values. t0 — t0 this element should be ignored. dt — dt returns the inverse of the waveform sample rate. y — y returns the array of complex waveform samples. error out — error out contains error information. This output provides standard error out functionality. |
| --- |
| t0 — t0 this element should be ignored. dt — dt returns the inverse of the waveform sample rate. y — y returns the array of complex waveform samples. |

Parent topic:

niRFSGPlayback Read Waveform From File VI

<!--NI_TOPIC bundle=rfsgplaybacklibrary-labview-api-ref path=instr-lib/nirfsgplayback/nirfsgplayback-read-waveform-from-file-1-wfm-tdms-csg-vi.html language=enus -->
## TOPIC 00021: niRFSGPlayback Read Waveform From File (1 Wfm,TDMS, CSG) VI

- bundle_id: `rfsgplaybacklibrary-labview-api-ref`
- source_path: `instr-lib/nirfsgplayback/nirfsgplayback-read-waveform-from-file-1-wfm-tdms-csg-vi.html`
- source_url: https://docs-be.ni.com/bundle/rfsgplaybacklibrary-labview-api-ref/raw/resource/enus/instr-lib/nirfsgplayback/nirfsgplayback-read-waveform-from-file-1-wfm-tdms-csg-vi.html
- document_id: `rfsgplaybacklibrary-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Reads the waveform from file and returns the waveform in the waveform parameter. icon Inputs/Outputs cpath.png file path file path specifies the absolute path to the TDMS file from which the playback library reads the waveforms. ci32.png waveform index waveform index specifies the index of the wavef

### niRFSGPlayback Read Waveform From File (1 Wfm,TDMS, CSG) VI

Reads the waveform from file and returns the waveform in the **waveform** parameter.

[IMAGE alt='icon' src='nirfsgplayback-read-waveform-from-file-1-wfm-tdms-csg-vi.png']

#### Inputs/Outputs

| file path — file path specifies the absolute path to the TDMS file from which the playback library reads the waveforms. waveform index — waveform index specifies the index of the waveform that you want to read from the TDMS file. error in — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. waveform — waveform returns the data for a complex waveform, including the start, delta, and actual values. t0 — t0 this element should be ignored. dt — dt returns the inverse of the waveform sample rate. y — y returns the array of complex waveform samples. error out — error out contains error information. This output provides standard error out functionality. |
| --- |
| t0 — t0 this element should be ignored. dt — dt returns the inverse of the waveform sample rate. y — y returns the array of complex waveform samples. |

Parent topic:

niRFSGPlayback Read Waveform From File VI

<!--NI_TOPIC bundle=rfsgplaybacklibrary-labview-api-ref path=instr-lib/nirfsgplayback/nirfsgplayback-read-waveform-from-file-n-wfms-tdms-cdb-vi.html language=enus -->
## TOPIC 00022: niRFSGPlayback Read Waveform From File (N Wfms,TDMS, CDB) VI

- bundle_id: `rfsgplaybacklibrary-labview-api-ref`
- source_path: `instr-lib/nirfsgplayback/nirfsgplayback-read-waveform-from-file-n-wfms-tdms-cdb-vi.html`
- source_url: https://docs-be.ni.com/bundle/rfsgplaybacklibrary-labview-api-ref/raw/resource/enus/instr-lib/nirfsgplayback/nirfsgplayback-read-waveform-from-file-n-wfms-tdms-cdb-vi.html
- document_id: `rfsgplaybacklibrary-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Reads the waveforms from file and returns the waveforms in the waveforms parameter. icon Inputs/Outputs cpath.png file path file path specifies the absolute path to the TDMS file from which the playback library reads the waveforms. cerrcodeclst.png error in error in describes error conditions that o

### niRFSGPlayback Read Waveform From File (N Wfms,TDMS, CDB) VI

Reads the waveforms from file and returns the waveforms in the **waveforms** parameter.

[IMAGE alt='icon' src='nirfsgplayback-read-waveform-from-file-n-wfms-tdms-cdb-vi.png']

#### Inputs/Outputs

| file path — file path specifies the absolute path to the TDMS file from which the playback library reads the waveforms. error in — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. waveforms — waveforms returns the array of complex waveforms read from the file. t0 — t0 this element should be ignored. dt — dt returns the inverse of the waveform sample rate. y — y returns the array of complex waveform samples. error out — error out contains error information. This output provides standard error out functionality. |
| --- |
| t0 — t0 this element should be ignored. dt — dt returns the inverse of the waveform sample rate. y — y returns the array of complex waveform samples. |

Parent topic:

niRFSGPlayback Read Waveform From File VI

<!--NI_TOPIC bundle=rfsgplaybacklibrary-labview-api-ref path=instr-lib/nirfsgplayback/nirfsgplayback-read-waveform-from-file-n-wfms-tdms-csg-vi.html language=enus -->
## TOPIC 00023: niRFSGPlayback Read Waveform From File (N Wfms,TDMS, CSG) VI

- bundle_id: `rfsgplaybacklibrary-labview-api-ref`
- source_path: `instr-lib/nirfsgplayback/nirfsgplayback-read-waveform-from-file-n-wfms-tdms-csg-vi.html`
- source_url: https://docs-be.ni.com/bundle/rfsgplaybacklibrary-labview-api-ref/raw/resource/enus/instr-lib/nirfsgplayback/nirfsgplayback-read-waveform-from-file-n-wfms-tdms-csg-vi.html
- document_id: `rfsgplaybacklibrary-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Reads the waveforms from the file and returns the waveforms in the waveforms parameter. icon Inputs/Outputs cpath.png file path file path specifies the absolute path to the TDMS file from which the playback library reads the waveforms. cerrcodeclst.png error in error in describes error conditions th

### niRFSGPlayback Read Waveform From File (N Wfms,TDMS, CSG) VI

Reads the waveforms from the file and returns the waveforms in the **waveforms** parameter.

[IMAGE alt='icon' src='nirfsgplayback-read-waveform-from-file-n-wfms-tdms-csg-vi.png']

#### Inputs/Outputs

| file path — file path specifies the absolute path to the TDMS file from which the playback library reads the waveforms. error in — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. waveforms — waveforms returns the array of complex waveforms read from the file. t0 — t0 this element should be ignored. dt — dt returns the inverse of the waveform sample rate. y — y returns the array of complex waveform samples. error out — error out contains error information. This output provides standard error out functionality. |
| --- |
| t0 — t0 this element should be ignored. dt — dt returns the inverse of the waveform sample rate. y — y returns the array of complex waveform samples. |

Parent topic:

niRFSGPlayback Read Waveform From File VI

<!--NI_TOPIC bundle=rfsgplaybacklibrary-labview-api-ref path=instr-lib/nirfsgplayback/nirfsgplayback-read-waveform-from-file-vi.html language=enus -->
## TOPIC 00024: niRFSGPlayback Read Waveform From File VI

- bundle_id: `rfsgplaybacklibrary-labview-api-ref`
- source_path: `instr-lib/nirfsgplayback/nirfsgplayback-read-waveform-from-file-vi.html`
- source_url: https://docs-be.ni.com/bundle/rfsgplaybacklibrary-labview-api-ref/raw/resource/enus/instr-lib/nirfsgplayback/nirfsgplayback-read-waveform-from-file-vi.html
- document_id: `rfsgplaybacklibrary-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the waveform stored in the technical data management streaming (TDMS) file. icon

### niRFSGPlayback Read Waveform From File VI

Returns the waveform stored in the technical data management streaming (TDMS) file.

[IMAGE alt='icon' src='nirfsgplayback-read-waveform-from-file-vi.png']

- [niRFSGPlayback Read Waveform From File (1 Wfm,TDMS, CSG) VI](../../instr-lib/nirfsgplayback/nirfsgplayback-read-waveform-from-file-1-wfm-tdms-csg-vi.html) Reads the waveform from file and returns the waveform in the waveform parameter.
- [niRFSGPlayback Read Waveform From File (1 Wfm,TDMS, CDB) VI](../../instr-lib/nirfsgplayback/nirfsgplayback-read-waveform-from-file-1-wfm-tdms-cdb-vi.html) Reads the waveform from the file and returns the waveform in the waveform parameter.
- [niRFSGPlayback Read Waveform From File (N Wfms,TDMS, CSG) VI](../../instr-lib/nirfsgplayback/nirfsgplayback-read-waveform-from-file-n-wfms-tdms-csg-vi.html) Reads the waveforms from the file and returns the waveforms in the waveforms parameter.
- [niRFSGPlayback Read Waveform From File (N Wfms,TDMS, CDB) VI](../../instr-lib/nirfsgplayback/nirfsgplayback-read-waveform-from-file-n-wfms-tdms-cdb-vi.html) Reads the waveforms from file and returns the waveforms in the waveforms parameter.

Parent topic:

NI-RFSG Playback Library

<!--NI_TOPIC bundle=rfsgplaybacklibrary-labview-api-ref path=instr-lib/nirfsgplayback/nirfsgplayback-read-waveform-size-from-file-vi.html language=enus -->
## TOPIC 00025: niRFSGPlayback Read Waveform Size From File VI

- bundle_id: `rfsgplaybacklibrary-labview-api-ref`
- source_path: `instr-lib/nirfsgplayback/nirfsgplayback-read-waveform-size-from-file-vi.html`
- source_url: https://docs-be.ni.com/bundle/rfsgplaybacklibrary-labview-api-ref/raw/resource/enus/instr-lib/nirfsgplayback/nirfsgplayback-read-waveform-size-from-file-vi.html
- document_id: `rfsgplaybacklibrary-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the size of the waveform stored in the file. This VI uses the waveform index parameter as the key to retrieve the waveform property. icon Inputs/Outputs cpath.png file path file path specifies the absolute path to the TDMS file from which the playback library reads the waveform. ci32.png wav

### niRFSGPlayback Read Waveform Size From File VI

Returns the size of the waveform stored in the file. This VI uses the **waveform index** parameter as the key to retrieve the waveform property.

[IMAGE alt='icon' src='nirfsgplayback-read-waveform-size-from-file-vi.png']

#### Inputs/Outputs

| file path — file path specifies the absolute path to the TDMS file from which the playback library reads the waveform. waveform index — waveform index specifies the waveform number in the file for which you want to read the waveform size. error in — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. waveform size — waveform size returns the size of the waveform stored in the file for the waveform number that you specified in the waveform index parameter. This value is expressed in samples. error out — error out contains error information. This output provides standard error out functionality. |
| --- |

Parent topic:

Utility

<!--NI_TOPIC bundle=rfsgplaybacklibrary-labview-api-ref path=instr-lib/nirfsgplayback/nirfsgplayback-retrieve-automatic-sg-sa-shared-lo-vi.html language=enus -->
## TOPIC 00026: niRFSGPlayback Retrieve Automatic SG SA Shared LO VI

- bundle_id: `rfsgplaybacklibrary-labview-api-ref`
- source_path: `instr-lib/nirfsgplayback/nirfsgplayback-retrieve-automatic-sg-sa-shared-lo-vi.html`
- source_url: https://docs-be.ni.com/bundle/rfsgplaybacklibrary-labview-api-ref/raw/resource/enus/instr-lib/nirfsgplayback/nirfsgplayback-retrieve-automatic-sg-sa-shared-lo-vi.html
- document_id: `rfsgplaybacklibrary-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the value of automatic SG SA shared LO parameter. icon Inputs/Outputs civrn.png instrument handle in instrument handle in identifies the instrument session. instrument handle in is obtained from either the niRFSG Initialize VI or the niRFSG Initialize With Options VI. cstr.png channel name c

### niRFSGPlayback Retrieve Automatic SG SA Shared LO VI

Returns the value of **automatic SG SA shared LO** parameter.

[IMAGE alt='icon' src='nirfsgplayback-retrieve-automatic-sg-sa-shared-lo-vi.png']

#### Inputs/Outputs

| instrument handle in — instrument handle in identifies the instrument session. instrument handle in is obtained from either the niRFSG Initialize VI or the niRFSG Initialize With Options VI. channel name — channel name this parameter is reserved for future use. error in — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. instrument handle out — instrument handle out passes a reference from the instrument session to the next VI. SG SA Shared LO Enabled — automatic SG SA shared LO returns the access control of NI-RFSG LO Out Export. error out — error out contains error information. This output provides standard error out functionality. |
| --- |

Parent topic:

Advanced

<!--NI_TOPIC bundle=rfsgplaybacklibrary-labview-api-ref path=instr-lib/nirfsgplayback/nirfsgplayback-retrieve-downloaded-waveform-names-vi.html language=enus -->
## TOPIC 00027: niRFSGPlayback Retrieve Downloaded Waveform Names VI

- bundle_id: `rfsgplaybacklibrary-labview-api-ref`
- source_path: `instr-lib/nirfsgplayback/nirfsgplayback-retrieve-downloaded-waveform-names-vi.html`
- source_url: https://docs-be.ni.com/bundle/rfsgplaybacklibrary-labview-api-ref/raw/resource/enus/instr-lib/nirfsgplayback/nirfsgplayback-retrieve-downloaded-waveform-names-vi.html
- document_id: `rfsgplaybacklibrary-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the names of the waveforms that are stored in the NI-RFSG waveform database. icon Inputs/Outputs civrn.png instrument handle in instrument handle in identifies the instrument session. instrument handle in is obtained from either the niRFSG Initialize VI or the niRFSG Initialize With Options

### niRFSGPlayback Retrieve Downloaded Waveform Names VI

Returns the names of the waveforms that are stored in the NI-RFSG waveform database.

[IMAGE alt='icon' src='nirfsgplayback-retrieve-downloaded-waveform-names-vi.png']

#### Inputs/Outputs

| instrument handle in — instrument handle in identifies the instrument session. instrument handle in is obtained from either the niRFSG Initialize VI or the niRFSG Initialize With Options VI. error in — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. instrument handle out — instrument handle out passes a reference from the instrument session to the next VI. waveform names — waveform names returns an array of the name of the waveforms that are stored in the NI-RFSG waveform database. error out — error out contains error information. This output provides standard error out functionality. |
| --- |

Parent topic:

Advanced

<!--NI_TOPIC bundle=rfsgplaybacklibrary-labview-api-ref path=instr-lib/nirfsgplayback/nirfsgplayback-retrieve-waveform-burst-start-locations-vi.html language=enus -->
## TOPIC 00028: niRFSGPlayback Retrieve Waveform Burst Start Locations VI

- bundle_id: `rfsgplaybacklibrary-labview-api-ref`
- source_path: `instr-lib/nirfsgplayback/nirfsgplayback-retrieve-waveform-burst-start-locations-vi.html`
- source_url: https://docs-be.ni.com/bundle/rfsgplaybacklibrary-labview-api-ref/raw/resource/enus/instr-lib/nirfsgplayback/nirfsgplayback-retrieve-waveform-burst-start-locations-vi.html
- document_id: `rfsgplaybacklibrary-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the burst start locations stored in the NI-RFSG waveform database. This VI uses the waveform name as the key to retrieve the waveform property. icon Inputs/Outputs civrn.png instrument handle in instrument handle in identifies the instrument session. instrument handle in is obtained from eit

### niRFSGPlayback Retrieve Waveform Burst Start Locations VI

Returns the burst start locations stored in the NI-RFSG waveform database. This VI uses the **waveform name** as the key to retrieve the waveform property.

[IMAGE alt='icon' src='nirfsgplayback-retrieve-waveform-burst-start-locations-vi.png']

#### Inputs/Outputs

| instrument handle in — instrument handle in identifies the instrument session. instrument handle in is obtained from either the niRFSG Initialize VI or the niRFSG Initialize With Options VI. waveform name — waveform name specifies the name of the waveform for which you want to retrieve the burst start locations. error in — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. instrument handle out — instrument handle out passes a reference from the instrument session to the next VI. burst start locations — burst start locations returns the burst start locations stored in the NI-RFSG waveform database for the waveform you specified in the waveform name parameter. error out — error out contains error information. This output provides standard error out functionality. |
| --- |

Parent topic:

Advanced

<!--NI_TOPIC bundle=rfsgplaybacklibrary-labview-api-ref path=instr-lib/nirfsgplayback/nirfsgplayback-retrieve-waveform-burst-stop-locations-vi.html language=enus -->
## TOPIC 00029: niRFSGPlayback Retrieve Waveform Burst Stop Locations VI

- bundle_id: `rfsgplaybacklibrary-labview-api-ref`
- source_path: `instr-lib/nirfsgplayback/nirfsgplayback-retrieve-waveform-burst-stop-locations-vi.html`
- source_url: https://docs-be.ni.com/bundle/rfsgplaybacklibrary-labview-api-ref/raw/resource/enus/instr-lib/nirfsgplayback/nirfsgplayback-retrieve-waveform-burst-stop-locations-vi.html
- document_id: `rfsgplaybacklibrary-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the burst stop locations stored in the NI-RFSG waveform database. This VI uses the waveform name parameter as the key to retrieve the waveform property. icon Inputs/Outputs civrn.png instrument handle in instrument handle in identifies the instrument session. instrument handle in is obtained

### niRFSGPlayback Retrieve Waveform Burst Stop Locations VI

Returns the burst stop locations stored in the NI-RFSG waveform database. This VI uses the **waveform name** parameter as the key to retrieve the waveform property.

[IMAGE alt='icon' src='nirfsgplayback-retrieve-waveform-burst-stop-locations-vi.png']

#### Inputs/Outputs

| instrument handle in — instrument handle in identifies the instrument session. instrument handle in is obtained from either the niRFSG Initialize VI or the niRFSG Initialize With Options VI. waveform name — waveform name specifies the name of the waveform for which you want to retrieve the burst stop locations. error in — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. instrument handle out — instrument handle out passes a reference from the instrument session to the next VI. burst stop locations — burst stop locations returns the burst stop locations stored in the NI-RFSG waveform database for the waveform you specified in the waveform name parameter. error out — error out contains error information. This output provides standard error out functionality. |
| --- |

Parent topic:

Advanced

<!--NI_TOPIC bundle=rfsgplaybacklibrary-labview-api-ref path=instr-lib/nirfsgplayback/nirfsgplayback-retrieve-waveform-file-version-vi.html language=enus -->
## TOPIC 00030: niRFSGPlayback Retrieve Waveform File Version VI

- bundle_id: `rfsgplaybacklibrary-labview-api-ref`
- source_path: `instr-lib/nirfsgplayback/nirfsgplayback-retrieve-waveform-file-version-vi.html`
- source_url: https://docs-be.ni.com/bundle/rfsgplaybacklibrary-labview-api-ref/raw/resource/enus/instr-lib/nirfsgplayback/nirfsgplayback-retrieve-waveform-file-version-vi.html
- document_id: `rfsgplaybacklibrary-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the waveform file version of the waveform stored in the NI-RFSG waveform database. This VI uses the waveform name parameter as the key to retrieve the waveform property. icon Inputs/Outputs civrn.png instrument handle in instrument handle in identifies the instrument session. instrument hand

### niRFSGPlayback Retrieve Waveform File Version VI

Returns the waveform file version of the waveform stored in the NI-RFSG waveform database. This VI uses the **waveform name** parameter as the key to retrieve the waveform property.

[IMAGE alt='icon' src='nirfsgplayback-retrieve-waveform-file-version-vi.png']

#### Inputs/Outputs

| instrument handle in — instrument handle in identifies the instrument session. instrument handle in is obtained from either the niRFSG Initialize VI or the niRFSG Initialize With Options VI. waveform name — waveform name specifies the name of the waveform for which you want to retrieve the waveform file version. error in — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. instrument handle out — instrument handle out passes a reference from the instrument session to the next VI. waveform file version — waveform file version returns the waveform file version of the waveform stored in the NI-RFSG waveform database for the waveform you specified in the waveform name parameter. error out — error out contains error information. This output provides standard error out functionality. |
| --- |

Parent topic:

Advanced

<!--NI_TOPIC bundle=rfsgplaybacklibrary-labview-api-ref path=instr-lib/nirfsgplayback/nirfsgplayback-retrieve-waveform-lo-offset-mode-vi.html language=enus -->
## TOPIC 00031: niRFSGPlayback Retrieve Waveform LO Offset Mode VI

- bundle_id: `rfsgplaybacklibrary-labview-api-ref`
- source_path: `instr-lib/nirfsgplayback/nirfsgplayback-retrieve-waveform-lo-offset-mode-vi.html`
- source_url: https://docs-be.ni.com/bundle/rfsgplaybacklibrary-labview-api-ref/raw/resource/enus/instr-lib/nirfsgplayback/nirfsgplayback-retrieve-waveform-lo-offset-mode-vi.html
- document_id: `rfsgplaybacklibrary-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the LO offset mode value stored in the NI-RFSG waveform database. This VI uses the waveform name parameter as the key to retrieve the waveform property. icon Inputs/Outputs civrn.png instrument handle in instrument handle in identifies the instrument session. instrument handle in is obtained

### niRFSGPlayback Retrieve Waveform LO Offset Mode VI

Returns the LO offset mode value stored in the NI-RFSG waveform database. This VI uses the **waveform name** parameter as the key to retrieve the waveform property.

[IMAGE alt='icon' src='nirfsgplayback-retrieve-waveform-lo-offset-mode-vi.png']

#### Inputs/Outputs

| instrument handle in — instrument handle in identifies the instrument session. instrument handle in is obtained from either the niRFSG Initialize VI or the niRFSG Initialize With Options VI. waveform name — waveform name specifies the name of the waveform for which you want to retrieve the waveform LO offset mode value. error in — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. instrument handle out — instrument handle out passes a reference from the instrument session to the next VI. LO offset mode — LO offset mode returns the LO offset mode value stored in the NI-RFSG waveform database for the waveform that you specified in the waveform name parameter. error out — error out contains error information. This output provides standard error out functionality. |
| --- |

Parent topic:

Advanced

<!--NI_TOPIC bundle=rfsgplaybacklibrary-labview-api-ref path=instr-lib/nirfsgplayback/nirfsgplayback-retrieve-waveform-papr-vi.html language=enus -->
## TOPIC 00032: niRFSGPlayback Retrieve Waveform PAPR VI

- bundle_id: `rfsgplaybacklibrary-labview-api-ref`
- source_path: `instr-lib/nirfsgplayback/nirfsgplayback-retrieve-waveform-papr-vi.html`
- source_url: https://docs-be.ni.com/bundle/rfsgplaybacklibrary-labview-api-ref/raw/resource/enus/instr-lib/nirfsgplayback/nirfsgplayback-retrieve-waveform-papr-vi.html
- document_id: `rfsgplaybacklibrary-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the peak to average power ratio (PAPR) stored in the NI-RFSG waveform database. This VI uses the waveform name parameter as the key to retrieve the waveform property. icon Inputs/Outputs civrn.png instrument handle in instrument handle in identifies the instrument session. instrument handle

### niRFSGPlayback Retrieve Waveform PAPR VI

Returns the peak to average power ratio (PAPR) stored in the NI-RFSG waveform database. This VI uses the **waveform name** parameter as the key to retrieve the waveform property.

[IMAGE alt='icon' src='nirfsgplayback-retrieve-waveform-papr-vi.png']

#### Inputs/Outputs

| instrument handle in — instrument handle in identifies the instrument session. instrument handle in is obtained from either the niRFSG Initialize VI or the niRFSG Initialize With Options VI. waveform name — waveform name specifies the name of the waveform for which you want to retrieve the PAPR. error in — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. instrument handle out — instrument handle out passes a reference from the instrument session to the next VI. PAPR — PAPR returns the PAPR stored in the NI-RFSG database, for the waveform you specified in the waveform name parameter. This value is expressed in dB. error out — error out contains error information. This output provides standard error out functionality. |
| --- |

Parent topic:

Advanced

<!--NI_TOPIC bundle=rfsgplaybacklibrary-labview-api-ref path=instr-lib/nirfsgplayback/nirfsgplayback-retrieve-waveform-peak-power-adjustment-vi.html language=enus -->
## TOPIC 00033: niRFSGPlayback Retrieve Waveform Peak Power Adjustment VI

- bundle_id: `rfsgplaybacklibrary-labview-api-ref`
- source_path: `instr-lib/nirfsgplayback/nirfsgplayback-retrieve-waveform-peak-power-adjustment-vi.html`
- source_url: https://docs-be.ni.com/bundle/rfsgplaybacklibrary-labview-api-ref/raw/resource/enus/instr-lib/nirfsgplayback/nirfsgplayback-retrieve-waveform-peak-power-adjustment-vi.html
- document_id: `rfsgplaybacklibrary-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the peak power adjustment stored in the NI-RFSG waveform database. This VI uses the waveform name as the key to retrieve the waveform property. icon Inputs/Outputs civrn.png instrument handle in instrument handle in identifies the instrument session. instrument handle in is obtained from eit

### niRFSGPlayback Retrieve Waveform Peak Power Adjustment VI

Returns the peak power adjustment stored in the NI-RFSG waveform database. This VI uses the **waveform name** as the key to retrieve the waveform property.

[IMAGE alt='icon' src='nirfsgplayback-retrieve-waveform-peak-power-adjustment-vi.png']

#### Inputs/Outputs

| instrument handle in — instrument handle in identifies the instrument session. instrument handle in is obtained from either the niRFSG Initialize VI or the niRFSG Initialize With Options VI. waveform name — waveform name specifies the name of the waveform for which you want to retrieve the peak power adjustment value. error in — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. instrument handle out — instrument handle out passes a reference from the instrument session to the next VI. peak power adjustment — peak power adjustment returns the Peak Power Adjustment property value stored in the NI-RFSG waveform database for the waveform you specified in the waveform name parameter. error out — error out contains error information. This output provides standard error out functionality. |
| --- |

Parent topic:

Obsolete

<!--NI_TOPIC bundle=rfsgplaybacklibrary-labview-api-ref path=instr-lib/nirfsgplayback/nirfsgplayback-retrieve-waveform-rf-blanking-enabled-vi.html language=enus -->
## TOPIC 00034: niRFSGPlayback Retrieve Waveform RF Blanking Enabled VI

- bundle_id: `rfsgplaybacklibrary-labview-api-ref`
- source_path: `instr-lib/nirfsgplayback/nirfsgplayback-retrieve-waveform-rf-blanking-enabled-vi.html`
- source_url: https://docs-be.ni.com/bundle/rfsgplaybacklibrary-labview-api-ref/raw/resource/enus/instr-lib/nirfsgplayback/nirfsgplayback-retrieve-waveform-rf-blanking-enabled-vi.html
- document_id: `rfsgplaybacklibrary-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the RF blanking enabled value stored in the NI-RFSG waveform database. The VI uses the waveform name parameter as the key to retrieve the waveform property. icon Inputs/Outputs civrn.png instrument handle in instrument handle in identifies the instrument session. instrument handle in is obta

### niRFSGPlayback Retrieve Waveform RF Blanking Enabled VI

Returns the RF blanking enabled value stored in the NI-RFSG waveform database. The VI uses the **waveform name** parameter as the key to retrieve the waveform property.

[IMAGE alt='icon' src='nirfsgplayback-retrieve-waveform-rf-blanking-enabled-vi.png']

#### Inputs/Outputs

| instrument handle in — instrument handle in identifies the instrument session. instrument handle in is obtained from either the niRFSG Initialize VI or the niRFSG Initialize With Options VI. waveform name — waveform name specifies the name of the waveform for which you want to retrieve the RF blanking enabled value. error in — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. instrument handle out — instrument handle out passes a reference from the instrument session to the next VI. RF blanking enabled — RF blanking enabled returns the RF blanking enabled value stored in the NI-RFSG waveform database for the waveform you specified in the waveform name parameter. error out — error out contains error information. This output provides standard error out functionality. |
| --- |

Parent topic:

Advanced

<!--NI_TOPIC bundle=rfsgplaybacklibrary-labview-api-ref path=instr-lib/nirfsgplayback/nirfsgplayback-retrieve-waveform-rf-blanking-marker-locations-vi.html language=enus -->
## TOPIC 00035: niRFSGPlayback Retrieve Waveform RF Blanking Marker Locations VI

- bundle_id: `rfsgplaybacklibrary-labview-api-ref`
- source_path: `instr-lib/nirfsgplayback/nirfsgplayback-retrieve-waveform-rf-blanking-marker-locations-vi.html`
- source_url: https://docs-be.ni.com/bundle/rfsgplaybacklibrary-labview-api-ref/raw/resource/enus/instr-lib/nirfsgplayback/nirfsgplayback-retrieve-waveform-rf-blanking-marker-locations-vi.html
- document_id: `rfsgplaybacklibrary-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the RF blanking marker positions stored in the NI-RFSG waveform database. This VI uses the waveform name as the key to retrieve the waveform property. icon Inputs/Outputs civrn.png instrument handle in instrument handle in identifies the instrument session. instrument handle in is obtained f

### niRFSGPlayback Retrieve Waveform RF Blanking Marker Locations VI

Returns the RF blanking marker positions stored in the NI-RFSG waveform database. This VI uses the **waveform name** as the key to retrieve the waveform property.

[IMAGE alt='icon' src='nirfsgplayback-retrieve-waveform-rf-blanking-marker-locations-vi.png']

#### Inputs/Outputs

| instrument handle in — instrument handle in identifies the instrument session. instrument handle in is obtained from either the niRFSG Initialize VI or the niRFSG Initialize With Options VI. waveform name — waveform name specifies the name of the waveform for which you want to retrieve the RF blanking marker locations. error in — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. instrument handle out — instrument handle out passes a reference from the instrument session to the next VI. RF blanking marker locations — RF blanking marker locations returns the array of RF blanking marker positions stored in the NI-RFSG waveform database for the waveform you specified in the waveform name parameter. error out — error out contains error information. This output provides standard error out functionality. |
| --- |

Parent topic:

Obsolete

<!--NI_TOPIC bundle=rfsgplaybacklibrary-labview-api-ref path=instr-lib/nirfsgplayback/nirfsgplayback-retrieve-waveform-rf-blanking-marker-source-vi.html language=enus -->
## TOPIC 00036: niRFSGPlayback Retrieve Waveform RF Blanking Marker Source VI

- bundle_id: `rfsgplaybacklibrary-labview-api-ref`
- source_path: `instr-lib/nirfsgplayback/nirfsgplayback-retrieve-waveform-rf-blanking-marker-source-vi.html`
- source_url: https://docs-be.ni.com/bundle/rfsgplaybacklibrary-labview-api-ref/raw/resource/enus/instr-lib/nirfsgplayback/nirfsgplayback-retrieve-waveform-rf-blanking-marker-source-vi.html
- document_id: `rfsgplaybacklibrary-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the RF blanking marker source stored in the NI-RFSG waveform database. This VI uses the waveform name as the key to retrieve the waveform property. icon Inputs/Outputs civrn.png instrument handle in instrument handle in identifies the instrument session. instrument handle in is obtained from

### niRFSGPlayback Retrieve Waveform RF Blanking Marker Source VI

Returns the RF blanking marker source stored in the NI-RFSG waveform database. This VI uses the **waveform name** as the key to retrieve the waveform property.

[IMAGE alt='icon' src='nirfsgplayback-retrieve-waveform-rf-blanking-marker-source-vi.png']

#### Inputs/Outputs

| instrument handle in — instrument handle in identifies the instrument session. instrument handle in is obtained from either the niRFSG Initialize VI or the niRFSG Initialize With Options VI. waveform name — waveform name specifies the name of the waveform for which you want to retrieve the RF blanking marker source value. error in — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. instrument handle out — instrument handle out passes a reference from the instrument session to the next VI. RF blanking marker source — RF blanking marker source returns the RF blanking marker source stored in the NI-RFSG waveform database for the waveform you specified in the waveform name parameter. error out — error out contains error information. This output provides standard error out functionality. |
| --- |

Parent topic:

Advanced

<!--NI_TOPIC bundle=rfsgplaybacklibrary-labview-api-ref path=instr-lib/nirfsgplayback/nirfsgplayback-retrieve-waveform-runtime-scaling-vi.html language=enus -->
## TOPIC 00037: niRFSGPlayback Retrieve Waveform Runtime Scaling VI

- bundle_id: `rfsgplaybacklibrary-labview-api-ref`
- source_path: `instr-lib/nirfsgplayback/nirfsgplayback-retrieve-waveform-runtime-scaling-vi.html`
- source_url: https://docs-be.ni.com/bundle/rfsgplaybacklibrary-labview-api-ref/raw/resource/enus/instr-lib/nirfsgplayback/nirfsgplayback-retrieve-waveform-runtime-scaling-vi.html
- document_id: `rfsgplaybacklibrary-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the runtime scaling value stored in the NI-RFSG waveform database. This VI uses the waveform name parameter as the key to retrieve the waveform property. icon Inputs/Outputs civrn.png instrument handle in instrument handle in identifies the instrument session. instrument handle in is obtaine

### niRFSGPlayback Retrieve Waveform Runtime Scaling VI

Returns the runtime scaling value stored in the NI-RFSG waveform database. This VI uses the **waveform name** parameter as the key to retrieve the waveform property.

[IMAGE alt='icon' src='nirfsgplayback-retrieve-waveform-runtime-scaling-vi.png']

#### Inputs/Outputs

| instrument handle in — instrument handle in identifies the instrument session. instrument handle in is obtained from either the niRFSG Initialize VI or the niRFSG Initialize With Options VI. waveform name — waveform name specifies the name of the waveform for which you want to retrieve the runtime scaling value. error in — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. instrument handle out — instrument handle out passes a reference from the instrument session to the next VI. runtime scaling — runtime scaling returns the runtime scaling value stored in the NI-RFSG database for the waveform specified in the waveform name parameter. This value is expressed in dB. error out — error out contains error information. This output provides standard error out functionality. |
| --- |

Parent topic:

Advanced

<!--NI_TOPIC bundle=rfsgplaybacklibrary-labview-api-ref path=instr-lib/nirfsgplayback/nirfsgplayback-retrieve-waveform-sample-rate-vi.html language=enus -->
## TOPIC 00038: niRFSGPlayback Retrieve Waveform Sample Rate VI

- bundle_id: `rfsgplaybacklibrary-labview-api-ref`
- source_path: `instr-lib/nirfsgplayback/nirfsgplayback-retrieve-waveform-sample-rate-vi.html`
- source_url: https://docs-be.ni.com/bundle/rfsgplaybacklibrary-labview-api-ref/raw/resource/enus/instr-lib/nirfsgplayback/nirfsgplayback-retrieve-waveform-sample-rate-vi.html
- document_id: `rfsgplaybacklibrary-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the sample rate stored in the NI-RFSG waveform database. This VI uses the waveform name parameter as the key to retrieve the waveform property. icon Inputs/Outputs civrn.png instrument handle in instrument handle in identifies the instrument session. instrument handle in is obtained from eit

### niRFSGPlayback Retrieve Waveform Sample Rate VI

Returns the sample rate stored in the NI-RFSG waveform database. This VI uses the **waveform name** parameter as the key to retrieve the waveform property.

[IMAGE alt='icon' src='nirfsgplayback-retrieve-waveform-sample-rate-vi.png']

#### Inputs/Outputs

| instrument handle in — instrument handle in identifies the instrument session. instrument handle in is obtained from either the niRFSG Initialize VI or the niRFSG Initialize With Options VI. waveform name — waveform name specifies the name of the waveform for which you want to retrieve the sample rate value. error in — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. instrument handle out — instrument handle out passes a reference from the instrument session to the next VI. sample rate — sample rate returns the sampling rate stored in the NI-RFSG waveform database for the waveform you specified in the waveform name parameter. This value is expressed in samples per second (S/s). error out — error out contains error information. This output provides standard error out functionality. |
| --- |

Parent topic:

Advanced

<!--NI_TOPIC bundle=rfsgplaybacklibrary-labview-api-ref path=instr-lib/nirfsgplayback/nirfsgplayback-retrieve-waveform-signal-bandwidth-vi.html language=enus -->
## TOPIC 00039: niRFSGPlayback Retrieve Waveform Signal Bandwidth VI

- bundle_id: `rfsgplaybacklibrary-labview-api-ref`
- source_path: `instr-lib/nirfsgplayback/nirfsgplayback-retrieve-waveform-signal-bandwidth-vi.html`
- source_url: https://docs-be.ni.com/bundle/rfsgplaybacklibrary-labview-api-ref/raw/resource/enus/instr-lib/nirfsgplayback/nirfsgplayback-retrieve-waveform-signal-bandwidth-vi.html
- document_id: `rfsgplaybacklibrary-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the signal bandwidth stored in the NI-RFSG waveform database. This VI uses the waveform name parameter as the key to retrieve the waveform property. icon Inputs/Outputs civrn.png instrument handle in instrument handle in identifies the instrument session. instrument handle in is obtained fro

### niRFSGPlayback Retrieve Waveform Signal Bandwidth VI

Returns the signal bandwidth stored in the NI-RFSG waveform database. This VI uses the **waveform name** parameter as the key to retrieve the waveform property.

[IMAGE alt='icon' src='nirfsgplayback-retrieve-waveform-signal-bandwidth-vi.png']

#### Inputs/Outputs

| instrument handle in — instrument handle in identifies the instrument session. instrument handle in is obtained from either the niRFSG Initialize VI or the niRFSG Initialize With Options VI. waveform name — waveform name specifies the name of the waveform for which you want to retrieve the waveform signal bandwidth. error in — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. instrument handle out — instrument handle out passes a reference from the instrument session to the next VI. signal bandwidth — signal bandwidth returns the signal bandwidth stored in the NI-RFSG waveform database for the waveform that you specified in the waveform name parameter. error out — error out contains error information. This output provides standard error out functionality. |
| --- |

Parent topic:

Advanced

<!--NI_TOPIC bundle=rfsgplaybacklibrary-labview-api-ref path=instr-lib/nirfsgplayback/nirfsgplayback-retrieve-waveform-size-vi.html language=enus -->
## TOPIC 00040: niRFSGPlayback Retrieve Waveform Size VI

- bundle_id: `rfsgplaybacklibrary-labview-api-ref`
- source_path: `instr-lib/nirfsgplayback/nirfsgplayback-retrieve-waveform-size-vi.html`
- source_url: https://docs-be.ni.com/bundle/rfsgplaybacklibrary-labview-api-ref/raw/resource/enus/instr-lib/nirfsgplayback/nirfsgplayback-retrieve-waveform-size-vi.html
- document_id: `rfsgplaybacklibrary-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the size of the waveform stored in the NI-RFSG waveform database. This VI uses the waveform name parameter as the key to retrieve the waveform property. icon Inputs/Outputs civrn.png instrument handle in instrument handle in identifies the instrument session. instrument handle in is obtained

### niRFSGPlayback Retrieve Waveform Size VI

Returns the size of the waveform stored in the NI-RFSG waveform database. This VI uses the **waveform name** parameter as the key to retrieve the waveform property.

[IMAGE alt='icon' src='nirfsgplayback-retrieve-waveform-size-vi.png']

#### Inputs/Outputs

| instrument handle in — instrument handle in identifies the instrument session. instrument handle in is obtained from either the niRFSG Initialize VI or the niRFSG Initialize With Options VI. waveform name — waveform name specifies the name of the waveform for which you want to retrieve the waveform size. error in — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. instrument handle out — instrument handle out passes a reference from the instrument session to the next VI. waveform size — waveform size returns the size of the waveform stored in the NI-RFSG waveform database for the waveform you specified in the waveform name parameter. This value is expressed in samples. error out — error out contains error information. This output provides standard error out functionality. |
| --- |

Parent topic:

Advanced

<!--NI_TOPIC bundle=rfsgplaybacklibrary-labview-api-ref path=instr-lib/nirfsgplayback/nirfsgplayback-set-script-to-generate-1-rfsg-vi.html language=enus -->
## TOPIC 00041: niRFSGPlayback Set Script to Generate (1 RFSG) VI

- bundle_id: `rfsgplaybacklibrary-labview-api-ref`
- source_path: `instr-lib/nirfsgplayback/nirfsgplayback-set-script-to-generate-1-rfsg-vi.html`
- source_url: https://docs-be.ni.com/bundle/rfsgplaybacklibrary-labview-api-ref/raw/resource/enus/instr-lib/nirfsgplayback/nirfsgplayback-set-script-to-generate-1-rfsg-vi.html
- document_id: `rfsgplaybacklibrary-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: The NI-RFSG IQ Rate property is set to the sample rate of the waveform in the script. If the version of the waveform file is 2.0 or later, the VI, Sets the NI-RFSG Peak Power Adjustment property to the minimum value of the peak to average power ratio (PAPR) of the waveform in the script. Sets the NI

### niRFSGPlayback Set Script to Generate (1 RFSG) VI

The NI-RFSG IQ Rate property is set to the sample rate of the waveform in the script.

If the version of the waveform file is 2.0 or later, the VI,

- Sets the NI-RFSG Peak Power Adjustment property to the minimum value of the peak to average power ratio (PAPR) of the waveform in the script.
- Sets the NI-RFSG Pre-filter Gain property to the minimum value of the runtime scaling of the waveform in the script.

If the version of the waveform file is lesser than 2.0, the VI,

- Sets the NI-RFSG Peak Power Adjustment property to the minimum value of the Headroom of the waveform in the script.
- Resets the NI-RFSG Pre-filter Gain property.

For the waveforms that have the RF blanking Enabled property set to True, this VI also does the following:

- If the values of RF blanking marker source of all the waveforms are empty, then the first unused marker in the script is set as the RF Blanking Source.
- Modifies the script to add the waveform burst start and stop locations as the RF Blanking marker locations

For PXIe-5840/5841/5842 and PXIe-5830/5831/5832 devices,

- Sets the NI-RFSG Signal Bandwidth property to the maximum signal bandwidth of the waveform in the script, if you set the LO Offset Mode to Auto . If no signal bandwidth is found in any waveform of the script, the NI-RFSG Signal Bandwidth property is set to 0.8 times the Sample Rate.
- Resets the NI-RFSG Signal Bandwidth, if you set the LO Offset Mode to No Offset .

[IMAGE alt='icon' src='nirfsgplayback-set-script-to-generate-1-rfsg-vi.png']

#### Inputs/Outputs

| instrument handle in — instrument handle in identifies the instrument session. instrument handle in is obtained from either the niRFSG Initialize VI or the niRFSG Initialize With Options VI. script text — script text specifies the script that controls the waveform generation. error in — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. instrument handle out — instrument handle out passes a reference from the instrument session to the next VI. error out — error out contains error information. This output provides standard error out functionality. |
| --- |

Parent topic:

niRFSGPlayback Set Script to Generate VI

<!--NI_TOPIC bundle=rfsgplaybacklibrary-labview-api-ref path=instr-lib/nirfsgplayback/nirfsgplayback-set-script-to-generate-n-rfsg-vi.html language=enus -->
## TOPIC 00042: niRFSGPlayback Set Script to Generate (N RFSG) VI

- bundle_id: `rfsgplaybacklibrary-labview-api-ref`
- source_path: `instr-lib/nirfsgplayback/nirfsgplayback-set-script-to-generate-n-rfsg-vi.html`
- source_url: https://docs-be.ni.com/bundle/rfsgplaybacklibrary-labview-api-ref/raw/resource/enus/instr-lib/nirfsgplayback/nirfsgplayback-set-script-to-generate-n-rfsg-vi.html
- document_id: `rfsgplaybacklibrary-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: The NI-RFSG IQ Rate property is set to the sample rate of the waveforms in the script. If the version of the waveform file is 2.0 or later, the VI, Sets the NI-RFSG Peak Power Adjustment property to the minimum value of the peak to average power ratio (PAPR) of the waveforms in the script. Sets the

### niRFSGPlayback Set Script to Generate (N RFSG) VI

The NI-RFSG IQ Rate property is set to the sample rate of the waveforms in the script.

If the version of the waveform file is 2.0 or later, the VI,

- Sets the NI-RFSG Peak Power Adjustment property to the minimum value of the peak to average power ratio (PAPR) of the waveforms in the script.
- Sets the NI-RFSG Pre-filter Gain property to the minimum value of the runtime scaling of the waveforms in the script.

If the version of the waveform file is lesser than 2.0, the VI,

- Sets the NI-RFSG Peak Power Adjustment property to the minimum value of the Headroom of the waveforms in the script.
- Resets the NI-RFSG Pre-filter Gain property.

For the waveforms that have the RF blanking Enabled property set to True, this VI also does the following:

- If the values of RF blanking marker source of all the waveforms are empty, then the first unused marker in the script is set as the RF Blanking Source.
- Modifies the script to add the waveform burst start and stop locations as the RF Blanking marker locations

For PXIe-5840/5841/5842 and PXIe-5830/5831/5832 devices,

- Sets the NI-RFSG Signal Bandwidth property to the maximum signal bandwidth of the waveforms in the script, if you set the LO Offset Mode to Auto . If no signal bandwidth is found in any waveform of the script, the NI-RFSG Signal Bandwidth property is set to 0.8 times the Sample Rate.
- Resets the NI-RFSG Signal Bandwidth, if you set the LO Offset Mode to No Offset .

[IMAGE alt='icon' src='nirfsgplayback-set-script-to-generate-n-rfsg-vi.png']

#### Inputs/Outputs

| instrument handles in — instrument handles in identifies instruments for multiple NI-RFSG sessions. instrument handles in is obtained from the niRFSG Initialize VI or the niRFSG Initialize With Options VI. script text — script text specifies the script that controls the waveform generation. error in — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. instrument handles out — instrument handles out passes an array of NI-RFSG instrument sessions to the next VI. error out — error out contains error information. This output provides standard error out functionality. |
| --- |

Parent topic:

niRFSGPlayback Set Script to Generate VI

<!--NI_TOPIC bundle=rfsgplaybacklibrary-labview-api-ref path=instr-lib/nirfsgplayback/nirfsgplayback-set-script-to-generate-vi.html language=enus -->
## TOPIC 00043: niRFSGPlayback Set Script to Generate VI

- bundle_id: `rfsgplaybacklibrary-labview-api-ref`
- source_path: `instr-lib/nirfsgplayback/nirfsgplayback-set-script-to-generate-vi.html`
- source_url: https://docs-be.ni.com/bundle/rfsgplaybacklibrary-labview-api-ref/raw/resource/enus/instr-lib/nirfsgplayback/nirfsgplayback-set-script-to-generate-vi.html
- document_id: `rfsgplaybacklibrary-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Configures the NI-RFSG driver to generate the waveforms specified in the script at the average power you configure on the NI-RFSG Power Level property. If you have enabled RF Blanking for the waveform, NI-RFSG is configured to correctly blank the output during the idle times of the waveform. icon

### niRFSGPlayback Set Script to Generate VI

Configures the NI-RFSG driver to generate the waveforms specified in the script at the average power you configure on the NI-RFSG Power Level property. If you have enabled RF Blanking for the waveform, NI-RFSG is configured to correctly blank the output during the idle times of the waveform.

[IMAGE alt='icon' src='nirfsgplayback-set-script-to-generate-vi.png']

- [niRFSGPlayback Set Script to Generate (1 RFSG) VI](../../instr-lib/nirfsgplayback/nirfsgplayback-set-script-to-generate-1-rfsg-vi.html) The NI-RFSG IQ Rate property is set to the sample rate of the waveform in the script.
- [niRFSGPlayback Set Script to Generate (N RFSG) VI](../../instr-lib/nirfsgplayback/nirfsgplayback-set-script-to-generate-n-rfsg-vi.html) The NI-RFSG IQ Rate property is set to the sample rate of the waveforms in the script.

Parent topic:

NI-RFSG Playback Library

<!--NI_TOPIC bundle=rfsgplaybacklibrary-labview-api-ref path=instr-lib/nirfsgplayback/nirfsgplayback-store-automatic-sg-sa-shared-lo-vi.html language=enus -->
## TOPIC 00044: niRFSGPlayback Store Automatic SG SA Shared LO VI

- bundle_id: `rfsgplaybacklibrary-labview-api-ref`
- source_path: `instr-lib/nirfsgplayback/nirfsgplayback-store-automatic-sg-sa-shared-lo-vi.html`
- source_url: https://docs-be.ni.com/bundle/rfsgplaybacklibrary-labview-api-ref/raw/resource/enus/instr-lib/nirfsgplayback/nirfsgplayback-store-automatic-sg-sa-shared-lo-vi.html
- document_id: `rfsgplaybacklibrary-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies whether the signal generator’s LO signal can be shared on request by the RFmx driver. It is recommended to use Automatic sharing of local oscillator (LO) in test setups that use a vector signal transceiver (VST) with the NI-RFSG to generate a signal at the DUT's input and the RFmx driver t

### niRFSGPlayback Store Automatic SG SA Shared LO VI

Specifies whether the signal generator’s LO signal can be shared on request by the RFmx driver. It is recommended to use Automatic sharing of local oscillator (LO) in test setups that use a vector signal transceiver (VST) with the NI-RFSG to generate a signal at the DUT's input and the RFmx driver to measure the signal at the DUT's output.

When using instruments that do not have LO with excellent phase noise, to minimize the contribution of the instrument's phase noise affecting your measurement, it is recommended to share the LO between the signal generator (SG) and signal analyzer (SA).

To enable sharing signal generator’s LO with signal analyzer automatically, setup the device specific physical connections as mentioned in the following table and follow the steps in the mentioned order.

| PXIe-5840/5841/5842 | SG LO is shared with SA via an external path. Hence you must connect RF Out LO Out to RF In LO In using a cable. |
| --- | --- |
| PXIe-5830/5831/5832 | SG LO is shared with SA via an internal path. Hence the external cable connection is not required. |

1. Enable Automatic SG SA Shared LO on NI-RFSG Playback Library
2. Set the LO Source property to Automatic_SG_SA_Shared in RFmx
3. Configure other required settings on NI-RFSG and RFmx, including selecting waveforms
4. Initiate NI-RFSG
5. Initiate RFmx

Note

LO Offset Mode

No Offset

[IMAGE alt='icon' src='nirfsgplayback-store-automatic-sg-sa-shared-lo-vi.png']

#### Inputs/Outputs

| instrument handle in — instrument handle in identifies the instrument session. instrument handle in is obtained from either the niRFSG Initialize VI or the niRFSG Initialize With Options VI. channel name — channel name this parameter is reserved for future use. SG SA Shared LO Enabled — automatic SG SA shared LO specifies the access control of SG LO. The default value is Disabled. Disabled (0) Disables automatic sharing the SG LO with SA. Enabled (1) Enables automatic sharing the SG LO with SA. error in — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. instrument handle out — instrument handle out passes a reference from the instrument session to the next VI. error out — error out contains error information. This output provides standard error out functionality. |  |
| --- | --- |
| Disabled (0) | Disables automatic sharing the SG LO with SA. |
| Enabled (1) | Enables automatic sharing the SG LO with SA. |

Parent topic:

Advanced

<!--NI_TOPIC bundle=rfsgplaybacklibrary-labview-api-ref path=instr-lib/nirfsgplayback/nirfsgplayback-store-waveform-burst-start-locations-vi.html language=enus -->
## TOPIC 00045: niRFSGPlayback Store Waveform Burst Start Locations VI

- bundle_id: `rfsgplaybacklibrary-labview-api-ref`
- source_path: `instr-lib/nirfsgplayback/nirfsgplayback-store-waveform-burst-start-locations-vi.html`
- source_url: https://docs-be.ni.com/bundle/rfsgplaybacklibrary-labview-api-ref/raw/resource/enus/instr-lib/nirfsgplayback/nirfsgplayback-store-waveform-burst-start-locations-vi.html
- document_id: `rfsgplaybacklibrary-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Stores the burst start location, which you specify in the burst start locations parameter, in the NI-RFSG waveform database. icon Inputs/Outputs civrn.png instrument handle in instrument handle in identifies the instrument session. instrument handle in is obtained from either the niRFSG Initialize V

### niRFSGPlayback Store Waveform Burst Start Locations VI

Stores the burst start location, which you specify in the **burst start locations** parameter, in the NI-RFSG waveform database.

[IMAGE alt='icon' src='nirfsgplayback-store-waveform-burst-start-locations-vi.png']

#### Inputs/Outputs

| instrument handle in — instrument handle in identifies the instrument session. instrument handle in is obtained from either the niRFSG Initialize VI or the niRFSG Initialize With Options VI. waveform name — waveform name specifies the name of the waveform for which you want to store the burst start locations. burst start locations — burst start locations specifies an array of the burst start locations to store in the NI-RFSG waveform database. error in — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. instrument handle out — instrument handle out passes a reference from the instrument session to the next VI. error out — error out contains error information. This output provides standard error out functionality. |
| --- |

Parent topic:

Advanced

<!--NI_TOPIC bundle=rfsgplaybacklibrary-labview-api-ref path=instr-lib/nirfsgplayback/nirfsgplayback-store-waveform-burst-stop-locations-vi.html language=enus -->
## TOPIC 00046: niRFSGPlayback Store Waveform Burst Stop Locations VI

- bundle_id: `rfsgplaybacklibrary-labview-api-ref`
- source_path: `instr-lib/nirfsgplayback/nirfsgplayback-store-waveform-burst-stop-locations-vi.html`
- source_url: https://docs-be.ni.com/bundle/rfsgplaybacklibrary-labview-api-ref/raw/resource/enus/instr-lib/nirfsgplayback/nirfsgplayback-store-waveform-burst-stop-locations-vi.html
- document_id: `rfsgplaybacklibrary-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Stores the burst stop location, which you specify in the burst stop locations parameter, in the NI-RFSG waveform database. icon Inputs/Outputs civrn.png instrument handle in instrument handle in identifies the instrument session. instrument handle in is obtained from either the niRFSG Initialize VI

### niRFSGPlayback Store Waveform Burst Stop Locations VI

Stores the burst stop location, which you specify in the **burst stop locations** parameter, in the NI-RFSG waveform database.

[IMAGE alt='icon' src='nirfsgplayback-store-waveform-burst-stop-locations-vi.png']

#### Inputs/Outputs

| instrument handle in — instrument handle in identifies the instrument session. instrument handle in is obtained from either the niRFSG Initialize VI or the niRFSG Initialize With Options VI. waveform name — waveform name specifies the name of the waveform for which you want to store the burst stop locations. burst stop locations — burst stop locations specifies an array of the burst stop locations to store in the NI-RFSG waveform database. error in — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. instrument handle out — instrument handle out passes a reference from the instrument session to the next VI. error out — error out contains error information. This output provides standard error out functionality. |
| --- |

Parent topic:

Advanced

<!--NI_TOPIC bundle=rfsgplaybacklibrary-labview-api-ref path=instr-lib/nirfsgplayback/nirfsgplayback-store-waveform-lo-offset-mode-vi.html language=enus -->
## TOPIC 00047: niRFSGPlayback Store Waveform LO Offset Mode VI

- bundle_id: `rfsgplaybacklibrary-labview-api-ref`
- source_path: `instr-lib/nirfsgplayback/nirfsgplayback-store-waveform-lo-offset-mode-vi.html`
- source_url: https://docs-be.ni.com/bundle/rfsgplaybacklibrary-labview-api-ref/raw/resource/enus/instr-lib/nirfsgplayback/nirfsgplayback-store-waveform-lo-offset-mode-vi.html
- document_id: `rfsgplaybacklibrary-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Stores the LO offset mode value, which you specify in the LO offset mode parameter, in the NI-RFSG waveform database. icon Inputs/Outputs civrn.png instrument handle in instrument handle in identifies the instrument session. instrument handle in is obtained from either the niRFSG Initialize VI or th

### niRFSGPlayback Store Waveform LO Offset Mode VI

Stores the LO offset mode value, which you specify in the **LO offset mode** parameter, in the NI-RFSG waveform database.

[IMAGE alt='icon' src='nirfsgplayback-store-waveform-lo-offset-mode-vi.png']

#### Inputs/Outputs

| instrument handle in — instrument handle in identifies the instrument session. instrument handle in is obtained from either the niRFSG Initialize VI or the niRFSG Initialize With Options VI. waveform name — waveform name specifies the name of the waveform for which you want to store the LO offset mode value. LO offset mode — LO offset mode specifies the LO offset mode to store in the NI-RFSG waveform database. The default value is Auto. The following enums define the behavior of the niRFSGPlayback Set Script to Generate VI on PXIe-5840/5841/5842 and PXIe-5830/5831/5832. Auto (0) Sets the signal bandwidth value to the niRFSG Signal Bandwidth property, and resets the niRFSG Upconverter Frequency Offset property. No Offset (1) Resets the values of the niRFSG Signal Bandwidth and niRFSG Upconverter Frequency Offset properties. Disabled (2) Does not set the niRFSG Signal Bandwidth property or reset the niRFSG Upconverter Frequency Offset property. Note Measurement results might get affected while performing measurements in the RFmx driver, if the signal analyzer measurement frequency span is wide enough to capture signal generator LO. In these cases, it is recommended to configure the LO Offset Mode parameter to No Offset. error in — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. instrument handle out — instrument handle out passes a reference from the instrument session to the next VI. error out — error out contains error information. This output provides standard error out functionality. |  |
| --- | --- |
| Auto (0) | Sets the signal bandwidth value to the niRFSG Signal Bandwidth property, and resets the niRFSG Upconverter Frequency Offset property. |
| No Offset (1) | Resets the values of the niRFSG Signal Bandwidth and niRFSG Upconverter Frequency Offset properties. |
| Disabled (2) | Does not set the niRFSG Signal Bandwidth property or reset the niRFSG Upconverter Frequency Offset property. |

Parent topic:

Advanced

<!--NI_TOPIC bundle=rfsgplaybacklibrary-labview-api-ref path=instr-lib/nirfsgplayback/nirfsgplayback-store-waveform-papr-vi.html language=enus -->
## TOPIC 00048: niRFSGPlayback Store Waveform PAPR VI

- bundle_id: `rfsgplaybacklibrary-labview-api-ref`
- source_path: `instr-lib/nirfsgplayback/nirfsgplayback-store-waveform-papr-vi.html`
- source_url: https://docs-be.ni.com/bundle/rfsgplaybacklibrary-labview-api-ref/raw/resource/enus/instr-lib/nirfsgplayback/nirfsgplayback-store-waveform-papr-vi.html
- document_id: `rfsgplaybacklibrary-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Stores the peak to average power ratio (PAPR), which you specify in the PAPR parameter, in the NI-RFSG waveform database. icon Inputs/Outputs civrn.png instrument handle in instrument handle in identifies the instrument session. instrument handle in is obtained from either the niRFSG Initialize VI o

### niRFSGPlayback Store Waveform PAPR VI

Stores the peak to average power ratio (PAPR), which you specify in the **PAPR** parameter, in the NI-RFSG waveform database.

[IMAGE alt='icon' src='nirfsgplayback-store-waveform-papr-vi.png']

#### Inputs/Outputs

| instrument handle in — instrument handle in identifies the instrument session. instrument handle in is obtained from either the niRFSG Initialize VI or the niRFSG Initialize With Options VI. waveform name — waveform name specifies the name of the waveform for which you want to store the PAPR. PAPR — PAPR specifies the PAPR to store in the NI-RFSG database. This value is expressed in dB. error in — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. instrument handle out — instrument handle out passes a reference from the instrument session to the next VI. error out — error out contains error information. This output provides standard error out functionality. |
| --- |

Parent topic:

Advanced

<!--NI_TOPIC bundle=rfsgplaybacklibrary-labview-api-ref path=instr-lib/nirfsgplayback/nirfsgplayback-store-waveform-peak-power-adjustment-vi.html language=enus -->
## TOPIC 00049: niRFSGPlayback Store Waveform Peak Power Adjustment VI

- bundle_id: `rfsgplaybacklibrary-labview-api-ref`
- source_path: `instr-lib/nirfsgplayback/nirfsgplayback-store-waveform-peak-power-adjustment-vi.html`
- source_url: https://docs-be.ni.com/bundle/rfsgplaybacklibrary-labview-api-ref/raw/resource/enus/instr-lib/nirfsgplayback/nirfsgplayback-store-waveform-peak-power-adjustment-vi.html
- document_id: `rfsgplaybacklibrary-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Stores the peak power adjustment, which you specify in the peak power adjustment parameter, in the NI-RFSG waveform database. icon Inputs/Outputs civrn.png instrument handle in instrument handle in identifies the instrument session. instrument handle in is obtained from either the niRFSG Initialize

### niRFSGPlayback Store Waveform Peak Power Adjustment VI

Stores the peak power adjustment, which you specify in the **peak power adjustment** parameter, in the NI-RFSG waveform database.

[IMAGE alt='icon' src='nirfsgplayback-store-waveform-peak-power-adjustment-vi.png']

#### Inputs/Outputs

| instrument handle in — instrument handle in identifies the instrument session. instrument handle in is obtained from either the niRFSG Initialize VI or the niRFSG Initialize With Options VI. waveform name — waveform name specifies the name of the waveform for which you want to store the peak power adjustment value. peak power adjustment — peak power adjustment specifies the peak power adjustment to store in the NI-RFSG waveform database. error in — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. instrument handle out — instrument handle out passes a reference from the instrument session to the next VI. error out — error out contains error information. This output provides standard error out functionality. |
| --- |

Parent topic:

Obsolete

<!--NI_TOPIC bundle=rfsgplaybacklibrary-labview-api-ref path=instr-lib/nirfsgplayback/nirfsgplayback-store-waveform-rf-blanking-enabled-vi.html language=enus -->
## TOPIC 00050: niRFSGPlayback Store Waveform RF Blanking Enabled VI

- bundle_id: `rfsgplaybacklibrary-labview-api-ref`
- source_path: `instr-lib/nirfsgplayback/nirfsgplayback-store-waveform-rf-blanking-enabled-vi.html`
- source_url: https://docs-be.ni.com/bundle/rfsgplaybacklibrary-labview-api-ref/raw/resource/enus/instr-lib/nirfsgplayback/nirfsgplayback-store-waveform-rf-blanking-enabled-vi.html
- document_id: `rfsgplaybacklibrary-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Stores the RF blanking enabled value, which you specify in the RF blanking enabled parameter, in the NI-RFSG waveform database. icon Inputs/Outputs civrn.png instrument handle in instrument handle in identifies the instrument session. instrument handle in is obtained from either the niRFSG Initializ

### niRFSGPlayback Store Waveform RF Blanking Enabled VI

Stores the RF blanking enabled value, which you specify in the **RF blanking enabled** parameter, in the NI-RFSG waveform database.

[IMAGE alt='icon' src='nirfsgplayback-store-waveform-rf-blanking-enabled-vi.png']

#### Inputs/Outputs

| instrument handle in — instrument handle in identifies the instrument session. instrument handle in is obtained from either the niRFSG Initialize VI or the niRFSG Initialize With Options VI. waveform name — waveform name specifies the name of the waveform for which you want to store the RF blanking enabled value. RF blanking enabled — RF blanking enabled specifies the RF blanking enabled value to store in the NI-RFSG waveform database. error in — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. instrument handle out — instrument handle out passes a reference from the instrument session to the next VI. error out — error out contains error information. This output provides standard error out functionality. |
| --- |

Parent topic:

Advanced

<!--NI_TOPIC bundle=rfsgplaybacklibrary-labview-api-ref path=instr-lib/nirfsgplayback/nirfsgplayback-store-waveform-rf-blanking-marker-locations-vi.html language=enus -->
## TOPIC 00051: niRFSGPlayback Store Waveform RF Blanking Marker Locations VI

- bundle_id: `rfsgplaybacklibrary-labview-api-ref`
- source_path: `instr-lib/nirfsgplayback/nirfsgplayback-store-waveform-rf-blanking-marker-locations-vi.html`
- source_url: https://docs-be.ni.com/bundle/rfsgplaybacklibrary-labview-api-ref/raw/resource/enus/instr-lib/nirfsgplayback/nirfsgplayback-store-waveform-rf-blanking-marker-locations-vi.html
- document_id: `rfsgplaybacklibrary-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Stores the RF blanking marker positions, which you specify in the RF blanking marker locations parameter, in the NI-RFSG waveform database. icon Inputs/Outputs civrn.png instrument handle in instrument handle in identifies the instrument session. instrument handle in is obtained from either the niRF

### niRFSGPlayback Store Waveform RF Blanking Marker Locations VI

Stores the RF blanking marker positions, which you specify in the **RF blanking marker locations** parameter, in the NI-RFSG waveform database.

[IMAGE alt='icon' src='nirfsgplayback-store-waveform-rf-blanking-marker-locations-vi.png']

#### Inputs/Outputs

| instrument handle in — instrument handle in identifies the instrument session. instrument handle in is obtained from either the niRFSG Initialize VI or the niRFSG Initialize With Options VI. waveform name — waveform name specifies the name of the waveform for which you want to store the RF blanking marker locations. RF blanking marker locations — RF blanking marker locations specifies the RF blanking marker positions to store. It is an array of sample positions, within the waveform, of the marker events that you can use to toggle the RF blanking state. error in — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. instrument handle out — instrument handle out passes a reference from the instrument session to the next VI. error out — error out contains error information. This output provides standard error out functionality. |
| --- |

Parent topic:

Obsolete

<!--NI_TOPIC bundle=rfsgplaybacklibrary-labview-api-ref path=instr-lib/nirfsgplayback/nirfsgplayback-store-waveform-rf-blanking-marker-source-vi.html language=enus -->
## TOPIC 00052: niRFSGPlayback Store Waveform RF Blanking Marker Source VI

- bundle_id: `rfsgplaybacklibrary-labview-api-ref`
- source_path: `instr-lib/nirfsgplayback/nirfsgplayback-store-waveform-rf-blanking-marker-source-vi.html`
- source_url: https://docs-be.ni.com/bundle/rfsgplaybacklibrary-labview-api-ref/raw/resource/enus/instr-lib/nirfsgplayback/nirfsgplayback-store-waveform-rf-blanking-marker-source-vi.html
- document_id: `rfsgplaybacklibrary-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Stores the RF blanking marker source, which you specify in the RF blanking marker source parameter, in the NI-RFSG waveform database. icon Inputs/Outputs civrn.png instrument handle in instrument handle in identifies the instrument session. instrument handle in is obtained from either the niRFSG Ini

### niRFSGPlayback Store Waveform RF Blanking Marker Source VI

Stores the RF blanking marker source, which you specify in the **RF blanking marker source** parameter, in the NI-RFSG waveform database.

[IMAGE alt='icon' src='nirfsgplayback-store-waveform-rf-blanking-marker-source-vi.png']

#### Inputs/Outputs

| instrument handle in — instrument handle in identifies the instrument session. instrument handle in is obtained from either the niRFSG Initialize VI or the niRFSG Initialize With Options VI. waveform name — waveform name specifies the name of the waveform for which you want to store the RF blanking marker source. RF blanking marker source — RF blanking marker source specifies the RF blanking marker source to store in the NI-RFSG waveform database. marker0 RF blanking source is tied to marker0 event. marker1 RF blanking source is tied to marker1 event. marker2 RF blanking source is tied to marker2 event. marker3 RF blanking source is tied to marker3 event. error in — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. instrument handle out — instrument handle out passes a reference from the instrument session to the next VI. error out — error out contains error information. This output provides standard error out functionality. |  |
| --- | --- |
| marker0 | RF blanking source is tied to marker0 event. |
| marker1 | RF blanking source is tied to marker1 event. |
| marker2 | RF blanking source is tied to marker2 event. |
| marker3 | RF blanking source is tied to marker3 event. |

Parent topic:

Advanced

<!--NI_TOPIC bundle=rfsgplaybacklibrary-labview-api-ref path=instr-lib/nirfsgplayback/nirfsgplayback-store-waveform-runtime-scaling-vi.html language=enus -->
## TOPIC 00053: niRFSGPlayback Store Waveform Runtime Scaling VI

- bundle_id: `rfsgplaybacklibrary-labview-api-ref`
- source_path: `instr-lib/nirfsgplayback/nirfsgplayback-store-waveform-runtime-scaling-vi.html`
- source_url: https://docs-be.ni.com/bundle/rfsgplaybacklibrary-labview-api-ref/raw/resource/enus/instr-lib/nirfsgplayback/nirfsgplayback-store-waveform-runtime-scaling-vi.html
- document_id: `rfsgplaybacklibrary-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Stores the runtime scaling value, which you specify in the runtime scaling parameter, in the NI-RFSG waveform database. icon Inputs/Outputs civrn.png instrument handle in instrument handle in identifies the instrument session. instrument handle in is obtained from either the niRFSG Initialize VI or

### niRFSGPlayback Store Waveform Runtime Scaling VI

Stores the runtime scaling value, which you specify in the **runtime scaling** parameter, in the NI-RFSG waveform database.

[IMAGE alt='icon' src='nirfsgplayback-store-waveform-runtime-scaling-vi.png']

#### Inputs/Outputs

| instrument handle in — instrument handle in identifies the instrument session. instrument handle in is obtained from either the niRFSG Initialize VI or the niRFSG Initialize With Options VI. waveform name — waveform name specifies the name of the waveform for which you want to store the runtime scaling value. runtime scaling — runtime scaling specifies the runtime scaling value to store in the NI-RFSG database. This value is expressed in dB. error in — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. instrument handle out — instrument handle out passes a reference from the instrument session to the next VI. error out — error out contains error information. This output provides standard error out functionality. |
| --- |

Parent topic:

Advanced

<!--NI_TOPIC bundle=rfsgplaybacklibrary-labview-api-ref path=instr-lib/nirfsgplayback/nirfsgplayback-store-waveform-sample-rate-vi.html language=enus -->
## TOPIC 00054: niRFSGPlayback Store Waveform Sample Rate VI

- bundle_id: `rfsgplaybacklibrary-labview-api-ref`
- source_path: `instr-lib/nirfsgplayback/nirfsgplayback-store-waveform-sample-rate-vi.html`
- source_url: https://docs-be.ni.com/bundle/rfsgplaybacklibrary-labview-api-ref/raw/resource/enus/instr-lib/nirfsgplayback/nirfsgplayback-store-waveform-sample-rate-vi.html
- document_id: `rfsgplaybacklibrary-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Stores the sample rate, which you specify in the sample rate parameter, in the NI-RFSG waveform database. icon Inputs/Outputs civrn.png instrument handle in instrument handle in identifies the instrument session. instrument handle in is obtained from either the niRFSG Initialize VI or the niRFSG Ini

### niRFSGPlayback Store Waveform Sample Rate VI

Stores the sample rate, which you specify in the **sample rate** parameter, in the NI-RFSG waveform database.

[IMAGE alt='icon' src='nirfsgplayback-store-waveform-sample-rate-vi.png']

#### Inputs/Outputs

| instrument handle in — instrument handle in identifies the instrument session. instrument handle in is obtained from either the niRFSG Initialize VI or the niRFSG Initialize With Options VI. waveform name — waveform name specifies the name of the waveform for which you want to store the sample rate. sample rate — sample rate specifies the sampling rate to store in the NI-RFSG waveform database. This value is expressed in samples per second (S/s). error in — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. instrument handle out — instrument handle out passes a reference from the instrument session to the next VI. error out — error out contains error information. This output provides standard error out functionality. |
| --- |

Parent topic:

Advanced

<!--NI_TOPIC bundle=rfsgplaybacklibrary-labview-api-ref path=instr-lib/nirfsgplayback/nirfsgplayback-store-waveform-signal-bandwidth-vi.html language=enus -->
## TOPIC 00055: niRFSGPlayback Store Waveform Signal Bandwidth VI

- bundle_id: `rfsgplaybacklibrary-labview-api-ref`
- source_path: `instr-lib/nirfsgplayback/nirfsgplayback-store-waveform-signal-bandwidth-vi.html`
- source_url: https://docs-be.ni.com/bundle/rfsgplaybacklibrary-labview-api-ref/raw/resource/enus/instr-lib/nirfsgplayback/nirfsgplayback-store-waveform-signal-bandwidth-vi.html
- document_id: `rfsgplaybacklibrary-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Stores the signal bandwidth, which you specify in the signal bandwidth parameter, in the NI-RFSG waveform database. icon Inputs/Outputs civrn.png instrument handle in instrument handle in identifies the instrument session. instrument handle in is obtained from either the niRFSG Initialize VI or the

### niRFSGPlayback Store Waveform Signal Bandwidth VI

Stores the signal bandwidth, which you specify in the **signal bandwidth** parameter, in the NI-RFSG waveform database.

[IMAGE alt='icon' src='nirfsgplayback-store-waveform-signal-bandwidth-vi.png']

#### Inputs/Outputs

| instrument handle in — instrument handle in identifies the instrument session. instrument handle in is obtained from either the niRFSG Initialize VI or the niRFSG Initialize With Options VI. waveform name — waveform name specifies the name of the waveform for which you want to store the signal bandwidth. signal bandwidth — signal bandwidth specifies the signal bandwidth to store in the NI-RFSG waveform database. error in — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. instrument handle out — instrument handle out passes a reference from the instrument session to the next VI. error out — error out contains error information. This output provides standard error out functionality. |
| --- |

Parent topic:

Advanced

<!--NI_TOPIC bundle=rfsgplaybacklibrary-labview-api-ref path=instr-lib/nirfsgplayback/nirfsgplayback-store-waveform-size-vi.html language=enus -->
## TOPIC 00056: niRFSGPlayback Store Waveform Size VI

- bundle_id: `rfsgplaybacklibrary-labview-api-ref`
- source_path: `instr-lib/nirfsgplayback/nirfsgplayback-store-waveform-size-vi.html`
- source_url: https://docs-be.ni.com/bundle/rfsgplaybacklibrary-labview-api-ref/raw/resource/enus/instr-lib/nirfsgplayback/nirfsgplayback-store-waveform-size-vi.html
- document_id: `rfsgplaybacklibrary-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Stores the size of the waveform, which you specify in the waveform size parameter, in the NI-RFSG waveform database. icon Inputs/Outputs civrn.png instrument handle in instrument handle in identifies the instrument session. instrument handle in is obtained from either the niRFSG Initialize VI or the

### niRFSGPlayback Store Waveform Size VI

Stores the size of the waveform, which you specify in the **waveform size** parameter, in the NI-RFSG waveform database.

[IMAGE alt='icon' src='nirfsgplayback-store-waveform-size-vi.png']

#### Inputs/Outputs

| instrument handle in — instrument handle in identifies the instrument session. instrument handle in is obtained from either the niRFSG Initialize VI or the niRFSG Initialize With Options VI. waveform name — waveform name specifies the name of the waveform for which you want to store the waveform size. waveform size — waveform size specifies the size of the waveform to store in the NI-RFSG waveform database. This value is expressed in samples. error in — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. instrument handle out — instrument handle out passes a reference from the instrument session to the next VI. error out — error out contains error information. This output provides standard error out functionality. |
| --- |

Parent topic:

Advanced

<!--NI_TOPIC bundle=rfsgplaybacklibrary-labview-api-ref path=instr-lib/nirfsgplayback/standard_error_parameter_behavior.html language=enus -->
## TOPIC 00057: Standard Error Parameter Behavior

- bundle_id: `rfsgplaybacklibrary-labview-api-ref`
- source_path: `instr-lib/nirfsgplayback/standard_error_parameter_behavior.html`
- source_url: https://docs-be.ni.com/bundle/rfsgplaybacklibrary-labview-api-ref/raw/resource/enus/instr-lib/nirfsgplayback/standard_error_parameter_behavior.html
- document_id: `rfsgplaybacklibrary-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Many LabVIEW nodes such as VIs contain error in or error out parameters you can use to manage errors. These parameters typically provide the same, standard functionality. When a node exhibits different parameter functionality, the exceptions are documented in the reference material for that node. St

### Standard Error Parameter Behavior

Many LabVIEW nodes such as VIs contain error in or error out parameters you can use to manage errors. These parameters typically provide the same, standard functionality. When a node exhibits different parameter functionality, the exceptions are documented in the reference material for that node. 
 Standard behaviour error in and error out described is as follows

Note

error in

error in

|  | error in describes error conditions that occur before this node runs. The default is no error. If an error occurred before this node runs, the node passes the error in value to error out. This node runs normally only if no error occurred before this node runs. If an error occurs while this node runs, it runs normally and sets its own error status in error out. Use error in and error out to check errors and to specify execution order by wiring error out from one node to error in of the next node. |
| --- | --- |

|  | error out contains error information. If error in indicates that an error occurred before this VI ran, error out contains the same error information. Otherwise, it describes the error status that this VI or function produces. Right-click the error out front panel indicator and select Explain Error from the shortcut menu for more information about the error. |
| --- | --- |

The error in cluster contains the following cluster elements:

|  | status is TRUE (X) if an error occurred before this node ran or FALSE (checkmark) to indicate a warning or that no error occurred before this node ran. The default is FALSE. |
| --- | --- |
|  | code is the error or warning code. The default is 0. If status is TRUE, code is an error code. If status is FALSE, code is 0 or a warning code. |
|  | source specifies the origin of the error or warning and is, in most cases, the name of the node that produced the error or warning. The default is an empty string. |

error out contains the following cluster elements:

|  | status is TRUE (X) if an error occurred before this node ran or during the running of this node or FALSE (checkmark) to indicate a warning or that no error occurred before this node ran or during the running of this node. |
| --- | --- |
|  | code is the error or warning code. If status is TRUE, code is an error code. If status is FALSE, code is 0 or a warning code. |
|  | source specifies the origin of the error or warning and is, in most cases, the name of the node that produced the error or warning. |

<!--NI_TOPIC bundle=rfsgplaybacklibrary-labview-api-ref path=menus/categories/measurement/nirfsgplayback-mnu.html language=enus -->
## TOPIC 00058: NI-RFSG Playback Library

- bundle_id: `rfsgplaybacklibrary-labview-api-ref`
- source_path: `menus/categories/measurement/nirfsgplayback-mnu.html`
- source_url: https://docs-be.ni.com/bundle/rfsgplaybacklibrary-labview-api-ref/raw/resource/enus/menus/categories/measurement/nirfsgplayback-mnu.html
- document_id: `rfsgplaybacklibrary-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Use the VIs on this palette to generate waveforms saved in a technical data management streaming (TDMS) file using the NI-RFSG driver. © 2015–2026 National Instruments Corporation. All rights reserved. icon

### NI-RFSG Playback Library

Use the VIs on this palette to generate waveforms saved in a technical data management streaming (TDMS) file using the NI-RFSG driver.

© 2015–2026 National Instruments Corporation. All rights reserved.

[IMAGE alt='icon' src='nirfsgplayback-mnu.png']

- [niRFSGPlayback Read and Download Waveform From File VI](../../../instr-lib/nirfsgplayback/nirfsgplayback-read-and-download-waveform-from-file-vi.html) Reads the waveform stored in a technical data management streaming (TDMS) file, downloads it to NI RF vector signal generators, and stores the waveform properties found in the TDMS file in the NI-RFSG waveform database.
- [niRFSGPlayback Read Waveform From File VI](../../../instr-lib/nirfsgplayback/nirfsgplayback-read-waveform-from-file-vi.html) Returns the waveform stored in the technical data management streaming (TDMS) file.
- [niRFSGPlayback Clear All Waveforms VI](../../../instr-lib/nirfsgplayback/nirfsgplayback-clear-all-waveforms-vi.html) Deletes all the waveforms from NI-RFSG memory and removes all the waveform properties from the NI-RFSG waveform database for the specified device.
- [niRFSGPlayback Clear Waveform VI](../../../instr-lib/nirfsgplayback/nirfsgplayback-clear-waveform-vi.html) Deletes the waveform from NI-RFSG device memory and removes the waveform properties from NI-RFSG waveform database for the specified device.
- [niRFSGPlayback Set Script to Generate VI](../../../instr-lib/nirfsgplayback/nirfsgplayback-set-script-to-generate-vi.html) Configures the NI-RFSG driver to generate the waveforms specified in the script at the average power you configure on the NI-RFSG Power Level property. If you have enabled RF Blanking for the waveform, NI-RFSG is configured to correctly blank the output during the idle times of the waveform.
- [niRFSGPlayback Download User Waveform VI](../../../instr-lib/nirfsgplayback/nirfsgplayback-download-user-waveform-vi.html) Normalizes the input waveform and writes it into the NI RF vector signal generator. This VI computes the peak to average power ratio (PAPR) using the bursts in the waveform, stores the PAPR, sample rate, waveform size, and runtime scaling value of -1.5 dB in the NI-RFSG waveform database.
- [Advanced](../../../menus/categories/measurement/nirfsgplayback/nirfsgplayback-advanced-mnu.html) Use the VIs on this palette to use advanced features.
- [Utility](../../../menus/categories/measurement/nirfsgplayback/nirfsgplayback-utility-mnu.html) Use the VIs on this palette to configure utility features.

<!--NI_TOPIC bundle=rfsgplaybacklibrary-labview-api-ref path=menus/categories/measurement/nirfsgplayback/nirfsgplayback-advanced-mnu.html language=enus -->
## TOPIC 00059: Advanced

- bundle_id: `rfsgplaybacklibrary-labview-api-ref`
- source_path: `menus/categories/measurement/nirfsgplayback/nirfsgplayback-advanced-mnu.html`
- source_url: https://docs-be.ni.com/bundle/rfsgplaybacklibrary-labview-api-ref/raw/resource/enus/menus/categories/measurement/nirfsgplayback/nirfsgplayback-advanced-mnu.html
- document_id: `rfsgplaybacklibrary-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Use the VIs on this palette to use advanced features. icon

### Advanced

Use the VIs on this palette to use advanced features.

[IMAGE alt='icon' src='nirfsgplayback-advanced-mnu.png']

- [niRFSGPlayback Store Waveform Sample Rate VI](../../../../instr-lib/nirfsgplayback/nirfsgplayback-store-waveform-sample-rate-vi.html) Stores the sample rate, which you specify in the sample rate parameter, in the NI-RFSG waveform database.
- [niRFSGPlayback Store Waveform PAPR VI](../../../../instr-lib/nirfsgplayback/nirfsgplayback-store-waveform-papr-vi.html) Stores the peak to average power ratio (PAPR), which you specify in the PAPR parameter, in the NI-RFSG waveform database.
- [niRFSGPlayback Store Waveform Runtime Scaling VI](../../../../instr-lib/nirfsgplayback/nirfsgplayback-store-waveform-runtime-scaling-vi.html) Stores the runtime scaling value, which you specify in the runtime scaling parameter, in the NI-RFSG waveform database.
- [niRFSGPlayback Store Waveform RF Blanking Enabled VI](../../../../instr-lib/nirfsgplayback/nirfsgplayback-store-waveform-rf-blanking-enabled-vi.html) Stores the RF blanking enabled value, which you specify in the RF blanking enabled parameter, in the NI-RFSG waveform database.
- [niRFSGPlayback Store Waveform RF Blanking Marker Source VI](../../../../instr-lib/nirfsgplayback/nirfsgplayback-store-waveform-rf-blanking-marker-source-vi.html) Stores the RF blanking marker source, which you specify in the RF blanking marker source parameter, in the NI-RFSG waveform database.
- [niRFSGPlayback Store Waveform Burst Start Locations VI](../../../../instr-lib/nirfsgplayback/nirfsgplayback-store-waveform-burst-start-locations-vi.html) Stores the burst start location, which you specify in the burst start locations parameter, in the NI-RFSG waveform database.
- [niRFSGPlayback Store Waveform Burst Stop Locations VI](../../../../instr-lib/nirfsgplayback/nirfsgplayback-store-waveform-burst-stop-locations-vi.html) Stores the burst stop location, which you specify in the burst stop locations parameter, in the NI-RFSG waveform database.
- [niRFSGPlayback Store Waveform LO Offset Mode VI](../../../../instr-lib/nirfsgplayback/nirfsgplayback-store-waveform-lo-offset-mode-vi.html) Stores the LO offset mode value, which you specify in the LO offset mode parameter, in the NI-RFSG waveform database.
- [niRFSGPlayback Store Waveform Signal Bandwidth VI](../../../../instr-lib/nirfsgplayback/nirfsgplayback-store-waveform-signal-bandwidth-vi.html) Stores the signal bandwidth, which you specify in the signal bandwidth parameter, in the NI-RFSG waveform database.
- [niRFSGPlayback Store Waveform Size VI](../../../../instr-lib/nirfsgplayback/nirfsgplayback-store-waveform-size-vi.html) Stores the size of the waveform, which you specify in the waveform size parameter, in the NI-RFSG waveform database.
- [niRFSGPlayback Store Automatic SG SA Shared LO VI](../../../../instr-lib/nirfsgplayback/nirfsgplayback-store-automatic-sg-sa-shared-lo-vi.html) Specifies whether the signal generator’s LO signal can be shared on request by the RFmx driver. It is recommended to use Automatic sharing of local oscillator (LO) in test setups that use a vector signal transceiver (VST) with the NI-RFSG to generate a signal at the DUT's input and the RFmx driver to measure the signal at the DUT's output.
- [niRFSGPlayback Retrieve Waveform Sample Rate VI](../../../../instr-lib/nirfsgplayback/nirfsgplayback-retrieve-waveform-sample-rate-vi.html) Returns the sample rate stored in the NI-RFSG waveform database. This VI uses the waveform name parameter as the key to retrieve the waveform property.
- [niRFSGPlayback Retrieve Waveform PAPR VI](../../../../instr-lib/nirfsgplayback/nirfsgplayback-retrieve-waveform-papr-vi.html) Returns the peak to average power ratio (PAPR) stored in the NI-RFSG waveform database. This VI uses the waveform name parameter as the key to retrieve the waveform property.
- [niRFSGPlayback Retrieve Waveform Runtime Scaling VI](../../../../instr-lib/nirfsgplayback/nirfsgplayback-retrieve-waveform-runtime-scaling-vi.html) Returns the runtime scaling value stored in the NI-RFSG waveform database. This VI uses the waveform name parameter as the key to retrieve the waveform property.
- [niRFSGPlayback Retrieve Waveform RF Blanking Enabled VI](../../../../instr-lib/nirfsgplayback/nirfsgplayback-retrieve-waveform-rf-blanking-enabled-vi.html) Returns the RF blanking enabled value stored in the NI-RFSG waveform database. The VI uses the waveform name parameter as the key to retrieve the waveform property.
- [niRFSGPlayback Retrieve Waveform RF Blanking Marker Source VI](../../../../instr-lib/nirfsgplayback/nirfsgplayback-retrieve-waveform-rf-blanking-marker-source-vi.html) Returns the RF blanking marker source stored in the NI-RFSG waveform database. This VI uses the waveform name as the key to retrieve the waveform property.
- [niRFSGPlayback Retrieve Waveform Burst Start Locations VI](../../../../instr-lib/nirfsgplayback/nirfsgplayback-retrieve-waveform-burst-start-locations-vi.html) Returns the burst start locations stored in the NI-RFSG waveform database. This VI uses the waveform name as the key to retrieve the waveform property.
- [niRFSGPlayback Retrieve Waveform Burst Stop Locations VI](../../../../instr-lib/nirfsgplayback/nirfsgplayback-retrieve-waveform-burst-stop-locations-vi.html) Returns the burst stop locations stored in the NI-RFSG waveform database. This VI uses the waveform name parameter as the key to retrieve the waveform property.
- [niRFSGPlayback Retrieve Waveform LO Offset Mode VI](../../../../instr-lib/nirfsgplayback/nirfsgplayback-retrieve-waveform-lo-offset-mode-vi.html) Returns the LO offset mode value stored in the NI-RFSG waveform database. This VI uses the waveform name parameter as the key to retrieve the waveform property.
- [niRFSGPlayback Retrieve Waveform Signal Bandwidth VI](../../../../instr-lib/nirfsgplayback/nirfsgplayback-retrieve-waveform-signal-bandwidth-vi.html) Returns the signal bandwidth stored in the NI-RFSG waveform database. This VI uses the waveform name parameter as the key to retrieve the waveform property.
- [niRFSGPlayback Retrieve Waveform Size VI](../../../../instr-lib/nirfsgplayback/nirfsgplayback-retrieve-waveform-size-vi.html) Returns the size of the waveform stored in the NI-RFSG waveform database. This VI uses the waveform name parameter as the key to retrieve the waveform property.
- [niRFSGPlayback Retrieve Downloaded Waveform Names VI](../../../../instr-lib/nirfsgplayback/nirfsgplayback-retrieve-downloaded-waveform-names-vi.html) Returns the names of the waveforms that are stored in the NI-RFSG waveform database.
- [niRFSGPlayback Retrieve Waveform File Version VI](../../../../instr-lib/nirfsgplayback/nirfsgplayback-retrieve-waveform-file-version-vi.html) Returns the waveform file version of the waveform stored in the NI-RFSG waveform database. This VI uses the waveform name parameter as the key to retrieve the waveform property.
- [niRFSGPlayback Retrieve Automatic SG SA Shared LO VI](../../../../instr-lib/nirfsgplayback/nirfsgplayback-retrieve-automatic-sg-sa-shared-lo-vi.html) Returns the value of automatic SG SA shared LO parameter.
- [Obsolete](../../../../menus/categories/measurement/nirfsgplayback/obsolete-mnu.html) The VIs on this palette are obsolete.

Parent topic:

NI-RFSG Playback Library

<!--NI_TOPIC bundle=rfsgplaybacklibrary-labview-api-ref path=menus/categories/measurement/nirfsgplayback/nirfsgplayback-utility-mnu.html language=enus -->
## TOPIC 00060: Utility

- bundle_id: `rfsgplaybacklibrary-labview-api-ref`
- source_path: `menus/categories/measurement/nirfsgplayback/nirfsgplayback-utility-mnu.html`
- source_url: https://docs-be.ni.com/bundle/rfsgplaybacklibrary-labview-api-ref/raw/resource/enus/menus/categories/measurement/nirfsgplayback/nirfsgplayback-utility-mnu.html
- document_id: `rfsgplaybacklibrary-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Use the VIs on this palette to configure utility features. icon

### Utility

Use the VIs on this palette to configure utility features.

[IMAGE alt='icon' src='nirfsgplayback-utility-mnu.png']

- [niRFSGPlayback Read Sample Rate From File VI](../../../../instr-lib/nirfsgplayback/nirfsgplayback-read-sample-rate-from-file-vi.html) Returns the sample rate stored in the file. This VI uses the waveform index as the key to retrieve the waveform property.
- [niRFSGPlayback Read PAPR From File VI](../../../../instr-lib/nirfsgplayback/nirfsgplayback-read-papr-from-file-vi.html) Returns the peak to average power ratio (PAPR) stored in the file. This VI uses the waveform index parameter as the key to read the waveform property.
- [niRFSGPlayback Read Runtime Scaling From File VI](../../../../instr-lib/nirfsgplayback/nirfsgplayback-read-runtime-scaling-from-file-vi.html) Returns the runtime scaling value stored in the file. This VI uses the waveform index parameter as the key to read the waveform property.
- [niRFSGPlayback Read RF Blanking Enabled From File VI](../../../../instr-lib/nirfsgplayback/nirfsgplayback-read-rf-blanking-enabled-from-file-vi.html) Returns the RF blanking enabled value stored in the file. This VI uses the waveform index parameter as the key to retrieve the waveform property.
- [niRFSGPlayback Read RF Blanking Marker Source From File VI](../../../../instr-lib/nirfsgplayback/nirfsgplayback-read-rf-blanking-marker-source-from-file-vi.html) Returns the RF blanking marker source stored in the file. This VI uses the waveform index parameter as the key to retrieve the waveform property.
- [niRFSGPlayback Read Burst Start Locations From File VI](../../../../instr-lib/nirfsgplayback/nirfsgplayback-read-burst-start-locations-from-file-vi.html) Returns the burst start locations stored in the file. This VI uses the waveform index parameter as the key to retrieve the waveform property.
- [niRFSGPlayback Read Burst Stop Locations From File VI](../../../../instr-lib/nirfsgplayback/nirfsgplayback-read-burst-stop-locations-from-file-vi.html) Returns the burst stop locations stored in the file. This VI uses the waveform index parameter as the key to retrieve the waveform property.
- [niRFSGPlayback Read Signal Bandwidth From File VI](../../../../instr-lib/nirfsgplayback/nirfsgplayback-read-signal-bandwidth-from-file-vi.html) Returns the signal bandwidth stored in the file. This VI uses the waveform index parameter as the key to retrieve the waveform property.
- [niRFSGPlayback Read Waveform Size From File VI](../../../../instr-lib/nirfsgplayback/nirfsgplayback-read-waveform-size-from-file-vi.html) Returns the size of the waveform stored in the file. This VI uses the waveform index parameter as the key to retrieve the waveform property.
- [niRFSGPlayback Read Waveform File Version From File VI](../../../../instr-lib/nirfsgplayback/nirfsgplayback-read-waveform-file-version-from-file-vi.html) Returns the waveform file version of the waveform stored in the file.
- [Obsolete](../../../../menus/categories/measurement/nirfsgplayback/obselete-utility-mnu.html) The VI on this palette is obsolete.

Parent topic:

NI-RFSG Playback Library

<!--NI_TOPIC bundle=rfsgplaybacklibrary-labview-api-ref path=menus/categories/measurement/nirfsgplayback/obselete-utility-mnu.html language=enus -->
## TOPIC 00061: Obsolete

- bundle_id: `rfsgplaybacklibrary-labview-api-ref`
- source_path: `menus/categories/measurement/nirfsgplayback/obselete-utility-mnu.html`
- source_url: https://docs-be.ni.com/bundle/rfsgplaybacklibrary-labview-api-ref/raw/resource/enus/menus/categories/measurement/nirfsgplayback/obselete-utility-mnu.html
- document_id: `rfsgplaybacklibrary-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: The VI on this palette is obsolete. icon

### Obsolete

The VI on this palette is obsolete.

[IMAGE alt='icon' src='obselete-utility-mnu.png']

- [niRFSGPlayback Read Peak Power Adjustment From File VI](../../../../instr-lib/nirfsgplayback/nirfsgplayback-read-peak-power-adjustment-from-file-vi.html) Returns the value of the peak power adjustment stored in the file. This VI uses the waveform index as the key to retrieve the waveform property.
- [niRFSGPlayback Read RF Blanking Marker Locations From File VI](../../../../instr-lib/nirfsgplayback/nirfsgplayback-read-rf-blanking-marker-locations-from-file-vi.html) Returns the RF blanking marker locations stored in the file. This VI uses the waveform index as the key to retrieve the waveform property.

Parent topic:

Utility

<!--NI_TOPIC bundle=rfsgplaybacklibrary-labview-api-ref path=menus/categories/measurement/nirfsgplayback/obsolete-mnu.html language=enus -->
## TOPIC 00062: Obsolete

- bundle_id: `rfsgplaybacklibrary-labview-api-ref`
- source_path: `menus/categories/measurement/nirfsgplayback/obsolete-mnu.html`
- source_url: https://docs-be.ni.com/bundle/rfsgplaybacklibrary-labview-api-ref/raw/resource/enus/menus/categories/measurement/nirfsgplayback/obsolete-mnu.html
- document_id: `rfsgplaybacklibrary-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: The VIs on this palette are obsolete. icon

### Obsolete

The VIs on this palette are obsolete.

[IMAGE alt='icon' src='obsolete-mnu.png']

- [niRFSGPlayback Store Waveform Peak Power Adjustment VI](../../../../instr-lib/nirfsgplayback/nirfsgplayback-store-waveform-peak-power-adjustment-vi.html) Stores the peak power adjustment, which you specify in the peak power adjustment parameter, in the NI-RFSG waveform database.
- [niRFSGPlayback Store Waveform RF Blanking Marker Locations VI](../../../../instr-lib/nirfsgplayback/nirfsgplayback-store-waveform-rf-blanking-marker-locations-vi.html) Stores the RF blanking marker positions, which you specify in the RF blanking marker locations parameter, in the NI-RFSG waveform database.
- [niRFSGPlayback Retrieve Waveform Peak Power Adjustment VI](../../../../instr-lib/nirfsgplayback/nirfsgplayback-retrieve-waveform-peak-power-adjustment-vi.html) Returns the peak power adjustment stored in the NI-RFSG waveform database. This VI uses the waveform name as the key to retrieve the waveform property.
- [niRFSGPlayback Retrieve Waveform RF Blanking Marker Locations VI](../../../../instr-lib/nirfsgplayback/nirfsgplayback-retrieve-waveform-rf-blanking-marker-locations-vi.html) Returns the RF blanking marker positions stored in the NI-RFSG waveform database. This VI uses the waveform name as the key to retrieve the waveform property.

Parent topic:

Advanced
