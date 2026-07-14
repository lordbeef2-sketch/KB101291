# OFFICIAL REPOSITORY FILE: SysML-v2-Pilot-Implementation/sysml/src/validation/03-Function-based Behavior/3c-Function-based Behavior-structure mod-3.sysml

- repository: `SysML-v2-Pilot-Implementation`
- source_path: `sysml/src/validation/03-Function-based Behavior/3c-Function-based Behavior-structure mod-3.sysml`
- source_url: https://github.com/Systems-Modeling/SysML-v2-Pilot-Implementation/blob/fa709f28dfd49dfdb7ee83e4e19da2f57e0eb3aa/sysml/src/validation/03-Function-based Behavior/3c-Function-based Behavior-structure mod-3.sysml
- source_bytes: 814
- source_sha256: `590047b792d3d11313ce3892ece837aaf036bce9f25d6481cc97741daaa930e4`
- decoded_as: `utf-8`


## EXACT SOURCE

````sysml
package '3c-Function-based Behavior-structure mod-3' {
	
	part def Vehicle;
	part def VehicleFrame;
	part def HitchBall;
	part def Trailer;
	part def TrailerFrame;
	part def TrailerCoupler;
	
	part vehicle : Vehicle {
		part vehicleFrame : VehicleFrame {
			part hitch : HitchBall;
		}
	}
	
	part trailer : Trailer {
		part trailerFrame : TrailerFrame {
			part coupler : TrailerCoupler {
				ref part hitch : HitchBall;
			}
		}		
	}
			
	action {
		// Insert the vehicle HitchBall into the TrailerCoupler.
		action 'connect trailer to vehicle'
			assign trailer.trailerFrame.coupler.hitch := vehicle.vehicleFrame.hitch;
		
		// Remove the HitchBall from the TrailerCoupler.
		then action 'disconnect trailer from vehicle'
			assign trailer.trailerFrame.coupler.hitch := null;
	}
}
````
