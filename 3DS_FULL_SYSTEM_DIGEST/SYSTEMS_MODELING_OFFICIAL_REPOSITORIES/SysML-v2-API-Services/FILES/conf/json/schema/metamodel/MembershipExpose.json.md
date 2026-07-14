# OFFICIAL REPOSITORY FILE: SysML-v2-API-Services/conf/json/schema/metamodel/MembershipExpose.json

- repository: `SysML-v2-API-Services`
- source_path: `conf/json/schema/metamodel/MembershipExpose.json`
- source_url: https://github.com/Systems-Modeling/SysML-v2-API-Services/blob/0af711b14bbcea7b240bb0a3a65817ae68302092/conf/json/schema/metamodel/MembershipExpose.json
- source_bytes: 7768
- source_sha256: `114ea2d7d5cc462299d97c9c14ecc5792c4d6dd3b56fcb5544829fd8252a4026`
- decoded_as: `utf-8`


## EXACT SOURCE

````json
{
  "$schema": "https://json-schema.org/draft/2020-12/schema",
  "$id": "https://www.omg.org/spec/SysML/20250201/MembershipExpose",
  "title": "MembershipExpose",
  "type": "object",
  "properties": {
    "@id": {
      "type": "string",
      "format": "uuid"
    },
    "@type": {
      "type": "string",
      "const": "MembershipExpose"
    },
    "aliasIds": {
      "type": "array",
      "items": {
        "type": "string"
      }
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
    "importOwningNamespace": {
      "$ref": "https://www.omg.org/spec/SysML/20250201/Identified",
      "$comment": "https://www.omg.org/spec/SysML/20250201/Namespace"
    },
    "importedElement": {
      "$ref": "https://www.omg.org/spec/SysML/20250201/Identified",
      "$comment": "https://www.omg.org/spec/SysML/20250201/Element"
    },
    "importedMembership": {
      "$ref": "https://www.omg.org/spec/SysML/20250201/Identified",
      "$comment": "https://www.omg.org/spec/SysML/20250201/Membership"
    },
    "isImplied": {
      "oneOf": [
        {
          "type": "boolean"
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
    "isImportAll": {
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
    "isRecursive": {
      "oneOf": [
        {
          "type": "boolean"
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
    "ownedRelatedElement": {
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
    "owningRelatedElement": {
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
    "relatedElement": {
      "type": "array",
      "items": {
        "$ref": "https://www.omg.org/spec/SysML/20250201/Identified",
        "$comment": "https://www.omg.org/spec/SysML/20250201/Element"
      }
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
    "source": {
      "type": "array",
      "items": {
        "$ref": "https://www.omg.org/spec/SysML/20250201/Identified",
        "$comment": "https://www.omg.org/spec/SysML/20250201/Element"
      }
    },
    "target": {
      "type": "array",
      "items": {
        "$ref": "https://www.omg.org/spec/SysML/20250201/Identified",
        "$comment": "https://www.omg.org/spec/SysML/20250201/Element"
      }
    },
    "textualRepresentation": {
      "type": "array",
      "items": {
        "$ref": "https://www.omg.org/spec/SysML/20250201/Identified",
        "$comment": "https://www.omg.org/spec/SysML/20250201/TextualRepresentation"
      }
    },
    "visibility": {
      "oneOf": [
        {
          "$ref": "https://www.omg.org/spec/SysML/20250201/VisibilityKind"
        },
        {
          "type": "null"
        }
      ]
    }
  },
  "required": [
    "@id",
    "@type",
    "aliasIds",
    "declaredName",
    "declaredShortName",
    "documentation",
    "elementId",
    "importOwningNamespace",
    "importedElement",
    "importedMembership",
    "isImplied",
    "isImpliedIncluded",
    "isImportAll",
    "isLibraryElement",
    "isRecursive",
    "name",
    "ownedAnnotation",
    "ownedElement",
    "ownedRelatedElement",
    "ownedRelationship",
    "owner",
    "owningMembership",
    "owningNamespace",
    "owningRelatedElement",
    "owningRelationship",
    "qualifiedName",
    "relatedElement",
    "shortName",
    "source",
    "target",
    "textualRepresentation",
    "visibility"
  ],
  "additionalProperties": false,
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
    "VisibilityKind": {
      "$id": "https://www.omg.org/spec/SysML/20250201/VisibilityKind",
      "title": "VisibilityKind",
      "type": "string",
      "enum": [
        "private",
        "protected",
        "public"
      ]
    }
  }
}
````
