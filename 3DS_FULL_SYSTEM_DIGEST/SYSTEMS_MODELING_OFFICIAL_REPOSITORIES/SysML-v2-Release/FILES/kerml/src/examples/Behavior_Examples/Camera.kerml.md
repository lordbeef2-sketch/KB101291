# OFFICIAL REPOSITORY FILE: SysML-v2-Release/kerml/src/examples/Behavior Examples/Camera.kerml

- repository: `SysML-v2-Release`
- source_path: `kerml/src/examples/Behavior Examples/Camera.kerml`
- source_url: https://github.com/Systems-Modeling/SysML-v2-Release/blob/288d129c0d532065d45434bbb48a920898b719af/kerml/src/examples/Behavior Examples/Camera.kerml
- source_bytes: 198
- source_sha256: `b5e3d23f35f58099f8d855ba0812d6e300f1aa9626b3b476fc796637f88daa01`
- decoded_as: `utf-8`


## EXACT SOURCE

````kerml
class Camera {
	private import ScalarValues::*;
	
	portion focusedState: Camera subsets timeSlices;
	portion shotState: Camera subsets timeSlices;
	
	succession focusedState then shotState;
}
````
