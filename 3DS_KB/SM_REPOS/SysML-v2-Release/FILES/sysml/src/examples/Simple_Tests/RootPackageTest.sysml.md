# OFFICIAL REPOSITORY FILE: SysML-v2-Release/sysml/src/examples/Simple Tests/RootPackageTest.sysml

- repository: `SysML-v2-Release`
- source_path: `sysml/src/examples/Simple Tests/RootPackageTest.sysml`
- source_url: https://github.com/Systems-Modeling/SysML-v2-Release/blob/288d129c0d532065d45434bbb48a920898b719af/sysml/src/examples/Simple Tests/RootPackageTest.sysml
- source_bytes: 150
- source_sha256: `082e3b068cab5aa63b4ba6e1ab4fd58dcadebc4fa327000a81cfe363dd8b2a72`
- decoded_as: `utf-8`


## EXACT SOURCE

````sysml
package P1 {
	part def A;
}

package P2 {
	private import P1::*;
	part a : A;
}

private import P2::*;

package P3 {
	part b subsets a;
}
````
