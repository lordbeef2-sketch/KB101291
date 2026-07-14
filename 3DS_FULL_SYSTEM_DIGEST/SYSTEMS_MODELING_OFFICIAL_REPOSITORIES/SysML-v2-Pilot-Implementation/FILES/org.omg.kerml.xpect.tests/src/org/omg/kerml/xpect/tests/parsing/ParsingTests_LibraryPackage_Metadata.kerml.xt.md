# OFFICIAL REPOSITORY FILE: SysML-v2-Pilot-Implementation/org.omg.kerml.xpect.tests/src/org/omg/kerml/xpect/tests/parsing/ParsingTests_LibraryPackage_Metadata.kerml.xt

- repository: `SysML-v2-Pilot-Implementation`
- source_path: `org.omg.kerml.xpect.tests/src/org/omg/kerml/xpect/tests/parsing/ParsingTests_LibraryPackage_Metadata.kerml.xt`
- source_url: https://github.com/Systems-Modeling/SysML-v2-Pilot-Implementation/blob/fa709f28dfd49dfdb7ee83e4e19da2f57e0eb3aa/org.omg.kerml.xpect.tests/src/org/omg/kerml/xpect/tests/parsing/ParsingTests_LibraryPackage_Metadata.kerml.xt
- source_bytes: 1757
- source_sha256: `673307eaffd82d486776c301488f827315d56720bac2cdb2394f8e53b2378f69`
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
       	File {from ="/library/ScalarValues.kerml"}
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
		       	File {from ="/library/ScalarValues.kerml"}
		       	File {from ="/library/KerML.kerml"}
			}
		}
	}
END_SETUP 
*/
// XPECT noErrors ---> ""
package MetadataTest {
	public import 'User Defined Extensions'::*;
	
	library package 'User Defined Extensions' {
		
		datatype ClassificationLevel :> ScalarValues::Natural;
		feature uncl[1] : ClassificationLevel = 0;
		feature conf[1] : ClassificationLevel = 1;
		feature secret[1] : ClassificationLevel = 2;
		
		metaclass Classified {
			feature :>> annotatedElement : KerML::Feature;
			feature classificationLevel : ClassificationLevel;
		}
		
		metaclass Security;
	}
	
	feature x {
		metadata Classified {
			classificationLevel = conf;
		}
		metadata Security;
	}
	
	feature y {
		@Classified {
			classificationLevel = conf;
		}
		@Security;
	}
	
	private #Classified #Security feature z1;
	abstract #Classified z2;
	
}
````
