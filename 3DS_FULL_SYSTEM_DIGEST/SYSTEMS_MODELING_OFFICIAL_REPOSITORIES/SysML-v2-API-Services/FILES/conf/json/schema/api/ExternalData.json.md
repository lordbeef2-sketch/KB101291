# OFFICIAL REPOSITORY FILE: SysML-v2-API-Services/conf/json/schema/api/ExternalData.json

- repository: `SysML-v2-API-Services`
- source_path: `conf/json/schema/api/ExternalData.json`
- source_url: https://github.com/Systems-Modeling/SysML-v2-API-Services/blob/0af711b14bbcea7b240bb0a3a65817ae68302092/conf/json/schema/api/ExternalData.json
- source_bytes: 534
- source_sha256: `2b5fe29be0a237ed07d68ceef1e111d640c30715325e8d7846e070401f3484dd`
- decoded_as: `utf-8`


## EXACT SOURCE

````json
{
  "$schema": "https://json-schema.org/draft/2020-12/schema",
  "$id": "https://www.omg.org/spec/SystemsModelingAPI/20230201/ExternalData",
  "type": "object",
  "properties": {
    "@id": {
      "type": "string",
      "format": "uuid"
    },
    "@type": {
      "type": "string",
      "const": "ExternalData"
    },
    "resourceIdentifier": {
      "type": "string",
      "format": "uri"
    }
  },
  "required": [
    "@id",
    "@type",
    "resourceIdentifier"
  ],
  "additionalProperties": false
}
````
