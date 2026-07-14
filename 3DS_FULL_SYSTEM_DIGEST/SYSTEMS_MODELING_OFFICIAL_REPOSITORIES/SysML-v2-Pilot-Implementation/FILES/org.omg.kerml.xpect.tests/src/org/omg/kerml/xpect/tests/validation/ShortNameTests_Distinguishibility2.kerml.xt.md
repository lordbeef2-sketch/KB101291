# OFFICIAL REPOSITORY FILE: SysML-v2-Pilot-Implementation/org.omg.kerml.xpect.tests/src/org/omg/kerml/xpect/tests/validation/ShortNameTests_Distinguishibility2.kerml.xt

- repository: `SysML-v2-Pilot-Implementation`
- source_path: `org.omg.kerml.xpect.tests/src/org/omg/kerml/xpect/tests/validation/ShortNameTests_Distinguishibility2.kerml.xt`
- source_url: https://github.com/Systems-Modeling/SysML-v2-Pilot-Implementation/blob/fa709f28dfd49dfdb7ee83e4e19da2f57e0eb3aa/org.omg.kerml.xpect.tests/src/org/omg/kerml/xpect/tests/validation/ShortNameTests_Distinguishibility2.kerml.xt
- source_bytes: 526
- source_sha256: `04517d3c46e16244e3497f71ca5095d1a054418ee8bb068b3d75181b2d32a2a6`
- decoded_as: `utf-8`


## EXACT SOURCE

````xtext
//* 
XPECT_SETUP org.omg.kerml.xpect.tests.parsing.KerMLParsingTest
	ResourceSet {
		ThisFile {}
		File {from ="/library/Base.kerml"}
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
	 //name and id are the same
	 //XPECT warnings --> "Duplicate of other owned member name" at "two"
	 classifier <one> two;
	  //XPECT warnings --> "Duplicate of other owned member name" at "two"
	 classifier <two> three;
}

````
