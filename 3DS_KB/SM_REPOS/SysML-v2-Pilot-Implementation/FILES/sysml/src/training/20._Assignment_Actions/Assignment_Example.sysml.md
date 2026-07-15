# OFFICIAL REPOSITORY FILE: SysML-v2-Pilot-Implementation/sysml/src/training/20. Assignment Actions/Assignment Example.sysml

- repository: `SysML-v2-Pilot-Implementation`
- source_path: `sysml/src/training/20. Assignment Actions/Assignment Example.sysml`
- source_url: https://github.com/Systems-Modeling/SysML-v2-Pilot-Implementation/blob/fa709f28dfd49dfdb7ee83e4e19da2f57e0eb3aa/sysml/src/training/20. Assignment Actions/Assignment Example.sysml
- source_bytes: 1206
- source_sha256: `b5f436a5e6cccfc5c69c2ac8d88e71effd9a98200c9f0773291c7eabb4267c1a`
- decoded_as: `utf-8`


## EXACT SOURCE

````sysml
package 'For Loop Example' {
	private import SequenceFunctions::*;
	
    action def StraightLineDynamics {
        in power : ISQ::PowerValue;
        in mass : ISQ::MassValue;
        in delta_t : ISQ::TimeValue;
        in x_in : ISQ::LengthValue;
        in v_in : ISQ::SpeedValue;
        out x_out : ISQ::LengthValue;
        out v_out : ISQ::SpeedValue;
    }
	    
	action def ComputeMotion {
		in attribute powerProfile :> ISQ::power[*];
		in attribute vehicleMass :> ISQ::mass;
		in attribute initialPosition :> ISQ::length;
		in attribute initialSpeed :> ISQ::speed;
		in attribute deltaT :> ISQ::time;
		out attribute positions :> ISQ::length[*] := ( );
		
		private attribute position := initialPosition;
		private attribute speed := initialSpeed;
		
		for vehiclePower in powerProfile {
			perform action dynamics : StraightLineDynamics {
				in power = vehiclePower;
				in mass = vehicleMass;
				in delta_t = deltaT;
				in x_in = position;
				in v_in = speed;
				out x_out;
				out v_out;
			}
			then assign position := dynamics.x_out;
			then assign speed := dynamics.v_out;
			then assign positions := positions->including(position);
		}
	}
	
}
````
