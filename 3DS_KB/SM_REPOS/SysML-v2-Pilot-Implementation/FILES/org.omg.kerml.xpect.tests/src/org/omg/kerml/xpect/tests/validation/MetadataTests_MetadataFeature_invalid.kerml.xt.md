# OFFICIAL REPOSITORY FILE: SysML-v2-Pilot-Implementation/org.omg.kerml.xpect.tests/src/org/omg/kerml/xpect/tests/validation/MetadataTests_MetadataFeature_invalid.kerml.xt

- repository: `SysML-v2-Pilot-Implementation`
- source_path: `org.omg.kerml.xpect.tests/src/org/omg/kerml/xpect/tests/validation/MetadataTests_MetadataFeature_invalid.kerml.xt`
- source_url: https://github.com/Systems-Modeling/SysML-v2-Pilot-Implementation/blob/fa709f28dfd49dfdb7ee83e4e19da2f57e0eb3aa/org.omg.kerml.xpect.tests/src/org/omg/kerml/xpect/tests/validation/MetadataTests_MetadataFeature_invalid.kerml.xt
- source_bytes: 2797
- source_sha256: `a025eb7177f36a4ef56572272e596de3c5f6670dc6ae300e615bc746ee9198b6`
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
       	File {from ="/library/BaseFunctions.kerml"}
       	File {from ="/library/DataFunctions.kerml"}
       	File {from ="/library/ScalarFunctions.kerml"}
       	File {from ="/library/ControlFunctions.kerml"}
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
		       	File {from ="/library/BaseFunctions.kerml"}
		       	File {from ="/library/DataFunctions.kerml"}
		       	File {from ="/library/ScalarFunctions.kerml"}
		       	File {from ="/library/ControlFunctions.kerml"}
		       	File {from ="/library/KerML.kerml"}
			}
		}
	}
END_SETUP 
*/
package MetadataFeatureTest {
	
	metaclass A {
		feature :>> annotatedElement : KerML::Feature;
		feature x : ScalarValues::Integer;
		feature y : ScalarValues::String;
		feature z : ScalarValues::Boolean;
		feature u {
			feature v : ScalarValues::Integer;
		}
	}
	
	function f { in x; return : ScalarValues::Boolean; }
	
	// XPECT errors --> "Must be model-level evaluable" at "filter f((as A).y);"
	filter f((as A).y);
	// XPECT errors --> "Must be model-level evaluable" at "filter ~(as A).z;"
	filter ~(as A).z;
	// XPECT errors --> "Must be model-level evaluable" at "filter (as A).y->ControlFunctions::collect {in x; x};"
	filter (as A).y->ControlFunctions::collect {in x; x};
	// XPECT errors --> "Must have a Boolean result" at "filter new A(null, 1, "", false);"
	filter new A(null, 1, "", false);
	
	feature bad;
	
	feature a {
		@A {
			// XPECT errors --> "Must be model-level evaluable" at "= ~3"
			x = ~3;
			y = "e";
			// XPECT errors --> "Must be model-level evaluable" at "= f((as A).y)"
			z = f((as A).y);
			u {
				v = 1;
				// XPECT errors --> "Must redefine an owning-type feature" at "bad;"
				bad;
			}		
		}
	}
	
	classifier B {
		// XPECT errors --> "Cannot annotate Classifier" at "@A;"
		@A;
		// XPECT errors --> "Must have a concrete type" at "@Metaobjects::Metaobject;"
		@Metaobjects::Metaobject;
	}
	
}

````
