# JAVA OPENAPI: HTMLHelper (2026x Refresh1 API)

- source_url: https://jdocs.nomagic.com/2026xRefresh1/com/nomagic/magicdraw/uml/symbols/shapes/html/HTMLHelper.html
- source_path: `com/nomagic/magicdraw/uml/symbols/shapes/html/HTMLHelper.html`
- source_sha256: `f9c7740eabff91d0bc25539329c3f93c9c969d3c307be8d2470d38af41cea484`
- captured_utc: `2026-07-14T16:46:08.540914+00:00`

## NORMALIZED JAVADOC CONTENT

======== START OF CLASS DATA ========

Package [com.nomagic.magicdraw.uml.symbols.shapes.html](package-summary.html)

## Class HTMLHelper

[java.lang.Object](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html)
com.nomagic.magicdraw.uml.symbols.shapes.html.HTMLHelper

@OpenApiAllpublic classHTMLHelper
extends [Object](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html)
The class is used for HTML document creation.

=========== FIELD SUMMARY =========== 
Field Summary
Fields
Modifier and Type
Field
Description
`static final [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html)`
`[MD_ICON_TAG](#MD_ICON_TAG)`
 ======== CONSTRUCTOR SUMMARY ======== 
Constructor Summary
Constructors
Constructor
Description
`[HTMLHelper](#%3Cinit%3E())()`
 ========== METHOD SUMMARY =========== 
Method Summary
All MethodsStatic MethodsConcrete MethodsDeprecated Methods
Modifier and Type
Method
Description
`static [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html)`
`[applyFontSizeStyleSheetColorOnP](#applyFontSizeStyleSheetColorOnP(java.lang.String,java.awt.Font,boolean,int,int,int))([String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) html,
 [Font](https://docs.oracle.com/en/java/javase/21/docs/api/java.desktop/java/awt/Font.html) font,
 boolean ptUnits,
 int red,
 int green,
 int blue)`
Deprecated.
use `HtmlStyleUtils.applyFontSizeStyleSheetColorOnP(String, Font, boolean, int, int, int)`
`static [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html)`
`[applyFontSizeStyleSheetOnP](#applyFontSizeStyleSheetOnP(java.lang.String,java.awt.Font,boolean))([String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) html,
 [Font](https://docs.oracle.com/en/java/javase/21/docs/api/java.desktop/java/awt/Font.html) font,
 boolean ptUnits)`
Deprecated.
use `HtmlStyleUtils.applyFontSizeStyleSheetOnP(String, Font, boolean)`
`static void`
`[applyStyleSheet](#applyStyleSheet(javax.swing.text.html.StyleSheet,com.nomagic.magicdraw.uml.symbols.shapes.TextObject,boolean))([StyleSheet](https://docs.oracle.com/en/java/javase/21/docs/api/java.desktop/javax/swing/text/html/StyleSheet.html) styles,
 com.nomagic.magicdraw.uml.symbols.shapes.TextObject obj,
 boolean takeZoomFactor)`
Changes the properties of the given style sheet according to the properties of the given text object.
`static [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html)`
`[constructHTMLText](#constructHTMLText(java.lang.String))([String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) text)`
Deprecated.
use [`HtmlTextUtils.toHtmlText(String)`](../../../../../text/html/HtmlTextUtils.html#toHtmlText(java.lang.String))
`static [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html)`
`[constructHTMLText](#constructHTMLText(java.lang.String,boolean,boolean))([String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) text,
 boolean convertCharacters,
 boolean addEnterAfterP)`
Deprecated.
use `HtmlTextUtilsInternal.toHtmlText(String, boolean, boolean)`
`static [HTMLDocument](https://docs.oracle.com/en/java/javase/21/docs/api/java.desktop/javax/swing/text/html/HTMLDocument.html)`
`[createDefaultDocument](#createDefaultDocument(com.nomagic.magicdraw.uml.symbols.shapes.TextObject))(com.nomagic.magicdraw.uml.symbols.shapes.TextObject obj)`
Creates the HTML document for a given text object with a given style sheet.
`static [View](https://docs.oracle.com/en/java/javase/21/docs/api/java.desktop/javax/swing/text/View.html)`
`[createHTMLView](#createHTMLView(com.nomagic.magicdraw.uml.symbols.shapes.TextObject,java.lang.String,com.nomagic.magicdraw.core.Project))(com.nomagic.magicdraw.uml.symbols.shapes.TextObject object,
 [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) html,
 [Project](../../../../core/Project.html) project)`
Create an HTML renderer for the text object and string of HTML.
`static [View](https://docs.oracle.com/en/java/javase/21/docs/api/java.desktop/javax/swing/text/View.html)`
`[createHTMLView](#createHTMLView(java.lang.String,javax.swing.text.StyledDocument,com.nomagic.magicdraw.core.Project))([String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) html,
 [StyledDocument](https://docs.oracle.com/en/java/javase/21/docs/api/java.desktop/javax/swing/text/StyledDocument.html) doc,
 [Project](../../../../core/Project.html) project)`
Deprecated.
use [`createHTMLView(String, StyledDocument, Project, ShapeElement, boolean)`](#createHTMLView(java.lang.String,javax.swing.text.StyledDocument,com.nomagic.magicdraw.core.Project,com.nomagic.magicdraw.uml.symbols.shapes.ShapeElement,boolean))
`static [View](https://docs.oracle.com/en/java/javase/21/docs/api/java.desktop/javax/swing/text/View.html)`
`[createHTMLView](#createHTMLView(java.lang.String,javax.swing.text.StyledDocument,com.nomagic.magicdraw.core.Project,com.nomagic.magicdraw.uml.symbols.shapes.ShapeElement,boolean))([String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) html,
 [StyledDocument](https://docs.oracle.com/en/java/javase/21/docs/api/java.desktop/javax/swing/text/StyledDocument.html) document,
 [Project](../../../../core/Project.html) project,
 [ShapeElement](../ShapeElement.html) object,
 boolean useAlphaChannelForTransparency)`
Create HTML renderer for the HTML text and document container
`static [View](https://docs.oracle.com/en/java/javase/21/docs/api/java.desktop/javax/swing/text/View.html)`
`[createHTMLView](#createHTMLView(java.lang.String,javax.swing.text.StyledDocument,com.nomagic.magicdraw.core.Project,com.nomagic.magicdraw.uml.symbols.shapes.ShapeElement,boolean,javax.swing.JTextPane))([String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) html,
 [StyledDocument](https://docs.oracle.com/en/java/javase/21/docs/api/java.desktop/javax/swing/text/StyledDocument.html) document,
 [Project](../../../../core/Project.html) project,
 [ShapeElement](../ShapeElement.html) object,
 boolean useAlphaChannelForTransparency,
 [JTextPane](https://docs.oracle.com/en/java/javase/21/docs/api/java.desktop/javax/swing/JTextPane.html) customContainer)`
Create HTML renderer for the HTML text and document container
`static [URL](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/net/URL.html)`
`[getDocumentBase](#getDocumentBase())()`

`static [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html)`
`[getHTMLBody](#getHTMLBody(java.lang.String))([String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) text)`
Deprecated.
use [`HtmlTextUtils.removeHtmlBodyTags(String)`](../../../../../text/html/HtmlTextUtils.html#removeHtmlBodyTags(java.lang.String))
`static [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html)`
`[getPureText](#getPureText(javax.swing.text.Document))([Document](https://docs.oracle.com/en/java/javase/21/docs/api/java.desktop/javax/swing/text/Document.html) doc)`
Deprecated.
use [`HtmlTextUtils.toPlainText(Document)`](../../../../../text/html/HtmlTextUtils.html#toPlainText(javax.swing.text.Document))
`static [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html)`
`[getPureTextFromHTMLSource](#getPureTextFromHTMLSource(java.lang.String))([String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) source)`
Deprecated.
use [`HtmlTextUtils.toPlainText(String)`](../../../../../text/html/HtmlTextUtils.html#toPlainText(java.lang.String))
`static boolean`
`[isHTMLText](#isHTMLText(java.lang.String))([String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) text)`
Deprecated.
use [`HtmlTextUtils.isHtml(String)`](../../../../../text/html/HtmlTextUtils.html#isHtml(java.lang.String))
`static [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html)`
`[makeEndTag](#makeEndTag(java.lang.String))([String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) tag)`
Deprecated.
use [`HtmlTextUtils.endTag(String)`](../../../../../text/html/HtmlTextUtils.html#endTag(java.lang.String))
`static [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html)`
`[makeStartTag](#makeStartTag(java.lang.String))([String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) tag)`
Deprecated.
use [`HtmlTextUtils.startTag(String)`](../../../../../text/html/HtmlTextUtils.html#startTag(java.lang.String))
`static [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html)`
`[removeHTMLHeader](#removeHTMLHeader(java.lang.String))([String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) text)`
Deprecated.
use [`HtmlTextUtils.removeHtmlBodyPTags(String)`](../../../../../text/html/HtmlTextUtils.html#removeHtmlBodyPTags(java.lang.String))
`static [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html)`
`[stringToHTMLString](#stringToHTMLString(java.lang.String))([String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) string)`
Deprecated.
use [`HtmlTextUtils.encodeHtmlCharacters(String)`](../../../../../text/html/HtmlTextUtils.html#encodeHtmlCharacters(java.lang.String))
`static [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html)`
`[wrapAsHTML](#wrapAsHTML(java.lang.String))([String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) text)`
Deprecated.
use [`HtmlTextUtils.wrapInHtmlTag(String)`](../../../../../text/html/HtmlTextUtils.html#wrapInHtmlTag(java.lang.String))
`static [StringBuilder](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/StringBuilder.html)`
`[wrapAsHTML](#wrapAsHTML(java.lang.StringBuilder))([StringBuilder](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/StringBuilder.html) text)`
Deprecated.
use [`HtmlTextUtils.wrapInHtmlTag(StringBuilder)`](../../../../../text/html/HtmlTextUtils.html#wrapInHtmlTag(java.lang.StringBuilder))
`static [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html)`
`[wrapAsHTMLDocument](#wrapAsHTMLDocument(java.lang.String))([String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) text)`
Deprecated.
use [`HtmlTextUtils.wrapInHtmlBodyPTags(String)`](../../../../../text/html/HtmlTextUtils.html#wrapInHtmlBodyPTags(java.lang.String))
`static [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html)`
`[wrapByHtmlBody](#wrapByHtmlBody(java.lang.String))([String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) text)`
Deprecated.
use [`HtmlTextUtils.wrapInHtmlBodyNewLineTags(String)`](../../../../../text/html/HtmlTextUtils.html#wrapInHtmlBodyNewLineTags(java.lang.String))
Methods inherited from class java.lang.[Object](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html)
`[clone](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#clone()), [equals](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#equals(java.lang.Object)), [finalize](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#finalize()), [getClass](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#getClass()), [hashCode](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#hashCode()), [notify](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#notify()), [notifyAll](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#notifyAll()), [toString](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#toString()), [wait](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#wait()), [wait](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#wait(long)), [wait](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#wait(long,int))`

============ FIELD DETAIL =========== 
Field Details
MD_ICON_TAG
public static final [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) MD_ICON_TAG
See Also:
[Constant Field Values](../../../../../../../constant-values.html#com.nomagic.magicdraw.uml.symbols.shapes.html.HTMLHelper.MD_ICON_TAG)
 ========= CONSTRUCTOR DETAIL ======== 
Constructor Details
HTMLHelper
public HTMLHelper()
 ============ METHOD DETAIL ========== 
Method Details
getDocumentBase
public static [URL](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/net/URL.html) getDocumentBase()
createHTMLView
public static [View](https://docs.oracle.com/en/java/javase/21/docs/api/java.desktop/javax/swing/text/View.html) createHTMLView(com.nomagic.magicdraw.uml.symbols.shapes.TextObject object,
 [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) html,
 @CheckForNull
 [Project](../../../../core/Project.html) project)
Create an HTML renderer for the text object and string of HTML.
Parameters:
`object` - the given text object
`html` - the given HTML text
createHTMLView
[@Deprecated](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Deprecated.html)public static [View](https://docs.oracle.com/en/java/javase/21/docs/api/java.desktop/javax/swing/text/View.html) createHTMLView([String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) html,
 [StyledDocument](https://docs.oracle.com/en/java/javase/21/docs/api/java.desktop/javax/swing/text/StyledDocument.html) doc,
 @CheckForNull
 [Project](../../../../core/Project.html) project)
Deprecated.
use [`createHTMLView(String, StyledDocument, Project, ShapeElement, boolean)`](#createHTMLView(java.lang.String,javax.swing.text.StyledDocument,com.nomagic.magicdraw.core.Project,com.nomagic.magicdraw.uml.symbols.shapes.ShapeElement,boolean))
createHTMLView
public static [View](https://docs.oracle.com/en/java/javase/21/docs/api/java.desktop/javax/swing/text/View.html) createHTMLView([String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) html,
 [StyledDocument](https://docs.oracle.com/en/java/javase/21/docs/api/java.desktop/javax/swing/text/StyledDocument.html) document,
 @CheckForNull
 [Project](../../../../core/Project.html) project,
 @CheckForNull
 [ShapeElement](../ShapeElement.html) object,
 boolean useAlphaChannelForTransparency)
Create HTML renderer for the HTML text and document container
Parameters:
`html` - the given HTML text
`document` - document
`object` - the given text object
createHTMLView
public static [View](https://docs.oracle.com/en/java/javase/21/docs/api/java.desktop/javax/swing/text/View.html) createHTMLView([String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) html,
 [StyledDocument](https://docs.oracle.com/en/java/javase/21/docs/api/java.desktop/javax/swing/text/StyledDocument.html) document,
 @CheckForNull
 [Project](../../../../core/Project.html) project,
 @CheckForNull
 [ShapeElement](../ShapeElement.html) object,
 boolean useAlphaChannelForTransparency,
 @CheckForNull
 [JTextPane](https://docs.oracle.com/en/java/javase/21/docs/api/java.desktop/javax/swing/JTextPane.html) customContainer)
Create HTML renderer for the HTML text and document container
Parameters:
`html` - the given HTML text
`document` - document
`object` - the given text object
`customContainer` - custom renderer component. Used to override font metrics
createDefaultDocument
public static [HTMLDocument](https://docs.oracle.com/en/java/javase/21/docs/api/java.desktop/javax/swing/text/html/HTMLDocument.html) createDefaultDocument(com.nomagic.magicdraw.uml.symbols.shapes.TextObject obj)
Creates the HTML document for a given text object with a given style sheet.
Parameters:
`obj` - the text object
applyStyleSheet
public static void applyStyleSheet([StyleSheet](https://docs.oracle.com/en/java/javase/21/docs/api/java.desktop/javax/swing/text/html/StyleSheet.html) styles,
 com.nomagic.magicdraw.uml.symbols.shapes.TextObject obj,
 boolean takeZoomFactor)
Changes the properties of the given style sheet according to the properties of the given text object.
Parameters:
`styles` - the given style sheet
`obj` - the given text object
applyFontSizeStyleSheetOnP
[@Deprecated](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Deprecated.html)public static [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) applyFontSizeStyleSheetOnP([String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) html,
 [Font](https://docs.oracle.com/en/java/javase/21/docs/api/java.desktop/java/awt/Font.html) font,
 boolean ptUnits)
Deprecated.
use `HtmlStyleUtils.applyFontSizeStyleSheetOnP(String, Font, boolean)`
applyFontSizeStyleSheetColorOnP
[@Deprecated](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Deprecated.html)public static [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) applyFontSizeStyleSheetColorOnP([String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) html,
 [Font](https://docs.oracle.com/en/java/javase/21/docs/api/java.desktop/java/awt/Font.html) font,
 boolean ptUnits,
 int red,
 int green,
 int blue)
Deprecated.
use `HtmlStyleUtils.applyFontSizeStyleSheetColorOnP(String, Font, boolean, int, int, int)`
wrapAsHTML
[@Deprecated](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Deprecated.html)public static [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) wrapAsHTML([String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) text)
Deprecated.
use [`HtmlTextUtils.wrapInHtmlTag(String)`](../../../../../text/html/HtmlTextUtils.html#wrapInHtmlTag(java.lang.String))
wrapAsHTML
[@Deprecated](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Deprecated.html)public static [StringBuilder](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/StringBuilder.html) wrapAsHTML([StringBuilder](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/StringBuilder.html) text)
Deprecated.
use [`HtmlTextUtils.wrapInHtmlTag(StringBuilder)`](../../../../../text/html/HtmlTextUtils.html#wrapInHtmlTag(java.lang.StringBuilder))
wrapAsHTMLDocument
[@Deprecated](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Deprecated.html)public static [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) wrapAsHTMLDocument([String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) text)
Deprecated.
use [`HtmlTextUtils.wrapInHtmlBodyPTags(String)`](../../../../../text/html/HtmlTextUtils.html#wrapInHtmlBodyPTags(java.lang.String))
wrapByHtmlBody
[@Deprecated](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Deprecated.html)public static [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) wrapByHtmlBody([String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) text)
Deprecated.
use [`HtmlTextUtils.wrapInHtmlBodyNewLineTags(String)`](../../../../../text/html/HtmlTextUtils.html#wrapInHtmlBodyNewLineTags(java.lang.String))
stringToHTMLString
[@Deprecated](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Deprecated.html)public static [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) stringToHTMLString([String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) string)
Deprecated.
use [`HtmlTextUtils.encodeHtmlCharacters(String)`](../../../../../text/html/HtmlTextUtils.html#encodeHtmlCharacters(java.lang.String))
getPureText
[@Deprecated](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Deprecated.html)public static [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) getPureText([Document](https://docs.oracle.com/en/java/javase/21/docs/api/java.desktop/javax/swing/text/Document.html) doc)
Deprecated.
use [`HtmlTextUtils.toPlainText(Document)`](../../../../../text/html/HtmlTextUtils.html#toPlainText(javax.swing.text.Document))
getPureTextFromHTMLSource
[@Deprecated](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Deprecated.html)public static [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) getPureTextFromHTMLSource([String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) source)
Deprecated.
use [`HtmlTextUtils.toPlainText(String)`](../../../../../text/html/HtmlTextUtils.html#toPlainText(java.lang.String))
isHTMLText
[@Deprecated](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Deprecated.html)public static boolean isHTMLText(@CheckForNull
 [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) text)
Deprecated.
use [`HtmlTextUtils.isHtml(String)`](../../../../../text/html/HtmlTextUtils.html#isHtml(java.lang.String))
removeHTMLHeader
[@Deprecated](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Deprecated.html)public static [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) removeHTMLHeader([String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) text)
Deprecated.
use [`HtmlTextUtils.removeHtmlBodyPTags(String)`](../../../../../text/html/HtmlTextUtils.html#removeHtmlBodyPTags(java.lang.String))
getHTMLBody
[@Deprecated](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Deprecated.html)public static [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) getHTMLBody([String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) text)
Deprecated.
use [`HtmlTextUtils.removeHtmlBodyTags(String)`](../../../../../text/html/HtmlTextUtils.html#removeHtmlBodyTags(java.lang.String))
constructHTMLText
[@Deprecated](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Deprecated.html)public static [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) constructHTMLText([String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) text)
Deprecated.
use [`HtmlTextUtils.toHtmlText(String)`](../../../../../text/html/HtmlTextUtils.html#toHtmlText(java.lang.String))
constructHTMLText
[@Deprecated](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Deprecated.html)public static [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) constructHTMLText([String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) text,
 boolean convertCharacters,
 boolean addEnterAfterP)
Deprecated.
use `HtmlTextUtilsInternal.toHtmlText(String, boolean, boolean)`
makeStartTag
[@Deprecated](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Deprecated.html)public static [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) makeStartTag([String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) tag)
Deprecated.
use [`HtmlTextUtils.startTag(String)`](../../../../../text/html/HtmlTextUtils.html#startTag(java.lang.String))
makeEndTag
[@Deprecated](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Deprecated.html)public static [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) makeEndTag([String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) tag)
Deprecated.
use [`HtmlTextUtils.endTag(String)`](../../../../../text/html/HtmlTextUtils.html#endTag(java.lang.String))

========= END OF CLASS DATA =========

## EXACT JAVADOC MAIN HTML

````html
<main role="main">
<!-- ======== START OF CLASS DATA ======== -->
<div class="header">
<div class="sub-title"><span class="package-label-in-type">Package</span> <a href="package-summary.html">com.nomagic.magicdraw.uml.symbols.shapes.html</a></div>
<h1 class="title" title="Class HTMLHelper">Class HTMLHelper</h1>
</div>
<div class="inheritance" title="Inheritance Tree"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">java.lang.Object</a>
<div class="inheritance">com.nomagic.magicdraw.uml.symbols.shapes.html.HTMLHelper</div>
</div>
<section class="class-description" id="class-description">
<hr/>
<div class="type-signature"><span class="annotations">@OpenApiAll
</span><span class="modifiers">public class </span><span class="element-name type-name-label">HTMLHelper</span>
<span class="extends-implements">extends <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a></span></div>
<div class="block">The class is used for HTML document creation.</div>
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
<div class="col-second even-row-color"><code><a class="member-name-link" href="#MD_ICON_TAG">MD_ICON_TAG</a></code></div>
<div class="col-last even-row-color"> </div>
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
<div class="col-constructor-name even-row-color"><code><a class="member-name-link" href="#%3Cinit%3E()">HTMLHelper</a>()</code></div>
<div class="col-last even-row-color"> </div>
</div>
</section>
</li>
<!-- ========== METHOD SUMMARY =========== -->
<li>
<section class="method-summary" id="method-summary">
<h2>Method Summary</h2>
<div id="method-summary-table">
<div aria-orientation="horizontal" class="table-tabs" role="tablist"><button aria-controls="method-summary-table.tabpanel" aria-selected="true" class="active-table-tab" id="method-summary-table-tab0" onclick="show('method-summary-table', 'method-summary-table', 3)" onkeydown="switchTab(event)" role="tab" tabindex="0">All Methods</button><button aria-controls="method-summary-table.tabpanel" aria-selected="false" class="table-tab" id="method-summary-table-tab1" onclick="show('method-summary-table', 'method-summary-table-tab1', 3)" onkeydown="switchTab(event)" role="tab" tabindex="-1">Static Methods</button><button aria-controls="method-summary-table.tabpanel" aria-selected="false" class="table-tab" id="method-summary-table-tab4" onclick="show('method-summary-table', 'method-summary-table-tab4', 3)" onkeydown="switchTab(event)" role="tab" tabindex="-1">Concrete Methods</button><button aria-controls="method-summary-table.tabpanel" aria-selected="false" class="table-tab" id="method-summary-table-tab6" onclick="show('method-summary-table', 'method-summary-table-tab6', 3)" onkeydown="switchTab(event)" role="tab" tabindex="-1">Deprecated Methods</button></div>
<div aria-labelledby="method-summary-table-tab0" id="method-summary-table.tabpanel" role="tabpanel">
<div class="summary-table three-column-summary">
<div class="table-header col-first">Modifier and Type</div>
<div class="table-header col-second">Method</div>
<div class="table-header col-last">Description</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4 method-summary-table-tab6"><code>static <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4 method-summary-table-tab6"><code><a class="member-name-link" href="#applyFontSizeStyleSheetColorOnP(java.lang.String,java.awt.Font,boolean,int,int,int)">applyFontSizeStyleSheetColorOnP</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> html,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.desktop/java/awt/Font.html" title="class or interface in java.awt">Font</a> font,
 boolean ptUnits,
 int red,
 int green,
 int blue)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4 method-summary-table-tab6">
<div class="block"><span class="deprecated-label">Deprecated.</span>
<div class="deprecation-comment">use <code>HtmlStyleUtils.applyFontSizeStyleSheetColorOnP(String, Font, boolean, int, int, int)</code></div>
</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4 method-summary-table-tab6"><code>static <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4 method-summary-table-tab6"><code><a class="member-name-link" href="#applyFontSizeStyleSheetOnP(java.lang.String,java.awt.Font,boolean)">applyFontSizeStyleSheetOnP</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> html,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.desktop/java/awt/Font.html" title="class or interface in java.awt">Font</a> font,
 boolean ptUnits)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4 method-summary-table-tab6">
<div class="block"><span class="deprecated-label">Deprecated.</span>
<div class="deprecation-comment">use <code>HtmlStyleUtils.applyFontSizeStyleSheetOnP(String, Font, boolean)</code></div>
</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#applyStyleSheet(javax.swing.text.html.StyleSheet,com.nomagic.magicdraw.uml.symbols.shapes.TextObject,boolean)">applyStyleSheet</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.desktop/javax/swing/text/html/StyleSheet.html" title="class or interface in javax.swing.text.html">StyleSheet</a> styles,
 com.nomagic.magicdraw.uml.symbols.shapes.TextObject obj,
 boolean takeZoomFactor)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Changes the properties of the given style sheet according to the properties of the given text object.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4 method-summary-table-tab6"><code>static <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4 method-summary-table-tab6"><code><a class="member-name-link" href="#constructHTMLText(java.lang.String)">constructHTMLText</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> text)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4 method-summary-table-tab6">
<div class="block"><span class="deprecated-label">Deprecated.</span>
<div class="deprecation-comment">use <a href="../../../../../text/html/HtmlTextUtils.html#toHtmlText(java.lang.String)"><code>HtmlTextUtils.toHtmlText(String)</code></a></div>
</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4 method-summary-table-tab6"><code>static <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4 method-summary-table-tab6"><code><a class="member-name-link" href="#constructHTMLText(java.lang.String,boolean,boolean)">constructHTMLText</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> text,
 boolean convertCharacters,
 boolean addEnterAfterP)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4 method-summary-table-tab6">
<div class="block"><span class="deprecated-label">Deprecated.</span>
<div class="deprecation-comment">use <code>HtmlTextUtilsInternal.toHtmlText(String, boolean, boolean)</code></div>
</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.desktop/javax/swing/text/html/HTMLDocument.html" title="class or interface in javax.swing.text.html">HTMLDocument</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#createDefaultDocument(com.nomagic.magicdraw.uml.symbols.shapes.TextObject)">createDefaultDocument</a><wbr/>(com.nomagic.magicdraw.uml.symbols.shapes.TextObject obj)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Creates the HTML document for a given text object with a given style sheet.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.desktop/javax/swing/text/View.html" title="class or interface in javax.swing.text">View</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#createHTMLView(com.nomagic.magicdraw.uml.symbols.shapes.TextObject,java.lang.String,com.nomagic.magicdraw.core.Project)">createHTMLView</a><wbr/>(com.nomagic.magicdraw.uml.symbols.shapes.TextObject object,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> html,
 <a href="../../../../core/Project.html" title="class in com.nomagic.magicdraw.core">Project</a> project)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Create an HTML renderer for the text object and string of HTML.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4 method-summary-table-tab6"><code>static <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.desktop/javax/swing/text/View.html" title="class or interface in javax.swing.text">View</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4 method-summary-table-tab6"><code><a class="member-name-link" href="#createHTMLView(java.lang.String,javax.swing.text.StyledDocument,com.nomagic.magicdraw.core.Project)">createHTMLView</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> html,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.desktop/javax/swing/text/StyledDocument.html" title="class or interface in javax.swing.text">StyledDocument</a> doc,
 <a href="../../../../core/Project.html" title="class in com.nomagic.magicdraw.core">Project</a> project)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4 method-summary-table-tab6">
<div class="block"><span class="deprecated-label">Deprecated.</span>
<div class="deprecation-comment">use <a href="#createHTMLView(java.lang.String,javax.swing.text.StyledDocument,com.nomagic.magicdraw.core.Project,com.nomagic.magicdraw.uml.symbols.shapes.ShapeElement,boolean)"><code>createHTMLView(String, StyledDocument, Project, ShapeElement, boolean)</code></a></div>
</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.desktop/javax/swing/text/View.html" title="class or interface in javax.swing.text">View</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#createHTMLView(java.lang.String,javax.swing.text.StyledDocument,com.nomagic.magicdraw.core.Project,com.nomagic.magicdraw.uml.symbols.shapes.ShapeElement,boolean)">createHTMLView</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> html,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.desktop/javax/swing/text/StyledDocument.html" title="class or interface in javax.swing.text">StyledDocument</a> document,
 <a href="../../../../core/Project.html" title="class in com.nomagic.magicdraw.core">Project</a> project,
 <a href="../ShapeElement.html" title="class in com.nomagic.magicdraw.uml.symbols.shapes">ShapeElement</a> object,
 boolean useAlphaChannelForTransparency)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Create HTML renderer for the HTML text and document container</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.desktop/javax/swing/text/View.html" title="class or interface in javax.swing.text">View</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#createHTMLView(java.lang.String,javax.swing.text.StyledDocument,com.nomagic.magicdraw.core.Project,com.nomagic.magicdraw.uml.symbols.shapes.ShapeElement,boolean,javax.swing.JTextPane)">createHTMLView</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> html,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.desktop/javax/swing/text/StyledDocument.html" title="class or interface in javax.swing.text">StyledDocument</a> document,
 <a href="../../../../core/Project.html" title="class in com.nomagic.magicdraw.core">Project</a> project,
 <a href="../ShapeElement.html" title="class in com.nomagic.magicdraw.uml.symbols.shapes">ShapeElement</a> object,
 boolean useAlphaChannelForTransparency,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.desktop/javax/swing/JTextPane.html" title="class or interface in javax.swing">JTextPane</a> customContainer)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Create HTML renderer for the HTML text and document container</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/net/URL.html" title="class or interface in java.net">URL</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#getDocumentBase()">getDocumentBase</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4 method-summary-table-tab6"><code>static <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4 method-summary-table-tab6"><code><a class="member-name-link" href="#getHTMLBody(java.lang.String)">getHTMLBody</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> text)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4 method-summary-table-tab6">
<div class="block"><span class="deprecated-label">Deprecated.</span>
<div class="deprecation-comment">use <a href="../../../../../text/html/HtmlTextUtils.html#removeHtmlBodyTags(java.lang.String)"><code>HtmlTextUtils.removeHtmlBodyTags(String)</code></a></div>
</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4 method-summary-table-tab6"><code>static <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4 method-summary-table-tab6"><code><a class="member-name-link" href="#getPureText(javax.swing.text.Document)">getPureText</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.desktop/javax/swing/text/Document.html" title="class or interface in javax.swing.text">Document</a> doc)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4 method-summary-table-tab6">
<div class="block"><span class="deprecated-label">Deprecated.</span>
<div class="deprecation-comment">use <a href="../../../../../text/html/HtmlTextUtils.html#toPlainText(javax.swing.text.Document)"><code>HtmlTextUtils.toPlainText(Document)</code></a></div>
</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4 method-summary-table-tab6"><code>static <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4 method-summary-table-tab6"><code><a class="member-name-link" href="#getPureTextFromHTMLSource(java.lang.String)">getPureTextFromHTMLSource</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> source)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4 method-summary-table-tab6">
<div class="block"><span class="deprecated-label">Deprecated.</span>
<div class="deprecation-comment">use <a href="../../../../../text/html/HtmlTextUtils.html#toPlainText(java.lang.String)"><code>HtmlTextUtils.toPlainText(String)</code></a></div>
</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4 method-summary-table-tab6"><code>static boolean</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4 method-summary-table-tab6"><code><a class="member-name-link" href="#isHTMLText(java.lang.String)">isHTMLText</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> text)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4 method-summary-table-tab6">
<div class="block"><span class="deprecated-label">Deprecated.</span>
<div class="deprecation-comment">use <a href="../../../../../text/html/HtmlTextUtils.html#isHtml(java.lang.String)"><code>HtmlTextUtils.isHtml(String)</code></a></div>
</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4 method-summary-table-tab6"><code>static <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4 method-summary-table-tab6"><code><a class="member-name-link" href="#makeEndTag(java.lang.String)">makeEndTag</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> tag)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4 method-summary-table-tab6">
<div class="block"><span class="deprecated-label">Deprecated.</span>
<div class="deprecation-comment">use <a href="../../../../../text/html/HtmlTextUtils.html#endTag(java.lang.String)"><code>HtmlTextUtils.endTag(String)</code></a></div>
</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4 method-summary-table-tab6"><code>static <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4 method-summary-table-tab6"><code><a class="member-name-link" href="#makeStartTag(java.lang.String)">makeStartTag</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> tag)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4 method-summary-table-tab6">
<div class="block"><span class="deprecated-label">Deprecated.</span>
<div class="deprecation-comment">use <a href="../../../../../text/html/HtmlTextUtils.html#startTag(java.lang.String)"><code>HtmlTextUtils.startTag(String)</code></a></div>
</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4 method-summary-table-tab6"><code>static <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4 method-summary-table-tab6"><code><a class="member-name-link" href="#removeHTMLHeader(java.lang.String)">removeHTMLHeader</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> text)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4 method-summary-table-tab6">
<div class="block"><span class="deprecated-label">Deprecated.</span>
<div class="deprecation-comment">use <a href="../../../../../text/html/HtmlTextUtils.html#removeHtmlBodyPTags(java.lang.String)"><code>HtmlTextUtils.removeHtmlBodyPTags(String)</code></a></div>
</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4 method-summary-table-tab6"><code>static <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4 method-summary-table-tab6"><code><a class="member-name-link" href="#stringToHTMLString(java.lang.String)">stringToHTMLString</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> string)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4 method-summary-table-tab6">
<div class="block"><span class="deprecated-label">Deprecated.</span>
<div class="deprecation-comment">use <a href="../../../../../text/html/HtmlTextUtils.html#encodeHtmlCharacters(java.lang.String)"><code>HtmlTextUtils.encodeHtmlCharacters(String)</code></a></div>
</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4 method-summary-table-tab6"><code>static <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4 method-summary-table-tab6"><code><a class="member-name-link" href="#wrapAsHTML(java.lang.String)">wrapAsHTML</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> text)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4 method-summary-table-tab6">
<div class="block"><span class="deprecated-label">Deprecated.</span>
<div class="deprecation-comment">use <a href="../../../../../text/html/HtmlTextUtils.html#wrapInHtmlTag(java.lang.String)"><code>HtmlTextUtils.wrapInHtmlTag(String)</code></a></div>
</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4 method-summary-table-tab6"><code>static <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/StringBuilder.html" title="class or interface in java.lang">StringBuilder</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4 method-summary-table-tab6"><code><a class="member-name-link" href="#wrapAsHTML(java.lang.StringBuilder)">wrapAsHTML</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/StringBuilder.html" title="class or interface in java.lang">StringBuilder</a> text)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4 method-summary-table-tab6">
<div class="block"><span class="deprecated-label">Deprecated.</span>
<div class="deprecation-comment">use <a href="../../../../../text/html/HtmlTextUtils.html#wrapInHtmlTag(java.lang.StringBuilder)"><code>HtmlTextUtils.wrapInHtmlTag(StringBuilder)</code></a></div>
</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4 method-summary-table-tab6"><code>static <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4 method-summary-table-tab6"><code><a class="member-name-link" href="#wrapAsHTMLDocument(java.lang.String)">wrapAsHTMLDocument</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> text)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4 method-summary-table-tab6">
<div class="block"><span class="deprecated-label">Deprecated.</span>
<div class="deprecation-comment">use <a href="../../../../../text/html/HtmlTextUtils.html#wrapInHtmlBodyPTags(java.lang.String)"><code>HtmlTextUtils.wrapInHtmlBodyPTags(String)</code></a></div>
</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4 method-summary-table-tab6"><code>static <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4 method-summary-table-tab6"><code><a class="member-name-link" href="#wrapByHtmlBody(java.lang.String)">wrapByHtmlBody</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> text)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4 method-summary-table-tab6">
<div class="block"><span class="deprecated-label">Deprecated.</span>
<div class="deprecation-comment">use <a href="../../../../../text/html/HtmlTextUtils.html#wrapInHtmlBodyNewLineTags(java.lang.String)"><code>HtmlTextUtils.wrapInHtmlBodyNewLineTags(String)</code></a></div>
</div>
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
<section class="detail" id="MD_ICON_TAG">
<h3>MD_ICON_TAG</h3>
<div class="member-signature"><span class="modifiers">public static final</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">MD_ICON_TAG</span></div>
<dl class="notes">
<dt>See Also:</dt>
<dd>
<ul class="tag-list">
<li><a href="../../../../../../../constant-values.html#com.nomagic.magicdraw.uml.symbols.shapes.html.HTMLHelper.MD_ICON_TAG">Constant Field Values</a></li>
</ul>
</dd>
</dl>
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
<h3>HTMLHelper</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="element-name">HTMLHelper</span>()</div>
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
<section class="detail" id="getDocumentBase()">
<h3>getDocumentBase</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/net/URL.html" title="class or interface in java.net">URL</a></span> <span class="element-name">getDocumentBase</span>()</div>
</section>
</li>
<li>
<section class="detail" id="createHTMLView(com.nomagic.magicdraw.uml.symbols.shapes.TextObject,java.lang.String,com.nomagic.magicdraw.core.Project)">
<h3>createHTMLView</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.desktop/javax/swing/text/View.html" title="class or interface in javax.swing.text">View</a></span> <span class="element-name">createHTMLView</span><wbr/><span class="parameters">(com.nomagic.magicdraw.uml.symbols.shapes.TextObject object,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> html,
 @CheckForNull
 <a href="../../../../core/Project.html" title="class in com.nomagic.magicdraw.core">Project</a> project)</span></div>
<div class="block">Create an HTML renderer for the text object and string of HTML.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>object</code> - the given text object</dd>
<dd><code>html</code> - the given HTML text</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="createHTMLView(java.lang.String,javax.swing.text.StyledDocument,com.nomagic.magicdraw.core.Project)">
<h3>createHTMLView</h3>
<div class="member-signature"><span class="annotations"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Deprecated.html" title="class or interface in java.lang">@Deprecated</a>
</span><span class="modifiers">public static</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.desktop/javax/swing/text/View.html" title="class or interface in javax.swing.text">View</a></span> <span class="element-name">createHTMLView</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> html,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.desktop/javax/swing/text/StyledDocument.html" title="class or interface in javax.swing.text">StyledDocument</a> doc,
 @CheckForNull
 <a href="../../../../core/Project.html" title="class in com.nomagic.magicdraw.core">Project</a> project)</span></div>
<div class="deprecation-block"><span class="deprecated-label">Deprecated.</span>
<div class="deprecation-comment">use <a href="#createHTMLView(java.lang.String,javax.swing.text.StyledDocument,com.nomagic.magicdraw.core.Project,com.nomagic.magicdraw.uml.symbols.shapes.ShapeElement,boolean)"><code>createHTMLView(String, StyledDocument, Project, ShapeElement, boolean)</code></a></div>
</div>
</section>
</li>
<li>
<section class="detail" id="createHTMLView(java.lang.String,javax.swing.text.StyledDocument,com.nomagic.magicdraw.core.Project,com.nomagic.magicdraw.uml.symbols.shapes.ShapeElement,boolean)">
<h3>createHTMLView</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.desktop/javax/swing/text/View.html" title="class or interface in javax.swing.text">View</a></span> <span class="element-name">createHTMLView</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> html,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.desktop/javax/swing/text/StyledDocument.html" title="class or interface in javax.swing.text">StyledDocument</a> document,
 @CheckForNull
 <a href="../../../../core/Project.html" title="class in com.nomagic.magicdraw.core">Project</a> project,
 @CheckForNull
 <a href="../ShapeElement.html" title="class in com.nomagic.magicdraw.uml.symbols.shapes">ShapeElement</a> object,
 boolean useAlphaChannelForTransparency)</span></div>
<div class="block">Create HTML renderer for the HTML text and document container</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>html</code> - the given HTML text</dd>
<dd><code>document</code> - document</dd>
<dd><code>object</code> - the given text object</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="createHTMLView(java.lang.String,javax.swing.text.StyledDocument,com.nomagic.magicdraw.core.Project,com.nomagic.magicdraw.uml.symbols.shapes.ShapeElement,boolean,javax.swing.JTextPane)">
<h3>createHTMLView</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.desktop/javax/swing/text/View.html" title="class or interface in javax.swing.text">View</a></span> <span class="element-name">createHTMLView</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> html,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.desktop/javax/swing/text/StyledDocument.html" title="class or interface in javax.swing.text">StyledDocument</a> document,
 @CheckForNull
 <a href="../../../../core/Project.html" title="class in com.nomagic.magicdraw.core">Project</a> project,
 @CheckForNull
 <a href="../ShapeElement.html" title="class in com.nomagic.magicdraw.uml.symbols.shapes">ShapeElement</a> object,
 boolean useAlphaChannelForTransparency,
 @CheckForNull
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.desktop/javax/swing/JTextPane.html" title="class or interface in javax.swing">JTextPane</a> customContainer)</span></div>
<div class="block">Create HTML renderer for the HTML text and document container</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>html</code> - the given HTML text</dd>
<dd><code>document</code> - document</dd>
<dd><code>object</code> - the given text object</dd>
<dd><code>customContainer</code> - custom renderer component. Used to override font metrics</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="createDefaultDocument(com.nomagic.magicdraw.uml.symbols.shapes.TextObject)">
<h3>createDefaultDocument</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.desktop/javax/swing/text/html/HTMLDocument.html" title="class or interface in javax.swing.text.html">HTMLDocument</a></span> <span class="element-name">createDefaultDocument</span><wbr/><span class="parameters">(com.nomagic.magicdraw.uml.symbols.shapes.TextObject obj)</span></div>
<div class="block">Creates the HTML document for a given text object with a given style sheet.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>obj</code> - the text object</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="applyStyleSheet(javax.swing.text.html.StyleSheet,com.nomagic.magicdraw.uml.symbols.shapes.TextObject,boolean)">
<h3>applyStyleSheet</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type">void</span> <span class="element-name">applyStyleSheet</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.desktop/javax/swing/text/html/StyleSheet.html" title="class or interface in javax.swing.text.html">StyleSheet</a> styles,
 com.nomagic.magicdraw.uml.symbols.shapes.TextObject obj,
 boolean takeZoomFactor)</span></div>
<div class="block">Changes the properties of the given style sheet according to the properties of the given text object.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>styles</code> - the given style sheet</dd>
<dd><code>obj</code> - the given text object</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="applyFontSizeStyleSheetOnP(java.lang.String,java.awt.Font,boolean)">
<h3>applyFontSizeStyleSheetOnP</h3>
<div class="member-signature"><span class="annotations"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Deprecated.html" title="class or interface in java.lang">@Deprecated</a>
</span><span class="modifiers">public static</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">applyFontSizeStyleSheetOnP</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> html,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.desktop/java/awt/Font.html" title="class or interface in java.awt">Font</a> font,
 boolean ptUnits)</span></div>
<div class="deprecation-block"><span class="deprecated-label">Deprecated.</span>
<div class="deprecation-comment">use <code>HtmlStyleUtils.applyFontSizeStyleSheetOnP(String, Font, boolean)</code></div>
</div>
</section>
</li>
<li>
<section class="detail" id="applyFontSizeStyleSheetColorOnP(java.lang.String,java.awt.Font,boolean,int,int,int)">
<h3>applyFontSizeStyleSheetColorOnP</h3>
<div class="member-signature"><span class="annotations"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Deprecated.html" title="class or interface in java.lang">@Deprecated</a>
</span><span class="modifiers">public static</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">applyFontSizeStyleSheetColorOnP</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> html,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.desktop/java/awt/Font.html" title="class or interface in java.awt">Font</a> font,
 boolean ptUnits,
 int red,
 int green,
 int blue)</span></div>
<div class="deprecation-block"><span class="deprecated-label">Deprecated.</span>
<div class="deprecation-comment">use <code>HtmlStyleUtils.applyFontSizeStyleSheetColorOnP(String, Font, boolean, int, int, int)</code></div>
</div>
</section>
</li>
<li>
<section class="detail" id="wrapAsHTML(java.lang.String)">
<h3>wrapAsHTML</h3>
<div class="member-signature"><span class="annotations"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Deprecated.html" title="class or interface in java.lang">@Deprecated</a>
</span><span class="modifiers">public static</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">wrapAsHTML</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> text)</span></div>
<div class="deprecation-block"><span class="deprecated-label">Deprecated.</span>
<div class="deprecation-comment">use <a href="../../../../../text/html/HtmlTextUtils.html#wrapInHtmlTag(java.lang.String)"><code>HtmlTextUtils.wrapInHtmlTag(String)</code></a></div>
</div>
</section>
</li>
<li>
<section class="detail" id="wrapAsHTML(java.lang.StringBuilder)">
<h3>wrapAsHTML</h3>
<div class="member-signature"><span class="annotations"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Deprecated.html" title="class or interface in java.lang">@Deprecated</a>
</span><span class="modifiers">public static</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/StringBuilder.html" title="class or interface in java.lang">StringBuilder</a></span> <span class="element-name">wrapAsHTML</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/StringBuilder.html" title="class or interface in java.lang">StringBuilder</a> text)</span></div>
<div class="deprecation-block"><span class="deprecated-label">Deprecated.</span>
<div class="deprecation-comment">use <a href="../../../../../text/html/HtmlTextUtils.html#wrapInHtmlTag(java.lang.StringBuilder)"><code>HtmlTextUtils.wrapInHtmlTag(StringBuilder)</code></a></div>
</div>
</section>
</li>
<li>
<section class="detail" id="wrapAsHTMLDocument(java.lang.String)">
<h3>wrapAsHTMLDocument</h3>
<div class="member-signature"><span class="annotations"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Deprecated.html" title="class or interface in java.lang">@Deprecated</a>
</span><span class="modifiers">public static</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">wrapAsHTMLDocument</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> text)</span></div>
<div class="deprecation-block"><span class="deprecated-label">Deprecated.</span>
<div class="deprecation-comment">use <a href="../../../../../text/html/HtmlTextUtils.html#wrapInHtmlBodyPTags(java.lang.String)"><code>HtmlTextUtils.wrapInHtmlBodyPTags(String)</code></a></div>
</div>
</section>
</li>
<li>
<section class="detail" id="wrapByHtmlBody(java.lang.String)">
<h3>wrapByHtmlBody</h3>
<div class="member-signature"><span class="annotations"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Deprecated.html" title="class or interface in java.lang">@Deprecated</a>
</span><span class="modifiers">public static</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">wrapByHtmlBody</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> text)</span></div>
<div class="deprecation-block"><span class="deprecated-label">Deprecated.</span>
<div class="deprecation-comment">use <a href="../../../../../text/html/HtmlTextUtils.html#wrapInHtmlBodyNewLineTags(java.lang.String)"><code>HtmlTextUtils.wrapInHtmlBodyNewLineTags(String)</code></a></div>
</div>
</section>
</li>
<li>
<section class="detail" id="stringToHTMLString(java.lang.String)">
<h3>stringToHTMLString</h3>
<div class="member-signature"><span class="annotations"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Deprecated.html" title="class or interface in java.lang">@Deprecated</a>
</span><span class="modifiers">public static</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">stringToHTMLString</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> string)</span></div>
<div class="deprecation-block"><span class="deprecated-label">Deprecated.</span>
<div class="deprecation-comment">use <a href="../../../../../text/html/HtmlTextUtils.html#encodeHtmlCharacters(java.lang.String)"><code>HtmlTextUtils.encodeHtmlCharacters(String)</code></a></div>
</div>
</section>
</li>
<li>
<section class="detail" id="getPureText(javax.swing.text.Document)">
<h3>getPureText</h3>
<div class="member-signature"><span class="annotations"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Deprecated.html" title="class or interface in java.lang">@Deprecated</a>
</span><span class="modifiers">public static</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">getPureText</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.desktop/javax/swing/text/Document.html" title="class or interface in javax.swing.text">Document</a> doc)</span></div>
<div class="deprecation-block"><span class="deprecated-label">Deprecated.</span>
<div class="deprecation-comment">use <a href="../../../../../text/html/HtmlTextUtils.html#toPlainText(javax.swing.text.Document)"><code>HtmlTextUtils.toPlainText(Document)</code></a></div>
</div>
</section>
</li>
<li>
<section class="detail" id="getPureTextFromHTMLSource(java.lang.String)">
<h3>getPureTextFromHTMLSource</h3>
<div class="member-signature"><span class="annotations"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Deprecated.html" title="class or interface in java.lang">@Deprecated</a>
</span><span class="modifiers">public static</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">getPureTextFromHTMLSource</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> source)</span></div>
<div class="deprecation-block"><span class="deprecated-label">Deprecated.</span>
<div class="deprecation-comment">use <a href="../../../../../text/html/HtmlTextUtils.html#toPlainText(java.lang.String)"><code>HtmlTextUtils.toPlainText(String)</code></a></div>
</div>
</section>
</li>
<li>
<section class="detail" id="isHTMLText(java.lang.String)">
<h3>isHTMLText</h3>
<div class="member-signature"><span class="annotations"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Deprecated.html" title="class or interface in java.lang">@Deprecated</a>
</span><span class="modifiers">public static</span> <span class="return-type">boolean</span> <span class="element-name">isHTMLText</span><wbr/><span class="parameters">(@CheckForNull
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> text)</span></div>
<div class="deprecation-block"><span class="deprecated-label">Deprecated.</span>
<div class="deprecation-comment">use <a href="../../../../../text/html/HtmlTextUtils.html#isHtml(java.lang.String)"><code>HtmlTextUtils.isHtml(String)</code></a></div>
</div>
</section>
</li>
<li>
<section class="detail" id="removeHTMLHeader(java.lang.String)">
<h3>removeHTMLHeader</h3>
<div class="member-signature"><span class="annotations"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Deprecated.html" title="class or interface in java.lang">@Deprecated</a>
</span><span class="modifiers">public static</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">removeHTMLHeader</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> text)</span></div>
<div class="deprecation-block"><span class="deprecated-label">Deprecated.</span>
<div class="deprecation-comment">use <a href="../../../../../text/html/HtmlTextUtils.html#removeHtmlBodyPTags(java.lang.String)"><code>HtmlTextUtils.removeHtmlBodyPTags(String)</code></a></div>
</div>
</section>
</li>
<li>
<section class="detail" id="getHTMLBody(java.lang.String)">
<h3>getHTMLBody</h3>
<div class="member-signature"><span class="annotations"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Deprecated.html" title="class or interface in java.lang">@Deprecated</a>
</span><span class="modifiers">public static</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">getHTMLBody</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> text)</span></div>
<div class="deprecation-block"><span class="deprecated-label">Deprecated.</span>
<div class="deprecation-comment">use <a href="../../../../../text/html/HtmlTextUtils.html#removeHtmlBodyTags(java.lang.String)"><code>HtmlTextUtils.removeHtmlBodyTags(String)</code></a></div>
</div>
</section>
</li>
<li>
<section class="detail" id="constructHTMLText(java.lang.String)">
<h3>constructHTMLText</h3>
<div class="member-signature"><span class="annotations"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Deprecated.html" title="class or interface in java.lang">@Deprecated</a>
</span><span class="modifiers">public static</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">constructHTMLText</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> text)</span></div>
<div class="deprecation-block"><span class="deprecated-label">Deprecated.</span>
<div class="deprecation-comment">use <a href="../../../../../text/html/HtmlTextUtils.html#toHtmlText(java.lang.String)"><code>HtmlTextUtils.toHtmlText(String)</code></a></div>
</div>
</section>
</li>
<li>
<section class="detail" id="constructHTMLText(java.lang.String,boolean,boolean)">
<h3>constructHTMLText</h3>
<div class="member-signature"><span class="annotations"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Deprecated.html" title="class or interface in java.lang">@Deprecated</a>
</span><span class="modifiers">public static</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">constructHTMLText</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> text,
 boolean convertCharacters,
 boolean addEnterAfterP)</span></div>
<div class="deprecation-block"><span class="deprecated-label">Deprecated.</span>
<div class="deprecation-comment">use <code>HtmlTextUtilsInternal.toHtmlText(String, boolean, boolean)</code></div>
</div>
</section>
</li>
<li>
<section class="detail" id="makeStartTag(java.lang.String)">
<h3>makeStartTag</h3>
<div class="member-signature"><span class="annotations"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Deprecated.html" title="class or interface in java.lang">@Deprecated</a>
</span><span class="modifiers">public static</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">makeStartTag</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> tag)</span></div>
<div class="deprecation-block"><span class="deprecated-label">Deprecated.</span>
<div class="deprecation-comment">use <a href="../../../../../text/html/HtmlTextUtils.html#startTag(java.lang.String)"><code>HtmlTextUtils.startTag(String)</code></a></div>
</div>
</section>
</li>
<li>
<section class="detail" id="makeEndTag(java.lang.String)">
<h3>makeEndTag</h3>
<div class="member-signature"><span class="annotations"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Deprecated.html" title="class or interface in java.lang">@Deprecated</a>
</span><span class="modifiers">public static</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">makeEndTag</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> tag)</span></div>
<div class="deprecation-block"><span class="deprecated-label">Deprecated.</span>
<div class="deprecation-comment">use <a href="../../../../../text/html/HtmlTextUtils.html#endTag(java.lang.String)"><code>HtmlTextUtils.endTag(String)</code></a></div>
</div>
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
