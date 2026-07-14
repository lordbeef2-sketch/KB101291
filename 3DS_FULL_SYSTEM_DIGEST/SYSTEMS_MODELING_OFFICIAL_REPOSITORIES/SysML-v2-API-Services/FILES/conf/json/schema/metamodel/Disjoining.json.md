# OFFICIAL REPOSITORY FILE: SysML-v2-API-Services/conf/json/schema/metamodel/Disjoining.json

- repository: `SysML-v2-API-Services`
- source_path: `conf/json/schema/metamodel/Disjoining.json`
- source_url: https://github.com/Systems-Modeling/SysML-v2-API-Services/blob/0af711b14bbcea7b240bb0a3a65817ae68302092/conf/json/schema/metamodel/Disjoining.json
- source_bytes: 6982
- source_sha256: `9cd87ef43794751e97d869101f554993ce204f7b0a3e4b48b9d243c838aa807e`
- decoded_as: `utf-8`


## EXACT SOURCE

````json
{
  "$schema": "https://json-schema.org/draft/2020-12/schema",
  "$id": "https://www.omg.org/spec/SysML/20250201/Disjoining",
  "title": "Disjoining",
  "type": "object",
  "properties": {
    "@id": {
      "type": "string",
      "format": "uuid"
    },
    "@type": {
      "type": "string",
      "const": "Disjoining"
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
    "disjoiningType": {
      "$ref": "https://www.omg.org/spec/SysML/20250201/Identified",
      "$comment": "https://www.omg.org/spec/SysML/20250201/Type"
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
    "owningType": {
      "oneOf": [
        {
          "$ref": "https://www.omg.org/spec/SysML/20250201/Identified",
          "$comment": "https://www.omg.org/spec/SysML/20250201/Type"
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
    "typeDisjoined": {
      "$ref": "https://www.omg.org/spec/SysML/20250201/Identified",
      "$comment": "https://www.omg.org/spec/SysML/20250201/Type"
    }
  },
  "required": [
    "@id",
    "@type",
    "aliasIds",
    "declaredName",
    "declaredShortName",
    "disjoiningType",
    "documentation",
    "elementId",
    "isImplied",
    "isImpliedIncluded",
    "isLibraryElement",
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
    "owningType",
    "qualifiedName",
    "relatedElement",
    "shortName",
    "source",
    "target",
    "textualRepresentation",
    "typeDisjoined"
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
    }
  }
}
````
