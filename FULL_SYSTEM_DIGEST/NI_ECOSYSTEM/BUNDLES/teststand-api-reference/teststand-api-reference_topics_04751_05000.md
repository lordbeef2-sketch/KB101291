# NI DOCUMENT BUNDLE: teststand-api-reference

<!--NI_BUNDLE_CHUNK bundle=teststand-api-reference start=4751 end=5000 -->
<!--NI_TOPIC bundle=teststand-api-reference path=tsuiref/button-font.html language=enus -->
## TOPIC 04751: Button.Font

- bundle_id: `teststand-api-reference`
- source_path: `tsuiref/button-font.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsuiref/button-font.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax Button.Font Data Type Font Purpose Specifies the font for the control when the value of the Button.FontSource property is FontSource_UseFontProperty . See Also Button.FontSource

### Button.Font

#### Syntax

[Button](button.html).Font

#### Data Type

[Font](data-types-for-teststand-user-interface.html)

#### Purpose

Specifies the font for the control when the value of the
 [Button.FontSource](button-fontsource.html)
 property is
 FontSource_UseFontProperty
 .

#### See Also

[Button.FontSource](button-fontsource.html)

Parent topic:

Properties

<!--NI_TOPIC bundle=teststand-api-reference path=tsuiref/button-fontsource.html language=enus -->
## TOPIC 04752: Button.FontSource

- bundle_id: `teststand-api-reference`
- source_path: `tsuiref/button-fontsource.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsuiref/button-fontsource.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax Button.FontSource Data Type FontSources Use the following constants with this data type: FontSource_UseContainerFont –(Value: 2) The font the container supplies. FontSource_UseFontProperty –(Value: 0) A corresponding Font property of the control determines the font. FontSource_UseGUIFont –(Va

### Button.FontSource

#### Syntax

[Button](button.html).FontSource

#### Data Type

[FontSources](fontsources.html)

Use the following constants with this data type:

- FontSource_UseContainerFont 
 –(Value: 2) The font the container supplies.
- FontSource_UseFontProperty 
 –(Value: 0) A corresponding
 Font 
 property of the control determines the font.
- FontSource_UseGUIFont 
 –(Value: 1) The default system font for user interface objects.
- FontSource_UseIconFont 
 –(Value: 5) The system font for an icon title.
- FontSource_UseInactiveTitlebarFont 
 –(Value: 4) The system font for an inactive titlebar.
- FontSource_UseMenuFont 
 –(Value: 6) The system font for a menu.
- FontSource_UseMessageBoxFont 
 –(Value: 7) The system font for a message box.
- FontSource_UsePaletteTitleFont 
 –(Value: 8) The system font for the title of a Tools window.
- FontSource_UseSelectedItemsFont 
 –(Value: 9) The system font for the selected menu items.
- FontSource_UseSystemFixedWidthFont 
 –(Value: 11) The system font for monospaced text.
- FontSource_UseTitlebarFont 
 –(Value: 3) The system font for a title bar.
- FontSource_UseToolTipFont 
 –(Value: 10) The system font for tooltips and status bars.
- FontSource_UseUIStyleFont 
 –(Value: 12) The font the
 UIStyle 
 object supplies.

#### Purpose

Specifies the font the control uses. The default value for this property is
 FontSource_UseGUIFont
 .

#### Remarks

When the value of this property is
 FontSource_UseFontProperty
 , the corresponding
 Font
 property specifies the particular font the control uses. Otherwise, the control uses the font from the source this property specifies. Refer to the
 [FontSources](fontsources.html)
 enumeration for the list of valid font sources.

Set this property to a value other than
 FontSource_UseFontProperty
 when you expect the font the
 [Button.Font](button-font.html)
 property specifies to not be present on a computer at run time. For example, a font present on an English version of the Microsoft Windows operating system might not be present on a Japanese version of the Windows operating system.

#### See Also

[Button.Font](button-font.html)

[FontSources](fontsources.html)

Parent topic:

Properties

<!--NI_TOPIC bundle=teststand-api-reference path=tsuiref/button-forecolor.html language=enus -->
## TOPIC 04753: Button.ForeColor

- bundle_id: `teststand-api-reference`
- source_path: `tsuiref/button-forecolor.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsuiref/button-forecolor.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax Button.ForeColor Data Type Color Purpose Specifies the text color for the Button control. Remarks Use the Button.BackColor property to change the face and border color of the control. See Also Button.BackColor

### Button.ForeColor

#### Syntax

[Button](button.html).ForeColor

#### Data Type

[Color](data-types-for-teststand-user-interface.html)

#### Purpose

Specifies the text color for the Button control.

#### Remarks

Use the
 [Button.BackColor](button-backcolor.html)
 property to change the face and border color of the control.

#### See Also

[Button.BackColor](button-backcolor.html)

Parent topic:

Properties

<!--NI_TOPIC bundle=teststand-api-reference path=tsuiref/button-hwnd.html language=enus -->
## TOPIC 04754: Button.hWnd

- bundle_id: `teststand-api-reference`
- source_path: `tsuiref/button-hwnd.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsuiref/button-hwnd.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax Button.hWnd Data Type Long Purpose Returns a Window handle for the control. Remarks You can use the returned Window handle with the Microsoft Windows API functions. Using Windows API functions with this property can cause undefined behavior.

### Button.hWnd

#### Syntax

[Button](button.html).hWnd

#### Data Type

[Long](data-types-for-teststand-user-interface.html)

#### Purpose

Returns a Window handle for the control.

#### Remarks

You can use the returned Window handle with the Microsoft Windows API functions.

Note

Parent topic:

Properties

<!--NI_TOPIC bundle=teststand-api-reference path=tsuiref/button-image.html language=enus -->
## TOPIC 04755: Button.Image

- bundle_id: `teststand-api-reference`
- source_path: `tsuiref/button-image.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsuiref/button-image.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax Button.Image Data Type Picture Purpose Specifies a custom graphic for the Button control. Remarks Use the Engine.Images property to obtain the TestStand images collection, and use the Images.FindImage method to obtain a particular image reference. Icon files are located in the <TestStand> \Co

### Button.Image

#### Syntax

[Button](button.html).Image

#### Data Type

[Picture](data-types-for-teststand-user-interface.html)

#### Purpose

Specifies a custom graphic for the Button control.

#### Remarks

Use the
 
 [Engine.Images](../tsapiref/engine-images.html)
 property to obtain the TestStand images collection, and use the
 
 [Images.FindImage](../tsapiref/images-findimage.html)
 method to obtain a particular image reference. Icon files are located in the
 [<TestStand>](/csh?context=ts_tsfundamentals_directories)
 \Components\Icons
 and
 <TestStand Public>\Components\Icons
 directories.

#### See Also

[Button.BackColor](button-backcolor.html)

[Button.ImageAlignment](button-imagealignment.html)

[Engine.Images](../tsapiref/engine-images.html)

[Images.FindImage](../tsapiref/images-findimage.html)

Parent topic:

Properties

<!--NI_TOPIC bundle=teststand-api-reference path=tsuiref/button-imagealignment.html language=enus -->
## TOPIC 04756: Button.ImageAlignment

- bundle_id: `teststand-api-reference`
- source_path: `tsuiref/button-imagealignment.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsuiref/button-imagealignment.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax Button.ImageAlignment Data Type ContentAlignmentStyles Use the following constants with this data type: ContentAlignmentStyle_BottomCenter –(Value: 8) Content is vertically aligned at the bottom and horizontally aligned in the center. ContentAlignmentStyle_BottomLeft –(Value: 6) Content is ve

### Button.ImageAlignment

#### Syntax

[Button](button.html).ImageAlignment

#### Data Type

[ContentAlignmentStyles](contentalignmentstyles.html)

Use the following constants with this data type:

- ContentAlignmentStyle_BottomCenter 
 –(Value: 8) Content is vertically aligned at the bottom and horizontally aligned in the center.
- ContentAlignmentStyle_BottomLeft 
 –(Value: 6) Content is vertically aligned at the bottom and horizontally aligned on the left.
- ContentAlignmentStyle_BottomRight 
 –(Value: 7) Content is vertically aligned at the bottom and horizontally aligned on the right.
- ContentAlignmentStyle_MiddleCenter 
 –(Value: 2) Content is vertically aligned in the middle and horizontally aligned in the center.
- ContentAlignmentStyle_MiddleLeft 
 –(Value: 0) Content is vertically aligned in the middle and horizontally aligned on the left.
- ContentAlignmentStyle_MiddleRight 
 –(Value: 1) Content is vertically aligned in the middle and horizontally aligned on the right.
- ContentAlignmentStyle_TopCenter 
 –(Value: 5) Content is vertically aligned at the top and horizontally aligned in the center.
- ContentAlignmentStyle_TopLeft 
 –(Value: 3) Content is vertically aligned at the top and horizontally aligned on the left.
- ContentAlignmentStyle_TopRight 
 –(Value: 4) Content is vertically aligned at the top and horizontally aligned on the right.

#### Purpose

Specifies the horizontal and vertical alignment of an image on a Button control.

#### See Also

[Button.Image](button-image.html)

[Button.ShowImage](button-showimage.html)

[Button.TextAlignment](button-textalignment.html)

[Button.TextImageRelation](button-textimagerelation.html)

Parent topic:

Properties

<!--NI_TOPIC bundle=teststand-api-reference path=tsuiref/button-keydown.html language=enus -->
## TOPIC 04757: Button.KeyDown

- bundle_id: `teststand-api-reference`
- source_path: `tsuiref/button-keydown.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsuiref/button-keydown.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax ControlName_KeyDown( keyCode, shift) Applies To Button Purpose Occurs when the user presses a key while the control has the input focus. This event occurs before the Button.KeyPress event. Parameters keyCode As Integer [In/Out] Specifies the KeyCodes constant of the key the user pressed. shif

### Button.KeyDown

#### Syntax

ControlName_KeyDown( keyCode, shift)

#### Applies To

[Button](button.html)

#### Purpose

Occurs when the user presses a key while the control has the input focus. This event occurs before the
 [Button.KeyPress](button-keypress.html)
 event.

#### Parameters

keyCode
 As
 [Integer](data-types-for-teststand-user-interface.html)

[In/Out] Specifies the
 [KeyCodes](keycodes.html)
 constant of the key the user pressed.

shift
 As
 [Integer](data-types-for-teststand-user-interface.html)

[In] Specifies a combination of the
 [KeyModifiers](keymodifiers.html)
 constants that specifies the state of the <Shift>, <Ctrl>, and <Alt> keys.

#### See Also

[Button.KeyPress](button-keypress.html)

[Button.KeyUp](button-keyup.html)

[KeyCodes](keycodes.html)

[KeyModifiers](keymodifiers.html)

Parent topic:

Events

<!--NI_TOPIC bundle=teststand-api-reference path=tsuiref/button-keypress.html language=enus -->
## TOPIC 04758: Button.KeyPress

- bundle_id: `teststand-api-reference`
- source_path: `tsuiref/button-keypress.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsuiref/button-keypress.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax ControlName_KeyPress( keyAscii) Applies To Button Purpose Occurs when the user presses a key while the control has the input focus. This event occurs after the Button.KeyDown event. Parameters keyAscii As Integer [In/Out] Specifies the ASCII value of the pressed key. See Also Button.KeyDown B

### Button.KeyPress

#### Syntax

ControlName_KeyPress( keyAscii)

#### Applies To

[Button](button.html)

#### Purpose

Occurs when the user presses a key while the control has the input focus. This event occurs after the
 [Button.KeyDown](button-keydown.html)
 event.

#### Parameters

keyAscii
 As
 [Integer](data-types-for-teststand-user-interface.html)

[In/Out] Specifies the ASCII value of the pressed key.

#### See Also

[Button.KeyDown](button-keydown.html)

[Button.KeyUp](button-keyup.html)

Parent topic:

Events

<!--NI_TOPIC bundle=teststand-api-reference path=tsuiref/button-keyup.html language=enus -->
## TOPIC 04759: Button.KeyUp

- bundle_id: `teststand-api-reference`
- source_path: `tsuiref/button-keyup.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsuiref/button-keyup.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax ControlName_KeyUp( keyCode, shift) Applies To Button Purpose Occurs when the user releases a key while the control has the input focus. Parameters keyCode As Integer [In] Specifies the KeyCodes constant of the key the user pressed. shift As Integer [In] Specifies a combination of the KeyModif

### Button.KeyUp

#### Syntax

ControlName_KeyUp( keyCode, shift)

#### Applies To

[Button](button.html)

#### Purpose

Occurs when the user releases a key while the control has the input focus.

#### Parameters

keyCode
 As
 [Integer](data-types-for-teststand-user-interface.html)

[In] Specifies the
 [KeyCodes](keycodes.html)
 constant of the key the user pressed.

shift
 As
 [Integer](data-types-for-teststand-user-interface.html)

[In] Specifies a combination of the
 [KeyModifiers](keymodifiers.html)
 constants that specifies the state of the <Shift>, <Ctrl>, and <Alt> keys.

#### See Also

[Button.KeyDown](button-keydown.html)

[Button.KeyPress](button-keypress.html)

[KeyCodes](keycodes.html)

[KeyModifiers](keymodifiers.html)

Parent topic:

Events

<!--NI_TOPIC bundle=teststand-api-reference path=tsuiref/button-localize.html language=enus -->
## TOPIC 04760: Button.Localize

- bundle_id: `teststand-api-reference`
- source_path: `tsuiref/button-localize.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsuiref/button-localize.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax Button.Localize( sectionName) Purpose Localizes the text caption on the button in this control. Remarks First, update a .ini file located in the TestStand Language directory with the required string. Second, use the string tag in the .ini file as the caption for the control. When you call thi

### Button.Localize

#### Syntax

[Button](button.html).Localize( sectionName)

#### Purpose

Localizes the text caption on the button in this control.

#### Remarks

First, update a
 .ini
 file located in the TestStand
 Language
 directory with the required string. Second, use the string tag in the
 .ini
 file as the caption for the control.

When you call this method, the control replaces the caption with the string from the
 .ini
 file. If the caption is not a tag in the
 .ini
 file, the caption does not change.

Note

#### Parameters

sectionName
 As
 [String](data-types-for-teststand-user-interface.html)

[In] Specifies the name of the section in the language files that contains the localized text.

#### See Also

[ApplicationMgr.LocalizeAllControls](applicationmgr-localizeallcontrols.html)

Parent topic:

Methods

<!--NI_TOPIC bundle=teststand-api-reference path=tsuiref/button-maskcolor.html language=enus -->
## TOPIC 04761: Button.MaskColor

- bundle_id: `teststand-api-reference`
- source_path: `tsuiref/button-maskcolor.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsuiref/button-maskcolor.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax Button.MaskColor Data Type Color Purpose Specifies a color in the picture of the control to use as a mask color when the Button.UseMaskColor property is True . You can use the mask color to create transparent regions. Remarks This property is used only when the button displays an image. See A

### Button.MaskColor

#### Syntax

[Button](button.html).MaskColor

#### Data Type

[Color](data-types-for-teststand-user-interface.html)

#### Purpose

Specifies a color in the picture of the control to use as a mask color when the
 [Button.UseMaskColor](button-usemaskcolor.html)
 property is
 True
 . You can use the mask color to create transparent regions.

#### Remarks

This property is used only when the button displays an image.

#### See Also

[Button.ShowImage](button-showimage.html)

[Button.UseMaskColor](button-usemaskcolor.html)

Parent topic:

Properties

<!--NI_TOPIC bundle=teststand-api-reference path=tsuiref/button-mousedown.html language=enus -->
## TOPIC 04762: Button.MouseDown

- bundle_id: `teststand-api-reference`
- source_path: `tsuiref/button-mousedown.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsuiref/button-mousedown.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax ControlName_MouseDown( btn, shift, x, y) Applies To Button Purpose Occurs when the user clicks the mouse on the control. This event occurs before the Button.MouseUp event. Parameters btn As Integer [In] Specifies a MouseButtons constant that specifies the mouse button the user pressed to gene

### Button.MouseDown

#### Syntax

ControlName_MouseDown( btn, shift, x, y)

#### Applies To

[Button](button.html)

#### Purpose

Occurs when the user clicks the mouse on the control. This event occurs before the
 [Button.MouseUp](button-mouseup.html)
 event.

#### Parameters

btn
 As
 [Integer](data-types-for-teststand-user-interface.html)

[In] Specifies a
 [MouseButtons](mousebuttons.html)
 constant that specifies the mouse button the user pressed to generate this event.

shift
 As
 [Integer](data-types-for-teststand-user-interface.html)

[In] Specifies a combination of the
 [KeyModifiers](keymodifiers.html)
 constants that specifies the state of the <Shift>, <Ctrl>, and <Alt> keys.

x
 As
 [long](data-types-for-teststand-user-interface.html)

[In] Specifies the x-coordinate of the mouse pointer, relative to the control, at the moment when the event occurs.

y
 As
 [long](data-types-for-teststand-user-interface.html)

[In] Specifies the y-coordinate of the mouse pointer, relative to the control, at the moment when the event occurs.

#### See Also

[Button.Click](button-click.html)

[Button.MouseMove](button-mousemove.html)

[Button.MouseUp](button-mouseup.html)

[KeyModifiers](keymodifiers.html)

[MouseButtons](mousebuttons.html)

Parent topic:

Events

<!--NI_TOPIC bundle=teststand-api-reference path=tsuiref/button-mouseicon.html language=enus -->
## TOPIC 04763: Button.MouseIcon

- bundle_id: `teststand-api-reference`
- source_path: `tsuiref/button-mouseicon.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsuiref/button-mouseicon.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax Button.MouseIcon Data Type Picture Purpose Specifies the custom mouse icon for the control. Remarks The control displays the specified picture as the cursor when the value of the Button.MousePointer property is MousePointer_Custom . When you set this property to NULL , the value of the Button

### Button.MouseIcon

#### Syntax

[Button](button.html).MouseIcon

#### Data Type

[Picture](data-types-for-teststand-user-interface.html)

#### Purpose

Specifies the custom mouse icon for the control.

#### Remarks

The control displays the specified picture as the cursor when the value of the
 [Button.MousePointer](button-mousepointer.html)
 property is
 MousePointer_Custom
 . When you set this property to
 NULL
 , the value of the
 Button.MousePointer
 property changes to
 MousePointer_Default
 .

Note

#### See Also

[Button.MousePointer](button-mousepointer.html)

Parent topic:

Properties

<!--NI_TOPIC bundle=teststand-api-reference path=tsuiref/button-mousemove.html language=enus -->
## TOPIC 04764: Button.MouseMove

- bundle_id: `teststand-api-reference`
- source_path: `tsuiref/button-mousemove.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsuiref/button-mousemove.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax ControlName_MouseMove( btn, shift, x, y) Applies To Button Purpose Occurs when the user moves the mouse over the control. Parameters btn As Integer [In] Specifies what mouse buttons are pressed. You can use any combination of the MouseButtons constants. shift As Integer [In] Specifies a combi

### Button.MouseMove

#### Syntax

ControlName_MouseMove( btn, shift, x, y)

#### Applies To

[Button](button.html)

#### Purpose

Occurs when the user moves the mouse over the control.

#### Parameters

btn
 As
 [Integer](data-types-for-teststand-user-interface.html)

[In] Specifies what mouse buttons are pressed. You can use any combination of the
 [MouseButtons](mousebuttons.html)
 constants.

shift
 As
 [Integer](data-types-for-teststand-user-interface.html)

[In] Specifies a combination of the
 [KeyModifiers](keymodifiers.html)
 constants that specifies the state of the <Shift>, <Ctrl>, and <Alt> keys.

x
 As
 [long](data-types-for-teststand-user-interface.html)

[In] Specifies the x-coordinate of the mouse pointer, relative to the control, at the moment when the event occurs.

y
 As
 [long](data-types-for-teststand-user-interface.html)

[In] Specifies the y-coordinate of the mouse pointer, relative to the control, at the moment when the event occurs.

#### See Also

[Button.Click](button-click.html)

[Button.MouseDown](button-mousedown.html)

[Button.MouseUp](button-mouseup.html)

[KeyModifiers](keymodifiers.html)

[MouseButtons](mousebuttons.html)

Parent topic:

Events

<!--NI_TOPIC bundle=teststand-api-reference path=tsuiref/button-mousepointer.html language=enus -->
## TOPIC 04765: Button.MousePointer

- bundle_id: `teststand-api-reference`
- source_path: `tsuiref/button-mousepointer.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsuiref/button-mousepointer.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax Button.MousePointer Data Type MousePointerStyles Use the following constants with this data type: MousePointer_Arrow –(Value: 1) MousePointer_ArrowHourGlass –(Value: 11) MousePointer_ArrowQuestion –(Value: 12) MousePointer_Crosshair –(Value: 2) MousePointer_Custom –(Value: 99) MousePointer_De

### Button.MousePointer

#### Syntax

[Button](button.html).MousePointer

#### Data Type

[MousePointerStyles](mousepointerstyles.html)

Use the following constants with this data type:

- MousePointer_Arrow 
 –(Value: 1)
- MousePointer_ArrowHourGlass 
 –(Value: 11)
- MousePointer_ArrowQuestion 
 –(Value: 12)
- MousePointer_Crosshair 
 –(Value: 2)
- MousePointer_Custom 
 –(Value: 99)
- MousePointer_Default 
 –(Value: 0)
- MousePointer_HourGlass 
 –(Value: 9)
- MousePointer_Ibeam 
 –(Value: 3)
- MousePointer_NoDrop 
 –(Value: 10)
- MousePointer_SizeAll 
 –(Value: 13)
- MousePointer_SizeNESW 
 –(Value: 4)
- MousePointer_SizeNS 
 –(Value: 5)
- MousePointer_SizeNWSE 
 –(Value: 6)
- MousePointer_SizeWE 
 –(Value: 7)
- MousePointer_UpArrow 
 –(Value: 8)

#### Purpose

Specifies the appearance of the mouse cursor when the cursor is over the control.

#### Remarks

When the parameter is
 MousePointer_Custom
 , the mouse cursor is the picture the
 [Button.MouseIcon](button-mouseicon.html)
 property specifies.

#### See Also

[Button.MouseIcon](button-mouseicon.html)

Parent topic:

Properties

<!--NI_TOPIC bundle=teststand-api-reference path=tsuiref/button-mouseup.html language=enus -->
## TOPIC 04766: Button.MouseUp

- bundle_id: `teststand-api-reference`
- source_path: `tsuiref/button-mouseup.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsuiref/button-mouseup.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax ControlName_MouseUp( btn, shift, x, y) Applies To Button Purpose Occurs when the user releases the mouse button on the control. This event occurs before the Button.Click event. Parameters btn As Integer [In] Specifies the mouse button pressed to cause this event. You can use any one of the Mo

### Button.MouseUp

#### Syntax

ControlName_MouseUp( btn, shift, x, y)

#### Applies To

[Button](button.html)

#### Purpose

Occurs when the user releases the mouse button on the control. This event occurs before the
 [Button.Click](button-click.html)
 event.

#### Parameters

btn
 As
 [Integer](data-types-for-teststand-user-interface.html)

[In] Specifies the mouse button pressed to cause this event. You can use any one of the
 [MouseButtons](mousebuttons.html)
 constants.

shift
 As
 [Integer](data-types-for-teststand-user-interface.html)

[In] Specifies a combination of the
 [KeyModifiers](keymodifiers.html)
 constants that specifies the state of the <Shift>, <Ctrl>, and <Alt> keys.

x
 As
 [long](data-types-for-teststand-user-interface.html)

[In] Specifies the x-coordinate of the mouse pointer, relative to the control, at the moment when the event occurs.

y
 As
 [long](data-types-for-teststand-user-interface.html)

[In] Specifies the y-coordinate of the mouse pointer, relative to the control, at the moment when the event occurs.

#### See Also

[Button.Click](button-click.html)

[Button.MouseDown](button-mousedown.html)

[Button.MouseMove](button-mousemove.html)

[KeyModifiers](keymodifiers.html)

[MouseButtons](mousebuttons.html)

Parent topic:

Events

<!--NI_TOPIC bundle=teststand-api-reference path=tsuiref/button-scalewithdpi.html language=enus -->
## TOPIC 04767: Button.ScaleWithDPI

- bundle_id: `teststand-api-reference`
- source_path: `tsuiref/button-scalewithdpi.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsuiref/button-scalewithdpi.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax Button.ScaleWithDPI Data Type Boolean Purpose Specifies how the control scales based on the dots per inch (DPI) setting. Remarks Some environments scale native controls based on the DPI settings of their display, while other environments do not. The TestStand User Interface Controls are desig

### Button.ScaleWithDPI

#### Syntax

[Button](button.html).ScaleWithDPI

#### Data Type

[Boolean](data-types-for-teststand-user-interface.html)

#### Purpose

Specifies how the control scales based on the dots per inch (DPI) setting.

#### Remarks

Some environments scale native controls based on the DPI settings of their display, while other environments do not. The TestStand User Interface Controls are designed to work in all environments.

The following are the recommended settings for various platforms:

- LabVIEW, LabWindows/CVI, C#, and Microsoft Visual Basic .NET—Set this property to
 False 
 .
- Active Template Library (ATL)/Microsoft Foundation Class (MFC)—Set this property to
 True 
 .

Parent topic:

Properties

<!--NI_TOPIC bundle=teststand-api-reference path=tsuiref/button-showimage.html language=enus -->
## TOPIC 04768: Button.ShowImage

- bundle_id: `teststand-api-reference`
- source_path: `tsuiref/button-showimage.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsuiref/button-showimage.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax Button.ShowImage Data Type Boolean Purpose Specifies whether the button displays an image. See Also Button.Image Button.ShowText

### Button.ShowImage

#### Syntax

[Button](button.html).ShowImage

#### Data Type

[Boolean](data-types-for-teststand-user-interface.html)

#### Purpose

Specifies whether the button displays an image.

#### See Also

[Button.Image](button-image.html)

[Button.ShowText](button-showtext.html)

Parent topic:

Properties

<!--NI_TOPIC bundle=teststand-api-reference path=tsuiref/button-showtext.html language=enus -->
## TOPIC 04769: Button.ShowText

- bundle_id: `teststand-api-reference`
- source_path: `tsuiref/button-showtext.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsuiref/button-showtext.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax Button.ShowText Data Type Boolean Purpose Specifies whether the button displays a text label. See Also Button.Caption Button.ShowImage

### Button.ShowText

#### Syntax

[Button](button.html).ShowText

#### Data Type

[Boolean](data-types-for-teststand-user-interface.html)

#### Purpose

Specifies whether the button displays a text label.

#### See Also

[Button.Caption](button-caption.html)

[Button.ShowImage](button-showimage.html)

Parent topic:

Properties

<!--NI_TOPIC bundle=teststand-api-reference path=tsuiref/button-style.html language=enus -->
## TOPIC 04770: Button.Style

- bundle_id: `teststand-api-reference`
- source_path: `tsuiref/button-style.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsuiref/button-style.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax Button.Style Data Type ButtonStyles Use the following constants with this data type: ButtonStyle_Standard –(Value: 1) The button displays a three-dimensional border. ButtonStyle_ToolBar –(Value: 2) You cannot tab to the button. When the application supports Microsoft Windows XP themes, the bu

### Button.Style

#### Syntax

[Button](button.html).Style

#### Data Type

[ButtonStyles](buttonstyles.html)

Use the following constants with this data type:

- ButtonStyle_Standard 
 –(Value: 1) The button displays a three-dimensional border.
- ButtonStyle_ToolBar 
 –(Value: 2) You cannot tab to the button. When the application supports Microsoft Windows XP themes, the button displays a border only when you hover over it.

#### Purpose

Specifies the appearance of the Button control.

#### See Also

[Button.ActionStyle](button-actionstyle.html)

Parent topic:

Properties

<!--NI_TOPIC bundle=teststand-api-reference path=tsuiref/button-textalignment.html language=enus -->
## TOPIC 04771: Button.TextAlignment

- bundle_id: `teststand-api-reference`
- source_path: `tsuiref/button-textalignment.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsuiref/button-textalignment.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax Button.TextAlignment Data Type ContentAlignmentStyles Use the following constants with this data type: ContentAlignmentStyle_BottomCenter –(Value: 8) Content is vertically aligned at the bottom and horizontally aligned in the center. ContentAlignmentStyle_BottomLeft –(Value: 6) Content is ver

### Button.TextAlignment

#### Syntax

[Button](button.html).TextAlignment

#### Data Type

[ContentAlignmentStyles](contentalignmentstyles.html)

Use the following constants with this data type:

- ContentAlignmentStyle_BottomCenter 
 –(Value: 8) Content is vertically aligned at the bottom and horizontally aligned in the center.
- ContentAlignmentStyle_BottomLeft 
 –(Value: 6) Content is vertically aligned at the bottom and horizontally aligned on the left.
- ContentAlignmentStyle_BottomRight 
 –(Value: 7) Content is vertically aligned at the bottom and horizontally aligned on the right.
- ContentAlignmentStyle_MiddleCenter 
 –(Value: 2) Content is vertically aligned in the middle and horizontally aligned in the center.
- ContentAlignmentStyle_MiddleLeft 
 –(Value: 0) Content is vertically aligned in the middle and horizontally aligned on the left.
- ContentAlignmentStyle_MiddleRight 
 –(Value: 1) Content is vertically aligned in the middle and horizontally aligned on the right.
- ContentAlignmentStyle_TopCenter 
 –(Value: 5) Content is vertically aligned at the top and horizontally aligned in the center.
- ContentAlignmentStyle_TopLeft 
 –(Value: 3) Content is vertically aligned at the top and horizontally aligned on the left.
- ContentAlignmentStyle_TopRight 
 –(Value: 4) Content is vertically aligned at the top and horizontally aligned on the right.

#### Purpose

Specifies the horizontal and vertical alignment of text on a Button control.

#### See Also

[Button.Caption](button-caption.html)

[Button.ImageAlignment](button-imagealignment.html)

[Button.ShowText](button-showtext.html)

[Button.TextImageRelation](button-textimagerelation.html)

Parent topic:

Properties

<!--NI_TOPIC bundle=teststand-api-reference path=tsuiref/button-textimagerelation.html language=enus -->
## TOPIC 04772: Button.TextImageRelation

- bundle_id: `teststand-api-reference`
- source_path: `tsuiref/button-textimagerelation.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsuiref/button-textimagerelation.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax Button.TextImageRelation Data Type TextImageRelations Use the following constants with this data type: TextImageRelation_ImageAboveText –(Value: 2) Displays the image above the text. TextImageRelation_ImageAfterText –(Value: 4) Displays the image to the right of the text. TextImageRelation_Im

### Button.TextImageRelation

#### Syntax

[Button](button.html).TextImageRelation

#### Data Type

[TextImageRelations](textimagerelations.html)

Use the following constants with this data type:

- TextImageRelation_ImageAboveText 
 –(Value: 2) Displays the image above the text.
- TextImageRelation_ImageAfterText 
 –(Value: 4) Displays the image to the right of the text.
- TextImageRelation_ImageBeforeText 
 –(Value: 3) Displays the image to the left of the text.
- TextImageRelation_ImageBelowText 
 –(Value: 1) Displays the image below the text.
- TextImageRelation_Overlay 
 –(Value: 0) Displays the image behind the text.

#### Purpose

Specifies how to display the image in relation to the text on the Button control.

#### Remarks

This property has an effect only when the
 [Button.ImageAlignment](button-imagealignment.html)
 and
 [Button.TextAlignment](button-textalignment.html)
 properties are set to the same value. When the values are different, TestStand ignores the
 Button.TextImageRelation
 property.

#### See Also

[Button.ImageAlignment](button-imagealignment.html)

[Button.ShowImage](button-showimage.html)

[Button.ShowText](button-showtext.html)

[Button.TextAlignment](button-textalignment.html)

Parent topic:

Properties

<!--NI_TOPIC bundle=teststand-api-reference path=tsuiref/button-tooltiptext.html language=enus -->
## TOPIC 04773: Button.ToolTipText

- bundle_id: `teststand-api-reference`
- source_path: `tsuiref/button-tooltiptext.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsuiref/button-tooltiptext.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax Button.ToolTipText Data Type String Purpose Specifies the tooltip for the Button control. When this property is an empty string, the Button control uses the Button.Caption property for the tooltip. See Also Button.Caption

### Button.ToolTipText

#### Syntax

[Button](button.html).ToolTipText

#### Data Type

[String](data-types-for-teststand-user-interface.html)

#### Purpose

Specifies the tooltip for the Button control. When this property is an empty string, the Button control uses the
 [Button.Caption](button-caption.html)
 property for the tooltip.

#### See Also

[Button.Caption](button-caption.html)

Parent topic:

Properties

<!--NI_TOPIC bundle=teststand-api-reference path=tsuiref/button-usemaskcolor.html language=enus -->
## TOPIC 04774: Button.UseMaskColor

- bundle_id: `teststand-api-reference`
- source_path: `tsuiref/button-usemaskcolor.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsuiref/button-usemaskcolor.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax Button.UseMaskColor Data Type Boolean Purpose The control uses the color the Button.MaskColor property specifies as a mask color when this property is True . You can use the mask color to create transparent regions. Remarks This property is used only when the button displays an image. See Als

### Button.UseMaskColor

#### Syntax

[Button](button.html).UseMaskColor

#### Data Type

[Boolean](data-types-for-teststand-user-interface.html)

#### Purpose

The control uses the color the
 [Button.MaskColor](button-maskcolor.html)
 property specifies as a mask color when this property is
 True
 . You can use the mask color to create transparent regions.

#### Remarks

This property is used only when the button displays an image.

#### See Also

[Button.MaskColor](button-maskcolor.html)

[Button.ShowImage](button-showimage.html)

Parent topic:

Properties

<!--NI_TOPIC bundle=teststand-api-reference path=tsuiref/button-usemnemonic.html language=enus -->
## TOPIC 04775: Button.UseMnemonic

- bundle_id: `teststand-api-reference`
- source_path: `tsuiref/button-usemnemonic.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsuiref/button-usemnemonic.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax Button.UseMnemonic Data Type Boolean Purpose The button interprets the character that follows an ampersand ( & ) character in the Button.Caption property as an accelerator character when this property is True . See Also Button.Caption

### Button.UseMnemonic

#### Syntax

[Button](button.html).UseMnemonic

#### Data Type

[Boolean](data-types-for-teststand-user-interface.html)

#### Purpose

The button interprets the character that follows an ampersand (
 &
 ) character in the
 [Button.Caption](button-caption.html)
 property as an accelerator character when this property is
 True
 .

#### See Also

[Button.Caption](button-caption.html)

Parent topic:

Properties

<!--NI_TOPIC bundle=teststand-api-reference path=tsuiref/button-value.html language=enus -->
## TOPIC 04776: Button.Value

- bundle_id: `teststand-api-reference`
- source_path: `tsuiref/button-value.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsuiref/button-value.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax Button.Value Data Type Boolean Purpose This property is True when the button is pressed and False when the button is not pressed. Use this property when the value of the ButtonActionStyles enumeration is ButtonActionStyle_ToggleButton to set the pressed state of the button. Remarks Setting th

### Button.Value

#### Syntax

[Button](button.html).Value

#### Data Type

[Boolean](data-types-for-teststand-user-interface.html)

#### Purpose

This property is
 True
 when the button is pressed and
 False
 when the button is not pressed. Use this property when the value of the
 [ButtonActionStyles](buttonactionstyles.html)
 enumeration is
 ButtonActionStyle_ToggleButton
 to set the pressed state of the button.

#### Remarks

Setting this property generates a
 [Button.Click](button-click.html)
 event.

Note

#### See Also

[Button.Click](button-click.html)

[Button.DoClick](button-doclick.html)

[ButtonActionStyles](buttonactionstyles.html)

Parent topic:

Properties

<!--NI_TOPIC bundle=teststand-api-reference path=tsuiref/button.html language=enus -->
## TOPIC 04777: Button

- bundle_id: `teststand-api-reference`
- source_path: `tsuiref/button.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsuiref/button.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Connect a manager control to a Button control to specify that the button performs a common user interface command, such as Open Sequence File . The Button control uses a localized caption and automatically enables or disables depending on the application state. Properties ActionStyle AutoSizing Back

### Button

Connect a manager control to a Button control to specify that the button performs a common user interface command, such as
 Open Sequence File
 . The Button control uses a localized caption and automatically enables or disables depending on the application state.

#### Properties

| ActionStyle |
| --- |
| AutoSizing |
| BackColor |
| Caption |
| Enabled |
| Font |
| FontSource |
| ForeColor |
| hWnd (Read Only) |
| Image |
| ImageAlignment |
| MaskColor |
| MouseIcon |
| MousePointer |
| ScaleWithDPI |
| ShowImage |
| ShowText |
| Style |
| TextAlignment |
| TextImageRelation |
| ToolTipText |
| UseMaskColor |
| UseMnemonic |
| Value |

#### Methods

| DoClick |
| --- |
| Localize |

#### Events

| Click |
| --- |
| ConnectionActivity |
| KeyDown |
| KeyPress |
| KeyUp |
| MouseDown |
| MouseMove |
| MouseUp |

#### See Also

[ApplicationMgr.ConnectCommand](applicationmgr-connectcommand.html)

[ExecutionViewMgr.ConnectCommand](executionviewmgr-connectcommand.html)

[SequenceFileViewMgr.ConnectCommand](sequencefileviewmgr-connectcommand.html)

Parent topic:

TestStand User Interface Controls

<!--NI_TOPIC bundle=teststand-api-reference path=tsuiref/buttonactionstyles.html language=enus -->
## TOPIC 04778: ButtonActionStyles

- bundle_id: `teststand-api-reference`
- source_path: `tsuiref/buttonactionstyles.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsuiref/buttonactionstyles.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Use these constants with Button.ActionStyle to specify how the button behaves when you click it. ButtonActionStyle_PushButton –(Value: 0) Specifies that the button changes to a pressed state only when you click it. ButtonActionStyle_ToggleButton –(Value: 1) Specifies that the button changes to a pre

### ButtonActionStyles

Use these constants with
 [Button.ActionStyle](button-actionstyle.html)
 to specify how the button behaves when you click it.

- ButtonActionStyle_PushButton 
 –(Value: 0) Specifies that the button changes to a pressed state only when you click it.
- ButtonActionStyle_ToggleButton 
 –(Value: 1) Specifies that the button changes to a pressed state when you set the
 Button.Value 
 property to
 True 
 and changes to a normal state when you set the value to
 False 
 .

#### See Also

[Button.ActionStyle](button-actionstyle.html)

[Button.Value](button-value.html)

Parent topic:

Core UI Enumerations

<!--NI_TOPIC bundle=teststand-api-reference path=tsuiref/buttonsizing.html language=enus -->
## TOPIC 04779: ButtonSizing

- bundle_id: `teststand-api-reference`
- source_path: `tsuiref/buttonsizing.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsuiref/buttonsizing.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Use these constants with the Button.AutoSizing property. ButtonSizing_AlwaysAutoSize –(Value: 0) Always resize the Button control to fit the text. ButtonSizing_GrowOnly –(Value: 1) Resize the Button control only when the text does not fit in the control. ButtonSizing_NeverAutoSize –(Value: 3) Never

### ButtonSizing

Use these constants with the
 [Button.AutoSizing](button-autosizing.html)
 property.

- ButtonSizing_AlwaysAutoSize 
 –(Value: 0) Always resize the Button control to fit the text.
- ButtonSizing_GrowOnly 
 –(Value: 1) Resize the Button control only when the text does not fit in the control.
- ButtonSizing_NeverAutoSize 
 –(Value: 3) Never resize the Button control.
- ButtonSizing_ShrinkOnly 
 –(Value: 2) Resize the Button control only when the text is smaller than the button.

#### See Also

[Button.AutoSizing](button-autosizing.html)

Parent topic:

Core UI Enumerations

<!--NI_TOPIC bundle=teststand-api-reference path=tsuiref/buttonstyles.html language=enus -->
## TOPIC 04780: ButtonStyles

- bundle_id: `teststand-api-reference`
- source_path: `tsuiref/buttonstyles.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsuiref/buttonstyles.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Use these constants with the Button.Style property to specify the appearance of the button and how the button operates. ButtonStyle_Standard –(Value: 1) The button displays a three-dimensional border. ButtonStyle_ToolBar –(Value: 2) You cannot tab to the button. When the application supports Microso

### ButtonStyles

Use these constants with the
 [Button.Style](button-style.html)
 property to specify the appearance of the button and how the button operates.

- ButtonStyle_Standard 
 –(Value: 1) The button displays a three-dimensional border.
- ButtonStyle_ToolBar 
 –(Value: 2) You cannot tab to the button. When the application supports Microsoft Windows XP themes, the button displays a border only when you hover over it.

#### See Also

[ButtonActionStyles](buttonactionstyles.html)

[Button.Style](button-style.html)

Parent topic:

Core UI Enumerations

<!--NI_TOPIC bundle=teststand-api-reference path=tsuiref/callstackconnection.html language=enus -->
## TOPIC 04781: CallStackConnection

- bundle_id: `teststand-api-reference`
- source_path: `tsuiref/callstackconnection.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsuiref/callstackconnection.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Represents a connection from the ExecutionView Manager control to a control that displays the callstack. You can use the connected control to change the selected sequence context when the execution is paused. This class currently contains no properties or methods. Properties or methods might be adde

### CallStackConnection

Represents a connection from the
 [ExecutionView Manager](executionviewmgr.html)
 control to a control that displays the callstack. You can use the connected control to change the selected sequence context when the execution is paused.

Note

#### See Also

[CallStackConnections](callstackconnections.html)

[ExecutionView Manager](executionviewmgr.html)

Parent topic:

TestStand User Interface Support Controls

<!--NI_TOPIC bundle=teststand-api-reference path=tsuiref/callstackconnections-add.html language=enus -->
## TOPIC 04782: CallStackConnections.Add

- bundle_id: `teststand-api-reference`
- source_path: `tsuiref/callstackconnections-add.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsuiref/callstackconnections-add.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax CallStackConnections.Add( uiObj) Return Value CallStackConnection New CallStackConnection. Purpose Creates and adds a new CallStackConnection to the collection. Parameters uiObj As Object [In] Specifies the user interface object to connect. See Also CallStackConnections.Remove ExecutionViewMg

### CallStackConnections.Add

#### Syntax

[CallStackConnections](callstackconnections.html).Add( uiObj)

#### Return Value

[CallStackConnection](callstackconnection.html)

New CallStackConnection.

#### Purpose

Creates and adds a new CallStackConnection to the collection.

#### Parameters

uiObj
 As
 [Object](data-types-for-teststand-user-interface.html)

[In] Specifies the user interface object to connect.

#### See Also

[CallStackConnections.Remove](callstackconnections-remove.html)

[ExecutionViewMgr.ConnectCallStack](executionviewmgr-connectcallstack.html)

Parent topic:

Methods

<!--NI_TOPIC bundle=teststand-api-reference path=tsuiref/callstackconnections-clear.html language=enus -->
## TOPIC 04783: CallStackConnections.Clear

- bundle_id: `teststand-api-reference`
- source_path: `tsuiref/callstackconnections-clear.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsuiref/callstackconnections-clear.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax CallStackConnections.Clear Purpose Removes all items from the collection. See Also CallStackConnections.Remove

### CallStackConnections.Clear

#### Syntax

[CallStackConnections](callstackconnections.html).Clear

#### Purpose

Removes all items from the collection.

#### See Also

[CallStackConnections.Remove](callstackconnections-remove.html)

Parent topic:

Methods

<!--NI_TOPIC bundle=teststand-api-reference path=tsuiref/callstackconnections-count.html language=enus -->
## TOPIC 04784: CallStackConnections.Count

- bundle_id: `teststand-api-reference`
- source_path: `tsuiref/callstackconnections-count.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsuiref/callstackconnections-count.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax CallStackConnections.Count Data Type Long Purpose Returns the number of items in the collection.

### CallStackConnections.Count

#### Syntax

[CallStackConnections](callstackconnections.html).Count

#### Data Type

[Long](data-types-for-teststand-user-interface.html)

#### Purpose

Returns the number of items in the collection.

Parent topic:

Properties

<!--NI_TOPIC bundle=teststand-api-reference path=tsuiref/callstackconnections-fromcontrol.html language=enus -->
## TOPIC 04785: CallStackConnections.FromControl

- bundle_id: `teststand-api-reference`
- source_path: `tsuiref/callstackconnections-fromcontrol.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsuiref/callstackconnections-fromcontrol.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax CallStackConnections.FromControl( uiObj) Return Value CallStackConnection CallStackConnection connected to this user interface object. When no CallStackConnection exists for this control, this method returns NULL . Purpose Returns the CallStackConnection connected to the UI object. Parameters

### CallStackConnections.FromControl

#### Syntax

[CallStackConnections](callstackconnections.html).FromControl( uiObj)

#### Return Value

[CallStackConnection](callstackconnection.html)

CallStackConnection connected to this user interface object. When no CallStackConnection exists for this control, this method returns
 NULL
 .

#### Purpose

Returns the CallStackConnection connected to the UI object.

#### Parameters

uiObj
 As
 [Object](data-types-for-teststand-user-interface.html)

[In] Specifies the connected user interface object.

Parent topic:

Methods

<!--NI_TOPIC bundle=teststand-api-reference path=tsuiref/callstackconnections-item.html language=enus -->
## TOPIC 04786: CallStackConnections.Item

- bundle_id: `teststand-api-reference`
- source_path: `tsuiref/callstackconnections-item.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsuiref/callstackconnections-item.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax CallStackConnections.Item( itemIndex) Data Type CallStackConnection Item located at the specified index. Purpose Returns a reference to an item at the specified index in the collection. Parameters itemIndex As Long [In] Specifies the index of the item to retrieve. See Also CallStackConnection

### CallStackConnections.Item

#### Syntax

[CallStackConnections](callstackconnections.html).Item( itemIndex)

#### Data Type

[CallStackConnection](callstackconnection.html)

Item located at the specified index.

#### Purpose

Returns a reference to an item at the specified index in the collection.

#### Parameters

itemIndex
 As
 [Long](data-types-for-teststand-user-interface.html)

[In] Specifies the index of the item to retrieve.

#### See Also

[CallStackConnection](callstackconnection.html)

[CallStackConnections.Count](callstackconnections-count.html)

Parent topic:

Properties

<!--NI_TOPIC bundle=teststand-api-reference path=tsuiref/callstackconnections-remove.html language=enus -->
## TOPIC 04787: CallStackConnections.Remove

- bundle_id: `teststand-api-reference`
- source_path: `tsuiref/callstackconnections-remove.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsuiref/callstackconnections-remove.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax CallStackConnections.Remove( uiObj) Return Value Boolean Returns True when the CallStackConnection is removed. Returns False when the CallStackConnection is not found. Purpose Removes the specified item from this collection, if it exists. Parameters uiObj As Object [In] Specifies the user int

### CallStackConnections.Remove

#### Syntax

[CallStackConnections](callstackconnections.html).Remove( uiObj)

#### Return Value

[Boolean](data-types-for-teststand-user-interface.html)

Returns
 True
 when the CallStackConnection is removed. Returns
 False
 when the CallStackConnection is not found.

#### Purpose

Removes the specified item from this collection, if it exists.

#### Parameters

uiObj
 As
 [Object](data-types-for-teststand-user-interface.html)

[In] Specifies the user interface object to disconnect.

#### See Also

[CallStackConnection](callstackconnection.html)

[CallStackConnections.Add](callstackconnections-add.html)

Parent topic:

Methods

<!--NI_TOPIC bundle=teststand-api-reference path=tsuiref/callstackconnections.html language=enus -->
## TOPIC 04788: CallStackConnections

- bundle_id: `teststand-api-reference`
- source_path: `tsuiref/callstackconnections.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsuiref/callstackconnections.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: A collection of CallStackConnection objects. Properties Count (Read Only) Item (Read Only) Methods Add Clear FromControl Remove See Also CallStackConnection

### CallStackConnections

A collection of
 [CallStackConnection](callstackconnection.html)
 objects.

#### Properties

| Count (Read Only) |
| --- |
| Item (Read Only) |

#### Methods

| Add |
| --- |
| Clear |
| FromControl |
| Remove |

#### See Also

[CallStackConnection](callstackconnection.html)

Parent topic:

TestStand User Interface Support Controls

<!--NI_TOPIC bundle=teststand-api-reference path=tsuiref/captionconnection-formatexpression.html language=enus -->
## TOPIC 04789: CaptionConnection.FormatExpression

- bundle_id: `teststand-api-reference`
- source_path: `tsuiref/captionconnection-formatexpression.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsuiref/captionconnection-formatexpression.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax CaptionConnection.FormatExpression Data Type String Purpose Specifies a format expression to evaluate when generating the caption text. Remarks For CaptionSource_MacroExpression , specify a format expression that evaluates to a string value that contains macros that specify other caption sour

### CaptionConnection.FormatExpression

#### Syntax

[CaptionConnection](captionconnection.html).FormatExpression

#### Data Type

[String](data-types-for-teststand-user-interface.html)

#### Purpose

Specifies a format expression to evaluate when generating the caption text.

#### Remarks

For
 [CaptionSource_MacroExpression](captionsources.html)
 , specify a format expression that evaluates to a string value that contains macros that specify other caption sources. For all other caption sources, specify a format expression that evaluates to a string value that contains the characters
 %1
 . This method replaces the
 %1
 characters with the text from the caption source. Pass an empty string to use the default format for the caption source.

#### See Also

[CaptionSource_MacroExpression](captionsources.html)

Parent topic:

Properties

<!--NI_TOPIC bundle=teststand-api-reference path=tsuiref/captionconnection-longname.html language=enus -->
## TOPIC 04790: CaptionConnection.LongName

- bundle_id: `teststand-api-reference`
- source_path: `tsuiref/captionconnection-longname.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsuiref/captionconnection-longname.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax CaptionConnection.LongName Data Type Boolean Purpose For certain caption sources, this property specifies whether to return a long or short version of the caption text. Refer to the CaptionSources enumeration for more information about determining when this option affects the text and for mor

### CaptionConnection.LongName

#### Syntax

[CaptionConnection](captionconnection.html).LongName

#### Data Type

[Boolean](data-types-for-teststand-user-interface.html)

#### Purpose

For certain caption sources, this property specifies whether to return a long or short version of the caption text. Refer to the
 [CaptionSources](captionsources.html)
 enumeration for more information about determining when this option affects the text and for more information about the long and short versions of the text.

#### See Also

[CaptionSources](captionsources.html)

Parent topic:

Properties

<!--NI_TOPIC bundle=teststand-api-reference path=tsuiref/captionconnection-refresh.html language=enus -->
## TOPIC 04791: CaptionConnection.Refresh

- bundle_id: `teststand-api-reference`
- source_path: `tsuiref/captionconnection-refresh.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsuiref/captionconnection-refresh.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax CaptionConnection.Refresh Purpose Refreshes the user interface control connected to this CaptionConnection with the most recent text from the CaptionSource.

### CaptionConnection.Refresh

#### Syntax

[CaptionConnection](captionconnection.html).Refresh

#### Purpose

Refreshes the user interface control connected to this CaptionConnection with the most recent text from the CaptionSource.

Parent topic:

Methods

<!--NI_TOPIC bundle=teststand-api-reference path=tsuiref/captionconnection-source.html language=enus -->
## TOPIC 04792: CaptionConnection.Source

- bundle_id: `teststand-api-reference`
- source_path: `tsuiref/captionconnection-source.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsuiref/captionconnection-source.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax CaptionConnection.Source Data Type CaptionSources Purpose Specifies the type of caption source to obtain the text from. See Also CaptionSources

### CaptionConnection.Source

#### Syntax

[CaptionConnection](captionconnection.html).Source

#### Data Type

[CaptionSources](captionsources.html)

#### Purpose

Specifies the type of caption source to obtain the text from.

#### See Also

[CaptionSources](captionsources.html)

Parent topic:

Properties

<!--NI_TOPIC bundle=teststand-api-reference path=tsuiref/captionconnection.html language=enus -->
## TOPIC 04793: CaptionConnection

- bundle_id: `teststand-api-reference`
- source_path: `tsuiref/captionconnection.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsuiref/captionconnection.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Represents a connection to a caption source. Properties FormatExpression LongName Source Method Refresh See Also CaptionConnections CaptionSources

### CaptionConnection

Represents a connection to a caption source.

#### Properties

| FormatExpression |
| --- |
| LongName |
| Source |

#### Method

| Refresh |
| --- |

#### See Also

[CaptionConnections](captionconnections.html)

[CaptionSources](captionsources.html)

Parent topic:

TestStand User Interface Support Controls

<!--NI_TOPIC bundle=teststand-api-reference path=tsuiref/captionconnections-add.html language=enus -->
## TOPIC 04794: CaptionConnections.Add

- bundle_id: `teststand-api-reference`
- source_path: `tsuiref/captionconnections-add.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsuiref/captionconnections-add.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax CaptionConnections.Add( uiObj) Return Value CaptionConnection New CaptionConnection. Purpose Creates and adds a new CaptionConnection to the collection. Parameters uiObj As Object [In] Specifies the user interface object to connect. See Also ApplicationMgr.ConnectCaption CaptionConnections.Re

### CaptionConnections.Add

#### Syntax

[CaptionConnections](captionconnections.html).Add( uiObj)

#### Return Value

[CaptionConnection](captionconnection.html)

New CaptionConnection.

#### Purpose

Creates and adds a new CaptionConnection to the collection.

#### Parameters

uiObj
 As
 [Object](data-types-for-teststand-user-interface.html)

[In] Specifies the user interface object to connect.

#### See Also

[ApplicationMgr.ConnectCaption](applicationmgr-connectcaption.html)

[CaptionConnections.Remove](captionconnections-remove.html)

Parent topic:

Methods

<!--NI_TOPIC bundle=teststand-api-reference path=tsuiref/captionconnections-clear.html language=enus -->
## TOPIC 04795: CaptionConnections.Clear

- bundle_id: `teststand-api-reference`
- source_path: `tsuiref/captionconnections-clear.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsuiref/captionconnections-clear.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax CaptionConnections.Clear Purpose Removes all items from the collection. See Also CaptionConnections.Remove

### CaptionConnections.Clear

#### Syntax

[CaptionConnections](captionconnections.html).Clear

#### Purpose

Removes all items from the collection.

#### See Also

[CaptionConnections.Remove](captionconnections-remove.html)

Parent topic:

Methods

<!--NI_TOPIC bundle=teststand-api-reference path=tsuiref/captionconnections-count.html language=enus -->
## TOPIC 04796: CaptionConnections.Count

- bundle_id: `teststand-api-reference`
- source_path: `tsuiref/captionconnections-count.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsuiref/captionconnections-count.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax CaptionConnections.Count Data Type Long Purpose Returns the number of items in the collection.

### CaptionConnections.Count

#### Syntax

[CaptionConnections](captionconnections.html).Count

#### Data Type

[Long](data-types-for-teststand-user-interface.html)

#### Purpose

Returns the number of items in the collection.

Parent topic:

Properties

<!--NI_TOPIC bundle=teststand-api-reference path=tsuiref/captionconnections-fromcontrol.html language=enus -->
## TOPIC 04797: CaptionConnections.FromControl

- bundle_id: `teststand-api-reference`
- source_path: `tsuiref/captionconnections-fromcontrol.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsuiref/captionconnections-fromcontrol.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax CaptionConnections.FromControl( uiObj) Return Value CaptionConnection CaptionConnection connected to the uiObj parameter. When no CaptionConnection exists for this control, this method returns NULL . Purpose Returns the CaptionConnection connected to the uiObj parameter. Parameters uiObj As O

### CaptionConnections.FromControl

#### Syntax

[CaptionConnections](captionconnections.html).FromControl( uiObj)

#### Return Value

[CaptionConnection](captionconnection.html)

CaptionConnection connected to the
 uiObj
 parameter. When no CaptionConnection exists for this control, this method returns
 NULL
 .

#### Purpose

Returns the CaptionConnection connected to the
 uiObj
 parameter.

#### Parameters

uiObj
 As
 [Object](data-types-for-teststand-user-interface.html)

[In] Specifies the connected user interface object.

Parent topic:

Methods

<!--NI_TOPIC bundle=teststand-api-reference path=tsuiref/captionconnections-item.html language=enus -->
## TOPIC 04798: CaptionConnections.Item

- bundle_id: `teststand-api-reference`
- source_path: `tsuiref/captionconnections-item.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsuiref/captionconnections-item.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax CaptionConnections.Item( itemIndex) Data Type CaptionConnection Item located at the specified index. Purpose Returns a reference to an item at the specified index in the collection. Parameters itemIndex As Long [In] Specifies the index of the item to retrieve. See Also CaptionConnection Capti

### CaptionConnections.Item

#### Syntax

[CaptionConnections](captionconnections.html).Item( itemIndex)

#### Data Type

[CaptionConnection](captionconnection.html)

Item located at the specified index.

#### Purpose

Returns a reference to an item at the specified index in the collection.

#### Parameters

itemIndex
 As
 [Long](data-types-for-teststand-user-interface.html)

[In] Specifies the index of the item to retrieve.

#### See Also

[CaptionConnection](captionconnection.html)

[CaptionConnections.Count](captionconnections-count.html)

Parent topic:

Properties

<!--NI_TOPIC bundle=teststand-api-reference path=tsuiref/captionconnections-remove.html language=enus -->
## TOPIC 04799: CaptionConnections.Remove

- bundle_id: `teststand-api-reference`
- source_path: `tsuiref/captionconnections-remove.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsuiref/captionconnections-remove.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax CaptionConnections.Remove( uiObj) Return Value Boolean Returns True when the CaptionConnection is removed. Returns False when the CaptionConnection is not found. Purpose Removes the specified item from this collection, if it exists. Parameters uiObj As Object [In] Specifies the user interface

### CaptionConnections.Remove

#### Syntax

[CaptionConnections](captionconnections.html).Remove( uiObj)

#### Return Value

[Boolean](data-types-for-teststand-user-interface.html)

Returns
 True
 when the CaptionConnection is removed. Returns
 False
 when the CaptionConnection is not found.

#### Purpose

Removes the specified item from this collection, if it exists.

#### Parameters

uiObj
 As
 [Object](data-types-for-teststand-user-interface.html)

[In] Specifies the user interface object to disconnect.

#### See Also

[CaptionConnections.Add](captionconnections-add.html)

Parent topic:

Methods

<!--NI_TOPIC bundle=teststand-api-reference path=tsuiref/captionconnections.html language=enus -->
## TOPIC 04800: CaptionConnections

- bundle_id: `teststand-api-reference`
- source_path: `tsuiref/captionconnections.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsuiref/captionconnections.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: A collection of CaptionConnection objects. Properties Count (Read Only) Item (Read Only) Methods Add Clear FromControl Remove See Also CaptionConnection

### CaptionConnections

A collection of
 [CaptionConnection](captionconnection.html)
 objects.

#### Properties

| Count (Read Only) |
| --- |
| Item (Read Only) |

#### Methods

| Add |
| --- |
| Clear |
| FromControl |
| Remove |

#### See Also

[CaptionConnection](captionconnection.html)

Parent topic:

TestStand User Interface Support Controls

<!--NI_TOPIC bundle=teststand-api-reference path=tsuiref/captionsources.html language=enus -->
## TOPIC 04801: CaptionSources

- bundle_id: `teststand-api-reference`
- source_path: `tsuiref/captionsources.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsuiref/captionsources.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: These constants specify types of caption sources. Each caption source provides text that describes an aspect of the current application state. You can use these constants to connect a caption to a Label or StatusBarPane using the ApplicationMgr.ConnectCaption , ExecutionViewMgr.ConnectCaption , or S

### CaptionSources

These constants specify types of caption sources. Each caption source provides text that describes an aspect of the current application state. You can use these constants to connect a caption to a
 [Label](label.html)
 or
 [StatusBarPane](statusbarpane.html)
 using the
 [ApplicationMgr.ConnectCaption](applicationmgr-connectcaption.html)
 ,
 [ExecutionViewMgr.ConnectCaption](executionviewmgr-connectcaption.html)
 , or
 [SequenceFileViewMgr.ConnectCaption](sequencefileviewmgr-connectcaption.html)
 method.

To obtain the text of a caption without connecting it to a control, call the
 [ApplicationMgr.GetCaptionText](applicationmgr-getcaptiontext.html)
 ,
 [ExecutionViewMgr.GetCaptionText](executionviewmgr-getcaptiontext.html)
 , or
 [SequenceFileViewMgr.GetCaptionText](sequencefileviewmgr-getcaptiontext.html)
 method.

A caption source applies to all manager controls unless the help for the enumeration element specifies the particular manager control or controls with which it applies.

- CaptionSource_BatchSerialNumber 
 –(Value: 4) Displays the batch serial number for the batch that contains the current execution. A process model sends the batch serial number through the
 UIMsg_ModelState_Identified 
 UIMessageCode. This caption source applies only to the ExecutionView Manager control.
- CaptionSource_BatchState 
 –(Value: 6) Displays a description of the execution state of the batch that contains the current execution. For example, this caption might display
 Initializing 
 ,
 Testing 
 ,
 Waiting 
 , or
 Completed [Passed] 
 . This caption source applies only to the ExecutionView Manager control.
- CaptionSource_BatchStatus 
 –(Value: 5) Displays the batch result status for the batch that contains the current execution. A process model sends the batch status through the
 UIMsg_ModelState_TestingComplete 
 UIMessageCode. This caption source applies only to the ExecutionView Manager control.
- CaptionSource_CurrentCallStackEntry 
 –(Value: 26) Displays a name that identifies the current call stack item in the foreground thread in the current execution. This caption source applies only to the ExecutionView Manager control.
- CaptionSource_CurrentExecution 
 –(Value: 24) Displays a name that identifies the current execution. This caption source applies only to the ExecutionView Manager control.
- CaptionSource_CurrentProcessModelFile 
 –(Value: 27) Displays the path name of the process model file for the currently executing or currently selected sequence file. When you pass
 True 
 to the long name option for the caption, the caption displays the full path name. Otherwise, the caption displays the base filename.
- CaptionSource_CurrentSequence 
 –(Value: 13) Displays the name of the currently executing or currently selected sequence. This caption source applies to the ExecutionView Manager and SequenceFileView Manager controls.
- CaptionSource_CurrentSequenceComment 
 –(Value: 14) Displays the comment for the currently executing or currently selected sequence. This caption source applies to the ExecutionView Manager and SequenceFileView Manager controls.
- CaptionSource_CurrentSequenceFile 
 –(Value: 11) Displays the path name of the currently executing or currently selected sequence file with a read-only, locked, executing, or modified file state suffix. When you pass
 True 
 to the long name option for the caption, the caption displays the full path name. Otherwise, the caption displays the base filename. This caption source applies to the ExecutionView Manager and SequenceFileView Manager controls.
- CaptionSource_CurrentSequenceFile_FileStateOnly 
 –(Value: 33) Displays only the read-only, locked, executing, or modified file state of the currently executing or currently selected sequence file. This caption source applies to the ExecutionView Manager and SequenceFileView Manager controls.
- CaptionSource_CurrentSequenceFile_WithoutFileState 
 –(Value: 32) Displays the path name of the currently executing or currently selected sequence file without a file state suffix. When you pass
 True 
 to the long name option for the caption, the caption displays the full path name. Otherwise, the caption displays the base filename. This caption source applies to the ExecutionView Manager and SequenceFileView Manager controls.
- CaptionSource_CurrentSequenceFileComment 
 –(Value: 12) Displays the comment for the currently executing or currently selected sequence file. This caption source applies to the ExecutionView Manager and SequenceFileView Manager controls.
- CaptionSource_CurrentStep 
 –(Value: 16) Displays the name of the current step in the current execution. This caption source applies only to the ExecutionView Manager control.
- CaptionSource_CurrentStepComment 
 –(Value: 17) Displays the comment for the current step in the current execution. This caption source applies only to the ExecutionView Manager control.
- CaptionSource_CurrentStepGroup 
 –(Value: 15) Displays the name of the currently executing or currently selected step group. This caption source applies to the ExecutionView Manager and SequenceFileView Manager controls.
- CaptionSource_CurrentStepIndex_ZeroBased 
 –(Value: 18) Displays the zero-based index of the current step in the current execution. This caption source applies only to the ExecutionView Manager control.
- CaptionSource_CurrentTestIndex_OneBased 
 –(Value: 19) Displays the one-based index of the current step in the current execution. This caption source applies only to the ExecutionView Manager control.
- CaptionSource_CurrentThread 
 –(Value: 25) Displays a name that identifies the foreground thread in the current execution. This caption source applies only to the ExecutionView Manager control.
- CaptionSource_Date 
 –(Value: 31) Displays the current date. When you pass
 True 
 to the long name option for the caption, the caption displays the system long date format. Otherwise, the caption displays the system short date format.
- CaptionSource_EngineEnvironment 
 –(Value: 34) Displays the path name of the current TestStand environment. When you pass
 True 
 to the long name option for the caption, the caption displays the full path name. Otherwise, the caption displays the base filename.
- CaptionSource_MacroExpression 
 –(Value: 1) Displays the evaluated result of a format expression that can contain macros that specify text from other caption sources. You can use this caption source to combine text from multiple caption sources. Place the macros that specify other caption sources within string constants in the format expression for the caption text or caption connection you create with this caption source. The following are the available macros:
 Macro, Caption Source, Specifies caption source long name 
 %UUTSerialNumber%, CaptionSource_UUTSerialNumber, no 
 %UUTStatus%, CaptionSource_UUTStatus, no 
 %BatchSerialNumber%, CaptionSource_BatchSerialNumber, no 
 %BatchStatus%, CaptionSource_BatchStatus, no 
 %BatchState%, CaptionSource_BatchState, no 
 %ModelState%, CaptionSource_ModelState, no 
 %UserName%, CaptionSource_UserName, no 
 %ProgressText%, CaptionSource_ProgressText, no 
 %ProgressPercent%, CaptionSource_ProgressPercent, no 
 %CurrentSequenceFile%, CaptionSource_CurrentSequenceFile, no 
 %CurrentSequence%, CaptionSource_CurrentSequence, no 
 %CurrentStepGroup%, CaptionSource_CurrentStepGroup, no 
 %CurrentStep%, CaptionSource_CurrentStep, no 
 %CurrentStepIndex_ZeroBased%, CaptionSource_CurrentStepIndex_ZeroBased, no 
 %CurrentTestIndex_OneBased%, CaptionSource_CurrentTestIndex_OneBased, no 
 %NumberOfSteps%, CaptionSource_NumberOfSteps, no 
 %CurrentExecution%, CaptionSource_CurrentExecution, no 
 %CurrentThread%, CaptionSource_CurrentThread, no 
 %CurrentCallStackEntry%, CaptionSource_CurrentCallStackEntry, no 
 %CurrentProcessModelFile%, CaptionSource_CurrentProcessModelFile, no 
 %UUTSerialNumberLongName%, CaptionSource_UUTSerialNumber, yes 
 %UUTStatusLongName%, CaptionSource_UUTStatus, yes 
 %BatchSerialNumberLongName%, CaptionSource_BatchSerialNumber, yes 
 %BatchStatusLongName%, CaptionSource_BatchStatus, yes 
 %BatchStateLongName%, CaptionSource_BatchState, yes 
 %ModelStateLongName%,CaptionSource_ModelState,yes 
 %UserNameLongName%,CaptionSource_UserName,yes 
 %ProgressTextLongName%,CaptionSource_ProgressText,yes 
 %ProgressPercentLongName%,CaptionSource_ProgressPercent,yes 
 %CurrentSequenceFileLongName%,CaptionSource_CurrentSequenceFile,yes 
 %CurrentSequenceLongName%,CaptionSource_CurrentSequence,yes 
 %CurrentStepGroupLongName%,CaptionSource_CurrentStepGroup,yes 
 %CurrentStepLongName%,CaptionSource_CurrentStep,yes 
 %CurrentStepIndex_ZeroBasedLongName%,CaptionSource_CurrentStepIndex_ZeroBased,yes 
 %CurrentTestIndex_OneBasedLongName%, CaptionSource_CurrentTestIndex_OneBased, yes 
 %NumberOfStepsLongName%, CaptionSource_NumberOfSteps, yes 
 %CurrentExecutionLongName%, CaptionSource_CurrentExecution, yes 
 %CurrentThreadLongName%, CaptionSource_CurrentThread, yes 
 %CurrentCallStackEntryLongName%, CaptionSource_CurrentCallStackEntry, yes 
 %CurrentProcessModelFileLongName%, CaptionSource_CurrentProcessModelFile, yes
- CaptionSource_ModelState 
 –(Value: 7) Displays a description of the execution state of the current execution. For example, this caption might display
 Initializing 
 ,
 Testing 
 ,
 Waiting 
 , or
 Completed [Passed] 
 . This caption source applies only to the ExecutionView Manager control.
- CaptionSource_NotASource 
 –(Value: 0) Guaranteed to never be a valid caption source specifier.
- CaptionSource_NumberOfSteps 
 –(Value: 22) Displays the number of steps in the currently executing or currently selected step group. This caption source applies to the ExecutionView Manager and SequenceFileView Manager controls.
- CaptionSource_NumberOfTests 
 –(Value: 23) Displays the number of steps in the currently executing or currently selected step group. The description uses the word
 test 
 in place of the word
 step 
 . This caption source applies to the ExecutionView Manager and SequenceFileView Manager controls.
- CaptionSource_ProgressPercent 
 –(Value: 10) Displays the progress percentage information for the current execution. This caption indicates the progress of operations for which the execution chooses to report the amount of progress. The caption does not necessarily reflect the progress of the execution as a whole. A process model sends the progress percent through the
 UIMsg_ProgressPercent 
 UIMessageCode. This caption source applies only to the ExecutionView Manager control.
- CaptionSource_ProgressText 
 –(Value: 9) Displays the progress message for the current execution. A process model sends the progress text through the
 UIMsg_ProgressText 
 UIMessageCode. This caption source applies only to the ExecutionView Manager control.
- CaptionSource_ReportLocation 
 –(Value: 28) Displays the location of the report for the current execution. The
 
 Report.Location 
 property specifies the display value for a report. This caption source applies only to the ExecutionView Manager control.
- CaptionSource_SelectedSteps_ZeroBased 
 –(Value: 20) Displays a description of which steps are selected. The description uses zero-based indexes. This caption source applies to the ExecutionView Manager and SequenceFileView Manager controls.
- CaptionSource_SelectedTests_OneBased 
 –(Value: 21) Displays a description of which steps are selected. The description uses one-based indexes and the word
 test 
 in place of the word
 step 
 . This caption source applies to the ExecutionView Manager and SequenceFileView Manager controls.
- CaptionSource_TestSocketIndex 
 –(Value: 29) Displays the zero-based index of the test socket for the current execution. Displays nothing when the execution is not participating in a multi-socket test process. A process model sends the text socket index through the
 UIMsg_ModelState_BeginTesting 
 and
 UIMsg_ModelState_Waiting 
 UIMessageCodes. This caption source applies only to the ExecutionView Manager control.
- CaptionSource_Time 
 –(Value: 30) Displays the current time using the system time format.
- CaptionSource_UserName 
 –(Value: 8) Displays the name of the current user. When you pass
 True 
 to the long name option for the caption, the caption displays the full user name. Otherwise, the caption displays the user login name.
- CaptionSource_UUTSerialNumber 
 –(Value: 2) Displays the serial number of the UUT for the current execution. A process model sends the UUT serial number through the
 UIMsg_ModelState_Identified 
 UIMessageCode. This caption source applies only to the ExecutionView Manager control.
- CaptionSource_UUTStatus 
 –(Value: 3) Displays the result status of the UUT for the current execution. A process model sends the UUT status through the
 UIMsg_ModelState_TestingComplete 
 UIMessageCode. This caption source applies only to the ExecutionView Manager control.

#### See Also

[ApplicationMgr.ConnectCaption](applicationmgr-connectcaption.html)

[ApplicationMgr.GetCaptionText](applicationmgr-getcaptiontext.html)

[ExecutionViewMgr.ConnectCaption](executionviewmgr-connectcaption.html)

[ExecutionViewMgr.GetCaptionText](executionviewmgr-getcaptiontext.html)

[Label](label.html)

[Report.Location](../tsapiref/report-location.html)

[SequenceFileViewMgr.ConnectCaption](sequencefileviewmgr-connectcaption.html)

[SequenceFileViewMgr.GetCaptionText](sequencefileviewmgr-getcaptiontext.html)

[StatusBarPane](statusbarpane.html)

[UIMessageCodes](../tsapiref/uimessagecodes.html)

Parent topic:

Support UI Enumerations

<!--NI_TOPIC bundle=teststand-api-reference path=tsuiref/checkbox-backcolor.html language=enus -->
## TOPIC 04802: CheckBox.BackColor

- bundle_id: `teststand-api-reference`
- source_path: `tsuiref/checkbox-backcolor.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsuiref/checkbox-backcolor.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax CheckBox.BackColor Data Type Color Purpose Specifies the background color for the control. This property does not change the appearance of a control when you set the CheckBox.Style property to CheckBoxStyle_Button . See Also CheckBox.ForeColor CheckBox.Style

### CheckBox.BackColor

#### Syntax

[CheckBox](checkbox.html).BackColor

#### Data Type

[Color](data-types-for-teststand-user-interface.html)

#### Purpose

Specifies the background color for the control. This property does not change the appearance of a control when you set the
 [CheckBox.Style](checkbox-style.html)
 property to
 CheckBoxStyle_Button
 .

#### See Also

[CheckBox.ForeColor](checkbox-forecolor.html)

[CheckBox.Style](checkbox-style.html)

Parent topic:

Properties

<!--NI_TOPIC bundle=teststand-api-reference path=tsuiref/checkbox-caption.html language=enus -->
## TOPIC 04803: CheckBox.Caption

- bundle_id: `teststand-api-reference`
- source_path: `tsuiref/checkbox-caption.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsuiref/checkbox-caption.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax CheckBox.Caption Data Type String Purpose Specifies the text the control displays. Remarks In the caption, include an ampersand ( & ) immediately before the character, if any, you want to designate as an accelerator character. The character displays as underlined. Press <Alt> and click the un

### CheckBox.Caption

#### Syntax

[CheckBox](checkbox.html).Caption

#### Data Type

[String](data-types-for-teststand-user-interface.html)

#### Purpose

Specifies the text the control displays.

#### Remarks

In the caption, include an ampersand (
 &
 ) immediately before the character, if any, you want to designate as an accelerator character. The character displays as underlined. Press <Alt> and click the underlined character to move the focus to the control. To include an ampersand character in a caption without creating an accelerator character, include two consecutive ampersands. A single ampersand displays in the caption and no characters display as underlined.

When you connect this control to a manager control, the manager control sets this property automatically.

#### See Also

[CheckBox.TextAlign](checkbox-textalign.html)

Parent topic:

Properties

<!--NI_TOPIC bundle=teststand-api-reference path=tsuiref/checkbox-checked.html language=enus -->
## TOPIC 04804: CheckBox.Checked

- bundle_id: `teststand-api-reference`
- source_path: `tsuiref/checkbox-checked.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsuiref/checkbox-checked.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax CheckBox.Checked Data Type Boolean Returns True when the CheckBox control is in the checked state. Otherwise, returns False . Purpose Specifies a value that indicates whether the CheckBox control is in the checked state.

### CheckBox.Checked

#### Syntax

[CheckBox](checkbox.html).Checked

#### Data Type

[Boolean](data-types-for-teststand-user-interface.html)

Returns
 True
 when the CheckBox control is in the checked state. Otherwise, returns
 False
 .

#### Purpose

Specifies a value that indicates whether the CheckBox control is in the checked state.

Parent topic:

Properties

<!--NI_TOPIC bundle=teststand-api-reference path=tsuiref/checkbox-click.html language=enus -->
## TOPIC 04805: CheckBox.Click

- bundle_id: `teststand-api-reference`
- source_path: `tsuiref/checkbox-click.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsuiref/checkbox-click.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax ControlName_Click Applies To CheckBox Purpose Occurs when you press and release the mouse on the control or when the checked state of the control changes. See Also CheckBox.Checked CheckBox.MouseDown CheckBox.MouseMove CheckBox.MouseUp

### CheckBox.Click

#### Syntax

ControlName_Click

#### Applies To

[CheckBox](checkbox.html)

#### Purpose

Occurs when you press and release the mouse on the control or when the checked state of the control changes.

#### See Also

[CheckBox.Checked](checkbox-checked.html)

[CheckBox.MouseDown](checkbox-mousedown.html)

[CheckBox.MouseMove](checkbox-mousemove.html)

[CheckBox.MouseUp](checkbox-mouseup.html)

Parent topic:

Events

<!--NI_TOPIC bundle=teststand-api-reference path=tsuiref/checkbox-connectionactivity.html language=enus -->
## TOPIC 04806: CheckBox.ConnectionActivity

- bundle_id: `teststand-api-reference`
- source_path: `tsuiref/checkbox-connectionactivity.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsuiref/checkbox-connectionactivity.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax ControlName_ConnectionActivity( activity) Applies To CheckBox Purpose Occurs after the connection to a manager control makes a change to a user interface control. Parameters activity As ConnectionActivityTypes [In] Specifies the type of change.

### CheckBox.ConnectionActivity

#### Syntax

ControlName_ConnectionActivity( activity)

#### Applies To

[CheckBox](checkbox.html)

#### Purpose

Occurs after the connection to a manager control makes a change to a user interface control.

#### Parameters

activity
 As
 [ConnectionActivityTypes](connectionactivitytypes.html)

[In] Specifies the type of change.

Parent topic:

Events

<!--NI_TOPIC bundle=teststand-api-reference path=tsuiref/checkbox-enabled.html language=enus -->
## TOPIC 04807: CheckBox.Enabled

- bundle_id: `teststand-api-reference`
- source_path: `tsuiref/checkbox-enabled.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsuiref/checkbox-enabled.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax CheckBox.Enabled Data Type Boolean Purpose The control responds to user input only when this property is True .

### CheckBox.Enabled

#### Syntax

[CheckBox](checkbox.html).Enabled

#### Data Type

[Boolean](data-types-for-teststand-user-interface.html)

#### Purpose

The control responds to user input only when this property is
 True
 .

Parent topic:

Properties

<!--NI_TOPIC bundle=teststand-api-reference path=tsuiref/checkbox-font.html language=enus -->
## TOPIC 04808: CheckBox.Font

- bundle_id: `teststand-api-reference`
- source_path: `tsuiref/checkbox-font.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsuiref/checkbox-font.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax CheckBox.Font Data Type Font Purpose Specifies the font for the control when the value of the CheckBox.FontSource property is FontSource_UseFontProperty . See Also CheckBox.FontSource FontSources

### CheckBox.Font

#### Syntax

[CheckBox](checkbox.html).Font

#### Data Type

[Font](data-types-for-teststand-user-interface.html)

#### Purpose

Specifies the font for the control when the value of the
 [CheckBox.FontSource](checkbox-fontsource.html)
 property is
 FontSource_UseFontProperty
 .

#### See Also

[CheckBox.FontSource](checkbox-fontsource.html)

[FontSources](fontsources.html)

Parent topic:

Properties

<!--NI_TOPIC bundle=teststand-api-reference path=tsuiref/checkbox-fontsource.html language=enus -->
## TOPIC 04809: CheckBox.FontSource

- bundle_id: `teststand-api-reference`
- source_path: `tsuiref/checkbox-fontsource.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsuiref/checkbox-fontsource.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax CheckBox.FontSource Data Type FontSources Use the following constants with this data type: FontSource_UseContainerFont –(Value: 2) The font the container supplies. FontSource_UseFontProperty –(Value: 0) A corresponding Font property of the control determines the font. FontSource_UseGUIFont –(

### CheckBox.FontSource

#### Syntax

[CheckBox](checkbox.html).FontSource

#### Data Type

[FontSources](fontsources.html)

Use the following constants with this data type:

- FontSource_UseContainerFont 
 –(Value: 2) The font the container supplies.
- FontSource_UseFontProperty 
 –(Value: 0) A corresponding
 Font 
 property of the control determines the font.
- FontSource_UseGUIFont 
 –(Value: 1) The default system font for user interface objects.
- FontSource_UseIconFont 
 –(Value: 5) The system font for an icon title.
- FontSource_UseInactiveTitlebarFont 
 –(Value: 4) The system font for an inactive titlebar.
- FontSource_UseMenuFont 
 –(Value: 6) The system font for a menu.
- FontSource_UseMessageBoxFont 
 –(Value: 7) The system font for a message box.
- FontSource_UsePaletteTitleFont 
 –(Value: 8) The system font for the title of a Tools window.
- FontSource_UseSelectedItemsFont 
 –(Value: 9) The system font for the selected menu items.
- FontSource_UseSystemFixedWidthFont 
 –(Value: 11) The system font for monospaced text.
- FontSource_UseTitlebarFont 
 –(Value: 3) The system font for a title bar.
- FontSource_UseToolTipFont 
 –(Value: 10) The system font for tooltips and status bars.
- FontSource_UseUIStyleFont 
 –(Value: 12) The font the
 UIStyle 
 object supplies.

#### Purpose

Specifies the font the control uses. The default value for this property is
 FontSource_UseGUIFont
 .

#### Remarks

When the value of this property is
 FontSource_UseFontProperty
 , the corresponding
 Font
 property specifies the particular font the control uses. Otherwise, the control uses the font from the source this property specifies. Refer to the
 [FontSources](fontsources.html)
 enumeration for the list of valid font sources.

Set this property to a value other than
 FontSource_UseFontProperty
 if you expect the font the
 [CheckBox.Font](checkbox-font.html)
 property specifies to not be present on a computer at run time. For example, a font present on an English version of the Microsoft Windows operating system might not be present on a Japanese version of the Windows operating system.

#### See Also

[CheckBox.Font](checkbox-font.html)

[FontSources](fontsources.html)

Parent topic:

Properties

<!--NI_TOPIC bundle=teststand-api-reference path=tsuiref/checkbox-forecolor.html language=enus -->
## TOPIC 04810: CheckBox.ForeColor

- bundle_id: `teststand-api-reference`
- source_path: `tsuiref/checkbox-forecolor.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsuiref/checkbox-forecolor.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax CheckBox.ForeColor Data Type Color Purpose Specifies the foreground color for the CheckBox control. This property does not change the appearance of a control when you set the CheckBox.Style property to CheckBoxStyle_Button . See Also CheckBox.BackColor CheckBox.Style

### CheckBox.ForeColor

#### Syntax

[CheckBox](checkbox.html).ForeColor

#### Data Type

[Color](data-types-for-teststand-user-interface.html)

#### Purpose

Specifies the foreground color for the CheckBox control. This property does not change the appearance of a control when you set the
 [CheckBox.Style](checkbox-style.html)
 property to
 CheckBoxStyle_Button
 .

#### See Also

[CheckBox.BackColor](checkbox-backcolor.html)

[CheckBox.Style](checkbox-style.html)

Parent topic:

Properties

<!--NI_TOPIC bundle=teststand-api-reference path=tsuiref/checkbox-hwnd.html language=enus -->
## TOPIC 04811: CheckBox.hWnd

- bundle_id: `teststand-api-reference`
- source_path: `tsuiref/checkbox-hwnd.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsuiref/checkbox-hwnd.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax CheckBox.hWnd Data Type Long Purpose Returns a Window handle for the CheckBox control. Remarks You can use the returned Window handle with the Microsoft Windows API functions. Using Windows API functions with this property can cause undefined behavior.

### CheckBox.hWnd

#### Syntax

[CheckBox](checkbox.html).hWnd

#### Data Type

[Long](data-types-for-teststand-user-interface.html)

#### Purpose

Returns a Window handle for the CheckBox control.

#### Remarks

You can use the returned Window handle with the Microsoft Windows API functions.

Note

Parent topic:

Properties

<!--NI_TOPIC bundle=teststand-api-reference path=tsuiref/checkbox-image.html language=enus -->
## TOPIC 04812: CheckBox.Image

- bundle_id: `teststand-api-reference`
- source_path: `tsuiref/checkbox-image.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsuiref/checkbox-image.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax CheckBox.Image Data Type Picture Purpose Specifies a custom graphic for the CheckBox control. Remarks This property is used only when the style of the control is CheckBoxStyle_Button . Use the Engine.Images property to obtain the TestStand images collection, and use the Images.FindImage metho

### CheckBox.Image

#### Syntax

[CheckBox](checkbox.html).Image

#### Data Type

[Picture](data-types-for-teststand-user-interface.html)

#### Purpose

Specifies a custom graphic for the CheckBox control.

#### Remarks

This property is used only when the style of the control is
 CheckBoxStyle_Button
 .

Use the
 
 [Engine.Images](../tsapiref/engine-images.html)
 property to obtain the TestStand images collection, and use the
 
 [Images.FindImage](../tsapiref/images-findimage.html)
 method to obtain a particular image reference. Icon files are located in the
 [<TestStand>](/csh?context=ts_tsfundamentals_directories)
 \Components\Icons
 and
 <TestStand Public>\Components\Icons
 directories.

#### See Also

[CheckBox.Style](checkbox-style.html)

[CheckBoxStyles](checkboxstyles.html)

[Engine.Images](../tsapiref/engine-images.html)

[Images.FindImage](../tsapiref/images-findimage.html)

Parent topic:

Properties

<!--NI_TOPIC bundle=teststand-api-reference path=tsuiref/checkbox-imagealign.html language=enus -->
## TOPIC 04813: CheckBox.ImageAlign

- bundle_id: `teststand-api-reference`
- source_path: `tsuiref/checkbox-imagealign.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsuiref/checkbox-imagealign.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax CheckBox.ImageAlign Data Type ContentAlignmentStyles Use the following constants with this data type: ContentAlignmentStyle_BottomCenter –(Value: 8) Content is vertically aligned at the bottom and horizontally aligned in the center. ContentAlignmentStyle_BottomLeft –(Value: 6) Content is vert

### CheckBox.ImageAlign

#### Syntax

[CheckBox](checkbox.html).ImageAlign

#### Data Type

[ContentAlignmentStyles](contentalignmentstyles.html)

Use the following constants with this data type:

- ContentAlignmentStyle_BottomCenter 
 –(Value: 8) Content is vertically aligned at the bottom and horizontally aligned in the center.
- ContentAlignmentStyle_BottomLeft 
 –(Value: 6) Content is vertically aligned at the bottom and horizontally aligned on the left.
- ContentAlignmentStyle_BottomRight 
 –(Value: 7) Content is vertically aligned at the bottom and horizontally aligned on the right.
- ContentAlignmentStyle_MiddleCenter 
 –(Value: 2) Content is vertically aligned in the middle and horizontally aligned in the center.
- ContentAlignmentStyle_MiddleLeft 
 –(Value: 0) Content is vertically aligned in the middle and horizontally aligned on the left.
- ContentAlignmentStyle_MiddleRight 
 –(Value: 1) Content is vertically aligned in the middle and horizontally aligned on the right.
- ContentAlignmentStyle_TopCenter 
 –(Value: 5) Content is vertically aligned at the top and horizontally aligned in the center.
- ContentAlignmentStyle_TopLeft 
 –(Value: 3) Content is vertically aligned at the top and horizontally aligned on the left.
- ContentAlignmentStyle_TopRight 
 –(Value: 4) Content is vertically aligned at the top and horizontally aligned on the right.

#### Purpose

Specifies the horizontal and vertical alignment of an
 [Image](checkbox-image.html)
 on a CheckBox control.

#### Remarks

This property is used only when the style of the control is
 CheckBoxStyle_Button
 .

#### See Also

[CheckBox.Image](checkbox-image.html)

[CheckBox.Style](checkbox-style.html)

[CheckBoxStyles](checkboxstyles.html)

Parent topic:

Properties

<!--NI_TOPIC bundle=teststand-api-reference path=tsuiref/checkbox-keydown.html language=enus -->
## TOPIC 04814: CheckBox.KeyDown

- bundle_id: `teststand-api-reference`
- source_path: `tsuiref/checkbox-keydown.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsuiref/checkbox-keydown.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax ControlName_KeyDown( keyCode, shift) Applies To CheckBox Purpose Occurs when the user presses a key while the control has the input focus. This event occurs before the CheckBox.KeyPress event. Parameters keyCode As Integer [In/Out] Specifies the KeyCodes constant of the key the user pressed.

### CheckBox.KeyDown

#### Syntax

ControlName_KeyDown( keyCode, shift)

#### Applies To

[CheckBox](checkbox.html)

#### Purpose

Occurs when the user presses a key while the control has the input focus. This event occurs before the
 [CheckBox.KeyPress](checkbox-keypress.html)
 event.

#### Parameters

keyCode
 As
 [Integer](data-types-for-teststand-user-interface.html)

[In/Out] Specifies the
 [KeyCodes](keycodes.html)
 constant of the key the user pressed.

shift
 As
 [Integer](data-types-for-teststand-user-interface.html)

[In] Specifies a combination of the
 [KeyModifiers](keymodifiers.html)
 constants that specifies the state of the <Shift>, <Ctrl>, and <Alt> keys.

#### See Also

[CheckBox.KeyPress](checkbox-keypress.html)

[CheckBox.KeyUp](checkbox-keyup.html)

[KeyCodes](keycodes.html)

[KeyModifiers](keymodifiers.html)

Parent topic:

Events

<!--NI_TOPIC bundle=teststand-api-reference path=tsuiref/checkbox-keypress.html language=enus -->
## TOPIC 04815: CheckBox.KeyPress

- bundle_id: `teststand-api-reference`
- source_path: `tsuiref/checkbox-keypress.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsuiref/checkbox-keypress.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax ControlName_KeyPress( keyAscii) Applies To CheckBox Purpose Occurs when the user presses a key while a control is active. This event occurs after the CheckBox.KeyDown event. Parameters keyAscii As Integer [In/Out] Specifies the ASCII value of the pressed key. See Also CheckBox.KeyDown CheckBo

### CheckBox.KeyPress

#### Syntax

ControlName_KeyPress( keyAscii)

#### Applies To

[CheckBox](checkbox.html)

#### Purpose

Occurs when the user presses a key while a control is active. This event occurs after the
 [CheckBox.KeyDown](checkbox-keydown.html)
 event.

#### Parameters

keyAscii
 As
 [Integer](data-types-for-teststand-user-interface.html)

[In/Out] Specifies the ASCII value of the pressed key.

#### See Also

[CheckBox.KeyDown](checkbox-keydown.html)

[CheckBox.KeyUp](checkbox-keyup.html)

Parent topic:

Events

<!--NI_TOPIC bundle=teststand-api-reference path=tsuiref/checkbox-keyup.html language=enus -->
## TOPIC 04816: CheckBox.KeyUp

- bundle_id: `teststand-api-reference`
- source_path: `tsuiref/checkbox-keyup.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsuiref/checkbox-keyup.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax ControlName_KeyUp( keyCode, shift) Applies To CheckBox Purpose Occurs when the user releases a key while the control has the input focus. Parameters keyCode As Integer [In] Specifies the KeyCodes constant of the key the user pressed. shift As Integer [In] Specifies a combination of the KeyMod

### CheckBox.KeyUp

#### Syntax

ControlName_KeyUp( keyCode, shift)

#### Applies To

[CheckBox](checkbox.html)

#### Purpose

Occurs when the user releases a key while the control has the input focus.

#### Parameters

keyCode
 As
 [Integer](data-types-for-teststand-user-interface.html)

[In] Specifies the
 [KeyCodes](keycodes.html)
 constant of the key the user pressed.

shift
 As
 [Integer](data-types-for-teststand-user-interface.html)

[In] Specifies a combination of the
 [KeyModifiers](keymodifiers.html)
 constants that specifies the state of the <Shift>, <Ctrl>, and <Alt> keys.

#### See Also

[CheckBox.KeyDown](checkbox-keydown.html)

[CheckBox.KeyPress](checkbox-keypress.html)

[KeyCodes](keycodes.html)

[KeyModifiers](keymodifiers.html)

Parent topic:

Events

<!--NI_TOPIC bundle=teststand-api-reference path=tsuiref/checkbox-localize.html language=enus -->
## TOPIC 04817: CheckBox.Localize

- bundle_id: `teststand-api-reference`
- source_path: `tsuiref/checkbox-localize.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsuiref/checkbox-localize.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax CheckBox.Localize( sectionName) Purpose Localizes the text caption on the button in this control. Remarks First, update a .ini file located in the TestStand Language directory with the required string. Second, use the string tag in the .ini file as the caption for the control. When you call t

### CheckBox.Localize

#### Syntax

[CheckBox](checkbox.html).Localize( sectionName)

#### Purpose

Localizes the text caption on the button in this control.

#### Remarks

First, update a
 .ini
 file located in the TestStand
 Language
 directory with the required string. Second, use the string tag in the
 .ini
 file as the caption for the control.

When you call this method, the control replaces the caption with the string from the
 .ini
 file. If the caption is not a tag in the
 .ini
 file, the caption does not change.

Note

#### Parameters

sectionName
 As
 [String](data-types-for-teststand-user-interface.html)

[In] Specifies the name of the section in the language files that contains the localized text.

#### See Also

[ApplicationMgr.LocalizeAllControls](applicationmgr-localizeallcontrols.html)

Parent topic:

Methods

<!--NI_TOPIC bundle=teststand-api-reference path=tsuiref/checkbox-maskcolor.html language=enus -->
## TOPIC 04818: CheckBox.MaskColor

- bundle_id: `teststand-api-reference`
- source_path: `tsuiref/checkbox-maskcolor.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsuiref/checkbox-maskcolor.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax CheckBox.MaskColor Data Type Color Purpose Specifies a color in the picture of the control as a mask color. You can use the mask color to create transparent regions. Remarks The color specified is used as a mask color when the CheckBox.UseMaskColor property is True . This property is used onl

### CheckBox.MaskColor

#### Syntax

[CheckBox](checkbox.html).MaskColor

#### Data Type

[Color](data-types-for-teststand-user-interface.html)

#### Purpose

Specifies a color in the picture of the control as a mask color. You can use the mask color to create transparent regions.

#### Remarks

The color specified is used as a mask color when the
 [CheckBox.UseMaskColor](checkbox-usemaskcolor.html)
 property is
 True
 .

This property is used only when the style of the control is
 CheckBoxStyle_Button
 .

#### See Also

[CheckBox.UseMaskColor](checkbox-usemaskcolor.html)

[CheckBoxStyles](checkboxstyles.html)

Parent topic:

Properties

<!--NI_TOPIC bundle=teststand-api-reference path=tsuiref/checkbox-mousedown.html language=enus -->
## TOPIC 04819: CheckBox.MouseDown

- bundle_id: `teststand-api-reference`
- source_path: `tsuiref/checkbox-mousedown.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsuiref/checkbox-mousedown.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax ControlName_MouseDown( btn, shift, x, y) Applies To CheckBox Purpose Occurs when the user clicks the mouse on the control. Parameters btn As Integer [In] Specifies the mouse button pressed to cause this event. You can use any one of the MouseButtons constants. shift As Integer [In] Specifies

### CheckBox.MouseDown

#### Syntax

ControlName_MouseDown( btn, shift, x, y)

#### Applies To

[CheckBox](checkbox.html)

#### Purpose

Occurs when the user clicks the mouse on the control.

#### Parameters

btn
 As
 [Integer](data-types-for-teststand-user-interface.html)

[In] Specifies the mouse button pressed to cause this event. You can use any one of the
 [MouseButtons](mousebuttons.html)
 constants.

shift
 As
 [Integer](data-types-for-teststand-user-interface.html)

[In] Specifies a combination of the
 [KeyModifiers](keymodifiers.html)
 constants that specifies the state of the <Shift>, <Ctrl>, and <Alt> keys.

x
 As
 [long](data-types-for-teststand-user-interface.html)

[In] Specifies the x-coordinate of the mouse pointer, relative to the control, at the moment when the event occurs.

y
 As
 [long](data-types-for-teststand-user-interface.html)

[In] Specifies the y-coordinate of the mouse pointer, relative to the control, at the moment when the event occurs.

#### See Also

[CheckBox.Click](checkbox-click.html)

[CheckBox.MouseMove](checkbox-mousemove.html)

[CheckBox.MouseUp](checkbox-mouseup.html)

[KeyModifiers](keymodifiers.html)

[MouseButtons](mousebuttons.html)

Parent topic:

Events

<!--NI_TOPIC bundle=teststand-api-reference path=tsuiref/checkbox-mousemove.html language=enus -->
## TOPIC 04820: CheckBox.MouseMove

- bundle_id: `teststand-api-reference`
- source_path: `tsuiref/checkbox-mousemove.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsuiref/checkbox-mousemove.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax ControlName_MouseMove( btn, shift, x, y) Applies To CheckBox Purpose Occurs when the user moves the mouse over the control. Parameters btn As Integer [In] Specifies the mouse button pressed to cause this event. You can use any one of the MouseButtons constants. shift As Integer [In] Specifies

### CheckBox.MouseMove

#### Syntax

ControlName_MouseMove( btn, shift, x, y)

#### Applies To

[CheckBox](checkbox.html)

#### Purpose

Occurs when the user moves the mouse over the control.

#### Parameters

btn
 As
 [Integer](data-types-for-teststand-user-interface.html)

[In] Specifies the mouse button pressed to cause this event. You can use any one of the
 [MouseButtons](mousebuttons.html)
 constants.

shift
 As
 [Integer](data-types-for-teststand-user-interface.html)

[In] Specifies a combination of the
 [KeyModifiers](keymodifiers.html)
 constants that specifies the state of the <Shift>, <Ctrl>, and <Alt> keys.

x
 As
 [long](data-types-for-teststand-user-interface.html)

[In] Specifies the x-coordinate of the mouse pointer, relative to the control, at the moment when the event occurs.

y
 As
 [long](data-types-for-teststand-user-interface.html)

[In] Specifies the y-coordinate of the mouse pointer, relative to the control, at the moment when the event occurs.

#### See Also

[CheckBox.Click](checkbox-click.html)

[CheckBox.MouseDown](checkbox-mousedown.html)

[CheckBox.MouseUp](checkbox-mouseup.html)

[KeyModifiers](keymodifiers.html)

[MouseButtons](mousebuttons.html)

Parent topic:

Events

<!--NI_TOPIC bundle=teststand-api-reference path=tsuiref/checkbox-mouseup.html language=enus -->
## TOPIC 04821: CheckBox.MouseUp

- bundle_id: `teststand-api-reference`
- source_path: `tsuiref/checkbox-mouseup.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsuiref/checkbox-mouseup.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax ControlName_MouseUp( btn, shift, x, y) Applies To CheckBox Purpose Occurs when the user releases the mouse on the control. Parameters btn As Integer [In] Specifies the mouse button pressed to cause this event. You can use any one of the MouseButtons constants. shift As Integer [In] Specifies

### CheckBox.MouseUp

#### Syntax

ControlName_MouseUp( btn, shift, x, y)

#### Applies To

[CheckBox](checkbox.html)

#### Purpose

Occurs when the user releases the mouse on the control.

#### Parameters

btn
 As
 [Integer](data-types-for-teststand-user-interface.html)

[In] Specifies the mouse button pressed to cause this event. You can use any one of the
 [MouseButtons](mousebuttons.html)
 constants.

shift
 As
 [Integer](data-types-for-teststand-user-interface.html)

[In] Specifies a combination of the
 [KeyModifiers](keymodifiers.html)
 constants that specifies the state of the <Shift>, <Ctrl>, and <Alt> keys.

x
 As
 [long](data-types-for-teststand-user-interface.html)

[In] Specifies the x-coordinate of the mouse pointer, relative to the control, at the moment when the event occurs.

y
 As
 [long](data-types-for-teststand-user-interface.html)

[In] Specifies the y-coordinate of the mouse pointer, relative to the control, at the moment when the event occurs.

#### See Also

[CheckBox.Click](checkbox-click.html)

[CheckBox.MouseDown](checkbox-mousedown.html)

[CheckBox.MouseMove](checkbox-mousemove.html)

[KeyModifiers](keymodifiers.html)

[MouseButtons](mousebuttons.html)

Parent topic:

Events

<!--NI_TOPIC bundle=teststand-api-reference path=tsuiref/checkbox-scalewithdpi.html language=enus -->
## TOPIC 04822: CheckBox.ScaleWithDPI

- bundle_id: `teststand-api-reference`
- source_path: `tsuiref/checkbox-scalewithdpi.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsuiref/checkbox-scalewithdpi.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax CheckBox.ScaleWithDPI Data Type Boolean Purpose Specifies how the control scales based on the dots per inch (DPI) setting. Remarks Some environments scale native controls based on the DPI settings of their display, while other environments do not. The TestStand User Interface Controls are des

### CheckBox.ScaleWithDPI

#### Syntax

[CheckBox](checkbox.html).ScaleWithDPI

#### Data Type

[Boolean](data-types-for-teststand-user-interface.html)

#### Purpose

Specifies how the control scales based on the dots per inch (DPI) setting.

#### Remarks

Some environments scale native controls based on the DPI settings of their display, while other environments do not. The TestStand User Interface Controls are designed to work in all environments.

The following are the recommended settings for various platforms:

- LabVIEW, LabWindows/CVI, C#, and Microsoft Visual Basic .NET—Set this property to
 False 
 .
- Active Template Library (ATL)/Microsoft Foundation Class (MFC)—Set this property to
 True 
 .

Parent topic:

Properties

<!--NI_TOPIC bundle=teststand-api-reference path=tsuiref/checkbox-style.html language=enus -->
## TOPIC 04823: CheckBox.Style

- bundle_id: `teststand-api-reference`
- source_path: `tsuiref/checkbox-style.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsuiref/checkbox-style.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax CheckBox.Style Data Type CheckBoxStyles Use the following constants with this data type: CheckBoxStyle_Button –(Value: 1) Specifies that the CheckBox control is a toggle button that you can toggle to an up or down state. CheckBoxStyle_Normal –(Value: 0) Specifies that the CheckBox control is

### CheckBox.Style

#### Syntax

[CheckBox](checkbox.html).Style

#### Data Type

[CheckBoxStyles](checkboxstyles.html)

Use the following constants with this data type:

- CheckBoxStyle_Button 
 –(Value: 1) Specifies that the CheckBox control is a toggle button that you can toggle to an up or down state.
- CheckBoxStyle_Normal 
 –(Value: 0) Specifies that the CheckBox control is normal in appearance.

#### Purpose

Specifies the appearance of the control.

Parent topic:

Properties

<!--NI_TOPIC bundle=teststand-api-reference path=tsuiref/checkbox-textalign.html language=enus -->
## TOPIC 04824: CheckBox.TextAlign

- bundle_id: `teststand-api-reference`
- source_path: `tsuiref/checkbox-textalign.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsuiref/checkbox-textalign.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax CheckBox.TextAlign Data Type ContentAlignmentStyles Use the following constants with this data type: ContentAlignmentStyle_BottomCenter –(Value: 8) Content is vertically aligned at the bottom and horizontally aligned in the center. ContentAlignmentStyle_BottomLeft –(Value: 6) Content is verti

### CheckBox.TextAlign

#### Syntax

[CheckBox](checkbox.html).TextAlign

#### Data Type

[ContentAlignmentStyles](contentalignmentstyles.html)

Use the following constants with this data type:

- ContentAlignmentStyle_BottomCenter 
 –(Value: 8) Content is vertically aligned at the bottom and horizontally aligned in the center.
- ContentAlignmentStyle_BottomLeft 
 –(Value: 6) Content is vertically aligned at the bottom and horizontally aligned on the left.
- ContentAlignmentStyle_BottomRight 
 –(Value: 7) Content is vertically aligned at the bottom and horizontally aligned on the right.
- ContentAlignmentStyle_MiddleCenter 
 –(Value: 2) Content is vertically aligned in the middle and horizontally aligned in the center.
- ContentAlignmentStyle_MiddleLeft 
 –(Value: 0) Content is vertically aligned in the middle and horizontally aligned on the left.
- ContentAlignmentStyle_MiddleRight 
 –(Value: 1) Content is vertically aligned in the middle and horizontally aligned on the right.
- ContentAlignmentStyle_TopCenter 
 –(Value: 5) Content is vertically aligned at the top and horizontally aligned in the center.
- ContentAlignmentStyle_TopLeft 
 –(Value: 3) Content is vertically aligned at the top and horizontally aligned on the left.
- ContentAlignmentStyle_TopRight 
 –(Value: 4) Content is vertically aligned at the top and horizontally aligned on the right.

#### Purpose

Specifies the horizontal and vertical alignment of text on a CheckBox control.

#### Remarks

When the style of the control is
 CheckBoxStyle_Normal
 , the control supports only the
 ContentAlignmentStyle_MiddleLeft
 and
 ContentAlignmentStyle_MiddleRight
 values.

#### See Also

[CheckBox.Style](checkbox-style.html)

[CheckBoxStyles](checkboxstyles.html)

Parent topic:

Properties

<!--NI_TOPIC bundle=teststand-api-reference path=tsuiref/checkbox-usemaskcolor.html language=enus -->
## TOPIC 04825: CheckBox.UseMaskColor

- bundle_id: `teststand-api-reference`
- source_path: `tsuiref/checkbox-usemaskcolor.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsuiref/checkbox-usemaskcolor.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax CheckBox.UseMaskColor Data Type Boolean Purpose The control uses the color the CheckBox.MaskColor property specifies as a mask color when this property is True . You can use the mask color to create transparent regions. Remarks This property is used only when the style of the control is Check

### CheckBox.UseMaskColor

#### Syntax

[CheckBox](checkbox.html).UseMaskColor

#### Data Type

[Boolean](data-types-for-teststand-user-interface.html)

#### Purpose

The control uses the color the
 [CheckBox.MaskColor](checkbox-maskcolor.html)
 property specifies as a mask color when this property is
 True
 . You can use the mask color to create transparent regions.

#### Remarks

This property is used only when the style of the control is
 CheckBoxStyle_Button
 .

#### See Also

[CheckBox.MaskColor](checkbox-maskcolor.html)

[CheckBoxStyles](checkboxstyles.html)

Parent topic:

Properties

<!--NI_TOPIC bundle=teststand-api-reference path=tsuiref/checkbox.html language=enus -->
## TOPIC 04826: CheckBox

- bundle_id: `teststand-api-reference`
- source_path: `tsuiref/checkbox.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsuiref/checkbox.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Connect a manager control to a CheckBox control so users can toggle the state of a common user interface command, such as Break on Step Failure . When you connect to a command, the CheckBox control automatically updates the caption text, visibility, and enabled state. When you enable the checkbox, t

### CheckBox

Connect a manager control to a CheckBox control so users can toggle the state of a common user interface command, such as
 Break on Step Failure
 . When you connect to a command, the CheckBox control automatically updates the caption text, visibility, and enabled state. When you enable the checkbox, the checkbox executes the command, which toggles the state of the command.

The CheckBox control supports the following commands:

- CommandKind_BreakonFirstStep
- CommandKind_BreakonSequenceFailure
- CommandKind_BreakonStepFailure
- CommandKind_ToggleBreakPoint
- CommandKind_TracingEnabled

#### Properties

| BackColor |
| --- |
| Caption |
| Checked |
| Enabled |
| Font |
| FontSource |
| ForeColor |
| hWnd (Read Only) |
| Image |
| ImageAlign |
| MaskColor |
| ScaleWithDPI |
| Style |
| TextAlign |
| UseMaskColor |

#### Method

| Localize |
| --- |

#### Events

| Click |
| --- |
| ConnectionActivity |
| KeyDown |
| KeyPress |
| KeyUp |
| MouseDown |
| MouseMove |
| MouseUp |

#### See Also

[ApplicationMgr.ConnectCommand](applicationmgr-connectcommand.html)

[CommandKinds](commandkinds.html)

[ExecutionViewMgr.ConnectCommand](executionviewmgr-connectcommand.html)

[SequenceFileViewMgr.ConnectCommand](sequencefileviewmgr-connectcommand.html)

Parent topic:

TestStand User Interface Controls

<!--NI_TOPIC bundle=teststand-api-reference path=tsuiref/checkboxstyles.html language=enus -->
## TOPIC 04827: CheckBoxStyles

- bundle_id: `teststand-api-reference`
- source_path: `tsuiref/checkboxstyles.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsuiref/checkboxstyles.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Use these constants with CheckBox.Style to specify the style of the CheckBox control. CheckBoxStyle_Button –(Value: 1) Specifies that the CheckBox control is a toggle button that you can toggle to an up or down state. CheckBoxStyle_Normal –(Value: 0) Specifies that the CheckBox control is normal in

### CheckBoxStyles

Use these constants with
 [CheckBox.Style](checkbox-style.html)
 to specify the style of the CheckBox control.

- CheckBoxStyle_Button 
 –(Value: 1) Specifies that the CheckBox control is a toggle button that you can toggle to an up or down state.
- CheckBoxStyle_Normal 
 –(Value: 0) Specifies that the CheckBox control is normal in appearance.

#### See Also

[CheckBox.Style](checkbox-style.html)

Parent topic:

Core UI Enumerations

<!--NI_TOPIC bundle=teststand-api-reference path=tsuiref/combobox-change.html language=enus -->
## TOPIC 04828: ComboBox.Change

- bundle_id: `teststand-api-reference`
- source_path: `tsuiref/combobox-change.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsuiref/combobox-change.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax ControlName_Change Applies To ComboBox Purpose Occurs when the contents of a control change.

### ComboBox.Change

#### Syntax

ControlName_Change

#### Applies To

[ComboBox](combobox.html)

#### Purpose

Occurs when the contents of a control change.

Parent topic:

Events

<!--NI_TOPIC bundle=teststand-api-reference path=tsuiref/combobox-click.html language=enus -->
## TOPIC 04829: ComboBox.Click

- bundle_id: `teststand-api-reference`
- source_path: `tsuiref/combobox-click.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsuiref/combobox-click.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax ControlName_Click Applies To ComboBox Purpose Occurs when you press and release the mouse on the control.

### ComboBox.Click

#### Syntax

ControlName_Click

#### Applies To

[ComboBox](combobox.html)

#### Purpose

Occurs when you press and release the mouse on the control.

Parent topic:

Events

<!--NI_TOPIC bundle=teststand-api-reference path=tsuiref/combobox-connectionactivity.html language=enus -->
## TOPIC 04830: ComboBox.ConnectionActivity

- bundle_id: `teststand-api-reference`
- source_path: `tsuiref/combobox-connectionactivity.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsuiref/combobox-connectionactivity.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax ControlName_ConnectionActivity( activity) Applies To ComboBox Purpose Occurs after the connection to a manager control makes a change to a user interface control. Parameters activity As ConnectionActivityTypes [In] Specifies the type of change.

### ComboBox.ConnectionActivity

#### Syntax

ControlName_ConnectionActivity( activity)

#### Applies To

[ComboBox](combobox.html)

#### Purpose

Occurs after the connection to a manager control makes a change to a user interface control.

#### Parameters

activity
 As
 [ConnectionActivityTypes](connectionactivitytypes.html)

[In] Specifies the type of change.

Parent topic:

Events

<!--NI_TOPIC bundle=teststand-api-reference path=tsuiref/combobox-count.html language=enus -->
## TOPIC 04831: ComboBox.Count

- bundle_id: `teststand-api-reference`
- source_path: `tsuiref/combobox-count.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsuiref/combobox-count.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax ComboBox.Count Data Type Long Purpose Returns the number of items in the ComboBox. See Also ComboBox.GetItemText ComboBox.ItemIndex

### ComboBox.Count

#### Syntax

[ComboBox](combobox.html).Count

#### Data Type

[Long](data-types-for-teststand-user-interface.html)

#### Purpose

Returns the number of items in the ComboBox.

#### See Also

[ComboBox.GetItemText](combobox-getitemtext.html)

[ComboBox.ItemIndex](combobox-itemindex.html)

Parent topic:

Properties

<!--NI_TOPIC bundle=teststand-api-reference path=tsuiref/combobox-dropdown.html language=enus -->
## TOPIC 04832: ComboBox.DropDown

- bundle_id: `teststand-api-reference`
- source_path: `tsuiref/combobox-dropdown.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsuiref/combobox-dropdown.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax ControlName_DropDown Applies To ComboBox Purpose Occurs when the list portion of the control is about to drop down. The ComboBox control does not allow you to populate the items in the drop-down list.

### ComboBox.DropDown

#### Syntax

ControlName_DropDown

#### Applies To

[ComboBox](combobox.html)

#### Purpose

Occurs when the list portion of the control is about to drop down.

Note

Parent topic:

Events

<!--NI_TOPIC bundle=teststand-api-reference path=tsuiref/combobox-enabled.html language=enus -->
## TOPIC 04833: ComboBox.Enabled

- bundle_id: `teststand-api-reference`
- source_path: `tsuiref/combobox-enabled.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsuiref/combobox-enabled.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax ComboBox.Enabled Data Type Boolean Purpose The control responds to user input only when this property is True . See Also ComboBox.ReadOnly

### ComboBox.Enabled

#### Syntax

[ComboBox](combobox.html).Enabled

#### Data Type

[Boolean](data-types-for-teststand-user-interface.html)

#### Purpose

The control responds to user input only when this property is
 True
 .

#### See Also

[ComboBox.ReadOnly](combobox-readonly.html)

Parent topic:

Properties

<!--NI_TOPIC bundle=teststand-api-reference path=tsuiref/combobox-font.html language=enus -->
## TOPIC 04834: ComboBox.Font

- bundle_id: `teststand-api-reference`
- source_path: `tsuiref/combobox-font.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsuiref/combobox-font.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax ComboBox.Font Data Type Font Purpose Specifies the font for the control when the value of the ComboBox.FontSource property is FontSource_UseFontProperty . See Also ComboBox.FontSource

### ComboBox.Font

#### Syntax

[ComboBox](combobox.html).Font

#### Data Type

[Font](data-types-for-teststand-user-interface.html)

#### Purpose

Specifies the font for the control when the value of the
 [ComboBox.FontSource](combobox-fontsource.html)
 property is
 FontSource_UseFontProperty
 .

#### See Also

[ComboBox.FontSource](combobox-fontsource.html)

Parent topic:

Properties

<!--NI_TOPIC bundle=teststand-api-reference path=tsuiref/combobox-fontsource.html language=enus -->
## TOPIC 04835: ComboBox.FontSource

- bundle_id: `teststand-api-reference`
- source_path: `tsuiref/combobox-fontsource.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsuiref/combobox-fontsource.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax ComboBox.FontSource Data Type FontSources Use the following constants with this data type: FontSource_UseContainerFont –(Value: 2) The font the container supplies. FontSource_UseFontProperty –(Value: 0) A corresponding Font property of the control determines the font. FontSource_UseGUIFont –(

### ComboBox.FontSource

#### Syntax

[ComboBox](combobox.html).FontSource

#### Data Type

[FontSources](fontsources.html)

Use the following constants with this data type:

- FontSource_UseContainerFont 
 –(Value: 2) The font the container supplies.
- FontSource_UseFontProperty 
 –(Value: 0) A corresponding
 Font 
 property of the control determines the font.
- FontSource_UseGUIFont 
 –(Value: 1) The default system font for user interface objects.
- FontSource_UseIconFont 
 –(Value: 5) The system font for an icon title.
- FontSource_UseInactiveTitlebarFont 
 –(Value: 4) The system font for an inactive titlebar.
- FontSource_UseMenuFont 
 –(Value: 6) The system font for a menu.
- FontSource_UseMessageBoxFont 
 –(Value: 7) The system font for a message box.
- FontSource_UsePaletteTitleFont 
 –(Value: 8) The system font for the title of a Tools window.
- FontSource_UseSelectedItemsFont 
 –(Value: 9) The system font for the selected menu items.
- FontSource_UseSystemFixedWidthFont 
 –(Value: 11) The system font for monospaced text.
- FontSource_UseTitlebarFont 
 –(Value: 3) The system font for a title bar.
- FontSource_UseToolTipFont 
 –(Value: 10) The system font for tooltips and status bars.
- FontSource_UseUIStyleFont 
 –(Value: 12) The font the
 UIStyle 
 object supplies.

#### Purpose

Specifies the font the control uses. The default value for this property is
 FontSource_UseGUIFont
 .

#### Remarks

When the value of this property is
 FontSource_UseFontProperty
 , the corresponding
 Font
 property specifies the particular font the control uses. Otherwise, the control uses the font from the source this property specifies. Refer to the
 [FontSources](fontsources.html)
 enumeration for the list of valid font sources.

Set this property to a value other than
 FontSource_UseFontProperty
 when you expect the font the
 [ComboBox.Font](combobox-font.html)
 property specifies to not be present on a computer at run time. For example, a font present on an English version of the Microsoft Windows operating system might not be present on a Japanese version of the Windows operating system.

#### See Also

[ComboBox.Font](combobox-font.html)

[FontSources](fontsources.html)

Parent topic:

Properties

<!--NI_TOPIC bundle=teststand-api-reference path=tsuiref/combobox-getitemtext.html language=enus -->
## TOPIC 04836: ComboBox.GetItemText

- bundle_id: `teststand-api-reference`
- source_path: `tsuiref/combobox-getitemtext.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsuiref/combobox-getitemtext.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax ComboBox.GetItemText( itemIdx) Return Value String Purpose Returns the text of the item at a specified index. Parameters itemIdx As Long [In] Specifies the zero-based index of the item to retrieve. Pass -1 to obtain the text of the currently selected item. See Also ComboBox.Count ComboBox.Ite

### ComboBox.GetItemText

#### Syntax

[ComboBox](combobox.html).GetItemText( itemIdx)

#### Return Value

[String](data-types-for-teststand-user-interface.html)

#### Purpose

Returns the text of the item at a specified index.

#### Parameters

itemIdx
 As
 [Long](data-types-for-teststand-user-interface.html)

[In] Specifies the zero-based index of the item to retrieve. Pass
 -1
 to obtain the text of the currently selected item.

#### See Also

[ComboBox.Count](combobox-count.html)

[ComboBox.ItemIndex](combobox-itemindex.html)

Parent topic:

Methods

<!--NI_TOPIC bundle=teststand-api-reference path=tsuiref/combobox-heightwithdropdown.html language=enus -->
## TOPIC 04837: ComboBox.HeightWithDropDown

- bundle_id: `teststand-api-reference`
- source_path: `tsuiref/combobox-heightwithdropdown.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsuiref/combobox-heightwithdropdown.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax ComboBox.HeightWithDropDown Data Type Long Purpose Specifies the maximum height of the edit box and drop-down list. Remarks When the total height of all the items in the drop-down list exceeds the value of this property, the drop-down list uses a vertical scrollbar. This value cannot be less

### ComboBox.HeightWithDropDown

#### Syntax

[ComboBox](combobox.html).HeightWithDropDown

#### Data Type

[Long](data-types-for-teststand-user-interface.html)

#### Purpose

Specifies the maximum height of the edit box and drop-down list.

#### Remarks

When the total height of all the items in the drop-down list exceeds the value of this property, the drop-down list uses a vertical scrollbar. This value cannot be less than 100 pixels.

Parent topic:

Properties

<!--NI_TOPIC bundle=teststand-api-reference path=tsuiref/combobox-hwnd.html language=enus -->
## TOPIC 04838: ComboBox.hWnd

- bundle_id: `teststand-api-reference`
- source_path: `tsuiref/combobox-hwnd.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsuiref/combobox-hwnd.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax ComboBox.hWnd Data Type Long Purpose Returns a Window handle for the control. Remarks You can use the returned Window handle with the Microsoft Windows API functions. Using Windows API functions with this property can cause undefined behavior.

### ComboBox.hWnd

#### Syntax

[ComboBox](combobox.html).hWnd

#### Data Type

[Long](data-types-for-teststand-user-interface.html)

#### Purpose

Returns a Window handle for the control.

#### Remarks

You can use the returned Window handle with the Microsoft Windows API functions.

Note

Parent topic:

Properties

<!--NI_TOPIC bundle=teststand-api-reference path=tsuiref/combobox-iconsize.html language=enus -->
## TOPIC 04839: ComboBox.IconSize

- bundle_id: `teststand-api-reference`
- source_path: `tsuiref/combobox-iconsize.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsuiref/combobox-iconsize.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax ComboBox.IconSize Data Type Long Purpose Specifies the size, in pixels, of the icon displayed in the control. Remarks The value of this property cannot be less than 1 or greater than 96. Icons are always square. For example, when you specify an icon size of 32, the dimensions of the icon are

### ComboBox.IconSize

#### Syntax

[ComboBox](combobox.html).IconSize

#### Data Type

[Long](data-types-for-teststand-user-interface.html)

#### Purpose

Specifies the size, in pixels, of the icon displayed in the control.

#### Remarks

The value of this property cannot be less than 1 or greater than 96.

Icons are always square. For example, when you specify an icon size of 32, the dimensions of the icon are 32 × 32 pixels.

Parent topic:

Properties

<!--NI_TOPIC bundle=teststand-api-reference path=tsuiref/combobox-itemindex.html language=enus -->
## TOPIC 04840: ComboBox.ItemIndex

- bundle_id: `teststand-api-reference`
- source_path: `tsuiref/combobox-itemindex.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsuiref/combobox-itemindex.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax ComboBox.ItemIndex Data Type Long Purpose Specifies the zero-based index of the currently selected item in the control. Remarks A value of -1 indicates no item is currently selected, or the user entered a new value not in the list. See Also ComboBox.Count ComboBox.GetItemText

### ComboBox.ItemIndex

#### Syntax

[ComboBox](combobox.html).ItemIndex

#### Data Type

[Long](data-types-for-teststand-user-interface.html)

#### Purpose

Specifies the zero-based index of the currently selected item in the control.

#### Remarks

A value of
 -1
 indicates no item is currently selected, or the user entered a new value not in the list.

#### See Also

[ComboBox.Count](combobox-count.html)

[ComboBox.GetItemText](combobox-getitemtext.html)

Parent topic:

Properties

<!--NI_TOPIC bundle=teststand-api-reference path=tsuiref/combobox-keydown.html language=enus -->
## TOPIC 04841: ComboBox.KeyDown

- bundle_id: `teststand-api-reference`
- source_path: `tsuiref/combobox-keydown.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsuiref/combobox-keydown.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax ControlName_KeyDown( keyCode, shift) Applies To ComboBox Purpose Occurs when the user presses a key while the control has input focus. This event occurs before the ComboBox.KeyPress event. Parameters keyCode As Integer [In/Out] Specifies the KeyCodes constant of the key the user pressed. shif

### ComboBox.KeyDown

#### Syntax

ControlName_KeyDown( keyCode, shift)

#### Applies To

[ComboBox](combobox.html)

#### Purpose

Occurs when the user presses a key while the control has input focus. This event occurs before the
 [ComboBox.KeyPress](combobox-keypress.html)
 event.

#### Parameters

keyCode
 As
 [Integer](data-types-for-teststand-user-interface.html)

[In/Out] Specifies the
 [KeyCodes](keycodes.html)
 constant of the key the user pressed.

shift
 As
 [Integer](data-types-for-teststand-user-interface.html)

[In] Specifies a combination of the
 [KeyModifiers](keymodifiers.html)
 constants that specifies the state of the <Shift>, <Ctrl>, and <Alt> keys.

#### See Also

[ComboBox.KeyPress](combobox-keypress.html)

[ComboBox.KeyUp](combobox-keyup.html)

[KeyCodes](keycodes.html)

[KeyModifiers](keymodifiers.html)

Parent topic:

Events

<!--NI_TOPIC bundle=teststand-api-reference path=tsuiref/combobox-keypress.html language=enus -->
## TOPIC 04842: ComboBox.KeyPress

- bundle_id: `teststand-api-reference`
- source_path: `tsuiref/combobox-keypress.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsuiref/combobox-keypress.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax ControlName_KeyPress( keyAscii) Applies To ComboBox Purpose Occurs when the user presses a key while a control is active. This event occurs after the ComboBox.KeyDown event. Parameters keyAscii As Integer [In/Out] Specifies the ASCII value of the pressed key. See Also ComboBox.KeyDown ComboBo

### ComboBox.KeyPress

#### Syntax

ControlName_KeyPress( keyAscii)

#### Applies To

[ComboBox](combobox.html)

#### Purpose

Occurs when the user presses a key while a control is active. This event occurs after the
 [ComboBox.KeyDown](combobox-keydown.html)
 event.

#### Parameters

keyAscii
 As
 [Integer](data-types-for-teststand-user-interface.html)

[In/Out] Specifies the ASCII value of the pressed key.

#### See Also

[ComboBox.KeyDown](combobox-keydown.html)

[ComboBox.KeyUp](combobox-keyup.html)

Parent topic:

Events

<!--NI_TOPIC bundle=teststand-api-reference path=tsuiref/combobox-keyup.html language=enus -->
## TOPIC 04843: ComboBox.KeyUp

- bundle_id: `teststand-api-reference`
- source_path: `tsuiref/combobox-keyup.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsuiref/combobox-keyup.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax ControlName_KeyUp( keyCode, shift) Applies To ComboBox Purpose Occurs when the user releases a key while the control has input focus. Parameters keyCode As Integer [In] Specifies the KeyCodes constant of the key the user pressed. shift As Integer [In] Specifies a combination of the KeyModifie

### ComboBox.KeyUp

#### Syntax

ControlName_KeyUp( keyCode, shift)

#### Applies To

[ComboBox](combobox.html)

#### Purpose

Occurs when the user releases a key while the control has input focus.

#### Parameters

keyCode
 As
 [Integer](data-types-for-teststand-user-interface.html)

[In] Specifies the
 [KeyCodes](keycodes.html)
 constant of the key the user pressed.

shift
 As
 [Integer](data-types-for-teststand-user-interface.html)

[In] Specifies a combination of the
 [KeyModifiers](keymodifiers.html)
 constants that specifies the state of the <Shift>, <Ctrl>, and <Alt> keys.

#### See Also

[ComboBox.KeyDown](combobox-keydown.html)

[ComboBox.KeyPress](combobox-keypress.html)

[KeyCodes](keycodes.html)

[KeyModifiers](keymodifiers.html)

Parent topic:

Events

<!--NI_TOPIC bundle=teststand-api-reference path=tsuiref/combobox-mouseicon.html language=enus -->
## TOPIC 04844: ComboBox.MouseIcon

- bundle_id: `teststand-api-reference`
- source_path: `tsuiref/combobox-mouseicon.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsuiref/combobox-mouseicon.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax ComboBox.MouseIcon Data Type Picture Purpose Specifies a custom mouse icon for the control. Remarks The control displays the specified picture as the cursor when the value of the ComboBox.MousePointer property is MousePointer_Custom . When you set this property to NULL , the value of the Comb

### ComboBox.MouseIcon

#### Syntax

[ComboBox](combobox.html).MouseIcon

#### Data Type

[Picture](data-types-for-teststand-user-interface.html)

#### Purpose

Specifies a custom mouse icon for the control.

#### Remarks

The control displays the specified picture as the cursor when the value of the
 [ComboBox.MousePointer](combobox-mousepointer.html)
 property is
 MousePointer_Custom
 . When you set this property to
 NULL
 , the value of the
 ComboBox.MousePointer
 property changes to
 MousePointer_Default
 .

Note

#### See Also

[ComboBox.MousePointer](combobox-mousepointer.html)

[MousePointerStyles](mousepointerstyles.html)

Parent topic:

Properties

<!--NI_TOPIC bundle=teststand-api-reference path=tsuiref/combobox-mousepointer.html language=enus -->
## TOPIC 04845: ComboBox.MousePointer

- bundle_id: `teststand-api-reference`
- source_path: `tsuiref/combobox-mousepointer.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsuiref/combobox-mousepointer.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax ComboBox.MousePointer Data Type MousePointerStyles Use the following constants with this data type: MousePointer_Arrow –(Value: 1) MousePointer_ArrowHourGlass –(Value: 11) MousePointer_ArrowQuestion –(Value: 12) MousePointer_Crosshair –(Value: 2) MousePointer_Custom –(Value: 99) MousePointer_

### ComboBox.MousePointer

#### Syntax

[ComboBox](combobox.html).MousePointer

#### Data Type

[MousePointerStyles](mousepointerstyles.html)

Use the following constants with this data type:

- MousePointer_Arrow 
 –(Value: 1)
- MousePointer_ArrowHourGlass 
 –(Value: 11)
- MousePointer_ArrowQuestion 
 –(Value: 12)
- MousePointer_Crosshair 
 –(Value: 2)
- MousePointer_Custom 
 –(Value: 99)
- MousePointer_Default 
 –(Value: 0)
- MousePointer_HourGlass 
 –(Value: 9)
- MousePointer_Ibeam 
 –(Value: 3)
- MousePointer_NoDrop 
 –(Value: 10)
- MousePointer_SizeAll 
 –(Value: 13)
- MousePointer_SizeNESW 
 –(Value: 4)
- MousePointer_SizeNS 
 –(Value: 5)
- MousePointer_SizeNWSE 
 –(Value: 6)
- MousePointer_SizeWE 
 –(Value: 7)
- MousePointer_UpArrow 
 –(Value: 8)

#### Purpose

Specifies the appearance of the mouse cursor when the cursor is over the control.

#### Remarks

When the parameter is
 MousePointer_Custom
 , the mouse cursor is the picture the
 [ComboBox.MouseIcon](combobox-mouseicon.html)
 property specifies.

#### See Also

[ComboBox.MouseIcon](combobox-mouseicon.html)

Parent topic:

Properties

<!--NI_TOPIC bundle=teststand-api-reference path=tsuiref/combobox-readonly.html language=enus -->
## TOPIC 04846: ComboBox.ReadOnly

- bundle_id: `teststand-api-reference`
- source_path: `tsuiref/combobox-readonly.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsuiref/combobox-readonly.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax ComboBox.ReadOnly Data Type Boolean Purpose Specifies whether the control can be edited. See Also ComboBox.Enabled

### ComboBox.ReadOnly

#### Syntax

[ComboBox](combobox.html).ReadOnly

#### Data Type

[Boolean](data-types-for-teststand-user-interface.html)

#### Purpose

Specifies whether the control can be edited.

#### See Also

[ComboBox.Enabled](combobox-enabled.html)

Parent topic:

Properties

<!--NI_TOPIC bundle=teststand-api-reference path=tsuiref/combobox-scalewithdpi.html language=enus -->
## TOPIC 04847: ComboBox.ScaleWithDPI

- bundle_id: `teststand-api-reference`
- source_path: `tsuiref/combobox-scalewithdpi.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsuiref/combobox-scalewithdpi.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax ComboBox.ScaleWithDPI Data Type Boolean Purpose Specifies how the control scales based on the dots per inch (DPI) setting. Remarks Some environments scale native controls based on the DPI settings of their display, while other environments do not. The TestStand User Interface controls are des

### ComboBox.ScaleWithDPI

#### Syntax

[ComboBox](combobox.html).ScaleWithDPI

#### Data Type

[Boolean](data-types-for-teststand-user-interface.html)

#### Purpose

Specifies how the control scales based on the dots per inch (DPI) setting.

#### Remarks

Some environments scale native controls based on the DPI settings of their display, while other environments do not. The TestStand User Interface controls are designed to work in all environments.

The following are the recommended settings for various platforms:

- LabVIEW, LabWindows/CVI, C#, and Microsoft Visual Basic .NET—Set this property to
 False 
 .
- Active Template Library (ATL)/Microsoft Foundation Class (MFC)—Set this property to
 True 
 .

Parent topic:

Properties

<!--NI_TOPIC bundle=teststand-api-reference path=tsuiref/combobox-showimages.html language=enus -->
## TOPIC 04848: ComboBox.ShowImages

- bundle_id: `teststand-api-reference`
- source_path: `tsuiref/combobox-showimages.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsuiref/combobox-showimages.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax ComboBox.ShowImages Data Type Boolean Purpose Specifies whether the control shows images. Remarks The edit box does not show images when the style is ComboBoxStyle_DropDownCombo . See Also ComboBoxStyles

### ComboBox.ShowImages

#### Syntax

[ComboBox](combobox.html).ShowImages

#### Data Type

[Boolean](data-types-for-teststand-user-interface.html)

#### Purpose

Specifies whether the control shows images.

#### Remarks

The edit box does not show images when the style is
 ComboBoxStyle_DropDownCombo
 .

#### See Also

[ComboBoxStyles](comboboxstyles.html)

Parent topic:

Properties

<!--NI_TOPIC bundle=teststand-api-reference path=tsuiref/combobox-style.html language=enus -->
## TOPIC 04849: ComboBox.Style

- bundle_id: `teststand-api-reference`
- source_path: `tsuiref/combobox-style.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsuiref/combobox-style.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax ComboBox.Style Data Type ComboBoxStyles Use the following constants with this data type: ComboBoxStyle_DropDownCombo –(Value: 0) Includes a drop-down list and an edit box. You can select from the list or type in the edit box. ComboBoxStyle_DropDownList –(Value: 2) Allows selection only from t

### ComboBox.Style

#### Syntax

[ComboBox](combobox.html).Style

#### Data Type

[ComboBoxStyles](comboboxstyles.html)

Use the following constants with this data type:

- ComboBoxStyle_DropDownCombo 
 –(Value: 0) Includes a drop-down list and an edit box. You can select from the list or type in the edit box.
- ComboBoxStyle_DropDownList 
 –(Value: 2) Allows selection only from the drop-down list.

#### Purpose

Specifies the appearance of the control.

Parent topic:

Properties

<!--NI_TOPIC bundle=teststand-api-reference path=tsuiref/combobox-tooltipvisible.html language=enus -->
## TOPIC 04850: ComboBox.ToolTipVisible

- bundle_id: `teststand-api-reference`
- source_path: `tsuiref/combobox-tooltipvisible.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsuiref/combobox-tooltipvisible.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax ComboBox.ToolTipVisible Data Type Boolean Purpose Specifies whether the control shows tooltips.

### ComboBox.ToolTipVisible

#### Syntax

[ComboBox](combobox.html).ToolTipVisible

#### Data Type

[Boolean](data-types-for-teststand-user-interface.html)

#### Purpose

Specifies whether the control shows tooltips.

Parent topic:

Properties

<!--NI_TOPIC bundle=teststand-api-reference path=tsuiref/combobox.html language=enus -->
## TOPIC 04851: ComboBox

- bundle_id: `teststand-api-reference`
- source_path: `tsuiref/combobox.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsuiref/combobox.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Connect a SequenceFileView Manager or ExecutionView Manager control to a ComboBox control so users can view or select from a list of sequence files, sequences, step groups, steps, executions, threads, or stack frames. Connect an Application Manager control to a ComboBox control so users can view or

### ComboBox

Connect a
 [SequenceFileView Manager](sequencefileviewmgr.html)
 or
 [ExecutionView Manager](executionviewmgr.html)
 control to a ComboBox control so users can view or select from a list of sequence files, sequences, step groups, steps, executions, threads, or stack frames. Connect an
 [Application Manager](applicationmgr.html)
 control to a ComboBox control so users can view or select the default adapter of the TestStand Engine.

Use the ComboBox control to connect to and display the
 [ExecutionViewMgrConnections.ExecutionList](executionviewmgrconnections-executionlist.html)
 ,
 [ExecutionViewMgrConnections.CallStack](executionviewmgrconnections-callstack.html)
 , and
 [ExecutionViewMgrConnections.ThreadList](executionviewmgrconnections-threadlist.html)
 properties in the ExecutionView Manager control and the
 [SequenceFileViewMgrConnections.SequenceList](sequencefileviewmgrconnections-sequencelist.html)
 ,
 [SequenceFileViewMgrConnections.SequenceFileList](sequencefileviewmgrconnections-sequencefileli.html)
 , and
 [SequenceFileViewMgrConnections.StepGroupList](sequencefileviewmgrconnections-stepgrouplist.html)
 properties in the SequenceFileView Manager control.

Selecting an item in the ComboBox control updates the application based on the type of data the connection specifies.

Note

#### Properties

| Count (Read Only) |
| --- |
| Enabled |
| Font |
| FontSource |
| HeightWithDropDown |
| hWnd (Read Only) |
| IconSize |
| ItemIndex |
| MouseIcon |
| MousePointer |
| ReadOnly |
| ScaleWithDPI |
| ShowImages |
| Style |
| ToolTipVisible |

#### Method

| GetItemText |
| --- |

#### Events

| Change |
| --- |
| Click |
| ConnectionActivity |
| DropDown |
| KeyDown |
| KeyPress |
| KeyUp |

#### See Also

[ExecutionViewMgr](executionviewmgr.html)

[ExecutionViewMgr.ConnectCallStack](executionviewmgr-connectcallstack.html)

[ExecutionViewMgr.ConnectExecutionList](executionviewmgr-connectexecutionlist.html)

[ExecutionViewMgr.ConnectThreadList](executionviewmgr-connectthreadlist.html)

[SequenceFileViewMgr](sequencefileviewmgr.html)

[SequenceFileViewMgr.ConnectSequenceFileList](sequencefileviewmgr-connectsequencefilelist.html)

[SequenceFileViewMgr.ConnectSequenceList](sequencefileviewmgr-connectsequencelist.html)

[SequenceFileViewMgr.ConnectStepGroupList](sequencefileviewmgr-connectstepgrouplist.html)

Parent topic:

TestStand User Interface Controls

<!--NI_TOPIC bundle=teststand-api-reference path=tsuiref/comboboxstyles.html language=enus -->
## TOPIC 04852: ComboBoxStyles

- bundle_id: `teststand-api-reference`
- source_path: `tsuiref/comboboxstyles.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsuiref/comboboxstyles.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Use these constants with the ComboBox.Style property. ComboBoxStyle_DropDownCombo –(Value: 0) Includes a drop-down list and an edit box. You can select from the list or type in the edit box. ComboBoxStyle_DropDownList –(Value: 2) Allows selection only from the drop-down list. See Also ComboBox.Heigh

### ComboBoxStyles

Use these constants with the
 [ComboBox.Style](combobox-style.html)
 property.

- ComboBoxStyle_DropDownCombo 
 –(Value: 0) Includes a drop-down list and an edit box. You can select from the list or type in the edit box.
- ComboBoxStyle_DropDownList 
 –(Value: 2) Allows selection only from the drop-down list.

#### See Also

[ComboBox.HeightWithDropDown](combobox-heightwithdropdown.html)

[ComboBox.Style](combobox-style.html)

Parent topic:

Core UI Enumerations

<!--NI_TOPIC bundle=teststand-api-reference path=tsuiref/command-enabled.html language=enus -->
## TOPIC 04853: Command.Enabled

- bundle_id: `teststand-api-reference`
- source_path: `tsuiref/command-enabled.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsuiref/command-enabled.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax Command.Enabled Data Type Boolean Purpose Specifies to enable or disable the menu item or user interface element that invokes the command. Remarks The command computes the value of this property according to the kind of command and the current state of the items to which the command applies.

### Command.Enabled

#### Syntax

[Command](command.html).Enabled

#### Data Type

[Boolean](data-types-for-teststand-user-interface.html)

#### Purpose

Specifies to enable or disable the menu item or user interface element that invokes the command.

#### Remarks

The command computes the value of this property according to the kind of command and the current state of the items to which the command applies. However, when you set this property, the command returns only the property values that you set for the remainder of the life of the Command object.

#### See Also

[Command.Visible](command-visible.html)

Parent topic:

Properties

<!--NI_TOPIC bundle=teststand-api-reference path=tsuiref/command-entrypoint.html language=enus -->
## TOPIC 04854: Command.EntryPoint

- bundle_id: `teststand-api-reference`
- source_path: `tsuiref/command-entrypoint.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsuiref/command-entrypoint.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax Command.EntryPoint Data Type EntryPoint Purpose Returns an EntryPoint object that represents an Execution or Configuration entry point for a CommandKind_RunEntryPoint command. See Also Command.EntryPointIndex EntryPoint

### Command.EntryPoint

#### Syntax

[Command](command.html).EntryPoint

#### Data Type

[EntryPoint](entrypoint.html)

#### Purpose

Returns an
 [EntryPoint](entrypoint.html)
 object that represents an Execution or Configuration entry point for a
 [CommandKind_RunEntryPoint](commandkinds.html)
 command.

#### See Also

[Command.EntryPointIndex](command-entrypointindex.html)

[EntryPoint](entrypoint.html)

Parent topic:

Properties

<!--NI_TOPIC bundle=teststand-api-reference path=tsuiref/command-entrypointindex.html language=enus -->
## TOPIC 04855: Command.EntryPointIndex

- bundle_id: `teststand-api-reference`
- source_path: `tsuiref/command-entrypointindex.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsuiref/command-entrypointindex.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax Command.EntryPointIndex Data Type Long Purpose Returns the index of an Execution or Configuration entry point for a CommandKind_RunEntryPoint command. See Also Command.EntryPoint CommandKinds

### Command.EntryPointIndex

#### Syntax

[Command](command.html).EntryPointIndex

#### Data Type

[Long](data-types-for-teststand-user-interface.html)

#### Purpose

Returns the index of an Execution or Configuration entry point for a
 [CommandKind_RunEntryPoint](commandkinds.html)
 command.

#### See Also

[Command.EntryPoint](command-entrypoint.html)

[CommandKinds](commandkinds.html)

Parent topic:

Properties

<!--NI_TOPIC bundle=teststand-api-reference path=tsuiref/command-execute.html language=enus -->
## TOPIC 04856: Command.Execute

- bundle_id: `teststand-api-reference`
- source_path: `tsuiref/command-execute.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsuiref/command-execute.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax Command.Execute( applicationHandlesError) Purpose Executes the action that the command performs. Parameters applicationHandlesError As Boolean [In] Specifies how the method reports an error that occurs when executing the command. When this parameter is False , the method returns the error to

### Command.Execute

#### Syntax

[Command](command.html).Execute( applicationHandlesError)

#### Purpose

Executes the action that the command performs.

#### Parameters

applicationHandlesError
 As
 [Boolean](data-types-for-teststand-user-interface.html)

[In] Specifies how the method reports an error that occurs when executing the command. When this parameter is
 False
 , the method returns the error to the caller. When this parameter is
 True
 , the method calls the
 [ApplicationMgr.ReportError](applicationmgr-reporterror.html)
 event to report the error.

#### See Also

[ApplicationMgr.PostCommandExecute](applicationmgr-postcommandexecute.html)

[ApplicationMgr.PreCommandExecute](applicationmgr-precommandexecute.html)

[ApplicationMgr.ReportError](applicationmgr-reporterror.html)

Parent topic:

Methods

<!--NI_TOPIC bundle=teststand-api-reference path=tsuiref/command-executionviewmgr.html language=enus -->
## TOPIC 04857: Command.ExecutionViewMgr

- bundle_id: `teststand-api-reference`
- source_path: `tsuiref/command-executionviewmgr.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsuiref/command-executionviewmgr.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax Command.ExecutionViewMgr Data Type ExecutionViewMgr Purpose Specifies the ExecutionView Manager control to which the command applies. The enabled, visible, or other states of the command, as well as the entity on which the command operates, vary according to the type of command and the Execut

### Command.ExecutionViewMgr

#### Syntax

[Command](command.html).ExecutionViewMgr

#### Data Type

[ExecutionViewMgr](executionviewmgr.html)

#### Purpose

Specifies the ExecutionView Manager control to which the command applies. The enabled, visible, or other states of the command, as well as the entity on which the command operates, vary according to the type of command and the ExecutionView Manager control selections for the execution, thread, call stack, and steps.

#### Remarks

A value of
 NULL
 specifies that the command does not apply to an ExecutionView Manager control.

#### See Also

[Command.SequenceFileViewMgr](command-sequencefileviewmgr.html)

[Commands.InsertKind](commands-insertkind.html)

[ExecutionViewMgr](executionviewmgr.html)

Parent topic:

Properties

<!--NI_TOPIC bundle=teststand-api-reference path=tsuiref/command-getdisplayname.html language=enus -->
## TOPIC 04858: Command.GetDisplayName

- bundle_id: `teststand-api-reference`
- source_path: `tsuiref/command-getdisplayname.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsuiref/command-getdisplayname.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax Command.GetDisplayName( acceleratorPrefix, includeShortcutText) Return Value String Purpose Returns text that describes the command to the end user. The default text value is localized for the currently selected language. Typically, this text labels the menu item or button that invokes the co

### Command.GetDisplayName

#### Syntax

[Command](command.html).GetDisplayName( acceleratorPrefix, includeShortcutText)

#### Return Value

[String](data-types-for-teststand-user-interface.html)

#### Purpose

Returns text that describes the command to the end user. The default text value is localized for the currently selected language. Typically, this text labels the menu item or button that invokes the command.

#### Parameters

acceleratorPrefix
 As
 [String](data-types-for-teststand-user-interface.html)

[In] Specifies the character(s) you want to precede the accelerator character, when one exists, in the display name the method returns. The accelerator prefix for menu items and button labels varies according to the programming environment. For example, LabVIEW uses
 "_"
 , LabWindows/CVI uses
 "__"
 , and C#, Microsoft Visual C++, and Microsoft Visual Basic .NET use
 "&"
 . When you are not assigning the display name to the label of a user interface element that supports accelerators, pass an empty string.

includeShortcutText
 As
 [Boolean](data-types-for-teststand-user-interface.html)

[In] Pass
 True
 to append characters that represent the shortcut key for the command to the display name the method returns. When the command does not have a shortcut key, the display name remains unchanged.

#### See Also

[Command.SetDisplayName](command-setdisplayname.html)

[StationOptions.Language](../tsapiref/stationoptions-language.html)

Parent topic:

Methods

<!--NI_TOPIC bundle=teststand-api-reference path=tsuiref/command-iconname.html language=enus -->
## TOPIC 04859: Command.IconName

- bundle_id: `teststand-api-reference`
- source_path: `tsuiref/command-iconname.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsuiref/command-iconname.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax Command.IconName Data Type String Purpose Specifies the name of the icon that represents the command. This property specifies an empty string when the command does not have an icon. See Also Engine.Images

### Command.IconName

#### Syntax

[Command](command.html).IconName

#### Data Type

[String](data-types-for-teststand-user-interface.html)

#### Purpose

Specifies the name of the icon that represents the command. This property specifies an empty string when the command does not have an icon.

#### See Also

[Engine.Images](../tsapiref/engine-images.html)

Parent topic:

Properties

<!--NI_TOPIC bundle=teststand-api-reference path=tsuiref/command-isseparator.html language=enus -->
## TOPIC 04860: Command.IsSeparator

- bundle_id: `teststand-api-reference`
- source_path: `tsuiref/command-isseparator.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsuiref/command-isseparator.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax Command.IsSeparator Data Type Boolean Purpose Specifies the menu item or user interface element that represents the command displays as a menu separator or other appropriate user interface divider element when this property is True . Remarks The command computes the value of this property acc

### Command.IsSeparator

#### Syntax

[Command](command.html).IsSeparator

#### Data Type

[Boolean](data-types-for-teststand-user-interface.html)

#### Purpose

Specifies the menu item or user interface element that represents the command displays as a menu separator or other appropriate user interface divider element when this property is
 True
 .

#### Remarks

The command computes the value of this property according to the kind of command. However, when you set this property, the command returns only the property values you set for the remainder of the life of the Command object.

#### See Also

[Commands](commands.html)

Parent topic:

Properties

<!--NI_TOPIC bundle=teststand-api-reference path=tsuiref/command-istoggle.html language=enus -->
## TOPIC 04861: Command.IsToggle

- bundle_id: `teststand-api-reference`
- source_path: `tsuiref/command-istoggle.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsuiref/command-istoggle.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax Command.IsToggle Data Type Boolean Purpose Specifies whether the menu item or user interface element that represents the command can toggle between the on and off states. When this property is True , a menu item that represents the command displays a checkmark the user can enable or disable.

### Command.IsToggle

#### Syntax

[Command](command.html).IsToggle

#### Data Type

[Boolean](data-types-for-teststand-user-interface.html)

#### Purpose

Specifies whether the menu item or user interface element that represents the command can toggle between the on and off states. When this property is
 True
 , a menu item that represents the command displays a checkmark the user can enable or disable.

#### Remarks

The command computes the value of this property according to the kind of command and the current state of the items to which the command applies. However, when you set this property, the command returns only the property values you set for the remainder of the life of the Command object.

#### See Also

[Command.ToggleState](command-togglestate.html)

Parent topic:

Properties

<!--NI_TOPIC bundle=teststand-api-reference path=tsuiref/command-kind.html language=enus -->
## TOPIC 04862: Command.Kind

- bundle_id: `teststand-api-reference`
- source_path: `tsuiref/command-kind.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsuiref/command-kind.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax Command.Kind Data Type CommandKinds Purpose Returns a code that identifies the action the command performs. See Also Commands.InsertKind CommandKinds

### Command.Kind

#### Syntax

[Command](command.html).Kind

#### Data Type

[CommandKinds](commandkinds.html)

#### Purpose

Returns a code that identifies the action the command performs.

#### See Also

[Commands.InsertKind](commands-insertkind.html)

[CommandKinds](commandkinds.html)

Parent topic:

Properties

<!--NI_TOPIC bundle=teststand-api-reference path=tsuiref/command-lvshortcutkey.html language=enus -->
## TOPIC 04863: Command.LVShortcutKey

- bundle_id: `teststand-api-reference`
- source_path: `tsuiref/command-lvshortcutkey.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsuiref/command-lvshortcutkey.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax Command.LVShortcutKey Data Type String Purpose Specifies the shortcut key that invokes the menu item or user interface element that represents the command. Use this value for the shortcut key element of the short cut cluster input to the LabVIEW Set Menu Item Info function when you create a m

### Command.LVShortcutKey

#### Syntax

[Command](command.html).LVShortcutKey

#### Data Type

[String](data-types-for-teststand-user-interface.html)

#### Purpose

Specifies the shortcut key that invokes the menu item or user interface element that represents the command. Use this value for the
 shortcut key
 element of the
 short cut
 cluster input to the LabVIEW
 Set Menu Item Info
 function when you create a menu item for the command. This property accounts for the set of shortcut keys LabVIEW run-time menus allow.

#### Remarks

All LabVIEW shortcut key operations require the <Ctrl> key to be pressed. Examples of shortcut key values include
 "x"
 ,
 "w"
 , and
 "F12"
 .

Set the
 [Command.LVShortcutModifier](command-lvshortcutmodifier.html)
 property to
 True
 to specify that the shortcut key requires the <Shift> key to be pressed to invoke the command.

The command computes the value of this property according to the kind of command and the current state of the items to which the command applies. However, when you set this property, the command returns only the property values you set for the remainder of the life of the Command object.

#### See Also

[Command.LVShortcutModifier](command-lvshortcutmodifier.html)

Parent topic:

Properties

<!--NI_TOPIC bundle=teststand-api-reference path=tsuiref/command-lvshortcutmodifier.html language=enus -->
## TOPIC 04864: Command.LVShortcutModifier

- bundle_id: `teststand-api-reference`
- source_path: `tsuiref/command-lvshortcutmodifier.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsuiref/command-lvshortcutmodifier.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax Command.LVShortcutModifier Data Type Boolean Purpose Specifies whether to include the <Shift> key for the shortcut key that invokes the menu item or user interface element that represents the command. Use this value for the include Shift key? element of the short cut cluster input to the LabV

### Command.LVShortcutModifier

#### Syntax

[Command](command.html).LVShortcutModifier

#### Data Type

[Boolean](data-types-for-teststand-user-interface.html)

#### Purpose

Specifies whether to include the <Shift> key for the shortcut key that invokes the menu item or user interface element that represents the command. Use this value for the
 include Shift key?
 element of the
 short cut
 cluster input to the LabVIEW
 Set Menu Item Info
 function when you create a menu item for the command.

#### Remarks

The command computes the value of this property according to the kind of command and the current state of the items to which the command applies. However, when you set this property, the command returns only the property values you set for the remainder of the life of the Command object.

#### See Also

[Command.LVShortcutKey](command-lvshortcutkey.html)

Parent topic:

Properties

<!--NI_TOPIC bundle=teststand-api-reference path=tsuiref/command-sequencefileviewmgr.html language=enus -->
## TOPIC 04865: Command.SequenceFileViewMgr

- bundle_id: `teststand-api-reference`
- source_path: `tsuiref/command-sequencefileviewmgr.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsuiref/command-sequencefileviewmgr.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax Command.SequenceFileViewMgr Data Type SequenceFileViewMgr Purpose Specifies the SequenceFileView Manager control to which the command applies. The enabled, visible, or other states of the command, as well as the entity on which the command operates, vary according to the type of command and t

### Command.SequenceFileViewMgr

#### Syntax

[Command](command.html).SequenceFileViewMgr

#### Data Type

[SequenceFileViewMgr](sequencefileviewmgr.html)

#### Purpose

Specifies the SequenceFileView Manager control to which the command applies. The enabled, visible, or other states of the command, as well as the entity on which the command operates, vary according to the type of command and the SequenceFileView Manager control selections for the sequence file, sequence, step group, and steps.

#### Remarks

A value of
 NULL
 specifies that the command does not apply to an SequenceFileView Manager control.

#### See Also

[Command.ExecutionViewMgr](command-executionviewmgr.html)

[Commands.InsertKind](commands-insertkind.html)

[SequenceFileViewMgr](sequencefileviewmgr.html)

Parent topic:

Properties

<!--NI_TOPIC bundle=teststand-api-reference path=tsuiref/command-setdisplayname.html language=enus -->
## TOPIC 04866: Command.SetDisplayName

- bundle_id: `teststand-api-reference`
- source_path: `tsuiref/command-setdisplayname.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsuiref/command-setdisplayname.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax Command.SetDisplayName( val) Purpose Specifies text that describes the command to the user. Parameters val As String [In] Pass the new value for the command display name. When the new display name has a character you want to designate as the accelerator character, precede the character with a

### Command.SetDisplayName

#### Syntax

[Command](command.html).SetDisplayName( val)

#### Purpose

Specifies text that describes the command to the user.

#### Parameters

val
 As
 [String](data-types-for-teststand-user-interface.html)

[In] Pass the new value for the command display name. When the new display name has a character you want to designate as the accelerator character, precede the character with an ampersand (
 &
 ).

#### See Also

[Command.GetDisplayName](command-getdisplayname.html)

Parent topic:

Methods

<!--NI_TOPIC bundle=teststand-api-reference path=tsuiref/command-shortcutkey.html language=enus -->
## TOPIC 04867: Command.ShortcutKey

- bundle_id: `teststand-api-reference`
- source_path: `tsuiref/command-shortcutkey.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsuiref/command-shortcutkey.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax Command.ShortcutKey Data Type ShortcutKeys Purpose Specifies which shortcut key to assign to a user interface element that represents a command. Remarks Use the Command.ShortcutModifier property to specify <Shift>, <Ctrl>, and <Alt> modifiers for the shortcut key. For example, to assign the s

### Command.ShortcutKey

#### Syntax

[Command](command.html).ShortcutKey

#### Data Type

[ShortcutKeys](shortcutkeys.html)

#### Purpose

Specifies which shortcut key to assign to a user interface element that represents a command.

#### Remarks

Use the
 [Command.ShortcutModifier](command-shortcutmodifier.html)
 property to specify <Shift>, <Ctrl>, and <Alt> modifiers for the shortcut key. For example, to assign the shortcut
 Ctrl+F12
 to the command, set this property to
 ShortcutKey_VK_F12
 and set the
 Command.ShortcutModifier
 property to
 ShortcutModifier_Control
 .

The command computes the value of this property according to the kind of command and the current state of the items to which the command applies. However, when you set this property, the command returns only the property values you set for the remainder of the life of the Command object.

#### See Also

[Command.ShortcutModifier](command-shortcutmodifier.html)

[Command.LVShortcutKey](command-lvshortcutkey.html)

[Commands](commands.html)

[ShortcutKeys](shortcutkeys.html)

Parent topic:

Properties

<!--NI_TOPIC bundle=teststand-api-reference path=tsuiref/command-shortcutmodifier.html language=enus -->
## TOPIC 04868: Command.ShortcutModifier

- bundle_id: `teststand-api-reference`
- source_path: `tsuiref/command-shortcutmodifier.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsuiref/command-shortcutmodifier.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax Command.ShortcutModifier Data Type Long Purpose Specifies which shortcut key modifiers to assign to a user interface element that represents a command. Remarks The command computes the value of this property according to the kind of command and the current state of the items to which the comm

### Command.ShortcutModifier

#### Syntax

[Command](command.html).ShortcutModifier

#### Data Type

[Long](data-types-for-teststand-user-interface.html)

#### Purpose

Specifies which shortcut key modifiers to assign to a user interface element that represents a command.

#### Remarks

The command computes the value of this property according to the kind of command and the current state of the items to which the command applies. However, when you set this property, the command returns only the property values you set for the remainder of the life of the Command object.

#### See Also

[Command.ShortcutKey](command-shortcutkey.html)

[Commands](commands.html)

[ShortcutModifiers](shortcutmodifiers.html)

Parent topic:

Properties

<!--NI_TOPIC bundle=teststand-api-reference path=tsuiref/command-subsidiarycommands.html language=enus -->
## TOPIC 04869: Command.SubsidiaryCommands

- bundle_id: `teststand-api-reference`
- source_path: `tsuiref/command-subsidiarycommands.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsuiref/command-subsidiarycommands.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax Command.SubsidiaryCommands Data Type Commands Purpose Specifies the subsidiary commands the command contains. When a menu contains an item for the command, the subsidiary commands appear as items in a submenu that attach to the item for the command. When the command has no subsidiary commands

### Command.SubsidiaryCommands

#### Syntax

[Command](command.html).SubsidiaryCommands

#### Data Type

[Commands](commands.html)

#### Purpose

Specifies the subsidiary commands the command contains. When a menu contains an item for the command, the subsidiary commands appear as items in a submenu that attach to the item for the command. When the command has no subsidiary commands, the value can be
 NULL
 or the
 [Commands](commands.html)
 collection is empty.

#### See Also

[Commands](commands.html)

Parent topic:

Properties

<!--NI_TOPIC bundle=teststand-api-reference path=tsuiref/command-togglestate.html language=enus -->
## TOPIC 04870: Command.ToggleState

- bundle_id: `teststand-api-reference`
- source_path: `tsuiref/command-togglestate.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsuiref/command-togglestate.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax Command.ToggleState Data Type Boolean Purpose When the Command.IsToggle property is True , this property specifies the on or off state of the menu item or user interface element that represents the command. When a menu item represents the command, the state of the menu item indicates the valu

### Command.ToggleState

#### Syntax

[Command](command.html).ToggleState

#### Data Type

[Boolean](data-types-for-teststand-user-interface.html)

#### Purpose

When the
 [Command.IsToggle](command-istoggle.html)
 property is
 True
 , this property specifies the on or off state of the menu item or user interface element that represents the command. When a menu item represents the command, the state of the menu item indicates the value of this property.

#### Remarks

The command computes the value of this property according to the kind of command and the current state of the items to which the command applies. However, when you set this property, the command returns only the property values you set for the remainder of the life of the Command object.

#### See Also

[Command.IsToggle](command-istoggle.html)

Parent topic:

Properties

<!--NI_TOPIC bundle=teststand-api-reference path=tsuiref/command-userdata.html language=enus -->
## TOPIC 04871: Command.UserData

- bundle_id: `teststand-api-reference`
- source_path: `tsuiref/command-userdata.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsuiref/command-userdata.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax Command.UserData Data Type Variant Purpose Holds a data item you associate with the Command object. Remarks Typically, you do not use this property unless you are implementing an event handler that requires specific data you define. See Also ApplicationMgr.PostCommandExecute ApplicationMgr.Pr

### Command.UserData

#### Syntax

[Command](command.html).UserData

#### Data Type

[Variant](data-types-for-teststand-user-interface.html)

#### Purpose

Holds a data item you associate with the Command object.

#### Remarks

Typically, you do not use this property unless you are implementing an event handler that requires specific data you define.

#### See Also

[ApplicationMgr.PostCommandExecute](applicationmgr-postcommandexecute.html)

[ApplicationMgr.PreCommandExecute](applicationmgr-precommandexecute.html)

[Command.UserObject](command-userobject.html)

Parent topic:

Properties

<!--NI_TOPIC bundle=teststand-api-reference path=tsuiref/command-userobject.html language=enus -->
## TOPIC 04872: Command.UserObject

- bundle_id: `teststand-api-reference`
- source_path: `tsuiref/command-userobject.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsuiref/command-userobject.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax Command.UserObject Data Type IUnknown Purpose Holds an ActiveX object you associate with the Command object. Remarks Typically, you do not use this property unless you are implementing an event handler that requires specific data you define. See Also ApplicationMgr.PostCommandExecute Applicat

### Command.UserObject

#### Syntax

[Command](command.html).UserObject

#### Data Type

[IUnknown](data-types-for-teststand-user-interface.html)

#### Purpose

Holds an ActiveX object you associate with the Command object.

#### Remarks

Typically, you do not use this property unless you are implementing an event handler that requires specific data you define.

#### See Also

[ApplicationMgr.PostCommandExecute](applicationmgr-postcommandexecute.html)

[ApplicationMgr.PreCommandExecute](applicationmgr-precommandexecute.html)

[Command.UserData](command-userdata.html)

Parent topic:

Properties

<!--NI_TOPIC bundle=teststand-api-reference path=tsuiref/command-visible.html language=enus -->
## TOPIC 04873: Command.Visible

- bundle_id: `teststand-api-reference`
- source_path: `tsuiref/command-visible.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsuiref/command-visible.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax Command.Visible Data Type Boolean Purpose Specifies whether to show or hide the menu item or user interface element that invokes the command. Remarks The command computes the value of this property according to the kind of command and the current state of the items to which the command applie

### Command.Visible

#### Syntax

[Command](command.html).Visible

#### Data Type

[Boolean](data-types-for-teststand-user-interface.html)

#### Purpose

Specifies whether to show or hide the menu item or user interface element that invokes the command.

#### Remarks

The command computes the value of this property according to the kind of command and the current state of the items to which the command applies. However, when you set this property, the command returns only the property values you set for the remainder of the life of the Command object.

#### See Also

[Enabled](command-enabled.html)

Parent topic:

Properties

<!--NI_TOPIC bundle=teststand-api-reference path=tsuiref/command.html language=enus -->
## TOPIC 04874: Command

- bundle_id: `teststand-api-reference`
- source_path: `tsuiref/command.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsuiref/command.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Use Command objects in applications to implement a user interface element that performs a standard action, such as opening a sequence file or executing a set of selected steps in a sequence. A Command object determines the dimming, visibility, shortcut key, and caption for the menu item, button, or

### Command

Use Command objects in applications to
 [implement a user interface element](/csh?context=ts_tsfundamentals_uis)
 that performs a standard action, such as opening a sequence file or executing a set of selected steps in a sequence. A Command object determines the dimming, visibility, shortcut key, and caption for the menu item, button, or checkbox that invokes the command. The Command object also provides the implementation of the action, which it performs when you call the
 Command.Execute
 method.

In many cases you can use a TestStand Utility Library function, such as
 InsertCommandsInMenu
 , instead of Command objects to create menu items that invoke the commands you specify. You can also call the
 ConnectCommand
 method on a TestStand manager control to connect a command to a TestStand button or checkbox control.

To create Command objects, call the
 [ApplicationMgr.NewCommands](applicationmgr-newcommands.html)
 method to create a Commands collection. You specify the commands to create with the
 [CommandKinds](commandkinds.html)
 enumeration constants. When you call the
 [Commands.InsertKind](commands-insertkind.html)
 method, you can also specify a TestStand manager control. A command you create uses the specified manager control to determine the currently selected sequence file, execution, sequence, or steps. According to the selection and the type of command, the command determines the state of its properties, such as enabled and visible, and determines which items the command operates on when it executes. Some commands do not require a manager control, while others require a specific manager control. Refer to the
 [CommandKinds](commandkinds.html)
 enumeration for more information about which manager controls work with specific commands.

You can also create commands using the following methods:

- ApplicationMgr.GetCommand
- ExecutionViewMgr.GetCommand
- SequenceFileViewMgr.GetCommand
- Commands.InsertKind

#### Properties

| Enabled |
| --- |
| EntryPoint (Read Only) |
| EntryPointIndex (Read Only) |
| ExecutionViewMgr |
| IconName |
| IsSeparator |
| IsToggle |
| Kind (Read Only) |
| LVShortcutKey |
| LVShortcutModifier |
| SequenceFileViewMgr |
| ShortcutKey |
| ShortcutModifier |
| SubsidiaryCommands |
| ToggleState |
| UserData |
| UserObject |
| Visible |

#### Methods

| Execute |
| --- |
| GetDisplayName |
| SetDisplayName |

#### See Also

[ApplicationMgr.ConnectCommand](applicationmgr-connectcommand.html)

[ApplicationMgr.GetCommand](applicationmgr-getcommand.html)

[ApplicationMgr.NewCommands](applicationmgr-newcommands.html)

[CommandKinds](commandkinds.html)

[Commands](commands.html)

[Commands.InsertKind](commands-insertkind.html)

[ExecutionViewMgr.ConnectCommand](executionviewmgr-connectcommand.html)

[ExecutionViewMgr.GetCommand](executionviewmgr-getcommand.html)

[SequenceFileViewMgr.ConnectCommand](sequencefileviewmgr-connectcommand.html)

[SequenceFileViewMgr.GetCommand](sequencefileviewmgr-getcommand.html)

Parent topic:

TestStand User Interface Controls

<!--NI_TOPIC bundle=teststand-api-reference path=tsuiref/commandconnection-freezerefresh.html language=enus -->
## TOPIC 04875: CommandConnection.FreezeRefresh

- bundle_id: `teststand-api-reference`
- source_path: `tsuiref/commandconnection-freezerefresh.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsuiref/commandconnection-freezerefresh.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax CommandConnection.FreezeRefresh( frz) Purpose Specifies to freeze the CommandConnection when setting the properties to avoid flicker on the connected control. Remarks FreezeRefresh calls must be balanced. For example, each time you call this method with a value of True , you must also call it

### CommandConnection.FreezeRefresh

#### Syntax

[CommandConnection](commandconnection.html).FreezeRefresh( frz)

#### Purpose

Specifies to freeze the CommandConnection when setting the properties to avoid flicker on the connected control.

#### Remarks

FreezeRefresh
 calls must be balanced. For example, each time you call this method with a value of
 True
 , you must also call it with a value of
 False
 .

#### Parameters

frz
 As
 [Boolean](data-types-for-teststand-user-interface.html)

[In] When this parameter is
 True
 , the CommandConnection does not refresh the control. When this parameter is
 False
 , the CommandConnection refreshes the control.

Parent topic:

Methods

<!--NI_TOPIC bundle=teststand-api-reference path=tsuiref/commandconnection-index.html language=enus -->
## TOPIC 04876: CommandConnection.Index

- bundle_id: `teststand-api-reference`
- source_path: `tsuiref/commandconnection-index.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsuiref/commandconnection-index.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax CommandConnection.Index Data Type Long Purpose Specifies which command in the set of commands to use. Remarks Use this on sets of commands. Refer to the CommandKinds enumeration for more information about supported command sets. See Also CommandKinds

### CommandConnection.Index

#### Syntax

[CommandConnection](commandconnection.html).Index

#### Data Type

[Long](data-types-for-teststand-user-interface.html)

#### Purpose

Specifies which command in the set of commands to use.

#### Remarks

Note

CommandKinds

#### See Also

[CommandKinds](commandkinds.html)

Parent topic:

Properties

<!--NI_TOPIC bundle=teststand-api-reference path=tsuiref/commandconnection-kind.html language=enus -->
## TOPIC 04877: CommandConnection.Kind

- bundle_id: `teststand-api-reference`
- source_path: `tsuiref/commandconnection-kind.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsuiref/commandconnection-kind.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax CommandConnection.Kind Data Type CommandKinds Purpose Specifies the type of Command to which this CommandConnection connects. See Also CommandKinds

### CommandConnection.Kind

#### Syntax

[CommandConnection](commandconnection.html).Kind

#### Data Type

[CommandKinds](commandkinds.html)

#### Purpose

Specifies the type of Command to which this CommandConnection connects.

#### See Also

[CommandKinds](commandkinds.html)

Parent topic:

Properties

<!--NI_TOPIC bundle=teststand-api-reference path=tsuiref/commandconnection-options.html language=enus -->
## TOPIC 04878: CommandConnection.Options

- bundle_id: `teststand-api-reference`
- source_path: `tsuiref/commandconnection-options.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsuiref/commandconnection-options.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax CommandConnection.Options Data Type Long Purpose Specifies the behavior of the CommandConnection. Remarks The value of this property is a bitwise-OR combination of the CommandConnectionOptions constants. See Also CommandConnectionOptions

### CommandConnection.Options

#### Syntax

[CommandConnection](commandconnection.html).Options

#### Data Type

[Long](data-types-for-teststand-user-interface.html)

#### Purpose

Specifies the behavior of the CommandConnection.

#### Remarks

The value of this property is a bitwise-OR combination of the
 [CommandConnectionOptions](commandconnectionoptions.html)
 constants.

#### See Also

[CommandConnectionOptions](commandconnectionoptions.html)

Parent topic:

Properties

<!--NI_TOPIC bundle=teststand-api-reference path=tsuiref/commandconnection-refresh.html language=enus -->
## TOPIC 04879: CommandConnection.Refresh

- bundle_id: `teststand-api-reference`
- source_path: `tsuiref/commandconnection-refresh.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsuiref/commandconnection-refresh.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax CommandConnection.Refresh Purpose Refreshes the state of the user interface control connected to the CommandConnection.

### CommandConnection.Refresh

#### Syntax

[CommandConnection](commandconnection.html).Refresh

#### Purpose

Refreshes the state of the user interface control connected to the CommandConnection.

Parent topic:

Methods

<!--NI_TOPIC bundle=teststand-api-reference path=tsuiref/commandconnection.html language=enus -->
## TOPIC 04880: CommandConnection

- bundle_id: `teststand-api-reference`
- source_path: `tsuiref/commandconnection.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsuiref/commandconnection.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Represents a connection to a CommandKind . Properties Index Kind Options Methods FreezeRefresh Refresh See Also CommandConnectionOptions CommandConnections CommandKinds

### CommandConnection

Represents a connection to a
 [CommandKind](commandkinds.html)
 .

#### Properties

| Index |
| --- |
| Kind |
| Options |

#### Methods

| FreezeRefresh |
| --- |
| Refresh |

#### See Also

[CommandConnectionOptions](commandconnectionoptions.html)

[CommandConnections](commandconnections.html)

[CommandKinds](commandkinds.html)

Parent topic:

TestStand User Interface Support Controls

<!--NI_TOPIC bundle=teststand-api-reference path=tsuiref/commandconnectionoptions.html language=enus -->
## TOPIC 04881: CommandConnectionOptions

- bundle_id: `teststand-api-reference`
- source_path: `tsuiref/commandconnectionoptions.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsuiref/commandconnectionoptions.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Use these constants with the CommandConnection.Options property. CommandConnection_EnableImage –(Value: 0x8) The connection sets the image on the connected control. CommandConnection_IgnoreCaption –(Value: 0x2) The connection does not set the caption on the connected control. CommandConnection_Ignor

### CommandConnectionOptions

Use these constants with the
 [CommandConnection.Options](commandconnection-options.html)
 property.

- CommandConnection_EnableImage 
 –(Value: 0x8) The connection sets the image on the connected control.
- CommandConnection_IgnoreCaption 
 –(Value: 0x2) The connection does not set the caption on the connected control.
- CommandConnection_IgnoreEnable 
 –(Value: 0x4) The connection does not enable or disable the connected control.
- CommandConnection_IgnoreVisible 
 –(Value: 0x1) The connection does not change the visibility of the connected control.
- CommandConnection_NoOptions 
 –(Value: 0x0) No options.

#### See Also

[CommandConnection.Options](commandconnection-options.html)

[ApplicationMgr.ConnectCommand](applicationmgr-connectcommand.html)

[ExecutionViewMgr.ConnectCommand](executionviewmgr-connectcommand.html)

[SequenceFileViewMgr.ConnectCommand](sequencefileviewmgr-connectcommand.html)

Parent topic:

Core UI Constants

<!--NI_TOPIC bundle=teststand-api-reference path=tsuiref/commandconnections-add.html language=enus -->
## TOPIC 04882: CommandConnections.Add

- bundle_id: `teststand-api-reference`
- source_path: `tsuiref/commandconnections-add.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsuiref/commandconnections-add.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax CommandConnections.Add( uiObj) Return Value CommandConnection New CommandConnection. Purpose Creates and adds a new CommandConnection to the collection. Parameters uiObj As Object [In] Specifies the user interface object to connect. See Also ApplicationMgr.ConnectCommand CommandConnections.Re

### CommandConnections.Add

#### Syntax

[CommandConnections](commandconnections.html).Add( uiObj)

#### Return Value

[CommandConnection](commandconnection.html)

New CommandConnection.

#### Purpose

Creates and adds a new CommandConnection to the collection.

#### Parameters

uiObj
 As
 [Object](data-types-for-teststand-user-interface.html)

[In] Specifies the user interface object to connect.

#### See Also

[ApplicationMgr.ConnectCommand](applicationmgr-connectcommand.html)

[CommandConnections.Remove](commandconnections-remove.html)

Parent topic:

Methods

<!--NI_TOPIC bundle=teststand-api-reference path=tsuiref/commandconnections-clear.html language=enus -->
## TOPIC 04883: CommandConnections.Clear

- bundle_id: `teststand-api-reference`
- source_path: `tsuiref/commandconnections-clear.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsuiref/commandconnections-clear.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax CommandConnections.Clear Purpose Removes all items from the collection. See Also CommandConnections.Remove

### CommandConnections.Clear

#### Syntax

[CommandConnections](commandconnections.html).Clear

#### Purpose

Removes all items from the collection.

#### See Also

[CommandConnections.Remove](commandconnections-remove.html)

Parent topic:

Methods

<!--NI_TOPIC bundle=teststand-api-reference path=tsuiref/commandconnections-count.html language=enus -->
## TOPIC 04884: CommandConnections.Count

- bundle_id: `teststand-api-reference`
- source_path: `tsuiref/commandconnections-count.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsuiref/commandconnections-count.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax CommandConnections.Count Data Type Long Purpose Returns the number of items in the collection.

### CommandConnections.Count

#### Syntax

[CommandConnections](commandconnections.html).Count

#### Data Type

[Long](data-types-for-teststand-user-interface.html)

#### Purpose

Returns the number of items in the collection.

Parent topic:

Properties

<!--NI_TOPIC bundle=teststand-api-reference path=tsuiref/commandconnections-fromcontrol.html language=enus -->
## TOPIC 04885: CommandConnections.FromControl

- bundle_id: `teststand-api-reference`
- source_path: `tsuiref/commandconnections-fromcontrol.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsuiref/commandconnections-fromcontrol.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax CommandConnections.FromControl( uiObj) Return Value CommandConnection CommandConnection connected to the uiObj parameter. When no CommandConnection exists for this control, this method returns NULL . Purpose Returns the CommandConnection connected to the uiObj parameter. Parameters uiObj As O

### CommandConnections.FromControl

#### Syntax

[CommandConnections](commandconnections.html).FromControl( uiObj)

#### Return Value

[CommandConnection](commandconnection.html)

CommandConnection connected to the
 uiObj
 parameter. When no CommandConnection exists for this control, this method returns
 NULL
 .

#### Purpose

Returns the CommandConnection connected to the
 uiObj
 parameter.

#### Parameters

uiObj
 As
 [Object](data-types-for-teststand-user-interface.html)

[In] Specifies the connected user interface object.

Parent topic:

Methods

<!--NI_TOPIC bundle=teststand-api-reference path=tsuiref/commandconnections-item.html language=enus -->
## TOPIC 04886: CommandConnections.Item

- bundle_id: `teststand-api-reference`
- source_path: `tsuiref/commandconnections-item.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsuiref/commandconnections-item.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax CommandConnections.Item( itemIndex) Data Type CommandConnection Item located at the specified index. Purpose Returns a reference to an item at the specified index in the collection. Parameters itemIndex As Long [In] Specifies the index of the item to retrieve. See Also CommandConnection Comma

### CommandConnections.Item

#### Syntax

[CommandConnections](commandconnections.html).Item( itemIndex)

#### Data Type

[CommandConnection](commandconnection.html)

Item located at the specified index.

#### Purpose

Returns a reference to an item at the specified index in the collection.

#### Parameters

itemIndex
 As
 [Long](data-types-for-teststand-user-interface.html)

[In] Specifies the index of the item to retrieve.

#### See Also

[CommandConnection](commandconnection.html)

[CommandConnections.Count](commandconnections-count.html)

Parent topic:

Properties

<!--NI_TOPIC bundle=teststand-api-reference path=tsuiref/commandconnections-remove.html language=enus -->
## TOPIC 04887: CommandConnections.Remove

- bundle_id: `teststand-api-reference`
- source_path: `tsuiref/commandconnections-remove.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsuiref/commandconnections-remove.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax CommandConnections.Remove( uiObj) Return Value Boolean Returns True when the CommandConnection is removed. Returns False when the CommandConnection is not found. Purpose Removes the specified item from this collection, if it exists. Parameters uiObj As Object [In] Specifies the user interface

### CommandConnections.Remove

#### Syntax

[CommandConnections](commandconnections.html).Remove( uiObj)

#### Return Value

[Boolean](data-types-for-teststand-user-interface.html)

Returns
 True
 when the CommandConnection is removed. Returns
 False
 when the CommandConnection is not found.

#### Purpose

Removes the specified item from this collection, if it exists.

#### Parameters

uiObj
 As
 [Object](data-types-for-teststand-user-interface.html)

[In] Specifies the user interface object to disconnect.

#### See Also

[CommandConnections.Add](commandconnections-add.html)

Parent topic:

Methods

<!--NI_TOPIC bundle=teststand-api-reference path=tsuiref/commandconnections.html language=enus -->
## TOPIC 04888: CommandConnections

- bundle_id: `teststand-api-reference`
- source_path: `tsuiref/commandconnections.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsuiref/commandconnections.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: A collection of CommandConnection objects. Properties Count (Read Only) Item (Read Only) Methods Add Clear FromControl Remove See Also CommandConnection

### CommandConnections

A collection of
 [CommandConnection](commandconnection.html)
 objects.

#### Properties

| Count (Read Only) |
| --- |
| Item (Read Only) |

#### Methods

| Add |
| --- |
| Clear |
| FromControl |
| Remove |

#### See Also

[CommandConnection](commandconnection.html)

Parent topic:

TestStand User Interface Support Controls

<!--NI_TOPIC bundle=teststand-api-reference path=tsuiref/commandkinds.html language=enus -->
## TOPIC 04889: CommandKinds

- bundle_id: `teststand-api-reference`
- source_path: `tsuiref/commandkinds.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsuiref/commandkinds.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: These constants specify types of standard commands. CommandKinds values specify a single command or a set of commands that can contain several commands or no commands, depending on the state of the application. You can pass these constants to the ApplicationMgr.ConnectCommand , SequenceFileViewMgr.C

### CommandKinds

These constants specify types of standard commands. CommandKinds values specify a single command or a set of commands that can contain several commands or no commands, depending on the state of the application.

You can pass these constants to the
 [ApplicationMgr.ConnectCommand](applicationmgr-connectcommand.html)
 ,
 [SequenceFileViewMgr.ConnectCommand](sequencefileviewmgr-connectcommand.html)
 , and
 [ExecutionViewMgr.ConnectCommand](executionviewmgr-connectcommand.html)
 methods to connect commands to buttons or checkboxes. You can also connect commands to
 [menu items](/csh?context=ts_tsfundamentals_menus)
 .

Note

CommandKind_Edit_Cut

CommandKind_Edit_EditCode

Button.Style

ButtonStyle_ToolBar

You can pass these constants to the
 [Commands.InsertKind](commands-insertkind.html)
 method to directly create command objects.

Most commands, such as
 OpenSequenceFile
 ,
 Login
 , and
 Restart
 , behave the same as the corresponding menu items in the TestStand Sequence Editor with regard to the action they take and the circumstances under which they are enabled. Refer to the
 [NI TestStand Environment Reference Help](../tsref/teststand-environment-reference-help.html)
 for the corresponding sequence editor menu item for more information about how the item behaves.

TestStand assigns default images to some commands, which TestStand displays when you connect the command to a
 [Button](button.html)
 control and you enable images for the control.

- CommandKind_Abort 
 –(Value: 75) Aborts the current execution. The execution does not run the Cleanup steps. This command applies to the
 ExecutionView Manager 
 control only.
- CommandKind_AbortAll 
 –(Value: 78) Aborts all executions. This command applies only to the
 Application Manager 
 control.
- CommandKind_Break 
 –(Value: 71) Suspends the selected execution. This command applies only to the ExecutionView Manager control. This command has a default image.
- CommandKind_BreakAll 
 –(Value: 76) Suspends all executions. This command applies only to the Application Manager control. This command has a default image.
- CommandKind_BreakOnFirstStep 
 –(Value: 50) Toggles whether executions suspend at the first step.
- CommandKind_BreakOnSequenceFailure 
 –(Value: 52) Toggles whether executions suspend when a sequence fails.
- CommandKind_BreakOnStepFailure 
 –(Value: 51) Toggles whether executions suspend when a step fails.
- CommandKind_BreakpointSubmenu 
 –(Value: 85) Contains the
 CommandKind_ToggleBreakpoint 
 and
 CommandKind_DisplayBreakpointSettings 
 subsidiary commands. When you insert this command into a menu, each subsidiary command appears as a submenu item. This command applies to the ExecutionView Manager and
 SequenceFileView Manager 
 controls.
- CommandKind_BreakResume 
 –(Value: 72) Suspends the selected execution if it is executing. Resumes the selected execution if it is suspended. This command applies only to the ExecutionView Manager control.
- CommandKind_Close 
 –(Value: 21) Closes the currently selected sequence file or execution. This command applies to the ExecutionView Manager and SequenceFileView Manager controls.
- CommandKind_CloseAll 
 –(Value: 22) Closes all executions and sequence files. This command applies only to the Application Manager control.
- CommandKind_CloseCompletedExecutions 
 –(Value: 23) Closes all completed executions. This command applies only to the Application Manager control.
- CommandKind_ConfigurationEntryPointDefaultMenuInsertionMarker 
 –(Value: 113) Specifies a set of commands that contains a
 CommandKind_RunEntryPoint 
 command for each Configuration entry point with a menu hint that does not select a menu other than the current menu. Because most entry points do not have menu hints, this constant typically specifies all Configuration entry points.
- CommandKind_ConfigurationEntryPointInsertionMarker 
 –(Value: 112) Specifies a set of commands that contains a
 CommandKind_RunEntryPoint 
 command for each Configuration entry point with a menu hint that selects the current menu.
- CommandKind_ConfigurationEntryPoints_Set 
 –(Value: 145) Specifies a set of commands that contains a
 CommandKind_RunEntryPoint 
 command for each Configuration entry point. When you specify commands to create menu items, use the
 CommandKind_ConfigurationEntryPointInsertionMarker 
 and
 CommandKind_ConfigurationEntryPointDefaultInsertionMarker 
 constants to honor menu hints entry points can specify.
- CommandKind_ConfigureAdapters 
 –(Value: 90) Launches the
 Adapter Configuration 
 dialog box.
- CommandKind_ConfigureEngineEnvironment 
 –(Value: 94) Launches the Configure Environment dialog box.
- CommandKind_ConfigureExternalViewers 
 –(Value: 93) Launches the
 Configure External Viewers 
 dialog box.
- CommandKind_ConfigureSearchDirectories 
 –(Value: 92) Launches the
 Edit Search Directories 
 dialog box.
- CommandKind_ConfigureSequenceViews 
 –(Value: 149) Launches the
 Edit Step List Configurations 
 dialog box. This command applies to the ExecutionView Manager and SequenceFileView Manager controls.
- CommandKind_ConfigureStationOptions 
 –(Value: 91) Launches the
 Station Options 
 dialog box.
- CommandKind_Container 
 –(Value: 1) Contains only subsidiary commands.
- CommandKind_Custom 
 –(Value: 3) Represents an action you define. You must set Command properties, such as the
 Command.Enabled 
 and
 Command.Visible 
 properties, to the values you require. Although this command does not perform an action when it executes, an application can perform an action when it receives the
 ApplicationMgr.PreCommandExecute 
 or
 ApplicationMgr.PostCommandExecute 
 event for the command. You can attach data you define to the command using the
 Command.UserObject 
 and
 Command.UserData 
 properties so the data is available to the application in the handlers for
 PreCommandExecute 
 and
 PostCommandExecute 
 events.
- CommandKind_CustomizeTools 
 –(Value: 101) Launches the
 Customize Tools Menu 
 dialog box.
- CommandKind_DefaultConfigureMenu_Set 
 –(Value: 124) Specifies a set of commands that correspond to the typical items in the
 Configure 
 menu of a TestStand application. Although the specific commands this constant represents might vary according to the version of TestStand, the following is a representative set of commands:
 CommandKind_ConfigureStationOptions 
 CommandKind_ConfigureSearchDirectories 
 CommandKind_ConfigureExternalViewers 
 CommandKind_ConfigureAdapters 
 CommandKind_Separator 
 CommandKind_ExecutionEntryPointInsertionMarker 
 CommandKind_ConfigurationEntryPointDefaultMenuInsertionMarker
- CommandKind_DefaultDebugMenu_Set 
 –(Value: 123) Specifies a set of commands that correspond to the typical items in the
 Debug 
 menu of a TestStand application. Although the specific commands this constant represents might vary according to the version of TestStand, the following is a representative set of commands:
 CommandKind_ExecutionEntryPointInsertionMarker 
 CommandKind_ConfigurationEntryPointInsertionMarker 
 CommandKind_Separator 
 CommandKind_ToggleBreakpoint 
 CommandKind_SetRunModeSubmenu 
 CommandKind_Separator 
 CommandKind_Resume 
 CommandKind_StepInto 
 CommandKind_StepOver 
 CommandKind_StepOut 
 CommandKind_SetNextStep 
 CommandKind_Separator 
 CommandKind_Break 
 CommandKind_Terminate 
 CommandKind_Abort 
 CommandKind_Separator 
 CommandKind_BreakAll 
 CommandKind_TerminateAll 
 CommandKind_AbortAll 
 CommandKind_ResumeAll 
 CommandKind_Separator 
 CommandKind_DisplayBreakAndWatchPoints
- CommandKind_DefaultEditMenu_Set 
 –(Value: 128) Specifies a set of commands that correspond to the typical items in the
 Edit 
 menu of a TestStand application. Although the specific commands this constant represents might vary according to the version of TestStand, the following is a representative set of commands:
 CommandKind_Edit_Undo* 
 CommandKind_Edit_Redo* 
 CommandKind_Separator* 
 CommandKind_Edit_Cut* 
 CommandKind_Edit_Copy 
 CommandKind_Edit_Paste* 
 CommandKind_Edit_Delete* 
 CommandKind_Edit_Rename* 
 CommandKind_Separator 
 CommandKind_SelectAll 
 CommandKind_Separator* 
 CommandKind_Edit_EditSteps_Set* 
 CommandKind_Edit_SpecifyModule* 
 CommandKind_Edit_EditCode* 
 CommandKind_Edit_Preconditions* 
 CommandKind_Separator* 
 CommandKind_Edit_SequenceFileCallbacks* 
 CommandKind_Separator* 
 CommandKind_Edit_StepProperties* 
 CommandKind_Edit_SequenceProperties* 
 CommandKind_Edit_SequenceFileProperties* 
 * The command is present only when editing is enabled.
- CommandKind_DefaultExecuteMenu_Set 
 –(Value: 121) Specifies a set of commands that correspond to the typical menu items in the
 Execute 
 menu of a TestStand application. Although the specific commands this constant represents might vary according to the version of TestStand, the following is a representative set of commands:
 CommandKind_Restart 
 CommandKind_Separator 
 CommandKind_ExecutionEntryPointDefaultMenuInsertionMarker 
 CommandKind_ConfigurationEntryPointDefaultMenuInsertionMarker 
 CommandKind_Separator 
 CommandKind_RunCurrentSequence 
 CommandKind_Separator 
 CommandKind_RunSelectedSteps 
 CommandKind_RunSelectedStepsUsingEntryPointSubmenu 
 CommandKind_LoopOnSelectedSteps 
 CommandKind_LoopOnSelectedStepsUsingEntryPointSubmenu 
 CommandKind_Separator 
 CommandKind_BreakOnFirstStep 
 CommandKind_BreakOnStepFailure 
 CommandKind_BreakOnSequenceFailure 
 CommandKind_TracingEnabled 
 This command applies only to the ExecutionView Manager control.
- CommandKind_DefaultFileMenu_Set 
 –(Value: 120) Specifies a set of commands that correspond to the typical items in the
 File 
 menu of a TestStand application. Although the specific commands this constant represents might vary according to the version of TestStand, the following is a representative set of commands:
 CommandKind_Login 
 CommandKind_Logout 
 CommandKind_Separator 
 CommandKind_Edit_NewSequenceFile* 
 CommandKind_OpenSequenceFiles 
 CommandKind_Close 
 CommandKind_Separator 
 CommandKind_CloseAll 
 CommandKind_CloseCompletedExecutions 
 CommandKind_Separator 
 CommandKind_OpenWorkspaceBrowser 
 CommandKind_Separator 
 CommandKind_Edit_Save* 
 CommandKind_Edit_SaveAs* 
 CommandKind_Edit_SaveAll* 
 CommandKind_Separator* 
 CommandKind_UnloadAllModules 
 CommandKind_LockUnlock 
 CommandKind_Separator 
 CommandKind_ExecutionEntryPointInsertionMarker 
 CommandKind_ConfigurationEntryPointInsertionMarker 
 CommandKind_Separator 
 CommandKind_MRUFiles_Set 
 CommandKind_Separator 
 CommandKind_Exit 
 * The command is present only when editing is enabled.
- CommandKind_DefaultHelpMenu_Set 
 –(Value: 440) Specifies a set of commands that corresponds to the typical items in the
 Help 
 menu of a TestStand application. Although the specific commands this constant represents might vary according to the version of TestStand, the following is a representative set of commands:
 CommandKind_ShowTestStandHelp 
 CommandKind_ShowGuideToDocumentation 
 CommandKind_ShowHelpTopic 
 CommandKind_Separator 
 CommandKind_ShowTestStandWebResources 
 CommandKind_ShowTestStandDiscussionForum 
 CommandKind_Separator 
 CommandKind_ShowPatents 
 CommandKind_Separator 
 CommandKind_ExecutionEntryPointInsertionMarker 
 CommandKind_ConfigurationEntryPointInsertionMarker
- CommandKind_DefaultListBarContextMenu_Set 
 –(Value: 127) Specifies a set of commands that corresponds to the typical items in the list bar context menu of a TestStand application. Although the specific commands this constant represents might vary according to the version of TestStand, the following are a representative set of commands:
 SequenceFileView Manager Control: 
 CommandKind_ExecutionEntryPointDefaultMenuInsertionMarker 
 CommandKind_Separator 
 CommandKind_RunCurrentSequence 
 CommandKind_Separator 
 CommandKind_OpenSequenceFile 
 CommandKind_Close 
 ExecutionView Manager Control: 
 CommandKind_Close 
 CommandKind_CloseCompletedExecutions 
 CommandKind_Separator 
 CommandKind_TerminateRestart 
 CommandKind_BreakResume 
 CommandKind_Abort 
 CommandKind_Separator 
 CommandKind_BreakAll 
 CommandKind_TerminateAll 
 CommandKind_AbortAll 
 CommandKind_ResumeAll
- CommandKind_DefaultSequenceListContextMenu_Set 
 –(Value: 129) Specifies a set of commands that corresponds to the typical items in the
 sequence list 
 context menu of a TestStand application. This constant applies to the SequenceFileView Manager control. Although the specific commands this constant represents might vary according to the version of TestStand, the following are a representative set of commands:
 CommandKind_Edit_InsertSequence* 
 CommandKind_Separator* 
 CommandKind_Edit_Cut* 
 CommandKind_Edit_Copy* 
 CommandKind_Edit_Paste* 
 CommandKind_Edit_Delete* 
 CommandKind_Edit_Rename* 
 CommandKind_Separator* 
 CommandKind_Edit_SequenceFileCallbacks* 
 CommandKind_Separator* 
 CommandKind_Edit_SequenceProperties* 
 * The command is present only when editing is enabled.
- CommandKind_DefaultSequenceViewContextMenu_Set 
 –(Value: 126) Specifies a set of commands that corresponds to the typical items in the
 sequence view 
 context menu of a TestStand application. Although the specific commands this constant represents might vary according to the version of TestStand, the following are a representative set of commands:
 SequenceFileView Manager Control 
 :
 CommandKind_Edit_InsertStepsSubmenu* 
 CommandKind_Edit_EncapsulateSelectedStepsSubmenu* 
 CommandKind_Edit_SelectDefaultAdapters_Set* 
 CommandKind_Separator* 
 CommandKind_Edit_EditSteps_Set* 
 CommandKind_Edit_SpecifyModule* 
 CommandKind_Edit_EditCode* 
 CommandKind_Edit_Preconditions* 
 CommandKind_Separator* 
 CommandKind_BreakpointSubmenu 
 CommandKind_SetRunModeSubmenu 
 CommandKind_Separator 
 CommandKind_Edit_Cut* 
 CommandKind_Edit_Copy* 
 CommandKind_Edit_Paste* 
 CommandKind_Edit_Delete* 
 CommandKind_Edit_Rename* 
 CommandKind_Separator 
 CommandKind_RunSelectedSteps 
 CommandKind_RunSelectedStepsUsingEntryPointsSubmenu 
 CommandKind_LoopOnSelectedSteps 
 CommandKind_LoopOnSelectedStepsUsingEntryPointsSubmenu 
 CommandKind_Separator 
 CommandKind_SequenceViewConfigurationsSubmenu 
 CommandKind_Separator* 
 CommandKind_Edit_StepProperties* 
 ExecutionView Manager Control 
 :
 CommandKind_BreakpointSubmenu 
 CommandKind_SetRunModeSubmenu 
 CommandKind_Separator 
 CommandKind_RunSelectedSteps 
 CommandKind_LoopOnSelectedSteps 
 CommandKind_Separator 
 CommandKind_SetNextStep 
 CommandKind_Separator* 
 CommandKind_SequenceViewConfigurationsSubmenu 
 * The command is present only when editing is enabled.
- CommandKind_DefaultToolsMenu_Set 
 –(Value: 125) Specifies a set of commands that correspond to the typical items found in the
 Tools 
 menu of a TestStand application. Although the specific commands this constant represents might vary according to the version of TestStand, the following is a representative set of commands:
 CommandKind_Tools_Set 
 CommandKind_Separator 
 CommandKind_CustomizeTools 
 CommandKind_Separator 
 CommandKind_ExecutionEntryPointInsertionMarker 
 CommandKind_ConfigurationEntryPointInsertionMarker
- CommandKind_DisplayBreakpointsAndWatchExpressions 
 –(Value: 80) Launches the
 Edit Breakpoints/Watch Expressions 
 dialog box.
- CommandKind_DisplayBreakpointSettings 
 –(Value: 81) Launches the
 Breakpoint Settings 
 dialog box for the selected step. This command applies to the ExecutionView Manager or SequenceFileView Manager controls.
- CommandKind_Edit_AdvancedSequenceListSubmenu 
 –(Value: 451) Contains the
 CommandKind_Edit_Attributes 
 subsidiary command. When you insert this command into a menu, the subsidiary commands appear within a submenu item. This command applies to the
 SequenceFileView Manager 
 control.
- CommandKind_Edit_Attributes 
 –(Value: 450) Displays the
 Attributes 
 dialog box. TestStand supports this command only for a sequence connection. This command applies to the
 SequenceFileView Manager 
 control. This command has a default image.
- CommandKind_Edit_Copy 
 –(Value: 204) Copies the selection to the clipboard. This command applies to the SequenceFileView Manager control. This command has a default image.
- CommandKind_Edit_Cut 
 –(Value: 203) Moves the selection onto the clipboard. This command applies to the SequenceFileView Manager control. This command has a default image.
- CommandKind_Edit_Delete 
 –(Value: 206) Deletes the selection. This command applies to the SequenceFileView Manager control.
- CommandKind_Edit_EditCode 
 –(Value: 216) Displays the module source code for the step with focus. This command applies to the SequenceFileView Manager control.
- CommandKind_Edit_EditPaths 
 –(Value: 223) Launches the
 Edit Paths in Files 
 dialog box.
- CommandKind_Edit_EditStep 
 –(Value: 217) Performs a step type-dependent editing operation on the step with focus. Typically, the operation launches an editing dialog box. For example, this command might launch the
 Edit Numeric Limit Test 
 dialog box for a Numeric Limit Test step. You do not create commands of this type. Instead, the
 CommandKind_Edit_EditSteps_Set 
 and
 CommandKind_Edit_EditStepsSubmenu 
 constants contain commands of this type as needed. This command applies to the SequenceFileView Manager control.
- CommandKind_Edit_EditSteps_Set 
 –(Value: 341) Specifies a set of commands that contains a
 CommandKind_Edit_EditStep 
 command for each step type specific editing operation that applies to the step with focus. A step type can define the available editing operations for instances of the type by specifying Edit substeps, which typically call a module to launch an editing dialog box.
- CommandKind_Edit_EditStepsSubmenu 
 –(Value: 301) Specifies a container command with subsidiary commands the
 CommandKind_Edit_ EditSteps_Set 
 constant specifies. When you insert this command into a menu, the subsidiary commands appear within a submenu item. This command applies to the SequenceFileView Manager control.
- CommandKind_Edit_EncapsulateSelectedSteps 
 –(Value: 224) Surrounds the selected steps with the specified step and a corresponding end step. You do not create commands of this type. Instead, the
 CommandKind_Edit_EncapsulateSelectedSteps_Set 
 and
 CommandKind_Edit_EncapsulateSelectedStepsSubmenu 
 constants contain commands of this type as needed. This command applies to the
 SequenceFileView Manager 
 control.
- CommandKind_Edit_EncapsulateSelectedSteps_Set 
 –(Value: 343) Specifies a set of commands that contains a
 CommandKind_Edit_EncapsulateSelectedSteps 
 command for each available step type with the
 
 StepType.CanEncapsulate 
 property set to
 True 
 and that starts a block structure in a sequence. Insert this command into a menu to create the contents of the Encapsulate With context menu. This command applies to the
 SequenceFileView Manager 
 control.
- CommandKind_Edit_EncapsulateSelectedStepsSubmenu 
 –(Value: 303) Specifies a container command whose subsidiary commands the
 CommandKind_Edit_EncapsulateSelectedSteps_Set 
 constant specifies. When you insert this command into a menu, each subsidiary command is visible as a submenu item. This command applies to the
 SequenceFileView Manager 
 control.
- CommandKind_Edit_InsertSequence 
 –(Value: 221) Inserts a new empty sequence into the selected sequence file. This command applies to the SequenceFileView Manager control.
- CommandKind_Edit_InsertStep 
 –(Value: 207) Inserts a step into the selected file. You do not create commands of this type. Instead, the
 CommandKind_Edit_InsertSteps_Set 
 and
 CommandKind_Edit_InsertStepsSubmenu 
 constants contain commands of this type as needed. This command applies to the SequenceFileView Manager control.
- CommandKind_Edit_InsertSteps_Set 
 –(Value: 340) Specifies a set of commands that contains a
 CommandKind_Edit_InsertStep 
 command for each available step type. The commands are organized hierarchically as specified for the step types in the
 Step Type Menu Editor 
 dialog box. Insert this command into a menu to create the contents of the Insert Step context menu. This command applies to the SequenceFileView Manager control.
- CommandKind_Edit_InsertStepsSubmenu 
 –(Value: 300) Specifies a container command with subsidiary commands the
 CommandKind_Edit_InsertSteps_Set 
 constant specifies. When you insert this command into a menu, each subsidiary command is visible as a submenu item. This command applies to the SequenceFileView Manager control.
- CommandKind_Edit_NewSequenceFile 
 –(Value: 211) Creates a new, empty sequence file. This command applies to the SequenceFileView Manager control. This command has a default image.
- CommandKind_Edit_Paste 
 –(Value: 205) Pastes the contents of the clipboard into the selected file. This command applies to the SequenceFileView Manager control. This command has a default image.
- CommandKind_Edit_Preconditions 
 –(Value: 218) Launches the
 Preconditions 
 dialog box. This command applies to the SequenceFileView Manager control.
- CommandKind_Edit_Redo 
 –(Value: 201) Calls Redo on the UndoStack of the connected manager control. This command applies to the SequenceFileView Manager and Application Manager controls. When connected to a SequenceFileView Manager control, this command redoes the last edit to the currently selected sequence file an undo command reverted. Before connecting this command to the Application Manager control, you must assign an UndoStack to the
 ApplicationMgr.UndoStack 
 property. This command has a default image.
- CommandKind_Edit_Rename 
 –(Value: 202) Enters name-editing mode for the step with focus or the sequence item in a
 SequenceView 
 or
 ListBox 
 control. This command applies to the SequenceFileView Manager control.
- CommandKind_Edit_Save 
 –(Value: 208) Saves the selected sequence file. This command applies to the SequenceFileView Manager control. This command has a default image.
- CommandKind_Edit_SaveAll 
 –(Value: 210) Saves all modified sequences files. This command has a default image.
- CommandKind_Edit_SaveAs 
 –(Value: 209) Launches the Save As dialog box. The dialog box prompts you to choose a location in which to save the selected sequence file. This command applies to the SequenceFileView Manager control.
- CommandKind_Edit_SelectDefaultAdapter 
 –(Value: 220) Select a specific module adapter for new steps. You do not create commands of this type. Instead, the
 CommandKind_Edit_SelectDefaultAdapters_Set 
 and
 CommandKind_Edit_SelectDefaultAdaptersSubmenu 
 constants contain commands of this type as needed.
- CommandKind_Edit_SelectDefaultAdapters_Set 
 –(Value: 342) Specifies a set of commands that contains a
 CommandKind_Edit_SelectDefaultAdapter 
 command for each module adapter.
- CommandKind_Edit_SelectDefaultAdaptersSubmenu 
 –(Value: 302) Specifies a container command with subsidiary commands the
 CommandKind_Edit_SelectDefaultAdapters_Set 
 constant specifies. When you insert this command into a menu, each subsidiary command is visible as a submenu item.
- CommandKind_Edit_SequenceFileCallbacks 
 –(Value: 222) Launches the
 Sequence File Callbacks 
 dialog box. This command applies to the SequenceFileView Manager control.
- CommandKind_Edit_SequenceFileProperties 
 –(Value: 214) Launches the
 Sequence File Properties 
 dialog box for the selected sequence file.
- CommandKind_Edit_SequenceProperties 
 –(Value: 213) Launches the
 Sequence Properties 
 dialog box for the sequence with focus.
- CommandKind_Edit_SpecifyModule 
 –(Value: 215) Launches the
 Specify Module 
 dialog box for the step with focus. This command applies to the SequenceFileView Manager control.
- CommandKind_Edit_StepProperties 
 –(Value: 212) Launches the
 Step Properties 
 dialog box for the step with focus.
- CommandKind_Edit_Undo 
 –(Value: 200) Calls Undo on the UndoStack of the connected manager control. This command applies to the SequenceFileView Manager and Application Manager controls. When connected to a SequenceFileView Manager control, this command reverts the most recent edit to the currently selected sequence file. Before connecting this command to the Application Manager control, you must assign an UndoStack to the
 ApplicationMgr.UndoStack 
 property. This command has a default image.
- CommandKind_ExecutionEntryPointDefaultMenuInsertionMarker 
 –(Value: 111) Specifies a set of commands that contains a
 CommandKind_RunEntryPoint 
 command for each Execution entry point with a menu hint that does not select a menu other than the current menu. Because most entry points do not have menu hints, this constant typically specifies all Execution entry points.
- CommandKind_ExecutionEntryPointInsertionMarker 
 –(Value: 110) Specifies a set of commands that contains a
 CommandKind_RunEntryPoint 
 command for each Execution entry point with a menu hint that selects the current menu.
- CommandKind_ExecutionEntryPoints_Set 
 –(Value: 141) Specifies a set of commands that contains a
 CommandKind_RunEntryPoint 
 command for each Execution entry point. When you specify commands to create menu items, use the
 CommandKind_ExecutionEntryPointInsertionMarker 
 and
 CommandKind_ExecutionEntryPointDefaultInsertionMarker 
 constants to honor any menu hints the entry points might specify.
- CommandKind_Exit 
 –(Value: 30) Unloads all files and exits the application.
- CommandKind_LockUnlock 
 –(Value: 148) When a sequence file is protected, this command launches the Lock
 File 
 dialog box or the Unlock
 File 
 dialog box, depending on whether the file is currently locked.
- CommandKind_Login 
 –(Value: 25) Launches the user login dialog box.
- CommandKind_LoginLogout 
 –(Value: 27) Launches the user login dialog box when no user is logged in. Otherwise, logs out the current user.
- CommandKind_Logout 
 –(Value: 26) Logs out the current user.
- CommandKind_LoopEntryPointOnSelectedSteps 
 –(Value: 43) Launches the
 Loop On Selected Steps 
 dialog box, in which you can specify how many times the command loops on the selected steps using a specific Process Model entry point sequence. Do not directly create commands of this type. Instead, the following constants contain commands of this type as needed:
 CommandKind_LoopOnSelectedStepsUsingEntryPoints_Set 
 CommandKind_LoopOnSelectedStepsUsingEntryPointsSubmenu 
 This command applies to the ExecutionView Manager and SequenceFileView Manager controls.
- CommandKind_LoopOnSelectedSteps 
 –(Value: 48) Launches the Loop On Selected Steps dialog box, in which you can specify how many times the command loops on the selected steps without using a process model. This command applies to the ExecutionView Manager and SequenceFileView Manager controls.
- CommandKind_LoopOnSelectedStepsUsingEntryPoints_Set 
 –(Value: 144) Specifies a set of
 CommandKind_LoopEntryPointOnSelectedSteps 
 commands that contains a command to run the selected steps with each applicable Execution entry point.
- CommandKind_LoopOnSelectedStepsUsingEntryPointsSubmenu 
 –(Value: 49) For each applicable Process Model entry point, this command contains a subsidiary command that launches the Loop On Selected Steps dialog box, in which you can specify how many times the subsidiary command loops on the selected steps using the entry point. When you insert this command into a menu, each subsidiary command is listed as a submenu item. This command applies to the ExecutionView Manager and SequenceFileView Manager controls.
- CommandKind_MRUFile 
 –(Value: 29) Opens a file in the most recently used (MRU) file list. Each command in the set opens one of the files from the most recently used file list. Do not directly create commands of this type. Instead, use
 CommandKind_MRUFiles_Set 
 to create a set of commands of this type.
- CommandKind_MRUFiles_Set 
 –(Value: 140) Specifies a set of
 CommandKind_MRUFile 
 commands. Each command opens one of the files in the MRU file list. This command applies only to the Application Manager control.
- CommandKind_NotACommand 
 –(Value: 0) Guaranteed to never be a valid command kind specifier.
- CommandKind_OpenSequenceFile 
 –(Value: 20) Launches the Open
 File 
 dialog box. When the user selects a sequence file, the command loads and displays the file. This command has a default image.
- CommandKind_OpenSequenceFiles 
 –(Value: 147) Launches the Open Multiple
 File 
 dialog box, in which the user can select any number of files to open. The command loads all selected sequence files and displays one of the selected sequence files. This command has a default image.
- CommandKind_OpenWorkspaceBrowser 
 –(Value: 24) Launches the
 Workspace Browser 
 dialog box.
- CommandKind_Restart 
 –(Value: 40) Restarts the selected execution. This command applies only to the ExecutionView Manager control. This command has a default image.
- CommandKind_Resume 
 –(Value: 66) Resumes the selected execution. This command applies only to the ExecutionView Manager control. This command has a default image.
- CommandKind_ResumeAll 
 –(Value: 79) Resumes all executions. This command applies only to the Application Manager control. This command has a default image.
- CommandKind_RunCurrentSequence 
 –(Value: 44) Runs the selected sequence without using a process model. This command applies only to the SequenceFileView Manager control. This command has a default image.
- CommandKind_RunEntryPoint 
 –(Value: 41) Runs a particular Process Model entry point sequence. Do not directly create commands of this type. Instead, use one of the following constants to create commands of this type as needed:
 CommandKind_ExecutionEntryPoints_Set 
 CommandKind_ConfigurationEntryPoints_Set 
 CommandKind_ExecutionEntryPointInsertionMarker 
 CommandKind_ExecutionEntryPointDefaultMenuInsertionMarker 
 CommandKind_ConfigurationEntryPointInsertionMarker 
 CommandKind_ConfigurationEntryPointDefaultInsertionMarker 
 This command has a default image.
- CommandKind_RunEntryPointOnSelectedSteps 
 –(Value: 42) Runs the selected steps using a specific Process Model entry point sequence. Do not directly create commands of this type. Instead, use one of the following constants to create commands of this type, as needed:
 CommandKind_RunSelectedStepsUsingEntryPoints_Set 
 CommandKind_RunSelectedStepsUsingEntryPointSubmenu 
 These commands apply only to the SequenceFileView Manager control.
- CommandKind_RunModeForceFail 
 –(Value: 63) Sets the run mode of the selected steps to
 Force Fail 
 . This command applies to the ExecutionView Manager and SequenceFileView Manager controls.
- CommandKind_RunModeForcePass 
 –(Value: 62) Sets the run mode of the selected steps to
 Force Pass 
 . This command applies to the ExecutionView Manager and SequenceFileView Manager controls.
- CommandKind_RunModeNormal 
 –(Value: 65) Sets the run mode of the selected steps to
 Normal 
 . This command applies to the ExecutionView Manager and SequenceFileView Manager controls.
- CommandKind_RunModeSkip 
 –(Value: 64) Sets the run mode of the selected steps to
 Skip 
 . This command applies to the ExecutionView Manager and SequenceFileView Manager controls.
- CommandKind_RunSelectedSteps 
 –(Value: 46) Runs the selected steps without using a process model. This command applies to the ExecutionView Manager and SequenceFileView Manager controls.
- CommandKind_RunSelectedStepsUsingEntryPoints_Set 
 –(Value: 143) Specifies a set of
 CommandKind_RunEntryPointOnSelectedSteps 
 commands that contains a command to run the selected steps with each applicable Execution entry point.
- CommandKind_RunSelectedStepsUsingEntryPointsSubmenu 
 –(Value: 47) For each applicable Process Model entry point, this command contains a subsidiary command that runs the selected steps with that entry point. When you insert this command into a menu, each subsidiary command appears as an item in a submenu. This command applies only to the SequenceFileView Manager control.
- CommandKind_RunSequences_Set 
 –(Value: 142) Specifies a set of
 CommandKind_RunSpecificSequence 
 commands that contains commands to run each sequence in the selected file without using a process model. This command applies only to the SequenceFileView Manager control.
- CommandKind_RunSpecificSequence 
 –(Value: 45) Runs a specific sequence without using a process model. You do not directly create commands of this type. Instead, the
 CommandKinds_RunSequences_Set 
 constant contains commands of this type as needed. This command applies only to the SequenceFileView Manager control.
- CommandKind_SelectAll 
 –(Value: 219) Selects all the items or text in the control with focus.
- CommandKind_Separator 
 –(Value: 2) Denotes a visual separation between other commands. For example, when commands appear as items in a menu, commands of this type appear as menu item separator bars.
- CommandKind_SequenceViewConfiguration 
 –(Value: 116) Do not directly create commands of this type. Instead the
 CommandKind_SequenceViewConfigurations_Set 
 constant contains commands of this type as needed.
- CommandKind_SequenceViewConfigurations_Set 
 –(Value: 139) Specifies a set of
 CommandKind_SequenceViewConfiguration 
 commands. Each command in the set applies a specific configuration to all SequenceView controls that connect to the specified manager control. This command applies to the ExecutionView Manager and SequenceFileView Manager controls.
- CommandKind_SequenceViewConfigurationsSubmenu 
 –(Value: 118) Contains all the
 CommandKind_SequenceViewConfiguration 
 commands the
 CommandKind_SequenceViewConfigurations_Set 
 constant specifies, followed by a
 CommandKind_Separator 
 and a
 CommandKind_ConfigureSequenceViews 
 command. Insert this command into a menu to create a submenu with menu items to apply any existing SequenceView configuration or to edit the set of available configurations. This command applies to the ExecutionView Manager and SequenceFileView Manager controls.
- CommandKind_SetNextStep 
 –(Value: 70) Moves the execution pointer to the selected step. This command applies only to the ExecutionView Manager control. This command has a default image.
- CommandKind_SetRunModeSubmenu 
 –(Value: 61) Contains the following subsidiary commands:
 CommandKind_RunModeForcePass 
 CommandKind_RunModeForceFail 
 CommandKind_RunModeSkip 
 CommandKind_RunModeForceNormal 
 When you insert this command into a menu, each subsidiary command appears as an item in a submenu. This command applies to the ExecutionView Manager and SequenceFileView Manager controls.
- CommandKind_ShowExamples 
 –(Value: 453) Launches the help for the NI TestStand example programs.
- CommandKind_ShowGettingStarted 
 –(Value: 454) Launches the
 Getting Started with TestStand 
 manual.
- CommandKind_ShowGuideToDocumentation 
 –(Value: 421) Launches a topic that is a
 
 guide to the TestStand documentation 
 . This command is visible only when editing is enabled.
- CommandKind_ShowHelpTopic 
 –(Value: 422) Launches the help for the currently active TestStand User Interface Control.
- CommandKind_ShowInList 
 –(Value: 400) Takes the selected step for an ExecutionView Manager control and selects the step in a SequenceFileView Manager control. This command is used in the context menu of a SequenceView control connected to an ExecutionView Manager control, and the command displays the step in the SequenceView control connected to a SequenceFileView Manager control.
- CommandKind_ShowInVariables 
 –(Value: 401) Takes the selected step for an ExecutionView Manager control and selects the step in a VariablesView control connected to the ExecutionView Manager control. This command is used in the context menu of a SequenceView control connected to an ExecutionView Manager control.
- CommandKind_ShowPatents 
 –(Value: 425) Displays a list of National Instruments patents.
- CommandKind_ShowTestStandDiscussionForum 
 –(Value: 424) Opens the
 TestStand discussion forum 
 on
 ni.com 
 in a web browser. This command is visible only when editing is enabled.
- CommandKind_ShowTestStandHelp 
 –(Value: 420) Launches the
 NI TestStand Help 
 file. This command is visible only when editing is enabled.
- CommandKind_ShowTestStandWebResources 
 –(Value: 423) Opens the
 TestStand support web page 
 in a browser. This command is visible only when editing is enabled.
- CommandKind_ShowUpdateService 
 –(Value: 452) Launches the NI Update Service. This option is available only when you have installed the NI Update Service.
- CommandKind_StepInto 
 –(Value: 67) Steps into the current step in the selected execution. This command applies only to the ExecutionView Manager control. This command has a default image.
- CommandKind_StepOut 
 –(Value: 69) Resumes execution through the end of the current sequence and suspends before the next step in the calling sequence. This command applies only to the ExecutionView Manager control. This command has a default image.
- CommandKind_StepOver 
 –(Value: 68) Steps over the current step in the selected execution. This command applies only to the ExecutionView Manager control. This command has a default image.
- CommandKind_Terminate 
 –(Value: 73) Terminates the selected execution. This command applies only to the ExecutionView Manager control. This command has a default image.
- CommandKind_TerminateAll 
 –(Value: 77) Terminates all executions. This command applies only to the Application Manager control. This command has a default image.
- CommandKind_TerminateRestart 
 –(Value: 74) Terminates the selected execution if it is executing or suspended and restarts the selected execution if it has completed. This command applies only to the ExecutionView Manager control. This command has a default image.
- CommandKind_ToggleBreakpoint 
 –(Value: 60) Toggles the breakpoint state of the selected steps. This command applies to the ExecutionView Manager and SequenceFileView Manager controls.
- CommandKind_ToolItem 
 –(Value: 100) Executes a particular tool item in the TestStand Tools menu. Do not directly create commands of this type. Instead, the
 CommandKind_Tools_Set 
 constant contains a command of this type for each item in the TestStand Tools menu.
- CommandKind_Tools_Set 
 –(Value: 146) Specifies a set of
 CommandKind_ToolItem 
 commands that contains a command for each tool item in the Tools menu.
- CommandKind_TracingEnabled 
 –(Value: 53) Toggles whether the user interface application displays the steps in an execution as they execute.
- CommandKind_UnloadAllModules 
 –(Value: 28) Removes all code modules from memory.
- CommandKind_UnloadStepModule 
 –(Value: 455) Displays the module source code for the step with focus. This command is similar to CommandKind_Edit_EditCode, but does not increment the change count of the current sequence file. Unlike CommandKind_Edit_EditCode, this command is available when a sequence file is not editable, such as while the sequence is executing. CommandKind_UnloadStepModule is not available while any executions are actively running; the user must suspend all executions to use this command. This command applies to the SequenceFileView Manager and ExecutionView Manager control.

#### See Also

[Adapter Configuration dialog box](../tsref/adapter-configuration-dialog-box.html)

[ApplicationMgr](applicationmgr.html)

[ApplicationMgr.ConnectCommand](applicationmgr-connectcommand.html)

[ApplicationMgr.PostCommandExecute](applicationmgr-postcommandexecute.html)

[ApplicationMgr.PreCommandExecute](applicationmgr-precommandexecute.html)

[ApplicationMgr.UndoStack](applicationmgr-undostack.html)

[Button](button.html)

[Breakpoint Settings dialog box](../tsref/breakpoint-settings-dialog-box.html)

[Configure menu](../tsref/configure-menu2.html)

[Command](command.html)

[Command.Enabled](command-enabled.html)

[Command.UserData](command-userdata.html)

[Command.UserObject](command-userobject.html)

[Command.Visible](command-visible.html)

[Commands.InsertKind](commands-insertkind.html)

[Commands](commands.html)

[Configure External Viewers dialog box](../tsref/configure-external-viewers-dialog-box.html)

[Connecting Commands to Menu Items](/csh?context=ts_tsfundamentals_menus)

[Customize Tools Menu dialog box](../tsref/customize-tools-menu-dialog-box.html)

[Debug menu](../tsref/debug-menu2.html)

[Edit Breakpoints/Watch Expressions dialog box](../tsref/edit-breakpoints-watch-expressions-dialog-box.html)

[Edit Numeric Limit Test dialog box](../tsref/edit-numeric-limit-test-dialog-box.html)

[Edit menu](../tsref/edit-menu2.html)

[Edit Paths in Files dialog box](../tsref/edit-paths-in-files-dialog-box.html)

[Edit Search Directories dialog box](../tsref/edit-search-directories-dialog-box.html)

[Edit Step List Configurations dialog box](../tsref/edit-step-list-configurations-dialog-box.html)

[Execute menu](../tsref/execute-menu2.html)

[ExecutionViewMgr](executionviewmgr.html)

[ExecutionViewMgr.ConnectCommand](executionviewmgr-connectcommand.html)

[ListBox](listbox.html)

[File menu](../tsref/file-menu2.html)

[Help menu](../tsref/help-menu2.html)

[Lock File dialog box](../tsref/lock-unlock-file-dialog-box.html)

[Loop On Selected Steps dialog box](../tsref/loop-on-selected-steps-dialog-box.html)

[NI TestStand Environment Reference Help](../tsref/teststand-environment-reference-help.html)

[Open File dialog box](../tsref/open-file-dialog-box.html)

[Open Multiple File dialog box](../tsref/open-multiple-file-dialog-box.html)

[Preconditions dialog box](../tsref/preconditions-dialog-box.html)

[Sequence File Callbacks dialog box](../tsref/select-sequence-file-callbacks-dialog-box.html)

[Sequence File Properties dialog box](../tsref/sequence-file-properties-dialog-box.html)

[Sequence Properties dialog box](../tsref/sequence-properties-dialog-box.html)

[SequenceFileViewMgr](sequencefileviewmgr.html)

[SequenceFileViewMgr.ConnectCommand](sequencefileviewmgr-connectcommand.html)

[Sequence List context menu](../tsref/sequences-pane-context-menu-sequence-file-tab.html)

[Sequence View context menu](../tsref/steps-pane-context-menu-sequence-file-tab.html)

[SequenceView](sequenceview.html)

[Specify Module dialog box](../tsref/edit-activex-com-call-dialog-box.html)

[Station Options dialog box](../tsref/station-options-dialog-box.html)

[Step Properties dialog box](../tsref/step-properties-dialog-box.html)

[Step Type Menu Editor dialog box](../tsref/step-type-menu-editor-dialog-box.html)

[Unlock File dialog box](../tsref/lock-unlock-file-dialog-box.html)

[Workspace Browser dialog box](../tsref/workspace-browser-dialog-box.html)

Parent topic:

Support UI Enumerations

<!--NI_TOPIC bundle=teststand-api-reference path=tsuiref/commands-clear.html language=enus -->
## TOPIC 04890: Commands.Clear

- bundle_id: `teststand-api-reference`
- source_path: `tsuiref/commands-clear.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsuiref/commands-clear.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax Commands.Clear Purpose Removes all items from the collection.

### Commands.Clear

#### Syntax

[Commands](commands.html).Clear

#### Purpose

Removes all items from the collection.

Parent topic:

Methods

<!--NI_TOPIC bundle=teststand-api-reference path=tsuiref/commands-count.html language=enus -->
## TOPIC 04891: Commands.Count

- bundle_id: `teststand-api-reference`
- source_path: `tsuiref/commands-count.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsuiref/commands-count.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax Commands.Count Data Type Long Purpose Returns the number of items in the collection.

### Commands.Count

#### Syntax

[Commands](commands.html).Count

#### Data Type

[Long](data-types-for-teststand-user-interface.html)

#### Purpose

Returns the number of items in the collection.

Parent topic:

Properties

<!--NI_TOPIC bundle=teststand-api-reference path=tsuiref/commands-insert.html language=enus -->
## TOPIC 04892: Commands.Insert

- bundle_id: `teststand-api-reference`
- source_path: `tsuiref/commands-insert.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsuiref/commands-insert.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax Commands.Insert( item, insertBefore) Purpose Adds a new item to the collection. Parameters item As Command [In] Specifies the command object to insert. insertBefore As Long [In] Specifies the index of the existing command before which to insert the new command. When you want the new command t

### Commands.Insert

#### Syntax

[Commands](commands.html).Insert( item, insertBefore)

#### Purpose

Adds a new item to the collection.

#### Parameters

item
 As
 [Command](command.html)

[In] Specifies the command object to insert.

insertBefore
 As
 [Long](data-types-for-teststand-user-interface.html)

[In] Specifies the index of the existing command before which to insert the new command. When you want the new command to insert at the end, pass
 -1
 to this parameter.

#### See Also

[ApplicationMgr.GetCommand](applicationmgr-getcommand.html)

Parent topic:

Methods

<!--NI_TOPIC bundle=teststand-api-reference path=tsuiref/commands-insertintowin32menu.html language=enus -->
## TOPIC 04893: Commands.InsertIntoWin32Menu

- bundle_id: `teststand-api-reference`
- source_path: `tsuiref/commands-insertintowin32menu.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsuiref/commands-insertintowin32menu.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax Commands.InsertIntoWin32Menu( menuHandle, menuItemToInsertBefore, byPosition, useShortcutKeys) Purpose Inserts a menu item into a menu for each command in the Commands collection. Use this method to build a context menu for a control that generates the SequenceView.CreateContextMenu or ListBa

### Commands.InsertIntoWin32Menu

#### Syntax

[Commands](commands.html).InsertIntoWin32Menu( menuHandle, menuItemToInsertBefore, byPosition, useShortcutKeys)

#### Purpose

Inserts a menu item into a menu for each command in the Commands collection. Use this method to build a context menu for a control that generates the
 [SequenceView.CreateContextMenu](sequenceview-createcontextmenu.html)
 or
 [ListBar.CreateContextMenu](listbar-createcontextmenu.html)
 event.

#### Parameters

menuHandle
 As
 [Long](data-types-for-teststand-user-interface.html)

[In] Specifies the Microsoft Windows menu handle (HMENU) to insert the menu items into. The menu items invoke their corresponding Command objects when selected. You do not handle menu events for items this method inserts.

menuItemToInsertBefore
 As
 [Long](data-types-for-teststand-user-interface.html)

[In] Specifies the position or menu item identifier (resource ID/command ID) of the menu item before which the method inserts the new menu items. To insert at the end of the menu, pass
 -1
 and pass
 True
 to the
 byPosition
 parameter.

byPosition
 As
 [Boolean](data-types-for-teststand-user-interface.html)

[In] Pass
 True
 when the
 menuItemToInsertBefore
 parameter contains a zero-based menu item position. Pass
 False
 when the
 menuItemToInsertBefore
 parameter contains a menu item identifier (resource ID/command ID).

useShortcutKeys
 As
 [Boolean](data-types-for-teststand-user-interface.html)

[In] Pass
 True
 to show shortcut key text for each item this method inserts that has a shortcut key. Typically, you use this method to build context menus which do not automatically implement shortcut key handling. Therefore, show shortcut keys only for items that also appear in the main menu bar, unless you explicitly provide shortcut key handling for items that appear only in the context menu.

#### See Also

[ListBar.CreateContextMenu](listbar-createcontextmenu.html)

[SequenceView.CreateContextMenu](sequenceview-createcontextmenu.html)

Parent topic:

Methods

<!--NI_TOPIC bundle=teststand-api-reference path=tsuiref/commands-insertkind.html language=enus -->
## TOPIC 04894: Commands.InsertKind

- bundle_id: `teststand-api-reference`
- source_path: `tsuiref/commands-insertkind.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsuiref/commands-insertkind.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax Commands.InsertKind( cmdKind, managerControl, insertBefore, currentMenuName, allMenuNames, numInserted) Purpose Inserts a new Command object or objects into the collection. Remarks This method uses the menu name the currentMenuName parameter specifies to determine whether to insert entry poin

### Commands.InsertKind

#### Syntax

[Commands](commands.html).InsertKind( cmdKind, managerControl, insertBefore, currentMenuName, allMenuNames, numInserted)

#### Purpose

Inserts a new Command object or objects into the collection.

#### Remarks

This method uses the menu name the
 currentMenuName
 parameter specifies to determine whether to insert entry point items that specify a matching menu hint name when you pass the following values to the
 cmdKind
 parameter:

CommandKind_ExecutionEntryPointInsertionMarker
 CommandKind_ConfigurationEntryPointInsertionMarker
 CommandKind_ExecutionEntryPointDefaultMenuInsertionMarker
 CommandKind_ConfigurationEntryPointDefaultMenuInsertionMarker

When an entry point does not specify a menu hint name or the menu hint names do not match any of the menu names listed in the
 allMenuNames
 parameter, the method creates commands to insert the entry point menus when you pass the following values to the
 cmdKind
 parameter:

CommandKind_ExecutionEntryPointDefaultMenuInsertionMarker
 CommandKind_ConfigurationEntryPointDefaultMenuInsertionMarker

#### Parameters

cmdKind
 As
 [CommandKinds](commandkinds.html)

Specifies the type of command to insert. Depending on the value you pass and the state of the application, the method might insert one command, a set of commands, or no commands.

managerControl
 As
 [Object](data-types-for-teststand-user-interface.html)

[In] Pass a
 [SequenceFileView Manager](sequencefileviewmgr.html)
 or
 [ExecutionView Manager](executionviewmgr.html)
 control when the command you insert requires it.

insertBefore
 As
 [Long](data-types-for-teststand-user-interface.html)

[In] Specifies the position in the collection at which to insert the new command. Pass
 -1
 to insert the new command at the end of the collection.

currentMenuName
 As
 [String](data-types-for-teststand-user-interface.html)

[In] Specifies the name of the menu when you create commands to insert into a menu in a top-level menu bar. Otherwise, pass an empty string.

This method ignores accelerator prefix characters when comparing menu hints to the menu name you pass.

allMenuNames
 As
 [String](data-types-for-teststand-user-interface.html)

[In] Specifies the name of all top-level menus in order, separated by commas, when you create commands to insert into a menu in a top-level menu bar. Otherwise, pass an empty string. The commands use this to decide into which menu to insert based on the menu hint name.

This method ignores accelerator prefix characters when comparing menu hints to the menu names you pass.

numInserted
 As
 [Long](data-types-for-teststand-user-interface.html)

[Out] Returns the number of commands the method inserted into the collection.

#### See Also

[Command](command.html)

[CommandKinds](commandkinds.html)

[ExecutionViewMgr](executionviewmgr.html)

[SequenceFileViewMgr](sequencefileviewmgr.html)

Parent topic:

Methods

<!--NI_TOPIC bundle=teststand-api-reference path=tsuiref/commands-item.html language=enus -->
## TOPIC 04895: Commands.Item

- bundle_id: `teststand-api-reference`
- source_path: `tsuiref/commands-item.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsuiref/commands-item.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax Commands.Item( itemIdx) Data Type Command Purpose Returns a reference to an item at the specified index in the collection. Parameters itemIdx As Long [In] Specifies the zero-based index. Use a non-negative number less than the value of the Commands.Count property. See Also Command Commands.Co

### Commands.Item

#### Syntax

[Commands](commands.html).Item( itemIdx)

#### Data Type

[Command](command.html)

#### Purpose

Returns a reference to an item at the specified index in the collection.

#### Parameters

itemIdx
 As
 [Long](data-types-for-teststand-user-interface.html)

[In] Specifies the zero-based index. Use a non-negative number less than the value of the
 [Commands.Count](commands-count.html)
 property.

#### See Also

[Command](command.html)

[Commands.Count](commands-count.html)

Parent topic:

Properties

<!--NI_TOPIC bundle=teststand-api-reference path=tsuiref/commands-remove.html language=enus -->
## TOPIC 04896: Commands.Remove

- bundle_id: `teststand-api-reference`
- source_path: `tsuiref/commands-remove.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsuiref/commands-remove.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax Commands.Remove( itemIdx) Purpose Removes the specified item from this collection, if it exists. Parameters itemIdx As Long [In] Specifies the zero-based index of the item to remove.

### Commands.Remove

#### Syntax

[Commands](commands.html).Remove( itemIdx)

#### Purpose

Removes the specified item from this collection, if it exists.

#### Parameters

itemIdx
 As
 [Long](data-types-for-teststand-user-interface.html)

[In] Specifies the zero-based index of the item to remove.

Parent topic:

Methods

<!--NI_TOPIC bundle=teststand-api-reference path=tsuiref/commands.html language=enus -->
## TOPIC 04897: Commands

- bundle_id: `teststand-api-reference`
- source_path: `tsuiref/commands.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsuiref/commands.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Contains a set of Command objects. To create new commands within the collection, call the Commands.InsertKind method. Properties Count (Read Only) Item (Read Only) Methods Clear Insert InsertIntoWin32Menu InsertKind Remove See Also ApplicationMgr.NewCommands Command Commands.InsertKind

### Commands

Contains a set of
 [Command](command.html)
 objects.

To create new commands within the collection, call the
 [Commands.InsertKind](commands-insertkind.html)
 method.

#### Properties

| Count (Read Only) |
| --- |
| Item (Read Only) |

#### Methods

| Clear |
| --- |
| Insert |
| InsertIntoWin32Menu |
| InsertKind |
| Remove |

#### See Also

[ApplicationMgr.NewCommands](applicationmgr-newcommands.html)

[Command](command.html)

[Commands.InsertKind](commands-insertkind.html)

Parent topic:

TestStand User Interface Controls

<!--NI_TOPIC bundle=teststand-api-reference path=tsuiref/connectionactivitytypes.html language=enus -->
## TOPIC 04898: ConnectionActivityTypes

- bundle_id: `teststand-api-reference`
- source_path: `tsuiref/connectionactivitytypes.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsuiref/connectionactivitytypes.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: This data type contains values that specify the type of change or refresh the connection to a manager control makes to a user interface control. Use these values with a ConnectionActivity event. ConnectionActivityType_BooleanChange –(Value: 3) The connection changed or refreshed the Boolean value of

### ConnectionActivityTypes

This data type contains values that specify the type of change or refresh the connection to a manager control makes to a user interface control. Use these values with a
 ConnectionActivity
 event.

- ConnectionActivityType_BooleanChange 
 –(Value: 3) The connection changed or refreshed the Boolean value of the control.
- ConnectionActivityType_ContentChange 
 –(Value: 5) The connection changed or refreshed the contents of the control, such as the available items in a
 Listbox 
 ,
 Combobox 
 ,
 ReportView 
 , or
 ListBarPage 
 .
- ConnectionActivityType_CursorOrSelectionChange 
 –(Value: 6) The connection changed or refreshed the cursor or selection in the control.
- ConnectionActivityType_EnabledChange 
 –(Value: 7) The connection changed or refreshed the enabled state of the control.
- ConnectionActivityType_ImageChange 
 –(Value: 4) The connection changed or refreshed an image the control displays.
- ConnectionActivityType_NumberChange 
 –(Value: 2) The connection changed or refreshed the numerical value of the control.
- ConnectionActivityType_TextChange 
 –(Value: 1) The connection changed or refreshed the text of the control.
- ConnectionActivityType_VisibleChange 
 –(Value: 8) The connection changed or refreshed the visibility of the control.

#### See Also

[ComboBox](combobox.html)

[ListBarPage](listbarpage.html)

[ListBox](listbox.html)

[ReportView](reportview.html)

Parent topic:

Core UI Enumerations

<!--NI_TOPIC bundle=teststand-api-reference path=tsuiref/contentalignmentstyles.html language=enus -->
## TOPIC 04899: ContentAlignmentStyles

- bundle_id: `teststand-api-reference`
- source_path: `tsuiref/contentalignmentstyles.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsuiref/contentalignmentstyles.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Use these constants to specify the alignment of content on the drawing surface. ContentAlignmentStyle_BottomCenter –(Value: 8) Content is vertically aligned at the bottom and horizontally aligned in the center. ContentAlignmentStyle_BottomLeft –(Value: 6) Content is vertically aligned at the bottom

### ContentAlignmentStyles

Use these constants to specify the alignment of content on the drawing surface.

- ContentAlignmentStyle_BottomCenter 
 –(Value: 8) Content is vertically aligned at the bottom and horizontally aligned in the center.
- ContentAlignmentStyle_BottomLeft 
 –(Value: 6) Content is vertically aligned at the bottom and horizontally aligned on the left.
- ContentAlignmentStyle_BottomRight 
 –(Value: 7) Content is vertically aligned at the bottom and horizontally aligned on the right.
- ContentAlignmentStyle_MiddleCenter 
 –(Value: 2) Content is vertically aligned in the middle and horizontally aligned in the center.
- ContentAlignmentStyle_MiddleLeft 
 –(Value: 0) Content is vertically aligned in the middle and horizontally aligned on the left.
- ContentAlignmentStyle_MiddleRight 
 –(Value: 1) Content is vertically aligned in the middle and horizontally aligned on the right.
- ContentAlignmentStyle_TopCenter 
 –(Value: 5) Content is vertically aligned at the top and horizontally aligned in the center.
- ContentAlignmentStyle_TopLeft 
 –(Value: 3) Content is vertically aligned at the top and horizontally aligned on the left.
- ContentAlignmentStyle_TopRight 
 –(Value: 4) Content is vertically aligned at the top and horizontally aligned on the right.

#### See Also

[Button.ImageAlignment](button-imagealignment.html)

[Button.TextAlignment](button-textalignment.html)

[CheckBox.ImageAlign](checkbox-imagealign.html)

[CheckBox.TextAlign](checkbox-textalign.html)

Parent topic:

Core UI Enumerations

<!--NI_TOPIC bundle=teststand-api-reference path=tsuiref/contextchangedreasons.html language=enus -->
## TOPIC 04900: ContextChangedReasons

- bundle_id: `teststand-api-reference`
- source_path: `tsuiref/contextchangedreasons.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsuiref/contextchangedreasons.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: The ExpressionEdit control passes one of these constants as the reason parameter to the ExpressionEdit.ContextChanged event to specify why the ExpressionEdit control generated the ExpressionEdit.ContextChanged event. ContextChangedReason_ExpressionBrowserDialogBox –(Value: 3) Specifies that the user

### ContextChangedReasons

The
 [ExpressionEdit](expressionedit.html)
 control passes one of these constants as the
 reason
 parameter to the
 [ExpressionEdit.ContextChanged](expressionedit-contextchanged.html)
 event to specify why the ExpressionEdit control generated the
 ExpressionEdit.ContextChanged
 event.

- ContextChangedReason_ExpressionBrowserDialogBox 
 –(Value: 3) Specifies that the user modified the context the
 ExpressionEdit.Context 
 property specifies through the context menu in the
 Expression Browser 
 dialog box. A user can rename, insert, or delete properties. This constant is not set when the user modifies only the value of a variable or property.
- ContextChangedReason_SetContext 
 –(Value: 1) Specifies that the application programmatically set the
 ExpressionEdit.Context 
 property to a new value.
- ContextChangedReason_VariableCreatedFromContextMenu 
 –(Value: 2) Specifies that the user modified the context the
 ExpressionEdit.Context 
 property specifies when creating a variable through the context menu in the ExpressionEdit control.

#### See Also

[Expression Browser dialog box](../tsref/expression-browser-dialog-box.html)

[ExpressionEdit](expressionedit.html)

[ExpressionEdit.Context](expressionedit-context.html)

[ExpressionEdit.ContextChanged](expressionedit-contextchanged.html)

Parent topic:

Core UI Enumerations

<!--NI_TOPIC bundle=teststand-api-reference path=tsuiref/core-ui-constants.html language=enus -->
## TOPIC 04901: Core UI Constants

- bundle_id: `teststand-api-reference`
- source_path: `tsuiref/core-ui-constants.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsuiref/core-ui-constants.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: This book contains information about each core TestStand User Interfaces Control constant.

### Core UI Constants

This book contains information about each core TestStand User Interfaces Control constant.

Parent topic:

UI Constants

<!--NI_TOPIC bundle=teststand-api-reference path=tsuiref/core-ui-enumerations.html language=enus -->
## TOPIC 04902: Core UI Enumerations

- bundle_id: `teststand-api-reference`
- source_path: `tsuiref/core-ui-enumerations.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsuiref/core-ui-enumerations.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: This book contains information about each core TestStand User Interfaces Control enumeration.

### Core UI Enumerations

This book contains information about each core TestStand User Interfaces Control enumeration.

Parent topic:

UI Enumerations

<!--NI_TOPIC bundle=teststand-api-reference path=tsuiref/data-types-for-teststand-user-interface.html language=enus -->
## TOPIC 04903: Data Types for TestStand User Interface

- bundle_id: `teststand-api-reference`
- source_path: `tsuiref/data-types-for-teststand-user-interface.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsuiref/data-types-for-teststand-user-interface.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Type OLE Automation Type Description Boolean VARIANT_BOOL Has the value True ( -1 ) or False ( 0 ). Byte Array SAFEARRAY(unsigned char) An array of bytes. Color OLE_COLOR A color. Many containers treat colors as 32-bit integers. Date DATE DATE is a variant time that is stored as an 8-byte real value

### Data Types for TestStand User Interface

| Type | OLE Automation Type | Description |
| --- | --- | --- |
| Boolean | VARIANT_BOOL | Has the value True ( -1 ) or False ( 0 ). |
| Byte Array | SAFEARRAY(unsigned char) | An array of bytes. |
| Color | OLE_COLOR | A color. Many containers treat colors as 32-bit integers. |
| Date | DATE | DATE is a variant time that is stored as an 8-byte real value (double) and represents a date between January 1, 100 and December 31, 9999, inclusive. The value 0 represents December 30, 1899. Adding 1 to the value increments the date by a day. The fractional part of the value represents the time of day. Negative numbers represent the dates before December 30, 1899. LabWindows/CVI users can use the VariantTimeToSystemTime Microsoft Windows Software Development Kit (SDK) function to convert the variant date to a system time value and then use the GetDateFormat and GetTimeFormat Windows SDK functions to generate display strings. LabVIEW automatically converts the DATE data type to a timestamp. |
| Double | double | 64-bit floating point number. |
| Float | float | 32-bit floating point number. |
| Font | IFontDisp | An Object Linking and Embedding (OLE) Automation Interface to a font . |
| Integer | short | 16-bit signed integer. |
| IUnknown | IUnknown | A generic OLE interface. |
| long | OLE_YPOS_PIXELS | Position on the Y-axis in pixels. |
| Long | Long | 32-bit signed integer. |
| long | OLE_XPOS_PIXELS | Position on the X-axis in pixels. |
| Long | LCID | A locale identifier. |
| Long Array | SAFEARRAY(long) | An array of longs. |
| long long | LONGLONG | 64-bit signed integer. |
| Object | IDispatch | A generic OLE Automation interface. |
| Object Array | SAFEARRAY | An array of objects. |
| Picture | IPicture | An OLE Automation Interface to a Picture object or image. |
| Picture | IPictureDisp | An OLE Automation Interface to a Picture object or image. |
| String | BSTR | A string. |
| String Array | SAFEARRAY(BSTR) | An array of strings. |
| SynchronizationStates |  |  |
| unsigned long long | ULONGLONG | 64-bit unsigned integer. |
| Variant | VARIANT | A variant. |
| VARTYPE | VARTYPE | An enumeration type used to describe a data type of a VARIANT or safearray value. Refer to VARTYPE for more information about VARTYPE enumeration values. |
| WIDESTR(OLD_CONFIG_FILE_HEADER_TYPE) |  |  |

Parent topic:

UI Classes, Properties, Methods, and Events

<!--NI_TOPIC bundle=teststand-api-reference path=tsuiref/displayerroroptions.html language=enus -->
## TOPIC 04904: DisplayErrorOptions

- bundle_id: `teststand-api-reference`
- source_path: `tsuiref/displayerroroptions.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsuiref/displayerroroptions.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Use these constants with the ExpressionEdit.DisplayError method. DisplayError_ForAll –(Value: 0x1) Use this option to show or hide the error for all ExpressionEdit controls. This is useful when you modify a PropertyObject used as the context for several ExpressionEdit controls and you want those Exp

### DisplayErrorOptions

Use these constants with the
 [ExpressionEdit.DisplayError](expressionedit-displayerror.html)
 method.

- DisplayError_ForAll 
 –(Value: 0x1) Use this option to show or hide the error for all
 ExpressionEdit 
 controls. This is useful when you modify a PropertyObject used as the context for several ExpressionEdit controls and you want those ExpressionEdit controls to re-evaluate their expressions for errors.
- DisplayError_NoOptions 
 –(Value: 0x0) No options.

#### See Also

[ExpressionEdit](expressionedit.html)

[ExpressionEdit.DisplayError](expressionedit-displayerror.html)

Parent topic:

Core UI Constants

<!--NI_TOPIC bundle=teststand-api-reference path=tsuiref/edgestyles.html language=enus -->
## TOPIC 04905: EdgeStyles

- bundle_id: `teststand-api-reference`
- source_path: `tsuiref/edgestyles.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsuiref/edgestyles.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: The following constants specify the appearance of the edge of a control or a control element: EdgeStyle_ControlEdge –(Value: 3) The edge has the appearance of a control edge. The appearance can vary depending on the Microsoft Windows appearance settings and on the specific property to which you appl

### EdgeStyles

The following constants specify the appearance of the edge of a control or a control element:

- EdgeStyle_ControlEdge 
 –(Value: 3) The edge has the appearance of a control edge. The appearance can vary depending on the Microsoft Windows appearance settings and on the specific property to which you apply this value.
- EdgeStyle_FixedSingle 
 –(Value: 2) The edge is a black line, one pixel thick.
- EdgeStyle_Flat 
 –(Value: 1) The edge appears flat.
- EdgeStyle_Inset 
 –(Value: 5) The edge has a sunken three-dimensional appearance.
- EdgeStyle_Raised 
 –(Value: 4) The edge has a raised three-dimensional appearance.
- EdgeStyle_UI 
 –(Value: 6) The edge uses the color from the property
 Borders.FrameEdgeUIStyleColor 
 .

#### See Also

[Borders.BorderEdgeStyle](borders-borderedgestyle.html)

[Borders.FrameEdgeStyle](borders-frameedgestyle.html)

Parent topic:

Core UI Enumerations

<!--NI_TOPIC bundle=teststand-api-reference path=tsuiref/editingdenialreasons.html language=enus -->
## TOPIC 04906: EditingDenialReasons

- bundle_id: `teststand-api-reference`
- source_path: `tsuiref/editingdenialreasons.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsuiref/editingdenialreasons.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: This data type contains values that indicate reasons why an editing action cannot take place. Use these constants with the ApplicationMgr.BeginEdit and ApplicationMgr.CanEdit events. EditingDenialReason_IsExecuting –(Value: 0x4) Editing is blocked because the file to edit is executing. EditingDenial

### EditingDenialReasons

This data type contains values that indicate reasons why an editing action cannot take place. Use these constants with the
 [ApplicationMgr.BeginEdit](applicationmgr-beginedit.html)
 and
 [ApplicationMgr.CanEdit](applicationmgr-canedit.html)
 events.

- EditingDenialReason_IsExecuting 
 –(Value: 0x4) Editing is blocked because the file to edit is executing.
- EditingDenialReason_IsLocked 
 –(Value: 0x8) Editing is blocked because the file to edit is locked.
- EditingDenialReason_IsNotEditor 
 –(Value: 0x2) Editing is blocked because the value of the
 ApplicationMgr.IsEditor 
 property is
 False 
 .
- EditingDenialReason_IsReadOnly 
 –(Value: 0x1) Editing is blocked because the file to edit is read-only.
- EditingDenialReason_NoFileEditingPrivilege 
 –(Value: 0x10) Editing is blocked because the current user does not have privileges to edit the file.

#### See Also

[ApplicationMgr.BeginEdit](applicationmgr-beginedit.html)

[ApplicationMgr.CanEdit](applicationmgr-canedit.html)

[ApplicationMgr.IsEditor](applicationmgr-iseditor.html)

Parent topic:

Core UI Enumerations

<!--NI_TOPIC bundle=teststand-api-reference path=tsuiref/editingflags.html language=enus -->
## TOPIC 04907: EditingFlags

- bundle_id: `teststand-api-reference`
- source_path: `tsuiref/editingflags.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsuiref/editingflags.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: This data type contains values that specify general editing capabilities you can selectively enable for certain controls. EditingFlag_Copy –(Value: 8) Copy operation is allowed, when applicable. EditingFlag_CutPasteDelete –(Value: 0x7) Cut, Paste, and Delete operations are allowed, when applicable.

### EditingFlags

This data type contains values that specify general editing capabilities you can selectively enable for certain controls.

- EditingFlag_Copy 
 –(Value: 8) Copy operation is allowed, when applicable.
- EditingFlag_CutPasteDelete 
 –(Value: 0x7) Cut, Paste, and Delete operations are allowed, when applicable.
- EditingFlag_DragDrop 
 –(Value: 16) Drag and Drop operations are allowed, when applicable.
- EditingFlag_Rename 
 –(Value: 32) You can rename items, when applicable.

#### See Also

[ListBox.EditingFlags](listbox-editingflags.html)

[SequenceView.EditingFlags](sequenceview-editingflags.html)

Parent topic:

Core UI Constants

<!--NI_TOPIC bundle=teststand-api-reference path=tsuiref/entrypoint-enabled.html language=enus -->
## TOPIC 04908: EntryPoint.Enabled

- bundle_id: `teststand-api-reference`
- source_path: `tsuiref/entrypoint-enabled.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsuiref/entrypoint-enabled.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax EntryPoint.Enabled Data Type Boolean Purpose Returns a Boolean value that indicates whether the entry point can be used to create an execution. Remarks Use this value to update the enabled state of the control that might call the entry point. When you use a Button control connected to an entr

### EntryPoint.Enabled

#### Syntax

[EntryPoint](entrypoint.html).Enabled

#### Data Type

[Boolean](data-types-for-teststand-user-interface.html)

#### Purpose

Returns a Boolean value that indicates whether the entry point can be used to create an execution.

#### Remarks

Use this value to update the enabled state of the control that might call the entry point. When you use a
 [Button](button.html)
 control connected to an entry point command source, the enabled state of the button updates automatically.

#### See Also

[Button](button.html)

Parent topic:

Properties

<!--NI_TOPIC bundle=teststand-api-reference path=tsuiref/entrypoint-interactiveexecutionallowed.html language=enus -->
## TOPIC 04909: EntryPoint.InteractiveExecutionAllowed

- bundle_id: `teststand-api-reference`
- source_path: `tsuiref/entrypoint-interactiveexecutionallowed.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsuiref/entrypoint-interactiveexecutionallowed.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax EntryPoint.InteractiveExecutionAllowed Data Type Boolean Purpose Returns True if interactive executions are permitted using this entry point. Remarks When this property is True , you can call the EntryPoint.RunSelectedSteps or EntryPoint.LoopOnSelectedSteps methods. See Also EntryPoint.LoopOn

### EntryPoint.InteractiveExecutionAllowed

#### Syntax

[EntryPoint](entrypoint.html).InteractiveExecutionAllowed

#### Data Type

[Boolean](data-types-for-teststand-user-interface.html)

#### Purpose

Returns
 True
 if interactive executions are permitted using this entry point.

#### Remarks

When this property is
 True
 , you can call the
 [EntryPoint.RunSelectedSteps](entrypoint-runselectedsteps.html)
 or
 [EntryPoint.LoopOnSelectedSteps](entrypoint-looponselectedsteps.html)
 methods.

#### See Also

[EntryPoint.LoopOnSelectedSteps](entrypoint-looponselectedsteps.html)

[EntryPoint.RunSelectedSteps](entrypoint-runselectedsteps.html)

Parent topic:

Properties

<!--NI_TOPIC bundle=teststand-api-reference path=tsuiref/entrypoint-looponselectedsteps.html language=enus -->
## TOPIC 04910: EntryPoint.LoopOnSelectedSteps

- bundle_id: `teststand-api-reference`
- source_path: `tsuiref/entrypoint-looponselectedsteps.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsuiref/entrypoint-looponselectedsteps.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax EntryPoint.LoopOnSelectedSteps( [interactiveArgsVal], [editArgsVal]) Return Value Execution The new interactive execution. Purpose Starts an interactive execution that loops on the selected steps using the entry point of the process model. Remarks Use the EntryPoint.InteractiveExecutionAllowe

### EntryPoint.LoopOnSelectedSteps

#### Syntax

[EntryPoint](entrypoint.html).LoopOnSelectedSteps( [interactiveArgsVal], [editArgsVal])

#### Return Value

[Execution](../tsapiref/execution.html)

The new interactive execution.

#### Purpose

Starts an interactive execution that loops on the selected steps using the entry point of the process model.

#### Remarks

Use the
 [EntryPoint.InteractiveExecutionAllowed](entrypoint-interactiveexecutionallowed.html)
 property to determine whether you can call this method.

#### Parameters

interactiveArgsVal
 As
 [Variant](data-types-for-teststand-user-interface.html)

[In] [
 [Optional](/csh?context=ts_tsuiref_optional_parameters)
 ] Specifies an
 
 [InteractiveArgs](../tsapiref/interactiveargs.html)
 object for the new interactive execution. Use this parameter only to override the
 InteractiveArgs
 object the SequenceFileView Manager control creates.

editArgsVal
 As
 [Variant](data-types-for-teststand-user-interface.html)

[In] [
 [Optional](/csh?context=ts_tsuiref_optional_parameters)
 ] Specifies the
 
 [EditArgs](../tsapiref/editargs.html)
 object for the new interactive execution. Use this parameter only to override the
 EditArgs
 object the SequenceFileView Manager control creates.

#### See Also

[CommandKind_LoopEntryPointOnSelectedSteps](commandkinds.html)

[EditArgs](../tsapiref/editargs.html)

[EntryPoint.InteractiveExecutionAllowed](entrypoint-interactiveexecutionallowed.html)

[EntryPoint.Run](entrypoint-run.html)

[EntryPoint.RunSelectedSteps](entrypoint-runselectedsteps.html)

[InteractiveArgs](../tsapiref/interactiveargs.html)

[Omitting Optional Parameters](/csh?context=ts_tsapiref_optional_parameters)

Parent topic:

Methods

<!--NI_TOPIC bundle=teststand-api-reference path=tsuiref/entrypoint-name.html language=enus -->
## TOPIC 04911: EntryPoint.Name

- bundle_id: `teststand-api-reference`
- source_path: `tsuiref/entrypoint-name.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsuiref/entrypoint-name.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax EntryPoint.Name Data Type String Purpose Returns the display name of the entry point.

### EntryPoint.Name

#### Syntax

[EntryPoint](entrypoint.html).Name

#### Data Type

[String](data-types-for-teststand-user-interface.html)

#### Purpose

Returns the display name of the entry point.

Parent topic:

Properties

<!--NI_TOPIC bundle=teststand-api-reference path=tsuiref/entrypoint-run.html language=enus -->
## TOPIC 04912: EntryPoint.Run

- bundle_id: `teststand-api-reference`
- source_path: `tsuiref/entrypoint-run.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsuiref/entrypoint-run.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax EntryPoint.Run( [editArgsVal]) Return Value Execution The new execution. Purpose Runs the entry point. Parameters editArgsVal As Variant [In] [ Optional ] Specifies the EditArgs object for the new execution. Use this parameter only to override the EditArgs object the SequenceFileView Manager

### EntryPoint.Run

#### Syntax

[EntryPoint](entrypoint.html).Run( [editArgsVal])

#### Return Value

[Execution](../tsapiref/execution.html)

The new execution.

#### Purpose

Runs the entry point.

#### Parameters

editArgsVal
 As
 [Variant](data-types-for-teststand-user-interface.html)

[In] [
 [Optional](/csh?context=ts_tsuiref_optional_parameters)
 ] Specifies the
 
 [EditArgs](../tsapiref/editargs.html)
 object for the new execution. Use this parameter only to override the
 EditArgs
 object the SequenceFileView Manager control creates.

#### See Also

[CommandKind_RunEntryPoint](commandkinds.html)

[EditArgs](../tsapiref/editargs.html)

[EntryPoint.LoopOnSelectedSteps](entrypoint-looponselectedsteps.html)

[EntryPoint.RunSelectedSteps](entrypoint-runselectedsteps.html)

[Omitting Optional Parameters](/csh?context=ts_tsapiref_optional_parameters)

Parent topic:

Methods

<!--NI_TOPIC bundle=teststand-api-reference path=tsuiref/entrypoint-runselectedsteps.html language=enus -->
## TOPIC 04913: EntryPoint.RunSelectedSteps

- bundle_id: `teststand-api-reference`
- source_path: `tsuiref/entrypoint-runselectedsteps.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsuiref/entrypoint-runselectedsteps.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax EntryPoint.RunSelectedSteps( [interactiveArgsVal], [editArgsVal]) Return Value Execution The new interactive execution Purpose Starts an interactive execution that runs the selected steps using the entry point of the process model. Remarks Use the EntryPoint.InteractiveExecutionAllowed proper

### EntryPoint.RunSelectedSteps

#### Syntax

[EntryPoint](entrypoint.html).RunSelectedSteps( [interactiveArgsVal], [editArgsVal])

#### Return Value

[Execution](../tsapiref/execution.html)

The new interactive execution

#### Purpose

Starts an interactive execution that runs the selected steps using the entry point of the process model.

#### Remarks

Use the
 [EntryPoint.InteractiveExecutionAllowed](entrypoint-interactiveexecutionallowed.html)
 property to determine whether you can call this method.

#### Parameters

interactiveArgsVal
 As
 [Variant](data-types-for-teststand-user-interface.html)

[In] [
 [Optional](/csh?context=ts_tsuiref_optional_parameters)
 ] Specifies the
 
 [InteractiveArgs](../tsapiref/interactiveargs.html)
 objects for the new interactive execution. Use this parameter only to override the
 InteractiveArgs
 objects the SequenceFileView Manager control creates.

editArgsVal
 As
 [Variant](data-types-for-teststand-user-interface.html)

[In] [
 [Optional](/csh?context=ts_tsuiref_optional_parameters)
 ] Specifies the
 
 [EditArgs](../tsapiref/editargs.html)
 object for the new interactive execution. Use this parameter only to override the
 EditArgs
 object the SequenceFileView Manager control creates.

#### See Also

[CommandKind_RunEntryPointOnSelectedSteps](commandkinds.html)

[EditArgs](../tsapiref/editargs.html)

[EntryPoint.InteractiveExecutionAllowed](entrypoint-interactiveexecutionallowed.html)

[EntryPoint.LoopOnSelectedSteps](entrypoint-looponselectedsteps.html)

[EntryPoint.Run](entrypoint-run.html)

[InteractiveArgs](../tsapiref/interactiveargs.html)

[Omitting Optional Parameters](/csh?context=ts_tsapiref_optional_parameters)

Parent topic:

Methods

<!--NI_TOPIC bundle=teststand-api-reference path=tsuiref/entrypoint-sequence.html language=enus -->
## TOPIC 04914: EntryPoint.Sequence

- bundle_id: `teststand-api-reference`
- source_path: `tsuiref/entrypoint-sequence.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsuiref/entrypoint-sequence.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax EntryPoint.Sequence Data Type Sequence Purpose Returns the sequence that defines this entry point. Remarks Use this property to access additional information about the entry point you cannot obtain from properties or methods of the entry point. For example, use this property to determine whet

### EntryPoint.Sequence

#### Syntax

[EntryPoint](entrypoint.html).Sequence

#### Data Type

[Sequence](../tsapiref/sequence.html)

#### Purpose

Returns the sequence that defines this entry point.

#### Remarks

Use this property to access additional information about the entry point you cannot obtain from properties or methods of the entry point. For example, use this property to determine whether the entry point is an Execution or a Configuration entry point.

#### See Also

[Sequence](../tsapiref/sequence.html)

Parent topic:

Properties

<!--NI_TOPIC bundle=teststand-api-reference path=tsuiref/entrypoint.html language=enus -->
## TOPIC 04915: EntryPoint

- bundle_id: `teststand-api-reference`
- source_path: `tsuiref/entrypoint.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsuiref/entrypoint.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: An EntryPoint object represents an Execution or Configuration entry point. You can execute the entry point sequence using the EntryPoint.LoopOnSelectedSteps , EntryPoint.Run , or EntryPoint.RunSelectedSteps methods. Use the ExecutionViewMgr.ConfigurationEntryPoints , ExecutionViewMgr.ExecutionEntryP

### EntryPoint

An EntryPoint object represents an Execution or Configuration entry point. You can execute the entry point sequence using the
 [EntryPoint.LoopOnSelectedSteps](entrypoint-looponselectedsteps.html)
 ,
 [EntryPoint.Run](entrypoint-run.html)
 , or
 [EntryPoint.RunSelectedSteps](entrypoint-runselectedsteps.html)
 methods.

Use the
 [ExecutionViewMgr.ConfigurationEntryPoints](executionviewmgr-configurationentrypoints.html)
 ,
 [ExecutionViewMgr.ExecutionEntryPoints](executionviewmgr-executionentrypoints.html)
 ,
 [SequenceFileViewMgr.ConfigurationEntryPoints](sequencefileviewmgr-configurationentrypoints.html)
 , and
 [SequenceFileViewMgr.ExecutionEntryPoints](sequencefileviewmgr-executionentrypoints.html)
 properties to retrieve an EntryPoints object that is a collection of entry points.

#### Properties

| Enabled (Read Only) |
| --- |
| InteractiveExecutionAllowed (Read Only) |
| Name (Read Only) |
| Sequence (Read Only) |

#### Methods

| LoopOnSelectedSteps |
| --- |
| Run |
| RunSelectedSteps |

#### See Also

[Commands.InsertKind](commands-insertkind.html)

[EntryPoints](entrypoints.html)

[ExecutionViewMgr](executionviewmgr.html)

[ExecutionViewMgr.ConfigurationEntryPoints](executionviewmgr-configurationentrypoints.html)

[ExecutionViewMgr.ExecutionEntryPoints](executionviewmgr-executionentrypoints.html)

[SequenceFileViewMgr](sequencefileviewmgr.html)

[SequenceFileViewMgr.ConfigurationEntryPoints](sequencefileviewmgr-configurationentrypoints.html)

[SequenceFileViewMgr.ExecutionEntryPoints](sequencefileviewmgr-executionentrypoints.html)

Parent topic:

TestStand User Interface Controls

<!--NI_TOPIC bundle=teststand-api-reference path=tsuiref/entrypoints-count.html language=enus -->
## TOPIC 04916: EntryPoints.Count

- bundle_id: `teststand-api-reference`
- source_path: `tsuiref/entrypoints-count.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsuiref/entrypoints-count.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax EntryPoints.Count Data Type Long Purpose Returns the number of items in the collection.

### EntryPoints.Count

#### Syntax

[EntryPoints](entrypoints.html).Count

#### Data Type

[Long](data-types-for-teststand-user-interface.html)

#### Purpose

Returns the number of items in the collection.

Parent topic:

Properties

<!--NI_TOPIC bundle=teststand-api-reference path=tsuiref/entrypoints-item.html language=enus -->
## TOPIC 04917: EntryPoints.Item

- bundle_id: `teststand-api-reference`
- source_path: `tsuiref/entrypoints-item.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsuiref/entrypoints-item.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax EntryPoints.Item( entryPointIndexParam) Data Type EntryPoint Purpose Returns a reference to an item at the specified index in the collection. Parameters entryPointIndexParam As Variant [In] Specifies the zero-based index. Use a non-negative number less than the value of the EntryPoints.Count

### EntryPoints.Item

#### Syntax

[EntryPoints](entrypoints.html).Item( entryPointIndexParam)

#### Data Type

[EntryPoint](entrypoint.html)

#### Purpose

Returns a reference to an item at the specified index in the collection.

#### Parameters

entryPointIndexParam
 As
 [Variant](data-types-for-teststand-user-interface.html)

[In] Specifies the zero-based index. Use a non-negative number less than the value of the
 [EntryPoints.Count](entrypoints-count.html)
 property.

#### See Also

[EntryPoint](entrypoint.html)

[EntryPoints.Count](entrypoints-count.html)

Parent topic:

Properties

<!--NI_TOPIC bundle=teststand-api-reference path=tsuiref/entrypoints.html language=enus -->
## TOPIC 04918: EntryPoints

- bundle_id: `teststand-api-reference`
- source_path: `tsuiref/entrypoints.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsuiref/entrypoints.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: A Collection of EntryPoint objects. Use the ConfigurationEntryPoints and ExecutionEntryPoints methods of the SequenceFileView Manager and ExecutionView Manager controls to retrieve an EntryPoints object. Properties Count (Read Only) Item (Read Only) See Also Commands.InsertKind EntryPoint ExecutionV

### EntryPoints

A Collection of EntryPoint objects. Use the
 ConfigurationEntryPoints
 and
 ExecutionEntryPoints
 methods of the
 [SequenceFileView Manager](sequencefileviewmgr.html)
 and
 [ExecutionView Manager](executionviewmgr.html)
 controls to retrieve an EntryPoints object.

#### Properties

| Count (Read Only) |
| --- |
| Item (Read Only) |

#### See Also

[Commands.InsertKind](commands-insertkind.html)

[EntryPoint](entrypoint.html)

[ExecutionViewMgr](executionviewmgr.html)

[ExecutionViewMgr.ConfigurationEntryPoints](executionviewmgr-configurationentrypoints.html)

[ExecutionViewMgr.ExecutionEntryPoints](executionviewmgr-executionentrypoints.html)

[SequenceFileViewMgr](sequencefileviewmgr.html)

[SequenceFileViewMgr.ConfigurationEntryPoints](sequencefileviewmgr-configurationentrypoints.html)

[SequenceFileViewMgr.ExecutionEntryPoints](sequencefileviewmgr-executionentrypoints.html)

Parent topic:

TestStand User Interface Controls

<!--NI_TOPIC bundle=teststand-api-reference path=tsuiref/errorcheck.html language=enus -->
## TOPIC 04919: ErrorCheck

- bundle_id: `teststand-api-reference`
- source_path: `tsuiref/errorcheck.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsuiref/errorcheck.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Use these constants with the ExpressionEdit.ErrorCheck property. ErrorCheck_None –(Value: 0) No error checking. ErrorCheck_Syntax –(Value: 1) Checks only for syntax errors. ErrorCheck_SyntaxAndEvaluation –(Value: 2) Checks for syntax and evaluation errors. See Also ExpressionEdit.ErrorCheck

### ErrorCheck

Use these constants with the
 [ExpressionEdit.ErrorCheck](expressionedit-errorcheck.html)
 property.

- ErrorCheck_None 
 –(Value: 0) No error checking.
- ErrorCheck_Syntax 
 –(Value: 1) Checks only for syntax errors.
- ErrorCheck_SyntaxAndEvaluation 
 –(Value: 2) Checks for syntax and evaluation errors.

#### See Also

[ExpressionEdit.ErrorCheck](expressionedit-errorcheck.html)

Parent topic:

Core UI Enumerations

<!--NI_TOPIC bundle=teststand-api-reference path=tsuiref/events.html language=enus -->
## TOPIC 04920: Events

- bundle_id: `teststand-api-reference`
- source_path: `tsuiref/events.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsuiref/events.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: This book contains the events in this class.

### Events

This book contains the events in this class.

Parent topic:

ApplicationMgr

<!--NI_TOPIC bundle=teststand-api-reference path=tsuiref/events_10.html language=enus -->
## TOPIC 04921: Events

- bundle_id: `teststand-api-reference`
- source_path: `tsuiref/events_10.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsuiref/events_10.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: This book contains the events in this class.

### Events

This book contains the events in this class.

Parent topic:

ListBox

<!--NI_TOPIC bundle=teststand-api-reference path=tsuiref/events_11.html language=enus -->
## TOPIC 04922: Events

- bundle_id: `teststand-api-reference`
- source_path: `tsuiref/events_11.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsuiref/events_11.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: This book contains the events in this class.

### Events

This book contains the events in this class.

Parent topic:

ReportView

<!--NI_TOPIC bundle=teststand-api-reference path=tsuiref/events_12.html language=enus -->
## TOPIC 04923: Events

- bundle_id: `teststand-api-reference`
- source_path: `tsuiref/events_12.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsuiref/events_12.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: This book contains the events in this class.

### Events

This book contains the events in this class.

Parent topic:

SequenceFileViewMgr

<!--NI_TOPIC bundle=teststand-api-reference path=tsuiref/events_13.html language=enus -->
## TOPIC 04924: Events

- bundle_id: `teststand-api-reference`
- source_path: `tsuiref/events_13.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsuiref/events_13.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: This book contains the events in this class.

### Events

This book contains the events in this class.

Parent topic:

SequenceView

<!--NI_TOPIC bundle=teststand-api-reference path=tsuiref/events_14.html language=enus -->
## TOPIC 04925: Events

- bundle_id: `teststand-api-reference`
- source_path: `tsuiref/events_14.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsuiref/events_14.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: This book contains the events in this class.

### Events

This book contains the events in this class.

Parent topic:

StatusBar

<!--NI_TOPIC bundle=teststand-api-reference path=tsuiref/events_15.html language=enus -->
## TOPIC 04926: Events

- bundle_id: `teststand-api-reference`
- source_path: `tsuiref/events_15.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsuiref/events_15.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: This book contains the events in this class.

### Events

This book contains the events in this class.

Parent topic:

VariablesView

<!--NI_TOPIC bundle=teststand-api-reference path=tsuiref/events_2.html language=enus -->
## TOPIC 04927: Events

- bundle_id: `teststand-api-reference`
- source_path: `tsuiref/events_2.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsuiref/events_2.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: This book contains the events in this class.

### Events

This book contains the events in this class.

Parent topic:

Button

<!--NI_TOPIC bundle=teststand-api-reference path=tsuiref/events_3.html language=enus -->
## TOPIC 04928: Events

- bundle_id: `teststand-api-reference`
- source_path: `tsuiref/events_3.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsuiref/events_3.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: This book contains the events in this class.

### Events

This book contains the events in this class.

Parent topic:

CheckBox

<!--NI_TOPIC bundle=teststand-api-reference path=tsuiref/events_4.html language=enus -->
## TOPIC 04929: Events

- bundle_id: `teststand-api-reference`
- source_path: `tsuiref/events_4.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsuiref/events_4.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: This book contains the events in this class.

### Events

This book contains the events in this class.

Parent topic:

ComboBox

<!--NI_TOPIC bundle=teststand-api-reference path=tsuiref/events_5.html language=enus -->
## TOPIC 04930: Events

- bundle_id: `teststand-api-reference`
- source_path: `tsuiref/events_5.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsuiref/events_5.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: This book contains the events in this class.

### Events

This book contains the events in this class.

Parent topic:

ExecutionViewMgr

<!--NI_TOPIC bundle=teststand-api-reference path=tsuiref/events_6.html language=enus -->
## TOPIC 04931: Events

- bundle_id: `teststand-api-reference`
- source_path: `tsuiref/events_6.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsuiref/events_6.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: This book contains the events in this class.

### Events

This book contains the events in this class.

Parent topic:

ExpressionEdit

<!--NI_TOPIC bundle=teststand-api-reference path=tsuiref/events_7.html language=enus -->
## TOPIC 04932: Events

- bundle_id: `teststand-api-reference`
- source_path: `tsuiref/events_7.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsuiref/events_7.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: This book contains the events in this class.

### Events

This book contains the events in this class.

Parent topic:

InsertionPalette

<!--NI_TOPIC bundle=teststand-api-reference path=tsuiref/events_8.html language=enus -->
## TOPIC 04933: Events

- bundle_id: `teststand-api-reference`
- source_path: `tsuiref/events_8.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsuiref/events_8.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: This book contains the events in this class.

### Events

This book contains the events in this class.

Parent topic:

Label

<!--NI_TOPIC bundle=teststand-api-reference path=tsuiref/events_9.html language=enus -->
## TOPIC 04934: Events

- bundle_id: `teststand-api-reference`
- source_path: `tsuiref/events_9.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsuiref/events_9.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: This book contains the events in this class.

### Events

This book contains the events in this class.

Parent topic:

ListBar

<!--NI_TOPIC bundle=teststand-api-reference path=tsuiref/executiondisplayreasons.html language=enus -->
## TOPIC 04935: ExecutionDisplayReasons

- bundle_id: `teststand-api-reference`
- source_path: `tsuiref/executiondisplayreasons.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsuiref/executiondisplayreasons.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: These constants are passed as a parameter in the ApplicationMgr.DisplayExecution event to provide the reason for why the event was generated. ExecutionDisplayReason_BreakOnRunTimeError –(Value: 4) Event occurred because the execution was paused as a result of a run-time error. ExecutionDisplayReason

### ExecutionDisplayReasons

These constants are passed as a parameter in the
 [ApplicationMgr.DisplayExecution](applicationmgr-displayexecution.html)
 event to provide the reason for why the event was generated.

- ExecutionDisplayReason_BreakOnRunTimeError 
 –(Value: 4) Event occurred because the execution was paused as a result of a run-time error.
- ExecutionDisplayReason_BreakOnUserRequest 
 –(Value: 3) Event occurred because the user paused the execution.
- ExecutionDisplayReason_Breakpoint 
 –(Value: 2) Event occurred because the execution hit a breakpoint.
- ExecutionDisplayReason_GotoLocation 
 –(Value: 5) Event occurred because of a request to display a location that resides in the execution.
- ExecutionDisplayReason_StartExecution 
 –(Value: 1) Event occurred because the execution was started.
- ExecutionDisplayReason_UIMessage 
 –(Value: 0) Event occurred because the TestStand Engine sent the
 UIMsg_OpenWindows 
 message for the execution.

#### See Also

[ApplicationMgr.DisplayExecution](applicationmgr-displayexecution.html)

[UIMessageCodes](../tsapiref/uimessagecodes.html)

Parent topic:

Core UI Enumerations

<!--NI_TOPIC bundle=teststand-api-reference path=tsuiref/executionlistconnection-displayexpression.html language=enus -->
## TOPIC 04936: ExecutionListConnection.DisplayExpression

- bundle_id: `teststand-api-reference`
- source_path: `tsuiref/executionlistconnection-displayexpression.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsuiref/executionlistconnection-displayexpression.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax ExecutionListConnection.DisplayExpression Data Type String Purpose Specifies how to display executions in the execution list using a format expression. By default, the value of this property is "%CurrentExecution%" . Refer to the CaptionSource_MacroExpression enumeration value for more inform

### ExecutionListConnection.DisplayExpression

#### Syntax

[ExecutionListConnection](executionlistconnection.html).DisplayExpression

#### Data Type

[String](data-types-for-teststand-user-interface.html)

#### Purpose

Specifies how to display executions in the execution list using a format expression. By default, the value of this property is
 "%CurrentExecution%"
 . Refer to the
 [CaptionSource_MacroExpression](captionsources.html)
 enumeration value for more information about types of caption sources.

#### See Also

[CaptionSource_MacroExpression](captionsources.html)

Parent topic:

Properties

<!--NI_TOPIC bundle=teststand-api-reference path=tsuiref/executionlistconnection-showhiddenexecutions.html language=enus -->
## TOPIC 04937: ExecutionListConnection.ShowHiddenExecutions

- bundle_id: `teststand-api-reference`
- source_path: `tsuiref/executionlistconnection-showhiddenexecutions.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsuiref/executionlistconnection-showhiddenexecutions.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax ExecutionListConnection.ShowHiddenExecutions Data Type Boolean Purpose When this property is True , the execution list shows executions created with the ExecTypeMask_InitiallyHidden flag.

### ExecutionListConnection.ShowHiddenExecutions

#### Syntax

[ExecutionListConnection](executionlistconnection.html).ShowHiddenExecutions

#### Data Type

[Boolean](data-types-for-teststand-user-interface.html)

#### Purpose

When this property is
 True
 , the execution list shows executions created with the
 ExecTypeMask_InitiallyHidden
 flag.

Parent topic:

Properties

<!--NI_TOPIC bundle=teststand-api-reference path=tsuiref/executionlistconnection.html language=enus -->
## TOPIC 04938: ExecutionListConnection

- bundle_id: `teststand-api-reference`
- source_path: `tsuiref/executionlistconnection.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsuiref/executionlistconnection.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Represents a connection from the ExecutionView Manager control to a control that displays the list of currently running executions. You can use the connected control to select an execution from the list of executions. Properties DisplayExpression ShowHiddenExecutions See Also ExecutionListConnection

### ExecutionListConnection

Represents a connection from the
 [ExecutionView Manager](executionviewmgr.html)
 control to a control that displays the list of currently running executions. You can use the connected control to select an execution from the list of executions.

#### Properties

| DisplayExpression |
| --- |
| ShowHiddenExecutions |

#### See Also

[ExecutionListConnections](executionlistconnections.html)

[ExecutionView Manager](executionviewmgr.html)

Parent topic:

TestStand User Interface Support Controls

<!--NI_TOPIC bundle=teststand-api-reference path=tsuiref/executionlistconnections-add.html language=enus -->
## TOPIC 04939: ExecutionListConnections.Add

- bundle_id: `teststand-api-reference`
- source_path: `tsuiref/executionlistconnections-add.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsuiref/executionlistconnections-add.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax ExecutionListConnections.Add( uiObj) Return Value ExecutionListConnection New ExecutionListConnection. Purpose Creates and adds a new ExecutionListConnection to the collection. Parameters uiObj As Object [In] Specifies the user interface object to connect. See Also ExecutionListConnections.Re

### ExecutionListConnections.Add

#### Syntax

[ExecutionListConnections](executionlistconnections.html).Add( uiObj)

#### Return Value

[ExecutionListConnection](executionlistconnection.html)

New ExecutionListConnection.

#### Purpose

Creates and adds a new ExecutionListConnection to the collection.

#### Parameters

uiObj
 As
 [Object](data-types-for-teststand-user-interface.html)

[In] Specifies the user interface object to connect.

#### See Also

[ExecutionListConnections.Remove](executionlistconnections-remove.html)

[ExecutionViewMgr.ConnectExecutionList](executionviewmgr-connectexecutionlist.html)

Parent topic:

Methods

<!--NI_TOPIC bundle=teststand-api-reference path=tsuiref/executionlistconnections-clear.html language=enus -->
## TOPIC 04940: ExecutionListConnections.Clear

- bundle_id: `teststand-api-reference`
- source_path: `tsuiref/executionlistconnections-clear.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsuiref/executionlistconnections-clear.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax ExecutionListConnections.Clear Purpose Removes all items from the collection. See Also ExecutionListConnections.Remove

### ExecutionListConnections.Clear

#### Syntax

[ExecutionListConnections](executionlistconnections.html).Clear

#### Purpose

Removes all items from the collection.

#### See Also

[ExecutionListConnections.Remove](executionlistconnections-remove.html)

Parent topic:

Methods

<!--NI_TOPIC bundle=teststand-api-reference path=tsuiref/executionlistconnections-count.html language=enus -->
## TOPIC 04941: ExecutionListConnections.Count

- bundle_id: `teststand-api-reference`
- source_path: `tsuiref/executionlistconnections-count.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsuiref/executionlistconnections-count.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax ExecutionListConnections.Count Data Type Long Purpose Returns the number of items in the collection.

### ExecutionListConnections.Count

#### Syntax

[ExecutionListConnections](executionlistconnections.html).Count

#### Data Type

[Long](data-types-for-teststand-user-interface.html)

#### Purpose

Returns the number of items in the collection.

Parent topic:

Properties

<!--NI_TOPIC bundle=teststand-api-reference path=tsuiref/executionlistconnections-fromcontrol.html language=enus -->
## TOPIC 04942: ExecutionListConnections.FromControl

- bundle_id: `teststand-api-reference`
- source_path: `tsuiref/executionlistconnections-fromcontrol.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsuiref/executionlistconnections-fromcontrol.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax ExecutionListConnections.FromControl( uiObj) Return Value ExecutionListConnection ExecutionListConnection connected to the uiObj parameter. When no ExecutionListConnection exists for this control, this method returns NULL . Purpose Returns the ExecutionListConnection connected to the uiObj pa

### ExecutionListConnections.FromControl

#### Syntax

[ExecutionListConnections](executionlistconnections.html).FromControl( uiObj)

#### Return Value

[ExecutionListConnection](executionlistconnection.html)

ExecutionListConnection connected to the
 uiObj
 parameter. When no ExecutionListConnection exists for this control, this method returns
 NULL
 .

#### Purpose

Returns the ExecutionListConnection connected to the
 uiObj
 parameter.

#### Parameters

uiObj
 As
 [Object](data-types-for-teststand-user-interface.html)

[In] Specifies the connected user interface object.

Parent topic:

Methods

<!--NI_TOPIC bundle=teststand-api-reference path=tsuiref/executionlistconnections-item.html language=enus -->
## TOPIC 04943: ExecutionListConnections.Item

- bundle_id: `teststand-api-reference`
- source_path: `tsuiref/executionlistconnections-item.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsuiref/executionlistconnections-item.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax ExecutionListConnections.Item( itemIndex) Data Type ExecutionListConnection Item located at the specified index. Purpose Returns a reference to an item at the specified index in the collection. Parameters itemIndex As Long [In] Specifies the index of the item to retrieve. See Also ExecutionLi

### ExecutionListConnections.Item

#### Syntax

[ExecutionListConnections](executionlistconnections.html).Item( itemIndex)

#### Data Type

[ExecutionListConnection](executionlistconnection.html)

Item located at the specified index.

#### Purpose

Returns a reference to an item at the specified index in the collection.

#### Parameters

itemIndex
 As
 [Long](data-types-for-teststand-user-interface.html)

[In] Specifies the index of the item to retrieve.

#### See Also

[ExecutionListConnection](executionlistconnection.html)

[ExecutionListConnections.Count](executionlistconnections-count.html)

Parent topic:

Properties

<!--NI_TOPIC bundle=teststand-api-reference path=tsuiref/executionlistconnections-remove.html language=enus -->
## TOPIC 04944: ExecutionListConnections.Remove

- bundle_id: `teststand-api-reference`
- source_path: `tsuiref/executionlistconnections-remove.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsuiref/executionlistconnections-remove.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax ExecutionListConnections.Remove( uiObj) Return Value Boolean Returns True when the ExecutionListConnection is removed. Returns False when the ExecutionListConnection is not found. Purpose Removes the specified item from this collection, if it exists. Parameters uiObj As Object [In] Specifies

### ExecutionListConnections.Remove

#### Syntax

[ExecutionListConnections](executionlistconnections.html).Remove( uiObj)

#### Return Value

[Boolean](data-types-for-teststand-user-interface.html)

Returns
 True
 when the
 [ExecutionListConnection](executionlistconnection.html)
 is removed. Returns
 False
 when the
 ExecutionListConnection
 is not found.

#### Purpose

Removes the specified item from this collection, if it exists.

#### Parameters

uiObj
 As
 [Object](data-types-for-teststand-user-interface.html)

[In] Specifies the user interface object to disconnect.

#### See Also

[ExecutionListConnection](executionlistconnection.html)

[ExecutionListConnections.Add](executionlistconnections-add.html)

Parent topic:

Methods

<!--NI_TOPIC bundle=teststand-api-reference path=tsuiref/executionlistconnections.html language=enus -->
## TOPIC 04945: ExecutionListConnections

- bundle_id: `teststand-api-reference`
- source_path: `tsuiref/executionlistconnections.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsuiref/executionlistconnections.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: A collection of ExecutionListConnection objects. Properties Count (Read Only) Item (Read Only) Methods Add Clear FromControl Remove See Also ExecutionListConnection

### ExecutionListConnections

A collection of
 [ExecutionListConnection](executionlistconnection.html)
 objects.

#### Properties

| Count (Read Only) |
| --- |
| Item (Read Only) |

#### Methods

| Add |
| --- |
| Clear |
| FromControl |
| Remove |

#### See Also

[ExecutionListConnection](executionlistconnection.html)

Parent topic:

TestStand User Interface Support Controls

<!--NI_TOPIC bundle=teststand-api-reference path=tsuiref/executions-count.html language=enus -->
## TOPIC 04946: Executions.Count

- bundle_id: `teststand-api-reference`
- source_path: `tsuiref/executions-count.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsuiref/executions-count.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax Executions.Count Data Type Long Purpose Returns the number of items in the collection.

### Executions.Count

#### Syntax

[Executions](executions.html).Count

#### Data Type

[Long](data-types-for-teststand-user-interface.html)

#### Purpose

Returns the number of items in the collection.

Parent topic:

Properties

<!--NI_TOPIC bundle=teststand-api-reference path=tsuiref/executions-item.html language=enus -->
## TOPIC 04947: Executions.Item

- bundle_id: `teststand-api-reference`
- source_path: `tsuiref/executions-item.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsuiref/executions-item.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax Executions.Item( itemIdx) Data Type Execution Purpose Returns a reference to an item at the specified index in the collection. Parameters itemIdx As Long [In] Specifies the zero-based index. Use a non-negative number less than the value of the Executions.Count property. See Also Execution Exe

### Executions.Item

#### Syntax

[Executions](executions.html).Item( itemIdx)

#### Data Type

[Execution](../tsapiref/execution.html)

#### Purpose

Returns a reference to an item at the specified index in the collection.

#### Parameters

itemIdx
 As
 [Long](data-types-for-teststand-user-interface.html)

[In] Specifies the zero-based index. Use a non-negative number less than the value of the
 [Executions.Count](executions-count.html)
 property.

#### See Also

[Execution](../tsapiref/execution.html)

[Executions.Count](executions-count.html)

Parent topic:

Properties

<!--NI_TOPIC bundle=teststand-api-reference path=tsuiref/executions-numincomplete.html language=enus -->
## TOPIC 04948: Executions.NumIncomplete

- bundle_id: `teststand-api-reference`
- source_path: `tsuiref/executions-numincomplete.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsuiref/executions-numincomplete.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax Executions.NumIncomplete Data Type Long Purpose Returns the number of incomplete executions in the collection, which is the sum of paused and running executions. See Also Executions.NumPaused Executions.NumRunning

### Executions.NumIncomplete

#### Syntax

[Executions](executions.html).NumIncomplete

#### Data Type

[Long](data-types-for-teststand-user-interface.html)

#### Purpose

Returns the number of incomplete executions in the collection, which is the sum of paused and running executions.

#### See Also

[Executions.NumPaused](executions-numpaused.html)

[Executions.NumRunning](executions-numrunning.html)

Parent topic:

Properties

<!--NI_TOPIC bundle=teststand-api-reference path=tsuiref/executions-numpaused.html language=enus -->
## TOPIC 04949: Executions.NumPaused

- bundle_id: `teststand-api-reference`
- source_path: `tsuiref/executions-numpaused.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsuiref/executions-numpaused.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax Executions.NumPaused Data Type Long Purpose Returns the number of paused executions in the collection. See Also Executions.NumIncomplete Executions.NumRunning

### Executions.NumPaused

#### Syntax

[Executions](executions.html).NumPaused

#### Data Type

[Long](data-types-for-teststand-user-interface.html)

#### Purpose

Returns the number of paused executions in the collection.

#### See Also

[Executions.NumIncomplete](executions-numincomplete.html)

[Executions.NumRunning](executions-numrunning.html)

Parent topic:

Properties

<!--NI_TOPIC bundle=teststand-api-reference path=tsuiref/executions-numrunning.html language=enus -->
## TOPIC 04950: Executions.NumRunning

- bundle_id: `teststand-api-reference`
- source_path: `tsuiref/executions-numrunning.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsuiref/executions-numrunning.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax Executions.NumRunning Data Type Long Purpose Returns the number of running executions. Paused executions are not considered to be running. See Also Executions.NumIncomplete Executions.NumPaused

### Executions.NumRunning

#### Syntax

[Executions](executions.html).NumRunning

#### Data Type

[Long](data-types-for-teststand-user-interface.html)

#### Purpose

Returns the number of running executions. Paused executions are not considered to be running.

#### See Also

[Executions.NumIncomplete](executions-numincomplete.html)

[Executions.NumPaused](executions-numpaused.html)

Parent topic:

Properties

<!--NI_TOPIC bundle=teststand-api-reference path=tsuiref/executions-resumeall.html language=enus -->
## TOPIC 04951: Executions.ResumeAll

- bundle_id: `teststand-api-reference`
- source_path: `tsuiref/executions-resumeall.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsuiref/executions-resumeall.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax Executions.ResumeAll Purpose Resumes all paused executions in the collection.

### Executions.ResumeAll

#### Syntax

[Executions](executions.html).ResumeAll

#### Purpose

Resumes all paused executions in the collection.

Parent topic:

Methods

<!--NI_TOPIC bundle=teststand-api-reference path=tsuiref/executions.html language=enus -->
## TOPIC 04952: Executions

- bundle_id: `teststand-api-reference`
- source_path: `tsuiref/executions.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsuiref/executions.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: A collection of Execution objects. The ApplicationMgr.Executions property returns an Executions object, which contains all the executions the application created. Properties Count (Read Only) Item (Read Only) NumIncomplete (Read Only) NumPaused (Read Only) NumRunning (Read Only) Method ResumeAll See

### Executions

A collection of Execution objects. The
 [ApplicationMgr.Executions](applicationmgr-executions.html)
 property returns an Executions object, which contains all the executions the application created.

#### Properties

| Count (Read Only) |
| --- |
| Item (Read Only) |
| NumIncomplete (Read Only) |
| NumPaused (Read Only) |
| NumRunning (Read Only) |

#### Method

| ResumeAll |
| --- |

#### See Also

[ApplicationMgr.Executions](applicationmgr-executions.html)

Parent topic:

TestStand User Interface Controls

<!--NI_TOPIC bundle=teststand-api-reference path=tsuiref/executionviewconnection-colorpaused.html language=enus -->
## TOPIC 04953: ExecutionViewConnection.ColorPaused

- bundle_id: `teststand-api-reference`
- source_path: `tsuiref/executionviewconnection-colorpaused.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsuiref/executionviewconnection-colorpaused.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax ExecutionViewConnection.ColorPaused Data Type Color Purpose Specifies the background color of the control when the execution in the ExecutionView Manager control is paused. This setting is ignored when the value of the ExecutionViewConnection.Options property is ExecutionViewConnection_Ignore

### ExecutionViewConnection.ColorPaused

#### Syntax

[ExecutionViewConnection](executionviewconnection.html).ColorPaused

#### Data Type

[Color](data-types-for-teststand-user-interface.html)

#### Purpose

Specifies the background color of the control when the execution in the ExecutionView Manager control is paused. This setting is ignored when the value of the
 [ExecutionViewConnection.Options](executionviewconnection-options.html)
 property is
 ExecutionViewConnection_IgnoreColors
 .

#### See Also

[ExecutionViewConnection.Options](executionviewconnection-options.html)

Parent topic:

Properties

<!--NI_TOPIC bundle=teststand-api-reference path=tsuiref/executionviewconnection-colorrunning.html language=enus -->
## TOPIC 04954: ExecutionViewConnection.ColorRunning

- bundle_id: `teststand-api-reference`
- source_path: `tsuiref/executionviewconnection-colorrunning.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsuiref/executionviewconnection-colorrunning.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax ExecutionViewConnection.ColorRunning Data Type Color Purpose Specifies the background color of the control when the execution in the ExecutionView Manager control is running. This setting is ignored when the value of the ExecutionViewConnection.Options property is ExecutionViewConnection_Igno

### ExecutionViewConnection.ColorRunning

#### Syntax

[ExecutionViewConnection](executionviewconnection.html).ColorRunning

#### Data Type

[Color](data-types-for-teststand-user-interface.html)

#### Purpose

Specifies the background color of the control when the execution in the ExecutionView Manager control is running. This setting is ignored when the value of the
 [ExecutionViewConnection.Options](executionviewconnection-options.html)
 property is
 ExecutionViewConnection_IgnoreColors
 .

#### See Also

[ExecutionViewConnection.Options](executionviewconnection-options.html)

Parent topic:

Properties

<!--NI_TOPIC bundle=teststand-api-reference path=tsuiref/executionviewconnection-colorstopped.html language=enus -->
## TOPIC 04955: ExecutionViewConnection.ColorStopped

- bundle_id: `teststand-api-reference`
- source_path: `tsuiref/executionviewconnection-colorstopped.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsuiref/executionviewconnection-colorstopped.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax ExecutionViewConnection.ColorStopped Data Type Color Purpose Specifies the background color of the control when the execution in the ExecutionView Manager control is stopped. This setting is ignored when the value of the ExecutionViewConnection.Options property is ExecutionViewConnection_Igno

### ExecutionViewConnection.ColorStopped

#### Syntax

[ExecutionViewConnection](executionviewconnection.html).ColorStopped

#### Data Type

[Color](data-types-for-teststand-user-interface.html)

#### Purpose

Specifies the background color of the control when the execution in the ExecutionView Manager control is stopped. This setting is ignored when the value of the
 [ExecutionViewConnection.Options](executionviewconnection-options.html)
 property is
 ExecutionViewConnection_IgnoreColors
 .

#### See Also

[ExecutionViewConnection.Options](executionviewconnection-options.html)

Parent topic:

Properties

<!--NI_TOPIC bundle=teststand-api-reference path=tsuiref/executionviewconnection-options.html language=enus -->
## TOPIC 04956: ExecutionViewConnection.Options

- bundle_id: `teststand-api-reference`
- source_path: `tsuiref/executionviewconnection-options.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsuiref/executionviewconnection-options.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax ExecutionViewConnection.Options Data Type Long Purpose Specifies the behavior of the ExecutionViewConnection. The value of this property is a bitwise-OR combination of the ExecutionViewOptions constants. See Also ExecutionViewOptions

### ExecutionViewConnection.Options

#### Syntax

[ExecutionViewConnection](executionviewconnection.html).Options

#### Data Type

[Long](data-types-for-teststand-user-interface.html)

#### Purpose

Specifies the behavior of the ExecutionViewConnection. The value of this property is a bitwise-OR combination of the
 [ExecutionViewOptions](executionviewoptions.html)
 constants.

#### See Also

[ExecutionViewOptions](executionviewoptions.html)

Parent topic:

Properties

<!--NI_TOPIC bundle=teststand-api-reference path=tsuiref/executionviewconnection-uicontrol.html language=enus -->
## TOPIC 04957: ExecutionViewConnection.UIControl

- bundle_id: `teststand-api-reference`
- source_path: `tsuiref/executionviewconnection-uicontrol.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsuiref/executionviewconnection-uicontrol.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax ExecutionViewConnection.UIControl Data Type Object Purpose Returns the user interface control the connection connects to an ExecutionView Manager control. See Also ExecutionView Manager

### ExecutionViewConnection.UIControl

#### Syntax

[ExecutionViewConnection](executionviewconnection.html).UIControl

#### Data Type

[Object](data-types-for-teststand-user-interface.html)

#### Purpose

Returns the user interface control the connection connects to an
 [ExecutionView Manager](executionviewmgr.html)
 control.

#### See Also

[ExecutionView Manager](executionviewmgr.html)

Parent topic:

Properties

<!--NI_TOPIC bundle=teststand-api-reference path=tsuiref/executionviewconnection.html language=enus -->
## TOPIC 04958: ExecutionViewConnection

- bundle_id: `teststand-api-reference`
- source_path: `tsuiref/executionviewconnection.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsuiref/executionviewconnection.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Represents a connection from an ExecutionView Manager control to an ExecutionViewMgrConnections.ExecutionView property. When tracing is enabled, the connected control shows the steps of the execution as they are executing. Use the ExecutionViewMgr.Connections property to obtain a collection of Execu

### ExecutionViewConnection

Represents a connection from an
 [ExecutionView Manager](executionviewmgr.html)
 control to an
 [ExecutionViewMgrConnections.ExecutionView](executionviewmgrconnections-executionview.html)
 property. When tracing is enabled, the connected control shows the steps of the execution as they are executing. Use the
 [ExecutionViewMgr.Connections](executionviewmgr-connections.html)
 property to obtain a collection of ExecutionViewConnection objects.

#### Properties

| ColorPaused |
| --- |
| ColorRunning |
| ColorStopped |
| Options |
| UIControl (Read Only) |

#### See Also

[ExecutionViewMgrConnections.ExecutionView](executionviewmgrconnections-executionview.html)

[ExecutionView Manager](executionviewmgr.html)

[ExecutionViewConnections](executionviewconnections.html)

[ExecutionViewMgr.Connections](executionviewmgr-connections.html)

Parent topic:

TestStand User Interface Support Controls

<!--NI_TOPIC bundle=teststand-api-reference path=tsuiref/executionviewconnections-add.html language=enus -->
## TOPIC 04959: ExecutionViewConnections.Add

- bundle_id: `teststand-api-reference`
- source_path: `tsuiref/executionviewconnections-add.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsuiref/executionviewconnections-add.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax ExecutionViewConnections.Add( uiObj) Return Value ExecutionViewConnection New ExecutionViewConnection. Purpose Creates and adds a new ExecutionViewConnection to the collection. Parameters uiObj As Object [In] Specifies the user interface object to connect. See Also ExecutionViewConnections.Re

### ExecutionViewConnections.Add

#### Syntax

[ExecutionViewConnections](executionviewconnections.html).Add( uiObj)

#### Return Value

[ExecutionViewConnection](executionviewconnection.html)

New ExecutionViewConnection.

#### Purpose

Creates and adds a new ExecutionViewConnection to the collection.

#### Parameters

uiObj
 As
 [Object](data-types-for-teststand-user-interface.html)

[In] Specifies the user interface object to connect.

#### See Also

[ExecutionViewConnections.Remove](executionviewconnections-remove.html)

Parent topic:

Methods

<!--NI_TOPIC bundle=teststand-api-reference path=tsuiref/executionviewconnections-clear.html language=enus -->
## TOPIC 04960: ExecutionViewConnections.Clear

- bundle_id: `teststand-api-reference`
- source_path: `tsuiref/executionviewconnections-clear.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsuiref/executionviewconnections-clear.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax ExecutionViewConnections.Clear Purpose Removes all items from the collection. See Also ExecutionViewConnections.Remove

### ExecutionViewConnections.Clear

#### Syntax

[ExecutionViewConnections](executionviewconnections.html).Clear

#### Purpose

Removes all items from the collection.

#### See Also

[ExecutionViewConnections.Remove](executionviewconnections-remove.html)

Parent topic:

Methods

<!--NI_TOPIC bundle=teststand-api-reference path=tsuiref/executionviewconnections-count.html language=enus -->
## TOPIC 04961: ExecutionViewConnections.Count

- bundle_id: `teststand-api-reference`
- source_path: `tsuiref/executionviewconnections-count.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsuiref/executionviewconnections-count.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax ExecutionViewConnections.Count Data Type Long Purpose Returns the number of items in the collection.

### ExecutionViewConnections.Count

#### Syntax

[ExecutionViewConnections](executionviewconnections.html).Count

#### Data Type

[Long](data-types-for-teststand-user-interface.html)

#### Purpose

Returns the number of items in the collection.

Parent topic:

Properties

<!--NI_TOPIC bundle=teststand-api-reference path=tsuiref/executionviewconnections-fromcontrol.html language=enus -->
## TOPIC 04962: ExecutionViewConnections.FromControl

- bundle_id: `teststand-api-reference`
- source_path: `tsuiref/executionviewconnections-fromcontrol.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsuiref/executionviewconnections-fromcontrol.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax ExecutionViewConnections.FromControl( uiObj) Return Value ExecutionViewConnection ExecutionViewConnection connected to the uiObj parameter. When no ExecutionViewConnection exists for this control, this method returns NULL . Purpose Returns the ExecutionViewConnection that is connected to the

### ExecutionViewConnections.FromControl

#### Syntax

[ExecutionViewConnections](executionviewconnections.html).FromControl( uiObj)

#### Return Value

[ExecutionViewConnection](executionviewconnection.html)

ExecutionViewConnection connected to the
 uiObj
 parameter. When no ExecutionViewConnection exists for this control, this method returns
 NULL
 .

#### Purpose

Returns the ExecutionViewConnection that is connected to the
 uiObj
 parameter.

#### Parameters

uiObj
 As
 [Object](data-types-for-teststand-user-interface.html)

[In] Specifies the connected user interface object.

Parent topic:

Methods

<!--NI_TOPIC bundle=teststand-api-reference path=tsuiref/executionviewconnections-item.html language=enus -->
## TOPIC 04963: ExecutionViewConnections.Item

- bundle_id: `teststand-api-reference`
- source_path: `tsuiref/executionviewconnections-item.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsuiref/executionviewconnections-item.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax ExecutionViewConnections.Item( itemIndex) Data Type ExecutionViewConnection Item located at the specified index. Purpose Returns a reference to an item at the specified index in the collection. Parameters itemIndex As Long [In] Specifies the index of the item to retrieve. See Also ExecutionVi

### ExecutionViewConnections.Item

#### Syntax

[ExecutionViewConnections](executionviewconnections.html).Item( itemIndex)

#### Data Type

[ExecutionViewConnection](executionviewconnection.html)

Item located at the specified index.

#### Purpose

Returns a reference to an item at the specified index in the collection.

#### Parameters

itemIndex
 As
 [Long](data-types-for-teststand-user-interface.html)

[In] Specifies the index of the item to retrieve.

#### See Also

[ExecutionViewConnection](executionviewconnection.html)

[ExecutionViewConnections.Count](executionviewconnections-count.html)

Parent topic:

Properties

<!--NI_TOPIC bundle=teststand-api-reference path=tsuiref/executionviewconnections-remove.html language=enus -->
## TOPIC 04964: ExecutionViewConnections.Remove

- bundle_id: `teststand-api-reference`
- source_path: `tsuiref/executionviewconnections-remove.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsuiref/executionviewconnections-remove.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax ExecutionViewConnections.Remove( uiObj) Return Value Boolean Returns True when the ExecutionViewConnection is removed. Returns False when the ExecutionViewConnection is not found. Purpose Removes the specified item from this collection, if it exists. Parameters uiObj As Object [In] Specifies

### ExecutionViewConnections.Remove

#### Syntax

[ExecutionViewConnections](executionviewconnections.html).Remove( uiObj)

#### Return Value

[Boolean](data-types-for-teststand-user-interface.html)

Returns
 True
 when the ExecutionViewConnection is removed. Returns
 False
 when the ExecutionViewConnection is not found.

#### Purpose

Removes the specified item from this collection, if it exists.

#### Parameters

uiObj
 As
 [Object](data-types-for-teststand-user-interface.html)

[In] Specifies the user interface object to disconnect.

#### See Also

[ExecutionViewConnections.Add](executionviewconnections-add.html)

Parent topic:

Methods

<!--NI_TOPIC bundle=teststand-api-reference path=tsuiref/executionviewconnections.html language=enus -->
## TOPIC 04965: ExecutionViewConnections

- bundle_id: `teststand-api-reference`
- source_path: `tsuiref/executionviewconnections.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsuiref/executionviewconnections.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: A collection of ExecutionViewConnection objects you obtain by calling the ExecutionViewMgr.Connections property. Properties Count (Read Only) Item (Read Only) Methods Add Clear FromControl Remove See Also ExecutionViewConnection ExecutionViewMgr.Connections

### ExecutionViewConnections

A collection of
 [ExecutionViewConnection](executionviewconnection.html)
 objects you obtain by calling the
 [ExecutionViewMgr.Connections](executionviewmgr-connections.html)
 property.

#### Properties

| Count (Read Only) |
| --- |
| Item (Read Only) |

#### Methods

| Add |
| --- |
| Clear |
| FromControl |
| Remove |

#### See Also

[ExecutionViewConnection](executionviewconnection.html)

[ExecutionViewMgr.Connections](executionviewmgr-connections.html)

Parent topic:

TestStand User Interface Support Controls

<!--NI_TOPIC bundle=teststand-api-reference path=tsuiref/executionviewmgr-abortexecution.html language=enus -->
## TOPIC 04966: ExecutionViewMgr.AbortExecution

- bundle_id: `teststand-api-reference`
- source_path: `tsuiref/executionviewmgr-abortexecution.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsuiref/executionviewmgr-abortexecution.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax ExecutionViewMgr.AbortExecution Purpose Attempts to abort the current execution if it is running. Remarks The ExecutionView Manager control generates the ExecutionViewMgr.TerminationStateChanged event after calling this method and then generates the ExecutionViewMgr.EndExecution event when th

### ExecutionViewMgr.AbortExecution

#### Syntax

[ExecutionViewMgr](executionviewmgr.html).AbortExecution

#### Purpose

Attempts to abort the current execution if it is running.

#### Remarks

The ExecutionView Manager control generates the
 [ExecutionViewMgr.TerminationStateChanged](executionviewmgr-terminationstatechanged.html)
 event after calling this method and then generates the
 [ExecutionViewMgr.EndExecution](executionviewmgr-endexecution.html)
 event when the execution has ended.

#### See Also

[CommandKind_Abort](commandkinds.html)

[ExecutionViewMgr.EndExecution](executionviewmgr-endexecution.html)

[ExecutionViewMgr.RestartExecution](executionviewmgr-restartexecution.html)

[ExecutionViewMgr.RunState](executionviewmgr-runstate.html)

[ExecutionViewMgr.TerminationStateChanged](executionviewmgr-terminationstatechanged.html)

Parent topic:

Methods

<!--NI_TOPIC bundle=teststand-api-reference path=tsuiref/executionviewmgr-applicationmgr.html language=enus -->
## TOPIC 04967: ExecutionViewMgr.ApplicationMgr

- bundle_id: `teststand-api-reference`
- source_path: `tsuiref/executionviewmgr-applicationmgr.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsuiref/executionviewmgr-applicationmgr.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax ExecutionViewMgr.ApplicationMgr Data Type Object Purpose Returns a reference to the Application Manager control of the application. The value is NULL when no Application Manager control exists within the process. See Also ApplicationMgr

### ExecutionViewMgr.ApplicationMgr

#### Syntax

[ExecutionViewMgr](executionviewmgr.html).ApplicationMgr

#### Data Type

[Object](data-types-for-teststand-user-interface.html)

#### Purpose

Returns a reference to the Application Manager control of the application. The value is
 NULL
 when no Application Manager control exists within the process.

#### See Also

[ApplicationMgr](applicationmgr.html)

Parent topic:

Properties

<!--NI_TOPIC bundle=teststand-api-reference path=tsuiref/executionviewmgr-break.html language=enus -->
## TOPIC 04968: ExecutionViewMgr.Break

- bundle_id: `teststand-api-reference`
- source_path: `tsuiref/executionviewmgr-break.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsuiref/executionviewmgr-break.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax ControlName_Break( exec, thrd, ctxt) Applies To ExecutionViewMgr Purpose Occurs when the selected execution in the ExecutionView Manager control breaks as a result of a breakpoint or upon user request, such as when you call the ExecutionViewMgr.BreakExecution method. Remarks To obtain the mes

### ExecutionViewMgr.Break

#### Syntax

ControlName_Break( exec, thrd, ctxt)

#### Applies To

[ExecutionViewMgr](executionviewmgr.html)

#### Purpose

Occurs when the selected execution in the ExecutionView Manager control breaks as a result of a breakpoint or upon user request, such as when you call the
 [ExecutionViewMgr.BreakExecution](executionviewmgr-breakexecution.html)
 method.

#### Remarks

To obtain the message that signaled this event, use the
 [ApplicationMgr.CurrentUIMessage](applicationmgr-currentuimessage.html)
 property.

#### Parameters

exec
 As
 
 [Execution](../tsapiref/execution.html)

[In] Specifies the paused execution.

thrd
 As
 
 [Thread](../tsapiref/thread.html)

[In] Specifies the thread that generated the break notification.

ctxt
 As
 
 [SequenceContext](../tsapiref/sequencecontext.html)

[In] Specifies the current context of the execution.

#### See Also

[ApplicationMgr.CurrentUIMessage](applicationmgr-currentuimessage.html)

[ExecutionViewMgr.BreakExecution](executionviewmgr-breakexecution.html)

Parent topic:

Events

<!--NI_TOPIC bundle=teststand-api-reference path=tsuiref/executionviewmgr-breakexecution.html language=enus -->
## TOPIC 04969: ExecutionViewMgr.BreakExecution

- bundle_id: `teststand-api-reference`
- source_path: `tsuiref/executionviewmgr-breakexecution.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsuiref/executionviewmgr-breakexecution.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax ExecutionViewMgr.BreakExecution Purpose Attempts to pause the current execution if it is running. Remarks The ExecutionView Manager control generates an ExecutionViewMgr.Break event when the execution suspends. See Also CommandKind_Break ExecutionViewMgr.Break ExecutionViewMgr.ResumeExecution

### ExecutionViewMgr.BreakExecution

#### Syntax

[ExecutionViewMgr](executionviewmgr.html).BreakExecution

#### Purpose

Attempts to pause the current execution if it is running.

#### Remarks

The ExecutionView Manager control generates an
 [ExecutionViewMgr.Break](executionviewmgr-break.html)
 event when the execution suspends.

#### See Also

[CommandKind_Break](commandkinds.html)

[ExecutionViewMgr.Break](executionviewmgr-break.html)

[ExecutionViewMgr.ResumeExecution](executionviewmgr-resumeexecution.html)

[ExecutionViewMgr.RunState](executionviewmgr-runstate.html)

Parent topic:

Methods

<!--NI_TOPIC bundle=teststand-api-reference path=tsuiref/executionviewmgr-buildeditargs.html language=enus -->
## TOPIC 04970: ExecutionViewMgr.BuildEditArgs

- bundle_id: `teststand-api-reference`
- source_path: `tsuiref/executionviewmgr-buildeditargs.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsuiref/executionviewmgr-buildeditargs.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax ExecutionViewMgr.BuildEditArgs Return Value EditArgs A new EditArgs object. Purpose Creates an EditArgs object that reflects the selection state of the ExecutionView Manager control. Remarks Use this method to create an EditArgs object, which you can modify before you pass it as the optional

### ExecutionViewMgr.BuildEditArgs

#### Syntax

[ExecutionViewMgr](executionviewmgr.html).BuildEditArgs

#### Return Value

[EditArgs](../tsapiref/editargs.html)

A new
 
 [EditArgs](../tsapiref/editargs.html)
 object.

#### Purpose

Creates an EditArgs object that reflects the selection state of the ExecutionView Manager control.

#### Remarks

Use this method to create an EditArgs object, which you can modify before you pass it as the optional parameter to a method that starts an execution.

#### See Also

[EditArgs](../tsapiref/editargs.html)

[Omitting Optional Parameters](/csh?context=ts_tsapiref_optional_parameters)

Parent topic:

Methods

<!--NI_TOPIC bundle=teststand-api-reference path=tsuiref/executionviewmgr-buildinteractiveargs.html language=enus -->
## TOPIC 04971: ExecutionViewMgr.BuildInteractiveArgs

- bundle_id: `teststand-api-reference`
- source_path: `tsuiref/executionviewmgr-buildinteractiveargs.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsuiref/executionviewmgr-buildinteractiveargs.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax ExecutionViewMgr.BuildInteractiveArgs( createLoopArgs, [cancel]) Return Value InteractiveArgs The new InteractiveArgs object. Purpose Creates an InteractiveArgs object that reflects the selection state of the ExecutionView Manager control. Remarks Use this method to create an InteractiveArgs

### ExecutionViewMgr.BuildInteractiveArgs

#### Syntax

[ExecutionViewMgr](executionviewmgr.html).BuildInteractiveArgs( createLoopArgs, [cancel])

#### Return Value

[InteractiveArgs](../tsapiref/interactiveargs.html)

The new InteractiveArgs object.

#### Purpose

Creates an InteractiveArgs object that reflects the selection state of the ExecutionView Manager control.

#### Remarks

Use this method to create an InteractiveArgs object, which you can modify before you pass it as an optional parameter to a method that starts an interactive execution.

#### Parameters

createLoopArgs
 As
 [Variant](data-types-for-teststand-user-interface.html)

[In] When this parameter is
 True
 , this property launches the
 [Loop on Selected Steps](../tsref/loop-on-selected-steps-dialog-box.html)
 dialog box to create the InteractiveArgs for the
 [ExecutionViewMgr.LoopOnSelectedSteps](executionviewmgr-looponselectedsteps.html)
 method.

cancel
 As
 [Variant](data-types-for-teststand-user-interface.html)

[Out] [
 [Optional](/csh?context=ts_tsuiref_optional_parameters)
 ] If the Loop on Selected Steps dialog box is cancelled, the value of the parameter passed in is
 True
 .

#### See Also

[ExecutionViewMgr.LoopOnSelectedSteps](executionviewmgr-looponselectedsteps.html)

[ExecutionViewMgr.RunSelectedSteps](executionviewmgr-runselectedsteps.html)

[Loop on Selected Steps dialog box](../tsref/loop-on-selected-steps-dialog-box.html)

[Omitting Optional Parameters](/csh?context=ts_tsapiref_optional_parameters)

Parent topic:

Methods

<!--NI_TOPIC bundle=teststand-api-reference path=tsuiref/executionviewmgr-configurationentrypoints.html language=enus -->
## TOPIC 04972: ExecutionViewMgr.ConfigurationEntryPoints

- bundle_id: `teststand-api-reference`
- source_path: `tsuiref/executionviewmgr-configurationentrypoints.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsuiref/executionviewmgr-configurationentrypoints.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax ExecutionViewMgr.ConfigurationEntryPoints Data Type EntryPoints Purpose Returns a collection of Configuration entry points for the selected execution. Remarks This collection can change when the selected execution changes. See Also EntryPoint EntryPoints ExecutionViewMgr.ExecutionEntryPoints

### ExecutionViewMgr.ConfigurationEntryPoints

#### Syntax

[ExecutionViewMgr](executionviewmgr.html).ConfigurationEntryPoints

#### Data Type

[EntryPoints](entrypoints.html)

#### Purpose

Returns a collection of Configuration entry points for the selected execution.

#### Remarks

This collection can change when the selected execution changes.

#### See Also

[EntryPoint](entrypoint.html)

[EntryPoints](entrypoints.html)

[ExecutionViewMgr.ExecutionEntryPoints](executionviewmgr-executionentrypoints.html)

Parent topic:

Properties

<!--NI_TOPIC bundle=teststand-api-reference path=tsuiref/executionviewmgr-connectcallstack.html language=enus -->
## TOPIC 04973: ExecutionViewMgr.ConnectCallStack

- bundle_id: `teststand-api-reference`
- source_path: `tsuiref/executionviewmgr-connectcallstack.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsuiref/executionviewmgr-connectcallstack.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax ExecutionViewMgr.ConnectCallStack( uiObj) Return Value CallStackConnection A reference to an object that represents the new connection. Discarding the reference does not affect the connection. When the object is already connected to this type of connection, the existing connection is returned

### ExecutionViewMgr.ConnectCallStack

#### Syntax

[ExecutionViewMgr](executionviewmgr.html).ConnectCallStack( uiObj)

#### Return Value

[CallStackConnection](callstackconnection.html)

A reference to an object that represents the new connection. Discarding the reference does not affect the connection. When the object is already connected to this type of connection, the existing connection is returned.

#### Purpose

Connects a
 [ComboBox](combobox.html)
 ,
 [ListBarPage](listbarpage.html)
 , or
 [ListBox](listbox.html)
 control to display the call stack of the paused execution.

#### Remarks

To disconnect an existing connection, you must first obtain the
 [ExecutionViewMgrConnections](executionviewmgrconnections.html)
 object from the
 [ExecutionViewMgr.Connections](executionviewmgr-connections.html)
 property. Then, access the
 [ExecutionViewMgrConnections.CallStack](executionviewmgrconnections-callstack.html)
 property to obtain the
 [CallstackConnections](callstackconnections.html)
 collection.

#### Parameters

uiObj
 As
 [Object](data-types-for-teststand-user-interface.html)

[In] Specifies the control or element to which the call stack connection connects. Pass a
 [ComboBox](combobox.html)
 ,
 [ListBarPage](listbarpage.html)
 , or
 [ListBox](listbox.html)
 .

#### See Also

[CallstackConnections](callstackconnections.html)

[ComboBox](combobox.html)

[ExecutionViewMgr.Connections](executionviewmgr-connections.html)

[ExecutionViewMgrConnections](executionviewmgrconnections.html)

[ExecutionViewMgrConnections.CallStack](executionviewmgrconnections-callstack.html)

[ListBarPage](listbarpage.html)

[ListBox](listbox.html)

Parent topic:

Methods

<!--NI_TOPIC bundle=teststand-api-reference path=tsuiref/executionviewmgr-connectcaption.html language=enus -->
## TOPIC 04974: ExecutionViewMgr.ConnectCaption

- bundle_id: `teststand-api-reference`
- source_path: `tsuiref/executionviewmgr-connectcaption.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsuiref/executionviewmgr-connectcaption.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax ExecutionViewMgr.ConnectCaption( uiObj, captionSource, longName) Return Value CaptionConnection A reference to an object that represents the new connection. Discarding the reference does not affect the connection. When the object is already connected to this type of connection, the existing c

### ExecutionViewMgr.ConnectCaption

#### Syntax

[ExecutionViewMgr](executionviewmgr.html).ConnectCaption( uiObj, captionSource, longName)

#### Return Value

[CaptionConnection](captionconnection.html)

A reference to an object that represents the new connection. Discarding the reference does not affect the connection. When the object is already connected to this type of connection, the existing connection is returned.

#### Purpose

Connects a caption source in an ExecutionView Manager control to a visible control or an element of a visible control. The connection automatically updates the visible control with text that describes an aspect of the current application state.

#### Remarks

To disconnect an existing connection, you must first obtain the
 [ExecutionViewMgrConnections](executionviewmgrconnections.html)
 object from the
 [ExecutionViewMgr.Connections](executionviewmgr-connections.html)
 property. Then, access the
 [ExecutionViewMgrConnections.Caption](executionviewmgrconnections-caption.html)
 property to obtain the
 [CaptionConnections](captionconnections.html)
 collection.

#### Parameters

uiObj
 As
 [Object](data-types-for-teststand-user-interface.html)

[In] Specifies the visible control or element of a visible control to which the caption source connects. Pass a
 [Label](label.html)
 ,
 [ExpressionEdit](expressionedit.html)
 , or
 [StatusBarPane](statusbarpane.html)
 control.

captionSource
 As
 [CaptionSources](captionsources.html)

[In] Specifies the type of caption source to connect.

longName
 As
 [Boolean](data-types-for-teststand-user-interface.html)

For certain caption sources, this parameter specifies whether the connection displays a long or short version of the caption text. Refer to the
 [CaptionSources](captionsources.html)
 enumeration for more information about determining when this option affects a caption source and for more information about the difference between the long and short versions of the text.

#### See Also

[ApplicationMgr.ConnectCaption](applicationmgr-connectcaption.html)

[CaptionConnections](captionconnections.html)

[CaptionSources](captionsources.html)

[ExecutionViewMgr.Connections](executionviewmgr-connections.html)

[ExecutionViewMgr.GetCaptionText](executionviewmgr-getcaptiontext.html)

[ExecutionViewMgrConnections](executionviewmgrconnections.html)

[ExecutionViewMgrConnections.Caption](executionviewmgrconnections-caption.html)

[ExpressionEdit](expressionedit.html)

[Label](label.html)

[SequenceFileViewMgr.ConnectCaption](sequencefileviewmgr-connectcaption.html)

[StatusBarPane](statusbarpane.html)

Parent topic:

Methods

<!--NI_TOPIC bundle=teststand-api-reference path=tsuiref/executionviewmgr-connectcommand.html language=enus -->
## TOPIC 04975: ExecutionViewMgr.ConnectCommand

- bundle_id: `teststand-api-reference`
- source_path: `tsuiref/executionviewmgr-connectcommand.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsuiref/executionviewmgr-connectcommand.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax ExecutionViewMgr.ConnectCommand( uiObj, cmdKind, index = 0, opts = 0) Return Value CommandConnection A reference to an object that represents the new connection. Discarding the reference does not affect the connection. When the object is already connected to this type of connection, the exist

### ExecutionViewMgr.ConnectCommand

#### Syntax

[ExecutionViewMgr](executionviewmgr.html).ConnectCommand( uiObj, cmdKind, index = 0, opts = 0)

#### Return Value

[CommandConnection](commandconnection.html)

A reference to an object that represents the new connection. Discarding the reference does not affect the connection. When the object is already connected to this type of connection, the existing connection is returned.

#### Purpose

Connects a command source in an ExecutionView Manager control to a TestStand button or checkbox control. The connection automatically updates the enabled, visible, and caption properties of the button or checkbox based on the state of the current execution. Clicking the button or enabling the checkbox executes the command.

#### Remarks

To disconnect an existing connection, you must first obtain the
 [ExecutionViewMgrConnections](executionviewmgrconnections.html)
 object from the
 [ExecutionViewMgr.Connections](executionviewmgr-connections.html)
 property. Then, access the
 [ExecutionViewMgrConnections.Command](executionviewmgrconnections-command.html)
 property to obtain the
 [CommandConnections](commandconnections.html)
 collection.

#### Parameters

uiObj
 As
 [Object](data-types-for-teststand-user-interface.html)

[In] Specifies the button or checkbox control to which the command connects.

cmdKind
 As
 [CommandKinds](commandkinds.html)

[In] Specifies the type of command to connect.

index
 As
 [Long](data-types-for-teststand-user-interface.html)

[In] For
 [CommandKinds](commandkinds.html)
 that are sets, this parameter indexes the set to obtain a particular command.

This parameter has a default value of
 0
 .

opts
 As
 [Long](data-types-for-teststand-user-interface.html)

[In] Specifies the options for the CommandConnection. Refer to the
 [CommandConnectionOptions](commandconnectionoptions.html)
 constants for more information about the options for the CommandConnection object.

This parameter has a default value of
 0
 .

#### See Also

[Button](button.html)

[CommandConnectionOptions](commandconnectionoptions.html)

[CommandConnections](commandconnections.html)

[CommandKinds](commandkinds.html)

[ExecutionViewMgr.Connections](executionviewmgr-connections.html)

[ExecutionViewMgr.GetCommand](executionviewmgr-getcommand.html)

[ExecutionViewMgrConnections](executionviewmgrconnections.html)

[ExecutionViewMgrConnections.Command](executionviewmgrconnections-command.html)

Parent topic:

Methods

<!--NI_TOPIC bundle=teststand-api-reference path=tsuiref/executionviewmgr-connectexecutionlist.html language=enus -->
## TOPIC 04976: ExecutionViewMgr.ConnectExecutionList

- bundle_id: `teststand-api-reference`
- source_path: `tsuiref/executionviewmgr-connectexecutionlist.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsuiref/executionviewmgr-connectexecutionlist.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax ExecutionViewMgr.ConnectExecutionList( uiObj) Return Value ExecutionListConnection A reference to an object that represents the new connection. Discarding the reference does not affect the connection. When the object is already connected to this type of connection, the existing connection is

### ExecutionViewMgr.ConnectExecutionList

#### Syntax

[ExecutionViewMgr](executionviewmgr.html).ConnectExecutionList( uiObj)

#### Return Value

[ExecutionListConnection](executionlistconnection.html)

A reference to an object that represents the new connection. Discarding the reference does not affect the connection. When the object is already connected to this type of connection, the existing connection is returned.

#### Purpose

Connects a
 [ComboBox](combobox.html)
 ,
 [ListBarPage](listbarpage.html)
 , or
 [ListBox](listbox.html)
 control to the list of running executions. The connected item displays the executions and allows the user to select an execution in the ExecutionView Manager control.

#### Remarks

To disconnect an existing connection, you must first obtain the
 [ExecutionViewMgrConnections](executionviewmgrconnections.html)
 object from the
 [ExecutionViewMgr.Connections](executionviewmgr-connections.html)
 property. Then, access the
 [ExecutionViewMgrConnections.ExecutionList](executionviewmgrconnections-executionlist.html)
 property to obtain the
 [ExecutionListConnections](executionlistconnections.html)
 collection.

#### Parameters

uiObj
 As
 [Object](data-types-for-teststand-user-interface.html)

[In] Use a
 [ComboBox](combobox.html)
 ,
 [ListBarPage](listbarpage.html)
 , or
 [ListBox](listbox.html)
 to display the list of executions.

#### See Also

[ComboBox](combobox.html)

[Execution](executionviewmgr-execution.html)

[ExecutionListConnections](executionlistconnections.html)

[ExecutionViewMgr.Connections](executionviewmgr-connections.html)

[ExecutionViewMgrConnections](executionviewmgrconnections.html)

[ExecutionViewMgrConnections.ExecutionList](executionviewmgrconnections-executionlist.html)

[ListBarPage](listbarpage.html)

[ListBox](listbox.html)

Parent topic:

Methods

<!--NI_TOPIC bundle=teststand-api-reference path=tsuiref/executionviewmgr-connectexecutionview.html language=enus -->
## TOPIC 04977: ExecutionViewMgr.ConnectExecutionView

- bundle_id: `teststand-api-reference`
- source_path: `tsuiref/executionviewmgr-connectexecutionview.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsuiref/executionviewmgr-connectexecutionview.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax ExecutionViewMgr.ConnectExecutionView( uiObj, opts = 0) Return Value ExecutionViewConnection A reference to an object that represents the new connection. Discarding the reference does not affect the connection. When the object is already connected to this type of connection, the existing conn

### ExecutionViewMgr.ConnectExecutionView

#### Syntax

[ExecutionViewMgr](executionviewmgr.html).ConnectExecutionView( uiObj, opts = 0)

#### Return Value

[ExecutionViewConnection](executionviewconnection.html)

A reference to an object that represents the new connection. Discarding the reference does not affect the connection. When the object is already connected to this type of connection, the existing connection is returned.

#### Purpose

Connects a SequenceView control to display the steps of the running sequence in the execution.

#### Remarks

To disconnect an existing connection, you must first obtain the
 [ExecutionViewMgrConnections](executionviewmgrconnections.html)
 object from the
 [ExecutionViewMgr.Connections](executionviewmgr-connections.html)
 property. Then, access the
 [ExecutionViewMgrConnections.ExecutionView](executionviewmgrconnections-executionview.html)
 property to obtain the
 [ExecutionViewConnections](executionviewconnections.html)
 collection.

#### Parameters

uiObj
 As
 [Object](data-types-for-teststand-user-interface.html)

[In] Specifies the SequenceView control to connect to the ExecutionViewConnection.

opts
 As
 [Long](data-types-for-teststand-user-interface.html)

[In] Specifies the options for the ExecutionViewConnection. Refer to the
 [ExecutionViewOptions](executionviewoptions.html)
 constants for more information about the options for the ExecutionViewConnection.

This parameter has a default value of
 0
 .

#### See Also

[ExecutionViewConnections](executionviewconnections.html)

[ExecutionViewOptions](executionviewoptions.html)

[ExecutionViewMgr.Connections](executionviewmgr-connections.html)

[ExecutionViewMgrConnections](executionviewmgrconnections.html)

[ExecutionViewMgrConnections.ExecutionView](executionviewmgrconnections-executionview.html)

[SequenceView](sequenceview.html)

Parent topic:

Methods

<!--NI_TOPIC bundle=teststand-api-reference path=tsuiref/executionviewmgr-connectimage.html language=enus -->
## TOPIC 04978: ExecutionViewMgr.ConnectImage

- bundle_id: `teststand-api-reference`
- source_path: `tsuiref/executionviewmgr-connectimage.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsuiref/executionviewmgr-connectimage.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax ExecutionViewMgr.ConnectImage( uiObj, imageSource) Return Value ImageConnection A reference to an object that represents the new connection. Discarding the reference does not affect the connection. When the object is already connected to this type of connection, the existing connection is ret

### ExecutionViewMgr.ConnectImage

#### Syntax

[ExecutionViewMgr](executionviewmgr.html).ConnectImage( uiObj, imageSource)

#### Return Value

[ImageConnection](imageconnection.html)

A reference to an object that represents the new connection. Discarding the reference does not affect the connection. When the object is already connected to this type of connection, the existing connection is returned.

#### Purpose

Connects an image source in an ExecutionView Manager control to a visible control or an element of a visible control. The connection automatically updates the visible control with an icon that describes an aspect of the current application state.

#### Remarks

To disconnect an existing connection, you must first obtain the
 [ExecutionViewMgrConnections](executionviewmgrconnections.html)
 object from the
 [ExecutionViewMgr.Connections](executionviewmgr-connections.html)
 property. Then, access the
 [ExecutionViewMgrConnections.Image](executionviewmgrconnections-image.html)
 property to obtain the
 [ImageConnections](imageconnections.html)
 collection.

#### Parameters

uiObj
 As
 [Object](data-types-for-teststand-user-interface.html)

[In] Specifies a visible control or element of a visible control to which the caption source connects. Pass a
 [StatusBarPane](statusbarpane.html)
 or
 [Button](button.html)
 .

imageSource
 As
 [ImageSources](imagesources.html)

[In] Specifies the type of image source to connect.

#### See Also

[Button](button.html)

[ExecutionViewMgr.Connections](executionviewmgr-connections.html)

[ExecutionViewMgr.GetImageName](executionviewmgr-getimagename.html)

[ExecutionViewMgrConnections](executionviewmgrconnections.html)

[ExecutionViewMgrConnections.Image](executionviewmgrconnections-image.html)

[ImageConnections](imageconnections.html)

[SequenceFileViewMgr.ConnectImage](sequencefileviewmgr-connectimage.html)

[StatusBarPane](statusbarpane.html)

Parent topic:

Methods

<!--NI_TOPIC bundle=teststand-api-reference path=tsuiref/executionviewmgr-connections.html language=enus -->
## TOPIC 04979: ExecutionViewMgr.Connections

- bundle_id: `teststand-api-reference`
- source_path: `tsuiref/executionviewmgr-connections.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsuiref/executionviewmgr-connections.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax ExecutionViewMgr.Connections Data Type ExecutionViewMgrConnections Purpose Accesses the connections of the ExecutionView Manager control. See Also ExecutionViewMgrConnections

### ExecutionViewMgr.Connections

#### Syntax

[ExecutionViewMgr](executionviewmgr.html).Connections

#### Data Type

[ExecutionViewMgrConnections](executionviewmgrconnections.html)

#### Purpose

Accesses the connections of the ExecutionView Manager control.

#### See Also

[ExecutionViewMgrConnections](executionviewmgrconnections.html)

Parent topic:

Properties

<!--NI_TOPIC bundle=teststand-api-reference path=tsuiref/executionviewmgr-connectnumeric.html language=enus -->
## TOPIC 04980: ExecutionViewMgr.ConnectNumeric

- bundle_id: `teststand-api-reference`
- source_path: `tsuiref/executionviewmgr-connectnumeric.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsuiref/executionviewmgr-connectnumeric.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax ExecutionViewMgr.ConnectNumeric( uiObj, numericSource) Return Value NumericConnection A reference to an object that represents the new connection. Discarding the reference does not affect the connection. When the object is already connected to this type of connection, the existing connection

### ExecutionViewMgr.ConnectNumeric

#### Syntax

[ExecutionViewMgr](executionviewmgr.html).ConnectNumeric( uiObj, numericSource)

#### Return Value

[NumericConnection](numericconnection.html)

A reference to an object that represents the new connection. Discarding the reference does not affect the connection. When the object is already connected to this type of connection, the existing connection is returned.

#### Purpose

Connects a numeric source in an ExecutionView Manager control to an element of a visible control. The connection automatically updates the visible control with the numeric information that describes an aspect of the current application state.

#### Remarks

Use this method to display an execution progress bar in a StatusBar pane.

To disconnect an existing connection, you must first obtain the
 [ExecutionViewMgrConnections](executionviewmgrconnections.html)
 object from the
 [ExecutionViewMgr.Connections](executionviewmgr-connections.html)
 property. Then, access the
 [ExecutionViewMgrConnections.Numeric](executionviewmgrconnections-numeric.html)
 property to obtain the
 [NumericConnections](numericconnections.html)
 collection.

#### Parameters

uiObj
 As
 [Object](data-types-for-teststand-user-interface.html)

[In] Specifies the element of a visible control to which the caption source connects. Pass a
 [StatusBarPane](statusbarpane.html)
 .

numericSource
 As
 [NumericSources](numericsources.html)

[In] Specifies the type of numeric source from which to obtain a numeric value.

#### See Also

[ExecutionViewMgr.Connections](executionviewmgr-connections.html)

[ExecutionViewMgr.GetNumericValue](executionviewmgr-getnumericvalue.html)

[ExecutionViewMgrConnections](executionviewmgrconnections.html)

[ExecutionViewMgrConnections.Numeric](executionviewmgrconnections-numeric.html)

[NumericConnections](numericconnections.html)

[StatusBarPane](statusbarpane.html)

Parent topic:

Methods

<!--NI_TOPIC bundle=teststand-api-reference path=tsuiref/executionviewmgr-connectreportview.html language=enus -->
## TOPIC 04981: ExecutionViewMgr.ConnectReportView

- bundle_id: `teststand-api-reference`
- source_path: `tsuiref/executionviewmgr-connectreportview.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsuiref/executionviewmgr-connectreportview.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax ExecutionViewMgr.ConnectReportView( uiObj) Return Value ReportViewConnection A reference to an object that represents the new connection. Discarding the reference does not affect the connection. When the object is already connected to this type of connection, the existing connection is return

### ExecutionViewMgr.ConnectReportView

#### Syntax

[ExecutionViewMgr](executionviewmgr.html).ConnectReportView( uiObj)

#### Return Value

[ReportViewConnection](reportviewconnection.html)

A reference to an object that represents the new connection. Discarding the reference does not affect the connection. When the object is already connected to this type of connection, the existing connection is returned.

#### Purpose

Connects a ReportView control to display the report of the selected execution in the ExecutionView Manager control.

#### Remarks

To disconnect an existing connection, you must first obtain the
 [ExecutionViewMgrConnections](executionviewmgrconnections.html)
 object from the
 [ExecutionViewMgr.Connections](executionviewmgr-connections.html)
 property. Then, access the
 [ExecutionViewMgrConnections.ReportView](executionviewmgrconnections-reportview.html)
 property to obtain the
 [ReportViewConnections](reportviewconnections.html)
 collection.

#### Parameters

uiObj
 As
 [Object](data-types-for-teststand-user-interface.html)

[In] Specifies the ReportView control to connect to the ExecutionView Manager control.

#### See Also

[ExecutionViewMgr.Connections](executionviewmgr-connections.html)

[ExecutionViewMgrConnections](executionviewmgrconnections.html)

[ExecutionViewMgrConnections.ReportView](executionviewmgrconnections-reportview.html)

[ReportView](reportview.html)

[ReportViewConnections](reportviewconnections.html)

Parent topic:

Methods

<!--NI_TOPIC bundle=teststand-api-reference path=tsuiref/executionviewmgr-connectthreadlist.html language=enus -->
## TOPIC 04982: ExecutionViewMgr.ConnectThreadList

- bundle_id: `teststand-api-reference`
- source_path: `tsuiref/executionviewmgr-connectthreadlist.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsuiref/executionviewmgr-connectthreadlist.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax ExecutionViewMgr.ConnectThreadList( uiObj) Return Value ThreadListConnection A reference to an object that represents the new connection. Discarding the reference does not affect the connection. When the object is already connected to this type of connection, the existing connection is return

### ExecutionViewMgr.ConnectThreadList

#### Syntax

[ExecutionViewMgr](executionviewmgr.html).ConnectThreadList( uiObj)

#### Return Value

[ThreadListConnection](threadlistconnection.html)

A reference to an object that represents the new connection. Discarding the reference does not affect the connection. When the object is already connected to this type of connection, the existing connection is returned.

#### Purpose

Connects the list of threads in the current execution to a control. The connected control displays the threads when the execution is paused and allows the user to specify a thread as the foreground thread.

#### Remarks

You can connect a
 [ComboBox](combobox.html)
 ,
 [ListBarPage](listbarpage.html)
 , or
 [ListBox](listbox.html)
 to this connection.

To disconnect an existing connection, you must first obtain the
 [ExecutionViewMgrConnections](executionviewmgrconnections.html)
 object from the
 [ExecutionViewMgr.Connections](executionviewmgr-connections.html)
 property. Then, access the
 [ExecutionViewMgrConnections.ThreadList](executionviewmgrconnections-threadlist.html)
 property to obtain the
 [ThreadListConnections](threadlistconnections.html)
 collection.

#### Parameters

uiObj
 As
 [Object](data-types-for-teststand-user-interface.html)

[In] Specifies a control or control element to connect to the ThreadListConnection.

#### See Also

[ComboBox](combobox.html)

[Execution.GetThread](../tsapiref/execution-getthread.html)

[ExecutionViewMgr.Connections](executionviewmgr-connections.html)

[ExecutionViewMgrConnections](executionviewmgrconnections.html)

[ExecutionViewMgrConnections.ThreadList](executionviewmgrconnections-threadlist.html)

[ListBarPage](listbarpage.html)

[ListBox](listbox.html)

[ThreadListConnections](threadlistconnections.html)

Parent topic:

Methods

<!--NI_TOPIC bundle=teststand-api-reference path=tsuiref/executionviewmgr-connectvariables.html language=enus -->
## TOPIC 04983: ExecutionViewMgr.ConnectVariables

- bundle_id: `teststand-api-reference`
- source_path: `tsuiref/executionviewmgr-connectvariables.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsuiref/executionviewmgr-connectvariables.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax ExecutionViewMgr.ConnectVariables( uiObj) Return Value VariablesConnection A reference to an object that represents the new connection. Discarding the reference does not affect the connection. When the object is already connected to this type of connection, the existing connection is returned

### ExecutionViewMgr.ConnectVariables

#### Syntax

[ExecutionViewMgr](executionviewmgr.html).ConnectVariables( uiObj)

#### Return Value

[VariablesConnection](variablesconnection.html)

A reference to an object that represents the new connection. Discarding the reference does not affect the connection. When the object is already connected to this type of connection, the existing connection is returned.

#### Purpose

Connects a
 [VariablesView](variablesview.html)
 control to display the current sequence context of the ExecutionView Manager control.

#### Remarks

To disconnect an existing connection, you must first obtain the
 [ExecutionViewMgrConnections](executionviewmgrconnections.html)
 object from the
 [ExecutionViewMgr.Connections](executionviewmgr-connections.html)
 property. Then, access the
 [ExecutionViewMgrConnections.Variables](executionviewmgrconnections-variables.html)
 property to obtain the
 [VariablesConnections](variablesconnections.html)
 collection.

#### Parameters

uiObj
 As
 [Object](data-types-for-teststand-user-interface.html)

[In] Specifies the reference to a VariablesView control that displays the current sequence context.

#### See Also

[ExecutionViewMgr.Connections](executionviewmgr-connections.html)

[ExecutionViewMgrConnections](executionviewmgrconnections.html)

[ExecutionViewMgrConnections.Variables](executionviewmgrconnections-variables.html)

[VariablesConnections](variablesconnections.html)

[VariablesView](variablesview.html)

Parent topic:

Methods

<!--NI_TOPIC bundle=teststand-api-reference path=tsuiref/executionviewmgr-contextchanged.html language=enus -->
## TOPIC 04984: ExecutionViewMgr.ContextChanged

- bundle_id: `teststand-api-reference`
- source_path: `tsuiref/executionviewmgr-contextchanged.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsuiref/executionviewmgr-contextchanged.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax ControlName_ContextChanged( ctxt) Applies To ExecutionViewMgr Purpose Occurs when the ExecutionViewMgr.SequenceContext property changes programmatically or when a control connected to a CallStackConnection changes the property. Parameters ctxt As SequenceContext [In] Specifies the current seq

### ExecutionViewMgr.ContextChanged

#### Syntax

ControlName_ContextChanged( ctxt)

#### Applies To

[ExecutionViewMgr](executionviewmgr.html)

#### Purpose

Occurs when the
 [ExecutionViewMgr.SequenceContext](executionviewmgr-sequencecontext.html)
 property changes programmatically or when a control connected to a
 [CallStackConnection](callstackconnection.html)
 changes the property.

#### Parameters

ctxt
 As
 
 [SequenceContext](../tsapiref/sequencecontext.html)

[In] Specifies the current sequence context of the ExecutionView Manager control.

#### See Also

[CallStackConnection](callstackconnection.html)

[ExecutionViewMgr.SequenceContext](executionviewmgr-sequencecontext.html)

Parent topic:

Events

<!--NI_TOPIC bundle=teststand-api-reference path=tsuiref/executionviewmgr-displayreport.html language=enus -->
## TOPIC 04985: ExecutionViewMgr.DisplayReport

- bundle_id: `teststand-api-reference`
- source_path: `tsuiref/executionviewmgr-displayreport.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsuiref/executionviewmgr-displayreport.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax ControlName_DisplayReport( exec) Applies To ExecutionViewMgr Purpose Occurs when an execution has ended and has a report to display. This event is also called in response to UIMsg_DisplayReport . Remarks Use this event to show the report for the execution. Parameters exec As Execution [In] Sp

### ExecutionViewMgr.DisplayReport

#### Syntax

ControlName_DisplayReport( exec)

#### Applies To

[ExecutionViewMgr](executionviewmgr.html)

#### Purpose

Occurs when an execution has ended and has a report to display. This event is also called in response to
 UIMsg_DisplayReport
 .

#### Remarks

Use this event to show the report for the execution.

#### Parameters

exec
 As
 
 [Execution](../tsapiref/execution.html)

[In] Specifies the execution that has the report to display.

#### See Also

[UIMessageCodes](../tsapiref/uimessagecodes.html)

Parent topic:

Events

<!--NI_TOPIC bundle=teststand-api-reference path=tsuiref/executionviewmgr-endexecution.html language=enus -->
## TOPIC 04986: ExecutionViewMgr.EndExecution

- bundle_id: `teststand-api-reference`
- source_path: `tsuiref/executionviewmgr-endexecution.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsuiref/executionviewmgr-endexecution.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax ControlName_EndExecution( exec) Applies To ExecutionViewMgr Purpose Occurs when the selected execution ends. Parameters exec As Execution [In] Specifies the execution that has ended. See Also ExecutionViewMgr.AbortExecution ExecutionViewMgr.RunState ExecutionViewMgr.TerminateExecution

### ExecutionViewMgr.EndExecution

#### Syntax

ControlName_EndExecution( exec)

#### Applies To

[ExecutionViewMgr](executionviewmgr.html)

#### Purpose

Occurs when the selected execution ends.

#### Parameters

exec
 As
 
 [Execution](../tsapiref/execution.html)

[In] Specifies the execution that has ended.

#### See Also

[ExecutionViewMgr.AbortExecution](executionviewmgr-abortexecution.html)

[ExecutionViewMgr.RunState](executionviewmgr-runstate.html)

[ExecutionViewMgr.TerminateExecution](executionviewmgr-terminateexecution.html)

Parent topic:

Events

<!--NI_TOPIC bundle=teststand-api-reference path=tsuiref/executionviewmgr-execution.html language=enus -->
## TOPIC 04987: ExecutionViewMgr.Execution

- bundle_id: `teststand-api-reference`
- source_path: `tsuiref/executionviewmgr-execution.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsuiref/executionviewmgr-execution.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax ExecutionViewMgr.Execution Data Type Execution Purpose Specifies the execution selected in the ExecutionView Manager control. Remarks An execution cannot be selected in more than one ExecutionView Manager control at a time. The ExecutionView Manager control generates an ExecutionViewMgr.Execu

### ExecutionViewMgr.Execution

#### Syntax

[ExecutionViewMgr](executionviewmgr.html).Execution

#### Data Type

[Execution](../tsapiref/execution.html)

#### Purpose

Specifies the execution selected in the ExecutionView Manager control.

#### Remarks

An execution cannot be selected in more than one ExecutionView Manager control at a time. The ExecutionView Manager control generates an
 [ExecutionViewMgr.ExecutionChanged](executionviewmgr-executionchanged.html)
 event when this property changes.

#### See Also

[Execution](../tsapiref/execution.html)

[ExecutionViewMgr.ExecutionChanged](executionviewmgr-executionchanged.html)

[ExecutionViewMgr.ReplaceExecutionOnClose](executionviewmgr-replaceexecutiononclose.html)

Parent topic:

Properties

<!--NI_TOPIC bundle=teststand-api-reference path=tsuiref/executionviewmgr-executionchanged.html language=enus -->
## TOPIC 04988: ExecutionViewMgr.ExecutionChanged

- bundle_id: `teststand-api-reference`
- source_path: `tsuiref/executionviewmgr-executionchanged.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsuiref/executionviewmgr-executionchanged.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax ControlName_ExecutionChanged( exec) Applies To ExecutionViewMgr Purpose Occurs when the ExecutionViewMgr.Execution property changes. Parameters exec As Execution [In] Specifies a new execution. See Also ExecutionViewMgr.ConnectExecutionList ExecutionViewMgr.Execution ExecutionViewMgr.ReplaceE

### ExecutionViewMgr.ExecutionChanged

#### Syntax

ControlName_ExecutionChanged( exec)

#### Applies To

[ExecutionViewMgr](executionviewmgr.html)

#### Purpose

Occurs when the
 [ExecutionViewMgr.Execution](executionviewmgr-execution.html)
 property changes.

#### Parameters

exec
 As
 
 [Execution](../tsapiref/execution.html)

[In] Specifies a new execution.

#### See Also

[ExecutionViewMgr.ConnectExecutionList](executionviewmgr-connectexecutionlist.html)

[ExecutionViewMgr.Execution](executionviewmgr-execution.html)

[ExecutionViewMgr.ReplaceExecutionOnClose](executionviewmgr-replaceexecutiononclose.html)

[ExecutionViewMgr.RunStateChanged](executionviewmgr-runstatechanged.html)

Parent topic:

Events

<!--NI_TOPIC bundle=teststand-api-reference path=tsuiref/executionviewmgr-executionentrypoints.html language=enus -->
## TOPIC 04989: ExecutionViewMgr.ExecutionEntryPoints

- bundle_id: `teststand-api-reference`
- source_path: `tsuiref/executionviewmgr-executionentrypoints.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsuiref/executionviewmgr-executionentrypoints.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax ExecutionViewMgr.ExecutionEntryPoints Data Type EntryPoints Purpose Returns the set of Execution entry points that the model sequence file for the selected execution defines. The collection includes only entry points that set the Sequence.ShowEntryPointForExeWindow property. Remarks This coll

### ExecutionViewMgr.ExecutionEntryPoints

#### Syntax

[ExecutionViewMgr](executionviewmgr.html).ExecutionEntryPoints

#### Data Type

[EntryPoints](entrypoints.html)

#### Purpose

Returns the set of Execution entry points that the model sequence file for the selected execution defines. The collection includes only entry points that set the
 
 [Sequence.ShowEntryPointForExeWindow](../tsapiref/sequence-showentrypointforexewindow.html)
 property.

#### Remarks

This collection can change when the selected execution changes.

#### See Also

[ApplicationMgr.ExecutionEntryPoints](applicationmgr-executionentrypoints.html)

[EntryPoints](entrypoints.html)

[ExecutionViewMgr.ConfigurationEntryPoints](executionviewmgr-configurationentrypoints.html)

[Sequence.ShowEntryPointForExeWindow](../tsapiref/sequence-showentrypointforexewindow.html)

[SequenceFileViewMgr.ExecutionEntryPoints](sequencefileviewmgr-executionentrypoints.html)

Parent topic:

Properties

<!--NI_TOPIC bundle=teststand-api-reference path=tsuiref/executionviewmgr-getcaptiontext.html language=enus -->
## TOPIC 04990: ExecutionViewMgr.GetCaptionText

- bundle_id: `teststand-api-reference`
- source_path: `tsuiref/executionviewmgr-getcaptiontext.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsuiref/executionviewmgr-getcaptiontext.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax ExecutionViewMgr.GetCaptionText( captionSource, longName, formatExpression = "") Return Value String The current text for the caption source you specify. Purpose Returns the current caption text for a caption source in an ExecutionView Manager control. Parameters captionSource As CaptionSourc

### ExecutionViewMgr.GetCaptionText

#### Syntax

[ExecutionViewMgr](executionviewmgr.html).GetCaptionText( captionSource, longName, formatExpression = "")

#### Return Value

[String](data-types-for-teststand-user-interface.html)

The current text for the caption source you specify.

#### Purpose

Returns the current caption text for a caption source in an ExecutionView Manager control.

#### Parameters

captionSource
 As
 [CaptionSources](captionsources.html)

[In] Specifies the type of caption source from which to obtain text.

longName
 As
 [Boolean](data-types-for-teststand-user-interface.html)

For certain caption sources, this parameter specifies to return a long or short version of the caption text. Refer to the
 [CaptionSources](captionsources.html)
 enumeration for more information about determining when this option affects the text and for more information about the difference between the long and short versions of the text.

formatExpression
 As
 [String](data-types-for-teststand-user-interface.html)

[In] Specifies a format expression to evaluate when generating the caption text. For the
 [CaptionSource_MacroExpression](captionsources.html)
 caption source, specify a format expression that evaluates to a string value that contains macros that specify other caption sources. For all other caption sources, specify an expression that evaluates to a string value that contains the characters
 %1
 . The method replaces the
 %1
 characters with the text from the caption source. Pass an empty string to use the default format string for the caption source.

This parameter has a default value of
 ""
 .

#### See Also

[ApplicationMgr.GetCaptionText](applicationmgr-getcaptiontext.html)

[CaptionSources](captionsources.html)

[SequenceFileViewMgr.GetCaptionText](sequencefileviewmgr-getcaptiontext.html)

Parent topic:

Methods

<!--NI_TOPIC bundle=teststand-api-reference path=tsuiref/executionviewmgr-getcommand.html language=enus -->
## TOPIC 04991: ExecutionViewMgr.GetCommand

- bundle_id: `teststand-api-reference`
- source_path: `tsuiref/executionviewmgr-getcommand.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsuiref/executionviewmgr-getcommand.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax ExecutionViewMgr.GetCommand( cmdKind, commandIndex = 0) Return Value Command Purpose Creates a Command object. When applicable, the command operates on the items the ExecutionView Manager control selects. Parameters cmdKind As CommandKinds [In] Specifies the type of Command object to create.

### ExecutionViewMgr.GetCommand

#### Syntax

[ExecutionViewMgr](executionviewmgr.html).GetCommand( cmdKind, commandIndex = 0)

#### Return Value

[Command](command.html)

#### Purpose

Creates a Command object. When applicable, the command operates on the items the ExecutionView Manager control selects.

#### Parameters

cmdKind
 As
 [CommandKinds](commandkinds.html)

[In] Specifies the type of Command object to create.

commandIndex
 As
 [Long](data-types-for-teststand-user-interface.html)

[In] Pass this parameter on commands that are sets to specify which command in the set to return.

This parameter has a default value of
 0
 .

#### See Also

[ApplicationMgr.GetCommand](applicationmgr-getcommand.html)

[CommandKinds](commandkinds.html)

[SequenceFileViewMgr.GetCommand](sequencefileviewmgr-getcommand.html)

Parent topic:

Methods

<!--NI_TOPIC bundle=teststand-api-reference path=tsuiref/executionviewmgr-getimagename.html language=enus -->
## TOPIC 04992: ExecutionViewMgr.GetImageName

- bundle_id: `teststand-api-reference`
- source_path: `tsuiref/executionviewmgr-getimagename.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsuiref/executionviewmgr-getimagename.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax ExecutionViewMgr.GetImageName( imageSource) Return Value String The current image name for the image source you specify. Purpose Returns the current image name for an image source in an ExecutionView Manager control. Use the Images.FindImage method to acquire a reference to the image. Paramet

### ExecutionViewMgr.GetImageName

#### Syntax

[ExecutionViewMgr](executionviewmgr.html).GetImageName( imageSource)

#### Return Value

[String](data-types-for-teststand-user-interface.html)

The current image name for the image source you specify.

#### Purpose

Returns the current image name for an image source in an ExecutionView Manager control. Use the
 
 [Images.FindImage](../tsapiref/images-findimage.html)
 method to acquire a reference to the image.

#### Parameters

imageSource
 As
 [ImageSources](imagesources.html)

[In] Specifies the type of image source from which to obtain an image name.

#### See Also

[ApplicationMgr.GetImageName](applicationmgr-getimagename.html)

[Engine.Images](../tsapiref/engine-images.html)

[Images.FindImage](../tsapiref/images-findimage.html)

[SequenceFileViewMgr.GetImageName](sequencefileviewmgr-getimagename.html)

Parent topic:

Methods

<!--NI_TOPIC bundle=teststand-api-reference path=tsuiref/executionviewmgr-getnumericvalue.html language=enus -->
## TOPIC 04993: ExecutionViewMgr.GetNumericValue

- bundle_id: `teststand-api-reference`
- source_path: `tsuiref/executionviewmgr-getnumericvalue.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsuiref/executionviewmgr-getnumericvalue.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax ExecutionViewMgr.GetNumericValue( numericSource) Return Value Double The current value for the numeric source you specify. Purpose Returns the current numeric value for a numeric source in an ExecutionView Manager control. Parameters numericSource As NumericSources [In] Specifies the type of

### ExecutionViewMgr.GetNumericValue

#### Syntax

[ExecutionViewMgr](executionviewmgr.html).GetNumericValue( numericSource)

#### Return Value

[Double](data-types-for-teststand-user-interface.html)

The current value for the numeric source you specify.

#### Purpose

Returns the current numeric value for a numeric source in an ExecutionView Manager control.

#### Parameters

numericSource
 As
 [NumericSources](numericsources.html)

[In] Specifies the type of numeric source from which to obtain a numeric value.

Parent topic:

Methods

<!--NI_TOPIC bundle=teststand-api-reference path=tsuiref/executionviewmgr-looponselectedsteps.html language=enus -->
## TOPIC 04994: ExecutionViewMgr.LoopOnSelectedSteps

- bundle_id: `teststand-api-reference`
- source_path: `tsuiref/executionviewmgr-looponselectedsteps.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsuiref/executionviewmgr-looponselectedsteps.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax ExecutionViewMgr.LoopOnSelectedSteps( [interArgs]) Purpose Starts an interactive execution that loops on the currently selected steps. Remarks You can call this method only when the execution is paused and the execution is not in interactive mode. Parameters interArgs As Variant [In] [ Option

### ExecutionViewMgr.LoopOnSelectedSteps

#### Syntax

[ExecutionViewMgr](executionviewmgr.html).LoopOnSelectedSteps( [interArgs])

#### Purpose

Starts an interactive execution that loops on the currently selected steps.

#### Remarks

Note

#### Parameters

interArgs
 As
 [Variant](data-types-for-teststand-user-interface.html)

[In] [
 [Optional](/csh?context=ts_tsuiref_optional_parameters)
 ] Specifies an
 
 [InteractiveArgs](../tsapiref/interactiveargs.html)
 object. When you do not pass an
 InteractiveArgs
 object, the ExecutionView Manager control creates the appropriate
 InteractiveArgs
 object.

#### See Also

[CommandKind_LoopOnSelectedSteps](commandkinds.html)

[ExecutionViewMgr.BuildInteractiveArgs](executionviewmgr-buildinteractiveargs.html)

[ExecutionViewMgr.RunSelectedSteps](executionviewmgr-runselectedsteps.html)

[Omitting Optional Parameters](/csh?context=ts_tsapiref_optional_parameters)

Parent topic:

Methods

<!--NI_TOPIC bundle=teststand-api-reference path=tsuiref/executionviewmgr-neweditcontext.html language=enus -->
## TOPIC 04995: ExecutionViewMgr.NewEditContext

- bundle_id: `teststand-api-reference`
- source_path: `tsuiref/executionviewmgr-neweditcontext.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsuiref/executionviewmgr-neweditcontext.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax ExecutionViewMgr.NewEditContext Return Value SequenceContext Purpose Returns a SequenceContext object that has a Step property that has only properties common to all the currently selected steps. Use the SequenceContext.GetMultipleValues method to determine whether the values of the Step subp

### ExecutionViewMgr.NewEditContext

#### Syntax

[ExecutionViewMgr](executionviewmgr.html).NewEditContext

#### Return Value

[SequenceContext](../tsapiref/sequencecontext.html)

#### Purpose

Returns a
 SequenceContext
 object that has a
 Step
 property that has only properties common to all the currently selected steps. Use the
 
 [SequenceContext.GetMultipleValues](../tsapiref/sequencecontext-getmultiplevalues.html)
 method to determine whether the values of the
 Step
 subproperties are common across all the currently selected steps.

#### See Also

[Engine.NewEditContext](../tsapiref/engine-neweditcontext.html)

[SequenceContext.GetMultipleValues](../tsapiref/sequencecontext-getmultiplevalues.html)

[SequenceContext.SetMultipleValues](../tsapiref/sequencecontext-setmultiplevalues.html)

[SequenceFileViewMgr.NewEditContext](sequencefileviewmgr-neweditcontext.html)

Parent topic:

Methods

<!--NI_TOPIC bundle=teststand-api-reference path=tsuiref/executionviewmgr-propertyobjectselectionchang.html language=enus -->
## TOPIC 04996: ExecutionViewMgr.PropertyObjectSelectionChanged

- bundle_id: `teststand-api-reference`
- source_path: `tsuiref/executionviewmgr-propertyobjectselectionchang.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsuiref/executionviewmgr-propertyobjectselectionchang.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax ControlName_PropertyObjectSelectionChanged Applies To ExecutionViewMgr Purpose Occurs when the selected property objects change. For example, this event is generated when you change the selection in a VariablesView control that connects to the ExecutionView Manager control or when you program

### ExecutionViewMgr.PropertyObjectSelectionChanged

#### Syntax

ControlName_PropertyObjectSelectionChanged

#### Applies To

[ExecutionViewMgr](executionviewmgr.html)

#### Purpose

Occurs when the selected property objects change. For example, this event is generated when you change the selection in a
 [VariablesView](variablesview.html)
 control that connects to the
 [ExecutionView Manager](executionviewmgr.html)
 control or when you programmatically change the contents of the
 [SelectedPropertyObjects](executionviewmgr-selectedpropertyobjects.html)
 collection.

#### See Also

[ExecutionViewMgr](executionviewmgr.html)

[SelectedPropertyObjects](executionviewmgr-selectedpropertyobjects.html)

[SequenceFileViewMgr.PropertyObjectSelectionChanged](sequencefileviewmgr-propertyobjectselectionch.html)

[VariablesView](variablesview.html)

Parent topic:

Events

<!--NI_TOPIC bundle=teststand-api-reference path=tsuiref/executionviewmgr-refresh.html language=enus -->
## TOPIC 04997: ExecutionViewMgr.Refresh

- bundle_id: `teststand-api-reference`
- source_path: `tsuiref/executionviewmgr-refresh.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsuiref/executionviewmgr-refresh.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax ExecutionViewMgr.Refresh( [seqCtxt]) Purpose Refreshes all connected controls. Remarks Typically, you do not call this method unless you have changed the state of the execution directly using the API. Call this method so these types of changes are reflected in the connected controls. Paramete

### ExecutionViewMgr.Refresh

#### Syntax

[ExecutionViewMgr](executionviewmgr.html).Refresh( [seqCtxt])

#### Purpose

Refreshes all connected controls.

#### Remarks

Typically, you do not call this method unless you have changed the state of the execution directly using the API. Call this method so these types of changes are reflected in the connected controls.

#### Parameters

seqCtxt
 As
 [Variant](data-types-for-teststand-user-interface.html)

[In] [
 [Optional](/csh?context=ts_tsuiref_optional_parameters)
 ] Specifies the SequenceContext used to refresh the controls. When you do pass a SequenceContext, the ExecutionView Manager control uses the current SequenceContext to refresh the controls.

#### See Also

[ApplicationMgr.Refresh](applicationmgr-refresh.html)

[ApplicationMgr.RefreshAllViewMgrs](applicationmgr-refreshallviewmgrs.html)

[Omitting Optional Parameters](/csh?context=ts_tsapiref_optional_parameters)

[SequenceFileViewMgr.Refresh](sequencefileviewmgr-refresh.html)

Parent topic:

Methods

<!--NI_TOPIC bundle=teststand-api-reference path=tsuiref/executionviewmgr-refreshstep.html language=enus -->
## TOPIC 04998: ExecutionViewMgr.RefreshStep

- bundle_id: `teststand-api-reference`
- source_path: `tsuiref/executionviewmgr-refreshstep.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsuiref/executionviewmgr-refreshstep.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax ExecutionViewMgr.RefreshStep( stepIndex) Purpose Refreshes a step in a SequenceView control connected to the ExecutionView Manager control. When the value of the ExecutionViewMgr.StepGroupMode property is not StepGroupMode_OneGroup , call ExecutionViewMgr.RefreshStepEx instead so you can spec

### ExecutionViewMgr.RefreshStep

#### Syntax

[ExecutionViewMgr](executionviewmgr.html).RefreshStep( stepIndex)

#### Purpose

Refreshes a step in a
 [SequenceView](sequenceview.html)
 control connected to the ExecutionView Manager control.

Note

ExecutionViewMgr.StepGroupMode

StepGroupMode_OneGroup

ExecutionViewMgr.RefreshStepEx

#### Remarks

Typically, you do not call this method unless you have changed the state of the step directly using the TestStand API. Call this method so these types of changes are reflected in connected SequenceView controls.

#### Parameters

stepIndex
 As
 [Long](data-types-for-teststand-user-interface.html)

[In] Specifies the index of the step to refresh. Passing
 -1
 refreshes all the steps in the connected SequenceView control.

#### See Also

[ExecutionViewMgr.RefreshStepEx](executionviewmgr-refreshstepex.html)

[ExecutionViewMgr.StepGroupMode](executionviewmgr-stepgroupmode.html)

[SequenceView](sequenceview.html)

Parent topic:

Methods

<!--NI_TOPIC bundle=teststand-api-reference path=tsuiref/executionviewmgr-refreshstepex.html language=enus -->
## TOPIC 04999: ExecutionViewMgr.RefreshStepEx

- bundle_id: `teststand-api-reference`
- source_path: `tsuiref/executionviewmgr-refreshstepex.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsuiref/executionviewmgr-refreshstepex.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax ExecutionViewMgr.RefreshStepEx( group, stepIndex) Purpose Refreshes a step in all connected SequenceView controls. Remarks Typically, you do not call this method unless you change the state of the step directly using the TestStand API. Parameters group As StepGroups [In] Specifies a particula

### ExecutionViewMgr.RefreshStepEx

#### Syntax

[ExecutionViewMgr](executionviewmgr.html).RefreshStepEx( group, stepIndex)

#### Purpose

Refreshes a step in all connected
 [SequenceView](sequenceview.html)
 controls.

#### Remarks

Typically, you do not call this method unless you change the state of the step directly using the TestStand API.

#### Parameters

group
 As
 
 [StepGroups](../tsapiref/stepgroups.html)

[In] Specifies a particular step group.

stepIndex
 As
 [Long](data-types-for-teststand-user-interface.html)

[In] Specifies the zero-based index in the step group of the step to refresh. Pass
 -1
 to refresh all the steps in all groups in the connected SequenceView controls.

#### See Also

[SequenceView](sequenceview.html)

Parent topic:

Methods

<!--NI_TOPIC bundle=teststand-api-reference path=tsuiref/executionviewmgr-refreshwindow.html language=enus -->
## TOPIC 05000: ExecutionViewMgr.RefreshWindow

- bundle_id: `teststand-api-reference`
- source_path: `tsuiref/executionviewmgr-refreshwindow.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsuiref/executionviewmgr-refreshwindow.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax ControlName_RefreshWindow( ctxt) Applies To ExecutionViewMgr Purpose Occurs when TestStand sends a UIMsg_RefreshWindows message that requires a refresh of the selected execution. Parameters ctxt As SequenceContext [In] Specifies the context of the steps to be refreshed. When the context is no

### ExecutionViewMgr.RefreshWindow

#### Syntax

ControlName_RefreshWindow( ctxt)

#### Applies To

[ExecutionViewMgr](executionviewmgr.html)

#### Purpose

Occurs when TestStand sends a
 UIMsg_RefreshWindows
 message that requires a refresh of the selected execution.

#### Parameters

ctxt
 As
 
 [SequenceContext](../tsapiref/sequencecontext.html)

[In] Specifies the context of the steps to be refreshed. When the context is not passed in, the steps in the current context refresh.

#### See Also

[ApplicationMgr.RefreshWindows](applicationmgr-refreshwindows.html)

[ExecutionViewMgr.Refresh](executionviewmgr-refresh.html)

[SequenceFileViewMgr.RefreshWindow](sequencefileviewmgr-refreshwindow.html)

[UIMsg_RefreshWindows](../tsapiref/uimessagecodes.html)

Parent topic:

Events
