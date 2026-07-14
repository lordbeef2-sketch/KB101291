# OFFICIAL REPOSITORY FILE: SysML-v2-Pilot-Implementation/org.omg.sysml.xpect.tests/src/org/omg/sysml/xpect/tests/validation/invalid/StateSubactions_invalid.sysml.xt

- repository: `SysML-v2-Pilot-Implementation`
- source_path: `org.omg.sysml.xpect.tests/src/org/omg/sysml/xpect/tests/validation/invalid/StateSubactions_invalid.sysml.xt`
- source_url: https://github.com/Systems-Modeling/SysML-v2-Pilot-Implementation/blob/fa709f28dfd49dfdb7ee83e4e19da2f57e0eb3aa/org.omg.sysml.xpect.tests/src/org/omg/sysml/xpect/tests/validation/invalid/StateSubactions_invalid.sysml.xt
- source_bytes: 2392
- source_sha256: `6c2c41a524ec28ce894e4af791694734e1841955d5479d744a7fe7908bbf723a`
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
		File {from ="/library.kernel/Transfers.kerml"}
		File {from ="/library.kernel/ControlPerformances.kerml"}
		File {from ="/library.kernel/StatePerformances.kerml"}
		File {from ="/library.kernel/TransitionPerformances.kerml"}
		File {from ="/library.systems/Items.sysml"}
		File {from ="/library.systems/Parts.sysml"}
		File {from ="/library.systems/Ports.sysml"}
		File {from ="/library.systems/Actions.sysml"}
		File {from ="/library.systems/States.sysml"}
	}
	Workspace {
		JavaProject {
			SrcFolder {
				ThisFile {}
				File {from ="/library.kernel/Base.kerml"}
				File {from ="/library.kernel/Occurrences.kerml"}
				File {from ="/library.kernel/Objects.kerml"}
				File {from ="/library.kernel/Performances.kerml"}
				File {from ="/library.kernel/Transfers.kerml"}
				File {from ="/library.kernel/ControlPerformances.kerml"}
				File {from ="/library.kernel/StatePerformances.kerml"}
				File {from ="/library.kernel/TransitionPerformances.kerml"}
				File {from ="/library.systems/Items.sysml"}
				File {from ="/library.systems/Parts.sysml"}
				File {from ="/library.systems/Ports.sysml"}
				File {from ="/library.systems/Actions.sysml"}
				File {from ="/library.systems/States.sysml"}
			}
		}
	}
END_SETUP 
*/
package 'State Subactions' {
	
	state def S {
		entry action a;
		do action b;
		exit action c;
		
		//XPECT errors --> "A state may have at most one exit action." at "exit action c1;"	
		exit action c1;
		//XPECT errors --> "A state may have at most one entry action." at "entry action a1;"	
		entry action a1;
		//XPECT errors --> "A state may have at most one do action." at "do action b1;"	
		do action b1;
	}
	
	state s {
		entry action a;
		do action b;
		exit action c;
		
		//XPECT errors --> "A state may have at most one exit action." at "exit action c1;"	
		exit action c1;
		//XPECT errors --> "A state may have at most one entry action." at "entry action a1;"	
		entry action a1;
		//XPECT errors --> "A state may have at most one do action." at "do action b1;"	
		do action b1;
	}
	
}

````
