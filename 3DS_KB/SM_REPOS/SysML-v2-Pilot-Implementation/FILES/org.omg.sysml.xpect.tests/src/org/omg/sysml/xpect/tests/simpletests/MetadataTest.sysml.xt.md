# OFFICIAL REPOSITORY FILE: SysML-v2-Pilot-Implementation/org.omg.sysml.xpect.tests/src/org/omg/sysml/xpect/tests/simpletests/MetadataTest.sysml.xt

- repository: `SysML-v2-Pilot-Implementation`
- source_path: `org.omg.sysml.xpect.tests/src/org/omg/sysml/xpect/tests/simpletests/MetadataTest.sysml.xt`
- source_url: https://github.com/Systems-Modeling/SysML-v2-Pilot-Implementation/blob/fa709f28dfd49dfdb7ee83e4e19da2f57e0eb3aa/org.omg.sysml.xpect.tests/src/org/omg/sysml/xpect/tests/simpletests/MetadataTest.sysml.xt
- source_bytes: 2111
- source_sha256: `724f95aea9498ecf3b30698c3a5b6f8fa5ae5a6738e072af54e00647cb4085c4`
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
       	File {from ="/library.kernel/Performances.kerml"}
       	File {from ="/library.kernel/KerML.kerml"}
       	File {from ="/library.kernel/Metaobjects.kerml"}
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
		       	File {from ="/library.kernel/Occurrences.kerml"}
		       	File {from ="/library.kernel/Objects.kerml"}
		       	File {from ="/library.kernel/Performances.kerml"}
		       	File {from ="/library.kernel/Metaobjects.kerml"}
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
// XPECT noErrors ---> ""
package MetadataTest {
	public import 'User Defined Extensions'::*;
	
	library package 'User Defined Extensions' {
		
		#Security enum def ClassificationLevel {
			uncl;
			conf;
			#Security enum secret;
		}
		
		metadata def Classified {
			ref :>> annotatedElement : SysML::Usage;
			ref classificationLevel : ClassificationLevel;
		}
		
		metadata def Security;
	}
	
	ref x {
		metadata Classified {
			classificationLevel = ClassificationLevel::conf;
		}
	}
	
	ref y {
		@Classified {
			classificationLevel = ClassificationLevel::conf;
		}
		@Security;
	}
	
	private ref #Classified #Security z1;
	abstract #Classified z2;
	
	ref z {
	    #Security #Classified metadata Classified {
	        classificationLevel = ClassificationLevel::secret;
	    }
	}	
	
}
````
