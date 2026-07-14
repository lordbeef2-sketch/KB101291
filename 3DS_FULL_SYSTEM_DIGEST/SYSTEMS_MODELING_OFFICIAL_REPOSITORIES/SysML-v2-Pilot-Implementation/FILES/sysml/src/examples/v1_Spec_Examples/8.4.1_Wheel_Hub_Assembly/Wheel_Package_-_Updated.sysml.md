# OFFICIAL REPOSITORY FILE: SysML-v2-Pilot-Implementation/sysml/src/examples/v1 Spec Examples/8.4.1 Wheel Hub Assembly/Wheel Package - Updated.sysml

- repository: `SysML-v2-Pilot-Implementation`
- source_path: `sysml/src/examples/v1 Spec Examples/8.4.1 Wheel Hub Assembly/Wheel Package - Updated.sysml`
- source_url: https://github.com/Systems-Modeling/SysML-v2-Pilot-Implementation/blob/fa709f28dfd49dfdb7ee83e4e19da2f57e0eb3aa/sysml/src/examples/v1 Spec Examples/8.4.1 Wheel Hub Assembly/Wheel Package - Updated.sysml
- source_bytes: 1843
- source_sha256: `d103ec6fc1d4223e247abc4afac13626b00779ed548253a3155f1a99d752de94`
- decoded_as: `utf-8`


## EXACT SOURCE

````sysml
package 'Wheel Package - Updated' {
	doc
	/*
	 * Example from the SysML 1.6 spec, subclause 8.4.1 Wheel Hub Assembly.
	 */

	private import ISQ::*;
	
	// Quantities
	
	pressure = force / length^2; 
	
	// Blocks
	
	part def WheelHubAssembly;
	part def WheelAssembly {
		inflationPressure :> pressure;
	}
	
	part def Tire {
		tireSpecification : ScalarValues::String;		
		action mountTire; // Should be operation
	}
	
	part def TireBead;
	
	connection def PressureSeat {
		end : TireBead[1];
		end : TireMountingRim[1];
	}
	
	part def Wheel {
		diameter :> length;
		width :> length;		
	}
	
	connection def BandMount {
		end : Wheel[1];
		end : WirelessTirePressureMonitor[1];
	}
	
	part def WirelessTirePressureMonitor {
		action transmitPressure; // Should be operation
	}
	
	part def TireMountingRim;
	
	part def InflationValve;
	
	part def BalanceWeight;
	
	part def LugBoltMountingHole {
		lugBoltSize :> length;
	}
	
	part def LugBoltJoint {
		torque :> ISQ::torque;
		boltTension :> force;
	}
	
	part def Hub;
	
	part def LugBoltThreadableHole {
		lugBoltSize :> length;
		threadSize :> length;
	}
	
	// Parts
	
	part wheelHubAssembly: WheelHubAssembly {
		part wheel: WheelAssembly[1] {
			part t: Tire[1] {
				part bead : TireBead[2];			
			}
			part w: Wheel[1] {
				part rim : TireMountingRim[2];
				part v : InflationValve[1];
				part weight : BalanceWeight[0..6];
				part mountingHoles : LugBoltMountingHole[5];
			}						
			connection : PressureSeat connect t.bead to w.rim;		
		}
		part lugBoltJoints: LugBoltJoint[5] {					
			ref mountingHole: LugBoltMountingHole[1] subsets wheel.w.mountingHoles;
			ref threadedHole: LugBoltThreadableHole[1] subsets hub.h;
		}
		part hub: Hub[1] {
			part h: LugBoltThreadableHole[5];
		}
	}
	
}
````
