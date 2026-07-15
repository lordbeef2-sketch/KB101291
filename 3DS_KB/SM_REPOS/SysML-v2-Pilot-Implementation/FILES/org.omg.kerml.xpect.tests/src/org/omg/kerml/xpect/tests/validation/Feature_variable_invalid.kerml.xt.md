# OFFICIAL REPOSITORY FILE: SysML-v2-Pilot-Implementation/org.omg.kerml.xpect.tests/src/org/omg/kerml/xpect/tests/validation/Feature_variable_invalid.kerml.xt

- repository: `SysML-v2-Pilot-Implementation`
- source_path: `org.omg.kerml.xpect.tests/src/org/omg/kerml/xpect/tests/validation/Feature_variable_invalid.kerml.xt`
- source_url: https://github.com/Systems-Modeling/SysML-v2-Pilot-Implementation/blob/fa709f28dfd49dfdb7ee83e4e19da2f57e0eb3aa/org.omg.kerml.xpect.tests/src/org/omg/kerml/xpect/tests/validation/Feature_variable_invalid.kerml.xt
- source_bytes: 1145
- source_sha256: `822bbddc1aac174fd0b0136987bfdef89d508777ffe810fe8d2ee6055511aaeb`
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

        }
        Workspace {
                JavaProject {
                        SrcFolder {
                                ThisFile {}
                                File {from ="/library/Base.kerml"}
                                File {from ="/library/Links.kerml"}
                                File {from ="/library/Occurrences.kerml"}
                 				File {from ="/library/Objects.kerml"}

                        }
                }
        }
END_SETUP 
*/

package Feature_variable_invalid {
	
	class C {
		var feature x;
		// XPECT errors ---> "A portion cannot be variable" at "portion var feature y;"
		portion var feature y;
	}
	
	datatype D {
		// XPECT errors ---> "Must be owned by an occurrence type" at "var feature z;"
		var feature z;
	}
	
}
````
