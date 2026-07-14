# OFFICIAL REPOSITORY FILE: SysML-v2-Pilot-Implementation/org.omg.kerml.xpect.tests/src/org/omg/kerml/xpect/tests/parsing/ParsingTests_Associations.kerml.xt

- repository: `SysML-v2-Pilot-Implementation`
- source_path: `org.omg.kerml.xpect.tests/src/org/omg/kerml/xpect/tests/parsing/ParsingTests_Associations.kerml.xt`
- source_url: https://github.com/Systems-Modeling/SysML-v2-Pilot-Implementation/blob/fa709f28dfd49dfdb7ee83e4e19da2f57e0eb3aa/org.omg.kerml.xpect.tests/src/org/omg/kerml/xpect/tests/parsing/ParsingTests_Associations.kerml.xt
- source_bytes: 1563
- source_sha256: `fea5e39d4129b0c6b2938d00e1c3d249f8633b98a0307a20b51bb4d6415ea522`
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
        File {from ="/library/Performances.kerml"}
        File {from ="/library/Objects.kerml"}
        File {from ="/library/Metaobjects.kerml"}
	}
	Workspace {
		JavaProject {
			SrcFolder {
				ThisFile {}
				File {from ="/library/Base.kerml"}
				File {from ="/library/Links.kerml"}
				File {from ="/library/Occurrences.kerml"}
				File {from ="/library/Performances.kerml"}
				File {from ="/library/Objects.kerml"}
                File {from ="/library/Metaobjects.kerml"}
			}
		}
	}
END_SETUP 
*/

// XPECT noErrors ---> ""
package Associations {
    datatype X;
    class Y;
    
    assoc A {
        end x_cross [1..1] feature x : X; 
        end y_cross [1..*] feature y : Y;
    }
    
    assoc B specializes A {
        end x1;
        end [0..*] feature y1 redefines y;
    }
    
    assoc struct C {
        const end [1] feature a;
        const end feature b;
    }
    
    metaclass M;    
    assoc XY {
        // Ensure that the owned cross feature is typed correctly,
        // even though getting type of end feature requires resolving
        // metadata nam to check if it is SemanticMetadata, which 
        // requires getting supertypes of end feature, including its types.
        end [0..1] #M feature x : X;
        end [0..1] #M feature y : Y;
    }
}
````
