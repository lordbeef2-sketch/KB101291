# OFFICIAL REPOSITORY FILE: SysML-v2-Pilot-Implementation/org.omg.kerml.xpect.tests/src/org/omg/kerml/xpect/tests/linking/Classes.kerml.xt

- repository: `SysML-v2-Pilot-Implementation`
- source_path: `org.omg.kerml.xpect.tests/src/org/omg/kerml/xpect/tests/linking/Classes.kerml.xt`
- source_url: https://github.com/Systems-Modeling/SysML-v2-Pilot-Implementation/blob/fa709f28dfd49dfdb7ee83e4e19da2f57e0eb3aa/org.omg.kerml.xpect.tests/src/org/omg/kerml/xpect/tests/linking/Classes.kerml.xt
- source_bytes: 667
- source_sha256: `523ee437d5a32cfb7ee11c70d44d6adc89a1e4397ebf2cdb29e81f9478526faf`
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

private import Classes2::*;
package Classes1 {
	// XPECT linkedName at A --> Classes2.A
	private class B specializes A {
		private y: A;
	} 
	
}

````
