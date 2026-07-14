# LEGACY SOURCE RECORD: References/TWC_API_WORKFLOWS.json

<!--LEGACY_SOURCE path=References/TWC_API_WORKFLOWS.json sha256=491edeaa1c0eebdd9757fbc349d8a0552ef2e7e7e266b64379fc09ebd0f41b52 bytes=1029 -->

- original_path: `References/TWC_API_WORKFLOWS.json`
- original_sha256: `491edeaa1c0eebdd9757fbc349d8a0552ef2e7e7e266b64379fc09ebd0f41b52`
- original_bytes: 1029

````json
{
  "api_modes": {
    "inventory": {
      "use_when": [
        "Need project/resource listings",
        "Need user/role awareness",
        "Need repository metadata"
      ],
      "preferred_surface": "REST"
    },
    "linked_model_access": {
      "use_when": [
        "Need OSLC/AM-CM style linked data access",
        "Need interoperable model element references"
      ],
      "preferred_surface": "OSLC"
    },
    "simulation": {
      "use_when": [
        "Need server-side simulation-oriented workflows"
      ],
      "preferred_surface": "Simulation REST API"
    },
    "sysml_v2_service_flow": {
      "use_when": [
        "Need SysML v2 textual or graphical repository-oriented workflows",
        "Need CI/CD-like v2 automation"
      ],
      "preferred_surface": "SysML v2 API extensions in newer TWC line"
    }
  },
  "operator_questions": [
    "What exact version line is the server on?",
    "What is the auth method?",
    "What schema is expected downstream?",
    "Is read-only enough?"
  ]
}
````
