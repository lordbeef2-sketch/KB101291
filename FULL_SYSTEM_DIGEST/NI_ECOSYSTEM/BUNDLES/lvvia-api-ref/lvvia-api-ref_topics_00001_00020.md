# NI DOCUMENT BUNDLE: lvvia-api-ref

<!--NI_BUNDLE_CHUNK bundle=lvvia-api-ref start=1 end=20 -->
<!--NI_TOPIC bundle=lvvia-api-ref path=errors/vi-analyzer-error-codes-vi-analyzer-toolkit.html language=enus -->
## TOPIC 00001: VI Analyzer Error Codes (VI Analyzer Toolkit)

- bundle_id: `lvvia-api-ref`
- source_path: `errors/vi-analyzer-error-codes-vi-analyzer-toolkit.html`
- source_url: https://docs-be.ni.com/bundle/lvvia-api-ref/raw/resource/enus/errors/vi-analyzer-error-codes-vi-analyzer-toolkit.html
- document_id: `lvvia-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: The VI Analyzer VIs can return the following error codes. Code Name Description14200 VIAn_CannotExclude The path you specified either is not a valid path or does not exist in the VI Analyzer item list.14201 VIAn_CannotModify You attempted to modify an item path that does not exist in the VI Analyzer

### VI Analyzer Error Codes (VI Analyzer Toolkit)

The [VI Analyzer](../menus/categories/programming/vianalyzertk-mnu.html) VIs can return the following error codes.

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

<!--NI_TOPIC bundle=lvvia-api-ref path=labview-vi-analyzer-toolkit-copyright.html language=enus -->
## TOPIC 00002: LabVIEW VI Analyzer Toolkit Copyright

- bundle_id: `lvvia-api-ref`
- source_path: `labview-vi-analyzer-toolkit-copyright.html`
- source_url: https://docs-be.ni.com/bundle/lvvia-api-ref/raw/resource/enus/labview-vi-analyzer-toolkit-copyright.html
- document_id: `lvvia-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Under the copyright laws, this publication may not be reproduced or transmitted in any form, electronic or mechanical, including photocopying, recording, storing in an information retrieval system, or translating, in whole or in part, without the prior written consent of National Instruments Corpora

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

<!--NI_TOPIC bundle=lvvia-api-ref path=menus/categories/programming/vianalyzertk-mnu.html language=enus -->
## TOPIC 00003: VI Analyzer

- bundle_id: `lvvia-api-ref`
- source_path: `menus/categories/programming/vianalyzertk-mnu.html`
- source_url: https://docs-be.ni.com/bundle/lvvia-api-ref/raw/resource/enus/menus/categories/programming/vianalyzertk-mnu.html
- document_id: `lvvia-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Use the VI Analyzer VIs with the LabVIEW VI Analyzer Toolkit to programmatically run tests that check VIs for style, efficiency, and other aspects of LabVIEW programming. Note Select Tools>>VI Analyzer>>Analyze VIs to use the VI Analyzer to interactively run tests on an open VI or to create a VI Ana

### VI Analyzer

Use the VI Analyzer VIs with the LabVIEW VI Analyzer Toolkit to programmatically run tests that check VIs for style, efficiency, and other aspects of LabVIEW programming. 

**Note** Select **Tools>>VI Analyzer>>Analyze VIs** to use the VI Analyzer to interactively run tests on an open VI or to create a VI Analyzer task to analyze a set of VIs.

You can add VIs written with the VI Analyzer VIs to the labview\project\_VI Analyzer\Quick Launch folder. These VIs appear as menu options in **Tools»VI Analyzer»Quick Launch**. If you want to create a quick launch test, you must start with the following template:

labview\vi. lib\addons\analyzer\analyzerapi. llb\VIAn Quick Launch VI Template. vit

The VIs you run from the **Quick Launch** menu run in a [private application instance](/csh?context=lvcore_lvconcepts_application_instances) that is separate from the main application instance.

The VIs on this palette can return [VI Analyzer error codes](/csh?context=lvmnt_via_lvvianalyzer_vi_analyzer_error_codes).

[IMAGE alt='icon' src='vianalyzertk-mnu.png']

- [VIAn Easy Analyze VI](../../../vi-lib/addons/analyzer/analyzerapi-llb/vian-easy-analyze-vi.html) Runs a VI Analyzer task automatically using settings in the specified configuration file.
- [VIAn Easy Report VI](../../../vi-lib/addons/analyzer/analyzerapi-llb/vian-easy-report-vi.html) Exports the results of an analysis to a file, either as a report in ASCII or HTML format or as a VI Analyzer results file.
- [VIAn New Task VI](../../../vi-lib/addons/analyzer/analyzerapi-llb/vian-new-task-vi.html) Creates a VI Analyzer task, which you can use with other VI Analyzer VIs to configure and run an analysis.
- [VIAn Run VI](../../../vi-lib/addons/analyzer/analyzerapi-llb/vian-run-vi.html) Analyzes VIs using the settings that VI Analyzer Task in specifies. You can wire the results to the VIAn Easy Report VI.
- [VIAn Save Configuration File VI](../../../vi-lib/addons/analyzer/analyzerapi-llb/vian-save-configuration-file-vi.html) Saves the current VI Analyzer task settings to a configuration file.
- [VIAn Destroy Task VI](../../../vi-lib/addons/analyzer/analyzerapi-llb/vian-destroy-task-vi.html) Closes an existing VI Analyzer task reference and releases resources associated with the task.
- [VI Analyzer Utilities](../../../menus/categories/programming/vianalyzertk/analyzeradv-mnu.html) Use the VI Analyzer Utilities VIs to modify the configuration settings for a VI Analyzer task.

<!--NI_TOPIC bundle=lvvia-api-ref path=menus/categories/programming/vianalyzertk/analyzeradv-mnu.html language=enus -->
## TOPIC 00004: VI Analyzer Utilities

- bundle_id: `lvvia-api-ref`
- source_path: `menus/categories/programming/vianalyzertk/analyzeradv-mnu.html`
- source_url: https://docs-be.ni.com/bundle/lvvia-api-ref/raw/resource/enus/menus/categories/programming/vianalyzertk/analyzeradv-mnu.html
- document_id: `lvvia-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Use the VI Analyzer Utilities VIs to modify the configuration settings for a VI Analyzer task. The VIs on this palette can return VI Analyzer error codes. icon

### VI Analyzer Utilities

Use the VI Analyzer Utilities VIs to modify the configuration settings for a VI Analyzer task.

The VIs on this palette can return [VI Analyzer error codes](/csh?context=lvmnt_via_lvvianalyzer_vi_analyzer_error_codes).

[IMAGE alt='icon' src='analyzeradv-mnu.png']

- [VIAn Get Items VI](../../../../vi-lib/addons/analyzer/analyzerapi-llb/vian-get-items-vi.html) Returns a list of all top-level VIs, folders, or LLBs in the VI Analyzer task.
- [VIAn Add Item VI](../../../../vi-lib/addons/analyzer/analyzerapi-llb/vian-add-item-vi.html) Adds an item, such as a VI, LLB, or folder, to the VI Analyzer task.
- [VIAn Remove Item VI](../../../../vi-lib/addons/analyzer/analyzerapi-llb/vian-remove-item-vi.html) Removes an item, such as a VI, LLB, or folder, or excludes a subitem, such as a VI within an LLB or folder, from the VI Analyzer task.
- [VIAn Get Tests VI](../../../../vi-lib/addons/analyzer/analyzerapi-llb/vian-get-tests-vi.html) Returns a cluster array containing the configuration information for each test in the VI Analyzer task.
- [VIAn Modify Test Settings VI](../../../../vi-lib/addons/analyzer/analyzerapi-llb/vian-modify-test-settings-vi.html) Modifies the configuration settings of a single test.
- [VIAn Modify Test Config Value VI](../../../../vi-lib/addons/analyzer/analyzerapi-llb/vian-modify-test-config-value-vi.html) Modifies the value of a single configuration option for a specific test.
- [VIAn Exclude Tests from VI VI](../../../../vi-lib/addons/analyzer/analyzerapi-llb/vian-exclude-tests-from-vi-vi.html) Specifies the tests to exclude for a specific VI in the VI Analyzer task.
- [VIAn Select Tests VI](../../../../vi-lib/addons/analyzer/analyzerapi-llb/vian-select-tests-vi.html) Selects or deselects the specified tests in the VI Analyzer task.
- [VIAn Get Analysis Status VI](../../../../vi-lib/addons/analyzer/analyzerapi-llb/vian-get-analysis-status-vi.html) Monitors the progress of the analysis.

Parent topic:

VI Analyzer

<!--NI_TOPIC bundle=lvvia-api-ref path=vi-lib/addons/analyzer/analyzerapi-llb/vian-add-item-vi.html language=enus -->
## TOPIC 00005: VIAn Add Item VI

- bundle_id: `lvvia-api-ref`
- source_path: `vi-lib/addons/analyzer/analyzerapi-llb/vian-add-item-vi.html`
- source_url: https://docs-be.ni.com/bundle/lvvia-api-ref/raw/resource/enus/vi-lib/addons/analyzer/analyzerapi-llb/vian-add-item-vi.html
- document_id: `lvvia-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Adds an item, such as a VI, LLB, or folder, to the VI Analyzer task. icon Inputs/Outputs cdlrn.png VI Analyzer Task in VI Analyzer Task in contains a reference to the current task. The VI Analyzer task must be a valid task that you created using the VIAn New Task VI. cpath.png Item to Add Item to Ad

### VIAn Add Item VI

Adds an item, such as a VI, LLB, or folder, to the VI Analyzer task.

[IMAGE alt='icon' src='vian-add-item-vi.png']

#### Inputs/Outputs

| VI Analyzer Task in — VI Analyzer Task in contains a reference to the current task. The VI Analyzer task must be a valid task that you created using the VIAn New Task VI. Item to Add — Item to Add specifies the path to the VI, LLB, or folder you want to add to the VI Analyzer task. If you specify an LLB or folder, the VI adds all the VIs included in the LLB or folder to the VI Analyzer task. If you specify an invalid path or a path to an invalid item, the VI returns an error. error in (no error) — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. VI Analyzer Task out — VI Analyzer Task out returns a reference to the VI Analyzer task specified in VI Analyzer Task in. error out — error out contains error information. This output provides standard error out functionality. |
| --- |

Parent topic:

VI Analyzer Utilities

<!--NI_TOPIC bundle=lvvia-api-ref path=vi-lib/addons/analyzer/analyzerapi-llb/vian-destroy-task-vi.html language=enus -->
## TOPIC 00006: VIAn Destroy Task VI

- bundle_id: `lvvia-api-ref`
- source_path: `vi-lib/addons/analyzer/analyzerapi-llb/vian-destroy-task-vi.html`
- source_url: https://docs-be.ni.com/bundle/lvvia-api-ref/raw/resource/enus/vi-lib/addons/analyzer/analyzerapi-llb/vian-destroy-task-vi.html
- document_id: `lvvia-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Closes an existing VI Analyzer task reference and releases resources associated with the task. icon Inputs/Outputs cdlrn.png VI Analyzer Task in VI Analyzer Task in contains a reference to the current task. The VI Analyzer task must be a valid task that you created using the VIAn New Task VI. cerrco

### VIAn Destroy Task VI

Closes an existing VI Analyzer task reference and releases resources associated with the task.

[IMAGE alt='icon' src='vian-destroy-task-vi.png']

#### Inputs/Outputs

| VI Analyzer Task in — VI Analyzer Task in contains a reference to the current task. The VI Analyzer task must be a valid task that you created using the VIAn New Task VI. error in (no error) — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. error out — error out contains error information. This output provides standard error out functionality. |
| --- |

Parent topic:

VI Analyzer

<!--NI_TOPIC bundle=lvvia-api-ref path=vi-lib/addons/analyzer/analyzerapi-llb/vian-easy-analyze-vi.html language=enus -->
## TOPIC 00007: VIAn Easy Analyze VI

- bundle_id: `lvvia-api-ref`
- source_path: `vi-lib/addons/analyzer/analyzerapi-llb/vian-easy-analyze-vi.html`
- source_url: https://docs-be.ni.com/bundle/lvvia-api-ref/raw/resource/enus/vi-lib/addons/analyzer/analyzerapi-llb/vian-easy-analyze-vi.html
- document_id: `lvvia-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Runs a VI Analyzer task automatically using settings in the specified configuration file. icon Inputs/Outputs cpath.png Analysis Target Analysis Target specifies the path to the configuration file that contains VI Analyzer task settings to use in the analysis. You can use a configuration file you sa

### VIAn Easy Analyze VI

Runs a VI Analyzer task automatically using settings in the specified configuration file.

[IMAGE alt='icon' src='vian-easy-analyze-vi.png']

#### Inputs/Outputs

| Analysis Target — Analysis Target specifies the path to the configuration file that contains VI Analyzer task settings to use in the analysis. You can use a configuration file you saved through the VI Analyzer or the VI Analyzer VIs. Alternatively, you can specify a VI, folder, or LLB to analyze. error in (no error) — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. Configuration File Password — Configuration File Password contains the password for the configuration file specified in Analysis Target. This input is valid only when specifying a legacy .cfg file that is password-protected. Analysis Results — Analysis Results returns the results of the VI Analyzer task. Wire this output to the Analysis Results input of the VIAn Easy Report VI. Raw Results — Raw Results contains the unparsed results data for every test and every VI in the VI Analyzer task. Test Name — Test Name displays the name of the test. Results Data — Results Data contains the unparsed results for the test specified in Test Name. Result Message — Ref Index — Status — Status indicates whether the test in Test Name passed or failed. Exceed Max Fails? — Exceed Max Fails? indicates whether the test in Test Name failed more than the maximum number of times specified for that test. Parsed Results Data (by VI) — Parsed Results Data (by VI) contains the results by VI for every test in the VI Analyzer task, including which tests passed and failed, which tests the VI Analyzer could not load or run, and which errors occurred. VI Path — VI Path contains the path to the VI for which the test results are listed. Pass — Pass contains data on the tests that passed for the VI specified in VI Path. row — column — Fail — Fail contains data on the tests that failed for the VI specified in VI Path. row — column — Skipped — Skipped contains data on the tests that the VI Analyzer skipped for the VI specified in VI Path. row — column — VI not loadable — VI not loadable contains data on whether the VI Analyzer was able to load the VI specified in VI Path. row — column — Test not loadable — Test not loadable contains data on the tests that the VI Analyzer was not able to load for the VI specified in VI Path. row — column — Test not runnable — Test not runnable contains data on the tests that the VI Analyzer was not able to run for the VI specified in VI Path. row — column — Test error out — Test error out contains data on errors that occurred when the VI Analyzer performed tests on the VI specified in VI Path. row — column — Parsed Results Data (by Test) — Parsed Results Data (by Test) contains the results of every test and whether the VI Analyzer passed, failed, or skipped the test for every VI in the VI Analyzer task. Test Name — Test Name displays the name of the test. Pass — Pass contains data on the tests that passed for the VI specified in VI Path. VI Path — VI Path contains the path to the VI for which the test results are listed. index — row — column — Fail — Fail contains data on the tests that failed for the VI specified in VI Path. VI Path — VI Path contains the path to the VI for which the test results are listed. index — row — column — Skipped — Skipped contains data on the tests that the VI Analyzer skipped for the VI specified in VI Path. VI Path — VI Path contains the path to the VI for which the test results are listed. index — row — column — Summary Statistics — Summary Statistics contains the summary for a VI Analyzer task. Passed Tests — Passed Tests indicates the total number of tests in the VI Analyzer task that passed. Failed Tests — Failed Tests indicates the total number of tests in the VI Analyzer task that failed. Skipped Tests — Skipped Tests indicates the total number of tests in the VI Analyzer task that the VI Analyzer skipped. VIs not loadable — VIs not loadable indicates the total number of VIs that the VI Analyzer could not load. Tests not loadable — Tests not loadable indicates the total number of tests that the VI Analyzer was not able to load. Tests not runnable — Tests not runnable indicates the total number of tests that the VI Analyzer was not able to run. Test error out — Test error out contains data on errors that occurred when the VI Analyzer performed tests on the VI specified in VI Path. Start Time — Start Time indicates the time when the analysis began. Total Time (s) — Total Time (s) indicates the time it took for the VI Analyzer to run the analysis. Test Config Data — Test Config Data contains the configuration settings for every test included in the VI Analyzer task. Test Name — The name of the VI Analyzer test. Config Ref — The reference to the configuration VI for the VI Analyzer test specified in Test Name. Ref Valid? — Specifies whether or not the Config Ref is a valid VI reference. Test Ranking — The ranking of the test specified in Test Name. Max Failures — The maximum allowable number of failures to return for the test specified in Test Name on each VI being tested. Test Path — The path to the test specified in Test Name. Control Values — The names and values of all configuration options of the test specified by Test Name. Control Name — Control Name specifies the name of the control in which you want to change the value. Control Value — Control Value contains the new value that you want for the control you specify in Control Name. If the value is a data type different than the control you specify in Control Name, the VI returns an error. Selected? — Indicates whether or not the test specified in Test Name will run in the current VI Analyzer task. error out — error out contains error information. This output provides standard error out functionality. |
| --- |
| Raw Results — Raw Results contains the unparsed results data for every test and every VI in the VI Analyzer task. Test Name — Test Name displays the name of the test. Results Data — Results Data contains the unparsed results for the test specified in Test Name. Result Message — Ref Index — Status — Status indicates whether the test in Test Name passed or failed. Exceed Max Fails? — Exceed Max Fails? indicates whether the test in Test Name failed more than the maximum number of times specified for that test. Parsed Results Data (by VI) — Parsed Results Data (by VI) contains the results by VI for every test in the VI Analyzer task, including which tests passed and failed, which tests the VI Analyzer could not load or run, and which errors occurred. VI Path — VI Path contains the path to the VI for which the test results are listed. Pass — Pass contains data on the tests that passed for the VI specified in VI Path. row — column — Fail — Fail contains data on the tests that failed for the VI specified in VI Path. row — column — Skipped — Skipped contains data on the tests that the VI Analyzer skipped for the VI specified in VI Path. row — column — VI not loadable — VI not loadable contains data on whether the VI Analyzer was able to load the VI specified in VI Path. row — column — Test not loadable — Test not loadable contains data on the tests that the VI Analyzer was not able to load for the VI specified in VI Path. row — column — Test not runnable — Test not runnable contains data on the tests that the VI Analyzer was not able to run for the VI specified in VI Path. row — column — Test error out — Test error out contains data on errors that occurred when the VI Analyzer performed tests on the VI specified in VI Path. row — column — Parsed Results Data (by Test) — Parsed Results Data (by Test) contains the results of every test and whether the VI Analyzer passed, failed, or skipped the test for every VI in the VI Analyzer task. Test Name — Test Name displays the name of the test. Pass — Pass contains data on the tests that passed for the VI specified in VI Path. VI Path — VI Path contains the path to the VI for which the test results are listed. index — row — column — Fail — Fail contains data on the tests that failed for the VI specified in VI Path. VI Path — VI Path contains the path to the VI for which the test results are listed. index — row — column — Skipped — Skipped contains data on the tests that the VI Analyzer skipped for the VI specified in VI Path. VI Path — VI Path contains the path to the VI for which the test results are listed. index — row — column — Summary Statistics — Summary Statistics contains the summary for a VI Analyzer task. Passed Tests — Passed Tests indicates the total number of tests in the VI Analyzer task that passed. Failed Tests — Failed Tests indicates the total number of tests in the VI Analyzer task that failed. Skipped Tests — Skipped Tests indicates the total number of tests in the VI Analyzer task that the VI Analyzer skipped. VIs not loadable — VIs not loadable indicates the total number of VIs that the VI Analyzer could not load. Tests not loadable — Tests not loadable indicates the total number of tests that the VI Analyzer was not able to load. Tests not runnable — Tests not runnable indicates the total number of tests that the VI Analyzer was not able to run. Test error out — Test error out contains data on errors that occurred when the VI Analyzer performed tests on the VI specified in VI Path. Start Time — Start Time indicates the time when the analysis began. Total Time (s) — Total Time (s) indicates the time it took for the VI Analyzer to run the analysis. Test Config Data — Test Config Data contains the configuration settings for every test included in the VI Analyzer task. Test Name — The name of the VI Analyzer test. Config Ref — The reference to the configuration VI for the VI Analyzer test specified in Test Name. Ref Valid? — Specifies whether or not the Config Ref is a valid VI reference. Test Ranking — The ranking of the test specified in Test Name. Max Failures — The maximum allowable number of failures to return for the test specified in Test Name on each VI being tested. Test Path — The path to the test specified in Test Name. Control Values — The names and values of all configuration options of the test specified by Test Name. Control Name — Control Name specifies the name of the control in which you want to change the value. Control Value — Control Value contains the new value that you want for the control you specify in Control Name. If the value is a data type different than the control you specify in Control Name, the VI returns an error. Selected? — Indicates whether or not the test specified in Test Name will run in the current VI Analyzer task. |
| Test Name — Test Name displays the name of the test. Results Data — Results Data contains the unparsed results for the test specified in Test Name. Result Message — Ref Index — Status — Status indicates whether the test in Test Name passed or failed. Exceed Max Fails? — Exceed Max Fails? indicates whether the test in Test Name failed more than the maximum number of times specified for that test. |
| Result Message — Ref Index — |
| VI Path — VI Path contains the path to the VI for which the test results are listed. Pass — Pass contains data on the tests that passed for the VI specified in VI Path. row — column — Fail — Fail contains data on the tests that failed for the VI specified in VI Path. row — column — Skipped — Skipped contains data on the tests that the VI Analyzer skipped for the VI specified in VI Path. row — column — VI not loadable — VI not loadable contains data on whether the VI Analyzer was able to load the VI specified in VI Path. row — column — Test not loadable — Test not loadable contains data on the tests that the VI Analyzer was not able to load for the VI specified in VI Path. row — column — Test not runnable — Test not runnable contains data on the tests that the VI Analyzer was not able to run for the VI specified in VI Path. row — column — Test error out — Test error out contains data on errors that occurred when the VI Analyzer performed tests on the VI specified in VI Path. row — column — |
| row — column — |
| row — column — |
| row — column — |
| row — column — |
| row — column — |
| row — column — |
| row — column — |
| Test Name — Test Name displays the name of the test. Pass — Pass contains data on the tests that passed for the VI specified in VI Path. VI Path — VI Path contains the path to the VI for which the test results are listed. index — row — column — Fail — Fail contains data on the tests that failed for the VI specified in VI Path. VI Path — VI Path contains the path to the VI for which the test results are listed. index — row — column — Skipped — Skipped contains data on the tests that the VI Analyzer skipped for the VI specified in VI Path. VI Path — VI Path contains the path to the VI for which the test results are listed. index — row — column — |
| VI Path — VI Path contains the path to the VI for which the test results are listed. index — row — column — |
| row — column — |
| VI Path — VI Path contains the path to the VI for which the test results are listed. index — row — column — |
| row — column — |
| VI Path — VI Path contains the path to the VI for which the test results are listed. index — row — column — |
| row — column — |
| Passed Tests — Passed Tests indicates the total number of tests in the VI Analyzer task that passed. Failed Tests — Failed Tests indicates the total number of tests in the VI Analyzer task that failed. Skipped Tests — Skipped Tests indicates the total number of tests in the VI Analyzer task that the VI Analyzer skipped. VIs not loadable — VIs not loadable indicates the total number of VIs that the VI Analyzer could not load. Tests not loadable — Tests not loadable indicates the total number of tests that the VI Analyzer was not able to load. Tests not runnable — Tests not runnable indicates the total number of tests that the VI Analyzer was not able to run. Test error out — Test error out contains data on errors that occurred when the VI Analyzer performed tests on the VI specified in VI Path. Start Time — Start Time indicates the time when the analysis began. Total Time (s) — Total Time (s) indicates the time it took for the VI Analyzer to run the analysis. |
| Test Name — The name of the VI Analyzer test. Config Ref — The reference to the configuration VI for the VI Analyzer test specified in Test Name. Ref Valid? — Specifies whether or not the Config Ref is a valid VI reference. Test Ranking — The ranking of the test specified in Test Name. Max Failures — The maximum allowable number of failures to return for the test specified in Test Name on each VI being tested. Test Path — The path to the test specified in Test Name. Control Values — The names and values of all configuration options of the test specified by Test Name. Control Name — Control Name specifies the name of the control in which you want to change the value. Control Value — Control Value contains the new value that you want for the control you specify in Control Name. If the value is a data type different than the control you specify in Control Name, the VI returns an error. Selected? — Indicates whether or not the test specified in Test Name will run in the current VI Analyzer task. |
| Control Name — Control Name specifies the name of the control in which you want to change the value. Control Value — Control Value contains the new value that you want for the control you specify in Control Name. If the value is a data type different than the control you specify in Control Name, the VI returns an error. |

Parent topic:

VI Analyzer

<!--NI_TOPIC bundle=lvvia-api-ref path=vi-lib/addons/analyzer/analyzerapi-llb/vian-easy-report-vi.html language=enus -->
## TOPIC 00008: VIAn Easy Report VI

- bundle_id: `lvvia-api-ref`
- source_path: `vi-lib/addons/analyzer/analyzerapi-llb/vian-easy-report-vi.html`
- source_url: https://docs-be.ni.com/bundle/lvvia-api-ref/raw/resource/enus/vi-lib/addons/analyzer/analyzerapi-llb/vian-easy-report-vi.html
- document_id: `lvvia-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Exports the results of an analysis to a file, either as a report in ASCII or HTML format or as a VI Analyzer results file. icon Inputs/Outputs cbool.png Overwrite Report? (T) Overwrite Report? specifies whether the VI overwrites a report file if the file specified in Report Save Path already exists.

### VIAn Easy Report VI

Exports the results of an analysis to a file, either as a report in ASCII or HTML format or as a VI Analyzer results file.

[IMAGE alt='icon' src='vian-easy-report-vi.png']

#### Inputs/Outputs

| Overwrite Report? (T) — Overwrite Report? specifies whether the VI overwrites a report file if the file specified in Report Save Path already exists. The default is TRUE, which overwrites the file. If Overwrite Report? is FALSE and the file exists, the VI returns an error. Report Save Path — Report Save Path contains the path to the report or results file. If the path you specify is invalid, the VI returns an error. Analysis Results — Analysis Results contains the results from a VI Analyzer task you run using either the VIAn Easy Analyze VI or the VIAn Run VI. Wire the Analysis Results output of either VI to this input. Raw Results — Raw Results contains the unparsed results data for every test and every VI in the VI Analyzer task for which you want to create a report. Test Name — Test Name contains the name of the test that the results reference. Results Data — Results Data contains the unparsed results for the test specified in Test Name. Result Message — Ref Index — Status — Status indicates whether the test in Test Name passed or failed. Exceed Max Fails? — Exceed Max Fails? indicates whether the test in Test Name failed more than the maximum number of times specified for that test. Parsed Results Data (by VI) — Parsed Results Data (by VI) contains the results by VI for every test in the VI Analyzer task, including which tests passed and failed, which tests the VI Analyzer could not load or run, and which errors occurred. VI Path — VI Path contains the path to the VI for which the test results are listed. Pass — Pass contains data on the tests that passed for the VI specified in VI Path. row — column — Fail — Fail contains data on the tests that failed for the VI specified in VI Path. row — column — Skipped — Skipped contains data on the tests the VI Analyzer skipped for the VI specified in VI Path. row — column — VI not loadable — VI not loadable contains data on whether the VI Analyzer was able to load the VI specified in VI Path. row — column — Test not loadable — Test not loadable contains data on the tests that the VI Analyzer was not able to load for the VI specified in VI Path. row — column — Test not runnable — Test not runnable contains data on the tests that the VI Analyzer was not able to run for the VI specified in VI Path. row — column — Test error out — Test error out contains data on errors that occurred when the VI Analyzer performed tests on the VI specified in VI Path. row — column — Parsed Results Data (by Test) — Parsed Results Data (by Test) contains the results of every test and whether the VI Analyzer passed, failed, or skipped the test for every VI in the VI Analyzer task. Test Name — Test Name contains the name of the test that the results reference. Pass — Pass contains data on the tests that passed for the VI specified in VI Path. VI Path — VI Path contains the path to the VI for which the test results are listed. index — row — column — Fail — Fail contains data on the tests that failed for the VI specified in VI Path. VI Path — VI Path contains the path to the VI for which the test results are listed. index — row — column — Skipped — Skipped contains data on the tests the VI Analyzer skipped for the VI specified in VI Path. VI Path — VI Path contains the path to the VI for which the test results are listed. index — row — column — Summary Statistics — Summary Statistics contains the summary for a VI Analyzer task on how many tests passed, failed, or were skipped; how many VIs and tests the VI Analyzer could not load or run; the total number of test errors; and the start time and elapsed time of the analysis. Passed Tests — Passed Tests contains the total number of tests in the VI Analyzer task that passed. Failed Tests — Failed Tests contains the total number of tests in the VI Analyzer task that failed. Skipped Tests — Skipped Tests contains the total number of tests in the VI Analyzer task that the VI Analyzer skipped. VIs not loadable — VIs not loadable contains the total number of VIs that the VI Analyzer could not load. Tests not loadable — Tests not loadable contains the total number of tests that the VI Analyzer was not able to load. Tests not runnable — Tests not runnable indicates the total number of tests that the VI Analyzer was not able to run. Test error out — Test error out contains data on errors that occurred when the VI Analyzer performed tests on the VI specified in VI Path. Start Time — Start Time contains the time when the analysis began. Total Time (s) — Total Times (s) contains the time it took for the VI Analyzer to run the analysis. Test Config Data — Test Config Data contains the configuration settings for every test included in the VI Analyzer task. Test Name — The name of the VI Analyzer test. Config Ref — The reference to the configuration VI for the VI Analyzer test specified in Test Name. Ref Valid? — Specifies whether or not the Config Ref is a valid VI reference. Test Ranking — The ranking of the test specified in Test Name. Max Failures — The maximum allowable number of failures to return for the test specified in Test Name on each VI being tested. Test Path — The path to the test specified in Test Name. Control Values — The names and values of all configuration options of the test specified by Test Name. Control Name — Control Name specifies the name of the control in which you want to change the value. Control Value — Control Value contains the new value that you want for the control you specify in Control Name. If the value is a data type different than the control you specify in Control Name, the VI returns an error. Selected? — Indicates whether or not the test specified in Test Name will run in the current VI Analyzer task. Report Save Type (ASCII) — Report Save Type determines whether the VI saves the results to a tab-delimited ASCII file, an HTML file, or a VI Analyzer results file (.rsl). The default is an ASCII file. If you select RSL File, the VI saves the report data to a VI Analyzer results file that you can load into the VI Analyzer Results Window. error in (no error) — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. Export Options (Summary, Fails, Errs) — Export Options specifies the sections of the analysis results to include in the report. The default selects the Summary Data, Failed Tests, and Errors options. If you set Report Save Type to RSL File, the VI ignores this input. Summary Data — Summary Data specifies whether you want to include the Summary Data section of the analysis in the report. The default is TRUE, which includes the section. Failed Tests — Failed Tests specifies whether you want to include the Failed Tests section of the analysis in the report. The default is TRUE, which includes the section. Passed Tests — Passed Tests specifies whether you want to include the Passed Tests section of the analysis in the report. The default is FALSE, which does not include the section. Skipped Tests — Skipped Tests specifies whether you want to include the Skipped Tests section of the analysis in the report. The default is FALSE, which does not include the section. Errors — Errors specifies whether you want to include the Errors section of the analysis in the report. The default is TRUE, which includes the section. Sort Type (VI) — Sort Type determines whether to sort the report results by VI or by test. The default sorts the results by VI. If you set Report Save Type to RSL File, the VI ignores this input. error out — error out contains error information. This output provides standard error out functionality. |
| --- |
| Raw Results — Raw Results contains the unparsed results data for every test and every VI in the VI Analyzer task for which you want to create a report. Test Name — Test Name contains the name of the test that the results reference. Results Data — Results Data contains the unparsed results for the test specified in Test Name. Result Message — Ref Index — Status — Status indicates whether the test in Test Name passed or failed. Exceed Max Fails? — Exceed Max Fails? indicates whether the test in Test Name failed more than the maximum number of times specified for that test. Parsed Results Data (by VI) — Parsed Results Data (by VI) contains the results by VI for every test in the VI Analyzer task, including which tests passed and failed, which tests the VI Analyzer could not load or run, and which errors occurred. VI Path — VI Path contains the path to the VI for which the test results are listed. Pass — Pass contains data on the tests that passed for the VI specified in VI Path. row — column — Fail — Fail contains data on the tests that failed for the VI specified in VI Path. row — column — Skipped — Skipped contains data on the tests the VI Analyzer skipped for the VI specified in VI Path. row — column — VI not loadable — VI not loadable contains data on whether the VI Analyzer was able to load the VI specified in VI Path. row — column — Test not loadable — Test not loadable contains data on the tests that the VI Analyzer was not able to load for the VI specified in VI Path. row — column — Test not runnable — Test not runnable contains data on the tests that the VI Analyzer was not able to run for the VI specified in VI Path. row — column — Test error out — Test error out contains data on errors that occurred when the VI Analyzer performed tests on the VI specified in VI Path. row — column — Parsed Results Data (by Test) — Parsed Results Data (by Test) contains the results of every test and whether the VI Analyzer passed, failed, or skipped the test for every VI in the VI Analyzer task. Test Name — Test Name contains the name of the test that the results reference. Pass — Pass contains data on the tests that passed for the VI specified in VI Path. VI Path — VI Path contains the path to the VI for which the test results are listed. index — row — column — Fail — Fail contains data on the tests that failed for the VI specified in VI Path. VI Path — VI Path contains the path to the VI for which the test results are listed. index — row — column — Skipped — Skipped contains data on the tests the VI Analyzer skipped for the VI specified in VI Path. VI Path — VI Path contains the path to the VI for which the test results are listed. index — row — column — Summary Statistics — Summary Statistics contains the summary for a VI Analyzer task on how many tests passed, failed, or were skipped; how many VIs and tests the VI Analyzer could not load or run; the total number of test errors; and the start time and elapsed time of the analysis. Passed Tests — Passed Tests contains the total number of tests in the VI Analyzer task that passed. Failed Tests — Failed Tests contains the total number of tests in the VI Analyzer task that failed. Skipped Tests — Skipped Tests contains the total number of tests in the VI Analyzer task that the VI Analyzer skipped. VIs not loadable — VIs not loadable contains the total number of VIs that the VI Analyzer could not load. Tests not loadable — Tests not loadable contains the total number of tests that the VI Analyzer was not able to load. Tests not runnable — Tests not runnable indicates the total number of tests that the VI Analyzer was not able to run. Test error out — Test error out contains data on errors that occurred when the VI Analyzer performed tests on the VI specified in VI Path. Start Time — Start Time contains the time when the analysis began. Total Time (s) — Total Times (s) contains the time it took for the VI Analyzer to run the analysis. Test Config Data — Test Config Data contains the configuration settings for every test included in the VI Analyzer task. Test Name — The name of the VI Analyzer test. Config Ref — The reference to the configuration VI for the VI Analyzer test specified in Test Name. Ref Valid? — Specifies whether or not the Config Ref is a valid VI reference. Test Ranking — The ranking of the test specified in Test Name. Max Failures — The maximum allowable number of failures to return for the test specified in Test Name on each VI being tested. Test Path — The path to the test specified in Test Name. Control Values — The names and values of all configuration options of the test specified by Test Name. Control Name — Control Name specifies the name of the control in which you want to change the value. Control Value — Control Value contains the new value that you want for the control you specify in Control Name. If the value is a data type different than the control you specify in Control Name, the VI returns an error. Selected? — Indicates whether or not the test specified in Test Name will run in the current VI Analyzer task. |
| Test Name — Test Name contains the name of the test that the results reference. Results Data — Results Data contains the unparsed results for the test specified in Test Name. Result Message — Ref Index — Status — Status indicates whether the test in Test Name passed or failed. Exceed Max Fails? — Exceed Max Fails? indicates whether the test in Test Name failed more than the maximum number of times specified for that test. |
| Result Message — Ref Index — |
| VI Path — VI Path contains the path to the VI for which the test results are listed. Pass — Pass contains data on the tests that passed for the VI specified in VI Path. row — column — Fail — Fail contains data on the tests that failed for the VI specified in VI Path. row — column — Skipped — Skipped contains data on the tests the VI Analyzer skipped for the VI specified in VI Path. row — column — VI not loadable — VI not loadable contains data on whether the VI Analyzer was able to load the VI specified in VI Path. row — column — Test not loadable — Test not loadable contains data on the tests that the VI Analyzer was not able to load for the VI specified in VI Path. row — column — Test not runnable — Test not runnable contains data on the tests that the VI Analyzer was not able to run for the VI specified in VI Path. row — column — Test error out — Test error out contains data on errors that occurred when the VI Analyzer performed tests on the VI specified in VI Path. row — column — |
| row — column — |
| row — column — |
| row — column — |
| row — column — |
| row — column — |
| row — column — |
| row — column — |
| Test Name — Test Name contains the name of the test that the results reference. Pass — Pass contains data on the tests that passed for the VI specified in VI Path. VI Path — VI Path contains the path to the VI for which the test results are listed. index — row — column — Fail — Fail contains data on the tests that failed for the VI specified in VI Path. VI Path — VI Path contains the path to the VI for which the test results are listed. index — row — column — Skipped — Skipped contains data on the tests the VI Analyzer skipped for the VI specified in VI Path. VI Path — VI Path contains the path to the VI for which the test results are listed. index — row — column — |
| VI Path — VI Path contains the path to the VI for which the test results are listed. index — row — column — |
| row — column — |
| VI Path — VI Path contains the path to the VI for which the test results are listed. index — row — column — |
| row — column — |
| VI Path — VI Path contains the path to the VI for which the test results are listed. index — row — column — |
| row — column — |
| Passed Tests — Passed Tests contains the total number of tests in the VI Analyzer task that passed. Failed Tests — Failed Tests contains the total number of tests in the VI Analyzer task that failed. Skipped Tests — Skipped Tests contains the total number of tests in the VI Analyzer task that the VI Analyzer skipped. VIs not loadable — VIs not loadable contains the total number of VIs that the VI Analyzer could not load. Tests not loadable — Tests not loadable contains the total number of tests that the VI Analyzer was not able to load. Tests not runnable — Tests not runnable indicates the total number of tests that the VI Analyzer was not able to run. Test error out — Test error out contains data on errors that occurred when the VI Analyzer performed tests on the VI specified in VI Path. Start Time — Start Time contains the time when the analysis began. Total Time (s) — Total Times (s) contains the time it took for the VI Analyzer to run the analysis. |
| Test Name — The name of the VI Analyzer test. Config Ref — The reference to the configuration VI for the VI Analyzer test specified in Test Name. Ref Valid? — Specifies whether or not the Config Ref is a valid VI reference. Test Ranking — The ranking of the test specified in Test Name. Max Failures — The maximum allowable number of failures to return for the test specified in Test Name on each VI being tested. Test Path — The path to the test specified in Test Name. Control Values — The names and values of all configuration options of the test specified by Test Name. Control Name — Control Name specifies the name of the control in which you want to change the value. Control Value — Control Value contains the new value that you want for the control you specify in Control Name. If the value is a data type different than the control you specify in Control Name, the VI returns an error. Selected? — Indicates whether or not the test specified in Test Name will run in the current VI Analyzer task. |
| Control Name — Control Name specifies the name of the control in which you want to change the value. Control Value — Control Value contains the new value that you want for the control you specify in Control Name. If the value is a data type different than the control you specify in Control Name, the VI returns an error. |
| Summary Data — Summary Data specifies whether you want to include the Summary Data section of the analysis in the report. The default is TRUE, which includes the section. Failed Tests — Failed Tests specifies whether you want to include the Failed Tests section of the analysis in the report. The default is TRUE, which includes the section. Passed Tests — Passed Tests specifies whether you want to include the Passed Tests section of the analysis in the report. The default is FALSE, which does not include the section. Skipped Tests — Skipped Tests specifies whether you want to include the Skipped Tests section of the analysis in the report. The default is FALSE, which does not include the section. Errors — Errors specifies whether you want to include the Errors section of the analysis in the report. The default is TRUE, which includes the section. |

Parent topic:

VI Analyzer

<!--NI_TOPIC bundle=lvvia-api-ref path=vi-lib/addons/analyzer/analyzerapi-llb/vian-exclude-tests-from-vi-vi.html language=enus -->
## TOPIC 00009: VIAn Exclude Tests from VI VI

- bundle_id: `lvvia-api-ref`
- source_path: `vi-lib/addons/analyzer/analyzerapi-llb/vian-exclude-tests-from-vi-vi.html`
- source_url: https://docs-be.ni.com/bundle/lvvia-api-ref/raw/resource/enus/vi-lib/addons/analyzer/analyzerapi-llb/vian-exclude-tests-from-vi-vi.html
- document_id: `lvvia-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the tests to exclude for a specific VI in the VI Analyzer task. icon Inputs/Outputs cdlrn.png VI Analyzer Task in VI Analyzer Task in contains a reference to the current task. The VI Analyzer task must be a valid task that you created using the VIAn New Task VI. cpath.png VI VI specifies t

### VIAn Exclude Tests from VI VI

Specifies the tests to exclude for a specific VI in the VI Analyzer task.

[IMAGE alt='icon' src='vian-exclude-tests-from-vi-vi.png']

#### Inputs/Outputs

| VI Analyzer Task in — VI Analyzer Task in contains a reference to the current task. The VI Analyzer task must be a valid task that you created using the VIAn New Task VI. VI — VI specifies the path to the VI you want to exclude from certain tests. If the VI is not included in the VI Analyzer task, or if the path you specify is empty or invalid, an error occurs. error in (no error) — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. Tests to Exclude — Tests to Exclude contains the names of the tests that you want to exclude from the VI specified in VI. You can wire the Test Names output of the VIAn Get Tests VI to this input. If you specify an invalid test name, an error occurs. VI Analyzer Task out — VI Analyzer Task out returns a reference to the VI Analyzer task specified in VI Analyzer Task in. error out — error out contains error information. This output provides standard error out functionality. |
| --- |

Parent topic:

VI Analyzer Utilities

<!--NI_TOPIC bundle=lvvia-api-ref path=vi-lib/addons/analyzer/analyzerapi-llb/vian-get-analysis-status-vi.html language=enus -->
## TOPIC 00010: VIAn Get Analysis Status VI

- bundle_id: `lvvia-api-ref`
- source_path: `vi-lib/addons/analyzer/analyzerapi-llb/vian-get-analysis-status-vi.html`
- source_url: https://docs-be.ni.com/bundle/lvvia-api-ref/raw/resource/enus/vi-lib/addons/analyzer/analyzerapi-llb/vian-get-analysis-status-vi.html
- document_id: `lvvia-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Monitors the progress of the analysis. icon Inputs/Outputs cdlrn.png VI Analyzer Task in VI Analyzer Task in contains a reference to the current task. The VI Analyzer task must be a valid task that you created using the VIAn New Task VI. cerrcodeclst.png error in (no error) error in describes error

### VIAn Get Analysis Status VI

Monitors the progress of the analysis.

[IMAGE alt='icon' src='vian-get-analysis-status-vi.png']

#### Inputs/Outputs

| VI Analyzer Task in — VI Analyzer Task in contains a reference to the current task. The VI Analyzer task must be a valid task that you created using the VIAn New Task VI. error in (no error) — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. Abort Analysis (F) — Abort Analysis specifies whether to abort the analysis process. The default is FALSE. If you call this VI in a loop structure, you can wire a value of TRUE to this input to abort an analysis that is currently running. VI Analyzer Task out — VI Analyzer Task out returns a reference to the VI Analyzer task specified in VI Analyzer Task in. Percent Complete — Percent Complete represents the percentage of the task that has completed. Values range from 0 to 100. VI in Analysis — VI in Analysis displays the name of the VI being analyzed. error out — error out contains error information. This output provides standard error out functionality. |
| --- |

Parent topic:

VI Analyzer Utilities

<!--NI_TOPIC bundle=lvvia-api-ref path=vi-lib/addons/analyzer/analyzerapi-llb/vian-get-items-vi.html language=enus -->
## TOPIC 00011: VIAn Get Items VI

- bundle_id: `lvvia-api-ref`
- source_path: `vi-lib/addons/analyzer/analyzerapi-llb/vian-get-items-vi.html`
- source_url: https://docs-be.ni.com/bundle/lvvia-api-ref/raw/resource/enus/vi-lib/addons/analyzer/analyzerapi-llb/vian-get-items-vi.html
- document_id: `lvvia-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns a list of all top-level VIs, folders, or LLBs in the VI Analyzer task. icon Inputs/Outputs cdlrn.png VI Analyzer Task in VI Analyzer Task in contains a reference to the current task. The VI Analyzer task must be a valid task that you created using the VIAn New Task VI. cerrcodeclst.png error

### VIAn Get Items VI

Returns a list of all top-level VIs, folders, or LLBs in the VI Analyzer task.

[IMAGE alt='icon' src='vian-get-items-vi.png']

#### Inputs/Outputs

| VI Analyzer Task in — VI Analyzer Task in contains a reference to the current task. The VI Analyzer task must be a valid task that you created using the VIAn New Task VI. error in (no error) — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. VI Analyzer Task out — VI Analyzer Task out returns a reference to the VI Analyzer task specified in VI Analyzer Task in. Items — Items returns the paths of all top-level VIs, folders, or LLBs that the VI Analyzer task includes. error out — error out contains error information. This output provides standard error out functionality. |
| --- |

Parent topic:

VI Analyzer Utilities

<!--NI_TOPIC bundle=lvvia-api-ref path=vi-lib/addons/analyzer/analyzerapi-llb/vian-get-tests-vi.html language=enus -->
## TOPIC 00012: VIAn Get Tests VI

- bundle_id: `lvvia-api-ref`
- source_path: `vi-lib/addons/analyzer/analyzerapi-llb/vian-get-tests-vi.html`
- source_url: https://docs-be.ni.com/bundle/lvvia-api-ref/raw/resource/enus/vi-lib/addons/analyzer/analyzerapi-llb/vian-get-tests-vi.html
- document_id: `lvvia-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns a cluster array containing the configuration information for each test in the VI Analyzer task. icon Inputs/Outputs cdlrn.png VI Analyzer Task in VI Analyzer Task in contains a reference to the current task. The VI Analyzer task must be a valid task that you created using the VIAn New Task V

### VIAn Get Tests VI

Returns a cluster array containing the configuration information for each test in the VI Analyzer task.

[IMAGE alt='icon' src='vian-get-tests-vi.png']

#### Inputs/Outputs

| VI Analyzer Task in — VI Analyzer Task in contains a reference to the current task. The VI Analyzer task must be a valid task that you created using the VIAn New Task VI. error in (no error) — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. VI Analyzer Task out — VI Analyzer Task out returns a reference to the VI Analyzer task specified in VI Analyzer Task in. Test Names — Test Names contains the names of the tests that the VI Analyzer task includes. Test Configurations — Test Configurations contains an array of clusters in which each cluster represents the configuration options for a specific test. Test Ranking — Test Ranking displays the rank of the test as Low, Normal, or High. High-ranking tests involve issues that have a significant impact on performance. Low-ranking tests involve minor style or cosmetic issues that do not significantly affect VI performance. Max Failures — Max Failures displays the maximum number of failed results the VI Analyzer can report for a specific test on a single VI. Control Values — Control Values displays the names and values of the controls that you use to configure the test. Control Name — Control Name specifies the name of the control in which you want to change the value. Control Value — Control Value contains the new value that you want for the control you specify in Control Name. If the value is a data type different than the control you specify in Control Name, the VI returns an error. Run Test? — Run Test? indicates whether you set the test to run. error out — error out contains error information. This output provides standard error out functionality. Test Descriptions — |
| --- |
| Test Ranking — Test Ranking displays the rank of the test as Low, Normal, or High. High-ranking tests involve issues that have a significant impact on performance. Low-ranking tests involve minor style or cosmetic issues that do not significantly affect VI performance. Max Failures — Max Failures displays the maximum number of failed results the VI Analyzer can report for a specific test on a single VI. Control Values — Control Values displays the names and values of the controls that you use to configure the test. Control Name — Control Name specifies the name of the control in which you want to change the value. Control Value — Control Value contains the new value that you want for the control you specify in Control Name. If the value is a data type different than the control you specify in Control Name, the VI returns an error. Run Test? — Run Test? indicates whether you set the test to run. |
| Control Name — Control Name specifies the name of the control in which you want to change the value. Control Value — Control Value contains the new value that you want for the control you specify in Control Name. If the value is a data type different than the control you specify in Control Name, the VI returns an error. |

Parent topic:

VI Analyzer Utilities

<!--NI_TOPIC bundle=lvvia-api-ref path=vi-lib/addons/analyzer/analyzerapi-llb/vian-modify-test-config-value-vi.html language=enus -->
## TOPIC 00013: VIAn Modify Test Config Value VI

- bundle_id: `lvvia-api-ref`
- source_path: `vi-lib/addons/analyzer/analyzerapi-llb/vian-modify-test-config-value-vi.html`
- source_url: https://docs-be.ni.com/bundle/lvvia-api-ref/raw/resource/enus/vi-lib/addons/analyzer/analyzerapi-llb/vian-modify-test-config-value-vi.html
- document_id: `lvvia-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Modifies the value of a single configuration option for a specific test. icon Inputs/Outputs cdlrn.png VI Analyzer Task in VI Analyzer Task in contains a reference to the current task. The VI Analyzer task must be a valid task that you created using the VIAn New Task VI. cstr.png Test Name Test Name

### VIAn Modify Test Config Value VI

Modifies the value of a single configuration option for a specific test.

[IMAGE alt='icon' src='vian-modify-test-config-value-vi.png']

#### Inputs/Outputs

| VI Analyzer Task in — VI Analyzer Task in contains a reference to the current task. The VI Analyzer task must be a valid task that you created using the VIAn New Task VI. Test Name — Test Name specifies the name of the test you want to modify. If you specify an invalid test name, the VI returns an error. Control Name — Control Name specifies the name of the control in which you want to change the value. The Control Values output in the Test Configurations indicator of the VIAn Get Tests VI returns a list of valid control names for the test you specify. If you do not specify a valid control name, the VI returns an error. error in (no error) — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. Control Value — Control Value contains the new value that you want for the control you specify in Control Name. If the value is a data type different than the control you specify in Control Name, the VI returns an error. Most controls in VI Analyzer tests are Boolean or numeric data types. Numeric controls in VI Analyzer tests are signed 32-bit integer numeric data types. The following table shows the tests that include control values that are not Boolean or numeric data types. Test Name Data Type Exceptions VI Name The Include Expressions and Exclude Expressions controls are strings. SubVI and TypeDef Locations The User Paths control is a one-dimensional array of paths. Connector Pane Pattern The Patterns control is a one-dimensional array of strings. Terminal Connection Type The Pattern and Type control is a two-dimensional array of strings. Terminal Positions The Pattern and Position control is a two-dimensional array of strings. VI Analyzer Task out — VI Analyzer Task out returns a reference to the VI Analyzer task specified in VI Analyzer Task in. error out — error out contains error information. This output provides standard error out functionality. |  |
| --- | --- |
| Test Name | Data Type Exceptions |
| VI Name | The Include Expressions and Exclude Expressions controls are strings. |
| SubVI and TypeDef Locations | The User Paths control is a one-dimensional array of paths. |
| Connector Pane Pattern | The Patterns control is a one-dimensional array of strings. |
| Terminal Connection Type | The Pattern and Type control is a two-dimensional array of strings. |
| Terminal Positions | The Pattern and Position control is a two-dimensional array of strings. |

Parent topic:

VI Analyzer Utilities

<!--NI_TOPIC bundle=lvvia-api-ref path=vi-lib/addons/analyzer/analyzerapi-llb/vian-modify-test-settings-vi.html language=enus -->
## TOPIC 00014: VIAn Modify Test Settings VI

- bundle_id: `lvvia-api-ref`
- source_path: `vi-lib/addons/analyzer/analyzerapi-llb/vian-modify-test-settings-vi.html`
- source_url: https://docs-be.ni.com/bundle/lvvia-api-ref/raw/resource/enus/vi-lib/addons/analyzer/analyzerapi-llb/vian-modify-test-settings-vi.html
- document_id: `lvvia-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Modifies the configuration settings of a single test. icon Inputs/Outputs cdlrn.png VI Analyzer Task in VI Analyzer Task in contains a reference to the current task. The VI Analyzer task must be a valid task that you created using the VIAn New Task VI. cstr.png Test Name Test Name specifies the name

### VIAn Modify Test Settings VI

Modifies the configuration settings of a single test.

[IMAGE alt='icon' src='vian-modify-test-settings-vi.png']

#### Inputs/Outputs

| VI Analyzer Task in — VI Analyzer Task in contains a reference to the current task. The VI Analyzer task must be a valid task that you created using the VIAn New Task VI. Test Name — Test Name specifies the name of the test you want to modify. If you specify an invalid test name, the VI returns an error. New Test Info — New Test Info contains the configuration settings to modify. Test Ranking — Test Ranking displays the rank of the test as Low, Normal, or High. The default is Normal. High-ranking tests involve issues that have a significant impact on performance. Low-ranking tests involve minor style or cosmetic issues that do not significantly affect VI performance. Max Failures — Max Failures specifies the maximum number of failed results you want to report for the test on a single VI. The default is 5. Control Values — Control Values lists the names and values of the controls you can modify for a specific test. Control Name — Control Name specifies the name of the control in which you want to change the value. The Control Values output in the Test Configurations indicator of the VIAn Get Tests VI returns a list of valid control names for the test you specify. If you do not specify a valid control name, the VI returns an error. Control Value — Control Value contains the new value that you want for the control you specify in Control Name. If the value is a data type different than the control you specify in Control Name, the VI returns an error. Most controls in VI Analyzer tests are Boolean or numeric data types. Numeric controls in VI Analyzer tests are signed 32-bit integer numeric data types. The following table shows the tests that include control values that are not Boolean or numeric data types. Test Name Data Type Exceptions VI Name The Include Expressions and Exclude Expressions controls are strings. SubVI and TypeDef Locations The User Paths control is a one-dimensional array of paths. Connector Pane Pattern The Patterns control is a one-dimensional array of strings. Terminal Connection Type The Pattern and Type control is a two-dimensional array of strings. Terminal Positions The Pattern and Position control is a two-dimensional array of strings. Run Test? — Run Test? specifies whether you want the test to run. The default is FALSE, which does not run the test. error in (no error) — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. VI Analyzer Task out — VI Analyzer Task out returns a reference to the VI Analyzer task specified in VI Analyzer Task in. error out — error out contains error information. This output provides standard error out functionality. |  |
| --- | --- |
| Test Ranking — Test Ranking displays the rank of the test as Low, Normal, or High. The default is Normal. High-ranking tests involve issues that have a significant impact on performance. Low-ranking tests involve minor style or cosmetic issues that do not significantly affect VI performance. Max Failures — Max Failures specifies the maximum number of failed results you want to report for the test on a single VI. The default is 5. Control Values — Control Values lists the names and values of the controls you can modify for a specific test. Control Name — Control Name specifies the name of the control in which you want to change the value. The Control Values output in the Test Configurations indicator of the VIAn Get Tests VI returns a list of valid control names for the test you specify. If you do not specify a valid control name, the VI returns an error. Control Value — Control Value contains the new value that you want for the control you specify in Control Name. If the value is a data type different than the control you specify in Control Name, the VI returns an error. Most controls in VI Analyzer tests are Boolean or numeric data types. Numeric controls in VI Analyzer tests are signed 32-bit integer numeric data types. The following table shows the tests that include control values that are not Boolean or numeric data types. Test Name Data Type Exceptions VI Name The Include Expressions and Exclude Expressions controls are strings. SubVI and TypeDef Locations The User Paths control is a one-dimensional array of paths. Connector Pane Pattern The Patterns control is a one-dimensional array of strings. Terminal Connection Type The Pattern and Type control is a two-dimensional array of strings. Terminal Positions The Pattern and Position control is a two-dimensional array of strings. Run Test? — Run Test? specifies whether you want the test to run. The default is FALSE, which does not run the test. |  |
| Control Name — Control Name specifies the name of the control in which you want to change the value. The Control Values output in the Test Configurations indicator of the VIAn Get Tests VI returns a list of valid control names for the test you specify. If you do not specify a valid control name, the VI returns an error. Control Value — Control Value contains the new value that you want for the control you specify in Control Name. If the value is a data type different than the control you specify in Control Name, the VI returns an error. Most controls in VI Analyzer tests are Boolean or numeric data types. Numeric controls in VI Analyzer tests are signed 32-bit integer numeric data types. The following table shows the tests that include control values that are not Boolean or numeric data types. Test Name Data Type Exceptions VI Name The Include Expressions and Exclude Expressions controls are strings. SubVI and TypeDef Locations The User Paths control is a one-dimensional array of paths. Connector Pane Pattern The Patterns control is a one-dimensional array of strings. Terminal Connection Type The Pattern and Type control is a two-dimensional array of strings. Terminal Positions The Pattern and Position control is a two-dimensional array of strings. |  |
| Test Name | Data Type Exceptions |
| VI Name | The Include Expressions and Exclude Expressions controls are strings. |
| SubVI and TypeDef Locations | The User Paths control is a one-dimensional array of paths. |
| Connector Pane Pattern | The Patterns control is a one-dimensional array of strings. |
| Terminal Connection Type | The Pattern and Type control is a two-dimensional array of strings. |
| Terminal Positions | The Pattern and Position control is a two-dimensional array of strings. |

Parent topic:

VI Analyzer Utilities

<!--NI_TOPIC bundle=lvvia-api-ref path=vi-lib/addons/analyzer/analyzerapi-llb/vian-new-task-vi.html language=enus -->
## TOPIC 00015: VIAn New Task VI

- bundle_id: `lvvia-api-ref`
- source_path: `vi-lib/addons/analyzer/analyzerapi-llb/vian-new-task-vi.html`
- source_url: https://docs-be.ni.com/bundle/lvvia-api-ref/raw/resource/enus/vi-lib/addons/analyzer/analyzerapi-llb/vian-new-task-vi.html
- document_id: `lvvia-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Creates a VI Analyzer task, which you can use with other VI Analyzer VIs to configure and run an analysis. icon Inputs/Outputs cpath.png Path to Configuration File Path to Configuration File specifies the path to the configuration file containing the VI Analyzer task settings you want to use. If you

### VIAn New Task VI

Creates a VI Analyzer task, which you can use with other VI Analyzer VIs to configure and run an analysis.

[IMAGE alt='icon' src='vian-new-task-vi.png']

#### Inputs/Outputs

| Path to Configuration File — Path to Configuration File specifies the path to the configuration file containing the VI Analyzer task settings you want to use. If you do not specify a path, the VI creates an empty VI Analyzer task. error in (no error) — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. Configuration File Password — Configuration File Password contains the password for the configuration file specified in Path to Configuration File. This input is valid only when specifying a legacy .cfg file that is password-protected. Select All Tests? (T) — Select All Tests? specifies whether to select all VI Analyzer tests to run in the VI Analyzer task. The default is TRUE, which selects all the tests. The VI ignores this input if you specify a configuration file in Path to Configuration File. VI Analyzer Task — VI Analyzer Task out returns a reference to the new VI Analyzer task. Wire this output to the VI Analyzer Task in input of a VI Analyzer VI. error out — error out contains error information. This output provides standard error out functionality. |
| --- |

Parent topic:

VI Analyzer

<!--NI_TOPIC bundle=lvvia-api-ref path=vi-lib/addons/analyzer/analyzerapi-llb/vian-remove-item-vi.html language=enus -->
## TOPIC 00016: VIAn Remove Item VI

- bundle_id: `lvvia-api-ref`
- source_path: `vi-lib/addons/analyzer/analyzerapi-llb/vian-remove-item-vi.html`
- source_url: https://docs-be.ni.com/bundle/lvvia-api-ref/raw/resource/enus/vi-lib/addons/analyzer/analyzerapi-llb/vian-remove-item-vi.html
- document_id: `lvvia-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Removes an item, such as a VI, LLB, or folder, or excludes a subitem, such as a VI within an LLB or folder, from the VI Analyzer task. icon Inputs/Outputs cdlrn.png VI Analyzer Task in VI Analyzer Task in contains a reference to the current task. The VI Analyzer task must be a valid task that you cr

### VIAn Remove Item VI

Removes an item, such as a VI, LLB, or folder, or excludes a subitem, such as a VI within an LLB or folder, from the VI Analyzer task.

[IMAGE alt='icon' src='vian-remove-item-vi.png']

#### Inputs/Outputs

| VI Analyzer Task in — VI Analyzer Task in contains a reference to the current task. The VI Analyzer task must be a valid task that you created using the VIAn New Task VI. Item to Remove — Item to Remove specifies the VI, folder, or LLB that you want to remove from the VI Analyzer task. If you specify a top-level item, the VI removes the item and all its subitems. If you specify a subitem, the VI excludes the subitem but includes other subitems within the top-level item. error in (no error) — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. VI Analyzer Task out — VI Analyzer Task out returns a reference to the VI Analyzer task specified in VI Analyzer Task in. error out — error out contains error information. This output provides standard error out functionality. |
| --- |

Parent topic:

VI Analyzer Utilities

<!--NI_TOPIC bundle=lvvia-api-ref path=vi-lib/addons/analyzer/analyzerapi-llb/vian-run-vi.html language=enus -->
## TOPIC 00017: VIAn Run VI

- bundle_id: `lvvia-api-ref`
- source_path: `vi-lib/addons/analyzer/analyzerapi-llb/vian-run-vi.html`
- source_url: https://docs-be.ni.com/bundle/lvvia-api-ref/raw/resource/enus/vi-lib/addons/analyzer/analyzerapi-llb/vian-run-vi.html
- document_id: `lvvia-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Analyzes VIs using the settings that VI Analyzer Task in specifies. You can wire the results to the VIAn Easy Report VI. icon Inputs/Outputs cdlrn.png VI Analyzer Task in VI Analyzer Task in contains a reference to the current task. The VI Analyzer task must be a valid task that you created using th

### VIAn Run VI

Analyzes VIs using the settings that **VI Analyzer Task in** specifies. You can wire the results to the VIAn Easy Report VI.

[IMAGE alt='icon' src='vian-run-vi.png']

#### Inputs/Outputs

| VI Analyzer Task in — VI Analyzer Task in contains a reference to the current task. The VI Analyzer task must be a valid task that you created using the VIAn New Task VI. error in (no error) — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. Show Results Window? — Show Results Window? (F) specifies whether to show the VI Analyzer Results Window after the VI completes execution. VIs Tested — VIs Tested returns an array of paths to every VI analyzed. Tests Run — Tests Run returns an array of strings containing the names of all the tests run in the analysis. VI Analyzer Task out — VI Analyzer Task out returns a reference to the VI Analyzer task specified in VI Analyzer Task in. Analysis Results — Analysis Results returns the results of the VI Analyzer task. Wire this output to the Analysis Results input of the VIAn Easy Report VI. Raw Results — Raw Results contains the unparsed results data for every test and every VI in the VI Analyzer task. Test Name — Test Name displays the name of the test. Results Data — Results Data contains the unparsed results for the test specified in Test Name. Result Message — Ref Index — Status — Status indicates whether the test in Test Name passed or failed. Exceed Max Fails? — Exceed Max Fails? indicates whether the test in Test Name failed more than the maximum number of times specified for that test. Parsed Results Data (by VI) — Parsed Results Data (by VI) contains the results by VI for every test in the VI Analyzer task, including which tests passed and failed, which tests the VI Analyzer could not load or run, and which errors occurred. VI Path — VI Path contains the path to the VI for which the test results are listed. Pass — Pass contains data on the tests that passed for the VI specified in VI Path. row — column — Fail — Fail contains data on the tests that failed for the VI specified in VI Path. row — column — Skipped — Skipped contains data on the tests that the VI Analyzer skipped for the VI specified in VI Path. row — column — VI not loadable — VI not loadable contains data on whether the VI Analyzer was able to load the VI specified in VI Path. row — column — Test not loadable — Test not loadable contains data on the tests that the VI Analyzer was not able to load for the VI specified in VI Path. row — column — Test not runnable — Test not runnable contains data on the tests that the VI Analyzer was not able to run for the VI specified in VI Path. row — column — Test error out — Test error out contains data on errors that occurred when the VI Analyzer performed tests on the VI specified in VI Path. row — column — Parsed Results Data (by Test) — Parsed Results Data (by Test) contains the results of every test and whether the VI Analyzer passed, failed, or skipped the test for every VI in the VI Analyzer task. Test Name — Test Name displays the name of the test. Pass — Pass contains data on the tests that passed for the VI specified in VI Path. VI Path — VI Path contains the path to the VI for which the test results are listed. index — row — column — Fail — Fail contains data on the tests that failed for the VI specified in VI Path. VI Path — VI Path contains the path to the VI for which the test results are listed. index — row — column — Skipped — Skipped contains data on the tests that the VI Analyzer skipped for the VI specified in VI Path. VI Path — VI Path contains the path to the VI for which the test results are listed. index — row — column — Summary Statistics — Summary Statistics contains the summary for a VI Analyzer task. Passed Tests — Passed Tests indicates the total number of tests in the VI Analyzer task that passed. Failed Tests — Failed Tests indicates the total number of tests in the VI Analyzer task that failed. Skipped Tests — Skipped Tests indicates the total number of tests in the VI Analyzer task that the VI Analyzer skipped. VIs not loadable — VIs not loadable indicates the total number of VIs that the VI Analyzer could not load. Tests not loadable — Tests not loadable indicates the total number of tests that the VI Analyzer was not able to load. Tests not runnable — Tests not runnable indicates the total number of tests that the VI Analyzer was not able to run. Test error out — Test error out contains data on errors that occurred when the VI Analyzer performed tests on the VI specified in VI Path. Start Time — Start Time indicates the time when the analysis began. Total Time (s) — Total Time (s) indicates the time it took for the VI Analyzer to run the analysis. Test Config Data — Test Config Data contains the configuration settings for every test included in the VI Analyzer task. Test Name — The name of the VI Analyzer test. Config Ref — The reference to the configuration VI for the VI Analyzer test specified in Test Name. Ref Valid? — Specifies whether or not the Config Ref is a valid VI reference. Test Ranking — The ranking of the test specified in Test Name. Max Failures — The maximum allowable number of failures to return for the test specified in Test Name on each VI being tested. Test Path — The path to the test specified in Test Name. Control Values — The names and values of all configuration options of the test specified by Test Name. Control Name — Control Name specifies the name of the control in which you want to change the value. Control Value — Control Value contains the new value that you want for the control you specify in Control Name. If the value is a data type different than the control you specify in Control Name, the VI returns an error. Selected? — Indicates whether or not the test specified in Test Name will run in the current VI Analyzer task. error out — error out contains error information. This output provides standard error out functionality. |
| --- |
| Raw Results — Raw Results contains the unparsed results data for every test and every VI in the VI Analyzer task. Test Name — Test Name displays the name of the test. Results Data — Results Data contains the unparsed results for the test specified in Test Name. Result Message — Ref Index — Status — Status indicates whether the test in Test Name passed or failed. Exceed Max Fails? — Exceed Max Fails? indicates whether the test in Test Name failed more than the maximum number of times specified for that test. Parsed Results Data (by VI) — Parsed Results Data (by VI) contains the results by VI for every test in the VI Analyzer task, including which tests passed and failed, which tests the VI Analyzer could not load or run, and which errors occurred. VI Path — VI Path contains the path to the VI for which the test results are listed. Pass — Pass contains data on the tests that passed for the VI specified in VI Path. row — column — Fail — Fail contains data on the tests that failed for the VI specified in VI Path. row — column — Skipped — Skipped contains data on the tests that the VI Analyzer skipped for the VI specified in VI Path. row — column — VI not loadable — VI not loadable contains data on whether the VI Analyzer was able to load the VI specified in VI Path. row — column — Test not loadable — Test not loadable contains data on the tests that the VI Analyzer was not able to load for the VI specified in VI Path. row — column — Test not runnable — Test not runnable contains data on the tests that the VI Analyzer was not able to run for the VI specified in VI Path. row — column — Test error out — Test error out contains data on errors that occurred when the VI Analyzer performed tests on the VI specified in VI Path. row — column — Parsed Results Data (by Test) — Parsed Results Data (by Test) contains the results of every test and whether the VI Analyzer passed, failed, or skipped the test for every VI in the VI Analyzer task. Test Name — Test Name displays the name of the test. Pass — Pass contains data on the tests that passed for the VI specified in VI Path. VI Path — VI Path contains the path to the VI for which the test results are listed. index — row — column — Fail — Fail contains data on the tests that failed for the VI specified in VI Path. VI Path — VI Path contains the path to the VI for which the test results are listed. index — row — column — Skipped — Skipped contains data on the tests that the VI Analyzer skipped for the VI specified in VI Path. VI Path — VI Path contains the path to the VI for which the test results are listed. index — row — column — Summary Statistics — Summary Statistics contains the summary for a VI Analyzer task. Passed Tests — Passed Tests indicates the total number of tests in the VI Analyzer task that passed. Failed Tests — Failed Tests indicates the total number of tests in the VI Analyzer task that failed. Skipped Tests — Skipped Tests indicates the total number of tests in the VI Analyzer task that the VI Analyzer skipped. VIs not loadable — VIs not loadable indicates the total number of VIs that the VI Analyzer could not load. Tests not loadable — Tests not loadable indicates the total number of tests that the VI Analyzer was not able to load. Tests not runnable — Tests not runnable indicates the total number of tests that the VI Analyzer was not able to run. Test error out — Test error out contains data on errors that occurred when the VI Analyzer performed tests on the VI specified in VI Path. Start Time — Start Time indicates the time when the analysis began. Total Time (s) — Total Time (s) indicates the time it took for the VI Analyzer to run the analysis. Test Config Data — Test Config Data contains the configuration settings for every test included in the VI Analyzer task. Test Name — The name of the VI Analyzer test. Config Ref — The reference to the configuration VI for the VI Analyzer test specified in Test Name. Ref Valid? — Specifies whether or not the Config Ref is a valid VI reference. Test Ranking — The ranking of the test specified in Test Name. Max Failures — The maximum allowable number of failures to return for the test specified in Test Name on each VI being tested. Test Path — The path to the test specified in Test Name. Control Values — The names and values of all configuration options of the test specified by Test Name. Control Name — Control Name specifies the name of the control in which you want to change the value. Control Value — Control Value contains the new value that you want for the control you specify in Control Name. If the value is a data type different than the control you specify in Control Name, the VI returns an error. Selected? — Indicates whether or not the test specified in Test Name will run in the current VI Analyzer task. |
| Test Name — Test Name displays the name of the test. Results Data — Results Data contains the unparsed results for the test specified in Test Name. Result Message — Ref Index — Status — Status indicates whether the test in Test Name passed or failed. Exceed Max Fails? — Exceed Max Fails? indicates whether the test in Test Name failed more than the maximum number of times specified for that test. |
| Result Message — Ref Index — |
| VI Path — VI Path contains the path to the VI for which the test results are listed. Pass — Pass contains data on the tests that passed for the VI specified in VI Path. row — column — Fail — Fail contains data on the tests that failed for the VI specified in VI Path. row — column — Skipped — Skipped contains data on the tests that the VI Analyzer skipped for the VI specified in VI Path. row — column — VI not loadable — VI not loadable contains data on whether the VI Analyzer was able to load the VI specified in VI Path. row — column — Test not loadable — Test not loadable contains data on the tests that the VI Analyzer was not able to load for the VI specified in VI Path. row — column — Test not runnable — Test not runnable contains data on the tests that the VI Analyzer was not able to run for the VI specified in VI Path. row — column — Test error out — Test error out contains data on errors that occurred when the VI Analyzer performed tests on the VI specified in VI Path. row — column — |
| row — column — |
| row — column — |
| row — column — |
| row — column — |
| row — column — |
| row — column — |
| row — column — |
| Test Name — Test Name displays the name of the test. Pass — Pass contains data on the tests that passed for the VI specified in VI Path. VI Path — VI Path contains the path to the VI for which the test results are listed. index — row — column — Fail — Fail contains data on the tests that failed for the VI specified in VI Path. VI Path — VI Path contains the path to the VI for which the test results are listed. index — row — column — Skipped — Skipped contains data on the tests that the VI Analyzer skipped for the VI specified in VI Path. VI Path — VI Path contains the path to the VI for which the test results are listed. index — row — column — |
| VI Path — VI Path contains the path to the VI for which the test results are listed. index — row — column — |
| row — column — |
| VI Path — VI Path contains the path to the VI for which the test results are listed. index — row — column — |
| row — column — |
| VI Path — VI Path contains the path to the VI for which the test results are listed. index — row — column — |
| row — column — |
| Passed Tests — Passed Tests indicates the total number of tests in the VI Analyzer task that passed. Failed Tests — Failed Tests indicates the total number of tests in the VI Analyzer task that failed. Skipped Tests — Skipped Tests indicates the total number of tests in the VI Analyzer task that the VI Analyzer skipped. VIs not loadable — VIs not loadable indicates the total number of VIs that the VI Analyzer could not load. Tests not loadable — Tests not loadable indicates the total number of tests that the VI Analyzer was not able to load. Tests not runnable — Tests not runnable indicates the total number of tests that the VI Analyzer was not able to run. Test error out — Test error out contains data on errors that occurred when the VI Analyzer performed tests on the VI specified in VI Path. Start Time — Start Time indicates the time when the analysis began. Total Time (s) — Total Time (s) indicates the time it took for the VI Analyzer to run the analysis. |
| Test Name — The name of the VI Analyzer test. Config Ref — The reference to the configuration VI for the VI Analyzer test specified in Test Name. Ref Valid? — Specifies whether or not the Config Ref is a valid VI reference. Test Ranking — The ranking of the test specified in Test Name. Max Failures — The maximum allowable number of failures to return for the test specified in Test Name on each VI being tested. Test Path — The path to the test specified in Test Name. Control Values — The names and values of all configuration options of the test specified by Test Name. Control Name — Control Name specifies the name of the control in which you want to change the value. Control Value — Control Value contains the new value that you want for the control you specify in Control Name. If the value is a data type different than the control you specify in Control Name, the VI returns an error. Selected? — Indicates whether or not the test specified in Test Name will run in the current VI Analyzer task. |
| Control Name — Control Name specifies the name of the control in which you want to change the value. Control Value — Control Value contains the new value that you want for the control you specify in Control Name. If the value is a data type different than the control you specify in Control Name, the VI returns an error. |

Parent topic:

VI Analyzer

<!--NI_TOPIC bundle=lvvia-api-ref path=vi-lib/addons/analyzer/analyzerapi-llb/vian-save-configuration-file-vi.html language=enus -->
## TOPIC 00018: VIAn Save Configuration File VI

- bundle_id: `lvvia-api-ref`
- source_path: `vi-lib/addons/analyzer/analyzerapi-llb/vian-save-configuration-file-vi.html`
- source_url: https://docs-be.ni.com/bundle/lvvia-api-ref/raw/resource/enus/vi-lib/addons/analyzer/analyzerapi-llb/vian-save-configuration-file-vi.html
- document_id: `lvvia-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Saves the current VI Analyzer task settings to a configuration file. icon Inputs/Outputs cbool.png Overwrite? (T) Overwrite? specifies whether to overwrite the configuration file if the file specified in Path to Configuration File already exists. The default is TRUE, which overwrites the existing fi

### VIAn Save Configuration File VI

Saves the current VI Analyzer task settings to a configuration file.

[IMAGE alt='icon' src='vian-save-configuration-file-vi.png']

#### Inputs/Outputs

| Overwrite? (T) — Overwrite? specifies whether to overwrite the configuration file if the file specified in Path to Configuration File already exists. The default is TRUE, which overwrites the existing file. If Overwrite? is FALSE and the file exists, the VI returns an error. VI Analyzer Task in — VI Analyzer Task in contains a reference to the current task. The VI Analyzer task must be a valid task that you created using the VIAn New Task VI. Path to Configuration File — Path to Configuration File contains the path to the configuration file you want to save. If you specify an invalid path, the VI returns an error. If you specify no path, the VI saves the configuration file using the path specified in the VIAn New Task VI. If you specified no paths for either VI, the VI returns an error. error in (no error) — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. VI Analyzer Task out — VI Analyzer Task out returns a reference to the VI Analyzer task specified in VI Analyzer Task in. error out — error out contains error information. This output provides standard error out functionality. |
| --- |

Parent topic:

VI Analyzer

<!--NI_TOPIC bundle=lvvia-api-ref path=vi-lib/addons/analyzer/analyzerapi-llb/vian-select-tests-vi.html language=enus -->
## TOPIC 00019: VIAn Select Tests VI

- bundle_id: `lvvia-api-ref`
- source_path: `vi-lib/addons/analyzer/analyzerapi-llb/vian-select-tests-vi.html`
- source_url: https://docs-be.ni.com/bundle/lvvia-api-ref/raw/resource/enus/vi-lib/addons/analyzer/analyzerapi-llb/vian-select-tests-vi.html
- document_id: `lvvia-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Selects or deselects the specified tests in the VI Analyzer task. icon Inputs/Outputs cdlrn.png VI Analyzer Task in VI Analyzer Task in contains a reference to the current task. The VI Analyzer task must be a valid task that you created using the VIAn New Task VI. c1dstr.png Test Names Test Names sp

### VIAn Select Tests VI

Selects or deselects the specified tests in the VI Analyzer task.

[IMAGE alt='icon' src='vian-select-tests-vi.png']

#### Inputs/Outputs

| VI Analyzer Task in — VI Analyzer Task in contains a reference to the current task. The VI Analyzer task must be a valid task that you created using the VIAn New Task VI. Test Names — Test Names specifies the names of the VI Analyzer tests you want to select or deselect. error in (no error) — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. Select Test? (T) — Select Test? specifies whether to select or deselect the specified tests in the VI Analyzer task. The default is TRUE, which selects the tests. If you set Select Test? to FALSE, the VI deselects the specified tests. VI Analyzer Task out — VI Analyzer Task out returns a reference to the VI Analyzer task specified in VI Analyzer Task in. error out — error out contains error information. This output provides standard error out functionality. |
| --- |

Parent topic:

VI Analyzer Utilities

<!--NI_TOPIC bundle=lvvia-api-ref path=via_intro.html language=enus -->
## TOPIC 00020: LabVIEW VI Analyzer Toolkit Programming Reference Manual

- bundle_id: `lvvia-api-ref`
- source_path: `via_intro.html`
- source_url: https://docs-be.ni.com/bundle/lvvia-api-ref/raw/resource/enus/via_intro.html
- document_id: `lvvia-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: The LabVIEW VI Analyzer Toolkit LabVIEW Release Notes Visit this site for links to known issues, bugs fixed since the last release, and other notes for any LabVIEW release.To comment on National Instruments documentation, refer to the National Instruments website.

### LabVIEW VI Analyzer Toolkit Programming Reference Manual

The LabVIEW VI Analyzer Toolkit

[LabVIEW Release Notes](https://www.ni.com/en-us/support/documentation/release-notes/product.labview.html) 
Visit this site for links to known issues, bugs fixed since the last release, and other notes for any LabVIEW release.

To comment on National Instruments documentation, refer to the National Instruments website.
