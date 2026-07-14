# OFFICIAL REPOSITORY FILE: SysML-v2-Release/kerml/src/examples/Simple Tests/Circular.kerml

- repository: `SysML-v2-Release`
- source_path: `kerml/src/examples/Simple Tests/Circular.kerml`
- source_url: https://github.com/Systems-Modeling/SysML-v2-Release/blob/288d129c0d532065d45434bbb48a920898b719af/kerml/src/examples/Simple Tests/Circular.kerml
- source_bytes: 183
- source_sha256: `823e6b6b459cb841fa50da55b6505d8ffad2368cd3e9cb91425131e487b1762b`
- decoded_as: `utf-8`


## EXACT SOURCE

````kerml
package Circular {
	class A { }
	feature a: A;
	alias Circ for Circular;
	package P {
		public import Circular::*;
	}
	
	feature x :> z;
	feature y :> x;
	feature z :> y;
}
````
