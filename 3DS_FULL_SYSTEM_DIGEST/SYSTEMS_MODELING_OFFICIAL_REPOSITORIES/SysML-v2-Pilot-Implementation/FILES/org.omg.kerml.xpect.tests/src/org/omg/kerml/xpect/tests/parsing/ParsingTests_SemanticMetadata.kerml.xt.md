# OFFICIAL REPOSITORY FILE: SysML-v2-Pilot-Implementation/org.omg.kerml.xpect.tests/src/org/omg/kerml/xpect/tests/parsing/ParsingTests_SemanticMetadata.kerml.xt

- repository: `SysML-v2-Pilot-Implementation`
- source_path: `org.omg.kerml.xpect.tests/src/org/omg/kerml/xpect/tests/parsing/ParsingTests_SemanticMetadata.kerml.xt`
- source_url: https://github.com/Systems-Modeling/SysML-v2-Pilot-Implementation/blob/fa709f28dfd49dfdb7ee83e4e19da2f57e0eb3aa/org.omg.kerml.xpect.tests/src/org/omg/kerml/xpect/tests/parsing/ParsingTests_SemanticMetadata.kerml.xt
- source_bytes: 1543
- source_sha256: `ca621c7f60224c573c5ca7f8a37e96cfffa29623e51fad2fb02ad8d33818e60e`
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
            }
    	}
	}
END_SETUP
*/

// XPECT noErrors ---> ""
package SemanticMetadataTest {
    private import Metaobjects::SemanticMetadata;

    classifier P {
        feature a;
    }
    feature p : P;

    metaclass M :> SemanticMetadata {
        :>> baseType = p meta KerML::Feature;
    }

    classifier Q {
        feature a = 1;
        #M feature p1 {
        	// This feature should redefine P::a, not Q::a.
        	// Redefining Q::a will causes a feature value override error.
            feature :>> a = 2;
        }
    }
}
````
