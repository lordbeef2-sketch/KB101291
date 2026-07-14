# OFFICIAL REPOSITORY FILE: SysML-v2-Pilot-Implementation/sysml/src/training/13. Flows/Flow Usage Example.sysml

- repository: `SysML-v2-Pilot-Implementation`
- source_path: `sysml/src/training/13. Flows/Flow Usage Example.sysml`
- source_url: https://github.com/Systems-Modeling/SysML-v2-Pilot-Implementation/blob/fa709f28dfd49dfdb7ee83e4e19da2f57e0eb3aa/sysml/src/training/13. Flows/Flow Usage Example.sysml
- source_bytes: 389
- source_sha256: `f1504686992a53032689e6dc2f904eb6b5df646ff2ac5261dbea6326ca407962`
- decoded_as: `utf-8`


## EXACT SOURCE

````sysml
package 'Flow Usage Example' {
	private import 'Port Example'::*;
	
	part def Vehicle;
	
	part vehicle : Vehicle {
		part tankAssy : FuelTankAssembly;
		part eng : Engine;
		
		flow of Fuel
		  from tankAssy.fuelTankPort.fuelSupply
			to eng.engineFuelPort.fuelSupply;
			
		flow of Fuel
		  from eng.engineFuelPort.fuelReturn
			to tankAssy.fuelTankPort.fuelReturn;
	} 
}
````
