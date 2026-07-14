# OFFICIAL REPOSITORY FILE: SysML-v2-API-Services/conf/json/schema/metamodel/RequirementVerificationMembership.json

- repository: `SysML-v2-API-Services`
- source_path: `conf/json/schema/metamodel/RequirementVerificationMembership.json`
- source_url: https://github.com/Systems-Modeling/SysML-v2-API-Services/blob/0af711b14bbcea7b240bb0a3a65817ae68302092/conf/json/schema/metamodel/RequirementVerificationMembership.json
- source_bytes: 10293
- source_sha256: `b30d9c3e18266277d17e0ba3cd3b63afd5a0c06347ae5d432950e5fa2b5e7456`
- decoded_as: `utf-8`


## EXACT SOURCE

````json
{
  "$schema": "https://json-schema.org/draft/2020-12/schema",
  "$id": "https://www.omg.org/spec/SysML/20250201/RequirementVerificationMembership",
  "title": "RequirementVerificationMembership",
  "type": "object",
  "properties": {
    "@id": {
      "type": "string",
      "format": "uuid"
    },
    "@type": {
      "type": "string",
      "const": "RequirementVerificationMembership"
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
    "ownedRequirement": {
      "$ref": "https://www.omg.org/spec/SysML/20250201/Identified",
      "$comment": "https://www.omg.org/spec/SysML/20250201/RequirementUsage"
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
    "verifiedRequirement": {
      "$ref": "https://www.omg.org/spec/SysML/20250201/Identified",
      "$comment": "https://www.omg.org/spec/SysML/20250201/RequirementUsage"
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
    "ownedConstraint",
    "ownedElement",
    "ownedMemberElement",
    "ownedMemberElementId",
    "ownedMemberFeature",
    "ownedMemberName",
    "ownedMemberShortName",
    "ownedRelatedElement",
    "ownedRelationship",
    "ownedRequirement",
    "owner",
    "owningMembership",
    "owningNamespace",
    "owningRelatedElement",
    "owningRelationship",
    "owningType",
    "qualifiedName",
    "referencedConstraint",
    "relatedElement",
    "shortName",
    "source",
    "target",
    "textualRepresentation",
    "verifiedRequirement",
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
