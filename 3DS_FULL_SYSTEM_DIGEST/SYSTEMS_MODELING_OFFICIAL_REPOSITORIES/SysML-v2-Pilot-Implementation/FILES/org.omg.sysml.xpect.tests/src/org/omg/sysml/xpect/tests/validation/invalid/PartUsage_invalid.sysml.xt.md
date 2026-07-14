# OFFICIAL REPOSITORY FILE: SysML-v2-Pilot-Implementation/org.omg.sysml.xpect.tests/src/org/omg/sysml/xpect/tests/validation/invalid/PartUsage_invalid.sysml.xt

- repository: `SysML-v2-Pilot-Implementation`
- source_path: `org.omg.sysml.xpect.tests/src/org/omg/sysml/xpect/tests/validation/invalid/PartUsage_invalid.sysml.xt`
- source_url: https://github.com/Systems-Modeling/SysML-v2-Pilot-Implementation/blob/fa709f28dfd49dfdb7ee83e4e19da2f57e0eb3aa/org.omg.sysml.xpect.tests/src/org/omg/sysml/xpect/tests/validation/invalid/PartUsage_invalid.sysml.xt
- source_bytes: 3388
- source_sha256: `a9596bd692db8702746d98cf2b4959adeebd683418d702a2671e220b0cfeb070`
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
		File {from ="/library.kernel/ScalarValues.kerml"}
		File {from ="/library.systems/Items.sysml"}
		File {from ="/library.systems/Parts.sysml"}
		File {from ="/library.systems/Ports.sysml"}
		File {from ="/library.systems/Actions.sysml"}
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
				File {from ="/library.kernel/ScalarValues.kerml"}
				File {from ="/library.systems/Items.sysml"}
				File {from ="/library.systems/Parts.sysml"}
				File {from ="/library.systems/Ports.sysml"}
				File {from ="/library.systems/Actions.sysml"}
			}
		}
	}
END_SETUP 
*/
package pkg {
	public import ScalarValues::*;
	part def A {
		// XPECT errors --> "An occurrence, item or part must be typed by occurrence definitions." at "part p1: Real;"
		// XPECT warnings --> "Duplicate of inherited member name 'self' from DataValue, Part" at "part p1: Real;"
		part p1: Real;
		// XPECT errors --> "An occurrence, item or part must be typed by occurrence definitions." at "part p2: att;"
		// XPECT warnings --> "Duplicate of inherited member name 'self' from DataValue, Part" at "part p2: att;"
		part p2: att;
		// XPECT errors --> "An occurrence, item or part must be typed by occurrence definitions." at "part p3: act;"
		//* XPECT warnings ---
		 "Duplicate of inherited member name 'self' from Action, Part" at "part p3: act;"
		 "Duplicate of inherited member name 'start' from Action, Part" at "part p3: act;"
		 "Duplicate of inherited member name 'done' from Action, Part" at "part p3: act;"
		--- */
		part p3: act;
		// XPECT errors --> "An occurrence, item or part must be typed by occurrence definitions." at "part p4: AttDef;"
		// XPECT warnings --> "Duplicate of inherited member name 'self' from DataValue, Part" at "part p4: AttDef;"
		part p4: AttDef;
		// XPECT errors --> "An occurrence, item or part must be typed by occurrence definitions." at "part p5: PartDef::aPort;"
		// XPECT warnings --> "Duplicate of inherited member name 'self' from Part, Port" at "part p5: PartDef::aPort;"
		part p5: PartDef::aPort;
		// XPECT errors ---> "An occurrence, item or part must be typed by occurrence definitions." at "part p6: PartDef::aPart;"
		part p6: PartDef::aPart;
		// XPECT errors --> "An occurrence, item or part must be typed by occurrence definitions." at "part p7: PartDef, AttDef;"
		// XPECT warnings --> "Duplicate of inherited member name 'self' from DataValue, Part" at "part p7: PartDef, AttDef;"
		part p7: PartDef, AttDef;
	}
	attribute def AttDef;
	attribute att: AttDef;
	part def PartDef {
		port aPort;
		part aPart;
	}
	action act;
}

````
