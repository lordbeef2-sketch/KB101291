# NI DOCUMENT BUNDLE: labview-unit-test-framework-toolkit-api-ref

<!--NI_BUNDLE_CHUNK bundle=labview-unit-test-framework-toolkit-api-ref start=1 end=65 -->
<!--NI_TOPIC bundle=labview-unit-test-framework-toolkit-api-ref path=lvutf/utf_error_codes.html language=enus -->
## TOPIC 00001: Error Codes (Unit Test Framework Toolkit)

- bundle_id: `labview-unit-test-framework-toolkit-api-ref`
- source_path: `lvutf/utf_error_codes.html`
- source_url: https://docs-be.ni.com/bundle/labview-unit-test-framework-toolkit-api-ref/raw/resource/enus/lvutf/utf_error_codes.html
- document_id: `labview-unit-test-framework-toolkit-api-ref`
- page_type: `leaf`
- content_type: ``

### Error Codes (Unit Test Framework Toolkit)

The [Unit Test Framework](../lvutf/utf_vis.html) VIs can return the following error codes. Refer to the KnowledgeBase for more information about correcting errors in LabVIEW.

| Code | Description |
| --- | --- |
| −25288 | Cannot access a shared variable. |
| −25287 | An error occurred when creating test(s). |
| −25286 | This VI does not have a block diagram. |
| −25285 | Cannot execute tests while related VIs are running, including the VI under test, setup VI, teardown VI, user-defined comparison VI, and user-defined test VI. |
| −25284 | This VI is in a locked library. Unlock the library or add the password in the Project Properties dialog box. |
| −25283 | This VI is password-protected. Unlock the VI or add the password in the Project Properties dialog box. |
| −25282 | The path to the user-defined test VI is invalid. |
| −25262 | The user-defined comparison VI is invalid. |
| −25261 | The path to the user-defined comparison VI is invalid. |
| −25260 | The .lvtest file is read-only. |
| −25259 | The .lvtest file is invalid. |
| −25258 | Test Case Data Error |
| −25257 | Test Case Data Missing |
| −25256 | An error occurred while setting input values to the VI under test. |
| −25253 | If the VI under test is a reentrant VI, a dynamic dispatch member VI, a subroutine VI, or executes on a real-time (RT) target, LabVIEW can compare only the indicators on the connector pane or global variables. |
| −25252 | If the VI under test is a reentrant VI, a dynamic dispatch member VI, a subroutine VI, or executes on a real-time (RT) target, LabVIEW can set values only to controls on the connector pane or to global variables. |
| −25251 | LabVIEW cannot find the following control(s). |
| −25250 | The .lvtest file header information contains an error. |
| −25249 | The following control name is not unique. |
| −25248 | The control name cannot contain the following: \\n, \\r, tabs, array brackets, name separators, and decimal separators. |
| −25245 | An error occurred when running the setup and teardown VIs. |
| −25244 | The configuration between setup VI, teardown VI, and VI under test is invalid. |
| −25242 | The user-defined test VI is invalid. |
| −25241 | The VI under test is invalid. |
| −25240 | The path to the VI under test is invalid. |
| −25232 | An error occurred with the teardown VI. |
| −25231 | The teardown VI is invalid. |
| −25230 | The path to the teardown VI is invalid. |
| −25222 | LabVIEW cannot find the following terminal(s). |
| −25221 | The setup VI is invalid. |
| −25220 | The path to the setup VI is invalid. |
| −25204 | Cannot load the class. Save the class before loading or executing tests. |
| −25201 | Cannot open multiple instances of the Unit Test Framework Results window. Close the window before executing tests. |
| −25200 | An unknown error occurred. |

<!--NI_TOPIC bundle=labview-unit-test-framework-toolkit-api-ref path=lvutf/utf_report.html language=enus -->
## TOPIC 00002: Create Report VI

- bundle_id: `labview-unit-test-framework-toolkit-api-ref`
- source_path: `lvutf/utf_report.html`
- source_url: https://docs-be.ni.com/bundle/labview-unit-test-framework-toolkit-api-ref/raw/resource/enus/lvutf/utf_report.html
- document_id: `labview-unit-test-framework-toolkit-api-ref`
- page_type: `leaf`
- content_type: ``

### Create Report VI

**Owning Palette:** [Unit Test Framework VIs](../lvutf/utf_vis.html)

**Requires:** Unit Test Framework Toolkit

Generates a [report](../lvutfconcepts/utfc_results.html) after test execution. You can generate this report in HTML, Automatic Test Markup Language (ATML), or ASCII format.

[Examples](#examples)

[IMAGE alt='image' src='create_report.gif']

|  | CSS file path specifies the path to the Cascading Style Sheet (CSS) file this VI uses to customize HTML reports. |
| --- | --- |
|  | view report? specifies whether to display the report after test execution. If you do not display the report after test execution, you can view the report by navigating to the report path you specified. The default is TRUE. |
|  | test results in contains the results of the test execution from using either the Run Tests from File VI or Run Tests from Project VI. |
|  | report path specifies the path to which LabVIEW saves the generated report file. The default is My Documents\\LabVIEW Data. |
|  | report type specifies the type of report this VI generates. 1ASCII (tab-delimited)2HTML (default)3ATML (XML-based) |
| 1 | ASCII (tab-delimited) |
| 2 | HTML (default) |
| 3 | ATML (XML-based) |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | display by specifies whether to display the test results according to the names of the tests or the names of the VIs. 1VI name2Test name (default) |
| 1 | VI name |
| 2 | Test name (default) |
|  | report settings specifies the contents of the test report. summary? specifies whether to include the Test Summary section in the test report. The default is TRUE. passed? specifies whether to include the Passed section in the Test Results section of the test report. The default is TRUE. passed details? specifies whether to include the details of the Passed section in the Test Details section of the test report. The default is FALSE. failed? specifies whether to include the Failed section in the Test Results section of the test report. The default is TRUE. failed details? specifies whether to include the details of the Failed section in the Test Details section of the test report. The default is FALSE. skipped? specifies whether to include the Skipped section in the Test Results section of the test report. The default is TRUE. error? specifies whether to include the Error section in the Test Results section of the test report. The default is TRUE. error details? specifies whether to include the details of the Error section in the Test Details section of the test report. The default is FALSE. |
|  | summary? specifies whether to include the Test Summary section in the test report. The default is TRUE. |
|  | passed? specifies whether to include the Passed section in the Test Results section of the test report. The default is TRUE. |
|  | passed details? specifies whether to include the details of the Passed section in the Test Details section of the test report. The default is FALSE. |
|  | failed? specifies whether to include the Failed section in the Test Results section of the test report. The default is TRUE. |
|  | failed details? specifies whether to include the details of the Failed section in the Test Details section of the test report. The default is FALSE. |
|  | skipped? specifies whether to include the Skipped section in the Test Results section of the test report. The default is TRUE. |
|  | error? specifies whether to include the Error section in the Test Results section of the test report. The default is TRUE. |
|  | error details? specifies whether to include the details of the Error section in the Test Details section of the test report. The default is FALSE. |
|  | test results out returns the test results in unchanged. |
|  | error out contains error information. This output provides standard error out functionality. |

#### Examples

Refer to the following VIs for examples of using the Create Report VI:

- Programmatically Run Tests from File VI: labview\examples\Unit Test Framework\Programmatic Tests
- Programmatically Run Tests from Project VI: labview\examples\Unit Test Framework\Programmatic Tests

<!--NI_TOPIC bundle=labview-unit-test-framework-toolkit-api-ref path=lvutf/utf_results_window.html language=enus -->
## TOPIC 00003: Open Results Window VI

- bundle_id: `labview-unit-test-framework-toolkit-api-ref`
- source_path: `lvutf/utf_results_window.html`
- source_url: https://docs-be.ni.com/bundle/labview-unit-test-framework-toolkit-api-ref/raw/resource/enus/lvutf/utf_results_window.html
- document_id: `labview-unit-test-framework-toolkit-api-ref`
- page_type: `leaf`
- content_type: ``

### Open Results Window VI

**Owning Palette:** [Unit Test Framework VIs](../lvutf/utf_vis.html)

**Requires:** Unit Test Framework Toolkit

Displays the [Unit Test Framework Results](../lvutf/utf_results_db.html) window after test execution.

[Examples](#examples)

[IMAGE alt='image' src='open_results_window.gif']

|  | test results in contains the results of the test execution from using either the Run Tests from File VI or Run Tests from Project VI. |
| --- | --- |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | test results out returns the test results in unchanged. |
|  | error out contains error information. This output provides standard error out functionality. |

#### Examples

Refer to the following VIs for examples of using the Open Results Window VI:

- Programmatically Run Tests from File VI: labview\examples\Unit Test Framework\Programmatic Tests
- Programmatically Run Tests from Project VI: labview\examples\Unit Test Framework\Programmatic Tests

<!--NI_TOPIC bundle=labview-unit-test-framework-toolkit-api-ref path=lvutf/utf_run_tests_file.html language=enus -->
## TOPIC 00004: Run Tests from File VI

- bundle_id: `labview-unit-test-framework-toolkit-api-ref`
- source_path: `lvutf/utf_run_tests_file.html`
- source_url: https://docs-be.ni.com/bundle/labview-unit-test-framework-toolkit-api-ref/raw/resource/enus/lvutf/utf_run_tests_file.html
- document_id: `labview-unit-test-framework-toolkit-api-ref`
- page_type: `leaf`
- content_type: ``

### Run Tests from File VI

**Owning Palette:** [Unit Test Framework VIs](../lvutf/utf_vis.html)

**Requires:** Unit Test Framework Toolkit

[Executes tests](../lvutfhowto/utfh_execute_vi.html#from_file) from [.lvtest](../lvutfconcepts/utfc_test_config.html) files.

You also can use the [Run Tests from Project](../lvutf/utf_run_tests_proj.html) VI to [execute tests](../lvutfhowto/utfh_execute_vi.html#from_project) from a [LabVIEW project](../lvutfconcepts/utfc_project.html).

|  | Note The Run Tests from File VI does not support execution on real-time (RT) targets. You must use the Run Tests from Project VI to execute tests on RT targets. |
| --- | --- |

[Example](#examples)

[IMAGE alt='image' src='run_tests_from_file.gif']

|  | show progress bar? specifies whether to show the progress window during test execution. The default is TRUE. |
| --- | --- |
|  | test file paths specifies the paths to each .lvtest file this VI executes. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | test results out returns test results of the specified .lvtest files. |
|  | error out contains error information. This output provides standard error out functionality. |

#### Example

Refer to the Programmatically Run Tests from File VI in the labview\examples\Unit Test Framework\Programmatic Tests directory for an example of using the Run Tests from File VI.

<!--NI_TOPIC bundle=labview-unit-test-framework-toolkit-api-ref path=lvutf/utf_run_tests_proj.html language=enus -->
## TOPIC 00005: Run Tests from Project VI

- bundle_id: `labview-unit-test-framework-toolkit-api-ref`
- source_path: `lvutf/utf_run_tests_proj.html`
- source_url: https://docs-be.ni.com/bundle/labview-unit-test-framework-toolkit-api-ref/raw/resource/enus/lvutf/utf_run_tests_proj.html
- document_id: `labview-unit-test-framework-toolkit-api-ref`
- page_type: `leaf`
- content_type: ``

### Run Tests from Project VI

**Owning Palette:** [Unit Test Framework VIs](../lvutf/utf_vis.html)

**Requires:** Unit Test Framework Toolkit

[Executes tests](../lvutfhowto/utfh_execute_vi.html#from_project) from a [LabVIEW project](../lvutfconcepts/utfc_project.html).

You also can use the [Run Tests from File](../lvutf/utf_run_tests_file.html) VI to [execute tests](../lvutfhowto/utfh_execute_vi.html#from_file) from [.lvtest](../lvutfconcepts/utfc_test_config.html) files.

[Example](#examples)

[IMAGE alt='image' src='run_tests_from_project.gif']

|  | show progress bar? specifies whether to show the progress window during test execution. The default is TRUE. |
| --- | --- |
|  | project file path specifies the path to the .lvproj file that contains .lvtest files. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | test results out returns test results of the .lvtest files in the specified .lvproj file. |
|  | error out contains error information. This output provides standard error out functionality. |

#### Example

Refer to the Programmatically Run Tests from Project VI in the labview\examples\Unit Test Framework\Programmatic Tests directory for an example of using the Run Tests from Project VI.

<!--NI_TOPIC bundle=labview-unit-test-framework-toolkit-api-ref path=lvutf/utf_vis.html language=enus -->
## TOPIC 00006: Unit Test Framework VIs

- bundle_id: `labview-unit-test-framework-toolkit-api-ref`
- source_path: `lvutf/utf_vis.html`
- source_url: https://docs-be.ni.com/bundle/labview-unit-test-framework-toolkit-api-ref/raw/resource/enus/lvutf/utf_vis.html
- document_id: `labview-unit-test-framework-toolkit-api-ref`
- page_type: `leaf`
- content_type: ``

### Unit Test Framework VIs

June 2013, 372585D-01

**Requires:** Unit Test Framework Toolkit. This topic might not match its corresponding palette in LabVIEW depending on your operating system, licensed product(s), and target.

Use the Unit Test Framework VIs to [execute tests programmatically](../lvutfhowto/utfh_execute_vi.html).

The VIs on this palette can return [general LabVIEW error codes](/csh?topicname=lverror/misc_lv_error_codes.html) or [specific Unit Test Framework error codes](../lvutf/utf_error_codes.html).

| Palette Object | Description |
| --- | --- |
| Create Report | Generates a report after test execution. You can generate this report in HTML, Automatic Test Markup Language (ATML), or ASCII format. |
| Open Results Window | Displays the Unit Test Framework Results window after test execution. |
| Run Tests from File | Executes tests from .lvtest files. You also can use the Run Tests from Project VI to execute tests from a LabVIEW project. |
| Run Tests from Project | Executes tests from a LabVIEW project. You also can use the Run Tests from File VI to execute tests from .lvtest files. |

© 2008–2013 National Instruments. All rights reserved.

<!--NI_TOPIC bundle=labview-unit-test-framework-toolkit-api-ref path=lvutfconcepts/utfc_code_cov.html language=enus -->
## TOPIC 00007: Code Coverage (Unit Test Framework Toolkit)

- bundle_id: `labview-unit-test-framework-toolkit-api-ref`
- source_path: `lvutfconcepts/utfc_code_cov.html`
- source_url: https://docs-be.ni.com/bundle/labview-unit-test-framework-toolkit-api-ref/raw/resource/enus/lvutfconcepts/utfc_code_cov.html
- document_id: `labview-unit-test-framework-toolkit-api-ref`
- page_type: `leaf`
- content_type: ``

### Code Coverage (Unit Test Framework Toolkit)

Code coverage measures the percentage of subdiagrams LabVIEW executes when you run a VI. This measurement provides information about the amount of code that was executed and might be useful when performing unit testing.

|  | Note The LabVIEW Unit Test Framework Toolkit cannot measure code coverage on real-time (RT) targets. |
| --- | --- |

The Unit Test Framework Toolkit calculates code coverage by dividing the total number of subdiagrams that execute during test execution by the total number of subdiagrams in the VI. Every VI has at least one subdiagram or diagram, which is the block diagram of the VI. Loops and structures have one or more subdiagrams. For example, For Loop and While Loop structures have one subdiagram each. Case and Sequence structures have one subdiagram per frame.

[IMAGE alt='image' src='code_cov_diagrams.gif']

The previous figure shows the block diagram of a VI. You can assume that each Case structure contains only two cases and no loops or structures other than the For Loop that already appears in the figure. Using these assumptions, this VI contains six subdiagrams. The six subdiagrams are the block diagram of the VI, the two cases for each Case structure (four subdiagrams total), and the For Loop. If five of the six subdiagrams execute during test execution, the code coverage measurement is 83.33%.

You must allow debugging for each VI under test in order to measure code coverage. If the VI properties of a VI under test do not have a checkmark in the **Allow debugging** checkbox, the code coverage result always will be zero. To allow debugging, open the VI under test, select **File»VI Properties** to display the [VI Properties](/csh?topicname=lvdialog/vi_properties_dialog_box.html) dialog box, select **Execution** from the pull-down menu, and place a checkmark in the **Allow debugging** checkbox.

You can specify a minimum code coverage requirement interactively by using the [Advanced](../lvutf/utf_advanced_db.html) page of the [Test Properties](../lvutf/utf_properties_db.html) dialog box. You also can specify a minimum code coverage requirement by editing .lvtest files.

When you execute a test, LabVIEW measures the percentage of subdiagrams covered for the VI under test. If the VI under test does not meet the minimum code coverage requirement you specified in the .lvtest file, test results show this test as failed. You can double-click an item on the **Code Coverage** page of the [Unit Test Framework Results](../lvutf/utf_results_db.html) window to highlight the subdiagram of the VI that LabVIEW did not cover during execution.

If you test a member VI of a dynamic dispatch method, LabVIEW may execute another member VI in the test according to the method. The Unit Test Framework toolkit generates code coverage of the VI that LabVIEW executed in the test. On the **Code Coverage** page of the [Unit Test Framework Results](../lvutf/utf_results_db.html) window, the Unit Test Framework toolkit uses a diamond (♦) to indicate a dynamic dispatch VI. The Unit Test Framework toolkit also lists all dynamic dispatch VIs of a test in the **Dependencies** list of this page.

Refer to the labview\examples\Unit Test Framework\Code Coverage\Code Coverage.lvproj for an example that demonstrates how to use code coverage.

##### Related Information

[Case Structures: Executing a Section of Code Based on Input Values](/csh?topicname=lvconcepts/case_structures_concepts.html)

[Dynamic and Static Dispatch Member VIs](/csh?topicname=lvconcepts/creating_classes.html)

[Loops and Other Structures](/csh?topicname=lvconcepts/loops_and_structures.html)

[Sequence Structures: Executing Sections of Code Sequentially](/csh?topicname=lvconcepts/sequence_structures_concepts.html)

[Specifying a Minimum Code Coverage Requirement](../lvutfhowto/utfh_specify_minimum_code_coverage.html)

#### Project Code Coverage

You can generate code coverage of a project by placing a checkmark in the **Include VIs that were not tested** checkbox on the [Unit Test Framework](../lvutf/utf_proj_prop_db.html) page. When you execute this test, LabVIEW opens all VIs in this project to count subdiagrams and generates the code coverage of this project. For example, you can create a project that contains two VIs and each VI contains three subdiagrams and a test case that covers all three subdiagrams of one VI. When you execute this test, LabVIEW opens both VIs to count subdiagrams. Because this projects contains six subdiagrams and the test covers three subdiagrams, the project code coverage measurement is 50%.

|  | Note If a project contains a large number of VIs, opening these VIs can slow performance. |
| --- | --- |

<!--NI_TOPIC bundle=labview-unit-test-framework-toolkit-api-ref path=lvutfconcepts/utfc_compare_type.html language=enus -->
## TOPIC 00008: Comparison Types (Unit Test Framework Toolkit)

- bundle_id: `labview-unit-test-framework-toolkit-api-ref`
- source_path: `lvutfconcepts/utfc_compare_type.html`
- source_url: https://docs-be.ni.com/bundle/labview-unit-test-framework-toolkit-api-ref/raw/resource/enus/lvutfconcepts/utfc_compare_type.html
- document_id: `labview-unit-test-framework-toolkit-api-ref`
- page_type: `leaf`
- content_type: ``

### Comparison Types (Unit Test Framework Toolkit)

The LabVIEW Unit Test Framework Toolkit provides several comparison types you use to compare resulting values with expected values. When you configure a test case, you specify a comparison type for each **Output Name** on the [Test Cases](../lvutf/utf_test_cases_db.html) page of the [Test Properties](../lvutf/utf_properties_db.html) dialog box. LabVIEW lists the available comparison types that each data type supports. You also can specify a user-defined comparison VI.

When you execute a test, LabVIEW runs the VI under test by using the input values you specified for each test case in the .lvtest file. LabVIEW then compares the resulting values with the expected values by using the comparison types you specified.

The following figure shows an example of specifying the comparison type for an output terminal.

[IMAGE alt='image' src='comparison.png']

In the previous figure, LabVIEW lists the available comparison types you can use to compare the resulting value of the **x*y** terminal with the expected value.

##### Related Information

[Creating a User-Defined Comparison VI](../lvutfhowto/utfh_create_comp.html)

#### Supported Comparison Types

The following table lists comparison types that the Unit Test Framework Toolkit supports.

| Comparison Type | Description |
| --- | --- |
| = | Resulting value equals the expected value. |
| = (elm) | Resulting array elements equal the expected array elements. |
| != | Resulting value does not equal the expected value. |
| != (elm) | Resulting array elements does not equal the expected array elements. |
| > | Resulting value is greater than the expected value. |
| >= | Resulting value is greater than or equal to the expected value. |
| < | Resulting value is less than the expected value. |
| <= | Resulting value is less than or equal to the expected value. |
| vector length | Resulting complex vector length equals the expected complex vector length. |
| range | Resulting value is within a given range, a and b, where a ≤ expected value ≤ b. |
| symmetric tolerance | Resulting value is within a symmetric tolerance, a and b, where a – b ≤expected value ≤ a + b. |
| asymmetric tolerance | Resulting value is within an asymmetric tolerance, a, b, and c where a – b ≤ expected value ≤ a + c. |
| string length | Resulting string length equals the expected value. |
| string contains | Resulting string contains the substring. |
| string not contain | Resulting string does not contain the substring. |
| array size | Resulting array size for each dimension equals the expected value. |
| array contains | Resulting array contains the element. |
| array not contain | Resulting array does not contain the element. |
| array range | All elements of the resulting array are within a given range, a and b, where a ≤ expected values ≤ b. |
| array range (limit array) | All elements of the resulting array are within the range of the array limit, A[n], and drift, b, where A[n] – b ≤ expected value ≤ A[n] + b. |
| by element | Applies to clusters and arrays only. Allows you to assign different comparison types for each element of an array or a cluster. |
| user-defined | Allows you to use a user-defined comparison VI to compare the resulting value with the expected value. |

|  | Note LabVIEW uses the Digits of precision for floating-point comparison you specified on the Advanced page of the Test Properties dialog box to compare the resulting floating-point values with expected floating-point values. |
| --- | --- |

Refer to the labview\examples\Unit Test Framework\User-Defined Comparison\User-Defined Comparison.lvproj for an example that demonstrates how to use user-defined comparison VIs in the Unit Test Framework Toolkit.

<!--NI_TOPIC bundle=labview-unit-test-framework-toolkit-api-ref path=lvutfconcepts/utfc_glossary.html language=enus -->
## TOPIC 00009: Glossary (Unit Test Framework Toolkit)

- bundle_id: `labview-unit-test-framework-toolkit-api-ref`
- source_path: `lvutfconcepts/utfc_glossary.html`
- source_url: https://docs-be.ni.com/bundle/labview-unit-test-framework-toolkit-api-ref/raw/resource/enus/lvutfconcepts/utfc_glossary.html
- document_id: `labview-unit-test-framework-toolkit-api-ref`
- page_type: `leaf`
- content_type: ``

### Glossary (Unit Test Framework Toolkit)

ACEINRSTUV

[LabVIEW Glossary](/csh?topicname=lvconcepts/glossary.html)

| A |  |
| --- | --- |
| array brackets | Characters LabVIEW uses to wrap control and indicator names of an array. |
| ATML | Automatic Test Markup Language—An industry standard report format commonly used in military and aerospace applications. Refer to the ATML website for more information about ATML. |
| C |  |
| caller VI | A VI that calls another VI. |
| code coverage | Measures the percentage of subdiagrams LabVIEW executes when you run a VI. |
| comparison types | How LabVIEW compares resulting values with expected values when checking VIs under test for functional correctness. |
| E |  |
| expected value | Value that you specify for a control or indicator of the VI under test. LabVIEW compares this value with the resulting value during test execution. |
| I |  |
| input value | Value that you specify for a control or indicator of the VI under test. LabVIEW uses this value as an input for the VI under test during test execution. |
| N |  |
| name separator | Character LabVIEW uses to separate control and indicator names of a cluster. |
| NI Requirements Gateway | Application that provides a requirements traceability solution linking development and verification documents to formal requirements stored in documents and databases. Refer to the National Instruments website for information about NI Requirements Gateway. |
| R |  |
| requirement IDs | Define traceability relationships between requirements and code. Use requirement IDs with NI Requirements Gateway. |
| resulting value | Value that the VI under test returns during test execution. When you execute a test, LabVIEW runs the VI under test by using the input values you specified in the .lvtest file. |
| S |  |
| setup VI | VI that LabVIEW runs before checking the VI under test for functional correctness. LabVIEW passes the output values from the setup VI to the inputs of the VI under test. |
| T |  |
| teardown VI | VI that LabVIEW runs after checking the VI under test for functional correctness. LabVIEW passes the resulting values from the VI under test to the inputs of the teardown VI. |
| test | .lvtest file containing the settings that LabVIEW uses to check the VI under test for functional correctness. |
| test case | Contains a set of input values, expected values, and comparison types that LabVIEW uses to check the VI under test for functional correctness. A test contains one or more test cases. |
| test result | .lvutf file containing the test results that LabVIEW displays in the Unit Test Framework Results window. |
| timeout | Amount of time in which LabVIEW must complete a test execution. |
| U |  |
| unit testing | Method of testing that verifies the individual units of source code are working properly. |
| V |  |
| VI under test | VI that LabVIEW checks for functional correctness when you execute a test. |

<!--NI_TOPIC bundle=labview-unit-test-framework-toolkit-api-ref path=lvutfconcepts/utfc_intro.html language=enus -->
## TOPIC 00010: Introduction to the LabVIEW Unit Test Framework Toolkit (Unit Test Framework Toolkit)

- bundle_id: `labview-unit-test-framework-toolkit-api-ref`
- source_path: `lvutfconcepts/utfc_intro.html`
- source_url: https://docs-be.ni.com/bundle/labview-unit-test-framework-toolkit-api-ref/raw/resource/enus/lvutfconcepts/utfc_intro.html
- document_id: `labview-unit-test-framework-toolkit-api-ref`
- page_type: `leaf`
- content_type: ``

### Introduction to the LabVIEW Unit Test Framework Toolkit (Unit Test Framework Toolkit)

The LabVIEW Unit Test Framework Toolkit provides tools you use to check VIs for functional correctness. When you create a test from the [Project Explorer](/csh?topicname=lvdialog/project_explorer_window.html) window, LabVIEW creates a .lvtest file on disk. Each .lvtest file contains the settings LabVIEW uses to check the VI under test for functional correctness. When you execute a test, LabVIEW runs the VI under test by using the input values you specified for each test case in the .lvtest file. LabVIEW then compares the resulting values with the expected values by using the comparison types you specified.

|  | Note The Unit Test Framework Toolkit cannot check polymorphic VIs for functional correctness. |
| --- | --- |

Using the Unit Test Framework Toolkit involves the following steps:

1. Creating projects and tests. You must create and save a LabVIEW project before you can create tests.
 Use projects to group together all the files you need to perform unit testing. Use the Project Explorer window to create tests.
2. Configuring tests. Use the Project Explorer window to configure tests interactively. You also can configure tests by editing .lvtest files. Each .lvtest file contains the settings you specify for a test.
3. Managing tests. Use virtual folders, auto-populating folders, and LabVIEW project libraries to organize a project. You can drag and drop files inside the Project Explorer window to manage a project. Use the Project Explorer window to find tests and VIs.
4. Executing tests. Use the Project Explorer window to execute tests interactively. You also can execute tests programmatically by using the Unit Test Framework VIs.
5. Viewing test results and generating reports. Use the Unit Test Framework Results window to view test results. The Project Explorer window also displays results from the test execution. You can generate test reports in different formats. Test reports contain results from the execution. You can customize test reports by specifying the contents of the reports. You also can format HTML reports by using a Cascading Style Sheet (CSS) file. In addition, you can generate log files during test execution.

Refer to the labview\examples\Unit Test Framework\Basic Functions\Basic Functions.lvproj for an example that demonstrates how to use the Unit Test Framework Toolkit to create tests.

##### Related Information

[Configuring Tests](../lvutfhowto/utfh_configure.html)

[Creating Tests](../lvutfhowto/utfh_create_tests.html)

[Executing Tests](../lvutfhowto/utfh_execute.html)

[Managing Tests](../lvutfhowto/utfh_manage.html)

[Viewing Test Results and Generating Reports](../lvutfhowto/utfh_results.html)

<!--NI_TOPIC bundle=labview-unit-test-framework-toolkit-api-ref path=lvutfconcepts/utfc_project.html language=enus -->
## TOPIC 00011: Using the Project Explorer Window (Unit Test Framework Toolkit)

- bundle_id: `labview-unit-test-framework-toolkit-api-ref`
- source_path: `lvutfconcepts/utfc_project.html`
- source_url: https://docs-be.ni.com/bundle/labview-unit-test-framework-toolkit-api-ref/raw/resource/enus/lvutfconcepts/utfc_project.html
- document_id: `labview-unit-test-framework-toolkit-api-ref`
- page_type: `leaf`
- content_type: ``

### Using the Project Explorer Window (Unit Test Framework Toolkit)

Use the [Project Explorer](/csh?topicname=lvdialog/project_explorer_window.html) window to create, configure, manage, and execute tests interactively in a LabVIEW project.
 You must create and save a LabVIEW project before you can create tests. When you save a project, LabVIEW creates a project file (.lvproj) that includes references to all the files in the project. Use projects to group together all the files you need to perform unit testing.
 Use virtual folders, auto-populating folders, and LabVIEW project libraries to organize a project.

#### Items and Files Pages

The [Project Explorer](/csh?topicname=lvdialog/project_explorer_window.html) window includes the **Items** and **Files** pages. The **Items** page displays all the .lvtest files, VIs, folders, and libraries that exist in the project tree. The **Files** page displays the project items that have a corresponding file on disk. When you create a test from the **Project Explorer** window, LabVIEW creates a .lvtest file on disk. A .lvtest file icon appears on both the **Items** and **Files** pages.

The following figure shows an example project.

[IMAGE alt='image' src='project_explorer.png']

##### Related Information

[Tests and .lvtest Files](../lvutfconcepts/utfc_test_config.html)

#### Test Results

After you execute tests and return to the [Project Explorer](/csh?topicname=lvdialog/project_explorer_window.html) window, colored dots appear next to the icon of each test you executed. These dots denote whether the test passed (green), failed (red), produced errors (exclamation mark), or was skipped (gray).

The following figure shows an example of test results in the [Project Explorer](/csh?topicname=lvdialog/project_explorer_window.html) window.

[IMAGE alt='image' src='results_project.png']

|  | Note After every subsequent test execution, LabVIEW updates the test results in the Project Explorer window. However, you cannot save the test results when you close the project. |
| --- | --- |

#### Unit Test Framework Toolbar

Use the buttons on the **Unit Test Framework** toolbar to execute tests and view the [Unit Test Framework Results](../lvutf/utf_results_db.html) window. This toolbar is available at the top of the [Project Explorer](/csh?topicname=lvdialog/project_explorer_window.html) window..

|  | Note You might need to expand the Project Explorer window horizontally to view this toolbar. |
| --- | --- |

You can show or hide the **Unit Test Framework** toolbar by selecting **View»Toolbars»Unit Test Framework**. You also can right-click an unused area on the toolbar and select **Unit Test Framework**.

The **Unit Test Framework** toolbar on the [Project Explorer](/csh?topicname=lvdialog/project_explorer_window.html) window contains the following buttons.

|  | Run Unit Tests—Executes all tests in a LabVIEW project. If test filters are set, such as executing tests by priority or executing only modified tests, LabVIEW executes only filtered tests. |
| --- | --- |
|  | Unit Test Framework Results—Displays the Unit Test Framework Results window. Use this window to view, save, and load test results. |

##### Related Information

[Executing Only Modified Tests (Unit Test Framework Toolkit)](../lvutfhowto/utfh_execute_mod.html)

[Executing Tests by Priority (Unit Test Framework Toolkit)](../lvutfhowto/utfh_execute_pri.html)

[Executing Tests Interactively (Unit Test Framework Toolkit)](../lvutfhowto/utfh_execute_test.html)

[Saving and Loading Test Results (Unit Test Framework Toolkit)](../lvutfhowto/utfh_result_saveload.html)

[Test Results (Unit Test Framework Toolkit)](../lvutfconcepts/utfc_results.html)

#### Project Properties

You can configure global settings related to creating and executing tests by using the [Project Properties](/csh?topicname=lvdialog/project_properties.html) dialog box. In the [Project Explorer](/csh?topicname=lvdialog/project_explorer_window.html) window, select **Project»Properties** to display this dialog box. You also can click the **Project Properties** button on the [Project toolbar](/csh?topicname=glang/project_toolbar.html) or right-click the project root and select **Properties** from the shortcut menu to display this dialog box.

#### Build Specifications

The **Build Specifications** item in the [Project Explorer](/csh?topicname=lvdialog/project_explorer_window.html) window allows you to create and configure build specifications for LabVIEW builds. A build specification contains all the settings for the build, such as files to include, directories to create, and settings for VIs.

You can configure the following types of build specifications to include .lvtest files:

- Installers (Windows)
- Source distributions
 [IMAGE alt='image' src='caution.gif']
**Caution** When configuring VIs in a source distribution, do not place checkmarks in the **Remove front panel** and **Remove block diagram** checkboxes on the [Source File Settings](/csh?topicname=lvdialog/source_file_distrib_page.html) page of the [Source Distribution Properties](/csh?topicname=lvdialog/source_distrib_db.html) dialog box for any VI under test. If you remove the front panel or block diagram of a VI under test, LabVIEW returns test errors on the **Test Errors** page of the [Unit Test Framework Results](../lvutf/utf_results_db.html) window.
- Zip files

You must have the Application Builder installed to build installers and zip files. The LabVIEW Professional Development System includes the Application Builder. If you use the LabVIEW Base Development System or Full Development System, you can purchase the Application Builder separately by visiting the National Instruments website. If you have already purchased the Application Builder, select **Help»Activate LabVIEW Components** to activate the product.

You can hide the **Build Specifications** item in the [Project Explorer](/csh?topicname=lvdialog/project_explorer_window.html) window. If you hide this item you must display it again to access the item.

##### Related Information

[Creating Build Specifications](/csh?topicname=lvconcepts/creating_build_specs.html)

[Configuring Build Specifications](/csh?topicname=lvconcepts/configuring_build_specs.html)

[Showing and Hiding Items in a Project](/csh?topicname=lvhowto/showing_hiding_nodes.html)

<!--NI_TOPIC bundle=labview-unit-test-framework-toolkit-api-ref path=lvutfconcepts/utfc_quick_start.html language=enus -->
## TOPIC 00012: Quick Start Guide (Unit Test Framework Toolkit)

- bundle_id: `labview-unit-test-framework-toolkit-api-ref`
- source_path: `lvutfconcepts/utfc_quick_start.html`
- source_url: https://docs-be.ni.com/bundle/labview-unit-test-framework-toolkit-api-ref/raw/resource/enus/lvutfconcepts/utfc_quick_start.html
- document_id: `labview-unit-test-framework-toolkit-api-ref`
- page_type: `leaf`
- content_type: ``

### Quick Start Guide (Unit Test Framework Toolkit)

Complete the following steps to create, configure, and execute tests in the [Project Explorer](/csh?topicname=lvdialog/project_explorer_window.html) window.

1. Launch LabVIEW.
2. Select File»New to display the New dialog box and select Project»Empty Project to create a new project.
3. Add VIs you want to test to a target, such as My Computer , and select File»Save to save the project.
4. Right-click a VI and select Unit Tests»New Test from the shortcut menu to create a test. A .lvtest file with the same name as the VI appears in the project tree.
5. Right-click the .lvtest file and select Properties from the shortcut menu to display the Test Properties dialog box. Use this dialog box to configure tests.
6. Use the Unit Test Framework Toolbar at the top of the Project Explorer window. Use the Project Properties dialog box to configure settings related to creating and executing tests.

##### Related Information

[Configuring Tests](../lvutfhowto/utfh_configure.html)

[Creating Tests](../lvutfhowto/utfh_create_tests.html)

[Executing Tests](../lvutfhowto/utfh_execute.html)

[Managing a Project in LabVIEW](/csh?topicname=lvconcepts/using_labview_projects.html)

<!--NI_TOPIC bundle=labview-unit-test-framework-toolkit-api-ref path=lvutfconcepts/utfc_related_doc.html language=enus -->
## TOPIC 00013: Related Documentation (Unit Test Framework Toolkit)

- bundle_id: `labview-unit-test-framework-toolkit-api-ref`
- source_path: `lvutfconcepts/utfc_related_doc.html`
- source_url: https://docs-be.ni.com/bundle/labview-unit-test-framework-toolkit-api-ref/raw/resource/enus/lvutfconcepts/utfc_related_doc.html
- document_id: `labview-unit-test-framework-toolkit-api-ref`
- page_type: `leaf`
- content_type: ``

### Related Documentation (Unit Test Framework Toolkit)

The following documents contain information that you may find helpful as you use this help file:

- LabVIEW Unit Test Framework Toolkit Readme —Use this file to obtain introductory information about the Unit Test Framework Toolkit, such as overview information, system requirements, installation instructions, and known issues with LabVIEW. Open this readme by navigating to the labview\readme directory and opening readme_UTF.html .
- LabVIEW Unit Test Framework Toolkit Example VIs—Refer to the labview\examples\Unit Test Framework directory for example VIs that demonstrate common tasks using the Unit Test Framework Toolkit. You also can access these VIs by selecting Help»Find Examples from the pull-down menu and selecting Toolkits and Modules»Unit Test Framework in the NI Example Finder window.
- Additional LabVIEW documentation .
- The LabVIEW VI Analyzer Toolkit documentation.
- The LabVIEW Desktop Execution Trace Toolkit documentation.
- The NI Requirements Gateway documentation.
- The NI TestStand documentation.

The following third-party document contains information that you may find helpful as you use this help file:

|  | Note The following resources offer useful background information on the general concepts discussed in this documentation. These resources are provided for general informational purposes only and are not affiliated, sponsored, or endorsed by National Instruments. The content of these resources is not a representation of, may not correspond to, and does not imply current or future functionality in the LabVIEW Unit Test Framework Toolkit or any other National Instruments product. |
| --- | --- |

- The Microsoft Excel documentation.

<!--NI_TOPIC bundle=labview-unit-test-framework-toolkit-api-ref path=lvutfconcepts/utfc_results.html language=enus -->
## TOPIC 00014: Test Results (Unit Test Framework Toolkit)

- bundle_id: `labview-unit-test-framework-toolkit-api-ref`
- source_path: `lvutfconcepts/utfc_results.html`
- source_url: https://docs-be.ni.com/bundle/labview-unit-test-framework-toolkit-api-ref/raw/resource/enus/lvutfconcepts/utfc_results.html
- document_id: `labview-unit-test-framework-toolkit-api-ref`
- page_type: `leaf`
- content_type: ``

### Test Results (Unit Test Framework Toolkit)

The LabVIEW Unit Test Framework Toolkit provides several methods of returning test results from the test execution. You can view test results in the [Unit Test Framework Results](../lvutf/utf_results_db.html) window that appears after execution is complete. The [Project Explorer](/csh?topicname=lvdialog/project_explorer_window.html) window also displays results from the test execution. You can generate test reports in several file formats. You also can generate log files.

##### Related Information

[Generating Test Reports](../lvutfhowto/utfh_report_generate.html)

[Generating Log Files](../lvutfhowto/utfh_report_log.html)

#### Results Window

The [Unit Test Framework Results](../lvutf/utf_results_db.html) window provides both summary and detailed information about the test execution, including tests and VIs that passed, failed, were skipped, or produced errors. Use this window to view test results. You also can save the results from this window to a .lvutf file that you can load later.

A .lvutf file contains the test results of the test execution. You can read .lvutf files interactively from the project window or programmatically by using the [Open Results Window](../lvutf/utf_results_window.html) VI. LabVIEW loads .lvutf files in the [Unit Test Framework Results](../lvutf/utf_results_db.html) window only.

The following figure shows an example of test results in the [Unit Test Framework Results](../lvutf/utf_results_db.html) window.

[IMAGE alt='image' src='results_window.png']

##### Related Information

[Saving and Loading Test Results](../lvutfhowto/utfh_result_saveload.html#save)

#### Project Explorer Window

After you execute tests and return to the [Project Explorer](/csh?topicname=lvdialog/project_explorer_window.html) window, colored dots appear next to the icon of each test you executed. These dots denote whether the test passed (green), failed (red), produced errors (exclamation mark), or was skipped (gray).

The following figure shows an example of test results in the [Project Explorer](/csh?topicname=lvdialog/project_explorer_window.html) window.

[IMAGE alt='image' src='results_project.png']

|  | Note After every subsequent test execution, LabVIEW updates the test results in the Project Explorer window. However, you cannot save the test results when you close the project. |
| --- | --- |

#### Test Reports

You can configure the Unit Test Framework Toolkit to generate test reports after test execution is complete. Test reports contain results from the execution. You can customize test reports by specifying the contents of the reports.

You can generate test reports in the following file formats:

- HTML —HTML reports contain advanced text formatting such as headings, a table of contents, tables, and hyperlinks. You can view HTML reports by using any Web browser. You also can format HTML reports by using a Cascading Style Sheet (CSS) file.
- ATML —Automatic Test Markup Language (ATML) is a standardized, XML-based report format. ATML is an emerging standard in military and aerospace industries for sharing data between different components of a test system. The primary purpose of ATML is to specify standards for test environments that encompass the total product life cycle. ATML defines an integrated set of test-related information that supports the information needs of test environments for testing applications. ATML reports include requirement IDs so that you can track tests and test results in NI Requirements Gateway. You can transform ATML files into HTML files by using Extensible Stylesheet Language Transformations (XSLT), providing flexibility in creating user-defined test reports. For more information about ATML, refer to the ATML website.
- ASCII —ASCII reports are tab-delimited text reports that you can view by using any data processing applications.

#### Log Files

You can configure the Unit Test Framework Toolkit to generate log files during test execution. Log files contain detailed information about the execution.

You can generate the following log files:

- Test Status —This log file is a .txt file that contains information about the most recent test execution and results. During execution, LabVIEW logs test names, times of execution, durations of execution, and whether the tests passed ( 1 ), failed ( 0 ), produced errors ( 2 ), or were skipped ( 3 ).
 [IMAGE alt='image' src='note.gif']
**Note** LabVIEW uses the information in this log file to determine which tests to execute when you execute tests that have been modified since the last execution. You must generate this log file in order to execute only modified tests.
- Test Execution —This log file is a .txt file that contains detailed information about the previous test execution(s). During execution, LabVIEW logs the entire execution process, including the test path, VI path, time of execution, running setup and teardown VIs, code coverage measurement, and test cases results. You can use this log file to troubleshoot tests that timed out, produced errors, or did not complete.

##### Related Information

[Executing Only Modified Tests](../lvutfhowto/utfh_execute_mod.html)

[Generating Log Files](../lvutfhowto/utfh_report_log.html)

<!--NI_TOPIC bundle=labview-unit-test-framework-toolkit-api-ref path=lvutfconcepts/utfc_set_tear.html language=enus -->
## TOPIC 00015: Setup and Teardown VIs (Unit Test Framework Toolkit)

- bundle_id: `labview-unit-test-framework-toolkit-api-ref`
- source_path: `lvutfconcepts/utfc_set_tear.html`
- source_url: https://docs-be.ni.com/bundle/labview-unit-test-framework-toolkit-api-ref/raw/resource/enus/lvutfconcepts/utfc_set_tear.html
- document_id: `labview-unit-test-framework-toolkit-api-ref`
- page_type: `leaf`
- content_type: ``

### Setup and Teardown VIs (Unit Test Framework Toolkit)

During unit testing, you might want to perform tasks before and after checking a VI for functional correctness. For example, you might want to power up an instrument, open a file, or pass values from another VI to the VI under test. After LabVIEW finishes checking the VI under test for functional correctness, you might want to pass values from the VI under test to another VI, close a file, or power down an instrument.

A setup VI is a VI that LabVIEW runs before checking the VI under test for functional correctness. A teardown VI is a VI that LabVIEW runs after checking the VI under test for functional correctness. The LabVIEW Unit Test Framework Toolkit provides tools you use to configure a test to run setup and teardown VIs. You also can pass values among the setup VI, the VI under test, and the teardown VI.

You can configure tests to run setup and teardown VIs by using the [Setup/Teardown](../lvutf/utf_set_tear_db.html) page of the [Test Properties](../lvutf/utf_properties_db.html) dialog box. You also can specify setup and teardown VIs by editing .lvtest files. Use the [Test Cases](../lvutf/utf_test_cases_db.html) page to specify the input values, expected values, and comparison types of the setup and teardown VIs for each test case.

When you execute a test, LabVIEW first runs the setup VI and then passes the output values from the setup VI to the inputs of the VI under test. LabVIEW then checks the VI under test for functional correctness and passes the resulting values from the VI under test to the inputs of the teardown VI.

The following figure shows an example of configuring the setup and teardown VIs for a test.

[IMAGE alt='image' src='setup_teardown.png']

The previous figure shows the configurations for running the setup and teardown VIs during test execution. When you execute this test, LabVIEW runs the setup VI and passes the values from the **refnum out** and **error out** terminals of the setup VI to the **refnum** and **error in** terminals of the VI under test. LabVIEW then runs the VI under test by using the values from the setup VI as input values. For input values that are not passed from the setup VI, such as the **text** input in this example, LabVIEW uses the input values from the **Test Cases** page. After checking the VI under test for functional correctness, LabVIEW passes the values from the **refnum out** and **error out** terminals to the corresponding inputs of the teardown VI.

|  | Note If the teardown VI has an error out output and the output contains an error, LabVIEW shows this test on the Test Errors page of the Unit Test Framework Results window instead of on the Test Results page. |
| --- | --- |

Refer to the labview\examples\Unit Test Framework\Setup Teardown\Setup Teardown.lvproj for an example that demonstrates how to use setup and teardown VIs.

##### Related Information

[Configuring Tests to Run Setup and Teardown VIs](../lvutfhowto/utfh_config_set_tear.html)

<!--NI_TOPIC bundle=labview-unit-test-framework-toolkit-api-ref path=lvutfconcepts/utfc_support.html language=enus -->
## TOPIC 00016: Supported Execution Targets (Unit Test Framework Toolkit)

- bundle_id: `labview-unit-test-framework-toolkit-api-ref`
- source_path: `lvutfconcepts/utfc_support.html`
- source_url: https://docs-be.ni.com/bundle/labview-unit-test-framework-toolkit-api-ref/raw/resource/enus/lvutfconcepts/utfc_support.html
- document_id: `labview-unit-test-framework-toolkit-api-ref`
- page_type: `leaf`
- content_type: ``

### Supported Execution Targets (Unit Test Framework Toolkit)

You can use the LabVIEW Unit Test Framework Toolkit to execute tests on different types of targets. The following table shows the supported target types and any additional software you must install to execute tests on that type of target.

| Type of Target | Additional Required Software |
| --- | --- |
| A Windows PC | — |
| An NI Real-Time (RT) target, such as an NI PXI or CompactRIO controller, running a real-time operating system (RTOS). | LabVIEW Real-Time Module Driver software for any hardware devices |

You must enable the VI Server on an RT target to execute unit tests on this RT target. You can enable the VI Server by using either of the following methods:

- In the Project Explorer window, configure the VI Server for the RT target .
- In the Test Execution section of the Unit Test Framework page, place a checkmark in the Enable VI Server on real-time targets checkbox.

Refer to the National Instruments website for information about the National Instruments products this table mentions.

##### Related Information

[Capabilities of the VI Server](/csh?topicname=lvconcepts/capabilities_of_the_vi_server.html)

[Configuring the VI Server](/csh?topicname=lvhowto/configuring_the_vi_server.html)

<!--NI_TOPIC bundle=labview-unit-test-framework-toolkit-api-ref path=lvutfconcepts/utfc_test_config.html language=enus -->
## TOPIC 00017: Tests and .lvtest Files (Unit Test Framework Toolkit)

- bundle_id: `labview-unit-test-framework-toolkit-api-ref`
- source_path: `lvutfconcepts/utfc_test_config.html`
- source_url: https://docs-be.ni.com/bundle/labview-unit-test-framework-toolkit-api-ref/raw/resource/enus/lvutfconcepts/utfc_test_config.html
- document_id: `labview-unit-test-framework-toolkit-api-ref`
- page_type: `leaf`
- content_type: ``

### Tests and .lvtest Files (Unit Test Framework Toolkit)

The LabVIEW Unit Test Framework Toolkit provides tools you use to create tests to check VIs for functional correctness. When you create a test from the [Project Explorer](/csh?topicname=lvdialog/project_explorer_window.html) window, LabVIEW creates a .lvtest file on disk. A .lvtesticon appears on both the **Items** and **Files** pages.

Each .lvtest file contains the settings LabVIEW uses to check the VI under test for functional correctness. When you execute a test, LabVIEW runs the VI under test by using the input values you specified for each test case in the .lvtest file. LabVIEW then compares the resulting values with the expected values by using the comparison types you specified.

|  | Note By default, LabVIEW saves the .lvtest file in the same directory as the VI under test. You can specify a different Default location file path on the Unit Test Framework page of the Project Properties dialog box. |
| --- | --- |

Use the [Project Explorer](/csh?topicname=lvdialog/project_explorer_window.html) window to configure tests interactively. You also can configure tests by editing .lvtest files.

##### Related Information

[Creating Tests](../lvutfhowto/utfh_create_tests.html)

[Tests and .lvtest Files](../lvutfconcepts/utfc_test_config.html)

#### Test File Format

You can view and edit .lvtest files by using Microsoft Excel or a text editor.

|  | Note If you use Microsoft Excel to edit a .lvtest file, you must save the file using Unicode Text (.txt) file format. When you save a .lvtest file, Microsoft Excel modifies formatting that is not compatible with tab-delimited text. For example, if a cell contains a comma, Microsoft Excel uses double quotation marks to enclose the cell contents. This conversion might result in an unexpected error in the .lvtest file. Refer to the Microsoft Excel documentation for more information about formatting that is not compatible with tab-delimited text. |
| --- | --- |

The following table contains information about each component of a .lvtest file, including descriptions, default values, and notes. When you edit a .lvtest file, the file must include components that LabVIEW uses to read and execute a test.

|  | Caution Do not remove any lines or components from a .lvtest file. If you remove anything, the test might not execute properly. |
| --- | --- |

| Component | Description | Default Value | Notes |
| --- | --- | --- | --- |
| LabVIEW Unit Test Framework | Header information that LabVIEW uses to identify tests that you created by using the Unit Test Framework Toolkit. | N/A | Do not modify. |
| Version | Header information that LabVIEW uses to identify the version of the Unit Test Framework Toolkit the test was created in. | Automatic† | Do not modify. |
| VI under Test | Specifies the path to the VI under test. If the .lvtest file is located in the same directory as the VI under test, LabVIEW displays only the name of the VI without the path. | Automatic† | If the .lvtest file is located in the same drive as the VI under test, use the relative path. Otherwise, use the absolute path. You can specify only one VI under test for each .lvtest file. |
| Library | Specifies the path to the LabVIEW class library (.lvclass) or the LabVIEW project library (.lvlib) the test vector file belongs to, if any. | Automatic† | If the .lvtest file is located in the same drive as the library, use the relative path. Otherwise, use the absolute path. |
| Comment | Specifies comments about the test. | N/A | Comment cannot contain line breaks. |
| Priority | Specifies priority of the test. This priority determines whether LabVIEW executes the test when you execute tests by priority. | 5 | The highest priority is 1000, and the lowest priority is 0. |
| Requirement ID | Specifies requirement IDs for integration with NI Requirements Gateway. | Optional | N/A |
| Skip Test (Project Explorer Window) | Specifies whether to skip the test when you execute tests interactively from the Project Explorer window. | NO | YES/NO |
| Skip Test (Unit Test Framework VIs) | Specifies whether to skip the test when you execute tests programmatically by using the Unit Test Framework VIs. | NO | YES/NO |
| Decimal Separator | Specifies the character LabVIEW uses to separate the integral and fractional parts of a decimal number. | . | Valid decimal separators: . , |
| Set Timeout | Specifies whether to set a timeout when executing the test. | NO | YES/NO |
| Timeout | Specifies the time limit, in seconds, in which LabVIEW must complete the test execution. | 0 | Use a numeric value.This value is valid only when Set Timeout is set to YES. |
| Check Code Coverage | Specifies whether to set a minimum code coverage requirement when executing the test. | NO | YES/NO |
| Minimum Code Coverage | Specifies the percentage of subdiagrams LabVIEW must execute during test execution. | 100 | Valid minimum code coverage: 0-100.This number is valid only when Check Code Coverage is set to YES. |
| User-Defined Test | Specifies whether to use a user-defined test VI to execute the test. | NO | YES/NO |
| User-Defined Test VI Path | Specifies the path to the user-defined test VI. | N/A | This path is valid only when User-Defined Test is set to YES. |
| Name Separator | Specifies the character LabVIEW uses to separate control and indicator names of a cluster. | / | Valid name separators: / \\ \| : ` ~ ! @ # $ % ^ & * - _ = + ' " : ; ? |
| Array Brackets | Specifies the characters LabVIEW uses to wrap control and indicator names of an array. | [] | Valid array brackets: () [] {} <> |
| Repetitions | Specifies the number of times to repeat a test. | 1 | Use a numeric value. |
| Digits of Precision | Specifies the number of digits after the decimal separator LabVIEW uses to compare floating-point values. | 6 | Valid digits of precision: 0-32 |
| Input/Output Values | Specifies which controls and indicators of the VI under test appear on the Test Cases page of the Test Properties dialog box. | Include controls and indicators from connector pane | Available Options:- Include controls and indicators from connector pane- Include controls and indicators from front panel- Include controls and indicators from front panel as both input and output |
| Maximum Array Elements | Specifies the maximum number of array elements that LabVIEW lists on the Test Cases page of the Test Properties dialog box. If an array contains more elements than the specified number, LabVIEW lists the array as one item. | 100 | Use a numeric value. |
| Save Control Names in Normal Format | Specifies whether to save control names in normal format. If a control name contains non-printable control characters used for text formatting, which are the first 32 codes (from 0 to 31) in the ASCII code table, LabVIEW displays NO. Otherwise, LabVIEW displays YES. | Automatic† | Do not modify. |
| Capture Input Values | Specifies whether to capture the default input values from the VI under test when creating a test. | YES | N/A |
| Capture Output Values | Specifies whether to capture the default output values from the VI under test when creating a test. | YES | N/A |
| Set Automatic Error Handling | Specifies whether to automatically handle errors for the VI under test during test execution. | As is | Available options:- As is- Enable automatic error handling- Disable automatic error handling |
| Remove Breakpoints | Specifies whether to toggle test execution suspension at a breakpoint. | YES | YES/NO |
| Test Case Name | Lists the name of each test case. | 1 | Use a numeric value or a user-defined name. Test Case Name cannot contain components of a.lvtestfile. |
| Test Case Comment | Specifies comments about the test case. | N/A | Test Case Comment cannot contain line breaks. |
| Test Case | Lists the name of each test case. | Automatic† | N/A |
| VI | Specifies the type of VI which contains the terminals to configure a test case. | N/A | Valid VI types:- VI under Test- Setup VI- Teardown VI |
| In/Out | Specifies whether LabVIEW uses each terminal as an input or output. | Default for controls is IN.Default for indicators is OUT. | IN/OUT |
| Set/Check | Specifies whether each terminal sets, checks, or ignores the input or expected value. | Default for controls is SET.Default for indicators is CHECK. | SET/CHECK/IGNORE |
| Control Name | Specifies the name of each terminal. | Automatic† | Name must match the terminals on the VI under test. If the terminal is an array, the number in square brackets ([ ]) indicates the index of a specific array element. The index is zero-based, which means it is in the range of 0 to n-1, where n is the number of elements in the array or cluster. For example, Array[0] refers to the first element of the array. If the terminal is a cluster, LabVIEW uses a forward slash (/) to separate control and indicator names. You can change the default array brackets and name separator on the Unit Test Framework page of the Project Properties dialog box. |
| Data Type | Specifies the data type of each terminal. | Automatic† | N/A |
| Value | Specifies the input or expected value of each terminal. | Automatic† | N/A |
| Comparison | Specifies the comparison type LabVIEW uses to compare the resulting value with the expected value. | = | Supported comparison types. |
| Comparison VI Path | Specifies the path to the user-defined comparison VI. | N/A | N/A |
| Vector Name | Specifies the name of test vector assigned to each terminal | N/A | N/A |
| Setup VI Path | Specifies the path to the setup VI. | N/A | N/A |
| Output of Setup VI | Specifies the output terminals of the setup VI that LabVIEW uses to pass values from the setup VI to the VI under test. | N/A | N/A |
| Input of VI under Test | Specifies the input terminals of the VI under test that LabVIEW uses to retrieve values from the setup VI. | N/A | N/A |
| Teardown VI Path | Specifies the path to the teardown VI. | N/A | N/A |
| Input of Teardown VI | Specifies the input terminals of the teardown VI that LabVIEW uses to retrieve values from the VI under test. | N/A | N/A |
| Output of VI under Test | Specifies the output terminals of the VI under test that LabVIEW uses to pass values from the VI under test to the teardown VI. | N/A | N/A |
| Included Vector Files | Specifies the test vector files that a test contains. | N/A | If the test vector file is located in the same folder as the VI under test, list the test vector file name. Otherwise, use the relative path. |
| Notes: † LabVIEW gathers and displays this information when you create the test. |  |  |  |

##### Related Information

[Code Coverage](../lvutfconcepts/utfc_code_cov.html)

[Creating Projects and Tests](../lvutfhowto/utfh_create.html)

[Executing Tests](../lvutfhowto/utfh_execute.html)

[Requirement IDs](../lvutfconcepts/utfc_test_require.html)

[Setup and Teardown VIs](../lvutfconcepts/utfc_set_tear.html)

#### Example of a .lvtest File

The following figure shows an example of a .lvtest file.

[IMAGE alt='image' src='lvtest_example.png']

<!--NI_TOPIC bundle=labview-unit-test-framework-toolkit-api-ref path=lvutfconcepts/utfc_test_priority.html language=enus -->
## TOPIC 00018: Test Priority (Unit Test Framework Toolkit)

- bundle_id: `labview-unit-test-framework-toolkit-api-ref`
- source_path: `lvutfconcepts/utfc_test_priority.html`
- source_url: https://docs-be.ni.com/bundle/labview-unit-test-framework-toolkit-api-ref/raw/resource/enus/lvutfconcepts/utfc_test_priority.html
- document_id: `labview-unit-test-framework-toolkit-api-ref`
- page_type: `leaf`
- content_type: ``

### Test Priority (Unit Test Framework Toolkit)

A test priority determines the level of importance of a test. When you create tests, LabVIEW assigns a default priority of 5. The highest priority is 1000, and the lowest priority is 0.

You can specify a test priority interactively by using the [Configuration](../lvutf/utf_configuration_db.html) page of the [Test Properties](../lvutf/utf_properties_db.html) dialog box. You also can specify a test priority by editing .lvtest files.

When you execute tests by priority, LabVIEW executes only tests with an equal or higher priority than the **Minimum priority** you specified on the [Unit Test Framework](../lvutf/utf_proj_prop_db.html) page of the [Project Properties](/csh?topicname=lvdialog/project_properties.html) dialog box.

##### Related Information

[Creating Tests](../lvutfhowto/utfh_create_tests.html)

[Specifying a Test Priority](../lvutfhowto/utfh_specify_priority.html)

[Executing Tests by Priority](../lvutfhowto/utfh_execute_pri.html)

<!--NI_TOPIC bundle=labview-unit-test-framework-toolkit-api-ref path=lvutfconcepts/utfc_test_require.html language=enus -->
## TOPIC 00019: Requirement IDs (Unit Test Framework Toolkit)

- bundle_id: `labview-unit-test-framework-toolkit-api-ref`
- source_path: `lvutfconcepts/utfc_test_require.html`
- source_url: https://docs-be.ni.com/bundle/labview-unit-test-framework-toolkit-api-ref/raw/resource/enus/lvutfconcepts/utfc_test_require.html
- document_id: `labview-unit-test-framework-toolkit-api-ref`
- page_type: `leaf`
- content_type: ``

### Requirement IDs (Unit Test Framework Toolkit)

Requirement IDs define the traceability relationships between requirements and code. You can integrate the LabVIEW Unit Test Framework Toolkit with NI Requirements Gateway. Requirements Gateway is an application that provides a requirements traceability solution. This application links development and verification documents with formal requirements stored in documents and databases.

When you configure tests and edit test vectors, you can specify requirement IDs for each test and test vector that you want to track with Requirements Gateway. LabVIEW includes the requirement IDs in ATML reports so that you can track tests and test results in Requirements Gateway. If LabVIEW executes a test and the test is passed, LabVIEW reports that the test covers the corresponding requirement. If LabVIEW uses a test vector in a test, LabVIEW reports that the test vector covers the corresponding requirement.

After you execute the tests, Requirements Gateway calculates a coverage ratio for all requirements by using the requirement IDs and other information in the test report. Refer to the NI Requirements Gateway documentation for the detailed calculating method.

You can specify requirement IDs interactively by using the [Configuration](../lvutf/utf_configuration_db.html) page of the [Test Properties](../lvutf/utf_properties_db.html) dialog box. You also can specify requirement IDs by editing .lvtest files.

##### Related Information

[Specifying Requirement IDs](../lvutfhowto/utfh_specify_requirements_ids.html)

[Test Results](../lvutfconcepts/utfc_results.html#test_report)

<!--NI_TOPIC bundle=labview-unit-test-framework-toolkit-api-ref path=lvutfconcepts/utfc_test_vector.html language=enus -->
## TOPIC 00020: Test Vectors and .lvvect Files (Unit Test Framework Toolkit)

- bundle_id: `labview-unit-test-framework-toolkit-api-ref`
- source_path: `lvutfconcepts/utfc_test_vector.html`
- source_url: https://docs-be.ni.com/bundle/labview-unit-test-framework-toolkit-api-ref/raw/resource/enus/lvutfconcepts/utfc_test_vector.html
- document_id: `labview-unit-test-framework-toolkit-api-ref`
- page_type: `leaf`
- content_type: ``

### Test Vectors and .lvvect Files (Unit Test Framework Toolkit)

The LabVIEW Unit Test Framework Toolkit provides test vectors you use to manage multiple input or expected values. A test vector is an array of input or expected values that you can assign to an input or output of the VI under test. You can use test vectors to assign multiple values to an input or output of the VI under test in a test case.

Before you create a test vector, you must create a test vector file in a LabVIEW project. A test vector file is a text file that contains one or multiple test vectors. When you create a test vector file in the [Project Explorer](/csh?topicname=lvdialog/project_explorer_window.html) window, LabVIEW creates a .lvvect file on the disk. A .lvvect icon appears on both the **Items** and **Files** pages.

|  | Note By default, LabVIEW saves the .lvvect file in the same directory as the VI under test. You can specify a different Default location file path on the Unit Test Framework page of the Project Properties dialog box. |
| --- | --- |

The Unit Test Framework Toolkit provides the following two types of test vectors:

- Sequence —This type of test vector lists all the values sequentially. For example, you can create a sequence test vector that contains the following values: (1, 2, 6, 92, 15). The data type of a sequence test vector can be either numeric or non-numeric.
- Linear —This type of test vector uses the following three elements to describe an array of numeric values that have linear relationship.
 
 For example, if you create a linear test vector (1, 2, 4), LabVIEW reads this test vector as an array that contains the following values: (1, 3, 5, 7). You cannot create a linear test vector for non-numeric values, such as strings, Boolean values, or paths.
  - First element—Specifies the start value of the linear test vector.
  - Second element—Specifies the increment step value of the linear test vector.
  - Third element—Specifies the value numbers of the linear test vector.

You can edit test vectors by using the following methods:

- Using the Test Vector Properties - Edit dialog box.
- Using the front panel of a VI.
- Using third-party text editors.

#### Using Test Vector Indexes

In the [Test Cases](../lvutf/utf_test_cases_db.html) page, you can assign test vectors to each input or output of a VI to test this VI with multiple input or expected values in one test case. After you assign test vectors to inputs of the VI under test, LabVIEW generates permutations for the input values. After you assign test vectors to outputs of the VI under test, LabVIEW compares the number of the input permutations and the size of the test vector assigned to the output terminal in the following methods:

- When the number of the input permutations is equal to the size of the test vector assigned to the output terminal, LabVIEW executes the test by comparing the resulting values with the expected values in the test vector.
- When the number of the input permutations is smaller than the size of the test vector assigned to the output terminal, LabVIEW executes the test and the Test Cases page displays a warning icon.
- When the number of the input permutations is larger than the size of the test vector assigned to the output terminal, LabVIEW reports an error and does not execute the test.

You can use test vector indexes to configure the numbers of input value permutations. LabVIEW does not set indexes to test vector by default. If the assigned test vectors have no or different indexes, LabVIEW generates all possible permutations of the input values. For example, you create two sequence test vectors, (3, 4, 5) and (1, 2). You then assign these test vectors to the **x** and **y** controls of the following VI with no or different indexes.

[IMAGE alt='image' src='xy.gif']

When you execute this test, LabVIEW tests this VI for six times with the following **x** and **y** values:

- x=3 y=1
- x=3 y=2
- x=4 y=1
- x=4 y=2
- x=5 y=1
- x=5 y=2

If the assigned test vectors have identical indexes, LabVIEW sends the test vector values to the inputs one by one and stops the test when any test vector reaches the end. For example, you can assign two test vectors, (3, 4, 5) and (1, 2), to the **x** and **y** controls of the previous VI and set the indexes of these test vectors to index 1. When you execute this test, LabVIEW tests this VI for twice with the following **x** and **y** values:

- x=3 y=1
- x=4 y=2

##### Related Information

[Assigning Test Vectors in Test Cases](../lvutfhowto/utfh_vctr_in_test.html)

#### Test Vector File Format

You can view and edit .lvvect files by using Microsoft Excel or a text editor.

|  | Note If you use Microsoft Excel to edit a .lvvect file, you must save the file using Unicode Text (.txt) file format. When you save a .lvvect file, Microsoft Excel modifies formatting that is not compatible with tab-delimited text. For example, if a cell contains a comma, Microsoft Excel uses double quotation marks to enclose the cell contents. This conversion might result in an unexpected error in the .lvvect file. Refer to the Microsoft Excel documentation for more information about formatting that is not compatible with tab-delimited text. |
| --- | --- |

The following table contains information about each component of a .lvvect file, including descriptions, default values, and notes.

| Component | Description | Default Value | Notes |
| --- | --- | --- | --- |
| LabVIEW Unit Test Framework | Header information that LabVIEW uses to identify test vectors that you created by using the Unit Test Framework Toolkit. | N/A | Do not modify. |
| Version | Header information that LabVIEW uses to identify the version of the Unit Test Framework Toolkit the test vector file was created in. | Automatic† | Do not modify. |
| Library | Specifies the path to the LabVIEW class library (.lvclass) or the LabVIEW project library (.lvlib) the test vector file belongs to, if any. | Automatic† | If the .lvvect file is located in the same drive as the library, use the relative path. Otherwise, use the absolute path. |
| Namespace | Specifies the name of the LabVIEW class library (.lvclass) or the LabVIEW project library (.lvlib) that the test vector file belongs to, if any. | Automatic† | N/A |
| Include | Lists the test vector files that this test vector file includes. You can use these test vector files in a test. | Optional | N/A |
| Test Vector | Lists test vectors that belong to this test vector file. If you open this test vector file in Microsoft Excel, each column in this section indicates a test vector. | N/A | Refer to the table below for detailed information about each component of a test vector. |
| Notes: † LabVIEW gathers and displays this information when you create the test vector. |  |  |  |

The following table contains information about each sub-component of a test vector in the **Test Vector** component of a test vector file.

| Row Number | Component | Description | Default Value | Note |
| --- | --- | --- | --- | --- |
| 1 | Name | Specifies the name of a test vector. | <Blank> | N/A |
| 2 | Data Type | Specifies the data type of a test vector. | <Blank> | A test vector supports the following data types: I8, I16, I32, I64, U8, U16, U32, U64, Single Float, Double Float, Extended Float, Single Complex, Double Complex, Extended Complex, Enum U8, Enum U16, Enum U32, Enum U64, Boolean, String, Path. A test vector does not support the Array or Cluster data type but you can assign test vectors to elements of array or cluster controls of the VI under test or the setup VI on the Test Cases page of the Test Properties dialog box. |
| 3 | Append to | Specifies another test vector. LabVIEW adds the values of the specified test vector to the beginning of the current test vector, and moves the original values of the current test vector after these new values. | <Blank> | N/A |
| 4 | Requirement ID | Specifies the requirements ID of this test vector to use this test vector with NI Requirements Gateway. | <Blank> | N/A |
| 5 | Edit Type | Specifies the type of the test vector. | Sequence | N/A |
| 6 | Value Start | Indicates the beginning point of the test vector values. | Value Start | Do not modify. |
| 7 and Greater | Values | Specifies values of this test vector. | <Blank> | Each row between the Value Start row and the Value End row indicates a test vector value. |
| Last | Value End | Specifies the ending point of the test vector values. | Value End | You can insert rows above this row to add new test vector values. |

##### Related Information

[Assigning Test Vectors in Test Cases](../lvutfhowto/utfh_vctr_in_test.html)

[Test Vectors and .lvvect Files](../lvutfconcepts/utfc_test_vector.html)

#### Example of a .lvvect File

The following figure shows an example of a test vector file.

[IMAGE alt='image' src='lvvect_sample.png']

You can add, edit, and remove test vectors by editing this test vector file in Microsoft Excel or a text editor.

<!--NI_TOPIC bundle=labview-unit-test-framework-toolkit-api-ref path=lvutfconcepts/utfc_tests_cases.html language=enus -->
## TOPIC 00021: Test Cases (Unit Test Framework Toolkit)

- bundle_id: `labview-unit-test-framework-toolkit-api-ref`
- source_path: `lvutfconcepts/utfc_tests_cases.html`
- source_url: https://docs-be.ni.com/bundle/labview-unit-test-framework-toolkit-api-ref/raw/resource/enus/lvutfconcepts/utfc_tests_cases.html
- document_id: `labview-unit-test-framework-toolkit-api-ref`
- page_type: `leaf`
- content_type: ``

### Test Cases (Unit Test Framework Toolkit)

A test case contains a set of input values, expected values, and comparison types that LabVIEW uses to check the VI under test for functional correctness. Each .lvtest file contains at least one test case. When you execute a test, LabVIEW runs the VI under test by using the input values you specified for each test case in the .lvtest file. LabVIEW then compares the resulting values with the expected values by using the comparison types you specified.

The LabVIEW Unit Test Framework Toolkit provides the following ways to configure test cases.

- You can configure test cases interactively by using the Test Cases page of the Test Properties dialog box. For each test case, enter the input values, expected values, and comparison types for each control and indicator of the VI under test.
 [IMAGE alt='image' src='note.gif']
**Note** LabVIEW lists the controls and indicators from the VI under test on the [Test Cases](../lvutf/utf_test_cases_db.html) page. If the **Input/output values** setting on the [Unit Test Framework](../lvutf/utf_proj_prop_db.html) page of the [Project Properties](/csh?topicname=lvdialog/project_properties.html) dialog box is **Include controls and indicators from connector pane**, make sure you select a connector pane pattern and assign the terminals for the VI under test.
- You also can configure test cases interactively by exchanging values between the VI under test and the Test Cases page. This method allows you to configure the input and expected values by using the front panel and then importing the values to the Test Cases page. You also can export values from a test case to the VI under test.
- You can configure test cases by editing .lvtest files.

The following figure shows an example of entering the input values, expected values, and comparison types for a test case.

[IMAGE alt='image' src='test_case.png']

In the previous figure, the input values are 8 and 10, the expected value is 100, and the comparison type is <. When you execute this test, LabVIEW uses 8 and 10 as input values for the VI under test and compares the resulting value with 100. If the resulting value is not less than 100, test results show this test as failed.

LabVIEW displays the following data types as binary data or flattened data.

- Picture
- Array
- Variant
- Digital waveform
- Dynamic data
- Refnum
- External data
- LabVIEW class instance

LabVIEW represents these data types by using [...] on the [Test Cases](../lvutf/utf_test_cases_db.html) page. You cannot edit these data types on the **Test Cases** page. However, you can configure the input and expected values of these data types by using the front panel of the VI under test, accessible by clicking the **Export Values to VI** button, and importing the updated values from the VI under test to the current test case.

You also can configure the input and expected values of these data types by using setup and teardown VIs. When you configure a test to run setup and teardown VIs, LabVIEW lists the controls and indicators of the setup and teardown VIs on the [Test Cases](../lvutf/utf_test_cases_db.html) page. You can configure the inputs of the setup VI before passing the data to the VI under test. Likewise, you can configure the outputs and comparison types of the teardown VI after accepting the outputs of the VI under test.

The following figure shows an example of configuring the input and expected values of setup and teardown VIs.

[IMAGE alt='image' src='test_case2.png']

In the previous figure, the VI under test contains a LabVIEW class data type input, whose value assembles in the setup VI. The **String** input in the setup VI is a data member of that LabVIEW class. By setting the input value of the setup VI, you know the input value of the data member of the LabVIEW class. Likewise, the VI under test contains a LabVIEW class data type output, whose value disassembles in the teardown VI. By setting the expected value and comparison type of the teardown VI, you can compare the resulting value of the data member of the LabVIEW class.

Refer to the labview\examples\Unit Test Framework\LabVIEW Class\LV Class.lvproj for an example that demonstrates how to test VIs that use LabVIEW classes.

##### Related Information

[Assigning Terminals to Controls and Indicators](/csh?topicname=lvhowto/assigning_controls_and_ind.html)

[Exchanging Values Between the VI under Test, Setup VI, Teardown VI, and the Test Cases Page](../lvutfhowto/utfh_exchange_values.html)

[Flattened Data](/csh?topicname=lvconcepts/flattened_data.html)

[Selecting a Connector Pane Pattern](/csh?topicname=lvhowto/selecting_a_connector_pane.html)

[Setup and Teardown VIs](../lvutfconcepts/utfc_set_tear.html)

<!--NI_TOPIC bundle=labview-unit-test-framework-toolkit-api-ref path=lvutfconcepts/utfconcepts.html language=enus -->
## TOPIC 00022: Unit Test Framework Toolkit

- bundle_id: `labview-unit-test-framework-toolkit-api-ref`
- source_path: `lvutfconcepts/utfconcepts.html`
- source_url: https://docs-be.ni.com/bundle/labview-unit-test-framework-toolkit-api-ref/raw/resource/enus/lvutfconcepts/utfconcepts.html
- document_id: `labview-unit-test-framework-toolkit-api-ref`
- page_type: `leaf`
- content_type: ``

### Unit Test Framework Toolkit

June 2013, 372584F-01

The LabVIEW Unit Test Framework Toolkit provides tools you use to check VIs for functional correctness. Use the [Project Explorer](/csh?topicname=lvdialog/project_explorer_window.html) window to create, configure, manage, and execute tests interactively in a LabVIEW project. You also can execute tests programmatically by using the [Unit Test Framework](../lvutf/utf_vis.html) VIs.

For more information about this help file, refer to the following topics:

[Related Documentation](../lvutfconcepts/utfc_related_doc.html)

[Glossary](../lvutfconcepts/utfc_glossary.html)

|  | To view related topics, click the Locate button, shown at left, in the toolbar at the top of this window. The LabVIEW Help highlights this topic in the Contents tab so you can navigate the related topics. |
| --- | --- |

© 2008–2013 National Instruments. All rights reserved.

<!--NI_TOPIC bundle=labview-unit-test-framework-toolkit-api-ref path=lvutfhowto/utfh_add_duplicate_test_case.html language=enus -->
## TOPIC 00023: Adding or Duplicating Test Cases (Unit Test Framework Toolkit)

- bundle_id: `labview-unit-test-framework-toolkit-api-ref`
- source_path: `lvutfhowto/utfh_add_duplicate_test_case.html`
- source_url: https://docs-be.ni.com/bundle/labview-unit-test-framework-toolkit-api-ref/raw/resource/enus/lvutfhowto/utfh_add_duplicate_test_case.html
- document_id: `labview-unit-test-framework-toolkit-api-ref`
- page_type: `leaf`
- content_type: ``

### Adding or Duplicating Test Cases (Unit Test Framework Toolkit)

Use the 
 [Project Explorer](/csh?topicname=lvdialog/project_explorer_window.html) window to add or duplicate test cases interactively. You also can add or delete test cases by editing .lvtest files..

Complete the following steps to add or duplicate a test case.

1. Open the LabVIEW project that contains the files on which you want to perform unit testing.
2. Add a test case to a test in one of the following ways:
  - Right-click the VI for which you want to add a new test case and select Unit Tests»New Test Case»*testname*.lvtest from the shortcut menu, where testname is the name of the .lvtest file to which you want to add a test case. The Test Cases page of the 
 Test Properties dialog box appears, displaying the new test case.
 [IMAGE alt='image' src='note.gif']
**Note** A .lvtest test file must already exist in the project for this VI.
  - Double-click the .lvtest file to which you want to add a new test case to display the Test Properties dialog box. On the Test Cases page, click the New button to add a new test case.
  - Double-click the .lvtest file to which you want to add a new test case to display the Test Properties dialog box. On the Test Cases page, click the Duplicate button to duplicate the current test case.
 [IMAGE alt='image' src='note.gif']
**Note** When you add or duplicate a test case, LabVIEW adds the new test case to the end of the test case list and displays the new test case.
3. Configure the new test case.
4. Select File»Save to save the project.

<!--NI_TOPIC bundle=labview-unit-test-framework-toolkit-api-ref path=lvutfhowto/utfh_config_adv.html language=enus -->
## TOPIC 00024: Configuring Advanced Settings of Tests (Unit Test Framework Toolkit)

- bundle_id: `labview-unit-test-framework-toolkit-api-ref`
- source_path: `lvutfhowto/utfh_config_adv.html`
- source_url: https://docs-be.ni.com/bundle/labview-unit-test-framework-toolkit-api-ref/raw/resource/enus/lvutfhowto/utfh_config_adv.html
- document_id: `labview-unit-test-framework-toolkit-api-ref`
- page_type: `leaf`
- content_type: ``

### Configuring Advanced Settings of Tests (Unit Test Framework Toolkit)

Use the [Advanced](../lvutf/utf_advanced_db.html) page of the 
 [Test Properties](../lvutf/utf_properties_db.html) dialog box to configure advanced settings of tests.

|  | Note The settings on this page apply to only the .lvtest file you are configuring and override the global settings specified on the Unit Test Framework page of the Project Properties dialog box. |
| --- | --- |

- Specifying a Timeout for a Test
- Specifying a Minimum Code Coverage Requirement
- Specifying the Number of Times to Repeat a Test
- Specifying the Digits of Precision for Floating-Point Comparison
- Configuring the Input/Output Setting of the VI under Test

<!--NI_TOPIC bundle=labview-unit-test-framework-toolkit-api-ref path=lvutfhowto/utfh_config_lvtest.html language=enus -->
## TOPIC 00025: Editing .lvtest Files (Unit Test Framework Toolkit)

- bundle_id: `labview-unit-test-framework-toolkit-api-ref`
- source_path: `lvutfhowto/utfh_config_lvtest.html`
- source_url: https://docs-be.ni.com/bundle/labview-unit-test-framework-toolkit-api-ref/raw/resource/enus/lvutfhowto/utfh_config_lvtest.html
- document_id: `labview-unit-test-framework-toolkit-api-ref`
- page_type: `leaf`
- content_type: ``

### Editing .lvtest Files (Unit Test Framework Toolkit)

When you create a test from the 
 [Project Explorer](/csh?topicname=lvdialog/project_explorer_window.html) window, LabVIEW creates a 
 .lvtest file
 on disk. Each .lvtest file contains the settings LabVIEW uses to check the VI under test for functional correctness. You can view or edit .lvtest files by using Microsoft Excel or a text editor.

|  | Note If you use Microsoft Excel to edit a .lvtest file, you must save the file using the Unicode Text (.txt) file format. When you save a .lvtest file, Microsoft Excel modifies formatting that is not compatible with tab-delimited text. For example, if a cell contains a comma, Microsoft Excel uses double quotation marks to enclose the cell contents. This conversion might result in an unexpected error in the .lvtest file. Refer to the Microsoft Excel documentation for more information about formatting that is not compatible with tab-delimited text. |
| --- | --- |

Complete the following steps to edit a .lvtest file by using Microsoft Excel.

|  | Note The default editor is Microsoft Excel. You can change the default editor LabVIEW uses to edit .lvtest files on the Unit Test Framework page of the Project Properties dialog box. |
| --- | --- |

1. Open the LabVIEW project that contains the files on which you want to perform unit testing.
2. Right-click a .lvtest file and select Open in External Editor . You also can open .lvtest files directly from Windows Explorer by right-clicking a .lvtest file and opening the file with Microsoft Excel.
 [IMAGE alt='image' src='note.gif']
**Note** If you double-click a .lvtest file from Windows Explorer, LabVIEW launches but does not open any project or dialog box. You must right-click the .lvtest file to open the file with Microsoft Excel.
3. Edit the .lvtest file to configure settings for this test. Make sure you follow the .lvtest file format.
 [IMAGE alt='image' src='caution.gif']
**Caution** Do not remove any lines from the .lvtest file. If you remove anything, the test might not execute properly.
4. Save and close the .lvtest file.
5. Select File»Save to save the project.

##### Related Information

[Creating Tests](../lvutfhowto/utfh_create_tests.html)

[Tests and .lvtest Files](../lvutfconcepts/utfc_test_config.html)

<!--NI_TOPIC bundle=labview-unit-test-framework-toolkit-api-ref path=lvutfhowto/utfh_config_set_tear.html language=enus -->
## TOPIC 00026: Configuring Tests to Run Setup and Teardown VIs (Unit Test Framework Toolkit)

- bundle_id: `labview-unit-test-framework-toolkit-api-ref`
- source_path: `lvutfhowto/utfh_config_set_tear.html`
- source_url: https://docs-be.ni.com/bundle/labview-unit-test-framework-toolkit-api-ref/raw/resource/enus/lvutfhowto/utfh_config_set_tear.html
- document_id: `labview-unit-test-framework-toolkit-api-ref`
- page_type: `leaf`
- content_type: ``

### Configuring Tests to Run Setup and Teardown VIs (Unit Test Framework Toolkit)

Use the [Setup/Teardown](../lvutf/utf_set_tear_db.html) page of the 
 [Test Properties](../lvutf/utf_properties_db.html) dialog box to configure tests to run [setup and teardown VIs](../lvutfconcepts/utfc_set_tear.html). You also can configure tests to run setup and teardown VIs by editing .lvtest files..

Complete the following steps to configure a test to run setup and teardown VIs.

1. Open the LabVIEW project that contains the files on which you want to perform unit testing.
2. Double-click a .lvtest file to display the Test Properties dialog box.
3. Select Setup/Teardown from the Category list to display the Setup/Teardown page.
4. Click the Browse button next to the Setup VI text box. A file dialog box appears.
5. Navigate to and select the VI you want to use as the setup VI. Click the OK button.
6. Select an output terminal from the Outputs of Setup VI column for each Inputs of VI under Test you want to pass values to.
7. Click the Browse button next to the Teardown VI text box. A file dialog box appears.
8. Navigate to and select the VI you want to use as the teardown VI. Click the OK button.
9. Select an input terminal from the Inputs of Teardown VI column for each Outputs of VI under Test you want to retrieve values from.
10. Enter the input values, expected values, and comparison types of the setup and teardown VIs for a test case.
11. Click the OK button to close the dialog box and return to the Project Explorer window.
12. Select File»Save to save the project.

The next time you execute this test, LabVIEW first runs the setup VI by using the input values and then passes the output values from the setup VI to the inputs of the VI under test. LabVIEW then checks the VI under test for functional correctness and passes the resulting values from the VI under test to the inputs of the teardown VI. LabVIEW compares the outputs of the teardown VI with the expected values.

Refer to the labview\examples\Unit Test Framework\Setup Teardown\Setup Teardown.lvproj for an example that demonstrates how to use setup and teardown VIs.

##### Related Information

[Entering Input Values, Expected Values, and Comparison Types](../lvutfhowto/utfh_enter_value.html)

<!--NI_TOPIC bundle=labview-unit-test-framework-toolkit-api-ref path=lvutfhowto/utfh_configure.html language=enus -->
## TOPIC 00027: Configuring Tests (Unit Test Framework Toolkit)

- bundle_id: `labview-unit-test-framework-toolkit-api-ref`
- source_path: `lvutfhowto/utfh_configure.html`
- source_url: https://docs-be.ni.com/bundle/labview-unit-test-framework-toolkit-api-ref/raw/resource/enus/lvutfhowto/utfh_configure.html
- document_id: `labview-unit-test-framework-toolkit-api-ref`
- page_type: `leaf`
- content_type: ``

### Configuring Tests (Unit Test Framework Toolkit)

Use the 
 [Project Explorer](/csh?topicname=lvdialog/project_explorer_window.html) window to configure tests interactively. You also can configure tests by editing .lvtest files.

Use this book to learn step-by-step instructions for configuring tests and test cases in a LabVIEW project.

##### Related Information

[Tests and .lvtest Files](../lvutfconcepts/utfc_test_config.html)

[Editing .lvtest Files](../lvutfhowto/utfh_config_lvtest.html)

<!--NI_TOPIC bundle=labview-unit-test-framework-toolkit-api-ref path=lvutfhowto/utfh_configure_input_output.html language=enus -->
## TOPIC 00028: Configuring the Input/Output Setting of the VI under Test (Unit Test Framework Toolkit)

- bundle_id: `labview-unit-test-framework-toolkit-api-ref`
- source_path: `lvutfhowto/utfh_configure_input_output.html`
- source_url: https://docs-be.ni.com/bundle/labview-unit-test-framework-toolkit-api-ref/raw/resource/enus/lvutfhowto/utfh_configure_input_output.html
- document_id: `labview-unit-test-framework-toolkit-api-ref`
- page_type: `leaf`
- content_type: ``

### Configuring the Input/Output Setting of the VI under Test (Unit Test Framework Toolkit)

Complete the following steps to configure which controls and indicators of the VI under test appear on the .

1. Open the LabVIEW project that contains the files on which you want to perform unit testing.
2. Double-click a .lvtest file to display the Test Properties dialog box.
3. Select Advanced from the Category list to display the Advanced page.
4. Click the Input/output values list and select which controls and indicators of the VI under test appear on the Test Cases page.
 [IMAGE alt='image' src='note.gif']
**Note** If you select the **Include controls and indicators from connector pane** setting, make sure you select a connector pane pattern and assign terminals for the VI under test.
5. Click the OK button to close the dialog box and return to the Project Explorer window.
6. Select File»Save to save the project.

##### Related Information

[Assigning Terminals to Controls and Indicators](/csh?topicname=lvhowto/assigning_controls_and_ind.html)

[Selecting a Connector Pane Pattern](/csh?topicname=lvhowto/selecting_a_connector_pane.html)

<!--NI_TOPIC bundle=labview-unit-test-framework-toolkit-api-ref path=lvutfhowto/utfh_configure_test_skip.html language=enus -->
## TOPIC 00029: Configuring a Test to Skip (Unit Test Framework Toolkit)

- bundle_id: `labview-unit-test-framework-toolkit-api-ref`
- source_path: `lvutfhowto/utfh_configure_test_skip.html`
- source_url: https://docs-be.ni.com/bundle/labview-unit-test-framework-toolkit-api-ref/raw/resource/enus/lvutfhowto/utfh_configure_test_skip.html
- document_id: `labview-unit-test-framework-toolkit-api-ref`
- page_type: `leaf`
- content_type: ``

### Configuring a Test to Skip (Unit Test Framework Toolkit)

Complete the following steps to configure a test to skip during test execution.

1. Open the LabVIEW project that contains the files on which you want to perform unit testing.
2. Double-click a .lvtest file to display the Test Properties dialog box.
3. On the Configuration page, place a checkmark in the Always skip this test checkbox. The Project Explorer window and the Unit Test Framework VIs checkboxes appear and contain checkmarks by default.
4. (Optional) If you want to skip this test only when executing tests interactively from the Project Explorer window, remove the checkmark from the Unit Test Framework VIs checkbox.
5. (Optional) If you want to skip this test only when executing tests programmatically with the Unit Test Framework VIs, remove the checkmark from the Project Explorer window checkbox.
6. Click the OK button to close the dialog box and return to the Project Explorer window.
7. Select File»Save to save the project.

The next time you execute tests, LabVIEW skips this test.

##### Related Information

[Executing Tests Interactively](../lvutfhowto/utfh_execute_test.html)

[Executing Tests Programmatically](../lvutfhowto/utfh_execute_vi.html)

<!--NI_TOPIC bundle=labview-unit-test-framework-toolkit-api-ref path=lvutfhowto/utfh_configure_ud_test_vi.html language=enus -->
## TOPIC 00030: Configuring a Test to Use a User-Defined Test VI (Unit Test Framework Toolkit)

- bundle_id: `labview-unit-test-framework-toolkit-api-ref`
- source_path: `lvutfhowto/utfh_configure_ud_test_vi.html`
- source_url: https://docs-be.ni.com/bundle/labview-unit-test-framework-toolkit-api-ref/raw/resource/enus/lvutfhowto/utfh_configure_ud_test_vi.html
- document_id: `labview-unit-test-framework-toolkit-api-ref`
- page_type: `leaf`
- content_type: ``

### Configuring a Test to Use a User-Defined Test VI (Unit Test Framework Toolkit)

Complete the following steps to configure a test to use a user-defined test VI.

1. Open the LabVIEW project that contains the files on which you want to perform unit testing.
2. Double-click a .lvtest file to display the Test Properties dialog box.
3. On the Configuration page, place a checkmark in the Use user-defined test VI checkbox.
 [IMAGE alt='image' src='note.gif']
**Note** When you place a checkmark in the **Use user-defined test VI** checkbox, LabVIEW dims the [Test Cases](../lvutf/utf_test_cases_db.html) page and the [Setup/Teardown](../lvutf/utf_set_tear_db.html) page in the [Test Properties](../lvutf/utf_properties_db.html) dialog box.
4. Click the Browse button next to the Use user-defined test VI file path text box. A file dialog box appears.
5. Navigate to and select the user-defined test VI you want to use. Click the OK button.
6. Click the OK button to close the dialog box and return to the Project Explorer window.
7. Select File»Save to save the project.

##### Related Information

[Creating a User-Defined Test VI](../lvutfhowto/utfh_create_ud_test.html)

<!--NI_TOPIC bundle=labview-unit-test-framework-toolkit-api-ref path=lvutfhowto/utfh_create.html language=enus -->
## TOPIC 00031: Creating Projects and Tests (Unit Test Framework Toolkit)

- bundle_id: `labview-unit-test-framework-toolkit-api-ref`
- source_path: `lvutfhowto/utfh_create.html`
- source_url: https://docs-be.ni.com/bundle/labview-unit-test-framework-toolkit-api-ref/raw/resource/enus/lvutfhowto/utfh_create.html
- document_id: `labview-unit-test-framework-toolkit-api-ref`
- page_type: `leaf`
- content_type: ``

### Creating Projects and Tests (Unit Test Framework Toolkit)

Use this book to learn step-by-step instructions for creating tests in a LabVIEW project.

|  | Note You must create and save a LabVIEW project before you can use the LabVIEW Unit Test Framework Toolkit to create tests. Use projects to group together all the files you need to perform unit testing. |
| --- | --- |

##### Related Information

[Managing a Project in LabVIEW](/csh?topicname=lvhowto/creating_lv_projects.html)

[Tests and .lvtest Files](../lvutfconcepts/utfc_test_config.html)

<!--NI_TOPIC bundle=labview-unit-test-framework-toolkit-api-ref path=lvutfhowto/utfh_create_comp.html language=enus -->
## TOPIC 00032: Creating a User-Defined Comparison VI (Unit Test Framework Toolkit)

- bundle_id: `labview-unit-test-framework-toolkit-api-ref`
- source_path: `lvutfhowto/utfh_create_comp.html`
- source_url: https://docs-be.ni.com/bundle/labview-unit-test-framework-toolkit-api-ref/raw/resource/enus/lvutfhowto/utfh_create_comp.html
- document_id: `labview-unit-test-framework-toolkit-api-ref`
- page_type: `leaf`
- content_type: ``

### Creating a User-Defined Comparison VI (Unit Test Framework Toolkit)

Complete the following steps to create a user-defined comparison VI.

1. Select File»New VI to create a new, blank VI.
2. On the Controls palette, select Modern»Variant & Class to display the Variant & Class palette.
3. Add a variant to the front panel and label the variant Resulting Value .
4. Right-click the variant and select Change to Control from the shortcut menu.
5. Add another variant to the front panel and label the variant Expected Value .
6. Right-click the Expected Value variant and select Change to Control from the shortcut menu.
7. On the Controls palette, select Modern»Boolean to display the Boolean palette.
8. Add a Round LED or Square LED Boolean indicator to the front panel and label the Boolean indicator Comparison Result .
9. Right-click the connector pane and select Patterns from the shortcut menu. Select the following connector pane pattern.
 [IMAGE alt='image' src='cpane.gif']
10. Assign each of the following connector pane terminals to a front panel control or indicator.
 
 [IMAGE alt='image' src='note.gif']
**Note** You must configure the connector pane properly in order for the user-defined comparison VI to work properly.
  1. Top left terminal to the Resulting Value variant control.
  2. Bottom left terminal to the Expected Value variant control.
  3. Right terminal to the Comparison Result Boolean indicator.
11. Display the block diagram by selecting Window»Show Block Diagram .
12. Add or define your own comparison to the block diagram.
13. Wire the Resulting Value and Expected Value variant controls to the comparison.
14. Wire the result of the comparison to the Comparison Result Boolean indicator.
 [IMAGE alt='image' src='note.gif']
**Note** The comparison must return a Boolean data type.
15. Select File»Save As to save this user-defined comparison VI in an easily accessible location.

Refer to the labview\examples\Unit Test Framework\User-Defined Comparison\User-Defined Comparison.lvproj for an example that demonstrates how to use user-defined comparison VIs in the Unit Test Framework Toolkit.

##### Related Information

[Assigning Terminals to Controls and Indicators](/csh?topicname=lvhowto/assigning_controls_and_ind.html)

[Variant Data](/csh?topicname=lvhowto/variants.html)

<!--NI_TOPIC bundle=labview-unit-test-framework-toolkit-api-ref path=lvutfhowto/utfh_create_tests.html language=enus -->
## TOPIC 00033: Creating Tests (Unit Test Framework Toolkit)

- bundle_id: `labview-unit-test-framework-toolkit-api-ref`
- source_path: `lvutfhowto/utfh_create_tests.html`
- source_url: https://docs-be.ni.com/bundle/labview-unit-test-framework-toolkit-api-ref/raw/resource/enus/lvutfhowto/utfh_create_tests.html
- document_id: `labview-unit-test-framework-toolkit-api-ref`
- page_type: `leaf`
- content_type: ``

### Creating Tests (Unit Test Framework Toolkit)

Use the 
 [Project Explorer](/csh?topicname=lvdialog/project_explorer_window.html) window to create tests interactively. You can create tests from VIs, existing .lvtest files, or user-defined test VIs.

|  | Note You must create and save a LabVIEW project before you can use the LabVIEW Unit Test Framework Toolkit to create tests. Use projects to group together all the files you need to perform unit testing. |
| --- | --- |

When you create a test from the [Project Explorer](/csh?topicname=lvdialog/project_explorer_window.html), LabVIEW creates a .lvtest file on disk. A .lvtest icon appears on both the **Items** and **Files** pages. Each .lvtest file contains the settings LabVIEW uses to check the VI under test for functional correctness.

|  | Note By default, LabVIEW saves .lvtest files in the same directory as the VIs under test. You can specify a different Default location file path on the Unit Test Framework page of the Project Properties dialog box. |
| --- | --- |

##### Related Information

[Tests and .lvtest Files](../lvutfconcepts/utfc_test_config.html)

[Creating a User-Defined Test VI](../lvutfhowto/utfh_create_ud_test.html)

#### Creating a Test from a VI

Complete the following steps to create a test from a VI.

1. Open the LabVIEW project that contains the files on which you want to perform unit testing.
2. Right-click a VI and select Unit Tests»New Test from the shortcut menu.
 [IMAGE alt='image' src='note.gif']
**Note** You also can create tests from multiple VIs by pressing the <Ctrl> key while clicking each VI. Then right-click the selection and select **New Unit Tests** from the shortcut menu. LabVIEW creates a .lvtest file for each VI.
3. Configure the .lvtest file you just created.
4. Select File»Save to save the project.

##### Related Information

[Configuring Tests](../lvutfhowto/utfh_configure.html)

#### Creating a Test from a .lvtest File

Complete the following steps to create a test from a .lvtest file on disk.

1. Open the LabVIEW project that contains the files on which you want to perform unit testing.
2. Right-click a VI and select Unit Tests»Add Test from File from the shortcut menu. A file dialog box appears.
3. Navigate to and select the .lvtest file you want to use. Click the OK button. LabVIEW adds the .lvtest file to the project tree.
 [IMAGE alt='image' src='note.gif']
**Note** If the .lvtest file was associated with a different VI previously, the .lvtest file now is associated with the new VI. You can specify only one VI under test for each .lvtest file.
4. Select File»Save to save the project.

#### Creating a Test from a User-Defined Test VI

Complete the following steps to create a test from a user-defined test VI.

1. Open the LabVIEW project that contains the files on which you want to perform unit testing.
2. Right-click a VI and select Unit Tests»New User-Defined Test from the shortcut menu. A Save dialog box appears. 
 LabVIEW automatically creates a user-defined test VI from the User-Defined Test Template.vit file located in the
 labview\templates\UnitTestFramework directory. You also can find the template file by selecting File»New to display the New dialog box and selecting VI»From Template»Unit Test Framework .
3. Enter a filename for the user-defined test VI.
4. Click the OK button to save the user-defined test VI. 
 LabVIEW automatically creates a test and configures the test to use the user-defined test VI. LabVIEW saves the .lvtest file in the same location as the user-defined test VI.
5. Select File»Save to save the project.
6. Modify the user-defined test VI to define your own test.

##### Related Information

[Creating a User-Defined Test VI](../lvutfhowto/utfh_create_ud_test.html)

<!--NI_TOPIC bundle=labview-unit-test-framework-toolkit-api-ref path=lvutfhowto/utfh_create_ud_test.html language=enus -->
## TOPIC 00034: Creating a User-Defined Test VI (Unit Test Framework Toolkit)

- bundle_id: `labview-unit-test-framework-toolkit-api-ref`
- source_path: `lvutfhowto/utfh_create_ud_test.html`
- source_url: https://docs-be.ni.com/bundle/labview-unit-test-framework-toolkit-api-ref/raw/resource/enus/lvutfhowto/utfh_create_ud_test.html
- document_id: `labview-unit-test-framework-toolkit-api-ref`
- page_type: `leaf`
- content_type: ``

### Creating a User-Defined Test VI (Unit Test Framework Toolkit)

Complete the following steps to create a user-defined test VI.

1. Create a user-defined test VI from the User-Defined Test Template.vit file in one of the following ways:
  - Select File»New to display the New dialog box and select VI»From Template»Unit Test Framework to open the User-Defined Test Template.vit file. You also can locate this file in the labview\templates\UnitTestFramework directory.
  - Create a test from a user-defined test VI. The test and user-defined test VI appear in the Project Explorer window. Right-click the user-defined test VI and select Open .
2. Modify the VI to define your own test. Keep in mind the following requirements for the user-defined test VI:
  - Do not modify the Unit Test Framework Result indicator name or cluster elements.
  - The Unit Test Framework Result indicator contains the following three cluster elements:
 Element Name
Data Type
Notes
Required
**time elapsed [ms]**
Numeric indicator
Time in milliseconds.
No
**result (test)**
Enum
Enum values must be Passed, Failed, Error, Skipped, and Not Processed.
Yes
**result (parameters)**
Array of cluster
Each array is a cluster of comparison results between the expected and resulting values.
No
**Note:** You must include data from this element in the **Unit Test Framework Result** indicator.
  - The Unit Test Framework Result indicator must be connected to the connector pane.
3. Wire the result of your test to the result (test) element.
4. (Optional) For advanced test VIs, wire the results of your tests to the time elapsed [ms] and results (parameters) elements.
5. Select File»Save As to save this user-defined test VI in an easily accessible location.
 [IMAGE alt='image' src='note.gif']
**Note** If you rename a user-defined test VI that you create from the shortcut menu, you must specify the new **User-defined test VI file path** on the [Configuration](../lvutf/utf_configuration_db.html) page of the [Test Properties](../lvutf/utf_properties_db.html) dialog box.

Refer to the labview\examples\Unit Test Framework\User-Defined Test\User-Defined Test.lvproj for an example that demonstrates how to use the Unit Test Framework Toolkit to create user-defined test VIs.

##### Related Information

[Creating a Test from a User-Defined Test VI](../lvutfhowto/utfh_create_tests.html#user_test)

<!--NI_TOPIC bundle=labview-unit-test-framework-toolkit-api-ref path=lvutfhowto/utfh_delete_test_case.html language=enus -->
## TOPIC 00035: Deleting Test Cases (Unit Test Framework)

- bundle_id: `labview-unit-test-framework-toolkit-api-ref`
- source_path: `lvutfhowto/utfh_delete_test_case.html`
- source_url: https://docs-be.ni.com/bundle/labview-unit-test-framework-toolkit-api-ref/raw/resource/enus/lvutfhowto/utfh_delete_test_case.html
- document_id: `labview-unit-test-framework-toolkit-api-ref`
- page_type: `leaf`
- content_type: ``

### Deleting Test Cases (Unit Test Framework)

Complete the following steps to delete a test case.

1. Open the LabVIEW project that contains the files on which you want to perform unit testing.
2. Double-click a .lvtest file to display the Test Properties dialog box.
3. Select Test Cases from the Category list to display the Test Cases page.
4. If this test has more than one test case, use the Test Case control to select the test case you want to delete.
5. Click the Delete button to delete this test case.
 [IMAGE alt='image' src='note.gif']
**Note** If this test has only one test case, LabVIEW resets the input and expected values to 0 and the comparison types to =.
6. Select File»Save to save the project.

<!--NI_TOPIC bundle=labview-unit-test-framework-toolkit-api-ref path=lvutfhowto/utfh_edit_vectors.html language=enus -->
## TOPIC 00036: Editing Test Vectors (Unit Test Framework Toolkit)

- bundle_id: `labview-unit-test-framework-toolkit-api-ref`
- source_path: `lvutfhowto/utfh_edit_vectors.html`
- source_url: https://docs-be.ni.com/bundle/labview-unit-test-framework-toolkit-api-ref/raw/resource/enus/lvutfhowto/utfh_edit_vectors.html
- document_id: `labview-unit-test-framework-toolkit-api-ref`
- page_type: `leaf`
- content_type: ``

### Editing Test Vectors (Unit Test Framework Toolkit)

Complete the following steps to edit test vectors:

1. Double-click a .lvvect file in the Project Explorer window to display the Test Vector File Properties dialog box.
2. Click the Edit Values button to display the Test Vector Properties - Edit dialog box.
3. (Optional) Specify a name in the Name cell of a test vector if you want to rename this test vector.
4. (Optional) Specify a test vector in the Append to cell if you want to append the values of a test vector to values of another test vector.
5. (Optional) Specify a requirement ID in the Requirement ID cell if you want to use a test vector with NI Requirements Gateway. Ensure the requirement IDs match the corresponding requirements in Requirements Gateway.
6. Specify a test vector type in the Edit Type cell of the test vector that you want to edit. The default is sequence .
7. Specify test vector values in the Value cell of the test vector that you want to edit. If you want to add multiple values to this test vector, you can enter the new values in the cells below the Value cell.
 [IMAGE alt='image' src='note.gif']
**Note** You can export the test vector to an array control of a VI, edit the values in the array control, and import the updated values to the test vector. The array control must have a proper data type.
8. (Optional) Repeat step 3 through 7 to edit multiple test vectors.
9. Click the OK button to close this dialog box and save the test vectors.

##### Related Information

[Exporting and Importing Test Vectors](utfh_expt_impt_vctr.html)

[Exporting Values from a Test Vector to an Array Control](utfh_expt_impt_vctr.html#export)

[Importing Values from an Array Control to a Test Vector](utfh_expt_impt_vctr.html#import)

[Requirement IDs](../lvutfconcepts/utfc_test_require.html)

[Test Vectors and .lvvect Files](../lvutfconcepts/utfc_test_vector.html)

<!--NI_TOPIC bundle=labview-unit-test-framework-toolkit-api-ref path=lvutfhowto/utfh_enter_value.html language=enus -->
## TOPIC 00037: Entering Input Values, Expected Values, and Comparison Types (Unit Test Framework Toolkit)

- bundle_id: `labview-unit-test-framework-toolkit-api-ref`
- source_path: `lvutfhowto/utfh_enter_value.html`
- source_url: https://docs-be.ni.com/bundle/labview-unit-test-framework-toolkit-api-ref/raw/resource/enus/lvutfhowto/utfh_enter_value.html
- document_id: `labview-unit-test-framework-toolkit-api-ref`
- page_type: `leaf`
- content_type: ``

### Entering Input Values, Expected Values, and Comparison Types (Unit Test Framework Toolkit)

Complete the following steps to enter the input values, expected values, and comparison types for a test case.

|  | Note LabVIEW lists the controls and indicators from the VI under test on the Test Cases page. If the Input/output values setting on the Unit Test Framework page of the Project Properties dialog box is Include controls and indicators from connector pane, make sure you select a connector pane pattern and assign the terminals for the VI under test. |
| --- | --- |

|  | Tip You can resize the Test Properties dialog box and table columns to fit the input and output data in the table. |
| --- | --- |

1. Open the LabVIEW project that contains the files on which you want to perform unit testing.
2. Double-click a .lvtest file to display the Test Properties dialog box.
3. Select Test Cases from the Category list to display the Test Cases page.
4. If this test has more than one test case, use the Test Case control to select the test case you want to configure.
5. Click the Input Value text box of the input terminal you want to configure and enter a value. Press the <Tab> key to move to the value in the next cell and press <Shift-Tab> to switch to the value in the previous cell.
 [IMAGE alt='image' src='tip.gif']
**Tip** You also can exchange values between the VI under test, setup VI, teardown VI, and the [Test Cases](../lvutf/utf_test_cases_db.html) page, accessible by clicking the **Export Values to VI** button or the **Import Values from VI** button.
6. Click the Expected Value text box of the output terminal you want to configure and enter a value. Repeat this step for other output terminals.
7. Select a comparison type from the Comparison list of the output terminal you want to configure. Repeat this step for other output terminals.
 [IMAGE alt='image' src='note.gif']
**Note** LabVIEW lists the available comparison types that each data type supports. You also can use a user-defined comparison VI by selecting **user-defined** from the **Comparison** list and selecting a user-defined comparison VI.
8. (Optional) Remove the checkmark from each input or output terminal that you do not want to test during execution.
 [IMAGE alt='image' src='tip.gif']
**Tip** You can select multiple entries by pressing the <Ctrl> key while clicking each entry. Then right-click the selection and select **Uncheck All Items** or **Check All Items**.
9. (Optional) Click the Run button to test the single test case.
10. Click the OK button to close the dialog box and return to the Project Explorer window.
11. Select File»Save to save the project.

##### Related Information

[Assigning Terminals to Controls and Indicators](/csh?topicname=lvhowto/assigning_controls_and_ind.html)

[Block Diagram Terminals](/csh?topicname=lvconcepts/block_diagram_objects.html)

[Creating a User-Defined Comparison VI](../lvutfhowto/utfh_create_comp.html)

[Exchanging Values Between the VI under Test, Setup VI, Teardown VI, and the Test Cases Page](../lvutfhowto/utfh_exchange_values.html)

[Selecting a Connector Pane Pattern](/csh?topicname=lvhowto/selecting_a_connector_pane.html)

<!--NI_TOPIC bundle=labview-unit-test-framework-toolkit-api-ref path=lvutfhowto/utfh_exchange_values.html language=enus -->
## TOPIC 00038: Exchanging Values Between the VI under Test, Setup VI, Teardown VI, and the Test Cases Page (Unit Test Framework Toolkit)

- bundle_id: `labview-unit-test-framework-toolkit-api-ref`
- source_path: `lvutfhowto/utfh_exchange_values.html`
- source_url: https://docs-be.ni.com/bundle/labview-unit-test-framework-toolkit-api-ref/raw/resource/enus/lvutfhowto/utfh_exchange_values.html
- document_id: `labview-unit-test-framework-toolkit-api-ref`
- page_type: `leaf`
- content_type: ``

### Exchanging Values Between the VI under Test, Setup VI, Teardown VI, and the Test Cases Page (Unit Test Framework Toolkit)

You can modify the input and expected values by using the front panel of the VI under test, setup VI, and teardown VI and then importing these values to a test case. You also can export values from a test case to the VI under test, setup VI, and teardown VI.

|  | Note LabVIEW lists the controls and indicators from the VI under test on the Test Cases page. If the Input/output values setting on the Unit Test Framework page of the Project Properties dialog box is Include controls and indicators from connector pane, make sure you select a connector pane pattern and assign the terminals for the VI under test. |
| --- | --- |

Complete the following steps to exchange values between the VI under test, setup VI, teardown VI, and the [Test Cases](../lvutf/utf_test_cases_db.html) page.

1. Open the LabVIEW project that contains the files on which you want to perform unit testing.
2. Double-click a .lvtest file to display the Test Properties dialog box.
3. Select Test Cases from the Category list to display the Test Cases page.
4. If this test has more than one test case, use the Test Case control to select the test case you want to configure.
5. Click the Export Values to VI button to export the input and expected values from the current test case to the VI under test, setup VI, and teardown VI. The VI under test, setup VI, and teardown VI open in a separate window.
 [IMAGE alt='image' src='tip.gif']
**Tip** Use the **Export Values to VI** button to open the VI under test while configuring a test.
6. From the front panel of the VI under test, setup VI, and teardown VI, modify the values of any controls and indicators you want to configure.
7. On the Test Properties dialog box, click the Import Values from VI button to import values from the VI under test, setup VI, and teardown VI to the current test case.
 [IMAGE alt='image' src='note.gif']
**Note** When you import values from the VI under test, setup VI, and teardown VI, LabVIEW replaces the input and expected values of the current test case with the values of the corresponding terminals in the VI under test, setup VI, and teardown VI.
8. Select a comparison type from the Comparison list of the output terminal you want to configure. Repeat this step for other output terminals.
9. Click the OK button to close the dialog box and return to the Project Explorer window.
10. Select File»Save to save the project.

The next time you execute this test, LabVIEW runs the setup VI and VI under test by using the input values you specified for each test case in the .lvtest file. LabVIEW then compares the resulting values with the expected values of the VI under test and teardown VI by using the comparison types you specified.

##### Related Information

[Assigning Terminals to Controls and Indicators](/csh?topicname=lvhowto/assigning_controls_and_ind.html)

[Selecting a Connector Pane Pattern](/csh?topicname=lvhowto/selecting_a_connector_pane.html)

<!--NI_TOPIC bundle=labview-unit-test-framework-toolkit-api-ref path=lvutfhowto/utfh_execute.html language=enus -->
## TOPIC 00039: Executing Tests (Unit Test Framework Toolkit)

- bundle_id: `labview-unit-test-framework-toolkit-api-ref`
- source_path: `lvutfhowto/utfh_execute.html`
- source_url: https://docs-be.ni.com/bundle/labview-unit-test-framework-toolkit-api-ref/raw/resource/enus/lvutfhowto/utfh_execute.html
- document_id: `labview-unit-test-framework-toolkit-api-ref`
- page_type: `leaf`
- content_type: ``

### Executing Tests (Unit Test Framework Toolkit)

The LabVIEW Unit Test Framework Toolkit provides several methods you can use to execute tests in a LabVIEW project. Use the 
 [Project Explorer](/csh?topicname=lvdialog/project_explorer_window.html) window to execute tests interactively. You also can execute tests programmatically by using the [Unit Test Framework](../lvutf/utf_vis.html) VIs.

Use this book to learn step-by-step instructions for executing tests in a LabVIEW project.

##### Related Information

[Executing Tests Interactively](../lvutfhowto/utfh_execute_test.html)

[Executing Tests Programmatically](../lvutfhowto/utfh_execute_vi.html)

<!--NI_TOPIC bundle=labview-unit-test-framework-toolkit-api-ref path=lvutfhowto/utfh_execute_mod.html language=enus -->
## TOPIC 00040: Executing Only Modified Tests (Unit Test Framework Toolkit)

- bundle_id: `labview-unit-test-framework-toolkit-api-ref`
- source_path: `lvutfhowto/utfh_execute_mod.html`
- source_url: https://docs-be.ni.com/bundle/labview-unit-test-framework-toolkit-api-ref/raw/resource/enus/lvutfhowto/utfh_execute_mod.html
- document_id: `labview-unit-test-framework-toolkit-api-ref`
- page_type: `leaf`
- content_type: ``

### Executing Only Modified Tests (Unit Test Framework Toolkit)

Complete the following steps to execute only tests that have been modified since a specified time.

1. Open the LabVIEW project that contains the files on which you want to perform unit testing.
2. Click the Project Properties button on the Project toolbar to display the Project Properties dialog box.
3. On the Unit Test Framework page, place a checkmark in the Modified tests and VIs checkbox. The Modified Since options become available.
4. Select the filter option you want to apply.
 [IMAGE alt='image' src='note.gif']
**Note** If you select the **Last test execution** option, you first must generate a test status log file before you can execute tests that have been modified since the last execution.
5. (Optional) Place a checkmark in the Include tests of all caller VIs if you want to execute tests of all the VIs that call the modified VI under test.
6. Click the OK button to close the dialog box and return to the Project Explorer window.
7. (Optional) Select File»Save if you want LabVIEW to save the filter setting in the project file ( .lvproj ).

The next time you execute tests interactively, LabVIEW executes only tests that have been modified since the time you specified on the [Unit Test Framework](../lvutf/utf_proj_prop_db.html) page. You also can execute only modified tests programmatically by using the [Run Tests from Project](../lvutf/utf_run_tests_proj.html) VI. You first must save the filter setting in the project that you want to execute modified tests.

##### Related Information

[Executing Tests from a Project](../lvutfhowto/utfh_execute_vi.html#from_project)

[Executing Tests Interactively](../lvutfhowto/utfh_execute_test.html)

[Generating Log Files](../lvutfhowto/utfh_report_log.html)

<!--NI_TOPIC bundle=labview-unit-test-framework-toolkit-api-ref path=lvutfhowto/utfh_execute_pri.html language=enus -->
## TOPIC 00041: Executing Tests by Priority (Unit Test Framework Toolkit)

- bundle_id: `labview-unit-test-framework-toolkit-api-ref`
- source_path: `lvutfhowto/utfh_execute_pri.html`
- source_url: https://docs-be.ni.com/bundle/labview-unit-test-framework-toolkit-api-ref/raw/resource/enus/lvutfhowto/utfh_execute_pri.html
- document_id: `labview-unit-test-framework-toolkit-api-ref`
- page_type: `leaf`
- content_type: ``

### Executing Tests by Priority (Unit Test Framework Toolkit)

Complete the following steps to execute tests by priority.

1. Open the LabVIEW project that contains the files on which you want to perform unit testing.
2. Click the Project Properties button on the Project toolbar to display the Project Properties dialog box.
3. On the Unit Test Framework page, place a checkmark in the Minimum priority checkbox.
4. Use the Minimum priority control to select a minimum priority.
5. Click the OK button to close the dialog box and return to the Project Explorer window.
6. (Optional) Select File»Save if you want LabVIEW to save the filter setting in the project file ( .lvproj ).

The next time you execute tests interactively, LabVIEW executes only tests with an equal or higher priority than the **Minimum priority** you specified. You also can execute tests by priority programmatically by using the [Run Tests from Project](../lvutf/utf_run_tests_proj.html) VI. You first must save the **Minimum priority** setting in the project that you want to execute tests by priority.

##### Related Information

[Executing Tests Interactively](../lvutfhowto/utfh_execute_test.html)

[Test Priority](../lvutfconcepts/utfc_test_priority.html)

[Executing Tests from a Project](../lvutfhowto/utfh_execute_vi.html#from_project)

<!--NI_TOPIC bundle=labview-unit-test-framework-toolkit-api-ref path=lvutfhowto/utfh_execute_test.html language=enus -->
## TOPIC 00042: Executing Tests Interactively (Unit Test Framework Toolkit)

- bundle_id: `labview-unit-test-framework-toolkit-api-ref`
- source_path: `lvutfhowto/utfh_execute_test.html`
- source_url: https://docs-be.ni.com/bundle/labview-unit-test-framework-toolkit-api-ref/raw/resource/enus/lvutfhowto/utfh_execute_test.html
- document_id: `labview-unit-test-framework-toolkit-api-ref`
- page_type: `leaf`
- content_type: ``

### Executing Tests Interactively (Unit Test Framework Toolkit)

Use the 
 [Project Explorer](/csh?topicname=lvdialog/project_explorer_window.html) window to execute tests interactively. LabVIEW executes tests in the order as they are listed in the project. The 
 [Unit Test Framework Results](../lvutf/utf_results_db.html) window appears after test execution is complete.

|  | Note Before you execute tests, check the Unit Test Framework page of the Project Properties dialog box for desired filter options. |
| --- | --- |

|  | Tip If the test you want to execute contains password-protected VIs, you can store the VI passwords in the project settings. During execution, LabVIEW stores the passwords in the LabVIEW password cache and saves them in the project file (.lvproj). LabVIEW encrypts the passwords before saving them in the project file. |
| --- | --- |

##### Related Information

[Storing VI Passwords for Unit Testing](utfh_passwords.html)

#### Executing Tests

Complete the following steps to execute tests in a LabVIEW project.

1. Open the LabVIEW project that contains the files on which you want to perform unit testing.
2. Right-click a 
 .lvtest file
 and select Run from the shortcut menu.
 [IMAGE alt='image' src='note.gif']
**Note** You also can execute multiple tests by pressing the <Ctrl> key while clicking each .lvtest file. Then right-click the selection and select **Run Unit Tests** from the shortcut menu.
3. Click the OK button to close the dialog box and return to the Project Explorer window.

#### Executing All Tests in a Project

Complete the following steps to execute all tests in a project.

1. Open the LabVIEW project that contains the files on which you want to perform unit testing.
2. Click the Run Unit Tests button on the Unit Test Framework toolbar.

##### Related Information

[Unit Test Framework Toolbar](../lvutfconcepts/utfc_project.html#toolbar)

#### Executing All Tests Associated with a VI

Complete the following steps to execute all tests associated with a VI.

|  | Caution LabVIEW cannot execute all tests associated with a VI if the VI and tests deploy to different targets. In this situation, you must follow the steps to execute tests in a LabVIEW project. |
| --- | --- |

1. Open the LabVIEW project that contains the files on which you want to perform unit testing.
2. Right-click a VI and select Unit Tests»Run from the shortcut menu.
 [IMAGE alt='image' src='note.gif']
**Note** You also can execute tests associated with multiple VIs by pressing the <Ctrl> key while clicking each VI. Then right-click the selection and select **Run Unit Tests** from the shortcut menu.

##### Related Information

[Executing Tests](../lvutfhowto/utfh_execute_test.html#tests)

#### Executing All Tests Associated with a LabVIEW Class

Complete the following steps to execute all tests associated with a LabVIEW class.

|  | Note LabVIEW executes all tests associated with the LabVIEW class library you select and all tests in the project that are assigned to VIs in the LabVIEW class library. |
| --- | --- |

1. Open the LabVIEW project that contains the files on which you want to perform unit testing.
2. Right-click a LabVIEW class library file ( .lvclass ) and select Unit Tests»Run from the shortcut menu. 
 [IMAGE alt='image' src='note.gif']
**Note** You can execute tests on classes that inherit from another LabVIEW class. Right-click the parent class library file and select **Unit Tests»Run Including Children** from the shortcut menu. LabVIEW executes all tests associated with the parent class and all tests associated with the children classes.

##### Related Information

[Creating LabVIEW Classes](/csh?topicname=lvconcepts/creating_classes.html)

[Inheritance](/csh?topicname=lvconcepts/creating_classes.html)

#### Executing All Tests in a Folder or Project Library

Complete the following steps to execute all tests in a virtual folder, folder, or LabVIEW project library.

1. Open the LabVIEW project that contains the files on which you want to perform unit testing.
2. Right-click a folder or project library and select Unit Tests»Run from the shortcut menu.
 [IMAGE alt='image' src='note.gif']
**Note** You also can execute tests in multiple folders or project libraries by pressing the <Ctrl> key while clicking each folder or project library. Then right-click the selection and select **Run Unit Tests** from the shortcut menu.

##### Related Information

[Adding Folders to a Project](/csh?topicname=lvhowto/adding_folders_project.html)

[Adding Items to a Project](/csh?topicname=lvhowto/adding_items_project.html)

<!--NI_TOPIC bundle=labview-unit-test-framework-toolkit-api-ref path=lvutfhowto/utfh_execute_vi.html language=enus -->
## TOPIC 00043: Executing Tests Programmatically (Unit Test Framework Toolkit)

- bundle_id: `labview-unit-test-framework-toolkit-api-ref`
- source_path: `lvutfhowto/utfh_execute_vi.html`
- source_url: https://docs-be.ni.com/bundle/labview-unit-test-framework-toolkit-api-ref/raw/resource/enus/lvutfhowto/utfh_execute_vi.html
- document_id: `labview-unit-test-framework-toolkit-api-ref`
- page_type: `leaf`
- content_type: ``

### Executing Tests Programmatically (Unit Test Framework Toolkit)

Use the [Unit Test Framework](../lvutf/utf_vis.html) VIs to execute tests programmatically.

#### Executing Tests from .lvtest Files

Complete the following steps to create a VI that executes tests from .lvtest files programmatically.

1. Select File»New VI to create a new, blank VI.
2. Display the block diagram by selecting Window»Show Block Diagram .
3. If you do not see the Functions palette, select View»Functions Palette to display this palette.
4. On this palette, select Programming»Unit Test Framework to display the Unit Test Framework VIs.
5. Add the Run Tests from File VI to the block diagram.
 [IMAGE alt='image' src='add.gif'] Add
6. Add the Open Results Window VI to the block diagram.
 [IMAGE alt='image' src='add.gif'] Add
7. Wire the test results out output of the Run Tests from File VI to the test results in input of the Open Results Window VI.
8. Right-click the test file paths input of the Run Tests from File VI and select Create»Control from the shortcut menu. 
 
 A front panel control appears to the left of this VI. This control represents an array of paths to the .lvtest files that you want to execute.
9. Wire all error in and error out terminals on the block diagram.
10. Display the front panel and click the Browse button on the test file paths control to select a .lvtest file.
11. (Optional) Move the cursor over the test file paths control. When a double-headed arrow appears, click and drag the border of the control to add more elements to the array of paths. You also can use the numeric control to display subsequent array elements. Add additional .lvtest files that you want to execute.
12. Select File»Save As and save this VI in an easily accessible location.
13. Click the Run button to run the VI.
 [IMAGE alt='image' src='note.gif']
**Note** When you execute tests from .lvtest files programmatically, LabVIEW executes tests in the order as they listed in the **test file paths** control.

Refer to the Programmatically Run Tests from File VI in the labview\examples\Unit Test Framework\Programmatic Tests directory for an example that demonstrates how to use the Run Tests from File VI to execute tests programmatically.

##### Related Information

[Setting up Error I/O in a VI](/csh?topicname=lvhowto/setting_up_error_i_o_in_vi.html)

#### Executing Tests from a Project

Complete the following steps to create a VI that executes tests from a project programmatically.

1. Select File»New VI to create a new, blank VI.
2. Add the Run Tests from Project VI to the block diagram.
 [IMAGE alt='image' src='add.gif'] Add
3. Add the Open Results Window VI to the block diagram.
 [IMAGE alt='image' src='add.gif'] Add
4. Wire the test results out output of the Run Tests from Project VI to the test results in input of the Open Results Window VI.
5. Right-click the project file path input of the Run Tests from Project VI and select Create»Control from the shortcut menu. 
 
 A front panel control appears to the left of this VI. This control represents the path to the project file ( .lvproj ) that you want to execute tests.
6. Wire all error in and error out terminals on the block diagram.
7. Display the front panel and click the Browse button on the project file path control to select a project file.
8. Select File»Save As and save this VI in an easily accessible location.
9. Click the Run button to run the VI.
 [IMAGE alt='image' src='note.gif']
**Note** When you execute tests from a project programmatically, LabVIEW executes tests in the order as they are listed in the project.

Refer to the Programmatically Run Tests from Project VI in the labview\examples\Unit Test Framework\Programmatic Tests for an example that demonstrates how to use the Run Tests from Project VI to execute tests programmatically.

##### Related Information

[Setting up Error I/O in a VI](/csh?topicname=lvhowto/setting_up_error_i_o_in_vi.html)

#### Generating a Test Report

Complete the following steps to generate a test report when you execute tests programmatically.

1. Open a VI that executes tests programmatically.
2. Add the Create Report VI to the block diagram.
 [IMAGE alt='image' src='add.gif'] Add
3. Wire the test results out output of the Open Results Window VI to the test results in input of the Create Report VI.
 [IMAGE alt='image' src='note.gif']
**Note** You also can wire the **test results out** output of the Open Results Window VI to the **test results in** input of the Run Tests from Project or Run Tests from Files VI.
4. Right-click the report type input of the Create Report VI and select Create»Control from the shortcut menu. 
 
 A front panel control appears to the left of this VI. This control represents the type of report that this VI generates after test execution.
5. Click the report type control and select the type of report this VI generates. The default report type is HTML.
6. Right-click the report path input of the Create Report VI and select Create»Control from the shortcut menu. 
 
 A front panel control appears to the left of this VI. This control represents the path to which this VI generates the test report.
7. Click the report path control and select the path to which this VI generates the test report.
 [IMAGE alt='image' src='note.gif']
**Note** If you do not select a path for the report, LabVIEW generates the report in the My Documents\LabVIEW Data directory.
8. Wire all error in and error out terminals on the block diagram.
 
 
 The block diagram now resembles the following figure.
 [IMAGE alt='image' src='bd_create_report.gif'] 
 [IMAGE alt='image' src='note.gif']
**Note** You can customize the test report by wiring values to the remaining inputs of the Create Report VI.
9. Select File»Save As and save this VI in an easily accessible location.
10. Click the Run button to run the VI.

##### Related Information

[Test Results](../lvutfconcepts/utfc_results.html)

[Setting up Error I/O in a VI](/csh?topicname=lvhowto/setting_up_error_i_o_in_vi.html)

<!--NI_TOPIC bundle=labview-unit-test-framework-toolkit-api-ref path=lvutfhowto/utfh_expt_impt_vctr.html language=enus -->
## TOPIC 00044: Exporting and Importing Test Vectors (Unit Test Framework Toolkit)

- bundle_id: `labview-unit-test-framework-toolkit-api-ref`
- source_path: `lvutfhowto/utfh_expt_impt_vctr.html`
- source_url: https://docs-be.ni.com/bundle/labview-unit-test-framework-toolkit-api-ref/raw/resource/enus/lvutfhowto/utfh_expt_impt_vctr.html
- document_id: `labview-unit-test-framework-toolkit-api-ref`
- page_type: `leaf`
- content_type: ``

### Exporting and Importing Test Vectors (Unit Test Framework Toolkit)

You can modify values of a test vector by using an array control of a VI. Complete the following steps to modify the values of a test vector by using an array control:

1. Export values from a test vector to a VI.
2. Edit the values by using the front panel of the VI.
3. Import modified values to the test vector.

To export or import the values of a test vector, you must have a VI that contains an array control with a proper data type.

If you export or import non-numeric values, the data type of the test vector and array control must be the same. For example, if you export values from a Boolean test vector to an array control, the data type of the control must be array of Booleans.

If you export numeric values of a test vector to an array control, the data type of the array control must have the same or larger scale than the test vector data type. For example, if you export values of an I8 test vector, the data type of the array control can be I8, I16, single floating-point, or other numeric data types that have larger scales.

If you import numeric values from an array control to a test vector, the data type of the test vector must have the same or larger scale than the array control data type. For example, if you import values from a single floating-point array control, the data type of the test vector can be single floating-point, double floating-point, or other numeric data types that have larger scales.

#### Exporting Values from a Test Vector to an Array Control

Complete the following steps to export values from a test vector to an array control:

1. Open the VI that contains the target array control.
2. Click the Export button in the Test Vector Properties - Edit dialog box to display the Test Vector Properties - Export dialog box.
3. Select the source test vector from the Test Vectors list.
4. Select the VI that you opened in step 1 from the Target VIs list.
 [IMAGE alt='image' src='note.gif']
**Note** The **Target VIs** list does not display the VI if you do not open this VI in LabVIEW.
5. Select the target array control from the Target Controls list. LabVIEW displays the array controls that have proper data types only.
6. Click the OK button to close this dialog box and export the values to the target array control. LabVIEW displays the front panel of this VI after you click the OK button.

#### Importing Values from an Array Control to a Test Vector

Complete the following steps to import values from an array control to a test vector.

1. Open the VI that contains the source array control.
2. Click the Import button in the Test Vector Properties - Edit dialog box to display the Test Vector Properties - Import dialog box.
3. Select the VI that you opened in step 1 from the Source VIs list.
 [IMAGE alt='image' src='note.gif']
**Note** The **Source VI** list does not display the VI if you do not open this VI in LabVIEW.
4. Select the target test vector from the Target Test Vectors list.
5. Select the source array control from the Source Controls list. LabVIEW displays the array controls that have proper data types only.
6. Click the OK button to close this dialog box and import the values to the target test vector.

<!--NI_TOPIC bundle=labview-unit-test-framework-toolkit-api-ref path=lvutfhowto/utfh_manage.html language=enus -->
## TOPIC 00045: Managing Tests (Unit Test Framework Toolkit)

- bundle_id: `labview-unit-test-framework-toolkit-api-ref`
- source_path: `lvutfhowto/utfh_manage.html`
- source_url: https://docs-be.ni.com/bundle/labview-unit-test-framework-toolkit-api-ref/raw/resource/enus/lvutfhowto/utfh_manage.html
- document_id: `labview-unit-test-framework-toolkit-api-ref`
- page_type: `leaf`
- content_type: ``

### Managing Tests (Unit Test Framework Toolkit)

Use the 
 [Project Explorer](/csh?topicname=lvdialog/project_explorer_window.html) window to manage tests in a project. You can use virtual folders, auto-populating folders, and LabVIEW project libraries to organize a project.

Use this book to learn step-by-step instructions for managing tests in a LabVIEW project.

##### Related Information

[Organizing a Project](../lvutfhowto/utfh_manage_organize.html)

[Using Folders in LabVIEW Projects](/csh?topicname=lvconcepts/using_project_folders.html)

[Using Libraries in LabVIEW Projects](/csh?topicname=lvconcepts/project_libraries.html)

<!--NI_TOPIC bundle=labview-unit-test-framework-toolkit-api-ref path=lvutfhowto/utfh_manage_find.html language=enus -->
## TOPIC 00046: Finding Tests and VIs (Unit Test Framework Toolkit)

- bundle_id: `labview-unit-test-framework-toolkit-api-ref`
- source_path: `lvutfhowto/utfh_manage_find.html`
- source_url: https://docs-be.ni.com/bundle/labview-unit-test-framework-toolkit-api-ref/raw/resource/enus/lvutfhowto/utfh_manage_find.html
- document_id: `labview-unit-test-framework-toolkit-api-ref`
- page_type: `leaf`
- content_type: ``

### Finding Tests and VIs (Unit Test Framework Toolkit)

Use the 
 [Project Explorer](/csh?topicname=lvdialog/project_explorer_window.html) window to find tests and VIs in a LabVIEW project. You also can find a 
 .lvtest file
 on disk.

#### Finding All Tests Associated with a VI

Complete the following steps to find all tests associated with a VI.

1. Open the LabVIEW project that contains the files on which you want to perform unit testing.
2. Right-click a VI and select Unit Tests»Find from the shortcut menu. LabVIEW highlights all the tests that are associated with this VI.
 [IMAGE alt='image' src='note.gif']
**Note** To find tests for multiple VIs, select multiple VIs by pressing the <Ctrl> key while clicking each VI. Then right-click the selection and select **Find Unit Tests** from the shortcut menu.

#### Finding the VI Associated with a Test

Complete the following steps to find the VI associated with a test.

1. Open the LabVIEW project that contains the files on which you want to perform unit testing.
2. Right-click the .lvtest file for which you want to find the VI under test and select Find VI . LabVIEW highlights the VI under test that is associated with this test.

#### Finding a .lvtest File on Disk

Complete the following steps to find a .lvtest file on disk.

1. Open the LabVIEW project that contains the files on which you want to perform unit testing.
2. Right-click a .lvtest file and select Explore from the shortcut menu.

<!--NI_TOPIC bundle=labview-unit-test-framework-toolkit-api-ref path=lvutfhowto/utfh_manage_organize.html language=enus -->
## TOPIC 00047: Organizing a Project (Unit Test Framework Toolkit)

- bundle_id: `labview-unit-test-framework-toolkit-api-ref`
- source_path: `lvutfhowto/utfh_manage_organize.html`
- source_url: https://docs-be.ni.com/bundle/labview-unit-test-framework-toolkit-api-ref/raw/resource/enus/lvutfhowto/utfh_manage_organize.html
- document_id: `labview-unit-test-framework-toolkit-api-ref`
- page_type: `leaf`
- content_type: ``

### Organizing a Project (Unit Test Framework Toolkit)

You must create and save a LabVIEW project before you can use the LabVIEW Unit Test Framework Toolkit to create tests. Use projects to group together all the files you need to perform unit testing. Use virtual folders, auto-populating folders, and LabVIEW project libraries to organize a project.

##### Related Information

[Using Folders in LabVIEW Projects](/csh?topicname=lvconcepts/using_project_folders.html)

[Using Libraries in LabVIEW Projects](/csh?topicname=lvconcepts/project_libraries.html)

#### Adding Files to a Project

Complete the following steps to add files, such as VIs, .lvtest files, .lvvect files, auto-populating folders, and LabVIEW project libraries, to a LabVIEW project.

1. Create a new project or open an existing project.
2. Right-click a target, such as My Computer , and select Add»File from the shortcut menu. A file dialog box appears.
3. Navigate to and select the files you want to add to the project.
4. Click the Add File button. The newly-added items appear at the bottom of the project tree, above the Dependencies icon.
 [IMAGE alt='image' src='note.gif']
**Note** When you add an item that is part of a LabVIEW project library, LabVIEW adds the entire project library to the project tree.
5. Select File»Save to save the project.

##### Related Information

[Creating a LabVIEW Project](/csh?topicname=lvhowto/creating_lv_projects.html)

[Using Libraries in LabVIEW Projects](/csh?topicname=lvconcepts/project_libraries.html)

#### Using Folders to Organize a Project

You can use virtual folders, auto-populating folders, and project libraries to organize a project.

Complete the following steps to organize VIs, .lvtest files, and .lvvect files in a project.

1. Open the LabVIEW project that contains the files on which you want to perform unit testing.
2. Add a folder or project library to a project.
3. Drag and drop VIs, .lvtest files, and .lvvect files to this folder. You also can add folders inside a folder.
4. Select File»Save to save the project.

##### Related Information

[Adding Folders to a Project](/csh?topicname=lvhowto/adding_folders_project.html)

[Adding Items to a Project](/csh?topicname=lvhowto/adding_items_project.html)

<!--NI_TOPIC bundle=labview-unit-test-framework-toolkit-api-ref path=lvutfhowto/utfh_manage_remove.html language=enus -->
## TOPIC 00048: Removing a Test from a LabVIEW Project (Unit Test Framework Toolkit)

- bundle_id: `labview-unit-test-framework-toolkit-api-ref`
- source_path: `lvutfhowto/utfh_manage_remove.html`
- source_url: https://docs-be.ni.com/bundle/labview-unit-test-framework-toolkit-api-ref/raw/resource/enus/lvutfhowto/utfh_manage_remove.html
- document_id: `labview-unit-test-framework-toolkit-api-ref`
- page_type: `leaf`
- content_type: ``

### Removing a Test from a LabVIEW Project (Unit Test Framework Toolkit)

Complete the following steps to remove a test from a LabVIEW project.

|  | Note Removing a test from a project does not delete the .lvtest file on disk. |
| --- | --- |

1. Open the LabVIEW project that contains the files on which you want to perform unit testing.
2. Right-click a .lvtest file and select Remove from Project from the shortcut menu. 
 [IMAGE alt='image' src='note.gif']
**Note** You also can remove multiple .lvtest files by pressing the <Ctrl> key while clicking each file. Then right-click the selection and select **Remove from Project** from the shortcut menu.
3. Select File»Save to save the project.

<!--NI_TOPIC bundle=labview-unit-test-framework-toolkit-api-ref path=lvutfhowto/utfh_manage_rename.html language=enus -->
## TOPIC 00049: Renaming a Test (Unit Test Framework Toolkit)

- bundle_id: `labview-unit-test-framework-toolkit-api-ref`
- source_path: `lvutfhowto/utfh_manage_rename.html`
- source_url: https://docs-be.ni.com/bundle/labview-unit-test-framework-toolkit-api-ref/raw/resource/enus/lvutfhowto/utfh_manage_rename.html
- document_id: `labview-unit-test-framework-toolkit-api-ref`
- page_type: `leaf`
- content_type: ``

### Renaming a Test (Unit Test Framework Toolkit)

Complete the following steps to rename a test in a LabVIEW project.

1. Open the LabVIEW project that contains the files on which you want to perform unit testing.
2. Right-click a .lvtest file and select Rename from the shortcut menu.
 [IMAGE alt='image' src='caution.gif']
**Caution** Do not rename .lvtest files in Windows Explorer if the .lvtest files already belong to a project. If you rename .lvtest files on disk, LabVIEW does not update the filenames in the project. You can no longer execute these tests from the [Project Explorer](/csh?topicname=lvdialog/project_explorer_window.html) window.
3. Enter the new name for this test and click the OK button.
4. Select File»Save to save the project.

<!--NI_TOPIC bundle=labview-unit-test-framework-toolkit-api-ref path=lvutfhowto/utfh_new_lvvect.html language=enus -->
## TOPIC 00050: Creating Test Vector Files (Unit Test Framework Toolkit)

- bundle_id: `labview-unit-test-framework-toolkit-api-ref`
- source_path: `lvutfhowto/utfh_new_lvvect.html`
- source_url: https://docs-be.ni.com/bundle/labview-unit-test-framework-toolkit-api-ref/raw/resource/enus/lvutfhowto/utfh_new_lvvect.html
- document_id: `labview-unit-test-framework-toolkit-api-ref`
- page_type: `leaf`
- content_type: ``

### Creating Test Vector Files (Unit Test Framework Toolkit)

Complete the following steps to create a test vector file.

1. Open the LabVIEW project for which you want to create a test vector file.
2. Right-click My Computer and select New»Test Vectors from the shortcut menu. LabVIEW creates a .lvvect file to save the test vector file.
3. (Optional) Double-click a .lvvect file in the Project Explorer window to display the Test Vector File Properties dialog box. You also can right-click the .lvvect file and select Properties from the shortcut menu to open the dialog box to configure the test vector file you just created.
4. (Optional) Save the changes you made to the test vector file.
5. Select File»Save to save the project.

After you create a test vector file, you can create test vectors or add other test vector files to this test vector file.

##### Related Information

[Creating Test Vectors in a Test Vector File](utfh_new_vector.html)

<!--NI_TOPIC bundle=labview-unit-test-framework-toolkit-api-ref path=lvutfhowto/utfh_new_vctr_file.html language=enus -->
## TOPIC 00051: Creating Test Vector Files and Test Vectors (Unit Test Framework Toolkit)

- bundle_id: `labview-unit-test-framework-toolkit-api-ref`
- source_path: `lvutfhowto/utfh_new_vctr_file.html`
- source_url: https://docs-be.ni.com/bundle/labview-unit-test-framework-toolkit-api-ref/raw/resource/enus/lvutfhowto/utfh_new_vctr_file.html
- document_id: `labview-unit-test-framework-toolkit-api-ref`
- page_type: `leaf`
- content_type: ``

### Creating Test Vector Files and Test Vectors (Unit Test Framework Toolkit)

Use this book to learn step-by-step instructions for creating and using test vector files and test vectors in a LabVIEW project.

|  | Note You must create and save a LabVIEW project before you can use the LabVIEW Unit Test Framework Toolkit to create test vector files and test vectors. |
| --- | --- |

##### Related Information

[Creating Test Vector Files](utfh_new_lvvect.html)

[Creating Test Vectors in a Test Vector File](utfh_new_vector.html)

[Test Vectors and .lvvect Files](../lvutfconcepts/utfc_test_vector.html)

[Creating a LabVIEW Project](/csh?topicname=lvhowto/creating_lv_projects.html)

<!--NI_TOPIC bundle=labview-unit-test-framework-toolkit-api-ref path=lvutfhowto/utfh_new_vector.html language=enus -->
## TOPIC 00052: Creating Test Vectors in a Test Vector File (Unit Test Framework Toolkit)

- bundle_id: `labview-unit-test-framework-toolkit-api-ref`
- source_path: `lvutfhowto/utfh_new_vector.html`
- source_url: https://docs-be.ni.com/bundle/labview-unit-test-framework-toolkit-api-ref/raw/resource/enus/lvutfhowto/utfh_new_vector.html
- document_id: `labview-unit-test-framework-toolkit-api-ref`
- page_type: `leaf`
- content_type: ``

### Creating Test Vectors in a Test Vector File (Unit Test Framework Toolkit)

Complete the following steps to create test vectors in a test vector file.

1. Open the LabVIEW project that contains the test vector file in which you want to create test vectors.
2. Double-click a .lvvect file in the Project Explorer window to display the Test Vector File Properties dialog box.
3. Click the New button to display the Test Vector Properties - New dialog box.
4. Specify a name in the Name field.
5. Specify the data type of the test vector in the Data type field.
6. Specify the element number of this test vector in the Size field. You can change the element number when you edit a test vector.
7. Click the OK button to close the Test Vector Properties - New dialog box and create the test vector.
8. (Optional) Repeat step 3 through 7 to create multiple test vectors.
9. Click the Save button to close the Test Vector File Properties dialog box and save the test vector file.

<!--NI_TOPIC bundle=labview-unit-test-framework-toolkit-api-ref path=lvutfhowto/utfh_passwords.html language=enus -->
## TOPIC 00053: Storing VI Passwords for Unit Testing (Unit Test Framework Toolkit)

- bundle_id: `labview-unit-test-framework-toolkit-api-ref`
- source_path: `lvutfhowto/utfh_passwords.html`
- source_url: https://docs-be.ni.com/bundle/labview-unit-test-framework-toolkit-api-ref/raw/resource/enus/lvutfhowto/utfh_passwords.html
- document_id: `labview-unit-test-framework-toolkit-api-ref`
- page_type: `leaf`
- content_type: ``

### Storing VI Passwords for Unit Testing (Unit Test Framework Toolkit)

You can execute tests on password-protected VIs by adding passwords to the project settings. During execution, LabVIEW stores the passwords in the LabVIEW password cache and saves them in the project file (.lvproj). LabVIEW encrypts the passwords before saving them in the project file.

Complete the following steps to store VI passwords to the project settings.

1. Open the LabVIEW project that contains the files on which you want to perform unit testing.
2. Click the Project Properties button on the Project toolbar to display the Project Properties dialog box.
3. Select Unit Test Framework from the Category list to display the Unit Test Framework page.
4. Enter the password of the password-protected VI in the Password to Add text box.
5. Click the Add button.
6. Repeat steps 4 and 5 to add more passwords to the password list.
7. Click the OK button to close the dialog box and return to the Project Explorer window.

You can clear the password list from the project settings and from the project file by clicking the **Clear All** button.

|  | Note Clicking the Clear All button does not remove passwords from the LabVIEW password cache. You can remove passwords from the LabVIEW password cache by restarting LabVIEW or by clearing the password cache from the Environment page of the Options dialog box. |
| --- | --- |

##### Related Information

[Executing Tests](../lvutfhowto/utfh_execute.html)

<!--NI_TOPIC bundle=labview-unit-test-framework-toolkit-api-ref path=lvutfhowto/utfh_report_custom.html language=enus -->
## TOPIC 00054: Customizing Test Reports (Unit Test Framework Toolkit)

- bundle_id: `labview-unit-test-framework-toolkit-api-ref`
- source_path: `lvutfhowto/utfh_report_custom.html`
- source_url: https://docs-be.ni.com/bundle/labview-unit-test-framework-toolkit-api-ref/raw/resource/enus/lvutfhowto/utfh_report_custom.html
- document_id: `labview-unit-test-framework-toolkit-api-ref`
- page_type: `leaf`
- content_type: ``

### Customizing Test Reports (Unit Test Framework Toolkit)

You can customize test reports by specifying the contents of the reports. You also can format HTML reports by using a Cascading Style Sheet (CSS) file.

##### Related Information

[Test Reports](../lvutfconcepts/utfc_results.html#test_report)

#### Customizing Report Contents

Complete the following steps to specify the types of results to include in test reports.

1. Open the LabVIEW project that contains the files on which you want to perform unit testing.
2. Click the Project Properties button on the Project toolbar to display the Project Properties dialog box.
3. Select Unit Test Framework from the Category list to display the Unit Test Framework page.
4. Place a checkmark in the checkbox of each type of results you want to include in test reports.
5. Click the OK button to close the dialog box and return to the Project Explorer window.

#### Formatting HTML Reports

Complete the following steps to format HTML reports by using a CSS file.

1. Open the LabVIEW project that contains the files on which you want to perform unit testing.
2. Click the Project Properties button on the Project toolbar to display the Project Properties dialog box.
3. Select Unit Test Framework from the Category list to display the Unit Test Framework page.
4. Make sure the Generate HTML report checkbox contains a checkmark.
5. In the Report Details section, place a checkmark in the Use user-defined CSS file checkbox.
6. Click the Browse button next to the CSS file path text box. A file dialog box appears.
7. Navigate to and select the CSS file you want to use to customize HTML reports. Click the OK button.
8. Click the OK button to close the dialog box and return to the Project Explorer window.

<!--NI_TOPIC bundle=labview-unit-test-framework-toolkit-api-ref path=lvutfhowto/utfh_report_generate.html language=enus -->
## TOPIC 00055: Generating Test Reports (Unit Test Framework Toolkit)

- bundle_id: `labview-unit-test-framework-toolkit-api-ref`
- source_path: `lvutfhowto/utfh_report_generate.html`
- source_url: https://docs-be.ni.com/bundle/labview-unit-test-framework-toolkit-api-ref/raw/resource/enus/lvutfhowto/utfh_report_generate.html
- document_id: `labview-unit-test-framework-toolkit-api-ref`
- page_type: `leaf`
- content_type: ``

### Generating Test Reports (Unit Test Framework Toolkit)

You can generate test reports in HTML, Automatic Test Markup Language (ATML), or ASCII format.

Complete the following steps to generate test reports.

1. Open the LabVIEW project that contains the files on which you want to perform unit testing.
2. Click the Project Properties button on the Project toolbar to display the Project Properties dialog box.
3. Select Unit Test Framework from the Category list to display the Unit Test Framework page.
4. In the Generate Reports section, place a checkmark in the checkbox of each report you want to generate.
5. Click the Browse button to select a file path for each report you want to generate.
 [IMAGE alt='image' src='note.gif']
**Note** If you do not select a path for the report(s), LabVIEW generates the report(s) in the same directory as the project.
6. (Optional) Place a checkmark in a View report after execution checkbox to display the test report after test execution.
7. Click the OK button to close the dialog box and return to the Project Explorer window.
8. (Optional) Select File»Save if you want LabVIEW to save the report settings in the project file ( .lvproj ).

The next time you execute tests interactively LabVIEW generates the test report(s) you specified on the [Unit Test Framework](../lvutf/utf_proj_prop_db.html) page. If a test report already exists from a previous test execution, LabVIEW replaces the existing test report.

##### Related Information

[Executing Tests Interactively](../lvutfhowto/utfh_execute_test.html)

<!--NI_TOPIC bundle=labview-unit-test-framework-toolkit-api-ref path=lvutfhowto/utfh_report_log.html language=enus -->
## TOPIC 00056: Generating Log Files (Unit Test Framework Toolkit)

- bundle_id: `labview-unit-test-framework-toolkit-api-ref`
- source_path: `lvutfhowto/utfh_report_log.html`
- source_url: https://docs-be.ni.com/bundle/labview-unit-test-framework-toolkit-api-ref/raw/resource/enus/lvutfhowto/utfh_report_log.html
- document_id: `labview-unit-test-framework-toolkit-api-ref`
- page_type: `leaf`
- content_type: ``

### Generating Log Files (Unit Test Framework Toolkit)

Complete the following steps to generate log files during and after execution.

1. Open the LabVIEW project that contains the files on which you want to perform unit testing.
2. Click the Project Properties button on the Project toolbar to display the Project Properties dialog box.
3. Select Unit Test Framework from the Category list to display the Unit Test Framework page.
4. In the Generate Log Files section, place a checkmark in the checkbox of each log file you want to generate.
5. Click the Browse button to select a file path for each log file you want to generate.
 [IMAGE alt='image' src='note.gif']
**Note** If you do not select a path for the log file(s), LabVIEW generates the log file(s) in the same directory as the project.
6. (Optional) If you generate a test execution log file, place a checkmark in the Overwrite log file checkbox if you want to replace the existing log file with the details from each subsequent test execution.
 [IMAGE alt='image' src='note.gif']
**Note** LabVIEW appends the details of each subsequent test execution to the existing log file unless you place a checkmark in the **Overwrite log file** or change the log file name.
7. Click the OK button to close the dialog box and return to the Project Explorer window.
8. (Optional) Select File»Save if you want LabVIEW to save the report settings in the project file ( .lvproj ).

The next time you execute tests interactively, LabVIEW generates the log file(s) you specified on the [Unit Test Framework](../lvutf/utf_proj_prop_db.html) page.

##### Related Information

[Executing Tests Interactively](../lvutfhowto/utfh_execute_test.html)

[Log Files](../lvutfconcepts/utfc_results.html#log_files)

<!--NI_TOPIC bundle=labview-unit-test-framework-toolkit-api-ref path=lvutfhowto/utfh_result_saveload.html language=enus -->
## TOPIC 00057: Saving and Loading Test Results (Unit Test Framework Toolkit)

- bundle_id: `labview-unit-test-framework-toolkit-api-ref`
- source_path: `lvutfhowto/utfh_result_saveload.html`
- source_url: https://docs-be.ni.com/bundle/labview-unit-test-framework-toolkit-api-ref/raw/resource/enus/lvutfhowto/utfh_result_saveload.html
- document_id: `labview-unit-test-framework-toolkit-api-ref`
- page_type: `leaf`
- content_type: ``

### Saving and Loading Test Results (Unit Test Framework Toolkit)

You can save test results from the 
 [Unit Test Framework Results](../lvutf/utf_results_db.html) window to a [.lvutf file](../lvutfconcepts/utfc_results.html) that you can load later.

##### Related Information

[Test Results](../lvutfconcepts/utfc_results.html)

#### Saving Test Results to a File

Complete the following steps to save test results from the 
 [Unit Test Framework Results](../lvutf/utf_results_db.html) window to a .lvutf file.

1. After you execute tests, LabVIEW displays the Unit Test Framework Results wind . Click the Save button to save test results to a .lvutf file. A file dialog box appears.
2. Navigate to the location where you want to save the .lvutf file.
3. Enter the filename you want for the .lvutf file and click the OK button.

#### Loading Test Results from a File

Complete the following steps to load a .lvutf file into the [Unit Test Framework Results](../lvutf/utf_results_db.html) window.

1. Open the LabVIEW project that contains the files on which you want to perform unit testing.
2. Click the Unit Test Framework Results button on the Unit Test Framework toolbar to display the Unit Test Framework Results window.
3. Click the Load button. A file dialog box appears.
4. Navigate to and select the .lvutf file you want to load. Click the OK button. The Unit Test Framework Results window displays the results you saved previously.
 [IMAGE alt='image' src='note.gif']
**Note** When you load .lvutf files into the [Unit Test Framework Results](../lvutf/utf_results_db.html) window, you might not be able to double-click errors to highlight them accurately in the VIs if the VIs have been modified since the last execution.

##### Related Information

[Unit Test Framework Toolbar](../lvutfconcepts/utfc_project.html#toolbar)

<!--NI_TOPIC bundle=labview-unit-test-framework-toolkit-api-ref path=lvutfhowto/utfh_results.html language=enus -->
## TOPIC 00058: Viewing Test Results and Generating Reports (Unit Test Framework Toolkit)

- bundle_id: `labview-unit-test-framework-toolkit-api-ref`
- source_path: `lvutfhowto/utfh_results.html`
- source_url: https://docs-be.ni.com/bundle/labview-unit-test-framework-toolkit-api-ref/raw/resource/enus/lvutfhowto/utfh_results.html
- document_id: `labview-unit-test-framework-toolkit-api-ref`
- page_type: `leaf`
- content_type: ``

### Viewing Test Results and Generating Reports (Unit Test Framework Toolkit)

Use the 
 [Unit Test Framework Results](../lvutf/utf_results_db.html) window to view test results. Use the [Project Properties](/csh?topicname=lvdialog/project_properties.html) to configure which test reports and log files you want to generate. You can customize test reports by specifying the contents of the reports. You also can format HTML reports by using a Cascading Style Sheet (CSS) file.

Use this book to learn step-by-step instructions for viewing test results, generating test reports, and generating log files.

##### Related Information

[Customizing Test Reports](../lvutfhowto/utfh_report_custom.html#content)

[Generating Log Files](../lvutfhowto/utfh_report_log.html)

[Generating Test Reports](../lvutfhowto/utfh_report_generate.html)

[Test Results](../lvutfconcepts/utfc_results.html)

<!--NI_TOPIC bundle=labview-unit-test-framework-toolkit-api-ref path=lvutfhowto/utfh_specify_minimum_code_coverage.html language=enus -->
## TOPIC 00059: Specifying a Minimum Code Coverage Requirement (Unit Test Framework Toolkit)

- bundle_id: `labview-unit-test-framework-toolkit-api-ref`
- source_path: `lvutfhowto/utfh_specify_minimum_code_coverage.html`
- source_url: https://docs-be.ni.com/bundle/labview-unit-test-framework-toolkit-api-ref/raw/resource/enus/lvutfhowto/utfh_specify_minimum_code_coverage.html
- document_id: `labview-unit-test-framework-toolkit-api-ref`
- page_type: `leaf`
- content_type: ``

### Specifying a Minimum Code Coverage Requirement (Unit Test Framework Toolkit)

Complete the following steps to specify a minimum code coverage requirement.

1. Open the LabVIEW project that contains the files on which you want to perform unit testing.
2. Double-click a .lvtest file to display the Test Properties dialog box.
3. Select Advanced from the Category list to display the Advanced page.
4. Place a checkmark in the Set minimum code coverage checkbox.
5. Use the Code coverage control to specify a minimum code coverage requirement, in percent.
 [IMAGE alt='image' src='note.gif']
**Note** Use minimum code coverage requirement for VIs that contain [Case structures](/csh?topicname=glang/case_structure.html).
6. Click the OK button to close the dialog box and return to the Project Explorer window.
7. Select File»Save to save the project.

The next time you execute this test, LabVIEW runs the VI under test and measures the percentage of subdiagrams executed. If the VI under test does not meet the minimum code coverage requirement you specified, test results show this test as failed.

##### Related Information

[Code Coverage](../lvutfconcepts/utfc_code_cov.html)

<!--NI_TOPIC bundle=labview-unit-test-framework-toolkit-api-ref path=lvutfhowto/utfh_specify_precision_digits.html language=enus -->
## TOPIC 00060: Specifying the Digits of Precision for Floating-Point Comparison (Unit Test Framework Toolkit)

- bundle_id: `labview-unit-test-framework-toolkit-api-ref`
- source_path: `lvutfhowto/utfh_specify_precision_digits.html`
- source_url: https://docs-be.ni.com/bundle/labview-unit-test-framework-toolkit-api-ref/raw/resource/enus/lvutfhowto/utfh_specify_precision_digits.html
- document_id: `labview-unit-test-framework-toolkit-api-ref`
- page_type: `leaf`
- content_type: ``

### Specifying the Digits of Precision for Floating-Point Comparison (Unit Test Framework Toolkit)

Complete the following steps to specify the digits of precision for comparing floating-point numbers.

1. Open the LabVIEW project that contains the files on which you want to perform unit testing.
2. Double-click a .lvtest file to display the Test Properties dialog box.
3. Select Advanced from the Category list to display the Advanced page.
4. Use the Digits of precision for floating-point comparison control to set the digits of precision for comparing floating-point numbers during test execution.
5. Click the OK button to close the dialog box and return to the Project Explorer window.
6. Select File»Save to save the project.

<!--NI_TOPIC bundle=labview-unit-test-framework-toolkit-api-ref path=lvutfhowto/utfh_specify_priority.html language=enus -->
## TOPIC 00061: Specifying a Test Priority (Unit Test Framework Toolkit)

- bundle_id: `labview-unit-test-framework-toolkit-api-ref`
- source_path: `lvutfhowto/utfh_specify_priority.html`
- source_url: https://docs-be.ni.com/bundle/labview-unit-test-framework-toolkit-api-ref/raw/resource/enus/lvutfhowto/utfh_specify_priority.html
- document_id: `labview-unit-test-framework-toolkit-api-ref`
- page_type: `leaf`
- content_type: ``

### Specifying a Test Priority (Unit Test Framework Toolkit)

Complete the following steps to specify a test priority for a test.

1. Open the LabVIEW project that contains the files on which you want to perform unit testing.
2. Double-click a .lvtest file to display the Test Properties dialog box. You also can right-click the .lvtest file and select Properties from the shortcut menu to open the dialog box.
3. On the Configuration page, use the Test Priority control to select a priority for this test.
4. Click the OK button to close the dialog box and return to the Project Explorer window.
5. Select File»Save to save the project.

The next time you execute tests by priority, LabVIEW executes only tests with an equal or higher priority than the **Minimum priority** you specified on the [Unit Test Framework](../lvutf/utf_proj_prop_db.html) page of the [Project Properties](/csh?topicname=lvdialog/project_properties.html) dialog box.

##### Related Information

[Executing Tests by Priority](../lvutfhowto/utfh_execute_pri.html)

[Test Priority](../lvutfconcepts/utfc_test_priority.html)

<!--NI_TOPIC bundle=labview-unit-test-framework-toolkit-api-ref path=lvutfhowto/utfh_specify_repetitions.html language=enus -->
## TOPIC 00062: Specifying the Number of Times to Repeat a Test (Unit Test Framework Toolkit)

- bundle_id: `labview-unit-test-framework-toolkit-api-ref`
- source_path: `lvutfhowto/utfh_specify_repetitions.html`
- source_url: https://docs-be.ni.com/bundle/labview-unit-test-framework-toolkit-api-ref/raw/resource/enus/lvutfhowto/utfh_specify_repetitions.html
- document_id: `labview-unit-test-framework-toolkit-api-ref`
- page_type: `leaf`
- content_type: ``

### Specifying the Number of Times to Repeat a Test (Unit Test Framework Toolkit)

Complete the following steps to specify the number of times to repeat a test.

1. Open the LabVIEW project that contains the files on which you want to perform unit testing.
2. Double-click a .lvtest file to display the Test Properties dialog box.
3. Select Advanced from the Category list to display the Advanced page.
4. Use the Repetitions control to specify the number of times LabVIEW repeats this test.
5. Click the OK button to close the dialog box and return to the Project Explorer window.
6. Select File»Save to save the project.

The next time you execute this test, LabVIEW runs the VI under test the number of times you specified. Test results show the results of each repetition.

<!--NI_TOPIC bundle=labview-unit-test-framework-toolkit-api-ref path=lvutfhowto/utfh_specify_requirements_ids.html language=enus -->
## TOPIC 00063: Specifying Requirement IDs (Unit Test Framework Toolkit)

- bundle_id: `labview-unit-test-framework-toolkit-api-ref`
- source_path: `lvutfhowto/utfh_specify_requirements_ids.html`
- source_url: https://docs-be.ni.com/bundle/labview-unit-test-framework-toolkit-api-ref/raw/resource/enus/lvutfhowto/utfh_specify_requirements_ids.html
- document_id: `labview-unit-test-framework-toolkit-api-ref`
- page_type: `leaf`
- content_type: ``

### Specifying Requirement IDs (Unit Test Framework Toolkit)

Complete the following steps to specify requirement IDs for a test.

1. Open the LabVIEW project that contains the files on which you want to perform unit testing.
2. Double-click a .lvtest file to display the Test Properties dialog box.
3. On the Configuration page, enter requirement IDs in the Requirement ID text box for integration with NI Requirements Gateway. Ensure the requirement IDs match the corresponding requirements in Requirements Gateway.
4. Click the OK button to close the dialog box and return to the Project Explorer window.
5. Select File»Save to save the project.

##### Related Information

[Requirement IDs](../lvutfconcepts/utfc_test_require.html)

<!--NI_TOPIC bundle=labview-unit-test-framework-toolkit-api-ref path=lvutfhowto/utfh_specify_timeout.html language=enus -->
## TOPIC 00064: Specifying a Timeout for a Test (Unit Test Framework Toolkit)

- bundle_id: `labview-unit-test-framework-toolkit-api-ref`
- source_path: `lvutfhowto/utfh_specify_timeout.html`
- source_url: https://docs-be.ni.com/bundle/labview-unit-test-framework-toolkit-api-ref/raw/resource/enus/lvutfhowto/utfh_specify_timeout.html
- document_id: `labview-unit-test-framework-toolkit-api-ref`
- page_type: `leaf`
- content_type: ``

### Specifying a Timeout for a Test (Unit Test Framework Toolkit)

Complete the following steps to specify a timeout for a test.

1. Open the LabVIEW project that contains the files on which you want to perform unit testing.
2. Double-click a .lvtest file to display the Test Properties dialog box.
3. Select Advanced from the Category list to display the Advanced page.
4. Place a checkmark in the Set timeout checkbox.
5. Use the Timeout control to specify a timeout, in seconds.
 [IMAGE alt='image' src='note.gif']
**Note** Use timeout for tests of VIs that loop forever or require you to perform any tasks manually.
6. Click the OK button to close the dialog box and return to the Project Explorer window.
7. Select File»Save to save the project.

The next time you execute this test, LabVIEW runs the VI under test. If the VI under test times out during execution, LabVIEW stops the VI and test results show this test as failed.

<!--NI_TOPIC bundle=labview-unit-test-framework-toolkit-api-ref path=lvutfhowto/utfh_vctr_in_test.html language=enus -->
## TOPIC 00065: Assigning Test Vectors in Test Cases (Unit Test Framework Toolkit)

- bundle_id: `labview-unit-test-framework-toolkit-api-ref`
- source_path: `lvutfhowto/utfh_vctr_in_test.html`
- source_url: https://docs-be.ni.com/bundle/labview-unit-test-framework-toolkit-api-ref/raw/resource/enus/lvutfhowto/utfh_vctr_in_test.html
- document_id: `labview-unit-test-framework-toolkit-api-ref`
- page_type: `leaf`
- content_type: ``

### Assigning Test Vectors in Test Cases (Unit Test Framework Toolkit)

Complete the following steps to use a test vector in a unit test.

1. In the Project Explorer window, double-click a .lvtest file to display the Test Properties dialog box.
2. Select Test Vectors from the Category list to display the Test Vectors page.
3. Click the Add button. A file dialog box appears.
4. Locate and select the test vector file that you want to add in this file dialog box and click the OK button to add this test vector file to the Test Vector Files list.
5. Select Test Cases from the Category list to display the Test Cases page.
6. Right-click the input or output terminal that you want to assign a test vector and select Assign Test Vector from the shortcut menu. The Input Value cell or Expected Value cell displays No Vector .
7. Select the test vector you want to use from the pull-down menu in the Input Value cell or Expected Value cell.
8. (Optional) Use indexes for test vectors assigned to inputs. Right-click the test vector and select Assign Index»New Index to create an index and assign this index to the test vector. You also can assign existing indexes to a test vector by selecting an existing index under Assign Index . Select Assign Index»No Index to remove an index from a test vector.
 [IMAGE alt='image' src='note.gif']
**Note** You cannot use indexes for test vectors assigned to output terminals.
9. Click the OK button to close the Test Properties dialog box and apply the change.

Refer to the labview\examples\Unit Test Framework\Assign Vector to Expected Value\Assign Vector to Expected Value.lvproj directory for an example that demonstrates how to assign test vectors to output terminals.

##### Related Information

[Using Test Vector Indexes](../lvutfconcepts/utfc_test_vector.html#index)
