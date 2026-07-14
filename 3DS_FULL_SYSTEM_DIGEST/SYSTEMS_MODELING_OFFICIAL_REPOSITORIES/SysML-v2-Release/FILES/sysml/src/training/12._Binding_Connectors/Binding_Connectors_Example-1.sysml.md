# OFFICIAL REPOSITORY FILE: SysML-v2-Release/sysml/src/training/12. Binding Connectors/Binding Connectors Example-1.sysml

- repository: `SysML-v2-Release`
- source_path: `sysml/src/training/12. Binding Connectors/Binding Connectors Example-1.sysml`
- source_url: https://github.com/Systems-Modeling/SysML-v2-Release/blob/288d129c0d532065d45434bbb48a920898b719af/sysml/src/training/12. Binding Connectors/Binding Connectors Example-1.sysml
- source_bytes: 624
- source_sha256: `5800024a905fe0a3a63a107686d70da56c7f80857b439ce552941894497a05af`
- decoded_as: `utf-8`


## EXACT SOURCE

````sysml
package 'Binding Connectors Example-1' {
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
			
			bind fuelTankPort.fuelSupply = pump.pumpOut;
			bind fuelTankPort.fuelReturn = tank.fuelIn;
			
			part pump : FuelPump {
				out item pumpOut : Fuel;
				in item pumpIn : Fuel;
			}
			
			part tank : FuelTank {
				out item fuelOut : Fuel;
				in item fuelIn : Fuel;
			}
		}
	} 
}
````
