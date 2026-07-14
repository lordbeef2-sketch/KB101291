# OFFICIAL REPOSITORY FILE: SysML-v2-Pilot-Implementation/org.omg.kerml.xpect.tests/src/org/omg/kerml/xpect/tests/validation/MetadataTests_SemanticMetadata_invalid.kerml.xt

- repository: `SysML-v2-Pilot-Implementation`
- source_path: `org.omg.kerml.xpect.tests/src/org/omg/kerml/xpect/tests/validation/MetadataTests_SemanticMetadata_invalid.kerml.xt`
- source_url: https://github.com/Systems-Modeling/SysML-v2-Pilot-Implementation/blob/fa709f28dfd49dfdb7ee83e4e19da2f57e0eb3aa/org.omg.kerml.xpect.tests/src/org/omg/kerml/xpect/tests/validation/MetadataTests_SemanticMetadata_invalid.kerml.xt
- source_bytes: 1702
- source_sha256: `df285919aba15641f2cc58e22b9bf9ebd5c72dd52818e1e503aa26daf22a13c6`
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
       	File {from ="/library/Objects.kerml"}
      	File {from ="/library/Metaobjects.kerml"}
       	File {from ="/library/Performances.kerml"}
       	File {from ="/library/BaseFunctions.kerml"}
        File {from ="/library/KerML.kerml"}
	}
	Workspace {
		JavaProject {
			SrcFolder {
				ThisFile {}
				File {from ="/library/Base.kerml"}
				File {from ="/library/Links.kerml"}
		       	File {from ="/library/Occurrences.kerml"}
		       	File {from ="/library/Objects.kerml"}
		       	File {from ="/library/Metaobjects.kerml"}
		       	File {from ="/library/Performances.kerml"}
		       	File {from ="/library/BaseFunctions.kerml"}
		       	File {from ="/library/KerML.kerml"}
			}
		}
	}
END_SETUP 
*/
package SemanticMetadata_invalid {

	class C {
		feature x;
	}
	feature f : C {
		feature y;
	}

    abstract metaclass A :> Metaobjects::SemanticMetadata {
    	feature :>> baseType; // Testing that baseType can be left unbound.
    }
	
	metaclass B :> A {
		feature :>> baseType = f meta KerML::Type;
	}
	
	class C1 {
		// XPECT errors --> "Must have a concrete type" at "@A;"
		@A;
		// XPECT errors --> "Couldn't resolve reference to Feature 'x'." at "x"
		feature :>> x;
	}
	
	class C2 {
		@B;
		feature :>> x;
		// XPECT errors --> "Couldn't resolve reference to Feature 'y'." at "y"
		feature :>> y;
	}
	
	feature f1 {
		// XPECT errors --> "Must have a concrete type" at "@A;"
		@A;
	}
	
}

````
