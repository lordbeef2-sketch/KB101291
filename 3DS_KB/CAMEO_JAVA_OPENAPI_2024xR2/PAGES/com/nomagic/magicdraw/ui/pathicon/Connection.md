# JAVA OPENAPI: Connection (2024x API)

- source_url: https://jdocs.nomagic.com/2024xRefresh2/com/nomagic/magicdraw/ui/pathicon/Connection.html
- source_path: `com/nomagic/magicdraw/ui/pathicon/Connection.html`
- source_sha256: `63a3ebd3269c2ff84f3875308948ef4de2614d07ecf372df138575cdd914efea`
- captured_utc: `2026-07-14T16:55:50.686407+00:00`

## NORMALIZED JAVADOC CONTENT

======== START OF CLASS DATA ========

Package [com.nomagic.magicdraw.ui.pathicon](package-summary.html)

## Class Connection

[java.lang.Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)
com.nomagic.magicdraw.ui.pathicon.Connection

@OpenApiAllpublic final classConnection
extends [Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)
Constants defining the kind of connection using for painting the path icons

=========== FIELD SUMMARY =========== 
Field Summary
Fields
Modifier and Type
Field
Description
`static final int`
`[ARROW](#ARROW)`

`static final int`
`[ARROW_SMALL](#ARROW_SMALL)`

`static final int`
`[ARROW_THIN](#ARROW_THIN)`

`static final int`
`[ARROW_WIDE](#ARROW_WIDE)`

`static final int`
`[CIRCLE](#CIRCLE)`

`static final int`
`[CLOSED](#CLOSED)`
Should figure be closed (none is the same as opened)?
 In some cases this mask is not used, example drawing circle.
`static final int`
`[CLOSED_ARROW_AND_COLON](#CLOSED_ARROW_AND_COLON)`

`static final int`
`[CLOSED_ARROW_AND_DOUBLE_COLON](#CLOSED_ARROW_AND_DOUBLE_COLON)`

`static final int`
`[CLOSED_ARROW_AND_LINE](#CLOSED_ARROW_AND_LINE)`

`static final int`
`[CROSSED_CIRCLE](#CROSSED_CIRCLE)`

`static final int`
`[CROSSED_CIRCLE_DIAG](#CROSSED_CIRCLE_DIAG)`

`static final int`
`[DIAMOND_1](#DIAMOND_1)`

`static final int`
`[DIAMOND_2](#DIAMOND_2)`

`static final int`
`[DIAMOND_SQUARE](#DIAMOND_SQUARE)`

`static final int`
`[FILLED](#FILLED)`
Should be filled? This field is already combined with CLOSED.
`static final int`
`[GENERALIZATION](#GENERALIZATION)`

`static final int`
`[GENERALIZATION2](#GENERALIZATION2)`

`static final int`
`[HALF_CIRCLE](#HALF_CIRCLE)`

`static final int`
`[NONE](#NONE)`
No drawings, just simple line.
`static final int`
`[PACMAN](#PACMAN)`

`static final int`
`[SLASH](#SLASH)`

`static final int`
`[SQUARE](#SQUARE)`

`static final int[]`
`[STYLES](#STYLES)`
 ======== CONSTRUCTOR SUMMARY ======== 
Constructor Summary
Constructors
Constructor
Description
`[Connection](#%3Cinit%3E())()`
 ========== METHOD SUMMARY =========== 
Method Summary
All MethodsStatic MethodsConcrete Methods
Modifier and Type
Method
Description
`static [Point](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Point.html)`
`[drawConnection](#drawConnection(java.awt.Graphics2D,int,int,int,int,int,int,java.awt.Rectangle))([Graphics2D](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Graphics2D.html) g,
 int type,
 int x,
 int y,
 int x2,
 int y2,
 int preferredSize,
 [Rectangle](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Rectangle.html) shapeBounds)`
Method for Path end shape drawing.
`static [Point](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Point.html)`
`[drawConnection](#drawConnection(java.awt.Graphics2D,int,int,int,int,int,int,java.awt.Shape,boolean))([Graphics2D](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Graphics2D.html) g,
 int type,
 int x,
 int y,
 int x2,
 int y2,
 int preferredSize,
 [Shape](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Shape.html) boundingShape,
 boolean useCorrecting)`
Method for Path end shape drawing.
`static [Point](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Point.html)`
`[drawConnection](#drawConnection(java.awt.Graphics2D,com.nomagic.magicdraw.ui.pathicon.PathIcon,boolean,int,int,int,int,int,java.awt.Rectangle,java.util.function.Function))([Graphics2D](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Graphics2D.html) g,
 com.nomagic.magicdraw.ui.pathicon.PathIcon icon,
 boolean left,
 int x,
 int y,
 int x2,
 int y2,
 int size,
 [Rectangle](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Rectangle.html) shapeBounds,
 [Function](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/function/Function.html)<[ResizableIcon](../../../ui/ResizableIcon.html),[ResizableIcon](../../../ui/ResizableIcon.html)> iconTransformer)`

`static [Point](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Point.html)`
`[drawConnection](#drawConnection(java.awt.Graphics2D,com.nomagic.magicdraw.ui.pathicon.PathIcon,boolean,int,int,int,int,int,java.awt.Shape,boolean,java.util.function.Function))([Graphics2D](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Graphics2D.html) g,
 com.nomagic.magicdraw.ui.pathicon.PathIcon icon,
 boolean left,
 int x,
 int y,
 int x2,
 int y2,
 int size,
 [Shape](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Shape.html) boundingShape,
 boolean fixOverlapping,
 [Function](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/function/Function.html)<[ResizableIcon](../../../ui/ResizableIcon.html),[ResizableIcon](../../../ui/ResizableIcon.html)> iconTransformer)`
Paints connection end.
`static [Point](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Point.html)`
`[drawConnection](#drawConnection(java.awt.Graphics2D,com.nomagic.ui.ResizableIcon,int,int,int,int,int,java.awt.Rectangle,java.util.function.Function))([Graphics2D](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Graphics2D.html) g,
 [ResizableIcon](../../../ui/ResizableIcon.html) icon,
 int x,
 int y,
 int x2,
 int y2,
 int size,
 [Rectangle](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Rectangle.html) shapeBounds,
 [Function](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/function/Function.html)<[ResizableIcon](../../../ui/ResizableIcon.html),[ResizableIcon](../../../ui/ResizableIcon.html)> iconTransformer)`
Methods inherited from class java.lang.[Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)
`[clone](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#clone()), [equals](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#equals(java.lang.Object)), [finalize](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#finalize()), [getClass](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#getClass()), [hashCode](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#hashCode()), [notify](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notify()), [notifyAll](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notifyAll()), [toString](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#toString()), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait()), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long)), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long,int))`

============ FIELD DETAIL =========== 
Field Details
CLOSED
public static final int CLOSED
Should figure be closed (none is the same as opened)?
 In some cases this mask is not used, example drawing circle.
See Also:
[Constant Field Values](../../../../../constant-values.html#com.nomagic.magicdraw.ui.pathicon.Connection.CLOSED)
FILLED
public static final int FILLED
Should be filled? This field is already combined with CLOSED.
See Also:
[Constant Field Values](../../../../../constant-values.html#com.nomagic.magicdraw.ui.pathicon.Connection.FILLED)
NONE
public static final int NONE
No drawings, just simple line.
See Also:
[Constant Field Values](../../../../../constant-values.html#com.nomagic.magicdraw.ui.pathicon.Connection.NONE)
ARROW
public static final int ARROW
See Also:
[Constant Field Values](../../../../../constant-values.html#com.nomagic.magicdraw.ui.pathicon.Connection.ARROW)
GENERALIZATION
public static final int GENERALIZATION
See Also:
[Constant Field Values](../../../../../constant-values.html#com.nomagic.magicdraw.ui.pathicon.Connection.GENERALIZATION)
GENERALIZATION2
public static final int GENERALIZATION2
See Also:
[Constant Field Values](../../../../../constant-values.html#com.nomagic.magicdraw.ui.pathicon.Connection.GENERALIZATION2)
CIRCLE
public static final int CIRCLE
See Also:
[Constant Field Values](../../../../../constant-values.html#com.nomagic.magicdraw.ui.pathicon.Connection.CIRCLE)
SQUARE
public static final int SQUARE
See Also:
[Constant Field Values](../../../../../constant-values.html#com.nomagic.magicdraw.ui.pathicon.Connection.SQUARE)
DIAMOND_SQUARE
public static final int DIAMOND_SQUARE
See Also:
[Constant Field Values](../../../../../constant-values.html#com.nomagic.magicdraw.ui.pathicon.Connection.DIAMOND_SQUARE)
DIAMOND_1
public static final int DIAMOND_1
See Also:
[Constant Field Values](../../../../../constant-values.html#com.nomagic.magicdraw.ui.pathicon.Connection.DIAMOND_1)
ARROW_WIDE
public static final int ARROW_WIDE
See Also:
[Constant Field Values](../../../../../constant-values.html#com.nomagic.magicdraw.ui.pathicon.Connection.ARROW_WIDE)
ARROW_THIN
public static final int ARROW_THIN
See Also:
[Constant Field Values](../../../../../constant-values.html#com.nomagic.magicdraw.ui.pathicon.Connection.ARROW_THIN)
CROSSED_CIRCLE
public static final int CROSSED_CIRCLE
See Also:
[Constant Field Values](../../../../../constant-values.html#com.nomagic.magicdraw.ui.pathicon.Connection.CROSSED_CIRCLE)
ARROW_SMALL
public static final int ARROW_SMALL
See Also:
[Constant Field Values](../../../../../constant-values.html#com.nomagic.magicdraw.ui.pathicon.Connection.ARROW_SMALL)
CROSSED_CIRCLE_DIAG
public static final int CROSSED_CIRCLE_DIAG
See Also:
[Constant Field Values](../../../../../constant-values.html#com.nomagic.magicdraw.ui.pathicon.Connection.CROSSED_CIRCLE_DIAG)
SLASH
public static final int SLASH
See Also:
[Constant Field Values](../../../../../constant-values.html#com.nomagic.magicdraw.ui.pathicon.Connection.SLASH)
HALF_CIRCLE
public static final int HALF_CIRCLE
See Also:
[Constant Field Values](../../../../../constant-values.html#com.nomagic.magicdraw.ui.pathicon.Connection.HALF_CIRCLE)
CLOSED_ARROW_AND_LINE
public static final int CLOSED_ARROW_AND_LINE
See Also:
[Constant Field Values](../../../../../constant-values.html#com.nomagic.magicdraw.ui.pathicon.Connection.CLOSED_ARROW_AND_LINE)
CLOSED_ARROW_AND_COLON
public static final int CLOSED_ARROW_AND_COLON
See Also:
[Constant Field Values](../../../../../constant-values.html#com.nomagic.magicdraw.ui.pathicon.Connection.CLOSED_ARROW_AND_COLON)
CLOSED_ARROW_AND_DOUBLE_COLON
public static final int CLOSED_ARROW_AND_DOUBLE_COLON
See Also:
[Constant Field Values](../../../../../constant-values.html#com.nomagic.magicdraw.ui.pathicon.Connection.CLOSED_ARROW_AND_DOUBLE_COLON)
DIAMOND_2
public static final int DIAMOND_2
See Also:
[Constant Field Values](../../../../../constant-values.html#com.nomagic.magicdraw.ui.pathicon.Connection.DIAMOND_2)
PACMAN
public static final int PACMAN
See Also:
[Constant Field Values](../../../../../constant-values.html#com.nomagic.magicdraw.ui.pathicon.Connection.PACMAN)
STYLES
public static final int[] STYLES
 ========= CONSTRUCTOR DETAIL ======== 
Constructor Details
Connection
public Connection()
 ============ METHOD DETAIL ========== 
Method Details
drawConnection
public static [Point](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Point.html) drawConnection([Graphics2D](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Graphics2D.html) g,
 int type,
 int x,
 int y,
 int x2,
 int y2,
 int preferredSize,
 @CheckForNull
 [Shape](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Shape.html) boundingShape,
 boolean useCorrecting)
Method for Path end shape drawing.
Parameters:
`g` - graphics context
`type` - path end draw style
`x` - from point
`y` - from point
`x2` - to point
`y2` - to point
`preferredSize` - preferred size of path end shape
`boundingShape` - client bounding shape
`useCorrecting` - use correcting in case the link end symbol covers specified bounds
Returns:
Point where path line should begin
See Also:
[`Connection`](Connection.html)
drawConnection
public static [Point](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Point.html) drawConnection([Graphics2D](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Graphics2D.html) g,
 int type,
 int x,
 int y,
 int x2,
 int y2,
 int preferredSize,
 @CheckForNull
 [Rectangle](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Rectangle.html) shapeBounds)
Method for Path end shape drawing.
Parameters:
`g` - graphics context
`type` - path end draw style
`x` - from point
`y` - from point
`x2` - to point
`y2` - to point
`preferredSize` - preferred size of path end shape
`shapeBounds` - connected shape bounds
Returns:
Point where path line should begin
See Also:
[`Connection`](Connection.html)
drawConnection
public static [Point](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Point.html) drawConnection([Graphics2D](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Graphics2D.html) g,
 com.nomagic.magicdraw.ui.pathicon.PathIcon icon,
 boolean left,
 int x,
 int y,
 int x2,
 int y2,
 int size,
 @CheckForNull
 [Shape](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Shape.html) boundingShape,
 boolean fixOverlapping,
 [Function](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/function/Function.html)<[ResizableIcon](../../../ui/ResizableIcon.html),[ResizableIcon](../../../ui/ResizableIcon.html)> iconTransformer)
Paints connection end.
Parameters:
`g` - graphics context
`icon` - icon of the end
`left` - left connection
`x` - x coordinate of the intersection with the shape point
`y` - y coordinate of the intersection with the shape point
`x2` - x coordinate of the next link segment point
`y2` - y coordinate of the next link segment point
`size` - size of the icon
`boundingShape` - bounding shape
`fixOverlapping` - if true then correcting of the link end shape covering client or supplier shape should be used
Returns:
connection point from which link must be painted
drawConnection
public static [Point](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Point.html) drawConnection([Graphics2D](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Graphics2D.html) g,
 com.nomagic.magicdraw.ui.pathicon.PathIcon icon,
 boolean left,
 int x,
 int y,
 int x2,
 int y2,
 int size,
 @CheckForNull
 [Rectangle](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Rectangle.html) shapeBounds,
 [Function](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/function/Function.html)<[ResizableIcon](../../../ui/ResizableIcon.html),[ResizableIcon](../../../ui/ResizableIcon.html)> iconTransformer)
drawConnection
public static [Point](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Point.html) drawConnection([Graphics2D](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Graphics2D.html) g,
 [ResizableIcon](../../../ui/ResizableIcon.html) icon,
 int x,
 int y,
 int x2,
 int y2,
 int size,
 @CheckForNull
 [Rectangle](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Rectangle.html) shapeBounds,
 [Function](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/function/Function.html)<[ResizableIcon](../../../ui/ResizableIcon.html),[ResizableIcon](../../../ui/ResizableIcon.html)> iconTransformer)

========= END OF CLASS DATA =========

## EXACT JAVADOC MAIN HTML

````html
<main role="main">
<!-- ======== START OF CLASS DATA ======== -->
<div class="header">
<div class="sub-title"><span class="package-label-in-type">Package</span> <a href="package-summary.html">com.nomagic.magicdraw.ui.pathicon</a></div>
<h1 class="title" title="Class Connection">Class Connection</h1>
</div>
<div class="inheritance" title="Inheritance Tree"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">java.lang.Object</a>
<div class="inheritance">com.nomagic.magicdraw.ui.pathicon.Connection</div>
</div>
<section class="class-description" id="class-description">
<hr/>
<div class="type-signature"><span class="annotations">@OpenApiAll
</span><span class="modifiers">public final class </span><span class="element-name type-name-label">Connection</span>
<span class="extends-implements">extends <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a></span></div>
<div class="block">Constants defining the kind of connection using for painting the path icons</div>
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
<div class="col-first even-row-color"><code>static final int</code></div>
<div class="col-second even-row-color"><code><a class="member-name-link" href="#ARROW">ARROW</a></code></div>
<div class="col-last even-row-color"> </div>
<div class="col-first odd-row-color"><code>static final int</code></div>
<div class="col-second odd-row-color"><code><a class="member-name-link" href="#ARROW_SMALL">ARROW_SMALL</a></code></div>
<div class="col-last odd-row-color"> </div>
<div class="col-first even-row-color"><code>static final int</code></div>
<div class="col-second even-row-color"><code><a class="member-name-link" href="#ARROW_THIN">ARROW_THIN</a></code></div>
<div class="col-last even-row-color"> </div>
<div class="col-first odd-row-color"><code>static final int</code></div>
<div class="col-second odd-row-color"><code><a class="member-name-link" href="#ARROW_WIDE">ARROW_WIDE</a></code></div>
<div class="col-last odd-row-color"> </div>
<div class="col-first even-row-color"><code>static final int</code></div>
<div class="col-second even-row-color"><code><a class="member-name-link" href="#CIRCLE">CIRCLE</a></code></div>
<div class="col-last even-row-color"> </div>
<div class="col-first odd-row-color"><code>static final int</code></div>
<div class="col-second odd-row-color"><code><a class="member-name-link" href="#CLOSED">CLOSED</a></code></div>
<div class="col-last odd-row-color">
<div class="block">Should figure be closed (none is the same as opened)?
 In some cases this mask is not used, example drawing circle.</div>
</div>
<div class="col-first even-row-color"><code>static final int</code></div>
<div class="col-second even-row-color"><code><a class="member-name-link" href="#CLOSED_ARROW_AND_COLON">CLOSED_ARROW_AND_COLON</a></code></div>
<div class="col-last even-row-color"> </div>
<div class="col-first odd-row-color"><code>static final int</code></div>
<div class="col-second odd-row-color"><code><a class="member-name-link" href="#CLOSED_ARROW_AND_DOUBLE_COLON">CLOSED_ARROW_AND_DOUBLE_COLON</a></code></div>
<div class="col-last odd-row-color"> </div>
<div class="col-first even-row-color"><code>static final int</code></div>
<div class="col-second even-row-color"><code><a class="member-name-link" href="#CLOSED_ARROW_AND_LINE">CLOSED_ARROW_AND_LINE</a></code></div>
<div class="col-last even-row-color"> </div>
<div class="col-first odd-row-color"><code>static final int</code></div>
<div class="col-second odd-row-color"><code><a class="member-name-link" href="#CROSSED_CIRCLE">CROSSED_CIRCLE</a></code></div>
<div class="col-last odd-row-color"> </div>
<div class="col-first even-row-color"><code>static final int</code></div>
<div class="col-second even-row-color"><code><a class="member-name-link" href="#CROSSED_CIRCLE_DIAG">CROSSED_CIRCLE_DIAG</a></code></div>
<div class="col-last even-row-color"> </div>
<div class="col-first odd-row-color"><code>static final int</code></div>
<div class="col-second odd-row-color"><code><a class="member-name-link" href="#DIAMOND_1">DIAMOND_1</a></code></div>
<div class="col-last odd-row-color"> </div>
<div class="col-first even-row-color"><code>static final int</code></div>
<div class="col-second even-row-color"><code><a class="member-name-link" href="#DIAMOND_2">DIAMOND_2</a></code></div>
<div class="col-last even-row-color"> </div>
<div class="col-first odd-row-color"><code>static final int</code></div>
<div class="col-second odd-row-color"><code><a class="member-name-link" href="#DIAMOND_SQUARE">DIAMOND_SQUARE</a></code></div>
<div class="col-last odd-row-color"> </div>
<div class="col-first even-row-color"><code>static final int</code></div>
<div class="col-second even-row-color"><code><a class="member-name-link" href="#FILLED">FILLED</a></code></div>
<div class="col-last even-row-color">
<div class="block">Should be filled?  This field is already combined with CLOSED.</div>
</div>
<div class="col-first odd-row-color"><code>static final int</code></div>
<div class="col-second odd-row-color"><code><a class="member-name-link" href="#GENERALIZATION">GENERALIZATION</a></code></div>
<div class="col-last odd-row-color"> </div>
<div class="col-first even-row-color"><code>static final int</code></div>
<div class="col-second even-row-color"><code><a class="member-name-link" href="#GENERALIZATION2">GENERALIZATION2</a></code></div>
<div class="col-last even-row-color"> </div>
<div class="col-first odd-row-color"><code>static final int</code></div>
<div class="col-second odd-row-color"><code><a class="member-name-link" href="#HALF_CIRCLE">HALF_CIRCLE</a></code></div>
<div class="col-last odd-row-color"> </div>
<div class="col-first even-row-color"><code>static final int</code></div>
<div class="col-second even-row-color"><code><a class="member-name-link" href="#NONE">NONE</a></code></div>
<div class="col-last even-row-color">
<div class="block">No drawings, just simple line.</div>
</div>
<div class="col-first odd-row-color"><code>static final int</code></div>
<div class="col-second odd-row-color"><code><a class="member-name-link" href="#PACMAN">PACMAN</a></code></div>
<div class="col-last odd-row-color"> </div>
<div class="col-first even-row-color"><code>static final int</code></div>
<div class="col-second even-row-color"><code><a class="member-name-link" href="#SLASH">SLASH</a></code></div>
<div class="col-last even-row-color"> </div>
<div class="col-first odd-row-color"><code>static final int</code></div>
<div class="col-second odd-row-color"><code><a class="member-name-link" href="#SQUARE">SQUARE</a></code></div>
<div class="col-last odd-row-color"> </div>
<div class="col-first even-row-color"><code>static final int[]</code></div>
<div class="col-second even-row-color"><code><a class="member-name-link" href="#STYLES">STYLES</a></code></div>
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
<div class="col-constructor-name even-row-color"><code><a class="member-name-link" href="#%3Cinit%3E()">Connection</a>()</code></div>
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
<div class="col-first even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Point.html" title="class or interface in java.awt">Point</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#drawConnection(java.awt.Graphics2D,int,int,int,int,int,int,java.awt.Rectangle)">drawConnection</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Graphics2D.html" title="class or interface in java.awt">Graphics2D</a> g,
 int type,
 int x,
 int y,
 int x2,
 int y2,
 int preferredSize,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Rectangle.html" title="class or interface in java.awt">Rectangle</a> shapeBounds)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Method for Path end shape drawing.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Point.html" title="class or interface in java.awt">Point</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#drawConnection(java.awt.Graphics2D,int,int,int,int,int,int,java.awt.Shape,boolean)">drawConnection</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Graphics2D.html" title="class or interface in java.awt">Graphics2D</a> g,
 int type,
 int x,
 int y,
 int x2,
 int y2,
 int preferredSize,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Shape.html" title="class or interface in java.awt">Shape</a> boundingShape,
 boolean useCorrecting)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Method for Path end shape drawing.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Point.html" title="class or interface in java.awt">Point</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#drawConnection(java.awt.Graphics2D,com.nomagic.magicdraw.ui.pathicon.PathIcon,boolean,int,int,int,int,int,java.awt.Rectangle,java.util.function.Function)">drawConnection</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Graphics2D.html" title="class or interface in java.awt">Graphics2D</a> g,
 com.nomagic.magicdraw.ui.pathicon.PathIcon icon,
 boolean left,
 int x,
 int y,
 int x2,
 int y2,
 int size,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Rectangle.html" title="class or interface in java.awt">Rectangle</a> shapeBounds,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/function/Function.html" title="class or interface in java.util.function">Function</a>&lt;<a href="../../../ui/ResizableIcon.html" title="interface in com.nomagic.ui">ResizableIcon</a>,<wbr/><a href="../../../ui/ResizableIcon.html" title="interface in com.nomagic.ui">ResizableIcon</a>&gt; iconTransformer)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Point.html" title="class or interface in java.awt">Point</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#drawConnection(java.awt.Graphics2D,com.nomagic.magicdraw.ui.pathicon.PathIcon,boolean,int,int,int,int,int,java.awt.Shape,boolean,java.util.function.Function)">drawConnection</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Graphics2D.html" title="class or interface in java.awt">Graphics2D</a> g,
 com.nomagic.magicdraw.ui.pathicon.PathIcon icon,
 boolean left,
 int x,
 int y,
 int x2,
 int y2,
 int size,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Shape.html" title="class or interface in java.awt">Shape</a> boundingShape,
 boolean fixOverlapping,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/function/Function.html" title="class or interface in java.util.function">Function</a>&lt;<a href="../../../ui/ResizableIcon.html" title="interface in com.nomagic.ui">ResizableIcon</a>,<wbr/><a href="../../../ui/ResizableIcon.html" title="interface in com.nomagic.ui">ResizableIcon</a>&gt; iconTransformer)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Paints connection end.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Point.html" title="class or interface in java.awt">Point</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#drawConnection(java.awt.Graphics2D,com.nomagic.ui.ResizableIcon,int,int,int,int,int,java.awt.Rectangle,java.util.function.Function)">drawConnection</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Graphics2D.html" title="class or interface in java.awt">Graphics2D</a> g,
 <a href="../../../ui/ResizableIcon.html" title="interface in com.nomagic.ui">ResizableIcon</a> icon,
 int x,
 int y,
 int x2,
 int y2,
 int size,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Rectangle.html" title="class or interface in java.awt">Rectangle</a> shapeBounds,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/function/Function.html" title="class or interface in java.util.function">Function</a>&lt;<a href="../../../ui/ResizableIcon.html" title="interface in com.nomagic.ui">ResizableIcon</a>,<wbr/><a href="../../../ui/ResizableIcon.html" title="interface in com.nomagic.ui">ResizableIcon</a>&gt; iconTransformer)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"> </div>
</div>
</div>
</div>
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
<section class="detail" id="CLOSED">
<h3>CLOSED</h3>
<div class="member-signature"><span class="modifiers">public static final</span> <span class="return-type">int</span> <span class="element-name">CLOSED</span></div>
<div class="block">Should figure be closed (none is the same as opened)?
 In some cases this mask is not used, example drawing circle.</div>
<dl class="notes">
<dt>See Also:</dt>
<dd>
<ul class="see-list">
<li><a href="../../../../../constant-values.html#com.nomagic.magicdraw.ui.pathicon.Connection.CLOSED">Constant Field Values</a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="FILLED">
<h3>FILLED</h3>
<div class="member-signature"><span class="modifiers">public static final</span> <span class="return-type">int</span> <span class="element-name">FILLED</span></div>
<div class="block">Should be filled?  This field is already combined with CLOSED.</div>
<dl class="notes">
<dt>See Also:</dt>
<dd>
<ul class="see-list">
<li><a href="../../../../../constant-values.html#com.nomagic.magicdraw.ui.pathicon.Connection.FILLED">Constant Field Values</a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="NONE">
<h3>NONE</h3>
<div class="member-signature"><span class="modifiers">public static final</span> <span class="return-type">int</span> <span class="element-name">NONE</span></div>
<div class="block">No drawings, just simple line.</div>
<dl class="notes">
<dt>See Also:</dt>
<dd>
<ul class="see-list">
<li><a href="../../../../../constant-values.html#com.nomagic.magicdraw.ui.pathicon.Connection.NONE">Constant Field Values</a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="ARROW">
<h3>ARROW</h3>
<div class="member-signature"><span class="modifiers">public static final</span> <span class="return-type">int</span> <span class="element-name">ARROW</span></div>
<dl class="notes">
<dt>See Also:</dt>
<dd>
<ul class="see-list">
<li><a href="../../../../../constant-values.html#com.nomagic.magicdraw.ui.pathicon.Connection.ARROW">Constant Field Values</a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="GENERALIZATION">
<h3>GENERALIZATION</h3>
<div class="member-signature"><span class="modifiers">public static final</span> <span class="return-type">int</span> <span class="element-name">GENERALIZATION</span></div>
<dl class="notes">
<dt>See Also:</dt>
<dd>
<ul class="see-list">
<li><a href="../../../../../constant-values.html#com.nomagic.magicdraw.ui.pathicon.Connection.GENERALIZATION">Constant Field Values</a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="GENERALIZATION2">
<h3>GENERALIZATION2</h3>
<div class="member-signature"><span class="modifiers">public static final</span> <span class="return-type">int</span> <span class="element-name">GENERALIZATION2</span></div>
<dl class="notes">
<dt>See Also:</dt>
<dd>
<ul class="see-list">
<li><a href="../../../../../constant-values.html#com.nomagic.magicdraw.ui.pathicon.Connection.GENERALIZATION2">Constant Field Values</a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="CIRCLE">
<h3>CIRCLE</h3>
<div class="member-signature"><span class="modifiers">public static final</span> <span class="return-type">int</span> <span class="element-name">CIRCLE</span></div>
<dl class="notes">
<dt>See Also:</dt>
<dd>
<ul class="see-list">
<li><a href="../../../../../constant-values.html#com.nomagic.magicdraw.ui.pathicon.Connection.CIRCLE">Constant Field Values</a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="SQUARE">
<h3>SQUARE</h3>
<div class="member-signature"><span class="modifiers">public static final</span> <span class="return-type">int</span> <span class="element-name">SQUARE</span></div>
<dl class="notes">
<dt>See Also:</dt>
<dd>
<ul class="see-list">
<li><a href="../../../../../constant-values.html#com.nomagic.magicdraw.ui.pathicon.Connection.SQUARE">Constant Field Values</a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="DIAMOND_SQUARE">
<h3>DIAMOND_SQUARE</h3>
<div class="member-signature"><span class="modifiers">public static final</span> <span class="return-type">int</span> <span class="element-name">DIAMOND_SQUARE</span></div>
<dl class="notes">
<dt>See Also:</dt>
<dd>
<ul class="see-list">
<li><a href="../../../../../constant-values.html#com.nomagic.magicdraw.ui.pathicon.Connection.DIAMOND_SQUARE">Constant Field Values</a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="DIAMOND_1">
<h3>DIAMOND_1</h3>
<div class="member-signature"><span class="modifiers">public static final</span> <span class="return-type">int</span> <span class="element-name">DIAMOND_1</span></div>
<dl class="notes">
<dt>See Also:</dt>
<dd>
<ul class="see-list">
<li><a href="../../../../../constant-values.html#com.nomagic.magicdraw.ui.pathicon.Connection.DIAMOND_1">Constant Field Values</a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="ARROW_WIDE">
<h3>ARROW_WIDE</h3>
<div class="member-signature"><span class="modifiers">public static final</span> <span class="return-type">int</span> <span class="element-name">ARROW_WIDE</span></div>
<dl class="notes">
<dt>See Also:</dt>
<dd>
<ul class="see-list">
<li><a href="../../../../../constant-values.html#com.nomagic.magicdraw.ui.pathicon.Connection.ARROW_WIDE">Constant Field Values</a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="ARROW_THIN">
<h3>ARROW_THIN</h3>
<div class="member-signature"><span class="modifiers">public static final</span> <span class="return-type">int</span> <span class="element-name">ARROW_THIN</span></div>
<dl class="notes">
<dt>See Also:</dt>
<dd>
<ul class="see-list">
<li><a href="../../../../../constant-values.html#com.nomagic.magicdraw.ui.pathicon.Connection.ARROW_THIN">Constant Field Values</a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="CROSSED_CIRCLE">
<h3>CROSSED_CIRCLE</h3>
<div class="member-signature"><span class="modifiers">public static final</span> <span class="return-type">int</span> <span class="element-name">CROSSED_CIRCLE</span></div>
<dl class="notes">
<dt>See Also:</dt>
<dd>
<ul class="see-list">
<li><a href="../../../../../constant-values.html#com.nomagic.magicdraw.ui.pathicon.Connection.CROSSED_CIRCLE">Constant Field Values</a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="ARROW_SMALL">
<h3>ARROW_SMALL</h3>
<div class="member-signature"><span class="modifiers">public static final</span> <span class="return-type">int</span> <span class="element-name">ARROW_SMALL</span></div>
<dl class="notes">
<dt>See Also:</dt>
<dd>
<ul class="see-list">
<li><a href="../../../../../constant-values.html#com.nomagic.magicdraw.ui.pathicon.Connection.ARROW_SMALL">Constant Field Values</a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="CROSSED_CIRCLE_DIAG">
<h3>CROSSED_CIRCLE_DIAG</h3>
<div class="member-signature"><span class="modifiers">public static final</span> <span class="return-type">int</span> <span class="element-name">CROSSED_CIRCLE_DIAG</span></div>
<dl class="notes">
<dt>See Also:</dt>
<dd>
<ul class="see-list">
<li><a href="../../../../../constant-values.html#com.nomagic.magicdraw.ui.pathicon.Connection.CROSSED_CIRCLE_DIAG">Constant Field Values</a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="SLASH">
<h3>SLASH</h3>
<div class="member-signature"><span class="modifiers">public static final</span> <span class="return-type">int</span> <span class="element-name">SLASH</span></div>
<dl class="notes">
<dt>See Also:</dt>
<dd>
<ul class="see-list">
<li><a href="../../../../../constant-values.html#com.nomagic.magicdraw.ui.pathicon.Connection.SLASH">Constant Field Values</a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="HALF_CIRCLE">
<h3>HALF_CIRCLE</h3>
<div class="member-signature"><span class="modifiers">public static final</span> <span class="return-type">int</span> <span class="element-name">HALF_CIRCLE</span></div>
<dl class="notes">
<dt>See Also:</dt>
<dd>
<ul class="see-list">
<li><a href="../../../../../constant-values.html#com.nomagic.magicdraw.ui.pathicon.Connection.HALF_CIRCLE">Constant Field Values</a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="CLOSED_ARROW_AND_LINE">
<h3>CLOSED_ARROW_AND_LINE</h3>
<div class="member-signature"><span class="modifiers">public static final</span> <span class="return-type">int</span> <span class="element-name">CLOSED_ARROW_AND_LINE</span></div>
<dl class="notes">
<dt>See Also:</dt>
<dd>
<ul class="see-list">
<li><a href="../../../../../constant-values.html#com.nomagic.magicdraw.ui.pathicon.Connection.CLOSED_ARROW_AND_LINE">Constant Field Values</a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="CLOSED_ARROW_AND_COLON">
<h3>CLOSED_ARROW_AND_COLON</h3>
<div class="member-signature"><span class="modifiers">public static final</span> <span class="return-type">int</span> <span class="element-name">CLOSED_ARROW_AND_COLON</span></div>
<dl class="notes">
<dt>See Also:</dt>
<dd>
<ul class="see-list">
<li><a href="../../../../../constant-values.html#com.nomagic.magicdraw.ui.pathicon.Connection.CLOSED_ARROW_AND_COLON">Constant Field Values</a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="CLOSED_ARROW_AND_DOUBLE_COLON">
<h3>CLOSED_ARROW_AND_DOUBLE_COLON</h3>
<div class="member-signature"><span class="modifiers">public static final</span> <span class="return-type">int</span> <span class="element-name">CLOSED_ARROW_AND_DOUBLE_COLON</span></div>
<dl class="notes">
<dt>See Also:</dt>
<dd>
<ul class="see-list">
<li><a href="../../../../../constant-values.html#com.nomagic.magicdraw.ui.pathicon.Connection.CLOSED_ARROW_AND_DOUBLE_COLON">Constant Field Values</a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="DIAMOND_2">
<h3>DIAMOND_2</h3>
<div class="member-signature"><span class="modifiers">public static final</span> <span class="return-type">int</span> <span class="element-name">DIAMOND_2</span></div>
<dl class="notes">
<dt>See Also:</dt>
<dd>
<ul class="see-list">
<li><a href="../../../../../constant-values.html#com.nomagic.magicdraw.ui.pathicon.Connection.DIAMOND_2">Constant Field Values</a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="PACMAN">
<h3>PACMAN</h3>
<div class="member-signature"><span class="modifiers">public static final</span> <span class="return-type">int</span> <span class="element-name">PACMAN</span></div>
<dl class="notes">
<dt>See Also:</dt>
<dd>
<ul class="see-list">
<li><a href="../../../../../constant-values.html#com.nomagic.magicdraw.ui.pathicon.Connection.PACMAN">Constant Field Values</a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="STYLES">
<h3>STYLES</h3>
<div class="member-signature"><span class="modifiers">public static final</span> <span class="return-type">int[]</span> <span class="element-name">STYLES</span></div>
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
<h3>Connection</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="element-name">Connection</span>()</div>
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
<section class="detail" id="drawConnection(java.awt.Graphics2D,int,int,int,int,int,int,java.awt.Shape,boolean)">
<h3>drawConnection</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Point.html" title="class or interface in java.awt">Point</a></span> <span class="element-name">drawConnection</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Graphics2D.html" title="class or interface in java.awt">Graphics2D</a> g,
 int type,
 int x,
 int y,
 int x2,
 int y2,
 int preferredSize,
 @CheckForNull
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Shape.html" title="class or interface in java.awt">Shape</a> boundingShape,
 boolean useCorrecting)</span></div>
<div class="block">Method for Path end shape drawing.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>g</code> - graphics context</dd>
<dd><code>type</code> - path end draw style</dd>
<dd><code>x</code> - from point</dd>
<dd><code>y</code> - from point</dd>
<dd><code>x2</code> - to point</dd>
<dd><code>y2</code> - to point</dd>
<dd><code>preferredSize</code> - preferred size of path end shape</dd>
<dd><code>boundingShape</code> - client bounding shape</dd>
<dd><code>useCorrecting</code> - use correcting in case the link end symbol covers specified bounds</dd>
<dt>Returns:</dt>
<dd>Point where path line should begin</dd>
<dt>See Also:</dt>
<dd>
<ul class="see-list">
<li><a href="Connection.html" title="class in com.nomagic.magicdraw.ui.pathicon"><code>Connection</code></a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="drawConnection(java.awt.Graphics2D,int,int,int,int,int,int,java.awt.Rectangle)">
<h3>drawConnection</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Point.html" title="class or interface in java.awt">Point</a></span> <span class="element-name">drawConnection</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Graphics2D.html" title="class or interface in java.awt">Graphics2D</a> g,
 int type,
 int x,
 int y,
 int x2,
 int y2,
 int preferredSize,
 @CheckForNull
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Rectangle.html" title="class or interface in java.awt">Rectangle</a> shapeBounds)</span></div>
<div class="block">Method for Path end shape drawing.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>g</code> - graphics context</dd>
<dd><code>type</code> - path end draw style</dd>
<dd><code>x</code> - from point</dd>
<dd><code>y</code> - from point</dd>
<dd><code>x2</code> - to point</dd>
<dd><code>y2</code> - to point</dd>
<dd><code>preferredSize</code> - preferred size of path end shape</dd>
<dd><code>shapeBounds</code> - connected shape bounds</dd>
<dt>Returns:</dt>
<dd>Point where path line should begin</dd>
<dt>See Also:</dt>
<dd>
<ul class="see-list">
<li><a href="Connection.html" title="class in com.nomagic.magicdraw.ui.pathicon"><code>Connection</code></a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="drawConnection(java.awt.Graphics2D,com.nomagic.magicdraw.ui.pathicon.PathIcon,boolean,int,int,int,int,int,java.awt.Shape,boolean,java.util.function.Function)">
<h3>drawConnection</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Point.html" title="class or interface in java.awt">Point</a></span> <span class="element-name">drawConnection</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Graphics2D.html" title="class or interface in java.awt">Graphics2D</a> g,
 com.nomagic.magicdraw.ui.pathicon.PathIcon icon,
 boolean left,
 int x,
 int y,
 int x2,
 int y2,
 int size,
 @CheckForNull
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Shape.html" title="class or interface in java.awt">Shape</a> boundingShape,
 boolean fixOverlapping,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/function/Function.html" title="class or interface in java.util.function">Function</a>&lt;<a href="../../../ui/ResizableIcon.html" title="interface in com.nomagic.ui">ResizableIcon</a>,<wbr/><a href="../../../ui/ResizableIcon.html" title="interface in com.nomagic.ui">ResizableIcon</a>&gt; iconTransformer)</span></div>
<div class="block">Paints connection end.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>g</code> - graphics context</dd>
<dd><code>icon</code> - icon of the end</dd>
<dd><code>left</code> - left connection</dd>
<dd><code>x</code> - x coordinate of the intersection with the shape point</dd>
<dd><code>y</code> - y coordinate of the intersection with the shape point</dd>
<dd><code>x2</code> - x coordinate of the next link segment point</dd>
<dd><code>y2</code> - y coordinate of the next link segment point</dd>
<dd><code>size</code> - size of the icon</dd>
<dd><code>boundingShape</code> - bounding shape</dd>
<dd><code>fixOverlapping</code> - if true then correcting of the link end shape covering client or supplier shape should be used</dd>
<dt>Returns:</dt>
<dd>connection point from which link must be painted</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="drawConnection(java.awt.Graphics2D,com.nomagic.magicdraw.ui.pathicon.PathIcon,boolean,int,int,int,int,int,java.awt.Rectangle,java.util.function.Function)">
<h3>drawConnection</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Point.html" title="class or interface in java.awt">Point</a></span> <span class="element-name">drawConnection</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Graphics2D.html" title="class or interface in java.awt">Graphics2D</a> g,
 com.nomagic.magicdraw.ui.pathicon.PathIcon icon,
 boolean left,
 int x,
 int y,
 int x2,
 int y2,
 int size,
 @CheckForNull
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Rectangle.html" title="class or interface in java.awt">Rectangle</a> shapeBounds,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/function/Function.html" title="class or interface in java.util.function">Function</a>&lt;<a href="../../../ui/ResizableIcon.html" title="interface in com.nomagic.ui">ResizableIcon</a>,<wbr/><a href="../../../ui/ResizableIcon.html" title="interface in com.nomagic.ui">ResizableIcon</a>&gt; iconTransformer)</span></div>
</section>
</li>
<li>
<section class="detail" id="drawConnection(java.awt.Graphics2D,com.nomagic.ui.ResizableIcon,int,int,int,int,int,java.awt.Rectangle,java.util.function.Function)">
<h3>drawConnection</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Point.html" title="class or interface in java.awt">Point</a></span> <span class="element-name">drawConnection</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Graphics2D.html" title="class or interface in java.awt">Graphics2D</a> g,
 <a href="../../../ui/ResizableIcon.html" title="interface in com.nomagic.ui">ResizableIcon</a> icon,
 int x,
 int y,
 int x2,
 int y2,
 int size,
 @CheckForNull
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Rectangle.html" title="class or interface in java.awt">Rectangle</a> shapeBounds,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/function/Function.html" title="class or interface in java.util.function">Function</a>&lt;<a href="../../../ui/ResizableIcon.html" title="interface in com.nomagic.ui">ResizableIcon</a>,<wbr/><a href="../../../ui/ResizableIcon.html" title="interface in com.nomagic.ui">ResizableIcon</a>&gt; iconTransformer)</span></div>
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
