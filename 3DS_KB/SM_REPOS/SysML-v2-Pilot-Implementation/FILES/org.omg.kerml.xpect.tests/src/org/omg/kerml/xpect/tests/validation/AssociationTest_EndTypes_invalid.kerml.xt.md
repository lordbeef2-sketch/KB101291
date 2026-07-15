# OFFICIAL REPOSITORY FILE: SysML-v2-Pilot-Implementation/org.omg.kerml.xpect.tests/src/org/omg/kerml/xpect/tests/validation/AssociationTest_EndTypes_invalid.kerml.xt

- repository: `SysML-v2-Pilot-Implementation`
- source_path: `org.omg.kerml.xpect.tests/src/org/omg/kerml/xpect/tests/validation/AssociationTest_EndTypes_invalid.kerml.xt`
- source_url: https://github.com/Systems-Modeling/SysML-v2-Pilot-Implementation/blob/fa709f28dfd49dfdb7ee83e4e19da2f57e0eb3aa/org.omg.kerml.xpect.tests/src/org/omg/kerml/xpect/tests/validation/AssociationTest_EndTypes_invalid.kerml.xt
- source_bytes: 1064
- source_sha256: `6800f775fcfd282f8182c24a8908985d89298ac4c7cf078f96894f57a3604ca5`
- decoded_as: `utf-8`


## EXACT SOURCE

````xtext
//* 
XPECT_SETUP org.omg.kerml.xpect.tests.parsing.KerMLParsingTest
	ResourceSet {
		ThisFile {}
		File {from ="/library/Base.kerml"}
		File {from ="/library/Links.kerml"}
		File {from ="/library/Occurrences.kerml"}
		File {from ="/library/Objects.kerml"}
		File {from ="/library/Performances.kerml"}
	}
	Workspace {
		JavaProject {
			SrcFolder {
				ThisFile {}
				File {from ="/library/Base.kerml"}
				File {from ="/library/Links.kerml"}
				File {from ="/library/Occurrences.kerml"}
				File {from ="/library/Objects.kerml"}
				File {from ="/library/Performances.kerml"}
			}
		}
	}
END_SETUP 
*/
package AssociationTest_EndTypes_invalid {
	class C1;	
	class C2;
	class C3 specializes C1;
	
	assoc A1 {
		end x : C1;
		// XPECT errors --> "An association end must have exactly one type" at "end y : C1, C2;"
		end y : C1, C2;
	}
	
	assoc A2 specializes A1 {
		// XPECT errors --> "An association end must have exactly one type" at "end x : C2;"
		end x : C2;
	}
	
	assoc A3 specializes A1 {
		end x : C3;
	}
	
}

````
