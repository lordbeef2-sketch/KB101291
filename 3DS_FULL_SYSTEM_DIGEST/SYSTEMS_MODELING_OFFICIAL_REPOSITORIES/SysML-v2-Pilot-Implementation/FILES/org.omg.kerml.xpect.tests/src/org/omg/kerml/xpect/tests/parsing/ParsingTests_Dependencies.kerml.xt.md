# OFFICIAL REPOSITORY FILE: SysML-v2-Pilot-Implementation/org.omg.kerml.xpect.tests/src/org/omg/kerml/xpect/tests/parsing/ParsingTests_Dependencies.kerml.xt

- repository: `SysML-v2-Pilot-Implementation`
- source_path: `org.omg.kerml.xpect.tests/src/org/omg/kerml/xpect/tests/parsing/ParsingTests_Dependencies.kerml.xt`
- source_url: https://github.com/Systems-Modeling/SysML-v2-Pilot-Implementation/blob/fa709f28dfd49dfdb7ee83e4e19da2f57e0eb3aa/org.omg.kerml.xpect.tests/src/org/omg/kerml/xpect/tests/parsing/ParsingTests_Dependencies.kerml.xt
- source_bytes: 848
- source_sha256: `c2f88a04ba9053cf910f3d9ec6f52e633bf90f0281b22679d53b84c6785fb897`
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
package DependencyTest {
	
	package System {
		package 'Application Layer';
		package 'Service Layer';
		package 'Data Layer';
	}
	
	public import System::*;
	
	dependency Use from 'Application Layer' to 'Service Layer';
	dependency from 'Service Layer' to 'Data Layer';
	
	feature x;
	feature y;
	feature z;
	
	dependency z to x, y;
	
}

````
