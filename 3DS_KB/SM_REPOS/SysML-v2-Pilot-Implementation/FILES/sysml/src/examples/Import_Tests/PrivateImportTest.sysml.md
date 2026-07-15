# OFFICIAL REPOSITORY FILE: SysML-v2-Pilot-Implementation/sysml/src/examples/Import Tests/PrivateImportTest.sysml

- repository: `SysML-v2-Pilot-Implementation`
- source_path: `sysml/src/examples/Import Tests/PrivateImportTest.sysml`
- source_url: https://github.com/Systems-Modeling/SysML-v2-Pilot-Implementation/blob/fa709f28dfd49dfdb7ee83e4e19da2f57e0eb3aa/sysml/src/examples/Import Tests/PrivateImportTest.sysml
- source_bytes: 591
- source_sha256: `5111a800ab20f0018277bef5b4ed9d055327d03ac8afbdea2c2d3e5713113007`
- decoded_as: `utf-8`


## EXACT SOURCE

````sysml
package PrivateImportTest {
	package P1 {
		part def A;
	}
	package P2 {
		private import P1::*;
	}

	part x: P1::A;
	
	public import P2::*;
	// This should fail.
	// A is not visible, because the import in P2 is private.
	// part y: A;
	// part y1: P2::A;
	
	package P3 {
		part def B;
	}
	
	private import P3::*;
	
	// This should not fail.
	// Private import only restricts visibility outside the package.
	part z: B;
	
	package P4 {
		public import all P2::*;
		
		// This should not fail because "import all" overrides private import.
		part z1: A;
	}	
}
````
