# OFFICIAL REPOSITORY FILE: SysML-v2-Pilot-Implementation/org.omg.sysml.xpect.tests/src/org/omg/sysml/xpect/tests/validation/invalid/SemanticMetadata_invalid.sysml.xt

- repository: `SysML-v2-Pilot-Implementation`
- source_path: `org.omg.sysml.xpect.tests/src/org/omg/sysml/xpect/tests/validation/invalid/SemanticMetadata_invalid.sysml.xt`
- source_url: https://github.com/Systems-Modeling/SysML-v2-Pilot-Implementation/blob/fa709f28dfd49dfdb7ee83e4e19da2f57e0eb3aa/org.omg.sysml.xpect.tests/src/org/omg/sysml/xpect/tests/validation/invalid/SemanticMetadata_invalid.sysml.xt
- source_bytes: 2746
- source_sha256: `e7046605bfe897346efc0b65d4f9db385940c6ce920bd132977607a270675afc`
- decoded_as: `utf-8`


## EXACT SOURCE

````xtext
//* 
XPECT_SETUP org.omg.sysml.xpect.tests.validation.invalid.SysMLTests
	ResourceSet {
		ThisFile {}
		File {from ="/library.kernel/Base.kerml"}
		File {from ="/library.kernel/Links.kerml"}
       	File {from ="/library.kernel/Occurrences.kerml"}
       	File {from ="/library.kernel/Objects.kerml"}
       	File {from ="/library.kernel/Metaobjects.kerml"}
       	File {from ="/library.kernel/Performances.kerml"}
       	File {from ="/library.kernel/ScalarValues.kerml"}
       	File {from ="/library.kernel/BaseFunctions.kerml"}
       	File {from ="/library.kernel/DataFunctions.kerml"}
       	File {from ="/library.kernel/ScalarFunctions.kerml"}
       	File {from ="/library.kernel/ControlFunctions.kerml"}
       	File {from ="/library.kernel/KerML.kerml"}
       	File {from ="/library.systems/Attributes.sysml"}
       	File {from ="/library.systems/Items.sysml"}
       	File {from ="/library.systems/Metadata.sysml"}
       	File {from ="/library.systems/SysML.sysml"}
	}
	Workspace {
		JavaProject {
			SrcFolder {
				ThisFile {}
				File {from ="/library.kernel/Base.kerml"}
				File {from ="/library.kernel/Links.kerml"}
		       	File {from ="/library.kernel/Occurrences.kerml"}
		       	File {from ="/library.kernel/Objects.kerml"}
		       	File {from ="/library.kernel/Metaobjects.kerml"}
		       	File {from ="/library.kernel/Performances.kerml"}
		       	File {from ="/library.kernel/ScalarValues.kerml"}
		       	File {from ="/library.kernel/BaseFunctions.kerml"}
		       	File {from ="/library.kernel/DataFunctions.kerml"}
		       	File {from ="/library.kernel/ScalarFunctions.kerml"}
		       	File {from ="/library.kernel/ControlFunctions.kerml"}
		       	File {from ="/library.kernel/KerML.kerml"}
		       	File {from ="/library.systems/Attributes.sysml"}
		       	File {from ="/library.systems/Items.sysml"}
       			File {from ="/library.systems/Metadata.sysml"}
		       	File {from ="/library.systems/SysML.sysml"}
			}
		}
	}
END_SETUP 
*/
package SemanticMetadata_invalid {

	item def C {
		ref x;
	}
	item f : C {
		ref y;
	}

    abstract metadata def A :> Metaobjects::SemanticMetadata {
    	ref :>> baseType; // Testing that baseType can be left unbound.
    }
	
	metadata def B :> A {
		ref :>> baseType = f meta SysML::Usage;
	}
	
	item def C1 {
		// XPECT errors --> "Must have a concrete type" at "@A;"
		@A;
		// XPECT errors --> "Couldn't resolve reference to Feature 'x'." at "x"
		ref :>> x;
	}
	
	item def C2 {
		@B;
		ref :>> x;
		// XPECT errors --> "Couldn't resolve reference to Feature 'y'." at "y"
		ref :>> y;
	}
	
	item f1 {
		// XPECT errors --> "Must have a concrete type" at "@A;"
		@A;
	}
	
}

````
