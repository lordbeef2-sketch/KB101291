# OFFICIAL REPOSITORY FILE: SysML-v2-Release/sysml/src/training/12. Binding Connectors/Binding Connectors Example-2.sysml

- repository: `SysML-v2-Release`
- source_path: `sysml/src/training/12. Binding Connectors/Binding Connectors Example-2.sysml`
- source_url: https://github.com/Systems-Modeling/SysML-v2-Release/blob/288d129c0d532065d45434bbb48a920898b719af/sysml/src/training/12. Binding Connectors/Binding Connectors Example-2.sysml
- source_bytes: 574
- source_sha256: `b13bcb9b9f8a3fbfc914501bf9c6d98206e8d47237e77a6092d4536cac0e72c4`
- decoded_as: `utf-8`


## EXACT SOURCE

````sysml
package 'Binding Connectors Example-2' {
	private import 'Port Example'::*;
	
	part def Vehicle;
	part def FuelPump;
	part def FuelTank;
	
	part vehicle : Vehicle {	
		part tank : FuelTankAssembly {
			port redefines fuelTankPort {
				out item redefines fuelSupply;
				in item redefines fuelReturn;
			}
			
			part pump : FuelPump {
				out item pumpOut : Fuel = fuelTankPort.fuelSupply;
				in item pumpIn : Fuel;
			}
			
			part tank : FuelTank {
				out item fuelOut : Fuel;
				in item fuelIn : Fuel = fuelTankPort.fuelReturn;
			}
		}
	} 
}
````
