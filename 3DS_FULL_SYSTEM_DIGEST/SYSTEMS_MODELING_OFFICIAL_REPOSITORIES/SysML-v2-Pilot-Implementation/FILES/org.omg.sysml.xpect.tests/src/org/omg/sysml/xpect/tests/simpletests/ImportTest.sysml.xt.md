# OFFICIAL REPOSITORY FILE: SysML-v2-Pilot-Implementation/org.omg.sysml.xpect.tests/src/org/omg/sysml/xpect/tests/simpletests/ImportTest.sysml.xt

- repository: `SysML-v2-Pilot-Implementation`
- source_path: `org.omg.sysml.xpect.tests/src/org/omg/sysml/xpect/tests/simpletests/ImportTest.sysml.xt`
- source_url: https://github.com/Systems-Modeling/SysML-v2-Pilot-Implementation/blob/fa709f28dfd49dfdb7ee83e4e19da2f57e0eb3aa/org.omg.sysml.xpect.tests/src/org/omg/sysml/xpect/tests/simpletests/ImportTest.sysml.xt
- source_bytes: 1133
- source_sha256: `4cf826bc90358d8367041e0235452079053702d082f49177220fc35a0098f817`
- decoded_as: `utf-8`


## EXACT SOURCE

````xtext
//* 
XPECT_SETUP org.omg.sysml.xpect.tests.simpletests.SysMLTests
	ResourceSet {
		ThisFile {}
		File {from ="/library.kernel/Base.kerml"}
       	File {from ="/library.kernel/Occurrences.kerml"}
       	File {from ="/library.kernel/Objects.kerml"}
 		File {from ="/library.systems/Items.sysml"}
 		File {from ="/library.systems/Parts.sysml"}
	}
	Workspace {
		JavaProject {
			SrcFolder {
				ThisFile {}
				File {from ="/library.kernel/Base.kerml"}
		       	File {from ="/library.kernel/Occurrences.kerml"}
		       	File {from ="/library.kernel/Objects.kerml"}
				File {from ="/library.systems/Items.sysml"}
				File {from ="/library.systems/Parts.sysml"}
			}
		}
	}
END_SETUP 
*/
// XPECT noErrors ---> ""
package ImportTest {
    package Pkg1 {
    	public import Pkg2::Pkg21::Pkg211::P211;
    	public import Pkg2::Pkg21::*;
    	public import Pkg211::*::**;
        part p11 : Pkg211::P211;
        part def P12;
    }

    package Pkg2 {
        public import Pkg1::*;
        package Pkg21 {
        	package Pkg211 {
        		part def P211 :> P12;
        	}
        }
    }
}
````
