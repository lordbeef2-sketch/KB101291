# OFFICIAL REPOSITORY FILE: SysML-v2-Release/kerml/src/examples/Simple Tests/FeatureInheritance.kerml

- repository: `SysML-v2-Release`
- source_path: `kerml/src/examples/Simple Tests/FeatureInheritance.kerml`
- source_url: https://github.com/Systems-Modeling/SysML-v2-Release/blob/288d129c0d532065d45434bbb48a920898b719af/kerml/src/examples/Simple Tests/FeatureInheritance.kerml
- source_bytes: 108
- source_sha256: `86b9e1e8ad5e8eacef5e5576d727c722d4414bbf38fe9181d215aff4a3ad1bbe`
- decoded_as: `utf-8`


## EXACT SOURCE

````kerml
package FeatureInheritance {
	feature s {
		feature t : ISQ::TorqueValue;
	}
	
	feature u subsets s;
}
````
