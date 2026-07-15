# OFFICIAL REPOSITORY FILE: SysML-v2-Pilot-Implementation/org.omg.sysml.xpect.tests/src/org/omg/sysml/xpect/tests/validation/invalid/Relationship_invalid_relatedElement1.sysml.xt

- repository: `SysML-v2-Pilot-Implementation`
- source_path: `org.omg.sysml.xpect.tests/src/org/omg/sysml/xpect/tests/validation/invalid/Relationship_invalid_relatedElement1.sysml.xt`
- source_url: https://github.com/Systems-Modeling/SysML-v2-Pilot-Implementation/blob/fa709f28dfd49dfdb7ee83e4e19da2f57e0eb3aa/org.omg.sysml.xpect.tests/src/org/omg/sysml/xpect/tests/validation/invalid/Relationship_invalid_relatedElement1.sysml.xt
- source_bytes: 2024
- source_sha256: `ed73c7a0d749a2af2a7d2747c825a49369c6d10cc6e9e4e2fc104657f1399c87`
- decoded_as: `utf-8`


## EXACT SOURCE

````xtext
//* XPECT_SETUP org.omg.sysml.xpect.tests.validation.invalid.SysMLTests
	ResourceSet {
		ThisFile {}
		File {from ="/library.kernel/Base.kerml"}
		File {from ="/library.kernel/Links.kerml"}
       	File {from ="/library.kernel/Occurrences.kerml"}
       	File {from ="/library.kernel/Objects.kerml"}
       	File {from ="/library.kernel/Performances.kerml"}
		File {from ="/library.kernel/BaseFunctions.kerml"}
		File {from ="/library.kernel/Transfers.kerml"}
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
				File {from ="/library.kernel/BaseFunctions.kerml"}
				File {from ="/library.kernel/Transfers.kerml"}
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
package 'Streaming Example' {
	
	part def  A {
		part def B {
			out ref myOut;
		}
		part def C {
			in ref myIn;
		}
		//* XPECT errors ---
			"Cannot identify flow end (use dot notation)" at "B::myOut"
			"Cannot identify flow end (use dot notation)" at "C::myIn"
			"Must be an accessible feature (use dot notation for nesting)" at "B::myOut"
			"Must be an accessible feature (use dot notation for nesting)" at "C::myIn"
			"Must have at least two related elements" at "flow XXX from B::myOut to C::myIn;"
		    --- */
		flow XXX from B::myOut to C::myIn;	
	} 
}
````
