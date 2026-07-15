# OFFICIAL REPOSITORY FILE: SysML-v2-Pilot-Implementation/org.omg.sysml.xpect.tests/src/org/omg/sysml/xpect/tests/validation/valid/IndividualUsage.sysml.xt

- repository: `SysML-v2-Pilot-Implementation`
- source_path: `org.omg.sysml.xpect.tests/src/org/omg/sysml/xpect/tests/validation/valid/IndividualUsage.sysml.xt`
- source_url: https://github.com/Systems-Modeling/SysML-v2-Pilot-Implementation/blob/fa709f28dfd49dfdb7ee83e4e19da2f57e0eb3aa/org.omg.sysml.xpect.tests/src/org/omg/sysml/xpect/tests/validation/valid/IndividualUsage.sysml.xt
- source_bytes: 2133
- source_sha256: `c7e3740859d18c65ac27392ccf6ee6d7e1bcf81bd419af572b5efb89ce3a4306`
- decoded_as: `utf-8`


## EXACT SOURCE

````xtext
//* 
XPECT_SETUP org.omg.sysml.xpect.tests.validation.valid.SysMLTests
	ResourceSet {
		ThisFile {}
		File {from ="/library.kernel/Base.kerml"}
		File {from ="/library.kernel/Links.kerml"}
		File {from ="/library.kernel/Occurrences.kerml"}
		File {from ="/library.kernel/Objects.kerml"}
		File {from ="/library.kernel/Performances.kerml"}
		File {from ="/library.kernel/BaseFunctions.kerml"}
		File {from ="/library.kernel/ScalarValues.kerml"}
		File {from ="/library.kernel/ScalarFunctions.kerml"}
		File {from ="/library.systems/Items.sysml"}
		File {from ="/library.systems/Parts.sysml"}
		File {from ="/library.systems/Ports.sysml"}
		File {from ="/library.domain/Quantities and Units/ISQ.sysml"}
		File {from ="/library.domain/Quantities and Units/SI.sysml"}
		

	}
	Workspace {
		JavaProject {
			SrcFolder {
				ThisFile {}
				File {from ="/library.kernel/Base.kerml"}
				File {from ="/library.kernel/Links.kerml"}
		       	File {from ="/library.kernel/Occurrences.kerml"}
				File {from ="/library.kernel/Objects.kerml"}
				File {from ="/library.kernel/Performances.kerml"}
				File {from ="/library.kernel/BaseFunctions.kerml"}
				File {from ="/library.kernel/ScalarValues.kerml"}
				File {from ="/library.kernel/ScalarFunctions.kerml"}
				File {from ="/library.systems/Items.sysml"}
				File {from ="/library.systems/Parts.sysml"}
				File {from ="/library.systems/Ports.sysml"}
				File {from ="/library.domain/Quantities and Units/ISQ.sysml"}
				File {from ="/library.domain/Quantities and Units/SI.sysml"}
			}
		}
	}
END_SETUP 
*/
// XPECT noErrors ---> ""
package IndividualUsage_Valid {
	part def Vehicle;	
	part def Wheel;
	
	individual def Vehicle_1 :> Vehicle {
		part leftFrontWheel : Wheel;
		part rightFrontWheel : Wheel;
	}
	
	individual def Wheel_1 :> Wheel;
	
	individual vehicle_1 : Vehicle_1 {
		snapshot vehicle_1_t0 {
			individual leftFrontWheel_t0 : Wheel_1 :>> leftFrontWheel;
		}
		
		timeslice vehicle_1_t1 {
			individual rightFrontWheel_t1 : Wheel_1 :>> rightFrontWheel;
		}
		
		first vehicle_1_t0 then vehicle_1_t1;
	}
}

````
