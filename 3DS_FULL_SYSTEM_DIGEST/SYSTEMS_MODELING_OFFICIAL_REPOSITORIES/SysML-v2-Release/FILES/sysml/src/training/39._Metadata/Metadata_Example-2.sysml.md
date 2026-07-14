# OFFICIAL REPOSITORY FILE: SysML-v2-Release/sysml/src/training/39. Metadata/Metadata Example-2.sysml

- repository: `SysML-v2-Release`
- source_path: `sysml/src/training/39. Metadata/Metadata Example-2.sysml`
- source_url: https://github.com/Systems-Modeling/SysML-v2-Release/blob/288d129c0d532065d45434bbb48a920898b719af/sysml/src/training/39. Metadata/Metadata Example-2.sysml
- source_bytes: 678
- source_sha256: `bc2958a991dd80c87ce275a8cb8b51c61ebc6863b37a1d9dc197205103bc98e2`
- decoded_as: `utf-8`


## EXACT SOURCE

````sysml
package 'Metadata Example-2' {
	
	action computeDynamics {
		private import AnalysisTooling::*;
		
		metadata ToolExecution {
			toolName = "ModelCenter";
			uri = "aserv://localhost/Vehicle/Equation1";
		}
			
		in dt : ISQ::TimeValue             { @ToolVariable { name = "deltaT"; } }
		in a : ISQ::AccelerationValue      { @ToolVariable { name = "mass"; } }
		in v_in : ISQ::SpeedValue          { @ToolVariable { name = "v0"; } }
		in x_in : ISQ::LengthValue         { @ToolVariable { name = "x0"; } }
		
		out v_out : ISQ::SpeedValue        { @ToolVariable { name = "v"; } }
		out x_out : ISQ::LengthValue       { @ToolVariable { name = "x"; } }			
	}
	
}
````
