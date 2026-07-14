# OFFICIAL REPOSITORY FILE: SysML-v2-Release/kerml/src/examples/Vehicle Example/VehicleDefinitions.kerml

- repository: `SysML-v2-Release`
- source_path: `kerml/src/examples/Vehicle Example/VehicleDefinitions.kerml`
- source_url: https://github.com/Systems-Modeling/SysML-v2-Release/blob/288d129c0d532065d45434bbb48a920898b719af/kerml/src/examples/Vehicle Example/VehicleDefinitions.kerml
- source_bytes: 682
- source_sha256: `99abf64596a707b8f3bf893d81cdd23d3d9cd9a3ff14b3757951acae6a385e58`
- decoded_as: `utf-8`


## EXACT SOURCE

````kerml
package VehicleDefinitions {
	doc
	/*
	 * Example vehicle definitions model.
	 */

	
	/* BLOCKS */
	
	class Vehicle;	
	class Transmission;	
	class AxleAssembly;
	class Axle;	
	class Wheel;
	class Lugbolt {
		tighteningTorque[1] : ScalarValues::Real;
	}
	
	/* INTERFACE BLOCKS */
	
	class DriveIF { 
		in driveTorque: ScalarValues::Real;
	}
	
	class AxleMountIF { 
		out transferredTorque : ScalarValues::Real;
	}
	
	class WheelHubIF { 
		in appliedTorque : ScalarValues::Real;
	}
	
	/* ASSOCIATION BLOCKS */
	
	assoc Mounting {
		doc
		/*
		 *  mounting a Wheel to an Axle.
		 */
	
		end axleMount: AxleMountIF;
		end hub: WheelHubIF;
	}
}
````
