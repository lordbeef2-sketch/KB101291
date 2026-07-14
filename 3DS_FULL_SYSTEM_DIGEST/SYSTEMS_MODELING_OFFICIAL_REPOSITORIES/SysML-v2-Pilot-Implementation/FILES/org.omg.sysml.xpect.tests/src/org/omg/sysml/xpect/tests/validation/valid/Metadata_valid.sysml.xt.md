# OFFICIAL REPOSITORY FILE: SysML-v2-Pilot-Implementation/org.omg.sysml.xpect.tests/src/org/omg/sysml/xpect/tests/validation/valid/Metadata_valid.sysml.xt

- repository: `SysML-v2-Pilot-Implementation`
- source_path: `org.omg.sysml.xpect.tests/src/org/omg/sysml/xpect/tests/validation/valid/Metadata_valid.sysml.xt`
- source_url: https://github.com/Systems-Modeling/SysML-v2-Pilot-Implementation/blob/fa709f28dfd49dfdb7ee83e4e19da2f57e0eb3aa/org.omg.sysml.xpect.tests/src/org/omg/sysml/xpect/tests/validation/valid/Metadata_valid.sysml.xt
- source_bytes: 3245
- source_sha256: `cad09d559824ba1b2832dd1dfe8f26bbebd0cba8b42d75739c65f297e7ecbb59`
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
       	File {from ="/library.systems/Actions.sysml"}
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
		        File {from ="/library.systems/Actions.sysml"}
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
package MetadataTest {
	public import 'User Defined Extensions'::*;
	
	library package 'User Defined Extensions' {
		
		enum def ClassificationLevel {
			uncl;
			conf;
			secret;
		}
		
		metadata def Classified {
			ref :>> annotatedElement : SysML::PartUsage;
			attribute classificationLevel : ClassificationLevel[1];
		}
		
		metadata def Security;
	}
	
	part x {
		metadata Classified {
			classificationLevel = ClassificationLevel::conf;
		}
		metadata Security;
	}
	
	part y {
		@Classified {
			classificationLevel = ClassificationLevel::conf;
		}
		@Security;
	}
	
	private #Classified #Security part z1;
	abstract #Security z2;
	
	#Security action a {
		#Security fork;
	}
	
}

````
