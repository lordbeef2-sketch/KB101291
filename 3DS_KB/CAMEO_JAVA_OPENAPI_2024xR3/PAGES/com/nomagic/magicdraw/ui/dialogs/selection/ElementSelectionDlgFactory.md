# JAVA OPENAPI: ElementSelectionDlgFactory (2024x Refresh3 API)

- source_url: https://jdocs.nomagic.com/2024xRefresh3/com/nomagic/magicdraw/ui/dialogs/selection/ElementSelectionDlgFactory.html
- source_path: `com/nomagic/magicdraw/ui/dialogs/selection/ElementSelectionDlgFactory.html`
- source_sha256: `268f6ce9d4e02536eea2ef0af97484a84484aa39c1c3fb1b83671b77a70210a8`
- captured_utc: `2026-07-14T16:55:51.932419+00:00`

## NORMALIZED JAVADOC CONTENT

======== START OF CLASS DATA ========

Package [com.nomagic.magicdraw.ui.dialogs.selection](package-summary.html)

## Class ElementSelectionDlgFactory

[java.lang.Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)
com.dassault_systemes.modeler.magic.ui.dialogs.selection.ElementSelectionDlgFactory
com.nomagic.magicdraw.ui.dialogs.selection.ElementSelectionDlgFactory

@OpenApipublic classElementSelectionDlgFactory
extends com.dassault_systemes.modeler.magic.ui.dialogs.selection.ElementSelectionDlgFactory

Element Selection dialog factory class. This factory should be used to create instances of ElementSelectionDlg
 and also configure dialog initial settings.

##### Selecting elements via element Selection dialog

````java
// Use ElementSelectionDlgFactory.create(...) methods to create element selection dialog.
 Frame dialogParent = MDDialogParentProvider.getProvider().getDialogParent();
 ElementSelectionDlg dlg = ElementSelectionDlgFactory.create(dialogParent);

 // Use ElementSelectionDlgFactory.initSingle(...) methods to initialize the dialog with single element selection mode.
 ElementSelectionDlgFactory.initSingle(....);

 // Use ElementSelectionDlgFactory.initMultiple(...) methods to initialize the dialog with multiple element selection mode.
 ElementSelectionDlgFactory.initMultiple(....);

 // Display dialog for the user to select elements.
 dlg.show();

 // Check if the user has clicked "Ok".
 if (dlg.isOkClicked())
 {
     // Get selected element in single selection mode.a
     BaseElement selected = dlg.getSelectedElement();

     // Get selected elements in multiple selection mode.
     BaseElement selected = dlg.getSelectedElements();
 }
````

See Also:
[`ElementSelectionDlg`](ElementSelectionDlg.html)
[`SelectElementInfo`](../SelectElementInfo.html)
[`ClassTypes`](../../../uml/ClassTypes.html)
[`SelectElementTypes`](../SelectElementTypes.html)
[`TypeFilter`](TypeFilter.html)
[`TypeFilterImpl`](TypeFilterImpl.html)
[`ModelHelper`](../../../../uml2/ext/jmi/helpers/ModelHelper.html)

=========== FIELD SUMMARY =========== 
Field Summary
Fields inherited from class com.dassault_systemes.modeler.magic.ui.dialogs.selection.ElementSelectionDlgFactory
`HELP_PATH, SELECT_ELEMENT_TITLE, SELECT_ELEMENTS_TITLE`
 ======== CONSTRUCTOR SUMMARY ======== 
Constructor Summary
Constructors
Constructor
Description
`[ElementSelectionDlgFactory](#%3Cinit%3E())()`
 ========== METHOD SUMMARY =========== 
Method Summary
All MethodsStatic MethodsConcrete Methods
Modifier and Type
Method
Description
`static [Collection](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html)`
`[collectDisplayable](#collectDisplayable(java.util.Collection,java.util.Collection))([Collection](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html) displayable,
 [Collection](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html) selectable)`
Collect displayable types for a given selectable types if given displayable is null
`static [ElementSelectionDlg](ElementSelectionDlg.html)`
`[create](#create())()`
Create an instance of the dialog
`static [ElementSelectionDlg](ElementSelectionDlg.html)`
`[create](#create(java.awt.Dialog))([Dialog](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Dialog.html) parent)`
Create an instance of dialog
`static [ElementSelectionDlg](ElementSelectionDlg.html)`
`[create](#create(java.awt.Dialog,java.lang.String,java.lang.String))([Dialog](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Dialog.html) parent,
 [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) title,
 [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) helpPath)`
Create an instance of dialog
`static [ElementSelectionDlg](ElementSelectionDlg.html)`
`[create](#create(java.awt.Frame))([Frame](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Frame.html) parent)`
Create an instance of dialog
`static [ElementSelectionDlg](ElementSelectionDlg.html)`
`[create](#create(java.awt.Frame,com.dassault_systemes.modeler.magic.ui.selection.ElementSelectionContext))([Frame](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Frame.html) parent,
 com.dassault_systemes.modeler.magic.ui.selection.ElementSelectionContext context)`

`static [ElementSelectionDlg](ElementSelectionDlg.html)`
`[create](#create(java.awt.Frame,java.lang.String,java.lang.String))([Frame](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Frame.html) parent,
 [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) title,
 [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) helpPath)`
Create an instance of dialog
`static [ElementSelectionDlg](ElementSelectionDlg.html)`
`[create](#create(java.awt.Window))([Window](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Window.html) parent)`
Create an instance of dialog
`static [ElementSelectionDlg](ElementSelectionDlg.html)`
`[create](#create(java.awt.Window,com.dassault_systemes.modeler.magic.ui.selection.ElementSelectionContext))([Window](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Window.html) parent,
 com.dassault_systemes.modeler.magic.ui.selection.ElementSelectionContext context)`

`static [ElementSelectionDlg](ElementSelectionDlg.html)`
`[create](#create(java.awt.Window,java.lang.String,java.lang.String))([Window](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Window.html) parent,
 [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) title,
 [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) helpPath)`
Create an instance of dialog
`static [ElementSelectionDlg](ElementSelectionDlg.html)`
`[create](#create(java.awt.Window,java.lang.String,java.lang.String,com.dassault_systemes.modeler.magic.ui.selection.ElementSelectionContext))([Window](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Window.html) parent,
 [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) title,
 [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) helpPath,
 com.dassault_systemes.modeler.magic.ui.selection.ElementSelectionContext context)`

`static [TypeFilter](TypeFilter.html)`
`[createDisplayableForSelectable](#createDisplayableForSelectable(com.nomagic.magicdraw.ui.dialogs.selection.TypeFilter))([TypeFilter](TypeFilter.html) selectable)`
Create displayable types filter for a given selectable types filter.
`static [TypeFilter](TypeFilter.html)`
`[createDisplayableForSelectable](#createDisplayableForSelectable(java.util.Collection))([Collection](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html) selectable)`
Create displayable types filter for a given selectable types.
`static [TypeFilter](TypeFilter.html)`
`[createDisplayableForSelectable](#createDisplayableForSelectable(java.util.Collection,com.nomagic.magicdraw.ui.dialogs.selection.TypeFilter))([Collection](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html) displayable,
 [TypeFilter](TypeFilter.html) selectable)`
Create displayable types filter for a given selectable types filter if given displayable is null
`static void`
`[initMultiple](#initMultiple(com.nomagic.magicdraw.ui.dialogs.selection.ElementSelectionDlg,com.nomagic.magicdraw.ui.dialogs.SelectElementInfo,com.nomagic.magicdraw.ui.dialogs.selection.TypeFilter,com.nomagic.magicdraw.ui.dialogs.selection.TypeFilter,boolean,java.util.Collection,java.lang.Object%5B%5D))([ElementSelectionDlg](ElementSelectionDlg.html) dlg,
 [SelectElementInfo](../SelectElementInfo.html) info,
 [TypeFilter](TypeFilter.html) visibleElementsFilter,
 [TypeFilter](TypeFilter.html) selectableElementsFilter,
 boolean usedAsType,
 [Collection](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html)<?> creatableTypes,
 [Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)[] selection)`
Initializes given dialog with a "multiple elements" selection mode.
`static void`
`[initMultiple](#initMultiple(com.nomagic.magicdraw.ui.dialogs.selection.ElementSelectionDlg,com.nomagic.magicdraw.ui.dialogs.SelectElementInfo,com.nomagic.magicdraw.ui.dialogs.selection.TypeFilter,com.nomagic.magicdraw.ui.dialogs.selection.TypeFilter,boolean,java.util.Collection,java.util.List))([ElementSelectionDlg](ElementSelectionDlg.html) dlg,
 [SelectElementInfo](../SelectElementInfo.html) info,
 [TypeFilter](TypeFilter.html) visibleElementsFilter,
 [TypeFilter](TypeFilter.html) selectableElementsFilter,
 boolean usedAsType,
 [Collection](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html)<?> creatableTypes,
 [List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html)<?> selection)`
Initializes given dialog with a "multiple elements" selection mode.
`static void`
`[initMultiple](#initMultiple(com.nomagic.magicdraw.ui.dialogs.selection.ElementSelectionDlg,com.nomagic.magicdraw.ui.dialogs.SelectElementInfo,com.nomagic.magicdraw.ui.dialogs.selection.TypeFilter,com.nomagic.magicdraw.ui.dialogs.selection.TypeFilter,java.util.Collection,java.lang.Object%5B%5D))([ElementSelectionDlg](ElementSelectionDlg.html) dlg,
 [SelectElementInfo](../SelectElementInfo.html) info,
 [TypeFilter](TypeFilter.html) visibleElementsFilter,
 [TypeFilter](TypeFilter.html) selectableElementsFilter,
 [Collection](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html)<?> creatableTypes,
 [Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)[] selection)`
Initializes given dialog with a "multiple elements" selection mode.
`static void`
`[initMultiple](#initMultiple(com.nomagic.magicdraw.ui.dialogs.selection.ElementSelectionDlg,com.nomagic.magicdraw.ui.dialogs.SelectElementInfo,com.nomagic.magicdraw.ui.dialogs.selection.TypeFilter,com.nomagic.magicdraw.ui.dialogs.selection.TypeFilter,java.util.Collection,java.util.List))([ElementSelectionDlg](ElementSelectionDlg.html) dlg,
 [SelectElementInfo](../SelectElementInfo.html) info,
 [TypeFilter](TypeFilter.html) visibleElementsFilter,
 [TypeFilter](TypeFilter.html) selectableElementsFilter,
 [Collection](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html)<?> creatableTypes,
 [List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html)<?> selection)`
Initializes given dialog with a "multiple elements" selection mode.
`static void`
`[initMultiple](#initMultiple(com.nomagic.magicdraw.ui.dialogs.selection.ElementSelectionDlg,com.nomagic.magicdraw.ui.dialogs.SelectElementTypes,com.nomagic.magicdraw.ui.dialogs.SelectElementInfo,java.lang.Object%5B%5D))([ElementSelectionDlg](ElementSelectionDlg.html) dlg,
 [SelectElementTypes](../SelectElementTypes.html) types,
 [SelectElementInfo](../SelectElementInfo.html) info,
 [Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)[] selection)`
Initializes given dialog with a "multiple elements" selection mode.
`static void`
`[initMultiple](#initMultiple(com.nomagic.magicdraw.ui.dialogs.selection.ElementSelectionDlg,com.nomagic.magicdraw.ui.dialogs.SelectElementTypes,com.nomagic.magicdraw.ui.dialogs.SelectElementInfo,java.util.List))([ElementSelectionDlg](ElementSelectionDlg.html) dlg,
 [SelectElementTypes](../SelectElementTypes.html) types,
 [SelectElementInfo](../SelectElementInfo.html) info,
 [List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html) selection)`
Initializes given dialog with a "multiple elements" selection mode.
`static void`
`[initMultipleAsMultipleInitial](#initMultipleAsMultipleInitial(com.nomagic.magicdraw.ui.dialogs.selection.ElementSelectionDlg,com.nomagic.magicdraw.ui.dialogs.SelectElementInfo,com.nomagic.magicdraw.ui.dialogs.selection.TypeFilter,com.nomagic.magicdraw.ui.dialogs.selection.TypeFilter,java.util.Collection,java.util.List))([ElementSelectionDlg](ElementSelectionDlg.html) dlg,
 [SelectElementInfo](../SelectElementInfo.html) info,
 [TypeFilter](TypeFilter.html) visibleElementsFilter,
 [TypeFilter](TypeFilter.html) selectableElementsFilter,
 [Collection](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html)<?> creatableTypes,
 [List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html)<?> selection)`
Initializes given dialog with a "multiple elements" selection mode.
`static void`
`[initSingle](#initSingle(com.nomagic.magicdraw.ui.dialogs.selection.ElementSelectionDlg,com.nomagic.magicdraw.ui.dialogs.SelectElementInfo,com.nomagic.magicdraw.ui.dialogs.selection.TypeFilter,com.nomagic.magicdraw.ui.dialogs.selection.TypeFilter,boolean,java.util.Collection,java.lang.Object))([ElementSelectionDlg](ElementSelectionDlg.html) dlg,
 [SelectElementInfo](../SelectElementInfo.html) info,
 [TypeFilter](TypeFilter.html) visibleElementsFilter,
 [TypeFilter](TypeFilter.html) selectableElementsFilter,
 boolean usedAsType,
 [Collection](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html)<?> creatableTypes,
 [Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html) selection)`
Initializes given dialog with a "single element" selection mode.
`static void`
`[initSingle](#initSingle(com.nomagic.magicdraw.ui.dialogs.selection.ElementSelectionDlg,com.nomagic.magicdraw.ui.dialogs.SelectElementInfo,com.nomagic.magicdraw.ui.dialogs.selection.TypeFilter,com.nomagic.magicdraw.ui.dialogs.selection.TypeFilter,java.util.Collection,java.lang.Object))([ElementSelectionDlg](ElementSelectionDlg.html) dlg,
 [SelectElementInfo](../SelectElementInfo.html) info,
 [TypeFilter](TypeFilter.html) visibleElementsFilter,
 [TypeFilter](TypeFilter.html) selectableElementsFilter,
 [Collection](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html)<?> creatableTypes,
 [Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html) selection)`
Initializes given dialog with a "single element" selection mode.
`static void`
`[initSingle](#initSingle(com.nomagic.magicdraw.ui.dialogs.selection.ElementSelectionDlg,com.nomagic.magicdraw.ui.dialogs.SelectElementTypes,com.nomagic.magicdraw.ui.dialogs.SelectElementInfo,java.lang.Object))([ElementSelectionDlg](ElementSelectionDlg.html) dlg,
 [SelectElementTypes](../SelectElementTypes.html) types,
 [SelectElementInfo](../SelectElementInfo.html) info,
 [Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html) selection)`
Initializes given dialog with a "single element" selection mode.
`static [TypeFilter](TypeFilter.html)`
`[wrapWithTagsFilter](#wrapWithTagsFilter(com.nomagic.magicdraw.ui.dialogs.selection.TypeFilter))([TypeFilter](TypeFilter.html) inner)`
Creates tags filter from given type filter.
Methods inherited from class com.dassault_systemes.modeler.magic.ui.dialogs.selection.ElementSelectionDlgFactory
`addExternalFactory, create, setSelectionMode`
Methods inherited from class java.lang.[Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)
`[clone](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#clone()), [equals](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#equals(java.lang.Object)), [finalize](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#finalize()), [getClass](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#getClass()), [hashCode](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#hashCode()), [notify](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notify()), [notifyAll](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notifyAll()), [toString](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#toString()), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait()), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long)), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long,int))`

========= CONSTRUCTOR DETAIL ======== 
Constructor Details
ElementSelectionDlgFactory
public ElementSelectionDlgFactory()
 ============ METHOD DETAIL ========== 
Method Details
create
@OpenApipublic static [ElementSelectionDlg](ElementSelectionDlg.html) create()
Create an instance of the dialog
Returns:
dialog instance
create
@OpenApipublic static [ElementSelectionDlg](ElementSelectionDlg.html) create(@CheckForNull
 [Frame](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Frame.html) parent)
Create an instance of dialog
Parameters:
`parent` - dialog parent
Returns:
dialog instance
create
public static [ElementSelectionDlg](ElementSelectionDlg.html) create(@CheckForNull
 [Frame](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Frame.html) parent,
 @CheckForNull
 com.dassault_systemes.modeler.magic.ui.selection.ElementSelectionContext context)
create
@OpenApipublic static [ElementSelectionDlg](ElementSelectionDlg.html) create(@CheckForNull
 [Frame](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Frame.html) parent,
 @CheckForNull
 [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) title,
 @CheckForNull
 [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) helpPath)
Create an instance of dialog
Parameters:
`parent` - dialog parent
`title` - dialog title
`helpPath` - help id
Returns:
dialog instance
create
@OpenApipublic static [ElementSelectionDlg](ElementSelectionDlg.html) create(@CheckForNull
 [Window](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Window.html) parent)
Create an instance of dialog
Parameters:
`parent` - dialog parent
Returns:
dialog instance
create
public static [ElementSelectionDlg](ElementSelectionDlg.html) create(@CheckForNull
 [Window](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Window.html) parent,
 @CheckForNull
 com.dassault_systemes.modeler.magic.ui.selection.ElementSelectionContext context)
create
@OpenApipublic static [ElementSelectionDlg](ElementSelectionDlg.html) create(@CheckForNull
 [Window](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Window.html) parent,
 @CheckForNull
 [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) title,
 @CheckForNull
 [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) helpPath)
Create an instance of dialog
Parameters:
`parent` - dialog parent
`title` - dialog title
`helpPath` - help id
Returns:
dialog instance
create
public static [ElementSelectionDlg](ElementSelectionDlg.html) create(@CheckForNull
 [Window](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Window.html) parent,
 @CheckForNull
 [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) title,
 @CheckForNull
 [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) helpPath,
 @CheckForNull
 com.dassault_systemes.modeler.magic.ui.selection.ElementSelectionContext context)
create
@OpenApipublic static [ElementSelectionDlg](ElementSelectionDlg.html) create(@CheckForNull
 [Dialog](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Dialog.html) parent)
Create an instance of dialog
Parameters:
`parent` - dialog parent
Returns:
dialog instance
create
@OpenApipublic static [ElementSelectionDlg](ElementSelectionDlg.html) create(@CheckForNull
 [Dialog](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Dialog.html) parent,
 @CheckForNull
 [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) title,
 @CheckForNull
 [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) helpPath)
Create an instance of dialog
Parameters:
`parent` - dialog parent
`title` - dialog title
`helpPath` - help id
Returns:
dialog instance
collectDisplayable
@OpenApipublic static [Collection](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html) collectDisplayable(@CheckForNull
 [Collection](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html) displayable,
 [Collection](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html) selectable)
Collect displayable types for a given selectable types if given displayable is null
Parameters:
`displayable` - displayable types
`selectable` - selectable types
Returns:
displayable types
createDisplayableForSelectable
@OpenApipublic static [TypeFilter](TypeFilter.html) createDisplayableForSelectable(@CheckForNull
 [Collection](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html) displayable,
 [TypeFilter](TypeFilter.html) selectable)
Create displayable types filter for a given selectable types filter if given displayable is null
Parameters:
`displayable` - displayable types
`selectable` - selectable types
Returns:
displayable types
createDisplayableForSelectable
@OpenApipublic static [TypeFilter](TypeFilter.html) createDisplayableForSelectable([TypeFilter](TypeFilter.html) selectable)
Create displayable types filter for a given selectable types filter.
Parameters:
`selectable` - selectable types
Returns:
displayable types
createDisplayableForSelectable
@OpenApipublic static [TypeFilter](TypeFilter.html) createDisplayableForSelectable([Collection](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html) selectable)
Create displayable types filter for a given selectable types.
Parameters:
`selectable` - selectable types
Returns:
displayable types
initSingle
@OpenApipublic static void initSingle([ElementSelectionDlg](ElementSelectionDlg.html) dlg,
 [SelectElementTypes](../SelectElementTypes.html) types,
 [SelectElementInfo](../SelectElementInfo.html) info,
 @CheckForNull
 [Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html) selection)
Initializes given dialog with a "single element" selection mode. It means dialog will allow to select
 just a single element.
Parameters:
`dlg` - dialog
`types` - element selection information
`info` - dialog settings
`selection` - initially selected element
initMultiple
@OpenApipublic static void initMultiple([ElementSelectionDlg](ElementSelectionDlg.html) dlg,
 [SelectElementTypes](../SelectElementTypes.html) types,
 [SelectElementInfo](../SelectElementInfo.html) info,
 @CheckForNull
 [Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)[] selection)
Initializes given dialog with a "multiple elements" selection mode. It means dialog will allow to select
 several elements.
Parameters:
`dlg` - dialog
`types` - element selection information
`info` - dialog settings
`selection` - initially selected elements
initMultiple
@OpenApipublic static void initMultiple([ElementSelectionDlg](ElementSelectionDlg.html) dlg,
 [SelectElementTypes](../SelectElementTypes.html) types,
 [SelectElementInfo](../SelectElementInfo.html) info,
 @CheckForNull
 [List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html) selection)
Initializes given dialog with a "multiple elements" selection mode. It means dialog will allow to select
 several elements.
Parameters:
`dlg` - dialog
`types` - element selection information
`info` - dialog settings
`selection` - initially selected elements
initSingle
@OpenApipublic static void initSingle([ElementSelectionDlg](ElementSelectionDlg.html) dlg,
 [SelectElementInfo](../SelectElementInfo.html) info,
 [TypeFilter](TypeFilter.html) visibleElementsFilter,
 [TypeFilter](TypeFilter.html) selectableElementsFilter,
 @CheckForNull
 [Collection](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html)<?> creatableTypes,
 @CheckForNull
 [Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html) selection)
Initializes given dialog with a "single element" selection mode. It means dialog will allow to select
 just a single element.
Parameters:
`dlg` - dialog
`info` - dialog settings
`visibleElementsFilter` - filter providing visible elements in the dialog
`selectableElementsFilter` - filter providing selectable elements in the dialog
`creatableTypes` - collection of creatable types (choice on Create button)
`selection` - initially selected element
initSingle
@OpenApipublic static void initSingle([ElementSelectionDlg](ElementSelectionDlg.html) dlg,
 [SelectElementInfo](../SelectElementInfo.html) info,
 [TypeFilter](TypeFilter.html) visibleElementsFilter,
 [TypeFilter](TypeFilter.html) selectableElementsFilter,
 boolean usedAsType,
 @CheckForNull
 [Collection](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html)<?> creatableTypes,
 @CheckForNull
 [Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html) selection)
Initializes given dialog with a "single element" selection mode. It means dialog will allow to select
 just a single element.
Parameters:
`dlg` - dialog
`info` - dialog settings
`visibleElementsFilter` - filter providing visible elements in the dialog
`selectableElementsFilter` - filter providing selectable elements in the dialog
`usedAsType` - is this dialog instance is used to select some UML Type. If true, some special filters
 from DSL will be used for elements filtering
`creatableTypes` - collection of creatable types (choice on Create button)
`selection` - initially selected element
initMultiple
@OpenApipublic static void initMultiple([ElementSelectionDlg](ElementSelectionDlg.html) dlg,
 [SelectElementInfo](../SelectElementInfo.html) info,
 [TypeFilter](TypeFilter.html) visibleElementsFilter,
 [TypeFilter](TypeFilter.html) selectableElementsFilter,
 boolean usedAsType,
 @CheckForNull
 [Collection](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html)<?> creatableTypes,
 @CheckForNull
 [Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)[] selection)
Initializes given dialog with a "multiple elements" selection mode. It means dialog will allow to select
 several elements.
Parameters:
`dlg` - dialog
`info` - dialog settings
`visibleElementsFilter` - filter providing visible elements in the dialog
`selectableElementsFilter` - filter providing selectable elements in the dialog
`usedAsType` - is this dialog instance is used to select some UML Type. If true, some special filters
 from DSL will be used for elements filtering
`creatableTypes` - collection of creatable types (choice on Create button)
`selection` - initially selected element
initMultiple
@OpenApipublic static void initMultiple([ElementSelectionDlg](ElementSelectionDlg.html) dlg,
 [SelectElementInfo](../SelectElementInfo.html) info,
 [TypeFilter](TypeFilter.html) visibleElementsFilter,
 [TypeFilter](TypeFilter.html) selectableElementsFilter,
 @CheckForNull
 [Collection](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html)<?> creatableTypes,
 @CheckForNull
 [Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)[] selection)
Initializes given dialog with a "multiple elements" selection mode. It means dialog will allow to select
 several elements.
Parameters:
`dlg` - dialog
`info` - dialog settings
`visibleElementsFilter` - filter providing visible elements in the dialog
`selectableElementsFilter` - filter providing selectable elements in the dialog
`creatableTypes` - collection of creatable types (choice on Create button)
`selection` - initially selected element
initMultiple
@OpenApipublic static void initMultiple([ElementSelectionDlg](ElementSelectionDlg.html) dlg,
 [SelectElementInfo](../SelectElementInfo.html) info,
 [TypeFilter](TypeFilter.html) visibleElementsFilter,
 [TypeFilter](TypeFilter.html) selectableElementsFilter,
 @CheckForNull
 [Collection](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html)<?> creatableTypes,
 @CheckForNull
 [List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html)<?> selection)
Initializes given dialog with a "multiple elements" selection mode. It means dialog will allow to select
 several elements.
Parameters:
`dlg` - dialog
`info` - dialog settings
`visibleElementsFilter` - filter providing visible elements in the dialog
`selectableElementsFilter` - filter providing selectable elements in the dialog
`creatableTypes` - collection of creatable types (choice on Create button)
`selection` - initially selected element
initMultiple
@OpenApipublic static void initMultiple([ElementSelectionDlg](ElementSelectionDlg.html) dlg,
 [SelectElementInfo](../SelectElementInfo.html) info,
 [TypeFilter](TypeFilter.html) visibleElementsFilter,
 [TypeFilter](TypeFilter.html) selectableElementsFilter,
 boolean usedAsType,
 @CheckForNull
 [Collection](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html)<?> creatableTypes,
 @CheckForNull
 [List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html)<?> selection)
Initializes given dialog with a "multiple elements" selection mode. It means dialog will allow to select
 several elements.
Parameters:
`dlg` - dialog
`info` - dialog settings
`visibleElementsFilter` - filter providing visible elements in the dialog
`selectableElementsFilter` - filter providing selectable elements in the dialog
`usedAsType` - is this dialog instance is used to select some UML Type. If true, some special filters
 from DSL will be used for elements filtering
`creatableTypes` - collection of creatable types (choice on Create button)
`selection` - initially selected element
initMultipleAsMultipleInitial
@OpenApipublic static void initMultipleAsMultipleInitial([ElementSelectionDlg](ElementSelectionDlg.html) dlg,
 [SelectElementInfo](../SelectElementInfo.html) info,
 [TypeFilter](TypeFilter.html) visibleElementsFilter,
 [TypeFilter](TypeFilter.html) selectableElementsFilter,
 @CheckForNull
 [Collection](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html)<?> creatableTypes,
 @CheckForNull
 [List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html)<?> selection)
Initializes given dialog with a "multiple elements" selection mode. It means dialog will allow to select
 several elements.
 Allows to set Multiple as mode initial multiple, (All initMultiple only use SINGLE_INITIAL)
Parameters:
`dlg` - dialog
`info` - dialog settings
`visibleElementsFilter` - filter providing visible elements in the dialog
`selectableElementsFilter` - filter providing selectable elements in the dialog
`creatableTypes` - collection of creatable types (choice on Create button)
`selection` - initially selected element
wrapWithTagsFilter
public static [TypeFilter](TypeFilter.html) wrapWithTagsFilter([TypeFilter](TypeFilter.html) inner)
Creates tags filter from given type filter. Tags filter in some cases are much faster than
 simple filter.
Parameters:
`inner` - type filter.
Returns:
created tags filter, or passed filter if it is already is tags filter.

========= END OF CLASS DATA =========

## EXACT JAVADOC MAIN HTML

````html
<main role="main">
<!-- ======== START OF CLASS DATA ======== -->
<div class="header">
<div class="sub-title"><span class="package-label-in-type">Package</span> <a href="package-summary.html">com.nomagic.magicdraw.ui.dialogs.selection</a></div>
<h1 class="title" title="Class ElementSelectionDlgFactory">Class ElementSelectionDlgFactory</h1>
</div>
<div class="inheritance" title="Inheritance Tree"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">java.lang.Object</a>
<div class="inheritance">com.dassault_systemes.modeler.magic.ui.dialogs.selection.ElementSelectionDlgFactory
<div class="inheritance">com.nomagic.magicdraw.ui.dialogs.selection.ElementSelectionDlgFactory</div>
</div>
</div>
<section class="class-description" id="class-description">
<hr/>
<div class="type-signature"><span class="annotations">@OpenApi
</span><span class="modifiers">public class </span><span class="element-name type-name-label">ElementSelectionDlgFactory</span>
<span class="extends-implements">extends com.dassault_systemes.modeler.magic.ui.dialogs.selection.ElementSelectionDlgFactory</span></div>
<div class="block">Element Selection dialog factory class. This factory should be used to create instances of ElementSelectionDlg
 and also configure dialog initial settings.

 <h4>Selecting elements via element Selection dialog</h4>
<pre>
 // Use ElementSelectionDlgFactory.create(...) methods to create element selection dialog.
 Frame dialogParent = MDDialogParentProvider.getProvider().getDialogParent();
 ElementSelectionDlg dlg = ElementSelectionDlgFactory.create(dialogParent);

 // Use ElementSelectionDlgFactory.initSingle(...) methods to initialize the dialog with single element selection mode.
 ElementSelectionDlgFactory.initSingle(....);

 // Use ElementSelectionDlgFactory.initMultiple(...) methods to initialize the dialog with multiple element selection mode.
 ElementSelectionDlgFactory.initMultiple(....);

 // Display dialog for the user to select elements.
 dlg.show();

 // Check if the user has clicked "Ok".
 if (dlg.isOkClicked())
 {
     // Get selected element in single selection mode.a
     BaseElement selected = dlg.getSelectedElement();

     // Get selected elements in multiple selection mode.
     BaseElement selected = dlg.getSelectedElements();
 }
 </pre></div>
<dl class="notes">
<dt>See Also:</dt>
<dd>
<ul class="see-list">
<li><a href="ElementSelectionDlg.html" title="class in com.nomagic.magicdraw.ui.dialogs.selection"><code>ElementSelectionDlg</code></a></li>
<li><a href="../SelectElementInfo.html" title="class in com.nomagic.magicdraw.ui.dialogs"><code>SelectElementInfo</code></a></li>
<li><a href="../../../uml/ClassTypes.html" title="class in com.nomagic.magicdraw.uml"><code>ClassTypes</code></a></li>
<li><a href="../SelectElementTypes.html" title="class in com.nomagic.magicdraw.ui.dialogs"><code>SelectElementTypes</code></a></li>
<li><a href="TypeFilter.html" title="interface in com.nomagic.magicdraw.ui.dialogs.selection"><code>TypeFilter</code></a></li>
<li><a href="TypeFilterImpl.html" title="class in com.nomagic.magicdraw.ui.dialogs.selection"><code>TypeFilterImpl</code></a></li>
<li><a href="../../../../uml2/ext/jmi/helpers/ModelHelper.html" title="class in com.nomagic.uml2.ext.jmi.helpers"><code>ModelHelper</code></a></li>
</ul>
</dd>
</dl>
</section>
<section class="summary">
<ul class="summary-list">
<!-- =========== FIELD SUMMARY =========== -->
<li>
<section class="field-summary" id="field-summary">
<h2>Field Summary</h2>
<div class="inherited-list">
<h3 id="fields-inherited-from-class-com.dassault_systemes.modeler.magic.ui.dialogs.selection.ElementSelectionDlgFactory">Fields inherited from class com.dassault_systemes.modeler.magic.ui.dialogs.selection.ElementSelectionDlgFactory</h3>
<code>HELP_PATH, SELECT_ELEMENT_TITLE, SELECT_ELEMENTS_TITLE</code></div>
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
<div class="col-constructor-name even-row-color"><code><a class="member-name-link" href="#%3Cinit%3E()">ElementSelectionDlgFactory</a>()</code></div>
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
<div class="col-first even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#collectDisplayable(java.util.Collection,java.util.Collection)">collectDisplayable</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a> displayable,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a> selectable)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Collect displayable types for a given selectable types if given displayable is null</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static <a href="ElementSelectionDlg.html" title="class in com.nomagic.magicdraw.ui.dialogs.selection">ElementSelectionDlg</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#create()">create</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Create an instance of the dialog</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static <a href="ElementSelectionDlg.html" title="class in com.nomagic.magicdraw.ui.dialogs.selection">ElementSelectionDlg</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#create(java.awt.Dialog)">create</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Dialog.html" title="class or interface in java.awt">Dialog</a> parent)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Create an instance of dialog</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static <a href="ElementSelectionDlg.html" title="class in com.nomagic.magicdraw.ui.dialogs.selection">ElementSelectionDlg</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#create(java.awt.Dialog,java.lang.String,java.lang.String)">create</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Dialog.html" title="class or interface in java.awt">Dialog</a> parent,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> title,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> helpPath)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Create an instance of dialog</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static <a href="ElementSelectionDlg.html" title="class in com.nomagic.magicdraw.ui.dialogs.selection">ElementSelectionDlg</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#create(java.awt.Frame)">create</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Frame.html" title="class or interface in java.awt">Frame</a> parent)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Create an instance of dialog</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static <a href="ElementSelectionDlg.html" title="class in com.nomagic.magicdraw.ui.dialogs.selection">ElementSelectionDlg</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#create(java.awt.Frame,com.dassault_systemes.modeler.magic.ui.selection.ElementSelectionContext)">create</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Frame.html" title="class or interface in java.awt">Frame</a> parent,
 com.dassault_systemes.modeler.magic.ui.selection.ElementSelectionContext context)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static <a href="ElementSelectionDlg.html" title="class in com.nomagic.magicdraw.ui.dialogs.selection">ElementSelectionDlg</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#create(java.awt.Frame,java.lang.String,java.lang.String)">create</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Frame.html" title="class or interface in java.awt">Frame</a> parent,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> title,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> helpPath)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Create an instance of dialog</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static <a href="ElementSelectionDlg.html" title="class in com.nomagic.magicdraw.ui.dialogs.selection">ElementSelectionDlg</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#create(java.awt.Window)">create</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Window.html" title="class or interface in java.awt">Window</a> parent)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Create an instance of dialog</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static <a href="ElementSelectionDlg.html" title="class in com.nomagic.magicdraw.ui.dialogs.selection">ElementSelectionDlg</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#create(java.awt.Window,com.dassault_systemes.modeler.magic.ui.selection.ElementSelectionContext)">create</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Window.html" title="class or interface in java.awt">Window</a> parent,
 com.dassault_systemes.modeler.magic.ui.selection.ElementSelectionContext context)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static <a href="ElementSelectionDlg.html" title="class in com.nomagic.magicdraw.ui.dialogs.selection">ElementSelectionDlg</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#create(java.awt.Window,java.lang.String,java.lang.String)">create</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Window.html" title="class or interface in java.awt">Window</a> parent,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> title,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> helpPath)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Create an instance of dialog</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static <a href="ElementSelectionDlg.html" title="class in com.nomagic.magicdraw.ui.dialogs.selection">ElementSelectionDlg</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#create(java.awt.Window,java.lang.String,java.lang.String,com.dassault_systemes.modeler.magic.ui.selection.ElementSelectionContext)">create</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Window.html" title="class or interface in java.awt">Window</a> parent,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> title,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> helpPath,
 com.dassault_systemes.modeler.magic.ui.selection.ElementSelectionContext context)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static <a href="TypeFilter.html" title="interface in com.nomagic.magicdraw.ui.dialogs.selection">TypeFilter</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#createDisplayableForSelectable(com.nomagic.magicdraw.ui.dialogs.selection.TypeFilter)">createDisplayableForSelectable</a><wbr/>(<a href="TypeFilter.html" title="interface in com.nomagic.magicdraw.ui.dialogs.selection">TypeFilter</a> selectable)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Create displayable types filter for a given selectable types filter.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static <a href="TypeFilter.html" title="interface in com.nomagic.magicdraw.ui.dialogs.selection">TypeFilter</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#createDisplayableForSelectable(java.util.Collection)">createDisplayableForSelectable</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a> selectable)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Create displayable types filter for a given selectable types.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static <a href="TypeFilter.html" title="interface in com.nomagic.magicdraw.ui.dialogs.selection">TypeFilter</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#createDisplayableForSelectable(java.util.Collection,com.nomagic.magicdraw.ui.dialogs.selection.TypeFilter)">createDisplayableForSelectable</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a> displayable,
 <a href="TypeFilter.html" title="interface in com.nomagic.magicdraw.ui.dialogs.selection">TypeFilter</a> selectable)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Create displayable types filter for a given selectable types filter if given displayable is null</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#initMultiple(com.nomagic.magicdraw.ui.dialogs.selection.ElementSelectionDlg,com.nomagic.magicdraw.ui.dialogs.SelectElementInfo,com.nomagic.magicdraw.ui.dialogs.selection.TypeFilter,com.nomagic.magicdraw.ui.dialogs.selection.TypeFilter,boolean,java.util.Collection,java.lang.Object%5B%5D)">initMultiple</a><wbr/>(<a href="ElementSelectionDlg.html" title="class in com.nomagic.magicdraw.ui.dialogs.selection">ElementSelectionDlg</a> dlg,
 <a href="../SelectElementInfo.html" title="class in com.nomagic.magicdraw.ui.dialogs">SelectElementInfo</a> info,
 <a href="TypeFilter.html" title="interface in com.nomagic.magicdraw.ui.dialogs.selection">TypeFilter</a> visibleElementsFilter,
 <a href="TypeFilter.html" title="interface in com.nomagic.magicdraw.ui.dialogs.selection">TypeFilter</a> selectableElementsFilter,
 boolean usedAsType,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;?&gt; creatableTypes,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a>[] selection)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Initializes given dialog with a "multiple elements" selection mode.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#initMultiple(com.nomagic.magicdraw.ui.dialogs.selection.ElementSelectionDlg,com.nomagic.magicdraw.ui.dialogs.SelectElementInfo,com.nomagic.magicdraw.ui.dialogs.selection.TypeFilter,com.nomagic.magicdraw.ui.dialogs.selection.TypeFilter,boolean,java.util.Collection,java.util.List)">initMultiple</a><wbr/>(<a href="ElementSelectionDlg.html" title="class in com.nomagic.magicdraw.ui.dialogs.selection">ElementSelectionDlg</a> dlg,
 <a href="../SelectElementInfo.html" title="class in com.nomagic.magicdraw.ui.dialogs">SelectElementInfo</a> info,
 <a href="TypeFilter.html" title="interface in com.nomagic.magicdraw.ui.dialogs.selection">TypeFilter</a> visibleElementsFilter,
 <a href="TypeFilter.html" title="interface in com.nomagic.magicdraw.ui.dialogs.selection">TypeFilter</a> selectableElementsFilter,
 boolean usedAsType,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;?&gt; creatableTypes,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;?&gt; selection)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Initializes given dialog with a "multiple elements" selection mode.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#initMultiple(com.nomagic.magicdraw.ui.dialogs.selection.ElementSelectionDlg,com.nomagic.magicdraw.ui.dialogs.SelectElementInfo,com.nomagic.magicdraw.ui.dialogs.selection.TypeFilter,com.nomagic.magicdraw.ui.dialogs.selection.TypeFilter,java.util.Collection,java.lang.Object%5B%5D)">initMultiple</a><wbr/>(<a href="ElementSelectionDlg.html" title="class in com.nomagic.magicdraw.ui.dialogs.selection">ElementSelectionDlg</a> dlg,
 <a href="../SelectElementInfo.html" title="class in com.nomagic.magicdraw.ui.dialogs">SelectElementInfo</a> info,
 <a href="TypeFilter.html" title="interface in com.nomagic.magicdraw.ui.dialogs.selection">TypeFilter</a> visibleElementsFilter,
 <a href="TypeFilter.html" title="interface in com.nomagic.magicdraw.ui.dialogs.selection">TypeFilter</a> selectableElementsFilter,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;?&gt; creatableTypes,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a>[] selection)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Initializes given dialog with a "multiple elements" selection mode.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#initMultiple(com.nomagic.magicdraw.ui.dialogs.selection.ElementSelectionDlg,com.nomagic.magicdraw.ui.dialogs.SelectElementInfo,com.nomagic.magicdraw.ui.dialogs.selection.TypeFilter,com.nomagic.magicdraw.ui.dialogs.selection.TypeFilter,java.util.Collection,java.util.List)">initMultiple</a><wbr/>(<a href="ElementSelectionDlg.html" title="class in com.nomagic.magicdraw.ui.dialogs.selection">ElementSelectionDlg</a> dlg,
 <a href="../SelectElementInfo.html" title="class in com.nomagic.magicdraw.ui.dialogs">SelectElementInfo</a> info,
 <a href="TypeFilter.html" title="interface in com.nomagic.magicdraw.ui.dialogs.selection">TypeFilter</a> visibleElementsFilter,
 <a href="TypeFilter.html" title="interface in com.nomagic.magicdraw.ui.dialogs.selection">TypeFilter</a> selectableElementsFilter,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;?&gt; creatableTypes,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;?&gt; selection)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Initializes given dialog with a "multiple elements" selection mode.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#initMultiple(com.nomagic.magicdraw.ui.dialogs.selection.ElementSelectionDlg,com.nomagic.magicdraw.ui.dialogs.SelectElementTypes,com.nomagic.magicdraw.ui.dialogs.SelectElementInfo,java.lang.Object%5B%5D)">initMultiple</a><wbr/>(<a href="ElementSelectionDlg.html" title="class in com.nomagic.magicdraw.ui.dialogs.selection">ElementSelectionDlg</a> dlg,
 <a href="../SelectElementTypes.html" title="class in com.nomagic.magicdraw.ui.dialogs">SelectElementTypes</a> types,
 <a href="../SelectElementInfo.html" title="class in com.nomagic.magicdraw.ui.dialogs">SelectElementInfo</a> info,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a>[] selection)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Initializes given dialog with a "multiple elements" selection mode.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#initMultiple(com.nomagic.magicdraw.ui.dialogs.selection.ElementSelectionDlg,com.nomagic.magicdraw.ui.dialogs.SelectElementTypes,com.nomagic.magicdraw.ui.dialogs.SelectElementInfo,java.util.List)">initMultiple</a><wbr/>(<a href="ElementSelectionDlg.html" title="class in com.nomagic.magicdraw.ui.dialogs.selection">ElementSelectionDlg</a> dlg,
 <a href="../SelectElementTypes.html" title="class in com.nomagic.magicdraw.ui.dialogs">SelectElementTypes</a> types,
 <a href="../SelectElementInfo.html" title="class in com.nomagic.magicdraw.ui.dialogs">SelectElementInfo</a> info,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a> selection)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Initializes given dialog with a "multiple elements" selection mode.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#initMultipleAsMultipleInitial(com.nomagic.magicdraw.ui.dialogs.selection.ElementSelectionDlg,com.nomagic.magicdraw.ui.dialogs.SelectElementInfo,com.nomagic.magicdraw.ui.dialogs.selection.TypeFilter,com.nomagic.magicdraw.ui.dialogs.selection.TypeFilter,java.util.Collection,java.util.List)">initMultipleAsMultipleInitial</a><wbr/>(<a href="ElementSelectionDlg.html" title="class in com.nomagic.magicdraw.ui.dialogs.selection">ElementSelectionDlg</a> dlg,
 <a href="../SelectElementInfo.html" title="class in com.nomagic.magicdraw.ui.dialogs">SelectElementInfo</a> info,
 <a href="TypeFilter.html" title="interface in com.nomagic.magicdraw.ui.dialogs.selection">TypeFilter</a> visibleElementsFilter,
 <a href="TypeFilter.html" title="interface in com.nomagic.magicdraw.ui.dialogs.selection">TypeFilter</a> selectableElementsFilter,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;?&gt; creatableTypes,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;?&gt; selection)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Initializes given dialog with a "multiple elements" selection mode.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#initSingle(com.nomagic.magicdraw.ui.dialogs.selection.ElementSelectionDlg,com.nomagic.magicdraw.ui.dialogs.SelectElementInfo,com.nomagic.magicdraw.ui.dialogs.selection.TypeFilter,com.nomagic.magicdraw.ui.dialogs.selection.TypeFilter,boolean,java.util.Collection,java.lang.Object)">initSingle</a><wbr/>(<a href="ElementSelectionDlg.html" title="class in com.nomagic.magicdraw.ui.dialogs.selection">ElementSelectionDlg</a> dlg,
 <a href="../SelectElementInfo.html" title="class in com.nomagic.magicdraw.ui.dialogs">SelectElementInfo</a> info,
 <a href="TypeFilter.html" title="interface in com.nomagic.magicdraw.ui.dialogs.selection">TypeFilter</a> visibleElementsFilter,
 <a href="TypeFilter.html" title="interface in com.nomagic.magicdraw.ui.dialogs.selection">TypeFilter</a> selectableElementsFilter,
 boolean usedAsType,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;?&gt; creatableTypes,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a> selection)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Initializes given dialog with a "single element" selection mode.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#initSingle(com.nomagic.magicdraw.ui.dialogs.selection.ElementSelectionDlg,com.nomagic.magicdraw.ui.dialogs.SelectElementInfo,com.nomagic.magicdraw.ui.dialogs.selection.TypeFilter,com.nomagic.magicdraw.ui.dialogs.selection.TypeFilter,java.util.Collection,java.lang.Object)">initSingle</a><wbr/>(<a href="ElementSelectionDlg.html" title="class in com.nomagic.magicdraw.ui.dialogs.selection">ElementSelectionDlg</a> dlg,
 <a href="../SelectElementInfo.html" title="class in com.nomagic.magicdraw.ui.dialogs">SelectElementInfo</a> info,
 <a href="TypeFilter.html" title="interface in com.nomagic.magicdraw.ui.dialogs.selection">TypeFilter</a> visibleElementsFilter,
 <a href="TypeFilter.html" title="interface in com.nomagic.magicdraw.ui.dialogs.selection">TypeFilter</a> selectableElementsFilter,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;?&gt; creatableTypes,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a> selection)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Initializes given dialog with a "single element" selection mode.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#initSingle(com.nomagic.magicdraw.ui.dialogs.selection.ElementSelectionDlg,com.nomagic.magicdraw.ui.dialogs.SelectElementTypes,com.nomagic.magicdraw.ui.dialogs.SelectElementInfo,java.lang.Object)">initSingle</a><wbr/>(<a href="ElementSelectionDlg.html" title="class in com.nomagic.magicdraw.ui.dialogs.selection">ElementSelectionDlg</a> dlg,
 <a href="../SelectElementTypes.html" title="class in com.nomagic.magicdraw.ui.dialogs">SelectElementTypes</a> types,
 <a href="../SelectElementInfo.html" title="class in com.nomagic.magicdraw.ui.dialogs">SelectElementInfo</a> info,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a> selection)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Initializes given dialog with a "single element" selection mode.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static <a href="TypeFilter.html" title="interface in com.nomagic.magicdraw.ui.dialogs.selection">TypeFilter</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#wrapWithTagsFilter(com.nomagic.magicdraw.ui.dialogs.selection.TypeFilter)">wrapWithTagsFilter</a><wbr/>(<a href="TypeFilter.html" title="interface in com.nomagic.magicdraw.ui.dialogs.selection">TypeFilter</a> inner)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Creates tags filter from given type filter.</div>
</div>
</div>
</div>
</div>
<div class="inherited-list">
<h3 id="methods-inherited-from-class-com.dassault_systemes.modeler.magic.ui.dialogs.selection.ElementSelectionDlgFactory">Methods inherited from class com.dassault_systemes.modeler.magic.ui.dialogs.selection.ElementSelectionDlgFactory</h3>
<code>addExternalFactory, create, setSelectionMode</code></div>
<div class="inherited-list">
<h3 id="methods-inherited-from-class-java.lang.Object">Methods inherited from class java.lang.<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a></h3>
<code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#clone()" title="class or interface in java.lang">clone</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#equals(java.lang.Object)" title="class or interface in java.lang">equals</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#finalize()" title="class or interface in java.lang">finalize</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#getClass()" title="class or interface in java.lang">getClass</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#hashCode()" title="class or interface in java.lang">hashCode</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notify()" title="class or interface in java.lang">notify</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notifyAll()" title="class or interface in java.lang">notifyAll</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#toString()" title="class or interface in java.lang">toString</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait()" title="class or interface in java.lang">wait</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long)" title="class or interface in java.lang">wait</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long,int)" title="class or interface in java.lang">wait</a></code></div>
</section>
</li>
</ul>
</section>
<section class="details">
<ul class="details-list">
<!-- ========= CONSTRUCTOR DETAIL ======== -->
<li>
<section class="constructor-details" id="constructor-detail">
<h2>Constructor Details</h2>
<ul class="member-list">
<li>
<section class="detail" id="&lt;init&gt;()">
<h3>ElementSelectionDlgFactory</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="element-name">ElementSelectionDlgFactory</span>()</div>
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
<section class="detail" id="create()">
<h3>create</h3>
<div class="member-signature"><span class="annotations">@OpenApi
</span><span class="modifiers">public static</span> <span class="return-type"><a href="ElementSelectionDlg.html" title="class in com.nomagic.magicdraw.ui.dialogs.selection">ElementSelectionDlg</a></span> <span class="element-name">create</span>()</div>
<div class="block">Create an instance of the dialog</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>dialog instance</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="create(java.awt.Frame)">
<h3>create</h3>
<div class="member-signature"><span class="annotations">@OpenApi
</span><span class="modifiers">public static</span> <span class="return-type"><a href="ElementSelectionDlg.html" title="class in com.nomagic.magicdraw.ui.dialogs.selection">ElementSelectionDlg</a></span> <span class="element-name">create</span><wbr/><span class="parameters">(@CheckForNull
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Frame.html" title="class or interface in java.awt">Frame</a> parent)</span></div>
<div class="block">Create an instance of dialog</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>parent</code> - dialog parent</dd>
<dt>Returns:</dt>
<dd>dialog instance</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="create(java.awt.Frame,com.dassault_systemes.modeler.magic.ui.selection.ElementSelectionContext)">
<h3>create</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type"><a href="ElementSelectionDlg.html" title="class in com.nomagic.magicdraw.ui.dialogs.selection">ElementSelectionDlg</a></span> <span class="element-name">create</span><wbr/><span class="parameters">(@CheckForNull
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Frame.html" title="class or interface in java.awt">Frame</a> parent,
 @CheckForNull
 com.dassault_systemes.modeler.magic.ui.selection.ElementSelectionContext context)</span></div>
</section>
</li>
<li>
<section class="detail" id="create(java.awt.Frame,java.lang.String,java.lang.String)">
<h3>create</h3>
<div class="member-signature"><span class="annotations">@OpenApi
</span><span class="modifiers">public static</span> <span class="return-type"><a href="ElementSelectionDlg.html" title="class in com.nomagic.magicdraw.ui.dialogs.selection">ElementSelectionDlg</a></span> <span class="element-name">create</span><wbr/><span class="parameters">(@CheckForNull
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Frame.html" title="class or interface in java.awt">Frame</a> parent,
 @CheckForNull
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> title,
 @CheckForNull
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> helpPath)</span></div>
<div class="block">Create an instance of dialog</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>parent</code> - dialog parent</dd>
<dd><code>title</code> - dialog title</dd>
<dd><code>helpPath</code> - help id</dd>
<dt>Returns:</dt>
<dd>dialog instance</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="create(java.awt.Window)">
<h3>create</h3>
<div class="member-signature"><span class="annotations">@OpenApi
</span><span class="modifiers">public static</span> <span class="return-type"><a href="ElementSelectionDlg.html" title="class in com.nomagic.magicdraw.ui.dialogs.selection">ElementSelectionDlg</a></span> <span class="element-name">create</span><wbr/><span class="parameters">(@CheckForNull
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Window.html" title="class or interface in java.awt">Window</a> parent)</span></div>
<div class="block">Create an instance of dialog</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>parent</code> - dialog parent</dd>
<dt>Returns:</dt>
<dd>dialog instance</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="create(java.awt.Window,com.dassault_systemes.modeler.magic.ui.selection.ElementSelectionContext)">
<h3>create</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type"><a href="ElementSelectionDlg.html" title="class in com.nomagic.magicdraw.ui.dialogs.selection">ElementSelectionDlg</a></span> <span class="element-name">create</span><wbr/><span class="parameters">(@CheckForNull
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Window.html" title="class or interface in java.awt">Window</a> parent,
 @CheckForNull
 com.dassault_systemes.modeler.magic.ui.selection.ElementSelectionContext context)</span></div>
</section>
</li>
<li>
<section class="detail" id="create(java.awt.Window,java.lang.String,java.lang.String)">
<h3>create</h3>
<div class="member-signature"><span class="annotations">@OpenApi
</span><span class="modifiers">public static</span> <span class="return-type"><a href="ElementSelectionDlg.html" title="class in com.nomagic.magicdraw.ui.dialogs.selection">ElementSelectionDlg</a></span> <span class="element-name">create</span><wbr/><span class="parameters">(@CheckForNull
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Window.html" title="class or interface in java.awt">Window</a> parent,
 @CheckForNull
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> title,
 @CheckForNull
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> helpPath)</span></div>
<div class="block">Create an instance of dialog</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>parent</code> - dialog parent</dd>
<dd><code>title</code> - dialog title</dd>
<dd><code>helpPath</code> - help id</dd>
<dt>Returns:</dt>
<dd>dialog instance</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="create(java.awt.Window,java.lang.String,java.lang.String,com.dassault_systemes.modeler.magic.ui.selection.ElementSelectionContext)">
<h3>create</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type"><a href="ElementSelectionDlg.html" title="class in com.nomagic.magicdraw.ui.dialogs.selection">ElementSelectionDlg</a></span> <span class="element-name">create</span><wbr/><span class="parameters">(@CheckForNull
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Window.html" title="class or interface in java.awt">Window</a> parent,
 @CheckForNull
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> title,
 @CheckForNull
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> helpPath,
 @CheckForNull
 com.dassault_systemes.modeler.magic.ui.selection.ElementSelectionContext context)</span></div>
</section>
</li>
<li>
<section class="detail" id="create(java.awt.Dialog)">
<h3>create</h3>
<div class="member-signature"><span class="annotations">@OpenApi
</span><span class="modifiers">public static</span> <span class="return-type"><a href="ElementSelectionDlg.html" title="class in com.nomagic.magicdraw.ui.dialogs.selection">ElementSelectionDlg</a></span> <span class="element-name">create</span><wbr/><span class="parameters">(@CheckForNull
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Dialog.html" title="class or interface in java.awt">Dialog</a> parent)</span></div>
<div class="block">Create an instance of dialog</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>parent</code> - dialog parent</dd>
<dt>Returns:</dt>
<dd>dialog instance</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="create(java.awt.Dialog,java.lang.String,java.lang.String)">
<h3>create</h3>
<div class="member-signature"><span class="annotations">@OpenApi
</span><span class="modifiers">public static</span> <span class="return-type"><a href="ElementSelectionDlg.html" title="class in com.nomagic.magicdraw.ui.dialogs.selection">ElementSelectionDlg</a></span> <span class="element-name">create</span><wbr/><span class="parameters">(@CheckForNull
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Dialog.html" title="class or interface in java.awt">Dialog</a> parent,
 @CheckForNull
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> title,
 @CheckForNull
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> helpPath)</span></div>
<div class="block">Create an instance of dialog</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>parent</code> - dialog parent</dd>
<dd><code>title</code> - dialog title</dd>
<dd><code>helpPath</code> - help id</dd>
<dt>Returns:</dt>
<dd>dialog instance</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="collectDisplayable(java.util.Collection,java.util.Collection)">
<h3>collectDisplayable</h3>
<div class="member-signature"><span class="annotations">@OpenApi
</span><span class="modifiers">public static</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a></span> <span class="element-name">collectDisplayable</span><wbr/><span class="parameters">(@CheckForNull
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a> displayable,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a> selectable)</span></div>
<div class="block">Collect displayable types for a given selectable types if given displayable is null</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>displayable</code> - displayable types</dd>
<dd><code>selectable</code> - selectable types</dd>
<dt>Returns:</dt>
<dd>displayable types</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="createDisplayableForSelectable(java.util.Collection,com.nomagic.magicdraw.ui.dialogs.selection.TypeFilter)">
<h3>createDisplayableForSelectable</h3>
<div class="member-signature"><span class="annotations">@OpenApi
</span><span class="modifiers">public static</span> <span class="return-type"><a href="TypeFilter.html" title="interface in com.nomagic.magicdraw.ui.dialogs.selection">TypeFilter</a></span> <span class="element-name">createDisplayableForSelectable</span><wbr/><span class="parameters">(@CheckForNull
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a> displayable,
 <a href="TypeFilter.html" title="interface in com.nomagic.magicdraw.ui.dialogs.selection">TypeFilter</a> selectable)</span></div>
<div class="block">Create displayable types filter for a given selectable types filter if given displayable is null</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>displayable</code> - displayable types</dd>
<dd><code>selectable</code> - selectable types</dd>
<dt>Returns:</dt>
<dd>displayable types</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="createDisplayableForSelectable(com.nomagic.magicdraw.ui.dialogs.selection.TypeFilter)">
<h3>createDisplayableForSelectable</h3>
<div class="member-signature"><span class="annotations">@OpenApi
</span><span class="modifiers">public static</span> <span class="return-type"><a href="TypeFilter.html" title="interface in com.nomagic.magicdraw.ui.dialogs.selection">TypeFilter</a></span> <span class="element-name">createDisplayableForSelectable</span><wbr/><span class="parameters">(<a href="TypeFilter.html" title="interface in com.nomagic.magicdraw.ui.dialogs.selection">TypeFilter</a> selectable)</span></div>
<div class="block">Create displayable types filter for a given selectable types filter.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>selectable</code> - selectable types</dd>
<dt>Returns:</dt>
<dd>displayable types</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="createDisplayableForSelectable(java.util.Collection)">
<h3>createDisplayableForSelectable</h3>
<div class="member-signature"><span class="annotations">@OpenApi
</span><span class="modifiers">public static</span> <span class="return-type"><a href="TypeFilter.html" title="interface in com.nomagic.magicdraw.ui.dialogs.selection">TypeFilter</a></span> <span class="element-name">createDisplayableForSelectable</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a> selectable)</span></div>
<div class="block">Create displayable types filter for a given selectable types.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>selectable</code> - selectable types</dd>
<dt>Returns:</dt>
<dd>displayable types</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="initSingle(com.nomagic.magicdraw.ui.dialogs.selection.ElementSelectionDlg,com.nomagic.magicdraw.ui.dialogs.SelectElementTypes,com.nomagic.magicdraw.ui.dialogs.SelectElementInfo,java.lang.Object)">
<h3>initSingle</h3>
<div class="member-signature"><span class="annotations">@OpenApi
</span><span class="modifiers">public static</span> <span class="return-type">void</span> <span class="element-name">initSingle</span><wbr/><span class="parameters">(<a href="ElementSelectionDlg.html" title="class in com.nomagic.magicdraw.ui.dialogs.selection">ElementSelectionDlg</a> dlg,
 <a href="../SelectElementTypes.html" title="class in com.nomagic.magicdraw.ui.dialogs">SelectElementTypes</a> types,
 <a href="../SelectElementInfo.html" title="class in com.nomagic.magicdraw.ui.dialogs">SelectElementInfo</a> info,
 @CheckForNull
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a> selection)</span></div>
<div class="block">Initializes given dialog with a "single element" selection mode. It means dialog will allow to select
 just a single element.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>dlg</code> - dialog</dd>
<dd><code>types</code> - element selection information</dd>
<dd><code>info</code> - dialog settings</dd>
<dd><code>selection</code> - initially selected element</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="initMultiple(com.nomagic.magicdraw.ui.dialogs.selection.ElementSelectionDlg,com.nomagic.magicdraw.ui.dialogs.SelectElementTypes,com.nomagic.magicdraw.ui.dialogs.SelectElementInfo,java.lang.Object[])">
<h3>initMultiple</h3>
<div class="member-signature"><span class="annotations">@OpenApi
</span><span class="modifiers">public static</span> <span class="return-type">void</span> <span class="element-name">initMultiple</span><wbr/><span class="parameters">(<a href="ElementSelectionDlg.html" title="class in com.nomagic.magicdraw.ui.dialogs.selection">ElementSelectionDlg</a> dlg,
 <a href="../SelectElementTypes.html" title="class in com.nomagic.magicdraw.ui.dialogs">SelectElementTypes</a> types,
 <a href="../SelectElementInfo.html" title="class in com.nomagic.magicdraw.ui.dialogs">SelectElementInfo</a> info,
 @CheckForNull
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a>[] selection)</span></div>
<div class="block">Initializes given dialog with a "multiple elements" selection mode. It means dialog will allow to select
 several elements.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>dlg</code> - dialog</dd>
<dd><code>types</code> - element selection information</dd>
<dd><code>info</code> - dialog settings</dd>
<dd><code>selection</code> - initially selected elements</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="initMultiple(com.nomagic.magicdraw.ui.dialogs.selection.ElementSelectionDlg,com.nomagic.magicdraw.ui.dialogs.SelectElementTypes,com.nomagic.magicdraw.ui.dialogs.SelectElementInfo,java.util.List)">
<h3>initMultiple</h3>
<div class="member-signature"><span class="annotations">@OpenApi
</span><span class="modifiers">public static</span> <span class="return-type">void</span> <span class="element-name">initMultiple</span><wbr/><span class="parameters">(<a href="ElementSelectionDlg.html" title="class in com.nomagic.magicdraw.ui.dialogs.selection">ElementSelectionDlg</a> dlg,
 <a href="../SelectElementTypes.html" title="class in com.nomagic.magicdraw.ui.dialogs">SelectElementTypes</a> types,
 <a href="../SelectElementInfo.html" title="class in com.nomagic.magicdraw.ui.dialogs">SelectElementInfo</a> info,
 @CheckForNull
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a> selection)</span></div>
<div class="block">Initializes given dialog with a "multiple elements" selection mode. It means dialog will allow to select
 several elements.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>dlg</code> - dialog</dd>
<dd><code>types</code> - element selection information</dd>
<dd><code>info</code> - dialog settings</dd>
<dd><code>selection</code> - initially selected elements</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="initSingle(com.nomagic.magicdraw.ui.dialogs.selection.ElementSelectionDlg,com.nomagic.magicdraw.ui.dialogs.SelectElementInfo,com.nomagic.magicdraw.ui.dialogs.selection.TypeFilter,com.nomagic.magicdraw.ui.dialogs.selection.TypeFilter,java.util.Collection,java.lang.Object)">
<h3>initSingle</h3>
<div class="member-signature"><span class="annotations">@OpenApi
</span><span class="modifiers">public static</span> <span class="return-type">void</span> <span class="element-name">initSingle</span><wbr/><span class="parameters">(<a href="ElementSelectionDlg.html" title="class in com.nomagic.magicdraw.ui.dialogs.selection">ElementSelectionDlg</a> dlg,
 <a href="../SelectElementInfo.html" title="class in com.nomagic.magicdraw.ui.dialogs">SelectElementInfo</a> info,
 <a href="TypeFilter.html" title="interface in com.nomagic.magicdraw.ui.dialogs.selection">TypeFilter</a> visibleElementsFilter,
 <a href="TypeFilter.html" title="interface in com.nomagic.magicdraw.ui.dialogs.selection">TypeFilter</a> selectableElementsFilter,
 @CheckForNull
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;?&gt; creatableTypes,
 @CheckForNull
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a> selection)</span></div>
<div class="block">Initializes given dialog with a "single element" selection mode. It means dialog will allow to select
 just a single element.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>dlg</code> - dialog</dd>
<dd><code>info</code> - dialog settings</dd>
<dd><code>visibleElementsFilter</code> - filter providing visible elements in the dialog</dd>
<dd><code>selectableElementsFilter</code> - filter providing selectable elements in the dialog</dd>
<dd><code>creatableTypes</code> - collection of creatable types (choice on Create button)</dd>
<dd><code>selection</code> - initially selected element</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="initSingle(com.nomagic.magicdraw.ui.dialogs.selection.ElementSelectionDlg,com.nomagic.magicdraw.ui.dialogs.SelectElementInfo,com.nomagic.magicdraw.ui.dialogs.selection.TypeFilter,com.nomagic.magicdraw.ui.dialogs.selection.TypeFilter,boolean,java.util.Collection,java.lang.Object)">
<h3>initSingle</h3>
<div class="member-signature"><span class="annotations">@OpenApi
</span><span class="modifiers">public static</span> <span class="return-type">void</span> <span class="element-name">initSingle</span><wbr/><span class="parameters">(<a href="ElementSelectionDlg.html" title="class in com.nomagic.magicdraw.ui.dialogs.selection">ElementSelectionDlg</a> dlg,
 <a href="../SelectElementInfo.html" title="class in com.nomagic.magicdraw.ui.dialogs">SelectElementInfo</a> info,
 <a href="TypeFilter.html" title="interface in com.nomagic.magicdraw.ui.dialogs.selection">TypeFilter</a> visibleElementsFilter,
 <a href="TypeFilter.html" title="interface in com.nomagic.magicdraw.ui.dialogs.selection">TypeFilter</a> selectableElementsFilter,
 boolean usedAsType,
 @CheckForNull
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;?&gt; creatableTypes,
 @CheckForNull
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a> selection)</span></div>
<div class="block">Initializes given dialog with a "single element" selection mode. It means dialog will allow to select
 just a single element.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>dlg</code> - dialog</dd>
<dd><code>info</code> - dialog settings</dd>
<dd><code>visibleElementsFilter</code> - filter providing visible elements in the dialog</dd>
<dd><code>selectableElementsFilter</code> - filter providing selectable elements in the dialog</dd>
<dd><code>usedAsType</code> - is this dialog instance is used to select some UML Type. If true, some special filters
                                 from DSL will be used for elements filtering</dd>
<dd><code>creatableTypes</code> - collection of creatable types (choice on Create button)</dd>
<dd><code>selection</code> - initially selected element</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="initMultiple(com.nomagic.magicdraw.ui.dialogs.selection.ElementSelectionDlg,com.nomagic.magicdraw.ui.dialogs.SelectElementInfo,com.nomagic.magicdraw.ui.dialogs.selection.TypeFilter,com.nomagic.magicdraw.ui.dialogs.selection.TypeFilter,boolean,java.util.Collection,java.lang.Object[])">
<h3>initMultiple</h3>
<div class="member-signature"><span class="annotations">@OpenApi
</span><span class="modifiers">public static</span> <span class="return-type">void</span> <span class="element-name">initMultiple</span><wbr/><span class="parameters">(<a href="ElementSelectionDlg.html" title="class in com.nomagic.magicdraw.ui.dialogs.selection">ElementSelectionDlg</a> dlg,
 <a href="../SelectElementInfo.html" title="class in com.nomagic.magicdraw.ui.dialogs">SelectElementInfo</a> info,
 <a href="TypeFilter.html" title="interface in com.nomagic.magicdraw.ui.dialogs.selection">TypeFilter</a> visibleElementsFilter,
 <a href="TypeFilter.html" title="interface in com.nomagic.magicdraw.ui.dialogs.selection">TypeFilter</a> selectableElementsFilter,
 boolean usedAsType,
 @CheckForNull
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;?&gt; creatableTypes,
 @CheckForNull
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a>[] selection)</span></div>
<div class="block">Initializes given dialog with a "multiple elements" selection mode. It means dialog will allow to select
 several elements.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>dlg</code> - dialog</dd>
<dd><code>info</code> - dialog settings</dd>
<dd><code>visibleElementsFilter</code> - filter providing visible elements in the dialog</dd>
<dd><code>selectableElementsFilter</code> - filter providing selectable elements in the dialog</dd>
<dd><code>usedAsType</code> - is this dialog instance is used to select some UML Type. If true, some special filters
                                 from DSL will be used for elements filtering</dd>
<dd><code>creatableTypes</code> - collection of creatable types (choice on Create button)</dd>
<dd><code>selection</code> - initially selected element</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="initMultiple(com.nomagic.magicdraw.ui.dialogs.selection.ElementSelectionDlg,com.nomagic.magicdraw.ui.dialogs.SelectElementInfo,com.nomagic.magicdraw.ui.dialogs.selection.TypeFilter,com.nomagic.magicdraw.ui.dialogs.selection.TypeFilter,java.util.Collection,java.lang.Object[])">
<h3>initMultiple</h3>
<div class="member-signature"><span class="annotations">@OpenApi
</span><span class="modifiers">public static</span> <span class="return-type">void</span> <span class="element-name">initMultiple</span><wbr/><span class="parameters">(<a href="ElementSelectionDlg.html" title="class in com.nomagic.magicdraw.ui.dialogs.selection">ElementSelectionDlg</a> dlg,
 <a href="../SelectElementInfo.html" title="class in com.nomagic.magicdraw.ui.dialogs">SelectElementInfo</a> info,
 <a href="TypeFilter.html" title="interface in com.nomagic.magicdraw.ui.dialogs.selection">TypeFilter</a> visibleElementsFilter,
 <a href="TypeFilter.html" title="interface in com.nomagic.magicdraw.ui.dialogs.selection">TypeFilter</a> selectableElementsFilter,
 @CheckForNull
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;?&gt; creatableTypes,
 @CheckForNull
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a>[] selection)</span></div>
<div class="block">Initializes given dialog with a "multiple elements" selection mode. It means dialog will allow to select
 several elements.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>dlg</code> - dialog</dd>
<dd><code>info</code> - dialog settings</dd>
<dd><code>visibleElementsFilter</code> - filter providing visible elements in the dialog</dd>
<dd><code>selectableElementsFilter</code> - filter providing selectable elements in the dialog</dd>
<dd><code>creatableTypes</code> - collection of creatable types (choice on Create button)</dd>
<dd><code>selection</code> - initially selected element</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="initMultiple(com.nomagic.magicdraw.ui.dialogs.selection.ElementSelectionDlg,com.nomagic.magicdraw.ui.dialogs.SelectElementInfo,com.nomagic.magicdraw.ui.dialogs.selection.TypeFilter,com.nomagic.magicdraw.ui.dialogs.selection.TypeFilter,java.util.Collection,java.util.List)">
<h3>initMultiple</h3>
<div class="member-signature"><span class="annotations">@OpenApi
</span><span class="modifiers">public static</span> <span class="return-type">void</span> <span class="element-name">initMultiple</span><wbr/><span class="parameters">(<a href="ElementSelectionDlg.html" title="class in com.nomagic.magicdraw.ui.dialogs.selection">ElementSelectionDlg</a> dlg,
 <a href="../SelectElementInfo.html" title="class in com.nomagic.magicdraw.ui.dialogs">SelectElementInfo</a> info,
 <a href="TypeFilter.html" title="interface in com.nomagic.magicdraw.ui.dialogs.selection">TypeFilter</a> visibleElementsFilter,
 <a href="TypeFilter.html" title="interface in com.nomagic.magicdraw.ui.dialogs.selection">TypeFilter</a> selectableElementsFilter,
 @CheckForNull
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;?&gt; creatableTypes,
 @CheckForNull
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;?&gt; selection)</span></div>
<div class="block">Initializes given dialog with a "multiple elements" selection mode. It means dialog will allow to select
 several elements.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>dlg</code> - dialog</dd>
<dd><code>info</code> - dialog settings</dd>
<dd><code>visibleElementsFilter</code> - filter providing visible elements in the dialog</dd>
<dd><code>selectableElementsFilter</code> - filter providing selectable elements in the dialog</dd>
<dd><code>creatableTypes</code> - collection of creatable types (choice on Create button)</dd>
<dd><code>selection</code> - initially selected element</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="initMultiple(com.nomagic.magicdraw.ui.dialogs.selection.ElementSelectionDlg,com.nomagic.magicdraw.ui.dialogs.SelectElementInfo,com.nomagic.magicdraw.ui.dialogs.selection.TypeFilter,com.nomagic.magicdraw.ui.dialogs.selection.TypeFilter,boolean,java.util.Collection,java.util.List)">
<h3>initMultiple</h3>
<div class="member-signature"><span class="annotations">@OpenApi
</span><span class="modifiers">public static</span> <span class="return-type">void</span> <span class="element-name">initMultiple</span><wbr/><span class="parameters">(<a href="ElementSelectionDlg.html" title="class in com.nomagic.magicdraw.ui.dialogs.selection">ElementSelectionDlg</a> dlg,
 <a href="../SelectElementInfo.html" title="class in com.nomagic.magicdraw.ui.dialogs">SelectElementInfo</a> info,
 <a href="TypeFilter.html" title="interface in com.nomagic.magicdraw.ui.dialogs.selection">TypeFilter</a> visibleElementsFilter,
 <a href="TypeFilter.html" title="interface in com.nomagic.magicdraw.ui.dialogs.selection">TypeFilter</a> selectableElementsFilter,
 boolean usedAsType,
 @CheckForNull
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;?&gt; creatableTypes,
 @CheckForNull
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;?&gt; selection)</span></div>
<div class="block">Initializes given dialog with a "multiple elements" selection mode. It means dialog will allow to select
 several elements.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>dlg</code> - dialog</dd>
<dd><code>info</code> - dialog settings</dd>
<dd><code>visibleElementsFilter</code> - filter providing visible elements in the dialog</dd>
<dd><code>selectableElementsFilter</code> - filter providing selectable elements in the dialog</dd>
<dd><code>usedAsType</code> - is this dialog instance is used to select some UML Type. If true, some special filters
                                 from DSL will be used for elements filtering</dd>
<dd><code>creatableTypes</code> - collection of creatable types (choice on Create button)</dd>
<dd><code>selection</code> - initially selected element</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="initMultipleAsMultipleInitial(com.nomagic.magicdraw.ui.dialogs.selection.ElementSelectionDlg,com.nomagic.magicdraw.ui.dialogs.SelectElementInfo,com.nomagic.magicdraw.ui.dialogs.selection.TypeFilter,com.nomagic.magicdraw.ui.dialogs.selection.TypeFilter,java.util.Collection,java.util.List)">
<h3>initMultipleAsMultipleInitial</h3>
<div class="member-signature"><span class="annotations">@OpenApi
</span><span class="modifiers">public static</span> <span class="return-type">void</span> <span class="element-name">initMultipleAsMultipleInitial</span><wbr/><span class="parameters">(<a href="ElementSelectionDlg.html" title="class in com.nomagic.magicdraw.ui.dialogs.selection">ElementSelectionDlg</a> dlg,
 <a href="../SelectElementInfo.html" title="class in com.nomagic.magicdraw.ui.dialogs">SelectElementInfo</a> info,
 <a href="TypeFilter.html" title="interface in com.nomagic.magicdraw.ui.dialogs.selection">TypeFilter</a> visibleElementsFilter,
 <a href="TypeFilter.html" title="interface in com.nomagic.magicdraw.ui.dialogs.selection">TypeFilter</a> selectableElementsFilter,
 @CheckForNull
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;?&gt; creatableTypes,
 @CheckForNull
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;?&gt; selection)</span></div>
<div class="block">Initializes given dialog with a "multiple elements" selection mode. It means dialog will allow to select
 several elements.
 Allows to set Multiple as mode initial multiple, (All initMultiple only use SINGLE_INITIAL)</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>dlg</code> - dialog</dd>
<dd><code>info</code> - dialog settings</dd>
<dd><code>visibleElementsFilter</code> - filter providing visible elements in the dialog</dd>
<dd><code>selectableElementsFilter</code> - filter providing selectable elements in the dialog</dd>
<dd><code>creatableTypes</code> - collection of creatable types (choice on Create button)</dd>
<dd><code>selection</code> - initially selected element</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="wrapWithTagsFilter(com.nomagic.magicdraw.ui.dialogs.selection.TypeFilter)">
<h3>wrapWithTagsFilter</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type"><a href="TypeFilter.html" title="interface in com.nomagic.magicdraw.ui.dialogs.selection">TypeFilter</a></span> <span class="element-name">wrapWithTagsFilter</span><wbr/><span class="parameters">(<a href="TypeFilter.html" title="interface in com.nomagic.magicdraw.ui.dialogs.selection">TypeFilter</a> inner)</span></div>
<div class="block">Creates tags filter from given type filter. Tags filter in some cases are much faster than
 simple filter.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>inner</code> - type filter.</dd>
<dt>Returns:</dt>
<dd>created tags filter, or passed filter if it is already is tags filter.</dd>
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
