# OFFICIAL REPOSITORY FILE: SysML-v2-Pilot-Implementation/tool-support/syntax-highlighting/vscode/sysml/language-configuration.json

- repository: `SysML-v2-Pilot-Implementation`
- source_path: `tool-support/syntax-highlighting/vscode/sysml/language-configuration.json`
- source_url: https://github.com/Systems-Modeling/SysML-v2-Pilot-Implementation/blob/fa709f28dfd49dfdb7ee83e4e19da2f57e0eb3aa/tool-support/syntax-highlighting/vscode/sysml/language-configuration.json
- source_bytes: 874
- source_sha256: `b69e88ac6e5fa5e88a3b9f1d2f15a7490f3e877c612b9cc2504c04ac2e54e20f`
- decoded_as: `utf-8`


## EXACT SOURCE

````json
{
    "comments": {
        // symbol used for single line comment. Remove this entry if your language does not support line comments
        "lineComment": "//",
        // symbols used for start and end a block comment. Remove this entry if your language does not support block comments
        "blockComment": [ "/*", "*/" ]
    },
    // symbols used as brackets
    "brackets": [
        ["{", "}"],
        ["@[", "]"],
        ["[", "]"],
        ["(", ")"]
    ],
    // symbols that are auto closed when typing
    "autoClosingPairs": [
        ["{", "}"],
        ["[", "]"],
        ["(", ")"],
        ["\"", "\""],
        ["'", "'"]
    ],
    // symbols that can be used to surround a selection
    "surroundingPairs": [
        ["{", "}"],
        ["[", "]"],
        ["(", ")"],
        ["\"", "\""],
        ["'", "'"]
    ]
}
````
