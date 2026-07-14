# OFFICIAL REPOSITORY FILE: SysML-v2-Release/sysml/src/training/13. Flows/Flow Definition Example.sysml

- repository: `SysML-v2-Release`
- source_path: `sysml/src/training/13. Flows/Flow Definition Example.sysml`
- source_url: https://github.com/Systems-Modeling/SysML-v2-Release/blob/288d129c0d532065d45434bbb48a920898b719af/sysml/src/training/13. Flows/Flow Definition Example.sysml
- source_bytes: 443
- source_sha256: `4d4bab75cc419e98f5cb6bef459aa087918ae697cfacf2aba80b63737aed1fc4`
- decoded_as: `utf-8`


## EXACT SOURCE

````sysml
package 'Flow Definition Example' {
	private import 'Port Example'::*;
	
	part def Vehicle;
	
	flow def FuelFlow {
		ref :>> payload : Fuel;
		end port supplierPort : FuelOutPort;
		end port consumerPort : FuelInPort;
	}
	
	part vehicle : Vehicle {
		part tankAssy : FuelTankAssembly;
		part eng : Engine;
		
		flow : FuelFlow of Fuel
		  from tankAssy.fuelTankPort.fuelSupply
			to eng.engineFuelPort.fuelSupply;
			
	} 
}
````
