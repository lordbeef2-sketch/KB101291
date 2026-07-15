# OFFICIAL REPOSITORY FILE: SysML-v2-Pilot-Implementation/org.omg.sysml.xpect.tests/src/org/omg/sysml/xpect/tests/simpletests/AnnotationTest.sysml.xt

- repository: `SysML-v2-Pilot-Implementation`
- source_path: `org.omg.sysml.xpect.tests/src/org/omg/sysml/xpect/tests/simpletests/AnnotationTest.sysml.xt`
- source_url: https://github.com/Systems-Modeling/SysML-v2-Pilot-Implementation/blob/fa709f28dfd49dfdb7ee83e4e19da2f57e0eb3aa/org.omg.sysml.xpect.tests/src/org/omg/sysml/xpect/tests/simpletests/AnnotationTest.sysml.xt
- source_bytes: 2168
- source_sha256: `88ac07a7abdde0e80c7edf5fa6e7bb6600727296b8fac0d4ef3fb8a4f5fa80c1`
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
		File {from ="/library.kernel/Metaobjects.kerml"}
		File {from ="/library.kernel/Performances.kerml"}
		File {from ="/library.kernel/ScalarValues.kerml"}
		File {from ="/library.systems/Items.sysml"}
        File {from ="/library.systems/Metadata.sysml"}
		File {from ="/library.systems/Actions.sysml"}
		File {from ="/library.domain/Analysis/AnalysisTooling.sysml"}
	}
	Workspace {
		JavaProject {
			SrcFolder {
				ThisFile {}
				File {from ="/library.kernel/Base.kerml"}
				File {from ="/library.kernel/Occurrences.kerml"}
				File {from ="/library.kernel/Objects.kerml"}
				File {from ="/library.kernel/Metaobjects.kerml"}
				File {from ="/library.kernel/Performances.kerml"}
				File {from ="/library.kernel/ScalarValues.kerml"}
				File {from ="/library.systems/Items.sysml"}
                File {from ="/library.systems/Metadata.sysml"}
				File {from ="/library.systems/Actions.sysml"}
				File {from ="/library.domain/Analysis/AnalysisTooling.sysml"}
			}
		}
	}
END_SETUP 
*/
// XPECT noErrors ---> ""
package AnalysisAnnotation {
	public import ScalarValues::Real;
	public import AnalysisTooling::*;
	
	action def ComputeDynamics {
		metadata ToolExecution {
			toolName = "ModelCenter";
			uri = "aserv://localhost/Vehicle/Equation1";
		}
			
		in dt : Real          { @ToolVariable { name = "deltaT"; } }
		in whlpwr : Real      { @ToolVariable { name = "power"; } }
		in Cd : Real          { @ToolVariable { name = "C_D"; } }
		in Cf : Real          { @ToolVariable { name = "C_F"; } }
		in tm : Real          { @ToolVariable { name = "mass"; } }
		in v_in : Real        { @ToolVariable { name = "v0"; } }
		in x_in : Real        { @ToolVariable { name = "x0"; } }
		
		out a_out : Real      { @ToolVariable { name = "a"; } }
		out v_out : Real      { @ToolVariable { name = "v"; } }
		out x_out : Real      { @ToolVariable { name = "x"; } }
			
	}

}
````
