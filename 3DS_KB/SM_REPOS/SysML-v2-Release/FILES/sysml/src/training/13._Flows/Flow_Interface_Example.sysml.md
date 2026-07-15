# OFFICIAL REPOSITORY FILE: SysML-v2-Release/sysml/src/training/13. Flows/Flow Interface Example.sysml

- repository: `SysML-v2-Release`
- source_path: `sysml/src/training/13. Flows/Flow Interface Example.sysml`
- source_url: https://github.com/Systems-Modeling/SysML-v2-Release/blob/288d129c0d532065d45434bbb48a920898b719af/sysml/src/training/13. Flows/Flow Interface Example.sysml
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
