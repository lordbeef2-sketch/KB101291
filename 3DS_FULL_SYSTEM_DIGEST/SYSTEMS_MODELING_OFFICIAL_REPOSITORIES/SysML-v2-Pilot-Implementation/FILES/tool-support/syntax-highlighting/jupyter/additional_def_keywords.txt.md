# OFFICIAL REPOSITORY FILE: SysML-v2-Pilot-Implementation/tool-support/syntax-highlighting/jupyter/additional_def_keywords.txt

- repository: `SysML-v2-Pilot-Implementation`
- source_path: `tool-support/syntax-highlighting/jupyter/additional_def_keywords.txt`
- source_url: https://github.com/Systems-Modeling/SysML-v2-Pilot-Implementation/blob/fa709f28dfd49dfdb7ee83e4e19da2f57e0eb3aa/tool-support/syntax-highlighting/jupyter/additional_def_keywords.txt
- source_bytes: 543
- source_sha256: `72a598042ca40ddf1322e595c977d229c5c4ed9f901b1e673a8d11c3cfc3865c`
- decoded_as: `utf-8`


## EXACT SOURCE

````text
# SysML v2 list of definition keywords in addition to 'def' and those that are directly used before 'def'
# Used by xtext_grammar_converter.py to generate Jupyter mode.ts source
# Format: one line per keyword, and comment lines start with # or //
# Keywords included for backwards compatibility
#
# Keywords without corresponding definition declarations
metadata
objective
ref
snapshot
subject
timeslice
binding
succession
transition
#
# Keywords that do not fall into the definition/usage pattern
comment
doc
package
rep

````
