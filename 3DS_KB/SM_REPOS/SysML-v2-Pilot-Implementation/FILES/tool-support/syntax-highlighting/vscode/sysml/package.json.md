# OFFICIAL REPOSITORY FILE: SysML-v2-Pilot-Implementation/tool-support/syntax-highlighting/vscode/sysml/package.json

- repository: `SysML-v2-Pilot-Implementation`
- source_path: `tool-support/syntax-highlighting/vscode/sysml/package.json`
- source_url: https://github.com/Systems-Modeling/SysML-v2-Pilot-Implementation/blob/fa709f28dfd49dfdb7ee83e4e19da2f57e0eb3aa/tool-support/syntax-highlighting/vscode/sysml/package.json
- source_bytes: 658
- source_sha256: `89454e9ef315084ce8e3d484272b029468305686286a1de6420cc82a1792e922`
- decoded_as: `utf-8`


## EXACT SOURCE

````json
{
    "name": "sysml",
    "displayName": "SysML",
    "description": "OMG Systems Modeling Language",
    "version": "0.0.1",
    "engines": {
        "vscode": "^1.45.0"
    },
    "categories": [
        "Programming Languages"
    ],
    "contributes": {
        "languages": [{
            "id": "sysml",
            "aliases": ["sysml", "SysML"],
            "extensions": [".sysml"],
            "configuration": "./language-configuration.json"
        }],
        "grammars": [{
            "language": "sysml",
            "scopeName": "source.sysml",
            "path": "./syntaxes/sysml.tmLanguage.json"
        }]
    }
}
````
