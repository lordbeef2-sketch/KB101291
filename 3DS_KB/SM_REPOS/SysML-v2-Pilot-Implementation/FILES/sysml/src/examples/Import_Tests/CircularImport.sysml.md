# OFFICIAL REPOSITORY FILE: SysML-v2-Pilot-Implementation/sysml/src/examples/Import Tests/CircularImport.sysml

- repository: `SysML-v2-Pilot-Implementation`
- source_path: `sysml/src/examples/Import Tests/CircularImport.sysml`
- source_url: https://github.com/Systems-Modeling/SysML-v2-Pilot-Implementation/blob/fa709f28dfd49dfdb7ee83e4e19da2f57e0eb3aa/sysml/src/examples/Import Tests/CircularImport.sysml
- source_bytes: 372
- source_sha256: `3ed6813e219e43b737251c69aaa421d0e993219cbf35d3f78819de8b6eef70d4`
- decoded_as: `utf-8`


## EXACT SOURCE

````sysml
package CircularImport {

	package P1 {
		public import P2::*;
		part def A;
	}
	package P2 {
		public import P1::*;
		part def B;
	}
	package Test1 {
		public import P1::*;
		part x: A;
		part y: B;
	}
	package Test2 {
		public import P2::*;
		part x: A;
		part y: B;
	}
	
	part x: P1::A;
	
	// The following should not fail.
	part y: P1::B;
	
}
````
