# OFFICIAL REPOSITORY FILE: SysML-v2-API-Services/conf/json/schema/metamodel/Comment.json

- repository: `SysML-v2-API-Services`
- source_path: `conf/json/schema/metamodel/Comment.json`
- source_url: https://github.com/Systems-Modeling/SysML-v2-API-Services/blob/0af711b14bbcea7b240bb0a3a65817ae68302092/conf/json/schema/metamodel/Comment.json
- source_bytes: 14364
- source_sha256: `506b59203c2c40c15b9a40b57308838f7ba877a581066aea5dea6b349cad9533`
- decoded_as: `utf-8`


## EXACT SOURCE

````json
{
  "$schema": "https://json-schema.org/draft/2020-12/schema",
  "$id": "https://www.omg.org/spec/SysML/20250201/Comment",
  "title": "Comment",
  "anyOf": [
    {
      "type": "object",
      "properties": {
        "@id": {
          "type": "string",
          "format": "uuid"
        },
        "@type": {
          "type": "string",
          "const": "Comment"
        },
        "aliasIds": {
          "type": "array",
          "items": {
            "type": "string"
          }
        },
        "annotatedElement": {
          "type": "array",
          "items": {
            "$ref": "https://www.omg.org/spec/SysML/20250201/Identified",
            "$comment": "https://www.omg.org/spec/SysML/20250201/Element"
          },
          "minItems": 1
        },
        "annotation": {
          "type": "array",
          "items": {
            "$ref": "https://www.omg.org/spec/SysML/20250201/Identified",
            "$comment": "https://www.omg.org/spec/SysML/20250201/Annotation"
          }
        },
        "body": {
          "type": "string"
        },
        "declaredName": {
          "oneOf": [
            {
              "type": "string"
            },
            {
              "type": "null"
            }
          ]
        },
        "declaredShortName": {
          "oneOf": [
            {
              "type": "string"
            },
            {
              "type": "null"
            }
          ]
        },
        "documentation": {
          "type": "array",
          "items": {
            "$ref": "https://www.omg.org/spec/SysML/20250201/Identified",
            "$comment": "https://www.omg.org/spec/SysML/20250201/Documentation"
          }
        },
        "elementId": {
          "oneOf": [
            {
              "type": "string"
            },
            {
              "type": "null"
            }
          ]
        },
        "isImpliedIncluded": {
          "oneOf": [
            {
              "type": "boolean"
            },
            {
              "type": "null"
            }
          ]
        },
        "isLibraryElement": {
          "oneOf": [
            {
              "type": "boolean"
            },
            {
              "type": "null"
            }
          ]
        },
        "locale": {
          "oneOf": [
            {
              "type": "string"
            },
            {
              "type": "null"
            }
          ]
        },
        "name": {
          "oneOf": [
            {
              "type": "string"
            },
            {
              "type": "null"
            }
          ]
        },
        "ownedAnnotatingRelationship": {
          "type": "array",
          "items": {
            "$ref": "https://www.omg.org/spec/SysML/20250201/Identified",
            "$comment": "https://www.omg.org/spec/SysML/20250201/Annotation"
          }
        },
        "ownedAnnotation": {
          "type": "array",
          "items": {
            "$ref": "https://www.omg.org/spec/SysML/20250201/Identified",
            "$comment": "https://www.omg.org/spec/SysML/20250201/Annotation"
          }
        },
        "ownedElement": {
          "type": "array",
          "items": {
            "$ref": "https://www.omg.org/spec/SysML/20250201/Identified",
            "$comment": "https://www.omg.org/spec/SysML/20250201/Element"
          }
        },
        "ownedRelationship": {
          "type": "array",
          "items": {
            "$ref": "https://www.omg.org/spec/SysML/20250201/Identified",
            "$comment": "https://www.omg.org/spec/SysML/20250201/Relationship"
          }
        },
        "owner": {
          "oneOf": [
            {
              "$ref": "https://www.omg.org/spec/SysML/20250201/Identified",
              "$comment": "https://www.omg.org/spec/SysML/20250201/Element"
            },
            {
              "type": "null"
            }
          ]
        },
        "owningAnnotatingRelationship": {
          "oneOf": [
            {
              "$ref": "https://www.omg.org/spec/SysML/20250201/Identified",
              "$comment": "https://www.omg.org/spec/SysML/20250201/Annotation"
            },
            {
              "type": "null"
            }
          ]
        },
        "owningMembership": {
          "oneOf": [
            {
              "$ref": "https://www.omg.org/spec/SysML/20250201/Identified",
              "$comment": "https://www.omg.org/spec/SysML/20250201/OwningMembership"
            },
            {
              "type": "null"
            }
          ]
        },
        "owningNamespace": {
          "oneOf": [
            {
              "$ref": "https://www.omg.org/spec/SysML/20250201/Identified",
              "$comment": "https://www.omg.org/spec/SysML/20250201/Namespace"
            },
            {
              "type": "null"
            }
          ]
        },
        "owningRelationship": {
          "oneOf": [
            {
              "$ref": "https://www.omg.org/spec/SysML/20250201/Identified",
              "$comment": "https://www.omg.org/spec/SysML/20250201/Relationship"
            },
            {
              "type": "null"
            }
          ]
        },
        "qualifiedName": {
          "oneOf": [
            {
              "type": "string"
            },
            {
              "type": "null"
            }
          ]
        },
        "shortName": {
          "oneOf": [
            {
              "type": "string"
            },
            {
              "type": "null"
            }
          ]
        },
        "textualRepresentation": {
          "type": "array",
          "items": {
            "$ref": "https://www.omg.org/spec/SysML/20250201/Identified",
            "$comment": "https://www.omg.org/spec/SysML/20250201/TextualRepresentation"
          }
        }
      },
      "required": [
        "@id",
        "@type",
        "aliasIds",
        "annotatedElement",
        "annotation",
        "body",
        "declaredName",
        "declaredShortName",
        "documentation",
        "elementId",
        "isImpliedIncluded",
        "isLibraryElement",
        "locale",
        "name",
        "ownedAnnotatingRelationship",
        "ownedAnnotation",
        "ownedElement",
        "ownedRelationship",
        "owner",
        "owningAnnotatingRelationship",
        "owningMembership",
        "owningNamespace",
        "owningRelationship",
        "qualifiedName",
        "shortName",
        "textualRepresentation"
      ],
      "additionalProperties": false
    },
    {
      "$ref": "https://www.omg.org/spec/SysML/20250201/Documentation"
    }
  ],
  "$defs": {
    "Identified": {
      "$id": "https://www.omg.org/spec/SysML/20250201/Identified",
      "title": "Identified",
      "type": "object",
      "properties": {
        "@id": {
          "type": "string",
          "format": "uuid"
        }
      },
      "required": [
        "@id"
      ],
      "additionalProperties": false
    },
    "Documentation": {
      "$id": "https://www.omg.org/spec/SysML/20250201/Documentation",
      "title": "Documentation",
      "type": "object",
      "properties": {
        "@id": {
          "type": "string",
          "format": "uuid"
        },
        "@type": {
          "type": "string",
          "const": "Documentation"
        },
        "aliasIds": {
          "type": "array",
          "items": {
            "type": "string"
          }
        },
        "annotatedElement": {
          "type": "array",
          "items": {
            "$ref": "https://www.omg.org/spec/SysML/20250201/Identified",
            "$comment": "https://www.omg.org/spec/SysML/20250201/Element"
          },
          "minItems": 1
        },
        "annotation": {
          "type": "array",
          "items": {
            "$ref": "https://www.omg.org/spec/SysML/20250201/Identified",
            "$comment": "https://www.omg.org/spec/SysML/20250201/Annotation"
          }
        },
        "body": {
          "type": "string"
        },
        "declaredName": {
          "oneOf": [
            {
              "type": "string"
            },
            {
              "type": "null"
            }
          ]
        },
        "declaredShortName": {
          "oneOf": [
            {
              "type": "string"
            },
            {
              "type": "null"
            }
          ]
        },
        "documentation": {
          "type": "array",
          "items": {
            "$ref": "https://www.omg.org/spec/SysML/20250201/Identified",
            "$comment": "https://www.omg.org/spec/SysML/20250201/Documentation"
          }
        },
        "documentedElement": {
          "$ref": "https://www.omg.org/spec/SysML/20250201/Identified",
          "$comment": "https://www.omg.org/spec/SysML/20250201/Element"
        },
        "elementId": {
          "oneOf": [
            {
              "type": "string"
            },
            {
              "type": "null"
            }
          ]
        },
        "isImpliedIncluded": {
          "oneOf": [
            {
              "type": "boolean"
            },
            {
              "type": "null"
            }
          ]
        },
        "isLibraryElement": {
          "oneOf": [
            {
              "type": "boolean"
            },
            {
              "type": "null"
            }
          ]
        },
        "locale": {
          "oneOf": [
            {
              "type": "string"
            },
            {
              "type": "null"
            }
          ]
        },
        "name": {
          "oneOf": [
            {
              "type": "string"
            },
            {
              "type": "null"
            }
          ]
        },
        "ownedAnnotatingRelationship": {
          "type": "array",
          "items": {
            "$ref": "https://www.omg.org/spec/SysML/20250201/Identified",
            "$comment": "https://www.omg.org/spec/SysML/20250201/Annotation"
          }
        },
        "ownedAnnotation": {
          "type": "array",
          "items": {
            "$ref": "https://www.omg.org/spec/SysML/20250201/Identified",
            "$comment": "https://www.omg.org/spec/SysML/20250201/Annotation"
          }
        },
        "ownedElement": {
          "type": "array",
          "items": {
            "$ref": "https://www.omg.org/spec/SysML/20250201/Identified",
            "$comment": "https://www.omg.org/spec/SysML/20250201/Element"
          }
        },
        "ownedRelationship": {
          "type": "array",
          "items": {
            "$ref": "https://www.omg.org/spec/SysML/20250201/Identified",
            "$comment": "https://www.omg.org/spec/SysML/20250201/Relationship"
          }
        },
        "owner": {
          "oneOf": [
            {
              "$ref": "https://www.omg.org/spec/SysML/20250201/Identified",
              "$comment": "https://www.omg.org/spec/SysML/20250201/Element"
            },
            {
              "type": "null"
            }
          ]
        },
        "owningAnnotatingRelationship": {
          "oneOf": [
            {
              "$ref": "https://www.omg.org/spec/SysML/20250201/Identified",
              "$comment": "https://www.omg.org/spec/SysML/20250201/Annotation"
            },
            {
              "type": "null"
            }
          ]
        },
        "owningMembership": {
          "oneOf": [
            {
              "$ref": "https://www.omg.org/spec/SysML/20250201/Identified",
              "$comment": "https://www.omg.org/spec/SysML/20250201/OwningMembership"
            },
            {
              "type": "null"
            }
          ]
        },
        "owningNamespace": {
          "oneOf": [
            {
              "$ref": "https://www.omg.org/spec/SysML/20250201/Identified",
              "$comment": "https://www.omg.org/spec/SysML/20250201/Namespace"
            },
            {
              "type": "null"
            }
          ]
        },
        "owningRelationship": {
          "oneOf": [
            {
              "$ref": "https://www.omg.org/spec/SysML/20250201/Identified",
              "$comment": "https://www.omg.org/spec/SysML/20250201/Relationship"
            },
            {
              "type": "null"
            }
          ]
        },
        "qualifiedName": {
          "oneOf": [
            {
              "type": "string"
            },
            {
              "type": "null"
            }
          ]
        },
        "shortName": {
          "oneOf": [
            {
              "type": "string"
            },
            {
              "type": "null"
            }
          ]
        },
        "textualRepresentation": {
          "type": "array",
          "items": {
            "$ref": "https://www.omg.org/spec/SysML/20250201/Identified",
            "$comment": "https://www.omg.org/spec/SysML/20250201/TextualRepresentation"
          }
        }
      },
      "required": [
        "@id",
        "@type",
        "aliasIds",
        "annotatedElement",
        "annotation",
        "body",
        "declaredName",
        "declaredShortName",
        "documentation",
        "documentedElement",
        "elementId",
        "isImpliedIncluded",
        "isLibraryElement",
        "locale",
        "name",
        "ownedAnnotatingRelationship",
        "ownedAnnotation",
        "ownedElement",
        "ownedRelationship",
        "owner",
        "owningAnnotatingRelationship",
        "owningMembership",
        "owningNamespace",
        "owningRelationship",
        "qualifiedName",
        "shortName",
        "textualRepresentation"
      ],
      "additionalProperties": false
    }
  }
}
````
