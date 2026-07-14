# JAVA OPENAPI: ReportVariables (2024x API)

- source_url: https://jdocs.nomagic.com/2024xRefresh1/com/nomagic/magicdraw/diff/report/ReportVariables.html
- source_path: `com/nomagic/magicdraw/diff/report/ReportVariables.html`
- source_sha256: `176a79307cacfbb1843d406cf47ed9809e2f4639166be7d5e83941b83656161f`
- captured_utc: `2026-07-14T16:51:18.399166+00:00`

## NORMALIZED JAVADOC CONTENT

======== START OF CLASS DATA ========

Package [com.nomagic.magicdraw.diff.report](package-summary.html)

## Class ReportVariables

[java.lang.Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)
com.nomagic.magicdraw.diff.report.ReportVariables

@OpenApiAllpublic final classReportVariables
extends [Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)
Report template variables

=========== FIELD SUMMARY =========== 
Field Summary
Fields
Modifier and Type
Field
Description
`static final [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)`
`[ADDED_INFOS](#ADDED_INFOS)`
Will have a list of addition com.nomagic.magicdraw.diff.report.ElementReportInfo instances
`static final [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)`
`[ANCESTOR_BRANCH](#ANCESTOR_BRANCH)`
Ancestor project branch name
`static final [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)`
`[ANCESTOR_DIAGRAM_COUNT](#ANCESTOR_DIAGRAM_COUNT)`
Ancestor project total diagram count
`static final [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)`
`[ANCESTOR_DIAGRAM_LABEL](#ANCESTOR_DIAGRAM_LABEL)`
Will have value "Base" when comparing, "Target" - when two merge, "Ancestor" - when three way merge
`static final [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)`
`[ANCESTOR_ELEMENT_COUNT](#ANCESTOR_ELEMENT_COUNT)`
Ancestor project total element count
`static final [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)`
`[ANCESTOR_PROJECT_NAME](#ANCESTOR_PROJECT_NAME)`
Ancestor project name
`static final [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)`
`[ANCESTOR_VERSION](#ANCESTOR_VERSION)`
Ancestor project version
`static final [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)`
`[AUTHOR](#AUTHOR)`
Project author name, or logged in twc user name when report is done for twc project,
`static final [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)`
`[DATE](#DATE)`
Report creation date
`static final [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)`
`[DIAGRAM_REPORT_INFOS](#DIAGRAM_REPORT_INFOS)`
Will have a list of com.nomagic.magicdraw.diff.report.DiagramReportInfo instances
`static final [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)`
`[ELEMENT_REPORT_INFOS](#ELEMENT_REPORT_INFOS)`
Will have a list of all com.nomagic.magicdraw.diff.report.ElementReportInfo instances
`static final [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)`
`[FOOTER_DATE](#FOOTER_DATE)`
Short format of report creation date
`static final [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)`
`[FOOTER_YEAR](#FOOTER_YEAR)`
Year of the report creation
`static final [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)`
`[IS_2WAY](#IS_2WAY)`
True, when two way project merge is done
`static final [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)`
`[IS_3WAY](#IS_3WAY)`
True, when three way project merge is done
`static final [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)`
`[IS_COMPARE](#IS_COMPARE)`
True, when two project compare is done
`static final [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)`
`[IS_FULL_REPORT](#IS_FULL_REPORT)`
True, when report is done from full report template
`static final [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)`
`[MODIFIED_INFOS](#MODIFIED_INFOS)`
Will have a list of modification com.nomagic.magicdraw.diff.report.ElementReportInfo instances
`static final [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)`
`[PROJECT](#PROJECT)`
Holds info from com.nomagic.magicdraw.core.Project instance of the target (when 2way or compare), or ancestor project
`static final [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)`
`[REMOVED_INFOS](#REMOVED_INFOS)`
Will have a list of removal com.nomagic.magicdraw.diff.report.ElementReportInfo instances
`static final [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)`
`[REPORT_TYPE](#REPORT_TYPE)`
Holds info from com.nomagic.magicdraw.diff.report.ReportType instance
`static final [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)`
`[SCOPE_NAME](#SCOPE_NAME)`
Content history report template variable.
`static final [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)`
`[SCOPE_QNAME](#SCOPE_QNAME)`
Content history report template variable.
`static final [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)`
`[SCOPE_TYPE](#SCOPE_TYPE)`
Content history report template variable.
`static final [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)`
`[SOURCE_ADDED](#SOURCE_ADDED)`
Number of addition changes in source project
`static final [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)`
`[SOURCE_ADDED_DIAGRAMS](#SOURCE_ADDED_DIAGRAMS)`
Number of added diagrams in source project
`static final [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)`
`[SOURCE_ADDED_SYMBOLS](#SOURCE_ADDED_SYMBOLS)`
Number of added symbols in source project
`static final [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)`
`[SOURCE_BRANCH](#SOURCE_BRANCH)`
Source project branch name
`static final [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)`
`[SOURCE_DIAGRAM_COUNT](#SOURCE_DIAGRAM_COUNT)`
Source project total diagram count
`static final [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)`
`[SOURCE_ELEMENT_COUNT](#SOURCE_ELEMENT_COUNT)`
Source project total element count
`static final [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)`
`[SOURCE_LABEL](#SOURCE_LABEL)`
Will have value "Compared" when comparing, and "Source" - when merging
`static final [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)`
`[SOURCE_MODIFIED](#SOURCE_MODIFIED)`
Number of modification changes in source project
`static final [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)`
`[SOURCE_MODIFIED_DIAGRAMS](#SOURCE_MODIFIED_DIAGRAMS)`
Number of modified diagrams in source project
`static final [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)`
`[SOURCE_MODIFIED_SYMBOLS](#SOURCE_MODIFIED_SYMBOLS)`
Number of modified symbols in source project
`static final [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)`
`[SOURCE_OVERALL](#SOURCE_OVERALL)`
Total number of addition, modification and removal changes in source project
`static final [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)`
`[SOURCE_OVERALL_DIAGRAMS](#SOURCE_OVERALL_DIAGRAMS)`
Total number of added, modified, deleted diagrams and symbols in source project
`static final [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)`
`[SOURCE_PROJECT_NAME](#SOURCE_PROJECT_NAME)`
Source project name
`static final [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)`
`[SOURCE_REMOVED](#SOURCE_REMOVED)`
Number of removal changes in source project
`static final [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)`
`[SOURCE_REMOVED_DIAGRAMS](#SOURCE_REMOVED_DIAGRAMS)`
Number of removed diagrams in source project
`static final [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)`
`[SOURCE_REMOVED_SYMBOLS](#SOURCE_REMOVED_SYMBOLS)`
Number of deleted symbols in source project
`static final [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)`
`[SOURCE_VERSION](#SOURCE_VERSION)`
Source project version
`static final [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)`
`[TARGET_ADDED](#TARGET_ADDED)`
Number of addition changes in target project
`static final [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)`
`[TARGET_ADDED_DIAGRAMS](#TARGET_ADDED_DIAGRAMS)`
Number of added diagrams in target project
`static final [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)`
`[TARGET_ADDED_SYMBOLS](#TARGET_ADDED_SYMBOLS)`
Number of added symbols in target project
`static final [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)`
`[TARGET_BRANCH](#TARGET_BRANCH)`
Target project branch name
`static final [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)`
`[TARGET_DIAGRAM_COUNT](#TARGET_DIAGRAM_COUNT)`
Target project total diagram count
`static final [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)`
`[TARGET_DIAGRAM_LABEL](#TARGET_DIAGRAM_LABEL)`
Will have value "Compared" when comparing, "Target" - when merging
`static final [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)`
`[TARGET_ELEMENT_COUNT](#TARGET_ELEMENT_COUNT)`
Target project total element count
`static final [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)`
`[TARGET_LABEL](#TARGET_LABEL)`
Will have value "Base" when comparing, and "Target" - when merging
`static final [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)`
`[TARGET_MODIFIED](#TARGET_MODIFIED)`
Number of modification changes in target project
`static final [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)`
`[TARGET_MODIFIED_DIAGRAMS](#TARGET_MODIFIED_DIAGRAMS)`
Number of modified diagrams in target project
`static final [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)`
`[TARGET_MODIFIED_SYMBOLS](#TARGET_MODIFIED_SYMBOLS)`
Number of modified symbols in target project
`static final [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)`
`[TARGET_OVERALL](#TARGET_OVERALL)`
Total number of addition, modification and removal changes in target project
`static final [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)`
`[TARGET_OVERALL_DIAGRAMS](#TARGET_OVERALL_DIAGRAMS)`
Total number of added, modified, deleted diagrams and symbols in target project
`static final [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)`
`[TARGET_PROJECT_NAME](#TARGET_PROJECT_NAME)`
Target project name
`static final [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)`
`[TARGET_REMOVED](#TARGET_REMOVED)`
Number of removal changes in target project
`static final [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)`
`[TARGET_REMOVED_DIAGRAMS](#TARGET_REMOVED_DIAGRAMS)`
Number of removed diagrams in target project
`static final [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)`
`[TARGET_REMOVED_SYMBOLS](#TARGET_REMOVED_SYMBOLS)`
Number of deleted symbols in target project
`static final [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)`
`[TARGET_VERSION](#TARGET_VERSION)`
Target project version
`static final [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)`
`[TITLE](#TITLE)`
Will have value "Comparison", when project compare is done, or "Merge" - when project merge
 ========== METHOD SUMMARY =========== 
Method Summary
Methods inherited from class java.lang.[Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)
`[clone](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#clone()), [equals](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#equals(java.lang.Object)), [finalize](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#finalize()), [getClass](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#getClass()), [hashCode](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#hashCode()), [notify](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notify()), [notifyAll](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notifyAll()), [toString](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#toString()), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait()), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long)), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long,int))`

============ FIELD DETAIL =========== 
Field Details
AUTHOR
public static final [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) AUTHOR
Project author name, or logged in twc user name when report is done for twc project,
See Also:
[Constant Field Values](../../../../../constant-values.html#com.nomagic.magicdraw.diff.report.ReportVariables.AUTHOR)
DATE
public static final [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) DATE
Report creation date
See Also:
[Constant Field Values](../../../../../constant-values.html#com.nomagic.magicdraw.diff.report.ReportVariables.DATE)
FOOTER_DATE
public static final [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) FOOTER_DATE
Short format of report creation date
See Also:
[Constant Field Values](../../../../../constant-values.html#com.nomagic.magicdraw.diff.report.ReportVariables.FOOTER_DATE)
FOOTER_YEAR
public static final [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) FOOTER_YEAR
Year of the report creation
See Also:
[Constant Field Values](../../../../../constant-values.html#com.nomagic.magicdraw.diff.report.ReportVariables.FOOTER_YEAR)
IS_COMPARE
public static final [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) IS_COMPARE
True, when two project compare is done
See Also:
[Constant Field Values](../../../../../constant-values.html#com.nomagic.magicdraw.diff.report.ReportVariables.IS_COMPARE)
IS_2WAY
public static final [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) IS_2WAY
True, when two way project merge is done
See Also:
[Constant Field Values](../../../../../constant-values.html#com.nomagic.magicdraw.diff.report.ReportVariables.IS_2WAY)
IS_3WAY
public static final [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) IS_3WAY
True, when three way project merge is done
See Also:
[Constant Field Values](../../../../../constant-values.html#com.nomagic.magicdraw.diff.report.ReportVariables.IS_3WAY)
REPORT_TYPE
public static final [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) REPORT_TYPE
Holds info from com.nomagic.magicdraw.diff.report.ReportType instance
See Also:
[Constant Field Values](../../../../../constant-values.html#com.nomagic.magicdraw.diff.report.ReportVariables.REPORT_TYPE)
IS_FULL_REPORT
public static final [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) IS_FULL_REPORT
True, when report is done from full report template
See Also:
[Constant Field Values](../../../../../constant-values.html#com.nomagic.magicdraw.diff.report.ReportVariables.IS_FULL_REPORT)
TITLE
public static final [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) TITLE
Will have value "Comparison", when project compare is done, or "Merge" - when project merge
See Also:
[Constant Field Values](../../../../../constant-values.html#com.nomagic.magicdraw.diff.report.ReportVariables.TITLE)
PROJECT
public static final [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) PROJECT
Holds info from com.nomagic.magicdraw.core.Project instance of the target (when 2way or compare), or ancestor project
See Also:
[Constant Field Values](../../../../../constant-values.html#com.nomagic.magicdraw.diff.report.ReportVariables.PROJECT)
TARGET_LABEL
public static final [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) TARGET_LABEL
Will have value "Base" when comparing, and "Target" - when merging
See Also:
[Constant Field Values](../../../../../constant-values.html#com.nomagic.magicdraw.diff.report.ReportVariables.TARGET_LABEL)
SOURCE_LABEL
public static final [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) SOURCE_LABEL
Will have value "Compared" when comparing, and "Source" - when merging
See Also:
[Constant Field Values](../../../../../constant-values.html#com.nomagic.magicdraw.diff.report.ReportVariables.SOURCE_LABEL)
TARGET_PROJECT_NAME
public static final [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) TARGET_PROJECT_NAME
Target project name
See Also:
[Constant Field Values](../../../../../constant-values.html#com.nomagic.magicdraw.diff.report.ReportVariables.TARGET_PROJECT_NAME)
TARGET_BRANCH
public static final [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) TARGET_BRANCH
Target project branch name
See Also:
[Constant Field Values](../../../../../constant-values.html#com.nomagic.magicdraw.diff.report.ReportVariables.TARGET_BRANCH)
TARGET_VERSION
public static final [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) TARGET_VERSION
Target project version
See Also:
[Constant Field Values](../../../../../constant-values.html#com.nomagic.magicdraw.diff.report.ReportVariables.TARGET_VERSION)
TARGET_ELEMENT_COUNT
public static final [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) TARGET_ELEMENT_COUNT
Target project total element count
See Also:
[Constant Field Values](../../../../../constant-values.html#com.nomagic.magicdraw.diff.report.ReportVariables.TARGET_ELEMENT_COUNT)
TARGET_DIAGRAM_COUNT
public static final [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) TARGET_DIAGRAM_COUNT
Target project total diagram count
See Also:
[Constant Field Values](../../../../../constant-values.html#com.nomagic.magicdraw.diff.report.ReportVariables.TARGET_DIAGRAM_COUNT)
SOURCE_PROJECT_NAME
public static final [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) SOURCE_PROJECT_NAME
Source project name
See Also:
[Constant Field Values](../../../../../constant-values.html#com.nomagic.magicdraw.diff.report.ReportVariables.SOURCE_PROJECT_NAME)
SOURCE_BRANCH
public static final [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) SOURCE_BRANCH
Source project branch name
See Also:
[Constant Field Values](../../../../../constant-values.html#com.nomagic.magicdraw.diff.report.ReportVariables.SOURCE_BRANCH)
SOURCE_VERSION
public static final [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) SOURCE_VERSION
Source project version
See Also:
[Constant Field Values](../../../../../constant-values.html#com.nomagic.magicdraw.diff.report.ReportVariables.SOURCE_VERSION)
SOURCE_ELEMENT_COUNT
public static final [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) SOURCE_ELEMENT_COUNT
Source project total element count
See Also:
[Constant Field Values](../../../../../constant-values.html#com.nomagic.magicdraw.diff.report.ReportVariables.SOURCE_ELEMENT_COUNT)
SOURCE_DIAGRAM_COUNT
public static final [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) SOURCE_DIAGRAM_COUNT
Source project total diagram count
See Also:
[Constant Field Values](../../../../../constant-values.html#com.nomagic.magicdraw.diff.report.ReportVariables.SOURCE_DIAGRAM_COUNT)
ANCESTOR_PROJECT_NAME
public static final [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) ANCESTOR_PROJECT_NAME
Ancestor project name
See Also:
[Constant Field Values](../../../../../constant-values.html#com.nomagic.magicdraw.diff.report.ReportVariables.ANCESTOR_PROJECT_NAME)
ANCESTOR_BRANCH
public static final [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) ANCESTOR_BRANCH
Ancestor project branch name
See Also:
[Constant Field Values](../../../../../constant-values.html#com.nomagic.magicdraw.diff.report.ReportVariables.ANCESTOR_BRANCH)
ANCESTOR_VERSION
public static final [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) ANCESTOR_VERSION
Ancestor project version
See Also:
[Constant Field Values](../../../../../constant-values.html#com.nomagic.magicdraw.diff.report.ReportVariables.ANCESTOR_VERSION)
ANCESTOR_ELEMENT_COUNT
public static final [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) ANCESTOR_ELEMENT_COUNT
Ancestor project total element count
See Also:
[Constant Field Values](../../../../../constant-values.html#com.nomagic.magicdraw.diff.report.ReportVariables.ANCESTOR_ELEMENT_COUNT)
ANCESTOR_DIAGRAM_COUNT
public static final [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) ANCESTOR_DIAGRAM_COUNT
Ancestor project total diagram count
See Also:
[Constant Field Values](../../../../../constant-values.html#com.nomagic.magicdraw.diff.report.ReportVariables.ANCESTOR_DIAGRAM_COUNT)
TARGET_ADDED
public static final [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) TARGET_ADDED
Number of addition changes in target project
See Also:
[Constant Field Values](../../../../../constant-values.html#com.nomagic.magicdraw.diff.report.ReportVariables.TARGET_ADDED)
TARGET_MODIFIED
public static final [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) TARGET_MODIFIED
Number of modification changes in target project
See Also:
[Constant Field Values](../../../../../constant-values.html#com.nomagic.magicdraw.diff.report.ReportVariables.TARGET_MODIFIED)
TARGET_REMOVED
public static final [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) TARGET_REMOVED
Number of removal changes in target project
See Also:
[Constant Field Values](../../../../../constant-values.html#com.nomagic.magicdraw.diff.report.ReportVariables.TARGET_REMOVED)
TARGET_OVERALL
public static final [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) TARGET_OVERALL
Total number of addition, modification and removal changes in target project
See Also:
[Constant Field Values](../../../../../constant-values.html#com.nomagic.magicdraw.diff.report.ReportVariables.TARGET_OVERALL)
SOURCE_ADDED
public static final [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) SOURCE_ADDED
Number of addition changes in source project
See Also:
[Constant Field Values](../../../../../constant-values.html#com.nomagic.magicdraw.diff.report.ReportVariables.SOURCE_ADDED)
SOURCE_MODIFIED
public static final [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) SOURCE_MODIFIED
Number of modification changes in source project
See Also:
[Constant Field Values](../../../../../constant-values.html#com.nomagic.magicdraw.diff.report.ReportVariables.SOURCE_MODIFIED)
SOURCE_REMOVED
public static final [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) SOURCE_REMOVED
Number of removal changes in source project
See Also:
[Constant Field Values](../../../../../constant-values.html#com.nomagic.magicdraw.diff.report.ReportVariables.SOURCE_REMOVED)
SOURCE_OVERALL
public static final [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) SOURCE_OVERALL
Total number of addition, modification and removal changes in source project
See Also:
[Constant Field Values](../../../../../constant-values.html#com.nomagic.magicdraw.diff.report.ReportVariables.SOURCE_OVERALL)
TARGET_ADDED_DIAGRAMS
public static final [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) TARGET_ADDED_DIAGRAMS
Number of added diagrams in target project
See Also:
[Constant Field Values](../../../../../constant-values.html#com.nomagic.magicdraw.diff.report.ReportVariables.TARGET_ADDED_DIAGRAMS)
TARGET_MODIFIED_DIAGRAMS
public static final [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) TARGET_MODIFIED_DIAGRAMS
Number of modified diagrams in target project
See Also:
[Constant Field Values](../../../../../constant-values.html#com.nomagic.magicdraw.diff.report.ReportVariables.TARGET_MODIFIED_DIAGRAMS)
TARGET_REMOVED_DIAGRAMS
public static final [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) TARGET_REMOVED_DIAGRAMS
Number of removed diagrams in target project
See Also:
[Constant Field Values](../../../../../constant-values.html#com.nomagic.magicdraw.diff.report.ReportVariables.TARGET_REMOVED_DIAGRAMS)
TARGET_ADDED_SYMBOLS
public static final [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) TARGET_ADDED_SYMBOLS
Number of added symbols in target project
See Also:
[Constant Field Values](../../../../../constant-values.html#com.nomagic.magicdraw.diff.report.ReportVariables.TARGET_ADDED_SYMBOLS)
TARGET_MODIFIED_SYMBOLS
public static final [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) TARGET_MODIFIED_SYMBOLS
Number of modified symbols in target project
See Also:
[Constant Field Values](../../../../../constant-values.html#com.nomagic.magicdraw.diff.report.ReportVariables.TARGET_MODIFIED_SYMBOLS)
TARGET_REMOVED_SYMBOLS
public static final [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) TARGET_REMOVED_SYMBOLS
Number of deleted symbols in target project
See Also:
[Constant Field Values](../../../../../constant-values.html#com.nomagic.magicdraw.diff.report.ReportVariables.TARGET_REMOVED_SYMBOLS)
TARGET_OVERALL_DIAGRAMS
public static final [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) TARGET_OVERALL_DIAGRAMS
Total number of added, modified, deleted diagrams and symbols in target project
See Also:
[Constant Field Values](../../../../../constant-values.html#com.nomagic.magicdraw.diff.report.ReportVariables.TARGET_OVERALL_DIAGRAMS)
SOURCE_ADDED_DIAGRAMS
public static final [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) SOURCE_ADDED_DIAGRAMS
Number of added diagrams in source project
See Also:
[Constant Field Values](../../../../../constant-values.html#com.nomagic.magicdraw.diff.report.ReportVariables.SOURCE_ADDED_DIAGRAMS)
SOURCE_MODIFIED_DIAGRAMS
public static final [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) SOURCE_MODIFIED_DIAGRAMS
Number of modified diagrams in source project
See Also:
[Constant Field Values](../../../../../constant-values.html#com.nomagic.magicdraw.diff.report.ReportVariables.SOURCE_MODIFIED_DIAGRAMS)
SOURCE_REMOVED_DIAGRAMS
public static final [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) SOURCE_REMOVED_DIAGRAMS
Number of removed diagrams in source project
See Also:
[Constant Field Values](../../../../../constant-values.html#com.nomagic.magicdraw.diff.report.ReportVariables.SOURCE_REMOVED_DIAGRAMS)
SOURCE_ADDED_SYMBOLS
public static final [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) SOURCE_ADDED_SYMBOLS
Number of added symbols in source project
See Also:
[Constant Field Values](../../../../../constant-values.html#com.nomagic.magicdraw.diff.report.ReportVariables.SOURCE_ADDED_SYMBOLS)
SOURCE_MODIFIED_SYMBOLS
public static final [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) SOURCE_MODIFIED_SYMBOLS
Number of modified symbols in source project
See Also:
[Constant Field Values](../../../../../constant-values.html#com.nomagic.magicdraw.diff.report.ReportVariables.SOURCE_MODIFIED_SYMBOLS)
SOURCE_REMOVED_SYMBOLS
public static final [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) SOURCE_REMOVED_SYMBOLS
Number of deleted symbols in source project
See Also:
[Constant Field Values](../../../../../constant-values.html#com.nomagic.magicdraw.diff.report.ReportVariables.SOURCE_REMOVED_SYMBOLS)
SOURCE_OVERALL_DIAGRAMS
public static final [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) SOURCE_OVERALL_DIAGRAMS
Total number of added, modified, deleted diagrams and symbols in source project
See Also:
[Constant Field Values](../../../../../constant-values.html#com.nomagic.magicdraw.diff.report.ReportVariables.SOURCE_OVERALL_DIAGRAMS)
ANCESTOR_DIAGRAM_LABEL
public static final [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) ANCESTOR_DIAGRAM_LABEL
Will have value "Base" when comparing, "Target" - when two merge, "Ancestor" - when three way merge
See Also:
[Constant Field Values](../../../../../constant-values.html#com.nomagic.magicdraw.diff.report.ReportVariables.ANCESTOR_DIAGRAM_LABEL)
TARGET_DIAGRAM_LABEL
public static final [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) TARGET_DIAGRAM_LABEL
Will have value "Compared" when comparing, "Target" - when merging
See Also:
[Constant Field Values](../../../../../constant-values.html#com.nomagic.magicdraw.diff.report.ReportVariables.TARGET_DIAGRAM_LABEL)
DIAGRAM_REPORT_INFOS
public static final [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) DIAGRAM_REPORT_INFOS
Will have a list of com.nomagic.magicdraw.diff.report.DiagramReportInfo instances
See Also:
[Constant Field Values](../../../../../constant-values.html#com.nomagic.magicdraw.diff.report.ReportVariables.DIAGRAM_REPORT_INFOS)
ELEMENT_REPORT_INFOS
public static final [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) ELEMENT_REPORT_INFOS
Will have a list of all com.nomagic.magicdraw.diff.report.ElementReportInfo instances
See Also:
[Constant Field Values](../../../../../constant-values.html#com.nomagic.magicdraw.diff.report.ReportVariables.ELEMENT_REPORT_INFOS)
ADDED_INFOS
public static final [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) ADDED_INFOS
Will have a list of addition com.nomagic.magicdraw.diff.report.ElementReportInfo instances
See Also:
[Constant Field Values](../../../../../constant-values.html#com.nomagic.magicdraw.diff.report.ReportVariables.ADDED_INFOS)
MODIFIED_INFOS
public static final [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) MODIFIED_INFOS
Will have a list of modification com.nomagic.magicdraw.diff.report.ElementReportInfo instances
See Also:
[Constant Field Values](../../../../../constant-values.html#com.nomagic.magicdraw.diff.report.ReportVariables.MODIFIED_INFOS)
REMOVED_INFOS
public static final [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) REMOVED_INFOS
Will have a list of removal com.nomagic.magicdraw.diff.report.ElementReportInfo instances
See Also:
[Constant Field Values](../../../../../constant-values.html#com.nomagic.magicdraw.diff.report.ReportVariables.REMOVED_INFOS)
SCOPE_NAME
public static final [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) SCOPE_NAME
Content history report template variable. Scope element's simple name
See Also:
[Constant Field Values](../../../../../constant-values.html#com.nomagic.magicdraw.diff.report.ReportVariables.SCOPE_NAME)
SCOPE_QNAME
public static final [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) SCOPE_QNAME
Content history report template variable. Scope element's qualified name
See Also:
[Constant Field Values](../../../../../constant-values.html#com.nomagic.magicdraw.diff.report.ReportVariables.SCOPE_QNAME)
SCOPE_TYPE
public static final [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) SCOPE_TYPE
Content history report template variable. Scope element's simple type
See Also:
[Constant Field Values](../../../../../constant-values.html#com.nomagic.magicdraw.diff.report.ReportVariables.SCOPE_TYPE)

========= END OF CLASS DATA =========

## EXACT JAVADOC MAIN HTML

````html
<main role="main">
<!-- ======== START OF CLASS DATA ======== -->
<div class="header">
<div class="sub-title"><span class="package-label-in-type">Package</span> <a href="package-summary.html">com.nomagic.magicdraw.diff.report</a></div>
<h1 class="title" title="Class ReportVariables">Class ReportVariables</h1>
</div>
<div class="inheritance" title="Inheritance Tree"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">java.lang.Object</a>
<div class="inheritance">com.nomagic.magicdraw.diff.report.ReportVariables</div>
</div>
<section class="class-description" id="class-description">
<hr/>
<div class="type-signature"><span class="annotations">@OpenApiAll
</span><span class="modifiers">public final class </span><span class="element-name type-name-label">ReportVariables</span>
<span class="extends-implements">extends <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a></span></div>
<div class="block">Report template variables</div>
</section>
<section class="summary">
<ul class="summary-list">
<!-- =========== FIELD SUMMARY =========== -->
<li>
<section class="field-summary" id="field-summary">
<h2>Field Summary</h2>
<div class="caption"><span>Fields</span></div>
<div class="summary-table three-column-summary">
<div class="table-header col-first">Modifier and Type</div>
<div class="table-header col-second">Field</div>
<div class="table-header col-last">Description</div>
<div class="col-first even-row-color"><code>static final <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second even-row-color"><code><a class="member-name-link" href="#ADDED_INFOS">ADDED_INFOS</a></code></div>
<div class="col-last even-row-color">
<div class="block">Will have a list of addition com.nomagic.magicdraw.diff.report.ElementReportInfo instances</div>
</div>
<div class="col-first odd-row-color"><code>static final <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second odd-row-color"><code><a class="member-name-link" href="#ANCESTOR_BRANCH">ANCESTOR_BRANCH</a></code></div>
<div class="col-last odd-row-color">
<div class="block">Ancestor project branch name</div>
</div>
<div class="col-first even-row-color"><code>static final <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second even-row-color"><code><a class="member-name-link" href="#ANCESTOR_DIAGRAM_COUNT">ANCESTOR_DIAGRAM_COUNT</a></code></div>
<div class="col-last even-row-color">
<div class="block">Ancestor project total diagram count</div>
</div>
<div class="col-first odd-row-color"><code>static final <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second odd-row-color"><code><a class="member-name-link" href="#ANCESTOR_DIAGRAM_LABEL">ANCESTOR_DIAGRAM_LABEL</a></code></div>
<div class="col-last odd-row-color">
<div class="block">Will have value "Base" when comparing, "Target" - when two merge, "Ancestor" - when three way merge</div>
</div>
<div class="col-first even-row-color"><code>static final <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second even-row-color"><code><a class="member-name-link" href="#ANCESTOR_ELEMENT_COUNT">ANCESTOR_ELEMENT_COUNT</a></code></div>
<div class="col-last even-row-color">
<div class="block">Ancestor project total element count</div>
</div>
<div class="col-first odd-row-color"><code>static final <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second odd-row-color"><code><a class="member-name-link" href="#ANCESTOR_PROJECT_NAME">ANCESTOR_PROJECT_NAME</a></code></div>
<div class="col-last odd-row-color">
<div class="block">Ancestor project name</div>
</div>
<div class="col-first even-row-color"><code>static final <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second even-row-color"><code><a class="member-name-link" href="#ANCESTOR_VERSION">ANCESTOR_VERSION</a></code></div>
<div class="col-last even-row-color">
<div class="block">Ancestor project version</div>
</div>
<div class="col-first odd-row-color"><code>static final <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second odd-row-color"><code><a class="member-name-link" href="#AUTHOR">AUTHOR</a></code></div>
<div class="col-last odd-row-color">
<div class="block">Project author name, or logged in twc user name when report is done for twc project,</div>
</div>
<div class="col-first even-row-color"><code>static final <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second even-row-color"><code><a class="member-name-link" href="#DATE">DATE</a></code></div>
<div class="col-last even-row-color">
<div class="block">Report creation date</div>
</div>
<div class="col-first odd-row-color"><code>static final <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second odd-row-color"><code><a class="member-name-link" href="#DIAGRAM_REPORT_INFOS">DIAGRAM_REPORT_INFOS</a></code></div>
<div class="col-last odd-row-color">
<div class="block">Will have a list of com.nomagic.magicdraw.diff.report.DiagramReportInfo instances</div>
</div>
<div class="col-first even-row-color"><code>static final <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second even-row-color"><code><a class="member-name-link" href="#ELEMENT_REPORT_INFOS">ELEMENT_REPORT_INFOS</a></code></div>
<div class="col-last even-row-color">
<div class="block">Will have a list of all com.nomagic.magicdraw.diff.report.ElementReportInfo instances</div>
</div>
<div class="col-first odd-row-color"><code>static final <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second odd-row-color"><code><a class="member-name-link" href="#FOOTER_DATE">FOOTER_DATE</a></code></div>
<div class="col-last odd-row-color">
<div class="block">Short format of report creation date</div>
</div>
<div class="col-first even-row-color"><code>static final <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second even-row-color"><code><a class="member-name-link" href="#FOOTER_YEAR">FOOTER_YEAR</a></code></div>
<div class="col-last even-row-color">
<div class="block">Year of the report creation</div>
</div>
<div class="col-first odd-row-color"><code>static final <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second odd-row-color"><code><a class="member-name-link" href="#IS_2WAY">IS_2WAY</a></code></div>
<div class="col-last odd-row-color">
<div class="block">True, when two way project merge is done</div>
</div>
<div class="col-first even-row-color"><code>static final <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second even-row-color"><code><a class="member-name-link" href="#IS_3WAY">IS_3WAY</a></code></div>
<div class="col-last even-row-color">
<div class="block">True, when three way project merge is done</div>
</div>
<div class="col-first odd-row-color"><code>static final <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second odd-row-color"><code><a class="member-name-link" href="#IS_COMPARE">IS_COMPARE</a></code></div>
<div class="col-last odd-row-color">
<div class="block">True, when two project compare is done</div>
</div>
<div class="col-first even-row-color"><code>static final <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second even-row-color"><code><a class="member-name-link" href="#IS_FULL_REPORT">IS_FULL_REPORT</a></code></div>
<div class="col-last even-row-color">
<div class="block">True, when report is done from full report template</div>
</div>
<div class="col-first odd-row-color"><code>static final <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second odd-row-color"><code><a class="member-name-link" href="#MODIFIED_INFOS">MODIFIED_INFOS</a></code></div>
<div class="col-last odd-row-color">
<div class="block">Will have a list of modification com.nomagic.magicdraw.diff.report.ElementReportInfo instances</div>
</div>
<div class="col-first even-row-color"><code>static final <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second even-row-color"><code><a class="member-name-link" href="#PROJECT">PROJECT</a></code></div>
<div class="col-last even-row-color">
<div class="block">Holds info from com.nomagic.magicdraw.core.Project instance of the target (when 2way or compare), or ancestor project</div>
</div>
<div class="col-first odd-row-color"><code>static final <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second odd-row-color"><code><a class="member-name-link" href="#REMOVED_INFOS">REMOVED_INFOS</a></code></div>
<div class="col-last odd-row-color">
<div class="block">Will have a list of removal com.nomagic.magicdraw.diff.report.ElementReportInfo instances</div>
</div>
<div class="col-first even-row-color"><code>static final <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second even-row-color"><code><a class="member-name-link" href="#REPORT_TYPE">REPORT_TYPE</a></code></div>
<div class="col-last even-row-color">
<div class="block">Holds info from com.nomagic.magicdraw.diff.report.ReportType instance</div>
</div>
<div class="col-first odd-row-color"><code>static final <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second odd-row-color"><code><a class="member-name-link" href="#SCOPE_NAME">SCOPE_NAME</a></code></div>
<div class="col-last odd-row-color">
<div class="block">Content history report template variable.</div>
</div>
<div class="col-first even-row-color"><code>static final <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second even-row-color"><code><a class="member-name-link" href="#SCOPE_QNAME">SCOPE_QNAME</a></code></div>
<div class="col-last even-row-color">
<div class="block">Content history report template variable.</div>
</div>
<div class="col-first odd-row-color"><code>static final <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second odd-row-color"><code><a class="member-name-link" href="#SCOPE_TYPE">SCOPE_TYPE</a></code></div>
<div class="col-last odd-row-color">
<div class="block">Content history report template variable.</div>
</div>
<div class="col-first even-row-color"><code>static final <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second even-row-color"><code><a class="member-name-link" href="#SOURCE_ADDED">SOURCE_ADDED</a></code></div>
<div class="col-last even-row-color">
<div class="block">Number of addition changes in source project</div>
</div>
<div class="col-first odd-row-color"><code>static final <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second odd-row-color"><code><a class="member-name-link" href="#SOURCE_ADDED_DIAGRAMS">SOURCE_ADDED_DIAGRAMS</a></code></div>
<div class="col-last odd-row-color">
<div class="block">Number of added diagrams in source project</div>
</div>
<div class="col-first even-row-color"><code>static final <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second even-row-color"><code><a class="member-name-link" href="#SOURCE_ADDED_SYMBOLS">SOURCE_ADDED_SYMBOLS</a></code></div>
<div class="col-last even-row-color">
<div class="block">Number of added symbols in source project</div>
</div>
<div class="col-first odd-row-color"><code>static final <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second odd-row-color"><code><a class="member-name-link" href="#SOURCE_BRANCH">SOURCE_BRANCH</a></code></div>
<div class="col-last odd-row-color">
<div class="block">Source project branch name</div>
</div>
<div class="col-first even-row-color"><code>static final <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second even-row-color"><code><a class="member-name-link" href="#SOURCE_DIAGRAM_COUNT">SOURCE_DIAGRAM_COUNT</a></code></div>
<div class="col-last even-row-color">
<div class="block">Source project total diagram count</div>
</div>
<div class="col-first odd-row-color"><code>static final <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second odd-row-color"><code><a class="member-name-link" href="#SOURCE_ELEMENT_COUNT">SOURCE_ELEMENT_COUNT</a></code></div>
<div class="col-last odd-row-color">
<div class="block">Source project total element count</div>
</div>
<div class="col-first even-row-color"><code>static final <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second even-row-color"><code><a class="member-name-link" href="#SOURCE_LABEL">SOURCE_LABEL</a></code></div>
<div class="col-last even-row-color">
<div class="block">Will have value "Compared" when comparing, and "Source" - when merging</div>
</div>
<div class="col-first odd-row-color"><code>static final <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second odd-row-color"><code><a class="member-name-link" href="#SOURCE_MODIFIED">SOURCE_MODIFIED</a></code></div>
<div class="col-last odd-row-color">
<div class="block">Number of modification changes in source project</div>
</div>
<div class="col-first even-row-color"><code>static final <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second even-row-color"><code><a class="member-name-link" href="#SOURCE_MODIFIED_DIAGRAMS">SOURCE_MODIFIED_DIAGRAMS</a></code></div>
<div class="col-last even-row-color">
<div class="block">Number of modified diagrams in source project</div>
</div>
<div class="col-first odd-row-color"><code>static final <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second odd-row-color"><code><a class="member-name-link" href="#SOURCE_MODIFIED_SYMBOLS">SOURCE_MODIFIED_SYMBOLS</a></code></div>
<div class="col-last odd-row-color">
<div class="block">Number of modified symbols in source project</div>
</div>
<div class="col-first even-row-color"><code>static final <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second even-row-color"><code><a class="member-name-link" href="#SOURCE_OVERALL">SOURCE_OVERALL</a></code></div>
<div class="col-last even-row-color">
<div class="block">Total number of addition, modification and removal changes in source project</div>
</div>
<div class="col-first odd-row-color"><code>static final <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second odd-row-color"><code><a class="member-name-link" href="#SOURCE_OVERALL_DIAGRAMS">SOURCE_OVERALL_DIAGRAMS</a></code></div>
<div class="col-last odd-row-color">
<div class="block">Total number of added, modified, deleted diagrams and symbols in source project</div>
</div>
<div class="col-first even-row-color"><code>static final <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second even-row-color"><code><a class="member-name-link" href="#SOURCE_PROJECT_NAME">SOURCE_PROJECT_NAME</a></code></div>
<div class="col-last even-row-color">
<div class="block">Source project name</div>
</div>
<div class="col-first odd-row-color"><code>static final <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second odd-row-color"><code><a class="member-name-link" href="#SOURCE_REMOVED">SOURCE_REMOVED</a></code></div>
<div class="col-last odd-row-color">
<div class="block">Number of removal changes in source project</div>
</div>
<div class="col-first even-row-color"><code>static final <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second even-row-color"><code><a class="member-name-link" href="#SOURCE_REMOVED_DIAGRAMS">SOURCE_REMOVED_DIAGRAMS</a></code></div>
<div class="col-last even-row-color">
<div class="block">Number of removed diagrams in source project</div>
</div>
<div class="col-first odd-row-color"><code>static final <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second odd-row-color"><code><a class="member-name-link" href="#SOURCE_REMOVED_SYMBOLS">SOURCE_REMOVED_SYMBOLS</a></code></div>
<div class="col-last odd-row-color">
<div class="block">Number of deleted symbols in source project</div>
</div>
<div class="col-first even-row-color"><code>static final <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second even-row-color"><code><a class="member-name-link" href="#SOURCE_VERSION">SOURCE_VERSION</a></code></div>
<div class="col-last even-row-color">
<div class="block">Source project version</div>
</div>
<div class="col-first odd-row-color"><code>static final <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second odd-row-color"><code><a class="member-name-link" href="#TARGET_ADDED">TARGET_ADDED</a></code></div>
<div class="col-last odd-row-color">
<div class="block">Number of addition changes in target project</div>
</div>
<div class="col-first even-row-color"><code>static final <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second even-row-color"><code><a class="member-name-link" href="#TARGET_ADDED_DIAGRAMS">TARGET_ADDED_DIAGRAMS</a></code></div>
<div class="col-last even-row-color">
<div class="block">Number of added diagrams in target project</div>
</div>
<div class="col-first odd-row-color"><code>static final <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second odd-row-color"><code><a class="member-name-link" href="#TARGET_ADDED_SYMBOLS">TARGET_ADDED_SYMBOLS</a></code></div>
<div class="col-last odd-row-color">
<div class="block">Number of added symbols in target project</div>
</div>
<div class="col-first even-row-color"><code>static final <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second even-row-color"><code><a class="member-name-link" href="#TARGET_BRANCH">TARGET_BRANCH</a></code></div>
<div class="col-last even-row-color">
<div class="block">Target project branch name</div>
</div>
<div class="col-first odd-row-color"><code>static final <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second odd-row-color"><code><a class="member-name-link" href="#TARGET_DIAGRAM_COUNT">TARGET_DIAGRAM_COUNT</a></code></div>
<div class="col-last odd-row-color">
<div class="block">Target project total diagram count</div>
</div>
<div class="col-first even-row-color"><code>static final <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second even-row-color"><code><a class="member-name-link" href="#TARGET_DIAGRAM_LABEL">TARGET_DIAGRAM_LABEL</a></code></div>
<div class="col-last even-row-color">
<div class="block">Will have value "Compared" when comparing, "Target" - when merging</div>
</div>
<div class="col-first odd-row-color"><code>static final <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second odd-row-color"><code><a class="member-name-link" href="#TARGET_ELEMENT_COUNT">TARGET_ELEMENT_COUNT</a></code></div>
<div class="col-last odd-row-color">
<div class="block">Target project total element count</div>
</div>
<div class="col-first even-row-color"><code>static final <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second even-row-color"><code><a class="member-name-link" href="#TARGET_LABEL">TARGET_LABEL</a></code></div>
<div class="col-last even-row-color">
<div class="block">Will have value "Base" when comparing, and "Target" - when merging</div>
</div>
<div class="col-first odd-row-color"><code>static final <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second odd-row-color"><code><a class="member-name-link" href="#TARGET_MODIFIED">TARGET_MODIFIED</a></code></div>
<div class="col-last odd-row-color">
<div class="block">Number of modification changes in target project</div>
</div>
<div class="col-first even-row-color"><code>static final <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second even-row-color"><code><a class="member-name-link" href="#TARGET_MODIFIED_DIAGRAMS">TARGET_MODIFIED_DIAGRAMS</a></code></div>
<div class="col-last even-row-color">
<div class="block">Number of modified diagrams in target project</div>
</div>
<div class="col-first odd-row-color"><code>static final <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second odd-row-color"><code><a class="member-name-link" href="#TARGET_MODIFIED_SYMBOLS">TARGET_MODIFIED_SYMBOLS</a></code></div>
<div class="col-last odd-row-color">
<div class="block">Number of modified symbols in target project</div>
</div>
<div class="col-first even-row-color"><code>static final <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second even-row-color"><code><a class="member-name-link" href="#TARGET_OVERALL">TARGET_OVERALL</a></code></div>
<div class="col-last even-row-color">
<div class="block">Total number of addition, modification and removal changes in target project</div>
</div>
<div class="col-first odd-row-color"><code>static final <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second odd-row-color"><code><a class="member-name-link" href="#TARGET_OVERALL_DIAGRAMS">TARGET_OVERALL_DIAGRAMS</a></code></div>
<div class="col-last odd-row-color">
<div class="block">Total number of added, modified, deleted diagrams and symbols in target project</div>
</div>
<div class="col-first even-row-color"><code>static final <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second even-row-color"><code><a class="member-name-link" href="#TARGET_PROJECT_NAME">TARGET_PROJECT_NAME</a></code></div>
<div class="col-last even-row-color">
<div class="block">Target project name</div>
</div>
<div class="col-first odd-row-color"><code>static final <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second odd-row-color"><code><a class="member-name-link" href="#TARGET_REMOVED">TARGET_REMOVED</a></code></div>
<div class="col-last odd-row-color">
<div class="block">Number of removal changes in target project</div>
</div>
<div class="col-first even-row-color"><code>static final <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second even-row-color"><code><a class="member-name-link" href="#TARGET_REMOVED_DIAGRAMS">TARGET_REMOVED_DIAGRAMS</a></code></div>
<div class="col-last even-row-color">
<div class="block">Number of removed diagrams in target project</div>
</div>
<div class="col-first odd-row-color"><code>static final <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second odd-row-color"><code><a class="member-name-link" href="#TARGET_REMOVED_SYMBOLS">TARGET_REMOVED_SYMBOLS</a></code></div>
<div class="col-last odd-row-color">
<div class="block">Number of deleted symbols in target project</div>
</div>
<div class="col-first even-row-color"><code>static final <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second even-row-color"><code><a class="member-name-link" href="#TARGET_VERSION">TARGET_VERSION</a></code></div>
<div class="col-last even-row-color">
<div class="block">Target project version</div>
</div>
<div class="col-first odd-row-color"><code>static final <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second odd-row-color"><code><a class="member-name-link" href="#TITLE">TITLE</a></code></div>
<div class="col-last odd-row-color">
<div class="block">Will have value "Comparison", when project compare is done, or "Merge" - when project merge</div>
</div>
</div>
</section>
</li>
<!-- ========== METHOD SUMMARY =========== -->
<li>
<section class="method-summary" id="method-summary">
<h2>Method Summary</h2>
<div class="inherited-list">
<h3 id="methods-inherited-from-class-java.lang.Object">Methods inherited from class java.lang.<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a></h3>
<code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#clone()" title="class or interface in java.lang">clone</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#equals(java.lang.Object)" title="class or interface in java.lang">equals</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#finalize()" title="class or interface in java.lang">finalize</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#getClass()" title="class or interface in java.lang">getClass</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#hashCode()" title="class or interface in java.lang">hashCode</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notify()" title="class or interface in java.lang">notify</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notifyAll()" title="class or interface in java.lang">notifyAll</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#toString()" title="class or interface in java.lang">toString</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait()" title="class or interface in java.lang">wait</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long)" title="class or interface in java.lang">wait</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long,int)" title="class or interface in java.lang">wait</a></code></div>
</section>
</li>
</ul>
</section>
<section class="details">
<ul class="details-list">
<!-- ============ FIELD DETAIL =========== -->
<li>
<section class="field-details" id="field-detail">
<h2>Field Details</h2>
<ul class="member-list">
<li>
<section class="detail" id="AUTHOR">
<h3>AUTHOR</h3>
<div class="member-signature"><span class="modifiers">public static final</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">AUTHOR</span></div>
<div class="block">Project author name, or logged in twc user name when report is done for twc project,</div>
<dl class="notes">
<dt>See Also:</dt>
<dd>
<ul class="see-list">
<li><a href="../../../../../constant-values.html#com.nomagic.magicdraw.diff.report.ReportVariables.AUTHOR">Constant Field Values</a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="DATE">
<h3>DATE</h3>
<div class="member-signature"><span class="modifiers">public static final</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">DATE</span></div>
<div class="block">Report creation date</div>
<dl class="notes">
<dt>See Also:</dt>
<dd>
<ul class="see-list">
<li><a href="../../../../../constant-values.html#com.nomagic.magicdraw.diff.report.ReportVariables.DATE">Constant Field Values</a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="FOOTER_DATE">
<h3>FOOTER_DATE</h3>
<div class="member-signature"><span class="modifiers">public static final</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">FOOTER_DATE</span></div>
<div class="block">Short format of report creation date</div>
<dl class="notes">
<dt>See Also:</dt>
<dd>
<ul class="see-list">
<li><a href="../../../../../constant-values.html#com.nomagic.magicdraw.diff.report.ReportVariables.FOOTER_DATE">Constant Field Values</a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="FOOTER_YEAR">
<h3>FOOTER_YEAR</h3>
<div class="member-signature"><span class="modifiers">public static final</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">FOOTER_YEAR</span></div>
<div class="block">Year of the report creation</div>
<dl class="notes">
<dt>See Also:</dt>
<dd>
<ul class="see-list">
<li><a href="../../../../../constant-values.html#com.nomagic.magicdraw.diff.report.ReportVariables.FOOTER_YEAR">Constant Field Values</a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="IS_COMPARE">
<h3>IS_COMPARE</h3>
<div class="member-signature"><span class="modifiers">public static final</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">IS_COMPARE</span></div>
<div class="block">True, when two project compare is done</div>
<dl class="notes">
<dt>See Also:</dt>
<dd>
<ul class="see-list">
<li><a href="../../../../../constant-values.html#com.nomagic.magicdraw.diff.report.ReportVariables.IS_COMPARE">Constant Field Values</a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="IS_2WAY">
<h3>IS_2WAY</h3>
<div class="member-signature"><span class="modifiers">public static final</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">IS_2WAY</span></div>
<div class="block">True, when two way project merge is done</div>
<dl class="notes">
<dt>See Also:</dt>
<dd>
<ul class="see-list">
<li><a href="../../../../../constant-values.html#com.nomagic.magicdraw.diff.report.ReportVariables.IS_2WAY">Constant Field Values</a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="IS_3WAY">
<h3>IS_3WAY</h3>
<div class="member-signature"><span class="modifiers">public static final</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">IS_3WAY</span></div>
<div class="block">True, when three way project merge is done</div>
<dl class="notes">
<dt>See Also:</dt>
<dd>
<ul class="see-list">
<li><a href="../../../../../constant-values.html#com.nomagic.magicdraw.diff.report.ReportVariables.IS_3WAY">Constant Field Values</a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="REPORT_TYPE">
<h3>REPORT_TYPE</h3>
<div class="member-signature"><span class="modifiers">public static final</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">REPORT_TYPE</span></div>
<div class="block">Holds info from com.nomagic.magicdraw.diff.report.ReportType instance</div>
<dl class="notes">
<dt>See Also:</dt>
<dd>
<ul class="see-list">
<li><a href="../../../../../constant-values.html#com.nomagic.magicdraw.diff.report.ReportVariables.REPORT_TYPE">Constant Field Values</a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="IS_FULL_REPORT">
<h3>IS_FULL_REPORT</h3>
<div class="member-signature"><span class="modifiers">public static final</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">IS_FULL_REPORT</span></div>
<div class="block">True, when report is done from full report template</div>
<dl class="notes">
<dt>See Also:</dt>
<dd>
<ul class="see-list">
<li><a href="../../../../../constant-values.html#com.nomagic.magicdraw.diff.report.ReportVariables.IS_FULL_REPORT">Constant Field Values</a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="TITLE">
<h3>TITLE</h3>
<div class="member-signature"><span class="modifiers">public static final</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">TITLE</span></div>
<div class="block">Will have value "Comparison", when project compare is done, or "Merge" - when project merge</div>
<dl class="notes">
<dt>See Also:</dt>
<dd>
<ul class="see-list">
<li><a href="../../../../../constant-values.html#com.nomagic.magicdraw.diff.report.ReportVariables.TITLE">Constant Field Values</a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="PROJECT">
<h3>PROJECT</h3>
<div class="member-signature"><span class="modifiers">public static final</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">PROJECT</span></div>
<div class="block">Holds info from com.nomagic.magicdraw.core.Project instance of the target (when 2way or compare), or ancestor project</div>
<dl class="notes">
<dt>See Also:</dt>
<dd>
<ul class="see-list">
<li><a href="../../../../../constant-values.html#com.nomagic.magicdraw.diff.report.ReportVariables.PROJECT">Constant Field Values</a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="TARGET_LABEL">
<h3>TARGET_LABEL</h3>
<div class="member-signature"><span class="modifiers">public static final</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">TARGET_LABEL</span></div>
<div class="block">Will have value "Base" when comparing, and "Target" - when merging</div>
<dl class="notes">
<dt>See Also:</dt>
<dd>
<ul class="see-list">
<li><a href="../../../../../constant-values.html#com.nomagic.magicdraw.diff.report.ReportVariables.TARGET_LABEL">Constant Field Values</a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="SOURCE_LABEL">
<h3>SOURCE_LABEL</h3>
<div class="member-signature"><span class="modifiers">public static final</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">SOURCE_LABEL</span></div>
<div class="block">Will have value "Compared" when comparing, and "Source" - when merging</div>
<dl class="notes">
<dt>See Also:</dt>
<dd>
<ul class="see-list">
<li><a href="../../../../../constant-values.html#com.nomagic.magicdraw.diff.report.ReportVariables.SOURCE_LABEL">Constant Field Values</a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="TARGET_PROJECT_NAME">
<h3>TARGET_PROJECT_NAME</h3>
<div class="member-signature"><span class="modifiers">public static final</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">TARGET_PROJECT_NAME</span></div>
<div class="block">Target project name</div>
<dl class="notes">
<dt>See Also:</dt>
<dd>
<ul class="see-list">
<li><a href="../../../../../constant-values.html#com.nomagic.magicdraw.diff.report.ReportVariables.TARGET_PROJECT_NAME">Constant Field Values</a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="TARGET_BRANCH">
<h3>TARGET_BRANCH</h3>
<div class="member-signature"><span class="modifiers">public static final</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">TARGET_BRANCH</span></div>
<div class="block">Target project branch name</div>
<dl class="notes">
<dt>See Also:</dt>
<dd>
<ul class="see-list">
<li><a href="../../../../../constant-values.html#com.nomagic.magicdraw.diff.report.ReportVariables.TARGET_BRANCH">Constant Field Values</a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="TARGET_VERSION">
<h3>TARGET_VERSION</h3>
<div class="member-signature"><span class="modifiers">public static final</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">TARGET_VERSION</span></div>
<div class="block">Target project version</div>
<dl class="notes">
<dt>See Also:</dt>
<dd>
<ul class="see-list">
<li><a href="../../../../../constant-values.html#com.nomagic.magicdraw.diff.report.ReportVariables.TARGET_VERSION">Constant Field Values</a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="TARGET_ELEMENT_COUNT">
<h3>TARGET_ELEMENT_COUNT</h3>
<div class="member-signature"><span class="modifiers">public static final</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">TARGET_ELEMENT_COUNT</span></div>
<div class="block">Target project total element count</div>
<dl class="notes">
<dt>See Also:</dt>
<dd>
<ul class="see-list">
<li><a href="../../../../../constant-values.html#com.nomagic.magicdraw.diff.report.ReportVariables.TARGET_ELEMENT_COUNT">Constant Field Values</a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="TARGET_DIAGRAM_COUNT">
<h3>TARGET_DIAGRAM_COUNT</h3>
<div class="member-signature"><span class="modifiers">public static final</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">TARGET_DIAGRAM_COUNT</span></div>
<div class="block">Target project total diagram count</div>
<dl class="notes">
<dt>See Also:</dt>
<dd>
<ul class="see-list">
<li><a href="../../../../../constant-values.html#com.nomagic.magicdraw.diff.report.ReportVariables.TARGET_DIAGRAM_COUNT">Constant Field Values</a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="SOURCE_PROJECT_NAME">
<h3>SOURCE_PROJECT_NAME</h3>
<div class="member-signature"><span class="modifiers">public static final</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">SOURCE_PROJECT_NAME</span></div>
<div class="block">Source project name</div>
<dl class="notes">
<dt>See Also:</dt>
<dd>
<ul class="see-list">
<li><a href="../../../../../constant-values.html#com.nomagic.magicdraw.diff.report.ReportVariables.SOURCE_PROJECT_NAME">Constant Field Values</a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="SOURCE_BRANCH">
<h3>SOURCE_BRANCH</h3>
<div class="member-signature"><span class="modifiers">public static final</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">SOURCE_BRANCH</span></div>
<div class="block">Source project branch name</div>
<dl class="notes">
<dt>See Also:</dt>
<dd>
<ul class="see-list">
<li><a href="../../../../../constant-values.html#com.nomagic.magicdraw.diff.report.ReportVariables.SOURCE_BRANCH">Constant Field Values</a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="SOURCE_VERSION">
<h3>SOURCE_VERSION</h3>
<div class="member-signature"><span class="modifiers">public static final</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">SOURCE_VERSION</span></div>
<div class="block">Source project version</div>
<dl class="notes">
<dt>See Also:</dt>
<dd>
<ul class="see-list">
<li><a href="../../../../../constant-values.html#com.nomagic.magicdraw.diff.report.ReportVariables.SOURCE_VERSION">Constant Field Values</a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="SOURCE_ELEMENT_COUNT">
<h3>SOURCE_ELEMENT_COUNT</h3>
<div class="member-signature"><span class="modifiers">public static final</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">SOURCE_ELEMENT_COUNT</span></div>
<div class="block">Source project total element count</div>
<dl class="notes">
<dt>See Also:</dt>
<dd>
<ul class="see-list">
<li><a href="../../../../../constant-values.html#com.nomagic.magicdraw.diff.report.ReportVariables.SOURCE_ELEMENT_COUNT">Constant Field Values</a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="SOURCE_DIAGRAM_COUNT">
<h3>SOURCE_DIAGRAM_COUNT</h3>
<div class="member-signature"><span class="modifiers">public static final</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">SOURCE_DIAGRAM_COUNT</span></div>
<div class="block">Source project total diagram count</div>
<dl class="notes">
<dt>See Also:</dt>
<dd>
<ul class="see-list">
<li><a href="../../../../../constant-values.html#com.nomagic.magicdraw.diff.report.ReportVariables.SOURCE_DIAGRAM_COUNT">Constant Field Values</a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="ANCESTOR_PROJECT_NAME">
<h3>ANCESTOR_PROJECT_NAME</h3>
<div class="member-signature"><span class="modifiers">public static final</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">ANCESTOR_PROJECT_NAME</span></div>
<div class="block">Ancestor project name</div>
<dl class="notes">
<dt>See Also:</dt>
<dd>
<ul class="see-list">
<li><a href="../../../../../constant-values.html#com.nomagic.magicdraw.diff.report.ReportVariables.ANCESTOR_PROJECT_NAME">Constant Field Values</a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="ANCESTOR_BRANCH">
<h3>ANCESTOR_BRANCH</h3>
<div class="member-signature"><span class="modifiers">public static final</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">ANCESTOR_BRANCH</span></div>
<div class="block">Ancestor project branch name</div>
<dl class="notes">
<dt>See Also:</dt>
<dd>
<ul class="see-list">
<li><a href="../../../../../constant-values.html#com.nomagic.magicdraw.diff.report.ReportVariables.ANCESTOR_BRANCH">Constant Field Values</a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="ANCESTOR_VERSION">
<h3>ANCESTOR_VERSION</h3>
<div class="member-signature"><span class="modifiers">public static final</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">ANCESTOR_VERSION</span></div>
<div class="block">Ancestor project version</div>
<dl class="notes">
<dt>See Also:</dt>
<dd>
<ul class="see-list">
<li><a href="../../../../../constant-values.html#com.nomagic.magicdraw.diff.report.ReportVariables.ANCESTOR_VERSION">Constant Field Values</a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="ANCESTOR_ELEMENT_COUNT">
<h3>ANCESTOR_ELEMENT_COUNT</h3>
<div class="member-signature"><span class="modifiers">public static final</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">ANCESTOR_ELEMENT_COUNT</span></div>
<div class="block">Ancestor project total element count</div>
<dl class="notes">
<dt>See Also:</dt>
<dd>
<ul class="see-list">
<li><a href="../../../../../constant-values.html#com.nomagic.magicdraw.diff.report.ReportVariables.ANCESTOR_ELEMENT_COUNT">Constant Field Values</a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="ANCESTOR_DIAGRAM_COUNT">
<h3>ANCESTOR_DIAGRAM_COUNT</h3>
<div class="member-signature"><span class="modifiers">public static final</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">ANCESTOR_DIAGRAM_COUNT</span></div>
<div class="block">Ancestor project total diagram count</div>
<dl class="notes">
<dt>See Also:</dt>
<dd>
<ul class="see-list">
<li><a href="../../../../../constant-values.html#com.nomagic.magicdraw.diff.report.ReportVariables.ANCESTOR_DIAGRAM_COUNT">Constant Field Values</a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="TARGET_ADDED">
<h3>TARGET_ADDED</h3>
<div class="member-signature"><span class="modifiers">public static final</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">TARGET_ADDED</span></div>
<div class="block">Number of addition changes in target project</div>
<dl class="notes">
<dt>See Also:</dt>
<dd>
<ul class="see-list">
<li><a href="../../../../../constant-values.html#com.nomagic.magicdraw.diff.report.ReportVariables.TARGET_ADDED">Constant Field Values</a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="TARGET_MODIFIED">
<h3>TARGET_MODIFIED</h3>
<div class="member-signature"><span class="modifiers">public static final</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">TARGET_MODIFIED</span></div>
<div class="block">Number of modification changes in target project</div>
<dl class="notes">
<dt>See Also:</dt>
<dd>
<ul class="see-list">
<li><a href="../../../../../constant-values.html#com.nomagic.magicdraw.diff.report.ReportVariables.TARGET_MODIFIED">Constant Field Values</a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="TARGET_REMOVED">
<h3>TARGET_REMOVED</h3>
<div class="member-signature"><span class="modifiers">public static final</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">TARGET_REMOVED</span></div>
<div class="block">Number of removal changes in target project</div>
<dl class="notes">
<dt>See Also:</dt>
<dd>
<ul class="see-list">
<li><a href="../../../../../constant-values.html#com.nomagic.magicdraw.diff.report.ReportVariables.TARGET_REMOVED">Constant Field Values</a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="TARGET_OVERALL">
<h3>TARGET_OVERALL</h3>
<div class="member-signature"><span class="modifiers">public static final</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">TARGET_OVERALL</span></div>
<div class="block">Total number of addition, modification and removal changes in target project</div>
<dl class="notes">
<dt>See Also:</dt>
<dd>
<ul class="see-list">
<li><a href="../../../../../constant-values.html#com.nomagic.magicdraw.diff.report.ReportVariables.TARGET_OVERALL">Constant Field Values</a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="SOURCE_ADDED">
<h3>SOURCE_ADDED</h3>
<div class="member-signature"><span class="modifiers">public static final</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">SOURCE_ADDED</span></div>
<div class="block">Number of addition changes in source project</div>
<dl class="notes">
<dt>See Also:</dt>
<dd>
<ul class="see-list">
<li><a href="../../../../../constant-values.html#com.nomagic.magicdraw.diff.report.ReportVariables.SOURCE_ADDED">Constant Field Values</a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="SOURCE_MODIFIED">
<h3>SOURCE_MODIFIED</h3>
<div class="member-signature"><span class="modifiers">public static final</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">SOURCE_MODIFIED</span></div>
<div class="block">Number of modification changes in source project</div>
<dl class="notes">
<dt>See Also:</dt>
<dd>
<ul class="see-list">
<li><a href="../../../../../constant-values.html#com.nomagic.magicdraw.diff.report.ReportVariables.SOURCE_MODIFIED">Constant Field Values</a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="SOURCE_REMOVED">
<h3>SOURCE_REMOVED</h3>
<div class="member-signature"><span class="modifiers">public static final</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">SOURCE_REMOVED</span></div>
<div class="block">Number of removal changes in source project</div>
<dl class="notes">
<dt>See Also:</dt>
<dd>
<ul class="see-list">
<li><a href="../../../../../constant-values.html#com.nomagic.magicdraw.diff.report.ReportVariables.SOURCE_REMOVED">Constant Field Values</a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="SOURCE_OVERALL">
<h3>SOURCE_OVERALL</h3>
<div class="member-signature"><span class="modifiers">public static final</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">SOURCE_OVERALL</span></div>
<div class="block">Total number of addition, modification and removal changes in source project</div>
<dl class="notes">
<dt>See Also:</dt>
<dd>
<ul class="see-list">
<li><a href="../../../../../constant-values.html#com.nomagic.magicdraw.diff.report.ReportVariables.SOURCE_OVERALL">Constant Field Values</a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="TARGET_ADDED_DIAGRAMS">
<h3>TARGET_ADDED_DIAGRAMS</h3>
<div class="member-signature"><span class="modifiers">public static final</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">TARGET_ADDED_DIAGRAMS</span></div>
<div class="block">Number of added diagrams in target project</div>
<dl class="notes">
<dt>See Also:</dt>
<dd>
<ul class="see-list">
<li><a href="../../../../../constant-values.html#com.nomagic.magicdraw.diff.report.ReportVariables.TARGET_ADDED_DIAGRAMS">Constant Field Values</a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="TARGET_MODIFIED_DIAGRAMS">
<h3>TARGET_MODIFIED_DIAGRAMS</h3>
<div class="member-signature"><span class="modifiers">public static final</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">TARGET_MODIFIED_DIAGRAMS</span></div>
<div class="block">Number of modified diagrams in target project</div>
<dl class="notes">
<dt>See Also:</dt>
<dd>
<ul class="see-list">
<li><a href="../../../../../constant-values.html#com.nomagic.magicdraw.diff.report.ReportVariables.TARGET_MODIFIED_DIAGRAMS">Constant Field Values</a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="TARGET_REMOVED_DIAGRAMS">
<h3>TARGET_REMOVED_DIAGRAMS</h3>
<div class="member-signature"><span class="modifiers">public static final</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">TARGET_REMOVED_DIAGRAMS</span></div>
<div class="block">Number of removed diagrams in target project</div>
<dl class="notes">
<dt>See Also:</dt>
<dd>
<ul class="see-list">
<li><a href="../../../../../constant-values.html#com.nomagic.magicdraw.diff.report.ReportVariables.TARGET_REMOVED_DIAGRAMS">Constant Field Values</a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="TARGET_ADDED_SYMBOLS">
<h3>TARGET_ADDED_SYMBOLS</h3>
<div class="member-signature"><span class="modifiers">public static final</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">TARGET_ADDED_SYMBOLS</span></div>
<div class="block">Number of added symbols in target project</div>
<dl class="notes">
<dt>See Also:</dt>
<dd>
<ul class="see-list">
<li><a href="../../../../../constant-values.html#com.nomagic.magicdraw.diff.report.ReportVariables.TARGET_ADDED_SYMBOLS">Constant Field Values</a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="TARGET_MODIFIED_SYMBOLS">
<h3>TARGET_MODIFIED_SYMBOLS</h3>
<div class="member-signature"><span class="modifiers">public static final</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">TARGET_MODIFIED_SYMBOLS</span></div>
<div class="block">Number of modified symbols in target project</div>
<dl class="notes">
<dt>See Also:</dt>
<dd>
<ul class="see-list">
<li><a href="../../../../../constant-values.html#com.nomagic.magicdraw.diff.report.ReportVariables.TARGET_MODIFIED_SYMBOLS">Constant Field Values</a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="TARGET_REMOVED_SYMBOLS">
<h3>TARGET_REMOVED_SYMBOLS</h3>
<div class="member-signature"><span class="modifiers">public static final</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">TARGET_REMOVED_SYMBOLS</span></div>
<div class="block">Number of deleted symbols in target project</div>
<dl class="notes">
<dt>See Also:</dt>
<dd>
<ul class="see-list">
<li><a href="../../../../../constant-values.html#com.nomagic.magicdraw.diff.report.ReportVariables.TARGET_REMOVED_SYMBOLS">Constant Field Values</a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="TARGET_OVERALL_DIAGRAMS">
<h3>TARGET_OVERALL_DIAGRAMS</h3>
<div class="member-signature"><span class="modifiers">public static final</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">TARGET_OVERALL_DIAGRAMS</span></div>
<div class="block">Total number of added, modified, deleted diagrams and symbols in target project</div>
<dl class="notes">
<dt>See Also:</dt>
<dd>
<ul class="see-list">
<li><a href="../../../../../constant-values.html#com.nomagic.magicdraw.diff.report.ReportVariables.TARGET_OVERALL_DIAGRAMS">Constant Field Values</a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="SOURCE_ADDED_DIAGRAMS">
<h3>SOURCE_ADDED_DIAGRAMS</h3>
<div class="member-signature"><span class="modifiers">public static final</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">SOURCE_ADDED_DIAGRAMS</span></div>
<div class="block">Number of added diagrams in source project</div>
<dl class="notes">
<dt>See Also:</dt>
<dd>
<ul class="see-list">
<li><a href="../../../../../constant-values.html#com.nomagic.magicdraw.diff.report.ReportVariables.SOURCE_ADDED_DIAGRAMS">Constant Field Values</a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="SOURCE_MODIFIED_DIAGRAMS">
<h3>SOURCE_MODIFIED_DIAGRAMS</h3>
<div class="member-signature"><span class="modifiers">public static final</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">SOURCE_MODIFIED_DIAGRAMS</span></div>
<div class="block">Number of modified diagrams in source project</div>
<dl class="notes">
<dt>See Also:</dt>
<dd>
<ul class="see-list">
<li><a href="../../../../../constant-values.html#com.nomagic.magicdraw.diff.report.ReportVariables.SOURCE_MODIFIED_DIAGRAMS">Constant Field Values</a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="SOURCE_REMOVED_DIAGRAMS">
<h3>SOURCE_REMOVED_DIAGRAMS</h3>
<div class="member-signature"><span class="modifiers">public static final</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">SOURCE_REMOVED_DIAGRAMS</span></div>
<div class="block">Number of removed diagrams in source project</div>
<dl class="notes">
<dt>See Also:</dt>
<dd>
<ul class="see-list">
<li><a href="../../../../../constant-values.html#com.nomagic.magicdraw.diff.report.ReportVariables.SOURCE_REMOVED_DIAGRAMS">Constant Field Values</a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="SOURCE_ADDED_SYMBOLS">
<h3>SOURCE_ADDED_SYMBOLS</h3>
<div class="member-signature"><span class="modifiers">public static final</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">SOURCE_ADDED_SYMBOLS</span></div>
<div class="block">Number of added symbols in source project</div>
<dl class="notes">
<dt>See Also:</dt>
<dd>
<ul class="see-list">
<li><a href="../../../../../constant-values.html#com.nomagic.magicdraw.diff.report.ReportVariables.SOURCE_ADDED_SYMBOLS">Constant Field Values</a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="SOURCE_MODIFIED_SYMBOLS">
<h3>SOURCE_MODIFIED_SYMBOLS</h3>
<div class="member-signature"><span class="modifiers">public static final</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">SOURCE_MODIFIED_SYMBOLS</span></div>
<div class="block">Number of modified symbols in source project</div>
<dl class="notes">
<dt>See Also:</dt>
<dd>
<ul class="see-list">
<li><a href="../../../../../constant-values.html#com.nomagic.magicdraw.diff.report.ReportVariables.SOURCE_MODIFIED_SYMBOLS">Constant Field Values</a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="SOURCE_REMOVED_SYMBOLS">
<h3>SOURCE_REMOVED_SYMBOLS</h3>
<div class="member-signature"><span class="modifiers">public static final</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">SOURCE_REMOVED_SYMBOLS</span></div>
<div class="block">Number of deleted symbols in source project</div>
<dl class="notes">
<dt>See Also:</dt>
<dd>
<ul class="see-list">
<li><a href="../../../../../constant-values.html#com.nomagic.magicdraw.diff.report.ReportVariables.SOURCE_REMOVED_SYMBOLS">Constant Field Values</a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="SOURCE_OVERALL_DIAGRAMS">
<h3>SOURCE_OVERALL_DIAGRAMS</h3>
<div class="member-signature"><span class="modifiers">public static final</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">SOURCE_OVERALL_DIAGRAMS</span></div>
<div class="block">Total number of added, modified, deleted diagrams and symbols in source project</div>
<dl class="notes">
<dt>See Also:</dt>
<dd>
<ul class="see-list">
<li><a href="../../../../../constant-values.html#com.nomagic.magicdraw.diff.report.ReportVariables.SOURCE_OVERALL_DIAGRAMS">Constant Field Values</a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="ANCESTOR_DIAGRAM_LABEL">
<h3>ANCESTOR_DIAGRAM_LABEL</h3>
<div class="member-signature"><span class="modifiers">public static final</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">ANCESTOR_DIAGRAM_LABEL</span></div>
<div class="block">Will have value "Base" when comparing, "Target" - when two merge, "Ancestor" - when three way merge</div>
<dl class="notes">
<dt>See Also:</dt>
<dd>
<ul class="see-list">
<li><a href="../../../../../constant-values.html#com.nomagic.magicdraw.diff.report.ReportVariables.ANCESTOR_DIAGRAM_LABEL">Constant Field Values</a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="TARGET_DIAGRAM_LABEL">
<h3>TARGET_DIAGRAM_LABEL</h3>
<div class="member-signature"><span class="modifiers">public static final</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">TARGET_DIAGRAM_LABEL</span></div>
<div class="block">Will have value "Compared" when comparing, "Target" - when merging</div>
<dl class="notes">
<dt>See Also:</dt>
<dd>
<ul class="see-list">
<li><a href="../../../../../constant-values.html#com.nomagic.magicdraw.diff.report.ReportVariables.TARGET_DIAGRAM_LABEL">Constant Field Values</a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="DIAGRAM_REPORT_INFOS">
<h3>DIAGRAM_REPORT_INFOS</h3>
<div class="member-signature"><span class="modifiers">public static final</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">DIAGRAM_REPORT_INFOS</span></div>
<div class="block">Will have a list of com.nomagic.magicdraw.diff.report.DiagramReportInfo instances</div>
<dl class="notes">
<dt>See Also:</dt>
<dd>
<ul class="see-list">
<li><a href="../../../../../constant-values.html#com.nomagic.magicdraw.diff.report.ReportVariables.DIAGRAM_REPORT_INFOS">Constant Field Values</a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="ELEMENT_REPORT_INFOS">
<h3>ELEMENT_REPORT_INFOS</h3>
<div class="member-signature"><span class="modifiers">public static final</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">ELEMENT_REPORT_INFOS</span></div>
<div class="block">Will have a list of all com.nomagic.magicdraw.diff.report.ElementReportInfo instances</div>
<dl class="notes">
<dt>See Also:</dt>
<dd>
<ul class="see-list">
<li><a href="../../../../../constant-values.html#com.nomagic.magicdraw.diff.report.ReportVariables.ELEMENT_REPORT_INFOS">Constant Field Values</a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="ADDED_INFOS">
<h3>ADDED_INFOS</h3>
<div class="member-signature"><span class="modifiers">public static final</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">ADDED_INFOS</span></div>
<div class="block">Will have a list of addition com.nomagic.magicdraw.diff.report.ElementReportInfo instances</div>
<dl class="notes">
<dt>See Also:</dt>
<dd>
<ul class="see-list">
<li><a href="../../../../../constant-values.html#com.nomagic.magicdraw.diff.report.ReportVariables.ADDED_INFOS">Constant Field Values</a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="MODIFIED_INFOS">
<h3>MODIFIED_INFOS</h3>
<div class="member-signature"><span class="modifiers">public static final</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">MODIFIED_INFOS</span></div>
<div class="block">Will have a list of modification com.nomagic.magicdraw.diff.report.ElementReportInfo instances</div>
<dl class="notes">
<dt>See Also:</dt>
<dd>
<ul class="see-list">
<li><a href="../../../../../constant-values.html#com.nomagic.magicdraw.diff.report.ReportVariables.MODIFIED_INFOS">Constant Field Values</a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="REMOVED_INFOS">
<h3>REMOVED_INFOS</h3>
<div class="member-signature"><span class="modifiers">public static final</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">REMOVED_INFOS</span></div>
<div class="block">Will have a list of removal com.nomagic.magicdraw.diff.report.ElementReportInfo instances</div>
<dl class="notes">
<dt>See Also:</dt>
<dd>
<ul class="see-list">
<li><a href="../../../../../constant-values.html#com.nomagic.magicdraw.diff.report.ReportVariables.REMOVED_INFOS">Constant Field Values</a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="SCOPE_NAME">
<h3>SCOPE_NAME</h3>
<div class="member-signature"><span class="modifiers">public static final</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">SCOPE_NAME</span></div>
<div class="block">Content history report template variable. Scope element's simple name</div>
<dl class="notes">
<dt>See Also:</dt>
<dd>
<ul class="see-list">
<li><a href="../../../../../constant-values.html#com.nomagic.magicdraw.diff.report.ReportVariables.SCOPE_NAME">Constant Field Values</a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="SCOPE_QNAME">
<h3>SCOPE_QNAME</h3>
<div class="member-signature"><span class="modifiers">public static final</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">SCOPE_QNAME</span></div>
<div class="block">Content history report template variable. Scope element's qualified name</div>
<dl class="notes">
<dt>See Also:</dt>
<dd>
<ul class="see-list">
<li><a href="../../../../../constant-values.html#com.nomagic.magicdraw.diff.report.ReportVariables.SCOPE_QNAME">Constant Field Values</a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="SCOPE_TYPE">
<h3>SCOPE_TYPE</h3>
<div class="member-signature"><span class="modifiers">public static final</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">SCOPE_TYPE</span></div>
<div class="block">Content history report template variable. Scope element's simple type</div>
<dl class="notes">
<dt>See Also:</dt>
<dd>
<ul class="see-list">
<li><a href="../../../../../constant-values.html#com.nomagic.magicdraw.diff.report.ReportVariables.SCOPE_TYPE">Constant Field Values</a></li>
</ul>
</dd>
</dl>
</section>
</li>
</ul>
</section>
</li>
</ul>
</section>
<!-- ========= END OF CLASS DATA ========= -->
</main>
````
