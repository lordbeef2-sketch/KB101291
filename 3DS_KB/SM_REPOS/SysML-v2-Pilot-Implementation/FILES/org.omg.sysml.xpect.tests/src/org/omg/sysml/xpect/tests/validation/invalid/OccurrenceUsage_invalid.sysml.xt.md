# OFFICIAL REPOSITORY FILE: SysML-v2-Pilot-Implementation/org.omg.sysml.xpect.tests/src/org/omg/sysml/xpect/tests/validation/invalid/OccurrenceUsage_invalid.sysml.xt

- repository: `SysML-v2-Pilot-Implementation`
- source_path: `org.omg.sysml.xpect.tests/src/org/omg/sysml/xpect/tests/validation/invalid/OccurrenceUsage_invalid.sysml.xt`
- source_url: https://github.com/Systems-Modeling/SysML-v2-Pilot-Implementation/blob/fa709f28dfd49dfdb7ee83e4e19da2f57e0eb3aa/org.omg.sysml.xpect.tests/src/org/omg/sysml/xpect/tests/validation/invalid/OccurrenceUsage_invalid.sysml.xt
- source_bytes: 2807
- source_sha256: `f46a4adae2b1b8e6c82781a820d763cf27534c8163bfbeff47d8e6faad739309`
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
	occurrence def A {
		// XPECT errors --> "An occurrence, item or part must be typed by occurrence definitions." at "occurrence areal: Real;"
		// XPECT warnings --> "Duplicate of inherited member name 'self' from DataValue, Occurrence" at "occurrence areal: Real;"
		occurrence areal: Real;
		// XPECT errors --> "An occurrence, item or part must be typed by occurrence definitions." at "occurrence avalue :> aValue;"
		// XPECT warnings --> "Duplicate of inherited member name 'self' from DataValue, Occurrence" at "occurrence avalue :> aValue;"
		occurrence avalue:> aValue;
		// XPECT errors --> "An occurrence, item or part must be typed by occurrence definitions." at "occurrence twoTypes: PartDef, Real;"
		// XPECT warnings --> "Duplicate of inherited member name 'self' from DataValue, Part" at "occurrence twoTypes: PartDef, Real;"
		occurrence twoTypes: PartDef, Real;
	}
	attribute aValue: Real;
	part def PartDef;
	part aPart: PartDef;	
	ref a : A;

	// XPECT errors --> "Must reference an occurrence." at "a"
	event a;

	// XPECT errors --> "An occurrence, item or part must be typed by occurrence definitions." at "event a.areal;"
	//* XPECT warnings ---
	   "Duplicate of inherited member name 'self' from DataValue, Occurrence" at "event a.areal;"
	   "Duplicate of inherited member name 'self' from DataValue, Occurrence" at "a.areal"
	--- */
	event a.areal;	
}
````
