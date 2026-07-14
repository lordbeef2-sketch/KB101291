# JAVA OPENAPI: TemplateConstants (2026x Refresh1 API)

- source_url: https://jdocs.nomagic.com/2026xRefresh1/com/nomagic/magicreport/engine/TemplateConstants.html
- source_path: `com/nomagic/magicreport/engine/TemplateConstants.html`
- source_sha256: `b1d69ad8051ee562798a52879e2f1fc27909ad88ea9ed1283eac92a25320707b`
- captured_utc: `2026-07-14T16:46:12.078960+00:00`

## NORMALIZED JAVADOC CONTENT

======== START OF CLASS DATA ========

Package [com.nomagic.magicreport.engine](package-summary.html)

## Class TemplateConstants

[java.lang.Object](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html)
com.nomagic.magicreport.engine.TemplateConstants

@OpenApiAllpublic final classTemplateConstants
extends [Object](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html)

Contain constants value for template engine.

Since:
Jun 20, 2007

=========== FIELD SUMMARY =========== 
Field Summary
Fields
Modifier and Type
Field
Description
`static final [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html)`
`[ADD_ADDITIONAL_ELEMENT](#ADD_ADDITIONAL_ELEMENT)`
Use additional element and owned element to get children of element.
`static final [Pattern](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/regex/Pattern.html)`
`[CONTEXT_NAME_PATTERN](#CONTEXT_NAME_PATTERN)`
Contains valid pattern of context name.
`static final [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html)`
`[DEFAULT_INPUT_ENCODING](#DEFAULT_INPUT_ENCODING)`
Default template encoding.
`static final [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html)`
`[DEFAULT_OUTPUT_ENCODING](#DEFAULT_OUTPUT_ENCODING)`
Default report output encoding.
`static final [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html)`
`[DEFAULT_PROCESS_SIZE](#DEFAULT_PROCESS_SIZE)`
Default processing size.
`static final [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html)`
`[RTF_FORMAT](#RTF_FORMAT)`

`static final [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html)`
`[TEMPLATE_AUTO_IMAGE](#TEMPLATE_AUTO_IMAGE)`
Key for store report auto image.
`static final [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html)`
`[TEMPLATE_COMMENT](#TEMPLATE_COMMENT)`
Key for enable template comment.
`static final [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html)`
`[TEMPLATE_DOCX_APPLYCHILDHEADERFOOTER](#TEMPLATE_DOCX_APPLYCHILDHEADERFOOTER)`
Key to apply header/footer for child template to main template
`static final [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html)`
`[TEMPLATE_DOCX_CHECKSIZE](#TEMPLATE_DOCX_CHECKSIZE)`
Key to estimate docx output file size
`static final [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html)`
`[TEMPLATE_DOCX_CHECKSIZE_MAX](#TEMPLATE_DOCX_CHECKSIZE_MAX)`
Key to define max file size of DOCX
`static final [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html)`
`[TEMPLATE_DOCX_FORCEAPPLYCHILDSTYLE](#TEMPLATE_DOCX_FORCEAPPLYCHILDSTYLE)`
Key to apply style for child template when the style duplicate with parent style
`static final [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html)`
`[TEMPLATE_DOCX_IGNORECHILDSTYLE](#TEMPLATE_DOCX_IGNORECHILDSTYLE)`
Key for ignoring style list of child template when using include/includesection
`static final [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html)`
`[TEMPLATE_DOCX_IGNOREDUPCHILDSTYLE](#TEMPLATE_DOCX_IGNOREDUPCHILDSTYLE)`
Key for apply only list of styles of child that not duplicated with parent
`static final [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html)`
`[TEMPLATE_DOCX_NEWLINE_INSERTED](#TEMPLATE_DOCX_NEWLINE_INSERTED)`
Key to add line break or carriage return instead of line break from CharSequence in formatter
`static final [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html)`
`[TEMPLATE_FORCE_HTML](#TEMPLATE_FORCE_HTML)`
Key for enable engine to render all content in HTML format.
`static final [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html)`
`[TEMPLATE_ICON_RETINALSCALE](#TEMPLATE_ICON_RETINALSCALE)`
Key for using retina scaling
`static final [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html)`
`[TEMPLATE_IMAGE_FORMAT](#TEMPLATE_IMAGE_FORMAT)`
Key for store image format of output template.
`static final [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html)`
`[TEMPLATE_INPUT_ENCODING](#TEMPLATE_INPUT_ENCODING)`
Key for store report output encoding.
`static final [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html)`
`[TEMPLATE_INPUT_FILE](#TEMPLATE_INPUT_FILE)`
Key for store report input file.
`static final [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html)`
`[TEMPLATE_INPUT_FORMAT](#TEMPLATE_INPUT_FORMAT)`
Key for store report input format.
`static final [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html)`
`[TEMPLATE_INPUT_LOCATION](#TEMPLATE_INPUT_LOCATION)`
Key for store report input location.
`static final [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html)`
`[TEMPLATE_LATEST_INPUT_FILE](#TEMPLATE_LATEST_INPUT_FILE)`
Key for currently file location that is evaluated.
`static final [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html)`
`[TEMPLATE_LATEST_INPUT_LOCATION](#TEMPLATE_LATEST_INPUT_LOCATION)`

`static final [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html)`
`[TEMPLATE_LATEST_OUTPUT_FILE](#TEMPLATE_LATEST_OUTPUT_FILE)`

`static final [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html)`
`[TEMPLATE_LATEST_OUTPUT_LOCATION](#TEMPLATE_LATEST_OUTPUT_LOCATION)`

`static final [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html)`
`[TEMPLATE_MAIN_INPUT_FILE](#TEMPLATE_MAIN_INPUT_FILE)`
Key for store report input file.
`static final [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html)`
`[TEMPLATE_MAIN_INPUT_LOCATION](#TEMPLATE_MAIN_INPUT_LOCATION)`
Key for store report input location.
`static final [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html)`
`[TEMPLATE_MAIN_OUTPUT_FILE](#TEMPLATE_MAIN_OUTPUT_FILE)`
Key for store report output file.
`static final [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html)`
`[TEMPLATE_MAIN_OUTPUT_LOCATION](#TEMPLATE_MAIN_OUTPUT_LOCATION)`
Key for store report output file.
`static final [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html)`
`[TEMPLATE_NAME](#TEMPLATE_NAME)`
Key for store report template name.
`static final [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html)`
`[TEMPLATE_ODP_USE_VIRTUAL_NAME](#TEMPLATE_ODP_USE_VIRTUAL_NAME)`
Key for enable engine to replace ODP hyperlink to page name.
`static final [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html)`
`[TEMPLATE_OUTPUT_DPI](#TEMPLATE_OUTPUT_DPI)`
Key for store report output DPI.
`static final [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html)`
`[TEMPLATE_OUTPUT_ENCODING](#TEMPLATE_OUTPUT_ENCODING)`
Key for store report output encoding.
`static final [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html)`
`[TEMPLATE_OUTPUT_FILE](#TEMPLATE_OUTPUT_FILE)`
Key for store report output file.
`static final [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html)`
`[TEMPLATE_OUTPUT_FILENAME](#TEMPLATE_OUTPUT_FILENAME)`
Key for store report output file.
`static final [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html)`
`[TEMPLATE_OUTPUT_FORMAT](#TEMPLATE_OUTPUT_FORMAT)`
Key for store report output format.
`static final [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html)`
`[TEMPLATE_OUTPUT_IMAGE_DPI](#TEMPLATE_OUTPUT_IMAGE_DPI)`
Key for global image output DPI
`static final [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html)`
`[TEMPLATE_OUTPUT_IMAGE_DPI_LOCAL](#TEMPLATE_OUTPUT_IMAGE_DPI_LOCAL)`
Key for local image output DPI
`static final [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html)`
`[TEMPLATE_OUTPUT_LOCATION](#TEMPLATE_OUTPUT_LOCATION)`
Key for store report output location.
`static final [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html)`
`[TEMPLATE_OUTPUT_ON_BLANK_FIELD](#TEMPLATE_OUTPUT_ON_BLANK_FIELD)`
Keys for printing string if field value is null.
`static final [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html)`
`[TEMPLATE_OUTPUT_RESOURCES](#TEMPLATE_OUTPUT_RESOURCES)`
Key for store report output resources.
`static final [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html)`
`[TEMPLATE_POOL_SIZE](#TEMPLATE_POOL_SIZE)`
Key for pool size.
`static final [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html)`
`[TEMPLATE_PROCESS_LOCATION](#TEMPLATE_PROCESS_LOCATION)`
Key for process location property.
`static final [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html)`
`[TEMPLATE_PROCESS_SIZE](#TEMPLATE_PROCESS_SIZE)`
Key for size of process in memory.
`static final [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html)`
`[TEMPLATE_RTF_NEWLINE](#TEMPLATE_RTF_NEWLINE)`
Use additional element and owned element to get children of element.
`static final [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html)`
`[TEMPLATE_RTF_RSID](#TEMPLATE_RTF_RSID)`
Key for enable RTF RSID support.
`static final [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html)`
`[TEMPLATE_SKIP_HTML_ALL](#TEMPLATE_SKIP_HTML_ALL)`
Key for disable engine to render all HTML content to HTML format.
`static final [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html)`
`[TEMPLATE_TEST](#TEMPLATE_TEST)`
Flag for testing template
`static final [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html)`
`[TEMPLATE_TRIM_TRAIL_SPACE](#TEMPLATE_TRIM_TRAIL_SPACE)`
Trim trail spaces after Hash statement.
`static final [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html)`
`[TEMPLATE_XLSX_CHECKSIZE](#TEMPLATE_XLSX_CHECKSIZE)`
Key to estimate xlsx output file size
`static final [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html)`
`[TEMPLATE_XLSX_HTML_LINK](#TEMPLATE_XLSX_HTML_LINK)`
Key for selecting the first or last hyperlink in the HTML String of any cell, and apply the selected hyperlink to the cell.
 ========== METHOD SUMMARY =========== 
Method Summary
Methods inherited from class java.lang.[Object](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html)
`[clone](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#clone()), [equals](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#equals(java.lang.Object)), [finalize](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#finalize()), [getClass](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#getClass()), [hashCode](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#hashCode()), [notify](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#notify()), [notifyAll](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#notifyAll()), [toString](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#toString()), [wait](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#wait()), [wait](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#wait(long)), [wait](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#wait(long,int))`

============ FIELD DETAIL =========== 
Field Details
TEMPLATE_PROCESS_LOCATION
public static final [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) TEMPLATE_PROCESS_LOCATION
Key for process location property. A location of temporary directory for processing template. Template
 engine may require to create some temporary file or resources for evaluate the template.
See Also:
[Constant Field Values](../../../../constant-values.html#com.nomagic.magicreport.engine.TemplateConstants.TEMPLATE_PROCESS_LOCATION)
TEMPLATE_PROCESS_SIZE
public static final [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) TEMPLATE_PROCESS_SIZE
Key for size of process in memory. If template size is larger than this value process will go on file
 system.
See Also:
[Constant Field Values](../../../../constant-values.html#com.nomagic.magicreport.engine.TemplateConstants.TEMPLATE_PROCESS_SIZE)
TEMPLATE_POOL_SIZE
public static final [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) TEMPLATE_POOL_SIZE
Key for pool size. You can set the number of the process of [`ConcurrentTool`](ConcurrentTool.html) instance for template
 engine. Default value is 1.
 Increase this value, may encounter problem on non-concurrent support environment.
See Also:
[Constant Field Values](../../../../constant-values.html#com.nomagic.magicreport.engine.TemplateConstants.TEMPLATE_POOL_SIZE)
TEMPLATE_IMAGE_FORMAT
public static final [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) TEMPLATE_IMAGE_FORMAT
Key for store image format of output template.
See Also:
[Constant Field Values](../../../../constant-values.html#com.nomagic.magicreport.engine.TemplateConstants.TEMPLATE_IMAGE_FORMAT)
TEMPLATE_AUTO_IMAGE
public static final [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) TEMPLATE_AUTO_IMAGE
Key for store report auto image.
 0 = none
1 = fit to paper (large only)
2 = fit and rotate left (large only)
3 = fit and rotate right (large only)
See Also:
[Constant Field Values](../../../../constant-values.html#com.nomagic.magicreport.engine.TemplateConstants.TEMPLATE_AUTO_IMAGE)
TEMPLATE_INPUT_FILE
public static final [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) TEMPLATE_INPUT_FILE
Key for store report input file.
See Also:
[Constant Field Values](../../../../constant-values.html#com.nomagic.magicreport.engine.TemplateConstants.TEMPLATE_INPUT_FILE)
TEMPLATE_INPUT_LOCATION
public static final [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) TEMPLATE_INPUT_LOCATION
Key for store report input location.
See Also:
[Constant Field Values](../../../../constant-values.html#com.nomagic.magicreport.engine.TemplateConstants.TEMPLATE_INPUT_LOCATION)
TEMPLATE_MAIN_INPUT_FILE
public static final [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) TEMPLATE_MAIN_INPUT_FILE
Key for store report input file.
See Also:
[Constant Field Values](../../../../constant-values.html#com.nomagic.magicreport.engine.TemplateConstants.TEMPLATE_MAIN_INPUT_FILE)
TEMPLATE_MAIN_INPUT_LOCATION
public static final [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) TEMPLATE_MAIN_INPUT_LOCATION
Key for store report input location.
See Also:
[Constant Field Values](../../../../constant-values.html#com.nomagic.magicreport.engine.TemplateConstants.TEMPLATE_MAIN_INPUT_LOCATION)
TEMPLATE_INPUT_FORMAT
public static final [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) TEMPLATE_INPUT_FORMAT
Key for store report input format.
See Also:
[Constant Field Values](../../../../constant-values.html#com.nomagic.magicreport.engine.TemplateConstants.TEMPLATE_INPUT_FORMAT)
TEMPLATE_OUTPUT_ON_BLANK_FIELD
public static final [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) TEMPLATE_OUTPUT_ON_BLANK_FIELD
Keys for printing string if field value is null. If the variable reference $variable has no value, but you
 prefer a blank text field. Use `engine.setProperty("template.output.on.blank.field", "")` If this
 property is `null`, engine will print the reference $variable as text. By default this value is
 `null`
See Also:
[Constant Field Values](../../../../constant-values.html#com.nomagic.magicreport.engine.TemplateConstants.TEMPLATE_OUTPUT_ON_BLANK_FIELD)
TEMPLATE_INPUT_ENCODING
public static final [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) TEMPLATE_INPUT_ENCODING
Key for store report output encoding.
See Also:
[Constant Field Values](../../../../constant-values.html#com.nomagic.magicreport.engine.TemplateConstants.TEMPLATE_INPUT_ENCODING)
TEMPLATE_OUTPUT_FILE
public static final [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) TEMPLATE_OUTPUT_FILE
Key for store report output file.
See Also:
[Constant Field Values](../../../../constant-values.html#com.nomagic.magicreport.engine.TemplateConstants.TEMPLATE_OUTPUT_FILE)
TEMPLATE_OUTPUT_FILENAME
public static final [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) TEMPLATE_OUTPUT_FILENAME
Key for store report output file.
See Also:
[Constant Field Values](../../../../constant-values.html#com.nomagic.magicreport.engine.TemplateConstants.TEMPLATE_OUTPUT_FILENAME)
TEMPLATE_OUTPUT_LOCATION
public static final [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) TEMPLATE_OUTPUT_LOCATION
Key for store report output location.
See Also:
[Constant Field Values](../../../../constant-values.html#com.nomagic.magicreport.engine.TemplateConstants.TEMPLATE_OUTPUT_LOCATION)
TEMPLATE_MAIN_OUTPUT_FILE
public static final [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) TEMPLATE_MAIN_OUTPUT_FILE
Key for store report output file.
See Also:
[Constant Field Values](../../../../constant-values.html#com.nomagic.magicreport.engine.TemplateConstants.TEMPLATE_MAIN_OUTPUT_FILE)
TEMPLATE_MAIN_OUTPUT_LOCATION
public static final [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) TEMPLATE_MAIN_OUTPUT_LOCATION
Key for store report output file.
See Also:
[Constant Field Values](../../../../constant-values.html#com.nomagic.magicreport.engine.TemplateConstants.TEMPLATE_MAIN_OUTPUT_LOCATION)
TEMPLATE_OUTPUT_RESOURCES
public static final [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) TEMPLATE_OUTPUT_RESOURCES
Key for store report output resources.
See Also:
[Constant Field Values](../../../../constant-values.html#com.nomagic.magicreport.engine.TemplateConstants.TEMPLATE_OUTPUT_RESOURCES)
TEMPLATE_LATEST_INPUT_FILE
public static final [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) TEMPLATE_LATEST_INPUT_FILE
Key for currently file location that is evaluated.
See Also:
[Constant Field Values](../../../../constant-values.html#com.nomagic.magicreport.engine.TemplateConstants.TEMPLATE_LATEST_INPUT_FILE)
TEMPLATE_LATEST_INPUT_LOCATION
public static final [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) TEMPLATE_LATEST_INPUT_LOCATION
See Also:
[Constant Field Values](../../../../constant-values.html#com.nomagic.magicreport.engine.TemplateConstants.TEMPLATE_LATEST_INPUT_LOCATION)
TEMPLATE_LATEST_OUTPUT_FILE
public static final [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) TEMPLATE_LATEST_OUTPUT_FILE
See Also:
[Constant Field Values](../../../../constant-values.html#com.nomagic.magicreport.engine.TemplateConstants.TEMPLATE_LATEST_OUTPUT_FILE)
TEMPLATE_LATEST_OUTPUT_LOCATION
public static final [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) TEMPLATE_LATEST_OUTPUT_LOCATION
See Also:
[Constant Field Values](../../../../constant-values.html#com.nomagic.magicreport.engine.TemplateConstants.TEMPLATE_LATEST_OUTPUT_LOCATION)
TEMPLATE_OUTPUT_FORMAT
public static final [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) TEMPLATE_OUTPUT_FORMAT
Key for store report output format.
See Also:
[Constant Field Values](../../../../constant-values.html#com.nomagic.magicreport.engine.TemplateConstants.TEMPLATE_OUTPUT_FORMAT)
TEMPLATE_OUTPUT_ENCODING
public static final [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) TEMPLATE_OUTPUT_ENCODING
Key for store report output encoding.
See Also:
[Constant Field Values](../../../../constant-values.html#com.nomagic.magicreport.engine.TemplateConstants.TEMPLATE_OUTPUT_ENCODING)
TEMPLATE_OUTPUT_DPI
public static final [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) TEMPLATE_OUTPUT_DPI
Key for store report output DPI.
See Also:
[Constant Field Values](../../../../constant-values.html#com.nomagic.magicreport.engine.TemplateConstants.TEMPLATE_OUTPUT_DPI)
TEMPLATE_OUTPUT_IMAGE_DPI_LOCAL
public static final [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) TEMPLATE_OUTPUT_IMAGE_DPI_LOCAL
Key for local image output DPI
See Also:
[Constant Field Values](../../../../constant-values.html#com.nomagic.magicreport.engine.TemplateConstants.TEMPLATE_OUTPUT_IMAGE_DPI_LOCAL)
TEMPLATE_OUTPUT_IMAGE_DPI
public static final [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) TEMPLATE_OUTPUT_IMAGE_DPI
Key for global image output DPI
See Also:
[Constant Field Values](../../../../constant-values.html#com.nomagic.magicreport.engine.TemplateConstants.TEMPLATE_OUTPUT_IMAGE_DPI)
TEMPLATE_NAME
public static final [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) TEMPLATE_NAME
Key for store report template name.
See Also:
[Constant Field Values](../../../../constant-values.html#com.nomagic.magicreport.engine.TemplateConstants.TEMPLATE_NAME)
TEMPLATE_COMMENT
public static final [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) TEMPLATE_COMMENT
Key for enable template comment. The template may corrupt the template structure by remove all necessary tag
 between comment. Possible value of this property is `true` or `false` (Default: true)
See Also:
[Constant Field Values](../../../../constant-values.html#com.nomagic.magicreport.engine.TemplateConstants.TEMPLATE_COMMENT)
TEMPLATE_FORCE_HTML
public static final [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) TEMPLATE_FORCE_HTML
Key for enable engine to render all content in HTML format. Generally, the engine automatically render the
 content in HTML format if and only if the content started with <html/>. (Default: false)
See Also:
[Constant Field Values](../../../../constant-values.html#com.nomagic.magicreport.engine.TemplateConstants.TEMPLATE_FORCE_HTML)
TEMPLATE_SKIP_HTML_ALL
public static final [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) TEMPLATE_SKIP_HTML_ALL
Key for disable engine to render all HTML content to HTML format.
 This key has more priority than the content that started with <html/> or template.force.html. (Default: false)
See Also:
[Constant Field Values](../../../../constant-values.html#com.nomagic.magicreport.engine.TemplateConstants.TEMPLATE_SKIP_HTML_ALL)
TEMPLATE_TRIM_TRAIL_SPACE
public static final [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) TEMPLATE_TRIM_TRAIL_SPACE
Trim trail spaces after Hash statement.
See Also:
[Constant Field Values](../../../../constant-values.html#com.nomagic.magicreport.engine.TemplateConstants.TEMPLATE_TRIM_TRAIL_SPACE)
TEMPLATE_ICON_RETINALSCALE
public static final [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) TEMPLATE_ICON_RETINALSCALE
Key for using retina scaling
See Also:
[Constant Field Values](../../../../constant-values.html#com.nomagic.magicreport.engine.TemplateConstants.TEMPLATE_ICON_RETINALSCALE)
TEMPLATE_DOCX_IGNORECHILDSTYLE
public static final [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) TEMPLATE_DOCX_IGNORECHILDSTYLE
Key for ignoring style list of child template when using include/includesection
See Also:
[Constant Field Values](../../../../constant-values.html#com.nomagic.magicreport.engine.TemplateConstants.TEMPLATE_DOCX_IGNORECHILDSTYLE)
TEMPLATE_DOCX_IGNOREDUPCHILDSTYLE
public static final [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) TEMPLATE_DOCX_IGNOREDUPCHILDSTYLE
Key for apply only list of styles of child that not duplicated with parent
See Also:
[Constant Field Values](../../../../constant-values.html#com.nomagic.magicreport.engine.TemplateConstants.TEMPLATE_DOCX_IGNOREDUPCHILDSTYLE)
TEMPLATE_DOCX_FORCEAPPLYCHILDSTYLE
public static final [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) TEMPLATE_DOCX_FORCEAPPLYCHILDSTYLE
Key to apply style for child template when the style duplicate with parent style
See Also:
[Constant Field Values](../../../../constant-values.html#com.nomagic.magicreport.engine.TemplateConstants.TEMPLATE_DOCX_FORCEAPPLYCHILDSTYLE)
TEMPLATE_DOCX_APPLYCHILDHEADERFOOTER
public static final [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) TEMPLATE_DOCX_APPLYCHILDHEADERFOOTER
Key to apply header/footer for child template to main template
See Also:
[Constant Field Values](../../../../constant-values.html#com.nomagic.magicreport.engine.TemplateConstants.TEMPLATE_DOCX_APPLYCHILDHEADERFOOTER)
TEMPLATE_DOCX_NEWLINE_INSERTED
public static final [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) TEMPLATE_DOCX_NEWLINE_INSERTED
Key to add line break or carriage return instead of line break from CharSequence in formatter
See Also:
[Constant Field Values](../../../../constant-values.html#com.nomagic.magicreport.engine.TemplateConstants.TEMPLATE_DOCX_NEWLINE_INSERTED)
TEMPLATE_DOCX_CHECKSIZE
public static final [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) TEMPLATE_DOCX_CHECKSIZE
Key to estimate docx output file size
See Also:
[Constant Field Values](../../../../constant-values.html#com.nomagic.magicreport.engine.TemplateConstants.TEMPLATE_DOCX_CHECKSIZE)
TEMPLATE_XLSX_CHECKSIZE
public static final [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) TEMPLATE_XLSX_CHECKSIZE
Key to estimate xlsx output file size
See Also:
[Constant Field Values](../../../../constant-values.html#com.nomagic.magicreport.engine.TemplateConstants.TEMPLATE_XLSX_CHECKSIZE)
TEMPLATE_DOCX_CHECKSIZE_MAX
public static final [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) TEMPLATE_DOCX_CHECKSIZE_MAX
Key to define max file size of DOCX
See Also:
[Constant Field Values](../../../../constant-values.html#com.nomagic.magicreport.engine.TemplateConstants.TEMPLATE_DOCX_CHECKSIZE_MAX)
TEMPLATE_RTF_NEWLINE
public static final [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) TEMPLATE_RTF_NEWLINE
Use additional element and owned element to get children of element.
See Also:
[Constant Field Values](../../../../constant-values.html#com.nomagic.magicreport.engine.TemplateConstants.TEMPLATE_RTF_NEWLINE)
TEMPLATE_RTF_RSID
public static final [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) TEMPLATE_RTF_RSID
Key for enable RTF RSID support. In Word 2002, a new style of revision tracking was established. RSIDs
 (Revision Save IDs) indicate when text or a property was changed. This tracking id can make the generated
 document errors. Possible value of this property is `true` or `false` (Default: false)
See Also:
[Constant Field Values](../../../../constant-values.html#com.nomagic.magicreport.engine.TemplateConstants.TEMPLATE_RTF_RSID)
TEMPLATE_ODP_USE_VIRTUAL_NAME
public static final [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) TEMPLATE_ODP_USE_VIRTUAL_NAME
Key for enable engine to replace ODP hyperlink to page name. The OpenOffice.org will render page name
 pattern "page1", "page2",... and "Slide 1", "Slide 2",... with virtual name of "Slide 1", "Slide 2",... thus
 all the hyperlink pointing to these page name will not be working. If this property is `true`,
 the engine will replace hyperlink name virtual name. (Default: true)
See Also:
[Constant Field Values](../../../../constant-values.html#com.nomagic.magicreport.engine.TemplateConstants.TEMPLATE_ODP_USE_VIRTUAL_NAME)
TEMPLATE_XLSX_HTML_LINK
public static final [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) TEMPLATE_XLSX_HTML_LINK
Key for selecting the first or last hyperlink in the HTML String of any cell, and apply the selected hyperlink to the cell.
See Also:
[Constant Field Values](../../../../constant-values.html#com.nomagic.magicreport.engine.TemplateConstants.TEMPLATE_XLSX_HTML_LINK)
ADD_ADDITIONAL_ELEMENT
public static final [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) ADD_ADDITIONAL_ELEMENT
Use additional element and owned element to get children of element.
See Also:
[Constant Field Values](../../../../constant-values.html#com.nomagic.magicreport.engine.TemplateConstants.ADD_ADDITIONAL_ELEMENT)
CONTEXT_NAME_PATTERN
public static final [Pattern](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/regex/Pattern.html) CONTEXT_NAME_PATTERN
Contains valid pattern of context name.
DEFAULT_INPUT_ENCODING
public static final [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) DEFAULT_INPUT_ENCODING
Default template encoding.
See Also:
[Constant Field Values](../../../../constant-values.html#com.nomagic.magicreport.engine.TemplateConstants.DEFAULT_INPUT_ENCODING)
DEFAULT_OUTPUT_ENCODING
public static final [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) DEFAULT_OUTPUT_ENCODING
Default report output encoding.
See Also:
[Constant Field Values](../../../../constant-values.html#com.nomagic.magicreport.engine.TemplateConstants.DEFAULT_OUTPUT_ENCODING)
RTF_FORMAT
public static final [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) RTF_FORMAT
See Also:
[Constant Field Values](../../../../constant-values.html#com.nomagic.magicreport.engine.TemplateConstants.RTF_FORMAT)
DEFAULT_PROCESS_SIZE
public static final [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) DEFAULT_PROCESS_SIZE
Default processing size.
See Also:
[Constant Field Values](../../../../constant-values.html#com.nomagic.magicreport.engine.TemplateConstants.DEFAULT_PROCESS_SIZE)
TEMPLATE_TEST
public static final [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) TEMPLATE_TEST
Flag for testing template
See Also:
[Constant Field Values](../../../../constant-values.html#com.nomagic.magicreport.engine.TemplateConstants.TEMPLATE_TEST)

========= END OF CLASS DATA =========

## EXACT JAVADOC MAIN HTML

````html
<main role="main">
<!-- ======== START OF CLASS DATA ======== -->
<div class="header">
<div class="sub-title"><span class="package-label-in-type">Package</span> <a href="package-summary.html">com.nomagic.magicreport.engine</a></div>
<h1 class="title" title="Class TemplateConstants">Class TemplateConstants</h1>
</div>
<div class="inheritance" title="Inheritance Tree"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">java.lang.Object</a>
<div class="inheritance">com.nomagic.magicreport.engine.TemplateConstants</div>
</div>
<section class="class-description" id="class-description">
<hr/>
<div class="type-signature"><span class="annotations">@OpenApiAll
</span><span class="modifiers">public final class </span><span class="element-name type-name-label">TemplateConstants</span>
<span class="extends-implements">extends <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a></span></div>
<div class="block">Contain constants value for template engine.</div>
<dl class="notes">
<dt>Since:</dt>
<dd>Jun 20, 2007</dd>
</dl>
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
<div class="col-first even-row-color"><code>static final <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second even-row-color"><code><a class="member-name-link" href="#ADD_ADDITIONAL_ELEMENT">ADD_ADDITIONAL_ELEMENT</a></code></div>
<div class="col-last even-row-color">
<div class="block">Use additional element and owned element to get children of element.</div>
</div>
<div class="col-first odd-row-color"><code>static final <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/regex/Pattern.html" title="class or interface in java.util.regex">Pattern</a></code></div>
<div class="col-second odd-row-color"><code><a class="member-name-link" href="#CONTEXT_NAME_PATTERN">CONTEXT_NAME_PATTERN</a></code></div>
<div class="col-last odd-row-color">
<div class="block">Contains valid pattern of context name.</div>
</div>
<div class="col-first even-row-color"><code>static final <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second even-row-color"><code><a class="member-name-link" href="#DEFAULT_INPUT_ENCODING">DEFAULT_INPUT_ENCODING</a></code></div>
<div class="col-last even-row-color">
<div class="block">Default template encoding.</div>
</div>
<div class="col-first odd-row-color"><code>static final <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second odd-row-color"><code><a class="member-name-link" href="#DEFAULT_OUTPUT_ENCODING">DEFAULT_OUTPUT_ENCODING</a></code></div>
<div class="col-last odd-row-color">
<div class="block">Default report output encoding.</div>
</div>
<div class="col-first even-row-color"><code>static final <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second even-row-color"><code><a class="member-name-link" href="#DEFAULT_PROCESS_SIZE">DEFAULT_PROCESS_SIZE</a></code></div>
<div class="col-last even-row-color">
<div class="block">Default processing size.</div>
</div>
<div class="col-first odd-row-color"><code>static final <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second odd-row-color"><code><a class="member-name-link" href="#RTF_FORMAT">RTF_FORMAT</a></code></div>
<div class="col-last odd-row-color"> </div>
<div class="col-first even-row-color"><code>static final <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second even-row-color"><code><a class="member-name-link" href="#TEMPLATE_AUTO_IMAGE">TEMPLATE_AUTO_IMAGE</a></code></div>
<div class="col-last even-row-color">
<div class="block">Key for store report auto image.</div>
</div>
<div class="col-first odd-row-color"><code>static final <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second odd-row-color"><code><a class="member-name-link" href="#TEMPLATE_COMMENT">TEMPLATE_COMMENT</a></code></div>
<div class="col-last odd-row-color">
<div class="block">Key for enable template comment.</div>
</div>
<div class="col-first even-row-color"><code>static final <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second even-row-color"><code><a class="member-name-link" href="#TEMPLATE_DOCX_APPLYCHILDHEADERFOOTER">TEMPLATE_DOCX_APPLYCHILDHEADERFOOTER</a></code></div>
<div class="col-last even-row-color">
<div class="block">Key to apply header/footer for child template to main template</div>
</div>
<div class="col-first odd-row-color"><code>static final <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second odd-row-color"><code><a class="member-name-link" href="#TEMPLATE_DOCX_CHECKSIZE">TEMPLATE_DOCX_CHECKSIZE</a></code></div>
<div class="col-last odd-row-color">
<div class="block">Key to estimate docx output file size</div>
</div>
<div class="col-first even-row-color"><code>static final <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second even-row-color"><code><a class="member-name-link" href="#TEMPLATE_DOCX_CHECKSIZE_MAX">TEMPLATE_DOCX_CHECKSIZE_MAX</a></code></div>
<div class="col-last even-row-color">
<div class="block">Key to define max file size of DOCX</div>
</div>
<div class="col-first odd-row-color"><code>static final <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second odd-row-color"><code><a class="member-name-link" href="#TEMPLATE_DOCX_FORCEAPPLYCHILDSTYLE">TEMPLATE_DOCX_FORCEAPPLYCHILDSTYLE</a></code></div>
<div class="col-last odd-row-color">
<div class="block">Key to apply style for child template when the style duplicate with parent style</div>
</div>
<div class="col-first even-row-color"><code>static final <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second even-row-color"><code><a class="member-name-link" href="#TEMPLATE_DOCX_IGNORECHILDSTYLE">TEMPLATE_DOCX_IGNORECHILDSTYLE</a></code></div>
<div class="col-last even-row-color">
<div class="block">Key for ignoring style list of child template when using include/includesection</div>
</div>
<div class="col-first odd-row-color"><code>static final <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second odd-row-color"><code><a class="member-name-link" href="#TEMPLATE_DOCX_IGNOREDUPCHILDSTYLE">TEMPLATE_DOCX_IGNOREDUPCHILDSTYLE</a></code></div>
<div class="col-last odd-row-color">
<div class="block">Key for apply only list of styles of child that not duplicated with parent</div>
</div>
<div class="col-first even-row-color"><code>static final <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second even-row-color"><code><a class="member-name-link" href="#TEMPLATE_DOCX_NEWLINE_INSERTED">TEMPLATE_DOCX_NEWLINE_INSERTED</a></code></div>
<div class="col-last even-row-color">
<div class="block">Key to add line break or carriage return instead of line break from CharSequence in formatter</div>
</div>
<div class="col-first odd-row-color"><code>static final <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second odd-row-color"><code><a class="member-name-link" href="#TEMPLATE_FORCE_HTML">TEMPLATE_FORCE_HTML</a></code></div>
<div class="col-last odd-row-color">
<div class="block">Key for enable engine to render all content in HTML format.</div>
</div>
<div class="col-first even-row-color"><code>static final <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second even-row-color"><code><a class="member-name-link" href="#TEMPLATE_ICON_RETINALSCALE">TEMPLATE_ICON_RETINALSCALE</a></code></div>
<div class="col-last even-row-color">
<div class="block">Key for using retina scaling</div>
</div>
<div class="col-first odd-row-color"><code>static final <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second odd-row-color"><code><a class="member-name-link" href="#TEMPLATE_IMAGE_FORMAT">TEMPLATE_IMAGE_FORMAT</a></code></div>
<div class="col-last odd-row-color">
<div class="block">Key for store image format of output template.</div>
</div>
<div class="col-first even-row-color"><code>static final <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second even-row-color"><code><a class="member-name-link" href="#TEMPLATE_INPUT_ENCODING">TEMPLATE_INPUT_ENCODING</a></code></div>
<div class="col-last even-row-color">
<div class="block">Key for store report output encoding.</div>
</div>
<div class="col-first odd-row-color"><code>static final <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second odd-row-color"><code><a class="member-name-link" href="#TEMPLATE_INPUT_FILE">TEMPLATE_INPUT_FILE</a></code></div>
<div class="col-last odd-row-color">
<div class="block">Key for store report input file.</div>
</div>
<div class="col-first even-row-color"><code>static final <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second even-row-color"><code><a class="member-name-link" href="#TEMPLATE_INPUT_FORMAT">TEMPLATE_INPUT_FORMAT</a></code></div>
<div class="col-last even-row-color">
<div class="block">Key for store report input format.</div>
</div>
<div class="col-first odd-row-color"><code>static final <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second odd-row-color"><code><a class="member-name-link" href="#TEMPLATE_INPUT_LOCATION">TEMPLATE_INPUT_LOCATION</a></code></div>
<div class="col-last odd-row-color">
<div class="block">Key for store report input location.</div>
</div>
<div class="col-first even-row-color"><code>static final <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second even-row-color"><code><a class="member-name-link" href="#TEMPLATE_LATEST_INPUT_FILE">TEMPLATE_LATEST_INPUT_FILE</a></code></div>
<div class="col-last even-row-color">
<div class="block">Key for currently file location that is evaluated.</div>
</div>
<div class="col-first odd-row-color"><code>static final <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second odd-row-color"><code><a class="member-name-link" href="#TEMPLATE_LATEST_INPUT_LOCATION">TEMPLATE_LATEST_INPUT_LOCATION</a></code></div>
<div class="col-last odd-row-color"> </div>
<div class="col-first even-row-color"><code>static final <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second even-row-color"><code><a class="member-name-link" href="#TEMPLATE_LATEST_OUTPUT_FILE">TEMPLATE_LATEST_OUTPUT_FILE</a></code></div>
<div class="col-last even-row-color"> </div>
<div class="col-first odd-row-color"><code>static final <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second odd-row-color"><code><a class="member-name-link" href="#TEMPLATE_LATEST_OUTPUT_LOCATION">TEMPLATE_LATEST_OUTPUT_LOCATION</a></code></div>
<div class="col-last odd-row-color"> </div>
<div class="col-first even-row-color"><code>static final <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second even-row-color"><code><a class="member-name-link" href="#TEMPLATE_MAIN_INPUT_FILE">TEMPLATE_MAIN_INPUT_FILE</a></code></div>
<div class="col-last even-row-color">
<div class="block">Key for store report input file.</div>
</div>
<div class="col-first odd-row-color"><code>static final <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second odd-row-color"><code><a class="member-name-link" href="#TEMPLATE_MAIN_INPUT_LOCATION">TEMPLATE_MAIN_INPUT_LOCATION</a></code></div>
<div class="col-last odd-row-color">
<div class="block">Key for store report input location.</div>
</div>
<div class="col-first even-row-color"><code>static final <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second even-row-color"><code><a class="member-name-link" href="#TEMPLATE_MAIN_OUTPUT_FILE">TEMPLATE_MAIN_OUTPUT_FILE</a></code></div>
<div class="col-last even-row-color">
<div class="block">Key for store report output file.</div>
</div>
<div class="col-first odd-row-color"><code>static final <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second odd-row-color"><code><a class="member-name-link" href="#TEMPLATE_MAIN_OUTPUT_LOCATION">TEMPLATE_MAIN_OUTPUT_LOCATION</a></code></div>
<div class="col-last odd-row-color">
<div class="block">Key for store report output file.</div>
</div>
<div class="col-first even-row-color"><code>static final <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second even-row-color"><code><a class="member-name-link" href="#TEMPLATE_NAME">TEMPLATE_NAME</a></code></div>
<div class="col-last even-row-color">
<div class="block">Key for store report template name.</div>
</div>
<div class="col-first odd-row-color"><code>static final <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second odd-row-color"><code><a class="member-name-link" href="#TEMPLATE_ODP_USE_VIRTUAL_NAME">TEMPLATE_ODP_USE_VIRTUAL_NAME</a></code></div>
<div class="col-last odd-row-color">
<div class="block">Key for enable engine to replace ODP hyperlink to page name.</div>
</div>
<div class="col-first even-row-color"><code>static final <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second even-row-color"><code><a class="member-name-link" href="#TEMPLATE_OUTPUT_DPI">TEMPLATE_OUTPUT_DPI</a></code></div>
<div class="col-last even-row-color">
<div class="block">Key for store report output DPI.</div>
</div>
<div class="col-first odd-row-color"><code>static final <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second odd-row-color"><code><a class="member-name-link" href="#TEMPLATE_OUTPUT_ENCODING">TEMPLATE_OUTPUT_ENCODING</a></code></div>
<div class="col-last odd-row-color">
<div class="block">Key for store report output encoding.</div>
</div>
<div class="col-first even-row-color"><code>static final <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second even-row-color"><code><a class="member-name-link" href="#TEMPLATE_OUTPUT_FILE">TEMPLATE_OUTPUT_FILE</a></code></div>
<div class="col-last even-row-color">
<div class="block">Key for store report output file.</div>
</div>
<div class="col-first odd-row-color"><code>static final <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second odd-row-color"><code><a class="member-name-link" href="#TEMPLATE_OUTPUT_FILENAME">TEMPLATE_OUTPUT_FILENAME</a></code></div>
<div class="col-last odd-row-color">
<div class="block">Key for store report output file.</div>
</div>
<div class="col-first even-row-color"><code>static final <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second even-row-color"><code><a class="member-name-link" href="#TEMPLATE_OUTPUT_FORMAT">TEMPLATE_OUTPUT_FORMAT</a></code></div>
<div class="col-last even-row-color">
<div class="block">Key for store report output format.</div>
</div>
<div class="col-first odd-row-color"><code>static final <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second odd-row-color"><code><a class="member-name-link" href="#TEMPLATE_OUTPUT_IMAGE_DPI">TEMPLATE_OUTPUT_IMAGE_DPI</a></code></div>
<div class="col-last odd-row-color">
<div class="block">Key for global image output DPI</div>
</div>
<div class="col-first even-row-color"><code>static final <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second even-row-color"><code><a class="member-name-link" href="#TEMPLATE_OUTPUT_IMAGE_DPI_LOCAL">TEMPLATE_OUTPUT_IMAGE_DPI_LOCAL</a></code></div>
<div class="col-last even-row-color">
<div class="block">Key for local image output DPI</div>
</div>
<div class="col-first odd-row-color"><code>static final <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second odd-row-color"><code><a class="member-name-link" href="#TEMPLATE_OUTPUT_LOCATION">TEMPLATE_OUTPUT_LOCATION</a></code></div>
<div class="col-last odd-row-color">
<div class="block">Key for store report output location.</div>
</div>
<div class="col-first even-row-color"><code>static final <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second even-row-color"><code><a class="member-name-link" href="#TEMPLATE_OUTPUT_ON_BLANK_FIELD">TEMPLATE_OUTPUT_ON_BLANK_FIELD</a></code></div>
<div class="col-last even-row-color">
<div class="block">Keys for printing string if field value is null.</div>
</div>
<div class="col-first odd-row-color"><code>static final <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second odd-row-color"><code><a class="member-name-link" href="#TEMPLATE_OUTPUT_RESOURCES">TEMPLATE_OUTPUT_RESOURCES</a></code></div>
<div class="col-last odd-row-color">
<div class="block">Key for store report output resources.</div>
</div>
<div class="col-first even-row-color"><code>static final <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second even-row-color"><code><a class="member-name-link" href="#TEMPLATE_POOL_SIZE">TEMPLATE_POOL_SIZE</a></code></div>
<div class="col-last even-row-color">
<div class="block">Key for pool size.</div>
</div>
<div class="col-first odd-row-color"><code>static final <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second odd-row-color"><code><a class="member-name-link" href="#TEMPLATE_PROCESS_LOCATION">TEMPLATE_PROCESS_LOCATION</a></code></div>
<div class="col-last odd-row-color">
<div class="block">Key for process location property.</div>
</div>
<div class="col-first even-row-color"><code>static final <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second even-row-color"><code><a class="member-name-link" href="#TEMPLATE_PROCESS_SIZE">TEMPLATE_PROCESS_SIZE</a></code></div>
<div class="col-last even-row-color">
<div class="block">Key for size of process in memory.</div>
</div>
<div class="col-first odd-row-color"><code>static final <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second odd-row-color"><code><a class="member-name-link" href="#TEMPLATE_RTF_NEWLINE">TEMPLATE_RTF_NEWLINE</a></code></div>
<div class="col-last odd-row-color">
<div class="block">Use additional element and owned element to get children of element.</div>
</div>
<div class="col-first even-row-color"><code>static final <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second even-row-color"><code><a class="member-name-link" href="#TEMPLATE_RTF_RSID">TEMPLATE_RTF_RSID</a></code></div>
<div class="col-last even-row-color">
<div class="block">Key for enable RTF RSID support.</div>
</div>
<div class="col-first odd-row-color"><code>static final <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second odd-row-color"><code><a class="member-name-link" href="#TEMPLATE_SKIP_HTML_ALL">TEMPLATE_SKIP_HTML_ALL</a></code></div>
<div class="col-last odd-row-color">
<div class="block">Key for disable engine to render all HTML content to HTML format.</div>
</div>
<div class="col-first even-row-color"><code>static final <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second even-row-color"><code><a class="member-name-link" href="#TEMPLATE_TEST">TEMPLATE_TEST</a></code></div>
<div class="col-last even-row-color">
<div class="block">Flag for testing template</div>
</div>
<div class="col-first odd-row-color"><code>static final <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second odd-row-color"><code><a class="member-name-link" href="#TEMPLATE_TRIM_TRAIL_SPACE">TEMPLATE_TRIM_TRAIL_SPACE</a></code></div>
<div class="col-last odd-row-color">
<div class="block">Trim trail spaces after Hash statement.</div>
</div>
<div class="col-first even-row-color"><code>static final <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second even-row-color"><code><a class="member-name-link" href="#TEMPLATE_XLSX_CHECKSIZE">TEMPLATE_XLSX_CHECKSIZE</a></code></div>
<div class="col-last even-row-color">
<div class="block">Key to estimate xlsx output file size</div>
</div>
<div class="col-first odd-row-color"><code>static final <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second odd-row-color"><code><a class="member-name-link" href="#TEMPLATE_XLSX_HTML_LINK">TEMPLATE_XLSX_HTML_LINK</a></code></div>
<div class="col-last odd-row-color">
<div class="block">Key for selecting the first or last hyperlink in the HTML String of any cell, and apply the selected hyperlink to the cell.</div>
</div>
</div>
</section>
</li>
<!-- ========== METHOD SUMMARY =========== -->
<li>
<section class="method-summary" id="method-summary">
<h2>Method Summary</h2>
<div class="inherited-list">
<h3 id="methods-inherited-from-class-java.lang.Object">Methods inherited from class java.lang.<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a></h3>
<code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#clone()" title="class or interface in java.lang">clone</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#equals(java.lang.Object)" title="class or interface in java.lang">equals</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#finalize()" title="class or interface in java.lang">finalize</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#getClass()" title="class or interface in java.lang">getClass</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#hashCode()" title="class or interface in java.lang">hashCode</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#notify()" title="class or interface in java.lang">notify</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#notifyAll()" title="class or interface in java.lang">notifyAll</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#toString()" title="class or interface in java.lang">toString</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#wait()" title="class or interface in java.lang">wait</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#wait(long)" title="class or interface in java.lang">wait</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#wait(long,int)" title="class or interface in java.lang">wait</a></code></div>
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
<section class="detail" id="TEMPLATE_PROCESS_LOCATION">
<h3>TEMPLATE_PROCESS_LOCATION</h3>
<div class="member-signature"><span class="modifiers">public static final</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">TEMPLATE_PROCESS_LOCATION</span></div>
<div class="block">Key for process location property. A location of temporary directory for processing template. Template
 engine may require to create some temporary file or resources for evaluate the template.</div>
<dl class="notes">
<dt>See Also:</dt>
<dd>
<ul class="tag-list">
<li><a href="../../../../constant-values.html#com.nomagic.magicreport.engine.TemplateConstants.TEMPLATE_PROCESS_LOCATION">Constant Field Values</a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="TEMPLATE_PROCESS_SIZE">
<h3>TEMPLATE_PROCESS_SIZE</h3>
<div class="member-signature"><span class="modifiers">public static final</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">TEMPLATE_PROCESS_SIZE</span></div>
<div class="block">Key for size of process in memory. If template size is larger than this value process will go on file
 system.</div>
<dl class="notes">
<dt>See Also:</dt>
<dd>
<ul class="tag-list">
<li><a href="../../../../constant-values.html#com.nomagic.magicreport.engine.TemplateConstants.TEMPLATE_PROCESS_SIZE">Constant Field Values</a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="TEMPLATE_POOL_SIZE">
<h3>TEMPLATE_POOL_SIZE</h3>
<div class="member-signature"><span class="modifiers">public static final</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">TEMPLATE_POOL_SIZE</span></div>
<div class="block">Key for pool size. You can set the number of the process of <a href="ConcurrentTool.html" title="class in com.nomagic.magicreport.engine"><code>ConcurrentTool</code></a> instance for template
 engine. Default value is 1.
 <p>
 Increase this value, may encounter problem on non-concurrent support environment.</p></div>
<dl class="notes">
<dt>See Also:</dt>
<dd>
<ul class="tag-list">
<li><a href="../../../../constant-values.html#com.nomagic.magicreport.engine.TemplateConstants.TEMPLATE_POOL_SIZE">Constant Field Values</a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="TEMPLATE_IMAGE_FORMAT">
<h3>TEMPLATE_IMAGE_FORMAT</h3>
<div class="member-signature"><span class="modifiers">public static final</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">TEMPLATE_IMAGE_FORMAT</span></div>
<div class="block">Key for store image format of output template.</div>
<dl class="notes">
<dt>See Also:</dt>
<dd>
<ul class="tag-list">
<li><a href="../../../../constant-values.html#com.nomagic.magicreport.engine.TemplateConstants.TEMPLATE_IMAGE_FORMAT">Constant Field Values</a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="TEMPLATE_AUTO_IMAGE">
<h3>TEMPLATE_AUTO_IMAGE</h3>
<div class="member-signature"><span class="modifiers">public static final</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">TEMPLATE_AUTO_IMAGE</span></div>
<div class="block">Key for store report auto image.
 <ul>
<li>0 = none</li>
<li>1 = fit to paper (large only)</li>
<li>2 = fit and rotate left (large only)</li>
<li>3 = fit and rotate right (large only)</li>
</ul></div>
<dl class="notes">
<dt>See Also:</dt>
<dd>
<ul class="tag-list">
<li><a href="../../../../constant-values.html#com.nomagic.magicreport.engine.TemplateConstants.TEMPLATE_AUTO_IMAGE">Constant Field Values</a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="TEMPLATE_INPUT_FILE">
<h3>TEMPLATE_INPUT_FILE</h3>
<div class="member-signature"><span class="modifiers">public static final</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">TEMPLATE_INPUT_FILE</span></div>
<div class="block">Key for store report input file.</div>
<dl class="notes">
<dt>See Also:</dt>
<dd>
<ul class="tag-list">
<li><a href="../../../../constant-values.html#com.nomagic.magicreport.engine.TemplateConstants.TEMPLATE_INPUT_FILE">Constant Field Values</a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="TEMPLATE_INPUT_LOCATION">
<h3>TEMPLATE_INPUT_LOCATION</h3>
<div class="member-signature"><span class="modifiers">public static final</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">TEMPLATE_INPUT_LOCATION</span></div>
<div class="block">Key for store report input location.</div>
<dl class="notes">
<dt>See Also:</dt>
<dd>
<ul class="tag-list">
<li><a href="../../../../constant-values.html#com.nomagic.magicreport.engine.TemplateConstants.TEMPLATE_INPUT_LOCATION">Constant Field Values</a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="TEMPLATE_MAIN_INPUT_FILE">
<h3>TEMPLATE_MAIN_INPUT_FILE</h3>
<div class="member-signature"><span class="modifiers">public static final</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">TEMPLATE_MAIN_INPUT_FILE</span></div>
<div class="block">Key for store report input file.</div>
<dl class="notes">
<dt>See Also:</dt>
<dd>
<ul class="tag-list">
<li><a href="../../../../constant-values.html#com.nomagic.magicreport.engine.TemplateConstants.TEMPLATE_MAIN_INPUT_FILE">Constant Field Values</a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="TEMPLATE_MAIN_INPUT_LOCATION">
<h3>TEMPLATE_MAIN_INPUT_LOCATION</h3>
<div class="member-signature"><span class="modifiers">public static final</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">TEMPLATE_MAIN_INPUT_LOCATION</span></div>
<div class="block">Key for store report input location.</div>
<dl class="notes">
<dt>See Also:</dt>
<dd>
<ul class="tag-list">
<li><a href="../../../../constant-values.html#com.nomagic.magicreport.engine.TemplateConstants.TEMPLATE_MAIN_INPUT_LOCATION">Constant Field Values</a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="TEMPLATE_INPUT_FORMAT">
<h3>TEMPLATE_INPUT_FORMAT</h3>
<div class="member-signature"><span class="modifiers">public static final</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">TEMPLATE_INPUT_FORMAT</span></div>
<div class="block">Key for store report input format.</div>
<dl class="notes">
<dt>See Also:</dt>
<dd>
<ul class="tag-list">
<li><a href="../../../../constant-values.html#com.nomagic.magicreport.engine.TemplateConstants.TEMPLATE_INPUT_FORMAT">Constant Field Values</a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="TEMPLATE_OUTPUT_ON_BLANK_FIELD">
<h3>TEMPLATE_OUTPUT_ON_BLANK_FIELD</h3>
<div class="member-signature"><span class="modifiers">public static final</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">TEMPLATE_OUTPUT_ON_BLANK_FIELD</span></div>
<div class="block">Keys for printing string if field value is null. If the variable reference $variable has no value, but you
 prefer a blank text field. Use <code>engine.setProperty("template.output.on.blank.field", "")</code> If this
 property is <code>null</code>, engine will print the reference $variable as text. By default this value is
 <code>null</code></div>
<dl class="notes">
<dt>See Also:</dt>
<dd>
<ul class="tag-list">
<li><a href="../../../../constant-values.html#com.nomagic.magicreport.engine.TemplateConstants.TEMPLATE_OUTPUT_ON_BLANK_FIELD">Constant Field Values</a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="TEMPLATE_INPUT_ENCODING">
<h3>TEMPLATE_INPUT_ENCODING</h3>
<div class="member-signature"><span class="modifiers">public static final</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">TEMPLATE_INPUT_ENCODING</span></div>
<div class="block">Key for store report output encoding.</div>
<dl class="notes">
<dt>See Also:</dt>
<dd>
<ul class="tag-list">
<li><a href="../../../../constant-values.html#com.nomagic.magicreport.engine.TemplateConstants.TEMPLATE_INPUT_ENCODING">Constant Field Values</a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="TEMPLATE_OUTPUT_FILE">
<h3>TEMPLATE_OUTPUT_FILE</h3>
<div class="member-signature"><span class="modifiers">public static final</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">TEMPLATE_OUTPUT_FILE</span></div>
<div class="block">Key for store report output file.</div>
<dl class="notes">
<dt>See Also:</dt>
<dd>
<ul class="tag-list">
<li><a href="../../../../constant-values.html#com.nomagic.magicreport.engine.TemplateConstants.TEMPLATE_OUTPUT_FILE">Constant Field Values</a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="TEMPLATE_OUTPUT_FILENAME">
<h3>TEMPLATE_OUTPUT_FILENAME</h3>
<div class="member-signature"><span class="modifiers">public static final</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">TEMPLATE_OUTPUT_FILENAME</span></div>
<div class="block">Key for store report output file.</div>
<dl class="notes">
<dt>See Also:</dt>
<dd>
<ul class="tag-list">
<li><a href="../../../../constant-values.html#com.nomagic.magicreport.engine.TemplateConstants.TEMPLATE_OUTPUT_FILENAME">Constant Field Values</a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="TEMPLATE_OUTPUT_LOCATION">
<h3>TEMPLATE_OUTPUT_LOCATION</h3>
<div class="member-signature"><span class="modifiers">public static final</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">TEMPLATE_OUTPUT_LOCATION</span></div>
<div class="block">Key for store report output location.</div>
<dl class="notes">
<dt>See Also:</dt>
<dd>
<ul class="tag-list">
<li><a href="../../../../constant-values.html#com.nomagic.magicreport.engine.TemplateConstants.TEMPLATE_OUTPUT_LOCATION">Constant Field Values</a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="TEMPLATE_MAIN_OUTPUT_FILE">
<h3>TEMPLATE_MAIN_OUTPUT_FILE</h3>
<div class="member-signature"><span class="modifiers">public static final</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">TEMPLATE_MAIN_OUTPUT_FILE</span></div>
<div class="block">Key for store report output file.</div>
<dl class="notes">
<dt>See Also:</dt>
<dd>
<ul class="tag-list">
<li><a href="../../../../constant-values.html#com.nomagic.magicreport.engine.TemplateConstants.TEMPLATE_MAIN_OUTPUT_FILE">Constant Field Values</a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="TEMPLATE_MAIN_OUTPUT_LOCATION">
<h3>TEMPLATE_MAIN_OUTPUT_LOCATION</h3>
<div class="member-signature"><span class="modifiers">public static final</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">TEMPLATE_MAIN_OUTPUT_LOCATION</span></div>
<div class="block">Key for store report output file.</div>
<dl class="notes">
<dt>See Also:</dt>
<dd>
<ul class="tag-list">
<li><a href="../../../../constant-values.html#com.nomagic.magicreport.engine.TemplateConstants.TEMPLATE_MAIN_OUTPUT_LOCATION">Constant Field Values</a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="TEMPLATE_OUTPUT_RESOURCES">
<h3>TEMPLATE_OUTPUT_RESOURCES</h3>
<div class="member-signature"><span class="modifiers">public static final</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">TEMPLATE_OUTPUT_RESOURCES</span></div>
<div class="block">Key for store report output resources.</div>
<dl class="notes">
<dt>See Also:</dt>
<dd>
<ul class="tag-list">
<li><a href="../../../../constant-values.html#com.nomagic.magicreport.engine.TemplateConstants.TEMPLATE_OUTPUT_RESOURCES">Constant Field Values</a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="TEMPLATE_LATEST_INPUT_FILE">
<h3>TEMPLATE_LATEST_INPUT_FILE</h3>
<div class="member-signature"><span class="modifiers">public static final</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">TEMPLATE_LATEST_INPUT_FILE</span></div>
<div class="block">Key for currently file location that is evaluated.</div>
<dl class="notes">
<dt>See Also:</dt>
<dd>
<ul class="tag-list">
<li><a href="../../../../constant-values.html#com.nomagic.magicreport.engine.TemplateConstants.TEMPLATE_LATEST_INPUT_FILE">Constant Field Values</a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="TEMPLATE_LATEST_INPUT_LOCATION">
<h3>TEMPLATE_LATEST_INPUT_LOCATION</h3>
<div class="member-signature"><span class="modifiers">public static final</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">TEMPLATE_LATEST_INPUT_LOCATION</span></div>
<dl class="notes">
<dt>See Also:</dt>
<dd>
<ul class="tag-list">
<li><a href="../../../../constant-values.html#com.nomagic.magicreport.engine.TemplateConstants.TEMPLATE_LATEST_INPUT_LOCATION">Constant Field Values</a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="TEMPLATE_LATEST_OUTPUT_FILE">
<h3>TEMPLATE_LATEST_OUTPUT_FILE</h3>
<div class="member-signature"><span class="modifiers">public static final</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">TEMPLATE_LATEST_OUTPUT_FILE</span></div>
<dl class="notes">
<dt>See Also:</dt>
<dd>
<ul class="tag-list">
<li><a href="../../../../constant-values.html#com.nomagic.magicreport.engine.TemplateConstants.TEMPLATE_LATEST_OUTPUT_FILE">Constant Field Values</a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="TEMPLATE_LATEST_OUTPUT_LOCATION">
<h3>TEMPLATE_LATEST_OUTPUT_LOCATION</h3>
<div class="member-signature"><span class="modifiers">public static final</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">TEMPLATE_LATEST_OUTPUT_LOCATION</span></div>
<dl class="notes">
<dt>See Also:</dt>
<dd>
<ul class="tag-list">
<li><a href="../../../../constant-values.html#com.nomagic.magicreport.engine.TemplateConstants.TEMPLATE_LATEST_OUTPUT_LOCATION">Constant Field Values</a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="TEMPLATE_OUTPUT_FORMAT">
<h3>TEMPLATE_OUTPUT_FORMAT</h3>
<div class="member-signature"><span class="modifiers">public static final</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">TEMPLATE_OUTPUT_FORMAT</span></div>
<div class="block">Key for store report output format.</div>
<dl class="notes">
<dt>See Also:</dt>
<dd>
<ul class="tag-list">
<li><a href="../../../../constant-values.html#com.nomagic.magicreport.engine.TemplateConstants.TEMPLATE_OUTPUT_FORMAT">Constant Field Values</a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="TEMPLATE_OUTPUT_ENCODING">
<h3>TEMPLATE_OUTPUT_ENCODING</h3>
<div class="member-signature"><span class="modifiers">public static final</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">TEMPLATE_OUTPUT_ENCODING</span></div>
<div class="block">Key for store report output encoding.</div>
<dl class="notes">
<dt>See Also:</dt>
<dd>
<ul class="tag-list">
<li><a href="../../../../constant-values.html#com.nomagic.magicreport.engine.TemplateConstants.TEMPLATE_OUTPUT_ENCODING">Constant Field Values</a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="TEMPLATE_OUTPUT_DPI">
<h3>TEMPLATE_OUTPUT_DPI</h3>
<div class="member-signature"><span class="modifiers">public static final</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">TEMPLATE_OUTPUT_DPI</span></div>
<div class="block">Key for store report output DPI.</div>
<dl class="notes">
<dt>See Also:</dt>
<dd>
<ul class="tag-list">
<li><a href="../../../../constant-values.html#com.nomagic.magicreport.engine.TemplateConstants.TEMPLATE_OUTPUT_DPI">Constant Field Values</a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="TEMPLATE_OUTPUT_IMAGE_DPI_LOCAL">
<h3>TEMPLATE_OUTPUT_IMAGE_DPI_LOCAL</h3>
<div class="member-signature"><span class="modifiers">public static final</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">TEMPLATE_OUTPUT_IMAGE_DPI_LOCAL</span></div>
<div class="block">Key for local image output DPI</div>
<dl class="notes">
<dt>See Also:</dt>
<dd>
<ul class="tag-list">
<li><a href="../../../../constant-values.html#com.nomagic.magicreport.engine.TemplateConstants.TEMPLATE_OUTPUT_IMAGE_DPI_LOCAL">Constant Field Values</a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="TEMPLATE_OUTPUT_IMAGE_DPI">
<h3>TEMPLATE_OUTPUT_IMAGE_DPI</h3>
<div class="member-signature"><span class="modifiers">public static final</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">TEMPLATE_OUTPUT_IMAGE_DPI</span></div>
<div class="block">Key for global image output DPI</div>
<dl class="notes">
<dt>See Also:</dt>
<dd>
<ul class="tag-list">
<li><a href="../../../../constant-values.html#com.nomagic.magicreport.engine.TemplateConstants.TEMPLATE_OUTPUT_IMAGE_DPI">Constant Field Values</a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="TEMPLATE_NAME">
<h3>TEMPLATE_NAME</h3>
<div class="member-signature"><span class="modifiers">public static final</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">TEMPLATE_NAME</span></div>
<div class="block">Key for store report template name.</div>
<dl class="notes">
<dt>See Also:</dt>
<dd>
<ul class="tag-list">
<li><a href="../../../../constant-values.html#com.nomagic.magicreport.engine.TemplateConstants.TEMPLATE_NAME">Constant Field Values</a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="TEMPLATE_COMMENT">
<h3>TEMPLATE_COMMENT</h3>
<div class="member-signature"><span class="modifiers">public static final</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">TEMPLATE_COMMENT</span></div>
<div class="block">Key for enable template comment. The template may corrupt the template structure by remove all necessary tag
 between comment. Possible value of this property is <code>true</code> or <code>false</code> (Default: true)</div>
<dl class="notes">
<dt>See Also:</dt>
<dd>
<ul class="tag-list">
<li><a href="../../../../constant-values.html#com.nomagic.magicreport.engine.TemplateConstants.TEMPLATE_COMMENT">Constant Field Values</a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="TEMPLATE_FORCE_HTML">
<h3>TEMPLATE_FORCE_HTML</h3>
<div class="member-signature"><span class="modifiers">public static final</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">TEMPLATE_FORCE_HTML</span></div>
<div class="block">Key for enable engine to render all content in HTML format. Generally, the engine automatically render the
 content in HTML format if and only if the content started with &lt;html/&gt;. (Default: false)</div>
<dl class="notes">
<dt>See Also:</dt>
<dd>
<ul class="tag-list">
<li><a href="../../../../constant-values.html#com.nomagic.magicreport.engine.TemplateConstants.TEMPLATE_FORCE_HTML">Constant Field Values</a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="TEMPLATE_SKIP_HTML_ALL">
<h3>TEMPLATE_SKIP_HTML_ALL</h3>
<div class="member-signature"><span class="modifiers">public static final</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">TEMPLATE_SKIP_HTML_ALL</span></div>
<div class="block">Key for disable engine to render all HTML content to HTML format.
 This key has more priority than the content that started with &lt;html/&gt; or template.force.html. (Default: false)</div>
<dl class="notes">
<dt>See Also:</dt>
<dd>
<ul class="tag-list">
<li><a href="../../../../constant-values.html#com.nomagic.magicreport.engine.TemplateConstants.TEMPLATE_SKIP_HTML_ALL">Constant Field Values</a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="TEMPLATE_TRIM_TRAIL_SPACE">
<h3>TEMPLATE_TRIM_TRAIL_SPACE</h3>
<div class="member-signature"><span class="modifiers">public static final</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">TEMPLATE_TRIM_TRAIL_SPACE</span></div>
<div class="block">Trim trail spaces after Hash statement.</div>
<dl class="notes">
<dt>See Also:</dt>
<dd>
<ul class="tag-list">
<li><a href="../../../../constant-values.html#com.nomagic.magicreport.engine.TemplateConstants.TEMPLATE_TRIM_TRAIL_SPACE">Constant Field Values</a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="TEMPLATE_ICON_RETINALSCALE">
<h3>TEMPLATE_ICON_RETINALSCALE</h3>
<div class="member-signature"><span class="modifiers">public static final</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">TEMPLATE_ICON_RETINALSCALE</span></div>
<div class="block">Key for using retina scaling</div>
<dl class="notes">
<dt>See Also:</dt>
<dd>
<ul class="tag-list">
<li><a href="../../../../constant-values.html#com.nomagic.magicreport.engine.TemplateConstants.TEMPLATE_ICON_RETINALSCALE">Constant Field Values</a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="TEMPLATE_DOCX_IGNORECHILDSTYLE">
<h3>TEMPLATE_DOCX_IGNORECHILDSTYLE</h3>
<div class="member-signature"><span class="modifiers">public static final</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">TEMPLATE_DOCX_IGNORECHILDSTYLE</span></div>
<div class="block">Key for ignoring style list of child template when using include/includesection</div>
<dl class="notes">
<dt>See Also:</dt>
<dd>
<ul class="tag-list">
<li><a href="../../../../constant-values.html#com.nomagic.magicreport.engine.TemplateConstants.TEMPLATE_DOCX_IGNORECHILDSTYLE">Constant Field Values</a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="TEMPLATE_DOCX_IGNOREDUPCHILDSTYLE">
<h3>TEMPLATE_DOCX_IGNOREDUPCHILDSTYLE</h3>
<div class="member-signature"><span class="modifiers">public static final</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">TEMPLATE_DOCX_IGNOREDUPCHILDSTYLE</span></div>
<div class="block">Key for apply only list of styles of child that not duplicated with parent</div>
<dl class="notes">
<dt>See Also:</dt>
<dd>
<ul class="tag-list">
<li><a href="../../../../constant-values.html#com.nomagic.magicreport.engine.TemplateConstants.TEMPLATE_DOCX_IGNOREDUPCHILDSTYLE">Constant Field Values</a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="TEMPLATE_DOCX_FORCEAPPLYCHILDSTYLE">
<h3>TEMPLATE_DOCX_FORCEAPPLYCHILDSTYLE</h3>
<div class="member-signature"><span class="modifiers">public static final</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">TEMPLATE_DOCX_FORCEAPPLYCHILDSTYLE</span></div>
<div class="block">Key to apply style for child template when the style duplicate with parent style</div>
<dl class="notes">
<dt>See Also:</dt>
<dd>
<ul class="tag-list">
<li><a href="../../../../constant-values.html#com.nomagic.magicreport.engine.TemplateConstants.TEMPLATE_DOCX_FORCEAPPLYCHILDSTYLE">Constant Field Values</a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="TEMPLATE_DOCX_APPLYCHILDHEADERFOOTER">
<h3>TEMPLATE_DOCX_APPLYCHILDHEADERFOOTER</h3>
<div class="member-signature"><span class="modifiers">public static final</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">TEMPLATE_DOCX_APPLYCHILDHEADERFOOTER</span></div>
<div class="block">Key to apply header/footer for child template to main template</div>
<dl class="notes">
<dt>See Also:</dt>
<dd>
<ul class="tag-list">
<li><a href="../../../../constant-values.html#com.nomagic.magicreport.engine.TemplateConstants.TEMPLATE_DOCX_APPLYCHILDHEADERFOOTER">Constant Field Values</a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="TEMPLATE_DOCX_NEWLINE_INSERTED">
<h3>TEMPLATE_DOCX_NEWLINE_INSERTED</h3>
<div class="member-signature"><span class="modifiers">public static final</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">TEMPLATE_DOCX_NEWLINE_INSERTED</span></div>
<div class="block">Key to add line break or carriage return instead of line break from CharSequence in formatter</div>
<dl class="notes">
<dt>See Also:</dt>
<dd>
<ul class="tag-list">
<li><a href="../../../../constant-values.html#com.nomagic.magicreport.engine.TemplateConstants.TEMPLATE_DOCX_NEWLINE_INSERTED">Constant Field Values</a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="TEMPLATE_DOCX_CHECKSIZE">
<h3>TEMPLATE_DOCX_CHECKSIZE</h3>
<div class="member-signature"><span class="modifiers">public static final</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">TEMPLATE_DOCX_CHECKSIZE</span></div>
<div class="block">Key to estimate docx output file size</div>
<dl class="notes">
<dt>See Also:</dt>
<dd>
<ul class="tag-list">
<li><a href="../../../../constant-values.html#com.nomagic.magicreport.engine.TemplateConstants.TEMPLATE_DOCX_CHECKSIZE">Constant Field Values</a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="TEMPLATE_XLSX_CHECKSIZE">
<h3>TEMPLATE_XLSX_CHECKSIZE</h3>
<div class="member-signature"><span class="modifiers">public static final</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">TEMPLATE_XLSX_CHECKSIZE</span></div>
<div class="block">Key to estimate xlsx output file size</div>
<dl class="notes">
<dt>See Also:</dt>
<dd>
<ul class="tag-list">
<li><a href="../../../../constant-values.html#com.nomagic.magicreport.engine.TemplateConstants.TEMPLATE_XLSX_CHECKSIZE">Constant Field Values</a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="TEMPLATE_DOCX_CHECKSIZE_MAX">
<h3>TEMPLATE_DOCX_CHECKSIZE_MAX</h3>
<div class="member-signature"><span class="modifiers">public static final</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">TEMPLATE_DOCX_CHECKSIZE_MAX</span></div>
<div class="block">Key to define max file size of DOCX</div>
<dl class="notes">
<dt>See Also:</dt>
<dd>
<ul class="tag-list">
<li><a href="../../../../constant-values.html#com.nomagic.magicreport.engine.TemplateConstants.TEMPLATE_DOCX_CHECKSIZE_MAX">Constant Field Values</a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="TEMPLATE_RTF_NEWLINE">
<h3>TEMPLATE_RTF_NEWLINE</h3>
<div class="member-signature"><span class="modifiers">public static final</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">TEMPLATE_RTF_NEWLINE</span></div>
<div class="block">Use additional element and owned element to get children of element.</div>
<dl class="notes">
<dt>See Also:</dt>
<dd>
<ul class="tag-list">
<li><a href="../../../../constant-values.html#com.nomagic.magicreport.engine.TemplateConstants.TEMPLATE_RTF_NEWLINE">Constant Field Values</a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="TEMPLATE_RTF_RSID">
<h3>TEMPLATE_RTF_RSID</h3>
<div class="member-signature"><span class="modifiers">public static final</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">TEMPLATE_RTF_RSID</span></div>
<div class="block">Key for enable RTF RSID support. In Word 2002, a new style of revision tracking was established. RSIDs
 (Revision Save IDs) indicate when text or a property was changed. This tracking id can make the generated
 document errors. Possible value of this property is <code>true</code> or <code>false</code> (Default: false)</div>
<dl class="notes">
<dt>See Also:</dt>
<dd>
<ul class="tag-list">
<li><a href="../../../../constant-values.html#com.nomagic.magicreport.engine.TemplateConstants.TEMPLATE_RTF_RSID">Constant Field Values</a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="TEMPLATE_ODP_USE_VIRTUAL_NAME">
<h3>TEMPLATE_ODP_USE_VIRTUAL_NAME</h3>
<div class="member-signature"><span class="modifiers">public static final</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">TEMPLATE_ODP_USE_VIRTUAL_NAME</span></div>
<div class="block">Key for enable engine to replace ODP hyperlink to page name. The OpenOffice.org will render page name
 pattern "page1", "page2",... and "Slide 1", "Slide 2",... with virtual name of "Slide 1", "Slide 2",... thus
 all the hyperlink pointing to these page name will not be working. If this property is <code>true</code>,
 the engine will replace hyperlink name virtual name. (Default: true)</div>
<dl class="notes">
<dt>See Also:</dt>
<dd>
<ul class="tag-list">
<li><a href="../../../../constant-values.html#com.nomagic.magicreport.engine.TemplateConstants.TEMPLATE_ODP_USE_VIRTUAL_NAME">Constant Field Values</a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="TEMPLATE_XLSX_HTML_LINK">
<h3>TEMPLATE_XLSX_HTML_LINK</h3>
<div class="member-signature"><span class="modifiers">public static final</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">TEMPLATE_XLSX_HTML_LINK</span></div>
<div class="block">Key for selecting the first or last hyperlink in the HTML String of any cell, and apply the selected hyperlink to the cell.</div>
<dl class="notes">
<dt>See Also:</dt>
<dd>
<ul class="tag-list">
<li><a href="../../../../constant-values.html#com.nomagic.magicreport.engine.TemplateConstants.TEMPLATE_XLSX_HTML_LINK">Constant Field Values</a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="ADD_ADDITIONAL_ELEMENT">
<h3>ADD_ADDITIONAL_ELEMENT</h3>
<div class="member-signature"><span class="modifiers">public static final</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">ADD_ADDITIONAL_ELEMENT</span></div>
<div class="block">Use additional element and owned element to get children of element.</div>
<dl class="notes">
<dt>See Also:</dt>
<dd>
<ul class="tag-list">
<li><a href="../../../../constant-values.html#com.nomagic.magicreport.engine.TemplateConstants.ADD_ADDITIONAL_ELEMENT">Constant Field Values</a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="CONTEXT_NAME_PATTERN">
<h3>CONTEXT_NAME_PATTERN</h3>
<div class="member-signature"><span class="modifiers">public static final</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/regex/Pattern.html" title="class or interface in java.util.regex">Pattern</a></span> <span class="element-name">CONTEXT_NAME_PATTERN</span></div>
<div class="block">Contains valid pattern of context name.</div>
</section>
</li>
<li>
<section class="detail" id="DEFAULT_INPUT_ENCODING">
<h3>DEFAULT_INPUT_ENCODING</h3>
<div class="member-signature"><span class="modifiers">public static final</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">DEFAULT_INPUT_ENCODING</span></div>
<div class="block">Default template encoding.</div>
<dl class="notes">
<dt>See Also:</dt>
<dd>
<ul class="tag-list">
<li><a href="../../../../constant-values.html#com.nomagic.magicreport.engine.TemplateConstants.DEFAULT_INPUT_ENCODING">Constant Field Values</a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="DEFAULT_OUTPUT_ENCODING">
<h3>DEFAULT_OUTPUT_ENCODING</h3>
<div class="member-signature"><span class="modifiers">public static final</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">DEFAULT_OUTPUT_ENCODING</span></div>
<div class="block">Default report output encoding.</div>
<dl class="notes">
<dt>See Also:</dt>
<dd>
<ul class="tag-list">
<li><a href="../../../../constant-values.html#com.nomagic.magicreport.engine.TemplateConstants.DEFAULT_OUTPUT_ENCODING">Constant Field Values</a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="RTF_FORMAT">
<h3>RTF_FORMAT</h3>
<div class="member-signature"><span class="modifiers">public static final</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">RTF_FORMAT</span></div>
<dl class="notes">
<dt>See Also:</dt>
<dd>
<ul class="tag-list">
<li><a href="../../../../constant-values.html#com.nomagic.magicreport.engine.TemplateConstants.RTF_FORMAT">Constant Field Values</a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="DEFAULT_PROCESS_SIZE">
<h3>DEFAULT_PROCESS_SIZE</h3>
<div class="member-signature"><span class="modifiers">public static final</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">DEFAULT_PROCESS_SIZE</span></div>
<div class="block">Default processing size.</div>
<dl class="notes">
<dt>See Also:</dt>
<dd>
<ul class="tag-list">
<li><a href="../../../../constant-values.html#com.nomagic.magicreport.engine.TemplateConstants.DEFAULT_PROCESS_SIZE">Constant Field Values</a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="TEMPLATE_TEST">
<h3>TEMPLATE_TEST</h3>
<div class="member-signature"><span class="modifiers">public static final</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">TEMPLATE_TEST</span></div>
<div class="block">Flag for testing template</div>
<dl class="notes">
<dt>See Also:</dt>
<dd>
<ul class="tag-list">
<li><a href="../../../../constant-values.html#com.nomagic.magicreport.engine.TemplateConstants.TEMPLATE_TEST">Constant Field Values</a></li>
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
