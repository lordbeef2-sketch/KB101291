# OFFICIAL REPOSITORY FILE: SysML-v2-Pilot-Implementation/org.omg.sysml.xpect.tests/src/org/omg/sysml/xpect/tests/validation/invalid/TransitionUsage_invalid.sysml.xt

- repository: `SysML-v2-Pilot-Implementation`
- source_path: `org.omg.sysml.xpect.tests/src/org/omg/sysml/xpect/tests/validation/invalid/TransitionUsage_invalid.sysml.xt`
- source_url: https://github.com/Systems-Modeling/SysML-v2-Pilot-Implementation/blob/fa709f28dfd49dfdb7ee83e4e19da2f57e0eb3aa/org.omg.sysml.xpect.tests/src/org/omg/sysml/xpect/tests/validation/invalid/TransitionUsage_invalid.sysml.xt
- source_bytes: 2320
- source_sha256: `ddc518682e7bde983dadf6e8b396697b6469c3f10b6ddfb5ccac09469cee3288`
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
package TransitionUsage_invalid {
	
	state def S1 parallel {
		state S1_1;
		// XPECT errors ---> "A parallel state cannot have successions or transitions." at "then S1_2;"
		then S1_2;
		state S1_2;
	}
	
	item def A;

	state def S2 {
		entry action init;
		// XPECT errors ---> "A transition with an accepter must have a state as its source." at "accept A"
		transition init accept A then S2_1;
		
		state S2_1;
		transition
			first S2_1
			// XPECT errors ---> "Must be a Boolean expression." at "if \"test\""
			if "test"
			then S2_2;
		state S2_2;
	}
	
	state s1 parallel {
		state s1_1;
		// XPECT errors ---> "A parallel state cannot have successions or transitions." at "then s1_2;"
		then s1_2;
		state s1_2;
	}
}

````
