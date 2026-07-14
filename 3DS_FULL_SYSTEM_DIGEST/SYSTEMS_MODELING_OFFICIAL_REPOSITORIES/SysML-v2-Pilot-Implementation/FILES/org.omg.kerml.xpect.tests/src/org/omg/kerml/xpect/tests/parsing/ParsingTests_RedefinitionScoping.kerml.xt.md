# OFFICIAL REPOSITORY FILE: SysML-v2-Pilot-Implementation/org.omg.kerml.xpect.tests/src/org/omg/kerml/xpect/tests/parsing/ParsingTests_RedefinitionScoping.kerml.xt

- repository: `SysML-v2-Pilot-Implementation`
- source_path: `org.omg.kerml.xpect.tests/src/org/omg/kerml/xpect/tests/parsing/ParsingTests_RedefinitionScoping.kerml.xt`
- source_url: https://github.com/Systems-Modeling/SysML-v2-Pilot-Implementation/blob/fa709f28dfd49dfdb7ee83e4e19da2f57e0eb3aa/org.omg.kerml.xpect.tests/src/org/omg/kerml/xpect/tests/parsing/ParsingTests_RedefinitionScoping.kerml.xt
- source_bytes: 935
- source_sha256: `ed36769eda7cb5912485c05f2e1e1fa0ca06329d6bd10cd3805637ef37d16a12`
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
package RedefinitionScoping {
	
    classifier A {
        feature x { 
            feature y;
        }
    }
    
    classifier B specializes A {
        feature x redefines x {
            // Should redefine A::x::y.
            feature redefines x::y;
        }
    }
    
    classifier C {
        feature x;
        feature y {
            // Should redefine C::x.
            feature redefines x;
        }
    }

}

````
