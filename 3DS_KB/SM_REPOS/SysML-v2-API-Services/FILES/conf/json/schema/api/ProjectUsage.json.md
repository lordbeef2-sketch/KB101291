# OFFICIAL REPOSITORY FILE: SysML-v2-API-Services/conf/json/schema/api/ProjectUsage.json

- repository: `SysML-v2-API-Services`
- source_path: `conf/json/schema/api/ProjectUsage.json`
- source_url: https://github.com/Systems-Modeling/SysML-v2-API-Services/blob/0af711b14bbcea7b240bb0a3a65817ae68302092/conf/json/schema/api/ProjectUsage.json
- source_bytes: 1194
- source_sha256: `9939e5d6dcd93416348660638fade0c3cfae32dcb4b7e1a0ef51ea47b1108e7e`
- decoded_as: `utf-8`


## EXACT SOURCE

````json
{
  "$schema": "https://json-schema.org/draft/2020-12/schema",
  "$id": "https://www.omg.org/spec/SystemsModelingAPI/20230201/ProjectUsage",
  "type": "object",
  "properties": {
    "@id": {
      "type": "string",
      "format": "uuid"
    },
    "@type": {
      "type": "string",
      "const": "ProjectUsage"
    },
    "usedCommit": {
      "$ref": "https://www.omg.org/spec/SysML/20230201/Identified",
      "$comment": "https://www.omg.org/spec/SystemsModelingAPI/20230201/Commit"
    },
    "usedProject": {
      "$ref": "https://www.omg.org/spec/SysML/20230201/Identified",
      "$comment": "https://www.omg.org/spec/SystemsModelingAPI/20230201/Project"
    }
  },
  "required": [
    "@id",
    "@type",
    "usedCommit",
    "usedProject"
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
