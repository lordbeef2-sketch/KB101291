# OFFICIAL REPOSITORY FILE: SysML-v2-Pilot-Implementation/org.omg.kerml.xpect.tests/src/org/omg/kerml/xpect/tests/parsing/ParsingTests_Scoping.kerml.xt

- repository: `SysML-v2-Pilot-Implementation`
- source_path: `org.omg.kerml.xpect.tests/src/org/omg/kerml/xpect/tests/parsing/ParsingTests_Scoping.kerml.xt`
- source_url: https://github.com/Systems-Modeling/SysML-v2-Pilot-Implementation/blob/fa709f28dfd49dfdb7ee83e4e19da2f57e0eb3aa/org.omg.kerml.xpect.tests/src/org/omg/kerml/xpect/tests/parsing/ParsingTests_Scoping.kerml.xt
- source_bytes: 1565
- source_sha256: `35925147af5d5f108913a57f53636af3da0c4ec5ab8c2d9ad750c42d03fac812`
- decoded_as: `utf-8`


## EXACT SOURCE

````xtext
//* XPECT_SETUP org.omg.kerml.xpect.tests.parsing.KerMLParsingTest
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

// XPECT noErrors ---> ""
package Scoping {
    package P1 {
        class A {
            feature f;
        }
        package P2 {
            class A {
                feature g;
            }
            package P3 {
                class B :> A {
                    feature :>> g;
                }
            }
        }
        package Objects {
            class Object {
                feature test1;
            }
        }
        package '$' {
            class Objects {
                class Object {
                    feature test2;
                }
            }
        }
        package P4 {
            class C :> Objects::Object {
                feature :>> test1;
            }
            class D :> '$'::Objects::Object {
                feature :>> test2;
            }
            class E :> $::Objects::Object {
                feature :>> subobjects;
            }
        }
    }
}
````
