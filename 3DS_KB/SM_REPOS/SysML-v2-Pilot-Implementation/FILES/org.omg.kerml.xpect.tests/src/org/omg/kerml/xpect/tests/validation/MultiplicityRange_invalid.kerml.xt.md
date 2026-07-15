# OFFICIAL REPOSITORY FILE: SysML-v2-Pilot-Implementation/org.omg.kerml.xpect.tests/src/org/omg/kerml/xpect/tests/validation/MultiplicityRange_invalid.kerml.xt

- repository: `SysML-v2-Pilot-Implementation`
- source_path: `org.omg.kerml.xpect.tests/src/org/omg/kerml/xpect/tests/validation/MultiplicityRange_invalid.kerml.xt`
- source_url: https://github.com/Systems-Modeling/SysML-v2-Pilot-Implementation/blob/fa709f28dfd49dfdb7ee83e4e19da2f57e0eb3aa/org.omg.kerml.xpect.tests/src/org/omg/kerml/xpect/tests/validation/MultiplicityRange_invalid.kerml.xt
- source_bytes: 1811
- source_sha256: `eeef99b3fc9f2764bf96312af60591c2db68d163cb5ea25826181dc373c584a5`
- decoded_as: `utf-8`


## EXACT SOURCE

````xtext
//* XPECT_SETUP org.omg.kerml.xpect.tests.validation.KerMLValidationTest
        ResourceSet {
                ThisFile {}
                File {from ="/library/Base.kerml"}
                File {from ="/library/Links.kerml"}
                File {from ="/library/Occurrences.kerml"}
                File {from ="/library/Objects.kerml"}
				File {from ="/library/Performances.kerml"}
				File {from ="/library/ScalarValues.kerml"}
				File {from ="/library/BaseFunctions.kerml"}
				File {from ="/library/DataFunctions.kerml"}
        }
        Workspace {
                JavaProject {
                        SrcFolder {
                                ThisFile {}
                                File {from ="/library/Base.kerml"}
                                File {from ="/library/Occurrences.kerml"}
                 				File {from ="/library/Objects.kerml"}
								File {from ="/library/Performances.kerml"}
								File {from ="/library/ScalarValues.kerml"}
								File {from ="/library/BaseFunctions.kerml"}
								File {from ="/library/DataFunctions.kerml"}
                        }
                }
        }
END_SETUP
*/

package MultiplicityRange {
	// XPECT errors ---> "Must have a Natural value" at "false"
	feature f [1..false];
	
	feature n = 0;
	feature b = n > 3;
	
	// XPECT errors ---> "Must have a Natural value" at "b"
	feature g1 [n..b];
	
	feature m1 = n - 1;
	feature m2 = 2 - m1;
	// XPECT errors ---> "Must have a Natural value" at "m1"
	feature g2 [m1..m2];
	
	function I{ return result : ScalarValues::Integer; }
	feature b1 = I() > 3;
	feature i1 = I();
	// XPECT errors ---> "Must have a Natural value" at "b1"
	feature g3 [b1..i1];
	
	// XPECT errors ---> "Must have a Natural value" at ""x""
	feature h ["x"..*];
}

````
