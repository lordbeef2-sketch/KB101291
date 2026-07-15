# OFFICIAL REPOSITORY FILE: SysML-v2-API-Services/conf/json/schema/metamodel/Identified.json

- repository: `SysML-v2-API-Services`
- source_path: `conf/json/schema/metamodel/Identified.json`
- source_url: https://github.com/Systems-Modeling/SysML-v2-API-Services/blob/0af711b14bbcea7b240bb0a3a65817ae68302092/conf/json/schema/metamodel/Identified.json
- source_bytes: 339
- source_sha256: `71d22b2809a5f0c53254ca337a16fd184700c05e66cfa75183d8b509c6b485e3`
- decoded_as: `utf-8`


## EXACT SOURCE

````json
{
  "$schema": "https://json-schema.org/draft/2020-12/schema",
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
````
