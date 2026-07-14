# OFFICIAL REPOSITORY FILE: SysML-v2-Release/kerml/src/examples/Simple Tests/Dependencies.kerml

- repository: `SysML-v2-Release`
- source_path: `kerml/src/examples/Simple Tests/Dependencies.kerml`
- source_url: https://github.com/Systems-Modeling/SysML-v2-Release/blob/288d129c0d532065d45434bbb48a920898b719af/kerml/src/examples/Simple Tests/Dependencies.kerml
- source_bytes: 373
- source_sha256: `788df85bc513418ab4c57a47c039407a263a299b62ac8f4fe08be5d75307a346`
- decoded_as: `utf-8`


## EXACT SOURCE

````kerml
package Dependencies {
	
	package System {
		package 'Application Layer';
		package 'Service Layer';
		package 'Data Layer';
	}
	
	public import System::*;
	
	dependency Use from 'Application Layer' to 'Service Layer';
	dependency from 'Service Layer' to 'Data Layer';
	
	feature x;
	feature y;
	feature z;
	
	dependency z to x, y {
		feature e;
	}
	
}
````
