# NI DOCUMENT BUNDLE: labview-unit-test-framework-toolkit

<!--NI_BUNDLE_CHUNK bundle=labview-unit-test-framework-toolkit start=1 end=86 -->
<!--NI_TOPIC bundle=labview-unit-test-framework-toolkit path=adding-files-to-a-project.html language=enus -->
## TOPIC 00001: Adding Files to a Project

- bundle_id: `labview-unit-test-framework-toolkit`
- source_path: `adding-files-to-a-project.html`
- source_url: https://docs-be.ni.com/bundle/labview-unit-test-framework-toolkit/raw/resource/enus/adding-files-to-a-project.html
- document_id: `labview-unit-test-framework-toolkit`
- page_type: `leaf`
- content_type: `task`
- source_description: Complete the following steps to add files, such as VIs, .lvtest files, .lvtest files, auto-populating folders, and LabVIEW project libraries, to a LabVIEW project. Create a new project or open an existing project. Right-click a target, such as My Computer, and select Add»File from the shortcut menu.

### Adding Files to a Project

.lvtest

.lvtest

1. Create a new project or open an existing project.
2. Right-click a target, such as My Computer, and select Add»File from the shortcut menu. A file dialog box appears.
3. Navigate to and select the files you want to add to the project.
4. Click the Add File button. 
 The newly-added items appear at the bottom of the project tree, above
 the Dependencies icon. Note When you add an
 item that is part of a LabVIEW project library, LabVIEW adds the entire
 project library to the project tree.
5. Select File»Save to save the project.

Parent topic:

Organize a Project

<!--NI_TOPIC bundle=labview-unit-test-framework-toolkit path=adding-or-duplicating-test-cases.html language=enus -->
## TOPIC 00002: Adding or Duplicating Test Cases

- bundle_id: `labview-unit-test-framework-toolkit`
- source_path: `adding-or-duplicating-test-cases.html`
- source_url: https://docs-be.ni.com/bundle/labview-unit-test-framework-toolkit/raw/resource/enus/adding-or-duplicating-test-cases.html
- document_id: `labview-unit-test-framework-toolkit`
- page_type: `leaf`
- content_type: `task`
- source_description: Use the Project Explorer window to add or duplicate test cases interactively. You also can add or delete test cases by editing .lvtest files.Complete the following steps to add or duplicate a test case: Open the LabVIEW project that contains the files on which you want to perform unit testing. Add a

### Adding or Duplicating Test Cases

Project
 Explorer

.lvtest

Complete
 the following steps to add or duplicate a test case:

1. Open the LabVIEW project that contains the files on which you want to perform
 unit testing.
2. Add a test case to a test in one of the following ways:
  - Right-click the VI for which you want to add a new test case and select Unit Tests»New Test
 Case»testname».lvtest from the shortcut menu, where testname is
 the name of the .lvtest file to which you want to add a
 test case. The Test Cases page of the Test
 Properties dialog box appears, displaying the new test
 case. Note An
 .lvtest test file must already exist in the
 project for this VI.
  - Double-click the .lvtest file to which you want to add a new test case
 to display the Test Properties dialog box. On the
 Test Cases page, click the
 New button to add a new test case.
  - Double-click the .lvtest file to which you want to add a new test case
 to display the Test Properties dialog box. On the
 Test Cases page, click the
 Duplicate button to duplicate the current test case. Note When you add
 or duplicate a test case, LabVIEW adds the new test case to the end of
 the test case list and displays the new test case.
3. Configure the new test case.
4. Select File»Save to save the project.

Parent topic:

Configure Tests

<!--NI_TOPIC bundle=labview-unit-test-framework-toolkit path=assigning-test-vectors-in-test-cases.html language=enus -->
## TOPIC 00003: Assigning Test Vectors in Test Cases

- bundle_id: `labview-unit-test-framework-toolkit`
- source_path: `assigning-test-vectors-in-test-cases.html`
- source_url: https://docs-be.ni.com/bundle/labview-unit-test-framework-toolkit/raw/resource/enus/assigning-test-vectors-in-test-cases.html
- document_id: `labview-unit-test-framework-toolkit`
- page_type: `leaf`
- content_type: `task`
- source_description: Complete the following steps to use a test vector in a unit test. In the Project Explorer window, double-click an .lvtest file to display the Test Properties dialog box. Select Test Vectors from the Category list to open the Test Vectors page Click the Add button. A file dialog box appears. Locate a

### Assigning Test Vectors in Test Cases

Complete the following steps to use a test vector in a
 unit test.

1. In the Project Explorer window, double-click an
 .lvtest file to display the Test
 Properties dialog box.
2. Select Test Vectors from the
 Category list to open the Test
 Vectors page
3. Click the Add button. A file dialog box appears.
4. Locate and select the test vector file that you want to add in this file dialog
 box and click the OK button to add this test vector file
 to the Test Vector Files list.
5. Select Test Cases from the
 Category list to open the Test
 Cases page.
6. Right-click the input or output terminal that you want to assign a test vector
 and select Assign Test Vector from the shortcut
 menu. The Input Value cell or Expected Value
 cell displays No Vector.
7. Select the test vector you want to use from the pull-down menu in the Input Value cell or Expected Value cell.
8. Optional: Use indexes for test vectors assigned to inputs. Right-click the test vector
 and select Assign Index»New Index to create an index and assign this index to the test vector. You
 also can assign existing indexes to a test vector by selecting an existing index
 under Assign Index. Select Assign Index»No Index to remove an index from a test vector. Note You cannot use
 indexes for test vectors assigned to output terminals.
9. Click the OK button to close the Test
 Properties dialog box and apply the change.

Parent topic:

Create Test Vector Files and Test Vectors

Related concepts:

- Test Vectors and .lvvect Files

<!--NI_TOPIC bundle=labview-unit-test-framework-toolkit path=build-specifications.html language=enus -->
## TOPIC 00004: Build Specifications

- bundle_id: `labview-unit-test-framework-toolkit`
- source_path: `build-specifications.html`
- source_url: https://docs-be.ni.com/bundle/labview-unit-test-framework-toolkit/raw/resource/enus/build-specifications.html
- document_id: `labview-unit-test-framework-toolkit`
- page_type: `leaf`
- content_type: `concept`
- source_description: The Build Specifications item in the Project Explorer window allows you to create and configure build specifications for LabVIEW builds. A build specification contains all the settings for the build, such as files to include, directories to create, and settings for VIs. You can configure the followi

### Build Specifications

The Build Specifications item in the Project
 Explorer window allows you to create and configure build specifications
 for LabVIEW builds.

A build specification contains all the settings for the build, such as files to include,
 directories to create, and settings for VIs.

You can configure the following types of build specifications to include
 .lvtest files:

- Installers (Windows)
- Source distributions Caution When configuring VIs in a source
 distribution, do not place checkmarks in the Remove front
 panel and Remove block diagram checkboxes
 on the Source File Settings page of the Source Distribution
 Properties dialog box for any VI under test. If you remove the
 front panel or block diagram of a VI under test, LabVIEW returns test errors on
 the Test Errors page of the Unit Test
 Framework Results window.
- Zip files

You must have the Application Builder installed to build installers and zip files. The
 LabVIEW Professional Development System includes the Application Builder. If you use the
 LabVIEW Base Development System or Full Development System, you can purchase the
 Application Builder separately by visiting the manufacturer's web site. If you have
 already purchased the Application Builder, select Help»Activate LabVIEW Components to activate the product.

You can hide the Build Specifications item in the
 Project Explorer window. If you hide this item you must
 display it again to access the item.

Parent topic:

Using the Project Explorer Window

Related information:

- LabVIEW Application Builder Module

<!--NI_TOPIC bundle=labview-unit-test-framework-toolkit path=code-coverage.html language=enus -->
## TOPIC 00005: Code Coverage

- bundle_id: `labview-unit-test-framework-toolkit`
- source_path: `code-coverage.html`
- source_url: https://docs-be.ni.com/bundle/labview-unit-test-framework-toolkit/raw/resource/enus/code-coverage.html
- document_id: `labview-unit-test-framework-toolkit`
- page_type: `leaf`
- content_type: `concept`
- source_description: Code coverage measures the percentage of subdiagrams LabVIEW executes when you run a VI. This measurement provides information about the amount of code that was executed and might be useful when performing unit testing.The LabVIEW Unit Test Framework Toolkit cannot measure code coverage on Real-Time

### Code Coverage

Note

The Unit Test Framework Toolkit calculates code coverage by dividing the total number of
 subdiagrams that execute during test execution by the total number of subdiagrams in the
 VI. Every VI has at least one subdiagram or diagram, which is the block diagram of the
 VI. Loops and structures have one or more subdiagrams. For example, For
 Loop and While Loop structures have one subdiagram
 each. Case and Sequence structures have one
 subdiagram per frame.

The following picture shows an example block diagram with six subdiagrams:

[IMAGE alt='image' src='GUID-55D6FCA5-6A19-4825-A9DA-729C46E5BBCC-a5.gif']

The previous figure shows the block diagram of a VI. You can assume that each
 Case structure contains only two cases and no loops or structures
 other than the For Loop that already appears in the figure. Using
 these assumptions, this VI contains six subdiagrams. The six subdiagrams are the block
 diagram of the VI, the two cases for each Case structure (four
 subdiagrams total), and the For Loop. If five of the six subdiagrams
 execute during test execution, the code coverage measurement is 83.33%.

You must allow debugging for each VI under test in order to measure code coverage. If the VI
 properties of a VI under test do not have a checkmark in the Allow
 debugging checkbox, the code coverage result always will be zero. To
 allow debugging, open the VI under test, select File»VI Properties to display the VI Properties dialog box, select
 Execution from the pull-down menu, and place a checkmark in
 the Allow debugging checkbox.

You can specify a minimum code coverage requirement interactively by using the
 Advanced page of the Test Properties
 dialog box. You also can specify a minimum code coverage requirement by editing
 .lvtest files.

When you execute a test, LabVIEW measures the percentage of subdiagrams covered for the VI under
 test. If the VI under test does not meet the minimum code coverage requirement you
 specified in the .lvtest file, test results show this test as
 failed. You can double-click an item on the Code Coverage page of
 the Unit Test Framework Results window to highlight the
 subdiagram of the VI that LabVIEW did not cover during execution.

If you test a member VI of a dynamic dispatch method, LabVIEW may execute another member VI in
 the test according to the method. The Unit Test Framework toolkit generates code
 coverage of the VI that LabVIEW executed in the test. On the Code
 Coverage page of the Unit Test Framework Results
 window, the Unit Test Framework toolkit uses a diamond (♦) to indicate a dynamic
 dispatch VI. The Unit Test Framework toolkit also lists all dynamic dispatch VIs of a
 test in the Dependencies list of this page.

Parent topic:

Introduction to the LabVIEW Unit Test Framework Toolkit

Related tasks:

- Specifying a Minimum Code Coverage Requirement

<!--NI_TOPIC bundle=labview-unit-test-framework-toolkit path=comparison-types.html language=enus -->
## TOPIC 00006: Comparison Types

- bundle_id: `labview-unit-test-framework-toolkit`
- source_path: `comparison-types.html`
- source_url: https://docs-be.ni.com/bundle/labview-unit-test-framework-toolkit/raw/resource/enus/comparison-types.html
- document_id: `labview-unit-test-framework-toolkit`
- page_type: `leaf`
- content_type: `concept`
- source_description: The LabVIEW Unit Test Framework Toolkit provides several comparison types you use to compare resulting values with expected values.When you configure a test case, you specify a comparison type for each Output Name on the Test Cases page of the Test Properties dialog box. LabVIEW lists the available

### Comparison Types

The LabVIEW Unit Test Framework Toolkit provides several comparison types you use to
 compare resulting values with expected values.

When you configure a test case, you specify a comparison type for each Output
 Name on the Test Cases page of the
 Test Properties dialog box. LabVIEW lists the available
 comparison types that each data type supports. You also can specify a user-defined
 comparison VI.

When you execute a test, LabVIEW runs the VI under test by using the input values you specified
 for each test case in the .lvtest file. LabVIEW then compares the
 resulting values with the expected values by using the comparison types you
 specified.

The following figure shows an example of specifying the comparison type for an output
 terminal:

[IMAGE alt='image' src='GUID-6008A974-7F04-4CF2-B250-D7E492816A8A-a5.png']

In the previous figure, LabVIEW lists the available comparison types you can use to compare the
 resulting value of the x*y terminal with the expected value.

#### Supported Comparison
 Types

The following table lists comparison types that the Unit Test
 Framework Toolkit supports:

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

Note

Digits of precision for floating-point comparison

Advanced

Test
 Properties

Parent topic:

Introduction to the LabVIEW Unit Test Framework Toolkit

Related tasks:

- Creating a User-Defined Comparison VI

<!--NI_TOPIC bundle=labview-unit-test-framework-toolkit path=configuring-a-test-to-skip.html language=enus -->
## TOPIC 00007: Configuring a Test to Skip

- bundle_id: `labview-unit-test-framework-toolkit`
- source_path: `configuring-a-test-to-skip.html`
- source_url: https://docs-be.ni.com/bundle/labview-unit-test-framework-toolkit/raw/resource/enus/configuring-a-test-to-skip.html
- document_id: `labview-unit-test-framework-toolkit`
- page_type: `leaf`
- content_type: `task`
- source_description: Complete the following steps to configure a test to skip during test execution.Open the LabVIEW project that contains the files on which you want to perform unit testing. Double-click an .lvtest file to display the Test Properties dialog box. On the Configuration page, place a checkmark in the Alway

### Configuring a Test to Skip

Complete the following steps to configure a test to skip
 during test execution.

1. Open the LabVIEW project that contains the files on which you want to perform
 unit testing.
2. Double-click an .lvtest file to display the
 Test Properties dialog box.
3. On the Configuration page, place a checkmark in the
 Always skip this test checkbox. The Project Explorer window and the Unit Test
 Framework VIs checkboxes appear and contain checkmarks by
 default.
4. Optional: 
 If you want to skip this test only when executing tests interactively from the
 Project Explorer window, remove the checkmark from
 the Unit Test Framework VIs checkbox.
5. Optional: 
 If you want to skip this test only when executing tests programmatically with
 the Unit Test Framework VIs, remove the checkmark from the Project
 Explorer window checkbox.
6. Click the OK button to close the dialog box and return
 to the Project Explorer window.
7. Select File»Save to save the project.

The next time you execute tests, LabVIEW skips this test.

Parent topic:

Configure Tests

Related concepts:

- Execute Tests Interactively
- Execute Tests Programmatically

<!--NI_TOPIC bundle=labview-unit-test-framework-toolkit path=configuring-a-test-to-use-a-user-defined-test.html language=enus -->
## TOPIC 00008: Configuring a Test to Use a User-Defined Test VI

- bundle_id: `labview-unit-test-framework-toolkit`
- source_path: `configuring-a-test-to-use-a-user-defined-test.html`
- source_url: https://docs-be.ni.com/bundle/labview-unit-test-framework-toolkit/raw/resource/enus/configuring-a-test-to-use-a-user-defined-test.html
- document_id: `labview-unit-test-framework-toolkit`
- page_type: `leaf`
- content_type: `task`
- source_description: Complete the following steps to configure a test to use a user-defined test VI.Open the LabVIEW project that contains the files on which you want to perform unit testing. Double-click an .lvtest file to display the Test Properties dialog box. On the Configuration page, place a checkmark in the Use u

### Configuring a Test to Use a User-Defined Test VI

Complete the following steps to configure a test
 to use a user-defined test VI.

1. Open the LabVIEW project that contains the files on which you want to perform unit testing.
2. Double-click an .lvtest file to display
 the Test Properties dialog box.
3. On the Configuration page, place a
 checkmark in the Use user-defined test
 VI checkbox. Note When you place a checkmark in the
 Use user-defined test VI
 checkbox, LabVIEW dims the Test
 Cases page and the
 Setup/Teardown page in the
 Test Properties dialog
 box.
4. Click the Browse button next to the
 Use user-defined test VI file
 path text box. A file dialog box
 appears.
5. Navigate to and select the user-defined test VI you want to use. Click the OK button.
6. Click the OK button to close the dialog
 box and return to the Project
 Explorer window.
7. Select File»Save to save the project.

Parent topic:

Configure Tests

Related tasks:

- Creating a User-Defined Test VI

<!--NI_TOPIC bundle=labview-unit-test-framework-toolkit path=configuring-advanced-settings-of-tests.html language=enus -->
## TOPIC 00009: Configure Advanced Settings of Tests

- bundle_id: `labview-unit-test-framework-toolkit`
- source_path: `configuring-advanced-settings-of-tests.html`
- source_url: https://docs-be.ni.com/bundle/labview-unit-test-framework-toolkit/raw/resource/enus/configuring-advanced-settings-of-tests.html
- document_id: `labview-unit-test-framework-toolkit`
- page_type: `leaf`
- content_type: `concept`
- source_description: Use the Advanced page of the Test Properties dialog box to configure advanced settings of tests.The settings on this page apply to only the .lvtest file you are configuring and override the global settings specified on the Unit Test Framework page of the Project Properties dialog box.

### Configure Advanced Settings of Tests

Advanced

Test Properties

Note

.lvtest

Unit Test Framework

Project Properties

- [Specifying a Timeout for a Test](specifying-a-timeout-for-a-test.html)
- [Specifying a Minimum Code Coverage Requirement](specifying-a-minimum-code-coverage-requiremen.html)
- [Specifying the Number of Times to Repeat a Test](specifying-the-number-of-times-to-repeat-a-te.html)
- [Specifying the Digits of Precision for Floating-Point Comparison](specifying-the-digits-of-precision-for-floati.html)
- [Configuring the Input/Output Setting of the VI under Test](configuring-the-input-output-setting-of-the-v.html)

Parent topic:

Configure Tests

<!--NI_TOPIC bundle=labview-unit-test-framework-toolkit path=configuring-tests-to-run-setup-and-teardown-v.html language=enus -->
## TOPIC 00010: Configuring Tests to Run Setup and Teardown VIs

- bundle_id: `labview-unit-test-framework-toolkit`
- source_path: `configuring-tests-to-run-setup-and-teardown-v.html`
- source_url: https://docs-be.ni.com/bundle/labview-unit-test-framework-toolkit/raw/resource/enus/configuring-tests-to-run-setup-and-teardown-v.html
- document_id: `labview-unit-test-framework-toolkit`
- page_type: `leaf`
- content_type: `task`
- source_description: Use the Setup/Teardown page of the Test Properties dialog box to configure tests to run setup and teardown VIs. You also can configure tests to run setup and teardown VIs by editing .lvtest files. Complete the following steps to configure a test to run setup and teardown VIs: Open the LabVIEW projec

### Configuring Tests to Run Setup and Teardown VIs

Use the Setup/Teardown page of the Test
 Properties dialog box to configure tests to run setup and teardown
 VIs. You also can configure tests to run setup and teardown VIs by editing
 .lvtest files.

Complete the following steps to configure a test to run setup and teardown VIs:

1. Open the LabVIEW project that contains the files on which you want to perform unit testing.
2. Double-click an .lvtest file to display the
 Test Properties dialog box
3. Select Setup/Teardown from the
 Category list to display the
 Setup/Teardown page
4. Click the Browse button next to the Setup
 VI text box. A file dialog box appears.
5. Navigate to and select the VI you want to use as the setup VI. Click the OK button.
6. Select an output terminal from the Outputs of Setup VI column for each Inputs of VI under Test you want to pass values to.
7. Click the Browse button next to the Teardown
 VI text box. A file dialog box appears.
8. Navigate to and select the VI you want to use as the teardown VI. Click the OK button.
9. Select an input terminal from the Inputs of Teardown VI
 column for each Outputs of VI under Test you want to
 retrieve values from.
10. Enter the input values, expected values, and comparison types of the setup and teardown VIs for a test case.
11. Click the OK button to close the dialog box and return
 to the Project Explorer window.
12. Select File»Save to save the project.

The next time you execute this test, LabVIEW first runs the setup VI by using the
 input values and then passes the output values from the setup VI to the inputs of the VI
 under test. LabVIEW then checks the VI under test for functional correctness and passes
 the resulting values from the VI under test to the inputs of the teardown VI. LabVIEW
 compares the outputs of the teardown VI with the expected values.

Parent topic:

Configure Tests

Related tasks:

- Entering Input Values, Expected Values, and Comparison Types

<!--NI_TOPIC bundle=labview-unit-test-framework-toolkit path=configuring-tests.html language=enus -->
## TOPIC 00011: Configure Tests

- bundle_id: `labview-unit-test-framework-toolkit`
- source_path: `configuring-tests.html`
- source_url: https://docs-be.ni.com/bundle/labview-unit-test-framework-toolkit/raw/resource/enus/configuring-tests.html
- document_id: `labview-unit-test-framework-toolkit`
- page_type: `leaf`
- content_type: `concept`
- source_description: Use the Project Explorer window to configure tests interactively. You also can configure tests by editing .lvtest files.Read the following pages to learn step-by-step instructions for configuring tests and test cases in a LabVIEW project:

### Configure Tests

Use the Project Explorer window to configure tests interactively.
 You also can configure tests by editing .lvtest files.

Read the following pages to learn step-by-step instructions for configuring tests and test cases
 in a LabVIEW project:

- [Specifying a Test Priority](specifying-a-test-priority.html)
- [Specifying Requirement IDs](specifying-requirement-ids.html)
- [Configuring a Test to Use a User-Defined Test VI](configuring-a-test-to-use-a-user-defined-test.html)
- [Configuring a Test to Skip](configuring-a-test-to-skip.html)
- [Entering Input Values, Expected Values, and Comparison Types](entering-input-values-expected-values-and-com.html)
- [Exchanging Values Between the VI under Test, Setup VI, Teardown VI, and the Test Cases Page](exchanging-values-between-the-vi-under-test-s.html)
- [Adding or Duplicating Test Cases](adding-or-duplicating-test-cases.html)
- [Deleting Test Cases](deleting-test-cases-unit-test-framework.html)
- [Configuring Tests to Run Setup and Teardown VIs](configuring-tests-to-run-setup-and-teardown-v.html)
- [Editing .lvtest Files](editing-lvtest-files.html)
- [Configure Advanced Settings of Tests](configuring-advanced-settings-of-tests.html)

Parent topic:

Unit Test Framework Toolkit

Related concepts:

- Tests and .lvtest Files

<!--NI_TOPIC bundle=labview-unit-test-framework-toolkit path=configuring-the-input-output-setting-of-the-v.html language=enus -->
## TOPIC 00012: Configuring the Input/Output Setting of the VI under Test

- bundle_id: `labview-unit-test-framework-toolkit`
- source_path: `configuring-the-input-output-setting-of-the-v.html`
- source_url: https://docs-be.ni.com/bundle/labview-unit-test-framework-toolkit/raw/resource/enus/configuring-the-input-output-setting-of-the-v.html
- document_id: `labview-unit-test-framework-toolkit`
- page_type: `leaf`
- content_type: `task`
- source_description: Complete the following steps to configure which controls and indicators of the VI under test appear on the Test Cases page.Open the LabVIEW project that contains the files on which you want to perform unit testing. Double-click an .lvtest file. to display the Test Properties dialog box. Select Advan

### Configuring the Input/Output Setting of the VI under Test

Test Cases

1. Open the LabVIEW project that contains the files on which you want to perform unit testing.
2. Double-click an .lvtest file. to display the
 Test Properties dialog box.
3. Select Advanced from the Category
 list to display the Advanced page.
4. Click the Input/output values list and select which
 controls and indicators of the VI under test appear on the Test
 Cases page. Note If you select
 the Include controls and indicators from connector
 pane setting, make sure you select a connector pane pattern
 and assign terminals for the VI under test.
5. Click the OK button to close the dialog box and return
 to the Project Explorer window.
6. Select File»Save to save the project.

Parent topic:

Configure Advanced Settings of Tests

<!--NI_TOPIC bundle=labview-unit-test-framework-toolkit path=create-test-from-lvtest-file.html language=enus -->
## TOPIC 00013: Creating a Test from an .lvtest File

- bundle_id: `labview-unit-test-framework-toolkit`
- source_path: `create-test-from-lvtest-file.html`
- source_url: https://docs-be.ni.com/bundle/labview-unit-test-framework-toolkit/raw/resource/enus/create-test-from-lvtest-file.html
- document_id: `labview-unit-test-framework-toolkit`
- page_type: `leaf`
- content_type: `task`
- source_description: Complete the following steps to create a test from an .lvtest file on disk. Open the LabVIEW project that contains the files on which you want to perform unit testing. Right-click a VI and select Unit Tests»Add Test from File from the shortcut menu. A file dialog box appears. Navigate to and select

### Creating a Test from an .lvtest File

.lvtest

1. Open the LabVIEW project that contains the files on which you want to perform
 unit testing.
2. Right-click a VI and select Unit Tests»Add Test from File from the shortcut menu. A file dialog box appears.
3. Navigate to and select the .lvtest file you want to use.
 Click the OK button. LabVIEW adds the
 .lvtest file to the project tree. 
 Note If the
 .lvtest file was associated with a different VI
 previously, the .lvtest file now is associated with the
 new VI. You can specify only one VI under test for each
 .lvtest file.
4. Select File»Save to save the project.

Parent topic:

Create Tests

<!--NI_TOPIC bundle=labview-unit-test-framework-toolkit path=create-test-from-userdefined-test-vi.html language=enus -->
## TOPIC 00014: Creating a Test from a User-Defined Test VI

- bundle_id: `labview-unit-test-framework-toolkit`
- source_path: `create-test-from-userdefined-test-vi.html`
- source_url: https://docs-be.ni.com/bundle/labview-unit-test-framework-toolkit/raw/resource/enus/create-test-from-userdefined-test-vi.html
- document_id: `labview-unit-test-framework-toolkit`
- page_type: `leaf`
- content_type: `task`
- source_description: Complete the following steps to create a test from a user-defined test VI. Open the LabVIEW project that contains the files on which you want to perform unit testing. Right-click a VI and select Unit Tests»New User-Defined Test from the shortcut menu. A Save dialog box appears. LabVIEW automatically

### Creating a Test from a User-Defined Test
 VI

Complete the following steps to create a test from a
 user-defined test VI.

1. Open the LabVIEW project that contains the files on which you want to perform
 unit testing.
2. Right-click a VI and select Unit Tests»New User-Defined Test from the shortcut menu. A Save dialog box
 appears. LabVIEW automatically creates a user-defined test VI from the
 User-Defined Test Template.vit file located in the
 labview\templates\UnitTestFramework directory. You also
 can find the template file by selecting File»New to display the New dialog box and
 selecting VI»From Template»Unit Test Framework.
3. Enter a filename for the user-defined test VI.
4. Click the OK button to save the user-defined test VI.
 LabVIEW automatically creates a test and configures the test to use the
 user-defined test VI. LabVIEW saves the .lvtest file in the
 same location as the user-defined test VI.
5. Select File»Save to save the project.
6. Modify the user-defined test VI to define your own test.

Parent topic:

Create Tests

<!--NI_TOPIC bundle=labview-unit-test-framework-toolkit path=create-test-from-vi.html language=enus -->
## TOPIC 00015: Creating a Test from a VI

- bundle_id: `labview-unit-test-framework-toolkit`
- source_path: `create-test-from-vi.html`
- source_url: https://docs-be.ni.com/bundle/labview-unit-test-framework-toolkit/raw/resource/enus/create-test-from-vi.html
- document_id: `labview-unit-test-framework-toolkit`
- page_type: `leaf`
- content_type: `task`
- source_description: Complete the following steps to create a test from a VI. Open the LabVIEW project that contains the files on which you want to perform unit testing. Right-click a VI and select Unit Tests»New Test from the shortcut menu. You also can create tests from multiple VIs by pressing the Ctrl key while clic

### Creating a Test from a VI

Complete the following steps to create a test from a
 VI.

1. Open the LabVIEW project that contains the files on which you want to perform
 unit testing.
2. Right-click a VI and select Unit Tests»New Test from the shortcut menu. 
 Note You also can
 create tests from multiple VIs by pressing the Ctrl
 key while clicking each VI. Then right-click the selection and select
 New Unit Tests from the shortcut menu. LabVIEW
 creates an .lvtest file for each VI.
3. Configure the .lvtest file you just created.
4. Select File»Save to save the project.

Parent topic:

Create Tests

Related concepts:

- Configure Tests

<!--NI_TOPIC bundle=labview-unit-test-framework-toolkit path=creating-a-user-defined-comparison-vi.html language=enus -->
## TOPIC 00016: Creating a User-Defined Comparison VI

- bundle_id: `labview-unit-test-framework-toolkit`
- source_path: `creating-a-user-defined-comparison-vi.html`
- source_url: https://docs-be.ni.com/bundle/labview-unit-test-framework-toolkit/raw/resource/enus/creating-a-user-defined-comparison-vi.html
- document_id: `labview-unit-test-framework-toolkit`
- page_type: `leaf`
- content_type: `task`
- source_description: Complete the following steps to create a user-defined comparison VI.Select File»New VI to create a new, blank VI.On the Controls palette, select Modern»Variant & Class to display the Variant & Class palette.Add a variant to the front panel and label the variant Resulting Value.Right-click the varian

### Creating a User-Defined Comparison VI

Complete the following steps to create a user-defined
 comparison VI.

1. Select File»New VI to create a new, blank VI.
2. On the Controls palette, select Modern»Variant & Class to display the Variant & Class
 palette.
3. Add a variant to the front panel and label the variant Resulting
 Value.
4. Right-click the variant and select Change to Control from the shortcut menu.
5. Add another variant to the front panel and label the variant
 Expected Value.
6. Right-click the Expected Value variant and select Change to Control from the shortcut menu.
7. On the Controls palette, select Modern»Boolean to display the Boolean palette.
8. Add a Round LED or Square LED
 Boolean indicator to the front panel and label the Boolean indicator
 Comparison Result.
9. Right-click the connector pane and select Patterns from
 the shortcut menu. Select the following connector pane pattern [IMAGE alt='image' src='GUID-5AAB3626-DC23-4B9B-B068-B852CCBF44C6-a5.gif'].
10. Assign each of the following connector pane terminals to a front panel control
 or indicator. Note You must
 configure the connector pane properly in order for the user-defined
 comparison VI to work properly.
  1. Top left terminal to the Resulting Value variant
 control.
  2. Bottom left terminal to the Expected Value
 variant control.
  3. Right terminal to the Comparison Result Boolean
 indicator.
11. Display the block diagram by selecting Window»Show Block Diagram.
12. Add or define your own comparison to the block diagram.
13. Wire the Resulting Value and Expected Value variant controls to the comparison.
14. Wire the result of the comparison to the Comparison
 Result Boolean indicator. Note The comparison must return a
 Boolean data type.
15. Select File»Save As to save this user-defined comparison VI in an easily accessible
 location.

Parent topic:

Create Projects and Tests

<!--NI_TOPIC bundle=labview-unit-test-framework-toolkit path=creating-a-user-defined-test-vi.html language=enus -->
## TOPIC 00017: Creating a User-Defined Test VI

- bundle_id: `labview-unit-test-framework-toolkit`
- source_path: `creating-a-user-defined-test-vi.html`
- source_url: https://docs-be.ni.com/bundle/labview-unit-test-framework-toolkit/raw/resource/enus/creating-a-user-defined-test-vi.html
- document_id: `labview-unit-test-framework-toolkit`
- page_type: `leaf`
- content_type: `task`
- source_description: Complete the following steps to create a user-defined test VI. Create a user-defined test VI from the User-Defined Test Template.vit file in one of the following ways: Select File»New to display the New dialog box and select VI»From Template»Unit Test Framework to open the User-Defined Test Template

### Creating a User-Defined Test VI

Complete the following steps to create a user-defined test
 VI.

1. Create a user-defined test VI from the User-Defined Test
 Template.vit file in one of the following ways:
  - Select File»New to display the New dialog box and
 select VI»From Template»Unit Test Framework to open the User-Defined Test
 Template.vit file. You also can locate this file in the
 labview\templates\UnitTestFramework 
 directory.
  - Create a test from a user-defined test VI. The test and user-defined
 test VI appear in the Project Explorer window.
 Right-click the user-defined test VI and select
 Open .
2. Modify the VI to define your own test. Keep in mind the following requirements
 for the user-defined test VI: Do not modify the Unit Test Framework Result
 indicator name or cluster elements.The Unit Test Framework Result indicator contains the following
 three cluster elements: Element NameData TypeNotesRequiredtime elapsed [ms]Numeric indicatorTime in milliseconds.Noresult (test)EnumEnum values must be Passed,
 Failed, Error,
 Skipped, and Not
 Processed.Yesresult
 (parameters)Array of clusterEach array is a cluster of comparison results
 between the expected and resulting values.NoNote You must
 include data from this element in the Unit Test Framework
 Result indicator.The Unit Test Framework Result indicator must be
 connected to the connector pane.
3. Wire the result of your test to the result (test) element.
4. Optional: For advanced test VIs, wire the results of your tests to the time
 elapsed [ms] and results (parameters)
 elements.
5. Select File»Save As to save this user-defined test VI in an easily accessible
 location. Note If you rename a user-defined
 test VI that you create from the shortcut menu, you must specify the new
 User-defined test VI file path on the
 Configuration page of the Test
 Properties dialog box.

Parent topic:

Create Projects and Tests

Related tasks:

- Creating a Test from a User-Defined Test VI

<!--NI_TOPIC bundle=labview-unit-test-framework-toolkit path=creating-projects-and-tests.html language=enus -->
## TOPIC 00018: Create Projects and Tests

- bundle_id: `labview-unit-test-framework-toolkit`
- source_path: `creating-projects-and-tests.html`
- source_url: https://docs-be.ni.com/bundle/labview-unit-test-framework-toolkit/raw/resource/enus/creating-projects-and-tests.html
- document_id: `labview-unit-test-framework-toolkit`
- page_type: `leaf`
- content_type: `concept`
- source_description: Use this section to learn step-by-step instructions for creating tests in a LabVIEW project.You must create and save a LabVIEW project before you can use the LabVIEW Unit Test Framework Toolkit to create tests. Use projects to group together all the files you need to perform unit testing.

### Create Projects and Tests

Note

- [Create Tests](creating-tests.html)
- [Creating a User-Defined Test VI](creating-a-user-defined-test-vi.html)
- [Creating a User-Defined Comparison VI](creating-a-user-defined-comparison-vi.html)
- [Storing VI Passwords for Unit Testing](storing-vi-passwords-for-unit-testing.html)

Parent topic:

Unit Test Framework Toolkit

Related concepts:

- Tests and .lvtest Files

<!--NI_TOPIC bundle=labview-unit-test-framework-toolkit path=creating-test-vector-files-and-test-vectors.html language=enus -->
## TOPIC 00019: Create Test Vector Files and Test Vectors

- bundle_id: `labview-unit-test-framework-toolkit`
- source_path: `creating-test-vector-files-and-test-vectors.html`
- source_url: https://docs-be.ni.com/bundle/labview-unit-test-framework-toolkit/raw/resource/enus/creating-test-vector-files-and-test-vectors.html
- document_id: `labview-unit-test-framework-toolkit`
- page_type: `leaf`
- content_type: `concept`
- source_description: Use this section to learn step-by-step instructions for creating and using test vector files and test vectors in a LabVIEW project.You must create and save a LabVIEW project before you can use the LabVIEW Unit Test Framework Toolkit to create test vector files and test vectors.

### Create Test Vector Files and Test
 Vectors

Note

- [Creating Test Vector Files](creating-test-vector-files.html)
- [Creating Test Vectors in a Test Vector File](creating-test-vectors-in-a-test-vector-file.html)
- [Editing Test Vectors](editing-test-vectors.html)
- [Exporting and Importing Test Vectors](exporting-and-importing-test-vectors.html)
- [Assigning Test Vectors in Test Cases](assigning-test-vectors-in-test-cases.html)

Parent topic:

Unit Test Framework Toolkit

<!--NI_TOPIC bundle=labview-unit-test-framework-toolkit path=creating-test-vector-files.html language=enus -->
## TOPIC 00020: Creating Test Vector Files

- bundle_id: `labview-unit-test-framework-toolkit`
- source_path: `creating-test-vector-files.html`
- source_url: https://docs-be.ni.com/bundle/labview-unit-test-framework-toolkit/raw/resource/enus/creating-test-vector-files.html
- document_id: `labview-unit-test-framework-toolkit`
- page_type: `leaf`
- content_type: `task`
- source_description: Complete the following steps to create a test vector file.Open the LabVIEW project for which you want to create a test vector file.Right-click My Computer and select New»Test Vectors from the shortcut menu.LabVIEW creates a .lvvect file to save the test vector file. Double-click a .lvvect file in th

### Creating Test Vector Files

Complete the following steps to create a test vector
 file.

1. Open the LabVIEW project for which you want to create a test vector file.
2. Right-click My Computer and select New»Test Vectors from the shortcut menu. LabVIEW creates a .lvvect file to save the test vector
 file.
3. Optional: 
 Double-click a .lvvect file in the Project
 Explorer window to display the Test Vector File
 Properties dialog box. You also can right-click the
 .lvvect file and select
 Properties from the shortcut menu to open the dialog
 box to configure the test vector file you just created.
4. Optional: Save the changes you made to the test vector file.
5. Select File»Save to save the project.

After you create a test vector file, you can create test vectors or add other test vector files
 to this test vector file.

Parent topic:

Create Test Vector Files and Test Vectors

<!--NI_TOPIC bundle=labview-unit-test-framework-toolkit path=creating-test-vectors-in-a-test-vector-file.html language=enus -->
## TOPIC 00021: Creating Test Vectors in a Test Vector File

- bundle_id: `labview-unit-test-framework-toolkit`
- source_path: `creating-test-vectors-in-a-test-vector-file.html`
- source_url: https://docs-be.ni.com/bundle/labview-unit-test-framework-toolkit/raw/resource/enus/creating-test-vectors-in-a-test-vector-file.html
- document_id: `labview-unit-test-framework-toolkit`
- page_type: `leaf`
- content_type: `task`
- source_description: Complete the following steps to create test vectors in a test vector file.Open the LabVIEW project that contains the test vector file in which you want to create test vectors. Double-click a .lvvect file in the Project Explorer window. The Test Vector File Properties dialog box appears. Click the Ne

### Creating Test Vectors in a Test Vector File

Complete the following steps to create test vectors in a
 test vector file.

1. Open the LabVIEW project that contains the test vector file in which you want
 to create test vectors.
2. Double-click a .lvvect file in the Project
 Explorer window. 
 The Test Vector File Properties dialog box
 appears.
3. Click the New button. 
 The Test Vector Properties - New dialog box
 appears.
4. Specify a name in the Name field.
5. Specify the data type of the test vector in the Data type field.
6. Specify the element number of this test vector in the Size field. You can change the element number when you edit a test vector.
7. Click the OK button to close the Test Vector
 Properties - New dialog box and create the test vector.
8. Optional: Repeat step 3 through 7 to create multiple test vectors.
9. Click the Save button to close the Test
 Vector File Properties dialog box and save the test vector
 file.

Parent topic:

Create Test Vector Files and Test Vectors

<!--NI_TOPIC bundle=labview-unit-test-framework-toolkit path=creating-tests.html language=enus -->
## TOPIC 00022: Create Tests

- bundle_id: `labview-unit-test-framework-toolkit`
- source_path: `creating-tests.html`
- source_url: https://docs-be.ni.com/bundle/labview-unit-test-framework-toolkit/raw/resource/enus/creating-tests.html
- document_id: `labview-unit-test-framework-toolkit`
- page_type: `leaf`
- content_type: `concept`
- source_description: Use the Project Explorer window to create tests interactively. You can create tests from VIs, existing .lvtest files, or user-defined test VIs.You must create and save a LabVIEW project before you can use the LabVIEW Unit Test Framework Toolkit to create tests. Use projects to group together all the

### Create Tests

Project Explorer

.lvtest

Note

Project Explorer

.lvtest

.lvtest

Items

Files

.lvtest

Note

.lvtest

Default location file path

Unit Test Framework

Project
 Properties

- [Creating a Test from a VI](create-test-from-vi.html)
- [Creating a Test from an .lvtest File](create-test-from-lvtest-file.html)
- [Creating a Test from a User-Defined Test VI](create-test-from-userdefined-test-vi.html)

Parent topic:

Create Projects and Tests

Related concepts:

- Tests and .lvtest Files

<!--NI_TOPIC bundle=labview-unit-test-framework-toolkit path=customizing-test-reports.html language=enus -->
## TOPIC 00023: Customizing Test Reports

- bundle_id: `labview-unit-test-framework-toolkit`
- source_path: `customizing-test-reports.html`
- source_url: https://docs-be.ni.com/bundle/labview-unit-test-framework-toolkit/raw/resource/enus/customizing-test-reports.html
- document_id: `labview-unit-test-framework-toolkit`
- page_type: `leaf`
- content_type: `topic`
- source_description: You can customize test reports by specifying the contents of the reports. You can also format HTML reports by using a Cascading Style Sheet (CSS) file. Customizing Report ContentsComplete the following steps to specify the types of results to include in test reports:Open the LabVIEW project that con

### Customizing Test Reports

You can customize test reports by specifying the contents of the reports. You can
 also format HTML reports by using a Cascading Style Sheet (CSS) file.

#### Customizing Report
 Contents

Complete the following steps to specify the types of results to
 include in test reports:

1. Open the LabVIEW project that contains the files on which you want to perform
 unit testing.
2. Click the Project Properties button on the
 Project toolbar to display the Project
 Properties dialog box.
3. Select Unit Test Framework from the Category 
 list to display the Unit Test Framework page.
4. Place a checkmark in the checkbox of each type of results you want to include in
 test reports.
5. Click the OK button to close the dialog box and return to the
 Project Explorer window.

#### Formatting HTML Reports

Complete the following steps to format
 HTML reports by using a CSS file:

1. Open the LabVIEW project that contains the files on which you want to perform
 unit testing.
2. Click the Project Properties button on the
 Project toolbar to display the Project
 Properties dialog box.
3. Select Unit Test Framework from the Category 
 list to display the Unit Test Framework page.
4. Make sure the Generate HTML report checkbox contains a
 checkmark.
5. In the Report Details section, place a checkmark in the
 Use user-defined CSS file checkbox.
6. Click the Browse button next to the CSS file path 
 text box. A file dialog box appears.
7. Navigate to and select the CSS file you want to use to customize HTML reports.
 Click the OK button.
8. Click the OK button to close the dialog box and return to the
 Project Explorer window.

Parent topic:

View Test Results and Generating Reports

Related concepts:

- Test Results

<!--NI_TOPIC bundle=labview-unit-test-framework-toolkit path=deleting-test-cases-unit-test-framework.html language=enus -->
## TOPIC 00024: Deleting Test Cases

- bundle_id: `labview-unit-test-framework-toolkit`
- source_path: `deleting-test-cases-unit-test-framework.html`
- source_url: https://docs-be.ni.com/bundle/labview-unit-test-framework-toolkit/raw/resource/enus/deleting-test-cases-unit-test-framework.html
- document_id: `labview-unit-test-framework-toolkit`
- page_type: `leaf`
- content_type: `task`
- source_description: Complete the following steps to delete a test case.Open the LabVIEW project that contains the files on which you want to perform unit testing. Double-click an .lvtest file to display the Test Properties dialog box. Select Test Cases from the Category list to display the Test Cases page.If this test

### Deleting Test Cases

Complete the following steps to delete a test
 case.

1. Open the LabVIEW project that contains the files on which you want to perform unit testing.
2. Double-click an .lvtest file to display the
 Test Properties dialog box.
3. Select Test Cases from the Category list to display the
 Test Cases page.
4. If this test has more than one test case, use the Test Case control to select the test case you want to delete.
5. Click the Delete button [IMAGE alt='image' src='GUID-21730690-F31A-47A1-95D0-7F98A9F15CFC-a5.png'] to
 delete this test case. 
 Note If this test
 has only one test case, LabVIEW resets the input and expected values to 0
 and the comparison types to =
6. Select File»Save to save the project.

Parent topic:

Configure Tests

<!--NI_TOPIC bundle=labview-unit-test-framework-toolkit path=editing-lvtest-files.html language=enus -->
## TOPIC 00025: Editing .lvtest Files

- bundle_id: `labview-unit-test-framework-toolkit`
- source_path: `editing-lvtest-files.html`
- source_url: https://docs-be.ni.com/bundle/labview-unit-test-framework-toolkit/raw/resource/enus/editing-lvtest-files.html
- document_id: `labview-unit-test-framework-toolkit`
- page_type: `leaf`
- content_type: `task`
- source_description: When you create a test from the Project Explorer window, LabVIEW creates an .lvtest file on disk. Each .lvtest file contains the settings LabVIEW uses to check the VI under test for functional correctness. You can view or edit .lvtest files by using Microsoft Excel or a text editor.If you use Micros

### Editing .lvtest Files

When you create a test from the Project Explorer window,
 LabVIEW creates an .lvtest file on disk. Each
 .lvtest file contains the settings LabVIEW uses to check
 the VI under test for functional correctness. You can view or edit
 .lvtest files by using Microsoft Excel or a text
 editor.

Note

.lvtest

.lvtest

.lvtest

.lvtest

.lvtest

Note

.lvtest

Unit Test
 Framework

Project Properties

1. Open the LabVIEW project that contains the files on which you want to perform
 unit testing.
2. Right-click an .lvtest file and select Open in
 External Editor. You also can open .lvtest
 files directly from Windows Explorer by right-clicking an
 .lvtest file and opening the file with Microsoft
 Excel. 
 Note If you
 double-click an .lvtest file from Windows Explorer,
 LabVIEW launches but does not open any project or dialog box. You must
 right-click the .lvtest file to open the file with
 Microsoft Excel.
3. Edit the .lvtest file to configure settings for this test.
 Make sure you follow the .lvtest file format. 
 Caution Do not
 remove any lines from the .lvtest file. If you remove
 anything, the test might not execute properly.
4. Save and close the .lvtest file.
5. Select File»Save to save the project.

Parent topic:

Configure Tests

Related concepts:

- Create Tests
- Tests and .lvtest Files

<!--NI_TOPIC bundle=labview-unit-test-framework-toolkit path=editing-test-vectors.html language=enus -->
## TOPIC 00026: Editing Test Vectors

- bundle_id: `labview-unit-test-framework-toolkit`
- source_path: `editing-test-vectors.html`
- source_url: https://docs-be.ni.com/bundle/labview-unit-test-framework-toolkit/raw/resource/enus/editing-test-vectors.html
- document_id: `labview-unit-test-framework-toolkit`
- page_type: `leaf`
- content_type: `task`
- source_description: Complete the following steps to edit test vectors. Double-click a .lvvect file in the Project Explorer window. The Test Vector File Properties dialog box appears. Click the Edit Values button.The Test Vector Properties - Edit dialog box appears.Specify a name in the Name cell of a test vector if you

### Editing Test Vectors

Complete the following steps to edit test
 vectors.

1. Double-click a .lvvect file in the Project
 Explorer window. 
 The Test Vector File Properties dialog box
 appears.
2. Click the Edit Values button. The Test Vector Properties - Edit dialog box
 appears.
3. Optional: Specify a name in the Name cell of a test vector if you
 want to rename this test vector.
4. Optional: Specify a test vector in the Append to cell if you want
 to append the values of a test vector to values of another test vector.
5. Optional: 
 Specify a requirement ID in the Requirement ID cell if
 you want to use a test vector with Requirements Gateway. 
 Ensure the requirement IDs match the corresponding requirements in
 Requirements Gateway.
6. Specify a test vector type in the Edit Type cell of the
 test vector that you want to edit. The default is sequence.
7. Specify test vector values in the Value cell of the test vector that you
 want to edit. If you want to add multiple values to this test vector, you can enter the new
 values in the cells below the Value cell.Note You can export
 the test vector to an array control of a VI, edit the values in the array
 control, and import the updated values to the test vector. The array control
 must have a proper data type.
8. Optional: Repeat step 3 through 7 to edit multiple test vectors.
9. Click the OK button to close this dialog box and save
 the test vectors.

Parent topic:

Create Test Vector Files and Test Vectors

Related concepts:

- Requirement IDs
- Test Vectors and .lvvect Files

<!--NI_TOPIC bundle=labview-unit-test-framework-toolkit path=entering-input-values-expected-values-and-com.html language=enus -->
## TOPIC 00027: Entering Input Values, Expected Values, and Comparison Types

- bundle_id: `labview-unit-test-framework-toolkit`
- source_path: `entering-input-values-expected-values-and-com.html`
- source_url: https://docs-be.ni.com/bundle/labview-unit-test-framework-toolkit/raw/resource/enus/entering-input-values-expected-values-and-com.html
- document_id: `labview-unit-test-framework-toolkit`
- page_type: `leaf`
- content_type: `task`
- source_description: Complete the following steps to enter the input values, expected values, and comparison types for a test case.LabVIEW lists the controls and indicators from the VI under test on the Test Cases page. If the Input/output values setting on the Unit Test Framework page of the Project Properties dialog b

### Entering Input Values, Expected Values, and Comparison Types

Note

Test
 Cases

Input/output values

Unit Test Framework

Project Properties

Include
 controls and indicators from connector pane

Tip

Test Properties

1. Open the LabVIEW project that contains the files on which you want to perform unit testing.
2. Double-click an .lvtest file to display the
 Test Properties dialog box is displayed.
3. Select Test Cases from the
 Category list to display the Test
 Cases page.
4. If this test has more than one test case, use the Test Case control to
 select the test case you want to configure.
5. Click the Input Value text box of the input terminal you
 want to configure and enter a value. Press the <Tab> key to move to the
 value in the next cell and press <Shift-Tab> to switch to the value in the
 previous cell. 
 Tip You also can
 exchange values between the VI under test, setup VI, teardown VI, and the
 Test Cases page, accessible by clicking the
 Export Values to VI button or the
 Import Values from VI button.
6. Click the Expected Value text box of the output terminal you want to configure and enter a value. Repeat this step for other output terminals.
7. Select a comparison type from the Comparison list of the
 output terminal you want to configure. Repeat this step for other output
 terminals. 
 Note LabVIEW lists
 the available comparison types that each data type supports. You also can
 use a user-defined comparison VI by selecting
 user-defined from the
 Comparison list and selecting a user-defined
 comparison VI.
8. Optional: 
 Remove the checkmark from each input or output terminal that you do not want to
 test during execution. 
 Tip You can select
 multiple entries by pressing the <Ctrl> key while clicking each entry.
 Then right-click the selection and select Uncheck All
 Items or Check All Items.
9. Optional: 
 Click the Run button [IMAGE alt='image' src='GUID-0FBF9E7D-FEC1-4B55-B97E-56F606B7790B-a5.png'] to test the single test case.
10. Click the OK button to close the dialog box and return
 to the Project Explorer window.
11. Select File»Save to save the project.

Parent topic:

Configure Tests

Related tasks:

- Creating a User-Defined Comparison VI

<!--NI_TOPIC bundle=labview-unit-test-framework-toolkit path=exchanging-values-between-the-vi-under-test-s.html language=enus -->
## TOPIC 00028: Exchanging Values Between the VI under Test, Setup VI, Teardown VI, and the Test Cases Page

- bundle_id: `labview-unit-test-framework-toolkit`
- source_path: `exchanging-values-between-the-vi-under-test-s.html`
- source_url: https://docs-be.ni.com/bundle/labview-unit-test-framework-toolkit/raw/resource/enus/exchanging-values-between-the-vi-under-test-s.html
- document_id: `labview-unit-test-framework-toolkit`
- page_type: `leaf`
- content_type: `task`
- source_description: You can modify the input and expected values by using the front panel of the VI under test, setup VI, and teardown VI and then importing these values to a test case. You also can export values from a test case to the VI under test, setup VI, and teardown VI.LabVIEW lists the controls and indicators

### Exchanging Values Between the VI under Test, Setup VI, Teardown VI, and the Test Cases Page

Note

Test Cases

Input/output values

Unit Test Framework

Project
 Properties

Include controls and
 indicators from connector pane

Complete the following steps to exchange values between the VI under test, setup VI, teardown VI,
 and the Test Cases page:

1. Open the LabVIEW project that contains the files on which you want to perform unit testing.
2. Double-click an .lvtest file. 
 The Test Properties dialog box
 displays.
3. Select Test Cases from the
 Category list. 
 The Test Cases page displays.
4. If this test has more than one test case, use the Test Case control to
 select the test case you want to configure.
5. Click the Export Values to VI button [IMAGE alt='image' src='GUID-BCB5769B-08BE-4854-AEFA-26D899148425-a5.png'] to
 export the input and expected values from the current test case to the VI under
 test, setup VI, and teardown VI. The VI under test, setup VI, and teardown VI
 open in a separate window. 
 Tip Use the
 Export Values to VI button to open the VI under
 test while configuring a test.
6. From the front panel of the VI under test, setup VI, and teardown VI, modify the values of any controls and indicators you want to configure.
7. On the Test Properties dialog box, click the
 Import Values from VI button [IMAGE alt='image' src='GUID-8A3DCE5C-8BCE-4143-BD71-5308E8CE260F-a5.png'] to
 import values from the VI under test, setup VI, and teardown VI to the current
 test case. 
 Note When you
 import values from the VI under test, setup VI, and teardown VI, LabVIEW
 replaces the input and expected values of the current test case with the
 values of the corresponding terminals in the VI under test, setup VI, and
 teardown VI.
8. Select a comparison type from the Comparison list of the output terminal
 you want to configure. Repeat this step for other output terminals.
9. Click the OK button to close the dialog box and return
 to the Project Explorer window.
10. Select File»Save to save the project.

The next time you execute this test, LabVIEW runs the setup VI and VI under test by using the
 input values you specified for each test case in the .lvtest
 file. LabVIEW then compares the resulting values with the expected values of the VI
 under test and teardown VI by using the comparison types you specified.

Parent topic:

Configure Tests

<!--NI_TOPIC bundle=labview-unit-test-framework-toolkit path=execute-all-tests-associated-with-a-lv-class.html language=enus -->
## TOPIC 00029: Executing All Tests Associated with a LabVIEW Class

- bundle_id: `labview-unit-test-framework-toolkit`
- source_path: `execute-all-tests-associated-with-a-lv-class.html`
- source_url: https://docs-be.ni.com/bundle/labview-unit-test-framework-toolkit/raw/resource/enus/execute-all-tests-associated-with-a-lv-class.html
- document_id: `labview-unit-test-framework-toolkit`
- page_type: `leaf`
- content_type: `task`
- source_description: Complete the following steps to execute all tests associated with a LabVIEW class.LabVIEW executes all tests associated with the LabVIEW class library you select and all tests in the project that are assigned to VIs in the LabVIEW class library. Open the LabVIEW project that contains the files on wh

### Executing All Tests Associated with a LabVIEW
 Class

Note

1. Open the LabVIEW project that contains the files on which you want to perform
 unit testing.
2. Right-click a LabVIEW class library file (.lvclass) and
 select Unit Tests»Run from the shortcut menu. 
 Note You can execute
 tests on classes that inherit from another LabVIEW class. Right-click the
 parent class library file and select Unit Tests»Run Including Children from the shortcut menu. LabVIEW executes all tests associated
 with the parent class and all tests associated with the children
 classes.

Parent topic:

Execute Tests Interactively

<!--NI_TOPIC bundle=labview-unit-test-framework-toolkit path=execute-all-tests-associated-with-a-vi.html language=enus -->
## TOPIC 00030: Executing All Tests Associated with a VI

- bundle_id: `labview-unit-test-framework-toolkit`
- source_path: `execute-all-tests-associated-with-a-vi.html`
- source_url: https://docs-be.ni.com/bundle/labview-unit-test-framework-toolkit/raw/resource/enus/execute-all-tests-associated-with-a-vi.html
- document_id: `labview-unit-test-framework-toolkit`
- page_type: `leaf`
- content_type: `task`
- source_description: Complete the following steps to execute all tests associated with a VI.LabVIEW cannot execute all tests associated with a VI if the VI and tests deploy to different targets. In this situation, you must follow the steps to execute tests in a LabVIEW project. Open the LabVIEW project that contains the

### Executing All Tests Associated with a
 VI

Caution

1. Open the LabVIEW project that contains the files on which you want to perform
 unit testing.
2. Right-click a VI and select Unit Tests»Run from the shortcut menu. 
 Note You also can
 execute tests associated with multiple VIs by pressing the <Ctrl> key
 while clicking each VI. Then right-click the selection and select
 Run Unit Tests from the shortcut menu.

Parent topic:

Execute Tests Interactively

<!--NI_TOPIC bundle=labview-unit-test-framework-toolkit path=execute-all-tests-in-a-project.html language=enus -->
## TOPIC 00031: Executing All Tests in a Project

- bundle_id: `labview-unit-test-framework-toolkit`
- source_path: `execute-all-tests-in-a-project.html`
- source_url: https://docs-be.ni.com/bundle/labview-unit-test-framework-toolkit/raw/resource/enus/execute-all-tests-in-a-project.html
- document_id: `labview-unit-test-framework-toolkit`
- page_type: `leaf`
- content_type: `task`
- source_description: Complete the following steps to execute all tests in a project. Open the LabVIEW project that contains the files on which you want to perform unit testing. Click the Run Unit Tests button on the Unit Test Framework toolbar.

### Executing All Tests in a Project

Complete the following steps to execute all tests in a
 project.

1. Open the LabVIEW project that contains the files on which you want to perform
 unit testing.
2. Click the Run Unit Tests button [IMAGE alt='image' src='GUID-B0847044-79E0-42F9-B623-46E9E73A9DC9-a5.gif'] on the Unit Test Framework
 toolbar.

Parent topic:

Execute Tests Interactively

Related concepts:

- Unit Test Framework Toolbar (Project Explorer Window)

<!--NI_TOPIC bundle=labview-unit-test-framework-toolkit path=execute-all-tests-in-folder-or-project-library.html language=enus -->
## TOPIC 00032: Executing All Tests in a Folder or Project Library

- bundle_id: `labview-unit-test-framework-toolkit`
- source_path: `execute-all-tests-in-folder-or-project-library.html`
- source_url: https://docs-be.ni.com/bundle/labview-unit-test-framework-toolkit/raw/resource/enus/execute-all-tests-in-folder-or-project-library.html
- document_id: `labview-unit-test-framework-toolkit`
- page_type: `leaf`
- content_type: `task`
- source_description: Complete the following steps to execute all tests in a virtual folder, folder, or LabVIEW project library. Open the LabVIEW project that contains the files on which you want to perform unit testing. Right-click a folder or project library and select Unit Tests»Run from the shortcut menu. You also ca

### Executing All Tests in a Folder or Project
 Library

Complete the following steps to execute all tests in a
 virtual folder, folder, or LabVIEW project library.

1. Open the LabVIEW project that contains the files on which you want to perform
 unit testing.
2. Right-click a folder or project library and select Unit Tests»Run from the shortcut menu. 
 Note You also can
 execute tests in multiple folders or project libraries by pressing the
 <Ctrl> key while clicking each folder or project library. Then
 right-click the selection and select Run Unit Tests
 from the shortcut menu.

Parent topic:

Execute Tests Interactively

<!--NI_TOPIC bundle=labview-unit-test-framework-toolkit path=execute-tests-from-lvtests-files.html language=enus -->
## TOPIC 00033: Executing Tests from .lvtest Files

- bundle_id: `labview-unit-test-framework-toolkit`
- source_path: `execute-tests-from-lvtests-files.html`
- source_url: https://docs-be.ni.com/bundle/labview-unit-test-framework-toolkit/raw/resource/enus/execute-tests-from-lvtests-files.html
- document_id: `labview-unit-test-framework-toolkit`
- page_type: `leaf`
- content_type: `task`
- source_description: Complete the following steps to create a VI that executes tests from .lvtest files programmatically. Select File»New VI to create a new, blank VI. Display the block diagram by selecting Window»Show Block Diagram . If you do not see the Functions palette, select View»Function Palette to display this

### Executing Tests from .lvtest Files

.lvtest

1. Select File»New VI to create a new, blank VI.
2. Display the block diagram by selecting Window»Show Block Diagram.
3. If you do not see the Functions palette, select View»Function Palette to display this palette.
4. On this palette, select Programming»Unit Test Framework. 
 The Unit Test Framework VIs appear.
5. Add the Run Tests from File VI to the block diagram.
6. Add the Open Results Window VI to the block diagram.
7. Wire the test results out output of the Run
 Tests from File VI to the test results in
 input of the Open Results Window VI.
8. Right-click the test file paths input of the
 Run Tests from File VI and select Create»Control from the shortcut menu. 
 A front panel control appears to the left of this VI. This control
 represents an array of paths to the .lvtest files that you
 want to execute.
9. Wire all error in and error out terminals on the block diagram.
10. Display the front panel and click the Browse button on
 the test file paths control to select an
 .lvtest file.
11. Optional: 
 Move the cursor over the test file paths control. When a
 double-headed arrow appears, click and drag the border of the control to add
 more elements to the array of paths. 
 You also can use the numeric control to display subsequent array elements. Add
 additional .lvtest files that you want to execute.
12. Select File»Save As and save this VI in an easily accessible location.
13. Click the Run button to run the VI. 
 Note When you
 execute tests from .lvtest files programmatically,
 LabVIEW executes tests in the order as they listed in the test
 file paths control.

Parent topic:

Execute Tests Programmatically

<!--NI_TOPIC bundle=labview-unit-test-framework-toolkit path=execute-tests-from-project.html language=enus -->
## TOPIC 00034: Executing Tests from a Project

- bundle_id: `labview-unit-test-framework-toolkit`
- source_path: `execute-tests-from-project.html`
- source_url: https://docs-be.ni.com/bundle/labview-unit-test-framework-toolkit/raw/resource/enus/execute-tests-from-project.html
- document_id: `labview-unit-test-framework-toolkit`
- page_type: `leaf`
- content_type: `task`
- source_description: Complete the following steps to create a VI that executes tests from a project programmatically. Select File»New VI to create a new, blank VI. Add the Run Tests from Project VI to the block diagram. Add the Open Results Window VI to the block diagram. Wire the test results out output of the Run Test

### Executing Tests from a Project

Complete the following steps to create a VI that executes
 tests from a project programmatically.

1. Select File»New VI to create a new, blank VI.
2. Add the Run Tests from Project VI to the block
 diagram.
3. Add the Open Results Window VI to the block diagram.
4. Wire the test results out output of the Run
 Tests from Project VI to the test results
 in input of the Open Results Window VI.
5. Right-click the project file path input of the
 Run Tests from Project VI and select Create»Control from the shortcut menu. A front panel control appears to the left
 of this VI. This control represents the path to the project file
 (.lvproj) that you want to execute tests.
6. Wire all error in and error out terminals on the block diagram.
7. Display the front panel and click the Browse button on
 the project file path control to select a project
 file.
8. Select File»Save As and save this VI in an easily accessible location.
9. Click the Run button to run the VI. 
 Note When you
 execute tests from a project programmatically, LabVIEW executes tests in the
 order as they are listed in the project.

Parent topic:

Execute Tests Programmatically

<!--NI_TOPIC bundle=labview-unit-test-framework-toolkit path=execute-tests-in-a-project.html language=enus -->
## TOPIC 00035: Executing Tests in a Project

- bundle_id: `labview-unit-test-framework-toolkit`
- source_path: `execute-tests-in-a-project.html`
- source_url: https://docs-be.ni.com/bundle/labview-unit-test-framework-toolkit/raw/resource/enus/execute-tests-in-a-project.html
- document_id: `labview-unit-test-framework-toolkit`
- page_type: `leaf`
- content_type: `task`
- source_description: Complete the following steps to execute tests in a LabVIEW project. Open the LabVIEW project that contains the files on which you want to perform unit testing. Right-click an .lvtest file and select Run from the shortcut menu. You also can execute multiple tests by pressing the <Ctrl> key while clic

### Executing Tests in a Project

Complete the following steps to execute tests in a LabVIEW
 project.

1. Open the LabVIEW project that contains the files on which you want to perform
 unit testing.
2. Right-click an .lvtest file and select
 Run from the shortcut menu. 
 Note You also can
 execute multiple tests by pressing the <Ctrl> key while clicking each
 .lvtest file. Then right-click the selection and
 select Run Unit Tests from the shortcut menu.
3. Click the OK button to close the dialog box and return
 to the Project Explorer window.

Parent topic:

Execute Tests Interactively

Related concepts:

- Using the Project Explorer Window

<!--NI_TOPIC bundle=labview-unit-test-framework-toolkit path=executing-only-modified-tests.html language=enus -->
## TOPIC 00036: Executing Only Modified Tests

- bundle_id: `labview-unit-test-framework-toolkit`
- source_path: `executing-only-modified-tests.html`
- source_url: https://docs-be.ni.com/bundle/labview-unit-test-framework-toolkit/raw/resource/enus/executing-only-modified-tests.html
- document_id: `labview-unit-test-framework-toolkit`
- page_type: `leaf`
- content_type: `task`
- source_description: Complete the following steps to execute only tests that have been modified since a specified time.Open the LabVIEW project that contains the files on which you want to perform unit testing. Click the Project Properties button on the Project toolbar to display the Project Properties dialog box. On th

### Executing Only Modified Tests

Complete the following steps to execute only tests that
 have been modified since a specified time.

1. Open the LabVIEW project that contains the files on which you want to perform
 unit testing.
2. Click the Project Properties button [IMAGE alt='image' src='GUID-B39EC891-2819-46B4-84C1-E65F2860E420-a5.gif'] on the
 Project toolbar to display the Project
 Properties dialog box.
3. On the Unit Test Framework page, place a checkmark in
 the Modified tests and VIs checkbox. The Modified Since options become
 available.
4. Select the filter option you want to apply. Note If you select the
 Last test execution option, you first must
 generate a test status log file before you can execute tests that have been
 modified since the last execution.
5. Optional: Place a checkmark in the Include tests of all caller VIs
 if you want to execute tests of all the VIs that call the modified VI under
 test.
6. Click the OK button to close the dialog box and return
 to the Project Explorer window.
7. Optional: 
 Select File»Save if you want LabVIEW to save the filter
 setting in the project file (.lvproj).

Unit Test Framework

Run Tests from Project

Parent topic:

Execute Tests Interactively

Related tasks:

- Executing Tests from a Project
- Generating Log Files

<!--NI_TOPIC bundle=labview-unit-test-framework-toolkit path=executing-tests-by-priority.html language=enus -->
## TOPIC 00037: Executing Tests by Priority

- bundle_id: `labview-unit-test-framework-toolkit`
- source_path: `executing-tests-by-priority.html`
- source_url: https://docs-be.ni.com/bundle/labview-unit-test-framework-toolkit/raw/resource/enus/executing-tests-by-priority.html
- document_id: `labview-unit-test-framework-toolkit`
- page_type: `leaf`
- content_type: `task`
- source_description: Complete the following steps to execute tests by priority.Open the LabVIEW project that contains the files on which you want to perform unit testing. Click the Project Properties button on the Project toolbar. The Project Properties dialog box appears. On the Unit Test Framework page, place a checkm

### Executing Tests by Priority

Complete the following steps to execute tests by
 priority.

1. Open the LabVIEW project that contains the files on which you want to perform unit testing.
2. Click the Project Properties button [IMAGE alt='image' src='GUID-B39EC891-2819-46B4-84C1-E65F2860E420-a5.gif'] on the
 Project toolbar. 
 The Project Properties dialog box
 appears.
3. On the Unit Test Framework page, place a checkmark in
 the Minimum priority checkbox.
4. Use the Minimum priority control to select a minimum
 priority.
5. Click the OK button to close the dialog box and return
 to the Project Explorer window.
6. Optional: 
 Select File»Save if you want LabVIEW to save the filter setting in the project
 file (.lvproj).

Minimum priority

You also can execute tests by priority programmatically by using the Run Tests from
 Project VI. You first must save the Minimum
 priority setting in the project that you want to execute tests by
 priority.

Parent topic:

Execute Tests Interactively

Related concepts:

- Test Priority

Related tasks:

- Executing Tests from a Project

<!--NI_TOPIC bundle=labview-unit-test-framework-toolkit path=executing-tests-interactively.html language=enus -->
## TOPIC 00038: Execute Tests Interactively

- bundle_id: `labview-unit-test-framework-toolkit`
- source_path: `executing-tests-interactively.html`
- source_url: https://docs-be.ni.com/bundle/labview-unit-test-framework-toolkit/raw/resource/enus/executing-tests-interactively.html
- document_id: `labview-unit-test-framework-toolkit`
- page_type: `leaf`
- content_type: `concept`
- source_description: Use the Project Explorer window to execute tests interactively. LabVIEW executes tests in the order as they are listed in the project. The Unit Test Framework Results window appears after test execution is complete.Before you execute tests, check the Unit Test Framework page of the Project Propertie

### Execute Tests Interactively

Project Explorer

Unit Test
 Framework Results

Note

Unit Test Framework

Project
 Properties

Tip

.lvproj

- [Executing Tests in a Project](execute-tests-in-a-project.html)
- [Executing All Tests in a Project](execute-all-tests-in-a-project.html)
- [Executing All Tests Associated with a VI](execute-all-tests-associated-with-a-vi.html)
- [Executing All Tests Associated with a LabVIEW Class](execute-all-tests-associated-with-a-lv-class.html)
- [Executing All Tests in a Folder or Project Library](execute-all-tests-in-folder-or-project-library.html)
- [Executing Only Modified Tests](executing-only-modified-tests.html)
- [Executing Tests by Priority](executing-tests-by-priority.html)

Parent topic:

Execute Tests

Related tasks:

- Storing VI Passwords for Unit Testing

<!--NI_TOPIC bundle=labview-unit-test-framework-toolkit path=executing-tests-programmatically.html language=enus -->
## TOPIC 00039: Execute Tests Programmatically

- bundle_id: `labview-unit-test-framework-toolkit`
- source_path: `executing-tests-programmatically.html`
- source_url: https://docs-be.ni.com/bundle/labview-unit-test-framework-toolkit/raw/resource/enus/executing-tests-programmatically.html
- document_id: `labview-unit-test-framework-toolkit`
- page_type: `leaf`
- content_type: `concept`
- source_description: Use the Unit Test Framework VIs to execute tests programmatically.

### Execute Tests Programmatically

Use the Unit Test Framework VIs to execute tests programmatically.

- [Executing Tests from .lvtest Files](execute-tests-from-lvtests-files.html)
- [Executing Tests from a Project](execute-tests-from-project.html)
- [Generating a Test Report](generate-test-report-programmatically.html)

Parent topic:

Execute Tests

<!--NI_TOPIC bundle=labview-unit-test-framework-toolkit path=executing-tests.html language=enus -->
## TOPIC 00040: Execute Tests

- bundle_id: `labview-unit-test-framework-toolkit`
- source_path: `executing-tests.html`
- source_url: https://docs-be.ni.com/bundle/labview-unit-test-framework-toolkit/raw/resource/enus/executing-tests.html
- document_id: `labview-unit-test-framework-toolkit`
- page_type: `leaf`
- content_type: `concept`
- source_description: The LabVIEW Unit Test Framework Toolkit provides several methods you can use to execute tests in a LabVIEW project. Use the Project Explorer window to execute tests interactively. You also can execute tests programmatically by using the Unit Test Framework VIs.Use this section to learn step-by-step

### Execute Tests

The LabVIEW Unit Test Framework Toolkit provides several methods you can use to execute
 tests in a LabVIEW project. Use the Project Explorer window to
 execute tests interactively. You also can execute tests programmatically by using the
 Unit Test Framework VIs.

Use this section to learn step-by-step instructions for executing tests in a LabVIEW project.

- [Execute Tests Interactively](executing-tests-interactively.html)
- [Execute Tests Programmatically](executing-tests-programmatically.html)

Parent topic:

Unit Test Framework Toolkit

<!--NI_TOPIC bundle=labview-unit-test-framework-toolkit path=exporting-and-importing-test-vectors.html language=enus -->
## TOPIC 00041: Exporting and Importing Test Vectors

- bundle_id: `labview-unit-test-framework-toolkit`
- source_path: `exporting-and-importing-test-vectors.html`
- source_url: https://docs-be.ni.com/bundle/labview-unit-test-framework-toolkit/raw/resource/enus/exporting-and-importing-test-vectors.html
- document_id: `labview-unit-test-framework-toolkit`
- page_type: `leaf`
- content_type: `task`
- source_description: You can modify values of a test vector by using a VI's array control. Complete the following steps to modify the values of a test vector using an array control: Export values from a test vector to a VI. Edit the values by using the front panel of the VI. Import modified values to the test vector. To

### Exporting and Importing Test Vectors

You can modify values of a test vector by using a VI's array control. Complete the following
 steps to modify the values of a test vector using
 an array control:

1. Export values from a test vector to a VI.
2. Edit the values by using the front panel of the VI.
3. Import modified values to the test vector.

To export or import the values of a test vector, you must have a VI that contains an
 array control with a proper data type.

If you export or import non-numeric values, the data type of the test vector and array control
 must be the same. For example, if you export
 values from a Boolean test vector to an array
 control, the data type of the control must be
 array of Booleans.

If you export numeric values of a test vector to an array control, the data type of the array
 control must have the same or larger scale than
 the test vector data type. For example, if you
 export values of an I8 test vector, the data type
 of the array control can be I8, I16, single
 floating-point, or other numeric data types that
 have larger scales.

If you import numeric values from an array control to a test vector, the data type of
 the test vector must have the same or larger scale than the array control data type.
 For example, if you import values from a single floating-point array control, the
 data type of the test vector can be single floating-point, double floating-point, or
 other numeric data types that have larger scales.

- [Exporting Values from a Test Vector to an Array Control](exporting-values-from-test-vector-to-array-control.html)
- [Importing Values from an Array Control to a Test Vector](importing-values-from-array-control-to-test-vector.html)

Parent topic:

Create Test Vector Files and Test Vectors

<!--NI_TOPIC bundle=labview-unit-test-framework-toolkit path=exporting-values-from-test-vector-to-array-control.html language=enus -->
## TOPIC 00042: Exporting Values from a Test Vector to an Array Control

- bundle_id: `labview-unit-test-framework-toolkit`
- source_path: `exporting-values-from-test-vector-to-array-control.html`
- source_url: https://docs-be.ni.com/bundle/labview-unit-test-framework-toolkit/raw/resource/enus/exporting-values-from-test-vector-to-array-control.html
- document_id: `labview-unit-test-framework-toolkit`
- page_type: `leaf`
- content_type: `task`
- source_description: Complete the following steps to modify the values of a test vector by using an array control. Open the VI that contains the target array control. Click the Export button in the Test Vector Properties - Edit dialog box. The Test Vector Properties - Export dialog box appears. Select the source test ve

### Exporting Values from a Test Vector to an
 Array Control

Complete the following steps to modify the values of a
 test vector by using an array control.

1. Open the VI that contains the target array control.
2. Click the Export button in the Test Vector
 Properties - Edit dialog box. 
 The Test Vector Properties - Export dialog box
 appears.
3. Select the source test vector from the Test Vectors
 list.
4. Select the VI that you opened in step 1 from the Target
 VIs list. 
 Note The
 Target VIs list does not display the VI if you do
 not open this VI in LabVIEW.
5. Select the target array control from the Target Controls
 list. 
 LabVIEW displays the array controls that have proper data types
 only.
6. Click the OK button to close this dialog box and export
 the values to the target array control. 
 LabVIEW displays the front panel of this VI after you click the
 OK button.

Parent topic:

Exporting and Importing Test Vectors

<!--NI_TOPIC bundle=labview-unit-test-framework-toolkit path=finding-tests-and-vis.html language=enus -->
## TOPIC 00043: Finding Tests and VIs

- bundle_id: `labview-unit-test-framework-toolkit`
- source_path: `finding-tests-and-vis.html`
- source_url: https://docs-be.ni.com/bundle/labview-unit-test-framework-toolkit/raw/resource/enus/finding-tests-and-vis.html
- document_id: `labview-unit-test-framework-toolkit`
- page_type: `leaf`
- content_type: `topic`
- source_description: Use the Project Explorer window to find tests and VIs in a LabVIEW project. You also can find an .lvtest file on disk. Finding All Tests Associated with a VIOpen the LabVIEW project that contains the files on which you want to perform unit testing.Right-click a VI and select Unit Tests»Find from the

### Finding Tests and VIs

Use the Project Explorer window to find tests and VIs in a
 LabVIEW project. You also can find an .lvtest file on disk.

#### Finding All Tests Associated with a VI

1. Open the LabVIEW project that contains the files on which you want to
 perform unit testing.
2. Right-click a VI and select Unit Tests»Find from the shortcut menu. LabVIEW highlights all the tests that
 are associated with this VI. Note To find tests for
 multiple VIs, select multiple VIs by pressing the <Ctrl> key while
 clicking each VI. Then right-click the selection and select
 Find Unit Tests from the shortcut
 menu.

#### Finding the VI Associated with a Test

1. Open the LabVIEW project that contains the files on which you want to
 perform unit testing.
2. Right-click the .lvtest file for which you want to find the VI under test
 and select Find VI . LabVIEW highlights the VI under
 test that is associated with this test.

#### Finding an .lvtest File on
 Disk

1. Open the LabVIEW project that contains the files on which you want to
 perform unit testing.
2. Right-click an .lvtest file and select Explore from
 the shortcut menu.

Parent topic:

Manage Tests

<!--NI_TOPIC bundle=labview-unit-test-framework-toolkit path=generate-test-report-programmatically.html language=enus -->
## TOPIC 00044: Generating a Test Report

- bundle_id: `labview-unit-test-framework-toolkit`
- source_path: `generate-test-report-programmatically.html`
- source_url: https://docs-be.ni.com/bundle/labview-unit-test-framework-toolkit/raw/resource/enus/generate-test-report-programmatically.html
- document_id: `labview-unit-test-framework-toolkit`
- page_type: `leaf`
- content_type: `task`
- source_description: Complete the following steps to generate a test report when you execute tests programmatically. Open a VI that executes tests programmatically. Add the Create Report VI to the block diagram. Wire the test results out output of the Open Results Window VI to the test results in input of the Create Rep

### Generating a Test Report

Complete the following steps to generate a test report
 when you execute tests programmatically.

1. Open a VI that executes tests programmatically.
2. Add the Create Report VI to the block diagram.
3. Wire the test results out output of the Open
 Results Window VI to the test results in
 input of the Create Report VI. 
 Note You also can
 wire the test results out output of the Open
 Results Window VI to the test results
 in input of the Run Tests from Project VI
 or the Run Tests from Files VI.
4. Right-click the report type input of the Create
 Report VI and select Create»Control from the shortcut menu. 
 A front panel control appears to the left of this VI. This control
 represents the type of report that this VI generates after test
 execution.
5. Click the report type control and select the type of
 report this VI generates. 
 The default report type is HTML.
6. Right-click the report path input of the Create
 Report VI and select Create»Control from the shortcut menu. 
 A front panel control appears to the left of this VI. This control
 represents the path to which this VI generates the test report.
7. Click the report path control and select the path to
 which this VI generates the test report. 
 Note If you do not
 select a path for the report, LabVIEW generates the report in the
 My Documents\LabVIEW Data directory.
8. Wire all error in and error out terminals on the block diagram. The block
 diagram now resembles the following figure: 
 [IMAGE alt='image' src='GUID-B7816D0B-4A44-46D1-9418-C10E426770E9-a5.gif']
 Note You can
 customize the test report by wiring values to the remaining inputs of the
 Create Report VI.
9. Select File»Save As and save this VI in an easily accessible location.
10. Click the Run button to run the VI.

Parent topic:

Execute Tests Programmatically

Related concepts:

- Test Results

<!--NI_TOPIC bundle=labview-unit-test-framework-toolkit path=generating-log-files.html language=enus -->
## TOPIC 00045: Generating Log Files

- bundle_id: `labview-unit-test-framework-toolkit`
- source_path: `generating-log-files.html`
- source_url: https://docs-be.ni.com/bundle/labview-unit-test-framework-toolkit/raw/resource/enus/generating-log-files.html
- document_id: `labview-unit-test-framework-toolkit`
- page_type: `leaf`
- content_type: `task`
- source_description: Complete the following steps to generate log files during and after execution.Open the LabVIEW project that contains the files on which you want to perform unit testing. Click the Project Properties button on the Project toolbar. The Project Properties dialog box appears. Select Unit Test Framework

### Generating Log Files

Complete the following steps to generate log files during
 and after execution.

1. Open the LabVIEW project that contains the files on which you want to perform unit testing.
2. Click the Project Properties button [IMAGE alt='image' src='GUID-B39EC891-2819-46B4-84C1-E65F2860E420-a5.gif'] on
 the Project toolbar. 
 The Project Properties dialog box
 appears.
3. Select Unit Test Framework from the
 Category list to display the Unit Test
 Framework page .
4. In the Generate Log Files section, place a checkmark in the checkbox of each log file you want to generate.
5. Click the Browse button to select a file path for each
 log file you want to generate. Note If you do not
 select a path for the log file(s), LabVIEW generates the log file(s) in the
 same directory as the project.
6. Optional: If you generate a test execution log file, place a checkmark in the
 Overwrite log file checkbox if you want to replace
 the existing log file with the details from each subsequent test
 execution. Note LabVIEW appends
 the details of each subsequent test execution to the existing log file
 unless you place a checkmark in the Overwrite log
 file or change the log file name.
7. Click the OK button to close the dialog box and return
 to the Project Explorer window.
8. Optional: 
 Select File»Save if you want LabVIEW to save the report settings in the project
 file (.lvproj).

The next time you execute tests interactively, LabVIEW generates the log file(s) you
 specified on the Unit Test Framework page.

Parent topic:

View Test Results and Generating Reports

Related concepts:

- Execute Tests Interactively
- Test Results

<!--NI_TOPIC bundle=labview-unit-test-framework-toolkit path=generating-test-reports.html language=enus -->
## TOPIC 00046: Generating Test Reports

- bundle_id: `labview-unit-test-framework-toolkit`
- source_path: `generating-test-reports.html`
- source_url: https://docs-be.ni.com/bundle/labview-unit-test-framework-toolkit/raw/resource/enus/generating-test-reports.html
- document_id: `labview-unit-test-framework-toolkit`
- page_type: `leaf`
- content_type: `task`
- source_description: You can generate test reports in HTML, Automatic Test Markup Language (ATML), or ASCII format. Complete the following steps to generate test reports: Open the LabVIEW project that contains the files on which you want to perform unit testing. Click the Project Properties button on the Project toolbar

### Generating Test Reports

You can generate test reports in HTML,
 Automatic Test Markup Language (ATML), or ASCII format. Complete the following steps to
 generate test reports:

1. Open the LabVIEW project that contains the files on which you want to perform
 unit testing.
2. Click the Project Properties button [IMAGE alt='image' src='GUID-B39EC891-2819-46B4-84C1-E65F2860E420-a5.gif'] on
 the Project toolbar. 
 The Project Properties dialog box
 appears.
3. Select Unit Test Framework from the
 Category list to display the Unit Test
 Framework page.
4. In the Generate Reports section, place a checkmark in the checkbox of each report you want to generate.
5. Click the Browse button to select a file path for each
 report you want to generate. 
 Note If you do not
 select a path for the report(s), LabVIEW generates the report(s) in the same
 directory as the project.
6. Optional: 
 Place a checkmark in a View report after execution
 checkbox to display the test report after test execution.
7. Click the OK button to close the dialog box and return
 to the Project Explorer window.
8. Optional: 
 Select File»Save if you want LabVIEW to save the report settings in the project
 file (.lvproj).

The next time you execute tests interactively LabVIEW generates the test report(s)
 you specified on the Unit Test Framework page. If a test
 report already exists from a previous test execution, LabVIEW replaces the existing
 test report.

Parent topic:

View Test Results and Generating Reports

Related concepts:

- Execute Tests Interactively

<!--NI_TOPIC bundle=labview-unit-test-framework-toolkit path=importing-values-from-array-control-to-test-vector.html language=enus -->
## TOPIC 00047: Importing Values from an Array Control to a Test Vector

- bundle_id: `labview-unit-test-framework-toolkit`
- source_path: `importing-values-from-array-control-to-test-vector.html`
- source_url: https://docs-be.ni.com/bundle/labview-unit-test-framework-toolkit/raw/resource/enus/importing-values-from-array-control-to-test-vector.html
- document_id: `labview-unit-test-framework-toolkit`
- page_type: `leaf`
- content_type: `task`
- source_description: Complete the following steps to import values from an array control to a test vector. Open the VI that contains the source array control. Click the Import button in the Test Vector Properties - Edit dialog box. The Test Vector Properties - Import dialog box appears. Select the VI that you opened in

### Importing Values from an Array Control to a
 Test Vector

Complete the following steps to import values from an
 array control to a test vector.

1. Open the VI that contains the source array control.
2. Click the Import button in the Test Vector
 Properties - Edit dialog box. 
 The Test Vector Properties - Import dialog box
 appears.
3. Select the VI that you opened in step 1 from the Source
 VIs list. 
 Note The
 Source VI list does not display the VI if you do
 not open this VI in LabVIEW.
4. Select the target test vector from the Target Test
 Vectors list.
5. Select the source array control from the Source Controls
 list. 
 LabVIEW displays the array controls that have proper data types
 only.
6. Click the OK button to close this dialog box and import
 the values to the target test vector.

Parent topic:

Exporting and Importing Test Vectors

<!--NI_TOPIC bundle=labview-unit-test-framework-toolkit path=introduction-to-the-labview-unit-test-framewo.html language=enus -->
## TOPIC 00048: Introduction to the LabVIEW Unit Test Framework Toolkit

- bundle_id: `labview-unit-test-framework-toolkit`
- source_path: `introduction-to-the-labview-unit-test-framewo.html`
- source_url: https://docs-be.ni.com/bundle/labview-unit-test-framework-toolkit/raw/resource/enus/introduction-to-the-labview-unit-test-framewo.html
- document_id: `labview-unit-test-framework-toolkit`
- page_type: `leaf`
- content_type: `concept`
- source_description: The LabVIEW Unit Test Framework Toolkit provides tools you use to check VIs for functional correctness. When you create a test from the Project Explorer window, LabVIEW creates an .lvtest file on disk. Each .lvtest file contains the settings LabVIEW uses to check the VI under test for functional cor

### Introduction to the LabVIEW Unit Test
 Framework Toolkit

The LabVIEW Unit Test Framework Toolkit provides tools you use to check VIs for
 functional correctness.

Project Explorer

.lvtest

.lvtest

.lvtest

Note

Using the Unit Test Framework Toolkit involves the following steps:

1. Creating projects and tests: You must create and save a LabVIEW project before you can create
 tests. Use projects to group together all the files you need to perform unit
 testing. Use the Project Explorer window to create
 tests.
2. Configuring tests: Use the Project Explorer window to configure tests
 interactively. You also can configure tests by editing .lvtest 
 files. Each .lvtest file contains the settings you specify for
 a test.
3. Managing tests: Use virtual folders, auto-populating folders, and LabVIEW project libraries to
 organize a project. You can drag and drop files inside the Project
 Explorer window to manage a project. Use the Project
 Explorer window to find tests and VIs.
4. Executing tests: Use the Project Explorer window to execute tests
 interactively. You also can execute tests programmatically by using the
 Unit Test Framework VIs.
5. Viewing test results and generating reports: Use the Unit Test Framework
 Results window to view test results. The Project
 Explorer window also displays results from the test execution.
 You can generate test reports in different formats. Test reports contain results
 from the execution. You can customize test reports by specifying the contents of
 the reports. You also can format HTML reports by using a Cascading Style Sheet
 (CSS) file. In addition, you can generate log files during test execution.

- [Using the Project Explorer Window](using-the-project-explorer-window.html)
- [Tests and .lvtest Files](tests-and-lvtest-files.html)
- [Test Cases](test-cases.html)
- [Test Vectors and .lvvect Files](test-vectors-and-lvvect-files.html)
- [Test Priority](test-priority.html)
- [Requirement IDs](requirement-ids.html)
- [Code Coverage](code-coverage.html)
- [Setup and Teardown VIs](setup-and-teardown-vis.html)
- [Comparison Types](comparison-types.html)
- [Test Results](test-results.html)

Parent topic:

Unit Test Framework Toolkit

Related concepts:

- Configure Tests
- Create Tests
- Execute Tests
- Manage Tests
- View Test Results and Generating Reports

<!--NI_TOPIC bundle=labview-unit-test-framework-toolkit path=items-and-files-pages.html language=enus -->
## TOPIC 00049: Items and Files Pages

- bundle_id: `labview-unit-test-framework-toolkit`
- source_path: `items-and-files-pages.html`
- source_url: https://docs-be.ni.com/bundle/labview-unit-test-framework-toolkit/raw/resource/enus/items-and-files-pages.html
- document_id: `labview-unit-test-framework-toolkit`
- page_type: `leaf`
- content_type: `concept`
- source_description: he Items page displays all the .lvtest files, VIs, folders, and libraries that exist in the project tree. The Files page displays the project items that have a corresponding file on disk. The Project Explorer window includes the Items and Files pages. When you create a test from the Project Explorer

### Items and Files Pages

he Items page displays all the .lvtest files,
 VIs, folders, and libraries that exist in the project tree. The
 Files page displays the project items that have a
 corresponding file on disk.

The Project Explorer window includes the
 Items and Files pages. When you create
 a test from the Project Explorer window, LabVIEW creates an
 .lvtest file on disk. An .lvtest file icon
 appears on both the Items and Files
 pages.

[IMAGE alt='image' src='GUID-38741938-C11A-4C98-9D67-6310F0F962EA-a5.png']

Parent topic:

Using the Project Explorer Window

Related concepts:

- Tests and .lvtest Files

<!--NI_TOPIC bundle=labview-unit-test-framework-toolkit path=log-files.html language=enus -->
## TOPIC 00050: Log Files

- bundle_id: `labview-unit-test-framework-toolkit`
- source_path: `log-files.html`
- source_url: https://docs-be.ni.com/bundle/labview-unit-test-framework-toolkit/raw/resource/enus/log-files.html
- document_id: `labview-unit-test-framework-toolkit`
- page_type: `leaf`
- content_type: `concept`
- source_description: You can configure the Unit Test Framework Toolkit to generate log files during test execution. Log files contain detailed information about the execution. You can generate the following log files: Test Status This log file is a .txt file that contains information about the most recent test execution

### Log Files

You can configure the Unit Test Framework Toolkit to generate log files during test
 execution. Log files contain detailed information about the execution.

You can generate the following log files:

Test Status

.txt

1

0

2

3

Note

Test Execution

.txt

Parent topic:

Test Results

Related tasks:

- Generating Log Files
- Executing Only Modified Tests

<!--NI_TOPIC bundle=labview-unit-test-framework-toolkit path=managing-tests.html language=enus -->
## TOPIC 00051: Manage Tests

- bundle_id: `labview-unit-test-framework-toolkit`
- source_path: `managing-tests.html`
- source_url: https://docs-be.ni.com/bundle/labview-unit-test-framework-toolkit/raw/resource/enus/managing-tests.html
- document_id: `labview-unit-test-framework-toolkit`
- page_type: `leaf`
- content_type: `concept`
- source_description: Use the Project Explorer window to manage tests in a project. You can use virtual folders, auto-populating folders, and LabVIEW project libraries to organize a project.Use this section to learn step-by-step instructions for managing tests in a LabVIEW project.

### Manage Tests

Use the Project Explorer window to manage tests in a project. You
 can use virtual folders, auto-populating folders, and LabVIEW project libraries to
 organize a project.

Use this section to learn step-by-step instructions for managing tests in a LabVIEW project.

- [Organize a Project](organizing-a-project.html)
- [Finding Tests and VIs](finding-tests-and-vis.html)
- [Renaming a Test](renaming-a-test.html)
- [Removing a Test from a LabVIEW Project](removing-a-test-from-a-labview-project.html)

Parent topic:

Unit Test Framework Toolkit

Related concepts:

- Organize a Project

<!--NI_TOPIC bundle=labview-unit-test-framework-toolkit path=new-features-and-changes.html language=enus -->
## TOPIC 00052: LabVIEW Unit Test Framework Toolkit New Features and Changes

- bundle_id: `labview-unit-test-framework-toolkit`
- source_path: `new-features-and-changes.html`
- source_url: https://docs-be.ni.com/bundle/labview-unit-test-framework-toolkit/raw/resource/enus/new-features-and-changes.html
- document_id: `labview-unit-test-framework-toolkit`
- page_type: `leaf`
- content_type: `concept`
- source_description: Learn about updates—including new features and behavior changes—introduced in each version of LabVIEW Unit Test Framework Toolkit. Discover what's new in the latest releases of LabVIEW Unit Test Framework Toolkit.If you cannot find new features and changes for your version, it might not include user

### LabVIEW Unit Test Framework Toolkit
 New Features and Changes

Learn about updates—including new features and behavior changes—introduced in each
 version of LabVIEW Unit Test Framework Toolkit.

LabVIEW Unit Test Framework Toolkit

Note

Release Notes

Related information:

- Software and Driver Downloads

#### LabVIEW Unit Test Framework Toolkit 2021
 Changes

Learn about new features, behavior changes, and other updates in LabVIEW Unit Test
 Framework Toolkit 2021.

- LabVIEW Unit Test Framework Toolkit no longer supports Windows 7/8.1, Windows Server
 2008/2012, or any 32-bit Windows operating system.
  - Versions of this product that ship after May 1, 2021 may not install or execute
 correctly on these operating systems. For information about operating systems that
 NI supports, visit NI Support for Windows 7, Windows 8.1, Windows Server 2008
 R2, Windows Server 2012 R2, and All 32-Bit Windows .

Related information:

- NI Support for Windows 7, Windows 8.1, Windows Server 2008 R2,
 Windows Server 2012 R2, and All 32-Bit Windows
- Release Notes

#### LabVIEW Unit Test Framework Toolkit 2020
 Changes

Learn about new features, behavior changes, and other updates in LabVIEW Unit Test
 Framework Toolkit 2020.

LabVIEW Unit Test Framework Toolkit 2020 includes only bug fixes. Refer to the Release
 Notes for a list of bug fixes.

Related information:

- Release Notes

#### LabVIEW Unit Test Framework Toolkit 2019
 Changes

Learn about new features, behavior changes, and other updates in LabVIEW Unit Test
 Framework Toolkit 2019.

LabVIEW Unit Test Framework Toolkit 2019 includes only bug fixes. Refer to the Release
 Notes for a list of bug fixes.

Related information:

- Release Notes

<!--NI_TOPIC bundle=labview-unit-test-framework-toolkit path=organizing-a-project.html language=enus -->
## TOPIC 00053: Organize a Project

- bundle_id: `labview-unit-test-framework-toolkit`
- source_path: `organizing-a-project.html`
- source_url: https://docs-be.ni.com/bundle/labview-unit-test-framework-toolkit/raw/resource/enus/organizing-a-project.html
- document_id: `labview-unit-test-framework-toolkit`
- page_type: `leaf`
- content_type: `concept`
- source_description: You must create and save a LabVIEW project before you can use the LabVIEW Unit Test Framework Toolkit to create tests.Use projects to group together all the files you need to perform unit testing. Use virtual folders, auto-populating folders, and LabVIEW project libraries to organize a project.

### Organize a Project

You must create and save a LabVIEW project before you can use the LabVIEW Unit Test
 Framework Toolkit to create tests.

Use projects to group together all the files you need to perform unit testing. Use virtual
 folders, auto-populating folders, and LabVIEW project libraries to organize a project.

- [Adding Files to a Project](adding-files-to-a-project.html)
- [Using Folders to Organize a Project](using-folders-to-organize-a-project.html)

Parent topic:

Manage Tests

<!--NI_TOPIC bundle=labview-unit-test-framework-toolkit path=overview.html language=enus -->
## TOPIC 00054: LabVIEW Unit Test Framework Toolkit Overview

- bundle_id: `labview-unit-test-framework-toolkit`
- source_path: `overview.html`
- source_url: https://docs-be.ni.com/bundle/labview-unit-test-framework-toolkit/raw/resource/enus/overview.html
- document_id: `labview-unit-test-framework-toolkit`
- page_type: `leaf`
- content_type: `concept`
- source_description: The LabVIEW Unit Test Framework Toolkit is a software add-on for LabVIEW that helps you automate functional validation and demonstrate whether an application behaves properly. You can generate a unit test or import test parameters from a text document created in an editor such as Microsoft Excel. Te

### LabVIEW Unit Test Framework Toolkit
 Overview

The LabVIEW Unit Test Framework Toolkit is a software add-on for LabVIEW that helps you
 automate functional validation and demonstrate whether an application behaves properly.
 You can generate a unit test or import test parameters from a text document created in
 an editor such as Microsoft Excel. Tests can encompass multiple test cases, which define
 input values and the expected output for any data type, including arrays and clusters.
 You can identify the source of incorrect outputs, track code coverage, and generate
 validation documents in HTML, ATML/XML, or ASCII formats.

<!--NI_TOPIC bundle=labview-unit-test-framework-toolkit path=project-code-coverage.html language=enus -->
## TOPIC 00055: Project Code Coverage

- bundle_id: `labview-unit-test-framework-toolkit`
- source_path: `project-code-coverage.html`
- source_url: https://docs-be.ni.com/bundle/labview-unit-test-framework-toolkit/raw/resource/enus/project-code-coverage.html
- document_id: `labview-unit-test-framework-toolkit`
- page_type: `leaf`
- content_type: `concept`
- source_description: You can generate code coverage of a project by placing a checkmark in the Include VIs that were not tested checkbox on the Unit Test Framework page. When you execute this test, LabVIEW opens all VIs in this project to count subdiagrams and generates the code coverage of this project. For example, yo

### Project Code Coverage

You can generate code coverage of a project by placing a checkmark in the
 Include VIs that were not tested checkbox on the
 Unit Test Framework page.

When you execute this test, LabVIEW opens all VIs in this project to count subdiagrams
 and generates the code coverage of this project. For example, you can create a project
 that contains two VIs and each VI contains three subdiagrams and a test case that covers
 all three subdiagrams of one VI. When you execute this test, LabVIEW opens both VIs to
 count subdiagrams. Because this projects contains six subdiagrams and the test covers
 three subdiagrams, the project code coverage measurement is 50%.

Note

Parent topic:

Code Coverage

<!--NI_TOPIC bundle=labview-unit-test-framework-toolkit path=project-explorer-window-test-results.html language=enus -->
## TOPIC 00056: Test Reports

- bundle_id: `labview-unit-test-framework-toolkit`
- source_path: `project-explorer-window-test-results.html`
- source_url: https://docs-be.ni.com/bundle/labview-unit-test-framework-toolkit/raw/resource/enus/project-explorer-window-test-results.html
- document_id: `labview-unit-test-framework-toolkit`
- page_type: `leaf`
- content_type: `concept`
- source_description: You can configure the Unit Test Framework Toolkit to generate test reports after test execution is complete. Test reports contain results from the execution. You can customize test reports by specifying the contents of the reports. You can generate test reports in the following file formats: HTML HT

### Test Reports

You can configure the Unit Test Framework Toolkit to generate test reports after test
 execution is complete. Test reports contain results from the execution. You can
 customize test reports by specifying the contents of the reports.

You can generate test reports in the following file formats:

HTML

ATML

ASCII

Parent topic:

Test Results

Related information::

- Customizing Test Reports

<!--NI_TOPIC bundle=labview-unit-test-framework-toolkit path=quick-start-guide.html language=enus -->
## TOPIC 00057: Quick Start Guide

- bundle_id: `labview-unit-test-framework-toolkit`
- source_path: `quick-start-guide.html`
- source_url: https://docs-be.ni.com/bundle/labview-unit-test-framework-toolkit/raw/resource/enus/quick-start-guide.html
- document_id: `labview-unit-test-framework-toolkit`
- page_type: `leaf`
- content_type: `task`
- source_description: Complete the following steps to create, configure, and execute tests in the Project Explorer window.Launch LabVIEW. Select File»New to display the New dialog box and select Project»Empty Project to create a new project. Add VIs you want to test to a target, such as My Computer, and select File»Save

### Quick Start Guide

Project Explorer

1. Launch LabVIEW.
2. Select File»New to display the New dialog box and select Project»Empty Project to create a new project.
3. Add VIs you want to test to a target, such as My Computer, and select File»Save to save the project.
4. Right-click a VI and select Unit Tests»New Test from the shortcut menu to create a test. An
 .lvtest file with the same name as the VI appears in
 the project tree.
5. Right-click the .lvtest file and select
 Properties from the shortcut menu to display the
 Test Properties dialog box. Use this dialog box to
 configure tests.
6. Use the Unit Test Framework toolbar [IMAGE alt='image' src='GUID-8AC3C4A3-F84F-4123-A2A8-85E355251B69-a5.gif'] at the top of the Project
 Explorer window. Use the Project
 Properties dialog box to configure settings related to creating
 and executing tests.

Parent topic:

Unit Test Framework Toolkit

Related concepts:

- Configure Tests
- Create Tests
- Execute Tests
- Unit Test Framework Toolbar (Project Explorer Window)

<!--NI_TOPIC bundle=labview-unit-test-framework-toolkit path=removing-a-test-from-a-labview-project.html language=enus -->
## TOPIC 00058: Removing a Test from a LabVIEW Project

- bundle_id: `labview-unit-test-framework-toolkit`
- source_path: `removing-a-test-from-a-labview-project.html`
- source_url: https://docs-be.ni.com/bundle/labview-unit-test-framework-toolkit/raw/resource/enus/removing-a-test-from-a-labview-project.html
- document_id: `labview-unit-test-framework-toolkit`
- page_type: `leaf`
- content_type: `task`
- source_description: Complete the following steps to remove a test from a LabVIEW project.Removing a test from a project does not delete the .lvtest file on disk. Open the LabVIEW project that contains the files on which you want to perform unit testing. Right-click an .lvtest file and select Remove from Project from th

### Removing a Test from a LabVIEW Project

Note

.lvtest

1. Open the LabVIEW project that contains the files on which you
 want to perform unit testing.
2. Right-click an .lvtest file and select Remove from
 Project from the shortcut menu. 
 Note You also can remove
 multiple .lvtest files by pressing the <Ctrl> key while
 clicking each file. Then right-click the selection and select Remove from
 Project from the shortcut menu.
3. Select File»Save to save the project.

Parent topic:

Manage Tests

<!--NI_TOPIC bundle=labview-unit-test-framework-toolkit path=renaming-a-test.html language=enus -->
## TOPIC 00059: Renaming a Test

- bundle_id: `labview-unit-test-framework-toolkit`
- source_path: `renaming-a-test.html`
- source_url: https://docs-be.ni.com/bundle/labview-unit-test-framework-toolkit/raw/resource/enus/renaming-a-test.html
- document_id: `labview-unit-test-framework-toolkit`
- page_type: `leaf`
- content_type: `task`
- source_description: Complete the following steps to rename a test in a LabVIEW project.Open the LabVIEW project that contains the files on which you want to perform unit testing. Right-click an .lvtest file and select Rename from the shortcut menu. Do not rename .lvtest files in Windows Explorer if the .lvtest files al

### Renaming a Test

Complete the following steps to rename a test in a LabVIEW
 project.

1. Open the LabVIEW project that contains the files on which you want to perform unit testing.
2. Right-click an .lvtest file and select
 Rename from the shortcut menu. 
 Caution Do not
 rename .lvtest files in Windows Explorer if the
 .lvtest files already belong to a project. If you
 rename .lvtest files on disk, LabVIEW does not update
 the filenames in the project. You can no longer execute these tests from the
 Project Explorer window.
3. Enter the new name for this test and click the OK button.
4. Select File»Save to save the project.

Parent topic:

Manage Tests

<!--NI_TOPIC bundle=labview-unit-test-framework-toolkit path=requirement-ids.html language=enus -->
## TOPIC 00060: Requirement IDs

- bundle_id: `labview-unit-test-framework-toolkit`
- source_path: `requirement-ids.html`
- source_url: https://docs-be.ni.com/bundle/labview-unit-test-framework-toolkit/raw/resource/enus/requirement-ids.html
- document_id: `labview-unit-test-framework-toolkit`
- page_type: `leaf`
- content_type: `concept`
- source_description: Requirement IDs define the traceability relationships between requirements and code.You can integrate the LabVIEW Unit Test Framework Toolkit with Requirements Gateway. Requirements Gateway is an application that provides a requirements traceability solution. This application links development and v

### Requirement IDs

Requirement IDs define the traceability relationships between requirements and code.

You can integrate the LabVIEW Unit Test Framework Toolkit with Requirements Gateway. Requirements
 Gateway is an application that provides a requirements traceability solution. This
 application links development and verification documents with formal requirements stored
 in documents and databases.

When you configure tests and edit test vectors, you can specify requirement IDs for each test and
 test vector that you want to track with Requirements Gateway. LabVIEW includes the
 requirement IDs in ATML reports so that you can track tests and test results in
 Requirements Gateway. If LabVIEW executes a test and the test is passed, LabVIEW reports
 that the test covers the corresponding requirement. If LabVIEW uses a test vector in a
 test, LabVIEW reports that the test vector covers the corresponding requirement.

After you execute the tests, Requirements Gateway calculates a coverage ratio for all
 requirements by using the requirement IDs and other information in the test report.
 Refer to the *Requirements Gateway* documentation for the detailed
 calculating method.

You can specify requirement IDs interactively by using the Configuration
 page of the Test Properties dialog box. You also can specify
 requirement IDs by editing .lvtest files.

Parent topic:

Introduction to the LabVIEW Unit Test Framework Toolkit

Related concepts:

- Test Results

Related tasks:

- Specifying Requirement IDs

<!--NI_TOPIC bundle=labview-unit-test-framework-toolkit path=saving-and-loading-test-results.html language=enus -->
## TOPIC 00061: Saving and Loading Test Results

- bundle_id: `labview-unit-test-framework-toolkit`
- source_path: `saving-and-loading-test-results.html`
- source_url: https://docs-be.ni.com/bundle/labview-unit-test-framework-toolkit/raw/resource/enus/saving-and-loading-test-results.html
- document_id: `labview-unit-test-framework-toolkit`
- page_type: `leaf`
- content_type: `concept`
- source_description: You can save test results from the Unit Test Framework Results window to a .lvutf file that you can load later. Saving Test Results to a FileComplete the following steps to save test results from the Unit Test Framework Results window to a .lvutf file: After you execute tests, LabVIEW displays the U

### Saving and Loading Test Results

You can save test results from the Unit Test Framework Results
 window to a .lvutf file that you can load later.

#### Saving Test Results to a
 File

Unit Test Framework Results

.lvutf

1. After you execute tests, LabVIEW displays the Unit Test Framework
 Results window. Click the Save button
 to save test results to a .lvutf file. A file dialog
 box appears.
2. Navigate to the location where you want to save the
 .lvutf file.
3. Enter the filename you want for the .lvutf file and click the
 OK button.

#### Loading Test Results from a
 File

.lvutf

Unit Test Framework Results

1. Open the LabVIEW project that contains the files on which you want to
 perform unit testing.
2. Click the Unit Test Framework Results button on
 the Unit Test Framework toolbar to display the
 Unit Test Framework Results window.
3. Click the Load button. A file dialog box
 appears.
4. Navigate to and select the .lvutf file you want to
 load. Click the OK button. The Unit Test
 Framework Results window displays the results you saved
 previously.

Parent topic:

View Test Results and Generating Reports

Related concepts:

- Unit Test Framework Toolbar (Project Explorer Window)

<!--NI_TOPIC bundle=labview-unit-test-framework-toolkit path=setup-and-teardown-vis.html language=enus -->
## TOPIC 00062: Setup and Teardown VIs

- bundle_id: `labview-unit-test-framework-toolkit`
- source_path: `setup-and-teardown-vis.html`
- source_url: https://docs-be.ni.com/bundle/labview-unit-test-framework-toolkit/raw/resource/enus/setup-and-teardown-vis.html
- document_id: `labview-unit-test-framework-toolkit`
- page_type: `leaf`
- content_type: `concept`
- source_description: A setup VI is a VI that LabVIEW runs before checking the VI under test for functional correctness. A teardown VI is a VI that LabVIEW runs after checking the VI under test for functional correctness.During unit testing, you might want to perform tasks before and after checking a VI for functional co

### Setup and Teardown VIs

A setup VI is a VI that LabVIEW runs before checking the VI under test for functional
 correctness. A teardown VI is a VI that LabVIEW runs after checking the VI under test
 for functional correctness.

During unit testing, you might want to perform tasks before and after checking a VI for
 functional correctness. For example, you might want to power up an instrument, open a
 file, or pass values from another VI to the VI under test. After LabVIEW finishes
 checking the VI under test for functional correctness, you might want to pass values
 from the VI under test to another VI, close a file, or power down an instrument.

The LabVIEW Unit Test Framework Toolkit provides tools you use to configure a test to run setup
 and teardown VIs. You also can pass values among the setup VI, the VI under test, and
 the teardown VI.

You can configure tests to run setup and teardown VIs by using the
 Setup/Teardown page of the Test
 Properties dialog box. You also can specify setup and teardown VIs by
 editing .lvtest files. Use the Test Cases
 page to specify the input values, expected values, and comparison types of the setup and
 teardown VIs for each test case.

When you execute a test, LabVIEW first runs the setup VI and then passes the output values from
 the setup VI to the inputs of the VI under test. LabVIEW then checks the VI under test
 for functional correctness and passes the resulting values from the VI under test to the
 inputs of the teardown VI.

The following figure shows an example of configuring the setup and teardown VIs for a test:

[IMAGE alt='image' src='GUID-A45DF337-7B47-4563-BD1D-F3A43D8BB986-a5.png']

refnum out

error out

refnum

error
 in

text

Test Cases

refnum out

error out

Note

error out

Test Errors

Unit Test Framework Results

Test Results

Parent topic:

Introduction to the LabVIEW Unit Test Framework Toolkit

Related tasks:

- Configuring Tests to Run Setup and Teardown VIs

<!--NI_TOPIC bundle=labview-unit-test-framework-toolkit path=specifying-a-minimum-code-coverage-requiremen.html language=enus -->
## TOPIC 00063: Specifying a Minimum Code Coverage Requirement

- bundle_id: `labview-unit-test-framework-toolkit`
- source_path: `specifying-a-minimum-code-coverage-requiremen.html`
- source_url: https://docs-be.ni.com/bundle/labview-unit-test-framework-toolkit/raw/resource/enus/specifying-a-minimum-code-coverage-requiremen.html
- document_id: `labview-unit-test-framework-toolkit`
- page_type: `leaf`
- content_type: `task`
- source_description: Complete the following steps to specify a minimum code coverage requirement.Open the LabVIEW project that contains the files on which you want to perform unit testing. Double-click a .lvtest file to display the Test Properties dialog box. Select Advanced from the Category list to display the Advance

### Specifying a Minimum Code Coverage Requirement

Complete the following steps to specify a minimum code
 coverage requirement.

1. Open the LabVIEW project that contains the files on which you want to perform
 unit testing.
2. Double-click a .lvtest file to display the Test
 Properties dialog box.
3. Select Advanced from the Category
 list to display the Advanced page.
4. Place a checkmark in the Set minimum code coverage checkbox.
5. Use the Code coverage control to specify a minimum code
 coverage requirement, in percent. Note Use minimum code coverage
 requirement for VIs that contain Case
 structures.
6. Click the OK button to close the dialog box and return
 to the Project Explorer window.
7. Select File»Save to save the project.

The next time you execute this test, LabVIEW runs the VI under test and measures the
 percentage of subdiagrams executed. If the VI under test does not meet the minimum code
 coverage requirement you specified, test results show this test as failed.

Parent topic:

Configure Advanced Settings of Tests

Related concepts:

- Code Coverage

<!--NI_TOPIC bundle=labview-unit-test-framework-toolkit path=specifying-a-test-priority.html language=enus -->
## TOPIC 00064: Specifying a Test Priority

- bundle_id: `labview-unit-test-framework-toolkit`
- source_path: `specifying-a-test-priority.html`
- source_url: https://docs-be.ni.com/bundle/labview-unit-test-framework-toolkit/raw/resource/enus/specifying-a-test-priority.html
- document_id: `labview-unit-test-framework-toolkit`
- page_type: `leaf`
- content_type: `task`
- source_description: Complete the following steps to specify a test priority for a test.Open the LabVIEW project that contains the files on which you want to perform unit testing. Double-click a .lvtest file or right-click the .lvtest file and select Properties from the shortcut menu to display the Test Properties dialo

### Specifying a Test Priority

Complete the following steps to specify a test priority
 for a test.

1. Open the LabVIEW project that contains the files on which you want to perform
 unit testing.
2. Double-click a .lvtest file or right-click the
 .lvtest file and select
 Properties from the shortcut menu to display the
 Test Properties dialog box.
3. On the Configuration page, use the Test
 Priority control to select a priority for this test.
4. Click the OK button to close the dialog box and return
 to the Project Explorer window.
5. Select File»Save to save the project.

The next time you execute tests by priority, LabVIEW executes only tests with an equal or higher
 priority than the Minimum priority you specified on the
 Unit Test Framework page of the Project
 Properties dialog box.

Parent topic:

Configure Tests

Related concepts:

- Test Priority

Related tasks:

- Executing Tests by Priority

<!--NI_TOPIC bundle=labview-unit-test-framework-toolkit path=specifying-a-timeout-for-a-test.html language=enus -->
## TOPIC 00065: Specifying a Timeout for a Test

- bundle_id: `labview-unit-test-framework-toolkit`
- source_path: `specifying-a-timeout-for-a-test.html`
- source_url: https://docs-be.ni.com/bundle/labview-unit-test-framework-toolkit/raw/resource/enus/specifying-a-timeout-for-a-test.html
- document_id: `labview-unit-test-framework-toolkit`
- page_type: `leaf`
- content_type: `task`
- source_description: Complete the following steps to specify a timeout for a test.Open the LabVIEW project that contains the files on which you want to perform unit testing. Double-click a .lvtest file to display the Test Properties dialog box. Select Advanced from the Category list to display the Advanced page.Place a

### Specifying a Timeout for a Test

Complete the following steps to specify a timeout for a
 test.

1. Open the LabVIEW project that contains the files on which you want to perform unit testing.
2. Double-click a .lvtest file to display the Test
 Properties dialog box.
3. Select Advanced from the Category
 list to display the Advanced page.
4. Place a checkmark in the Set timeout checkbox.
5. Use the Timeout control to specify a timeout, in
 seconds. Note Use timeout for
 tests of VIs that loop forever or require you to perform any tasks
 manually.
6. Click the OK button to close the dialog box and return
 to the Project Explorer window.
7. Select File»Save to save the project.

The next time you execute this test, LabVIEW runs the VI under test. If the VI under
 test times out during execution, LabVIEW stops the VI and test results show this
 test as failed.

Parent topic:

Configure Advanced Settings of Tests

<!--NI_TOPIC bundle=labview-unit-test-framework-toolkit path=specifying-requirement-ids.html language=enus -->
## TOPIC 00066: Specifying Requirement IDs

- bundle_id: `labview-unit-test-framework-toolkit`
- source_path: `specifying-requirement-ids.html`
- source_url: https://docs-be.ni.com/bundle/labview-unit-test-framework-toolkit/raw/resource/enus/specifying-requirement-ids.html
- document_id: `labview-unit-test-framework-toolkit`
- page_type: `leaf`
- content_type: `task`
- source_description: Complete the following steps to specify requirement IDs for a test.Open the LabVIEW project that contains the files on which you want to perform unit testing. Double-click a .lvtest file to display the Test Properties dialog box. On the Configuration page, enter requirement IDs in the Requirement ID

### Specifying Requirement IDs

Complete the following steps to specify requirement IDs
 for a test.

1. Open the LabVIEW project that contains the files on which you want to perform
 unit testing.
2. Double-click a .lvtest file to display the Test
 Properties dialog box.
3. On the Configuration page, enter requirement IDs in the
 Requirement ID text box for integration with
 Requirements Gateway. 
 Ensure the requirement IDs match the corresponding requirements in
 Requirements Gateway.
4. Click the OK button to close the dialog box and return
 to the Project Explorer window.
5. Select File»Save to save the project.

Parent topic:

Configure Tests

Related concepts:

- Requirement IDs

<!--NI_TOPIC bundle=labview-unit-test-framework-toolkit path=specifying-the-digits-of-precision-for-floati.html language=enus -->
## TOPIC 00067: Specifying the Digits of Precision for Floating-Point Comparison

- bundle_id: `labview-unit-test-framework-toolkit`
- source_path: `specifying-the-digits-of-precision-for-floati.html`
- source_url: https://docs-be.ni.com/bundle/labview-unit-test-framework-toolkit/raw/resource/enus/specifying-the-digits-of-precision-for-floati.html
- document_id: `labview-unit-test-framework-toolkit`
- page_type: `leaf`
- content_type: `task`
- source_description: Complete the following steps to specify the digits of precision for comparing floating-point numbers.Open the LabVIEW project that contains the files on which you want to perform unit testing. Double-click a .lvtest file. Select Advanced from the Category list to display the Advanced page.Use the Di

### Specifying the Digits of Precision for Floating-Point Comparison

Complete the following steps to specify the digits of
 precision for comparing floating-point numbers.

1. Open the LabVIEW project that contains the files on which you want to perform
 unit testing.
2. Double-click a .lvtest file.
3. Select Advanced from the Category
 list to display the Advanced page.
4. Use the Digits of precision for floating-point comparison control to set the digits of precision for comparing floating-point numbers during test execution.
5. Click the OK button to close the dialog box and return
 to the Project Explorer window.
6. Select File»Save to save the project.

Parent topic:

Configure Advanced Settings of Tests

<!--NI_TOPIC bundle=labview-unit-test-framework-toolkit path=specifying-the-number-of-times-to-repeat-a-te.html language=enus -->
## TOPIC 00068: Specifying the Number of Times to Repeat a Test

- bundle_id: `labview-unit-test-framework-toolkit`
- source_path: `specifying-the-number-of-times-to-repeat-a-te.html`
- source_url: https://docs-be.ni.com/bundle/labview-unit-test-framework-toolkit/raw/resource/enus/specifying-the-number-of-times-to-repeat-a-te.html
- document_id: `labview-unit-test-framework-toolkit`
- page_type: `leaf`
- content_type: `task`
- source_description: Complete the following steps to specify the number of times to repeat a test.Open the LabVIEW project that contains the files on which you want to perform unit testing. Double-click a .lvtest file to display the Test Properties dialog box. Select Advanced from the Category list to display the Advanc

### Specifying the Number of Times to Repeat a Test

Complete the following steps to specify the number
 of times to repeat a test.

1. Open the LabVIEW project that contains the files on which you want to perform unit testing.
2. Double-click a .lvtest file to display the
 Test Properties dialog
 box.
3. Select Advanced from the Category
 list to display the Advanced page.
4. Use the Repetitions control to specify the number of times LabVIEW repeats this test.
5. Click the OK button to close the dialog
 box and return to the Project
 Explorer window.
6. Select File»Save to save the project.

The next time you execute this test, LabVIEW runs the VI under test the number of
 times you specified. Test results show the results of each repetition.

Parent topic:

Configure Advanced Settings of Tests

<!--NI_TOPIC bundle=labview-unit-test-framework-toolkit path=storing-vi-passwords-for-unit-testing.html language=enus -->
## TOPIC 00069: Storing VI Passwords for Unit Testing

- bundle_id: `labview-unit-test-framework-toolkit`
- source_path: `storing-vi-passwords-for-unit-testing.html`
- source_url: https://docs-be.ni.com/bundle/labview-unit-test-framework-toolkit/raw/resource/enus/storing-vi-passwords-for-unit-testing.html
- document_id: `labview-unit-test-framework-toolkit`
- page_type: `leaf`
- content_type: `task`
- source_description: You can execute tests on password-protected VIs by adding passwords to the project settings. During execution, LabVIEW stores the passwords in the LabVIEW password cache and saves them in the project file (.lvproj). LabVIEW encrypts the passwords before saving them in the project file. Complete the

### Storing VI Passwords for Unit Testing

You can execute tests on password-protected VIs by adding passwords to
 the project settings. During execution, LabVIEW stores the passwords
 in the LabVIEW password cache and saves them in the project file
 (.lvproj). LabVIEW encrypts the
 passwords before saving them in the project file.

Complete the following steps to store VI passwords to the project
 settings:

1. Open the LabVIEW project that contains the files on which you want to perform unit
 testing.
2. Click the Project Properties button
 [IMAGE alt='image' src='GUID-B39EC891-2819-46B4-84C1-E65F2860E420-a5.gif'] on the
 Project toolbar to display
 the Project Properties dialog
 box.
3. Select Unit Test Framework from the
 Category list to display the
 Unit Test Framework
 page.
4. Enter the password of the password-protected VI in the Password to Add text box.
5. Click the Add button.
6. Repeat steps 4 and 5 to add more passwords to the password list.
7. Click the OK button to close the dialog
 box and return to the Project
 Explorer window.

Clear All

Note

Clear All

Environment

Options

Parent topic:

Create Projects and Tests

Related concepts:

- Execute Tests

<!--NI_TOPIC bundle=labview-unit-test-framework-toolkit path=supported-execution-targets.html language=enus -->
## TOPIC 00070: Supported Execution Targets

- bundle_id: `labview-unit-test-framework-toolkit`
- source_path: `supported-execution-targets.html`
- source_url: https://docs-be.ni.com/bundle/labview-unit-test-framework-toolkit/raw/resource/enus/supported-execution-targets.html
- document_id: `labview-unit-test-framework-toolkit`
- page_type: `leaf`
- content_type: `concept`
- source_description: You can use the LabVIEW Unit Test Framework Toolkit to execute tests on different types of targets.The following table shows the supported target types and any additional software you must install to execute tests on that type of target:Type of TargetAdditional Required SoftwareA Windows PC—An Real-

### Supported Execution Targets

You can use the LabVIEW Unit Test Framework Toolkit to execute tests on different types
 of targets.

The following table shows the supported target types and any additional software you must install
 to execute tests on that type of target:

| Type of Target | Additional Required Software |
| --- | --- |
| A Windows PC | — |
| An Real-Time (RT) target, such as an PXI or CompactRIO controller, running a Real-Time Operating System (RTOS). | LabVIEW Real-Time ModuleDriver software for any hardware devices |

You must enable the VI Server on an RT target to execute unit tests on this RT target. You can
 enable the VI Server by using either of the following methods:

- In the Project Explorer window, configure the VI Server for the RT
 target.
- In the Test Execution section of the Unit Test
 Framework page, place a checkmark in the Enable VI Server
 on real-time targets checkbox.

Parent topic:

Unit Test Framework Toolkit

Related information:

- Software and Driver Downloads
- LabVIEW Real-Time Module Download

<!--NI_TOPIC bundle=labview-unit-test-framework-toolkit path=test-cases.html language=enus -->
## TOPIC 00071: Test Cases

- bundle_id: `labview-unit-test-framework-toolkit`
- source_path: `test-cases.html`
- source_url: https://docs-be.ni.com/bundle/labview-unit-test-framework-toolkit/raw/resource/enus/test-cases.html
- document_id: `labview-unit-test-framework-toolkit`
- page_type: `leaf`
- content_type: `concept`
- source_description: A test case contains a set of input values, expected values, and comparison types that LabVIEW uses to check the VI under test for functional correctness. Each .lvtest file contains at least one test case.When you execute a test, LabVIEW runs the VI under test by using the input values you specified

### Test Cases

A test case contains a set of input values, expected values, and comparison types that
 LabVIEW uses to check the VI under test for functional correctness. Each
 .lvtest file contains at least one test case.

When you execute a test, LabVIEW runs the VI under test by using the input values you specified
 for each test case in the .lvtest file. LabVIEW then compares the
 resulting values with the expected values by using the comparison types you
 specified.

The LabVIEW Unit Test Framework Toolkit provides the following ways to configure test cases.

- You can configure test cases interactively by using the Test Cases page
 of the Test Properties dialog box. For each test case, enter
 the input values, expected values, and comparison types for each control and
 indicator of the VI under test. Note LabVIEW lists the controls and
 indicators from the VI under test on the Test Cases page.
 If the Input/output values setting on the Unit
 Test Framework page of the Project
 Properties dialog box is Include controls and
 indicators from connector pane, make sure you select a connector
 pane pattern and assign the terminals for the VI under test.
- You also can configure test cases interactively by exchanging values between the VI under test
 and the Test Cases page. This method allows you to configure
 the input and expected values by using the front panel and then importing the values
 to the Test Cases page. You also can export values from a
 test case to the VI under test.
- You can configure test cases by editing .lvtest files.

The following figure shows an example of entering the input values, expected values, and
 comparison types for a test case:

[IMAGE alt='image' src='GUID-F022B559-3445-4601-B4DF-2310D1C95E5A-a5.png']

In the previous figure, the input values are 8 and 10, the expected value is 100, and the
 comparison type is <. When you execute this test, LabVIEW uses 8 and 10 as input
 values for the VI under test and compares the resulting value with 100. If the resulting
 value is not less than 100, test results show this test as failed.

LabVIEW displays the following data types as binary data or flattened data:

- Picture
- Array
- Variant
- Digital waveform
- Dynamic data
- Refnum
- External data
- LabVIEW class instance

LabVIEW represents these data types by using [...] on the Test
 Cases page. You cannot edit these data types on the Test
 Cases page. However, you can configure the input and expected values of
 these data types by using the front panel of the VI under test, accessible by clicking
 the Export Values to VI button, and importing the updated values
 from the VI under test to the current test case.

You also can configure the input and expected values of these data types by using setup and
 teardown VIs. When you configure a test to run setup and teardown VIs, LabVIEW lists the
 controls and indicators of the setup and teardown VIs on the Test
 Cases page. You can configure the inputs of the setup VI before passing
 the data to the VI under test. Likewise, you can configure the outputs and comparison
 types of the teardown VI after accepting the outputs of the VI under test.

The following figure shows an example of configuring the input and expected values of setup and
 teardown VIs:

[IMAGE alt='image' src='GUID-1CB60F03-C464-4DC8-8833-4BB552D38056-a5.png']

In the previous figure, the VI under test contains a LabVIEW class data type input, whose value
 assembles in the setup VI. The String input in the setup VI is a
 data member of that LabVIEW class. By setting the input value of the setup VI, you know
 the input value of the data member of the LabVIEW class. Likewise, the VI under test
 contains a LabVIEW class data type output, whose value disassembles in the teardown VI.
 By setting the expected value and comparison type of the teardown VI, you can compare
 the resulting value of the data member of the LabVIEW class.

Parent topic:

Introduction to the LabVIEW Unit Test Framework Toolkit

Related concepts:

- Setup and Teardown VIs

Related tasks:

- Exchanging Values Between the VI under Test, Setup VI, Teardown VI, and the Test Cases Page

<!--NI_TOPIC bundle=labview-unit-test-framework-toolkit path=test-priority.html language=enus -->
## TOPIC 00072: Test Priority

- bundle_id: `labview-unit-test-framework-toolkit`
- source_path: `test-priority.html`
- source_url: https://docs-be.ni.com/bundle/labview-unit-test-framework-toolkit/raw/resource/enus/test-priority.html
- document_id: `labview-unit-test-framework-toolkit`
- page_type: `leaf`
- content_type: `concept`
- source_description: A test priority determines the level of importance of a test. When you create tests, LabVIEW assigns a default priority of 5. The highest priority is 1000, and the lowest priority is 0.You can specify a test priority interactively by using the Configuration page of the Test Properties dialog box. Yo

### Test Priority

A test priority determines the level of importance of a test. When you create tests,
 LabVIEW assigns a default priority of 5. The highest priority is 1000, and the lowest
 priority is 0.

You can specify a test priority interactively by using the Configuration
 page of the Test Properties dialog box. You also can specify a
 test priority by editing .lvtest files.

When you execute tests by priority, LabVIEW executes only tests with an equal or higher priority
 than the Minimum priority you specified on the Unit
 Test Framework page of the Project Properties
 dialog box.

Parent topic:

Introduction to the LabVIEW Unit Test Framework Toolkit

Related concepts:

- Create Tests

Related tasks:

- Specifying a Test Priority
- Executing Tests by Priority

<!--NI_TOPIC bundle=labview-unit-test-framework-toolkit path=test-results-project-explorer-window.html language=enus -->
## TOPIC 00073: Test Results (Project Explorer Window)

- bundle_id: `labview-unit-test-framework-toolkit`
- source_path: `test-results-project-explorer-window.html`
- source_url: https://docs-be.ni.com/bundle/labview-unit-test-framework-toolkit/raw/resource/enus/test-results-project-explorer-window.html
- document_id: `labview-unit-test-framework-toolkit`
- page_type: `leaf`
- content_type: `concept`
- source_description: After you execute tests and return to the Project Explorer window, colored dots appear next to the icon of each test you executed. These dots denote whether the test passed (green), failed (red), produced errors (exclamation mark), or was skipped (gray). The following figure shows an example of test

### Test Results (Project Explorer Window)

After you execute tests and return to the Project Explorer window,
 colored dots appear next to the icon of each test you executed. These dots denote
 whether the test passed (green), failed (red), produced errors (exclamation mark), or
 was skipped (gray).

The following figure shows an example of test results in the Project
 Explorer window:

[IMAGE alt='image' src='GUID-7C98A5AE-2509-4266-BC4F-EC4144F4038E-a5.png']

Note

Project
 Explorer

Parent topic:

Using the Project Explorer Window

<!--NI_TOPIC bundle=labview-unit-test-framework-toolkit path=test-results.html language=enus -->
## TOPIC 00074: Test Results

- bundle_id: `labview-unit-test-framework-toolkit`
- source_path: `test-results.html`
- source_url: https://docs-be.ni.com/bundle/labview-unit-test-framework-toolkit/raw/resource/enus/test-results.html
- document_id: `labview-unit-test-framework-toolkit`
- page_type: `leaf`
- content_type: `concept`
- source_description: The LabVIEW Unit Test Framework Toolkit provides several methods of returning test results from the test execution. You can view test results in the Unit Test Framework Results window that appears after execution is complete. The Project Explorer window also displays results from the test execution.

### Test Results

The LabVIEW Unit Test Framework Toolkit provides several methods of returning test results from
 the test execution. You can view test results in the Unit Test Framework
 Results window that appears after execution is complete. The
 Project Explorer window also displays results from the test
 execution. You can generate test reports in several file formats. You also can generate
 log files.

- [Unit Test Framework Results Window](unit-test-framework-results-window.html)
- [Project Explorer Window](unit-test-framework-project-explorer-window.html)
- [Test Reports](project-explorer-window-test-results.html)
- [Log Files](log-files.html)

Parent topic:

Introduction to the LabVIEW Unit Test Framework Toolkit

Related tasks:

- Generating Test Reports
- Generating Log Files

<!--NI_TOPIC bundle=labview-unit-test-framework-toolkit path=test-vectors-and-lvvect-files.html language=enus -->
## TOPIC 00075: Test Vectors and .lvvect Files

- bundle_id: `labview-unit-test-framework-toolkit`
- source_path: `test-vectors-and-lvvect-files.html`
- source_url: https://docs-be.ni.com/bundle/labview-unit-test-framework-toolkit/raw/resource/enus/test-vectors-and-lvvect-files.html
- document_id: `labview-unit-test-framework-toolkit`
- page_type: `leaf`
- content_type: `concept`
- source_description: A test vector is an array of input or expected values that you can assign to an input or output of the VI under test. You can use test vectors to assign multiple values to an input or output of the VI under test in a test case.The LabVIEW Unit Test Framework Toolkit provides test vectors you use to

### Test Vectors and .lvvect Files

A test vector is an array of input or expected values that you can assign to an input or
 output of the VI under test. You can use test vectors to assign multiple values to an
 input or output of the VI under test in a test case.

Project
 Explorer

.lvvect

.lvvect

Items

Files

Note

.lvvect

Default location file path

Unit Test Framework

Project
 Properties

The Unit Test Framework Toolkit provides the following two types of test vectors:

Sequence

Linear

First element

Second element

Third element

You can edit test vectors by using the following methods:

- Using the Test Vector Properties - Edit dialog box.
- Using the front panel of a VI.
- Using third-party text editors.

#### Test Vector File Format

You
 can view and edit .lvvect files by using Microsoft Excel or a
 text editor.

Note

.lvvect

.txt

.lvvect

.lvvect

The following
 table contains information about each component of a .lvvect
 file, including descriptions, default values, and notes:

| Component | Description | Default Value | Notes |
| --- | --- | --- | --- |
| LabVIEW Unit Test Framework | Header information that LabVIEW uses to identify test vectors that you created by using the Unit Test Framework Toolkit. | N/A | Do not modify. |
| Version | Header information that LabVIEW uses to identify the version of the Unit Test Framework Toolkit the test vector file was created in. | Automatic | Do not modify. |
| Library | Specifies the path to the LabVIEW class library (.lvclass) or the LabVIEW project library (.lvlib) the test vector file belongs to, if any. | Automatic | If the .lvvect file is located in the same drive as the library, use the relative path. Otherwise, use the absolute path. |
| Namespace | Specifies the name of the LabVIEW class library (.lvclass) or the LabVIEW project library (.lvlib) that the test vector file belongs to, if any. | Automatic | N/A |
| Include | Lists the test vector files that this test vector file includes. You can use these test vector files in a test. | Optional | N/A |
| Test Vector | Lists test vectors that belong to this test vector file. If you open this test vector file in Microsoft Excel, each column in this section indicates a test vector. | N/A | Refer to the table below for detailed information about each component of a test vector. |

Note

LabVIEW automatically gathers and displays measurements when you create a
 test.

The following table contains information about each sub-component of a test
 vector in the Test Vector component of a test vector
 file:

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

#### Example of a .lvvect File

The following figure shows an example of a test vector file:

[IMAGE alt='image' src='GUID-ADEE9410-3897-4333-A623-DD5A8508DE1C-a5.png']

You can add, edit, and remove test vectors by editing this test vector file in
 Microsoft Excel or a text editor.

Parent topic:

Introduction to the LabVIEW Unit Test Framework Toolkit

<!--NI_TOPIC bundle=labview-unit-test-framework-toolkit path=tests-and-lvtest-files.html language=enus -->
## TOPIC 00076: Tests and .lvtest Files

- bundle_id: `labview-unit-test-framework-toolkit`
- source_path: `tests-and-lvtest-files.html`
- source_url: https://docs-be.ni.com/bundle/labview-unit-test-framework-toolkit/raw/resource/enus/tests-and-lvtest-files.html
- document_id: `labview-unit-test-framework-toolkit`
- page_type: `leaf`
- content_type: `concept`
- source_description: The LabVIEW Unit Test Framework Toolkit provides tests and .lvtest files you can use to create tests to check VIs for functional correctness.When you create a test from the Project Explorer window, LabVIEW creates a .lvtest file on disk. A .lvtest icon appears on both the Items and Files pages.Each

### Tests and .lvtest Files

The LabVIEW Unit Test Framework Toolkit provides tests and .lvtest
 files you can use to create tests to check VIs for functional correctness.

When you create a test from the Project Explorer window, LabVIEW creates a
 .lvtest file on disk. A .lvtest icon appears
 on both the Items and Files pages.

.lvtest

.lvtest

Note

.lvtest

Default location file path

Unit Test Framework

Project
 Properties

Use the Project Explorer window to configure tests interactively. You also
 can configure tests by editing .lvtest files.

#### Test File Format

You can
 view and edit .lvtest files by using Microsoft Excel or a text
 editor.

Note

.lvtest

.txt

.lvtest

.lvtest

Microsoft Excel documentation

The
 following table contains information about each component of a
 .lvtest file, including descriptions, default values, and
 notes. When you edit a .lvtest file, the file must include
 components that LabVIEW uses to read and execute a test.

| Component | Description | Default Value | Notes |
| --- | --- | --- | --- |
| LabVIEW Unit Test Framework | Header information that LabVIEW uses to identify tests that you created by using the Unit Test Framework Toolkit. | N/A | Do not modify. |
| Version | Header information that LabVIEW uses to identify the version of the Unit Test Framework Toolkit the test was created in. | Automatic | Do not modify. |
| VI under Test | Specifies the path to the VI under test. If the .lvtest file is located in the same directory as the VI under test, LabVIEW displays only the name of the VI without the path. | Automatic | If the .lvtest file is located in the same drive as the VI under test, use the relative path. Otherwise, use the absolute path. You can specify only one VI under test for each .lvtest file. |
| Library | Specifies the path to the LabVIEW class library (.lvtest) or the LabVIEW project library (.lvlib) the test vector file belongs to, if any. | Automatic | If the .lvtest file is located in the same drive as the library, use the relative path. Otherwise, use the absolute path. |
| Comment | Specifies comments about the test. | N/A | Comment cannot contain line breaks. |
| Priority | Specifies priority of the test. This priority determines whether LabVIEW executes the test when you execute tests by priority. | 5 | The highest priority is 1000, and the lowest priority is 0. |
| Requirement ID | Specifies requirement IDs for integration with NI Requirements Gateway. | Optional | N/A |
| Skip Test (Project Explorer Window) | Specifies whether to skip the test when you execute tests interactively from the Project Explorer window. | NO | YES/NO |
| Skip Test (Unit Test Framework VIs) | Specifies whether to skip the test when you execute tests programmatically by using the Unit Test Framework VIs. | NO | YES/NO |
| Decimal Separator | Specifies the character LabVIEW uses to separate the integral and fractional parts of a decimal number. | . | Valid decimal separators: . , |
| Set Timeout | Specifies whether to set a timeout when executing the test. | NO | YES/NO |
| Timeout | Specifies the time limit, in seconds, in which LabVIEW must complete the test execution. | 0 | Use a numeric value. This value is valid only when Set Timeout is set to YES. |
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
| Save Control Names in Normal Format | Specifies whether to save control names in normal format. If a control name contains non-printable control characters used for text formatting, which are the first 32 codes (from 0 to 31) in the ASCII code table, LabVIEW displays NO. Otherwise, LabVIEW displays YES. | Automatic | Do not modify. |
| Capture Input Values | Specifies whether to capture the default input values from the VI under test when creating a test. | YES | N/A |
| Capture Output Values | Specifies whether to capture the default output values from the VI under test when creating a test. | YES | N/A |
| Set Automatic Error Handling | Specifies whether to automatically handle errors for the VI under test during test execution. | As is | Available options:- As is- Enable automatic error handling- Disable automatic error handling |
| Remove Breakpoints | Specifies whether to toggle test execution suspension at a breakpoint. | YES | YES/NO |
| Test Case Name | Lists the name of each test case. | 1 | Use a numeric value or a user-defined name. Test Case Name cannot contain components of a.lvtest file. |
| Test Case Comment | Specifies comments about the test case. | N/A | Test Case Comment cannot contain line breaks. |
| Test Case | Lists the name of each test case. | Automatic | N/A |
| VI | Specifies the type of VI which contains the terminals to configure a test case. | N/A | Valid VI types:- VI under Test- Setup VI- Teardown VI |
| In/Out | Specifies whether LabVIEW uses each terminal as an input or output. | Default for controls is IN.Default for indicators is OUT. | IN/OUT |
| Set/Check | Specifies whether each terminal sets, checks, or ignores the input or expected value. | Default for controls is SET.Default for indicators is CHECK. | SET/CHECK/IGNORE |
| Control Name | Specifies the name of each terminal. | Automatic | Name must match the terminals on the VI under test. If the terminal is an array, the number in square brackets ([ ]) indicates the index of a specific array element. The index is zero-based, which means it is in the range of 0 to n-1, where n is the number of elements in the array or cluster. For example, Array[0] refers to the first element of the array. If the terminal is a cluster, LabVIEW uses a forward slash (/) to separate control and indicator names. You can change the default array brackets and name separator on the Unit Test Framework page of the Project Properties dialog box. |
| Data Type | Specifies the data type of each terminal. | Automatic | N/A |
| Value | Specifies the input or expected value of each terminal. | Automatic | N/A |
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

Caution

.lvtest

Note

LabVIEW automatically gathers and displays measurements when you create a
 test.

#### Example of a .lvtest
 File

The following figure shows an example of a
 .lvtest file:

[IMAGE alt='image' src='GUID-FAE28DC9-D0AD-49DC-9A2A-961E23B685C1-a5.png']

Parent topic:

Introduction to the LabVIEW Unit Test Framework Toolkit

Related concepts:

- Create Tests
- Create Projects and Tests
- Execute Tests

<!--NI_TOPIC bundle=labview-unit-test-framework-toolkit path=unit-test-framework-project-explorer-window.html language=enus -->
## TOPIC 00077: Project Explorer Window

- bundle_id: `labview-unit-test-framework-toolkit`
- source_path: `unit-test-framework-project-explorer-window.html`
- source_url: https://docs-be.ni.com/bundle/labview-unit-test-framework-toolkit/raw/resource/enus/unit-test-framework-project-explorer-window.html
- document_id: `labview-unit-test-framework-toolkit`
- page_type: `leaf`
- content_type: `concept`
- source_description: After you execute tests and return to the Project Explorer window, colored dots appear next to the icon of each test you executed. These dots denote whether the test passed (green), failed (red), produced errors (exclamation mark), or was skipped (gray). The following figure shows an example of test

### Project Explorer Window

After you execute tests and return to the Project Explorer window,
 colored dots appear next to the icon of each test you executed. These dots denote
 whether the test passed (green), failed (red), produced errors (exclamation mark), or
 was skipped (gray).

The following figure shows an example of test results in the Project
 Explorer window:

[IMAGE alt='image' src='GUID-7C98A5AE-2509-4266-BC4F-EC4144F4038E-a5.png']

Note

Project
 Explorer

Parent topic:

Test Results

<!--NI_TOPIC bundle=labview-unit-test-framework-toolkit path=unit-test-framework-results-window.html language=enus -->
## TOPIC 00078: Unit Test Framework Results Window

- bundle_id: `labview-unit-test-framework-toolkit`
- source_path: `unit-test-framework-results-window.html`
- source_url: https://docs-be.ni.com/bundle/labview-unit-test-framework-toolkit/raw/resource/enus/unit-test-framework-results-window.html
- document_id: `labview-unit-test-framework-toolkit`
- page_type: `leaf`
- content_type: `concept`
- source_description: The Unit Test Framework Results window provides both summary and detailed information about the test execution, including tests and VIs that passed, failed, were skipped, or produced errors. Use this window to view test results. You also can save the results from this window to a .lvutf file that yo

### Unit Test Framework Results Window

The Unit Test Framework Results window provides both summary and
 detailed information about the test execution, including tests and VIs that passed,
 failed, were skipped, or produced errors. Use this window to view test results.

You also can save the results from this window to a .lvutf file that
 you can load later.

A .lvutf file contains the test results of the test execution. You
 can read .lvutf files interactively from the project window or
 programmatically by using the Open Results Window VI. LabVIEW loads
 .lvutf files in the Unit Test Framework
 Results window only.

The following figure shows an example of test results in the Unit Test
 Framework Results window:

[IMAGE alt='image' src='GUID-F8539F76-37DF-470C-B03B-464277D221D4-a5.png']

Parent topic:

Test Results

Related concepts:

- Saving and Loading Test Results

<!--NI_TOPIC bundle=labview-unit-test-framework-toolkit path=unit-test-framework-toolbar.html language=enus -->
## TOPIC 00079: Unit Test Framework Toolbar (Project Explorer Window)

- bundle_id: `labview-unit-test-framework-toolkit`
- source_path: `unit-test-framework-toolbar.html`
- source_url: https://docs-be.ni.com/bundle/labview-unit-test-framework-toolkit/raw/resource/enus/unit-test-framework-toolbar.html
- document_id: `labview-unit-test-framework-toolkit`
- page_type: `leaf`
- content_type: `concept`
- source_description: Use the buttons on the Unit Test Framework toolbar to execute tests and view the Unit Test Framework Results window. This toolbar is available at the top of the Project Explorer window. You might need to expand the Project Explorer window horizontally to view this toolbar. You can show or hide the U

### Unit Test Framework Toolbar (Project Explorer
 Window)

Use the buttons on the Unit Test Framework toolbar to execute
 tests and view the Unit Test Framework Results window. This
 toolbar is available at the top of the Project Explorer
 window.

Note

Project Explorer

You can show or hide the Unit Test Framework toolbar by selecting View»Toolbars»Unit Test Framework. You also can right-click an unused area on the toolbar and select
 Unit Test Framework.

The Unit Test Framework toolbar on the Project
 Explorer window contains the following buttons:

|  | Run Unit Tests — Executes all tests in a LabVIEW project. If test filters are set, such as executing tests by priority or executing only modified tests, LabVIEW executes only filtered tests. |
| --- | --- |
|  | Unit Test Framework Results — Displays the Unit Test Framework Results window. Use this window to view, save, and load test results. |

Parent topic:

Using the Project Explorer Window

Related concepts:

- Execute Tests Interactively
- Saving and Loading Test Results
- Test Results

Related tasks:

- Executing Only Modified Tests
- Executing Tests by Priority

<!--NI_TOPIC bundle=labview-unit-test-framework-toolkit path=unit-test-framework-toolkit.html language=enus -->
## TOPIC 00080: Unit Test Framework Toolkit

- bundle_id: `labview-unit-test-framework-toolkit`
- source_path: `unit-test-framework-toolkit.html`
- source_url: https://docs-be.ni.com/bundle/labview-unit-test-framework-toolkit/raw/resource/enus/unit-test-framework-toolkit.html
- document_id: `labview-unit-test-framework-toolkit`
- page_type: `leaf`
- content_type: `concept`
- source_description: The LabVIEW Unit Test Framework Toolkit provides tools you use to check VIs for functional correctness. Use the Project Explorer window to create, configure, manage, and execute tests interactively in a LabVIEW project. You also can execute tests programmatically by using the Unit Test Framework VIs

### Unit Test Framework Toolkit

The LabVIEW Unit Test Framework Toolkit provides tools you use to check VIs for functional
 correctness. Use the Project Explorer window to create,
 configure, manage, and execute tests interactively in a LabVIEW project. You also can
 execute tests programmatically by using the Unit Test Framework
 VIs.

- [Supported Execution Targets](supported-execution-targets.html)
- [Quick Start Guide](quick-start-guide.html)
- [Introduction to the LabVIEW Unit Test Framework Toolkit](introduction-to-the-labview-unit-test-framewo.html)
- [Create Projects and Tests](creating-projects-and-tests.html)
- [Configure Tests](configuring-tests.html)
- [Create Test Vector Files and Test Vectors](creating-test-vector-files-and-test-vectors.html)
- [Manage Tests](managing-tests.html)
- [Execute Tests](executing-tests.html)
- [View Test Results and Generating Reports](viewing-test-results-and-generating-reports.html)

<!--NI_TOPIC bundle=labview-unit-test-framework-toolkit path=user-manual-welcome.html language=enus -->
## TOPIC 00081: LabVIEW Unit Test Framework Toolkit User Manual

- bundle_id: `labview-unit-test-framework-toolkit`
- source_path: `user-manual-welcome.html`
- source_url: https://docs-be.ni.com/bundle/labview-unit-test-framework-toolkit/raw/resource/enus/user-manual-welcome.html
- document_id: `labview-unit-test-framework-toolkit`
- page_type: `leaf`
- content_type: `concept`
- source_description: The LabVIEW Unit Test Framework Toolkit User Manual provides detailed descriptions of the product functionality and the step by step processes for use. Looking for Something Else?For information not found in the User Manual for your product, such as specifications and API reference, browse Related I

### LabVIEW Unit Test Framework Toolkit
 User Manual

The LabVIEW Unit Test Framework Toolkit User Manual provides detailed
 descriptions of the product functionality and the step by step processes for use.

#### Looking for Something Else?

For information not found in the User Manual
 for your product, such as specifications and API reference, browse *Related
 Information*.

Related information:

- Hardware and Software Operating System Compatibility
- License Setup and Activation

<!--NI_TOPIC bundle=labview-unit-test-framework-toolkit path=using-folders-to-organize-a-project.html language=enus -->
## TOPIC 00082: Using Folders to Organize a Project

- bundle_id: `labview-unit-test-framework-toolkit`
- source_path: `using-folders-to-organize-a-project.html`
- source_url: https://docs-be.ni.com/bundle/labview-unit-test-framework-toolkit/raw/resource/enus/using-folders-to-organize-a-project.html
- document_id: `labview-unit-test-framework-toolkit`
- page_type: `leaf`
- content_type: `task`
- source_description: Complete the following steps to organize VIs, .lvtest files, and .lvvect files in a project. You can use virtual folders, auto-populating folders, and project libraries to organize a project. Open the LabVIEW project that contains the files on which you want to perform unit testing. Add a folder or

### Using Folders to Organize a Project

.lvtest

.lvvect

1. Open the LabVIEW project that contains the files on which you want to perform
 unit testing.
2. Add a folder or project library to a project.
3. Drag and drop VIs, .lvtest files, and
 .lvvect files to this folder. You also can add folders
 inside a folder.
4. Select File»Save to save the project.

Parent topic:

Organize a Project

<!--NI_TOPIC bundle=labview-unit-test-framework-toolkit path=using-test-vector-indexes.html language=enus -->
## TOPIC 00083: Using Test Vector Indexes

- bundle_id: `labview-unit-test-framework-toolkit`
- source_path: `using-test-vector-indexes.html`
- source_url: https://docs-be.ni.com/bundle/labview-unit-test-framework-toolkit/raw/resource/enus/using-test-vector-indexes.html
- document_id: `labview-unit-test-framework-toolkit`
- page_type: `leaf`
- content_type: `concept`
- source_description: In the Test Cases page, you can assign test vectors to each input or output of a VI to test this VI with multiple input or expected values in one test case. After you assign test vectors to inputs of the VI under test, LabVIEW generates permutations for the input values. After you assign test vector

### Using Test Vector Indexes

In the Test Cases page, you can assign test vectors to each input
 or output of a VI to test this VI with multiple input or expected values in one test
 case.

After you assign test vectors to inputs of the VI under test, LabVIEW generates
 permutations for the input values. After you assign test vectors to outputs of the VI
 under test, LabVIEW compares the number of the input permutations and the size of the
 test vector assigned to the output terminal in the following methods:

- When the number of the input permutations is equal to the size of the test vector
 assigned to the output terminal, LabVIEW executes the test by comparing the
 resulting values with the expected values in the test vector.
- When the number of the input permutations is smaller than the size of the test
 vector assigned to the output terminal, LabVIEW executes the test and the
 Test Cases page displays a warning icon.
- When the number of the input permutations is larger than the size of the test vector
 assigned to the output terminal, LabVIEW reports an error and does not execute the
 test.

You can use test vector indexes to configure the numbers of input value permutations.
 LabVIEW does not set indexes to test vector by default. If the assigned test vectors
 have no or different indexes, LabVIEW generates all possible permutations of the input
 values. For example, you create two sequence test vectors, (3, 4, 5) and (1, 2). You
 then assign these test vectors to the x and
 y controls of the following VI with no or different
 indexes.

The following picture shows a block diagram of example test vectors:

[IMAGE alt='image' src='GUID-532BAE2F-CC8B-4F2C-AF61-7AC494D5D5BC-a5.gif']

When you execute this test, LabVIEW tests this VI for six times with the following
 x and y values:

- x=3 y=1
- x=3 y=2
- x=4 y=1
- x=4 y=2
- x=5 y=1
- x=5 y=2

If the assigned test vectors have identical indexes, LabVIEW sends the test vector values
 to the inputs one by one and stops the test when any test vector reaches the end. For
 example, you can assign two test vectors, (3, 4, 5) and (1, 2), to the
 x and y controls of the previous VI
 and set the indexes of these test vectors to index 1. When you execute this test,
 LabVIEW tests this VI for twice with the following x and
 y values:

- x=3 y=1
- x=4 y=2

Parent topic:

Test Vectors and .lvvect Files

Related tasks:

- Assigning Test Vectors in Test Cases

<!--NI_TOPIC bundle=labview-unit-test-framework-toolkit path=using-the-project-explorer-window.html language=enus -->
## TOPIC 00084: Using the Project Explorer Window

- bundle_id: `labview-unit-test-framework-toolkit`
- source_path: `using-the-project-explorer-window.html`
- source_url: https://docs-be.ni.com/bundle/labview-unit-test-framework-toolkit/raw/resource/enus/using-the-project-explorer-window.html
- document_id: `labview-unit-test-framework-toolkit`
- page_type: `leaf`
- content_type: `concept`
- source_description: Use the Project Explorer window to create, configure, manage, and execute tests interactively in a LabVIEW project.You must create and save a LabVIEW project before you can create tests. When you save a project, LabVIEW creates a project file (.lvproj) that includes references to all the files in th

### Using the Project Explorer Window

Use the Project Explorer window to create, configure, manage, and
 execute tests interactively in a LabVIEW project.

You must create and save a LabVIEW project before you can create tests. When you save a project,
 LabVIEW creates a project file (.lvproj) that includes references
 to all the files in the project. Use projects to group together all the files you need
 to perform unit testing. Use virtual folders, auto-populating folders, and LabVIEW
 project libraries to organize a project.

The Project Explorer window includes the following:

- [Items and Files Pages](items-and-files-pages.html)
- [Test Results (Project Explorer Window)](test-results-project-explorer-window.html)
- [Unit Test Framework Toolbar (Project Explorer Window)](unit-test-framework-toolbar.html)
- [Using the Project Properties Dialog Box](using-the-project-properties-dialog-box.html)
- [Build Specifications](build-specifications.html)

Parent topic:

Introduction to the LabVIEW Unit Test Framework Toolkit

<!--NI_TOPIC bundle=labview-unit-test-framework-toolkit path=using-the-project-properties-dialog-box.html language=enus -->
## TOPIC 00085: Using the Project Properties Dialog Box

- bundle_id: `labview-unit-test-framework-toolkit`
- source_path: `using-the-project-properties-dialog-box.html`
- source_url: https://docs-be.ni.com/bundle/labview-unit-test-framework-toolkit/raw/resource/enus/using-the-project-properties-dialog-box.html
- document_id: `labview-unit-test-framework-toolkit`
- page_type: `leaf`
- content_type: `task`
- source_description: You can configure global settings related to creating and executing tests by using the Project Properties dialog box. To open the Project Properties dialog box, use one of the following methods: In the Project Explorer window, select Project»Properties to display this dialog box. You also can click

### Using the Project Properties Dialog
 Box

Project Properties

Project Properties

- In the Project Explorer window, select Project»Properties to display this dialog box.
- You also can click the Project Properties button on the
 Project toolbar or right-click the project root and
 select Properties from the shortcut menu to display this
 dialog box.

Parent topic:

Using the Project Explorer Window

<!--NI_TOPIC bundle=labview-unit-test-framework-toolkit path=viewing-test-results-and-generating-reports.html language=enus -->
## TOPIC 00086: View Test Results and Generating Reports

- bundle_id: `labview-unit-test-framework-toolkit`
- source_path: `viewing-test-results-and-generating-reports.html`
- source_url: https://docs-be.ni.com/bundle/labview-unit-test-framework-toolkit/raw/resource/enus/viewing-test-results-and-generating-reports.html
- document_id: `labview-unit-test-framework-toolkit`
- page_type: `leaf`
- content_type: `concept`
- source_description: Use this section to learn step-by-step instructions for viewing test results, generating test reports, and generating log files.Use the Unit Test Framework Results window to view test results. Use the Project Properties to configure which test reports and log files you want to generate. You can cust

### View Test Results and Generating
 Reports

Use this section to learn step-by-step instructions for viewing test results,
 generating test reports, and generating log files.

Use the Unit Test Framework Results window to view test results. Use the
 Project Properties to configure which test
 reports and log files you want to generate. You can customize test reports
 by specifying the contents of the reports. You also can format HTML reports
 by using a Cascading Style Sheet (CSS) file.

- [Saving and Loading Test Results](saving-and-loading-test-results.html#GUID-796A35AB-200D-4267-8C8C-CEC086149B7F)
- [Generating Test Reports](generating-test-reports.html)
- [Generating Log Files](generating-log-files.html)
- [Customizing Test Reports](customizing-test-reports.html)

Parent topic:

Unit Test Framework Toolkit

Related concepts:

- Test Results

Related tasks:

- Generating Log Files
- Generating Test Reports

Related information::

- Customizing Test Reports
