# OFFICIAL REPOSITORY FILE: SysML-v2-Pilot-Implementation/org.omg.sysml.xpect.tests/src/org/omg/sysml/xpect/tests/validation/invalid/CalculationUsage_Invalid2.sysml.xt

- repository: `SysML-v2-Pilot-Implementation`
- source_path: `org.omg.sysml.xpect.tests/src/org/omg/sysml/xpect/tests/validation/invalid/CalculationUsage_Invalid2.sysml.xt`
- source_url: https://github.com/Systems-Modeling/SysML-v2-Pilot-Implementation/blob/fa709f28dfd49dfdb7ee83e4e19da2f57e0eb3aa/org.omg.sysml.xpect.tests/src/org/omg/sysml/xpect/tests/validation/invalid/CalculationUsage_Invalid2.sysml.xt
- source_bytes: 1733
- source_sha256: `c5473571cc53612bb999cbcaeaa4103d4dcedcf8c86db20c87fb60b84adabc74`
- decoded_as: `utf-8`


## EXACT SOURCE

````xtext
//*
XPECT_SETUP org.omg.sysml.xpect.tests.validation.invalid.SysMLTests
	ResourceSet {
		ThisFile {}
		File {from ="/library.kernel/Base.kerml"}
		File {from ="/library.kernel/Occurrences.kerml"}
		File {from ="/library.kernel/Objects.kerml"}
		File {from ="/library.kernel/Performances.kerml"}
		File {from ="/library.kernel/ControlPerformances.kerml"}
		File {from ="/library.kernel/TransitionPerformances.kerml"}
		File {from ="/library.systems/Items.sysml"}
		File {from ="/library.systems/Parts.sysml"}
		File {from ="/library.systems/Ports.sysml"}
		File {from ="/library.systems/Actions.sysml"}
		File {from ="/library.systems/Calculations.sysml"}
	}
	Workspace {
		JavaProject {
			SrcFolder {
				ThisFile {}
				File {from ="/library.kernel/Base.kerml"}
				File {from ="/library.kernel/Occurrences.kerml"}
				File {from ="/library.kernel/Objects.kerml"}
				File {from ="/library.kernel/Performances.kerml"}
				File {from ="/library.kernel/ControlPerformances.kerml"}
				File {from ="/library.kernel/TransitionPerformances.kerml"}
				File {from ="/library.systems/Items.sysml"}
				File {from ="/library.systems/Parts.sysml"}
				File {from ="/library.systems/Ports.sysml"}
				File {from ="/library.systems/Actions.sysml"}
				File {from ="/library.systems/Calculations.sysml"}
			}
		}
	}
END_SETUP
*/
package Test {
	attribute def T;
	
	calc def C { return T; }
	
	calc def C1 {
		return r1 : T;
		// XPECT errors --> "Only one return parameter is allowed" at "return r2 : T;"
		return r2 : T;
	}
	
	calc c : C { return T; }
	
	calc c2 : C {
		return r1 : T;
		// XPECT errors --> "Only one return parameter is allowed" at "return r2 : T;"
		return r2 : T;
	}
}
````
