# OFFICIAL REPOSITORY FILE: SysML-v2-Release/sysml/src/examples/Camera Example/PictureTaking.sysml

- repository: `SysML-v2-Release`
- source_path: `sysml/src/examples/Camera Example/PictureTaking.sysml`
- source_url: https://github.com/Systems-Modeling/SysML-v2-Release/blob/288d129c0d532065d45434bbb48a920898b719af/sysml/src/examples/Camera Example/PictureTaking.sysml
- source_bytes: 272
- source_sha256: `2fc31c25a62bcaff412248aaeb72aef7d956da9b0e427da78c8a3c160fd78fe5`
- decoded_as: `utf-8`


## EXACT SOURCE

````sysml
package PictureTaking {
	part def Exposure;
	
	action def Focus { out xrsl: Exposure; }
	action def Shoot { in xsf: Exposure; }	
		
	action takePicture {		
		action focus: Focus[1];
		flow of Exposure from focus.xrsl to shoot.xsf;
		action shoot: Shoot[1];
	}
}
````
