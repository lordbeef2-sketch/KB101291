# OFFICIAL REPOSITORY FILE: SysML-v2-Pilot-Implementation/org.omg.sysml.xpect.tests/src/org/omg/sysml/xpect/tests/validation/invalid/RequirementUsage_Invalid.sysml.xt

- repository: `SysML-v2-Pilot-Implementation`
- source_path: `org.omg.sysml.xpect.tests/src/org/omg/sysml/xpect/tests/validation/invalid/RequirementUsage_Invalid.sysml.xt`
- source_url: https://github.com/Systems-Modeling/SysML-v2-Pilot-Implementation/blob/fa709f28dfd49dfdb7ee83e4e19da2f57e0eb3aa/org.omg.sysml.xpect.tests/src/org/omg/sysml/xpect/tests/validation/invalid/RequirementUsage_Invalid.sysml.xt
- source_bytes: 3632
- source_sha256: `68372049e264eddfdca55c23d6da95fb3be52148dab47f6d6cdb244a764a337d`
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
package 'Requirement Definitions' {
	
	part def A {
		part a;
	}
	constraint def Rdef;
	constraint c: Rdef;
	requirement def <'1'> R1def;
	requirement def <'11'> R11def;
	requirement def <'2'> R2def  :> Rdef;
	
	//XPECT errors --> "A requirement must be typed by one requirement definition." at "requirement <'1.0'> r10 : R1def, R11def;"
	requirement <'1.0'> r10 : R1def, R11def;
	/* XPECT errors ---
		"A requirement  must be typed by one requirement definition." at "requirement <'1.1'> r11 : Rdef;"
	--- */
	requirement <'1.1'> r11 : Rdef;
	//XPECT errors --> "A requirement must be typed by one requirement definition." at "requirement <'1.2'> r12 : R1def, R2def;"
	requirement <'1.2'> r12 : R1def, R2def;
	//*XPECT errors ---
		"A requirement must be typed by one requirement definition." at "requirement r13 : A;"
	---*/
	// XPECT warnings --> "Duplicate of inherited member name 'self' from Part, RequirementCheck" at "requirement r13 : A;"
	requirement r13 : A;
	//*XPECT errors ---
		"A requirement must be typed by one requirement definition." at "requirement r14 : A::a;"
	---*/
	// XPECT warnings --> "Duplicate of inherited member name 'self' from Part, RequirementCheck" at "requirement r14 : A::a;"
	requirement r14 : A::a;
	//*XPECT errors ---
		"A requirement must be typed by one requirement definition." at "requirement r15 : c;"
	---*/
	requirement r15 : c;
}
````
