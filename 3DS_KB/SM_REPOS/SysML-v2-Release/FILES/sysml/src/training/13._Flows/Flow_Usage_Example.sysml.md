# OFFICIAL REPOSITORY FILE: SysML-v2-Release/sysml/src/training/13. Flows/Flow Usage Example.sysml

- repository: `SysML-v2-Release`
- source_path: `sysml/src/training/13. Flows/Flow Usage Example.sysml`
- source_url: https://github.com/Systems-Modeling/SysML-v2-Release/blob/288d129c0d532065d45434bbb48a920898b719af/sysml/src/training/13. Flows/Flow Usage Example.sysml
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
