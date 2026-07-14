# OFFICIAL REPOSITORY FILE: SysML-v2-Pilot-Implementation/org.omg.sysml.xpect.tests/src/org/omg/sysml/xpect/tests/validation/valid/InterfaceUsage.sysml.xt

- repository: `SysML-v2-Pilot-Implementation`
- source_path: `org.omg.sysml.xpect.tests/src/org/omg/sysml/xpect/tests/validation/valid/InterfaceUsage.sysml.xt`
- source_url: https://github.com/Systems-Modeling/SysML-v2-Pilot-Implementation/blob/fa709f28dfd49dfdb7ee83e4e19da2f57e0eb3aa/org.omg.sysml.xpect.tests/src/org/omg/sysml/xpect/tests/validation/valid/InterfaceUsage.sysml.xt
- source_bytes: 2436
- source_sha256: `02672885ccb46453c74545bfbb8aa705878359a19052bde3a48766df28c73b91`
- decoded_as: `utf-8`


## EXACT SOURCE

````xtext
//* 
XPECT_SETUP org.omg.sysml.xpect.tests.validation.valid.SysMLTests
	ResourceSet {
		ThisFile {}
		File {from ="/library.kernel/Base.kerml"}
		File {from ="/library.kernel/Links.kerml"}
		File {from ="/library.kernel/Objects.kerml"}
		File {from ="/library.kernel/Occurrences.kerml"}
		File {from ="/library.kernel/Performances.kerml"}
		File {from ="/library.systems/Items.sysml"}
		File {from ="/library.systems/Parts.sysml"}
		File {from ="/library.systems/Ports.sysml"}
		File {from ="/library.systems/Connections.sysml"}
		File {from ="/library.systems/Interfaces.sysml"}
		File {from ="/library.systems/Actions.sysml"}
		File {from ="/library.systems/Flows.sysml"}
	}
	Workspace {
		JavaProject {
			SrcFolder {
				ThisFile {}
				File {from ="/library.kernel/Base.kerml"}
				File {from ="/library.kernel/Links.kerml"}
				File {from ="/library.kernel/Objects.kerml"}
				File {from ="/library.kernel/Occurrences.kerml"}
				File {from ="/library.kernel/Performances.kerml"}
				File {from ="/library.systems/Items.sysml"}
				File {from ="/library.systems/Parts.sysml"}
				File {from ="/library.systems/Ports.sysml"}
				File {from ="/library.systems/Connections.sysml"}
				File {from ="/library.systems/Interfaces.sysml"}
				File {from ="/library.systems/Actions.sysml"}
				File {from ="/library.systems/Flows.sysml"}
			}
		}
	}
END_SETUP 
*/
// XPECT noErrors ---> ""
package 'Interface Example' {
	attribute def Temp;
	part def Fuel;

	port def FuelOutPort {
		attribute temperature : Temp;
		out ref fuelSupply : Fuel;
		in ref fuelReturn : Fuel;
	}
	
	port def FuelInPort {
		attribute temperature : Temp;
		in ref fuelSupply : Fuel;
		out ref fuelReturn : Fuel;
	}
	
	part def FuelTankAssembly {
		port fuelTankPort : FuelOutPort;
	}
	
	part def Engine {
		port engineFuelPort : FuelInPort;
	}
	
	part def Vehicle;
	
	interface def FuelInterface {
		end supplierPort : FuelOutPort;
		end consumerPort : FuelInPort;
		flow supplierPort.fuelSupply to consumerPort.fuelSupply;
		flow consumerPort.fuelReturn to supplierPort.fuelReturn;
	}
	
	part vehicle : Vehicle {	
		part tankAssy : FuelTankAssembly {
			port redefines fuelTankPort;
		}
		
		part eng : Engine {
			port redefines engineFuelPort;
		}
		interface FuelInterface connect 
			supplierPort ::> tankAssy.fuelTankPort to 
			consumerPort ::> eng.engineFuelPort;
	} 
}

````
