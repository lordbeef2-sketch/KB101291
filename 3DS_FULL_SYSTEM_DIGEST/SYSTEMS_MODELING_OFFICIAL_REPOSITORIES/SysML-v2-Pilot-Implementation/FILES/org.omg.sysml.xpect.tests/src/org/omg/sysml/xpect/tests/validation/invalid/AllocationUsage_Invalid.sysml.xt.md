# OFFICIAL REPOSITORY FILE: SysML-v2-Pilot-Implementation/org.omg.sysml.xpect.tests/src/org/omg/sysml/xpect/tests/validation/invalid/AllocationUsage_Invalid.sysml.xt

- repository: `SysML-v2-Pilot-Implementation`
- source_path: `org.omg.sysml.xpect.tests/src/org/omg/sysml/xpect/tests/validation/invalid/AllocationUsage_Invalid.sysml.xt`
- source_url: https://github.com/Systems-Modeling/SysML-v2-Pilot-Implementation/blob/fa709f28dfd49dfdb7ee83e4e19da2f57e0eb3aa/org.omg.sysml.xpect.tests/src/org/omg/sysml/xpect/tests/validation/invalid/AllocationUsage_Invalid.sysml.xt
- source_bytes: 1873
- source_sha256: `80021255d9b1fdafe6e33c3a5e858f22055c740362fc4636aff52e750647fb88`
- decoded_as: `utf-8`


## EXACT SOURCE

````xtext
//*
XPECT_SETUP org.omg.sysml.xpect.tests.validation.invalid.SysMLTests
	ResourceSet {
		ThisFile {}
		File {from ="/library.kernel/Base.kerml"}
		File {from ="/library.kernel/Occurrences.kerml"}
       	File {from ="/library.kernel/Objects.kerml"}
       	File {from ="/library.kernel/Performances.kerml"}
 		File {from ="/library.systems/Items.sysml"}
		File {from ="/library.systems/Parts.sysml"}
		File {from ="/library.systems/Ports.sysml"}
		File {from ="/library.systems/Connections.sysml"}
		File {from ="/library.systems/Allocations.sysml"}
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
				File {from ="/library.systems/Ports.sysml"}
				File {from ="/library.systems/Connections.sysml"}
				File {from ="/library.systems/Allocations.sysml"}
			}
		}
	}
END_SETUP 
*/
package P {
	part def P;	
	part def B;	
	part def C;	
	
	connection def BC1 {
		end : B[1];
		end : C[1];
	}
	allocation def BC2 {
		end : B[1];
		end : C[1];
	}
	part p : P {
		part b : B[1];
		part c: C[1];
		
		allocation bc : BC2 allocate b to c;
		
		// XPECT errors --> "An allocation must be typed by allocation definitions." at "allocation :P allocate b to c;"
		allocation :P allocate b to c;
		// XPECT errors --> "An allocation must be typed by allocation definitions." at "allocation :p allocate b to c;"
		allocation :p allocate b to c;
		// XPECT errors --> "An allocation must be typed by allocation definitions." at "allocation :BC1 allocate b to c;"
		allocation :BC1 allocate b to c;
	}
}


````
