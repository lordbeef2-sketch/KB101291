# OFFICIAL REPOSITORY FILE: SysML-v2-Pilot-Implementation/sysml/src/validation/03-Function-based Behavior/3c-Function-based Behavior-structure mod-2.sysml

- repository: `SysML-v2-Pilot-Implementation`
- source_path: `sysml/src/validation/03-Function-based Behavior/3c-Function-based Behavior-structure mod-2.sysml`
- source_url: https://github.com/Systems-Modeling/SysML-v2-Pilot-Implementation/blob/fa709f28dfd49dfdb7ee83e4e19da2f57e0eb3aa/sysml/src/validation/03-Function-based Behavior/3c-Function-based Behavior-structure mod-2.sysml
- source_bytes: 1112
- source_sha256: `414e37e6a7cb98979cc28e33ed4cb454fb101c8f02a55744310caca08434c565`
- decoded_as: `utf-8`


## EXACT SOURCE

````sysml
package '3c-Function-based Behavior-structure mod-2' {
	
	part def Vehicle;
	part def VehicleFrame;
	
	part def HitchBall;
	part def TrailerCoupler;
	
	part def Trailer;
	part def TrailerFrame;
	
	connection def TrailerHitch {
		end hitch : HitchBall;
		end coupler : TrailerCoupler;
	}
	
	part 'vehicle-trailer system' {
		
		part vehicle : Vehicle {
			part vehicleFrame : VehicleFrame {
				part hitch : HitchBall;
			}
		}
		
		connection trailerHitch : TrailerHitch[0..1]
			connect vehicle.vehicleFrame.hitch to trailer.trailerFrame.coupler;
		
		part trailer : Trailer {
			part trailerFrame : TrailerFrame {
				part coupler : TrailerCoupler;
			}
		}
		
		perform action {
			action 'connect trailer to vehicle' {
				// Assert that exactly one connection exists during the
				// performance of this action.
				abstract ref :>> trailerHitch[1];
			}
			then action 'disconnect trailer from vehicle' {
				// Assert that exactly no connection exists during the
				// performance of this action.
				abstract ref :>> trailerHitch[0];		
			}
		}
		
	}
	
}
````
