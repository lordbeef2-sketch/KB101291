# OFFICIAL REPOSITORY FILE: SysML-v2-Pilot-Implementation/sysml/src/examples/v1 Spec Examples/8.4.1 Wheel Hub Assembly/Wheel Package.sysml

- repository: `SysML-v2-Pilot-Implementation`
- source_path: `sysml/src/examples/v1 Spec Examples/8.4.1 Wheel Hub Assembly/Wheel Package.sysml`
- source_url: https://github.com/Systems-Modeling/SysML-v2-Pilot-Implementation/blob/fa709f28dfd49dfdb7ee83e4e19da2f57e0eb3aa/sysml/src/examples/v1 Spec Examples/8.4.1 Wheel Hub Assembly/Wheel Package.sysml
- source_bytes: 1816
- source_sha256: `3333ca0b933a6775943ac6aa926c258b48daaa2c76bb75bae13b9f804724bce7`
- decoded_as: `utf-8`


## EXACT SOURCE

````sysml
package 'Wheel Package' {
	doc
	/*
	 * Example from the SysML 1.6 spec, subclause 8.4.1 Wheel Hub Assembly.
	 */

	private import ISQ::*;
	
	pressure = force / length^2; 
	
	part def WheelHubAssembly {
		part wheel: WheelAssembly[1];
		part lugBoltJoints: LugBoltJoint[5] {
			ref redefines threadedHole subsets hub.h;
			ref redefines mountingHole subsets wheel.w.mountingHoles;
		}
		part hub: Hub[1];
	}
	
	part def WheelAssembly {
		inflationPressure :> pressure;
		
		part t: Tire[1] {
			part bead redefines Tire::bead;
		}
		part w: Wheel[1] {
			part rim redefines Wheel::rim;
		}		
				
		connection : PressureSeat connect t.bead to w.rim;		
	}
	
	part def Tire {
		tireSpecification : ScalarValues::String;
		
		part bead : TireBead[2];
		
		action mountTire;
	}
	
	part def TireBead;
	
	connection def PressureSeat {
		end : TireBead[1];
		end : TireMountingRim[1];
	}
	
	part def Wheel {
		diameter :> length;
		width :> length;
		
		part rim : TireMountingRim[2];
		part v : InflationValve[1];
		part weight : BalanceWeight[0..6];
		part mountingHoles : LugBoltMountingHole[5];
	}
	
	connection def BandMount {
		end : Wheel[1];
		end : WirelessTirePressureMonitor[1];
	}
	
	part def WirelessTirePressureMonitor {
		action transmitPressure;
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
		
		ref mountingHole: LugBoltMountingHole[1];
		ref threadedHole: LugBoltThreadableHole[1];
	}
	
	part def Hub {
		part h: LugBoltThreadableHole[5];
	}
	
	part def LugBoltThreadableHole {
		lugBoltSize :> length;
		threadSize :> length;
	}
	
}
````
