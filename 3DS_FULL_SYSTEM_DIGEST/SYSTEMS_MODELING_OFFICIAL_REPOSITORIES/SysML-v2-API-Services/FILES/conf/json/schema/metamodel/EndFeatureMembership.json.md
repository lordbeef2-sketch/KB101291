# OFFICIAL REPOSITORY FILE: SysML-v2-API-Services/conf/json/schema/metamodel/EndFeatureMembership.json

- repository: `SysML-v2-API-Services`
- source_path: `conf/json/schema/metamodel/EndFeatureMembership.json`
- source_url: https://github.com/Systems-Modeling/SysML-v2-API-Services/blob/0af711b14bbcea7b240bb0a3a65817ae68302092/conf/json/schema/metamodel/EndFeatureMembership.json
- source_bytes: 8926
- source_sha256: `782b6b2fc0ee2746c37dce37533efef4048a9b7e687bf89c5234e20ca1f8422a`
- decoded_as: `utf-8`


## EXACT SOURCE

````json
{
  "$schema": "https://json-schema.org/draft/2020-12/schema",
  "$id": "https://www.omg.org/spec/SysML/20250201/EndFeatureMembership",
  "title": "EndFeatureMembership",
  "type": "object",
  "properties": {
    "@id": {
      "type": "string",
      "format": "uuid"
    },
    "@type": {
      "type": "string",
      "const": "EndFeatureMembership"
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
    "memberElement": {
      "$ref": "https://www.omg.org/spec/SysML/20250201/Identified",
      "$comment": "https://www.omg.org/spec/SysML/20250201/Element"
    },
    "memberElementId": {
      "oneOf": [
        {
          "type": "string"
        },
        {
          "type": "null"
        }
      ]
    },
    "memberName": {
      "oneOf": [
        {
          "type": "string"
        },
        {
          "type": "null"
        }
      ]
    },
    "memberShortName": {
      "oneOf": [
        {
          "type": "string"
        },
        {
          "type": "null"
        }
      ]
    },
    "membershipOwningNamespace": {
      "$ref": "https://www.omg.org/spec/SysML/20250201/Identified",
      "$comment": "https://www.omg.org/spec/SysML/20250201/Namespace"
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
    "ownedMemberElement": {
      "$ref": "https://www.omg.org/spec/SysML/20250201/Identified",
      "$comment": "https://www.omg.org/spec/SysML/20250201/Element"
    },
    "ownedMemberElementId": {
      "oneOf": [
        {
          "type": "string"
        },
        {
          "type": "null"
        }
      ]
    },
    "ownedMemberFeature": {
      "$ref": "https://www.omg.org/spec/SysML/20250201/Identified",
      "$comment": "https://www.omg.org/spec/SysML/20250201/Feature"
    },
    "ownedMemberName": {
      "oneOf": [
        {
          "type": "string"
        },
        {
          "type": "null"
        }
      ]
    },
    "ownedMemberShortName": {
      "oneOf": [
        {
          "type": "string"
        },
        {
          "type": "null"
        }
      ]
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
    "owningType": {
      "$ref": "https://www.omg.org/spec/SysML/20250201/Identified",
      "$comment": "https://www.omg.org/spec/SysML/20250201/Type"
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
    "isImplied",
    "isImpliedIncluded",
    "isLibraryElement",
    "memberElement",
    "memberElementId",
    "memberName",
    "memberShortName",
    "membershipOwningNamespace",
    "name",
    "ownedAnnotation",
    "ownedElement",
    "ownedMemberElement",
    "ownedMemberElementId",
    "ownedMemberFeature",
    "ownedMemberName",
    "ownedMemberShortName",
    "ownedRelatedElement",
    "ownedRelationship",
    "owner",
    "owningMembership",
    "owningNamespace",
    "owningRelatedElement",
    "owningRelationship",
    "owningType",
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
