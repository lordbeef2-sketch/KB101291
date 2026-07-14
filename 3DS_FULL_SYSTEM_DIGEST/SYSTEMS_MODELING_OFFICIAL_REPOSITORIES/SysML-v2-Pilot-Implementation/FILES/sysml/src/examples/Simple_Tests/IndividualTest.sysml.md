# OFFICIAL REPOSITORY FILE: SysML-v2-Pilot-Implementation/sysml/src/examples/Simple Tests/IndividualTest.sysml

- repository: `SysML-v2-Pilot-Implementation`
- source_path: `sysml/src/examples/Simple Tests/IndividualTest.sysml`
- source_url: https://github.com/Systems-Modeling/SysML-v2-Pilot-Implementation/blob/fa709f28dfd49dfdb7ee83e4e19da2f57e0eb3aa/sysml/src/examples/Simple Tests/IndividualTest.sysml
- source_bytes: 631
- source_sha256: `0919b61e25d3d6d10901aa95f6b7cff5ffe19519dd911d924a080d2895a05b9c`
- decoded_as: `utf-8`


## EXACT SOURCE

````sysml
package IndividualTest {
	individual def IO1;
	individual occurrence def IO2 {
		individual io : IO1;
	}
	
	individual item def II1 {
		individual item ii : II1;
	}
	
	item def I {
		part i : I;
	}
	individual item def II2 :> I {
		individual item :>> i : II2;
	}
	
	individual part def IP1 {
		individual part p : IP1;
	}
	
	part def P {
		part p : P;
	}
	individual part def IP2 :> P {
		individual part :>> p : IP2;
	}
	
	individual action def AP1 {
		individual action a : AP1;
	}
	
	action def A {
		action a : A;
	}
	individual action def IA2 :> A {
		individual action :>> a : IA2;
	}
}
````
