# OFFICIAL REPOSITORY FILE: SysML-v2-Release/sysml/src/training/11. Interfaces/Interface Example.sysml

- repository: `SysML-v2-Release`
- source_path: `sysml/src/training/11. Interfaces/Interface Example.sysml`
- source_url: https://github.com/Systems-Modeling/SysML-v2-Release/blob/288d129c0d532065d45434bbb48a920898b719af/sysml/src/training/11. Interfaces/Interface Example.sysml
- source_bytes: 426
- source_sha256: `024abc50f2d2047124d8bbf8b3716e4849e70b5574a8c445b0694f55fc467c40`
- decoded_as: `utf-8`


## EXACT SOURCE

````sysml
package 'Interface Example' {
	private import 'Port Example'::*;
	
	part def Vehicle;
	
	interface def FuelInterface {
		end supplierPort : FuelOutPort;
		end consumerPort : FuelInPort;
	}
	
	part vehicle : Vehicle {	
		part tankAssy : FuelTankAssembly;		
		part eng : Engine;
		
		interface : FuelInterface connect 
			supplierPort ::> tankAssy.fuelTankPort to 
			consumerPort ::> eng.engineFuelPort;
	} 
}
````
