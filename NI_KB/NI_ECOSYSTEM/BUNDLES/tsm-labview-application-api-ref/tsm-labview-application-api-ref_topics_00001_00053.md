# NI DOCUMENT BUNDLE: tsm-labview-application-api-ref

<!--NI_BUNDLE_CHUNK bundle=tsm-labview-application-api-ref start=1 end=53 -->
<!--NI_TOPIC bundle=tsm-labview-application-api-ref path=menus/categories/ni-semiconductormodule/semiconductormodulemanager/lotdata/getbatchruntimedata-vi.html language=enus -->
## TOPIC 00001: Get Batch Runtime Data

- bundle_id: `tsm-labview-application-api-ref`
- source_path: `menus/categories/ni-semiconductormodule/semiconductormodulemanager/lotdata/getbatchruntimedata-vi.html`
- source_url: https://docs-be.ni.com/bundle/tsm-labview-application-api-ref/raw/resource/enus/menus/categories/ni-semiconductormodule/semiconductormodulemanager/lotdata/getbatchruntimedata-vi.html
- document_id: `tsm-labview-application-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the run-time data associated with the current batch. For more information, see the documentation for the IBatchRuntimeData interface in the Semiconductor Module Application API topic in the NI TestStand Semiconductor Module help. icon Inputs/Outputs coarn.png Semiconductor Module Manager Semico

### Get Batch Runtime Data

Gets the run-time data associated with the current batch. For more information, see the documentation for the IBatchRuntimeData interface in the Semiconductor Module Application API topic in the NI TestStand Semiconductor Module help.

[IMAGE alt='icon' src='getbatchruntimedata-vi.png']

#### Inputs/Outputs

| Semiconductor Module Manager — Semiconductor Module Manager is a valid ActiveX reference to a Semiconductor Module Manager object. error in (no error) — describes error conditions that occur before this VI or function runs. The default is no error. If an error occurred before this VI or function runs, the VI or function passes the error in (no error) Semiconductor Module Manager (out) — returns the Semiconductor Module Manager parameter unchanged. Batch Runtime Data — Contains run-time data for the current batch of parts being tested. Start of Test Time — The time that the the site starts testing after the tester sends the start-of-test (SOT) signal to the handler/prober driver. When using the Batch process model, this value is the same for all test sites and is valid in the Model Plugin - Pre Batch entry point and later. When using the Sequential and Parallel process models, this property value is valid in the Model Plugin - Pre UUT entry point and later. End of Test Time — The time that the site ended testing before the tester sends the end-of-test (EOT) signal to the handler/prober driver. When using the Batch process model, this value is the same for all test sites and is valid in the Model Plugin - Batch Done entry point and later. It is not valid in the Model Plugin - UUT Done entry point. Is Start Of Wafer? — Returns true if the current batch is the first batch of parts of a new wafer. This property remains true if the first batch of parts are retested. When using the Batch process model, this property value is valid in the Model Plugin - Pre Batch entry point and later. When using the Sequential process model, this property value is valid in the Model Plugin - Pre UUT entry point and later. IsEndOfWafer — Returns true if the current batch is the last batch of parts of the current wafer. This property is true after the prober driver indicates that it has tested the last die on the wafer. When using the Batch process model, this property value is valid in the Model Plugin - Batch Done entry point and later. When using the Sequential process model, this property value is valid in the Model Plugin - UUT Done entry point and later. Is Retesting? — Returns true if the tester is currently retesting the same part on the site because the operator requested a retest. When using the Batch process model, this property value is the same for all test sites and is valid in the Model Plugin - Pre Batch entry point and beyond. When using other process models, this property value is valid in the Model Plugin - Pre UUT entry point and beyond. Will Retest? — Returns true if the tester will retest the current part on the site because the operator requested a retest. When using the Batch process model, this property value is the same for all test sites and is valid in the Model Plugin - Batch Done entry point and beyond. When using other process models, this property value is valid in the Model Plugin - UUT Done entry point and beyond. error out — contains error information. If error in indicates that an error occurred before this VI or function ran, error out contains the same error information. Otherwise, it describes the error status that this VI or function produces. Right-click the error out front panel indicator and select Explain Error from the shortcut menu for more information about the error. |
| --- |
| Start of Test Time — The time that the the site starts testing after the tester sends the start-of-test (SOT) signal to the handler/prober driver. When using the Batch process model, this value is the same for all test sites and is valid in the Model Plugin - Pre Batch entry point and later. When using the Sequential and Parallel process models, this property value is valid in the Model Plugin - Pre UUT entry point and later. End of Test Time — The time that the site ended testing before the tester sends the end-of-test (EOT) signal to the handler/prober driver. When using the Batch process model, this value is the same for all test sites and is valid in the Model Plugin - Batch Done entry point and later. It is not valid in the Model Plugin - UUT Done entry point. Is Start Of Wafer? — Returns true if the current batch is the first batch of parts of a new wafer. This property remains true if the first batch of parts are retested. When using the Batch process model, this property value is valid in the Model Plugin - Pre Batch entry point and later. When using the Sequential process model, this property value is valid in the Model Plugin - Pre UUT entry point and later. IsEndOfWafer — Returns true if the current batch is the last batch of parts of the current wafer. This property is true after the prober driver indicates that it has tested the last die on the wafer. When using the Batch process model, this property value is valid in the Model Plugin - Batch Done entry point and later. When using the Sequential process model, this property value is valid in the Model Plugin - UUT Done entry point and later. Is Retesting? — Returns true if the tester is currently retesting the same part on the site because the operator requested a retest. When using the Batch process model, this property value is the same for all test sites and is valid in the Model Plugin - Pre Batch entry point and beyond. When using other process models, this property value is valid in the Model Plugin - Pre UUT entry point and beyond. Will Retest? — Returns true if the tester will retest the current part on the site because the operator requested a retest. When using the Batch process model, this property value is the same for all test sites and is valid in the Model Plugin - Batch Done entry point and beyond. When using other process models, this property value is valid in the Model Plugin - UUT Done entry point and beyond. |

Parent topic:

Lot Data

<!--NI_TOPIC bundle=tsm-labview-application-api-ref path=menus/categories/ni-semiconductormodule/semiconductormodulemanager/lotdata/getcsvtestresultslogfilepaths-vi.html language=enus -->
## TOPIC 00002: Get CSV Test Results Log File Paths

- bundle_id: `tsm-labview-application-api-ref`
- source_path: `menus/categories/ni-semiconductormodule/semiconductormodulemanager/lotdata/getcsvtestresultslogfilepaths-vi.html`
- source_url: https://docs-be.ni.com/bundle/tsm-labview-application-api-ref/raw/resource/enus/menus/categories/ni-semiconductormodule/semiconductormodulemanager/lotdata/getcsvtestresultslogfilepaths-vi.html
- document_id: `tsm-labview-application-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the absolute file paths of all CSV test results logs generated for the current lot. icon Inputs/Outputs coarn.png Semiconductor Module Manager Semiconductor Module Manager is a valid ActiveX reference to a Semiconductor Module Manager object. cerrcodeclst.png error in (no error) describes er

### Get CSV Test Results Log File Paths

Returns the absolute file paths of all CSV test results logs generated for the current lot.

[IMAGE alt='icon' src='getcsvtestresultslogfilepaths-vi.png']

#### Inputs/Outputs

| Semiconductor Module Manager — Semiconductor Module Manager is a valid ActiveX reference to a Semiconductor Module Manager object. error in (no error) — describes error conditions that occur before this VI or function runs. The default is no error. If an error occurred before this VI or function runs, the VI or function passes the error in (no error) Semiconductor Module Manager Out — returns the Semiconductor Module Manager parameter unchanged. Current CSV Test Results Log File — returns the absolute file path of the last CSV test results log generated for the current lot. All CSV Test Results Log Files for Lot — returns the absolute file paths of all CSV test results logs generated for the current lot. If the Generate One File per Wafer option is enabled, the size of the array is the number of wafers processed in the lot so far. Otherwise, the array has just one element. error out — contains error information. If error in indicates that an error occurred before this VI or function ran, error out contains the same error information. Otherwise, it describes the error status that this VI or function produces. Right-click the error out front panel indicator and select Explain Error from the shortcut menu for more information about the error. |
| --- |

Parent topic:

Lot Data

<!--NI_TOPIC bundle=tsm-labview-application-api-ref path=menus/categories/ni-semiconductormodule/semiconductormodulemanager/lotdata/gethardwarebinnumbers-vi.html language=enus -->
## TOPIC 00003: Get Hardware Bin Numbers

- bundle_id: `tsm-labview-application-api-ref`
- source_path: `menus/categories/ni-semiconductormodule/semiconductormodulemanager/lotdata/gethardwarebinnumbers-vi.html`
- source_url: https://docs-be.ni.com/bundle/tsm-labview-application-api-ref/raw/resource/enus/menus/categories/ni-semiconductormodule/semiconductormodulemanager/lotdata/gethardwarebinnumbers-vi.html
- document_id: `tsm-labview-application-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the bin numbers for each hardware bin in the lot the Lot Statistics parameter specifies. icon Inputs/Outputs coarn.png Lot Statistics Lot Statistics is a valid ActiveX reference to a Lot Statistics object. cerrcodeclst.png error in (no error) describes error conditions that occur before this

### Get Hardware Bin Numbers

Returns the bin numbers for each hardware bin in the lot the **Lot Statistics** parameter specifies.

[IMAGE alt='icon' src='gethardwarebinnumbers-vi.png']

#### Inputs/Outputs

| Lot Statistics — Lot Statistics is a valid ActiveX reference to a Lot Statistics object. error in (no error) — describes error conditions that occur before this VI or function runs. The default is no error. If an error occurred before this VI or function runs, the VI or function passes the error in (no error) Lot Statistics (out) — returns the Lot Statistics parameter unchanged. Hardware Bin Numbers — returns a one-dimensional array of data with one element for each hardware bin in the lot. error out — contains error information. If error in indicates that an error occurred before this VI or function ran, error out contains the same error information. Otherwise, it describes the error status that this VI or function produces. Right-click the error out front panel indicator and select Explain Error from the shortcut menu for more information about the error. |
| --- |

Parent topic:

Lot Data

<!--NI_TOPIC bundle=tsm-labview-application-api-ref path=menus/categories/ni-semiconductormodule/semiconductormodulemanager/lotdata/gethardwarebinstatistics-vi.html language=enus -->
## TOPIC 00004: Get Hardware Bin Statistics

- bundle_id: `tsm-labview-application-api-ref`
- source_path: `menus/categories/ni-semiconductormodule/semiconductormodulemanager/lotdata/gethardwarebinstatistics-vi.html`
- source_url: https://docs-be.ni.com/bundle/tsm-labview-application-api-ref/raw/resource/enus/menus/categories/ni-semiconductormodule/semiconductormodulemanager/lotdata/gethardwarebinstatistics-vi.html
- document_id: `tsm-labview-application-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the bin statistics data for the hardware bin the Bin parameter specifies. icon Inputs/Outputs coarn.png Lot Statistics Lot Statistics is a valid ActiveX reference to a Lot Statistics object. cu16.png Bin Bin is the bin number of the hardware bin for which to retrieve data. Use the Get Hardwa

### Get Hardware Bin Statistics

Returns the bin statistics data for the hardware bin the **Bin** parameter specifies.

[IMAGE alt='icon' src='gethardwarebinstatistics-vi.png']

#### Inputs/Outputs

| Lot Statistics — Lot Statistics is a valid ActiveX reference to a Lot Statistics object. Bin — Bin is the bin number of the hardware bin for which to retrieve data. Use the Get Hardware Bin Numbers VI to obtain hardware bin numbers for a given lot. error in (no error) — describes error conditions that occur before this VI or function runs. The default is no error. If an error occurred before this VI or function runs, the VI or function passes the error in (no error) Part Count — returns the number of parts in the bin the Bin parameter specifies. Lot Statistics (out) — returns the Lot Statistics parameter unchanged. Bin Name — returns the name of the bin the Bin parameter specifies. Bin Number — returns the bin number for the bin the Bin parameter specifies. Bin Type — returns the type of bin the Bin parameter specifies. error out — contains error information. If error in indicates that an error occurred before this VI or function ran, error out contains the same error information. Otherwise, it describes the error status that this VI or function produces. Right-click the error out front panel indicator and select Explain Error from the shortcut menu for more information about the error. |
| --- |

Parent topic:

Lot Data

<!--NI_TOPIC bundle=tsm-labview-application-api-ref path=menus/categories/ni-semiconductormodule/semiconductormodulemanager/lotdata/getinlineqapartcountstatistics-vi.html language=enus -->
## TOPIC 00005: Get Inline QA Part Count Statistics

- bundle_id: `tsm-labview-application-api-ref`
- source_path: `menus/categories/ni-semiconductormodule/semiconductormodulemanager/lotdata/getinlineqapartcountstatistics-vi.html`
- source_url: https://docs-be.ni.com/bundle/tsm-labview-application-api-ref/raw/resource/enus/menus/categories/ni-semiconductormodule/semiconductormodulemanager/lotdata/getinlineqapartcountstatistics-vi.html
- document_id: `tsm-labview-application-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns statistical part count data for parts tested with Inline QA enabled. icon Inputs/Outputs coarn.png Lot Statistics Lot Statistics is a valid ActiveX reference to a Lot Statistics object. cerrcodeclst.png error in (no error) describes error conditions that occur before this VI or function runs

### Get Inline QA Part Count Statistics

Returns statistical part count data for parts tested with Inline QA enabled.

[IMAGE alt='icon' src='getinlineqapartcountstatistics-vi.png']

#### Inputs/Outputs

| Lot Statistics — Lot Statistics is a valid ActiveX reference to a Lot Statistics object. error in (no error) — describes error conditions that occur before this VI or function runs. The default is no error. If an error occurred before this VI or function runs, the VI or function passes the error in (no error) Total — returns the total number of parts tested. Lot Statistics (out) — returns the Lot Statistics parameter unchanged. Passed — returns the total number of parts passed. Failed — returns the total number of parts failed. Other — returns the total number of parts that neither passed nor failed. error out — contains error information. If error in indicates that an error occurred before this VI or function ran, error out contains the same error information. Otherwise, it describes the error status that this VI or function produces. Right-click the error out front panel indicator and select Explain Error from the shortcut menu for more information about the error. |
| --- |

Parent topic:

Lot Data

<!--NI_TOPIC bundle=tsm-labview-application-api-ref path=menus/categories/ni-semiconductormodule/semiconductormodulemanager/lotdata/getlotsummaryreportfilepaths-vi.html language=enus -->
## TOPIC 00006: Get Lot Summary Report File Paths

- bundle_id: `tsm-labview-application-api-ref`
- source_path: `menus/categories/ni-semiconductormodule/semiconductormodulemanager/lotdata/getlotsummaryreportfilepaths-vi.html`
- source_url: https://docs-be.ni.com/bundle/tsm-labview-application-api-ref/raw/resource/enus/menus/categories/ni-semiconductormodule/semiconductormodulemanager/lotdata/getlotsummaryreportfilepaths-vi.html
- document_id: `tsm-labview-application-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the absolute file paths of all Lot Summary reports generated for the current lot. icon Inputs/Outputs coarn.png Semiconductor Module Manager Semiconductor Module Manager is a valid ActiveX reference to a Semiconductor Module Manager object. cerrcodeclst.png error in (no error) describes erro

### Get Lot Summary Report File Paths

Returns the absolute file paths of all Lot Summary reports generated for the current lot.

[IMAGE alt='icon' src='getlotsummaryreportfilepaths-vi.png']

#### Inputs/Outputs

| Semiconductor Module Manager — Semiconductor Module Manager is a valid ActiveX reference to a Semiconductor Module Manager object. error in (no error) — describes error conditions that occur before this VI or function runs. The default is no error. If an error occurred before this VI or function runs, the VI or function passes the error in (no error) Semiconductor Module Manager Out — returns the Semiconductor Module Manager parameter unchanged. Current Lot Summary Report File — Returns the absolute file path of the last Lot Summary report generated for the current lot. All Lot Summary Report Files for Lot — returns the absolute file paths of all Lot Summary reports generated for the current lot. If the Generate One File per Wafer option is enabled, the size of the array is the number of wafers processed in the lot so far. Otherwise, the array has just one element. error out — contains error information. If error in indicates that an error occurred before this VI or function ran, error out contains the same error information. Otherwise, it describes the error status that this VI or function produces. Right-click the error out front panel indicator and select Explain Error from the shortcut menu for more information about the error. |
| --- |

Parent topic:

Lot Data

<!--NI_TOPIC bundle=tsm-labview-application-api-ref path=menus/categories/ni-semiconductormodule/semiconductormodulemanager/lotdata/getpartcountstatistics-vi.html language=enus -->
## TOPIC 00007: Get Part Count Statistics

- bundle_id: `tsm-labview-application-api-ref`
- source_path: `menus/categories/ni-semiconductormodule/semiconductormodulemanager/lotdata/getpartcountstatistics-vi.html`
- source_url: https://docs-be.ni.com/bundle/tsm-labview-application-api-ref/raw/resource/enus/menus/categories/ni-semiconductormodule/semiconductormodulemanager/lotdata/getpartcountstatistics-vi.html
- document_id: `tsm-labview-application-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns statistical part count data for parts tested. icon Inputs/Outputs coarn.png Lot Statistics Lot Statistics is a valid ActiveX reference to a Lot Statistics object. cerrcodeclst.png error in (no error) describes error conditions that occur before this VI or function runs. The default is no err

### Get Part Count Statistics

Returns statistical part count data for parts tested.

[IMAGE alt='icon' src='getpartcountstatistics-vi.png']

#### Inputs/Outputs

| Lot Statistics — Lot Statistics is a valid ActiveX reference to a Lot Statistics object. error in (no error) — describes error conditions that occur before this VI or function runs. The default is no error. If an error occurred before this VI or function runs, the VI or function passes the error in (no error) Total — returns the total number of parts tested. Lot Statistics (out) — returns the Lot Statistics parameter unchanged. Passed — returns the total number of parts passed. Failed — returns the total number of parts failed. Other — returns the total number of parts that neither passed nor failed. error out — Contains error information. If error in indicates that an error occurred before this VI or function ran, error out contains the same error information. Otherwise, it describes the error status that this VI or function produces. Right-click the error out front panel indicator and select Explain Error from the shortcut menu for more information about the error. Retested — returns the total number of parts retested one or more times. If a part is retested on multiple sites, this property is set only for the site that first retested the part. |
| --- |

Parent topic:

Lot Data

<!--NI_TOPIC bundle=tsm-labview-application-api-ref path=menus/categories/ni-semiconductormodule/semiconductormodulemanager/lotdata/getsemiconductormodulemanager-vi.html language=enus -->
## TOPIC 00008: Get Semiconductor Module Manager

- bundle_id: `tsm-labview-application-api-ref`
- source_path: `menus/categories/ni-semiconductormodule/semiconductormodulemanager/lotdata/getsemiconductormodulemanager-vi.html`
- source_url: https://docs-be.ni.com/bundle/tsm-labview-application-api-ref/raw/resource/enus/menus/categories/ni-semiconductormodule/semiconductormodulemanager/lotdata/getsemiconductormodulemanager-vi.html
- document_id: `tsm-labview-application-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the existing Semiconductor Module Manager object. icon Inputs/Outputs coarn.png TestStand Engine TestStand Engine is an ActiveX reference to the TestStand Engine object. cerrcodeclst.png error in (no error) describes error conditions that occur before this VI or function runs. The default is no

### Get Semiconductor Module Manager

Gets the existing Semiconductor Module Manager object.

[IMAGE alt='icon' src='getsemiconductormodulemanager-vi.png']

#### Inputs/Outputs

| TestStand Engine — TestStand Engine is an ActiveX reference to the TestStand Engine object. error in (no error) — describes error conditions that occur before this VI or function runs. The default is no error. If an error occurred before this VI or function runs, the VI or function passes the error in (no error) Semiconductor Module Manager Out — returns the Semiconductor Module Manager that the VI creates. error out — contains error information. If error in indicates that an error occurred before this VI or function ran, error out contains the same error information. Otherwise, it describes the error status that this VI or function produces. Right-click the error out front panel indicator and select Explain Error from the shortcut menu for more information about the error. |
| --- |

Parent topic:

Lot Data

<!--NI_TOPIC bundle=tsm-labview-application-api-ref path=menus/categories/ni-semiconductormodule/semiconductormodulemanager/lotdata/getsitelotstatistics-vi.html language=enus -->
## TOPIC 00009: Get Site Lot Statistics

- bundle_id: `tsm-labview-application-api-ref`
- source_path: `menus/categories/ni-semiconductormodule/semiconductormodulemanager/lotdata/getsitelotstatistics-vi.html`
- source_url: https://docs-be.ni.com/bundle/tsm-labview-application-api-ref/raw/resource/enus/menus/categories/ni-semiconductormodule/semiconductormodulemanager/lotdata/getsitelotstatistics-vi.html
- document_id: `tsm-labview-application-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the lot statistics objects for each site. If the lot has not yet been configured, the statistics objects contain empty data (no bin data, and part counts are 0). When you configure the lot, the SemiconductorModuleManager creates new statistics objects that contain valid bin numbers, but all

### Get Site Lot Statistics

Returns the lot statistics objects for each site. If the lot has not yet been configured, the statistics objects contain empty data (no bin data, and part counts are 0). When you configure the lot, the SemiconductorModuleManager creates new statistics objects that contain valid bin numbers, but all part counts are set to 0. The statistics objects remain valid during testing and after testing is complete until you configure a new lot.

[IMAGE alt='icon' src='getsitelotstatistics-vi.png']

#### Inputs/Outputs

| Semiconductor Module Manager — Semiconductor Module Manager is a valid ActiveX reference to a Semiconductor Module Manager object. error in (no error) — describes error conditions that occur before this VI or function runs. The default is no error. If an error occurred before this VI or function runs, the VI or function passes the error in (no error) Semiconductor Module Manager (out) — returns the Semiconductor Module Manager parameter unchanged. Site Lot Statistics — is an array that contains the lot statistics objects for each site. error out — contains error information. If error in indicates that an error occurred before this VI or function ran, error out contains the same error information. Otherwise, it describes the error status that this VI or function produces. Right-click the error out front panel indicator and select Explain Error from the shortcut menu for more information about the error. |
| --- |

Parent topic:

Lot Data

<!--NI_TOPIC bundle=tsm-labview-application-api-ref path=menus/categories/ni-semiconductormodule/semiconductormodulemanager/lotdata/getsiteruntimedata-vi.html language=enus -->
## TOPIC 00010: Get Site Runtime Data

- bundle_id: `tsm-labview-application-api-ref`
- source_path: `menus/categories/ni-semiconductormodule/semiconductormodulemanager/lotdata/getsiteruntimedata-vi.html`
- source_url: https://docs-be.ni.com/bundle/tsm-labview-application-api-ref/raw/resource/enus/menus/categories/ni-semiconductormodule/semiconductormodulemanager/lotdata/getsiteruntimedata-vi.html
- document_id: `tsm-labview-application-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the run-time data associated with the current site. For more information, see the documentation for the ISiteRuntimeData interface in the Semiconductor Module Application API topic in the NI TestStand Semiconductor Module help. icon Inputs/Outputs coarn.png Semiconductor Module Manager Semicond

### Get Site Runtime Data

Gets the run-time data associated with the current site. For more information, see the documentation for the ISiteRuntimeData interface in the Semiconductor Module Application API topic in the NI TestStand Semiconductor Module help.

[IMAGE alt='icon' src='getsiteruntimedata-vi.png']

#### Inputs/Outputs

| Semiconductor Module Manager — Semiconductor Module Manager is a valid ActiveX reference to a Semiconductor Module Manager object. Site index — Site index is a zero-based index that specifies the site for which runtime data is returned. error in (no error) — describes error conditions that occur before this VI or function runs. The default is no error. If an error occurred before this VI or function runs, the VI or function passes the error in (no error) Semiconductor Module Manager (out) — returns the Semiconductor Module Manager parameter unchanged. Site Runtime Data — Contains run-time data for a specific test site. Start of Test Time — The time that the the site starts testing after the tester sends the start-of-test (SOT) signal to the handler/prober driver. When using the Batch process model, this value is the same for all test sites and is valid in the Model Plugin - Pre Batch entry point and later. When using the Sequential and Parallel process models, this property value is valid in the Model Plugin - Pre UUT entry point and later. End of Test Time — The time that the site ended testing before the tester sends the end-of-test (EOT) signal to the handler/prober driver. When using the Batch process model, this value is the same for all test sites and is valid in the Model Plugin - Batch Done entry point and later. It is not valid in the Model Plugin - UUT Done entry point. Test Time in Seconds — Returns the time to execute the MainSequence sequence for the last part that was tested on this site. This property value is valid in the Model Plugin - UUT Done entry point and beyond. Is Testing? — When called before the end-of-test, returns true if the site is currently testing a part. When called after the end-of-test, returns true if the site tested a part in the most recent batch. This value is false if the handler/prober driver indicated that the test site is not testing parts. When using the Batch process model, this value is valid in the Model Plugin - Pre Batch entry point and later. When using the Sequential and Parallel process models, this property value is valid in the Model Plugin - Pre UUT entry point and later. Will Retest? — Returns true if the tester will retest the current part on the site because the operator requested a retest. When using the Batch process model, this property value is the same for all test sites and is valid in the Model Plugin - Batch Done entry point and beyond. When using other process models, this property value is valid in the Model Plugin - UUT Done entry point and beyond. Is Retesting? — Returns true if the tester is currently retesting the same part on the site because the operator requested a retest. When using the Batch process model, this property value is the same for all test sites and is valid in the Model Plugin - Pre Batch entry point and beyond. When using other process models, this property value is valid in the Model Plugin - Pre UUT entry point and beyond. Site Number — Returns the site number that the run-time data is associated with. Part Id — Returns the part identifier for the current part being tested on this site. The handler/prober driver sets this property value by setting values in the SitePartIds parameter in the StartOfTest handler driver entry point sequence. If the handler/prober driver does not set this property, the tester sets the value to a unique value if the GenerateUniquePartIds station settings is set to true. Part Text — Returns the part description text for the current part being tested on this site. The handler/prober driver sets this property value by setting values in the SitePartTexts parameter in the StartOfTest handler driver entry point sequence. Die Coordinate X — Returns the X wafer coordinate of the current die being tested on this site. The handler/prober driver sets this property value by setting values in the WaferRuntimeData.SiteDieCoordinates parameter in the StartOfTest handler driver entry point sequence. Die Coordinate Y — Returns the Y wafer coordinate of the current die being tested on this site. The handler/prober driver sets this property value by setting values in the WaferRuntimeData.SiteDieCoordinates parameter in the StartOfTest handler driver entry point sequence. This property corresponds to the Y_COORD field in the Part Results Record (PRR) in the STDF data log. When using the Batch process model, this property value is valid in the Model Plugin - Pre Batch entry point and later. When using the Sequential process model, this property value is valid in the Model Plugin - Pre UUT entry point and later. Is Inline QA Enabled? — Returns true if an InlineQA step executed its block of steps for this site. Use this property to determine whether InlineQA tests were run for last part that was tested on this site. An InlineQA step executes its block of steps when the InlineQA station settings is true and the InlineQA algorithm sequence file selects the current part to run InlineQA tests. Hardware Bin Number — Returns the number of the hardware bin that the tester assigned to the last part that was tested on this site. Returns -1 if the tester has not yet assigned a bin to the part or a value between 0 and 65535 if the bin was assigned. This property value is valid in the Model Plugin - UUT Done entry point and later. Hardware Bin Name — Returns the name of the hardware bin that the tester assigned to the last part that was tested on this site. This property value is valid in the Model Plugin - UUT Done entry point and later. Software Bin Number — Returns the number of the software bin that the tester assigned to the last part that was tested on this site. Returns -1 if the tester has not yet assigned a bin to the part or a value between 0 and 65535 if the bin was assigned. This property value is valid in the Model Plugin - UUT Done entry point and later. Software Bin Name — Returns the name of the software bin that the tester assigned to the last part that was tested on this site. This property value is valid in the Model Plugin - UUT Done entry point and later. Bin Type — Returns the type of the bin that the tester assigned to the last part that was tested on this site. This property value is valid in the Model Plugin - UUT Done entry point and beyond. Is Duplicate Part Id? — Returns true if a part with the same part ID as the current part was tested previously in the current lot. When using the Batch process model, this property value is valid in the Model Plugin - Pre Batch entry point and later. When using the Sequential process model, this property value is valid in the Model Plugin - Pre UUT entry point and later. Is Duplicate Die Coordinates? — Returns true if a part with the same die coordinates as the current part was tested previously in the current wafer. When using the Batch process model, this property value is valid in the Model Plugin - Pre Batch entry point and later. When using the Sequential process model, this property value is valid in the Model Plugin - Pre UUT entry point and later. error out — contains error information. If error in indicates that an error occurred before this VI or function ran, error out contains the same error information. Otherwise, it describes the error status that this VI or function produces. Right-click the error out front panel indicator and select Explain Error from the shortcut menu for more information about the error. |
| --- |
| Start of Test Time — The time that the the site starts testing after the tester sends the start-of-test (SOT) signal to the handler/prober driver. When using the Batch process model, this value is the same for all test sites and is valid in the Model Plugin - Pre Batch entry point and later. When using the Sequential and Parallel process models, this property value is valid in the Model Plugin - Pre UUT entry point and later. End of Test Time — The time that the site ended testing before the tester sends the end-of-test (EOT) signal to the handler/prober driver. When using the Batch process model, this value is the same for all test sites and is valid in the Model Plugin - Batch Done entry point and later. It is not valid in the Model Plugin - UUT Done entry point. Test Time in Seconds — Returns the time to execute the MainSequence sequence for the last part that was tested on this site. This property value is valid in the Model Plugin - UUT Done entry point and beyond. Is Testing? — When called before the end-of-test, returns true if the site is currently testing a part. When called after the end-of-test, returns true if the site tested a part in the most recent batch. This value is false if the handler/prober driver indicated that the test site is not testing parts. When using the Batch process model, this value is valid in the Model Plugin - Pre Batch entry point and later. When using the Sequential and Parallel process models, this property value is valid in the Model Plugin - Pre UUT entry point and later. Will Retest? — Returns true if the tester will retest the current part on the site because the operator requested a retest. When using the Batch process model, this property value is the same for all test sites and is valid in the Model Plugin - Batch Done entry point and beyond. When using other process models, this property value is valid in the Model Plugin - UUT Done entry point and beyond. Is Retesting? — Returns true if the tester is currently retesting the same part on the site because the operator requested a retest. When using the Batch process model, this property value is the same for all test sites and is valid in the Model Plugin - Pre Batch entry point and beyond. When using other process models, this property value is valid in the Model Plugin - Pre UUT entry point and beyond. Site Number — Returns the site number that the run-time data is associated with. Part Id — Returns the part identifier for the current part being tested on this site. The handler/prober driver sets this property value by setting values in the SitePartIds parameter in the StartOfTest handler driver entry point sequence. If the handler/prober driver does not set this property, the tester sets the value to a unique value if the GenerateUniquePartIds station settings is set to true. Part Text — Returns the part description text for the current part being tested on this site. The handler/prober driver sets this property value by setting values in the SitePartTexts parameter in the StartOfTest handler driver entry point sequence. Die Coordinate X — Returns the X wafer coordinate of the current die being tested on this site. The handler/prober driver sets this property value by setting values in the WaferRuntimeData.SiteDieCoordinates parameter in the StartOfTest handler driver entry point sequence. Die Coordinate Y — Returns the Y wafer coordinate of the current die being tested on this site. The handler/prober driver sets this property value by setting values in the WaferRuntimeData.SiteDieCoordinates parameter in the StartOfTest handler driver entry point sequence. This property corresponds to the Y_COORD field in the Part Results Record (PRR) in the STDF data log. When using the Batch process model, this property value is valid in the Model Plugin - Pre Batch entry point and later. When using the Sequential process model, this property value is valid in the Model Plugin - Pre UUT entry point and later. Is Inline QA Enabled? — Returns true if an InlineQA step executed its block of steps for this site. Use this property to determine whether InlineQA tests were run for last part that was tested on this site. An InlineQA step executes its block of steps when the InlineQA station settings is true and the InlineQA algorithm sequence file selects the current part to run InlineQA tests. Hardware Bin Number — Returns the number of the hardware bin that the tester assigned to the last part that was tested on this site. Returns -1 if the tester has not yet assigned a bin to the part or a value between 0 and 65535 if the bin was assigned. This property value is valid in the Model Plugin - UUT Done entry point and later. Hardware Bin Name — Returns the name of the hardware bin that the tester assigned to the last part that was tested on this site. This property value is valid in the Model Plugin - UUT Done entry point and later. Software Bin Number — Returns the number of the software bin that the tester assigned to the last part that was tested on this site. Returns -1 if the tester has not yet assigned a bin to the part or a value between 0 and 65535 if the bin was assigned. This property value is valid in the Model Plugin - UUT Done entry point and later. Software Bin Name — Returns the name of the software bin that the tester assigned to the last part that was tested on this site. This property value is valid in the Model Plugin - UUT Done entry point and later. Bin Type — Returns the type of the bin that the tester assigned to the last part that was tested on this site. This property value is valid in the Model Plugin - UUT Done entry point and beyond. Is Duplicate Part Id? — Returns true if a part with the same part ID as the current part was tested previously in the current lot. When using the Batch process model, this property value is valid in the Model Plugin - Pre Batch entry point and later. When using the Sequential process model, this property value is valid in the Model Plugin - Pre UUT entry point and later. Is Duplicate Die Coordinates? — Returns true if a part with the same die coordinates as the current part was tested previously in the current wafer. When using the Batch process model, this property value is valid in the Model Plugin - Pre Batch entry point and later. When using the Sequential process model, this property value is valid in the Model Plugin - Pre UUT entry point and later. |

Parent topic:

Lot Data

<!--NI_TOPIC bundle=tsm-labview-application-api-ref path=menus/categories/ni-semiconductormodule/semiconductormodulemanager/lotdata/getsoftwarebinnumbers-vi.html language=enus -->
## TOPIC 00011: Get Software Bin Numbers

- bundle_id: `tsm-labview-application-api-ref`
- source_path: `menus/categories/ni-semiconductormodule/semiconductormodulemanager/lotdata/getsoftwarebinnumbers-vi.html`
- source_url: https://docs-be.ni.com/bundle/tsm-labview-application-api-ref/raw/resource/enus/menus/categories/ni-semiconductormodule/semiconductormodulemanager/lotdata/getsoftwarebinnumbers-vi.html
- document_id: `tsm-labview-application-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the bin numbers for each software bin in the lot the Lot Statistics parameter specifies. icon Inputs/Outputs coarn.png Lot Statistics Lot Statistics is a valid ActiveX reference to a Lot Statistics object. cerrcodeclst.png error in (no error) describes error conditions that occur before this

### Get Software Bin Numbers

Returns the bin numbers for each software bin in the lot the **Lot Statistics** parameter specifies.

[IMAGE alt='icon' src='getsoftwarebinnumbers-vi.png']

#### Inputs/Outputs

| Lot Statistics — Lot Statistics is a valid ActiveX reference to a Lot Statistics object. error in (no error) — describes error conditions that occur before this VI or function runs. The default is no error. If an error occurred before this VI or function runs, the VI or function passes the error in (no error) Lot Statistics (out) — returns the Lot Statistics parameter unchanged. Software Bin Numbers — returns a one-dimensional array of data with one element for each software bin in the lot. error out — contains error information. If error in indicates that an error occurred before this VI or function ran, error out contains the same error information. Otherwise, it describes the error status that this VI or function produces. Right-click the error out front panel indicator and select Explain Error from the shortcut menu for more information about the error. |
| --- |

Parent topic:

Lot Data

<!--NI_TOPIC bundle=tsm-labview-application-api-ref path=menus/categories/ni-semiconductormodule/semiconductormodulemanager/lotdata/getsoftwarebinnumbersbycount-vi.html language=enus -->
## TOPIC 00012: Get Software Bin Numbers By Count

- bundle_id: `tsm-labview-application-api-ref`
- source_path: `menus/categories/ni-semiconductormodule/semiconductormodulemanager/lotdata/getsoftwarebinnumbersbycount-vi.html`
- source_url: https://docs-be.ni.com/bundle/tsm-labview-application-api-ref/raw/resource/enus/menus/categories/ni-semiconductormodule/semiconductormodulemanager/lotdata/getsoftwarebinnumbersbycount-vi.html
- document_id: `tsm-labview-application-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the bin numbers for each software bin in the lot the Lot Statistics parameter specifies, sorted in descending order by the part count per bin. icon Inputs/Outputs coarn.png Lot Statistics Lot Statistics is a valid ActiveX reference to a Lot Statistics object. cerrcodeclst.png error in (no er

### Get Software Bin Numbers By Count

Returns the bin numbers for each software bin in the lot the **Lot Statistics** parameter specifies, sorted in descending order by the part count per bin.

[IMAGE alt='icon' src='getsoftwarebinnumbersbycount-vi.png']

#### Inputs/Outputs

| Lot Statistics — Lot Statistics is a valid ActiveX reference to a Lot Statistics object. error in (no error) — describes error conditions that occur before this VI or function runs. The default is no error. If an error occurred before this VI or function runs, the VI or function passes the error in (no error) Lot Statistics (out) — returns the Lot Statistics parameter unchanged. Software Bin Numbers — returns a one-dimensional array of data with one element for each software bin in the lot. The array is sorted in descending order corresponding to the part count per bin. error out — contains error information. If error in indicates that an error occurred before this VI or function ran, error out contains the same error information. Otherwise, it describes the error status that this VI or function produces. Right-click the error out front panel indicator and select Explain Error from the shortcut menu for more information about the error. |
| --- |

Parent topic:

Lot Data

<!--NI_TOPIC bundle=tsm-labview-application-api-ref path=menus/categories/ni-semiconductormodule/semiconductormodulemanager/lotdata/getsoftwarebinstatistics-vi.html language=enus -->
## TOPIC 00013: Get Software Bin Statistics

- bundle_id: `tsm-labview-application-api-ref`
- source_path: `menus/categories/ni-semiconductormodule/semiconductormodulemanager/lotdata/getsoftwarebinstatistics-vi.html`
- source_url: https://docs-be.ni.com/bundle/tsm-labview-application-api-ref/raw/resource/enus/menus/categories/ni-semiconductormodule/semiconductormodulemanager/lotdata/getsoftwarebinstatistics-vi.html
- document_id: `tsm-labview-application-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the bin statistics data for the software bin the Bin parameter specifies. icon Inputs/Outputs coarn.png Lot Statistics Lot Statistics is a valid ActiveX reference to a Lot Statistics object. cu16.png Bin Bin is the bin number of the hardware bin for which to retrieve data. Use the Get Hardwa

### Get Software Bin Statistics

Returns the bin statistics data for the software bin the **Bin** parameter specifies.

[IMAGE alt='icon' src='getsoftwarebinstatistics-vi.png']

#### Inputs/Outputs

| Lot Statistics — Lot Statistics is a valid ActiveX reference to a Lot Statistics object. Bin — Bin is the bin number of the hardware bin for which to retrieve data. Use the Get Hardware Bin Numbers VI to obtain hardware bin numbers for a given lot. error in (no error) — describes error conditions that occur before this VI or function runs. The default is no error. If an error occurred before this VI or function runs, the VI or function passes the error in (no error) Part Count — returns the number of parts in the bin the Bin parameter specifies. Lot Statistics (out) — returns the Lot Statistics parameter unchanged. Bin Name — returns the name of the bin the Bin parameter specifies. Bin Number — returns the bin number for the bin the Bin parameter specifies. Bin Type — returns the type of bin the Bin parameter specifies. error out — contains error information. If error in indicates that an error occurred before this VI or function ran, error out contains the same error information. Otherwise, it describes the error status that this VI or function produces. Right-click the error out front panel indicator and select Explain Error from the shortcut menu for more information about the error. Hardware Bin Number — returns the bin number of the hardware bin to which the specified software bin corresponds. |
| --- |

Parent topic:

Lot Data

<!--NI_TOPIC bundle=tsm-labview-application-api-ref path=menus/categories/ni-semiconductormodule/semiconductormodulemanager/lotdata/getstdflogfilepaths-vi.html language=enus -->
## TOPIC 00014: Get STDF Log File Paths

- bundle_id: `tsm-labview-application-api-ref`
- source_path: `menus/categories/ni-semiconductormodule/semiconductormodulemanager/lotdata/getstdflogfilepaths-vi.html`
- source_url: https://docs-be.ni.com/bundle/tsm-labview-application-api-ref/raw/resource/enus/menus/categories/ni-semiconductormodule/semiconductormodulemanager/lotdata/getstdflogfilepaths-vi.html
- document_id: `tsm-labview-application-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the absolute file paths of all STDF logs generated for the current lot. icon Inputs/Outputs coarn.png Semiconductor Module Manager Semiconductor Module Manager is a valid ActiveX reference to a Semiconductor Module Manager object. cerrcodeclst.png error in (no error) describes error conditio

### Get STDF Log File Paths

Returns the absolute file paths of all STDF logs generated for the current lot.

[IMAGE alt='icon' src='getstdflogfilepaths-vi.png']

#### Inputs/Outputs

| Semiconductor Module Manager — Semiconductor Module Manager is a valid ActiveX reference to a Semiconductor Module Manager object. error in (no error) — describes error conditions that occur before this VI or function runs. The default is no error. If an error occurred before this VI or function runs, the VI or function passes the error in (no error) Semiconductor Module Manager Out — returns the Semiconductor Module Manager parameter unchanged. Current STDF Log File — returns the absolute file path of the last STDF log generated for the current lot. All STDF Log Files for Lot — returns the absolute file paths of all STDF logs generated for the current lot. If the Generate One File per Wafer option is enabled, the size of the array is the number of wafers processed in the lot so far. Otherwise, the array has just one element. error out — contains error information. If error in indicates that an error occurred before this VI or function ran, error out contains the same error information. Otherwise, it describes the error status that this VI or function produces. Right-click the error out front panel indicator and select Explain Error from the shortcut menu for more information about the error. |
| --- |

Parent topic:

Lot Data

<!--NI_TOPIC bundle=tsm-labview-application-api-ref path=menus/categories/ni-semiconductormodule/semiconductormodulemanager/lotdata/gettestingstate-vi.html language=enus -->
## TOPIC 00015: Get Testing State

- bundle_id: `tsm-labview-application-api-ref`
- source_path: `menus/categories/ni-semiconductormodule/semiconductormodulemanager/lotdata/gettestingstate-vi.html`
- source_url: https://docs-be.ni.com/bundle/tsm-labview-application-api-ref/raw/resource/enus/menus/categories/ni-semiconductormodule/semiconductormodulemanager/lotdata/gettestingstate-vi.html
- document_id: `tsm-labview-application-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns whether the lot is currently configuring, testing, paused, or idle. icon Inputs/Outputs coarn.png Semiconductor Module Manager Semiconductor Module Manager is a valid ActiveX reference to a Semiconductor Module Manager object. cerrcodeclst.png error in (no error) describes error conditions t

### Get Testing State

Returns whether the lot is currently configuring, testing, paused, or idle.

[IMAGE alt='icon' src='gettestingstate-vi.png']

#### Inputs/Outputs

| Semiconductor Module Manager — Semiconductor Module Manager is a valid ActiveX reference to a Semiconductor Module Manager object. error in (no error) — describes error conditions that occur before this VI or function runs. The default is no error. If an error occurred before this VI or function runs, the VI or function passes the error in (no error) Semiconductor Module Manager Out — returns the Semiconductor Module Manager parameter unchanged. TestingState — returns whether the lot is currently configuring, testing, paused, or idle. error out — contains error information. If error in indicates that an error occurred before this VI or function ran, error out contains the same error information. Otherwise, it describes the error status that this VI or function produces. Right-click the error out front panel indicator and select Explain Error from the shortcut menu for more information about the error. |
| --- |

Parent topic:

Lot Data

<!--NI_TOPIC bundle=tsm-labview-application-api-ref path=menus/categories/ni-semiconductormodule/semiconductormodulemanager/lotdata/gettimingfromlotstatistics-vi.html language=enus -->
## TOPIC 00016: Get Timing From Lot Statistics

- bundle_id: `tsm-labview-application-api-ref`
- source_path: `menus/categories/ni-semiconductormodule/semiconductormodulemanager/lotdata/gettimingfromlotstatistics-vi.html`
- source_url: https://docs-be.ni.com/bundle/tsm-labview-application-api-ref/raw/resource/enus/menus/categories/ni-semiconductormodule/semiconductormodulemanager/lotdata/gettimingfromlotstatistics-vi.html
- document_id: `tsm-labview-application-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the start time and end time for the current lot. The end time is valid only in the ModelPlugin - End entry point and later. For more information, see the ILotStatistics interface in the Semiconductor Module Application API topic in the NI TestStand Semiconductor Module help. icon Inputs/Outputs

### Get Timing From Lot Statistics

Gets the start time and end time for the current lot. The end time is valid only in the ModelPlugin - End entry point and later. For more information, see the ILotStatistics interface in the Semiconductor Module Application API topic in the NI TestStand Semiconductor Module help.

[IMAGE alt='icon' src='gettimingfromlotstatistics-vi.png']

#### Inputs/Outputs

| Lot Statistics — Lot Statistics is a valid ActiveX reference to a Lot Statistics object. error in (no error) — describes error conditions that occur before this VI or function runs. The default is no error. If an error occurred before this VI or function runs, the VI or function passes the error in (no error) Lot Statistics (out) — returns the Lot Statistics parameter unchanged. Lot Start Time — Returns the lot start time. The lot start time corresponds to the time that the handler/prober driver receives the first start-of-test (SOT) signal. Lot End Time — Returns the lot end time. The lot end time corresponds to the time that tester completes testing and writing all reports and data log files. This property value is valid in the Model Plugin - End entry point. error out — contains error information. If error in indicates that an error occurred before this VI or function ran, error out contains the same error information. Otherwise, it describes the error status that this VI or function produces. Right-click the error out front panel indicator and select Explain Error from the shortcut menu for more information about the error. |
| --- |

Parent topic:

Lot Data

<!--NI_TOPIC bundle=tsm-labview-application-api-ref path=menus/categories/ni-semiconductormodule/semiconductormodulemanager/lotdata/getwaferruntimedata-vi.html language=enus -->
## TOPIC 00017: Get Wafer Runtime Data

- bundle_id: `tsm-labview-application-api-ref`
- source_path: `menus/categories/ni-semiconductormodule/semiconductormodulemanager/lotdata/getwaferruntimedata-vi.html`
- source_url: https://docs-be.ni.com/bundle/tsm-labview-application-api-ref/raw/resource/enus/menus/categories/ni-semiconductormodule/semiconductormodulemanager/lotdata/getwaferruntimedata-vi.html
- document_id: `tsm-labview-application-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the run-time data associated with the current wafer. For more information, see the documentation for the IWaferRuntimeData interface in the Semiconductor Module Application API topic in the NI TestStand Semiconductor Module help. icon Inputs/Outputs coarn.png Semiconductor Module Manager Semico

### Get Wafer Runtime Data

Gets the run-time data associated with the current wafer. For more information, see the documentation for the IWaferRuntimeData interface in the Semiconductor Module Application API topic in the NI TestStand Semiconductor Module help.

[IMAGE alt='icon' src='getwaferruntimedata-vi.png']

#### Inputs/Outputs

| Semiconductor Module Manager — Semiconductor Module Manager is a valid ActiveX reference to a Semiconductor Module Manager object. error in (no error) — describes error conditions that occur before this VI or function runs. The default is no error. If an error occurred before this VI or function runs, the VI or function passes the error in (no error) Wafer Id — Returns the wafer ID. This property corresponds to the WAFER_ID field in the Wafer Information Record (WIR) and Wafer Results Record (WRR) in the STDF data log. The value is null when not using a prober driver. Semiconductor Module Manager (out) — returns the Semiconductor Module Manager parameter unchanged. Fab Wafer Id — Returns the fab wafer ID. This property corresponds to the FABWF_ID field in the Wafer Results Record (WRR) in the STDF data log. The value is null when not using a prober driver. Frame Id — Returns the wafer frame ID. This property corresponds to the FRAME_ID field in the Wafer Results Record (WRR) in the STDF data log. The value is null when not using a prober driver. Mask Id — Returns the wafer mask ID. This property corresponds to the MASK_ID field in the Wafer Results Record (WRR) in the STDF data log. The value is null when not using a prober driver. error out — contains error information. If error in indicates that an error occurred before this VI or function ran, error out contains the same error information. Otherwise, it describes the error status that this VI or function produces. Right-click the error out front panel indicator and select Explain Error from the shortcut menu for more information about the error. User Description — Returns the wafer description supplied by user. This property corresponds to the USR_DESC field in the Wafer Results Record (WRR) in the STDF data log. The value is null when not using a prober driver. Exec Description — Returns the wafer description supplied by exec. This property corresponds to the EXC_DESC field in the Wafer Results Record (WRR) in the STDF data log. The value is null when not using a prober driver. |
| --- |

Parent topic:

Lot Data

<!--NI_TOPIC bundle=tsm-labview-application-api-ref path=menus/categories/ni-semiconductormodule/semiconductormodulemanager/lotdata/getwafersitelotstatistics-vi.html language=enus -->
## TOPIC 00018: Get Wafer Site Lot Statistics

- bundle_id: `tsm-labview-application-api-ref`
- source_path: `menus/categories/ni-semiconductormodule/semiconductormodulemanager/lotdata/getwafersitelotstatistics-vi.html`
- source_url: https://docs-be.ni.com/bundle/tsm-labview-application-api-ref/raw/resource/enus/menus/categories/ni-semiconductormodule/semiconductormodulemanager/lotdata/getwafersitelotstatistics-vi.html
- document_id: `tsm-labview-application-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the lot statistics objects for each site for the current wafer. Each object in the array contains the wafer statistics for a single site. Use site numbers to index into this array to obtain an instance of ILotStatistics for each site. The number of elements in the array equals the value of t

### Get Wafer Site Lot Statistics

Returns the lot statistics objects for each site for the current wafer. Each object in the array contains the wafer statistics for a single site. Use site numbers to index into this array to obtain an instance of ILotStatistics for each site. The number of elements in the array equals the value of the NumberOfSites property. If the lot has not yet been configured, the statistics objects contain empty data (no bin data, and part counts are 0). When you begin a new wafer, the SemiconductorModuleManager creates new statistics objects that contain valid bin numbers, but all part counts are set to 0. The statistics objects remain valid during testing and after testing is complete until you begin testing of a new wafer or configure a new lot.

[IMAGE alt='icon' src='getwafersitelotstatistics-vi.png']

#### Inputs/Outputs

| Semiconductor Module Manager — Semiconductor Module Manager is a valid ActiveX reference to a Semiconductor Module Manager object. error in (no error) — describes error conditions that occur before this VI or function runs. The default is no error. If an error occurred before this VI or function runs, the VI or function passes the error in (no error) Semiconductor Module Manager (out) — returns the Semiconductor Module Manager parameter unchanged. Wafer Site Lot Statistics — is an array that contains the lot statistics objects for each site for the current wafer. error out — contains error information. If error in indicates that an error occurred before this VI or function ran, error out contains the same error information. Otherwise, it describes the error status that this VI or function produces. Right-click the error out front panel indicator and select Explain Error from the shortcut menu for more information about the error. |
| --- |

Parent topic:

Lot Data

<!--NI_TOPIC bundle=tsm-labview-application-api-ref path=menus/categories/ni-semiconductormodule/semiconductormodulemanager/lotdata/getwindowpartcountstatistics-vi.html language=enus -->
## TOPIC 00019: Get Window Part Count Statistics

- bundle_id: `tsm-labview-application-api-ref`
- source_path: `menus/categories/ni-semiconductormodule/semiconductormodulemanager/lotdata/getwindowpartcountstatistics-vi.html`
- source_url: https://docs-be.ni.com/bundle/tsm-labview-application-api-ref/raw/resource/enus/menus/categories/ni-semiconductormodule/semiconductormodulemanager/lotdata/getwindowpartcountstatistics-vi.html
- document_id: `tsm-labview-application-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns statistical part count data for the last n parts tested, where n is the number the Site Status Part Count station setting specifies. icon Inputs/Outputs coarn.png Lot Statistics Lot Statistics is a valid ActiveX reference to a Lot Statistics object. cerrcodeclst.png error in (no error) descr

### Get Window Part Count Statistics

Returns statistical part count data for the last n parts tested, where n is the number the Site Status Part Count station setting specifies.

[IMAGE alt='icon' src='getwindowpartcountstatistics-vi.png']

#### Inputs/Outputs

| Lot Statistics — Lot Statistics is a valid ActiveX reference to a Lot Statistics object. error in (no error) — describes error conditions that occur before this VI or function runs. The default is no error. If an error occurred before this VI or function runs, the VI or function passes the error in (no error) Total — returns the total number of parts tested through the last n parts, where n is the number the Site Status Part Count station setting specifies. Lot Statistics (out) — returns the Lot Statistics parameter unchanged. Passed — returns the total number of parts that passed over the last n parts. Failed — returns the total number of parts that failed over the last n parts. Other — returns the total number of parts that neither passed nor failed over the last n parts. error out — contains error information. If error in indicates that an error occurred before this VI or function ran, error out contains the same error information. Otherwise, it describes the error status that this VI or function produces. Right-click the error out front panel indicator and select Explain Error from the shortcut menu for more information about the error. |
| --- |

Parent topic:

Lot Data

<!--NI_TOPIC bundle=tsm-labview-application-api-ref path=menus/categories/ni-semiconductormodule/semiconductormodulemanager/lotdata/lotdata-mnu.html language=enus -->
## TOPIC 00020: Lot Data

- bundle_id: `tsm-labview-application-api-ref`
- source_path: `menus/categories/ni-semiconductormodule/semiconductormodulemanager/lotdata/lotdata-mnu.html`
- source_url: https://docs-be.ni.com/bundle/tsm-labview-application-api-ref/raw/resource/enus/menus/categories/ni-semiconductormodule/semiconductormodulemanager/lotdata/lotdata-mnu.html
- document_id: `tsm-labview-application-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Use the Lot Data VIs to access edit time or runtime information about a lot. icon

### Lot Data

Use the Lot Data VIs to access edit time or runtime information about a lot.

[IMAGE alt='icon' src='lotdata-mnu.png']

- [Get Semiconductor Module Manager](../../../../../menus/categories/ni-semiconductormodule/semiconductormodulemanager/lotdata/getsemiconductormodulemanager-vi.html) Gets the existing Semiconductor Module Manager object.
- [Get Testing State](../../../../../menus/categories/ni-semiconductormodule/semiconductormodulemanager/lotdata/gettestingstate-vi.html) Returns whether the lot is currently configuring, testing, paused, or idle.
- [Get Batch Runtime Data](../../../../../menus/categories/ni-semiconductormodule/semiconductormodulemanager/lotdata/getbatchruntimedata-vi.html) Gets the run-time data associated with the current batch. For more information, see the documentation for the IBatchRuntimeData interface in the Semiconductor Module Application API topic in the NI TestStand Semiconductor Module help.
- [Get Wafer Runtime Data](../../../../../menus/categories/ni-semiconductormodule/semiconductormodulemanager/lotdata/getwaferruntimedata-vi.html) Gets the run-time data associated with the current wafer. For more information, see the documentation for the IWaferRuntimeData interface in the Semiconductor Module Application API topic in the NI TestStand Semiconductor Module help.
- [Get Site Runtime Data](../../../../../menus/categories/ni-semiconductormodule/semiconductormodulemanager/lotdata/getsiteruntimedata-vi.html) Gets the run-time data associated with the current site. For more information, see the documentation for the ISiteRuntimeData interface in the Semiconductor Module Application API topic in the NI TestStand Semiconductor Module help.
- [Get Site Lot Statistics](../../../../../menus/categories/ni-semiconductormodule/semiconductormodulemanager/lotdata/getsitelotstatistics-vi.html) Returns the lot statistics objects for each site. If the lot has not yet been configured, the statistics objects contain empty data (no bin data, and part counts are 0). When you configure the lot, the SemiconductorModuleManager creates new statistics objects that contain valid bin numbers, but all part counts are set to 0. The statistics objects remain valid during testing and after testing is complete until you configure a new lot.
- [Get Wafer Site Lot Statistics](../../../../../menus/categories/ni-semiconductormodule/semiconductormodulemanager/lotdata/getwafersitelotstatistics-vi.html) Returns the lot statistics objects for each site for the current wafer. Each object in the array contains the wafer statistics for a single site. Use site numbers to index into this array to obtain an instance of ILotStatistics for each site. The number of elements in the array equals the value of the NumberOfSites property. If the lot has not yet been configured, the statistics objects contain empty data (no bin data, and part counts are 0). When you begin a new wafer, the SemiconductorModuleManager creates new statistics objects that contain valid bin numbers, but all part counts are set to 0. The statistics objects remain valid during testing and after testing is complete until you begin testing of a new wafer or configure a new lot.
- [Get Timing From Lot Statistics](../../../../../menus/categories/ni-semiconductormodule/semiconductormodulemanager/lotdata/gettimingfromlotstatistics-vi.html) Gets the start time and end time for the current lot. The end time is valid only in the ModelPlugin - End entry point and later. For more information, see the ILotStatistics interface in the Semiconductor Module Application API topic in the NI TestStand Semiconductor Module help.
- [Get Part Count Statistics](../../../../../menus/categories/ni-semiconductormodule/semiconductormodulemanager/lotdata/getpartcountstatistics-vi.html) Returns statistical part count data for parts tested.
- [Get Window Part Count Statistics](../../../../../menus/categories/ni-semiconductormodule/semiconductormodulemanager/lotdata/getwindowpartcountstatistics-vi.html) Returns statistical part count data for the last n parts tested, where n is the number the Site Status Part Count station setting specifies.
- [Get Inline QA Part Count Statistics](../../../../../menus/categories/ni-semiconductormodule/semiconductormodulemanager/lotdata/getinlineqapartcountstatistics-vi.html) Returns statistical part count data for parts tested with Inline QA enabled.
- [Get Software Bin Numbers](../../../../../menus/categories/ni-semiconductormodule/semiconductormodulemanager/lotdata/getsoftwarebinnumbers-vi.html) Returns the bin numbers for each software bin in the lot the Lot Statistics parameter specifies.
- [Get Software Bin Statistics](../../../../../menus/categories/ni-semiconductormodule/semiconductormodulemanager/lotdata/getsoftwarebinstatistics-vi.html) Returns the bin statistics data for the software bin the Bin parameter specifies.
- [Get Software Bin Numbers By Count](../../../../../menus/categories/ni-semiconductormodule/semiconductormodulemanager/lotdata/getsoftwarebinnumbersbycount-vi.html) Returns the bin numbers for each software bin in the lot the Lot Statistics parameter specifies, sorted in descending order by the part count per bin.
- [Get Hardware Bin Numbers](../../../../../menus/categories/ni-semiconductormodule/semiconductormodulemanager/lotdata/gethardwarebinnumbers-vi.html) Returns the bin numbers for each hardware bin in the lot the Lot Statistics parameter specifies.
- [Get Hardware Bin Statistics](../../../../../menus/categories/ni-semiconductormodule/semiconductormodulemanager/lotdata/gethardwarebinstatistics-vi.html) Returns the bin statistics data for the hardware bin the Bin parameter specifies.
- [Get STDF Log File Paths](../../../../../menus/categories/ni-semiconductormodule/semiconductormodulemanager/lotdata/getstdflogfilepaths-vi.html) Returns the absolute file paths of all STDF logs generated for the current lot.
- [Get Lot Summary Report File Paths](../../../../../menus/categories/ni-semiconductormodule/semiconductormodulemanager/lotdata/getlotsummaryreportfilepaths-vi.html) Returns the absolute file paths of all Lot Summary reports generated for the current lot.
- [Get CSV Test Results Log File Paths](../../../../../menus/categories/ni-semiconductormodule/semiconductormodulemanager/lotdata/getcsvtestresultslogfilepaths-vi.html) Returns the absolute file paths of all CSV test results logs generated for the current lot.

Parent topic:

Application Development

<!--NI_TOPIC bundle=tsm-labview-application-api-ref path=menus/categories/ni-semiconductormodule/semiconductormodulemanager/operatorinterface/configurelotdialog-vi.html language=enus -->
## TOPIC 00021: Display Configure Lot Dialog

- bundle_id: `tsm-labview-application-api-ref`
- source_path: `menus/categories/ni-semiconductormodule/semiconductormodulemanager/operatorinterface/configurelotdialog-vi.html`
- source_url: https://docs-be.ni.com/bundle/tsm-labview-application-api-ref/raw/resource/enus/menus/categories/ni-semiconductormodule/semiconductormodulemanager/operatorinterface/configurelotdialog-vi.html
- document_id: `tsm-labview-application-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Displays the Configure Lot Settings dialog box by executing the ConfigureLotSettings callback sequence in SemiconductorModuleCallbacks.seq sequence file. icon Inputs/Outputs coarn.png Semiconductor Module Manager Semiconductor Module Manager is a valid ActiveX reference to a Semiconductor Module Man

### Display Configure Lot Dialog

Displays the Configure Lot Settings dialog box by executing the ConfigureLotSettings callback sequence in SemiconductorModuleCallbacks.seq sequence file.

[IMAGE alt='icon' src='configurelotdialog-vi.png']

#### Inputs/Outputs

| Semiconductor Module Manager — Semiconductor Module Manager is a valid ActiveX reference to a Semiconductor Module Manager object. TestStand Modal ID — TestStand Modal ID is the Modal ID value the TestStand - Start Modal Dialog VI returns in the Modal ID parameter. Use this input only if you use the TestStand - Start Modal Dialog VI to make the calling VI modal to TestStand. error in (no error) — describes error conditions that occur before this VI or function runs. The default is no error. If an error occurred before this VI or function runs, the VI or function passes the error in (no error) Semiconductor Module Manager Out — returns the Semiconductor Module Manager parameter unchanged. error out — contains error information. If error in indicates that an error occurred before this VI or function ran, error out contains the same error information. Otherwise, it describes the error status that this VI or function produces. Right-click the error out front panel indicator and select Explain Error from the shortcut menu for more information about the error. |
| --- |

Parent topic:

Operator Interface

<!--NI_TOPIC bundle=tsm-labview-application-api-ref path=menus/categories/ni-semiconductormodule/semiconductormodulemanager/operatorinterface/configurestationdialog-vi.html language=enus -->
## TOPIC 00022: Display Configure Station Dialog

- bundle_id: `tsm-labview-application-api-ref`
- source_path: `menus/categories/ni-semiconductormodule/semiconductormodulemanager/operatorinterface/configurestationdialog-vi.html`
- source_url: https://docs-be.ni.com/bundle/tsm-labview-application-api-ref/raw/resource/enus/menus/categories/ni-semiconductormodule/semiconductormodulemanager/operatorinterface/configurestationdialog-vi.html
- document_id: `tsm-labview-application-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Displays the Configure Station Settings dialog box by executing the ConfigureStationSettings callback sequence in the SemiconductorModuleCallbacks.seq sequence file. icon Inputs/Outputs coarn.png Semiconductor Module Manager Semiconductor Module Manager is a valid ActiveX reference to a Semiconducto

### Display Configure Station Dialog

Displays the Configure Station Settings dialog box by executing the ConfigureStationSettings callback sequence in the SemiconductorModuleCallbacks.seq sequence file.

[IMAGE alt='icon' src='configurestationdialog-vi.png']

#### Inputs/Outputs

| Semiconductor Module Manager — Semiconductor Module Manager is a valid ActiveX reference to a Semiconductor Module Manager object. TestStand Modal ID — TestStand Modal ID is the Modal ID value the TestStand - Start Modal Dialog VI returns in the Modal ID parameter. Use this input only if you use the TestStand - Start Modal Dialog VI to make the calling VI modal to TestStand. error in (no error) — describes error conditions that occur before this VI or function runs. The default is no error. If an error occurred before this VI or function runs, the VI or function passes the error in (no error) Semiconductor Module Manager Out — returns the Semiconductor Module Manager parameter unchanged. error out — contains error information. If error in indicates that an error occurred before this VI or function ran, error out contains the same error information. Otherwise, it describes the error status that this VI or function produces. Right-click the error out front panel indicator and select Explain Error from the shortcut menu for more information about the error. |
| --- |

Parent topic:

Operator Interface

<!--NI_TOPIC bundle=tsm-labview-application-api-ref path=menus/categories/ni-semiconductormodule/semiconductormodulemanager/operatorinterface/createsemiconductormodulemanager-vi.html language=enus -->
## TOPIC 00023: Create Semiconductor Module Manager

- bundle_id: `tsm-labview-application-api-ref`
- source_path: `menus/categories/ni-semiconductormodule/semiconductormodulemanager/operatorinterface/createsemiconductormodulemanager-vi.html`
- source_url: https://docs-be.ni.com/bundle/tsm-labview-application-api-ref/raw/resource/enus/menus/categories/ni-semiconductormodule/semiconductormodulemanager/operatorinterface/createsemiconductormodulemanager-vi.html
- document_id: `tsm-labview-application-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Creates the Semiconductor Module Manager object. icon Inputs/Outputs coarn.png TestStand Engine TestStand Engine is an ActiveX reference to the TestStand Engine object. coarn.png SequenceFileViewMgr is the TestStand UI controller that manages the selected sequence file and keeps all connected UI con

### Create Semiconductor Module Manager

Creates the Semiconductor Module Manager object.

[IMAGE alt='icon' src='createsemiconductormodulemanager-vi.png']

#### Inputs/Outputs

| TestStand Engine — TestStand Engine is an ActiveX reference to the TestStand Engine object. SequenceFileViewMgr — is the TestStand UI controller that manages the selected sequence file and keeps all connected UI controls synchronized with its current view and state. SequenceFileViewMgr error in (no error) — describes error conditions that occur before this VI or function runs. The default is no error. If an error occurred before this VI or function runs, the VI or function passes the error in (no error) Semiconductor Module Manager Out — returns the Semiconductor Module Manager that the VI creates. error out — contains error information. If error in indicates that an error occurred before this VI or function ran, error out contains the same error information. Otherwise, it describes the error status that this VI or function produces. Right-click the error out front panel indicator and select Explain Error from the shortcut menu for more information about the error. |
| --- |

Parent topic:

Operator Interface

<!--NI_TOPIC bundle=tsm-labview-application-api-ref path=menus/categories/ni-semiconductormodule/semiconductormodulemanager/operatorinterface/getcommand-vi.html language=enus -->
## TOPIC 00024: Get Command

- bundle_id: `tsm-labview-application-api-ref`
- source_path: `menus/categories/ni-semiconductormodule/semiconductormodulemanager/operatorinterface/getcommand-vi.html`
- source_url: https://docs-be.ni.com/bundle/tsm-labview-application-api-ref/raw/resource/enus/menus/categories/ni-semiconductormodule/semiconductormodulemanager/operatorinterface/getcommand-vi.html
- document_id: `tsm-labview-application-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns a valid ActiveX reference to a Command object for the command or action the CommandType parameter specifies. icon Inputs/Outputs coarn.png Semiconductor Module Manager Semiconductor Module Manager is a valid ActiveX reference to a Semiconductor Module Manager object. cenum.png CommandType Co

### Get Command

Returns a valid ActiveX reference to a Command object for the command or action the **CommandType** parameter specifies.

[IMAGE alt='icon' src='getcommand-vi.png']

#### Inputs/Outputs

| Semiconductor Module Manager — Semiconductor Module Manager is a valid ActiveX reference to a Semiconductor Module Manager object. CommandType — CommandType is a valid ActiveX reference to a CommandType object. error in (no error) — describes error conditions that occur before this VI or function runs. The default is no error. If an error occurred before this VI or function runs, the VI or function passes the error in (no error) Semiconductor Module Manager (out) — returns the Semiconductor Module Manager parameter unchanged. Command — returns a valid ActiveX reference to a Command object. error out — contains error information. If error in indicates that an error occurred before this VI or function ran, error out contains the same error information. Otherwise, it describes the error status that this VI or function produces. Right-click the error out front panel indicator and select Explain Error from the shortcut menu for more information about the error. |
| --- |

Parent topic:

Operator Interface

<!--NI_TOPIC bundle=tsm-labview-application-api-ref path=menus/categories/ni-semiconductormodule/semiconductormodulemanager/operatorinterface/getsettingstodisplay-vi.html language=enus -->
## TOPIC 00025: Get Settings To Display

- bundle_id: `tsm-labview-application-api-ref`
- source_path: `menus/categories/ni-semiconductormodule/semiconductormodulemanager/operatorinterface/getsettingstodisplay-vi.html`
- source_url: https://docs-be.ni.com/bundle/tsm-labview-application-api-ref/raw/resource/enus/menus/categories/ni-semiconductormodule/semiconductormodulemanager/operatorinterface/getsettingstodisplay-vi.html
- document_id: `tsm-labview-application-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns arrays of lot settings and station settings to display in the operator interface settings table. icon Inputs/Outputs coarn.png Semiconductor Module Manager Semiconductor Module Manager is a valid ActiveX reference to a Semiconductor Module Manager object. cerrcodeclst.png error in (no error)

### Get Settings To Display

Returns arrays of lot settings and station settings to display in the operator interface settings table.

[IMAGE alt='icon' src='getsettingstodisplay-vi.png']

#### Inputs/Outputs

| Semiconductor Module Manager — Semiconductor Module Manager is a valid ActiveX reference to a Semiconductor Module Manager object. error in (no error) — describes error conditions that occur before this VI or function runs. The default is no error. If an error occurred before this VI or function runs, the VI or function passes the error in (no error) Semiconductor Module Manager Out — returns the Semiconductor Module Manager parameter unchanged. Display Names — is an array that contains the names of the lot settings configured to be displayed. Display Values — is an array that contains the values of the lot settings configured to be displayed. error out — contains error information. If error in indicates that an error occurred before this VI or function ran, error out contains the same error information. Otherwise, it describes the error status that this VI or function produces. Right-click the error out front panel indicator and select Explain Error from the shortcut menu for more information about the error. |
| --- |

Parent topic:

Operator Interface

<!--NI_TOPIC bundle=tsm-labview-application-api-ref path=menus/categories/ni-semiconductormodule/semiconductormodulemanager/operatorinterface/getsitestesting-vi.html language=enus -->
## TOPIC 00026: Get Sites Testing

- bundle_id: `tsm-labview-application-api-ref`
- source_path: `menus/categories/ni-semiconductormodule/semiconductormodulemanager/operatorinterface/getsitestesting-vi.html`
- source_url: https://docs-be.ni.com/bundle/tsm-labview-application-api-ref/raw/resource/enus/menus/categories/ni-semiconductormodule/semiconductormodulemanager/operatorinterface/getsitestesting-vi.html
- document_id: `tsm-labview-application-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns an array that indicates which of the sites are currently testing a part or waiting for a part. The Semiconductor Module Manager updates the values in the array after receiving the start-of-test (SOT) signal and before sending the end-of-test (EOT) signal. icon Inputs/Outputs coarn.png Semico

### Get Sites Testing

Returns an array that indicates which of the sites are currently testing a part or waiting for a part. The Semiconductor Module Manager updates the values in the array after receiving the start-of-test (SOT) signal and before sending the end-of-test (EOT) signal.

[IMAGE alt='icon' src='getsitestesting-vi.png']

#### Inputs/Outputs

| Semiconductor Module Manager — Semiconductor Module Manager is a valid ActiveX reference to a Semiconductor Module Manager object. error in (no error) — describes error conditions that occur before this VI or function runs. The default is no error. If an error occurred before this VI or function runs, the VI or function passes the error in (no error) Semiconductor Module Manager Out — returns the Semiconductor Module Manager parameter unchanged. Sites Testing — is an array that indicates which of the sites are currently testing a part or waiting for a part. error out — contains error information. If error in indicates that an error occurred before this VI or function ran, error out contains the same error information. Otherwise, it describes the error status that this VI or function produces. Right-click the error out front panel indicator and select Explain Error from the shortcut menu for more information about the error. |
| --- |

Parent topic:

Operator Interface

<!--NI_TOPIC bundle=tsm-labview-application-api-ref path=menus/categories/ni-semiconductormodule/semiconductormodulemanager/operatorinterface/operatorinterface-mnu.html language=enus -->
## TOPIC 00027: Operator Interface

- bundle_id: `tsm-labview-application-api-ref`
- source_path: `menus/categories/ni-semiconductormodule/semiconductormodulemanager/operatorinterface/operatorinterface-mnu.html`
- source_url: https://docs-be.ni.com/bundle/tsm-labview-application-api-ref/raw/resource/enus/menus/categories/ni-semiconductormodule/semiconductormodulemanager/operatorinterface/operatorinterface-mnu.html
- document_id: `tsm-labview-application-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Use the Operator Interface VIs to implement custom operator interfaces. icon

### Operator Interface

Use the Operator Interface VIs to implement custom operator interfaces.

[IMAGE alt='icon' src='operatorinterface-mnu.png']

- [Create Semiconductor Module Manager](../../../../../menus/categories/ni-semiconductormodule/semiconductormodulemanager/operatorinterface/createsemiconductormodulemanager-vi.html) Creates the Semiconductor Module Manager object.
- [Display Configure Lot Dialog](../../../../../menus/categories/ni-semiconductormodule/semiconductormodulemanager/operatorinterface/configurelotdialog-vi.html) Displays the Configure Lot Settings dialog box by executing the ConfigureLotSettings callback sequence in SemiconductorModuleCallbacks.seq sequence file.
- [Display Configure Station Dialog](../../../../../menus/categories/ni-semiconductormodule/semiconductormodulemanager/operatorinterface/configurestationdialog-vi.html) Displays the Configure Station Settings dialog box by executing the ConfigureStationSettings callback sequence in the SemiconductorModuleCallbacks.seq sequence file.
- [Get Command](../../../../../menus/categories/ni-semiconductormodule/semiconductormodulemanager/operatorinterface/getcommand-vi.html) Returns a valid ActiveX reference to a Command object for the command or action the CommandType parameter specifies.
- [Get Settings To Display](../../../../../menus/categories/ni-semiconductormodule/semiconductormodulemanager/operatorinterface/getsettingstodisplay-vi.html) Returns arrays of lot settings and station settings to display in the operator interface settings table.
- [Get Sites Testing](../../../../../menus/categories/ni-semiconductormodule/semiconductormodulemanager/operatorinterface/getsitestesting-vi.html) Returns an array that indicates which of the sites are currently testing a part or waiting for a part. The Semiconductor Module Manager updates the values in the array after receiving the start-of-test (SOT) signal and before sending the end-of-test (EOT) signal.

Parent topic:

Application Development

<!--NI_TOPIC bundle=tsm-labview-application-api-ref path=menus/categories/ni-semiconductormodule/semiconductormodulemanager/semiconductormodulemanager-mnu.html language=enus -->
## TOPIC 00028: Application Development

- bundle_id: `tsm-labview-application-api-ref`
- source_path: `menus/categories/ni-semiconductormodule/semiconductormodulemanager/semiconductormodulemanager-mnu.html`
- source_url: https://docs-be.ni.com/bundle/tsm-labview-application-api-ref/raw/resource/enus/menus/categories/ni-semiconductormodule/semiconductormodulemanager/semiconductormodulemanager-mnu.html
- document_id: `tsm-labview-application-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Use the Application Development VIs to implement custom Operator Interfaces, lot settings dialogs and station settings dialogs. icon

### Application Development

Use the Application Development VIs to implement custom Operator Interfaces, lot settings dialogs and station settings dialogs.

[IMAGE alt='icon' src='semiconductormodulemanager-mnu.png']

- [Operator Interface](../../../../menus/categories/ni-semiconductormodule/semiconductormodulemanager/operatorinterface/operatorinterface-mnu.html) Use the Operator Interface VIs to implement custom operator interfaces.
- [Lot Data](../../../../menus/categories/ni-semiconductormodule/semiconductormodulemanager/lotdata/lotdata-mnu.html) Use the Lot Data VIs to access edit time or runtime information about a lot.
- [Station Configuration](../../../../menus/categories/ni-semiconductormodule/semiconductormodulemanager/stationconfiguration/stationconfiguration-mnu.html) Use the Station Configuration VIs to get information about the station and lot settings.
- [Test Program](../../../../menus/categories/ni-semiconductormodule/semiconductormodulemanager/testprogram/testprogram-mnu.html) Use the Test Program VIs to access information about a test program.

<!--NI_TOPIC bundle=tsm-labview-application-api-ref path=menus/categories/ni-semiconductormodule/semiconductormodulemanager/stationconfiguration/canconfigurehandlerdriver-vi.html language=enus -->
## TOPIC 00029: Can Configure Handler/Prober?

- bundle_id: `tsm-labview-application-api-ref`
- source_path: `menus/categories/ni-semiconductormodule/semiconductormodulemanager/stationconfiguration/canconfigurehandlerdriver-vi.html`
- source_url: https://docs-be.ni.com/bundle/tsm-labview-application-api-ref/raw/resource/enus/menus/categories/ni-semiconductormodule/semiconductormodulemanager/stationconfiguration/canconfigurehandlerdriver-vi.html
- document_id: `tsm-labview-application-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Determines whether you can configure the handler/prober driver the Handler/Prober Driver Path parameter specifies. The handler/prober driver sequence file must contain a Configure entrypoint sequence for you to configure the handler/prober driver. Use the Display Configure Handler/Prober Dialog VI t

### Can Configure Handler/Prober?

Determines whether you can configure the handler/prober driver the **Handler/Prober Driver Path** parameter specifies. The handler/prober driver sequence file must contain a Configure entrypoint sequence for you to configure the handler/prober driver. Use the Display Configure Handler/Prober Dialog VI to configure the handler/prober driver.

[IMAGE alt='icon' src='canconfigurehandlerdriver-vi.png']

#### Inputs/Outputs

| Semiconductor Module Manager — Semiconductor Module Manager is a valid ActiveX reference to a Semiconductor Module Manager object. Handler/Prober Driver Path — Handler/Prober Driver Path is the absolute path of the handler/prober driver sequence file. error in (no error) — describes error conditions that occur before this VI or function runs. The default is no error. If an error occurred before this VI or function runs, the VI or function passes the error in (no error) Semiconductor Module Manager Out — returns the Semiconductor Module Manager parameter unchanged. Can Configure Handler/Prober Driver? — returns True if you can configure the handler/prober driver. error out — contains error information. If error in indicates that an error occurred before this VI or function ran, error out contains the same error information. Otherwise, it describes the error status that this VI or function produces. Right-click the error out front panel indicator and select Explain Error from the shortcut menu for more information about the error. |
| --- |

Parent topic:

Station Configuration

<!--NI_TOPIC bundle=tsm-labview-application-api-ref path=menus/categories/ni-semiconductormodule/semiconductormodulemanager/stationconfiguration/configurehandlerdialog-vi.html language=enus -->
## TOPIC 00030: Display Configure Handler/Prober Dialog

- bundle_id: `tsm-labview-application-api-ref`
- source_path: `menus/categories/ni-semiconductormodule/semiconductormodulemanager/stationconfiguration/configurehandlerdialog-vi.html`
- source_url: https://docs-be.ni.com/bundle/tsm-labview-application-api-ref/raw/resource/enus/menus/categories/ni-semiconductormodule/semiconductormodulemanager/stationconfiguration/configurehandlerdialog-vi.html
- document_id: `tsm-labview-application-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Configures the handler/prober driver the Handler/Prober Driver Path parameter specifies by calling the Configure entry point sequence in the handler/prober driver sequence file. Typically, the Configure entry point sequence displays a handler/prober configuration dialog box. Use the Can Configure Ha

### Display Configure Handler/Prober Dialog

Configures the handler/prober driver the **Handler/Prober Driver Path** parameter specifies by calling the Configure entry point sequence in the handler/prober driver sequence file. Typically, the Configure entry point sequence displays a handler/prober configuration dialog box. Use the Can Configure Handler? VI to determine if you can configure the handler/prober driver.

[IMAGE alt='icon' src='configurehandlerdialog-vi.png']

#### Inputs/Outputs

| Semiconductor Module Manager — Semiconductor Module Manager is a valid ActiveX reference to a Semiconductor Module Manager object. Handler/Prober Driver Path — Handler/Prober Driver Path is the absolute path of the handler/prober driver sequence file. TestStand Modal ID — TestStand Modal ID is the Modal ID value the TestStand - Start Modal Dialog VI returns in the Modal ID parameter. Use this input only if you use the TestStand - Start Modal Dialog VI to make the calling VI modal to TestStand. error in (no error) — describes error conditions that occur before this VI or function runs. The default is no error. If an error occurred before this VI or function runs, the VI or function passes the error in (no error) Semiconductor Module Manager Out — returns the Semiconductor Module Manager parameter unchanged. error out — contains error information. If error in indicates that an error occurred before this VI or function ran, error out contains the same error information. Otherwise, it describes the error status that this VI or function produces. Right-click the error out front panel indicator and select Explain Error from the shortcut menu for more information about the error. |
| --- |

Parent topic:

Station Configuration

<!--NI_TOPIC bundle=tsm-labview-application-api-ref path=menus/categories/ni-semiconductormodule/semiconductormodulemanager/stationconfiguration/gethandlerdriversequencefilepath-vi.html language=enus -->
## TOPIC 00031: Get Actual Handler/Prober Driver Sequence File Path

- bundle_id: `tsm-labview-application-api-ref`
- source_path: `menus/categories/ni-semiconductormodule/semiconductormodulemanager/stationconfiguration/gethandlerdriversequencefilepath-vi.html`
- source_url: https://docs-be.ni.com/bundle/tsm-labview-application-api-ref/raw/resource/enus/menus/categories/ni-semiconductormodule/semiconductormodulemanager/stationconfiguration/gethandlerdriversequencefilepath-vi.html
- document_id: `tsm-labview-application-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the path of the handler/prober driver sequence file the Handler/Prober Mode and Handler/Prober Driver Path parameters specify. If the Handler/Prober Mode parameter is HandlerMode_Custom, this VI returns the value of the Handler/Prober Driver Path parameter. If the Handler/Prober Mode paramet

### Get Actual Handler/Prober Driver Sequence File Path

Returns the path of the handler/prober driver sequence file the Handler/Prober Mode and Handler/Prober Driver Path parameters specify. If the Handler/Prober Mode parameter is HandlerMode_Custom, this VI returns the value of the Handler/Prober Driver Path parameter. If the Handler/Prober Mode parameter is HandlerMode_Simulated, this VI returns the absolute path of the TSM simulated handler driver. If the Handler/Prober Mode parameter is HandlerMode_None, this VI returns an empty string.

[IMAGE alt='icon' src='gethandlerdriversequencefilepath-vi.png']

#### Inputs/Outputs

| Semiconductor Module Manager — Semiconductor Module Manager is a valid ActiveX reference to a Semiconductor Module Manager object. Handler/Prober Mode — Handler/Prober Mode is the handler/prober mode to use to determine the handler/prober driver path. Handler/Prober Driver Path — Handler/Prober Driver Path is the absolute path of the handler/prober driver sequence file. error in (no error) — describes error conditions that occur before this VI or function runs. The default is no error. If an error occurred before this VI or function runs, the VI or function passes the error in (no error) Semiconductor Module Manager Out — returns the Semiconductor Module Manager parameter unchanged. Actual Handler/Prober Driver Path — is the path of the handler/prober driver sequence file as determined by the Handler/Prober Mode and Handler/Prober Driver Path parameters. error out — contains error information. If error in indicates that an error occurred before this VI or function ran, error out contains the same error information. Otherwise, it describes the error status that this VI or function produces. Right-click the error out front panel indicator and select Explain Error from the shortcut menu for more information about the error. |
| --- |

Parent topic:

Station Configuration

<!--NI_TOPIC bundle=tsm-labview-application-api-ref path=menus/categories/ni-semiconductormodule/semiconductormodulemanager/stationconfiguration/gethandlerdriversequencefilepaths-vi.html language=enus -->
## TOPIC 00032: Get Handler/Prober Driver Paths

- bundle_id: `tsm-labview-application-api-ref`
- source_path: `menus/categories/ni-semiconductormodule/semiconductormodulemanager/stationconfiguration/gethandlerdriversequencefilepaths-vi.html`
- source_url: https://docs-be.ni.com/bundle/tsm-labview-application-api-ref/raw/resource/enus/menus/categories/ni-semiconductormodule/semiconductormodulemanager/stationconfiguration/gethandlerdriversequencefilepaths-vi.html
- document_id: `tsm-labview-application-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the paths and display names of all the available handler/prober driver sequence files. Handler/prober driver sequence files reside in the TestStandPublic\Components\Modules\NI_SemiconductorModule\Handlers directory. icon Inputs/Outputs coarn.png Semiconductor Module Manager Semiconductor Mod

### Get Handler/Prober Driver Paths

Returns the paths and display names of all the available handler/prober driver sequence files. Handler/prober driver sequence files reside in the TestStandPublic\Components\Modules\NI_SemiconductorModule\Handlers directory.

[IMAGE alt='icon' src='gethandlerdriversequencefilepaths-vi.png']

#### Inputs/Outputs

| Semiconductor Module Manager — Semiconductor Module Manager is a valid ActiveX reference to a Semiconductor Module Manager object. error in (no error) — describes error conditions that occur before this VI or function runs. The default is no error. If an error occurred before this VI or function runs, the VI or function passes the error in (no error) Semiconductor Module Manager Out — returns the Semiconductor Module Manager parameter unchanged. Handler/Prober Driver Sequence File Paths — returns the list of handler/prober driver sequence file absolute paths. Handler/Prober Driver Display Names — returns the list of handler/prober driver display names. The handler/prober driver display names are the base filenames without the file extension. error out — contains error information. If error in indicates that an error occurred before this VI or function ran, error out contains the same error information. Otherwise, it describes the error status that this VI or function produces. Right-click the error out front panel indicator and select Explain Error from the shortcut menu for more information about the error. |
| --- |

Parent topic:

Station Configuration

<!--NI_TOPIC bundle=tsm-labview-application-api-ref path=menus/categories/ni-semiconductormodule/semiconductormodulemanager/stationconfiguration/getinlineqaalgorithmsequencefilepaths-vi.html language=enus -->
## TOPIC 00033: Get Inline QA Algorithm Paths

- bundle_id: `tsm-labview-application-api-ref`
- source_path: `menus/categories/ni-semiconductormodule/semiconductormodulemanager/stationconfiguration/getinlineqaalgorithmsequencefilepaths-vi.html`
- source_url: https://docs-be.ni.com/bundle/tsm-labview-application-api-ref/raw/resource/enus/menus/categories/ni-semiconductormodule/semiconductormodulemanager/stationconfiguration/getinlineqaalgorithmsequencefilepaths-vi.html
- document_id: `tsm-labview-application-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the paths and display names of all the available inline QA algorithm sequence files. Inline QA algorithm sequence files reside in the TestStandPublic\Components\Modules\NI_SemiconductorModule\InlineQA directory. icon Inputs/Outputs coarn.png Semiconductor Module Manager Semiconductor Module

### Get Inline QA Algorithm Paths

Returns the paths and display names of all the available inline QA algorithm sequence files. Inline QA algorithm sequence files reside in the TestStandPublic\Components\Modules\NI_SemiconductorModule\InlineQA directory.

[IMAGE alt='icon' src='getinlineqaalgorithmsequencefilepaths-vi.png']

#### Inputs/Outputs

| Semiconductor Module Manager — Semiconductor Module Manager is a valid ActiveX reference to a Semiconductor Module Manager object. error in (no error) — describes error conditions that occur before this VI or function runs. The default is no error. If an error occurred before this VI or function runs, the VI or function passes the error in (no error) Semiconductor Module Manager Out — returns the Semiconductor Module Manager parameter unchanged. Inline QA Algorithm Sequence File Paths — returns the list of inline QA algorithm sequence file paths. Inline QA Algorithm Display Names — returns the list of inline QA algorithm display names. The inline QA algorithm display names are the base filenames without the file extension. error out — contains error information. If error in indicates that an error occurred before this VI or function ran, error out contains the same error information. Otherwise, it describes the error status that this VI or function produces. Right-click the error out front panel indicator and select Explain Error from the shortcut menu for more information about the error. |
| --- |

Parent topic:

Station Configuration

<!--NI_TOPIC bundle=tsm-labview-application-api-ref path=menus/categories/ni-semiconductormodule/semiconductormodulemanager/stationconfiguration/getnumberofsitestotest-vi.html language=enus -->
## TOPIC 00034: Get Number of Sites to Test

- bundle_id: `tsm-labview-application-api-ref`
- source_path: `menus/categories/ni-semiconductormodule/semiconductormodulemanager/stationconfiguration/getnumberofsitestotest-vi.html`
- source_url: https://docs-be.ni.com/bundle/tsm-labview-application-api-ref/raw/resource/enus/menus/categories/ni-semiconductormodule/semiconductormodulemanager/stationconfiguration/getnumberofsitestotest-vi.html
- document_id: `tsm-labview-application-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the number of sites that TestStand uses to execute with the Batch or Parallel process models. This method returns the Number of Test Sockets setting in the model options. Although TestStand starts executing with the number of sites returned by this method, TSM might reduce the number of site

### Get Number of Sites to Test

Returns the number of sites that TestStand uses to execute with the Batch or Parallel process models. This method returns the Number of Test Sockets setting in the model options. Although TestStand starts executing with the number of sites returned by this method, TSM might reduce the number of sites at run time based on the number of sites in the current pin map and the contents of the AvailableSiteNumbers station setting.

[IMAGE alt='icon' src='getnumberofsitestotest-vi.png']

#### Inputs/Outputs

| Semiconductor Module Manager — Semiconductor Module Manager is a valid ActiveX reference to a Semiconductor Module Manager object. error in (no error) — describes error conditions that occur before this VI or function runs. The default is no error. If an error occurred before this VI or function runs, the VI or function passes the error in (no error) Semiconductor Module Manager Out — returns the Semiconductor Module Manager parameter unchanged. Number of Sites — returns the number of sites that TestStand uses to execute with the Batch or Parallel process models. error out — contains error information. If error in indicates that an error occurred before this VI or function ran, error out contains the same error information. Otherwise, it describes the error status that this VI or function produces. Right-click the error out front panel indicator and select Explain Error from the shortcut menu for more information about the error. |
| --- |

Parent topic:

Station Configuration

<!--NI_TOPIC bundle=tsm-labview-application-api-ref path=menus/categories/ni-semiconductormodule/semiconductormodulemanager/stationconfiguration/readlotsettings-vi.html language=enus -->
## TOPIC 00035: Read Lot Settings

- bundle_id: `tsm-labview-application-api-ref`
- source_path: `menus/categories/ni-semiconductormodule/semiconductormodulemanager/stationconfiguration/readlotsettings-vi.html`
- source_url: https://docs-be.ni.com/bundle/tsm-labview-application-api-ref/raw/resource/enus/menus/categories/ni-semiconductormodule/semiconductormodulemanager/stationconfiguration/readlotsettings-vi.html
- document_id: `tsm-labview-application-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns a TestStand PropertyObject that contains the lot settings stored in the lot settings configuration file. If the lot settings configuration file does not exist, this VI returns the default lot settings by creating a new instance of the NI_SemiconductorModule_LotSettings TestStand data type. i

### Read Lot Settings

Returns a TestStand PropertyObject that contains the lot settings stored in the lot settings configuration file. If the lot settings configuration file does not exist, this VI returns the default lot settings by creating a new instance of the NI_SemiconductorModule_LotSettings TestStand data type.

[IMAGE alt='icon' src='readlotsettings-vi.png']

#### Inputs/Outputs

| Semiconductor Module Manager — Semiconductor Module Manager is a valid ActiveX reference to a Semiconductor Module Manager object. error in (no error) — describes error conditions that occur before this VI or function runs. The default is no error. If an error occurred before this VI or function runs, the VI or function passes the error in (no error) Semiconductor Module Manager Out — returns the Semiconductor Module Manager parameter unchanged. Lot Settings — returns a TestStand PropertyObject object that contains the lot settings. error out — contains error information. If error in indicates that an error occurred before this VI or function ran, error out contains the same error information. Otherwise, it describes the error status that this VI or function produces. Right-click the error out front panel indicator and select Explain Error from the shortcut menu for more information about the error. |
| --- |

Parent topic:

Station Configuration

<!--NI_TOPIC bundle=tsm-labview-application-api-ref path=menus/categories/ni-semiconductormodule/semiconductormodulemanager/stationconfiguration/readstationsettings-vi.html language=enus -->
## TOPIC 00036: Read Station Settings

- bundle_id: `tsm-labview-application-api-ref`
- source_path: `menus/categories/ni-semiconductormodule/semiconductormodulemanager/stationconfiguration/readstationsettings-vi.html`
- source_url: https://docs-be.ni.com/bundle/tsm-labview-application-api-ref/raw/resource/enus/menus/categories/ni-semiconductormodule/semiconductormodulemanager/stationconfiguration/readstationsettings-vi.html
- document_id: `tsm-labview-application-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns a TestStand PropertyObject that contains the station settings stored in the station settings configuration file. If the station settings configuration file does not exist, this VI returns the default station settings by creating a new instance of the NI_SemiconductorModule_StationSettings Te

### Read Station Settings

Returns a TestStand PropertyObject that contains the station settings stored in the station settings configuration file. If the station settings configuration file does not exist, this VI returns the default station settings by creating a new instance of the NI_SemiconductorModule_StationSettings TestStand data type.

[IMAGE alt='icon' src='readstationsettings-vi.png']

#### Inputs/Outputs

| Semiconductor Module Manager — Semiconductor Module Manager is a valid ActiveX reference to a Semiconductor Module Manager object. error in (no error) — describes error conditions that occur before this VI or function runs. The default is no error. If an error occurred before this VI or function runs, the VI or function passes the error in (no error) Semiconductor Module Manager Out — returns the Semiconductor Module Manager parameter unchanged. Station Settings — returns a TestStand PropertyObject object that contains the station settings. error out — contains error information. If error in indicates that an error occurred before this VI or function ran, error out contains the same error information. Otherwise, it describes the error status that this VI or function produces. Right-click the error out front panel indicator and select Explain Error from the shortcut menu for more information about the error. |
| --- |

Parent topic:

Station Configuration

<!--NI_TOPIC bundle=tsm-labview-application-api-ref path=menus/categories/ni-semiconductormodule/semiconductormodulemanager/stationconfiguration/setnumberofsitestotest-vi.html language=enus -->
## TOPIC 00037: Set Number of Sites to Test

- bundle_id: `tsm-labview-application-api-ref`
- source_path: `menus/categories/ni-semiconductormodule/semiconductormodulemanager/stationconfiguration/setnumberofsitestotest-vi.html`
- source_url: https://docs-be.ni.com/bundle/tsm-labview-application-api-ref/raw/resource/enus/menus/categories/ni-semiconductormodule/semiconductormodulemanager/stationconfiguration/setnumberofsitestotest-vi.html
- document_id: `tsm-labview-application-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Sets the number of sites that TestStand uses to execute with the Batch or Parallel process models. This method sets the Number of Test Sockets setting in the model options. Although TestStand starts executing with the number of sites returned by this method, TSM might reduce the number of sites at r

### Set Number of Sites to Test

Sets the number of sites that TestStand uses to execute with the Batch or Parallel process models.
 This method sets the Number of Test Sockets setting in the model options.
 Although TestStand starts executing with the number of sites returned by this method,
 TSM might reduce the number of sites at run time based on the number of sites in the current pin map
 and the contents of the AvailableSiteNumbers station setting.

[IMAGE alt='icon' src='setnumberofsitestotest-vi.png']

#### Inputs/Outputs

| Semiconductor Module Manager — Semiconductor Module Manager is a valid ActiveX reference to a Semiconductor Module Manager object. Number of Sites — Number of Sites The number of sites for TestStand to use to execute with the Batch or Parallel process models. error in (no error) — describes error conditions that occur before this VI or function runs. The default is no error. If an error occurred before this VI or function runs, the VI or function passes the error in (no error) Semiconductor Module Manager Out — returns the Semiconductor Module Manager parameter unchanged. error out — contains error information. If error in indicates that an error occurred before this VI or function ran, error out contains the same error information. Otherwise, it describes the error status that this VI or function produces. Right-click the error out front panel indicator and select Explain Error from the shortcut menu for more information about the error. |
| --- |

Parent topic:

Station Configuration

<!--NI_TOPIC bundle=tsm-labview-application-api-ref path=menus/categories/ni-semiconductormodule/semiconductormodulemanager/stationconfiguration/stationconfiguration-mnu.html language=enus -->
## TOPIC 00038: Station Configuration

- bundle_id: `tsm-labview-application-api-ref`
- source_path: `menus/categories/ni-semiconductormodule/semiconductormodulemanager/stationconfiguration/stationconfiguration-mnu.html`
- source_url: https://docs-be.ni.com/bundle/tsm-labview-application-api-ref/raw/resource/enus/menus/categories/ni-semiconductormodule/semiconductormodulemanager/stationconfiguration/stationconfiguration-mnu.html
- document_id: `tsm-labview-application-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Use the Station Configuration VIs to get information about the station and lot settings. icon

### Station Configuration

Use the Station Configuration VIs to get information about the station and lot settings.

[IMAGE alt='icon' src='stationconfiguration-mnu.png']

- [Can Configure Handler/Prober?](../../../../../menus/categories/ni-semiconductormodule/semiconductormodulemanager/stationconfiguration/canconfigurehandlerdriver-vi.html) Determines whether you can configure the handler/prober driver the Handler/Prober Driver Path parameter specifies. The handler/prober driver sequence file must contain a Configure entrypoint sequence for you to configure the handler/prober driver. Use the Display Configure Handler/Prober Dialog VI to configure the handler/prober driver.
- [Display Configure Handler/Prober Dialog](../../../../../menus/categories/ni-semiconductormodule/semiconductormodulemanager/stationconfiguration/configurehandlerdialog-vi.html) Configures the handler/prober driver the Handler/Prober Driver Path parameter specifies by calling the Configure entry point sequence in the handler/prober driver sequence file. Typically, the Configure entry point sequence displays a handler/prober configuration dialog box. Use the Can Configure Handler? VI to determine if you can configure the handler/prober driver.
- [Get Actual Handler/Prober Driver Sequence File Path](../../../../../menus/categories/ni-semiconductormodule/semiconductormodulemanager/stationconfiguration/gethandlerdriversequencefilepath-vi.html) Returns the path of the handler/prober driver sequence file the Handler/Prober Mode and Handler/Prober Driver Path parameters specify. If the Handler/Prober Mode parameter is HandlerMode_Custom, this VI returns the value of the Handler/Prober Driver Path parameter. If the Handler/Prober Mode parameter is HandlerMode_Simulated, this VI returns the absolute path of the TSM simulated handler driver. If the Handler/Prober Mode parameter is HandlerMode_None, this VI returns an empty string.
- [Get Handler/Prober Driver Paths](../../../../../menus/categories/ni-semiconductormodule/semiconductormodulemanager/stationconfiguration/gethandlerdriversequencefilepaths-vi.html) Returns the paths and display names of all the available handler/prober driver sequence files. Handler/prober driver sequence files reside in the TestStandPublic\Components\Modules\NI_SemiconductorModule\Handlers directory.
- [Get Inline QA Algorithm Paths](../../../../../menus/categories/ni-semiconductormodule/semiconductormodulemanager/stationconfiguration/getinlineqaalgorithmsequencefilepaths-vi.html) Returns the paths and display names of all the available inline QA algorithm sequence files. Inline QA algorithm sequence files reside in the TestStandPublic\Components\Modules\NI_SemiconductorModule\InlineQA directory.
- [Read Lot Settings](../../../../../menus/categories/ni-semiconductormodule/semiconductormodulemanager/stationconfiguration/readlotsettings-vi.html) Returns a TestStand PropertyObject that contains the lot settings stored in the lot settings configuration file. If the lot settings configuration file does not exist, this VI returns the default lot settings by creating a new instance of the NI_SemiconductorModule_LotSettings TestStand data type.
- [Read Station Settings](../../../../../menus/categories/ni-semiconductormodule/semiconductormodulemanager/stationconfiguration/readstationsettings-vi.html) Returns a TestStand PropertyObject that contains the station settings stored in the station settings configuration file. If the station settings configuration file does not exist, this VI returns the default station settings by creating a new instance of the NI_SemiconductorModule_StationSettings TestStand data type.
- [Set Number of Sites to Test](../../../../../menus/categories/ni-semiconductormodule/semiconductormodulemanager/stationconfiguration/setnumberofsitestotest-vi.html) Sets the number of sites that TestStand uses to execute with the Batch or Parallel process models. This method sets the Number of Test Sockets setting in the model options. Although TestStand starts executing with the number of sites returned by this method, TSM might reduce the number of sites at run time based on the number of sites in the current pin map and the contents of the AvailableSiteNumbers station setting.
- [Get Number of Sites to Test](../../../../../menus/categories/ni-semiconductormodule/semiconductormodulemanager/stationconfiguration/getnumberofsitestotest-vi.html) Returns the number of sites that TestStand uses to execute with the Batch or Parallel process models. This method returns the Number of Test Sockets setting in the model options. Although TestStand starts executing with the number of sites returned by this method, TSM might reduce the number of sites at run time based on the number of sites in the current pin map and the contents of the AvailableSiteNumbers station setting.

Parent topic:

Application Development

<!--NI_TOPIC bundle=tsm-labview-application-api-ref path=menus/categories/ni-semiconductormodule/semiconductormodulemanager/testprogram/getactualsitecount-vi.html language=enus -->
## TOPIC 00039: Get Site Counts

- bundle_id: `tsm-labview-application-api-ref`
- source_path: `menus/categories/ni-semiconductormodule/semiconductormodulemanager/testprogram/getactualsitecount-vi.html`
- source_url: https://docs-be.ni.com/bundle/tsm-labview-application-api-ref/raw/resource/enus/menus/categories/ni-semiconductormodule/semiconductormodulemanager/testprogram/getactualsitecount-vi.html
- document_id: `tsm-labview-application-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the actual number of sites that will be used to run the test program. The actual number depends on the number of sites in the pin map and the number of sites configured in the station settings. icon Inputs/Outputs coarn.png Semiconductor Module Manager Semiconductor Module Manager is a valid

### Get Site Counts

Returns the actual number of sites that will be used to run the test program. The actual number depends on the number of sites in the pin map and the number of sites configured in the station settings.

[IMAGE alt='icon' src='getactualsitecount-vi.png']

#### Inputs/Outputs

| Semiconductor Module Manager — Semiconductor Module Manager is a valid ActiveX reference to a Semiconductor Module Manager object. Test Program Path — Test Program Path is the path of the test program sequence file. Configuration Name — Configuration Name is the name of the test program configuration. error in (no error) — describes error conditions that occur before this VI or function runs. The default is no error. If an error occurred before this VI or function runs, the VI or function passes the error in (no error) Semiconductor Module Manager Out — returns the Semiconductor Module Manager parameter unchanged. Actual Site Count — returns the actual number of sites that will be used to run the test program. The actual number depends on the number of sites in the pin map and the number of sites configured in the station settings. Pin Map Site Count — returns the number of sites in the pin map associated with the test program. error out — contains error information. If error in indicates that an error occurred before this VI or function ran, error out contains the same error information. Otherwise, it describes the error status that this VI or function produces. Right-click the error out front panel indicator and select Explain Error from the shortcut menu for more information about the error. |
| --- |

Parent topic:

Test Program

<!--NI_TOPIC bundle=tsm-labview-application-api-ref path=menus/categories/ni-semiconductormodule/semiconductormodulemanager/testprogram/getcurrentsitenumbers-vi.html language=enus -->
## TOPIC 00040: Get Site Numbers

- bundle_id: `tsm-labview-application-api-ref`
- source_path: `menus/categories/ni-semiconductormodule/semiconductormodulemanager/testprogram/getcurrentsitenumbers-vi.html`
- source_url: https://docs-be.ni.com/bundle/tsm-labview-application-api-ref/raw/resource/enus/menus/categories/ni-semiconductormodule/semiconductormodulemanager/testprogram/getcurrentsitenumbers-vi.html
- document_id: `tsm-labview-application-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the current site numbers that are being used to run the test program. The site numbers used depend on the number of sites in the pin map and the AvailableSiteNumbers property configured in the station settings. icon Inputs/Outputs coarn.png Semiconductor Module Manager Semiconductor Module M

### Get Site Numbers

Returns the current site numbers that are being used to run the test program. The site numbers used depend on the number of sites in the pin map and the AvailableSiteNumbers property configured in the station settings.

[IMAGE alt='icon' src='getcurrentsitenumbers-vi.png']

#### Inputs/Outputs

| Semiconductor Module Manager — Semiconductor Module Manager is a valid ActiveX reference to a Semiconductor Module Manager object. error in (no error) — describes error conditions that occur before this VI or function runs. The default is no error. If an error occurred before this VI or function runs, the VI or function passes the error in (no error) Semiconductor Module Manager Out — returns the Semiconductor Module Manager parameter unchanged. Site Numbers — returns an array of the current site numbers that are being used to run the test program. The site numbers depend on the number of sites in the pin map and the AvailableSiteNumbers property configured in the station settings. error out — contains error information. If error in indicates that an error occurred before this VI or function ran, error out contains the same error information. Otherwise, it describes the error status that this VI or function produces. Right-click the error out front panel indicator and select Explain Error from the shortcut menu for more information about the error. |
| --- |

Parent topic:

Test Program

<!--NI_TOPIC bundle=tsm-labview-application-api-ref path=menus/categories/ni-semiconductormodule/semiconductormodulemanager/testprogram/getspecificationsfilepaths-vi.html language=enus -->
## TOPIC 00041: Get Specifications File Paths

- bundle_id: `tsm-labview-application-api-ref`
- source_path: `menus/categories/ni-semiconductormodule/semiconductormodulemanager/testprogram/getspecificationsfilepaths-vi.html`
- source_url: https://docs-be.ni.com/bundle/tsm-labview-application-api-ref/raw/resource/enus/menus/categories/ni-semiconductormodule/semiconductormodulemanager/testprogram/getspecificationsfilepaths-vi.html
- document_id: `tsm-labview-application-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the paths of all the specifications files associated with the current test program. icon Inputs/Outputs coarn.png Semiconductor Module Manager Semiconductor Module Manager is a valid ActiveX reference to a Semiconductor Module Manager object. cerrcodeclst.png error in (no error) describes er

### Get Specifications File Paths

Returns the paths of all the specifications files associated with the current test program.

[IMAGE alt='icon' src='getspecificationsfilepaths-vi.png']

#### Inputs/Outputs

| Semiconductor Module Manager — Semiconductor Module Manager is a valid ActiveX reference to a Semiconductor Module Manager object. error in (no error) — describes error conditions that occur before this VI or function runs. The default is no error. If an error occurred before this VI or function runs, the VI or function passes the error in (no error) Semiconductor Module Manager Out — returns the Semiconductor Module Manager parameter unchanged. Specifications File Paths — returns the list of specifications file paths. error out — contains error information. If error in indicates that an error occurred before this VI or function ran, error out contains the same error information. Otherwise, it describes the error status that this VI or function produces. Right-click the error out front panel indicator and select Explain Error from the shortcut menu for more information about the error. |
| --- |

Parent topic:

Test Program

<!--NI_TOPIC bundle=tsm-labview-application-api-ref path=menus/categories/ni-semiconductormodule/semiconductormodulemanager/testprogram/gettestconditionvalue-vi.html language=enus -->
## TOPIC 00042: Get Test Condition Value

- bundle_id: `tsm-labview-application-api-ref`
- source_path: `menus/categories/ni-semiconductormodule/semiconductormodulemanager/testprogram/gettestconditionvalue-vi.html`
- source_url: https://docs-be.ni.com/bundle/tsm-labview-application-api-ref/raw/resource/enus/menus/categories/ni-semiconductormodule/semiconductormodulemanager/testprogram/gettestconditionvalue-vi.html
- document_id: `tsm-labview-application-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the test condition value for the specified configuration in the test program. icon

### Get Test Condition Value

Returns the test condition value for the specified configuration in the test program.

[IMAGE alt='icon' src='gettestconditionvalue-vi.png']

- [Get Test Condition Value Boolean](../../../../../menus/categories/ni-semiconductormodule/semiconductormodulemanager/testprogram/gettestconditionvalueboolean-vi.html) Returns the test condition Boolean value for the specified configuration in the test program. If the test condition does not exist or is not a Boolean value, this VI returns an error.
- [Get Test Condition Value Number](../../../../../menus/categories/ni-semiconductormodule/semiconductormodulemanager/testprogram/gettestconditionvaluenumber-vi.html) Returns the test condition number value for the specified configuration in the test program. If the test condition does not exist or is not a number value, this VI returns an error.
- [Get Test Condition Value String](../../../../../menus/categories/ni-semiconductormodule/semiconductormodulemanager/testprogram/gettestconditionvaluestring-vi.html) Returns the test condition string value for the specified configuration in the test program. If the test condition does not exist or is not a string value, this VI returns an error.

Parent topic:

Test Program

<!--NI_TOPIC bundle=tsm-labview-application-api-ref path=menus/categories/ni-semiconductormodule/semiconductormodulemanager/testprogram/gettestconditionvalueboolean-vi.html language=enus -->
## TOPIC 00043: Get Test Condition Value Boolean

- bundle_id: `tsm-labview-application-api-ref`
- source_path: `menus/categories/ni-semiconductormodule/semiconductormodulemanager/testprogram/gettestconditionvalueboolean-vi.html`
- source_url: https://docs-be.ni.com/bundle/tsm-labview-application-api-ref/raw/resource/enus/menus/categories/ni-semiconductormodule/semiconductormodulemanager/testprogram/gettestconditionvalueboolean-vi.html
- document_id: `tsm-labview-application-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the test condition Boolean value for the specified configuration in the test program. If the test condition does not exist or is not a Boolean value, this VI returns an error. icon Inputs/Outputs coarn.png Semiconductor Module Manager Semiconductor Module Manager is a valid ActiveX reference

### Get Test Condition Value Boolean

Returns the test condition Boolean value for the specified configuration in the test program. If the test condition does not exist or is not a Boolean value, this VI returns an error.

[IMAGE alt='icon' src='gettestconditionvalueboolean-vi.png']

#### Inputs/Outputs

| Semiconductor Module Manager — Semiconductor Module Manager is a valid ActiveX reference to a Semiconductor Module Manager object. Test Program Path — Test Program Path is the path of the test program sequence file. Configuration Name — Configuration Name is the name of the test program configuration. error in (no error) — describes error conditions that occur before this VI or function runs. The default is no error. If an error occurred before this VI or function runs, the VI or function passes the error in (no error) Test Condition Name — Test Condition Name is the name of the test condition. Semiconductor Module Manager Out — returns the Semiconductor Module Manager parameter unchanged. Test Condition Value — returns the value of the test condition from the configuration in the test program. error out — contains error information. If error in indicates that an error occurred before this VI or function ran, error out contains the same error information. Otherwise, it describes the error status that this VI or function produces. Right-click the error out front panel indicator and select Explain Error from the shortcut menu for more information about the error. |
| --- |

Parent topic:

Get Test Condition Value

<!--NI_TOPIC bundle=tsm-labview-application-api-ref path=menus/categories/ni-semiconductormodule/semiconductormodulemanager/testprogram/gettestconditionvaluenumber-vi.html language=enus -->
## TOPIC 00044: Get Test Condition Value Number

- bundle_id: `tsm-labview-application-api-ref`
- source_path: `menus/categories/ni-semiconductormodule/semiconductormodulemanager/testprogram/gettestconditionvaluenumber-vi.html`
- source_url: https://docs-be.ni.com/bundle/tsm-labview-application-api-ref/raw/resource/enus/menus/categories/ni-semiconductormodule/semiconductormodulemanager/testprogram/gettestconditionvaluenumber-vi.html
- document_id: `tsm-labview-application-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the test condition number value for the specified configuration in the test program. If the test condition does not exist or is not a number value, this VI returns an error. icon Inputs/Outputs coarn.png Semiconductor Module Manager Semiconductor Module Manager is a valid ActiveX reference t

### Get Test Condition Value Number

Returns the test condition number value for the specified configuration in the test program. If the test condition does not exist or is not a number value, this VI returns an error.

[IMAGE alt='icon' src='gettestconditionvaluenumber-vi.png']

#### Inputs/Outputs

| Semiconductor Module Manager — Semiconductor Module Manager is a valid ActiveX reference to a Semiconductor Module Manager object. Test Program Path — Test Program Path is the path of the test program sequence file. Configuration Name — Configuration Name is the name of the test program configuration. error in (no error) — describes error conditions that occur before this VI or function runs. The default is no error. If an error occurred before this VI or function runs, the VI or function passes the error in (no error) Test Condition Name — Test Condition Name is the name of the test condition. Semiconductor Module Manager Out — returns the Semiconductor Module Manager parameter unchanged. Test Condition Value — returns the value of the test condition from the configuration in the test program. error out — contains error information. If error in indicates that an error occurred before this VI or function ran, error out contains the same error information. Otherwise, it describes the error status that this VI or function produces. Right-click the error out front panel indicator and select Explain Error from the shortcut menu for more information about the error. |
| --- |

Parent topic:

Get Test Condition Value

<!--NI_TOPIC bundle=tsm-labview-application-api-ref path=menus/categories/ni-semiconductormodule/semiconductormodulemanager/testprogram/gettestconditionvaluestring-vi.html language=enus -->
## TOPIC 00045: Get Test Condition Value String

- bundle_id: `tsm-labview-application-api-ref`
- source_path: `menus/categories/ni-semiconductormodule/semiconductormodulemanager/testprogram/gettestconditionvaluestring-vi.html`
- source_url: https://docs-be.ni.com/bundle/tsm-labview-application-api-ref/raw/resource/enus/menus/categories/ni-semiconductormodule/semiconductormodulemanager/testprogram/gettestconditionvaluestring-vi.html
- document_id: `tsm-labview-application-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the test condition string value for the specified configuration in the test program. If the test condition does not exist or is not a string value, this VI returns an error. icon Inputs/Outputs coarn.png Semiconductor Module Manager Semiconductor Module Manager is a valid ActiveX reference t

### Get Test Condition Value String

Returns the test condition string value for the specified configuration in the test program. If the test condition does not exist or is not a string value, this VI returns an error.

[IMAGE alt='icon' src='gettestconditionvaluestring-vi.png']

#### Inputs/Outputs

| Semiconductor Module Manager — Semiconductor Module Manager is a valid ActiveX reference to a Semiconductor Module Manager object. Test Program Path — Test Program Path is the path of the test program sequence file. Configuration Name — Configuration Name is the name of the test program configuration. error in (no error) — describes error conditions that occur before this VI or function runs. The default is no error. If an error occurred before this VI or function runs, the VI or function passes the error in (no error) Test Condition Name — Test Condition Name is the name of the test condition. Semiconductor Module Manager Out — returns the Semiconductor Module Manager parameter unchanged. Test Condition Value — returns the value of the test condition from the configuration in the test program. error out — contains error information. If error in indicates that an error occurred before this VI or function ran, error out contains the same error information. Otherwise, it describes the error status that this VI or function produces. Right-click the error out front panel indicator and select Explain Error from the shortcut menu for more information about the error. |
| --- |

Parent topic:

Get Test Condition Value

<!--NI_TOPIC bundle=tsm-labview-application-api-ref path=menus/categories/ni-semiconductormodule/semiconductormodulemanager/testprogram/gettestprogramconfigurationnames-vi.html language=enus -->
## TOPIC 00046: Get Test Program Configurations

- bundle_id: `tsm-labview-application-api-ref`
- source_path: `menus/categories/ni-semiconductormodule/semiconductormodulemanager/testprogram/gettestprogramconfigurationnames-vi.html`
- source_url: https://docs-be.ni.com/bundle/tsm-labview-application-api-ref/raw/resource/enus/menus/categories/ni-semiconductormodule/semiconductormodulemanager/testprogram/gettestprogramconfigurationnames-vi.html
- document_id: `tsm-labview-application-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the list of configuration names in the specified test program sequence file. icon Inputs/Outputs coarn.png Semiconductor Module Manager Semiconductor Module Manager is a valid ActiveX reference to a Semiconductor Module Manager object. cpath.png Test Program Path Test Program Path is the pat

### Get Test Program Configurations

Returns the list of configuration names in the specified test program sequence file.

[IMAGE alt='icon' src='gettestprogramconfigurationnames-vi.png']

#### Inputs/Outputs

| Semiconductor Module Manager — Semiconductor Module Manager is a valid ActiveX reference to a Semiconductor Module Manager object. Test Program Path — Test Program Path is the path of the test program sequence file. error in (no error) — describes error conditions that occur before this VI or function runs. The default is no error. If an error occurred before this VI or function runs, the VI or function passes the error in (no error) Semiconductor Module Manager Out — returns the Semiconductor Module Manager parameter unchanged. Test Program Configuration Names — returns the list of configuration names in the specified test program sequence file. error out — contains error information. If error in indicates that an error occurred before this VI or function ran, error out contains the same error information. Otherwise, it describes the error status that this VI or function produces. Right-click the error out front panel indicator and select Explain Error from the shortcut menu for more information about the error. |
| --- |

Parent topic:

Test Program

<!--NI_TOPIC bundle=tsm-labview-application-api-ref path=menus/categories/ni-semiconductormodule/semiconductormodulemanager/testprogram/gettestprogrammodelsequencefilepath-vi.html language=enus -->
## TOPIC 00047: Get Test Program Model Sequence File Path

- bundle_id: `tsm-labview-application-api-ref`
- source_path: `menus/categories/ni-semiconductormodule/semiconductormodulemanager/testprogram/gettestprogrammodelsequencefilepath-vi.html`
- source_url: https://docs-be.ni.com/bundle/tsm-labview-application-api-ref/raw/resource/enus/menus/categories/ni-semiconductormodule/semiconductormodulemanager/testprogram/gettestprogrammodelsequencefilepath-vi.html
- document_id: `tsm-labview-application-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the absolute path of the process model sequence file associated with the specified test program sequence file. If the test program Model Option is Use Station Model, this method returns the path of the TestStand Station Model. This method returns an empty path if the test program does not ha

### Get Test Program Model Sequence File Path

Returns the absolute path of the process model sequence file associated with the specified test program sequence file. If the test program Model Option is Use Station Model, this method returns the path of the TestStand Station Model. This method returns an empty path if the test program does not have a model or if the test program is invalid.

[IMAGE alt='icon' src='gettestprogrammodelsequencefilepath-vi.png']

#### Inputs/Outputs

| Semiconductor Module Manager — Semiconductor Module Manager is a valid ActiveX reference to a Semiconductor Module Manager object. Test Program Path — Test Program Path is the path of the test program sequence file. error in (no error) — describes error conditions that occur before this VI or function runs. The default is no error. If an error occurred before this VI or function runs, the VI or function passes the error in (no error) Semiconductor Module Manager Out — returns the Semiconductor Module Manager parameter unchanged. Model Sequence File Path — returns the absolute path of the process model sequence file associated with the specified test program sequence file. error out — contains error information. If error in indicates that an error occurred before this VI or function ran, error out contains the same error information. Otherwise, it describes the error status that this VI or function produces. Right-click the error out front panel indicator and select Explain Error from the shortcut menu for more information about the error. |
| --- |

Parent topic:

Test Program

<!--NI_TOPIC bundle=tsm-labview-application-api-ref path=menus/categories/ni-semiconductormodule/semiconductormodulemanager/testprogram/gettestprogramsequencefilepaths-vi.html language=enus -->
## TOPIC 00048: Get Test Program Paths

- bundle_id: `tsm-labview-application-api-ref`
- source_path: `menus/categories/ni-semiconductormodule/semiconductormodulemanager/testprogram/gettestprogramsequencefilepaths-vi.html`
- source_url: https://docs-be.ni.com/bundle/tsm-labview-application-api-ref/raw/resource/enus/menus/categories/ni-semiconductormodule/semiconductormodulemanager/testprogram/gettestprogramsequencefilepaths-vi.html
- document_id: `tsm-labview-application-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the paths and display names of all the available test program sequence files. The test program sequence files reside in the directory the TestProgramDirectory standard station setting specifies. If the TestProgramDirectory setting is empty or invalid, this VI returns an empty list. icon Inpu

### Get Test Program Paths

Returns the paths and display names of all the available test program sequence files. The test program sequence files reside in the directory the TestProgramDirectory standard station setting specifies. If the TestProgramDirectory setting is empty or invalid, this VI returns an empty list.

[IMAGE alt='icon' src='gettestprogramsequencefilepaths-vi.png']

#### Inputs/Outputs

| Semiconductor Module Manager — Semiconductor Module Manager is a valid ActiveX reference to a Semiconductor Module Manager object. error in (no error) — describes error conditions that occur before this VI or function runs. The default is no error. If an error occurred before this VI or function runs, the VI or function passes the error in (no error) Semiconductor Module Manager Out — returns the Semiconductor Module Manager parameter unchanged. Test Program Sequence File Paths — returns the list of test program sequence file paths. Test Program Display Names — returns the list of test program display names. The test program display names are the base filenames without the file extension. error out — contains error information. If error in indicates that an error occurred before this VI or function ran, error out contains the same error information. Otherwise, it describes the error status that this VI or function produces. Right-click the error out front panel indicator and select Explain Error from the shortcut menu for more information about the error. |
| --- |

Parent topic:

Test Program

<!--NI_TOPIC bundle=tsm-labview-application-api-ref path=menus/categories/ni-semiconductormodule/semiconductormodulemanager/testprogram/inperformancemeasurementsession-vi.html language=enus -->
## TOPIC 00049: In Performance Measurement Session?

- bundle_id: `tsm-labview-application-api-ref`
- source_path: `menus/categories/ni-semiconductormodule/semiconductormodulemanager/testprogram/inperformancemeasurementsession-vi.html`
- source_url: https://docs-be.ni.com/bundle/tsm-labview-application-api-ref/raw/resource/enus/menus/categories/ni-semiconductormodule/semiconductormodulemanager/testprogram/inperformancemeasurementsession-vi.html
- document_id: `tsm-labview-application-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns true if the sequence editor is waiting for a performance measurement session to be completed. TSM sets this property to true before it launches the OI session that will measure the performance and sets it to false when the OI process exits. icon Inputs/Outputs coarn.png Semiconductor Module

### In Performance Measurement Session?

Returns true if the sequence editor is waiting for a performance measurement session to be completed. TSM sets this property to true before it launches the OI session that will measure the performance and sets it to false when the OI process exits.

[IMAGE alt='icon' src='inperformancemeasurementsession-vi.png']

#### Inputs/Outputs

| Semiconductor Module Manager — Semiconductor Module Manager is a valid ActiveX reference to a Semiconductor Module Manager object. error in (no error) — describes error conditions that occur before this VI or function runs. The default is no error. If an error occurred before this VI or function runs, the VI or function passes the error in (no error) Semiconductor Module Manager Out — returns the Semiconductor Module Manager parameter unchanged. In Performance Measurement Session — returns whether the sequence editor is waiting for a performance measurement session to be completed. error out — contains error information. If error in indicates that an error occurred before this VI or function ran, error out contains the same error information. Otherwise, it describes the error status that this VI or function produces. Right-click the error out front panel indicator and select Explain Error from the shortcut menu for more information about the error. |
| --- |

Parent topic:

Test Program

<!--NI_TOPIC bundle=tsm-labview-application-api-ref path=menus/categories/ni-semiconductormodule/semiconductormodulemanager/testprogram/testprogram-mnu.html language=enus -->
## TOPIC 00050: Test Program

- bundle_id: `tsm-labview-application-api-ref`
- source_path: `menus/categories/ni-semiconductormodule/semiconductormodulemanager/testprogram/testprogram-mnu.html`
- source_url: https://docs-be.ni.com/bundle/tsm-labview-application-api-ref/raw/resource/enus/menus/categories/ni-semiconductormodule/semiconductormodulemanager/testprogram/testprogram-mnu.html
- document_id: `tsm-labview-application-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Use the Test Program VIs to access information about a test program. icon

### Test Program

Use the Test Program VIs to access information about a test program.

[IMAGE alt='icon' src='testprogram-mnu.png']

- [Get Site Counts](../../../../../menus/categories/ni-semiconductormodule/semiconductormodulemanager/testprogram/getactualsitecount-vi.html) Returns the actual number of sites that will be used to run the test program. The actual number depends on the number of sites in the pin map and the number of sites configured in the station settings.
- [Get Site Numbers](../../../../../menus/categories/ni-semiconductormodule/semiconductormodulemanager/testprogram/getcurrentsitenumbers-vi.html) Returns the current site numbers that are being used to run the test program. The site numbers used depend on the number of sites in the pin map and the AvailableSiteNumbers property configured in the station settings.
- [Test Program Contains Test Condition?](../../../../../menus/categories/ni-semiconductormodule/semiconductormodulemanager/testprogram/testprogramcontainstestcondition-vi.html) Returns True if the test program contains the specified test condition.
- [Get Test Condition Value](../../../../../menus/categories/ni-semiconductormodule/semiconductormodulemanager/testprogram/gettestconditionvalue-vi.html) Returns the test condition value for the specified configuration in the test program.
- [Get Test Program Model Sequence File Path](../../../../../menus/categories/ni-semiconductormodule/semiconductormodulemanager/testprogram/gettestprogrammodelsequencefilepath-vi.html) Returns the absolute path of the process model sequence file associated with the specified test program sequence file. If the test program Model Option is Use Station Model, this method returns the path of the TestStand Station Model. This method returns an empty path if the test program does not have a model or if the test program is invalid.
- [Get Test Program Configurations](../../../../../menus/categories/ni-semiconductormodule/semiconductormodulemanager/testprogram/gettestprogramconfigurationnames-vi.html) Returns the list of configuration names in the specified test program sequence file.
- [Validate Test Program](../../../../../menus/categories/ni-semiconductormodule/semiconductormodulemanager/testprogram/validatetestprogram-vi.html) Validates the specified test program and configuration.
- [Get Test Program Paths](../../../../../menus/categories/ni-semiconductormodule/semiconductormodulemanager/testprogram/gettestprogramsequencefilepaths-vi.html) Returns the paths and display names of all the available test program sequence files. The test program sequence files reside in the directory the TestProgramDirectory standard station setting specifies. If the TestProgramDirectory setting is empty or invalid, this VI returns an empty list.
- [Get Specifications File Paths](../../../../../menus/categories/ni-semiconductormodule/semiconductormodulemanager/testprogram/getspecificationsfilepaths-vi.html) Returns the paths of all the specifications files associated with the current test program.
- [In Performance Measurement Session?](../../../../../menus/categories/ni-semiconductormodule/semiconductormodulemanager/testprogram/inperformancemeasurementsession-vi.html) Returns true if the sequence editor is waiting for a performance measurement session to be completed. TSM sets this property to true before it launches the OI session that will measure the performance and sets it to false when the OI process exits.

Parent topic:

Application Development

<!--NI_TOPIC bundle=tsm-labview-application-api-ref path=menus/categories/ni-semiconductormodule/semiconductormodulemanager/testprogram/testprogramcontainstestcondition-vi.html language=enus -->
## TOPIC 00051: Test Program Contains Test Condition?

- bundle_id: `tsm-labview-application-api-ref`
- source_path: `menus/categories/ni-semiconductormodule/semiconductormodulemanager/testprogram/testprogramcontainstestcondition-vi.html`
- source_url: https://docs-be.ni.com/bundle/tsm-labview-application-api-ref/raw/resource/enus/menus/categories/ni-semiconductormodule/semiconductormodulemanager/testprogram/testprogramcontainstestcondition-vi.html
- document_id: `tsm-labview-application-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns True if the test program contains the specified test condition. icon Inputs/Outputs coarn.png Semiconductor Module Manager Semiconductor Module Manager is a valid ActiveX reference to a Semiconductor Module Manager object. cpath.png Test Program Path Test Program Path is the path of the test

### Test Program Contains Test Condition?

Returns True if the test program contains the specified test condition.

[IMAGE alt='icon' src='testprogramcontainstestcondition-vi.png']

#### Inputs/Outputs

| Semiconductor Module Manager — Semiconductor Module Manager is a valid ActiveX reference to a Semiconductor Module Manager object. Test Program Path — Test Program Path is the path of the test program sequence file. Test Condition Name — Test Condition Name is the name of the test condition. error in (no error) — describes error conditions that occur before this VI or function runs. The default is no error. If an error occurred before this VI or function runs, the VI or function passes the error in (no error) Semiconductor Module Manager Out — returns the Semiconductor Module Manager parameter unchanged. Test Condition Exists? — returns True if the test program contains the specified test condition. error out — contains error information. If error in indicates that an error occurred before this VI or function ran, error out contains the same error information. Otherwise, it describes the error status that this VI or function produces. Right-click the error out front panel indicator and select Explain Error from the shortcut menu for more information about the error. |
| --- |

Parent topic:

Test Program

<!--NI_TOPIC bundle=tsm-labview-application-api-ref path=menus/categories/ni-semiconductormodule/semiconductormodulemanager/testprogram/validatetestprogram-vi.html language=enus -->
## TOPIC 00052: Validate Test Program

- bundle_id: `tsm-labview-application-api-ref`
- source_path: `menus/categories/ni-semiconductormodule/semiconductormodulemanager/testprogram/validatetestprogram-vi.html`
- source_url: https://docs-be.ni.com/bundle/tsm-labview-application-api-ref/raw/resource/enus/menus/categories/ni-semiconductormodule/semiconductormodulemanager/testprogram/validatetestprogram-vi.html
- document_id: `tsm-labview-application-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Validates the specified test program and configuration. icon Inputs/Outputs coarn.png Semiconductor Module Manager Semiconductor Module Manager is a valid ActiveX reference to a Semiconductor Module Manager object. cpath.png Test Program Path Test Program Path is the path of the test program sequenc

### Validate Test Program

Validates the specified test program and configuration.

[IMAGE alt='icon' src='validatetestprogram-vi.png']

#### Inputs/Outputs

| Semiconductor Module Manager — Semiconductor Module Manager is a valid ActiveX reference to a Semiconductor Module Manager object. Test Program Path — Test Program Path is the path of the test program sequence file. Configuration Name — Configuration Name is the name of the test program configuration. error in (no error) — describes error conditions that occur before this VI or function runs. The default is no error. If an error occurred before this VI or function runs, the VI or function passes the error in (no error) Semiconductor Module Manager Out — returns the Semiconductor Module Manager parameter unchanged. Is Valid? — returns whether the test program is valid. Error Message — returns an error message that describes the error if the test program is not valid. error out — contains error information. If error in indicates that an error occurred before this VI or function ran, error out contains the same error information. Otherwise, it describes the error status that this VI or function produces. Right-click the error out front panel indicator and select Explain Error from the shortcut menu for more information about the error. |
| --- |

Parent topic:

Test Program

<!--NI_TOPIC bundle=tsm-labview-application-api-ref path=Using_TSM_ApplicationAPI_inLV.html language=enus -->
## TOPIC 00053: Using the TSM Application API in LabVIEW Applications (TSM)

- bundle_id: `tsm-labview-application-api-ref`
- source_path: `Using_TSM_ApplicationAPI_inLV.html`
- source_url: https://docs-be.ni.com/bundle/tsm-labview-application-api-ref/raw/resource/enus/Using_TSM_ApplicationAPI_inLV.html
- document_id: `tsm-labview-application-api-ref`
- page_type: `leaf`
- content_type: `topic`
- source_description: TSM does not provide a full set of VIs for every TSM Application API method and property. You can access the methods and properties on the TSM Application API COM server using the LabVIEW ActiveX Invoke and Property nodes. The Application Development palette in LabVIEW includes a set of wrapper VIs

### Using the TSM Application API in LabVIEW Applications (TSM)

TSM does not provide a full set of VIs for every TSM Application API method and property. You can access the methods and properties on the TSM Application API COM server using the LabVIEW ActiveX Invoke and Property nodes. The Application Development palette in LabVIEW includes a set of wrapper VIs that use the TSM Application API COM server for some functionality. To access the wrapper VIs, add the SemiconductorModuleManager.mnu palette from the <LabVIEW>\vi.lib\NI_TestStand_SemiconductorModule\NI_TestStand_Semiconductor_Module.lvlibp project library to the palette in LabVIEW.

Refer to the **TestStand Semiconductor Module Application API** topic in the **TestStand Semiconductor Module Help** for more information about the TSM Application API. Select Help»TestStand Help and navigate to the TestStand Semiconductor Module book in the table of contents of the TestStand Help to launch the TestStand Semiconductor Module Help.
