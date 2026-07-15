# OFFICIAL REPOSITORY FILE: SysML-v2-Pilot-Implementation/sysml/src/training/30. Calculations/Calculation Definitions.sysml

- repository: `SysML-v2-Pilot-Implementation`
- source_path: `sysml/src/training/30. Calculations/Calculation Definitions.sysml`
- source_url: https://github.com/Systems-Modeling/SysML-v2-Pilot-Implementation/blob/fa709f28dfd49dfdb7ee83e4e19da2f57e0eb3aa/sysml/src/training/30. Calculations/Calculation Definitions.sysml
- source_bytes: 734
- source_sha256: `c8c08362b9031d1ca737e8e8566dcd015c8d20d1fd1c50a021a3fec42824b605`
- decoded_as: `utf-8`


## EXACT SOURCE

````sysml
package 'Calculation Definitions' {
	private import ScalarValues::Real;
	private import ISQ::*;
	
	calc def Power { in whlpwr : PowerValue; in Cd : Real; in Cf : Real; in tm : MassValue; in v : SpeedValue;
		attribute drag = Cd * v;
		attribute friction = Cf * tm * v;
		
		return : PowerValue = whlpwr - drag - friction;
	}
	
	calc def Acceleration { in tp: PowerValue; in tm : MassValue; in v : SpeedValue;
		return : AccelerationValue = tp / (tm * v);
	}
	
	calc def Velocity { in dt : TimeValue; in v0 : SpeedValue; in a : AccelerationValue;
		return : SpeedValue = v0 + a * dt;
 	}
 	
	calc def Position { in dt : TimeValue; in x0 : LengthValue; in v : SpeedValue;
		return : LengthValue = x0 + v * dt;
	}
}
````
