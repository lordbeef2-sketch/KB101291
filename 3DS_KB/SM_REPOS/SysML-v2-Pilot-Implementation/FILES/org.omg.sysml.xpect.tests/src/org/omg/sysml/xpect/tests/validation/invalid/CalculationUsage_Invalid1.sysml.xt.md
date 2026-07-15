# OFFICIAL REPOSITORY FILE: SysML-v2-Pilot-Implementation/org.omg.sysml.xpect.tests/src/org/omg/sysml/xpect/tests/validation/invalid/CalculationUsage_Invalid1.sysml.xt

- repository: `SysML-v2-Pilot-Implementation`
- source_path: `org.omg.sysml.xpect.tests/src/org/omg/sysml/xpect/tests/validation/invalid/CalculationUsage_Invalid1.sysml.xt`
- source_url: https://github.com/Systems-Modeling/SysML-v2-Pilot-Implementation/blob/fa709f28dfd49dfdb7ee83e4e19da2f57e0eb3aa/org.omg.sysml.xpect.tests/src/org/omg/sysml/xpect/tests/validation/invalid/CalculationUsage_Invalid1.sysml.xt
- source_bytes: 2839
- source_sha256: `1c3faa754d03f3a5e84d6e8d6eb3652bc3f5361711adf9a3e1d87ab3628af4a3`
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
package pkg {
	calc def 'F1';
	calc def 'F2';
	action def B;
	action bb: B;
	part def A {
		// XPECT errors --> "A calculation must be typed by one calculation definition." at "calc f1 : F1, F2;"
	 	calc f1 : F1, F2;
	 	/* XPECT errors --- 
	 	   "A calculation must be typed by one calculation definition." at "calc f2 : A;"
		--- */ 
		//* XPECT warnings ---
		   "Duplicate of inherited member name 'self' from Calculation, Part" at "calc f2 : A;"
		   "Duplicate of inherited member name 'start' from Action, Part" at "calc f2 : A;"
		   "Duplicate of inherited member name 'done' from Action, Part" at "calc f2 : A;"
		--- */
    	calc f2: A;
    	// XPECT errors ---> "A calculation must be typed by one calculation definition." at "calc f3 : f2;"
		//* XPECT warnings ---
		   "Duplicate of inherited member name 'self' from Calculation, Part" at "calc f3 : f2;"
		   "Duplicate of inherited member name 'start' from Action, Part" at "calc f3 : f2;"
		   "Duplicate of inherited member name 'done' from Action, Part" at "calc f3 : f2;"
		--- */
    	calc f3: f2;
    	// XPECT errors ---> "A calculation must be typed by one calculation definition." at "calc f4 : A::f1;"
    	calc f4: A::f1;
    	// XPECT errors ---> "A calculation must be typed by one calculation definition." at "calc f5 : B;"
    	calc f5: B;
    	// XPECT errors ---> "A calculation must be typed by one calculation definition." at "calc f6 : bb;"
    	calc f6: bb;
   	}
}
````
