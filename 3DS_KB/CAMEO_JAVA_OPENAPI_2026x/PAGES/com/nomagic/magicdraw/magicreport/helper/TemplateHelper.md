# JAVA OPENAPI: TemplateHelper (2026x API)

- source_url: https://jdocs.nomagic.com/2026x/com/nomagic/magicdraw/magicreport/helper/TemplateHelper.html
- source_path: `com/nomagic/magicdraw/magicreport/helper/TemplateHelper.html`
- source_sha256: `4546c36991309e7c3ac9792dbb58f68ec17ef29b862c6ec7b0508e3c82113acf`
- captured_utc: `2026-07-14T16:57:59.217550+00:00`

## NORMALIZED JAVADOC CONTENT

======== START OF CLASS DATA ========

Package [com.nomagic.magicdraw.magicreport.helper](package-summary.html)

## Class TemplateHelper

[java.lang.Object](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html)
com.nomagic.magicdraw.magicreport.helper.TemplateHelper

@OpenApiAllpublic classTemplateHelper
extends [Object](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html)

Provide helper methods for template such as create and save.

Since:
May 10, 2007

=========== FIELD SUMMARY =========== 
Field Summary
Fields
Modifier and Type
Field
Description
`static final [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html)`
`[DBK](#DBK)`
Constants for Default DOCBOOK type.
`static final [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html)`
`[DESCRIPTOR_FILE](#DESCRIPTOR_FILE)`

`static final [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html)`
`[DOCBOOK](#DOCBOOK)`
Constants for DOCBOOK type.
`static final [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html)`
`[DOCX](#DOCX)`
Constants for DOCX type.
`static final [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html)`
`[HTML](#HTML)`
Constants for HTML type.
`static final org.apache.logging.log4j.Logger`
`[LOG](#LOG)`

`static final [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html)`
`[ODP](#ODP)`
Constants for ODP type.
`static final [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html)`
`[ODS](#ODS)`
Constants for ODS type.
`static final [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html)`
`[ODT](#ODT)`
Constants for ODT type.
`static final [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html)`
`[PPTX](#PPTX)`
Constants for PPTX type.
`static final [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html)`
`[PROPERTY_CREATE](#PROPERTY_CREATE)`

`static final [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html)`
`[PROPERTY_DELETE](#PROPERTY_DELETE)`
Delete property name.
`static final [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html)`
`[PROPERTY_RELOAD](#PROPERTY_RELOAD)`
Reload property name.
`static final [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html)`
`[PROPERTY_SAVE](#PROPERTY_SAVE)`
Save property name.
`static final [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html)`
`[RTF](#RTF)`
Constants for RTF type.
`static final [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html)`
`[TEMPLATE_EXTENSION](#TEMPLATE_EXTENSION)`
Constants for template extension.
`static final [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html)`
`[TXT](#TXT)`
Constants for TXT type.
`static final [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html)`
`[XLSX](#XLSX)`
Constants for XLSX type.
`static final [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html)`
`[XML](#XML)`
Constants for XML type.
 ======== CONSTRUCTOR SUMMARY ======== 
Constructor Summary
Constructors
Constructor
Description
`[TemplateHelper](#%3Cinit%3E())()`
 ========== METHOD SUMMARY =========== 
Method Summary
All MethodsStatic MethodsConcrete Methods
Modifier and Type
Method
Description
`static void`
`[addPropertyChangeListener](#addPropertyChangeListener(java.beans.PropertyChangeListener))([PropertyChangeListener](https://docs.oracle.com/en/java/javase/21/docs/api/java.desktop/java/beans/PropertyChangeListener.html) listener)`
Register a listener for the PropertyChange event.
`static boolean`
`[checkEdition](#checkEdition(com.nomagic.magicdraw.magicreport.ui.bean.TemplateBean,com.nomagic.magicdraw.lic.MDVersion))(com.nomagic.magicdraw.magicreport.ui.bean.TemplateBean bean,
 com.nomagic.magicdraw.lic.MDVersion version)`
Return true if this template is valid to MDVersion.
`static [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html)`
`[checkRequiredPlugins](#checkRequiredPlugins(com.nomagic.magicdraw.magicreport.ui.bean.TemplateBean))(com.nomagic.magicdraw.magicreport.ui.bean.TemplateBean bean)`

`static void`
`[clearCachedElements](#clearCachedElements())()`

`static void`
`[copyFiles](#copyFiles(java.io.File,java.io.File))([File](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/io/File.html) tmpFile,
 [File](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/io/File.html) templateFile)`

`static [File](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/io/File.html)`
`[createTemplateFile](#createTemplateFile(com.nomagic.magicdraw.magicreport.ui.bean.TemplateBean))(com.nomagic.magicdraw.magicreport.ui.bean.TemplateBean templateBean)`
Create a directory or file from given template bean.
`static [File](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/io/File.html)`
`[createTemplateFile](#createTemplateFile(java.lang.String))([String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) templateName)`
Create a directory or file from given template name.
`static [Icon](https://docs.oracle.com/en/java/javase/21/docs/api/java.desktop/javax/swing/Icon.html)`
`[createTemplateIcon](#createTemplateIcon(com.nomagic.magicdraw.magicreport.ui.bean.TemplateBean))(com.nomagic.magicdraw.magicreport.ui.bean.TemplateBean templateBean)`
Create and return icon for this template bean.
`static void`
`[exportZip](#exportZip(java.io.File,com.nomagic.magicdraw.magicreport.ui.bean.TemplateBean))([File](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/io/File.html) zipFile,
 com.nomagic.magicdraw.magicreport.ui.bean.TemplateBean templateBean)`
Export template bean to zip file with default progress status.
`static void`
`[exportZip](#exportZip(java.io.File,com.nomagic.magicdraw.magicreport.ui.bean.TemplateBean,com.nomagic.task.ProgressStatus))([File](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/io/File.html) zipFile,
 com.nomagic.magicdraw.magicreport.ui.bean.TemplateBean templateBean,
 [ProgressStatus](../../../task/ProgressStatus.html) progress)`
Export template bean to zip file.
`static void`
`[exportZip](#exportZip(java.io.File,com.nomagic.magicdraw.magicreport.ui.bean.TemplateBean,com.nomagic.task.ProgressStatus,java.util.List))([File](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/io/File.html) zipFile,
 com.nomagic.magicdraw.magicreport.ui.bean.TemplateBean templateBean,
 [ProgressStatus](../../../task/ProgressStatus.html) progress,
 [List](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html)<[File](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/io/File.html)> includedFiles)`
Export template bean to zip file.
`static boolean`
`[extractZip](#extractZip(java.io.File,java.io.File,com.nomagic.task.ProgressStatus))([File](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/io/File.html) zipFile,
 [File](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/io/File.html) destinationDir,
 [ProgressStatus](../../../task/ProgressStatus.html) progress)`

`static com.nomagic.magicdraw.magicreport.ui.bean.TemplateBean`
`[findTemplateBean](#findTemplateBean(java.lang.String,java.lang.String))([String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) catName,
 [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) templName)`
Get the templateBean by given category name and template name.
`static void`
`[firePropertyChange](#firePropertyChange(java.beans.PropertyChangeEvent))([PropertyChangeEvent](https://docs.oracle.com/en/java/javase/21/docs/api/java.desktop/java/beans/PropertyChangeEvent.html) evt)`
Fire an existing PropertyChangeEvent to any registered listeners.
`static void`
`[firePropertyChange](#firePropertyChange(java.lang.Object,java.lang.String,java.lang.Object,java.lang.Object))([Object](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html) source,
 [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) propertyName,
 [Object](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html) oldValue,
 [Object](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html) newValue)`
Report a bound property update to any registered listeners.
`static [Set](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Set.html)<[File](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/io/File.html)>`
`[getCustomTemplateLocations](#getCustomTemplateLocations())()`
Get custom location that store template.
`static [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html)`
`[getDefaultReportKey](#getDefaultReportKey(com.nomagic.magicdraw.magicreport.ui.bean.TemplateBean))(com.nomagic.magicdraw.magicreport.ui.bean.TemplateBean templateBean)`
Return a key for default report preference.
`static [ResizableIcon](../../../ui/ResizableIcon.html)`
`[getIconByFileExtension](#getIconByFileExtension(java.lang.String))([String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) ext)`

`static [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html)`
`[getOutputReportKey](#getOutputReportKey(com.nomagic.magicdraw.magicreport.ui.bean.ReportBean))(com.nomagic.magicdraw.magicreport.ui.bean.ReportBean reportBean)`
Return a key for output report preference.
`static com.nomagic.magicdraw.magicreport.ui.bean.TemplateBean`
`[getTemplateBean](#getTemplateBean(java.lang.String))([String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) path)`
Return existing template bean from the template path.
`static com.nomagic.magicdraw.magicreport.ui.bean.TemplateBean`
`[getTemplateBeanByName](#getTemplateBeanByName(java.lang.String,java.lang.String))([String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) catName,
 [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) templateName)`
Get template bean by category name and template name
`static [File](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/io/File.html)`
`[getTemplateFile](#getTemplateFile(com.nomagic.magicdraw.magicreport.ui.bean.TemplateBean))(com.nomagic.magicdraw.magicreport.ui.bean.TemplateBean templateBean)`

`static [File](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/io/File.html)`
`[getTemplateFile](#getTemplateFile(com.nomagic.magicdraw.magicreport.ui.bean.TemplateBean,boolean))(com.nomagic.magicdraw.magicreport.ui.bean.TemplateBean templateBean,
 boolean revolveDir)`

`static [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html)`
`[getTemplateType](#getTemplateType(java.lang.String))([String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) extension)`
Consider template type from file extension.
`static [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html)`
`[getViewerReportKey](#getViewerReportKey(com.nomagic.magicdraw.magicreport.ui.bean.ReportBean))(com.nomagic.magicdraw.magicreport.ui.bean.ReportBean reportBean)`
Return a key for viewer report preference.
`static com.nomagic.magicdraw.magicreport.ui.bean.TemplateBean`
`[importZip](#importZip(java.io.File,boolean))([File](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/io/File.html) zipFile,
 boolean copyToData)`
Import zip file to template bean.
`static com.nomagic.magicdraw.magicreport.ui.bean.TemplateBean`
`[importZip](#importZip(java.io.File,boolean,com.nomagic.task.ProgressStatus))([File](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/io/File.html) zipFile,
 boolean copyToData,
 [ProgressStatus](../../../task/ProgressStatus.html) progress)`
Import zip file to template bean.
`static boolean`
`[isFileExternal](#isFileExternal(java.io.File,com.nomagic.magicdraw.magicreport.ui.bean.TemplateBean))([File](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/io/File.html) file,
 com.nomagic.magicdraw.magicreport.ui.bean.TemplateBean templateBean)`

`static [List](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html)<com.nomagic.magicdraw.magicreport.ui.bean.TemplateBean>`
`[listAvailableTemplates](#listAvailableTemplates(com.nomagic.magicdraw.lic.MDVersion,com.nomagic.magicdraw.usermodes.UserMode))(com.nomagic.magicdraw.lic.MDVersion version,
 com.nomagic.magicdraw.usermodes.UserMode userMode)`
Return a list of available template to MDVersion and Perspective.
`static void`
`[listMRZipTemplates](#listMRZipTemplates())()`
Load and Unzip MRZip template file from template directory.
`static [List](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html)<com.nomagic.magicdraw.magicreport.ui.bean.TemplateBean>`
`[listTemplates](#listTemplates())()`
This method will automatically load all template file from "data" directory of report plugin and return a
 List of `TemplateBean`.
`static [List](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html)<com.nomagic.magicdraw.magicreport.ui.bean.TemplateBean>`
`[listTemplates](#listTemplates(boolean))(boolean forceReload)`
Load all template files from report plugin "data" directory and return to List of `TemplateBean`.
`static com.nomagic.magicdraw.magicreport.ui.bean.ReportBean`
`[loadReport](#loadReport(java.io.File))([File](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/io/File.html) reportFile)`
Create a `ReportBean` from given reportFile.
`static void`
`[loadReportDataAndConfig](#loadReportDataAndConfig(java.io.File,com.nomagic.magicdraw.magicreport.ui.bean.TemplateBean))([File](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/io/File.html) templateDir,
 com.nomagic.magicdraw.magicreport.ui.bean.TemplateBean templateBean)`

`static com.nomagic.magicdraw.magicreport.ui.bean.TemplateBean`
`[loadTemplate](#loadTemplate(java.io.File))([File](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/io/File.html) templateFile)`
Create a `TemplateBean` from given templateFile.
`static com.nomagic.magicdraw.magicreport.ui.bean.TemplateBean`
`[loadTemplate](#loadTemplate(java.io.File,boolean))([File](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/io/File.html) templateFile,
 boolean checkValid)`
Create a `TemplateBean` from given templateFile.
`static void`
`[loadTemplateBean](#loadTemplateBean(com.nomagic.magicdraw.magicreport.ui.bean.TemplateBean,org.w3c.dom.Document))(com.nomagic.magicdraw.magicreport.ui.bean.TemplateBean templateBean,
 [Document](https://docs.oracle.com/en/java/javase/21/docs/api/java.xml/org/w3c/dom/Document.html) document)`

`static com.nomagic.magicdraw.magicreport.ui.bean.TemplateBean`
`[loadTemplateBean](#loadTemplateBean(java.io.File))([File](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/io/File.html) file)`

`static com.nomagic.magicdraw.magicreport.ui.bean.TemplateBean`
`[reloadTemplate](#reloadTemplate(com.nomagic.magicdraw.magicreport.ui.bean.TemplateBean))(com.nomagic.magicdraw.magicreport.ui.bean.TemplateBean templateBean)`
Force the application to remove this template from cache and then reload it from file.
`static void`
`[removeImportHistory](#removeImportHistory(java.io.File%5B%5D))([File](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/io/File.html)[] importedMrzipFiles)`

`static void`
`[removePropertyChangeListener](#removePropertyChangeListener(java.beans.PropertyChangeListener))([PropertyChangeListener](https://docs.oracle.com/en/java/javase/21/docs/api/java.desktop/java/beans/PropertyChangeListener.html) listener)`
Remove a listener for the PropertyChange event.
`static void`
`[removeTemplate](#removeTemplate(com.nomagic.magicdraw.magicreport.ui.bean.TemplateBean))(com.nomagic.magicdraw.magicreport.ui.bean.TemplateBean templateBean)`
Delete a template file from physical storage.
`static void`
`[saveReport](#saveReport(com.nomagic.magicdraw.magicreport.ui.bean.ReportBean))(com.nomagic.magicdraw.magicreport.ui.bean.ReportBean reportBean)`
Create a new report file from ReportBean.
`static void`
`[saveReport](#saveReport(com.nomagic.magicdraw.magicreport.ui.bean.TemplateBean,com.nomagic.magicdraw.magicreport.ui.bean.ReportBean))(com.nomagic.magicdraw.magicreport.ui.bean.TemplateBean templateBean,
 com.nomagic.magicdraw.magicreport.ui.bean.ReportBean reportBean)`
Create a new report file from ReportBean.
`static void`
`[saveTemplate](#saveTemplate(com.nomagic.magicdraw.magicreport.ui.bean.TemplateBean))(com.nomagic.magicdraw.magicreport.ui.bean.TemplateBean templateBean)`
Create a new template file from TemplateBean.
`static void`
`[unzipMRZipTemplates](#unzipMRZipTemplates(java.io.File%5B%5D))([File](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/io/File.html)[] mrZipFile)`
Unzip MRZip Templates files.
Methods inherited from class java.lang.[Object](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html)
`[clone](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#clone()), [equals](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#equals(java.lang.Object)), [finalize](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#finalize()), [getClass](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#getClass()), [hashCode](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#hashCode()), [notify](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#notify()), [notifyAll](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#notifyAll()), [toString](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#toString()), [wait](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#wait()), [wait](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#wait(long)), [wait](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#wait(long,int))`

============ FIELD DETAIL =========== 
Field Details
TEMPLATE_EXTENSION
public static final [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) TEMPLATE_EXTENSION
Constants for template extension.
See Also:
[Constant Field Values](../../../../../constant-values.html#com.nomagic.magicdraw.magicreport.helper.TemplateHelper.TEMPLATE_EXTENSION)
PROPERTY_SAVE
public static final [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) PROPERTY_SAVE
Save property name.
See Also:
[Constant Field Values](../../../../../constant-values.html#com.nomagic.magicdraw.magicreport.helper.TemplateHelper.PROPERTY_SAVE)
PROPERTY_DELETE
public static final [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) PROPERTY_DELETE
Delete property name.
See Also:
[Constant Field Values](../../../../../constant-values.html#com.nomagic.magicdraw.magicreport.helper.TemplateHelper.PROPERTY_DELETE)
PROPERTY_CREATE
public static final [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) PROPERTY_CREATE
See Also:
[Constant Field Values](../../../../../constant-values.html#com.nomagic.magicdraw.magicreport.helper.TemplateHelper.PROPERTY_CREATE)
PROPERTY_RELOAD
public static final [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) PROPERTY_RELOAD
Reload property name.
See Also:
[Constant Field Values](../../../../../constant-values.html#com.nomagic.magicdraw.magicreport.helper.TemplateHelper.PROPERTY_RELOAD)
HTML
public static final [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) HTML
Constants for HTML type.
See Also:
[Constant Field Values](../../../../../constant-values.html#com.nomagic.magicdraw.magicreport.helper.TemplateHelper.HTML)
RTF
public static final [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) RTF
Constants for RTF type.
See Also:
[Constant Field Values](../../../../../constant-values.html#com.nomagic.magicdraw.magicreport.helper.TemplateHelper.RTF)
XML
public static final [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) XML
Constants for XML type.
See Also:
[Constant Field Values](../../../../../constant-values.html#com.nomagic.magicdraw.magicreport.helper.TemplateHelper.XML)
TXT
public static final [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) TXT
Constants for TXT type.
See Also:
[Constant Field Values](../../../../../constant-values.html#com.nomagic.magicdraw.magicreport.helper.TemplateHelper.TXT)
ODT
public static final [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) ODT
Constants for ODT type.
See Also:
[Constant Field Values](../../../../../constant-values.html#com.nomagic.magicdraw.magicreport.helper.TemplateHelper.ODT)
ODS
public static final [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) ODS
Constants for ODS type.
See Also:
[Constant Field Values](../../../../../constant-values.html#com.nomagic.magicdraw.magicreport.helper.TemplateHelper.ODS)
ODP
public static final [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) ODP
Constants for ODP type.
See Also:
[Constant Field Values](../../../../../constant-values.html#com.nomagic.magicdraw.magicreport.helper.TemplateHelper.ODP)
DOCX
public static final [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) DOCX
Constants for DOCX type.
See Also:
[Constant Field Values](../../../../../constant-values.html#com.nomagic.magicdraw.magicreport.helper.TemplateHelper.DOCX)
XLSX
public static final [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) XLSX
Constants for XLSX type.
See Also:
[Constant Field Values](../../../../../constant-values.html#com.nomagic.magicdraw.magicreport.helper.TemplateHelper.XLSX)
PPTX
public static final [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) PPTX
Constants for PPTX type.
See Also:
[Constant Field Values](../../../../../constant-values.html#com.nomagic.magicdraw.magicreport.helper.TemplateHelper.PPTX)
DBK
public static final [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) DBK
Constants for Default DOCBOOK type.
See Also:
[Constant Field Values](../../../../../constant-values.html#com.nomagic.magicdraw.magicreport.helper.TemplateHelper.DBK)
DOCBOOK
public static final [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) DOCBOOK
Constants for DOCBOOK type.
See Also:
[Constant Field Values](../../../../../constant-values.html#com.nomagic.magicdraw.magicreport.helper.TemplateHelper.DOCBOOK)
DESCRIPTOR_FILE
public static final [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) DESCRIPTOR_FILE
See Also:
[Constant Field Values](../../../../../constant-values.html#com.nomagic.magicdraw.magicreport.helper.TemplateHelper.DESCRIPTOR_FILE)
LOG
public static final org.apache.logging.log4j.Logger LOG
 ========= CONSTRUCTOR DETAIL ======== 
Constructor Details
TemplateHelper
public TemplateHelper()
 ============ METHOD DETAIL ========== 
Method Details
listTemplates
public static [List](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html)<com.nomagic.magicdraw.magicreport.ui.bean.TemplateBean> listTemplates()
This method will automatically load all template file from "data" directory of report plugin and return a
 List of `TemplateBean`. `TemplateBean` is a container of template information.
Returns:
a List of `TemplateBean` from "data" directory.
See Also:
[`listTemplates(boolean)`](#listTemplates(boolean))
[`listAvailableTemplates(MDVersion, UserMode)`](#listAvailableTemplates(com.nomagic.magicdraw.lic.MDVersion,com.nomagic.magicdraw.usermodes.UserMode))
listAvailableTemplates
public static [List](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html)<com.nomagic.magicdraw.magicreport.ui.bean.TemplateBean> listAvailableTemplates(@CheckForNull
 com.nomagic.magicdraw.lic.MDVersion version,
 @CheckForNull
 com.nomagic.magicdraw.usermodes.UserMode userMode)
Return a list of available template to MDVersion and Perspective.
Parameters:
`version` - MDVersion
`userMode` - UserMode
Returns:
a list of available template after filter out
See Also:
[`listTemplates()`](#listTemplates())
checkEdition
public static boolean checkEdition(com.nomagic.magicdraw.magicreport.ui.bean.TemplateBean bean,
 @CheckForNull
 com.nomagic.magicdraw.lic.MDVersion version)
Return true if this template is valid to MDVersion.
Parameters:
`version` - MDVersion
Returns:
true if this template is valid to given MDVersion; otherwise false.
checkRequiredPlugins
public static [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) checkRequiredPlugins(com.nomagic.magicdraw.magicreport.ui.bean.TemplateBean bean)
Returns:
empty string if all required plugins are ok. Otherwise, a multiline info message for each missing/outdated plugin
addPropertyChangeListener
public static void addPropertyChangeListener([PropertyChangeListener](https://docs.oracle.com/en/java/javase/21/docs/api/java.desktop/java/beans/PropertyChangeListener.html) listener)
Register a listener for the PropertyChange event. When a Template changes its value it should fire a
 PropertyChange event on all registered PropertyChangeListeners.
Parameters:
`listener` - An object to be invoked when a PropertyChange event is fired.
removePropertyChangeListener
public static void removePropertyChangeListener([PropertyChangeListener](https://docs.oracle.com/en/java/javase/21/docs/api/java.desktop/java/beans/PropertyChangeListener.html) listener)
Remove a listener for the PropertyChange event.
Parameters:
`listener` - The PropertyChange listener to be removed.
firePropertyChange
public static void firePropertyChange([Object](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html) source,
 [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) propertyName,
 @CheckForNull
 [Object](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html) oldValue,
 [Object](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html) newValue)
Report a bound property update to any registered listeners. No event is fired if old and new are equal and
 non-null.
Parameters:
`source` - property source
`propertyName` - The programmatic name of the property that was changed.
`oldValue` - The old value of the property.
`newValue` - The new value of the property.
firePropertyChange
public static void firePropertyChange([PropertyChangeEvent](https://docs.oracle.com/en/java/javase/21/docs/api/java.desktop/java/beans/PropertyChangeEvent.html) evt)
Fire an existing PropertyChangeEvent to any registered listeners. No event is fired if the given event's old
 and new values are equal and non-null.
Parameters:
`evt` - The PropertyChangeEvent object.
listTemplates
public static [List](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html)<com.nomagic.magicdraw.magicreport.ui.bean.TemplateBean> listTemplates(boolean forceReload)
Load all template files from report plugin "data" directory and return to List of `TemplateBean`.
Parameters:
`forceReload` - true if you want this method to reload template from disk; false use template from cache.
Returns:
a List of `TemplateBean` from "data" directory.
See Also:
[`listTemplates()`](#listTemplates())
listMRZipTemplates
public static void listMRZipTemplates()
Load and Unzip MRZip template file from template directory.
unzipMRZipTemplates
public static void unzipMRZipTemplates([File](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/io/File.html)[] mrZipFile)
Unzip MRZip Templates files.
Parameters:
`mrZipFile` - file
removeImportHistory
public static void removeImportHistory([File](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/io/File.html)[] importedMrzipFiles)
reloadTemplate
public static com.nomagic.magicdraw.magicreport.ui.bean.TemplateBean reloadTemplate(com.nomagic.magicdraw.magicreport.ui.bean.TemplateBean templateBean)
Force the application to remove this template from cache and then reload it from file.
Parameters:
`templateBean` - a target template
Returns:
TemplateBean or null if invalid template file format.
getTemplateBean
public static com.nomagic.magicdraw.magicreport.ui.bean.TemplateBean getTemplateBean([String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) path)
Return existing template bean from the template path.
Parameters:
`path` - path of template `TemplateBean.getPath()`
Returns:
the `TemplateBean`
getTemplateBeanByName
public static com.nomagic.magicdraw.magicreport.ui.bean.TemplateBean getTemplateBeanByName([String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) catName,
 [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) templateName)
Get template bean by category name and template name
Parameters:
`catName` - template category name
`templateName` - template name
Returns:
template bean
loadTemplate
public static com.nomagic.magicdraw.magicreport.ui.bean.TemplateBean loadTemplate([File](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/io/File.html) templateFile)
Create a `TemplateBean` from given templateFile. If template file is not valid template format, return
 null.
Parameters:
`templateFile` - a File for template
Returns:
TemplateBean or null if invalid template file format.
loadTemplate
@CheckForNullpublic static com.nomagic.magicdraw.magicreport.ui.bean.TemplateBean loadTemplate([File](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/io/File.html) templateFile,
 boolean checkValid)
 throws [TemplateException](../../../magicreport/TemplateException.html)
Create a `TemplateBean` from given templateFile. If template file is not valid template format, return
 null.
Parameters:
`templateFile` - a File for template
`checkValid` - true if this template file require format checking
Returns:
TemplateBean or null if invalid template file format.
Throws:
`[TemplateException](../../../magicreport/TemplateException.html)` - if the template file is not valid format and check parameter is true.
loadReportDataAndConfig
public static void loadReportDataAndConfig([File](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/io/File.html) templateDir,
 com.nomagic.magicdraw.magicreport.ui.bean.TemplateBean templateBean)
importZip
public static com.nomagic.magicdraw.magicreport.ui.bean.TemplateBean importZip([File](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/io/File.html) zipFile,
 boolean copyToData)
 throws [IOException](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/io/IOException.html)
Import zip file to template bean.
Parameters:
`zipFile` - an input zip file.
`copyToData` - copy template to data folder after successfully extract.
Returns:
templateBean a template bean
Throws:
`[IOException](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/io/IOException.html)` - when unable to import zip file.
See Also:
[`importZip(File, boolean, ProgressStatus)`](#importZip(java.io.File,boolean,com.nomagic.task.ProgressStatus))
importZip
@CheckForNullpublic static com.nomagic.magicdraw.magicreport.ui.bean.TemplateBean importZip([File](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/io/File.html) zipFile,
 boolean copyToData,
 [ProgressStatus](../../../task/ProgressStatus.html) progress)
 throws [IOException](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/io/IOException.html)
Import zip file to template bean.
Parameters:
`zipFile` - an input zip file.
`copyToData` - copy template to data folder after successfully extract.
`progress` - the progress status
Returns:
templateBean a template bean
Throws:
`[IOException](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/io/IOException.html)` - when unable to import zip file.
See Also:
[`importZip(File, boolean)`](#importZip(java.io.File,boolean))
copyFiles
public static void copyFiles([File](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/io/File.html) tmpFile,
 [File](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/io/File.html) templateFile)
 throws [IOException](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/io/IOException.html)
Throws:
`[IOException](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/io/IOException.html)`
extractZip
public static boolean extractZip([File](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/io/File.html) zipFile,
 [File](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/io/File.html) destinationDir,
 [ProgressStatus](../../../task/ProgressStatus.html) progress)
 throws [IOException](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/io/IOException.html)
Throws:
`[IOException](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/io/IOException.html)`
exportZip
public static void exportZip([File](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/io/File.html) zipFile,
 com.nomagic.magicdraw.magicreport.ui.bean.TemplateBean templateBean)
 throws [IOException](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/io/IOException.html)
Export template bean to zip file with default progress status.
Parameters:
`zipFile` - a output zip file.
`templateBean` - a template bean
Throws:
`[IOException](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/io/IOException.html)` - when unable to export zip file.
See Also:
[`exportZip(File, TemplateBean, ProgressStatus)`](#exportZip(java.io.File,com.nomagic.magicdraw.magicreport.ui.bean.TemplateBean,com.nomagic.task.ProgressStatus))
exportZip
public static void exportZip([File](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/io/File.html) zipFile,
 com.nomagic.magicdraw.magicreport.ui.bean.TemplateBean templateBean,
 [ProgressStatus](../../../task/ProgressStatus.html) progress)
 throws [IOException](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/io/IOException.html)
Export template bean to zip file.
Parameters:
`zipFile` - a output zip file.
`templateBean` - a template bean
`progress` - the progress status
Throws:
`[IOException](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/io/IOException.html)` - when unable to export zip file.
See Also:
[`exportZip(File, TemplateBean)`](#exportZip(java.io.File,com.nomagic.magicdraw.magicreport.ui.bean.TemplateBean))
exportZip
public static void exportZip([File](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/io/File.html) zipFile,
 com.nomagic.magicdraw.magicreport.ui.bean.TemplateBean templateBean,
 [ProgressStatus](../../../task/ProgressStatus.html) progress,
 [List](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html)<[File](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/io/File.html)> includedFiles)
 throws [IOException](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/io/IOException.html)
Export template bean to zip file.
Parameters:
`zipFile` - a output zip file.
`templateBean` - a template bean
`progress` - the progress status
`includedFiles` - other files to be included in this zip
Throws:
`[IOException](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/io/IOException.html)` - when unable to export zip file.
See Also:
[`exportZip(File, TemplateBean)`](#exportZip(java.io.File,com.nomagic.magicdraw.magicreport.ui.bean.TemplateBean))
isFileExternal
public static boolean isFileExternal([File](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/io/File.html) file,
 com.nomagic.magicdraw.magicreport.ui.bean.TemplateBean templateBean)
Parameters:
`file` - to check
`templateBean` -
Returns:
true if checked file resides outside the template package
getTemplateFile
public static [File](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/io/File.html) getTemplateFile(com.nomagic.magicdraw.magicreport.ui.bean.TemplateBean templateBean)
getTemplateFile
public static [File](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/io/File.html) getTemplateFile(com.nomagic.magicdraw.magicreport.ui.bean.TemplateBean templateBean,
 boolean revolveDir)
loadReport
public static com.nomagic.magicdraw.magicreport.ui.bean.ReportBean loadReport([File](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/io/File.html) reportFile)
Create a `ReportBean` from given reportFile. If report file is not valid report format, return null.
Parameters:
`reportFile` - a File for report
Returns:
ReportBean or null if invalid report file format.
saveTemplate
public static void saveTemplate(com.nomagic.magicdraw.magicreport.ui.bean.TemplateBean templateBean)
 throws [IOException](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/io/IOException.html)
Create a new template file from TemplateBean. If `TemplateBean.getPath()` exists, write a template
 file to this value; if value doesn't exists create a new file with `TemplateBean.getName()` as
 template filename.
Parameters:
`templateBean` - a Template Bean
Throws:
`[IOException](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/io/IOException.html)` - if the template was not successfully created
loadTemplateBean
public static com.nomagic.magicdraw.magicreport.ui.bean.TemplateBean loadTemplateBean([File](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/io/File.html) file)
 throws [IOException](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/io/IOException.html)
Throws:
`[IOException](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/io/IOException.html)`
loadTemplateBean
public static void loadTemplateBean(com.nomagic.magicdraw.magicreport.ui.bean.TemplateBean templateBean,
 [Document](https://docs.oracle.com/en/java/javase/21/docs/api/java.xml/org/w3c/dom/Document.html) document)
 throws [IOException](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/io/IOException.html)
Throws:
`[IOException](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/io/IOException.html)`
saveReport
public static void saveReport(com.nomagic.magicdraw.magicreport.ui.bean.TemplateBean templateBean,
 com.nomagic.magicdraw.magicreport.ui.bean.ReportBean reportBean)
 throws [IOException](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/io/IOException.html)
Create a new report file from ReportBean. If `ReportBean.getFileName()` exists, write a report file to
 this value; if value doesn't exists create a new file with `TemplateBean.getName()` as template
 filename.
Parameters:
`templateBean` - a TemplateBean
`reportBean` - a ReportBean
Throws:
`[IOException](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/io/IOException.html)` - if the template was not successfully created
saveReport
public static void saveReport(com.nomagic.magicdraw.magicreport.ui.bean.ReportBean reportBean)
 throws [IOException](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/io/IOException.html)
Create a new report file from ReportBean. If `ReportBean.getFileName()` exists, write a report file to
 this value; if value doesn't exists throw IOException.
Parameters:
`reportBean` - a ReportBean
Throws:
`[IOException](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/io/IOException.html)` - if the report was not successfully created
removeTemplate
public static void removeTemplate(com.nomagic.magicdraw.magicreport.ui.bean.TemplateBean templateBean)
 throws [IOException](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/io/IOException.html)
Delete a template file from physical storage. Physical storage meaning that template file will not be able
 to recovery after successfully deleted.
Parameters:
`templateBean` - a Template Bean
Throws:
`[IOException](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/io/IOException.html)` - if the template was not successfully deleted
createTemplateFile
public static [File](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/io/File.html) createTemplateFile(com.nomagic.magicdraw.magicreport.ui.bean.TemplateBean templateBean)
 throws [IOException](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/io/IOException.html)
Create a directory or file from given template bean. This method use template name as a directory name.
Parameters:
`templateBean` - a template bean
Returns:
File references to template bean
Throws:
`[IOException](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/io/IOException.html)` - if false to create directory.
createTemplateFile
public static [File](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/io/File.html) createTemplateFile([String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) templateName)
 throws [IOException](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/io/IOException.html)
Create a directory or file from given template name.
Parameters:
`templateName` - a template name
Returns:
File references to template bean
Throws:
`[IOException](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/io/IOException.html)` - if false to create directory.
findTemplateBean
public static com.nomagic.magicdraw.magicreport.ui.bean.TemplateBean findTemplateBean(@CheckForNull
 [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) catName,
 [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) templName)
Get the templateBean by given category name and template name.
Parameters:
`catName` - categoryName or null
`templName` - the template name
Returns:
the TemplateBean
getTemplateType
public static [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) getTemplateType([String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) extension)
Consider template type from file extension.
Parameters:
`extension` - a file extension.
Returns:
a template type.
createTemplateIcon
public static [Icon](https://docs.oracle.com/en/java/javase/21/docs/api/java.desktop/javax/swing/Icon.html) createTemplateIcon(com.nomagic.magicdraw.magicreport.ui.bean.TemplateBean templateBean)
Create and return icon for this template bean.
Parameters:
`templateBean` - a template bean
Returns:
template icon
getIconByFileExtension
public static [ResizableIcon](../../../ui/ResizableIcon.html) getIconByFileExtension([String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) ext)
getDefaultReportKey
public static [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) getDefaultReportKey(com.nomagic.magicdraw.magicreport.ui.bean.TemplateBean templateBean)
 throws [IllegalArgumentException](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/IllegalArgumentException.html)
Return a key for default report preference. A key is a concatenation of `#hashCode()` and ";default".
Parameters:
`templateBean` - a template bean
Returns:
a key.
Throws:
`[IllegalArgumentException](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/IllegalArgumentException.html)` - illegal argument is used.
getOutputReportKey
public static [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) getOutputReportKey(com.nomagic.magicdraw.magicreport.ui.bean.ReportBean reportBean)
 throws [IllegalArgumentException](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/IllegalArgumentException.html)
Return a key for output report preference. A key is a concatenation of 
invalid @link
{@link ReportBean#getModel()#getID()
}
 and ";output" or 
invalid @link
{@link ReportBean#getFileName()#hashCode()
} + ";output".
Parameters:
`reportBean` - a report bean
Returns:
a key.
Throws:
`[IllegalArgumentException](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/IllegalArgumentException.html)` - illegal argument is used.
getViewerReportKey
public static [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) getViewerReportKey(com.nomagic.magicdraw.magicreport.ui.bean.ReportBean reportBean)
 throws [IllegalArgumentException](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/IllegalArgumentException.html)
Return a key for viewer report preference. A key is a concatenation of 
invalid @link
{@link ReportBean#getModel()#getID()
}
 and ";viewer" or 
invalid @link
{@link ReportBean#getFileName()#hashCode()
} + ";viewer".
Parameters:
`reportBean` - a report bean
Returns:
a key.
Throws:
`[IllegalArgumentException](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/IllegalArgumentException.html)` - illegal argument is used.
getCustomTemplateLocations
public static [Set](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Set.html)<[File](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/io/File.html)> getCustomTemplateLocations()
Get custom location that store template.
Returns:
list of custom location
clearCachedElements
public static void clearCachedElements()

========= END OF CLASS DATA =========

## EXACT JAVADOC MAIN HTML

````html
<main role="main">
<!-- ======== START OF CLASS DATA ======== -->
<div class="header">
<div class="sub-title"><span class="package-label-in-type">Package</span> <a href="package-summary.html">com.nomagic.magicdraw.magicreport.helper</a></div>
<h1 class="title" title="Class TemplateHelper">Class TemplateHelper</h1>
</div>
<div class="inheritance" title="Inheritance Tree"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">java.lang.Object</a>
<div class="inheritance">com.nomagic.magicdraw.magicreport.helper.TemplateHelper</div>
</div>
<section class="class-description" id="class-description">
<hr/>
<div class="type-signature"><span class="annotations">@OpenApiAll
</span><span class="modifiers">public class </span><span class="element-name type-name-label">TemplateHelper</span>
<span class="extends-implements">extends <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a></span></div>
<div class="block">Provide helper methods for template such as create and save.</div>
<dl class="notes">
<dt>Since:</dt>
<dd>May 10, 2007</dd>
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
<div class="col-second even-row-color"><code><a class="member-name-link" href="#DBK">DBK</a></code></div>
<div class="col-last even-row-color">
<div class="block">Constants for Default DOCBOOK type.</div>
</div>
<div class="col-first odd-row-color"><code>static final <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second odd-row-color"><code><a class="member-name-link" href="#DESCRIPTOR_FILE">DESCRIPTOR_FILE</a></code></div>
<div class="col-last odd-row-color"> </div>
<div class="col-first even-row-color"><code>static final <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second even-row-color"><code><a class="member-name-link" href="#DOCBOOK">DOCBOOK</a></code></div>
<div class="col-last even-row-color">
<div class="block">Constants for DOCBOOK type.</div>
</div>
<div class="col-first odd-row-color"><code>static final <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second odd-row-color"><code><a class="member-name-link" href="#DOCX">DOCX</a></code></div>
<div class="col-last odd-row-color">
<div class="block">Constants for DOCX type.</div>
</div>
<div class="col-first even-row-color"><code>static final <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second even-row-color"><code><a class="member-name-link" href="#HTML">HTML</a></code></div>
<div class="col-last even-row-color">
<div class="block">Constants for HTML type.</div>
</div>
<div class="col-first odd-row-color"><code>static final org.apache.logging.log4j.Logger</code></div>
<div class="col-second odd-row-color"><code><a class="member-name-link" href="#LOG">LOG</a></code></div>
<div class="col-last odd-row-color"> </div>
<div class="col-first even-row-color"><code>static final <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second even-row-color"><code><a class="member-name-link" href="#ODP">ODP</a></code></div>
<div class="col-last even-row-color">
<div class="block">Constants for ODP type.</div>
</div>
<div class="col-first odd-row-color"><code>static final <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second odd-row-color"><code><a class="member-name-link" href="#ODS">ODS</a></code></div>
<div class="col-last odd-row-color">
<div class="block">Constants for ODS type.</div>
</div>
<div class="col-first even-row-color"><code>static final <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second even-row-color"><code><a class="member-name-link" href="#ODT">ODT</a></code></div>
<div class="col-last even-row-color">
<div class="block">Constants for ODT type.</div>
</div>
<div class="col-first odd-row-color"><code>static final <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second odd-row-color"><code><a class="member-name-link" href="#PPTX">PPTX</a></code></div>
<div class="col-last odd-row-color">
<div class="block">Constants for PPTX type.</div>
</div>
<div class="col-first even-row-color"><code>static final <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second even-row-color"><code><a class="member-name-link" href="#PROPERTY_CREATE">PROPERTY_CREATE</a></code></div>
<div class="col-last even-row-color"> </div>
<div class="col-first odd-row-color"><code>static final <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second odd-row-color"><code><a class="member-name-link" href="#PROPERTY_DELETE">PROPERTY_DELETE</a></code></div>
<div class="col-last odd-row-color">
<div class="block">Delete property name.</div>
</div>
<div class="col-first even-row-color"><code>static final <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second even-row-color"><code><a class="member-name-link" href="#PROPERTY_RELOAD">PROPERTY_RELOAD</a></code></div>
<div class="col-last even-row-color">
<div class="block">Reload property name.</div>
</div>
<div class="col-first odd-row-color"><code>static final <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second odd-row-color"><code><a class="member-name-link" href="#PROPERTY_SAVE">PROPERTY_SAVE</a></code></div>
<div class="col-last odd-row-color">
<div class="block">Save property name.</div>
</div>
<div class="col-first even-row-color"><code>static final <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second even-row-color"><code><a class="member-name-link" href="#RTF">RTF</a></code></div>
<div class="col-last even-row-color">
<div class="block">Constants for RTF type.</div>
</div>
<div class="col-first odd-row-color"><code>static final <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second odd-row-color"><code><a class="member-name-link" href="#TEMPLATE_EXTENSION">TEMPLATE_EXTENSION</a></code></div>
<div class="col-last odd-row-color">
<div class="block">Constants for template extension.</div>
</div>
<div class="col-first even-row-color"><code>static final <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second even-row-color"><code><a class="member-name-link" href="#TXT">TXT</a></code></div>
<div class="col-last even-row-color">
<div class="block">Constants for TXT type.</div>
</div>
<div class="col-first odd-row-color"><code>static final <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second odd-row-color"><code><a class="member-name-link" href="#XLSX">XLSX</a></code></div>
<div class="col-last odd-row-color">
<div class="block">Constants for XLSX type.</div>
</div>
<div class="col-first even-row-color"><code>static final <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second even-row-color"><code><a class="member-name-link" href="#XML">XML</a></code></div>
<div class="col-last even-row-color">
<div class="block">Constants for XML type.</div>
</div>
</div>
</section>
</li>
<!-- ======== CONSTRUCTOR SUMMARY ======== -->
<li>
<section class="constructor-summary" id="constructor-summary">
<h2>Constructor Summary</h2>
<div class="caption"><span>Constructors</span></div>
<div class="summary-table two-column-summary">
<div class="table-header col-first">Constructor</div>
<div class="table-header col-last">Description</div>
<div class="col-constructor-name even-row-color"><code><a class="member-name-link" href="#%3Cinit%3E()">TemplateHelper</a>()</code></div>
<div class="col-last even-row-color"> </div>
</div>
</section>
</li>
<!-- ========== METHOD SUMMARY =========== -->
<li>
<section class="method-summary" id="method-summary">
<h2>Method Summary</h2>
<div id="method-summary-table">
<div aria-orientation="horizontal" class="table-tabs" role="tablist"><button aria-controls="method-summary-table.tabpanel" aria-selected="true" class="active-table-tab" id="method-summary-table-tab0" onclick="show('method-summary-table', 'method-summary-table', 3)" onkeydown="switchTab(event)" role="tab" tabindex="0">All Methods</button><button aria-controls="method-summary-table.tabpanel" aria-selected="false" class="table-tab" id="method-summary-table-tab1" onclick="show('method-summary-table', 'method-summary-table-tab1', 3)" onkeydown="switchTab(event)" role="tab" tabindex="-1">Static Methods</button><button aria-controls="method-summary-table.tabpanel" aria-selected="false" class="table-tab" id="method-summary-table-tab4" onclick="show('method-summary-table', 'method-summary-table-tab4', 3)" onkeydown="switchTab(event)" role="tab" tabindex="-1">Concrete Methods</button></div>
<div aria-labelledby="method-summary-table-tab0" id="method-summary-table.tabpanel" role="tabpanel">
<div class="summary-table three-column-summary">
<div class="table-header col-first">Modifier and Type</div>
<div class="table-header col-second">Method</div>
<div class="table-header col-last">Description</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#addPropertyChangeListener(java.beans.PropertyChangeListener)">addPropertyChangeListener</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.desktop/java/beans/PropertyChangeListener.html" title="class or interface in java.beans">PropertyChangeListener</a> listener)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Register a listener for the PropertyChange event.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static boolean</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#checkEdition(com.nomagic.magicdraw.magicreport.ui.bean.TemplateBean,com.nomagic.magicdraw.lic.MDVersion)">checkEdition</a><wbr/>(com.nomagic.magicdraw.magicreport.ui.bean.TemplateBean bean,
 com.nomagic.magicdraw.lic.MDVersion version)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Return true if this template is valid to MDVersion.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#checkRequiredPlugins(com.nomagic.magicdraw.magicreport.ui.bean.TemplateBean)">checkRequiredPlugins</a><wbr/>(com.nomagic.magicdraw.magicreport.ui.bean.TemplateBean bean)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#clearCachedElements()">clearCachedElements</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#copyFiles(java.io.File,java.io.File)">copyFiles</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/io/File.html" title="class or interface in java.io">File</a> tmpFile,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/io/File.html" title="class or interface in java.io">File</a> templateFile)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/io/File.html" title="class or interface in java.io">File</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#createTemplateFile(com.nomagic.magicdraw.magicreport.ui.bean.TemplateBean)">createTemplateFile</a><wbr/>(com.nomagic.magicdraw.magicreport.ui.bean.TemplateBean templateBean)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Create a directory or file from given template bean.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/io/File.html" title="class or interface in java.io">File</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#createTemplateFile(java.lang.String)">createTemplateFile</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> templateName)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Create a directory or file from given template name.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.desktop/javax/swing/Icon.html" title="class or interface in javax.swing">Icon</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#createTemplateIcon(com.nomagic.magicdraw.magicreport.ui.bean.TemplateBean)">createTemplateIcon</a><wbr/>(com.nomagic.magicdraw.magicreport.ui.bean.TemplateBean templateBean)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Create and return icon for this template bean.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#exportZip(java.io.File,com.nomagic.magicdraw.magicreport.ui.bean.TemplateBean)">exportZip</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/io/File.html" title="class or interface in java.io">File</a> zipFile,
 com.nomagic.magicdraw.magicreport.ui.bean.TemplateBean templateBean)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Export template bean to zip file with default progress status.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#exportZip(java.io.File,com.nomagic.magicdraw.magicreport.ui.bean.TemplateBean,com.nomagic.task.ProgressStatus)">exportZip</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/io/File.html" title="class or interface in java.io">File</a> zipFile,
 com.nomagic.magicdraw.magicreport.ui.bean.TemplateBean templateBean,
 <a href="../../../task/ProgressStatus.html" title="interface in com.nomagic.task">ProgressStatus</a> progress)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Export template bean to zip file.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#exportZip(java.io.File,com.nomagic.magicdraw.magicreport.ui.bean.TemplateBean,com.nomagic.task.ProgressStatus,java.util.List)">exportZip</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/io/File.html" title="class or interface in java.io">File</a> zipFile,
 com.nomagic.magicdraw.magicreport.ui.bean.TemplateBean templateBean,
 <a href="../../../task/ProgressStatus.html" title="interface in com.nomagic.task">ProgressStatus</a> progress,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/io/File.html" title="class or interface in java.io">File</a>&gt; includedFiles)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Export template bean to zip file.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static boolean</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#extractZip(java.io.File,java.io.File,com.nomagic.task.ProgressStatus)">extractZip</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/io/File.html" title="class or interface in java.io">File</a> zipFile,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/io/File.html" title="class or interface in java.io">File</a> destinationDir,
 <a href="../../../task/ProgressStatus.html" title="interface in com.nomagic.task">ProgressStatus</a> progress)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static com.nomagic.magicdraw.magicreport.ui.bean.TemplateBean</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#findTemplateBean(java.lang.String,java.lang.String)">findTemplateBean</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> catName,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> templName)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Get the templateBean by given category name and template name.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#firePropertyChange(java.beans.PropertyChangeEvent)">firePropertyChange</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.desktop/java/beans/PropertyChangeEvent.html" title="class or interface in java.beans">PropertyChangeEvent</a> evt)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Fire an existing PropertyChangeEvent to any registered listeners.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#firePropertyChange(java.lang.Object,java.lang.String,java.lang.Object,java.lang.Object)">firePropertyChange</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a> source,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> propertyName,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a> oldValue,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a> newValue)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Report a bound property update to any registered listeners.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Set.html" title="class or interface in java.util">Set</a><wbr/>&lt;<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/io/File.html" title="class or interface in java.io">File</a>&gt;</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#getCustomTemplateLocations()">getCustomTemplateLocations</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Get custom location that store template.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#getDefaultReportKey(com.nomagic.magicdraw.magicreport.ui.bean.TemplateBean)">getDefaultReportKey</a><wbr/>(com.nomagic.magicdraw.magicreport.ui.bean.TemplateBean templateBean)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Return a key for default report preference.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static <a href="../../../ui/ResizableIcon.html" title="interface in com.nomagic.ui">ResizableIcon</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#getIconByFileExtension(java.lang.String)">getIconByFileExtension</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> ext)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#getOutputReportKey(com.nomagic.magicdraw.magicreport.ui.bean.ReportBean)">getOutputReportKey</a><wbr/>(com.nomagic.magicdraw.magicreport.ui.bean.ReportBean reportBean)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Return a key for output report preference.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static com.nomagic.magicdraw.magicreport.ui.bean.TemplateBean</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#getTemplateBean(java.lang.String)">getTemplateBean</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> path)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Return existing template bean from the template path.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static com.nomagic.magicdraw.magicreport.ui.bean.TemplateBean</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#getTemplateBeanByName(java.lang.String,java.lang.String)">getTemplateBeanByName</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> catName,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> templateName)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Get template bean by category name and template name</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/io/File.html" title="class or interface in java.io">File</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#getTemplateFile(com.nomagic.magicdraw.magicreport.ui.bean.TemplateBean)">getTemplateFile</a><wbr/>(com.nomagic.magicdraw.magicreport.ui.bean.TemplateBean templateBean)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/io/File.html" title="class or interface in java.io">File</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#getTemplateFile(com.nomagic.magicdraw.magicreport.ui.bean.TemplateBean,boolean)">getTemplateFile</a><wbr/>(com.nomagic.magicdraw.magicreport.ui.bean.TemplateBean templateBean,
 boolean revolveDir)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#getTemplateType(java.lang.String)">getTemplateType</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> extension)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Consider template type from file extension.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#getViewerReportKey(com.nomagic.magicdraw.magicreport.ui.bean.ReportBean)">getViewerReportKey</a><wbr/>(com.nomagic.magicdraw.magicreport.ui.bean.ReportBean reportBean)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Return a key for viewer report preference.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static com.nomagic.magicdraw.magicreport.ui.bean.TemplateBean</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#importZip(java.io.File,boolean)">importZip</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/io/File.html" title="class or interface in java.io">File</a> zipFile,
 boolean copyToData)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Import zip file to template bean.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static com.nomagic.magicdraw.magicreport.ui.bean.TemplateBean</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#importZip(java.io.File,boolean,com.nomagic.task.ProgressStatus)">importZip</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/io/File.html" title="class or interface in java.io">File</a> zipFile,
 boolean copyToData,
 <a href="../../../task/ProgressStatus.html" title="interface in com.nomagic.task">ProgressStatus</a> progress)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Import zip file to template bean.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static boolean</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#isFileExternal(java.io.File,com.nomagic.magicdraw.magicreport.ui.bean.TemplateBean)">isFileExternal</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/io/File.html" title="class or interface in java.io">File</a> file,
 com.nomagic.magicdraw.magicreport.ui.bean.TemplateBean templateBean)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a><wbr/>&lt;com.nomagic.magicdraw.magicreport.ui.bean.TemplateBean&gt;</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#listAvailableTemplates(com.nomagic.magicdraw.lic.MDVersion,com.nomagic.magicdraw.usermodes.UserMode)">listAvailableTemplates</a><wbr/>(com.nomagic.magicdraw.lic.MDVersion version,
 com.nomagic.magicdraw.usermodes.UserMode userMode)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Return a list of available template to MDVersion and Perspective.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#listMRZipTemplates()">listMRZipTemplates</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Load and Unzip MRZip template file from template directory.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a><wbr/>&lt;com.nomagic.magicdraw.magicreport.ui.bean.TemplateBean&gt;</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#listTemplates()">listTemplates</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">This method will automatically load all template file from "data" directory of report plugin and return a
 List of <code>TemplateBean</code>.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a><wbr/>&lt;com.nomagic.magicdraw.magicreport.ui.bean.TemplateBean&gt;</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#listTemplates(boolean)">listTemplates</a><wbr/>(boolean forceReload)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Load all template files from report plugin "data" directory and return to List of <code>TemplateBean</code>.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static com.nomagic.magicdraw.magicreport.ui.bean.ReportBean</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#loadReport(java.io.File)">loadReport</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/io/File.html" title="class or interface in java.io">File</a> reportFile)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Create a <code>ReportBean</code> from given reportFile.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#loadReportDataAndConfig(java.io.File,com.nomagic.magicdraw.magicreport.ui.bean.TemplateBean)">loadReportDataAndConfig</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/io/File.html" title="class or interface in java.io">File</a> templateDir,
 com.nomagic.magicdraw.magicreport.ui.bean.TemplateBean templateBean)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static com.nomagic.magicdraw.magicreport.ui.bean.TemplateBean</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#loadTemplate(java.io.File)">loadTemplate</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/io/File.html" title="class or interface in java.io">File</a> templateFile)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Create a <code>TemplateBean</code> from given templateFile.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static com.nomagic.magicdraw.magicreport.ui.bean.TemplateBean</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#loadTemplate(java.io.File,boolean)">loadTemplate</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/io/File.html" title="class or interface in java.io">File</a> templateFile,
 boolean checkValid)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Create a <code>TemplateBean</code> from given templateFile.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#loadTemplateBean(com.nomagic.magicdraw.magicreport.ui.bean.TemplateBean,org.w3c.dom.Document)">loadTemplateBean</a><wbr/>(com.nomagic.magicdraw.magicreport.ui.bean.TemplateBean templateBean,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.xml/org/w3c/dom/Document.html" title="class or interface in org.w3c.dom">Document</a> document)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static com.nomagic.magicdraw.magicreport.ui.bean.TemplateBean</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#loadTemplateBean(java.io.File)">loadTemplateBean</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/io/File.html" title="class or interface in java.io">File</a> file)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static com.nomagic.magicdraw.magicreport.ui.bean.TemplateBean</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#reloadTemplate(com.nomagic.magicdraw.magicreport.ui.bean.TemplateBean)">reloadTemplate</a><wbr/>(com.nomagic.magicdraw.magicreport.ui.bean.TemplateBean templateBean)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Force the application to remove this template from cache and then reload it from file.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#removeImportHistory(java.io.File%5B%5D)">removeImportHistory</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/io/File.html" title="class or interface in java.io">File</a>[] importedMrzipFiles)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#removePropertyChangeListener(java.beans.PropertyChangeListener)">removePropertyChangeListener</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.desktop/java/beans/PropertyChangeListener.html" title="class or interface in java.beans">PropertyChangeListener</a> listener)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Remove a listener for the PropertyChange event.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#removeTemplate(com.nomagic.magicdraw.magicreport.ui.bean.TemplateBean)">removeTemplate</a><wbr/>(com.nomagic.magicdraw.magicreport.ui.bean.TemplateBean templateBean)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Delete a template file from physical storage.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#saveReport(com.nomagic.magicdraw.magicreport.ui.bean.ReportBean)">saveReport</a><wbr/>(com.nomagic.magicdraw.magicreport.ui.bean.ReportBean reportBean)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Create a new report file from ReportBean.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#saveReport(com.nomagic.magicdraw.magicreport.ui.bean.TemplateBean,com.nomagic.magicdraw.magicreport.ui.bean.ReportBean)">saveReport</a><wbr/>(com.nomagic.magicdraw.magicreport.ui.bean.TemplateBean templateBean,
 com.nomagic.magicdraw.magicreport.ui.bean.ReportBean reportBean)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Create a new report file from ReportBean.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#saveTemplate(com.nomagic.magicdraw.magicreport.ui.bean.TemplateBean)">saveTemplate</a><wbr/>(com.nomagic.magicdraw.magicreport.ui.bean.TemplateBean templateBean)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Create a new template file from TemplateBean.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#unzipMRZipTemplates(java.io.File%5B%5D)">unzipMRZipTemplates</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/io/File.html" title="class or interface in java.io">File</a>[] mrZipFile)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Unzip MRZip Templates files.</div>
</div>
</div>
</div>
</div>
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
<section class="detail" id="TEMPLATE_EXTENSION">
<h3>TEMPLATE_EXTENSION</h3>
<div class="member-signature"><span class="modifiers">public static final</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">TEMPLATE_EXTENSION</span></div>
<div class="block">Constants for template extension.</div>
<dl class="notes">
<dt>See Also:</dt>
<dd>
<ul class="tag-list">
<li><a href="../../../../../constant-values.html#com.nomagic.magicdraw.magicreport.helper.TemplateHelper.TEMPLATE_EXTENSION">Constant Field Values</a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="PROPERTY_SAVE">
<h3>PROPERTY_SAVE</h3>
<div class="member-signature"><span class="modifiers">public static final</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">PROPERTY_SAVE</span></div>
<div class="block">Save property name.</div>
<dl class="notes">
<dt>See Also:</dt>
<dd>
<ul class="tag-list">
<li><a href="../../../../../constant-values.html#com.nomagic.magicdraw.magicreport.helper.TemplateHelper.PROPERTY_SAVE">Constant Field Values</a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="PROPERTY_DELETE">
<h3>PROPERTY_DELETE</h3>
<div class="member-signature"><span class="modifiers">public static final</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">PROPERTY_DELETE</span></div>
<div class="block">Delete property name.</div>
<dl class="notes">
<dt>See Also:</dt>
<dd>
<ul class="tag-list">
<li><a href="../../../../../constant-values.html#com.nomagic.magicdraw.magicreport.helper.TemplateHelper.PROPERTY_DELETE">Constant Field Values</a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="PROPERTY_CREATE">
<h3>PROPERTY_CREATE</h3>
<div class="member-signature"><span class="modifiers">public static final</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">PROPERTY_CREATE</span></div>
<dl class="notes">
<dt>See Also:</dt>
<dd>
<ul class="tag-list">
<li><a href="../../../../../constant-values.html#com.nomagic.magicdraw.magicreport.helper.TemplateHelper.PROPERTY_CREATE">Constant Field Values</a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="PROPERTY_RELOAD">
<h3>PROPERTY_RELOAD</h3>
<div class="member-signature"><span class="modifiers">public static final</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">PROPERTY_RELOAD</span></div>
<div class="block">Reload property name.</div>
<dl class="notes">
<dt>See Also:</dt>
<dd>
<ul class="tag-list">
<li><a href="../../../../../constant-values.html#com.nomagic.magicdraw.magicreport.helper.TemplateHelper.PROPERTY_RELOAD">Constant Field Values</a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="HTML">
<h3>HTML</h3>
<div class="member-signature"><span class="modifiers">public static final</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">HTML</span></div>
<div class="block">Constants for HTML type.</div>
<dl class="notes">
<dt>See Also:</dt>
<dd>
<ul class="tag-list">
<li><a href="../../../../../constant-values.html#com.nomagic.magicdraw.magicreport.helper.TemplateHelper.HTML">Constant Field Values</a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="RTF">
<h3>RTF</h3>
<div class="member-signature"><span class="modifiers">public static final</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">RTF</span></div>
<div class="block">Constants for RTF type.</div>
<dl class="notes">
<dt>See Also:</dt>
<dd>
<ul class="tag-list">
<li><a href="../../../../../constant-values.html#com.nomagic.magicdraw.magicreport.helper.TemplateHelper.RTF">Constant Field Values</a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="XML">
<h3>XML</h3>
<div class="member-signature"><span class="modifiers">public static final</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">XML</span></div>
<div class="block">Constants for XML type.</div>
<dl class="notes">
<dt>See Also:</dt>
<dd>
<ul class="tag-list">
<li><a href="../../../../../constant-values.html#com.nomagic.magicdraw.magicreport.helper.TemplateHelper.XML">Constant Field Values</a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="TXT">
<h3>TXT</h3>
<div class="member-signature"><span class="modifiers">public static final</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">TXT</span></div>
<div class="block">Constants for TXT type.</div>
<dl class="notes">
<dt>See Also:</dt>
<dd>
<ul class="tag-list">
<li><a href="../../../../../constant-values.html#com.nomagic.magicdraw.magicreport.helper.TemplateHelper.TXT">Constant Field Values</a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="ODT">
<h3>ODT</h3>
<div class="member-signature"><span class="modifiers">public static final</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">ODT</span></div>
<div class="block">Constants for ODT type.</div>
<dl class="notes">
<dt>See Also:</dt>
<dd>
<ul class="tag-list">
<li><a href="../../../../../constant-values.html#com.nomagic.magicdraw.magicreport.helper.TemplateHelper.ODT">Constant Field Values</a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="ODS">
<h3>ODS</h3>
<div class="member-signature"><span class="modifiers">public static final</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">ODS</span></div>
<div class="block">Constants for ODS type.</div>
<dl class="notes">
<dt>See Also:</dt>
<dd>
<ul class="tag-list">
<li><a href="../../../../../constant-values.html#com.nomagic.magicdraw.magicreport.helper.TemplateHelper.ODS">Constant Field Values</a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="ODP">
<h3>ODP</h3>
<div class="member-signature"><span class="modifiers">public static final</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">ODP</span></div>
<div class="block">Constants for ODP type.</div>
<dl class="notes">
<dt>See Also:</dt>
<dd>
<ul class="tag-list">
<li><a href="../../../../../constant-values.html#com.nomagic.magicdraw.magicreport.helper.TemplateHelper.ODP">Constant Field Values</a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="DOCX">
<h3>DOCX</h3>
<div class="member-signature"><span class="modifiers">public static final</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">DOCX</span></div>
<div class="block">Constants for DOCX type.</div>
<dl class="notes">
<dt>See Also:</dt>
<dd>
<ul class="tag-list">
<li><a href="../../../../../constant-values.html#com.nomagic.magicdraw.magicreport.helper.TemplateHelper.DOCX">Constant Field Values</a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="XLSX">
<h3>XLSX</h3>
<div class="member-signature"><span class="modifiers">public static final</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">XLSX</span></div>
<div class="block">Constants for XLSX type.</div>
<dl class="notes">
<dt>See Also:</dt>
<dd>
<ul class="tag-list">
<li><a href="../../../../../constant-values.html#com.nomagic.magicdraw.magicreport.helper.TemplateHelper.XLSX">Constant Field Values</a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="PPTX">
<h3>PPTX</h3>
<div class="member-signature"><span class="modifiers">public static final</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">PPTX</span></div>
<div class="block">Constants for PPTX type.</div>
<dl class="notes">
<dt>See Also:</dt>
<dd>
<ul class="tag-list">
<li><a href="../../../../../constant-values.html#com.nomagic.magicdraw.magicreport.helper.TemplateHelper.PPTX">Constant Field Values</a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="DBK">
<h3>DBK</h3>
<div class="member-signature"><span class="modifiers">public static final</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">DBK</span></div>
<div class="block">Constants for Default DOCBOOK type.</div>
<dl class="notes">
<dt>See Also:</dt>
<dd>
<ul class="tag-list">
<li><a href="../../../../../constant-values.html#com.nomagic.magicdraw.magicreport.helper.TemplateHelper.DBK">Constant Field Values</a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="DOCBOOK">
<h3>DOCBOOK</h3>
<div class="member-signature"><span class="modifiers">public static final</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">DOCBOOK</span></div>
<div class="block">Constants for DOCBOOK type.</div>
<dl class="notes">
<dt>See Also:</dt>
<dd>
<ul class="tag-list">
<li><a href="../../../../../constant-values.html#com.nomagic.magicdraw.magicreport.helper.TemplateHelper.DOCBOOK">Constant Field Values</a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="DESCRIPTOR_FILE">
<h3>DESCRIPTOR_FILE</h3>
<div class="member-signature"><span class="modifiers">public static final</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">DESCRIPTOR_FILE</span></div>
<dl class="notes">
<dt>See Also:</dt>
<dd>
<ul class="tag-list">
<li><a href="../../../../../constant-values.html#com.nomagic.magicdraw.magicreport.helper.TemplateHelper.DESCRIPTOR_FILE">Constant Field Values</a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="LOG">
<h3>LOG</h3>
<div class="member-signature"><span class="modifiers">public static final</span> <span class="return-type">org.apache.logging.log4j.Logger</span> <span class="element-name">LOG</span></div>
</section>
</li>
</ul>
</section>
</li>
<!-- ========= CONSTRUCTOR DETAIL ======== -->
<li>
<section class="constructor-details" id="constructor-detail">
<h2>Constructor Details</h2>
<ul class="member-list">
<li>
<section class="detail" id="&lt;init&gt;()">
<h3>TemplateHelper</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="element-name">TemplateHelper</span>()</div>
</section>
</li>
</ul>
</section>
</li>
<!-- ============ METHOD DETAIL ========== -->
<li>
<section class="method-details" id="method-detail">
<h2>Method Details</h2>
<ul class="member-list">
<li>
<section class="detail" id="listTemplates()">
<h3>listTemplates</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;com.nomagic.magicdraw.magicreport.ui.bean.TemplateBean&gt;</span> <span class="element-name">listTemplates</span>()</div>
<div class="block">This method will automatically load all template file from "data" directory of report plugin and return a
 List of <code>TemplateBean</code>. <code>TemplateBean</code> is a container of template information.</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>a List of <code>TemplateBean</code> from "data" directory.</dd>
<dt>See Also:</dt>
<dd>
<ul class="tag-list-long">
<li><a href="#listTemplates(boolean)"><code>listTemplates(boolean)</code></a></li>
<li><a href="#listAvailableTemplates(com.nomagic.magicdraw.lic.MDVersion,com.nomagic.magicdraw.usermodes.UserMode)"><code>listAvailableTemplates(MDVersion, UserMode)</code></a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="listAvailableTemplates(com.nomagic.magicdraw.lic.MDVersion,com.nomagic.magicdraw.usermodes.UserMode)">
<h3>listAvailableTemplates</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;com.nomagic.magicdraw.magicreport.ui.bean.TemplateBean&gt;</span> <span class="element-name">listAvailableTemplates</span><wbr/><span class="parameters">(@CheckForNull
 com.nomagic.magicdraw.lic.MDVersion version,
 @CheckForNull
 com.nomagic.magicdraw.usermodes.UserMode userMode)</span></div>
<div class="block">Return a list of available template to MDVersion and Perspective.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>version</code> - MDVersion</dd>
<dd><code>userMode</code> - UserMode</dd>
<dt>Returns:</dt>
<dd>a list of available template after filter out</dd>
<dt>See Also:</dt>
<dd>
<ul class="tag-list">
<li><a href="#listTemplates()"><code>listTemplates()</code></a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="checkEdition(com.nomagic.magicdraw.magicreport.ui.bean.TemplateBean,com.nomagic.magicdraw.lic.MDVersion)">
<h3>checkEdition</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type">boolean</span> <span class="element-name">checkEdition</span><wbr/><span class="parameters">(com.nomagic.magicdraw.magicreport.ui.bean.TemplateBean bean,
 @CheckForNull
 com.nomagic.magicdraw.lic.MDVersion version)</span></div>
<div class="block">Return true if this template is valid to MDVersion.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>version</code> - MDVersion</dd>
<dt>Returns:</dt>
<dd>true if this template is valid to given MDVersion; otherwise false.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="checkRequiredPlugins(com.nomagic.magicdraw.magicreport.ui.bean.TemplateBean)">
<h3>checkRequiredPlugins</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">checkRequiredPlugins</span><wbr/><span class="parameters">(com.nomagic.magicdraw.magicreport.ui.bean.TemplateBean bean)</span></div>
<dl class="notes">
<dt>Returns:</dt>
<dd>empty string if all required plugins are ok. Otherwise, a multiline info message for each missing/outdated plugin</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="addPropertyChangeListener(java.beans.PropertyChangeListener)">
<h3>addPropertyChangeListener</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type">void</span> <span class="element-name">addPropertyChangeListener</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.desktop/java/beans/PropertyChangeListener.html" title="class or interface in java.beans">PropertyChangeListener</a> listener)</span></div>
<div class="block">Register a listener for the PropertyChange event. When a Template changes its value it should fire a
 PropertyChange event on all registered PropertyChangeListeners.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>listener</code> - An object to be invoked when a PropertyChange event is fired.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="removePropertyChangeListener(java.beans.PropertyChangeListener)">
<h3>removePropertyChangeListener</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type">void</span> <span class="element-name">removePropertyChangeListener</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.desktop/java/beans/PropertyChangeListener.html" title="class or interface in java.beans">PropertyChangeListener</a> listener)</span></div>
<div class="block">Remove a listener for the PropertyChange event.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>listener</code> - The PropertyChange listener to be removed.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="firePropertyChange(java.lang.Object,java.lang.String,java.lang.Object,java.lang.Object)">
<h3>firePropertyChange</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type">void</span> <span class="element-name">firePropertyChange</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a> source,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> propertyName,
 @CheckForNull
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a> oldValue,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a> newValue)</span></div>
<div class="block">Report a bound property update to any registered listeners. No event is fired if old and new are equal and
 non-null.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>source</code> - property source</dd>
<dd><code>propertyName</code> - The programmatic name of the property that was changed.</dd>
<dd><code>oldValue</code> - The old value of the property.</dd>
<dd><code>newValue</code> - The new value of the property.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="firePropertyChange(java.beans.PropertyChangeEvent)">
<h3>firePropertyChange</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type">void</span> <span class="element-name">firePropertyChange</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.desktop/java/beans/PropertyChangeEvent.html" title="class or interface in java.beans">PropertyChangeEvent</a> evt)</span></div>
<div class="block">Fire an existing PropertyChangeEvent to any registered listeners. No event is fired if the given event's old
 and new values are equal and non-null.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>evt</code> - The PropertyChangeEvent object.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="listTemplates(boolean)">
<h3>listTemplates</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;com.nomagic.magicdraw.magicreport.ui.bean.TemplateBean&gt;</span> <span class="element-name">listTemplates</span><wbr/><span class="parameters">(boolean forceReload)</span></div>
<div class="block">Load all template files from report plugin "data" directory and return to List of <code>TemplateBean</code>.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>forceReload</code> - true if you want this method to reload template from disk; false use template from cache.</dd>
<dt>Returns:</dt>
<dd>a List of <code>TemplateBean</code> from "data" directory.</dd>
<dt>See Also:</dt>
<dd>
<ul class="tag-list">
<li><a href="#listTemplates()"><code>listTemplates()</code></a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="listMRZipTemplates()">
<h3>listMRZipTemplates</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type">void</span> <span class="element-name">listMRZipTemplates</span>()</div>
<div class="block">Load and Unzip MRZip template file from template directory.</div>
</section>
</li>
<li>
<section class="detail" id="unzipMRZipTemplates(java.io.File[])">
<h3>unzipMRZipTemplates</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type">void</span> <span class="element-name">unzipMRZipTemplates</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/io/File.html" title="class or interface in java.io">File</a>[] mrZipFile)</span></div>
<div class="block">Unzip MRZip Templates files.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>mrZipFile</code> - file</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="removeImportHistory(java.io.File[])">
<h3>removeImportHistory</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type">void</span> <span class="element-name">removeImportHistory</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/io/File.html" title="class or interface in java.io">File</a>[] importedMrzipFiles)</span></div>
</section>
</li>
<li>
<section class="detail" id="reloadTemplate(com.nomagic.magicdraw.magicreport.ui.bean.TemplateBean)">
<h3>reloadTemplate</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type">com.nomagic.magicdraw.magicreport.ui.bean.TemplateBean</span> <span class="element-name">reloadTemplate</span><wbr/><span class="parameters">(com.nomagic.magicdraw.magicreport.ui.bean.TemplateBean templateBean)</span></div>
<div class="block">Force the application to remove this template from cache and then reload it from file.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>templateBean</code> - a target template</dd>
<dt>Returns:</dt>
<dd>TemplateBean or null if invalid template file format.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getTemplateBean(java.lang.String)">
<h3>getTemplateBean</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type">com.nomagic.magicdraw.magicreport.ui.bean.TemplateBean</span> <span class="element-name">getTemplateBean</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> path)</span></div>
<div class="block">Return existing template bean from the template path.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>path</code> - path of template <code>TemplateBean.getPath()</code></dd>
<dt>Returns:</dt>
<dd>the <code>TemplateBean</code></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getTemplateBeanByName(java.lang.String,java.lang.String)">
<h3>getTemplateBeanByName</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type">com.nomagic.magicdraw.magicreport.ui.bean.TemplateBean</span> <span class="element-name">getTemplateBeanByName</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> catName,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> templateName)</span></div>
<div class="block">Get template bean by category name and template name</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>catName</code> - template category name</dd>
<dd><code>templateName</code> - template name</dd>
<dt>Returns:</dt>
<dd>template bean</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="loadTemplate(java.io.File)">
<h3>loadTemplate</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type">com.nomagic.magicdraw.magicreport.ui.bean.TemplateBean</span> <span class="element-name">loadTemplate</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/io/File.html" title="class or interface in java.io">File</a> templateFile)</span></div>
<div class="block">Create a <code>TemplateBean</code> from given templateFile. If template file is not valid template format, return
 null.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>templateFile</code> - a File for template</dd>
<dt>Returns:</dt>
<dd>TemplateBean or null if invalid template file format.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="loadTemplate(java.io.File,boolean)">
<h3>loadTemplate</h3>
<div class="member-signature"><span class="annotations">@CheckForNull
</span><span class="modifiers">public static</span> <span class="return-type">com.nomagic.magicdraw.magicreport.ui.bean.TemplateBean</span> <span class="element-name">loadTemplate</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/io/File.html" title="class or interface in java.io">File</a> templateFile,
 boolean checkValid)</span>
                                                                           throws <span class="exceptions"><a href="../../../magicreport/TemplateException.html" title="class in com.nomagic.magicreport">TemplateException</a></span></div>
<div class="block">Create a <code>TemplateBean</code> from given templateFile. If template file is not valid template format, return
 null.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>templateFile</code> - a File for template</dd>
<dd><code>checkValid</code> - true if this template file require format checking</dd>
<dt>Returns:</dt>
<dd>TemplateBean or null if invalid template file format.</dd>
<dt>Throws:</dt>
<dd><code><a href="../../../magicreport/TemplateException.html" title="class in com.nomagic.magicreport">TemplateException</a></code> - if the template file is not valid format and check parameter is true.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="loadReportDataAndConfig(java.io.File,com.nomagic.magicdraw.magicreport.ui.bean.TemplateBean)">
<h3>loadReportDataAndConfig</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type">void</span> <span class="element-name">loadReportDataAndConfig</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/io/File.html" title="class or interface in java.io">File</a> templateDir,
 com.nomagic.magicdraw.magicreport.ui.bean.TemplateBean templateBean)</span></div>
</section>
</li>
<li>
<section class="detail" id="importZip(java.io.File,boolean)">
<h3>importZip</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type">com.nomagic.magicdraw.magicreport.ui.bean.TemplateBean</span> <span class="element-name">importZip</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/io/File.html" title="class or interface in java.io">File</a> zipFile,
 boolean copyToData)</span>
                                                                        throws <span class="exceptions"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/io/IOException.html" title="class or interface in java.io">IOException</a></span></div>
<div class="block">Import zip file to template bean.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>zipFile</code> - an input zip file.</dd>
<dd><code>copyToData</code> - copy template to data folder after successfully extract.</dd>
<dt>Returns:</dt>
<dd>templateBean a template bean</dd>
<dt>Throws:</dt>
<dd><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/io/IOException.html" title="class or interface in java.io">IOException</a></code> - when unable to import zip file.</dd>
<dt>See Also:</dt>
<dd>
<ul class="tag-list-long">
<li><a href="#importZip(java.io.File,boolean,com.nomagic.task.ProgressStatus)"><code>importZip(File, boolean, ProgressStatus)</code></a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="importZip(java.io.File,boolean,com.nomagic.task.ProgressStatus)">
<h3>importZip</h3>
<div class="member-signature"><span class="annotations">@CheckForNull
</span><span class="modifiers">public static</span> <span class="return-type">com.nomagic.magicdraw.magicreport.ui.bean.TemplateBean</span> <span class="element-name">importZip</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/io/File.html" title="class or interface in java.io">File</a> zipFile,
 boolean copyToData,
 <a href="../../../task/ProgressStatus.html" title="interface in com.nomagic.task">ProgressStatus</a> progress)</span>
                                                                        throws <span class="exceptions"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/io/IOException.html" title="class or interface in java.io">IOException</a></span></div>
<div class="block">Import zip file to template bean.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>zipFile</code> - an input zip file.</dd>
<dd><code>copyToData</code> - copy template to data folder after successfully extract.</dd>
<dd><code>progress</code> - the progress status</dd>
<dt>Returns:</dt>
<dd>templateBean a template bean</dd>
<dt>Throws:</dt>
<dd><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/io/IOException.html" title="class or interface in java.io">IOException</a></code> - when unable to import zip file.</dd>
<dt>See Also:</dt>
<dd>
<ul class="tag-list-long">
<li><a href="#importZip(java.io.File,boolean)"><code>importZip(File, boolean)</code></a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="copyFiles(java.io.File,java.io.File)">
<h3>copyFiles</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type">void</span> <span class="element-name">copyFiles</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/io/File.html" title="class or interface in java.io">File</a> tmpFile,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/io/File.html" title="class or interface in java.io">File</a> templateFile)</span>
                      throws <span class="exceptions"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/io/IOException.html" title="class or interface in java.io">IOException</a></span></div>
<dl class="notes">
<dt>Throws:</dt>
<dd><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/io/IOException.html" title="class or interface in java.io">IOException</a></code></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="extractZip(java.io.File,java.io.File,com.nomagic.task.ProgressStatus)">
<h3>extractZip</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type">boolean</span> <span class="element-name">extractZip</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/io/File.html" title="class or interface in java.io">File</a> zipFile,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/io/File.html" title="class or interface in java.io">File</a> destinationDir,
 <a href="../../../task/ProgressStatus.html" title="interface in com.nomagic.task">ProgressStatus</a> progress)</span>
                          throws <span class="exceptions"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/io/IOException.html" title="class or interface in java.io">IOException</a></span></div>
<dl class="notes">
<dt>Throws:</dt>
<dd><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/io/IOException.html" title="class or interface in java.io">IOException</a></code></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="exportZip(java.io.File,com.nomagic.magicdraw.magicreport.ui.bean.TemplateBean)">
<h3>exportZip</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type">void</span> <span class="element-name">exportZip</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/io/File.html" title="class or interface in java.io">File</a> zipFile,
 com.nomagic.magicdraw.magicreport.ui.bean.TemplateBean templateBean)</span>
                      throws <span class="exceptions"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/io/IOException.html" title="class or interface in java.io">IOException</a></span></div>
<div class="block">Export template bean to zip file with default progress status.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>zipFile</code> - a output zip file.</dd>
<dd><code>templateBean</code> - a template bean</dd>
<dt>Throws:</dt>
<dd><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/io/IOException.html" title="class or interface in java.io">IOException</a></code> - when unable to export zip file.</dd>
<dt>See Also:</dt>
<dd>
<ul class="tag-list-long">
<li><a href="#exportZip(java.io.File,com.nomagic.magicdraw.magicreport.ui.bean.TemplateBean,com.nomagic.task.ProgressStatus)"><code>exportZip(File, TemplateBean, ProgressStatus)</code></a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="exportZip(java.io.File,com.nomagic.magicdraw.magicreport.ui.bean.TemplateBean,com.nomagic.task.ProgressStatus)">
<h3>exportZip</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type">void</span> <span class="element-name">exportZip</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/io/File.html" title="class or interface in java.io">File</a> zipFile,
 com.nomagic.magicdraw.magicreport.ui.bean.TemplateBean templateBean,
 <a href="../../../task/ProgressStatus.html" title="interface in com.nomagic.task">ProgressStatus</a> progress)</span>
                      throws <span class="exceptions"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/io/IOException.html" title="class or interface in java.io">IOException</a></span></div>
<div class="block">Export template bean to zip file.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>zipFile</code> - a output zip file.</dd>
<dd><code>templateBean</code> - a template bean</dd>
<dd><code>progress</code> - the progress status</dd>
<dt>Throws:</dt>
<dd><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/io/IOException.html" title="class or interface in java.io">IOException</a></code> - when unable to export zip file.</dd>
<dt>See Also:</dt>
<dd>
<ul class="tag-list-long">
<li><a href="#exportZip(java.io.File,com.nomagic.magicdraw.magicreport.ui.bean.TemplateBean)"><code>exportZip(File, TemplateBean)</code></a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="exportZip(java.io.File,com.nomagic.magicdraw.magicreport.ui.bean.TemplateBean,com.nomagic.task.ProgressStatus,java.util.List)">
<h3>exportZip</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type">void</span> <span class="element-name">exportZip</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/io/File.html" title="class or interface in java.io">File</a> zipFile,
 com.nomagic.magicdraw.magicreport.ui.bean.TemplateBean templateBean,
 <a href="../../../task/ProgressStatus.html" title="interface in com.nomagic.task">ProgressStatus</a> progress,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/io/File.html" title="class or interface in java.io">File</a>&gt; includedFiles)</span>
                      throws <span class="exceptions"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/io/IOException.html" title="class or interface in java.io">IOException</a></span></div>
<div class="block">Export template bean to zip file.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>zipFile</code> - a output zip file.</dd>
<dd><code>templateBean</code> - a template bean</dd>
<dd><code>progress</code> - the progress status</dd>
<dd><code>includedFiles</code> - other files to be included in this zip</dd>
<dt>Throws:</dt>
<dd><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/io/IOException.html" title="class or interface in java.io">IOException</a></code> - when unable to export zip file.</dd>
<dt>See Also:</dt>
<dd>
<ul class="tag-list-long">
<li><a href="#exportZip(java.io.File,com.nomagic.magicdraw.magicreport.ui.bean.TemplateBean)"><code>exportZip(File, TemplateBean)</code></a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="isFileExternal(java.io.File,com.nomagic.magicdraw.magicreport.ui.bean.TemplateBean)">
<h3>isFileExternal</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type">boolean</span> <span class="element-name">isFileExternal</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/io/File.html" title="class or interface in java.io">File</a> file,
 com.nomagic.magicdraw.magicreport.ui.bean.TemplateBean templateBean)</span></div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>file</code> - to check</dd>
<dd><code>templateBean</code> - </dd>
<dt>Returns:</dt>
<dd>true if checked file resides outside the template package</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getTemplateFile(com.nomagic.magicdraw.magicreport.ui.bean.TemplateBean)">
<h3>getTemplateFile</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/io/File.html" title="class or interface in java.io">File</a></span> <span class="element-name">getTemplateFile</span><wbr/><span class="parameters">(com.nomagic.magicdraw.magicreport.ui.bean.TemplateBean templateBean)</span></div>
</section>
</li>
<li>
<section class="detail" id="getTemplateFile(com.nomagic.magicdraw.magicreport.ui.bean.TemplateBean,boolean)">
<h3>getTemplateFile</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/io/File.html" title="class or interface in java.io">File</a></span> <span class="element-name">getTemplateFile</span><wbr/><span class="parameters">(com.nomagic.magicdraw.magicreport.ui.bean.TemplateBean templateBean,
 boolean revolveDir)</span></div>
</section>
</li>
<li>
<section class="detail" id="loadReport(java.io.File)">
<h3>loadReport</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type">com.nomagic.magicdraw.magicreport.ui.bean.ReportBean</span> <span class="element-name">loadReport</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/io/File.html" title="class or interface in java.io">File</a> reportFile)</span></div>
<div class="block">Create a <code>ReportBean</code> from given reportFile. If report file is not valid report format, return null.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>reportFile</code> - a File for report</dd>
<dt>Returns:</dt>
<dd>ReportBean or null if invalid report file format.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="saveTemplate(com.nomagic.magicdraw.magicreport.ui.bean.TemplateBean)">
<h3>saveTemplate</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type">void</span> <span class="element-name">saveTemplate</span><wbr/><span class="parameters">(com.nomagic.magicdraw.magicreport.ui.bean.TemplateBean templateBean)</span>
                         throws <span class="exceptions"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/io/IOException.html" title="class or interface in java.io">IOException</a></span></div>
<div class="block">Create a new template file from TemplateBean. If <code>TemplateBean.getPath()</code> exists, write a template
 file to this value; if value doesn't exists create a new file with <code>TemplateBean.getName()</code> as
 template filename.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>templateBean</code> - a Template Bean</dd>
<dt>Throws:</dt>
<dd><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/io/IOException.html" title="class or interface in java.io">IOException</a></code> - if the template was not successfully created</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="loadTemplateBean(java.io.File)">
<h3>loadTemplateBean</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type">com.nomagic.magicdraw.magicreport.ui.bean.TemplateBean</span> <span class="element-name">loadTemplateBean</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/io/File.html" title="class or interface in java.io">File</a> file)</span>
                                                                               throws <span class="exceptions"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/io/IOException.html" title="class or interface in java.io">IOException</a></span></div>
<dl class="notes">
<dt>Throws:</dt>
<dd><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/io/IOException.html" title="class or interface in java.io">IOException</a></code></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="loadTemplateBean(com.nomagic.magicdraw.magicreport.ui.bean.TemplateBean,org.w3c.dom.Document)">
<h3>loadTemplateBean</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type">void</span> <span class="element-name">loadTemplateBean</span><wbr/><span class="parameters">(com.nomagic.magicdraw.magicreport.ui.bean.TemplateBean templateBean,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.xml/org/w3c/dom/Document.html" title="class or interface in org.w3c.dom">Document</a> document)</span>
                             throws <span class="exceptions"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/io/IOException.html" title="class or interface in java.io">IOException</a></span></div>
<dl class="notes">
<dt>Throws:</dt>
<dd><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/io/IOException.html" title="class or interface in java.io">IOException</a></code></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="saveReport(com.nomagic.magicdraw.magicreport.ui.bean.TemplateBean,com.nomagic.magicdraw.magicreport.ui.bean.ReportBean)">
<h3>saveReport</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type">void</span> <span class="element-name">saveReport</span><wbr/><span class="parameters">(com.nomagic.magicdraw.magicreport.ui.bean.TemplateBean templateBean,
 com.nomagic.magicdraw.magicreport.ui.bean.ReportBean reportBean)</span>
                       throws <span class="exceptions"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/io/IOException.html" title="class or interface in java.io">IOException</a></span></div>
<div class="block">Create a new report file from ReportBean. If <code>ReportBean.getFileName()</code> exists, write a report file to
 this value; if value doesn't exists create a new file with <code>TemplateBean.getName()</code> as template
 filename.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>templateBean</code> - a TemplateBean</dd>
<dd><code>reportBean</code> - a ReportBean</dd>
<dt>Throws:</dt>
<dd><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/io/IOException.html" title="class or interface in java.io">IOException</a></code> - if the template was not successfully created</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="saveReport(com.nomagic.magicdraw.magicreport.ui.bean.ReportBean)">
<h3>saveReport</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type">void</span> <span class="element-name">saveReport</span><wbr/><span class="parameters">(com.nomagic.magicdraw.magicreport.ui.bean.ReportBean reportBean)</span>
                       throws <span class="exceptions"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/io/IOException.html" title="class or interface in java.io">IOException</a></span></div>
<div class="block">Create a new report file from ReportBean. If <code>ReportBean.getFileName()</code> exists, write a report file to
 this value; if value doesn't exists throw IOException.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>reportBean</code> - a ReportBean</dd>
<dt>Throws:</dt>
<dd><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/io/IOException.html" title="class or interface in java.io">IOException</a></code> - if the report was not successfully created</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="removeTemplate(com.nomagic.magicdraw.magicreport.ui.bean.TemplateBean)">
<h3>removeTemplate</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type">void</span> <span class="element-name">removeTemplate</span><wbr/><span class="parameters">(com.nomagic.magicdraw.magicreport.ui.bean.TemplateBean templateBean)</span>
                           throws <span class="exceptions"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/io/IOException.html" title="class or interface in java.io">IOException</a></span></div>
<div class="block">Delete a template file from physical storage. Physical storage meaning that template file will not be able
 to recovery after successfully deleted.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>templateBean</code> - a Template Bean</dd>
<dt>Throws:</dt>
<dd><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/io/IOException.html" title="class or interface in java.io">IOException</a></code> - if the template was not successfully deleted</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="createTemplateFile(com.nomagic.magicdraw.magicreport.ui.bean.TemplateBean)">
<h3>createTemplateFile</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/io/File.html" title="class or interface in java.io">File</a></span> <span class="element-name">createTemplateFile</span><wbr/><span class="parameters">(com.nomagic.magicdraw.magicreport.ui.bean.TemplateBean templateBean)</span>
                               throws <span class="exceptions"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/io/IOException.html" title="class or interface in java.io">IOException</a></span></div>
<div class="block">Create a directory or file from given template bean. This method use template name as a directory name.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>templateBean</code> - a template bean</dd>
<dt>Returns:</dt>
<dd>File references to template bean</dd>
<dt>Throws:</dt>
<dd><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/io/IOException.html" title="class or interface in java.io">IOException</a></code> - if false to create directory.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="createTemplateFile(java.lang.String)">
<h3>createTemplateFile</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/io/File.html" title="class or interface in java.io">File</a></span> <span class="element-name">createTemplateFile</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> templateName)</span>
                               throws <span class="exceptions"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/io/IOException.html" title="class or interface in java.io">IOException</a></span></div>
<div class="block">Create a directory or file from given template name.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>templateName</code> - a template name</dd>
<dt>Returns:</dt>
<dd>File references to template bean</dd>
<dt>Throws:</dt>
<dd><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/io/IOException.html" title="class or interface in java.io">IOException</a></code> - if false to create directory.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="findTemplateBean(java.lang.String,java.lang.String)">
<h3>findTemplateBean</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type">com.nomagic.magicdraw.magicreport.ui.bean.TemplateBean</span> <span class="element-name">findTemplateBean</span><wbr/><span class="parameters">(@CheckForNull
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> catName,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> templName)</span></div>
<div class="block">Get the templateBean by given category name and template name.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>catName</code> - categoryName or null</dd>
<dd><code>templName</code> - the template name</dd>
<dt>Returns:</dt>
<dd>the TemplateBean</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getTemplateType(java.lang.String)">
<h3>getTemplateType</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">getTemplateType</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> extension)</span></div>
<div class="block">Consider template type from file extension.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>extension</code> - a file extension.</dd>
<dt>Returns:</dt>
<dd>a template type.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="createTemplateIcon(com.nomagic.magicdraw.magicreport.ui.bean.TemplateBean)">
<h3>createTemplateIcon</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.desktop/javax/swing/Icon.html" title="class or interface in javax.swing">Icon</a></span> <span class="element-name">createTemplateIcon</span><wbr/><span class="parameters">(com.nomagic.magicdraw.magicreport.ui.bean.TemplateBean templateBean)</span></div>
<div class="block">Create and return icon for this template bean.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>templateBean</code> - a template bean</dd>
<dt>Returns:</dt>
<dd>template icon</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getIconByFileExtension(java.lang.String)">
<h3>getIconByFileExtension</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type"><a href="../../../ui/ResizableIcon.html" title="interface in com.nomagic.ui">ResizableIcon</a></span> <span class="element-name">getIconByFileExtension</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> ext)</span></div>
</section>
</li>
<li>
<section class="detail" id="getDefaultReportKey(com.nomagic.magicdraw.magicreport.ui.bean.TemplateBean)">
<h3>getDefaultReportKey</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">getDefaultReportKey</span><wbr/><span class="parameters">(com.nomagic.magicdraw.magicreport.ui.bean.TemplateBean templateBean)</span>
                                  throws <span class="exceptions"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/IllegalArgumentException.html" title="class or interface in java.lang">IllegalArgumentException</a></span></div>
<div class="block">Return a key for default report preference. A key is a concatenation of <code>#hashCode()</code> and ";default".</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>templateBean</code> - a template bean</dd>
<dt>Returns:</dt>
<dd>a key.</dd>
<dt>Throws:</dt>
<dd><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/IllegalArgumentException.html" title="class or interface in java.lang">IllegalArgumentException</a></code> - illegal argument is used.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getOutputReportKey(com.nomagic.magicdraw.magicreport.ui.bean.ReportBean)">
<h3>getOutputReportKey</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">getOutputReportKey</span><wbr/><span class="parameters">(com.nomagic.magicdraw.magicreport.ui.bean.ReportBean reportBean)</span>
                                 throws <span class="exceptions"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/IllegalArgumentException.html" title="class or interface in java.lang">IllegalArgumentException</a></span></div>
<div class="block">Return a key for output report preference. A key is a concatenation of 
<details class="invalid-tag">
<summary>invalid @link</summary>
<pre>{@link ReportBean#getModel()#getID()</pre>
</details>
}
 and ";output" or 
<details class="invalid-tag">
<summary>invalid @link</summary>
<pre>{@link ReportBean#getFileName()#hashCode()</pre>
</details>
} + ";output".</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>reportBean</code> - a report bean</dd>
<dt>Returns:</dt>
<dd>a key.</dd>
<dt>Throws:</dt>
<dd><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/IllegalArgumentException.html" title="class or interface in java.lang">IllegalArgumentException</a></code> - illegal argument is used.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getViewerReportKey(com.nomagic.magicdraw.magicreport.ui.bean.ReportBean)">
<h3>getViewerReportKey</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">getViewerReportKey</span><wbr/><span class="parameters">(com.nomagic.magicdraw.magicreport.ui.bean.ReportBean reportBean)</span>
                                 throws <span class="exceptions"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/IllegalArgumentException.html" title="class or interface in java.lang">IllegalArgumentException</a></span></div>
<div class="block">Return a key for viewer report preference. A key is a concatenation of 
<details class="invalid-tag">
<summary>invalid @link</summary>
<pre>{@link ReportBean#getModel()#getID()</pre>
</details>
}
 and ";viewer" or 
<details class="invalid-tag">
<summary>invalid @link</summary>
<pre>{@link ReportBean#getFileName()#hashCode()</pre>
</details>
} + ";viewer".</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>reportBean</code> - a report bean</dd>
<dt>Returns:</dt>
<dd>a key.</dd>
<dt>Throws:</dt>
<dd><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/IllegalArgumentException.html" title="class or interface in java.lang">IllegalArgumentException</a></code> - illegal argument is used.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getCustomTemplateLocations()">
<h3>getCustomTemplateLocations</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Set.html" title="class or interface in java.util">Set</a>&lt;<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/io/File.html" title="class or interface in java.io">File</a>&gt;</span> <span class="element-name">getCustomTemplateLocations</span>()</div>
<div class="block">Get custom location that store template.</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>list of custom location</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="clearCachedElements()">
<h3>clearCachedElements</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type">void</span> <span class="element-name">clearCachedElements</span>()</div>
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
