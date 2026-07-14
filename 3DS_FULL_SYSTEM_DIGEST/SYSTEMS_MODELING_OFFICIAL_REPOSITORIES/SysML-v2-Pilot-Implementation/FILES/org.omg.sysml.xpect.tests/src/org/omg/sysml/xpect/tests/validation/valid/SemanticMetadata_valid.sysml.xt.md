# OFFICIAL REPOSITORY FILE: SysML-v2-Pilot-Implementation/org.omg.sysml.xpect.tests/src/org/omg/sysml/xpect/tests/validation/valid/SemanticMetadata_valid.sysml.xt

- repository: `SysML-v2-Pilot-Implementation`
- source_path: `org.omg.sysml.xpect.tests/src/org/omg/sysml/xpect/tests/validation/valid/SemanticMetadata_valid.sysml.xt`
- source_url: https://github.com/Systems-Modeling/SysML-v2-Pilot-Implementation/blob/fa709f28dfd49dfdb7ee83e4e19da2f57e0eb3aa/org.omg.sysml.xpect.tests/src/org/omg/sysml/xpect/tests/validation/valid/SemanticMetadata_valid.sysml.xt
- source_bytes: 3123
- source_sha256: `b2826f8e4a5f1e8bd5e30633fb98b622ce105795f6d57518b992928e313f333b`
- decoded_as: `utf-8`


## EXACT SOURCE

````xtext
//* 
XPECT_SETUP org.omg.sysml.xpect.tests.validation.valid.SysMLTests
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
       	File {from ="/library.systems/Parts.sysml"}
        File {from ="/library.systems/Constraints.sysml"}
        File {from ="/library.systems/Requirements.sysml"}
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
		        File {from ="/library.systems/Parts.sysml"}
		        File {from ="/library.systems/Constraints.sysml"}
		        File {from ="/library.systems/Requirements.sysml"}
		       	File {from ="/library.systems/Metadata.sysml"}
		       	File {from ="/library.systems/SysML.sysml"}
			}
		}
	}
END_SETUP 
*/
// XPECT noErrors ---> ""
package SemanticMetadata_valid {
	public import Metaobjects::SemanticMetadata;

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
	
	#B def C1 {
		ref :>> x;
	}
	
	#B f1 {
		ref :>> x;
		ref :>> y;
	}
	
    requirement def G;
	requirement gs : G[*] nonunique;
	metadata def g :> SemanticMetadata {
	    :>> baseType = gs meta SysML::RequirementUsage;
	}
	
	requirement r1;
	#g requirement r2 {
		subject;
		actor #B a;
		assume #g constraint b;
		require #g r1;
	}
}

````
