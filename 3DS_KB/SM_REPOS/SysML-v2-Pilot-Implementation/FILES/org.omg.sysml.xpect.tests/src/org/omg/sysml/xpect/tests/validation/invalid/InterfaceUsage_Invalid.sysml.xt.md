# OFFICIAL REPOSITORY FILE: SysML-v2-Pilot-Implementation/org.omg.sysml.xpect.tests/src/org/omg/sysml/xpect/tests/validation/invalid/InterfaceUsage_Invalid.sysml.xt

- repository: `SysML-v2-Pilot-Implementation`
- source_path: `org.omg.sysml.xpect.tests/src/org/omg/sysml/xpect/tests/validation/invalid/InterfaceUsage_Invalid.sysml.xt`
- source_url: https://github.com/Systems-Modeling/SysML-v2-Pilot-Implementation/blob/fa709f28dfd49dfdb7ee83e4e19da2f57e0eb3aa/org.omg.sysml.xpect.tests/src/org/omg/sysml/xpect/tests/validation/invalid/InterfaceUsage_Invalid.sysml.xt
- source_bytes: 2856
- source_sha256: `0c7cbc5061eba1d3b021fe273bce7365a6f5e2e76b82e04c034f5a7a06f06219`
- decoded_as: `utf-8`


## EXACT SOURCE

````xtext
//*
XPECT_SETUP org.omg.sysml.xpect.tests.validation.invalid.SysMLTests
	ResourceSet {
		ThisFile {}
		File {from ="/library.kernel/Base.kerml"}
		File {from ="/library.kernel/Objects.kerml"}
		File {from ="/library.kernel/Occurrences.kerml"}
		File {from ="/library.systems/Items.sysml"}
		File {from ="/library.systems/Parts.sysml"}
		File {from ="/library.systems/Ports.sysml"}
		File {from ="/library.systems/Connections.sysml"}
		File {from ="/library.systems/Interfaces.sysml"}
	}
	Workspace {
		JavaProject {
			SrcFolder {
				ThisFile {}
				File {from ="/library.kernel/Base.kerml"}
				File {from ="/library.kernel/Objects.kerml"}
				File {from ="/library.kernel/Occurrences.kerml"}
				File {from ="/library.systems/Items.sysml"}
				File {from ="/library.systems/Parts.sysml"}
				File {from ="/library.systems/Ports.sysml"}
				File {from ="/library.systems/Connections.sysml"}
				File {from ="/library.systems/Interfaces.sysml"}
			}
		}
	}
END_SETUP 
*/
package 'Interface Example' {
	part def Fuel;
	
	port def FuelOutPort;
	port def FuelInPort;
	
	interface def FuelInterface {
		end supplierPort : FuelOutPort;
		end consumerPort : FuelInPort;
	}
	interface def FuelInterface2 {
		end supplierPort : FuelOutPort;
		end consumerPort : FuelInPort;
	}
	interface def FuelInterface3 {
		end supplierPort : FuelOutPort;
		end consumerPort : FuelInPort;
		
		//*XPECT errors ---
			"An interface definition end must be a port." at "end part notPort : Fuel;"
			"Cannot have more than two ends" at "end part notPort : Fuel;"
		--- */
		end part notPort : Fuel;
	}
	
	part def Vehicle;
	part vehicle  {	
		part tankAssy {
			port fuelTankPort : FuelOutPort;
			part fuel : Fuel;
		}
		
		part eng {
			port engineFuelPort : FuelInPort;
		}
		interface fi: FuelInterface connect tankAssy.fuelTankPort to eng.engineFuelPort;
		interface original: FuelInterface, FuelInterface2 connect 
			tankAssy.fuelTankPort to 
			eng.engineFuelPort;
		//XPECT errors --> "An interface must be typed by interface definitions." at "interface opposite : Fuel connect   			x ::> tankAssy.fuelTankPort to  			y ::> eng.engineFuelPort;"
		interface opposite : Fuel connect 
			x ::> tankAssy.fuelTankPort to
			y ::> eng.engineFuelPort;
		//XPECT errors ---> "An interface must be typed by interface definitions." at "interface opposite1 : fi connect eng.engineFuelPort to tankAssy.fuelTankPort;"
		interface opposite1 : fi connect eng.engineFuelPort to tankAssy.fuelTankPort; 
		interface bad {
			//XPECT errors --> "An interface end must be a port." at "end part ::> tankAssy.fuel;"
			// XPECT warnings ---> "Duplicate of inherited member name 'self' from Part, Port" at "end part ::> tankAssy.fuel;"
			end part ::> tankAssy.fuel;
			end port ::> eng.engineFuelPort;
		}
	} 
}
````
