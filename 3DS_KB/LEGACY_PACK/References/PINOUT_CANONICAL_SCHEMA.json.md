# LEGACY SOURCE RECORD: References/PINOUT_CANONICAL_SCHEMA.json

<!--LEGACY_SOURCE path=References/PINOUT_CANONICAL_SCHEMA.json sha256=17caf68e56785cdf951d3de0b76a64ace834c8c6b382f0391f17ea9d7175c57f bytes=1357 -->

- original_path: `References/PINOUT_CANONICAL_SCHEMA.json`
- original_sha256: `17caf68e56785cdf951d3de0b76a64ace834c8c6b382f0391f17ea9d7175c57f`
- original_bytes: 1357

````json
{
  "$schema": "https://json-schema.org/draft/2020-12/schema",
  "title": "Canonical Pinout Row",
  "type": "object",
  "required": [
    "interface_id",
    "interface_name",
    "source_system",
    "source_connector",
    "source_pin",
    "dest_system",
    "dest_connector",
    "dest_pin",
    "signal_name",
    "direction",
    "revision",
    "source_doc_ref"
  ],
  "properties": {
    "interface_id": { "type": "string" },
    "interface_name": { "type": "string" },
    "source_system": { "type": "string" },
    "source_element": { "type": "string" },
    "source_connector": { "type": "string" },
    "source_pin": { "type": "string" },
    "dest_system": { "type": "string" },
    "dest_element": { "type": "string" },
    "dest_connector": { "type": "string" },
    "dest_pin": { "type": "string" },
    "signal_name": { "type": "string" },
    "signal_type": { "type": "string" },
    "direction": {
      "type": "string",
      "enum": ["source-to-dest", "dest-to-source", "bidirectional", "n/a"]
    },
    "protocol_layer": { "type": "string" },
    "electrical_limits": { "type": "string" },
    "wire_color_or_id": { "type": "string" },
    "shield_drain": { "type": "string" },
    "revision": { "type": "string" },
    "source_doc_ref": { "type": "string" },
    "notes": { "type": "string" }
  },
  "additionalProperties": false
}
````
