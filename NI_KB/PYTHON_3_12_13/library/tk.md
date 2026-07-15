# PYTHON_3_12_13::library/tk.md

<!--SYSTEM_CORPUS id=PYTHON_3_12_13 source_path=library/tk.txt -->
- source: https://docs.python.org/3.12/
- archive_sha256: 48e950ab70335f2f49bd0418eaa26ab225942cd9c100e15428dc4f70f21b6ba0
- license: Python Software Foundation License Version 2; documentation examples additionally Zero Clause BSD
- fidelity: full-official-plain-text-document

Graphical User Interfaces with Tk
*********************************

Tk/Tcl has long been an integral part of Python.  It provides a robust
and platform independent windowing toolkit, that is available to
Python programmers using the "tkinter" package, and its extension, the
"tkinter.tix" and the "tkinter.ttk" modules.

The "tkinter" package is a thin object-oriented layer on top of
Tcl/Tk. To use "tkinter", you don't need to write Tcl code, but you
will need to consult the Tk documentation, and occasionally the Tcl
documentation. "tkinter" is a set of wrappers that implement the Tk
widgets as Python classes.

"tkinter"'s chief virtues are that it is fast, and that it usually
comes bundled with Python. Although its standard documentation is
weak, good material is available, which includes: references,
tutorials, a book and others. "tkinter" is also famous for having an
outdated look and feel, which has been vastly improved in Tk 8.5.
Nevertheless, there are many other GUI libraries that you could be
interested in. The Python wiki lists several alternative GUI
frameworks and tools.

* "tkinter" --- Python interface to Tcl/Tk

  * Architecture

  * Tkinter Modules

  * Tkinter Life Preserver

    * A Hello World Program

    * Important Tk Concepts

    * Understanding How Tkinter Wraps Tcl/Tk

    * How do I...? What option does...?

    * Navigating the Tcl/Tk Reference Manual

  * Threading model

  * Handy Reference

    * Setting Options

    * The Packer

    * Packer Options

    * Coupling Widget Variables

    * The Window Manager

    * Tk Option Data Types

    * Bindings and Events

    * The index Parameter

    * Images

  * File Handlers

* "tkinter.colorchooser" --- Color choosing dialog

* "tkinter.font" --- Tkinter font wrapper

* Tkinter Dialogs

  * "tkinter.simpledialog" --- Standard Tkinter input dialogs

  * "tkinter.filedialog" --- File selection dialogs

    * Native Load/Save Dialogs

  * "tkinter.commondialog" --- Dialog window templates

* "tkinter.messagebox" --- Tkinter message prompts

* "tkinter.scrolledtext" --- Scrolled Text Widget

* "tkinter.dnd" --- Drag and drop support

* "tkinter.ttk" --- Tk themed widgets

  * Using Ttk

  * Ttk Widgets

  * Widget

    * Standard Options

    * Scrollable Widget Options

    * Label Options

    * Compatibility Options

    * Widget States

    * ttk.Widget

  * Combobox

    * Options

    * Virtual events

    * ttk.Combobox

  * Spinbox

    * Options

    * Virtual events

    * ttk.Spinbox

  * Notebook

    * Options

    * Tab Options

    * Tab Identifiers

    * Virtual Events

    * ttk.Notebook

  * Progressbar

    * Options

    * ttk.Progressbar

  * Separator

    * Options

  * Sizegrip

    * Platform-specific notes

    * Bugs

  * Treeview

    * Options

    * Item Options

    * Tag Options

    * Column Identifiers

    * Virtual Events

    * ttk.Treeview

  * Ttk Styling

    * Layouts

* "tkinter.tix" --- Extension widgets for Tk

  * Using Tix

  * Tix Widgets

    * Basic Widgets

    * File Selectors

    * Hierarchical ListBox

    * Tabular ListBox

    * Manager Widgets

    * Image Types

    * Miscellaneous Widgets

    * Form Geometry Manager

  * Tix Commands

* IDLE --- Python editor and shell

  * Menus

    * File menu (Shell and Editor)

    * Edit menu (Shell and Editor)

    * Format menu (Editor window only)

    * Run menu (Editor window only)

    * Shell menu (Shell window only)

    * Debug menu (Shell window only)

    * Options menu (Shell and Editor)

    * Window menu (Shell and Editor)

    * Help menu (Shell and Editor)

    * Context menus

  * Editing and Navigation

    * Editor windows

    * Key bindings

    * Automatic indentation

    * Search and Replace

    * Completions

    * Calltips

    * Code Context

    * Shell window

    * Text colors

  * Startup and Code Execution

    * Command line usage

    * Startup failure

    * Running user code

    * User output in Shell

    * Developing tkinter applications

    * Running without a subprocess

  * Help and Preferences

    * Help sources

    * Setting preferences

    * IDLE on macOS

    * Extensions

  * idlelib --- implementation of IDLE application
