# OFFICIAL REPOSITORY FILE: SysML-v2-Pilot-Implementation/org.omg.kerml.xpect.tests/src/org/omg/kerml/xpect/tests/validation/ShortNameTests_Distinguishibility1.kerml.xt

- repository: `SysML-v2-Pilot-Implementation`
- source_path: `org.omg.kerml.xpect.tests/src/org/omg/kerml/xpect/tests/validation/ShortNameTests_Distinguishibility1.kerml.xt`
- source_url: https://github.com/Systems-Modeling/SysML-v2-Pilot-Implementation/blob/fa709f28dfd49dfdb7ee83e4e19da2f57e0eb3aa/org.omg.kerml.xpect.tests/src/org/omg/kerml/xpect/tests/validation/ShortNameTests_Distinguishibility1.kerml.xt
- source_bytes: 527
- source_sha256: `20ae2a5531331c12367027ed5e212331375648a868afa57d6802055f98067961`
- decoded_as: `utf-8`


## EXACT SOURCE

````xtext
//* 
XPECT_SETUP org.omg.kerml.xpect.tests.parsing.KerMLParsingTest
	ResourceSet {
		File {from ="/library/Base.kerml"}
		ThisFile {}
	}
	Workspace {
		JavaProject {
			SrcFolder {
				ThisFile {}
				File {from ="/library/Base.kerml"}
			}
		}
	}
END_SETUP 
*/

package Test {
	 //short names are the same
	 //XPECT warnings --> "Duplicate of other owned member name" at "one"
	 classifier <one> two;
	 //XPECT warnings --> "Duplicate of other owned member name" at "one"
	 classifier <one> three;
}


````
