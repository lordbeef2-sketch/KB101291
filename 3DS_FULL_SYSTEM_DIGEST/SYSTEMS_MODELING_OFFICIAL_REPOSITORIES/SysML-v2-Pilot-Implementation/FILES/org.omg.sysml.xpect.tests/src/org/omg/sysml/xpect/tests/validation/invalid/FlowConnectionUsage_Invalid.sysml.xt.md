# OFFICIAL REPOSITORY FILE: SysML-v2-Pilot-Implementation/org.omg.sysml.xpect.tests/src/org/omg/sysml/xpect/tests/validation/invalid/FlowConnectionUsage_Invalid.sysml.xt

- repository: `SysML-v2-Pilot-Implementation`
- source_path: `org.omg.sysml.xpect.tests/src/org/omg/sysml/xpect/tests/validation/invalid/FlowConnectionUsage_Invalid.sysml.xt`
- source_url: https://github.com/Systems-Modeling/SysML-v2-Pilot-Implementation/blob/fa709f28dfd49dfdb7ee83e4e19da2f57e0eb3aa/org.omg.sysml.xpect.tests/src/org/omg/sysml/xpect/tests/validation/invalid/FlowConnectionUsage_Invalid.sysml.xt
- source_bytes: 2912
- source_sha256: `2f26f15a610cf3f01360c058a61c858e721cf50f2c9440b69320ec658eadee71`
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
       	File {from ="/library.kernel/Transfers.kerml"}
		File {from ="/library.kernel/BaseFunctions.kerml"}
		File {from ="/library.systems/Items.sysml"}
		File {from ="/library.systems/Parts.sysml"}
		File {from ="/library.systems/Ports.sysml"}
		File {from ="/library.systems/Flows.sysml"}
		File {from ="/library.systems/Actions.sysml"}
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
 		      	File {from ="/library.kernel/Transfers.kerml"}
				File {from ="/library.kernel/BaseFunctions.kerml"}
				File {from ="/library.systems/Items.sysml"}
				File {from ="/library.systems/Parts.sysml"}
				File {from ="/library.systems/Ports.sysml"}
				File {from ="/library.systems/Flows.sysml"}
				File {from ="/library.systems/Actions.sysml"}
			}
		}
	}
END_SETUP 
*/
package P {
	part def A;	
	
	abstract flow def F;
	abstract flow def G;
	
	abstract flow def H {
		end a;
	}
	
	flow def I :> H {
		end a;
		end b;
		// XPECT errors --> "A flow connection definition can have at most two ends." at "end c;"
		end c;
	}
	
	// XPECT errors --> "A flow connection definition can have at most two ends." at "flow def J :> I;"
	flow def J :> I;
	
	part apart : A {
		part b;
		part c;
		
		message : F from b to c;
		message : F, G from b to c;
		
		// XPECT errors --> "A flow connection must be typed by flow connection definitions." at "message :A from b to c;"
		//* XPECT warnings ---
		   "Duplicate of inherited member name 'self' from Action, Part" at "message :A from b to c;"
		   "Duplicate of inherited member name 'start' from Action, Part" at "message :A from b to c;"
		   "Duplicate of inherited member name 'done' from Action, Part" at "message :A from b to c;"
		--- */
		message :A from b to c;
		// XPECT errors --> "A flow connection must be typed by flow connection definitions." at "message :apart from b to c;"
		//* XPECT warnings ---
		   "Duplicate of inherited member name 'self' from Action, Part" at "message :apart from b to c;"
		   "Duplicate of inherited member name 'start' from Action, Part" at "message :apart from b to c;"
		   "Duplicate of inherited member name 'done' from Action, Part" at "message :apart from b to c;"
		--- */
		message :apart from b to c;
	}
}


````
