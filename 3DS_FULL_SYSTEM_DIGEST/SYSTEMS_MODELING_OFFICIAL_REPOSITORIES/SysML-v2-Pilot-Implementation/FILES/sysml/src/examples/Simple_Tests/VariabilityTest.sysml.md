# OFFICIAL REPOSITORY FILE: SysML-v2-Pilot-Implementation/sysml/src/examples/Simple Tests/VariabilityTest.sysml

- repository: `SysML-v2-Pilot-Implementation`
- source_path: `sysml/src/examples/Simple Tests/VariabilityTest.sysml`
- source_url: https://github.com/Systems-Modeling/SysML-v2-Pilot-Implementation/blob/fa709f28dfd49dfdb7ee83e4e19da2f57e0eb3aa/sysml/src/examples/Simple Tests/VariabilityTest.sysml
- source_bytes: 629
- source_sha256: `ef1456b8fad56830143f14238fcab639985438d8b87756dc2b1856c2ac522d0d`
- decoded_as: `utf-8`


## EXACT SOURCE

````sysml
package VariabilityTest {
	part def P {
		attribute a;
	}
	
	part def Q :> P;
	attribute def B;
	variation part def V :> P {
		variant part x : Q {
			attribute b : B :>> a;
		}
	}
	
	part q : Q;
	variation part v : P {
		variant q {
			attribute b : B :>> a;
		}
	}
	
	part y : P = v::q;
	
	variation action def A {
		variant action a1;
		variant action a2;
	}
	
	variation use case uc1 {
    	variant use case uc11;
    	variant use case uc12;
    }

    variation analysis a1;
    
    variation verification v1;
    
    variation requirement r {
    	variant requirement r1;
    }
	
}
````
