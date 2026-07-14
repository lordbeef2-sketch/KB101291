# OFFICIAL REPOSITORY FILE: SysML-v2-Pilot-Implementation/org.omg.sysml.xpect.tests/src/org/omg/sysml/xpect/tests/validation/invalid/RequirementSubject_Invalid.sysml.xt

- repository: `SysML-v2-Pilot-Implementation`
- source_path: `org.omg.sysml.xpect.tests/src/org/omg/sysml/xpect/tests/validation/invalid/RequirementSubject_Invalid.sysml.xt`
- source_url: https://github.com/Systems-Modeling/SysML-v2-Pilot-Implementation/blob/fa709f28dfd49dfdb7ee83e4e19da2f57e0eb3aa/org.omg.sysml.xpect.tests/src/org/omg/sysml/xpect/tests/validation/invalid/RequirementSubject_Invalid.sysml.xt
- source_bytes: 2799
- source_sha256: `94dabcafe0c7fb7c4bc3a6b65f9e725d8c96bb900bc88ab94904f9fe40869c6f`
- decoded_as: `utf-8`


## EXACT SOURCE

````xtext
//*
XPECT_SETUP org.omg.sysml.xpect.tests.validation.invalid.SysMLTests
	ResourceSet {
		ThisFile {}
		File {from ="/library.kernel/Base.kerml"}
		File {from ="/library.kernel/BaseFunctions.kerml"}
		File {from ="/library.kernel/Objects.kerml"}
		File {from ="/library.kernel/Occurrences.kerml"}
		File {from ="/library.kernel/Performances.kerml"}
		File {from ="/library.kernel/ControlPerformances.kerml"}
		File {from ="/library.kernel/TransitionPerformances.kerml"}
		File {from ="/library.kernel/Transfers.kerml"}
		File {from ="/library.kernel/ControlFunctions.kerml"}
		File {from ="/library.kernel/ScalarValues.kerml"}
		File {from ="/library.systems/Attributes.sysml"}
		File {from ="/library.systems/Items.sysml"}
		File {from ="/library.systems/Parts.sysml"}
		File {from ="/library.systems/Ports.sysml"}
		File {from ="/library.systems/Connections.sysml"}
		File {from ="/library.systems/Interfaces.sysml"}
		File {from ="/library.systems/Actions.sysml"}
		File {from ="/library.systems/Constraints.sysml"}
		File {from ="/library.systems/Requirements.sysml"}
	}
	Workspace {
		JavaProject {
			SrcFolder {
				ThisFile {}
				File {from ="/library.kernel/Base.kerml"}
				File {from ="/library.kernel/BaseFunctions.kerml"}
				File {from ="/library.kernel/Objects.kerml"}
				File {from ="/library.kernel/Occurrences.kerml"}
				File {from ="/library.kernel/Performances.kerml"}
				File {from ="/library.kernel/ControlPerformances.kerml"}
				File {from ="/library.kernel/TransitionPerformances.kerml"}
				File {from ="/library.kernel/Transfers.kerml"}
				File {from ="/library.kernel/ControlFunctions.kerml"}
				File {from ="/library.kernel/ScalarValues.kerml"}
				File {from ="/library.systems/Attributes.sysml"}
				File {from ="/library.systems/Items.sysml"}
				File {from ="/library.systems/Parts.sysml"}
				File {from ="/library.systems/Ports.sysml"}
				File {from ="/library.systems/Connections.sysml"}
				File {from ="/library.systems/Interfaces.sysml"}
				File {from ="/library.systems/Actions.sysml"}
				File {from ="/library.systems/Constraints.sysml"}
				File {from ="/library.systems/Requirements.sysml"}
			}
		}
	}
END_SETUP 
*/
package 'Requirement Subjects' {
	
	requirement def R {
		subject s1;
		
		// XPECT errors --> "Only one subject is allowed." at "subject s2;"
		subject s2;
	}
	
	requirement r: R {
		subject s3;
		
		// XPECT errors --> "Only one subject is allowed." at "subject s4;"
		subject s4;
	}
	
	requirement def R1 :> R {
		in x;
		
		// XPECT errors --> "Subject must be first parameter." at "subject s5;"
		subject s5;
	}
	
	requirement r1 : R1 {
		in y;
		
		// XPECT errors --> "Subject must be first parameter." at "subject s6;"
		subject s6;		
	}
	
}
````
