# OFFICIAL REPOSITORY FILE: SysML-v2-Release/sysml/src/training/34. Verification/Verification Case Usage Example.sysml

- repository: `SysML-v2-Release`
- source_path: `sysml/src/training/34. Verification/Verification Case Usage Example.sysml`
- source_url: https://github.com/Systems-Modeling/SysML-v2-Release/blob/288d129c0d532065d45434bbb48a920898b719af/sysml/src/training/34. Verification/Verification Case Usage Example.sysml
- source_bytes: 1228
- source_sha256: `c1775be385c07c9a1b3cb1734204308099b072bd2c6b61a2d0fc608324210c93`
- decoded_as: `utf-8`


## EXACT SOURCE

````sysml
package 'Verification Case Usage Example' {
	private import 'Verification Case Definition Example'::*;
	
	part def MassVerificationSystem;
	part def Scale;
	
	part vehicleTestConfig : Vehicle {
		// ...
	}
	
	verification vehicleMassTest : VehicleMassTest {
		subject testVehicle :> vehicleTestConfig;
	}
	
	part massVerificationSystem : MassVerificationSystem {
		perform vehicleMassTest;
		
		part scale : Scale {
			perform vehicleMassTest.collectData {
				in part :>> testVehicle;
				
				// In reality, this would be some more involved process.
				measurement = testVehicle.mass;
				
				out :>> massMeasured = measurement;
			}
		}
	}		
		
	individual def TestSystem :> MassVerificationSystem;
	
	individual def TestVehicle1 :> Vehicle;
	individual def TestVehicle2 :> Vehicle;

	individual testSystem : TestSystem :> massVerificationSystem {
		timeslice test1 {
			perform action :>> vehicleMassTest {
				in individual :>> testVehicle : TestVehicle1 {
					:>> mass = 2500[SI::kg];
				}
			}
		}
		
		then timeslice test2 {
			perform action :>> vehicleMassTest {
				in individual :>> testVehicle : TestVehicle2 {
					:>> mass = 3000[SI::kg];
				}
			}
		}
	}
}
````
