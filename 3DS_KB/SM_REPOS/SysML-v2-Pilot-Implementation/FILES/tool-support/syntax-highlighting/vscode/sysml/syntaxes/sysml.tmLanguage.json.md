# OFFICIAL REPOSITORY FILE: SysML-v2-Pilot-Implementation/tool-support/syntax-highlighting/vscode/sysml/syntaxes/sysml.tmLanguage.json

- repository: `SysML-v2-Pilot-Implementation`
- source_path: `tool-support/syntax-highlighting/vscode/sysml/syntaxes/sysml.tmLanguage.json`
- source_url: https://github.com/Systems-Modeling/SysML-v2-Pilot-Implementation/blob/fa709f28dfd49dfdb7ee83e4e19da2f57e0eb3aa/tool-support/syntax-highlighting/vscode/sysml/syntaxes/sysml.tmLanguage.json
- source_bytes: 3481
- source_sha256: `9828f50a938b99175be170e471b54cff424545f1473e5d9b4482aeeff51475ba`
- decoded_as: `utf-8`


## EXACT SOURCE

````json
{
  "$schema": "https://raw.githubusercontent.com/martinring/tmlanguage/master/tmlanguage.json",
  "name": "SysML",
  "patterns": [
    {
      "include": "#comments"
    },
    {
      "include": "#keywords"
    },
    {
      "include": "#quoted-variables"
    },
    {
      "include": "#strings"
    }
  ],
  "repository": {
    "keywords": {
      "patterns": [
        { "match": "\\b(about|abstract|accept|action|actor|after|alias|all|allocate|allocation|analysis|and|as|assert|assign|assume|at|attribute|bind|binding|by|calc|case|comment|concern|connect|connection|constant|constraint|crosses|decide|def|default|defined|dependency|derived|do|doc|else|end|entry|enum|event|exhibit|exit|expose|false|filter|first|flow|for|fork|frame|from|hastype|if|implies|import|in|include|individual|inout|interface|istype|item|join|language|library|locale|loop|merge|message|meta|metadata|new|nonunique|not|null|objective|occurrence|of|or|ordered|out|package|parallel|part|perform|port|private|protected|public|redefines|ref|references|render|rendering|rep|require|requirement|return|satisfy|send|snapshot|specializes|stakeholder|standard|state|subject|subsets|succession|terminate|then|timeslice|to|transition|true|until|use|variant|variation|verification|verify|via|view|viewpoint|when|while|xor)\\b", "name": "keyword.other.sysml" },
        { "match": "(#|\\$|%|&|\\?|\\?\\?|@@|\\^|\\|)", "name": "keyword.operator.logical.sysml" },
        { "match": "(!=|!==|\\<|\\<=|=|==|===|\\>|\\>=)", "name": "keyword.operator.comparison.sysml" },
        { "match": "(\\*|\\*\\*|\\+|\\-|/)", "name": "keyword.operator.arithmetic.sysml" },
        { "match": "(\\-\\>|\\.\\.|\\.\\?|:|::|::\\>|:=|:\\>|:\\>\\>|=\\>|@|~)", "name": "keyword.operator.other.sysml" }
      ]
    },
    "strings": {
      "name": "string.quoted.double.sysml",
      "begin": "\"",
      "end": "\"",
      "patterns": [
        {
          "name": "constant.character.escape.sysml",
          "match": "\\\\."
        }
      ]
    },
    "quoted-variables": {
      "patterns": [{ "match": "('[^\\f\\n\\r\\t\\v\\\"\\\\]+?')", "name": "variable.name.quoted.sysml" }]
    },
    "comments": {
      "patterns": [
        {
          "captures": {
            "0": {
              "name": "punctuation.definition.comment.sysml"
            }
          },
          "match": "/\\*\\*/",
          "name": "comment.block.empty.sysml"
        },
        {
          "include": "#comments-inline"
        }
      ]
    },
    "comments-inline": {
      "patterns": [
        {
          "begin": "/\\*",
          "captures": {
            "0": {
              "name": "punctuation.definition.comment.sysml"
            }
          },
          "end": "\\*/",
          "name": "comment.block.sysml"
        },
        {
          "begin": "(^[ \\t]+)?(?=//)",
          "beginCaptures": {
            "1": {
              "name": "punctuation.whitespace.comment.leading.sysml"
            }
          },
          "end": "(?!\\G)",
          "patterns": [
            {
              "begin": "//",
              "beginCaptures": {
                "0": {
                  "name": "punctuation.definition.comment.sysml"
                }
              },
              "end": "\\n",
              "name": "comment.line.double-slash.sysml"
            }
          ]
        }
      ]
    }
  },
  "scopeName": "source.sysml"
}

````
