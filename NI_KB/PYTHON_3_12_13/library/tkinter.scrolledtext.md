# PYTHON_3_12_13::library/tkinter.scrolledtext.md

<!--SYSTEM_CORPUS id=PYTHON_3_12_13 source_path=library/tkinter.scrolledtext.txt -->
- source: https://docs.python.org/3.12/
- archive_sha256: 48e950ab70335f2f49bd0418eaa26ab225942cd9c100e15428dc4f70f21b6ba0
- license: Python Software Foundation License Version 2; documentation examples additionally Zero Clause BSD
- fidelity: full-official-plain-text-document

"tkinter.scrolledtext" --- Scrolled Text Widget
***********************************************

**Source code:** Lib/tkinter/scrolledtext.py

======================================================================

The "tkinter.scrolledtext" module provides a class of the same name
which implements a basic text widget which has a vertical scroll bar
configured to do the "right thing."  Using the "ScrolledText" class is
a lot easier than setting up a text widget and scroll bar directly.

The text widget and scrollbar are packed together in a "Frame", and
the methods of the "Grid" and "Pack" geometry managers are acquired
from the "Frame" object.  This allows the "ScrolledText" widget to be
used directly to achieve most normal geometry management behavior.

Should more specific control be necessary, the following attributes
are available:

class tkinter.scrolledtext.ScrolledText(master=None, **kw)

   frame

      The frame which surrounds the text and scroll bar widgets.

   vbar

      The scroll bar widget.
