# NI DOCUMENT BUNDLE: labview-vi-analyzer-toolkit-api-ref

<!--NI_BUNDLE_CHUNK bundle=labview-vi-analyzer-toolkit-api-ref start=1 end=19 -->
<!--NI_TOPIC bundle=labview-vi-analyzer-toolkit-api-ref path=lvvianalyzer/an_add_item.html language=enus -->
## TOPIC 00001: VIAn Add Item VI

- bundle_id: `labview-vi-analyzer-toolkit-api-ref`
- source_path: `lvvianalyzer/an_add_item.html`
- source_url: https://docs-be.ni.com/bundle/labview-vi-analyzer-toolkit-api-ref/raw/resource/enus/lvvianalyzer/an_add_item.html
- document_id: `labview-vi-analyzer-toolkit-api-ref`
- page_type: `leaf`
- content_type: ``

### VIAn Add Item VI

**Owning Palette:** [VI Analyzer Utilities VIs](../lvvianalyzer/vi_an_utilities_vis.html)

**Requires:** VI Analyzer Toolkit

Adds an item, such as a VI, LLB, or folder, to the VI Analyzer task.

[IMAGE alt='image' src='vian_add_item.gif']

|  | VI Analyzer Task in contains a reference to the current task. The VI Analyzer task must be a valid task that you created using the VIAn New Task VI. |
| --- | --- |
|  | Item to Add specifies the path to the VI, LLB, or folder you want to add to the VI Analyzer task. If you specify an LLB or folder, the VI adds all the VIs included in the LLB or folder to the VI Analyzer task. If you specify an invalid path or a path to an invalid item, the VI returns an error. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | VI Analyzer Task out returns a reference to the VI Analyzer task specified in VI Analyzer Task in. |
|  | error out contains error information. This output provides standard error out functionality. |

<!--NI_TOPIC bundle=labview-vi-analyzer-toolkit-api-ref path=lvvianalyzer/an_destroy_task.html language=enus -->
## TOPIC 00002: VIAn Destroy Task VI

- bundle_id: `labview-vi-analyzer-toolkit-api-ref`
- source_path: `lvvianalyzer/an_destroy_task.html`
- source_url: https://docs-be.ni.com/bundle/labview-vi-analyzer-toolkit-api-ref/raw/resource/enus/lvvianalyzer/an_destroy_task.html
- document_id: `labview-vi-analyzer-toolkit-api-ref`
- page_type: `leaf`
- content_type: ``

### VIAn Destroy Task VI

**Owning Palette:** [VI Analyzer VIs](../lvvianalyzer/vi_analyzer_vis.html)

**Requires:** VI Analyzer Toolkit

Closes an existing VI Analyzer task reference and releases resources associated with the task.

[IMAGE alt='image' src='vian_destroy_task.gif']

|  | VI Analyzer Task in contains a reference to the current task. The VI Analyzer task must be a valid task that you created using the VIAn New Task VI. |
| --- | --- |
|  | error in describes error conditions that occur before this node runs. With the following exception, this input provides standard error in functionality. This node runs normally even if an error occurred before this node runs. |
|  | error out contains error information. This output provides standard error out functionality. |

<!--NI_TOPIC bundle=labview-vi-analyzer-toolkit-api-ref path=lvvianalyzer/an_easy_analyze.html language=enus -->
## TOPIC 00003: VIAn Easy Analyze VI

- bundle_id: `labview-vi-analyzer-toolkit-api-ref`
- source_path: `lvvianalyzer/an_easy_analyze.html`
- source_url: https://docs-be.ni.com/bundle/labview-vi-analyzer-toolkit-api-ref/raw/resource/enus/lvvianalyzer/an_easy_analyze.html
- document_id: `labview-vi-analyzer-toolkit-api-ref`
- page_type: `leaf`
- content_type: ``

### VIAn Easy Analyze VI

**Owning Palette:** [VI Analyzer VIs](../lvvianalyzer/vi_analyzer_vis.html)

**Requires:** VI Analyzer Toolkit

Runs a VI Analyzer task automatically using settings in the specified configuration file.

[IMAGE alt='image' src='vian_easy_analyze.gif']

|  | Analysis Target specifies the path to the configuration file that contains VI Analyzer task settings to use in the analysis. You can use a configuration file you saved through the VI Analyzer or the VI Analyzer VIs. Alternatively, you can specify a VI, folder, or LLB to analyze. If you specify an item other than a configuration file, the VI runs all VI Analyzer tests on the specified item. |
| --- | --- |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | Configuration File Password contains the password for the configuration file specified in Analysis Target. This input is valid only when specifying a legacy .cfg file that is password-protected. |
|  | Analysis Results returns the results of the VI Analyzer task. Wire this output to the Analysis Results input of the VIAn Easy Report VI. Raw Results contains the unparsed results data for every test and every VI in the VI Analyzer task. Test Name displays the name of the test. Results Data contains the unparsed results for the test specified in Test Name. Status indicates whether the test in Test Name passed or failed. Exceed Max Fails? indicates whether the test in Test Name failed more than the maximum number of times specified for that test. Parsed Results Data (by VI) contains the results by VI for every test in the VI Analyzer task, including which tests passed and failed, which tests the VI Analyzer could not load or run, and which errors occurred. VI Path contains the path to the VI for which the test results are listed. Pass contains data on the tests that passed for the VI specified in VI Path. Fail contains data on the tests that failed for the VI specified in VI Path. Skipped contains data on the tests that the VI Analyzer skipped for the VI specified in VI Path. VI not loadable contains data on whether the VI Analyzer was able to load the VI specified in VI Path. Test not loadable contains data on the tests that the VI Analyzer was not able to load for the VI specified in VI Path. Test not runnable contains data on the tests that the VI Analyzer was not able to run for the VI specified in VI Path. Test error out contains data on errors that occurred when the VI Analyzer performed tests on the VI specified in VI Path. Parsed Results Data (by Test) contains the results of every test and whether the VI Analyzer passed, failed, or skipped the test for every VI in the VI Analyzer task. Test Name displays the name of the test. Pass contains data on each VI that passed the test specified in Test Name. Fail contains data on each VI that failed the test specified in Test Name. Skipped contains data on each VI for which the VI Analyzer skipped the test specified in Test Name. Summary Statistics contains the summary for a VI Analyzer task. Passed Tests indicates the total number of tests in the VI Analyzer task that passed. Failed Tests indicates the total number of tests in the VI Analyzer task that failed. Skipped Tests indicates the total number of tests in the VI Analyzer task that the VI Analyzer skipped. VIs not loadable indicates the total number of VIs that the VI Analyzer could not load. Tests not loadable indicates the total number of tests that the VI Analyzer was not able to load. Tests not runnable indicates the total number of tests that the VI Analyzer was not able to run. Test error out indicates the total number of errors that occurred during the analysis. Start Time indicates the time when the analysis began. Total Time (s) indicates the time it took for the VI Analyzer to run the analysis. Test Config Data contains the configuration settings for every test included in the VI Analyzer task. |
|  | Raw Results contains the unparsed results data for every test and every VI in the VI Analyzer task. Test Name displays the name of the test. Results Data contains the unparsed results for the test specified in Test Name. Status indicates whether the test in Test Name passed or failed. Exceed Max Fails? indicates whether the test in Test Name failed more than the maximum number of times specified for that test. |
|  | Test Name displays the name of the test. |
|  | Results Data contains the unparsed results for the test specified in Test Name. |
|  | Status indicates whether the test in Test Name passed or failed. |
|  | Exceed Max Fails? indicates whether the test in Test Name failed more than the maximum number of times specified for that test. |
|  | Parsed Results Data (by VI) contains the results by VI for every test in the VI Analyzer task, including which tests passed and failed, which tests the VI Analyzer could not load or run, and which errors occurred. VI Path contains the path to the VI for which the test results are listed. Pass contains data on the tests that passed for the VI specified in VI Path. Fail contains data on the tests that failed for the VI specified in VI Path. Skipped contains data on the tests that the VI Analyzer skipped for the VI specified in VI Path. VI not loadable contains data on whether the VI Analyzer was able to load the VI specified in VI Path. Test not loadable contains data on the tests that the VI Analyzer was not able to load for the VI specified in VI Path. Test not runnable contains data on the tests that the VI Analyzer was not able to run for the VI specified in VI Path. Test error out contains data on errors that occurred when the VI Analyzer performed tests on the VI specified in VI Path. |
|  | VI Path contains the path to the VI for which the test results are listed. |
|  | Pass contains data on the tests that passed for the VI specified in VI Path. |
|  | Fail contains data on the tests that failed for the VI specified in VI Path. |
|  | Skipped contains data on the tests that the VI Analyzer skipped for the VI specified in VI Path. |
|  | VI not loadable contains data on whether the VI Analyzer was able to load the VI specified in VI Path. |
|  | Test not loadable contains data on the tests that the VI Analyzer was not able to load for the VI specified in VI Path. |
|  | Test not runnable contains data on the tests that the VI Analyzer was not able to run for the VI specified in VI Path. |
|  | Test error out contains data on errors that occurred when the VI Analyzer performed tests on the VI specified in VI Path. |
|  | Parsed Results Data (by Test) contains the results of every test and whether the VI Analyzer passed, failed, or skipped the test for every VI in the VI Analyzer task. Test Name displays the name of the test. Pass contains data on each VI that passed the test specified in Test Name. Fail contains data on each VI that failed the test specified in Test Name. Skipped contains data on each VI for which the VI Analyzer skipped the test specified in Test Name. |
|  | Test Name displays the name of the test. |
|  | Pass contains data on each VI that passed the test specified in Test Name. |
|  | Fail contains data on each VI that failed the test specified in Test Name. |
|  | Skipped contains data on each VI for which the VI Analyzer skipped the test specified in Test Name. |
|  | Summary Statistics contains the summary for a VI Analyzer task. Passed Tests indicates the total number of tests in the VI Analyzer task that passed. Failed Tests indicates the total number of tests in the VI Analyzer task that failed. Skipped Tests indicates the total number of tests in the VI Analyzer task that the VI Analyzer skipped. VIs not loadable indicates the total number of VIs that the VI Analyzer could not load. Tests not loadable indicates the total number of tests that the VI Analyzer was not able to load. Tests not runnable indicates the total number of tests that the VI Analyzer was not able to run. Test error out indicates the total number of errors that occurred during the analysis. Start Time indicates the time when the analysis began. Total Time (s) indicates the time it took for the VI Analyzer to run the analysis. |
|  | Passed Tests indicates the total number of tests in the VI Analyzer task that passed. |
|  | Failed Tests indicates the total number of tests in the VI Analyzer task that failed. |
|  | Skipped Tests indicates the total number of tests in the VI Analyzer task that the VI Analyzer skipped. |
|  | VIs not loadable indicates the total number of VIs that the VI Analyzer could not load. |
|  | Tests not loadable indicates the total number of tests that the VI Analyzer was not able to load. |
|  | Tests not runnable indicates the total number of tests that the VI Analyzer was not able to run. |
|  | Test error out indicates the total number of errors that occurred during the analysis. |
|  | Start Time indicates the time when the analysis began. |
|  | Total Time (s) indicates the time it took for the VI Analyzer to run the analysis. |
|  | Test Config Data contains the configuration settings for every test included in the VI Analyzer task. |
|  | error out contains error information. This output provides standard error out functionality. |

<!--NI_TOPIC bundle=labview-vi-analyzer-toolkit-api-ref path=lvvianalyzer/an_easy_report.html language=enus -->
## TOPIC 00004: VIAn Easy Report VI

- bundle_id: `labview-vi-analyzer-toolkit-api-ref`
- source_path: `lvvianalyzer/an_easy_report.html`
- source_url: https://docs-be.ni.com/bundle/labview-vi-analyzer-toolkit-api-ref/raw/resource/enus/lvvianalyzer/an_easy_report.html
- document_id: `labview-vi-analyzer-toolkit-api-ref`
- page_type: `leaf`
- content_type: ``

### VIAn Easy Report VI

**Owning Palette:** [VI Analyzer VIs](../lvvianalyzer/vi_analyzer_vis.html)

**Requires:** VI Analyzer Toolkit

Exports the results of an analysis to a file, either as a report in ASCII or HTML format or as a VI Analyzer results file.

[IMAGE alt='image' src='vian_easy_report.gif']

|  | Overwrite Report? specifies whether the VI overwrites a report file if the file specified in Report Save Path already exists. The default is TRUE, which overwrites the file. If Overwrite Report? is FALSE and the file exists, the VI returns an error. |
| --- | --- |
|  | Report Save Path contains the path to the report or results file. If the path you specify is invalid, the VI returns an error. |
|  | Analysis Results contains the results from a VI Analyzer task you run using either the VIAn Easy Analyze VI or the VIAn Run VI. Wire the Analysis Results output of either VI to this input. Raw Results contains the unparsed results data for every test and every VI in the VI Analyzer task for which you want to create a report. Test Name contains the name of the test that the results reference. Results Data contains the unparsed results for the test specified in Test Name. Status indicates whether the test in Test Name passed or failed. Exceed Max Fails? indicates whether the test in Test Name failed more than the maximum number of times specified for that test. Parsed Results Data (by VI) contains the results by VI for every test in the VI Analyzer task, including which tests passed and failed, which tests the VI Analyzer could not load or run, and which errors occurred. VI Path contains the path to the VI for which the test results are listed. Pass contains data on the tests that passed for the VI specified in VI Path. Fail contains data on the tests that failed for the VI specified in VI Path. Skipped contains data on the tests the VI Analyzer skipped for the VI specified in VI Path. VI not loadable contains data on whether the VI Analyzer was able to load the VI specified in VI Path. Test not loadable contains data on the tests that the VI Analyzer was not able to load for the VI specified in VI Path. Test not runnable contains data on the tests that the VI Analyzer was not able to run for the VI specified in VI Path. Test error out contains data on errors that occurred when the VI Analyzer performed tests on the VI specified in VI Path. Parsed Results Data (by Test) contains the results of every test and whether the VI Analyzer passed, failed, or skipped the test for every VI in the VI Analyzer task. Test Name contains the name of the test that the results reference. Pass contains data on each VI that passed the test specified in Test Name. Fail contains data on each VI that failed the test specified in Test Name. Skipped contains data on each VI for which the VI Analyzer skipped the test specified in Test Name. Summary Statistics contains the summary for a VI Analyzer task on how many tests passed, failed, or were skipped; how many VIs and tests the VI Analyzer could not load or run; the total number of test errors; and the start time and elapsed time of the analysis. Passed Tests contains the total number of tests in the VI Analyzer task that passed. Failed Tests contains the total number of tests in the VI Analyzer task that failed. Skipped Tests contains the total number of tests in the VI Analyzer task that the VI Analyzer skipped. VIs not loadable contains the total number of VIs that the VI Analyzer could not load. Tests not loadable contains the total number of tests that the VI Analyzer was not able to load. Test not runnable contains data on the tests that the VI Analyzer was not able to run for the VI specified in VI Path. Test error out contains the total number of errors that occurred during the analysis. Start Time contains the time when the analysis began. Total Times (s) contains the time it took for the VI Analyzer to run the analysis. Test Config Data contains the configuration settings for every test included in the VI Analyzer task. |
|  | Raw Results contains the unparsed results data for every test and every VI in the VI Analyzer task for which you want to create a report. Test Name contains the name of the test that the results reference. Results Data contains the unparsed results for the test specified in Test Name. Status indicates whether the test in Test Name passed or failed. Exceed Max Fails? indicates whether the test in Test Name failed more than the maximum number of times specified for that test. |
|  | Test Name contains the name of the test that the results reference. |
|  | Results Data contains the unparsed results for the test specified in Test Name. |
|  | Status indicates whether the test in Test Name passed or failed. |
|  | Exceed Max Fails? indicates whether the test in Test Name failed more than the maximum number of times specified for that test. |
|  | Parsed Results Data (by VI) contains the results by VI for every test in the VI Analyzer task, including which tests passed and failed, which tests the VI Analyzer could not load or run, and which errors occurred. VI Path contains the path to the VI for which the test results are listed. Pass contains data on the tests that passed for the VI specified in VI Path. Fail contains data on the tests that failed for the VI specified in VI Path. Skipped contains data on the tests the VI Analyzer skipped for the VI specified in VI Path. VI not loadable contains data on whether the VI Analyzer was able to load the VI specified in VI Path. Test not loadable contains data on the tests that the VI Analyzer was not able to load for the VI specified in VI Path. Test not runnable contains data on the tests that the VI Analyzer was not able to run for the VI specified in VI Path. Test error out contains data on errors that occurred when the VI Analyzer performed tests on the VI specified in VI Path. |
|  | VI Path contains the path to the VI for which the test results are listed. |
|  | Pass contains data on the tests that passed for the VI specified in VI Path. |
|  | Fail contains data on the tests that failed for the VI specified in VI Path. |
|  | Skipped contains data on the tests the VI Analyzer skipped for the VI specified in VI Path. |
|  | VI not loadable contains data on whether the VI Analyzer was able to load the VI specified in VI Path. |
|  | Test not loadable contains data on the tests that the VI Analyzer was not able to load for the VI specified in VI Path. |
|  | Test not runnable contains data on the tests that the VI Analyzer was not able to run for the VI specified in VI Path. |
|  | Test error out contains data on errors that occurred when the VI Analyzer performed tests on the VI specified in VI Path. |
|  | Parsed Results Data (by Test) contains the results of every test and whether the VI Analyzer passed, failed, or skipped the test for every VI in the VI Analyzer task. Test Name contains the name of the test that the results reference. Pass contains data on each VI that passed the test specified in Test Name. Fail contains data on each VI that failed the test specified in Test Name. Skipped contains data on each VI for which the VI Analyzer skipped the test specified in Test Name. |
|  | Test Name contains the name of the test that the results reference. |
|  | Pass contains data on each VI that passed the test specified in Test Name. |
|  | Fail contains data on each VI that failed the test specified in Test Name. |
|  | Skipped contains data on each VI for which the VI Analyzer skipped the test specified in Test Name. |
|  | Summary Statistics contains the summary for a VI Analyzer task on how many tests passed, failed, or were skipped; how many VIs and tests the VI Analyzer could not load or run; the total number of test errors; and the start time and elapsed time of the analysis. Passed Tests contains the total number of tests in the VI Analyzer task that passed. Failed Tests contains the total number of tests in the VI Analyzer task that failed. Skipped Tests contains the total number of tests in the VI Analyzer task that the VI Analyzer skipped. VIs not loadable contains the total number of VIs that the VI Analyzer could not load. Tests not loadable contains the total number of tests that the VI Analyzer was not able to load. Test not runnable contains data on the tests that the VI Analyzer was not able to run for the VI specified in VI Path. Test error out contains the total number of errors that occurred during the analysis. Start Time contains the time when the analysis began. Total Times (s) contains the time it took for the VI Analyzer to run the analysis. |
|  | Passed Tests contains the total number of tests in the VI Analyzer task that passed. |
|  | Failed Tests contains the total number of tests in the VI Analyzer task that failed. |
|  | Skipped Tests contains the total number of tests in the VI Analyzer task that the VI Analyzer skipped. |
|  | VIs not loadable contains the total number of VIs that the VI Analyzer could not load. |
|  | Tests not loadable contains the total number of tests that the VI Analyzer was not able to load. |
|  | Test not runnable contains data on the tests that the VI Analyzer was not able to run for the VI specified in VI Path. |
|  | Test error out contains the total number of errors that occurred during the analysis. |
|  | Start Time contains the time when the analysis began. |
|  | Total Times (s) contains the time it took for the VI Analyzer to run the analysis. |
|  | Test Config Data contains the configuration settings for every test included in the VI Analyzer task. |
|  | Report Save Type determines whether the VI saves the results to a tab-delimited ASCII file, an HTML file, or a VI Analyzer results file (.rsl). The default is an ASCII file. If you select RSL File, the VI saves the report data to a VI Analyzer results file that you can load into the VI Analyzer Results Window. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | Export Options specifies the sections of the analysis results to include in the report. The default selects the Summary Data, Failed Tests, and Errors options. If you set Report Save Type to RSL File, the VI ignores this input. Summary Data specifies whether you want to include the Summary Data section of the analysis in the report. The default is TRUE, which includes the section. Failed Tests specifies whether you want to include the Failed Tests section of the analysis in the report. The default is TRUE, which includes the section. Passed Tests specifies whether you want to include the Passed Tests section of the analysis in the report. The default is FALSE, which does not include the section. Skipped Tests specifies whether you want to include the Skipped Tests section of the analysis in the report. The default is FALSE, which does not include the section. Errors specifies whether you want to include the Errors section of the analysis in the report. The default is TRUE, which includes the section. |
|  | Summary Data specifies whether you want to include the Summary Data section of the analysis in the report. The default is TRUE, which includes the section. |
|  | Failed Tests specifies whether you want to include the Failed Tests section of the analysis in the report. The default is TRUE, which includes the section. |
|  | Passed Tests specifies whether you want to include the Passed Tests section of the analysis in the report. The default is FALSE, which does not include the section. |
|  | Skipped Tests specifies whether you want to include the Skipped Tests section of the analysis in the report. The default is FALSE, which does not include the section. |
|  | Errors specifies whether you want to include the Errors section of the analysis in the report. The default is TRUE, which includes the section. |
|  | Sort Type determines whether to sort the report results by VI or by test. The default sorts the results by VI. If you set Report Save Type to RSL File, the VI ignores this input. |
|  | error out contains error information. This output provides standard error out functionality. |

<!--NI_TOPIC bundle=labview-vi-analyzer-toolkit-api-ref path=lvvianalyzer/an_exclude_tests_vi.html language=enus -->
## TOPIC 00005: VIAn Exclude Tests from VI VI

- bundle_id: `labview-vi-analyzer-toolkit-api-ref`
- source_path: `lvvianalyzer/an_exclude_tests_vi.html`
- source_url: https://docs-be.ni.com/bundle/labview-vi-analyzer-toolkit-api-ref/raw/resource/enus/lvvianalyzer/an_exclude_tests_vi.html
- document_id: `labview-vi-analyzer-toolkit-api-ref`
- page_type: `leaf`
- content_type: ``

### VIAn Exclude Tests from VI VI

**Owning Palette:** [VI Analyzer Utilities VIs](../lvvianalyzer/vi_an_utilities_vis.html)

**Requires:** VI Analyzer Toolkit

Specifies the tests to exclude for a specific VI in the VI Analyzer task.

[IMAGE alt='image' src='vian_exclude_tests_from_vi.gif']

|  | VI Analyzer Task in contains a reference to the current task. The VI Analyzer task must be a valid task that you created using the VIAn New Task VI. |
| --- | --- |
|  | VI specifies the path to the VI you want to exclude from certain tests. If the VI is not included in the VI Analyzer task, or if the path you specify is empty or invalid, an error occurs. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | Tests to Exclude contains the names of the tests that you want to exclude from the VI specified in VI. You can wire the Test Names output of the VIAn Get Tests VI to this input. If you specify an invalid test name, an error occurs. |
|  | VI Analyzer Task out returns a reference to the VI Analyzer task specified in VI Analyzer Task in. |
|  | error out contains error information. This output provides standard error out functionality. |

<!--NI_TOPIC bundle=labview-vi-analyzer-toolkit-api-ref path=lvvianalyzer/an_get_items.html language=enus -->
## TOPIC 00006: VIAn Get Items VI

- bundle_id: `labview-vi-analyzer-toolkit-api-ref`
- source_path: `lvvianalyzer/an_get_items.html`
- source_url: https://docs-be.ni.com/bundle/labview-vi-analyzer-toolkit-api-ref/raw/resource/enus/lvvianalyzer/an_get_items.html
- document_id: `labview-vi-analyzer-toolkit-api-ref`
- page_type: `leaf`
- content_type: ``

### VIAn Get Items VI

**Owning Palette:** [VI Analyzer Utilities VIs](../lvvianalyzer/vi_an_utilities_vis.html)

**Requires:** VI Analyzer Toolkit

Returns a list of all top-level VIs, folders, or LLBs in the VI Analyzer task.

[IMAGE alt='image' src='vian_get_items.gif']

|  | VI Analyzer Task in contains a reference to the current task. The VI Analyzer task must be a valid task that you created using the VIAn New Task VI. |
| --- | --- |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | VI Analyzer Task out returns a reference to the VI Analyzer task specified in VI Analyzer Task in. |
|  | Items returns the paths of all top-level VIs, folders, or LLBs that the VI Analyzer task includes. |
|  | error out contains error information. This output provides standard error out functionality. |

<!--NI_TOPIC bundle=labview-vi-analyzer-toolkit-api-ref path=lvvianalyzer/an_get_tests.html language=enus -->
## TOPIC 00007: VIAn Get Tests VI

- bundle_id: `labview-vi-analyzer-toolkit-api-ref`
- source_path: `lvvianalyzer/an_get_tests.html`
- source_url: https://docs-be.ni.com/bundle/labview-vi-analyzer-toolkit-api-ref/raw/resource/enus/lvvianalyzer/an_get_tests.html
- document_id: `labview-vi-analyzer-toolkit-api-ref`
- page_type: `leaf`
- content_type: ``

### VIAn Get Tests VI

**Owning Palette:** [VI Analyzer Utilities VIs](../lvvianalyzer/vi_an_utilities_vis.html)

**Requires:** VI Analyzer Toolkit

Returns a cluster array containing the configuration information for each test in the VI Analyzer task.

[IMAGE alt='image' src='vian_get_tests.gif']

|  | VI Analyzer Task in contains a reference to the current task. The VI Analyzer task must be a valid task that you created using the VIAn New Task VI. |
| --- | --- |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | VI Analyzer Task out returns a reference to the VI Analyzer task specified in VI Analyzer Task in. |
|  | Test Names contains the names of the tests that the VI Analyzer task includes. |
|  | Test Configurations contains an array of clusters in which each cluster represents the configuration options for a specific test. Test Ranking displays the rank of the test as Low, Normal, or High. High-ranking tests involve issues that have a significant impact on performance. Low-ranking tests involve minor style or cosmetic issues that do not significantly affect VI performance. Max Failures displays the maximum number of failed results the VI Analyzer can report for a specific test on a single VI. Control Values displays the names and values of the controls that you use to configure the test. Control Name contains a list of valid control names for controls in the test. Control Value contains values for each control specified in Control Name. Run Test? indicates whether you set the test to run. |
|  | Test Ranking displays the rank of the test as Low, Normal, or High. High-ranking tests involve issues that have a significant impact on performance. Low-ranking tests involve minor style or cosmetic issues that do not significantly affect VI performance. |
|  | Max Failures displays the maximum number of failed results the VI Analyzer can report for a specific test on a single VI. |
|  | Control Values displays the names and values of the controls that you use to configure the test. Control Name contains a list of valid control names for controls in the test. Control Value contains values for each control specified in Control Name. |
|  | Control Name contains a list of valid control names for controls in the test. |
|  | Control Value contains values for each control specified in Control Name. |
|  | Run Test? indicates whether you set the test to run. |
|  | error out contains error information. This output provides standard error out functionality. |

<!--NI_TOPIC bundle=labview-vi-analyzer-toolkit-api-ref path=lvvianalyzer/an_modify_test_config.html language=enus -->
## TOPIC 00008: VIAn Modify Test Config Value VI

- bundle_id: `labview-vi-analyzer-toolkit-api-ref`
- source_path: `lvvianalyzer/an_modify_test_config.html`
- source_url: https://docs-be.ni.com/bundle/labview-vi-analyzer-toolkit-api-ref/raw/resource/enus/lvvianalyzer/an_modify_test_config.html
- document_id: `labview-vi-analyzer-toolkit-api-ref`
- page_type: `leaf`
- content_type: ``

### VIAn Modify Test Config Value VI

**Owning Palette:** [VI Analyzer Utilities VIs](../lvvianalyzer/vi_an_utilities_vis.html)

**Requires:** VI Analyzer Toolkit

Modifies the value of a single configuration option for a specific test.

[IMAGE alt='image' src='vian_modify_test_config_value.gif']

|  | VI Analyzer Task in contains a reference to the current task. The VI Analyzer task must be a valid task that you created using the VIAn New Task VI. |
| --- | --- |
|  | Test Name specifies the name of the test you want to modify. If you specify an invalid test name, the VI returns an error. |
|  | Control Name specifies the name of the control in which you want to change the value. The Control Values output in the Test Configurations indicator of the VIAn Get Tests VI returns a list of valid control names for the test you specify. If you do not specify a valid control name, the VI returns an error. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | Control Value contains the new value that you want for the control you specify in Control Name. If the value is a data type different than the control you specify in Control Name, the VI returns an error. Most controls in VI Analyzer tests are Boolean or numeric data types. Numeric controls in VI Analyzer tests are signed 32-bit integer numeric data types. The following table shows the tests that include control values that are not Boolean or numeric data types. Test Name Data Type Exceptions VI Name The Include Expressions and Exclude Expressions controls are strings. SubVI and TypeDef Locations The User Paths control is a one-dimensional array of paths. Connector Pane Pattern The Patterns control is a one-dimensional array of strings. Terminal Connection Type The Pattern and Type control is a two-dimensional array of strings. Terminal Positions The Pattern and Position control is a two-dimensional array of strings. |
| Test Name | Data Type Exceptions |
| VI Name | The Include Expressions and Exclude Expressions controls are strings. |
| SubVI and TypeDef Locations | The User Paths control is a one-dimensional array of paths. |
| Connector Pane Pattern | The Patterns control is a one-dimensional array of strings. |
| Terminal Connection Type | The Pattern and Type control is a two-dimensional array of strings. |
| Terminal Positions | The Pattern and Position control is a two-dimensional array of strings. |
|  | VI Analyzer Task out returns a reference to the VI Analyzer task specified in VI Analyzer Task in. |
|  | error out contains error information. This output provides standard error out functionality. |

<!--NI_TOPIC bundle=labview-vi-analyzer-toolkit-api-ref path=lvvianalyzer/an_modify_test_settings.html language=enus -->
## TOPIC 00009: VIAn Modify Test Settings VI

- bundle_id: `labview-vi-analyzer-toolkit-api-ref`
- source_path: `lvvianalyzer/an_modify_test_settings.html`
- source_url: https://docs-be.ni.com/bundle/labview-vi-analyzer-toolkit-api-ref/raw/resource/enus/lvvianalyzer/an_modify_test_settings.html
- document_id: `labview-vi-analyzer-toolkit-api-ref`
- page_type: `leaf`
- content_type: ``

### VIAn Modify Test Settings VI

**Owning Palette:** [VI Analyzer Utilities VIs](../lvvianalyzer/vi_an_utilities_vis.html)

**Requires:** VI Analyzer Toolkit

Modifies the configuration settings of a single test.

[IMAGE alt='image' src='vian_modify_test_settings.gif']

|  | VI Analyzer Task in contains a reference to the current task. The VI Analyzer task must be a valid task that you created using the VIAn New Task VI. |
| --- | --- |
|  | Test Name specifies the name of the test you want to modify. If you specify an invalid test name, the VI returns an error. |
|  | New Test Info contains the configuration settings to modify. Test Ranking displays the rank of the test as Low, Normal, or High. The default is Normal. High-ranking tests involve issues that have a significant impact on performance. Low-ranking tests involve minor style or cosmetic issues that do not significantly affect VI performance. Max Failures specifies the maximum number of failed results you want to report for the test on a single VI. The default is 5. Control Values lists the names and values of the controls you can modify for a specific test. Control Name specifies the name of the control in which you want to change the value. The Control Values output in the Test Configurations indicator of the VIAn Get Tests VI returns a list of valid control names for the test you specify. If you do not specify a valid control name, the VI returns an error. Control Value contains the new value that you want for the control you specify in Control Name. If the value is a data type different than the control you specify in Control Name, the VI returns an error. Most controls in VI Analyzer tests are Boolean or numeric data types. Numeric controls in VI Analyzer tests are signed 32-bit integer numeric data types. The following table shows the tests that include control values that are not Boolean or numeric data types. Test Name Data Type Exceptions VI Name The Include Expressions and Exclude Expressions controls are strings. SubVI and TypeDef Locations The User Paths control is a one-dimensional array of paths. Connector Pane Pattern The Patterns control is a one-dimensional array of strings. Terminal Connection Type The Pattern and Type control is a two-dimensional array of strings. Terminal Positions The Pattern and Position control is a two-dimensional array of strings. Run Test? specifies whether you want the test to run. The default is FALSE, which does not run the test. |
|  | Test Ranking displays the rank of the test as Low, Normal, or High. The default is Normal. High-ranking tests involve issues that have a significant impact on performance. Low-ranking tests involve minor style or cosmetic issues that do not significantly affect VI performance. |
|  | Max Failures specifies the maximum number of failed results you want to report for the test on a single VI. The default is 5. |
|  | Control Values lists the names and values of the controls you can modify for a specific test. Control Name specifies the name of the control in which you want to change the value. The Control Values output in the Test Configurations indicator of the VIAn Get Tests VI returns a list of valid control names for the test you specify. If you do not specify a valid control name, the VI returns an error. Control Value contains the new value that you want for the control you specify in Control Name. If the value is a data type different than the control you specify in Control Name, the VI returns an error. Most controls in VI Analyzer tests are Boolean or numeric data types. Numeric controls in VI Analyzer tests are signed 32-bit integer numeric data types. The following table shows the tests that include control values that are not Boolean or numeric data types. Test Name Data Type Exceptions VI Name The Include Expressions and Exclude Expressions controls are strings. SubVI and TypeDef Locations The User Paths control is a one-dimensional array of paths. Connector Pane Pattern The Patterns control is a one-dimensional array of strings. Terminal Connection Type The Pattern and Type control is a two-dimensional array of strings. Terminal Positions The Pattern and Position control is a two-dimensional array of strings. |
|  | Control Name specifies the name of the control in which you want to change the value. The Control Values output in the Test Configurations indicator of the VIAn Get Tests VI returns a list of valid control names for the test you specify. If you do not specify a valid control name, the VI returns an error. |
|  | Control Value contains the new value that you want for the control you specify in Control Name. If the value is a data type different than the control you specify in Control Name, the VI returns an error. Most controls in VI Analyzer tests are Boolean or numeric data types. Numeric controls in VI Analyzer tests are signed 32-bit integer numeric data types. The following table shows the tests that include control values that are not Boolean or numeric data types. Test Name Data Type Exceptions VI Name The Include Expressions and Exclude Expressions controls are strings. SubVI and TypeDef Locations The User Paths control is a one-dimensional array of paths. Connector Pane Pattern The Patterns control is a one-dimensional array of strings. Terminal Connection Type The Pattern and Type control is a two-dimensional array of strings. Terminal Positions The Pattern and Position control is a two-dimensional array of strings. |
| Test Name | Data Type Exceptions |
| VI Name | The Include Expressions and Exclude Expressions controls are strings. |
| SubVI and TypeDef Locations | The User Paths control is a one-dimensional array of paths. |
| Connector Pane Pattern | The Patterns control is a one-dimensional array of strings. |
| Terminal Connection Type | The Pattern and Type control is a two-dimensional array of strings. |
| Terminal Positions | The Pattern and Position control is a two-dimensional array of strings. |
|  | Run Test? specifies whether you want the test to run. The default is FALSE, which does not run the test. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | VI Analyzer Task out returns a reference to the VI Analyzer task specified in VI Analyzer Task in. |
|  | error out contains error information. This output provides standard error out functionality. |

<!--NI_TOPIC bundle=labview-vi-analyzer-toolkit-api-ref path=lvvianalyzer/an_new_task.html language=enus -->
## TOPIC 00010: VIAn New Task VI

- bundle_id: `labview-vi-analyzer-toolkit-api-ref`
- source_path: `lvvianalyzer/an_new_task.html`
- source_url: https://docs-be.ni.com/bundle/labview-vi-analyzer-toolkit-api-ref/raw/resource/enus/lvvianalyzer/an_new_task.html
- document_id: `labview-vi-analyzer-toolkit-api-ref`
- page_type: `leaf`
- content_type: ``

### VIAn New Task VI

**Owning Palette:** [VI Analyzer VIs](../lvvianalyzer/vi_analyzer_vis.html)

**Requires:** VI Analyzer Toolkit

Creates a VI Analyzer task, which you can use with other VI Analyzer VIs to configure and run an analysis.

[IMAGE alt='image' src='vian_new_task.gif']

|  | Path to Configuration File specifies the path to the configuration file containing the VI Analyzer task settings you want to use. If you do not specify a path, the VI creates an empty VI Analyzer task. You can use a configuration file you saved through the VI Analyzer or VI Analyzer VIs. |
| --- | --- |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | Configuration File Password contains the password for the configuration file specified in Path to Configuration File. This input is valid only when specifying a legacy .cfg file that is password-protected. |
|  | Select All Tests? specifies whether to select all VI Analyzer tests to run in the VI Analyzer task. The default is TRUE, which selects all the tests. The VI ignores this input if you specify a configuration file in Path to Configuration File. |
|  | VI Analyzer Task out returns a reference to the new VI Analyzer task. Wire this output to the VI Analyzer Task in input of a VI Analyzer VI. |
|  | error out contains error information. This output provides standard error out functionality. |

<!--NI_TOPIC bundle=labview-vi-analyzer-toolkit-api-ref path=lvvianalyzer/an_remove_item.html language=enus -->
## TOPIC 00011: VIAn Remove Item VI

- bundle_id: `labview-vi-analyzer-toolkit-api-ref`
- source_path: `lvvianalyzer/an_remove_item.html`
- source_url: https://docs-be.ni.com/bundle/labview-vi-analyzer-toolkit-api-ref/raw/resource/enus/lvvianalyzer/an_remove_item.html
- document_id: `labview-vi-analyzer-toolkit-api-ref`
- page_type: `leaf`
- content_type: ``

### VIAn Remove Item VI

**Owning Palette:** [VI Analyzer Utilities VIs](../lvvianalyzer/vi_an_utilities_vis.html)

**Requires:** VI Analyzer Toolkit

Removes an item, such as a VI, LLB, or folder, or excludes a subitem, such as a VI within an LLB or folder, from the VI Analyzer task.

[IMAGE alt='image' src='vian_remove_item.gif']

|  | VI Analyzer Task in contains a reference to the current task. The VI Analyzer task must be a valid task that you created using the VIAn New Task VI. |
| --- | --- |
|  | Item to Remove specifies the VI, folder, or LLB that you want to remove from the VI Analyzer task. If you specify a top-level item, the VI removes the item and all its subitems. If you specify a subitem, the VI excludes the subitem but includes other subitems within the top-level item. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | VI Analyzer Task out returns a reference to the VI Analyzer task specified in VI Analyzer Task in. |
|  | error out contains error information. This output provides standard error out functionality. |

<!--NI_TOPIC bundle=labview-vi-analyzer-toolkit-api-ref path=lvvianalyzer/an_run.html language=enus -->
## TOPIC 00012: VIAn Run VI

- bundle_id: `labview-vi-analyzer-toolkit-api-ref`
- source_path: `lvvianalyzer/an_run.html`
- source_url: https://docs-be.ni.com/bundle/labview-vi-analyzer-toolkit-api-ref/raw/resource/enus/lvvianalyzer/an_run.html
- document_id: `labview-vi-analyzer-toolkit-api-ref`
- page_type: `leaf`
- content_type: ``

### VIAn Run VI

**Owning Palette:** [VI Analyzer VIs](../lvvianalyzer/vi_analyzer_vis.html)

**Requires:** VI Analyzer Toolkit

Analyzes VIs using the settings that **VI Analyzer Task in** specifies. You can wire the results to the [VIAn Easy Report VI](../lvvianalyzer/an_easy_report.html).

[IMAGE alt='image' src='vian_run.gif']

|  | VI Analyzer Task in contains a reference to the current task. The VI Analyzer task must be a valid task that you created using the VIAn New Task VI. |
| --- | --- |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | Show Results Window? (F) specifies whether to show the VI Analyzer Results Window after the VI completes execution. |
|  | VIs Tested returns an array of paths to every VI analyzed. |
|  | Tests Run returns an array of strings containing the names of all the tests run in the analysis. |
|  | VI Analyzer Task out returns a reference to the VI Analyzer task specified in VI Analyzer Task in. |
|  | Analysis Results returns the results of the VI Analyzer task. Wire this output to the Analysis Results input of the VIAn Easy Report VI. Raw Results contains the unparsed results data for every test and every VI in the VI Analyzer task. Test Name displays the name of the test. Results Data contains the unparsed results for the test specified in Test Name. Status indicates whether the test in Test Name passed or failed. Exceed Max Fails? indicates whether the test in Test Name failed more than the maximum number of times specified for that test. Parsed Results Data (by VI) contains the results by VI for every test in the VI Analyzer task, including which tests passed and failed, which tests the VI Analyzer could not load or run, and which errors occurred. VI Path contains the path to the VI for which the test results are listed. Pass contains data on the tests that passed for the VI specified in VI Path. Fail contains data on the tests that failed for the VI specified in VI Path. Skipped contains data on the tests that the VI Analyzer skipped for the VI specified in VI Path. VI not loadable contains data on whether the VI Analyzer was able to load the VI specified in VI Path. Test not loadable contains data on the tests that the VI Analyzer was not able to load for the VI specified in VI Path. Test not runnable contains data on the tests that the VI Analyzer was not able to run for the VI specified in VI Path. Test error out contains data on errors that occurred when the VI Analyzer performed tests on the VI specified in VI Path. Parsed Results Data (by Test) contains the results of every test and whether the VI Analyzer passed, failed, or skipped the test for every VI in the VI Analyzer task. Test Name displays the name of the test. Pass contains data on each VI that passed the test specified in Test Name. Fail contains data on each VI that failed the test specified in Test Name. Skipped contains data on each VI for which the VI Analyzer skipped the test specified in Test Name. Summary Statistics contains the summary for a VI Analyzer task. Passed Tests indicates the total number of tests in the VI Analyzer task that passed. Failed Tests indicates the total number of tests in the VI Analyzer task that failed. Skipped Tests indicates the total number of tests in the VI Analyzer task that the VI Analyzer skipped. VIs not loadable indicates the total number of VIs that the VI Analyzer could not load. Tests not loadable indicates the total number of tests that the VI Analyzer was not able to load. Tests not runnable indicates the total number of tests that the VI Analyzer was not able to run. Test error out indicates the total number of errors that occurred during the analysis. Start Time indicates the time when the analysis began. Total Time (s) indicates the time it took for the VI Analyzer to run the analysis. Test Config Data contains the configuration settings for every test included in the VI Analyzer task. |
|  | Raw Results contains the unparsed results data for every test and every VI in the VI Analyzer task. Test Name displays the name of the test. Results Data contains the unparsed results for the test specified in Test Name. Status indicates whether the test in Test Name passed or failed. Exceed Max Fails? indicates whether the test in Test Name failed more than the maximum number of times specified for that test. |
|  | Test Name displays the name of the test. |
|  | Results Data contains the unparsed results for the test specified in Test Name. |
|  | Status indicates whether the test in Test Name passed or failed. |
|  | Exceed Max Fails? indicates whether the test in Test Name failed more than the maximum number of times specified for that test. |
|  | Parsed Results Data (by VI) contains the results by VI for every test in the VI Analyzer task, including which tests passed and failed, which tests the VI Analyzer could not load or run, and which errors occurred. VI Path contains the path to the VI for which the test results are listed. Pass contains data on the tests that passed for the VI specified in VI Path. Fail contains data on the tests that failed for the VI specified in VI Path. Skipped contains data on the tests that the VI Analyzer skipped for the VI specified in VI Path. VI not loadable contains data on whether the VI Analyzer was able to load the VI specified in VI Path. Test not loadable contains data on the tests that the VI Analyzer was not able to load for the VI specified in VI Path. Test not runnable contains data on the tests that the VI Analyzer was not able to run for the VI specified in VI Path. Test error out contains data on errors that occurred when the VI Analyzer performed tests on the VI specified in VI Path. |
|  | VI Path contains the path to the VI for which the test results are listed. |
|  | Pass contains data on the tests that passed for the VI specified in VI Path. |
|  | Fail contains data on the tests that failed for the VI specified in VI Path. |
|  | Skipped contains data on the tests that the VI Analyzer skipped for the VI specified in VI Path. |
|  | VI not loadable contains data on whether the VI Analyzer was able to load the VI specified in VI Path. |
|  | Test not loadable contains data on the tests that the VI Analyzer was not able to load for the VI specified in VI Path. |
|  | Test not runnable contains data on the tests that the VI Analyzer was not able to run for the VI specified in VI Path. |
|  | Test error out contains data on errors that occurred when the VI Analyzer performed tests on the VI specified in VI Path. |
|  | Parsed Results Data (by Test) contains the results of every test and whether the VI Analyzer passed, failed, or skipped the test for every VI in the VI Analyzer task. Test Name displays the name of the test. Pass contains data on each VI that passed the test specified in Test Name. Fail contains data on each VI that failed the test specified in Test Name. Skipped contains data on each VI for which the VI Analyzer skipped the test specified in Test Name. |
|  | Test Name displays the name of the test. |
|  | Pass contains data on each VI that passed the test specified in Test Name. |
|  | Fail contains data on each VI that failed the test specified in Test Name. |
|  | Skipped contains data on each VI for which the VI Analyzer skipped the test specified in Test Name. |
|  | Summary Statistics contains the summary for a VI Analyzer task. Passed Tests indicates the total number of tests in the VI Analyzer task that passed. Failed Tests indicates the total number of tests in the VI Analyzer task that failed. Skipped Tests indicates the total number of tests in the VI Analyzer task that the VI Analyzer skipped. VIs not loadable indicates the total number of VIs that the VI Analyzer could not load. Tests not loadable indicates the total number of tests that the VI Analyzer was not able to load. Tests not runnable indicates the total number of tests that the VI Analyzer was not able to run. Test error out indicates the total number of errors that occurred during the analysis. Start Time indicates the time when the analysis began. Total Time (s) indicates the time it took for the VI Analyzer to run the analysis. |
|  | Passed Tests indicates the total number of tests in the VI Analyzer task that passed. |
|  | Failed Tests indicates the total number of tests in the VI Analyzer task that failed. |
|  | Skipped Tests indicates the total number of tests in the VI Analyzer task that the VI Analyzer skipped. |
|  | VIs not loadable indicates the total number of VIs that the VI Analyzer could not load. |
|  | Tests not loadable indicates the total number of tests that the VI Analyzer was not able to load. |
|  | Tests not runnable indicates the total number of tests that the VI Analyzer was not able to run. |
|  | Test error out indicates the total number of errors that occurred during the analysis. |
|  | Start Time indicates the time when the analysis began. |
|  | Total Time (s) indicates the time it took for the VI Analyzer to run the analysis. |
|  | Test Config Data contains the configuration settings for every test included in the VI Analyzer task. |
|  | error out contains error information. This output provides standard error out functionality. |

<!--NI_TOPIC bundle=labview-vi-analyzer-toolkit-api-ref path=lvvianalyzer/an_save_cfg.html language=enus -->
## TOPIC 00013: VIAn Save Configuration File VI

- bundle_id: `labview-vi-analyzer-toolkit-api-ref`
- source_path: `lvvianalyzer/an_save_cfg.html`
- source_url: https://docs-be.ni.com/bundle/labview-vi-analyzer-toolkit-api-ref/raw/resource/enus/lvvianalyzer/an_save_cfg.html
- document_id: `labview-vi-analyzer-toolkit-api-ref`
- page_type: `leaf`
- content_type: ``

### VIAn Save Configuration File VI

**Owning Palette:** [VI Analyzer VIs](../lvvianalyzer/vi_analyzer_vis.html)

**Requires:** VI Analyzer Toolkit

Saves the current VI Analyzer task settings to a configuration file.

[IMAGE alt='image' src='vian_save_configuration_file.gif']

|  | Overwrite? specifies whether to overwrite the configuration file if the file specified in Path to Configuration File already exists. The default is TRUE, which overwrites the existing file. If Overwrite? is FALSE and the file exists, the VI returns an error. |
| --- | --- |
|  | VI Analyzer Task in contains a reference to the current task. The VI Analyzer task must be a valid task that you created using the VIAn New Task VI. |
|  | Path to Configuration File contains the path to the configuration file you want to save. If you specify an invalid path, the VI returns an error. If you specify no path, the VI saves the configuration file using the path specified in the VIAn New Task VI. If you specified no paths for either VI, the VI returns an error. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | VI Analyzer Task out returns a reference to the VI Analyzer task specified in VI Analyzer Task in. |
|  | error out contains error information. This output provides standard error out functionality. |

<!--NI_TOPIC bundle=labview-vi-analyzer-toolkit-api-ref path=lvvianalyzer/an_select_tests.html language=enus -->
## TOPIC 00014: VIAn Select Tests VI

- bundle_id: `labview-vi-analyzer-toolkit-api-ref`
- source_path: `lvvianalyzer/an_select_tests.html`
- source_url: https://docs-be.ni.com/bundle/labview-vi-analyzer-toolkit-api-ref/raw/resource/enus/lvvianalyzer/an_select_tests.html
- document_id: `labview-vi-analyzer-toolkit-api-ref`
- page_type: `leaf`
- content_type: ``

### VIAn Select Tests VI

**Owning Palette:** [VI Analyzer Utilities VIs](../lvvianalyzer/vi_an_utilities_vis.html)

**Requires:** VI Analyzer Toolkit

Selects or deselects the specified tests in the VI Analyzer task.

[IMAGE alt='image' src='vian_select_tests.gif']

|  | VI Analyzer Task in contains a reference to the current task. The VI Analyzer task must be a valid task that you created using the VIAn New Task VI. |
| --- | --- |
|  | Test Names specifies the names of the VI Analyzer tests you want to select or deselect. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | Select Test? specifies whether to select or deselect the specified tests in the VI Analyzer task. The default is TRUE, which selects the tests. If you set Select Test? to FALSE, the VI deselects the specified tests. |
|  | VI Analyzer Task out returns a reference to the VI Analyzer task specified in VI Analyzer Task in. |
|  | error out contains error information. This output provides standard error out functionality. |

<!--NI_TOPIC bundle=labview-vi-analyzer-toolkit-api-ref path=lvvianalyzer/vi_an_utilities_vis.html language=enus -->
## TOPIC 00015: VI Analyzer Utilities VIs

- bundle_id: `labview-vi-analyzer-toolkit-api-ref`
- source_path: `lvvianalyzer/vi_an_utilities_vis.html`
- source_url: https://docs-be.ni.com/bundle/labview-vi-analyzer-toolkit-api-ref/raw/resource/enus/lvvianalyzer/vi_an_utilities_vis.html
- document_id: `labview-vi-analyzer-toolkit-api-ref`
- page_type: `leaf`
- content_type: ``

### VI Analyzer Utilities VIs

**Owning Palette:** [VI Analyzer VIs](../lvvianalyzer/vi_analyzer_vis.html)

**Requires:** VI Analyzer Toolkit. This topic might not match its corresponding palette in LabVIEW depending on your operating system, licensed product(s), and target.

Use the VI Analyzer Utilities VIs to modify the configuration settings for a VI Analyzer task.

The VIs on this palette can return [VI Analyzer error codes](../lvvianalyzer/vi_analyzer_error_codes.html).

| Palette Object | Description |
| --- | --- |
| VIAn Add Item | Adds an item, such as a VI, LLB, or folder, to the VI Analyzer task. |
| VIAn Exclude Tests from VI | Specifies the tests to exclude for a specific VI in the VI Analyzer task. |
| VIAn Get Analysis Status | Monitors the progress of the analysis. |
| VIAn Get Items | Returns a list of all top-level VIs, folders, or LLBs in the VI Analyzer task. |
| VIAn Get Tests | Returns a cluster array containing the configuration information for each test in the VI Analyzer task. |
| VIAn Modify Test Config Value | Modifies the value of a single configuration option for a specific test. |
| VIAn Modify Test Settings | Modifies the configuration settings of a single test. |
| VIAn Remove Item | Removes an item, such as a VI, LLB, or folder, or excludes a subitem, such as a VI within an LLB or folder, from the VI Analyzer task. |
| VIAn Select Tests | Selects or deselects the specified tests in the VI Analyzer task. |

<!--NI_TOPIC bundle=labview-vi-analyzer-toolkit-api-ref path=lvvianalyzer/vi_analyzer_error_codes.html language=enus -->
## TOPIC 00016: VI Analyzer Error Codes (VI Analyzer Toolkit)

- bundle_id: `labview-vi-analyzer-toolkit-api-ref`
- source_path: `lvvianalyzer/vi_analyzer_error_codes.html`
- source_url: https://docs-be.ni.com/bundle/labview-vi-analyzer-toolkit-api-ref/raw/resource/enus/lvvianalyzer/vi_analyzer_error_codes.html
- document_id: `labview-vi-analyzer-toolkit-api-ref`
- page_type: `leaf`
- content_type: ``

### VI Analyzer Error Codes (VI Analyzer Toolkit)

The [VI Analyzer](../lvvianalyzer/vi_analyzer_vis.html) VIs can return the following error codes.

| Code | Name | Description |
| --- | --- | --- |
| 14200 | VIAn_CannotExclude | The path you specified either is not a valid path or does not exist in the VI Analyzer item list. |
| 14201 | VIAn_CannotModify | You attempted to modify an item path that does not exist in the VI Analyzer item list. |
| 14202 | VIAn_CannotRemove | You attempted to remove an item that does not exist in the VI Analyzer item list. |
| 14203 | VIAn_CorruptConfig | There was an error reading the specified configuration file. The configuration file might be corrupt. You might need to re-create your configuration file. |
| 14204 | VIAn_ErrSavingConfig | An error occurred while saving the configuration file. Make sure you specified a valid path, that you have permission to write to the specified location, and that you set Overwrite? to TRUE if you are specifying an existing file. |
| 14205 | VIAn_ErrSavingResults | An error occurred while saving your results. Make sure you specified a valid path, that you have permission to write to the specified location, and that you set Overwrite? to TRUE if you are specifying an existing file. |
| 14206 | VIAn_InvalidCFG | The path you specified is an invalid configuration file path. |
| 14207 | VIAn_InvalidItem | The item path you specified is invalid. You must enter a path to an existing VI, LLB, or folder. |
| 14208 | VIAn_InvalidRef | The VI Analyzer task reference you wired is invalid. |
| 14209 | VIAn_InvalidTest | The test you specified is an invalid VI Analyzer test name. |
| 14210 | VIAn_MaxPwds | You cannot store more than 20 passwords through the VI Analyzer programmatic interface. |
| 14211 | VIAn_NoCFG | You did not specify a configuration file path. |
| 14212 | VIAn_PasswordWrong | You did not specify the correct configuration file password. |
| 14213 | VIAn_InvalidConfigControlValue | You provided an invalid configuration VI control value. Ensure that both the control name and the data type are compatible with the test configuration you are editing. |
| 14214 | VIAn_NoResults | Unable to display the VI Analyzer Results Window. Make sure the VI Analyzer Results Window and the VI Analyzer are not already in use. |
| 14215 | VIAn_UnsupportedVI | The specified VI is no longer a supported feature in the VI Analyzer Toolkit. You cannot use the VI to perform VI Analyzer operations. |

<!--NI_TOPIC bundle=labview-vi-analyzer-toolkit-api-ref path=lvvianalyzer/vi_analyzer_vis.html language=enus -->
## TOPIC 00017: VI Analyzer VIs

- bundle_id: `labview-vi-analyzer-toolkit-api-ref`
- source_path: `lvvianalyzer/vi_analyzer_vis.html`
- source_url: https://docs-be.ni.com/bundle/labview-vi-analyzer-toolkit-api-ref/raw/resource/enus/lvvianalyzer/vi_analyzer_vis.html
- document_id: `labview-vi-analyzer-toolkit-api-ref`
- page_type: `leaf`
- content_type: ``

### VI Analyzer VIs

March 2018, 370928G-01

**Requires:** VI Analyzer Toolkit. This topic might not match its corresponding palette in LabVIEW depending on your operating system, licensed product(s), and target.

Use the VI Analyzer VIs with the LabVIEW VI Analyzer Toolkit to programmatically run [tests that check VIs for style, efficiency, and other aspects of LabVIEW programming](/csh?topicname=lvvianalyzerhelp/test_descriptions.html).

|  | Note Select Tools»VI Analyzer»Analyze VIs to use the VI Analyzer to interactively run tests on an open VI or to create a VI Analyzer task to analyze a set of VIs. |
| --- | --- |

You can add VIs written with the VI Analyzer VIs to the labview\project\_VI Analyzer\Quick Launch folder. These VIs appear as menu options in **Tools»VI Analyzer»Quick Launch**. If you want to create a quick launch test, you must start with the following template:

labview\vi.lib\addons\analyzer\analyzerapi.llb\VIAn Quick Launch VI Template.vit

The VIs you run from the **Quick Launch** menu run in a [private application instance](/csh?topicname=lvconcepts/application_instances.html) that is separate from the main application instance.

The VIs on this palette can return [VI Analyzer error codes](../lvvianalyzer/vi_analyzer_error_codes.html).

| Palette Object | Description |
| --- | --- |
| VIAn Destroy Task | Closes an existing VI Analyzer task reference and releases resources associated with the task. |
| VIAn Easy Analyze | Runs a VI Analyzer task automatically using settings in the specified configuration file. |
| VIAn Easy Report | Exports the results of an analysis to a file, either as a report in ASCII or HTML format or as a VI Analyzer results file. |
| VIAn New Task | Creates a VI Analyzer task, which you can use with other VI Analyzer VIs to configure and run an analysis. |
| VIAn Run | Analyzes VIs using the settings that VI Analyzer Task in specifies. You can wire the results to the VIAn Easy Report VI. |
| VIAn Save Configuration File | Saves the current VI Analyzer task settings to a configuration file. |

| Subpalette | Description |
| --- | --- |
| VI Analyzer Utilities VIs | Use the VI Analyzer Utilities VIs to modify the configuration settings for a VI Analyzer task. |

© 2003–2018 National Instruments. All rights reserved.

<!--NI_TOPIC bundle=labview-vi-analyzer-toolkit-api-ref path=lvvianalyzer/vian_copyright.html language=enus -->
## TOPIC 00018: LabVIEW VI Analyzer Toolkit Copyright

- bundle_id: `labview-vi-analyzer-toolkit-api-ref`
- source_path: `lvvianalyzer/vian_copyright.html`
- source_url: https://docs-be.ni.com/bundle/labview-vi-analyzer-toolkit-api-ref/raw/resource/enus/lvvianalyzer/vian_copyright.html
- document_id: `labview-vi-analyzer-toolkit-api-ref`
- page_type: `leaf`
- content_type: ``

### LabVIEW VI Analyzer Toolkit Copyright

Under the copyright laws, this publication may not be reproduced or transmitted in any form, electronic or mechanical, including photocopying, recording, storing in an information retrieval system, or translating, in whole or in part, without the prior written consent of National Instruments Corporation.

In regards to the automatically generated inflection database, the following copyrights apply. For a listing of conditions and disclaimers, refer to the agid-readme.txt.

Copyright 2000-2003 by Kevin Atkinson

Permission to use, copy, modify, distribute and sell this database, the associated scripts, the output created form the scripts and its documentation for any purpose is hereby granted without fee, provided that the above copyright notice appears in all copies and that both that copyright notice and this permission notice appear in supporting documentation. Kevin Atkinson makes no representations about the suitability of this array for any purpose. It is provided "as is" without express or implied warranty.

The part-of-speech database is taken from Alan Beale 2of12id 
and the WordNet database which is under the following copyright:

This software and database is being provided to you, the LICENSEE, by Princeton University under the following license. By obtaining, using and/or copying this software and database, you agree that you have read, understood, and will comply with these terms and conditions.

Permission to use, copy, modify and distribute this software and database and its documentation for any purpose and without fee or royalty is hereby granted, provided that you agree to comply with the following copyright notice and statements, including the disclaimer, and that the same appear on ALL copies of the software, database and documentation, including modifications that you make for internal use or for distribution.

WordNet 1.6 Copyright 1997 by Princeton University. All rights reserved.

THIS SOFTWARE AND DATABASE IS PROVIDED "AS IS" AND PRINCETON UNIVERSITY MAKES NO REPRESENTATIONS OR WARRANTIES, EXPRESS OR IMPLIED. BY WAY OF EXAMPLE, BUT NOT LIMITATION, PRINCETON UNIVERSITY MAKES NO REPRESENTATIONS OR WARRANTIES OF MERCHANT-ABILITY OR FITNESS FOR ANY PARTICULAR PURPOSE OR THAT THE USE OF THE LICENSED SOFTWARE, DATABASE OR DOCUMENTATION WILL NOT INFRINGE ANY THIRD PARTY PATENTS, COPYRIGHTS, TRADEMARKS OR OTHER RIGHTS.

The name of Princeton University or Princeton may not be used in advertising or publicity pertaining to distribution of the software and/or database. Title to copyright in this software, database and any associated documentation shall at all times remain with Princeton University and LICENSEE agrees to preserve same.

Alan Beale 2of12id.txt is indirectly derived from the Moby part-of-speech database and the WordNet database. The Moby part-of-speech is in the public domain:

The Moby lexicon project is complete and has been placed into the public domain. Use, sell, rework, excerpt and use in any way on any platform.

Placing this material on internal or public servers is also encouraged. The compiler is not aware of any export restrictions so freely distribute world-wide.

You can verify the public domain status by contacting

Grady Ward 

3449 Martha CT. 

Arcata, CA 95521-4884 
 

grady@netcom.com 

grady@northcoast.com

The word list used is a combination of several word lists:

1. The ENABLE2K word lists which is in the public domain: 
 The ENABLE master word list, WORD.LST, is herewith formally
 released into the Public Domain. Anyone is free to use it or
 distribute it in any manner they see fit. No fee or registration
 is required for its use nor are "contributions" solicited (if you
 feel you absolutely must contribute something for your own peace
 of mind, the authors of the ENABLE list ask that you make a
 donation on their behalf to your favorite charity). This word
 list is our gift to the Scrabble community, as an alternate to
 "official" word lists. Game designers may feel free to
 incorporate the WORD.LST into their games. Please mention the
 source and credit us as originators of the list. Note that if
 you, as a game designer, use the WORD.LST in your product, you
 may still copyright and protect your product, but you may *not*
 legally copyright or in any way restrict redistribution of the
 WORD.LST portion of your product. This *may* under law restrict
 your rights to restrict your users' rights, but that is only
 fair.
2. All of the word lists except ABLE.LST in the ENABLE2K Supplemnt which consists of: 
 2DICTS.LST ALSO.LST LETTERS.LST OSPDADD.LST UCACR.LST
 LCACR.LST NOPOS.LST PLURALS.LST UPPER.LST 
 All of these word lists are also in the public domain.
3. The list of signature words from the YAWL package which is in the
 public domain.
4. The UK Advanced Cryptics Dictionary which in under the following copyright: Copyright © J Ross Beresford 1993-1999. All Rights Reserved. 

 The following restriction is placed on the use of this
 publication: if The UK Advanced Cryptics Dictionary is used
 in a software package or redistributed in any form, the
 copyright notice must be prominently displayed and the text
 of this document must be included verbatim. 

 There are no other restrictions: I would like to see the
 list distributed as widely as possible.
5. Some extra words found in the Part-Of-Speech database that was not found in any of the above word lists.
6. Words found in the Jargon File Word List package, available at
 http://aspell.sourceforge.net/wl/, which is in the Public Domain.
7. Words in 2of12id.txt not in any of the word lists above. 2of12id is
 indirectly derived from all the above sources and most of the word
 lists from the Moby Words package: 
 10196pla.ces 113809of.fic 21986na.mes 256772co.mpo 354984si.ngl
 3897male.nam 4160offi.cia 4946fema.len 6213acro.nym 74550com.mon
 
 The Moby Word package, like the Part-Of-Speech database is in the
 public domain.
8. And finally some extra words that I added myself. These words can be
 found in the file "extra-words"

The "dontuse", "irregular", and "variant" file was created by me (Kevin Atkinson) from numerous sources.

The word list used in the automatically generated inflection database is a combination of several word lists, and includes the following copyright:

The UK Advanced Cryptics Dictionary which in under the following
copyright:

Copyright © J Ross Beresford 1993-1999. All Rights Reserved.

The following restriction is placed on the use of this publication: if The UK Advanced Cryptics Dictionary is used in a software package or redistributed in any form, the copyright notice must be prominently displayed and the text of this document must be included verbatim.

<!--NI_TOPIC bundle=labview-vi-analyzer-toolkit-api-ref path=lvvianalyzer/vian_get_analysis_status.html language=enus -->
## TOPIC 00019: VIAn Get Analysis Status VI

- bundle_id: `labview-vi-analyzer-toolkit-api-ref`
- source_path: `lvvianalyzer/vian_get_analysis_status.html`
- source_url: https://docs-be.ni.com/bundle/labview-vi-analyzer-toolkit-api-ref/raw/resource/enus/lvvianalyzer/vian_get_analysis_status.html
- document_id: `labview-vi-analyzer-toolkit-api-ref`
- page_type: `leaf`
- content_type: ``

### VIAn Get Analysis Status VI

**Owning Palette:** [VI Analyzer Utilities VIs](../lvvianalyzer/vi_an_utilities_vis.html)

**Requires:** VI Analyzer Toolkit

Monitors the progress of the analysis.

[IMAGE alt='image' src='vian_get_analysis_status.gif']

|  | VI Analyzer Task in contains a reference to the current task. The VI Analyzer task must be a valid task that you created using the VIAn New Task VI. |
| --- | --- |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | Abort Analysis specifies whether to abort the analysis process. The default is FALSE. If you call this VI in a loop structure, you can wire a value of TRUE to this input to abort an analysis that is currently running. |
|  | VI Analyzer Task out returns a reference to the VI Analyzer task specified in VI Analyzer Task in. |
|  | Percent Complete represents the percentage of the task that has completed. Values range from 0 to 100. |
|  | VI in Analysis displays the name of the VI being analyzed. |
|  | error out contains error information. This output provides standard error out functionality. |
