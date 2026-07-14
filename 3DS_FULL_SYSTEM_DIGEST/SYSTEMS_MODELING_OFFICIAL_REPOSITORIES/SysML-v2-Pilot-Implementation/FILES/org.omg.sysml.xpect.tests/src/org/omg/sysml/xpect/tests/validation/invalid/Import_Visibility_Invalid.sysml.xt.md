# OFFICIAL REPOSITORY FILE: SysML-v2-Pilot-Implementation/org.omg.sysml.xpect.tests/src/org/omg/sysml/xpect/tests/validation/invalid/Import_Visibility_Invalid.sysml.xt

- repository: `SysML-v2-Pilot-Implementation`
- source_path: `org.omg.sysml.xpect.tests/src/org/omg/sysml/xpect/tests/validation/invalid/Import_Visibility_Invalid.sysml.xt`
- source_url: https://github.com/Systems-Modeling/SysML-v2-Pilot-Implementation/blob/fa709f28dfd49dfdb7ee83e4e19da2f57e0eb3aa/org.omg.sysml.xpect.tests/src/org/omg/sysml/xpect/tests/validation/invalid/Import_Visibility_Invalid.sysml.xt
- source_bytes: 707
- source_sha256: `005952a924bf446e90a17c5a9f59d6a01aa47056422d606868d8bd6039c578d8`
- decoded_as: `utf-8`


## EXACT SOURCE

````xtext
//* 
XPECT_SETUP org.omg.sysml.xpect.tests.validation.invalid.SysMLTests
	ResourceSet {
		ThisFile {}
		File {from ="/library.kernel/Base.kerml"}
       	File {from ="/library.kernel/ScalarValues.kerml"}
	}
	Workspace {
		JavaProject {
			SrcFolder {
				ThisFile {}
				File {from ="/library.kernel/Base.kerml"}
		       	File {from ="/library.kernel/ScalarValues.kerml"}
			}
		}
	}
END_SETUP 
*/
package ImportVisibility {
	public import ScalarValues;
	private import ScalarValues;
	protected import ScalarValues;
	// XPECT errors ---> "mismatched input 'import' expecting '}'" at "import"
	import ScalarValues;
	// XPECT errors ---> "extraneous input '}' expecting EOF" at "}"
}
````
