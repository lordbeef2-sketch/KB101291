# OFFICIAL REPOSITORY FILE: SysML-v2-Pilot-Implementation/org.omg.sysml/json-schema/ModelInterchange.json

- repository: `SysML-v2-Pilot-Implementation`
- source_path: `org.omg.sysml/json-schema/ModelInterchange.json`
- source_url: https://github.com/Systems-Modeling/SysML-v2-Pilot-Implementation/blob/fa709f28dfd49dfdb7ee83e4e19da2f57e0eb3aa/org.omg.sysml/json-schema/ModelInterchange.json
- source_bytes: 2508
- source_sha256: `3faf47a07dce7b93c17a91942050d73d72d204d11d38a2574b452a98d2034c15`
- decoded_as: `utf-8`


## EXACT SOURCE

````json
{
  "$schema": "https://json-schema.org/draft/2020-12/schema",
  "$defs": {
    "Project": {
      "$id": "https://www.omg.org/spec/KerML/20240201/Project",
      "title": "Project",
      "type": "object",
      "properties": {
        "name": {
          "type": "string"
        },
        "description": {
          "type": "string"
        },
        "version": {
          "type": "string"
        },
        "license": {
          "type": "string"
        },
        "maintainer": {
          "type": "array",
          "items": {
            "type": "string"
          }
        },
        "website": {
          "type": "string",
          "format": "iri"
        },
        "topic": {
          "type": "array",
          "items": {
            "type": "string"
          }
        },
        "usage": {
          "type": "array",
          "items": {
            "type": "object",
            "properties": {
              "resource": {
                "type": "string",
                "format": "iri"
              },
              "versionConstraint": {
                "type": "string"
              }
            },
            "required": [
              "resource"
            ]
          }
        }
      },
      "required": [
        "name",
        "version"
      ]
    },
    "Meta": {
      "$id": "https://www.omg.org/spec/KerML/20240201/Meta",
      "title": "Meta",
      "type": "object",
      "properties": {
        "index": {
          "type": "object",
          "additionalProperties": {
            "type": "string"
          }
        },
        "created": {
          "type": "string",
          "format": "date-time"
        },
        "metamodel": {
          "type": "string",
          "format": "iri"
        },
        "includesDerived": {
          "type": "boolean"
        },
        "includesImplied": {
          "type": "boolean"
        },
        "checksum": {
          "type": "object",
          "additionalProperties": {
            "type": "object",
            "properties": {
              "value": {
                "type": "string"
              },
              "algorithm": {
                "type": "string"
              }
            },
            "required": [
              "value",
              "algorithm"
            ]
          }
        }
      },
      "required": [
        "index",
        "created"
      ]
    }
  }
}
````
