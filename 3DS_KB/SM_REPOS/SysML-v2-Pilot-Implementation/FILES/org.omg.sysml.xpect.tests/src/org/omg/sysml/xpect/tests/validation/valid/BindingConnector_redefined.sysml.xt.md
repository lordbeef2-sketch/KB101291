# OFFICIAL REPOSITORY FILE: SysML-v2-Pilot-Implementation/org.omg.sysml.xpect.tests/src/org/omg/sysml/xpect/tests/validation/valid/BindingConnector_redefined.sysml.xt

- repository: `SysML-v2-Pilot-Implementation`
- source_path: `org.omg.sysml.xpect.tests/src/org/omg/sysml/xpect/tests/validation/valid/BindingConnector_redefined.sysml.xt`
- source_url: https://github.com/Systems-Modeling/SysML-v2-Pilot-Implementation/blob/fa709f28dfd49dfdb7ee83e4e19da2f57e0eb3aa/org.omg.sysml.xpect.tests/src/org/omg/sysml/xpect/tests/validation/valid/BindingConnector_redefined.sysml.xt
- source_bytes: 2357
- source_sha256: `228f1a342594a7de11e1042806e283822f533bd269a9724f460dacd535b7c815`
- decoded_as: `utf-8`


## EXACT SOURCE

````xtext
//* 
XPECT_SETUP org.omg.sysml.xpect.tests.validation.valid.SysMLTests
	ResourceSet {
		ThisFile {}
		File {from ="/library.kernel/Base.kerml"}
		File {from ="/library.kernel/Links.kerml"}
		File {from ="/library.kernel/Occurrences.kerml"}
		File {from ="/library.kernel/Objects.kerml"}
		File {from ="/library.kernel/Performances.kerml"}
		File {from ="/library.kernel/BaseFunctions.kerml"}
		File {from ="/library.kernel/ControlFunctions.kerml"}
		File {from ="/library.kernel/ScalarValues.kerml"}
		File {from ="/library.systems/Items.sysml"}
		File {from ="/library.systems/Parts.sysml"}
		File {from ="/library.systems/Ports.sysml"}

	}
	Workspace {
		JavaProject {
			SrcFolder {
				ThisFile {}
				File {from ="/library.kernel/Base.kerml"}
				File {from ="/library.kernel/Links.kerml"}
		       	File {from ="/library.kernel/Occurrences.kerml"}
				File {from ="/library.kernel/Objects.kerml"}
				File {from ="/library.kernel/Performances.kerml"}
				File {from ="/library.kernel/BaseFunctions.kerml"}
				File {from ="/library.kernel/ControlFunctions.kerml"}
				File {from ="/library.kernel/ScalarValues.kerml"}
				File {from ="/library.systems/Items.sysml"}
				File {from ="/library.systems/Parts.sysml"}
				File {from ="/library.systems/Ports.sysml"}
			}
		}
	}
END_SETUP 
*/
// XPECT noErrors ---> ""
package Example2 {
	part def Fuel;
	port def FuelOutPort {
		out ref fuelSupply : Fuel;
		in ref fuelReturn : Fuel;
	}
	part def FuelTankAssembly {
		port fuelTankPort : FuelOutPort;
	}

	part def Vehicle;
	part def FuelPump;
	part def FuelTank;
	
	part vehicle : Vehicle {	
		part tank : FuelTankAssembly {
			port fuelTankPort0 redefines FuelTankAssembly::fuelTankPort {
				out ref fuelSupply redefines FuelTankAssembly::fuelTankPort::fuelSupply;
				in ref redefines fuelReturn;
			}
			port redefines FuelTankAssembly::fuelTankPort {
				out ref fuelSupply redefines FuelTankAssembly::fuelTankPort::fuelSupply;
			}
			
			bind fuelTankPort0.fuelSupply = pump.pumpOut;
			bind fuelTankPort0.fuelReturn = tank.fuelIn;
			bind fuelTankPort.fuelSupply = pump.pumpOut;
					
			part pump : FuelPump {
				out ref pumpOut : Fuel;
				in ref pumpIn : Fuel;
			}
			
			part tank : FuelTank {
				in ref fuelOut : Fuel;
				in ref fuelIn : Fuel;
			}
		}
	} 
}

````
