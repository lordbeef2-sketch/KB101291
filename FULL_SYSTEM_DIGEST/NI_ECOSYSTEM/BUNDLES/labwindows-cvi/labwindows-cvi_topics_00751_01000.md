# NI DOCUMENT BUNDLE: labwindows-cvi

<!--NI_BUNDLE_CHUNK bundle=labwindows-cvi start=751 end=1000 -->
<!--NI_TOPIC bundle=labwindows-cvi path=cvi/uiref/cviattrplotlgvisible.htm language=enus -->
## TOPIC 00751: ATTR_PLOT_LG_VISIBLE

- bundle_id: `labwindows-cvi`
- source_path: `cvi/uiref/cviattrplotlgvisible.htm`
- source_url: https://docs-be.ni.com/bundle/labwindows-cvi/raw/resource/enus/cvi/uiref/cviattrplotlgvisible.htm
- document_id: `labwindows-cvi`
- page_type: `leaf`
- content_type: ``

### ATTR_PLOT_LG_VISIBLE

| Type: | Plot attribute |
| --- | --- |
| Description: | Specifies whether the graph legend should show an item corresponding to this plot. If, at the time the plot was added to the graph, the graph ATTR_LEGEND_AUTO_DISPLAY attribute was enabled, then the plot will have this attribute set to 1 by default, otherwise it will be set to 0. |
| Plot Types: | Arc, bitmap, intensity, line, oval, point, polygon, rectangle, scaled intensity, text, waveform, X, XY, Y. |
| Data Type: | integer |
| LabWindows/CVICompatibility: | LabWindows/CVI 7.0 and later |

##### Values

| 0 | False |
| --- | --- |
| 1 | True |

<!--NI_TOPIC bundle=labwindows-cvi path=cvi/uiref/cviattrplotopacity.htm language=enus -->
## TOPIC 00752: ATTR_PLOT_OPACITY

- bundle_id: `labwindows-cvi`
- source_path: `cvi/uiref/cviattrplotopacity.htm`
- source_url: https://docs-be.ni.com/bundle/labwindows-cvi/raw/resource/enus/cvi/uiref/cviattrplotopacity.htm
- document_id: `labwindows-cvi`
- page_type: `leaf`
- content_type: ``

### ATTR_PLOT_OPACITY

| Type: | Plot attribute |
| --- | --- |
| Description: | The level of opacity for the plot on the graph, with 0 being full transparency and 255 being full opacity. You can specify the opacity for VAL_THIN_LINE and VAL_FAT_LINE. All other plot styles draw with opacity set to 255. For polygon plots, plots always draw with opacity set to 255 if the fill color is not transparent. |
| Plot Types: | Bitmap, intensity, line, polygon, rectangle, scaled intensity, waveform, X, XY, Y. |
| Data Type: | integer |
| Valid Range: | 0 to 255 |
| Default Value: | 255 |
| LabWindows/CVICompatibility: | LabWindows/CVI 2013 and later |

<!--NI_TOPIC bundle=labwindows-cvi path=cvi/uiref/cviattrplotsnappable.htm language=enus -->
## TOPIC 00753: ATTR_PLOT_SNAPPABLE

- bundle_id: `labwindows-cvi`
- source_path: `cvi/uiref/cviattrplotsnappable.htm`
- source_url: https://docs-be.ni.com/bundle/labwindows-cvi/raw/resource/enus/cvi/uiref/cviattrplotsnappable.htm
- document_id: `labwindows-cvi`
- page_type: `leaf`
- content_type: ``

### ATTR_PLOT_SNAPPABLE

| Type: | Plot attribute |
| --- | --- |
| Description: | Used to prevent graph cursors from snapping to a particular plot. By default, graph cursors for which the ATTR_CURSOR_MODE is VAL_SNAP_TO_POINT snap to the closest X, Y, XY, Waveform, Point and Polygon plot. If you want to prevent cursors from snapping to a certain plot, set ATTR_PLOT_SNAPPABLE for the plot to FALSE. 0 = Do not snap to this plot 1 = Snap to this plot |
| Plot Types: | Point, polygon, waveform, X, XY, Y. |
| Data Type: | integer |
| Default Value: | 1 |
| LabWindows/CVICompatibility: | LabWindows/CVI 4.0 and later |

##### Values

| 0 | False |
| --- | --- |
| 1 | True |

<!--NI_TOPIC bundle=labwindows-cvi path=cvi/uiref/cviattrplotstyle_trace.htm language=enus -->
## TOPIC 00754: ATTR_PLOT_STYLE (Trace)

- bundle_id: `labwindows-cvi`
- source_path: `cvi/uiref/cviattrplotstyle_trace.htm`
- source_url: https://docs-be.ni.com/bundle/labwindows-cvi/raw/resource/enus/cvi/uiref/cviattrplotstyle_trace.htm
- document_id: `labwindows-cvi`
- page_type: `leaf`
- content_type: ``

### ATTR_PLOT_STYLE (Trace)

| Type: | Trace attribute |
| --- | --- |
| Description: | The plot style for the trace on the strip chart. Note: When ATTR_ENABLE_ANTI_ALIASING is disabled, setting the plot style to VAL_FAT_LINE, VAL_FAT_STEP, VAL_VERTICAL_BAR, or VAL_BASE_ZERO_VERTICAL_BAR forces the line style to solid, regardless of the value of ATTR_LINE_STYLE. |
| Data Type: | integer |
| Default Value: | VAL_THIN_LINE |
| LabWindows/CVICompatibility: | LabWindows/CVI 3.0 and later |

##### Values

| VAL_THIN_LINE | A single thin line. |
| --- | --- |
| VAL_FAT_LINE | A fat line. (On the Windows platform, this plot style forces the line style to be VAL_SOLID). |
| VAL_CONNECTED_POINTS | A single thin line with asterisk characters at each plotted point. |
| VAL_SCATTER | Asterisk characters at each plotted point with no lines connecting each point. |
| VAL_THIN_STEP | A thin line stepping from one point to the next. |
| VAL_FAT_STEP | A fat line stepping from one point to the next. |
| VAL_VERTICAL_BAR | Vertical bars are plotted for each plotted point. The bars extend upward from the minimum value. |
| VAL_BASE_ZERO_VERTICAL_BAR | Vertical bars are plotted for each plotted point. The bars extend upward and downward from zero. |

<!--NI_TOPIC bundle=labwindows-cvi path=cvi/uiref/cviattrplotxdata.htm language=enus -->
## TOPIC 00755: ATTR_PLOT_XDATA

- bundle_id: `labwindows-cvi`
- source_path: `cvi/uiref/cviattrplotxdata.htm`
- source_url: https://docs-be.ni.com/bundle/labwindows-cvi/raw/resource/enus/cvi/uiref/cviattrplotxdata.htm
- document_id: `labwindows-cvi`
- page_type: `leaf`
- content_type: ``

### ATTR_PLOT_XDATA

| Type: | Plot attribute |
| --- | --- |
| Description: | Getting this value copies the X data of the plot into a pre-allocated buffer. Setting this value replaces the X data of the current plot with the buffer passed in. This buffer must be the same datatype and contain the same number of elements as the plot data it is replacing. |
| Plot Types: | Polygon, X, XY. |
| Data Type: | pointer |
| LabWindows/CVICompatibility: | LabWindows/CVI 4.0 and later |

<!--NI_TOPIC bundle=labwindows-cvi path=cvi/uiref/cviattrplotxdatatype.htm language=enus -->
## TOPIC 00756: ATTR_PLOT_XDATA_TYPE

- bundle_id: `labwindows-cvi`
- source_path: `cvi/uiref/cviattrplotxdatatype.htm`
- source_url: https://docs-be.ni.com/bundle/labwindows-cvi/raw/resource/enus/cvi/uiref/cviattrplotxdatatype.htm
- document_id: `labwindows-cvi`
- page_type: `leaf`
- content_type: ``

### ATTR_PLOT_XDATA_TYPE

| Type: | Plot attribute |
| --- | --- |
| Description: | The type of X data of the plot |
| Plot Types: | Polygon, X, XY. |
| Restrictions: | Not settable. |
| Data Type: | integer |
| LabWindows/CVICompatibility: | LabWindows/CVI 4.0 and later |

##### Values

| VAL_64BIT_INTEGER | An 8 byte integer. |
| --- | --- |
| VAL_UNSIGNED_64BIT_INTEGER | An unsigned 8 byte integer. |
| VAL_CHAR | A single byte character. |
| VAL_DOUBLE | An 8 byte floating point value. |
| VAL_FLOAT | A 4 byte floating point value. |
| VAL_INTEGER | A 4 byte integer. |
| VAL_SHORT_INTEGER | A 2 byte integer. |
| VAL_UNSIGNED_CHAR | An unsigned single byte character. |
| VAL_UNSIGNED_INTEGER | An unsigned 4 byte integer. |
| VAL_UNSIGNED_SHORT_INTEGER | An unsigned 2 byte integer. |
| VAL_SIZE_T | An unsigned 4 byte integer (32-bit applications). An unsigned 8 byte integer (64-bit applications). |
| VAL_SSIZE_T | A 4 byte integer (32-bit applications). An 8 byte integer (64-bit applications). |
| VAL_PTRDIFF_T | A 4 byte integer (32-bit applications). An 8 byte integer (64-bit applications). |
| VAL_UINTPTR_T | An unsigned 4 byte integer (32-bit applications). An unsigned 8 byte integer (64-bit applications). |
| VAL_INTPTR_T | A 4 byte integer (32-bit applications). An 8 byte integer (64-bit applications). |

<!--NI_TOPIC bundle=labwindows-cvi path=cvi/uiref/cviattrplotzdata.htm language=enus -->
## TOPIC 00757: ATTR_PLOT_ZDATA

- bundle_id: `labwindows-cvi`
- source_path: `cvi/uiref/cviattrplotzdata.htm`
- source_url: https://docs-be.ni.com/bundle/labwindows-cvi/raw/resource/enus/cvi/uiref/cviattrplotzdata.htm
- document_id: `labwindows-cvi`
- page_type: `leaf`
- content_type: ``

### ATTR_PLOT_ZDATA

| Type: | Plot attribute |
| --- | --- |
| Description: | Getting this value copies the Z data of the plot into a pre-allocated buffer. Setting this value replaces the Z data of the current plot with the buffer passed in. This buffer must be the same datatype and contain the same number of elements as the plot data it is replacing. |
| Plot Types: | Intensity, scaled intensity. |
| Data Type: | pointer |
| LabWindows/CVICompatibility: | LabWindows/CVI 4.0 and later |

<!--NI_TOPIC bundle=labwindows-cvi path=cvi/uiref/cviattrplotzdatatype.htm language=enus -->
## TOPIC 00758: ATTR_PLOT_ZDATA_TYPE

- bundle_id: `labwindows-cvi`
- source_path: `cvi/uiref/cviattrplotzdatatype.htm`
- source_url: https://docs-be.ni.com/bundle/labwindows-cvi/raw/resource/enus/cvi/uiref/cviattrplotzdatatype.htm
- document_id: `labwindows-cvi`
- page_type: `leaf`
- content_type: ``

### ATTR_PLOT_ZDATA_TYPE

| Type: | Plot attribute |
| --- | --- |
| Description: | The type of Z data of the plot |
| Plot Types: | Intensity, scaled intensity. |
| Restrictions: | Not settable. |
| Data Type: | integer |
| LabWindows/CVICompatibility: | LabWindows/CVI 4.0 and later |

##### Values

| VAL_64BIT_INTEGER | An 8 byte integer. |
| --- | --- |
| VAL_UNSIGNED_64BIT_INTEGER | An unsigned 8 byte integer. |
| VAL_CHAR | A single byte character. |
| VAL_DOUBLE | An 8 byte floating point value. |
| VAL_FLOAT | A 4 byte floating point value. |
| VAL_INTEGER | A 4 byte integer. |
| VAL_SHORT_INTEGER | A 2 byte integer. |
| VAL_UNSIGNED_CHAR | An unsigned single byte character. |
| VAL_UNSIGNED_INTEGER | An unsigned 4 byte integer. |
| VAL_UNSIGNED_SHORT_INTEGER | An unsigned 2 byte integer. |
| VAL_SIZE_T | An unsigned 4 byte integer (32-bit applications). An unsigned 8 byte integer (64-bit applications). |
| VAL_SSIZE_T | A 4 byte integer (32-bit applications). An 8 byte integer (64-bit applications). |
| VAL_PTRDIFF_T | A 4 byte integer (32-bit applications). An 8 byte integer (64-bit applications). |
| VAL_UINTPTR_T | An unsigned 4 byte integer (32-bit applications). An unsigned 8 byte integer (64-bit applications). |
| VAL_INTPTR_T | A 4 byte integer (32-bit applications). An 8 byte integer (64-bit applications). |

<!--NI_TOPIC bundle=labwindows-cvi path=cvi/uiref/cviattrpointsperscreen.htm language=enus -->
## TOPIC 00759: ATTR_POINTS_PER_SCREEN

- bundle_id: `labwindows-cvi`
- source_path: `cvi/uiref/cviattrpointsperscreen.htm`
- source_url: https://docs-be.ni.com/bundle/labwindows-cvi/raw/resource/enus/cvi/uiref/cviattrpointsperscreen.htm
- document_id: `labwindows-cvi`
- page_type: `leaf`
- content_type: ``

### ATTR_POINTS_PER_SCREEN

| Type: | Control attribute |
| --- | --- |
| Description: | The number of points that can fit into the strip chart plot area. |
| Control Types: | Strip charts. |
| Data Type: | integer |
| Valid Range: | 3 to 10000 |
| Default Value: | 100 |
| LabWindows/CVICompatibility: | LabWindows/CVI 3.0 and later |

<!--NI_TOPIC bundle=labwindows-cvi path=cvi/uiref/cviattrpopupstyle.htm language=enus -->
## TOPIC 00760: ATTR_POPUP_STYLE

- bundle_id: `labwindows-cvi`
- source_path: `cvi/uiref/cviattrpopupstyle.htm`
- source_url: https://docs-be.ni.com/bundle/labwindows-cvi/raw/resource/enus/cvi/uiref/cviattrpopupstyle.htm
- document_id: `labwindows-cvi`
- page_type: `leaf`
- content_type: ``

### ATTR_POPUP_STYLE

| Type: | System Pop-Ups attribute |
| --- | --- |
| Description: | Determines the style of control to use for system pop-up panels. |
| Data Type: | integer |
| Default Value: | VAL_LAB_STYLE |
| LabWindows/CVICompatibility: | LabWindows/CVI 6.0 and later |

##### Values

| VAL_CLASSIC | Use standard Windows style controls in system popups |
| --- | --- |
| VAL_LAB_STYLE | Use rendered controls in system popups |

<!--NI_TOPIC bundle=labwindows-cvi path=cvi/uiref/cviattrprecision_cell.htm language=enus -->
## TOPIC 00761: ATTR_PRECISION (Cell)

- bundle_id: `labwindows-cvi`
- source_path: `cvi/uiref/cviattrprecision_cell.htm`
- source_url: https://docs-be.ni.com/bundle/labwindows-cvi/raw/resource/enus/cvi/uiref/cviattrprecision_cell.htm
- document_id: `labwindows-cvi`
- page_type: `leaf`
- content_type: ``

### ATTR_PRECISION (Cell)

| Type: | Cell attribute |
| --- | --- |
| Description: | The number of places after the decimal point. |
| Data Type: | integer |
| Valid Range: | 0 to 32 |
| Default Value: | 2 |
| LabWindows/CVICompatibility: | LabWindows/CVI 5.5 and later |

<!--NI_TOPIC bundle=labwindows-cvi path=cvi/uiref/cviattrprecision_column.htm language=enus -->
## TOPIC 00762: ATTR_PRECISION (Column)

- bundle_id: `labwindows-cvi`
- source_path: `cvi/uiref/cviattrprecision_column.htm`
- source_url: https://docs-be.ni.com/bundle/labwindows-cvi/raw/resource/enus/cvi/uiref/cviattrprecision_column.htm
- document_id: `labwindows-cvi`
- page_type: `leaf`
- content_type: ``

### ATTR_PRECISION (Column)

| Type: | Column attribute |
| --- | --- |
| Description: | The number of places after the decimal point. |
| Data Type: | integer |
| Valid Range: | 0 to 32 |
| Default Value: | 2 |
| LabWindows/CVICompatibility: | LabWindows/CVI 5.5 and later |

<!--NI_TOPIC bundle=labwindows-cvi path=cvi/uiref/cviattrprecision_row.htm language=enus -->
## TOPIC 00763: ATTR_PRECISION (Row)

- bundle_id: `labwindows-cvi`
- source_path: `cvi/uiref/cviattrprecision_row.htm`
- source_url: https://docs-be.ni.com/bundle/labwindows-cvi/raw/resource/enus/cvi/uiref/cviattrprecision_row.htm
- document_id: `labwindows-cvi`
- page_type: `leaf`
- content_type: ``

### ATTR_PRECISION (Row)

| Type: | Row attribute |
| --- | --- |
| Description: | The number of places after the decimal point. |
| Data Type: | integer |
| Valid Range: | 0 to 32 |
| Default Value: | 2 |
| LabWindows/CVICompatibility: | LabWindows/CVI 5.5 and later |

<!--NI_TOPIC bundle=labwindows-cvi path=cvi/uiref/cviattrprimarymonitor.htm language=enus -->
## TOPIC 00764: ATTR_PRIMARY_MONITOR

- bundle_id: `labwindows-cvi`
- source_path: `cvi/uiref/cviattrprimarymonitor.htm`
- source_url: https://docs-be.ni.com/bundle/labwindows-cvi/raw/resource/enus/cvi/uiref/cviattrprimarymonitor.htm
- document_id: `labwindows-cvi`
- page_type: `leaf`
- content_type: ``

### ATTR_PRIMARY_MONITOR

| Type: | System attribute |
| --- | --- |
| Description: | The monitor ID for the primary monitor as determined by the system. |
| Restrictions: | Not settable. |
| Data Type: | integer |
| LabWindows/CVICompatibility: | LabWindows/CVI 5.5 and later |

<!--NI_TOPIC bundle=labwindows-cvi path=cvi/uiref/cviattrprintfontnamelength.htm language=enus -->
## TOPIC 00765: ATTR_PRINT_FONT_NAME_LENGTH

- bundle_id: `labwindows-cvi`
- source_path: `cvi/uiref/cviattrprintfontnamelength.htm`
- source_url: https://docs-be.ni.com/bundle/labwindows-cvi/raw/resource/enus/cvi/uiref/cviattrprintfontnamelength.htm
- document_id: `labwindows-cvi`
- page_type: `leaf`
- content_type: ``

### ATTR_PRINT_FONT_NAME_LENGTH

| Type: | Print attribute |
| --- | --- |
| Description: | Indicates the number of bytes in the current value of the font to use when printing. The length does not include the ASCII NUL byte. Use this value to determine the size of the buffer to pass when you call GetPrintAttribute and specify the ATTR_PRINT_FONT_NAME attribute. |
| Types of Printing: | Text. |
| Restrictions: | Not settable. |
| Data Type: | integer |
| LabWindows/CVICompatibility: | LabWindows/CVI 5.0 and later |

<!--NI_TOPIC bundle=labwindows-cvi path=cvi/uiref/cviattrprintpointsize.htm language=enus -->
## TOPIC 00766: ATTR_PRINT_POINT_SIZE

- bundle_id: `labwindows-cvi`
- source_path: `cvi/uiref/cviattrprintpointsize.htm`
- source_url: https://docs-be.ni.com/bundle/labwindows-cvi/raw/resource/enus/cvi/uiref/cviattrprintpointsize.htm
- document_id: `labwindows-cvi`
- page_type: `leaf`
- content_type: ``

### ATTR_PRINT_POINT_SIZE

| Type: | Print attribute |
| --- | --- |
| Description: | Specifies the size of the font to use when printing a text file or buffer. |
| Types of Printing: | Text. |
| Data Type: | integer |
| Valid Range: | 6 to 48 |
| Default Value: | 13 |
| LabWindows/CVICompatibility: | LabWindows/CVI 5.0 and later |

<!--NI_TOPIC bundle=labwindows-cvi path=cvi/uiref/cviattrrightactualrange.htm language=enus -->
## TOPIC 00767: ATTR_RIGHT_ACTUAL_RANGE

- bundle_id: `labwindows-cvi`
- source_path: `cvi/uiref/cviattrrightactualrange.htm`
- source_url: https://docs-be.ni.com/bundle/labwindows-cvi/raw/resource/enus/cvi/uiref/cviattrrightactualrange.htm
- document_id: `labwindows-cvi`
- page_type: `leaf`
- content_type: ``

### ATTR_RIGHT_ACTUAL_RANGE

| Type: | Control attribute |
| --- | --- |
| Description: | Use this attribute to obtain the effective rightmost range of the splitter control. Several factors determine this value, such as the setting of the ATTR_RIGHT_RANGE attribute, the size of the panel, the type, size, and position of controls you have attached to the top edge of the splitter, and in what mode they are attached. |
| Control Types: | Splitters. |
| Restrictions: | Not settable. Not valid for horizontal splitters |
| Data Type: | integer |
| Valid Range: | -32768 to 32767 |
| LabWindows/CVICompatibility: | LabWindows/CVI 7.1 and later |

<!--NI_TOPIC bundle=labwindows-cvi path=cvi/uiref/cviattrrightrange.htm language=enus -->
## TOPIC 00768: ATTR_RIGHT_RANGE

- bundle_id: `labwindows-cvi`
- source_path: `cvi/uiref/cviattrrightrange.htm`
- source_url: https://docs-be.ni.com/bundle/labwindows-cvi/raw/resource/enus/cvi/uiref/cviattrrightrange.htm
- document_id: `labwindows-cvi`
- page_type: `leaf`
- content_type: ``

### ATTR_RIGHT_RANGE

| Type: | Control attribute |
| --- | --- |
| Description: | This is one of four attributes that define the range of motion of the splitter control. You can allow LabWindows/CVI to automatically set this range using the rules below, or you can define your own range. You can also choose to not enforce a range by setting the attribute to VAL_NO_RANGE_LIMIT. The default range rules are as follows: the splitter control can be moved up to the point where the far edge of any attached controls or panels that are attached in "move" mode would reach the far edge of the panel, or up to the point where the splitter itself would reach the panel edge, whichever comes first. Regardless of whether you use the default range, or set your own range, splitters cannot be moved past the point where any control or panel that is attached to the splitter in "size" mode is reduced to its standard minimum size (this varies according to control type). You specify values for this attribute using panel coordinates, relative to the top/left corner of the panel. |
| Control Types: | Splitters. |
| Restrictions: | Not valid for horizontal splitters |
| Data Type: | integer |
| Valid Range: | -32768 to 32767, or VAL_AUTO_RANGE, or VAL_NO_RANGE_LIMIT |
| Default Value: | VAL_AUTO_RANGE |
| LabWindows/CVICompatibility: | LabWindows/CVI 7.1 and later |

##### Values

| VAL_AUTO_RANGE | Set this value to allow LabWindows/CVI to automatically determine the range of motion of splitter controls. |
| --- | --- |
| VAL_NO_RANGE_LIMIT | Set this value if you don't want LabWindows/CVI to impose a range of motion on splitter controls. Note: even if you set this value, you cannot move splitters past the point where any control or panel that is attached to the splitter in "size" mode is reduced to its standard minimum size (this varies according to control type) |

<!--NI_TOPIC bundle=labwindows-cvi path=cvi/uiref/cviattrringarrowlocation_cell.htm language=enus -->
## TOPIC 00769: ATTR_RING_ARROW_LOCATION (Cell)

- bundle_id: `labwindows-cvi`
- source_path: `cvi/uiref/cviattrringarrowlocation_cell.htm`
- source_url: https://docs-be.ni.com/bundle/labwindows-cvi/raw/resource/enus/cvi/uiref/cviattrringarrowlocation_cell.htm
- document_id: `labwindows-cvi`
- page_type: `leaf`
- content_type: ``

### ATTR_RING_ARROW_LOCATION (Cell)

| Type: | Cell attribute |
| --- | --- |
| Description: | Determines whether the pull-down arrow of ring and combo box cells is on the left edge of the cell, or the right edge of the cell. |
| Data Type: | integer |
| Default Value: | VAL_RIGHT_ANCHOR |
| LabWindows/CVICompatibility: | LabWindows/CVI 8.0 and later |

##### Values

| VAL_LEFT_ANCHOR | Place the pull-down arrow on the left edge of the cell |
| --- | --- |
| VAL_RIGHT_ANCHOR | Place the pull-down arrow on the right edge of the cell |

<!--NI_TOPIC bundle=labwindows-cvi path=cvi/uiref/cviattrringarrowlocation_column.htm language=enus -->
## TOPIC 00770: ATTR_RING_ARROW_LOCATION (Column)

- bundle_id: `labwindows-cvi`
- source_path: `cvi/uiref/cviattrringarrowlocation_column.htm`
- source_url: https://docs-be.ni.com/bundle/labwindows-cvi/raw/resource/enus/cvi/uiref/cviattrringarrowlocation_column.htm
- document_id: `labwindows-cvi`
- page_type: `leaf`
- content_type: ``

### ATTR_RING_ARROW_LOCATION (Column)

| Type: | Column attribute |
| --- | --- |
| Description: | Determines whether the pull-down arrow of ring and combo box cells is on the left edge of the cell, or the right edge of the cell. |
| Data Type: | integer |
| Default Value: | VAL_RIGHT_ANCHOR |
| LabWindows/CVICompatibility: | LabWindows/CVI 8.0 and later |

##### Values

| VAL_LEFT_ANCHOR | Place the pull-down arrow on the left edge of the cell |
| --- | --- |
| VAL_RIGHT_ANCHOR | Place the pull-down arrow on the right edge of the cell |

<!--NI_TOPIC bundle=labwindows-cvi path=cvi/uiref/cviattrringarrowlocation_control.htm language=enus -->
## TOPIC 00771: ATTR_RING_ARROW_LOCATION (Control)

- bundle_id: `labwindows-cvi`
- source_path: `cvi/uiref/cviattrringarrowlocation_control.htm`
- source_url: https://docs-be.ni.com/bundle/labwindows-cvi/raw/resource/enus/cvi/uiref/cviattrringarrowlocation_control.htm
- document_id: `labwindows-cvi`
- page_type: `leaf`
- content_type: ``

### ATTR_RING_ARROW_LOCATION (Control)

| Type: | Control attribute |
| --- | --- |
| Description: | Determines whether the pull-down arrow of ring and combo box cells is on the left edge of the cell, or the right edge of the cell, when ATTR_TABLE_MODE is set to VAL_GRID. |
| Control Types: | Tables. |
| Data Type: | integer |
| Default Value: | VAL_RIGHT_ANCHOR |
| LabWindows/CVICompatibility: | LabWindows/CVI 8.0 and later |

##### Values

| VAL_LEFT_ANCHOR | Place the pull-down arrow on the left edge of the cell |
| --- | --- |
| VAL_RIGHT_ANCHOR | Place the pull-down arrow on the right edge of the cell |

<!--NI_TOPIC bundle=labwindows-cvi path=cvi/uiref/cviattrringarrowlocation_row.htm language=enus -->
## TOPIC 00772: ATTR_RING_ARROW_LOCATION (Row)

- bundle_id: `labwindows-cvi`
- source_path: `cvi/uiref/cviattrringarrowlocation_row.htm`
- source_url: https://docs-be.ni.com/bundle/labwindows-cvi/raw/resource/enus/cvi/uiref/cviattrringarrowlocation_row.htm
- document_id: `labwindows-cvi`
- page_type: `leaf`
- content_type: ``

### ATTR_RING_ARROW_LOCATION (Row)

| Type: | Row attribute |
| --- | --- |
| Description: | Determines whether the pull-down arrow of ring and combo box cells is on the left edge of the cell, or the right edge of the cell. |
| Data Type: | integer |
| Default Value: | VAL_RIGHT_ANCHOR |
| LabWindows/CVICompatibility: | LabWindows/CVI 8.0 and later |

##### Values

| VAL_LEFT_ANCHOR | Place the pull-down arrow on the left edge of the cell |
| --- | --- |
| VAL_RIGHT_ANCHOR | Place the pull-down arrow on the right edge of the cell |

<!--NI_TOPIC bundle=labwindows-cvi path=cvi/uiref/cviattrringitemsunique_row.htm language=enus -->
## TOPIC 00773: ATTR_RING_ITEMS_UNIQUE (Row)

- bundle_id: `labwindows-cvi`
- source_path: `cvi/uiref/cviattrringitemsunique_row.htm`
- source_url: https://docs-be.ni.com/bundle/labwindows-cvi/raw/resource/enus/cvi/uiref/cviattrringitemsunique_row.htm
- document_id: `labwindows-cvi`
- page_type: `leaf`
- content_type: ``

### ATTR_RING_ITEMS_UNIQUE (Row)

| Type: | Row attribute |
| --- | --- |
| Description: | When enabled, the values in the item list of a ring or combo box cell must be unique. |
| Data Type: | integer |
| Default Value: | 1 |
| LabWindows/CVICompatibility: | LabWindows/CVI 8.0 and later |

##### Values

| 0 | False |
| --- | --- |
| 1 | True |

<!--NI_TOPIC bundle=labwindows-cvi path=cvi/uiref/cviattrrowactualheight.htm language=enus -->
## TOPIC 00774: ATTR_ROW_ACTUAL_HEIGHT

- bundle_id: `labwindows-cvi`
- source_path: `cvi/uiref/cviattrrowactualheight.htm`
- source_url: https://docs-be.ni.com/bundle/labwindows-cvi/raw/resource/enus/cvi/uiref/cviattrrowactualheight.htm
- document_id: `labwindows-cvi`
- page_type: `leaf`
- content_type: ``

### ATTR_ROW_ACTUAL_HEIGHT

| Type: | Row attribute |
| --- | --- |
| Description: | The actual height of the row in pixels, resulting from the calculations performed as a consequence of the value of ATTR_SIZE_MODE. |
| Restrictions: | Not settable. |
| Data Type: | integer |
| LabWindows/CVICompatibility: | LabWindows/CVI 5.5 and later |

<!--NI_TOPIC bundle=labwindows-cvi path=cvi/uiref/cviattrrowheight.htm language=enus -->
## TOPIC 00775: ATTR_ROW_HEIGHT

- bundle_id: `labwindows-cvi`
- source_path: `cvi/uiref/cviattrrowheight.htm`
- source_url: https://docs-be.ni.com/bundle/labwindows-cvi/raw/resource/enus/cvi/uiref/cviattrrowheight.htm
- document_id: `labwindows-cvi`
- page_type: `leaf`
- content_type: ``

### ATTR_ROW_HEIGHT

| Type: | Row attribute |
| --- | --- |
| Description: | When you set the row height manually, this attribute determines the height of the row in pixels. This value is used only if you set ATTR_SIZE_MODE to VAL_USE_EXPLICIT_SIZE. Use ATTR_ROW_ACTUAL_HEIGHT to obtain the resulting height of the row. |
| Data Type: | integer |
| Valid Range: | 1 to 32767 |
| Default Value: | 25 |
| LabWindows/CVICompatibility: | LabWindows/CVI 5.5 and later |

<!--NI_TOPIC bundle=labwindows-cvi path=cvi/uiref/cviattrrowlabelswidth.htm language=enus -->
## TOPIC 00776: ATTR_ROW_LABELS_WIDTH

- bundle_id: `labwindows-cvi`
- source_path: `cvi/uiref/cviattrrowlabelswidth.htm`
- source_url: https://docs-be.ni.com/bundle/labwindows-cvi/raw/resource/enus/cvi/uiref/cviattrrowlabelswidth.htm
- document_id: `labwindows-cvi`
- page_type: `leaf`
- content_type: ``

### ATTR_ROW_LABELS_WIDTH

| Type: | Control attribute |
| --- | --- |
| Description: | The width in pixels of the column of row labels on the table. |
| Control Types: | Tables. |
| Data Type: | integer |
| Valid Range: | 0 to 32767 |
| Default Value: | 40 |
| LabWindows/CVICompatibility: | LabWindows/CVI 5.5 and later |

<!--NI_TOPIC bundle=labwindows-cvi path=cvi/uiref/cviattrrowoffset.htm language=enus -->
## TOPIC 00777: ATTR_ROW_OFFSET

- bundle_id: `labwindows-cvi`
- source_path: `cvi/uiref/cviattrrowoffset.htm`
- source_url: https://docs-be.ni.com/bundle/labwindows-cvi/raw/resource/enus/cvi/uiref/cviattrrowoffset.htm
- document_id: `labwindows-cvi`
- page_type: `leaf`
- content_type: ``

### ATTR_ROW_OFFSET

| Type: | Control attribute |
| --- | --- |
| Description: | A constant offset to add to the row indices. |
| Control Types: | Tables. |
| Data Type: | integer |
| Valid Range: | -2147483648 to 1000000000 |
| Default Value: | 0 |
| LabWindows/CVICompatibility: | LabWindows/CVI 2013 and later |

<!--NI_TOPIC bundle=labwindows-cvi path=cvi/uiref/cviattrrowvisible.htm language=enus -->
## TOPIC 00778: ATTR_ROW_VISIBLE

- bundle_id: `labwindows-cvi`
- source_path: `cvi/uiref/cviattrrowvisible.htm`
- source_url: https://docs-be.ni.com/bundle/labwindows-cvi/raw/resource/enus/cvi/uiref/cviattrrowvisible.htm
- document_id: `labwindows-cvi`
- page_type: `leaf`
- content_type: ``

### ATTR_ROW_VISIBLE

| Type: | Row attribute |
| --- | --- |
| Description: | Determines whether the row is visible. Cells in invisible rows cannot be made active, but they can be included as part of cell selections. 0 = Not visible 1 = Visible |
| Data Type: | integer |
| Default Value: | 1 |
| LabWindows/CVICompatibility: | LabWindows/CVI 2012 and later |

##### Values

| 0 | False |
| --- | --- |
| 1 | True |

<!--NI_TOPIC bundle=labwindows-cvi path=cvi/uiref/cviattrscalecontentsonresize.htm language=enus -->
## TOPIC 00779: ATTR_SCALE_CONTENTS_ON_RESIZE

- bundle_id: `labwindows-cvi`
- source_path: `cvi/uiref/cviattrscalecontentsonresize.htm`
- source_url: https://docs-be.ni.com/bundle/labwindows-cvi/raw/resource/enus/cvi/uiref/cviattrscalecontentsonresize.htm
- document_id: `labwindows-cvi`
- page_type: `leaf`
- content_type: ``

### ATTR_SCALE_CONTENTS_ON_RESIZE

| Type: | Panel attribute |
| --- | --- |
| Description: | Specifies whether the contents are scaled when the panel is resized. This applies to programmatic resizing, resizing in the User Interface Editor, and resizing by the end-user. 0 = Disabled 1 = Enabled |
| Data Type: | integer |
| Default Value: | 0 |
| LabWindows/CVICompatibility: | LabWindows/CVI 5.0 and later |

##### Values

| 0 | False |
| --- | --- |
| 1 | True |

<!--NI_TOPIC bundle=labwindows-cvi path=cvi/uiref/cviattrscrollbarcolor_control.htm language=enus -->
## TOPIC 00780: ATTR_SCROLL_BAR_COLOR (Control)

- bundle_id: `labwindows-cvi`
- source_path: `cvi/uiref/cviattrscrollbarcolor_control.htm`
- source_url: https://docs-be.ni.com/bundle/labwindows-cvi/raw/resource/enus/cvi/uiref/cviattrscrollbarcolor_control.htm
- document_id: `labwindows-cvi`
- page_type: `leaf`
- content_type: ``

### ATTR_SCROLL_BAR_COLOR (Control)

| Type: | Control attribute |
| --- | --- |
| Description: | The RGB color value of the scroll bar. LabWindows/CVI ignores this attribute if you enable the ATTR_CONFORM_TO_SYSTEM_THEME attribute, enable the Use Windows Visual Styles for Controls option, or disable the ATTR_DISABLE_PANEL_THEME attribute. An RGB value is a 4-byte integer with the hexadecimal format 0x00RRGGBB. RR, GG, and BB are the respective red, green, and blue components of the color value. See MakeColor. |
| Control Types: | List boxes, tables, text boxes, trees. |
| Data Type: | integer |
| LabWindows/CVICompatibility: | LabWindows/CVI 3.0 and later |

##### Values

| VAL_RED | Red = 255, Green = 0, Blue = 0 |
| --- | --- |
| VAL_GREEN | Red = 0, Green = 255, Blue = 0 |
| VAL_BLUE | Red = 0, Green = 0, Blue = 255 |
| VAL_CYAN | Red = 0, Green = 255, Blue = 255 |
| VAL_MAGENTA | Red = 255, Green = 0, Blue = 255 |
| VAL_YELLOW | Red = 255, Green = 255, Blue = 0 |
| VAL_DK_RED | Red = 128, Green = 0, Blue = 0 |
| VAL_DK_BLUE | Red = 0, Green = 0, Blue = 128 |
| VAL_DK_GREEN | Red = 0, Green = 128, Blue = 0 |
| VAL_DK_CYAN | Red = 0, Green = 128, Blue = 128 |
| VAL_DK_MAGENTA | Red = 128, Green = 0, Blue = 128 |
| VAL_DK_YELLOW | Red = 128, Green = 128, Blue = 0 |
| VAL_LT_GRAY | Red = 192, Green = 192, Blue = 192 |
| VAL_DK_GRAY | Red = 128, Green = 128, Blue = 128 |
| VAL_BLACK | Red = 0, Green = 0, Blue = 0 |
| VAL_WHITE | Red = 255, Green = 255, Blue = 255 |
| VAL_GRAY | Red = 160, Green = 160, Blue = 160 |
| VAL_OFFWHITE | Red = 224, Green = 224, Blue = 224 |
| VAL_TRANSPARENT | Red = 0, Green = 0, Blue = 0, transparent bit set. |
| VAL_PANEL_GRAY | Red = 192, Green = 192, Blue = 192 |

<!--NI_TOPIC bundle=labwindows-cvi path=cvi/uiref/cviattrscrollbarcolor_panel.htm language=enus -->
## TOPIC 00781: ATTR_SCROLL_BAR_COLOR (Panel)

- bundle_id: `labwindows-cvi`
- source_path: `cvi/uiref/cviattrscrollbarcolor_panel.htm`
- source_url: https://docs-be.ni.com/bundle/labwindows-cvi/raw/resource/enus/cvi/uiref/cviattrscrollbarcolor_panel.htm
- document_id: `labwindows-cvi`
- page_type: `leaf`
- content_type: ``

### ATTR_SCROLL_BAR_COLOR (Panel)

| Type: | Panel attribute |
| --- | --- |
| Description: | The RGB color value of the panel scroll bars. LabWindows/CVI ignores this attribute if you enable the ATTR_CONFORM_TO_SYSTEM_THEME attribute, enable the Use Windows Visual Styles for Controls option, or disable the ATTR_DISABLE_PANEL_THEME attribute. An RGB value is a 4-byte integer with the hexadecimal format 0x00RRGGBB. RR, GG, and BB are the respective red, green, and blue components of the color value. See MakeColor. |
| Data Type: | integer |
| LabWindows/CVICompatibility: | LabWindows/CVI 3.0 and later |

##### Values

| VAL_RED | Red = 255, Green = 0, Blue = 0 |
| --- | --- |
| VAL_GREEN | Red = 0, Green = 255, Blue = 0 |
| VAL_BLUE | Red = 0, Green = 0, Blue = 255 |
| VAL_CYAN | Red = 0, Green = 255, Blue = 255 |
| VAL_MAGENTA | Red = 255, Green = 0, Blue = 255 |
| VAL_YELLOW | Red = 255, Green = 255, Blue = 0 |
| VAL_DK_RED | Red = 128, Green = 0, Blue = 0 |
| VAL_DK_BLUE | Red = 0, Green = 0, Blue = 128 |
| VAL_DK_GREEN | Red = 0, Green = 128, Blue = 0 |
| VAL_DK_CYAN | Red = 0, Green = 128, Blue = 128 |
| VAL_DK_MAGENTA | Red = 128, Green = 0, Blue = 128 |
| VAL_DK_YELLOW | Red = 128, Green = 128, Blue = 0 |
| VAL_LT_GRAY | Red = 192, Green = 192, Blue = 192 |
| VAL_DK_GRAY | Red = 128, Green = 128, Blue = 128 |
| VAL_BLACK | Red = 0, Green = 0, Blue = 0 |
| VAL_WHITE | Red = 255, Green = 255, Blue = 255 |
| VAL_GRAY | Red = 160, Green = 160, Blue = 160 |
| VAL_OFFWHITE | Red = 224, Green = 224, Blue = 224 |
| VAL_TRANSPARENT | Red = 0, Green = 0, Blue = 0, transparent bit set. |
| VAL_PANEL_GRAY | Red = 192, Green = 192, Blue = 192 |

<!--NI_TOPIC bundle=labwindows-cvi path=cvi/uiref/cviattrscrollbars_control.htm language=enus -->
## TOPIC 00782: ATTR_SCROLL_BARS (Control)

- bundle_id: `labwindows-cvi`
- source_path: `cvi/uiref/cviattrscrollbars_control.htm`
- source_url: https://docs-be.ni.com/bundle/labwindows-cvi/raw/resource/enus/cvi/uiref/cviattrscrollbars_control.htm
- document_id: `labwindows-cvi`
- page_type: `leaf`
- content_type: ``

### ATTR_SCROLL_BARS (Control)

| Type: | Control attribute |
| --- | --- |
| Description: | Specifies whether vertical and/or horizontal scroll bars are shown on the control. (Horizontal scroll bars not valid for list boxes) |
| Control Types: | List boxes, tables, text boxes, trees. |
| Data Type: | integer |
| Default Value: | VAL_NO_SCROLL_BARS (text boxes), VAL_VERT_SCROLL_BAR (list boxes), VAL_BOTH_SCROLL_BARS (tables and trees) |
| LabWindows/CVICompatibility: | LabWindows/CVI 3.0 and later |

##### Values

| VAL_NO_SCROLL_BARS |  |
| --- | --- |
| VAL_HORIZ_SCROLL_BAR | Not valid for list boxes. |
| VAL_VERT_SCROLL_BAR |  |
| VAL_BOTH_SCROLL_BARS | Not valid for list boxes. |

<!--NI_TOPIC bundle=labwindows-cvi path=cvi/uiref/cviattrscrollbarsize_control.htm language=enus -->
## TOPIC 00783: ATTR_SCROLL_BAR_SIZE (Control)

- bundle_id: `labwindows-cvi`
- source_path: `cvi/uiref/cviattrscrollbarsize_control.htm`
- source_url: https://docs-be.ni.com/bundle/labwindows-cvi/raw/resource/enus/cvi/uiref/cviattrscrollbarsize_control.htm
- document_id: `labwindows-cvi`
- page_type: `leaf`
- content_type: ``

### ATTR_SCROLL_BAR_SIZE (Control)

| Type: | Control attribute |
| --- | --- |
| Description: | Specifies the size (width) of the scroll bars, in pixels. Defined values for setting the size are VAL_SMALL_SCROLL_BARS (8 pixels), VAL_MEDIUM_SCROLL_BARS (12 pixels), and VAL_LARGE_SCROLL_BARS (16 pixels). |
| Control Types: | List boxes, tables, text boxes, trees. |
| Data Type: | integer |
| Valid Range: | 8 to 32767 |
| Default Value: | VAL_LARGE_SCROLL_BARS |
| LabWindows/CVICompatibility: | LabWindows/CVI 3.0 and later |

##### Values

| VAL_MEDIUM_SCROLL_BARS | Medium-sized scroll bars that contain up and down arrows. |
| --- | --- |
| VAL_SMALL_SCROLL_BARS | Small scroll bars that contain up and down boxes instead of up and down arrows. |
| VAL_LARGE_SCROLL_BARS | Large scroll bars that contain up and down arrows. |

<!--NI_TOPIC bundle=labwindows-cvi path=cvi/uiref/cviattrscrollbarsize_panel.htm language=enus -->
## TOPIC 00784: ATTR_SCROLL_BAR_SIZE (Panel)

- bundle_id: `labwindows-cvi`
- source_path: `cvi/uiref/cviattrscrollbarsize_panel.htm`
- source_url: https://docs-be.ni.com/bundle/labwindows-cvi/raw/resource/enus/cvi/uiref/cviattrscrollbarsize_panel.htm
- document_id: `labwindows-cvi`
- page_type: `leaf`
- content_type: ``

### ATTR_SCROLL_BAR_SIZE (Panel)

| Type: | Panel attribute |
| --- | --- |
| Description: | Specifies the size (width) of the scroll bars, in pixels. Defined values for setting the size are VAL_SMALL_SCROLL_BARS (8 pixels), VAL_MEDIUM_SCROLL_BARS (12 pixels), and VAL_LARGE_SCROLL_BARS (16 pixels). |
| Data Type: | integer |
| Valid Range: | 8 to 32767 |
| Default Value: | VAL_LARGE_SCROLL_BARS |
| LabWindows/CVICompatibility: | LabWindows/CVI 3.0 and later |

##### Values

| VAL_MEDIUM_SCROLL_BARS | Medium-sized scroll bars that contain up and down arrows. |
| --- | --- |
| VAL_SMALL_SCROLL_BARS | Small scroll bars that contain up and down boxes instead of up and down arrows. |
| VAL_LARGE_SCROLL_BARS | Large scroll bars that contain up and down arrows. |

<!--NI_TOPIC bundle=labwindows-cvi path=cvi/uiref/cviattrscrollbarstyle.htm language=enus -->
## TOPIC 00785: ATTR_SCROLL_BAR_STYLE

- bundle_id: `labwindows-cvi`
- source_path: `cvi/uiref/cviattrscrollbarstyle.htm`
- source_url: https://docs-be.ni.com/bundle/labwindows-cvi/raw/resource/enus/cvi/uiref/cviattrscrollbarstyle.htm
- document_id: `labwindows-cvi`
- page_type: `leaf`
- content_type: ``

### ATTR_SCROLL_BAR_STYLE

| Type: | Panel attribute |
| --- | --- |
| Description: | The style of the scroll bars used for the panel. |
| Data Type: | integer |
| Default Value: | VAL_CLASSIC |
| LabWindows/CVICompatibility: | LabWindows/CVI 6.0 and later |

##### Values

| VAL_CLASSIC | Use standard Windows scroll bars. |
| --- | --- |
| VAL_LAB_STYLE | Use rendered scroll bars. |

<!--NI_TOPIC bundle=labwindows-cvi path=cvi/uiref/cviattrscrollmode.htm language=enus -->
## TOPIC 00786: ATTR_SCROLL_MODE

- bundle_id: `labwindows-cvi`
- source_path: `cvi/uiref/cviattrscrollmode.htm`
- source_url: https://docs-be.ni.com/bundle/labwindows-cvi/raw/resource/enus/cvi/uiref/cviattrscrollmode.htm
- document_id: `labwindows-cvi`
- page_type: `leaf`
- content_type: ``

### ATTR_SCROLL_MODE

| Type: | Control attribute |
| --- | --- |
| Description: | The scrolling mode of the strip chart. |
| Control Types: | Strip charts. |
| Data Type: | integer |
| Default Value: | VAL_CONTINUOUS |
| LabWindows/CVICompatibility: | LabWindows/CVI 3.0 and later |

##### Values

| VAL_SWEEP | Allow new data to overwrite old data as it wraps past the right and starts over on the left. |
| --- | --- |
| VAL_CONTINUOUS | Scroll data off the left edge of the plot area as new data appears on the right. |
| VAL_BLOCK | Erase the entire plot when the data reaches the right edge. |

<!--NI_TOPIC bundle=labwindows-cvi path=cvi/uiref/cviattrselected.htm language=enus -->
## TOPIC 00787: ATTR_SELECTED

- bundle_id: `labwindows-cvi`
- source_path: `cvi/uiref/cviattrselected.htm`
- source_url: https://docs-be.ni.com/bundle/labwindows-cvi/raw/resource/enus/cvi/uiref/cviattrselected.htm
- document_id: `labwindows-cvi`
- page_type: `leaf`
- content_type: ``

### ATTR_SELECTED

| Type: | Tree Item attribute |
| --- | --- |
| Description: | Specifies whether the tree item is selected. This attribute is only settable when the tree selection mode is VAL_SELECTION_MULTIPLE. If the selection mode is VAL_SELECTION_SINGLE, the active item is always the only item selected. If the selection mode is VAL_SELECTION_NONE, there are never any selected items. |
| Data Type: | integer |
| Default Value: | 0 |
| LabWindows/CVICompatibility: | LabWindows/CVI 7.0 and later |

##### Values

| 0 | False |
| --- | --- |
| 1 | True |

<!--NI_TOPIC bundle=labwindows-cvi path=cvi/uiref/cviattrselectionmode.htm language=enus -->
## TOPIC 00788: ATTR_SELECTION_MODE

- bundle_id: `labwindows-cvi`
- source_path: `cvi/uiref/cviattrselectionmode.htm`
- source_url: https://docs-be.ni.com/bundle/labwindows-cvi/raw/resource/enus/cvi/uiref/cviattrselectionmode.htm
- document_id: `labwindows-cvi`
- page_type: `leaf`
- content_type: ``

### ATTR_SELECTION_MODE

| Type: | Control attribute |
| --- | --- |
| Description: | Determines how many tree items can be selected. |
| Control Types: | Trees. |
| Data Type: | integer |
| Default Value: | VAL_SELECTION_MULTIPLE |
| LabWindows/CVICompatibility: | LabWindows/CVI 7.0 and later |

##### Values

| VAL_SELECTION_NONE | No tree items can be selected. |
| --- | --- |
| VAL_SELECTION_SINGLE | The active tree item is always selected, and no other tree item can be selected. |
| VAL_SELECTION_MULTIPLE | Any number of tree items can be selected. |

<!--NI_TOPIC bundle=labwindows-cvi path=cvi/uiref/cviattrsenddimmereventsforallkeys.htm language=enus -->
## TOPIC 00789: ATTR_SEND_DIMMER_EVENTS_FOR_ALL_KEYS

- bundle_id: `labwindows-cvi`
- source_path: `cvi/uiref/cviattrsenddimmereventsforallkeys.htm`
- source_url: https://docs-be.ni.com/bundle/labwindows-cvi/raw/resource/enus/cvi/uiref/cviattrsenddimmereventsforallkeys.htm
- document_id: `labwindows-cvi`
- page_type: `leaf`
- content_type: ``

### ATTR_SEND_DIMMER_EVENTS_FOR_ALL_KEYS

| Type: | Menu attribute |
| --- | --- |
| Description: | When enabled, this attribute forces your menu dimmer callbacks to be called whenever a valid shortcut key is pressed on the panel, regardless of whether the key is assigned to a particular menu item. 0 = Enabled only for shortcut keys assigned to a menu item 1 = Enabled for all valid shortcut keys |
| Menu Objects: | Menu Bars. |
| Data Type: | integer |
| Default Value: | 0 |
| LabWindows/CVICompatibility: | LabWindows/CVI 7.0 and later |

##### Values

| 0 | False |
| --- | --- |
| 1 | True |

<!--NI_TOPIC bundle=labwindows-cvi path=cvi/uiref/cviattrtextfont_cell.htm language=enus -->
## TOPIC 00790: ATTR_TEXT_FONT (Cell)

- bundle_id: `labwindows-cvi`
- source_path: `cvi/uiref/cviattrtextfont_cell.htm`
- source_url: https://docs-be.ni.com/bundle/labwindows-cvi/raw/resource/enus/cvi/uiref/cviattrtextfont_cell.htm
- document_id: `labwindows-cvi`
- page_type: `leaf`
- content_type: ``

### ATTR_TEXT_FONT (Cell)

| Type: | Cell attribute |
| --- | --- |
| Description: | The name of the font for the table cell text. To determine the size of the buffer to pass when you are obtaining the font name, call GetTableCellAttribute and specify the ATTR_TEXT_FONT_NAME_LENGTH attribute. You can use a LabWindows/CVI-supplied font; any host font—such as Arial or Courier—supported on your system; or a user-defined metafont saved by a previous call to functions such as CreateMetaFont and CreateMetaFontEx. Note: LabWindows/CVI returns an error if you use a metafont that specifies an angle for the text. Always set the font before setting the size or style. |
| Data Type: | string |
| Default Value: | VAL_DIALOG_META_FONT |
| LabWindows/CVICompatibility: | LabWindows/CVI 5.5 and later |

##### Values

| VAL_MENU_FONT | Default font style for LabWindows/CVI menus. This font contains typeface information only. This value is an alias to an operating system font. Therefore, the operating system and user preferences on your machine determine this font style. |
| --- | --- |
| VAL_DIALOG_FONT | Default font style for LabWindows/CVI dialog boxes and control text. This font contains typeface information only. This value is an alias to an operating system font. Therefore, the operating system and user preferences on your machine determine this font style. |
| VAL_EDITOR_FONT | Default font style for the LabWindows/CVI Source window. This font contains typeface information only. This value is an alias to an operating system font. Therefore, the operating system and user preferences on your machine determine this font style. |
| VAL_APP_FONT | Default font style for the LabWindows/CVI Workspace window. This font contains typeface information only. This value is an alias to an operating system font. Therefore, the operating system and user preferences on your machine determine this font style. |
| VAL_MESSAGE_BOX_FONT | Default font style for LabWindows/CVI message boxes. This font contains typeface information only. This value is an alias to an operating system font. Therefore, the operating system and user preferences on your machine determine this font style. |
| VAL_MENU_META_FONT | Default font for LabWindows/CVI menus. Metafonts contain typeface information, point size, and text styles such as bold, shadow outline, underline, italics, and strikeout. Because metafonts contain character size information, strings that use metafonts are more likely to have the same width across platforms. This value is an alias to an operating system font. Therefore, the operating system and user preferences on your machine determine this font. |
| VAL_DIALOG_META_FONT | Default font for LabWindows/CVI dialog boxes and control text. Metafonts contain typeface information, point size, and text styles such as bold, shadow outline, underline, italics, and strikeout. Because metafonts contain character size information, strings that use metafonts are more likely to have the same width across platforms. This value is an alias to an operating system font. Therefore, the operating system and user preferences on your machine determine this font. |
| VAL_EDITOR_META_FONT | Default font for the LabWindows/CVI Source window. Metafonts contain typeface information, point size, and text styles such as bold, shadow outline, underline, italics, and strikeout. Because metafonts contain character size information, strings that use metafonts are more likely to have the same width across platforms. This value is an alias to an operating system font. Therefore, the operating system and user preferences on your machine determine this font. |
| VAL_APP_META_FONT | Default font for the LabWindows/CVI Workspace window. Metafonts contain typeface information, point size, and text styles such as bold, shadow outline, underline, italics, and strikeout. Because metafonts contain character size information, strings that use metafonts are more likely to have the same width across platforms. This value is an alias to an operating system font. Therefore, the operating system and user preferences on your machine determine this font. |
| VAL_MESSAGE_BOX_META_FONT | Default font for LabWindows/CVI message boxes. Metafonts contain typeface information, point size, and text styles such as bold, shadow outline, underline, italics, and strikeout. Because metafonts contain character size information, strings that use metafonts are more likely to have the same width across platforms. This value is an alias to an operating system font. Therefore, the operating system and user preferences on your machine determine this font. |
| VAL_7SEG_META_FONT | Font that provides compatibility with LabWindows for DOS. Metafonts contain typeface information, point size, and text styles such as bold, shadow outline, underline, italics, and strikeout. Because metafonts contain character size information, strings that use metafonts are more likely to have the same width across platforms. |
| VAL_SYSTEM_META_FONT | Font that provides compatibility with function panels and user interface panels from LabWindows for DOS that use extended IBM PC characters. Because other fonts may not contain these extended characters, cut/paste operations may fail. Metafonts contain typeface information, point size, and text styles such as bold, shadow outline, underline, italics, and strikeout. Because metafonts contain character size information, strings that use metafonts are more likely to have the same width across platforms. |

<!--NI_TOPIC bundle=labwindows-cvi path=cvi/uiref/cviattrtextfont_column.htm language=enus -->
## TOPIC 00791: ATTR_TEXT_FONT (Column)

- bundle_id: `labwindows-cvi`
- source_path: `cvi/uiref/cviattrtextfont_column.htm`
- source_url: https://docs-be.ni.com/bundle/labwindows-cvi/raw/resource/enus/cvi/uiref/cviattrtextfont_column.htm
- document_id: `labwindows-cvi`
- page_type: `leaf`
- content_type: ``

### ATTR_TEXT_FONT (Column)

| Type: | Column attribute |
| --- | --- |
| Description: | The name of the font for the table cell text. To determine the size of the buffer to pass when you are obtaining the font name, call GetTableColumnAttribute and specify the ATTR_TEXT_FONT_NAME_LENGTH attribute. You can use a LabWindows/CVI-supplied font; any host font—such as Arial or Courier—supported on your system; or a user-defined metafont saved by a previous call to functions such as CreateMetaFont and CreateMetaFontEx. Note:LabWindows/CVI returns an error if you use a metafont that specifies an angle for the text. Always set the font before setting the size or style. |
| Data Type: | string |
| Default Value: | VAL_DIALOG_META_FONT |
| LabWindows/CVICompatibility: | LabWindows/CVI 5.5 and later |

##### Values

| VAL_MENU_FONT | Default font style for LabWindows/CVI menus. This font contains typeface information only. This value is an alias to an operating system font. Therefore, the operating system and user preferences on your machine determine this font style. |
| --- | --- |
| VAL_DIALOG_FONT | Default font style for LabWindows/CVI dialog boxes and control text. This font contains typeface information only. This value is an alias to an operating system font. Therefore, the operating system and user preferences on your machine determine this font style. |
| VAL_EDITOR_FONT | Default font style for the LabWindows/CVI Source window. This font contains typeface information only. This value is an alias to an operating system font. Therefore, the operating system and user preferences on your machine determine this font style. |
| VAL_APP_FONT | Default font style for the LabWindows/CVI Workspace window. This font contains typeface information only. This value is an alias to an operating system font. Therefore, the operating system and user preferences on your machine determine this font style. |
| VAL_MESSAGE_BOX_FONT | Default font style for LabWindows/CVI message boxes. This font contains typeface information only. This value is an alias to an operating system font. Therefore, the operating system and user preferences on your machine determine this font style. |
| VAL_MENU_META_FONT | Default font for LabWindows/CVI menus. Metafonts contain typeface information, point size, and text styles such as bold, shadow outline, underline, italics, and strikeout. Because metafonts contain character size information, strings that use metafonts are more likely to have the same width across platforms. This value is an alias to an operating system font. Therefore, the operating system and user preferences on your machine determine this font. |
| VAL_DIALOG_META_FONT | Default font for LabWindows/CVI dialog boxes and control text. Metafonts contain typeface information, point size, and text styles such as bold, shadow outline, underline, italics, and strikeout. Because metafonts contain character size information, strings that use metafonts are more likely to have the same width across platforms. This value is an alias to an operating system font. Therefore, the operating system and user preferences on your machine determine this font. |
| VAL_EDITOR_META_FONT | Default font for the LabWindows/CVI Source window. Metafonts contain typeface information, point size, and text styles such as bold, shadow outline, underline, italics, and strikeout. Because metafonts contain character size information, strings that use metafonts are more likely to have the same width across platforms. This value is an alias to an operating system font. Therefore, the operating system and user preferences on your machine determine this font. |
| VAL_APP_META_FONT | Default font for the LabWindows/CVI Workspace window. Metafonts contain typeface information, point size, and text styles such as bold, shadow outline, underline, italics, and strikeout. Because metafonts contain character size information, strings that use metafonts are more likely to have the same width across platforms. This value is an alias to an operating system font. Therefore, the operating system and user preferences on your machine determine this font. |
| VAL_MESSAGE_BOX_META_FONT | Default font for LabWindows/CVI message boxes. Metafonts contain typeface information, point size, and text styles such as bold, shadow outline, underline, italics, and strikeout. Because metafonts contain character size information, strings that use metafonts are more likely to have the same width across platforms. This value is an alias to an operating system font. Therefore, the operating system and user preferences on your machine determine this font. |
| VAL_7SEG_META_FONT | Font that provides compatibility with LabWindows for DOS. Metafonts contain typeface information, point size, and text styles such as bold, shadow outline, underline, italics, and strikeout. Because metafonts contain character size information, strings that use metafonts are more likely to have the same width across platforms. |
| VAL_SYSTEM_META_FONT | Font that provides compatibility with function panels and user interface panels from LabWindows for DOS that use extended IBM PC characters. Because other fonts may not contain these extended characters, cut/paste operations may fail. Metafonts contain typeface information, point size, and text styles such as bold, shadow outline, underline, italics, and strikeout. Because metafonts contain character size information, strings that use metafonts are more likely to have the same width across platforms. |

<!--NI_TOPIC bundle=labwindows-cvi path=cvi/uiref/cviattrtextfont_control.htm language=enus -->
## TOPIC 00792: ATTR_TEXT_FONT (Control)

- bundle_id: `labwindows-cvi`
- source_path: `cvi/uiref/cviattrtextfont_control.htm`
- source_url: https://docs-be.ni.com/bundle/labwindows-cvi/raw/resource/enus/cvi/uiref/cviattrtextfont_control.htm
- document_id: `labwindows-cvi`
- page_type: `leaf`
- content_type: ``

### ATTR_TEXT_FONT (Control)

| Type: | Control attribute |
| --- | --- |
| Description: | The name of the font for text on the control. For table controls, this attribute refers to the default state of new cells when you set ATTR_TABLE_MODE to VAL_GRID. To determine the size of the buffer to pass when you are obtaining the font name, call GetCtrlAttribute and specify the ATTR_TEXT_FONT_NAME_LENGTH attribute. You can use a LabWindows/CVI-supplied font; any host font—such as Arial or Courier—supported on your system; or a user-defined metafont saved by a previous call to functions such as CreateMetaFont and CreateMetaFontEx. Always set the font before setting the size or style. |
| Control Types: | Binary switches, list boxes, numerics, rings, numeric slides, ring slides, strings, tables, text boxes, text buttons, text messages. |
| Data Type: | string |
| Default Value: | VAL_DIALOG_META_FONT |
| LabWindows/CVICompatibility: | LabWindows/CVI 3.0 and later |

##### Values

| VAL_MENU_FONT | Default font style for LabWindows/CVI menus. This font contains typeface information only. This value is an alias to an operating system font. Therefore, the operating system and user preferences on your machine determine this font style. |
| --- | --- |
| VAL_DIALOG_FONT | Default font style for LabWindows/CVI dialog boxes and control text. This font contains typeface information only. This value is an alias to an operating system font. Therefore, the operating system and user preferences on your machine determine this font style. |
| VAL_EDITOR_FONT | Default font style for the LabWindows/CVI Source window. This font contains typeface information only. This value is an alias to an operating system font. Therefore, the operating system and user preferences on your machine determine this font style. |
| VAL_APP_FONT | Default font style for the LabWindows/CVI Workspace window. This font contains typeface information only. This value is an alias to an operating system font. Therefore, the operating system and user preferences on your machine determine this font style. |
| VAL_MESSAGE_BOX_FONT | Default font style for LabWindows/CVI message boxes. This font contains typeface information only. This value is an alias to an operating system font. Therefore, the operating system and user preferences on your machine determine this font style. |
| VAL_MENU_META_FONT | Default font for LabWindows/CVI menus. Metafonts contain typeface information, point size, and text styles such as bold, shadow outline, underline, italics, and strikeout. Because metafonts contain character size information, strings that use metafonts are more likely to have the same width across platforms. This value is an alias to an operating system font. Therefore, the operating system and user preferences on your machine determine this font. |
| VAL_DIALOG_META_FONT | Default font for LabWindows/CVI dialog boxes and control text. Metafonts contain typeface information, point size, and text styles such as bold, shadow outline, underline, italics, and strikeout. Because metafonts contain character size information, strings that use metafonts are more likely to have the same width across platforms. This value is an alias to an operating system font. Therefore, the operating system and user preferences on your machine determine this font. |
| VAL_EDITOR_META_FONT | Default font for the LabWindows/CVI Source window. Metafonts contain typeface information, point size, and text styles such as bold, shadow outline, underline, italics, and strikeout. Because metafonts contain character size information, strings that use metafonts are more likely to have the same width across platforms. This value is an alias to an operating system font. Therefore, the operating system and user preferences on your machine determine this font. |
| VAL_APP_META_FONT | Default font for the LabWindows/CVI Workspace window. Metafonts contain typeface information, point size, and text styles such as bold, shadow outline, underline, italics, and strikeout. Because metafonts contain character size information, strings that use metafonts are more likely to have the same width across platforms. This value is an alias to an operating system font. Therefore, the operating system and user preferences on your machine determine this font. |
| VAL_MESSAGE_BOX_META_FONT | Default font for LabWindows/CVI message boxes. Metafonts contain typeface information, point size, and text styles such as bold, shadow outline, underline, italics, and strikeout. Because metafonts contain character size information, strings that use metafonts are more likely to have the same width across platforms. This value is an alias to an operating system font. Therefore, the operating system and user preferences on your machine determine this font. |
| VAL_7SEG_META_FONT | Font that provides compatibility with LabWindows for DOS. Metafonts contain typeface information, point size, and text styles such as bold, shadow outline, underline, italics, and strikeout. Because metafonts contain character size information, strings that use metafonts are more likely to have the same width across platforms. |
| VAL_SYSTEM_META_FONT | Font that provides compatibility with function panels and user interface panels from LabWindows for DOS that use extended IBM PC characters. Because other fonts may not contain these extended characters, cut/paste operations may fail. Metafonts contain typeface information, point size, and text styles such as bold, shadow outline, underline, italics, and strikeout. Because metafonts contain character size information, strings that use metafonts are more likely to have the same width across platforms. |

<!--NI_TOPIC bundle=labwindows-cvi path=cvi/uiref/cviattrtextfont_row.htm language=enus -->
## TOPIC 00793: ATTR_TEXT_FONT (Row)

- bundle_id: `labwindows-cvi`
- source_path: `cvi/uiref/cviattrtextfont_row.htm`
- source_url: https://docs-be.ni.com/bundle/labwindows-cvi/raw/resource/enus/cvi/uiref/cviattrtextfont_row.htm
- document_id: `labwindows-cvi`
- page_type: `leaf`
- content_type: ``

### ATTR_TEXT_FONT (Row)

| Type: | Row attribute |
| --- | --- |
| Description: | The name of the font for the table cell text. To determine the size of the buffer to pass when you are obtaining the font name, call GetTableRowAttribute and specify the ATTR_TEXT_FONT_NAME_LENGTH attribute. You can use a LabWindows/CVI-supplied font; any host font—such as Arial or Courier—supported on your system; or a user-defined metafont saved by a previous call to functions such as CreateMetaFont and CreateMetaFontEx. Note: LabWindows/CVI returns an error if you use a metafont that specifies an angle for the text. Always set the font before setting the size or style. |
| Data Type: | string |
| Default Value: | VAL_DIALOG_META_FONT |
| LabWindows/CVICompatibility: | LabWindows/CVI 5.5 and later |

##### Values

| VAL_MENU_FONT | Default font style for LabWindows/CVI menus. This font contains typeface information only. This value is an alias to an operating system font. Therefore, the operating system and user preferences on your machine determine this font style. |
| --- | --- |
| VAL_DIALOG_FONT | Default font style for LabWindows/CVI dialog boxes and control text. This font contains typeface information only. This value is an alias to an operating system font. Therefore, the operating system and user preferences on your machine determine this font style. |
| VAL_EDITOR_FONT | Default font style for the LabWindows/CVI Source window. This font contains typeface information only. This value is an alias to an operating system font. Therefore, the operating system and user preferences on your machine determine this font style. |
| VAL_APP_FONT | Default font style for the LabWindows/CVI Workspace window. This font contains typeface information only. This value is an alias to an operating system font. Therefore, the operating system and user preferences on your machine determine this font style. |
| VAL_MESSAGE_BOX_FONT | Default font style for LabWindows/CVI message boxes. This font contains typeface information only. This value is an alias to an operating system font. Therefore, the operating system and user preferences on your machine determine this font style. |
| VAL_MENU_META_FONT | Default font for LabWindows/CVI menus. Metafonts contain typeface information, point size, and text styles such as bold, shadow outline, underline, italics, and strikeout. Because metafonts contain character size information, strings that use metafonts are more likely to have the same width across platforms. This value is an alias to an operating system font. Therefore, the operating system and user preferences on your machine determine this font. |
| VAL_DIALOG_META_FONT | Default font for LabWindows/CVI dialog boxes and control text. Metafonts contain typeface information, point size, and text styles such as bold, shadow outline, underline, italics, and strikeout. Because metafonts contain character size information, strings that use metafonts are more likely to have the same width across platforms. This value is an alias to an operating system font. Therefore, the operating system and user preferences on your machine determine this font. |
| VAL_EDITOR_META_FONT | Default font for the LabWindows/CVI Source window. Metafonts contain typeface information, point size, and text styles such as bold, shadow outline, underline, italics, and strikeout. Because metafonts contain character size information, strings that use metafonts are more likely to have the same width across platforms. This value is an alias to an operating system font. Therefore, the operating system and user preferences on your machine determine this font. |
| VAL_APP_META_FONT | Default font for the LabWindows/CVI Workspace window. Metafonts contain typeface information, point size, and text styles such as bold, shadow outline, underline, italics, and strikeout. Because metafonts contain character size information, strings that use metafonts are more likely to have the same width across platforms. This value is an alias to an operating system font. Therefore, the operating system and user preferences on your machine determine this font. |
| VAL_MESSAGE_BOX_META_FONT | Default font for LabWindows/CVI message boxes. Metafonts contain typeface information, point size, and text styles such as bold, shadow outline, underline, italics, and strikeout. Because metafonts contain character size information, strings that use metafonts are more likely to have the same width across platforms. This value is an alias to an operating system font. Therefore, the operating system and user preferences on your machine determine this font. |
| VAL_7SEG_META_FONT | Font that provides compatibility with LabWindows for DOS. Metafonts contain typeface information, point size, and text styles such as bold, shadow outline, underline, italics, and strikeout. Because metafonts contain character size information, strings that use metafonts are more likely to have the same width across platforms. |
| VAL_SYSTEM_META_FONT | Font that provides compatibility with function panels and user interface panels from LabWindows for DOS that use extended IBM PC characters. Because other fonts may not contain these extended characters, cut/paste operations may fail. Metafonts contain typeface information, point size, and text styles such as bold, shadow outline, underline, italics, and strikeout. Because metafonts contain character size information, strings that use metafonts are more likely to have the same width across platforms. |

<!--NI_TOPIC bundle=labwindows-cvi path=cvi/uiref/cviattrtextfontnamelength_system popups.htm language=enus -->
## TOPIC 00794: ATTR_TEXT_FONT_NAME_LENGTH (System Popups)

- bundle_id: `labwindows-cvi`
- source_path: `cvi/uiref/cviattrtextfontnamelength_system popups.htm`
- source_url: https://docs-be.ni.com/bundle/labwindows-cvi/raw/resource/enus/cvi/uiref/cviattrtextfontnamelength_system%20popups.htm
- document_id: `labwindows-cvi`
- page_type: `leaf`
- content_type: ``

### ATTR_TEXT_FONT_NAME_LENGTH (System Popups)

| Type: | System Pop-Ups attribute |
| --- | --- |
| Description: | The number of bytes in the name of the font for the system pop-up message text. The length does not include the ASCII NUL byte. Use this value to determine the size of the buffer to pass when you call GetTableColumnAttribute and specify the ATTR_TEXT_FONT attribute. |
| Restrictions: | Not settable. |
| Data Type: | integer |
| Default Value: | 0 |
| LabWindows/CVICompatibility: | LabWindows/CVI 2012 and later |

<!--NI_TOPIC bundle=labwindows-cvi path=cvi/uiref/cviattrtextpointsize_column.htm language=enus -->
## TOPIC 00795: ATTR_TEXT_POINT_SIZE (Column)

- bundle_id: `labwindows-cvi`
- source_path: `cvi/uiref/cviattrtextpointsize_column.htm`
- source_url: https://docs-be.ni.com/bundle/labwindows-cvi/raw/resource/enus/cvi/uiref/cviattrtextpointsize_column.htm
- document_id: `labwindows-cvi`
- page_type: `leaf`
- content_type: ``

### ATTR_TEXT_POINT_SIZE (Column)

| Type: | Column attribute |
| --- | --- |
| Description: | The font point size for the table cell text. |
| Data Type: | integer |
| Valid Range: | 1 to 255 |
| LabWindows/CVICompatibility: | LabWindows/CVI 5.5 and later |

<!--NI_TOPIC bundle=labwindows-cvi path=cvi/uiref/cviattrtextpointsize_control.htm language=enus -->
## TOPIC 00796: ATTR_TEXT_POINT_SIZE (Control)

- bundle_id: `labwindows-cvi`
- source_path: `cvi/uiref/cviattrtextpointsize_control.htm`
- source_url: https://docs-be.ni.com/bundle/labwindows-cvi/raw/resource/enus/cvi/uiref/cviattrtextpointsize_control.htm
- document_id: `labwindows-cvi`
- page_type: `leaf`
- content_type: ``

### ATTR_TEXT_POINT_SIZE (Control)

| Type: | Control attribute |
| --- | --- |
| Description: | The text point size of the control. When used on a table, it refers to the default state of new cells when ATTR_TABLE_MODE is set to VAL_GRID. |
| Control Types: | Binary switches, list boxes, numerics, rings, numeric slides, ring slides, strings, tables, text boxes, text buttons, text messages. |
| Data Type: | integer |
| Valid Range: | 1 to 255 |
| LabWindows/CVICompatibility: | LabWindows/CVI 3.0 and later |

<!--NI_TOPIC bundle=labwindows-cvi path=cvi/uiref/cviattrtextpointsize_row.htm language=enus -->
## TOPIC 00797: ATTR_TEXT_POINT_SIZE (Row)

- bundle_id: `labwindows-cvi`
- source_path: `cvi/uiref/cviattrtextpointsize_row.htm`
- source_url: https://docs-be.ni.com/bundle/labwindows-cvi/raw/resource/enus/cvi/uiref/cviattrtextpointsize_row.htm
- document_id: `labwindows-cvi`
- page_type: `leaf`
- content_type: ``

### ATTR_TEXT_POINT_SIZE (Row)

| Type: | Row attribute |
| --- | --- |
| Description: | The font point size for the table cell text. |
| Data Type: | integer |
| Valid Range: | 1 to 255 |
| LabWindows/CVICompatibility: | LabWindows/CVI 5.5 and later |

<!--NI_TOPIC bundle=labwindows-cvi path=cvi/uiref/cviattrtextpointsize_system popups.htm language=enus -->
## TOPIC 00798: ATTR_TEXT_POINT_SIZE (System Popups)

- bundle_id: `labwindows-cvi`
- source_path: `cvi/uiref/cviattrtextpointsize_system popups.htm`
- source_url: https://docs-be.ni.com/bundle/labwindows-cvi/raw/resource/enus/cvi/uiref/cviattrtextpointsize_system%20popups.htm
- document_id: `labwindows-cvi`
- page_type: `leaf`
- content_type: ``

### ATTR_TEXT_POINT_SIZE (System Popups)

| Type: | System Pop-Ups attribute |
| --- | --- |
| Description: | The font point size for the system pop-up message text. |
| Data Type: | integer |
| LabWindows/CVICompatibility: | LabWindows/CVI 2012 and later |

<!--NI_TOPIC bundle=labwindows-cvi path=cvi/uiref/cviattrtextraised.htm language=enus -->
## TOPIC 00799: ATTR_TEXT_RAISED

- bundle_id: `labwindows-cvi`
- source_path: `cvi/uiref/cviattrtextraised.htm`
- source_url: https://docs-be.ni.com/bundle/labwindows-cvi/raw/resource/enus/cvi/uiref/cviattrtextraised.htm
- document_id: `labwindows-cvi`
- page_type: `leaf`
- content_type: ``

### ATTR_TEXT_RAISED

| Type: | Control attribute |
| --- | --- |
| Description: | Specifies whether the message text is raised. 0 = Not raised text 1 = Raised text |
| Control Types: | Text messages. |
| Data Type: | integer |
| Default Value: | 0 |
| LabWindows/CVICompatibility: | LabWindows/CVI 3.0 and later |

##### Values

| 0 | False |
| --- | --- |
| 1 | True |

<!--NI_TOPIC bundle=labwindows-cvi path=cvi/uiref/cviattrtextselectionlength.htm language=enus -->
## TOPIC 00800: ATTR_TEXT_SELECTION_LENGTH

- bundle_id: `labwindows-cvi`
- source_path: `cvi/uiref/cviattrtextselectionlength.htm`
- source_url: https://docs-be.ni.com/bundle/labwindows-cvi/raw/resource/enus/cvi/uiref/cviattrtextselectionlength.htm
- document_id: `labwindows-cvi`
- page_type: `leaf`
- content_type: ``

### ATTR_TEXT_SELECTION_LENGTH

| Type: | Control attribute |
| --- | --- |
| Description: | The number of bytes in the text currently selected in the control. The length does not include the terminating NUL byte. If no text is selected, the value is zero. When used on a table, and the table is in edit state, this attribute refers to the cell being edited. |
| Control Types: | Strings, tables, text boxes. |
| Data Type: | integer |
| Valid Range: | 0 or greater |
| LabWindows/CVICompatibility: | LabWindows/CVI 3.0 and later |

<!--NI_TOPIC bundle=labwindows-cvi path=cvi/uiref/cviattrtextstrikeout_column.htm language=enus -->
## TOPIC 00801: ATTR_TEXT_STRIKEOUT (Column)

- bundle_id: `labwindows-cvi`
- source_path: `cvi/uiref/cviattrtextstrikeout_column.htm`
- source_url: https://docs-be.ni.com/bundle/labwindows-cvi/raw/resource/enus/cvi/uiref/cviattrtextstrikeout_column.htm
- document_id: `labwindows-cvi`
- page_type: `leaf`
- content_type: ``

### ATTR_TEXT_STRIKEOUT (Column)

| Type: | Column attribute |
| --- | --- |
| Description: | Specifies whether the table cell text has strikeout. 0 = Do not strikeout 1 = Strikeout |
| Data Type: | integer |
| Default Value: | 0 |
| LabWindows/CVICompatibility: | LabWindows/CVI 5.5 and later |

##### Values

| 0 | False |
| --- | --- |
| 1 | True |

<!--NI_TOPIC bundle=labwindows-cvi path=cvi/uiref/cviattrtextstrikeout_system popups.htm language=enus -->
## TOPIC 00802: ATTR_TEXT_STRIKEOUT (System Popups)

- bundle_id: `labwindows-cvi`
- source_path: `cvi/uiref/cviattrtextstrikeout_system popups.htm`
- source_url: https://docs-be.ni.com/bundle/labwindows-cvi/raw/resource/enus/cvi/uiref/cviattrtextstrikeout_system%20popups.htm
- document_id: `labwindows-cvi`
- page_type: `leaf`
- content_type: ``

### ATTR_TEXT_STRIKEOUT (System Popups)

| Type: | System Pop-Ups attribute |
| --- | --- |
| Description: | Specifies whether to strike out text on the system pop-up message. 0 = Do not strikeout 1 = Strikeout |
| Data Type: | integer |
| Default Value: | 0 |
| LabWindows/CVICompatibility: | LabWindows/CVI 2012 and later |

##### Values

| 0 | False |
| --- | --- |
| 1 | True |

<!--NI_TOPIC bundle=labwindows-cvi path=cvi/uiref/cviattrtextunderline_control.htm language=enus -->
## TOPIC 00803: ATTR_TEXT_UNDERLINE (Control)

- bundle_id: `labwindows-cvi`
- source_path: `cvi/uiref/cviattrtextunderline_control.htm`
- source_url: https://docs-be.ni.com/bundle/labwindows-cvi/raw/resource/enus/cvi/uiref/cviattrtextunderline_control.htm
- document_id: `labwindows-cvi`
- page_type: `leaf`
- content_type: ``

### ATTR_TEXT_UNDERLINE (Control)

| Type: | Control attribute |
| --- | --- |
| Description: | Specifies whether the control text is underlined. When used on a table, it refers to the default state of new cells when ATTR_TABLE_MODE is set to VAL_GRID. 0 = Not underlined 1 = Underlined |
| Control Types: | Binary switches, list boxes, numerics, rings, numeric slides, ring slides, strings, tables, text boxes, text buttons, text messages. |
| Data Type: | integer |
| Default Value: | 0 |
| LabWindows/CVICompatibility: | LabWindows/CVI 3.0 and later |

##### Values

| 0 | False |
| --- | --- |
| 1 | True |

<!--NI_TOPIC bundle=labwindows-cvi path=cvi/uiref/cviattrtitlebarthickness.htm language=enus -->
## TOPIC 00804: ATTR_TITLEBAR_THICKNESS

- bundle_id: `labwindows-cvi`
- source_path: `cvi/uiref/cviattrtitlebarthickness.htm`
- source_url: https://docs-be.ni.com/bundle/labwindows-cvi/raw/resource/enus/cvi/uiref/cviattrtitlebarthickness.htm
- document_id: `labwindows-cvi`
- page_type: `leaf`
- content_type: ``

### ATTR_TITLEBAR_THICKNESS

| Type: | Panel attribute |
| --- | --- |
| Description: | The thickness of the panel titlebar in pixels. |
| Restrictions: | Valid for child panels only. |
| Data Type: | integer |
| Valid Range: | 0 to 32767 |
| Default Value: | 16 |
| LabWindows/CVICompatibility: | LabWindows/CVI 3.0 and later |

<!--NI_TOPIC bundle=labwindows-cvi path=cvi/uiref/cviattrtitlefontnamelength.htm language=enus -->
## TOPIC 00805: ATTR_TITLE_FONT_NAME_LENGTH

- bundle_id: `labwindows-cvi`
- source_path: `cvi/uiref/cviattrtitlefontnamelength.htm`
- source_url: https://docs-be.ni.com/bundle/labwindows-cvi/raw/resource/enus/cvi/uiref/cviattrtitlefontnamelength.htm
- document_id: `labwindows-cvi`
- page_type: `leaf`
- content_type: ``

### ATTR_TITLE_FONT_NAME_LENGTH

| Type: | Panel attribute |
| --- | --- |
| Description: | The number of bytes in the name of the font for the panel title. The length does not include the ASCII NUL byte. Use this value to determine the size of the buffer to pass when you call GetPanelAttribute and specify the ATTR_TITLE_FONT attribute. |
| Restrictions: | Not settable. Valid for child panels only. |
| Data Type: | integer |
| LabWindows/CVICompatibility: | LabWindows/CVI 3.0 and later |

<!--NI_TOPIC bundle=labwindows-cvi path=cvi/uiref/cviattrtitleitalic.htm language=enus -->
## TOPIC 00806: ATTR_TITLE_ITALIC

- bundle_id: `labwindows-cvi`
- source_path: `cvi/uiref/cviattrtitleitalic.htm`
- source_url: https://docs-be.ni.com/bundle/labwindows-cvi/raw/resource/enus/cvi/uiref/cviattrtitleitalic.htm
- document_id: `labwindows-cvi`
- page_type: `leaf`
- content_type: ``

### ATTR_TITLE_ITALIC

| Type: | Panel attribute |
| --- | --- |
| Description: | Specifies whether the panel title is in italics. 0 = Not italics 1 = Italics |
| Restrictions: | Valid for child panels only. |
| Data Type: | integer |
| Default Value: | 0 |
| LabWindows/CVICompatibility: | LabWindows/CVI 3.0 and later |

##### Values

| 0 | False |
| --- | --- |
| 1 | True |

<!--NI_TOPIC bundle=labwindows-cvi path=cvi/uiref/cviattrtitlelength.htm language=enus -->
## TOPIC 00807: ATTR_TITLE_LENGTH

- bundle_id: `labwindows-cvi`
- source_path: `cvi/uiref/cviattrtitlelength.htm`
- source_url: https://docs-be.ni.com/bundle/labwindows-cvi/raw/resource/enus/cvi/uiref/cviattrtitlelength.htm
- document_id: `labwindows-cvi`
- page_type: `leaf`
- content_type: ``

### ATTR_TITLE_LENGTH

| Type: | Panel attribute |
| --- | --- |
| Description: | The number of bytes in the panel title. The length does not include the ASCII NUL byte. Use this value to determine the size of the buffer to pass when you call GetPanelAttribute and specify the ATTR_TITLE attribute. |
| Restrictions: | Not settable. |
| Data Type: | integer |
| LabWindows/CVICompatibility: | LabWindows/CVI 3.0 and later |

<!--NI_TOPIC bundle=labwindows-cvi path=cvi/uiref/cviattrtitlepointsize.htm language=enus -->
## TOPIC 00808: ATTR_TITLE_POINT_SIZE

- bundle_id: `labwindows-cvi`
- source_path: `cvi/uiref/cviattrtitlepointsize.htm`
- source_url: https://docs-be.ni.com/bundle/labwindows-cvi/raw/resource/enus/cvi/uiref/cviattrtitlepointsize.htm
- document_id: `labwindows-cvi`
- page_type: `leaf`
- content_type: ``

### ATTR_TITLE_POINT_SIZE

| Type: | Panel attribute |
| --- | --- |
| Description: | The font point size for the panel title. |
| Restrictions: | Valid for child panels only. |
| Data Type: | integer |
| Valid Range: | 1 to 255 |
| LabWindows/CVICompatibility: | LabWindows/CVI 3.0 and later |

<!--NI_TOPIC bundle=labwindows-cvi path=cvi/uiref/cviattrtitlesizetofont.htm language=enus -->
## TOPIC 00809: ATTR_TITLE_SIZE_TO_FONT

- bundle_id: `labwindows-cvi`
- source_path: `cvi/uiref/cviattrtitlesizetofont.htm`
- source_url: https://docs-be.ni.com/bundle/labwindows-cvi/raw/resource/enus/cvi/uiref/cviattrtitlesizetofont.htm
- document_id: `labwindows-cvi`
- page_type: `leaf`
- content_type: ``

### ATTR_TITLE_SIZE_TO_FONT

| Type: | Panel attribute |
| --- | --- |
| Description: | Specifies whether the panel title is sized to the font. 0 = Not sized 1 = Sized |
| Restrictions: | Valid for child panels only. |
| Data Type: | integer |
| Default Value: | 1 |
| LabWindows/CVICompatibility: | LabWindows/CVI 4.0 and later |

##### Values

| 0 | False |
| --- | --- |
| 1 | True |

<!--NI_TOPIC bundle=labwindows-cvi path=cvi/uiref/cviattrtooltiphidedelay.htm language=enus -->
## TOPIC 00810: ATTR_TOOLTIP_HIDE_DELAY

- bundle_id: `labwindows-cvi`
- source_path: `cvi/uiref/cviattrtooltiphidedelay.htm`
- source_url: https://docs-be.ni.com/bundle/labwindows-cvi/raw/resource/enus/cvi/uiref/cviattrtooltiphidedelay.htm
- document_id: `labwindows-cvi`
- page_type: `leaf`
- content_type: ``

### ATTR_TOOLTIP_HIDE_DELAY

| Type: | Control attribute |
| --- | --- |
| Description: | The amount of time to delay, in milliseconds, before the visible control tooltip is hidden. A value of 0 indicates that the tooltip displays continuously while the mouse hovers over the control. |
| Control Types: | ActiveX controls, binary switches, canvases, color numerics, command buttons, decorations, digital graphs, graphs, LEDs, list boxes, numerics, picture buttons, picture rings, pictures, radio buttons, rings, numeric slides, ring slides, splitters, strings, strip charts, tab controls, tables, text boxes, text buttons, text messages, timers, toggle buttons, trees. |
| Data Type: | integer |
| Valid Range: | >=0 |
| Default Value: | 0 |
| LabWindows/CVICompatibility: | LabWindows/CVI 2013 and later |

<!--NI_TOPIC bundle=labwindows-cvi path=cvi/uiref/cviattrtooltiptext_control.htm language=enus -->
## TOPIC 00811: ATTR_TOOLTIP_TEXT (Control)

- bundle_id: `labwindows-cvi`
- source_path: `cvi/uiref/cviattrtooltiptext_control.htm`
- source_url: https://docs-be.ni.com/bundle/labwindows-cvi/raw/resource/enus/cvi/uiref/cviattrtooltiptext_control.htm
- document_id: `labwindows-cvi`
- page_type: `leaf`
- content_type: ``

### ATTR_TOOLTIP_TEXT (Control)

| Type: | Control attribute |
| --- | --- |
| Description: | The text for the tooltip that displays when you hover the mouse over the control. If no value is assigned to this attribute, LabWindows/CVI does not display a tooltip. To create multiline tooltips, insert a newline character (\\n) in the tooltip text string. Use the \\t escape sequence to insert a tab in your tooltips. To determine the size of the buffer to pass when you are obtaining the text, call GetCtrlAttribute and specify the ATTR_TOOLTIP_TEXT_LENGTH attribute. |
| Control Types: | ActiveX controls, binary switches, canvases, color numerics, command buttons, decorations, digital graphs, graphs, LEDs, list boxes, numerics, picture buttons, picture rings, pictures, radio buttons, rings, numeric slides, ring slides, splitters, strings, strip charts, tab controls, tables, text boxes, text buttons, text messages, timers, toggle buttons, trees. |
| Data Type: | string |
| LabWindows/CVICompatibility: | LabWindows/CVI 2012 and later |

<!--NI_TOPIC bundle=labwindows-cvi path=cvi/uiref/cviattrtooltiptext_tree cell.htm language=enus -->
## TOPIC 00812: ATTR_TOOLTIP_TEXT (Tree Cell)

- bundle_id: `labwindows-cvi`
- source_path: `cvi/uiref/cviattrtooltiptext_tree cell.htm`
- source_url: https://docs-be.ni.com/bundle/labwindows-cvi/raw/resource/enus/cvi/uiref/cviattrtooltiptext_tree%20cell.htm
- document_id: `labwindows-cvi`
- page_type: `leaf`
- content_type: ``

### ATTR_TOOLTIP_TEXT (Tree Cell)

| Type: | Tree Cell attribute |
| --- | --- |
| Description: | The text for the tree cell tooltip. To determine the size of the buffer to pass when you are obtaining the text, call GetTreeCellAttribute and specify the ATTR_TOOLTIP_TEXT_LENGTH attribute. |
| Data Type: | string |
| LabWindows/CVICompatibility: | LabWindows/CVI 8.5 and later |

<!--NI_TOPIC bundle=labwindows-cvi path=cvi/uiref/cviattrtooltiptext_tree item.htm language=enus -->
## TOPIC 00813: ATTR_TOOLTIP_TEXT (Tree Item)

- bundle_id: `labwindows-cvi`
- source_path: `cvi/uiref/cviattrtooltiptext_tree item.htm`
- source_url: https://docs-be.ni.com/bundle/labwindows-cvi/raw/resource/enus/cvi/uiref/cviattrtooltiptext_tree%20item.htm
- document_id: `labwindows-cvi`
- page_type: `leaf`
- content_type: ``

### ATTR_TOOLTIP_TEXT (Tree Item)

| Type: | Tree Item attribute |
| --- | --- |
| Description: | The text for the tree item tooltip. To determine the size of the buffer to pass when you are obtaining the text, call GetTreeItemAttribute and specify the ATTR_TOOLTIP_TEXT_LENGTH attribute. Using this in SetTreeItemAttribute or GetTreeItemAttribute is equivalent to using it in SetTreeCellAttribute or GetTreeCellAttribute if you pass zero for the column index. |
| Data Type: | string |
| LabWindows/CVICompatibility: | LabWindows/CVI 8.5 and later |

<!--NI_TOPIC bundle=labwindows-cvi path=cvi/uiref/cviattrtooltiptextlength_control.htm language=enus -->
## TOPIC 00814: ATTR_TOOLTIP_TEXT_LENGTH (Control)

- bundle_id: `labwindows-cvi`
- source_path: `cvi/uiref/cviattrtooltiptextlength_control.htm`
- source_url: https://docs-be.ni.com/bundle/labwindows-cvi/raw/resource/enus/cvi/uiref/cviattrtooltiptextlength_control.htm
- document_id: `labwindows-cvi`
- page_type: `leaf`
- content_type: ``

### ATTR_TOOLTIP_TEXT_LENGTH (Control)

| Type: | Control attribute |
| --- | --- |
| Description: | The number of bytes in the control tooltip. The length does not include the ASCII NUL byte. Use this value to determine the size of the buffer to pass when you call GetCtrlAttribute and specify the ATTR_TOOLTIP_TEXT attribute. |
| Control Types: | ActiveX controls, binary switches, canvases, color numerics, command buttons, decorations, digital graphs, graphs, LEDs, list boxes, numerics, picture buttons, picture rings, pictures, radio buttons, rings, numeric slides, ring slides, splitters, strings, strip charts, tab controls, tables, text boxes, text buttons, text messages, timers, toggle buttons, trees. |
| Restrictions: | Not settable. |
| Data Type: | integer |
| LabWindows/CVICompatibility: | LabWindows/CVI 2012 and later |

<!--NI_TOPIC bundle=labwindows-cvi path=cvi/uiref/cviattrtooltiptextlength_tree cell.htm language=enus -->
## TOPIC 00815: ATTR_TOOLTIP_TEXT_LENGTH (Tree Cell)

- bundle_id: `labwindows-cvi`
- source_path: `cvi/uiref/cviattrtooltiptextlength_tree cell.htm`
- source_url: https://docs-be.ni.com/bundle/labwindows-cvi/raw/resource/enus/cvi/uiref/cviattrtooltiptextlength_tree%20cell.htm
- document_id: `labwindows-cvi`
- page_type: `leaf`
- content_type: ``

### ATTR_TOOLTIP_TEXT_LENGTH (Tree Cell)

| Type: | Tree Cell attribute |
| --- | --- |
| Description: | The number of bytes in the tree cell tooltip. The length does not include the ASCII NUL byte. Use this value to determine the size of the buffer to pass when you call GetTreeCellAttribute and specify the ATTR_TOOLTIP_TEXT attribute. |
| Restrictions: | Not settable. |
| Data Type: | integer |
| LabWindows/CVICompatibility: | LabWindows/CVI 8.5 and later |

<!--NI_TOPIC bundle=labwindows-cvi path=cvi/uiref/cviattrtooltiptextlength_tree item.htm language=enus -->
## TOPIC 00816: ATTR_TOOLTIP_TEXT_LENGTH (Tree Item)

- bundle_id: `labwindows-cvi`
- source_path: `cvi/uiref/cviattrtooltiptextlength_tree item.htm`
- source_url: https://docs-be.ni.com/bundle/labwindows-cvi/raw/resource/enus/cvi/uiref/cviattrtooltiptextlength_tree%20item.htm
- document_id: `labwindows-cvi`
- page_type: `leaf`
- content_type: ``

### ATTR_TOOLTIP_TEXT_LENGTH (Tree Item)

| Type: | Tree Item attribute |
| --- | --- |
| Description: | The number of bytes in the tree item tooltip. The length does not include the ASCII NUL byte. Use this value to determine the size of the buffer to pass when you call GetTreeItemAttribute and specify the ATTR_TOOLTIP_TEXT attribute. Using this in GetTreeItemAttribute or SetTreeItemAttribute is equivalent to using it in GetTreeCellAttribute or SetTreeCellAttribute if you pass zero for the column index. |
| Restrictions: | Not settable. |
| Data Type: | integer |
| LabWindows/CVICompatibility: | LabWindows/CVI 8.5 and later |

<!--NI_TOPIC bundle=labwindows-cvi path=cvi/uiref/cviattrtop_control.htm language=enus -->
## TOPIC 00817: ATTR_TOP (Control)

- bundle_id: `labwindows-cvi`
- source_path: `cvi/uiref/cviattrtop_control.htm`
- source_url: https://docs-be.ni.com/bundle/labwindows-cvi/raw/resource/enus/cvi/uiref/cviattrtop_control.htm
- document_id: `labwindows-cvi`
- page_type: `leaf`
- content_type: ``

### ATTR_TOP (Control)

| Type: | Control attribute |
| --- | --- |
| Description: | The vertical offset in pixels of the control relative to the origin of the panel. The panel origin (0,0) is the upper-left corner of the panel below the title bar and to right of the panel frame. |
| Control Types: | ActiveX controls, binary switches, canvases, color numerics, command buttons, decorations, digital graphs, graphs, LEDs, list boxes, numerics, picture buttons, picture rings, pictures, radio buttons, rings, numeric slides, ring slides, splitters, strings, strip charts, tab controls, tables, text boxes, text buttons, text messages, timers, toggle buttons, trees. |
| Data Type: | integer |
| Valid Range: | -32768 to 32767 |
| LabWindows/CVICompatibility: | LabWindows/CVI 3.0 and later |

<!--NI_TOPIC bundle=labwindows-cvi path=cvi/uiref/cviattrtop_monitor.htm language=enus -->
## TOPIC 00818: ATTR_TOP (Monitor)

- bundle_id: `labwindows-cvi`
- source_path: `cvi/uiref/cviattrtop_monitor.htm`
- source_url: https://docs-be.ni.com/bundle/labwindows-cvi/raw/resource/enus/cvi/uiref/cviattrtop_monitor.htm
- document_id: `labwindows-cvi`
- page_type: `leaf`
- content_type: ``

### ATTR_TOP (Monitor)

| Type: | Monitor attribute |
| --- | --- |
| Description: | The vertical position (in pixels) of the top of the work area of the monitor. The work area is the portion of the screen not obscured by the taskbar. The position is relative to the origin of the virtual desktop (the upper-left corner of the primary monitor). |
| Restrictions: | Not settable. |
| Data Type: | integer |
| LabWindows/CVICompatibility: | LabWindows/CVI 5.5 and later |

<!--NI_TOPIC bundle=labwindows-cvi path=cvi/uiref/cviattrtop_panel.htm language=enus -->
## TOPIC 00819: ATTR_TOP (Panel)

- bundle_id: `labwindows-cvi`
- source_path: `cvi/uiref/cviattrtop_panel.htm`
- source_url: https://docs-be.ni.com/bundle/labwindows-cvi/raw/resource/enus/cvi/uiref/cviattrtop_panel.htm
- document_id: `labwindows-cvi`
- page_type: `leaf`
- content_type: ``

### ATTR_TOP (Panel)

| Type: | Panel attribute |
| --- | --- |
| Description: | The vertical offset (in pixels) of the panel relative to the origin of the screen (for top-level windows) or the parent panel (for child panels). The screen origin is the upper-left corner of the screen. The origin of a parent panel is the upper-left corner of the panel below the title bar and to the right of the panel frame. |
| Data Type: | integer |
| Valid Range: | -32768 to 32767, or VAL_AUTO_CENTER |
| LabWindows/CVICompatibility: | LabWindows/CVI 3.0 and later |

##### Values

| VAL_AUTO_CENTER | Center the panel on the screen or within the parent panel. |
| --- | --- |

<!--NI_TOPIC bundle=labwindows-cvi path=cvi/uiref/cviattrtopactualrange.htm language=enus -->
## TOPIC 00820: ATTR_TOP_ACTUAL_RANGE

- bundle_id: `labwindows-cvi`
- source_path: `cvi/uiref/cviattrtopactualrange.htm`
- source_url: https://docs-be.ni.com/bundle/labwindows-cvi/raw/resource/enus/cvi/uiref/cviattrtopactualrange.htm
- document_id: `labwindows-cvi`
- page_type: `leaf`
- content_type: ``

### ATTR_TOP_ACTUAL_RANGE

| Type: | Control attribute |
| --- | --- |
| Description: | Use this attribute to obtain the effective topmost range of the splitter control. Several factors determine this value, such as the setting of the ATTR_TOP_RANGE attribute, the type, size, and position of controls you have attached to the top edge of the splitter, and in what mode they are attached. |
| Control Types: | Splitters. |
| Restrictions: | Not settable. Not valid for vertical splitters |
| Data Type: | integer |
| Valid Range: | -32768 to 32767 |
| LabWindows/CVICompatibility: | LabWindows/CVI 7.1 and later |

<!--NI_TOPIC bundle=labwindows-cvi path=cvi/uiref/cviattrtoprange.htm language=enus -->
## TOPIC 00821: ATTR_TOP_RANGE

- bundle_id: `labwindows-cvi`
- source_path: `cvi/uiref/cviattrtoprange.htm`
- source_url: https://docs-be.ni.com/bundle/labwindows-cvi/raw/resource/enus/cvi/uiref/cviattrtoprange.htm
- document_id: `labwindows-cvi`
- page_type: `leaf`
- content_type: ``

### ATTR_TOP_RANGE

| Type: | Control attribute |
| --- | --- |
| Description: | This is one of four attributes that define the range of motion of the splitter control. You can allow LabWindows/CVI to automatically set this range using the rules below, or you can define your own range. You can also choose to not enforce a range by setting the attribute to VAL_NO_RANGE_LIMIT. The default range rules are as follows: the splitter control can be moved up to the point where the far edge of any attached controls or panels that are attached in "move" mode would reach the far edge of the panel, or up to the point where the splitter itself would reach the panel edge, whichever comes first. Regardless of whether you use the default range, or set your own range, splitters cannot be moved past the point where any control or panel that is attached to the splitter in "size" mode is reduced to its standard minimum size (this varies according to control type). You specify values for this attribute using panel coordinates, relative to the top/left corner of the panel. |
| Control Types: | Splitters. |
| Restrictions: | Not valid for vertical splitters |
| Data Type: | integer |
| Valid Range: | -32768 to 32767, or VAL_AUTO_RANGE, or VAL_NO_RANGE_LIMIT |
| Default Value: | VAL_AUTO_RANGE |
| LabWindows/CVICompatibility: | LabWindows/CVI 7.1 and later |

##### Values

| VAL_AUTO_RANGE | Set this value to allow LabWindows/CVI to automatically determine the range of motion of splitter controls. |
| --- | --- |
| VAL_NO_RANGE_LIMIT | Set this value if you don't want LabWindows/CVI to impose a range of motion on splitter controls. Note: even if you set this value, you cannot move splitters past the point where any control or panel that is attached to the splitter in "size" mode is reduced to its standard minimum size (this varies according to control type) |

<!--NI_TOPIC bundle=labwindows-cvi path=cvi/uiref/cviattrtotallines.htm language=enus -->
## TOPIC 00822: ATTR_TOTAL_LINES

- bundle_id: `labwindows-cvi`
- source_path: `cvi/uiref/cviattrtotallines.htm`
- source_url: https://docs-be.ni.com/bundle/labwindows-cvi/raw/resource/enus/cvi/uiref/cviattrtotallines.htm
- document_id: `labwindows-cvi`
- page_type: `leaf`
- content_type: ``

### ATTR_TOTAL_LINES

| Type: | Control attribute |
| --- | --- |
| Description: | The total number of lines of text that are currently retained by the text box control. |
| Control Types: | Text boxes. |
| Restrictions: | Not settable. |
| Data Type: | integer |
| LabWindows/CVICompatibility: | LabWindows/CVI 3.0 and later |

<!--NI_TOPIC bundle=labwindows-cvi path=cvi/uiref/cviattrtracebgcolor.htm language=enus -->
## TOPIC 00823: ATTR_TRACE_BGCOLOR

- bundle_id: `labwindows-cvi`
- source_path: `cvi/uiref/cviattrtracebgcolor.htm`
- source_url: https://docs-be.ni.com/bundle/labwindows-cvi/raw/resource/enus/cvi/uiref/cviattrtracebgcolor.htm
- document_id: `labwindows-cvi`
- page_type: `leaf`
- content_type: ``

### ATTR_TRACE_BGCOLOR

| Type: | Plot attribute |
| --- | --- |
| Description: | The RGB color value for the background text of a text plot, or the fill color for a geometric plot. An RGB value is a 4-byte integer with the hexadecimal format 0x00RRGGBB. RR, GG, and BB are the respective red, green, and blue components of the color value. See MakeColor. |
| Plot Types: | Arc, oval, polygon, rectangle, text. |
| Data Type: | integer |
| LabWindows/CVICompatibility: | LabWindows/CVI 4.0 and later |

##### Values

| VAL_RED | Red = 255, Green = 0, Blue = 0 |
| --- | --- |
| VAL_GREEN | Red = 0, Green = 255, Blue = 0 |
| VAL_BLUE | Red = 0, Green = 0, Blue = 255 |
| VAL_CYAN | Red = 0, Green = 255, Blue = 255 |
| VAL_MAGENTA | Red = 255, Green = 0, Blue = 255 |
| VAL_YELLOW | Red = 255, Green = 255, Blue = 0 |
| VAL_DK_RED | Red = 128, Green = 0, Blue = 0 |
| VAL_DK_BLUE | Red = 0, Green = 0, Blue = 128 |
| VAL_DK_GREEN | Red = 0, Green = 128, Blue = 0 |
| VAL_DK_CYAN | Red = 0, Green = 128, Blue = 128 |
| VAL_DK_MAGENTA | Red = 128, Green = 0, Blue = 128 |
| VAL_DK_YELLOW | Red = 128, Green = 128, Blue = 0 |
| VAL_LT_GRAY | Red = 192, Green = 192, Blue = 192 |
| VAL_DK_GRAY | Red = 128, Green = 128, Blue = 128 |
| VAL_BLACK | Red = 0, Green = 0, Blue = 0 |
| VAL_WHITE | Red = 255, Green = 255, Blue = 255 |
| VAL_GRAY | Red = 160, Green = 160, Blue = 160 |
| VAL_OFFWHITE | Red = 224, Green = 224, Blue = 224 |
| VAL_TRANSPARENT | Red = 0, Green = 0, Blue = 0, transparent bit set. |
| VAL_PANEL_GRAY | Red = 192, Green = 192, Blue = 192 |

<!--NI_TOPIC bundle=labwindows-cvi path=cvi/uiref/cviattrtracecolor_plot.htm language=enus -->
## TOPIC 00824: ATTR_TRACE_COLOR (Plot)

- bundle_id: `labwindows-cvi`
- source_path: `cvi/uiref/cviattrtracecolor_plot.htm`
- source_url: https://docs-be.ni.com/bundle/labwindows-cvi/raw/resource/enus/cvi/uiref/cviattrtracecolor_plot.htm
- document_id: `labwindows-cvi`
- page_type: `leaf`
- content_type: ``

### ATTR_TRACE_COLOR (Plot)

| Type: | Plot attribute |
| --- | --- |
| Description: | The RGB color value for the plot on the graph. An RGB value is a 4-byte integer with the hexadecimal format 0x00RRGGBB. RR, GG, and BB are the respective red, green, and blue components of the color value. See MakeColor. |
| Plot Types: | Arc, line, oval, point, polygon, rectangle, text, waveform, X, XY, Y. |
| Data Type: | integer |
| LabWindows/CVICompatibility: | LabWindows/CVI 4.0 and later |

##### Values

| VAL_RED | Red = 255, Green = 0, Blue = 0 |
| --- | --- |
| VAL_GREEN | Red = 0, Green = 255, Blue = 0 |
| VAL_BLUE | Red = 0, Green = 0, Blue = 255 |
| VAL_CYAN | Red = 0, Green = 255, Blue = 255 |
| VAL_MAGENTA | Red = 255, Green = 0, Blue = 255 |
| VAL_YELLOW | Red = 255, Green = 255, Blue = 0 |
| VAL_DK_RED | Red = 128, Green = 0, Blue = 0 |
| VAL_DK_BLUE | Red = 0, Green = 0, Blue = 128 |
| VAL_DK_GREEN | Red = 0, Green = 128, Blue = 0 |
| VAL_DK_CYAN | Red = 0, Green = 128, Blue = 128 |
| VAL_DK_MAGENTA | Red = 128, Green = 0, Blue = 128 |
| VAL_DK_YELLOW | Red = 128, Green = 128, Blue = 0 |
| VAL_LT_GRAY | Red = 192, Green = 192, Blue = 192 |
| VAL_DK_GRAY | Red = 128, Green = 128, Blue = 128 |
| VAL_BLACK | Red = 0, Green = 0, Blue = 0 |
| VAL_WHITE | Red = 255, Green = 255, Blue = 255 |
| VAL_GRAY | Red = 160, Green = 160, Blue = 160 |
| VAL_OFFWHITE | Red = 224, Green = 224, Blue = 224 |
| VAL_TRANSPARENT | Red = 0, Green = 0, Blue = 0, transparent bit set. |
| VAL_PANEL_GRAY | Red = 192, Green = 192, Blue = 192 |

<!--NI_TOPIC bundle=labwindows-cvi path=cvi/uiref/cviattrtracecolor_trace.htm language=enus -->
## TOPIC 00825: ATTR_TRACE_COLOR (Trace)

- bundle_id: `labwindows-cvi`
- source_path: `cvi/uiref/cviattrtracecolor_trace.htm`
- source_url: https://docs-be.ni.com/bundle/labwindows-cvi/raw/resource/enus/cvi/uiref/cviattrtracecolor_trace.htm
- document_id: `labwindows-cvi`
- page_type: `leaf`
- content_type: ``

### ATTR_TRACE_COLOR (Trace)

| Type: | Trace attribute |
| --- | --- |
| Description: | The RGB color value for the trace on the strip chart. An RGB value is a 4-byte integer with the hexadecimal format 0x00RRGGBB. RR, GG, and BB are the respective red, green, and blue components of the color value. See MakeColor. |
| Data Type: | integer |
| LabWindows/CVICompatibility: | LabWindows/CVI 3.0 and later |

##### Values

| VAL_RED | Red = 255, Green = 0, Blue = 0 |
| --- | --- |
| VAL_GREEN | Red = 0, Green = 255, Blue = 0 |
| VAL_BLUE | Red = 0, Green = 0, Blue = 255 |
| VAL_CYAN | Red = 0, Green = 255, Blue = 255 |
| VAL_MAGENTA | Red = 255, Green = 0, Blue = 255 |
| VAL_YELLOW | Red = 255, Green = 255, Blue = 0 |
| VAL_DK_RED | Red = 128, Green = 0, Blue = 0 |
| VAL_DK_BLUE | Red = 0, Green = 0, Blue = 128 |
| VAL_DK_GREEN | Red = 0, Green = 128, Blue = 0 |
| VAL_DK_CYAN | Red = 0, Green = 128, Blue = 128 |
| VAL_DK_MAGENTA | Red = 128, Green = 0, Blue = 128 |
| VAL_DK_YELLOW | Red = 128, Green = 128, Blue = 0 |
| VAL_LT_GRAY | Red = 192, Green = 192, Blue = 192 |
| VAL_DK_GRAY | Red = 128, Green = 128, Blue = 128 |
| VAL_BLACK | Red = 0, Green = 0, Blue = 0 |
| VAL_WHITE | Red = 255, Green = 255, Blue = 255 |
| VAL_GRAY | Red = 160, Green = 160, Blue = 160 |
| VAL_OFFWHITE | Red = 224, Green = 224, Blue = 224 |
| VAL_PANEL_GRAY | Red = 192, Green = 192, Blue = 192 |

<!--NI_TOPIC bundle=labwindows-cvi path=cvi/uiref/cviattrtracelgfont.htm language=enus -->
## TOPIC 00826: ATTR_TRACE_LG_FONT

- bundle_id: `labwindows-cvi`
- source_path: `cvi/uiref/cviattrtracelgfont.htm`
- source_url: https://docs-be.ni.com/bundle/labwindows-cvi/raw/resource/enus/cvi/uiref/cviattrtracelgfont.htm
- document_id: `labwindows-cvi`
- page_type: `leaf`
- content_type: ``

### ATTR_TRACE_LG_FONT

| Type: | Trace attribute |
| --- | --- |
| Description: | The name of the font for the text string that describes the trace in the strip chart legend. To determine the size of the buffer to pass when you are obtaining the font name, call GetTraceAttribute and specify the ATTR_TRACE_LG_FONT_NAME_LENGTH attribute. You can use a LabWindows/CVI-supplied font; any host font—such as Arial or Courier—supported on your system; or a user-defined metafont saved by a previous call to functions such as CreateMetaFont and CreateMetaFontEx. Always set the font before setting the size or style. Note: You must use SetTraceAttributeEx to set this attribute. |
| Data Type: | string |
| Default Value: | VAL_DIALOG_META_FONT |
| LabWindows/CVICompatibility: | LabWindows/CVI 8.5 and later |

##### Values

| VAL_MENU_FONT | Default font style for LabWindows/CVI menus. This font contains typeface information only. This value is an alias to an operating system font. Therefore, the operating system and user preferences on your machine determine this font style. |
| --- | --- |
| VAL_DIALOG_FONT | Default font style for LabWindows/CVI dialog boxes and control text. This font contains typeface information only. This value is an alias to an operating system font. Therefore, the operating system and user preferences on your machine determine this font style. |
| VAL_EDITOR_FONT | Default font style for the LabWindows/CVI Source window. This font contains typeface information only. This value is an alias to an operating system font. Therefore, the operating system and user preferences on your machine determine this font style. |
| VAL_APP_FONT | Default font style for the LabWindows/CVI Workspace window. This font contains typeface information only. This value is an alias to an operating system font. Therefore, the operating system and user preferences on your machine determine this font style. |
| VAL_MESSAGE_BOX_FONT | Default font style for LabWindows/CVI message boxes. This font contains typeface information only. This value is an alias to an operating system font. Therefore, the operating system and user preferences on your machine determine this font style. |
| VAL_MENU_META_FONT | Default font for LabWindows/CVI menus. Metafonts contain typeface information, point size, and text styles such as bold, shadow outline, underline, italics, and strikeout. Because metafonts contain character size information, strings that use metafonts are more likely to have the same width across platforms. This value is an alias to an operating system font. Therefore, the operating system and user preferences on your machine determine this font. |
| VAL_DIALOG_META_FONT | Default font for LabWindows/CVI dialog boxes and control text. Metafonts contain typeface information, point size, and text styles such as bold, shadow outline, underline, italics, and strikeout. Because metafonts contain character size information, strings that use metafonts are more likely to have the same width across platforms. This value is an alias to an operating system font. Therefore, the operating system and user preferences on your machine determine this font. |
| VAL_EDITOR_META_FONT | Default font for the LabWindows/CVI Source window. Metafonts contain typeface information, point size, and text styles such as bold, shadow outline, underline, italics, and strikeout. Because metafonts contain character size information, strings that use metafonts are more likely to have the same width across platforms. This value is an alias to an operating system font. Therefore, the operating system and user preferences on your machine determine this font. |
| VAL_APP_META_FONT | Default font for the LabWindows/CVI Workspace window. Metafonts contain typeface information, point size, and text styles such as bold, shadow outline, underline, italics, and strikeout. Because metafonts contain character size information, strings that use metafonts are more likely to have the same width across platforms. This value is an alias to an operating system font. Therefore, the operating system and user preferences on your machine determine this font. |
| VAL_MESSAGE_BOX_META_FONT | Default font for LabWindows/CVI message boxes. Metafonts contain typeface information, point size, and text styles such as bold, shadow outline, underline, italics, and strikeout. Because metafonts contain character size information, strings that use metafonts are more likely to have the same width across platforms. This value is an alias to an operating system font. Therefore, the operating system and user preferences on your machine determine this font. |
| VAL_7SEG_META_FONT | Font that provides compatibility with LabWindows for DOS. Metafonts contain typeface information, point size, and text styles such as bold, shadow outline, underline, italics, and strikeout. Because metafonts contain character size information, strings that use metafonts are more likely to have the same width across platforms. |
| VAL_SYSTEM_META_FONT | Font that provides compatibility with function panels and user interface panels from LabWindows for DOS that use extended IBM PC characters. Because other fonts may not contain these extended characters, cut/paste operations may fail. Metafonts contain typeface information, point size, and text styles such as bold, shadow outline, underline, italics, and strikeout. Because metafonts contain character size information, strings that use metafonts are more likely to have the same width across platforms. |

<!--NI_TOPIC bundle=labwindows-cvi path=cvi/uiref/cviattrtracelgfontnamelength.htm language=enus -->
## TOPIC 00827: ATTR_TRACE_LG_FONT_NAME_LENGTH

- bundle_id: `labwindows-cvi`
- source_path: `cvi/uiref/cviattrtracelgfontnamelength.htm`
- source_url: https://docs-be.ni.com/bundle/labwindows-cvi/raw/resource/enus/cvi/uiref/cviattrtracelgfontnamelength.htm
- document_id: `labwindows-cvi`
- page_type: `leaf`
- content_type: ``

### ATTR_TRACE_LG_FONT_NAME_LENGTH

| Type: | Trace attribute |
| --- | --- |
| Description: | The number of bytes in the name of the font for the text string that describes the trace in the strip chart legend. The length does not include the ASCII NUL byte. Use this value to determine the size of the buffer to pass when you call GetTraceAttribute and specify the ATTR_TRACE_LG_FONT attribute. |
| Restrictions: | Not settable. |
| Data Type: | integer |
| LabWindows/CVICompatibility: | LabWindows/CVI 8.5 and later |

<!--NI_TOPIC bundle=labwindows-cvi path=cvi/uiref/cviattrtracelgtext.htm language=enus -->
## TOPIC 00828: ATTR_TRACE_LG_TEXT

- bundle_id: `labwindows-cvi`
- source_path: `cvi/uiref/cviattrtracelgtext.htm`
- source_url: https://docs-be.ni.com/bundle/labwindows-cvi/raw/resource/enus/cvi/uiref/cviattrtracelgtext.htm
- document_id: `labwindows-cvi`
- page_type: `leaf`
- content_type: ``

### ATTR_TRACE_LG_TEXT

| Type: | Trace attribute |
| --- | --- |
| Description: | The text string that describes the trace in the strip chart legend. To determine the size of the buffer to pass when you are obtaining the text, call GetTraceAttribute and specify the ATTR_TRACE_LG_TEXT_LENGTH attribute. Note: You must use SetTraceAttributeEx to set this attribute. |
| Data Type: | string |
| Default Value: | "Trace xx" where xx is the index of this trace |
| LabWindows/CVICompatibility: | LabWindows/CVI 8.5 and later |

<!--NI_TOPIC bundle=labwindows-cvi path=cvi/uiref/cviattrtracelgtextcolor.htm language=enus -->
## TOPIC 00829: ATTR_TRACE_LG_TEXT_COLOR

- bundle_id: `labwindows-cvi`
- source_path: `cvi/uiref/cviattrtracelgtextcolor.htm`
- source_url: https://docs-be.ni.com/bundle/labwindows-cvi/raw/resource/enus/cvi/uiref/cviattrtracelgtextcolor.htm
- document_id: `labwindows-cvi`
- page_type: `leaf`
- content_type: ``

### ATTR_TRACE_LG_TEXT_COLOR

| Type: | Trace attribute |
| --- | --- |
| Description: | The RGB color of the string that describes the trace in the strip chart legend. An RGB value is a 4-byte integer with the hexadecimal format 0x00RRGGBB. RR, GG, and BB are the respective red, green, and blue components of the color value. See MakeColor. |
| Data Type: | integer |
| LabWindows/CVICompatibility: | LabWindows/CVI 8.5 and later |

##### Values

| VAL_RED | Red = 255, Green = 0, Blue = 0 |
| --- | --- |
| VAL_GREEN | Red = 0, Green = 255, Blue = 0 |
| VAL_BLUE | Red = 0, Green = 0, Blue = 255 |
| VAL_CYAN | Red = 0, Green = 255, Blue = 255 |
| VAL_MAGENTA | Red = 255, Green = 0, Blue = 255 |
| VAL_YELLOW | Red = 255, Green = 255, Blue = 0 |
| VAL_DK_RED | Red = 128, Green = 0, Blue = 0 |
| VAL_DK_BLUE | Red = 0, Green = 0, Blue = 128 |
| VAL_DK_GREEN | Red = 0, Green = 128, Blue = 0 |
| VAL_DK_CYAN | Red = 0, Green = 128, Blue = 128 |
| VAL_DK_MAGENTA | Red = 128, Green = 0, Blue = 128 |
| VAL_DK_YELLOW | Red = 128, Green = 128, Blue = 0 |
| VAL_LT_GRAY | Red = 192, Green = 192, Blue = 192 |
| VAL_DK_GRAY | Red = 128, Green = 128, Blue = 128 |
| VAL_BLACK | Red = 0, Green = 0, Blue = 0 |
| VAL_WHITE | Red = 255, Green = 255, Blue = 255 |
| VAL_GRAY | Red = 160, Green = 160, Blue = 160 |
| VAL_OFFWHITE | Red = 224, Green = 224, Blue = 224 |
| VAL_TRANSPARENT | Red = 0, Green = 0, Blue = 0, transparent bit set. |
| VAL_PANEL_GRAY | Red = 192, Green = 192, Blue = 192 |

<!--NI_TOPIC bundle=labwindows-cvi path=cvi/uiref/cviattrtracelgtextlength.htm language=enus -->
## TOPIC 00830: ATTR_TRACE_LG_TEXT_LENGTH

- bundle_id: `labwindows-cvi`
- source_path: `cvi/uiref/cviattrtracelgtextlength.htm`
- source_url: https://docs-be.ni.com/bundle/labwindows-cvi/raw/resource/enus/cvi/uiref/cviattrtracelgtextlength.htm
- document_id: `labwindows-cvi`
- page_type: `leaf`
- content_type: ``

### ATTR_TRACE_LG_TEXT_LENGTH

| Type: | Trace attribute |
| --- | --- |
| Description: | The number of bytes in the text string that describes the trace in the strip chart legend. The length does not include the ASCII NUL byte. Use this value to determine the size of the buffer to pass when you call GetTraceAttribute and specify the ATTR_TRACE_LG_TEXT attribute. |
| Restrictions: | Not settable. |
| Data Type: | integer |
| LabWindows/CVICompatibility: | LabWindows/CVI 8.5 and later |

<!--NI_TOPIC bundle=labwindows-cvi path=cvi/uiref/cviattrtracelgvisible.htm language=enus -->
## TOPIC 00831: ATTR_TRACE_LG_VISIBLE

- bundle_id: `labwindows-cvi`
- source_path: `cvi/uiref/cviattrtracelgvisible.htm`
- source_url: https://docs-be.ni.com/bundle/labwindows-cvi/raw/resource/enus/cvi/uiref/cviattrtracelgvisible.htm
- document_id: `labwindows-cvi`
- page_type: `leaf`
- content_type: ``

### ATTR_TRACE_LG_VISIBLE

| Type: | Trace attribute |
| --- | --- |
| Description: | Specifies whether the strip chart legend shows an item corresponding to this trace. By default, the strip chart legend displays only the first trace. Use this attribute to specify other traces to display in the legend. |
| Data Type: | integer |
| LabWindows/CVICompatibility: | LabWindows/CVI 8.5 and later |

##### Values

| 0 | False |
| --- | --- |
| 1 | True |

<!--NI_TOPIC bundle=labwindows-cvi path=cvi/uiref/cviattrtraceopacity.htm language=enus -->
## TOPIC 00832: ATTR_TRACE_OPACITY

- bundle_id: `labwindows-cvi`
- source_path: `cvi/uiref/cviattrtraceopacity.htm`
- source_url: https://docs-be.ni.com/bundle/labwindows-cvi/raw/resource/enus/cvi/uiref/cviattrtraceopacity.htm
- document_id: `labwindows-cvi`
- page_type: `leaf`
- content_type: ``

### ATTR_TRACE_OPACITY

| Type: | Trace attribute |
| --- | --- |
| Description: | The level of opacity for the trace on the strip chart, with 0 being full transparency and 255 being full opacity. You can specify the opacity for VAL_THIN_LINE and VAL_FAT_LINE. All other trace styles draw with opacity set to 255. |
| Data Type: | integer |
| Valid Range: | 0 to 255 |
| Default Value: | 255 |
| LabWindows/CVICompatibility: | LabWindows/CVI 2013 and later |

<!--NI_TOPIC bundle=labwindows-cvi path=cvi/uiref/cviattrtracepointstyle_plot.htm language=enus -->
## TOPIC 00833: ATTR_TRACE_POINT_STYLE (Plot)

- bundle_id: `labwindows-cvi`
- source_path: `cvi/uiref/cviattrtracepointstyle_plot.htm`
- source_url: https://docs-be.ni.com/bundle/labwindows-cvi/raw/resource/enus/cvi/uiref/cviattrtracepointstyle_plot.htm
- document_id: `labwindows-cvi`
- page_type: `leaf`
- content_type: ``

### ATTR_TRACE_POINT_STYLE (Plot)

| Type: | Plot attribute |
| --- | --- |
| Description: | The point style for the plot on the graph. |
| Plot Types: | Point, waveform, X, XY, Y. |
| Data Type: | integer |
| LabWindows/CVICompatibility: | LabWindows/CVI 4.0 and later |

##### Values

| VAL_EMPTY_SQUARE | An empty square. |
| --- | --- |
| VAL_SOLID_SQUARE | A solid square. |
| VAL_ASTERISK | An asterisk type character. |
| VAL_DOTTED_EMPTY_SQUARE | An empty square with a dot in its center. |
| VAL_DOTTED_SOLID_SQUARE | A solid square with a dot in its center. |
| VAL_SOLID_DIAMOND | A diamond shape (similar to a cross). |
| VAL_EMPTY_SQUARE_WITH_X | An empty square with an x-like shape in its center. |
| VAL_EMPTY_SQUARE_WITH_CROSS | An empty square with a cross in its center. |
| VAL_BOLD_X | A bold x-like shape. |
| VAL_SMALL_SOLID_SQUARE | A small solid square. |
| VAL_SIMPLE_DOT | A small dot. |
| VAL_EMPTY_CIRCLE | An empty circle. |
| VAL_SOLID_CIRCLE | A solid circle. |
| VAL_DOTTED_SOLID_CIRCLE | A circle with a dot in its center. |
| VAL_DOTTED_EMPTY_CIRCLE | A solid circle with a dot in its center. |
| VAL_BOLD_CROSS | A bold cross of equal height and width. |
| VAL_CROSS | A cross of equal height and width. |
| VAL_SMALL_CROSS | A small cross of equal height and width. |
| VAL_X | An x-like shape. |
| VAL_SMALL_X | A small x-like shape. |
| VAL_DOTTED_SOLID_DIAMOND | A solid diamond shape with a dot in its center. |
| VAL_EMPTY_DIAMOND | An empty diamond shape. |
| VAL_DOTTED_EMPTY_DIAMOND | An empty solid diamond shape with a dot in its center. |
| VAL_SMALL_EMPTY_SQUARE | A small empty square. |
| VAL_NO_POINT | No cursor point. |

<!--NI_TOPIC bundle=labwindows-cvi path=cvi/uiref/cviattrtracepointstyle_trace.htm language=enus -->
## TOPIC 00834: ATTR_TRACE_POINT_STYLE (Trace)

- bundle_id: `labwindows-cvi`
- source_path: `cvi/uiref/cviattrtracepointstyle_trace.htm`
- source_url: https://docs-be.ni.com/bundle/labwindows-cvi/raw/resource/enus/cvi/uiref/cviattrtracepointstyle_trace.htm
- document_id: `labwindows-cvi`
- page_type: `leaf`
- content_type: ``

### ATTR_TRACE_POINT_STYLE (Trace)

| Type: | Trace attribute |
| --- | --- |
| Description: | The point style for the trace on the strip chart. |
| Data Type: | integer |
| Default Value: | VAL_EMPTY_SQUARE_WITH_CROSS |
| LabWindows/CVICompatibility: | LabWindows/CVI 3.0 and later |

##### Values

| VAL_EMPTY_SQUARE | An empty square. |
| --- | --- |
| VAL_SOLID_SQUARE | A solid square. |
| VAL_ASTERISK | An asterisk type character. |
| VAL_DOTTED_EMPTY_SQUARE | An empty square with a dot in its center. |
| VAL_DOTTED_SOLID_SQUARE | A solid square with a dot in its center. |
| VAL_SOLID_DIAMOND | A diamond shape (similar to a cross). |
| VAL_EMPTY_SQUARE_WITH_X | An empty square with an x-like shape in its center. |
| VAL_EMPTY_SQUARE_WITH_CROSS | An empty square with a cross in its center. |
| VAL_BOLD_X | A bold x-like shape. |
| VAL_SMALL_SOLID_SQUARE | A small solid square. |
| VAL_SIMPLE_DOT | A small dot. |
| VAL_EMPTY_CIRCLE | An empty circle. |
| VAL_SOLID_CIRCLE | A solid circle. |
| VAL_DOTTED_SOLID_CIRCLE | A circle with a dot in its center. |
| VAL_DOTTED_EMPTY_CIRCLE | A solid circle with a dot in its center. |
| VAL_BOLD_CROSS | A bold cross of equal height and width. |
| VAL_CROSS | A cross of equal height and width. |
| VAL_SMALL_CROSS | A small cross of equal height and width. |
| VAL_X | An x-like shape. |
| VAL_SMALL_X | A small x-like shape. |
| VAL_DOTTED_SOLID_DIAMOND | A solid diamond shape with a dot in its center. |
| VAL_EMPTY_DIAMOND | An empty diamond shape. |
| VAL_DOTTED_EMPTY_DIAMOND | An empty solid diamond shape with a dot in its center. |
| VAL_SMALL_EMPTY_SQUARE | A small empty square. |
| VAL_NO_POINT | No cursor point. |

<!--NI_TOPIC bundle=labwindows-cvi path=cvi/uiref/cviattrtracethickness.htm language=enus -->
## TOPIC 00835: ATTR_TRACE_THICKNESS

- bundle_id: `labwindows-cvi`
- source_path: `cvi/uiref/cviattrtracethickness.htm`
- source_url: https://docs-be.ni.com/bundle/labwindows-cvi/raw/resource/enus/cvi/uiref/cviattrtracethickness.htm
- document_id: `labwindows-cvi`
- page_type: `leaf`
- content_type: ``

### ATTR_TRACE_THICKNESS

| Type: | Trace attribute |
| --- | --- |
| Description: | The thickness of the trace line, in pixels. Applies only when ATTR_LINE_STYLE is VAL_SOLID. If ATTR_PLOT_STYLE is VAL_FAT_LINE or VAL_FAT_STEP, the plot is drawn with three times the thickness specified in this attribute. |
| Data Type: | integer |
| Valid Range: | 1 to 32 |
| Default Value: | 1 |
| LabWindows/CVICompatibility: | LabWindows/CVI 9.0 and later |

<!--NI_TOPIC bundle=labwindows-cvi path=cvi/uiref/cviattrtracevisible_plot.htm language=enus -->
## TOPIC 00836: ATTR_TRACE_VISIBLE (Plot)

- bundle_id: `labwindows-cvi`
- source_path: `cvi/uiref/cviattrtracevisible_plot.htm`
- source_url: https://docs-be.ni.com/bundle/labwindows-cvi/raw/resource/enus/cvi/uiref/cviattrtracevisible_plot.htm
- document_id: `labwindows-cvi`
- page_type: `leaf`
- content_type: ``

### ATTR_TRACE_VISIBLE (Plot)

| Type: | Plot attribute |
| --- | --- |
| Description: | Specifies whether the plot is visible. 0 = Not visible 1 = Visible |
| Plot Types: | Arc, bitmap, intensity, line, oval, point, polygon, rectangle, scaled intensity, text, waveform, X, XY, Y. |
| Data Type: | integer |
| Default Value: | 1 |
| LabWindows/CVICompatibility: | LabWindows/CVI 4.0 and later |

##### Values

| 0 | False |
| --- | --- |
| 1 | True |

<!--NI_TOPIC bundle=labwindows-cvi path=cvi/uiref/cviattrtracevisible_trace.htm language=enus -->
## TOPIC 00837: ATTR_TRACE_VISIBLE (Trace)

- bundle_id: `labwindows-cvi`
- source_path: `cvi/uiref/cviattrtracevisible_trace.htm`
- source_url: https://docs-be.ni.com/bundle/labwindows-cvi/raw/resource/enus/cvi/uiref/cviattrtracevisible_trace.htm
- document_id: `labwindows-cvi`
- page_type: `leaf`
- content_type: ``

### ATTR_TRACE_VISIBLE (Trace)

| Type: | Trace attribute |
| --- | --- |
| Description: | Specifies whether the trace line is visible. 0 = Not visible 1 = Visible |
| Data Type: | integer |
| Default Value: | 1 |
| LabWindows/CVICompatibility: | LabWindows/CVI 3.0 and later |

##### Values

| 0 | False |
| --- | --- |
| 1 | True |

<!--NI_TOPIC bundle=labwindows-cvi path=cvi/uiref/cviattrtraceyaxis.htm language=enus -->
## TOPIC 00838: ATTR_TRACE_YAXIS

- bundle_id: `labwindows-cvi`
- source_path: `cvi/uiref/cviattrtraceyaxis.htm`
- source_url: https://docs-be.ni.com/bundle/labwindows-cvi/raw/resource/enus/cvi/uiref/cviattrtraceyaxis.htm
- document_id: `labwindows-cvi`
- page_type: `leaf`
- content_type: ``

### ATTR_TRACE_YAXIS

| Type: | Trace attribute |
| --- | --- |
| Description: | Specifies the y-axis with which the trace is associated. When you add new traces to the strip chart by setting ATTR_NUM_TRACES, the value of ATTR_ACTIVE_YAXIS determines the y-axis with which the new traces are associated. Afterward, you can change the association using ATTR_TRACE_YAXIS. |
| Data Type: | integer |
| LabWindows/CVICompatibility: | LabWindows/CVI 8.5 and later |

##### Values

| VAL_LEFT_YAXIS | The y-axis on the left side of the graph or strip chart. |
| --- | --- |
| VAL_RIGHT_YAXIS | The y-axis on the right side of the graph or strip chart. |

<!--NI_TOPIC bundle=labwindows-cvi path=cvi/uiref/cviattrtreebgcolor.htm language=enus -->
## TOPIC 00839: ATTR_TREE_BGCOLOR

- bundle_id: `labwindows-cvi`
- source_path: `cvi/uiref/cviattrtreebgcolor.htm`
- source_url: https://docs-be.ni.com/bundle/labwindows-cvi/raw/resource/enus/cvi/uiref/cviattrtreebgcolor.htm
- document_id: `labwindows-cvi`
- page_type: `leaf`
- content_type: ``

### ATTR_TREE_BGCOLOR

| Type: | Control attribute |
| --- | --- |
| Description: | The RGB color value in the portion of a tree not covered by tree items, cells, the scroll bars, or the column labels. An RGB value is a 4-byte integer with the hexadecimal format 0x00RRGGBB. RR, GG, and BB are the respective red, green, and blue components of the color value. See MakeColor. |
| Control Types: | Trees. |
| Data Type: | integer |
| LabWindows/CVICompatibility: | LabWindows/CVI 7.0 and later |

##### Values

| VAL_RED | Red = 255, Green = 0, Blue = 0 |
| --- | --- |
| VAL_GREEN | Red = 0, Green = 255, Blue = 0 |
| VAL_BLUE | Red = 0, Green = 0, Blue = 255 |
| VAL_CYAN | Red = 0, Green = 255, Blue = 255 |
| VAL_MAGENTA | Red = 255, Green = 0, Blue = 255 |
| VAL_YELLOW | Red = 255, Green = 255, Blue = 0 |
| VAL_DK_RED | Red = 128, Green = 0, Blue = 0 |
| VAL_DK_BLUE | Red = 0, Green = 0, Blue = 128 |
| VAL_DK_GREEN | Red = 0, Green = 128, Blue = 0 |
| VAL_DK_CYAN | Red = 0, Green = 128, Blue = 128 |
| VAL_DK_MAGENTA | Red = 128, Green = 0, Blue = 128 |
| VAL_DK_YELLOW | Red = 128, Green = 128, Blue = 0 |
| VAL_LT_GRAY | Red = 192, Green = 192, Blue = 192 |
| VAL_DK_GRAY | Red = 128, Green = 128, Blue = 128 |
| VAL_BLACK | Red = 0, Green = 0, Blue = 0 |
| VAL_WHITE | Red = 255, Green = 255, Blue = 255 |
| VAL_GRAY | Red = 160, Green = 160, Blue = 160 |
| VAL_OFFWHITE | Red = 224, Green = 224, Blue = 224 |
| VAL_TRANSPARENT | Red = 0, Green = 0, Blue = 0, transparent bit set. |
| VAL_PANEL_GRAY | Red = 192, Green = 192, Blue = 192 |

<!--NI_TOPIC bundle=labwindows-cvi path=cvi/uiref/cviattrtreeeditablecells.htm language=enus -->
## TOPIC 00840: ATTR_TREE_EDITABLE_CELLS

- bundle_id: `labwindows-cvi`
- source_path: `cvi/uiref/cviattrtreeeditablecells.htm`
- source_url: https://docs-be.ni.com/bundle/labwindows-cvi/raw/resource/enus/cvi/uiref/cviattrtreeeditablecells.htm
- document_id: `labwindows-cvi`
- page_type: `leaf`
- content_type: ``

### ATTR_TREE_EDITABLE_CELLS

| Type: | Control attribute |
| --- | --- |
| Description: | When enabled, the cells in the tree control are editable. This attribute does not affect cells in the first column. |
| Control Types: | Trees. |
| Data Type: | integer |
| Default Value: | 0 |
| LabWindows/CVICompatibility: | LabWindows/CVI 2009 and later |

##### Values

| 0 | False |
| --- | --- |
| 1 | True |

<!--NI_TOPIC bundle=labwindows-cvi path=cvi/uiref/cviattrtreerunstate_control.htm language=enus -->
## TOPIC 00841: ATTR_TREE_RUN_STATE (Control)

- bundle_id: `labwindows-cvi`
- source_path: `cvi/uiref/cviattrtreerunstate_control.htm`
- source_url: https://docs-be.ni.com/bundle/labwindows-cvi/raw/resource/enus/cvi/uiref/cviattrtreerunstate_control.htm
- document_id: `labwindows-cvi`
- page_type: `leaf`
- content_type: ``

### ATTR_TREE_RUN_STATE (Control)

| Type: | Control attribute |
| --- | --- |
| Description: | Allows programmatic control of the run state of the tree. |
| Control Types: | Trees. |
| Data Type: | integer |
| Default Value: | VAL_SELECT_STATE |
| LabWindows/CVICompatibility: | LabWindows/CVI 7.0 and later |

##### Values

| VAL_SELECT_STATE | The tree run state is set for item selection. |
| --- | --- |
| VAL_EDIT_STATE | The tree run state is set for item label editing. This state is not valid if the tree is empty, or if the active item/specified cell has ATTR_NO_EDIT_LABEL set. |

<!--NI_TOPIC bundle=labwindows-cvi path=cvi/uiref/cviattrtreerunstate_tree cell.htm language=enus -->
## TOPIC 00842: ATTR_TREE_RUN_STATE (Tree Cell)

- bundle_id: `labwindows-cvi`
- source_path: `cvi/uiref/cviattrtreerunstate_tree cell.htm`
- source_url: https://docs-be.ni.com/bundle/labwindows-cvi/raw/resource/enus/cvi/uiref/cviattrtreerunstate_tree%20cell.htm
- document_id: `labwindows-cvi`
- page_type: `leaf`
- content_type: ``

### ATTR_TREE_RUN_STATE (Tree Cell)

| Type: | Tree Cell attribute |
| --- | --- |
| Description: | Allows programmatic control of the run state of the tree cell. Notes: When you set this attribute to VAL_SELECT_STATE, if the cell is not being edited, setting this value causes no change. When you set this attribute to VAL_EDIT_STATE, if the cell is not currently the active item, it becomes the active item. If another cell was being edited, those edits are committed and then the new active item is changed to edit mode. |
| Data Type: | integer |
| Default Value: | VAL_SELECT_STATE |
| LabWindows/CVICompatibility: | LabWindows/CVI 2009 and later |

##### Values

| VAL_SELECT_STATE | The tree run state is set for item selection. |
| --- | --- |
| VAL_EDIT_STATE | The tree run state is set for item label editing. This state is not valid if the tree is empty, or if the active item/specified cell has ATTR_NO_EDIT_LABEL set. |

<!--NI_TOPIC bundle=labwindows-cvi path=cvi/uiref/cviattrupperleftcornercolor.htm language=enus -->
## TOPIC 00843: ATTR_UPPER_LEFT_CORNER_COLOR

- bundle_id: `labwindows-cvi`
- source_path: `cvi/uiref/cviattrupperleftcornercolor.htm`
- source_url: https://docs-be.ni.com/bundle/labwindows-cvi/raw/resource/enus/cvi/uiref/cviattrupperleftcornercolor.htm
- document_id: `labwindows-cvi`
- page_type: `leaf`
- content_type: ``

### ATTR_UPPER_LEFT_CORNER_COLOR

| Type: | Control attribute |
| --- | --- |
| Description: | The RGB color value of the upper left corner of the table. This area is visible if and only if ATTR_ROW_LABELS_VISIBLE and ATTR_COLUMN_LABELS_VISIBLE are both set to TRUE. LabWindows/CVI ignores this attribute if you enable the ATTR_CONFORM_TO_SYSTEM_THEME attribute, enable the Use Windows Visual Styles for Controls option, or disable the ATTR_DISABLE_PANEL_THEME attribute. An RGB value is a 4-byte integer with the hexadecimal format 0x00RRGGBB. RR, GG, and BB are the respective red, green, and blue components of the color value. See MakeColor. |
| Control Types: | Tables. |
| Data Type: | integer |
| LabWindows/CVICompatibility: | LabWindows/CVI 5.5 and later |

##### Values

| VAL_RED | Red = 255, Green = 0, Blue = 0 |
| --- | --- |
| VAL_GREEN | Red = 0, Green = 255, Blue = 0 |
| VAL_BLUE | Red = 0, Green = 0, Blue = 255 |
| VAL_CYAN | Red = 0, Green = 255, Blue = 255 |
| VAL_MAGENTA | Red = 255, Green = 0, Blue = 255 |
| VAL_YELLOW | Red = 255, Green = 255, Blue = 0 |
| VAL_DK_RED | Red = 128, Green = 0, Blue = 0 |
| VAL_DK_BLUE | Red = 0, Green = 0, Blue = 128 |
| VAL_DK_GREEN | Red = 0, Green = 128, Blue = 0 |
| VAL_DK_CYAN | Red = 0, Green = 128, Blue = 128 |
| VAL_DK_MAGENTA | Red = 128, Green = 0, Blue = 128 |
| VAL_DK_YELLOW | Red = 128, Green = 128, Blue = 0 |
| VAL_LT_GRAY | Red = 192, Green = 192, Blue = 192 |
| VAL_DK_GRAY | Red = 128, Green = 128, Blue = 128 |
| VAL_BLACK | Red = 0, Green = 0, Blue = 0 |
| VAL_WHITE | Red = 255, Green = 255, Blue = 255 |
| VAL_GRAY | Red = 160, Green = 160, Blue = 160 |
| VAL_OFFWHITE | Red = 224, Green = 224, Blue = 224 |
| VAL_TRANSPARENT | Red = 0, Green = 0, Blue = 0, transparent bit set. |
| VAL_PANEL_GRAY | Red = 192, Green = 192, Blue = 192 |

<!--NI_TOPIC bundle=labwindows-cvi path=cvi/uiref/cviattrusecheckerboarddimming.htm language=enus -->
## TOPIC 00844: ATTR_USE_CHECKERBOARD_DIMMING

- bundle_id: `labwindows-cvi`
- source_path: `cvi/uiref/cviattrusecheckerboarddimming.htm`
- source_url: https://docs-be.ni.com/bundle/labwindows-cvi/raw/resource/enus/cvi/uiref/cviattrusecheckerboarddimming.htm
- document_id: `labwindows-cvi`
- page_type: `leaf`
- content_type: ``

### ATTR_USE_CHECKERBOARD_DIMMING

| Type: | System attribute |
| --- | --- |
| Description: | Enable this attribute to revert the control dimming algorithm to the one used in LabWindows/CVI 7.1 and earlier. This algorithm involves drawing a 1-pixel checkerboard pattern, using the panel color, over the control. You must enable this attribute before you enable ATTR_DIMMED or before you load a panel containing controls that are dimmed. 0 = Do not use checkerboard dimming 1 = Use checkerboard dimming |
| Data Type: | integer |
| Default Value: | 0 |
| LabWindows/CVICompatibility: | LabWindows/CVI 9.0 and later |

##### Values

| 0 | False |
| --- | --- |
| 1 | True |

<!--NI_TOPIC bundle=labwindows-cvi path=cvi/uiref/cviattruselabeltext_column.htm language=enus -->
## TOPIC 00845: ATTR_USE_LABEL_TEXT (Column)

- bundle_id: `labwindows-cvi`
- source_path: `cvi/uiref/cviattruselabeltext_column.htm`
- source_url: https://docs-be.ni.com/bundle/labwindows-cvi/raw/resource/enus/cvi/uiref/cviattruselabeltext_column.htm
- document_id: `labwindows-cvi`
- page_type: `leaf`
- content_type: ``

### ATTR_USE_LABEL_TEXT (Column)

| Type: | Column attribute |
| --- | --- |
| Description: | Determines whether each column should be labeled with its numeric index or with a custom string. If the value is TRUE the custom string is specified using ATTR_LABEL_TEXT. 0 = Use numeric index as label 1 = Use custom text as label |
| Data Type: | integer |
| Default Value: | 0 |
| LabWindows/CVICompatibility: | LabWindows/CVI 5.5 and later |

##### Values

| 0 | False |
| --- | --- |
| 1 | True |

<!--NI_TOPIC bundle=labwindows-cvi path=cvi/uiref/cviattruselabeltext_row.htm language=enus -->
## TOPIC 00846: ATTR_USE_LABEL_TEXT (Row)

- bundle_id: `labwindows-cvi`
- source_path: `cvi/uiref/cviattruselabeltext_row.htm`
- source_url: https://docs-be.ni.com/bundle/labwindows-cvi/raw/resource/enus/cvi/uiref/cviattruselabeltext_row.htm
- document_id: `labwindows-cvi`
- page_type: `leaf`
- content_type: ``

### ATTR_USE_LABEL_TEXT (Row)

| Type: | Row attribute |
| --- | --- |
| Description: | Determines whether each row should be labeled with its numeric index or with a custom string. If the value is TRUE the custom string is specified using ATTR_LABEL_TEXT. 0 = Use numeric index as label 1 = Use custom text as label |
| Data Type: | integer |
| Default Value: | 0 |
| LabWindows/CVICompatibility: | LabWindows/CVI 5.5 and later |

##### Values

| 0 | False |
| --- | --- |
| 1 | True |

<!--NI_TOPIC bundle=labwindows-cvi path=cvi/uiref/cviattruselocalizeddecimalsymbol.htm language=enus -->
## TOPIC 00847: ATTR_USE_LOCALIZED_DECIMAL_SYMBOL

- bundle_id: `labwindows-cvi`
- source_path: `cvi/uiref/cviattruselocalizeddecimalsymbol.htm`
- source_url: https://docs-be.ni.com/bundle/labwindows-cvi/raw/resource/enus/cvi/uiref/cviattruselocalizeddecimalsymbol.htm
- document_id: `labwindows-cvi`
- page_type: `leaf`
- content_type: ``

### ATTR_USE_LOCALIZED_DECIMAL_SYMBOL

| Type: | System attribute |
| --- | --- |
| Description: | This attribute allows you to customize the symbol used as the decimal point by all UI controls. |
| Data Type: | integer |
| Default Value: | VAL_USE_PERIOD |
| LabWindows/CVICompatibility: | LabWindows/CVI 5.5 and later |

##### Values

| VAL_USE_SYSTEM_SETTING | Allow the Windows system settings to determine which character UI controls use as the decimal point. |
| --- | --- |
| VAL_USE_PERIOD | Use the ASCII period ('.') character as the decimal point symbol in UI controls. |

<!--NI_TOPIC bundle=labwindows-cvi path=cvi/uiref/cviattruseprogressbarvisualstyles.htm language=enus -->
## TOPIC 00848: ATTR_USE_PROGRESS_BAR_VISUAL_STYLES

- bundle_id: `labwindows-cvi`
- source_path: `cvi/uiref/cviattruseprogressbarvisualstyles.htm`
- source_url: https://docs-be.ni.com/bundle/labwindows-cvi/raw/resource/enus/cvi/uiref/cviattruseprogressbarvisualstyles.htm
- document_id: `labwindows-cvi`
- page_type: `leaf`
- content_type: ``

### ATTR_USE_PROGRESS_BAR_VISUAL_STYLES

| Type: | Control attribute |
| --- | --- |
| Description: | This attribute allows a numeric slide or scale to draw as a progress bar using Windows themes. When enabled, the control uses the progress bar Windows themes even if you disasble theming for the panel. To disable Windows themes, enable ATTR_DISABLE_PANEL_THEME for the control. When ATTR_USE_PROGESS_BAR_VISUAL_STYLES is enabled, the control can function only as an indicator. |
| Control Types: | Numeric slides, ring slides. |
| Restrictions: | Not valid for controls of type CTRL_NUMERIC_GAUGE CTRL_NUMERIC_GAUGE_LS CTRL_NUMERIC_METER CTRL_NUMERIC_METER_LS CTRL_NUMERIC_KNOB CTRL_NUMERIC_KNOB_LS CTRL_NUMERIC_DIAL CTRL_NUMERIC_DIAL_LS CTRL_RING_GAUGE CTRL_RING_GAUGE_LS CTRL_RING_METER CTRL_RING_METER_LS CTRL_RING_KNOB CTRL_RING_KNOB_LS CTRL_RING_DIAL CTRL_RING_DIAL_LS |
| Data Type: | integer |
| Default Value: | 0 |
| LabWindows/CVICompatibility: | LabWindows/CVI 2009 and later |

##### Values

| 0 | False |
| --- | --- |
| 1 | True |

<!--NI_TOPIC bundle=labwindows-cvi path=cvi/uiref/cviattrusesubimage.htm language=enus -->
## TOPIC 00849: ATTR_USE_SUBIMAGE

- bundle_id: `labwindows-cvi`
- source_path: `cvi/uiref/cviattrusesubimage.htm`
- source_url: https://docs-be.ni.com/bundle/labwindows-cvi/raw/resource/enus/cvi/uiref/cviattrusesubimage.htm
- document_id: `labwindows-cvi`
- page_type: `leaf`
- content_type: ``

### ATTR_USE_SUBIMAGE

| Type: | Control attribute |
| --- | --- |
| Description: | Specifies whether to allow a picture button control to display a subset of its loaded image. The subset of the image file is sized to the control. The location and size of the subset is specified by the following attributes, which are in terms of pixels: ATTR_SUBIMAGE_TOP ATTR_SUBIMAGE_LEFT ATTR_SUBIMAGE_WIDTH ATTR_SUBIMAGE_HEIGHT 0 = Disable subimage 1 = Enable subimage |
| Control Types: | Picture buttons. |
| Data Type: | integer |
| Default Value: | 0 |
| LabWindows/CVICompatibility: | LabWindows/CVI 4.0 and later |

##### Values

| 0 | False |
| --- | --- |
| 1 | True |

<!--NI_TOPIC bundle=labwindows-cvi path=cvi/uiref/cviattrverticalgridcolor_cell.htm language=enus -->
## TOPIC 00850: ATTR_VERTICAL_GRID_COLOR (Cell)

- bundle_id: `labwindows-cvi`
- source_path: `cvi/uiref/cviattrverticalgridcolor_cell.htm`
- source_url: https://docs-be.ni.com/bundle/labwindows-cvi/raw/resource/enus/cvi/uiref/cviattrverticalgridcolor_cell.htm
- document_id: `labwindows-cvi`
- page_type: `leaf`
- content_type: ``

### ATTR_VERTICAL_GRID_COLOR (Cell)

| Type: | Cell attribute |
| --- | --- |
| Description: | The RGB color value of the vertical grid line of the table cell. This attribute refers to the grid line to the immediate right of the cell. An RGB value is a 4-byte integer with the hexadecimal format 0x00RRGGBB. RR, GG, and BB are the respective red, green, and blue components of the color value. See MakeColor. |
| Data Type: | integer |
| Default Value: | VAL_BLACK |
| LabWindows/CVICompatibility: | LabWindows/CVI 5.5 and later |

##### Values

| VAL_RED | Red = 255, Green = 0, Blue = 0 |
| --- | --- |
| VAL_GREEN | Red = 0, Green = 255, Blue = 0 |
| VAL_BLUE | Red = 0, Green = 0, Blue = 255 |
| VAL_CYAN | Red = 0, Green = 255, Blue = 255 |
| VAL_MAGENTA | Red = 255, Green = 0, Blue = 255 |
| VAL_YELLOW | Red = 255, Green = 255, Blue = 0 |
| VAL_DK_RED | Red = 128, Green = 0, Blue = 0 |
| VAL_DK_BLUE | Red = 0, Green = 0, Blue = 128 |
| VAL_DK_GREEN | Red = 0, Green = 128, Blue = 0 |
| VAL_DK_CYAN | Red = 0, Green = 128, Blue = 128 |
| VAL_DK_MAGENTA | Red = 128, Green = 0, Blue = 128 |
| VAL_DK_YELLOW | Red = 128, Green = 128, Blue = 0 |
| VAL_LT_GRAY | Red = 192, Green = 192, Blue = 192 |
| VAL_DK_GRAY | Red = 128, Green = 128, Blue = 128 |
| VAL_BLACK | Red = 0, Green = 0, Blue = 0 |
| VAL_WHITE | Red = 255, Green = 255, Blue = 255 |
| VAL_GRAY | Red = 160, Green = 160, Blue = 160 |
| VAL_OFFWHITE | Red = 224, Green = 224, Blue = 224 |
| VAL_TRANSPARENT | Red = 0, Green = 0, Blue = 0, transparent bit set. |
| VAL_PANEL_GRAY | Red = 192, Green = 192, Blue = 192 |

<!--NI_TOPIC bundle=labwindows-cvi path=cvi/uiref/cviattrverticalgridcolor_column.htm language=enus -->
## TOPIC 00851: ATTR_VERTICAL_GRID_COLOR (Column)

- bundle_id: `labwindows-cvi`
- source_path: `cvi/uiref/cviattrverticalgridcolor_column.htm`
- source_url: https://docs-be.ni.com/bundle/labwindows-cvi/raw/resource/enus/cvi/uiref/cviattrverticalgridcolor_column.htm
- document_id: `labwindows-cvi`
- page_type: `leaf`
- content_type: ``

### ATTR_VERTICAL_GRID_COLOR (Column)

| Type: | Column attribute |
| --- | --- |
| Description: | The RGB color value of the vertical grid line of the table cell. This attribute refers to the grid line to the immediate right of the cell. An RGB value is a 4-byte integer with the hexadecimal format 0x00RRGGBB. RR, GG, and BB are the respective red, green, and blue components of the color value. See MakeColor. |
| Data Type: | integer |
| Default Value: | VAL_BLACK |
| LabWindows/CVICompatibility: | LabWindows/CVI 5.5 and later |

##### Values

| VAL_RED | Red = 255, Green = 0, Blue = 0 |
| --- | --- |
| VAL_GREEN | Red = 0, Green = 255, Blue = 0 |
| VAL_BLUE | Red = 0, Green = 0, Blue = 255 |
| VAL_CYAN | Red = 0, Green = 255, Blue = 255 |
| VAL_MAGENTA | Red = 255, Green = 0, Blue = 255 |
| VAL_YELLOW | Red = 255, Green = 255, Blue = 0 |
| VAL_DK_RED | Red = 128, Green = 0, Blue = 0 |
| VAL_DK_BLUE | Red = 0, Green = 0, Blue = 128 |
| VAL_DK_GREEN | Red = 0, Green = 128, Blue = 0 |
| VAL_DK_CYAN | Red = 0, Green = 128, Blue = 128 |
| VAL_DK_MAGENTA | Red = 128, Green = 0, Blue = 128 |
| VAL_DK_YELLOW | Red = 128, Green = 128, Blue = 0 |
| VAL_LT_GRAY | Red = 192, Green = 192, Blue = 192 |
| VAL_DK_GRAY | Red = 128, Green = 128, Blue = 128 |
| VAL_BLACK | Red = 0, Green = 0, Blue = 0 |
| VAL_WHITE | Red = 255, Green = 255, Blue = 255 |
| VAL_GRAY | Red = 160, Green = 160, Blue = 160 |
| VAL_OFFWHITE | Red = 224, Green = 224, Blue = 224 |
| VAL_TRANSPARENT | Red = 0, Green = 0, Blue = 0, transparent bit set. |
| VAL_PANEL_GRAY | Red = 192, Green = 192, Blue = 192 |

<!--NI_TOPIC bundle=labwindows-cvi path=cvi/uiref/cviattrverticalgridcolor_control.htm language=enus -->
## TOPIC 00852: ATTR_VERTICAL_GRID_COLOR (Control)

- bundle_id: `labwindows-cvi`
- source_path: `cvi/uiref/cviattrverticalgridcolor_control.htm`
- source_url: https://docs-be.ni.com/bundle/labwindows-cvi/raw/resource/enus/cvi/uiref/cviattrverticalgridcolor_control.htm
- document_id: `labwindows-cvi`
- page_type: `leaf`
- content_type: ``

### ATTR_VERTICAL_GRID_COLOR (Control)

| Type: | Control attribute |
| --- | --- |
| Description: | The default RGB color value of the vertical grid line of new table cells when ATTR_TABLE_MODE is set to VAL_GRID. This attribute refers to the grid line to the immediate right of the cell. An RGB value is a 4-byte integer with the hexadecimal format 0x00RRGGBB. RR, GG, and BB are the respective red, green, and blue components of the color value. See MakeColor. |
| Control Types: | Tables. |
| Data Type: | integer |
| Default Value: | VAL_BLACK |
| LabWindows/CVICompatibility: | LabWindows/CVI 5.5 and later |

##### Values

| VAL_RED | Red = 255, Green = 0, Blue = 0 |
| --- | --- |
| VAL_GREEN | Red = 0, Green = 255, Blue = 0 |
| VAL_BLUE | Red = 0, Green = 0, Blue = 255 |
| VAL_CYAN | Red = 0, Green = 255, Blue = 255 |
| VAL_MAGENTA | Red = 255, Green = 0, Blue = 255 |
| VAL_YELLOW | Red = 255, Green = 255, Blue = 0 |
| VAL_DK_RED | Red = 128, Green = 0, Blue = 0 |
| VAL_DK_BLUE | Red = 0, Green = 0, Blue = 128 |
| VAL_DK_GREEN | Red = 0, Green = 128, Blue = 0 |
| VAL_DK_CYAN | Red = 0, Green = 128, Blue = 128 |
| VAL_DK_MAGENTA | Red = 128, Green = 0, Blue = 128 |
| VAL_DK_YELLOW | Red = 128, Green = 128, Blue = 0 |
| VAL_LT_GRAY | Red = 192, Green = 192, Blue = 192 |
| VAL_DK_GRAY | Red = 128, Green = 128, Blue = 128 |
| VAL_BLACK | Red = 0, Green = 0, Blue = 0 |
| VAL_WHITE | Red = 255, Green = 255, Blue = 255 |
| VAL_GRAY | Red = 160, Green = 160, Blue = 160 |
| VAL_OFFWHITE | Red = 224, Green = 224, Blue = 224 |
| VAL_TRANSPARENT | Red = 0, Green = 0, Blue = 0, transparent bit set. |
| VAL_PANEL_GRAY | Red = 192, Green = 192, Blue = 192 |

<!--NI_TOPIC bundle=labwindows-cvi path=cvi/uiref/cviattrxlabelfont.htm language=enus -->
## TOPIC 00853: ATTR_XLABEL_FONT

- bundle_id: `labwindows-cvi`
- source_path: `cvi/uiref/cviattrxlabelfont.htm`
- source_url: https://docs-be.ni.com/bundle/labwindows-cvi/raw/resource/enus/cvi/uiref/cviattrxlabelfont.htm
- document_id: `labwindows-cvi`
- page_type: `leaf`
- content_type: ``

### ATTR_XLABEL_FONT

| Type: | Control attribute |
| --- | --- |
| Description: | The name of the font for the x-axis label. To determine the size of the buffer to pass when you are obtaining the font name, call GetCtrlAttribute and specify the ATTR_XLABEL_FONT_NAME_LENGTH attribute. You can use a LabWindows/CVI-supplied font; any host font—such as Arial or Courier—supported on your system; or a user-defined metafont saved by a previous call to functions such as CreateMetaFont and CreateMetaFontEx. Always set the font before setting the size or style. |
| Control Types: | Digital graphs, graphs, strip charts. |
| Data Type: | string |
| Default Value: | VAL_DIALOG_META_FONT |
| LabWindows/CVICompatibility: | LabWindows/CVI 8.5 and later |

##### Values

| VAL_MENU_FONT | Default font style for LabWindows/CVI menus. This font contains typeface information only. This value is an alias to an operating system font. Therefore, the operating system and user preferences on your machine determine this font style. |
| --- | --- |
| VAL_DIALOG_FONT | Default font style for LabWindows/CVI dialog boxes and control text. This font contains typeface information only. This value is an alias to an operating system font. Therefore, the operating system and user preferences on your machine determine this font style. |
| VAL_EDITOR_FONT | Default font style for the LabWindows/CVI Source window. This font contains typeface information only. This value is an alias to an operating system font. Therefore, the operating system and user preferences on your machine determine this font style. |
| VAL_APP_FONT | Default font style for the LabWindows/CVI Workspace window. This font contains typeface information only. This value is an alias to an operating system font. Therefore, the operating system and user preferences on your machine determine this font style. |
| VAL_MESSAGE_BOX_FONT | Default font style for LabWindows/CVI message boxes. This font contains typeface information only. This value is an alias to an operating system font. Therefore, the operating system and user preferences on your machine determine this font style. |
| VAL_MENU_META_FONT | Default font for LabWindows/CVI menus. Metafonts contain typeface information, point size, and text styles such as bold, shadow outline, underline, italics, and strikeout. Because metafonts contain character size information, strings that use metafonts are more likely to have the same width across platforms. This value is an alias to an operating system font. Therefore, the operating system and user preferences on your machine determine this font. |
| VAL_DIALOG_META_FONT | Default font for LabWindows/CVI dialog boxes and control text. Metafonts contain typeface information, point size, and text styles such as bold, shadow outline, underline, italics, and strikeout. Because metafonts contain character size information, strings that use metafonts are more likely to have the same width across platforms. This value is an alias to an operating system font. Therefore, the operating system and user preferences on your machine determine this font. |
| VAL_EDITOR_META_FONT | Default font for the LabWindows/CVI Source window. Metafonts contain typeface information, point size, and text styles such as bold, shadow outline, underline, italics, and strikeout. Because metafonts contain character size information, strings that use metafonts are more likely to have the same width across platforms. This value is an alias to an operating system font. Therefore, the operating system and user preferences on your machine determine this font. |
| VAL_APP_META_FONT | Default font for the LabWindows/CVI Workspace window. Metafonts contain typeface information, point size, and text styles such as bold, shadow outline, underline, italics, and strikeout. Because metafonts contain character size information, strings that use metafonts are more likely to have the same width across platforms. This value is an alias to an operating system font. Therefore, the operating system and user preferences on your machine determine this font. |
| VAL_MESSAGE_BOX_META_FONT | Default font for LabWindows/CVI message boxes. Metafonts contain typeface information, point size, and text styles such as bold, shadow outline, underline, italics, and strikeout. Because metafonts contain character size information, strings that use metafonts are more likely to have the same width across platforms. This value is an alias to an operating system font. Therefore, the operating system and user preferences on your machine determine this font. |
| VAL_7SEG_META_FONT | Font that provides compatibility with LabWindows for DOS. Metafonts contain typeface information, point size, and text styles such as bold, shadow outline, underline, italics, and strikeout. Because metafonts contain character size information, strings that use metafonts are more likely to have the same width across platforms. |
| VAL_SYSTEM_META_FONT | Font that provides compatibility with function panels and user interface panels from LabWindows for DOS that use extended IBM PC characters. Because other fonts may not contain these extended characters, cut/paste operations may fail. Metafonts contain typeface information, point size, and text styles such as bold, shadow outline, underline, italics, and strikeout. Because metafonts contain character size information, strings that use metafonts are more likely to have the same width across platforms. |

<!--NI_TOPIC bundle=labwindows-cvi path=cvi/uiref/cviattrxlabelfontnamelength.htm language=enus -->
## TOPIC 00854: ATTR_XLABEL_FONT_NAME_LENGTH

- bundle_id: `labwindows-cvi`
- source_path: `cvi/uiref/cviattrxlabelfontnamelength.htm`
- source_url: https://docs-be.ni.com/bundle/labwindows-cvi/raw/resource/enus/cvi/uiref/cviattrxlabelfontnamelength.htm
- document_id: `labwindows-cvi`
- page_type: `leaf`
- content_type: ``

### ATTR_XLABEL_FONT_NAME_LENGTH

| Type: | Control attribute |
| --- | --- |
| Description: | The number of bytes in the name of the font for the x-axis label. The length does not include the ASCII NUL byte. Use this value to determine the size of the buffer to pass when you call GetCtrlAttribute and specify the ATTR_XLABEL_FONT attribute. |
| Control Types: | Digital graphs, graphs, strip charts. |
| Restrictions: | Not settable. |
| Data Type: | integer |
| LabWindows/CVICompatibility: | LabWindows/CVI 8.5 and later |

<!--NI_TOPIC bundle=labwindows-cvi path=cvi/uiref/cviattrxlabelitalic.htm language=enus -->
## TOPIC 00855: ATTR_XLABEL_ITALIC

- bundle_id: `labwindows-cvi`
- source_path: `cvi/uiref/cviattrxlabelitalic.htm`
- source_url: https://docs-be.ni.com/bundle/labwindows-cvi/raw/resource/enus/cvi/uiref/cviattrxlabelitalic.htm
- document_id: `labwindows-cvi`
- page_type: `leaf`
- content_type: ``

### ATTR_XLABEL_ITALIC

| Type: | Control attribute |
| --- | --- |
| Description: | Specifies whether the x-axis label is in italics. 0 = Not italics 1 = Italics |
| Control Types: | Digital graphs, graphs, strip charts. |
| Data Type: | integer |
| Default Value: | 0 |
| LabWindows/CVICompatibility: | LabWindows/CVI 8.5 and later |

##### Values

| 0 | False |
| --- | --- |
| 1 | True |

<!--NI_TOPIC bundle=labwindows-cvi path=cvi/uiref/cviattrxmarkorigin.htm language=enus -->
## TOPIC 00856: ATTR_XMARK_ORIGIN

- bundle_id: `labwindows-cvi`
- source_path: `cvi/uiref/cviattrxmarkorigin.htm`
- source_url: https://docs-be.ni.com/bundle/labwindows-cvi/raw/resource/enus/cvi/uiref/cviattrxmarkorigin.htm
- document_id: `labwindows-cvi`
- page_type: `leaf`
- content_type: ``

### ATTR_XMARK_ORIGIN

| Type: | Control attribute |
| --- | --- |
| Description: | Specifies whether to show or hide the X-origin tick marks. 0 = Hide tick marks 1 = Show tick marks |
| Control Types: | Digital graphs, graphs. |
| Data Type: | integer |
| Default Value: | 1 |
| LabWindows/CVICompatibility: | LabWindows/CVI 3.0 and later |

##### Values

| 0 | False |
| --- | --- |
| 1 | True |

<!--NI_TOPIC bundle=labwindows-cvi path=cvi/uiref/cviattrxminorgridvisible.htm language=enus -->
## TOPIC 00857: ATTR_XMINORGRID_VISIBLE

- bundle_id: `labwindows-cvi`
- source_path: `cvi/uiref/cviattrxminorgridvisible.htm`
- source_url: https://docs-be.ni.com/bundle/labwindows-cvi/raw/resource/enus/cvi/uiref/cviattrxminorgridvisible.htm
- document_id: `labwindows-cvi`
- page_type: `leaf`
- content_type: ``

### ATTR_XMINORGRID_VISIBLE

| Type: | Control attribute |
| --- | --- |
| Description: | Specifies whether to show or hide the minor grid lines for the x-axis on the graph. In order for the minor grid lines to be visible, you must also enable the ATTR_XGRID_VISIBLE attribute. The number of minor grid lines that are visible when this attribute is enabled is proportional to the space between consecutive major grid lines. In some cases, when this space is too small, it's possible for this number to be zero. 0 = Hide minor grid lines 1 = Show minor grid lines |
| Control Types: | Digital graphs, graphs, strip charts. |
| Data Type: | integer |
| Default Value: | 0 |
| LabWindows/CVICompatibility: | LabWindows/CVI 7.0 and later |

##### Values

| 0 | False |
| --- | --- |
| 1 | True |

<!--NI_TOPIC bundle=labwindows-cvi path=cvi/uiref/cviattrxname.htm language=enus -->
## TOPIC 00858: ATTR_XNAME

- bundle_id: `labwindows-cvi`
- source_path: `cvi/uiref/cviattrxname.htm`
- source_url: https://docs-be.ni.com/bundle/labwindows-cvi/raw/resource/enus/cvi/uiref/cviattrxname.htm
- document_id: `labwindows-cvi`
- page_type: `leaf`
- content_type: ``

### ATTR_XNAME

| Type: | Control attribute |
| --- | --- |
| Description: | The text name to display for the X-axis. To determine the size of the buffer to pass when you are obtaining the name, call GetCtrlAttribute and specify the ATTR_XNAME_LENGTH attribute. |
| Control Types: | Digital graphs, graphs, strip charts. |
| Data Type: | string |
| LabWindows/CVICompatibility: | LabWindows/CVI 3.0 and later |

<!--NI_TOPIC bundle=labwindows-cvi path=cvi/uiref/cviattrxnamelength.htm language=enus -->
## TOPIC 00859: ATTR_XNAME_LENGTH

- bundle_id: `labwindows-cvi`
- source_path: `cvi/uiref/cviattrxnamelength.htm`
- source_url: https://docs-be.ni.com/bundle/labwindows-cvi/raw/resource/enus/cvi/uiref/cviattrxnamelength.htm
- document_id: `labwindows-cvi`
- page_type: `leaf`
- content_type: ``

### ATTR_XNAME_LENGTH

| Type: | Control attribute |
| --- | --- |
| Description: | The number of bytes in the x-axis text name. The length does not include the ASCII NUL byte. Use this value to determine the size of the buffer to pass when you call GetCtrlAttribute and specify the ATTR_XNAME attribute. |
| Control Types: | Digital graphs, graphs, strip charts. |
| Restrictions: | Not settable. |
| Data Type: | integer |
| LabWindows/CVICompatibility: | LabWindows/CVI 3.0 and later |

<!--NI_TOPIC bundle=labwindows-cvi path=cvi/uiref/cviattrxoffset.htm language=enus -->
## TOPIC 00860: ATTR_XOFFSET

- bundle_id: `labwindows-cvi`
- source_path: `cvi/uiref/cviattrxoffset.htm`
- source_url: https://docs-be.ni.com/bundle/labwindows-cvi/raw/resource/enus/cvi/uiref/cviattrxoffset.htm
- document_id: `labwindows-cvi`
- page_type: `leaf`
- content_type: ``

### ATTR_XOFFSET

| Type: | Print attribute |
| --- | --- |
| Description: | Sets the X offset of the hardcopy image on the paper. The offset is expressed in tenths of millimeters. The offset is relative to the left edge of the paper as seen in portrait mode, regardless of the ATTR_ORIENTATION setting. A value of 0 forces the image to what you see as the "left" edge when looking at the paper in portrait mode. This is equivalent to what you see as the "top" edge when looking at the paper in landscape mode. VAL_CENTER_ON_PAPER centers the image in the X direction. (Note: VAL_CENTER_ON_PAPER was formerly called VAL_USE_PRINTER_DEFAULT.) |
| Types of Printing: | Graphics. |
| Data Type: | integer |
| Valid Range: | 0 or greater, or VAL_CENTER_ON_PAPER. |
| Default Value: | VAL_CENTER_ON_PAPER. |
| LabWindows/CVICompatibility: | LabWindows/CVI 3.0 and later |

##### Values

| VAL_CENTER_ON_PAPER | Center the output on the paper. (This value was formerly called VAL_USE_PRINTER_DEFAULT). |
| --- | --- |

<!--NI_TOPIC bundle=labwindows-cvi path=cvi/uiref/cviattrxpadding.htm language=enus -->
## TOPIC 00861: ATTR_XPADDING

- bundle_id: `labwindows-cvi`
- source_path: `cvi/uiref/cviattrxpadding.htm`
- source_url: https://docs-be.ni.com/bundle/labwindows-cvi/raw/resource/enus/cvi/uiref/cviattrxpadding.htm
- document_id: `labwindows-cvi`
- page_type: `leaf`
- content_type: ``

### ATTR_XPADDING

| Type: | Control attribute |
| --- | --- |
| Description: | The minimum number of characters to display in the X-axis labels. This pads the labels with zeros to ensure that they are at least the minimum length. If the length of the labels are greater than the minimum, the X-axis labels will display the complete number even if they exceed the minimum number of characters. |
| Control Types: | Digital graphs, graphs, strip charts. |
| Data Type: | integer |
| Valid Range: | 0 to 64 |
| Default Value: | 0 |
| LabWindows/CVICompatibility: | LabWindows/CVI 5.5 and later |

<!--NI_TOPIC bundle=labwindows-cvi path=cvi/uiref/cviattrxprecision.htm language=enus -->
## TOPIC 00862: ATTR_XPRECISION

- bundle_id: `labwindows-cvi`
- source_path: `cvi/uiref/cviattrxprecision.htm`
- source_url: https://docs-be.ni.com/bundle/labwindows-cvi/raw/resource/enus/cvi/uiref/cviattrxprecision.htm
- document_id: `labwindows-cvi`
- page_type: `leaf`
- content_type: ``

### ATTR_XPRECISION

| Type: | Control attribute |
| --- | --- |
| Description: | The number of characters after the decimal point to display in the numeric X-axis labels. If ATTR_XFORMAT is set to VAL_ABSOLUTE_TIME_FORMAT or VAL_RELATIVE_TIME_FORMAT, specifies the default precision for the fractional part of the seconds. |
| Control Types: | Digital graphs, graphs, strip charts. |
| Restrictions: | VAL_AUTO is not valid for strip charts. |
| Data Type: | integer |
| Valid Range: | 0 to 15, or VAL_AUTO |
| Default Value: | VAL_AUTO (graphs), 0 (strip charts) |
| LabWindows/CVICompatibility: | LabWindows/CVI 3.0 and later |

##### Values

| VAL_AUTO |
| --- |

<!--NI_TOPIC bundle=labwindows-cvi path=cvi/uiref/cviattrxresolution.htm language=enus -->
## TOPIC 00863: ATTR_XRESOLUTION

- bundle_id: `labwindows-cvi`
- source_path: `cvi/uiref/cviattrxresolution.htm`
- source_url: https://docs-be.ni.com/bundle/labwindows-cvi/raw/resource/enus/cvi/uiref/cviattrxresolution.htm
- document_id: `labwindows-cvi`
- page_type: `leaf`
- content_type: ``

### ATTR_XRESOLUTION

| Type: | Print attribute |
| --- | --- |
| Description: | Sets the X resolution of the printer. The resolution is expressed in dots per inch. If you specify VAL_USE_PRINTER_SETTING, the next call to a User Interface Library printing function uses the system's current setting for the selected printer. After the printing function returns, the value of the attribute is no longer VAL_USE_PRINTER_SETTING. Instead, the library stores the system's setting as the attribute value. If you want to update the attribute value based on the current system setting each time you print, set the attribute to VAL_USE_PRINTER_SETTING before each call to a printing function. (Note: VAL_USE_PRINTER_SETTING was formerly called VAL_USE_PRINTER_DEFAULT.) |
| Types of Printing: | Text and graphics. |
| Data Type: | integer |
| Valid Range: | 0 or greater, or VAL_USE_PRINTER_SETTING |
| Default Value: | VAL_USE_PRINTER_SETTING |
| LabWindows/CVICompatibility: | LabWindows/CVI 3.0 and later |

##### Values

| VAL_USE_PRINTER_SETTING | (Windows platforms only). Use the system's current setting for the selected printer. The next printing operation uses the current system setting and stores it as the attribute value. If you want to update the attribute from the current system setting each time you print, set the attribute to VAL_USE_PRINTER_SETTING before each call to a printing function. (Note: VAL_USE_PRINTER_SETTING was formerly called VAL_USE_PRINTER_DEFAULT). |
| --- | --- |

<!--NI_TOPIC bundle=labwindows-cvi path=cvi/uiref/cviattrxreverse.htm language=enus -->
## TOPIC 00864: ATTR_XREVERSE

- bundle_id: `labwindows-cvi`
- source_path: `cvi/uiref/cviattrxreverse.htm`
- source_url: https://docs-be.ni.com/bundle/labwindows-cvi/raw/resource/enus/cvi/uiref/cviattrxreverse.htm
- document_id: `labwindows-cvi`
- page_type: `leaf`
- content_type: ``

### ATTR_XREVERSE

| Type: | Control attribute |
| --- | --- |
| Description: | Determines whether to reverse the orientation of the x-axis so that the lowest value is shown at the right. If the orientation of the x-axis is reversed, the horizontal orientation of the plots is also reversed. 0 = do not reverse 1 = reverse |
| Control Types: | Graphs. |
| Data Type: | integer |
| Default Value: | 0 |
| LabWindows/CVICompatibility: | LabWindows/CVI 4.0 and later |

##### Values

| 0 | False |
| --- | --- |
| 1 | True |

<!--NI_TOPIC bundle=labwindows-cvi path=cvi/uiref/cviattrxscaling.htm language=enus -->
## TOPIC 00865: ATTR_XSCALING

- bundle_id: `labwindows-cvi`
- source_path: `cvi/uiref/cviattrxscaling.htm`
- source_url: https://docs-be.ni.com/bundle/labwindows-cvi/raw/resource/enus/cvi/uiref/cviattrxscaling.htm
- document_id: `labwindows-cvi`
- page_type: `leaf`
- content_type: ``

### ATTR_XSCALING

| Type: | Control attribute |
| --- | --- |
| Description: | The factor used to scale user-supplied horizontal coordinates and widths into pixel-based coordinates and widths. |
| Control Types: | Canvases. |
| Data Type: | double |
| Default Value: | 1.0 |
| LabWindows/CVICompatibility: | LabWindows/CVI 4.0 and later |

<!--NI_TOPIC bundle=labwindows-cvi path=cvi/uiref/cviattrxuselabelstrings.htm language=enus -->
## TOPIC 00866: ATTR_XUSE_LABEL_STRINGS

- bundle_id: `labwindows-cvi`
- source_path: `cvi/uiref/cviattrxuselabelstrings.htm`
- source_url: https://docs-be.ni.com/bundle/labwindows-cvi/raw/resource/enus/cvi/uiref/cviattrxuselabelstrings.htm
- document_id: `labwindows-cvi`
- page_type: `leaf`
- content_type: ``

### ATTR_XUSE_LABEL_STRINGS

| Type: | Control attribute |
| --- | --- |
| Description: | Determines whether the value labels on the x-axis are replaced by strings associated with those values. These strings can be specified either in the User Interface Editor or by calling the InsertAxisItem function. If ATTR_XFORMAT is set to VAL_ABSOLUTE_TIME_FORMAT or VAL_RELATIVE_TIME_FORMAT, this attribute formats any date/time specifiers included in the label string. 0 = Use numeric values in axis labels 1 = Use custom text in axis labels |
| Control Types: | Digital graphs, graphs, strip charts. |
| Data Type: | integer |
| Default Value: | 0 |
| LabWindows/CVICompatibility: | LabWindows/CVI 4.0 and later |

##### Values

| 0 | False |
| --- | --- |
| 1 | True |

<!--NI_TOPIC bundle=labwindows-cvi path=cvi/uiref/cviattrxynamebold.htm language=enus -->
## TOPIC 00867: ATTR_XYNAME_BOLD

- bundle_id: `labwindows-cvi`
- source_path: `cvi/uiref/cviattrxynamebold.htm`
- source_url: https://docs-be.ni.com/bundle/labwindows-cvi/raw/resource/enus/cvi/uiref/cviattrxynamebold.htm
- document_id: `labwindows-cvi`
- page_type: `leaf`
- content_type: ``

### ATTR_XYNAME_BOLD

| Type: | Control attribute |
| --- | --- |
| Description: | Specifies whether the x- and y-axis names are bold. 0 = Not bold 1 = Bold |
| Control Types: | Digital graphs, graphs, strip charts. |
| Data Type: | integer |
| Default Value: | 0 |
| LabWindows/CVICompatibility: | LabWindows/CVI 3.0 and later |

##### Values

| 0 | False |
| --- | --- |
| 1 | True |

<!--NI_TOPIC bundle=labwindows-cvi path=cvi/uiref/cviattrxynamecharacterset.htm language=enus -->
## TOPIC 00868: ATTR_XYNAME_CHARACTER_SET

- bundle_id: `labwindows-cvi`
- source_path: `cvi/uiref/cviattrxynamecharacterset.htm`
- source_url: https://docs-be.ni.com/bundle/labwindows-cvi/raw/resource/enus/cvi/uiref/cviattrxynamecharacterset.htm
- document_id: `labwindows-cvi`
- page_type: `leaf`
- content_type: ``

### ATTR_XYNAME_CHARACTER_SET

| Type: | Control attribute |
| --- | --- |
| Description: | The character set for the x- and y-axis names. |
| Control Types: | Digital graphs, graphs, strip charts. |
| Data Type: | integer |
| Default Value: | VAL_NATIVE_CHARSET |
| LabWindows/CVICompatibility: | LabWindows/CVI 9.0 and later |

##### Values

| VAL_NATIVE_CHARSET | Character set that corresponds to the language selected in the Control Panel for non-Unicode programs. |
| --- | --- |
| VAL_ANSI_CHARSET | The Western character set. |
| VAL_SHIFTJIS_CHARSET | The Japanese character set. |
| VAL_HANGUL_CHARSET | The Korean character set. |
| VAL_GB2312_CHARSET | The Simplified Chinese character set. |
| VAL_CHINESEBIG5_CHARSET | The Traditional Chinese character set. |
| VAL_HEBREW_CHARSET | The Hebrew character set. |
| VAL_ARABIC_CHARSET | The Arabic character set. |
| VAL_GREEK_CHARSET | The Greek character set. |
| VAL_TURKISH_CHARSET | The Turkish character set. |
| VAL_VIETNAMESE_CHARSET | The Vietnamese character set. |
| VAL_THAI_CHARSET | The Thai character set. |
| VAL_EASTEUROPE_CHARSET | The Eastern European character set. |
| VAL_RUSSIAN_CHARSET | The Cyrillic character set. |
| VAL_BALTIC_CHARSET | The Baltic character set. |

<!--NI_TOPIC bundle=labwindows-cvi path=cvi/uiref/cviattrxynamepointsize.htm language=enus -->
## TOPIC 00869: ATTR_XYNAME_POINT_SIZE

- bundle_id: `labwindows-cvi`
- source_path: `cvi/uiref/cviattrxynamepointsize.htm`
- source_url: https://docs-be.ni.com/bundle/labwindows-cvi/raw/resource/enus/cvi/uiref/cviattrxynamepointsize.htm
- document_id: `labwindows-cvi`
- page_type: `leaf`
- content_type: ``

### ATTR_XYNAME_POINT_SIZE

| Type: | Control attribute |
| --- | --- |
| Description: | The font point size for the x- and y-axis names. |
| Control Types: | Digital graphs, graphs, strip charts. |
| Data Type: | integer |
| Valid Range: | 1 to 255 |
| LabWindows/CVICompatibility: | LabWindows/CVI 3.0 and later |

<!--NI_TOPIC bundle=labwindows-cvi path=cvi/uiref/cviattrxynamestrikeout.htm language=enus -->
## TOPIC 00870: ATTR_XYNAME_STRIKEOUT

- bundle_id: `labwindows-cvi`
- source_path: `cvi/uiref/cviattrxynamestrikeout.htm`
- source_url: https://docs-be.ni.com/bundle/labwindows-cvi/raw/resource/enus/cvi/uiref/cviattrxynamestrikeout.htm
- document_id: `labwindows-cvi`
- page_type: `leaf`
- content_type: ``

### ATTR_XYNAME_STRIKEOUT

| Type: | Control attribute |
| --- | --- |
| Description: | Specifies whether the x- and y-axis names have strikeout. 0 = No strikeout 1 = Strikeout |
| Control Types: | Digital graphs, graphs, strip charts. |
| Data Type: | integer |
| Default Value: | 0 |
| LabWindows/CVICompatibility: | LabWindows/CVI 3.0 and later |

##### Values

| 0 | False |
| --- | --- |
| 1 | True |

<!--NI_TOPIC bundle=labwindows-cvi path=cvi/uiref/cviattrxynameunderline.htm language=enus -->
## TOPIC 00871: ATTR_XYNAME_UNDERLINE

- bundle_id: `labwindows-cvi`
- source_path: `cvi/uiref/cviattrxynameunderline.htm`
- source_url: https://docs-be.ni.com/bundle/labwindows-cvi/raw/resource/enus/cvi/uiref/cviattrxynameunderline.htm
- document_id: `labwindows-cvi`
- page_type: `leaf`
- content_type: ``

### ATTR_XYNAME_UNDERLINE

| Type: | Control attribute |
| --- | --- |
| Description: | Specifies whether the x- and y-axis names are underlined. 0 = Not underlined 1 = Underlined |
| Control Types: | Digital graphs, graphs, strip charts. |
| Data Type: | integer |
| Default Value: | 0 |
| LabWindows/CVICompatibility: | LabWindows/CVI 3.0 and later |

##### Values

| 0 | False |
| --- | --- |
| 1 | True |

<!--NI_TOPIC bundle=labwindows-cvi path=cvi/uiref/cviattryaxisoffset.htm language=enus -->
## TOPIC 00872: ATTR_YAXIS_OFFSET

- bundle_id: `labwindows-cvi`
- source_path: `cvi/uiref/cviattryaxisoffset.htm`
- source_url: https://docs-be.ni.com/bundle/labwindows-cvi/raw/resource/enus/cvi/uiref/cviattryaxisoffset.htm
- document_id: `labwindows-cvi`
- page_type: `leaf`
- content_type: ``

### ATTR_YAXIS_OFFSET

| Type: | Control attribute |
| --- | --- |
| Description: | The amount added to the value labels shown on the y-axis. For example, if the actual Y value is 10.0 and the ATTR_YAXIS_OFFSET is 5.0, then the label on the y-axis will show up as 15.0. (Note: The Y value is multiplied by the ATTR_YAXIS_GAIN factor before the ATTR_YAXIS_OFFSET is added to it.) |
| Control Types: | Graphs, strip charts. |
| Data Type: | double |
| Default Value: | 0.0 |
| LabWindows/CVICompatibility: | LabWindows/CVI 4.0 and later |

<!--NI_TOPIC bundle=labwindows-cvi path=cvi/uiref/cviattrycoordatorigin.htm language=enus -->
## TOPIC 00873: ATTR_YCOORD_AT_ORIGIN

- bundle_id: `labwindows-cvi`
- source_path: `cvi/uiref/cviattrycoordatorigin.htm`
- source_url: https://docs-be.ni.com/bundle/labwindows-cvi/raw/resource/enus/cvi/uiref/cviattrycoordatorigin.htm
- document_id: `labwindows-cvi`
- page_type: `leaf`
- content_type: ``

### ATTR_YCOORD_AT_ORIGIN

| Type: | Control attribute |
| --- | --- |
| Description: | The vertical coordinate that is mapped to the top edge of the canvas. (Note: The library multiplies this value by the value of ATTR_YSCALING to arrive at a pixel offset.) |
| Control Types: | Canvases. |
| Data Type: | double |
| Default Value: | 0.0 |
| LabWindows/CVICompatibility: | LabWindows/CVI 4.0 and later |

<!--NI_TOPIC bundle=labwindows-cvi path=cvi/uiref/cviattrydivisions.htm language=enus -->
## TOPIC 00874: ATTR_YDIVISIONS

- bundle_id: `labwindows-cvi`
- source_path: `cvi/uiref/cviattrydivisions.htm`
- source_url: https://docs-be.ni.com/bundle/labwindows-cvi/raw/resource/enus/cvi/uiref/cviattrydivisions.htm
- document_id: `labwindows-cvi`
- page_type: `leaf`
- content_type: ``

### ATTR_YDIVISIONS

| Type: | Control attribute |
| --- | --- |
| Description: | The number of Y-divisions for the graph. |
| Control Types: | Graphs, strip charts. |
| Data Type: | integer |
| Valid Range: | 1 to 100, or VAL_AUTO |
| Default Value: | VAL_AUTO (graphs), 5 (strip charts) |
| LabWindows/CVICompatibility: | LabWindows/CVI 3.0 and later |

##### Values

| VAL_AUTO |
| --- |

<!--NI_TOPIC bundle=labwindows-cvi path=cvi/uiref/cviattryformat.htm language=enus -->
## TOPIC 00875: ATTR_YFORMAT

- bundle_id: `labwindows-cvi`
- source_path: `cvi/uiref/cviattryformat.htm`
- source_url: https://docs-be.ni.com/bundle/labwindows-cvi/raw/resource/enus/cvi/uiref/cviattryformat.htm
- document_id: `labwindows-cvi`
- page_type: `leaf`
- content_type: ``

### ATTR_YFORMAT

| Type: | Control attribute |
| --- | --- |
| Description: | The display format of the Y-axis values. If you specify VAL_ABSOLUTE_TIME_FORMAT or VAL_RELATIVE_TIME_FORMAT, you can call SetAxisTimeFormat to specify how to display the date/time on the specified axis. |
| Control Types: | Graphs, strip charts. |
| Data Type: | integer |
| Default Value: | VAL_FLOATING_PT_FORMAT |
| LabWindows/CVICompatibility: | LabWindows/CVI 3.0 and later |

##### Values

| VAL_RELATIVE_TIME_FORMAT | LabWindows/CVI displays axis labels as formatted strings that describe the time elapsed since a reference point. Example: 00:00:52:23. When you use this format, LabWindows/CVI interprets a plotted data value as the number of seconds that have elapsed since the reference point. The fractional part of the data value represents a fraction of a second. |
| --- | --- |
| VAL_ABSOLUTE_TIME_FORMAT | LabWindows/CVI displays axis labels as formatted strings that describe fixed points in time. Example: 12:30:54 10/7/04. When you use this format, LabWindows/CVI interprets a plotted data value as the number of seconds since midnight, January 1, 1900. The fractional part of the data value represents a fraction of a second. |
| VAL_FLOATING_PT_FORMAT | Example: 123.000 |
| VAL_SCIENTIFIC_FORMAT | Example: 1.23E+2 |
| VAL_ENGINEERING_FORMAT | Example: 123.00E+0 |

<!--NI_TOPIC bundle=labwindows-cvi path=cvi/uiref/cviattrygridvisible.htm language=enus -->
## TOPIC 00876: ATTR_YGRID_VISIBLE

- bundle_id: `labwindows-cvi`
- source_path: `cvi/uiref/cviattrygridvisible.htm`
- source_url: https://docs-be.ni.com/bundle/labwindows-cvi/raw/resource/enus/cvi/uiref/cviattrygridvisible.htm
- document_id: `labwindows-cvi`
- page_type: `leaf`
- content_type: ``

### ATTR_YGRID_VISIBLE

| Type: | Control attribute |
| --- | --- |
| Description: | Specifies whether to show or hide the Y grid on the graph. When you hide the grid lines, the minor grid lines are also hidden. 0 = Hide Y grid 1 = Show Y grid |
| Control Types: | Digital graphs, graphs, strip charts. |
| Data Type: | integer |
| Default Value: | 1 (left y axis), 0 (right y axis) |
| LabWindows/CVICompatibility: | LabWindows/CVI 3.0 and later |

##### Values

| 0 | False |
| --- | --- |
| 1 | True |

<!--NI_TOPIC bundle=labwindows-cvi path=cvi/uiref/cviattrylabelcharacterset.htm language=enus -->
## TOPIC 00877: ATTR_YLABEL_CHARACTER_SET

- bundle_id: `labwindows-cvi`
- source_path: `cvi/uiref/cviattrylabelcharacterset.htm`
- source_url: https://docs-be.ni.com/bundle/labwindows-cvi/raw/resource/enus/cvi/uiref/cviattrylabelcharacterset.htm
- document_id: `labwindows-cvi`
- page_type: `leaf`
- content_type: ``

### ATTR_YLABEL_CHARACTER_SET

| Type: | Control attribute |
| --- | --- |
| Description: | The character set for the y-axis label. |
| Control Types: | Digital graphs, graphs, strip charts. |
| Data Type: | integer |
| Default Value: | VAL_NATIVE_CHARSET |
| LabWindows/CVICompatibility: | LabWindows/CVI 9.0 and later |

##### Values

| VAL_NATIVE_CHARSET | Character set that corresponds to the language selected in the Control Panel for non-Unicode programs. |
| --- | --- |
| VAL_ANSI_CHARSET | The Western character set. |
| VAL_SHIFTJIS_CHARSET | The Japanese character set. |
| VAL_HANGUL_CHARSET | The Korean character set. |
| VAL_GB2312_CHARSET | The Simplified Chinese character set. |
| VAL_CHINESEBIG5_CHARSET | The Traditional Chinese character set. |
| VAL_HEBREW_CHARSET | The Hebrew character set. |
| VAL_ARABIC_CHARSET | The Arabic character set. |
| VAL_GREEK_CHARSET | The Greek character set. |
| VAL_TURKISH_CHARSET | The Turkish character set. |
| VAL_VIETNAMESE_CHARSET | The Vietnamese character set. |
| VAL_THAI_CHARSET | The Thai character set. |
| VAL_EASTEUROPE_CHARSET | The Eastern European character set. |
| VAL_RUSSIAN_CHARSET | The Cyrillic character set. |
| VAL_BALTIC_CHARSET | The Baltic character set. |

<!--NI_TOPIC bundle=labwindows-cvi path=cvi/uiref/cviattrylabelcolor.htm language=enus -->
## TOPIC 00878: ATTR_YLABEL_COLOR

- bundle_id: `labwindows-cvi`
- source_path: `cvi/uiref/cviattrylabelcolor.htm`
- source_url: https://docs-be.ni.com/bundle/labwindows-cvi/raw/resource/enus/cvi/uiref/cviattrylabelcolor.htm
- document_id: `labwindows-cvi`
- page_type: `leaf`
- content_type: ``

### ATTR_YLABEL_COLOR

| Type: | Control attribute |
| --- | --- |
| Description: | The RGB color value of the y-axis label. An RGB value is a 4-byte integer with the hexadecimal format 0x00RRGGBB. RR, GG, and BB are the respective red, green, and blue components of the color value. See MakeColor. |
| Control Types: | Digital graphs, graphs, strip charts. |
| Data Type: | integer |
| LabWindows/CVICompatibility: | LabWindows/CVI 8.5 and later |

##### Values

| VAL_RED | Red = 255, Green = 0, Blue = 0 |
| --- | --- |
| VAL_GREEN | Red = 0, Green = 255, Blue = 0 |
| VAL_BLUE | Red = 0, Green = 0, Blue = 255 |
| VAL_CYAN | Red = 0, Green = 255, Blue = 255 |
| VAL_MAGENTA | Red = 255, Green = 0, Blue = 255 |
| VAL_YELLOW | Red = 255, Green = 255, Blue = 0 |
| VAL_DK_RED | Red = 128, Green = 0, Blue = 0 |
| VAL_DK_BLUE | Red = 0, Green = 0, Blue = 128 |
| VAL_DK_GREEN | Red = 0, Green = 128, Blue = 0 |
| VAL_DK_CYAN | Red = 0, Green = 128, Blue = 128 |
| VAL_DK_MAGENTA | Red = 128, Green = 0, Blue = 128 |
| VAL_DK_YELLOW | Red = 128, Green = 128, Blue = 0 |
| VAL_LT_GRAY | Red = 192, Green = 192, Blue = 192 |
| VAL_DK_GRAY | Red = 128, Green = 128, Blue = 128 |
| VAL_BLACK | Red = 0, Green = 0, Blue = 0 |
| VAL_WHITE | Red = 255, Green = 255, Blue = 255 |
| VAL_GRAY | Red = 160, Green = 160, Blue = 160 |
| VAL_OFFWHITE | Red = 224, Green = 224, Blue = 224 |
| VAL_PANEL_GRAY | Red = 192, Green = 192, Blue = 192 |

<!--NI_TOPIC bundle=labwindows-cvi path=cvi/uiref/cviattrylabelfont.htm language=enus -->
## TOPIC 00879: ATTR_YLABEL_FONT

- bundle_id: `labwindows-cvi`
- source_path: `cvi/uiref/cviattrylabelfont.htm`
- source_url: https://docs-be.ni.com/bundle/labwindows-cvi/raw/resource/enus/cvi/uiref/cviattrylabelfont.htm
- document_id: `labwindows-cvi`
- page_type: `leaf`
- content_type: ``

### ATTR_YLABEL_FONT

| Type: | Control attribute |
| --- | --- |
| Description: | The name of the font for the y-axis label. To determine the size of the buffer to pass when you are obtaining the font name, call GetCtrlAttribute and specify the ATTR_YLABEL_FONT_NAME_LENGTH attribute. You can use a LabWindows/CVI-supplied font; any host font—such as Arial or Courier—supported on your system; or a user-defined metafont saved by a previous call to functions such as CreateMetaFont and CreateMetaFontEx. Always set the font before setting the size or style. |
| Control Types: | Digital graphs, graphs, strip charts. |
| Data Type: | string |
| Default Value: | VAL_DIALOG_META_FONT |
| LabWindows/CVICompatibility: | LabWindows/CVI 8.5 and later |

##### Values

| VAL_MENU_FONT | Default font style for LabWindows/CVI menus. This font contains typeface information only. This value is an alias to an operating system font. Therefore, the operating system and user preferences on your machine determine this font style. |
| --- | --- |
| VAL_DIALOG_FONT | Default font style for LabWindows/CVI dialog boxes and control text. This font contains typeface information only. This value is an alias to an operating system font. Therefore, the operating system and user preferences on your machine determine this font style. |
| VAL_EDITOR_FONT | Default font style for the LabWindows/CVI Source window. This font contains typeface information only. This value is an alias to an operating system font. Therefore, the operating system and user preferences on your machine determine this font style. |
| VAL_APP_FONT | Default font style for the LabWindows/CVI Workspace window. This font contains typeface information only. This value is an alias to an operating system font. Therefore, the operating system and user preferences on your machine determine this font style. |
| VAL_MESSAGE_BOX_FONT | Default font style for LabWindows/CVI message boxes. This font contains typeface information only. This value is an alias to an operating system font. Therefore, the operating system and user preferences on your machine determine this font style. |
| VAL_MENU_META_FONT | Default font for LabWindows/CVI menus. Metafonts contain typeface information, point size, and text styles such as bold, shadow outline, underline, italics, and strikeout. Because metafonts contain character size information, strings that use metafonts are more likely to have the same width across platforms. This value is an alias to an operating system font. Therefore, the operating system and user preferences on your machine determine this font. |
| VAL_DIALOG_META_FONT | Default font for LabWindows/CVI dialog boxes and control text. Metafonts contain typeface information, point size, and text styles such as bold, shadow outline, underline, italics, and strikeout. Because metafonts contain character size information, strings that use metafonts are more likely to have the same width across platforms. This value is an alias to an operating system font. Therefore, the operating system and user preferences on your machine determine this font. |
| VAL_EDITOR_META_FONT | Default font for the LabWindows/CVI Source window. Metafonts contain typeface information, point size, and text styles such as bold, shadow outline, underline, italics, and strikeout. Because metafonts contain character size information, strings that use metafonts are more likely to have the same width across platforms. This value is an alias to an operating system font. Therefore, the operating system and user preferences on your machine determine this font. |
| VAL_APP_META_FONT | Default font for the LabWindows/CVI Workspace window. Metafonts contain typeface information, point size, and text styles such as bold, shadow outline, underline, italics, and strikeout. Because metafonts contain character size information, strings that use metafonts are more likely to have the same width across platforms. This value is an alias to an operating system font. Therefore, the operating system and user preferences on your machine determine this font. |
| VAL_MESSAGE_BOX_META_FONT | Default font for LabWindows/CVI message boxes. Metafonts contain typeface information, point size, and text styles such as bold, shadow outline, underline, italics, and strikeout. Because metafonts contain character size information, strings that use metafonts are more likely to have the same width across platforms. This value is an alias to an operating system font. Therefore, the operating system and user preferences on your machine determine this font. |
| VAL_7SEG_META_FONT | Font that provides compatibility with LabWindows for DOS. Metafonts contain typeface information, point size, and text styles such as bold, shadow outline, underline, italics, and strikeout. Because metafonts contain character size information, strings that use metafonts are more likely to have the same width across platforms. |
| VAL_SYSTEM_META_FONT | Font that provides compatibility with function panels and user interface panels from LabWindows for DOS that use extended IBM PC characters. Because other fonts may not contain these extended characters, cut/paste operations may fail. Metafonts contain typeface information, point size, and text styles such as bold, shadow outline, underline, italics, and strikeout. Because metafonts contain character size information, strings that use metafonts are more likely to have the same width across platforms. |

<!--NI_TOPIC bundle=labwindows-cvi path=cvi/uiref/cviattrylabelfontnamelength.htm language=enus -->
## TOPIC 00880: ATTR_YLABEL_FONT_NAME_LENGTH

- bundle_id: `labwindows-cvi`
- source_path: `cvi/uiref/cviattrylabelfontnamelength.htm`
- source_url: https://docs-be.ni.com/bundle/labwindows-cvi/raw/resource/enus/cvi/uiref/cviattrylabelfontnamelength.htm
- document_id: `labwindows-cvi`
- page_type: `leaf`
- content_type: ``

### ATTR_YLABEL_FONT_NAME_LENGTH

| Type: | Control attribute |
| --- | --- |
| Description: | The number of bytes in the name of the font for the y-axis label. The length does not include the ASCII NUL byte. Use this value to determine the size of the buffer to pass when you call GetCtrlAttribute and specify the ATTR_YLABEL_FONT attribute. |
| Control Types: | Digital graphs, graphs, strip charts. |
| Restrictions: | Not settable. |
| Data Type: | integer |
| LabWindows/CVICompatibility: | LabWindows/CVI 8.5 and later |

<!--NI_TOPIC bundle=labwindows-cvi path=cvi/uiref/cviattrylabelitalic.htm language=enus -->
## TOPIC 00881: ATTR_YLABEL_ITALIC

- bundle_id: `labwindows-cvi`
- source_path: `cvi/uiref/cviattrylabelitalic.htm`
- source_url: https://docs-be.ni.com/bundle/labwindows-cvi/raw/resource/enus/cvi/uiref/cviattrylabelitalic.htm
- document_id: `labwindows-cvi`
- page_type: `leaf`
- content_type: ``

### ATTR_YLABEL_ITALIC

| Type: | Control attribute |
| --- | --- |
| Description: | Specifies whether the y-axis label is in italics. 0 = Not italics 1 = Italics |
| Control Types: | Digital graphs, graphs, strip charts. |
| Data Type: | integer |
| Default Value: | 0 |
| LabWindows/CVICompatibility: | LabWindows/CVI 8.5 and later |

##### Values

| 0 | False |
| --- | --- |
| 1 | True |

<!--NI_TOPIC bundle=labwindows-cvi path=cvi/uiref/cviattrylabelpointsize.htm language=enus -->
## TOPIC 00882: ATTR_YLABEL_POINT_SIZE

- bundle_id: `labwindows-cvi`
- source_path: `cvi/uiref/cviattrylabelpointsize.htm`
- source_url: https://docs-be.ni.com/bundle/labwindows-cvi/raw/resource/enus/cvi/uiref/cviattrylabelpointsize.htm
- document_id: `labwindows-cvi`
- page_type: `leaf`
- content_type: ``

### ATTR_YLABEL_POINT_SIZE

| Type: | Control attribute |
| --- | --- |
| Description: | The font point size for the y-axis label. |
| Control Types: | Digital graphs, graphs, strip charts. |
| Data Type: | integer |
| Valid Range: | 1 to 255 |
| LabWindows/CVICompatibility: | LabWindows/CVI 8.5 and later |

<!--NI_TOPIC bundle=labwindows-cvi path=cvi/uiref/cviattrylabelstrikeout.htm language=enus -->
## TOPIC 00883: ATTR_YLABEL_STRIKEOUT

- bundle_id: `labwindows-cvi`
- source_path: `cvi/uiref/cviattrylabelstrikeout.htm`
- source_url: https://docs-be.ni.com/bundle/labwindows-cvi/raw/resource/enus/cvi/uiref/cviattrylabelstrikeout.htm
- document_id: `labwindows-cvi`
- page_type: `leaf`
- content_type: ``

### ATTR_YLABEL_STRIKEOUT

| Type: | Control attribute |
| --- | --- |
| Description: | Specifies whether the y-axis label has strikeout. 0 = No strikeout 1 = Strikeout |
| Control Types: | Digital graphs, graphs, strip charts. |
| Data Type: | integer |
| Default Value: | 0 |
| LabWindows/CVICompatibility: | LabWindows/CVI 8.5 and later |

##### Values

| 0 | False |
| --- | --- |
| 1 | True |

<!--NI_TOPIC bundle=labwindows-cvi path=cvi/uiref/cviattrylabelvisible.htm language=enus -->
## TOPIC 00884: ATTR_YLABEL_VISIBLE

- bundle_id: `labwindows-cvi`
- source_path: `cvi/uiref/cviattrylabelvisible.htm`
- source_url: https://docs-be.ni.com/bundle/labwindows-cvi/raw/resource/enus/cvi/uiref/cviattrylabelvisible.htm
- document_id: `labwindows-cvi`
- page_type: `leaf`
- content_type: ``

### ATTR_YLABEL_VISIBLE

| Type: | Control attribute |
| --- | --- |
| Description: | Specifies whether to show or hide the Y labels on the graph. 0 = Hide Y labels 1 = Show Y labels |
| Control Types: | Digital graphs, graphs, strip charts. |
| Data Type: | integer |
| Default Value: | 1 (left y axis), 0 (right y axis) |
| LabWindows/CVICompatibility: | LabWindows/CVI 3.0 and later |

##### Values

| 0 | False |
| --- | --- |
| 1 | True |

<!--NI_TOPIC bundle=labwindows-cvi path=cvi/uiref/cviattryloosefitautoscaling.htm language=enus -->
## TOPIC 00885: ATTR_YLOOSE_FIT_AUTOSCALING

- bundle_id: `labwindows-cvi`
- source_path: `cvi/uiref/cviattryloosefitautoscaling.htm`
- source_url: https://docs-be.ni.com/bundle/labwindows-cvi/raw/resource/enus/cvi/uiref/cviattryloosefitautoscaling.htm
- document_id: `labwindows-cvi`
- page_type: `leaf`
- content_type: ``

### ATTR_YLOOSE_FIT_AUTOSCALING

| Type: | Control attribute |
| --- | --- |
| Description: | Determines how the maximum and minimum values of the scale are calculated when autoscaling is enabled. If ATTR_YLOOSE_FIT_AUTOSCALING is FALSE, the maximum and minimum values of the scale are respectively the largest and smallest value of all plots. If ATTR_YLOOSE_FIT_AUTOSCALING is TRUE, the maximum and minimum values of the scale are calculated in accordance with the value of the ATTR_YLOOSE_FIT_AUTOSCALING_UNIT attribute. 0 = Do not use loose fit 1 = Use loose fit |
| Control Types: | Graphs, strip charts. |
| Data Type: | integer |
| Default Value: | 0 |
| LabWindows/CVICompatibility: | LabWindows/CVI 5.5 and later |

##### Values

| 0 | False |
| --- | --- |
| 1 | True |

<!--NI_TOPIC bundle=labwindows-cvi path=cvi/uiref/cviattryloosefitautoscalingunit.htm language=enus -->
## TOPIC 00886: ATTR_YLOOSE_FIT_AUTOSCALING_UNIT

- bundle_id: `labwindows-cvi`
- source_path: `cvi/uiref/cviattryloosefitautoscalingunit.htm`
- source_url: https://docs-be.ni.com/bundle/labwindows-cvi/raw/resource/enus/cvi/uiref/cviattryloosefitautoscalingunit.htm
- document_id: `labwindows-cvi`
- page_type: `leaf`
- content_type: ``

### ATTR_YLOOSE_FIT_AUTOSCALING_UNIT

| Type: | Control attribute |
| --- | --- |
| Description: | The base 10 logarithm of the loose fit factor. The loose fit factor determines how the maximum and minimum values of the scale are calculated when loose fit autoscaling is enabled. (Linear Scale) The maximum is the smallest multiple of the loose fit factor that is greater than or equal to the largest value of all plots. The minimum is likewise the largest multiple of the loose fit factor that is less than or equal to the smallest value of all plots. For example, if the loose fit unit value is 1, the loose fit factor is 10. In that case, if the largest value of all plots is 41 and the smallest value of all plots is 27, the new maximum is 50 and the new minimum is 20. (Logarithmic Scale) For a loose fit unit equal to 0, the maximum is the smallest decade that is greater than the largest value of all plots. The minimum is likewise the largest decade that is smaller than the smallest value of all plots. The decade is the power-multiple of 10 that is closest to the largest value or smallest value of all plots, respectively. Examples: Smallest value: 0.0234, new minimum: 0.01 Largest value: 0.0567, new maximum: .01 Smallest value: 3.45, new minimum: 1 Largest value: 5.678, new maximum: 10 For loose fit values other than 0, the loose fit unit is the offset of the position of the most significant digit. The most significant digit of a number is the first non-zero digit of the number regardless of the decimal point. Examples where the loose fit unit is 1: Smallest value: 0.0234, new minimum: 0.02 Largest value: 0.0567, new maximum: 0.06 Smallest value: 3.45, new minimum: 3 Largest value: 5.678, new maximum: 6 Examples where the loose fit unit is 2: Smallest value: 0.0234, new minimum: 0.023 Largest value: 0.0567, new maximum: 0.057 Smallest value: 3.45, new minimum: 3.4 Largest value: 5.678, new maximum: 5.7 |
| Control Types: | Graphs, strip charts. |
| Data Type: | integer |
| Valid Range: | -308 to 308 |
| Default Value: | 0 |
| LabWindows/CVICompatibility: | LabWindows/CVI 5.5 and later |

<!--NI_TOPIC bundle=labwindows-cvi path=cvi/uiref/cviattrymapmode.htm language=enus -->
## TOPIC 00887: ATTR_YMAP_MODE

- bundle_id: `labwindows-cvi`
- source_path: `cvi/uiref/cviattrymapmode.htm`
- source_url: https://docs-be.ni.com/bundle/labwindows-cvi/raw/resource/enus/cvi/uiref/cviattrymapmode.htm
- document_id: `labwindows-cvi`
- page_type: `leaf`
- content_type: ``

### ATTR_YMAP_MODE

| Type: | Control attribute |
| --- | --- |
| Description: | The display format of the y-axis. For log scaling, the minimum value of the axis must be greater than zero. |
| Control Types: | Graphs, strip charts. |
| Data Type: | integer |
| Default Value: | VAL_LINEAR |
| LabWindows/CVICompatibility: | LabWindows/CVI 3.0 and later |

##### Values

| VAL_LINEAR | Use a linear scale for the graph axis. |
| --- | --- |
| VAL_LOG | Use a logarithmic scale for the graph axis. The minimum axis value must be greater than zero. |

<!--NI_TOPIC bundle=labwindows-cvi path=cvi/uiref/cviattrymarkorigin.htm language=enus -->
## TOPIC 00888: ATTR_YMARK_ORIGIN

- bundle_id: `labwindows-cvi`
- source_path: `cvi/uiref/cviattrymarkorigin.htm`
- source_url: https://docs-be.ni.com/bundle/labwindows-cvi/raw/resource/enus/cvi/uiref/cviattrymarkorigin.htm
- document_id: `labwindows-cvi`
- page_type: `leaf`
- content_type: ``

### ATTR_YMARK_ORIGIN

| Type: | Control attribute |
| --- | --- |
| Description: | Specifies whether to show or hide the Y-origin tick marks. 0 = Hide tick marks 1 = Show tick marks |
| Control Types: | Graphs. |
| Data Type: | integer |
| Default Value: | 1 |
| LabWindows/CVICompatibility: | LabWindows/CVI 3.0 and later |

##### Values

| 0 | False |
| --- | --- |
| 1 | True |

<!--NI_TOPIC bundle=labwindows-cvi path=cvi/uiref/cviattryminorgridvisible.htm language=enus -->
## TOPIC 00889: ATTR_YMINORGRID_VISIBLE

- bundle_id: `labwindows-cvi`
- source_path: `cvi/uiref/cviattryminorgridvisible.htm`
- source_url: https://docs-be.ni.com/bundle/labwindows-cvi/raw/resource/enus/cvi/uiref/cviattryminorgridvisible.htm
- document_id: `labwindows-cvi`
- page_type: `leaf`
- content_type: ``

### ATTR_YMINORGRID_VISIBLE

| Type: | Control attribute |
| --- | --- |
| Description: | Specifies whether to show or hide the minor grid lines for the y-axis on the graph. In order for the minor grid lines to be visible, you must also enable the ATTR_YGRID_VISIBLE attribute. The number of minor grid lines that are visible when this attribute is enabled is proportional to the space between consecutive major grid lines. In some cases, when this space is too small, it's possible for this number to be zero. 0 = Hide inner grid lines 1 = Show inner grid lines |
| Control Types: | Graphs, strip charts. |
| Data Type: | integer |
| Default Value: | 0 |
| LabWindows/CVICompatibility: | LabWindows/CVI 7.0 and later |

##### Values

| 0 | False |
| --- | --- |
| 1 | True |

<!--NI_TOPIC bundle=labwindows-cvi path=cvi/uiref/cviattryname.htm language=enus -->
## TOPIC 00890: ATTR_YNAME

- bundle_id: `labwindows-cvi`
- source_path: `cvi/uiref/cviattryname.htm`
- source_url: https://docs-be.ni.com/bundle/labwindows-cvi/raw/resource/enus/cvi/uiref/cviattryname.htm
- document_id: `labwindows-cvi`
- page_type: `leaf`
- content_type: ``

### ATTR_YNAME

| Type: | Control attribute |
| --- | --- |
| Description: | The text name to display for the Y-axis. To determine the size of the buffer to pass when you are obtaining the name, call GetCtrlAttribute and specify the ATTR_YNAME_LENGTH attribute. |
| Control Types: | Digital graphs, graphs, strip charts. |
| Data Type: | string |
| LabWindows/CVICompatibility: | LabWindows/CVI 3.0 and later |

<!--NI_TOPIC bundle=labwindows-cvi path=cvi/uiref/cviattrynamelength.htm language=enus -->
## TOPIC 00891: ATTR_YNAME_LENGTH

- bundle_id: `labwindows-cvi`
- source_path: `cvi/uiref/cviattrynamelength.htm`
- source_url: https://docs-be.ni.com/bundle/labwindows-cvi/raw/resource/enus/cvi/uiref/cviattrynamelength.htm
- document_id: `labwindows-cvi`
- page_type: `leaf`
- content_type: ``

### ATTR_YNAME_LENGTH

| Type: | Control attribute |
| --- | --- |
| Description: | The number of bytes in the Y-axis text name. The length does not include the ASCII NUL byte. Use this value to determine the size of the buffer to pass when you call GetCtrlAttribute and specify the ATTR_YNAME attribute. |
| Control Types: | Digital graphs, graphs, strip charts. |
| Restrictions: | Not settable. |
| Data Type: | integer |
| LabWindows/CVICompatibility: | LabWindows/CVI 3.0 and later |

<!--NI_TOPIC bundle=labwindows-cvi path=cvi/uiref/cviattryoffset.htm language=enus -->
## TOPIC 00892: ATTR_YOFFSET

- bundle_id: `labwindows-cvi`
- source_path: `cvi/uiref/cviattryoffset.htm`
- source_url: https://docs-be.ni.com/bundle/labwindows-cvi/raw/resource/enus/cvi/uiref/cviattryoffset.htm
- document_id: `labwindows-cvi`
- page_type: `leaf`
- content_type: ``

### ATTR_YOFFSET

| Type: | Print attribute |
| --- | --- |
| Description: | Sets the Y offset of the hardcopy image on the paper. The offset is expressed in tenths of millimeters. The offset is relative to the top edge of the paper as seen in portrait mode, regardless of the ATTR_ORIENTATION setting. A value of 0 forces the image to what you see as the "top" edge when looking at the paper in portrait mode. This is equivalent to what you see as the "left" edge when looking at the paper in landscape mode. VAL_CENTER_ON_PAPER centers the image in the Y direction. (Note: VAL_CENTER_ON_PAPER was formerly called VAL_USE_PRINTER_DEFAULT.) |
| Types of Printing: | Graphics. |
| Data Type: | integer |
| Valid Range: | 0 or greater, or VAL_CENTER_ON_PAPER. |
| Default Value: | VAL_CENTER_ON_PAPER. |
| LabWindows/CVICompatibility: | LabWindows/CVI 3.0 and later |

##### Values

| VAL_CENTER_ON_PAPER | Center the output on the paper. (This value was formerly called VAL_USE_PRINTER_DEFAULT). |
| --- | --- |

<!--NI_TOPIC bundle=labwindows-cvi path=cvi/uiref/cviattrypadding.htm language=enus -->
## TOPIC 00893: ATTR_YPADDING

- bundle_id: `labwindows-cvi`
- source_path: `cvi/uiref/cviattrypadding.htm`
- source_url: https://docs-be.ni.com/bundle/labwindows-cvi/raw/resource/enus/cvi/uiref/cviattrypadding.htm
- document_id: `labwindows-cvi`
- page_type: `leaf`
- content_type: ``

### ATTR_YPADDING

| Type: | Control attribute |
| --- | --- |
| Description: | The minimum number of characters to display in the Y-axis labels. This pads the labels with zeros to ensure that they are at least the minimum length. If the length of the labels are greater than the minimum, the Y-axis labels will display the complete number even if they exceed the minimum number of characters. |
| Control Types: | Graphs, strip charts. |
| Data Type: | integer |
| Valid Range: | 0 to 64 |
| Default Value: | 0 |
| LabWindows/CVICompatibility: | LabWindows/CVI 5.5 and later |

<!--NI_TOPIC bundle=labwindows-cvi path=cvi/uiref/cviattryprecision.htm language=enus -->
## TOPIC 00894: ATTR_YPRECISION

- bundle_id: `labwindows-cvi`
- source_path: `cvi/uiref/cviattryprecision.htm`
- source_url: https://docs-be.ni.com/bundle/labwindows-cvi/raw/resource/enus/cvi/uiref/cviattryprecision.htm
- document_id: `labwindows-cvi`
- page_type: `leaf`
- content_type: ``

### ATTR_YPRECISION

| Type: | Control attribute |
| --- | --- |
| Description: | The number of characters after the decimal point to display in the numeric Y-axis labels. If ATTR_YFORMAT is set to VAL_ABSOLUTE_TIME_FORMAT or VAL_RELATIVE_TIME_FORMAT, specifies the default precision for the fractional part of the seconds. |
| Control Types: | Graphs, strip charts. |
| Data Type: | integer |
| Valid Range: | 0 to 15, or VAL_AUTO |
| Default Value: | VAL_AUTO (graphs), 1 (strip charts) |
| LabWindows/CVICompatibility: | LabWindows/CVI 3.0 and later |

##### Values

| VAL_AUTO |
| --- |

<!--NI_TOPIC bundle=labwindows-cvi path=cvi/uiref/cviattryreverse.htm language=enus -->
## TOPIC 00895: ATTR_YREVERSE

- bundle_id: `labwindows-cvi`
- source_path: `cvi/uiref/cviattryreverse.htm`
- source_url: https://docs-be.ni.com/bundle/labwindows-cvi/raw/resource/enus/cvi/uiref/cviattryreverse.htm
- document_id: `labwindows-cvi`
- page_type: `leaf`
- content_type: ``

### ATTR_YREVERSE

| Type: | Control attribute |
| --- | --- |
| Description: | Determines whether to reverse the orientation of the y-axis so that the lowest value is shown at the top. If the orientation of the y-axis is reversed, the vertical orientation of the plots is also reversed. 0 = do not reverse 1 = reverse |
| Control Types: | Graphs, strip charts. |
| Data Type: | integer |
| Default Value: | 0 |
| LabWindows/CVICompatibility: | LabWindows/CVI 4.0 and later |

##### Values

| 0 | False |
| --- | --- |
| 1 | True |

<!--NI_TOPIC bundle=labwindows-cvi path=cvi/uiref/cviattrzplaneposition_panel.htm language=enus -->
## TOPIC 00896: ATTR_ZPLANE_POSITION (Panel)

- bundle_id: `labwindows-cvi`
- source_path: `cvi/uiref/cviattrzplaneposition_panel.htm`
- source_url: https://docs-be.ni.com/bundle/labwindows-cvi/raw/resource/enus/cvi/uiref/cviattrzplaneposition_panel.htm
- document_id: `labwindows-cvi`
- page_type: `leaf`
- content_type: ``

### ATTR_ZPLANE_POSITION (Panel)

| Type: | Panel attribute |
| --- | --- |
| Description: | The drawing order of the child panel. The panel with the lowest number (0) is drawn last (i.e., on top). |
| Restrictions: | Valid for child panels only. |
| Data Type: | integer |
| LabWindows/CVICompatibility: | LabWindows/CVI 3.0 and later |

<!--NI_TOPIC bundle=labwindows-cvi path=cvi/uiref/cvibatch_drawing_and_multithreading.htm language=enus -->
## TOPIC 00897: Batch Drawing and Multithreading

- bundle_id: `labwindows-cvi`
- source_path: `cvi/uiref/cvibatch_drawing_and_multithreading.htm`
- source_url: https://docs-be.ni.com/bundle/labwindows-cvi/raw/resource/enus/cvi/uiref/cvibatch_drawing_and_multithreading.htm
- document_id: `labwindows-cvi`
- page_type: `leaf`
- content_type: ``

### Batch Drawing and Multithreading

While [batch drawing](cviprogramming_with_canvas_controls.htm) is in effect on a [canvas control](cvicanvas_control_overview.htm), do not access a control from any other [thread](cvidifferent_approaches_to_multithr.htm).

<!--NI_TOPIC bundle=labwindows-cvi path=cvi/uiref/cvibinary_switch_attributes.htm language=enus -->
## TOPIC 00898: Binary Switch Control Attributes

- bundle_id: `labwindows-cvi`
- source_path: `cvi/uiref/cvibinary_switch_attributes.htm`
- source_url: https://docs-be.ni.com/bundle/labwindows-cvi/raw/resource/enus/cvi/uiref/cvibinary_switch_attributes.htm
- document_id: `labwindows-cvi`
- page_type: `leaf`
- content_type: ``

### Binary Switch Control Attributes

The User Interface Library attributes that are valid for
[binary switch](cvibinary_switch_control_overview.htm)
controls appear in the following list:

#### Control Appearance

- Binary Switch Color
- Disable Panel Theme
- Off Text
- On Text
- Visible
- Size/Position
- Text Style

#### Control Settings

- Control Mode
- Control Style
- Control Value
- Data Type
- Default Value
- Default Value Length
- Dimmed
- Disable Control Tooltip
- Next Panel Control
- Off Text Length
- Off Value
- Off Value Length
- On Text Length
- On Value
- On Value Length
- Tab Position
- Tooltip Delay
- Tooltip Hide Delay
- Tooltip Text
- Tooltip Text Length
- Z-Plane Position
- Index

#### Label Appearance

- Label Background Color
- Label Height
- Label Left
- Label Raised
- Label Size to Text
- Label Text
- Label Text Length
- Label Top
- Label Visible
- Label Width
- Label Style

#### Source Code Connection

- Callback Data
- Callback Function Name
- Callback Function Name Length
- Callback Function Pointer
- Constant Name
- Constant Name Length

<!--NI_TOPIC bundle=labwindows-cvi path=cvi/uiref/cvibinary_switch_control_events.htm language=enus -->
## TOPIC 00899: Binary Switch Control Events

- bundle_id: `labwindows-cvi`
- source_path: `cvi/uiref/cvibinary_switch_control_events.htm`
- source_url: https://docs-be.ni.com/bundle/labwindows-cvi/raw/resource/enus/cvi/uiref/cvibinary_switch_control_events.htm
- document_id: `labwindows-cvi`
- page_type: `leaf`
- content_type: ``

### Binary Switch Control Events

The following User Interface Library [events](cvievents_overview.htm) are sent to [binary switch](cvibinary_switch_control_overview.htm) control [callback](cviusing_callback_functions_to_resp.htm) functions.

- EVENT_COMMIT
- EVENT_VAL_CHANGED
- EVENT_LEFT_CLICK
- EVENT_LEFT_DOUBLE_CLICK
- EVENT_RIGHT_CLICK
- EVENT_RIGHT_DOUBLE_CLICK
- EVENT_KEYPRESS
- EVENT_GOT_FOCUS
- EVENT_LOST_FOCUS
- EVENT_DISCARD
- EVENT_MOUSE_POINTER_MOVE
- EVENT_LEFT_CLICK_UP
- EVENT_RIGHT_CLICK_UP
- EVENT_MOUSE_WHEEL_SCROLL
- EVENT_MOUSE_WHEEL_CLICK

<!--NI_TOPIC bundle=labwindows-cvi path=cvi/uiref/cvicanvas_control_functions.htm language=enus -->
## TOPIC 00900: Canvas Control Functions

- bundle_id: `labwindows-cvi`
- source_path: `cvi/uiref/cvicanvas_control_functions.htm`
- source_url: https://docs-be.ni.com/bundle/labwindows-cvi/raw/resource/enus/cvi/uiref/cvicanvas_control_functions.htm
- document_id: `labwindows-cvi`
- page_type: `leaf`
- content_type: ``

### Canvas Control Functions

The following User Interface Library functions operate on [canvas](cvicanvas_control_overview.htm) controls.

- AddCtrlToSplitter
- CanvasClear
- CanvasDefaultPen
- CanvasDimRect
- CanvasDrawArc
- CanvasDrawBitmap
- CanvasDrawLine
- CanvasDrawLineTo
- CanvasDrawOval
- CanvasDrawPoint
- CanvasDrawPoly
- CanvasDrawRect
- CanvasDrawRoundedRect
- CanvasDrawText
- CanvasDrawTextAtPoint
- CanvasEndBatchDraw
- CanvasGetClipRect
- CanvasGetPenPosition
- CanvasGetPixel
- CanvasGetPixels
- CanvasInvertRect
- CanvasScroll
- CanvasSetClipRect
- CanvasSetPenPosition
- CanvasStartBatchDraw
- CanvasUpdate
- DiscardCtrl
- DuplicateCtrl
- GetCtrlArrayIndex
- GetCtrlAttribute
- GetCtrlBitmap
- GetCtrlBoundingRect
- GetCtrlDisplayBitmap
- GetRelativeMouseState
- GetScaledCtrlDisplayBitmap
- InsertCtrlArrayItem
- InstallCtrlCallback
- PrintCtrl
- QueueUserEvent
- RemoveCtrlFromSplitter
- SetActiveCtrl
- SetCtrlAttribute
- SetInputMode

<!--NI_TOPIC bundle=labwindows-cvi path=cvi/uiref/cvicanvas_control_overview.htm language=enus -->
## TOPIC 00901: Canvas Controls Overview

- bundle_id: `labwindows-cvi`
- source_path: `cvi/uiref/cvicanvas_control_overview.htm`
- source_url: https://docs-be.ni.com/bundle/labwindows-cvi/raw/resource/enus/cvi/uiref/cvicanvas_control_overview.htm
- document_id: `labwindows-cvi`
- page_type: `leaf`
- content_type: ``

### Canvas Controls Overview

Use *canvas [controls](cvioperating_controls.htm)* as an arbitrary drawing surface. You can draw text, shapes, and [bitmap](cviusing_bitmap_objects.htm) images. LabWindows/CVI maintains an off-screen bitmap so that it can restore
the appearance of the canvas when the region is exposed. A sample canvas
control appears in the following figure.

[IMAGE alt='image' src='canvas.gif']

**Canvas Control**

[Operating Canvas Controls](cvioperating_canvas_controls.htm)

[Programming Canvas Controls](cviprogramming_with_canvas_controls.htm)

[Canvas Control Attributes](cvicanvas_attributes.htm)

[Canvas Control Functions](cvicanvas_control_functions.htm)

[Canvas Control Events](cvicanvas_control_events.htm)

<!--NI_TOPIC bundle=labwindows-cvi path=cvi/uiref/cvicanvasdefaultpen.htm language=enus -->
## TOPIC 00902: CanvasDefaultPen

- bundle_id: `labwindows-cvi`
- source_path: `cvi/uiref/cvicanvasdefaultpen.htm`
- source_url: https://docs-be.ni.com/bundle/labwindows-cvi/raw/resource/enus/cvi/uiref/cvicanvasdefaultpen.htm
- document_id: `labwindows-cvi`
- page_type: `leaf`
- content_type: ``

### CanvasDefaultPen

int CanvasDefaultPen (int panelHandle, int controlID);

#### Purpose

Sets all of the attributes of the canvas pen to the default values. The defaults appear in the following table.

| Canvas Pen Attribute | Default Value |
| --- | --- |
| ATTR_PEN_WIDTH | 1 |
| ATTR_PEN_STYLE | VAL_SOLID |
| ATTR_PEN_COLOR | VAL_BLACK |
| ATTR_PEN_FILL_COLOR | VAL_BLACK |
| ATTR_PEN_MODE | VAL_COPY_MODE |
| ATTR_PEN_PATTERN | A solid pattern, expressed as an array of eight unsigned characters, each of which is 0xFF. |

#### Supported Controls

You can use CanvasDefaultPen with [canvas controls](../../cvi/uiref/cviprogramming_with_canvas_controls.htm).

#### Parameters

| Input |  |  |
| --- | --- | --- |
| Name | Type | Description |
| panelHandle | int | Specifier for a particular panel that is currently in memory. You can obtain this handle from functions such as LoadPanel and NewPanel. |
| controlID | int | The defined constant, located in the .uir header file, that you assigned to the control in the User Interface Editor, or the ID returned by functions such as NewCtrl and DuplicateCtrl. |

#### Return Value

| Name | Type | Description |
| --- | --- | --- |
| status | int | Return value indicating whether the function was successful. A negative number indicates that an error occurred. |

#### Additional Information

**Library:** [User Interface Library](../../cvi/uiref/cviuser_interface_library_function_tree.htm)

**Include file:** userint.h

**LabWindows/CVI compatibility:** LabWindows/CVI 4.0 and later

<!--NI_TOPIC bundle=labwindows-cvi path=cvi/uiref/cvicanvasdimrect.htm language=enus -->
## TOPIC 00903: CanvasDimRect

- bundle_id: `labwindows-cvi`
- source_path: `cvi/uiref/cvicanvasdimrect.htm`
- source_url: https://docs-be.ni.com/bundle/labwindows-cvi/raw/resource/enus/cvi/uiref/cvicanvasdimrect.htm
- document_id: `labwindows-cvi`
- page_type: `leaf`
- content_type: ``

### CanvasDimRect

int CanvasDimRect (int panelHandle, int controlID, Rect rectangle);

#### Purpose

Overlays a partially opaque color field onto the specified rectangular area of a canvas
control. This operation has the visual effect of dimming objects within this area.

CanvasDimRect uses as its color the current value of the ATTR_PEN_FILL_COLOR attribute.

#### Supported Controls

You can use CanvasDimRect with [canvas controls](../../cvi/uiref/cviprogramming_with_canvas_controls.htm).

#### Parameters

| Input |  |  |
| --- | --- | --- |
| Name | Type | Description |
| panelHandle | int | Specifier for a particular panel that is currently in memory. You can obtain this handle from functions such as LoadPanel and NewPanel. |
| controlID | int | The defined constant, located in the .uir header file, that you assigned to the control in the User Interface Editor, or the ID returned by functions such as NewCtrl and DuplicateCtrl. |
| rectangle | Rect | Rect structure specifying the location and size of the area to be dimmed. Use VAL_ENTIRE_OBJECT to specify the entire canvas. The Rect structure is defined as follows: typedef struct { int top; int left; int height; int width; } Rect; You can create a Rect without having to declare a variable by using the following function: Rect MakeRect (int top, int left, int height, int width); Example CanvasDimRect (panelHandle, controlID, MakeRect(20,30,150,200)); |

#### Return Value

| Name | Type | Description |
| --- | --- | --- |
| status | int | Return value indicating whether the function was successful. A negative number indicates that an error occurred. |

#### Additional Information

**Library:** [User Interface Library](../../cvi/uiref/cviuser_interface_library_function_tree.htm)

**Include file:** userint.h

**LabWindows/CVI compatibility:** LabWindows/CVI 4.0 and later

<!--NI_TOPIC bundle=labwindows-cvi path=cvi/uiref/cvicanvasdrawarc.htm language=enus -->
## TOPIC 00904: CanvasDrawArc

- bundle_id: `labwindows-cvi`
- source_path: `cvi/uiref/cvicanvasdrawarc.htm`
- source_url: https://docs-be.ni.com/bundle/labwindows-cvi/raw/resource/enus/cvi/uiref/cvicanvasdrawarc.htm
- document_id: `labwindows-cvi`
- page_type: `leaf`
- content_type: ``

### CanvasDrawArc

int CanvasDrawArc (int panelHandle, int controlID, Rect rectangle, int beginningAngle, int arcAngle, int drawMode);

#### Purpose

Draws an arc on the canvas control. Define the arc by specifying a rectangle that encloses the arc, along with a beginning angle, in tenths of degrees, and an arc angle, in tenths of degrees.

The arc is a section of an oval. A beginning angle of 0 indicates that the arc starts at the midpoint of the right edge of the rectangle. The arc angle indicates how far around the oval, counter-clockwise, up to 3,600, to extend the arc.

CanvasDrawArc draws the frame of the arc using the current value of the following attributes:

ATTR_PEN_COLOR 

ATTR_PEN_MODE 

ATTR_PEN_WIDTH 

ATTR_PEN_STYLE (ignored when pen width is greater than one)

CanvasDrawArc draws interior of the arc using the current value of the following attributes:

ATTR_PEN_FILL_COLOR 

ATTR_PEN_MODE 

ATTR_PEN_PATTERN

The frame of the arc does not include the radius lines going from the center of the oval to the end points of the arc.

#### Supported Controls

You can use CanvasDrawArc with [canvas controls](../../cvi/uiref/cviprogramming_with_canvas_controls.htm).

#### Parameters

| Input |  |  |
| --- | --- | --- |
| Name | Type | Description |
| panelHandle | int | Specifier for a particular panel that is currently in memory. You can obtain this handle from functions such as LoadPanel and NewPanel. |
| controlID | int | The defined constant, located in the .uir header file, that you assigned to the control in the User Interface Editor, or the ID returned by functions such as NewCtrl and DuplicateCtrl. |
| rectangle | Rect | Rect structure specifying the location and size of the rectangle within which to draw the arc. The Rect structure is defined as follows: typedef struct { int top; int left; int height; int width; } Rect; You can create a Rect without having to declare a variable by using the following function: Rect MakeRect (int top, int left, int height, int width); Example CanvasDrawArc (panelHandle, controlID, MakeRect(20,30,150,200), 0, 90, VAL_DRAW_FRAME); |
| beginningAngle | int | Starting angle of the arc, in tenths of degrees. 0 indicates the arc starts at the midpoint of the right edge of the rectangle. 900 indicates that the arc starts at the midpoint of the top edge of the rectangle. Negative values are valid. |
| arcAngle | int | Indicates how far around the oval, counter-clockwise, up to 3,600, to extend the arc. This value is specified in tenths of degrees. If the beginning angle is 900 and the arc angle is 1,800, the arc is drawn from the midpoint of the top edge of the rectangle to the midpoint of the bottom edge. Negative values are valid. |
| drawMode | int | Specifies whether to draw the arc frame, or interior, or both. The following lists the valid values. VAL_DRAW_FRAME VAL_DRAW_INTERIOR VAL_DRAW_FRAME_AND_INTERIOR The frame of the arc does not include the radius lines going from the center of the oval to the end points of the arc. |

#### Return Value

| Name | Type | Description |
| --- | --- | --- |
| status | int | Return value indicating whether the function was successful. A negative number indicates that an error occurred. |

#### Additional Information

**Library:** [User Interface Library](../../cvi/uiref/cviuser_interface_library_function_tree.htm)

**Include file:** userint.h

**LabWindows/CVI compatibility:** LabWindows/CVI 4.0 and later

#### Example

Refer to userint\canvas.cws for an example of using the CanvasDrawArc function.

<!--NI_TOPIC bundle=labwindows-cvi path=cvi/uiref/cvicanvasdrawbitmap.htm language=enus -->
## TOPIC 00905: CanvasDrawBitmap

- bundle_id: `labwindows-cvi`
- source_path: `cvi/uiref/cvicanvasdrawbitmap.htm`
- source_url: https://docs-be.ni.com/bundle/labwindows-cvi/raw/resource/enus/cvi/uiref/cvicanvasdrawbitmap.htm
- document_id: `labwindows-cvi`
- page_type: `leaf`
- content_type: ``

### CanvasDrawBitmap

int CanvasDrawBitmap (int panelHandle, int controlID, int bitmapID, Rect sourceRectangle, Rect destinationRectangle);

#### Purpose

Draws a bitmap image, or portion thereof, in the destination rectangle that you
specify on a canvas control.

|  | Note Canvas controls do not support partial transparency; each pixel is either opaque or fully transparent. If you use this function to draw a bitmap containing an alpha channel over some region of a transparent canvas, that region will no longer be transparent. If you need to overlay a bitmap with an alpha channel on top of a transparent canvas, create a transparent picture control, associate the bitmap with the picture control, and then place the picture control over the canvas. |
| --- | --- |

##### Example Code

The following code copies a bitmap image, without any stretching or shrinking,
to the canvas control, starting 20 pixels below the top edge of the canvas, and 30 pixels to the right of left edge of the canvas:

CanvasDrawBitmap (panelHandle, controlID, bitmapID, VAL_ENTIRE_OBJECT, MakeRect(20,30, VAL_KEEP_SAME_SIZE, VAL_KEEP_SAME_SIZE));

#### Supported Controls

You can use CanvasDrawBitmap with [canvas controls](../../cvi/uiref/cviprogramming_with_canvas_controls.htm).

#### Parameters

| Input |  |  |
| --- | --- | --- |
| Name | Type | Description |
| panelHandle | int | Specifier for a particular panel that is currently in memory. You can obtain this handle from functions such as LoadPanel and NewPanel. |
| controlID | int | The defined constant, located in the .uir header file, that you assigned to the control in the User Interface Editor, or the ID returned by functions such as NewCtrl and DuplicateCtrl. |
| bitmapID | int | ID of the bitmap object that contains the image. You can obtain the ID from functions such as NewBitmapEx and GetCtrlBitmap. |
| sourceRectangle | Rect | Rect structure specifying the portion of the bitmap to draw. The values are in terms of the pixel coordinates of the bitmap. The origin (0,0) is at the upper left corner of the bitmap. The Rect structure is defined as follows: typedef struct { int top; int left; int height; int width; } Rect; You can create a Rect without having to declare a variable by using the following function: Rect MakeRect (int top, int left, int height, int width); Use VAL_ENTIRE_OBJECT to specify the entire image. Example CanvasDrawBitmap (panelHandle, controlID, bitmapID, VAL_ENTIRE_OBJECT, destinationRect); |
| destinationRectangle | Rect | Rect structure specifying the size and location of the area in which to draw the bitmap image on the canvas control. If sourceRect and destinationRect are not the same size, the bitmap stretches or shrinks to fit. The Rect structure is defined as follows: typedef struct { int top; int left; int height; int width; } Rect; You can create a Rect without having to declare a variable by using the following function: Rect MakeRect (int top, int left, int height, int width); Use VAL_ENTIRE_OBJECT to specify the entire image. If you want the bitmap to stretch to fit the size of the canvas, pass VAL_ENTIRE_OBJECT as destinationRect. Example CanvasDrawBitmap (panelHandle, controlID, bitmapID, sourceRectangle, MakeRect(20,30, VAL_KEEP_SAME_SIZE, VAL_KEEP_SAME_SIZE)); |

#### Return Value

| Name | Type | Description |
| --- | --- | --- |
| status | int | Return value indicating whether the function was successful. A negative number indicates that an error occurred. |

#### Additional Information

**Library:** [User Interface Library](../../cvi/uiref/cviuser_interface_library_function_tree.htm)

**Include file:** userint.h

**LabWindows/CVI compatibility:** LabWindows/CVI 4.0 and later

#### Examples

Refer to the following examples that use the CanvasDrawBitmap function:

- toolbox\msgdemo.cws 
 [IMAGE alt='image' src='open.gif'] Open example
- userint\alphablend.cws 
 [IMAGE alt='image' src='open.gif'] Open example
- userint\canvas.cws 
 [IMAGE alt='image' src='open.gif'] Open example
- userint\clipbord.cws 
 [IMAGE alt='image' src='open.gif'] Open example

<!--NI_TOPIC bundle=labwindows-cvi path=cvi/uiref/cvicanvasdrawline.htm language=enus -->
## TOPIC 00906: CanvasDrawLine

- bundle_id: `labwindows-cvi`
- source_path: `cvi/uiref/cvicanvasdrawline.htm`
- source_url: https://docs-be.ni.com/bundle/labwindows-cvi/raw/resource/enus/cvi/uiref/cvicanvasdrawline.htm
- document_id: `labwindows-cvi`
- page_type: `leaf`
- content_type: ``

### CanvasDrawLine

int CanvasDrawLine (int panelHandle, int controlID, Point start, Point end);

#### Purpose

Draws a line between two specified points.

CanvasDrawLine draws the line using the current value of the following attributes:

ATTR_PEN_COLOR 

ATTR_PEN_MODE 

ATTR_PEN_WIDTH 

ATTR_PEN_STYLE (ignored when pen width is greater than one)

#### Supported Controls

You can use CanvasDrawLine with [canvas controls](../../cvi/uiref/cviprogramming_with_canvas_controls.htm).

#### Parameters

| Input |  |  |
| --- | --- | --- |
| Name | Type | Description |
| panelHandle | int | Specifier for a particular panel that is currently in memory. You can obtain this handle from functions such as LoadPanel and NewPanel. |
| controlID | int | The defined constant, located in the .uir header file, that you assigned to the control in the User Interface Editor, or the ID returned by functions such as NewCtrl and DuplicateCtrl. |
| start | Point | Point structure specifying the location at which the line begins. The Point structure is defined as follows: typedef struct { int x; int y; } Point; You can create a Point without having to declare a variable by using the following function: Point MakePoint (int x, int y); Example CanvasDrawLine (panelHandle, controlID, MakePoint (20, 30), endPoint); |
| end | Point | Point structure specifying the location at which the line ends. The Point structure is defined as follows: typedef struct { int x; int y; } Point; You can create a Point without having to declare a variable by using the following function: Point MakePoint (int x, int y); Example CanvasDrawLine (panelHandle, controlID, startPoint, MakePoint (90, 80)); |

#### Return Value

| Name | Type | Description |
| --- | --- | --- |
| status | int | Return value indicating whether the function was successful. A negative number indicates that an error occurred. |

#### Additional Information

**Library:** [User Interface Library](../../cvi/uiref/cviuser_interface_library_function_tree.htm)

**Include file:** userint.h

**LabWindows/CVI compatibility:** LabWindows/CVI 4.0 and later

#### Example

Refer to userint\canvas.cws for an example of using the CanvasDrawLine function.

<!--NI_TOPIC bundle=labwindows-cvi path=cvi/uiref/cvicanvasdrawlineto.htm language=enus -->
## TOPIC 00907: CanvasDrawLineTo

- bundle_id: `labwindows-cvi`
- source_path: `cvi/uiref/cvicanvasdrawlineto.htm`
- source_url: https://docs-be.ni.com/bundle/labwindows-cvi/raw/resource/enus/cvi/uiref/cvicanvasdrawlineto.htm
- document_id: `labwindows-cvi`
- page_type: `leaf`
- content_type: ``

### CanvasDrawLineTo

int CanvasDrawLineTo (int panelHandle, int controlID, Point end);

#### Purpose

Draws a line between the current pen position and an end point you specify, and sets the pen position to the end point.

CanvasDrawLineTo draws the line using the current value of the following attributes:

ATTR_PEN_COLOR 

ATTR_PEN_MODE 

ATTR_PEN_WIDTH 

ATTR_PEN_STYLE (ignored when pen width is greater than one)

#### Supported Controls

You can use CanvasDrawLineTo with [canvas controls](../../cvi/uiref/cviprogramming_with_canvas_controls.htm).

#### Parameters

| Input |  |  |
| --- | --- | --- |
| Name | Type | Description |
| panelHandle | int | Specifier for a particular panel that is currently in memory. You can obtain this handle from functions such as LoadPanel and NewPanel. |
| controlID | int | The defined constant, located in the .uir header file, that you assigned to the control in the User Interface Editor, or the ID returned by functions such as NewCtrl and DuplicateCtrl. |
| end | Point | Point structure specifying the location at which the line ends. The Point structure is defined as follows: typedef struct { int x; int y; } Point; You can create a Point without having to declare a variable by using the following function: Point MakePoint (int x, int y); Example CanvasDrawLineTo (panelHandle, controlID, MakePoint (90, 80)); |

#### Return Value

| Name | Type | Description |
| --- | --- | --- |
| status | int | Return value indicating whether the function was successful. A negative number indicates that an error occurred. |

#### Additional Information

**Library:** [User Interface Library](../../cvi/uiref/cviuser_interface_library_function_tree.htm)

**Include file:** userint.h

**LabWindows/CVI compatibility:** LabWindows/CVI 4.0 and later

#### Examples

Refer to the following examples that use the CanvasDrawLineTo function:

- userint\canvas.cws 
 [IMAGE alt='image' src='open.gif'] Open example
- userint\canvsbmk.cws 
 [IMAGE alt='image' src='open.gif'] Open example

<!--NI_TOPIC bundle=labwindows-cvi path=cvi/uiref/cvicanvasdrawoval.htm language=enus -->
## TOPIC 00908: CanvasDrawOval

- bundle_id: `labwindows-cvi`
- source_path: `cvi/uiref/cvicanvasdrawoval.htm`
- source_url: https://docs-be.ni.com/bundle/labwindows-cvi/raw/resource/enus/cvi/uiref/cvicanvasdrawoval.htm
- document_id: `labwindows-cvi`
- page_type: `leaf`
- content_type: ``

### CanvasDrawOval

int CanvasDrawOval (int panelHandle, int controlID, Rect rectangle, int drawMode);

#### Purpose

Draws an oval on the canvas control within the specified rectangle.

CanvasDrawOval draws the frame of the oval using the current value of the following attributes:

ATTR_PEN_COLOR 

ATTR_PEN_MODE 

ATTR_PEN_WIDTH 

ATTR_PEN_STYLE (ignored when pen width is greater than one)

CanvasDrawOval draws the interior of the oval using the current value of the following attributes:

ATTR_PEN_FILL_COLOR 

ATTR_PEN_MODE 

ATTR_PEN_PATTERN

#### Supported Controls

You can use CanvasDrawOval with [canvas controls](../../cvi/uiref/cviprogramming_with_canvas_controls.htm).

#### Parameters

| Input |  |  |
| --- | --- | --- |
| Name | Type | Description |
| panelHandle | int | Specifier for a particular panel that is currently in memory. You can obtain this handle from functions such as LoadPanel and NewPanel. |
| controlID | int | The defined constant, located in the .uir header file, that you assigned to the control in the User Interface Editor, or the ID returned by functions such as NewCtrl and DuplicateCtrl. |
| rectangle | Rect | Rect structure specifying the location and size of the rectangle within which to draw the oval. The Rect structure is defined as follows: typedef struct { int top; int left; int height; int width; } Rect; You can create a Rect without having to declare a variable by using the following function: Rect MakeRect (int top, int left, int height, int width); Example CanvasDrawOval (panelHandle, controlID, MakeRect(20,30,150,200), VAL_DRAW_FRAME); |
| drawMode | int | Specifies whether to draw the oval frame, or interior, or both. The following lists the valid values. VAL_DRAW_FRAME VAL_DRAW_INTERIOR VAL_DRAW_FRAME_AND_INTERIOR |

#### Return Value

| Name | Type | Description |
| --- | --- | --- |
| status | int | Return value indicating whether the function was successful. A negative number indicates that an error occurred. |

#### Additional Information

**Library:** [User Interface Library](../../cvi/uiref/cviuser_interface_library_function_tree.htm)

**Include file:** userint.h

**LabWindows/CVI compatibility:** LabWindows/CVI 4.0 and later

#### Example

Refer to userint\canvas.cws for an example of using the CanvasDrawOval function.

<!--NI_TOPIC bundle=labwindows-cvi path=cvi/uiref/cvicanvasdrawpoint.htm language=enus -->
## TOPIC 00909: CanvasDrawPoint

- bundle_id: `labwindows-cvi`
- source_path: `cvi/uiref/cvicanvasdrawpoint.htm`
- source_url: https://docs-be.ni.com/bundle/labwindows-cvi/raw/resource/enus/cvi/uiref/cvicanvasdrawpoint.htm
- document_id: `labwindows-cvi`
- page_type: `leaf`
- content_type: ``

### CanvasDrawPoint

int CanvasDrawPoint (int panelHandle, int controlID, Point point);

#### Purpose

Draws a point on the canvas control at a position you specify.

CanvasDrawPoint draws the point using the current value of the following attributes:

ATTR_PEN_COLOR 

ATTR_PEN_MODE
ATTR_PEN_WIDTH

At pen widths of greater than one, the point might appear to be non-circular.

#### Supported Controls

You can use CanvasDrawPoint with [canvas controls](../../cvi/uiref/cviprogramming_with_canvas_controls.htm).

#### Parameters

| Input |  |  |
| --- | --- | --- |
| Name | Type | Description |
| panelHandle | int | Specifier for a particular panel that is currently in memory. You can obtain this handle from functions such as LoadPanel and NewPanel. |
| controlID | int | The defined constant, located in the .uir header file, that you assigned to the control in the User Interface Editor, or the ID returned by functions such as NewCtrl and DuplicateCtrl. |
| point | Point | Point structure specifying the location at which to draw the point. The Point structure is defined as follows: typedef struct { int x; int y; } Point; You can create a Point without having to declare a variable by using the following function: Point MakePoint (int x, int y); Example CanvasDrawPoint (panelHandle, controlID, MakePoint (20, 30)); |

#### Return Value

| Name | Type | Description |
| --- | --- | --- |
| status | int | Return value indicating whether the function was successful. A negative number indicates that an error occurred. |

#### Additional Information

**Library:** [User Interface Library](../../cvi/uiref/cviuser_interface_library_function_tree.htm)

**Include file:** userint.h

**LabWindows/CVI compatibility:** LabWindows/CVI 4.0 and later

#### Examples

Refer to the following examples that use the CanvasDrawPoint function:

- apps\iconedit\iconedit.cws 
 [IMAGE alt='image' src='open.gif'] Open example
- apps\life\life.cws 
 [IMAGE alt='image' src='open.gif'] Open example
- userint\canvas.cws 
 [IMAGE alt='image' src='open.gif'] Open example

<!--NI_TOPIC bundle=labwindows-cvi path=cvi/uiref/cvicanvasdrawpoly.htm language=enus -->
## TOPIC 00910: CanvasDrawPoly

- bundle_id: `labwindows-cvi`
- source_path: `cvi/uiref/cvicanvasdrawpoly.htm`
- source_url: https://docs-be.ni.com/bundle/labwindows-cvi/raw/resource/enus/cvi/uiref/cvicanvasdrawpoly.htm
- document_id: `labwindows-cvi`
- page_type: `leaf`
- content_type: ``

### CanvasDrawPoly

int CanvasDrawPoly (int panelHandle, int controlID, size_t numberOfPoints, Point points[], int wrap, int drawMode);

#### Purpose

Draws a polygon on the canvas control by connecting the specified points.

CanvasDrawPoly draws the frame of the polygon using the current value of the following
attributes:

ATTR_PEN_COLOR 

ATTR_PEN_MODE 

ATTR_PEN_WIDTH 

ATTR_PEN_STYLE (ignored when pen width is greater than one)

CanvasDrawPoly draws the interior of the polygon using the current value of the following
attributes:

ATTR_PEN_MODE 

ATTR_PEN_PATTERN

#### Supported Controls

You can use CanvasDrawPoly with [canvas controls](../../cvi/uiref/cviprogramming_with_canvas_controls.htm).

#### Parameters

| Input |  |  |
| --- | --- | --- |
| Name | Type | Description |
| panelHandle | int | Specifier for a particular panel that is currently in memory. You can obtain this handle from functions such as LoadPanel and NewPanel. |
| controlID | int | The defined constant, located in the .uir header file, that you assigned to the control in the User Interface Editor, or the ID returned by functions such as NewCtrl and DuplicateCtrl. |
| numberOfPoints | size_t | Number of vertices in the polygon. |
| points | Point [] | Array of Point structures specifying the locations of the vertices of the polygon. The Point structure is defined as follows: typedef struct { int x; int y; } Point; Example /* Declare and initialize an array of Points for the polygon: */ Point polyPoints[5] = { {40,10}, {70, 30}, {50, 50}, {20, 40}, {30, 25} }; CanvasDrawPoly(panelHandle, controlId, 5, polyPoints, 1 /* wrap */, VAL_DRAW_FRAME); |
| wrap | int | Indicates whether to draw a line between last point and first point, thereby closing the polygon frame. Specify a nonzero value or select Yes in the function panel to close the polygon frame. Specify 0 or select No in the function panel if you do not want to close the polygon frame. The function ignores the value when drawing only the interior. |
| drawMode | int | Specifies whether to draw the polygon frame, or interior, or both. The following lists the valid values. VAL_DRAW_FRAME VAL_DRAW_INTERIOR VAL_DRAW_FRAME_AND_INTERIOR |

#### Return Value

| Name | Type | Description |
| --- | --- | --- |
| status | int | Return value indicating whether the function was successful. A negative number indicates that an error occurred. |

#### Additional Information

**Library:** [User Interface Library](../../cvi/uiref/cviuser_interface_library_function_tree.htm)

**Include file:** userint.h

**LabWindows/CVI compatibility:** LabWindows/CVI 4.0 and later

#### Example

Refer to userint\canvas.cws for an example of using the CanvasDrawPoly function.

<!--NI_TOPIC bundle=labwindows-cvi path=cvi/uiref/cvicanvasdrawrect.htm language=enus -->
## TOPIC 00911: CanvasDrawRect

- bundle_id: `labwindows-cvi`
- source_path: `cvi/uiref/cvicanvasdrawrect.htm`
- source_url: https://docs-be.ni.com/bundle/labwindows-cvi/raw/resource/enus/cvi/uiref/cvicanvasdrawrect.htm
- document_id: `labwindows-cvi`
- page_type: `leaf`
- content_type: ``

### CanvasDrawRect

int CanvasDrawRect (int panelHandle, int controlID, Rect rectangle, int drawMode);

#### Purpose

Draws a rectangle on the canvas control at the position and with the dimensions specified by the **rect** parameter.

CanvasDrawRect draws the frame of the rectangle using the current value of the following attributes:

ATTR_PEN_COLOR 

ATTR_PEN_MODE 

ATTR_PEN_WIDTH 

ATTR_PEN_STYLE (ignored when pen width is greater than one)

CanvasDrawRect draws the interior of the rectangle using the current value of the following attributes:

ATTR_PEN_FILL_COLOR 

ATTR_PEN_MODE 

ATTR_PEN_PATTERN

#### Supported Controls

You can use CanvasDrawRect with [canvas controls](../../cvi/uiref/cviprogramming_with_canvas_controls.htm).

#### Parameters

| Input |  |  |
| --- | --- | --- |
| Name | Type | Description |
| panelHandle | int | Specifier for a particular panel that is currently in memory. You can obtain this handle from functions such as LoadPanel and NewPanel. |
| controlID | int | The defined constant, located in the .uir header file, that you assigned to the control in the User Interface Editor, or the ID returned by functions such as NewCtrl and DuplicateCtrl. |
| rectangle | Rect | Rect structure specifying the location and size of the rectangle to be drawn. The Rect structure is defined as follows: typedef struct { int top; int left; int height; int width; } Rect; You can create a Rect without having to declare a variable by using the following function: Rect MakeRect (int top, int left, int height, int width); Example CanvasDrawRect (panelHandle, controlID, MakeRect(20,30,150,200), VAL_DRAW_FRAME); |
| drawMode | int | Specifies whether to draw the rectangle frame, or interior, or both. The following lists the valid values: VAL_DRAW_FRAME VAL_DRAW_INTERIOR VAL_DRAW_FRAME_AND_INTERIOR |

#### Return Value

| Name | Type | Description |
| --- | --- | --- |
| status | int | Return value indicating whether the function was successful. A negative number indicates that an error occurred. |

#### Additional Information

**Library:** [User Interface Library](../../cvi/uiref/cviuser_interface_library_function_tree.htm)

**Include file:** userint.h

**LabWindows/CVI compatibility:** LabWindows/CVI 4.0 and later

#### Examples

Refer to the following examples that use the CanvasDrawRect function:

- apps\iconedit\iconedit.cws 
 [IMAGE alt='image' src='open.gif'] Open example
- apps\life\life.cws 
 [IMAGE alt='image' src='open.gif'] Open example
- userint\canvas.cws 
 [IMAGE alt='image' src='open.gif'] Open example

<!--NI_TOPIC bundle=labwindows-cvi path=cvi/uiref/cvicanvasdrawroundedrect.htm language=enus -->
## TOPIC 00912: CanvasDrawRoundedRect

- bundle_id: `labwindows-cvi`
- source_path: `cvi/uiref/cvicanvasdrawroundedrect.htm`
- source_url: https://docs-be.ni.com/bundle/labwindows-cvi/raw/resource/enus/cvi/uiref/cvicanvasdrawroundedrect.htm
- document_id: `labwindows-cvi`
- page_type: `leaf`
- content_type: ``

### CanvasDrawRoundedRect

int CanvasDrawRoundedRect (int panelHandle, int controlID, Rect rectangle, int ovalHeight, int ovalWidth, int drawMode);

#### Purpose

Draws a rounded rectangle on the canvas control at the position and with the dimensions specified by the **rect** parameter. Each corner of the rectangle is drawn as a quadrant of an oval.

CanvasDrawRoundedRect draws the frame of the rectangle using the current value of the following attributes:

ATTR_PEN_COLOR 

ATTR_PEN_MODE 

ATTR_PEN_WIDTH 

ATTR_PEN_STYLE (ignored when pen width is greater than one)

CanvasDrawRoundedRect draws the interior of the rectangle using the current value of the following attributes:

ATTR_PEN_FILL_COLOR 

ATTR_PEN_MODE 

ATTR_PEN_PATTERN

#### Supported Controls

You can use CanvasDrawRoundedRect with [canvas controls](../../cvi/uiref/cviprogramming_with_canvas_controls.htm).

#### Parameters

| Input |  |  |
| --- | --- | --- |
| Name | Type | Description |
| panelHandle | int | Specifier for a particular panel that is currently in memory. You can obtain this handle from functions such as LoadPanel and NewPanel. |
| controlID | int | The defined constant, located in the .uir header file, that you assigned to the control in the User Interface Editor, or the ID returned by functions such as NewCtrl and DuplicateCtrl. |
| rectangle | Rect | Rect structure specifying the location and size of the rectangle to be drawn. The Rect structure is defined as follows: typedef struct { int top; int left; int height; int width; } Rect; You can create a Rect without having to declare a variable by using the following function: Rect MakeRect (int top, int left, int height, int width); Example CanvasDrawRoundedRect (panelHandle, controlID, MakeRect(20,30,150,200), 5, 5, VAL_DRAW_FRAME); |
| ovalHeight | int | Vertical diameter of the oval whose quadrants are drawn at the corners of the rounded rectangle. |
| ovalWidth | int | Horizontal diameter of the oval whose quadrants are drawn at the corners of the rounded rectangle. |
| drawMode | int | Specifies whether to draw the rectangle frame, or interior, or both. The following lists the valid values: VAL_DRAW_FRAME VAL_DRAW_INTERIOR VAL_DRAW_FRAME_AND_INTERIOR |

#### Return Value

| Name | Type | Description |
| --- | --- | --- |
| status | int | Return value indicating whether the function was successful. A negative number indicates that an error occurred. |

#### Additional Information

**Library:** [User Interface Library](../../cvi/uiref/cviuser_interface_library_function_tree.htm)

**Include file:** userint.h

**LabWindows/CVI compatibility:** LabWindows/CVI 4.0 and later

<!--NI_TOPIC bundle=labwindows-cvi path=cvi/uiref/cvicanvasdrawtext.htm language=enus -->
## TOPIC 00913: CanvasDrawText

- bundle_id: `labwindows-cvi`
- source_path: `cvi/uiref/cvicanvasdrawtext.htm`
- source_url: https://docs-be.ni.com/bundle/labwindows-cvi/raw/resource/enus/cvi/uiref/cvicanvasdrawtext.htm
- document_id: `labwindows-cvi`
- page_type: `leaf`
- content_type: ``

### CanvasDrawText

int CanvasDrawText (int panelHandle, int controlID, char text[], char metaFont[], Rect bounds, int alignment);

#### Purpose

Draws a text string within a specified rectangular area on the canvas control. You can set the alignment of the string within the rectangle. If the string exceeds the size of the rectangle, 
CanvasDrawText clips the string.

CanvasDrawText draws the text using the current value of ATTR_PEN_COLOR.

CanvasDrawText draws the background rectangle using the current value of the following attributes:

ATTR_PEN_FILL_COLOR 

ATTR_PEN_MODE 

ATTR_PEN_PATTERN

If you do not want to draw the background of the rectangle, set the ATTR_PEN_FILL_COLOR attribute of the canvas control to VAL_TRANSPARENT.

#### Supported Controls

You can use CanvasDrawText with [canvas controls](../../cvi/uiref/cviprogramming_with_canvas_controls.htm).

#### Parameters

| Input |  |  |
| --- | --- | --- |
| Name | Type | Description |
| panelHandle | int | Specifier for a particular panel that is currently in memory. You can obtain this handle from functions such as LoadPanel and NewPanel. |
| controlID | int | The defined constant, located in the .uir header file, that you assigned to the control in the User Interface Editor, or the ID returned by functions such as NewCtrl and DuplicateCtrl. |
| text | char [] | Text string to draw within the rectangle. |
| metaFont | char [] | The font to use for the text string. metaFont can be a predefined NI metafont or a user-defined metafont saved by a previous call to functions such as CreateMetaFont and CreateMetaFontEx. The following are NI metafonts: Predefined metafonts—Contain typeface information, point size, and text styles such as bold, underline, italic, and strikeout. These metafonts are used in the LabWindows/CVI environment. The predefined metafonts are VAL_MENU_META_FONT, VAL_DIALOG_META_FONT, VAL_EDITOR_META_FONT, VAL_APP_META_FONT, and VAL_MESSAGE_BOX_META_FONT. LabWindows/CVI-supplied metafonts—Use typefaces that are not native to the operating system. These metafonts are installed while LabWindows/CVI is running. The LabWindows/CVI-supplied metafonts are VAL_7SEG_META_FONT and VAL_SYSTEM_META_FONT. |
| bounds | Rect | Rect structure specifying the location and size of the background rectangle within which to draw the text. Specify values in the bounds parameter in terms of pixel coordinates, with the origin (0,0) at the upper left corner of the canvas control. The Rect structure is defined as follows: typedef struct { int top; int left; int height; int width; } Rect; You can create a Rect without having to declare a variable by using the following function: Rect MakeRect (int top, int left, int height, int width); If you want the size of the background rectangle to adjust automatically to the display size of the text string, set the height and width of the rectangle to VAL_KEEP_SAME_SIZE. Example CanvasDrawText (panelHandle, controlID, "sample text" VAL_APP_META_FONT, MakeRect(20,30,150,200), VAL_CENTER); |
| alignment | int | Determines the placement of the text string within the background rectangle. VAL_LOWER_LEFT Draw the string in the lower left corner of the background rectangle. VAL_CENTER_LEFT Start the string from the midpoint of the left edge of the background rectangle. VAL_UPPER_LEFT Draw the string in the upper left corner of the background rectangle. VAL_LOWER_CENTER Center the string just above the bottom edge of the background rectangle. VAL_CENTER Center the string in the middle of the background rectangle. VAL_UPPER_CENTER Center the string just below the top edge of the background rectangle. VAL_LOWER_RIGHT Draw the string in the lower right corner of the background rectangle. VAL_CENTER_RIGHT Draw the string so that it ends just at the midpoint of the right edge of the background rectangle. VAL_UPPER_RIGHT Draw the string in the upper right corner of the background rectangle. The value specifies the location within the background rectangle at which the string is placed. For example, VAL_UPPER_LEFT means that the string ise drawn in the upper left corner of the background rectangle. If the background rectangle you specify in bounds is smaller than the text display size, the function clips the text to the rectangle and ignores the alignment parameter. If the rectangle width is smaller than the text display width, the text starts from the left. If the rectangle height is smaller than the text display height, the text starts from the top. |
| VAL_LOWER_LEFT | Draw the string in the lower left corner of the background rectangle. |  |
| VAL_CENTER_LEFT | Start the string from the midpoint of the left edge of the background rectangle. |  |
| VAL_UPPER_LEFT | Draw the string in the upper left corner of the background rectangle. |  |
| VAL_LOWER_CENTER | Center the string just above the bottom edge of the background rectangle. |  |
| VAL_CENTER | Center the string in the middle of the background rectangle. |  |
| VAL_UPPER_CENTER | Center the string just below the top edge of the background rectangle. |  |
| VAL_LOWER_RIGHT | Draw the string in the lower right corner of the background rectangle. |  |
| VAL_CENTER_RIGHT | Draw the string so that it ends just at the midpoint of the right edge of the background rectangle. |  |
| VAL_UPPER_RIGHT | Draw the string in the upper right corner of the background rectangle. |  |

#### Return Value

| Name | Type | Description |
| --- | --- | --- |
| status | int | Return value indicating whether the function was successful. A negative number indicates that an error occurred. |

#### Additional Information

**Library:** [User Interface Library](../../cvi/uiref/cviuser_interface_library_function_tree.htm)

**Include file:** userint.h

**LabWindows/CVI compatibility:** LabWindows/CVI 4.0 and later

#### Example

Refer to userint\canvas.cws for an example of using the CanvasDrawText function.

<!--NI_TOPIC bundle=labwindows-cvi path=cvi/uiref/cvicanvasdrawtextatpoint.htm language=enus -->
## TOPIC 00914: CanvasDrawTextAtPoint

- bundle_id: `labwindows-cvi`
- source_path: `cvi/uiref/cvicanvasdrawtextatpoint.htm`
- source_url: https://docs-be.ni.com/bundle/labwindows-cvi/raw/resource/enus/cvi/uiref/cvicanvasdrawtextatpoint.htm
- document_id: `labwindows-cvi`
- page_type: `leaf`
- content_type: ``

### CanvasDrawTextAtPoint

int CanvasDrawTextAtPoint (int panelHandle, int controlID, char text[], char metaFont[], Point anchorPoint, int alignment);

#### Purpose

Draws a text string at the specified location in the canvas control. The location is in terms of an anchor point and an alignment around the point. If the string exceeds the size of the rectangle, CanvasDrawTextAtPoint clips the text.

CanvasDrawTextAtPoint draws the text using the current value of ATTR_PEN_COLOR.

CanvasDrawTextAtPoint draws the background of the text using the current value of the following attributes:

ATTR_PEN_FILL_COLOR 

ATTR_PEN_MODE 

ATTR_PEN_PATTERN

If you do not want to draw the background of the rectangle, set the ATTR_PEN_FILL_COLOR attribute of the canvas control to VAL_TRANSPARENT.

#### Supported Controls

You can use CanvasDrawTextAtPoint with [canvas controls](../../cvi/uiref/cviprogramming_with_canvas_controls.htm).

#### Parameters

| Input |  |  |
| --- | --- | --- |
| Name | Type | Description |
| panelHandle | int | Specifier for a particular panel that is currently in memory. You can obtain this handle from functions such as LoadPanel and NewPanel. |
| controlID | int | The defined constant, located in the .uir header file, that you assigned to the control in the User Interface Editor, or the ID returned by functions such as NewCtrl and DuplicateCtrl. |
| text | char [] | Text string to be drawn at the anchor point. |
| metaFont | char [] | The font to use for the text string. metaFont can be a predefined NI metafont or a user-defined metafont saved by a previous call to functions such as CreateMetaFont and CreateMetaFontEx. The following are NI metafonts: Predefined metafonts—Contain typeface information, point size, and text styles such as bold, underline, italic, and strikeout. These metafonts are used in the LabWindows/CVI environment. The predefined metafonts are VAL_MENU_META_FONT, VAL_DIALOG_META_FONT, VAL_EDITOR_META_FONT, VAL_APP_META_FONT, and VAL_MESSAGE_BOX_META_FONT. LabWindows/CVI-supplied metafonts—Use typefaces that are not native to the operating system. These metafonts are installed while LabWindows/CVI is running. The LabWindows/CVI-supplied metafonts are VAL_7SEG_META_FONT and VAL_SYSTEM_META_FONT. |
| anchorPoint | Point | Point structure specifying location of the point at which to draw the text. The Point structure is defined as follows: typedef struct { int x; int y; } Point; You can create a Point without having to declare a variable by using the following function: Point MakePoint (int x, int y); Example CanvasDrawTextAtPoint (panelHandle, controlID, "sample text", VAL_APP_META_FONT, MakePoint (20, 30), VAL_CENTER); |
| alignment | int | Determines the placement of the text string in relation to the anchor point. Each alignment value refers to a point on the rectangle that implicitly encloses the text string. The text string is placed so that the point you specify with the alignment parameter is at the location you specify with the anchorPoint parameter. The valid values for the alignment parameter are listed in the following table. VAL_LOWER_LEFT Draw the string so that lower left corner of its enclosing rectangle is at the location specified by anchorPoint. VAL_CENTER_LEFT Draw the string so that midpoint of the left edge of its enclosing rectangle is at the location specified by anchorPoint. VAL_UPPER_LEFT Draw the string so that upper left corner of its enclosing rectangle is at the location specified by anchorPoint. VAL_LOWER_CENTER Draw the string so that midpoint of the bottom edge of its enclosing rectangle is at the location specified by anchorPoint. VAL_CENTER Draw the string so that center of its enclosing rectangle is at the location specified by anchorPoint. VAL_UPPER_CENTER Draw the string so that midpoint of the top edge of its enclosing rectangle is at the location specified by anchorPoint. VAL_LOWER_RIGHT Draw the string so that lower right corner of its enclosing rectangle is at the location specified by anchorPoint. VAL_CENTER_RIGHT Draw the string so that midpoint of the right edge of its enclosing rectangle is at the location specified by anchorPoint. VAL_UPPER_RIGHT Draw the string so that upper right corner of its enclosing rectangle is at the location specified by anchorPoint. For example, VAL_UPPER_LEFT means that the text string is placed so that the upper left corner of the text string is at the anchorPoint. |
| VAL_LOWER_LEFT | Draw the string so that lower left corner of its enclosing rectangle is at the location specified by anchorPoint. |  |
| VAL_CENTER_LEFT | Draw the string so that midpoint of the left edge of its enclosing rectangle is at the location specified by anchorPoint. |  |
| VAL_UPPER_LEFT | Draw the string so that upper left corner of its enclosing rectangle is at the location specified by anchorPoint. |  |
| VAL_LOWER_CENTER | Draw the string so that midpoint of the bottom edge of its enclosing rectangle is at the location specified by anchorPoint. |  |
| VAL_CENTER | Draw the string so that center of its enclosing rectangle is at the location specified by anchorPoint. |  |
| VAL_UPPER_CENTER | Draw the string so that midpoint of the top edge of its enclosing rectangle is at the location specified by anchorPoint. |  |
| VAL_LOWER_RIGHT | Draw the string so that lower right corner of its enclosing rectangle is at the location specified by anchorPoint. |  |
| VAL_CENTER_RIGHT | Draw the string so that midpoint of the right edge of its enclosing rectangle is at the location specified by anchorPoint. |  |
| VAL_UPPER_RIGHT | Draw the string so that upper right corner of its enclosing rectangle is at the location specified by anchorPoint. |  |

#### Return Value

| Name | Type | Description |
| --- | --- | --- |
| status | int | Return value indicating whether the function was successful. A negative number indicates that an error occurred. |

#### Additional Information

**Library:** [User Interface Library](../../cvi/uiref/cviuser_interface_library_function_tree.htm)

**Include file:** userint.h

**LabWindows/CVI compatibility:** LabWindows/CVI 4.0 and later

#### Example

Refer to userint\RotatedText.cws for an example of using the CanvasDrawTextAtPoint function.

<!--NI_TOPIC bundle=labwindows-cvi path=cvi/uiref/cvicanvasendbatchdraw.htm language=enus -->
## TOPIC 00915: CanvasEndBatchDraw

- bundle_id: `labwindows-cvi`
- source_path: `cvi/uiref/cvicanvasendbatchdraw.htm`
- source_url: https://docs-be.ni.com/bundle/labwindows-cvi/raw/resource/enus/cvi/uiref/cvicanvasendbatchdraw.htm
- document_id: `labwindows-cvi`
- page_type: `leaf`
- content_type: ``

### CanvasEndBatchDraw

int CanvasEndBatchDraw (int panelHandle, int controlID);

#### Purpose

Ends the batch drawing you started with [CanvasStartBatchDraw](../../cvi/uiref/cvicanvasstartbatchdraw.htm).

Refer to the CanvasStartBatchDraw function reference for an example of how to use this function.

#### Supported Controls

You can use CanvasEndBatchDraw with [canvas controls](../../cvi/uiref/cviprogramming_with_canvas_controls.htm).

#### Parameters

| Input |  |  |
| --- | --- | --- |
| Name | Type | Description |
| panelHandle | int | Specifier for a particular panel that is currently in memory. You can obtain this handle from functions such as LoadPanel and NewPanel. |
| controlID | int | The defined constant, located in the .uir header file, that you assigned to the control in the User Interface Editor, or the ID returned by functions such as NewCtrl and DuplicateCtrl. |

#### Return Value

| Name | Type | Description |
| --- | --- | --- |
| nestingDepth | int | Number of calls to CanvasStartBatchDraw that have not been matched by calls to CanvasEndBatchDraw (including this call). A negative value indicates that an error occurred. |

#### Additional Information

**Library:** [User Interface Library](../../cvi/uiref/cviuser_interface_library_function_tree.htm)

**Include file:** userint.h

**LabWindows/CVI compatibility:** LabWindows/CVI 4.0 and later

#### Examples

Refer to the following examples that use the CanvasEndBatchDraw function:

- apps\iconedit\iconedit.cws 
 [IMAGE alt='image' src='open.gif'] Open example
- apps\life\life.cws 
 [IMAGE alt='image' src='open.gif'] Open example
- userint\canvas.cws 
 [IMAGE alt='image' src='open.gif'] Open example
- userint\canvsbmk.cws 
 [IMAGE alt='image' src='open.gif'] Open example

<!--NI_TOPIC bundle=labwindows-cvi path=cvi/uiref/cvicanvasgetcliprect.htm language=enus -->
## TOPIC 00916: CanvasGetClipRect

- bundle_id: `labwindows-cvi`
- source_path: `cvi/uiref/cvicanvasgetcliprect.htm`
- source_url: https://docs-be.ni.com/bundle/labwindows-cvi/raw/resource/enus/cvi/uiref/cvicanvasgetcliprect.htm
- document_id: `labwindows-cvi`
- page_type: `leaf`
- content_type: ``

### CanvasGetClipRect

int CanvasGetClipRect (int panelHandle, int controlID, Rect *clipRect);

#### Purpose

Obtains the current clipping rectangle for the canvas control. Canvas drawing operations do not extend beyond the clipping rectangle. Any drawing outside the clipping rectangle is not shown. The exception is [CanvasClear](../../cvi/uiref/cvicanvasclear.htm), which is not limited to the clipping rectangle.

#### Supported Controls

You can use CanvasGetClipRect with [canvas controls](../../cvi/uiref/cviprogramming_with_canvas_controls.htm).

#### Parameters

| Input |  |  |
| --- | --- | --- |
| Name | Type | Description |
| panelHandle | int | Specifier for a particular panel that is currently in memory. You can obtain this handle from functions such as LoadPanel and NewPanel. |
| controlID | int | The defined constant, located in the .uir header file, that you assigned to the control in the User Interface Editor, or the ID returned by functions such as NewCtrl and DuplicateCtrl. |
| Output |  |  |
| Name | Type | Description |
| clipRect | Rect | Rect structure that contains the location and size of the current clipping area. If clipping is disabled (the default state), the function sets the height and width values in the structure to zero. The Rect structure is defined as follows: typedef struct { int top; int left; int height; int width; } Rect; |

#### Return Value

| Name | Type | Description |
| --- | --- | --- |
| status | int | Return value indicating whether the function was successful. A negative number indicates that an error occurred. |

#### Additional Information

**Library:** [User Interface Library](../../cvi/uiref/cviuser_interface_library_function_tree.htm)

**Include file:** userint.h

**LabWindows/CVI compatibility:** LabWindows/CVI 4.0 and later

<!--NI_TOPIC bundle=labwindows-cvi path=cvi/uiref/cvicanvasgetpenposition.htm language=enus -->
## TOPIC 00917: CanvasGetPenPosition

- bundle_id: `labwindows-cvi`
- source_path: `cvi/uiref/cvicanvasgetpenposition.htm`
- source_url: https://docs-be.ni.com/bundle/labwindows-cvi/raw/resource/enus/cvi/uiref/cvicanvasgetpenposition.htm
- document_id: `labwindows-cvi`
- page_type: `leaf`
- content_type: ``

### CanvasGetPenPosition

int CanvasGetPenPosition (int panelHandle, int controlID, Point *point);

#### Purpose

Obtains the current position of the canvas pen.

[CanvasDrawLineTo](../../cvi/uiref/cvicanvasdrawlineto.htm) is the only canvas drawing function that uses the pen position.

#### Supported Controls

You can use CanvasGetPenPosition with [canvas controls](../../cvi/uiref/cviprogramming_with_canvas_controls.htm).

#### Parameters

| Input |  |  |
| --- | --- | --- |
| Name | Type | Description |
| panelHandle | int | Specifier for a particular panel that is currently in memory. You can obtain this handle from functions such as LoadPanel and NewPanel. |
| controlID | int | The defined constant, located in the .uir header file, that you assigned to the control in the User Interface Editor, or the ID returned by functions such as NewCtrl and DuplicateCtrl. |
| Output |  |  |
| Name | Type | Description |
| point | Point | Point structure indicating the current position of the pen. The Point structure is defined as follows: typedef struct { int x; int y; } Point; |

#### Return Value

| Name | Type | Description |
| --- | --- | --- |
| status | int | Return value indicating whether the function was successful. A negative number indicates that an error occurred. |

#### Additional Information

**Library:** [User Interface Library](../../cvi/uiref/cviuser_interface_library_function_tree.htm)

**Include file:** userint.h

**LabWindows/CVI compatibility:** LabWindows/CVI 4.0 and later

<!--NI_TOPIC bundle=labwindows-cvi path=cvi/uiref/cvicanvasgetpixel.htm language=enus -->
## TOPIC 00918: CanvasGetPixel

- bundle_id: `labwindows-cvi`
- source_path: `cvi/uiref/cvicanvasgetpixel.htm`
- source_url: https://docs-be.ni.com/bundle/labwindows-cvi/raw/resource/enus/cvi/uiref/cvicanvasgetpixel.htm
- document_id: `labwindows-cvi`
- page_type: `leaf`
- content_type: ``

### CanvasGetPixel

int CanvasGetPixel (int panelHandle, int controlID, Point point, int *pixelColor);

#### Purpose

Obtains the color of a single pixel on a canvas control.

|  | Note The canvas control maintains an internal bitmap reflecting all of the drawing operations (except for drawing operations made while the ATTR_DRAW_POLICY attribute is VAL_DIRECT_TO_SCREEN). Sometimes the internal bitmap contains the result of recent drawing operations that have not yet been reflected on the screen. CanvasGetPixel obtains the pixel colors from the internal bitmap, not from the screen. |
| --- | --- |

#### Supported Controls

You can use CanvasGetPixel with [canvas controls](../../cvi/uiref/cviprogramming_with_canvas_controls.htm).

#### Parameters

| Input |  |  |
| --- | --- | --- |
| Name | Type | Description |
| panelHandle | int | Specifier for a particular panel that is currently in memory. You can obtain this handle from functions such as LoadPanel and NewPanel. |
| controlID | int | The defined constant, located in the .uir header file, that you assigned to the control in the User Interface Editor, or the ID returned by functions such as NewCtrl and DuplicateCtrl. |
| point | Point | Point structure that indicates the location of a pixel. The location is in terms of unscaled pixel coordinates. The origin (0,0) is the upper left corner of the canvas control. The Point structure is defined as follows. typedef struct { int x; int y; } Point; You can create a Point without having to declare a variable by using the following function: Point MakePoint (int x, int y); Example CanvasGetPixel (panelHandle, controlID, MakePoint (20, 30), &pixelColor); |
| Output |  |  |
| Name | Type | Description |
| pixelColor | int | RGB color value of the pixel at the specified point. |

#### Return Value

| Name | Type | Description |
| --- | --- | --- |
| status | int | Return value indicating whether the function was successful. A negative number indicates that an error occurred. |

#### Additional Information

**Library:** [User Interface Library](../../cvi/uiref/cviuser_interface_library_function_tree.htm)

**Include file:** userint.h

**LabWindows/CVI compatibility:** LabWindows/CVI 4.0 and later

<!--NI_TOPIC bundle=labwindows-cvi path=cvi/uiref/cvicanvasgetpixels.htm language=enus -->
## TOPIC 00919: CanvasGetPixels

- bundle_id: `labwindows-cvi`
- source_path: `cvi/uiref/cvicanvasgetpixels.htm`
- source_url: https://docs-be.ni.com/bundle/labwindows-cvi/raw/resource/enus/cvi/uiref/cvicanvasgetpixels.htm
- document_id: `labwindows-cvi`
- page_type: `leaf`
- content_type: ``

### CanvasGetPixels

int CanvasGetPixels (int panelHandle, int controlID, Rect rect, int pixelColors[]);

#### Purpose

Obtains the colors of the pixels in a specific rectangular area of a canvas control.

|  | Note The canvas control maintains an internal bitmap reflecting all of the drawing operations (except for drawing operations made while the ATTR_DRAW_POLICY attribute is VAL_DIRECT_TO_SCREEN). Sometimes the internal bitmap contains the result of recent drawing operations that have not yet been reflected on the screen. CanvasGetPixels obtains the pixel colors from the internal bitmap, not from the screen. |
| --- | --- |

#### Supported Controls

You can use CanvasGetPixels with [canvas controls](../../cvi/uiref/cviprogramming_with_canvas_controls.htm).

#### Parameters

| Input |  |  |
| --- | --- | --- |
| Name | Type | Description |
| panelHandle | int | Specifier for a particular panel that is currently in memory. You can obtain this handle from functions such as LoadPanel and NewPanel. |
| controlID | int | The defined constant, located in the .uir header file, that you assigned to the control in the User Interface Editor, or the ID returned by functions such as NewCtrl and DuplicateCtrl. |
| rect | Rect | Rect structure that specifies the location and size of the rectangular area from which to obtain the pixel colors. Location and size are expressed in terms of unscaled pixel coordinates. The origin (0,0) is the upper left corner of the canvas control. Use VAL_ENTIRE_OBJECT to specify the entire canvas. The Rect structure is defined as follows: typedef struct { int top; int left; int height; int width; } Rect; You can create a Rect without having to declare a variable by using the following function: Rect MakeRect (int top, int left, int height, int width); Example CanvasGetPixels (panelHandle, controlID, VAL_ENTIRE_OBJECT, pixelArray); |
| Output |  |  |
| Name | Type | Description |
| pixelColors | int [] | Array of RGB color values of the pixels in the specified rectangle. The total number of elements in the pixelColors array must be equal to rect.height * rect.width. The pixel color values are stored in row-major order. For example, consider a rect with the following values: rect.top = 50 rect.left = 60 rect.height = 20 rect.width = 15 The color of pixel {x = 65, y = 58} of this rect is stored in a pixel array at the following index: pixelArray[(y — rect.top) × rect.width + (x — rect.left)] pixelArray[(58 — 50) × 15 + (65 — 60)] When using a rect.width of VAL_TO_EDGE, substitute the following for rect.width in the preceding formula: (total width of canvas) — rect.left |

#### Return Value

| Name | Type | Description |
| --- | --- | --- |
| status | int | Return value indicating whether the function was successful. A negative number indicates that an error occurred. |

#### Additional Information

**Library:** [User Interface Library](../../cvi/uiref/cviuser_interface_library_function_tree.htm)

**Include file:** userint.h

**LabWindows/CVI compatibility:** LabWindows/CVI 4.0 and later

#### Example

Refer to apps\iconedit\iconedit.cws for an example of using the CanvasGetPixels function.

<!--NI_TOPIC bundle=labwindows-cvi path=cvi/uiref/cvicanvasinvertrect.htm language=enus -->
## TOPIC 00920: CanvasInvertRect

- bundle_id: `labwindows-cvi`
- source_path: `cvi/uiref/cvicanvasinvertrect.htm`
- source_url: https://docs-be.ni.com/bundle/labwindows-cvi/raw/resource/enus/cvi/uiref/cvicanvasinvertrect.htm
- document_id: `labwindows-cvi`
- page_type: `leaf`
- content_type: ``

### CanvasInvertRect

int CanvasInvertRect (int panelHandle, int controlID, Rect rectangle);

#### Purpose

Inverts the colors in the specified rectangular area of a canvas control.

The resulting colors depend on the operating system. If you invert the same rectangle twice, you are guaranteed to get the original colors back.

#### Supported Controls

You can use CanvasInvertRect with [canvas controls](../../cvi/uiref/cviprogramming_with_canvas_controls.htm).

#### Parameters

| Input |  |  |
| --- | --- | --- |
| Name | Type | Description |
| panelHandle | int | Specifier for a particular panel that is currently in memory. You can obtain this handle from functions such as LoadPanel and NewPanel. |
| controlID | int | The defined constant, located in the .uir header file, that you assigned to the control in the User Interface Editor, or the ID returned by functions such as NewCtrl and DuplicateCtrl. |
| rectangle | Rect | Rect structure that specifies the location and size of the rectangular area in which to invert the colors. Use VAL_ENTIRE_OBJECT to specify the entire canvas. The Rect structure is defined as follows: typedef struct { int top; int left; int height; int width; } Rect; You can create a Rect without having to declare a variable by using the following function: Rect MakeRect (int top, int left, int height, int width); Example CanvasInvertRect (panelHandle, controlID, MakeRect(20,30,150,200)); |

#### Return Value

| Name | Type | Description |
| --- | --- | --- |
| status | int | Return value indicating whether the function was successful. A negative number indicates that an error occurred. |

#### Additional Information

**Library:** [User Interface Library](../../cvi/uiref/cviuser_interface_library_function_tree.htm)

**Include file:** userint.h

**LabWindows/CVI compatibility:** LabWindows/CVI 4.0 and later

<!--NI_TOPIC bundle=labwindows-cvi path=cvi/uiref/cvicanvasscroll.htm language=enus -->
## TOPIC 00921: CanvasScroll

- bundle_id: `labwindows-cvi`
- source_path: `cvi/uiref/cvicanvasscroll.htm`
- source_url: https://docs-be.ni.com/bundle/labwindows-cvi/raw/resource/enus/cvi/uiref/cvicanvasscroll.htm
- document_id: `labwindows-cvi`
- page_type: `leaf`
- content_type: ``

### CanvasScroll

int CanvasScroll (int panelHandle, int controlID, Rect rectangle, int scrollAmountInXDirection, int scrollAmountInYDirection);

#### Purpose

Scrolls the contents of a specific rectangular area of a canvas 
control. The area that is exposed by the scrolling is filled using 
the current value of the ATTR_PEN_FILL_COLOR attribute. The contents 
of the canvas outside the rectangular area are not affected.

#### Supported Controls

You can use CanvasScroll with [canvas controls](../../cvi/uiref/cviprogramming_with_canvas_controls.htm).

#### Parameters

| Input |  |  |
| --- | --- | --- |
| Name | Type | Description |
| panelHandle | int | Specifier for a particular panel that is currently in memory. You can obtain this handle from functions such as LoadPanel and NewPanel. |
| controlID | int | The defined constant, located in the .uir header file, that you assigned to the control in the User Interface Editor, or the ID returned by functions such as NewCtrl and DuplicateCtrl. |
| rectangle | Rect | Rect structure that specifies the location and size of the rectangular area to scroll. Use VAL_ENTIRE_OBJECT to specify the entire canvas. The area of the canvas outside the specified rectangle is not affected by the scrolling. The Rect structure is defined as follows: typedef struct { int top; int left; int height; int width; } Rect; You can create a Rect without having to declare a variable by using the following function: Rect MakeRect (int top, int left, int height, int width); Example CanvasScroll (panelHandle, controlID, VAL_ENTIRE_OBJECT, xScrollAmount, yScrollAmount, 1); |
| scrollAmountInXDirection | int | Amount to scroll horizontally. A positive value for scrollAmountInXDirection moves the contents of the rectangle to the right. An area on the left side of the rectangle is exposed. The area is filled with the current value of the ATTR_PEN_FILL_COLOR attribute. A negative value for scrollAmountInXDirection moves the contents of the rectangle to the left. An area on the right side of the rectangle is exposed. The area is filled with the current value of the ATTR_PEN_FILL_COLOR attribute. |
| scrollAmountInYDirection | int | Amount to scroll vertically. A positive value for scrollAmountInYDirection moves the contents of the rectangle down. An area at the top of the rectangle is exposed. The area is filled with the current value of the ATTR_PEN_FILL_COLOR attribute. A negative value for scrollAmountInYDirection moves the contents of the rectangle the up. An area at the bottom of the rectangle is exposed. The area is filled with the current value of the ATTR_PEN_FILL_COLOR attribute. |

#### Return Value

| Name | Type | Description |
| --- | --- | --- |
| status | int | Return value indicating whether the function was successful. A negative number indicates that an error occurred. |

#### Additional Information

**Library:** [User Interface Library](../../cvi/uiref/cviuser_interface_library_function_tree.htm)

**Include file:** userint.h

**LabWindows/CVI compatibility:** LabWindows/CVI 4.0 and later

<!--NI_TOPIC bundle=labwindows-cvi path=cvi/uiref/cvicanvassetcliprect.htm language=enus -->
## TOPIC 00922: CanvasSetClipRect

- bundle_id: `labwindows-cvi`
- source_path: `cvi/uiref/cvicanvassetcliprect.htm`
- source_url: https://docs-be.ni.com/bundle/labwindows-cvi/raw/resource/enus/cvi/uiref/cvicanvassetcliprect.htm
- document_id: `labwindows-cvi`
- page_type: `leaf`
- content_type: ``

### CanvasSetClipRect

int CanvasSetClipRect (int panelHandle, int controlID, Rect clipRect);

#### Purpose

Sets the clipping rectangle for the canvas control. Canvas drawing operations do not extend beyond the clipping rectangle. Any drawing outside the clipping rectangle is not shown. The exception is [CanvasClear](../../cvi/uiref/cvicanvasclear.htm), which is not limited to the clipping rectangle.

Changing the clipping rectangle does not affect the current contents of the canvas.

In the initial state for a canvas control, clipping is disabled.

#### Supported Controls

You can use CanvasSetClipRect with [canvas controls](../../cvi/uiref/cviprogramming_with_canvas_controls.htm).

#### Parameters

| Input |  |  |
| --- | --- | --- |
| Name | Type | Description |
| panelHandle | int | Specifier for a particular panel that is currently in memory. You can obtain this handle from functions such as LoadPanel and NewPanel. |
| controlID | int | The defined constant, located in the .uir header file, that you assigned to the control in the User Interface Editor, or the ID returned by functions such as NewCtrl and DuplicateCtrl. |
| clipRect | Rect | Rect structure specifying into the location and size of the clipping rectangle. To disable clipping, set the height or width of clipRect to zero, or to a negative number. The macro VAL_EMPTY_RECT is convenient for this. The Rect structure is defined as follows: typedef struct { int top; int left; int height; int width; } Rect; You can create a Rect without having to declare a variable by using the following function: Rect MakeRect (int top, int left, int height, int width); Example Code CanvasSetClipRect (panelHandle, controlID, MakeRect(20,30,50,50)); |

#### Return Value

| Name | Type | Description |
| --- | --- | --- |
| status | int | Return value indicating whether the function was successful. A negative number indicates that an error occurred. |

#### Additional Information

**Library:** [User Interface Library](../../cvi/uiref/cviuser_interface_library_function_tree.htm)

**Include file:** userint.h

**LabWindows/CVI compatibility:** LabWindows/CVI 4.0 and later

<!--NI_TOPIC bundle=labwindows-cvi path=cvi/uiref/cvicanvassetpenposition.htm language=enus -->
## TOPIC 00923: CanvasSetPenPosition

- bundle_id: `labwindows-cvi`
- source_path: `cvi/uiref/cvicanvassetpenposition.htm`
- source_url: https://docs-be.ni.com/bundle/labwindows-cvi/raw/resource/enus/cvi/uiref/cvicanvassetpenposition.htm
- document_id: `labwindows-cvi`
- page_type: `leaf`
- content_type: ``

### CanvasSetPenPosition

int CanvasSetPenPosition (int panelHandle, int controlID, Point point);

#### Purpose

Sets the position of the canvas pen.

[CanvasDrawLineTo](../../cvi/uiref/cvicanvasdrawlineto.htm) is the only canvas drawing function that uses the pen position.

#### Supported Controls

You can use CanvasSetPenPosition with [canvas controls](../../cvi/uiref/cviprogramming_with_canvas_controls.htm).

#### Parameters

| Input |  |  |
| --- | --- | --- |
| Name | Type | Description |
| panelHandle | int | Specifier for a particular panel that is currently in memory. You can obtain this handle from functions such as LoadPanel and NewPanel. |
| controlID | int | The defined constant, located in the .uir header file, that you assigned to the control in the User Interface Editor, or the ID returned by functions such as NewCtrl and DuplicateCtrl. |
| point | Point | Point structure that specifies the new position of the canvas pen. The Point structure is defined as follows. typedef struct { int x; int y; } Point; You can create a Point without having to declare a variable by using the following function: Point MakePoint (int x, int y); Example CanvasSetPenPosition (panelHandle, controlID, MakePoint (20, 30)); |

#### Return Value

| Name | Type | Description |
| --- | --- | --- |
| status | int | Return value indicating whether the function was successful. A negative number indicates that an error occurred. |

#### Additional Information

**Library:** [User Interface Library](../../cvi/uiref/cviuser_interface_library_function_tree.htm)

**Include file:** userint.h

**LabWindows/CVI compatibility:** LabWindows/CVI 4.0 and later

#### Example

Refer to userint\canvas.cws for an example of using the CanvasSetPenPosition function.

<!--NI_TOPIC bundle=labwindows-cvi path=cvi/uiref/cvicanvasstartbatchdraw.htm language=enus -->
## TOPIC 00924: CanvasStartBatchDraw

- bundle_id: `labwindows-cvi`
- source_path: `cvi/uiref/cvicanvasstartbatchdraw.htm`
- source_url: https://docs-be.ni.com/bundle/labwindows-cvi/raw/resource/enus/cvi/uiref/cvicanvasstartbatchdraw.htm
- document_id: `labwindows-cvi`
- page_type: `leaf`
- content_type: ``

### CanvasStartBatchDraw

int CanvasStartBatchDraw (int panelHandle, int controlID);

#### Purpose

Allows you to increase the drawing performance of the canvas control. In general, use CanvasStartBatchDraw whenever you want to make two or more consecutive calls to canvas drawing functions. Match each call to CanvasStartBatchDraw with a call to [CanvasEndBatchDraw](../../cvi/uiref/cvicanvasendbatchdraw.htm).

You can nest calls to CanvasStartBatchDraw.

Before LabWindows/CVI performs drawing operations, it invokes certain operating system functions to prepare for drawing on the particular canvas. Without batch drawing, LabWindows/CVI must call these system functions for each canvas drawing operation. With batch drawing, LabWindows/CVI calls the system functions only once for all of the drawing operations between CanvasStartBatchDraw and the matching CanvasEndBatchDraw.

During a batch draw, you can call drawing operations on other canvas controls or call other User Interface Library functions that perform drawing operations or process events. This has the effect of implicitly ending the batch. The next time you call a drawing function on the same canvas, the batch is implicitly restarted.

Failure to properly match CanvasStartBatchDraw and CanvasEndBatchDraw calls can negate the potential performance improvements but does not cause any other negative effects.

Do not access a canvas control from other threads while batch drawing is in effect for the control.

|  | Note If the ATTR_DRAW_POLICY attribute for the canvas control is VAL_UPDATE_IMMEDIATELY, no update to the screen occurs until you end the batch. Also, changing values of the ATTR_DRAW_POLICY and ATTR_OVERLAP_POLICY attributes during a batch draw has no effect until after you end the batch. |
| --- | --- |

##### Example Code

The following code demonstrates how to incorporate a sequence of drawing operations on the same canvas control into one batch:

CanvasStartBatchDraw (panelHandle, controlID);

CanvasDrawLine (panelHandle, controlID, point1, point2);

CanvasDrawLine (panelHandle, controlID, point3, point4);

CanvasDrawRect (panelHandle, controlID, rect5);

CanvasEndBatchDraw (panelHandle, controlID);

#### Supported Controls

You can use CanvasStartBatchDraw with [canvas controls](../../cvi/uiref/cviprogramming_with_canvas_controls.htm).

#### Parameters

| Input |  |  |
| --- | --- | --- |
| Name | Type | Description |
| panelHandle | int | Specifier for a particular panel that is currently in memory. You can obtain this handle from functions such as LoadPanel and NewPanel. |
| controlID | int | The defined constant, located in the .uir header file, that you assigned to the control in the User Interface Editor, or the ID returned by functions such as NewCtrl and DuplicateCtrl. |

#### Return Value

| Name | Type | Description |
| --- | --- | --- |
| nestingDepth | int | Number of calls to CanvasStartBatchDraw (including this call) that have not been matched by calls to CanvasEndBatchDraw. A negative value indicates that an error occurred. |

#### Additional Information

**Library:** [User Interface Library](../../cvi/uiref/cviuser_interface_library_function_tree.htm)

**Include file:** userint.h

**LabWindows/CVI compatibility:** LabWindows/CVI 4.0 and later

#### Examples

Refer to the following examples that use the CanvasStartBatchDraw function:

- apps\iconedit\iconedit.cws 
 [IMAGE alt='image' src='open.gif'] Open example
- apps\life\life.cws 
 [IMAGE alt='image' src='open.gif'] Open example
- userint\canvas.cws 
 [IMAGE alt='image' src='open.gif'] Open example
- userint\canvsbmk.cws 
 [IMAGE alt='image' src='open.gif'] Open example

<!--NI_TOPIC bundle=labwindows-cvi path=cvi/uiref/cvicanvasupdate.htm language=enus -->
## TOPIC 00925: CanvasUpdate

- bundle_id: `labwindows-cvi`
- source_path: `cvi/uiref/cvicanvasupdate.htm`
- source_url: https://docs-be.ni.com/bundle/labwindows-cvi/raw/resource/enus/cvi/uiref/cvicanvasupdate.htm
- document_id: `labwindows-cvi`
- page_type: `leaf`
- content_type: ``

### CanvasUpdate

int CanvasUpdate (int panelHandle, int controlID, Rect updateArea);

#### Purpose

Immediately updates on the screen the contents of the canvas control 
within a specific rectangular area.

The canvas control maintains an internal bitmap reflecting all of the 
drawing operations, except for drawing operations made while the 
ATTR_DRAW_POLICY attribute is VAL_DIRECT_TO_SCREEN. Maintaining the 
internal bitmap ensures that the canvas is redrawn correctly when it 
is exposed.

CanvasUpdate copies the content of the rectangular area in the 
internal bitmap to the canvas control.

#### Supported Controls

You can use CanvasUpdate with [canvas controls](../../cvi/uiref/cviprogramming_with_canvas_controls.htm).

#### Parameters

| Input |  |  |
| --- | --- | --- |
| Name | Type | Description |
| panelHandle | int | Specifier for a particular panel that is currently in memory. You can obtain this handle from functions such as LoadPanel and NewPanel. |
| controlID | int | The defined constant, located in the .uir header file, that you assigned to the control in the User Interface Editor, or the ID returned by functions such as NewCtrl and DuplicateCtrl. |
| updateArea | Rect | Rect structure specifying the location and size of the rectangular to update from the internal bitmap. Use VAL_ENTIRE_OBJECT to specify the entire canvas control. The Rect structure is defined as follows: typedef struct { int top; int left; int height; int width; } Rect; You can create a Rect without having to declare a variable by using the following function: Rect MakeRect (int top, int left, int height, int width); Example CanvasUpdate (panelHandle, controlID, VAL_ENTIRE_OBJECT); |

#### Return Value

| Name | Type | Description |
| --- | --- | --- |
| status | int | Return value indicating whether the function was successful. A negative number indicates that an error occurred. |

#### Additional Information

**Library:** [User Interface Library](../../cvi/uiref/cviuser_interface_library_function_tree.htm)

**Include file:** userint.h

**LabWindows/CVI compatibility:** LabWindows/CVI 4.0 and later

<!--NI_TOPIC bundle=labwindows-cvi path=cvi/uiref/cvichecklistitem.htm language=enus -->
## TOPIC 00926: CheckListItem

- bundle_id: `labwindows-cvi`
- source_path: `cvi/uiref/cvichecklistitem.htm`
- source_url: https://docs-be.ni.com/bundle/labwindows-cvi/raw/resource/enus/cvi/uiref/cvichecklistitem.htm
- document_id: `labwindows-cvi`
- page_type: `leaf`
- content_type: ``

### CheckListItem

int CheckListItem (int panelHandle, int controlID, int itemIndex, int checked);

#### Purpose

Places a check by, or removes a check from, a specific list item.

This function applies only to list boxes with the check mode attribute enabled.

#### Supported Controls

You can use CheckListItem with the following controls:

- List boxes
- Trees

#### Parameters

| Input |  |  |
| --- | --- | --- |
| Name | Type | Description |
| panelHandle | int | Specifier for a particular panel that is currently in memory. You can obtain this handle from functions such as LoadPanel and NewPanel. |
| controlID | int | The defined constant, located in the .uir header file, that you assigned to the control in the User Interface Editor, or the ID returned by functions such as NewCtrl and DuplicateCtrl. |
| itemIndex | int | Zero-based index into the list. |
| checked | int | Specify a nonzero value or select Yes in the function panel to place a check by the list item. Specify 0 or select No in the function panel to omit a check by the list item. |

#### Return Value

| Name | Type | Description |
| --- | --- | --- |
| status | int | Return value indicating whether the function was successful. A negative number indicates that an error occurred. |

#### Additional Information

**Library:** [User Interface Library](../../cvi/uiref/cviuser_interface_library_function_tree.htm)

**Include file:** userint.h

**LabWindows/CVI compatibility:** LabWindows/CVI 3.0 and later

<!--NI_TOPIC bundle=labwindows-cvi path=cvi/uiref/cvichild_panels.htm language=enus -->
## TOPIC 00927: Child Panels

- bundle_id: `labwindows-cvi`
- source_path: `cvi/uiref/cvichild_panels.htm`
- source_url: https://docs-be.ni.com/bundle/labwindows-cvi/raw/resource/enus/cvi/uiref/cvichild_panels.htm
- document_id: `labwindows-cvi`
- page_type: `leaf`
- content_type: ``

### Child Panels

You can configure [LoadPanel](cviloadpanel.htm) so that [panels](cvioperating_panels.htm) appear within other panels in your user interface. When you do this, the
principal panel is called the parent panel; panels within it are child panels. Child
panels can appear within other child panels too.

A child panel helps developers control the appearance of the user interface.
Users cannot drag a child panel outside its parent panel. And if users shrink a
parent panel, a child panel might be partially or completely hidden in the
shrunken panel view.

<!--NI_TOPIC bundle=labwindows-cvi path=cvi/uiref/cviclearaxisitems.htm language=enus -->
## TOPIC 00928: ClearAxisItems

- bundle_id: `labwindows-cvi`
- source_path: `cvi/uiref/cviclearaxisitems.htm`
- source_url: https://docs-be.ni.com/bundle/labwindows-cvi/raw/resource/enus/cvi/uiref/cviclearaxisitems.htm
- document_id: `labwindows-cvi`
- page_type: `leaf`
- content_type: ``

### ClearAxisItems

int ClearAxisItems (int panelHandle, int controlID, int axis);

#### Purpose

Clears all string/value pairs from the list of label strings for a graph or
strip chart axis.

#### Supported Controls

You can use ClearAxisItems with the following controls:

- Graphs
- Strip charts
- Digital graphs

#### Parameters

| Input |  |  |
| --- | --- | --- |
| Name | Type | Description |
| panelHandle | int | Specifier for a particular panel that is currently in memory. You can obtain this handle from functions such as LoadPanel and NewPanel. |
| controlID | int | The defined constant, located in the .uir header file, that you assigned to the control in the User Interface Editor, or the ID returned by functions such as NewCtrl and DuplicateCtrl. |
| axis | int | Specifies for which axis to obtain the mode and range. The following lists the valid values: VAL_BOTTOM_XAXIS (graphs only) VAL_TOP_XAXIS (graphs only) VAL_LEFT_YAXIS (graphs and strip charts) VAL_RIGHT_YAXIS (graphs only) |

#### Return Value

| Name | Type | Description |
| --- | --- | --- |
| status | int | Return value indicating whether the function was successful. A negative number indicates that an error occurred. |

#### Additional Information

**Library:** [User Interface Library](../../cvi/uiref/cviuser_interface_library_function_tree.htm)

**Include file:** userint.h

**LabWindows/CVI compatibility:** LabWindows/CVI 4.0 and later

#### Example

Refer to userint\timeaxis.cws for an example of using the ClearAxisItems function.

<!--NI_TOPIC bundle=labwindows-cvi path=cvi/uiref/cviclearctrlarray.htm language=enus -->
## TOPIC 00929: ClearCtrlArray

- bundle_id: `labwindows-cvi`
- source_path: `cvi/uiref/cviclearctrlarray.htm`
- source_url: https://docs-be.ni.com/bundle/labwindows-cvi/raw/resource/enus/cvi/uiref/cviclearctrlarray.htm
- document_id: `labwindows-cvi`
- page_type: `leaf`
- content_type: ``

### ClearCtrlArray

int ClearCtrlArray (int controlArrayHandle);

#### Purpose

Clears all controls from the specified control array. 
 


This function does not discard the controls from the panel.

#### Parameters

| Input |  |  |
| --- | --- | --- |
| Name | Type | Description |
| controlArrayHandle | int | Specifier for a particular control array that is currently in memory. You obtain this handle from GetCtrlArrayFromResourceID or NewCtrlArray. |

#### Return Value

| Name | Type | Description |
| --- | --- | --- |
| status | int | Return value indicating whether the function was successful. A negative number indicates that an error occurred. |

#### Additional Information

**Library:** [User Interface Library](../../cvi/uiref/cviuser_interface_library_function_tree.htm)

**Include file:** userint.h

**LabWindows/CVI compatibility:** LabWindows/CVI 2010 and later

<!--NI_TOPIC bundle=labwindows-cvi path=cvi/uiref/cvicleardigitalgraph.htm language=enus -->
## TOPIC 00930: ClearDigitalGraph

- bundle_id: `labwindows-cvi`
- source_path: `cvi/uiref/cvicleardigitalgraph.htm`
- source_url: https://docs-be.ni.com/bundle/labwindows-cvi/raw/resource/enus/cvi/uiref/cvicleardigitalgraph.htm
- document_id: `labwindows-cvi`
- page_type: `leaf`
- content_type: ``

### ClearDigitalGraph

int ClearDigitalGraph (int panelHandle, int controlID);

#### Purpose

Deletes all plot lines from a [digital graph](../../cvi/uiref/cviprogramming_with_digital_graph_controls.htm) control. Because you cannot obtain a handle for a particular digital graph plot, you cannot delete an individual plot.

#### Supported Controls

You can use ClearDigitalGraph with [digital graph controls](../../cvi/uiref/cviprogramming_with_digital_graph_controls.htm).

#### Parameters

| Input |  |  |
| --- | --- | --- |
| Name | Type | Description |
| panelHandle | int | Specifier for a particular panel that is currently in memory. You can obtain this handle from functions such as LoadPanel and NewPanel. |
| controlID | int | The defined constant, located in the .uir header file, that you assigned to the control in the User Interface Editor, or the ID returned by functions such as NewCtrl and DuplicateCtrl. |

#### Return Value

| Name | Type | Description |
| --- | --- | --- |
| status | int | Return value indicating whether the function was successful. A negative number indicates that an error occurred. |

#### Additional Information

**Library:** [User Interface Library](../../cvi/uiref/cviuser_interface_library_function_tree.htm)

**Include file:** userint.h

**LabWindows/CVI compatibility:** LabWindows/CVI 7.1 and later

#### Example

Refer to userint\TreeBusDigitalGraph.cws for an example of using the ClearDigitalGraph function.

<!--NI_TOPIC bundle=labwindows-cvi path=cvi/uiref/cviclearfilepopupdirhistory.htm language=enus -->
## TOPIC 00931: ClearFilePopupDirHistory

- bundle_id: `labwindows-cvi`
- source_path: `cvi/uiref/cviclearfilepopupdirhistory.htm`
- source_url: https://docs-be.ni.com/bundle/labwindows-cvi/raw/resource/enus/cvi/uiref/cviclearfilepopupdirhistory.htm
- document_id: `labwindows-cvi`
- page_type: `leaf`
- content_type: ``

### ClearFilePopupDirHistory

int ClearFilePopupDirHistory (void);

#### Purpose

Clears the entries from one of the following lists depending on the function you use in conjunction with the ClearFilePopupDirHistory function:

- Previous locations list that appears in the dialog
boxes you can display with the FileSelectPopupEx , MultiFileSelectPopupEx , and DirSelectPopupEx functions.
 [IMAGE alt='Note' src='note.gif']
**Note** In addition to directories you add programmatically to the Previous locations list using the [AddToFilePopupDirHistory](../../cvi/uiref/cviaddtofilepopupdirhistory.htm) function, directories selected by the user in another application's common item dialog might also appear in the Previous locations list. The ClearFilePopupDirHistory function clears only the directories added using the AddToFilePopupDirHistory function.
- Directory history list that appears in the dialog boxes you can display with the FileSelectPopup , MultiFileSelectPopup , or DirSelectPopup functions.

#### Parameters

None.

#### Return Value

| Name | Type | Description |
| --- | --- | --- |
| status | int | Return value indicating whether the function was successful. A negative number indicates that an error occurred. |

#### Additional Information

**Library:** [User Interface Library](../../cvi/uiref/cviuser_interface_library_function_tree.htm)

**Include file:** userint.h

**LabWindows/CVI compatibility:** LabWindows/CVI 5.5 and later

<!--NI_TOPIC bundle=labwindows-cvi path=cvi/uiref/cviclearlegend.htm language=enus -->
## TOPIC 00932: ClearLegend

- bundle_id: `labwindows-cvi`
- source_path: `cvi/uiref/cviclearlegend.htm`
- source_url: https://docs-be.ni.com/bundle/labwindows-cvi/raw/resource/enus/cvi/uiref/cviclearlegend.htm
- document_id: `labwindows-cvi`
- page_type: `leaf`
- content_type: ``

### ClearLegend

int ClearLegend (int panelHandle, int controlID);

#### Purpose

Hides all items in the graph or strip chart legend.

Calling this function is equivalent to disabling the [ATTR_PLOT_LG_VISIBLE](../../cvi/uiref/cviattrplotlgvisible.htm) attribute for each plot in the graph or disabling the [ATTR_TRACE_LG_VISIBLE](../../cvi/uiref/cviattrtracelgvisible.htm) attribute for each trace in the strip chart.

#### Supported Controls

You can use ClearLegend with the following controls:

- Graphs
- Strip charts

#### Parameters

| Input |  |  |
| --- | --- | --- |
| Name | Type | Description |
| panelHandle | int | Specifier for a particular panel that is currently in memory. You can obtain this handle from functions such as LoadPanel and NewPanel. |
| controlID | int | The defined constant, located in the .uir header file, that you assigned to the control in the User Interface Editor, or the ID returned by functions such as NewCtrl and DuplicateCtrl. |

#### Return Value

| Name | Type | Description |
| --- | --- | --- |
| status | int | Return value indicating whether the function was successful. A negative number indicates that an error occurred. |

#### Additional Information

**Library:** [User Interface Library](../../cvi/uiref/cviuser_interface_library_function_tree.htm)

**Include file:** userint.h

**LabWindows/CVI compatibility:** LabWindows/CVI 7.0 and later

<!--NI_TOPIC bundle=labwindows-cvi path=cvi/uiref/cviclearlistctrl.htm language=enus -->
## TOPIC 00933: ClearListCtrl

- bundle_id: `labwindows-cvi`
- source_path: `cvi/uiref/cviclearlistctrl.htm`
- source_url: https://docs-be.ni.com/bundle/labwindows-cvi/raw/resource/enus/cvi/uiref/cviclearlistctrl.htm
- document_id: `labwindows-cvi`
- page_type: `leaf`
- content_type: ``

### ClearListCtrl

int ClearListCtrl (int panelHandle, int controlID);

#### Purpose

Clears all list items from the specified control.

#### Supported Controls

You can use ClearListCtrl with the following controls:

- Rings
- Picture rings
- Ring slides
- List boxes
- Trees

#### Parameters

| Input |  |  |
| --- | --- | --- |
| Name | Type | Description |
| panelHandle | int | Specifier for a particular panel that is currently in memory. You can obtain this handle from functions such as LoadPanel and NewPanel. |
| controlID | int | The defined constant, located in the .uir header file, that you assigned to the control in the User Interface Editor, or the ID returned by functions such as NewCtrl and DuplicateCtrl. |

#### Return Value

| Name | Type | Description |
| --- | --- | --- |
| status | int | Return value indicating whether the function was successful. A negative number indicates that an error occurred. |

#### Additional Information

**Library:** [User Interface Library](../../cvi/uiref/cviuser_interface_library_function_tree.htm)

**Include file:** userint.h

**LabWindows/CVI compatibility:** LabWindows/CVI 3.0 and later

#### Examples

Refer to the following examples that use the ClearListCtrl function:

- userint\events.cws 
 [IMAGE alt='image' src='open.gif'] Open example
- userint\imagedit.cws 
 [IMAGE alt='image' src='open.gif'] Open example
- userint\listbox.cws 
 [IMAGE alt='image' src='open.gif'] Open example

<!--NI_TOPIC bundle=labwindows-cvi path=cvi/uiref/cviclearstripchart.htm language=enus -->
## TOPIC 00934: ClearStripChart

- bundle_id: `labwindows-cvi`
- source_path: `cvi/uiref/cviclearstripchart.htm`
- source_url: https://docs-be.ni.com/bundle/labwindows-cvi/raw/resource/enus/cvi/uiref/cviclearstripchart.htm
- document_id: `labwindows-cvi`
- page_type: `leaf`
- content_type: ``

### ClearStripChart

int ClearStripChart (int panelHandle, int controlID);

#### Purpose

Clears all traces from a strip chart control.

#### Supported Controls

You can use ClearStripChart with [strip chart controls](../../cvi/uiref/cviprogramming_with_strip_chart_controls.htm).

#### Parameters

| Input |  |  |
| --- | --- | --- |
| Name | Type | Description |
| panelHandle | int | Specifier for a particular panel that is currently in memory. You can obtain this handle from functions such as LoadPanel and NewPanel. |
| controlID | int | The defined constant, located in the .uir header file, that you assigned to the control in the User Interface Editor, or the ID returned by functions such as NewCtrl and DuplicateCtrl. |

#### Return Value

| Name | Type | Description |
| --- | --- | --- |
| status | int | Return value indicating whether the function was successful. A negative number indicates that an error occurred. |

#### Additional Information

**Library:** [User Interface Library](../../cvi/uiref/cviuser_interface_library_function_tree.htm)

**Include file:** userint.h

**LabWindows/CVI compatibility:** LabWindows/CVI 3.0 and later

#### Example

Refer to apps\daqmthread\daqMT.cws for an example of using the ClearStripChart function.

<!--NI_TOPIC bundle=labwindows-cvi path=cvi/uiref/cviclipboardgetbitmap.htm language=enus -->
## TOPIC 00935: ClipboardGetBitmap

- bundle_id: `labwindows-cvi`
- source_path: `cvi/uiref/cviclipboardgetbitmap.htm`
- source_url: https://docs-be.ni.com/bundle/labwindows-cvi/raw/resource/enus/cvi/uiref/cviclipboardgetbitmap.htm
- document_id: `labwindows-cvi`
- page_type: `leaf`
- content_type: ``

### ClipboardGetBitmap

int ClipboardGetBitmap (int *bitmapID, int *available);

#### Purpose

Determines whether or not a bitmap image is available on the system clipboard and optionally retrieves a copy of the bitmap. You can pass the ID of the bitmap to any function that accepts a bitmap, such as [CanvasDrawBitmap](../../cvi/uiref/cvicanvasdrawbitmap.htm).

(Linux) This function accesses only the internal LabWindows/CVI clipboard, not the host system clipboard.

Regardless of the original color depth of bitmap on the clipboard, the bitmap that ClipboardGetBitmap creates matches the color depth of the display screen.

#### Parameters

| Output |  |  |
| --- | --- | --- |
| Name | Type | Description |
| bitmapID | int | ID that serves as a handle to the bitmap copied from the clipboard. You can pass the ID to functions that accept a bitmap, such as CanvasDrawBitmap and ClipboardPutBitmap. When you no longer need the bitmap, free it by passing the ID to DiscardBitmap. If there is no bitmap on the clipboard, bitmapID is set to NULL. If you want to check whether a bitmap is on the clipboard but do not want to retrieve it, pass 0 for this parameter. Zero is not a valid bitmap ID. |
| available | int | Indicates whether a bitmap image is available on the system clipboard. This parameter is set to 1 if a bitmap is available on the system clipboard, 0 otherwise. You can pass NULL for this parameter. |

#### Return Value

| Name | Type | Description |
| --- | --- | --- |
| status | int | Return value indicating whether the function was successful. A negative number indicates that an error occurred. |

#### Additional Information

**Library:** [User Interface Library](../../cvi/uiref/cviuser_interface_library_function_tree.htm)

**Include file:** userint.h

**LabWindows/CVI compatibility:** LabWindows/CVI 4.0 and later

#### Examples

Refer to the following examples that use the ClipboardGetBitmap function:

- apps\iconedit\iconedit.cws 
 [IMAGE alt='image' src='open.gif'] Open example
- userint\clipbord.cws 
 [IMAGE alt='image' src='open.gif'] Open example

<!--NI_TOPIC bundle=labwindows-cvi path=cvi/uiref/cviclipboardgettablevals.htm language=enus -->
## TOPIC 00936: ClipboardGetTableVals

- bundle_id: `labwindows-cvi`
- source_path: `cvi/uiref/cviclipboardgettablevals.htm`
- source_url: https://docs-be.ni.com/bundle/labwindows-cvi/raw/resource/enus/cvi/uiref/cviclipboardgettablevals.htm
- document_id: `labwindows-cvi`
- page_type: `leaf`
- content_type: ``

### ClipboardGetTableVals

int ClipboardGetTableVals (int panelHandle, int controlID, Rect cellRange, int *available);

#### Purpose

Determines whether or not text data is available on the system clipboard and/or retrieves a copy of the text and formats it into the specified cell range of a table control.

(Linux) This function accesses only the internal LabWindows/CVI clipboard, not the host system clipboard.

#### Supported Controls

You can use ClipboardGetTableVals with [table controls](../../cvi/uiref/cviprogramming_with_table_controls.htm).

#### Parameters

| Input |  |  |
| --- | --- | --- |
| Name | Type | Description |
| panelHandle | int | Specifier for a particular panel that is currently in memory. You can obtain this handle from functions such as LoadPanel and NewPanel. |
| controlID | int | The defined constant, located in the .uir header file, that you assigned to the control in the User Interface Editor, or the ID returned by functions such as NewCtrl and DuplicateCtrl. |
| cellRange | Rect | The Rect structure that specifies the cell range to which to copy the clipboard data. The Rect structure is defined as follows: typedef struct { int top; int left; int height; int width; } Rect; You can create a Rect without declaring a variable by using the following function: Rect MakeRect (int top, int left, int height, int width); The function assumes that each cell data in the clipboard is separated from the neighboring cell data with a tab character. A line feed instead of a tab character denotes the end of the data for the row. If the number of cells in a given row's data is less than the width of the cell range passed in, the extra cells in that row remain unchanged. If the number is greater than the width, the extra data of that row is ignored. The function interprets the text data for each given cell in accordance with the type of that cell. Cells of type VAL_CELL_NUMERIC remain unchanged unless the text data is convertible into a number matching the data type and format specifications of the cell. Cells of type VAL_CELL_RING remain unchanged unless the clipboard data for the cell matches an existing value in that cell's value list. Cells of type VAL_CELL_PICTURE remain unchanged unless the cell range contains a single cell and there is a bitmap available on the clipboard. |
| Output |  |  |
| Name | Type | Description |
| available | int | Indicates whether text data is available on the system clipboard. If the specified cell range consists of a single cell, and the type of that cell is VAL_CELL_PICTURE, this parameter instead indicates whether a bitmap image is available on the system clipboard. This parameter is set to 1 if text (or a bitmap) is available on the clipboard. Otherwise, it is set to 0. If you do not need this information, you can pass zero for this parameter. |

#### Return Value

| Name | Type | Description |
| --- | --- | --- |
| status | int | Return value indicating whether the function was successful. A negative number indicates that an error occurred. |

#### Additional Information

**Library:** [User Interface Library](../../cvi/uiref/cviuser_interface_library_function_tree.htm)

**Include file:** userint.h

**LabWindows/CVI compatibility:** LabWindows/CVI 5.5 and later

<!--NI_TOPIC bundle=labwindows-cvi path=cvi/uiref/cviclipboardgettext.htm language=enus -->
## TOPIC 00937: ClipboardGetText

- bundle_id: `labwindows-cvi`
- source_path: `cvi/uiref/cviclipboardgettext.htm`
- source_url: https://docs-be.ni.com/bundle/labwindows-cvi/raw/resource/enus/cvi/uiref/cviclipboardgettext.htm
- document_id: `labwindows-cvi`
- page_type: `leaf`
- content_type: ``

### ClipboardGetText

int ClipboardGetText (char **text, int *available);

#### Purpose

Determines whether or not a text string is available on the system 
clipboard and optionally retrieves a copy of the text.

When the copy of the text is no longer needed, free it by calling the 
ANSI C Library free function.

(Linux) This function accesses only the internal LabWindows/CVI clipboard, not the host system clipboard.

You can run the following example in the Interactive Execution Window.

char *text;

ClipboardGetText (&text, 0); 

 if (text != 0)

printf ("clipboard text is '%s'\n", text);

else

printf ("there is no text on the clipboard\n");

free (text);

#### Parameters

| Output |  |  |
| --- | --- | --- |
| Name | Type | Description |
| text | char * | Pointer to the null-terminated string copied from the clipboard. If no text exists on the clipboard, this pointer is set to NULL. If you want to check whether text is on the clipboard but do not want to retrieve it, pass 0 for this parameter. When the pointer is no longer needed, free the pointer by calling the free function. |
| available | int | Indicates whether text is available on the system clipboard. This parameter is set to 1 if a text string is available on the system clipboard, 0 otherwise. You can pass NULL for this parameter. |

#### Return Value

| Name | Type | Description |
| --- | --- | --- |
| status | int | Return value indicating whether the function was successful. A negative number indicates that an error occurred. |

#### Additional Information

**Library:** [User Interface Library](../../cvi/uiref/cviuser_interface_library_function_tree.htm)

**Include file:** userint.h

**LabWindows/CVI compatibility:** LabWindows/CVI 4.0 and later

#### Example

Refer to userint\clipbord.cws for an example of using the ClipboardGetText function.

<!--NI_TOPIC bundle=labwindows-cvi path=cvi/uiref/cviclipboardputbitmap.htm language=enus -->
## TOPIC 00938: ClipboardPutBitmap

- bundle_id: `labwindows-cvi`
- source_path: `cvi/uiref/cviclipboardputbitmap.htm`
- source_url: https://docs-be.ni.com/bundle/labwindows-cvi/raw/resource/enus/cvi/uiref/cviclipboardputbitmap.htm
- document_id: `labwindows-cvi`
- page_type: `leaf`
- content_type: ``

### ClipboardPutBitmap

int ClipboardPutBitmap (int bitmapID);

#### Purpose

Copies a bitmap image onto the system clipboard.

(Linux) This function affects only the internal LabWindows/CVI clipboard, not the host system clipboard.

#### Parameters

| Input |  |  |
| --- | --- | --- |
| Name | Type | Description |
| bitmapID | int | ID of the bitmap object that contains the image. You can obtain the ID from functions such as NewBitmapEx and GetCtrlBitmap. |

#### Return Value

| Name | Type | Description |
| --- | --- | --- |
| status | int | Return value indicating whether the function was successful. A negative number indicates that an error occurred. |

#### Additional Information

**Library:** [User Interface Library](../../cvi/uiref/cviuser_interface_library_function_tree.htm)

**Include file:** userint.h

**LabWindows/CVI compatibility:** LabWindows/CVI 4.0 and later

#### Examples

Refer to the following examples that use the ClipboardPutBitmap function:

- apps\iconedit\iconedit.cws 
 [IMAGE alt='image' src='open.gif'] Open example
- apps\uirview\uirview.cws 
 [IMAGE alt='image' src='open.gif'] Open example
- userint\clipbord.cws 
 [IMAGE alt='image' src='open.gif'] Open example

<!--NI_TOPIC bundle=labwindows-cvi path=cvi/uiref/cviclipboardputtablevals.htm language=enus -->
## TOPIC 00939: ClipboardPutTableVals

- bundle_id: `labwindows-cvi`
- source_path: `cvi/uiref/cviclipboardputtablevals.htm`
- source_url: https://docs-be.ni.com/bundle/labwindows-cvi/raw/resource/enus/cvi/uiref/cviclipboardputtablevals.htm
- document_id: `labwindows-cvi`
- page_type: `leaf`
- content_type: ``

### ClipboardPutTableVals

int ClipboardPutTableVals (int panelHandle, int controlID, Rect cellRange);

#### Purpose

Copies the data from the specified cell range of a table control onto the clipboard.

(Linux) This function affects only the internal LabWindows/CVI clipboard, not the host system clipboard.

#### Supported Controls

You can use ClipboardPutTableVals with [table controls](../../cvi/uiref/cviprogramming_with_table_controls.htm).

#### Parameters

| Input |  |  |
| --- | --- | --- |
| Name | Type | Description |
| panelHandle | int | Specifier for a particular panel that is currently in memory. You can obtain this handle from functions such as LoadPanel and NewPanel. |
| controlID | int | The defined constant, located in the .uir header file, that you assigned to the control in the User Interface Editor, or the ID returned by functions such as NewCtrl and DuplicateCtrl. |
| cellRange | Rect | The Rect structure that specifies the cell range from which to copy the clipboard data. The Rect structure is defined as follows: typedef struct { int top; int left; int height; int width; } Rect; You can create a Rect without having to declare a variable by using the following function: Rect MakeRect (int top, int left, int height, int width); The function places each cell data in the clipboard separated from the neighboring cell data with a tab character. For the last cell in each row, it places a line feed after its data. The function treats cells of type VAL_CELL_PICTURE as cells of type VAL_CELL_STRING containing empty strings. Only the separator tab, or line feed, is copied for such cells. However, if the cell range consists of a single cell, and its type is VAL_CELL_PICTURE, the function copies the corresponding bitmap onto the clipboard. In that case, no text is copied onto the clipboard. |

#### Return Value

| Name | Type | Description |
| --- | --- | --- |
| status | int | Return value indicating whether the function was successful. A negative number indicates that an error occurred. |

#### Additional Information

**Library:** [User Interface Library](../../cvi/uiref/cviuser_interface_library_function_tree.htm)

**Include file:** userint.h

**LabWindows/CVI compatibility:** LabWindows/CVI 5.5 and later

<!--NI_TOPIC bundle=labwindows-cvi path=cvi/uiref/cviclipboardputtext.htm language=enus -->
## TOPIC 00940: ClipboardPutText

- bundle_id: `labwindows-cvi`
- source_path: `cvi/uiref/cviclipboardputtext.htm`
- source_url: https://docs-be.ni.com/bundle/labwindows-cvi/raw/resource/enus/cvi/uiref/cviclipboardputtext.htm
- document_id: `labwindows-cvi`
- page_type: `leaf`
- content_type: ``

### ClipboardPutText

int ClipboardPutText (char text[]);

#### Purpose

Copies a NULL terminated text string onto the system clipboard.

(Linux) This function affects only the internal LabWindows/CVI clipboard, not the host system clipboard.

#### Parameters

| Input |  |  |
| --- | --- | --- |
| Name | Type | Description |
| text | char [] | Null-terminated string to copy onto the system clipboard. |

#### Return Value

| Name | Type | Description |
| --- | --- | --- |
| status | int | Return value indicating whether the function was successful. A negative number indicates that an error occurred. |

#### Additional Information

**Library:** [User Interface Library](../../cvi/uiref/cviuser_interface_library_function_tree.htm)

**Include file:** userint.h

**LabWindows/CVI compatibility:** LabWindows/CVI 4.0 and later

#### Example

Refer to userint\clipbord.cws for an example of using the ClipboardPutText function.

<!--NI_TOPIC bundle=labwindows-cvi path=cvi/uiref/cvicolor_numeric_attributes.htm language=enus -->
## TOPIC 00941: Color Numeric Control Attributes

- bundle_id: `labwindows-cvi`
- source_path: `cvi/uiref/cvicolor_numeric_attributes.htm`
- source_url: https://docs-be.ni.com/bundle/labwindows-cvi/raw/resource/enus/cvi/uiref/cvicolor_numeric_attributes.htm
- document_id: `labwindows-cvi`
- page_type: `leaf`
- content_type: ``

### Color Numeric Control Attributes

The User Interface Library attributes that are valid for
[color numeric](cvicolor_numeric_control_overview.htm)
controls appear in the following list:

#### Control Appearance

- Disable Panel Theme
- Frame Color
- Frame Thickness
- Visible
- Show/Hide Parts
- Size/Position

#### Control Settings

- Control Mode
- Control Style
- Control Value
- Default Value
- Dimmed
- Disable Control Tooltip
- Next Panel Control
- Tab Position
- Tooltip Delay
- Tooltip Hide Delay
- Tooltip Text
- Tooltip Text Length
- Z-Plane Position

#### Label Appearance

- Label Background Color
- Label Height
- Label Left
- Label Raised
- Label Size to Text
- Label Text
- Label Text Length
- Label Top
- Label Visible
- Label Width
- Label Style

#### Source Code Connection

- Callback Data
- Callback Function Name
- Callback Function Name Length
- Callback Function Pointer
- Constant Name
- Constant Name Length

<!--NI_TOPIC bundle=labwindows-cvi path=cvi/uiref/cvicolor_numeric_control_events.htm language=enus -->
## TOPIC 00942: Color Numeric Control Events

- bundle_id: `labwindows-cvi`
- source_path: `cvi/uiref/cvicolor_numeric_control_events.htm`
- source_url: https://docs-be.ni.com/bundle/labwindows-cvi/raw/resource/enus/cvi/uiref/cvicolor_numeric_control_events.htm
- document_id: `labwindows-cvi`
- page_type: `leaf`
- content_type: ``

### Color Numeric Control Events

The following User Interface Library [events](cvievents_overview.htm) are sent to [color numeric](cvicolor_numeric_control_overview.htm) control [callback](cviusing_callback_functions_to_resp.htm) functions.

- EVENT_COMMIT
- EVENT_VAL_CHANGED
- EVENT_LEFT_CLICK
- EVENT_LEFT_DOUBLE_CLICK
- EVENT_RIGHT_CLICK
- EVENT_RIGHT_DOUBLE_CLICK
- EVENT_KEYPRESS
- EVENT_GOT_FOCUS
- EVENT_LOST_FOCUS
- EVENT_DISCARD
- EVENT_MOUSE_POINTER_MOVE
- EVENT_LEFT_CLICK_UP
- EVENT_RIGHT_CLICK_UP
- EVENT_MOUSE_WHEEL_SCROLL
- EVENT_MOUSE_WHEEL_CLICK

<!--NI_TOPIC bundle=labwindows-cvi path=cvi/uiref/cvicolor_numeric_control_functions.htm language=enus -->
## TOPIC 00943: Color Numeric Control Functions

- bundle_id: `labwindows-cvi`
- source_path: `cvi/uiref/cvicolor_numeric_control_functions.htm`
- source_url: https://docs-be.ni.com/bundle/labwindows-cvi/raw/resource/enus/cvi/uiref/cvicolor_numeric_control_functions.htm
- document_id: `labwindows-cvi`
- page_type: `leaf`
- content_type: ``

### Color Numeric Control Functions

The following User Interface Library functions operate on [color numeric](cvicolor_numeric_control_overview.htm) controls.

- AddCtrlToSplitter
- DefaultCtrl
- DiscardCtrl
- DuplicateCtrl
- GetCtrlArrayIndex
- GetCtrlAttribute
- GetCtrlBoundingRect
- GetCtrlDisplayBitmap
- GetCtrlVal
- GetRelativeMouseState
- GetScaledCtrlDisplayBitmap
- InsertCtrlArrayItem
- InstallCtrlCallback
- PrintCtrl
- QueueUserEvent
- RemoveCtrlFromSplitter
- SetActiveCtrl
- SetCtrlAttribute
- SetCtrlVal
- SetInputMode

<!--NI_TOPIC bundle=labwindows-cvi path=cvi/uiref/cvicolor_numeric_control_overview.htm language=enus -->
## TOPIC 00944: Color Numeric Controls Overview

- bundle_id: `labwindows-cvi`
- source_path: `cvi/uiref/cvicolor_numeric_control_overview.htm`
- source_url: https://docs-be.ni.com/bundle/labwindows-cvi/raw/resource/enus/cvi/uiref/cvicolor_numeric_control_overview.htm
- document_id: `labwindows-cvi`
- page_type: `leaf`
- content_type: ``

### Color Numeric Controls Overview

Use *color numeric [controls](cvioperating_controls.htm)* to input or view [colors](cviusing_colors.htm). A color numeric control has a fixed [data type](cviattrdatatype_control.htm) 
of unsigned long int. Each color has a [unique 
numeric code](cviusing_colors.htm) represented by its RGB value. A sample color numeric control appears in the following figure.

[IMAGE alt='image' src='colnumcl.gif']

[Operating Color Numeric Controls](cvioperating_color_numeric_controls.htm)

[Programming Color Numeric Controls](cviprogramming_with_color_numeric_controls.htm)

[Color Numeric Control Attributes](cvicolor_numeric_attributes.htm)

[Color Numeric Control Functions](cvicolor_numeric_control_functions.htm)

[Color Numeric Control Events](cvicolor_numeric_control_events.htm)

<!--NI_TOPIC bundle=labwindows-cvi path=cvi/uiref/cvicommand_button_attributes.htm language=enus -->
## TOPIC 00945: Command Button Control Attributes

- bundle_id: `labwindows-cvi`
- source_path: `cvi/uiref/cvicommand_button_attributes.htm`
- source_url: https://docs-be.ni.com/bundle/labwindows-cvi/raw/resource/enus/cvi/uiref/cvicommand_button_attributes.htm
- document_id: `labwindows-cvi`
- page_type: `leaf`
- content_type: ``

### Command Button Control Attributes

The User Interface Library attributes that are valid for
[command button](cvicommand_button_control_overview.htm)
controls appear in the following list:

#### Control Appearance

- Command Button Color
- Disable Panel Theme
- Visible
- Size/Position

#### Control Settings

- Auto Sizing
- Control Mode
- Control Style
- Control Value
- Default Value
- Dimmed
- Disable Control Tooltip
- Next Panel Control
- Shortcut Key
- Tab Position
- Tooltip Delay
- Tooltip Hide Delay
- Tooltip Text
- Tooltip Text Length
- Z-Plane Position

#### Label Appearance

- Label Text
- Label Text Length
- Label Visible
- Label Style

#### Source Code Connection

- Callback Data
- Callback Function Name
- Callback Function Name Length
- Callback Function Pointer
- Constant Name
- Constant Name Length

<!--NI_TOPIC bundle=labwindows-cvi path=cvi/uiref/cvicommand_button_control_events.htm language=enus -->
## TOPIC 00946: Command Button Control Events

- bundle_id: `labwindows-cvi`
- source_path: `cvi/uiref/cvicommand_button_control_events.htm`
- source_url: https://docs-be.ni.com/bundle/labwindows-cvi/raw/resource/enus/cvi/uiref/cvicommand_button_control_events.htm
- document_id: `labwindows-cvi`
- page_type: `leaf`
- content_type: ``

### Command Button Control Events

The following User Interface Library [events](cvievents_overview.htm) are sent to [command button](cvicommand_button_control_overview.htm) control [callback](cviusing_callback_functions_to_resp.htm) functions.

- EVENT_COMMIT
- EVENT_LEFT_CLICK
- EVENT_LEFT_DOUBLE_CLICK
- EVENT_RIGHT_CLICK
- EVENT_RIGHT_DOUBLE_CLICK
- EVENT_KEYPRESS
- EVENT_GOT_FOCUS
- EVENT_LOST_FOCUS
- EVENT_DISCARD
- EVENT_MOUSE_POINTER_MOVE
- EVENT_LEFT_CLICK_UP
- EVENT_RIGHT_CLICK_UP
- EVENT_MOUSE_WHEEL_SCROLL
- EVENT_MOUSE_WHEEL_CLICK

<!--NI_TOPIC bundle=labwindows-cvi path=cvi/uiref/cvicommand_button_control_functions.htm language=enus -->
## TOPIC 00947: Command Button Control Functions

- bundle_id: `labwindows-cvi`
- source_path: `cvi/uiref/cvicommand_button_control_functions.htm`
- source_url: https://docs-be.ni.com/bundle/labwindows-cvi/raw/resource/enus/cvi/uiref/cvicommand_button_control_functions.htm
- document_id: `labwindows-cvi`
- page_type: `leaf`
- content_type: ``

### Command Button Control Functions

The following User Interface Library functions operate on [command button](cvicommand_button_control_overview.htm) controls.

- AddCtrlToSplitter
- DefaultCtrl
- DiscardCtrl
- DuplicateCtrl
- GetCtrlArrayIndex
- GetCtrlAttribute
- GetCtrlBoundingRect
- GetCtrlDisplayBitmap
- GetRelativeMouseState
- GetScaledCtrlDisplayBitmap
- InsertCtrlArrayItem
- InstallCtrlCallback
- PrintCtrl
- QueueUserEvent
- RemoveCtrlFromSplitter
- SetActiveCtrl
- SetCtrlAttribute
- SetInputMode

<!--NI_TOPIC bundle=labwindows-cvi path=cvi/uiref/cvicommand_button_control_overview.htm language=enus -->
## TOPIC 00948: Command Button Controls Overview

- bundle_id: `labwindows-cvi`
- source_path: `cvi/uiref/cvicommand_button_control_overview.htm`
- source_url: https://docs-be.ni.com/bundle/labwindows-cvi/raw/resource/enus/cvi/uiref/cvicommand_button_control_overview.htm
- document_id: `labwindows-cvi`
- page_type: `leaf`
- content_type: ``

### Command Button Controls Overview

Use *command button* [*controls*](cvioperating_controls.htm) to trigger an action. You can give a button a label that corresponds to its
action. A sample command button control appears in the following figure.

[IMAGE alt='image' src='cmdctrl.gif']

[Operating Command Button Controls](cvioperating_command_button_control.htm)

[Programming Command Button Controls](cviprogramming_with_command_button_controls.htm)

[Command Button Control Attributes](cvicommand_button_attributes.htm)

[Command Button Control Functions](cvicommand_button_control_functions.htm)

[Command Button Control Events](cvicommand_button_control_events.htm)

<!--NI_TOPIC bundle=labwindows-cvi path=cvi/uiref/cviconfigureprinter.htm language=enus -->
## TOPIC 00949: ConfigurePrinter

- bundle_id: `labwindows-cvi`
- source_path: `cvi/uiref/cviconfigureprinter.htm`
- source_url: https://docs-be.ni.com/bundle/labwindows-cvi/raw/resource/enus/cvi/uiref/cviconfigureprinter.htm
- document_id: `labwindows-cvi`
- page_type: `leaf`
- content_type: ``

### ConfigurePrinter

int ConfigurePrinter (char printFile[], int orientation, int imageWidth, int imageHeight, int ejectAfter);

#### Purpose

|  | Note This function has been superseded by SetPrintAttribute. |
| --- | --- |

Sets the orientation, height, width, and eject after [print attributes](../../cvi/uiref/cvilist_of_print_attributes.htm).

#### Parameters

| Input |  |  |
| --- | --- | --- |
| Name | Type | Description |
| printFile | char [] | LabWindows/CVI ignores printFile because you specify the print file at the system level. |
| orientation | int | Orientation of the image on the page. Valid Values 1 = VAL_PORTRAIT (Default) 2 = VAL_LANDSCAPE |
| imageWidth | int | Width of the image in millimeter/10 or VAL_USE_PRINTER_DEFAULT or VAL_INTEGRAL_SCALE. Depending on the resolution of the display adapter and the printer, specifying an absolute width can produce aliasing in the output. Aliasing occurs when lines on the screen are either lost or duplicated in a uneven manner on the printer. You can prevent aliasing by specifying a width of VAL_INTEGRAL_SCALE. This action causes the image width to be based on the image length. In this case, the image is scaled using an integral ratio (1:1, 1:2, 1:3, and so on) that produces an image on the printer less than or equal to the specified length. If the length is also VAL_INTEGRAL_SCALE, a scaling ratio of 1:1 is used. |
| imageHeight | int | Height of the image in millimeter/10 or VAL_USE_PRINTER_DEFAULT or VAL_INTEGRAL_SCALE. Depending on the resolution of the display adapter and the printer, specifying an absolute height can produce aliasing in the output. Aliasing occurs when lines on the screen are either lost or duplicated in a uneven manner on the printer. You can prevent aliasing by specifying a height of VAL_INTEGRAL_SCALE. This action causes the image height to be based on the image width. In this case, the image is scaled using an integral ratio (1:1, 1:2, 1:3, and so on) that produces a image on the printer less than or equal to the specified length. If the length is also VAL_INTEGRAL_SCALE, a scaling ratio of 1:1 is used. |
| ejectAfter | int | Specifies whether to eject the paper from the printer after the next call to a printing function. Specify a nonzero value or select yes in the function panel to print output on a separate page. Specify 0 or select no in the function panel to print output on the same page. |

#### Return Value

| Name | Type | Description |
| --- | --- | --- |
| status | int | Return value indicating whether the function was successful. A negative number indicates that an error occurred. |

#### Additional Information

**Library:** [User Interface Library](../../cvi/uiref/cviuser_interface_library_function_tree.htm)

**Include file:** userint.h

**LabWindows/CVI compatibility:** LabWindows/CVI 3.0 and later

<!--NI_TOPIC bundle=labwindows-cvi path=cvi/uiref/cviconfirmpopup.htm language=enus -->
## TOPIC 00950: ConfirmPopup

- bundle_id: `labwindows-cvi`
- source_path: `cvi/uiref/cviconfirmpopup.htm`
- source_url: https://docs-be.ni.com/bundle/labwindows-cvi/raw/resource/enus/cvi/uiref/cviconfirmpopup.htm
- document_id: `labwindows-cvi`
- page_type: `leaf`
- content_type: ``

### ConfirmPopup

int ConfirmPopup (char title[], char message[]);

#### Purpose

Displays a prompt message in a dialog box and waits for the user to 
select the **Yes** or **No** button.

#### Parameters

| Input |  |  |
| --- | --- | --- |
| Name | Type | Description |
| title | char [] | Title of the dialog box. |
| message | char [] | Message to display in the dialog box. To display a multi-line message, embed newline characters (\\n) in the message string. |

#### Return Value

| Name | Type | Description |
| --- | --- | --- |
| responseValue | int | The user response. 1 User selected Yes. 0 User selected No. If the value is negative, an error occurred. |
| 1 | User selected Yes. |  |
| 0 | User selected No. |  |

#### Additional Information

**Library:** [User Interface Library](../../cvi/uiref/cviuser_interface_library_function_tree.htm)

**Include file:** userint.h

**LabWindows/CVI compatibility:** LabWindows/CVI 3.0 and later

#### Examples

Refer to the following examples that use the ConfirmPopup function:

- toolbox\ini.cws 
 [IMAGE alt='image' src='open.gif'] Open example
- userint\clipbord.cws 
 [IMAGE alt='image' src='open.gif'] Open example
- userint\popups.cws 
 [IMAGE alt='image' src='open.gif'] Open example

<!--NI_TOPIC bundle=labwindows-cvi path=cvi/uiref/cviconnecting_user_interface_object.htm language=enus -->
## TOPIC 00951: Connecting User Interface Objects to Your C Source Code

- bundle_id: `labwindows-cvi`
- source_path: `cvi/uiref/cviconnecting_user_interface_object.htm`
- source_url: https://docs-be.ni.com/bundle/labwindows-cvi/raw/resource/enus/cvi/uiref/cviconnecting_user_interface_object.htm
- document_id: `labwindows-cvi`
- page_type: `leaf`
- content_type: ``

### Connecting User Interface Objects to Your C Source Code

To establish the connection between the objects in .uir 
files and C source files, prepare and include a header file with
the source code as follows:

1. Give each control a constant name . Constant names identify the controls on the GUI in calls
 to the User Interface Library functions. Several rules govern your choice of constant names .
2. As appropriate, assign callback functions 
to controls in the User Interface Editor. For example, to have a 
function called AcquireData execute whenever the command button Acquire 
 is clicked, assign the callback function name AcquireData to the Acquire 
 button in the User Interface Editor.
3. Save the .uir file. LabWindows/CVI then automatically 
generates the necessary header ( .h ) file which contains the appropriate
callback functions and ID constant names.
4. Include this .h file in the application program using the 
#include preprocessor command. The #include directive allows the program to reference the resource 
IDs and callback functions for the user interface objects. In contrast, 
 panel and menu bar 
handles are obtained at run time when using the LoadPanel and 
 LoadMenuBar functions.

<!--NI_TOPIC bundle=labwindows-cvi path=cvi/uiref/cvicontrol_array_overview.htm language=enus -->
## TOPIC 00952: Control Arrays Overview

- bundle_id: `labwindows-cvi`
- source_path: `cvi/uiref/cvicontrol_array_overview.htm`
- source_url: https://docs-be.ni.com/bundle/labwindows-cvi/raw/resource/enus/cvi/uiref/cvicontrol_array_overview.htm
- document_id: `labwindows-cvi`
- page_type: `leaf`
- content_type: ``

### Control Arrays Overview

Use an array of user interface controls to perform batch operations on the controls in the array at run time or to iterate through controls in the array at run time. Control arrays belong to the same panel as the controls that make up the array.

In addition to performing operations at run time, you can use the [User Interface Browser](../usermanual/uibrowser.htm)User Interface Browser to interactively manipulate controls in the array.

<!--NI_TOPIC bundle=labwindows-cvi path=cvi/uiref/cvicontrol_modes_for_generating_eve.htm language=enus -->
## TOPIC 00953: Control Modes for Generating Events

- bundle_id: `labwindows-cvi`
- source_path: `cvi/uiref/cvicontrol_modes_for_generating_eve.htm`
- source_url: https://docs-be.ni.com/bundle/labwindows-cvi/raw/resource/enus/cvi/uiref/cvicontrol_modes_for_generating_eve.htm
- document_id: `labwindows-cvi`
- page_type: `leaf`
- content_type: ``

### Control Modes for Generating Events

You can set the mode—Normal, Indicator, Hot, or Validate—for many 
[controls](cvioperating_controls.htm) to match the type of 
[event](cvievents_overview.htm) a control generates.

- Value changed events are generated 
when the user of the GUI modifies the setting on a
control by performing an action, like dragging the slider on a slide 
control with the mouse or entering a character in a string 
control .
- Commit events are generated when the user of the GUI actually 
commits to an operation, such as selecting from a menu , 
typing in a number and then pressing <Enter>, or releasing the mouse
button after dragging the slider on a slide control.

When creating a control, [assign](cviattrctrlmode.htm) one of the 
following control modes to determine how the control generates
events and to what extent the user can operate it.

- Normal mode specifies that the user can operate the control and that the control
generates all types of events except commit events.
- Indicator mode specifies that users cannot operate the control and that the control cannot
generate commit or value changed events. Strip chart and
 text message controls are examples of controls that are 
 always indicators.
- Hot mode is identical to Normal mode except that the control
generates a commit event when a user acts upon it. For example, if the user drags a 
 binary switch from off to on and then releases the 
mouse button, a commit event is generated.
- Validate mode is identical to Hot mode except that before a commit event is generated, the
program validates all numeric controls on the panel for which you have set the 
 range-checking attribute to Notify. 
The Notify setting causes LabWindows/CVI to check the
control value against a predefined range. If it finds an invalid condition,
LabWindows/CVI activates the control and displays a notification box like the following one. 
The validate control cannot generate a commit event until the user
enters a new, valid value into all controls that are out of range. This process
ensures that all numeric/scalar controls are valid before the GUI reports a
commit event. 

 


Numeric Control with Out Of Range Message Pop-Up

<!--NI_TOPIC bundle=labwindows-cvi path=cvi/uiref/cvicontrol_styles.htm language=enus -->
## TOPIC 00954: Control Styles

- bundle_id: `labwindows-cvi`
- source_path: `cvi/uiref/cvicontrol_styles.htm`
- source_url: https://docs-be.ni.com/bundle/labwindows-cvi/raw/resource/enus/cvi/uiref/cvicontrol_styles.htm
- document_id: `labwindows-cvi`
- page_type: `leaf`
- content_type: ``

### Control Styles

The User Interface Library distinguishes between several types of 
[controls](cvioperating_controls.htm). Each control type, in turn can encompass one or 
more control styles. Most of these control styles are the function identically, but their appearances 
may differ substantially. The following table lists the relationships between various control types and 
control styles.

#### Control Types and Styles

| Type | Style (Used in NewCtrl and ATTR_CTRL_STYLE) |
| --- | --- |
| Numeric | CTRL_NUMERIC CTRL_NUMERIC_LS |
| Color Numeric | CTRL_COLOR_NUMERIC CTRL_COLOR_NUMERIC_LS |
| Numeric Slide | CTRL_NUMERIC_THERMOMETER CTRL_NUMERIC_THERMOMETER_LS |
|  | CTRL_NUMERIC_TANK CTRL_NUMERIC_TANK_LS |
|  | CTRL_NUMERIC_GAUGE CTRL_NUMERIC_GAUGE_LS |
|  | CTRL_NUMERIC_METER CTRL_NUMERIC_METER_LS |
|  | CTRL_NUMERIC_KNOB CTRL_NUMERIC_KNOB_LS |
|  | CTRL_NUMERIC_DIAL CTRL_NUMERIC_DIAL_LS |
|  | CTRL_NUMERIC_VSLIDE |
|  | CTRL_NUMERIC_HSLIDE |
|  | CTRL_NUMERIC_FLAT_VSLIDE |
|  | CTRL_NUMERIC_FLAT_HSLIDE |
|  | CTRL_NUMERIC_LEVEL_VSLIDE CTRL_NUMERIC_LEVEL_VSLIDE_LS |
|  | CTRL_NUMERIC_LEVEL_HSLIDE CTRL_NUMERIC_LEVEL_HSLIDE_LS |
|  | CTRL_NUMERIC_POINTER_VSLIDE CTRL_NUMERIC_POINTER_VSLIDE_LS |
|  | CTRL_NUMERIC_POINTER_HSLIDE CTRL_NUMERIC_POINTER_HSLIDE_LS |
| String | CTRL_STRING CTRL_STRING_LS |
| Text Message | CTRL_TEXT_MSG |
| Text Box | CTRL_TEXT_BOX CTRL_TEXT_BOX_LS |
| Command Button | CTRL_SQUARE_COMMAND_BUTTON CTRL_SQUARE_COMMAND_BUTTON_LS |
|  | CTRL_OBLONG_COMMAND_BUTTON |
|  | CTRL_ROUND_COMMAND_BUTTON |
|  | CTRL_ROUNDED_COMMAND_BUTTON |
| Picture Button | CTRL_PICTURE_COMMAND_BUTTON CTRL_PICTURE_COMMAND_BUTTON_LS |
|  | CTRL_PICTURE_TOGGLE_BUTTON CTRL_PICTURE_TOGGLE_BUTTON_LS |
| Toggle Button | CTRL_ROUND_BUTTON |
|  | CTRL_SQUARE_BUTTON CTRL_SQUARE_BUTTON_LS |
|  | CTRL_ROUND_FLAT_BUTTON |
|  | CTRL_SQUARE_FLAT_BUTTON |
|  | CTRL_ROUND_PUSH_BUTTON |
|  | CTRL_SQUARE_PUSH_BUTTON CTRL_SQUARE_PUSH_BUTTON_LS |
|  | CTRL_ROUND_PUSH_BUTTON2 |
|  | CTRL_SQUARE_PUSH_BUTTON2 |
| Text Button | CTRL_SQUARE_TEXT_BUTTON CTRL_SQUARE_TEXT_BUTTON_LS |
|  | CTRL_OBLONG_TEXT_BUTTON |
|  | CTRL_ROUND_TEXT_BUTTON |
|  | CTRL_ROUNDED_TEXT_BUTTON |
| Radio Button | CTRL_ROUND_RADIO_BUTTON |
|  | CTRL_SQUARE_RADIO_BUTTON |
|  | CTRL_CHECK_BOX |
| LED | CTRL_ROUND_LIGHT |
|  | CTRL_SQUARE_LIGHT |
|  | CTRL_ROUND_LED CTRL_ROUND_LED_LS |
|  | CTRL_SQUARE_LED CTRL_SQUARE_LED_LS |
| Binary Switch | CTRL_HSWITCH |
|  | CTRL_VSWITCH |
|  | CTRL_GROOVED_HSWITCH |
|  | CTRL_GROOVED_VSWITCH |
|  | CTRL_TOGGLE_HSWITCH CTRL_TOGGLE_HSWITCH_LS |
|  | CTRL_TOGGLE_VSWITCH CTRL_TOGGLE_VSWITCH_LS |
| Ring | CTRL_RING CTRL_RING_LS |
|  | CTRL_RECESSED_MENU_RING CTRL_RECESSED_MENU_RING_LS |
|  | CTRL_MENU_RING CTRL_MENU_RING_LS |
|  | CTRL_POPUP_MENU_RING CTRL_POPUP_MENU_RING_LS |
| Ring Slide | CTRL_RING_VSLIDE |
|  | CTRL_RING_HSLIDE |
|  | CTRL_RING_FLAT_VSLIDE |
|  | CTRL_RING_FLAT_HSLIDE |
|  | CTRL_RING_LEVEL_VSLIDE CTRL_RING_LEVEL_VSLIDE_LS |
|  | CTRL_RING_LEVEL_HSLIDE CTRL_RING_LEVEL_HSLIDE_LS |
|  | CTRL_RING_POINTER_VSLIDE CTRL_RING_POINTER_VSLIDE_LS |
|  | CTRL_RING_POINTER_HSLIDE CTRL_RING_POINTER_HSLIDE_LS |
|  | CTRL_RING_THERMOMETER CTRL_RING_THERMOMETER_LS |
|  | CTRL_RING_TANK CTRL_RING_TANK_LS |
|  | CTRL_RING_GAUGE CTRL_RING_GAUGE_LS |
|  | CTRL_RING_METER CTRL_RING_METER_LS |
|  | CTRL_RING_KNOB CTRL_RING_KNOB_LS |
|  | CTRL_RING_DIAL CTRL_RING_DIAL_LS |
| Picture Ring | CTRL_PICTURE_RING CTRL_PICTURE_RING_LS |
| List Box | CTRL_LIST CTRL_LIST_LS |
| Tree | CTRL_TREE CTRL_TREE_LS |
| Decoration | CTRL_RAISED_BOX CTRL_RAISED_BOX_LS |
|  | CTRL_RECESSED_BOX CTRL_RECESSED_BOX_LS |
|  | CTRL_FLAT_BOX |
|  | CTRL_RAISED_CIRCLE |
|  | CTRL_RECESSED_CIRCLE |
|  | CTRL_FLAT_CIRCLE |
|  | CTRL_RAISED_FRAME |
|  | CTRL_RECESSED_FRAME CTRL_RECESSED_NARROW_FRAME |
|  | CTRL_FLAT_FRAME |
|  | CTRL_RAISED_ROUND_FRAME |
|  | CTRL_RECESSED_ROUND_FRAME |
|  | CTRL_FLAT_ROUND_FRAME |
|  | CTRL_RAISED_ROUNDED_BOX |
|  | CTRL_RECESSED_ROUNDED_BOX |
|  | CTRL_FLAT_ROUNDED_BOX CTRL_SMOOTH_VERTICAL_BOX_LS CTRL_SMOOTH_HORIZONTAL_BOX_LS |
| Graph | CTRL_GRAPH CTRL_GRAPH_LS |
| Strip Chart | CTRL_STRIP_CHART CTRL_STRIP_CHART_LS |
| Digital Graph Control | CTRL_DIGITAL_GRAPH CTRL_DIGITAL_GRAPH_LS |
| Picture | CTRL_PICTURE CTRL_PICTURE_LS |
| Timer | CTRL_TIMER |
| Canvas | CTRL_CANVAS |
| Table | CTRL_TABLE CTRL_TABLE_LS |
| Splitter | CTRL_HORIZONTAL_SPLITTER CTRL_HORIZONTAL_SPLITTER_LS CTRL_VERTICAL_SPLITTER CTRL_VERTICAL_SPLITTER_LS |
| Tab | CTRL_TABS |
| ActiveX | CTRL_ACTIVEX |

<!--NI_TOPIC bundle=labwindows-cvi path=cvi/uiref/cvicopytabpage.htm language=enus -->
## TOPIC 00955: CopyTabPage

- bundle_id: `labwindows-cvi`
- source_path: `cvi/uiref/cvicopytabpage.htm`
- source_url: https://docs-be.ni.com/bundle/labwindows-cvi/raw/resource/enus/cvi/uiref/cvicopytabpage.htm
- document_id: `labwindows-cvi`
- page_type: `leaf`
- content_type: ``

### CopyTabPage

int CopyTabPage (int sourcePanelHandle, int sourceControlID, int sourceIndex, int destinationPanelHandle, int destinationControlID, int destinationIndex);

#### Purpose

Copies a tab page to another position in the same tab control or to a different tab control.

The indices of the existing tab pages in the destination tab control at and beyond the insertion point increase by one.

The function returns the index of the new tab page or an error.

#### Supported Controls

You can use CopyTabPage with [tab controls](../../cvi/uiref/cviprogramming_with_tab_controls.htm).

#### Parameters

| Input |  |  |
| --- | --- | --- |
| Name | Type | Description |
| sourcePanelHandle | int | Handle of the source panel containing the tab page to copy. You obtain this handle from LoadPanel, NewPanel, or DuplicatePanel. |
| sourceControlID | int | The defined constant, located in the .uir header file, that you assigned to the control in the User Interface Editor, or the ID returned by NewCtrl or DuplicateCtrl. This ID refers to the tab control that contains the tab page to copy. |
| sourceIndex | int | Zero-based index of the source tab page to copy into the destination tab control. |
| destinationPanelHandle | int | The panel that contains the tab control into which you want to copy the tab page. You obtain this handle from LoadPanel, NewPanel, or DuplicatePanel. |
| destinationControlID | int | The defined constant, located in the .uir header file, that you assigned to the control in the User Interface Editor, or the ID returned by NewCtrl or DuplicateCtrl. This ID refers to the tab control into which the tab page will be copied. |
| destinationIndex | int | The zero based index into the list where CopyTabPage places the new tab page. Pass –1 to insert the new tab page at the end of the list in the destination tab control. |

#### Return Value

| Name | Type | Description |
| --- | --- | --- |
| newTabIndex | int | Returns the index of the new tab page in the destination tab control. Use this index to specify the tab page in subsequent function calls. Negative values indicate that an error occurred. |

#### Additional Information

**Library:** [User Interface Library](../../cvi/uiref/cviuser_interface_library_function_tree.htm)

**Include file:** userint.h

**LabWindows/CVI compatibility:** LabWindows/CVI 8.0 and later

#### Example

Refer to udp\UDPChat.cws for an example of using the CopyTabPage function.

<!--NI_TOPIC bundle=labwindows-cvi path=cvi/uiref/cvicopytreeitem.htm language=enus -->
## TOPIC 00956: CopyTreeItem

- bundle_id: `labwindows-cvi`
- source_path: `cvi/uiref/cvicopytreeitem.htm`
- source_url: https://docs-be.ni.com/bundle/labwindows-cvi/raw/resource/enus/cvi/uiref/cvicopytreeitem.htm
- document_id: `labwindows-cvi`
- page_type: `leaf`
- content_type: ``

### CopyTreeItem

int CopyTreeItem (int sourcePanelHandle, int sourceControlID, int sourceItemIndex, int destinationPanelHandle, int destinationControlID, int destinationRelation, int destinationRelativeIndex, int destinationPosition);

#### Purpose

Copies a tree item and its descendents to another position in the same tree or to a different tree. The position is defined by the destination relative index, the destination relation, and the destination position.

The indices of the existing items at and beyond the insertion point increase by the number of items copied.

The function returns the index of the copied item or an error.

#### Supported Controls

You can use CopyTreeItem with [tree controls](../../cvi/uiref/cviprogramming_with_tree_controls.htm).

#### Parameters

| Input |  |  |
| --- | --- | --- |
| Name | Type | Description |
| sourcePanelHandle | int | Handle of the source panel containing the tree item to copy. You obtain this handle from LoadPanel, NewPanel, or DuplicatePanel. |
| sourceControlID | int | The defined constant, located in the .uir header file, that you assigned to the control in the User Interface Editor, or the ID returned by NewCtrl or DuplicateCtrl. This ID refers to the tree control that contains the item to copy. |
| sourceItemIndex | int | Zero-based index of the source tree item to copy into the destination tree. |
| destinationPanelHandle | int | The panel that contains the tree into which you want to copy the tree item. You obtain this handle from LoadPanel, NewPanel, or DuplicatePanel. |
| destinationControlID | int | The defined constant, located in the .uir header file, that you assigned to the control in the User Interface Editor, or the ID returned by NewCtrl or DuplicateCtrl. This ID refers to the tree control into which the tree item will be copied. |
| destinationRelation | int | Defines whether the copied item will be a child or sibling of the relative item in the destination tree. This parameter is ignored if the destination tree is empty. You can use the following values: VAL_CHILD—The item is a child of the relative item. VAL_SIBLING—The item is a sibling of the relative item. |
| destinationRelativeIndex | int | Identifies the relative of the copied item in the destination tree. The destinationRelation parameter defines whether the item will become a child or sibling of the relative item in the destination tree. This parameter is ignored if the destination tree is empty. |
| destinationPosition | int | Defines the position of the copied item in the destination tree. VAL_PREV—The copied item is inserted before the relative item. Valid only for items copied as a sibling. VAL_NEXT—The copied item is inserted after the relative item. Valid only for items copied as a sibling. VAL_FIRST—If the copied item is inserted as a child, it is the first child of the relative index. If the copied item is inserted as a sibling, it is the first sibling of the relative index. VAL_LAST—If the copied item is inserted as a child, it is the last child of the relative index. If the copied item is inserted as a sibling, it is the last sibling of the relative index. This parameter is ignored if the destination tree is empty. Note To optimize tree control performance, insert child items in a position where they do not have subsequent siblings. |
|  | Note To optimize tree control performance, insert child items in a position where they do not have subsequent siblings. |  |

#### Return Value

| Name | Type | Description |
| --- | --- | --- |
| copiedItemIndex | int | Returns the index of the copied item in the destination tree. Use the index to specify the tree item in subsequent function calls. Negative values indicate that an error occurred. |

#### Additional Information

**Library:** [User Interface Library](../../cvi/uiref/cviuser_interface_library_function_tree.htm)

**Include file:** userint.h

**LabWindows/CVI compatibility:** LabWindows/CVI 7.0 and later

#### Example

Refer to userint\treecopy.cws for an example of using the CopyTreeItem function.

<!--NI_TOPIC bundle=labwindows-cvi path=cvi/uiref/cvicreatemetafont.htm language=enus -->
## TOPIC 00957: CreateMetaFont

- bundle_id: `labwindows-cvi`
- source_path: `cvi/uiref/cvicreatemetafont.htm`
- source_url: https://docs-be.ni.com/bundle/labwindows-cvi/raw/resource/enus/cvi/uiref/cvicreatemetafont.htm
- document_id: `labwindows-cvi`
- page_type: `leaf`
- content_type: ``

### CreateMetaFont

int CreateMetaFont (char newMetaFontName[], char existingFontName[], int pointSize, int bold, int italics, int underlined, int strikeout);

#### Purpose

|  | Note This function has been superseded by CreateMetaFontWithCharacterSet, which you can use to specify a value for text angle and character set. |
| --- | --- |

Creates a new metafont based on a predefined National Instruments font, an
existing metafont, or a font supplied by the operating system.

You can use metafonts that you create with this function in any control or panel attribute that requires a font.

The metafonts you create with this function contain typeface information, point size, and text style.

#### Parameters

| Input |  |  |
| --- | --- | --- |
| Name | Type | Description |
| newMetaFontName | char [] | Name to associate with the new metafont. |
| existingFontName | char [] | Name of the existing font on which to base the new metafont. The font can be a predefined font; a predefined NI metafont; a user-defined metafont saved by a previous call to functions such as CreateMetaFont and CreateMetaFontEx; or a font, such as Courier, supplied by the operating system. Predefined fonts—Contain typeface information only and use typefaces native to the operating system. The predefined fonts are VAL_MENU_FONT, VAL_DIALOG_FONT, VAL_EDITOR_FONT, VAL_APP_FONT, and VAL_MESSAGE_BOX_FONT. Predefined metafonts—Contain typeface information, point size, and text styles such as bold, underline, italic, and strikeout. These metafonts are used in the LabWindows/CVI environment. The predefined metafonts are VAL_MENU_META_FONT, VAL_DIALOG_META_FONT, VAL_EDITOR_META_FONT, VAL_APP_META_FONT, and VAL_MESSAGE_BOX_META_FONT. LabWindows/CVI-supplied metafonts—Use typefaces that are not native to the operating system. These metafonts are installed while LabWindows/CVI is running. The LabWindows/CVI-supplied metafonts are VAL_7SEG_META_FONT and VAL_SYSTEM_META_FONT. |
| pointSize | int | Point size of the new metafont. The valid range is from 1 to 255. |
| bold | int | Specify a nonzero value or select yes in the function panel to create a metafont with bold text. Specify 0 or select no in the function panel otherwise. |
| italics | int | Specify a nonzero value or select yes in the function panel to create a metafont with italicized text. Specify 0 or select no in the function panel otherwise. |
| underlined | int | Specify a nonzero value or select yes in the function panel to create a metafont with underlined text. Specify 0 or select no in the function panel otherwise. |
| strikeout | int | Specify a nonzero value or select yes in the function panel to create a metafont with strikeout text. Specify 0 or select no in the function panel otherwise. |

#### Return Value

| Name | Type | Description |
| --- | --- | --- |
| status | int | Return value indicating whether the function was successful. A negative number indicates that an error occurred. |

#### Additional Information

**Library:** [User Interface Library](../../cvi/uiref/cviuser_interface_library_function_tree.htm)

**Include file:** userint.h

**LabWindows/CVI compatibility:** LabWindows/CVI 3.0 and later

#### Example

Refer to userint\listdelx.cws for an example of using the CreateMetaFont function.

<!--NI_TOPIC bundle=labwindows-cvi path=cvi/uiref/cvicreatemetafontex.htm language=enus -->
## TOPIC 00958: CreateMetaFontEx

- bundle_id: `labwindows-cvi`
- source_path: `cvi/uiref/cvicreatemetafontex.htm`
- source_url: https://docs-be.ni.com/bundle/labwindows-cvi/raw/resource/enus/cvi/uiref/cvicreatemetafontex.htm
- document_id: `labwindows-cvi`
- page_type: `leaf`
- content_type: ``

### CreateMetaFontEx

int CreateMetaFontEx (char newMetaFontName[], char existingFontName[], int pointSize, int bold, int italics, int underlined, int strikeout, int angle);

#### Purpose

|  | Note This function has been superseded by CreateMetaFontWithCharacterSet, which you can use to specify a value for text angle and character set. |
| --- | --- |

Creates a new metafont based on a predefined National Instruments font, an existing metafont, or a font supplied by the operating system. CreateMetaFontEx is similar to [CreateMetaFont](../../cvi/uiref/cvicreatemetafont.htm), except that CreateMetaFontEx provides the **angle** parameter, which you can use to rotate the font.

You can use metafonts that you create with this function in any control or panel attribute that requires a font.

The metafonts you create with this function contain typeface information, point size, text style, and orientation angle.

#### Parameters

| Input |  |  |
| --- | --- | --- |
| Name | Type | Description |
| newMetaFontName | char [] | Name to associate with the new metafont. |
| existingFontName | char [] | Name of the existing font on which to base the new metafont. The font can be a predefined font; a predefined NI metafont; a user-defined metafont saved by a previous call to functions such as CreateMetaFont and CreateMetaFontEx; or a font, such as Courier, supplied by the operating system. Predefined fonts—Contain typeface information only and use typefaces native to the operating system. The predefined fonts are VAL_MENU_FONT, VAL_DIALOG_FONT, VAL_EDITOR_FONT, VAL_APP_FONT, and VAL_MESSAGE_BOX_FONT. Predefined metafonts—Contain typeface information, point size, and text styles such as bold, underline, italic, and strikeout. These metafonts are used in the LabWindows/CVI environment. The predefined metafonts are VAL_MENU_META_FONT, VAL_DIALOG_META_FONT, VAL_EDITOR_META_FONT, VAL_APP_META_FONT, and VAL_MESSAGE_BOX_META_FONT. LabWindows/CVI-supplied metafonts—Use typefaces that are not native to the operating system. These metafonts are installed while LabWindows/CVI is running. The LabWindows/CVI-supplied metafonts are VAL_7SEG_META_FONT and VAL_SYSTEM_META_FONT. |
| pointSize | int | Point size of the new metafont. The valid range is from 1 to 255. |
| bold | int | Specify a nonzero value or select yes in the function panel to create a metafont with bold text. Specify 0 or select no in the function panel otherwise. |
| italics | int | Specify a nonzero value or select yes in the function panel to create a metafont with italicized text. Specify 0 or select no in the function panel otherwise. |
| underlined | int | Specify a nonzero value or select yes in the function panel to create a metafont with underlined text. Specify 0 or select no in the function panel otherwise. |
| strikeout | int | Specify a nonzero value or select yes in the function panel to create a metafont with strikeout text. Specify 0 or select no in the function panel otherwise. |
| angle | int | The angle of rotation, in tenths of degrees, of the font. For example, if you want to rotate the text by 90°, specify 900. The valid range is from -32768 to 32767. The following user interface objects support rotated text: Text message controls Control labels Table row labels Table column labels Graph axis labels Strip chart axis labels Digital graph axis labels Graph annotations Text on graphs that you add using PlotText Text you place on canvas controls using CanvasDrawText or CanvasDrawTextAtPoint |

#### Return Value

| Name | Type | Description |
| --- | --- | --- |
| status | int | Return value indicating whether the function was successful. A negative number indicates that an error occurred. |

#### Additional Information

**Library:** [User Interface Library](../../cvi/uiref/cviuser_interface_library_function_tree.htm)

**Include file:** userint.h

**LabWindows/CVI compatibility:** LabWindows/CVI 8.5 and later

#### Example

Refer to userint\RotatedText.cws for an example of using the CreateMetaFontEx function.

<!--NI_TOPIC bundle=labwindows-cvi path=cvi/uiref/cvicreatemetafontwithcharacterset.htm language=enus -->
## TOPIC 00959: CreateMetaFontWithCharacterSet

- bundle_id: `labwindows-cvi`
- source_path: `cvi/uiref/cvicreatemetafontwithcharacterset.htm`
- source_url: https://docs-be.ni.com/bundle/labwindows-cvi/raw/resource/enus/cvi/uiref/cvicreatemetafontwithcharacterset.htm
- document_id: `labwindows-cvi`
- page_type: `leaf`
- content_type: ``

### CreateMetaFontWithCharacterSet

int CreateMetaFontWithCharacterSet (char newMetaFontName[], char existingFontName[], int pointSize, int bold, int italics, int underlined, int strikeout, int angle, int characterSet);

#### Purpose

Creates a new metafont based on a predefined National Instruments font, an existing metafont, or a font supplied by the operating system. CreateMetaFontWithCharacterSet is similar to [CreateMetaFontEx](../../cvi/uiref/cvicreatemetafontex.htm), except that CreateMetaFontWithCharacterSet provides the **characterSet** parameter.

You can use metafonts that you create with this function in any control or panel attribute that requires a font.

The metafonts you create with this function contain typeface and character set information, point size, text style, and orientation angle.

#### Parameters

| Input |  |  |
| --- | --- | --- |
| Name | Type | Description |
| newMetaFontName | char [] | Name to associate with the new metafont. |
| existingFontName | char [] | Name of the existing font on which to base the new metafont. The font can be a predefined font; a predefined NI metafont; a user-defined metafont saved by a previous call to functions such as CreateMetaFont and CreateMetaFontEx; or a font, such as Courier, supplied by the operating system. Predefined fonts—Contain typeface information only and use typefaces native to the operating system. The predefined fonts are VAL_MENU_FONT, VAL_DIALOG_FONT, VAL_EDITOR_FONT, VAL_APP_FONT, and VAL_MESSAGE_BOX_FONT. Predefined metafonts—Contain typeface information, point size, and text styles such as bold, underline, italic, and strikeout. These metafonts are used in the LabWindows/CVI environment. The predefined metafonts are VAL_MENU_META_FONT, VAL_DIALOG_META_FONT, VAL_EDITOR_META_FONT, VAL_APP_META_FONT, and VAL_MESSAGE_BOX_META_FONT. LabWindows/CVI-supplied metafonts—Use typefaces that are not native to the operating system. These metafonts are installed while LabWindows/CVI is running. The LabWindows/CVI-supplied metafonts are VAL_7SEG_META_FONT and VAL_SYSTEM_META_FONT. |
| pointSize | int | Point size of the new metafont. The valid range is from 1 to 255. |
| bold | int | Specify a nonzero value or select yes in the function panel to create a metafont with bold text. Specify 0 or select no in the function panel otherwise. |
| italics | int | Specify a nonzero value or select yes in the function panel to create a metafont with italicized text. Specify 0 or select no in the function panel otherwise. |
| underlined | int | Specify a nonzero value or select yes in the function panel to create a metafont with underlined text. Specify 0 or select no in the function panel otherwise. |
| strikeout | int | Specify a nonzero value or select yes in the function panel to create a metafont with strikeout text. Specify 0 or select no in the function panel otherwise. |
| angle | int | The angle of rotation, in tenths of degrees, of the font. For example, if you want to rotate the text by 90°, specify 900. The valid range is from -32768 to 32767. The following user interface objects support rotated text: Text message controls Control labels Table row labels Table column labels Graph axis labels Strip chart axis labels Digital graph axis labels Graph annotations Text on graphs that you add using PlotText Text you place on canvas controls using CanvasDrawText or CanvasDrawTextAtPoint |
| characterSet | int | The character set of the font. Note The VAL_OEM_CHARSET, VAL_SYMBOL_CHARSET, and VAL_MAC_CHARSET values are not supported and will default to the System Codepage. You can modify the System Codepage with any of the other supported character sets. You can select the following values: Value Description VAL_NATIVE_CHARSET Character set that corresponds to the language selected in the Control Panel for non-Unicode programs VAL_ANSI_CHARSET Western character set VAL_SHIFTJIS_CHARSET Japanese character set VAL_HANGUL_CHARSET Korean character set VAL_GB2312_CHARSET Simplified Chinese character set VAL_CHINESEBIG5_CHARSET Traditional Chinese character set VAL_HEBREW_CHARSET Hebrew character set VAL_ARABIC_CHARSET Arabic character set VAL_GREEK_CHARSET Greek character set VAL_TURKISH_CHARSET Turkish character set VAL_VIETNAMESE_CHARSET Vietnamese character set VAL_THAI_CHARSET Thai character set VAL_EASTEUROPE_CHARSET Eastern European character set VAL_RUSSIAN_CHARSET Cyrillic character set VAL_BALTIC_CHARSET Baltic character set |
|  | Note The VAL_OEM_CHARSET, VAL_SYMBOL_CHARSET, and VAL_MAC_CHARSET values are not supported and will default to the System Codepage. You can modify the System Codepage with any of the other supported character sets. |  |
| Value | Description |  |
| VAL_NATIVE_CHARSET | Character set that corresponds to the language selected in the Control Panel for non-Unicode programs |  |
| VAL_ANSI_CHARSET | Western character set |  |
| VAL_SHIFTJIS_CHARSET | Japanese character set |  |
| VAL_HANGUL_CHARSET | Korean character set |  |
| VAL_GB2312_CHARSET | Simplified Chinese character set |  |
| VAL_CHINESEBIG5_CHARSET | Traditional Chinese character set |  |
| VAL_HEBREW_CHARSET | Hebrew character set |  |
| VAL_ARABIC_CHARSET | Arabic character set |  |
| VAL_GREEK_CHARSET | Greek character set |  |
| VAL_TURKISH_CHARSET | Turkish character set |  |
| VAL_VIETNAMESE_CHARSET | Vietnamese character set |  |
| VAL_THAI_CHARSET | Thai character set |  |
| VAL_EASTEUROPE_CHARSET | Eastern European character set |  |
| VAL_RUSSIAN_CHARSET | Cyrillic character set |  |
| VAL_BALTIC_CHARSET | Baltic character set |  |

#### Return Value

| Name | Type | Description |
| --- | --- | --- |
| status | int | Return value indicating whether the function was successful. A negative number indicates that an error occurred. |

#### Additional Information

**Library:** [User Interface Library](../../cvi/uiref/cviuser_interface_library_function_tree.htm)

**Include file:** userint.h

**LabWindows/CVI compatibility:** LabWindows/CVI 9.0 and later

<!--NI_TOPIC bundle=labwindows-cvi path=cvi/uiref/cvicreating_objects_for_a_graphical.htm language=enus -->
## TOPIC 00960: Creating Objects for a Graphical User Interface

- bundle_id: `labwindows-cvi`
- source_path: `cvi/uiref/cvicreating_objects_for_a_graphical.htm`
- source_url: https://docs-be.ni.com/bundle/labwindows-cvi/raw/resource/enus/cvi/uiref/cvicreating_objects_for_a_graphical.htm
- document_id: `labwindows-cvi`
- page_type: `leaf`
- content_type: ``

### Creating Objects for a Graphical User Interface

You can create [Graphical User Interface (GUI)](cvigraphical_user_interface.htm) objects for your application program in the following ways:

- Create objects programmatically using function calls .
- Create objects interactively using the User Interface Editor .

After designing your GUI in LabWindows/CVI, [develop a C program](cvisteps_for_developing_and_running.htm) to process the [events](cvievents_overview.htm) generated from the user interface and to control the flow of your program.
LabWindows/CVI offers the following two basic methods for designing your
programs:

- Callback Functions —Callback functions are individual functions in your program that
are called directly by user interface controls. When any type of event is
generated on a panel, menu, or control, the appropriate callback function executes.
For example, you might have a function in your program called 
 AcquireData that you assign to a 
button labeled Acquire . Whenever a user clicks on the 
 Acquire 
button, LabWindows/CVI passes all of the event information generated by the
button directly to AcquireData , where your program takes 
appropriate action. 
It is important to 
 assign IDs and callback functions 
to every interface object.
- Event Loops —In an 
event loop, you poll for commit events by 
calling GetUserEvent . When a commit event is generated, 
 GetUserEvent returns the appropriate panel , 
 menu , or control 
identifier, then the program conditionally executes portions of code. Event
loops can poll for commit events only. To process events other than commit
events, you must install callback functions.

You can use either method in your program or combine methods for added
flexibility. However, try to limit the use of event loops to the processing of
events from [modal dialog boxes](../bp_glossary.htm#modal) (also called [pop-up panels](cvioperating_popup_panels.htm)).

Keep in mind the following distinction regarding user interface objects:

- An ID represents an object that a higher-level object must contain. An object
that is represented by an ID cannot contain other objects. For example, a
control must be within a panel and cannot contain any other controls.
- A handle for a panel or menu bar represents a top-level object that can
contain other objects. For example, if you call DiscardPanel 
on a panel handle, LabWindows/CVI not only destroys the panel itself, but also all of the controls
that the panel contains.

<!--NI_TOPIC bundle=labwindows-cvi path=cvi/uiref/cvicurrent_working_directory_and_mu.htm language=enus -->
## TOPIC 00961: Current Working Directory and Multithreading

- bundle_id: `labwindows-cvi`
- source_path: `cvi/uiref/cvicurrent_working_directory_and_mu.htm`
- source_url: https://docs-be.ni.com/bundle/labwindows-cvi/raw/resource/enus/cvi/uiref/cvicurrent_working_directory_and_mu.htm
- document_id: `labwindows-cvi`
- page_type: `leaf`
- content_type: ``

### Current Working Directory and Multithreading

Do not rely on the concept of a "current working directory" if you perform
file I/O or display [file dialog](cvifileselectpopup.htm) boxes from more than one [thread](cvidifferent_approaches_to_multithr.htm). The operating system does *not* maintain a separate working directory for each thread.

<!--NI_TOPIC bundle=labwindows-cvi path=cvi/uiref/cvicursors_and_multithreading.htm language=enus -->
## TOPIC 00962: Cursors and Multithreading

- bundle_id: `labwindows-cvi`
- source_path: `cvi/uiref/cvicursors_and_multithreading.htm`
- source_url: https://docs-be.ni.com/bundle/labwindows-cvi/raw/resource/enus/cvi/uiref/cvicursors_and_multithreading.htm
- document_id: `labwindows-cvi`
- page_type: `leaf`
- content_type: ``

### Cursors and Multithreading

Each [thread](cvidifferent_approaches_to_multithr.htm) maintains the state of the wait cursor independently. Thus, calling [SetWaitCursor](cvisetwaitcursor.htm) in one thread does *not* cause the wait cursor to appear when a [panel](cvioperating_panels.htm) you create in another thread is active.

On the other hand, the choice of mouse cursor that appears when the wait
cursor is inactive is global across all threads in a process. Thus, calling [SetMouseCursor](cvisetmousecursor.htm) changes the mouse cursor regardless of which panel is active.

<!--NI_TOPIC bundle=labwindows-cvi path=cvi/uiref/cvidecoration_attributes.htm language=enus -->
## TOPIC 00963: Decoration Control Attributes

- bundle_id: `labwindows-cvi`
- source_path: `cvi/uiref/cvidecoration_attributes.htm`
- source_url: https://docs-be.ni.com/bundle/labwindows-cvi/raw/resource/enus/cvi/uiref/cvidecoration_attributes.htm
- document_id: `labwindows-cvi`
- page_type: `leaf`
- content_type: ``

### Decoration Control Attributes

The User Interface Library attributes that are valid for
[decoration](cvidecoration_control_overview.htm)
controls appear in the following list:

#### Control Appearance

- Disable Panel Theme
- Frame Color
- Visible
- Size/Position

#### Control Settings

- Control Style
- Dimmed
- Disable Control Tooltip
- Next Panel Control
- Tooltip Delay
- Tooltip Hide Delay
- Tooltip Text
- Tooltip Text Length
- Z-Plane Position

#### Source Code Connection

- Callback Data
- Callback Function Name
- Callback Function Name Length
- Callback Function Pointer
- Constant Name
- Constant Name Length

<!--NI_TOPIC bundle=labwindows-cvi path=cvi/uiref/cvidecoration_control_events.htm language=enus -->
## TOPIC 00964: Decoration Control Events

- bundle_id: `labwindows-cvi`
- source_path: `cvi/uiref/cvidecoration_control_events.htm`
- source_url: https://docs-be.ni.com/bundle/labwindows-cvi/raw/resource/enus/cvi/uiref/cvidecoration_control_events.htm
- document_id: `labwindows-cvi`
- page_type: `leaf`
- content_type: ``

### Decoration Control Events

The following User Interface Library [events](cvievents_overview.htm) are sent to [decoration](cvidecoration_control_overview.htm) control [callback](cviusing_callback_functions_to_resp.htm) functions.

- EVENT_LEFT_CLICK
- EVENT_LEFT_DOUBLE_CLICK
- EVENT_RIGHT_CLICK
- EVENT_RIGHT_DOUBLE_CLICK
- EVENT_DISCARD
- EVENT_MOUSE_POINTER_MOVE
- EVENT_LEFT_CLICK_UP
- EVENT_RIGHT_CLICK_UP
- EVENT_MOUSE_WHEEL_CLICK

<!--NI_TOPIC bundle=labwindows-cvi path=cvi/uiref/cvidecoration_control_functions.htm language=enus -->
## TOPIC 00965: Decoration Control Functions

- bundle_id: `labwindows-cvi`
- source_path: `cvi/uiref/cvidecoration_control_functions.htm`
- source_url: https://docs-be.ni.com/bundle/labwindows-cvi/raw/resource/enus/cvi/uiref/cvidecoration_control_functions.htm
- document_id: `labwindows-cvi`
- page_type: `leaf`
- content_type: ``

### Decoration Control Functions

The following User Interface Library functions operate on [decoration](cvidecoration_control_overview.htm) controls.

- AddCtrlToSplitter
- DiscardCtrl
- DuplicateCtrl
- GetCtrlArrayIndex
- GetCtrlAttribute
- GetCtrlBoundingRect
- GetCtrlDisplayBitmap
- GetRelativeMouseState
- GetScaledCtrlDisplayBitmap
- InsertCtrlArrayItem
- InstallCtrlCallback
- PrintCtrl
- QueueUserEvent
- RemoveCtrlFromSplitter
- SetActiveCtrl
- SetCtrlAttribute
- SetInputMode

<!--NI_TOPIC bundle=labwindows-cvi path=cvi/uiref/cvidecoration_control_overview.htm language=enus -->
## TOPIC 00966: Decoration Controls Overview

- bundle_id: `labwindows-cvi`
- source_path: `cvi/uiref/cvidecoration_control_overview.htm`
- source_url: https://docs-be.ni.com/bundle/labwindows-cvi/raw/resource/enus/cvi/uiref/cvidecoration_control_overview.htm
- document_id: `labwindows-cvi`
- page_type: `leaf`
- content_type: ``

### Decoration Controls Overview

*Decoration [controls](cvioperating_controls.htm)* can enhance the visual appeal of the GUI. They do not contain data but you
can assign [callback](cviusing_callback_functions_to_resp.htm) functions to a decoration so that it can respond to mouse click [events](cvievents_overview.htm).

The following figure consists of a sampling of some different decoration [styles](cvicontrol_styles.htm):

[IMAGE alt='image' src='decor.gif']

[Operating Decoration Controls](cvioperating_decoration_controls.htm)

[Programming Decoration Controls](cviprogramming_with_decoration_controls.htm)

[Decoration Control Attributes](cvidecoration_attributes.htm)

[Decoration Control Functions](cvidecoration_control_functions.htm)

[Decoration Control Events](cvidecoration_control_events.htm)

<!--NI_TOPIC bundle=labwindows-cvi path=cvi/uiref/cvidefaultctrl.htm language=enus -->
## TOPIC 00967: DefaultCtrl

- bundle_id: `labwindows-cvi`
- source_path: `cvi/uiref/cvidefaultctrl.htm`
- source_url: https://docs-be.ni.com/bundle/labwindows-cvi/raw/resource/enus/cvi/uiref/cvidefaultctrl.htm
- document_id: `labwindows-cvi`
- page_type: `leaf`
- content_type: ``

### DefaultCtrl

int DefaultCtrl (int panelHandle, int controlID);

#### Purpose

Restores a control to its default value.

If the control is visible, it updates to reflect its default value. Assign
default values to controls in the User Interface Editor or through [SetCtrlAttribute](../../cvi/uiref/cvisetctrlattribute.htm).

#### Supported Controls

You can use DefaultCtrl with [ActiveX controls](../../cvi/uiref/cviprogramming_with_activex_controls.htm), [binary switches](../../cvi/uiref/cviprogramming_with_binary_switch_controls.htm), [color numerics](../../cvi/uiref/cviprogramming_with_color_numeric_controls.htm), [command buttons](../../cvi/uiref/cviprogramming_with_command_button_controls.htm), [LEDs](../../cvi/uiref/cviprogramming_with_led_controls.htm), [list boxes](../../cvi/uiref/cviprogramming_with_list_box_controls.htm), [numerics](../../cvi/uiref/cviprogramming_with_numeric_controls.htm), [picture buttons](../../cvi/uiref/cviprogramming_with_picture_button_controls.htm), [picture rings](../../cvi/uiref/cviprogramming_with_picture_ring_controls.htm), [radio buttons](../../cvi/uiref/cviprogramming_with_radio_button_controls.htm), [rings](../../cvi/uiref/cviprogramming_with_ring_controls.htm), [numeric slides](../../cvi/uiref/cviprogramming_with_numeric_slide_controls.htm), [ring slides](../../cvi/uiref/cviprogramming_with_ring_slide_controls.htm), [strings](../../cvi/uiref/cviprogramming_with_string_controls.htm), [tab controls](../../cvi/uiref/cviprogramming_with_tab_controls.htm), [tables](../../cvi/uiref/cviprogramming_with_table_controls.htm), [text boxes](../../cvi/uiref/cviprogramming_with_text_box_controls.htm), [text buttons](../../cvi/uiref/cviprogramming_with_text_button_controls.htm), [text messages](../../cvi/uiref/cviprogramming_with_text_message_controls.htm), [toggle buttons](../../cvi/uiref/cviprogramming_with_toggle_button_controls.htm), [trees](../../cvi/uiref/cviprogramming_with_tree_controls.htm).

#### Parameters

| Input |  |  |
| --- | --- | --- |
| Name | Type | Description |
| panelHandle | int | Specifier for a particular panel that is currently in memory. You can obtain this handle from functions such as LoadPanel and NewPanel. |
| controlID | int | The defined constant, located in the .uir header file, that you assigned to the control in the User Interface Editor, or the ID returned by functions such as NewCtrl and DuplicateCtrl. |

#### Return Value

| Name | Type | Description |
| --- | --- | --- |
| status | int | Return value indicating whether the function was successful. A negative number indicates that an error occurred. |

#### Additional Information

**Library:** [User Interface Library](../../cvi/uiref/cviuser_interface_library_function_tree.htm)

**Include file:** userint.h

**LabWindows/CVI compatibility:** LabWindows/CVI 3.0 and later

<!--NI_TOPIC bundle=labwindows-cvi path=cvi/uiref/cvidefaultpanel.htm language=enus -->
## TOPIC 00968: DefaultPanel

- bundle_id: `labwindows-cvi`
- source_path: `cvi/uiref/cvidefaultpanel.htm`
- source_url: https://docs-be.ni.com/bundle/labwindows-cvi/raw/resource/enus/cvi/uiref/cvidefaultpanel.htm
- document_id: `labwindows-cvi`
- page_type: `leaf`
- content_type: ``

### DefaultPanel

int DefaultPanel (int panelHandle);

#### Purpose

Restores all panel controls to their default values.

If the panel is visible, it updates to reflect the new control values. Assign default values to controls in the User Interface Editor or through [SetCtrlAttribute](../../cvi/uiref/cvisetctrlattribute.htm) using ATTR_DFLT_VALUE.

#### Parameters

| Input |  |  |
| --- | --- | --- |
| Name | Type | Description |
| panelHandle | int | Specifier for a particular panel that is currently in memory. You can obtain this handle from functions such as LoadPanel and NewPanel. |

#### Return Value

| Name | Type | Description |
| --- | --- | --- |
| status | int | Return value indicating whether the function was successful. A negative number indicates that an error occurred. |

#### Additional Information

**Library:** [User Interface Library](../../cvi/uiref/cviuser_interface_library_function_tree.htm)

**Include file:** userint.h

**LabWindows/CVI compatibility:** LabWindows/CVI 3.0 and later

<!--NI_TOPIC bundle=labwindows-cvi path=cvi/uiref/cvideleteaxisitem.htm language=enus -->
## TOPIC 00969: DeleteAxisItem

- bundle_id: `labwindows-cvi`
- source_path: `cvi/uiref/cvideleteaxisitem.htm`
- source_url: https://docs-be.ni.com/bundle/labwindows-cvi/raw/resource/enus/cvi/uiref/cvideleteaxisitem.htm
- document_id: `labwindows-cvi`
- page_type: `leaf`
- content_type: ``

### DeleteAxisItem

int DeleteAxisItem (int panelHandle, int controlID, int axis, int itemIndex, int numberOfItems);

#### Purpose

Deletes one or more string/value pairs from the list of label strings for a graph or strip chart axis. These strings appear in place of the numerical labels. They appear at the location of their associated values on the graph or strip chart.

To see string labels on an x-axis, you must set the ATTR_XUSE_LABEL_STRINGS attribute to TRUE. To see string labels on a y-axis, you must set the ATTR_YUSE_LABEL_STRINGS attribute to TRUE.

#### Supported Controls

You can use DeleteAxisItem with the following controls:

- Graphs
- Strip charts
- Digital graphs

#### Parameters

| Input |  |  |
| --- | --- | --- |
| Name | Type | Description |
| panelHandle | int | Specifier for a particular panel that is currently in memory. You can obtain this handle from functions such as LoadPanel and NewPanel. |
| controlID | int | The defined constant, located in the .uir header file, that you assigned to the control in the User Interface Editor, or the ID returned by functions such as NewCtrl and DuplicateCtrl. |
| axis | int | Specifies for which axis to obtain the mode and range. The following lists the valid values: VAL_BOTTOM_XAXIS (graphs only) VAL_TOP_XAXIS (graphs only) VAL_LEFT_YAXIS (graphs and strip charts) VAL_RIGHT_YAXIS (graphs only) |
| itemIndex | int | Zero-based index of the first item to delete. |
| numberOfItems | int | Number of items to delete. To delete all items from itemIndex to the end, pass –1. |

#### Return Value

| Name | Type | Description |
| --- | --- | --- |
| status | int | Return value indicating whether the function was successful. A negative number indicates that an error occurred. |

#### Additional Information

**Library:** [User Interface Library](../../cvi/uiref/cviuser_interface_library_function_tree.htm)

**Include file:** userint.h

**LabWindows/CVI compatibility:** LabWindows/CVI 4.0 and later

<!--NI_TOPIC bundle=labwindows-cvi path=cvi/uiref/cvideletectrlarrayitem.htm language=enus -->
## TOPIC 00970: DeleteCtrlArrayItem

- bundle_id: `labwindows-cvi`
- source_path: `cvi/uiref/cvideletectrlarrayitem.htm`
- source_url: https://docs-be.ni.com/bundle/labwindows-cvi/raw/resource/enus/cvi/uiref/cvideletectrlarrayitem.htm
- document_id: `labwindows-cvi`
- page_type: `leaf`
- content_type: ``

### DeleteCtrlArrayItem

int DeleteCtrlArrayItem (int controlArrayHandle, int index, int numberOfControls);

#### Purpose

Deletes one or more controls from the specified control array. 
 


This function does not discard the controls from the panel.

#### Parameters

| Input |  |  |
| --- | --- | --- |
| Name | Type | Description |
| controlArrayHandle | int | Specifier for a particular control array that is currently in memory. You obtain this handle from GetCtrlArrayFromResourceID or NewCtrlArray. |
| index | int | Zero-based index of the first control to delete. |
| numberOfControls | int | Number of controls to delete from the control array. To delete all controls from index to the end of the array, enter –1. |

#### Return Value

| Name | Type | Description |
| --- | --- | --- |
| status | int | Return value indicating whether the function was successful. A negative number indicates that an error occurred. |

#### Additional Information

**Library:** [User Interface Library](../../cvi/uiref/cviuser_interface_library_function_tree.htm)

**Include file:** userint.h

**LabWindows/CVI compatibility:** LabWindows/CVI 2010 and later

<!--NI_TOPIC bundle=labwindows-cvi path=cvi/uiref/cvideletegraphannotation.htm language=enus -->
## TOPIC 00971: DeleteGraphAnnotation

- bundle_id: `labwindows-cvi`
- source_path: `cvi/uiref/cvideletegraphannotation.htm`
- source_url: https://docs-be.ni.com/bundle/labwindows-cvi/raw/resource/enus/cvi/uiref/cvideletegraphannotation.htm
- document_id: `labwindows-cvi`
- page_type: `leaf`
- content_type: ``

### DeleteGraphAnnotation

int DeleteGraphAnnotation (int panelHandle, int controlID, int annotationIndex);

#### Purpose

Deletes the graph annotation at the specified 1-based index. If you pass –1 for **annotationIndex**, this function deletes all annotations for the specified graph.

#### Supported Controls

You can use DeleteGraphAnnotation with [graph controls](../../cvi/uiref/cviprogramming_with_graph_controls.htm).

#### Parameters

| Input |  |  |
| --- | --- | --- |
| Name | Type | Description |
| panelHandle | int | Specifier for a particular panel that is currently in memory. You can obtain this handle from functions such as LoadPanel and NewPanel. |
| controlID | int | The defined constant, located in the .uir header file, that you assigned to the control in the User Interface Editor, or the ID returned by functions such as NewCtrl and DuplicateCtrl. |
| annotationIndex | int | The 1-based index of the graph annotation to delete. If you pass –1 for the index, this function deletes all annotations for the specified graph. |

#### Return Value

| Name | Type | Description |
| --- | --- | --- |
| status | int | Return value indicating whether the function was successful. A negative number indicates that an error occurred. |

#### Additional Information

**Library:** [User Interface Library](../../cvi/uiref/cviuser_interface_library_function_tree.htm)

**Include file:** userint.h

**LabWindows/CVI compatibility:** LabWindows/CVI 8.0 and later

#### Example

Refer to userint\GraphAnnotations.cws for an example of using the DeleteGraphAnnotation function.

<!--NI_TOPIC bundle=labwindows-cvi path=cvi/uiref/cvideletegraphplot.htm language=enus -->
## TOPIC 00972: DeleteGraphPlot

- bundle_id: `labwindows-cvi`
- source_path: `cvi/uiref/cvideletegraphplot.htm`
- source_url: https://docs-be.ni.com/bundle/labwindows-cvi/raw/resource/enus/cvi/uiref/cvideletegraphplot.htm
- document_id: `labwindows-cvi`
- page_type: `leaf`
- content_type: ``

### DeleteGraphPlot

int DeleteGraphPlot (int panelHandle, int controlID, int plotHandle, int refresh);

#### Purpose

Deletes one or all plots from a graph control.

#### Supported Controls

You can use DeleteGraphPlot with [graph controls](../../cvi/uiref/cviprogramming_with_graph_controls.htm).

#### Parameters

| Input |  |  |
| --- | --- | --- |
| Name | Type | Description |
| panelHandle | int | Specifier for a particular panel that is currently in memory. You can obtain this handle from functions such as LoadPanel and NewPanel. |
| controlID | int | The defined constant, located in the .uir header file, that you assigned to the control in the User Interface Editor, or the ID returned by functions such as NewCtrl and DuplicateCtrl. |
| plotHandle | int | Handle for the particular plot to delete or –1 to delete all plots in the graph control. You can obtain plotHandle from one of the following functions: PlotX PlotY PlotXY PlotWaveform PlotPoint PlotText PlotLine PlotRectangle PlotPolygon PlotOval PlotArc PlotIntensity PlotScaledIntensity PlotBitmap |
| refresh | int | Selects when to refresh the graph control. The following choices are valid: VAL_DELAYED_DRAW = delayed draw VAL_IMMEDIATE_DRAW = immediate draw VAL_NO_DRAW = no draw If refresh is VAL_DELAYED_DRAW, the deleted plot remains on the graph until one of the following actions takes place: You rescaled the graph. You change the size of the plot area. You expose the plot area after hiding or overlapping it. You set ATTR_REFRESH_GRAPH to 1. You call RefreshGraph. You add another plot to the graph while ATTR_REFRESH_GRAPH is 1. When one of the above events occurs, LabWindows/CVI redraws the entire plot area. If refresh is VAL_IMMEDIATE_DRAW, the plot area is redrawn immediately and the deleted plot is removed from the graph. If refresh is VAL_NO_DRAW, the deleted plot remains on the graph until one of the following actions takes place: You rescale the graph. You change the size of the plot area. You expose the plot area after hiding or overlapping it, and ATTR_SMOOTH_UPDATE is 0. |

#### Return Value

| Name | Type | Description |
| --- | --- | --- |
| status | int | Return value indicating whether the function was successful. A negative number indicates that an error occurred. |

#### Additional Information

**Library:** [User Interface Library](../../cvi/uiref/cviuser_interface_library_function_tree.htm)

**Include file:** userint.h

**LabWindows/CVI compatibility:** LabWindows/CVI 3.0 and later

#### Examples

Refer to the following examples that use the DeleteGraphPlot function:

- userint\getuserevent.cws 
 [IMAGE alt='image' src='open.gif'] Open example
- userint\graphcursors.cws 
 [IMAGE alt='image' src='open.gif'] Open example
- userint\graphs.cws 
 [IMAGE alt='image' src='open.gif'] Open example
- userint\GraphZooming.cws 
 [IMAGE alt='image' src='open.gif'] Open example
- userint\TimeDateUnits.cws 
 [IMAGE alt='image' src='open.gif'] Open example
- userint\custctrl\colorpicker\colorpickerdemo.cws 
 [IMAGE alt='image' src='open.gif'] Open example

<!--NI_TOPIC bundle=labwindows-cvi path=cvi/uiref/cvideleteimage.htm language=enus -->
## TOPIC 00973: DeleteImage

- bundle_id: `labwindows-cvi`
- source_path: `cvi/uiref/cvideleteimage.htm`
- source_url: https://docs-be.ni.com/bundle/labwindows-cvi/raw/resource/enus/cvi/uiref/cvideleteimage.htm
- document_id: `labwindows-cvi`
- page_type: `leaf`
- content_type: ``

### DeleteImage

int DeleteImage (int panelHandle, int controlID);

#### Purpose

Removes an image from a picture control and from memory.

#### Supported Controls

You can use DeleteImage with [picture controls](../../cvi/uiref/cviprogramming_with_picture_controls.htm).

#### Parameters

| Input |  |  |
| --- | --- | --- |
| Name | Type | Description |
| panelHandle | int | Specifier for a particular panel that is currently in memory. You can obtain this handle from functions such as LoadPanel and NewPanel. |
| controlID | int | The defined constant, located in the .uir header file, that you assigned to the control in the User Interface Editor, or the ID returned by functions such as NewCtrl and DuplicateCtrl. |

#### Return Value

| Name | Type | Description |
| --- | --- | --- |
| status | int | Return value indicating whether the function was successful. A negative number indicates that an error occurred. |

#### Additional Information

**Library:** [User Interface Library](../../cvi/uiref/cviuser_interface_library_function_tree.htm)

**Include file:** userint.h

**LabWindows/CVI compatibility:** LabWindows/CVI 3.0 and later

#### Example

Refer to userint\custctrl\ComboBox\combodemo.cws for an example of using the DeleteImage function.

<!--NI_TOPIC bundle=labwindows-cvi path=cvi/uiref/cvideletelistitem.htm language=enus -->
## TOPIC 00974: DeleteListItem

- bundle_id: `labwindows-cvi`
- source_path: `cvi/uiref/cvideletelistitem.htm`
- source_url: https://docs-be.ni.com/bundle/labwindows-cvi/raw/resource/enus/cvi/uiref/cvideletelistitem.htm
- document_id: `labwindows-cvi`
- page_type: `leaf`
- content_type: ``

### DeleteListItem

int DeleteListItem (int panelHandle, int controlID, int itemIndex, int numberOfItems);

#### Purpose

Deletes one or more items from a list starting at **itemIndex**.

#### Supported Controls

You can use DeleteListItem with the following controls:

- Rings
- Picture rings
- Ring slides
- List boxes
- Trees

#### Parameters

| Input |  |  |
| --- | --- | --- |
| Name | Type | Description |
| panelHandle | int | Specifier for a particular panel that is currently in memory. You can obtain this handle from functions such as LoadPanel and NewPanel. |
| controlID | int | The defined constant, located in the .uir header file, that you assigned to the control in the User Interface Editor, or the ID returned by functions such as NewCtrl and DuplicateCtrl. |
| itemIndex | int | Zero-based index of the first item to delete. Note To optimize tree control performance in your application, delete child items from a position where they do not have subsequent siblings. |
|  | Note To optimize tree control performance in your application, delete child items from a position where they do not have subsequent siblings. |  |
| numberOfItems | int | Number of items to delete. To delete all items from itemIndex to the end, enter –1 for numberOfItems. When deleting items from a tree, numberOfItems refers to the number of sibling items to delete starting at itemIndex. |

#### Return Value

| Name | Type | Description |
| --- | --- | --- |
| status | int | Return value indicating whether the function was successful. A negative number indicates that an error occurred. |

#### Additional Information

**Library:** [User Interface Library](../../cvi/uiref/cviuser_interface_library_function_tree.htm)

**Include file:** userint.h

**LabWindows/CVI compatibility:** LabWindows/CVI 3.0 and later

#### Examples

Refer to the following examples that use the DeleteListItem function:

- apps\uirview\uirview.cws 
 [IMAGE alt='image' src='open.gif'] Open example
- userint\GraphAnnotations.cws 
 [IMAGE alt='image' src='open.gif'] Open example
- userint\graphlegend.cws 
 [IMAGE alt='image' src='open.gif'] Open example
- userint\listbox.cws 
 [IMAGE alt='image' src='open.gif'] Open example
- userint\listdelx.cws 
 [IMAGE alt='image' src='open.gif'] Open example
- userint\treecopy.cws 
 [IMAGE alt='image' src='open.gif'] Open example

<!--NI_TOPIC bundle=labwindows-cvi path=cvi/uiref/cvideletetablecellrangeringitems.htm language=enus -->
## TOPIC 00975: DeleteTableCellRangeRingItems

- bundle_id: `labwindows-cvi`
- source_path: `cvi/uiref/cvideletetablecellrangeringitems.htm`
- source_url: https://docs-be.ni.com/bundle/labwindows-cvi/raw/resource/enus/cvi/uiref/cvideletetablecellrangeringitems.htm
- document_id: `labwindows-cvi`
- page_type: `leaf`
- content_type: ``

### DeleteTableCellRangeRingItems

int DeleteTableCellRangeRingItems (int panelHandle, int controlID, Rect cellRange, int index, int numberOfItems);

#### Purpose

Deletes one or more items from the list of values of a specified range of ring or combo-box cells of a table control.

The indexes of the remaining values beyond the specified index are decreased by **numItems** .

#### Supported Controls

You can use DeleteTableCellRangeRingItems with [table controls](../../cvi/uiref/cviprogramming_with_table_controls.htm).

#### Parameters

| Input |  |  |
| --- | --- | --- |
| Name | Type | Description |
| panelHandle | int | Specifier for a particular panel that is currently in memory. You can obtain this handle from functions such as LoadPanel and NewPanel. |
| controlID | int | The defined constant, located in the .uir header file, that you assigned to the control in the User Interface Editor, or the ID returned by functions such as NewCtrl and DuplicateCtrl. |
| cellRange | Rect | A Rect structure specifying the range of cells from which you want to remove the values. The cells in the specified range must be of type VAL_CELL_RING, or VAL_CELL_COMBO_BOX, or a mixture of the two. If the range includes cells of any other type, an error is returned and the results are unspecified. The Rect structure is defined as follows: typedef struct { int top; int left; int height; int width; } Rect; Pass the one-based row and column indices of the first cell in the range as the top and left fields of the structure, respectively. Pass the number of columns in the range as the width field of the structure, and the number of rows in the range as the height field of the structure. You can create a Rect without having to declare a variable by using the following function: Rect MakeRect (int top, int left, int height, int width); Example DeleteTableCellRangeRingItems (panelHandle, controlID, MakeRect (2, 3, 5, 5), 1, -1); |
| index | int | The zero-based index of the first item to delete from the list of values This index must be valid for every cell in the specified range. If it is not valid for one or more cells, an error is returned and the results are unspecified. |
| numberOfItems | int | The number of items to delete. To delete all items from Index to the end, enter –1. |

#### Return Value

| Name | Type | Description |
| --- | --- | --- |
| status | int | Return value indicating whether the function was successful. A negative number indicates that an error occurred. |

#### Additional Information

**Library:** [User Interface Library](../../cvi/uiref/cviuser_interface_library_function_tree.htm)

**Include file:** userint.h

**LabWindows/CVI compatibility:** LabWindows/CVI 8.0 and later

<!--NI_TOPIC bundle=labwindows-cvi path=cvi/uiref/cvideletetablecellringitems.htm language=enus -->
## TOPIC 00976: DeleteTableCellRingItems

- bundle_id: `labwindows-cvi`
- source_path: `cvi/uiref/cvideletetablecellringitems.htm`
- source_url: https://docs-be.ni.com/bundle/labwindows-cvi/raw/resource/enus/cvi/uiref/cvideletetablecellringitems.htm
- document_id: `labwindows-cvi`
- page_type: `leaf`
- content_type: ``

### DeleteTableCellRingItems

int DeleteTableCellRingItems (int panelHandle, int controlID, Point cell, int index, int numberOfItems);

#### Purpose

Deletes one or more items from the list of values of a specified ring or combo-box cell of a table control.

The indexes of the remaining values beyond the specified index are decreased by **numItems** .

#### Supported Controls

You can use DeleteTableCellRingItems with [table controls](../../cvi/uiref/cviprogramming_with_table_controls.htm).

#### Parameters

| Input |  |  |
| --- | --- | --- |
| Name | Type | Description |
| panelHandle | int | Specifier for a particular panel that is currently in memory. You can obtain this handle from functions such as LoadPanel and NewPanel. |
| controlID | int | The defined constant, located in the .uir header file, that you assigned to the control in the User Interface Editor, or the ID returned by functions such as NewCtrl and DuplicateCtrl. |
| cell | Point | A Point structure specifying the cell from which you want to remove the values. The specified cell must be of type VAL_CELL_RING or VAL_CELL_COMBO_BOX. The Point structure is defined as follows: typedef struct { int x; int y; } Point; Pass the one-based column index of the cell in the x field of the structure, and the one-based row index of the cell in the y field of the structure. You can create a Point without having to declare a variable by using the following function: Point MakePoint (int x, int y); Example DeleteTableCellRingItems (panelHandle, controlID, MakePoint (2, 3), 1, -1); |
| index | int | The zero-based index of the first item to delete from the list of values. |
| numberOfItems | int | The number of items to delete. To delete all items from Index to the end, enter –1. |

#### Return Value

| Name | Type | Description |
| --- | --- | --- |
| status | int | Return value indicating whether the function was successful. A negative number indicates that an error occurred. |

#### Additional Information

**Library:** [User Interface Library](../../cvi/uiref/cviuser_interface_library_function_tree.htm)

**Include file:** userint.h

**LabWindows/CVI compatibility:** LabWindows/CVI 8.0 and later

<!--NI_TOPIC bundle=labwindows-cvi path=cvi/uiref/cvideletetablecolumns.htm language=enus -->
## TOPIC 00977: DeleteTableColumns

- bundle_id: `labwindows-cvi`
- source_path: `cvi/uiref/cvideletetablecolumns.htm`
- source_url: https://docs-be.ni.com/bundle/labwindows-cvi/raw/resource/enus/cvi/uiref/cvideletetablecolumns.htm
- document_id: `labwindows-cvi`
- page_type: `leaf`
- content_type: ``

### DeleteTableColumns

int DeleteTableColumns (int panelHandle, int controlID, int columnIndex, int numberOfColumns);

#### Purpose

Deletes one or more columns from a table control starting at the specified
one-based index.

#### Supported Controls

You can use DeleteTableColumns with [table controls](../../cvi/uiref/cviprogramming_with_table_controls.htm).

#### Parameters

| Input |  |  |
| --- | --- | --- |
| Name | Type | Description |
| panelHandle | int | Specifier for a particular panel that is currently in memory. You can obtain this handle from functions such as LoadPanel and NewPanel. |
| controlID | int | The defined constant, located in the .uir header file, that you assigned to the control in the User Interface Editor, or the ID returned by functions such as NewCtrl and DuplicateCtrl. |
| columnIndex | int | The one-based index of the first column to delete. |
| numberOfColumns | int | The number of columns to delete. To delete all items from columnIndex to the end, enter –1. |

#### Return Value

| Name | Type | Description |
| --- | --- | --- |
| status | int | Return value indicating whether the function was successful. A negative number indicates that an error occurred. |

#### Additional Information

**Library:** [User Interface Library](../../cvi/uiref/cviuser_interface_library_function_tree.htm)

**Include file:** userint.h

**LabWindows/CVI compatibility:** LabWindows/CVI 5.5 and later

<!--NI_TOPIC bundle=labwindows-cvi path=cvi/uiref/cvideletetablerows.htm language=enus -->
## TOPIC 00978: DeleteTableRows

- bundle_id: `labwindows-cvi`
- source_path: `cvi/uiref/cvideletetablerows.htm`
- source_url: https://docs-be.ni.com/bundle/labwindows-cvi/raw/resource/enus/cvi/uiref/cvideletetablerows.htm
- document_id: `labwindows-cvi`
- page_type: `leaf`
- content_type: ``

### DeleteTableRows

int DeleteTableRows (int panelHandle, int controlID, int rowIndex, int numberOfRows);

#### Purpose

Deletes one or more rows from a table control starting at the specified
one-based index.

#### Supported Controls

You can use DeleteTableRows with [table controls](../../cvi/uiref/cviprogramming_with_table_controls.htm).

#### Parameters

| Input |  |  |
| --- | --- | --- |
| Name | Type | Description |
| panelHandle | int | Specifier for a particular panel that is currently in memory. You can obtain this handle from functions such as LoadPanel and NewPanel. |
| controlID | int | The defined constant, located in the .uir header file, that you assigned to the control in the User Interface Editor, or the ID returned by functions such as NewCtrl and DuplicateCtrl. |
| rowIndex | int | The one-based index of the first row to delete. |
| numberOfRows | int | The number of rows to delete. To delete all items from rowIndex to the end, enter –1. |

#### Return Value

| Name | Type | Description |
| --- | --- | --- |
| status | int | Return value indicating whether the function was successful. A negative number indicates that an error occurred. |

#### Additional Information

**Library:** [User Interface Library](../../cvi/uiref/cviuser_interface_library_function_tree.htm)

**Include file:** userint.h

**LabWindows/CVI compatibility:** LabWindows/CVI 5.5 and later

#### Example

Refer to utility\threading\ThreadPool\ParallelTestInit\ParallelTestInit.cws for an example of using the DeleteTableRows function.

<!--NI_TOPIC bundle=labwindows-cvi path=cvi/uiref/cvideletetabpage.htm language=enus -->
## TOPIC 00979: DeleteTabPage

- bundle_id: `labwindows-cvi`
- source_path: `cvi/uiref/cvideletetabpage.htm`
- source_url: https://docs-be.ni.com/bundle/labwindows-cvi/raw/resource/enus/cvi/uiref/cvideletetabpage.htm
- document_id: `labwindows-cvi`
- page_type: `leaf`
- content_type: ``

### DeleteTabPage

int DeleteTabPage (int panelHandle, int controlID, int index, int numberOfTabPages);

#### Purpose

Deletes tab pages from a tab control.

#### Supported Controls

You can use DeleteTabPage with [tab controls](../../cvi/uiref/cviprogramming_with_tab_controls.htm).

#### Parameters

| Input |  |  |
| --- | --- | --- |
| Name | Type | Description |
| panelHandle | int | Specifier for a particular panel that is currently in memory. You can obtain this handle from functions such as LoadPanel and NewPanel. |
| controlID | int | The defined constant, located in the .uir header file, that you assigned to the control in the User Interface Editor, or the ID returned by functions such as NewCtrl and DuplicateCtrl. |
| index | int | Zero-based index of the tab page to delete. |
| numberOfTabPages | int | Number of tab pages to delete. To delete all tab pages from index to the end, enter –1 for numberOfTabPages. |

#### Return Value

| Name | Type | Description |
| --- | --- | --- |
| status | int | Return value indicating whether the function was successful. A negative number indicates that an error occurred. |

#### Additional Information

**Library:** [User Interface Library](../../cvi/uiref/cviuser_interface_library_function_tree.htm)

**Include file:** userint.h

**LabWindows/CVI compatibility:** LabWindows/CVI 8.0 and later

#### Example

Refer to udp\UDPChat.cws for an example of using the DeleteTabPage function.

<!--NI_TOPIC bundle=labwindows-cvi path=cvi/uiref/cvideletetextboxline.htm language=enus -->
## TOPIC 00980: DeleteTextBoxLine

- bundle_id: `labwindows-cvi`
- source_path: `cvi/uiref/cvideletetextboxline.htm`
- source_url: https://docs-be.ni.com/bundle/labwindows-cvi/raw/resource/enus/cvi/uiref/cvideletetextboxline.htm
- document_id: `labwindows-cvi`
- page_type: `leaf`
- content_type: ``

### DeleteTextBoxLine

int DeleteTextBoxLine (int panelHandle, int controlID, int lineIndex);

#### Purpose

Removes a line of text from a text box control at the specified index.

|  | Note The function removes the newline character that terminates the line at the specified index, if one exists. |
| --- | --- |

#### Supported Controls

You can use DeleteTextBoxLine with [text box controls](../../cvi/uiref/cviprogramming_with_text_box_controls.htm).

#### Parameters

| Input |  |  |
| --- | --- | --- |
| Name | Type | Description |
| panelHandle | int | Specifier for a particular panel that is currently in memory. You can obtain this handle from functions such as LoadPanel and NewPanel. |
| controlID | int | The defined constant, located in the .uir header file, that you assigned to the control in the User Interface Editor, or the ID returned by functions such as NewCtrl and DuplicateCtrl. |
| lineIndex | int | Zero-based index into the text box. |

#### Return Value

| Name | Type | Description |
| --- | --- | --- |
| status | int | Return value indicating whether the function was successful. A negative number indicates that an error occurred. |

#### Additional Information

**Library:** [User Interface Library](../../cvi/uiref/cviuser_interface_library_function_tree.htm)

**Include file:** userint.h

**LabWindows/CVI compatibility:** LabWindows/CVI 3.0 and later

#### Example

Refer to userint\textbox.cws for an example of using the DeleteTextBoxLine function.

<!--NI_TOPIC bundle=labwindows-cvi path=cvi/uiref/cvideletetextboxlines.htm language=enus -->
## TOPIC 00981: DeleteTextBoxLines

- bundle_id: `labwindows-cvi`
- source_path: `cvi/uiref/cvideletetextboxlines.htm`
- source_url: https://docs-be.ni.com/bundle/labwindows-cvi/raw/resource/enus/cvi/uiref/cvideletetextboxlines.htm
- document_id: `labwindows-cvi`
- page_type: `leaf`
- content_type: ``

### DeleteTextBoxLines

int DeleteTextBoxLines (int panelHandle, int controlID, int lineIndex, int numberOfLines);

#### Purpose

Deletes one or more lines from a text box starting at the specified zero-based
index.

#### Supported Controls

You can use DeleteTextBoxLines with [text box controls](../../cvi/uiref/cviprogramming_with_text_box_controls.htm).

#### Parameters

| Input |  |  |
| --- | --- | --- |
| Name | Type | Description |
| panelHandle | int | Specifier for a particular panel that is currently in memory. You can obtain this handle from functions such as LoadPanel and NewPanel. |
| controlID | int | The defined constant, located in the .uir header file, that you assigned to the control in the User Interface Editor, or the ID returned by functions such as NewCtrl and DuplicateCtrl. |
| lineIndex | int | Zero-based index into the text box. |
| numberOfLines | int | The number of lines to delete. To delete all lines from lineIndex to the end, pass –1. |

#### Return Value

| Name | Type | Description |
| --- | --- | --- |
| status | int | Return value indicating whether the function was successful. A negative number indicates that an error occurred. |

#### Additional Information

**Library:** [User Interface Library](../../cvi/uiref/cviuser_interface_library_function_tree.htm)

**Include file:** userint.h

**LabWindows/CVI compatibility:** LabWindows/CVI 5.5 and later

<!--NI_TOPIC bundle=labwindows-cvi path=cvi/uiref/cvideletetreecellringitems.htm language=enus -->
## TOPIC 00982: DeleteTreeCellRingItems

- bundle_id: `labwindows-cvi`
- source_path: `cvi/uiref/cvideletetreecellringitems.htm`
- source_url: https://docs-be.ni.com/bundle/labwindows-cvi/raw/resource/enus/cvi/uiref/cvideletetreecellringitems.htm
- document_id: `labwindows-cvi`
- page_type: `leaf`
- content_type: ``

### DeleteTreeCellRingItems

int DeleteTreeCellRingItems (int panelHandle, int controlID, int itemIndex, int columnIndex, int ringIndex, int numberOfItems);

#### Purpose

Deletes one or more items from the list of values of a specified ring or combo box cell of a tree control.

LabWindows/CVI decreases the indexes of the remaining values beyond the specified index by **numberOfItems**.

#### Supported Controls

You can use DeleteTreeCellRingItems with [tree controls](../../cvi/uiref/cviprogramming_with_tree_controls.htm).

#### Parameters

| Input |  |  |
| --- | --- | --- |
| Name | Type | Description |
| panelHandle | int | Specifier for a particular panel that is currently in memory. You can obtain this handle from functions such as LoadPanel and NewPanel. |
| controlID | int | The defined constant, located in the .uir header file, that you assigned to the control in the User Interface Editor, or the ID returned by functions such as NewCtrl and DuplicateCtrl. |
| itemIndex | int | Zero-based index of the tree item containing the cell from which you want to remove the value(s). |
| columnIndex | int | Zero-based index of the tree column that contains the cell from which you want to remove the value(s). |
| ringIndex | int | The zero-based index of the first item to delete from the list of values. |
| numberOfItems | int | The number of items to delete. To delete all items from ringIndex to the end of the list of values, enter –1. |

#### Return Value

| Name | Type | Description |
| --- | --- | --- |
| status | int | Return value indicating whether the function was successful. A negative number indicates that an error occurred. |

#### Additional Information

**Library:** [User Interface Library](../../cvi/uiref/cviuser_interface_library_function_tree.htm)

**Include file:** userint.h

**LabWindows/CVI compatibility:** LabWindows/CVI 2009 and later

<!--NI_TOPIC bundle=labwindows-cvi path=cvi/uiref/cvideletetreecolumn.htm language=enus -->
## TOPIC 00983: DeleteTreeColumn

- bundle_id: `labwindows-cvi`
- source_path: `cvi/uiref/cvideletetreecolumn.htm`
- source_url: https://docs-be.ni.com/bundle/labwindows-cvi/raw/resource/enus/cvi/uiref/cvideletetreecolumn.htm
- document_id: `labwindows-cvi`
- page_type: `leaf`
- content_type: ``

### DeleteTreeColumn

int DeleteTreeColumn (int panelHandle, int controlID, int columnIndex);

#### Purpose

Deletes the column at the specified index.

You cannot delete column zero.

#### Supported Controls

You can use DeleteTreeColumn with [tree controls](../../cvi/uiref/cviprogramming_with_tree_controls.htm).

#### Parameters

| Input |  |  |
| --- | --- | --- |
| Name | Type | Description |
| panelHandle | int | Specifier for a particular panel that is currently in memory. You can obtain this handle from functions such as LoadPanel and NewPanel. |
| controlID | int | The defined constant, located in the .uir header file, that you assigned to the control in the User Interface Editor, or the ID returned by functions such as NewCtrl and DuplicateCtrl. |
| columnIndex | int | Zero-based index of the column to delete. You cannot delete column zero. Pass –1 to delete the last column. |

#### Return Value

| Name | Type | Description |
| --- | --- | --- |
| status | int | Return value indicating whether the function was successful. A negative number indicates that an error occurred. |

#### Additional Information

**Library:** [User Interface Library](../../cvi/uiref/cviuser_interface_library_function_tree.htm)

**Include file:** userint.h

**LabWindows/CVI compatibility:** LabWindows/CVI 7.0 and later

<!--NI_TOPIC bundle=labwindows-cvi path=cvi/uiref/cvidifferent_approaches_to_multithr.htm language=enus -->
## TOPIC 00984: Different Approaches to Multithreaded User Interface Programming

- bundle_id: `labwindows-cvi`
- source_path: `cvi/uiref/cvidifferent_approaches_to_multithr.htm`
- source_url: https://docs-be.ni.com/bundle/labwindows-cvi/raw/resource/enus/cvi/uiref/cvidifferent_approaches_to_multithr.htm
- document_id: `labwindows-cvi`
- page_type: `leaf`
- content_type: ``

### Different Approaches to Multithreaded User Interface Programming

You can take three general approaches to the use of [multiple threads](../programmerref/multithreadingoverview.htm)multiple threads in conjunction with the User Interface Library.

#### Perform All User Interface Processing in the Main Thread

The first approach is to perform all of your user interface processing in the
main thread. Create [panels](cvioperating_panels.htm) and call functions like [SetCtrlAttribute](cvisetctrlattribute.htm) and [SetCtrlVal](cvisetctrlval.htm) in the main thread; use your other threads for I/O processing or data analysis. For example, you can acquire data continuously in a secondary thread. If
you want to display the data in the main thread, you can place the
acquired data in a global variable and use state variables to indicate how much data
is available for display. If you use global variables, you must ensure that they are [thread safe](../libref/thread_safe_variable_class_utility.html).

Another example of the first approach is to create a new thread each time the
user clicks a [command button](cvicommand_button_control_overview.htm) on your user interface panel. Each thread performs the assigned task and then
terminates. Because a secondary thread performs the user-requested task, the
user can continue to operate the user interface panel without waiting for the
task to complete.

#### Separate User Interface Processing in Multiple Threads

In the second approach, you create all of your panels in the main thread but
call functions such as SetCtrlAttribute and SetCtrlVal from different threads. For instance, if you perform data acquisition
in a secondary thread, you can update a [numeric](cvinumeric_control_overview.htm) control with a newly acquired data point by calling SetCtrlVal from the data acquisition thread.

#### Create Panels Using Multiple Threads

In the third approach, you create panels in multiple threads. The set of
panels in each thread behaves almost as if it were in a separate process. For
instance, each set of panels is in a separate [z-plane](cviattrzplaneposition_panel.htm) grouping. The panels in the thread of the active panel are on top of the
panels in the other threads. Also, [pop-up panels](cvioperating_popup_panels.htm) are [modal](../bp_glossary.htm#modal) only with respect to panels of the same thread. If you use [InstallPopup](cviinstallpopup.htm) to display a dialog box, the user cannot access any other panels in the
same thread, but is free to operate panels you create in different threads. You
can display a separate task bar button for each thread.

<!--NI_TOPIC bundle=labwindows-cvi path=cvi/uiref/cvidigital_graph_attributes.htm language=enus -->
## TOPIC 00985: Digital Graph Control Attributes

- bundle_id: `labwindows-cvi`
- source_path: `cvi/uiref/cvidigital_graph_attributes.htm`
- source_url: https://docs-be.ni.com/bundle/labwindows-cvi/raw/resource/enus/cvi/uiref/cvidigital_graph_attributes.htm
- document_id: `labwindows-cvi`
- page_type: `leaf`
- content_type: ``

### Digital Graph Control Attributes

The User Interface Library attributes that are valid for
[digital graph](cvidigital_graph_control_overview.htm)
controls appear in the following list:

#### Control Appearance

- Disable Panel Theme
- Edge Style
- Fixed Plot Area
- Graph Background Color
- Grid Color
- Grid Style
- Plot Area Height
- Plot Area Left
- Plot Area Top
- Plot Area Width
- Plot Background Color
- Visible
- Axis Names
- Show/Hide Parts
- Size/Position

#### Control Settings

- Autosize Plots
- Bus Label
- Bus Label Length
- Control Mode
- Control Style
- Digital Graph Plot Color
- Dimmed
- Disable Control Tooltip
- Expand Buses
- Line Label
- Line Label Length
- Next Panel Control
- Refresh Graph
- Show State Labels
- Smooth Update
- State Label Font
- State Label Font Length
- Tab Position
- Tooltip Delay
- Tooltip Hide Delay
- Tooltip Text
- Tooltip Text Length
- Z-Plane Position
- X-Axis
- Y-Axis

#### Label Appearance

- Label Background Color
- Label Height
- Label Left
- Label Raised
- Label Size to Text
- Label Text
- Label Text Length
- Label Top
- Label Visible
- Label Width
- Label Style

#### Source Code Connection

- Callback Data
- Callback Function Name
- Callback Function Name Length
- Callback Function Pointer
- Constant Name
- Constant Name Length

<!--NI_TOPIC bundle=labwindows-cvi path=cvi/uiref/cvidigital_graph_control_events.htm language=enus -->
## TOPIC 00986: Digital Graph Control Events

- bundle_id: `labwindows-cvi`
- source_path: `cvi/uiref/cvidigital_graph_control_events.htm`
- source_url: https://docs-be.ni.com/bundle/labwindows-cvi/raw/resource/enus/cvi/uiref/cvidigital_graph_control_events.htm
- document_id: `labwindows-cvi`
- page_type: `leaf`
- content_type: ``

### Digital Graph Control Events

The following User Interface Library [events](cvievents_overview.htm) are sent to [digital graph](cvidigital_graph_control_overview.htm) control [callback](cviusing_callback_functions_to_resp.htm) functions.

- EVENT_LEFT_CLICK
- EVENT_LEFT_DOUBLE_CLICK
- EVENT_RIGHT_CLICK
- EVENT_RIGHT_DOUBLE_CLICK
- EVENT_DISCARD
- EVENT_MOUSE_POINTER_MOVE
- EVENT_LEFT_CLICK_UP
- EVENT_RIGHT_CLICK_UP
- EVENT_MOUSE_WHEEL_SCROLL
- EVENT_MOUSE_WHEEL_CLICK

<!--NI_TOPIC bundle=labwindows-cvi path=cvi/uiref/cvidigital_graph_control_functions.htm language=enus -->
## TOPIC 00987: Digital Graph Control Functions

- bundle_id: `labwindows-cvi`
- source_path: `cvi/uiref/cvidigital_graph_control_functions.htm`
- source_url: https://docs-be.ni.com/bundle/labwindows-cvi/raw/resource/enus/cvi/uiref/cvidigital_graph_control_functions.htm
- document_id: `labwindows-cvi`
- page_type: `leaf`
- content_type: ``

### Digital Graph Control Functions

The following User Interface Library functions operate on [digital graph](cvidigital_graph_control_overview.htm) controls.

- AddCtrlToSplitter
- ClearAxisItems
- ClearDigitalGraph
- DeleteAxisItem
- DiscardCtrl
- DuplicateCtrl
- GetAxisItem
- GetAxisItemLabelLength
- GetAxisRange
- GetAxisScalingMode
- GetAxisTimeFormat
- GetCtrlArrayIndex
- GetCtrlAttribute
- GetCtrlBoundingRect
- GetCtrlDisplayBitmap
- GetRelativeMouseState
- GetScaledCtrlDisplayBitmap
- InsertAxisItem
- InsertCtrlArrayItem
- InstallCtrlCallback
- PlotDigitalLines
- PlotDigitalLinesMultiBus
- PlotPackedDigitalLines
- PlotPackedDigitalLinesMultiBus
- PrintCtrl
- QueueUserEvent
- RemoveCtrlFromSplitter
- ReplaceAxisItem
- SetActiveCtrl
- SetAxisRange
- SetAxisScalingMode
- SetAxisTimeFormat
- SetCtrlAttribute
- SetInputMode

<!--NI_TOPIC bundle=labwindows-cvi path=cvi/uiref/cvidigital_graph_control_overview.htm language=enus -->
## TOPIC 00988: Digital Graph Controls Overview

- bundle_id: `labwindows-cvi`
- source_path: `cvi/uiref/cvidigital_graph_control_overview.htm`
- source_url: https://docs-be.ni.com/bundle/labwindows-cvi/raw/resource/enus/cvi/uiref/cvidigital_graph_control_overview.htm
- document_id: `labwindows-cvi`
- page_type: `leaf`
- content_type: ``

### Digital Graph Controls Overview

*Digital graph [controls](cvioperating_controls.htm)* display arrays of data as lines or buses. A sample digital graph control appears in the following figure.

[IMAGE alt='image' src='digitalgraph.gif']

**Digital Graph Control**

[Operating Digital Graph Controls](cvioperating_digital_graph_controls.htm)

[Programming Digital Graph Controls](cviprogramming_with_digital_graph_controls.htm)

[Digital Graph Control Attributes](cvidigital_graph_attributes.htm)

[Digital Graph Control Functions](cvidigital_graph_control_functions.htm)

[Digital Graph Control Events](cvidigital_graph_control_events.htm)

<!--NI_TOPIC bundle=labwindows-cvi path=cvi/uiref/cvidirselectpopup.htm language=enus -->
## TOPIC 00989: DirSelectPopup

- bundle_id: `labwindows-cvi`
- source_path: `cvi/uiref/cvidirselectpopup.htm`
- source_url: https://docs-be.ni.com/bundle/labwindows-cvi/raw/resource/enus/cvi/uiref/cvidirselectpopup.htm
- document_id: `labwindows-cvi`
- page_type: `leaf`
- content_type: ``

### DirSelectPopup

int DirSelectPopup (char defaultDirectory[], char title[], int allowCancel, int allowMakeDirectory, char pathName[]);

#### Purpose

|  | Note This function has been superseded by DirSelectPopupEx. Use DirSelectPopupEx to display a Windows Vista and later style dialog box. |
| --- | --- |

Displays a directory selection dialog box and waits for the user to select 
a directory or cancel.

#### Parameters

| Input |  |  |
| --- | --- | --- |
| Name | Type | Description |
| title | char [] | Title of the dialog box. |
| allowCancel | int | Specify a nonzero value or select yes in the function panel to allow the user to cancel out of the dialog box. Specify 0 or select no in the function panel to force the user to make a selection before exiting the dialog box. |
| allowMakeDirectory | int | Specify a nonzero value or select yes in the function panel to display a new directory icon that allows the user to create a new directory from the dialog box. This option is useful when a user wants to save a file into a new directory. Specify 0 or select no in the function panel to not include the icon in the dialog box. Note Specifying 0 or selecting no in the function panel does not prevent users from right-clicking in the file list of the dialog box and selecting New»Folder to create a new directory. |
|  | Note Specifying 0 or selecting no in the function panel does not prevent users from right-clicking in the file list of the dialog box and selecting New»Folder to create a new directory. |  |
| Output |  |  |
| Name | Type | Description |

#### Return Value

| Name | Type | Description |
| --- | --- | --- |
| selectionStatus | int | The selection status or error codes generated during the function call. 0 VAL_NO_DIRECTORY_SELECTED 1 VAL_DIRECTORY_SELECTED Negative values indicate that an error occurred. |
| 0 | VAL_NO_DIRECTORY_SELECTED |  |
| 1 | VAL_DIRECTORY_SELECTED |  |

#### Additional Information

**Library:** [User Interface Library](../../cvi/uiref/cviuser_interface_library_function_tree.htm)

**Include file:** userint.h

**LabWindows/CVI compatibility:** LabWindows/CVI 4.0 and later

<!--NI_TOPIC bundle=labwindows-cvi path=cvi/uiref/cvidirselectpopupex.htm language=enus -->
## TOPIC 00990: DirSelectPopupEx

- bundle_id: `labwindows-cvi`
- source_path: `cvi/uiref/cvidirselectpopupex.htm`
- source_url: https://docs-be.ni.com/bundle/labwindows-cvi/raw/resource/enus/cvi/uiref/cvidirselectpopupex.htm
- document_id: `labwindows-cvi`
- page_type: `leaf`
- content_type: ``

### DirSelectPopupEx

int DirSelectPopupEx (char defaultDirectory[], char title[], char pathName[]);

#### Purpose

Displays a directory selection dialog box and waits for the user to select a directory or cancel.

(Linux) There are no differences between the directory selection dialog box displayed with [DirSelectPopup](../../cvi/uiref/cvidirselectpopup.htm) and DirSelectPopupEx.

|  | Note The underlying Windows SDK function used to create and run the DirSelectPopupEx dialog box does not work properly when the threading modelthreading model is multithread apartment (MTA). ActiveX functions use this thread type by default, and calling any ActiveX function initializes the thread to MTA. This might cause subsequent calls to the DirSelectPopupEx function to return an error. To ensure the DirSelectPopupEx dialog box works properly, LabWindows/CVI initializes the thread calling the DirSelectPopupEx function to COINIT_APARTMENTTHREADED prior to creating the dialog box. If you want to run in the default MTA threading model, consider calling the DirSelectPopupEx function from a different thread that does not call any ActiveX functions. You can explicitly set the ActiveX threading model for a thread using the CA_InitActiveXThreadStyleForCurrentThreadCA_InitActiveXThreadStyleForCurrentThread function. |
| --- | --- |

#### Parameters

| Input |  |  |
| --- | --- | --- |
| Name | Type | Description |
| title | char [] | Title of the dialog box. |
| Output |  |  |
| Name | Type | Description |

#### Return Value

| Name | Type | Description |
| --- | --- | --- |
| selectionStatus | int | The selection status or error codes generated during the function call. 0 VAL_NO_DIRECTORY_SELECTED 1 VAL_DIRECTORY_SELECTED Negative values indicate that an error occurred. |
| 0 | VAL_NO_DIRECTORY_SELECTED |  |
| 1 | VAL_DIRECTORY_SELECTED |  |

#### Additional Information

**Library:** [User Interface Library](../../cvi/uiref/cviuser_interface_library_function_tree.htm)

**Include file:** userint.h

**LabWindows/CVI compatibility:** LabWindows/CVI 2012 and later

<!--NI_TOPIC bundle=labwindows-cvi path=cvi/uiref/cvidiscardbitmap.htm language=enus -->
## TOPIC 00991: DiscardBitmap

- bundle_id: `labwindows-cvi`
- source_path: `cvi/uiref/cvidiscardbitmap.htm`
- source_url: https://docs-be.ni.com/bundle/labwindows-cvi/raw/resource/enus/cvi/uiref/cvidiscardbitmap.htm
- document_id: `labwindows-cvi`
- page_type: `leaf`
- content_type: ``

### DiscardBitmap

int DiscardBitmap (int bitmapID);

#### Purpose

Discards a bitmap object created using [one of functions that returns a bitmap ID](../../cvi/uiref/cviusing_bitmap_objects.htm).

#### Parameters

| Input |  |  |
| --- | --- | --- |
| Name | Type | Description |
| bitmapID | int | ID of the bitmap object that contains the image. You can obtain the ID from functions such as ClipboardGetBitmap and OGLGetScaledCtrlBitmapOGLGetScaledCtrlBitmap. |

#### Return Value

| Name | Type | Description |
| --- | --- | --- |
| status | int | Return value indicating whether the function was successful. A negative number indicates that an error occurred. |

#### Additional Information

**Library:** [User Interface Library](../../cvi/uiref/cviuser_interface_library_function_tree.htm)

**Include file:** userint.h

**LabWindows/CVI compatibility:** LabWindows/CVI 4.0 and later

#### Examples

Refer to the following examples that use the DiscardBitmap function:

- apps\iconedit\iconedit.cws 
 [IMAGE alt='image' src='open.gif'] Open example
- toolbox\msgdemo.cws 
 [IMAGE alt='image' src='open.gif'] Open example
- userint\ICOViewer.cws 
 [IMAGE alt='image' src='open.gif'] Open example
- userint\imagedit.cws 
 [IMAGE alt='image' src='open.gif'] Open example
- userint\treeimage.cws 
 [IMAGE alt='image' src='open.gif'] Open example
- utility\threading\ThreadPool\ParallelTestInit\ParallelTestInit.cws 
 [IMAGE alt='image' src='open.gif'] Open example

<!--NI_TOPIC bundle=labwindows-cvi path=cvi/uiref/cvidiscardctrl.htm language=enus -->
## TOPIC 00992: DiscardCtrl

- bundle_id: `labwindows-cvi`
- source_path: `cvi/uiref/cvidiscardctrl.htm`
- source_url: https://docs-be.ni.com/bundle/labwindows-cvi/raw/resource/enus/cvi/uiref/cvidiscardctrl.htm
- document_id: `labwindows-cvi`
- page_type: `leaf`
- content_type: ``

### DiscardCtrl

int DiscardCtrl (int panelHandle, int controlID);

#### Purpose

Removes a control from the specified panel and from memory.

You cannot discard a control in the callback function for the control, except
when responding to the [EVENT_COMMIT](../../cvi/uiref/cvieventcommit.htm) event. Discarding the control from its own callback function in response to other events might cause unpredictable behavior.

#### Supported Controls

You can use DiscardCtrl with all LabWindows/CVI [user interface controls](../../cvi/uiref/cvioperating_controls.htm).

#### Parameters

| Input |  |  |
| --- | --- | --- |
| Name | Type | Description |
| panelHandle | int | Specifier for a particular panel that is currently in memory. You can obtain this handle from functions such as LoadPanel and NewPanel. |
| controlID | int | The defined constant, located in the .uir header file, that you assigned to the control in the User Interface Editor, or the ID returned by functions such as NewCtrl and DuplicateCtrl. |

#### Return Value

| Name | Type | Description |
| --- | --- | --- |
| status | int | Return value indicating whether the function was successful. A negative number indicates that an error occurred. |

#### Additional Information

**Library:** [User Interface Library](../../cvi/uiref/cviuser_interface_library_function_tree.htm)

**Include file:** userint.h

**LabWindows/CVI compatibility:** LabWindows/CVI 3.0 and later

<!--NI_TOPIC bundle=labwindows-cvi path=cvi/uiref/cvidiscardctrlarray.htm language=enus -->
## TOPIC 00993: DiscardCtrlArray

- bundle_id: `labwindows-cvi`
- source_path: `cvi/uiref/cvidiscardctrlarray.htm`
- source_url: https://docs-be.ni.com/bundle/labwindows-cvi/raw/resource/enus/cvi/uiref/cvidiscardctrlarray.htm
- document_id: `labwindows-cvi`
- page_type: `leaf`
- content_type: ``

### DiscardCtrlArray

int DiscardCtrlArray (int controlArrayHandle);

#### Purpose

Removes a control array from memory. 
 


This function does not discard the controls from the panel.

#### Parameters

| Input |  |  |
| --- | --- | --- |
| Name | Type | Description |
| controlArrayHandle | int | Specifier for a particular control array that is currently in memory. You obtain this handle from GetCtrlArrayFromResourceID or NewCtrlArray. |

#### Return Value

| Name | Type | Description |
| --- | --- | --- |
| status | int | Return value indicating whether the function was successful. A negative number indicates that an error occurred. |

#### Additional Information

**Library:** [User Interface Library](../../cvi/uiref/cviuser_interface_library_function_tree.htm)

**Include file:** userint.h

**LabWindows/CVI compatibility:** LabWindows/CVI 2010 and later

<!--NI_TOPIC bundle=labwindows-cvi path=cvi/uiref/cvidiscardctrlmenuitem.htm language=enus -->
## TOPIC 00994: DiscardCtrlMenuItem

- bundle_id: `labwindows-cvi`
- source_path: `cvi/uiref/cvidiscardctrlmenuitem.htm`
- source_url: https://docs-be.ni.com/bundle/labwindows-cvi/raw/resource/enus/cvi/uiref/cvidiscardctrlmenuitem.htm
- document_id: `labwindows-cvi`
- page_type: `leaf`
- content_type: ``

### DiscardCtrlMenuItem

int DiscardCtrlMenuItem (int panelHandle, int controlID, int menuItemID);

#### Purpose

Removes a menu item from the menu owned by the specified control.

You cannot remove a built-in menu item. To hide a built-in menu item, use the [HideBuiltInCtrlMenuItem](../../cvi/uiref/cvihidebuiltinctrlmenuitem.htm) function. To delete all user-defined menu items, pass –1 for **menuItemID**.

#### Supported Controls

You can use DiscardCtrlMenuItem with the following controls:

- Tables
- Trees
- Graphs
- Strip charts

#### Parameters

| Input |  |  |
| --- | --- | --- |
| Name | Type | Description |
| panelHandle | int | Specifier for a particular panel that is currently in memory. You can obtain this handle from functions such as LoadPanel and NewPanel. |
| controlID | int | The defined constant, located in the .uir header file, that you assigned to the control in the User Interface Editor, or the ID returned by functions such as NewCtrl and DuplicateCtrl. |
| menuItemID | int | The ID used to reference this menu item. Use a menuItemID you obtained from NewCtrlMenuItem or NewCtrlMenuSeparator. To delete all user-defined menu items, pass –1. |

#### Return Value

| Name | Type | Description |
| --- | --- | --- |
| status | int | Return value indicating whether the function was successful. A negative number indicates that an error occurred. |

#### Additional Information

**Library:** [User Interface Library](../../cvi/uiref/cviuser_interface_library_function_tree.htm)

**Include file:** userint.h

**LabWindows/CVI compatibility:** LabWindows/CVI 5.5 and later

#### Example

Refer to userint\treemenu.cws for an example of using the DiscardCtrlMenuItem function.

<!--NI_TOPIC bundle=labwindows-cvi path=cvi/uiref/cvidiscardmenu.htm language=enus -->
## TOPIC 00995: DiscardMenu

- bundle_id: `labwindows-cvi`
- source_path: `cvi/uiref/cvidiscardmenu.htm`
- source_url: https://docs-be.ni.com/bundle/labwindows-cvi/raw/resource/enus/cvi/uiref/cvidiscardmenu.htm
- document_id: `labwindows-cvi`
- page_type: `leaf`
- content_type: ``

### DiscardMenu

int DiscardMenu (int menuBarHandle, int menuID);

#### Purpose

Removes the specified menu and its submenus and items from a menu bar.

#### Parameters

| Input |  |  |
| --- | --- | --- |
| Name | Type | Description |
| menuBarHandle | int | Specifier for a particular menu bar that is currently in memory. You can obtain this handle from functions such as LoadMenuBar and NewMenuBar. If the menu bar was automatically loaded through LoadPanel, use GetPanelMenuBar to get the menu bar handle. |
| menuID | int | ID for a particular menu within a menu bar. The ID must be a constant name, located in the .uir header file, that you assign in the User Interface Editor or a value that you obtain from functions such as NewMenu and NewSubMenu. |

#### Return Value

| Name | Type | Description |
| --- | --- | --- |
| status | int | Return value indicating whether the function was successful. A negative number indicates that an error occurred. |

#### Additional Information

**Library:** [User Interface Library](../../cvi/uiref/cviuser_interface_library_function_tree.htm)

**Include file:** userint.h

**LabWindows/CVI compatibility:** LabWindows/CVI 3.0 and later

#### Example

Refer to apps\uirview\uirview.cws for an example of using the DiscardMenu function.

<!--NI_TOPIC bundle=labwindows-cvi path=cvi/uiref/cvidiscardmenubar.htm language=enus -->
## TOPIC 00996: DiscardMenuBar

- bundle_id: `labwindows-cvi`
- source_path: `cvi/uiref/cvidiscardmenubar.htm`
- source_url: https://docs-be.ni.com/bundle/labwindows-cvi/raw/resource/enus/cvi/uiref/cvidiscardmenubar.htm
- document_id: `labwindows-cvi`
- page_type: `leaf`
- content_type: ``

### DiscardMenuBar

int DiscardMenuBar (int menuBarHandle);

#### Purpose

Removes a menu bar from every panel on which it resides and from memory.

#### Parameters

| Input |  |  |
| --- | --- | --- |
| Name | Type | Description |
| menuBarHandle | int | Specifier for a particular menu bar that is currently in memory. You can obtain this handle from functions such as LoadMenuBar and NewMenuBar. If the menu bar was automatically loaded through LoadPanel, use GetPanelMenuBar to get the menu bar handle. |

#### Return Value

| Name | Type | Description |
| --- | --- | --- |
| status | int | Return value indicating whether the function was successful. A negative number indicates that an error occurred. |

#### Additional Information

**Library:** [User Interface Library](../../cvi/uiref/cviuser_interface_library_function_tree.htm)

**Include file:** userint.h

**LabWindows/CVI compatibility:** LabWindows/CVI 3.0 and later

#### Examples

Refer to the following examples that use the DiscardMenuBar function:

- apps\uirview\uirview.cws 
 [IMAGE alt='image' src='open.gif'] Open example
- userint\custctrl\toolbar\tooldemo.cws 
 [IMAGE alt='image' src='open.gif'] Open example

<!--NI_TOPIC bundle=labwindows-cvi path=cvi/uiref/cvidiscardmenuitem.htm language=enus -->
## TOPIC 00997: DiscardMenuItem

- bundle_id: `labwindows-cvi`
- source_path: `cvi/uiref/cvidiscardmenuitem.htm`
- source_url: https://docs-be.ni.com/bundle/labwindows-cvi/raw/resource/enus/cvi/uiref/cvidiscardmenuitem.htm
- document_id: `labwindows-cvi`
- page_type: `leaf`
- content_type: ``

### DiscardMenuItem

int DiscardMenuItem (int menuBarHandle, int menuItemID);

#### Purpose

Removes a menu item from the specified menu and from memory.

#### Parameters

| Input |  |  |
| --- | --- | --- |
| Name | Type | Description |
| menuBarHandle | int | Specifier for a particular menu bar that is currently in memory. You can obtain this handle from functions such as LoadMenuBar and NewMenuBar. If the menu bar was automatically loaded through LoadPanel, use GetPanelMenuBar to get the menu bar handle. |
| menuItemID | int | The ID used to reference this menu item. The ID must be a constant name, located in the .uir file, that you assign in the User Interface Editor or a value you obtain from NewMenuItem. |

#### Return Value

| Name | Type | Description |
| --- | --- | --- |
| status | int | Return value indicating whether the function was successful. A negative number indicates that an error occurred. |

#### Additional Information

**Library:** [User Interface Library](../../cvi/uiref/cviuser_interface_library_function_tree.htm)

**Include file:** userint.h

**LabWindows/CVI compatibility:** LabWindows/CVI 3.0 and later

<!--NI_TOPIC bundle=labwindows-cvi path=cvi/uiref/cvidiscardnumericcolorramp.htm language=enus -->
## TOPIC 00998: DiscardNumericColorRamp

- bundle_id: `labwindows-cvi`
- source_path: `cvi/uiref/cvidiscardnumericcolorramp.htm`
- source_url: https://docs-be.ni.com/bundle/labwindows-cvi/raw/resource/enus/cvi/uiref/cvidiscardnumericcolorramp.htm
- document_id: `labwindows-cvi`
- page_type: `leaf`
- content_type: ``

### DiscardNumericColorRamp

int DiscardNumericColorRamp (int panelHandle, int controlID);

#### Purpose

Removes the color ramp from a [numeric slide control](../../cvi/uiref/cvinumeric_slide_control_overview.htm).

|  | Note You can replace a color ramp by calling SetNumericColorRamp without first calling DiscardNumericColorRamp. |
| --- | --- |

#### Supported Controls

You can use DiscardNumericColorRamp with [numeric slide controls](../../cvi/uiref/cviprogramming_with_numeric_slide_controls.htm).

#### Parameters

| Input |  |  |
| --- | --- | --- |
| Name | Type | Description |
| panelHandle | int | Specifier for a particular panel that is currently in memory. You can obtain this handle from functions such as LoadPanel and NewPanel. |
| controlID | int | The defined constant, located in the .uir header file, that you assigned to the control in the User Interface Editor, or the ID returned by functions such as NewCtrl and DuplicateCtrl. |

#### Return Value

| Name | Type | Description |
| --- | --- | --- |
| status | int | Return value indicating whether the function was successful. A negative number indicates that an error occurred. |

#### Additional Information

**Library:** [User Interface Library](../../cvi/uiref/cviuser_interface_library_function_tree.htm)

**Include file:** userint.h

**LabWindows/CVI compatibility:** LabWindows/CVI 8.5 and later

<!--NI_TOPIC bundle=labwindows-cvi path=cvi/uiref/cvidiscardpanel.htm language=enus -->
## TOPIC 00999: DiscardPanel

- bundle_id: `labwindows-cvi`
- source_path: `cvi/uiref/cvidiscardpanel.htm`
- source_url: https://docs-be.ni.com/bundle/labwindows-cvi/raw/resource/enus/cvi/uiref/cvidiscardpanel.htm
- document_id: `labwindows-cvi`
- page_type: `leaf`
- content_type: ``

### DiscardPanel

int DiscardPanel (int panelHandle);

#### Purpose

Removes a panel and any of its child panels from memory and clears them from the screen if visible.

You must call DiscardPanel from the thread in which you create the panel.

Refer to the [LoadPanel](../../cvi/uiref/cviloadpanel.htm) function reference for an example of how to use this and other panel functions.

#### Parameters

| Input |  |  |
| --- | --- | --- |
| Name | Type | Description |
| panelHandle | int | Specifier for a particular panel that is currently in memory. You can obtain this handle from functions such as LoadPanel and NewPanel. |

#### Return Value

| Name | Type | Description |
| --- | --- | --- |
| status | int | Return value indicating whether the function was successful. A negative number indicates that an error occurred. |

#### Additional Information

**Library:** [User Interface Library](../../cvi/uiref/cviuser_interface_library_function_tree.htm)

**Include file:** userint.h

**LabWindows/CVI compatibility:** LabWindows/CVI 3.0 and later

<!--NI_TOPIC bundle=labwindows-cvi path=cvi/uiref/cvidiscardsubmenu.htm language=enus -->
## TOPIC 01000: DiscardSubMenu

- bundle_id: `labwindows-cvi`
- source_path: `cvi/uiref/cvidiscardsubmenu.htm`
- source_url: https://docs-be.ni.com/bundle/labwindows-cvi/raw/resource/enus/cvi/uiref/cvidiscardsubmenu.htm
- document_id: `labwindows-cvi`
- page_type: `leaf`
- content_type: ``

### DiscardSubMenu

int DiscardSubMenu (int menuBarHandle, int subMenuID);

#### Purpose

Removes a submenu from a specified menu bar and from memory.

#### Parameters

| Input |  |  |
| --- | --- | --- |
| Name | Type | Description |
| menuBarHandle | int | Specifier for a particular menu bar that is currently in memory. You can obtain this handle from functions such as LoadMenuBar and NewMenuBar. If the menu bar was automatically loaded through LoadPanel, use GetPanelMenuBar to get the menu bar handle. |
| subMenuID | int | ID for a particular menu item within a menu bar. The ID must be a constant name, located in the .uir file, that you assign in the User Interface Editor or a value you obtain from functions such as NewSubMenu. |

#### Return Value

| Name | Type | Description |
| --- | --- | --- |
| status | int | Return value indicating whether the function was successful. A negative number indicates that an error occurred. |

#### Additional Information

**Library:** [User Interface Library](../../cvi/uiref/cviuser_interface_library_function_tree.htm)

**Include file:** userint.h

**LabWindows/CVI compatibility:** LabWindows/CVI 3.0 and later
