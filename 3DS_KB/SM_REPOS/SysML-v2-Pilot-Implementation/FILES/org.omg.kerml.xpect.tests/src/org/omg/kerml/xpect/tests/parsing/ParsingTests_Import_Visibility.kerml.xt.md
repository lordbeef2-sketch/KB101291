# OFFICIAL REPOSITORY FILE: SysML-v2-Pilot-Implementation/org.omg.kerml.xpect.tests/src/org/omg/kerml/xpect/tests/parsing/ParsingTests_Import_Visibility.kerml.xt

- repository: `SysML-v2-Pilot-Implementation`
- source_path: `org.omg.kerml.xpect.tests/src/org/omg/kerml/xpect/tests/parsing/ParsingTests_Import_Visibility.kerml.xt`
- source_url: https://github.com/Systems-Modeling/SysML-v2-Pilot-Implementation/blob/fa709f28dfd49dfdb7ee83e4e19da2f57e0eb3aa/org.omg.kerml.xpect.tests/src/org/omg/kerml/xpect/tests/parsing/ParsingTests_Import_Visibility.kerml.xt
- source_bytes: 674
- source_sha256: `06a861b5520daec576c9937e243e581d07e33a13f17994d3e31bfe787390e865`
- decoded_as: `utf-8`


## EXACT SOURCE

````xtext
//* 
XPECT_SETUP org.omg.kerml.xpect.tests.parsing.KerMLParsingTest
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
package ImportVisibility {
	public import ScalarValues;
	private import ScalarValues;
	protected import ScalarValues;
	// XPECT errors ---> "mismatched input 'import' expecting '}'" at "import"
	import ScalarValues;
	// XPECT errors ---> "extraneous input '}' expecting EOF" at "}"
}
````
