# OFFICIAL REPOSITORY FILE: SysML-v2-Pilot-Implementation/org.omg.kerml.xpect.tests/src/org/omg/kerml/xpect/tests/validation/LibraryPackage_invalid_notStandard.kerml.xt

- repository: `SysML-v2-Pilot-Implementation`
- source_path: `org.omg.kerml.xpect.tests/src/org/omg/kerml/xpect/tests/validation/LibraryPackage_invalid_notStandard.kerml.xt`
- source_url: https://github.com/Systems-Modeling/SysML-v2-Pilot-Implementation/blob/fa709f28dfd49dfdb7ee83e4e19da2f57e0eb3aa/org.omg.kerml.xpect.tests/src/org/omg/kerml/xpect/tests/validation/LibraryPackage_invalid_notStandard.kerml.xt
- source_bytes: 409
- source_sha256: `d49d29991b10eb31f96b27be464b093703f7da9189a76dd4b46eaa06485723e5`
- decoded_as: `utf-8`


## EXACT SOURCE

````xtext
//* 
XPECT_SETUP org.omg.kerml.xpect.tests.validation.KerMLValidationTest
	ResourceSet {
		ThisFile {}
	}
	Workspace {
		JavaProject {
			SrcFolder {
				ThisFile {}
			}
		}
	}
END_SETUP 
*/
//XPECT warnings --> "User library packages should not be marked as standard" at "standard"
standard library package LibraryPackage_invalid_notStandard {
	
	library package LibraryPackage_valid;
	
}
````
