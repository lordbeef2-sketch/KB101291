# OFFICIAL REPOSITORY FILE: SysML-v2-Pilot-Implementation/org.omg.kerml.xpect.tests/src/org/omg/kerml/xpect/tests/parsing/ParsingTests_Metadata.kerml.xt

- repository: `SysML-v2-Pilot-Implementation`
- source_path: `org.omg.kerml.xpect.tests/src/org/omg/kerml/xpect/tests/parsing/ParsingTests_Metadata.kerml.xt`
- source_url: https://github.com/Systems-Modeling/SysML-v2-Pilot-Implementation/blob/fa709f28dfd49dfdb7ee83e4e19da2f57e0eb3aa/org.omg.kerml.xpect.tests/src/org/omg/kerml/xpect/tests/parsing/ParsingTests_Metadata.kerml.xt
- source_bytes: 1841
- source_sha256: `760af75e26fd060e1c8adf7290030e255fa12922bbc2b8aef0e24c88c5090fd5`
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
       	File {from ="/library/Performances.kerml"}
      	File {from ="/library/Metaobjects.kerml"}
        File {from ="/library/KerML.kerml"}
        File {from ="/library/BaseFunctions.kerml"}
        File {from ="/library/ControlFunctions.kerml"}
    }
    Workspace {
        JavaProject {
            SrcFolder {
		        ThisFile {}
				File {from ="/library/Base.kerml"}
				File {from ="/library/Links.kerml"}
		       	File {from ="/library/Occurrences.kerml"}
		       	File {from ="/library/Objects.kerml"}
		       	File {from ="/library/Performances.kerml"}
		      	File {from ="/library/Metaobjects.kerml"}
		        File {from ="/library/KerML.kerml"}
                File {from ="/library/BaseFunctions.kerml"}
                File {from ="/library/ControlFunctions.kerml"}
            }
    	}
	}
END_SETUP
*/

// XPECT noErrors ---> ""
package Metadata {
	
	metaclass A {
		feature f;
	}
	
	metaclass B;
	metaclass C;
	
	feature x {
		metaclass A {
			f = null;
		}
	}
	
	feature y {
		@A { f = null; }
		@B;
	}
	
	private #A #B feature z1;
	abstract #A z2;
	
	feature z {
		#A #B metadata C;
		#A #B @C;
	}
	
    class CC;
    struct SS {
        feature cc : CC;
    }
    
    metaclass M :> Metaobjects::SemanticMetadata {
      :>> annotatedElement : KerML::Class;
      :>> baseType = if annotatedElement istype KerML::Structure ? 
                         SS meta KerML::Type else CC meta KerML::Class;
    }
    
    #M struct T {
        feature :>> cc;
    }
}

````
