# OFFICIAL REPOSITORY FILE: SysML-v2-Pilot-Implementation/sysml/src/training/13. Flows/Flow Interface Example.sysml

- repository: `SysML-v2-Pilot-Implementation`
- source_path: `sysml/src/training/13. Flows/Flow Interface Example.sysml`
- source_url: https://github.com/Systems-Modeling/SysML-v2-Pilot-Implementation/blob/fa709f28dfd49dfdb7ee83e4e19da2f57e0eb3aa/sysml/src/training/13. Flows/Flow Interface Example.sysml
- source_bytes: 558
- source_sha256: `15ebaa4cc15137f4dfe4d2357d79365506661c1f890bb2708f3cea59c3237b0b`
- decoded_as: `utf-8`


## EXACT SOURCE

````sysml
package 'Flow Interface Example' {
	private import 'Port Example'::*;
	
	part def Vehicle;
	
	interface def FuelInterface {
		end supplierPort : FuelOutPort;
		end consumerPort : FuelInPort;
		
		flow supplierPort.fuelSupply to consumerPort.fuelSupply;			
		flow consumerPort.fuelReturn to supplierPort.fuelReturn;
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
