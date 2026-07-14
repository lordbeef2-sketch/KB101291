# OFFICIAL REPOSITORY FILE: SysML-v2-Pilot-Implementation/kerml/src/examples/Behavior Examples/TakePicture.kerml

- repository: `SysML-v2-Pilot-Implementation`
- source_path: `kerml/src/examples/Behavior Examples/TakePicture.kerml`
- source_url: https://github.com/Systems-Modeling/SysML-v2-Pilot-Implementation/blob/fa709f28dfd49dfdb7ee83e4e19da2f57e0eb3aa/kerml/src/examples/Behavior Examples/TakePicture.kerml
- source_bytes: 428
- source_sha256: `522901e1bbbf80e650c0015a943e953f5cc4f268e50f7c1c78fdd81565a03410`
- decoded_as: `utf-8`


## EXACT SOURCE

````kerml
behavior TakePicture {
	private import Camera;
	
	feature camera: Camera[1] subsets involvedObjects;
	
	class Exposure;
	
	behavior Focus { out xrsl: Exposure; }
	behavior Shoot { in xsf: Exposure; }
	
	step step1: Focus[1];	
	step step2: Shoot[1];
	
	succession flow exposure[1] of Exposure from step1.xrsl to step2.xsf;

	succession step1 then camera.focusedState;
	succession step2 then camera.shotState;
}

````
