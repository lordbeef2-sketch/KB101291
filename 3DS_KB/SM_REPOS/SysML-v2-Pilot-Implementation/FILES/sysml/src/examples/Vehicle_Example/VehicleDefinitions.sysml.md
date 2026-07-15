# OFFICIAL REPOSITORY FILE: SysML-v2-Pilot-Implementation/sysml/src/examples/Vehicle Example/VehicleDefinitions.sysml

- repository: `SysML-v2-Pilot-Implementation`
- source_path: `sysml/src/examples/Vehicle Example/VehicleDefinitions.sysml`
- source_url: https://github.com/Systems-Modeling/SysML-v2-Pilot-Implementation/blob/fa709f28dfd49dfdb7ee83e4e19da2f57e0eb3aa/sysml/src/examples/Vehicle Example/VehicleDefinitions.sysml
- source_bytes: 1104
- source_sha256: `6e6128a4dda956ba8eafda11f2d961fe77eb98ed3001d4befd609ab4559c67ba`
- decoded_as: `utf-8`


## EXACT SOURCE

````sysml
package VehicleDefinitions {
	doc
	/*
	 * Example vehicle definitions model.
	 */

	private import ScalarValues::*;
	private import Quantities::*;
	private import MeasurementReferences::*;
	private import ISQ::*;
	private import SI::*;
	
	/* PART DEFINITIONS */
	
	part def Vehicle {
		attribute mass :> ISQ::mass;
	}
	part def Transmission;	
	part def AxleAssembly;
	part def Axle {
		port leftMountingPoint: AxleMountIF;
		port rightMountingPoint: AxleMountIF;
	}
	part def Wheel {
		port hub: WheelHubIF;
	}
	part def Lugbolt {
		attribute tighteningTorque :> ISQ::torque;
	}
	
	/* PORT DEFINITIONS */
	
	port def DriveIF { 
		in driveTorque :> ISQ::torque;
	}
	
	port def AxleMountIF { 
		out transferredTorque :> ISQ::torque;
	}
	
	port def WheelHubIF { 
		in appliedTorque :> ISQ::torque;
	}
	
	/* INTERFACE DEFINITIONS */
	
	interface def Mounting {
		doc /* The definition of the interface for mounting a Wheel to an Axle. */
		end axleMount: AxleMountIF;
		end hub: WheelHubIF;
		
		flow axleMount.transferredTorque to hub.appliedTorque;
	}
}
````
