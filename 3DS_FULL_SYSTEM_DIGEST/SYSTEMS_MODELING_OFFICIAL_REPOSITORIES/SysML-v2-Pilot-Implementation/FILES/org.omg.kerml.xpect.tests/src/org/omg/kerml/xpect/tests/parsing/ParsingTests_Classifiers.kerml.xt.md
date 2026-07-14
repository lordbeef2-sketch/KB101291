# OFFICIAL REPOSITORY FILE: SysML-v2-Pilot-Implementation/org.omg.kerml.xpect.tests/src/org/omg/kerml/xpect/tests/parsing/ParsingTests_Classifiers.kerml.xt

- repository: `SysML-v2-Pilot-Implementation`
- source_path: `org.omg.kerml.xpect.tests/src/org/omg/kerml/xpect/tests/parsing/ParsingTests_Classifiers.kerml.xt`
- source_url: https://github.com/Systems-Modeling/SysML-v2-Pilot-Implementation/blob/fa709f28dfd49dfdb7ee83e4e19da2f57e0eb3aa/org.omg.kerml.xpect.tests/src/org/omg/kerml/xpect/tests/parsing/ParsingTests_Classifiers.kerml.xt
- source_bytes: 881
- source_sha256: `bbd1384ec23af03e0ce2d64f2868eb80534a44f2565ceb64e42302b90c0c9f29`
- decoded_as: `utf-8`


## EXACT SOURCE

````xtext
//* XPECT_SETUP org.omg.kerml.xpect.tests.parsing.KerMLParsingTest
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

// XPECT noErrors ---> ""
package Classifiers {
	classifier A;
	classifier B;
	
	specialization Super subclassifier A specializes B;
	specialization subclassifier B :> A;
	
	subclassifier C specializes A;
	subclassifier C specializes B;
	
	classifier C specializes A, B;
	
	classifier D disjoint from C differences A, B;
	classifier E specializes C intersects A, B;
	classifier F unions A unions B;
}

````
