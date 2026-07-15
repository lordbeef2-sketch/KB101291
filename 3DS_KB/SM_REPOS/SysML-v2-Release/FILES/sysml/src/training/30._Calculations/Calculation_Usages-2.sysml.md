# OFFICIAL REPOSITORY FILE: SysML-v2-Release/sysml/src/training/30. Calculations/Calculation Usages-2.sysml

- repository: `SysML-v2-Release`
- source_path: `sysml/src/training/30. Calculations/Calculation Usages-2.sysml`
- source_url: https://github.com/Systems-Modeling/SysML-v2-Release/blob/288d129c0d532065d45434bbb48a920898b719af/sysml/src/training/30. Calculations/Calculation Usages-2.sysml
- source_bytes: 786
- source_sha256: `7ccd8ee0ffc46c75145f796353410021c0f25e2656c0def29de2556f044c6a46`
- decoded_as: `utf-8`


## EXACT SOURCE

````sysml
package 'Calculation Usages-2' {
	private import ScalarValues::Real;
	private import ISQ::*;
	private import 'Calculation Definitions'::*;
	
	attribute def DynamicState {
		attribute v: SpeedValue;
		attribute x: LengthValue;
	}
	
	part def VehicleDynamics {
		attribute C_d : Real;
		attribute C_f : Real;
		attribute wheelPower : PowerValue;
		attribute mass : MassValue;
		
		calc updateState { 
			in delta_t : TimeValue; 
			in currState : DynamicState;
			attribute totalPower : PowerValue = Power(wheelPower, C_d, C_f, mass, currState.v);
			
			return attribute newState : DynamicState {
				:>> v = Velocity(delta_t, currState.v, Acceleration(totalPower, mass, currState.v));
				:>> x = Position(delta_t, currState.x, currState.v);
			}
		}
	} 
	
}
````
