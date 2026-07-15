# OFFICIAL REPOSITORY FILE: SysML-v2-Pilot-Implementation/kerml/src/examples/Behavior Examples/Camera.kerml

- repository: `SysML-v2-Pilot-Implementation`
- source_path: `kerml/src/examples/Behavior Examples/Camera.kerml`
- source_url: https://github.com/Systems-Modeling/SysML-v2-Pilot-Implementation/blob/fa709f28dfd49dfdb7ee83e4e19da2f57e0eb3aa/kerml/src/examples/Behavior Examples/Camera.kerml
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
