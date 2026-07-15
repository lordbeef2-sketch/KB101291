# NI DOCUMENT BUNDLE: lvutf-api-ref

<!--NI_BUNDLE_CHUNK bundle=lvutf-api-ref start=1 end=20 -->
<!--NI_TOPIC bundle=lvutf-api-ref path=dialog-boxes/advanced-page-test-properties-dialog-box.html language=enus -->
## TOPIC 00001: Advanced Page (Test Properties Dialog Box)

- bundle_id: `lvutf-api-ref`
- source_path: `dialog-boxes/advanced-page-test-properties-dialog-box.html`
- source_url: https://docs-be.ni.com/bundle/lvutf-api-ref/raw/resource/enus/dialog-boxes/advanced-page-test-properties-dialog-box.html
- document_id: `lvutf-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Requires: Unit Test Framework Toolkit Select Advanced from the Category list of the Test Properties dialog box to display this page. Use this page to configure the settings related to the execution of a test, including the timeout, minimum code coverage requirement, number of times to repeat a test,

### Advanced Page (Test Properties Dialog Box)

**Requires:** Unit Test Framework Toolkit

Select **Advanced** from the **Category** list of the [Test Properties](/csh?context=lvmnt_utf_lvutf_utf_properties_db) dialog box to display this page.

minimum code coverage requirement

Note

.lvtest

Unit Test Framework

Project Properties

This page includes the following components:

- Execution —Configures the settings related to executing a test.
  - Digits of precision for floating-point comparison —Specifies the number of digits after the decimal separator that LabVIEW uses for comparing floating-point values. Valid values are 0-32. The default is 6.
  - Repetitions —Specifies the number of times that LabVIEW repeats the test. The default is 1.
  - Set timeout (s) —Specifies whether to set a timeout, in seconds, for the test during test execution. For example, you can set a timeout for tests of VIs that loop forever or require you to perform tasks manually. If the VI under test times out during execution, LabVIEW stops the VI and test results show this test as failed. By default, this checkbox does not contain a checkmark.
    - Timeout —Specifies the time limit, in seconds, in which LabVIEW must complete the test execution. If you place a checkmark in the Set timeout checkbox, the default is 0.
  - Set minimum code coverage (%) —Specifies whether to set a minimum code coverage requirement, in percent, for the VI under test during test execution. If the VI under test does not meet the minimum code coverage requirement during test execution, test results show this test as failed. By default, this checkbox does not contain a checkmark.
    - Code coverage —Specifies the percentage of subdiagrams LabVIEW must execute during test execution. If you place a checkmark in the Set minimum code coverage checkbox, the default is 100.
  - Automatic error handling —Specifies whether to automatically handle errors for the VI under test, setup VI, and teardown VI during test execution. This control takes effect only on VIs during test execution instead of changing the specifications in the VIs. You can select from the following options:
    - As is —Enables or disables automatic error handling as a VI specified. This is the default option.
    - Enable automatic error handling —Suspends test execution, highlights the subVI or function where the error occurred, and displays an error dialog box for any error that occurs when running a VI during test execution.
    - Disable automatic error handling —Continues to run a VI when an error occurs during test execution.
  - Disable breakpoints —Specifies whether to toggle test execution suspension at a breakpoint. By default, the test continues when LabVIEW reaches a breakpoint. This option takes effect only on the VI under test, setup VI, and teardown VI during test execution instead of changing the specifications in the VI.
- Configuration —Specifies the settings related to configuring the VI under test, setup VI, and teardown VI .
  - Input/output values —Specifies which controls and indicators of the VI under test appear on the Test Cases page of the Test Properties dialog box. You can select from the following options:
    - Include controls and indicators from connector pane (Default)—Displays the controls from the connector pane of the VI under test and setup VI as input and displays the indicators from the connector pane of the VI under test and teardown VI as output. You must select a connector pane pattern and assign terminals for the VI under test. National Instruments recommends this option when executing a test on a real-time (RT) target. Doing so avoids test errors that result if the RT target cannot find an input or output.
    - Include controls and indicators from front panel —Displays the controls from the front panel of the VI under test as input and displays the indicators from the front panel of the VI under test as output.
    - Include controls and indicators from front panel as both input and output —Displays the controls and indicators from the front panel of the VI under test as both input and output.
  - Capture input values —Specifies whether to capture the default input values from the VI under test when creating a test. By default, this checkbox contains a checkmark.
  - Capture output values —Specifies whether to capture the default output values from the VI under test when creating a test. By default, this checkbox contains a checkmark.
  - Decimal separator —Specifies the character LabVIEW uses to separate the integral and fractional parts of a decimal number. Use a period (.) or a comma (,). The default is a period.
  - Maximum array elements —Specifies the maximum number of array elements that LabVIEW lists on the Test Cases page of the Test Properties dialog box. If an array contains more elements than the specified number, LabVIEW lists the array as one item. The default is 100.
 Note If you change the **Maximum array elements**, you need to update each test case by clicking the **Import Values from VI** button on the [Test Cases](/csh?context=lvmnt_utf_lvutf_utf_test_cases_db) page.

<!--NI_TOPIC bundle=lvutf-api-ref path=dialog-boxes/configuration-page-test-properties-dialog-box.html language=enus -->
## TOPIC 00002: Configuration Page (Test Properties Dialog Box)

- bundle_id: `lvutf-api-ref`
- source_path: `dialog-boxes/configuration-page-test-properties-dialog-box.html`
- source_url: https://docs-be.ni.com/bundle/lvutf-api-ref/raw/resource/enus/dialog-boxes/configuration-page-test-properties-dialog-box.html
- document_id: `lvutf-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Requires: Unit Test Framework Toolkit Select Configuration from the Category list of the Test Properties dialog box to display this page. Use this page to configure the basic settings of a test, including path to the VI under test, comment, test priority, and requirement IDs. You also can configure

### Configuration Page (Test Properties Dialog Box)

**Requires:** Unit Test Framework Toolkit

Select **Configuration** from the **Category** list of the [Test Properties](/csh?context=lvmnt_utf_lvutf_utf_properties_db) dialog box to display this page.

Use this page to [configure](/csh?context=lvmnt_utf_lvutfhowto_utfh_configure) the basic settings of a test, including path to the VI under test, comment, [test priority](/csh?context=lvmnt_utf_lvutfconcepts_utfc_test_priority), and [requirement IDs](/csh?context=lvmnt_utf_lvutfconcepts_utfc_test_require). You also can [configure a test to skip](/csh?context=lvmnt_utf_lvutfhowto_utfh_configure_test_skip) during execution and [configure a test to use a user-defined test VI](/csh?context=lvmnt_utf_lvutfhowto_utfh_configure_ud_test_vi).

This page includes the following components:

- Test Name —Displays the full path to the .lvtest file.
- VI under Test —Specifies the path to the VI that LabVIEW checks for functional correctness.
 Note You can specify only one VI under test for each .lvtest file.
- Test Priority —Specifies the priority of the test. This priority determines whether LabVIEW executes the test when you execute tests by priority . The highest priority is 1000, and the lowest priority is 0. The default is 5.
- Comment —Specifies optional comments about the test.
- Requirement ID —Specifies the requirement IDs for integration with NI Requirements Gateway.
- Skip Test —Specifies the settings related to skipping the test when executing tests.
  - Always skip this test —Specifies whether LabVIEW skips the test when executing tests interactively, programmatically, or both. By default, this checkbox does not contain a checkmark.
    - Project Explorer window —Specifies whether LabVIEW skips the test when executing tests interactively from the Project Explorer window. This checkbox contains a checkmark by default when you place a checkmark in the Always skip this test checkbox.
    - Unit Test Framework VIs —Specifies whether LabVIEW skips the test when executing tests programmatically by using the Unit Test Framework VIs. This checkbox contains a checkmark by default when you place a checkmark in the Always skip this test checkbox.
- Test VI —Specifies the user-defined test VI LabVIEW uses to execute the test.
  - Use user-defined test VI —Specifies whether to use a user-defined test VI to execute the test. When you place a checkmark in the Use user-defined test VI checkbox, LabVIEW dims the Test Cases page and the Setup/Teardown page of the Test Properties dialog box.
  - User-defined test VI file path —Specifies the path to the user-defined test VI LabVIEW uses to execute the test.

<!--NI_TOPIC bundle=lvutf-api-ref path=dialog-boxes/rearrange-test-cases-dialog-box-test-properties-dialog-box.html language=enus -->
## TOPIC 00003: Rearrange Test Cases Dialog Box (Test Properties Dialog Box)

- bundle_id: `lvutf-api-ref`
- source_path: `dialog-boxes/rearrange-test-cases-dialog-box-test-properties-dialog-box.html`
- source_url: https://docs-be.ni.com/bundle/lvutf-api-ref/raw/resource/enus/dialog-boxes/rearrange-test-cases-dialog-box-test-properties-dialog-box.html
- document_id: `lvutf-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Requires: Unit Test Framework Toolkit In the Test Cases page of the Test Properties dialog box, click the Rearrange button to display this dialog box. Use the buttons in the right of this dialog box or drag the test cases in the Test Case List to change the order of test cases. Test Case List—Lists

### Rearrange Test Cases Dialog Box (Test Properties Dialog Box)

**Requires:** Unit Test Framework Toolkit

In the [Test Cases](/csh?context=lvmnt_utf_lvutf_utf_test_cases_db) page of the [Test Properties](/csh?context=lvmnt_utf_lvutf_utf_properties_db) dialog box, click the **Rearrange** button to display this dialog box.

Use the buttons in the right of this dialog box or drag the test cases in the **Test Case List** to change the order of test cases.

- Test Case List —Lists all the test cases in the project.
- Move to Top —Moves the test case you select to the top of the Test Case List .
- Move Up —Moves the test case you select up in the Test Case List .
- Move Down —Moves the test case you select down in the Test Case List .
- Move to Bottom —Moves the test case you select to the bottom of the Test Case List .

<!--NI_TOPIC bundle=lvutf-api-ref path=dialog-boxes/setup-teardown-page-test-properties-dialog-box.html language=enus -->
## TOPIC 00004: Setup/Teardown Page (Test Properties Dialog Box)

- bundle_id: `lvutf-api-ref`
- source_path: `dialog-boxes/setup-teardown-page-test-properties-dialog-box.html`
- source_url: https://docs-be.ni.com/bundle/lvutf-api-ref/raw/resource/enus/dialog-boxes/setup-teardown-page-test-properties-dialog-box.html
- document_id: `lvutf-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Requires: Unit Test Framework Toolkit Select Setup/Teardown from the Category list of the Test Properties dialog box to display this page. Use this page to configure the setup and teardown VIs to run before and after executing a test. This page includes the following components: Setup VI—Specifies t

### Setup/Teardown Page (Test Properties Dialog Box)

**Requires:** Unit Test Framework Toolkit

Select **Setup/Teardown** from the **Category** list of the [Test Properties](/csh?context=lvmnt_utf_lvutf_utf_properties_db) dialog box to display this page.

Use this page to [configure](/csh?context=lvmnt_utf_lvutfhowto_utfh_config_set_tear) the [setup and teardown VIs](/csh?context=lvmnt_utf_lvutfconcepts_utfc_set_tear) to run before and after executing a test.

This page includes the following components:

- Setup VI —Specifies the path to the VI that LabVIEW runs before executing the test.
- Setup VI Table —Assigns the outputs of the setup VI to the inputs of the VI under test. When you execute the test, LabVIEW first runs the setup VI and then passes the output values from the setup VI to the inputs of the VI under test.
 Note You must [configure the connector pane](/csh?context=lvcore_lvhowto_assigning_controls_and_ind) of the setup VI before you can use the setup VI in tests.
  - Inputs of VI under Test —Displays all the inputs of the VI under test.
  - Outputs of Setup VI —Specifies the output of the setup VI that you want to pass value to each input of the VI under test. You can assign the inputs of the setup VI on the Test Cases page of the Test Properties dialog box.
- Teardown VI —Specifies the path to the VI that LabVIEW runs after executing the test.
- Teardown VI Table —Assigns the outputs of the VI under test to the inputs of the teardown VI. When you execute the test, LabVIEW runs the VI under test and then passes the resulting values from the VI under test to the inputs of the teardown VI.
 Note You must configure the connector pane of the teardown VI before you can use the teardown VI in tests.
  - Outputs of VI under Test —Displays all the outputs of the VI under test.
  - Inputs of Teardown VI —Specifies the input of the teardown VI for each output of the VI under test that you want to pass values to. You can assign the expected output values and comparison types of the teardown VI on the Test Cases page of the Test Properties dialog box. Note If the teardown VI has an **error out** indicator, and the indicator contains an error, LabVIEW lists this test on the **Test Errors** page of the [Unit Test Framework Results](/csh?context=lvmnt_utf_lvutf_utf_results_db) window instead of the **Test Results** page.

<!--NI_TOPIC bundle=lvutf-api-ref path=dialog-boxes/test-cases-page-test-properties-dialog-box.html language=enus -->
## TOPIC 00005: Test Cases Page (Test Properties Dialog Box)

- bundle_id: `lvutf-api-ref`
- source_path: `dialog-boxes/test-cases-page-test-properties-dialog-box.html`
- source_url: https://docs-be.ni.com/bundle/lvutf-api-ref/raw/resource/enus/dialog-boxes/test-cases-page-test-properties-dialog-box.html
- document_id: `lvutf-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Requires: Unit Test Framework Toolkit Select Test Cases from the Category list of the Test Properties dialog box to display this page. Use this page to configure the settings for each test case, including the input values, expected values, and comparison types. LabVIEW lists the controls and indicat

### Test Cases Page (Test Properties Dialog Box)

**Requires:** Unit Test Framework Toolkit

Select **Test Cases** from the **Category** list of the [Test Properties](/csh?context=lvmnt_utf_lvutf_utf_properties_db) dialog box to display this page.

test case

comparison types

Note

Input/output values setting

Unit Test Framework

Project Properties

Include controls and indicators from connector pane

select a connector pane pattern

assign the terminals

This page includes the following components:

- Test Case —Specifies the test case you want to display and configure. Use this control to switch between test cases. You also can use this control to rename test cases.
- New —Creates a new test case.
- Duplicate —Duplicates the current test case.
- Delete —Deletes the current test case. A test file must have at least one test case. If you click the Delete button on the only test case, LabVIEW resets the input values, expected values, and comparison types.
- Run —Executes the current test case.
- Export Values to VI — Exports the input and expected values of the current test case to the corresponding terminals of the VI under test, setup VI, and teardown VI. Note If the VI under test is a [reentrant VI](/csh?context=lvcore_lvconcepts_suggestions_for_exec) and no clones of the VI under test are in memory, **Export Values to VI** exports the values to the VI under test. If exactly one clone of the VI under test is in memory, **Export Values to VI** exports the values to that clone VI. If multiple clones of the VI under test are in memory, LabVIEW prompts you to choose a clone VI to export values to.
- Import Values from VI — Imports the input and expected values from the VI under test, setup VI, and teardown VI to the corresponding terminals of the current test case. Note If the VI under test is a [reentrant VI](/csh?context=lvcore_lvconcepts_suggestions_for_exec) and no clones of the VI under test are in memory, **Import Values from VI** imports the values from the VI under test. If exactly one clone of the VI under test is in memory, **Import Values from VI** imports the values from the clone VI. If multiple clones of the VI under test are in memory, LabVIEW prompts you to choose a clone VI to import values from.
- Rearrange —Displays the Rearrange Test Cases dialog box. Use this dialog box to change the order of test cases.
- Update —Updates the inputs and outputs of each test case. If you modify a VI after creating a test, the Update button updates the inputs and outputs of the VI on this page. Refer to the KnowledgeBase at ni.com for more information about when LabVIEW applies original values and comparison types.
- Connector Pane Image —Displays the connector pane image of the VI under test.
- Comment —Adds a comment to the current test case.
- Input Values Table —Lists the name, data type, and input value of each control for the current test case.
  - Input Name —Displays the names of each control from the VI under test and from the setup VI . Note LabVIEW displays arrays and clusters as trees. Expand each tree to view the individual elements.
  - Input Name Checkbox —Specifies whether to use the value you specify in the Input Value of each control during test execution. If you remove the checkmark from an input terminal, LabVIEW uses the default value for front panel controls and the current values for global variables and shared variables during test execution.
  - Data Type —Displays the data type of the corresponding control or indicator.
  - Input Value —Specifies the input value or test vector LabVIEW uses for each control during test execution.
- Expected Values Table —Lists the name, data type, comparison type, and expected value of each indicator for the current test case.
  - Output Name —Displays the name of each indicator from the VI under test and from the teardown VI .
 Note LabVIEW displays arrays and clusters as trees. Expand each tree to view the individual elements.
  - Output Name Checkbox —Specifies whether to check each indicator for functional correctness during test execution. If you remove the checkmark from an output terminal, LabVIEW does not check the corresponding indicators.
  - Data Type —Displays the data type of the corresponding control or indicator.
  - Comparison —Specifies the comparison type LabVIEW uses to compare the resulting value of each indicator with the expected value.
  - Expected Value —Specifies the indicator value or test vector that LabVIEW uses to compare with the corresponding resulting values.

Note

[…]

Export Values to VI

Import Values from VI

<!--NI_TOPIC bundle=lvutf-api-ref path=dialog-boxes/test-properties-dialog-box.html language=enus -->
## TOPIC 00006: Test Properties Dialog Box

- bundle_id: `lvutf-api-ref`
- source_path: `dialog-boxes/test-properties-dialog-box.html`
- source_url: https://docs-be.ni.com/bundle/lvutf-api-ref/raw/resource/enus/dialog-boxes/test-properties-dialog-box.html
- document_id: `lvutf-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Requires: Unit Test Framework Toolkit In the Project Explorer window, right-click a .lvtest file and select Properties from the shortcut menu to display this dialog box. You also can double-click the .lvtest file to display this dialog box. Use this dialog box to configure a test. Use the Category l

### Test Properties Dialog Box

**Requires:** Unit Test Framework Toolkit

In the [Project Explorer](/csh?context=lvcore_lvconcepts_using_labview_projects) window, right-click a [.lvtest file](/csh?context=lvmnt_utf_lvutfconcepts_utfc_test_config) and select **Properties** from the shortcut menu to display this dialog box. You also can double-click the .lvtest file to display this dialog box.

Use this dialog box to [configure a test](/csh?context=lvmnt_utf_lvutfhowto_utfh_configure).

Use the **Category** list at the left side of the dialog box to access the following options:

- Configuration —Configures the basic settings of a test.
- Test Cases —Configures the settings for each test case .
- Setup/Teardown — Configures the settings for running setup and teardown VIs .
- Test Vectors — Configures test vector files that a test contains.
- Advanced — Configures the advanced settings related to configuring and executing a test.

<!--NI_TOPIC bundle=lvutf-api-ref path=dialog-boxes/test-vector-file-properties-dialog-box.html language=enus -->
## TOPIC 00007: Test Vector File Properties Dialog Box

- bundle_id: `lvutf-api-ref`
- source_path: `dialog-boxes/test-vector-file-properties-dialog-box.html`
- source_url: https://docs-be.ni.com/bundle/lvutf-api-ref/raw/resource/enus/dialog-boxes/test-vector-file-properties-dialog-box.html
- document_id: `lvutf-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Requires: Unit Test Framework Toolkit In the Project Explorer window, double-click a .lvvect file to display the dialog box. You also can right-click a .lvvect file and select Properties to display this dialog box. Use this dialog box to manage test vectors in a test vector file. You can create new

### Test Vector File Properties Dialog Box

**Requires:** Unit Test Framework Toolkit

In the [Project Explorer](/csh?context=lvcore_lvconcepts_using_labview_projects) window, double-click a .lvvect file to display the dialog box. You also can right-click a .lvvect file and select **Properties** to display this dialog box.

Use this dialog box to manage test vectors in a test vector file. You can create new test vectors or delete existing test vectors. You also can add other test vector files to or remove other test vector files from this test vector file.

This page includes the following components:

- Included Test Vector Files —Lists the test vector files that this test vector file includes. The Test Vectors list displays the test vectors of the included test vector files. You can use these test vector files in a test.
- Add —Adds a test vector file to the Included Test Vector Files list.
- Remove —Removes a test vector file from the Included Test Vector Files list.
- Test Vectors —Lists all test vectors in this test vector file and included test vector files.
- New —Creates a test vector and add this test vector to the Test Vectors list.
- Delete —Removes a test vector from the Test Vectors list. You cannot delete a test vector that belongs to an included test vector file.
- Move Up —Moves the selected test vector up in the Test Vectors list. You cannot move a test vector that belongs to an included test vector file.
- Move Down —Moves the selected test vector down in the Test Vectors list. You cannot move a test vector that belongs to an included test vector file.
- Edit Values —Displays the Test Vector Properties - Edit dialog box. Use this dialog box to edit test vectors . You cannot edit a test vector that belongs to an included test vector file.

<!--NI_TOPIC bundle=lvutf-api-ref path=dialog-boxes/test-vector-properties-edit-dialog-box.html language=enus -->
## TOPIC 00008: Test Vector Properties - Edit Dialog Box

- bundle_id: `lvutf-api-ref`
- source_path: `dialog-boxes/test-vector-properties-edit-dialog-box.html`
- source_url: https://docs-be.ni.com/bundle/lvutf-api-ref/raw/resource/enus/dialog-boxes/test-vector-properties-edit-dialog-box.html
- document_id: `lvutf-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Requires: Unit Test Framework Toolkit In the Test Vector Properties dialog box, click the Edit Values button or double-click a test vector to display this dialog box. Use this dialog box to configure properties of test vectors. This dialog box contains the following components: Test Vector Values—Li

### Test Vector Properties - Edit Dialog Box

**Requires:** Unit Test Framework Toolkit

In the [Test Vector Properties](/csh?context=lvmnt_utf_lvutf_utf_vect_prop_db) dialog box, click the **Edit Values** button or double-click a test vector to display this dialog box.

Use this dialog box to configure properties of test vectors.

This dialog box contains the following components:

- Test Vector Values —Lists the following properties of test vectors in a test vector file .
  - Name —Specifies the name of the test vector.
  - Data Type —Specifies the data type of the test vector. A test vector does not support the Array or Cluster data type but you can assign test vectors to elements of array or cluster controls of the VI under test, setup VI, or teardown VI on the Test Cases page of the Test Properties dialog box.
  - Vector File —Specifies the test vector file that contains the test vector.
  - Append to —Specifies the name and the test vector file of another test vector. LabVIEW adds the values of the specified test vector to the beginning of the current test vector and moves the original values of the current test vector after these new values. You cannot edit these new values or change the order of these new values.
  - Requirement ID —Specifies the requirement ID of this test vector to use this test vector with NI Requirements Gateway.
  - Edit Type —Specifies the type of the test vector .
  - Value —Specifies the values of the test vector. You can enter new values in cells below the existing values. You also can press <Tab> to move to the value in the next cell or press <shift-Tab> to switch to the value in the previous cell.
- Export —Displays the Test Vector Properties - Export dialog box. Use this dialog box to export values of a test vector to an array control.
- Import —Displays the Test Vector Properties - Import dialog box. Use this dialog box to import values from an array control to a test vector.

<!--NI_TOPIC bundle=lvutf-api-ref path=dialog-boxes/test-vector-properties-export-dialog-box.html language=enus -->
## TOPIC 00009: Test Vector Properties - Export Dialog Box

- bundle_id: `lvutf-api-ref`
- source_path: `dialog-boxes/test-vector-properties-export-dialog-box.html`
- source_url: https://docs-be.ni.com/bundle/lvutf-api-ref/raw/resource/enus/dialog-boxes/test-vector-properties-export-dialog-box.html
- document_id: `lvutf-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Requires: Unit Test Framework Toolkit In the Test Vector Properties - Edit dialog box, click the Export button to display this dialog box. Use this dialog box to export values of a test vector to an array control with a proper data type. This dialog box contains the following components: Test Vector

### Test Vector Properties - Export Dialog Box

**Requires:** Unit Test Framework Toolkit

In the [Test Vector Properties - Edit](/csh?context=lvmnt_utf_lvutf_utf_vect_edit_db) dialog box, click the **Export** button to display this dialog box.

Use this dialog box to [export values of a test vector](/csh?context=lvmnt_utf_lvutfhowto_utfh_expt_impt_vctr) to an array control with a [proper data type](/csh?context=lvmnt_utf_lvutfhowto_utfh_expt_impt_vctr).

This dialog box contains the following components:

- Test Vectors —Lists test vectors in the current test vector file. You can export values of these test vectors to an array control in the Target Controls list. The Test Vectors list does not display test vectors that belong to an included test vector file.
- Target VIs —Lists the VIs that are open in LabVIEW.
- Ignore VIs in vi.lib —Specifies whether the Target VIs list ignores VIs that are in the vi.lib directory. By default, this checkbox contains a checkmark.
- Target Controls —Lists array controls to which you can export the test vector values. After you select the test vector from the Test Vectors list and the target VI from the Target VIs list, the Target Controls list displays the array controls that belong to the target VI and have proper data types.

<!--NI_TOPIC bundle=lvutf-api-ref path=dialog-boxes/test-vector-properties-import-dialog-box.html language=enus -->
## TOPIC 00010: Test Vector Properties - Import Dialog Box

- bundle_id: `lvutf-api-ref`
- source_path: `dialog-boxes/test-vector-properties-import-dialog-box.html`
- source_url: https://docs-be.ni.com/bundle/lvutf-api-ref/raw/resource/enus/dialog-boxes/test-vector-properties-import-dialog-box.html
- document_id: `lvutf-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Requires: Unit Test Framework Toolkit In the Test Vector Properties - Edit dialog box, click the Import button to display this dialog box. Use this dialog box to import values from an array control to a test vector with a proper data type. This dialog box contains the following components: Source VI

### Test Vector Properties - Import Dialog Box

**Requires:** Unit Test Framework Toolkit

In the [Test Vector Properties - Edit](/csh?context=lvmnt_utf_lvutf_utf_vect_edit_db) dialog box, click the **Import** button to display this dialog box.

Use this dialog box to [import values from an array control](/csh?context=lvmnt_utf_lvutfhowto_utfh_expt_impt_vctr) to a test vector with a [proper data type](/csh?context=lvmnt_utf_lvutfhowto_utfh_expt_impt_vctr).

This dialog box contains the following components:

- Source VIs —Lists VIs that are open in LabVIEW.
- Ignore VIs in vi.lib —Specifies whether the Source VIs list ignores VIs that are in the vi.lib directory. By default, this checkbox contains a checkmark.
- Source Controls —Lists array controls of the VI that you select from the Source VIs list. You can import values from these array controls to a test vector in the Target Test Vectors list.
- Target Test Vectors —Lists test vectors to which you can import values from an array control. After you select the source control from the Source Controls list, the Target Test Vectors list displays test vectors that have proper data types. This list does not display test vectors that belong to an included test vector file.

<!--NI_TOPIC bundle=lvutf-api-ref path=dialog-boxes/test-vectors-page-test-properties-dialog-box.html language=enus -->
## TOPIC 00011: Test Vectors Page (Test Properties Dialog Box)

- bundle_id: `lvutf-api-ref`
- source_path: `dialog-boxes/test-vectors-page-test-properties-dialog-box.html`
- source_url: https://docs-be.ni.com/bundle/lvutf-api-ref/raw/resource/enus/dialog-boxes/test-vectors-page-test-properties-dialog-box.html
- document_id: `lvutf-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Requires: Unit Test Framework Toolkit Select Test Vectors from the Category list of the Test Properties dialog box to display this page. Use this page to configure test vector files that a test contains. You can add test vector files to or remove test vector files from this test. This page includes

### Test Vectors Page (Test Properties Dialog Box)

**Requires:** Unit Test Framework Toolkit

Select **Test Vectors** from the **Category** list of the [Test Properties](/csh?context=lvmnt_utf_lvutf_utf_properties_db) dialog box to display this page.

Use this page to configure [test vector files](/csh?context=lvmnt_utf_lvutfconcepts_utfc_test_vector) that a test contains. You can [add](/csh?context=lvmnt_utf_lvutfhowto_utfh_vctr_in_test) test vector files to or remove test vector files from this test.

This page includes the following components:

- Test Vector Files -Lists test vector files that this test contains. You must add test vector files to this test before assigning test vectors to the inputs or outputs of the VI under test.
- Add -Adds a test vector file to the Test Vector Files list.
- Remove -Removes a test vector file from the Test Vector Files list.
- Test Vectors -Lists test vectors that belongs to the test vector files in the Test Vector Files list.
 Note This list does not display test vectors that belong to included test vector files.
- Move Left -Moves the selected test vector left in the Test Vectors list.
- Move Right -Moves the selected test vector right in the Test Vectors list.

<!--NI_TOPIC bundle=lvutf-api-ref path=dialog-boxes/unit-test-framework-page-project-properties-dialog-box.html language=enus -->
## TOPIC 00012: Unit Test Framework Page (Project Properties Dialog Box)

- bundle_id: `lvutf-api-ref`
- source_path: `dialog-boxes/unit-test-framework-page-project-properties-dialog-box.html`
- source_url: https://docs-be.ni.com/bundle/lvutf-api-ref/raw/resource/enus/dialog-boxes/unit-test-framework-page-project-properties-dialog-box.html
- document_id: `lvutf-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Requires: Unit Test Framework Toolkit In the Project Explorer window, select Project»Properties to display the Project Properties dialog box. Select Unit Test Framework from the Category list to display this page. Use this dialog box to configure the testing options of a LabVIEW project. This page i

### Unit Test Framework Page (Project Properties Dialog Box)

**Requires:** Unit Test Framework Toolkit

In the [Project Explorer](/csh?context=lvcore_lvconcepts_using_labview_projects) window, select **Project»Properties** to display the [Project Properties](/csh?context=lvcore_lvdialog_project_properties) dialog box. Select **Unit Test Framework** from the **Category** list to display this page.

Use this dialog box to configure the testing options of a LabVIEW project.

This page includes the following components:

- Filters —Specifies the types of filters to use when executing tests in a LabVIEW project, including executing tests by priority and modified tests .
  - Minimum priority —Specifies whether to execute only tests with a minimum test priority . If the Minimum priority checkbox contains a checkmark, LabVIEW executes only tests with an equal or higher priority than the Test priority you specified. By default, this checkbox does not contain a checkmark.
    - Test priority —Specifies the minimum priority of tests to execute. The highest priority is 1000, and the lowest priority is 0. The default is 5.
  - Modified tests and VIs —Specifies whether to execute only tests that have been modified since a specified time. By default, this checkbox does not contain a checkmark.
    - Last test execution —Specifies whether to execute only tests and VIs that have been modified since the last test execution.
 Note You must configure the LabVIEW Unit Test Framework Toolkit to [generate a test status log](/csh?context=lvmnt_utf_lvutfhowto_utfh_report_log) before you can use this filter.
    - Timestamp —Specifies whether to execute only tests and VIs that have been modified since a given date and time.
      - Date/time —Specifies the date and time after which LabVIEW checks to see if tests and VIs have been modified.
    - Last N days —Specifies whether to execute only tests and VIs that have been modified in the last N days, where N is the number you specify using the N control.
      - N —Specifies the number of days after which LabVIEW checks for tests and VIs that have been modified. The default is 1.
    - Include tests of all caller VIs —Specifies whether to execute tests of all VIs that call any of the modified VIs. By default, this checkbox does not contain a checkmark.
- Generate Reports —Specifies the types of reports LabVIEW generates after test execution.
  - ATML/XML Report —Specifies the settings related to generating a report in Automatic Test Markup Language (ATML) format.
    - Generate ATML/XML report —Specifies whether LabVIEW generates a report in ATML format.
      - ATML/XML report file path —Specifies the path to the ATML file where LabVIEW generates this report.
 Note By default, LabVIEW generates this report in the same directory as the project.
      - View report after execution —Specifies whether to display this report after test execution.
  - HTML Report —Specifies settings related to generating a report in HTML format.
    - Generate HTML report —Specifies whether LabVIEW generates a report in HTML format.
      - HTML report file path —Specifies the path to the HTML file where LabVIEW generates this report.
 Note By default, LabVIEW generates this report in the same directory as the project.
      - Use user-defined CSS file —Specifies whether to use a user-defined Cascading Style Sheet (CSS) file to format HTML reports.
        - CSS file path —Specifies the path to the CSS file.
      - View report after execution —Specifies whether to display this report after test execution.
  - ASCII Report —Specifies the settings related to generating a report in ASCII format.
    - Generate ASCII report —Specifies whether LabVIEW generates a report in ASCII format.
      - ASCII report file path —Specifies the path to the ASCII file where LabVIEW generates this test report.
 Note By default, LabVIEW generates this report in the same directory as the project.
      - View report after execution —Specifies whether to display this report after test execution.
- Report Details —Specifies the contents of the test reports . Note You must specify a report type in the **Generate Reports** section to use this section.
  - Report Contents —Specifies the contents of the test reports.
    - Summary data —Includes a summary of the number of tests that passed, failed, were skipped, or produced errors. By default, this checkbox contains a checkmark.
    - Failed tests —Includes information about tests that failed. By default, this checkbox contains a checkmark.
      - Include details —Includes detailed information about this type of test results, such as the path to the VI under test, test status, execution time, and test case results. By default, this checkbox does not contain a checkmark.
    - Passed tests —Includes information about tests that passed. By default, this checkbox contains a checkmark.
      - Include details —Includes detailed information about this type of test results, such as the path to the VI under test, test status, execution time, and test case results. By default, this checkbox does not contain a checkmark.
    - Skipped tests —Includes information about tests that LabVIEW skipped. By default, this checkbox contains a checkmark.
    - Errors —Includes information about errors that occurred during test execution. By default, this checkbox contains a checkmark.
      - Include details —Includes detailed information about this type of test results, such as the path to the VI under test, test status, execution time, and test case results. By default, this checkbox does not contain a checkmark.
  - Display By —Specifies whether to display the test results according to the names of the tests or names of the VIs. The default is to display by the test name.
    - VI name —Displays the results according to the names of the VIs.
    - Test name —Displays the results according to the names of the tests.
- Generate Log Files —Specifies the types of log files LabVIEW generates during test execution.
  - Test Status —Specifies settings related to generating a test status log file.
    - Log test status —Specifies whether to generate a test status log file during test execution. This log file contains information about the most recent test execution and results. During execution, LabVIEW logs the test names, times of execution, durations of execution, and whether the tests passed ( 1 ), failed ( 0 ), produced errors ( 2 ), or were skipped ( 3 ). By default, this checkbox does not contain a checkmark.
 Note LabVIEW uses the information in this log file to determine which tests to execute when you [execute tests that have been modified](/csh?context=lvmnt_utf_lvutfhowto_utfh_execute_mod) since the last execution. You must generate this log file in order to execute only modified tests.
      - Test status log file path —Specifies the path to the file where LabVIEW saves this log file.
 Note By default, LabVIEW generates this log file in the same directory as the project.
  - Test Execution —Specifies settings related to generating a test execution log file.
    - Log test execution —Specifies whether to generate a test execution log file during test execution. This log file contains information about the previous test execution(s). During execution, LabVIEW logs the entire execution process, including the test path, VI path, time of execution, running setup and teardown VIs, code coverage measurement, and test cases results. You can use this log file to troubleshoot tests that timed out, produced errors, or did not complete. By default, this checkbox does not contain a checkmark.
 Note If you place a checkmark in this checkbox, LabVIEW appends the details of each subsequent execution to the existing log file unless you place a checkmark in the **Overwrite log file** checkbox or change the log file name.
      - Test execution log file path —Specifies the path to the file where LabVIEW saves this log file.
 Note By default, LabVIEW generates this log file in the same directory as the project.
      - Overwrite log file —Specifies whether LabVIEW overwrites this log file during every execution. If you place a checkmark in this checkbox, LabVIEW replaces the existing log file with details from the current execution. By default, this checkbox does not contain a checkmark.
- Test Creation —Specifies the settings related to creating .lvtest and .lvvect files.
  - Test File and Test Vector File Location —Specifies the settings related to the default location where LabVIEW saves new .lvtest and .lvvect files.
    - Change default location —Specifies whether to change the default location where LabVIEW saves new .lvtest and .lvvect files. By default, this checkbox does not contain a checkmark, and LabVIEW saves new .lvtest and .lvvect files in the same directory as the VIs under test.
      - Default location file path —Specifies the default directory where LabVIEW saves new .lvtest and .lvvect files.
 Note If you specify a location in the same disk drive that contains the project under test, this control displays a relative path. Otherwise, this control displays an absolute path, which describes the location starting from the top level of the file system.
  - External Editor —Specifies the settings related to editing .lvtest and .lvvect files.
    - Change default editor —Specifies whether to change the default editor LabVIEW uses to edit .lvtest and .lvvect files. By default, this checkbox does not contain a checkmark, and LabVIEW uses Microsoft Excel as the default editor.
      - Default editor file path —Specifies the default editor LabVIEW uses to edit .lvtest and .lvvect files.
  - Configuration —Specifies the settings related to configuring VIs under test, setup and teardown VIs .
    - Input/output values —Specifies which controls and indicators of the VI under test appear on the Test Cases page of the Test Properties dialog box. You can select from the following options:
      - Include controls and indicators from connector pane (Default)—Displays the controls from the connector pane of the VI under test and setup VI as input and displays the indicators from the connector pane of the VI under test and teardown VI as output. You must select a connector pane pattern and assign terminals for the VI under test. National Instruments recommends this option when executing a test on a real-time (RT) target. Doing so avoids test errors that result if the RT target cannot find an input or output.
      - Include controls and indicators from front panel —Displays the controls from the front panel of the VI under test as input and displays the indicators from the front panel of the VI under test as output.
      - Include controls and indicators from front panel as both input and output —Displays the controls and indicators from the front panel of the VI under test as both input and output.
    - Capture input values —Specifies whether to capture the default input values from the VI under test when creating a test. By default, this checkbox contains a checkmark.
    - Capture output values —Specifies whether to capture the default output values from the VI under test when creating a test. By default, this checkbox contains a checkmark.
    - Maximum array elements —Specifies the maximum number of array elements that LabVIEW lists on the Test Cases page of the Test Properties dialog box. If an array contains more elements than the specified number, LabVIEW lists the array as one item. The default is 100.
 Note If you change the **Maximum array elements**, you need to update each test case by clicking the **Import Values from VI** button on the [Test Cases](/csh?context=lvmnt_utf_lvutf_utf_test_cases_db) page.
    - Default array brackets —Specifies the characters LabVIEW uses to wrap control and indicator names of an array. The default is [] .
    - Default name separator —Specifies the character LabVIEW uses to separate control and indicator names in a cluster. The default is / .
- Test Execution —Specifies passwords to the project settings so you can execute tests on password-protected VIs. During execution, LabVIEW stores the passwords in the LabVIEW password cache and saves them in the project file ( .lvproj ). LabVIEW encrypts the passwords before saving them in the project file. 
You also can use this section to configure whether LabVIEW generates code coverage of the whole project and whether LabVIEW enables VI server on a real-time target.
  - Passwords —Specifies settings related to passwords.
    - Password(s) Currently Stored —Displays the number of passwords stored in the password list.
    - Password to Add —Specifies the password you want to add to the password list.
    - Add —Adds the password you specify in the Password to Add text box to the password list.
    - Clear All —Clears the password list from the project settings.
 Note Clicking the **Clear All** button does not remove passwords from the LabVIEW password cache. You can remove passwords from the LabVIEW password cache by restarting LabVIEW or by clearing the password cache from the [Environment](/csh?context=lvcore_lvdialog_miscellaneous_options) page of the [Options](/csh?context=lvcore_lvdialog_options_dialog_box) dialog box.
  - Execution —Configures the settings related to executing a test.
    - Digits of precision for floating-point comparison —Specifies the number of digits after the decimal separator that LabVIEW uses for comparing floating-point values. Valid values are 0-32. The default is 6.
    - Repetitions —Specifies the number of times that LabVIEW repeats the test. The default is 1.
    - Set timeout (s) —Specifies whether to set a timeout, in seconds, for the test during test execution. For example, you can set a timeout for tests of VIs that loop forever or require you to perform tasks manually. If the VI under test times out during execution, LabVIEW stops the VI and test results show this test as failed. By default, this checkbox does not contain a checkmark.
      - Timeout —Specifies the time limit, in seconds, in which LabVIEW must complete the test execution. If you place a checkmark in the Set timeout checkbox, the default is 0.
    - Set minimum code coverage (%) —Specifies whether to set a minimum code coverage requirement, in percent, for the VI under test during test execution. If the VI under test does not meet the minimum code coverage requirement during test execution, test results show this test as failed. By default, this checkbox does not contain a checkmark.
      - Code coverage —Specifies the percentage of subdiagrams LabVIEW must execute during test execution. If you place a checkmark in the Set minimum code coverage checkbox, the default is 100.
  - Include VIs that were not tested —Specifies whether LabVIEW opens all VIs in this project to count subdiagrams and generates the code coverage rate of this project.
 Note If this project contains a large number of VIs, opening these VIs can slow performance.
  - Enable VI Server on real-time targets —Specifies whether to enable the VI Server when you run this test on an RT target. You must enable the VI server to execute unit tests on an RT target. LabVIEW disables the VI server on the RT target when the test completes. You also can manually enable or disable the VI server on an RT target by configuring the VI server for the RT target.

<!--NI_TOPIC bundle=lvutf-api-ref path=errors/error-codes-unit-test-framework-toolkit.html language=enus -->
## TOPIC 00013: Error Codes (Unit Test Framework Toolkit)

- bundle_id: `lvutf-api-ref`
- source_path: `errors/error-codes-unit-test-framework-toolkit.html`
- source_url: https://docs-be.ni.com/bundle/lvutf-api-ref/raw/resource/enus/errors/error-codes-unit-test-framework-toolkit.html
- document_id: `lvutf-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: The Unit Test Framework VIs can return the following error codes. Refer to the KnowledgeBase for more information about correcting errors in LabVIEW. Code Description −25288 Cannot access a shared variable. −25287 An error occurred when creating test(s). −25286 This VI does not have a block diagram.

### Error Codes (Unit Test Framework Toolkit)

The [Unit Test Framework](../menus/categories/programming/utf/unittestframework-mnu.html) VIs can return the following error codes. Refer to the KnowledgeBase for more information about correcting errors in LabVIEW.

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

<!--NI_TOPIC bundle=lvutf-api-ref path=functions/unit-test-framework-results-window.html language=enus -->
## TOPIC 00014: Unit Test Framework Results Window

- bundle_id: `lvutf-api-ref`
- source_path: `functions/unit-test-framework-results-window.html`
- source_url: https://docs-be.ni.com/bundle/lvutf-api-ref/raw/resource/enus/functions/unit-test-framework-results-window.html
- document_id: `lvutf-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Requires: Unit Test Framework Toolkit In the Project Explorer window, click the Unit Test Framework Results button on the Unit Test Framework toolbar to display this window. LabVIEW displays this window after executing tests interactively. LabVIEW also displays this window if you use Open Results Wi

### Unit Test Framework Results Window

**Requires:** Unit Test Framework Toolkit

In the [Project Explorer](/csh?context=lvcore_lvconcepts_using_labview_projects) window, click the **Unit Test Framework Results** button on the [Unit Test Framework toolbar](/csh?context=lvmnt_utf_lvutfconcepts_utfc_project) to display this window. LabVIEW displays this window after [executing tests interactively](/csh?context=lvmnt_utf_lvutfhowto_utfh_execute_test). LabVIEW also displays this window if you use [Open Results Window](../vi-lib/utf/open-results-window-vi.html) VI when [executing tests programmatically](/csh?context=lvmnt_utf_lvutfhowto_utfh_execute_vi).

Use this window to view the [results](/csh?context=lvmnt_utf_lvutfconcepts_utfc_results) of a test execution. You also can [load results from a .lvutf file](/csh?context=lvmnt_utf_lvutfhowto_utfh_result_saveload) to view the results you [saved from a previous test execution](/csh?context=lvmnt_utf_lvutfhowto_utfh_result_saveload).

- Summary —Displays summary results of the test execution. This page includes the following components:
  - Test Results —Displays the number of tests that passed, failed, were skipped, or produced errors.
    - Passed —Displays the number of tests that passed.
    - Failed —Displays the number of tests that failed.
    - Skipped —Displays the number of tests that LabVIEW skips during test execution. LabVIEW skips a test in the following cases:
      - You configure the test to skip during test execution.
      - The priority of the test you specified on the Configuration page of the Test Properties dialog box is lower than the Minimum priority you specified on the Unit Test Framework page of the Project Properties dialog box.
      - You specified to execute only modified tests and the test has not been modified since the time you specified on the Unit Test Framework page.
    - Error —Displays the number of tests that contain errors.
    - Total —Displays the number of tests that executed.
  - Test Errors —Displays the number of .lvtest file errors, VI under test errors, setup VI errors, teardown VI errors, and errors that occurred during test execution.
    - .lvtest File —Displays the number of errors that .lvtest files contain.
    - VI under Test —Displays the number of errors that the VIs under test contain.
    - Setup VI —Displays the number of errors that setup VIs contain.
    - Teardown VI —Displays the number of errors that teardown VIs contain.
    - Test Execution —Displays the number of errors that occurred during test execution.
    - Total —Displays the number of errors that occurred during test execution and errors that .lvtest files, VIs under test, setup VIs, and teardown VIs contain.
  - Statistics —Displays the total execution time and the project code coverage of the current tests.
    - Total Time —Displays the total execution time of the current tests.
    - Project Code Coverage —Displays the project code coverage of the current tests. When you execute the tests, LabVIEW opens all VIs in this project to count subdiagrams and generates the code coverage of this project. For example, you can create a project that contains two VIs and each VI contains three subdiagrams and a test case that covers all three subdiagrams of one VI. When you execute this test, LabVIEW opens both VIs to count subdiagrams. Because this project contains six subdiagrams and the test covers three subdiagrams, the project code coverage measurement is 50%.
  - VIs —Displays the number of VIs in the current project that passed, failed, did not have .lvtest test files, or did not run during test execution.
    - VIs in Project —Displays the number of VIs in the current project.
    - VIs Passed —Displays the number of VIs in the current project that passed during test execution.
    - VIs Failed —Displays the number of VIs in the current project that failed during test execution.
    - VIs Indirectly Tested —Displays the number of VIs in the current project that ran during test execution but did not have .lvtest test files. VIs Indirectly Tested may include subVIs, teardown VIs, and setup VIs.
    - VIs Not Tested —Displays the number of VIs in the current project that did not run during test execution.
- Test Results —Displays the details of the test results. This page includes the following components:
  - Results Details —Lists the results of each test. Expand the tree to view the individual elements. Double-click an item to open the VI in which a test failed. LabVIEW highlights the indicator where the test failed. 
 Note If the VI under test has been modified since the last execution, LabVIEW might highlight the wrong indicator.
  - Show failures only —Specifies whether to display only the results of tests that failed.
  - Display by VI name —Displays the test results according to the names of the VIs.
  - Display by test name —Displays the test results according to the names of the tests.
  - Description —Displays details about the item you select in the Results Details tree.
- Test Errors —Displays errors that occurred during test execution. This page includes the following components:
  - Error Details —Lists the tests and VIs that produced errors during test execution. Expand the tree to view the individual elements.
  - Error Description —Displays details about the item you select in the Error Details tree.
- Code Coverage —Displays the details of code coverage during test execution. This page includes the following components:
  - Code Coverage Details —Lists the code coverage details of each test. If the VI under test calls other VIs, LabVIEW lists the code coverage details of dependencies separately. Expand the tree to view the individual details. 
 Code Coverage —Displays the percentage of subdiagrams LabVIEW executed during test execution.
  - Uncovered Diagrams —Displays details about subdiagrams that LabVIEW did not execute during test execution.
 Note Double-click an item to open the VI. LabVIEW highlights the subdiagram that was not covered during execution.
- Save — Saves the results from the Unit Test Framework Results window to a .lvutf file.
- Load — Loads the results from a previous execution to the Unit Test Framework Results window. LabVIEW loads .lvutf files in the Unit Test Framework Results window only.
- Expand Tree —Expands the tree on the current page.

<!--NI_TOPIC bundle=lvutf-api-ref path=menus/categories/programming/utf/unittestframework-mnu.html language=enus -->
## TOPIC 00015: Unit Test Framework

- bundle_id: `lvutf-api-ref`
- source_path: `menus/categories/programming/utf/unittestframework-mnu.html`
- source_url: https://docs-be.ni.com/bundle/lvutf-api-ref/raw/resource/enus/menus/categories/programming/utf/unittestframework-mnu.html
- document_id: `lvutf-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Use the Unit Test Framework VIs to execute tests programmatically. The VIs on this palette can return general LabVIEW error codes or specific Unit Test Framework error codes. icon

### Unit Test Framework

Use the Unit Test Framework VIs to execute tests programmatically.

The VIs on this palette can return [general LabVIEW error codes](/csh?context=lvcore_lverror_misc_lv_error_codes) or [specific Unit Test Framework error codes](/csh?context=lvmnt_utf_lvutf_utf_error_codes).

[IMAGE alt='icon' src='unittestframework-mnu.png']

- [Run Tests from Project VI](../../../../vi-lib/utf/run-tests-from-project-vi.html) Executes tests from a LabVIEW project. You also can use the Run Tests from File VI to execute tests from .lvtest files.
- [Run Tests from File VI](../../../../vi-lib/utf/run-tests-from-file-vi.html) Executes tests from .lvtest files. You also can use the Run Tests from Project VI to execute tests from a LabVIEW project.
- [Open Results Window VI](../../../../vi-lib/utf/open-results-window-vi.html) Displays the Unit Test Framework Results window after test execution.
- [Create Report VI](../../../../vi-lib/utf/create-report-vi.html) Generates a report after test execution. You can generate this report in HTML, Automatic Test Markup Language (ATML), or ASCII format.

<!--NI_TOPIC bundle=lvutf-api-ref path=utf_intro.html language=enus -->
## TOPIC 00016: LabVIEW Unit Test Framework Toolkit Programming Reference Manual

- bundle_id: `lvutf-api-ref`
- source_path: `utf_intro.html`
- source_url: https://docs-be.ni.com/bundle/lvutf-api-ref/raw/resource/enus/utf_intro.html
- document_id: `lvutf-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: The LabVIEW Unit Test Framework Toolkit LabVIEW Release Notes Visit this site for links to known issues, bugs fixed since the last release, and other notes for any LabVIEW release.To comment on National Instruments documentation, refer to the National Instruments website.

### LabVIEW Unit Test Framework Toolkit Programming Reference Manual

The LabVIEW Unit Test Framework Toolkit

[LabVIEW Release Notes](https://www.ni.com/en-us/support/documentation/release-notes/product.labview.html) 
Visit this site for links to known issues, bugs fixed since the last release, and other notes for any LabVIEW release.

To comment on National Instruments documentation, refer to the National Instruments website.

<!--NI_TOPIC bundle=lvutf-api-ref path=vi-lib/utf/create-report-vi.html language=enus -->
## TOPIC 00017: Create Report VI

- bundle_id: `lvutf-api-ref`
- source_path: `vi-lib/utf/create-report-vi.html`
- source_url: https://docs-be.ni.com/bundle/lvutf-api-ref/raw/resource/enus/vi-lib/utf/create-report-vi.html
- document_id: `lvutf-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Generates a report after test execution. You can generate this report in HTML, Automatic Test Markup Language (ATML), or ASCII format. icon Inputs/Outputs cpath.png CSS file path CSS file path specifies the path to the Cascading Style Sheet (CSS) file this VI uses to customize HTML reports. cbool.pn

### Create Report VI

Generates a report after test execution. You can generate this report in HTML, Automatic Test Markup Language (ATML), or ASCII format.

[IMAGE alt='icon' src='create-report-vi.png']

#### Inputs/Outputs

| CSS file path — CSS file path specifies the path to the Cascading Style Sheet (CSS) file this VI uses to customize HTML reports. view report? (T) — view report? specifies whether to display the report after test execution. If you do not display the report after test execution, you can view the report by navigating to the report path you specified. The default is TRUE. test results in — test results in contains the results of the test execution from using either the Run Tests from File VI or Run Tests from Project VI. utf results out — test case — test result — run Times — result (test) — Vector Result — time elapsed [ms] — result (test) — result (parameters) — result — error message — parameter name — parameter value — parameters — comparison — requirement ID — VI — Used Vector Name — Used Vector Values — Vector Name — element — Executed Class Path — Input — Name — Input Value — VI — Used Vector Index — test case name — requirements — code coverage — coverage — diagram run flag — subVI coverage info — coverage — diagram run flag — test status — test path — setup VI — teardown VI — code coverage — coverage — diagram run flag — start time — end time — test hierarchy — VI path — VI timestamp — VI rev hist — requirements ID — array brackets — name separator — errors — error type — description — paragraph header — result comment — vi hierarchy — subVI coverage info — coverage — diagram run flag — subVI info — Path — Dependence VI — big array threshold — VI Index — Comment — Dynamic Dispatch — User-defined test VI — user-defined VI code coverage — coverage — diagram run flag — untested VIs — VI path — code coverage — coverage — diagram run flag — vi hierarchy — project file path — system information — report path — report path specifies the path to which LabVIEW saves the generated report file. The default is My Documents\\LabVIEW Data. report type (HTML) — report type specifies the type of report this VI generates. error in (no error) — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. display by (Test name) — display by specifies whether to display the test results according to the names of the tests or the names of the VIs. report settings — report settings specifies the contents of the test report. summary? (T) — summary? specifies whether to include the Test Summary section in the test report. The default is TRUE. passed? (T) — passed? specifies whether to include the Passed section in the Test Results section of the test report. The default is TRUE. passed details? (F) — passed details? specifies whether to include the details of the Passed section in the Test Details section of the test report. The default is FALSE. failed? (T) — failed? specifies whether to include the Failed section in the Test Results section of the test report. The default is TRUE. failed details? (F) — failed details? specifies whether to include the details of the Failed section in the Test Details section of the test report. The default is FALSE. skipped? (T) — skipped? specifies whether to include the Skipped section in the Test Results section of the test report. The default is TRUE. error? (T) — error? specifies whether to include the Error section in the Test Results section of the test report. The default is TRUE. error details? (F) — error details? specifies whether to include the details of the Error section in the Test Details section of the test report. The default is FALSE. test results out — test results out returns the test results in unchanged. utf results out — test case — test result — run Times — result (test) — Vector Result — time elapsed [ms] — result (test) — result (parameters) — result — error message — parameter name — parameter value — parameters — comparison — requirement ID — VI — Used Vector Name — Used Vector Values — Vector Name — element — Executed Class Path — Input — Name — Input Value — VI — Used Vector Index — test case name — requirements — code coverage — coverage — diagram run flag — subVI coverage info — coverage — diagram run flag — test status — test path — setup VI — teardown VI — code coverage — coverage — diagram run flag — start time — end time — test hierarchy — VI path — VI timestamp — VI rev hist — requirements ID — array brackets — name separator — errors — error type — description — paragraph header — result comment — vi hierarchy — subVI coverage info — coverage — diagram run flag — subVI info — Path — Dependence VI — big array threshold — VI Index — Comment — Dynamic Dispatch — User-defined test VI — user-defined VI code coverage — coverage — diagram run flag — untested VIs — VI path — code coverage — coverage — diagram run flag — vi hierarchy — project file path — system information — error out — error out contains error information. This output provides standard error out functionality. |
| --- |
| utf results out — test case — test result — run Times — result (test) — Vector Result — time elapsed [ms] — result (test) — result (parameters) — result — error message — parameter name — parameter value — parameters — comparison — requirement ID — VI — Used Vector Name — Used Vector Values — Vector Name — element — Executed Class Path — Input — Name — Input Value — VI — Used Vector Index — test case name — requirements — code coverage — coverage — diagram run flag — subVI coverage info — coverage — diagram run flag — test status — test path — setup VI — teardown VI — code coverage — coverage — diagram run flag — start time — end time — test hierarchy — VI path — VI timestamp — VI rev hist — requirements ID — array brackets — name separator — errors — error type — description — paragraph header — result comment — vi hierarchy — subVI coverage info — coverage — diagram run flag — subVI info — Path — Dependence VI — big array threshold — VI Index — Comment — Dynamic Dispatch — User-defined test VI — user-defined VI code coverage — coverage — diagram run flag — untested VIs — VI path — code coverage — coverage — diagram run flag — vi hierarchy — project file path — system information — |
| test case — test result — run Times — result (test) — Vector Result — time elapsed [ms] — result (test) — result (parameters) — result — error message — parameter name — parameter value — parameters — comparison — requirement ID — VI — Used Vector Name — Used Vector Values — Vector Name — element — Executed Class Path — Input — Name — Input Value — VI — Used Vector Index — test case name — requirements — code coverage — coverage — diagram run flag — subVI coverage info — coverage — diagram run flag — test status — test path — setup VI — teardown VI — code coverage — coverage — diagram run flag — start time — end time — test hierarchy — VI path — VI timestamp — VI rev hist — requirements ID — array brackets — name separator — errors — error type — description — paragraph header — result comment — vi hierarchy — subVI coverage info — coverage — diagram run flag — subVI info — Path — Dependence VI — big array threshold — VI Index — Comment — Dynamic Dispatch — User-defined test VI — user-defined VI code coverage — coverage — diagram run flag — |
| test result — run Times — result (test) — Vector Result — time elapsed [ms] — result (test) — result (parameters) — result — error message — parameter name — parameter value — parameters — comparison — requirement ID — VI — Used Vector Name — Used Vector Values — Vector Name — element — Executed Class Path — Input — Name — Input Value — VI — Used Vector Index — test case name — requirements — code coverage — coverage — diagram run flag — subVI coverage info — coverage — diagram run flag — |
| result (test) — Vector Result — time elapsed [ms] — result (test) — result (parameters) — result — error message — parameter name — parameter value — parameters — comparison — requirement ID — VI — Used Vector Name — Used Vector Values — Vector Name — element — Executed Class Path — Input — Name — Input Value — VI — Used Vector Index — |
| time elapsed [ms] — result (test) — result (parameters) — result — error message — parameter name — parameter value — parameters — comparison — requirement ID — VI — Used Vector Name — Used Vector Values — Vector Name — element — Executed Class Path — Input — Name — Input Value — VI — Used Vector Index — |
| result — error message — parameter name — parameter value — parameters — comparison — requirement ID — VI — Used Vector Name — |
| Vector Name — element — |
| Name — Input Value — VI — Used Vector Index — |
| coverage — diagram run flag — |
| coverage — diagram run flag — |
| coverage — diagram run flag — |
| error type — description — |
| coverage — diagram run flag — |
| Path — Dependence VI — |
| coverage — diagram run flag — |
| VI path — code coverage — coverage — diagram run flag — vi hierarchy — |
| coverage — diagram run flag — |
| summary? (T) — summary? specifies whether to include the Test Summary section in the test report. The default is TRUE. passed? (T) — passed? specifies whether to include the Passed section in the Test Results section of the test report. The default is TRUE. passed details? (F) — passed details? specifies whether to include the details of the Passed section in the Test Details section of the test report. The default is FALSE. failed? (T) — failed? specifies whether to include the Failed section in the Test Results section of the test report. The default is TRUE. failed details? (F) — failed details? specifies whether to include the details of the Failed section in the Test Details section of the test report. The default is FALSE. skipped? (T) — skipped? specifies whether to include the Skipped section in the Test Results section of the test report. The default is TRUE. error? (T) — error? specifies whether to include the Error section in the Test Results section of the test report. The default is TRUE. error details? (F) — error details? specifies whether to include the details of the Error section in the Test Details section of the test report. The default is FALSE. |
| utf results out — test case — test result — run Times — result (test) — Vector Result — time elapsed [ms] — result (test) — result (parameters) — result — error message — parameter name — parameter value — parameters — comparison — requirement ID — VI — Used Vector Name — Used Vector Values — Vector Name — element — Executed Class Path — Input — Name — Input Value — VI — Used Vector Index — test case name — requirements — code coverage — coverage — diagram run flag — subVI coverage info — coverage — diagram run flag — test status — test path — setup VI — teardown VI — code coverage — coverage — diagram run flag — start time — end time — test hierarchy — VI path — VI timestamp — VI rev hist — requirements ID — array brackets — name separator — errors — error type — description — paragraph header — result comment — vi hierarchy — subVI coverage info — coverage — diagram run flag — subVI info — Path — Dependence VI — big array threshold — VI Index — Comment — Dynamic Dispatch — User-defined test VI — user-defined VI code coverage — coverage — diagram run flag — untested VIs — VI path — code coverage — coverage — diagram run flag — vi hierarchy — project file path — system information — |
| test case — test result — run Times — result (test) — Vector Result — time elapsed [ms] — result (test) — result (parameters) — result — error message — parameter name — parameter value — parameters — comparison — requirement ID — VI — Used Vector Name — Used Vector Values — Vector Name — element — Executed Class Path — Input — Name — Input Value — VI — Used Vector Index — test case name — requirements — code coverage — coverage — diagram run flag — subVI coverage info — coverage — diagram run flag — test status — test path — setup VI — teardown VI — code coverage — coverage — diagram run flag — start time — end time — test hierarchy — VI path — VI timestamp — VI rev hist — requirements ID — array brackets — name separator — errors — error type — description — paragraph header — result comment — vi hierarchy — subVI coverage info — coverage — diagram run flag — subVI info — Path — Dependence VI — big array threshold — VI Index — Comment — Dynamic Dispatch — User-defined test VI — user-defined VI code coverage — coverage — diagram run flag — |
| test result — run Times — result (test) — Vector Result — time elapsed [ms] — result (test) — result (parameters) — result — error message — parameter name — parameter value — parameters — comparison — requirement ID — VI — Used Vector Name — Used Vector Values — Vector Name — element — Executed Class Path — Input — Name — Input Value — VI — Used Vector Index — test case name — requirements — code coverage — coverage — diagram run flag — subVI coverage info — coverage — diagram run flag — |
| result (test) — Vector Result — time elapsed [ms] — result (test) — result (parameters) — result — error message — parameter name — parameter value — parameters — comparison — requirement ID — VI — Used Vector Name — Used Vector Values — Vector Name — element — Executed Class Path — Input — Name — Input Value — VI — Used Vector Index — |
| time elapsed [ms] — result (test) — result (parameters) — result — error message — parameter name — parameter value — parameters — comparison — requirement ID — VI — Used Vector Name — Used Vector Values — Vector Name — element — Executed Class Path — Input — Name — Input Value — VI — Used Vector Index — |
| result — error message — parameter name — parameter value — parameters — comparison — requirement ID — VI — Used Vector Name — |
| Vector Name — element — |
| Name — Input Value — VI — Used Vector Index — |
| coverage — diagram run flag — |
| coverage — diagram run flag — |
| coverage — diagram run flag — |
| error type — description — |
| coverage — diagram run flag — |
| Path — Dependence VI — |
| coverage — diagram run flag — |
| VI path — code coverage — coverage — diagram run flag — vi hierarchy — |
| coverage — diagram run flag — |

Parent topic:

Unit Test Framework

<!--NI_TOPIC bundle=lvutf-api-ref path=vi-lib/utf/open-results-window-vi.html language=enus -->
## TOPIC 00018: Open Results Window VI

- bundle_id: `lvutf-api-ref`
- source_path: `vi-lib/utf/open-results-window-vi.html`
- source_url: https://docs-be.ni.com/bundle/lvutf-api-ref/raw/resource/enus/vi-lib/utf/open-results-window-vi.html
- document_id: `lvutf-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Displays the Unit Test Framework Results window after test execution. icon Inputs/Outputs ccclst.png test results in test results in contains the results of the test execution from using either the Run Tests from File VI or Run Tests from Project VI. c1dcclst.png utf results out c1dcclst.png test ca

### Open Results Window VI

Displays the Unit Test Framework Results window after test execution.

[IMAGE alt='icon' src='open-results-window-vi.png']

#### Inputs/Outputs

| test results in — test results in contains the results of the test execution from using either the Run Tests from File VI or Run Tests from Project VI. utf results out — test case — test result — run Times — result (test) — Vector Result — time elapsed [ms] — result (test) — result (parameters) — result — error message — parameter name — parameter value — parameters — comparison — requirement ID — VI — Used Vector Name — Used Vector Values — Vector Name — element — Executed Class Path — Input — Name — Input Value — VI — Used Vector Index — test case name — requirements — code coverage — coverage — diagram run flag — subVI coverage info — coverage — diagram run flag — test status — test path — setup VI — teardown VI — code coverage — coverage — diagram run flag — start time — end time — test hierarchy — VI path — VI timestamp — VI rev hist — requirements ID — array brackets — name separator — errors — error type — description — paragraph header — result comment — vi hierarchy — subVI coverage info — coverage — diagram run flag — subVI info — Path — Dependence VI — big array threshold — VI Index — Comment — Dynamic Dispatch — User-defined test VI — user-defined VI code coverage — coverage — diagram run flag — untested VIs — VI path — code coverage — coverage — diagram run flag — vi hierarchy — project file path — system information — error in (no error) — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. test results out — test results out returns the test results in unchanged. utf results out — test case — test result — run Times — result (test) — Vector Result — time elapsed [ms] — result (test) — result (parameters) — result — error message — parameter name — parameter value — parameters — comparison — requirement ID — VI — Used Vector Name — Used Vector Values — Vector Name — element — Executed Class Path — Input — Name — Input Value — VI — Used Vector Index — test case name — requirements — code coverage — coverage — diagram run flag — subVI coverage info — coverage — diagram run flag — test status — test path — setup VI — teardown VI — code coverage — coverage — diagram run flag — start time — end time — test hierarchy — VI path — VI timestamp — VI rev hist — requirements ID — array brackets — name separator — errors — error type — description — paragraph header — result comment — vi hierarchy — subVI coverage info — coverage — diagram run flag — subVI info — Path — Dependence VI — big array threshold — VI Index — Comment — Dynamic Dispatch — User-defined test VI — user-defined VI code coverage — coverage — diagram run flag — untested VIs — VI path — code coverage — coverage — diagram run flag — vi hierarchy — project file path — system information — error out — error out contains error information. This output provides standard error out functionality. |
| --- |
| utf results out — test case — test result — run Times — result (test) — Vector Result — time elapsed [ms] — result (test) — result (parameters) — result — error message — parameter name — parameter value — parameters — comparison — requirement ID — VI — Used Vector Name — Used Vector Values — Vector Name — element — Executed Class Path — Input — Name — Input Value — VI — Used Vector Index — test case name — requirements — code coverage — coverage — diagram run flag — subVI coverage info — coverage — diagram run flag — test status — test path — setup VI — teardown VI — code coverage — coverage — diagram run flag — start time — end time — test hierarchy — VI path — VI timestamp — VI rev hist — requirements ID — array brackets — name separator — errors — error type — description — paragraph header — result comment — vi hierarchy — subVI coverage info — coverage — diagram run flag — subVI info — Path — Dependence VI — big array threshold — VI Index — Comment — Dynamic Dispatch — User-defined test VI — user-defined VI code coverage — coverage — diagram run flag — untested VIs — VI path — code coverage — coverage — diagram run flag — vi hierarchy — project file path — system information — |
| test case — test result — run Times — result (test) — Vector Result — time elapsed [ms] — result (test) — result (parameters) — result — error message — parameter name — parameter value — parameters — comparison — requirement ID — VI — Used Vector Name — Used Vector Values — Vector Name — element — Executed Class Path — Input — Name — Input Value — VI — Used Vector Index — test case name — requirements — code coverage — coverage — diagram run flag — subVI coverage info — coverage — diagram run flag — test status — test path — setup VI — teardown VI — code coverage — coverage — diagram run flag — start time — end time — test hierarchy — VI path — VI timestamp — VI rev hist — requirements ID — array brackets — name separator — errors — error type — description — paragraph header — result comment — vi hierarchy — subVI coverage info — coverage — diagram run flag — subVI info — Path — Dependence VI — big array threshold — VI Index — Comment — Dynamic Dispatch — User-defined test VI — user-defined VI code coverage — coverage — diagram run flag — |
| test result — run Times — result (test) — Vector Result — time elapsed [ms] — result (test) — result (parameters) — result — error message — parameter name — parameter value — parameters — comparison — requirement ID — VI — Used Vector Name — Used Vector Values — Vector Name — element — Executed Class Path — Input — Name — Input Value — VI — Used Vector Index — test case name — requirements — code coverage — coverage — diagram run flag — subVI coverage info — coverage — diagram run flag — |
| result (test) — Vector Result — time elapsed [ms] — result (test) — result (parameters) — result — error message — parameter name — parameter value — parameters — comparison — requirement ID — VI — Used Vector Name — Used Vector Values — Vector Name — element — Executed Class Path — Input — Name — Input Value — VI — Used Vector Index — |
| time elapsed [ms] — result (test) — result (parameters) — result — error message — parameter name — parameter value — parameters — comparison — requirement ID — VI — Used Vector Name — Used Vector Values — Vector Name — element — Executed Class Path — Input — Name — Input Value — VI — Used Vector Index — |
| result — error message — parameter name — parameter value — parameters — comparison — requirement ID — VI — Used Vector Name — |
| Vector Name — element — |
| Name — Input Value — VI — Used Vector Index — |
| coverage — diagram run flag — |
| coverage — diagram run flag — |
| coverage — diagram run flag — |
| error type — description — |
| coverage — diagram run flag — |
| Path — Dependence VI — |
| coverage — diagram run flag — |
| VI path — code coverage — coverage — diagram run flag — vi hierarchy — |
| coverage — diagram run flag — |
| utf results out — test case — test result — run Times — result (test) — Vector Result — time elapsed [ms] — result (test) — result (parameters) — result — error message — parameter name — parameter value — parameters — comparison — requirement ID — VI — Used Vector Name — Used Vector Values — Vector Name — element — Executed Class Path — Input — Name — Input Value — VI — Used Vector Index — test case name — requirements — code coverage — coverage — diagram run flag — subVI coverage info — coverage — diagram run flag — test status — test path — setup VI — teardown VI — code coverage — coverage — diagram run flag — start time — end time — test hierarchy — VI path — VI timestamp — VI rev hist — requirements ID — array brackets — name separator — errors — error type — description — paragraph header — result comment — vi hierarchy — subVI coverage info — coverage — diagram run flag — subVI info — Path — Dependence VI — big array threshold — VI Index — Comment — Dynamic Dispatch — User-defined test VI — user-defined VI code coverage — coverage — diagram run flag — untested VIs — VI path — code coverage — coverage — diagram run flag — vi hierarchy — project file path — system information — |
| test case — test result — run Times — result (test) — Vector Result — time elapsed [ms] — result (test) — result (parameters) — result — error message — parameter name — parameter value — parameters — comparison — requirement ID — VI — Used Vector Name — Used Vector Values — Vector Name — element — Executed Class Path — Input — Name — Input Value — VI — Used Vector Index — test case name — requirements — code coverage — coverage — diagram run flag — subVI coverage info — coverage — diagram run flag — test status — test path — setup VI — teardown VI — code coverage — coverage — diagram run flag — start time — end time — test hierarchy — VI path — VI timestamp — VI rev hist — requirements ID — array brackets — name separator — errors — error type — description — paragraph header — result comment — vi hierarchy — subVI coverage info — coverage — diagram run flag — subVI info — Path — Dependence VI — big array threshold — VI Index — Comment — Dynamic Dispatch — User-defined test VI — user-defined VI code coverage — coverage — diagram run flag — |
| test result — run Times — result (test) — Vector Result — time elapsed [ms] — result (test) — result (parameters) — result — error message — parameter name — parameter value — parameters — comparison — requirement ID — VI — Used Vector Name — Used Vector Values — Vector Name — element — Executed Class Path — Input — Name — Input Value — VI — Used Vector Index — test case name — requirements — code coverage — coverage — diagram run flag — subVI coverage info — coverage — diagram run flag — |
| result (test) — Vector Result — time elapsed [ms] — result (test) — result (parameters) — result — error message — parameter name — parameter value — parameters — comparison — requirement ID — VI — Used Vector Name — Used Vector Values — Vector Name — element — Executed Class Path — Input — Name — Input Value — VI — Used Vector Index — |
| time elapsed [ms] — result (test) — result (parameters) — result — error message — parameter name — parameter value — parameters — comparison — requirement ID — VI — Used Vector Name — Used Vector Values — Vector Name — element — Executed Class Path — Input — Name — Input Value — VI — Used Vector Index — |
| result — error message — parameter name — parameter value — parameters — comparison — requirement ID — VI — Used Vector Name — |
| Vector Name — element — |
| Name — Input Value — VI — Used Vector Index — |
| coverage — diagram run flag — |
| coverage — diagram run flag — |
| coverage — diagram run flag — |
| error type — description — |
| coverage — diagram run flag — |
| Path — Dependence VI — |
| coverage — diagram run flag — |
| VI path — code coverage — coverage — diagram run flag — vi hierarchy — |
| coverage — diagram run flag — |

Parent topic:

Unit Test Framework

<!--NI_TOPIC bundle=lvutf-api-ref path=vi-lib/utf/run-tests-from-file-vi.html language=enus -->
## TOPIC 00019: Run Tests from File VI

- bundle_id: `lvutf-api-ref`
- source_path: `vi-lib/utf/run-tests-from-file-vi.html`
- source_url: https://docs-be.ni.com/bundle/lvutf-api-ref/raw/resource/enus/vi-lib/utf/run-tests-from-file-vi.html
- document_id: `lvutf-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Executes tests from .lvtest files. You also can use the Run Tests from Project VI to execute tests from a LabVIEW project. icon Inputs/Outputs cbool.png show progress bar? (T) show progress bar? specifies whether to show the progress window during test execution. The default is TRUE. c1dpath.png tes

### Run Tests from File VI

Executes tests from .lvtest files.

You also can use the Run Tests from Project VI to execute tests from a LabVIEW project.

[IMAGE alt='icon' src='run-tests-from-file-vi.png']

#### Inputs/Outputs

| show progress bar? (T) — show progress bar? specifies whether to show the progress window during test execution. The default is TRUE. test file paths — test file paths specifies the paths to each .lvtest file this VI executes. error in (no error) — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. test results out — test results out returns test results of the specified .lvtest files. utf results out — test case — test result — run Times — result (test) — Vector Result — time elapsed [ms] — result (test) — result (parameters) — result — error message — parameter name — parameter value — parameters — comparison — requirement ID — VI — Used Vector Name — Used Vector Values — Vector Name — element — Executed Class Path — Input — Name — Input Value — VI — Used Vector Index — test case name — requirements — code coverage — coverage — diagram run flag — subVI coverage info — coverage — diagram run flag — test status — test path — setup VI — teardown VI — code coverage — coverage — diagram run flag — start time — end time — test hierarchy — VI path — VI timestamp — VI rev hist — requirements ID — array brackets — name separator — errors — error type — description — paragraph header — result comment — vi hierarchy — subVI coverage info — coverage — diagram run flag — subVI info — Path — Dependence VI — big array threshold — VI Index — Comment — Dynamic Dispatch — User-defined test VI — user-defined VI code coverage — coverage — diagram run flag — untested VIs — VI path — code coverage — coverage — diagram run flag — vi hierarchy — project file path — system information — error out — error out contains error information. This output provides standard error out functionality. |
| --- |
| utf results out — test case — test result — run Times — result (test) — Vector Result — time elapsed [ms] — result (test) — result (parameters) — result — error message — parameter name — parameter value — parameters — comparison — requirement ID — VI — Used Vector Name — Used Vector Values — Vector Name — element — Executed Class Path — Input — Name — Input Value — VI — Used Vector Index — test case name — requirements — code coverage — coverage — diagram run flag — subVI coverage info — coverage — diagram run flag — test status — test path — setup VI — teardown VI — code coverage — coverage — diagram run flag — start time — end time — test hierarchy — VI path — VI timestamp — VI rev hist — requirements ID — array brackets — name separator — errors — error type — description — paragraph header — result comment — vi hierarchy — subVI coverage info — coverage — diagram run flag — subVI info — Path — Dependence VI — big array threshold — VI Index — Comment — Dynamic Dispatch — User-defined test VI — user-defined VI code coverage — coverage — diagram run flag — untested VIs — VI path — code coverage — coverage — diagram run flag — vi hierarchy — project file path — system information — |
| test case — test result — run Times — result (test) — Vector Result — time elapsed [ms] — result (test) — result (parameters) — result — error message — parameter name — parameter value — parameters — comparison — requirement ID — VI — Used Vector Name — Used Vector Values — Vector Name — element — Executed Class Path — Input — Name — Input Value — VI — Used Vector Index — test case name — requirements — code coverage — coverage — diagram run flag — subVI coverage info — coverage — diagram run flag — test status — test path — setup VI — teardown VI — code coverage — coverage — diagram run flag — start time — end time — test hierarchy — VI path — VI timestamp — VI rev hist — requirements ID — array brackets — name separator — errors — error type — description — paragraph header — result comment — vi hierarchy — subVI coverage info — coverage — diagram run flag — subVI info — Path — Dependence VI — big array threshold — VI Index — Comment — Dynamic Dispatch — User-defined test VI — user-defined VI code coverage — coverage — diagram run flag — |
| test result — run Times — result (test) — Vector Result — time elapsed [ms] — result (test) — result (parameters) — result — error message — parameter name — parameter value — parameters — comparison — requirement ID — VI — Used Vector Name — Used Vector Values — Vector Name — element — Executed Class Path — Input — Name — Input Value — VI — Used Vector Index — test case name — requirements — code coverage — coverage — diagram run flag — subVI coverage info — coverage — diagram run flag — |
| result (test) — Vector Result — time elapsed [ms] — result (test) — result (parameters) — result — error message — parameter name — parameter value — parameters — comparison — requirement ID — VI — Used Vector Name — Used Vector Values — Vector Name — element — Executed Class Path — Input — Name — Input Value — VI — Used Vector Index — |
| time elapsed [ms] — result (test) — result (parameters) — result — error message — parameter name — parameter value — parameters — comparison — requirement ID — VI — Used Vector Name — Used Vector Values — Vector Name — element — Executed Class Path — Input — Name — Input Value — VI — Used Vector Index — |
| result — error message — parameter name — parameter value — parameters — comparison — requirement ID — VI — Used Vector Name — |
| Vector Name — element — |
| Name — Input Value — VI — Used Vector Index — |
| coverage — diagram run flag — |
| coverage — diagram run flag — |
| coverage — diagram run flag — |
| error type — description — |
| coverage — diagram run flag — |
| Path — Dependence VI — |
| coverage — diagram run flag — |
| VI path — code coverage — coverage — diagram run flag — vi hierarchy — |
| coverage — diagram run flag — |

Parent topic:

Unit Test Framework

<!--NI_TOPIC bundle=lvutf-api-ref path=vi-lib/utf/run-tests-from-project-vi.html language=enus -->
## TOPIC 00020: Run Tests from Project VI

- bundle_id: `lvutf-api-ref`
- source_path: `vi-lib/utf/run-tests-from-project-vi.html`
- source_url: https://docs-be.ni.com/bundle/lvutf-api-ref/raw/resource/enus/vi-lib/utf/run-tests-from-project-vi.html
- document_id: `lvutf-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Executes tests from a LabVIEW project. You also can use the Run Tests from File VI to execute tests from .lvtest files. icon Inputs/Outputs cbool.png show progress bar? (T) show progress bar? specifies whether to show the progress window during test execution. The default is TRUE. cpath.png project

### Run Tests from Project VI

Executes tests from a LabVIEW project.

You also can use the Run Tests from File VI to execute tests from .lvtest files.

[IMAGE alt='icon' src='run-tests-from-project-vi.png']

#### Inputs/Outputs

| show progress bar? (T) — show progress bar? specifies whether to show the progress window during test execution. The default is TRUE. project file path — project file path specifies the path to the .lvproj file that contains .lvtest files. error in (no error) — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. test results out — test results out returns test results of the .lvtest files in the specified .lvproj file. utf results out — test case — test result — run Times — result (test) — Vector Result — time elapsed [ms] — result (test) — result (parameters) — result — error message — parameter name — parameter value — parameters — comparison — requirement ID — VI — Used Vector Name — Used Vector Values — Vector Name — element — Executed Class Path — Input — Name — Input Value — VI — Used Vector Index — test case name — requirements — code coverage — coverage — diagram run flag — subVI coverage info — coverage — diagram run flag — test status — test path — setup VI — teardown VI — code coverage — coverage — diagram run flag — start time — end time — test hierarchy — VI path — VI timestamp — VI rev hist — requirements ID — array brackets — name separator — errors — error type — description — paragraph header — result comment — vi hierarchy — subVI coverage info — coverage — diagram run flag — subVI info — Path — Dependence VI — big array threshold — VI Index — Comment — Dynamic Dispatch — User-defined test VI — user-defined VI code coverage — coverage — diagram run flag — untested VIs — VI path — code coverage — coverage — diagram run flag — vi hierarchy — project file path — system information — error out — error out contains error information. This output provides standard error out functionality. |
| --- |
| utf results out — test case — test result — run Times — result (test) — Vector Result — time elapsed [ms] — result (test) — result (parameters) — result — error message — parameter name — parameter value — parameters — comparison — requirement ID — VI — Used Vector Name — Used Vector Values — Vector Name — element — Executed Class Path — Input — Name — Input Value — VI — Used Vector Index — test case name — requirements — code coverage — coverage — diagram run flag — subVI coverage info — coverage — diagram run flag — test status — test path — setup VI — teardown VI — code coverage — coverage — diagram run flag — start time — end time — test hierarchy — VI path — VI timestamp — VI rev hist — requirements ID — array brackets — name separator — errors — error type — description — paragraph header — result comment — vi hierarchy — subVI coverage info — coverage — diagram run flag — subVI info — Path — Dependence VI — big array threshold — VI Index — Comment — Dynamic Dispatch — User-defined test VI — user-defined VI code coverage — coverage — diagram run flag — untested VIs — VI path — code coverage — coverage — diagram run flag — vi hierarchy — project file path — system information — |
| test case — test result — run Times — result (test) — Vector Result — time elapsed [ms] — result (test) — result (parameters) — result — error message — parameter name — parameter value — parameters — comparison — requirement ID — VI — Used Vector Name — Used Vector Values — Vector Name — element — Executed Class Path — Input — Name — Input Value — VI — Used Vector Index — test case name — requirements — code coverage — coverage — diagram run flag — subVI coverage info — coverage — diagram run flag — test status — test path — setup VI — teardown VI — code coverage — coverage — diagram run flag — start time — end time — test hierarchy — VI path — VI timestamp — VI rev hist — requirements ID — array brackets — name separator — errors — error type — description — paragraph header — result comment — vi hierarchy — subVI coverage info — coverage — diagram run flag — subVI info — Path — Dependence VI — big array threshold — VI Index — Comment — Dynamic Dispatch — User-defined test VI — user-defined VI code coverage — coverage — diagram run flag — |
| test result — run Times — result (test) — Vector Result — time elapsed [ms] — result (test) — result (parameters) — result — error message — parameter name — parameter value — parameters — comparison — requirement ID — VI — Used Vector Name — Used Vector Values — Vector Name — element — Executed Class Path — Input — Name — Input Value — VI — Used Vector Index — test case name — requirements — code coverage — coverage — diagram run flag — subVI coverage info — coverage — diagram run flag — |
| result (test) — Vector Result — time elapsed [ms] — result (test) — result (parameters) — result — error message — parameter name — parameter value — parameters — comparison — requirement ID — VI — Used Vector Name — Used Vector Values — Vector Name — element — Executed Class Path — Input — Name — Input Value — VI — Used Vector Index — |
| time elapsed [ms] — result (test) — result (parameters) — result — error message — parameter name — parameter value — parameters — comparison — requirement ID — VI — Used Vector Name — Used Vector Values — Vector Name — element — Executed Class Path — Input — Name — Input Value — VI — Used Vector Index — |
| result — error message — parameter name — parameter value — parameters — comparison — requirement ID — VI — Used Vector Name — |
| Vector Name — element — |
| Name — Input Value — VI — Used Vector Index — |
| coverage — diagram run flag — |
| coverage — diagram run flag — |
| coverage — diagram run flag — |
| error type — description — |
| coverage — diagram run flag — |
| Path — Dependence VI — |
| coverage — diagram run flag — |
| VI path — code coverage — coverage — diagram run flag — vi hierarchy — |
| coverage — diagram run flag — |

Parent topic:

Unit Test Framework
