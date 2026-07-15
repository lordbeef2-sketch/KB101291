# OFFICIAL REPOSITORY FILE: SysML-v2-Pilot-Implementation/tool-support/syntax-highlighting/vscode/kerml/package.json

- repository: `SysML-v2-Pilot-Implementation`
- source_path: `tool-support/syntax-highlighting/vscode/kerml/package.json`
- source_url: https://github.com/Systems-Modeling/SysML-v2-Pilot-Implementation/blob/fa709f28dfd49dfdb7ee83e4e19da2f57e0eb3aa/tool-support/syntax-highlighting/vscode/kerml/package.json
- source_bytes: 657
- source_sha256: `7a85fff7943b1d050c3751d97259165e8864c3afcbe1ab4c62e13fc554861cf7`
- decoded_as: `utf-8`


## EXACT SOURCE

````json
{
    "name": "kerml",
    "displayName": "KerML",
    "description": "OMG Kernel Modeling Language",
    "version": "0.0.1",
    "engines": {
        "vscode": "^1.45.0"
    },
    "categories": [
        "Programming Languages"
    ],
    "contributes": {
        "languages": [{
            "id": "kerml",
            "aliases": ["kerml", "KerML"],
            "extensions": [".kerml"],
            "configuration": "./language-configuration.json"
        }],
        "grammars": [{
            "language": "kerml",
            "scopeName": "source.kerml",
            "path": "./syntaxes/kerml.tmLanguage.json"
        }]
    }
}
````
