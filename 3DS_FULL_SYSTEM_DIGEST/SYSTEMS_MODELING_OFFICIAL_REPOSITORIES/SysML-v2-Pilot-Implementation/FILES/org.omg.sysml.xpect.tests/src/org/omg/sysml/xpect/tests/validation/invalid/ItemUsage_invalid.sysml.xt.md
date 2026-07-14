# OFFICIAL REPOSITORY FILE: SysML-v2-Pilot-Implementation/org.omg.sysml.xpect.tests/src/org/omg/sysml/xpect/tests/validation/invalid/ItemUsage_invalid.sysml.xt

- repository: `SysML-v2-Pilot-Implementation`
- source_path: `org.omg.sysml.xpect.tests/src/org/omg/sysml/xpect/tests/validation/invalid/ItemUsage_invalid.sysml.xt`
- source_url: https://github.com/Systems-Modeling/SysML-v2-Pilot-Implementation/blob/fa709f28dfd49dfdb7ee83e4e19da2f57e0eb3aa/org.omg.sysml.xpect.tests/src/org/omg/sysml/xpect/tests/validation/invalid/ItemUsage_invalid.sysml.xt
- source_bytes: 3394
- source_sha256: `b2b39c2706b717e1949c88cd03a21c0a8e5814ce8052bc8a69cbafde9c53300b`
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
	item def A {
		// XPECT errors --> "An occurrence, item or part must be typed by occurrence definitions." at "item i1: Real;"
		// XPECT warnings --> "Duplicate of inherited member name 'self' from DataValue, Item" at "item i1: Real;"
		item i1: Real;
		// XPECT errors --> "An occurrence, item or part must be typed by occurrence definitions." at "item i2: att;"
		// XPECT warnings --> "Duplicate of inherited member name 'self' from DataValue, Item" at "item i2: att;"
		item i2: att;
		// XPECT errors --> "An occurrence, item or part must be typed by occurrence definitions." at "item i3: act;"
		//* XPECT warnings ---
		   "Duplicate of inherited member name 'self' from Action, Item" at "item i3: act;"
		   "Duplicate of inherited member name 'start' from Action, Item" at "item i3: act;"
		   "Duplicate of inherited member name 'done' from Action, Item" at "item i3: act;"
		--- */
		item i3: act;
		// XPECT errors --> "An occurrence, item or part must be typed by occurrence definitions." at "item i4: AttDef;"
		// XPECT warnings --> "Duplicate of inherited member name 'self' from DataValue, Item" at "item i4: AttDef;"
		item i4: AttDef;
		// XPECT errors ---> "An occurrence, item or part must be typed by occurrence definitions." at "item i5: PartDef::aPort;"
		// XPECT warnings --> "Duplicate of inherited member name 'self' from Item, Port" at "item i5: PartDef::aPort;"
		item i5: PartDef::aPort;
		// XPECT errors ---> "An occurrence, item or part must be typed by occurrence definitions." at "item i6: PartDef::aPart;"
		item i6: PartDef::aPart;
		// XPECT errors --> "An occurrence, item or part must be typed by occurrence definitions." at "item i7: PartDef, AttDef;"
		// XPECT warnings --> "Duplicate of inherited member name 'self' from DataValue, Part" at "item i7: PartDef, AttDef;"
		item i7: PartDef, AttDef;
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
