# OFFICIAL REPOSITORY FILE: SysML-v2-Pilot-Implementation/kerml/src/examples/Simple Tests/FeatureInheritance.kerml

- repository: `SysML-v2-Pilot-Implementation`
- source_path: `kerml/src/examples/Simple Tests/FeatureInheritance.kerml`
- source_url: https://github.com/Systems-Modeling/SysML-v2-Pilot-Implementation/blob/fa709f28dfd49dfdb7ee83e4e19da2f57e0eb3aa/kerml/src/examples/Simple Tests/FeatureInheritance.kerml
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
