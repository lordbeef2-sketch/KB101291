# OFFICIAL REPOSITORY FILE: SysML-v2-Pilot-Implementation/org.omg.sysml.xpect.tests/src/org/omg/sysml/xpect/tests/validation/invalid/BindingConnector_invalid1.sysml.xt

- repository: `SysML-v2-Pilot-Implementation`
- source_path: `org.omg.sysml.xpect.tests/src/org/omg/sysml/xpect/tests/validation/invalid/BindingConnector_invalid1.sysml.xt`
- source_url: https://github.com/Systems-Modeling/SysML-v2-Pilot-Implementation/blob/fa709f28dfd49dfdb7ee83e4e19da2f57e0eb3aa/org.omg.sysml.xpect.tests/src/org/omg/sysml/xpect/tests/validation/invalid/BindingConnector_invalid1.sysml.xt
- source_bytes: 2786
- source_sha256: `d6d698046e66b07d101d598295be48ec68b57e6e56b97811c1bf1998471648db`
- decoded_as: `utf-8`


## EXACT SOURCE

````xtext
//*
XPECT_SETUP org.omg.sysml.xpect.tests.validation.invalid.SysMLTests
	ResourceSet {
		ThisFile {}
		File {from ="/library.kernel/Base.kerml"}
		File {from ="/library.kernel/Links.kerml"}
       	File {from ="/library.kernel/Occurrences.kerml"}
       	File {from ="/library.kernel/Objects.kerml"}
       	File {from ="/library.kernel/Performances.kerml"}
		File {from ="/library.kernel/BaseFunctions.kerml"}
		File {from ="/library.kernel/Transfers.kerml"}
		File {from ="/library.systems/Actions.sysml"}
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
				File {from ="/library.kernel/Transfers.kerml"}
				File {from ="/library.systems/Actions.sysml"}
				File {from ="/library.systems/Items.sysml"}
				File {from ="/library.systems/Parts.sysml"}
				File {from ="/library.systems/Ports.sysml"}
			}
		}
	}
END_SETUP 
*/
package Example3 {
	part def Fuel;
	port def FuelOutPort {
		out ref fuelSupply : Fuel;
		in ref fuelReturn : Fuel;
	}
	part def FuelTankAssembly {
		port fuelTankPort : FuelOutPort;
	}

	part def Vehicle;
	part vehicle : Vehicle {
		action myAction {
			in myIn;
			out myOut;
		}
		
		part tankAssy {
			port fuelTankPort {
				out ref fuelSupplyOut;
				in ref fuelReturnIn;
			}
		}
		// (TBD) XPECT noErrors --> "Output feature must conform to input feature" at "bind myAction.myOut = tankAssy.fuelTankPort.fuelReturnIn;"
		bind myAction.myOut = tankAssy.fuelTankPort.fuelReturnIn; //InTypes[Part, Object], OutTypes[Anything]
        bind tankAssy.fuelTankPort.fuelSupplyOut = myAction.myIn; //InTypes [Anything], OutTypes [Part, Object]
        
        
        part tankAssy2 : FuelTankAssembly {
			port fuelTankPort redefines FuelTankAssembly::fuelTankPort {
				out ref fuelSupplyOut redefines FuelTankAssembly::fuelTankPort::fuelSupply;
				in ref fuelReturnIn redefines FuelTankAssembly::fuelTankPort::fuelReturn;
			}
		}
		// (TBD) XPECT noErrors --> "Output feature must conform to input feature" at "bind myAction.myOut = tankAssy2.fuelTankPort.fuelReturnIn;"
		bind myAction.myOut = tankAssy2.fuelTankPort.fuelReturnIn; //InTypes[Fuel, Part, Object], OutTypes[Anything]
        bind tankAssy2.fuelTankPort.fuelSupplyOut = myAction.myIn; //InTypes [Anything], OutTypes [Part, Object]
		
	} 
}
````
