# OFFICIAL REPOSITORY FILE: SysML-v2-Pilot-Implementation/org.omg.kerml.xpect.tests/src/org/omg/kerml/xpect/tests/validation/Redefinition_End_Invalid.kerml.xt

- repository: `SysML-v2-Pilot-Implementation`
- source_path: `org.omg.kerml.xpect.tests/src/org/omg/kerml/xpect/tests/validation/Redefinition_End_Invalid.kerml.xt`
- source_url: https://github.com/Systems-Modeling/SysML-v2-Pilot-Implementation/blob/fa709f28dfd49dfdb7ee83e4e19da2f57e0eb3aa/org.omg.kerml.xpect.tests/src/org/omg/kerml/xpect/tests/validation/Redefinition_End_Invalid.kerml.xt
- source_bytes: 850
- source_sha256: `73c023e60c69ea08578ca25f1934f4feacadc11aac78852057207c71849d86e5`
- decoded_as: `utf-8`


## EXACT SOURCE

````xtext
//* 
XPECT_SETUP org.omg.kerml.xpect.tests.validation.KerMLValidationTest
	ResourceSet {
       ThisFile {}
        File {from ="/library/Base.kerml"}
        File {from ="/library/Occurrences.kerml"}
        File {from ="/library/Objects.kerml"}
        File {from ="/library/Performances.kerml"}
    }
    Workspace {
        JavaProject {
            SrcFolder {
                ThisFile {}
		            File {from ="/library/Base.kerml"}
		            File {from ="/library/Occurrences.kerml"}
		            File {from ="/library/Objects.kerml"}
		            File {from ="/library/Performances.kerml"}
			}
		}
	}
END_SETUP 
*/
package RedefinitionEnd {
	classifier A {
		end feature e[1];
	}
	
	classifier B :> A {
		// XPECT errors ---> "Redefining feature must be an end feature" at "e"
		feature :>> e;
	}

}
````
