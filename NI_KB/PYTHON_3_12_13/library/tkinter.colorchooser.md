# PYTHON_3_12_13::library/tkinter.colorchooser.md

<!--SYSTEM_CORPUS id=PYTHON_3_12_13 source_path=library/tkinter.colorchooser.txt -->
- source: https://docs.python.org/3.12/
- archive_sha256: 48e950ab70335f2f49bd0418eaa26ab225942cd9c100e15428dc4f70f21b6ba0
- license: Python Software Foundation License Version 2; documentation examples additionally Zero Clause BSD
- fidelity: full-official-plain-text-document

"tkinter.colorchooser" --- Color choosing dialog
************************************************

**Source code:** Lib/tkinter/colorchooser.py

======================================================================

The "tkinter.colorchooser" module provides the "Chooser" class as an
interface to the native color picker dialog. "Chooser" implements a
modal color choosing dialog window. The "Chooser" class inherits from
the "Dialog" class.

class tkinter.colorchooser.Chooser(master=None, **options)

tkinter.colorchooser.askcolor(color=None, **options)

   Create a color choosing dialog. A call to this method will show the
   window, wait for the user to make a selection, and return the
   selected color (or "None") to the caller.

See also:

  Module "tkinter.commondialog"
     Tkinter standard dialog module
