# PYTHON_3_12_13::library/html.entities.md

<!--SYSTEM_CORPUS id=PYTHON_3_12_13 source_path=library/html.entities.txt -->
- source: https://docs.python.org/3.12/
- archive_sha256: 48e950ab70335f2f49bd0418eaa26ab225942cd9c100e15428dc4f70f21b6ba0
- license: Python Software Foundation License Version 2; documentation examples additionally Zero Clause BSD
- fidelity: full-official-plain-text-document

"html.entities" --- Definitions of HTML general entities
********************************************************

**Source code:** Lib/html/entities.py

======================================================================

This module defines four dictionaries, "html5", "name2codepoint",
"codepoint2name", and "entitydefs".

html.entities.html5

   A dictionary that maps HTML5 named character references [1] to the
   equivalent Unicode character(s), e.g. "html5['gt;'] == '>'". Note
   that the trailing semicolon is included in the name (e.g. "'gt;'"),
   however some of the names are accepted by the standard even without
   the semicolon: in this case the name is present with and without
   the "';'". See also "html.unescape()".

   Added in version 3.3.

html.entities.entitydefs

   A dictionary mapping XHTML 1.0 entity definitions to their
   replacement text in ISO Latin-1.

html.entities.name2codepoint

   A dictionary that maps HTML4 entity names to the Unicode code
   points.

html.entities.codepoint2name

   A dictionary that maps Unicode code points to HTML4 entity names.

-[ Footnotes ]-

[1] See https://html.spec.whatwg.org/multipage/named-characters.html
    #named-character-references
