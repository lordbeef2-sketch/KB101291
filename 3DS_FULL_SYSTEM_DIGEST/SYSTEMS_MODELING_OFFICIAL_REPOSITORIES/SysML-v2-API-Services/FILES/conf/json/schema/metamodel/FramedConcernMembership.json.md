# OFFICIAL REPOSITORY FILE: SysML-v2-API-Services/conf/json/schema/metamodel/FramedConcernMembership.json

- repository: `SysML-v2-API-Services`
- source_path: `conf/json/schema/metamodel/FramedConcernMembership.json`
- source_url: https://github.com/Systems-Modeling/SysML-v2-API-Services/blob/0af711b14bbcea7b240bb0a3a65817ae68302092/conf/json/schema/metamodel/FramedConcernMembership.json
- source_bytes: 10243
- source_sha256: `21b6e95147b124178bc47b7c902f0e289a52a8e2378952bb8d28d9daf02d4342`
- decoded_as: `utf-8`


## EXACT SOURCE

````json
{
  "$schema": "https://json-schema.org/draft/2020-12/schema",
  "$id": "https://www.omg.org/spec/SysML/20250201/FramedConcernMembership",
  "title": "FramedConcernMembership",
  "type": "object",
  "properties": {
    "@id": {
      "type": "string",
      "format": "uuid"
    },
    "@type": {
      "type": "string",
      "const": "FramedConcernMembership"
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
    "kind": {
      "oneOf": [
        {
          "$ref": "https://www.omg.org/spec/SysML/20250201/RequirementConstraintKind"
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
    "ownedConcern": {
      "$ref": "https://www.omg.org/spec/SysML/20250201/Identified",
      "$comment": "https://www.omg.org/spec/SysML/20250201/ConcernUsage"
    },
    "ownedConstraint": {
      "$ref": "https://www.omg.org/spec/SysML/20250201/Identified",
      "$comment": "https://www.omg.org/spec/SysML/20250201/ConstraintUsage"
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
    "referencedConcern": {
      "$ref": "https://www.omg.org/spec/SysML/20250201/Identified",
      "$comment": "https://www.omg.org/spec/SysML/20250201/ConcernUsage"
    },
    "referencedConstraint": {
      "$ref": "https://www.omg.org/spec/SysML/20250201/Identified",
      "$comment": "https://www.omg.org/spec/SysML/20250201/ConstraintUsage"
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
    "kind",
    "memberElement",
    "memberElementId",
    "memberName",
    "memberShortName",
    "membershipOwningNamespace",
    "name",
    "ownedAnnotation",
    "ownedConcern",
    "ownedConstraint",
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
    "referencedConcern",
    "referencedConstraint",
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
    "RequirementConstraintKind": {
      "$id": "https://www.omg.org/spec/SysML/20250201/RequirementConstraintKind",
      "title": "RequirementConstraintKind",
      "type": "string",
      "enum": [
        "assumption",
        "requirement"
      ]
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
