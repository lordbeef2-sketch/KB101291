# OFFICIAL REPOSITORY FILE: SysML-v2-API-Services/conf/json/schema/api/ExternalRelationship.json

- repository: `SysML-v2-API-Services`
- source_path: `conf/json/schema/api/ExternalRelationship.json`
- source_url: https://github.com/Systems-Modeling/SysML-v2-API-Services/blob/0af711b14bbcea7b240bb0a3a65817ae68302092/conf/json/schema/api/ExternalRelationship.json
- source_bytes: 1561
- source_sha256: `87ef5021a27b644bad8a863eb8e407062c88f4529bef6f050f891af1a0aedecc`
- decoded_as: `utf-8`


## EXACT SOURCE

````json
{
  "$schema": "https://json-schema.org/draft/2020-12/schema",
  "$id": "https://www.omg.org/spec/SystemsModelingAPI/20230201/ExternalRelationship",
  "type": "object",
  "properties": {
    "@id": {
      "type": "string",
      "format": "uuid"
    },
    "@type": {
      "type": "string",
      "const": "ExternalRelationship"
    },
    "elementEnd": {
      "$ref": "https://www.omg.org/spec/SysML/20230201/Identified",
      "$comment": "https://www.omg.org/spec/SysML/20230201/Element"
    },
    "externalDataEnd": {
      "$ref": "https://www.omg.org/spec/SysML/20230201/Identified",
      "$comment": "https://www.omg.org/spec/SystemsModelingAPI/20230201/ExternalData"
    },
    "language": {
      "oneOf": [
        {
          "type": "string"
        },
        {
          "type": "null"
        }
      ]
    },
    "specification": {
      "oneOf": [
        {
          "type": "string"
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
    "elementEnd",
    "externalDataEnd",
    "language",
    "specification"
  ],
  "additionalProperties": false,
  "$defs": {
    "Identified": {
      "$id": "https://www.omg.org/spec/SysML/20230201/Identified",
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
