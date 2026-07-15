# OFFICIAL REPOSITORY FILE: SysML-v2-Pilot-Implementation/tool-support/bnf_grammar_tools/unittests/test_render_nested_lists.py

- repository: `SysML-v2-Pilot-Implementation`
- source_path: `tool-support/bnf_grammar_tools/unittests/test_render_nested_lists.py`
- source_url: https://github.com/Systems-Modeling/SysML-v2-Pilot-Implementation/blob/fa709f28dfd49dfdb7ee83e4e19da2f57e0eb3aa/tool-support/bnf_grammar_tools/unittests/test_render_nested_lists.py
- source_bytes: 1200
- source_sha256: `e5d52b989be76ff9543245090a6c238ea71eeecb2e36319753912e2f951f92e8`
- decoded_as: `utf-8`


## EXACT SOURCE

````python
import unittest
from ..bnf_grammar import bnf_grammar_processor as bgp

class TestRenderNestedLists(unittest.TestCase):

    def test_render_nested_lists(self):
        html_snippet = "<ol><li>One</li><li>Two<ul><li>Two sub one</li><li>Two sub two</li></ul>Two continued</li></ol>"
        self.assertEqual(bgp.render_nested_lists(html_snippet, bgp.RenderMode.TXT, False), """\
  1. One
  2. Two
    • Two sub one
    • Two sub two
  Two continued""")

        self.assertEqual(bgp.render_nested_lists(html_snippet, bgp.RenderMode.TXT, True), """\
//   1. One
//   2. Two
//     • Two sub one
//     • Two sub two
//   Two continued""")

        self.assertEqual(bgp.render_nested_lists(html_snippet, bgp.RenderMode.HTML, False), """\
<ol>
<li>1. One</li>
<li>2. Two
<ul>
<li>• Two sub one</li>
<li>• Two sub two</li>
</ul>
Two continued</li>
</ol>
""")

        self.assertEqual(bgp.render_nested_lists(html_snippet, bgp.RenderMode.HTML, True), """\
<ol>
<li>// 1. One</li>
<li>// 2. Two
<ul>
<li>// • Two sub one</li>
<li>// • Two sub two</li>
</ul>
// Two continued</li>
</ol>
""")

# if __name__ == '__main__':
#     unittest.main()

````
