# OFFICIAL REPOSITORY FILE: SysML-v2-Pilot-Implementation/org.omg.kerml.xpect.tests/src/org/omg/kerml/xpect/tests/validation/Import_RootNamspace_invalid.kerml.xt

- repository: `SysML-v2-Pilot-Implementation`
- source_path: `org.omg.kerml.xpect.tests/src/org/omg/kerml/xpect/tests/validation/Import_RootNamspace_invalid.kerml.xt`
- source_url: https://github.com/Systems-Modeling/SysML-v2-Pilot-Implementation/blob/fa709f28dfd49dfdb7ee83e4e19da2f57e0eb3aa/org.omg.kerml.xpect.tests/src/org/omg/kerml/xpect/tests/validation/Import_RootNamspace_invalid.kerml.xt
- source_bytes: 583
- source_sha256: `80ea56e616e1ee83b4ee0e7eaee03c938b03d7fadbde2bc0ad4aed3fdeb477ce`
- decoded_as: `utf-8`


## EXACT SOURCE

````xtext
//* 
XPECT_SETUP org.omg.kerml.xpect.tests.validation.KerMLValidationTest
	ResourceSet {
		ThisFile {}
		File {from ="/library/Base.kerml"}
       	File {from ="/library/ScalarValues.kerml"}
	}
	Workspace {
		JavaProject {
			SrcFolder {
				ThisFile {}
				File {from ="/library/Base.kerml"}
		       	File {from ="/library/ScalarValues.kerml"}
			}
		}
	}
END_SETUP 
*/
// XPECT errors ---> "Top level import must be private" at "public import ScalarValues"
public import ScalarValues;

private import Import_RootNamespace;

package Import_RootNamespace {
}
````
