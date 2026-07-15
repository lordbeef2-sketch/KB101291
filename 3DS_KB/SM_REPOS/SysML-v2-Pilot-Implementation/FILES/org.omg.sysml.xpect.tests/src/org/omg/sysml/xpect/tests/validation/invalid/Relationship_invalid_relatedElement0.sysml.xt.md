# OFFICIAL REPOSITORY FILE: SysML-v2-Pilot-Implementation/org.omg.sysml.xpect.tests/src/org/omg/sysml/xpect/tests/validation/invalid/Relationship_invalid_relatedElement0.sysml.xt

- repository: `SysML-v2-Pilot-Implementation`
- source_path: `org.omg.sysml.xpect.tests/src/org/omg/sysml/xpect/tests/validation/invalid/Relationship_invalid_relatedElement0.sysml.xt`
- source_url: https://github.com/Systems-Modeling/SysML-v2-Pilot-Implementation/blob/fa709f28dfd49dfdb7ee83e4e19da2f57e0eb3aa/org.omg.sysml.xpect.tests/src/org/omg/sysml/xpect/tests/validation/invalid/Relationship_invalid_relatedElement0.sysml.xt
- source_bytes: 1167
- source_sha256: `d48e4afacdcc26a2319ac4b5712662e52ce77f69123da4025427532e02b813f5`
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
		File {from ="/library.systems/Items.sysml"}
		File {from ="/library.systems/Parts.sysml"}
		File {from ="/library.systems/Connections.sysml"}
	}
	Workspace {
		JavaProject {
			SrcFolder {
				ThisFile {}
				File {from ="/library.kernel/Base.kerml"}
				File {from ="/library.kernel/Links.kerml"}
        		File {from ="/library.kernel/Occurrences.kerml"}
 		      	File {from ="/library.kernel/Objects.kerml"}
 				File {from ="/library.systems/Items.sysml"}
				File {from ="/library.systems/Parts.sysml"}
				File {from ="/library.systems/Connections.sysml"}
			}
		}
	}
END_SETUP 
*/
package Relationship_invalid_relatedElement {
	part v {
		part b0;
		// XPECT errors ---> "Must have at least two related elements" at "connection { end ::> b0; }"
		connection { end ::> b0; }
		
		abstract connection { end ::> b0; }	
	} 
}
````
