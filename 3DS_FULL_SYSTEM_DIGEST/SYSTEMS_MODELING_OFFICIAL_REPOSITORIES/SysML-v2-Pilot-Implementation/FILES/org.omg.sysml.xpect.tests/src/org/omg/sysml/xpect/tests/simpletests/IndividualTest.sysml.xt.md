# OFFICIAL REPOSITORY FILE: SysML-v2-Pilot-Implementation/org.omg.sysml.xpect.tests/src/org/omg/sysml/xpect/tests/simpletests/IndividualTest.sysml.xt

- repository: `SysML-v2-Pilot-Implementation`
- source_path: `org.omg.sysml.xpect.tests/src/org/omg/sysml/xpect/tests/simpletests/IndividualTest.sysml.xt`
- source_url: https://github.com/Systems-Modeling/SysML-v2-Pilot-Implementation/blob/fa709f28dfd49dfdb7ee83e4e19da2f57e0eb3aa/org.omg.sysml.xpect.tests/src/org/omg/sysml/xpect/tests/simpletests/IndividualTest.sysml.xt
- source_bytes: 1592
- source_sha256: `43a75b718a86581ee312b4b9657b50c2b4b2b9f5c8c3bf35917245c263a75a47`
- decoded_as: `utf-8`


## EXACT SOURCE

````xtext
//* 
XPECT_SETUP org.omg.sysml.xpect.tests.simpletests.SysMLTests
	ResourceSet {
		ThisFile {}
		File {from ="/library.kernel/Base.kerml"}
       	File {from ="/library.kernel/Occurrences.kerml"}
       	File {from ="/library.kernel/Objects.kerml"}
       	File {from ="/library.kernel/Performances.kerml"}
 		File {from ="/library.systems/Items.sysml"}
 		File {from ="/library.systems/Parts.sysml"}
 		File {from ="/library.systems/Actions.sysml"}
	}
	Workspace {
		JavaProject {
			SrcFolder {
				ThisFile {}
				File {from ="/library.kernel/Base.kerml"}
		       	File {from ="/library.kernel/Occurrences.kerml"}
		       	File {from ="/library.kernel/Objects.kerml"}
		       	File {from ="/library.kernel/Performances.kerml"}
				File {from ="/library.systems/Items.sysml"}
				File {from ="/library.systems/Parts.sysml"}
 				File {from ="/library.systems/Actions.sysml"}
			}
		}
	}
END_SETUP 
*/
// XPECT noErrors ---> ""
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
