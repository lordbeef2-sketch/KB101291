# OFFICIAL REPOSITORY FILE: SysML-v2-Pilot-Implementation/sysml/src/examples/Import Tests/QualifiedNameImportTest.sysml

- repository: `SysML-v2-Pilot-Implementation`
- source_path: `sysml/src/examples/Import Tests/QualifiedNameImportTest.sysml`
- source_url: https://github.com/Systems-Modeling/SysML-v2-Pilot-Implementation/blob/fa709f28dfd49dfdb7ee83e4e19da2f57e0eb3aa/sysml/src/examples/Import Tests/QualifiedNameImportTest.sysml
- source_bytes: 242
- source_sha256: `2720d3539f24ebfc294bec9dad4c7537af099e46df8b02b31a197aca51d7a1ed`
- decoded_as: `utf-8`


## EXACT SOURCE

````sysml
package QualifiedNameImportTest {
	package P1 {
		part def A;
	}
	package P2 {
		package P2a {
			public import P1::*;
		}
		// The following should not fail.
		// A is a member of P2a because of the import.
		part x: P2a::A;
	}
}
````
