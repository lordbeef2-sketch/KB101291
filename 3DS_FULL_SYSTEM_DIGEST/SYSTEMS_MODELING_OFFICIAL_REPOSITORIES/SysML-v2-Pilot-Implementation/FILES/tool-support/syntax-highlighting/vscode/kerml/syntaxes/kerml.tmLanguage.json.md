# OFFICIAL REPOSITORY FILE: SysML-v2-Pilot-Implementation/tool-support/syntax-highlighting/vscode/kerml/syntaxes/kerml.tmLanguage.json

- repository: `SysML-v2-Pilot-Implementation`
- source_path: `tool-support/syntax-highlighting/vscode/kerml/syntaxes/kerml.tmLanguage.json`
- source_url: https://github.com/Systems-Modeling/SysML-v2-Pilot-Implementation/blob/fa709f28dfd49dfdb7ee83e4e19da2f57e0eb3aa/tool-support/syntax-highlighting/vscode/kerml/syntaxes/kerml.tmLanguage.json
- source_bytes: 3342
- source_sha256: `ba081b410fce07b1ee99fe0b657a01bb40f21d7a57960799adb13d8174baf111`
- decoded_as: `utf-8`


## EXACT SOURCE

````json
{
  "$schema": "https://raw.githubusercontent.com/martinring/tmlanguage/master/tmlanguage.json",
  "name": "KerML",
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
        { "match": "\\b(about|abstract|alias|all|and|as|assoc|behavior|binding|bool|by|chains|class|classifier|comment|composite|conjugate|conjugates|conjugation|connector|const|crosses|datatype|default|dependency|derived|differences|disjoining|disjoint|doc|else|end|expr|false|feature|featured|featuring|filter|first|flow|for|from|function|hastype|if|implies|import|in|inout|interaction|intersects|inv|inverse|inverting|istype|language|library|locale|member|meta|metaclass|metadata|multiplicity|namespace|new|nonunique|not|null|of|or|ordered|out|package|portion|predicate|private|protected|public|redefines|redefinition|references|rep|return|specialization|specializes|standard|step|struct|subclassifier|subset|subsets|subtype|succession|then|to|true|type|typed|typing|unions|var|xor)\\b", "name": "keyword.other.kerml" },
        { "match": "(#|\\$|%|&|\\?|\\?\\?|@@|\\^|\\|)", "name": "keyword.operator.logical.kerml" },
        { "match": "(!=|!==|\\<|\\<=|=|==|===|\\>|\\>=)", "name": "keyword.operator.comparison.kerml" },
        { "match": "(\\*|\\*\\*|\\+|\\-|/)", "name": "keyword.operator.arithmetic.kerml" },
        { "match": "(\\-\\>|\\.\\.|\\.\\?|:|::|::\\>|:=|:\\>|:\\>\\>|=\\>|@|~)", "name": "keyword.operator.other.kerml" }
      ]
    },
    "strings": {
      "name": "string.quoted.double.kerml",
      "begin": "\"",
      "end": "\"",
      "patterns": [
        {
          "name": "constant.character.escape.kerml",
          "match": "\\\\."
        }
      ]
    },
    "quoted-variables": {
      "patterns": [{ "match": "('[^\\f\\n\\r\\t\\v\\\"\\\\]+?')", "name": "variable.name.quoted.kerml" }]
    },
    "comments": {
      "patterns": [
        {
          "captures": {
            "0": {
              "name": "punctuation.definition.comment.kerml"
            }
          },
          "match": "/\\*\\*/",
          "name": "comment.block.empty.kerml"
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
              "name": "punctuation.definition.comment.kerml"
            }
          },
          "end": "\\*/",
          "name": "comment.block.kerml"
        },
        {
          "begin": "(^[ \\t]+)?(?=//)",
          "beginCaptures": {
            "1": {
              "name": "punctuation.whitespace.comment.leading.kerml"
            }
          },
          "end": "(?!\\G)",
          "patterns": [
            {
              "begin": "//",
              "beginCaptures": {
                "0": {
                  "name": "punctuation.definition.comment.kerml"
                }
              },
              "end": "\\n",
              "name": "comment.line.double-slash.kerml"
            }
          ]
        }
      ]
    }
  },
  "scopeName": "source.kerml"
}

````
