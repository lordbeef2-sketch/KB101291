# OFFICIAL REPOSITORY FILE: SysML-v2-Release/kerml/src/examples/Simple Tests/Expansion.kerml

- repository: `SysML-v2-Release`
- source_path: `kerml/src/examples/Simple Tests/Expansion.kerml`
- source_url: https://github.com/Systems-Modeling/SysML-v2-Release/blob/288d129c0d532065d45434bbb48a920898b719af/kerml/src/examples/Simple Tests/Expansion.kerml
- source_bytes: 115
- source_sha256: `ad0b0c916c227753fa4473212c9ac884dbd941d882322331d70bf3b998d6106f`
- decoded_as: `utf-8`


## EXACT SOURCE

````kerml
package Expansion {
	private import ControlFunctions::select;
	feature x = x->select {in y; in w; in z; w+1}; 
}
````
