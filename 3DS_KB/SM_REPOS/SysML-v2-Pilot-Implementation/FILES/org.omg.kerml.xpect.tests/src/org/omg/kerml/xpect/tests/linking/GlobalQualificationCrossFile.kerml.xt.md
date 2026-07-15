# OFFICIAL REPOSITORY FILE: SysML-v2-Pilot-Implementation/org.omg.kerml.xpect.tests/src/org/omg/kerml/xpect/tests/linking/GlobalQualificationCrossFile.kerml.xt

- repository: `SysML-v2-Pilot-Implementation`
- source_path: `org.omg.kerml.xpect.tests/src/org/omg/kerml/xpect/tests/linking/GlobalQualificationCrossFile.kerml.xt`
- source_url: https://github.com/Systems-Modeling/SysML-v2-Pilot-Implementation/blob/fa709f28dfd49dfdb7ee83e4e19da2f57e0eb3aa/org.omg.kerml.xpect.tests/src/org/omg/kerml/xpect/tests/linking/GlobalQualificationCrossFile.kerml.xt
- source_bytes: 908
- source_sha256: `3253a7d05b152f6b7cbb1c9911f8931e9746fb7810e2cfbbf3f67b3b9707cac4`
- decoded_as: `utf-8`


## EXACT SOURCE

````xtext
//* 
XPECT_SETUP org.omg.kerml.xpect.tests.linking.KerMLLinkingTest
	ResourceSet {
		ThisFile {}
		File {from ="/library/Base.kerml"}
		File {from ="/library/Occurrences.kerml"}
		File {from ="/library/Objects.kerml"}
		File "Classes2.kerml" {}
	}
	Workspace {
		JavaProject {
			SrcFolder {
				ThisFile {}
				File {from ="/library/Base.kerml"}
				File {from ="/library/Occurrences.kerml"}
				File {from ="/library/Objects.kerml"}
				File "Classes2.kerml" {}
			}
		}
	}
END_SETUP 
*/

package Classes1 {
	private import Classes2::*;
	
	package Classes2;
	class A;
	
	// XPECT linkedName at A --> Classes2.A
	private class B specializes $::Classes2::A {
		// XPECT linkedName at A --> Classes1.A
		private y: A;
		// XPECT linkedName at A --> Classes1.$.Classes2.A
		feature x : '$'::Classes2::A; 
	} 
	
	package '$' {
		class Classes2 {
			class A;
		}
	}	
}

````
