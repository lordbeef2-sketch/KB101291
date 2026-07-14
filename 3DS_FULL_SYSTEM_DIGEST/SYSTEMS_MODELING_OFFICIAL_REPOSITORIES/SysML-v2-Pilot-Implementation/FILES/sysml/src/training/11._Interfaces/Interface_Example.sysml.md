# OFFICIAL REPOSITORY FILE: SysML-v2-Pilot-Implementation/sysml/src/training/11. Interfaces/Interface Example.sysml

- repository: `SysML-v2-Pilot-Implementation`
- source_path: `sysml/src/training/11. Interfaces/Interface Example.sysml`
- source_url: https://github.com/Systems-Modeling/SysML-v2-Pilot-Implementation/blob/fa709f28dfd49dfdb7ee83e4e19da2f57e0eb3aa/sysml/src/training/11. Interfaces/Interface Example.sysml
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
