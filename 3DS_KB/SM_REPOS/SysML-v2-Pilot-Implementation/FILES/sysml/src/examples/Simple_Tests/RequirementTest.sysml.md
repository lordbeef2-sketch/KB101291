# OFFICIAL REPOSITORY FILE: SysML-v2-Pilot-Implementation/sysml/src/examples/Simple Tests/RequirementTest.sysml

- repository: `SysML-v2-Pilot-Implementation`
- source_path: `sysml/src/examples/Simple Tests/RequirementTest.sysml`
- source_url: https://github.com/Systems-Modeling/SysML-v2-Pilot-Implementation/blob/fa709f28dfd49dfdb7ee83e4e19da2f57e0eb3aa/sysml/src/examples/Simple Tests/RequirementTest.sysml
- source_bytes: 506
- source_sha256: `6cc840f6f9b4d01ca16aefddb9dee4d7b4f49bc60af89787cc9dcc7303b3b186`
- decoded_as: `utf-8`


## EXACT SOURCE

````sysml
package RequirementTest {
	constraint def C;
	constraint c : C;
	private import q::**;
	requirement def R {
		assume constraint c1 : C;
		require c;
		doc /* */
    	requirement;
    	requirement def <'1'> A {
    		doc /* Text */
    		subject s;
    	}
	}
	requirement def R1 {
		require constraint c1 :>> c;
	}
	part p;
	part q {
		requirement r : R;
		satisfy r by p;
		assert satisfy r by q;
	}
	
	requirement r1 : R1;
	not satisfy r1 by p;
	assert not satisfy r1 by q;
	
}
````
