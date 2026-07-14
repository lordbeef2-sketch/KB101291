# PYTHON_3_12_13::library/curses.panel.md

<!--SYSTEM_CORPUS id=PYTHON_3_12_13 source_path=library/curses.panel.txt -->
- source: https://docs.python.org/3.12/
- archive_sha256: 48e950ab70335f2f49bd0418eaa26ab225942cd9c100e15428dc4f70f21b6ba0
- license: Python Software Foundation License Version 2; documentation examples additionally Zero Clause BSD
- fidelity: full-official-plain-text-document

"curses.panel" --- A panel stack extension for curses
*****************************************************

======================================================================

Panels are windows with the added feature of depth, so they can be
stacked on top of each other, and only the visible portions of each
window will be displayed.  Panels can be added, moved up or down in
the stack, and removed.


Functions
=========

The module "curses.panel" defines the following functions:

curses.panel.bottom_panel()

   Returns the bottom panel in the panel stack.

curses.panel.new_panel(win)

   Returns a panel object, associating it with the given window *win*.
   Be aware that you need to keep the returned panel object referenced
   explicitly.  If you don't, the panel object is garbage collected
   and removed from the panel stack.

curses.panel.top_panel()

   Returns the top panel in the panel stack.

curses.panel.update_panels()

   Updates the virtual screen after changes in the panel stack. This
   does not call "curses.doupdate()", so you'll have to do this
   yourself.


Panel Objects
=============

Panel objects, as returned by "new_panel()" above, are windows with a
stacking order. There's always a window associated with a panel which
determines the content, while the panel methods are responsible for
the window's depth in the panel stack.

Panel objects have the following methods:

Panel.above()

   Returns the panel above the current panel.

Panel.below()

   Returns the panel below the current panel.

Panel.bottom()

   Push the panel to the bottom of the stack.

Panel.hidden()

   Returns "True" if the panel is hidden (not visible), "False"
   otherwise.

Panel.hide()

   Hide the panel. This does not delete the object, it just makes the
   window on screen invisible.

Panel.move(y, x)

   Move the panel to the screen coordinates "(y, x)".

Panel.replace(win)

   Change the window associated with the panel to the window *win*.

Panel.set_userptr(obj)

   Set the panel's user pointer to *obj*. This is used to associate an
   arbitrary piece of data with the panel, and can be any Python
   object.

Panel.show()

   Display the panel (which might have been hidden).

Panel.top()

   Push panel to the top of the stack.

Panel.userptr()

   Returns the user pointer for the panel.  This might be any Python
   object.

Panel.window()

   Returns the window object associated with the panel.
