# OFFICIAL REPOSITORY FILE: SysML-v2-Pilot-Implementation/org.omg.sysml.xpect.tests/src/org/omg/sysml/xpect/tests/validation/invalid/ConstraintUsage_Invalid.sysml.xt

- repository: `SysML-v2-Pilot-Implementation`
- source_path: `org.omg.sysml.xpect.tests/src/org/omg/sysml/xpect/tests/validation/invalid/ConstraintUsage_Invalid.sysml.xt`
- source_url: https://github.com/Systems-Modeling/SysML-v2-Pilot-Implementation/blob/fa709f28dfd49dfdb7ee83e4e19da2f57e0eb3aa/org.omg.sysml.xpect.tests/src/org/omg/sysml/xpect/tests/validation/invalid/ConstraintUsage_Invalid.sysml.xt
- source_bytes: 2070
- source_sha256: `a6440cb3e4b2982035b913daf61a1b95c3494ea940c9c36cbbc50632d31b9098`
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
		File {from ="/library.systems/Items.sysml"}
		File {from ="/library.systems/Parts.sysml"}
		File {from ="/library.systems/Ports.sysml"}
		File {from ="/library.systems/Constraints.sysml"}
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
				File {from ="/library.systems/Items.sysml"}
				File {from ="/library.systems/Parts.sysml"}
				File {from ="/library.systems/Ports.sysml"}
				File {from ="/library.systems/Constraints.sysml"}
			}
		}
	}
END_SETUP 
*/
package pkg {
	constraint def AConstraint;
	constraint def AConstraint1;
	part def ABlock {
		// XPECT errors ---> "A constraint must be typed by one constraint definition." at "assert constraint two_types : AConstraint, ABlock;"
		// XPECT warnings ---> "Duplicate of inherited member name 'self' from ConstraintCheck, Part" at "assert constraint two_types : AConstraint, ABlock;"
		assert constraint two_types : AConstraint, ABlock;
		// XPECT errors ---> "A constraint must be typed by one constraint definition." at "assert constraint aConstraint0 : ABlock;"
		// XPECT warnings ---> "Duplicate of inherited member name 'self' from ConstraintCheck, Part" at "assert constraint aConstraint0: ABlock;"
		assert constraint aConstraint0: ABlock;
		//XPECT errors ---> "A constraint must be typed by one constraint definition." at "assert constraint aConstraint1 : AConstraint, AConstraint1;"
		assert constraint aConstraint1 : AConstraint, AConstraint1;
	}	
}
````
