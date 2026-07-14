# OFFICIAL REPOSITORY FILE: SysML-v2-Release/kerml/src/examples/Massed Thing Example/MassedThings.kerml

- repository: `SysML-v2-Release`
- source_path: `kerml/src/examples/Massed Thing Example/MassedThings.kerml`
- source_url: https://github.com/Systems-Modeling/SysML-v2-Release/blob/288d129c0d532065d45434bbb48a920898b719af/kerml/src/examples/Massed Thing Example/MassedThings.kerml
- source_bytes: 289
- source_sha256: `927ee7c24dac9f80d5be0e711eb4e60a6e0198d77375d9d8ab90f3e1f4fac331`
- decoded_as: `utf-8`


## EXACT SOURCE

````kerml
private import ScalarValues::*;
package MassedThings {
	
	public class MassedThing {
		public name: String;
		public mass: Real = 0;
	}
	
	public assoc MassedThingAssembly {
		public end [0..1] feature assembly: MassedThing;
		public end [0..*] feature parts: MassedThing;
	}
}
````
