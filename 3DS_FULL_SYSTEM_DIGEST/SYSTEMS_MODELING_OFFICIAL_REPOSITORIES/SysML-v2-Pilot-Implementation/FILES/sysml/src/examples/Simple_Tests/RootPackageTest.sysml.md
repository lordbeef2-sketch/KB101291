# OFFICIAL REPOSITORY FILE: SysML-v2-Pilot-Implementation/sysml/src/examples/Simple Tests/RootPackageTest.sysml

- repository: `SysML-v2-Pilot-Implementation`
- source_path: `sysml/src/examples/Simple Tests/RootPackageTest.sysml`
- source_url: https://github.com/Systems-Modeling/SysML-v2-Pilot-Implementation/blob/fa709f28dfd49dfdb7ee83e4e19da2f57e0eb3aa/sysml/src/examples/Simple Tests/RootPackageTest.sysml
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
